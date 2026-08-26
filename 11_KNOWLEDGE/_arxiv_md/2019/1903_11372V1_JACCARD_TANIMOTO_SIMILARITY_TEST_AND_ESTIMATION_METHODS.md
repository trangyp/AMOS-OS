---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1903.11372v1
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 1903.11372v1_Jaccard_Tanimoto_similarity_test_and_estimation_methods

> Source: 1903.11372v1_Jaccard_Tanimoto_similarity_test_and_estimation_methods.pdf

> Pages: 19

---


## Page 1


Jaccard/Tanimoto similarity test
and estimation methods
Neo Christopher Chung1,*, Błażej Miasojedow2, Michał Startek1, Anna Gambin1
1Institute of Informatics, University of Warsaw
2Institute of Mathematics, Polish Academy of Sciences
*nchchung@gmail.com
A survey of presences and absences of speciﬁc species across multiple biogeo-
graphic units (or bioregions) are used in a broad area of biological studies from
ecology to microbiology. Using binary presence-absence data, we evaluate species
co-occurrences that help elucidate relationships among organisms and environments.
To summarize similarity between occurrences of species, we routinely use the Jac-
card/Tanimoto coeﬃcient, which is the ratio of their intersection to their union. It
is natural, then, to identify statistically signiﬁcant Jaccard/Tanimoto coeﬃcients,
which suggest non-random co-occurrences of species. However, statistical hypothesis
testing using this similarity coeﬃcient has been seldom used or studied.
We introduce a hypothesis test for similarity for biological presence-absence data,
using the Jaccard/Tanimoto coeﬃcient. Several key improvements are presented
including unbiased estimation of expectation and centered Jaccard/Tanimoto coef-
ﬁcients, that account for occurrence probabilities. The exact and asymptotic solu-
tions are derived. To overcome a computational burden due to high-dimensionality,
we propose the bootstrap and measurement concentration algorithms to eﬃciently
estimate statistical signiﬁcance of binary similarity. Simulation studies demonstrate
that our proposed methods produce accurate p-values and false discovery rates. The
proposed estimation methods are orders of magnitude faster than the exact solu-
tion, particularly with an increasing dimensionality. We showcase their application
in evaluating co-occurrences of bird species in 28 islands of Vanuatu and ﬁsh species
in 3347 freshwater habitats in France. The proposed methods are implemented in
a R package called jaccard (https://cran.r-project.org/package=jaccard).
We introduce a suite of statistical methods for the Jaccard/Tanimoto similarity
coeﬃcient, that enable straightforward incorporation of probabilistic measures in
analysis for species co-occurrences. Due to their generality, the proposed methods
and implementations are applicable to a wide range of binary data arising from
genomics, biochemistry, and other areas of science.
Keyword: Jaccard, Tanimoto, binary similarity, hypothesis test, co-occurrences, p-value
Funding: Narodowe Centrum Nauki 2014/12/W/ST5/00592 and 2016/23/D/ST6/03613
1
arXiv:1903.11372v1  [stat.ME]  27 Mar 2019


## Page 2


Page 2 of 19
Background
Analysis of species co-occurrences helps us understand ecological and biological rela-
tionships among species. Essentially, the presence (1) and absence (0) of species are
surveyed in multiple biogeographic units (or bioregions) using ﬁeldwork, imaging,
sequencing, and other techniques. Then, the Jaccard/Tanimoto coeﬃcient is one of
the most fundamental and popular similarity measures to compare such biological
presence-absence data. Given two presence-absence vectors yi and yj of length m
that represent two diﬀerent species, the Jaccard/Tanimoto similarity coeﬃcient is
the ratio of their intersection to their union, T(yi, yj) = yi ∩yj/yi ∪yj [1, 2]. This
quantiﬁcation of overlaps allows us to quantify co-existence of species [3, 4, 5, 6].
However, the Jaccard/Tanimoto coeﬃcient lacks probabilistic interpretations or sta-
tistical error controls. Surprisingly, its statistical properties, hypothesis testing, and
estimation methods for p-values have been inadequately studied. Here, we present
a rigorous statistical test evaluating the similarity in presence-absence data, de-
rive exact and asymptotic solutions, and introduce eﬃcient estimation methods for
signiﬁcance of the Jaccard/Tanimoto similarity coeﬃcient.
Generally, analysis of co-occurrences enables us to distinguish generalist species
that survive in a broad range of environments from specialists that only thrive in
a few localities [7, 8]. Alternatively, similarity between two localities – how two
biogeographic units share an overlapping set of species – sheds light on the beta
diversity that may arise from ecological processes over time [9, 10, 11]. There has
been a long standing discussion on how to conduct association analysis for oc-
currences of species, including appropriate null models and evaluation techniques
[12, 13, 14, 15, 16, 17]. There are also specialized probabilistic approaches, including
metrics related to the Jaccard/Tanimoto coeﬃcient [18, 19, 20, 21]. Yet, these stud-
ies rarely utilized statistical signiﬁcance. Therefore, we investigated a hypothesis
test using the Jaccard/Tanimoto coeﬃcient that underlies or accompanies most of
such association analyses.
The Jaccard/Tanimoto coeﬃcient measuring similarity between two species has
long been used to evaluate co-occurrences between species or between biogeographic
units [22, 23, 3, 4, 5, 24]. Pioneering early works on probabilistic treatment of the
Jaccard/Tanimoto coeﬃcient assume that the probability of species occurrences
is 0.5 [22, 23, 5]. These can be seen as special cases of our methods where both
probabilities of yi and yj are set to 0.5. Recently, [24] and [25] proposed estimat-
ing p-values with combinatorics and hypergeometric distributions, respectively. We
found that they are inaccurate. To provide a comprehensive statistical treatment, we
have developed a suite of methods and estimation techniques for rigorously testing
similarity between presence-absence data.
We derive a hypothesis test from the ﬁrst principles using the Jaccard/Tanimoto
coeﬃcient. In the process, we propose an unbiased estimation of expectation and
a centered Jaccard/Tanimoto coeﬃcient that accounts for diﬀerent probabilities
of species occurrences. The negative and positive values of the centered Jac-
card/Tanimoto coeﬃcient naturally correspond to negative and positive association.
We introduce an exact distribution of Jaccard/Tanimoto similarity coeﬃcients un-
der independence that is shown to provide accurate p-values. Because the exact
solution for a large m is computationally expensive, we have developed two eﬃcient


## Page 3


Page 3 of 19
and accurate estimation algorithms. We demonstrate their remarkable accuracy
and computational eﬃciency in comprehensive simulation studies, where p-values
and false discovery rates (FDRs) are evaluated. As applications, we evaluated co-
occurrences of bird species from m = 28 islands of Vanuatu and of ﬁsh species from
m = 3347 freshwater habitats in France.
All proposed methods are implemented in a statistical programming language
R [26], available on the Comprehensive R Archive Network (https://cran.
r-project.org/package=jaccard). We additionally provide an interactive web
app (https://nnnn.shinyapps.io/jaccard). The implementations are eﬃcient
and general, such that the jaccard package can rigorously test similarity between
binary data arising from genomics, biochemistry, and others.
Methods
Statistical Model and Test
Quantitative comparison of presence-absence data in ecology and biology plays a
crucial role in evaluating species co-existences, biodiversities, and ecosystems. In
particular, one may be interested in comparing how species are co-occurring in bio-
geographic units or how biogeographic units are occupied by certain species. Note
that species are used generally to indicate groups of organisms under investiga-
tions, such as operational taxonomic units (OTUs); similarly, biogeographic units
or bioregions could be distinct survey areas, islands, or habitats. We are interested
in statistically testing similarity between a pair of presence-absence data.
Given two presence-absence vectors yi and yj of length m, we are interested in
inferring whether they are signiﬁcantly related. Consider presence (1) and absence
(0) of two species are recorded at m biogeographic units. We measure their similarity
by the ratio of their intersection to their union, T(yi, yj) = yi ∩yj/yi ∪yj. This is
well known as the Jaccard/Tanimoto index or similarity coeﬃcient [1, 2]. In order to
utilize the Jaccard/Tanimoto similarity coeﬃcient in a statistically rigorous manner,
we propose a family of methods and algorithms (Figure 1).
Under the null model of independence, yi and yj are assumed to be independent
and identically distributed (i.i.d.). They are modeled by a Bernoulli distribution,
with corresponding occurrence (i.e., success) probabilities pi and pj ∈[0, 1]. Specif-
ically, for k = 1, . . . , m, yi,k ∼i.i.d. Bernoulli(pi) and yj,k ∼i.i.d. Bernoulli(pj). Be-
cause this conventional deﬁnition is undeﬁned if both binary vectors contain only
zeros such that yi ∪yj = 0, we reﬁne the deﬁnition of Jaccard/Tanimoto coeﬃcient
T(yi, yj) =



yi∩yj
yi∪yj
if yi ∪yj ̸= 0
pipj
pi+pj−pipj
otherwise.
(1)
Following the deﬁnition of Jaccard/Tanimoto similarity coeﬃcient in Eq. (1),
we derive its expected value E[T(yi, yj)] =
pipj
pi+pj−pipj . Substantial deviation from
the expected value signiﬁes similarity. Note that the Jaccard/Tanimoto coeﬃcient
can also be deﬁned in terms of a multinomial distribution with four categories
and m trials (for example, representing m biogeographic units). Four categories
arising from presence-absence data are N1 = yi ∩yj, N2 = yi ∩(1 −yj), N3 =


## Page 4


Page 4 of 19
(1−yi)∩yj and N4 = m−N1 −N2 −N3. From pi and pj, probabilities of those four
categories are pipj, pi(1 −pj), (1 −pi)pj and (1 −pi)(1 −pj), respectively. Putting
them together, N = (N1, N2, N3, N4) is distributed according to a multinomial
distribution, Multi(m, pipj, pi(1 −pj), (1 −pi)pj, (1 −pi)(1 −pj)).
Proposition 1
If yi and yj are independent, then
E(T(yi, yj)) =
pipj
pi + pj −pipj
.
Proof First, we compute conditional expectation given N1 + N2 + N3. We observe
that N1|N1 + N2 + N3 follows Bernoulli(N1 + N2 + N3,
pipj
pi+pj−pipj ). Hence, on set
N1 + N2 + N3 > 0, we have
E(T(yi, yj)|N1 + N2 + N3) = E

N1
N1 + N2 + N3
|N1 + N2 + N3

= E(N1|N1 + N2 + N3)
N1 + N2 + N3
=
pipj
pi+pj−pipj (N1 + N2 + N3)
N1 + N2 + N3
=
pipj
pi + pj −pipj
and on set N1 + N2 + N3 = 0, we have
E(T(yi, yj)|N1 + N2 + N3) =
pipj
pi + pj −pipj
Therefore,
E(T(yi, yj)) = E[E(T(yi, yj)|N1 + N2 + N3)]
=
pipj
pi + pj −pipj
P(N1 + N2 + N3 = 0)
+
pipj
pi + pj −pipj
P(N1 + N2 + N3 > 0)
=
pipj
pi + pj −pipj
.
This allows us to deﬁne the centered Jaccard/Tanimoto coeﬃcient as
T c(yi, yj) = T(yi, yj) −E[T(yi, yj)]
(2)
This accounts for expected values, naturally distinguishing negative and positive
associations. Generally, we would like to measure the deviation of an observed co-
eﬃcient from an expected value, instead of simply looking at a magnitude of an
observed statistics. Furthermore, this centered coeﬃcient may be scaled by vari-
ance in order to span a pre-deﬁned range.


## Page 5


Page 5 of 19
To evaluate whether yi and yj are independent, a following statistical hypothesis
testing is performed:
H0 : T c(yi, yj) = 0
H1 : T c(yi, yj) ̸= 0.
(3)
The null hypothesis H0 is that the centered Jaccard/Tanimoto coeﬃcient equals
zero. Note that this is equivalent to that the conventional (uncentered) Jac-
card/Tanimoto coeﬃcient equals an expected value under independence. Therefore,
although we propose and use the centered coeﬃcient, this hypothesis testing is
attributed to both uncentered and centered versions. Then, a p-value indicates a
probability of observing a coeﬃcient equal to or more extreme than an observed
coeﬃcient under the null hypothesis.
Distribution of the Jaccard/Tanimoto Coeﬃcient
To obtain its p-value, we derive the distribution of Jaccard/Tanimoto coeﬃcient
under the null hypothesis. In terms of N = (N1, N2, N3, N4), the Jaccard/Tanimoto
coeﬃcient can be expressed as
T(yi, yj) =



N1
N1+N2+N3
if N1 + N2 + N3 > 0
pipj
pi+pj−pipj
otherwise.
When pi and pj are known, the p-value is given by P(KT c) where
KT c =

(N1, N2, N3, N4):

N1
N1 + N2 + N3
−E[T(yi, yj)]
 ≥|T c|

.
(4)
However, in practice, probabilities pi and pj are usually unknown. Therefore, we
deﬁne the centered Jaccard/Tanimoto coeﬃcient by ˆT c = T −
ˆpi ˆpj
ˆpi+ˆpj−ˆpi ˆpj , where
ˆpi =
Pyi
m , ˆpj =
Pyj
m
are standard estimators of pi and pj respectively. Plug-in
estimates of E[T(yi, yj)] into Eq. (4) will result in conservative behaviors, since
we estimate the probabilities on the same sample that we want to perform the
test. Then, the estimates of expectation are biased toward the observed value of
Jaccard/Tanimoto coeﬃcient. To overcome this bias, we estimate probabilities pi
and pj for each conﬁguration (N1, N2, N3, N4) separately.
So in this case, the critical region is deﬁned as follows
K ˆT c =

(N1, N2, N3, N4):

N1
N1 + N2 + N3
−
˜pi˜pj
˜pi + ˜pj −˜pi˜pj
 ≥| ˆT c|

,
(5)
where ˜pi = N1+N2
m
and ˜pj = N1+N3
m
.
Because the exact distribution is computationally expensive (see Results for com-
parison), we introduce an asymptotic approximation when m →∞. It may be
useful when dealing with very large binary data, where computational power is a
bottleneck. Denote by q1 = pipj the probability that both yi and yj have ones,
and by q2 = pi + pj −2pipj the probability that only one of two vectors has one.
Similarly, ˆq1 and ˆq2 are deﬁned with the plug-in estimators. As m →∞, we can
estimate the variance:


## Page 6


Page 6 of 19
Proposition 2
If yi and yj are independent then
√mT c(yi, yj) →N(0, σ2)
as m →∞, where
σ2 = q1q2(1 −q2)
(q1 + q2)3 .
Proof Theorem 14.6 of [27] states that
√m ((N1, N2 + N3)/m −(q1, q2)) →N(0, Σ)
where
Σ =
"
q1(1 −q1)
−q1q2
−q1q2
q2(1 −q2)
#
.
Then, we deﬁne function g(x1, x2) =
x1
x1+x2 and apply the delta method. So, we get
√m

T(yi, yj) −
q1
q1 + q2

→N(0, ∇g(q1, q2)Σ∇g(q1, q2)T ).
The gradient of g is
∇g(x1, x2) =

x2
(x1 + x2)2 ,
−x1
(x1 + x2)2

.
Finally, after simpliﬁcation, we obtain
∇g(q1, q2)Σ∇g(q1, q2)T = q1q2(1 −q2)
(q1 + q2)3 .
In practice, probabilities pi and pj are unknown and need to be estimated. Recall
that ˆpi = #{yik=1}
m
and ˆpj = #{yjk=1}
m
. We deﬁne ˆq1 and ˆq2 by replacing in deﬁnition
of q1 and q2 true probabilities pi and pj by its estimators. So based on Proposition 2
we are able to approximate p-values as follow:
2φ
√m
σ

T(yi, yj) −
ˆq1
ˆq1 + ˆq2

−1 ,
(6)
where φ =
1
√
2π
R x
−∞e−x2/2dx is a standard Gaussian cumulative distribution func-
tion (CDF).


## Page 7


Page 7 of 19
Measure Concentration Algorithm
The distribution of the centered Jaccard/Tanimoto coeﬃcient can be expressed
in terms of the multinomial distribution. However, evaluating a signiﬁcance test
based on this representation requires exhaustive computations. It needs summa-
tion over all possible states of the multinomial distribution. For the centered Jac-
card/Tanimoto coeﬃcient between yi and yj, we need to compute probability of
event K ˆT c deﬁned by Eq. (5).
This can be quickly and accurately estimated by the measure concentration al-
gorithm (MCA) with a known error bound [28]. For every ε > 0, we will con-
struct Iε, a set of (N1, N2, N3, N4) with N1 + N2 + N3 + N4 = m, such that
P(N1, N2, N3, N4) ∈Iε ≥1 −ε. Given the set Iε, we have following bounds
pL
ε ( ˆT c) = P
 K ˆT c ∩Iε

≤P
 K ˆT c

≤P
 K ˆT c ∩Iε

+ ε = pU
ε ( ˆT c).
In addition, pU
ε ( ˆT c) −pL
ε ( ˆT c) = ε.
The idea behind the algorithm is that a multinomial distribution concen-
trates around its mode. Two possible states N = (N1, N2, N3, N4) and N ′ =
(N ′
1, N ′
2, N ′
3, N ′
4) are neighbors, N ∼N ′, if P4
i=1 |Ni−N ′
i| = 2. This means that N ′
can be obtained from N by moving one element to a diﬀerent class. We construct
the set Iε as follows.
At the onset, Iε contains only the mode of multinomial distribution. We ﬁnd
the mode by a simple hill climbing algorithm, which starts with a state close to
the mean of the multinomial distribution and follows the direction of increasing
probability until the maximum is reached. Because of unimodality, it is indeed a
global maximum. In the next steps, we add the neighbors of states which were
previously visited. The procedure is repeated until the total probability of set Iε
reaches the desired value 1 −ε. The details of the above method can be found in
[28]. We construct the set Iε and we estimate the p-value by
pL( ˆT c) =
X
N∈Iε
1

N1
N1 + N2 + N3
−
˜pi˜pj
˜pi + ˜pj −˜pi˜pj
 ≥| ˆT c|

P(N1, N2, N3, N4).
(7)
Bootstrap Procedure
The bootstrap procedure has gained mainstream popularity for its wide applicability
and statistical treatments [29]. Creating an empirical distribution of null statistics
allows for a ﬂexible and robust estimation of p-values and related statistics. We
show how to use the resampling with replacement to obtain statistical signiﬁcance of
T c(yi, yj). Particularly, resampling with replacement yi and yj, separately, breaks
any potential dependency. This allows us to calculate an empirical distribution of
Jaccard/Tanimoto coeﬃcients under the null hypothesis:


## Page 8


Page 8 of 19
Algorithm 1: Bootstrap Procedure for Jaccard/Tanimoto Coeﬃcients
Input: two binary vectors yi and yj
Output: p-value
1 Calculate a centered Jaccard/Tanimoto coeﬃcient t = T c(yi, yj).
2 for b ←1 to B do
3
Resample with replacement yi and yj, resulting in y∗
i and y∗
j.
4
Calculate bootstrap null coeﬃcients t∗
b = T c(y∗
i , y∗
j).
5 end
6 Compute the p-value by
p-value = 1{|t∗
b| ≥|t|; b = 1, . . . , B}
B
.
The expectation of Jaccard/Tanimoto coeﬃcients is estimated directly from re-
sampled vectors y∗
i and y∗
j, that are eﬀectively independent. Therefore, each iter-
ation provides randomness, which helps avoid a bias related to using an estimated
expectation based only on observation. Previously, there are early works in Monte
Carlo procedures [30, 14] and published statistical tables for assessing randomness
in species co-occurances [22, 23]. However, earlier works have assumed that a proba-
bility of occurrences is 0.5 regardless of species or biogeographic units. Permutation
methods based on conventional uncentered coeﬃcients are available in R packages,
whose operating characteristics are not described in details [31, 32].
The resolution of the empirical null distribution depends on B, where the larger
B will result in more precise estimation of p-values. Although the choice of B
would likely be dictated by n and m, as well as available computational power, we
recommend setting B to at least 5-10 times of m. In our simulation studies, the
total bootstrap iterations is set to B = 5×m, which are shown to be both accurate
and fast. When comparing a very large set of species or OTUs, it may be helpful to
pool null statistics to increase the p-value resolution and speed up the computation.
Results and discussion
Simulation Studies
We have developed statistical methods and algorithms to obtain statistical signif-
icance of Jaccard/Tanimoto similarity coeﬃcients for biological presence-absence
data. Beyond deriving the exact solution, we introduce the measurement concen-
tration algorithm (MCA) and bootstrap method. We characterize their operating
characteristics by comprehensive simulation studies where a wide range of parame-
ters for presence-absence datasets are considered. Our goal is to maintain theoreti-
cally correct behaviors of p-values. Null p-values corresponding to H0 are evaluated
against a Uniform(0,1) distribution. False discovery rates (FDRs) are directly es-
timated from p-values produced by our methods to demonstrate an overall error
control.
First, we conducted 5 simulation scenarios using diﬀerent underlying occurrence
probabilities p = 0.1, 0.3, 0.5, 0.7, 0.9 to generate independent presence-absence


## Page 9


Page 9 of 19
datasets. In essence, they are two species of length m = 100 that exhibit unre-
lated co-occurrence patterns, where a proportion of presence (1’s) ranges from 10%
to 90%. For each of simulation scenarios, a total of 2000 comparisons were made
using a length m = 100. Without any information about simulation parameters,
our proposed methods are applied on an identically simulated dataset (Figure 2).
Theoretically correct p-values under the null hypothesis (null p-values) should form
a Uniform distribution between 0 and 1, which are denoted by dashed diagonal lines
in QQ plots. An upward deviation from diagonals shows an anti-conservative bias,
as shown among some asymptotic p-values. In all scenarios, p-values from the exact
solution, bootstrap (B = 500), and measure concentration (accuracy = 1×10−5) al-
gorithms follow a theoretically correct Uniform(0,1) distribution (Figure 2). Asymp-
totic approximation is inconsistent; its behavior is anti-conservative with p = 0.3, 0.5
and slightly conservative with p = 0.7, 0.9. Asymptotic approximation should only
be used when computational time is a critical bottleneck.
Second, we generated a mixture of independent and dependent datasets out of
n = 2000 presence-absence vectors (of n = 2000 species observed in m = 200 bio-
geographic units) to evaluate false discovery rates. In three separate scenarios, we
simulated 25%, 50%, and 75% of n = 2000 species to be independent, resulting
in null proportions of π0 = .25, .50, .75 respectively. For example, a scenario with
π0 = .75 produces 500 out of n = 2000 presence-absence variables that are truly
associated with the query variable. Then, our proposed asymptotic approximation,
bootstrap method, and measure concentration algorithm (MCA) are used to au-
tomatically compute p-values. To account for variation in simulation, we repeated
each scenario 20 times. False discovery rates (FDRs) and π0 are estimated by the q-
value methodology [33]. Q-values are evaluated against FDR thresholds, so that we
can evaluate accuracy of observed FDRs (Figure 3). Twenty simulation replications
are shown in semi-transparent shades, whereas their group averages for 3 methods
are shown as solid lines. An upward deviation as shown by asymptotic approxi-
mation indicates an overall anti-conservative behavior, likely due to m ̸→∞. The
bootstrap and MCA maintain the overall error rates, where the bootstrap exhibits
slightly conservative characteristics (Figure 3).
Third, we compared the computational eﬃciency of our proposed methods using
our jaccard package on RStudio Cloud (Intel Xeon 2.90GHz and 1GB RAM), with
R 3.5.0. We measured the runtime for a range of lengths m = 50, . . . , 500. For each
m, we applied the proposed methods 10 times, with the bootstrap iteration B =
5×m and MCA accuracy of 1×10−5. The average runtimes are shown Figure 4. Our
proposed computational methods show drastic improvement over the exact solution
as m increases. The asymptotic approximation is mostly instantaneous. When the
similarity between two presence-absence vectors of length m = 500 were tested
using the jaccard package, the exact solution was prohibitively slow, taking 41.5s
on average. The bootstrap method was 449.8 times (0.09s) faster, whereas MCA
was 92.5 times (0.45s) faster than the exact solution. Furthermore, we compared
the runtimes of estimation methods for m = 1000, . . . , 10000 (Figure S1). The gain
in computational eﬃciency is more pronounced as the dimension (i.e., a length of
presence-absence vectors) grows in size.


## Page 10


Page 10 of 19
Last, a simulation study with p = 0.5 and m = 200 was used to evaluate two recent
methods of species co-occurrences analysis. We generated independent presence-
absence data where two species are truly unrelated. Then, methods of combina-
torics [24] and hypergeometric distributions [25] are applied to obtain p-values. We
followed the recommendations given in each paper, displaying four possible p-values
from [24] (Figure S2) and two one-sided p-values from [25] (Figure S3). We observe
these p-values under the null hypothesis to substantially deviate from theoretically
correct Uniform(0,1) distributions.
Applications in Species Co-occurrences
To show applications in statistically testing biological presence-absence data, the
proposed methods are applied to species co-occurrence data. We investigated bird
species on 28 islands in the Republic of Vanuatu, that are available in [6] and
analyzed in several pioneering studies in non-random co-occurrences of species [12,
14, 15, 16]. The data is consisted of presence and absence of bird species in 28 islands
of Vanuatu, which used to be known as the New Hebrides. Three generalist species
that existed in all 28 islands were removed from our analysis. We are interested in
identifying what pairs of species exhibit statistically signiﬁcantly co-occurrences.
For n = 53 bird species in m = 28 islands, we obtained 1378 pair-wise Jac-
card/Tanimoto similarity coeﬃcients. The conventional Jaccard/Tanimoto coeﬃ-
cients depends strongly on their expected values under independence (Figure 5).
Similarly, the conventional Jaccard/Tanimoto coeﬃcients are substantially corre-
lated with the proportion of occurrences, with a Pearson correlation of 0.43 (p-value
< 2.2 × 10−16). Relying only on similarity coeﬃcients would miss non-random co-
occurrences among bird species that live in a few islands (Figure S4). Our proposed
methods account for co-occurrences that would be expected under independence.
Histograms of the uncentered and centered Jaccard/Tanimoto coeﬃcients are com-
pared in Figure S5.
We computed statistical signiﬁcance by applying the bootstrap method with B =
5000 and MCA with accuracy of 1 × 10−5. Our two computational approaches
estimated p-values that are almost identical with their mean squared deviation of
1.15 × 10−4 (Figure S6). Signiﬁcant results that are substantially deviating from
random samples indicate non-random co-occurrences of species (Figure 6). Out of
1378 pairs of species that were tested, the proportion of independent specie pairs
was estimated to be 24% using q-value methodology [33]. Then, we calculated false
discovery rates (FDRs) from 1378 pair-wise p-values. We discovered that 374 (27%)
pairs are deemed signiﬁcant at a q-value threshold of 0.10.
Additionally, we applied the Jaccard/Tanimoto similarity tests among ﬁsh species
in French freshwater streams, surveyed over a long period of time [34]. Brieﬂy, the
presence and absence data of the n = 32 most common ﬁsh species in m = 3347
sites across French rivers are obtained during 1980 - 1991 [34]. Our analysis esti-
mates that about 84.3% of 496 pairs are estimated to be non-randomly co-occurring.
As surveyed for over a decade across Fresh rivers and surrounding habitats, it is
reasonable that many ﬁsh species are interacting or inﬂuenced by related climate
conditions. There are 21 pairs of species with q-values > 0.1 (corresponding p-values
ranging from 0.637 and 0.969). For example, the centered statistics between Pungi-
tius pungitius and Cyprinus carpio is 3.31 × 10−4, whereas that between Pungitius


## Page 11


Page 11 of 19
pungitius and Lota lota is −4.40×10−4. P. pungitius is a small ﬁsh species typically
riding in thick submerged vegetation with the breeding season falling in April - July.
C. carpio and L. lota are much bigger species and generally prefers a large body of
water.
Conclusion
From biogeography to microbiology, evaluating similarity among species and bio-
geographic units is fundamental to assessing co-existence and biodiversity. Having
observed occurrences of species in multiple biogeographic units, one of the primary
goals in analyzing presence-absence data is to identify non-random co-occurrences.
Even if two species would be present independently of each other, they may occur
together by chance. For the last 30 years, the Jaccard/Tanimoto coeﬃcient has been
shown to be highly useful for quantitative analysis of co-occurrences that help in-
form systematic relationship among species [3, 4, 5]. We have developed a rigorous
statistical framework and methods to eﬃciently calculate statistical signiﬁcance of
such similarity and to identify non-random co-occurrences.
For testing co-occurrences using the Jaccard/Tanimoto coeﬃcient, we introduce
exact and asymptotic solutions, as well as bootstrap and measure concentration al-
gorithm. The proposed suite of statistical methods can provide a rigorous guideline
to identify related species. Through comprehensive simulation studies, we char-
acterized their operating characteristics using p-values and FDRs. The proposed
bootstrap and measure concentration algorithms are highly accurate and eﬃcient,
providing orders of magnitude improvement in a computational speed. We have
implemented the proposed methods in an open source R package and a Shiny web
app. A user can upload a dataset to be analyzed, and create histograms and heat
maps automatically. This will facilitate adaptation of p-values, FDRs, and related
quantities in analyzing species co-occurrences.
Beyond species co-occurrences, the Jaccard/Tanimoto coeﬃcient is used in di-
verse areas of biological science where binary data are observed and compared.
When molecules and reactions are represented as hashed ﬁngerprints, it is used for
quantitative comparisons and classiﬁcations [35, 36, 37]. Similarity between bio-
chemical reactions can be tested by applying our methods on their corresponding
ﬁngerprints. In genomics, the standard tools such as BEDTools [38] evaluate ge-
nomic intervals using the Jaccard/Tanimoto coeﬃcients. Given genomic intervals
from two samples or groups, one could test whether their overlap is statistically sig-
niﬁcant, providing evidences for shared genomic variations. Due to the popularity
of Jaccard/Tanimoto coeﬃcients, the proposed suite of methods would be useful in
a broad range of scientiﬁc applications.
References
1. Jaccard, P.: The distribution of the ﬂora in the alpine zone. New Phytologist 11(2), 37–50 (1912).
doi:10.1111/j.1469-8137.1912.tb05611.x
2. Tanimoto, T.: An elementary mathematical theory of classiﬁcation and prediction. Technical report,
International Business Machines Corporation, New York (1958)
3. Birks, H.J.B.: Recent methodological developments in quantitative descriptive biogeography. Ann. Zool.
Fenn. 24, 165–178 (1987)
4. Jackson, D.A., Somers, K.M., Harvey, H.H.: Null models and ﬁsh communities: Evidence of nonrandom
patterns. The American Naturalist 139(5), 930–951 (1992)
5. Real, R., Vargas, J.M.: The probabilistic basis of jaccard’s index of similarity. Systematic Biology 45(3),
380–385 (1996). doi:10.1093/sysbio/45.3.380


## Page 12


Page 12 of 19
6. Manly, B.F.J.: Randomization, Bootstrap and Monte Carlo Methods in Biology. Chapman & Hall / CRC
Press, Boca Raton, FL (2006)
7. Davies, N.B., Krebs, J.R.: An Introduction to Behavioural Ecology. Wiley-Blackwell, U.S.A. (1993)
8. Townsend, C.R., Begon, M., Harper, J.L.: Essentials of Ecology. Wiley-Blackwell, U.S.A. (2002)
9. Whittaker, R.H.: Vegetation of the siskiyou mountains, oregon and california. Ecological Monographs
30(3), 279–338 (1960). doi:10.2307/1943563
10. Harrison, S., Ross, S.J., Lawton, J.H.: Beta diversity on geographic gradients in britain. The Journal of
Animal Ecology 61(1), 151 (1992). doi:10.2307/5518
11. Koleﬀ, P., Gaston, K.J., Lennon, J.J.: Measuring beta diversity for presence-absence data. Journal of
Animal Ecology 72(3), 367–382 (2003). doi:10.1046/j.1365-2656.2003.00710.x
12. Connor, E.F., Simberloﬀ, D.: The assembly of species communities: Chance or competition? Ecology
60(6), 1132 (1979). doi:10.2307/1936961
13. Diamond, J.M., Gilpin, M.E.: Examination of the "null" model of connor and simberloﬀfor species
co-occurrence on islands. Oecologia 52, 64–74 (1982). doi:10.1007/BF00349013
14. Gilpin, M.E., Diamond, J.M.: Factors contributing to non-randomness in species co-occurrences on islands.
Oecologia 52, 75–84 (1982). doi:10.1007/BF00349014
15. Wilson, J.B.: Methods for detecting non-randomness in species co-occurrences: a contribution. Oecologia
73(4), 579–582 (1987). doi:10.1007/BF00379419
16. Manly, B.F.J.: A note on the analysis of species co-occurrences. Ecology 76(4), 1109–1115 (1995).
doi:10.2307/1940919
17. Sanderson, J., Moulton, M., Selfridge, R.: Null matrices and the analysis of species
co-occurrencessanderson. Oecologia 116(1–2), 275–283 (1998). doi:10.1007/s004420050
18. Ellwood, M.D.F., Manica, A., Foster, W.A.: Stochastic and deterministic processes jointly structure tropical
arthropod communities. Ecology Letters 12(4), 277–284 (2009). doi:10.1111/j.1461-0248.2009.01284.x
19. Chase, J.M., Myers, J.A.: Disentangling the importance of ecological niches from stochastic processes
across scales. Philosophical transactions of the Royal Society B: Biological sciences 366(1576), 2351–2363
(2011). doi:10.1098/rstb.2011.0063
20. Fridley, J.D., Vandermast, D.B., Kuppinger, D.M., Manthey, M., Peet, R.K.: Co-occurrence based
assessment of habitat generalists and specialists: A new approach for the measurement of niche width.
Journal of Ecology 95(4), 707–722 (2007). doi:10.1111/j.1365-2745.2007.01236.x
21. Araújo, M.B., Rozenfeld, A.: The geographic scaling of biotic interactions. Ecography (2013).
doi:10.1111/j.1600-0587.2013.00643.x
22. Baroni-Urbani, C., Buser, M.W.: Similarity of binary data. Systematic Zoology 25(3), 251 (1976).
doi:10.2307/2412493
23. Baroni-Urbani, C.: A statistical table for the degree of coexistence between two species. Oecologia 44(3),
287–289 (1979). doi:10.1007/bf00545229
24. Veech, J.A.: A probabilistic model for analysing species co-occurrence. Global Ecology and Biogeography
22, 252–260 (2013). doi:10.1111/j.1466-8238.2012.00789.x
25. Griﬃth, D.M., Veech, J.A., Marsh, C.J.: cooccur: Probabilistic species co-occurrence analysis inr. Journal
of Statistical Software 69 (2016). doi:10.18637/jss.v069.c02
26. R Core Team: R: A Language and Environment for Statistical Computing. R Foundation for Statistical
Computing, Vienna, Austria (2017). R Foundation for Statistical Computing. https://www.R-project.org
27. Wasserman, L.: All of Statistics: A Concise Course in Statistical Inference. Springer, New York, U.S.A.
(2010)
28. Łącki, M.K., Startek, M., Valkenborg, D., Gambin, A.: IsoSpec: Hyperfast ﬁne structure calculator.
Analytical Chemistry 89(6), 3272–3277 (2017). doi:10.1021/acs.analchem.6b01459
29. Efron, B., Tibshirani, R.: An Introduction to the Bootstrap. Chapman & Hall / CRC Press, Boca Raton,
Florida (1994)
30. Connor, E.F., Simberloﬀ, D.: Species number and compositional similarity of the galapagos ﬂora and
avifauna. Ecological Monographs 48, 219–248 (1978). doi:10.2307/2937300
31. Gotelli, N.J., Hart, E.M., Ellison, A.M.: EcoSimR: Null Model Analysis for Ecological Data. (2015). R
package version 0.1.0. http://github.com/gotellilab/EcoSimR
32. Oksanen, J., Blanchet, F.G., Friendly, M., Kindt, R., Legendre, P., McGlinn, D., Minchin, P.R., O’Hara,
R.B., Simpson, G.L., Solymos, P., Stevens, M.H.H., Szoecs, E., Wagner, H.: Vegan: Community Ecology
Package. (2017). R package version 2.4-5. https://CRAN.R-project.org/package=vegan
33. Storey, J.D., Tibshirani, R.: Statistical signiﬁcance for genomewide studies. Proceedings of the National
Academy of Sciences 100(16), 9440–9445 (2003). doi:10.1073/pnas.1530509100
34. Comte, L., Hugueny, B., Grenouillet, G.: Climate interacts with anthropogenic drivers to determine
extirpation dynamics. Ecography 39(10), 1008–1016 (2016). doi:10.1111/ecog.01871
35. Todeschini, R., Consonni, V., Xiang, H., Holliday, J., Buscema, M., Willett, P.: Similarity coeﬃcients for
binary chemoinformatics data: Overview and extended comparison using simulated and real data sets. J.
Chem. Inf. Model. 52(11), 2884–2901 (2012). doi:10.1021/ci300261r
36. Rahman, S.A., Cuesta, S.M., Furnham, N., Holliday, G.L., Thornton, J.M.: EC-BLAST: a tool to
automatically search and compare enzyme reactions. Nature Methods 11(2), 171–174 (2014).
doi:10.1038/nmeth.2803
37. Bajusz, D., Rácz, A., Héberger, K.: Why is tanimoto index an appropriate choice for ﬁngerprint-based
similarity calculations? J Cheminform 7(1) (2015). doi:10.1186/s13321-015-0069-3
38. Quinlan, A.R.: Bedtools: the swiss-army tool for genome feature analysis. Current Protocols in
Bioinformatics, 11–12 (2014). doi:10.1002/0471250953.bi1112s47


## Page 13


Page 13 of 19
Figures
yi
e.g. {0,1,0, …}
yj
e.g. {1,0,0, …}
E[T(yi, yj)]
Expectation
Proposition 1
Tc(yi, yj)
Centered
Coefﬁcient
Equation 2
H0: Tc = 0
H1: Tc ≠ 0
Hypothesis
Equation 3
Exact
Eq. 4,5
Asymptotic
Eq. 6
MCA
Eq. 7
Bootstrap
Algorithm 1
Significance  Calculation 
Input
Figure 1 Flowchart of the proposed statistical methods and algorithms.
Exact
Asymptotic
MCA
Bootstrap
0.00
0.25
0.50
0.75
1.00 0.00
0.25
0.50
0.75
1.00 0.00
0.25
0.50
0.75
1.00 0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
P−value
Theoretical Uniform(0,1)
Probability of presence
.10
.30
.50
.70
.90
Figure 2 P-values of similarity among independent presence-absence vectors of m = 100,
with a wide range of probabilities p = .1, .3, .5, .7, .9. In each scenario, 2000 independent
variables are simulated and tested using four proposed methods. The diagonal lines
indicate a theoretically correct Uniform(0,1) distribution.


## Page 14


Page 14 of 19
Figure 3 False discovery rate (FDR) estimates from a mixture of independent and
dependent presence-absence vectors. In 3 separate scenarios with null proportions
π0 = .25, .50, .75, 2000 presence-absence vectors of m = 200 are simulated with
occurrence probabilities of p = .5. Each simulation scenario is repeated 20 times and the
proposed methods are used to automatically compute p-values and q-values. FDR
thresholds are plotted against observed false discovery proportions, where a downward
deviation from a theoretically correct diagonal red line indicates a conservative behavior.
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
1e−04
0.001
0.01
0.1
1
10
100
200
300
400
500
Dimension (m)
Time (log10(seconds))
Method
G
G
G
G
Exact
Asymptotic
MCA
Bootstrap
Figure 4 Computational runtimes of our 4 proposed methods. The means of 100
independent runs are plotted against an increasing size of dimension m = 50, . . . , 500.
Compared to the exact solution, the bootstrap and measure concentration algorithm
(MCA) provide vast improvements in speed whose relative eﬃciency increases with higher
dimension.


## Page 15


Page 15 of 19
0.00
0.25
0.50
0.75
0.00
0.25
0.50
0.75
1.00
Coefficients
Expectation
Uncentered
Centered
Figure 5 Comparison of uncentered and centered Jaccard/Tanimoto coeﬃcients from the
bird dataset. The conventional uncentered coeﬃcients are shown to be strongly dependent
on expectation under independence. By centering each coeﬃcient by its expectation, the
proposed centered coeﬃcients alleviate this dependency.
Figure 6 Heatmap of uncentered Jaccard/Tanimoto coeﬃcients and their p-values.
Similarity among 53 bird species in 28 islands of Vanuatu are tested using the proposed
method. Species are ordered from high to low occurrences, that are highly correlated with
Jaccard/Tanimoto coeﬃcients (p-value < 2.2 × 10−16). The upper triangle shows the
p-values from our methods, whereas the lower triangle the observed Jaccard/Tanimoto
coeﬃcients.


## Page 16


Page 16 of 19
Supplementary Figures
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
1e−04
0.001
0.01
0.1
1
10
0
2500
5000
7500
10000
Dimension (m)
Time (log10(seconds))
Method
G
G
G
G
Exact
Asymptotic
MCA
Bootstrap
Figure S1 Computational runtimes when testing similarity between presence-absence data
upto m = 10000. We ran the proposed 4 methods to compute p-values for a wide range
of dimension m. For each m, 100 independent simulations are conducted. Note that for
m ≥1000, the exact solution did not compute in a reasonable time. The bootstrap and
measure concentration algorithm (MCA) are orders of magnitude faster than the exact
solution. The asymptotic solution is instantaneous regardless of m.


## Page 17


Page 17 of 19
p_et + p_lt
p_et + p_gt
p_lt
p_gt
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
0
50
100
150
200
250
0
50
100
150
200
250
Null P−values
Frequency
Figure S2 Combinatoric p-values of similarity among independent presence-absence
vectors of m = 200 with p = .5. In each scenario, 2000 independent variables are
simulated and tested using a combinatorics [24]. [24] recommends plt + pet and pgt + pet
as p-values. The dashed red lines indicate theoretically correct Uniform distributions.
p_lt
p_gt
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
0
50
100
150
200
250
Null P−values
Frequency
Figure S3 Hypergeometric p-values of similarity among independent presence-absence
vectors of m = 200 with p = .5. We used a hypergeometric distribution [25] to obtain
p-values of similarity between independent species. The original authors suggested that
pgt and plt can be “interpreted and reported as p-values”. The dashed red lines indicate
theoretically correct Uniform distributions.


## Page 18


Page 18 of 19
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
Marginal Occurrences
Jaccard/Tanimoto coefficients
Figure S4 Scatterplot of marginal occurrences of 53 bird species and Jaccard/Tanimoto
coeﬃcients. As expected, we observe high correlation (Pearson correlation = 0.43)
between marginal occurrences and Jaccard/Tanimoto coeﬃcients.
0
30
60
90
0
100
200
300
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
Coefficients
Centered Coefficients
Frequency
Frequency
(a) Jaccard/Tanimoto coefficients
(b) Centered Jaccard/Tanimoto coefficients
Figure S5 Histograms of conventional and centered Jaccard/Tanimoto similarity
coeﬃcients. The conventional (uncentered) Jaccard/Tanimoto coeﬃcients are centered by
their expected values under the independence assumption.


## Page 19


Page 19 of 19
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
Bootstrap
MCA
Figure S6 Comparison of p-values from the bootstrap and measure concentration
algorithm (MCA). Both algorithms were applied on 1378 co-occurrences of bird species.
The diﬀerence between estimated p-values from two methods is minimal with a mean
squared deviation of 1.15 × 10−4. The diagonal red line indicates the identity.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
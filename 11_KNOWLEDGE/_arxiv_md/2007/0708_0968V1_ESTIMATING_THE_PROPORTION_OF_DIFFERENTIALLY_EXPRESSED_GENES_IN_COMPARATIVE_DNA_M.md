---
canon-group: reference
rscf-state: source-claim
arxiv_id: 0708.0968v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 0708.0968v1_Estimating_the_proportion_of_differentially_expressed_genes_in_comparative_DNA_m

> Source: 0708.0968v1_Estimating_the_proportion_of_differentially_expressed_genes_in_comparative_DNA_m.pdf

> Pages: 11

---


## Page 1


arXiv:0708.0968v1  [stat.ME]  7 Aug 2007
IMS Lecture Notes–Monograph Series
Complex Datasets and Inverse Problems: Tomography, Networks and Beyond
Vol. 54 (2007) 92–102
c⃝Institute of Mathematical Statistics, 2007
DOI: 10.1214/074921707000000076
Estimating the proportion of diﬀerentially
expressed genes in comparative DNA
microarray experiments∗
Javier Cabrera1 and Ching-Ray Yu1
Rutgers University
Abstract: DNA microarray experiments, a well-established experimental
technique, aim at understanding the function of genes in some biological pro-
cesses. One of the most common experiments in functional genomics research
is to compare two groups of microarray data to determine which genes are
diﬀerentially expressed. In this paper, we propose a methodology to estimate
the proportion of diﬀerentially expressed genes in such experiments. We study
the performance of our method in a simulation study where we compare it to
other standard methods. Finally we compare the methods in real data from
two toxicology experiments with mice.
1. Introduction
The human genome and a number of other genomes have been almost fully se-
quenced, but the functions of most genes are still unknown. The diﬃculty is that
gene expression is only one of the pieces of cellular processes sometimes called bio-
logical pathways or networks, and it is not yet possible to observe these pathways
directly. DNA microarray technology has made it possible to quantify and compare
relative gene expression proﬁles across a series of conditions many thousands of
genes at a time. By identifying groups of genes that are simultaneously expressed
the guesswork of reconstructing biological pathways is expedited. The information
collected through the years on genes that participate on biological pathways or net-
works has been used to construct GO (Gene Ontology Consortium [8]). The infor-
mation on diﬀerentially expressed genes from a microarray experiment is contrasted
with the groupings that are known according to existing GO and a determination is
made on whether or not a certain cellular process is taking place. In addition there
might be a few genes that are diﬀerentially expressed in the experiment but were
not known to be part of the biological process. These genes become candidates for
further extending the pathway and will be conﬁrmed by further experimentation
and also by searching for annotations that describe their function in other processes.
However, how to determine biological diﬀerentially expressed genes accurately is
a nontrivial issue. Microarray experiments are high throughput in the sense that
they evaluate the expression levels of thousands of genes at a time but with little
replications. It is often the case that the number of replicate chips (biological, or
technical) is 3 to 5 per condition. In addition the distributions of gene expressions
across samples tend to be skewed and/or heavily tailed and hence they do not follow
∗The First and Second author make the same contributions to this paper.
1Department
of
Statistics,
Rutgers
University,
NJ,
08854,
USA,
e-mail:
cabrera@stat.rutgers.edu; chingray@stat.rutgers.edu
Keywords and phrases: biological process, DNA microarray, diﬀerentially expressed genes, tox-
icology experiment.
92


## Page 2


Estimating the proportion of diﬀerentially expressed genes
93
a normal distribution. In this situation, permutation tests and traditional t-tests
do not work very well because they have very low power.
One way to improve the power of the test is to incorporate the GO information
to the process. Fisher’s exact test (Fisher [7]) has been proposed as a way to detect
if a particular subgroup of genes as a whole is diﬀerentially expressed. The test is
applied to a two-way table of the indicator variable detecting the signiﬁcance of
the individual gene versus the indicator variable of the group. Another test is to
consider the test statistic computed by Mean- Log-P, mean(-log(p-value)), (Pavlidis
et al. [13] and Raghavan et al. [14]), of the genes in the group and compare this to
the distribution of the statistics under a random subset of genes.
On the other hand, if when applying real data on GO, the number of diﬀerentially
expressed genes overall is large, then the Fisher’s exact test or Mean-Log-P test
would still have low power. In order to overcome these problems we propose a new
model approach, which consists of the following steps:
1. Estimate the proportion of diﬀerentially expressed genes.
2. Estimate the distribution of p-values for genes that are not diﬀerentially ex-
pressed. One would expect that this distribution is uniform but this is not the
case in many examples that we have studied. The reason might be related to
the processing of the data and the discarding of genes that take place at some
stages of the process. Therefore the model has to estimate the distributions
of null p-values by a semi-parametric or nonparametric method.
3. Estimate the distribution of p-values corresponding to diﬀerentially expressed
genes.
4. Proceed by modeling the distribution of Mean-Log -P statistics for genes
that belong to a subgroup or network. See Raghavan et al. [14], by using the
estimators of steps 1-3.
In this paper we concentrate on step 1 of the procedure, which corresponds to the
estimation of π. This quantity π is important also in other situations, for example
to calculate q-values (moderated p-values) proposed by Storey and Tibshirani [16].
For step 2-4 of the procedure, we will publish elsewhere as well. In Section 2 we
propose a method and an algorithm for estimating π. In Section 3 we report the
results of extensive simulation that support the performance of our method as well
as comparison with other simpler methods.
Example mice and mice2: To illustrate the estimation of π, we apply our proce-
dure for the mouse data sets from toxicology experiments (Amaratunga and Cabrera
[3]). These datasets correspond to typical toxicology experiments where a group of
mice is treated with a toxic compound and the objective is to ﬁnd genes that are
diﬀerentially expressed against samples from untreated mice.
mice and mice2 are two of the data sets that consist n1 = n2 = 4 mice in the
control and treatment groups and total number of genes are G = 4077 from mice
and G = 3434 for mice2 respectively. They represent two examples of cDNA chips,
the ﬁrst one mice has a high proportion π of diﬀerentially expressed genes whereas
mice2 has a much smaller π.
The data from such experiments consist of suitably normalized intensities: Xgij,
where g(g = 1, . . . , G) indicates the genes on the microarray, i(i = 1, 2) indexes
the groups, and j(j = 1, . . . , ni) is the i-th mouse in the j-th group. Our goal is to
characterize Γ, a subset of genes, among the G genes in the experiment that are
diﬀerentially expressed across two groups.
Methods for determining Γ, researchers (e.g. Schena et al. [15]) use fold change,
but they did not take variability into account. Subsequent improvements were t-test


## Page 3


94
J. Cabrera and C. Yu
statistics (Efron et al. [6], Tusher et al. [17], and Broberg [5]), median-based methods
(Amaratunga and Cabrera [1]) and Bayes and Empirical Bayes procedures (Lee et
al. [10], Baldi and Long [4], Efron et al. [6], Newton et al. [12], and Lonnstedt and
Speed [11]).
T-tests are the most widely used method for assessing diﬀerential expression.
The assumption of the t-tests is that normalized intensities are approximately nor-
mally distributed with the same variance across the groups. i.e.Xgij ∼N(µgi, σ2
g).
For each gene g, a t-statistic is calculated in order to test null hypothesis µg1 = µg2
and a p-value is generated. For small samples the t-test might be replaced by SAM
or conditional t-test, Ct (Amaratunga and Cabrera [3]) in order to improve the
power. Here we will follow the model proposed by Amaratunga and Cabrera [3] for
the Ct method. Instead of trying to determine which genes are diﬀerentially ex-
pressed we will estimate the proportion of diﬀerentially expressed genes. Of course,
as a consequence we could also produce an ordered list of genes that would be of
interest to the biologist, but as we said above the entire procedure will be published
elsewhere.
2. Statistical model and inference
The data for experiments typically consists of suitable iid normalized intensities:
(2.1)
Xgij = µg + τgi + σgǫgij,
where µg and σ2
g, g = 1, . . . , G, are the eﬀect and variance of the g-th gene re-
spectively, τgi is the eﬀect of the g-th gene in the i-th group (i = 1, 2), and
j(j = 1, . . . , ni) indexes the samples. This is the same model in Amaratunga and
Cabrera [3]. The treatment eﬀect of the g-th gene is:
τg = |τg2 −τg1|
We assume that ǫgij are iid observations from an unknown distribution F and we
assume that σg and τg are iid observations from unknown distributions Fσ and Fτ,
respectively. Fσ represents the distribution of the gene variances. Fτ is likely to have
a mass at zero with probability π representing the proportion of gene that are not
diﬀerentially expressed. If the sample sizes were bigger the unknown distributions
could be readily estimated by their respective cdf’s but for small sample sizes the
cdf’s would produce very biased estimators. In the remainder of this section we will
provide three procedures to estimate the three distributions F, Fτ, and Fσ, which
try to overcome the biases induced by small sample size.
In the model step:
1. Estimation of the error distribution Fǫ:
In (2.1) when the number of samples per group is very small (3, 4, 5) and
after residuals are subject to two constraints (sample mean ¯X = 0, sample
standard deviation s = 1) then if we pool the residuals together, the em-
pirical distribution that is obtained gives a very poor estimator of the error
distribution F.
For example: Suppose we sample 1000 genes from a normal distribution with
two groups of subjects of sizes 4 and 4. The empirical distribution of the
residuals is close to the true error distribution (which is standard normal)
which is shown in the left-top graph of Figure 1, but if we also simulated the


## Page 4


Estimating the proportion of diﬀerentially expressed genes
95
t- distribution with df.=4, and 10 the qq-plot of the empirical distribution is
not so good which is shown in the Figure 1.
One simple way to avoid this problem is to select a subset of genes SG that
have small absolute t-values (say below 1 or some threshold that gives a large
set of numbers). For each gene in SG, both samples are pooled together and
normalized by subtracting the gene mean and dividing by the standard devi-
ation. If the sample size per group is very small (3, 4, 5) instead of the sample
mean and standard deviation it is much better to use Huber M-estimator of
location and scale (Huber [9]) as shown by Figure 1. This will result in a table
of residuals ˆǫgij, g ∈SG. The error distribution Fǫ is estimated by
(2.2)
ˆFǫ = EmpiricalCDF{ˆǫgij, g ∈SG, i = 1, 2, j = 1, . . . , ni},
Figure 1 shows the qq-plot for the estimated error distribution on t- distribu-
tion. The improvement is very clear.
2. Estimating Fσ:
We follow the method described in Amaratunga and Cabrera [2, 3]. They
pointed out that the empirical distribution, ˆFσ, of sg is a very poor estimator
of the distribution Fσ, because on average ˆFσ is much more scattered than
Fσ. They proposed an estimate ˜Fσ of Fσ that shrinks ˆFσ towards its center
and hence producing a better estimator of Fσ. A similar algorithm will be
discussed in 3.
3. Estimating Fτ: (determine the proportion of diﬀerential expressed genes)
We said earlier that τg is drawn from some distribution Fτ. We expect that Fτ
has a mass at zero of probability Fτ(0) ≥0, which represents the genes that
are not diﬀerentially expressed. In order to estimate the probability P(τg =
0) we apply an algorithm that will produce an estimator ˜Fτ such that the
E ˜
Fτ ( ˆF ∗
τ (t)) = ˆFτ(t), where ˆF ∗
τ (t) is the random variable representing the
empirical cdf of τ ∗∗at value t, which is constructed in following algorithm
and ˆFτ(t) represents the actual observed value.
The algorithm is as follows:
Algorithm:
Step 1:
1.1) Draw a random sample, s∗, from ˜Fσ, which our estimate of the distri-
bution of σ.
1.2) Estimate the error distribution Fǫ with the empirical distribution ˆFǫ
deﬁned in (2.2).
1.3) Take a random sample (with replacement): rgij ∼ˆFǫ for i = 1, 2, j =
1, . . . , ni, g = 1, . . . , N.
1.4) Draw a sample τ ∗
g from ˆFτ(t) = I{t≥0}, where I{t≥0} = 1 if t ≥0 and
I{t≥0} = 0 if t < 0.
1.5) Construct the pseudo-data: X∗
g1j = sg ∗rg1j, X∗
g2j = τ ∗
g + sg ∗rg2j.
1.6) Reconstruct the distribution F ∗
ˆ
Fτ = E( ˆF ∗
τ | ˆFτ), where ˆF ∗
τ is the distri-
bution of τ ∗∗by pseudo-data: τ ∗∗
g
= | ¯X∗
g2 −¯X∗
g1|.
1.7) Start by setting ˆF (old)
τ
= ˆFτ.
1.8) Let ˆF (new)
τ
= ˆFτ(F ∗−1
ˆ
F (old)
τ
( ˆFτ)).
1.9) Set ˆF (old)
τ
= ˆF (new)
τ
and go to 1.3).


## Page 5


96
J. Cabrera and C. Yu
Fig 1. A comparison of the error distribution estimates obtained from the empirical distribution
(left) and our estimator (right), when the errors come from a Normal(0,1), t10 and t4 distribu-
tions.


## Page 6


Estimating the proportion of diﬀerentially expressed genes
97
1.10) Iterate until convergence (approximately 100 iterations). At conver-
gence we get our ﬁnal estimate ˜Fτ = ˆF (new)
τ
.
1.11) Give a cutoﬀpoint, say η, which is a 95% quantile of the ﬁnal ˜Fτ(t).
Step 2:
2.1) Repeat 1.4)-1.8) using all original data Xgij and the estimated ˆFτ.
2.2) Get the estimated percentage of τ ∗∗
g
which is greater than η × 95%
quantile of standard normal.
Theorem 2.1. At convergence the estimator ˜Fτ is a ﬁx point of the step in
1.8) of the algorithm. That is ˜Fτ = ˆFτ(F ∗−1
˜
Fτ ( ˆFτ)), then we have
(2.3)
E ˜
Fτ ( ˆF ∗
τ ) = ˆFτ.
Proof. If the algorithm converges, then ˜Fτ = ˆFτ(F ∗−1
˜
Fτ ( ˆFτ)). Thus
ˆFτ ◦˜F −1
τ
◦ˆFτ = F ∗
˜
Fτ = E( ˜Fτ| ˜Fτ) = ˜Fτ
⇒ˆFτ ◦˜F −1
τ
= ˜Fτ ◦ˆF −1
τ
⇒( ˆFτ ◦˜F −1
τ
)2 = I
⇒ˆFτ ◦˜F −1
τ
= I
or ˆFτ ◦˜F −1
τ
= −I (impossible, since ˆFτ, ˜Fτ ≥0)
E ˜
Fτ ( ˆF ∗
τ ) = E ˜
Fτ ( ˜Fτ) = ˜Fτ = ˆFτ.
Remark 1. Base on our simulations, the algorithm converges in at most 100
iterations.
Remark 2. At convergence, ˜Fτ is very close to ˆFτ and ˆF ∗
τ is also very close
to ˜Fτ, such that we have nice result E ˜
Fτ ( ˆF ∗
τ ) = ˆFτ.
Remark 3. This is a two-stage estimation method. We split data into two
pieces. One is non-informative data, which produces a good estimation of the
error distribution. The other is the informative data, we use shrinkage method
to estimate the distribution of τg, which gives the better result.
Performance assessment: To assess the performance of this method, we sim-
ulated data points, which are normally and independently distributed.
1. Xgij ∼N(τg, 1), where G = 10000, n1 = n2 = 4 and we assume that Gsig =
1000, . . ., 9000 of G genes were diﬀerentially expressed between two groups
and their diﬀerence was δ, i.e. τg = δ(δ = 1, 2) for all g = 1, . . . , Gsig, and
τg = 0 otherwise.
2. Xgij ∼N(τg, σ2
g), where G = 10000, n1 = n2 = 4 and we assume that Gsig =
1000, . . ., 9000 of G genes were diﬀerentially expressed between two groups
and their diﬀerence was δ = 1, 2, for all g = 1, . . . , Gsig, and τg = 0 otherwise
and σ2
g are chi-square distributed with degrees of freedom 3. We calibrate the
mean of σ2
g to 1. i.e. σ2
g/3.
We compare our method to permutation tests and t-tests using a threshold
of 0.05 to determine signiﬁcance. These two methods are standard in biological
applications. Our method is much more accurate than other two methods (Table


## Page 7


98
J. Cabrera and C. Yu
1-4, Figure 2). Each cell in the table is the mean (standard deviation) based on 10
times simulations on each condition. In Figure 2, the straight line represents the
true values and the red line is obtained by the smooth spline function. We also
calculate the pFDR of our method in diﬀerent values of lambda (Table 5-6). pFDR
decreases when the true value increases.
3. Discussion and extensions
In this paper we propose an algorithm for estimating the proportion of diﬀerentially
expressed genes in a microarray experiment. We also show that the estimator of
the distribution of the variance converges to a ﬁx point. We performed a simulation
study to check the performance of our estimate and it is shown to be “satisfac-
tory” and we show that our method has better performance than other alternatives
such as permutation tests and standard two-sample t- test. The simulations were
performed under normal and gamma error distribution and with constant vari-
ances and chi-square variances. In addition we illustrate the method with real data
examples on mice and mice2 (Table 7, Figure 3). In the real data examples we
obtained estimates of the proportion of signiﬁcant genes that were more realistic
than those produced by the other methods. Hence, this algorithm gives us more
accurate prediction to detect diﬀerential genes.
This same method is generally extendable to other more complicated modeling
procedures such as the one-way ANOVA F-test and other linear models. The same
model is used and the same ideas are easily extendable into a second paper. Another
paper will deal with the GO issues, by modeling the p-values and getting a null
distribution that will be used to detect diﬀerentially expressed gene network and
subsets.
Table 1
Normal(0,1)
δ
true λ
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
t-test
0.066
(0.002)
0.085
(0.003)
0.103
(0.002)
0.119
(0.003)
0.136
(0.003)
0.154
(0.005)
0.171
(0.004)
0.186
(0.004)
0.207
(0.004)
1
Permutation
test
0.039
(0.002)
0.051
(0.002)
0.063
(0.002)
0.073
(0.003)
0.085
(0.003)
0.096
(0.003)
0.107
(0.003)
0.116
(0.003)
0.130
(0.003)
1
New method
0.071
(0.058)
0.163
(0.091)
0.226
(0.084)
0.282
(0.072)
0.304
(0.049)
0.422
(0.081)
0.473
(0.105)
0.479
(0.145)
0.518
(0.120)
2
t-test
0.109
(0.002)
0.171
(0.002)
0.234
(0.003)
0.294
(0.003)
0.354
(0.003)
0.415
(0.004)
0.474
(0.005)
0.534
(0.004)
0.595
(0.004)
2
Permutation
test
0.074
(0.003)
0.120
(0.002)
0.168
(0.002)
0.214
(0.003)
0.259
(0.004)
0.305
(0.003)
0.350
(0.005)
0.397
(0.005)
0.442
(0.004)
2
New method
0.087
(0.020)
0.196
(0.022)
0.321
(0.034)
0.431
(0.033)
0.522
(0.030)
0.635
(0.045)
0.720
(0.034)
0.823
(0.022)
0.923
(0.021)


## Page 8


Estimating the proportion of diﬀerentially expressed genes
99
Table 2
N(0,a),a ∼χ2
(3)/3
δ
true λ
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
t-test
0.066
(0.001)
0.087
(0.004)
0.110
(0.002)
0.134
(0.004)
0.157
(0.003)
0.180
(0.004)
0.204
(0.003)
0.227
(0.004)
0.252
(0.003)
1
Permutation
test
0.045
(0.002)
0.060
(0.002)
0.077
(0.002)
0.095
(0.003)
0.112
(0.002)
0.129
(0.003)
0.148
(0.004)
0.163
(0.003)
0.182
(0.002)
1
New method
0.079
(0.072)
0.145
(0.096)
0.153
(0.040)
0.301
(0.069)
0.327
(0.062)
0.436
(0.119)
0.513
(0.138)
0.576
(0.138)
0.577
(0.116)
2
t-test
0.105
(0.002)
0.172
(0.002)
0.237
(0.003)
0.303
(0.003)
0.370
(0.004)
0.435
(0.003)
0.498
(0.003)
0.565
(0.006)
0.630
(0.003)
2
Permutation
test
0.080
(0.003)
0.134
(0.002)
0.186
(0.003)
0.241
(0.004)
0.295
(0.003)
0.347
(0.004)
0.400
(0.004)
0.451
(0.005)
0.508
(0.005)
2
New method
0.111
(0.027)
0.207
(0.034)
0.311
(0.032)
0.413
(0.030)
0.514
(0.025)
0.609
(0.022)
0.712
(0.017)
0.811
(0.018)
0.914
(0.015)
Table 3
Gamma(1, 1)
δ
true λ
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
t-test
0.067
(0.002)
0.094
(0.004)
0.123
(0.003)
0.150
(0.004)
0.178
(0.004)
0.207
(0.004)
0.233
(0.004)
0.264
(0.004)
0.292
(0.003)
1
Permutation
test
0.053
(0.001)
0.075
(0.002)
0.099
(0.003)
0.120
(0.003)
0.143
(0.004)
0.168
(0.003)
0.190
(0.003)
0.213
(0.006)
0.237
(0.003)
1
New method
0.059
(0.043)
0.151
(0.035)
0.225
(0.075)
0.310
(0.062)
0.321
(0.099)
0.377
(0.110)
0.482
(0.094)
0.504
(0.119)
0.626
(0.107)
2
t-test
0.108
(0.002)
0.177
(0.002)
0.246
(0.003)
0.313
(0.003)
0.381
(0.005)
0.450
(0.003)
0.521
(0.004)
0.588
(0.005)
0.657
(0.005)
2
Permutation
test
0.090
(0.003)
0.151
(0.002)
0.212
(0.002)
0.272
(0.003)
0.330
(0.004)
0.391
(0.004)
0.454
(0.003)
0.514
(0.005)
0.576
(0.004)
2
New method
0.126
(0.048)
0.232
(0.045)
0.310
(0.024)
0.417
(0.020)
0.515
(0.023)
0.613
(0.010)
0.712
(0.015)
0.802
(0.014)
0.912
(0.013)
Table 4
t5
δ
true λ
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
t-test
0.065
(0.003)
0.086
(0.003)
0.109
(0.005)
0.130
(0.004)
0.153
(0.003)
0.174
(0.004)
0.197
(0.003)
0.218
(0.004)
0.243
(0.002)
1
Permutation
test
0.043
(0.002)
0.058
(0.002)
0.075
(0.004)
0.090
(0.003)
0.106
(0.003)
0.122
(0.003)
0.138
(0.004)
0.153
(0.003)
0.170
(0.003)
1
New method
0.074
(0.060)
0.141
(0.100)
0.208
(0.065)
0.212
(0.074)
0.319
(0.080)
0.368
(0.091)
0.490
(0.133)
0.530
(0.128)
0.641
(0.084)
2
t-test
0.112
(0.002)
0.177
(0.002)
0.241
(0.002)
0.309
(0.005)
0.373
(0.003)
0.440
(0.003)
0.507
(0.004)
0.575
(0.005)
0.639
(0.005)
2
Permutation
test
0.083
(0.002)
0.136
(0.003)
0.190
(0.002)
0.246
(0.004)
0.298
(0.003)
0.352
(0.004)
0.408
(0.004)
0.461
(0.006)
0.517
(0.006)
2
New method
0.113
(0.030)
0.205
(0.013)
0.309
(0.028)
0.411
(0.027)
0.516
(0.022)
0.610
(0.016)
0.718
(0.027)
0.811
(0.017)
0.918
(0.013)
Table 5
pFDR for our method with Normal(0,1) error distribution
true λ
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
δ = 1
0.5471
(0.1679)
0.3768
(0.1371)
0.3823
(0.0537)
0.2372
(0.0535)
0.2372
(0.0535)
0.1924
(0.0354)
0.1486
(0.0363)
0.0860
(0.0209)
0.0482
(0.0131)
δ = 2
0.1963
(0.0753)
0.1924
(0.0741)
0.2416
(0.0876)
0.1533
(0.0393)
0.1215
(0.0406)
0.0965
(0.0242)
0.0841
(0.0255)
0.0601
(0.0093)
0.0465
(0.0112)


## Page 9


100
J. Cabrera and C. Yu
Fig 2.
Example comparing our method to the Permutation and t methods. The true errors are
N(0, σ2), σ2 ∼χ2
(3)/3.
Fig 3. Density estimators for the p-values obtained from two toxicology datasets.


## Page 10


Estimating the proportion of diﬀerentially expressed genes
101
Table 6
pFDR for our method with Normal(0, σ2), σ ∼χ2
(3)/3 error distribution
true λ
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
δ = 1
0.634
(0.069)
0.480
(0.060)
0.375
(0.060)
0.323
(0.040)
0.233
(0.053)
0.185
(0.048)
0.102
(0.018)
0.094
(0.017)
0.047
(0.0135)
δ = 2
0.325
(0.099)
0.226
(0.054)
0.167
(0.042)
0.139
(0.022)
0.119
(0.020)
0.107
(0.016)
0.074
(0.017)
0.063
(0.014)
0.037
(0.0047)
Table 7
Results for the three methods applied to
two real examples from toxicology
Estimated π
Mice
Mice2
t −test
0.245
0.499
P ermutation test
0.220
0.443
New method
0.107
0.363
References
[1] Amaratunga, D. and Cabrera, J. (2001). Statistical analysis of viral mi-
crochip data. J. Amer. Statist. Assoc. 96 1161–1170. MR1963418
[2] Amaratunga, D. and Cabrera, J. (2003). Exploration and Analysis of
DNA Microarray and Protein Array Data. Wiley, New York.
[3] Amaratunga, D. and Cabrera, J. (2006). Diﬀeretial expression in DNA
microarray and protein array experiment. Technical Report 06-001, Depart-
ment of Statistics, Rutgers University.
[4] Baldi, P. and Long, A. D. (2001). A Bayesian framework for the analysis
of microarray expression data: Regularized t-test and statistical inferences of
gene changes. Bioinformatics 7 509–519.
[5] Broberg, P. (2003). Ranking genes with respect to diﬀerential expression.
Genome Biology 4 R41.
[6] Efron, B., Tibshirani, R., Storey, J. D. and Tusher, V. (2001). Em-
pirical Bayes analysis of a microarry experiment. J. Amer. Statist. Assoc. 96
1151–1160. MR1946571
[7] Fisher, R. A. (1934). Statistical Methods for Researcher Workers. Oxford
University Press.
[8] Gene Otology Consortium (2000). Gene ontology: Tool for the uniﬁcation
of biology. Nature Genet. 25 25–29.
[9] Huber, P. J. (1981). Robust Statistics. Wiley, New York. MR0606374
[10] Lee, M. L. T., Kuo, F. C., Whitmore, G. A. and Sklar, J. (2000).
Importance of replication in microarray gene expression studies: statistical
methods and evidence from repetitive cDNA hybridizations. Proceedings of
the National Academic of Sciences 97 9834–9839.
[11] Lonnstedt, I. and Speed, T. P. (2002). Replicated microarray data. Statist.
Sinica 12 31–46. MR1894187
[12] Newton, M. A., Kendziorski, C. M., Richmond, C. S., Blattner, F.
R. and Tsui, K. W. (2001). On diﬀerential variability of expression ratios:
Improving statistical inference about gene expression changes from microarray
data. J. Comp. Biol. 8 37–52.
[13] Pavlidis, P. et al. (2004). Using the gene ontology for microarray data
mining: A comparison of Methods and Application to Age Eﬀect in Human
Prefrontal Cortex. Neurochemical Research 29 1213–1222.


## Page 11


102
J. Cabrera and C. Yu
[14] Raghavan, R., Amaratunga, D., Cabrera, J. Nie, A. Qin, J. and
Mcmillian, M. (2006). On methods for gene function scoring as a mean of fa-
cilitating the interpretation of microarray results. J. Comp. Biol. 13 798–809.
MR2255444
[15] Schena, M., Shalon, D., Davis, D. R. and Brown, P. O. (1995). Quan-
titative monitoring of gene expression patterns with a complementary DNA
microarray. Science 270(5235) 467–470.
[16] Storey, J. D. and Tibshirani, R. (2001). Estimating false discovery rates
under dependence, with applications to DNA microarrays. Technical Report
2001–18, Dep. Statistics, Stanford Universtity, Stanford.
[17] Tusher, V., Tibshirani, R. and Chu, G. (2001). Signiﬁcance analysis of
microarrays applied to the ionizing radiation response. PNAS 98 5116–5124.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
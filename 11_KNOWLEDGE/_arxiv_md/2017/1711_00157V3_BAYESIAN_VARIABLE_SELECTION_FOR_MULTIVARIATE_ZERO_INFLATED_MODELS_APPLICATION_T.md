---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1711.00157v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1711.00157v3_Bayesian_Variable_Selection_for_Multivariate_Zero-Inflated_Models__Application_t

> Source: 1711.00157v3_Bayesian_Variable_Selection_for_Multivariate_Zero-Inflated_Models__Application_t.pdf

> Pages: 29

---


## Page 1


arXiv:1711.00157v3  [stat.AP]  20 May 2018
Bayesian Variable Selection for Multivariate
Zero-Inﬂated Models: Application to
Microbiome Count Data
KYU HA LEE∗
The Forsyth Institute, Cambridge, Massachusetts, U.S.A.
and
BRENT A. COULL
Harvard T.H. Chan School of Public Health, Boston, Massachusetts, U.S.A.
and
ANNA-BARBARA MOSCICKI
University of California, Los Angeles, California, U.S.A
and
BRUCE J. PASTER
The Forsyth Institute, Cambridge, Massachusetts, U.S.A.
and
JACQUELINE R. STARR
The Forsyth Institute, Cambridge, Massachusetts, U.S.A.
May 22, 2018
Abstract
Microorganisms play critical roles in human health and disease. They live in di-
verse communities in which they interact synergistically or antagonistically.
Thus
for estimating microbial associations with clinical covariates, such as treatment ef-
fects, joint (multivariate) statistical models are preferred. Multivariate models allow
one to estimate and exploit complex interdependencies among multiple taxa, yielding
more powerful tests of exposure or treatment eﬀects than application of taxon-speciﬁc
univariate analyses. Analysis of microbial count data also requires special attention
because data commonly exhibit zero inﬂation, i.e. more zeros than expected from
a standard count distribution. To meet these needs, we developed a Bayesian vari-
able selection model for multivariate count data with excess zeros that incorporates
∗To whom correspondence should be addressed. This work was supported by NIH grant CA134294,
ES000002, HD052104, HD052102.
1


## Page 2


information on the covariance structure of the outcomes (counts for multiple taxa),
while estimating associations with the mean levels of these outcomes. Though there
has been much work on zero-inﬂated models for longitudinal data, little attention has
been given to high-dimensional multivariate zero-inﬂated data modeled via a general
correlation structure. Through simulation, we compared performance of the proposed
method to that of existing univariate approaches, for both the binary (“excess zero”)
and count parts of the model. When outcomes were correlated the proposed variable
selection method maintained type I error while boosting the ability to identify true
associations in the binary component of the model. For the count part of the model,
in some scenarios the univariate method had higher power than the multivariate ap-
proach.
This higher power was at a cost of a highly inﬂated false discovery rate
not observed with the proposed multivariate method. We applied the approach to
oral microbiome data from the Pediatric HIV/AIDS Cohort Oral Health Study and
identiﬁed ﬁve (of 44) species associated with HIV infection.
Keywords: Bayesian variable selection; Markov chain Monte Carlo; microbiome sequencing
data, multivariate analysis; zero-inﬂated models.
1
Introduction
The human microbiome plays a critical role in maintaining health and causing both acute
and chronic disease.
Microbes live in communities in which multiple species establish
synergistic and antagonistic relationships (Pﬂughoeft and Versalovic, 2012). These inter-
actions allow some species to thrive and keep others in check.
The complex biological
dependencies among taxa demand statistical methods that account for and exploit this
interdependence. There are valid and powerful methods for jointly analyzing microbiome
sequence data as predictors of health outcomes, but there are fewer methodologic options
for analyzing microbiome community data as a set of joint endpoints. We speciﬁcally ad-
dress three challenges that commonly arise in analysis of microbiome sequencing data as
responses (dependent variables): excess zeros, interdependence of the endpoints, and the
need for outcome-speciﬁc covariate selection.
First, in most human microbiome studies, a large proportion of microbial taxa is absent
in the majority of subjects, leading to many more zero counts for each taxon than expected
on the basis of a Poisson, negative binomial, or Dirichlet-multinomial distribution (e.g.,
see Supplementary Material A) (Chen and Li, 2013). Application of a conventional linear
model that uses untransformed or logarithmic-transformed counts is inappropriate for zero-
inﬂated data (Loeys et al., 2012; Xu et al., 2015).
An intuitive approach to analyzing
2


## Page 3


zero-inﬂated count data is to view the data as arising from an underlying zero-inﬂated
distribution, which is a mixture of a point mass at zero and a count distribution, such as
Poisson (Lambert, 1992).
Second, as mentioned above, microbiome sequencing data are typically multivariate
(joint response) count data sampled from communities of interdependent species. Na¨ıve
application of a univariate, taxon-by-taxon approach implicitly assumes that counts of each
taxon are uncorrelated. Although one could control for the type I error in this approach,
this generally results in loss of power (Breiman and Friedman, 1997; La Rosa et al., 2012).
Multivariate non-parametric methods are available compare bacterial community composi-
tion between two groups (Mantel, 1967; Mantel and Valand, 1970; Anderson, 2001); these
are generally less powerful than regression methods and often do not quantify the magnitude
of group diﬀerences. One approach for joint modeling of multivariate microbial sequence
count data is Dirichlet-multinomial regression (Holmes et al., 2012; La Rosa et al., 2012;
Chen and Li, 2013; Wadsworth et al., 2017). However, the Dirichlet-multinomial model
imposes restrictions that may misrepresent features of multivariate taxa count data dis-
tributions. For example, despite that relationships among microbial species can be either
positively or negatively correlated, the dependence between Dirichlet variates is always
negatively correlated (Aitchison and Ho, 1989; Li, 2015).
Multivariate zero-inﬂated regression models can address both excess zeros as well as
interdependent responses.
Such methods that have been developed to date have been
scaled to model only a small number of interdependent count endpoints, which include
bivariate (Arab et al., 2012; Fox, 2013) and trivariate (Li et al., 1999) zero-inﬂated Pois-
son models. In some cases, existing methods have incorporated a restrictive covariance
structure among outcomes, which may not always be appropriate. Speciﬁc examples of
such restrictions include zero-inﬂated models for longitudinal data only with variance com-
ponents (with no covariance components) (Lee et al., 2006; Hall, 2000; Long et al., 2015),
models with dependence structures speciﬁc to spatial-temporal data (Earnest et al., 2007;
Fernandes et al., 2009; Wang et al., 2015a), and models including latent factors that can
induce only positive correlations among outcomes (Neelon and Chung, 2017).
A third impediment to developing and applying a multivariate analysis technique to
3


## Page 4


microbiome data is that due to having more than one endpoint, there is a large number of
potential covariate-endpoint associations to be modeled. It is well recognized that variable
selection helps improve prediction accuracy and reduce the cost of measurement and storage
of future data. The need for variable selection techniques is well appreciated for high-
dimensional covariate data and may be less well known in the context of multiple outcomes.
Although there exist variable selection methods for multivariate normal (Brown et al., 1998;
Lee et al., 2017) or multinomial responses (Wadsworth et al., 2017), we know of no such
technique applied to methods for multivariate zero-inﬂated outcomes.
We have developed multivariate zero-inﬂated regression models by relaxing require-
ments regarding the covariance structure and incorporating a Bayesian variable selection
approach. The proposed methods can be used to identify zero-inﬂated count outcomes
associated with a set of covariates while accounting for the covariance structure of the
outcomes.
Since it is implausible that all outcomes are relevant to the same subset of
covariates, we enable the proposed model to perform outcome-speciﬁc variable selection,
i.e., to identify exposures or treatments associated with particular outcomes, in this case
microbial taxa. Spike-and-slab approaches have been widely used for Bayesian variable
selection(George and McCulloch, 1993, 1997), including for multivariate linear regression
problems (Brown et al., 1998; Lee et al., 2017). In this work, we extend the spike-and-slab
approach to the context of multivariate zero-inﬂated data.
We use the newly developed model to analyze data from the Pediatric HIV/AIDS
Cohort Oral Health Study (PHACS). PHACS is an ongoing prospective cohort study at 15
US clinical sites, designed to assess the health eﬀects of HIV infection and antiretroviral
therapy (ART) on youth perinatally infected with HIV (PHIV) compared with exposed
but uninfected (PHEU) youth (Alperen et al., 2014; Tassiopoulos et al., 2016; Starr et al.,
2018). The data analyzed were from a cross-sectional study focused on oral health and the
oral microbiome (Moscicki et al., 2016; Ryder et al., 2017). All participants were exposed
to HIV perinatally, the period when they became HIV infected if at all. Emerging from
the womb, it is likely that they began acquiring their oral microbiota at birth and should
have had oral microbiota similar to those of adults by 3 years of age (Mueller et al., 2015;
Perez-Mu˜noz et al., 2017). Thus, if there is a causal association, the oral bacterial sequences
4


## Page 5


we measured at 10-22 years of age more likely resulted from perinatal HIV infection rather
than the reverse. This is why we treat taxa’s counts as endpoints and HIV as the exposure.
The goals of this analysis are (i) to identify taxa associated with HIV infection; and (ii) to
estimate and test the association of HIV infection with counts of the identiﬁed taxa.
The remainder of this paper is organized as follows. Section 2 describes the proposed
Bayesian framework, including model formulation and speciﬁcation of prior distributions.
Section 3 describes results from simulation studies conducted to compare the operating per-
formance of the proposed variable selection approach versus an existing univariate method.
Section 4 describes results from the PHACS data analysis. In section 5 we further discuss
the method and results.
2
Methods
In this section, we describe the proposed multivariate zero-inﬂated model, present prior dis-
tributions for model parameters and the variable selection strategy, discuss interpretation of
the regression parameters, and summarize the computational scheme and implementation
(see Supplementary Material B for a summary of model parameters and C for implemen-
tation details).
2.1
Model Formulations
Suppose that count outcomes Yij are observed for taxon j=1,. . . ,q and subject i=1,. . . ,n.
We use an approach that assumes that Yij follow a multivariate zero-inﬂated Poisson
(MZIP) distribution, which is a mixture of a Poisson distribution and point mass dis-
tribution at zero (I0):
Yij
∼
Poisson(λij),
if Uij = 1,
∼
I0,
if Uij = 0,
(1)
where Uij is an unobservable indicator for the excess zeros for taxon j in subject i, and λij
is the mean of the Poisson distribution. The model implies that some zeros occur through a
5


## Page 6


Poisson process whereas others represent the impossibility for a given taxon to be observed
in some subjects. In practice, regression analysis based on the MZIP model proceeds by
placing structure on λij and P[Uij = 1], speciﬁcally as a function of the covariates and
random eﬀects. Toward this, let xi and zi be a vector of px and pz covariates for the ith
subject that will be considered in the model for λij and P[Uij = 1], respectively. With this
formulation it is not necessary for the presence and the count of a taxon to depend on the
same set of covariates.
For the count (Poisson) model part, we consider the following general modeling speci-
ﬁcation:
log(λij)
=
β0j + x⊤
i βj + log(ξi) + Vij,
(2)
where β0=(β01,. . . ,β0q)⊤are the outcome-speciﬁc intercepts and βj=(βj1,. . . ,βjpx)⊤are
the outcome-speciﬁc vectors of ﬁxed-eﬀect regression parameters. The random eﬀects Vi =
(Vi1, . . . , Viq)⊤characterize the unobserved characteristics that are associated with the mean
count for taxon j in subject i and account for within-subject correlations. The term log(ξi)
is included as an oﬀset variable for settings in which one is interested in the incidence
density λij/ξi. For application to genetic sequence counts, setting ξi to the total number
of sequencing reads accounts for individual variation in sequencing depth.
To account for the dependency structure in the binary part of the model, we adopt
a multivariate probit model (Ashford and Sowden, 1970). Letting Uij=I(wij ≥0), with
indicator function I(·) , we consider a multivariate normal (MVN) distribution for the
latent variable wi=(wi1,. . . ,wiq)⊤, with location vector α0 + A⊤zi and variance-covariance
matrix R. Here, α0=(α01,. . . ,α0q)⊤are the intercepts and A is the pz ×q coeﬃcient matrix
whose columns are αj=(αj1, . . . ,αjpz)⊤, j=1,· · · ,q. Then the probability density function
of Uij is given by
wi|α0, A, R, zi
∼
MVNq(α0 + A⊤zi, R).
(3)
R is restricted to be a correlation matrix to ensure identiﬁability of all model parameters
(Chib and Greenberg, 1998; Liu, 2001). R measures the dependence between Uij and Uij′
6


## Page 7


by using the correlations among the elements of the vector wi.
Let ⃗Y , ⃗w, ⃗V , and φ
denote the collections of Yi, wi, Vi, and φi, respectively, across all subjects. Let B be the
px ×q coeﬃcient matrix whose columnsβj=(βj1, . . . ,βjpx)⊤, j=1,· · · ,q. Combining (1), (2),
and (3), the augmented data likelihood function, as a function of the unknown parameters
Θ={α0, A, β0, B, ⃗V , R}, is:
L(⃗Y , ⃗w|Θ)
=
n
Y
i=1
qY
j=1

I(wij ≥0)exp {yij log(λij) −λij}
yij!
+ I(wij < 0)I(yij = 0)

×
n
Y
i=1
(2π)−q/2 |R|−1
2 exp

−1
2(wi −α0 −A⊤zi)⊤R−1(wi −α0 −A⊤zi)

.(4)
2.2
Prior Speciﬁcation and Covariance structure
We complete the Bayesian formulation of the proposed framework by specifying prior dis-
tributions for the unknown parameters. To facilitate outcome-speciﬁc variable selection,
we adopt spike-and-slab priors for the regression parameters in both parts of the proposed
model. Such a prior has been widely used in the context of Bayesian stochastic search vari-
able selection (George and McCulloch, 1993, 1997). Speciﬁcally, we assign the following
priors for βj and αj:
βj,k|γj,k, σ2
β,k
∼
γj,kNormal(0, v2
β,jσ2
β,k) + (1 −γj,k)I0 and
αj,l|δj,l, σ2
α,l
∼
δj,lNormal(0, v2
α,jσ2
α,l) + (1 −δj,l)I0,
(5)
where γk = (γ1,k, . . . , γq,k)⊤and δl = (δ1,l, . . . , δq,l)⊤, for k = 1, . . . , px, l = 1, . . . , pz, are
vectors
of binary latent variables indicating the membership of each regression parameter to one
of the mixture components in (5). The kth covariate is considered to be associated with
mean counts for the j-th outcome if the data support γj,k = 1 over γj,k = 0. A similar
interpretation holds for δj,k. We use independent Bernoulli hyperpriors for γj,k and δj,l with
inclusion probability ωβ,k and ωα,l, respectively.
As outlined in Section 2.1, the dependence among mean bacterial counts of multiple
taxa is accounted for by the distribution of random eﬀects Vi. Speciﬁcally, we structure
this dependence through a hierarchical Poisson-logNormal model (Aitchison and Ho, 1989;
7


## Page 8


Fox, 2013), which corresponds to a MVN prior, Vi|ΣV ∼MVN(0, ΣV ). We use an un-
structured covariance pattern for ΣV and R, thus imposing no speciﬁc structure for the
dependence among outcomes. Under the unstructured model, we adopt a conjugate hyper-
prior, inverse-Wishart(Ψ0, ρ0), for ΣV . For R, we use π(R) ∝|R|−(q+1)/2, which is the prior
for a correlation matrix based on Jeﬀreys’ prior distribution for the variance-covariance ma-
trix (Box and Tiao, 2011). In addition, we assign α0 ∼MVN(µα0, σ2
α0R), where µα0 is the
hyperparameter to be speciﬁed. We discuss the desirable properties of the prior distribu-
tions for R and α0 in Supplementary Material C (Chib and Greenberg, 1998; Liu and Sun,
2000). We assign MVN(µβ0, σ2
β0Iq) for the intercepts β0, where µβ0 is the hyperparameter
to be speciﬁed, and Iq is the q×q identity matrix. Lastly, we use the conjugate hyper-
priors inverse-Gamma(aβ,k, bβ,k), inverse-Gamma(aα,l, bα,l), inverse-Gamma(aβ0, bβ0) and
inverse-Gamma(aα0, bα0), for σ2
β,k, σ2
α,l, σ2
β0, and σ2
α0, respectively.
2.3
Induced Marginal Incident Density Ratio
Because the MZIP model is a mixture model, the regression parameters, βj,k, have latent
interpretations: βj,k represents the change in log mean count of taxon j associated with a
one-unit increase in the covariate k, in a susceptible sub-population (Preisser et al., 2012).
The relationship between E[Yij|Vij] and the parameters from the proposed MZIP model is
given by
E[Yij|Vij] = λijP(Uij = 1) = exp
 β0j + x⊤
i βj + log(ξi) + Vij

Φ
 α0j + z⊤
i αj

,
where Φ(·) is the cumulative distribution function of the standard normal distribution. For
models with log-links and normally distributed random eﬀects such as the one we propose,
it is straightforward to marginalize the conditional expectation over the random eﬀects
distribution (Long et al., 2015). Under a model with xi = zi, the ratio of means for a
8


## Page 9


one-unit increase in covariate k is given by
IDR(xi,(−k))
=
E[Yij|xik = x + 1, xi,(−k)]
E[Yij|xik = x, xi,(−k)]
= E

E[Yij|xik = x + 1, xi,(−k), Vij]

E

E[Yij|xik = x, xi,(−k), Vij]

=
eβjk Φ

α0j + x⊤
i,(−k)αj,(−k) + (x + 1)αj,k

Φ

α0j + x⊤
i,(−k)αj,(−k) + xαj,k

,
(6)
where xi,(−k) and αj,(−k) are the vectors xi and αj, respectively, with the k-th element
removed. Although we obtain IDR(xi,(−k)) by marginalizing E[Yij|Vij, Uij = 1] over the
latent mixture distribution and the distribution of random eﬀect Vij, the quantity still
depends on the values of other covariates xi,(−k), which can be addressed several ways
(Preisser et al., 2012). For continuous covariates, one could obtain a covariate-adjusted
IDR(¯x(−k)) by either i) inserting mean values of covariates xi,(−k), or ii) assuming speciﬁc
covariate distributions and marginalizing the quantity over these distributions. For dis-
crete covariates, one could iii) empirically marginalize the IDR(xi,(−k)) over the observed
distribution of covariates, or iv) present multiple diﬀerent values for the IDR(xi,(−k)), one
for each category deﬁned by unique covariate proﬁles.
As has been well described, estimating the variance of measures such as the IDR(xi,(−k))
in a frequentist framework would require an extra statistical technique such as bootstrap
resampling (Albert et al., 2014). An advantage of the Bayesian paradigm is that estimation
of uncertainty for IDR(xi,(−k)) follows directly from the variance of its posterior distribu-
tion, estimated by evaluating its expression at each scan of the Markov chain Monte Carlo
(MCMC) scheme.
2.4
Markov Chain Monte Carlo
We perform estimation and inference for the proposed model by using a Gibbs sampling al-
gorithm to generate samples from the posterior distribution. In the corresponding MCMC
scheme, parameters are updated either by exploiting conjugacies inherent in the model
structure or by using a Metropolis-Hastings step. However, MCMC is far from straight-
forward because the joint posterior distribution under the proposed framework involves i)
the unobserved multivariate latent variables, wi; ii) the augmented data likelihood func-
tion based upon the latent mixture distribution; iii) spike-and-slab mixture priors for the
9


## Page 10


regression parameters; iv) a high-dimensional parameter space due to the unstructured
pattern for ΣV and R; and v) restrictions on the correlation parameters in R. Therefore,
we develop an eﬃcient MCMC sampling scheme based on a data augmentation algorithm
(Tanner and Wong, 1987) in which the computational challenge of high-dimensionality is
avoided by iterating between an “imputation step,” in which values of the unobserved latent
variables wi are imputed and updated, and a “posterior step,” in which the model parame-
ters are updated. In the posterior step, we used a parameter expanded data augmentation
method (Liu, 2001) to update R for computational eﬃciency (see Supplementary Material
C for detailed description of the proposed computation scheme). We have developed a
series of core functions in C to improve the computation speed, for which we provide the
algorithm in the mBvs package for R (https://cran.r-project.org/web/packages/mBvs). As
an example of computational time, it takes approximately 3 minutes to generate 10,000
MCMC scans on a 2.5 GHz Intel Core i7 MacBook Pro for the analysis of the PHACS data
(n=254, q=44, px=pz=2).
3
Simulation Studies
We evaluated the performance of the proposed method on simulated data. We generated
data sets under six scenarios with varying outcome correlation structures and association
patterns between a covariate and the vector of outcomes in the two model parts.
3.1
Set-Up and Data Generation
We generated samples of size n = 300 with q = 20 outcomes and px = pz = 1 covariate
under the proposed model given in (1), (2), and (3). The covariate was generated from
Normal(0, 2) and the intercepts set to α0 = 1q and β0 = 5 · 1q. In Scenarios I-III and VI,
we varied the scale and sign of the association between the covariate and outcomes in the
two model parts by setting B = A =[0.05, 0.10, 0.15, 0.20, 0.25, -0.05, -0.10, -0.15, -0.20,
-0.25, 0⊤
10]. In Scenario IV, the covariate was associated with outcomes in only one of the
two model parts: B =[0.05, 0.10, 0.15, 0.20, 0.25, 0⊤
15] and A =[05, 0.05, 0.10, 0.15, 0.20,
0.25, 0⊤
10]. We considered the null case in Scenario V by setting all elements of B and A
10


## Page 11


to zero. We set each variance-covariance matrix ΣV in the count part of the model and
R in the binary part of the model to a correlation matrix with an exchangeable structure
with correlation c1 within the block of the ﬁrst ten outcomes, an exchangeable structure
with correlation c2 within the block of the second 10 outcomes, and a common cross-block
correlation of c3 for pairs of outcomes from diﬀerent blocks. In Scenarios I, IV, and V, the
outcomes associated with the covariate were highly correlated and outcomes unassociated
with the covariate only moderately correlated, (c1, c2, c3)=(0.70, 0.30, 0.20). In Scenario II,
the outcomes associated with the covariate were moderately correlated and the remaining
outcomes weakly correlated, (c1, c2, c3)=(0.40, 0.05, 0.10). In Scenario III, the outcomes
associated with the covariate were weakly correlated and those unassociated with the co-
variate highly correlated, (c1, c2, c3)=(0.20, 0.70, 0.30). In Scenario VI, each outcome is
assumed to follow a univariate zero-inﬂated Poisson (UZIP) distribution, indicating (c1, c2,
c3)=(0, 0, 0) (independence), and diag(ΣV )=diag(R)=0 (no overdispersion).
3.2
Analyses and Speciﬁcation of Hyperparameters
We ﬁt the proposed MZIP model to 600 simulated data sets, 100 under each of the six
scenarios.
For comparison purposes in each data set, we also implemented UZIP re-
gression with and without the lasso penalty by using the pscl(Zeileis et al., 2008) and
mpath(Wang et al., 2015b) R packages, respectively. As outlined in Section 2.2, the pro-
posed Bayesian framework requires the speciﬁcation of several hyperparameters. For the
intercepts β0 and α0 and their variance components σ2
α0 and σ2
β0, we assigned noninfor-
mative priors by setting (µβ0, aβ0, bβ0)=(µα0, aα0, bα0)=(0q, 0.7, 0.7). For the regression
parameters, β and α, and their variance components, σ2
α and σ2
β, the hyperparameters (vβ,j,
aβ,k, bβ,k)=(vα,j, aα,l, bα,l), k = 1, . . . , px, l = 1, . . . , pz, were set to (10, 0.7, 0.7) to make
the corresponding priors fairly noninformative. The hyperparameters ωβ,k = ωα,l were set
to either 0.1 or 0.5, implying 0.1 or 0.5 a priori probability, respectively, of each covariate
to be selected as associated with each outcome. Finally, we set (Ψ0, ρ0) = (ψIq, q + ψ + 1)
with ψ = 3, corresponding to a prior distribution of ΣV centered at Iq and with variance
of the diagonal elements equal to 2.0. We ran each MCMC chain for 1 million iterations
with the ﬁrst half taken as burn-in.
11


## Page 12


For the proposed Bayesian MZIP model, we perform variable selection based on the
marginal posterior distribution of variable selection indicators, γj,1 and δj,1. Here, we ap-
plied a marginal posterior probability cutoﬀof 0.5. Between the two univariate approaches
implemented, in initial simulation studies the penalized UZIP model tended to select the
covariate for all outcomes in both model parts when the outcomes were correlated. For
this reason, and because it would be one typical practice, for the UZIP regression analyses
we performed variable selection by applying 95% conﬁdence intervals with a false discovery
rate (FDR)-controlling procedure (Benjamini and Hochberg, 1995) to account for multiple
comparisons.
We assessed performance of the variable selection feature of the model by calculat-
ing four quantities based on the true positives (TP; the number of outcomes associated
with the covariate and selected into the model) and false positives (FP; the number of
outcomes unrelated to the covariate and mistakenly selected into the model), where τ is
the number of outcomes that are truly associated with the covariate: the true positive
rate, TPR=TP/τ, the false positive rate, FPR=FP/(20 −τ), the positive predictive value,
PPV=TP/(TP+FP), and the negative predictive value, NPV=(20−τ−FP)/(20−TP−FP).
3.3
Results
We focus the presentation of results in this section on the MZIP model with ωβ,1=ωα,1=0.1.
This is to demonstrate the improvement gained by the proposed multivariate approach
over an analogous univariate method, while implementing the fairest comparison to the
univariate method. When the values of the overall prior inclusion probabilities (ωβ,1 and
ωα,1) increased from 0.1 to 0.5, the MZIP model tended to select one to two more variables
on average, yielding higher TPR and NPV but also a bit higher FPR and lower PPV in
both parts of the model (Table 1). When the outcome variables were uncorrelated (Scenario
VI), the variable selection capability for the MZIP model with ωβ,1=ωα,1=0.1 was almost
the same as that of UZIP model.
Across scenarios in which the outcomes were correlated (I-III), the binary part of the
MZIP model was more sensitive than in the UZIP approach (Table 1), for example, with
TPR=61% versus 54% in Scenario II, respectively. The TPR in UZIP models was insensi-
12


## Page 13


Table 1: Four operating characteristics∗(%) and the number of outcomes selected to be associ-
ated with the covariate (qsel) for the univariate zero-inﬂated Poisson (UZIP)† and the proposed
multivariate zero-inﬂated Poisson (MZIP)‡ models across six simulation scenarios described in
Section 3.1.
UZIP
MZIP
(ωα = ωβ = 0.1)
(ωα = ωβ = 0.5)
Scenario
Binary
Count
Binary
Count
Binary
Count
Mean
(SD)
Mean
(SD)
Mean
(SD)
Mean
(SD)
Mean
(SD)
Mean
(SD)
TPR
54.3
(9.7)
99.1
(2.9)
67.4
(8.4)
82.5
(5.5)
78.4
(8.1)
87.4
(5.5)
FPR
0.1
(1.0)
86.0
(11.1)
0.3
(1.8)
0.8
(2.8)
4.6
(6.5)
3.1
(5.5)
I
PPV
99.8
(1.7)
53.7
(3.4)
99.6
(2.4)
99.1
(3.0)
95.0
(6.8)
96.9
(5.3)
NPV
68.9
(4.7)
94.4
(17.0)
75.6
(4.9)
85.2
(4.2)
81.9
(5.6)
88.7
(4.4)
qsel
5.4
(1.0)
18.5
(1.2)
6.8
(0.8)
8.3
(0.6)
8.3
(1.1)
9.1
(0.8)
TPR
53.7
(9.9)
99.3
(2.6)
60.8
(9.6)
75.2
(8.0)
73.0
(8.8)
84.1
(7.0)
FPR
0.4
(1.9)
87.1
(10.0)
0.5
(2.1)
0.6
(2.4)
4.0
(5.8)
2.7
(5.1)
II
PPV
99.5
(2.8)
53.4
(2.9)
99.4
(2.8)
99.3
(2.8)
95.3
(6.7)
97.2
(5.4)
NPV
68.6
(4.6)
96.4
(14.2)
72.1
(4.9)
80.4
(5.3)
78.4
(5.6)
86.2
(5.5)
qsel
5.4
(1.0)
18.6
(1.1)
6.1
(1.0)
7.6
(0.8)
7.7
(1.1)
8.7
(0.8)
TPR
56.0
(10.2)
99.1
(2.8)
60.0
(10.0)
73.5
(8.3)
74.3
(9.2)
82.6
(7.9)
FPR
0.2
(1.5)
88.7
(11.1)
0.2
(1.5)
0.1
(1.0)
3.9
(5.8)
1.8
(4.1)
III
PPV
99.6
(2.5)
53.0
(3.3)
99.6
(2.4)
99.9
(1.2)
95.2
(7.1)
98.1
(4.3)
NPV
69.8
(5.0)
92.3
(23.2)
71.7
(5.1)
79.4
(5.2)
79.2
(6.3)
85.4
(5.9)
qsel
5.6
(1.0)
18.8
(1.2)
6.0
(1.0)
7.4
(0.8)
7.8
(0.9)
8.4
(1.0)
TPR
56.8
(16.3)
98.8
(4.8)
63.0
(17.4)
82.6
(11.2)
79.0
(15.1)
88.6
(10.7)
FPR
0.1
(0.7)
86.8
(8.6)
0.4
(1.6)
0.3
(1.3)
3.3
(4.6)
2.5
(4.2)
IV
PPV
99.8
(2.0)
27.6
(2.5)
98.5
(6.0)
99.3
(3.6)
90.3
(12.8)
93.3
(10.8)
NPV
87.6
(4.2)
95.9
(17.1)
89.2
(4.6)
94.6
(3.4)
93.4
(4.5)
96.3
(3.4)
qsel
2.9
(0.8)
18.0
(1.3)
3.2
(0.9)
4.2
(0.6)
4.5
(1.0)
4.8
(0.8)
TPR
-
-
-
-
-
-
-
-
-
-
-
-
FPR
0.1
(0.5)
86.8
(8.5)
0.1
(0.7)
0.1
(0.7)
1.9
(3.4)
1.1
(2.3)
V§
PPV
-
-
-
-
-
-
-
-
-
-
-
-
NPV
100.0
(0.0)
100.0
(0.0)
100.0
(0.0)
100.0
(0.0)
100.0
(0.0)
100.0
(0.0)
qsel
0.0
(0.1)
17.4
(1.7)
0.0
(0.1)
0.0
(0.1)
0.4
(0.7)
0.2
(0.5)
TPR
58.1
(10.7)
100.0
(0.0)
57.7
(10.8)
100.0
(0.0)
72.2
(9.6)
100.0
(0.0)
FPR
0.0
(0.0)
0.0
(0.0)
0.1
(1.2)
0.0
(0.0)
4.7
(6.3)
0.1
(1.1)
VI
PPV
100.0
(0.0)
100.0
(0.0)
99.8
(1.9)
100.0
(0.0)
94.4
(7.3)
99.9
(1.0)
NPV
70.9
(5.5)
100.0
(0.0)
70.6
(5.4)
100.0
(0.0)
77.8
(6.1)
100.0
(0.0)
qsel
5.8
(1.1)
10.0
(0.0)
5.8
(1.1)
10.0
(0.0)
7.7
(1.1)
10.0
(0.1)
∗TPR=TP/τ, FPR=FP/(20 −τ), PPV=TP/(TP+FP), NPV=(20 −τ −FP)/(20 −TP+FP), where TP is the number of outcomes
associated with the covariate and selected into the model, FP is the number of outcomes unrelated to the covariate and mistakenly
selected into the model, and τ is the number of outcomes that are truly associated with the covariate. Note, τ is 10 in Scenarios I-III
and VI, 5 in Scenario IV, and 0 in Scenario V.
†For variable selection in UZIP analyses, we used 95% conﬁdence intervals with a false discovery rate controlling procedure.
‡For variable selection in MZIP models, we applied a marginal posterior probability cutoﬀof 0.5 for both γ and δ. The hyperparameters
ωα=ωβ are set to either 0.1 or 0.5
§Since there is no outcomes that are truly associated with the covariate in Scenario V, TPR and PPV are not presented.
NOTE: Throughout the mean and standard deviation (SD) values are based on results from 100 simulated datasets.
tive to the strength of correlation among outcomes, whereas the MZIP TPR increased to
67% in Scenario I, in which there was a stronger correlation among outcomes associated
with the covariate. Both the UZIP and the MZIP methods successfully identiﬁed the co-
variate associations for the four outcomes with the largest eﬀect sizes (|αj,1| ≥0.20; Table
2). However, the MZIP model performed much better at detecting smaller-magnitude as-
sociations: when |αj,1| = 0.10 (outcomes 2 and 7), associations were correctly included in
13


## Page 14


Table 2: Estimated regression parameters and inclusion probabilities for the univariate zero-
inﬂated Poisson (UZIP)†,∗and the proposed multivariate zero-inﬂated Poisson (MZIP)‡ models
for Scenario I.
UZIP
MZIP†
Binary
Count
Binary
Count
True
αj,1
βj,1
αj,1|δj,1 = 1
δj,1
βj,1|γj,1 = 1
γj,1
j
αj,1, βj,1
Est (SE)
mα,j
Est (SE)
mβ,j
PM (SD)
PM
PM (SD)
PM
1
0.05
0.05 (0.04)
0.02
0.042 (0.002)
0.95
0.06 (0.04)
0.04
0.03 (0.02)
0.03
2
0.10
0.11 (0.04)
0.14
0.088 (0.002)
1.00
0.11 (0.04)
0.43
0.09 (0.02)
1.00
3
0.15
0.15 (0.05)
0.63
0.142 (0.002)
1.00
0.15 (0.04)
0.95
0.15 (0.02)
1.00
4
0.20
0.20 (0.05)
0.91
0.191 (0.002)
1.00
0.20 (0.04)
1.00
0.19 (0.02)
1.00
5
0.25
0.25 (0.05)
0.99
0.233 (0.002)
1.00
0.24 (0.04)
1.00
0.24 (0.02)
1.00
6
-0.05
-0.04 (0.04)
0.01
-0.046 (0.002)
0.97
-0.06 (0.04)
0.04
-0.06 (0.02)
0.23
7
-0.10
-0.11 (0.04)
0.25
-0.104 (0.002)
0.99
-0.11 (0.04)
0.36
-0.11 (0.02)
1.00
8
-0.15
-0.14 (0.05)
0.55
-0.143 (0.002)
1.00
-0.15 (0.04)
0.95
-0.15 (0.02)
1.00
9
-0.20
-0.20 (0.05)
0.95
-0.194 (0.002)
1.00
-0.20 (0.04)
1.00
-0.20 (0.02)
1.00
10
-0.25
-0.25 (0.05)
0.99
-0.251 (0.002)
1.00
-0.24 (0.04)
1.00
-0.25 (0.02)
1.00
11
0.00
-0.01 (0.04)
0.00
0.001 (0.002)
0.82
-0.01 (0.04)
0.01
0.00 (0.01)
0.00
12
0.00
0.02 (0.04)
0.00
0.001 (0.002)
0.84
0.02 (0.04)
0.02
0.00 (0.01)
0.00
13
0.00
-0.01 (0.04)
0.00
-0.004 (0.002)
0.89
-0.00 (0.04)
0.01
-0.00 (0.01)
0.00
14
0.00
-0.00 (0.04)
0.00
-0.002 (0.002)
0.82
-0.00 (0.04)
0.01
-0.00 (0.01)
0.00
15
0.00
0.00 (0.04)
0.00
-0.000 (0.002)
0.93
-0.00 (0.04)
0.01
-0.00 (0.01)
0.01
16
0.00
-0.00 (0.04)
0.00
-0.004 (0.002)
0.80
-0.00 (0.04)
0.01
-0.00 (0.01)
0.00
17
0.00
0.00 (0.04)
0.00
-0.005 (0.002)
0.85
0.00 (0.04)
0.01
-0.00 (0.01)
0.00
18
0.00
0.01 (0.04)
0.00
0.007 (0.002)
0.96
0.00 (0.04)
0.01
-0.00 (0.01)
0.00
19
0.00
0.00 (0.04)
0.01
-0.003 (0.002)
0.85
-0.00 (0.04)
0.01
0.00 (0.01)
0.00
20
0.00
-0.01 (0.04)
0.00
0.002 (0.002)
0.83
-0.00 (0.04)
0.01
-0.00 (0.01)
0.00
† The medians of the maximum likelihood estimate (Est) and standard error (SE) of αj,1 and βj,1, the proportion that
the covariate is selected for the jth outcome (mα,j, mβ,j) are calculated.
∗The empirical standard deviations of Est(βj,1) range between 0.036 and 0.054. (not presented in the table)
‡ The medians of the posterior means (PM) and posterior standard deviation (SD) of αj,1 and βj,1 (conditioning on
δj,1 = 1 and γj,1 = 1, respectively), the medians of the posterior means of δj,1 and γj,1 (marginal posterior probability
of inclusion) are computed. The hyperparameters ωα = ωβ are set to 0.1.
NOTE: Throughout values are based on results from 100 simulated datasets.
40% and 20% of MZIP and UZIP models, respectively; the corresponding inclusion rates
were 95% and 60% when |αj,1| = 0.15 (outcomes 3 and 8).
The multivariate approach yielded much more substantial improvement for the count
part of model when outcomes were correlated (Table 1). Even controlling the FDR, the
univariate approach generally exhibited inﬂated type I error, as high as 86% across Scenarios
I-V. In contrast, across all scenarios the MZIP model had a low probability of false discovery
(FPR< 1%) while also exhibiting high TPR that ranged from 73% to 83% in Scenarios I-IV.
The relatively poor performance of the UZIP method is not due to bias, since the estimated
association for outcomes unassociated with the covariate (βj,1, j=11,. . . ,20) were very close
to zero (Table 2). However, the medians of the asymptotic standard errors (SE) for ˆβj,1 were
14


## Page 15


20 times smaller than the empirical standard deviations of ˆβj,1 (rang between 0.036 and
0.054) (Table 2), was also observed in Scenario II-V (Supplementary Material D). Thus,
the univariate approach appears to perform poorly in estimation of the standard errors
for count model parameters when outcomes are correlated. Consequently, the estimated
conﬁdence intervals are too narrow.
In the null case (Scenario V), both approaches successfully excluded the covariate for
all outcomes for the binary part of the model even when outcomes were strongly correlated;
the UZIP model exhibited a high false discovery rate (87%) for the count part of the model.
We ran extensive additional simulations to explore other factors (detailed in Table E.1
and E.2 in Supplementary Material E), including a larger number of outcomes (q=50),
a lower signal density (4∼5%), a smaller sample size (n=150) and negative correlations.
Brieﬂy, the results were similar to those described above, with the MZIP performing much
better for variable selection and the UZIP exhibiting inﬂated type I error. We also com-
pared the proposed MZIP to a univariate non-parametric method, the Wilcoxon rank sum
test. Although type I error was well controlled in the univariate non-parametric method,
substantially higher power was achieved by the MZIP.
To summarize, compared with the univariate approach, the proposed multivariate
method improved upon the UZIP’s performance for the binary part of the model by main-
taining type I error while boosting the ability to identify true associations under the sim-
ulated settings. For the count part of the model, there were some scenarios in which the
power of UZIP was higher than with the MZIP approach. This higher power of UZIP was
at a cost of a highly inﬂated false discovery rate, whereas the MZIP FPR was < 1%. Per-
formance of the MZIP model was enhanced by increasing the prior inclusion probabilities,
ωβ,k = ωα,l = 0.5. The TPR then exceeded 80% in all non-null scenarios and FPR remained
< 4% across all scenarios.
15


## Page 16


4
Application to Pediatric HIV/AIDS Cohort Study
Data
The proposed MZIP method was originally motivated by research into whether caries-
associated bacteria diﬀer in PHIV and PHEU youth (Moscicki et al., 2016; Ryder et al.,
2017). The 254 subjects were age 10 to 22 years at the time of an oral health examination
done from September 2012 to January 2014. Subgingival dental plaque samples were col-
lected at two preselected sites and excluded if participants had antibiotic exposure in the
previous three months. DNA was isolated from plaque specimens and 16S rDNA sequenced
(Caporaso et al., 2011; Gomes et al., 2015). The sequencing reads were trimmed, ﬁltered,
and grouped using the DADA2 pipeline, and reads matched to the curated Human Oral Mi-
crobiome Database (99.9% of reads matched to the species or genus level) (Dewhirst et al.,
2010). Each subject had a count (number of sequencing reads) for each taxon identiﬁed in
the study.
4.1
Analysis Details and Prior Speciﬁcations
We focused our analysis on q = 44 taxa: 14 known caries-associated species (Aas et al.,
2008) and any additional species that were highly correlated with them in this dataset
(Figure 2 (a)). HIV infection status (xi1=zi1; 0, uninfected; 1, infected) was the covariate
of primary interest, with adjustment for participants’ age (xi2=zi2) without performing
variable selection on it (i.e., it was “forced” into the model). To account for sequencing
depth variation across samples, the total number of sequencing reads was included as an
oﬀset in the count model.
We ﬁt the proposed MZIP model and the UZIP model to PHACS data. For the Bayesian
MZIP approach, we set the hyperparameters, (µβ0, µα0, aβ0, bβ0, aα0, bα0, vβ,j, vα,j, aβ,k,
bβ,k, aα,l, bα,l, Ψ0, ρ0), to the same values as in Section 3. Since performance of the MZIP
was improved when the prior inclusion probabilities were increased from 0.1 to 0.5 in the
simulation studies, we set ωβ,k = ωα,l=0.5. We ran two independent MCMC chains for 2
million iterations, each with the ﬁrst half taken as burn-in. We assessed convergence of
the MCMC sampler by plotting traces of the MCMC scans for each parameter. A visual
16


## Page 17


assessment of convergence to the stationary distribution was carried out by overlaying plots
for the two MCMC chains.
We also calculated the posterior median with 95% credible intervals for the marginal
IDR for MZIP (described in Section 2.3). We age-adjusted the estimate by using the mean
value, 16 years.
4.2
Results
Table 3: Estimated regression parameters and inclusion probabilities for the ﬁve species identiﬁed
as associated with HIV infection by using a multivariate zero-inﬂated Poisson (MZIP)† and the
univariate zero-inﬂated Poisson (UZIP)‡ models.
Binary
Count
IDR∗
αj,1|δj,1 = 1
IP
βj,1|γj,1 = 1
IP
PM (95% CI)
PM (95% CI)
PM (95% CI)
Actinomyces graevenitzi
-0.39 (-0.67, -0.09)
0.54
0.25 (-0.22, 0.72)
0.11
0.96 (0.57, 1.08)
Fusobacterium periodonticum
0.16 (-0.60, 0.48)
0.07
-0.43 (-0.66, -0.14)
0.93
0.66 (0.53, 0.98)
MZIP
Lachnoanaerobaculum orale
0.10 (-0.17, 0.33)
0.03
-0.67 (-1.15, -0.25)
0.95
0.52 (0.24, 0.86)
Leptotrichia sp oral taxon 215
-0.44 (-0.75, -0.17)
0.63
-0.04 (-0.19, 0.20)
0.02
0.86 (0.74, 1.00)
Veillonella genus NOI§
-0.04 (-0.60, 0.45)
0.05
-0.37 (-0.60, -0.12)
0.88
0.71 (0.57, 1.00)
αj,l
βj,k
Est (95% CIF)
Est (95% CIF)
Actinomyces graevenitzi
-0.27 (-0.89, 0.35)
-0.46 (-0.69, -0.23)
Fusobacterium periodonticum
-0.08 (-0.93, 0.77)
-0.80 (-0.84, -0.75)
UZIP
Lachnoanaerobaculum orale
0.31 (-0.38, 0.99)
-2.58 (-2.79, -2.36)
Leptotrichia sp oral taxon 215
-0.41 (-1.04, 0.21)
-0.26 (-0.41, -0.11)
Veillonella genus NOI
0.20 (-1.02, 1.41)
-0.24 (-0.27, -0.21)
† In the MZIP model, the posterior median (PM) and 95% credible interval (CI) of regression parameters and incidence density ratio (IDR) are
computed.
‡ In the UZIP model, the maximum likelihood estimates (Est) and 95% conﬁdence intervals (CIF ) of regression parameters are computed.
∗Adjusted for individuals with age of 16 years.
§ not otherwise identiﬁed
With a marginal posterior probability cutoﬀof 0.5, the MZIP method identiﬁed three
species (Fusobacterium periodonticum, Lachnoanaerobaculum orale, and Veillonella genus
NOI) for which counts were associated with HIV infection among “susceptible” individu-
als, and it selected two species (Actinomyces graevenitzii and Leptotrichia sp oral taxon
215) for which the probability of participants being susceptible to these two species was
17


## Page 18


Inclusion probability
Actinomyces genus NOI
Actinomyces graevenitzii
Actinomyces lingnaeNVP
Actinomyces sp oral taxon 448
Alloprevotella sp oral taxon 473
Atopobium parvulum
Atopobium rimae
Bifidobacterium dentium
Campylobacter concisus
Cryptobacterium curtum
Fusobacterium periodonticum
Gemella genus NOI
Granulicatella elegans
Haemophilus genus NOI
Haemophilus parainfluenzae
Haemophilus sputorum
Kingella oralis
Lachnoanaerobaculum orale
Lactobacillus genus NOI
Lactobacillus salivarius
Leptotrichia hongkongensis
Leptotrichia sp oral taxon 215
Leptotrichia wadei
Megasphaera micronuciformis
Oribacterium parvum
Oribacterium sinus
Prevotella denticola
Prevotella histicola
Prevotella melaninogenica
Prevotella oris
Prevotella salivae
Scardovia wiggsiae
Selenomonas sp oral taxon 136
Shuttleworthia satelles
Stomatobaculum longum
Stomatobaculum sp oral taxon 097
Streptococcus mutans
Streptococcus sobrinus
Veillonella atypica
Veillonella genus NOI
Veillonella parvula
Veillonella rogosae
Veillonella sp oral taxon 780
VeillonellaceaeG1 sp oral taxon 150
0.0
0.5
1.0
Binary part
Count part
Figure 1: Analysis of Pediatric HIV/AIDS Cohort Study (PHACS) data: marginal posterior
inclusion probabilities for the HIV status covariate in relation to excess zeros and counts of 44
microbial species as estimated via the proposed multivariate zero-inﬂated Poisson (MZIP) model.
We adjust for participants age, a potential confounder, but do not perform variable selection on
it. “NOI” stands for “not otherwise identiﬁed”.
18


## Page 19


Figure 2: Observed and estimated correlations among counts of 44 microbial species in the Pedi-
atrics HIV/AIDS Cohort Study (PHACS): (a) Empirical correlations calculated by cor(log(y+1));
(b) Posterior median of R; (c) Posterior median of RV , calculated based on posterior samples of
ΣV from the proposed multivariate zero-inﬂated Poisson (MZIP) model ﬁt.
19


## Page 20


associated with HIV infection (Figure 1). In contrast, the frequentist UZIP analysis with
95% conﬁdence intervals identiﬁed 39 species whose levels were associated with HIV infec-
tion in the susceptible population, including the three associations identiﬁed by MZIP. The
UZIP analysis identiﬁed no species for which the probability of being “susceptible” to that
species was associated with HIV infection. Based on the methods’ relative performance
in the simulation study, it is plausible that the UZIP’s lack of accounting for outcomes’
correlation patterns, which are complex (Figure 2 (a)), grossly inﬂated the type I error rate
in the count model and may also have decreased sensitivity of the zero model.
Indeed, comparing the estimated associations between HIV infection and the ﬁve taxa
selected based on the MZIP model (Table 3), the uncertainty associated with the count
part of UZIP model was much smaller than that generated by the MZIP method.
As
with the simulation, this may have accounted for the detection of 39 associations, many
of which are presumably false positive associations.
Because of how we calculated the
IDR estimate, it has an age-speciﬁc interpretation. For example, 16 year-old youth, PHIV
youth had 34% (95% credible interval 2%, 47%) and 48% (95% credible interval 14%, 76%)
lower abundance of Fusobacterium periodonticum and Lachnoanaerobaculum orale species,
respectively, compared with PHEU youth.
The proposed MZIP model captures within-subject dependence among multiple out-
comes via two correlation components, R and ΣV . The dependence patterns arising from
the empirical correlations appear to reﬂect, strongly, the correlation structure predicted by
the binary component of the proposed MZIP (Figure 2). This implies that in these data,
the presence of taxa is more structured than their counts. This result is not attributable
to smoothing of the empirical correlation from having added 1 to every count, because
the results were not sensitive to changes of this value to 0.5, 0.1, and 0.01. The model
also provides an opportunity to quantify and compare the contribution of zero inﬂation
versus other sources of overdispersion to microbiome taxon abundance (see Supplementary
Material F for posterior estimates of ΣV j,j and α0,j).
20


## Page 21


5
Discussion
We have described the development of a new Bayesian variable selection method that ad-
dresses challenges arising in the analysis of microbiome sequencing data: excess zero counts
and high-dimensional outcomes with a complex association structure. Applying the pro-
posed multivariate approach led to the identiﬁcation of two species for which the probability
of being susceptible to those species was associated with HIV infection; these associations
did not meet FDR thresholds when the existing univariate approach was applied. In addi-
tion, based on the estimated induced marginalized IDR under the proposed model, another
two species were less abundant in HIV-infected youth aged 16 years compared with PHEU
youth of the same age.
One might question how realistic are these analyses when they are adjusted for only
one confounder, age. Some reassurance might be provided from the observation that in
univariate analyses that included additional confounders (e.g., sex, race, and dental visit in
previous year as a marker of oral hygiene), inference was not greatly altered compared with
models including only HIV status and age. We are continuing to study performance in a
range of datasets, including more complete confounder adjustment. We are also working to
scale up the proposed method in the number of endpoints, as discussed further below, and
also in the number of covariates, both of which are required for integrated omics analyses.
The simulation study demonstrated superior performance of the proposed MZIP ap-
proach over the existing UZIP method when outcomes were correlated. The sample size
was small enough that asymptotic assumptions under the frequentist-based UZIP model
did not hold. This aﬀected estimation of the asymptotic variance of the regression parame-
ters for the count model, which was not a limitation for the proposed multivariate Bayesian
approach. This diﬀerence in performance is primarily because i) for small data settings,
estimation is generally more stable with Bayesian approaches, which exploit information
from both the observed data likelihood and prior distribution; and ii) the MZIP method
uses information not only on the mean model but also from the structure of covariance
among outcomes.
We used a multivariate probit model for the binary part of the MZIP mixture model.
An alternative is to assume a multivariate logistic distribution for wi (O’Brien and Dunson,
21


## Page 22


2004), for which posterior computation can be facilitated based on a data augmentation
algorithm (Albert and Chib, 1993).
However, initial numerical studies using the latter
approach resulted in prohibitively slow mixing of the MCMC algorithms due to sparseness
of data, even for data with q=10 and assuming an unstructured covariance pattern. This
is because the multivariate logistic model speciﬁcation requires the estimation of n more
latent parameters than does the multivariate probit model. Thus, the multivariate probit
model in the MZIP proved to be much more computationally tractable.
We have presented the model in its most general form that allows the importance of
each covariate, as well as the correlation structure among the multivariate outcomes, to
vary across the binary and the count components of the model. This gives the user maximal
ﬂexibility and provides evidence on how a covariate is associated with each response, i.e.
with more zeros or higher counts. The question arises whether the complexity of the model
is necessary or whether simpler models should suﬃce. Analysis of the motivating data
suggests that diﬀerent correlation structures were needed in this case. It is diﬃcult to
provide a general answer to this question until we have had more opportunity to apply it a
range of datasets and compare results with those obtained in simpler models. One would
not be able to make this comparison if the most general model is not available as a basis
for comparison. Yet, simpler models might well be useful in other datasets.
Thus, the software implementation of the proposed approach oﬀers more parsimonious
versions of the model, simpliﬁed by imposing additional restrictions regarding the model
parameters. For example, the two model parts can be forced to have one common variable
selection indicator by setting γj,k = δj,l. In practice, such a restriction might facilitate im-
plementation by providing a single vector of variable selection indicators, i.e. one list as to
which species are associated with each covariate. A diﬀerent assumption is that both model
parts share the same covariance pattern (R = RV ), which will greatly reduce the number
of parameters to be estimated and thus the computational complexity in the MCMC algo-
rithm, especially for data with large q. In our initial analysis, ﬁtting this restricted model
to the PHACS data yielded unreliable estimates of R, because the assumption that R = RV
is violated in these data (Figure 2). Again, the restricted model may serve well in other
datasets. Therefore, we made available the algorithms to implement both types of simpler
22


## Page 23


MZIP models as options in the mBvs package.
There are several ways the proposed framework could be extended. First, marginal-
ized zero-inﬂated models have recently been developed so that inference can be made on
the marginal mean of the sampled population via a set of uniﬁed regression coeﬃcients
(Long et al., 2015; Tabb et al., 2016). The uniﬁed regression coeﬃcients have better in-
terpretability, as the marginalized models do not require the additional steps described in
Section 2.3 to address the dependence of parameter values on xi,(−k). In some applications,
it may be more appropriate to interpret the two sets of regression coeﬃcients separately,
yet there also may be other applications for which interpretability of regression parameters
would be enhanced by adopting a marginalized model within the proposed multivariate
Bayesian variable selection method. Marginalization may also provide more stable model
ﬁtting. Second, although we focused data analysis on a preselected subset of species in the
application, often microbiologists’ goal is to perform whole-community oral microbiome
analysis, which generally involves several hundred taxa. We are currently working to ad-
dress the computational issues arising from an even higher-dimensional parameter space.
Because the complexity mainly results from the ﬂexible unstructured covariance model, we
propose to scale up the proposed MZIP method by adopting alternative correlation struc-
tures that can ﬂexibly accommodate potentially complicated patterns among hundreds of
taxa. A ﬁnal possibility is to study the interaction between the marginal posterior proba-
bility cutoﬀand the prior inclusion probability in controlling the FDR at the desired level
under the proposed model.
In conclusion, the proposed framework gives researchers valid and powerful statistical
tools to overcome major methodological barriers in microbiome sequencing data analysis.
Beyond the study of the human microbiome, the methods, software, and guidance from
simulation studies in this work will be useful in any ﬁeld requiring analysis of multivariate
zero-inﬂated count data.
SUPPLEMENTARY MATERIALS
R-package ‘mBvs’: R-package mBvs contains codes to implement proposed Bayesian frame-
work described in the article. The package is currently available in CRAN (https://cran.r-
project.org/web/packages/mBvs).
23


## Page 24


References
Aas, J., Griﬀen, A., Dardis, S., Lee, A., Olsen, I., Dewhirst, F., Leys, E., and Paster, B.
(2008). Bacteria of dental caries in primary and permanent teeth in children and young
adults. Journal of Clinical Microbiology, 46(4):1407–1417.
Aitchison, J. and Ho, C. (1989).
The multivariate Poisson-log normal distribution.
Biometrika, 76(4):643–653.
Albert, J. and Chib, S. (1993). Bayesian analysis of binary and polychotomous response
data. Journal of the American statistical Association, 88(422):669–679.
Albert, J., Wang, W., and Nelson, S. (2014). Estimating overall exposure eﬀects for zero-
inﬂated regression models with application to dental caries. Statistical Methods in Medical
Research, 23(3):257–278.
Alperen, J., Brummel, S., Tassiopoulos, K., Mellins, C., Kacanek, D., Smith, R., Seage,
G., and Moscicki, A. (2014). Prevalence of and risk factors for substance use among peri-
natally human immunodeﬁciency virus–infected and perinatally exposed but uninfected
youth. Journal of Adolescent Health, 54(3):341–349.
Anderson, M. J. (2001). A new method for non-parametric multivariate analysis of variance.
Austral Ecology, 26(1):32–46.
Arab, A., Holan, S., Wikle, C., and Wildhaber, M. (2012). Semiparametric bivariate zero-
inﬂated Poisson models with application to studies of abundance for multiple species.
Environmetrics, 23(2):183–196.
Ashford, J. and Sowden, R. (1970). Multi-variate probit analysis. Biometrics, 26:535–546.
Benjamini, Y. and Hochberg, Y. (1995). Controlling the false discovery rate: a practical and
powerful approach to multiple testing. Journal of the Royal Statistical Society: Series B
B, 57(1):289–300.
Box, G. and Tiao, G. (2011). Bayesian Inference in Statistical Analysis. John Wiley &
Sons.
24


## Page 25


Breiman, L. and Friedman, J. (1997). Predicting multivariate responses in multiple linear
regression. Journal of the Royal Statistical Society: Series B, 59(1):3–54.
Brown, P., Vannucci, M., and Fearn, T. (1998). Multivariate Bayesian variable selection
and prediction. Journal of the Royal Statistical Society: Series B, 60(3):627–641.
Caporaso, J., Lauber, C., Walters, W., Berg-Lyons, D., Lozupone, C., Turnbaugh, P.,
Fierer, N., and Knight, R. (2011). Global patterns of 16S rRNA diversity at a depth of
millions of sequences per sample. PNAS, 108:4516–4522.
Chen, J. and Li, H. (2013). Variable selection for sparse Dirichlet-multinomial regression
with an application to microbiome data analysis.
The Annals of Applied Statistics,
7(1):418–442.
Chib, S. and Greenberg, E. (1998). Analysis of multivariate probit models. Biometrika,
85(2):347–361.
Dewhirst, F. E., Chen, T., Izard, J., Paster, B. J., Tanner, A., Yu, W.-H., Lakshmanan,
A., and Wade, W. G. (2010). The human oral microbiome. Journal of bacteriology,
192(19):5002–5017.
Earnest, A., Morgan, G., Mengersen, K., Ryan, L., Summerhayes, R., and Beard, J. (2007).
Evaluating the eﬀect of neighbourhood weight matrices on smoothing properties of con-
ditional autoregressive (car) models. International journal of health geographics, 6(1):54.
Fernandes, M. V., Schmidt, A. M., and Migon, H. S. (2009). Modelling zero-inﬂated spatio-
temporal processes. Statistical Modelling, 9(1):3–25.
Fox, J. (2013). Multivariate zero-inﬂated modeling with latent predictors: Modeling feed-
back behavior. Computational Statistics & Data Analysis, 68:361–374.
George, E. and McCulloch, R. (1997). Approaches for Bayesian variable selection. Statistica
Sinica, 7:339–374.
George, E. I. and McCulloch, R. E. (1993). Variable selection via Gibbs sampling. Journal
of the American Statistical Association, 88(423):881–889.
25


## Page 26


Gomes, B., Berber, V., Kokaras, A., Chen, T., and Paster, B. (2015). Microbiomes of
endodontic-periodontal lesions before and after chemomechanical preparation. Journal
of endodontics, 41(12):1975–1984.
Hall, D. B. (2000). Zero-inﬂated poisson and binomial regression with random eﬀects: a
case study. Biometrics, 56(4):1030–1039.
Holmes, I., Harris, K., and Quince, C. (2012). Dirichlet multinomial mixtures: generative
models for microbial metagenomics. PLoS ONE, 7(2):e30126.
La Rosa, P. S., Brooks, J. P., Deych, E., Boone, E. L., Edwards, D. J., Wang, Q., Sodergren,
E., Weinstock, G., and Shannon, W. D. (2012). Hypothesis testing and power calculations
for taxonomic-based human microbiome data. PloS one, 7(12):e52078.
Lambert, D. (1992). Zero-inﬂated Poisson regression, with an application to defects in
manufacturing. Technometrics, 34(1):1–14.
Lee, A. H., Wang, K., Scott, J. A., Yau, K. K. W., and McLachlan, G. J. (2006). Multi-
level zero-inﬂated Poisson regression modelling of correlated count data with excess zeros.
Statistical Methods in Medical Research, 15(1):47–61.
Lee, K. H., Tadesse, M. G., Baccarelli, A. A., Schwartz, J., and Coull, B. A. (2017). Mul-
tivariate Bayesian variable selection exploiting dependence structure among outcomes:
Application to air pollution eﬀects on DNA methylation. Biometrics, 73(1):232–241.
Li, C., Lu, J., Park, J., Kim, K., Brinkley, P. A., and Peterson, J. P. (1999). Multivariate
zero-inﬂated Poisson models and their applications. Technometrics, 41(1):29–38.
Li, H. (2015). Microbiome, metagenomics, and high-dimensional compositional data anal-
ysis. Annual Review of Statistics and Its Application, 2:73–94.
Liu, C. (2001). Bayesian analysis of multivariate probit models - discussion on the art of
data augmentation. Journal of Computational and Graphical Statistics, 10(1):75–81.
Liu, C. and Sun, D. X. (2000). Analysis of interval-censored data from fractionated exper-
iments using covariance adjustment. Technometrics, 42(4):353–365.
26


## Page 27


Loeys, T., Moerkerke, B., De Smet, O., and Buysse, A. (2012). The analysis of zero-inﬂated
count data: Beyond zero-inﬂated Poisson regression. British Journal of Mathematical
and Statistical Psychology, 65(1):163–180.
Long, D. L., Preisser, J. S., Herring, A. H., and Golin, C. E. (2015). A marginalized zero-
inﬂated Poisson regression model with random eﬀects. Journal of the Royal Statistical
Society: Series C, 64(5):815–830.
Mantel, N. (1967). The detection of disease clustering and a generalized regression ap-
proach. Cancer research, 27(2 Part 1):209–220.
Mantel, N. and Valand, R. S. (1970). A technique of nonparametric multivariate analysis.
Biometrics, 26(3):547–558.
Moscicki, A.-B., Yao, T.-J., Ryder, M. I., Russell, J. S., Dominy, S. S., Patel, K., McKenna,
M., Van Dyke, R. B., Seage III, G. R., Hazra, R., and Shiboski, C. H. (2016). The burden
of oral disease among perinatally hiv-infected and hiv-exposed uninfected youth. PloS
one, 11(6):e0156459.
Mueller, N. T., Bakacs, E., Combellick, J., Grigoryan, Z., and Dominguez-Bello, M. G.
(2015).
The infant microbiome development:
mom matters.
Trends in molecular
medicine, 21(2):109–117.
Neelon, B. and Chung, D. (2017). The LZIP: A Bayesian latent factor model for correlated
zero-inﬂated counts. Biometrics, 73(1):185–196.
O’Brien, S. M. and Dunson, D. B. (2004). Bayesian multivariate logistic regression. Bio-
metrics, 60(3):739–746.
Perez-Mu˜noz, M. E., Arrieta, M.-C., Ramer-Tait, A. E., and Walter, J. (2017). A critical
assessment of the “sterile womb” and “in utero colonization” hypotheses: implications
for research on the pioneer infant microbiome. Microbiome, 5(1):48.
Pﬂughoeft, K. J. and Versalovic, J. (2012). Human microbiome in health and disease.
Annual Review of Pathology: Mechanisms of Disease, 7:99–122.
27


## Page 28


Preisser, J. S., Stamm, J. W., Long, D. L., and Kincade, M. E. (2012).
Review and
recommendations for zero-inﬂated count regression modeling of dental caries indices in
epidemiological studies. Caries research, 46(4):413–423.
Ryder, M. I., Yao, T.-J., Russell, J. S., Moscicki, A.-B., and Shiboski, C. H. (2017). Preva-
lence of periodontal diseases in a multicenter cohort of perinatally HIV-infected and
HIV-exposed and uninfected youth. Journal of clinical periodontology, 44(1):2–12.
Starr, J., Huang, Y., Lee, K., Murphy, C., Moscicki, A., Shiboski, C., Ryder, M., Yao, T.,
Faller, L., Van Dyke, R., and Paster, B. (2018). Oral microbiota in youth with perinatally
acquired HIV infection. Microbiome, page in press.
Tabb, L. P., Tchetgen, E. J., Wellenius, G. A., and Coull, B. A. (2016). Marginalized
zero-altered models for longitudinal count data. Statistics in biosciences, 8(2):181–203.
Tanner, M. A. and Wong, W. H. (1987). The calculation of posterior distributions by data
augmentation. Journal of the American Statistical Association, 82(398):528–540.
Tassiopoulos, K., Patel, K., Alperen, J., Kacanek, D., Ellis, A., Berman, C., Allison, S. M.,
Hazra, R., Barr, E., Cantos, K., et al. (2016). Following young people with perinatal
HIV infection from adolescence into adulthood: the protocol for PHACS AMP Up, a
prospective cohort study. BMJ open, 6(6):e011396.
Wadsworth, W. D., Argiento, R., Guindani, M., Galloway-Pena, J., Shelburne, S. A., and
Vannucci, M. (2017). An integrative Bayesian Dirichlet-multinomial regression model
for the analysis of taxonomic abundances in microbiome data.
BMC bioinformatics,
18(1):94.
Wang, X., Chen, M., Kuo, R. C., and Dey, D. K. (2015a).
Bayesian spatial-temporal
modeling of ecological zero-inﬂated count data. Statistica Sinica, 25(1):189–204.
Wang, Z., Ma, S., and Wang, C. (2015b). Variable selection for zero-inﬂated and overdis-
persed data with application to health care demand in Germany. Biometrical Journal,
57(5):867–884.
28


## Page 29


Xu, L., Paterson, A. D., Turpin, W., and Xu, W. (2015). Assessment and selection of
competing models for zero-inﬂated microbiome data. PloS one, 10(7):e0129606.
Zeileis, A., Kleiber, C., and Jackman, S. (2008). Regression models for count data in R.
Journal of statistical software, 27(8):1–25.
29

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
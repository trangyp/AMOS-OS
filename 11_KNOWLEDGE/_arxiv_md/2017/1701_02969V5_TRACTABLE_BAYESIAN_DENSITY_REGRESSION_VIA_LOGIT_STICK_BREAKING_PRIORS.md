---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1701.02969v5
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1701.02969v5_Tractable_Bayesian_Density_Regression_via_Logit_Stick-Breaking_Priors

> Source: 1701.02969v5_Tractable_Bayesian_Density_Regression_via_Logit_Stick-Breaking_Priors.pdf

> Pages: 18

---


## Page 1


Tractable Bayesian density regression via logit stick-breaking priors
Tommaso Rigona,∗, Daniele Duranteb
aDepartment of Statistical Science, Duke University, Durham, NC, USA
bDepartment of Decision Sciences and Bocconi Institute for Data Science and Analytics, Bocconi University, Via Roentgen 1, 20136 Milano, Italy
Abstract
There is a growing interest in learning how the distribution of a response variable changes with a set of predictors.
Bayesian nonparametric dependent mixture models provide a ﬂexible approach to address this goal. However, sev-
eral formulations require computationally demanding algorithms for posterior inference. Motivated by this issue, we
study a class of predictor-dependent inﬁnite mixture models, which relies on a simple representation of the stick-
breaking prior via sequential logistic regressions. This formulation maintains the same desirable properties of popular
predictor-dependent stick-breaking priors, and leverages a recent P´olya-gamma data augmentation to facilitate the im-
plementation of several computational methods for posterior inference. These routines include Markov chain Monte
Carlo via Gibbs sampling, expectation-maximization algorithms, and mean-ﬁeld variational Bayes for scalable infer-
ence, thereby stimulating a wider implementation of Bayesian density regression by practitioners. The algorithms
associated with these methods are presented in detail and tested in a toxicology study.
Keywords: Continuation-ratio logistic regression, Density regression, Gibbs sampling, Expectation-maximization,
Variational Bayes
1. Introduction
There is a growing interest in density regression models which allow the entire distribution of a univariate re-
sponse variable y ∈Y to be unknown and changing with a vector of predictors x ∈X. Indeed, the increased ﬂexi-
bility provided by these procedures allows improvements in inference and prediction compared to classical regression
frameworks, as seen in applications (e.g. Dunson and Park, 2008; Grifﬁn and Steel, 2011; Wade et al., 2014).
Within the Bayesian nonparametric framework, there is a wide variety of alternative methods to provide ﬂexible
inference for conditional distributions. Most of these strategies represent generalizations of the marginal density es-
timation problem for f(y), which is commonly addressed via Bayesian nonparametric mixture models of the form
f(y) =
R
K(y; θ)p(dθ), where K(y; θ) is a known parametric kernel indexed by θ ∈Θ, and p is a random probabil-
ity measure which is assigned a ﬂexible prior Π. Popular choices for Π are the Dirichlet process (Ferguson, 1973), the
∗Corresponding author
Email addresses: tommaso.rigon@duke.edu (Tommaso Rigon), daniele.durante@unibocconi.it (Daniele Durante)
Preprint submitted to Elsevier
May 6, 2020
arXiv:1701.02969v5  [stat.CO]  4 May 2020


## Page 2


two-parameter Poisson-Dirichlet process (Pitman and Yor, 1997), and other random measures having a stick-breaking
representation (Ishwaran and James, 2001). This choice leads to the inﬁnite mixture model
f(y) =
Z
K(y; θ)p(dθ) =
∞
X
h=1
πhK(y; θh),
(1)
where πh = νh
Qh−1
l=1 (1 −νl) for every h ≥1, with π1 = ν1. In equation (1), the kernel parameters (θh)h≥1 are
distributed according to a diffuse base measure P0, whereas the stick-breaking weights (νh)h≥1 have independent
Beta(ah, bh) priors, so that P∞
h=1 πh = 1 almost surely.
Model (1) has key computational beneﬁts in allowing the implementation of simple Markov chain Monte Carlo
methods for posterior inference (e.g. Escobar and West, 1995; Neal, 2000), and provides a consistent strategy for den-
sity estimation (e.g. Ghosal et al., 1999; Tokdar, 2006; Ghosal and Van Der Vaart, 2007). This has motivated different
generalizations of (1) to incorporate the conditional density inference problem for f(y | x) = fx(y), by allowing the
random mixing measure px to change with x ∈X, under a dependent stick-breaking characterization (MacEachern,
1999, 2000). Popular representations consider predictor-independent mixing weights πh, and incorporate changes
with x ∈X in the atoms θh(x); see for instance De Iorio et al. (2004); Gelfand et al. (2005); De la Cruz-Mes´ıa
et al. (2007). As noted in MacEachern (2000) and Grifﬁn and Steel (2006), the predictor-independent assumption for
the mixing weights might have limited ﬂexibility in practice. This has motivated more general formulations allowing
also πh(x) to change with the predictors. Relevant examples include the order-based dependent Dirichlet process
(Grifﬁn and Steel, 2006), the kernel stick-breaking process (Dunson and Park, 2008), the inﬁnite mixture model with
predictor-dependent weights (Antoniano-Villalobos et al., 2014), and more recent representations for Bayesian dy-
namic inference (Guti´errez et al., 2016). These formulations provide a broader class of priors for Bayesian density
regression, but their ﬂexibility comes at a computational cost. In particular, the availability of simple algorithms for
tractable posterior inference is limited by the speciﬁc construction of these representations.
The above issues motivate alternative formulations which preserve theoretical properties, but facilitate tractable
posterior computation under a broader variety of algorithms. We aim to address this goal via a logit stick-breaking
prior (LSBP), which relates each stick-breaking weight νh(x) ∈(0, 1) to a function ηh(x) ∈ℜof the covariates, using
the logit link. The proposed formulation is closely related to the probit stick-breaking prior (PSBP) of Rodriguez and
Dunson (2011). Indeed, as we will discuss in Section 2, both LSBP and PSBP are characterized by a continuation-ratio
representation (Tutz, 1991), which allows to express the underlying clustering assignment in terms of independent and
sequential binary regressions. This representation has key computational beneﬁts and has been exploited by Rodriguez
and Dunson (2011) to derive a Markov chain Monte Carlo (MCMC) algorithm for posterior inference. However, while
the MCMC for PSBP relies on the truncated Gaussian data augmentation for probit regression (Albert and Chib, 1993),
the one for LSBP exploits the recent P´olya-gamma data augmentation for logistic regression (Polson et al., 2013),
which might improve mixing compared to the PSBP, especially in imbalanced situations (Johndrow et al., 2019). As
2


## Page 3


we will clarify in Section 2, these imbalanced settings can also occur in our case, since the binary regressions are
associated to latent clustering allocations. We illustrate the MCMC algorithm for the LSBP in Section 3.
Besides developing tractable Gibbs sampling methods, we further derive alternative computational routines which
address the scalability and mixing issues of MCMC in high-dimensional studies. Speciﬁcally, in Section 3 we illustrate
a tractable expectation-maximization (EM) routine for point estimation, and a simple variational Bayes (VB) algorithm
for scalable inference. Both strategies leverage again the sequential representation of the LSBP and the associated
P´olya-gamma data augmentation. Note that a VB routine for LSBP is also presented in Ren et al. (2011), but it is
based on the bound of Jaakkola and Jordan (2000). As a consequence of the recent theoretical ﬁndings in Durante and
Rigon (2019), it can be shown that our approach is intimately related to the one of Ren et al. (2011), although being
developed by means of seemingly unrelated strategies. Finally, while tractable algorithms such as EM or VB could be
possibly obtained also for PSBP, we are not aware of any actual discussion or implementation. Indeed, the analytical
derivations might be slightly more complex in the PSBP case compared to the LSBP, as discussed in Section 3.
We shall emphasize that the overarching focus of our contribution is not on developing a novel methodological
framework for Bayesian density regression, but on deriving a broad set of routine-use computational strategies under
a suitable and tractable representation. To our knowledge this goal remains partially unaddressed, but represents a
fundamental condition to facilitate routine implementation of Bayesian density regression by practitioners. The three
proposed algorithms are empirically compared in Section 4 using a real data toxicology study, previously considered
in Dunson and Park (2008). Section 5 provides concluding remarks.
2. Logit stick-breaking prior
This section presents a formal construction of the LSBP via continuation-ratio logistic regressions. As a natural
extension of model (1), we consider the general class of predictor-dependent inﬁnite mixture models
fx(y) =
Z
Kx(y; θ)px(dθ) =
∞
X
h=1
πh(x)Kx(y; θh),
(2)
where πh(x) = νh(x) Qh−1
l=1 {1 −νl(x)} are predictor-dependent mixing probabilities having a stick-breaking repre-
sentation, whereas Kx(y; θ) denotes a predictor-dependent kernel, indexed by parameters θ and covariates x.
To highlight the continuation-ratio representation of the LSBP, let us ﬁrst consider an equivalent formulation of the
predictor-dependent mixture model in (2). In particular, following standard hierarchical representations of mixture
models, independent samples y1, . . . , yn of the variable with density function displayed in (2), can be obtained from
(yi | Gi = h, xi) ∼Kxi(yi; θh),
with pr(Gi = h | xi) = πh(xi) = νh(xi)
h−1
Y
l=1
{1 −νl(xi)},
(3)
3


## Page 4


ASSIGNMENT
pr(Gi > 1 | xi) = 1 −ν1(xi)
Gi > 1
pr(Gi = 1 | xi) = ν1(xi)
Gi = 1
pr(Gi > 2 | Gi > 1, xi) = 1 −ν2(xi)
Gi > 2
pr(Gi = 2 | Gi > 1, xi) = ν2(xi)
Gi = 2
pr(Gi > 3 | Gi > 2, xi) = 1 −ν3(xi)
Gi > 3
pr(Gi = 3 | Gi > 2, xi) = ν3(xi)
Gi = 3
. . .
. . .
. . .
. . .
Figure 1: Representation of the sequential mechanism to sample Gi.
for each unit i = 1, . . . , n, where θh ∼P0 independently for h ∈N, whereas Gi ∈N is the categorical variable
denoting the mixture component associated with the ith unit. According to (3), every Gi has probability mass function
f(Gi | xi) = Q∞
h=1 πh(xi)1(Gi=h), where 1(·) denotes the indicator function. Hence, re-writing {νh(xi)}h∈N as a
function of the mixing probabilities {πh(xi)}h∈N via
νh(xi) =
πh(xi)
1 −Ph−1
l=1 πl(xi)
=
pr(Gi = h | xi)
pr(Gi > h −1 | xi),
h ∈N,
(4)
allows to interpret each νh(xi) as the probability of being allocated to component h, conditionally on the event of
surviving to the previous 1, . . . , h −1 components, namely νh(xi) = pr(Gi = h | Gi > h −1, xi). This result
provides a formal characterization of the stick-breaking construction in (3) as the continuation-ratio parameterization
(Tutz, 1991) of the probability mass function for each component membership variable Gi. This connection with the
literature on sequential inference for categorical data is common to all the stick-breaking priors—as mentioned also
by Rodriguez and Dunson (2011) in the probit case.
As we will describe in Section 3, the above result facilitates the implementation of different routine-use algorithms
in Bayesian inference, and provides a simple generative process for each Gi. In particular, as illustrated in Figure 1,
in the ﬁrst step of this continuation-ratio generative mechanism, unit i is either assigned to the ﬁrst component with
probability ν1(xi) or to one of the others with complement probability. If Gi = 1 the process stops, otherwise
it continues considering the reduced set {h : h > 1}. A generic step h is reached if i has not been assigned to
1, . . . , h −1, and the decision at this step will be to either allocate i to component h with probability νh(xi), or to one
of the subsequent components with probability 1 −νh(xi), conditioned on Gi > h −1. Based on this representation,
4


## Page 5


the assignment indicator ζih = 1(Gi = h) can be expressed, for every unit i = 1, . . . , n, as
ζih = zih
h−1
Y
l=1
(1 −zil),
h ∈N,
(5)
where the generic zih, h ∈N, is a Bernoulli variable (zih | xi) ∼Bern{νh(xi)} denoting the decision at the hth
step to either allocate i to component h or to one of the subsequents. Hence, according to (5), the sampling of each
Gi, under the predictor-dependent stick-breaking representation for each πh(xi) in (3), can be reformulated as a set
of sequential Bernoulli choices with natural parameters ηh(xi) = logit{νh(xi)} = log[νh(xi)/{1 −νh(xi)}] under
an exponential family representation. Hence, we can write
πh(xi) =
exp{ηh(xi)}
1 + exp{ηh(xi)}
h−1
Y
l=1

1
1 + exp{ηl(xi)}

,
h ∈N,
(6)
allowing each ηh(xi) to be explicitly interpreted as the log-odds of the probability of being allocated to component h,
conditionally on the event of surviving to the ﬁrst 1, . . . , h −1 components. This result might be helpful in driving
prior speciﬁcation for the stick-breaking weights, while allowing recent computational advances in Bayesian logistic
regression (Polson et al., 2013) to be inherited in our density regression problem.
To conclude our Bayesian representation, we require priors for the log-odds ηh(xi), h ∈N in the continuation-
ratio logistic regressions. A natural choice, which is consistent with classical generalized linear models (e.g. Nelder
and Wedderburn, 1972), is to deﬁne ηh(xi) as a linear combination of selected functions of the covariates ψ(xi) =
{ψ1(xi), . . . , ψR(xi)}⊺and consider Gaussian priors for the coefﬁcients, thus obtaining
ηh(xi) = ψ(xi)⊺αh,
with αh ∼NR(µα, Σα),
h ∈N.
(7)
Although the linearity assumption in (7) may seem restrictive, note that ﬂexible formulations for ηh(xi), including
regression via splines and Gaussian processes, induce linear relations in the coefﬁcients. Moreover, as we will out-
line in Section 3, the linearity assumption simpliﬁes computations, while inducing a logistic-normal prior for each
νh(xi). Although such a prior can closely approximate Dirichlet distributions (Aitchison and Shen, 1980), the logit
stick-breaking does not induce beta distributed stick-breaking weights, and therefore it cannot be included in the class
discussed by Ishwaran and James (2001). However, one can easily adapt the theoretical results in Rodriguez and Dun-
son (2011) to our logit link. For example, the inﬁnite summation of the mixing weights is such that P∞
h=1 πh(xi) = 1
almost surely for any x ∈X; see the Appendix for details. Moreover, the LSBP is highly similar in its probabilistic
nature and properties to other popular predictor-dependent stick-breaking constructions. In particular, PSBP can be
approximated by LSBP, and viceversa, up to a simple transformation of the prior for each αh. This is a natural conse-
quence of the well known relationship between the probit and the logit function (Amemiya, 1981), since the mapping
{1 + exp(−ψ(x)⊺αh)}−1 can be roughly approximated by Φ{ψ(x)⊺αh
p
π/8}. This is summarized in Remark 1.
5


## Page 6


Remark 1. The logit stick-breaking prior in (6)–(7), can be approximated by a probit stick-breaking process νh(x) ≈
Φ{ψ(x)⊺¯αh}, with ¯αh = αh
p
π/8 ∼NR{
p
π/8µα, (π/8)Σα}, for every x ∈X and h ∈N.
Hence, a researcher considering a PSBP could perform approximate inference leveraging our algorithms, after a suit-
able rescaling of the prior for each αh. Moreover, this link suggests that the O(log n) growth of the number of clusters
found in empirical studies on the PSBP, should hold also for LSBP.
3. Bayesian computational methods
Although the LSBP and the associated computational procedures apply to a wider set of dependent mixture models
and kernels, we focus, for the sake of clarity, on the general class of predictor-dependent inﬁnite mixtures of Gaussians
fx(y) =
Z √τφ[√τ {y −λ(x)⊺β}]px(dβ, dτ) =
∞
X
h=1
πh(x)√τhφ[√τh {y −λ(x)⊺βh}],
(8)
where τh = σ−2
h
is the precision parameter, whereas βh = (β1h, . . . , βMh)⊺denotes a vector of coefﬁcients linearly
related to selected functions of the observed predictors λ(x) = {λ1(x), . . . , λM(x)}⊺. Formulation (8) provides a
ﬂexible construction (Barrientos et al., 2012; Pati et al., 2013), and is arguably the most widely used in Bayesian
density regression. As mentioned in Section 1, we provide here a detailed derivation of three computational methods
for Bayesian density regression under model (8), with logit stick-breaking prior (6)–(7) for the mixing weights. In
particular, we consider a Gibbs sampler converging to the exact posterior, an expectation-maximization (EM) algo-
rithm for point estimation, and a mean-ﬁeld variational Bayes (VB) approximation for scalable posterior inference.
The algorithms associated with these methods are available at https://github.com/tommasorigon/LSBP,
along with the code to reproduce the application in Section 4.
In the classical predictor-independent mixture of Gaussians framework, these computational methods are closely
related, and relevant connections can be drawn also with k-means and Bayesian k-means algorithms (Bishop, 2006;
Kurihara and Welling, 2009). A summary of these relations is depicted in Figure 1 of Kurihara and Welling (2009).
Broadly speaking, these strategies differ in how they handle unknown parameters and the involved latent quantities,
either through maximization or by taking expectations. These connections are paralleled in the LSBP model, although
our focus is mainly on Gibbs sampling, EM and VB.
Before providing a detailed derivation of these different algorithms, we ﬁrst study a truncated version of the
random probability measure px, which will be employed as an approximation of the inﬁnite process. Indeed, although
Gibbs samplers for inﬁnite representations are available (Kalli et al., 2011), developing EM and VB algorithms is not
straightforward. In line with Rodriguez and Dunson (2011) and Ren et al. (2011), we develop detailed routines based
on a ﬁnite representation. In particular, we model the ﬁrst H −1 weights ν1(x), . . . , νH−1(x) and let νH(x) = 1 for
any x ∈X, so that PH
h=1 πh(x) = 1. Based on Theorem 1 below, this choice provides an accurate approximation of
the inﬁnite representation for sufﬁciently large truncations H.
6


## Page 7


Theorem 1. For a sample y = (y1, . . . , yn)⊺with covariates X = (x1, . . . , xn)⊺, let
f (H)
X
(y) = E
 n
Y
i=1
H
X
h=1
πh(xi)√τhφ[√τh {yi −λ(xi)⊺βh}]
!
,
be the marginal joint density arising from a truncated LSBP prior with H components, and deﬁne with f (∞)
X
(y) the
same quantity in the inﬁnite case. Moreover, let µν(x) = E{νh(x)} be the expected value of a generic stick-breaking
weight. Then ||f (H)
X
(y) −f (∞)
X
(y)||1 ≤4 Pn
i=1{1 −µν(xi)}H−1, where || · ||1 denotes the L1–norm. Note that in
the above formula the expectation is taken with respect to the LSBP prior law.
According to Theorem 1, for ﬁxed sample size n and covariates X, the L1 distance between f (H)
X
(y) and f (∞)
X
(y)
vanishes as H →∞, implying that the marginal density f (H)
X
(y) converges to f (∞)
X
(y). This rate of decay is
exponential in H, and therefore the number of components does not have to be very large in practice to accurately
approximate the inﬁnite representation, thus motivating computational methods based on truncated versions.
3.1. MCMC via Gibbs sampling
In deriving a Gibbs sampler for model (8) we focus on a dependent mixture of Gaussians with ﬁxed H, and exploit
the hierarchical representation (3) along with the continuation-ratio characterization of the logit stick-breaking prior,
given in Section 2. Under these constructions, the joint law for the augmented model (3) and its parameters becomes
f(α)f(β)f(τ)
n
Y
i=1
" H
Y
h=1
(√τhφ[√τh{yi −λ(xi)⊺βh}])1(Gi=h)
H−1
Y
h=1
νh(xi)1(Gi=h){1 −νh(xi)}1(Gi>h)
#
,
(9)
with νh(xi) = exp{ψ(xi)⊺αh}/[1+exp{ψ(xi)⊺αh}], whereas f(α)f(β)f(τ) = QH−1
h=1 f(αh) QH
h=1 f(βh)f(τh)
denote the prior laws of the parameters comprising α, β and τ. As is clear from (9), given G = (G1, . . . , Gn),
sampling of βh and τh, for h = 1, . . . , H, requires standard methods for Gaussian linear regression within each
mixture component, as long as conditionally conjugate priors βh ∼NM(µβ, Σβ) and τh ∼Ga(aτ, bτ), or normal-
gammas for the pair (βh, τh), are employed. Here we focus on the ﬁrst choice to keep notation more compact.
The updating of the αh parameters, for h = 1, . . . , H −1, relies instead on a set of separate Bayesian logistic
regressions with responses zih = 1 when Gi = h and zih = 0 if Gi > h, for those units i having Gi > h −1, thus
allowing parallel sampling from the full-conditional of each αh. Adapting results from the recent P´olya-gamma data
augmentation scheme (Polson et al., 2013) to our statistical model, these updatings can be easily accomplished by
noticing that νh(xi)zih{1 −νh(xi)}1−zih =
R
fxi(zih)fxi(ωih)dωih, with laws fxi(zih) and fxi(ωih) deﬁned as
fxi(zih) = 0.5 exp{(zih −0.5)ψ(xi)⊺αh}
cosh{0.5ψ(xi)⊺αh}
,
fxi(ωih) = exp[−0.5{ψ(xi)⊺αh}2ωih]f(ωih)
[cosh{0.5ψ(xi)⊺αh}]−1
,
(10)
for every i : Gi > h −1 and h = 1, . . . , H −1. In (10), fxi(ωih) and f(ωih) are the density functions of the P´olya-
gamma random variables PG{1, ψ(xi)⊺αh}, and PG(1, 0), respectively. Hence, based on (10), the contribution to the
7


## Page 8


Algorithm 1: Steps of the Gibbs sampler for predictor-dependent ﬁnite mixtures of Gaussians
begin
[1] Assign each unit i = 1, . . . , n to a mixture component h = 1, . . . , H;
for i from 1 to n do
Sample Gi ∈{1, . . . , H} from the categorical variable with probabilities
pr(Gi = h | −) =
h
νh(xi) Qh−1
l=1 {1 −νl(xi)}
i √τhφ[√τh{yi −λ(xi)⊺βh}]
PH
q=1

νq(xi) Qq−1
l=1 {1 −νl(xi)}
 √τqφ[√τq{yi −λ(xi)⊺βq}]
,
for every h = 1, . . . , H.
[2] Update the parameters αh for h = 1, . . . , H −1 exploiting the continuation-ratio representation and the results
from the P´olya-gamma data augmentation in (10);
for h from 1 to H −1 do
for every i such that Gi > h −1 do
Sample the P´olya-gamma data ωih from (ωih | −) ∼PG{1, ψ(xi)⊺αh}.
Given the P´olya-gamma data, update αh from the full conditional (αh | −) ∼NR(µαh, Σαh), having
µαh = Σαh{Ψh(x)⊺κh + Σ−1
α µα}, Σαh = {Ψh(x)⊺diag(ω1h, . . . , ω¯nhh)Ψh(x) + Σ−1
α }−1, where
κh = (z1h −0.5, . . . , z¯nhh −0.5)⊺, with zih = 1 if Gi = h and zih = 0 if Gi > h.
[3] Update the kernel parameters βh, h = 1, . . . , H, in (8), leveraging standard Bayesian linear regression;
for h from 1 to H do
Sample the coefﬁcients comprising βh from the full conditional (βh | −) ∼NM(µβh, Σβh), with
µβh = Σβh{τhΛh(x)⊺yh + Σ−1
β µβ}, Σβh = {τhΛh(x)⊺Λh(x) + Σ−1
β }−1, and yh the nh × 1 vector
containing the responses for all the units with Gi = h.
[4] Update the precision parameters τh, h = 1, . . . , H of each kernel in (8);
for h from 1 to H do
Sample τh from (τh | −) ∼Ga[aτ + 0.5 Pn
i=1 1(Gi = h), bτ + 0.5 P
i:Gi=h{yi −λ(xi)⊺βh}2].
augmented likelihood for each pair (zih, ωih) is proportional to a Gaussian kernel for transformed data (zih−0.5)/ωih,
provided that fxi(zih)fxi(ωih) ∝exp[(zih −0.5)ψ(xi)⊺αh −0.5{ψ(xi)⊺αh}2ωih]. This allows conditionally
conjugate updating steps for each αh under a classical Bayesian linear regression framework. Refer to Choi and
Hobert (2013); Wang and Roy (2018a,b) for further theoretical properties of the P´olya-gamma scheme. Finally, note
that in (10), the latent indicators zih and the P´olya-gamma random variables ωih are conditionally independent given
the coefﬁcients αh for i : Gi > h −1. This is in contrast with the data augmentation underlying the PSBP, which
would lead to more complex calculations, especially in the EM and VB algorithms discussed in Sections 3.2 and 3.3.
The detailed steps of the Gibbs sampler for the truncated representation of model (8) are outlined in Algorithm
1. In this routine, Λh(x) and Ψh(x) denote the nh × M and the ¯nh × R predictor matrices in (8) and (7) having
row entries λ(xi)⊺and ψ(xi)⊺, for only those statistical units i such that Gi = h and Gi > h −1, respectively. We
shall also emphasize that step [1] can be run in parallel across units i = 1, . . . , n, whereas parallel computing for the
different mixture components can be easily implemented in steps [2], [3] and [4].
3.2. EM algorithm
In high-dimensional studies, the Gibbs sampler described in Section 3.1 could face computational bottlenecks. If
a point estimate of model (8) is the main quantity of interest, for example for prediction purposes, one possibility is
8


## Page 9


Algorithm 2: Steps of the EM algorithm for predictor-dependent ﬁnite mixtures of Gaussians
begin
Let (α(t), β(t), τ (t)) denote the values of the parameters at iteration t.
[1] Expectation: Exploiting results in (12), the expectation of (11) with respect to the augmented data (ζi, ¯ωi), for
each i = 1, . . . , n, can be obtained by plugging in ˆζi = E(ζi | yi, xi, β(t), τ (t)) and ˆ¯ωi = E(¯ωi | xi, ˆζi, α(t)) in
(12). Therefore:
for i from 1 to n do
for h from 1 to H do
Compute ˆζih by applying the following expression
ˆζih =
h
ν(t)
h (xi) Qh−1
l=1 {1 −ν(t)
l
(xi)}
i q
τ (t)
h φ[
q
τ (t)
h {yi −λ(xi)⊺β(t)
h }]
PH
q=1
h
ν(t)
q (xi) Qq−1
l=1 {1 −ν(t)
l
(xi)}
i q
τ (t)
q φ[
q
τ (t)
q {yi −λ(xi)⊺β(t)
q }]
,
and calculate ˆ¯ωih via ˆ¯ωih = {2ψ(xi)⊺α(t)
h }−1 tanh {0.5ψ(xi)⊺α(t)
h } PH
l=h ˆζil, (Polson et al., 2013).
[2] Maximization: To maximize the expected complete log-posterior logfx(α, β, τ | y, ˆζ, ˆ¯ω), note that according to
(11)–(12), modes α(t+1) and (β(t+1), τ (t+1)) can be obtained separately as follow:
for h from 1 to H −1 do
To compute α(t+1)
h
, note that since αh has Gaussian prior, and provided that the second term in (12) is based on
Gaussian kernels, the estimated αh at step t + 1 coincides with the mean of a full conditional Gaussian, similar
to the one in step [2] of Algorithm 1.
α(t+1)
h
= {Ψ(x)⊺diag(ˆ¯ω1h, . . . , ˆ¯ωnh)Ψ(x) + Σ−1
α }−1{Ψ(x)⊺(ˆ¯κ1h, . . . , ˆ¯κnh)⊺+ Σ−1
α µα},
where each ˆ¯κih = ˆζih −0.5 PH
l=h ˆζil and Ψ(x) is the design matrix of the logistic regression based on all units.
for h from 1 to H do
A similar approach can be considered to compute β(t+1)
h
and τ (t+1)
h
under the Gaussian and gamma priors for
these parameters and the Gaussian kernel characterizing the ﬁrst term in (12). Hence, adapting steps [3] and [4] in
Algorithm 1 to the EM setting, provides:
β(t+1)
h
=
{τ (t)
h Λ(x)⊺diag(ˆζ1h, . . . , ˆζnh)Λ(x) + Σ−1
β }−1{τ (t)
h Λ(x)⊺diag(ˆζ1h, . . . , ˆζnh)y + Σ−1
β µβ},
τ (t+1)
h
=
max{0, [aτ + 0.5
n
X
i=1
ˆζih −1][bτ + 0.5
n
X
i=1
ˆζih{yi −λ(xi)⊺β(t)
h }2]−1},
where Λ(x) is the design matrix of the Gaussian regression within each kernel based on all units.
to rely on a more efﬁcient procedure speciﬁcally designed for this goal, such as the EM (Dempster et al., 1977). The
implementation of a simple EM for a ﬁnite representation of model (8) under the LSBP prior beneﬁts from the P´olya-
gamma data augmentation, which has analytical expectation and allows direct maximization within a Gaussian linear
regression framework. Note that, although the EM algorithm is commonly implemented for maximum likelihood
estimation, it can be easily modiﬁed to estimate posterior modes (e.g. Dempster et al., 1977).
The proposed EM in Algorithm 2 alternates between a maximization step for the parameters (α, β, τ) and an
expectation step for the augmented data (ζi, ¯ωi), i = 1, . . . , n, with ζi = {ζi1 = 1(Gi = 1), . . . , ζiH = 1(Gi =
H)}⊺the vector of binary indicators denoting the membership to a mixture component, and ¯ωi = (¯ωi1, . . . , ¯ωiH−1)⊺
the corresponding P´olya-gamma augmented data. Although this data augmentation parallels the one described for the
9


## Page 10


Gibbs sampler, we adopt a slightly different notation for the P´olya-gamma random variables ¯ωih, to emphasize that
we are considering n units, and not only those for which the cluster indicators Gi > h −1. Indeed, in line with the
EM rationale, we do not condition on the membership indicators and on the P´olya-gamma latent random variables, but
we rather take expectations with respect to their conditional distributions. For the same reason, in this case we work
directly with the component indicator variables ζi instead of the binary vectors zi = (zi1, . . . , ziH−1)⊺in (5).
Based on the data augmentations outlined in (3) and (10), the complete log-posterior logfx(α, β, τ | y, ζ, ¯ω)
underlying the proposed EM routine, can be written as
n
X
i=1
ℓxi(α, β, τ; yi, ζi, ¯ωi) +
H−1
X
h=1
log f(αh) +
H
X
h=1
log f(βh) +
H
X
h=1
log f(τh) + const,
(11)
where ℓxi(α, β, τ; yi, ζi, ¯ωi) is the contribution of unit i to the complete log-likelihood. Working on the complete
log-likelihood has relevant beneﬁts. Indeed, exploiting equations (3) and (5), and the results in Polson et al. (2013)
summarized in (10), the term ℓxi(α, β, τ; yi, ζi, ¯ωi) = ℓxi(β, τ; yi, ζi) + ℓxi(α; ζi, ¯ωi), can be factorized as
H
X
h=1
ζih

−τh{yi −λ(xi)⊺βh}2
2
+ 1
2 log(τh)

+
H−1
X
h=1

¯κihψ(xi)⊺αh −¯ωih
{ψ(xi)⊺αh}2
2

+ const,
(12)
where ¯κih = ζih −0.5 PH
l=h ζil. Hence, both terms in equation (12) are linear in the augmented data (ζi, ¯ωi), and
represent the sum of Gaussian kernels. This linearity property simpliﬁes computations in the expectation step for the
complete log-posterior in equation (11), whereas the Gaussian structure allows simple maximizations. Since the joint
maximization of the expected complete log-posterior with respect to (β, τ) is intractable, we rely on a conditional
maximization procedure (Meng and Rubin, 1993) in the last step of Algorithm 2, which provides analytical solutions.
3.3. Mean-ﬁeld variational Bayes
Section 3.2 provides a scalable procedure for estimation of posterior modes in large-scale problems. However,
an appealing aspect of the Bayesian approach is in allowing uncertainty quantiﬁcation via inference on the entire
posterior. The Gibbs sampler in Section 3.1 represents an appealing procedure which converges to the exact posterior,
but faces computational bottlenecks. This motivates scalable variational methods for approximate Bayesian inference
(Bishop, 2006; Blei et al., 2017). Clearly, these computational gains do not come without some drawbacks. For
example, variational approximations typically underestimate posterior variability. This issue might be mitigated via a
post-processing operation as in Giordano et al. (2015), at the cost of an additional computational step.
Due to the P´olya-gamma data augmentation, our variational strategy is framed within the well-established expo-
nential family setting, for which there exists a closed-form coordinate ascent variational inference algorithm (CAVI).
Compared to more accurate black-box variational strategies (e.g. Ranganath et al., 2014), the CAVI algorithm is ap-
pealing because it requires no tuning. Moreover, recent theoretical properties for this class of computational methods
(Blei et al., 2017) are inherited by our variational algorithm. This seems in contrast with the variational strategy dis-
10


## Page 11


Algorithm 3: Steps of the CAVI algorithm for predictor-dependent ﬁnite mixtures of Gaussians
begin
Let q(t)(·) denote the generic variational distribution at iteration t.
[1] Compute q∗(t)
xi (zih), for each i = 1, . . . , n and h = 1, . . . , H −1;
for i from 1 to n do
for h from 1 to H −1 do
It can be easily shown that the optimal solution q∗(t)
xi (zih) for the variational distribution of each zih coincides
with the probability mass function of a Bern(ρih), having
logit(ρih) = ψ(xi)⊺E(αh) +
H
X
l=h
ζ(h)
il

0.5 · E(log τl) −0.5 · E(τl)E{(yi −λ(xi)⊺βl)2}

,
where the expectations are taken with the respect to the current variational distributions for the other
parameters, whereas ζ(h)
il
= Ql−1
r=1(1 −ρir) if l = h, and ζ(h)
il
= −ρil
Ql−1
r=1,r̸=h(1 −ρir) otherwise. Note
also that ρiH = 1.
[2] Compute q∗(t)
x
(αh), for each h = 1, . . . , H −1;
for h from 1 to H −1 do
The optimal solution q∗(t)
x
(αh) for the variational distribution of each αh is the density of the Gaussian random
variable NR[{Ψ(x)⊺VhΨ(x) + Σ−1
α }−1{Ψ(x)⊺ρh + Σ−1
α µα}, {Ψ(x)⊺VhΨ(x) + Σ−1
α }−1] with
Vh= diag{E(ω1h), . . . , E(ωnh)} and ρh= (ρ1h −0.5, . . . , ρnh −0.5)⊺.
[3] Compute the variational distribution q∗(t)
xi (ωih) for each i = 1, . . . , n and h = 1, . . . , H −1;
for i from 1 to n do
for h from 1 to H −1 do
Update the optimal solution q∗(t)
xi (ωih) to obtain the density of a P´olya-gamma PG (1, ξih), with
ξ2
ih = ψ(xi)⊺E(αhα⊺
h)ψ(xi). Recall that E(ωih) = 0.5ξ−1
ih tanh(0.5ξih).
[4] Compute q∗(t)
x
(βh) and q∗(t)
x
(τh), for each h = 1, . . . , H;
for h from 1 to H do
Update variational solutions for βh and τh. In particular, q∗(t)
x
(βh) and q∗(t)
x
(τh) are easily available as the
densities of the Gaussian
NM[{Λ(x)⊺ΓhΛ(x) + Σ−1
β }−1{Λ(x)⊺Γhy + Σ−1
β µβ}, {Λ(x)⊺ΓhΛ(x) + Σ−1
β }−1] and the gamma
Ga[aτ + 0.5 Pn
i=1 E(ζih), bτ + 0.5 Pn
i=1 E(ζih)E{yi −λ(xi)⊺βh}2], respectively, with
Γh = E(τh)diag{E(ζ1h), . . . , E(ζnh)} and ζih = zih
Qh−1
l=1 (1 −zil), i = 1, . . . , n.
cussed by Ren et al. (2011), which considers a local approximation based on the lower bound of Jaakkola and Jordan
(2000). However, the recent contribution of Durante and Rigon (2019) allows to draw a sharp connection between
the P´olya-gamma data augmentation and the Jaakkola and Jordan (2000) lower bound. As a consequence, the VB
approach we propose relies on the same optimization problem considered by Ren et al. (2011).
Compared to the Gibbs sampler in Section 3.1, here we augment the entire model (8) with respect to the binary
vectors zi = (zi1, . . . , ziH−1)⊺, i = 1, . . . , n comprising z, rather than using the membership indicators G. Hence,
the joint law fx(y, α, β, τ, z, ω) = fx(y | z, β, τ)fx(z | α)fx(ω | α)f(α)f(β)f(τ) is equal to
f(α)f(β)f(τ)
n
Y
i=1
" H
Y
h=1
(√τhφ[√τh{yi −λ(xi)⊺βh}])zih
Qh−1
l=1 (1−zil)
H−1
Y
h=1
f(ωih)
2
exp{(zih −0.5)ψ(xi)⊺αh}
exp {0.5ωih(ψ(xi)⊺αh)2}
#
, (13)
11


## Page 12


where ziH = 1. Our goal is to ﬁnd a variational distribution qx(α, β, τ, z, ω) that best approximates the joint posterior
fx(α, β, τ, z, ω | y), while maintaining simple computations. This can be obtained by minimizing the Kullback-
Leibler divergence KL{qx(α, β, τ, z, ω) || fx(α, β, τ, z, ω | y)} between the variational distribution and the full
posterior, or, alternatively, by maximizing the evidence lower bound ELBO{qx(α, β, τ, z, ω)} of the log-marginal
density log f (H)
X
(y), since log f (H)
X
(y) can be analytically expressed as the sum of the ELBO and the positive KL
divergence. This evidence lower bound to be maximized can be expressed as
X
z
Z
qx(α, β, τ, z, ω)

log
fx(y | z, β, τ)fx(z | α)fx(ω | α)f(α)f(β)f(τ)
qx(α, β, τ, z, ω)

d(α, β, τ, ω).
Without further restrictions, the Kullback-Leibler divergence is minimized when the variational distribution is equal
to the true posterior, which is intractable. To address this issue, a common strategy is to assume that the variational
distribution belongs to a mean-ﬁeld family (see e.g. Blei et al., 2017). This incorporates a posteriori independence
among distinct groups of parameters, implying that the variational distribution can be expressed as the product of
marginal laws. Speciﬁcally, we consider the following factorization for the variational distribution
qx(α, β, τ, z, ω) =
H−1
Y
h=1
qx(αh)
H
Y
h=1
qx(βh)
H
Y
h=1
qx(τh)
H−1
Y
h=1
n
Y
i=1
qxi(zih)
H−1
Y
h=1
n
Y
i=1
qxi(ωih).
(14)
Note that we are not making speciﬁc assumptions about the functional form of the variational distributions. Combining
(13) with (14), we obtain a tractable expression for the ELBO, which can be easily maximized as in Bishop (2006, Ch.
10). In particular, the optimal solutions are provided by the following system of equations
log q∗
x(βh) = Eτ,z[log{fx(y | z, β, τ)f(βh)}] + cβh,
h = 1, . . . , H,
log q∗
x(τh) = Eβ,z[log{fx(y | z, β, τ)f(τh)}] + cτh,
h = 1, . . . , H,
log q∗
x(αh) = Ez,ω[log{fx(z, ω | α)f(αh)}] + cαh,
h = 1, . . . , H −1,
log q∗
xi(zih) = Eα,β,τ,zi,−h[log fx(y, z | β, τ, α)] + czih,
h = 1, . . . , H −1, i = 1, . . . , n,
log q∗
xi(ωih) = Eα[log fx(ωih | α)] + cωih,
h = 1, . . . , H −1, i = 1, . . . , n,
where zi,−h denotes the vector of binary indicators zi without considering the hth one, whereas cβh, cτh, cαh, czih
and cωih, are additive constants with respect to the argument in the corresponding variational distribution. Each ex-
pectation in the above equations is evaluated with respect to the variational distribution of the other parameters, and
therefore we need to rely on iterative methods to ﬁnd the optimal solution. We consider the coordinate ascent varia-
tional inference (CAVI) iterative procedure—described in Algorithm 3—which maximizes the variational distribution
of each parameter based on the current estimate for the remaining ones (e.g. Bishop, 2006, Ch. 10). This proce-
dure generates a monotone sequence for the ELBO{qx(α, β, τ, z, ω)}, which ensures convergence to a local joint
maximum. Refer to Blei et al. (2017) for practical guidelines to address issues of local maxima via multiple runs.
12


## Page 13


Finally, note that as shown in Algorithm 3, the normalizing constants in the above equations have not to be computed
numerically, since kernels of well known distributions can be recognized.
4. Epidemiology application
We compare the performance of the three computational methods developed in Section 3, in a toxicology study.
Consistent with recent interests in Bayesian density regression (e.g. Dunson and Park, 2008; Hwang and Pennell,
2014; Canale et al., 2018), we focus on a dataset aimed at studying the relationship between the DDE concentration in
maternal serum, and the gestational days at delivery (Longnecker et al., 2001).
The DDE is a metabolite of DDT, which is still used against malaria-transmitting mosquitoes in certain develop-
ing countries—according to the Malaria Report 2015 from the World Health Organization—thus raising concerns
about its adverse effects on premature delivery. Popular studies in reproductive epidemiology address this goal by
dichotomizing the gestational age at delivery (GAD) with a clinical threshold, so that births occurred before the 37th
week are considered preterm. Although this approach allows for a simpler modeling strategy, it leads to a clear loss of
information. In particular, a greater risk of mortality and morbidity is associated with preterm birth, which increases
rapidly as the GAD decreases. This has motivated an increasing interest in modeling how the entire distribution of
GAD changes with DDE exposure (e.g. Dunson and Park, 2008; Hwang and Pennell, 2014; Canale et al., 2018).
Data are composed by n = 2312 measurements (xi, yi), i = 1, . . . , n, where xi denotes the DDE concentration,
and yi is the gestational age at delivery for woman i. Our goal is to reproduce the analyses in Dunson and Park (2008)
on this dataset, and compare the inference and computational performance of the MCMC via Gibbs sampling, the EM
algorithm, and the VB routine proposed in Section 3. Note that, consistent with the main novelty of this contribution,
we do not attempt to improve the ﬂexibility and the efﬁciency of the available statistical models for Bayesian density
regression—such as the kernel stick-breaking (Dunson and Park, 2008), and the PSBP (Rodriguez and Dunson, 2011).
Indeed, as discussed in Sections 1 and 2, these representations are expected to provide a comparable performance to
our LSBP in terms of inference. However, unlike current models for Bayesian density regression, inference under the
LSBP is available under a broader variety of simple computational methods, thus facilitating implementation of the
same model in a wider range of applications—including large M, R and n settings. Due to this, the main focus is on
providing an empirical comparison of the algorithms in Section 3, while using results in Dunson and Park (2008) as a
benchmark to provide reassurance that inference under the LSBP is comparable to alternative representations.
We apply the predictor-dependent mixture of Gaussians (8) with LSBP (6)–(7), to a normalized version of the
DDE and GAD (¯xi, ¯yi), i = 1, . . . , n, and then show results for fx(y) on the original scale of the data. Consistent
with previous works (Dunson and Park, 2008; Canale et al., 2018), we let M = 2, with λ1(¯xi) = 1 and λ2(¯xi) =
¯xi, for every i = 1, . . . , n, and rely instead on a ﬂexible representation for ηh(¯xi) to characterize changes in the
stick-breaking weights with DDE. In particular, each ηh(¯xi) is deﬁned via a natural cubic spline basis ψ(¯xi) =
{1, ψ1(¯xi), . . . , ψ5(¯xi)}⊺, for every h = 1, . . . , H −1. Bayesian posterior inference—under the three computational
13


## Page 14


12.57
28.44
53.72
105.47
EM
Gibbs sampler
Variational Bayes
210
240
270
300
210
240
270
300
210
240
270
300
210
240
270
300
0.00
0.01
0.02
0.03
0.00
0.01
0.02
0.03
0.00
0.01
0.02
0.03
Gestational age at delivery
Density
Figure 2: For selected quantiles of DDE ∈(12.57, 28.44, 53.72, 105.47), graphical representation of the posterior mean of the conditional density
for GAD given DDE, obtained from the Gibbs sampler and the VB, together with 0.95 pointwise credibility intervals (shaded area). Since the EM
provides only a mode for the conditional density, we consider a graphical representation of the plug-in estimate for f(y | x). The histograms
represent the observations of GAD, having DDE in the intervals (−∞, 20.505), [20.505, 41.08), [41.08, 79.6), [79.6, ∞), respectively.
methods developed in Section 3—is instead performed with default hyperparameters µβ = (0, 0)⊺, Σβ = I2×2,
µα = (0, . . . , 0)⊺, Σα = I6×6 and aτ = bτ = 1. For the total number of mixture components we consider H = 20,
and allow the shrinkage induced by the stick-breaking prior to adaptively delete redundant components not required
to characterize the data. As shown in Figure 2, these choices allows accurate inference on fx(y).
In providing posterior inference under the Gibbs sampling algorithm described in Section 3.1, we rely on 30,000
iterations, after discarding the ﬁrst 5,000 as a burn-in, and initialize the routine from random starting values sampled
from the prior. Analysis of the traceplots for the quantities discussed in Figures 2 and 3 showed that this choice is
sufﬁcient for good convergence. The EM algorithm and the VB procedures discussed in Sections 3.2 and 3.3, respec-
tively, are instead run until convergence to a modal solution. Since such modes could be local, we run both algorithms
for different initial values, and consider the solutions having the highest log-posterior and ELBO, respectively. We
also controlled the monotonicity of the sequences for these quantities, in order to further validate the correctness of
our derivations. In this study, the EM and the VB reach convergence in about 2 and 6 seconds, respectively, whereas
the Gibbs sampler requires 5 minutes, using a MacBook Air with a Intel Core i5.
Similarly to Figure 3 in Dunson and Park (2008), Figure 2 provides posterior inference for the conditional density
fx(y) evaluated at the 0.1, 0.6, 0.9, 0.99 quantiles of DDE, for the three algorithms. Histograms for the GAD, are
instead obtained by grouping the response data according to a binning of the DDE with cut-offs at the central values
of subsequent quantiles, so that the conditional density can be plotted alongside the corresponding histogram. Results
in Figure 2 conﬁrm accurate ﬁt to the data and suggest that the left tail of the GAD distribution—associated with
preterm deliveries—increasingly inﬂates as DDE grows. Moreover, as seen in Figure 2, the three algorithms have
14


## Page 15


y* = 7 x 33
y* = 7 x 35
y* = 7 x 37
y* = 7 x 40
EM
Gibbs sampler
Variational Bayes
0
50
100
150
0
50
100
150
0
50
100
150
0
50
100
150
0.00
0.25
0.50
0.75
0.00
0.25
0.50
0.75
0.00
0.25
0.50
0.75
DDE (mg/L)
Pr(Gestational Length < y*)
Figure 3: For the Gibbs sampler and the VB, posterior means of four different conditional probabilities pr(y < y∗| x)—based on thresholds
y∗∈(7 × 33, 7 × 35, 7 × 37, 7 × 40)—along with 0.95 pointwise credibility intervals (shaded area). These quantities are not available from the
EM algorithm, for which a plug-in estimate of pr(y < y∗| x) is displayed.
similar results, thus providing empirical reassurance for the goodness of the proposed routines. Although the EM
outputs a posterior mode, such an estimate matches closely the posterior mean of the Gibbs sampler, whereas the VB
tends to over-smooth some modes of the conditional distribution. This is likely due to the fact that the VB provides an
approximation of the posterior, instead of the exact one. However, unlike for the EM, this routine allows uncertainty
quantiﬁcation, and provides a much scalable methodology compared to the Gibbs sampler, thus representing a valid
candidate in high-dimensional inference when the focus is on speciﬁc functionals of fx(y). Indeed, as shown in Figure
3, when the aim is to exploit fx(y) to infer conditional preterm probabilities pr(y < y∗| x) =
R y∗
−∞fx(y)dy with
y∗∈(7 × 33, 7 × 35, 7 × 37, 7 × 40) denoting a clinical threshold, the VB provides very similar conclusions.
Prior to conclude our analysis, note that the results in Figures 2 and 3 are similar to those obtained under the kernel
stick-breaking prior in Dunson and Park (2008). This provides empirical guarantee that the ﬂexibility characterizing
popular Bayesian nonparametric models for density regression is maintained also under LSBP, which has the additional
relevant beneﬁt of facilitating computational implementation of these methodologies. Minor differences are found at
extreme DDE exposures, but this is mainly due to the sparsity of the data in this subset of the predictor space.
5. Discussion
The focus of this paper has been on providing novel methods to facilitate the computational implementation of
Bayesian nonparametric models for density regression in a broad range of applications. To address this goal, we
have proposed an alternative reparameterization of the predictor-dependent stick-breaking weights, which relies on
a set of sequential logistic regressions. This representation has relevant connections with continuation-ratio logistic
15


## Page 16


regressions and P´olya-gamma data augmentation, thus allowing simple derivation of several algorithms of routine use
in Bayesian inference. The proposed computational methods are empirically evaluated in a toxicology study, obtaining
good results and reassurance that the LSBP maintains the same ﬂexibility and efﬁciency properties characterizing
popular Bayesian nonparametric models for density regression.
Although our dependent mixture of Gaussians provides a ﬂexible representation, it is worth considering extensions
to other kernels. For example, all our algorithms can be easily adapted to predictor-independent kernels coming from
an exponential family, when conjugate priors for their parameters are used. Similar derivations are also possible for
predictor-dependent kernels within a generalized linear model representation, provided that conjugate priors for the
coefﬁcients can be found (e.g. Chen and Ibrahim, 2003).
Acknowledgments
The authors are grateful to the Associate Editor and the four referees for the insightful comments and suggestions
that led to a substantial improvement of the paper. This work was partially supported by grant 1R01ES027498 of the
National Institutes of Environmental Health Sciences of the United States National Institutes of Health, and by the
MIUR–PRIN 2017 grant 20177BRJXS.
Appendix. Proofs and additional properties of the LSBP
Proposition 1. For any ﬁxed x ∈X, P∞
h=1 πh(x) = 1 almost surely, with πh(x) factorized as in (6) and αh ∼
NR(µα, Σα) independently for every h ∈N. Hence, the LSBP provides a well deﬁned predictor-dependent random
probability measure px at every x ∈X.
Proof of Proposition 1. Recalling results in Ishwaran and James (2001), we have that P∞
h=1 πh(x) = 1 almost surely
if and only if the equality P∞
h=1 E[log{1−νh(x)}] = −∞holds. Since log{1−νh(x)} is concave in νh(x) for every
x ∈X and h ∈N, by the Jensen inequality E[log{1−νh(x)}] ≤log[1−E{νh(x)}]. Therefore, since νh(x) ∈(0, 1),
we have that 0 < E{νh(x)} = µν(x) < 1, thereby providing log{1 −µν(x)} < 0. Leveraging these results, the
proof of Proposition 1 follows after noticing that P∞
h=1 E[log{1 −νh(x)}] ≤P∞
h=1 log{1 −µν(x)} = −∞.
Proof of Theorem 1. Adapting the proof of Theorem 1 in Ishwaran and James (2002) to our representation we have
||f (H)
X
(y) −f (∞)
X
(y)||1 ≤4
"
1 −E
( n
Y
i=1
H−1
X
h=1
πh(xi)
)#
= 4 · E
"
1 −
n
Y
i=1
H−1
X
h=1
πh(xi)
#
.
Since PH−1
h=1 πh(xi) ≤1, and 1 = Qn
i=1 1, we can write 1−Qn
i=1
PH−1
h=1 πh(xi) = Qn
i=1 1−Qn
i=1
PH−1
h=1 πh(xi) ≤
Pn
i=1{1−PH−1
h=1 πh(xi)} (Billingsley, 1995, pp. 358). Hence ||f (H)
X
(y)−f (∞)
X
(y)||1 ≤4[n−Pn
i=1
PH−1
h=1 E{πh(xi)}],
with PH−1
h=1 E{πh(xi)} = PH−1
h=1 µν(xi){1 −µν(xi)}h−1 = 1 −{1 −µν(xi)}H−1. Substituting this quantity in
4[n −Pn
i=1
PH−1
h=1 E{πh(xi)}], we obtain the ﬁnal bound 4 Pn
i=1{1 −µν(xi)}H−1.
16


## Page 17


References
Aitchison, J., Shen, S.M., 1980. Logistic-normal distributions: some properties and uses. Biometrika 67, 262–272.
Albert, J.H., Chib, S., 1993. Bayesian analysis of binary and polychotomous response data. Journal of the American Statistical Association 88,
669–679.
Amemiya, T., 1981. Qualitative response models: a survey. Journal of Economic Literature 19, 1483–1536.
Antoniano-Villalobos, I., Wade, S., Walker, S., 2014. A Bayesian nonparametric regression model with normalized weights: a study of hippocampal
atrophy in Alzheimer’s disease. Journal of the American Statistical Association 109, 477–490.
Barrientos, A.F., Jara, A., Quintana, F.A., 2012. On the support of MacEachern’s dependent Dirichlet processes and extensions. Bayesian Analysis
7, 277–310.
Billingsley, P., 1995. Probability and Measure, Third Edition. Wiley.
Bishop, C.M., 2006. Pattern Recognition and Machine Learning. Springer.
Blei, D.M., Kucukelbir, A., McAuliffe, J.D., 2017. Variational inference: a review for statisticians. Journal of the American Statistical Association
112, 859–877.
Canale, A., Durante, D., Dunson, D.B., 2018. Convex mixture regression for quantitative risk assessment. Biometrics 74, 1331–1340.
Chen, M.H., Ibrahim, J.G., 2003. Conjugate priors for generalized linear models. Statistica Sinica 13, 461–476.
Choi, H.M., Hobert, J.P., 2013. The Polya-Gamma Gibbs sampler for Bayesian logistic regression is uniformly ergodic. Electronic Journal of
Statistics 7, 2054–2064.
De Iorio, M., M¨uller, P., Rosner, G.L., MacEachern, S.N., 2004. An ANOVA model for dependent random measures. Journal of the American
Statistical Association 99, 205–215.
De la Cruz-Mes´ıa, R., Quintana, F.A., M¨uller, P., 2007. Semiparametric Bayesian classiﬁcation with longitudinal markers. Journal of the Royal
Statistical Society: Series C 56, 119–137.
Dempster, A.P., Laird, N.M., Rubin, D.B., 1977. Maximum likelihood from incomplete data via the EM algorithm. Journal of the Royal Statistical
Society, Series B 39, 1–38.
Dunson, D.B., Park, J.H., 2008. Kernel stick-breaking processes. Biometrika 95, 307–323.
Durante, D., Rigon, T., 2019. Conditionally conjugate mean-ﬁeld variational Bayes for logistic models. Statistical Science 34, 472–485.
Escobar, M.D., West, M., 1995. Bayesian density estimation and inference using mixtures. Journal of the American Statistical Association 90,
577–588.
Ferguson, T.S., 1973. A Bayesian analysis of some nonparametric problems. The Annals of Statistics 1, 209–230.
Gelfand, A.E., Kottas, A., MacEachern, S.N., 2005. Bayesian nonparametric spatial modeling with Dirichlet process mixing. Journal of the
American Statistical Association 100, 1021–1035.
Ghosal, S., Ghosh, J.K., Ramamoorthi, R., 1999. Posterior consistency of Dirichlet mixtures in density estimation. The Annals of Statistics 27,
143–158.
Ghosal, S., Van Der Vaart, A., 2007. Posterior convergence rates of Dirichlet mixtures at smooth densities. The Annals of Statistics 35, 697–723.
Giordano, R., Broderick, T., Jordan, M., 2015. Linear response methods for accurate covariance estimates from mean ﬁeld variational Bayes, in:
Neural Information Processing Systems, pp. 1–19.
Grifﬁn, J.E., Steel, M.F., 2006. Order-based dependent Dirichlet processes. Journal of the American Statistical Association 10, 179–194.
Grifﬁn, J.E., Steel, M.F., 2011. Stick-breaking autoregressive processes. Journal of Econometrics 162, 383–396.
Guti´errez, L., Mena, R.H., Ruggiero, M., 2016. A time dependent Bayesian nonparametric model for air quality analysis. Computational Statistics
& Data Analysis 95, 161–175.
Hwang, B.S., Pennell, M.L., 2014. Semiparametric Bayesian joint modeling of a binary and continuous outcome with applications in toxicological
risk assessment. Statistics in Medicine 33, 1162–1175.
Ishwaran, H., James, L.F., 2001. Gibbs sampling methods for stick-breaking priors. Journal of the American Statistical Association 96, 161–173.
17


## Page 18


Ishwaran, H., James, L.F., 2002. Approximate Dirichlet process computing ﬁnite normal mixtures: smoothing and prior information. Journal of
Computational and Graphical Statistics 11, 508–532.
Jaakkola, T.S., Jordan, M.I., 2000. Bayesian parameter estimation via variational methods. Statistics and Computing 10, 25–37.
Johndrow, J.E., Smith, A., Pillai, N., Dunson, D.B., 2019. MCMC for imbalanced categorical data. Journal of the American Statistical Association
114, 1394–1403.
Kalli, M., Grifﬁn, J.E., Walker, S.G., 2011. Slice sampling mixture models. Statistics and Computing 21, 93–105.
Kurihara, K., Welling, M., 2009. Bayesian k-means as a “Maximization-Expectation” algorithm. Neural Computation 21, 1145–1172.
Longnecker, M.P., Klebanoff, M.A., Zhou, H., Brock, J.W., 2001. Association between maternal serum concentration of the DDT metabolite DDE
and preterm and small-for-gestational-age babies at birth. Lancet 358, 110–114.
MacEachern, S.N., 1999. Dependent nonparametric processes, in: Proceedings of the Bayesian Section, pp. 50–55.
MacEachern, S.N., 2000. Dependent Dirichlet processes. Technical Report. Department of Statistics, Ohio State University.
Meng, X.L., Rubin, D.B., 1993. Maximum likelihood estimation via the ECM algorithm: a general framework. Biometrika 80, 267–278.
Neal, R.M., 2000. Markov chain sampling methods for Dirichlet process mixture models. Journal of Computational and Graphical Statistics 9,
249–265.
Nelder, J.A., Wedderburn, R.W.M., 1972. Generalized linear models. Journal of the Royal Statistical Society, Series A 135, 370 – 384.
Pati, D., Dunson, D.B., Tokdar, S.T., 2013. Posterior consistency in conditional distribution estimation. Journal of Multivariate Analysis 116,
456–472.
Pitman, J., Yor, M., 1997. The two-parameter Poisson-Dirichlet distribution derived from a stable subordinator. The Annals of Probability 25,
855–900.
Polson, N.G., Scott, J.G., Windle, J., 2013. Bayesian inference for logistic models using P´olya–Gamma latent variables. Journal of the American
Statistical Association 108, 1339–1349.
Ranganath, R., Gerrish, S., Blei, D., 2014. Black box variational inference, in: Artiﬁcial Intelligence and Statistics, pp. 814–822.
Ren, L., Du, L., Carin, L., Dunson, D.B., 2011. Logistic stick-breaking process. Journal of Machine Learning Research 12, 203–239.
Rodriguez, A., Dunson, D.B., 2011. Nonparametric Bayesian models through probit stick-breaking processes. Bayesian Analysis 6, 145–178.
Tokdar, S.T., 2006. Posterior consistency of Dirichlet location-scale mixture of normals in density estimation and regression. Sankhy¯a: The Indian
Journal of Statistics , 90–110.
Tutz, G., 1991. Sequential models in categorical regression. Computational Statistics & Data Analysis 11, 275–295.
Wade, S., Dunson, D.B., Petrone, S., Trippa, L., 2014. Improving prediction from Dirichlet Process mixtures via enrichment. Journal of Machine
Learning Research 15, 1041–1071.
Wang, X., Roy, V., 2018a. Analysis of the P´olya-gamma block Gibbs sampler for Bayesian logistic linear mixed models. Statistics and Probability
Letters 137, 251–256.
Wang, X., Roy, V., 2018b. Geometric ergodicity of P´olya-Gamma Gibbs sampler for Bayesian logistic regression with a ﬂat prior. Electronic
Journal of Statistics 12, 3295–3311.
18

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
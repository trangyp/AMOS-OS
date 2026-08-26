---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.06722v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1911.06722v3_Bayesian_nonparametric_discontinuity_design

> Source: 1911.06722v3_Bayesian_nonparametric_discontinuity_design.pdf

> Pages: 15

---


## Page 1


Bayesian nonparametric discontinuity design
Max Hinne, David Leeftink, Marcel A. J. van Gerven, and Luca Ambrogioni
Radboud University, Nijmegen, The Netherlands
m.hinne@donders.ru.nl
December 15, 2021
Abstract
Quasi-experimental research designs, such as regression discontinuity and interrupted time series,
allow for causal inference in the absence of a randomized controlled trial, at the cost of additional
assumptions. In this paper, we provide a framework for discontinuity-based designs using Bayesian
model comparison and Gaussian process regression, which we refer to as ‘Bayesian nonparametric
discontinuity design’, or BNDD for short. BNDD addresses the two major shortcomings in most
implementations of such designs: overconﬁdence due to implicit conditioning on the alleged eﬀect, and
model misspeciﬁcation due to reliance on overly simplistic regression models. With the appropriate
Gaussian process covariance function, our approach can detect discontinuities of any order, and in
spectral features. We demonstrate the usage of BNDD in simulations, and apply the framework to
determine the eﬀect of running for political positions on longevity, of the eﬀect of an alleged historical
phantom border in the Netherlands on Dutch voting behaviour, and of Kundalini Yoga meditation
on heart rate.
1
Introduction
The bread and butter of scientiﬁc research is the randomized-controlled trial (RCT) (Hill, 1952). In
this design, the sample population is randomly divided into two groups; one that is manipulated (e.g. a
drug is administered or a treatment is performed), while the other is left unchanged. RCT allows one
to perform causal inference, and learn about the causal eﬀect of the intervention (Imbens and Rubin,
2015; Pearl, 2009).
However, in practice there may be several insurmountable ethical or pragmatic
hurdles that deter one from using RCT, such as ethical or pragmatic concerns. Luckily, all is not lost
for experimental design. There exist several quasi-experimental designs (QEDs) that replace random
assignment with deterministic assignment, which still allow for causal inferences, but at the cost of
additional assumptions (Shadish et al., 2002). Prominent examples are regression discontinuity (RD)
and interrupted time series (ITS) designs, that assign a sample to one of the two groups based on it
passing a threshold on an assignment variable (Campbell and Stanley, 1963; Lauritzen, 2001; McDowall
et al., 1980). The idea behind these approaches is that, around the assignment threshold, observations
are distributed essentially randomly, so that locally the conditions of RCT are recreated (Imbens and
Lemieux, 2008; Lee and Lemieux, 2010). The methodological pipeline of quasi-experimental designs like
these generally consists of three steps (Rischard et al., 2021). First, a regression (typically linear) is ﬁt
to each of the two groups individually. Next, the regressions are extrapolated to the threshold (RD), or
to the entire post-intervention range (ITS). Finally, the diﬀerence between the extrapolations of the two
groups is taken as the eﬀect size of the intervention. A straightforward statistical test can be applied to
check whether the eﬀect is present.
Here, we provide a novel framework for such approaches, which we call ‘Bayesian nonparametric dis-
continuity design’ (BNDD). The main innovations of BNDD are: First, we frame the problem of detecting
an eﬀect as Bayesian model comparison. Instead of comparing the pre- and post-intervention regressions,
we introduce a continuous model and a discontinuous model. In the discontinuous model, observations
before and after the intervention are assumed to be independent, while in the continuous model this
assumption is lifted. We quantify the evidence in favor of either model, rather than only for the alterna-
tive model, via Bayesian model comparison (Wagenmakers, 2007). This enables the computation of the
1
arXiv:1911.06722v3  [stat.ME]  14 Dec 2021


## Page 2


marginal eﬀect size, which provides a more nuanced estimate compared to implicitly conditioning on the
alternative model (Hoeting et al., 1999). Furthermore, the model comparison approach automatically
penalizes the discontinuous model for its additional ﬂexibility (MacKay, 2002). Second, we use Gaussian
process (GP) regression to avoid strong parametric assumptions. The result is a ﬂexible model that can
capture nonlinear interactions between the predictor and outcome variables. Traditional assumptions,
such as linearity, can still be implemented in our model by using the appropriate covariance function.
At the same time, much more expressive covariance functions can be used, such as the spectral mixture
kernel (Wilson and Adams, 2013), that better capture long-range correlations, and lead to more accu-
rate inference. Lastly, in most discontinuity-based methods for quasi-experimental design, a bandwidth
parameter determines the trade-oﬀbetween estimation reliability and the local randomness assumptions
that are needed to draw causal inferences (Geneletti et al., 2015). In BNDD, all observations are used to
estimate both the continuous and discontinuous model, but by optimizing the length-scale parameter of
the GP covariance functions we control the sensitivity to diﬀerent types of discontinuities and adherence
to locality assumptions.
2
Related work
While quasi-experimental designs have been around since the 1960s (Campbell and Stanley, 1963;
Thistlethwaite and T, 1960), recently there has been a renewed interest in this class of methods (Choi
and Lee, 2017; Imbens and Lemieux, 2008), in particular in epidemiology (Harris et al., 2004) and ed-
ucation (Bloom, 2012). Researchers from diﬀerent domains are promoting the use of QED (Li et al.,
2021; Marinescu et al., 2018; Moscoe et al., 2015), which has prompted several extensions of classical
QEDs. For instance, several authors have proposed to use Bayesian models for QED (Freni-Sterrantino
et al., 2019; Geneletti et al., 2015). By assuming a prior distribution for alleged eﬀect size and using
Bayes’ theorem, these studies provide an explicit descriptions of the estimation uncertainty. In contrast
to our work, these methods focus on the estimation of the treatment eﬀect instead of model comparison,
and typically assume restrictive parametric forms. Other studies have considered nonparametric alter-
natives to linear models. For example, Hahn et al. (2001) use locally linear nonparametric regression.
Alternatively, one can use kernel methods that compute a smoothly weighted average of the data points
to create an interpolated regression that does not depend on a speciﬁc parametric form (Bloom, 2012).
Most similar to BNDD are the approaches by Branson et al. (2019); Rischard et al. (2021). Here, instead
of ﬁtting a parametric form such as linear regression, the regression is modelled by a GP, which results in
a ﬂexible, nonparametric model and more accurate eﬀect size estimates compared to when using linear
regression. BNDD uses GP regression as well, but whereas Branson et al. (2019); Rischard et al. (2021)
focus on the inference of the magnitude of the treatment eﬀect, we ﬁrst determine whether an eﬀect
is present at all using Bayesian model comparison (Wagenmakers, 2007), and we use Bayesian model
averaging (Hoeting et al., 1999) to reduce the overconﬁdence that follows from conditioning on the al-
ternative model or particular covariance functions. Consequently, BNDD is less prone to false positives,
is able to detect discontinuities in derivatives of the latent function rather than in the function per sé,
and using the spectral mixture kernel our approach is well-suited for detecting changes in time series,
which is crucial in ITS design.
3
Discontinuity-based causal inference
We provide a brief introduction of the background of causal inference using RD and ITS designs, for a
more in-depth discussion, we refer to e.g. Bernal et al. (2017); McDowall et al. (1980). The detection of
a causal eﬀect is naturally formulated using the potential outcomes framework by Rubin (1974), which
assumes that for each individual in the study both the outcome of the treatment and its alternative can
potentially be observed.
Consider an observation i (with or without temporal ordering) with independent variable xi ∈Rp
and response yi ∈Rq (we will assume p = q = 1, but multidimensional extensions are straightforward).
In addition, we observe an indicator variable zi, where zi = 1 denotes the intervention of interest has
2


## Page 3


been applied to case i, and zi = 0 indicates it has not. The outcome depends on treatment, so
yi =
(
yi(0)
if zi = 0,
yi(1)
if zi = 1.
(1)
The individual causal eﬀect is deﬁned as the diﬀerence between these two potential outcomes, that is
di = yi(1) −yi(0). Since we only ever observe one outcome, the individual causal eﬀect is out of reach,
so in RD design we focus on the average causal eﬀect (ACE) instead, deﬁned by the diﬀerences in the
expectations:
dACE = E[y(1)] −E[y(0)] .
(2)
In the randomized controlled trial, the assignment of treatment zi is random, so that all diﬀerences other
than due to the treatment are integrated out in these expectations (Bloom, 2012). In QED designs
such as RD and ITS however, the allocation to intervention or control group is based on a threshold
x0 (O’Keeﬀe and Baio, 2016):
zi =
(
1
if xi ≥x0 and
0
otherwise.
(3)
This changes how the ACE is computed, which for RD design becomes (Imbens and Kalyanaraman,
2012; Lee and Lemieux, 2010):
dRD = E[yi(1) −yi(0) | xi = x0]
= lim
x↓x0 E[yi|xi = x0] −lim
x↑x0 E[yi|xi = x0] ,
(4)
provided the distributions of yi given xi are continuous in x, and the conditional expectations E[yi(1) | xi]
and E[yi(0) | xi] exist.
For interrupted time series, there are no post-intervention control observations, as all post-threshold
observations xi ≥x0 are in the intervention group. Here, the causal estimand becomes the average eﬀect
of the treatment on the treated (ATT) (Kim and Steiner, 2016):
dITS(xi) = E[yi(1) −yi(0) | xi ≥x0]
= E[yi | xi, D] −E[yi | xi, D0] ,
(5)
for xi ≥x0, D = {(xi, yi)}n
i=1, and D0 = {(xi, yi)}xi<x0. Intuitively, this measure of eﬀect size is the
diﬀerence between the extrapolation based on the pre-intervention data, and the actual post-intervention
observations. Due the the reliance on extrapolation, it is crucial that correct assumptions are made on
the functional form. For example, assuming linearity will lead to a biased ATT estimate if this does not
describe the functional form well.
Importantly, for both approaches we assume there are no confounding variables that aﬀect the rela-
tionship between x and y (for a more in-depth discussion of RD design, see Geneletti et al. (2015)).
4
Bayesian nonparametric discontinuity design
In standard RD and ITS analyses, causal conclusions are drawn by estimating the eﬀect d and testing
whether this diﬀers from zero. Instead, we perform Bayesian model comparison to see whether the data
are better supported by the alternative model M1, that claims an eﬀect is present, than by the null
model M0, in which such an eﬀect is absent. The result of the model comparison is quantiﬁed by the
Bayes factor (Kass and Raftery, 1995):
BF10 = p(D | M1)
p(D | M0) .
(6)
Here, p(D | M1) and p(D | M0) are the marginal likelihoods of the two models with their respective
parameters integrated out. The Bayes factor indicates how much more likely the data are given the
discontinuous model, compared to the continuous model (Jarosz and Wiley, 2014). Unlike a p-value, it
can provide evidence for either model, so that it is possible to ﬁnd evidence supporting the absence of
3


## Page 4


a discontinuity (Goodman, 1999; Wagenmakers, 2007). Furthermore, this model comparison approach
automatically accounts for model complexity (MacKay, 2002).
In the null model, all probability mass of p(d | D, M0) is concentrated at d = 0, while for the
alternative model we have an eﬀect size distribution p(d | D, M1). Existing regression discontinuity
methods focus on inference of d, and hence implicitly condition on M1.
This approach ignores the
uncertainty in the model posterior p(M | D), which results in an overconﬁdent overestimate of the eﬀect
size, and consequently of too optimistic conclusions of the eﬃcacy of an intervention. This uncertainty
can be accounted for via the Bayesian model average (BMA) estimate of d:
p(d | D) =
X
j=0,1
p(d | D, Mj)p(Mj | D) .
(7)
The resulting distribution integrates out the uncertainty of the model, which has been shown to lead
to optimal predictive performance (Hoeting et al., 1999).
Since the eﬀect size is by deﬁnition zero
according to M0, Eq. (7) is a spike-and-slab distribution that combines a spike at d = 0 with a Gaussian
distribution determined by M1, where each component is weighted by the posterior probability of the
corresponding model. Compared to the overconﬁdent estimation of d conditioned only on M1, this has
a regularizing eﬀect (Brodersen et al., 2015), shrinking small eﬀect size estimates towards zero.
4.1
The continuous model
The continuous (null) model M0 implies that the regression does not depend on the threshold, which
leaves us with a single regression for all data points. We assume Gaussian observation noise:
yi ∼N
 f0(xi), σ2
n

.
Here, σ2
n is the observation noise variance, and f0(xi) captures the relationship between the predictor
and the response. We do not impose a parametric form on f0, and instead assume f0 follows a Gaussian
process (GP) (Rasmussen and Williams, 2005):
f0 | M0 ∼GP (µ(x; θ0), k(x, x′; θ0)) ,
with mean function µ(x; θ0) and covariance function k(x, x′; θ0)). We omit the dependence on the hy-
perparameters θ when confusion is unlikely to arise.
4.2
The discontinuous model
In the alternative model we assume the latent processes before and after x0 are independent. We write
f1 | M1 ∼GP (µ(x; θ1), k1(x, x′; θ1) ,
(8)
where k1(x, x′; θ1) = k(x, x′; θ1) if x and x′ are on the same side of x0, and k1(x, x′; θ1) = 0 otherwise.
As a result, the Gram matrix with elements Kij = k1(xi, xj; θ1) is block-diagonal:
K =
A
0
0
B

,
(9)
with the elements in the matrices A and B corresponding to the covariances between observations at
the same side of the threshold x0.
4.3
Regression discontinuity eﬀect size
Since f1 is continuous everywhere except at x0, we can determine the eﬀect size given M1 by taking the
diﬀerence of its limits as in Eq. (4). The result is a Gaussian distribution:
p(d | D, M1) = N
 m, s2
,
(10)
with m = limx↓x0 f1(x)−limx↑x0 f1(x) and s2 = limx↓x0 V[f1(x)]+limx↑x0 V[f1(x)] = 2σ2
n , for stationary
covariance functions, where σ2
n ∈θ1 represents the observation noise hyperparameter of the discontinuous
model.
4


## Page 5


4.4
Interrupted time series eﬀect size
In contrast to RD design, in ITS the discontinuity may induce a nonstationarity in the latent process,
such as a change in length-scale or frequency. To address this, we allow the hyperparameters pre- and
post-intervention to diﬀer, i.e. Aij = k(xi, xj; θA
1 ) and Bij = k(xi, xj; θB
1 ). The diﬀerences in design
also imply a diﬀerent notion of eﬀect size, which is now a function of x:
p(d(x) | D, M1) = N
 m(x), s2
n

,
(11)
with m(x) = f1
 x; θB
1

−f1
 x; θA
1

and s2
n = (σA
n )2 + (σB
n )2. Note that s2
n does not depend on x.
Of particular interest in ITS are covariance functions that capture long-range correlations, because
these have the potential to extrapolate better and hence provide more accurate eﬀect size estimates.
The spectral mixture kernel was designed for this purpose (Wilson and Adams, 2013). It is deﬁned as a
mixture of Gaussian components in the frequency domain:
S(ω) =
Q
X
q=1
wq
1
σq
√
2π exp
"
−1
2
ω −µq
σq
2#
,
(12)
where µq and σ2
q are the mean and variance of each component, respectively.
This spectral repre-
sentation is then transformed into a regular stationary covariance function using the inverse Fourier
transform (Bochner, 1959), which results in
k(τ) =
Q
X
q=1
wq cos (2πτµq) exp
 −2π2τ 2σ2
q

,
(13)
with τ = |x −x′|. The hyperparameters θ = (Q, µ, σ, w) have the following meaning: Q is the number
of mixture components, µq indicates the mean frequency of component q, the inverse of the variance
1/σq can be interpreted as the length-scale of each component, reﬂecting how quickly that frequency
contribution changes with the input x, and the weights wq determine the relative contribution of each
component (Wilson and Adams, 2013).
4.5
Model training
The marginal likelihood of Gaussian process regression with Gaussian observation noise is available
in closed form (Rasmussen and Williams, 2005), but unfortunately this is not the case for the model
marginal likelihood that integrates over the hyperparameters θ, which is needed to compute the Bayes
factor. We therefore approximate these using the Bayesian Information Criterion (BIC) (Schwarz, 1978),
given by as
log p(D | Mi) ≈log p(y|x, ˆθ, Mi) −l
2 log n ,
(14)
with x = (x1, . . . , xn)T and y = (y1, . . . , yn)T , l the number of hyperparameters, and ˆθ = arg maxθ p(y |
x, θ, M) the optimized hyperparameters, for i ∈{0, 1}.
BNDD is implemented in Python using GPﬂow 2.2 (Matthews et al., 2017). We set the prior function
to the empirical mean. The BMA distribution is approximated via Monte Carlo, and visualized with
kernel density estimation. Code and data are available at Github. More details on the training and
initialization of the spectral mixture covariance function are provided in Appendix A.
5
Covariance functions as design choices
The choice of the Gaussian process covariance functions plays two conceptually distinct roles in BNDD.
First, our choice of covariance function reﬂects our beliefs about the latent process that generated the
observations. In traditional RD designs, one assumes a parametrized model such as (local) linear re-
gression. In BNDD, this explicit parametric form is replaced by a GP prior that assigns a probability
distribution to the space of functions. For instance, we may expect functions to be smooth in x, or
assume functions are a superposition of sine waves (Rasmussen and Williams, 2005; Wilson and Adams,
5


## Page 6


0.0
0.5
Linear
0.0
0.5
Quad
0
1
2
Cubic
0.0
0.5
Lee
0.0
2.5
5.0
CATE1
0.0
2.5
5.0
CATE2
1
2
Ludwig
0.0
0.5
1.0
Curvature
0
20
0
20
40
0
10
0
20
0
25
50
0
20
0
20
40
0
20
40
0
1
2
3
4
d
0.0
0.5
0
1
2
3
4
d
0.00
0.25
0.50
0
1
2
3
4
d
0.00
0.25
0.50
0
1
2
3
4
d
0.00
0.25
0.50
0
1
2
3
4
d
0.00
0.25
0.50
0
1
2
3
4
d
0.00
0.25
0.50
0
1
2
3
4
d
0.0
0.2
0
1
2
3
4
d
0.00
0.25
0.50
All data
Optimized bandwidth
M  / 2-stage GP
1
BMA
Linear
Exponential
Matérn
ExpQuad
Total
Frequentist RDD
Error
log BF
p-value
Figure 1: Simulation results. Top row: the error between the true and estimated eﬀect size. The dashed
line indicates the 2-stage GP approach (see text), which is equivalent to M1. Middle row: The log Bayes
factor. Final row: The p-values obtained by the RDD baseline (black) and the 2-stage approach. The
horizontal dashed lines indicates the common thresholds of |BF| < 3 and p = 0.05.
2013). BNDD can replicate parametrized models by selecting degenerate covariance functions, such as a
linear covariance function.
These modeling choices are crucial in RD design as model misspeciﬁcation can lead to incorrect
inference. When we do not have clear prior beliefs about a covariance function, we may compute the
Bayesian model average (Hoeting et al., 1999) across a set of candidate kernels K:
BFtotal
10
= p(D | M1)
p(D | M0) =
P
k∈K p(D | k)p(k | M1)
P
k∈K p(D | k)p(k | M0) .
(15)
Here, the quantity BFtotal
10
serves as a ﬁnal decision metric to determine an eﬀect in a quasi-experimental
design, while a detailed report is provided by inspecting the Bayes factors corresponding to each consid-
ered covariance function. Similarly, we can compute a marginal eﬀect size across all considered kernels.
In practice, the evidence of one covariance function can dominate all others, in which case the BMA
procedure converges to performing the analysis with the best covariance function only.
The second role of the covariance function choice is that it determines to which types of discontinu-
ities BNDD is sensitive. Importantly, diﬀerent covariance functions can be used to test fundamentally
diﬀerent hypotheses, as they determine which features of the latent function are part of the alleged eﬀect.
For example, the simplest (degenerate) covariance function, the constant function, is sensitive only to
diﬀerences in the means of the two groups (resulting essentially in a quasi-experimental Bayesian t-test),
while the linear covariance function is sensitive to both the diﬀerence in mean as well as in slope. In the
non-degenerate case, the Matérn covariance function with parameter ν = p + 1/2 can detect discontinu-
ities in up to the p-th derivative. It has two interesting special cases: one is the exponential covariance
function (Matérn with p = 1/2), which detects only discontinuities in the function itself (and not in its
derivatives). This is the nonparametric counterpart of traditional linear regression discontinuity. On the
other end is the exponentiated-quadratic covariance function which (Matérn kernel with ν = ∞). This
allows us to detect discontinuities of any order, although the amount of data required to detect such
subtle eﬀects may become prohibitively large.
6
Simulations
We evaluate the performance of BNDD using simulations, using the functions discussed by Imbens and
Kalyanaraman (2012), which consist of diﬀerent polynomials up to order 5. We apply BNDD using
linear, exponential, Matérn (ν = 3/2) and exponentiated-quadratic covariance functions, as well as the
model average of this set. We compare the performance of BNDD with two baselines. The ﬁrst is the
6


## Page 7


−1.0
−0.5
0.0
0.5
1.0
x
−2
−1
0
1
2
y
log S(ω)
10
20
30
ω
Observations
f0(x)
f
(x), x < x0
f
(x), x ≥x0
f B(x), x ≥x0
A
α=0
α=1
α=2
Density
α=3
α=4
α=5
0.0
0.5
1.0
RMSE
α=6
0.0
0.5
1.0
RMSE
α=7
0.0
0.5
1.0
RMSE
α=8
C
B
ARMA
r
GPR r
1
1
A
A
1
Figure 2: A. ITS application. Model ﬁt and extrapolation of M0 and M1. The data were generated
with a post-intervention frequency shift of α = 4. We ﬁnd log BF = 0.15. The shaded interval represents
two standard deviations around the mean. B. Estimated power spectra. The colors of the power density
spectrum correspond to the legend of the regression. C. The RMSE between the estimated and true
dITS using posterior samples of BNDD and an ARMA baseline (dashed line).
Python RDD package, which uses linear regression together with the bandwidth selection method by
Imbens and Kalyanaraman (2012) to select only a subset of the data around x0 to perform the analysis
on. The second is the approach by Branson et al. (2019), which ﬁrst estimates the conditional eﬀect size
distribution p(d | M1, D) and then tests the null hypothesis d = 0 using this distribution. We refer to
this approach as the 2-stage GP. Simulation details and visual examples are provided in Appendix B.
Figure 1 shows the absolute diﬀerence between the true eﬀect size and the posterior expectations, as
well as the decision metrics (averaged over 100 runs). The discontinuous model overestimates d when the
true eﬀect size is small, as is to be expected from the implicit conditioning on an eﬀect. The BMA does
not have this bias, resulting in lower errors for small and absent eﬀects. For medium eﬀects, this itself can
result in a bias due to shrinkage (e.g. the Cubic function), while for large eﬀects the BMA converges to
M1 and the bias disappears. Generally, BNDD performs on par with the optimized-bandwidth baseline,
with worse performance for the Ludwig function, and better for e.g. Curvature, as well as for most cases
with an absent or small eﬀect.
The decision metrics show that for small or absent eﬀects, BNDD can report evidence in favor of the
null, while the corresponding p-values are inconclusive. The methods positively identify eﬀects at roughly
the same true eﬀect sizes. An interesting special case is observed for the Lee and Ludwig functions, which
both feature a discontinuity in their derivative (Branson et al., 2019), which is correctly picked up by
BNDD even when the magnitude of the eﬀect is small, conﬁrming the ability to detect discontinuities of
higher orders.
We explore the ITS application of BNDD in another simulation. Here, we generate oscillating data
where for x ≥x0 a frequency shift is introduced. We compare our extrapolations based on the spectral
mixture covariance function with an ARMA model, which is commonly used in ITS designs (Jandoc
et al., 2015; Prado and West, 2010). Details of the simulation procedure are provided in Appendix B. An
example simulation run and BNDD application is shown in Fig. 2A, with a post-intervention frequency
shift of α = 4Hz.
The model correctly recovers the true power spectrum, as well as the decreased
amplitude of the second harmonic component post-intervention, and ﬁnds barely worth mentioning
evidence in favor of an eﬀect (log BF = 0.15). The estimated spectral mixture of the continuous model
is centered between the true frequencies of the control and intervention group (Fig. 2B). This faithfully
represents the null hypothesis that the observations can be explained without any changes in spectral
content. As the discontinuity grows larger, the standard deviation of the components of the continuous
model increases as well, since it has to account for a larger diﬀerence. M1 instead correctly identiﬁes
the true mixture components. Fig. 2C shows the RMSE of samples from the posterior distributions of
f1 and the true function, as well as the ARMA estimate. BNDD consistently outperforms the baseline.
7
Applications
7.1
The eﬀects of winning an election and longevity
Barfort et al. (2021) investigated the eﬀect of running for US gubernatorial oﬃce on longevity. The
authors use a regression discontinuity design, and conclude that politicians winning a close election live
5 to 10 years longer than if they had lost. These ﬁndings have been heavily criticized (Gelman, 2020),
7


## Page 8


−10
−5
0
5
10
Win/loss vote diff. (percentile pts)
0
20
40
60
Years alive
post election
Mat´ern (ν = 3/2)
M0
M1
−10
−5
0
5
10
Linear RD with opt. bw. = 5.48
Win/loss vote diff. (percentile pts)
Figure 3: Discontinuity analysis of the eﬀect of close gubernatorial elections on longevity (Barfort et al.,
2021). Shown are regressions by BNDD using a Matérn covariance function, and a linear RD baseline
with an optimized bandwidth of 5.48 percentile points (shaded area). For BNDD, the regressions for
M0 and M1 are nearly identical. For the baseline, the bandwidth optimization leads to a poor linear
ﬁt, and hence a spurious detection of an eﬀect.
Continuous
Discontinuous
Phantom border (west-east)
-0.05
0.00
0.05
0.10
Effect size
Linear
Matérn
No effect
Effect size along border
Continuous
Discontinuous
0.1
0.2
0.3
0.4
0.5
0.6
Populist vote fraction
Linear
Matérn
Figure 4: Discontinuity analysis along a two-dimensional boundary (indicated by the dashed line). A.
Circles indicate the observed fraction of populist votes; municipalities are shaded according to the Gaus-
sian process predictions. B. The distribution of eﬀect size conditioned on M1, p(d | D, M1), along the
phantom border. The shaded interval indicates one standard deviation around the mean.
and it is unclear whether a regression discontinuity analysis is actually appropriate here, as there is
no clear intervention at x = 0 (where x is the percentile diﬀerence in election result). Despite these
concerns, we analyze this data set here as it allows us to demonstrate some of the functionality speciﬁc
to BNDD. The data are available from the original publication (Barfort et al., 2021), and preprocessed
following Gelman (2020).
Using the linear RDD baseline we ﬁnd an optimal bandwidth of 5.48 percentile points using the
Imbens-Kalyanaraman procedure (Imbens and Kalyanaraman, 2012). When using this bandwidth and
testing for an eﬀect, we ﬁnd p = 0.019 and an estimated eﬀect size of 9.4 years. With BNDD, using either
a linear, exponential, or Matérn (ν = 3/2) covariance function, we ﬁnd a more parsimonious explanation
of these data by a constant function and a substantial noise term σ2
n, as shown by log Bayes factors of
-0.12, 0.0, and 0.0, respectively. This indicates that from these data, no clear conclusion can be drawn,
and that such a scenario is clearly identiﬁed using BNDD.
7.2
Phantom border eﬀect on Dutch government elections
In 2017, the Dutch general elections were held (Kennis- en Exploitatiecentrum Oﬃciële Overheidspub-
licaties (KOOP), 2018). According to Dutch electorate geographer De Voogd, the share of votes that
go to populist parties1 is diﬀerent north and south of a so-called ‘phantom border’, a line that histori-
1We refrain from an extensive discussion of the deﬁnition of populism and refer to populist parties as those parties that
emphasize ‘an alleged chasm between the elite and the general population’. In the Dutch 2017 elections, parties that ﬁt
this description were PVV, SP, 50Plus and FvD (Müller, 2016).
8


## Page 9


-00:10
-00:07
-00:03
00:00
00:03
00:07
00:10
Time (h)
50
60
70
80
90
Heart rate (bpm)
log S(ω)
0.0
0.5
1.0
1.5
ω
Data
f0(x)
f A
1 (x)
f B
1 (x)
Figure 5: Analysis of meditation eﬀect on heart rate. Shown is the participant’s heart rate, who starts
meditation at x0 = 00 : 00. The extrapolation, indicated by the dashed (mean) and dotted (posterior
samples) red lines, is poor in comparison to the actual observations, which is corroborated by the large
log Bayes factor. The panel on the right shows the (log) power spectra expressed by the optimized
covariance function hyperparameters.
cally divided the catholic south of the Netherlands from the protestant north (De Voogd, 2016, 2017).
This border serves as a two-dimensional threshold along which one can apply RD design. This special
case of RD design where the assignment threshold is a geographical boundary is also referred to as
GeoRDD (Rischard et al., 2021). Here, we test the hypothesis by De Voogd.
We apply BNDD using the linear and ﬁrst-order Matérn covariance functions. The results of the
analysis are shown in Fig. 4. The ﬁgure shows the Netherlands with the fraction of populist votes per
municipality superimposed, together with the phantom border representing the supposed divide in voting
behaviour.
If we assume a linear underlying process, there is strong evidence for a discontinuity (log BF =
24.4), conﬁrming the hypothesis by De Voogd.
Visually however, the data do not appear to follow
these linear trends. The nonparametric Matérn covariance function results in evidence against an eﬀect
(log BF = −3.5). As the Matérn covariance function ﬁts the data much more accurately than the linear
covariance function, the Bayesian model average is completely dominated by the former, leading to the
conclusion that the historical phantom border does not create a geographic discontinuity in populist
voting behaviour.
7.3
Kundalini meditation eﬀect on heart rate
Peng et al. (1999) studied the hypothesis that Kundalini Yoga meditation techniques reduce one’s heart
rate. However, they ﬁnd the opposite; the meditation instead brings about an increase in heart rate.
The experiment lends itself well for ITS design, but in practice may be diﬃcult to perform because the
data are not evenly sampled. However, this is not a prerequisite for Gaussian process regression, which
together with the spectral mixture kernel (Wilson and Adams, 2013) is well-suited to model these data.
The observations are obtained from the PhysioNet database and consists of heart rates of two women
and two men, of ages 20–52 (mean 33) (Goldberger et al., 2000). We focus on one participant due to
space constraints. Since we do not merely want to detect a change in absolute heart rate, but in its
ﬂuctuations, use a changepoint mean function (Saatçi et al., 2010) for M0 and two separate constant
mean functions for M1 to capture the diﬀerent means. Figure 5 shows the corresponding regression and
extrapolation. The continuous model requires more spectral mixture components; Q = 6 for f0 compared
to Q = 2 for f
 x; θA
1

and Q = 3 for f
 x; θB
1

. The analysis ﬁnds overwhelming evidence for an eﬀect
(log BF = 281.2).
8
Discussion
BNDD extends naturally to the setting of multiple assignment variables(Choi and Lee, 2017, 2018; Papay
et al., 2011; Reardon and Robinson, 2012; Wong et al., 2013). A special case of such multivariate QED
9


## Page 10


is GeoRDD, in which the two-dimensional assignment variable represents a spatial location (Keele et al.,
2017; Keele and Titiunik, 2015; Rischard et al., 2021).
Our approach does not assume a univariate
threshold to determine the assignment to intervention and control group, and can work on arbitrary
complex label functions. This can be a geographical border, but also more complex shapes such as, for
example, one region versus the rest of a country, or a particular regime of diagnostic variables.
In order to infer causality from QED, one assumes that the alleged change occurs at the threshold, but
that the latent process is otherwise stationary. Consequently, the behaviour of the two groups changes
sharply around the intervention. In standard RD studies, this locality is controlled via a bandwidth
parameter that determines the sensitivity of the detection approach (Bloom, 2012). This requires the
availability of suﬃcient data around the threshold, and the analysis is sensitive to this parameter. In
BNDD with stationary nonparametric covariance functions, the bandwidth is replaced by a length-scale
hyperparameter, which we optimize using the model marginal likelihood. The length-scale regulates how
fast the correlations between consecutive points decay with their distance, and thus how sensitive BNDD
is around the threshold (Duvenaud, 2014). This implements a trade-oﬀbetween estimation reliability and
the locality assumption that is needed to draw causal inferences (Geneletti et al., 2015). The beneﬁt of a
length-scale instead of a ﬁxed bandwidth parameter is that the relative inﬂuence of observations decreases
gradually as they are further away from the intervention point, and that this distance is automatically
adjusted.
With an exponential covariance function the most rigorous form of locality can be enforced. Here,
the Markov properties of the Gaussian process guarantee that only discontinuities at the intervention
threshold are detectable. On the other hand, non-local covariance functions such as the periodic covari-
ance function are vulnerable to false positives if the true process is non-stationary. Here, the presence of
change points away from the intervention threshold can lead to false alarms, due to the ﬂexibility of the
regressions. In this case, or in exploratory applications, BNDD can be performed in a sliding-window
fashion to ensure that the highest Bayes factor is at the intervention threshold.
BNDD can be extended in several ways. For instance, we do not currently account for covariates
that may serve as confounds for causal inference (Brodersen et al., 2015; Harris et al., 2004). However,
such covariates can be explicitly taken into account in the regression models, or even be learned from the
observations (Kocaoglu et al., 2017). Covariate selection can be performed using automatic relevance
determination (Wipf and Nagarajan, 2008), where we learn separate length-scales for each covariate.
Furthermore, improvement is expected from more accurate estimators of the model marginal likelihood
than the BIC, such as the ELBO or bridge sampling (Fourment et al., 2020).
In all, BNDD serves as a Bayesian nonparametric approach for causal inference in quasi-experimental
designs.
By selecting the appropriate covariance function, one has precise control over the type of
discontinuity that can be detected, as well as a priori assumptions of the latent data generating processes.
References
S Barfort, R Klemmensen, and E G Larsen.
Longevity returns to political oﬃce.
Political Science
Research and Methods, 9:658–664, 2021. doi: 10.1017/psrm.2019.63.
J L Bernal, S Cummins, and A Gasparrini. Interrupted time series regression for the evaluation of public
health interventions: A tutorial. International Journal of Epidemiology, 46(1):348–355, 2017.
H S Bloom. Modern regression discontinuity analysis. Journal of Research on Educational Eﬀectiveness,
5(1):43–82, 2012.
S Bochner. Lectures on Fourier integrals, volume 42. Princeton University Press, 1959.
Z Branson, M Rischard, L Bornn, and L W Miratrix.
A nonparametric Bayesian methodology for
regression discontinuity designs. Journal of Statistical Planning and Inference, 202:14–30, 2019.
K H Brodersen, F Gallusser, J Koehler, N Remy, and S L Scott. Inferring causal impact using Bayesian
structural time-series models. Annals of Applied Statistics, 9(1):247–274, 2015.
D T Campbell and J C Stanley. Experimental and Quasi-Experimental Designs for Research. Rand
McNally College Publishing, 1963.
10


## Page 11


J-Y Choi and M-J Lee. Regression discontinuity: review with extensions.
Statistical Papers, 58(4):
1217–1246, 2017.
J-Y Choi and M-J Lee. Regression discontinuity with multiple running variables allowing partial eﬀects.
Political Analysis, 26(3):258––274, 2018.
J
De
Voogd.
Van
Volendam
tot
Vinkeveen:
de
electorale
geograﬁe
van
de
PVV,
December
22nd
2016.
http://www.socialevraagstukken.nl/
volendam-tot-vinkeveen-de-electorale-geografie-van-de-pvv/ (visited: 21-09-2019).
J De Voogd. Deze eeuwenoude grenzen kleuren de verkiezingen nog altijd, March 1st 2017. https://
decorrespondent.nl/6298/deze-eeuwenoude-grenzen-kleuren-de-verkiezingen-nog-altijd/
(visited: 21-09-2019).
D Duvenaud. Automatic model construction with Gaussian processes. PhD thesis, Computational and
biological learning laboratory, University of Cambridge, 2014.
M Fourment, A F Magee, C Whidden, A Bilge, F A Matsen, and V N Minin. 19 dubious ways to compute
the marginal likelihood of a phylogenetic tree topology. Systematic Biology, 69(2):209–220, 2020.
A Freni-Sterrantino, R E Ghosh, D Fecht, M B Toledano, P Elliott, A L Hansell, and M Blangiardo.
Bayesian spatial modelling for quasi-experimental designs: An interrupted time series study of the
opening of municipal waste incinerators in relation to infant mortality and sex ratio. Environment
International, 128(November 2018):109–115, 2019.
A
Gelman.
No,
I
don’t
believe
that
claim
based
on
regression
discontinu-
ity
analysis
that. . . .
https://statmodeling.stat.columbia.edu/2020/07/02/
no-i-dont-believe-that-claim-based-on-regression-discontinuity-analysis-that/, 2020.
[Online; accessed 19-January-2021].
S Geneletti, A G O’Keeﬀe, L D Sharples, S Richardson, and G Baio. Bayesian regression discontinuity
designs: Incorporating clinical knowledge in the causal analysis of primary care data. Statistics in
Medicine, 34:2334–2352, 2015.
A Goldberger, L Amaral, L Glass, J Hausdorﬀ, P C Ivanov, R Mark, and H E Stanley. Physiobank,
physiotoolkit, and physionet: Components of a new research resource for complex physiologic signals.
Circulation [Online], 101(23):e215–e220, 2000.
S N Goodman. Toward evidence-based medical statistics. 1: The p-value fallacy. Annals of Internal
Medicine, 130(12):995–1004, 06 1999.
B Y J Hahn, P Todd, and W van der Klaauw. Identiﬁcation and estimation of treatment eﬀects with a
regression-discontinuity design. Econometrica, 69(1):201–209, 2001.
A D Harris, D D Bradham, M Baumgarten, I H Zuckerman, J C Fink, and E N Perencevich. The use
and interpretation of quasi-experimental studies in infectious diseases. Antimicrobial resistance, 38:
1586–1591, 2004.
A B Hill. The clinical trial. N Engl J Med, 247:113–119, 1952.
J A Hoeting, D Madigan, A E Raftery, and C T Volinsky.
Bayesian model averaging: A tutorial.
Statistical Science, 14(4):382–401, 1999.
G Imbens and K Kalyanaraman. Optimal bandwidth choice for the regression discontinuity estimator.
Review of Economic Studies, 79(3):933–959, 2012.
G W Imbens and T Lemieux. Regression discontinuity designs: A guide to practice. Journal of Econo-
metrics, 142(2):615–635, 2008.
G W Imbens and D B Rubin. Causal Inference in Statistics, Social, and Biomedical Sciences. Causal
Inference for Statistics, Social, and Biomedical Sciences: An Introduction. Cambridge University Press,
2015.
11


## Page 12


R Jandoc, A M Burden, M Mamdani, E L Linda, and S M Cadarette. Interrupted time series analysis
in drug utilization research is increasing: systematic review and recommendations. Journal of Clinical
Epidemiology, 68:950–956, 2015.
A F Jarosz and J Wiley. What are the odds? A practical guide to computing and reporting Bayes
factors. Journal of Problem Solving, 7:2–9, 2014.
R E Kass and A E Raftery. Bayes factors. Journal of the American Statistical Association, 90(430):
773–795, 1995.
L Keele, S Lorch, M Passarella, D Small, and R Titiunik. An overview of geographically discontinuous
treatment assignments with an application to children’s health insurance, chapter 4, pages 147–194.
Emerald Publishing Limited, 2017.
L J Keele and R Titiunik. Geographic boundaries as regression discontinuities. Political Analysis, 23(1):
127–155, 2015.
Kennis- en Exploitatiecentrum Oﬃciële Overheidspublicaties (KOOP). Verkiezingsuitslag Tweede Kamer
2017.
https://data.overheid.nl/data/dataset/verkiezingsuitslag-tweede-kamer-2017/,
2018.
Y Kim and P Steiner. Quasi-experimental designs for causal inference. Educational Psychologist, 51
(3-4):395–405, 2016.
M Kocaoglu, K Shanmugam, and E Bareinboim. Experimental design for learning causal graphs with
latent variables. In I Guyon, U V Luxburg, S Bengio, H Wallach, R Fergus, S Vishwanathan, and
R Garnett, editors, Advances in Neural Information Processing Systems (NeurIPS) 30, pages 7018–
7028. Curran Associates, Inc., 2017.
S L Lauritzen. Causal inference from graphical models. Complex stochastic systems, pages 63–107, 2001.
D S Lee and T Lemieux. Regression discontinuity designs in econometrics. Journal of Economic Litera-
ture, 48(June):281–355, 2010.
T Li, L Ungar, and K Kording. Quantifying causality in data science with quasi-experiments. Nature
Computational Science, 1:24–32, 2021.
D J C MacKay. Information Theory, Inference & Learning Algorithms. Cambridge University Press,
USA, 2002.
I E Marinescu, P N Lawlor, and K P Kording. Quasi-experimental causality in neuroscience and be-
havioural research. Nature Human Behaviour, pages 1–11, 2018.
A G Matthews, M van der Wilk, T Nickson, K. Fujii, A Boukouvalas, P León-Villagrá, Z Ghahramani,
and J Hensman. GPﬂow: A Gaussian process library using TensorFlow. Journal of Machine Learning
Research, 18(40):1–6, apr 2017.
D McDowall, R McCleary, E Meidinger, and R Hay. Interrupted time series analysis. Sage Publications
Inc., Thousand Oaks, CA, USA, 1980.
E Moscoe, J Bor, and T Bärnighausen. Regression discontinuity designs are underutilized in medicine,
epidemiology, and public health: A review of current and best practice. Journal of Clinical Epidemi-
ology, 68(2):132–143, 2015.
J-W Müller. What is populism? University Of Pennsylvania Press, Philadelphia, PA, U.S.A., 2016.
A G O’Keeﬀe and G Baio. Approaches to the estimation of the local average treatment eﬀect in a
regression discontinuity design. Scandinavian Journal of Statistics, 43(4):978–995, 2016.
J P Papay, J B Willett, and R J Murnane. Extending the regression-discontinuity approach to multiple
assignment variables. Journal of Econometrics, 161(2):203–207, 2011.
J Pearl. Causal inference in statistics: An overview. Statistics Surveys, 3:96–146, 2009.
12


## Page 13


C Peng, Joseph E Mietus, Yanhui Liu, Gurucharan Khalsa, Pamela S Douglas, Herbert Benson, and
Ary L Goldberger. Exaggerated heart rate oscillations during two meditation techniques. International
Journal of Cardiology, 70:101–107, 1999.
R Prado and M West. Time Series: Modeling, Computation, and Inference. Chapman &Hall/CRC, 1st
edition, 2010.
C E Rasmussen and C K I Williams. Gaussian processes for machine learning. The MIT Press, 2005.
S F Reardon and J P Robinson. Regression discontinuity designs with multiple rating-score variables.
Journal of Research on Educational Eﬀectiveness, 5(1):83–104, 2012.
M Rischard, Z Branson, L Miratrix, and L Bornn. Do school districts aﬀect NYC house prices? Identify-
ing border diﬀerences using a Bayesian nonparametric approach to geographic regression discontinuity
designs. Journal of the American Statistical Association, 116(534):619–631, 2021.
D B Rubin. Estimating causal eﬀects of treatments in randomized and nonrandomized studies. Journal
of Educational Psychology, 66(5):688–701, 1974.
Y Saatçi, R Turner, and C E Rasmussen. Gaussian process change point models. In Proceedings of
the 27th International Conference on International Conference on Machine Learning, ICML’10, page
927–934, Madison, WI, USA, 2010. Omnipress.
G Schwarz. Estimating the dimension of a model. The Annals of Statistics, 6:461–464, 1978.
W R Shadish, Thomas D Cook, and D T Campbell. Experimental and quasi-experimental designs for
generalized causal inference. Cencage Learning, Inc., 2nd edition, 2002.
D L Thistlethwaite and Campbell D T. Regression-discontinuity analysis: an alternative to the ex-post
facto experiment. Journal of Educational Psychology, 51:309–317, 1960.
J T Vanderplas. Understanding the Lomb–Scargle periodogram. The Astrophysical Journal Supplement
Series, 236(1):16, 2018.
E-J Wagenmakers. A practical solution to the pervasive problems of p-values. Psychonomic Bulletin &
Review, 14(5):779–804, 2007.
A Wilson and R Adams. Gaussian process kernels for pattern discovery and extrapolation. In Interna-
tional conference on machine learning, pages 1067–1075, 2013.
D P Wipf and S S Nagarajan. A new view of automatic relevance determination. In J C Platt, D Koller,
Y Singer, and S T Roweis, editors, Advances in Neural Information Processing Systems 20, volume 20,
pages 1625–1632. Curran Associates, Inc., 2008.
V C Wong, P M Steiner, and T D. Cook.
Analyzing regression-discontinuity designs with multiple
assignment variables: A comparative study of four estimation methods. Journal of Educational and
Behavioral Statistics, 38(2):107–141, 2013.
A
Training the spectral mixture kernel
The number of mixture components Q in the spectral mixture kernel of our ITS approach is optimized
in the same way as other covariance function parameters are optimized, that is, by optimizing the GP
marginal likelihood. The covariance function mixture parameters are initialized by ﬁtting a Gaussian
mixture model to the empirical spectral using the Lomb-Scargle periodogram, which is applicable for
detecting spectral features in (potentially) unevenly sampled data (Vanderplas, 2018).
13


## Page 14


0
5
Linear
0
5
Quad
−5
0
5
Cubic
0
5
Lee
−20
0
CATE1
−20
0
CATE2
0
10
Ludwig
−5
0
5
Curvature
0
5
0
5
−5
0
5
0
5
−20
0
−20
0
0
10
−5
0
5
−1
0
1
x
0
5
−1
0
1
x
0
5
−1
0
1
x
−5
0
5
−1
0
1
x
0
5
−1
0
1
x
−20
0
−1
0
1
x
−20
0
−1
0
1
x
0
10
−1
0
1
x
−5
0
5
Linear
Exponential
Matérn
Exp. Quadratic
BMA
d=0.0
d=2.0
d=4.0
Figure 6: Example of one simulation run for eﬀect sizes d ∈{0.25, 1.0, 4.0} and σ = 1.0. The covariance
functions used here are linear, exponential, Matérn (ν = 3/2) and exponentiated-quadratic. The vertical
bars indicate the estimated eﬀect sizes by the discontinuous models for the diﬀerent covariance functions.
As the ﬁgure shows, the linear covariance function tends to have the strongest bias, in particular in the
low signal-to-noise regime.
B
Simulations
B.1
RD simulations
Figure 6 shows an example run of BNDD on the functions considered in our simulation. Here, the diﬀerent
functions are shown, as well as the regressions by both the continuous and discontinuous models, for
each of the four considered covariance functions. The vertical bars in the ﬁgure show the expectation of
the estimated eﬀect size p(d | D, M1). These functions used are provided in Imbens and Kalyanaraman
(2012), and are complemented by a simple linear function to see the behaviour when the linearity
assumption by the baseline is actually correct. The function deﬁnitions are given by
f(x) = 0.23 + 0.89x
Linear
f(x) =
(
3x2
if x < x0,
4x2
otherwise.
Quad
f(x) =
(
3x3
if x < x0,
4x3
otherwise.
Cubic
f(x) =
(
0.48 + 1.27x + 7.18x2 + 20.21x3 + 21.54x4 + 7.33x5
if x < x0,
0.48 + 0.84x −3.0x2 + 7.99x3 −9.01x4 + 3.56x5
otherwise.
Lee
f(x) = 0.42 + 0.84x −3.0x2 + 7.99x3 −9.01x4 + 3.56x5
CATE1
f(x) = 0.42 + 0.84x + 7.99x3 −9.01x4 + 3.56x5
CATE2
f(x) =
(
3.71 + 2.3x + 3.28x2 + 1.45x3 + 0.23x4 + 0.03x5
if x < x0,
3.71 + 18.49x −54.81x2 + 74.3x3 −45.02x4 + 9.83x5
otherwise.
Ludwig
f(x) =
(
0.48 + 1.27x −3.44x2 + 14.147x3 + 23.694x4 + 10.995x5
if x < x0,
0.48 + 0.84x −0.3x2 −2.397x3 −0, 901x4 + 3.56x5
otherwise.Curvature
For each latent function f, we generate n = 100 observations (xi, yi) according to the following
14


## Page 15


procedure:
xi ∼U(−1, 1)
yi | xi, σ, d, f ∼N
 f(xi) + d[xi ≥x0], σ2
,
where the threshold x0 = 0. We ﬁx σ = 1.0 and vary d ∈{0, 0.5, . . . , 4.0}, eﬀectively providing a range
of diﬀerent signal-to-noise regimes. Next, we subject the simulated data to analysis by BNDD, using
a ﬁrst-order polynomial, an exponential, a Matérn (ν = 3/2) and a exponentiated-quadratic covariance
function. For each covariance function, we compute the Bayes factor for the presence of a discontinuity,
and we estimate the marginal eﬀect size (Eq. (7) in the main text).
We also compute p-values and conditional eﬀect size estimates for the RDD baseline using the Imbens-
Kalyanaraman bandwidth optimization method, and for the two-step GP method (Branson et al., 2019).
The latter corresponds to ﬁtting a GP regression pre- and post-intervention, computing the implied
eﬀect size distribution at x = x0, and then testing whether d = 0 is in this distribution. Note that
this distribution is the same as our conditional eﬀect size distribution in Eq. (4), but the subsequent
testing procedure is diﬀerent; a frequentist signiﬁcance test is performed rather than Bayesian model
comparison.
For each of the three methods, we compute the absolute error between the estimated and true eﬀect
size, and use this to quantify the estimation performance. In addition, we show the decision metrics for
each method, so that the diﬀerences between a Bayesian and frequentist approach can be seen.
As these and the aggregated results (see main text) show, the linear covariance function results in
the largest bias in the eﬀect size estimate, which is unsurprising given its strong assumptions that do
not match the data generating process here.
B.2
ITS simulations
The latent function for the ITS simulation is given by
f(x) =
(
sin(12x) + 2
3 cos(25x)
for x < x0 and
sin((12 + α)x) + 2
3 cos((25 + α)x)
for x ≥x0,
with x0 = 0, and where α indicates the shift in frequency (set to α = 4 in the example ﬁgure in the main
text). We vary α across the range [0, . . . , 8] Hz. For observation noise, we once more assume
y ∼N(f(x), σ2) ,
and σ2 = 0.2. For each value of α, we generate 20 datasets containing n = 200 evenly spaced observations.
As a baseline for comparison of our approach we use an ARMA model (Prado and West, 2010). The
parameters of the ARMA model are determined using a grid search and its BIC score. We then compare
the root-mean-squared-error between samples from the predictive distribution obtained by BNDD and
the true post-intervention signal, and similarly evaluate the performance of the ARMA extrapolations
and the true signal. The results are shown in Fig. 2 in the main text, and demonstrate that the spectral
mixture kernel-based ITS approach consistently outperforms the baseline.
15

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1912.05595v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1912.05595v1_A_state-space_model_for_dynamic_functional_connectivity

> Source: 1912.05595v1_A_state-space_model_for_dynamic_functional_connectivity.pdf

> Pages: 5

---


## Page 1


A state-space model for dynamic functional connectivity
Sourish Chakravarty1,5,6, Zachary D. Threlkeld7, Yelena G. Bodien6, Brian L. Edlow6, Emery N. Brown1−5
Abstract— Dynamic functional connectivity (DFC) analysis
involves measuring correlated neural activity over time across
multiple brain regions. Signiﬁcant regional correlations among
neural signals, such as those obtained from resting-state func-
tional magnetic resonance imaging (fMRI), may represent
neural circuits associated with rest. The conventional approach
of estimating the correlation dynamics as a sequence of static
correlations from sliding time-windows has statistical limita-
tions. To address this issue, we propose a multivariate stochastic
volatility model for estimating DFC inspired by recent work
in econometrics research. This model assumes a state-space
framework where the correlation dynamics of a multivariate
normal observation sequence is governed by a positive-deﬁnite
matrix-variate latent process. Using this statistical model within
a sequential Bayesian estimation framework, we use blood
oxygenation level dependent activity from multiple brain re-
gions to estimate posterior distributions on the correlation
trajectory. We demonstrate the utility of this DFC estimation
framework by analyzing its performance on simulated data,
and by estimating correlation dynamics in resting state fMRI
data from a patient with a disorder of consciousness (DoC).
Our work advances the state-of-the-art in DFC analysis and its
principled use in DoC biomarker exploration.
I. INTRODUCTION
Functional connectivity (FC) analysis can be broadly de-
scribed as an analysis of “statistical dependencies among
remote neuro-physiological events” [Fri11]. The FC mea-
sures are considered to be representative of long-range neural
coordination across brain-regions. Conventionally, they are
calculated as pair-wise correlation in neural signals, e.g.
This work was partially supported by NIH Award P01-GM118629 (to
E.N.B), by funds from Massachusetts General Hospital (to E.N.B.), by funds
from the Picower Institute for Learning and Memory (to E.N.B. and S.C.),
by funds from the NIH/NINDS (DP2-HD101400, R21-NS109627, RF1-
NS115268, K23-NS094538; to B.L.E.), by funds from James S. McDonnell
Foundation (to B.L.E.), and by funds from the National Institute on
Disability, Independent Living and Rehabilitation Research, Administration
for Community Living (90DP0039, Spaulding- Harvard TBI Model System;
to Y.G.B.).
1Picower Institute for Learning and Memory, Massachusetts Institute of
Technology (MIT), Cambridge, MA
2Department of Brain and Cognitive Sciences, MIT, Cambridge, MA
3Institute of Medical Engineering and Science, MIT, Cambridge, MA
4 Harvard-MIT Division of Health Science and Technology
5 Department of Anesthesia, Critical Care and Pain Medicine, Mas-
sachusetts General Hospital (MGH), Boston, MA
6 Center for Neurotechnology and Neurorecovery, Department of Neu-
rology, MGH, Boston, MA
7 Dept. of Neurology and Neurological Sciences, Stanford University
School of Medicine, Stanford, CA
Accepted in 53rd Annual Asilomar Conference on Signals, Systems, and
Computers, Paciﬁc Grove, CA. c⃝2019 IEEE. Personal use of this material
is permitted. Permission from IEEE must be obtained for all other uses, in
any current or future media, including reprinting/republishing this material
for advertising or promotional purposes, creating new collective works,
for resale or redistribution to servers or lists, or reuse of any copyrighted
component of this work in other works.
blood oxygen level dependent (BOLD) activation in func-
tional magnetic resonance imaging (fMRI) data and or elec-
trical activity in electroencephalography (EEG) data, across
multiple brain regions. From a signal processing perspective,
FC analysis is based upon estimation of correlation matrices
from multivariate time-series data. FC analysis is widely rel-
evant in basic neuroscience [AM14] as well as translational
clinical neuroscience research ([BCE17], [ECS+17]).
An emerging paradigm in FC research is that of dynamic
functional connectivity (DFC) [TL15]. Conventionally, FC
analysis is performed on an entire session of multi-site/multi-
channel neural recordings to generate a correlation map.
A key assumption of such an analysis is that the true
correlation remains constant across the entire sequence of
a recording session. This static FC (SFC) interpretation can
be generalized to DFC by assuming that the true correlation
map changes over time. Therefore, DFC analysis involves
estimating a time-series of pairwise correlations from mul-
tivariate neural data. The DFC analysis yields information
that is complementary to SFC analysis of the same dataset:
SFC indicates the degree to which any two brain-regions
are synchronous with each other on average, whereas DFC
indicates how this degree of synchrony varies over time.
Principled DFC analysis may aid translational research aimed
at biomarker discovery for neurological disorders such as
disorders of consciousness (DoC) [DTD+19].
Conventionally, DFC analysis generates dynamic estimates
of correlations by assuming a sliding-window (SW) ap-
proach. In this approach, a sequence of instantaneous corre-
lation measures is calculated by repeating the SFC analyses
on a sequence of short data windows where the window-size
is user-prescribed. A sub-optimal choice of window-size can
lead to statistical challenges. For example, if the window size
is too long, then the estimated correlation trajectory may be
unable to capture faster dynamics. Conversely, if window size
is too short then the estimates will be more sensitive to noise
in the data. Therefore, it is preferable to use alternative DFC
estimation techniques that can yield reliable estimates of cor-
relation dynamics without requiring subjective windows. One
such promising alternative has been proposed by Lindquist
et al.[LXNC14] where the authors estimated correlation
dynamics by ﬁtting a dynamic conditional correlation model
(DCC) to resting-state fMRI data. The DCC model originated
in econometrics literature to estimate covariance trajectories
in multivariate ﬁnancial time-series data [ES01]. Motivated
by this work, here we propose a novel approach based on
state-space models (SSMs) to estimate DFC from neural data
while avoiding data-windowing. In particular, we consider
a speciﬁc class of SSMs known as Multivariate Stochastic
arXiv:1912.05595v1  [stat.AP]  11 Dec 2019


## Page 2


Volatility (MVSV) models that also originated in economet-
rics research [CST18]. Such an MVSV model incorporates
a matrix-variate latent state process to describe correlation
dynamics in the observed neural signals. DFC statistics may
then be derived by estimating the latent states and model
parameters from the data. This SSM framework provides
more ﬂexibility in describing complex correlation dynamics
[CG16], and in estimating instantaneous correlations even
under scenarios of missing data and non-uniform sampling
time-intervals of observations [SS82].
In Sec. II, we present our SSM, which is a modiﬁed
version of the existing MVSV model [CST18], for estimat-
ing correlation dynamics in multivariate noisy neural data.
Speciﬁcally, we do not consider certain modeling features of
[CST18] such as a ﬁrst-order vector autoregressive process
to track the mean of observations, and additional latent states
to track both gradual changes in channel-wise variance and
temporally sharp regime transitions in mean and covari-
ance dynamics of the signals. Except for minor differences
in notational conventions and a major difference in the
proposal distributions in Secs.II-F and II-G, the statistical
model and estimation procedure used here are identical to
[CST18] conditioned on the assumptions made in this work.
In Sec. III, we numerically verify our model on synthetic
data and demonstrate its utility in estimating time-varying
correlations from BOLD-fMRI data from a DoC patient.
Finally, in Sec. IV, we summarize the current work, and
discuss potential next steps.
II. THEORY
A. State-Space Model (SSM)
Consider a sequence of multivariate neural data {yk}K
k=1.
At the k-th instant, the observation vector, yk ∈Rm, is as-
sumed to be a realization of a multivariate normal distribution
characterized by zero mean and covariance matrix Σk. This
is represented as,
yk ∼Nm(0m, Σk)
(1)
where, 0m denotes a m × 1 matrix of zeros. The covariance
matrix, Σk, is decomposed as,
Σk = ΛkΩkΛk
(2)
where, Λ2
k is a diagonal matrix of variances and Ωk denotes
the current correlation matrix. The stochastic evolution of
the sequence, {Ωk}K
k=1, is assumed to be governed by a
latent state sequence, {Qk}K
k=1 where Qk is a real-valued
positive-deﬁnite random matrix. The dynamics of this latent
positive-deﬁnite process is described by,
Q−1
k
= 1
ν Q−d/2
k−1 EkQ−d/2
k−1
such that Ek ∼Wm(ν, Im) ,
(3)
Ωk = eQ−1
k Qk eQ−1
k
(4)
where, eQk,ij = Q1/2
k,ijδij, δij denotes the Kronecker delta
function, ν
> m, and −1 ≤d ≤1. Here, we use
X ∼Wm(ν, S) to denote a real-valued, positive-deﬁnite,
m × m random matrix X distributed according to a Wishart
probability density function (pdf) described as,
 2
νm
2 Γm(ν/2)|S|
ν
2 −1 |X|
ν−m−1
2
eTr

−1
2S−1X

, (5)
Γm(ν/2) = πm(m−1)/4
m
Y
i=1
Γ ((ν −i + 1)/2) .
(6)
and characterized by parameters S (a positive-deﬁnite ma-
trix) and scalar ν (> m) [GN09]. In this work, we use |·| and
eTr(·) to denote, respectively, determinant and exponential-
of-trace operations on a square matrix. Note that Eq. (3)
ensures that each point on the dynamic trajectory of Qk will
be positive-deﬁnite, and Q−1
k
∼Wm(ν, Q−d
k−1/ν) [GN09].
The matrix scaling operation in Eq. (4) preserves the unit-
diagonal character of the resulting correlation matrices, Ωk.
Further simplifying our theoretical modeling in Eq. (3), we
do not consider additional multiplicative coefﬁcient matrices
that can be used in relative scaling of past information
(Qk−1) [CST18, Eqs.8, 9], and assume Λk = Im, where
Im denotes a m × m identity matrix.
B. Likelihood and model parameters
The total data log-likelihood can be written out as,
p(y1:K, Q1:K|Θ) = p(Q0)
K
Y
k=1
p(yk|Qk)p(Qk|Qk−1, Θ)
(7)
where, p(X) denotes a pdf described on the appropriate
space to which X belongs, and Θ = {ν, d}. We assume
Q0 = Im and set p(Q0) = 1 [CST18].
C. Bayesian inference & Markov Chain Monte Carlo steps
For a given sequence of observations, y1:K ≡{yk}K
k=1, we
employ a Bayesian inference framework to estimate posterior
distributions on the DFC statistics, Q−1
1:K ≡{Q−1
k }K
k=1 and
Θ. Using the model (Eqs. (1), (2), (3), (4)), the unit variance
assumption, Bayes’ rule and prior probability distributions
p(ν) and p(d), we can write the following posterior pdf,
p(Q−1
1:K, ν, d|y1:K) ∝p(y1:K, Q−1
1:K|ν, d)p(ν)p(d),
(8)
where,
p(ν) = βαν
ν
αν
(ν −m)αν−1exp(−βν(ν −m))I(0,∞)(ν −m),
(9)
p(d) = (1/2)I[−1,1](d),
(10)
where, (αν, βν) denote the user-prescribed hyper-parameters
for the prior pdf on (ν−m) distributed according to a Gamma
probability distribution denoted as Gamma(αν, βν). I(X)(x)
denotes an indicator function that takes value = 1 ∀x ∈X
and = 0, otherwise.
To sample from the joint posterior pdf (Eq. (8)) per
[CST18], we use a Gibb’s sampling approach [CG95] where


## Page 3


in the j-th iteration we draw the j-th samples from the
following conditional posterior pdf’s,
Q−1
k,(j) ∼p(Q−1
k−1|Q−1
k−1,(j), Q−1
k+1,(j−1), ν(j−1), d(j−1), y1:K)
(11)
Q−1
K,(j) ∼p(Q−1
K |Q−1
K−1,(j), ν(j−1), d(j−1), y1:K)
(12)
ν(j) ∼p(ν|Q−1
1:K,(j), d(j−1), y1:K) = p(ν|Q−1
1:K,(j), d(j−1))
(13)
d(j) ∼p(d|Q−1
1:K,(j), ν(j), y1:K) = p(d|Q−1
1:K,(j), ν(j)) (14)
where, the equalities in Eqs. (13) and (14) are due to the
conditional independence assumption in the proposed SSM.
To sample x(j) ∼p(x) (where, p(x) may denote any of the
K + 2 conditional pdf’s in Eqs. (11)-(14)), given the last
sample x(j−1), we perform the following general steps of
MCMC algorithm [CG95]: we draw a candidate sample x⋆
from a relatively easy-to-sample proposal distribution whose
pdf, conditioned on x(j−1), is denoted by q(x⋆|x(j−1)) and
accept it as a new sample x(j) with an acceptance probability
given by,
min

1,
g(x⋆)q(x(j−1)|x⋆)
g(x(j−1))q(x⋆|x(j−1))

(15)
where, p(x) ∝g(x). If we are unable to accept x⋆, then we
set x(j) = x(j−1). In the following sections, Secs. II-D - II-
G, we provide the details of our choice of g(·) and q(·|·) that
will be used in Eq. 15 for each of the conditional posterior
pdfs, Eqs. (11)-(14). Note that with the expressions available
to calculate g(x⋆) and q(x⋆|x(j−1)), we can also calculate
g(x(j−1)) and q(x(j−1)|x⋆) by exchanging x(j−1) and x⋆in
the arguments.
D. Sampling Q−1
k
from conditional posterior pdf
The conditional posterior in Eq. (11) can be evaluated up
to an unknown constant factor as,
p(yk|Q−1
k , Θ)p(Q−1
k+1|Q−1
k , Θ)p(Q−1
k |Q−1
k−1, Θ) ∝g(Q−1
k )
(16)
= |Q−1
k |(ν+1−m−1)/2eTr

−ν
2S−1
k Q−1
k

|Q−1
k |(−dν)/2·
| eQk|eTr

−1
2(( eQkΛ−1
k ykyT
k Λ−1
k
eQk)Q−1
k
+ νS−1
k+1Q−1
k+1)

(17)
= |Q−1
k |(ν+1−m−1)/2·
eTr

−1
2(νS−1
k
+ eQΛ−1
k ykyT
k Λ−1
k
eQ)Q−1
k

|Q−1
k |(−dν)/2·
| eQk|
eTr

−1
2(( eQkΛ−1
k ykyT
k Λ−1
k
eQk)Q−1
k
+ νS−1
k+1Q−1
k+1)

eTr

−1
2( eQΛ−1
k ykyT
k Λ−1
k
eQ)Q−1
k

(18)
where,
Sk
≡
Q−d
k−1.
Note
that
Eq.
(18)
is
obtained
by
multiplying
and
dividing
Eq.
(17)
by
eTr(−(1/2)( eQΛ−1
k ykyT
k Λ−1
k
eQ)Q−1
k )
where
eQ = ( eQk−1 + eQk+1)/2. Per [CST18], to sample a candidate
realization, Q−1
k,⋆we use as proposal pdf, q(Q−1
k,⋆|Q−1
k,(j−1)),
the pdf of Wm(ν + 1, (νS−1
k
+ eQΛ−1
k ykyT
k Λ−1
k
eQ)−1).
E. Sampling Q−1
K from conditional posterior pdf
The conditional posterior in Eq. (12) can be expressed
upto an unknown constant as,
g(Q−1
K ) = |S−1
K |ν/2|Q−1
K |(ν+1−m−1)/2eTr

−ν
2S−1
K Q−1
K

·
| eQK|eTr

−1
2( eQKΛ−1
K yKyT
KΛ−1
K eQK

Q−1
K
(19)
. Per [CST18], to sample any candidate QK,⋆we use as
proposal pdf, q(QK,⋆|QK,(j−1)), the pdf corresponding to
Wm(ν + 1, SK/ν).
F. Sampling ν from conditional posterior pdf
The conditional posterior distribution in Eq. (13) can be
written out up to a constant multiplying factor as g(ν), such
that
ln g(ν) = I(m,∞)(ln(ν −m)αν−1 −K ln Γm(ν/2)
+ (mνK/2) ln ν −(ν/2)(2βν + mK ln 2
+
K
X
k=1
(ln|Sk|−ln|Q−1
k |+Tr(S−1
k Q−1
k ))))
(20)
To generate a candidate sample ν⋆we use as proposal pdf,
q(ν⋆|ν(j−1)), the pdf corresponding to a shifted Gamma
distribution denoted by Gamma(αp, βp). The characteristic
parameters (αp, βp) are functions of a prescribed mode
νM = ν(j−1) and user-prescribed constant variance νvar,
such that
βp(νM, νvar) = ((νM −m) + ((νM −m)2 + 4νvar)1/2
2νvar
(21)
αp(νM, νvar) = 1 + (νM −m)βp(νM)
(22)
Here, the proposal distribution, q(ν⋆|ν(j−1)), is designed
such that the mode of the distribution is at last sample ν(j−1),
and the bounds on ν are respected. To calculate q(ν(j−1)|ν⋆),
we use a different shifted Gamma pdf whose parameters are
calculated using Eqs. (21) and (22) with νM = ν⋆.
G. Sampling d from conditional posterior pdf
The posterior pdf in Eq. (14) can be written out upto an
unknown constant factor as,
g(d) = I[−1,1] exp(
K
X
k=1
(−dν/2) ln|Q−1
k−1|+
(−ν/2)Tr(Qd
k−1Q−1
k ))
(23)
To sample a candidate d⋆we use a proposal density
q(d⋆|d(j−1)) which corresponds to (1/2)× the pdf of
Beta(ap, bp). For a given mean, dA = d(j−1), constraint


## Page 4


bp = 1/ap, and a user-prescribed constant threshold param-
eter af such that 1/af ≤ap ≤af where af > 1, the
characteristic parameter is given by,
ap(dA, af) =
max
 
min
 
(1 + dA)/2
1 −(1 + dA)/2
1/2
, af
!
, 1/af
!
(24)
The proposal distribution is designed such that its mean
corresponds to the previous sample, while also having
more probability mass around this mean and respecting
the bounds on d. To determine q(d(j−1)|d⋆), we use
Beta(ap(d⋆, af), 1/ap(d⋆, af)).
III. RESULTS
A. Initialization of MCMC simulation
In all the DFC analyses performed here on synthetic and
fMRI datasets, we consider bivariate observation sequences
(m = 2), K = 150 and maximum MCMC iterations of
NMCMC = 10000. For the very ﬁrst MCMC iteration,
we initialize Q−1
k,(j=0) = Im, ∀k = 1, · · · , K. The hyper-
parameters for the prior on ν, we choose αν = m + 2, and
βν = 1, and initialize ν(j=0) = m + (αν −1)/βν. Also, we
set d(j=0) = 0.5, νvar = 0.1 and af = 5. With regard
to post-processing the MCMC generated samples, we set
the burn-in iterations for latent states and model parameters
as 1000 and 4000, respectively. Also, we set the thinning
interval for latent state and model parameters as 100 and 200,
respectively. The numbers for burn-in and thinning interval
are chosen based on visual inspection of the convergence in
the respective Markov chains and the auto-correlation (after
ignoring the samples from the burn-in iterations) in each
MCMC chain.
B. DFC analyses of simulated data
Using the generative model (Eqs.(1), (3), (4), (2)) and
setting ν = 5, d = 0.8, Λk = I2 ∀k = 1, · · · , K we generate
a single realization of bivariate observation y1:K (Fig. 1(a)).
On this data, we run our MVSV model-based estimation
procedure that is agnostic to the ground-truth model param-
eters. The ordered statistics from samples estimated from
the posterior distribution of correlation (Fig. 1(b)), and the
empirical histograms on ν and d (Fig. 1(c,d)) are reported.
Note, in Fig. 1(b), the 2.5-th and 97.5-th percentiles include
not only the true value, but also track the changes in true
correlation trajectory. Comparing with the raw data, Fig. 1(a),
we observe that where the estimated 2.5th percentile is above
0, the two time-series appear to be in synchrony (high pos-
itive correlation) with each other. On the other hand, when
the estimated 97.5th percentile is below 0, the two signals
are synchronous, but in the opposite sense (high negative
correlation). Therefore, the posterior estimates generated by
our DFC analyses enable us to infer whether the correlation
is signiﬁcant at any time instant. In Figs. 1(c) and 1(d), the
posterior samples of the model parameters are indeed in the
near-neighborhood of the ground truth. Also, note that the
posterior estimates on ν and d use only K = 150 data-points.
Fig. 1.
MVSV-based estimation on simulated data. (a) Simulated obser-
vations, (b) True correlation (magenta) and ordered statistics on estimated
posterior samples (2.5-th, 97.5-th percentiles indicated as dashed black line,
while median indicated as solid black line), green line indicates MCMC
initialization state. (c) and (d) present estimated empirical pdf’s (epdf’s)
and true value (magenta triangle) on ν and d, respectively.
With longer sessions, these estimates can be expected to be
more accurate.
C. DFC analyses of BOLD fMRI data from a patient
We demonstrate the utility of the DFC analyses pipeline,
numerically demonstrated in the previous section, on 2
recording sessions of BOLD-fMRI data. These sessions were
collected from a single DoC patient who underwent a resting-
state fMRI scan (time to repeat = 2.4 seconds) while in
post traumatic confusional state (PTCS; pre-recovery), and
6 months later after full recovery of consciousness (post-
recovery). Details of the clinical trial, recording and data pre-
processing procedures can be found in [TBR+18] 1. For the
purpose of this proof-of-concept study, we use the denoised
and artifact-rejected signal that is averaged within 2 regions-
of-interest (ROI’s) located in the medial pre-frontal cortex
(MPFC) and in the posterior cingulate cortex (PCC). The
MPFC and PCC are nodes of the default mode network, and
in a healthy subject, these ROI’s are known to have positively
correlated BOLD activity [BCE17]. The time-series dataset
from each of these 2 ROI’s is standardized by shifting the
mean to zero followed by dividing by the standard deviation,
where both the mean and standard deviations are calculated
across the entire session. The resulting standardized bivariate
sequence constitutes the observations, y1:K, to be analyzed.
For each session, using our DFC analysis framework we
estimate correlation trajectories (Fig. 2) from the entire data
sequence without application of a SW approach. The esti-
mated correlation trajectory demonstrates how the degree of
synchrony between the BOLD signals from MPFC and PCC
gradually evolve over time. The inference of such smooth
correlation trajectories is enabled by the MVSV model which
1Denoising, artifact rejection and roi-based averaging steps are performed
within CONN Matlab toolbox [WGNC12]


## Page 5


Fig. 2.
DFC analyses of BOLD fMRI data from a PTCS patient, before
and after recovery. (a, e) illustrate the standardized bivariate data from
MPFC and PCC, (b, f) present the ordered statistics (2.5-th, and 97.5-th
percentiles as dashed black lines, median as solid black line) calculated
from the estimated samples of instantaneous correlation. Figure panels (c,
g) and (d, h) present empirical pdf’s (epdf’s) on ν and d, respectively.
incorporates the inﬂuence of neighboring time points on the
current latent correlation state (Eq. (3)). Furthermore, this
DFC analysis provides session-speciﬁc estimates of ν and
d, which may be regarded as reduced-order descriptors of
the correlation dynamics. For each of these sessions, we
note that there are brief epochs where the 95% conﬁdence
interval trajectory of the estimated correlations does not
include 0. Therefore, we infer that for these 2 sessions of
fMRI data, the correlation is indeed time-varying. From
Fig. 2, we also observe that the correlation trajectory prior
to recovery includes both positive and negative correlation
values, but the trajectory after recovery remains mostly
above zero. Thus, the MVSV model and the corresponding
DFC statistics (latent states and model parameters), together
provide a principled lower-dimensional objective vocabulary
to describe the complex correlation dynamics in multivariate
BOLD signals. In the absence of ground truth, the generative
nature of the MVSV model allowed us to analyze the
performance of the inference framework against synthetically
generated ground truth (see Sec. III-B).
IV. CONCLUSION
In summary, we modiﬁed an MVSV model from the
econometrics literature [CST18] to develop a novel DFC
analysis approach for multivariate neural data. We used this
approach to perform exploratory DFC analyses of bivariate
resting-state BOLD fMRI data from a patient with DoC. We
introduced principled modiﬁcations to the proposal densities
within the MCMC simulations for estimating two key DFC
model parameters. We numerically veriﬁed the estimation
framework on synthetic data. We then deployed the numeri-
cally veriﬁed DFC analysis pipeline on two fMRI recordings
from the patient, before and after recovery of consciousness.
Our analysis of resting-state BOLD activity in this DoC
patient indicates that the correlation between MPFC and PCC
varied within the duration of the recording and correlation
dynamics showed marked change when the patient recovered.
Our MVSV model-based DFC analysis pipeline does
not require sliding windows, and it can estimate gradually
evolving correlation trajectories as well as reduced-order
statistical descriptors of correlation dynamics. Furthermore,
the estimation framework results in probability distributions,
learnt from both prior knowledge and available data, that
quantify the uncertainty in both the estimated time-varying
correlations and the model parameters. Such probability
distributions can be used to compare correlations across
multiple time-points in the same session, and to infer dy-
namic connectivity graphs. A next step will be to extend our
bivariate treatment to higher dimensions. Furthermore, this
work suggests that exploring SSMs with matrix-variate latent
processes for principled DFC analysis of neural data may aid
DFC-based bio-marker discovery.
REFERENCES
[AM14]
Evan G Antzoulatos and Earl K Miller. Increases in functional
connectivity between prefrontal cortex and striatum during
category learning. Neuron, 83(1):216–225, 2014.
[BCE17]
Yelena G Bodien, Camille Chatelle, and Brian L Edlow.
Functional networks in disorders of consciousness. In Seminars
in neurology, volume 37, pages 485–502. Thieme Medical
Publishers, 2017.
[CG95]
Siddhartha Chib and Edward Greenberg. Understanding the
Metropolis-Hastings algorithm.
The American Statistician,
49(4):327–335, 1995.
[CG16]
Joshua CC Chan and Angelia L Grant.
Modeling energy
price dynamics: GARCH versus stochastic volatility. Energy
Economics, 54:182–189, 2016.
[CST18]
Roberto Casarin, Domenico Sartore, and Marco Tronzano. A
Bayesian Markov-switching correlation model for contagion
analysis on exchange rate markets.
Journal of Business &
Economic Statistics, 36(1):101–114, 2018.
[DTD+19]
Athena Demertzi, Enzo Tagliazucchi, Stanislas Dehaene, Gus-
tavo Deco, Pablo Barttfeld, Federico Raimondo, Charlotte Mar-
tial, Davinia Fern´andez-Espejo, Benjamin Rohaut, HU Voss,
et al. Human consciousness is supported by dynamic com-
plex patterns of brain signal coordination. Science advances,
5(2):eaat7603, 2019.
[ECS+17]
Brian L Edlow, Camille Chatelle, Camille A. Spencer, Cather-
ine J. Chu, Yelena G. Bodien, Kathryn L. OConnor, Ronald E.
Hirschberg, Leigh R. Hochberg, Joseph T. Giacino, Eric S.
Rosenthal, and Ona Wu.
Early detection of consciousness
in patients with acute severe traumatic brain injury.
Brain,
140(9):2399–2414, 07 2017.
[ES01]
Robert F Engle and Kevin Sheppard. Theoretical and empiri-
cal properties of dynamic conditional correlation multivariate
garch.
Technical report, National Bureau of Economic Re-
search, 2001.
[Fri11]
Karl J Friston. Functional and effective connectivity: a review.
Brain connectivity, 1(1):13–36, 2011.
[GN09]
Arjun K Gupta and Daya K Nagar. Matrix variate distributions.
Chapman and Hall/CRC, 2009.
[LXNC14]
Martin A Lindquist, Yuting Xu, Mary Beth Nebel, and Brain S
Caffo.
Evaluating dynamic bivariate correlations in resting-
state fmri: a comparison study and a new approach. NeuroIm-
age, 101:531–546, 2014.
[SS82]
Robert H Shumway and David S Stoffer.
An approach to
time series smoothing and forecasting using the EM algorithm.
Journal of time series analysis, 3(4):253–264, 1982.
[TBR+18]
Zachary D Threlkeld, Yelena G Bodien, Eric S Rosenthal,
Joseph T Giacino, Alfonso Nieto-Castanon, Ona Wu, Susan
Whitﬁeld-Gabrieli, and Brian L Edlow. Functional networks
reemerge during recovery of consciousness after acute severe
traumatic brain injury. Cortex, 106:299–308, 2018.
[TL15]
Enzo Tagliazucchi and Helmut Laufs. Multimodal imaging of
dynamic functional connectivity. Frontiers in Neurology, 6:10,
2015.
[WGNC12] Susan Whitﬁeld-Gabrieli and Alfonso Nieto-Castanon. Conn:
a functional connectivity toolbox for correlated and anticorre-
lated brain networks. Brain connectivity, 2(3):125–141, 2012.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
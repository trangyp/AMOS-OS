---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1809.06913v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1809.06913v2_Predictive_Collective_Variable_Discovery_with_Deep_Bayesian_Models

> Source: 1809.06913v2_Predictive_Collective_Variable_Discovery_with_Deep_Bayesian_Models.pdf

> Pages: 47

---


## Page 1


Predictive Collective Variable Discovery with Deep Bayesian Models
Markus Sch¨oberl,1, 2, a) Nicholas Zabaras,1, b) and Phaedon-Stelios Koutsourelakis2, c)
1)Center for Informatics and Computational Science, University of Notre Dame,
311 Cushing Hall, Notre Dame, IN 46556, USA.
2)Continuum Mechanics Group, Technical University of Munich,
Boltzmannstraße 15, 85748 Garching, Germany.
(Dated: 18 January 2019)
Preprint - accepted and published in The Journal of Chemical Physics 2019 150:2;
https: // doi. org/ 10. 1063/ 1. 5058063 .
Extending spatio-temporal scale limitations of models for complex atomistic systems
considered in biochemistry and materials science necessitates the development of en-
hanced sampling methods. The potential acceleration in exploring the conﬁgurational
space by enhanced sampling methods depends on the choice of collective variables
(CVs). In this work, we formulate the discovery of CVs as a Bayesian inference prob-
lem and consider the CVs as hidden generators of the full-atomistic trajectory. The
ability to generate samples of the ﬁne-scale atomistic conﬁgurations using limited
training data allows us to compute estimates of observables as well as our proba-
bilistic conﬁdence on them. The methodology is based on emerging methodological
advances in machine learning and variational inference. The discovered CVs are re-
lated to physicochemical properties which are essential for understanding mechanisms
especially in unexplored complex systems. We provide a quantitative assessment of
the CVs in terms of their predictive ability for alanine dipeptide (ALA-2) and ALA-15
peptide.
a)Electronic mail: mschoeberl@gmail.com
b)https://cics.nd.edu/; Electronic mail: nzabaras@gmail.com
c)http://www.contmech.mw.tum.de; Electronic mail: p.s.koutsourelakis@tum.de
1
arXiv:1809.06913v2  [stat.ML]  16 Jan 2019


## Page 2


I.
INTRODUCTION
Molecular dynamics (MD) simulations, in combination with prevalent algorithmic en-
hancements and tremendous progress in computational resources, have contributed to new
insights into mechanisms and processes present in physics, chemistry, biology and engineer-
ing. However, their applicability in systems of practical relevance poses insurmountable
computational diﬃculties1,2. For example, the simulation of M = 105 atoms over a time
horizon of a mere T ≈10−4 s with a time step of ∆t = 10−15 s implies a computational time
of one year3. A rugged free-energy surface and conﬁgurations separated by high free-energy
barriers lead to unobserved conformations even in very long simulations.
Enhanced sampling methods4 provide a framework for accelerating the exploration of
the conﬁgurational space5–11. Those methods rely on the existence of a lower-dimensional
representation of the atomistic detail. Lower-dimensional system variables (reaction coordi-
nates), capture the characteristics of the system, allow us to understand relevant processes
and conformational changes12, and can enable guided and enhanced MD simulations. Re-
action coordinates provide quantitative understanding of macromolecular motion, whereas
order parameters are of qualitative nature as discussed in [13]. In the following, we use the
term collective variables (CVs), combining the quantitative and qualitative properties of re-
action coordinates and order parameters, respectively. Refs. [4 and 13] review the challenges
in the exploration of the free-energy landscape and the identiﬁcation of “good” collective
variables.
Adding an appropriate biasing potential or force, based on CVs, results into an accel-
erated exploration of the conﬁgurational space13.
Such algorithms might employ a con-
stant bias term (e.g. umbrella sampling14, hyperdynamics15, accelerated MD16, etc.) or a
time-dependent one (e.g. local elevation17, conformational ﬂooding18, metadynamics3,19,20,
adaptive biasing force21,22, etc.). The crucial ingredient for almost all of the aforementioned
algorithms is the right choice of the collective variables. The potential beneﬁt and justi-
ﬁcation of enhanced sampling algorithms strongly depend on the quality of the collective
variables as comprehensively elaborated in [23–25]. Physical intuition, experience gathered
from previous simulation as well as quantitative methods for dimensionality reduction (e.g.
by utilizing principal component analysis26 (PCA)), potentially support the choice of reason-
able collective variables. For complex materials-design problems and large-scale biochemical
2


## Page 3


processes, complexity exceeds our intuition and the question of “good” collective variables
remains unanswered. Enhanced sampling methods employing inappropriate collective vari-
ables can be outperformed by brute force MD simulations27. Thus, the identiﬁcation of
collective variables or reaction coordinates poses an important and diﬃcult problem.
A systematic, robust, and general approach is needed for the discovery of lower-dimensional
representations. Recent developments in dimensionality reduction methods provide a sys-
tematic strategy for discovering CVs13.
For completeness, we give a brief overview of
signiﬁcant tools addressing CV discovery and dimensionality reduction in the context of
molecular systems.
An early study28 found a steep decay in the eigenvalues of peptide
trajectories indicating the existence of a low-dimensional representation that is capable
of capturing essential physics. This study is based on PCA26,29 which identiﬁes a linear
coordinate transformation for best capturing the variance. However, the linear coordinate
transformations employed merely describe local ﬂuctuations in the context of peptide trajec-
tories. Multidimensional scaling (MDS)30,31 identiﬁes a lower-dimensional embedding such
that pairwise distances (e.g. root-mean-square deviation (RMSD)) between atomistic con-
ﬁgurations are best preserved. Sketch-map32 focuses on preserving “middle” ranged RMSD
between trajectory pairs. Middle ranged RMSD pairs are the most relevant for observing
pertinent behavior of the system32. Isometric feature map or ISOMAP33 follows a similar
idea of preserving geodesic distances. The aforementioned methods require dense sampling
and encounter problems if the training data is non-uniformly distributed34–36. Furthermore,
we note that those methods involve a mapping from the atomistic conﬁgurations to the
CVs whereas predictive tasks require a generative mapping from the CVs to the atomistic
conﬁguration.
Another group of non-linear dimensionality reduction methods follows the idea of ap-
proximating the eigenfunctions of the backward Fokker-Plank operator37 by identifying
eigenvalues and eigenvectors of transition kernels.
The employed kernels resemble tran-
sition probabilities between conﬁgurations that we aim to preserve. For example, the diﬀu-
sion map38–40 retains the diﬀusion distance by the identiﬁed coordinates for dynamic41 and
stochastic systems42. A variation of diﬀusion maps exploits locally scaled diﬀusion maps (LS-
DMap)34 which calculate the transition probabilities between two conﬁgurations, utilizing
the RMSD instead of an Euclidean distance. An additional local scale parameter, indicating
the distance around a speciﬁc conﬁguration presumably could be well approximated by a
3


## Page 4


low-dimensional hyperplane tangent. LSDMap is applied in [43] and enhances the explo-
ration of the conﬁgurational space as shown in [44]. More recent approaches to collective
variable discovery work under a common variational approach for conformation dynamics
(VAC)45 and employ a combination of basis functions for deﬁning the eigenfunctions to the
backward Fokker-Planck operator. One approach under VAC was developed in the context
of metadynamics19 combining ideas from time-lagged independent component analysis and
well-tempered metadynamics46. Further developments have focused on alternate distance
metrics, relying either on a kinetic distance which measures how slowly conﬁgurations inter-
convert47, or on the commute distance48 which provides an extension (arising by integration)
of the former.
Several methods rely on the estimation of the eigenvectors of transitions matrices which
is an expensive task in terms of computational cost. The need for “large” training datasets
(e.g. 10 000 datapoints are required for robustness of the results 13) limits the applicability of
these methods to less complex systems. We refer to [49] for a critical review and comparison
of the various methodologies mentioned before.
In this work, we propose a data-driven reformulation of the identiﬁcation of CVs under the
paradigm of probabilistic (Bayesian) inference. The methodology implies a generative model,
considering CVs as lower-dimensional (latent) generators50 of the full atomistic trajectory.
The focus furthermore is on problems where limited atomistic training data are available that
prohibit the accurate calculation of statistics for quantities of interest. Our approach is to
compute an approximation of the underlying probabilistic distribution of the data. We then
use this approximate distribution in a generative manner to perform accurate Monte Carlo
estimation of the quantities of interest. To account for the limited information provided
by small size training datasets, epistemic uncertainties on quantities of interest are also
computed within the Bayesian paradigm.
In the context of coarse-graining atomistic systems, latent variable models have been
introduced in [51 and 52]. We optimize a ﬂexible non-linear mapping between CVs and
atomistic coordinates which implicitly speciﬁes the meaning of the CVs.
The identiﬁed
CVs provide physical/chemical insight into the characteristics of the considered system.
In the proposed model, the posterior distribution of the CVs for a given atomistic data
point is computed. This posterior provides a pre-image of the atomistic representation in
the lower-dimensional latent space. We utilize recent developments in machine learning and
4


## Page 5


deep Bayesian modeling (Auto-Encoding Variational Bayes53,54). While typically deep learn-
ing models rely on huge amounts on data, we demonstrate the robustness of the proposed
methodology considering only small and highly-variable datasets (e.g. 50 data points com-
pared to 10 000 as required in the aforementioned methods). The proposed strategy requires
signiﬁcantly less data as compared to MDS30,31, ISOMAP33, and diﬀusion map38,39,41 and
simultaneously enables the quantiﬁcation of uncertainties arising from limited data. We also
discuss how additional datapoints can be readily incorporated by eﬃciently updating the
previously trained model.
Apart from the possibility of utilizing the discovered CVs for dimensionality reduction and
enhanced sampling, we exploit them for predictive purposes i.e. for generating new atom-
istic conﬁgurations and estimating macroscopic observables. One could draw similarities
between the identiﬁcation of CVs and the problem of identifying a good coarse-grained rep-
resentation51,55–66. In addition, rather than solely obtaining point estimates of observables,
the Bayesian framework adopted provides whole distributions which capture the epistemic
uncertainty. This uncertainty propagates in the form of error bars around the predicted
observables.
Several recent publications focus on similar problems67–69.
The present work clearly
diﬀers from [69] where the data is provided in a pre-processed form of sine and cosine
backbone dihedral angles, i.e. not as the full-atom conﬁgurations. The approach in [68]
utilizes a pre-reduced representation of heavy atom positions as training data. While this is
valid, it necessitates physical insight which might be not available for unexplored complex
chemical compounds. In contrast, we rely on training data represented as Cartesian coordi-
nates comprising all atoms of the considered system. We do not consider any physically- or
chemically-motivated transformation nor do we perform any preprocessing of the dataset.
Instead, we reveal, given the dimensionality of the CVs, important characteristics (i.e. di-
hedral angles, heavy atom positions) or less relevant ﬂuctuations (noise) from the full atom-
istic picture. This work is also distinguished by following throughout a formalism based
on Bayesian Learning.
Instead of adopting or designing optimization objectives or loss
functions, we consistently work within a Bayesian framework where the objective naturally
arises. Furthermore, this readily allows us to make use of sparsisty-inducing priors which
reveal parsimonious features. The work of [8] is based on auto-associative artiﬁcial neural
networks (autoencoders) which allow the encoding and reconstruction of atomistic conﬁgu-
5


## Page 6


rations given an input datum. Ref. [8] relies on reduced Cartesian coordinates in the form of
backbone atoms which induces information loss. In addition, the focus in [8] is on CV dis-
covery and enhanced sampling whereas we focus on CV discovery and obtaining a predictive
model accounting for epistemic uncertainty.
The structure of the rest of the paper is as follows. Section II presents the basic model
components, the use of Variational Autoencoders (VAEs53) in the CV discovery, and pro-
vides details on the learning algorithms employed. Numerical evidence of the capabilities of
the proposed framework is provided in Section III. We identify CVs for alanine dipeptide and
show the correlation between the discovered CVs and the dihedral angles. We furthermore
assess the predictive quality of the discovered CVs and estimate observables augmented by
credible intervals. We show the dependence of credible intervals on the amount of training
data.
We also present the results of a similar analysis for a more complex and higher-
dimensional molecule, i.e. the ALA-15 peptide. Finally, Section IV summarizes the key
ﬁndings of this paper and provides a brief discussion on potential extensions.
II.
METHODS
After introducing the main notational convention in the context of equilibrium statistical
mechanics, this section is devoted to the key concepts of generative latent variable models
and variational inference70 with emphasis on the identiﬁcation of collective variables in
atomistic systems.
A.
Equilibrium statistical mechanics
We denote the coordinates of atoms of a molecular ensemble as x ∈Mf ⊂Rnf, with
nf = dim(x). The coordinates x follow the Boltzmann-Gibbs density,
ptarget(x) =
1
Z(β)e−βU(x),
(1)
with the interatomic potential U(x), β =
1
kbT where kb is the Boltzmann constant and T
the temperature. The normalization constant is given as Z(β) =
R
Mf exp{−βU(x)} dx.
MD simulations71, or Monte-Carlo-based methods72 allow us to obtain samples from the
distribution deﬁned in Eq. (1). In the following, we assume that a dataset, X = {x(i)}N
i=1,
6


## Page 7


has been collected, where x(i) ∼ptarget(x). N denotes the amount of data points considered.
The dataset X will be used for training the generative model to be introduced in the
sequel. The underlying assumption in this work is that the size of the available training
dataset X is small and not suﬃcient to compute directly statistics of observables. Our
focus is thus on deriving an approximation to the distribution in Eq. (1) from which, in
a computationally inexpensive manner, one can sample suﬃcient realizations of x to allow
probabilistic estimates of observables.
As elaborated in [13], the collection of a dataset X that suﬃciently captures the conﬁgu-
rational space constitutes a diﬃcult problem of its own. Hampered by free-energy barriers,
a MD simulation is not guaranteed to visit all conformations of an atomistic system within
a ﬁnite simulation time. The discovery of CVs can facilitate the development of enhanced
sampling methods3,19,23 to address the eﬃcient exploration of the conﬁgurational space.
This study considers systems in equilibrium for a given constant temperature T and
consequently constant β. Optimally, the CVs discovered should be suitable for a range of
temperatures25.
B.
Probabilistic generative models
Deep learning73 integrated with probabilistic modeling74 has impacted many research
areas75. In this paper, we emphasize a subset of these models referred to as probabilistic
generative models50,76.
The objective is to identify CVs associated with relevant conﬁgurational changes of the
system of interest. We consider CVs as hidden (low-dimensional) generators, giving rise
to the observed atomistic conﬁgurations x77.
Extending the variable space of atomistic
coordinates x by latent CVs denoted as z ∈MCV ⊂RnCV, with nCV = dim(z) and
dim(z) ≪dim(x), allows us to deﬁne a joint distribution over the observed data x and
latent CVs50,78 p(x, z). The joint distribution p(x, z) is written as,
p(x, z) = p(x|z) p(z).
(2)
In Eq. (2), p(z) prescribes the distribution of the CVs and p(x|z) represents the conditional
probability of the full atomistic coordinates x given their latent representation z. The prob-
abilistic connection between the latent CVs z and the atomistic representation x implicitly
deﬁnes the meaning of the CVs.
7


## Page 8


Marginalizing the joint representation of Eq. (2) with respect to the CVs leads to p(x),
p(x) =
Z
MCV
p(x, z) dz =
Z
MCV
p(x|z) p(z) dz.
(3)
Equation (3) provides a generative model for the atomistic conﬁgurations x and will be uti-
lized as an eﬃcient estimator for observables of the atomistic system. Standard autoencoders
in the context of CV discovery8 do not yield a probabilistic, predictive model which is the
focus of this work. With appropriate selection of p(z) and p(x|z), the resulting predictive
distribution p(x) should resemble the atomistic reference ptarget(x) in Eq. (1). In order to
quantify the closeness of the approximating distribution p(x) and the actual distribution
ptarget(x), a distance measure is employed. The KL-divergence is one possibility out of the
family of α-divergences79,8081 measuring the similarity between redptarget(x) and p(x). The
non-negative valued KL-divergence is zero if and only if the two distributions coincide, which
leads to the minimization objective with respect to p(x) of the following form:
DKL(ptarget(x)||p(x)) = −
Z
Mf
ptarget(x) log
p(x)
ptarget(x) dx
= −
Z
Mf
ptarget(x) log p(x) dx
+
Z
Mf
ptarget(x) log ptarget(x) dx.
(4)
We introduce a parametrization θ of the approximating distribution as p(x|θ) =
R
MCV pθ(x|z)pθ(z) dz.
Instead of minimizing the KL-divergence with respect to p(x), one can optimize the objective
with respect to the parameters θ. We note that the minimization of Eq. (4) is equivalent to
maximizing the expression
R
Mf ptarget(x) log p(x) dx. If we consider a data-driven approach
where ptarget(x) is approximated by a ﬁnite-sized dataset X, we can write the problem as
the maximization of the marginal log-likelihood log pθ(x(i), · · · , x(N)):
log p(X|θ) =
N
X
i=1
log p(x(i)|θ)
=
N
X
i=1
log
Z
MCV
pθ(x(i)|z(i)) pθ(z(i)) dz(i)

.
(5)
Maximizing Eq. (5) with respect to the model parameters θ results into the maximum likeli-
hood estimate (MLE) θMLE. By introducing a prior p(θ) on the parameters, one can augment
this optimization problem to compute the Maximum a Posteriori (MAP) estimate82–84 of θ
8


## Page 9


as follows:
arg max
θ
{log p(X|θ) + log p(θ)} .
(6)
The full posterior of the model parameters θ could also be obtained by applying Bayes’ rule,
p(θ|X) = p(X|θ)p(θ)
p(X)
.
(7)
Quantifying uncertainties in θ enables us to capture the epistemic uncertainty introduced
from the limited training data. The discovery of CVs through Bayesian inference is elabo-
rated in the sequel.
C.
Inference and learning
This section focuses on the details of inference and parameter learning for the gener-
ative model introduced in Eq. (3). Both tasks are facilitated by approximate variational
inference85 and stochastic backpropagation54,86,87 which we discuss next.
Direct optimization of the marginal likelihood p(x|θ) requires the evaluation of p(x|θ) =
R
MCV pθ(x|z)pθ(z) dz which constitutes an intractable integration over MCV. The posterior
over the latent CVs, pθ(z|x) = pθ(x|z)pθ(z)/p(x|θ), is also computationally intractable.
Therefore, direct application of Expectation-Maximization88,89 is not feasible. To that end,
we reformulate the marginal log-likelihood for the dataset X = {x(i)}N
i=1 by introducing
auxiliary densities qφ(z(i)|x(i)) parametrized by φ.
The meaning of qφ(z(i)|x(i)) will be
speciﬁed later in the text. The marginal log-likelihood follows,
log p(X|θ) =
N
X
i=1
log p(x(i)|θ)
=
N
X
i=1
log
Z
MCV
pθ(x(i)|z(i))pθ(z(i)) dz(i)
=
N
X
i=1
log
Z
MCV
qφ(z(i)|x(i))pθ(x(i)|z(i))pθ(z(i))
qφ(z(i)|x(i))
dz(i)
≥
N
X
i=1
Z
MCV
qφ(z(i)|x(i)) log pθ(x(i)|z(i))pθ(z(i))
qφ(z(i)|x(i))
dz(i)
|
{z
}
L(θ,φ;x(i))
,
(8)
where in the last step we have made use of Jensen’s inequality. Note that for each data
9


## Page 10


point x(i), one latent CV z(i) is assigned. The lower-bound of the marginal log-likelihood is:
L(θ, φ; X) =
N
X
i=1
L(θ, φ; x(i)),
(9)
and implicitly depends on φ through the parametrization of qφ(z|x). For each data point
x(i) and from the deﬁnition of L(θ, φ; x(i)), one can rewrite the marginal log-likelihood
log p(x(i)|θ) as,
log p(x(i)|θ) = DKL
 qφ(z(i)|x(i))||pθ(z(i)|x(i))

+ L(θ, φ; x(i)) ≥L(θ, φ; x(i)).
(10)
Since the KL-divergence is always non-negative, the inequalities in Eq. (8) and Eq. (10) be-
come equalities if and only if qθ(z(i)|x(i)) = pθ(z(i)|x(i)) as in this case DKL
 qφ(z(i)|x(i))||pθ(z(i)|x(i))

=
0. Thus qφ(z(i)|x(i)) can be thought of as an approximation of the true posterior over the
latent variables z. If the lower-bound gets tight, qφ(z(i)|x(i)) equals the exact posterior
pθ(z|x(i)).
Equation (8) can also be written as follows,
L(θ, φ; X) =
N
X
i=1
Eqφ(z(i)|x(i))[−log qφ(z(i)|x(i)) + log pθ(x(i), z(i))]
= −
N
X
i=1
DKL
 qφ(z(i)|x(i))||pθ(z(i))

+
N
X
i=1
Eqφ(z(i)|x(i))[log pθ(x(i)|z(i))].
(11)
It is clear from Eq. (11) that the lower-bound balances the optimization of the following two
objectives53:
1. Minimizing PN
i=1 DKL
 qφ(z(i)|x(i))||pθ(z)

regularizes the approximate posterior
qφ(z(i)|x(i)) such that, on average over all data points x(i), it resembles pθ(z). We
expect highly probable atomistic conﬁgurations x(i) to be encoded to CVs z(i) located
in regions with high probability mass in pθ(z). The approximate posterior qφ(z(i)|x(i))
over the latent CVs z accounts for this and supports ﬁndings presented in [68].
2. Eqφ(z(i)|x(i))[log pθ(x(i)|z(i))] is the negative expected reconstruction error employing
the encoded pre-image of the atomistic conﬁguration x(i) in the latent CV space. For
example assuming pθ(x(i)|z(i)) to be a Gaussian with mean µ(z(i)) and variance σ2,
10


## Page 11


x(i)
z(i)
φ
θ
N
FIG. 1. Probabilistic graphical model representation following [53] with the latent CV representa-
tion z(i) of each conﬁguration x(i) obtained by the approximate variational posterior qφ(z(i)|x(i))
using the parametrization φ. The variational approximation is indicated with dashed edges and the
generative model pθ(x|z)p(z) with solid edges. θ is the parametrization of the generative model.
one can rewrite Eqφ(z(i)|x(i))[log pθ(x(i)|z(i))] as,
Eqφ(z(i)|x(i))[log pθ(x(i)|z(i))] = Eqφ(z(i)|x(i))
"
−1
2
 x(i) −µ(z(i))
2
σ2
#
+ const.
∝−Eqφ(z(i)|x(i))
h x(i) −µ(z(i))
2i
= −
Z
MCV
qφ(z(i)|x(i))
 x(i) −µ(z(i))
2 dz(i).
(12)
The second line of Eq. (12) is the negative expected error of reconstructing the atom-
istic conﬁguration x(i) through the decoder pθ(x(i)|z(i)). The expectation (see last line
in Eq. (12)) is evaluated with respect to qφ(z(i)|x(i)) and therefore with respect to all
CVs z(i) probabilistically assigned to x(i).
The approximate posterior qφ of the latent variables z serves as a recognition model
and is called the encoder53. Atomistic conﬁgurations x can be mapped via qφ(z|x) to their
lower-dimensional representation z in the CV space. Hence, each z could be interpreted as a
(latent) encoding of an x. Its counterpart, the decoder pθ(x|z), probabilistically maps CVs
z to atomistic conﬁgurations x. As it will be demonstrated in the sequel, z sampled from
pθ(z) will be used to reconstruct atomistic conﬁgurations via pθ(x|z). The corresponding
graphical model is presented in Fig. 1. Note that we do not require any physicochemical
meaning assigned to the latent CVs that are identiﬁed implicitly during the training process.
The (approximate) inference task of qφ(z|x) has been re-formulated as an optimization
11


## Page 12


problem with respect to the parameters φ. These will be updated in combination with the
parameters θ as described in the following. At this point, we emphasize that the lower-
bound L(θ, φ; x(i)) on the marginal log-likelihood (unobserved CVs are marginalized out)
of Eq. (11) has been used as a negative “loss” function in non-Bayesian applications of
autoencoders in the context of atomistic simulations as in [67 and 69].
In order to carry out the optimization L(φ, θ; X) with respect to {φ, θ}, ﬁrst-order
derivatives are needed of terms involving expectations with respect to qφ as it can be
seen in Eq. (11). Consider in general a function f(z) and the corresponding expectation
Eqφ(z|x)[f(z)]. Its gradient with respect to φ can be expressed as
∇φEqφ(z|x)[f(z)] = Eqφ(z|x)

f(z)∇qφ(z|x) log qφ(z|x)

,
(13)
and the expectation Eqφ(z|x)[·] on the right hand-side can be approximated via a Monte-
Carlo (MC) estimate using samples of z drawn from qφ(z|x). It is however known86 that
the variance of such estimators can be very high which adversely aﬀects the optimization
process. The high variance of the estimator in Eq. (13) can be addressed with the so-called
reparametrization trick53,54. It is based on expressing z by auxiliary random variables ϵ and
a diﬀerentiable transformation gφ(ϵ; x) as
z = gφ(ϵ; x) with ϵ ∼p(ϵ).
(14)
Using the mapping, gφ : ϵ →z, we can write the following for the densities p(ϵ) and qφ(z|x):
qφ(z|x) = p
 g−1
φ (z; x)

∂g−1
φ (z; x)
∂z
.
(15)
In Eq. (15), g−1
φ : z →ϵ denotes the inverse function of gφ which gives rise to ϵ = g−1
φ (z; x).
Several such transformations have been documented for typical densities (e.g. Gaussians)90.
The change of variables leads to the following expression for the gradient,
∇φEqφ(z|x)[f(z)] = Ep(ϵ)[∇φf(gφ(ϵ; x))]
= Ep(ϵ)
∂f(gφ(ϵ; x))
∂z
∂gφ(ϵ; x))
∂φ

,
(16)
which can in turn be calculated by Monte Carlo using samples of ϵ drawn from p(ϵ). Based
on this, we deﬁne the following modiﬁed estimator for the lower-bound53,
˜L(φ, θ; x(i)) = −DKL
 qφ(z(i)|x(i))||pθ(z)

+ 1
L
L
X
l=1
log pθ(x(i)|z(i,l))
with z(i,l) = gφ(ϵ(l); x(i)) and ϵ(l) ∼p(ϵ).
(17)
12


## Page 13


Note that for the particular forms of qφ(z(i)|x(i)) and pθ(z) selected in Section III A 2,
DKL
 qφ(z(i)|x(i))||pθ(z)

becomes an analytically tractable expression. In order to increase
the computational eﬃciency, we work with a sub-sampled minibatch XM comprising M
datapoints from X, with M < N.
This leads to ⌊N/M⌋minibatches, each uniformly
sampled from X. The corresponding estimator of the lower-bound on the marginal log-
likelihood is then given as,
L(φ, θ; X) ≃˜LM(θ, φ; XM) = N
M
M
X
i=1
˜L(θ, φ; x(i)),
(18)
with ˜L(θ, φ; x(i)) computed in Eq. (17). The factor N/M in Eq. (18) rescales PM
i=1 ˜L(θ, φ; x(i))
such that the lower-bound ˜LM(θ, φ; XM) computed by M < N datapoints approximates
the actual lower-bound L(φ, θ; X) computed with N datapoints53. However, note that us-
ing a subset of the datapoints unavoidably increases the variance in the stochastic gradient
estimator Eq. (17). Strategies compensating this increase are presented in [91 and 92] and
a rigorous study of optimization techniques with enhancements in the context of coarse-
graining is given in [62]. The overall inference procedure is summarized in Algorithm 1.
Algorithm 1 Stochastic Variational Inference Algorithm.
{θ, φ} ←Initialize parameters.
repeat
XM ←Random minibatch of M datapoints drawn from dataset X.
ϵ ←Random sample(s) from noise distribution p(ϵ).
g ←∇φ,θ ˜LM(φ, θ; XM) Calculate gradients with the estimator in Eq. (18).
{φ, θ} ←Update parameters with gradient g (e.g. employing ADAM93).
until Convergence of {θ, φ}.
return {θ, φ}.
We ﬁnally note that new data can be readily incorporated by augmenting accordingly
the objective and initializing the algorithm with the optimal parameter values found up to
that point. In fact this strategy was adopted in the results presented in the Section III and
led to signiﬁcant eﬃciency gains. One can envision running an all-atom simulation which
sequentially generates new training data that are automatically and quickly ingested by the
proposed coarse-grained model which is in turn used to produce predictive estimates as will
13


## Page 14


be described in the sequel. In contrast, other dimensionality reduction methods based on the
solution of an eigenvalue problem are required to solve a new system for the whole dataset
when new data is presented.
D.
Predicting atomistic conﬁgurations - Leveraging the exact likelihood
After training the model as described in Section II C, we are interested in obtaining the
predictive distribution p(x|θ) =
R
MCV pθ(x|z)pθ(z) dz (see Eq. (3)) which poses a demand-
ing computational task. One approach for predicting conﬁgurations x distributed according
to p(x|θ) is ancestral sampling. Firstly, one can generate a sample zl from pθ(z) and sec-
ondly sample x(k,l) ∼pθ(x|zl). The variance of such estimators signiﬁcantly increases with
increasing dim(z). Ancestral sampling does not account for training the model by employing
an approximate posterior qφ(z|x) instead of the actual posterior pθ(z|x) of the CVs z. The
Metropolis-within-Gibbs sampling scheme94 accounts for grounding the optimization of the
objective in Eq. (11) on a variational approximation. This approach builds upon ﬁndings
in [54] and proposes that generated samples ¯x follow a Markov chain (zt, ¯xt) for steps t ≥1.
Ref. [94] proposes employing the following Metropolis95,96 update criterion ρt reﬂecting a
ratio of importance ratios,
ρt =
pθ(¯xt−1|˜zt) pθ(¯zt)
pθ(¯xt−1|zt−1) pθ(zt−1)
qφ(˜zt|¯xt−1)
qφ(zt−1|¯xt−1)
.
(19)
Equation (19) provides the needed correction when using the approximate latent variable
posterior qφ(z|x). When the CV’s exact posterior is identiﬁed, i.e. when DKL (qφ(z|x)||pθ(z|x)) =
0, all proposals zt in Algorithm 2 are accepted with ρt = 1.
14


## Page 15


Algorithm 2 Metropolis-within-Gibbs Sampler [94].
Input Trained model pθ(x|z)pθ(z) and approximate posterior qφ(z|x). Total steps T.
Initialize (z0, ¯x0).
for t = 1 to T do
˜zt ∼qφ(z|¯xt−1) Draw proposal ˜zt from the approximate posterior qφ(z|¯xt−1).
ρt =
pθ(¯xt−1|˜zt) pθ(¯zt)
pθ(¯xt−1|zt−1) pθ(zt−1)
qφ(zt−1|¯xt−1)
qφ(˜zt|¯xt−1)
Estimate the Metropolis acceptance ratio, correcting for
the use of the approximate posterior distribution qφ(z|x).
zt =







˜zt
with probability ρt
zt−1
with probability 1 −ρt.
¯xt ∼pθ(x|zt)
end for
return ¯x1:T .
E.
Prior speciﬁcation
The recent work of [94] discusses the pitfalls of overly expressive, deep, latent variable
models which can yield inﬁnite likelihoods and ill-posed optimization problems97. We address
these issues by regularizing the log-likelihood with functional priors98,99. The prior contri-
bution is added as an additional component in the log-likelihood as indicated in Eq. (6).
In addition to enhanced stability during training94, sparsity inducing priors alleviate the
overparameterized nature of complex neural networks.
We adopt the Automatic Relevance Determination (ARD100) model which consists of the
following distributions:
p(θ|τ) ≡
Y
k
N(θk|0, τ −1
k ),
τk ∼Gamma(τk|a0, b0).
(20)
Equation (20) implies modeling each θk with an independent Gaussian distribution. The
Gaussian distribution has zero-mean and an independent precision hyper-parameter τk, mod-
eled with a (conjugate) Gamma density. The resulting prior p(θk) follows (by marginalizing
the hyper-parameter τk) a heavy-tailed Student’s t−distribution. This distribution favors a
priori sparse solutions with θk close to zero. In order to compute derivatives of the log-prior,
required for learning the parameters θ, we treat the τk’s as latent variables in an inner-loop
expectation-maximization scheme101 which consists of the following steps:
15


## Page 16


• E-step - evaluate:
⟨τk⟩p(τk|θk) = a0 + 1
2
b0 +
θ2
k
2
.
(21)
• M-step - evaluate:
∂log p(θ)
∂θk
= −Ep(τk|θk) [τk] θk.
(22)
The second derivative of the log-prior with respect to θ is obtained as:
∂2 log p(θ)
∂θk∂θl
=



−Ep(τk|θk) [τk] ,
if k = l
0,
otherwise.
(23)
The ARD choice of the hyper-parameters is a0 = b0 = 1.0 × 10−5. In similar settings, e.g.
coarse-graining of atomistic systems, the ARD prior identiﬁed the most salient features51,
whereas in this context it improves stability and turns oﬀunnecessary parameters for de-
scribing the training data.
F.
Approximate Bayesian inference for model parameters - Laplace’s
approximation
This subsection addresses the calculation of an approximate posterior of the model pa-
rameters θ. Thus far, we have considered point estimates of the model parameters θ (either
MLE or MAP). A fully Bayesian treatment however requires the evaluation of the normal-
ization constant of the exact posterior distribution p(θ|X) of the model parameters θ, which
is computationally impractical. We advocate an approximation to the posterior of θ that is
based on Laplace’s method77. The latter has been rediscovered as an eﬃcient approximation
for weight uncertainties in the context of neural networks in [102].
In Laplace’s approach, the exact posterior is approximated with a normal distribution
with mean θMAP and covariance the inverse of the negative Hessian of the log-posterior at
θMAP. Here, we assume a Gaussian with diagonal covariance matrix SL = diag(σ2
L) as
follows,
p(θ|X) ≈N
 µL, SL = diag(σ2
L)

,
(24)
with,
µL = θMAP,
(25)
16


## Page 17


and the diagonal entries of S−1
L ,
σ−2
L,k = −∂2L(φ, θ; X)
∂θ2
k

θMAP,φMAP
+ Ep(τk|θk)[τk],
(26)
where the term Ep(τk|θk)[τk] arises from the prior via Eq. (23). The quantities in Eqs. (25)
and (26) are obtained at the last iteration (upon convergence) of the Auto-Encoding Varia-
tional Bayes algorithm. We summarize the procedure in Algorithm 3.
Algorithm 3 Predictive Collective Variable Discovery.
Input Dataset X with N samples x(i) ∼ptarget(x).
1: {θ, φ} ←Specify the generative model pθ(z), pθ(x|z) Eq. (3) and the approximate posterior
of the latent CVs qφ(z|x) introduced in Eq. (8) with the corresponding parameters θ and φ,
respectively.
2: {θMAP, φMAP} ←Maximize the lower-bound in Eq. (8) with stochastic variational inference,
see Algorithm 1, and obtain the MAP estimates of the model parameters θ and φ.
3: p(θ|X) ←Perform approximate Bayesian inference for obtaining the posterior distribution of
the parameters of the generative model θ. See Section II F.
4: Predict the atomistic trajectory with Algorithm 2 for samples from the approximate posterior
of the generative model parameters θj ∼p(θ|X).
5: Estimate credible intervals of observables. This step is summarized in Algorithm 4.
Return Probabilistic estimates of observables accounting for epistemic uncertainty.
III.
NUMERICAL ILLUSTRATIONS
The following section is devoted to the application of the proposed procedure for identi-
fying collective variables of alanine dipeptide (ALA-2103,104) as well as of a longer peptide
i.e. ALA-15. We discuss the performance and robustness of the proposed methodology in
the presence of a small amount of training data and emphasize the predictive capabilities
of the model by the Ramachandran plot105 and the radius of gyration. The predictions are
augmented by error bars capturing epistemic uncertainty. The source code and data needed
to reproduce all results presented next are available at https://github.com/cics-nd/
predictive-cvs.
17


## Page 18


φ
ψ
(a) ALA-2 peptide with indicated dihedral
angels.
β-1
β-2
α
β-2
β-1
(b) Characteristic conformations
and their labelling as used in the
sequel.
FIG. 2. Deﬁnition of the dihedral angles and the labelling of characteristic modes as utilized in
this paper.
A.
ALA-2
1.
Simulation of ALA-2
Alanine dipeptide consists of 22 atoms leading to dim(x) = 66 in a Cartesian repre-
sentation comprising the coordinates of all atoms which we will use later on as the model
input. The actual degrees of freedom (DOF) are 60 after removing rigid-body motion. It is
well-known that ALA-2 exhibits distinct conformations which are categorized depending on
the dihedral angles (φ, ψ) (as indicated in Fig. 2(a)) of the atomistic conﬁguration. We label
the three characteristic modes as α, β-1, and β-2 in accordance with [106] (see Fig. 2(b)).
The procedure for generating the training data for ALA-2 is similar to that in [107].
The atoms of the alanine dipeptide interact via the AMBER ﬀ96108–110 force ﬁeld and we
employ an implicit water model based on generalized Born/solvent accessible surface area
model111,112.
However, we note that an explicit water model would better represent an
experimental environment. We employ an Andersen thermostat and the simulations were
carried out at constant temperature T = 330 K using Gromacs113–119. The time step is
taken as ∆t = 1 fs with an equilibration phase of 50 ns. The training dataset consisted of
snapshots taken every 10 ps after the equilibration phase. Rigid-body motions have been
removed from the dataset.
18


## Page 19


For demonstrating the encoding into the latent CV space of atomistic conﬁgurations not
contained in the training dataset, we used a test dataset selected so that the dihedral angles
(φ, ψ) had values belonging to all three modes i.e. α, β-1, and β-2 (deﬁned in Fig. 2(b)).
2.
Model speciﬁcation
The model requires the speciﬁcation of three components. Two components are needed to
describe the generative model p(x|θ): the probabilistic mapping pθ(x|z) and the distribution
of the CVs pθ(z). The third component is the approximate posterior qφ(z|x) of the latent
CVs as shown in Eq. (8).
Following [53], the distribution of the CVs is taken to be a standard Gaussian,
pθ(z) = p(z) = N(z; 0, I).
(27)
The simplicity in the distribution in Eq. (27) is compensated by a ﬂexible mapping from z to
the atomistic coordinates x. This probabilistic mapping (decoder) is given by a parametrized
Gaussian as follows,
pθ(x|z) = N(x; µθ(z), Sθ),
(28)
where,
µθ(z) = f µ
θ (z),
(29)
is a non-linear mapping z 7→f µ
θ (z) (f µ
θ : RnCV 7→Rnf) parametrized by an expressive
multilayer perceptron120–122.
We consider a diagonal covariance matrix i.e. Sθ = diag(σ2
θ)94 where its entries σ2
θ,j are
treated as model parameters and do not depend on the latent CVs z. In order to ensure the
non-negativity of σ2
θ,j > 0 while performing unconstrained optimization, we operate instead
on log σ2
θ,j.
The approximate posterior qφ(z(i)|x(i)) of the latent variables (encoder, approximating
pθ(z(i)|x(i))) introduced in Eq. (8) is modeled by a Gaussian with ﬂexible mean and variance
represented by a neural network. For each pair of x(i), z(i) (for notational simplicity, we drop
the index (i)):
qφ(z|x) = N(z; µφ(x), Sφ(x))
(30)
where the covariance matrix is assumed to be diagonal i.e. Sφ(x) = diag
 σ2
φ(x)

. Further-
more µφ(x) and log σ2
φ(x) are taken as the outputs of the encoding neural networks f µ
φ(x)
19


## Page 20


and f σ
φ (x), respectively:
µφ(x) = f µ
φ(x)
and
log σ2
φ(x) = f σ
φ (x).
(31)
We provide further details later in this section along with the structure of the employed
networks. In our model, we assume a diagonal Gaussian approximation for qφ(z|x).
We are aware that the actual, but intractable, posterior pθ(z|x) could diﬀer from a diag-
onal Gaussian and even from a multivariate normal distribution. However, the low variance
σ2
φ observed in test cases justiﬁes the assumption of a diagonal Gaussian in this context.
An enriched model for the approximate posterior qφ(z|x) over the CVs could rely on e.g.
normalizing ﬂows123. Recent developments on autoregressive ﬂows124 overcome the practical
restriction of normalizing ﬂows to low-dimensional latent spaces. This discussion equally
holds for the assumption of a Gaussian with diagonal covariance matrix for the genera-
tive distribution pθ(x|z). In the latter case, the diagonal entries of the covariance matrix
Sθ = diag(σ2
θ) were modeled as parameters independent of z. Either using Sθ = diag(σ2
θ)
or introducing a dependency on the latent CVs, Sθ(z) = diag(σ2
θ(z)) does not inﬂuence
the predictive quality in terms of observables and predicted atomistic conﬁgurations. This
statement is particularly valid when an expressive model for the mean µθ(z) in pθ(x|z) (as
in this work) is considered. It would be of interest employing more complex noise models for
pθ(x|z) which e.g. could be achieved by a Cholesky parametrization125. This might reveal
structure correlations while reducing the need for higher complexity in µθ(z).
As noted in Eq. (17), we employ the reparametrization trick by writing each random
variable z(i,l) ∼qφ(z(i)|x(i)) as
z(i,l) = gφ(ϵ(l); x(i)) = µφ(x(i)) + σφ(x(i)) ⊙ϵ(l),
(32)
and
ϵ(l) ∼p(ϵ) = N(0, I),
(33)
where ⊙denotes element-wise vector product.
We utilize the following structure for the decoding neural network f µ
θ (z):
f µ
θ (z) =

l(4)
θ ◦˜a(3) ◦l(3)
θ ◦˜a(2) ◦l(2)
θ ◦˜a(1) ◦l(1)
θ

(z).
(34)
The encoding networks for obtaining µφ(x) and σ2
φ(x) of the approximate posterior
qθ(z|x) over the latent CVs share the structure,
fφ(x) =

a(3) ◦l(3)
φ ◦a(2) ◦l(2)
φ ◦a(1) ◦l(1)
φ

(x),
(35)
20


## Page 21


which gives rise to f µ
φ(x) and f σ
φ (x) with,
f µ
φ(x) = l(4)
φ (fφ(x))
and
f σ
φ (x) = l(5)
φ (fφ(x)) .
(36)
In Eqs. (34)-(36), we consider linear layers l(i) of a variable y with l(i)(y) = W (i)y + b(i)
and non-linear activation functions denoted with a(·). The indices φ and θ of the linear
layers l(i) reﬂect correspondence to either the encoding or decoding network, respectively.
φ comprises all parameters of the encoding networks f µ
φ(x) and f σ
φ (x), θ all parameters
of the decoding network fθ(z) including the parameters σ2
θ discussed in Eq. (28).
We
diﬀerentiate the encoding and decoding activation functions by denoting them as a(i) and
˜a(i), respectively. All layers considered were fully connected. The general architecture of
the neural networks employed and how these aﬀect the objective L(θ, φ; X) are depicted in
Fig. 3.
The optimization of the objective is carried out by a stochastic gradient ascent algorithm.
In our case, we employ ADAM93 with the parameters chosen as α = 0.001, β1 = 0.9, β2 =
0.999, ϵADAM = 1.0 × 10−8. Gradients of the lower-bound L(θ, φ; X) with respect to the
model parametrization {φ, θ} are estimated by the backpropagation procedure120.
The
required gradients for optimizing the parameters σ2
θ can be computed analytically. For an
entry σ2
j,θ, we can write the following:
∂L(θ, φ; x(i))
∂log σ2
j,θ
= ∂log pθ(x(i)|z)
∂log σ2
j,θ
=
∂
∂log σ2
j,θ


−1
2
dim(x(i))
X
j=1

x(i)
j −µj,θ(z)
2
σ2
j,θ



=
∂
∂log σ2
j,θ


−1
2
dim(x(i))
X
j=1

x(i)
j −µj,θ(z)
2
exp
 log
 σ2
j,θ




= 1
2

x(i)
j −µj,θ(z)
2
σ2
j,θ
.
(37)
Studying diﬀerent combinations of activation functions and layers for the encoding net-
work f µ,σ
φ
(x) and decoding network f µ
θ (z) led to the network architecture depicted in Ta-
bles I and II, respectively. This network provided a repeatedly stable optimization during
training. Variations of the given network architecture resulted into similar predictive ca-
pabilities as shown in Fig. 4. Stability is not limited to symmetric encoding and decoding
21


## Page 22


l(1)
φ
a(1)
l(2)
φ
a(2)
l(3)
φ
a(3)
x(i)
l(4)
φ
µφ(x(i))
l(5)
φ
log σ2
φ(x(i))
qφ(z(i)|x(i)) = N
 z(i)|µφ(x(i)), Sφ(x(i))

l(1)
θ
˜a(1)
l(2)
θ
˜a(2)
l(3)
θ
˜a(3)
l(4)
θ
µθ(z)
z ∼pθ(z)
pθ(x|z) = N (x|µθ(z), Sθ)
L(θ, φ; X) = PN
i=1 Eqφ(z(i)|x(i))[log pθ(x(i)|z(i))] −PN
i=1 DKL
 qφ(z(i)|x(i))||pθ(z)

Encoder
Decoder
FIG. 3. Schematic of the AEVB depicting the employed network architecture. Fully connected
linear layers are denoted with l(i) and non-linear activation functions with a(i). The indices φ and
θ indicate encoding and decoding networks, respectively. The maximization of the lower-bound on
the marginal log-likelihood L(θ, φ; X) in Eq. (11) simultaneously optimizes the parametrization
of the encoder and decoder. The ﬁrst term in L(θ, φ; X) accounts for the reconstruction of the
training data x(i) with z(i) distributed according qφ(z(i)|x(i)). The second term, in aggregation of
all data x(i), ensures that qφ(z(i)|x(i)) is close to p(z).
activation functions. An automated approach for selecting or learning the best architecture
is an active research area127. Increasing the dimension of z did not improve the predictive
capabilities as shown in Fig. 5. This implies that CVs with dim(z) = 2 suﬃce to capture
the physics encapsulated in the ALA-2 dataset with dim(x) = 66 or 60 DOF.
22


## Page 23


2.0
2.1
2.2
2.3
2.4
2.5
2.6
2.7
2.8
Rg[ ]
0
2
4
6
8
10
p(Rg)
Reference
100-50-100
50-50-50
50-100-100
100-100-100
(a) Varying dimensionality of the layers
l(i)
{θ,φ}. The ﬁgure’s labels represent the
dimensionality of the layers in the format
d1-d2-d3 as speciﬁed in Tables I and II. We
use the activation functions as denoted in the
tables.
2.0
2.1
2.2
2.3
2.4
2.5
2.6
2.7
2.8
Rg[ ]
0
2
4
6
8
10
p(Rg)
Reference
s-s-ls-t-t-t
s-ls-ls-t-ls-t
s-ls-ls-t-t-t
s-s-ls-t-ls-t
(b) Testing diﬀerent activation functions
for a(i). The labels specify the utilized
activation functions in the following
manner: a(1)-a(2)-a(3)-˜a(1)-˜a(2)-˜a(3). We use
the abbreviations: t: Tanh, s: SeLu, ls: Log
Sigmoid.
FIG. 4. Prediction of the radius of gyration with diﬀering networks, in terms of (a) the dimen-
sionality of the layers and (b) regarding the type of activation functions used. Changes in the
network speciﬁcation lead to similar predictions. This model has been trained with a dataset of
size N = 500.
2.0
2.1
2.2
2.3
2.4
2.5
2.6
2.7
2.8
Rg[ ]
0
2
4
6
8
10
p(Rg)
Reference
dim(z) =2
dim(z) =4
dim(z) =6
FIG. 5. Predicted radius of gyration for models utilizing diﬀerent dim(z). The predictions are
based on a model as speciﬁed in Tables I and II with N = 500.
23


## Page 24


Linear layer Input dimension Output dimension Activation layer Activation function
l(1)
φ
dim(x)
d1
a(1)
SeLua
l(2)
φ
d1
d2
a(2)
SeLu
l(3)
φ
d2
d3
a(3)
Log Sigmoid b
l(4)
φ
d3
dim(z)
None
-
l(5)
φ
d3
dim(z)
None
-
a SeLu: a(x) =







α(ex −1)
if x < 0
x
otherwise.
See [126] for further details.
b Log Sigmoid: a(x) = log
1
1+e−x
TABLE I. Network speciﬁcation of the encoding neural network with d1 = 50, d2 = 100, and
d3 = 100.
Linear layer Input dimension Output dimension Activation layer Activation function
l(1)
θ
dim(z)
d3
˜a(1)
Tanh
l(2)
θ
d3
d2
˜a(2)
Tanh
l(3)
θ
d2
d1
˜a(3)
Tanh
l(4)
θ
d1
dim(x)
None
-
TABLE II. Network speciﬁcation of the decoding neural network with d{1,2,3} as deﬁned in Table I.
3.
Results
In the following illustrations, we trained the model by varying the number of snapshots
N. We utilized a sub-sampled batch of size M = 64 from the dataset of size N. In cases
where N < 64, we set M = N. The hyper parameters of the ARD prior in Eq. (20) are set
to a0 = b0 = 1.0 × 10−5. Other values for a0, b0 in the range of [1.0 × 10−8, 1.0 × 10−4] were
also employed without a signiﬁcant eﬀect on the obtained sparsity patterns or the predictive
accuracy of the model.
Figure 6 depicts the z-coordinates of N = 500 training data as well as those of 1527 test
data which have been classiﬁed into the three modes based on the values of the dihedral
angles (see Fig. 2(b)). In order to obtain the z-coordinates of the test data, we made use of
the mean µφ(x(i)) of the inferred approximate posterior qφ as obtained after training. The
24


## Page 25


−4
−3
−2
−1
0
1
2
3
4
z1
−4
−3
−2
−1
0
1
2
3
4
z2
α
β-1
β-2
Training Data
FIG. 6. Representation of the z-coordinates of the training data X with N = 500 in the CV
space (yellow diamonds). Using the trained model and the mean of qφ(z|z) we computed the z-
coordinates of 1527 test samples corresponding to diﬀerent conformations of the alanine dipeptide
to α (black), β-1 (blue), and β-2 (red). Without any prior physical information, the encoder yields
three distinct clusters in the CV space.
resulting picture essentially provides the pre-images of the atomistic conﬁgurations in the
CV space. Interestingly, similar atomistic conﬁgurations, i.e. belonging to one of the three
modes, α, β-1, β-2, are recognized by qφ(z|x) and mapped to clusters in the identiﬁed CV
space. β-1 conﬁgurations are encoded by qφ(z|x) to regions with high probability mass in
pθ(z), i.e. CVs z close to the center of pθ(z) = N(0, I) are assigned. This is in accordance
with the reference Boltzmann distribution p(x) where β-1 is the most probable conformation.
Various dimensionality reduction methods are designed in order to keep similar x close
in their embedding on the lower-dimensional CV manifold, e.g., multidimensional scaling30
or ISOMAP33. In the presented scheme, the generative model learns that mapping similar
x to similar z leads to an expressive (in terms of the marginal likelihood) lower-dimensional
representation. This similarity is revealed by inferring the approximate latent variable pos-
terior qφ(z|x). Therefore, the desired similarity mentioned in [13] between conﬁgurations in
the atomistic representation x and via qφ(z|x) in the assigned CVs z is achieved.
25


## Page 26


In contrast to several other dimensionality reduction techniques (e.g. Isomap33 and Dif-
fusion maps38–41), which as mentioned in the introduction require large amounts of training
data e.g. N > 10 00013,49, the proposed method can perform well in the small data regime,
e.g. for N = 50 as shown in Fig. 7. The latter depicts the Ramachandran plot in terms of
the dihedral angles based on various amounts of training data N and compares it with the
one predicted by the trained model on the same N as well as with the reference (obtained
with N = 10 000). We note that the trained model yields Ramachandran plots that more
closely resemble the reference as compared to the ones computed by the training data alone.
The encoder, trained with N = 200, is capable of generating atomistic conﬁgurations leading
to (φ, ψ) tuples which are not included in the training data.
The ARD prior in Eq. (20) drives 58% of the parameters θ to zero (as a threshold, we
consider a parameter to be inactive when its value drops below 1.0 × 10−4). In contrast,
all network parameters θ remain active while optimizing the objective without the ARD
prior. Apart from the qualitative advantage, the sparsity-inducing prior provides a strong
regularization in the presence of limited data and yields superior predictive estimates. In
addition to obtaining sparse solutions, the ARD prior facilitates the identiﬁcation of phys-
ically meaningful latent representations for limited data (e.g. N = 50) as shown in Fig. 8.
Without the ARD prior, the data is encoded in a rather small region of the latent space.
In Fig. 9, we attempt to provide insight on the physical meaning of the CVs z identiﬁed.
In particular, we plot the atomistic conﬁgurations x corresponding to various values of the
ﬁrst CV z1 while keeping z2 = 0.
The conformational transition in predicted atomistic
conﬁgurations can be clearly recognized in the peptides of Fig. 9. We note that we start on
the left (z1 < 0) with α conﬁgurations, then move towards β-1 (starting at z1 ≈−1), and
ﬁnally obtain β-2 conﬁgurations. For illustration purposes, the predictions in
Fig. 9 are
based solely on the mean µθ(z) of the probabilistic decoder pθ(x|z) = N(x; µθ(z), Sθ =
diag(σ2
θ)). We note that for each value of the CVs z several atomistic realizations x can
be drawn from pθ(x|z) as depicted in Fig. 10. This ﬁgure reveals the characteristic and
relevant movement of the backbone that is captured by the predictive mean µθ(z) = f µ
θ (z).
Fluctuations of less relevant outer Hydrogen atoms (see Figs. 10(b)-10(d)) are recognized as
noise of the decoder pθ(x|z) = N (µ(z), Sθ = diag(σ2
θ)) denoted in Eq. (28). We note also
that the corresponding entries of σθ responsible for the outer Hydrogen atoms are ﬁve times
larger compared to the remaining atoms. The proposed model can therefore in unsupervised
26


## Page 27


150
100
50
0
50
100
150
ψ [°]
Training Data
N = 50
Prediction
Reference
150
100
50
0
50
100
150
ψ [°]
N = 100
150
100
50
0
50
100
150
ψ [°]
N = 200
150 100
50
0
50
100 150
φ [°]
150
100
50
0
50
100
150
ψ [°]
N = 500
150 100
50
0
50
100 150
φ [°]
150 100
50
0
50
100 150
φ [°]
FIG. 7. Ramachandran plots estimated with the training data X (left column), using predictions of
the trained model (middle column), and the reference (right column, estimated with N = 10 000).
Each row refers to diﬀerent size N of training datasets (the ﬁgure on the right column is repeated to
allow easy comparison with the results on the ﬁrst two columns). The represented predictions are
obtained by applying Algorithm 2 with T = 10 000 samples. The generative nature of the model
allows more accurate estimates than when using the training data alone. In addition, the Bayesian
approach allows for predictions with their associated uncertainties as discussed subsequently.
fashion identify the central role of the backbone coordinates whereas this physical insight is
pre-assumed in [8 and 68].
In order to gain further insight into the relation between the dihedral angles φ, ψ and the
discovered CVs z, we plot in Figs. 11 and 12 the corresponding maps for various combinations
of z-values. While it is clear that the map is not always bijective, the ﬁgures reveal the strong
correlation between the two sets of variables. It should also be noted that in contrast to
27


## Page 28


−4
−3
−2
−1
0
1
2
3
4
z1
−4
−3
−2
−1
0
1
2
3
4
z2
α
β-1
β-2
Training Data
(a) Active ARD prior.
−4
−3
−2
−1
0
1
2
3
4
z1
−4
−3
−2
−1
0
1
2
3
4
z2
α
β-1
β-2
Training Data
(b) Without ARD prior.
FIG. 8.
Representation of the z-coordinates of the training data X with N = 50 in the CV
space (yellow diamonds). Using the trained model and the mean of qφ(z|z) we computed the z-
coordinates of 1527 test samples corresponding to diﬀerent conformations of the alanine dipeptide
to α (black), β-1 (blue), and β-2 (red).
In the case of limited training data, the ARD prior
facilitates the identiﬁcation of physically meaningful CVs (left) compared to the representation on
the right obtained without the ARD prior. Note that the changed positioning of the conformations
in the CV space compared to Fig. 6 is due to symmetries in pθ(z).
the dihedral angles, the z value for a given atomistic conﬁguration x are not unique but
rather there is a whole distribution as implied by qφ(z|x). For the aforementioned plots we
computed the z from the mean of this density, i.e. µφ(x).
The trained model can also be employed in computing predictive estimates of observables
R
a(x) ptarget(x) dx by making use of pθ(x) and samples drawn from it as described in
Section II D. We illustrate this by computing the radius of gyration (Rg)107,129 given as,
aRg(x) =
sP
p mp||xp −xCOM||2
P
p mp
.
(38)
The sum in Eq. (38) considers all atoms p = 1, . . . , P of the peptide, where mp and xp
denote the mass and the coordinates of each atom, respectively. xCOM denotes the center
of mass of the peptide. The histogram of aRg(x) reﬂects the distribution of the size of the
peptide and is correlated with the various conformations129.
In the estimates that we depict in Fig. 13, we have also employed the posterior approxi-
mation of the model parameters θ obtained as described in Section II F in order to compute
28


## Page 29


φ = -52.1°
ψ = 116.0°
φ = -41.8°
ψ = 106.4°
φ = -45.0°
ψ = -47.0°
φ = -57.0°
ψ = -45.2°
φ = -136.1°
ψ = -70.9°
φ = -143.2°
ψ = 160.6°
φ = -98.1°
ψ = 144.3°
φ = -57.8°
ψ = 133.7°
FIG.
9.
Predicted
conﬁgurations
x
(including
dihedral
angle
values)
for
{z|z1
=
{−3.5, −2.5, . . . , 3.5}, z2 = 0} with µθ(z) of pθ(x|z).
As one moves along the z1 axis, we ob-
tain for the given CVs atomistic conﬁgurations x reﬂecting the conformations α, β-1, and β-2. All
rendered atomistic representations in this work are created by VMD128.
credible intervals for the observable. These credible intervals are estimated as described in
Algorithm 4 utilizing J = 3000 samples. We observe that the model’s predictive conﬁdence
increases with the size of the training data. This is reﬂected in shrinking credible intervals
in Fig. 13 for increasing N.
29


## Page 30


(a) Mean prediction µθ(z0) for a
sample z0 ∼p(z).
(b) Realization x0,0 ∼
pθ(x|µθ(z0), Sθ = diag(σ2
θ)).
(c) Realization x1,0 ∼
pθ(x|µθ(z0), Sθ = diag(σ2
θ)).
(d) Realization x2,0 ∼
pθ(x|µθ(z0), Sθ = diag(σ2
θ)).
FIG. 10. Visualization of the mean prediction (a) for a sample z0 ∼p(z), obtained from the
decoding network µθ(z0) = fθ(z0), and realizations (b-d) xj,0 ∼pθ(x|z0). Less relevant positions
of the outer Hydrogen atoms are captured by the noise σθ of the model pθ(x|z0) = N(µ(z0
θ), Sθ =
diag(σ2
θ)).
Algorithm 4 Estimating Credible Intervals.
Input J the number of samples to be drawn, optimal values of θ = θMAP and φ = φMAP .
Compute Laplace’s approximation N(µL, SL = diag(σ2
L)) to the posterior p(θ|X) (Eq. (24)).
for j = 1 to J do
Draw a posterior sample: θj ∼N(µL, SL = diag(σ2
L)).
Obtain a predictive trajectory ¯xj
1:T , given the parametrization θj utilizing Algorithm 2.
Estimate the observable ˆa(θj) = 1
T
PT
t=1 a(¯xj
t), given the trajectory ¯xj
1:T .
end for
Estimate the desired quantiles with ˆa(θ1:J).
In summary for ALA-2, we note that the proposed methodology for identifying CVs
(Fig. 6) and predicting observables (Figs. 7 and 13) works well with small size datasets, e.g.
N = {50, 200, 500}.
30


## Page 31


4
2
0
2
4
z2
-135°
-90°
-45°
-45°
0°
0°
5°
4
2
0
2
4
z1
4
2
0
2
4
z2
-135°
-90°
-45°
0°
45°
45°
90°
90°
135°
-180°
-135°
-90°
-45°
0°
45°
90°
135°
180°
,
FIG. 11. Predicted dihedral angles (φ, ψ) given the latent variables z ∈[−4, 4]2.
4
2
0
2
4
z1 at z2 = 0
-100°
0°
100°
200°
300°
,
(a)
4
2
0
2
4
z2 at z1 = 0
-100°
0°
100°
200°
300°
,
(b)
FIG. 12. Predicted dihedral angles (φ, ψ) given the latent variables (a) {z1, z2|z1 ∈[−4, 4], z2 = 0}
and (b) {z1, z2|z1 = 0, z2 ∈[−4, 4]}.
B.
ALA-15
1.
Simulation of ALA-15 and model speciﬁcation
The following example considers a larger alanine peptide with 15 residues, ALA-15 which
consists of 162 atoms giving rise to dim(x) = 486 with 480 DOF. The reference dataset
X has been obtained in a similar manner as speciﬁed in Section III A 1 with the only
diﬀerence being that we utilize a replica-exchange molecular dynamics130 algorithm with 21
31


## Page 32


2.0
2.1
2.2
2.3
2.4
2.5
2.6
2.7
2.8
Rg[ ]
0
2
4
6
8
10
p(Rg)
Reference
MAP
5% - 95% Credible interval
(a) N = 50.
2.0
2.1
2.2
2.3
2.4
2.5
2.6
2.7
2.8
Rg[ ]
0
2
4
6
8
10
p(Rg)
Reference
MAP
5% - 95% Credible interval
(b) N = 200.
2.0
2.1
2.2
2.3
2.4
2.5
2.6
2.7
2.8
Rg[ ]
0
2
4
6
8
10
p(Rg)
Reference
MAP
5% - 95% Credible interval
(c) N = 500.
FIG. 13. Predicted radius of gyration with dim(z) = 2 for various sizes N of the training dataset.
The MAP estimate indicated in red is compared to the reference (black) solution. The latter is
estimated by N = 10 000. The shaded area represents the 5%-95% credible interval, reﬂecting the
induced epistemic uncertainty from the limited amount of training data.
temperature replicas distributed according to Ti = T0eκ·i (T0 = 270 K, and κ = 0.04). This
leads to an analogous simulation setting as employed in [107]. The datasets are obtained
as mentioned in the previous example. We consider here N = {300, 3000, 5000}. Using the
same model speciﬁcations as in Section III A 2, we present next a summary of the obtained
results.
2.
Results
For visualization purposes of the latent CV space, we assumed dim(z) = 2 in the follow-
ing, even though the presence of 15 residues each requiring a pair of dihedral angles (φ, ψ)
would potentially suggest a higher-dimensional representation. However, when considering
test cases with dim(z) = {15, 30}, no signiﬁcant diﬀerences were observed in the predictive
capabilities. This is in agreement with [131] where it is argued based on density functional
theory calculations that not all dihedral angles are equally relevant. The (φ, ψ) pairs within
a peptide chain show high correlation. Mulitlayer neural networks provide the capability of
transforming independent CVs (as considered in this study) to correlated ones by passing
them through the subsequent network layers. This explains the reasonable predictive quality
of the model using independent and low-dimensional CVs with dim(z) = 2. Considering
more expressive pθ(z) than the standard Gaussian employed, could have accounted (in part)
for such correlations. In this example, by employing the ARD prior, only 43% of the decoder
32


## Page 33


parameters θ remained eﬀective.
Figure 14 depicts the posterior means of the N = 3000 training data in the CV space z.
Given that a peptide conﬁguration contains residues from diﬀerent conformations labelled
here as α, β-1, and β-2 and residues in intermediate (φ, ψ) states, we applied the following
rule for labelling/coloring each datapoint. The assigned color in Fig. 14 is a mixture between
the RGB colors black (for α), blue (for β-1), and red (for β-2). The mixture weights of the
assigned color are proportional to the number of residues belonging to the α (black), β-1
(blue), and β-2 (red) conformations, normalized by the total amount of residues which can
be clearly assigned to α, β-1, and β-2. Additionally, we visualize the amount of intermediate
(φ, ψ) states of the residues by the opacity of the scatter points. The opacity reﬂects the
amount of residues which are clearly assigned to the α, β-1, and β-2 conformations compared
to the total amount of residues in the peptide. For example, if all residues of a peptide
conﬁguration correspond to a speciﬁc mode, the opacity is taken as 100%. If all residues are
in non-classiﬁed intermediate states, the opacity is set to the minimal value which is here
taken as 20%.
We note that peptide conﬁgurations in which the majority of residues belong to β-1 (blue)
or in the β-2 conformation (red), are clearly separated in the CV space from datapoints with
residues predominantly in the α conformation (black). Nevertheless, we observe that the
encoder has diﬃculties separating blue (β-1) and red (β-2) datapoints. We remark though
that the related secondary structures132 resulting from the assembly of residues in β-1 and
β-2, such as the β-sheet and β-hairpin, share a similar atomistic representation x which
explains the similarity in the CV space.
When one moves in the CV space z along the path indicated by a red dashed line in Fig. 15
and reconstructs the corresponding x using the mean function of the decoder pθ(x|z), we
obtain atomistic conﬁgurations of the ALA-15 partially consisting of the conformations α,
β-1, and β-2 which correspond to the aforementioned secondary structures i.e. β-sheet (top
left), β-hairpin (top middle and right), and α-helix (bottom row).
The ambiguity between β-1 and β-2 states is also reﬂected in the predicted Ramachandran
plot in Fig. 16. Nevertheless properties, independent of the explicit separation of conﬁgu-
rations predominantly consisting of residues in β-1 and β-2 states, are predicted accurately
by the framework. This is demonstrated with the computed radius of gyration in Fig. 17.
The MAP estimate is complemented by the credible intervals which reﬂect the epistemic
33


## Page 34


−4
−3
−2
−1
0
1
2
3
4
z1
−4
−3
−2
−1
0
1
2
3
4
z2
α
β-1
β-2
FIG. 14. Representation of the training data X with N = 3000 in the encoded collective variable
space. The inferred approximate posterior qφ(z|x) of the latent CVs separates residues mostly
belonging to the β conformations (mixture of red and blue) and peptide conﬁgurations containing
largely residues in the α conﬁguration (black). Here, the mean µφ(x) of the approximate posterior
qφ(z|x) = N(x; µφ(x), Sφ = diag(σ2
φ(x))) is depicted.
uncertainty and are able to envelop the reference proﬁle. As in the previous example, the
breadth of the credible intervals shrinks with increasing training data N.
IV.
CONCLUSIONS
We presented an unsupervised learning scheme for discovering CVs of atomistic systems.
We deﬁned the CVs as latent generators of the atomistic conﬁgurations and formulated
their identiﬁcation as a Bayesian inference task. Inference of the posterior distribution of
34


## Page 35


FIG. 15.
Predicted conﬁgurations x for decoding CVs indicated as red points on the dashed
line in the plot. Depicted conﬁgurations have been produced by evaluating the mean µθ(z) of
pθ(x|z). Moving along the path, we obtain atomistic conﬁgurations x partially consisting of the
conformations α, β-1, and β-2 in the ALA-15 peptide resulting into peptide secondary structures
such as β-sheet (top left), β-hairpin (top middle and right), and α-helix (bottom row).
the latent CVs given the ﬁne-scale atomistic training data identiﬁes a probabilistic mapping
from the space of atomistic conﬁgurations to the latent space. This posterior distribution
resembles a dictionary translating atomistic conﬁgurations to the lower-dimensional CV
space which is inferred during the training procedure. Compared to other dimensionality
reduction methods, the proposed scheme is capable of performing well with comparably
heterogeneous and small datasets.
We presented the capabilities of the model for the test case of an ALA-2 peptide (Sec-
tion III). When the dimensionality of the CVs dim(z) was set to 2, the model discovered
variables that correlate strongly with the widely known dihedral angles (φ, ψ). Other di-
mensionality reduction methods26,30,31,33,38,39,41 rely on an objective keeping small distances
35


## Page 36


150 100
50
0
50
100 150
φ [°]
150
100
50
0
50
100
150
ψ [°]
N = 300
150 100
50
0
50
100 150
φ [°]
N = 3000
150 100
50
0
50
100 150
φ [°]
N = 5000
150 100
50
0
50
100 150
φ [°]
Reference
FIG. 16. Predicted Ramachandran plots with dim(z) = 2 for various sizes N of the training dataset
(ﬁrst three plots from the left). Depicted predictions are MAP estimates based on T = 10 000
samples. The plot on the right is the reference MD prediction with N = 10 000 conﬁgurations.
4
5
6
7
8
9
10
Rg[ ]
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
p(Rg)
Reference
MAP
1% - 99% Credible interval
(a) N = 300.
4
5
6
7
8
9
10
Rg[ ]
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
p(Rg)
Reference
MAP
1% - 99% Credible interval
(b) N = 3000.
4
5
6
7
8
9
10
Rg[ ]
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
p(Rg)
Reference
MAP
1% - 99% Credible interval
(c) N = 5000.
FIG. 17. Predicted radius of gyration with dim(z) = 2 for various sizes N of the training dataset.
The MAP estimate indicated in red is compared to the reference (black) solution. The latter is
estimated by N = 10 000. The shaded area represents the 1%-99% credible interval, reﬂecting the
induced epistemic uncertainty from the limited amount of training data.
between conﬁgurations in the atomistic space also small in the latent space. Rather than
enforcing this requirement directly, the proposed framework identiﬁes a lower-dimensional
representation that clusters conﬁgurations in the CV space which show similarities in the
atomistic space. The Bayesian formulation presented allows for a rigorous quantiﬁcation
of the unavoidable uncertainties and their propagation in the predicted observables. The
ARD prior chosen was shown to lead to on average 45% less parameters compared to the
optimization without it.
We presented an approach for approximating the intractable posterior of the decoding
model parameters (Eq. (24)) and provided an algorithm (Algorithm 4) for estimating credible
intervals. The uncertainty propagated to the observables captures the parameter uncertainty
36


## Page 37


of the decoding neural network f µ
θ (z).
In addition to discovering CVs, the generative model employed is able to predict atomistic
conﬁgurations by sampling the CV space with pθ(z) and mapping the CVs probabilistically
via pθ(x|z) to full atomistic conﬁgurations. We showed that the predictive mapping pθ(x|z)
recognizes essential backbone behavior of the peptide while it models ﬂuctuations of the outer
Hydrogen atoms with the noise of pθ(x|z) (see Fig. 10). We use the model for predicting
observables and quantifying the uncertainty arising from limited training data.
We emphasize that the whole work was based on data represented by Cartesian coordi-
nates x of all the atoms of the ALA-2 (dim(x) = 66, and 60 DOF adjusted by removing
rigid-body motion) and ALA-15 (dim(x) = 486, and 480 DOF adjusted by removing rigid-
body motion) peptides.
Considering a pre-processed dataset e.g.
by considering solely
coordinates of the backbone atoms, heavy atom positions, or a representation by dihedral
angles assumes the availability of tremendous physical insight. The aim of this work was
to reveal CVs with physicochemical meaning and the prediction of observables of complex
systems without using any domain-speciﬁc physical notion.
Besides the framework proposed, generative adversarial networks (GANs)133 and its
Bayesian reformulation in [134] open an additional promising avenue in the context of CV
discovery and enhanced sampling of atomistic systems. GANs are accompanied by a two
player (generator and discriminator) min-max objective which poses known diﬃculties in
training the model. The training of GANs is not as robust as the VAE employed here and
Bayesian formulations are not well studied. In addition, one needs to address the mode
collapse issue (see [135]) which is critical for atomistic systems.
Future work involves the use of the CVs discovered in the context of enhanced sampling
techniques that can lead to an accelerated exploration of the conﬁgurational space.
In
addition to identifying good CVs, a crucial step for enhanced sampling methods is the
biasing potential for lifting deep free-energy wells. In contrast to the ideas e.g. presented
in [8, 9, 136], we would advocate a formulation where the biasing potential is based on
the lower-dimensional pre-image of the currently visited free-energy surface. To that end,
we envision using the posterior distribution qφ(z|x) to construct a locally optimal biasing
potential deﬁned in the CV space which gets updated on the ﬂy as the simulations explore the
conﬁguration space. The biasing potential can be transformed by the probabilistic mapping
37


## Page 38


of the generative model pθ(x|z) to the atomistic description as follows,
U x(i)
bias(x) ∝−log
Z
MCV
pθ(x|z)qφ(z|x(i)) dz.
(39)
Equation (39) is diﬀerentiable with respect to atomistic coordinates. Subtracting it from
the atomistic potential could accelerate the simulation by “ﬁlling-in” the deep free-energy
wells.
ACKNOWLEDGEMENTS
The authors acknowledge support from the Defense Advanced Research Projects Agency
(DARPA) under the Physics of Artiﬁcial Intelligence (PAI) program (contract HR00111890034).
M.S. gratefully acknowledges the non-material and ﬁnancial support of the Hanns-Seidel-
Foundation, Germany funded by the German Federal Ministry of Education and Research.
M.S. likewise acknowledges the support of NVIDIA Corporation.
REFERENCES
1J. R. Perilla, B. C. Goh, C. K. Cassidy, B. Liu, R. C. Bernardi, T. Rudack, H. Yu, Z. Wu,
and K. Schulten, Current Opinion in Structural Biology 31, 64 (2015).
2P. Koutsourelakis, N. Zabaras, and M. Girolami, Journal of Computational Physics 321,
1252 (2016).
3A. Barducci, M. Bonomi, and M. Parrinello, Wiley Interdisciplinary Reviews: Compu-
tational Molecular Science 1, 826 (2011).
4F. Pietrucci and W. Andreoni, Phys. Rev. Lett. 107, 085504 (2011).
5A. L. Ferguson, A. Z. Panagiotopoulos, P. G. Debenedetti,
and I. G. Kevrekidis, The
Journal of Chemical Physics 134, 135103 (2011), https://doi.org/10.1063/1.3574394.
6W. Zheng, M. A. Rohrdanz, and C. Clementi, The Journal of Physical Chemistry B 117,
12769 (2013), pMID: 23865517, https://doi.org/10.1021/jp401911h.
7O. Valsson and M. Parrinello, Phys. Rev. Lett. 113, 090601 (2014).
8W. Chen and A. L. Ferguson, Journal of Computational Chemistry 39, 2079 (2018),
https://onlinelibrary.wiley.com/doi/pdf/10.1002/jcc.25520.
9P.-Y. Chen and M. E. Tuckerman, The Journal of Chemical Physics 148, 024106 (2018),
https://doi.org/10.1063/1.4999447.
38


## Page 39


10A. Mitsutake, Y. Mori, and Y. Okamoto, “Enhanced sampling algorithms,” in Biomolecu-
lar Simulations: Methods and Protocols, edited by L. Monticelli and E. Salonen (Humana
Press, Totowa, NJ, 2013) pp. 153–195.
11C. Bierig and A. Chernov, Journal of Computational Physics 314, 661 (2016).
12J. Luque and X. Barril, eds., Physico-Chemical and Computational Approaches to Drug
Discovery, RSC Drug Discovery (The Royal Society of Chemistry, 2012) pp. FP001–418.
13M. A. Rohrdanz, W. Zheng, and C. Clementi, Annual Review of Physical Chemistry 64,
295 (2013), pMID: 23298245, https://doi.org/10.1146/annurev-physchem-040412-110006.
14G. Torrie and J. Valleau, Journal of Computational Physics 23, 187 (1977).
15A.
F.
Voter,
The
Journal
of
Chemical
Physics
106,
4665
(1997),
https://doi.org/10.1063/1.473503.
16D. Hamelberg, J. Mongan, and J. A. McCammon, The Journal of Chemical Physics 120,
11919 (2004), https://doi.org/10.1063/1.1755656.
17T. Huber, A. E. Torda, and W. F. van Gunsteren, Journal of Computer-Aided Molecular
Design 8, 695 (1994).
18H. Grubm¨uller, Phys. Rev. E 52, 2893 (1995).
19A. Laio and M. Parrinello, Proceedings of the National Academy of Sciences 99, 12562
(2002), http://www.pnas.org/content/99/20/12562.full.pdf.
20A.
Barducci,
M.
Bonomi,
and
M.
Parrinello,
Wiley
Interdisci-
plinary
Reviews:
Computational
Molecular
Science
1,
826
(2011),
https://onlinelibrary.wiley.com/doi/pdf/10.1002/wcms.31.
21E. Darve, D. Rodr´ıguez-G´omez, and A. Pohorille, The Journal of Chemical Physics 128,
144120 (2008), https://doi.org/10.1063/1.2829861.
22J. H´enin, G. Fiorin, C. Chipot,
and M. L. Klein, Journal of Chemical Theory and
Computation 6, 35 (2010), pMID: 26614317, https://doi.org/10.1021/ct9004432.
23F. Pietrucci, Reviews in Physics 2, 32 (2017).
24A. C. Pan,
T. M. Weinreich,
Y. Shan,
D. P. Scarpazza,
and D. E. Shaw,
Journal of Chemical Theory and Computation 10, 2860 (2014), pMID: 26586510,
https://doi.org/10.1021/ct500223p.
25C. D. Fu, L. F. L. Oliveira, and J. Pfaendtner, Journal of Chemical Theory and Com-
putation 13, 968 (2017), pMID: 28212010, https://doi.org/10.1021/acs.jctc.7b00038.
26H. Hotelling, J. Educ. Psych. 24 (1933).
39


## Page 40


27R. T. McGibbon, B. E. Husic, and V. S. Pande, The Journal of Chemical Physics 146,
044109 (2017), https://doi.org/10.1063/1.4974306.
28A.
Amadei,
A.
B.
M.
Linssen,
and
H.
J.
C.
Berendsen,
Pro-
teins:
Structure,
Function,
and
Bioinformatics
17,
412
(1993),
https://onlinelibrary.wiley.com/doi/pdf/10.1002/prot.340170408.
29K. Pearson, The London, Edinburgh, and Dublin Philosophical Magazine and Journal of
Science 2, 559 (1901), https://doi.org/10.1080/14786440109462720.
30J. M. Troyer and F. E. Cohen, Proteins: Structure, Function, and Bioinformatics 23, 97
(1995), https://onlinelibrary.wiley.com/doi/pdf/10.1002/prot.340230111.
31W. H¨ardle and L. Simar, Applied Multivariate Statistical Analysis (Springer Berlin Hei-
delberg, 2007).
32M. Ceriotti, G. A. Tribello, and M. Parrinello, Proceedings of the National Academy of
Sciences 108, 13023 (2011), http://www.pnas.org/content/108/32/13023.full.pdf.
33J. B. Tenenbaum, V. d. Silva,
and J. C. Langford, Science 290, 2319 (2000),
http://science.sciencemag.org/content/290/5500/2319.full.pdf.
34M. A. Rohrdanz, W. Zheng, M. Maggioni, and C. Clementi, The Journal of Chemical
Physics 134, 124116 (2011), https://doi.org/10.1063/1.3569857.
35M.
Balasubramanian
and
E.
L.
Schwartz,
Science
295,
7
(2002),
http://science.sciencemag.org/content/295/5552/7.full.pdf.
36D. L. Donoho and C. Grimes, Proceedings of the National Academy of Sciences 100, 5591
(2003), http://www.pnas.org/content/100/10/5591.full.pdf.
37H. Risken and T. Frank, The Fokker-Planck Equation: Methods of Solution and Applica-
tions (Springer Series in Synergetics) (Springer, 1996).
38R. R. Coifman, S. Lafon, A. B. Lee, M. Maggioni, B. Nadler, F. Warner,
and
S. W. Zucker, Proceedings of the National Academy of Sciences 102, 7426 (2005),
http://www.pnas.org/content/102/21/7426.full.pdf.
39R. R. Coifman, S. Lafon, A. B. Lee, M. Maggioni, B. Nadler, F. Warner,
and
S. W. Zucker, Proceedings of the National Academy of Sciences 102, 7432 (2005),
http://www.pnas.org/content/102/21/7432.full.pdf.
40A. L. Ferguson, A. Z. Panagiotopoulos, I. G. Kevrekidis, and P. G. Debenedetti, Chemical
Physics Letters 509, 1 (2011).
40


## Page 41


41B. Nadler, S. Lafon, R. R. Coifman, and I. G. Kevrekidis, Applied and Computational
Harmonic Analysis 21, 113 (2006), special Issue: Diﬀusion Maps and Wavelets.
42R. R. Coifman, I. G. Kevrekidis, S. Lafon, M. Maggioni,
and B. Nadler, Multiscale
Modeling & Simulation 7, 842 (2008), https://doi.org/10.1137/070696325.
43M. A. Rohrdanz, W. Zheng, B. Lambeth, J. Vreede, and C. Clementi, PLOS Computa-
tional Biology 10, 1 (2014).
44W. Zheng, A. V. Vargiu, M. A. Rohrdanz, P. Carloni, and C. Clementi, The Journal of
Chemical Physics 139, 145102 (2013), https://doi.org/10.1063/1.4824106.
45F.
No´e
and
F.
N¨uske,
Multiscale
Modeling
&
Simulation
11,
635
(2013),
https://doi.org/10.1137/110858616.
46J. McCarty and M. Parrinello, The Journal of Chemical Physics 147, 204109 (2017),
https://doi.org/10.1063/1.4998598.
47F. No´e and C. Clementi, Journal of Chemical Theory and Computation 11, 5002 (2015),
pMID: 26574285, https://doi.org/10.1021/acs.jctc.5b00553.
48F. No´e, R. Banisch, and C. Clementi, Journal of Chemical Theory and Computation 12,
5620 (2016), pMID: 27696838, https://doi.org/10.1021/acs.jctc.6b00762.
49M. Duan, J. Fan, M. Li, L. Han, and S. Huo, Journal of Chemical Theory and Compu-
tation 9, 2490 (2013).
50M. I. Jordan, ed., Learning in Graphical Models (MIT Press, Cambridge, MA, USA, 1999).
51M. Sch¨oberl, N. Zabaras,
and P.-S. Koutsourelakis, Journal of Computational Physics
333, 49 (2017).
52L. Felsberger and P. Koutsourelakis, Communications in Computational Physics
(ac-
cepted, 2018), arXiv:1802.03824.
53D.
P.
Kingma
and
M.
Welling,
“Auto-encoding
variational
bayes,”
(2013),
arXiv:1312.6114.
54D. J. Rezende, S. Mohamed, and D. Wierstra, in Proceedings of the 31th International
Conference on Machine Learning, ICML 2014, Beijing, China, 21-26 June 2014 (2014)
pp. 1278–1286.
55S.
Kmiecik,
D.
Gront,
M.
Kolinski,
L.
Wieteska,
A.
E.
Dawid,
and
A.
Kolinski,
Chemical
Reviews
116,
7898
(2016),
pMID:
27333362,
https://doi.org/10.1021/acs.chemrev.6b00163.
41


## Page 42


56W. G. Noid, J.-W. Chu, G. S. Ayton, and G. A. Voth, The Journal of Physical Chemistry
B 111, 4116 (2007), pMID: 17394308, https://doi.org/10.1021/jp068549t.
57M.
S.
Shell,
The
Journal
of
Chemical
Physics
129,
144108
(2008),
https://doi.org/10.1063/1.2992060.
58C. Peter and K. Kremer, Soft Matter 5, 4357 (2009).
59J. Trashorras and D. Tsagkarogiannis, SIAM Journal on Numerical Analysis 48, 1647
(2010).
60E. Kalligiannaki, M. A. Katsoulakis, P. Plech´aˇc, and D. G. Vlachos, Journal of Compu-
tational Physics 231, 2599 (2012).
61V. Harmandaris, E. Kalligiannaki, M. Katsoulakis, and P. Plech´aˇc, Journal of Compu-
tational Physics 314, 355 (2016).
62I. Bilionis and N. Zabaras, The Journal of Chemical Physics 138, 044313 (2013),
https://doi.org/10.1063/1.4789308.
63J. F. Dama, A. V. Sinitskiy, M. McCullagh, J. Weare, B. Roux, A. R. Dinner, and G. A.
Voth, Journal of Chemical Theory and Computation 9, 2466 (2013), pMID: 26583735,
https://doi.org/10.1021/ct4000444.
64W.
G.
Noid,
The
Journal
of
Chemical
Physics
139,
090901
(2013),
https://doi.org/10.1063/1.4818908.
65T. T. Foley, M. S. Shell, and W. G. Noid, The Journal of Chemical Physics 143, 243104
(2015), https://doi.org/10.1063/1.4929836.
66M. Langenberg, N. E. Jackson, J. J. de Pablo, and M. M¨uller, The Journal of Chemical
Physics 148, 094112 (2018), https://doi.org/10.1063/1.5018178.
67C. X. Hern´andez, H. K. Wayment-Steele, M. M. Sultan, B. E. Husic, and V. S. Pande
(2017).
68C. Wehmeyer and F. No´e, The Journal of Chemical Physics 148, 241703 (2018),
https://doi.org/10.1063/1.5011399.
69M.
M.
Sultan,
H.
K.
Wayment-Steele,
and
V.
S.
Pande,
Journal
of
Chemical
Theory
and
Computation
14,
1887
(2018),
pMID:
29529369,
https://doi.org/10.1021/acs.jctc.8b00025.
70M. J. Beal, Variational Algorithms for Approximate Bayesian Inference, Ph.D. thesis,
Gatsby Computational Neuroscience Unit, University College London (2003).
71B. J. Alder and T. E. Wainwright, The Journal of Chemical Physics 31, 459 (1959).
42


## Page 43


72D. Landau and K. Binder, A Guide to Monte Carlo Simulations in Statistical Physics
(Cambridge University Press, New York, NY, USA, 2005).
73Y. LeCun, Y. Bengio, and G. Hinton, Nature 521, 436 EP (2015).
74Z. Ghahramani, Nature 521, 452 EP (2015).
75W. von der Linden, V. Dose, and U. von Toussaint, Bayesian Probability Theory: Appli-
cations in the Physical Sciences (Cambridge University Press, 2014) p. 649.
76A. Y. Ng and M. I. Jordan, in Advances in Neural Information Processing Systems 14,
edited by T. G. Dietterich, S. Becker, and Z. Ghahramani (MIT Press, 2002) pp. 841–848.
77D. J. C. MacKay, Information theory, inference, and learning algorithms (Cambridge
University Press, 2003).
78C. Bishop, in Learning in Graphical Models (MIT Press, 1999) p. 371403.
79A. Cichocki and S.-i. Amari, Entropy 12, 1532 (2010).
80S.-H. Cha, “Comprehensive survey on distance/similarity measures between probability
density functions,” (2007).
81Inference on the generalized α-divergence is addressed in Ref. [? ].
82D. J. C. MacKay, Neural Comput. 4, 448 (1992).
83D. B. D. A. V. John B. Carlin, Hal S. Stern and D. B. R. A. Gelman, Bayesian Data
Analysis, 3Rd Edn (T&F/Crc Press, 2014).
84E. T. Jaynes, The Mathematical Intelligencer 27, 83 (2005).
85M. D. Hoﬀman, D. M. Blei, C. Wang,
and J. Paisley, J. Mach. Learn. Res. 14, 1303
(2013).
86R. Ranganath, S. Gerrish, and D. Blei, in Proceedings of the Seventeenth International
Conference on Artiﬁcial Intelligence and Statistics, Proceedings of Machine Learning
Research, Vol. 33, edited by S. Kaski and J. Corander (PMLR, Reykjavik, Iceland, 2014)
pp. 814–822.
87J. Paisley, D. M. Blei, and M. I. Jordan, in Proceedings of the 29th International Coference
on International Conference on Machine Learning, ICML (Omnipress, USA, 2012) pp.
1363–1370.
88A. P. Dempster, N. M. Laird, and D. B. Rubin, Journal of the Royal Statistical Society.
Series B (Methodological) 39, 1 (1977).
89R. M. Neal and G. E. Hinton (MIT Press, Cambridge, MA, USA, 1999) Chap. A View of
the EM Algorithm That Justiﬁes Incremental, Sparse, and Other Variants, pp. 355–368.
43


## Page 44


90F. R. Ruiz, M. Titsias RC AUEB,
and D. Blei, in Advances in Neural Information
Processing Systems 29, edited by D. D. Lee, M. Sugiyama, U. V. Luxburg, I. Guyon,
and R. Garnett (Curran Associates, Inc., 2016) pp. 460–468.
91P. Zhao and T. Zhang, “Accelerating minibatch stochastic gradient descent using stratiﬁed
sampling,” (2014), arXiv:1405.3080.
92L.
Bottou,
F.
Curtis,
and
J.
Nocedal,
SIAM
Review
60,
223
(2018),
https://doi.org/10.1137/16M1080173.
93D. P. Kingma and J. Ba, “Adam:
A method for stochastic optimization,”
(2014),
arXiv:1412.6980.
94P.-A. Mattei and J. Frellsen, in Advances in Neural Information Processing Systems 31,
edited by S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi,
and
R. Garnett (Curran Associates, Inc., 2018) pp. 3859–3870.
95N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, and E. Teller, The
Journal of Chemical Physics 21, 1087 (1953), https://doi.org/10.1063/1.1699114.
96W. K. Hastings, Biometrika 57, 97 (1970).
97L. L. Cam, International Statistical Review / Revue Internationale de Statistique 58, 153
(1990).
98M. West, in Bayesian Statistics (Oxford University Press, 2003) pp. 723–732.
99M. A. Figueiredo and S. Member, IEEE Transactions on Pattern Analysis and Machine
Intelligence 25, 1150 (2003).
100D. J. C. MacKay and R. M. Neal, “Automatic relevance determination for neural net-
works,” Tech. Rep. (University of Cambridge, 1994).
101M. E. Tipping, J. Mach. Learn. Res. 1, 211 (2001).
102H. Ritter, A. Botev, and D. Barber, in International Conference on Learning Represen-
tations (2018).
103P.
E.
Smith,
The
Journal
of
Chemical
Physics
111,
5568
(1999),
https://doi.org/10.1063/1.479860.
104J. Hermans, Proceedings of the National Academy of Sciences 108, 3095 (2011),
http://www.pnas.org/content/108/8/3095.full.pdf.
105G. Ramachandran, C. Ramakrishnan, and V. Sasisekharan, Journal of Molecular Biology
7, 95 (1963).
44


## Page 45


106R. Vargas, J. Garza, B. P. Hay, and D. A. Dixon, The Journal of Physical Chemistry A
106, 3213 (2002), https://doi.org/10.1021/jp013952f.
107S. P. Carmichael and M. S. Shell, The Journal of Physical Chemistry B 116, 8383 (2012),
pMID: 22300263, https://doi.org/10.1021/jp2114994.
108E. J. Sorin and V. S. Pande, Biophys J 88, 2472 (2005).
109A. J. DePaul, E. J. Thompson, S. S. Patel, K. Haldeman, and E. J. Sorin, Nucleic Acids
Res 38, 4856 (2010).
110M. P. Allen and D. J. Tildesley, Computer Simulation of Liquids (Clarendon Press, New
York, NY, USA, 1989).
111A. Onufriev, D. Bashford, and D. A. Case, Proteins: Structure, Function, and Bioinfor-
matics 55, 383 (2004), https://onlinelibrary.wiley.com/doi/pdf/10.1002/prot.20033.
112W. C. Still, A. Tempczyk, R. C. Hawley, and T. Hendrickson, Journal of the American
Chemical Society 112, 6127 (1990).
113H. Berendsen, D. van der Spoel, and R. van Drunen, Computer Physics Communications
91, 43 (1995).
114E. Lindahl, B. Hess, and D. van der Spoel, Molecular modeling annual 7, 306 (2001).
115D.
V.
D.
Spoel,
E.
Lindahl,
B.
Hess,
G.
Groenhof,
A.
E.
Mark,
and
H.
J.
C.
Berendsen,
Journal
of
Computational
Chemistry
26,
1701
(2005),
https://onlinelibrary.wiley.com/doi/pdf/10.1002/jcc.20291.
116B. Hess, C. Kutzner, D. van der Spoel, and E. Lindahl, Journal of Chemical Theory and
Computation 4, 435 (2008).
117S. Pronk, S. P´all, R. Schulz, P. Larsson, P. Bjelkmar, R. Apostolov, M. R. Shirts, J. C.
Smith, P. M. Kasson, D. van der Spoel, B. Hess, and E. Lindahl, Bioinformatics 29, 845
(2013).
118S. P´all, M. J. Abraham, C. Kutzner, B. Hess, and E. Lindahl, in Solving Software Chal-
lenges for Exascale, edited by S. Markidis and E. Laure (Springer International Publishing,
Cham, 2015) pp. 3–27.
119M. J. Abraham, T. Murtola, R. Schulz, S. P´all, J. C. Smith, B. Hess, and E. Lindahl,
SoftwareX 1-2, 19 (2015).
120D. E. Rumelhart, G. E. Hinton, and R. J. Williams (MIT Press, Cambridge, MA, USA,
1986) Chap. Learning Internal Representations by Error Propagation, pp. 318–362.
45


## Page 46


121C. Van Der Malsburg, in Brain Theory, edited by G. Palm and A. Aertsen (Springer
Berlin Heidelberg, Berlin, Heidelberg, 1986) pp. 245–248.
122S. Haykin, Neural Networks: A Comprehensive Foundation, 2nd ed. (Prentice Hall PTR,
Upper Saddle River, NJ, USA, 1998).
123D. Rezende and S. Mohamed, in Proceedings of the 32nd International Conference on
Machine Learning, Proceedings of Machine Learning Research, Vol. 37, edited by F. Bach
and D. Blei (PMLR, Lille, France, 2015) pp. 1530–1538.
124D. P. Kingma, T. Salimans, R. Jozefowicz, X. Chen, I. Sutskever, and M. Welling, in Ad-
vances in Neural Information Processing Systems 29, edited by D. D. Lee, M. Sugiyama,
U. V. Luxburg, I. Guyon, and R. Garnett (Curran Associates, Inc., 2016) pp. 4743–4751.
125J. C. Pinheiro and D. M. Bates, Statistics and Computing 6, 289 (1996).
126G. Klambauer, T. Unterthiner, A. Mayr, and S. Hochreiter, in Advances in Neural Infor-
mation Processing Systems 30, edited by I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach,
R. Fergus, S. Vishwanathan, and R. Garnett (Curran Associates, Inc., 2017) pp. 971–980.
127P. Ramachandran, B. Zoph, and Q. V. Le, ArXiv e-prints (2017), arXiv:1710.05941.
128W. Humphrey, A. Dalke, and K. Schulten, Journal of Molecular Graphics 14, 33 (1996).
129A. M. Fluitt and J. J. de Pablo, Biophysical Journal 109, 1009 (2015).
130Y. Sugita and Y. Okamoto, Chemical Physics Letters 314, 141 (1999).
131A. Marini and R. Y. Dong, Phys. Rev. E 83, 041712 (2011).
132Y. Zhou, A. Kloczkowski, E. Faraggi,
and Y. Yang, Prediction of Protein Secondary
Structure, Methods in Molecular Biology (Springer New York, 2016).
133I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair,
A. Courville, and Y. Bengio, in Advances in Neural Information Processing Systems 27,
edited by Z. Ghahramani, M. Welling, C. Cortes, N. D. Lawrence, and K. Q. Weinberger
(Curran Associates, Inc., 2014) pp. 2672–2680.
134Y. Saatci and A. G. Wilson, in Advances in Neural Information Processing Systems 30,
edited by I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan,
and R. Garnett (Curran Associates, Inc., 2017) pp. 3622–3631.
135T. Salimans, I. Goodfellow, W. Zaremba, V. Cheung, A. Radford, X. Chen,
and
X. Chen, in Advances in Neural Information Processing Systems 29, edited by D. D.
Lee, M. Sugiyama, U. V. Luxburg, I. Guyon, and R. Garnett (Curran Associates, Inc.,
2016) pp. 2234–2242.
46


## Page 47


136R. Galvelis and Y. Sugita, Journal of Chemical Theory and Computation 13, 2489 (2017),
pMID: 28437616, https://doi.org/10.1021/acs.jctc.7b00188.
47

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1809_06913v2_predictive_collective_variable_discovery_with_deep_bayesian_models
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1809_06913V2_PREDICTIVE_COLLECTIVE_VARIABLE_DISCOVERY_WITH_DEEP_BAYESIAN_MODELS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

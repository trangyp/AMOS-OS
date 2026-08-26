---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1501.07668v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1501.07668v1_Sloppiness_and_Emergent_Theories_in_Physics__Biology__and_Beyond

> Source: 1501.07668v1_Sloppiness_and_Emergent_Theories_in_Physics__Biology__and_Beyond.pdf

> Pages: 15

---


## Page 1


Sloppiness and Emergent Theories in Physics, Biology, and Beyond
Mark K. Transtrum,1 Benjamin Machta,2 Kevin Brown,3, 4 Bryan C. Daniels,5 Christopher R. Myers,6, 7 and
James Sethna6
1)Department of Physics and Astronomy, Brigham Young University, Provo, Utah 84602,
USA
2)Lewis-Sigler Institute for Integrative Genomics, Princeton University, Princeton, NJ,
USA
3)Departments of Biomedical Engineering, Physics, Chemical and Biomolecular Engineering, and Marine Sciences,
University of Connecticut, Storrs, CT, USA
4)Institute for Systems Genomics, University of Connecticut, Storrs, CT, USA
5)Center for Complexity and Collective Computation, Wisconsin Institute for Discovery, University of Wisconsin,
Madison, WI, USA
6)Laboratory of Atomic and Solid State Physics, Cornell University, Ithaca, NY,
USA
7)Institute of Biotechnology, Cornell University, Ithaca, NY, USA
Large scale models of physical phenomena demand the development of new statistical and computational
tools in order to be eﬀective. Many such models are ‘sloppy’, i.e., exhibit behavior controlled by a relatively
small number of parameter combinations. We review an information theoretic framework for analyzing sloppy
models. This formalism is based on the Fisher Information Matrix, which we interpret as a Riemannian metric
on a parameterized space of models. Distance in this space is a measure of how distinguishable two models
are based on their predictions. Sloppy model manifolds are bounded with a hierarchy of widths and extrinsic
curvatures.
We show how the manifold boundary approximation can extract the simple, hidden theory
from complicated sloppy models. We attribute the success of simple eﬀective models in physics as likewise
emerging from complicated processes exhibiting a low eﬀective dimensionality. We discuss the ramiﬁcations
and consequences of sloppy models for biochemistry and science more generally. We suggest that the reason
our complex world is understandable is due to the same fundamental reason: simple theories of macroscopic
behavior are hidden inside complicated microscopic processes.
I.
PARAMETER INDETERMINACY AND SLOPPINESS
As a young physicist, Freeman Dyson paid a visit to
Enrico Fermi1 (recounted in Ditley, Mayer, and Loew 2).
Dyson wanted to tell Fermi about a set of calculations
that he was quite excited about.
Fermi asked Dyson
how many parameters needed to be tuned in the theory
to match experimental data. When Dyson replied there
were four, Fermi shared with Dyson a favorite adage of
his that he had learned from Von Neumann: “with four
parameters I can ﬁt an elephant, and with ﬁve I can make
him wiggle his trunk.” Dejected, Dyson took the next bus
back to Ithaca.
As scientists, we are frequently in a similar position
to Dyson. We are often confronted with a model — a
heavily parameterized, possibly incomplete or inaccurate
mathematical representation of nature — rather than a
theory (e. g., the Navier-Stokes equations) with few to
no free parameters to tune. In recent decades, fueled by
advances in computing capabilities, the size and scope
of mathematical models has exploded. Massive complex
models describing everything from biochemical reaction
networks to climate to economics are now a centerpiece of
scientiﬁc inquiry. The complexity of these models raises a
number of challenges and questions, both technical and
profound, and demands development of new statistical
and computational tools to eﬀectively use such models.
Here we review several developments that have oc-
curred in the domain of sloppy model research. Sloppy is
the term used to describe a class of complex models ex-
hibiting large parameter uncertainty when ﬁt to data.
Sloppy models were initially characterized in complex
biochemical reaction networks3,4, but were soon after-
ward found in a much larger class of phenomena includ-
ing quantum Monte Carlo5, empirical atomic potentials6,
particle accelerator design7, insect ﬂight8, and critical
phenomena9.
As a prototypical example, consider ﬁtting decay data
to a sum of exponentials with unknown decay rates:
y(t, θ) =
X
µ
e−θµt.
(1)
We denote the vector of unknown parameters by θ. These
parameters are to be inferred from data, for example, by
nonlinear least squares.
This inference problem is no-
toriously diﬃcult10. Intuitively, we can understand why
by noting that the eﬀect of each individual parameter is
obscured by our choice to observe only the sum. Param-
eters have compensatory eﬀects relative to the system’s
collective behavior. A single decay rate can be decreased,
for example, provided other rates are appropriately in-
creased to compensate.
This uncertainty can be quantiﬁed using statistical
methods, as we detail in section II. In particular, the
Fisher Information Matrix (FIM) can be used to estimate
the uncertainty in each parameter in our model. The re-
sult for the sum of exponentials is that each parameter
is almost completely undetermined. Any parameter can
be varied by an inﬁnite amount and the model could still
ﬁt the data.
This does not mean that all parameters
arXiv:1501.07668v1  [cond-mat.stat-mech]  30 Jan 2015


## Page 2


2
FIG. 1.
Sloppy eigenvalue spectra of multiparameter
models from various ﬁelds3–5,9,11.
Eigenvalues of the FIM,
indicating sensitivity to perturbations along orthogonal di-
rections in parameter space, are roughly evenly spaced in log-
space, extending over many orders of magnitude.
can be varied independently of the others. Indeed, while
the statistical uncertainty in each individual parameter
might be inﬁnite, the data places constraints on combi-
nations of the parameters.
The eigenvalues of the FIM tell us which parameter
combinations are well-constrained by the data and which
are not. Most of the FIM eigenvalues are very small, cor-
responding to combinations of parameters that have little
eﬀect on model behavior. These unimportant parame-
ter combinations are designated sloppy. A small number
of eigenvalues are relatively large, revealing the few pa-
rameter combinations that are important to the model
(known as stiﬀ). It is generally observed that the FIM
eigenvalues decay roughly log-linearly, with each param-
eter combination being less important than the previous
by a ﬁxed factor, as in Figure 1. Consequently there is
not a well-deﬁned boundary between the stiﬀand sloppy
combinations, and four parameters really can “ﬁt the ele-
phant”.
The degree of parameter indeterminacy in the simple
sum-of-exponentials model has been seen in many com-
plex models of real life systems for many of the same
reasons. The FIMs for seventeen systems biology models
have been shown to have the same characteristic eigen-
value structure12, and examples from other scientiﬁc do-
mains abound5.
In each case, observations measure a
system’s collective behavior, and this means that when
parameters have compensatory eﬀects they cannot be in-
dividually identiﬁed.
The ubiquity of sloppiness would seem to limit the use-
fulness of complex parameterized models. If we cannot
accurately know parameter values, how can a model be
predictive? Surprisingly, predictions are possible with-
out precise parameter knowledge. As long as the model
predictions depend on the same stiﬀparameter combi-
nations as the data, the predictions of the model will
be constrained in spite of large numbers of poorly deter-
mined parameters.
The existence of a few stiﬀparameter combinations can
be understood as a type of low eﬀective dimensionality of
the model. In section III we make this idea quantitative
by considering a geometric interpretation of statistics.
This leads naturally to a new method of model reduction
that constructs low-dimensional approximations to high-
dimensional models (section IV). These low-dimensional
approximations are useful for revealing the emergent con-
trol mechanisms that govern the system’s behavior, i.e.,
extracting a simple emergent theory of the collective be-
havior from the larger, complex model.
Simple approximations to complex processes are com-
mon in physics (section V). The ubiquity of sloppiness
suggests that similarly simple models can be constructed
for other complex systems. Indeed, sloppiness has a num-
ber of profound implications for the unreasonable eﬀec-
tiveness of mathematics13 and the hierarchical structure
of scientiﬁc theories14.
We discuss some of these con-
sequences speciﬁcally for modeling biochemical networks
in section VI. We discuss more generally the implications
of sloppiness for mathematical modeling in section VII.
We argue that sloppiness is the underlying reason why
the universe (a complete description of which would be
indescribably complex) is comprehensible.
II.
MATHEMATICAL FRAMEWORK
In this section we use information theory to deﬁne key
measures of sloppiness geometrically15. We ﬁrst consider
the special case of model selection for models ﬁt to data
by least squares. We then generalize to the case of ar-
bitrary probabilistic models. The key insight is that the
Fisher Information deﬁnes a Riemannian geometry on the
space of possible models15. The geometric picture allows
us to show (in section III) that this local sloppy struc-
ture in the metric is paralleled by a global hyper-ribbon
structure of the entire space of possible models.
We begin with a simple case – a model y predicting
data d at experimental conditions u, with independent
Gaussian errors; each of these are vectors whose length
M is given by the number of data points. Our model de-
pends on N parameters θ. In general, an arbitrary model
is a mathematical mapping from a parameter space into
predictions, so interpreting a model as a manifold of di-
mension N embedded in a data space RM is natural; the
parameters θ then become the coordinates for the mani-
fold. If our error bars are independent and Gaussian all
with the same width (say, σ = 1), ﬁnding the best ﬁt of
model to data is a least squares data ﬁtting problem, as
we illustrate in Figure 2. In this case, we assume that
each experimental data point, di, is generated from a pa-
rameterized model, y(ui, θ), plus random Gaussian noise,


## Page 3


3
FIG. 2.
The Model Manifold A simple model16,17 of
an enzyme-catalyzed reaction can be expressed as a rational
function in substrate concentration (u) with four parameters
(θ) predicting the reaction velocity (y) (inset, top). By vary-
ing θ the model can predict a variety of behaviors y as a
function of u (top). The model manifold is constructed by
collecting all possible predictions of the model at speciﬁc val-
ues of u (red vertical lines at u = 0.1, 2.0, 4.0). To visualize
the manifold, we take a two-dimensional cross section of the
four dimensional manifold by choosing θ1 and θ2 to best ﬁt the
experimental data. Varying θ3 and θ4 then maps out a two-
dimensional surface of possible values in three-dimensional
data space (bottom). Each curve in the top ﬁgure corresponds
to a point of the same color on the model manifold (bottom);
the red crosses on top are data corresponding to the red dot
below.
ξi:
di = y(ui, θ) + ξi.
(2)
Since the noise is Gaussian,
P(ξ) ∝e−ξ2/2,
(3)
maximizing the log likelihood is equivalent to minimizing
the sum of squared residuals, sometimes referred to as the
cost or χ2 function:
χ2(θ) =
X
i
r2
i =
X
i
(di −y(ui, θ))2 .
(4)
A sum of squares is reminiscent of a Euclidean dis-
tance. Fitting a model to data by least squares is there-
fore minimizing a distance in data space between the ob-
served data and the model. Distance in data space mea-
sures the quality of a ﬁt to experimental data (red point
in Figure 2). Distance on the manifold is induced by, i.e.,
is the same as, the corresponding distance in data space
and is measured using the metric tensor
gµν =
X
i
∂y(ui, θ)
∂θµ
∂y(ui, θ)
∂θν
= (JT J)µν,
(5)
where Jiµ = ∂y(ui, θ)/∂θµ is the Jacobian matrix of par-
tial derivatives. This metric tensor is precisely the Fisher
Information Matrix (FIM) deﬁned below, specialized to
our least-squares problem. It is the least squares Hessian
matrix of second derivatives of 1/2χ2 from eqn 4, evaluated
where the data point d is taken to be perfectly predicted
by y(θ). On the manifold, distance is a measure of identi-
ﬁability – how diﬃcult it would be to distinguish nearby
points on the manifold (i.e., alternate models) through
their predictions.
We can generalize from this least-squares ﬁtting prob-
lem to encompass other models (like the Ising model)
where the predictions are for entire probability distribu-
tions. For the purpose of modeling, the output of our
model is a probability distribution for x, the outcome of
an experiment. A parameterized space of models is thus
deﬁned by P(x|θ). To deﬁne a geometry on this space
we must deﬁne a measure of how distinct two points θ1
and θ2 in parameter space are, based on their predictions.
Imagine getting a sequence of assumed independent data
x1, x2, ... with the task of inferring the model which pro-
duced them. The likelihood that model θ1 would have
produced this data is given by
P(x1, x2, ...|θ) =
Y
i
P(xi|θ) = exp
 X
i
log P(xi|θ)
!
.
(6)
In maximum likelihood estimation our goal is simply to
ﬁnd the parameter set θ which maximizes this likelihood.
It is useful to talk about log P(x|θ), the log-likelihood, as
this is the unique measure which is additive for indepen-
dent data points.
The familiar Shannon entropy of a
model’s predictions x is given by minus the expectation
value of the log-likelihood:
S(θ) = −
X
x
P(x|θ) log P(x|θ).
(7)
We can also deﬁne an analogous quantity that measures
the likelihood that model θ2 would produce typical data
from θ1:
X
x
P(x|θ1) log P(x|θ2).
(8)
The Kullback-Leibler divergence between θ1 and θ2 mea-
sures how much more likely θ1 is to produce typical data
from θ1 than θ2 would be:
DKL(θ1||θ2) =
X
x
P(x|θ1)
 log P(x|θ1) −log P(x|θ2)

.
(9)


## Page 4


4
Thus DKL is an intrinsic measure of how diﬃcult distin-
guishing these two models will be from their data.
The KL divergence does not satisfy the mathemati-
cal requirements of a distance measure. It is asymmet-
ric, and does not satisfy even a weak triangle inequality:
In some cases DKL(θ1||θ3) > DKL(θ1||θ2) + DKL(θ2||θ3).
However, for models whose parameters θ and θ + δθ are
quite close to one another, the leading terms are sym-
metric and can be written as:
DKL(θ||θ + δθ) = gµνδθµδθν + Oδθ3
(10)
where gµν is the Fisher Information Matrix (FIM), which
can be written:
gµν(Pθ) = −
X
x
Pθ(x) ∂
∂θµ
∂
∂θν log Pθ(x).
(11)
The FIM has all the properties of a metric tensor. It is
symmetric and positive semi-deﬁnite (because no model
can on average be better described by a diﬀerent model)
and it transforms properly under a coordinate reparame-
terization of θ. Information Geometry11,18–24 is the study
of the properties of the model manifold deﬁned by this
metric. In particular, it deﬁnes a space of models in a way
that does not depend on the labels given to the parame-
ters, which are presumably arbitrary; should one measure
rate constants in seconds or hours, and more problemat-
ically, should one label these constants as rates, or time
constants? Information Geometry makes clear that some
aspects of a parameterized model can be deﬁned in ways
that are invariant to these arbitrary choices.
III.
WHY SLOPPINESS? INFORMATION GEOMETRY
Sloppy models can be identiﬁed by the characteristic
eigenvalue spectrum of the FIM. We interpret the exis-
tence of many small eigenvalues in the FIM to be repre-
sentative of a complex model with a low eﬀective dimen-
sionality. Many combinations of parameters have mini-
mal eﬀect on the behavior of the model, while the key
features of model behavior are controlled by a relatively
small number of stiﬀparameter combinations. In a sense,
then, there really is a simpler ‘theory’ embedded in the
multiparameter ‘model’.
In this section we make the notion of low eﬀective di-
mensionality explicit. We will see that although this in-
terpretation of sloppy models turns out to be correct,
the eigenvalues of the FIM are not suﬃcient to make this
conclusion. Instead, we use the geometric interpretation
of modeling introduced in section II that allows us to
quantify important features of the model in a global and
parameterization independent way. The eﬀort to develop
this formalism will pay further dividends when we con-
sider model reduction in section IV.
To understand the limitations of interpreting the eigen-
values of the FIM, we return to the question of model
reparameterization. Something as trivial as changing the
units of a rate constant from Hz to kHz changes the corre-
sponding row and column of the FIM by a factor of 1000,
in turn changing the eigenvalues. Of course, none of the
model predictions are altered by such a change since a
correcting factor of 1000 will be introduced throughout
the model. More generally, the FIM can be transformed
into any positive deﬁnite matrix by a simple linear trans-
formation of parameters while model predictions are al-
ways invariant to such a reparameterization.
Although the FIM eigenvalues are not invariant to
reparameterization, we can use information geometry to
search for a parameterization independent measure of
sloppiness.
With the deﬁnitions of section II, compu-
tational diﬀerential geometry can be used to explore the
a wide variety of model manifolds in a parameter inde-
pendent way. A review of these methods is beyond the
scope of this paper, and we refer the interested reader to
references11,24 or any standard text on diﬀerential geom-
etry25,26.
The key geometric feature of the model manifolds of
nonlinear sloppy systems is that they have boundaries.
Many parameters and parameter combinations can be
taken to extreme values (zero or inﬁnity) without leading
to inﬁnite predictions. These boundaries can be explored
by numerically constructing manifold geodesics: analogs
of straight lines on curved surfaces. The arc lengths of
geodesics are a measure of the width of the model man-
ifold in each direction. Measuring these arc lengths for
a sloppy model shows that the widths of sloppy model
manifolds are exponentially distributed, reminiscent of
the exponential distribution of FIM eigenvalues. Indeed,
when we use dimensionless model parameters (e. g. log-
parameters), the square roots of the FIM eigenvalues are
a reliable approximation to the widths of the manifold in
the corresponding eigendirections11,24.
The exponential distribution of manifold widths has
been described as a hyperribbon (Fig. 3).
A three-
dimensional ribbon has a long dimension, a broad di-
mension, and a very thin dimension. The observed hi-
erarchy of exponentially decreasing manifold widths are
a high-dimensional generalization of this structure. We
will explore the nature of these boundaries in more detail
when we discuss model reduction in section IV.
The observed hierarchy of widths can be demonstrated
analytically for the case of a single independent variable
(such as time or substrate concentration in Figure 2) by
appealing to theorems for the convergence of interpolat-
ing functions (Fig. 3(a)). Consider removing a few de-
grees of freedom from a time series by ﬁxing the output of
the model at a few time points. The resulting model man-
ifold corresponds to a cross-section of the original. Next,
consider how much the predictions at intermediate time
points can be made to vary as the remaining parameters
are scanned.
As more and more predictions are ﬁxed
(i.e., considering higher-dimensional cross sections of the
model manifold), we intuitively predict that the behav-
ior of the model at intermediate time points will become
more constrained. Interpolation theorems make this in-


## Page 5


5
(a)
(b)
(c)
FIG. 3.
Hyperribbon. (a) Given a multiparameter model
for one-dimensional data f(t) at diﬀerent times t, the model
manifold has a diﬀerent dimension for every time t. Specify-
ing a data point f(tn) thus gives a cross-section of the model
manifold, and also reduces the uncertainty in the values of
neighboring points – hence giving the cross-section a nar-
rower width – a hyperribbon. Interpolation theory11,24 can
be used to quantify this qualitative argument. (Figure from
ﬁg. 5 of11.) (b,c) Two views of a hyperribbon cross section
of a model manifold. The model is decaying exponentials ﬁt
to radioactive decay data5. Notice the ribbon-like structure
of this three-dimensional projection: long, narrow, and very
thin.
tuition formal; presuming smoothness or analyticity of
the predictions as a function of time, one can demon-
strate an exponential hierarchy of widths consistent with
the hyperribbon structure observed empirically11,24.
The exponential hierarchy of manifold widths makes
explicit the notion of a low eﬀective dimensionality in
the model that was hinted at by the eigenvalues of the
FIM. It also helps illustrate how models can be predic-
tive without parameters being tightly constrained. Only
those parameter combinations that are required to ﬁt
the key features of the data need to be estimated ac-
curately. The remaining parameter combinations (con-
trolling for example the high-frequency behavior in our
time series example) are unnecessary. In short, the model
essentially functions as an interpolation scheme among
observed data points.
Models are predictive with un-
constrained parameters when the predictions interpolate
among observed data.
Understanding models as generalized interpolation
schemes makes additional predictions about the generic
structure of sloppy model manifolds. Not only is there
an exponential distribution of widths, there is also an
exponential distribution of extrinsic curvatures. Further-
more, these curvatures are relatively small in relation to
the widths, making the model manifold surprisingly ﬂat.
Most of the nonlinearity of the model’s parameters take
the form of ‘parameter eﬀects curvature’19,27–29, (equiva-
lent to the connection coeﬃcients11). The small extrinsic
curvature of many models was a mystery ﬁrst noted in
the early 1980s19 that is explained by interpolation ar-
guments.
IV.
MODEL REDUCTION
In this section, we leverage the power of the informa-
tion geometry formalism to answer the question: how can
a simple eﬀective model be constructed from a (more-
or-less) complete but sloppy representation of a physical
system? Our goal is to construct a physically meaning-
ful representation that reveals the simple ‘theory’ that is
hidden in the model.
The model reduction problem has a long history, and
it would be impossible in this review to even approach a
comprehensive survey of literature on the subject. Sev-
eral standard methods have emerged that have proven
eﬀective in appropriate contexts. Examples include clus-
tering components into modules30–32, mean ﬁeld theory,
various limiting approximations (e.g., continuum, ther-
modynamic, or singular limits), and the renormaliza-
tion group33,34.
Considerable eﬀort has been devoted
by the control and engineering communities to approxi-
mate large-scale dynamical systems35–39, leading to the
method of balanced truncation40–42, including several
structure preserving variations43–45 and generalizations
to nonlinear cases46–48. Methods for inferring minimal
dynamical models in cases for which the underlying struc-
ture is not known are also beginning to be developed49,50.
Unfortunately,
many
automatic
methods
produce
‘black box’ approximations. For most scenarios of prac-
tical importance, a reduced representation alone has lim-
ited utility since attempts to engineer or control the sys-
tem typically operate on the microscopic level. For ex-
ample, mutations operate on individual genes and drugs
target speciﬁc proteins. A method that explicitly reveals
how microscopic components are ‘compressed’ into a few
eﬀective degrees of freedom would be very useful.
On
the other hand, methods that do explicitly connect mi-
croscopic components to macroscopic behaviors have lim-
ited scope since they often exploit special properties of
the model’s functional form, such as symmetries. Con-
sider, for example, the renormalization group, which op-
erates on ﬁeld theories with a scale invariance or con-
formal symmetry. Simplifying modular network systems,
such as biochemical networks, is particularly challenging
due to inhomogeneity and lack of symmetries.
The
Manifold
Boundary
Approximation
Method
(MBAM)51 is an approach to model approximation
whose goal is to alleviate these challenges.
As the
name implies, the basic idea is to approximate a high-
dimensional, but thin model manifold by its boundary.
The procedure can be summarized as a four step al-
gorithm. First, the least sensitive parameter combina-
tion is identiﬁed from an eigenvalue decomposition of the
FIM. Second, a geodesic on the model manifold is con-
structed numerically to identify the boundary.
Third,
having found the edge of the model manifold, the cor-
responding model is identiﬁed as an approximation to
the original model. Fourth, the parameter values for this
approximate model are calibrated by ﬁtting the approx-
imate model to the behavior of the original model.


## Page 6


6
The result of this procedure is an approximate model
that has one less parameter and that is marginally less
sloppy than the original. Iterating the MBAM algorithm
therefore produces a series of models of decreasing com-
plexity that explicitly connect the microscopic compo-
nents to the macroscopic behavior. These models corre-
spond to hyper-corners of the original model manifold.
The method requires only that the model manifold have
a hierarchy of boundaries while making no assumptions
about the mathematical form of the model or underlying
physics of the system. As such, MBAM is a very general
approximation scheme.
The key component that enables MBAM are the edges
of the model manifold. The existence of these edges was
ﬁrst noted in the context of data ﬁtting24 and MCMC
sampling of Bayesian posterior distributions7.
It was
noted that algorithms would often ‘evaporate’ parame-
ters, i.e., allow them to drift to extreme, usually inﬁnite,
values. These extreme parameter values correspond to
limiting behaviors in the model, i.e., manifold bound-
aries.
‘Evaporated parameters’ are especially problematic for
numerical algorithms. Numerical methods often push pa-
rameters to the edge of the manifold and then become lost
in parameter space. Consider the case of MCMC sam-
pling of a Bayesian posterior. If a parameter drifts to
inﬁnity, there is an inﬁnite amount of entropy associated
with that region of parameter space and the sampling will
never converge. Furthermore, the model behavior of such
a region will always dominate the posterior distribution7.
For
data
ﬁtting
algorithms,
methods
such
as
Levenberg-Marquardt operate by ﬁtting the key features
of the data ﬁrst (i.e., the stiﬀest directions), followed
by successive reﬁning approximations (i.e., progressively
more sloppy components). While ﬁtting the initial key
features, algorithms often evaporate those parameters as-
sociated with less prominent features of the data. The
algorithm is then unable bring the parameters away from
inﬁnity in order to further reﬁne the ﬁt24.
Although problematic for numerical algorithms, mani-
fold edges are useful for both approximating (ala MBAM)
and interpreting complex models. To illustrate, we con-
sider an EGFR signaling model3.
Figure 4 illustrates
components of one eigenparameter, corresponding in this
case to the smallest eigenvalue of the FIM. Notice that
the eigenparameters do not align with bare parameters of
the model, but typically involve an unintuitive combina-
tion of bare parameters. However, by following a geodesic
along the model manifold to the manifold edge (step 2
of the MBAM algorithm), these complex combinations
slowly rotate to reveal relatively simple, interpretable
combinations that correspond to a limiting approxima-
tion of the model. For example, the EGFR model in ref-
erence3 consists of a network of Michaelis-Menten reac-
tions. The boundary revealed51 in Figure 4 corresponds
to the limit of a reaction rate and a Michaelis-Menten
Initial
Final
FIG. 4.
Identifying the boundary limit51. The compo-
nents of the smallest eigenvector of the FIM is often a compli-
cated combination of bare parameters that is diﬃcult to either
interpret or remove from the model (top left). By following a
geodesic to the manifold boundary, the combination rotates to
reveal a limiting behavior (bottom left); here two parameters
(a reaction rate and a Michaelis-Menten constant) become
inﬁnite. The limiting behavior is revealed when the smallest
eigenvalue has become separated from the other eigenvalues
(right).
constant becoming inﬁnite while their ratio is ﬁnite:
d
dt[A] =
k[A][B]
KM + [A] + . . .
(12)
→
 k
KM

[A][B] + . . . ,
(13)
where [A] and [B] are concentrations of two enzymes in
the model and the ratio k/KM is the renormalized pa-
rameter in the approximate model.
Because the manifold edges correspond to models that
are simple approximations of the original, the MBAM
can be used to iteratively construct simple representa-
tions of otherwise complex processes. By combining sev-
eral limiting approximations, simple insights into the sys-
tem behavior emerge that were obfuscated by the origi-
nal model’s complexity. Figure 5 compares network di-
agrams for the original and approximate EGFR models.
The original consists of 29 diﬀerential equations and 48
parameters, while the approximate consists of 6 diﬀer-
ential equations and 12 parameters and is notably not
sloppy.
Because the MBAM process explicitly connects models
through a series of limiting approximations, the param-
eters of the reduced model can be identiﬁed with (non-
linear) combinations of parameters in the original model.
For example, one of the twelve variables in the reduced


## Page 7


7
FIG. 5. Original3 and reduced51 EGFR models. The in-
teractions of the EGFR signaling pathway3,4 are summarized
in the leftmost network. Solid circles are chemical species for
which the experimental data was available to ﬁt. Manifold
boundaries reduce the model to a form (right) capable of ﬁt-
ting the same data and making the same predictions as in the
original references3,4. The FIM eigenvalues (center) indicate
that the simpliﬁed model has removed the irrelevant param-
eters identiﬁed as eigenvalues less than 1 (dotted line) while
retaining the original model’s predictive power.
model of Fig. 5 is written as an explicit combination of
seven ‘bare’ parameters of the original model:
φ = (kRap1ToBRaf)(KmdBRaf)(kpBRaf)(KmdMek)
(kdBRaf)(KmRap1ToBRaf)(kdMek)
.
(14)
Expressions such as this explicitly identify which combi-
nations of microscopic parameters act as emergent con-
trol knobs for the system.
MBAM naturally includes many other approximation
methods as special cases51. By an appropriate choice of
parameterization, it is both a natural language for model
reduction and a systematic method that in practice can
be mostly automated.
The MBAM is a semi-global approximation method.
Manifold boundaries are a non-local feature of the model.
However, MBAM only explores the region of the manifold
in the vicinity of a single hyper-corner. More generally,
it is possible to identify all of the edges of a particular
model (and by extension, all possible simpliﬁed models).
This analysis is known information topology52.
V.
EMERGENCE IN PHYSICS AS SLOPPINESS
Unlike in systems biology, physics is dominated by ef-
fective models and theories whose forms are often de-
duced long before a microscopic theory is available. This
is in large part due to the great success of continuum
limit arguments and Renormalization Group (RG) pro-
cedures in justifying the expectation and deriving the
form of simple emergent theories. These methods show
that many diﬀerent multi-parameter microscopic theories
typically collapse onto one coarse-grained model, with
the complex microscopics being summarized into just a
few ‘relevant’ coarse-grained parameters. This explains
why an eﬀective theory, or an oversimpliﬁed ‘cartoon’
microscopic theory, can often make quantitatively cor-
rect predictions. Thus, while three dimensional liquids
have enormous microscopic diversity, in a certain regime
(lengths and times large compared to molecules and their
vibration periods), their behavior is determined entirely
by their viscosity and density.
Although two diﬀerent
liquids can be microscopically completely diﬀerent, their
eﬀective behavior is determined only by the projection of
their microscopic details onto these two control param-
eters. This parameter space compression underlies the
success of renormalizable and continuum limit models.
This connection has been made explicit, by examining
the FIM for typical microscopic models in physics9. A
microscopic hopping model for the continuum diﬀusion
equation quickly develops ‘stiﬀ’ directions correspond-
ing to the parameters of the continuum theory – the to-
tal number of particles, net mean velocity, and diﬀusion
constant. As time evolves, all other microscopic param-
eter combinations become increasingly sloppy – irrele-
vant for prediction of long-time behavior.
Similarly, a
microscopic long-range Ising model for ferromagnetism,
when observed on long length scales, develops stiﬀdi-
rections along precisely those parameter combinations
deemed ‘relevant’ under the renormalization group.
Consider a model of stochastic motion as a stand-in for
a molecular level description of particles moving through
a possibly complicated ﬂuid.
Such a ﬂuid’s properties
depend on many parameters such as the bond angle of
the molecules which make it up, all of which enter into
the probability distribution for motion within the ﬂuid,
which can presumably be microscopically complex. How-
ever, the law of large numbers says that as many of these
random steps are added together, the long-time move-
ment of particles will lead to them being distributed in
space according to a Gaussian.
As this happens, di-
verse microscopic details must become compressed into
the two parameters of a Gaussian distribution- its mean
and width. As a concrete example, in the top of Figure 6,
two very diﬀerent microscopic motions are considered. In
each time step, red particles take a random step from a
triangular distribution, while blue particles step accord-
ing to a square distribution. While these motions lead
to very diﬀerent distributions after a single time step,
as time proceeds they become indistinguishable precisely
because their ﬁrst and second moments are matched.
This indistinguishability can be quantiﬁed by consider-
ing the model manifold of possible microscopic models of
stochastic motion, again paralleling real ﬂuids that can
be microscopically diverse. When probed at the intrinsic
time and length scales of these ﬂuids, we should make
few assumptions about the type of motion we expect; in
particular, we should allow for behaviors much more com-
plicated than diﬀusion, by analogy with square and trian-
gle described in two dimensions above. Following Ref.9,
we consider a one dimensional ‘molecular level’ model
for stochastic motion, in which parameters describe the


## Page 8


8
FIG. 6. Microscopic Motion becomes Diﬀusive. Top: Simulated particles undergo stochastic motion in discrete time.
Red particles hop according to a triangular kernel, while blue particles hop according to a square kernel. After a single time
step, the particles have very diﬀerent distributions in space, and neither resemble the distribution predicted by the diﬀusion
equation. However, as time evolves, most of the information about this kernel is lost. Only the particles’ diﬀusion tensor and
average drift enter into a continuum description. For the particles shown, the drift is 0, and their respective diﬀusion tensors
are matched, so that the resulting distributions become quantiﬁably indistinguishable as time proceeds. The compression of
microscopic details mirrors the compression of molecular level detail in the emergence of diﬀusion as a continuum limit of
motion in real ﬂuids. Bottom: We consider the model manifold of a one dimensional lattice version of this diﬀusion example.
As with the triangle and square, the red and blue kernels shown on the left have drift 0, and identical second moments, though
higher moments and the distribution in general are very diﬀerent. The remaining white points making up the manifold are
taken from a uniform distribution in parameter space describing the probability of hopping to one of six nearest neighbors in
a given time step, as in Ref.9. Here we plot a three dimensional projection of the model manifold taken from measurements
of particle distributions at diﬀerent time points. After a single time step, this three dimensional projection from data space
shows a ‘hyper-blob’, with changes in parameters leading to a large diversity of observable behaviors. In particular, the red and
blue points are not close to each other even though their drifts are both 0 and their diﬀusion constants are matched; as with
the square and triangle, their distributions are easily distinguishable after a single time step. However, after several stochastic
steps, the model manifold takes on a hyperribbon structure. Models for which all eﬀective parameters are matched, like the red
and blue kernels highlighted, rapidly move close to each other. At late times, any model suﬃciently ﬂexible to capture the two
remaining extended directions is adequate to describe eﬀective behavior, explaining the ubiquity and success of the continuum
diﬀusion equation.
rates at which a particle hops to one of its close-by neigh-
bors. After a single time step, the corresponding model
manifold is a ‘hyper-blob’ (ﬁg. 6, bottom) and two par-
ticular models, marked in red and blue, are distinguish-
able; they are not nearby on the model manifold. The
prediction space of a model is truly multidimensional in
this regime- it cannot be described by the two parameter
diﬀusion equation. In this ‘ballistic’ regime, motion is
not described by the diﬀusion equation, and is presum-
ably not just diﬀerent, but genuinely more complicated.
However, as time proceeds, the model manifold contracts
onto a hyper-ribbon, in which just two parameter combi-
nations distinguish behavior. In this regime, all points lie
close to the two dimensional manifold predicted by the
diﬀusion equation, and the red and blue points have be-
come indistinguishable; they are now in close proximity
on the manifold.
Using information geometry, approximations analo-
gous to continuum limits or the renormalization group
can be found and used to construct similarly simple the-
ories in ﬁelds for which eﬀective theories have historically
been diﬃcult to construct or justify.
VI.
RAMIFICATIONS OF SLOPPINESS IN BIOCHEMICAL
MODELING
In previous sections, we have emphasized picturing the
model manifold in data space, as in Figure 2; here, thin,
sloppy dimensions of the hyperribbon correspond to be-
havior that is minimally dependent on parameters. The
dual picture in parameter space, sketched in Figure 7, is
one in which the set of parameters that suﬃciently well
ﬁt some given data is stretched to extend far along sloppy


## Page 9


9
✓1 = log(p1)
✓2 = log(p2)
✓1 = log(p1)
✓2 = log(p2)
bare
eigen
λ−1/2
1
λ−1/2
2
FIG. 7. Sloppiness in Parameter Space. Left: A schematic of a typical Sloppy Model ensemble, pictured in two dimensions
for clarity. The underlying cost surface (with constant cost contours illustrated as ellipses) is generated by the ﬁt to data.
Eigenvectors of the FIM correspond to principal axes of the ellipse, with widths of the ellipse inversely proportional to the
square roots of the corresponding eigenvalues λi. Points inside the ellipse each represent a set of parameters that ﬁts the
data within a given tolerance (in practice often created using a Monte Carlo approach), forming an ensemble representing
uncertainty about the true values of parameters. Sloppiness can result in good ﬁts to data despite enormous uncertainties in
‘bare’ θ parameters (dotted lines intersecting the axes). Right: Careful measurements of individual parameters (like θ1) can
shrink uncertainty, but if even a single parameter remains unknown (like θ2), large predictive uncertainty can still result.
dimensions. This picture is important to understanding
implications for biochemical modeling with regard to pa-
rameter uncertainty.
For instance, using the full EGFR signal transduction
network (left side of Figure 5), we may wish to make a
prediction about an unmeasured experimental condition,
e.g. the time-course of ERK activity upon EGF stimu-
lation. In general, if there are large uncertainties about
the model’s parameters, we expect our uncertainty about
this time-course to also be large.
Indeed this is the case if we neglect eﬀects of compen-
sation among parameters and assume that uncertainties
in diﬀerent parameters are uncorrelated. If we view the
problem of uncertainties in model predictions as com-
ing from a lack of precision measurements of individual
parameters, we may try to carefully and independently
measure each parameter.
This can work if such mea-
surements are feasible, but can fail if even one relevant
parameter remains unknown: as in the right plot of Fig-
ure 7, a large uncertainty along the direction of a single
parameter corresponds to large changes in system-level
behavior, leading to large predictive uncertainties12.
Contrasting with this approach, we can instead con-
strain the model parameters with system-level measure-
ments that are similar to the types of measurements we
wish to predict. Due to the phenomenon of sloppiness,
we expect that this approach will produce a subspace of
acceptable parameters that will include large uncertain-
ties in individual parameter values (left plot of Figure 7).
Again, this arises because two parameters that change
the output in a correlated way can consequently be simul-
taneously varied without changing the model output. It
is often true that variance of system-level measurements
over the large sloppy parameter subspace is as small as
would require extremely precise measurements if param-
eters were measured independently. Predictions of inter-
est can be made without precisely knowing any single
parameter.
Thus, in the sense that estimating parameters entails
discovering their precise values, in sloppy models param-
eter estimation becomes useless. This does not mean that
anything goes; the region of acceptable parameters may
be small compared to prior knowledge about their values.
Yet it does validate a common approach to modeling such
systems, in which educated guesses are made for most pa-
rameters, and a remaining handful are ﬁt to the data. In
the common situation in which there are a small number
m of important ‘stiﬀ’ directions, with remaining sloppy
directions extending to cover the full range of feasible pa-
rameters, ﬁtting m parameters will be enough to locate
the sloppy subspace. (And if using a maximum likelihood
approach, this is in fact statistically preferred to ﬁtting
all parameters, in order to avoid overﬁtting.) Unfortu-
nately, it is hard to know m ahead of time, in general
requiring a sampling scheme like MCMC or a geodesic-
following algorithm11,24 to ascertain the global structure
of the sloppy subspace.
The problem of parameter estimation has been central
to the ﬁeld of systems biology for many years. The ex-
tremely large uncertainties in parameter estimates led to


## Page 10


10
the suggestion that accurate parameter estimates might
not be possible12. However, advances in experimental de-
sign have suggested that such estimates might be feasible
after all53–56, although requiring considerable experimen-
tal eﬀort57. The perspective provided by sloppy model
analysis provides at least two alternatives to this method
of operation.
First, in spite of the large number of parameters, com-
plex biological systems typically exhibit simple behavior
that requires only a few parameters to describe, analo-
gous to how the diﬀusion equation can describe micro-
scopically diverse processes.
Attempting to accurately
infer all of the parameters in a complex biological model58
is analogous to learning all of the mechanical and electri-
cal properties of water molecules in order to accurately
predict a diﬀusion constant.
It would involve consid-
erable eﬀort (measuring all the microscopic parameters
accurately12), while the diﬀusion constant can be easily
measured using collective experiments, and used to de-
termine the result of any other collective experiment.
Second, in many biological systems, there is consider-
able uncertainty about the microscopic structure of the
system. Sloppiness suggests that an eﬀective model that
is microscopically inaccurate may still be insightful and
predictive in spite of getting many speciﬁc details wrong.
For example a hopping model for thermal conductivity
would be ‘wrong’ even though it gives the right thermal
diﬀusion equation. ‘Wrong’ models can provide key in-
sights into the system level behavior because they share
important features with the true system. In such a sce-
nario, it is the ﬂexibility provided by large uncertainties
in the parameters that allows the model to be useful. Any
attempt to infer all the microscopic parameters would
break the model, preventing it from being able to ﬁt the
data.
Indeed, it is diﬃcult to envision a completely micro-
scopic model in systems biology. Any model will have
rates and binding aﬃnities that will be altered by the
surrounding complex stew of proteins, ions, lipids, and
cellular substructures. Is the well-known dependence of
a reaction rate on salt concentration (described by an ef-
fective Gibbs free energy tracing over the ionic degrees of
freedom) qualitatively diﬀerent from the dependence of
an eﬀective reaction rate on cross-talk, regulatory mech-
anisms, or even parallel or competing pathways not in-
corporated into the model? We are reminded of quan-
tum ﬁeld theories, where the properties (say) of the elec-
tron known to quantum chemistry are renormalized by
electron-hole reactions in the surrounding vacuum which
are ignored and ignorable at low energies.
Insofar as
a model provides both insight and correct predictions
within its realm of validity, the fact that its parameters
have eﬀective, renormalized values incorporating missing
microscopic mechanisms should be expected, not dispar-
aged.
VII.
MORE GENERAL CONSEQUENCES OF SLOPPINESS
The hyperribbon structures implied by interpolation
theory and information geometry in section III have pro-
found implications. Complex scientiﬁc models have pre-
dictions that vary in far fewer ways than their complexity
would indicate.
Multiparameter models have behavior
that largely depend upon only a few combinations of mi-
croscopic parameters. The high-dimensional results of a
system with a large number of control parameters will
be well encompassed by a rather ﬂat, low-dimensional
manifold of behavior. In this section, we shall speculate
about these larger issues, and how they may explain the
success of our eﬀorts to organize and understand our en-
vironment.
Eﬃcacy of Principal Component Analysis. Princi-
pal component analysis, or PCA, has long been an eﬀec-
tive tool for data analysis. Given a high-dimensional data
set, such as the changes of mRNA levels for thousands
of genes under several experimental conditions59, PCA
provides a reduced-dimensional description which often
retains most of the variation in the original data set in a
few linear components. Arranging the data into a matrix
Rjn + cj of experiments n and data points j centered at
cj, PCA uses the singular value decomposition (SVD)
R =
X
k
σkˆu(k) ⊗ˆv(k)
(15)
Rjn =
X
k
σkˆu(k)
j
ˆv(k)
n
(16)
to write R as the sum of outer products of orthonor-
mal vectors ˆu(k) in data space and ˆv(k) in the space of
experiments. Here σ1 ≥σ2 ≥... ≥0 are nonnegative
‘strengths’ of the diﬀerent components k. These singular
values can be viewed as a generalization of eigenvalues for
non-square, non-symmetric matrices. The ˆu(k) for small
k describe the ‘long axes’ of the data, viewed as a cloud
of points Rn in data space; σk is the RMS extent of the
cloud in direction ˆu(k). The utility of PCA stems from
the fact that in many circumstances only a few compo-
nents k are needed to provide an accurate reconstruction
of the original data. Just as our sloppy eigenvalues con-
verge geometrically to zero, the singular values σk often
rapidly vanish.
It is straightforward to show that the
truncated SVD keeping only the ﬁrst, largest K com-
ponents is an optimal approximation to the data, with
total least square error bounded by P
K+1 σ2
k.
These
largest singular components often have physical or bio-
logical interpretations – sometimes mundane but useful
(which machine was used to take the data), sometimes
scientiﬁcally central.
Why does Nature often demand so few components to
describe large dimensional data sets? Sloppiness provides
a natural explanation. If the data results from (say) a
biological system whose behavior is described by a sloppy
model y(θ), and if the diﬀerent experiments are sampling
diﬀerent parameter sets θn, then the data will be points


## Page 11


11
Rjn + cj = yj(θn) on the model manifold. Insofar as the
model manifold has the hyperribbon structure we pre-
dict, it has only a few long axes (corresponding to stiﬀ
directions) and it is extrinsically very ﬂat along these
axes11 (Fig. 18). Here each yj −cj, being a diﬀerence
between a data point and the center of the data, will be
nearly a linear sum of a small number K of long direc-
tions of the model manifold, and the RMS spread along
this kth direction will be bounded by the width of the
model manifold in that direction, plus a small correction
for the curvature. As any cloud of experimental points
must be bounded by the model manifold, the high singu-
lar values will be bounded by the hierarchy of widths of
the hyperribbon. Hence our arguments for the hyperrib-
bon structure of the model manifold in multiparameter
models provide a fundamental explanation for the success
of PCA for these systems.
Eﬃcacy of Levenberg-Marquardt; improved algo-
rithms.
The Levenberg-Marquardt algorithm60–62 is one of the
standard algorithms for least squares minimization. Its
broad utility can be explained through the lens of sloppy
models and geometric insights lead to natural improve-
ments. Minimizing a linear approximation to a nonlinear
model with a constraint on the step size
min
δθ |y(θ0) + Jδθ −y0|2 ,
|δθ| ≤∆
(17)
leads to the iterative algorithm
δθ = −
 JT J + λ
−1 JT (y(θ0) −y0) ,
(18)
where λ is a Lagrange multiplier. The FIM (JT J) for a
typical sloppy model is extremely ill-conditioned. How-
ever, the dampened scaling matrix JT J + λ will have no
eigenvalues smaller than λ. By tuning λ, the algorithm
is able to explicitly control the eﬀects of sloppiness. Fur-
thermore, since the eigenvalues of JT J are roughly log-
linear, λ need not be ﬁnely tuned to be eﬀective.
By
slowly decreasing λ, the algorithm ﬁts the key features of
the data ﬁrst (i.e., the stiﬀest directions), followed by suc-
cessive reﬁning approximations (i.e., progressively more
sloppy components). The algorithm may still converge
slowly as it navigates the extremely narrow canyons of
the cost surface (see Figure 7) or fail completely if it
becomes trapped near the boundary of the model mani-
fold11,24.
Information geometry provides a remarkable new per-
spective on the Levenberg Marquardt algorithm.
The
move δθ for λ = 0 is the direction in parameter space
corresponding to the steepest descent direction in data
space; for λ ̸= 0 the move is the steepest descent direc-
tion on the model graph11,24. The fact that the model
graph is extrinsically rather ﬂat turns the narrow opti-
mization valleys in parameter space into nearly concen-
tric hyperspheres in data space – explaining the power
of the method. Levenberg-Marquardt takes steps along
straight lines in parameter space; to take full advantage
of the ﬂatness of the model manifold, it should ideally
move along geodesics. As it happens, the leading term in
the geodesic equation is numerically cheap to calculate,
providing a a “geodesic acceleration” correction to the
Levenberg-Marquardt algorithm which greatly improves
the performance and reliability of the algorithm63,64.
Evolution is enabled. Besides practical consequences
for parameter estimation of biochemical networks (sec-
tion VI), sloppiness has potential implications for biol-
ogy and evolution. Speciﬁcally, the fact that biological
systems often achieve remarkable robustness to environ-
mental perturbations may be less mysterious when tak-
ing into account the vastness of sloppy subspaces. For in-
stance, the circadian rhythm in cyanobacteria, controlled
by the dynamics of phosphorylation of three interacting
Kai proteins, seems remarkable in that it maintains a 24–
hour cycle over a range of temperature over which kinetic
rates in the system are expected to double. Yet the de-
gree of sloppiness in the system suggests that evolution
may have to tune only a few stiﬀparameter directions to
get the desired behavior at any given temperature, and
perhaps only one extra parameter direction to make that
behavior robust to temperature variation65. Extended,
high-dimensional neutral spaces have been identiﬁed as a
central element underlying robustness and evolvability in
living systems66, and sloppy parameter spaces play a sim-
ilar role: a population with individuals spread through-
out a sloppy subspace can more easily reach a broader
range of phenotypic changes, such that the population is
simultaneously highly robust and highly evolvable65.
Pattern recognition as low-dimensional represen-
tation. The pattern recognition methods we use to com-
prehend the world around us are clearly low-dimensional
representations. Cartoons embody this: we can recog-
nize and appreciate faces, motion, objects, and animals
depicted with a few pen strokes. In principle, one could
distinguish diﬀerent people by patterns of scars, ﬁnger-
prints, or retinal patterns, but our brains instead process
subtle overall features. Caricatures in particular build on
this low-dimensional representation – exaggerating un-
usual features of the ears or nose of a celebrity makes
them more recognizable, placing them farther along the
relevant axes of some model manifold of facial features.
Archetypal analysis67, a branch of machine learning, an-
alyzes data sets with a matrix factorization similar to
PCA, but expressing data points as convex sums of fea-
tures that are not constrained to be orthogonal. In addi-
tion, the features must be convex combinations of data
points. Archetypal analysis applied to suitably processed
facial image data allows faces to be decomposed into
strikingly meaningful characteristic features67–69.
The
success of such algorithms is clearly related to a hidden
low-dimensional representation of the data.
One may
speculate that our facial structures are determined by
the eﬀects of genetic and environmental control param-
eters θ, and that the resulting model manifold of faces
has a hyperribbon structure, explaining the success of
the linear, low-dimensional archetypal analysis methods,
and perhaps also the success of our biological pattern


## Page 12


12
recognition skills.
Big data is reducible. Machine learning methods that
search for patterns in enormous data sets are a grow-
ing feature of our information economy.
These meth-
ods at root discover low-dimensional representations of
the high-dimensional data set. Some tasks, such as the
methods used to win the Netﬂix challenge70 of predict-
ing what movies users will like, directly make use of this
low-dimensional representation by using SVD and PCA.
More complex problems, such as digital image recog-
nition, make use of artiﬁcial neural networks, such as
stacked denoising autoencoders71. Consider the problem
of recognizing handwritten digits (the MNIST database).
The neural networks can be viewed as a ﬁtting prob-
lem, with parameters θα giving the outputs of the digital
neurons, and the model y(θ) producing a digital image
that is optimized to best represent the written digits.
The training of these networks focuses on simultaneously
developing a model manifold ﬂexible enough to closely
mimic the data set of digits, and of developing a map-
ping ˜y−1(d) from the original data d depicting the digit
to neural outputs θ = ˜y−1(d) close to the best ﬁt. Neural
networks starting with high-dimensional data routinely
distill the data into a much smaller, more comprehensible
set of neural outputs θ – which are then used to classify
or reconstruct the original data. Initial explorations of
a stacked denoising autoencoder trained on the MNIST
digit data by Hayden et al.72 show a clear hyperribbon
structure. What is surprising is not that the structure
of a successful neural network has a hyperribbon struc-
ture. Indeed, if it were not true that the N +1th thinnest
direction on the model manifold is signiﬁcantly thinner
than the ﬁrst N directions, surely an N neuron model
would fail to capture the behavior of the data.
What
does demand explanation is that these methods succeed
at all – that our handwritten digits live on a hyperribbon,
allowing the neural networks to succeed.
Science is possible.
In ﬁelds like ecology, systems
biology, and macroeconomics, grossly simpliﬁed models
capture important features of the behavior of incredi-
bly complex interacting systems. If what everyone ate
for breakfast was crucial in determining the economic
productivity each day, and breakfast eating habits were
themselves not comprehensible, macroeconomics would
be doomed as a subject.
We argue that adding more
complexity to a model produces diminishing returns in
ﬁdelity, because the model predictions have an underlying
hyperribbon structure.
Diﬀerent models can describe the same behav-
ior. We are told that science works by creating theories,
and testing rival theories with experiments to determine
which is wrong. A more nuanced view allows for eﬀective
theories of limited validity – Newton wasn’t wrong and
Einstein right, Newton’s theory is valid when velocities
are slow compared to the speed of light. In more com-
plex environments, several theoretical descriptions can
cast useful light onto the same phenomena (‘soft’ and
‘hard’ order parameters for magnets and liquid crystals73
(Ch. 9)). Also, in ﬁelds like economics and systems biol-
ogy, all descriptions are doomed to neglect pathways or
behavior without the justiﬁcation of a small parameter.
So long as these models are capable of capturing the ‘long
axes’ of the model manifold in the data space of known
behavior, and are successful at predicting the behavior
in the larger data space of experiments of interest, one
must view them as successful. Many such models will in
general exist – certainly reduced models extracted sys-
tematically from a microscopic model (section IV), but
other models as well. Naturally, one should design exper-
iments that test the limits of these models, and cleanly
discriminate between rival models. Our information ge-
ometry methods could be useful in the design of experi-
ments distinguishing rival models; current methods that
linearize about expected behavior74 could be replaced by
geometric methods that allow for large uncertainties in
model parameters corresponding to nearly indistinguish-
able model predictions.
Why is the world comprehensible? Surely the rea-
son that handwritten digits have a hyperribbon struc-
ture – that we don’t use random dot patterns to write
numbers – is partially related to the way our brain is
wired. We recognize cartoons easily, therefore the infor-
mation in our handwriting is encapsulated in cartoon-like
subrepresentations. Surely physics has low-dimensional
representations (section V) independently of the way our
brain works. The continuum limit describes our world
perturbatively in the inverse length and time scales of
the observation; the renormalization group in addition
perturbs in the distance to the critical point.
Why is
science successful in other ﬁelds, systems biology and
macroeconomics, for example?
Is it a selection eﬀect
– do we choose to study subjects where our brains see
patterns (low-dimensional representations), and then de-
scribe those patterns using theories with hyperribbon
structures? Or are there deep underpinning structures
(evolution, game theory) that guide the behavior into
comprehensible patterns? A cellular control circuit where
hundreds of parameters all individually control impor-
tant, diﬀerent aspects of the behavior would be incompre-
hensible without full microscopic information, discourag-
ing us from trying to model it. On the other hand, it
would seem challenging for such a circuit to arise under
Darwinian evolution. Perhaps modularity and compre-
hensibility themselves are the result of evolution75–78.
Conclusion. What began as a rather pragmatic exer-
cise in parameter ﬁtting has blossomed into an enterprise
that stretches across the landscape of science. The work
described here has both methodological implications for
the development and validation of scientiﬁc models (in
the areas of optimization, machine learning and model
reduction) as well as philosophical implications for how
we reason about the world around us. By investigating
and characterizing in detail the geometric and topologi-
cal structures underlying scientiﬁc models, this work con-
nects bottom-up descriptions of complex processes with
top-down inferences drawn from data, paving the way for


## Page 13


13
emergent theories in physics, biology, and beyond.
ACKNOWLEDGMENTS
We would like to thank Alex Alemi, Phil Burnham,
Colin Clement, Josh Fass, Ryan Gutenkunst, Lorien Hay-
den, Lei Huang, Jaron Kent-Dobias, Ben Nicholson and
Hao Shi for their assistance and insights. This work was
supported in part by NSF DMR 1312160 (JPS), NSF
IOS 1127017 (CRM), the John Templeton Foundation
through a grant to SFI to study complexity (BCD), the
U.S. Army Research Laboratory and the U.S. Army Re-
search Oﬃce under contract number W911NF-13-1-0340
(BCD).


## Page 14


14
1F. Dyson, Nature 427, 297 (2004).
2J. Ditley, B. Mayer, and L. Loew, Biophysical Journal 104, 520
(2013).
3K. S. Brown and J. P. Sethna, Physical Review E 68, 021904
(2003).
4K. S. Brown, C. C. Hill, G. A. Calero, C. R. Myers, K. H. Lee,
J. P. Sethna, and R. A. Cerione, Physical Biology 1, 184 (2004).
5J. J. Waterfall, F. P. Casey, R. N. Gutenkunst, K. S. Brown,
C. R. Myers, P. W. Brouwer, V. Elser, and J. P. Sethna, Physical
Review Letters 97, 150601 (2006).
6S. L. Frederiksen, K. W. Jacobsen, K. S. Brown,
and J. P.
Sethna, Physical Review Letters 93, 216401 (2004).
7R. Gutenkunst, Sloppiness, Modeling, and Evolution in Bio-
chemical Networks, Ph.D. thesis, Cornell University (2007),
http://ecommons.library.cornell.edu/handle/1813/8206.
8G. J. BERMAN and Z. J. WANG, Journal of Fluid Mechanics
582, 153 (2007).
9B. B. Machta, R. Chachra, M. Transtrum,
and J. P. Sethna,
Science 342, 604 (2013).
10A. Ruhe, SIAM Journal on Scientiﬁc and Statistical Computing
1, 481 (1980).
11M. K. Transtrum, B. B. Machta, and J. P. Sethna, Phys. Rev.
E 83, 036701 (2011).
12R. N. Gutenkunst, J. J. Waterfall, F. P. Casey, K. S. Brown,
C. R. Myers, and J. P. Sethna, PLoS Computational Biology 3,
1871 (2007).
13E. P. Wigner, Communications on Pure and Applied Mathemat-
ics 13, 1 (1960).
14P. W. Anderson et al., Science 177, 393 (1972).
15S. Amari and H. Nagaoka, Methods of Information Geometry,
Translations of Mathematical Monographs (American Mathe-
matical Society, 2000).
16B. Averick, R. Carter, J. More, and G. Xue, Preprint MCS-P153-
0694, Mathematics and Computer Science Division, Argonne Na-
tional Laboratory, Argonne, Illinois (1992).
17J. Kowalik and J. Morrison, Mathematical Biosciences 2, 57
(1968).
18E. Beale, Journal of the Royal Statistical Society. Series B
(Methodological) , 41 (1960).
19D. M. Bates and D. G. Watts, Journal of the Royal Statistical
Society. Series B (Methodological) , 1 (1980).
20S.-i.
Amari,
Diﬀerential-geometrical
methods
in
statistics
(Springer, 1985).
21S.-I. Amari, O. E. Barndorﬀ-Nielsen, R. Kass, S. Lauritzen, and
C. Rao, Lecture Notes-Monograph Series , i (1987).
22M. K. Murray and J. W. Rice, Diﬀerential geometry and statis-
tics, Vol. 48 (CRC Press, 1993).
23S.-i. Amari and H. Nagaoka, Methods of information geometry,
Vol. 191 (American Mathematical Soc., 2007).
24M. K. Transtrum, B. B. Machta, and J. P. Sethna, Phys. Rev.
Lett. 104, 060201 (2010).
25M. Spivak, A comprehensive introduction to diﬀerential geome-
try (Publish or Perish, 1979).
26T. Ivancevic, Applied diﬀerential geometry: a modern introduc-
tion (World Scientiﬁc Pub Co Inc, 2007).
27D. Bates and D. Watts, Ann. Statist 9, 1152 (1981).
28D. Bates, D. Hamilton,
and D. Watts, Communications in
Statistics-Simulation and Computation 12, 469 (1983).
29D. Bates and D. Watts, Nonlinear Regression Analysis and Its
Applications (John Wiley, 1988).
30J. Wei and J. C. Kuo, Industrial & Engineering chemistry fun-
damentals 8, 114 (1969).
31J. C. Liao and E. N. Lightfoot, Biotechnology and bioengineering
31, 869 (1988).
32H. Huang, M. Fairweather, J. Griﬃths, A. Tomlin, and R. Brad,
Proceedings of the Combustion Institute 30, 1309 (2005).
33N. Goldenfeld, Lectures on phase transitions and the renormal-
ization group (Addison-Wesley, Advanced Book Program, Read-
ing, 1992).
34J. Zinn-Justin, Phase transitions and renormalization group
(Oxford University Press, 2007).
35V. Saksena, J. O’reilly,
and P. V. Kokotovic, Automatica 20,
273 (1984).
36P. Kokotovic, H. K. Khali, and J. O’Reilly, Singular perturbation
methods in control: analysis and design, Vol. 25 (Siam, 1999).
37D. Naidu, Dynamics of Continuous Discrete and Impulsive Sys-
tems Series B 9, 233 (2002).
38A. C. Antoulas, Approximation of large-scale dynamical systems,
Vol. 6 (Siam, 2005).
39C. H. Lee and H. G. Othmer, Journal of mathematical biology
60, 387 (2010).
40B. Moore, Automatic Control, IEEE Transactions on 26, 17
(1981).
41G. Dullerud and F. Paganini, Course in Robust Control Theory
(Springer-Verlag New York, 2000).
42S. Gugercin and A. C. Antoulas, International Journal of Control
77, 748 (2004).
43K. Zhou, C. D’Souza,
and J. R. Cloutier, Systems & control
letters 24, 235 (1995).
44L. Li and F. Paganini, Automatica 41, 145 (2005).
45H. Sandberg and R. M. Murray, Optimal Control Applications
and Methods 30, 225 (2009).
46J. M. Scherpen, Systems & Control Letters 21, 143 (1993).
47S. Lall, J. E. Marsden, and S. Glavaški, International journal of
robust and nonlinear control 12, 519 (2002).
48A. J. Krener, in Analysis and Design of Nonlinear Control Sys-
tems (Springer, 2008) pp. 41–62.
49B. C. Daniels and I. Nemenman, arXiv:1404.6283 [q-bio.QM]
(2014).
50B. C. Daniels and I. Nemenman, PLOS ONE (in press, 2015).
51M. K. Transtrum and P. Qiu, Physical Review Letters 113,
098701 (2014).
52M. K. Transtrum,
G. Hart,
and P. Qiu, arXiv preprint
arXiv:1409.6203 (2014).
53J. F. Apgar, D. K. Witmer, F. M. White,
and B. Tidor, Mol.
Biosyst. 6, 1890 (2010).
54M. Vilela, S. Vinga, M. A. Maia, E. O. Voit, and J. S. Almeida,
BMC systems biology 3, 47 (2009).
55K. Erguler and M. P. H. Stumpf, Molecular BioSystems 7, 1593
(2011).
56M. Transtrum and P. Qiu, BMC Bioinformatics 13, 181 (2012).
57R. Chachra, M. K. Transtrum, and J. P. Sethna, Mol. BioSyst.
, (2011).
58E. Lee, A. Salic, R. Kr uger, R. Heinrich, and M. W. Kirschner,
PLoS Biology 1, e10 (2008).
59M. Ringner, Nat Biotech 26, 303 (2008).
60K. Levenberg, Quart. Appl. Math 2, 164 (1944).
61D. Marquardt, Journal of the Society for Industrial and Applied
Mathematics 11, 431 (1963).
62W. Press, S. A. Teukolsky, W. T. Vetterling, and B. P. Flannery,
Numerical recipes: the art of scientiﬁc computing, (Cambridge
University Press, 2007).
63M. K. Transtrum and J. P. Sethna, (manuscript in revision),
http://arxiv.org/abs/1201.5885.
64M.
Transtrum
and
J.
P.
Sethna,
“geodesiclm,”
http://
sourceforge.net/projects/geodesiclm/ (2011).
65B. C. Daniels, Y. J. Chen, J. P. Sethna, R. N. Gutenkunst, and
C. R. Myers, Current Opinion In Biotechnology 19, 389 (2008).
66A. Wagner, Robustness and Evolvability in Living Systems
(Princeton University Press, 2005).
67A. Cutler and L. Breiman, Technometrics 36, 338 (1994).
68M. MÃžrup and L. K. Hansen, Neurocomputing 80, 54 (2012),
special Issue on Machine Learning for Signal Processing 2010.
69C. Thurau, K. Kersting,
and C. Bauckhage, in Data Min-
ing, 2009. ICDM ’09. Ninth IEEE International Conference on
(2009) pp. 523–532.
70Y. Koren, R. Bell, and C. Volinsky, Computer 42, 30 (2009).
71P. Vincent, H. Larochelle, Y. Bengio,
and P.-A. Manzagol, in
Proceedings of the 25th International Conference on Machine
Learning, ICML ’08 (ACM, New York, NY, USA, 2008) pp.


## Page 15


15
1096–1103.
72L. X. Hayden, A. A. Alemi, and J. P. Sethn, (work in progress).
73J. P. Sethna, Statistical Mechanics: Entropy, Order Parameters,
and Complexity, http: // www. physics. cornell. edu/ sethna/
StatMech/ (Oxford University Press, Oxford, 2006).
74F. P. Casey, D. Baird, Q. Feng, R. N. Gutenkunst, J. J. Waterfall,
C. R. Myers, K. S. Brown, R. A. Cerione, and J. P. Sethna, Iet
Systems Biology 1, 190 (2007).
75M. Kirschner and J. Gerhart, Proceedings of the National
Academy of Sciences 95, 8420 (1998).
76L. H. Hartwell, J. J. Hopﬁeld, S. Leibler,
and A. W. Murray,
Nature 402, C47 (1999).
77N. Kashtan and U. Alon, Proceedings of the National Academy
of Sciences 102, 13773 (2005).
78J. Clune, J.-B. Mouret,
and H. Lipson, Proceedings of the
Royal Society of London B: Biological Sciences 280 (2013),
10.1098/rspb.2012.2863.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1501_07668v1_sloppiness_and_emergent_theories_in_physics_biology_and_beyond
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2015/1501_07668V1_SLOPPINESS_AND_EMERGENT_THEORIES_IN_PHYSICS_BIOLOGY_AND_BEYOND.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1807.05319v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1807.05319v3_Information-based_Variational_Model_Reduction_of_high-dimensional_Reaction_Netwo

> Source: 1807.05319v3_Information-based_Variational_Model_Reduction_of_high-dimensional_Reaction_Netwo.pdf

> Pages: 79

---


## Page 1


arXiv:1807.05319v3  [math.NA]  9 Oct 2019
Data-driven, Variational Model Reduction of
high-dimensional Reaction Networks
Markos A. Katsoulakisa,∗, Pedro Vilanovaa
aDepartment of Mathematics and Statistics, University of Massachusetts Amherst,
Amherst MA 01002, USA
Abstract
In this work we present new scalable, information theory-based variational
methods for the eﬃcient model reduction of high-dimensional determinis-
tic and stochastic reaction networks. The proposed methodology combines,
(a) information theoretic tools for sensitivity analysis that allow us to iden-
tify the proper coarse variables of the reaction network, with (b) variational
approximate inference methods for training a best-ﬁt reduced model. This
approach takes advantage of both physicochemical modeling and data-based
approaches and allows to construct optimal parameterized reduced dynamics
in the number of variables, reactions and parameters, while controlling the
information loss due to the reduction. We demonstrate the eﬀectiveness of
our model reduction method on several complex, high-dimensional chemical
reaction networks arising in biochemistry.
Keywords:
Model reduction, Pathwise relative entropy, Pathwise Fisher
information matrix, Variational Inference, Reaction Networks, Markov
processes, Scientiﬁc Machine Learning.
1. Introduction
The modeling and simulation of complex biochemical systems typically
involves non-linear and high-dimensional dynamical systems, in terms of
both state variables and parameters [1, 2]. Of particular importance would
∗Corresponding author. We use alphabetical convention in author’s name order.
Email addresses: markos@umass.math.edu (Markos A. Katsoulakis),
pedro.vilanova@gmail.com (Pedro Vilanova)
1


## Page 2


2
be a simpler model able to capture key characteristics of the biochemi-
cal system and therefore more amenable for analysis, parameter identiﬁ-
cation, statistical inference, and eventually design and optimization. Model
reduction techniques seek to obtain such models, but in many cases the
required computational work may quickly become prohibitive.
Addition-
ally, modeling goals usually constrain these reduction methods, for exam-
ple, the biochemical meaning of the state variables is likely to be diﬃcult
to interpret if non-linear (and even linear) coarse-graining transformations
are applied during the model reduction process. The most widely applied
reduction methods can be roughly classiﬁed as timescale exploitation ap-
proaches [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], reduction methods based on sen-
sitivity analysis [13, 14, 15, 16, 17, 13, 18, 19], optimization based methods
[18, 20, 21, 22, 23, 24], and lumping methods [25, 26, 27, 28]. Finally, an
important class of model reduction methods are based on maximum entropy
techniques for the closure of the equation that determines the time evolution
of the probabilistic description of the stochastic reaction network (see for in-
stance [29, 30, 31, 32, 33]). In particular, the method proposed in this work
can be considered as a combination of sensitivity and optimization-based
methods, using an information theory approach. We refer to Section 8 for a
discussion on the connections between our method and the current literature.
It is well-known that, when the population sizes of the biochemical sys-
tem become small, a deterministic formulation of the dynamics is inadequate
for understanding many important properties of the system (see for instance
[34, 35]).
Therefore, our method is primarily concerned with stochastic,
Markovian models of reaction networks. In order to estimate distances be-
tween corresponding probability distributions for our stochastic models and
train models from data, information metrics such as the relative entropy are
natural choices, [36]. The relative entropy (Kullback-Leibler divergence) of
two probability measures P and Q is given by
R(P ∥Q) = EP

log dP
dQ

,
(1)
where dP
dQ is the Radon-Nikodym derivative for P absolutely continuous with
respect to Q (see for instance [36]).
Entropy-based analytical tools have
proved essential for deriving rigorous model reductions of interacting particle
models to the so-called hydrodynamic limits, [37].
In a closely related direction, information metrics provide systematic,
practical, and widely used tools to build approximate statistical models of


## Page 3


3
reduced complexity through variational inference methods [38, 39, 40] for
machine learning [41, 42, 39], and coarse-graining of complex systems at equi-
librium [43, 44, 45, 46, 47, 48]. However, dynamics are of critical importance
in reaction networks and such earlier works on equilibrium coarse-graining
are not directly applicable. Here we build on earlier work [49, 50, 51], where
coarse-graining methods for dynamics and non-equilibrium steady states were
derived for molecular dynamics and Kinetic Monte Carlo methods. In par-
ticular, in order to address model reduction for dynamics it is essential to
consider time series data that include temporal correlations, necessitating the
use of information theory methods for probability distributions in path-space,
i.e. the space of all possible time series.
In this work we develop a method that, given a reaction network with path
distribution P0:T , i.e., a probability over the set of all possible dynamics over
a time interval, ﬁnds an element from a parameterized family of distributions
that is close to P0:T. The novelty of this work is two-fold, (a) it extends
the coarse-graining path-space information theory methods of [49, 50] to
achieve model reductions of complex reaction networks, and (b) obtains the
most eﬃcient model reduction in (a) by applying a path-space sensitivity
analysis technique presented in [52, 53], thus identifying the most sensitive
model parameters. More speciﬁcally, in (a) we consider the path probability
distribution P0:T of a high-dimensional reaction network, i.e., a probability
over the set of all possible dynamics (time series) on a time interval [0, T];
then we seek an element from a parameterized family of reduced models
distributions that is closest to P0:T with respect to a loss function, which in
this case is the relative entropy:
min
θ∈Θ R(P0:T ∥Qθ
0:T ) .
(2)
Here by Qθ
0:T we denote the parameterized path probability distribution,
where θ belongs to a certain parametric space Θ. As we will show in this
paper, R(P0:T ∥Qθ
0:T) in (2) turns out to be a parameter-dependent com-
putable quantity that can be ﬁtted (or trained) by means of the time series
data of the high-dimensional model P0:T.
Furthermore, in Step (b) in order to determine sensitive model param-
eters, we use the Hessian of the relative entropy R(P c
0:T ∥P c+ǫ
0:T ) where
the vector c corresponds to the parameters of the high-dimensional model
P0:T = P c
0:T and ǫ is any vector perturbation of c, i.e., the pathwise Fisher
Information Matrix (pFIM), [54, 53]. This pFIM is block-diagonal and scales


## Page 4


4
linearly with the number of parameters, thus is computationally an eﬃcient
tool for sensitivity analysis of reaction networks.
In turn, this sensitivity
analysis identiﬁes and ranks sensitive model parameters, but crucially for
the optimization in (2), determines a family of reduced coarse variables and
associated models Qθ
0:T by retaining only the corresponding reactions and
species to just the sensitive parameters. In this fashion, step (b) enables
step (a) in order to obtain the best-ﬁt reduced model by optimizing the loss
function in (2), over only the sensitive parameters θ and subsequently the
proper family of reduced models Qθ
0:T. Overall, the path-space model reduc-
tion methodology introduced earlier in [49, 50] is here augmented to include
the sensitivity analysis and uncertainty quantiﬁcation, information-theoretic
tools described earlier that allow us to identify the proper coarse variables,
a long-standing open question in the coarse-graining literature. This latter
was made feasible here, both due to the use of the pFIM and the inherent
sparse structure of reaction networks.
The resulting method provides a simple, eﬃcient and principled model
reduction method targeted to high-dimensional deterministic and stochastic
reaction networks. This method enables signiﬁcant model reductions in the
number of variables, reactions and parameters, while preserving the original
dynamics, especially in the case of models in “sloppy” regimes, i.e., when
most of the information contained in the pFIM is accumulated in a reduced
number of parameters, for a given time interval. This reduction method con-
struct models in such a way that the information contained in the reduced
model, relative to the full model, satisﬁes a user deﬁned information thresh-
old. Furthermore, the quality of a given reduction is assessed by comparing
suitable distances between the mean-ﬁeld of the full and the reduced models,
and aim to satisfy a user deﬁned error tolerance. One of the main advan-
tages of our reduction method is its feasibility in terms of computational
work. From the algorithmic point of view, to construct the reduced model in
step (b) using the pFIM (not including the minimization step (2)) a linear
amount of computational work on the number of parameters plus the number
of state variables is usually required (per timestep). As a comparison, note
that the work required for classical sensitivity analysis is of the order of the
number of parameters times the number of state variables. In a nutshell, our
method can be visually described as in Figure 2.
We demonstrate the eﬃciency of our method by reducing three well-
known models present in the biochemical literature: A protein homeostasis
network in a sloppy regime from [55], a Epidermal Growth Factor Receptor


## Page 5


5
(EGFR) model from [56], a mammalian circadian clock model from [57], and
ﬁnally two stochastic pure jump models: a growth factor receptor derived
from [56], and a circadian clock model derived from [57]. In the ﬁrst case, we
consider a particular regime studied by the authors, in which it is possible to
obtain a substantial reduction both in the number of state variables and in
the number of parameters and reaction channels. In the second example we
analyze a non-sloppy model of signalling phenomena, i.e. has two diﬀerent
regimes in time, and still able to obtain signiﬁcant reductions. In the third
example, we reduce a model whose dynamics are dominated by non-trivial
oscillatory behaviour. Finally, both stochastic models are reduced to obtain
remarkable agreements even in the presence of non-Gaussian distributions.
In all the examples, even though the models were carefully designed by re-
searchers, signiﬁcant model reductions are achieved.
One of the key elements of our approach is that we combine two diﬀer-
ent modeling philosophies: the physically based behavior description of a
biochemical system, and the data-based approach, i.e., the analysis of time
series data. The physics is modeled by using the reaction network formalism,
and in particular we focus on the stoichiometry matrix, which describes the
relation between state variables and reaction paths of the process and does
not depend on the type of the model (discrete or continuous, deterministic
or stochastic). The physical modeling point of view is then emphasized in
the selection of the most important reactions and state variables and the
construction of the reduced stoichiometry. The data-based approach is em-
phasized in the data ﬁt step i.e. the minimization problem (2) via a suitable
simpliﬁed loss function that is derived in Section 4.3. Three main challenges
were considered in the reduction method presented in this work. The ﬁrst
one, is to preserve the structure and therefore the physical model of the
original network. This means not only to incorporate the reaction network
formalism, but in particular to exploit its stoichiometry in order to identify
the most relevant variables, parameters and reaction channels. This eﬀec-
tively reduces data requirements in comparison to alternative machine learn-
ing techniques that do not take into account the scientiﬁc domain knowledge
and therefore substantially accelerates identiﬁcation and training steps. In
particular, our method allows to optimize the parameter vector by consid-
ering the drift associated to the reduced model instead of the full model,
dramatically reducing the complexity of the optimization step (see Theorem
4.1).
Second challenge was to preserve physicochemical understanding of
the reduced model, which is of crucial importance in mathematical model-


## Page 6


6
ing. User conﬁdence in model predictions is directly linked to the conviction
that the model accounts for the correct variables, parameters, and appli-
cable physicochemical laws. The goal of obtaining understandable models
which are readily interpretable becomes signiﬁcantly more diﬃcult in the
high-dimensional case. Computational intensive and involved model reduc-
tion techniques may achieve more parsimonious reductions, but the lack of
interpretability makes them insuﬃcient speciﬁcally in the high-dimensional
case.
Finally, we aimed to obtain a method able to provide, in a robust
manner, reduced models within a prescribed accuracy and information loss,
requiring the least amount of computational work. The iterative nature of
our approach, allows to subsequently construct improved reduced models by
increasing the number of variables, parameters and reactions channels. Then,
a hierarchy of reduced models for model selection is obtained. Even though
our method uses the stoichiometry of the network to ontain the reduced
model, choose sensitive species, further structural and chemical information
may be extracted from it. In that respect, our method can be considered as
a knowledge-domain-aware scientiﬁc machine learning technique that makes
use of well established machine learning methods such as variational and
approximate inference.
The paper is structured as follows. In the next section we present main
notations and assumptions regarding reaction networks. In Section 3 we re-
view main information-based tools used in the variational model reduction
approach for stochastic systems, such as the pathwise Fisher information
matrix, scalable information-based sensitivity indexes and its mean-ﬁeld ap-
proximation. In Section 4 we recap the variational inference idea applied to
coarse-graining and we present the core of the contribution contained in this
work: a scalable loss function for data training. In Section 5 we present our
information-based reduction method for high dimensional reaction networks.
This reduction method is driven by the pathwise Fisher information matrix
to ﬁnd the most sensitive parameters and reaction channels, and then uses
the stoichiometry of the network to build a family of parameterized models
to ﬁnally use the loss function to ﬁt the resulting model to time series data.
In sections 6 and 7 we apply our method to three models taken from the
literature and two proposed stochastic pure jump models obtaining relevant
reductions in all of them. In Section 8 we discuss closely related state of the
art on model reduction for biochemical reaction networks. We ﬁnally draw
main conclusions of this work in Section 9.


## Page 7


7
2. Models for reaction networks
The purpose of this section is to present main notations and assumptions
regarding reaction networks.
A Reaction Network is a dynamical system
whose state can be described by a d-dimensional time dependent vector, de-
noted by X(t) = (X1(t), X2(t), ..., Xd(t)) ∈L, and a ﬁnite number, J, of pos-
sible transitions of the system. Each transition is a pair (νj, aj), j=1, 2, ..., J,
formed by a d-dimensional state-change vector νj and a non-negative func-
tion aj = aj(x; c) that depends on the state of the system, x ∈L, and a
K-dimensional vector of model parameters c ∈C. Each state-change vector
describes the eﬀect of the transition on the state of the system. If the state
of the system at time t is X(t)=x and the j-th transition is taken, then
the next state is x+νj. The function aj models the rate at which the j-th
reaction occurs. The matrix ν is deﬁned as the matrix whose j-column is
νj, and a is the column vector whose components are aj. In this work, we
assume νj ∈Zd, L = Rd, and C = RK. More importantly, we focus on
high-dimensional systems, i.e., J≫1, d≫1, and K≫1.
In biochemical reaction networks, νj is called stoichiometric vector, aj is
called propensity function, the pair (νj, aj) is called reaction channel, and
X(t) accounts for the population of d interacting species (S1, S2, ..., Sd). The
stoichiometry of each reaction channel can be represented as
νin,1S1 + νin,2S2 + . . . + νin,dSd →νout,1S1 + νout,2S2 + . . . + νout,dSd
where νin,i, νout,i ∈N for i=1, 2, ..., d. The left hand side of the arrow repre-
sents the species that take part as the input in the reaction (called reactants),
and the right hand side represents the species that take part as the output
(called products). We then have ν = νout −νin. The stoichiometry models
the law of conservation of mass where the total mass of the reactants equals
the total mass of the products. Stoichiometry describes the static, algebraic
structure of the network of reactions. It can be considered as the framework
within each chemical motion take place. Here we focus on the stoichiometry
of the network to construct a reduced model. Having the full stoichiometry
information allows to identify when a reactant is consumed in a reaction,
and distinguish it from a catalytic reactant, which is not consumed. In some
cases, the stoichiometry determines the form of the propensity function, e.g.
in the case of the law of mass action, which is the proposition that the rate of
a chemical reaction is directly proportional to the product of the activities or


## Page 8


8
concentrations of the reactants. In this work, we assume that, for every re-
action channel, vectors νin and νout are sparse. That is, |{i : νin,i ̸= 0}| ≪d
and |{i : νout,i ̸= 0}| ≪d, for j=1, 2, ..., J. This is typically the case in
biochemical reaction networks.
Each reaction channel depends on a vector of model parameters. Here we
denote with ϕ the function that maps, for each parameter, the set of reaction
channels that explicitly depend on that parameter,
ϕ : {1, 2, . . ., K} →℘({1, 2, . . . , J}) ,
(3)
where ℘(A) denotes the set of all possible subsets of A. For example, in
the linear parameter dependent case, the map ϕ is the identity that maps
the index k to the singleton {k}. In this work, we assume that the reaction
channels depend on a reduced number of parameters, that is, for a given
propensity function aj, we have
aj(x; c) = aj(x; ck1, ck2, ..., ckM) ,
(4)
where k1, ..., kM ∈{1, 2, ..., K} and M≪K for j=1, 2, ..., J. This is typically
the case in biochemical reaction networks.
Next, we discuss stochastic and deterministic models for RNs.
The
stochastic models are of two types: discrete state, called Stochastic Reac-
tion Networks (SRNs), and continuous state, usually called the Chemical
Langevin equation (CLE). The ﬁrst one is a counting stochastic process, and
usually models the number of particles of diﬀerent species interacting in a
ﬁxed volume, while the second is a diﬀusion process that models concen-
trations instead of number of particles. The deterministic model is usually
called reaction-rate system (of diﬀerential equations) and models the average
concentration of the species. By means of a proper renormalization of the
variables by the size of the volume in which the species interact, it is possible
to obtain a relation between the stochastic intensity and the deterministic re-
action rate. In this work we assume the scalings are properly done, whenever
it may be needed (see [58] and references therein).
2.1. Stochastic reaction networks
Stochastic Reaction Networks (SRNs) are a class of continuous-time Markov
chains that describe the stochastic evolution of a system of d interacting
species, where X : R+ × Ω→Nd models the number of particles of each
species present in the system at time t.


## Page 9


9
The probability that reaction j occurs during an inﬁnitesimal interval
(t, t + ∆t], when the state of the system is X(t) = x, is given by
Pr

X(t + ∆t) = x + νj
 X(t) = x
	
= aj(x; ·)∆t + o(∆t) .
(5)
We assume aj(x; ·)=0 for x such that x+νj /∈L, that is, the process never
leaves the domain L. This is sometimes not the case in some biochemical
models used in practice, but it can be suitably enforced by means of smooth
indicator functions. The total propensity (or rate) a0(x; c) := P
j aj(x; c) is
in fact the waiting time for the process departing from state x. SRNs can be
characterized by the following representation [59]
X(t) = x0 +
J
X
j=1
Yj
Z t
0
aj(X(s)) ds

νj ,
(6)
where Yj : R+×Ω→L are independent unit-rate Poisson processes. A typi-
cal feature of biochemical systems is that the modeled reaction network has
thousands of species and/or reaction channels together with diﬀerent time
scales coming from the orders of magnitude disparity between the propen-
sity of each reaction channel, making an exact simulation of a SRN un-
feasible from the computational point of view. The tau-leap method [60]
approximates (6) by applying a forward Euler discretization, that is, sam-
pling a batch of events by means of a Poisson random variable at each time-
increment. Although several improvements of the basic tau-leap algorithm
have been proposed, methods for high-dimensional systems are still under
active research [61, 62, 63, 64, 65].
2.2. Chemical Langevin equation and the mean-ﬁeld equation
A number of approximations to the pure jump process (5) have been
developed in order to reduce the computational work required to sample a
trajectory of the system. For example, the reaction-rate ODE system (or
mean-ﬁeld) approximation ignores the stochastic ﬂuctuations and yields a
deterministic system that approximates the mean populations of the species
[66, 67]. Stochastic counterparts such as the Chemical Langevin equation
[68] or the linear noise approximation [69] can be applied in order to improve
the accuracy of the simulation. The reaction-rate ODE system (or mean-
ﬁeld) can be formally obtained by linearizing the inﬁnitesimal generator of


## Page 10


10
the SRN, to obtain 
dz(t) = νa(z(t); c)dt,
t ∈R+
z(0) = x0
.
(7)
A second order expansion gives the so called chemical Langevin (CLE) ap-
proximation

dY (t) = νa(Y (t); c)dt + ν
p
diag(a(Y (t); c))dW(t),
t ∈R+
Y (0) = x0
,
(8)
where Y (t) is a diﬀusion process, W(t) is a RJ-valued Wiener process with
independent components, and diag(v) of a vector v is a square matrix whose
diagonal is v and zero everywhere else (see [58] and references therein).
Euler discretization of the CLE. Usually, specialized solvers are used by
the modeller to obtain time series data of a complex reaction network by run-
ning suitable software like CHEMKIN [70] or TChem [71]. In this work, we
aim to obtain model reductions by using available data. For this reason, and
without losing any methodological generality, we focus on describing the dy-
namics of the reaction network by means of the following Euler discretization
of the CLE (8) for a time-step of size ∆t
xk+1 = xk + b(xk)∆t + σ(xk)∆Wk ,
(9)
where
b(x) := νa(x; c)
and
σ(x) := ν
p
diag(a(x; c)) ,
with ∆Wk ∼N (0, ∆tI) independent Gaussian increments. The density of
its transition probability, given x ∈Rd to x′ ∈Rd, is a multivariate Gaussian
random variable that depends on ∆t and can be written
p(x, x′) =
1
Z∆t(x) exp

−1
2∆t(x′ −m∆t(x))trΣ−1(x)(x′ −m∆t(x))

, (10)
where m∆t(x) := x −b(x)∆t, Z∆t(x) :=
p
(2π∆t)d det(Σ(x)) and Σ(x) :=
σ(x)σtr(x).
This Euler discretization of the CLE allows to obtain the following time
series
(x0, x1, x2, ..., xT) ,
where xi=(xi,1, xi,2, ..., xi,d) for i=0, 1, ..., T ,
(11)
for (∆ti)T
i=1 on the time interval [0, T]. Notice that similar time series can
also be obtained by sampling the representation (6) or by the numerical
integration of the reaction-rate ODEs (7). In this work, we do not consider
measurement errors.


## Page 11


11
3. Path-space information methods in discrete time
The purpose of this section is to review main information-based tools used
in the variational model reduction approach for stochastic systems introduced
in [50, 49].
3.1. Information-based model reduction
In this section we brieﬂy recap the main idea of information-based model
reduction. Given a reaction network with path distribution denoted by P0:T
(the full model), we aim to ﬁnd an element from a parameterized family of
distributions that is close to this original distribution in a suitable distance.
Let Qθ
0:T denote the parameterized path distribution, where θ belongs to a
certain parametric space Θ. Using the relative entropy as the distance, we
aim to solve
min
θ∈Θ R(P0:T ∥Qθ
0:T) ,
to ﬁnd the optimal representation of P0:T in terms of Qθ
0:T. We notice that
P0:T also depends on a model parameter vector, i.e., P c
0:T, but for simplicity
we avoid this notation here. Recall that the relative entropy is not symmetric
so we may be also interested in the problem
min
θ∈Θ R(Qθ
0:T ∥P0:T) ,
typically addressed in the variational inference literature, [REF7]. Here we
choose to work with the former one, primarily due to the relative simplic-
ity of implementation. The relative entropy between the two path distribu-
tions P0:T and Qθ
0:T (or Kullback-Leibler divergence), on the same measurable
space, is given by
R(P0:T ∥Qθ
0:T) = EP0:T

log dP0:T
dQθ
0:T

,
provided P0:T is absolutely continuous with respect to Qθ
0:T . From an informa-
tion theory perspective, the relative entropy quantiﬁes the loss of information
when Qθ
0:T is used instead of P0:T. One notable analytical advantage of the
relative entropy is that it reduces to minimizing the expectation of a single
distinguished observable given by log dP0:T
dQθ
0:T . We refer to [52, 53, 54] and ref-
erences therein for additional details, in particular for relative entropy for


## Page 12


12
discrete time Markov Chains. In our setting of model reduction (or coarse-
graining), the path distribution P0:T is associated with the original model
(which will be mapped to the coarse space in order to be able to compute
the relative entropy) and Qθ
0:T is associated with the approximating reduced
model. The parameterized family of distributions Qθ
0:T is considered in or-
der to construct the best approximation to the original distribution P0:T.
This approximation is then ﬁtted using entropy-based criteria over a set of
data coming from the model with distribution P0:T, to ﬁnd the best possible
Markovian approximation of the projected original model. By training this
single functional given by the relative entropy instead of an observable-based
quantity of interest, we obtain a reliable parameterization that gives rise to
transferability properties applicable to any observable.
3.2. Pathwise relative entropy
Here we present the pathwise distribution of the original model, P0:T, and
the parameterized one, Qθ
0:T , for a discrete-time Markovian time-homogeneous
process that generates the time series (xi)T
i=0 (see (11)). Let p(x, x′) denote
its transition probability function for x, x′ ∈L. In virtue of the Markov prop-
erty, the path space probability distribution P0:T for the time series {xi}T
i=0,
starting from the distribution ν(x), is given by
P0:T
 x0, . . . , xT

= ν(x0)p(x0, x1) . . . p(xT−1, xT) .
(12)
Then the probability density function at the time instant i is denoted as νi(x)
and given by
νi(x) =
Z
L
· · ·
Z
L
ν(x0)p(x0, x1) . . . p(xi−1, x)dx0 . . . dxi−1 ,
i=1, 2, ..., T ,
where ν0(x) := ν(x).
In the same line, consider a parameterized transition probability density
function qθ(x, x′), which depends on the parameter vector θ ∈Θ for x, x′ ∈L.
Its path space probability distribution, starting from νθ(x), is given by
Qθ
0:T
 x0, . . . , xT

= νθ(x0)qθ(x0, x1) . . . qθ(xT−1, xT ) .
(13)
The pathwise relative entropy can be decomposed as (see Appendix)
R(P0:T ∥Qθ
0:T ) = R(ν ∥νθ) +
T
X
i=1
R(Pi ∥Qθ
i ) ,
(14)


## Page 13


13
where the following quantity
R(Pi ∥Qθ
i ) = Eνi−1
Z
L
p(x, x′) log p(x, x′)
qθ(x, x′)dx′

,
(15)
can be interpreted as the “instantaneous relative entropy”.
3.3. Pathwise Fisher information matrix of a parameterized distribution
In this work, we employ fast parametric screening with controlled accu-
racy to detect and discard (eliminate or ﬁx) parameters considered insensi-
tive. This screening step is based on sensitivity indexes that can be bounded
by the pathwise Fisher information matrix (pFIM), which is presented in this
section. We stress that in the high-dimensional RN case, fast screening is
especially important due to the large number of parameters that increase by
orders of magnitude the computational work when compared to the simula-
tion of the model. We refer to [53, 72] for further details.
Consider a vector ǫ ∈RK such that c+ǫ is a small perturbation of the
model parameter vector c with non-negative components. Assume that the
instantaneous pathwise relative entropy R(P c
i ∥P c+ǫ
i
) is smooth with respect
to c. Then, in combination with its non-negativity property, it can be Taylor-
expanded around c (see Theorem 9.2 in the Appendix) to obtain
R(P c
i ∥P c+ǫ
i
) = 1
2ǫtrIH
 P c
i

ǫ + O(|ǫ|3) ,
(16)
where
IH
 P c
i

= Eνc
i−1
Z
L
pc(x, x′)∇c log pc(x, x′)∇c log pc(x, x′)trdx′

(17)
is the instantaneous Fisher information matrix associated to the instanta-
neous relative entropy. The Fisher information is a measure of the amount
of information that a random variable contains regarding a set of parameters.
An appealing property is that the FIM is independent of the perturbation
vector, ǫ, and contains up to third order accuracy the sensitivity information
as it is quantiﬁed by the relative entropy. Consequently, the pathwise FIM,
i.e., the Hessian of the pathwise relative entropy at c is given by
I
 P c
0:T

= I
 νc
+
T
X
i=1
IH
 P c
i

,
(18)


## Page 14


14
where I
 νc
= Eνc [∇c log νc(x)∇c log νc(x)tr] is the FIM of the initial distri-
bution.
Block diagonal structure of the pFIM. As previously mentioned, reaction
channels of biochemical reaction networks typically depend on a reduced
number of parameters, which determine a block diagonal structure of the
pFIM. This parametric dependence allows to reduce the computational work
of the quantities to estimate from O(K2) to O(K). This reduction may be
essential in the high-dimensional case. In Figure 1 we show two examples of
the block structure of the pFIM.
0
20
40
60
80
Parameters
0
10
20
30
40
50
60
70
80
Parameters
Proctor2011-Protein-Homeostasis-NC
0
10
20
30
40
50
Parameters
0
5
10
15
20
25
30
35
40
45
50
Parameters
EGFR
0
10
20
30
40
50
Parameters
0
5
10
15
20
25
30
35
40
45
50
Parameters
Leloup2003-CircClock-DD
Figure 1: Pathwise FIM block structure in the three models presented in Section 6. Pro-
tein Homeostasis model [55], Epidermal Growth Factor Receptor (EGFR) model [56] and
Mammalian Circadian Clock model [57]. We notice that the sparsity of the pathwise FIM
allows to reduce the computational work from O(K2) to O(K).
Remark 3.1 (Fisher information for model reduction). Fisher information
matrices has been used before in the context of model reduction for reaction
networks (see [2] and references therein). However, these information matri-
ces are diﬀerent from our pathwise FIM. In [2] the matrix is computed based
on the adjoint system (29), so the computational work issue still remains. In
[73] the authors assume that the quantities of interest (measurements) are
aﬀected by identically distributed and independent Gaussian noise. Then,
the Fisher information matrix of these independent measurements is com-
puted. Similar comments apply to [74, 75]. We stress here that our pFIM is
computed by taking into account the Markovian dynamics of the process and
therefore, taking into account its intrinsic noise (see (18)).
Remark 3.2 (Pathwise FIM for Stochastic Reaction Networks). The pFIM


## Page 15


15
over an interval [0, T] is given by
I(P c
[0,T]) = I(νc) +
Z T
0
IH(P c
t )dt ,
where I(νc) is the FIM of the initial distribution and the process P c
t can be
viewed as the instantaneous pFIM given by
IH(P c
t ) = EP c
[0,t]
" J
X
j=1
aj(Xt−; c)∇c log aj(Xt−; c)∇c log a(Xt−; c)tr
#
,
(19)
where Xt−denotes the left side limit at time t. The transition probabilities
for the embedded discrete time Markov chain deﬁned as (Zn)n∈N := X(tn),
where tn is the time of the n-th jump, are given by
p(x, x+νj; c) := aj(x; c)
a0(x; c) ,
j=1, 2, ..., J ,
(20)
for X(tn)=x →X(tn+1)=x+νj, assuming a0(x; c)>0.
Remark 3.3. In many applications, model parameters diﬀer by several or-
ders of magnitude, so we perform relative parameter perturbations. This is
done by perturbing the logarithm of the parameters. Using the chain rule on
∇log cpc we obtain

I(P log c
0:T )

k,l = ckcl (I(P c
0:T ))k,l ,
k, l = 1, ..., K .
(21)
Note that (16) continues to be valid for the logarithmic scale.
From
now, we use relative parameter perturbations, i.e., we use I(P c
0:T ) to denote
I(P log c
0:T ).
3.4. Scalable information-based sensitivity indexes
In this section we discuss a scalable information-based inequality that
connects observables of the system with the pFIM, and we present a reliable
sample-free implementation.
Relative entropy provides a rigorous and computationally tractable method-
ology for parameter sensitivity analysis of complex, stochastic dynamical sys-
tems focusing on the sensitivity of the entire probability distribution. How-
ever, in most simulations of biochemical networks, the main interest are


## Page 16


16
observables such as population means, variances or time averages, as well as
autocorrelations or extinction times. Therefore, it is reasonable to connect
parameter sensitivities with observables. Given a pathwise distribution P c
0:T,
let
DF,k := ∂EP c
0:T [F]
∂ck
,
(22)
be the classical local sensitivity index, then the following information-based
bound
|DF,k| ≤
q
VarP c
0:T [F]
q
(I(P c
0:T))k,k ,
(23)
can be obtained by rearranging the generalized Cramer-Rao bound for esti-
mators of the form
F((xi)T
i=1) = 1
T
T
X
i=1
f(xi)∆ti ,
with f a suitable observable. Here (I(P c
0:T))k,k denotes the k-th diagonal
element of the pathwise Fisher Information Matrix (pFIM). For a given ob-
servable, this inequality can be used as an indicator that allows to classify
–even in the presence of a very high-dimensional parameter space– insensitive
parameters, in the sense that a small pFIM diagonal value suggests relatively
low SIs. In the same way, large pFIM values suggest high SIs. However, no-
tice that large or small pFIM values does not imply sensitive or insensitive
parameters respectively. We refer to [53, 72, 54] for further details. In this
work, we focus instead on the following normalized local sensitivity index
DF,k :=
∂EP c
0:T [F ]
∂ck
q
VarP c
0:T [F]
,
(24)
which has the advantage of capturing how “noisy” each observable is, and
therefore, weights the sensitivity accordingly, meaning that perturbations in
the expected value of F are less signiﬁcant when its variance is large. Then
we readily have the sensitivity bound
|DF,k| ≤
q
(I(P c
0:T ))k,k .
(25)
In this work, since we focus on model reduction, we mainly consider the
observable f(x) = x, that is, F is the time average of the state variables


## Page 17


17
(species)
F((xi)T
i=1) := 1
T
T
X
i=1
xi∆ti .
(26)
Despite of this, further observables may be considered in the last step of
our method, in which the reduced model may be augmented with additional
parameters depending on particular quantities of interest.
3.5. Mean-ﬁeld estimation of the pFIM
Here we discuss a classical mean-ﬁeld type of approximation to avoid
sampling of (17). For such cases in which sampling is not feasible, either
due the high dimension of the system or due to the fact that the available
data is limited, a deterministic approximation is usually the only alternative.
The linear noise approximation can be used to eﬃciently compute the pFIM,
while maintaining controlled bias in the statistical estimators. First notice
that, under certain conditions and properly scaling the state variables, the
CLE can be written as
Y (t) = z(t) + ηξ(t)
(27)
where z(t) is the deterministic mean-ﬁeld part that satisﬁes (7), ξ(t) is a zero-
mean external noise process and η is the amplitude of this stochastic term,
which is proportional to the inverse square root of the reactant populations
[69, 76, 68, 67, 53]. Thus, for large populations, the dominant part of the
stochastic process is the deterministic term whose dynamics are governed
by the ODE system (7). Assuming the process starts at a ﬁxed value, the
diagonal elements of the pFIM (19) are approximated using (27) to get
(I(P c
0:T ))k,k ≈
T
X
i=1
J
X
j=1
aj(zi; c)
∂log aj(zi; c)
∂ck
2
∆ti .
(28)
Here the sequence (zi)T
i=0 corresponds to the mean-ﬁeld part of (27). This
approximation is usually valid for large populations and usually cannot cap-
ture complex dynamics such as bistability nor exit times nor rare events.
Here we use the time series data (11) in place of the sequence (zi)T
i=0.
Due to the parametric sparsity usually found in biochemical models,
i.e., (4), we can assume that the computational work required to compute
these quantities is of the order O(K) per timestep.
In contrast, most of
the sensitivity-based reduction methods require to solve the classical para-
metric sensitivity adjoint system (29), which requires work on the order of


## Page 18


18
O((K+1)×d), where d is the number of state variables, as presented in the
next remark.
Remark 3.4 (Classic parametric sensitivity system). The classic parametric
sensitivity analysis for deterministic reaction networks consists of solving the
coupled system:



dz = b(z; c)dt
dsk = ∂b
∂zskdt + ∂b
∂sk
dt ,
k=1, ..., K , t ∈R+ , ,
(29)
where b(z; c) = νa(z; c), z ∈Rd are the state variables, and c ∈RK is the
parameter vector, for the sensitivity indexes
sk := ∂z
∂ck
,
k=1, ..., K .
(30)
The ﬁrst line of the coupled system (29) is the reaction-rate ODE system,
which approximates EP0:T [F], i.e.
the expected value of a pathwise quan-
tity of interest of the form
1
T
R T
0 f(z(s))ds, where f is a suitable observable.
The computational work required for integrating this system is of the order
of (K+1) × d per timestep, which renders this method unfeasible for high-
dimensional systems. The alternative Green’s function method allows to solve
this system using work of order of d × d. For d ≫1 and K ≫1 this method
turns to be impractical especially taking into account that the system is usu-
ally stiﬀ.
4. Variational model reduction in path-space
In this section we present one of the main results of this work: a simpliﬁed
loss function that allows to ﬁnd a solution to the variational inference problem
(31) in the macroscopic space state by using available microscopic data time
series (11).
4.1. Variational inference and coarse-graining
Here we brieﬂy recap the variational inference approach. Variational in-
ference is a machine learning technique for approximating probability dis-
tributions [77, 78], and is widely used to approximate posterior densities in
Bayesian models, as an alternative strategy to Monte Carlo sampling. Com-
pared to Monte Carlo sampling, tends to be faster and more scalable to large


## Page 19


19
datasets [79]. Instead of using sampling, the main idea of variational infer-
ence is to apply optimization, and therefore for complex models it provides
a relevant alternative approach.
In this work, we aim to construct a suitable reduced parametric model
and to ﬁnd the optimal set of parameters that minimizes the information loss
in an eﬃcient and principled manner. This is achieved by means of a loss
function based on the following relative entropy minimization
θ∗:= θ∗
0:T := arg min
θ∈Θ R(P0:T ∥Qθ
0:T) .
(31)
We seek for this optimal solution θ∗based on the following ﬁrst order
optimality condition,
∇θR(P0:T ∥Qθ∗
0:T ) = 0 ,
whose solutions reveal the local optima of the relative entropy in the micro-
scopic state space. Notice that if the relative entropy is a strictly convex
function then there is a unique global minimum. This clearly depends on the
choice of the parameterized model (see [50]). For example, if the parameter-
ized model depends linearly on θ then there is a unique global minimum and
the problem reduces to solve a linear system. In this work, the parameterized
model is constructed by using the original propensity functions, assumed to
be an analytical function.
In what follows, we present two such loss functions; the ﬁrst one is equiv-
alent to solving the problem (31) (see Theorem 4.1), and the second one is
an upper bound but is computationally less demanding.
4.2. Building the approximating parametric family
Since the main goal of this work is to construct a reduced model for a
high-dimensional RN, we start by considering the application of the linear
map Π : Rd →R
¯d.
Examples of these maps used in the literature for
molecular systems (called coarse-graining maps) include the mapping to the
centers of mass of groups of particles, or a projection on a speciﬁc set of
particles, among others. Without losing generality, in this work we consider
the following map. For x ∈Rd let Π be such that
x 7→(Πx, Π⊥x) = (¯x, ˆx)
(32)
where ¯x ∈R
¯d is the macroscopic state, and ˆx ∈Rd−¯d. If we denote with
the same symbol Π ∈R
¯d×d the matrix representation of the map, then Π


## Page 20


20
together with Π⊥form a permutation matrix. This Π map determines the
macroscopic state, ¯x, as a function of the full model state x. Further details
of this map can be found on Section 5.4.
Assuming the data is generated by means of the Euler discretization of
the CLE (see (11)) is clear that xi is a multivariate Gaussian random variable
for i=1, 2, ..., T. We can then split the transition density in the microscopic
state space (see (12)) as
p(x, x′) = p(1)(x, ¯x′)p(2)(x, ¯x′|ˆx′) ,
for x, x′ ∈Rd, ¯x′∈R
¯d ,
and the associated microscopic parameterized transition density (see (13))
as
qθ(x, x′) = r(x′|¯x′)pθ(¯x, ¯x′) ,
for x, x′∈Rd, ¯x′∈R
¯d ,
(33)
where r is a reconstruction density independent of θ, and pθ is the density
of the reduced model. This reconstruction density essentially recovers the
lost degrees of freedom and, together with pθ, approximates the microscopic
density.
This reconstruction density serves as an auxiliary tool that con-
nects the reduced dynamics with the full dynamics on the same space. The
important fact of this density is that it is independent of θ and can be ar-
bitrarily chosen.
In this work, we do not focus on this auxiliary density,
since it is not relevant in our optimization procedure.
We have then the
original transition density p which is associated with the path distribution
P0:T. For the Euler CLE case, the forumla is given by equation (12). Then,
we have the parameterized approximation to the original microscopic path
distribution P0:T, i.e., Qθ
0:T, which is associated to the transition density qθ.
For the Euler CLE case, the formula is given by equation (13). Finally, we
have the transition density pθ (see (33)), which is associated with the path
distribution of the reduced model, which lives in the macroscopic space. The
main goal of this work is to construct a reduced model which corresponds
to this transition density. In Section 5 we show how to construct this re-
duced model, which can be described by a ¯d-dimensional time dependent
state vector ¯x = Πx, and ¯J reaction channels ((¯νj, ¯aj)) ¯J
j=1, where ¯νj is a ¯d-
dimensional state change vector properly constructed by considering the full
model stoichiometry, and ¯aj = ¯aj(¯x; θ), j=1, 2, ..., ¯J its propensity functions,
with θ ∈Θ a ¯K-dimensional vector of model parameters. The deﬁnition of
¯ν is given in (51) while th deﬁnition of ¯a is given in (53).
In this work, propensity functions in the reduced model have the same
functional form of the corresponding full model propensity functions. Two


## Page 21


21
main reasons apply. First, from the modeling point of view, usually it is desir-
able that the functional form of the propensity functions belong to the same
parametric space as the full model. In the biochemical literature, propensity
functions usually include mass-action and Michaelis-menten type of expres-
sions, but may in general include closed form expressions. As a consequence
the dependence of the propensity functions on the parameters is usually non-
linear. Second, in the context of biochemical reaction networks, each state
variable is associated with a diﬀerent species and in some cases with physical
location. Therefore, even a linear transformation may be diﬃcult to interpret
and thus render the reduction meaningless.
4.3. Loss function for time-series data training
The following theorem allows to connect the optimization problem (31)
with the macroscopic space of state variables. This theorem also provides a
pathwise relative entropy representation for the Euler CLE case and shows
computable quantities that can be trained by means of the microscopic data.
Theorem 4.1. Let P0:T be the path distribution of the Euler CLE approxima-
tion of a RN ((νj, aj))J
j=1, and Qθ
0:T be the path distribution of a parameterized
approximation. Let Π : Rd →R ¯d be a linear map as in (32). Then, we have
arg min
θ∈Θ R(P0:T ∥Qθ
0:T) = arg min
θ∈Θ [R0:T(θ) + M0:T(θ)]
(34)
where
R0:T(θ) :=
T
X
i=1
Ri(θ),
M0:T (θ) :=
T
X
i=1
Mi(θ)∆ti ,
∆ti>0 ,
and
Ri(θ) := 1
2Eνi−1

Trace
 ΠΣ(x)Πtr ¯Σ−1(¯x; θ)

−log det
 ΠΣ(x)Πtr ¯Σ−1(¯x; θ)

,
(35)
Mi(θ) := 1
2Eνi−1

(¯b(¯x; θ) −Πb(x))tr ¯Σ−1(¯x; θ)(¯b(¯x; θ) −Πb(x))

.
Here Σ(x) = σ(x)σtr(x), where σ(x) = ν
p
diag(a(x)) and b(x) = νa(x)
are the diﬀusion and drift coeﬃcients of the RN ((νj, aj))J
j=1 respectively.
Moreover, ¯Σ(¯x; θ) = ¯σ(¯x; θ)¯σtr(¯x; θ) with ¯σ and ¯b the reduced RN ((¯νj, ¯aj)) ¯J
j=1
diﬀusion and drift coeﬃcients respectively.


## Page 22


22
The proof of this Theorem is presented in the Appendix. Notice that
this result allows to optimize the parameter vector θ by considering the drift
associated to the reduced model, ¯b(¯x; θ) = ¯ν¯a(¯x; θ), and the projected mi-
croscopic drift, Πνa, instead of the microscopic drift, since the pathwise
quantities R0:T(θ) and M0:T(θ) can be computed in the macroscopic state
space.
The macroscopic pathwise quantity
F0:T(θ) := R0:T(θ) + M0:T (θ)
(36)
can be then interpreted as a pathwise loss function whose minimization al-
lows to determine the optimal value of the approximating distribution set of
parameters. We notice that the R0:T term acts as a penalization term for
M0:T by the discrepancy of ¯Σ from ΠΣΠtr.
A simpliﬁed loss function. Next, we derive a simpliﬁed loss function from
(36) that substantially simpliﬁes the numerical method search space, and
therefore the associated computational work to ﬁnd its solution. First we
notice that
Ri(θ) ≥
¯d
2,
for θ ∈Θ ,
(37)
with equality if and only if ¯Σ = ΠΣΠtr. This is proved in Proposition 9.4
(see Appendix). Replacing in (36) ¯Σ by ΠΣΠtr we obtain
F0:T(θ)
¯Σ=ΠΣΠtr = R0:T(θ) + M0:T (θ)
¯Σ=ΠΣΠtr
= T
¯d
2 +
T
X
i=1
Mi(θ)
¯Σ=ΠΣΠtr∆ti
= T
¯d
2 + 1
2
T
X
i=1
Eνi−1

∥¯b(¯x; θ −Πb(x))∥2
Π

∆ti ,
where ∥· ∥2
Π is deﬁned as
∥z∥2
Π := ztr(ΠΣΠtr)−1z .
(38)
Finally, ignoring the constant T
¯d
2 we have the following simpliﬁed loss
functional
E0:T(θ) := 1
2
T
X
i=1
Eνi−1

∥¯b(¯x; θ) −Πb(x))∥2
Π

∆ti .
(39)


## Page 23


23
By applying the same approximation as in Section 3.5, i.e. (27) we obtain
E0:T(θ) ≈ˆE0:T(θ) := 1
2
T
X
i=1
∥¯b(Πzi; θ) −Πb(zi)∥2
Π∆ti .
(40)
As before, the sequence (zi)T
i=0 corresponds to the mean-ﬁeld part of (27),
replaced by the time series data (11).
We then solve the following optimization problem
min
θ∈Θ
ˆE0:T(θ) ,
(41)
by considering steepest descent and Newton-Raphson type of methods, re-
calling that the Hessian of the relative entropy is the Fisher Information Ma-
trix. In this work, we do not explore further this topic, and we use instead
standard optimization packages to ﬁnd a numerical solution, in particular
MATLAB 2016b.
We emphasize that the CLE formulation is only required to derive the
loss function which allows to ﬁnd an approximate solution of the variational
problem (31). The loss function is suitable to be applied in non-Langevin
regimes, as we show in the pure jump stochastic models in Section 7.
Remark 4.2. The loss functions (36) and (41) may be regularized by using
penalization terms like Tichonov or L1 to simplify the optimization procedure
or to obtain a more parsimonious model. For example we can solve
min
θ∈Θ
1
2
T
X
i=1
∥¯b(Πzi; θ) −Πb(zi)∥2
Π∆ti + λ∥θ∥2
Π ,
(42)
where λ is a parameter to determine (see [80, 81, 82] for additional refer-
ences).
Remark 4.3. One of the computational novelties of our method lies in
the derivation and implementation of a pathwise force matching condition
(termed Dynamic Force Matching) such as (41) and Theorem 4.1, where the
norm is now ∥· ∥2
Π instead of the Euclidean one. The classic force match-
ing method can be viewed as a particular case (see for instance [83, 84] and
references therein).


## Page 24


24
Remark 4.4. The optimization principle in (34) can be further extended
to obtain an improved time-dependent optimal parameterization, which is
obviously more demanding in terms of computational work. That is, obtain
θ∗
0:T = (θ∗
i )T
i=1,
i=1, 2, ..., T ,
by optimizing
arg min
(θi)T
i=1
1
2
T
X
i=1
Eνi−1

∥¯b(¯xi; θi) −Πb(xi))∥2
Π

∆ti .
Remark 4.5. In the case that the matrix ¯Σ is singular, the conclusions
of Theorem 4.1 are still valid, by means of the Moore-Penrose generalized
inverse instead of the inverse, and the pseudo-determinant instead of the
determinant in (35). We refer to [35] and references therein for additional
details.
In the next Section we present a procedure to construct a reduced model,
i.e., how to choose ¯ν and ¯a, such that ¯b = ¯ν¯a and ¯σ = ¯ν
p
diag(¯a) are the
drift and diﬀusion terms of the reduced model.
Remark 4.6. The drift of the reduced model, ¯b, may be alternatively con-
structed by using the fact that most physical models of the form have only a
few relevant terms that deﬁne the equations of motion of the system (i.e. the
RHS of the system ˙x(t) = f(x)). These methods are called sparse identiﬁca-
tion of nonlinear dynamics (see for instance [85, 86]). Since the construction
can be considered on reduced space by virtue of Theorem 4.1, this certainly
mitigates one of the main drawbacks of the aforementioned methods, that
is, when data is high-dimensional and therefore the state dimension of the
dictionary of candidate functions is usually prohibitively large.
5. Model reduction procedure
In this section we present an information-based model reduction pro-
cedure for high-dimensional reaction networks. The goal is to construct a
suitable reduced model in a principled and eﬃcient manner using the tools
developed in Section 3.4. This reduction is achieved in several steps as fol-
lows. In Section 5.1 we present a summary of the steps, in Section 5.2 we
show how to identify the most sensitive parameters, in sections 5.3 and 5.4 to


## Page 25


25
use the stoichiometry of the network to choose the associated variables and
reaction channels. In Section 5.5 we show how to construct a paramterized
family of reduced models to then in Section 5.6 how to ﬁnd an optimal model.
Finally, in Section 5.7 we show how to validate and iteratively improve the
reduced model obtained in the previous steps.
5.1. Summary of the reduction method
The reduction method presented here can be described in 6 steps as fol-
lows.
Step 1. Selecting parameters and reaction channels. The reduction method
starts with the estimation of the full model pFIM (18) by using the available
time series (11) to determine the parameters that accumulate at least κ%
(usually 97% or 99%) of the total information. This criterion determines a
set of parameter indexes P ⊆{1, 2, ..., K} to include in the reduced model
and later train (in Step 4). By means of the ϕ map, (3), we determine a
set of reaction channel indexes to include in the reduced model, JP. This
set is if indexes correspond to reactions that include at least one sensitive
parameter as per the pFIM diagonal. Finally, notice that parameter map Γ
(55) is also determined by P.
Step 2. Selecting variables. Given the set of reaction channels JP from
Step 1, deﬁne a state variable map Π that contains every species that takes
part in the stoichiometry of any reaction j ∈JP. The set of species (or state
variables) that satisﬁes the aforementioned relation, are selected to be the
species of the reduced model, and denoted by SP.
Step 3. Construction of a parameterized family of reduced models. Given
JP and SP, construct a family of candidate reduced models of the form
((¯νj, ¯aj)) ¯J
j=1, parameterized by the sensitive parameters of the full model in
the sense (25), and taking into account the stoichiometry structure. This
step includes the deﬁnition of ¯νj and ¯aj = ¯aj(¯x; θ), where θ is the parameter
vector of the reduced model.
Step 4. Model training. By means of the loss function (40) the reduced
model parameters, denoted by θ, are ﬁtted to the time series data (11). This
optimization also provides a goodness-of-ﬁt in terms of entropy loss.
Step 5.
Validation.
Determine if further reaction channels should be
added to the reduced model, by means of computing a suitable distance on
the time series data (11).
Step 6. Iteration. Finally, previous steps can be subsequently iterated
to obtain either alternative or further reduced models that may provide a


## Page 26


26
better ﬁt.
The model reduction process (Step 1–6) is depicted in Figure 2.
Full Model:
((νj, aj))J
j=1
Data: (xi)T
i=0
(11)
Compute diag(pFIM) (18)
Determine JP (48)
Information
threshold
(46)
Construct Γ (55) and Π (57)
Stoichiometry:
νin, νout
Construct parameterized family of reduced models: ((¯νj, ¯aj(·; θ))) ¯J
j=1
Loss function (40) training to get θ∗
Reduction ok?
user deﬁned
error TOL
Output:
((¯νj, ¯aj(·; θ∗))) ¯J
j=1
yes
no
iterate
Figure 2:
Main steps in the information-based model reduction method for high-
dimensional reaction networks method (see Section 5.1).
5.2. Parameter selection (step 1)
By means of the information-based bound (25), we focus our sensitivity
analysis of the full model on
ξk := (I(P0:T))k,k ,
(43)
which are the diagonal elements of the pFIM (18) of the full model, which
has pathwise distribution P0:T (14) and parameter vector c. This corresponds


## Page 27


27
to perturbations of full model parameters in the canonical directions, where
ξk corresponds to parameter ck.
Let ξσ(1) > ξσ(2) > ... > ξσ(K) be the ordering from highest to lowest
of the diagonal elements ξk where σ denotes a sorting permutation of the
indices. So σ(1) is the index of the parameter with the largest diagonal value
in the pFIM. In the case that the pFIM is diagonal, this is equivalent to the
sorted eigenvalues of the pFIM. Given the ordered set of diagonal elements,
{ξσ(1), ξσ(2), ..., ξσ(K)}, we say that the percentage of information contained in
the corresponding parameters {σ(1), σ(2), ..., σ( ¯K)} is
Ξ ¯
K :=
1
Trace (I(P0:T))
¯
K
X
ℓ=1
ξσ(ℓ) ,
(44)
where ξk is deﬁned in (43).
Now deﬁne
P := {σ(1), σ(2), ..., σ( ¯K)} ⊆{1, 2, ..., K}
(45)
as the set of parameter indexes intended to keep in the reduced model, such
that
Ξ ¯
K ≥κ ,
(46)
where κ is a user deﬁned threshold that represents (κ × 100)% of the total
information preserved in the reduced model as per the trace of the full model
pFIM. We collectively call these parameters as pFIM-sensitive parameters.
In the examples studied in Section 6, keeping the parameters whose pFIM
values accumulate at least 95% of the total sum is enough to include all
sensitive parameters for the time average of the species, in the sense of (29).
More precisely, the reduction of the parameter space is considered as the
application of a full rank linear map Γ : RK →R ¯
K such that
c 7→(Γc, Γ ⊥,1c, Γ ⊥,2c) = (θ, u, ˜c) ,
(47)
where c ∈RK is the full model parameter vector, θ ∈Θ := R ¯
K is the vector
of sensitive parameters, u ∈R ¯
K′ is the vector of insensitive parameters but
still relevant for the reduction as explained below, and ˜c is the vector of
irrelevant parameters.
This map determines a partition in the full model parameter space, identi-
fying sensitive parameters that will be included as parameters in the reduced


## Page 28


28
model i.e., θ = Γc, insensitive but relevant parameters that will be included
as constants in the reduced model i.e., u = Γ ⊥,1c, and irrelevant parameters
that will be eliminated from the reduced model, i.e., ˜c = Γ ⊥,2c.
The distinction between θ and u is relevant when ﬁtting the reduced
model to the given time series data (11) (see Step 4). This ﬁtting is achieved
by minimizing the information loss between the full model and the param-
eterized reduced model, and the number of dimensions of this optimization
problem is given by the number of parameters of the reduced model. The
linear map Γ is depicted in Figure 3.
(c1, c2, ..., cK)
(θ1, θ2, ..., θ ¯
K)
(u1, u2, ..., u ¯
K′)
˜c
parameters
(trained in Step 4)
constants
(ﬁxed)
non-resolved
(eliminated)
Full model:
Reduced model:
Γ
Γ ⊥,1
Γ ⊥,2
Figure 3: Schematic representation of the linear Γ mapping, from full model parameters
to reduced model parameters.
Remark 5.1. Further information can be extracted from the pFIM (18), for
example, the spectral analysis reveals the most and the least sensitive direc-
tions of the system around c, which corresponds to the eigenvector with the
largest/smaller smaller eigenvalue. In the same direction, parameter identi-
ﬁability can also be studied. Parameter identiﬁability is satisﬁed when all the
eigenvalues of the pFIM are above a certain threshold (see [87]). For exam-
ple, when the determinant one of the blocks is zero then the corresponding
linear combinations of parameters are non-identiﬁable.
5.3. Reaction channel selection (Step 1)
Here we describe how reaction channels are selected in order to keep the
most sensitive ones in the sense explained below. Notice that this is not the
only way to select the relevant reaction channels. Given a set of sensitive
parameter indexes P (eq.
(45)), the set of sensitive reaction channels is
deﬁned as the full model reaction channels that contain at least one sensitive


## Page 29


29
parameter (indexed by P), i.e.,
JP :=
[
k∈P
ϕ(k) ,
(48)
where JP is the set of indices of reaction channels that depends on the set
of parameter indexes P, with |JP| = ¯J. That is, if j ∈JP then exists k ∈P
such that the propensity function aj explicitly depends on the parameter ck.
The formal deﬁnition of the reduced model propensity function is given in
Section 5.5, equation (53).
5.4. Selecting variables (Step 2)
Here we describe how the matrix representation of the state variables full
rank linear map Π : Rd →R ¯d, such that
x 7→(Πx, Π⊥,1x, Π⊥,2x) = (¯x, ¯y, ˜x) ,
(49)
is constructed. Here ¯x ∈R ¯d is the state space of the reduced model, i.e.,
the microscopic variables that take part in the stoichiometry of the selected
reaction channels; ¯y ∈R
¯d′ is the set of microscopic state variables that are not
part of the stoichiometry of the selected reaction channels; and ˜x ∈Rd−¯d−¯d′
is the set of microscopic state variables that are not included in the reduced
model.
Given the set of sensitive reaction channels JP (eq. (48)) , the map Π
is in fact a projection on a smaller number of variables ¯x, corresponding
to the species that take part in the stoichiometry of the sensitive reaction
channels. In this way, the state variables included in the reduced model are
determined by JP and the stoichiometry structure of the full model, that is,
νin and νout. We denote with SP the set of indexes of variables that take part
on the stoichiometry of the sensitive reaction channels JP, i.e.,
i ∈SP ⇐⇒
exists j∈JP for which (νin)i,j > 0 or (νout)i,j > 0 .
(50)
These variables are selected because are part of the stoichiometry of the
sensitive reaction channels, and therefore are considered necessary for con-
structing the reduced model.
Since a propensity function may depend on any state variable, and not
only the ones that take part in the stoichiometry, we deﬁne the complement
of Π by Π⊥,1 and Π⊥,2. The ﬁrst one takes into account, for each j ∈JP, the


## Page 30


30
state variables that are included in the respective propensity function j and
not in the stoichiometry reaction channel j. In this work, those state variables
are not included in the reduced model as variables, but time averages, as
explained below in Section 5.5.
Those variables are in fact relevant but
not necessary for constructing the reduced model, and therefore modeled as
constant values. The linear map Π is depicted in Figure 4.
(x1, x2, ..., xd)
(¯x1, ¯x2, ..., ¯x ¯d)
(¯y1, ¯y2, ..., ¯y ¯d′)
˜x
variables
constants
(time averages)
non-resolved
(eliminated)
Full model:
Reduced model:
Π
Π⊥,1
Π⊥,2
Figure 4: Schematic representation of the full model state variables to reduced model state
variables.
5.5. Construction of a parameterized family of reduced models (Step 3)
Here we present a particular method to construct the parametric family
of reduced models. Let (νj, aj)J
j=1 be the full RN, as deﬁned in Section 2.
Let P be a set of parameters to include in the reduced model, and JP be
the corresponding set of reaction channels (from Step 1 and Step 2). Let
¯x = Πx denote the macroscopic state, and recall that x can be decomposed
as (Πx, Π⊥,1x, Π⊥,2x) = (¯x, ¯y, ˜x) (49). Let θ = Γc denote the reduced model
parameter vector, and recall that the microscopic parameter vector can be
decomposed as (Γc, Γ ⊥,1c, Γ ⊥,2c) = (θ, u, ˜c) (47).
The reduced model stoichiometry is deﬁned as follows. For i ∈SP and
j ∈JP as
(¯νin)k,l := (νin)i,j for k = 1, 2, ..., ¯d, l = 1, 2, ..., ¯J ,
(51)
where the indexes k = k(i) and l = l(j) preserve the order of i and j, and
similarly for νout. Then ¯ν = ¯νout −¯νin.
Let x0:T denote the time average of the microscopic data (xi)T
i=0 (11),
x0:T := 1
T
T
X
i=1
xi∆ti .
(52)


## Page 31


31
for a non-uniform time step ∆ti.
We deﬁne the reduced model propensity functions as follows. For j ∈JP
there is a corresponding k = k(j) ∈{1, 2, ..., ¯J} such that
¯ak(¯x; θ) := aj((¯x, Π⊥,1x0:T); (θ, u)) ,
(53)
where ¯x ∈R
¯d, θ ∈R ¯
K.
Some observations apply. The reduced model propensity functions are
deﬁned to have the same functional form than its full model counterparts, but
evaluated at (¯x, Π⊥,1x0:T) and its parameters evaluated at (θ, u) (47). Since
j ∈JP, the full model propensity function aj depends explicitly on state
variables ¯x = Πx and ¯y = Π⊥,1x only. For the same reason, it only depends
explicitly on parameters θ = Γc and constants u = Γ ⊥,1c. Here we choose ¯y
to be equal to the projection of the time average of the data, Π⊥,1x0:T . This
is a natural choice consistent with long-term behaviour assuming that exists
the time-average limit of the mean ﬁeld approximation of the full model, z(t),
in the sense that limT→+∞
1
T
R T
0 y(t)dt = z∞, where z∞is a constant.
It is important to notice that this reduction method focuses on the stoi-
chiometry, i.e., structure of the reaction network, and not on the propensity
functions. This allows to take advantage of the natural sparsity of the ν ma-
trix and to use the full model function space for the reduced model propensity
functions.
5.6. Model training (Step 4)
Given the times series data (xi)T
i=0 (11) with non-uniform step ∆ti, we
numerically ﬁnd θ∗by maximizing the loss function (40)
arg min
θ
1
2
T
X
i=1
∥¯b(¯xi; θ) −Πb(xi))∥2
Π∆ti ,
(54)
where ¯b(¯x; θ) = ¯ν¯a(¯x; θ) and the norm ∥· ∥2
Π as in (38). Even though the
loss function E0:T(θ), as given by formula (39) is based on the Langevin
approximation, we can plug-in any time series as (11), by using the mean-
ﬁeld approximation discussed in Section 3.5.
5.7. Validation and improvement of the reduced RN (Step 5 and Step 6)
In this step, we assess the quality of the mean-ﬁeld trajectories generated
by a ﬁtted reduced model (as obtained in Step 4) and the mean-ﬁeld trajec-
tories generated by the full model. This comparison can be also performed


## Page 32


32
by using the times series data (11) instead of the full model mean-ﬁeld. We
opt for using the former one. Also, we discuss how the reduced model may be
expanded by adding reaction channels of a given species of interest. Suppose
that, in a given a ﬁtted reduced model with a set of species S, exists a species
of interest i ∈S such that
sup
t∈[0,T]
|zi(t) −¯zi(t)|
zi(t)
> TOL ,
where zi(t) denotes the full model mean-ﬁeld trajectory of the i-th state
component, and, similarily ¯zi, is the mean-ﬁeld trajectory generated with
the reduced model, for a user deﬁned relative tolerance TOL > 0. Since
the diagonal of the pFIM determines a linear order on the parameters, any
reduced model that can be obtained by changing the information threshold
κ are nested in terms of species and reaction channels. We now discuss an
idea to obtain models that are not attached to this nested hierarchy, focusing
on a one step analysis, that can be easily extended to a multi-step one by
traversing the graph deﬁned by the stoichiometry structure of the full model.
Let Ji be the set of reaction channel indexes such that for j ∈Ji, we have
(νin)i,j > 0
or
(νout)i,j > 0 ,
that is, Ji denotes the set of reaction channels in which species i ∈S takes
part in the stoichiometry. Then, if Ji\Jp is not empty, a new state variables
map can be deﬁned as in Section 5.4, equation (50), but using JP ∩Ji instead
of JP in (50). A simple illustration of this extension idea is presented in the
ﬁrst example of Section 6.2.
Remark 5.2 (Other strategies to construct the parameterized family). As
long as the state map Π is linear and orthogonal, the general form of the loss
function applies, assuming the data comes from an Euler discretization of
the CLE. Otherwise, the loss function needs to be rederived from the relative
entropy as we did in Theorem 4.1. To construct the state map, Π, one can
use our pFIM approach, or other criteria for variable selection.
Remark 5.3 (Computational work considerations of the reduced model con-
struction). One of the main advantages of the reduction method presented in
this work is its feasibility in terms of computational work. From the algorith-
mic point of view, there are three main computational steps to construct the
reduced model (not including the ﬁtting step):


## Page 33


33
1. Computing the pFIM (18) and determine the sensitive parameter set P:
As previously mentioned, in virtue of its block diagonal structure this
step can be achieved with a computational work roughly of the order of
the number of parameters of the full model, K.
2. Parameter mapping: Work to construct Γ (55) is of order K and to
construct Γ ⊥,1 (56) is linear on |JP|, which is of order of the number
of reaction channels, J.
3. State variable mapping: Work to construct Π (57) is linear on |JP|
which is of order J. Work to construct Π⊥,1 (58) is linear on |JP|
which is of order J, and requires additional storage of the order of the
dimension of the state space, d.
6. Numerical experiments
In this section we demonstrate the applicability of our method by analyz-
ing three models taken from the literature: A protein homeostasis network
in a sloppy regime [55], a Epidermal Growth Factor Receptor (EGFR) model
[56], and a Mammalian Circadian clock model that presents dymanics dom-
inated by oscillations [57]. Moreover, we present two stochastic pure jump
models: a circadian clock model which is based on [57], and a growth factor
receptor, based on [56] The parameter values, as well as initial conditions,
quantities of interest, and time horizon of the study are taken from the model
database [88, 89] (manually curated section). In the ﬁrst case, we consider
a particular regime studied in the corresponding paper, in which is possible
to obtain a substantial reduction both in the number of state variables (or
species) and in the number of parameters and reaction channels. In the sec-
ond example we analyze a non-sloppy model of signalling phenomena, and
ﬁnally, in the third example, we reduce a model whose dynamics are domi-
nated by non-trivial oscillatory behaviour. Finally, in Section 7 we scale the
deterministic Mammalian Circadian clock model and the EGFR to obtain
in each case a stochastic pure jump model. The ﬁrst one is clearly not in a
Langevin nor mean-ﬁeld regime. The second one is still well approximated
by the deterministic model. Both stochastic models exhibit non-Gaussian
distributions for some of the species. In all the examples, even though the
models were carefully designed by researchers, signiﬁcant model reductions
are achieved.


## Page 34


34
6.1. Matrix representations of the linear maps
Here we brieﬂy describe the matrix representations of Γ and Π used in
the numerical experiments. The matrix representation of Γ is constructed
(row-wise) as follows. The k-th row is deﬁned as
(Γ)k,· := el for k = 1, 2, ..., ¯K ,
(55)
for parameter index l ∈P and el is the l-th element of the standard basis
of dimension K, assuming the row index k preserves the order of index l.
Similarily, the k-th row of the matrix representation of the map Γ ⊥,1 is
deﬁned as
(Γ ⊥,1)k,· := el for k = 1, 2, ..., ¯K′ ,
(56)
for each parameter index l ∈{1, 2, ..., K} such that l ̸∈P but exists j ∈JP
such that j ∈ϕ(l). Finally, ˜cl is an component of ˜c if exists l ∈{1, 2, ..., K},
l ̸∈P and there is no j ∈JP such that j ∈ϕ(l).
Now, let P be a set of selected parameters, with |P| = ¯K, as deﬁned in
Section 5.2, and let JP = S
k∈P ϕ(k) be the set of indices of reaction channels
associated with the set of parameter indexes P. The k-th row of Π is then
deﬁned as
(Π)k,· := ei for k = 1, 2, ..., ¯d ,
(57)
for each species index i ∈{1, 2, ..., d} such that
exists j∈JP for which (νin)i,j > 0 or (νout)i,j > 0 ,
where ei is the i-th element of the standard basis of dimension d, assuming
that the row index k = k(i) preserves the order of index i as in (55). We de-
note with SP the set of indexes of species that take part on the stoichiometry
of the sensitive reaction channels JP.
The map Π does not take into account the case in which a propensity
function aj depends explicitly on a particular component of the state variable
x, say xi, and i ̸∈SP. Since the functional expression of the propensity func-
tions of the sensitive reaction channels are preserved in the reduced model,
a suitable complement, Π⊥,1, is deﬁned as follows.
For each reaction channel index j ∈JP such that
exists i∈{1, 2, ..., d},
such that aj = aj(xi; ·) and i ̸∈SP ,
deﬁne
(Π⊥,1)k,· := ei for k = 1, 2, ..., ¯d′ ,
(58)


## Page 35


35
where ()k,· denotes the k-th row of the matrix, ei is the i-th element of the
standard basis of dimension d, and aj = aj(xi; ·) denotes the fact that the
propensity function aj is an explicit function of xi. Here we assume that the
row index k = k(i) preserves the order of index i as in (55).
6.2. Protein homeostasis
Model description
Loss of protein homeostasis is the common link between neuro-degeneration
disorders which are characterized by the accumulation of aggregated protein
and neuronal cell death.
The authors in [55] examined the role of both
Hsp70 and Hsp90 under three diﬀerent regimes: no stress, moderate stress
and high stress. This reaction network consists of 52 species and 80 reactions
with propensities being of mass-action kinetics type. The reaction constants,
the initial population and time interval, [0, T], T=10, are taken from [55] and
[88]. The variables represent particle counts. This model can be well approx-
imated by a diﬀusion (CLE approximation (8)), since the particle count is
large for every species. The authors study a regime of no stress, in which most
of the classical sensitivity indexes as per (29) are close to zero. Recall that
we consider that a system is in a sloppy regime when most of the information
contained in the pFIM is accumulated in a reduced number of parameters
(see Figure 5). In this work, we study the Protein Homeostasis model in this
regime as an example of substantial model reduction, both in the number of
species and in the number of parameters and reaction channels. Every plot
shown refers to the time interval [0, T].
Selecting parameters and reaction channels (Step 1)
We start this example by noticing that 10 out of 87 parameters accumu-
late at least 95% (precisely, 96.524%) of the total information as per the pFIM
diagonal (44), as shown in Figure 5. Total information of a set of parameters
is a natural and intuitive measure that allows to choose a meaningful set of
parameters for information-based model reduction.
As a comparison, in Figure 6 we plot the sensitivity indexes of the time
average of the species (see (26)), computed by using the adjoint deterministic
method (see (29)). The time average is considered as a pathwise quantity of
interest for assessing the quality of the reduced model for replicating the full
dynamics. The axis containing the parameter indexes, are sorted by using
the diagonal values of the pFIM (see (25)). The group of parameters with


## Page 36


36
Other
14
13
10
 9
12
11
56
55
42
43
Parameter Index
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
0.18
0.2
Information Percentage
Total pctg not including "Other" = 96.524
Figure 5: Total information as per the pFIM diagonal (see (44) and (46)). It can be seen
that the parameters that represent at least 95% of the total information as per the pFIM
(10 parameters), contains the most sensitive parameters, as shown in Figure 6.
largest sensitivity indexes as per the adjoint method appears in the rightmost
side of the plot.
Figure 6: Sensitivity indexes for the time average of the species (see (29)). Parameter
axis is ordered by the diagonal of the pFIM. The computational work required to compute
these indexes is of the order of Parameters×Species.
By comparing both ﬁgures, we can note that the aforementioned 10 pa-
rameters, that represent more than 95% of the total information as per the
pFIM diagonal, include the most sensitive parameters as per the adjoint
method, for the time average of the species. This stresses the fact that by
considering a large amount of the total information as per the pFIM diago-
nal, sensitive parameters in the classical sense (29), for the time average, is


## Page 37


37
likely to be classiﬁed as pFIM sensitive. We empirically observed this fact
in several examples contained in the EMBL-EBI BioModels database [88].
Notice, however, that the two parameters that accumulate most of the infor-
mation as per the pFIM diagonal (parameters c42 and c43) are not sensitive
with respect to the time average (see the two rightmost part of the plot in
Figure 6). Finally, we recall that in the case of high-dimensional models,
the computational work required to compute the sensitivity indexes by the
adjoint and related methods is usually prohibitive (see Remark 3.4). On the
other hand, for computing the pFIM, a computational work of the order of
the number of parameters is required (see Section 3.3). This can be readily
seen by comparing Figure 6 with Figure 5.
In Figure 7 (left pane) we show the pathwise information geometry for the
full model, that is, how the total information is structured in the network
described by the stoichiometry.
This plot distinguishes sensitive reaction
channels (see (48)). We show reaction channels and species in a circumfer-
ence, where black dots depicts reaction channels and red dots, species. A
link between one reaction channel and one species shows the stoichiometry
structure, that is, which species takes part in the stoichiometry of which re-
action channels where the color of the link represents the total information
as per the pFIM diagonal of that particular reaction channel. That is,
j-th link color =
1
PJ
ℓ=1
P
k∈Kℓξk
X
k∈Kj
ξk ,
(59)
where ξk = (I(P0:T))k,k (eq. (43)), and Kj := {k∈{1, 2, ..., K} : j∈ϕ(k)}.
Finally, ϕ is deﬁned in (3).
Selecting variables (Step 2)
In Figure 7 (right pane) we show only the sensitive reaction channels
(48) and species (50), for κ = 0.95. Dotted lines shows, for the sensitive
species (i.e., included in the reduced model), the stoichiometry relations with
reaction channels not included in the reduced model. For example, species
S4 (see right pane of Figure 7) takes part in the stoichiometry of reaction
channel j=4 (R4 in Figure 7) but this reaction channel is not included in the
reduced model because contains no pFIM-sensitive parameters.
In this plot we can identify an almost isolated sensitive subsystem in
the stoichiometry of this network. That is, this network has a few sensitive
reaction channels that aﬀect only a few species, and those species are mainly


## Page 38


38
R:1
R:2
R:3
R:4
R:5
R:6
R:7
R:8
R:9
R:10
R:11
R:12
R:13
R:14
R:15
R:16
R:17
R:18
R:19
R:20
R:21
R:22
R:23
R:24
R:25
R:26
R:27
R:28
R:29
R:30
R:31
R:32
R:33
R:34
R:35
R:36
R:37
R:38
R:39
R:40
R:41
R:42
R:43
R:44
R:45
R:46
R:47
R:48
R:49
R:50
R:51
R:52
R:53
R:54
R:55
R:56
R:57
R:58
R:59
R:60
R:61
R:62
R:63
R:64
R:65
R:66
R:67
R:68
R:69
R:70
R:71
R:72
R:73
R:74
R:75
R:76
R:77
R:78
R:79
R:80
S:1
S:2
S:3
S:4
S:5S:6S:7S:8S:9S:10
S:11
S:12
S:13
S:14
S:15
S:16
S:17
S:18
S:19
S:20
S:21
S:22
S:23
S:24
S:25
S:26
S:27
S:28
S:29
S:30
S:31
S:32
S:33
S:34
S:35
S:36
S:37
S:38
S:39
S:40
S:41
S:42
S:43
S:44
S:45
S:46
S:47
S:48
S:49
S:50
S:51
S:52
Low
High
total pFIM per reaction channel
R:9
R:10
R:11
R:12
R:13
R:14
R:42
R:43
R:55
R:56
S:4
S:7
S:9S:10
S:11
S:12
S:13
S:14
S:23
S:31
S:40
S:41
Low
High
total pFIM per reaction channel
Figure 7: Stoichiometry and information. Black dots: reaction channels, red dots: species.
A link shows stoichiometry of each reaction channel. The color of the link shows the total
information of the corresponding reaction channel (see 59).
Left: Full model.
Right:
Reduced model, including at least 95% of the total information as per the pFIM diagonal
(44). In the plot, species indexes are shown, while species names are given in Figure 8.
aﬀected by those reaction channels. This latter is shown by dotted black
links in right pane of Figure 7).
Species Hsp70 and Hsp90 (S7 and S4 respectively, see Figure 8), which
are the main quantities of interest measured in [55], are already chosen in the
ﬁrst iteration of our method for κ=0.95. This is because both species take
part in the stoichiometry of a sensitive reaction channel for the speciﬁed κ.
Note that any particular species that may be of interest, even if it is sensitive,
can be also included in the reduction procedure presented in this work.
Reduced model (Step 3 and Step 4)
In Figure 8 we compare in a log scale the mean-ﬁeld trajectories of the
species included in the reduced model for κ=0.95, and the respective mean-
ﬁeld trajectories of the same species in the full model.
We also show a
comparison between the time average on [0, T] of the full model versus the
corresponding reduced one. Names of the species included in the reduced
model are given in both plots of Figure 8.
To visually compare how the amount of information as per the pFIM
included in the reduced model aﬀects the resulting mean-ﬁeld trajectories, in
Figure 9 we show, as in Figure 8, a comparison of the mean-ﬁeld trajectories
of the full model but in this case versus a reduced model for κ=0.93. It can
be clearly seen that the trajectory of one of the species in the reduced model
has very diﬀerent dynamics than in the full model. This explains why the


## Page 39


39
information loss and the pathwise distance are much larger than the case
with κ=0.95 (see Table 1).
0
2
4
6
8
10
Time
10 -2
10 -1
10 0
10 1
10 2
10 3
Species
Hsp90
Hsp70
Hsp70Client
Hsp70-Hsp70Client
Hsp90Client
Hsp90-Hsp90Client
Hsf1
Hsf1-Hsp90
Hsp70-Ppx
Ppx
Akt
Akt-Hsp90
Hsp90
Hsp70
Hsp70Client
Hsp70-Hsp70Client
Hsp90Client
Hsp90-Hsp90Client
Hsf1
Hsf1-Hsp90
Hsp70-Ppx
Ppx
Akt
Akt-Hsp90
10 1
10 2
10 3
Steady state of Species
Figure 8: Left: Mean-ﬁeld trajectories of the species indexed by SP. Solid lines correspond
to the reduced model and thick dashed lines to the full model at 95% of total information.
Right: Time average of species in the reduced model (circle), vs. the full model (star) at
95% of total information as per the pFIM diagonal.
0
2
4
6
8
10
Time
10 -8
10 -6
10 -4
10 -2
10 0
10 2
Species
Hsp90
Hsp70
Hsp70Client
Hsp70-Hsp70Client
Hsp90Client
Hsp90-Hsp90Client
Hsf1
Hsf1-Hsp90
Hsp70-Ppx
Ppx
Akt
Akt-Hsp90
Hsp90
Hsp70
Hsp70Client
Hsp70-Hsp70Client
Hsp90Client
Hsp90-Hsp90Client
Hsf1
Hsf1-Hsp90
Hsp70-Ppx
Ppx
Akt
Akt-Hsp90
10 0
10 1
10 2
10 3
Steady state of Species
Figure 9: Mean-ﬁeld trajectories and time average of species indexed by SP, at 93% of
total information. Dynamics of species Hsf1 is diﬀerent in the reduced model. Compare
the trajectories versus a reduced model with 95% if total information (Figure 8).
In Table 1 we show diﬀerent reduced models, according to total infor-
mation as per the pFIM (ﬁrst column).
In the second, third and fourth
columns we show the number of reaction channels, parameters and species
in the reduced model respectively. Column “Loss” shows the value of the
loss function (39) at which θ∗is achieved, by numerically solving problem


## Page 40


40
(54). When the information as per the pFIM diagonal increases from 95%
to 97%, the loss function at the optimal value also increases. Notice that
the loss function value decrease (by a large factor) when the minimum total
information to keep increases from 93% to 95%. This is due to the fact that
an additional reaction channel is included in the reduced model while pre-
serving the same number of species. This suggests that this reaction channel
is crucial to correctly represent the dynamics of those species.
pFIM % (18)
¯J
¯K
¯d
Loss (39)
93
9
9
12
194.87
95
10
10
12
0.0168709
97
11
11
15
6.95971
99
13
13
18
6.97222
Table 1: Diﬀerent reduced models as per total diagonal pFIM information. Observe the
non-monotone behaviour of the loss function (39) as the number of species increase. The
trajectories associated with the ﬁrst two models (93% and 95%) are shown in Figure 9
and Figure 8 respectively.
Validation (Step 5)
In this step we assess the quality of the trajectories generated by diﬀer-
ent reduced models, and we compute two validation distances. In order to
perform a detailed comparison, in table 2 we show diﬀerent models as per
the total number of parameters kept (ordered by total information as per the
pFIM diagonal). Column “path-dist” shows the following pathwise distance
max
i∈O
sup
t∈[0,T]
|zi(t) −¯zi(t)|
zi(t)
,
(60)
where O is a ﬁxed set of species, z denotes the full model mean-ﬁeld trajec-
tories, and ¯z the mean-ﬁeld trajectories generated with the reduced model.
By means of ﬁxing the set of species, we can compare reduced models with
diﬀerent number of species. If zi(t) = 0 then the quotient is deﬁned to be
equal to ¯zi(t). Finally, column “SS-dist” shows the following time average
distance
max
i∈O
|z0:T,i −¯z0:T,i|
z0:T,i
,
(61)
where O is a ﬁxed set of species, z0:T is the time average z0:t := 1
T
R T
0 z(s)ds
of the full model mean-ﬁeld, and ¯z0:T its corresponding counterpart in the
reduced model.


## Page 41


41
It is important to note that, as the total information increases (93% →
95% →97% →99%), reduced models may have additional species. In order
to compare them, in Table 2 we restrict the comparison to the set of species
of the model that has 10 parameters (line 4 in the table).
¯J
¯K
¯d
path-dist (60)
SS-dist (61)
7
7
10
0.530
0.128
8
8
10
0.041
0.002
9
9
12
0.034
0.005
10
10
12
0.002
0.001
Table 2: Diﬀerent reduced models as per total number of parameters in the reduced
models. Distances shown in the last two columns are given in (60) and (61) respectively,
where O is given by the set of species associated with the model that has 10 parameters
(line 4 in the table). In such a way, we compare for the same species trajectories.
Iteration (Step 6)
We ﬁrst point out that, a ﬁrst model selection is carried out by by running
the reduction procedure with diﬀerent information thresholds (see Table 1
and 2). In this section we show a further strategy to improve a given reduced
model. Suppose that it is required by the user to keep in the reduced model at
least 99% of the total information. This reduced model, obtained by applying
Steps 1-5, is the one shown in last line of Table 1). By inspecting the distance
between the full model mean-ﬁeld trajectories versus the reduced ones, we
can observe that the reduced model dynamics of species Jnk-P (species index
33) is departing from the full dynamics (see Figure 10). To improve this
model, as described in Section 5.7, we further include in the set of selected
reaction channels JP all reaction channels in which species Jnk-P aﬀects the
stoichiometry. In Table 3 we show the results. Two reaction channels are
then added, with indexes j=45 and j=79, with stoichiometry
S33 + S34
c45
−→S32 + S34 ,
S33 + S33
c79
−→S50 + S51 .
Since parameters c45 and c79 are not pFIM-sensitive (and that is why these
two reactions were not included in the original reduced model, plotted in
Figure 10), they will be included in the reduced model as constants and not
parameters. The number of species remains unchanged. This new augmented
model is shown in Table 3. Notice the large drop in the information loss with
respect to the information loss given in the last row of Table 1.


## Page 42


42
ROS
Hsp90
Hsp70
Hsp70Client
Hsp70-Hsp70Client
Hsp90Client
Hsp90-Hsp90Client
Hsf1
Hsf1-Hsp90
Hsp70-Ppx
Ppx
Jnk
Jnk-P
Mkp1-P
p38
p38-P
Akt
Akt-Hsp90
10 1
10 2
10 3
Steady state of Species
Figure 10: Mean-ﬁeld trajectories and approximate steady state of species indexed by
SP, at 99% of total information (see last line of Table 1). Dynamics of species Jnk-P is
diﬀerent in the reduced model. Compare this reduced model vs the one at 95% of the
total information in Figure 8. Trajectories of species previously included in that model
are now correctly represented, but new species emerge.
pFIM %
¯J
¯K
¯d
Loss (39)
path-dist (60)
SS-dist (61)
99
15
13
18
0.0203601
0.002
0.001
Table 3: Improved reduced model at 99% of total information. Notice the large drop in
the information loss with respect to the information loss given in the last row of Table 1
Discussion
This example presents a prototypical case of a model in a regime where
signiﬁcant reductions are possible. By considering the parameters that accu-
mulate at least 95% of the total information as per (44), we observe a sub-
stantial reduction in terms of species and reaction channels while controlling
the information loss and obtaining virtually identical mean-ﬁeld trajectories.
Only 12 out of 52 species are kept in the reduced model, and 10 out of 80
reaction channels. The number of parameters decreased from 87 to 10 (see
Table 1).
We also presented the case that, for a given information threshold, there
exists species for which the reduced model mean-ﬁeld trajectories does not
replicate the corresponding ones of the full model (see Figure 10). We also
showed how to improve such a reduced model iteratively (see Table 3). In
that respect, we demonstrated that iteration and validation components of
our method are relevant for a meaningful reduction.


## Page 43


43
6.3. Mammalian circadian clock model
Model description
This reaction network consists of 16 species, 52 reactions and 52 param-
eters, the initial population and time interval, [0, T], T=72, are taken from
[57] and [88]. The variables in this model represent concentrations of species.
The purpose of the original authors is to present a deterministic model for
the mammalian circadian clock. This model presents oscillatory behavior in
most of its species.
Selecting parameters and reaction channels (Step 1)
We start this example by noticing that 35 out of 52 parameters acccu-
mulate at least 95% (precisely, 95.051%) of the total information as per the
pFIM diagonal (44), i.e., κ=0.95, as shown in Figure 11.
Total pctg not including "Other" = 95.051
Other
50
 9
19
41
44
24
30
20
45
23
26
32
42
16
43
22
13
 6
40
14
36
28
12
29
38
15
34
 8
17
 1
25
 4
18
21
10
Parameter Index
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
0.09
Information Percentage
Figure 11: Total information as per the pFIM diagonal (44). Notice that 35 out of 52
parameters accumulate at least 95% (precisely, 95.051%) of the total information as per
the pFIM diagonal.
Selecting variables (Step 2)
In Figure 12 (right pane) we show the sensitive reaction channels (48) and
corresponding species (50), at κ=0.95. Dotted lines shows, for the selected
species (i.e., included in the reduced model), the stoichiometry relations with
reaction channels considered not sensitive and therefore not included in the
reduced model. Some sparsity can be observed in the stoichiometry of this
reaction network.


## Page 44


44
R:1
R:2
R:3
R:4
R:5
R:6
R:7
R:8
R:9
R:10
R:11
R:12
R:13
R:14
R:15
R:16
R:17
R:18
R:19
R:20
R:21
R:22
R:23
R:24
R:25
R:26
R:27
R:28
R:29
R:30
R:31
R:32
R:33
R:34
R:35
R:36
R:37
R:38
R:39
R:40
R:41
R:42
R:43
R:44
R:45
R:46
R:47
R:48R:49 R:50 R:51 R:52 S:1
S:2 S:3 S:4
S:5
S:6
S:7
S:8
S:9
S:10
S:11
S:12
S:13
S:14
S:15
S:16
Low
High
total pFIM per reaction channel
R:1
R:2
R:4
R:5
R:6
R:7
R:9
R:10
R:11
R:12
R:13
R:14
R:15
R:16
R:17
R:18
R:19
R:20
R:24
R:25
R:27
R:29
R:30
R:31
R:33
R:38
R:40
R:41
R:42
R:44
R:49
S:1
S:2
S:3 S:4
S:5
S:6
S:7
S:8
S:9
S:10
S:11
S:12
S:13
S:14
S:15
S:16
Low
High
total pFIM per reaction channel
Figure 12:
Stoichiometry and information.
Black dots:
reaction channels, red dots:
species. A link shows stoichiometry of each reaction channel. The color of the link shows
the total pFIM of the corresponding reaction channel (see 59). Left: Full model. Right:
Reduced model, including at least 95% of the total information as per the pFIM diagonal
(44). In the plot, species indexes are shown, while species names are given in Figure 13.
Reduced model (Step 3 and Step 4)
In Figure 13 we compare the mean-ﬁeld trajectories of the species included
in the reduced model at 95% of information, and the respective mean-ﬁeld
trajectories of the same species in the full model. We also show a comparison
between the time average of the full model versus the corresponding one of
the reduced model at κ=0.95. Names of the species included in the reduced
model are given in both plots of Figure 13.
Validation (Step 5)
In Table 4 we show diﬀerent reduced models, according to total pFIM
information. Every reduced model includes all 16 species, so every reduced
model is already comparable in terms of the validation distances.
Notice
there are at least two candidate models. At 97% of total information we
have virtually the same trajectories (not shown in the ﬁgures) but only 7
out of 52 reactions channels and 13 out of 52 parameters are eliminated. At
95%, 21 out of 52 reaction channels are reduced and 17 parameters out of 52
are reduced but the mean-ﬁeld trajectories of the reduced model seems out
of phase with respect to the ones of the full model.
Discussion
This model presents non-trivial oscillatory behaviour and there is no re-
duction on the number of species. Despite of this, the number of reaction


## Page 45


45
0
10
20
30
40
50
60
70
Time
0
1
2
3
4
5
6
7
8
9
Species abundance
Mb
Bc
Bcp
Bn
Cc
Mc
Ccp
Mp
Pc
Pcp
PCc
PCcp
PCn
Bnp
PCnp
In
10 -1
10 0
Time average of species abundance
Figure 13: Left: Mean-ﬁeld trajectories of species indexed by SP (50). Solid lines corre-
spond to the reduced model and thick dashed lines to the full model. Right: Approximation
of the mean-ﬁeld steady state of species in the reduced model (circle), vs. the full model
(star), for t ∈[0, T ] at 95% of total information.
pFIM % (18)
¯J
¯K
¯d
Loss (39)
path-dist (60)
SS-dist (61)
93
29
33
16
0.0109498
4.506
0.267
95
31
35
16
0.000820265
0.597
0.083
97
45
39
16
0.000381857
0.082
0.040
99
49
45
16
0.000172741
0.102
0.019
Table 4: Diﬀerent reduced models as per total pFIM information. Since the number of
species in every model is the same, the validation distances of the last two columns are
applied to the same set of species. Notice the monotone decrease of the loss function.
channels and parameters are still reduced from 52 to 31 and from 52 to 35
respectively, by considering 95% of the total information as per the pFIM
diagonal (see Table 4). The mean-ﬁeld trajectories of this reduced model
reasonably replicates the original ones (see Figure 13). Notice, however, a
phase shift in some of its trajectories. Increasing the total pFIM to 97%,
we obtain superior replication of the trajectories, but more parameters and
reaction channels are kept in the reduced model.
6.4. Epidermal Growth Factor Receptor (EGFR) model
Model description
This example is a well-studied model that describes signaling phenomena
of mammalian cells, regulating its growth, survival and proliferation playing
a crucial role in many biological processes. This reaction network consists of


## Page 46


46
24 species, 47 reaction channels and 50 parameters. The variables account
for species concentrations. It has mass-action kinetics type and Michaelis-
Menten approximation type of propensities. This model of signalling phe-
nomena has a transient regime that corresponds to the time interval [0, 50]
and also a stationary regime for T>50. Here we consider the transient regime
and the reaction constants, the initial population are taken from [56].
Selecting parameters and reaction channels (Step 1)
We start the analysis by noticing that that 25 out of 50 parameters accu-
mulate at least 97% (precisely, 97.244%) of the total information as per the
pFIM (44), as shown In Figure 14.
Other
10
28
35
 2
33
44
50
 4
43
11
13
46
45
42
29
 3
 9
 1
41
25
49
27
 8
 7
 5
Parameter Index
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
Information Percentage
Total pctg not including "Other" = 97.244
Figure 14: Total information as per the pFIM. Notice that 25 out of 50 parameters acc-
cumulate 97.244% of the total information as per the pFIM diagonal (see (44)).
Selecting variables (Step 2)
In Figure 15 (right pane) we show the sensitive reaction channels (48)
and the corresponding species (50), that represent at least 97% of total pFIM
diagonal information. Dotted lines shows, for the selected species (i.e., as-
sociated with sensitive reaction channels), the stoichiometry relations with
reaction channels not considered sensitive, and therefore, not included in the
reduced model. We can observe that many reaction channels not consid-
ered sensitive aﬀect many selected species. In principle, for a ﬁxed κ this
may aﬀect the quality of the reduced model, since many reactions that may
increase or decrease the populations/concentrations of the selected species
are not included in the reduced model. As seen in Figure 16, those missing
reaction channels seems to be non essential.


## Page 47


47
R:1
R:2
R:3
R:4
R:5
R:6
R:7
R:8
R:9
R:10
R:11
R:12
R:13
R:14
R:15
R:16
R:17
R:18
R:19
R:20
R:21
R:22
R:23
R:24
R:25
R:26
R:27
R:28
R:29
R:30
R:31
R:32
R:33
R:34
R:35
R:36
R:37
R:38
R:39
R:40
R:41
R:42
R:43
R:44
R:45
R:46
R:47
S:1
S:2
S:3 S:4 S:5 S:6 S:7 S:8 S:9 S:10S:11
S:12
S:13
S:14
S:15
S:16
S:17
S:18
S:19
S:20
S:21
S:22
S:23
S:24
Low
High
total pFIM per reaction channel
R:1
R:2
R:3
R:4
R:5
R:7
R:8
R:9
R:10
R:12
R:23
R:25
R:26
R:27
R:30
R:32
R:38
R:39
R:40
R:41
R:42
R:43
R:46
R:47
S:2
S:3 S:4 S:5 S:6 S:7 S:8 S:9 S:10S:11
S:13
S:15
S:16
S:17
S:18
S:19
S:20
S:21
S:23
S:24
Low
High
total pFIM per reaction channel
Figure 15:
Stoichiometry and information.
Black dots:
reaction channels, red dots:
species. A link shows stoichiometry of each reaction channel. The color of the link shows
the total pFIM of the corresponding reaction channel (see 59). Left: Full model. Right:
Reduced model, which includes at least 97% of the total information as per the pFIM
diagonal (44). In the plot, species indexes are shown, while species names are given in
Figure 16.
Reduced model (Step 3 and Step 4)
In Figure 16 we compare the mean-ﬁeld trajectories of the species included
in the reduced model at κ=0.97, and the respective mean-ﬁeld trajectories
of the same species in the full model. We also show a comparison for the
time average on [0, T], of the full model versus the reduced model at κ=0.97.
Most of the trajectories and time averages are correctly represented in the
reduced model. The validation distances (60) and (61), which are properly
normalized, are shown in Table 5.
Validation (Step 5)
In Table 5 we show diﬀerent reduced models, according to total informa-
tion as per the pFIM diagonal. Column “Loss” shows the value of the loss
function (39) at which θ∗
0:T is achieved, by numerically solving problem (54).
Observe the monotone reduction of the information loss, it has two large
decays when going from 93% to 95% and from 97% to 99%. Distances shown
in the last two columns are given by (60) and (61) respectively, where the
set O is given by the set of species associated with each respective reduced
model. That is, the set O associated with the second line (95%) correspond
to the 20 species selected in that reduced model. Notice that the number
of selected species remain unchanged when increasing the total information
from 95% to 97%, but three additional reaction channels are added to the


## Page 48


48
0
10
20
30
40
50
Time
0
100
200
300
400
500
600
Species
EGFR
EGF
EGF-EGFR
EGF-EGFR-2
EGF-EGFR-2-P
PLCg
EGF-EGFR-2-PLCg
EGF-EGFR-2-PLCg-P
PLCg-P
Grb2
SOS
Grb2-SOS
Shc
EGF-EGFR-2-Shc
EGF-EGFR-Shc-P
Shc-P
EGF-EGFR-2-Shc-Grb2
Shc-Grb2
Shc-Grb2-SOS
PLCgP-I
10 0
10 1
10 2
Steady state of Species
Figure 16: Left: Mean-ﬁeld trajectories of species indexed by SP (50). Solid lines cor-
respond to the reduced model and thick dashed lines to the full model.
Right: Time
average on [0, T ] for the reduced model (circle), vs. the full model (star) at 97% of total
information per pFIM diagonal.
reduced model. This results in lower information loss and also lower path-
wise and steady state distance of the species trajectories. Model at 97% of
total information as per the pFIM seems a good compromise between infor-
mation loss and pathwise distances in comparison the reduction of species
and reaction channels.
pFIM % (18)
¯J
¯K
¯d
Loss (39)
path-dist (60)
SS-dist (61)
93
19
20
19
1.45047
0.681
0.353
95
21
22
20
0.464843
7.776
3.824
97
24
25
20
0.16691
0.638
0.214
99
31
32
21
0.0469859
0.437
0.093
Table 5: Diﬀerent reduced models as per total pFIM information for the EGFR model.
Observe the monotone decrease of the information loss even though model has diﬀerent
number of species. Distances shown in the last two columns are given by (60) and (61)
respectively, where the set O is given by the set of species associated with each respective
reduced model.
Discussion
We observe a signiﬁcant reduction in terms of species, reaction channels
and parameters, while controlling the entropy loss and obtaining virtually
identical mean-ﬁeld trajectories for almost all the species. The number of
species in the reduced model (at 97% of total information) is 20 (out of 24)


## Page 49


49
and the number of reaction channels is 24 (out of 47) while the number of
parameters is 25 (out of 50). Further details can be found on Table 5.
7. Numerical experiments: Stochastic models
In this section we present two stochastic pure jump models: a circadian
clock model which is based on [57], and a growth factor receptor, based
on [56].
By scaling the original models, we obtain stochastic pure jump
representations that manifest non-Gaussian distributions of the time average
of species counts for many of the species.
We show in this section that
our method is robust in the sense that it can be used to either reduce a
model which is close to a Langevin or mean-ﬁeld regime and also to reduce
a pure jump model with low count in many of its species. Therefore, once
the reduced network (¯νj, ¯aj) ¯J
j=1 is constructed, a pure jump stochastic, a
Langevin diﬀusion or a deterministic representation can be readily obtained
up to the corresponding scalings.
7.1. A stochastic circadian clock model
In this section we focus on a stochastic circadian model which is derived
from the deterministic model presented in the previous section, to demon-
strate the robustness of the method in a challenging non-Gaussian regime.
Using Kurtz’s classical scaling ([90]) we obtain a stochastic pure jump model
from the original deterministic one to perform a statistical validation. We
ﬁrst observe that the original model can be written in integral form (see (7)
for the diﬀerential form) as
z(t) = z(0) +
J
X
j=1
νj
Z t
0
aj(z(s); c)ds ,
and z(0) = z0 where z(t) ∈Rd represents the concentration of the species.
Now given a parameter that measures the size of the system, N, we obtain
the following counting process that approximates z(t)
X(t) = X(0) +
J
X
j=1
νjYj

N
Z t
0
¯aj(N−1X(s); c)ds

,
and X(t) = Nz0 where Pj are independent unit-rate Poisson processes and
¯aj are the kinetic propensity functions, independent of N. When N →∞


## Page 50


50
it can be shown that the mean of N−1X converge pathwise to z (for further
details and more advanced scaling limits we refer to [91]). In this example,
for N=105 a stochastic trajectory is indistinguishable from z. In ﬁgure 17
(left) we show one stochastic trajectory for N=2.
We compute the pFIM for this stochastic network (see (19)) by sampling
M=103 trajectories of X(t), for t ∈[0, T], T=72. Using the same trajectories,
we compute the mean time average of each species Si
A(Xi) := 1
M
M
X
m=1
1
T
T (m)
X
k=1
xk,m∆tk,m ,
i=1, 2, ..., d ,
(62)
where T (m) is the number of jumps of the m−th trajectory. Using this sample,
we construct a bootstrap estimation of the mean of the time average and
the corresponding 95% conﬁdence interval (together for comparison with the
time average of z), as shown in Figure 17 (left). We observe that, for many
species, the time average of the deterministic model is not included in a 95%
conﬁdence interval of the mean time average of the stochastic model. This is
reasonable because in the small particle count case, species may get extinct
(hit the zero boundary), among many other possible stochastic behaviour not
captured by the deterministic model. It is clear that this stochastic model,
derived from the original deterministic one, is not in a Langevin or mean-ﬁeld
regime.
0
10
20
30
40
50
60
70
Time
0
2
4
6
8
10
12
14
16
18
Species count
Mean A(X)
CI left end
CI right end
A(z)
Mb
7.5033
7.6258
7.7452
8.3065
Bc
1.8569
1.8943
1.9329
1.8996
Bcp
1.2518
1.2908
1.3358
0.8379
Bn
0.9846
1.0046
1.0252
0.8525
Cc
7.2024
7.6510
8.1144
4.0765
Mc
1.4039
1.4477
1.4910
1.1686
Ccp
0.9937
1.0335
1.0701
0.6391
Mp
1.9802
2.0290
2.0767
1.7567
Pc
4.5863
5.0638
5.5887
0.6214
Pcp
0.2495
0.2582
0.2672
0.0978
PCc
2.5751
2.6586
2.7325
2.2676
PCcp
0.4379
0.4500
0.4618
0.2002
PCn
2.1762
2.2683
2.3543
1.6901
Bnp
0.4313
0.4442
0.4573
0.2506
PCnp
0.3609
0.3720
0.3845
0.1829
In
0.9378
1.0125
1.0843
0.2606
Figure 17: Table: Mean time average of each species with the corresponding 95% empirical
conﬁdence interval and the time average of z (the time average denoted by A), for the
stochastic circadian model. We can observe that, for some species, there are signiﬁcant
diﬀerences (e.g. species Pc).


## Page 51


51
We now reduce this stochastic model by using our method. We show in
Table 6 the results. For an equivalent number of parameters, we have con-
sistent pFIM and validation distances in comparison with the deterministic
model. This is a remarkable robustness of our reduction method, and stress
the point that it can be applied to deterministic, Langevin or pure jump
reaction networks. For example, we compare the reduced model obtained by
applying our method to the deterministic model versus the reduced model
of the stochastic circadian model. Compare for instance the model with 35
parameters and 31 reaction channels that accumulates 95.05% of the de-
terministic pFIM (Table 4) versus the model with 34 parameters and 30
reaction channels that accumulates 95.47% of the stochastic pFIM (Table
6). In fact, we obtained a slightly more parsimonious model (less parameters
and reaction channels) with smaller validation distances. We notice that the
validation distances are mean-ﬁeld based (see (60) and (61)).
pFIM % (18)
¯J
¯K
¯d
Loss (39)
path-dist (60)
SS-dist (61)
91.96
28
30
16
0.119118
2.204
0.268
92.94
29
31
16
0.0570935
3.125
0.268
93.91
30
32
16
0.00611969
0.681
0.051
94.69
30
33
16
0.00542096
0.698
0.055
95.46
30
34
16
0.00533519
0.421
0.061
96.08
30
35
16
0.00535939
0.663
0.050
96.64
42
36
16
0.0053336
0.179
0.038
97.20
43
37
16
0.00490005
0.215
0.043
Table 6: Diﬀerent reduced stochastic models as per total pFIM information, for the
stochastic circadian model.
Since the number of species in every model is the same,
the validation distances of the last two columns are applied to the same set of species.
In Figure 18 we show a box-plot comparison between the full stochastic
model and the reduced model at 95.46% of total information. On each x-axis
we show a box for the species in the full model and next a box for the same
species in the reduced model. We can observe a tight agreement on the vast
majority of the resolved species. In Figure 19 we show histograms for 3 rep-
resentative species with non-Gaussian behaviour showing tight agreements.
7.2. A stochastic growth factor receptor model
In this section we focus on a stochastic growth factor receptor model
which is derived from the deterministic model presented in Section 6.4, by
using Kurtz’s classical scaling ([90]) (for more details see Section 7.1).


## Page 52


52
Pcp
Pcp (r)
PCnp
PCnp (r)
Bnp
Bnp (r)
PCcp
PCcp (r)
In
In (r)
Ccp
Ccp (r)
0
1
2
3
4
5
6
7
8
9
10
Bn
Bn (r)
Bcp
Bcp (r)
Mc
Mc (r)
Bc
Bc (r)
Mp
Mp (r)
Pc
Pc (r)
0
5
10
15
20
25
30
35
40
PCn
PCn (r)
PCc
PCc (r)
Cc
Cc (r)
Mb
Mb (r)
0
10
20
30
40
50
Figure 18: Box plot comparison of time average of species, for the stochastic circadian
model. On each box, the central mark indicates the median, and the bottom and top
edges of the box indicate the 25th and 75th percentiles, respectively of the time average.
The whiskers extend to the most extreme data points not considering outliers. Species
name with suﬃx “(r)” correspond to the reduced model at 95.46%.
Figure 19: Histograms for 3 representative species with non-Gaussian behaviour showing
tight agreements, for the stochastic circadian model.
We compute the pFIM for this stochastic network (see (19)) by sampling
M=103 trajectories of X(t), for t ∈[0, T], T=50. Using that sample, we
construct a bootstrap estimation of the mean of the time average and the
corresponding 95% conﬁdence interval (together for comparison with the time
average of z), as shown in Figure 20. We observe that, for many species, the
time average of the deterministic model is a good approximation of the mean
time average. In this respect, we can consider this stochastic model close to
a mean-ﬁeld regime.
We now reduce this stochastic model by using our method. We show in
Table 7 the results. For an equivalent number of parameters, we have con-
sistent pFIM and validation distances in comparison with the deterministic
model. We stress again this robustness feature of our reduction method. For
example, we compare the reduced model obtained by applying our method
to the deterministic model versus the reduced model of the stochastic cir-


## Page 53


53
Mean A(X)
CI left end
CI right end
A(z)
EGFR
2.0997
2.1353
2.1715
2.2993
EGF
60.0997
60.1353
60.1715
60.2993
EGF-EGFR
3.7125
3.7529
3.7945
3.9655
EGF-EGFR-2
1.1980
1.2183
1.2375
1.0995
EGF-EGFR-2-P
0.1318
0.1344
0.1370
0.1200
PLCg
9.6485
9.6979
9.7485
9.8726
EGF-EGFR-2-PLCg
0.0602
0.0627
0.0652
0.0563
EGF-EGFR-2-PLCg-P
0.1770
0.1852
0.1944
0.1718
PLCg-P
0.0786
0.0826
0.0864
0.0727
Grb2
8.4036
8.4293
8.4555
8.5213
EGF-EGFR-2-Grb2
0.0293
0.0368
0.0443
0.0290
SOS
2.7198
2.7376
2.7553
2.7840
EGF-EGFR-2-Grb2-SOS
0.0057
0.0082
0.0111
0.0060
Grb2-SOS
0.1124
0.1245
0.1381
0.1070
Shc
12.3810
12.4518
12.5232
12.7312
EGF-EGFR-2-Shc
0.0236
0.0244
0.0251
0.0229
EGF-EGFR-Shc-P
0.3506
0.3619
0.3734
0.3390
Shc-P
1.7070
1.7607
1.8174
1.5703
EGF-EGFR-2-Shc-Grb2
0.0162
0.0185
0.0207
0.0191
Shc-Grb2
0.2400
0.2530
0.2667
0.2147
EGF-EGFR-2-Shc-Grb2-SOS
0.0036
0.0053
0.0073
0.0041
Shc-Grb2-SOS
0.1147
0.1244
0.1342
0.0989
PLCgP-I
0.9308
0.9715
1.0134
0.8265
Figure 20: Table: Mean time average of each species with the corresponding 95% empirical
conﬁdence interval and the time average of z (the time average denoted by A), stochastic
growth factor receptor model. We can observe that, for many species, the time average
of the deterministic model is a good approximation of the mean time average. We notice
that only 23 species are shown in the table because in the original model a dummy species
is used to model the creation of particles.
cadian model. Compare for instance the model with 25 parameters and 24
reaction channels that accumulates 97.244% of the deterministic pFIM (Ta-
ble 5) versus the model with 24 parameters and 22 reaction channels that
accumulates 99.5% of the stochastic pFIM (Table 7). In fact, we obtained
a slightly more parsimonious model (less parameters and reaction channels)
with similar validation distances. We notice that the validation distances are
mean-ﬁeld based (see (60) and (61)).
pFIM % (18)
¯J
¯K
¯d
Loss (39)
path-dist (60)
SS-dist (61)
98.97
20
21
18
0.0033021
2.443
0.477
99.50
22
24
19
0.000889939
0.627
0.191
99.73
24
26
20
0.000326358
0.359
0.106
Table 7: Diﬀerent reduced stochastic models as per total pFIM information, stochastic
growth factor receptor model. Since the number of species in every model is the same, the
validation distances of the last two columns are applied to the same set of species.
In Figure 21 we show a comparison between the full stochastic model
and the reduced model at 99.5% of total information by using a box plot.
On each x-axis we show a box for the species in the full model and next


## Page 54


54
a box for the same species in the reduced model. We can observe a tight
agreement on the vast majority of the species. In Figure 22 we show his-
tograms for 3 representative species with non-Gaussian behaviour showing
tight agreements.
EGF-EGFR-2-Grb2-SOS
EGF-EGFR-2-Grb2-SOS (r)
PLCg
PLCg (r)
EGF-EGFR-2-PLCg-P
EGF-EGFR-2-PLCg-P (r)
EGF-EGFR-2
EGF-EGFR-2 (r)
EGF-EGFR-2-PLCg
EGF-EGFR-2-PLCg (r)
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
Grb2-SOS
Grb2-SOS (r)
Shc-P
Shc-P (r)
EGF-EGFR
EGF-EGFR (r)
Shc
Shc (r)
NULL
NULL (r)
0
1
2
3
4
5
6
EGF
EGF (r)
EGF-EGFR-2-P
EGF-EGFR-2-P (r)
SOS
SOS (r)
EGFR
EGFR (r)
0
10
20
30
40
50
60
Figure 21: Box plot comparison of time average of resolved species, stochastic growth
factor receptor model.
On each box, the central mark indicates the median, and the
bottom and top edges of the box indicate the 25th and 75th percentiles, respectively of
the time average. The whiskers extend to the most extreme data points not considering
outliers. Resolved species name with suﬃx “(r)” correspond to the reduced model.
Figure 22: Histograms for 3 representative resolved species with non-Gaussian behaviour
showing tight agreements, stochastic growth factor receptor model.
8. Connections with related reduction methods
In this section we brieﬂy discuss related state of the art on model reduc-
tion for biochemical reaction networks.
Sensitivity-based reduction methods.
The goal of sensitivity analysis
is to determine how certain quantities of interest of the system vary under
perturbations to model parameters and/or state variables. To reduce a given
system by using this technique, the most common approach is to eliminate


## Page 55


55
the least sensitive parameters and/or state variables. One of the advantages
of sensitivity-based methods is the meaning preservation of the state variables
and reaction channels.
Local sensitivity-based reduction methods [13, 14, 15, 16, 17, 13] usually
require to solve the system (29), and therefore are not suitable for high-
dimensional networks (see Remark 3.4) not only due to the high dimension
(number of parameters times number of state variables) but also the stiﬀness
of the system to solve. Our method only requires to compute the pathwise
FIM which is of the order of the number of parameters. A typical drawback
of sensitivity-based model reduction approaches is that the elimination of
low -sensitivity parameters may lead to unsatisfactory results. An example
of this issue is presented in [92], for which the sensitivities of some of the
reaction channels are close to zero, however the removal of these reactions
would result in the shutdown of the whole reaction network. We applied
our method to this model obtaining a substantial reduction without compro-
mising the dynamics of any of the species present in the original model. If
a matrix of sensitivity indexes is feasible to compute, principle component
analysis (PCA) is a commonly used method to rank reaction channels and
then determine which ones can be eliminated [93, 94, 95]. As we previusly
mentioned, our method is amenable to combine with PCA by applying this
analysis to extract further information from the pFIM, especially taking into
account its block diagonal structure. We do not pursue this direction any
further here.
Finally, the use of global sensitivity analysis for model reduction of biochem-
ical reaction networks is still an open problem, due to the extremely high
computational work requirements of these methods (see [18, 19]). We antic-
ipate that the main blocks of our method (i.e. model selection by means of
the pFIM and its stoichiometry matrix and the use of a loss function in the
macroscopic space for data training) can be of great help in applying global
sensitivity analysis for model reduction of high-dimensional systems.
Optimization approaches.
A technique that is usually related with
sensitivity-based reduction methods is the optimization approach. The aim
is to reduce a system by testing candidate reduced models while minimizing
an error metric to choose the best one. The optimization techniques vary in
construction process of the set of candidate reduced models.
In [18, 20], the authors present a method that combines a model reduction
technique together with a parameter estimation algorithm. In this work, in
order to reduce the number of parameters, the least inﬂuential reaction rates


## Page 56


56
are just set to zero. In this optimisation problem, the authors use a genetic
algorithm to simultaneously identify parameter values and further eliminate
unimportant reactions. A similar approach is used in [21], for the case of
polynomial or rational propensity functions, based on a integer quadratic
programming optimization. This approach also contains rate coeﬃcients es-
timation in the reduced model to minimize the deﬁned model error. This
approach is demonstrated by the authors by reducing a model of the Ara-
bidopsis thaliana circadian clock involving 7 state variables and 27 reactions,
from [22]. Even though we do not consider this model as high-dimensional,
we applied our reduction method and obtained the same reduced model as
in [22].
In [23, 24], the authors proposed a method to calculate the error associated
with a model reduction algorithm.
This approach is based on the error
between observables of the original and the reduce system.
A worst-case
error type of bound between the original and the reduced system in form
of sum of squares are used for developing an optimization-based method for
model reduction.
Timescale-based reduction methods.
Alternatively, model reduction can
be carried out by by exploiting timescale diﬀerences that are often present
in biochemical systems [2]. Timescale analysis methods are one of the most
widely used approaches for model reduction in the literature. These methods
aim to partition the reaction network into diﬀerent timescales by exploiting
the several orders of magnitude diﬀerence that usually exist between reaction
channel rates. This timescale diﬀerence allows to reduce a given model as
certain species or reaction channels can be assumed to be constant with
respect to the timescale of interest.
A group of timescale exploitation methods that is close to our method is
based on identifying species or reactions which can be classiﬁed to be on a
fast dynamics regime in comparison with the other ones, and therefore par-
titioning the reaction network into fast and slow components. Once such a
partition has been found, the reduction of the system is achieved by means
of the application of singular perturbation techniques. These methods are
based on Tikhonov’s singular perturbation theory for the reduction of ﬁrst
order ODE’s going back at least to [96]. The aforementioned partition could
be done in terms of species or reaction channels. Among the species-based
partitioning methods the quasi-steady-state approximation (QSSA) is well-
known for its application to the reduction of the Michaelis–Menten equation
[3]. This method is limited to models in which species exhibit a clear sepa-


## Page 57


57
ration in timescales. For low-dimensional systems, it is feasible to search for
such a partition, by the use of additional intuitive information about the sys-
tem. Unfortunately, for high-dimensional systems these methods are usually
prohibitive due to the combinatorial nature of diﬀerent model representa-
tions [4, 5, 6, 7, 8]. Other works aim to provide algorithmic procedures for
determining which species can be considered fast (see for instance [97, 98]).
The reaction-based partitioning methods assume that certain reactions occur
fast enough such that it can be assumed that they reach an equilibrium im-
mediately, so these methods are referred as rapid equilibrium approximation.
This is de idea behind the Michaelis-Menten original approximation [99]. Re-
lated works include [100, 24, 101]. The main diﬃculty associated with the
previous timescale partitioning method is to ﬁnd a formulation such that
the timescales diﬀerences between species or reaction channels are clearly
exposed.
A second group of timescale methods aims to obtain a transformation of the
state variables to obtain a reduced model where timescale separations are
clear. Such approaches often lead to more accurate and substantial model
reductions than the previous methods but transformations often diﬃcult the
biochemical interpretation of the reduced model. An example of these meth-
ods is the eigenbasis transformation of the state variables, as in the intrin-
sic low-dimensional manifold method (ILDM), originally developed in [9].
A brief review for the biochemical reaction network case is given in [10].
Other applications of this method is given in [11, 12]. Another transforma-
tion method that is widely used is the computational singular perturbation
(CSP), originally published in [102] and further developed in [103, 104]. A
rigorous analysis of this method and its comparison with the ILDM is given in
[105]. This aims to transform the set of reaction channels into a diﬀerent ba-
sis to clearly enhance timescale diﬀerences between the transformed reaction
channels. The fast transformed reaction channels are assumed to equilibrate
instantaneously, and then their dynamical contribution is neglected in the
reduced model. Some works in this direction include [106, 107].
Lumping-based reduction methods.
Lumping is another wide class of
model reduction methods, usually applied to linear systems. How a proper
lumping can be formulated for a nonlinear system is still an open problem.
Methods presented in the literature for non-linear systems usually are based
on trial and error approaches which may be computationally prohibitive for
high-dimensional systems. This class of methods originated in the dynamical
systems literature [108, 109]. The idea is to remove sets of state variables


## Page 58


58
and replace them with new lumped variables that represent mappings from
the original ones. Applications of lumping to biochemical reaction networks
are [25, 26, 27, 28]
9. Conclusions
In this work we presented an eﬃcient and principled model reduction
method for high-dimensional deterministic and stochastic reaction networks.
The goal of model reduction is to construct a simpler model in terms of a
reduced set of state variables, parameters and reaction channels. In general,
there is no universal model reduction method which can be considered supe-
rior for every reaction network, especially in the high-dimensional case. The
appropriateness of each method is entangled to the nature of the model that
is intended to reduce. Our method is particularly suited for high-dimensional
biochemical systems, applicable to any smooth propensity function and no
equilibrium assumptions are required. Despite our method is designed for
high-dimensional models, it is well suited for many low-dimensional exam-
ples found in the literature although alternative reduction methods may be
better suited for low dimensional models, such as transforming methods or
lumping approaches (see Section 8 for brief discussions of these methods).
Our method is also well suited for pure jump models, in Langevin regimes
or deterministic ones.
Our method is based on pathwise information metrics to screen-out insen-
sitive parameters via the analysis of the pathwise Fisher Information Matrix.
By means of a simple loss function for time-series data based on path-space
information theory, candidate reduced models can be ﬁtted to full model time
series data and therefore the resulting reduced model dynamics conform an
accurate approximation to the full model dynamics on a given time interval.
The main features of this approach are summarized as follows: i) scalable
method targeted to high-dimensional deterministic and stochastic biochem-
ical systems; ii) applicable to stiﬀand non-linear models; iii) independent of
particular quantities of interest; iv) given a user-deﬁned information thresh-
old, the information loss of the reduced model is controlled; v) applicable to
any smooth propensity function form and no information is required concern-
ing which reactions are in partial equilibrium nor which species are assumed
to be in steady state; vi) no biochemical knowledge is required to reduced the
model; vii) intuitive and automatizable method; viii) it is not a data-hungry
method.


## Page 59


59
As previously mentioned, our method has a clear advantage with respect
to sensitivity-based and optimization-based methods that require to solve
classical sensitivity systems (e.g.
29), since our method only requires to
compute the pathwise FIM (18). We recall that the computational work in
the ﬁrst case is of the order of the number of state variables times parameters
while in the second is of the order of the number of parameters only (see
Remark 3.4).
One of the features of our method is that it preserves the
biochemical meaning of the variables and reaction channels. However, when
this requirement is not relevant for a particular application, transformation-
based reduction methods like lumping or timescale transforming methods
may be a superior alternative depending on the dimension of the system (see
Section 8).
Even though our method uses the stoichiometry of the network to choose
sensitive species, further information may be extracted from it as well. For
example, graph-theoretic tools may allow to dissect the stoichiometry graph
into functional modules and determine diﬀerent types of interactions between
these modules (see for instance [110, 111, 112]). Biochemical information
can also be included in this analysis, as for example retroactivity, i.e., which
sub-modules inﬂuences (or not) each other (see for instance [113, 114]). In
[115], the authors use graph-theoretic tools to characterize conditions for two
diﬀerent reaction networks to have the same dynamics, in the case of mass
action kinetics dynamics.
We ﬁnally notice that in our method, the reduced model depends on
the time interval [0, T] considered. However, our methodology can be also
applied to long-time horizons by working with the relative entropy rate
H(P ∥Q) = lim
T→∞
1
T R(P[0,T] ∥Q[0,T]) ,
where P and Q denote the corresponding stationary processes. We refer to
[54] and references therein.
Acknowledgments
The research of M.K. was partially supported by the Defense Advanced Re-
search Projects Agency (DARPA) EQUiPS program under the grant W911NF1520122.
The research of P.V. was supported by the Defense Advanced Research
Projects Agency (DARPA) EQUiPS program under the grant W911NF1520122.


## Page 60


60
Appendix: Relative entropy and pFIM decomposition
Theorem 9.1. The pathwise relative entropy for a discrete-time Markov
chain can be decomposed as
R(P0:T ∥Qθ
0:T) = R(ν ∥νθ) +
T
X
i=1
R(Pi ∥Qθ
i ) ,
(63)
where the quantity
R(Pi ∥Qθ
i ) = Eνi−1
h Z
L
p(x, x′) log p(x, x′)
qθ(x, x′)dx′i
.
(64)
can be interpreted as the instantaneous relative entropy.
Proof. The proof of this theorem can be found in [36, Ch. 2], but for the
sake of completeness we present it here. The Radon-Nikodym derivative of
P0:T w.r.t. Qθ
0:T takes the form
dP0:T
dQθ
0:T
 (xi)T
i=0

= ν(x0) QT−1
i=0 p(xi, xi+1)
νθ(x0) QT−1
i=0 qθ(xi, xi+1)
,
which is well-deﬁned since the transition probabilities are always positive.
Then,
R(P0:T ∥Qθ
0:T )
=
Z
L
· · ·
Z
L
ν(x0)
TY
j=1
p(xj−1, xj) log ν(x0) QT
i=1 p(xi−1, xi)
νθ(x0) QT
i=1 qθ(xi−1, xi)
dx0 . . . dxT
=
Z
L
· · ·
Z
L
ν(x0)
TY
j=1
p(xj−1, xj) log ν(x0)
νθ(x0)dx0 . . . dxT
+
T
X
i=1
Z
L
· · ·
Z
L
ν(x0)
TY
j=1
p(xj−1, xj) log p(xi−1, Xi)
qθ(xi−1, xi)dx0 . . . dxT
= R(ν ∥νθ) +
T
X
i=1
R(Pi ∥Qθ
i ) ,
where R(ν ∥νθ) = Eν
h
log ν(x)
νθ(x)
i
is the relative entropy of the initial distri-
butions, while the instantaneous relative entropy is
R(Pi ∥Qθ
i ) = Eνi−1
h Z
L
p(x, x′) log p(x, x′)
qθ(x, x′)dx′i
.


## Page 61


61
Theorem 9.2. Under smoothness assumption on the transition probability
function w.r.t. the parameter vector θ, the pFIM can be also decomposed as
I
 Qθ
0:T

= I
 νθ
+
T
X
i=1
IH
 Qθ
i

,
(65)
where I
 νθ
is the FIM of the initial distribution and the instantaneous FIM
is given by
IH
 Qθ
i

= Eνi−1
Z
L
pθ(x, x′)∇θ log pθ(x, x′)∇θ log pθ(x, x′)trdx′

.
(66)
Proof. This proof is similar to the proof presented in [52, 72]. We recap it
here with minor but necessary adaptations.
Let ∆p(x, x′) := pθ+ǫ(x, x′) −pθ(x, x′). Thus, we have that
R(Qθ
i ∥Qθ+ǫ
i
) = −
Z
L
Z
L
νθ
i−1(x)pθ(x, x′) log

1 + ∆p(x, x′)
pθ(x, x′)

dxdx′
= −
Z
L
Z
L

νθ
i−1(x)∆p(x, x′) −1
2νθ
i (x)∆p(x, x′)2
pθ(x, x′) + O(|∆p(x, x′)|3)

dxdx′ .
Moreover, for all x ∈L, it holds that
Z
L
∆p(x, x′)dx′ =
Z
L
pθ+ǫ(x, x′)dx′ −
Z
L
pθ(x, x′)dx′ = 0.
By using the smoothness assumption and Taylor-expanding ∆p we obtain
δp(x, x′) = ǫtr∇θpθ(x, x′) + O(|ǫ|2) .
Finally, we have that
R(Qθ
i ∥Qθ+ǫ
i
) = 1
2
Z
L
Z
L
νθ
i−1(x)(ǫtr∇θpθ(x, x′))2
pθ(x, x′)
dxdx′ + O(|ǫ|3)
= 1
2ǫtr Z
L
Z
L
νθ
i−1(x)pθ(x, x)∇θ log pθ(x, x′)∇θ log pθ(x, x′)trdxdx′
ǫ + O(|ǫ|3)
= 1
2ǫtrIH
 Qθ
i

ǫ + O(|ǫ|3)


## Page 62


62
where
IH
 Qθ
i

= Eνθ
i−1
Z
L
pθ(x, x′)∇θ log pθ(x, x′)∇θ log pθ(x, x′)trdx′

is the instantaneous FIM associated to the instantaneous relative entropy.
Consequently, the pFIM I
 Qθ
0:T

, i.e., the Hessian of the pathwise relative
entropy at point θ, is given by
I
 Qθ
0:T

= I
 νθ
+
T
X
i=1
IH
 Qθ
i

,
where I
 νθ
= Eνθ

∇θ log νθ(x)∇θ log νθ(x)tr
is the FIM of the initial dis-
tribution.


## Page 63


63
Appendix: Proof of Theorem 4.1
The following Lemma is an instrumental result for proving this theorem.
Lemma 9.3. For ∆ti > 0 and i ∈{1, 2, ..., T} we have
∇θH(Pi ∥Qθ
i ) = ∇θ [Ri(θ) + ∆tiMi(θ)] ,
where Ri(θ) and Mi(θ) are deﬁned as in Theorem 4.1.
Proof. In order to compute H(Pi ∥Qθ
i ) recall that the transition probability
density of the Euler discretization of the microscopic CLE for x′ ∈Rd is
given by
p(x, x′) =
1
Z∆t(x) exp

−1
2∆t(x′ −m∆t(x))trΣ−1(x)(x′ −m∆t(x))

, (67)
where m∆t(x) := x −b(x)∆t, Z∆t(x) :=
p
(2π∆t)d det(Σ(x)) and Σ(x) :=
σ(x)σtr(x).
Let Π : Rd →R ¯d be a linear map as in (32) such that, Σ(x) can be
partitioned as

Σ1,1(x)
Σ1,2(x)
Σ2,1(x)
Σ2,2(x)

,
where Σ1,1(x) = ΠΣ(x)Πtr ∈R
¯d×R
¯d, Σ2,2(x) = Π⊥Σ(x)Π⊥,tr ∈Rd−¯d×Rd−¯d
and Σ2,1(x) = Σtr
1,2(x).
Considering (67) for x′ ∈Rd let x′ 7→(Πx′, Π⊥x′) = (¯x′, ˆx′), then the
conditional distribution of ˆx′ given ¯x′ can be written as
ˆx′|¯x′ ∼N (Πm∆t(x)+Σ2,1(x)Σ−1
1,1(x)(¯x′−Π⊥m∆t(x)), Σ2,2(x)−Σ2,1(x)Σ−1
1,1(x)Σ1,2(x)) .
This allows us to split the microscopic transition probability as
p(x, x′) = p(1)(x, ¯x′)p(2)(x, ˆx′|¯x′) ,
(68)
where
p(1)(x, ¯x′) =
1
Z(1)
∆t (x)
exp

−1
2∆t(¯x′ −Πm∆t(x))trΣ−1
1,1(x)(¯x′ −Πm∆t(x))

,
with Z(1)
∆t (x) :=
q
(2π∆t) ¯d det(Σ1,1(x)), assuming the matrix Σ1,1 is non-
singular without losing generality.


## Page 64


64
We now describe the macroscopic CLE (corresponding to the reduced
model), which is an approximation of the projected time series (Πxi)T
i=0. Its
Euler discretization is given by
¯xk+1 = ¯xk + ¯b(¯xk; θ)∆t + ¯σ(¯xk; θ)∆¯Wk ,
where
¯b(¯x; θ) = ¯ν¯a(¯x; θ)
and
¯σ(¯x; θ) = ¯ν
p
diag(¯a(¯x; θ) ,
with ∆¯Wk ∼N (0, ∆tI) independent Gaussian increments.
This macroscopic (reduced) model is a parameterized approximation of
the projected microscopic (full) model, with the following conditional density
for ¯x′ ∈R ¯d given ¯x ∈R ¯d
pθ(¯x, ¯x′) =
1
¯Z∆t(¯x; θ) exp

−1
2∆t(¯x′ −¯m∆t(¯x; θ))trΣ−1(¯x; θ)(¯x′ −¯m∆t(¯x; θ))

,
where ¯m∆t(¯x; θ) := ¯x −¯b(¯x; θ)∆t, ¯Z∆t(¯x; θ) :=
p
(2π∆t) ¯d det(¯Σ(¯x; θ)) and
¯Σ(¯x; θ) = ¯σ(¯x; θ)¯σtr(¯x; θ), assuming ¯Σ is non-singular. In the singular case,
a Moore-Penrose pseudo-inverse must be used instead of ¯Σ−1, and a pseudo
determinant instead of the determinant.
In order to compare the microscopic density p with the approximating
macroscopic density pθ, we consider a reconstructed transition probability qθ
in the microscopic space, written in terms of pθ, as follows
qθ(x, x′) = r(x′|¯x′)pθ(¯x, ¯x′) ,
(69)
where r(x′|¯x′) is any probability associated with the reconstruction, indepen-
dent of θ. Now we can write
log p(x, x′)
qθ(x, x′) = log p(1)(x, ¯x′)p(2)(x, ˆx′|¯x′)
pθ(¯x, ¯x′)r(x′|¯x′)
= log p(1)(x, ¯x′)
pθ(¯x, ¯x′) + log p(2)(x, ˆx′|¯x′)
r(x′|¯x′)
,
(*)
where the second term does not depend on θ, so it can be ignored.
Furthermore we have,
log p(1)(x, ¯x′)
pθ(¯x, ¯x′) = −
1
2∆ti
(¯x′ −Πm∆tix))trΣ−1
1,1(x)(¯x′ −Πm∆ti(x))
(**)
+ log
¯Z∆ti(¯x; θ)
Z(1)
∆ti(x)
+
1
2∆ti
(¯x′ −¯m∆ti(¯x; θ))trΣ−1(¯x; θ)(¯x′ −¯m∆ti(¯x; θ)) .


## Page 65


65
The ﬁrst term does not depend on θ so it can be also ignored.
Then using (68), (69), and taking into account (*) and (**), we have
∇θH(Pi ∥Qθ
i ) = ∇θEνi−1
Z
p(x, x′) log p(x, x′)
qθ(x, x′)dx′

= ∇θEνi−1
"Z Z
p(1)(x, ¯x′)p(2)(x, ˆx′|¯x′)
 
log
¯Z∆ti(¯x; θ)
Z(1)
∆ti(x)
+ K∆ti(¯x, ¯x′; θ)
!
dˆx′d¯x′
#
= ∇θEνi−1
"Z
p(1)(x, ¯x′)
 
log
¯Z∆ti(¯x; θ)
Z(1)
∆ti(x)
+ K∆ti(¯x, ¯x′; θ)
!
d¯x′
#
,
where K∆ti(¯x, ¯x′; θ) :=
1
2∆ti(¯x′ −¯m∆ti(¯x; θ))tr ¯Σ−1(¯x; θ)(¯x′ −¯m∆ti(¯x; θ)). The
last equality is because p(2) is a density on ˆx′.
∇θH(Pi ∥Qθ
i ) = ∇θEνi−1
"Z
p(1)(x, ¯x′) log
¯Z∆ti(¯x; θ)
Z(1)
∆ti(x)
d¯x′
#
+ ∇θEνi−1
Z
p(1)(x, ¯x′)K∆ti(¯x, ¯x′; θ)d¯x′

By replacing Z(1)
∆ti, ¯Z∆ti and using that
R
p(1)(x, ¯x′)d¯x′ = 1 the ﬁrst term
is equal to
∇θEνi−1
1
2 log det
 ¯Σ(¯x; θ)Σ−1
1,1(x)

= 1
2∇θEνi−1

log det
 ¯Σ(¯x; θ)(ΠΣ(x)Πtr)−1
= −1
2∇θEνi−1

log det
 (ΠΣ(x)Πtr)¯Σ−1(¯x; θ)

.


## Page 66


66
Consider the second term. We can split K∆ti = K∆ti(¯x, ¯x′; θ) as follows
K∆ti =
1
2∆ti
(Πm∆ti(x)−Πm∆ti(x)+¯x′−¯m∆ti(¯x; θ))tr ¯Σ−1(¯x; θ)
· (Πm∆ti(x)−Πm∆ti(x)+¯x′−¯m∆ti(¯x; θ))
=
1
2∆ti
(Πm∆ti(x) −¯m∆ti(¯x; θ))tr ¯Σ−1(¯x; θ)(Πm∆ti(x) −¯m∆ti(¯x; θ))
+
1
2∆ti
(¯x′ −Πm∆ti(x))tr ¯Σ−1(¯x; θ)(¯x′ −Πm∆ti(x))
= ∆ti
2 (¯b(¯x; θ) −Πb(x))tr ¯Σ−1(¯x; θ)(¯b(¯x; θ) −Πb(x))
+
1
2∆ti
(¯x′ −Πm∆ti(x))tr ¯Σ−1(¯x; θ)(¯x′ −Πm∆ti(x)) .
Now use
R
p(1)(x, ¯x′)d¯x′ = 1 to get
∇θEνi−1
Z
p(1)(x, ¯x′)K∆ti(¯x, ¯x′; θ)d¯x′

=
∆ti
2 ∇θEνi−1

(¯b(¯x; θ) −Πb(x))tr ¯Σ−1(¯x; θ)((¯b(¯x; θ) −Πb(x)))

(I)
+
1
2∆ti
∇θEνi−1
Z
p(1)(x, x′)(¯x′ −Πm∆ti(x))tr ¯Σ−1(¯x; θ)(¯x′ −Πm∆ti(x))d¯x′

.
(II)
For the second summand, (II), consider that ¯Σ(¯x; θ) is a covariance ma-
trix, so exists a matrix S = S(¯x; θ) such that
¯Σ−1(¯x; θ) = Str(¯x; θ)S(¯x; θ) .
Let z := S(¯x; θ)(¯x′ −Πm∆ti(x)), so we have
¯x′ −Πm∆ti(x) = S−1(¯x; θ)z ,
and therefore
(¯x′ −Πm∆ti(x))tr ¯Σ−1(¯x; θ)(¯x′ −Πm∆ti(x)) = ztr(S−1)trStrSS−1z = ztrz .


## Page 67


67
Moreover,
p(1)(x, ¯x′) =
1
Z(1)
∆ti(x)
exp

−
1
2∆ti
(¯x′ −Πm∆ti(x))trΣ−1
1,1(x)(¯x′ −Πm∆ti(x))

=
1
Z(1)
∆ti(x)
exp

−
1
2∆ti
ztr(S−1)trΣ−1
1,1(x)S−1z

=
1
q
(2Π∆ti) ¯d det(Σ1,1(x))
exp

−
1
2∆ti
ztr ˜Σ−1(x)z

,
where ˜Σ(x) := S Σ1,1(x)Str.
Now perform the change of variables det(S)d¯x′ = dz to get that
(II) =
1
2∆ti
∇θEνi−1


1
det(S)
1
q
(2Π∆ti) ¯d det(Σ1,1(x))
exp

−
1
2∆ti
ztr ˜Σ−1(x)z

ztrzdz


=
1
2∆ti
∇θEνi−1


1
q
(2Π∆ti) ¯d det(˜Σ(x))
exp

−
1
2∆ti
ztr ˜Σ−1(x)z

ztrzdz


=
1
2∆ti
∇θEνi−1

Ez

ztrz

=
1
2∆ti
∇θEνi−1

Trace
 Ez

zztr
=
1
2∆ti
∇θEνi−1
h
Trace

∆ti ˜Σ(x)
i
= 1
2∇θEνi−1

Trace
 SΣ1,1(x)Str
= 1
2∇θEνi−1

Trace
 ΠΣ(x)Πtr ¯Σ−1(¯x; θ)

,
where z ∼N (0, ∆ti ˜Σ(x)).


## Page 68


68
Summarizing we have
∇θH(Pi ∥Qθ
i ) = −1
2∇θEνi−1

log det
 (ΠΣ(x)Πtr)¯Σ−1(¯x; θ)

+ 1
2∇θEνi−1

Trace
 ΠΣ(x)Πtr ¯Σ−1(¯x; θ)

+ ∆ti
2 ∇θEνi−1

(¯b(¯x; θ) −Πb(x))tr ¯Σ−1(¯x; θ)(¯b(¯x; θ) −Πb(x))

=: ∇θ [Ri(θ) + Mi(θ)∆ti]
Proof. (of Theorem 4.1). Apply Lemma 9.3 and linearity on (14). Then we
have the same minimizers.
We ﬁrst prove the following Lemma which is instrumental for the proof
of this theorem.
Proposition 9.4. Let
B := (ΠΣ(x)Πtr)¯Σ−1(¯x; θ)
be a ¯d× ¯d matrix .
Then
Trace (B) −log det(B) ≥¯d .
Moreover, the equality is attained if and only if B = I ¯d× ¯d.
Proof. Notice that B is a diagonalizable matrix for any x ∈Rd, ¯x ∈R
¯d,
θ ∈Θ and therefore the problem is reduced to state that
−log λk + λk ≥1 , k=1, 2, ..., ¯d ,
where λk are the positive eigenvalues of B. By simple optimality arguments
we get that 1 −1/λk ≥0 with equality if and only if λk = 1 for k ∈
{1, 2, ..., ¯d}.
References
[1] J. E. Sutton, D. G. Vlachos, Building large microkinetic models with
ﬁrst-principles accuracy at reduced computational cost, Chemical En-
gineering Science 121 (2015) 190–199, 2013 Danckwerts Special Issue
on Molecular Modelling in Chemical Engineering.


## Page 69


69
[2] J. DiStefano III, Dynamic Systems Biology Modeling and Simulation,
1st Edition, Academic Press, 2015.
[3] G. E. Briggs, J. B. S. Haldane, A note on the kinetics of enzyme action,
Biochemical journal 19 (2) (1925) 338.
[4] M. R. Roussel, S. J. Fraser, Invariant manifold methods for metabolic
model reduction, Chaos: An Interdisciplinary Journal of Nonlinear Sci-
ence 11 (1) (2001) 196–206. doi:10.1063/1.1349891.
[5] B. Kooi, J. Poggiale, P. Auger, S. Kooijman, Aggregation methods in
food chains with nutrient recycling., Ecological Modelling 157 (2002)
69–86. doi:10.1016/S0304-3800(02)00217-X.
[6] O. Radulescu, A. N. Gorban, A. Zinovyev, A. Lilienbaum, Robust sim-
pliﬁcations of multiscale biochemical networks, BMC systems biology
2 (1) (2008) 86.
[7] V. Petrov, E. Nikolova, O. Wolkenhauer, Reduction of nonlinear dy-
namic systems with an application to signal transduction pathways,
IET systems biology 1 (1) (2007) 2–9.
[8] K. R. Schneider, T. Wilhelm, Model reduction by extended quasi-
steady-state approximation, Journal of Mathematical Biology 40 (5)
(2000) 443–450. doi:10.1007/s002850000026.
[9] U. Maas, S. B. Pope, Simplifying chemical kinetics:
intrinsic low-
dimensional manifolds in composition space, Combustion and ﬂame
88 (3-4) (1992) 239–264.
[10] R. R. Vallabhajosyula, V. Chickarmane, H. M. Sauro, Conservation
analysis of large biochemical networks, Bioinformatics 22 (3) (2005)
346–353.
[11] J. Zobeley, D. Lebiedz, J. Kammerer, A. Ishmurzin, U. Kummer, A new
time-dependent complexity reduction method for biochemical systems,
in: Transactions on Computational Systems Biology I, Springer, 2005,
pp. 90–110.
[12] I. Surovtsova, N. Simus, T. Lorenz, A. K¨onig, S. Sahle, U. Kummer,
Accessible methods for the dynamic time-scale decomposition of bio-
chemical systems, Bioinformatics 25 (21) (2009) 2816–2823.


## Page 70


70
[13] G. Liu, M. T. Swihart, S. Neelamegham, Sensitivity, principal compo-
nent and ﬂux analysis applied to signal transduction: the case of epi-
dermal growth factor mediated signaling, Bioinformatics 21 (7) (2004)
1194–1202.
[14] D.
Degenring,
C.
Froemel,
G.
Dikta,
R.
Takors,
Sensitiv-
ity
analysis
for
the
reduction
of
complex
metabolism
models,
Journal of Process Control 14 (7) (2004) 729 – 745,
dynam-
ics, Monitoring, Control and Optimization of Biological Systems.
doi:https://doi.org/10.1016/j.jprocont.2003.12.008.
[15] M. Apri, M. de Gee, J. Molenaar, Complexity reduction preserving
dynamical behavior of biochemical networks, Journal of theoretical bi-
ology 304 (2012) 16–26.
[16] T. Tur´anyi, Sensitivity analysis of complex kinetic systems. tools and
applications, Journal of mathematical chemistry 5 (3) (1990) 203–248.
[17] A. S. Tomlin, M. J. Pilling, J. H. Merkin, J. Brindley, N. Burgess,
A. Gough, Reduced mechanisms for propane pyrolysis, Industrial &
engineering chemistry research 34 (11) (1995) 3749–3760.
[18] M. Maurya, S. Bornheimer, V. Venkatasubramanian, S. Subrama-
niam, Reduced-order modelling of biochemical networks: application to
the gtpase-cycle signalling module, IEE Proceedings-Systems Biology
152 (4) (2005) 229–242.
[19] D. Jayachandran, A. E. Rundell, R. E. Hannemann, T. A. Vik,
D. Ramkrishna, Optimal chemotherapy for leukemia: a model-based
strategy for individualized treatment, PloS one 9 (10) (2014) e109623.
[20] M. Maurya, S. Bornheimer, V. Venkatasubramanian, S. Subramaniam,
Mixed-integer nonlinear optimisation approach to coarse-graining bio-
chemical networks, IET systems biology 3 (1) (2009) 24–39.
[21] K. M. Hangos, A. G´abor, G. Szederk´enyi, Model reduction in bio-
chemical reaction networks with michaelis-menten kinetics, in: Control
Conference (ECC), 2013 European, IEEE, 2013, pp. 4478–4483.
[22] J. C. Locke, M. M. Southern, L. Kozma-Bogn´ar, V. Hibberd, P. E.
Brown, M. S. Turner, A. J. Millar, Extension of a genetic network


## Page 71


71
model by iterative experimentation and mathematical analysis, Molec-
ular systems biology 1 (1).
[23] J. Anderson, Y.-C. Chang, A. Papachristodoulou, Model decomposi-
tion and reduction tools for large-scale networks in systems biology,
Automatica 47 (6) (2011) 1165–1174.
[24] T. P. Prescott, A. Papachristodoulou, Guaranteed error bounds for
structured complexity reduction of biochemical networks, Journal of
theoretical biology 304 (2012) 172–182.
[25] S. Danø, M. F. Madsen, H. Schmidt, G. Cedersund, Reduction of a
biochemical model with preservation of its basic dynamic properties,
The FEBS journal 273 (21) (2006) 4862–4877.
[26] A. Dokoumetzidis, L. Aarons, Proper lumping in systems biology mod-
els, IET systems biology 3 (1) (2009) 40–51.
[27] M. Koschorreck, H. Conzelmann, S. Ebert, M. Ederer, E. D. Gilles,
Reduced modeling of signal transduction–a modular approach, BMC
bioinformatics 8 (1) (2007) 336.
[28] M. Sunn˚aker, G. Cedersund, M. Jirstrand, A method for zooming of
nonlinear models of biochemical systems, BMC systems biology 5 (1)
(2011) 140.
[29] A. Majda, R. V. Abramov, M. J. Grote, Information theory and
stochastics for multiscale nonlinear systems, Vol. 25, American Math-
ematical Soc., 2005.
[30] P.
H.
Constantino,
Y.
N.
Kaznessis,
Maximum
en-
tropy
prediction
of
non-equilibrium
stationary
distributions
for
stochastic
reaction
networks
with
oscillatory
dynam-
ics,
Chemical
Engineering
Science
171
(2017)
139
–
148.
doi:https://doi.org/10.1016/j.ces.2017.05.029.
[31] C. H. Lee, K.-H. Kim, P. Kim, A moment closure method for stochastic
reaction networks, The Journal of chemical physics 130 (13) (2009)
134107.


## Page 72


72
[32] C. S. Gillespie, Moment-closure approximations for mass-action mod-
els, IET systems biology 3 (1) (2009) 52–58.
[33] R. Grima, A study of the accuracy of moment-closure approxima-
tions for stochastic chemical kinetics, The Journal of chemical physics
136 (15) (2012) 04B616.
[34] P. ´Erdi, J. T´oth, Mathematical Models of Chemical Reactions: Theory
and Applications of Deterministic and Stochastic Models (Nonlinear
Science), 1st Edition, Princeton University Press, 1989.
[35] D. J. Wilkinson, Stochastic Modelling for Systems Biology, Chapman
& Hall, 2012.
[36] T. Cover, J. Thomas, Elements of Information Theory, John Wiley &
Sons, 1991.
[37] C. Kipnis, C. Landim, Scaling Limits of Interacting Particle Systems,
Springer-Verlag, 1999.
[38] D. J. C. MacKay, Information Theory, Inference & Learning Algo-
rithms, Cambridge University Press, 2003.
[39] C. M. Bishop, Pattern Recognition and Machine Learning (Information
Science and Statistics), Springer-Verlag New York, Inc., Secaucus, NJ,
USA, 2006.
[40] F. J. Pinski, G. Simpson, A. M. Stuart, H. Weber, Kullback–Leibler
approximation for probability measures on inﬁnite dimensional spaces,
SIAM Journal on Mathematical Analysis 47 (6) (2015) 4091–4122.
[41] M. J. Wainwright, M. I. Jordan, Graphical models, exponential fam-
ilies, and variational inference, Found. Trends Mach. Learn. 1 (1-2)
(2008) 1–305.
[42] M. D. Hoﬀman, D. M. Blei, C. Wang, J. Paisley, Stochastic variational
inference, The Journal of Machine Learning Research 14 (1) (2013)
1303–1347.
[43] M. S. Shell, The relative entropy is fundamental to multiscale and
inverse thermodynamic problems, The Journal of Chemical Physics
129 (14) (2008) –. doi:http://dx.doi.org/10.1063/1.2992060.


## Page 73


73
[44] A. Chaimovich, M. S. Shell, Relative entropy as a universal metric for
multiscale errors, Phys. Rev. E 81 (6) (2010) 060104.
[45] J. F. Rudzinski, W. G. Noid, Coarse-graining, entropy, forces and struc-
tures, J. Chem. Phys. 135 (21).
[46] I.
Bilionis,
P.
Koutsourelakis,
Free
energy
computations
by
minimization
of
Kullback-Leibler
divergence:
An
eﬃ-
cient
adaptive
biasing
potential
method
for
sparse
repre-
sentations,
J.
Comput.
Phys.
231
(9)
(2012)
3849
–
3870.
doi:http://dx.doi.org/10.1016/j.jcp.2012.01.033.
[47] I. Bilionis, N. Zabaras, A stochastic optimization approach to coarse-
graining using a relative-entropy framework, J. Chem. Phys. 138 (4)
(2013) 044313.
[48] T. T. Foley, M. S. Shell, W. G. Noid, The impact of resolution upon
entropy and information in coarse-grained models, J. Chem. Phys.
143 (24) (2015) –. doi:http://dx.doi.org/10.1063/1.4929836.
[49] M.
A.
Katsoulakis,
P.
Plech´aˇc,
Information-theoretic tools for
parametrized
coarse-graining
of
non-equilibrium
extended
sys-
tems, The Journal of Chemical Physics 139 (7) (2013) 074115.
doi:10.1063/1.4818534.
[50] V. Harmandaris,
E. Kalligiannaki,
M. Katsoulakis,
P. Plech´aˇc,
Path-space variational inference for non-equilibrium coarse-grained
systems,
Journal of Computational Physics 314 (2016) 355–383.
doi:https://doi.org/10.1016/j.jcp.2016.03.021.
[51] E.
Kalligiannaki,
A.
Chazirakis,
A.
Tsourtis,
M.
Katsoulakis,
P.
Plech´aˇc,
V.
Harmandaris,
Parametrizing
coarse
grained
models
for
molecular
systems
at
equilibrium,
The
European
Physical
Journal
Special
Topics
225
(8)
(2016)
1347–1372.
doi:10.1140/epjst/e2016-60145-x.
[52] Y. Pantazis, M. Katsoulakis, A relative entropy rate method for path
space sensitivity analysis of stationary complex stochastic dynamics, J.
Chem. Phys. 138 (5) (2013) 054115.


## Page 74


74
[53] Y. Pantazis,
M. Katsoulakis,
D. Vlachos,
Parametric sensitiv-
ity
analysis
for biochemical
reaction
networks
based
on
path-
wise information theory, BMC Bioinformatics 14 (1) (2013) 311.
doi:10.1186/1471-2105-14-311.
[54] P. Dupuis, M. A. Katsoulakis, Y. Pantazis, P. Plech´aˇc, Path-space in-
formation bounds for uncertainty quantiﬁcation and sensitivity analysis
of stochastic dynamics, SIAM/ASA Journal on Uncertainty Quantiﬁ-
cation 4 (1) (2016) 80–111. doi:10.1137/15M1025645.
[55] C. J. Proctor, I. A. J. Lorimer, Modelling the role of the hsp70/hsp90
system in the maintenance of protein homeostasis, PLOS ONE 6 (7)
(2011) 1–17. doi:10.1371/journal.pone.0022038.
[56] B. N. Kholodenko, O. V. Demin, G. Moehren, J. B. Hoek, Quan-
tiﬁcation of short term signaling by the epidermal growth factor re-
ceptor, Journal of Biological Chemistry 274 (42) (1999) 30169–30181.
doi:10.1074/jbc.274.42.30169.
[57] J.-C.
Leloup,
A.
Goldbeter,
Toward
a
detailed
computational
model
for
the
mammalian
circadian
clock,
Proceedings
of
the National Academy of Sciences 100 (12) (2003) 7051–7056.
doi:10.1073/pnas.1132112100.
[58] P. Vilanova, Multilevel approximations of markovian jump processes
with applications in communication networks, PhD dissertation, King
Abdullah University of Science and Technology (2015).
[59] S. N. Ethier, T. G. Kurtz, Markov Processes: Characterization and
Convergence (Wiley Series in Probability and Statistics), 2nd Edition,
Wiley-Interscience, 2005.
[60] D. T. Gillespie, Approximated accelerated stochastic simulation of
chemically reacting systems, J. Chem. Phys. 115 (4) (2001) 1716–1733.
[61] Y. Cao, D. T. Gillespie, L. R. Petzold, Eﬃcient step size selection for
the tau-leaping simulation method, J. Chem. Phys. 124 (2006) 044109.
[62] T. Tian, K. Burrage, Binomial leap methods for simulating stochastic
chemical kinetics, J. Chem. Phys. 121 (2004) 10356.


## Page 75


75
[63] A. Chatterjee, D. G. Vlachos, M. A. Katsoulakis, Binomial distribution
based tau-leap accelerated stochastic simulation, J Chem. Phys. 122
(2005) 024112.
[64] A.
Moraes,
R.
Tempone,
P.
Vilanova,
Multilevel
Hybrid
Chernoﬀ
Tau-leap,
BIT
Numerical
Mathematics
(2015)
1–
51doi:10.1007/s10543-015-0556-y.
[65] A.
Moraes,
R.
Tempone,
P.
Vilanova,
Hybrid
Chernoﬀ
tau-
leap, Multiscale Modeling & Simulation 12 (2) (2014) 581–615.
doi:10.1137/130925657.
[66] C. Gardiner, Handbook of Stochastic Methods: for Physics, Chemistry
and the Natural Sciences, Springer, 1985.
[67] N. G. van Kampen, Stochastic Processes in Physics and Chemistry,
North Holland, 2006.
[68] D. T. Gillespie, The chemical Langevin equation, J. Chem. Phys. 113
(2000) 297–306.
[69] T. G. Kurtz, The relationship between stochastic and deterministic
models for chemical reactions, J. Chem. Phys. 57 (1972) 2976.
[70] R. J. Kee, J. A. Miller, T. H. Jeﬀerson, Chemkin: A general-purpose,
problem-independent, transportable, fortran chemical kinetics code
package, Tech. rep., Sandia Labs. (1980).
[71] C. Safta, H. N. Najm, O. Knio, Tchem-a software toolkit for the anal-
ysis of complex kinetic models, Sandia Report, SAND2011-3282.
[72] G. Arampatzis, M. A. Katsoulakis, Y. Pantazis, Accelerated sensitivity
analysis in high-dimensional stochastic reaction networks, PLOS ONE
10 (7) (2015) 1–24. doi:10.1371/journal.pone.0130825.
[73] Y. Chu, J. Hahn, Parameter set selection via clustering of parame-
ters into pairwise indistinguishable groups of parameters, Industrial &
Engineering Chemistry Research 48 (13) (2008) 6000–6009.
[74] A. Cintr´on-Arias, H. Banks, A. Capaldi, A. L. Lloyd, A sensitivity
matrix based methodology for inverse problem formulation, Journal of
Inverse and Ill-posed Problems 17 (6) (2009) 545–564.


## Page 76


76
[75] H. Yue, M. Brown, J. Knowles, H. Wang, D. S. Broomhead, D. B.
Kell, Insights into the behaviour of systems biology models from dy-
namic sensitivity and identiﬁability analysis: a case study of an nf-κb
signalling pathway, Molecular BioSystems 2 (12) (2006) 640–649.
[76] T. G. Kurtz, Approximation of population processes, Society for In-
dustrial and Applied Mathematics (SIAM), 1981.
[77] M. I. Jordan, Z. Ghahramani, T. S. Jaakkola, L. K. Saul, An introduc-
tion to variational methods for graphical models, Machine Learning
37 (2) (1999) 183–233. doi:10.1023/A:1007665907178.
[78] M. J. Wainwright, M. I. Jordan, Graphical models, exponential fami-
lies, and variational inference, Foundations and Trends R⃝in Machine
Learning 1 (1–2) (2008) 1–305. doi:10.1561/2200000001.
[79] D. M. Blei, A. Kucukelbir, J. D. McAuliﬀe, Variational inference: A
review for statisticians, Journal of the American Statistical Association
112 (518) (2017) 859–877. doi:10.1080/01621459.2017.1285773.
[80] B. Efron, Computer age statistical inference : algorithms, evidence,
and data science, Cambridge University Press, New York, NY, 2016.
[81] R. Aster, Parameter estimation and inverse problems, Elsevier Aca-
demic Press, Amsterdam Boston, 2005.
[82] J. Kaipio, Statistical and computational inverse problems, Springer,
New York, 2005.
[83] M. G. Saunders, G. A. Voth, Coarse-graining methods for computa-
tional biology, Annual Review of Biophysics 42 (1) (2013) 73–93, pMID:
23451897. doi:10.1146/annurev-biophys-083012-130348.
[84] S. Izvekov, G. A. Voth, A multiscale coarse-graining method for
biomolecular systems, The Journal of Physical Chemistry B 109 (7)
(2005) 2469–2473. doi:10.1021/jp044629q.
[85] S. L. Brunton, J. L. Proctor, J. N. Kutz, Discovering governing equa-
tions from data by sparse identiﬁcation of nonlinear dynamical systems,
Proceedings of the National Academy of Sciences 113 (15) (2016) 3932–
3937. doi:10.1073/pnas.1517384113.


## Page 77


77
[86] M.
Schmidt,
H.
Lipson,
Distilling
free-form
natural
laws
from
experimental
data,
Science
324
(5923)
(2009)
81–85.
doi:10.1126/science.1165893.
[87] M. Komorowski, M. J. Costa, D. A. Rand, M. P. H. Stumpf, Sensitivity,
robustness, and identiﬁability in stochastic chemical kinetics models,
Proc. Natl. Acad. Sci. USA 108 (2011) 8645–8650.
[88] EMBL-EBI, BioModels Database[link].
URL http://wwwdev.ebi.ac.uk/biomodels/
[89] C. Li, M. Donizelli, N. Rodriguez, H. Dharuri, L. Endler, V. Chel-
liah, L. Li, E. He, A. Henry, M. I. Stefan, J. L. Snoep, M. Hucka,
N. Le Nov`ere, C. Laibe, BioModels Database: An enhanced, curated
and annotated resource for published quantitative kinetic models.,
BMC Systems Biology 4 (2010) 92.
[90] T. G. Kurtz, Strong approximation theorems for density dependent
markov chains, Stochastic Processes and their Applications 6 (3) (1978)
223 – 240.
[91] H.-W. Kang, T. G. Kurtz, Separation of time-scales and model reduc-
tion for stochastic reaction networks, Ann. Appl. Probab. 23 (2) (2013)
529–583. doi:10.1214/12-AAP841.
[92] C. Chassagnole, N. Noisommit-Rizzi, J. W. Schmid, K. Mauch,
M. Reuss, Dynamic modeling of the central carbon metabolism of es-
cherichia coli, Biotechnology and bioengineering 79 (1) (2002) 53–73.
[93] T. Turanyi, T. Berces, S. Vajda, Reaction rate analysis of complex ki-
netic systems, International Journal of Chemical Kinetics 21 (2) (1989)
83–99.
[94] D. Degenring, C. Froemel, G. Dikta, R. Takors, Sensitivity analysis
for the reduction of complex metabolism models, Journal of Process
Control 14 (7) (2004) 729–745.
[95] I. Smets,
K. Bernaerts,
J. Sun,
K. Marchal,
J. Vanderleyden,
J. Van Impe, Sensitivity function-based model reduction: A bacterial
gene expression case study, Biotechnology and bioengineering 80 (2)
(2002) 195–200.


## Page 78


78
[96] A. N. Tikhonov, Systems of diﬀerential equations containing small pa-
rameters in the derivatives, Matematicheskii sbornik 73 (3) (1952) 575–
586.
[97] J. Choi, K.-w. Yang, T.-y. Lee, S. Y. Lee, New time-scale criteria for
model simpliﬁcation of bio-reaction systems, BMC bioinformatics 9 (1)
(2008) 338.
[98] S. West, L. J. Bridge, M. R. White, P. Paszek, V. N. Biktashev, A
method of ‘speed coeﬃcients’ for biochemical model reduction applied
to the nf-\upkappa κ b system, Journal of mathematical biology 70 (3)
(2015) 591–620.
[99] L. Menten, M. Michaelis, Die kinetik der invertinwirkung, Biochem Z
49 (1913) 333–369.
[100] Z. P. Gerdtzen, P. Daoutidis, W.-S. Hu, Non-linear reduction for kinetic
models of metabolic reaction networks, Metabolic Engineering 6 (2)
(2004) 140–154.
[101] V. Noel, D. Grigoriev, S. Vakulenko, O. Radulescu, Tropicalization and
tropical equilibration of chemical reactions, Tropical and Idempotent
Mathematics and Applications 616 (2014) 261–277.
[102] S. Lam, Singular perturbation for stiﬀequations using numerical meth-
ods, in: Recent advances in the aerospace sciences, Springer, 1985, pp.
3–19.
[103] S. Lam, D. Coussis, Conventional asymptotics and computational
singular perturbation for simpliﬁed kinetics modelling, in: Reduced
kinetic mechanisms and asymptotic approximations for methane-air
ﬂames, Springer, 1991, pp. 227–242.
[104] S. Lam, D. Goussis, The csp method for simplifying kinetics, Interna-
tional Journal of Chemical Kinetics 26 (4) (1994) 461–486.
[105] A. Zagaris, H. G. Kaper, T. J. Kaper, Analysis of the computational
singular perturbation reduction method for chemical kinetics, Journal
of Nonlinear Science 14 (1) (2004) 59–91.


## Page 79


79
[106] I. Surovtsova, N. Simus, K. H¨ubner, S. Sahle, U. Kummer, Simpliﬁca-
tion of biochemical models: a general approach based on the analysis of
the impact of individual species and reactions on the systems dynamics,
BMC systems biology 6 (1) (2012) 14.
[107] P. D. Kourdis, R. Steuer, D. A. Goussis, Physical understanding of
complex multiscale biochemical models via algorithmic simpliﬁcation:
Glycolysis in saccharomyces cerevisiae, Physica D: Nonlinear Phenom-
ena 239 (18) (2010) 1798–1817.
[108] J. Wei, J. C. Kuo, Lumping analysis in monomolecular reaction sys-
tems. analysis of the exactly lumpable system, Industrial & Engineering
chemistry fundamentals 8 (1) (1969) 114–123.
[109] J. C. Kuo, J. Wei, Lumping analysis in monomolecular reaction sys-
tems. analysis of approximately lumpable system, Industrial & Engi-
neering chemistry fundamentals 8 (1) (1969) 124–133.
[110] L. H. Hartwell, J. J. Hopﬁeld, S. Leibler, A. W. Murray, From molecular
to modular cell biology, Nature 402 (6761supp) (1999) C47.
[111] J. Saez-Rodriguez, A. Kremling, E. D. Gilles, Dissecting the puzzle
of life: modularization of signal transduction networks, Computers &
chemical engineering 29 (3) (2005) 619–629.
[112] J. Saez-Rodriguez, A. Kremling, H. Conzelmann, K. Bettenbrock, E. D.
Gilles, Modular analysis of signal transduction networks, IEEE control
systems 24 (4) (2004) 35–52.
[113] H.
Conzelmann,
J.
Saez-Rodriguez,
T.
Sauter,
E.
Bullinger,
F. Allg¨ower, E. D. Gilles, Reduction of mathematical models of sig-
nal transduction networks: simulation-based approach applied to egf
receptor signalling, Systems biology 1 (1) (2004) 159–169.
[114] D. M. Wolf, A. P. Arkin, Motifs, modules and games in bacteria, Cur-
rent opinion in microbiology 6 (2) (2003) 125–134.
[115] G. Craciun, C. Pantea, Identiﬁability of chemical reaction networks,
Journal of Mathematical Chemistry 44 (1) (2008) 244–259.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
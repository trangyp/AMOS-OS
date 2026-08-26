---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1906.05353v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1906.05353v2_Conditional_Monte_Carlo_for_Reaction_Networks

> Source: 1906.05353v2_Conditional_Monte_Carlo_for_Reaction_Networks.pdf

> Pages: 36

---


## Page 1


arXiv:1906.05353v2  [math.NA]  4 Jan 2022
CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
DAVID F. ANDERSON∗AND KURT W. EHLERT†
Abstract.
Reaction networks are often used to model interacting species in ﬁelds such as
biochemistry and ecology.
When the counts of the species are suﬃciently large, the dynamics of
their concentrations are typically modeled via a system of diﬀerential equations. However, when the
counts of some species are small, the dynamics of the counts are typically modeled stochastically via
a discrete state, continuous time Markov chain.
A key quantity of interest for such models is the probability mass function of the process at some
ﬁxed time. Since paths of such models are relatively straightforward to simulate, we can estimate
the probabilities by constructing an empirical distribution. However, the support of the distribution
is often diﬀuse across a high-dimensional state space, where the dimension is equal to the number of
species. Therefore generating an accurate empirical distribution can come with a large computational
cost.
We present a new Monte Carlo estimator that fundamentally improves on the “classical” Monte
Carlo estimator described above. It also preserves much of classical Monte Carlo’s simplicity. The
idea is basically one of conditional Monte Carlo. Our conditional Monte Carlo estimator has two
parameters, and their choice critically aﬀects the performance of the algorithm. Hence, a key con-
tribution of the present work is that we demonstrate how to approximate optimal values for these
parameters in an eﬃcient manner. Moreover, we provide a central limit theorem for our estimator,
which leads to approximate conﬁdence intervals for its error.
Key words. Monte Carlo, continuous time Markov chain, chemical master equation, nonpara-
metric density estimation, reaction networks
AMS subject classiﬁcations. 65C05, 60J28, 62G07
1. Introduction. Systems of interacting species appear often in nature.
To
better understand the dynamics of such systems, we can model them as reaction
networks with deterministic or stochastic dynamics [12, 28, 35, 58]. If the counts
of the constituent species are high, then the dynamics are commonly modeled by a
system of diﬀerential equations [12, 24, 58].
However, if the count of any species
is small, then a stochastic model with a discrete state space is more appropriate
[11, 12, 42, 50, 55, 58].
Since the amount of each species is necessarily nonnegative and discrete, the state
space of the stochastic process is a subset of Zd
≥0, where d is the number of species
types.
Let ν be the distribution of the initial state, which is often a point mass
distribution, and suppose we are interested in the distribution of the state of the
process at some ﬁxed time t > 0. That is, if X(t) is the state of the process at time
t, then we would like to know the value of
pν
t (x)
def
= Pν(X(t) = x), x ∈Zd
≥0.
In general, ﬁnding the exact values of pν
t (·) is extremely diﬃcult. More precisely,
the authors are not aware of any general class of models for which pν
t can be solved for
explicitly, with the exception of linear, or ﬁrst-order, models [33] or, more generally,
models that satisfy a dynamical and restricted complex-balanced condition and admit
a time-dependent product form Poisson distribution [13]. However, there are many
numerical methods that give an estimate. One type of approach is to approximately
solve Kolmogorov’s forward equation, which is called the chemical master equation
∗Department of Mathematics, University of Wisconsin-Madison (anderson@math.wisc.edu)
†Department of Mathematics, University of Wisconsin-Madison (kehlert@math.wisc.edu)
1


## Page 2


2
D. F. ANDERSON K. W. EHLERT
(CME) in much of the biology and chemistry literature. The CME can be written as
(1.1)
d
dtpν
t (x) =
R
X
r=1

pν
t (x −ζr)λr(x −ζr) −pν
t (x)λr(x)

, x ∈Zd
≥0,
where R is the number of reactions in the system, λr : Zd
≥0 →R≥0 is the intensity (or
propensity) function for the rth reaction, ζr ∈Zd gives the net change in the counts
of the species due to an occurrence of the rth reaction, and the initial distribution
pν
0(·) is given by ν. See section 2 for the precise speciﬁcation of the model, including
terminology.
For most models of interest, solving (1.1) entails solving a high-dimensional (often
inﬁnite-dimensional) system of linear ordinary diﬀerential equations. Solving such
a system directly is almost always very diﬃcult, so there has been a considerable
amount of research devoted to the development of fast and accurate approximate
algorithms. The general approach for many such algorithms is to ﬁrst truncate the
state space of the system to a smaller subset.
This truncation makes solving the
problem computationally feasible, at the cost of introducing a controllable error to
the solution. After truncation, the new system of ODEs must be solved.
There is currently a wide variety of methods for performing both the truncation
step and solution step. In particular, there is the ﬁnite state projection algorithm
[45, 56], the uniformization method [21], sliding window methods [32, 59], the sparse
grid method [31], the radial basis function approximation [37], a class of spectral
methods [23, 34], and methods that specialize to systems with multiple scales [16,
19, 39, 40, 48]. Moreover, there are tensor methods [36, 53, 57] that represents the
truncated CME with tensors.
As an alternative to approximating (1.1) directly via the methods above, we can
take a Monte Carlo approach. That is, we can generate n independent and identically
distributed (i.i.d.) realizations of the process X, denoted by {Xi}n
i=1, and use the
Monte Carlo estimator
(1.2)
1
n
n
X
i=1
1(Xi(t) = x) ≈Eν,0 [
1(X(t) = x)] = pν
t (x),
where Eν,0 is the expectation under the initial distribution ν and starting time of
zero. By the strong law of large numbers, the approximation becomes an equality as
n goes to inﬁnity.
To utilize the above estimator, we need to simulate exact realizations of the
process X over the time interval [0, t], and there are many methods to choose from.
In particular, there is the Gillespie algorithm, also called the stochastic simulation
algorithm, [26], the next reaction method [25], and the modiﬁed next reaction method
[1], which are all straightforward to implement and often have similar eﬃciency. For
our numerical results in the later sections, we used the modiﬁed next reaction method.
One drawback of using the Monte Carlo estimator (1.2) to approximate the solu-
tion to the CME (1.1) is that huge numbers of simulations are generally required to
achieve a high level of accuracy. That said, the Monte Carlo estimator has at least
two distinct advantages when compared against the methods that approximately solve
the CME directly: it is very simple to implement and it is substantially less sensitive
to the dimension of the state space.
There are two natural ways to improve upon a Monte Carlo estimator.
The
ﬁrst way is to decrease the time required to generate realizations of the random


## Page 3


CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
3
samples (i.e., the process X in our case). Lowering the time required to generate
paths of the processes that we are interested in has been an active area of research for
almost two decades [1, 25, 41, 43, 49, 54]. Moreover, researchers have also designed
eﬃcient algorithms that generate approximate paths that trade some accuracy for
speed [2, 10, 17, 18, 22, 27, 30, 51].
The second way to improve upon a Monte Carlo estimator, and the focus of
this article, is to instead lower the variance of the estimator itself. There are many
broadly applicable variance reduction techniques, including coupling methods, control
variates, stratiﬁed sampling, antithetic random variables, quasi-Monte Carlo, and
conditional Monte Carlo [29, 47].
In this paper, we utilize a form of conditional Monte Carlo to reduce the variance.
Brieﬂy, conditional Monte Carlo follows from the observation that for one-dimensional
random variables X and Y , deﬁned on the same probability space, we have E[X] =
E[E[X|Y ]], and Var(E[X|Y ]) ≤Var(X), so long as all the expectations are well
deﬁned [14]. That is, one can always reduce variance by conditioning. Of course, the
“art” is in the selection of an appropriate random variable Y .
Returning to our situation, deﬁne Eν,s[f(X(t)] as the expectation of f(X(t)) taken
with respect to the initial state distribution ν and starting time 0 ≤s ≤t. That is,
P(X(s) = x) = ν(x). If ν is a point-mass distribution at y ∈Zd
≥0, then we write
Ey,s[f(X(t))]. Fix h ∈[0, t], then
pν
t (x) = Eν,0 [1(X(t) = x)]
= Eν,0 [Eν,0 [
1(X(t) = x)| X(t −h)]]
= Eν,0

EX(t−h),t−h [1(X(t) = x)]

(Markov property)
= lim
n→∞
1
n
n
X
i=1
EXi(t−h),t−h [1(X(t) = x)] , a.s.
(strong law of large numbers)
(1.3)
where the {Xi(t −h)}n
i=1 are i.i.d. realizations of X(t −h). A natural estimator for
the right hand side of the above equation is
(1.4)
ˆpν
t (x; n, m, h)
def
= 1
n
n
X
i=1
1
m
m
X
j=1
1(Xij(t) = x),
where we generate the Xij in the following manner:
• simulate n independent realizations of the process X over the time interval
[0, t −h], each with an initial value determined by ν, and denote the ith
realization by Xi,
• for each i ∈{1, . . . , n}, generate m conditionally independent realizations
over the time interval [t −h, t], each of which has initial state Xi(t −h).
Denote the jth such realization by Xij.
Note that for each j ∈{1, . . . , m}, the process Xij is equal to Xi over the interval
[0, t −h]. See Figure 1.
Since {Xi1j(t)}m
j=1 and {Xi2j}m
j=1 are independent for i1 ̸= i2, the strong law of
law numbers implies that with probability one we have
lim
n→∞ˆpν
t (x; n, m, h) = Eν,0

1
m
m
X
j=1
1(Xij(t) = x)

= pν
t (x).
Hereafter we will refer to the original estimator (1.2) as classical Monte Carlo, and


## Page 4


4
D. F. ANDERSON K. W. EHLERT
0
0.5
1
1.5
2
0
20
40
60
80
100
120
(a) Two independent realizations of
the process over the time interval
[0, 2].
0
0.5
1
1.5
2
0
20
40
60
80
100
120
m
h
(b) Two independent realizations of
the process generated over [0, 1.5].
Each is then followed by m con-
ditionally independent “branches”
simulated over [1.5, 2].
Fig. 1. Paths generated for the birth model X →2X.
the new estimator (1.4) as conditional Monte Carlo. The conditional Monte Carlo
estimator has two unspeciﬁed parameters, denoted m and h. The number of branches
is determined by m, and the time at which branching occurs is controlled by h. If m
and h are ﬁxed, then the remaining parameter n is simply chosen large enough such
that the estimator’s variance is below some desired threshold. If m = 1, h = 0, or
h = t, then the conditional and classical Monte Carlo estimators are the same. If
m > 1 and h ∈(0, t), then for the same computational cost as classical Monte Carlo,
the conditional Monte Carlo estimator obtains more observations of X(t). We would
like to choose the values of m and h such that, in some sense, our new estimator is
more eﬃcient than classical Monte Carlo. In section 3, we provide an algorithm for
ﬁnding optimal values of m and h, which is the key contribution of this article.
The distributions produced by our conditional Monte Carlo method can, of course,
be used to construct unbiased estimates of moments and other expectations. How-
ever, we stress here that our new estimator is optimized for estimating the entire
distribution of the process and not for estimating expectations. Estimating expec-
tations is a separate–and very important–problem that has seen a large amount of
research activity over the past decade (see [5, 6, 7, 8, 9, 17, 18, 44] for a subset of
works focusing on this problem). In fact, in Appendix B we prove that the type of
conditioning we carry out here (optimized for estimating the entire distribution) can
not be more eﬃcient than standard Monte Carlo for the estimation of the expected
value of a linear birth process at some future time t > 0. This may seem surprising at
ﬁrst since conditioning always reduces the variance (as discussed above). However, in
the present method we also use Monte Carlo to solve for the conditional expectation,
which has its own cost. Determining better, and perhaps optimal, ways to estimate
expectations via conditional Monte Carlo in the present context is a worthy direction
of future research and will be discussed further in section 6 and Appendix B.
The remainder of the article is organized as follows. In section 2, we deﬁne the
continuous time Markov chain model of reaction networks. Then in section 3, we
present an algorithm for ﬁnding the optimal values of m and h, and also the full
algorithm, Algorithm 3.3, for the implementation of the conditional Monte Carlo
estimator.
Next, in section 4, we give numerical results demonstrating the order


## Page 5


CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
5
of magnitude improvement that can be obtained with the use of conditional Monte
Carlo in the current context.
In section 5, we derive a central limit theorem for
the error of the conditional Monte Carlo estimator and then test it on examples.
Finally, in section 6, we summarize our results and suggest ideas for future work. The
proofs of the main results are in Appendix A. The supplementary material contain
more ﬁgures related to numerical results. An example MATLAB implementation of
the conditional Monte Carlo algorithm is at https://github.com/kehlert/conditional
monte carlo example.
2. Mathematical model. Suppose our reaction network has d types of species
and R reactions. For 1 ≤r ≤R,
(i) we will denote by ζr the reaction vector for the rth reaction, meaning that
if the rth reaction occurs at time t, and the process is currently in state
x ∈Zd
≥0, then the new state becomes x + ζr;
(ii) we will denote by λr : Zd
≥0 →[0, ∞) the intensity, or propensity, function of
the rth reaction.
A standing assumption is that λr(x) = 0 if x + ζr /∈Zd
≥0, which preserves the non-
negativity of the components. We let X be a continuous time Markov chain (CTMC)
whose transition rate from state x to x′ is
q(x, x′) =
R
X
r=1
λr(x)1(x′ −x = ζr).
Hence, X is a Markov process with inﬁnitesimal generator Af(x) = PR
r=1 λr(x)(f(x+
ζr) −f(x)), where f : Zd
≥0 →R is a bounded function with compact support. We
will denote our process by X, so that X(t) ∈Zd
≥0 is the vector whose ith component
gives the count of species i at time t ≥0.
The most common choice of intensity function is stochastic mass action kinetics.
Suppose that we require yi copies of species i for the rth reaction to occur. Then we
say that λr has stochastic mass action kinetics if
(2.1)
λr(x) = κr
d
Y
i=1
xi!
(xi −yi)!
1(xi ≥yi),
for some κr > 0, which is called the rate constant of the reaction. For example,
for the reaction 2A + B →A + C, where A, B, and C are the species types in our
model system, the reaction vector is (−1, −1, 1)T and y = (2, 1, 0)T, in which case
λr(x) = κrx1(x1 −1)x2, where we have ordered the species alphabetically.
None of our theoretical results assume that the λr has the above mass action
form, but the models we tested do use it unless otherwise noted.
One well–known representation for the stochastic process X is the random time
change representation of Thomas Kurtz [11, 12, 38]
(2.2)
X(t) = X(0) +
R
X
r=1
Yr
Z t
0
λr (X(s)) ds

ζr,
where X(0) is the initial state and the Yr are independent unit-rate Poisson processes.
We will make use of the above representation in some of our proofs.


## Page 6


6
D. F. ANDERSON K. W. EHLERT
2.1. Examples. In the subsequent sections, we intersperse numerical results,
and below is a list of all the example models we used. The species to the left of the
arrows are the reactants (giving the counts of the species consumed in the reaction),
and those to the right are the products. The numbers above the arrows are the rate
constants κr. Unless otherwise noted, for every model and reaction we deﬁne the
intensities λr with (2.1).
(i) Birth
The initial state is X(0) = 10 and t = 2. The single reaction is
X
1−→2X.
Following (2.1), the rate of the reaction is λ(x) = x.
(ii) Birth–Death
The initial state is X(0) = 100 and t = 2. There are two reactions
∅
50
−→X, X
1−→∅.
Following (2.1), the rates of the reactions are λ1(x) = 50, and λ2(x) = x,
respectively.
(iii) Lotka–Volterra
This model is also often called the predator-prey model. The initial state is
A(0) = 200 and B(0) = 100. We set t = 4. The reactions are
A
2−→2A, A + B
0.01
−−→2B, B
2−→∅.
Following (2.1), and after ordering the species as (A, B), the rates of the
reactions are λ1(x) = 2x1, λ2(x) = 0.01x1x2, and λ3(x) = 2x2, respectively.
(iv) Dimerization
In this model, mRNA is translated into the protein P, which then dimerizes
into D, and the dimer D accumulates over time. The initial state for every
species is zero except for G(0) = 1. We set t = 1. The reactions are
G
25
−→G + mRNA, mRNA
100
−−→mRNA + P
2P
0.001
−−−→D, mRNA
0.1
−−→∅, P
1−→∅.
Following (2.1), and after ordering the species as (G, mRNA, P, D), the rates
of the reactions are λ1(x) = 25x1, λ2(x) = 100x2, λ3(x) = 0.001x3(x3 −1),
λ4(x) = 0.1x2, and λ5(x) = x3 respectively.
(v) Toggle
Each species represses the production of the other, which leads to a probabil-
ity mass function that is multimodal. The initial state is A(0) = B(0) = 0.
We set t = 100. The reactions are
∅−→A, A −→∅, ∅−→B, B −→∅.
For this model, the ﬁrst and third intensity functions are not chosen to be
mass action. Speciﬁcally, we let
λ1(x) =
50
1 + 2x2
, λ2(x) = x1, λ3(x) =
50
1 + 2x1
, λ4(x) = x2,
where we again ordered the species as (A, B).


## Page 7


CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
7
(vi) Fast/Slow
A and B quickly convert into one another, and B slowly turns into C. The
initial state is A(0) = B(0) = 100 and C(0) = 0. We set t = 10. The reactions
are
A
10
−→B, B
10
−→A, B
0.1
−−→C.
Following (2.1), and after ordering the species as (A, B, C), the rates are
λ1(x) = 10x1, λ2(x) = 10x2, and λ3(x) = 0.1x2, respectively.
3. Determining the values of m and h via optimization. The conditional
Monte Carlo estimator (1.4) is of little value without knowledge of which values of m
and h to use. In this section, we will show that appropriate values can be found by
numerically solving an easy optimization problem.
Recall that the distribution of the process is denoted by pν
t , and we denote an
estimate of this distribution by ˆpν
t . We will measure the quality of the estimation via
the mean integrated squared error (MISE), which is
(3.1)
MISE(ˆpν
t )
def
= Eν,0


X
x∈Zd
≥0
 ˆpν
t (x) −pν
t (x)
2

.
Note that if ˆpν
t is constructed via our conditional Monte Carlo estimator, then it,
and by extension MISE(ˆpν
t ), is a function of n, m, and h. Suppose we have a ﬁxed
computational budget, which we denote as b. We then want to choose the values of
n, m, and h so that we minimize MISE(ˆpν
t ) subject to our budget constraint b. We
choose the squared error in (3.1), as opposed to the total variation norm or some other
Lp error, as this choice was more amenable to analysis, especially in the derivation of
the central limit theorem in Section 5.
3.1. Computational cost model. Assuming that our model is non-explosive1
the expected number of reactions required to generate {X1j}m
j=1 is given by
Eν,0
"Z t−h
0
λ0(X(s)) ds
#
|
{z
}
expected # of reactions in [0,t−h]
+ m · Eν,0
Z t
t−h
λ0(X(s)) ds

|
{z
}
expected # of reactions in [t−h,t]
,
where λ0(x) = PR
r=1 λr(x) (see Theorem A.1). Hence, the expected computational
cost for our conditional Monte Carlo estimator is
(3.2)
n · c
 
Eν,0
"Z t−h
0
λ0(X(s)) ds
#
+ m · Eν,0
Z t
t−h
λ0(X(s)) ds
!
,
where c > 0 is an unknown constant.
Since we cannot generally evaluate the expectations in the cost model (3.2), as
this would be as diﬃcult as the problem we are attempting to solve, we need to
1A process is said to explode if there are an inﬁnite number of transitions in a ﬁnite amount of
time. A process is said to be non-explosive if the probability of an explosion is zero for all initial
distributions [3, 46].


## Page 8


8
D. F. ANDERSON K. W. EHLERT
estimate them. To do so, ﬁx a relatively small ˜n and simulate ˜n i.i.d. paths {Xi}˜n
i=1.
Then the expectations are approximately equal to
(3.3)
1
˜n
˜n
X
i=1
Z t−h
0
λ0(Xi(s)) ds, and 1
˜n
˜n
X
i=1
Z t
t−h
λ0(Xi(s)) ds.
Importantly, for the ﬁxed set of ˜n paths, the values (3.3) can be computed for a
variety of diﬀerent h values. The process Xi is piecewise constant, and therefore so is
λ0(Xi). Thus, for any value of h, we can easily compute the integrals so long as we
have stored the jump times of Xi and the value of λ0(Xi) at each jump.
3.2. Optimization problem. Given a reaction network, our goal is to ﬁnd
values of n, m, and h that minimize the mean integrated squared error (MISE) (3.1) for
our conditional Monte Carlo estimator (1.4) while staying within our computational
budget of b. More precisely, we want to solve the following optimization problem
min
n,m,h Eν,0


X
x∈Zd
≥0
 ˆpν
t (x; n, m, h) −pν
t (x)
2


|
{z
}
mean integrated squared error (MISE)
,
(3.4)
subject to
n · c
 
Eν,0
"Z t−h
0
λ0(X(s)) ds
#
+ m · Eν,0
Z t
t−h
λ0(X(s)) ds
!
≤b
n, m ∈Z≥1 and 0 ≤h ≤t.
(3.5)
The following theorem will allow us to transform the above optimization problem
into a more solvable form.
Theorem 3.1. Suppose the process X is non-explosive. For any ﬁxed n, m ∈Z≥1
and h ∈[0, t]
Eν,0


X
x∈Zd
≥0
 ˆpν
t (x; n, m, h) −pν
t (x)
2

=
1
n

1
m +

1 −1
m

Pν(X11(t) = X12(t)) −
X
x∈Zd
≥0
pν
t (x)2

.
The proof of Theorem 3.1 can be found in Appendix A.2.
If we allow n to be continuous, then we can use the constraint (3.5) to solve
for n−1, and subsequently eliminate the constraint by substitution. This leads to a
simpler optimization problem. In particular, let
f(m, h)
def
=
 
1
m Eν,0
"Z t−h
0
λ0(X(s)) ds
#
+ Eν,0
Z t
t−h
λ0(X(s)) ds
!
×


1 + (m −1)Pν(X11(t) = X12(t)) −m
X
x∈Zd
≥0
pν
t (x)2


.


## Page 9


CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
9
Then the original optimization problem (3.4) and (3.5) is equivalent to
min
m,h f(m, h)
m ∈Z≥1, 0 ≤h ≤t.
(3.6)
Note that both c and b have dropped out of the optimization problem.
There are three terms in f that we must know, or be able to approximate, in
order to solve (3.6).
• The expectations of the integrals. We discussed how to approximate these in
subsection 3.1.
• The sum P
x pν
t (x)2. However, we note that P
x pν
t (x)2 is the probability that
two independent paths end up in the same state at time t. For many models,
including the ones we tested, that sum is much smaller than Pν(X11(t) =
X12(t)) and is close to zero. Thus for our examples, we replace the sum with
zero and make that our general recommendation.
• The term Pν(X11(t) = X12(t)), whose approximation is the subject of the
next section.
Note that there are many models for which P
x pν
t (x)2 will not be near zero. How-
ever, for such models a small number of states will necessarily have a large probability.
An example of such a model would be a Birth-Death model, as in Section 2.1, with
input rate 1 and output rate 1. Such a model has a stationary distribution that is
Poisson with a parameter of 1 [4], and so for large t the distribution pν
t will concen-
trate on the set {0, 1, 2, 3}. Other examples where P
x pν
t (x)2 is not small include
those with extinction events. For such models, it would not be appropriate to set
this term to zero. However, for models with diﬀuse probability mass functions, i.e.,
those models for which estimating pν
t is diﬃcult and are the focus of this paper, the
assumption will often be valid.
3.3. Approximating the joint probability. In order to optimize the objective
function f(m, h) in (3.6), we need to know, or be able to quickly approximate, the
term Pν(X11(t) = X12(t)). The following theorem, proven in Appendix A.3, will allow
us to make a good approximation, without requiring any additional simulations. The
theorem makes use of the Skellam(µ1, µ2) distribution, which is the distribution of
the diﬀerence between two independent Poisson random variables with parameters µ1
and µ2, respectively.
Theorem 3.2. Let S be the d × R matrix whose rth column is ζr and let null(S)
be the right nullspace of S restricted to integer values. Let X and Z satisfy
X(t) = X(0) +
R
X
r=1
Y X
r
Z t
0
λr(X(s))ds

ζr,
Z(t) = X(0) +
R
X
r=1
Y Z
r
Z t
0
λr(X(s))ds

ζr,
where the Y X
r
and Y Z
r
are independent, unit-rate Poisson processes. Assume that X
is non-explosive. For each 1 ≤r ≤R and 0 ≤a ≤b ≤t, denote
Λa,b
r
=
Z b
a
λr(X(s))ds,


## Page 10


10
D. F. ANDERSON K. W. EHLERT
and let Ka,b
r
have the Skellam(Λa,b
r , Λa,b
r ) distribution. Then
(3.7)
Pν(X(t) = Z(t)) =
X
k∈null(S)
Eν,0
" R
Y
r=1
P
 K0,t
r
= kr
 Λ0,t
r

#
.
Note that X is the process (2.2) that is of interest to us. Returning to our setup, if
we assume that
Z t
t−h
λr(X11(s)) ds ≈
Z t
t−h
λr(X12(s)) ds,
which should be valid for small h, then Theorem 3.2 leads to an approximation of
Pν(X11(t) = X12(t)). In particular, we may sample ˜n paths and for the ith such path
deﬁne
Λt−h,t
r,i
=
Z t
t−h
λr(Xi(s)) ds, 1 ≤i ≤˜n.
Then Pν(X11(t) = X12(t)) ≈ˆPν(X11(t) = X12(t)), where
(3.8)
ˆPν(X11(t) = X12(t))
def
=
X
k∈˜
N
1
˜n
˜n
X
i=1
R
Y
r=1
P

Kt−h,t
r
= kr
 Λt−h,t
r,i

,
and ˜N is a ﬁnite subset of null(S).
To ﬁnd ˜N, we use the “Algorithm for Solving the Linear Diophantine Equation
Problem” from section 1.5.2 of [20]. In general, the algorithm ﬁnds solutions x ∈Zd
to linear equations of the form Ax = b for rational A and b. In our case, we enumerate
solutions to Sk = 0 for k ∈Zd. Generally, there are inﬁnitely many solutions, however
the right-hand side of (3.8) is always maximized at k = 0, and decreases as k moves
away from 0. Thus we approximate (3.8) by starting at k = 0 and enumerating all
“nearby” solutions. Algorithm 3.1 shows how to apply the algorithm from [20] to our
particular problem. In all of our numerical examples, we chose C = 4 in Algorithm 3.1.
Algorithm 3.1 Algorithm for enumerating a ﬁnite subset of null(S) ∈Zd×R
Require: the stoichiometry matrix S and C ∈Z>0
1: if S does not have full row rank then
2:
Remove redundant equations from the system and replace S.
3: end if
4:
5: Transform S into its Hermite normal form H, and store the matrix U that satisﬁes
H = SU.
6: r ←R −rank(S)
7: Let ˜U be the matrix containing the last r columns of U.
8:
9: ˜N ←
n
˜Uz
 z ∈Zr, ||z||∞≤C
o
3.4. Approximation to the optimization problem. By using the joint prob-
ability approximation (3.8), we can approximate the function f in the optimization


## Page 11


CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
11
Algorithm 3.2 Algorithm for computing ˆPν(X11(t) = X12(t))
Require: ˜n i.i.d. samples of X, denoted {Xi}˜n
i=1 ⊲˜n = 500 was more than suﬃcient.
Require: the stoichiometry matrix S, and a ﬁnite ˜N ⊂null(S)
1: for all r in 1, . . . , R and i in 1, . . . , ˜n do
2:
Λt−h,t
r,i
←
R t
t−h λr(Xi(s)) ds
3: end for
4:
5: ˆP ←0
6: for all k in ˜N and i in 1, . . . , ˜n do
7:
ˆP ←ˆP + QR
r=1 P

Kt−h,t
r
= kr
 Λt−h,t
r,i

⊲Kt−h,t
r
∼Skellam(Λt−h,t
r,i
, Λt−h,t
r,i
)
8: end for
9:
10: ˆPν(X11(t) = X12(t)) ←ˆP/˜n
problem (3.6). In particular, let
ˆf(m, h)
def
=
 
1
m
Z t−h
0
¯λ0(X(s)) ds +
Z t
t−h
¯λ0(X(s)) ds
!


1 + (m −1) ˆPν(X11(t) = X12(t)) −m
✟✟✟✟✟✟
✯0
X
x∈Zd
≥0
pν
t (x)2


,
(3.9)
where ¯λ0(X(s)) = 1
˜n
P˜n
i=1
PR
r=1 λr(Xi(s)), and the {Xi}˜n
i=1 are independent paths
of X. Then we may substitute f with ˆf and our new optimization problem is the
following:
min
m,h
ˆf(m, h)
m ∈R≥1, 0 ≤h ≤t.
(3.10)
Note that above we have allowed m to be real–valued, as opposed to integer valued.
This allows us to use continuous optimization algorithms, which generally converge
more rapidly. According to Figure SM1, which shows ˆf(m, h) for many values of m
and h, ˆf does not change too quickly with m, so allowing m to range over the reals
instead of the integers should not change the optimal values of m and h appreciably.
It is important to know when the optimization problem (3.10) has a ﬁnite solution.
In the proposition below, we show that a solution necessarily exists when ˆPν(X11(t) =
X12(t)) is larger than the approximation used for P
x pν
t (x)2. Since we approximate
the sum with zero, we may conclude that a ﬁnite solution always exists in our setup.
Proposition 3.3. Let bp2 be our approximation to P
x pν
t (x)2. If ˆPν(X11(t) =
X12(t)) > bp2 for all h ∈[0, t], then (3.10) has a ﬁnite solution.
Proof. Since the integrals are nonnegative, h is in a compact domain, ˆf depends
continuously on h and m, and limm→∞ˆf(m, h) = ∞, a ﬁnite solution exists.
Algorithm 3.3 outlines the full conditional Monte Carlo algorithm, which brings
together all of the individual pieces of the algorithm that we previously discussed.


## Page 12


12
D. F. ANDERSON K. W. EHLERT
Algorithm 3.3 Conditional Monte Carlo algorithm
Require: ˜n i.i.d. samples of X, denoted {Xi}˜n
i=1 ⊲˜n = 500 was more than suﬃcient.
1: m, h ←arg minm∈R≥1
0≤h≤t
ˆf(m, h)
2:
⊲Use {Xi}˜n
i=1, (3.9), and Algorithm 3.2 to evaluate ˆf.
3: for all i in 1, . . . , n do
4:
Sample Xi(t −h).
⊲The Xi(t −h) are i.i.d.
5:
for all j in 1, . . . , m do
6:
Sample Xij(t) conditioned on Xij(t −h) = Xi(t −h).
7:
⊲See section 1 for details about Xij.
8:
end for
9: end for
10:
11: ˆpν
t (x; n, m, h) ←1
n
Pn
i=1
1
m
Pm
j=1
1(Xij(t) = x)
4. Numerical results. In this section, we present numerical results demon-
strating the improvement in accuracy, quantiﬁed via the mean integrated squared
error (3.1), that comes from using our conditional Monte Carlo estimator instead of
the classical Monte Carlo estimator. In particular, when near–optimal values of m
and h are utilized, the accuracy often improves by an order of magnitude for a ﬁxed
computational budget. Moreover, we show that the function ˆf of (3.10) is indeed a
very good approximation for f of (3.6) for the examples we considered, allowing us
to conclude that the values of m and h our method produces are near–optimal.
The following steps were carried out on each of our test examples. First, we ﬁxed
an integer n1 and computed the classical Monte Carlo estimator
pMC
t
(x; n1) = 1
n1
n1
X
i=1
1(Xi(t) = x), x ∈Zd
≥0.
For all models, we used n1 = 104. We also recorded the number of random variates
used in generating pMC
t
( · ; n1), which served as the budget b in the computational
cost constraint (3.5).
After obtaining pMC
t
( · ; n1), we computed the conditional Monte Carlo estimator
pCMC
t
(x; n2, m, h) = 1
n2
n2
X
i=1
1
m
m
X
j=1
1(Xij(t) = x), x ∈Zd
≥0,
for various pairs of m and h, and n2 was allowed to increase until the conditional
estimator used essentially the same number of random variates as the classical Monte
Carlo estimator. All random variates generated for the conditional estimators were
independent of those utilized for the classical estimator.
Next, for both classical and conditional Monte Carlo, we computed the integrated
squared error
(4.1)
ISE =
X
˜S
(ˆp(x) −pν
t (x))2 ,
where ˜S was a large ﬁxed subset of the state space, and ˆp(x) was either the classical
or conditional Monte Carlo estimate. The ISE is itself a random variable, and so we


## Page 13


CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
13
0.001
0.0017
0.0028
0.0048
0.0081
0.0136
0.023
0.0387
0.0653
0.1101
0.1856
0.313
0.5277
0.8897
1.5
h
1
2
3
5
8
12
20
32
52
85
139
228
373
611
1000
m
Empirical error improvement
1.00
1.78
2.40
3.33
4.25
5.02
5.87
6.48
6.92
7.18
7.25
7.19
6.95
6.53
5.90
1.00
1.88
2.64
3.94
5.45
6.90
8.76
10.27
11.52
12.32
12.72
12.53
11.96
10.87
9.43
1.00
1.93
2.79
4.33
6.29
8.40
11.47
14.35
16.97
18.88
19.85
19.69
18.40
16.08
13.27
1.00
1.96
2.87
4.59
6.90
9.58
13.85
18.47
23.19
27.12
29.02
28.81
26.21
22.09
17.28
1.00
1.97
2.91
4.71
7.23
10.28
15.42
21.34
28.13
27.13
20.41
1.00
1.98
2.93
4.78
7.38
10.58
16.19
22.91
30.86
29.96
21.78
1.00
1.98
2.93
4.77
7.38
10.58
16.17
22.84
30.76
29.90
22.10
1.00
1.97
2.91
4.71
7.22
10.22
15.33
21.24
27.88
27.20
20.75
1.00
1.96
2.87
4.58
6.88
9.55
13.82
18.38
23.08
26.96
29.19
29.29
26.87
23.02
18.37
1.00
1.93
2.80
4.37
6.37
8.56
11.76
14.86
17.72
19.92
21.18
21.20
20.12
17.98
14.89
1.00
1.89
2.69
4.06
5.68
7.30
9.46
11.30
12.88
13.99
14.55
14.62
14.09
13.14
11.56
1.00
1.83
2.54
3.66
4.87
5.96
7.28
8.27
9.08
9.59
9.88
9.92
9.70
9.31
8.53
1.00
1.76
2.35
3.21
4.05
4.73
5.48
6.00
6.39
6.63
6.76
6.80
6.72
6.57
6.31
1.00
1.66
2.14
2.77
3.32
3.73
4.13
4.40
4.60
4.72
4.77
4.80
4.78
4.76
4.66
1.00
1.55
1.90
2.33
2.65
2.88
3.10
3.22
3.31
3.37
3.40
3.41
3.40
3.39
3.38
34.16
37.50
37.13
33.20
38.29
42.76
42.43
37.27
38.14
42.63
42.48
37.65
33.80
37.30
37.31
33.61
0.001
0.0017
0.0028
0.0048
0.0081
0.0136
0.023
0.0387
0.0653
0.1101
0.1856
0.313
0.5277
0.8897
1.5
h
1
2
3
5
8
12
20
32
52
85
139
228
373
611
1000
m
Scaled reciprocal of the objective function
1.00
1.62
2.03
2.55
2.98
3.29
3.58
3.76
3.87
3.91
3.90
3.82
3.68
3.44
3.11
1.00
1.79
2.43
3.41
4.39
5.23
6.16
6.82
7.27
7.51
7.54
7.34
6.93
6.28
5.41
1.00
1.89
2.68
4.02
5.61
7.17
9.20
10.89
12.25
13.06
13.29
12.87
11.86
10.35
8.46
1.00
1.94
2.82
4.43
6.53
8.85
12.31
15.72
18.86
21.09
21.91
21.14
18.97
15.76
12.22
1.00
1.97
2.90
4.65
7.05
9.88
14.50
19.55
24.83
26.06
20.91
15.47
1.00
1.97
2.90
4.65
7.05
9.88
14.51
19.56
24.85
26.06
20.89
15.47
1.00
1.98
2.93
4.76
7.34
10.49
15.90
22.27
25.58
18.37
1.00
1.98
2.92
4.74
7.28
10.36
15.62
21.72
28.57
25.62
18.75
1.00
1.96
2.88
4.59
6.91
9.59
13.89
18.45
23.15
26.94
28.85
28.42
25.73
21.45
16.62
1.00
1.94
2.81
4.40
6.45
8.70
12.03
15.27
18.29
20.56
21.67
21.44
19.98
17.30
14.19
1.00
1.90
2.70
4.07
5.72
7.36
9.54
11.41
12.98
14.06
14.53
14.48
13.75
12.45
10.79
1.00
1.84
2.54
3.68
4.90
6.01
7.33
8.35
9.13
9.64
9.83
9.83
9.48
8.87
7.93
1.00
1.76
2.36
3.24
4.10
4.80
5.56
6.10
6.48
6.73
6.80
6.77
6.69
6.37
5.83
1.00
1.67
2.15
2.78
3.34
3.76
4.17
4.44
4.63
4.74
4.78
4.77
4.69
4.59
4.35
1.00
1.56
1.91
2.34
2.68
2.91
3.12
3.26
3.34
3.39
3.42
3.43
3.36
3.32
3.16
29.03
30.95
29.81
29.04
30.88
29.81
29.53
35.90
39.11
37.86
32.66
34.59
37.73
36.94
32.31
Fig. 2. Lotka-Volterra model. The ﬁrst heatmap shows MISEMC/MISECMC(m, h) for diﬀerent
values of m and h. The method we used to obtain the ratio is described in section 4. The second
heatmap shows that value of ˆf(1, 0)/ ˆf(m, h). The deﬁnition of ˆf is given by (3.9).
approximated the mean integrated square error (MISE) by averaging 100 independent
samples of the ISE.
The exact values of pν
t (x) were unknown. Thus the values were estimated with
conditional Monte Carlo with a large value of n1 (we used n1 = 109), and with m and
h chosen so that they approximately minimize the MISE.
Finally, we denote by MISEMC our estimate of the classical Monte Carlo MISE,
and, for a given m and h, we denote by MISECMC(m, h) the conditional version. For
each model, and for each choice of m and h, an “empirical error improvement” was
computed as the following ratio
MISEMC
MISECMC(m, h),
where a number greater than one implies that conditional Monte Carlo has a lower
MISE than classical Monte Carlo when given the same computational budget. These
values, one for each pair of m and h, can then be plotted. In the top half of Figures 2
and 3 (and Figures SM2 to SM5), we display these values with a heatmap. Of par-
ticular interest is the order of magnitude improvement in computational eﬃciency we
see with the conditional Monte Carlo estimator as compared to classical Monte Carlo
when well–chosen values of h and m are utilized. In particular, for the Lotka-Volterra
model we see a 40-fold improvement, for the dimerization model we see a 20-fold im-
provement, for the toggle model we see a 20-fold improvement, and for the fast/slow


## Page 14


14
D. F. ANDERSON K. W. EHLERT
0.001
0.0015
0.0022
0.0033
0.0048
0.0072
0.0107
0.0158
0.0235
0.0348
0.0516
0.0766
0.1136
0.1685
0.25
h
1
2
3
5
8
12
20
32
52
85
139
228
373
611
1000
m
Empirical error improvement
1.00
1.85
2.57
3.74
5.02
6.19
7.54
8.51
9.08
9.18
8.75
7.85
6.60
5.20
3.84
1.00
1.90
2.70
4.09
5.74
7.38
9.50
11.15
12.24
12.46
11.76
10.28
8.33
6.29
4.46
1.00
1.93
2.79
4.34
6.29
8.37
11.26
13.79
15.58
16.11
15.10
12.92
10.15
7.40
5.12
1.00
1.95
2.84
4.50
6.68
9.11
12.74
16.13
15.63
12.02
8.60
5.84
1.00
1.96
2.87
4.57
6.85
9.47
13.48
13.53
9.61
6.50
1.00
1.95
2.87
4.57
6.86
9.48
13.54
14.65
10.56
7.21
1.00
1.95
2.84
4.50
6.69
9.14
12.87
16.48
14.98
11.21
7.88
1.00
1.93
2.79
4.36
6.36
8.51
11.64
14.50
16.93
16.90
14.41
11.32
8.36
1.00
1.90
2.72
4.14
5.87
7.62
9.99
12.03
13.69
14.66
14.82
14.17
12.73
10.62
8.38
1.00
1.86
2.61
3.85
5.24
6.57
8.21
9.53
10.53
11.13
11.30
11.02
10.31
9.19
7.74
1.00
1.80
2.46
3.48
4.54
5.45
6.49
7.25
7.81
8.16
8.25
8.16
7.89
7.31
6.56
1.00
1.73
2.28
3.06
3.79
4.37
4.96
5.38
5.66
5.83
5.90
5.86
5.75
5.49
5.14
1.00
1.63
2.06
2.61
3.07
3.39
3.72
3.93
4.07
4.14
4.18
4.18
4.13
4.01
3.84
1.00
1.51
1.81
2.16
2.42
2.59
2.76
2.85
2.91
2.95
2.96
2.96
2.94
2.92
2.84
1.00
1.37
1.56
1.75
1.89
1.97
2.04
2.08
2.11
2.13
2.13
2.13
2.12
2.11
2.07
18.83
19.76
18.54
17.40
20.71
22.10
20.89
17.65
17.55
21.05
22.73
21.88
18.80
19.62
21.28
20.87
18.53
18.36
18.32
0.001
0.0015
0.0022
0.0033
0.0048
0.0072
0.0107
0.0158
0.0235
0.0348
0.0516
0.0766
0.1136
0.1685
0.25
h
1
2
3
5
8
12
20
32
52
85
139
228
373
611
1000
m
Scaled reciprocal of the objective function
1.00
1.31
1.46
1.63
1.68
1.72
1.75
1.73
1.67
1.58
1.46
1.27
1.05
0.81
0.60
1.00
1.41
1.64
1.86
2.03
2.16
2.15
2.10
2.05
1.88
1.66
1.39
1.10
0.81
0.58
1.00
1.49
1.77
2.08
2.28
2.40
2.49
2.43
2.33
2.11
1.79
1.49
1.12
0.81
0.55
1.00
1.49
1.76
2.08
2.29
2.42
2.49
2.45
2.32
2.09
1.82
1.47
1.11
0.81
0.55
1.00
1.64
2.05
2.58
2.98
2.95
2.51
2.06
1.51
1.08
0.72
0.47
1.00
1.69
2.18
2.83
3.17
2.65
2.00
1.43
0.99
0.65
0.42
1.00
1.74
2.31
3.06
2.57
1.91
1.31
0.85
0.54
0.35
1.00
1.76
2.35
3.16
3.19
2.53
1.78
1.15
0.78
0.49
0.30
1.00
1.78
2.38
3.21
2.98
2.23
1.50
1.00
0.65
0.42
0.26
1.00
1.77
2.34
3.14
2.76
2.08
1.34
0.89
0.55
0.36
0.22
1.00
1.75
2.27
2.96
3.17
2.45
1.76
1.18
0.78
0.50
0.32
0.19
1.00
1.68
2.17
2.84
3.11
3.08
2.89
2.15
1.58
1.11
0.73
0.48
0.50
0.25
1.00
1.60
2.01
2.42
2.81
2.78
2.73
2.44
1.96
1.54
1.08
0.74
0.50
0.33
0.25
1.00
1.49
1.77
2.11
2.25
2.29
2.61
2.07
1.98
1.45
1.49
0.79
0.73
0.47
0.23
1.00
1.36
1.54
1.72
1.88
1.96
1.92
1.92
1.80
1.39
1.10
0.93
0.86
0.42
0.38
3.22
3.30
3.23
3.29
3.63
3.76
3.64
3.66
4.11
4.20
3.87
3.35
3.79
4.25
4.31
3.92
3.85
4.25
4.26
3.83
3.81
4.01
3.95
3.54
3.47
3.82
3.50
3.41
Fig. 3. Dimerization model. The ﬁrst heatmap shows MISEMC/MISECMC(m, h) for diﬀerent
values of m and h. The method we used to obtain the ratio is described in section 4. The second
heatmap shows that value of ˆf(1, 0)/ ˆf(m, h). The deﬁnition of ˆf is given by (3.9).
model we see a 20-fold improvement. For the birth and birth–death models we see
more modest improvements in computational eﬃciency, but this can be explained by
the simplicity of these models which makes classical Monte Carlo suﬃcient for the
task at hand. In particular, one promising aspect of the present work comes into fo-
cus with these numerical results: the more complicated the model, and the larger and
more diﬀuse the distribution of the model (which is where other methods, including
those that approximately solve the chemical master equation directly, struggle), the
better the performance of the conditional Monte Carlo estimator.
In practice, we are not given the optimal values of the parameters m and h, so
we ﬁnd them via the optimization problem (3.10). In each of the bottom portions
of Figures 2 and 3 (and Figures SM2 to SM5), we provide the values of ˆf(m, h) for
the diﬀerent pairs of m and h. We report the inverse so that the heatmap will agree
qualitatively with the top portion of the ﬁgures (higher values are desirable). We also
normalized the values by multiplying them by ˆf(1, 0), which does not aﬀect the results
of the optimization problem in any way. To generate each value 1/ ˆf(m, h) we ﬁrst
sampled ˜n = 500 paths, which then allowed us to compute ¯λ0 and ˆPν(X11(t) = X12(t))
as detailed in the previous section. We could then use these values to compute ˆf(m, h)
via (3.9).
Note that the empirical error improvement and ˆf do not need to have the same
value for a pair of m and h. The important thing is that the maximizer of the empirical
error improvement is similar to the minimizer of ˆf. The heatmaps do indeed suggest


## Page 15


CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
15
that the true and approximate optimization problems have similar solutions. What
is also clear from these numerical results is that even if m and h slightly deviate from
their optimal values, we still get a substantial improvement.
We stress that such heatmaps do not need to be made by anyone who uses the
conditional Monte Carlo algorithm. They are only used here to demonstrate that
the optimization problem (3.10) can be safely used to ﬁnd the near–optimal values
of m and h, which can then be used to construct the desired estimator (1.4) via
Algorithm 3.3.
5. A central limit theorem. In this section, we will show how to obtain an
approximate one-sided conﬁdence interval for the integrated squared error (4.1) with-
out running more simulations. Speciﬁcally, for a ﬁxed (presumably large) ﬁnite subset
of the state space ˜S, a ﬁxed α ∈(0, 1), and large n, we want to ﬁnd a sequence of
positive constants {Cn} and a constant u > 0 such that
(5.1)
lim
n→∞P

Cn
X
x∈˜S
 ˆpν
t (x; n, m, h) −pν
t (x)
2
|
{z
}
integrated squared error
≤u

= 1 −α,
where Cn is allowed to depend on m and h. The following central limit theorem will
lead us to values for {Cn} and u.
Theorem 5.1. Fix m ∈Z≥1 and h ∈[0, t].
Let S ⊂Zd
≥0 be the state space
of the continuous time Markov chain, and let ˜S be a ﬁnite subset of S. Choose an
enumeration of ˜S and denote it {xi}| ˜
S|
i=1. Let pν
t , ˆpν
t ∈R| ˜
S| with their ith elements
equal to pν
t (xi) and ˆpν
t (xi; n, m, h), respectively. Let
(5.2)
Σ
def
= m diag(pν
t ) + m(m −1)A −m2pν
t (pν
t )T ,
where diag(pν
t ) is the diagonal matrix with pν
t along its diagonal, and A is a | ˜S| × | ˜S|
matrix where Aij = Pν(X11(t) = xi, X12(t) = xj). Then
(5.3)
nm2 X
x∈˜
S
 ˆpν
t (x; n, m, h) −pν
t (x)
2
d→
| ˜S|
X
ℓ=1
λℓZ2
ℓ, as n →∞,
where {λℓ}| ˜S|
ℓ=1 are the eigenvalues of Σ and Zℓ
i.i.d.
∼N(0, 1).
Σ is usually an enormous matrix, so we do not want to store it, much less compute
its eigenvalues. The Satterthwaite approximation [52] says that
(5.4)
X
ℓ
λℓZ2
ℓ
d≈
P
ℓλ2
ℓ
P
ℓλℓ
χ2
 
(P
ℓλℓ)2
P
ℓλ2
ℓ
!
= tr
 Σ2
tr (Σ) χ2
 
tr (Σ)2
tr (Σ2)
!
,
where χ2(v) denotes a χ2 random variable with v degrees of freedom. The approxima-
tion is obtained by matching the ﬁrst two moments of the linear combination (above
left-hand side) and the chi-squared distribution (above right-hand side). The advan-
tage of the approximation is that we can estimate tr (Σ) and tr
 Σ2
without storing
Σ explicitly or computing its eigenvalues.
Theorem 5.2. Fix n, m ∈Z≥1 and h ∈[0, t]. Let ˜S, {xk}| ˜
S|
k=1, and ˆpν
t be deﬁned
as in Theorem 5.1. For 1 ≤i ≤n, let Mi ∈Z| ˜
S|
≥0, and set its kth element to Mi(xk)
def
=


## Page 16


16
D. F. ANDERSON K. W. EHLERT
Pm
j=1
1(Xij = xk) (the {Xij} are deﬁned in section 1). Let ˆΣn be the usual sample
covariance matrix of {Mi}n
i=1. Speciﬁcally,
ˆΣn
def
=
1
n −1
n
X
i=1
 Mi −M
  Mi −M
T ,
where M = n−1 Pn
i=1 Mi. Then
(5.5)
tr

ˆΣn

=
1
n −1
n
X
i=1
M T
i Mi −nm2
n −1(ˆpν
t )T ˆpν
t ,
and
(5.6)
tr

ˆΣ2
n

=
1
(n −1)2
n
X
i=1
h
M T
i Mi −2M
T Mi + m2(ˆpν
t )T ˆpν
t
i2
+
2
(n −1)2
X
1≤i<j≤n
h
M T
i Mj −M
T Mi −M
T Mj + m2(ˆpν
t )T ˆpν
t
i2
.
Furthermore
tr

ˆΣn
 a.s.
→tr (Σ) and tr

ˆΣ2
n
 a.s.
→tr
 Σ2
as n →∞.
For the models we tested, the optimal value of m was only moderately large (on
the order of 10 to 100), and the indicator in the summand of Mi(x) is zero for many
values of x. Whenever those two conditions hold, Mi sparse. Consequently, storing
{Mi}n
i=1 does not require too much memory, and the terms M T
i Mj and M
T Mi are
cheap to compute. Algorithm 5.1 summarizes how we compute the traces. Using the
sparsity of the Mi is important, because otherwise the vectors are too large to store
and the operations are slow.
Algorithm 5.1 Algorithm for computing ˆpν
t , tr

ˆΣn

, and tr

ˆΣ2
n

Require: n, m ∈Z≥1 and h ∈[0, t]
1: for i in {1, . . . , n} do
2:
Sample Xi(t −h).
3:
Given Xi(t −h), sample {Xij(t)}m
j=1.
4:
for x in ˜S do
5:
Mi(x) ←Pm
j=1
1(Xij(t) = x)
⊲Store Mi as a sparse vector.
6:
end for
7: end for
8:
9: ˆpν
t ←
1
nm
Pn
i=1 Mi
10: Compute tr

ˆΣn

according to (5.5).
11: Compute tr

ˆΣ2
n

according to (5.6).
Corollary 5.3. Fix n, m ∈Z≥1 and h ∈[0, t]. Also ﬁx an α ∈(0, 1), and let
χ2
α(v) be the 1−α quantile of the χ2 distribution with v degrees of freedom. An approx-
imate 1 −α conﬁdence interval for P
x∈˜
S
 ˆpν
t (x; n, m, h) −pν
t (x)
2 is [0, Un/(nm2)],


## Page 17


CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
17
where
(5.7)
Un
def
=
tr

ˆΣ2
n

tr

ˆΣn
χ2
α



tr

ˆΣn
2
tr

ˆΣ2n



.
Figures 4a and 4b (and also Figures SM6 to SM9), compare the empirical distri-
bution of
(5.8)
nm2 X
x∈˜
S
 ˆpν
t (x; n, m, h) −pν
t (x)
2
to the approximate asymptotic distribution (5.4), where the true traces are replaced
with the sample traces from Algorithm 5.1. The ﬁgures also compare the sample 95%
quantile to the same quantile based on Corollary 5.3, which turned out to be close.
6. Directions for future research. We demonstrated how to implement a
version of conditional Monte Carlo in the context of continuous time Markov chain
models for reaction networks. There are many possible directions for future research;
we list three.
1. The method could be extended so it provides estimates of the distribution at
multiple ﬁxed time-points. The method we developed, and in particular the
optimization problem we utilize to ﬁnd the values of m and h, is tailored to
the single time-point case.
2. In the method developed here the conditional expectation in (1.3)
EXi(t−h),t−h [1(X(t) = x)]
is approximated by Monte Carlo with m conditionally independent realiza-
tions. However, it could be approximated by solving the chemical master
equation directly, perhaps via the ﬁnite state projection algorithm [45]. Be-
cause the solver need only integrate the system of ODEs over the time interval
[t −h, t], the probability mass should not become too diﬀuse, thereby solving
one of the major diﬃculties related to these solvers.
We implemented this approach and observed some increase in eﬃciency over
the conditional Monte Carlo algorithm Algorithm 3.3, around a factor of
three.
However, the gains were only realized when an optimal value of h
was chosen, and we needed to test many diﬀerent h values in order to ﬁnd
the optimal value. In practice, we would need a faster method for ﬁnding
the optimal parameters, similar to the optimization problem detailed in this
paper.
3. As discussed in the introduction and Appendix B, the present method is not
optimized for the estimation of expectations. Developing a new conditional
Monte Carlo estimator tailored to that problem is a natural focus of future
work.
Appendix A. Proofs.
A.1. Theorem regarding the expected number of reactions.
Theorem A.1. Suppose that the process X is non-explosive and ﬁx h ∈[0, t] and
m ∈Z≥1. Then the expected number of reactions required to sample {X1j}m
j=1 is
Eν,0
"Z t−h
0
λ0(X(s)) ds
#
+ m Eν,0
Z t
t−h
λ0(X(s)) ds

.


## Page 18


18
D. F. ANDERSON K. W. EHLERT
0
100
200
300
400
500
0
0.01
0.02
0.03
0.04
0.05
339.07
338.86
0
100
200
300
400
500
0
0.01
0.02
0.03
0.04
0.05
335.88
338.86
0
100
200
300
400
500
0
0.01
0.02
0.03
0.04
0.05
335.88
338.86
0
100
200
300
400
500
0
0.01
0.02
0.03
0.04
0.05
338.90
338.86
(a) Lotka-Volterra model.
0
1000
2000
3000
4000
5000
0
0.2
0.4
0.6
0.8
1
1.2
10-3
2168.62
2239.30
0
1000
2000
3000
4000
5000
0
0.2
0.4
0.6
0.8
1
1.2
10-3
2180.26
2239.30
0
1000
2000
3000
4000
5000
0
0.2
0.4
0.6
0.8
1
1.2
10-3
2181.25
2239.30
0
1000
2000
3000
4000
5000
0
0.2
0.4
0.6
0.8
1
1.2
10-3
2199.28
2239.30
(b) Dimerization model.
Fig. 4. The dashed blue density is the empirical density of the integrated squared error (5.8),
whereas the solid red density is the Satterwaithe approximation to the asymptotic density (5.4). The
blue cross and red circle are the 95% quantiles of their respective densities. To generate the blue
curve, ﬁrst we sampled 104 values of nm2 P
x∈˜
S
 ˆpν
t (x; n, m, h) −pν
t (x)
2 (which we call the “scaled
integrated squared error”) for diﬀerent values of n.
Given those samples, we used MATLAB’s
ksdensity function to generate the blue curve.
The traces of Σ and Σ2 were estimated with an
independent set of 105 simulations and Algorithm 5.1.


## Page 19


CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
19
Proof. The number of reactions required to sample {X(s)}s∈[a,b] is
R
X
r=1
"
Yr
 Z b
0
λr (X(s)) ds
!
−Yr
Z a
0
λr (X(s)) ds
#
,
where the Yr are independent unit-rate Poisson processes [38]. For each r,
Yr
Z t
0
λr (X(s)) ds

−
Z t
0
λr (X(s)) ds
is a martingale [12, Theorem 1.22], so the result follows.
A.2. Proof of Theorem 3.1. For simplicity, denote Xij(t) as Xij. We start
with the left-hand side of the desired equality. The monotone convergence theorem
implies that we can move the expectation inside the sum, by which we mean
Eν,0
"X
x
 ˆpν
t (x; n, m, h) −pν
t (x)
2
#
=
X
x
Eν,0
h ˆpν
t (x; n, m, h) −pν
t (x)
2i
=
X
x
Var[ˆpν
t (x; n, m, h)].
The last line follows from the fact that the estimator ˆpν
t is unbiased.
From the
deﬁnition of ˆpν
t , and also basic properties of variance, the above is equal to
=
X
x
Var

1
nm
n
X
i=1
m
X
j=1
1(Xij = x)


=
1
nm2
X
x


m
X
j=1
Var[1(X1j = x)] + 2
X
1≤i<j≤m
Cov
 1(X1i = x),
1(X1j = x)



=
1
nm2
X
x
[mVar[1(X11 = x)] + m(m −1)Cov(1(X11 = x),
1(X12 = x))]
=
1
nm
X
x
h
pν
t (x)(1−pν
t (x)) + (m−1)

Eν,0 [1(X11 = x)1(X12 = x)] −pν
t (x)2i
=
1
nm
X
x

pν
t (x) + (m −1)Pν(X11 = x, X12 = x) −mpν
t (x)2
= 1
n
"
1
m +

1 −1
m

Pν(X11 = X12) −
X
x
pν
t (x)2
#
.
We can also take pν
t (x) to be a marginal distribution. In that case, interpret sums
over x as sums over the lower-dimensional marginal variables. Also, view X11 = X12
as being true if their coordinates corresponding to the marginal variables are equal.
A.3. Proof of Theorem 3.2. Let Λ0,t ∈RR
≥0 be the vector whose rth element
is Λ0,t
r , and let Y X, Y Z ∈ZR
≥0 be the vectors whose rth elements are Y X
r (Λ0,t
r ) and


## Page 20


20
D. F. ANDERSON K. W. EHLERT
Y Z
r (Λ0,t
r ), respectively. Then
Pν(X(t) = Z(t)) = Pν
 SY X = SY Z
= Pν
 S(Y X −Y Z) = 0

=
X
k∈null(S)
Pν(Y X −Y Z = k)
=
X
k∈null(S)
Eν,0

P(Y X −Y Z = k
 Λ0,t)

.
The elements of Y X and Y Z are independent when conditioned on Λ0,t. Therefore
we can expand the conditional probability into a product of probabilities, by which
we mean
P
 Y X −Y Z = k | Λ0,t
=
R
Y
r=1
P
 Y X
r
−Y Z
r = kr
 Λ0,t
r

.
When conditioned on Λ0,t
r , Y X
r
−Y Z
r
is the diﬀerence of two independent Poissons
with the same intensity Λ0,t
r . Therefore the diﬀerence follows a Skellam distribution.
To summarize,
K0,t
r
def
= Y X
r
−Y Z
r ∼Skellam(Λ0,t
r , Λ0,t
r ), when conditioned on Λ0,t.
Continuing from above,
Pν(X11(t) = X12(t)) =
X
k∈null(S)
Eν,0
" R
Y
r=1
P
 K0,t
r
= kr
 Λ0,t
r

#
,
where the expectation is taken over Λ0,t.
If we are estimating a marginal distribution, then we need to modify the sum
slightly. Let S′ be the same as S, except the rows corresponding to the marginalized-
out variables are removed. Then replace null(S) with null(S′).
A.4. Proof of Theorem 5.1. Let {Xi(t−h)}n
i=1 be i.i.d. realizations of X(t−h).
Deﬁne Xij(t) to be the state of the CTMC conditioned on Xij(t −h) = Xi(t −h),
where 1 ≤j ≤m. For simplicity, later we will denote Xij(t) as just Xij.
Let Mi ∈Z| ˜
S|
≥0, where the kth element of Mi is deﬁned as Pm
j=1
1(Xij = xk). Let
Σ ∈R| ˜
S|×| ˜
S| be the covariance matrix of M1. The Mi are i.i.d., so if Σ is ﬁnite, then
the usual multivariate central limit theorem implies that
1
√n
n
X
i=1
(Mi −mpν
t )
d→N(0, Σ), as n →∞.
Let Mi(x) denote the element if Mi corresponding to x. Then by deﬁnition, for all x
nmˆpν
t (x; n, m, h) =
n
X
i=1
Mi(x).
Therefore
√nm (ˆpν
t −pν
t )
d→N(0, Σ), as n →∞.


## Page 21


CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
21
The dot product is continuous, so the continuous mapping theorem implies that
nm2 X
x∈˜
S
 ˆpν
t (x; n, m, h) −pν
t (x)
2
d→N(0, Σ)T N(0, Σ), as n →∞.
[15, Theorem 2.1] implies that the right side has the same distribution as P| ˜S|
ℓ=1 λℓZ2
ℓ.
Let Σxx be the element of Σ on the diagonal corresponding to state x.
Then by
deﬁnition
Σxx = Var


m
X
j=1
1(X1j = x)


=
m
X
j=1
Var [1(X1j = x)] + 2
X
1≤j<k≤m
Cov( 1(X1j = x),
1(X1k = x)) .
Var [1(X1j = x)] = pν
t (x)(1 −pν
t (x)), and the covariance simpliﬁes when we rewrite it
in terms of expectations. We get
Σxx = mpν
t (x) + m(m −1)Pν(X11(t) = x, X12(t) = x) −m2pν
t (x)2 < ∞.
Let x1 and x2 be distinct states, and let Σx1,x2 be the element whose row and column
correspond to the states x1 and x2, respectively. By deﬁnition
Σx1,x2 = Cov


m
X
j=1
1(X1j = x1),
m
X
j=1
1(X1j = x2)


=
m
X
j=1
m
X
k=1
Cov [1(X1j = x1),
1(X1k = x2)] .
Rearrange the terms in the sum to get
m
X
j=1
Cov[1(X1j = x1),
1(X1j = x2)] +
m
X
j=1
m
X
k=1
k̸=j
Cov [1(X1j = x1),
1(X1k = x2)] ,
which is equivalent to
m
X
j=1

Eν,0 [1(X1j = x1)1(X1j = x2)] −p(x1)p(x2)

+
m
X
j=1
m
X
k=1
k̸=j

Eν,0 [1(X1j = x1)1(X1k = x2)] −p(x1)p(x2)

.
Since x1 ̸= x2,
1(X1j = x1)1(X1j = x2) = 0. Also, the second expectation can be
rewritten as a probability. The above expression simpliﬁes to
m(m −1)Pν (X11(t) = x1, X12(t) = x2) −m2pν
t (x1)pν
t (x2) < ∞.
Equation (5.2) simply expresses the above results with matrix-vector notation.
If we are estimating a marginal distribution, then take S to be the lower dimen-
sional space corresponding to the marginal variables. Also interpret X(t) as the state
vector containing only the marginal variables.


## Page 22


22
D. F. ANDERSON K. W. EHLERT
A.5. Proof of Theorem 5.2. If we write out the deﬁnition of ˆΣn and use the
fact that the trace is linear, we can see that
tr

ˆΣn

=
1
n −1
n
X
i=1
tr
 Mi −¯
M
  Mi −¯
M
T 
.
We use the cyclic property of the trace to rewrite the right side as
1
n −1
n
X
i=1
 Mi −¯
M
T  Mi −¯
M

.
Expanding the summands leads to
1
n −1
n
X
i=1
 M T
i Mi −2 ¯
M TMi + ¯
M T ¯
M

.
From the deﬁnition of ¯
M, the above expression is equal to
−
n
n −1
¯
M T ¯
M +
1
n −1
n
X
i=1
M T
i Mi.
By deﬁnition, mˆpt = ¯
M, therefore
tr

ˆΣn

= −nm2
n −1(ˆpν
t )T ˆpν
t +
1
n −1
n
X
i=1
M T
i Mi.
Next consider tr

ˆΣ2
n

. We will proceed in a similar way. By deﬁnition
ˆΣ2
n =
1
(n −1)2
" n
X
i=1
(Mi −¯
M)(Mi −¯
M)T
#2
=
1
(n −1)2
n
X
i=1
n
X
j=1
(Mi −¯
M)(Mi −¯
M)T (Mj −¯
M)(Mj −¯
M)T .
The trace is linear, so
tr

ˆΣ2
n

=
1
(n −1)2
n
X
i=1
n
X
j=1
tr
 (Mi −¯
M)(Mi −¯
M)T (Mj −¯
M)(Mj −¯
M)T 
=
1
(n −1)2
n
X
i=1
n
X
j=1

(Mi −¯
M)T (Mj −¯
M)
2 .
The last line follows from the cyclic property of the trace.
When we expand the
summands, the right side becomes
1
(n −1)2
n
X
i=1
n
X
j=1

M T
i Mj −¯
M T Mi −¯
M TMj + m2(ˆpν
t )T ˆpν
t
2 .
As for the claim about almost sure convergence of the traces, note that ˆΣn
a.s.
→Σ.
Since matrix multiplication and the trace are continuous, the continuous mapping
theorem implies the result.


## Page 23


CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
23
A.6. Proof of Corollary 5.3. Deﬁne
U = tr
 Σ2
tr (Σ) χ2
α
 
tr (Σ)2
tr (Σ2)
!
.
Since ˆΣn
a.s.
→Σ as n →∞, the continuous mapping theorem and Lemma A.2 taken
together imply that Un →U almost surely as n →∞. Also Theorem 5.1 says that
nm2 X
x∈˜
S
 ˆpν
t (x; n, m, h) −pν
t (x)
2
d→
| ˜S|
X
ℓ=1
λℓZ2
ℓ, as n →∞.
Therefore by Slutsky’s theorem
nm2 P
x∈˜
S
 ˆpν
t (x; n, m, h) −pν
t (x)
2
Un
d→
P| ˜S|
ℓ=1 λℓZ2
ℓ
U
, as n →∞,
which we can rewrite as
lim
n→∞Pν

nm2 X
x∈˜
S
 ˆpν
t (x; n, m, h) −pν
t (x)
2 ≤Un

= P


| ˜S|
X
ℓ=1
λℓZ2
ℓ≤U

.
Applying the Satterthwaite approximation [52] to the right-hand side gives
lim
n→∞Pν

nm2 X
x∈˜
S
 ˆpν
t (x; n, m, h) −pν
t (x)
2 ≤Un


≈P
 
tr
 Σ2
tr (Σ) χ2
 
tr (Σ)2
tr (Σ2)
!
≤U
!
= 1 −α.
The result still holds for marginal distributions. We just need to remove the coordi-
nates of ˜S corresponding to the variables that are marginalized out.
Lemma A.2. Let Xθ be a family of random variables parameterized by θ ∈R with
strictly increasing cumulative distribution functions Fθ. Suppose that for each θ, the
function Fθ is continuous. Assume also that Fθ(x) is continuous in θ for each x ∈R.
Then the 1 −α quantiles of Fθ are also continuous in θ for all α ∈(0, 1).
Proof. Let α ∈(0, 1), and let {θn}∞
n=1 be a sequence that converges to θ. Deﬁne
qn and q to be the 1 −α quantiles corresponding the θn and θ, respectively. We want
to show that qn converges to q.
Let ε > 0. Since α ∈(0, 1), we know that q is ﬁnite. Therefore, we can choose q
and q such that
q < q < q
and
q −q < ε.
We want to show that |qn −q| < ε for all suﬃciently large n, so it will suﬃce to prove
that q < qn < q for all n large enough.
By assumption, Fθ(q) is continuous in θ, so
lim
n→∞Fθn(q) = Fθ(q) < Fθ(q) = 1 −α = Fθn(qn).


## Page 24


24
D. F. ANDERSON K. W. EHLERT
The inequality is strict, because q is a quantile and Fθ is strictly increasing and q < q.
Since Fθn is non–decreasing, qn > q for all suﬃciently large n. We can use essentially
the same argument to conclude that qn < q for all n large enough.
Appendix B. Expectations.
The speciﬁc conditional Monte Carlo method introduced in this paper has been
developed to estimate the entire distribution in a manner that is more eﬃcient than
regular Monte Carlo, as quantiﬁed by the mean integrated squared error (3.4) for
a ﬁxed computational budget.
This does not imply that it will be more eﬃcient
in the computation of any speciﬁc expectation. In fact, in this Appendix we prove
that it is necessarily less eﬃcient in computing the ﬁrst moment of a linear birth
model. Speciﬁcally, we prove that for a ﬁxed computational budget the variance of
the estimator generated via the conditional Monte Carlo method is greater than or
equal to the variance of the standard Monte Carlo estimator. This demonstrates that
caution is required when implementing a method in a context it was not intended for.
Recall the Birth Model, which consists of the single reaction X
1−→2X, where we
have chosen a rate parameter of 1. Assuming a ﬁxed initial condition of X0 ∈Z≥0, it
is straightforward to show that
E[X(t)] = X0et
and
Var[X(t)] = X0et(et −1).
For a ﬁxed number of paths n1, and a point mass X0, the standard Monte Carlo
estimator has an expected cost–quantiﬁed by the number of random variables utilized–
of
CostMC(n1) = E[n1(X(t) −X0)] = n1X0(et −1),
and a variance of Var

n−1
1
Pn1
i=1 Xi(t)

= n−1
1 Var(X1(t)) = n−1
1 X0et(et −1).
For a ﬁxed number of paths n and m, and a ﬁxed parameter h ∈[0, t], the
expected cost of the conditional Monte Carlo estimator is
CostCMC(n, m, h) = n E[X1i(t −h) −X0] + n · m E[X1i(t) −X1i(t −h)]
= nX0(et−h −1) + n · mX0(et −et−h).
The variance of the conditional Monte Carlo estimator is
Var

1
n
1
m
n
X
i=1
m
X
j=1
Xij(t)

=
1
n · m2 Var


m
X
j=1
Xij(t)

.
(B.1)
Using the generic result that for random variables X and Y on the same probability
space Var(X) = E[Var(X|Y )] + Var(E[X|Y ]), we have
Var


m
X
j=1
Xij(t)

= E

Var


m
X
j=1
X1j(t)
X11(t −h)




+ Var

E


m
X
j=1
X1j(t)
X11(t −h)




= m E[Var(X1j(t)|X11(t −h))] + Var(m E[X1j(t)|X11(t −h)])
= m E

X11(t −h)eh(eh −1)

+ m2Var
 X11(t −h)eh
= mX0et−heh(eh −1) + m2e2hX0et−h(et−h −1)
= mX0et(eh −1) + m2X0et(et −eh)


## Page 25


CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
25
Thus, dividing by n · m2 as in (B.1), the variance of the conditional Monte Carlo
estimator is
Var

1
n
1
m
n
X
i=1
m
X
j=1
Xij(t)

=
1
n · m

X0et(eh −1) + mX0et(et −eh)

.
For a ﬁxed n1, setting CostCMC(n, m, h) = CostMC(n1) yields
nX0(et−h −1) + n · mX0(et −et−h) = n1X0(et −1),
or
n =
n1(et −1)
(et−h −1) + m(et −et−h).
Thus, for a ﬁxed n1 and n chosen above the variance of the conditional Monte Carlo
estimator is
1
n1
· (et−h −1) + m(et −et−h)
m(et −1)

X0et(eh −1) + mX0et(et −eh)

.
This is minimized at the boundary with m = 1, giving exactly the same variance as the
regular Monte Carlo estimator. Thus, to summarize, for a given ﬁxed computational
cost the variance of the conditional Monte Carlo estimator must be larger than the
variance of the standard Monte Carlo estimator.
Acknowledgments. We are grateful for ﬁnancial support from the Army Re-
search Oﬃce through grant W911NF-18-1-0324 and the National Science Foundation
through grant DMS-2051498.
REFERENCES
[1] D. F. Anderson, A modiﬁed next reaction method for simulating chemical systems with time
dependent propensities and delays, The Journal of chemical physics, 127 (2007), p. 214107.
[2] D. F. Anderson, Incorporating postleap checks in tau-leaping, The Journal of chemical physics,
128 (2008), p. 054103.
[3] D. F. Anderson, D. Cappelletti, M. Koyama, and T. G. Kurtz, Non-explosivity of stochas-
tically modeled reaction networks that are complex balanced, Bull. Math. Biol., 80 (2018),
pp. 2561–2579.
[4] D. F. Anderson, G. Craciun, and T. G. Kurtz, Product-form stationary distributions for
deﬁciency zero chemical reaction networks, Bulletin of mathematical biology, 72 (2010),
pp. 1947–1970.
[5] D. F. Anderson, A. Ganguly, and T. G. Kurtz, Error analysis of tau-leap simulation
methods, Annals of Applied Probability, 21 (2011), pp. 2226 – 2262.
[6] D. F. Anderson and D. J. Higham, Multi-level Monte Carlo for continuous time Markov
chains, with applications in biochemical kinetics, SIAM: Multiscale Modeling and Simula-
tion, 10 (2012), pp. 146 – 179.
[7] D. F. Anderson, D. J. Higham, and Y. Sun, Complexity of multilevel Monte Carlo tau-
leaping, SIAM J. Numer. Anal., 52 (2014), pp. 3106–3127.
[8] D. F. Anderson, D. J. Higham, and Y. Sun, Computational complexity analysis for Monte
Carlo approximations of classically scaled population processes, SIAM Multiscale Model.
Simul., 16 (2018), pp. 1206–1226.
[9] D. F. Anderson and M. Koyama, Weak error analysis of numerical methods for stochastic
models of population processes, SIAM Multiscale Model. Simul., 10 (2012), pp. 1493–1524.
[10] D. F. Anderson and T. G. Kurtz, Error analysis of tau-leap simulation methods, Annals of
Applied Probability, 72 (2010), pp. 1947–1970.
[11] D. F. Anderson and T. G. Kurtz, Continuous time Markov chain models for chemical re-
action networks, chapter in Design and Analysis of Biomolecular Circuits: Engineering
Approaches to Systems and Synthetic Biology, H. Koeppl et al. (Editors), (2011).


## Page 26


26
D. F. ANDERSON K. W. EHLERT
[12] D. F. Anderson and T. G. Kurtz, Stochastic analysis of biochemical systems, Springer, 2015.
[13] D. F. Anderson, D. Schnoerr, and C. Yuan, Time-dependent product-form poisson distribu-
tions for reaction networks with higher order complexes, Journal of Mathematical Biology,
80 (2020), pp. 1919–1951.
[14] D. F. Anderson, T. Seppalainen, and B. Valko, Introduction to Probability, Cambridge
University Press, 2017.
[15] G. E. Box, Some theorems on quadratic forms applied in the study of analysis of variance
problems, i. eﬀect of inequality of variance in the one-way classiﬁcation, The annals of
mathematical statistics, (1954), pp. 290–302.
[16] H. Busch, W. Sandmann, and V. Wolf, A numerical aggregation algorithm for the enzyme-
catalyzed substrate conversion, in International Conference on Computational Methods in
Systems Biology, Springer, 2006, pp. 298–311.
[17] Y. Cao, D. T. Gillespie, and L. R. Petzold, Eﬃcient step size selection for the tau-leaping
simulation method, The Journal of chemical physics, 124 (2006), p. 044109.
[18] Y. Cao, D. T. Gillespie, and L. R. Petzold, Adaptive explicit-implicit tau-leaping method
with automatic tau selection, The Journal of chemical physics, 126 (2007), p. 224101.
[19] Y. Cao, A. Terebus, and J. Liang, Accurate chemical master equation solution using multi-
ﬁnite buﬀers, Multiscale Modeling & Simulation, 14 (2016), pp. 923–963.
[20] M. Conforti, G. Cornu´ejols, and G. Zambelli, Integer programming, Springer, 2014.
[21] F. Didier, T. A. Henzinger, M. Mateescu, and V. Wolf, Fast adaptive uniformization
of the chemical master equation, in 2009 International Workshop on High Performance
Computational Systems Biology, IEEE, 2009, pp. 118–127.
[22] K. Ehlert and L. Loewe, Lazy updating of hubs can enable more realistic models by speeding
up stochastic simulations, The Journal of chemical physics, 141 (2014), p. 11B617 1.
[23] S. Engblom, Spectral approximation of solutions to the chemical master equation, Journal of
computational and applied mathematics, 229 (2009), pp. 208–221.
[24] M. Feinberg, Lectures on chemical reaction networks. Delivered at the Mathematics Research
Center, Univ. Wisc.-Madison. Available for download at http://crnt.engineering.osu.edu/
LecturesOnReactionNetworks, 1979.
[25] M. A. Gibson and J. Bruck, Eﬃcient exact stochastic simulation of chemical systems
with many species and many channels, The journal of physical chemistry A, 104 (2000),
pp. 1876–1889.
[26] D. T. Gillespie, A general method for numerically simulating the stochastic time evolution of
coupled chemical reactions, Journal of computational physics, 22 (1976), pp. 403–434.
[27] D. T. Gillespie, Approximate accelerated stochastic simulation of chemically reacting systems,
The Journal of Chemical Physics, 115 (2001), pp. 1716–1733.
[28] D. T. Gillespie, A. Hellander, and L. R. Petzold, Perspective: Stochastic algorithms for
chemical kinetics, The Journal of chemical physics, 138 (2013), p. 05B201 1.
[29] P. Glasserman, Monte Carlo Methods in Financial Engineering, Springer-Verlag New York,
2003.
[30] E. L. Haseltine and J. B. Rawlings, Approximate simulation of coupled fast and slow
reactions for stochastic chemical kinetics, The Journal of chemical physics, 117 (2002),
pp. 6959–6969.
[31] M. Hegland, C. Burden, L. Santoso, S. MacNamara, and H. Booth, A solver for the
stochastic master equation applied to gene regulatory networks, Journal of computational
and applied mathematics, 205 (2007), pp. 708–724.
[32] T. A. Henzinger, M. Mateescu, and V. Wolf, Sliding window abstraction for inﬁnite
markov chains, in International Conference on Computer Aided Veriﬁcation, Springer,
2009, pp. 337–352.
[33] T. Jahnke and W. Huisinga, Solving the chemical master equation for monomolecular reac-
tion systems analytically, Journal of mathematical biology, 54 (2007), pp. 1–26.
[34] T. Jahnke and T. Udrescu, Solving chemical master equations by adaptive wavelet compres-
sion, Journal of Computational Physics, 229 (2010), pp. 5724–5741.
[35] G. Karlebach and R. Shamir, Modelling and analysis of gene regulatory networks, Nature
Reviews Molecular Cell Biology, 9 (2008), p. 770.
[36] V. Kazeev, M. Khammash, M. Nip, and C. Schwab, Direct solution of the chemical
master equation using quantized tensor trains, PLoS computational biology, 10 (2014),
p. e1003359.
[37] I. Kryven, S. R¨oblitz, and C. Sch¨utte, Solution of the chemical master equation by radial
basis functions approximation with interface tracking, BMC systems biology, 9 (2015),
p. 67.
[38] T. G. Kurtz, Representations of markov processes as multiparameter time changes, The An-


## Page 27


CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
27
nals of Probability, (1980), pp. 682–715.
[39] S. MacNamara, A. M. Bersani, K. Burrage, and R. B. Sidje, Stochastic chemical kinet-
ics and the total quasi-steady-state assumption: application to the stochastic simulation
algorithm and chemical master equation, The Journal of chemical physics, 129 (2008),
p. 09B605.
[40] S. MacNamara, K. Burrage, and R. B. Sidje, Multiscale modeling of chemical kinetics via
the master equation, Multiscale Modeling & Simulation, 6 (2008), pp. 1146–1168.
[41] S. Mauch and M. Stalzer, Eﬃcient formulations for exact stochastic simulation of chemical
systems, IEEE/ACM Transactions on Computational Biology and Bioinformatics (TCBB),
8 (2011), pp. 27–35.
[42] H. H. McAdams and A. Arkin, Stochastic mechanisms in gene expression, Proceedings of the
National Academy of Sciences, 94 (1997), pp. 814–819.
[43] J. M. McCollum, G. D. Peterson, C. D. Cox, M. L. Simpson, and N. F. Samatova,
The sorting direct method for stochastic simulation of biochemical systems with varying
reaction execution behavior, Computational biology and chemistry, 30 (2006), pp. 39–49.
[44] A. Moraes, R. Tempone, and P. Vilanova, Multilevel hybrid Chernoﬀtau-leap, BIT Nu-
merical Mathematics, 56 (2016), pp. 189–239.
[45] B. Munsky and M. Khammash, The ﬁnite state projection algorithm for the solution of the
chemical master equation, The Journal of chemical physics, 124 (2006), p. 044104.
[46] J. R. Norris, Markov Chains, Cambridge University Press, 1997.
[47] A. B. Owen, Monte carlo theory, methods and examples. http://statweb.stanford.edu/∼owen/
mc/, 2013.
[48] S. Peleˇs, B. Munsky, and M. Khammash, Reduction and solution of the chemical master
equation using time scale separation and ﬁnite state projection, The Journal of chemical
physics, 125 (2006), p. 204104.
[49] R. Ramaswamy, N. Gonz´alez-Segredo, and I. F. Sbalzarini, A new class of highly eﬃcient
exact stochastic simulation algorithms for chemical reaction networks, The Journal of
chemical physics, 130 (2009), p. 244104.
[50] C. V. Rao, D. M. Wolf, and A. P. Arkin, Control, exploitation and tolerance of intracellular
noise, Nature, 420 (2002), p. 231.
[51] M. Rathinam, L. R. Petzold, Y. Cao, and D. T. Gillespie, Stiﬀness in stochastic chemically
reacting systems: The implicit tau-leaping method, The Journal of Chemical Physics, 119
(2003), pp. 12784–12794.
[52] F. E. Satterthwaite, Synthesis of variance, Psychometrika, 6 (1941), pp. 309–316.
[53] R. B. Sidje and H. D. Vo, Solving the chemical master equation by a fast adaptive ﬁnite
state projection based on the stochastic simulation algorithm, Mathematical biosciences,
269 (2015), pp. 10–16.
[54] A. Slepoy, A. P. Thompson, and S. J. Plimpton, A constant-time kinetic monte carlo
algorithm for simulation of large biochemical reaction networks, The journal of chemical
physics, 128 (2008), p. 05B618.
[55] M. Thattai and A. van Oudenaarden, Intrinsic noise in gene regulatory networks, Proceed-
ings of the National Academy of Sciences, 98 (2001), pp. 8614–8619.
[56] H. D. Vo and R. B. Sidje, Improved krylov-fsp method for solving the chemical master equa-
tion, in Proceedings of the World Congress on Engineering and Computer Science, vol. 2,
2016.
[57] H. D. Vo and R. B. Sidje, An adaptive solution to the chemical master equation using tensors,
The Journal of chemical physics, 147 (2017), p. 044102.
[58] D. J. Wilkinson, Stochastic modelling for systems biology, Chapman and Hall/CRC, 2006.
[59] V. Wolf, R. Goel, M. Mateescu, and T. A. Henzinger, Solving the chemical master equa-
tion using sliding windows, BMC systems biology, 4 (2010), p. 42.


## Page 28


arXiv:1906.05353v2  [math.NA]  4 Jan 2022
SUPPLEMENTARY MATERIALS: CONDITIONAL MONTE CARLO
FOR REACTION NETWORKS
DAVID F. ANDERSON∗AND KURT W. EHLERT†
SM1. Objective function ﬁgures. This section contains ﬁgures related to the
objective function of the optimization problem (3.10).
Fig. SM1. The surfaces are the approximate objective functions ˆf(m, h) for the diﬀerent ex-
ample models. The red dots show where the minimums are achieved, and the pair of numbers in
each title are the coordinates of the minimum in m and h space. The approximate objective function
utilized the approximation ˆp2 = 0. For ˜
N, we took all possible linear combinations of the nullspace
basis vectors with coeﬃcient over {−4, . . . , 4}. We used 103 samples to estimate the parameters
in the objective function. We used MATLAB’s fminsearch function (a derivative-free optimizer) to
ﬁnd a minimizer of ˆf(m, h).
∗Department of Mathematics, University of Wisconsin-Madison (anderson@math.wisc.edu)
†Department of Mathematics, University of Wisconsin-Madison (kehlert@math.wisc.edu)
SM1


## Page 29


SM2
D. F. ANDERSON K. W. EHLERT
0.01
0.0174
0.0304
0.0531
0.0927
0.1618
0.2823
0.4926
0.8596
1.5
h
1
2
3
5
8
13
22
36
60
100
m
Empirical error improvement
0.98
1.38
1.62
1.85
2.00
2.05
1.96
1.67
1.46
1.17
0.93
1.49
1.84
2.17
2.18
2.02
1.65
1.17
0.96
1.60
1.98
2.12
1.58
1.12
0.99
1.60
2.05
1.88
1.41
1.01
1.00
1.59
2.05
2.20
1.79
1.19
0.81
0.95
1.55
1.94
2.24
1.86
1.47
1.05
0.62
0.97
1.45
1.69
1.87
1.93
1.96
1.52
1.13
0.86
0.54
0.95
1.30
1.44
1.50
1.51
1.43
1.22
0.95
0.77
0.55
0.97
1.17
1.21
1.23
1.22
1.18
1.05
0.91
0.75
0.54
0.97
1.01
1.06
1.04
1.03
1.05
0.97
0.93
0.84
0.75
2.40
2.41
2.44
2.57
2.58
2.59
2.55
2.75
2.86
2.36
2.43
2.72
2.56
2.33
2.38
0.01
0.0174
0.0304
0.0531
0.0927
0.1618
0.2823
0.4926
0.8596
1.5
h
1
2
3
5
8
13
22
36
60
100
m
Scaled reciprocal of the objective function
1.00
1.39
1.58
1.76
1.86
1.89
1.82
1.68
1.46
1.19
1.00
1.53
1.84
1.97
1.59
1.19
1.00
1.61
1.99
2.03
1.55
1.10
1.00
1.65
2.06
1.86
1.35
0.91
1.00
1.63
2.03
2.06
1.57
1.10
0.73
1.00
1.57
1.91
2.07
1.68
1.26
0.87
0.57
1.00
1.46
1.69
1.85
1.82
1.63
1.30
0.97
0.67
0.44
1.00
1.31
1.43
1.47
1.40
1.23
0.99
0.74
0.52
0.35
1.00
1.15
1.18
1.16
1.08
0.94
0.76
0.58
0.41
0.28
1.00
1.01
0.99
0.94
0.86
0.75
0.61
0.47
0.34
0.23
2.16
2.34
2.38
2.24
2.41
2.64
2.66
2.43
2.52
2.75
2.70
2.35
2.44
2.60
2.47
2.20
2.26
Fig. SM2. Birth model. The ﬁrst heatmap shows MISEMC/MISECMC(m, h) for diﬀerent values
of m and h. The method we used to obtain the ratio is described in section 4. The second heatmap
shows that value of ˆf(1, 0)/ ˆf(m, h). The deﬁnition of ˆf is in (3.9)


## Page 30


SUPPLEMENTARY MATERIALS: CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
SM3
0.01
0.0174
0.0304
0.0531
0.0927
0.1618
0.2823
0.4926
0.8596
1.5
h
1
2
3
5
8
13
22
36
60
100
m
Empirical error improvement
1.03
1.58
1.93
2.29
2.65
2.91
3.23
2.91
2.80
2.64
1.07
1.72
2.20
3.03
3.72
3.84
4.25
3.82
3.68
2.94
1.05
1.79
2.35
3.12
3.95
4.35
4.09
3.48
1.11
1.89
2.45
3.56
4.37
4.31
3.21
1.04
1.81
2.61
3.60
4.28
3.60
2.97
1.06
1.87
2.55
3.48
4.32
4.49
3.50
2.56
1.06
1.90
2.52
3.14
3.91
4.29
4.57
4.15
3.33
2.43
1.05
1.67
2.08
2.58
3.02
3.23
3.24
3.00
2.63
2.14
1.05
1.47
1.76
2.08
2.30
2.22
2.18
2.09
2.09
1.88
1.07
1.16
1.31
1.33
1.44
1.37
1.36
1.41
1.44
1.35
4.78
4.72
5.05
5.25
4.99
5.69
5.46
5.92
4.77
5.02
0.01
0.0174
0.0304
0.0531
0.0927
0.1618
0.2823
0.4926
0.8596
1.5
h
1
2
3
5
8
13
22
36
60
100
m
Scaled reciprocal of the objective function
1.00
1.25
1.36
1.45
1.50
1.52
1.51
1.46
1.37
1.23
1.00
1.48
1.76
2.05
2.24
2.34
2.34
2.22
2.00
1.69
1.00
1.61
2.02
2.50
2.84
2.81
2.41
1.92
1.00
1.70
2.20
2.85
2.56
1.91
1.00
1.74
2.29
2.41
1.71
1.00
1.74
2.28
2.78
2.08
1.45
1.00
1.69
2.16
2.72
2.78
2.25
1.66
1.13
1.00
1.58
1.93
2.28
2.45
2.39
2.12
1.69
1.24
0.86
1.00
1.40
1.59
1.74
1.77
1.67
1.46
1.18
0.91
0.63
1.00
1.14
1.18
1.19
1.16
1.08
0.93
0.78
0.60
0.46
3.04
3.03
3.35
3.62
3.55
3.17
3.01
3.56
3.82
3.65
3.13
2.97
3.47
3.64
3.36
3.06
3.11
Fig. SM3. Birth-death model. The ﬁrst heatmap shows MISEMC/MISECMC(m, h) for diﬀerent
values of m and h. The method we used to obtain the ratio is described in section 4. The second
heatmap shows that value of ˆf(1, 0)/ ˆf(m, h). The deﬁnition of ˆf is in (3.9).


## Page 31


SM4
D. F. ANDERSON K. W. EHLERT
0.05
0.067
0.0897
0.1202
0.1611
0.2158
0.2891
0.3873
0.5189
0.6951
0.9313
1.2476
1.6715
2.2393
3
h
10
17
27
44
72
118
194
317
518
849
1390
2276
3728
6106
10000
m
Empirical error improvement
3.95
4.55
4.89
5.11
5.32
5.37
5.06
4.96
4.77
4.04
3.40
2.68
2.00
1.39
0.95
4.36
5.31
5.90
6.56
6.58
6.58
6.39
6.00
5.38
4.76
3.79
2.96
2.13
1.44
0.98
5.20
6.41
7.21
7.55
8.17
8.10
7.75
7.45
6.60
5.24
4.17
3.11
2.17
1.45
0.95
5.67
7.23
8.50
9.36
9.90
9.62
9.00
8.67
7.43
5.94
4.34
3.18
2.19
1.46
0.93
6.21
8.19
9.65
11.43
11.64
11.39
11.09
9.92
7.94
6.70
4.76
3.17
2.25
1.40
0.91
6.75
9.28
10.94
13.30
13.78
13.23
12.99
10.94
9.50
6.76
4.92
3.29
2.21
1.40
0.93
7.06
10.20
12.38
14.31
16.05
16.42
14.40
12.71
10.35
7.24
4.95
3.46
2.21
1.36
0.86
7.72
11.05
13.67
16.35
16.03
14.54
10.32
7.50
4.80
3.20
2.05
1.49
0.81
7.80
11.29
14.56
15.44
14.69
10.46
6.80
5.22
3.06
2.07
1.31
0.79
8.12
11.77
15.39
14.54
10.64
6.83
4.43
3.10
2.07
1.18
0.68
8.01
12.25
15.86
14.75
10.78
7.10
4.78
2.96
2.03
1.27
0.74
8.03
11.55
15.25
14.99
10.05
6.90
4.54
2.85
1.74
1.19
0.63
8.04
11.73
14.76
13.27
10.18
6.54
4.96
2.89
1.83
1.10
0.62
7.85
11.07
13.91
16.91
15.04
12.32
8.05
5.71
3.77
3.03
1.91
1.07
0.67
7.46
10.51
13.28
15.60
16.76
16.76
14.08
10.91
8.55
5.79
3.47
2.40
1.44
1.06
0.60
17.73
18.59
17.78
18.88
20.24
18.68
20.24
20.09
17.30
19.84
22.89
22.15
18.04
18.78
21.57
19.66
17.55
17.68
20.22
19.12
17.16
18.42
17.91
0.05
0.067
0.0897
0.1202
0.1611
0.2158
0.2891
0.3873
0.5189
0.6951
0.9313
1.2476
1.6715
2.2393
3
h
10
17
27
44
72
118
194
317
518
849
1390
2276
3728
6106
10000
m
Scaled reciprocal of the objective function
2.74
2.97
3.14
3.17
3.27
3.16
3.11
2.95
2.72
2.43
2.01
1.57
1.19
0.82
0.56
3.23
3.61
3.83
3.95
4.07
3.98
3.77
3.55
3.19
2.75
2.20
1.70
1.22
0.83
0.55
3.76
4.27
4.66
4.77
4.81
4.76
4.50
4.24
3.68
3.03
2.40
1.79
1.23
0.83
0.53
4.28
5.04
5.42
5.76
5.83
5.71
5.40
4.79
4.21
3.33
2.49
1.77
1.22
0.79
0.52
4.70
5.64
6.25
6.58
6.81
6.58
6.17
5.39
4.47
3.43
2.48
1.72
1.16
0.76
0.47
5.09
6.15
6.96
7.51
7.44
7.33
6.67
5.64
4.57
3.47
2.55
1.70
1.11
0.70
0.44
5.08
6.29
6.94
7.55
7.57
7.19
6.59
5.67
4.61
3.54
2.47
1.69
1.10
0.72
0.45
5.09
6.21
6.96
7.38
7.51
7.43
6.66
5.69
4.60
3.44
2.48
1.70
1.11
0.71
0.44
6.01
7.62
7.60
6.07
4.51
3.23
2.13
1.39
0.87
0.55
0.34
6.38
7.64
5.81
4.20
2.90
1.87
1.20
0.76
0.47
0.29
6.57
7.58
5.73
3.94
2.59
1.69
1.10
0.68
0.42
0.26
6.77
6.87
5.27
3.55
2.28
1.48
0.92
0.58
0.35
0.22
6.85
6.61
4.68
3.17
2.11
1.34
0.87
0.51
0.31
0.20
6.81
8.12
6.12
4.28
2.82
1.89
1.16
0.70
0.46
0.28
0.17
6.56
7.48
5.49
3.97
2.54
1.60
1.06
0.66
0.41
0.26
0.16
8.71
9.50
9.45
8.79
8.27
9.72
10.54
10.21
9.27
8.74
10.14
10.76
10.48
9.62
8.96
10.51
11.17
11.01
9.44
9.10
10.50
10.99
10.20
8.58
8.87
10.21
10.58
10.01
8.61
9.72
9.79
9.00
Fig. SM4. Gene toggle model. The ﬁrst heatmap shows MISEMC/MISECMC(m, h) for diﬀerent
values of m and h. The method we used to obtain the ratio is described in section 4. The second
heatmap shows that value of ˆf(1, 0)/ ˆf(m, h). The deﬁnition of ˆf is in (3.9).


## Page 32


SUPPLEMENTARY MATERIALS: CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
SM5
0.01
0.0146
0.0213
0.0311
0.0454
0.0663
0.0969
0.1414
0.2065
0.3015
0.4401
0.6426
0.9382
1.3698
2
h
1
2
3
5
8
12
20
32
52
85
139
228
373
611
1000
m
Empirical error improvement
1.00
1.83
2.60
3.81
5.07
6.45
7.91
9.33
10.04
10.76
10.47
10.50
9.81
8.55
6.85
1.00
1.84
2.66
3.92
5.47
7.10
8.93
10.33
11.54
12.06
12.50
11.78
10.89
9.15
7.42
1.01
1.90
2.71
4.10
5.78
7.59
9.69
11.62
12.99
14.16
13.93
12.94
11.16
9.58
7.23
0.99
1.91
2.80
4.29
6.04
8.06
10.80
13.31
14.30
12.07
9.71
7.36
1.01
1.94
2.76
4.34
6.36
8.52
11.43
14.12
14.57
12.17
9.51
6.54
1.00
1.94
2.79
4.46
6.60
8.83
12.07
14.91
12.36
9.39
6.05
1.00
1.94
2.82
4.50
6.68
8.94
12.60
14.94
11.53
8.52
5.56
1.00
1.93
2.80
4.52
6.71
9.21
12.89
14.66
10.14
7.64
5.23
0.99
1.93
2.86
4.48
6.59
9.07
12.31
13.72
10.74
6.95
4.59
1.00
1.90
2.78
4.36
6.38
8.63
11.86
14.60
14.76
12.03
9.06
6.22
4.23
1.00
1.92
2.75
4.32
6.07
8.02
10.61
12.61
14.11
13.94
12.13
9.65
7.75
5.64
3.53
1.00
1.89
2.69
4.09
5.63
7.28
9.31
10.84
11.73
11.37
9.94
8.65
6.01
4.41
3.11
0.99
1.84
2.57
3.80
5.13
6.32
7.62
8.58
8.83
8.62
7.82
6.94
5.37
4.17
2.82
0.99
1.76
2.46
3.45
4.45
5.24
6.13
6.75
6.87
6.69
6.02
5.40
4.21
3.46
2.20
1.01
1.72
2.22
3.03
3.66
4.24
4.69
4.90
5.06
4.98
4.47
4.02
3.56
2.53
2.02
15.15
16.01
15.87
16.58
17.69
16.94
17.25
19.14
17.96
15.20
15.67
18.22
20.16
17.67
16.28
19.04
18.04
18.09
15.68
17.91
18.14
16.83
15.98
15.69
0.01
0.0146
0.0213
0.0311
0.0454
0.0663
0.0969
0.1414
0.2065
0.3015
0.4401
0.6426
0.9382
1.3698
2
h
1
2
3
5
8
12
20
32
52
85
139
228
373
611
1000
m
Scaled reciprocal of the objective function
1.00
1.84
2.56
3.73
5.00
6.17
7.58
8.65
9.44
9.89
9.94
9.62
8.94
7.92
6.62
1.00
1.88
2.65
3.96
5.47
6.94
8.79
10.31
11.45
12.13
12.14
11.61
10.50
9.00
7.22
1.00
1.90
2.72
4.13
5.84
7.57
9.92
11.84
13.39
14.30
14.28
13.48
11.95
9.81
7.61
1.00
1.90
2.72
4.13
5.84
7.57
9.88
11.88
13.41
14.46
14.28
13.58
11.87
9.81
7.66
1.00
1.94
2.83
4.44
6.53
8.84
12.25
15.51
18.28
19.92
19.77
17.93
14.88
11.53
8.27
1.00
1.96
2.87
4.57
6.84
9.42
13.47
17.48
17.18
12.49
8.75
1.00
1.96
2.88
4.62
6.99
9.72
14.14
18.60
18.03
13.27
9.19
1.00
1.97
2.90
4.66
7.07
9.90
14.51
19.48
19.21
14.13
10.03
1.00
1.96
2.88
4.63
6.98
9.77
14.10
18.67
19.16
14.86
9.87
1.00
1.95
2.85
4.52
6.75
9.28
13.15
17.03
17.65
16.03
11.60
1.00
1.93
2.80
4.37
6.37
8.53
11.64
14.59
17.51
18.83
18.74
17.86
15.34
12.98
10.84
1.00
1.91
2.72
4.15
5.89
7.64
10.03
11.99
13.67
14.69
15.41
14.29
12.83
10.18
8.12
1.00
1.87
2.62
3.87
5.28
6.62
8.29
9.55
10.77
11.27
11.60
10.65
10.14
8.47
7.85
1.00
1.81
2.46
3.48
4.53
5.44
6.48
7.20
7.70
8.05
7.98
7.81
7.57
6.66
5.73
1.00
1.72
2.26
3.03
3.74
4.29
4.87
5.27
5.52
5.67
5.67
5.53
5.45
5.15
4.98
21.22
23.36
23.12
20.64
22.88
25.37
25.32
22.35
24.08
27.17
27.06
23.95
23.08
26.24
26.03
23.43
20.42
22.67
23.03
20.86
Fig. SM5. Fast/slow model. The ﬁrst heatmap shows MISEMC/MISECMC(m, h) for diﬀerent
values of m and h. The method we used to obtain the ratio is described in section 4. The second
heatmap shows that value of ˆf(1, 0)/ ˆf(m, h). The deﬁnition of ˆf is in (3.9).


## Page 33


SM6
D. F. ANDERSON K. W. EHLERT
SM2. Central limit theorem ﬁgures. This section contains ﬁgures related to
the central limit theorem (Theorem 5.1). The dashed blue density is the empirical
density of the integrated squared error (5.1), and the solid red density is the Satter-
waithe approximation to the asymptotic density (5.4). On the x-axis there is a blue
cross and red circle. The blue cross is the 95% sample quantile, and the red circle
is the 95% quantile of the red density. To generate the blue curve, we sampled 104
values of nm2 P
x∈˜
S
 ˆpt(x; n, m, h)−pt(x)
2 for diﬀerent values of n, and then we gave
those values to MATLAB’s ksdensity function. The traces of Σ and Σ2 were based an
independent set of 105 simulations. Since the densities and quantiles agree, the red
density and its corresponding 95% quantile are a good approximation. Therefore we
can use them to provide conﬁdence intervals for the integrated squared error.
0
20
40
60
80
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
32.10
32.06
0
20
40
60
80
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
32.57
32.06
0
20
40
60
80
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
32.75
32.06
0
20
40
60
80
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
32.70
32.06
Fig. SM6. Birth model.


## Page 34


SUPPLEMENTARY MATERIALS: CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
SM7
0
50
100
150
200
0
0.005
0.01
0.015
0.02
0.025
0.03
0.035
0.04
55.06
54.87
0
50
100
150
200
0
0.005
0.01
0.015
0.02
0.025
0.03
0.035
0.04
55.71
54.87
0
50
100
150
200
0
0.005
0.01
0.015
0.02
0.025
0.03
0.035
0.04
55.49
54.87
0
50
100
150
200
0
0.005
0.01
0.015
0.02
0.025
0.03
0.035
0.04
56.13
54.87
Fig. SM7. Birth-death model.


## Page 35


SM8
D. F. ANDERSON K. W. EHLERT
0
2000
4000
6000
8000
10000
0
1
2
3
4
5
6
10-4
3729.99
3759.15
0
2000
4000
6000
8000
10000
0
1
2
3
4
5
6
10-4
3805.83
3759.15
0
2000
4000
6000
8000
10000
0
1
2
3
4
5
6
10-4
3796.37
3759.15
0
2000
4000
6000
8000
10000
0
1
2
3
4
5
6
10-4
3774.02
3759.15
Fig. SM8. Toggle model.


## Page 36


SUPPLEMENTARY MATERIALS: CONDITIONAL MONTE CARLO FOR REACTION NETWORKS
SM9
0
500
1000
1500
2000
2500
0
0.5
1
1.5
2
2.5
10-3
1006.11
1005.02
0
500
1000
1500
2000
2500
0
0.5
1
1.5
2
2.5
10-3
1024.05
1005.02
0
500
1000
1500
2000
2500
0
0.5
1
1.5
2
2.5
10-3
1013.03
1005.02
0
500
1000
1500
2000
2500
0
0.5
1
1.5
2
2.5
10-3
1025.47
1005.02
Fig. SM9. Fast/slow model.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1906_05353v2_conditional_monte_carlo_for_reaction_networks
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1906_05353V2_CONDITIONAL_MONTE_CARLO_FOR_REACTION_NETWORKS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

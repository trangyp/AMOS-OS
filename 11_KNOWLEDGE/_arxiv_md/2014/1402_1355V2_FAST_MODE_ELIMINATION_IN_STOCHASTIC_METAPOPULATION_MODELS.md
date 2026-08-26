---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1402.1355v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1402.1355v2_Fast-mode_elimination_in_stochastic_metapopulation_models

> Source: 1402.1355v2_Fast-mode_elimination_in_stochastic_metapopulation_models.pdf

> Pages: 14

---


## Page 1


Fast-mode elimination in stochastic metapopulation models
George W. A. Constable and Alan J. McKane
Theoretical Physics Division, School of Physics and Astronomy,
The University of Manchester, Manchester M13 9PL, United Kingdom
We investigate the stochastic dynamics of entities which are conﬁned to a set of islands, between
which they migrate. They are assumed to be one of two types, and in addition to migration, they also
reproduce and die. Birth and death events are later moderated by weak selection. Systems which
fall into this class are common in biology and social science, occurring in ecology, population genet-
ics, epidemiology, biochemistry, linguistics, opinion dynamics, and other areas. In all these cases the
governing equations are intractable, consisting as they do of multidimensional Fokker-Planck equa-
tions or, equivalently, coupled nonlinear stochastic diﬀerential equations with multiplicative noise.
We develop a methodology which exploits a separation in time scales between fast and slow vari-
ables to reduce these equations so that they resemble those for a single island, which are amenable
to analysis. The technique is generally applicable, but we choose to discuss it in the context of
population genetics, in part because of the extra features that appear due to selection. The idea
behind the method is simple, its application systematic, and the results in very good agreement
with simulations of the full model for a range of parameter values.
PACS numbers: 05.40.-a, 02.50.Ey, 87.10.Mn
I.
INTRODUCTION
Physicists now routinely apply the ideas and tech-
niques of non-equilibrium statistical mechanics to areas
outside of their own discipline. In the biological sciences,
social sciences and in economics there are many instances
of the interaction of the basic constituents of the systems
giving rise to structures at the mesoscale or macroscale
which can be studied and understood using the method-
ology of statistical physics [1–3].
There are some cru-
cial diﬀerences, however. In physics, atoms, molecules or
spins frequently lie on regular grids or lattices and have
an interaction strength depending on the distance be-
tween them. By contrast, conventional spatial modelling
of this type will typically not be appropriate in a biolog-
ical or social context. In these disciplines the interaction
between individuals is more likely to be speciﬁed by a
network, with links being of varying strengths or absent
altogether [4, 5]. An alternative structure which is per-
haps even more common is the situation where the nodes
of the network are not individuals, but a population of
individuals. The interaction is then between one popu-
lation and another population connected to it by a link.
The whole system is then a ‘population of populations’
or metapopulation [6].
Metapopulations occur when modelling a wide variety
of phenomena. In ecology, they may consist of disjoint
pieces of vegetation able to support insects or animals,
which are able to move from one area of vegetation to
another [7]. In population genetics, they may be islands
or ‘demes’ of individuals with one of two diﬀerent alleles
of a particular gene, which are able to migrate from one
deme to another [8]. In epidemiology, they may be cities
with people who are infected or susceptible to a disease
moving from one city to another [9]. In reaction kinetics,
they may be compartments in which chemical reactions
take place [10]. In linguistics the nodes may be people,
who have two diﬀerent linguemes — two diﬀerent ways
of saying the same thing — which they exchange with
other people through conversation at a frequency given
by the strength of the link [11]. Similarly, in opinion dy-
namics, people may hold tokens which represent two dif-
ferent opinions, which may be exchanged with others [3].
The common mathematical structure in all these cases
is a set of D ‘islands’ which we will label by an index
i = 1, . . . , D. Island i will contain a ﬁxed number of indi-
viduals Ni, which undergo the processes of birth, death
and migration from one island to another, in addition to
perhaps other processes depending on the application.
A systematic analytic approach to investigating sys-
tems such as these begins at the microscale, that is, with
the fundamental constituents of the system.
It is as-
sumed that the basic processes of birth, death, migra-
tion, etc. can be described by a continuous time Markov
process.
The dynamics is then governed by a master
equation [12], which, for any case of interest, will be in-
tractable. It can be made less so by using a diﬀusion ap-
proximation in which the variables describing the state
of the system are no longer the (discrete) number of indi-
viduals of a given type on island i, but the (continuous)
fraction of that type of individual on island i. This ap-
proximation, valid for large Ni, turns the master equa-
tion into a Fokker-Planck equation (FPE) [13]. Although
somewhat more tractable than the master equation, the
FPE is still a partial diﬀerential equation in many vari-
ables, with a diﬀusion term which is state-dependent. It
is equivalent to a set of stochastic diﬀerential equations
(SDEs) with multiplicative noise [14], which is equally
diﬃcult to analyze.
There is a way forward in the analysis of equations
such as these, providing that a set of ‘fast’ modes can
be identiﬁed, and eliminated systematically. This pro-
cedure, if it can be carried out, leaves a simpler set of
equations which hopefully are amenable to analysis. We
arXiv:1402.1355v2  [cond-mat.stat-mech]  1 Apr 2014


## Page 2


2
have recently described such a method, which was ap-
plied directly to a set of SDEs [15], although there is a
long history of techniques based on the same idea being
applied to deterministic equations or to FPEs (for refer-
ences see [15]).
In this paper we show that a variant of the procedure
described in [15], is in many instances ideally suited to
reduce the population genetics of D demes to those of
a single deme, with an eﬀective population size and new
eﬀective parameters. This will be true even with variable
deme size (Ni ̸= Nj), as long as the sizes are of the same
order, and also if selection is present. The technique is
simple to understand and systematic — eﬀectively an al-
gorithm — with ﬁnal expressions that are given as formu-
las involving, for example, eigenvalues and eigenvectors
of matrices deﬁned by the network. While there has been
work constructing reduced models of similar systems to
the one we discuss here [16, 17], both the models and
the techniques employed to reduce them, are less general
than those we present. We also mention two approaches
to the study of diﬀerent systems which use some of the
same ideas that we utilize [18, 19].
The outline of the paper is as follows. In Section II we
deﬁne the microscopic model for a set of D demes each
containing individuals with two diﬀerent alleles, and con-
nected in a general network, and give the form of the cor-
responding SDEs. Initially the model is introduced for
the selectively neutral case, in which neither of the alle-
les has an advantage over the other. The model is then
naturally extended to the case where a selective bias ex-
ists. The details of the reduction method, whereby the D
SDEs are reduced to a single SDE, are given in Section
III, along with formulas for the parameters appearing in
the reduced equations.
For clarity the method is pre-
sented in two broad regimes; the selectively neutral case,
Section III A, and the case with selective bias, section
III B. In Section IV we compare the probability of ﬁxa-
tion of one of the alleles and the mean time to ﬁxation
calculated from the reduced SDEs with the results from
simulating the original microscopic model for a range of
parameters. The agreement is found to be very good. In
Section V, we conduct an investigation into the range of
validity of the method. We ﬁnd it continues to provide
good predictions across a larger parameter range than
one might na¨ıvely expect. In Section VI we conclude and
describe possible future avenues of investigation. A tech-
nical appendix gives details of the derivation of analytic
results used in the main text.
II.
MODEL
As outlined in the Introduction, the system consists of
a set of D islands or demes. On each of these demes is a
ﬁxed population of well-mixed individuals. The popula-
tion can vary from deme to deme such that the popula-
tion on the ith deme is denoted by the integer Ni = βiN,
where βi is of order one and acts to moderate some typ-
ical deme size N. We assume that on each island there
exist two types of haploid (single allele) organisms, carry-
ing alleles A and B respectively. The number of A alleles
on the ith island is denoted ni. Since the population of
each island is ﬁxed this leaves βiN −ni organisms carry-
ing allele B. Having described the initial set-up we can
proceed to consider the dynamical behaviour.
The key aspect of the dynamics comes from the ﬁnite
size of the population.
Only in this case is there ge-
netic drift, which is a consequence of the demographic
stochasticity, or noise, generated from the ﬁnite and dis-
crete nature of the population. In order to correctly and
consistently include demographic stochasticity, it is nec-
essary to begin from an individual based model (IBM).
Rather than arrive at an equation which describes the
deﬁnite state of the system at some time (a deterministic
description), we require an equation which describes the
probability that the system occupies any of the possible
states at each time. To do this we ﬁrst need to deﬁne
the states of the system, which we assume are given by a
vector of non-negative integers, n, which in our case has
as the ith entry the number of individuals with allele A
on island i. We then need to specify a set of probabil-
ity transition rates, T(n′|n). These give the probability
per unit time that the system transitions from its current
state, given by the vector n, to a new state, n′. Assum-
ing that these transition rates only depend on the current
state of the system, and not on its past history, the sta-
tistical time evolution of the system is then completely
described by the master equation [12]
dp(n, t)
dt
=
X
n′̸=n
[T(n|n′)p(n′, t) −T(n′|n)p(n, t)] .
(1)
The choice of the transition rates T(n′|n) fully deﬁne
the dynamics. To construct these, we start by choosing
an island, j, on which a reproduction event should take
place based on a probability fj such that PD
j=1 fj = 1. If
the per capita birth rate on each island is equal, then fj
will simply be proportional to the number of individuals
on island j, so that we have fj = βj/ PD
k=1 βk. Once an
island has been chosen, an organism on the island must
be picked to reproduce.
If alleles A and B are selec-
tively neutral this probability will be entirely dependent
on the local allele frequencies. Once an allele is picked
to reproduce, the oﬀspring must displace a pre-existing
individual in one of the demes to keep the population of
the demes ﬁxed. The deme it chooses to migrate to is
dependent on the migration matrix mij, the probability
an oﬀspring with progenitor in deme j will migrate to
deme i, normalized such that PD
i mij = 1. The proba-
bility of oﬀspring not migrating can then be alternatively
written mii = 1 −PD
j̸=i mji. Finally, the type of organ-
ism it replaces is proportional to the allele frequencies in
the destination deme, i. This is essentially the Moran
model [20, 21], with migration, depicted in Fig. 1. A
simple consideration of the combinatorics of this process


## Page 3


3
mij
fj µ Βj
FIG. 1. (Color online) A simple depiction of the model: a
set of D islands, each containing two types of individual, is
connected by links whose strength is given by a product of
the birth rates, fj, and the migration probabilities mij.
leads to the transition rates,
T(ni + 1|ni) =
D
X
j=1
(fj)
 nj
βjN

(mij)
 βiN −ni
βiN −δij

,
T(ni −1|ni) =
D
X
j=1
(fj)
βjN −nj
βjN

(mij)

ni
βiN −δij

,
(2)
where the dependence of the probability transition rates,
T(n′|n), on elements of n that do no change in the tran-
sition has been suppressed. With all island sizes equal
(βi = 1 ∀i), this reduces to the migration model ﬁrst dis-
cussed using this formalism in [22]. Since the only tran-
sitions are those where n′
i = ni ± 1, the master equation
(1) takes the much simpler form
dp(n, t)
dt
=
D
X
i=1
[T(ni|ni −1)p(ni −1, t)
−T(ni + 1|ni)p(ni, t)]
+
D
X
i=1
[T(ni|ni + 1)p(ni + 1, t)
−T(ni −1|ni)p(ni, t)] .
(3)
The situation becomes only slightly more complicated
if a selective bias for one of the alleles exists. In this case,
when picking which allele will reproduce, we must weight
the local deme frequencies by the relative ﬁtness of each
allele. For simplicity, we consider here the case of fre-
quency independent selection and weight the probability
of selecting an A allele on island j by 1 + sαj and the B
allele by 1. Here s indicates the typical strength of selec-
tion, while αj is a parameter that allows us to moderate
this selection strength from island to island. The param-
eter αj is positive if allele A is advantageous in deme j,
or negative if it is deleterious. The probability of picking
A and B conditional on island j ﬁrst being chosen for
reproduction are then respectively
(1 + sαj)nj
(1 + sαj)nj + (βjN −nj) and
βjN −nj
(1 + sαj)nj + (βjN −nj).
Typically, the parameter s will be small in biological sit-
uations, which allows us to Taylor expand in s to arrive
at the set of transition rates
T(ni + 1|ni) =
D
X
j=1
(fj)
 βiN −ni
βiN −δij

(mij) ×
 nj
βjN
+sαj
nj(βjN −nj)
(βjN)2
−s2α2
j
n2
j(βjN −nj)
(βjN)3
+ O(s3)
!
,
(4)
and
T(ni −1|ni) =
D
X
j=1
(fj)

ni
βiN −δij

(mij) ×
 
1 −nj
βjN
−sαj
nj(βjN −nj)
(βjN)2
+ s2α2
j
n2
j(βjN −nj)
(βjN)3
+ O(s3)
!
,
(5)
for the generalized model with selection. We note that
by setting s = 0, we once again obtain the neutral model
described by Eq. (2).
While the master equations in both these cases are in-
tractable, there exist a range of standard approximation
techniques which can be used to simplify it. Historically,
the one which has been used most extensively in pop-
ulation genetics is the diﬀusion approximation [23, 24]
in which the variables xi = ni/βiN are introduced, and
assumed to be continuous. This is clearly a large N ap-
proximation, which allows the master equation to be Tay-
lor expanded in N −1, and then truncated at second or-
der to obtain a generalized diﬀusion, or Fokker-Planck,
equation.
More systematically, we are starting from a
Kramers-Moyal expansion [14, 25], and then using the
master equation to calculate the jump-moments, showing
that the third and higher moments are down by powers
of N −1 [13]. This will be described in more detail else-
where for the speciﬁc model we are considering in this
paper [26].
The FPE for the case of the transitions rates given by
Eqs. (4) and (5) is
∂p(x, t)
∂t
= −1
N
D
X
i=1
∂
∂xi
[Ai(x)p(x, t)]
+
1
2N 2
D
X
i=1
∂2
∂x2
i
[Bii(x)p(x, t)] ,
(6)


## Page 4


4
where the drift terms Ai(x) and the diﬀusion terms
Bii(x) are given below. A quantity which naturally ap-
pears in both Ai(x) and B(x) is G, a generalized migra-
tion rate matrix, which is the product of the birth rate,
fj, and the migration probability, mij:
Gij = mijfj,
where
D
X
i,j=1
Gij = 1;
(7)
the normalization of G being inherited from the normal-
ization of m and f. For the neutral case the drift vector
is found to be
Ai(x) = 1
βi

−xi
D
X
j̸=i
Gij +
D
X
j̸=i
Gijxj

,
(8)
and the diﬀusion matrix is found to be diagonal, with
elements
Bii(x) = 1
β2
i

xi
D
X
j=1
Gij +
D
X
j=1
Gijxj
−2xi
D
X
j=1
Gijxj

.
(9)
In order to highlight the linearity of Ai(x), it may be
alternatively expressed as
Ai(x) =
D
X
j=1
Hijxj,
(10)
where the matrix H is deﬁned by
Hij = Gij
βi
i ̸= j,
Hii = −
D
X
j̸=i
Gij
βi
.
(11)
In the case where selection is present, s ̸= 0, we again
obtain the FPE (6), but now with a drift term given by
Ai(x) = 1
βi



D
X
j̸=i
Gij(xj −xi) + s
D
X
j=1
Gijαjxj(1 −xj)
−s2
D
X
j=1
Gijα2
jx2
j(1 −xj)


+ O(s3) .
(12)
The diﬀusion matrix meanwhile is unchanged from the
neutral case to leading order in s, Eq. (9).
The Taylor expansion in s is independent of the imple-
mentation of the Kramers-Moyal expansion. Since the
Kramers-Moyal expansion involves a truncation at order
N −2, the appropriate truncation of the series in s is ulti-
mately dependent on the relative size of s and N. We will
ﬁnd in the following analysis that it is suﬃcient for our
purposes to work to the orders in s indicated in Eqs. (12)
and (9).
III.
PROJECTION METHOD
This simpliﬁed system, described by the approximately
continuous state variable x, is not much more analyt-
ically tractable than the original master equation.
In
addition, writing the dynamics as a partial diﬀerential
equation does not aid the use of physical intuition in
suggesting further simpliﬁcations. However, as is well-
known [14, 25], the FPE (6), is entirely equivalent to the
It¯o stochastic diﬀerential equation
˙xi = Ai(x) +
1
√
N
ηi(τ),
(13)
where the dot indicates diﬀerentiation with respect to
τ = t/N and η(τ) is a Gaussian correlated white noise
with correlation functions
⟨ηi(τ)ηj(τ ′)⟩= Bij(x)δ(τ −τ ′).
(14)
It is in this framework that we choose to work, applying
concepts from deterministic dynamical systems theory in
order to understand the stochastic problem, and intro-
duce a method of simpliﬁcation which has not been used
before.
A.
The neutral case
Let us begin by considering the neutral case. The sys-
tem is then governed by the SDE
˙xi =
D
X
j=1
Hijxj +
1
√
N
ηi(τ),
i = 1, . . . , D.
(15)
First, we examine this equation in the deterministic
limit, N →∞. The SDE (15) is then solvable through
a linear analysis. It is clear from the deﬁnition of the
matrix H in Eq. (11) that each row in H sums exactly to
0 for any choice of parameters. We may therefore write
PD
j=1 Hij = 0 for all i, or alternatively as the eigenvalue
equation PD
j=1 Hij v(1)
j
= 0, where v(1)
j
= 1 ∀j is a right-
eigenvector of H with eigenvalue zero. We shall denote
this eigenvector as v(1) = 1, where 1 is the D-dimensional
vector
1 ≡





1
1
...
1




,
so that
H1 = 0 .
(16)
In addition, it can be shown that all other eigenvalues,
λ(2) . . . λ(D) have a real part which is negative, under the
condition that H is irreducible. In terms of our physical
system, this amounts to specifying that no subgroup of
demes is isolated from any other.
To prove this, one can transform H into a stochas-
tic matrix. Firstly we introduce a matrix ˜H, such that


## Page 5


5
˜Hij = βminHij/(D −1), where βmin is the smallest el-
ement of β. Every oﬀ-diagonal element of ˜H then lies
in the interval [0, 1], while every diagonal element lies
in the interval [−1, 0). We now form the matrix S with
entries Sij = ˜Hij + δij; since all entries of this matrix
are non-negative, and since each row sums to one, S is
a stochastic matrix [27, 28].
This implies that largest
eigenvalue of S is 1, and the magnitude of all its other
eigenvalues is less than one [27, 28]. Further, by construc-
tion, S and H share the same set of eigenvectors. We can
use these properties to show that the largest eigenvalue
of H is zero, while all other eigenvalues have a negative
real part.
The right- and left-eigenvectors corresponding to
eigenvalue λ(i) will be denoted by v(i) and u(i) respec-
tively. They are orthogonal to each other, and will be
normalized so that
D
X
k=1
u(i)
k v(j)
k
= δij.
(17)
In the special case that H is symmetric the left- and
right-eigenvectors coincide and the eigenvalues are real.
Already this tells us a great deal about the system
dynamics in the deterministic limit, since the general so-
lution to these equations is
xi(τ) =
D
X
j=1
cjv(j)
i eλ(j)τ ,
(18)
where the cj are constants.
Both ˙xi and Ai(x) =
P
j Hijxj have a similar form to (18), which means that
after some time:
(i) The vectors x, ˙x and A(x) are all in the direction
1.
(ii) The vectors ˙x and A(x) are actually zero in this
direction, since λ(1) = 0.
In other words, the eigenvalues λ(i) for i ≥2 control
the initial transient dynamics, which decay exponentially
along the eigenvectors v(i), i ≥2, to some point on the
vector v(1) where the system will stay indeﬁnitely.
In
the terminology of dynamical systems v(1) is coincident
with a center manifold [29], and we shall refer to the
eigenvectors v(i), i ≥2 as the fast directions.
Now, suppose we wish to ignore the initial fast be-
haviour of the system and pick out only the long-term
dynamics. The condition that A(x) has no components
in the fast directions v(j), j = 2, . . . , D may be written
in the form
D
X
i=1
u(j)
i Ai(x) = 0 ,
j = 2, . . . , D,
(19)
which we will also make use of when discussing the non-
neutral case. Since the state of the system, x, lies on the
line 1, we have x1 = x2 = . . . = xD. We will denote the
coordinate along 1 as z, so that the center manifold in
the neutral case is simply
xi = z,
i = 1, . . . , D.
(20)
However both ˙x and A(x) are zero on the center mani-
fold, and so the value of z does not change with time. Al-
though the deterministic dynamics of the neutral model
is trivial, the methodology developed here will be appli-
cable to the case with selection, which has non-trivial
dynamics.
We now ask, what happens when the population is ﬁ-
nite and the stochastic dynamics play a role? We would
expect that far from the center manifold, the determin-
istic dynamics would dominate over the noise terms, and
drag the system to the center manifold, along which the
stochastic dynamics would dominate. In turn any ﬂuctu-
ation that acted to move the system oﬀthe center man-
ifold, would soon be quashed by the deterministic term.
This is indeed what we see, as demonstrated in Fig. 2
for two and ﬁve demes respectively. A clear separation of
timescales exists; the deterministic dynamics act quickly
to bring the system to the region of the center manifold,
along which the system moves stochastically. Our inten-
tion is now to extend our treatment of the deterministic
system, in which we sought to neglect initial transient
dynamics, to the full stochastic system.
With this in mind, we make the assumption that there
is no noise in the fast directions.
The only remain-
ing contribution to the noise is then in the direction 1:
η(τ) = ζ(τ)1. Since, x is restricted to the center mani-
fold, and there is no deterministic drift along it, the SDE
(15) simply reduces to
˙z =
1
√
N
ζ(τ).
(21)
The noise ζ can be characterized by using Eq. (17) to
write it in terms of η as ζ(τ) = P
i u(1)
i ηi(τ). Then we
see that ζ is a Gaussian white noise with zero mean and
correlator
⟨ζ(τ)ζ(τ ′)⟩=
D
X
i,j=1
u(1)
i
Bij(x)|x=z1 u(1)
j δ(τ −τ ′),(22)
where Bij(x) has been evaluated on the center manifold
x = z1. Setting x = z1 in Eq. (9) with s = 0 we ﬁnd
¯B(z) ≡
D
X
i,j=1
u(1)
i
Bij(x)|x=z1 u(1)
j
= 2z(1 −z)
D
X
i,k=1
[u(1)
i ]2Gikβ−2
i
≡2b1z(1 −z) ,
(23)
where we have introduced the constant
b1 =
D
X
i,k=1
[u(1)
i ]2Gikβ−2
i
,
(24)


## Page 6


6
0
0.5
1
0
0.5
1
x1
x2
0
0.02
0.04
0
0.5
1
tHNâiΒiL2
ni
Βi N
0
0.003
0.006
0
0.5
1
ni
Βi N
FIG. 2. (Color online) Upper panel: Time series of an individ-
ual stochastic trajectory (red) and deterministic trajectories
(gray) for a neutral model with D = 2. The stochastic tra-
jectory can be seen to quickly collapse onto the deterministic
center manifold x1 = x2, highlighted in blue, along which
stochastic dynamics are observed. Lower panel: Time series
for the populations in a D = 5 system with equal deme sizes.
The inset graph shows clearly that the trajectories collapse to
the center manifold, after which they are coupled and move
in a stochastic fashion. The system size is N = 300 for each
deme in both plots.
and use a bar to indicate evaluation on the center man-
ifold.
Extending this notation, Eq. (21) may be more
generally expressed as
˙z = ¯A(z) +
1
√
N
ζ(τ),
(25)
where the drift term evaluated on the center manifold is
zero, ¯A(z) = 0, and where ζ(t) is Gaussian correlated
white noise with zero mean and correlation function
⟨ζ(τ)ζ(τ ′)⟩= ¯B(z)δ(τ −τ ′).
(26)
Our aim in this subsection has been to characterize the
stochastic dynamics along the center manifold, and so
to develop a one-dimensional, reduced theory. We have
also observed that given some set of initial conditions,
the stochastic system relaxes to the center manifold on a
much faster timescale than that on which the stochastic
dynamics act.
The reduced model is therefore ideally
suited to answering questions related to global ﬁxation,
such as the ﬁxation probability and the mean ﬁxation
time, which are long-time properties of the system.
In order to approximate the initial value of the system
on the center manifold, we assume that the trajectory to
the center manifold is essentially deterministic. Then the
initial condition on the center manifold, z0, is simply the
component of the full initial condition x0, along v1 = 1:
z0 =
D
X
i=1
u(1)
i x0i .
(27)
Together with Eqs. (25) and (26), this fully deﬁnes the
reduced model.
B.
The case with selection
Having considered the neutral model with migration,
in which neither allele A nor B has any ﬁtness relative
to the other, we now consider the case where there is a
relative ﬁtness.
To reiterate, this model is now described by the SDE
(13), with drift and diﬀusion terms given by Eq. (12) and
Eq. (9) to leading order. We note that deterministically
the system may now admit a non-trivial ﬁxed point in the
region between 0 < xi < 1, i = 1, . . . , D; the analysis of
the consequences of this will be discussed elsewhere [26].
We begin by noting that since s has been deﬁned as
a small parameter in relation to the migration matrix
(and hence also the matrix H), we would still expect the
system to exhibit a separation of timescales. Now how-
ever there is no center manifold; there is no line along
which the deterministic dynamics vanish, as the nonlin-
ear s terms cause deterministic drift.
Instead, a slow
subspace exists onto which the system quickly relaxes.
The existence of such a subspace is clearly seen in deter-
ministic and stochastic simulations. We avoid the term
“slow manifold”, since this has a distinct technical mean-
ing [30]; the slow subspace is a curved line in the present
context, although because s is small it only has a slight
curvature.
How do we mathematically specify the slow subspace?
Although Eq. (12) shows that the s ̸= 0 deterministic
theory is inherently nonlinear, since s is typically very
small, we will continue to use the s = 0 left-eigenvectors
u(j) to approximate the slow subspace through Eq. (19).
Solving these equations numerically, we ﬁnd that they
provide a very good approximation to the observed slow
subspace. In Appendix A we solve the (D −1) equations
of Eq. (19) to ﬁnd the slow subspace analytically.
To


## Page 7


7
do this we transform to a co-ordinate system x = z1 +
PD−1
a=1 yav(a+1). We ﬁnd that the equation of the slow
subspace takes the form
ya(z) = casz(1 −z) + O(s2),
(28)
where the ca are constants which are calculated in the
Appendix. As s →0, ya(z) →0, and the slow subspace
becomes the center manifold, 1, of the neutral case dis-
cussed in Section III A.
The condition given by Eq. (19) still means that A lies
in the 1 direction. Therefore once again the deterministic
dynamics is only in this direction.
If we ask that the
noise is only in this direction too, then we again write
η(τ) = ζ(τ)1, just as we did in the neutral case, to ﬁnd
Eqs. (25) and (26), but now with ¯A(z) ̸= 0. To ﬁnd ¯A(z)
we use Eq. (17) to pick out the component of A along 1,
and evaluate it in the slow subspace given by Eq. (28):
¯A(z) ≡
D
X
i=1
u(1)
i Ai(z, y(z)) .
(29)
It is important to note that the dynamics is only in the
direction 1, even though the system relaxes to the slow
subspace given by Eq. (28). Thus the approximation re-
quires that the ya have no dynamics; they are simply
mapped on to a value of z using Eq. (28).
In fact from a mathematical point of view, the whole
procedure may be speciﬁed in terms of a projection onto
the direction 1 from any point in state space, together
with an understanding that the drift should be evaluated
on Eq. (28). To do this, we construct a matrix P, such
that when it is applied to any vector wipes out the fast
directions v(a) for a = 2, . . . , D, but leaves the compo-
nent along the direction v(1) = 1, untouched. Using the
vector u(1), which is perpendicular to the fast directions,
we can construct the projection matrix as
Pij =
v(1)
i
u(1)
j
PD
k=1 v(1)
k u(1)
k
.
(30)
Since v(1) is simply 1,
Pij = u(1)
j
,
i = 1, . . . , D,
(31)
using the orthonormality condition (17).
We have al-
ready implicitly used this to deﬁne ¯A and ¯B, but it
can be directly applied to Eq. (13) to obtain Eq. (25).
The requirement that the drift vanishes in the fast direc-
tions, Eq. (19), is still required to ﬁnd the slow subspace
Eq. (28).
Let us now apply this approximation procedure. We
begin by noting that the drift vector Eq. (12) truncated
at second order in s can be alternatively expressed by
Ai(x) = PD
j=1 Hijxj + β−1
i
n
s PD
j=1 Gijαjxj(1 −xj)
−s2 PD
j=1 Gijα2
jx2
j(1 −xj)
o
,
(32)
while the diﬀusion matrix is left unchanged from the neu-
tral case to leading order (see Eq. (9)). In Appendix A,
we obtain the expression (A8) for the drift vector eval-
uated on the slow subspace (Ai(z, y(z)) in Eq. (29)) in
terms of the projected variable z. The elements of A(z)
to this order take the form
Ai(z) = −sq(0)
i
z(1 −z) + sq(1)
i
z(1 −z) −s2q(2)
i
z2(1 −z)
−s2q(3)
i
z(1 −z)(1 −2z) ,
where the vectors of parameters, q(i), i = 0, . . . , 3, are
deﬁned in Appendix A. The diﬀusion matrix evaluated
on the slow subspace is given in Eq. (A10).
As in Section III A we apply the projection (Eq. (31))
to the SDE (13), with the above drift vector and dif-
fusion matrix. This again leads to the reduced SDE of
type Eq. (25), but now with ¯A(z) given by Eq. (29). The
term −sq(0)
i
z(1 −z) which appears in Ai(z) does not ap-
pear in ¯A(z) because P
i u(1)
i q(0)
i
= 0, which follows from
P
i u(1)
i Hij = 0. The remainder of the expression is given
by
¯A(z) = sa1z(1 −z) + s2a2z2(1 −z)
+s2a3z(1 −z)(1 −2z) ,
(33)
and ¯B(z) retains the form obtained in the neutral case,
Eq. (23). The parameters a1 and a2 are found to be only
dependent on the parameters of the problem (m, f, β,
α) and on the left-eigenvector u(1):
a1 =
D
X
i=1
Pkiq(1)
i
=
D
X
i,j=1
u(1)
i
Gijαj
βi
(34)
and
a2 = −
D
X
i=1
Pkiq(2)
i
= −
D
X
i,j=1
u(1)
i
Gijα2
j
βi
.
(35)
The parameter a3 meanwhile is found to be dependent
on the full set of left- and right-eigenvectors and their
corresponding eigenvalues:
a3 = −
D
X
i=1
Pkiq(3)
i
(36)
= −
D−1
X
a=1


D
X
i,j=1
u(1)
i Gijαj
βi
D
X
k,l=1
v(a+1)
j
u(a+1)
k
λ(a+1)
Gklαl
βk

.
Its more complicated form is a consequence of the curva-
ture of the slow subspace.
IV.
COMPARISON WITH SIMULATIONS
In the last section, fast-variable elimination was used
to simplify the migration model to a one-dimensional
SDE with the form of Eq. (25).
The drift term ¯A(z)


## Page 8


8
is zero for the case s = 0 and given by Eq. (33) to second
order in s. The diﬀusion term ¯B(z) is given by Eq. (23)
in each case.
Having started from an IBM, the validity of the ap-
proximation can now be tested by comparing predictions
of the model against Gillespie simulations [31, 32], which
provide exact solutions to realizations of the master equa-
tion (3). As measures to test the validity of the approx-
imation, we choose the ﬁxation probability and time to
ﬁxation of the system given a set of initial allele frequen-
cies on each deme.
First we note that the one-dimensional It¯o SDE
(25) that we have constructed is equivalent to a one-
dimensional FPE [14, 25] which takes the form
∂p(z, t)
∂t
= −1
N
∂
∂z
 ¯A(z)p(z, t)

+
1
2N 2
∂2
∂z2
 ¯B(z)p(z, t)

.
(37)
The ﬁxation probability of allele A, Q(z0), and time to
ﬁxation, T(z0), as a function of the initial condition, pro-
jected onto the manifold
Px0 = z01 ,
(38)
can be calculated from the backward Fokker-Planck
equation, formally the adjoint of the FPE [14, 25]
∂q(z, t)
∂t
=
¯A(z)
N
∂
∂z [q(z, t)] +
¯B(z)
2N 2
∂2
∂z2 [q(z, t)] . (39)
The general theory which starts from a FPE of the form
given by Eq. (37), and via the backward equation (39)
leads to equations for Q(z0) and T(z0), is standard and
we refer the reader to the literature [14, 25] for the details.
The probability of ﬁxation, Q(z0) satisﬁes the ordinary
diﬀerential equation
¯A(z0)
N
dQ(z0)
dz0
+
¯B(z0)
2N 2
d2Q(z0)
dz2
0
= 0,
(40)
with boundary conditions
Q(0) = 0 ,
Q(1) = 1 .
(41)
The boundary conditions may be understood by noting
that when there are no instances of allele A in the popu-
lation, z0 = 0, there is no possibility of ﬁxation, while if
there are no B alleles, z0 = 1 and allele A has ﬁxed.
The equation for the mean time to ﬁxation, T(z0), is
¯A(z0)
N
dT(z0)
dz0
+
¯B(z0)
2N 2
d2T(z0)
dz2
0
= −1,
(42)
with the boundary conditions,
T(0) = 0 ,
T(1) = 0 .
(43)
In this case the boundary conditions follow by noting
that they are the time to ﬁxation of either A or B allele,
so that at both extremes, z0 = 0 and z0 = 1, the system
has already ﬁxed on A or B.
Solutions to these equations will now be described for
the reduced dimension model in the cases s = 0 and
s ̸= 0, and the predictions from the reduced systems
compared to simulation.
A.
Comparison with simulations — Neutral Case
We begin by noting that the reduced Fokker-Planck
equation now takes on the same functional form as that
which is derived for the neutral Moran model on a single
island [24]. Scaling N 2 by b1 and setting z = x1, the
results are identical.
For a general system with known parameters, the
calculation of b1 depends only on obtaining the left-
eigenvector of H, u(1). For small values of D, or alter-
natively, H matrices with some exploitable symmetries,
it may be possible to obtain this analytically. Numer-
ically however, expressions for b1 are easily obtainable.
One could thus proceed in an almost algorithmic way to
obtain the reduced FPE given a migration matrix, m,
island sizes, β and the island birth rates f.
We now note some special cases. Firstly, let us take
the case where the matrix H is symmetric. Then the left-
and right-eigenvectors, u(1) and v(1) coincide (up to an
overall constant). Since v(1) = 1, u(1)
i
= constant for all
i. Using the normalization condition (17) we ﬁnd that
u(1)
i
= D−1 ∀i, and so from Eq. (24)
b1 =
D
X
i,j=1
Gij
(βiD)2 .
(44)
Perhaps more interesting is the case where the ma-
trix G is symmetric. We begin by looking at the quan-
tity PD
i=1 βiHij and expressing H in terms of G using
Eq. (11):
D
X
i=1
βiHij =
D
X
i̸=j
βi
Gij
βi
+ βj

−
D
X
k̸=j
Gjk
βj


=
D
X
i̸=j
Gij −
D
X
k̸=j
Gjk =
D
X
i̸=j
[Gij −Gji] = 0,
(45)
if G is symmetric. So in this case βi is the left-eigenvector
of H with zero eigenvalue, that is, it is equal to u(1)
i , up to
an overall constant. Since from Eq. (17), PD
i=1 u(1)
i
= 1,
we have that
u(1)
i
=
βi
PD
j=1 βj
.
(46)
This leads to
b1 =


D
X
j=1
βj


−2
,
(47)
using Eqs. (7) and (24). This shows that, for a symmet-
ric G matrix, the reduced FPE for the metapopulation
model is identical to the full FPE for a well-mixed model
with the same total number of individuals, N PD
i=1 βi.
In the neutral case Eq. (40) can be solved trivially to
give
Q(z0) = z0,
(48)


## Page 9


9
where we recall that the projected initial condition, z0 is
found from Eq. (38). The probability of ﬁxation depends
only on the structure and form of the metapopulations
through the determination of the initial conditions.
The mean time to ﬁxation can be calculated from
Eq. (42), and also resembles the standard result for one
island [33]:
T(z0) = −N 2
b1
[(1 −z0) ln (1 −z0) + z0 ln (z0)] . (49)
In order to test the predictions of the reduced model,
Eq. (48) and Eq. (49), we compare them against stochas-
tic Gillespie simulations of the underlying microscopic
model (speciﬁed by the transition rates (2)) for a range
of systems. We ﬁnd excellent agreement. In particular,
Fig. 3 illustrates the results obtained from three diﬀerent
migration matrices, m. As predicted the probability of
ﬁxation, Q(z0) is only dependent on the structure of m
though the projected initial condition, z0 (see Eq. (27)).
The mean time to ﬁxation meanwhile is highly dependent
on the structure of m. It is clear that the reduced model
reﬂects this dependency very well.
B.
Comparison with simulations — case with
selection
In the following analysis we shall consider the case in
which ¯A(z) given by Eq. (33) is truncated at ﬁrst and
second order in s separately. There are two reasons for
doing this.
First, the case where only the linear term
in s is retained can again be mapped onto the full FPE
for a one-island Moran model, but with selection. Now
not only is N 2 scaled by b1, but s is scaled by a1 and
√b1. Second, the order at which we truncate ¯A(z) can
be viewed as an assumption about the relative size of
the parameters s and N. In the Kramers-Moyal expan-
sion, which was used to obtain (6), we have neglected
terms smaller than order N −2. For consistency we would
also like to neglect any terms smaller than this arising
from s contributions. If s ≈O(N −1), neglecting O(N −3)
terms in (6) results in an expression for ¯A(x) which is
ﬁrst order in s. However, if s ≈O(N −1/2), neglecting
O(N −5/2) terms results in ¯A(x) which is second order in
s. Finally, we will present results for rather small val-
ues of N and rather large values of s, as compared with
those commonly found in population genetics. We would
expect our approximation scheme to become better as N
increases, and as a consequence of the above argument,
give similar results for proportionally smaller values of s.
We begin by investigating the case where ¯A(z) is trun-
cated at ﬁrst order in s.
Solving Eq. (42), with ¯B(z)
given by Eq. (23), leads to the probability of ﬁxation
being given by
Q(z0) = 1 −exp (−Nsa1z0/b1)
1 −exp (−Nsa1/b1) .
(50)
Scaling N by a factor a1/b1 gives the one island result
with z = x1 [33]. The form of T(z0) is found by solving
0.5
1
0.5
1
z0
QHz0L
0.5
1
2.5
5
z0
T Hz0L
HN Úi ΒiL2
FIG. 3. (Color online) Upper panel: Probability of ﬁxation
as a function of the projected initial conditions for neutral
systems, s = 0.
Lower panel: Mean time to ﬁxation as a
function of the projected initial conditions, again for s = 0
neutral systems. Continuous lines show the analytic predic-
tions from Eq. (48) and (49) while the values of symbols are
obtained as the mean of 5000 stochastic simulations. Here
the model with three demes is studied, each of the demes has
size N = 200. The various colors/symbols are obtained from
diﬀering migration matrices. The system indicted by a blue
line (the central data in the lower panel) has a symmetric
migration matrix with b1 =
PD
j=1 βj
−2
.
Eq. (42) numerically with the same choice of ¯A(z) and
¯B(z).
We ﬁnd that simulation and the one-dimensional ap-
proximation give excellent agreement for a wide range of
parameters, as demonstrated in Fig. 4. For systems in
which the form of a1 and b1 result in a large selective
advantage for one or the other of the alleles, the time
to ﬁxation can be observed to clearly lose the symmetric
form observed in the neutral case. This can be seen in
Fig. 4 for the results represented in green/squares and
those in blue/circles.
We now perform a similar comparison in the case where
¯A(z) truncated at second order in s. While analytical re-
sults for the probability of ﬁxation and mean time to ﬁx-
ation can be obtained in this case, as they can be in the
case when ¯A(z) is linear in s, they will be discussed else-
where [26]. Here we restrict ourselves to solving the dif-
ferential equations (40) and (42) numerically in order to
demonstrate the predictive power of the reduced model.


## Page 10


10
0.5
1
0.5
1
z0
QHz0L
0
0.5
1
0.
0.5
1
z0
T Hz0L
HN Úi ΒiL2
FIG. 4. (Color online) Plots for the probability of ﬁxation
(upper panel) and mean time to ﬁxation (lower panel) as a
function of the projected initial conditions for the ﬁrst order
in s case. Continuous lines are obtained from Eq. (50) and by
solving (42) numerically with ¯A(z) to order s and ¯B(z) given
by Eq. (23). Various symbols indicate the results obtained
from simulations. For each diﬀerent color/symbol diﬀerent α
vectors are used; green squares, α = (1, 1, −1), red triangles,
α = (−1, −1, 1), and blue circles, α = (1, −2, −1). All other
parameters are kept constant; s = 0.005, N = 200, β =
(3, 2, 1) and the migration matrix m is ﬁxed, though not given
here. Simulation results are the average of 5000 runs.
We will also choose model parameters which are not re-
lated to any speciﬁc application for a similar reason; the
method in speciﬁc contexts will also be described else-
where [26]. In Fig. 5 results are plotted for two particular
parameter sets, in which very good agreement between
simulation and theory is observed. In particular we note
the plot for the probability of ﬁxation, Q(z0), in repre-
sented by blue lines and circles; the functional form ob-
served here is unobtainable from the order s description,
Eq. (50).
V.
ESTIMATING THE RANGE OF VALIDITY
OF THE METHOD
Having discussed the approximation method and re-
sults, we now turn to considering the range of validity
of the expressions for the reduced system, providing a
heuristic argument along with a numerical analysis.
0
0.5
1
0
0.5
1
z0
QHz0L
0
0.5
1
0
0.75
1.5
z0
T Hz0L
HN Úi ΒiL2
FIG. 5. (Color online) Plots for the probability of ﬁxation,
Q(z0), and mean time to ﬁxation, T(z0), to second order in
s.
Continuous lines are obtained from the reduced model,
solving (40) and (42) respectively. Parameters used for the
results in blue circles are D = 2, N = 400, s = 1/
√
N, β =
(1, 1), α = (1, −1). Parameters used for the results in red
triangles are D = 4, N = 300, s = 1/
√
N, β = (1, 1, 1, 2),
α = (1, 1, 0.3, −1). In both cases the migration matrices are
non-symmetric. Simulation results are the mean of 104 runs.
As stated in Section III A the quantities that govern
the separation of timescales are the eigenvalues of H.
While the ﬁrst eigenvalue, λ(1), is always zero, we require
that the remaining eigenvalues are suﬃciently less than
zero so that the collapse of the system onto the slow
subspace or center manifold happens on a much faster
timescale than that of ﬁxation. What, then, is a suﬃcient
separation of eigenvalues? To investigate this we consider
a D = 3 system where each deme is of equal size, whose
migration matrix is characterized by a single number 0 <
θ < 1:
m =


θ
(1 −θ)/2 (1 −θ)/2
(1 −θ)/2
θ
(1 −θ)/2
(1 −θ)/2 (1 −θ)/2
θ

.
(51)
With these properties, the H matrix for the system can
be simply constructed. We ﬁnd a degenerate system with
only two eigenvalues, the ﬁrst, zero, and the other two
given by λ(2) = (θ −1)/2. We can then plot how the pre-
dictions of the reduced system, Eq. (25), compare against
the results of simulation for some ﬁxed initial condition
as λ(2) increases.


## Page 11


11
-0.2
-0.1
0
0
0.2
0.4
ΛH2L
QH0.2L
-0.2
-0.1
0
0
0.75
1.5
ΛH2L
T H0.2L
HN Úi ΒiL2
FIG. 6. (Color online) Plots of the probability of ﬁxation and
normalized time to ﬁxation as a function of increasing eigen-
value (equivalent to decreasing the strength of collapse onto
the center manifold). The system is prescribed by the migra-
tion matrix given in Eq. (51), with D = 3, β = (1, 1, 1),
s = 0, and N = 200, and the initial condition for both
plots is z0 = 0.2. Mean values from 104 stochastic simula-
tions are plotted as circles, whereas continuous lines repre-
sent theoretical predictions. The ﬁnal point on both plots is
λ(2) = −5 × 10−4.
The results in the neutral case are shown in Fig. 6. We
recall that since the matrix is symmetric, b1 is given by
Eq. (47). One can see that the reduced system agrees well
with the probability of ﬁxation across a remarkably large
range of eigenvalues. While the prediction for the time
to ﬁxation fares slightly less well, results from simulation
still agree over a very large range of parameters, only
beginning to diverge at approximately λ2 = −0.05, at
which point one begins to see an rapid increase in ﬁxation
time of the simulations. This is also the point at which
the magnitude of the noise, moderated by 1/
√
N, is of
the order of the deterministic term (see Eq. (13)).
In the case where selection is present, s ̸= 0, we can
conduct a study of the same system for a ﬁxed set of
selection parameters. We recall here, that the reduction
techniques relies on the term PD
j=1 Hijxj in Eq. (32) in-
ducing a near-deterministic, linear collapse and restric-
tion of the system to the slow subspace. In this situation,
where s ̸= 0, this assumption is not only broken by the
noise but also the order s nonlinear terms in Eq. (32).
We might therefore expect the reduced system to per-
-0.2
-0.1
0
0
0.2
0.4
ΛH2L
QH0.6L
-0.2
-0.1
0
0
1.25
2.5
ΛH2L
T H0.6L
HN Úi ΒiL2
FIG. 7.
(Color online) Plots of the probability of ﬁxation
and normalized time to ﬁxation as a function of increasing
eigenvalue in a system with s = 0.035. The system is pre-
scribed by the migration matrix given in Eq. (51), with D = 3,
β = (1, 1, 1), N = 200 and α = (1, −2, 0.5), and the initial
condition for both plots is z0 = 0.6. Mean values from 6×103
stochastic simulations are plotted as circles, whereas continu-
ous lines represent theoretical predictions. The ﬁnal point on
both plots is λ(2) = −0.025.
form less well with decreasing λ(2) than the neutral case.
While we ﬁnd this is the case (see Fig. 7), the approxi-
mation still works very well up to λ(2) ≈−0.05. At this
point our reduced system under-predicts the probability
of ﬁxation and over-predicts the time to ﬁxation, grow-
ing rapidly, much faster than the results from simulation
would suggest.
VI.
CONCLUSIONS
The methodology of statistical mechanics is frequently
applicable in areas outside of the physical sciences in
cases where a large number of entities of a similar type
interact with each other. However, the nature of the in-
teraction will usually be more varied than in physics or
chemistry.
One kind of system structure that is often
encountered is that of a set of ‘islands’, each contain-
ing a large number of constituents, which interact with
each other with a strength given by the magnitude of the
links in a ﬁxed network. The diﬃculty in studying the
statistical dynamics of such systems is the complexity of


## Page 12


12
the governing equations. Even after making a diﬀusion
approximation, they will consist of a set of coupled non-
linear SDEs with multiplicative noise.
In this paper we have presented a method of reducing
this set of SDEs down to a single SDE, which can then
be analyzed. The method was applied in the speciﬁc case
of population genetics where the islands are demes, the
constituents are individuals with a gene which can be
one of two types, and with the interaction being the mi-
gration between demes. The approximation was based
on the elimination of fast degrees of freedom, which re-
sulted in a stochastic dynamics that was conﬁned to a
one-dimensional slow subspace. We expect this method
to be applicable to many other areas, such as those re-
ferred to the Section I, but chose to illustrate the idea in
the case of population genetics because of the importance
of selection in that context.
The method we have developed is in excellent agree-
ment with simulations, is simple to understand, and re-
sults in a what is eﬀectively an algorithm which may
be applied to any network. The constants a1, a2 and a3
which appear in the drift term in the ﬁnal SDE, Eq. (33),
are given by precise formulas which can be calculated
given any network structure.
These are the constants
that appear when the form of the SDE is calculated to
order s2, where s is the selection strength. It is possible
to go to higher order in s, but s is usually so small that
this would almost certainly never be required; studies
which work to order s2 are already extremely rare, most
authors being content to work only to order s.
The method does not assume that the number of in-
dividuals is the same in each deme, although we expect
the results will be less reliable if some demes are an order
of magnitude bigger than others. If this is the case, the
elimination of fast modes may still go through, but diﬀer-
ent methods of approximation would be more applicable.
Similarly, as discussed in Section V, if the non-zero eigen-
values of the matrix H are too close to zero, then the ap-
proximation may break down. This means that, a priori,
one cannot tell if the reduction technique is applicable
for general m, f and s. Instead one must ﬁrst construct
the matrix H to determine its eigenvalues. One can then
check that the parameters lie broadly in the range iden-
tiﬁed in Section V; the non-zero eigenvalue of H which
is closest to zero, λ(2), should have a magnitude greater
than both O(N −1/2) and s. The mathematical origins of
these limits are interesting points to investigate in future
work.
Here we have conﬁned ourselves to describing the
methodology of the reduction from many coupled SDEs
to a single SDE, and to showing that it is an excellent
approximation for a wide range of parameters. We will
explore the consequences for a number of problems in
population genetics elsewhere [26], but we believe that
the method is quite general, and hope and expect that it
will be used in a large range of applications in the future.
ACKNOWLEDGMENTS
We
thank
Tim
Rogers
for
useful
discussions.
G.W.A.C. thanks the Faculty of Engineering and Phys-
ical Sciences,
University of Manchester for funding
through a Dean’s Scholarship.
Appendix A: Calculation of the dynamics on the
slow subspace
In this appendix some of the more technical aspects of
ﬁnding the slow subspace and calculating the dynamics
of the reduced system will be set out. So far we have
only speciﬁed the natural variable which we use in the
reduced system, that is z = PD
i=1 u(1)
i xi.
More generally, we can deﬁne a linear transformation
to the coordinate z and D −1 coordinates y such that

z
y

= T −1x ,
x = T

z
y

.
(A1)
A convenient choice for xi is
xi = z +
D−1
X
a=1
Wiaya .
(A2)
Since, from Eq. (20), xi = z on the center manifold in the
neutral case, we ask that the ya are of order s on the slow
subspace in the case with selection. This will simplify our
calculation because, as we will see, this means that we
will only have to calculate the ya as functions of z to
leading order in s.
In terms of the transition matrix T, the choices made
so far mean that
T −1 =

[u(1)]T
R

,
T = (1
W) ,
(A3)
where R is a D −1 by D matrix and W is a D by D −1
matrix. The form of the matrices R and W is restricted
through the conditions TT −1 = T −1T = I, the identity
matrix. The condition relevant if we are trying to express
x in terms of z and y, is
D
X
i=1
u(1)
i Wia = 0 ,
a = 1, . . . , D −1.
(A4)
We will need to check that any choice we make for Wia
satisﬁes this condition.
We now substitute the transformation (A2) into


## Page 13


13
Eq. (32) for the drift vector in terms of x:
Ai(z, y) =
D
X
j=1
Hij
 
z +
D−1
X
a=1
Wjaya
!
+ sz(1 −z)
D
X
j=1
Gijαj
βi
+ s(1 −2z)
D
X
j=1
Gijαj
βi
D−1
X
a=1
Wjaya
−s2z2(1 −z)
D
X
j=1
Gijα2
j
βi
+ O(s2y, s3) .
(A5)
Using (i) PD
j=1 Hijz = z PD
j=1 Hij = 0, from Eq, (11),
and (ii) the slow subspace condition PD
i=1 u(a+1)
i
Ai = 0,
a = 1, . . . , D −1 (see Eq. (19)), we ﬁnd
0 =
D
X
i,j=1
D−1
X
a=1
u(a+1)
i
HijWjaya
+ sz(1 −z)
D
X
i,j=1
u(a+1)
i
Gijαj
βi
,
(A6)
since the slow subspace condition must be satisﬁed order
by order in s and y is assumed to be of order s. Choosing
Wja to be the right-eigenvectors v(a+1)
j
, a = 1, . . . , D−1,
which is consistent with the conditions (A4), we see that
the ﬁrst term on the right-hand side of Eq. (A6) is simply
λ(a+1)ya. Therefore
ya(z) = −sz(1 −z)
λ(a+1)
D
X
i,j=1
u(a+1)
i
Gijαj
βi
+ O(s2) .(A7)
Substituting Eq. (A7) into Eq. (A5), the drift vector
evaluated on the slow subspace is found to be
Ai(z) = −sq(0)
i
z(1 −z) + sq(1)
i
z(1 −z) −s2q(2)
i
z2(1 −z)
−s2q(3)
i
z(1 −z)(1 −2z) + O(s3) ,
(A8)
where the vectors q0, q1, q2 and q3 are the parameter
combinations
q(0)
i
=
D−1
X
a=1
D
X
j,k,l=1
Hijv(a+1)
j
u(a+1)
k
Gklαl
βkλ(a+1)
,
q(1)
i
=
D
X
j=1
Gijαj
βi
,
q(2)
i
=
D
X
j=1
Gijα2
j
βi
,
q(3)
i
=
D−1
X
a=1
D
X
j,k,l=1
Gijαj
βi
v(a+1)
j
u(a+1)
k
λ(a+1)
Gklαl
βk
.
(A9)
The elements of the diﬀusion matrix meanwhile, when
evaluated on the slow subspace, have the form
Bii(z) = 2z(1 −z)
D
X
j=1
Gij
β2
i
+ O(s) .
(A10)
Since the matrix H is not in general symmetric, then
the eigenvalues will not in general be real. However since
the entries of H are real, the eigenvalues will occur in
complex conjugate pairs, and the eigenvectors associated
with an eigenvalue λ∗will be the complex conjugates of
those associated with λ. Since the expressions for q(0)
i
and q(3)
i
in Eq. (A9) take the form of sums over a, for
each term which is not real there will be another term
added to it which is its complex conjugate. Thus q(0)
i
and q(3)
i
are guaranteed to be real. Therefore, the pro-
cedure goes through whether the eigenvalues are real or
not. Of course, if there are complex conjugate pairs, the
corresponding ya cannot be interpreted as coordinates.
However this interpretation is not crucial to the method,
and if one wishes, it is always possible to deﬁne real co-
ordinates by working with the real and imaginary parts
of the eigenvalues and eigenvectors.
[1] A. J. Black and A. J. McKane, Trends Ecol. Evol., 27,
337 (2012).
[2] H. P. de Vladar and H. Barton, Trends Ecol. Evol., 26,
424 (2011).
[3] C. Castellano, S. Fortunato, and V. Loreto, Rev. Mod.
Phys, 81, 591 (2009).
[4] S. N. Dorogovtsev and J. F. F. Mendes, Evolution of Net-
works: From Biological Nets to the Internet and WWW
(Oxford University Press, Oxford, 2003).
[5] M. Newman, Networks: An Introduction (Oxford Uni-
versity Press, Oxford, 2010).
[6] R. Levins, Bull. Entomol. Soc. Am., 15, 237 (1969).
[7] I. Hanski, Metapopulation Ecology (Oxford University
Press, Oxford, 1999).
[8] D. L. Hartl and A. G. Clark, Principles of Population Ge-
netics (Sinauer Associates Inc., Sunderland, Mass., 2007)
Fourth edition.
[9] G. Rozhnova, A. Nunes, and A. J. McKane, Phys. Rev.
E, 84, 051919 (2011).
[10] J. D. Challenger and A. J. McKane, Phys. Rev. E, 88,
012107 (2013).
[11] W. Croft, Explaining Language Change: An Evolutionary
Approach (Longman, Harlow, 2000).
[12] N. G. van Kampen, Stochastic Processes in Physics and
Chemistry, 3rd ed. (Elsevier Science, Amsterdam, 2007).
[13] A. J. McKane, T. Biancalani, and T. Rogers, Bull. Math.
Biol., DOI:10.1007/s11538 (2014).
[14] H. Risken, The Fokker-Planck Equation - Methods of So-


## Page 14


14
lution and Applications, 2nd ed. (Springer, Berlin, 1989).
[15] G. W. A. Constable, A. J. McKane, and T. Rogers, J.
Phys. A: Math. Theor., 46, 295002 (2013).
[16] T. Nagylaki, J. Math. Biol., 9, 101 (1980).
[17] G. J. Baxter, R. A. Blythe,
and A. J. McKane, Phys.
Rev. Lett., 101, 258701 (2008).
[18] T. Rogers and T. Gross, Phys. Rev. E, 88, 030102(R)
(2013).
[19] Y. T. Lin, H. Kim,
and C. R. Doering, J. Stat. Phys.,
148, 646 (2012).
[20] P. A. P. Moran, Math. Proc. Cam. Phil. Soc., 54, 60
(1957).
[21] P. A. P. Moran, The Statistical Processes of Evolutionary
Theory (Clarendon Press, Oxford, 1962).
[22] R. A. Blythe and A. J. McKane, J. Stat. Mech., P07018
(2007).
[23] R. A. Fisher, Proc. Roy. Soc. Edin., 42, 321 (1922).
[24] J. F. Crow and M. Kimura, An Introduction to Popu-
lation Genetics Theory (The Blackburn Press, Caldwell,
New Jersey, USA, 2009).
[25] C.
W.
Gardiner,
Handbook
of
Stochastic
Methods
(Springer, Berlin, 2009) Fourth edition.
[26] G. W. A. Constable and A. J. McKane, “Population ge-
netics on islands connected by an arbitrary network: an
analytic approach,” (2014), Pre-print arXiv:1402.2564.
[27] F. R. Gantmacher, Applications of the Theory of Matrices
(Interscience, New York, 1959).
[28] D. R. Cox and H. D. Miller, The Theory of Stochastic
Processes (Chapman and Hall, London, 1965).
[29] S. Wiggins, Introduction to Applied Nonlinear Dynamical
Systems and Chaos (Springer, New York, 2003).
[30] N. Berglund and B. Gentz, Noise-Induced Phenomena
in Slow-Fast Dynamical Systems: A Sample-Paths Ap-
proach (Springer-Verlag, London, 2006).
[31] D. T. Gillespie, J. Comput. Phys., 22, 403 (1976).
[32] D. T. Gillespie, J. Phys. Chem., 81, 2340 (1977).
[33] W.
J.
Ewens,
Mathematical
Population
Genetics
(Springer-Verlag, Berlin, 2004) Second edition.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
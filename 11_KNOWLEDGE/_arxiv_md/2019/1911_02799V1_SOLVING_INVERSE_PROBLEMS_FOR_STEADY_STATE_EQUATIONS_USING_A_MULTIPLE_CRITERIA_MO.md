---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.02799v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1911.02799v1_Solving_Inverse_Problems_for_Steady-State_Equations_using_A_Multiple_Criteria_Mo

> Source: 1911.02799v1_Solving_Inverse_Problems_for_Steady-State_Equations_using_A_Multiple_Criteria_Mo.pdf

> Pages: 17

---


## Page 1


Solving Inverse Problems for Steady-State
Equations using A Multiple Criteria
Model with Collage Distance, Entropy,
and Sparsity
Herb Kunze∗
Davide La Torre†
November 11, 2019
Abstract
In this paper, we extend the previous method for solving inverse
problems for steady-state equations using the Generalized Collage The-
orem by searching for an approximation that not only minimizes the
collage error but also maximizes the entropy and minimize the sparsity.
In this extended formulation, the parameter estimation minimization
problem can be understood as a multiple criteria problem, with three
diﬀerent and conﬂicting criteria: The generalized collage error, the en-
tropy associated with the unknown parameters, and the sparsity of
the set of unknown parameters. We implement a scalarization tech-
nique to reduce the multiple criteria program to a single criterion one,
by combining all objective functions with diﬀerent trade-oﬀweights.
Numerical examples conﬁrm that the collage method produces good,
but sub-optimal, results. A relatively low-weighted entropy term al-
lows for better approximations while the sparsity term decreases the
complexity of the solution in terms of the number of elements in the
basis.
1
Introduction
We present a multiple criteria model for solving an inverse problem for
diﬀusion models described in terms of Partial Diﬀerential Equations (PDEs).
The theory of PDEs is crucial for modelling several problems in diﬀerent
disciplines, such as Business, Economics, Engineering, Finance and so on.
For instance it can be used to model the process of innovation and spread of
∗Department of Mathematics and Statistics, University of Guelph, Guelph, Canada.
Email: hkunze@uoguelph.ca
†SKEMA Business School - Universit´e Cˆote d’Azur, Sophia Antipolis Campus, France.
Email: davide.latorre@skema.edu
1
arXiv:1911.02799v1  [math.NA]  7 Nov 2019


## Page 2


ideas, the evolution of population dynamics, the dynamics of ﬂuids, option
pricing, and many other.
A PDE can be analyzed from both a direct and inverse approach: the
direct problem is the analysis of the properties of existence, uniqueness, and
stability of the solution. This is also refereed to the notion of well-posedness
in the sense of Hadamard [14].
The inverse problem, instead, aims to identify causes from eﬀects. In
practice, this may be done by using observed data to estimate parameters
in the functional form of a model. Usually an inverse problem is ill-posed
because some the properties related to existence, uniqueness, and stability
fail to hold. When this happens, it is crucial to identify a suitable numerical
scheme that ensures the convergence to the solution.
The literature is rich in papers studying ad hoc methods to address ill-
posed inverse problems by minimizing a suitable approximation error along
with utilizing some regularization techniques [6, 15, 19, 20]. The Collage-
based approach instead, that has been utilized in this paper, relies on an
extension of the Collage Theorem [1], a consequence of Banach’s ﬁxed point
theorem that has shown its importance to solve inverse problems for ﬁxed
point equations. The Collage Theorem is also the basis of the collage-based
compression algorithm in fractal imaging [1, 12]. It has also been extended
to inverse problems for ordinary diﬀerential equations and their application
to diﬀerent ﬁelds in [7] and for partial diﬀerential equations over solid and
perforated domains in [2, 13].
The results presented in this paper are a further contribution to this
stream of research. We extend the Collage-based algorithm for steady-state
equations by searching for an approximation that not only minimizes the
collage error but also maximizes the entropy and minimize the sparsity. In
this extended formulation, the parameter estimation minimization problem
can be understood as a multiple criteria problem, with three diﬀerent and
conicting criteria: The generalized collage error, the entropy associated with
the unknown parameters, and the sparsity of the set of unknown parame-
ters. We implement a scalarization technique to reduce the multiple criteria
program to a single criterion one, by combining all objective functions with
diﬀerent trade-oﬀweights.
Numerical examples conﬁrm that the collage
method produces good, but sub-optimal, results. A relatively low-weighted
entropy term allows for better approximations while the sparsity term de-
creases the complexity of the solution in terms of the number of elements in
the basis.
The paper is organized as follows: Section 2 recalls some basic deﬁni-
tions in multiple criteria optimization. Section 3 recalls the main ideas of
the Generalized Collage Theorem and how it can be used to solve inverse
problems for steady-state equations. Section 4 presents the notion of entropy
and how this formulation can be adapted to this particular context. Sec-
tion 5 introduces the notion of sparsity and its importance to determine the
2


## Page 3


complexity of the approximation. Section 6 formulates the multiple criteria
model, which Section 7 illustrates some numerical computations. Section 8
presents an application to an inverse problem in population dynamics and
Section 9, as usual, concludes.
2
Basics on Multiple Criteria Optimization
This section focuses on recalling some basic facts in Multiple Criteria Opti-
mization (MCO). In an abstract setting, a ﬁnite-dimensional MCO problem
(see Sawaragi et al., 1985) can be stated as follows:
max
x∈X J(x)
(1)
where (X, ∥· ∥) is a Banach space and J : X →Rp is a vector-valued
functional, and Rp is ordered by the Pareto cone Rp
+. A point x ∈X is
said to be Pareto optimal or eﬃcient if J(x) is one of the maximal elements
of the set of achievable values J(X). Thus a point x is Pareto optimal if
it is feasible and, for any possible x′ ∈X, J(x) ≤Rp
+ J(x′) implies x = x′.
In a more synthetic way, a point x ∈X is said to be Pareto optimal if
(J(x) + Rp
+) ∩J(X) = {J(x)}.
2.1
Scalarization
Among the diﬀerent techniques to reduce an MOP problem to a single cri-
terion model there is, for sure, the scalarization technique. Using a scalar-
ization technique, a multiple objective model can be reduced to a single
criterion problem by summing up all criteria with diﬀerent weights. The
weights in front of each criterion express the relative importance of that
criterion for the Decision Maker. By using this approach, More precisely,
by scalarization an MOP model boils down to:
max
x∈X
p
X
i=1
βiJi(x)
(2)
where β is a vector taking values in the interior of Rp
+, namely β ∈int(Rp
+).
The equivalence between the scalarized problem and the original MOP prob-
lem is complete if the Ji are linear and, by varying β, it is possible to obtain
diﬀerent Pareto optimal points. In the other cases linear scalarization pro-
vides only partial results. Other scalarization methods can be found in the
literature and one which is worth to be mentioned is the Chebyshev scalar-
ization model that can also be used for non-convex problems. Scalarization
can also be applied to problems in which the ordering cone is diﬀerent than
the Pareto one. In this case, one has to rely on the elements of the dual
cone to scalarize the multicriteria problem.
3


## Page 4


2.2
ϵ-constraint method
The second model that is proposed to solve the vector-valued problem is
the ϵ-constraint method. In this methodology one of the objective functions
is optimised using the others as constraints, then they are added to the
constraint part of the model. The method is an hybrid methodology, in fact
for the {Ji}i̸=k, least acceptable levels, ϵi have to be set while the remaining
objective function Jk is optimised. Then the decision maker plays a relevant
role in this model, choosing the objective function to be optimised and
the least acceptable levels for the objective functions added as constraints.
Therefore, the original vector-valued problem can be now written as:
max Jk(x)
(3)
subject to:
 Ji(x) ≥ϵi
i ̸= k
x ∈X
(4)
This method has the advantage of being theorically able to identify
Pareto optimal points also of non-convex problems. However, it also has
two potential drawbacks: The identiﬁed optimal point is only granted to be
weakly Pareto optimal, and the problem might become unfeasible due to
the additional constraints.
2.3
Goal Programming
Another method that can be used to solve vector-valued problems that is
worth to be mentioned is the Goal Programming (or GP approach). Goal
Programming was ﬁrst introduced by Charnes, Cooper, and Ferguson (1955)
and Charnes and Cooper (1961). The innovative idea behind this model is
the determination of the aspiration levels of an objective function.
This
model does not try to ﬁnd an optimal solution but an acceptable one, it
tries to achieve the goals set by the decision maker rather than maximising
or minimising the objective functions. Given a set of ideal goals gi, with
i = 1, . . . , p, chosen by the decision maker, it is possible to re-write the
problem in a GP form:
min
p
X
i=1
θ+
i δ+
i + θ−
i δ−
i
Subject to:



Ji(x) + δ−
i −δ+
i = gi
i = 1, . . . , p
δ−
i , δ+
i ≥0
∀i = 1, . . . , p
x ∈X
(5)
where δ+
i , δ−
i are the positive and negative deviations (slack variables),respectively,
and θ+
i , θ−
i are the corresponding weights.
4


## Page 5


3
Inverse Problems for Steady-State Equations us-
ing the Generalized Collage Theorem
The purpose of this paper is to provide an extended multiple criteria algo-
rithm for the estimation of unknown parameters in steady-state equation
by combining the collage distance, the entropy, and the sparsity of the set
of estimated coeﬃcients. The next Section 8 will illustrate an application
of this approach within the context of population dynamics. Here we recall
some basic facts about the collage-based approach. Before formulating the
inverse problem for a generic family of problems in variational forms, let us
have a quick look how a classical steady-state equation can be reformulated
in such a form. Consider the steady-state equation: Find u such that

−d
dx
 K(x)du
dx(x)

= f(x),
x ∈(0, 1)
u(0) = u(1) = 0
It is well-known that if we take the above model, we multiply both sides by
a test function ξ ∈C1
c ([0, 1]) - the space of all continuous and diﬀerentiable
functions with compact support in [0, 1] - and integrate over [0, 1], the model
can be written as
Z 1
0
K(x)du
dx(x) dξ
dx(x)dx =
Z 1
0
f(x)ξ(x)dx.
If we deﬁne by λ the vector of all unknown coeﬃcients in K and f, the
model boils down to the more compact form:
aλ(u, ξ) = f∗
λ(ξ)
where aλ is a family of bilinear forms deﬁned as
aλ(u, ξ) =
Z 1
0
K(x)du
dx(x) dξ
dx(x)dx
and f∗
λ is a family of linear operators deﬁned as
f∗
λ(ξ) =
Z 1
0
f(x)ξ(x)dx
The steady-state equation can be reformulated as a variational problem for
which existence and uniqueness is guaranteed by the classical Lax-Milgram
theorem and over the space H1
0([0, 1]) of all integrable functions with inte-
grable weak derivative on [0, 1] (see [4] for more details in this).
More in general, if E is an Hilbert space, consider the following variational
equation: Find u ∈E such that
aλ(u, v) = f∗
λ(v),
(6)
5


## Page 6


for any v ∈H, where f∗
λ(v) and aλ(u, v) are families of linear and bilinear
maps, respectively, both deﬁned on an Hilbert space E for any λ ∈Λ. Let
⟨·⟩denote the inner product in E, ∥u∥2 = ⟨u, u⟩and d(u, v) = ∥u−v∥, for all
u, v ∈E. The existence and uniqueness of solutions to this kind of equation
are provided by the classical Lax-Milgram representation theorem (see [4]).
The following theorem presents how to determine the solution to the inverse
problem for the above variational problem. Following our earlier studies of
inverse problems using ﬁxed points of contraction mappings, we shall refer
to it as a “generalized collage method.”
Theorem 1. (Generalized Collage Theorem) [10] Let Λ be a compact subset
of Rn, and suppose that, for any λ ∈Λ, aλ : E × E →R be a family of
bilinear forms and f∗
λ : E →R be a family of linear forms. Furthermore,
suppose that:
1. There exists a constant M = supλ∈Λ Mλ > 0 such that for any λ ∈Λ,
|aλ(u, v)| ≤Mλ∥u∥∥v∥for all u, v ∈E,
2. There exists a constant m = infλ∈Λ mλ > 0 such that for any λ ∈Λ,
|aλ(u, u)| ≥mλ∥u∥2 for all u ∈E.
Then by the Lax-Milgram theorem, then for any λ ∈Λ there exists a
unique vector uλ such that
aλ(uλ, v) = f∗
λ(v)
for all v ∈E. Then, for any u ∈E,
∥u −uλ∥≤
1
mλ
F(λ),
(7)
where
F(λ) =
sup
v∈E, ∥v∥=1
|aλ(u, v) −f∗(v)| = ∥aλ(u, ·) −f∗∥.
(8)
In order to ensure that the approximation uλ is close to a target element
u ∈H, we can, by the Generalized Collage Theorem, try to make the term
F(λ)/mλ as close to zero as possible.
The appearance of the mλ factor
complicates the procedure. However, if infλ∈Λ mλ ≥m > 0 then the inverse
problem can be reduced to the minimization of the function F(λ) on the
space F, that is,
min
λ∈Λ F(λ).
(9)
In the following section we use the abbreviation CD, to denote the function
F(λ).
6


## Page 7


4
The Notion of Entropy
The concept of entropy, as it is now used in information theory, was devel-
oped by C.E. Shannon [18]. Over the years it has been used in diﬀerent areas
and applications in various scientiﬁc disciplines. In his article, Shannon in-
troduces the concept of information of a discrete random variable with no
memory as a functional that quantiﬁes the uncertainty of a random variable.
The concept of entropy describes the level of information associated with an
event. More precisely, the deﬁnition of Shannon’s entropy [18, 5] satisﬁes
the following properties:
• The measure is continuous and by changing the value of one of the
probabilities by a very small amount should only produce a small
change of the entropy;
• If all the outcomes are equally likely, then entropy should be maximal.
• If a certain outcome is a certainty, then the entropy should be zero.
• The amount of entropy should be the same independently of how the
process is regarded as being divided into parts.
According to these desiderata, Shannon deﬁnes the entropy in terms of
a discrete random variable X, with possible outcomes x1, ..., xn as:
ENT(X) = −
n
X
i=1
p(xi) ln(p(xi))
(10)
For our purposes, this deﬁnition needs to be adapted to deal with a set of
parameters, that can take both positive and negative values. For a set of
parameters λ = {λ1, λ2, ..., λn} the notion of entropy is:
ENT(λ) = −
n
X
1
|λi|
λT
ln |λi|
λT
(11)
where λT = P
i |λi|.
In the sequel, rather than maximizing the entropy
term - that represents the total amount of information associated with that
particular combination of parameters’ values - we will consider the mini-
mization of its opposite, also known as neg-entropy. This criterion will be
included in the multiple criteria model illustrated in the following Section
6.
5
The Notion of Sparsity
In literature the notion of sparsity has been widely used to reduce the com-
plexity of a model by taking into in consideration only those parameters
7


## Page 8


whose values have major impact on the solution. In other words, by adding
this term we wish to determine solutions that are “simple”, or more pre-
cisely sparse. We say that a real vector x in Rn is sparse, when most of
the entries of x vanish. We also say that a vector x is s-sparse if it has at
most s nonzero entries. This is equivalent to say that the ℓ0-pseudonorm,
or counting norm, deﬁned as
∥λ∥0 = #{i : λi ̸= 0}
(12)
is at most s.
The ℓ0-pseudonorm is a strict sparsity measure, and most
optimization problems based on it are combinatorial in nature, and hence in
general NP-hard. To overcome these diﬃculties, it is common to replace the
function with relaxed variants or smooth approximations that measure and
induce sparsity. One possible variant is to use the ℓ1 norm instead, which is
a convex surrogate for the ℓ0, deﬁned as
∥λ∥1 =
n
X
i=1
|λi|
(13)
It is also the best surrogate in the sense that the 1 ball is the smallest
convex body containing all 1-sparse objects of the form ei (see [3]). Another
possibility is to replace the ℓ0 pseudonorm with some approximation, as for
instance
∥λ∥∗=
n
X
i=1
max{e−αλi, eαλi}
(14)
or
∥λ∥∗∗=
n
X
i=1
[max{e−αλi, eαλi}]2
(15)
for a given α > 0. It is worth noticing that ∥λ∥∗∗is a C1,1 or LC1 function
(continuous with Lipschitz gradient).
6
The Model
We now propose a new collage-based approach for solving inverse problems
based on Multiple Criteria Optimization which combines together the Col-
lage Distance, the Entropy, and the Sparsity. Then we consider the following
criteria to be maximized/minimized simultaneously:
• CD(λ) is the Collage Distance, to be minimized over λ ∈Λ. This
criterion describes the accuracy of the approximation;
• ENT(λ) is the Entropy, to be maximized over λ ∈Λ. This criterion
models the amount of information carried by the parameters’ model;
8


## Page 9


• SP(λ) is the Sparsity, to me minimized over λ ∈Λ. This criterion
instead describes the complexity of the solution in terms of number of
elements in the basis to be utilized to approximate the target.
It is worth noticing that these three criteria are, in general, conﬂicting.
It is clear that by reducing the sparsity criterion SP(λ), this will negatively
aﬀect the CD(λ) as less elements in the basis are available to construct
the solution. To observe that the Entropy ENT(λ) and the Sparsity SP(λ)
criteria are also conﬂicting, let us take a simple example where X is a random
variable with only two possible outcomes x1 and x2 with probabilities p and
1 −p, respectively. It is clear that if p increases, and then 1 −p decreases,
x1 gets more and more likely to happen. This would produce a decrement
in ENT(X) while the sparsity of the vector (x1, x2) would increase (see also
[16] for a nice discussion on the importance of the concepts of entropy and
sparsity).
By introduction the neg-entropy −ENT, the multiple criteria
model can be formulated as a minimization program as follows:
min
λ∈Λ(CD(λ), −ENT(λ), SP(λ))
(16)
This multiple criteria problem can be transformed into a single criterion
model by using one the approaches presented above. In particular, one can
construct the following single-criterion models:
Model 1: We scalarize the model by introducing three diﬀerent positive
weights, namely η1, η2, η3. The scalarized model boils down to:
min
λ∈Λ η1CD(λ) −η2ENT(λ) + η3SP(λ)
The next section shows how the method works for diﬀerent combinations of
the weights.
Model 2: We move two out of three criteria into the constraints. Then
Model 2 reads as:
min CD(λ)
Subject to:



λ ∈Λ
−ENT(λ) ≤ϵ1
SP(λ) ≤ϵ2
Model 3: In the GP formulation, let us g1, g2, g3 be the goals of CD(λ),
ENT(λ), SP(λ) respectively. Then Model 3 reads as:
min
3
X
i=1
θ+
i δ+
i + θ−
i δ−
i
9


## Page 10


Subject to:











λ ∈Λ
CD(λ) + δ−
1 −δ+
1 = g1
−ENT(λ) + δ−
2 −δ+
2 = g2
SP(λ) + δ−
3 −δ+
3 = g3
δ−
i , δ+
i ≥0
∀i = 1, . . . , 3
(17)
7
A Computational Study
To show the implementation of the algorithm, consider the following steady-
state equation:

−d
dx
 K(x)du
dx(x)

= f(x),
x ∈(0, 1)
u(0) = u(1) = 0
with true u(x) = x −x2, dK(x) = 1 + 3x, and f(x) = −12x + 1.
The
following tables show the result of our parameter estimation technique. Here
we implement Model I presented in the previous section, Models II and III
can be implemented similarly.
Let us recall that η1 is the coeﬃcient of
generalized collage distance, η2 is the coeﬃcient of entropy criterion, η3 is
the coeﬃcient of the sparsity criterion. In the following tables, we denote
by CD the value of the minimal general collage distance, by ENT the value
of the minimal entropy, and by SP the value of minimal sparsity. ER is
the L2 distance between the true k(x) and the recovered k(x). We work
with overlapping ”hat” bases, the ﬁrst with 11 interior elements, the second
with 23 interior elements, so every other element in the ﬁner basis has the
same peak point as an element from the coarser basis. We include the ”half
hats” at each end, as well, since we recover K(x) in these bases and K(x)
is nonzero at the endpoints. So, in total there are 11 + 23 + 38 elements.
In particular, the following Table 4 considers the eﬀects of all three criteria
simultaneously. This table shows how the three criteria interact diﬀerently
when the three weights vary.
Table 1: CD versus ENT
η1
η2
η3
CD
ENT
SP
ER
1.0
0.0
0
0.0000000000000000000
−5.258363
38
0.12553297515980
0.9
0.1
0
0.0000001334065773123
−13.843577
38
0.04686792274056
0.8
0.2
0
0.0000006753359361650
−13.843580
38
0.04687624208382
0.7
0.3
0
0.0000019845290201299
−13.843584
38
0.04688698216096
0.6
0.4
0
0.0000078272526691447
−13.525527
38
0.20963394909766
0.5
0.5
0
0.0000108023649479836
−13.843597
38
0.04692168077792
0.4
0.6
0
0.0000243008103020118
−13.843607
38
0.04695245397844
0.3
0.7
0
0.0000587837869956570
−13.843625
38
0.04700459363829
0.2
0.8
0
0.0001726457353481080
−13.843661
38
0.04711204428741
0.1
0.9
0
0.0008724077594118485
−13.843769
38
0.04745936241855
0.0
1.0
0
118740.8284896594930938881
−13.979419
38
15.91754842300381
10


## Page 11


Figure 1: Hat basis with 11 elements
Figure 2: Hat basis with 23 elements
11


## Page 12


Table 2: CD vs sparsity
η1
η2
η3
CD
ENT
SP
ER
1.0
0
0.0
0.0000000000000000000
−5.258363
38
0.12553297515980
0.9
0
0.1
0.0005639498502964314
−8.116850
33
2.70901013729197
0.8
0
0.2
0.0000000000000000000
−8.808666
31
3.19468535484908
0.7
0
0.3
0.0000000000000000009
−6.252997
26
1.03475376421398
0.6
0
0.4
0.0042233007356215981
−6.375100
32
1.53269905190502
0.5
0
0.5
0.0000000000000000000
−7.665059
29
2.71407610080125
0.4
0
0.6
0.0000000000000000000
−5.906960
32
0.00000000000000
0.3
0
0.7
0.0065716738513130884
−4.777920
28
0.98261846051097
0.2
0
0.8
0.0000000000000000000
−5.914810
27
1.94905796188513
0.1
0
0.9
0.5203345122050530642
−5.935058
30
2.53646236821924
0.0
0
1.0
4111.1111111111111111111
−0.000000
0
2.64575131106459
Table 3: CD versus SP. Add another set of even ﬁner basis elements,
also sharing peak points with the other bases, for a total of 87 elements.
η1
η2
η3
CD
ENT
SP
ER
1.0
0
0.0
0.0000000000000000000
−8.432182
87
0.10275834304913
0.9
0
0.1
0.0000000000000000000
−9.285139
37
0.00000000000000
0.8
0
0.2
0.0000000000000000000
−8.582890
35
0.00000000000000
0.7
0
0.3
0.0000000000000000000
−8.052108
32
0.00000000000000
0.6
0
0.4
0.0000000000000000000
−7.115012
39
0.00000000000000
0.5
0
0.5
0.0000000000000000000
−4.397848
20
0.00000000000000
0.4
0
0.6
0.0000000000000000000
−8.002280
28
0.00000000000000
0.3
0
0.7
0.0000000000000000000
−7.709068
29
0.00000000000000
0.2
0
0.8
0.0000000000000000000
−5.204042
22
0.00000000000000
0.1
0
0.9
0.0000000000000000000
−7.699073
28
0.00000000000000
0.0
0
1.0
4855.6857638888888888889
−0.000000
0
2.64575131106459
Table 4: How the three criteria interact
η1
η2
η3
CD
ENT
SP
ER
0.96
0.02
0.02
0.0000005845708580369
−30.713841
87
1.35681152916365
0.38
0.02
0.60
0.0020363227800240392
−20.407920
79
0.07009496798767
0.58
0.02
0.40
0.0000007665555795281
−15.963332
85
0.00008905869569
8
An Application to Population Dynamics
Population dynamics is an extremely important ﬁeld and it is the basis of
many economic models. Recently a lot of attention has been devoted to a
new stream of research, called Economic Geography, that aims at under-
standing the evolution of population over space and time and the eﬀects
of migration ﬂows on economies. A spatial population model can be for-
mulated as follows: Given a compact interval [xa, xb] ⊂R, consider the
12


## Page 13


Figure 3: True (K,u) vs Estimated (K,u),ent=0.02,sp=0.02
Figure 4: True (K,u) vs Estimated (K,u),ent=0.02,sp=0.6
Figure 5: True (K,u) vs Estimated (K,u),ent=0.02,sp=0.4
13


## Page 14


following diﬀerential model with Dirichlet boundary conditions on [xa, xb]:



∂P (x,t)
∂t
= ∇(dP (x)∇P(x, t)) + A(x),
(x, t) ∈(xa, xb) × (0, +∞)
P(x, t) = PM,
x ∈{xa, xb}
P(x, 0) = P0(x).
x ∈[xa, xb]
where P(x, t) is the population level at time t in location x, P0(x) is the ini-
tial distribution of population, and A(x) is an exogenous ﬂow of population.
For simplicity, we also suppose that P(x, t) is equal to a constant value PM
at xa and xb and over time. The steady-state level of population ˜P is the
unique solution to the model
(
−∇

dP (x)∇˜P(x)

= A(x),
x ∈(xa, xb)
˜P(x) = PM,
x ∈{xa, xb}
Let us consider the following numerical example where xa = 0, xb = 1,
dP (x) = x + 1, PM = 1, and A(x) = 4x + 1. In this case the true solution
is P(x) = x −x2 + 1.
Figure 6: Evolution of P
The following tables present the results for inverse problem instead. The
ﬁrst table shows the results with no noise added, 9 interior data points,
11+23=34 interior basis functions. The second table, instead, reports the
result of the algorithm with 1% relative noise added to data.
14


## Page 15


η1
η2
η3
CD
ENT
SP
ER
1.0000000
0.0000000
0.0000000
0.00000000000000
-3.817973
38
0.08124517
0.9990000
0.0010000
0.0000000
0.00000000000351
-13.935231
38
0.02629649
0.9000000
0.1000000
0.0000000
0.00000004336279
-13.935232
38
0.02630015
0.8000000
0.2000000
0.0000000
0.00000021951333
-13.935233
38
0.02630479
0.4000000
0.6000000
0.0000000
0.00000789898350
-13.935242
38
0.02634729
0.1000000
0.9000000
0.0000000
0.00028361315324
-13.935294
38
0.02663119
0.9999000
0.0000000
0.0001000
0.00000000343665
-4.083520
34
0.385780654
0.9600000
0.0200000
0.0200000
0.00000000152452
-13.935231
38
0.026297154
0.7800000
0.0200000
0.2000000
0.00000224173370
-6.525117
38
1.139612982
0.5800000
0.0200000
0.4000000
0.00000282419676
-5.958487
37
0.382813679
η1
η2
η3
CD
ENT
SP
ER
1.0000000
0.0000000
0.0000000
0.00000000000000
-3.925169
38
0.248001091
0.9990000
0.0010000
0.0000000
0.00000000000422
-13.934251
38
0.22401013
0.9000000
0.1000000
0.0000000
0.00000005211046
-13.934252
38
0.22400520
0.8000000
0.2000000
0.0000000
0.00027783818395
-4.462927
38
0.292032117
0.4000000
0.6000000
0.0000000
0.00994433112542
-4.473986
38
0.295136541
0.1000000
0.9000000
0.0000000
0.34642831463774
-4.538449
38
0.316445908
0.9999000
0.0000000
0.0001000
0.00000000369833
-3.272674
32
0.377684011
0.9600000
0.0200000
0.0200000
0.00000000183208
-13.934251
38
0.22400924
0.7800000
0.0200000
0.2000000
0.00000144023205
-5.710676
38
0.790857843
0.5800000
0.0200000
0.4000000
0.00000012701174
-11.825482
38
2.07316956
9
Conclusion
The analysis of inverse problems for dynamical systems driven by diﬀerential
equation is a crucial area in applied science. In fact, in practical applications,
it is relevant to be able to estimate the unknown parameters of a given
equation starting from samples of the solution collected by experiments or
observations. In this paper we have extended a previous algorithm, based
on the so-called ”Collage Distance”, to estimate the unknown parameters
of steady-state equations. This extended version also includes the notion
of entropy and the notion of sparsity and it is modelled as a multicriteria
model.
These three criteria are conﬂicting by nature, as a increment in
precision usually implies an increment in sparsity. We have solved the model
using a scalarization technique with diﬀerent weights and conducted several
numerical experiments to show how the method works practically.
References
[1] Barnsley M, Fractals Everywhere, Academic Press, New York, 1989.
15


## Page 16


[2] M.I. Berenguer, H. Kunze, D. La Torre, M. Ruiz Gal´an, Galerkin method
for constrained variational equations and a collage-based approach to
related inverse problems, J. Comput. Appl. Math. 292 (2016), 67–75.
[3] E. J. Cands (2014), Mathematics of sparsity (and a few other things),
Proceedings of the International Congress of Mathematicians, Seoul,
South Korea, 2014.
[4] L.C. Evans (2010), Partial Diﬀerential Equations, Graduate Studies in
Mathematics, American Mathematical Society.
[5] F. Flores Camachoa, N. Ulloa Lugob, H. Covarrubias Martneza (2015),
The concept of entropy, from its origins to teachers, Revista Mexicana
de Fsica E 61, 69–80.
[6] A. Kirsch, An introduction to the mathematical theory of inverse prob-
lems, Springer, 2011.
[7] Kunze H and Vrscay E R, Solving inverse problems for ordinary diﬀeren-
tial equations using the Picard contraction mapping, Inverse Problems
15 (1999) 745–770.
[8] Kunze H and Gomes S, Solving An Inverse Problem for Urison-type Inte-
gral Equations Using Banach’s Fixed Point Theorem, Inverse Problems
19 (2003) 411–418.
[9] Kunze H, Hicken J and Vrscay E R, Inverse Problems for ODEs Us-
ing Contraction Maps: Suboptimality of the “Collage Method”, Inverse
Problems 20 (2004) 977–991.
[10] Kunze H, La Torre D and Vrscay E R, A generalized collage method
based upon the Lax–Milgram functional for solving boundary value in-
verse problems, Nonlinear Anal. 71 12 (2009) e1337–e1343.
[11] Kunze H, La Torre D, Vrscay E R, Solving inverse problems for DEs
using the collage theorem and entropy maximization, Applied Mathe-
matics Letters, 25 (2012), 2306-2311.
[12] Kunze H, La Torre D, Mendivil F and Vrscay E R, Fractal-based meth-
ods in analysis, Springer, 2012.
[13] Kunze H and La Torre D, Collage-type approach to inverse problems for
elliptic PDEs on perforated domains, Electronic Journal of Diﬀerential
Equations, 48, 2015.
[14] J. Hadamard, Lectures on the Cauchy problem in linear partial diﬀer-
ential equations, Yale University Press, 1923.
16


## Page 17


[15] F.D. Moura Neto, A.J. da Silva Neto, An Introduction to Inverse Prob-
lems with Applications, Springer, New York, 2013.
[16] G. Pastor, I. Mora-Jimenez, R. Jantti, and A.J. Caamano (2013), Math-
ematics of Sparsity and Entropy: Axioms, Core Functions and Sparse
Recovery, Proceedings of the Tenth International Symposium in Wireless
Communication Systems (ISWCS 2013).
[17] Sawaragi, Y., Nakayama, H., Tanino, T. (1985). Theory of multiobjec-
tive optimization (Academic Press, Inc.)
[18] C.E. Shannon (1948), A Mathematical Theory of Communication, Bell
System Technical Journal, 27 (3), 379423.
[19] A.N. Tychonoﬀ, N.Y. Arsenin, Solution of Ill-posed Problems, Wash-
ington: Winston & Sons, 1977.
[20] C.R. Vogel, Computational Methods for Inverse Problems, SIAM, New
York, 2002.
17

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1911_02799v1_solving_inverse_problems_for_steady_state_equations_using_a_multiple_criteria_mo
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1911_02799V1_SOLVING_INVERSE_PROBLEMS_FOR_STEADY_STATE_EQUATIONS_USING_A_MULTIPLE_CRITERIA_MO.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

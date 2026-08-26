---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.08247v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1911.08247v1_A_Multicriteria_Macroeconomic_Model_with_Intertemporal_Equity_and_Spatial_Spillo

> Source: 1911.08247v1_A_Multicriteria_Macroeconomic_Model_with_Intertemporal_Equity_and_Spatial_Spillo.pdf

> Pages: 14

---


## Page 1


A Multicriteria Macroeconomic Model with
Intertemporal Equity and Spatial Spillovers
Herb Kunze∗
Davide La Torre†
Simone Marsiglio‡
November 20, 2019
Abstract
We analyze a macroeconomic model with intergenerational equity considerations and spatial spillovers,
which gives rise to a multicriteria optimization problem. Intergenerational equity requires to add in the
deﬁnition of social welfare a long run sustainability criterion to the traditional discounted utilitarian cri-
terion. The spatial structure allows for the possibility of heterogeneiity and spatial diﬀusion implies that
all locations within the spatial domain are interconnected via spatial spillovers. We rely on diﬀerent tech-
niques (scalarization, ϵ-constraint method and goal programming) to analyze such a spatial multicriteria
problem, relying on numerical approaches to illustrate the nature of the trade-oﬀbetween the discounted
utilitarian and the sustainability criteria.
Keywords: Multicriteria Optimization; Intergenerational Equity; Spatial Diﬀusion
1
Introduction
After decades of debates a wide consensus on the eﬀects of anthropogenetic activities on the environment has
ﬁnally emerged, and even policymakers seem ﬁnally convinced that it is now time to act in order to ensure
the long term sustainability of economic activities. Sustainability is a complicated notion to deﬁne but
in its most widely accepted terms it requires some respect of natural resources and some eﬀorts to ensure
intergenerational equity ([30]).
While the former aspect can be easily accounted for in macroeconomic
analysis by adding an additional constraint to the standard optimization problem representing the society’s
planning device, the latter is more problematic since the criterion generally used in the deﬁnition of such a
problem, the discounted utilitarianism, attaches less and less weight to future generations and so it cannot
accommodate for intergenerational issues ([13]). Diﬀerent approaches to overcome such an issue have been
proposed, but probably the most commonly used consists of extending the objective function to include an
additional term representing somehow long term sustainablity considerations ([12]). The introduction of such
an additional term in the optimization problem makes it a multiple objective problem in which the society
needs to balance two conﬂicting goals, represented by short term and long term objectives, respectively; such
an interpretation of a macroeconomic problem as a multicriteria problem allows to rely upon the operations
research methods to analyze macroeconomic issues, bridging somehow these two important but distinct ﬁelds
of research ([21]; [22]).
The goal of this paper is therefore to analyze from an operations research perspective a traditional
macroeconomic model extended along two diﬀerent directions. The ﬁrst consists of allowing for long term
sustainability considerations, in the form of intertemporal equity issues, which introduces a second criterion
in the otherwise standard unicriterion macroeconomic optimization problem; several studies have analyzed
∗Department of Mathematics and Statistics, University of Guelph, Guelph, Canada. Email: hkunze@uoguelph.ca
†SKEMA Business School - Universit´e Cˆote d’Azur, Sophia Antipolis Campus, France. Email: davide.latorre@skema.edu
‡Department of Economics and Management, University of Pisa, Pisa, Italy. Email: simone.marsiglio@unipi.it
1
arXiv:1911.08247v1  [econ.TH]  19 Nov 2019


## Page 2


in diﬀerent contexts problems of this kind by focusing on pollution control and debt reduction settings ([17];
[19]). The second consists of allowing for a spatial dimension in which diﬀerent locations within the entire
economy interact one another through the trade channel; several studies analyze problems of this kind,
which generally are all unicriterion, by focusing on capital accumulation and environmental problems ([16];
[18]). Speciﬁcally, we consider a simple setting with intergenerational equity (as in [13]) in which capital
evolves both over time and across space (as in [3]), and to the best of our knowledge our paper represents
the ﬁrst attempt to analyze a spatial macroeconomic problem from an operational research point of view.
Our paper relates thus to two very distinct literatures addressing the intertemporal equity issues as-
sociated with sustainabiility and the existence of spatial spillovers in macroeconomic geography contexts,
respectively. Several papers discuss the problems embedded in the use of discounted utilitarianism as a social
welfare criterion by proposing alternative criteria and discussing their limits in terms of applicability and
in terms of existence of optimal solution paths ([26]; [11]; [23]; [20]; [2]; [14]). Several other papers instead
more recently discuss how the presence of a spatial dimension allows to characterize the possibility of spatial
heterogeneity and spatial spillovers, along with their implications for macroeconomic outcomes ([6]; [3]; [7];
[8]; [16]). We bridge these two branches of the economics literature by developing a spatial version of the
simplest intertemporal equity problem to show how an operations research approach can be used to inform
our analysis.
The paper proceeds as follows. Section 2 recalls the basic deﬁnitions and properties of optimization
theory with multiple objectives, discussing the main methods that we shall adopt in our analysis, that
are scalarization, ϵ-constraint method and goal programming. Section 3 presents our multicriteria problem
showing how it can be reformulated from the points of view of scalarization, ϵ-constraint method and goal
programming. Section 4 determines the solution of the problem relying on scalarization illustrating the
nature of the trade-oﬀbetween the discounted utilitarian and the sustainability criteria and deriving the
Pareto-frontier in a speciﬁc model’s parametrization. Section 5 presents some further numerical experi-
ments by analyzing the problem via the ϵ-constraint method and goal programming, under diﬀerent model’s
parametrizations. Section 6 as usual concludes.
2
Preliminaries on Multiple Objective Optimization
This section recalls some basic facts in Multiple Objective Optimization (MOP). In a very abstract setting,
a ﬁnite-dimensional MOP problem (see [27]) takes the form
max
x∈X J(x)
(1)
where (X, ∥· ∥) is a Banach space and J : X →Rp is a vector-valued functional. As usual we suppose that
Rp is ordered by the classical Pareto cone Rp
+. A point x ∈X is said to be Pareto optimal or eﬃcient if
J(x) is one of the maximal elements of the set of achievable values J(X). Thus a point x is Pareto optimal
if it is feasible and, for any possible x′ ∈X, J(x) ≤Rp
+ J(x′) implies x = x′. In a more synthetic way, a
point x ∈X is said to be Pareto optimal if (J(x) + Rp
+) ∩J(X) = {J(x)}. Because of its dimensionality
and the existing of conﬂicting criteria, a MOP model is usually diﬃcult to be solved and the determination
of the entire or part of the Pareto frontier can be very complicated and computationally intensive.
In
particular this applies when the number of objectives is larger than two, leading to a higher-dimensional
Pareto surface.
To overcome this diﬃculties and reduce the model complexity, several techniques have
been proposed in literature. The generation of the Pareto frontier can be accomplished through one of two
predominant techniques: scalarization and vectorization methods. Among the scalarization techniques, the
most frequently applied are linear scalarization, the ϵ-constraint method, and goal programming. These
techniques will be used in the sequel of this paper. The vectorization algorithms, instead, tackle the MOP
model directly without transforming it into some equivalent single criterion model.
2


## Page 3


2.1
Linear Scalarization
The linear scalarization technique (or weighted sum) is probably the simplest and the most widely used
technique to solve MOP problems and it converts the MOP model into a family of parametric single criterion
optimization models. By using this approach, a multiple objective model can be reduced to a single criterion
problem by summing up all criteria with diﬀerent weights. More precisely, by linear scalarization a MOP
model boils down to:
max
x∈X
p
X
i=1
βiJi(x)
(2)
where β is a vector taking values in the interior of Rp
+, namely β ∈int(Rp
+). Since the Pareto optimal
solution depends on β, by modifying the weights β diﬀerent points on the Pareto optimal set can be found.
Linear scalarization can also be applied to problems in which the ordering cone is diﬀerent from the Pareto
one. In this case, we have to rely on the elements of the dual cone to scalarize the problem.
If J is a vector-valued concave functional, namely each component Ji is concave, then the linear scalarized
problem (2) is also concave. This means that one can ﬁnd Pareto optimal points of a concave problem by
solving a concave scalar optimization problem, and for each β ∈int(Rp
+), diﬀerent Pareto optimal points can
be obtained. For concave problems the converse of this result is only partially true, since for each Pareto
optimal point ¯x, there is a nonzero ¯β ∈Rp
+ such that ¯x is a solution of the scalarized problem (2) with
β = ¯β. This is stated in the following theorem.
Proposition 1. ([27]) Suppose that D is convex and Ji are concave for all i = 1...p. Then for all Pareto
optimal solutions ¯x there exists β ∈Rp
+ such that
¯x ∈argmaxx∈D
( p
X
i=1
βiJi(x)
)
.
(3)
If the linear scalarization method is used for non-concave problems, the Pareto frontier generated will
be incomplete and the Decision Maker (DM) will have a non-complete set of possible solutions. In this
case, other scalarization methods can be found in literature and one which is worth to be mentioned is the
Chebyshev scalarization model.
2.1.1
ϵ-constraint method
The second model that is proposed to solve the vector-valued problem is the ϵ-constraint method. In this
method, one of the objective functions is selected to be optimized while the others are converted into
additional constraints.
The method is an hybrid methodology, in fact for the {Ji}i̸=k, least acceptable
levels, ϵi have to be set while the remaining objective function Jk is optimized. Then the decision maker
plays a crucial role in this setting, by choosing which objective function to optimize and the least acceptable
levels for the objective functions to add as constraints.
Under this method, the original vector-valued
problem can be now written as:
max Jk(x)
(4)
subject to:
(
Ji(x) ≥ϵi
i ̸= k
x ∈X
(5)
This method has the advantage of being theoretically able to identify Pareto optimal points also of non-
convex problems. However, it also has two potential drawbacks: the identiﬁed optimal point is only granted
to be weakly Pareto optimal, and the problem might become unfeasible due to the additional constraints.
3


## Page 4


2.2
Goal Programming
The Goal Programming (or GP approach) is another widely used method to deal with vector-valued problems
(see [9] [10]). With respect to other scalarization techniques, the idea behind this model is the determination
of the aspiration levels of an objective function. A GP model does not try to ﬁnd an optimal solution but
an acceptable one, as it tries to achieve the goals set by the DM rather than maximizing or minimizing the
objective functions. However, an optimization procedure is involved anyway. Within this formulation, one
tries to minimize any possible deviation from the objective goals, either positive or negative. In fact, the GP
model is a distance-function model in which the obtained optimal solution represents the best compromise
between diﬀerent objectives. Since the introduction of this methodology for MOP problems, many variants
have been presented in literature. Among them, the most popular one is the Weighted Goal Programming
([1]) which reads as follows: Given a set of ideal goals gi, with i = 1, . . . , p, chosen by the DM, solve the
following program:
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



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
(6)
where δ+
i , δ−
i
are the positive and negative deviations (slack variables), respectively, and θ+
i , θ−
i
are the
corresponding weights.
Due to its simplicity, the GP model and its variants have been widely applied
to diﬀerent areas such as accounting, marketing, human resources, production, and so on.
A negative
counterpart of the GP model, that it is important to consider, is the ability of GP to produce solutions that
are not Pareto eﬃcient. To overcome this diﬃculty, in order to produce Pareto optimal solutions the GP
model is implemented within a two-steps algorithm: At ﬁrst, the GP solution is tested for Pareto eﬃciency
and, if it is not eﬃcient, a restoration or projection method is proposed to restore eﬃciency at the second
step.
3
The Model
The simplest macroeconomic setting to account for intergenerational equity ([21]; [22]) and spatial links
and spillovers ([6]; [3]) consists of an optimization problem in which the social planner, by considering the
evolution of the capital stock K(x, t), tries to determine the optimal level of consumption C(x, t) over time
t ∈[0, T] and across space x ∈Ωto maximize the vector-valued social welfare which is composed of two
terms. The ﬁrst term represents the discounted utility stream of the representative individuals located in
diﬀerent venues within the entire spatial economy J1 =
R T
0
R
ΩU(C(x, t))e−ρtdxdt, where the utility function
depends on consumption and the discount factor is ρ > 0. The second term represents the payoﬀof the
representative individuals located in diﬀerent venues within the entire spatial economy at the end of the
planning horizon, J2 =
R
ΩK(x, T) where the payoﬀfunction depends on the ﬁnal capital level. The society’s
optimization problem can therefore be stated as a bi-criteria problem as follows:
max
C(x,t) W =
Z T
0
Z
Ω
U(C(x, t))e−ρtdxdt,
Z
Ω
K(x, T)dx

(7)
Subject to





∂K(x,t)
∂t
= ∇(d(x)∇K(x, t)) + f(K(x, t), C(x, t)),
(x, t) ∈Ω× (0, T)
d(x) ∂K
∂n (x) = 0,
x ∈∂Ω
K(x, 0) = K0(x).
x ∈Ω
(8)
4


## Page 5


where the spatio-temporal evolution of capital in (15) is driven by the functions f(K(x, t), C(x, t)) with
fK > 0 and fC < 0, and ∇(d(x)∇K(x, t)) which quantiﬁes the process of spatial diﬀusion between diﬀerent
locations within the spatial domain. Note that the function f(K(x, t), C(x, t)) determines the nature of
the trade-oﬀbetween the two terms in (7). The ﬁrst term represents the traditional criterion considered in
macroeconomic analysis, characterizing the short termism of policymaking which leads the society to care
about the wellbeing of the current generation. The second term represents instead a sustainability criterion
introduced to account for the wellbeing of future generations by allowing the society to determine today how
many resources not to exploit in order to preserve them for the future. Clearly, a higher consumption today
increases the ﬁrst criterion and through its subtraction of resources to capital accumulation decreases the
second one. Therefore, the society needs to balance these two conﬂicting criteria determining the optimal
dynamic path of consumption.
The above maximization has to be understood in a Pareto sense and with respect to the Pareto or-
der in R2:
Given a, b ∈R2, a ≤b if and only if ai ≤bi, i = 1, 2.
So, in other words, a feasible
pair ( ¯K(x, t), ¯C(x, t)) that solves (15) is optimal if there is no other feasible pair (K(x, t), C(x, t)) such
that(J1(K(x, t), C(x, t)), J2(K(x, t), C(x, t))) dominates (J1( ¯K(x, t), ¯C(x, t)), J2( ¯K(x, t), ¯C(x, t))). This can
be rewritten by stating that there exists no feasible (K(x, t), C(x, t)) such that
(J1( ¯K, ¯C), J2( ¯K, ¯C)) ∈(J1(K, C), J2(K, C)) + int(R2).
Using the three approaches presented in the previous section to reduce a multiple objective problem to a
single objective model, we can deﬁne the following three diﬀerent single-criterion formulations.
3.1
Model I
In this ﬁrst fomulation the two criteria are combined together through scalarization weights. The DM decides
the value of a trade-oﬀparameter Θ ∈(0, 1), that expresses the relative importance of ﬁrst criterion with
respect to the second one. The parameter Θ is then expressing the level of priority and preference that each
criterion has for the DM. The scalarized problem reads as
max JΦ(C, K) := (1 −Φ)J1(C, K) + ΦJ2(C, K)
Subject to



∂K(x,t)
∂t
= ∇(d(x)∇K(x, t)) + f(K(x, t), C(x, t)),
(x, t) ∈Ω× (0, T)
d(x) ∂K
∂n (x) = 0,
x ∈∂Ω
K(x, 0) = K0(x).
x ∈Ω
where
J1(C, K) =
Z T
0
Z
Ω
U(C(x, t))e−ρtdxdt
and
J2(C, K) =
Z
Ω
K(x, T)dx
If we replace Θ =
Φ
1−Φ then the objective function boils down to:
max JΘ(C, K) := J1(C, K) + ΘJ2(C, K)
We will see in the following section dedicated to a numerical simulation that, by varying over Θ ∈(0, +∞),
it is possible to reconstruct the Pareto frontier. In fact the objective function is concave in (C, K) for any
Θ ∈(0, +∞).
5


## Page 6


3.2
Model II
In this second formulation we proceed by using the ϵ-constraint method. Within this approach there are
essentially two diﬀerent formulations that can be proposed, once again this decision being dependent on
the relative importance of each criterion for the DM. If DM considers the intertemporal utility as the main
criterion and supposes that a certain level ϵ of the criterion has to be attained, the model boils down to:
max Jϵ(C, K) :=
Z T
0
Z
Ω
U(C(x, t))e−ρtdxdt
(9)
Subject to









R
ΩK(x, T)dx ≥ϵ,
∂K(x,t)
∂t
= ∇(d(x)∇K(x, t)) + f(K(x, t), C(x, t)),
(x, t) ∈Ω× (0, T)
d(x) ∂K
∂n (x) = 0,
x ∈∂Ω
K(x, 0) = K0(x).
x ∈Ω
(10)
By varying ϵ it is possible to obtain diﬀerent points of the Pareto frontier. If, instead, the DM is more
interested in the sustainability criterion, the model can be written as
max Jϵ(C, K) :=
Z
Ω
K(x, T)dx
(11)
Subject to









R T
0
R
ΩU(C(x, t))e−ρtdxdt ≥ϵ,
∂K(x,t)
∂t
= ∇(d(x)∇K(x, t)) + f(K(x, t), C(x, t)),
(x, t) ∈Ω× (0, T)
d(x) ∂K
∂n (x) = 0,
x ∈∂Ω
K(x, 0) = K0(x).
x ∈Ω
(12)
3.3
Model III
In this third formulation we rely on a GP approach.
Let us suppose that g1 and g2 are the two goals
associated with the two criteria J1 and J2, respectively. Within this technique, the DM is not interested in
the maximization process tout court, but instead in the achievement levels of the two criteria J1 and J2.
The previous model, reformulated using the GP technique, reads as
min Jg1,g2 :=
2
X
i=1
θ+
i δ+
i + θ−
i δ−
i
Subject to













R
ΩK(x, T)dx −δ+
1 + δ−
1 = g1
R T
0
R
ΩU(C(x, t))e−ρtdxdt −δ+
2 + δ−
2 = g2,
∂K(x,t)
∂t
= ∇(d(x)∇K(x, t)) + f(K(x, t), C(x, t)),
(x, t) ∈Ω× (0, T)
d(x) ∂K
∂n (x) = 0,
x ∈∂Ω
K(x, 0) = K0(x).
x ∈Ω
(13)
4
Computational Results
In this section we present a numerical implementation of Model I introduced above and we determine an
approximation of the Pareto frontier. The next section, instead, will present other possible numerical im-
plementations of Models II and III. Before doing that, we specify the components of this model and, in
particular, the form of the function f(K(x, t), C(x, t)).
It is a traditional Ramsey-type optimal control
problem, extendeto account for intergenerational equity issues ([12]; [13]) along with spatial heterogene-
ity and spillovers ([3]; [16]). The economy develops along a linear city and the social planner wishes to
maximize the vector-valued social welfare by choosing the level of consumption in each location, which in
6


## Page 7


turn determines the evolution of capital in each location and in the whole economy. Capital accumulation
depends on the diﬀerence between net (of depreciation, where the depreciation rate is δK > 0) production,
Y (x, t) = AK(x, t)α and consumption, augmented for the inﬂows of capital from other locations; these ﬂows
are captured by a diﬀusion term ∇(d(x)∇K(x, t)), where d(x) is the diﬀusion parameter. Given the initial
condition, K(x, 0) = K0(x), the problem can be summarized as follows:
max
Z T
0
Z
Ω
U(C(x, t))e−ρtdxdt,
Z
Ω
K(x, T)dx

(14)
Subject to





∂K(x,t)
∂t
= ∇(d(x)∇K(x, t)) + AK(x, t)α −δKK(x, t) −C(x, t),
(x, t) ∈Ω× (0, T)
d(x) ∂K
∂n (x) = 0,
x ∈∂Ω
K(x, 0) = K0(x).
x ∈Ω
(15)
We ﬁrst discuss how to solve numerically the scalarized problem:
max JΘ(C, K) := J1(C, K) + ΘJ2(C, K)
Subject to



∂K(x,t)
∂t
= ∇(d(x)∇K(x, t)) + AK(y, t)αdy −C(x, t) −δKK(x, t),
(x, t) ∈Ω× (0, T)
d(x) ∂K
∂n (x) = 0,
x ∈∂Ω
K(x, 0) = K0(x).
x ∈Ω
To determine an optimal policy result, let us deﬁne the current Hamiltonian function as
H(C, K, λ) = U(C) + λ (∇(d(x)∇K(x, t) + AK(x, t)α −δK(x, t) −C(x, t))
The following proposition provides the optimality conditions for an optimal solution of the problem above.
Proposition 2. Suppose that U(C) is a concave function of C. Then a pair ( ˜C, ˜K) solves the above optimal
control model if and only if it is solution to the following Hamiltonian system:























∂K(x,t)
∂t
= ∇(d(x)∇K(x, t)) + AK(x, y)α −δKK(x, t) −C(x, t),
(x, t) ∈Ω× (0, T)
∂λ(x,t)
∂t
= ρλ −∇(d(x)∇λ(x, t)) −λαAKα−1(x, t) −δKλ,
(x, t) ∈Ω× (0, T)
U′(C) = λ
(x, t) ∈Ω× (0, T)
d(x)∂K
∂n (x) = 0,
x ∈∂Ω
d(x) ∂λ
∂n(x) = 0,
x ∈∂Ω
λ(x, T) = Θ
x ∈Ω
K(x, 0) = K0(x)
x ∈Ω
Since analyzing explicitly the Hamiltonian system above is generally not possible (unless we introduce
restrictive assumptions), we now proceed with numerical simulations to illustrate the optimal behavior of
capital and consumption. If we use the dynamic constraint and plug it into the objective function we obtain:
J(K) =
Z T
0
Z
Ω
U

−∂K(x, t)
∂t
+ ∇(dk(x)∇K(x, t)) + AK(y, t)α −δKK(x, t)

e−ρtdxdt + Θ
Z
Ω
K(x, T)dx
Subject to





−∂K(x,t)
∂t
+ ∇(d(x)∇K(x, t)) + AK(x, t)α −δKK(x, t) ≥0,
(x, t) ∈Ω× (0, T)
d(x)∂K
∂n (x) = 0,
x ∈∂Ω
K(x, 0) = K0(x).
x ∈Ω
7


## Page 8


The direction derivative of J along any feasible h is given by
J′(K; h)
=
lim
δ→0
J(K + δh) −J(K)
δ
=
Z T
0
Z
Ω
U′(−∂K(x, t)
∂t
+ ∇(d(x)∇K(x, t)) + AKα(x, t) −δKK(x, t))
∗

−∂h(x, t)
∂t
+ ∇(d(x)∇h(x, t)) + Ahα(x, t)dx −δKh(x, t)

e−ρtdxdt + Θ
Z
Ω
h(x, T)dx
We propose an algorithm to determine an approximation of the optimal solution. At each step this algorithm
determines the direction of growth h using the above calculated directional derivative J′(K; h).
• Given the value of the state variable Kn(x, t), solve the following problem
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
−∂h(x,t)
∂t
+ ∇(d(x)∇h(x, t)) + Ahα(x, t) −δKh(x, t) =
h
U′ 
−∂Kn(x,t)
∂t
+ ∇(d(x)∇Kn(x, t)) + AKα
n(x, t) −δKKn(x, t)
i−1  −Θ∂h
∂t + 1

eρt,
(x, t) ∈Ω× (0, T)
d(x)∂K
∂n (x) = 0,
x ∈∂Ω
h(x, 0) = 0.
x ∈Ω
• Determine δ > 0 that corresponds to the maximum increment of J along the direction h
• Update Kn+1 = Kn + δh
• If |J(Kn+1) −J(Kn)| < ϵ then stop otherwise go to the top.
The following result shows that J is increasing along the sequence generated by the above algorithm.
The implementation of the above algorithm generates a sequence of functions Kn along which the objective
function is increasing.
Proposition 3. If δ is small then J(Kn+1) ≥J(Kn), ∀n ≥0.
Proof. Computing we have:
J(Kn+1) −J(Kn)
=
δJ′(Kn; h) + o(δ)
=
δ
Z T
0
Z
Ω

−Θ∂h
∂t + 1

dxdt + Θ
Z
Ω
h(x, T)dx

+ o(δ)
=
δ

−Θ
Z
Ω
h(x, T) −h(x, 0)dx + Tµ(Ω) + Θ
Z
Ω
h(x, T)dx

+ o(δ)
=
δ

Tµ(Ω) + o(δ)
δ

≥0
and this last passage relies on the boundary condition h(x, 0) = 0.
■
We now apply the above algorithm to the following model where U(C) = [(1 + C(x, t))
2
3 −1], T = 1,
Ω= [0, 1], dk(x) = 1 −0.5x2, α = 1, δK = 0.01.
max
Z 1
0
Z 1
0
[(1 + C(x, t))
2
3 −1]dxdt,
Z 1
0
K(x, 1)dx

Subject to





∂K(x,t)
∂t
= ∇
 (1 −0.5x2)∇K(x, t)

+ K(x, t) −C(x, t) −0.01K(x, t),
(x, t) ∈[0, 1] × (0, 1)
(1 −0.5x2)∂K
∂n (x) = 0,
x = 0, 1
K(x, 0) = 1 + x.
x ∈[0, 1]
8


## Page 9


We have implemented the above algorithm in COMSOL. Firstly, we run the algorithm with Θ = 0. The
values of the objective function after three iterations are: J0 = 0.579453721074241, J1 = 0.6059822543917376,
J2 = 0.6287663921318654, J3 = 0.6534865860743782. Then we used Θ = 0.1. The values of the objec-
tive functions after three iterations are given by: J0 = 0.5944537210742411, J1 = 0.6200510708312351,
J2 = 0.6404132122774402, and J3 = 0.6570096551286734. Figure 1 shows the spatio-temporal behavior of
K in the Θ = 0 case (left panel) and Θ = 0.1 case (right panel). It clearly shows our simple algorithm
is capable to handle an optimal control problem on partial diﬀerential equations without requiring speciﬁc
restrictive assumptions on the functional forms of the utility and production functions.
Figure 1: Spatio-temporal evolution of capital in the Θ = 0 case (left) and Θ = 0.1 case (right).
In order to construct the Pareto frontier we proceed as follows:
• For each Θ we solve the scalarized problem max J1 + ΘJ2,
• Let KΘ(x, t) be the optimal solution, we plug it into the two separated criteria and get the pair of
values (J1, J2),
• We plot the pair (J1, J2).
The Pareto frontier is illustrated in Figure 2, from which we can clearly observe that it is bowed outward
as expected, give the nature of the trade oﬀbetween the two criteria.
Figure 2: Piecewise linear Pareto frontier under scalarization.
5
Further Numerical Experiments
In this section we discuss some further numerical experiments that can be implemented using diﬀerent model
formulations based on the ϵ-constraint and the GP approaches.
9


## Page 10


5.1
Experiment I
We now discuss a model formulation that has been obtained by applying the ϵ-constraint method. In this
formulation we suppose that the DM maximizes his intertemporal utility and the level of physical capital
at the ﬁnal horizon T is included in the set of constraints. Given a positive value of ϵ, the model can be
written as:
max
Z T
0
Z
Ω
U(C(x, t))e−ρtdxdt
(16)
Subject to:









R
ΩK(x, T)dx ≥ϵ,
∂K(x,t)
∂t
= ∇(d(x)∇K(x, t)) + AK(x, t)α −δKK(x, t) −C(x, t),
(x, t) ∈Ω× (0, T)
d(x)∂K
∂n (x) = 0,
x ∈∂Ω
K(x, 0) = K0(x).
x ∈Ω
(17)
This model can be solved using the same approach and a slightly modiﬁed version of the algorithm used
in the linear scalarization case. If we use the dynamic constraint to express the level of consumption C(x, t)
as function of K(x, t), the model boils down to:
max
Z T
0
Z
Ω
U
∂K(x, t)
∂t
−∇(d(x)∇K(x, t)) −AK(x, t)α + δKK(x, t)

e−ρtdxdt
(18)
Subject to:









R
ΩK(x, T)dx ≥ϵ,
−∂K(x,t)
∂t
+ ∇(d(x)∇K(x, t)) + AK(x, t)α −δKK(x, t) ≥0,
(x, t) ∈Ω× (0, T)
d(x)∂K
∂n (x) = 0,
x ∈∂Ω
K(x, 0) = K0(x).
x ∈Ω
(19)
As a numerical experiment, we now apply the above model when U(C) = [(1 + C(x, t))
2
3 −1], T = 1,
Ω= [0, 1], dk(x) = 1 −0.5x2, α = 1, δK = 0.01. The model is formulated as:
max
Z 1
0
Z 1
0
"
1 + −∂K(x, t)
∂t
+ ∇
 (1 −0.5x2)∇K(x, t)

+ K(x, t) −0.01K(x, t)
 2
3
−1
#
dxdt
Subject to







R 1
0 K(x, 1)dx ≥1.3
−∂K(x,t)
∂t
+ ∇
 (1 −0.5x2)∇K(x, t)

+ K(x, t) −0.01K(x, t) ≥0,
(x, t) ∈[0, 1] × (0, 1)
(1 −0.5x2) ∂K
∂n (x) = 0,
x = 0, 1
K(x, 0) = 1 + x.
x ∈[0, 1]
The application of the above algorithm provides J(1) = 0.57945, J(2) = 0.60822, J(3) = 0.63879. The
optimal behaviour of K is shown in Figure 3.
5.2
Experiment II
In this model formulation we still use the ϵ-constraint method but we assume a linear utility function
U(C) = C, and α = 1. In this context the spatial model can be reduced to a one-dimensional optimal
control model by introducing the average of consumption and physical capital at t, CM(t) and KM(t),
deﬁned as
CM(t) =
Z
Ω
C(x, t)dx
10


## Page 11


Figure 3: The evolution of K
and
KM(t) =
Z
Ω
K(x, t)dx
and the average amount of consumption per unit amount cM(t) as
cM(t) = CM(t)
KM(t) ∈[0, 1]
Let us suppose that a pair (K, C) solves the model:
max
C(x,t),K(x,t)
Z T
0
Z
Ω
C(x, t)e−ρtdxdt
(20)
Subject to:









R
ΩK(x, T)dx ≥ϵ,
∂K(x,t)
∂t
= ∇(d(x)∇K(x, t)) + AK(x, t)α −δKK(x, t) −C(x, t),
(x, t) ∈Ω× (0, T)
d(x)∂K
∂n (x) = 0,
x ∈∂Ω
K(x, 0) = K0(x).
x ∈Ω
(21)
Then, by easy calculations and taking the integral of the contraints, the pair (KM, cM) solves the following
one:
max
cM(t),KM(t)
Z T
0
cM(t)KM(t)e−ρtdt
(22)
Subject to





˙
KM(t) = AKM(t) −δKKM(t) −cM(t)KM(t),
t ∈(0, T)
KM(T) ≥ϵ,
KM(0) =
R
ΩK0(x)dx.
(23)
This is classical calculus of variations model with a bang-bang control and it can be solved in closed-form
to determine the optimal paths of CM(t) and KM(t).
5.3
Experiment III
This third experiment is devoted to a diﬀerent formulation that has been obtained by applying the GP
approach. Here we also assume a linear utility function U(C) = C, and α = 1. We also suppose that all
11


## Page 12


weights are equal and then normalized to 1 and that T is an integer number. Given two goals g1 and g2 for
the two criteria J1 and J2, the model reads as:
min δ+
1 + δ−
1 + δ+
2 + δ−
2
(24)
Subject to:













R
ΩK(x, T)dx −δ+
1 + δ−
1 = g1
R T
0
R
ΩC(x, t)e−ρtdxdt −δ+
2 + δ−
2 = g2,
∂K(x,t)
∂t
= ∇(d(x)∇K(x, t)) + AK(x, t) −δKK(x, t) −C(x, t),
(x, t) ∈Ω× (0, T)
d(x)∂K
∂n (x) = 0,
x ∈∂Ω
K(x, 0) = K0(x).
x ∈Ω
(25)
To simplify the model, we take the integral of the PDE and reduce the analysis to the variables KM and
CM introduced in the previous experiment. The model boils down to:
min δ+
1 + δ−
1 + δ+
2 + δ−
2
(26)
Subject to:









KM(T) −δ+
1 + δ−
1 = g1
R T
0 CM(t)e−ρtdt −δ+
2 + δ−
2 = g2,
˙
KM(t) = (A −δK)KM(t) −CM(t),
t ∈(0, T)
KM(0) =
R
ΩK0(x)dx.
(27)
By discretizing the time, and introducing the discrete variables KM(i), CM(i), i = 0...T, the model can be
written as
min δ+
1 + δ−
1 + δ+
2 + δ−
2
(28)
Subject to:









KM(T) −δ+
1 + δ−
1 = g1
PT
i=0 CM(i)e−ρi −δ+
2 + δ−
2 = g2,
KM(i + 1) −KM(i) = (A −δK)KM(i) −CM(i),
i = 0...T −1
KM(0) =
R
ΩK0(x)dx.
(29)
This is a linear optimization model that can be solved by standard optimization solvers such LINGO or
MATLAB.
6
Conclusion
The introduction of intergenerational equity considerations associated with sustainability issues into a tradi-
tional macroeconomic setting transforms the typical unicriterion macroeconomic problem into a bi-criteria
optimization problem, which can be analyzed through the lenses of the multicriteria optimization techniques
developed in the operations research literature. Recently traditional macroeconomic problems have been
extended to introduce a spatial dimension, allowing to consider the extent to which spatial heterogeneity
and spatial spillovers aﬀect economic outcomes not only over time but also across space. The goal of this
papers consists thus to merge these two diﬀerent lines of research by analyzing a simple macroeconomic
setting to account for intergenerational equity and spatial spillovers from the operations research point of
view. In particular, we show that our macroeconomic problem can be reformulated as a multicriteria prob-
lem by relying on diﬀerent techniques (scalarization, ϵ-constraint method and goal programming), and such
diﬀerent formulations of the problem can be solved through numerical methods, which allow us to illustrate
the nature of the trade-oﬀbetween the two criteria and to derive the Pareto-frontier in some speciﬁc cases
and parametrizations.
12


## Page 13


Our paper represents one of the ﬁrst attempts to bridge the economics and the operations research
literature, but still much needs to be done in order to develop further the possible synergies existing be-
tween these two diﬀerent disciplines. In particular, apart from scalarization, ϵ-constraint method and goal
programming approaches, several other techniques developed in the operations research literature can be
applied in similar macroeconomic contexts, especially in the context of stochastic or fuzzy multiple objective
optimization. It would also be worth exploring the use of vectorization algorithms and methods that tackle
the MOP model directly such as, for instance, genetic algorithms. Moreover, apart from the applications
to macroeconomic questions, similar multicriteria approaches can be applied to other economic problems
arising in environmental economics, game theory and cost-beneﬁt analysis.
References
[1] Aouni B., Colapinto C. and La Torre (2014). Financial portfolio management through the goal program-
ming model: Current state-of-the-art, European Journal of Operational Research 234, pp. 536-545.
[2] Arrow, K., Dasgupta, P., Goulder, L., Daily, G., Ehrlich, P., Heal, G., Levin, S., Maler, K.G., Schneider,
S., Starrett D., Walker, B. (2004). Are we consuming too much?, Journal of Economic Perspectives 18,
147–172
[3] Boucekkine, R., Camacho, C., Zou, B. (2009). Bridging the gap between growth theory and economic
geography: the spatial Ramsey model, Macroeconomic Dynamics 13, 20–45
[4] Boucekkine, R., Camacho, C., Fabbri, G. (2013a). On the optimal control of some parabolic diﬀerential
equations arising in economics, Serdica Mathematical Journal 39, 331–354
[5] Boucekkine, R., Camacho, C., Fabbri, G. (2013b). Spatial dynamics and convergence: the spatial AK
model, Journal of Economic Theory 148, 2719–2736
[6] Brito, P. (2004). The dynamics of growth and distribution in a spatially heterogeneous world, UECE-
ISEG, Technical University of Lisbon
[7] Camacho, C., Zou, B. (2004). The spatial Solow model, Economics Bulletin 18, 1–11
[8] Camacho, C., Zou, B., Briani, M. (2008). On the dynamics of capital accumulation across space, Euro-
pean Journal of Operational Research 186 2, 451–465
[9] Charnes, A., Cooper, W.W., Ferguson, R.O. (1955). Optimal estimation of executive compensation by
linear programming, Management Science, 2 138–151
[10] Charnes, A., Cooper, W.W. (1961). Management models and industrial applications of linear program-
ming (New York: John Wiley & Sons)
[11] Chinchilnisky, G., Heal, G., Beltratti, A. (1995). The green golden rule, Economics Letters 49, 174–179
[12] Chinchilnisky, G. (1997). What is sustainable development?, Land Economics 73, 476–491
[13] Colapinto, C., Liuzzi, D., Marsiglio, S. (2017). Sustainability and intertemporal equity: a multicriteria
approach, Annals of Operations Research 251, 271–284
[14] Heal, G. (2005). Intertemporal welfare economics and the environment, in (Maler, K.G., Vincent, J.R.,
Eds.), “Handbook of Environmental Economics”, vol. 3 (North-Holland: Amsterdam)
[15] Krugman, P. (1991). Increasing returns and economic geography, Journal of Political Economy 99,
483–499
13


## Page 14


[16] La Torre, D., Liuzzi, D., Marsiglio, S. (2015). Pollution diﬀusion and abatement activities across space
and over time, Mathematical Social Sciences 78, 48–63
[17] La Torre, D., Liuzzi, D., Marsiglio, S. (2017). Pollution control under uncertainty and sustainability
concern, Environmental and Resource Economics 67, 885-903
[18] La Torre, D., Liuzzi, D., Marsiglio, S. (2019). Population and geography do matter for sustainable
development, Environment and Development Economics 24, 201-223
[19] La Torre, D., Marsiglio, S. (2019). A note on optimal debt reduction policies, Macroeconomic Dynamics,
forthcoming
[20] Le Kama, A.D.A. (2001). Sustainable growth, renewable resources and pollution, Journal of Economic
Dynamics & Control 25, 1911–1918
[21] Marsiglio, S., La Torre, D. (2018). Economic growth and abatement activities in a stochastic environ-
ment: a multi-objective approach, Annals of Operations Research 267, 321-334
[22] Marsiglio, S., Privileggi, F. (2019). On the economic growth and environmental trade–oﬀ: a multi-
objective analysis, Annals of Operations Research, forthcoming
[23] Pezzey, J.C.V. (1997). Sustainability constraints versus “optimality” versus intertemporal concern, and
axioms versus data, Land Economics 73, 448–466
[24] Ramsey, F. (1928). A mathematical theory of saving, Economic Journal 38, 543–559
[25] Quah, D.T. (1996). Regional convergence clusters across Europe, European Economic Review 40, 951–
958
[26] Ramsey, F. (1928). A mathematical theory of saving, Economic Journal 38, 543–559
[27] Sawaragi, Y., Nakayama, H., Tanino, T. (1985). Theory of multiobjective optimization (Academic Press,
Inc.)
[28] Solow, R.M. (1956). A contribution to the theory of economic growth, Quarterly Journal of Economics
70, 65–94
[29] Wolfe, D.A., Gertler, M.S. (2004). Clusters from the inside and out: local dynamics and global linkages,
Urban Studies 41, 1071-1093
[30] World Commission on Environment and Development (1987). Our common future (Oxford University
Press, Oxford)
14

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
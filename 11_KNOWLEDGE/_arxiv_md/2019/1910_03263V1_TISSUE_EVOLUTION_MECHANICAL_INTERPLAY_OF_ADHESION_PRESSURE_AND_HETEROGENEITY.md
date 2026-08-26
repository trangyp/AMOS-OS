---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1910.03263v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1910.03263v1_Tissue_evolution__Mechanical_interplay_of_adhesion__pressure__and_heterogeneity

> Source: 1910.03263v1_Tissue_evolution__Mechanical_interplay_of_adhesion__pressure__and_heterogeneity.pdf

> Pages: 13

---


## Page 1


Tissue evolution: Mechanical interplay of adhesion, pressure,
and heterogeneity
Tobias B¨uscher1, Nirmalendu Ganai1,2, Gerhard Gompper1, Jens Elgeti1*,
1 Theoretical Soft Matter and Biophysics, Institute of Complex Systems and Institute
for Advanced Simulation, Forschungszentrum J¨ulich, 52425 J¨ulich, Germany
2 Department of Physics, Nabadwip Vidyasagar College, Nabadwip, Nadia 741302, India
* j.elgeti@fz-juelich.de
Abstract
The evolution of various competing cell types in tissues, and the resulting persistent
tissue population, is studied numerically and analytically in a particle-based model of
active tissues. Mutations change the properties of cells in various ways, including their
mechanical properties. Each mutation results in an advantage or disadvantage to grow
in the competition between different cell types. While changes in signaling processes
and biochemistry play an important role, we focus on changes in the mechanical
properties by studying the result of variation of growth force and adhesive
cross-interactions between cell types. For independent mutations of growth force and
adhesion strength, the tissue evolves towards cell types with high growth force and low
internal adhesion strength, as both increase the homeostatic pressure. Motivated by
biological evidence, we postulate a coupling between both parameters, such that an
increased growth force comes at the cost of a higher internal adhesion strength or vice
versa. This tradeoff controls the evolution of the tissue, ranging from unidirectional
evolution to very heterogeneous and dynamic populations. The special case of two
competing cell types reveals three distinct parameter regimes: Two in which one cell
type outcompetes the other, and one in which both cell types coexist in a highly mixed
state. Interestingly, a single mutated cell alone suffices to reach the mixed state, while a
finite mutation rate affects the results only weakly. Finally, the coupling between
changes in growth force and adhesion strength reveals a mechanical explanation for the
evolution towards intra-tumor heterogeneity, in which multiple species coexist even
under a constant evolutianary pressure.
Introduction
Mutations change the cell fitness and thus its chance to survive and proliferate [1].
Advantageous mutations are more likely to persist due to natural selection, which drives
the evolution of a tissue towards fitter cells [2]. Cancer represents an example of
evolution on a short time scale [3]. Furthermore, cancer is a multistep process, i.e.
several mutations are needed for a tumor in order to develop and become malignant [4].
Hence, tumorigenesis might be expected to happen in a serial manner, i.e. a cell
acquiring a ”beneficial” mutation and taking over the whole tissue. After some time, a
daughter cell acquires another mutation and again takes over. Interestingly, however,
tumors do not consist of a single cell type, but instead several subpopulations coexist
within the same tumor. This is called intra-tumor heterogeneity [5].
1/13
arXiv:1910.03263v1  [q-bio.PE]  8 Oct 2019


## Page 2


Each mutation changes certain biochemical properties of a cell. This ranges from
misfunction in the error correction machinery during DNA replication and disruptions
in signaling pathways to epigenetic changes in the expression level of certain
proteins [1,6,7]. All these changes can also affect the mechanical properties of the
mutated cell, e.g. mutated cells which express less adhesion proteins might be able to
detach from the primary tumor more easily [8], necessary to form metastases. On the
other hand, mechanics feeds back onto growth in several ways, e.g. increased apoptosis
rate due to mechanical stresses [9,10] or dependence of the growth of tissue spheroids on
the properties of the surrounding medium [11–13].
It is the mechanical contribution to tissue development that we want to focus on in
this work. For mechanically regulated growth, homeostatic pressure plays an important
role [14]. In the homeostatic state, when apoptosis and division balance each other, a
tissue exerts a certain pressure onto its surrounding, the homeostatic pressure PH. The
tissue is able to grow as long as the external pressure P is smaller than PH. For the
competition between different tissues for space, it has been suggested that the tissue
with the higher homeostatic pressure grows at the expense of the weaker tissue. Several
theoretical studies employ this concept in order to describe interface propagation
between two competing tissues [15–17]. A metastasis would need to reach a critical size,
below which the additional Laplace pressure due to surface tension would cause the
metastasis to shrink and disappear [14]. However, reduced adhesion between tissues,
which increases surface tension, leads to an enhanced growth rate at the interface
between them, stabilizing coexistence even for differing homeostatic pressures [18].
In this work, we study the influence of mutations that change the mechanical
properties of cells on the competition dynamics, especially the interplay between
changes in the adhesive properties and the strength with which a cell pushes onto its
surrounding. Particularly interesting is the case where loss of adhesion comes at the
cost of lower growth strength. This is motivated by the observed down-regulation of
E-cadherin, an adhesion protein in epithelia, in many types of cancer [19]. Interestingly,
E-cadherin is also involved in signaling processes connected to cell growth [20]. We find
that in this case several cell types with different mechanical properties can coexist and
that the cell type with the highest homeostatic pressure does not necessarily dominate
the competition.
Results
Several models have been developed previously in order to study tissue growth [21], in
combination with different simulation techniques, including vertex [22,23] and
particle-based [24,25] models as well as Cellular Potts models [26,27]. We employ the
two particle growth (2PG) model of Refs. [18,28,29]. A cell is described by two particles
which repel each other via a growth force
F G
ij =
G
(rij + r0)2 ˆr ij,
(1)
with strength G, unit vector ˆr ij, distance rij between the two particles and a constant
r0. Different cells interact via a soft repulsive force F V
ij on short distances, maintaining
an excluded volume, and a constant attractive force F A
ij on intermediate distances,
modeling cell-cell adhesion, with
F V
ij
= f0

R5
PP
r5
ij −1

ˆr ij
F A
ij
= −f1ˆr ij
)
for rij < RPP,
(2)
2/13


## Page 3


Fig 1. Evolution of a tissue with mutations altering growth-force strengh G† and adhesion strength f †
1 independently.
Heatmaps displaying cell-number fractions φα after a) zero generations (initial condition), b) 50 generations, c) 100
generations and d) 125 generations.
with exclusion coefficient f0, adhesion strength coefficient f1, and cut-off length RPP. A
cell divides when the distance between its two particles reaches a size threshold rct. A
new particle is then placed close (randomly within a short distance rd) to each of the
two particles of the divided cell. Each of these pairs then constitutes a new cell.
Apoptosis is modeled by removing cells randomly at a constant rate ka.
We employ a dissipative particle dynamics-type thermostat, with an effective
temperature T, to account for energy dissipation and random fluctuations. We choose
the value of T such that cells can escape local minima, but other thermal effects are
negligible. Note that all parameters can be set individually for each cell type as well as
between different cell types for inter-cell interactions. We only vary the growth-force
strength Gα and adhesion strength f αβ
1
between cells of the same (α = β) and different
(α ̸= β) cell types, respectively, where α and β are cell-type numbers. We report
simulation parameters relative to a standard host cell type (see Materials and methods
for numerical values), denoted with a dagger, e.g. G† = G/G0. Time is measured in
terms of the inverse apoptosis rate ka, distance in units of the pair potential cut-off
length RPP and stresses in units of G0/R4
PP. Quantities reported in these units are
denoted by an asterisk ∗. All simulations are performed in a cubic box with edge length
L = 12 · RPP and periodic boundary conditions in all directions, unless stated otherwise.
Tumor cells even within the same tumor are not all identical, but vary in terms of all
kind of attributes, e.g. expression levels of different proteins [30] or their reaction to
certain treatments [31]. Hence, there is not only a competition between the tumor and
the host, but also between cell-subpopulations of the tumor. Different models exist to
describe tumor heterogeneity, e.g. cancer stem cells [32] or clonal evolution [33]. In the
latter case, a tumor originates from a single mutated cell, which can acquire additional
mutations over time, yielding additional subpopulations. We model this behaviour by
defining a fixed number n of different ”genotypes”, each having a different growth-force
strength Gα and adhesion strength f αα
1 . Mutations are implemented by offering each
daughter cell after a division event the chance to change its genotype with a certain
probability.
In tissues, several adhesion mechanisms exist, serving a variety of different functions
to maintain tissue integrity. Between epithelial cells, the strength of cell-cell adhesion is
to a large degree regulated by anchoring junctions, e.g. adherens junctions, which
connect the actin cytosceletons of neighbouring cells. Adherens junctions are mediated
by cadherins, which form homophilic bonds between cells. Thus, the strength of
adhesion between cells is limited by the cell expressing less cadherin, or, in terms of our
simulation model f αβ
1
= min(f αα
1 , f ββ
1 ). A reduced adhesion strength yields a higher
3/13


## Page 4


Fig 2. Time evolution of the cell-number fractions φα of each genotype for tradeoff paramter a) τ = 0, b) τ = 1, c) τ = 2
and d) τ →∞, d →0. Simulations start from a host (standard) tissue at homeostasis, with n = 21 genotypes, pm = 0.01 in
all and d = 0.025 in a)-c). White space corresponds to times where no cells of the genotype exist. Color is coded on a
logarithmic scale. Curves above display homeostatic pressure P α∗
H
(black solid), growth-force strength Gα†(red dashed) and
self adhesion strength f αα†
1
(green dotted) of the corresponding genotype.
homeostatic pressure [29], which is otherwise dominated by the growth-force strength G.
For free parameter evolution, the tissue thus evolves to a strong-growing and
low-adhesive genotype (see Fig 1), as predicted by the homeostatic pressure
approach [14].
However, E-cadherin also plays a role in signaling processes connected to cell growth,
and thus a reduced expression might come at the cost of a lower growth-force strength
G, which in turn yields a lower homeostatic pressure. We thus turn our attention to the
case where an increase in growth-force strength Gα comes at the cost of a higher
self-adhesion strength f αα
1 . We assume the relations as
Gα = (1 + Dα)G0
(3)
f αα
1
= (1 + Dα · τ)f 0
1 ,
(4)
with genotype number α in the range [−(n −1)/2, (n −1)/2], evolutionary distance
Dα = d · α, distance d between neighbouring genotypes and tradeoff paramteter τ (with
Gα, f αα
1
> 0 ∀α). After a division event, each daughter cell might mutate into a new
genotype with probability pm. If the cell mutates, its genotype number is changed to
αmother ± 1 randomly. This yields a mutation rate km = 2pmka.
Figure 2 displays results of such simulations for four different cases: only variation of
growth-force strength (τ = 0), balanced tradeoff (τ = 1), adhesion strength varied twice
as much as growth-force strength (τ = 2) and only variation of adhesion strength
(τ →∞). Without tradeoff (Fig 2a)), the tissue evolves towards the strongest growing
genotype or, equivalently, the one with the highest homeostatic pressure. Similarly, for
τ →∞(Fig 2d)), the system evolves towards the lowest adhesive genotype (again, the
one with the highest PH). We find the most dynamic evolution for a balanced tradeoff
(Fig 3 and 2b)). At first, the system evolves to stronger growing and more adhesive
genotypes. Over time a noticable fraction of cells evolves also towards weak-growing,
less adhesive genotypes. The cell-number fractions φα = Nα/N (with individual and
4/13


## Page 5


a)
b)
c)
Fig 3. Simulation snapshots obtained from the simulation shown in Fig 2b). a) The dominating genotype (φ10 = 0.283) after
1000 generations. b) Genotype α = −6 (blue) and α = 6 (green) after 485 generations (φ−6 = 0.027, φ6 = 0.002). c) Same as
b), but after 910 generations (φ−6 = 0.003, φ6 = 0.045).
total number of cells, Nα and N), show large fluctuations (see Fig 3b) and c)), with
individual genotypes not being populated at all for certain time periods. Besides this
highly dynamic temporal evolution, after an initial time period the system is dominated
by genotypes with increased growth force and adhesion strength at all times, with the
one at the upper boundary having the highest cell-number fraction for most of the time
(see Fig 3a)). This result comes at a surprise, as this is also the genotype with the
lowest homeostatic pressure, while the one at the lower boundary, which is basically
never populated, has the highest PH. For a higher tradeoff (Fig 2c)), we still find a
broad distribution of genotypes, with less adhesive genotypes dominating over the
stronger growing ones, i.e. the loss in growth-force strength is overcompensated by a
lower adhesion strength.
In order to gain insight into the underlying mechanism of this dynamic evolution, we
study the competition between two genotypes and no mutations (pm = 0). Simulations
are started from a single mutated cell (with increased/decreased growth force and
adhesion strength) in a host tissue at the homeostatic state (we label the mutant with
M and the host (wild type) with W). Even in this simplified case, we find one parameter
regime in which the mutant is not able to grow, one regime with stable coexistence in a
highly mixed state and another regime in which the mutant outcompetes the host.
Figure 4 shows the averaged number fractions of the mutant at the steady state. For
reduced growth force and adhesion strength (Fig 4a)), the mutant can only grow against
the host if its adhesion strength is reduced below a critical f crit
1
. In terms of Eq. (4),
the value of f crit
1
roughly corresponds to a balanced tradeoff (τ ≈1). Already for
f MM
1
> f crit
1
, the homeostatic pressure of the mutant exceeds the one of the host, i.e. a
parameter regime exists in which the mutant is not able to grow, despite of the higher
PH. The reverse happens when growth force and adhesion strength are increased. The
mutant completely takes over the compartment, although its homeostatic pressure is
smaller than that of the host. Again, coexistence is only found when the adhesion
strength is increased above f crit
1
. In the coexistence regime, the mutant number fraction
scales as φM ∝1/(f MM
1
−f WW
1
).
Altogether, the competition between two genotypes alone yields the same qualitative
results as the more complex multi-genotype case discussed before. Still, the question
remains how a genotype with lower homeostatic pressure can outcompete a stronger
5/13


## Page 6


(a)
(b)
0.5
0.6
0.7
0.8
0.9
1.0
Adhesion strength f MM†
1
0.0
0.2
0.4
0.6
0.8
1.0
Mutant number fraction φM
GM†=0.750
GM†=0.825
GM†=0.875
GM†=0.925
GM†=0.975
1.0
1.1
1.2
1.3
1.4
1.5
Adhesion strength f MM†
1
0.0
0.2
0.4
0.6
0.8
1.0
Mutant number fraction φM
GM†=1.025
GM†=1.075
GM†=1.125
GM†=1.175
GM†=1.250
Fig 4. a) Average number fraction φM of the mutant in terms of its adhesion strength f MM†
1
for various (reduced)
growth-force strengths GM†. Error bars are obtained via block-averaging method (hidden behind markers) [34]. Dashed
vertical lines indicate the points below which the mutant has a higher homeostatic pressure, solid lines are fits to Eq. 10.
b) Same as in a) but for increased growth force and adhesion strengths of the mutant.
genotype. The answer can only lie in the adhesion strength f MW
1
= min(f MM
1
, f WW
1
)
between mutant and host cells. This choice of cross-adhesion strength breaks symmetry,
as the stronger adhering genotype has more free space at the interface, which favors
divisions [18].
To address this question, we develop a phenomenological model which incorporates
pressure-dependent growth as well as interfacial effects, in order to obtain a qualitative
explanation of the simulation results.
We start with the expansion of the bulk growth rate kb around the homeostatic
pressure,
kb = κ(P −PH),
(5)
with the pressure response coefficient κ. Due to the high degree of mixing, the number
fractions φM/W and hence the strengh of interfacial effects vary locally. In a mean-field
approximation, we take the interfacial effects to be proportional to φM(1 −φM), with
individual prefactors ∆kM/W
s
for each genotype. The time evolution is then given by
∂tφM =κ(P M
H −P)φM + ∆kM
s φM(1 −φM)
(6)
∂t(1 −φM) =κ(P M
H + ∆PH −P)(1 −φ) + ∆kW
s φM(1 −φM),
(7)
with the difference in homeostatic pressure ∆PH = P W
H −P M
H . Addition of Eqs. (6) and
(7) yields the pressure
P = P W
H −∆PHφM + ∆kM
s + ∆kW
s
κ
φM(1 −φM).
(8)
Thus, the pressure is given by the homeostatic pressures of the two genotypes weighted
by their number fraction plus an interfacial term. A figure displaying the pressure
measured during the simulations shown in Fig 4 can be found in the S1 Appendix.
Insertion of Eq. (8) into Eq. (6) yields a differential equation for the number fraction
with three fixed points (∂tφM = 0), φM
1 = 0, φM
2 = 1, and
6/13


## Page 7


(a)
(b)
0
1
2
3
4
5
Tradeoﬀτ
0.0
0.2
0.4
0.6
0.8
1.0
Mutant number fraction φM
Dα=-0.250
Dα=-0.175
Dα=-0.125
Dα=-0.075
Dα=-0.025
0
1
2
3
4
5
Tradeoﬀτ
0.0
0.2
0.4
0.6
0.8
1.0
Mutant number fraction φM
Dα=0.025
Dα=0.075
Dα=0.125
Dα=0.175
Dα=0.250
Fig 5. a) Average number fractions of the mutant (same simulations as shown in Fig 4a)) as a function of the tradeoff τ of
Eq. (4) for different evolutionary distances Dα. b) Same as in a) but with results from Fig 4b). Error bars are obtained via
block-averaging method (hidden behind markers).
φM
3 = −κ∆PH + ∆kM
s
∆kM
s + ∆kW
s
.
(9)
We discuss this result for the case of reduced growth force and adhesion strength of
the mutant. ∆kM
s
might be expected to vanish, as f MM
1
= f MW
1
and mutant cells thus
would not feel whether neighbouring cells are mutant or host cells. However, in order to
grow, a cell needs to impose a strain on its surrounding. Host cells adhere more strongly
to each other, thus it is harder for a mutant cell to impose a strain when surrounded by
host cells. Hence, ∆kM
s
is actually negative and the homeostatic pressure of the mutant
needs to exceed the host pressure by −∆kM
s /κ in order to be able to grow against the
host. At this point, φM
3 becomes positive, as long as ∆kM
s + ∆kW
s
> 0. Host cells can
impose a strain more easily when surrounded by mutant cells and, additionally, have
more free space than when surrounded by other host cells. Hence, |∆kM
s | < ∆kW
s
and
the above mentioned condition is fulfilled. Similarly, coexistence can be found for
increased growth force and adhesion strength when ∆PH > −∆kW
s /κ. The above
mentioned scaling of the mutant number fraction can be obtained by an expansion of
∆PH and ∆kM/W
s
to linear order in terms of ϵ := (f MM
1
−f WW
1
)/f WW
1
in Eq. (9),
φM
3 =
−κ∆P 0
H
(∆kM1
s
+ ∆kW1
s
)ϵ + −κ∆P 1
H + ∆kM1
s
∆kM1
s
+ ∆kW1
s
.
(10)
The zeroth order terms of ∆kM/W
s
vanish as there are no interfacial effects when the
adhesion strength between host and mutant cells is equal to their self-adhesion strength,
while ∆P 0
H can be non-zero due to a changed growth-force strength. Indeed, Eq. (10)
reproduces the simulation data reasonably well (see Fig 4). A discussion of the
numerical values of the fitted parameters and additional results can be found in S1
Appendix.
Figure 5 displays similar results as shown in Fig 4, but now as a function of the
tradeoff τ in Eq. (4). For τ < 1 the genotype with higher growth-force strength
outcompetes the weaker genotype, for 1 < τ < 2 a transition towards the less adhesive
genotype occurs, while for even higher values of the tradeoff τ > 2 the less adhesive
genotype outcompetes the second genotype. This transition from strongly growing,
7/13


## Page 8


(a)
(b)
10−4
10−3
10−2
10−1
Mutation rate k∗
m
0.0
0.2
0.4
0.6
0.8
1.0
Mutant number fraction φM
τ = 1.0
τ = 1.5
τ = 2.0
10−4
10−3
10−2
10−1
Mutation rate k∗
m
0
10
20
30
40
50
Number cluster Nc
τ = 1.0
τ = 1.5
τ = 2.0
Fig 6. a) Average number fraction φM of the mutant as a function of the mutation rate k∗
m for different values of the tradeoff
τ, for evolutionary distances Dα = 0.025 (circles) and Dα = −0.025 (triangles). Horizontal dotted lines display results for a
single mutation event. Vertical black dashed line indicates standard mutation rate. Solid lines are a guide to the eye.
b) Average number of clusters of the weaker genotype Nc measured in the same competitions in a). Horizontal dotted lines
display results for a single mutation event. Error bars are obtained via block-averaging method.
adhesive to weakly growing, less adhesive genotypes is found in the same range of τ as
in the competition between many genotypes. Hence, the simplified case of two
competing genotypes captures the essential physics to explain the coexistence between
many competing genotypes and, additionally, provides a quantitative description.
Next, we turn our attention to the effect of a finite mutation rate on the evolution of
the system. Figure 6a) shows the number fraction of the mutant as a function of km for
different combinations of evolutionary distance Dα and tradeoff τ, in comparision to the
number fraction reached for a single mutation event. As expexted, the number fraction
converges towards 1/2 with increasing km for all combinations. For moderate mutation
rates, however, the number fraction largely fluctuates around the same average as of a
single mutation event. The single mutation leads to a stable coexistence of the two
genotypes - additional mutations quickly relax back to this state. Siginificant deviations
occur only if in the steady state of the single mutation event the number fraction of the
weaker genotype is close to zero. In that case, the weaker genotype consists only of one
or very few small cohesive clusters of cells, because cells of the weaker genotype need to
detach from the primary cluster in order to form new clusters, but are likely to die when
they do so, as they are only surrounded by cells of the stronger genotype. Hence, the
distribution of cells is highly non-homogenous. Compared to the single mutation event,
even a small mutation rate leads to the formation of multiple small cluster all over the
system, thus increasing the number fraction of the weaker genotype (see Fig 6b) for
comparision in terms of number of clusters and Materials and methods for further
discussion). This result explains why at least two genotypes, in addition to the
dominating genotype, are populated as well in the cases shown in Fig 2a) and d). When
the number fractions of both genotypes are sufficiently large (for 1 ≤τ ≤2), deviations
from the average of a single mutation are still small for the standard mutation
probability. Additionally, in the competitions between many genotypes, mutations
change the genotype to α ± 1 randomly and not in a preferred direction. Hence, we
conclude that the precise value of the mutation probability does not play an important
role in the regime where we find a heterogeneous distribution of genotypes, as long as it
is reasonably small (km ≪ka).
8/13


## Page 9


(a)
(b)
0.5
0.6
0.7
0.8
0.9
1.0
Adhesion strength f MM†
1
0.0
0.2
0.4
0.6
0.8
1.0
Survival probability ps
GM† = 0.750
GM† = 0.825
GM† = 0.875
GM† = 0.925
GM† = 0.975
1.0
1.1
1.2
1.3
1.4
1.5
Adhesion strength f MM†
1
0.0
0.2
0.4
0.6
0.8
1.0
Survival probability ps
GM† = 1.025
GM† = 1.075
GM† = 1.125
GM† = 1.175
GM† = 1.250
Fig 7. a) Probability ps of a single mutated cell to grow to macroscopic size as a function of its (reduced) adhesion strength
f MM†
1
for several values of the (reduced) growth-force strength GM†. Error bars are a 1σ binomial confidence interval
obtained by Clopper-Pearson. Solid lines are linear fits. b) Same as in a), but with a constant fitted in the plateau regime
and increased growth force and adhesion strength. Box size L∗= 8.
Given that a single mutated cell can grow to tissue of macroscopic size in a certain
parameter regime for f MW
1
= min(f MM
1
, f WW
1
), the question arises how likely it is to
actually reach this state. In order to study this probability, we mutate again a single
cell in a host tissue at its homeostatic state. A mutation that reaches a certain
threshold Nt = 20 of cells counts as a survival event (the chance to die after reaching
this treshold becomes extremely small), apoptosis of the last mutant cell as a death
event. Figure 7 shows the averages of many such simulations. For reduced growth force
and adhesion strength, the survival probability ps is only non-zero below the critical
adhesion strength f crit
1
. For f MM
1
< f crit
1
, ps increases linearly with further decreasing
adhesion strength. On the other hand, when growth force and adhesion strength are
increased, the survival probability first shows a plateau, whose value increases with
increasing growth force strength, from which it will probably drop to zero with further
increase. Simulations in this regime are difficult, because a mutated cell can easily grow
to a few cells, but will hardly reach the number threshold nor completely vanish again.
Due to the high self-adhesion strength on the one hand, it becomes hard to detach from
the other cells, but on the other hand easy to grow against the host when only few or no
other mutant cells are around. This explains the larger error bars at the highest values
of the adhesion strength, where the sample size is small.
Discussion
We have shown how intra-tumor heterogeneity, the existence of multiple subpopulations
within the same tumor, can arise due to mechanical interactions alone. The
simultaneous change of the adhesion and growth-force strength stabilizes the
coexistence of multiple subpopulations, in a highly dynamic state. A higher
growth-force strength alone, as well as a lower adhesion strength, favor proliferation of a
single subpopulation and the evolution of the system to cell types with the highest
growth-force strength, or lowest adhesion strength, respectively. A tradeoff between the
two, however, yields coexistence between multiple subpopulations of different cell types.
Interestingly, the expression of the adhesion protein E-cadherin, which also affects cell
growth, has been found to be down-regulated in many real tumors [19].
The simulations also reveal that the homeostatic pressure of a cell type is not
9/13


## Page 10


necessarily the only quantity that determines the result of a competition. Interactions
between different cell types, in our model determined by the adhesion between them,
can lead to a completely reverse outcome, i.e. a cell type with lower homeostatic
pressure can outcompete a stronger one completely. A phenomenological model explains
the results on a qualitative level. The evolution of each cell type is governed by
mechanically-regulated growth, while mutation rates only play a minor role in the
dynamics.
An interesting future aspect to be studied is the influence of open boundaries. A
tissue with a negative homeostatic pressure then naturally grows to a spheroid of finite
size, with an enhanced rate of division at the surface [29]. For competing cell types, this
would lead to an interplay between surface and interfacial effects.
Materials and methods
Standard (host) tissue and simulation parameters
We define a set of reference simulation parameters, which we refer to as host parameters.
Table 1 shows the values in simulation units. In simulations we keep the host W fixed
and vary the parameters of the mutant M around the values of the host.
Table 1. Simulation parameters and measured properties of the standard (host) tissue
.
Parameter
Symbol
Value
Time Step
∆t
10−3
Pair potential interaction range
RPP
1
Cellular expansion pressure constant
r0
1
Cell division distance treshold
rct
0.8
New cell particle initial distance
rd
0.00001
Growth-force strength
G
40
Mass
m
1
Intracell dissipation coefficient
γc
100
Intercell dissipation coefficient
γt
50
Background dissipation coefficient
γb
0.1
Apoptosis rate
ka
0.01
Mutation propability
pm
0.01
Noise intensity
kBT
0.1
Repulsive cell-cell potential coefficient
f0
2.39566
Attractive cell-cell potential coefficient
f1
6.0
Isothermal compressibility
βT
1
Relaxation time constant
tP
1
Homeostatic pressure
P ∗
H
0.1321 ± 0.0005
Pressure response coefficient
κ∗
2.676 ± 0.080
Cluster analysis
As explained in the results section, a constant rate of mutation leads to an enhanced
formation of clusters when the weaker genotype is barely able to grow against the
stronger genotype and consists of only one or few clusters for a single mutation event.
We define a cluster as all cells of the same genotype that are in interaction range to at
least one other member of the cluster (DBSCAN clustering algorithm with number of
minimal points equal to one). Figure 6b) displays the number of clusters of the weaker
genotype in the competitions displayed in Fig 6a), in comparison to the result of a
10/13


## Page 11


single mutation event. Indeed, when the number fraction of the weaker genotype is
small for a the single mutation event (τ = 1), we find significant deviations even for
small mutation rates. In this case, the number of clusters first strongly increases with
mutation rate, with roughly a tenfold increase at the peak. For even higher mutation
probability, the number of clusters decreases again, due to merging of clusters, finally
leading to percolation.
Supporting information
S1 Appendix.
Additional Results. Appendix containing additional results and
the corresponding figures.
Acknowledgments
The authors gratefully acknowledge the computing time granted through JARA-HPC
on the supercomputer JURECA [35] at Forschungszentrum J¨ulich.
References
1. Weinberg RA. The biology of cancer. Garland Publishing, Inc.; 2007.
2. Greaves M, Maley CC. Clonal evolution in cancer. Nature 2012;481(7381):306.
3. Bozic I, Reiter JG, Allen B, Antal T, Chatterjee K, Shah P, et al. Evolutionary
dynamics of cancer in response to targeted combination therapy. eLife.
2013;2:e00747. doi:10.7554/eLife.00747.
4. Vogelstein B, Kinzler KW. The multistep nature of cancer. Trends Genet.
1993;9(4):138 – 141. doi:https://doi.org/10.1016/0168-9525(93)90209-Z.
5. Heppner GH. Tumor Heterogeneity. Cancer Res. 1984;44(6):2259–2265.
6. Preston BD, Albertson TM, Herr AJ. DNA replication fidelity and cancer. Semin
Cancer Biol. 2010;20(5):281 – 293.
doi:https://doi.org/10.1016/j.semcancer.2010.10.009.
7. Schnekenburger M, Diederich M. Epigenetics Offer New Horizons for Colorectal
Cancer Prevention. Curr Colorectal Cancer Rep. 2012;8(1):66–81.
doi:10.1007/s11888-011-0116-z.
8. Petrova YI, Schecterson L, Gumbiner BM. Roles for E-cadherin cell surface
regulation in cancer. Mol Biol Cell. 2016;27(21):3233–3244.
doi:10.1091/mbc.E16-01-0058.
9. Wernig F, Xu Q. Mechanical stress-induced apoptosis in the cardiovascular
system. Prog Biophys Mol Bio. 2002;78(2):105 – 137.
doi:https://doi.org/10.1016/S0079-6107(02)00008-1.
10. Cheng G, Tse J, Jain RK, Munn LL. Micro-environmental mechanical stress
controls tumor spheroid size and morphology by suppressing proliferation and
inducing apoptosis in cancer cells. PLoS One. 2009;4(2):e4632.
doi:10.1371/journal.pone.0004632.
11/13


## Page 12


11. Montel F, Delarue M, Elgeti J, Malaquin L, Basan M, Risler T, et al. Stress
Clamp Experiments on Multicellular Tumor Spheroids. Phys Rev Lett.
2011;107(18):188102. doi:10.1103/PhysRevLett.107.188102.
12. Alessandri K, Sarangi BR, Gurchenkov VV, Sinha B, Kiesling TR, Fetler L, et al.
Cellular capsules as a tool for multicellular spheroid production and for
investigating the mechanics of tumor progression in vitro. Proc Natl Acad Sci
USA. 2013;110(37):14843–14848. doi:10.1073/pnas.1309482110.
13. Helmlinger G, Netti PA, Lichtenbeld HC, Melder RJ, Jain RK. Solid stress
inhibits the growth of multicellular tumor spheroids. Nat Biotechnol.
1997;15(8):778–783. doi:10.1038/nbt0897-778.
14. Basan M, Risler T, Joanny JF, Sastre-Garau X, Prost J. Homeostatic
competition drives tumor growth and metastasis nucleation. HFSP J.
2009;3(4):265–272. doi:10.2976/1.3086732.
15. Williamson JJ, Salbreux G. Stability and Roughness of Interfaces in Mechanically
Regulated Tissues. Phys Rev Lett. 2018;121:238102.
doi:10.1103/PhysRevLett.121.238102.
16. Ranft J, Aliee M, Prost J, J¨ulicher F, Joanny JF. Mechanically driven interface
propagation in biological tissues. New J Phys. 2014;16(3):035002.
17. Podewitz N, J¨ulicher F, Gompper G, Elgeti J. Interface dynamics of competing
tissues. New J Phys. 2016;18(8):083020.
18. Ganai N, B¨uscher T, Gompper G, Elgeti J. Mechanics of tissue competition:
interfaces stabilize coexistence. New J Phys. 2019;21(6):063017.
doi:10.1088/1367-2630/ab2475.
19. Beavon IRG. The E-cadherin–catenin complex in tumour metastasis: structure,
function and regulation. Eur J Cancer. 2000;36(13):1607 – 1620.
doi:https://doi.org/10.1016/S0959-8049(00)00158-1.
20. Pece S, Gutkind JS. Signaling from E-cadherins to the MAPK Pathway by the
Recruitment and Activation of Epidermal Growth Factor Receptors upon
Cell-Cell Contact Formation. J Biol Chem. 2000;275(52):41227–41233.
doi:10.1074/jbc.M006578200.
21. Van Liedekerke P, Palm MM, Jagiella N, Drasdo D. Simulating tissue mechanics
with agent-based models: concepts, perspectives and some novel results. Comp
Part Mech. 2015;2(4):401–444. doi:10.1007/s40571-015-0082-3.
22. Farhadifar R, R¨oper JC, Aigouy B, Eaton S, J¨ulicher F. The Influence of Cell
Mechanics, Cell-Cell Interactions, and Proliferation on Epithelial Packing. Curr
Biol. 2007;17(24):2095 – 2104. doi:https://doi.org/10.1016/j.cub.2007.11.049.
23. Alt S, Ganguly P, Salbreux G. Vertex models: From cell mechanics to tissue
morphogenesis. Phil Trans R Soc B. 2017;372:20150520.
doi:10.1098/rstb.2015.0520.
24. Drasdo D, H¨ohme S. A single-cell-based model of tumor growth in vitro:
monolayers and spheroids. Phys Biol. 2005;2(3):133–147.
doi:10.1088/1478-3975/2/3/001.
25. Schaller G, Meyer-Hermann M. Multicellular tumor spheroid in an off-lattice
Voronoi-Delaunay cell model. Phys Rev E. 2005;71(5 Pt 1):051910.
12/13


## Page 13


26. Graner F, Glazier JA. Simulation of biological cell sorting using a
two-dimensional extended Potts model. Phys Rev Lett. 1992;69:2013–2016.
doi:10.1103/PhysRevLett.69.2013.
27. Szab´o A, Merks RM. Cellular Potts Modeling of Tumor Growth, Tumor Invasion,
and Tumor Evolution. Front Oncol. 2013;3:87. doi:10.3389/fonc.2013.00087.
28. Basan M, Prost J, Joanny JF, Elgeti J. Dissipative particle dynamics simulations
for biological tissues: rheology and competition. Phys Biol. 2011;8(2):026014.
doi:10.1088/1478-3975/8/2/026014.
29. Podewitz N, Delarue M, Elgeti J. Tissue homeostasis: A tensile state. EPL.
2015;109(5):58005.
30. Marusyk A, Almendro V, Polyak K. Intra-tumour heterogeneity: a looking glass
for cancer? Nat Rev Cancer. 2012;12:323–334.
31. Marusyk A, Polyak K. Tumor heterogeneity: Causes and consequences. Biochim
Biophys Acta. 2010;1805(1):105 – 117.
doi:https://doi.org/10.1016/j.bbcan.2009.11.002.
32. Shackleton M, Quintana E, Fearon ER, Morrison SJ. Heterogeneity in Cancer:
Cancer Stem Cells versus Clonal Evolution. Cell. 2009;138(5):822 – 829.
doi:https://doi.org/10.1016/j.cell.2009.08.017.
33. Nowell P. The clonal evolution of tumor cell populations. Science.
1976;194(4260):23–28. doi:10.1126/science.959840.
34. Allen MP, Tildesley DJ. Computer simulation of liquids. Oxford: Clarendon
Press; 1989.
35. J¨ulich Supercomputing Centre. JURECA: Modular supercomputer at J¨ulich
Supercomputing Centre. Journal of large-scale research facilities. 2018;4(A132).
doi:10.17815/jlsrf-4-121-1.
13/13

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
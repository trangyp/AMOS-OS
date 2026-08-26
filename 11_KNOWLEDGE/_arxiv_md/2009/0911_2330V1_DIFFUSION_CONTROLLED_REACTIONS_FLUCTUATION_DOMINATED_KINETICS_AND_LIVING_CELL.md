---
canon-group: reference
rscf-state: source-claim
arxiv_id: 0911.2330v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 0911.2330v1_Diffusion_Controlled_Reactions__Fluctuation_Dominated_Kinetics__and_Living_Cell_

> Source: 0911.2330v1_Diffusion_Controlled_Reactions__Fluctuation_Dominated_Kinetics__and_Living_Cell_.pdf

> Pages: 10

---


## Page 1


S. Barry Cooper & Vincent Danos (eds.): Fifth Workshop on
Developments in Computational Models—Computational Models From Nature
EPTCS 9, 2009, pp. 98–107, doi:10.4204/EPTCS.9.11
c⃝Z. Konkoli
This work is licensed under the
Creative Commons Attribution License.
Diffusion controlled reactions, ﬂuctuation dominated kinetics,
and living cell biochemistry
Zoran Konkoli
Chalmers University of Technology, Gothenburg, Sweden
Department of Microtechnology and Nanoscience - MC2
Bionano Systems Laboratory
zorank@chalmers.se
In recent years considerable portion of the computer science community has focused its attention
on understanding living cell biochemistry and efforts to understand such complication reaction en-
vironment have spread over wide front, ranging from systems biology approaches, through network
analysis (motif identiﬁcation) towards developing language and simulators for low level biochemical
processes. Apart from simulation work, much of the efforts are directed to using mean ﬁeld equations
(equivalent to the equations of classical chemical kinetics) to address various problems (stability, ro-
bustness, sensitivity analysis, etc.). Rarely is the use of mean ﬁeld equations questioned. This review
will provide a brief overview of the situations when mean ﬁeld equations fail and should not be used.
These equations can be derived from the theory of diffusion controlled reactions, and emerge when
assumption of perfect mixing is used.
1
Introduction
The emphasis of this review is on discussing the use of the framework of diffusion controlled reactions
to model the living cell biochemistry. No attempt is being made to provide a comprehensive list of
references for such a complex ﬁeld. Instead, selected topics have been carefully chosen to help the non-
experts gain the glimpse of the relevant issues. First aim is to introduce general framework for describing
living cell biochemistry and give few examples of mathematical models one needs to solve. Second goal
is to illustrate that the mean ﬁeld equations are lowest order approximation of a more complicated set of
equations. Final aim is to discuss these equations of motion, the way they are solved, and behavior of
solutions.
First, few words about the problem. Chemical reaction kinetics in vivo differs signiﬁcantly from the
one in pipette [1]. Geometry of the living cell interior can be quite complicated and there is experimental
evidence that the cell is structured in many ways, already starting at the cytoplasm level. For example,
for a single cell the total amount of protein content can be as high as 17-30% by weight which results
in extremely structured and crowded space. In addition, the cell interior (roughly 10µm in diameter)
is further partitioned in smaller spaces such as organelles (e.g. mitochondria with 50 nm in diameter),
and roughly 50% of the cell volume is ﬁlled by organelles. For typical physiological concentrations of
individual proteins of 1nM one gets Nprot ∼1nM(10µm)3 ∼1000 copies of individual protein. This can
result in large spatio-temporal ﬂuctuations of protein number. Also, delivery of proteins can become an
issue.
There are two ways to theoretically study such complicated reaction environment, either by per-
forming stochastic simulations or by constructing equations of motion that describe time evolution of
averaged quantities (e.g. concentration). The focus will be on the later. It will be argued that any attempt
to describe intracellular chemical reactions in terms of mean ﬁeld equations (that assume perfect mixing)


## Page 2


Z. Konkoli
99
might fail spectacularly. Intracellular dynamics is intrinsically stochastic due to low number of chem-
icals, exclusion effects are important and, ultimately, many scales interact at the same time with large
degree of spatio-temporal organization. To develop theoretical framework that can be used to describe
such situation is far from trivial. The theory of diffusion controlled reactions naturally suggests itself in
this context. In the following some generic features of diffusion controlled reaction will be discussed
with a particular emphasis on mathematical/physical models that are used to describe them. The validity
of the truncated equation of motion approach will be critically reviewed, with a particular emphasis on
its simplest form, the mean ﬁeld equations/kineteics.
2
Diffusion controlled reactions: mathematical model
Diffusion controlled reactions are ubiquitous in nature. They appear in the matter-antimatter annihilation
in the early universe, epidemics spreading and occur frequently at small scales in the living cell. Few
references on the topic can be found in [2, 3, 4, 5]. Reviews [2, 3] provide gentle introduction to the
ﬁeld. Unfortunately, the ﬁeld of diffusion controlled reaction is rather technical and paper [4] is tutorial
of basic techniques one can use. One dimensional systems are reviewed in [5]. This work provides rather
lengthy account of experimental and theoretical approaches used to describe one dimensional diffusion-
controlled reactions.
Perhaps the simplest way to introduce diffusion-controlled reactions is through two stochastic bench
mark models: the A + A →P or A + B →P reaction diffusion models. (For simplicity reasons, both
reaction result in same product, though this obviously needs not be the case.) It is assumed that one
can clearly separate two time scales in the problem, related to the rates of transport D and the reaction
processes λ.
There are two ways to describe the system, either by using off- or on-lattice models. In this review
on-lattice models will be used, thought results obtained for such model hold for off-lattice models as
well. For example, assuming that the spacing in the lattice is h, continuous models can be obtained by
taking the h →0 limit, and by re-scaling variables in the appropriate way (e.g. see reference [4] for
details).
By assumption, particles A and B move on the lattice with jump rates (diffusion constants) DA ≡D
and DB respectively. Further, it is assumed that a pair of particles X and Y at r and r′ reacts with rate
σX,Y(r −r′) where X,Y ∈{A,B}. Here the assumption of translational invariance have been used. For
simplicity reasons it will be assumed that σA,A(r−r′) = λ∆r,r′ and σA,B(r−r′) = δ∆r,r′ where ∆r,r′ equals
one (zero) for r = r′ (r ̸= r′). More complicated model can be obtained by allowing for ﬁnite reaction
range but such models are much more technical without conveying anything beyond what short range
models already do (within the scope of this review). Please note that in the case of lattice models all rates
have the dimension 1/s. These rates are re-scaled when limit h →0 is taken, leading to the parameters
that can be directly related to experiments.
Reactants and products are conﬁned in a reaction volume V ∼Ld, where L denotes the size of the
system and d dimension. (As will be discussed, the dimensionality of the system is the most important
parameter that governs validity of mean ﬁeld equations.) It is assumed that typical size of molecules
participating in reactions is a. The setup for the A+B reaction is shown in Figure 1. (To visualize A+A
system just imagine that all B particles are changed into A.) Particles A and B can be almost anything,
molecules, excitons, electron-hole pairs, sellers and buyers on the stock market etc. P denotes reaction
product.
Figure 1 depicts three distinct regimes. Panel (a) shows a situation when L ≫a and reactants have


## Page 3


100
Diffusion controlled reactions
A
A
A
A
A
B
P
A
B
A
B
B
P
B
P
B
P
P
Figure 1: A+B reaction in three different regimes. Panel (a): reactant radius a much smaller than size of
the system L. In such a case reactants have lot of space to move. Panel (c): crowded situation where a is
of the same order of magnitude as L. Panel (b) represents intermediate case.
space to move and do not disturb each other. Such situation is often modeled by assuming that the
size of the reaction volume L is inﬁnite. Also it is assumed that products of the reaction P do not
exert inﬂuence on the reactants leading to a simpliﬁcation that reactants annihilate without further trace
leading to A+B →/0 (or A+A →/0). These approximations are very good when L ≫a. Panel (c) shows
an opposite situation when a ∼L (and still a < L). In such a case reactants do not have space to move
and one needs to consider exclusion effects. Panel (c) shows intermediate case. In the following the two
extreme cases (a) and (b) will be discussed. The living cell harbors reactions with both types of behaviors
depending on the relative sizes of reactants and reaction volumes. As time goes on the reaction-diffusion
system exhibits variety of behaviors, as discussed in [6].
System constructed so far is stochastic. To study its behavior one could perform stochastic simu-
lations and there are variety of techniques for doing it. However, in the following another approach is
followed where equations are constructed that describe time evolution of averaged quantities of interest
(various observables such as particle number, correlation functions, variance of particle number etc). In
the following section the generic behavior of the diffusion controlled reactions will be discussed. The
emphasis will be on intuitive understanding. The technical side of the problem will be presented later.
3
Qualitative analysis of diffusion controlled reactions in inﬁnite (large)
volumes
Figure 2 shows a sketch of a snapshot of the A+A →/0 reaction diffusion system. (Later on real ﬁgures
from the simulation will be shown.) Interesting phenomena happen when reaction rate λ is lot larger than
the diffusion rate D. Large spatial density ﬂuctuations may develop as time ﬂows. For that particular
reason it is far from trivial to predict how particle number NA(t) or particle density ρA(t) = NA(t)/V
vanish in time. The problem at hand is a complex many body problem and the mechanism that governs
its behavior is illustrated in the ﬁgure.
Even if reactants were mixed well initially, reactions create spatial ﬂuctuations that diffusion cannot
smear out. Figure 2, panel (b), shows a cavity that is created when A particles, emphasized by gray
shade in panel (a), annihilate. The A particle that is left in the middle of the cavity will not be annihilated
unless diffusion ﬁlls in the cavity by other A particles. However, if diffusion processes are much slower
than the reaction processes D ≪λ it takes longer time to ﬁll the cavity. Even if this cavity is ﬁlled by


## Page 4


Z. Konkoli
101
(a) reactants mixed well
(b) cavity created by reaction
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
Figure 2: Reactions create spatial ﬂuctuations. Diffusion is slow in ﬁlling in the cavity and spatial
ﬂuctuations remain leading to the ﬂuctuation dominated kinetics.
A
A
A
A
A
(a) Domains
(b) Domains slightly mixed
(c) Domains formed again
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
B
B
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
B
B
B
B
B
B
B
A
A
B
B
B
A
A
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
A
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
Figure 3: Spontaneous formation of domains for A+B reaction. Panel (a): Assumption is made that
domains are formed. Panel (b): domains are mixed by diffusion. Diffusion process should ruin domain
structure. Panel (c): Domains get reestablished due to the presence of reactions.
particles there will be other cavities that emerge due to the reactions going on. In such a case dynamics
of the system is plagued by spatial ﬂuctuations in particle density. Since particles are not mixed well it
takes longer time to annihilate all particles.
The ﬂuctuation dominate regime of A+B reaction looks slightly different from the one for A+A re-
action. The behavior of the system differs signiﬁcantly depending on whether DA = DB. In the following
such situation will be only discussed. Figure 3 depicts typical particle distribution when particles are
mixed well (e.g. at t=0) and after the reactions proceed for some time. If D ≪δ domains rich in A or B
particles develop.
Figure 3 shows how reactions lead to spontaneous formation of domains. Even if diffusion tried to
mix particles minority species is immediately annihilated. For example, upper part shows a situation
when two B molecules (in such a case minority species) diffuses into the domain rich with A particles. B
molecules will be immediately annihilated. Same holds for A molecules in the lower part of the panel (b).
The mechanism just discussed indeed show up in the snapshots of the particle distribution that originate
from stochastic computer simulations. Please see Figure 4 for details. The simulation in Figure 4 is done
using improved minimal process algorithm [7] and clearly shows formation of domains. This is a well
know result [10].


## Page 5


102
Diffusion controlled reactions
Figure 4: Snapshots of the A+B reaction dynamics in ﬂuctuation dominated regime. Red denotes A
particles, B denotes blue particles, and white indicates same number of A and B particles. Intermediate
colors correspond to intermediate cases. Black color denotes absence of particles. One can see that
domains rich in A and B particles are formed as time goes on.
4
Mathematical analysis of the diffusion controlled reactions: pair ap-
proach
The type of the kinetics discussed in the previous section is referred to as ﬂuctuation dominated kinetics
since presence of reactions lead to appearance of spatio-temporal ﬂuctuations. Equally often the term
anomalous kinetics is used to describe such systems where in this context ”anomalous” indicates devia-
tion from mean ﬁeld kinetics. The ﬂuctuation dominated kinetics cannot be described using mean ﬁeld
equations and in this section it will be discussed where the problem is.
The problem at hand, i.e. a set of particles moving and reacting on the lattice can be described in
terms of the master equation,
˙P(c,t) = ∑
c′

Rc′→cP(c′,t)−Rc→c′P(c,t)

(1)
where P(c,t) describes probability that system is in the state c at time t. The R(c →c′) denote transition
rates which can be deduced from details of the model described previously. Here and in the following
the dot over a symbol denotes the time derivative.
The observables of interest denote average quantities such as densities ρ(r,t) or correlation functions
ρ(r,r′,t) where r, r′, etc point to lattice sites. There are couple of ways how to obtain equations for
time dependence of observables. For example one can map the problem in Eq. (1) to ﬁeld theory and use
various ﬁeld-theoretic techniques to construct equations of motion. [8, 16] An alternative to this approach
is to construct equations directly starting from (1), as discussed in [4]. In either case calculations are
rather technical and will be omitted. Only ﬁnal form of equations will be stated here. Equations of
motion have the same form regardless whether multiple occupancy or single occupancy of lattice sites are
allowed (though form of boundary conditions might differ). Work in [16] focuses on multiple occupancy
situation while work in [4] deals with single occupancy situation. For large volumes both approaches


## Page 6


Z. Konkoli
103
give essentially the same results.
To illustrate how the mean ﬁeld equations emerge it is useful to look at the simplest possible example,
the A+A annihilation process. After taking the continuum limit (e.g. x = hr, x′ = hr′, etc) the equations
that describe A+A reaction-diffusion system are given by
˙ρ(x,t) = D∇2
xρ(x,t)−
Z
dV ′σ(x−x′)ρ(x,x′,t)
(2)
and two point density is deﬁned through
˙ρ(x,x′,t)
=
D(∇2
x +∇2
x′)ρ(x,x′,t)−σ(x−x′)ρ(x,x′,t)
−
Z
dV ′′ 
σ(x−x′′)+σ(x′ −x′′)

ρ(x,x′,x′′,t)
(3)
Equation (3) shows that two point density depends on three point density. Such behavior continues
ad inﬁnitum. One needs to cut the hierarchy in order to be able to use it. The most common approx-
imation is pair approximation, where book-keeping of pair correlations is only done. This amounts to
approximating three point density as [4, 16]
ρ(x,x′,x′′,t) ≈ρ(x,t)ρ(x′,t)ρ(x′′,t)χ(x,x′,t)χ(x′,x′′,t)χ(x,x′′,t)
(4)
where χ(x,x′,t) denotes pair correlation function deﬁned through ρ(x,x′,t) ≡ρ(x,t)ρ(x′,t)χ(x,x′,t).
Using the pair approximation and after assuming translational invariance, ρ(x,t) = ρ(t) and χ(x,x′,t) =
χ(x−x′,t), results in following equations:
˙ρ(t) = −k(t)ρ(t)2
(5)
where k(t) =
R dVσ(x)χ(x,t) and pair correlation function satisﬁes
˙χ(x,t) = 2D∇2
xχ(x,t)−σ(x)χ(x,t)
(6)
with initial condition given by χ(x,t = 0) = 1, which denotes perfect mixing at t=0.
Equation (5) is always exact while Eq. (6) is valid only in the pair approximation. One can see from
Eq. (5) how mean ﬁeld result emerges. If χ(x,t) = 1, i.e. reactants are mixed all the time, k(t) = λ
becomes constant and one obtains law of classical chemical kinetics, with a solution ρ(t) = ρ0/(1 +
λρ0t) and for large times one has ρ(t) ≈1/λt ∝t−1. The -1 is referred to as a mean ﬁeld exponent.
From ﬁgures 2, 3, and 4 it is clear that χ(x,t) ̸= 1 since diffusion can not mix reactants well. Such
behavior can be traced back to the Eq. (6) where ﬁrst term describes mixing by diffusion and second term
how reactions burn hole in the pair correlation function. Once the equation is solved one can see that for
D ≪λ and d ≤2 pair correlation function never equals one.
To get the correct kinetics rather technical analysis needs to be done for each particular case. Such
analysis is beyond the scope of this review. The results are as follows. For A+A reaction the mean ﬁeld
result holds for d > 2. For d < 2 the correct result is given by
ρ(t) ≈A (d)(Dt)−d/2
(7)
where constant A only depends on the dimensionality of the problem and dependence on the reaction
rate λ has been lost. d/2 is the anomalous kinetics exponent (different from mean ﬁeld exponent for
d < 2). At d = 2 one obtains logarithmic corrections, ρ(t) ∝lnt/t.


## Page 7


104
Diffusion controlled reactions
For the A+B model one has following behavior. To save the space only the case with equal diffusion
constants DA = DB = D and equal amount of A and B particles at t=0, ρA(x,0) = ρB(x,0) = ρ0, will
be discussed. In such a case mean ﬁeld equations reduce to ordinary differential equations in time;
˙ρA(t) = ˙ρB(t) = −δρA(t)ρB(t). One has the same scaling behavior as in the case of A+A reaction;
ρA(t) = ρB(t) ≈1/δt. This is the correct result for d > 4. However, for d < 4 one has anomalous
kinetics with exponent d/4,
ρA(t) = ρB(t) ≈B(ρ0,d)(Dt)−d/4
(8)
The constant B depends both on dimensionality and the initial concentration of particles. To see tech-
nical details of the calculations that lead to the results in (7) and (8) please see [9] and [10, 11, 12]
respectively and references therein. The calculations are rather technical. The A+B has not been solved
yet bellow and at d = 2, though exact derivation of lower and upper bounds exists that conﬁrm critical
exponent in (8).
To illustrate importance of ﬂuctuation dominated kinetics when studying living cell biochemistry an
particular example will be discussed. The model where A+B, A+B, and B+B reactions occur at the same
time was suggested previously [13, 14, 15, 16]. The behavior of the system depends very much on the
equality of diffusion constants. Assumptions DA ̸= DB [13] and DA = DB [14, 15, 16] stem from different
setups and lead to very different behavior of the system.
The DA = DB case is a notorious example of how mean ﬁeld can go wrong. In particular the ABBA
model suggested and studied in [14, 15, 16] shows dramatic failure of mean ﬁeld approach. The model
arises when one wants to include steric effects into the simplest possible way and results in the following
set of reactions: A+A, A+B, and B+B with rates λ, δ, and λ respectively. Please note that the A+A
and B+B reactions have the same rate constant. Also rate constants are such that δ > λ. (The opposite
case can be also studied but is not interesting in the context of this review). The mean ﬁeld equations
for such model are given by ˙ρA = −λρ2
A −δρAρB and ˙ρB = −λρ2
B −δρAρB. By mapping the problem
to Poincare sphere [15] large time behavior is given by ρA(t)/ρB(t) ∝tδ/λ−1, when ρA(0) > ρB(0). The
type of molecule that is minority at t=0 simply has to vanish asymptotically. Majority species survives
only. However, the careful calculation [15, 16] reveals that the ratio ρA(t)/ρB(t) saturates to constant for
large times and minority species survives. This is an example that the mean ﬁeld description spectacularly
fails to describe.
5
Diffusion controlled reactions in restricted geometries
In previous subsections diffusion controlled reactions in the inﬁnite volumes have been discussed. In
here, focus will be shifted on discussing diffusion controlled reactions in restricted geometries. A typical
situation of interest is depicted in ﬁgure 1, panel (c). When size of the reactants is comparable to the
size of system extreme crowding conditions arise and in situation like this one cannot neglect presence
of product molecules (even if back reaction is absent).
Compared to the inﬁnite volume case diffusion controlled reactions in small (restricted) volumes are
relatively unexplored. There are some pioneering efforts in this area, e.g. the work by Khairutdinov and
Serpone, Tachiya, or Ramamurthy; see references [17, 18, 19] for reviews on the subject. In such systems
the number of reactants tends to be small and the effects of ﬂuctuations are enhanced. The methods used
to study bulk situation (inﬁnite volume), if they indeed work, have to be heavily modiﬁed.
The main difference from the case when the volume is ﬁnite is that the particle decay is governed by
an exponential decay law, instead of the power law found in inﬁnite systems. Such behavior comes from
the fact that conﬁguration space becomes strictly discrete. When number of particles becomes low one


## Page 8


Z. Konkoli
105
needs to count them one by one. The average of the number of particles behaves as n(t) = c1 +c2e−E1t +
c3e−E2t + .... In such a case the transition rate operator entering master equation attains eigenvalues
that are well separated. And when time is large enough one has (E1 −Ei)t ≫1 for i = 2,3,4,... and
ﬁrst two terms in the expansion for n(t) dominate resulting in the exponential decay. Please note that
even the very large system with large number of particles might eventually arrive in the regime where
particle/density decay is exponential (e.g. as discussed in [6]).
One can naturally wonder about the usefulness of pair approach in the context of reactions in re-
stricted geometries. It was shown that approach can be used but it has severe drawback in small reactions
volumes when symmetries or conservation laws exist [6].
6
Relevance for understanding the living cell biochemistry
The importance of proper modeling of the living cell biochemistry has been discussed in [20] and there
are couple of reasons why the framework of diffusion controlled reactions and the ﬂuctuation dominated
kinetics are relevant for modeling of the living cell biochemistry. The diffusion is the ubiquitous transport
mechanism in the living cell and there are one million reactions happening in the cell per second. In
that sense the framework of diffusion controlled reactions is certainly right choice of the computational
platform.
Many important biochemical details are not addressed in the reaction-diffusion framework such as
effects related to structured water, chain like structure of molecules, or processes on the time scales
much smaller than the reaction times. Nevertheless, the formalism captures the most important aspects
of the problem with a clear separation between transport and reaction processes and provides a well
deﬁned mathematical formulation of the problem. The structure of the conﬁguration space and transitions
among the states are well deﬁned. Calculation of observables is straight forward, thought technically
complicated. Also, should a need occur one can perform simulation of the system based on the reaction-
diffusion framework.
If one wants to use the diffusion controlled reactions framework couples of issues have to be dealt
with. For example, it is not clear whether to use rather technical diffusion-controlled reactions formal-
ism or simpliﬁed version of it such as mean ﬁeld calculations (classical chemical kinetics). In general,
one cannot say when the classical chemical kinetics is applicable and when expect appearance of the
ﬂuctuation dominated kinetics. There are series of problems where validity of mean ﬁeld equations is an
issue. For example, the stability, sensitivity, or robustness analysis based on mean ﬁeld equations. The
example of the ABBA model discussed in the review shows that even at qualitative level mean ﬁeld can
fail miserably. Thus in general mean ﬁeld kinetics should be used with caution. It is important to be
aware of the risks.
To determine whether mean ﬁeld equations are valid rather lengthy and technical analysis needs to be
done for each new model. Central issue is to identify the critical dimension of the system. For example,
dc = 2 for A+A reaction in the inﬁnite volume, and dc = 4 for A+B reaction for the situation discussed in
previous sections. Unfortunately, power counting techniques from ﬁeld theory do not always work. For
example, using power counting one can predict critical dimension for A+A problem but not for A+B.
The value of critical dimension is determining factor that governs validity of mean ﬁeld equations. In
three dimensions (d=3) A+A reaction does not suffer from anomalous kinetics and mean ﬁeld (classical
kinetics) approach can be safely used. However, if one studies reactions on surface (d=2) or line (d=1)
one has to be careful. The situation is more alarming or A+B reaction. The A+B reaction is always
critical (it always suffers from anomalous kinetics) regardless whether occurring in bulk (d=3), surface


## Page 9


106
Diffusion controlled reactions
(d=2) or line (d=1) since its critical dimension equals dc = 4.
Should one use the computer simulations, there are couple of issues to be aware of. If one solely
counts the particles in the cell then perfect mixing is assumed. In such a case effects related to spatio-
temporal ﬂuctuations are ignored. To go beyond that simpliﬁcation and account for position of particles
one needs to formalize the problem in mathematical terms and naturally ends up using the framework of
diffusion controlled reactions. Simulations done at that level account for most important aspects of the
problem. Also, ﬂuctuation dominated kinetics (if it appears) is automatically taken care of. For example,
one does not need to worry about validity of the mean ﬁeld equations. In that respect, there is no need
to perform rather technical and time consuming analysis, such as ﬁnding the critical dimension of the
system. Simulations are very attractive approach to describing living cell.
However, though extremely useful, in silico experiments are heavily dependent on the computer
resources, the cpu power, the memory etc. There is certainly an upper limit on the number of particles one
can simulate. The equation of motion approach discussed in this review could be interesting alternative
in the situation when there are large number of particles in the system and there are not that many particle
types. Admittedly, the situation in the living cell is the opposite (large number of particle types in low
copy numbers). Nevertheless, equation of motion approach could be useful since it could be adjusted to
describe low particle number as shown in [6].
Extremely important issue is whether effects related to ﬂuctuation dominated kinetics appear in the
living cell and to what extent. The properties of the diffusion controlled reactions discussed in previous
sections might have profound effects on our understanding of the living cell biochemistry. One of the
important question is whether the living cell exploits these properties in any way to successfully perform
its function. For example, the living cell environment exhibits kinetics in all dimensions. As a rule
of thumb, lowering the dimensionality results in increasing deviation from mean ﬁeld results. Two
dimensional reactions at the membrane surface are certainly very different from the one in the bulk. In
that sense ﬂuctuation dominated kinetics should be abundant in the living cell. However, careful analysis
needs to be done, since living cell is ﬁnite.
The problems discussed so far get even more complicated when structure of the cell is taken into
account. New issues emerge that need to be addressed. Understanding interplay between geometrical
shape that sustains the reactions and topological structure of the pathways is one of the central problems.
Ultimately, the question is whether we can understand the shape of the organelles with reference to the set
of reactions they sustain. Unfortunately, the role that the geometry plays for cell function is poorly under-
stood, see review papers [22, 20] and references therein. In that context diffusion controlled reaction can
provide useful tool for that type of analysis. The mathematical platform for studying geometry-reaction
interplay framework (GRIP) have been suggested in [20, 21].
The framework of diffusion controlled reactions is studied extensively in the statistical physics and
chemistry community. However, the study of the ﬂuctuation dominated kinetics has been extensively
done within the statistical physics community. Interestingly, in publications that address computational
cell biology comparatively little attention has been payed to the effects related to ﬂuctuation dominated
kinetics, and in particular validity of mean ﬁeld equation, though some work exists (e.g. [23, 24]). The
goal of this review is to point out these facts.
References
[1] Luby-Phelps, K., Cytoarchitecture and physical properties of cytoplasm: Volume, viscosity. diffusion, intra-
cellular surface area. International Review of Cytology - a Survey of Cell Biology, 2000. 192: p. 189-221.


## Page 10


Z. Konkoli
107
[2] Calef, D.F. and J.M. Deutch, Diffusion-controlled reactions. Annual Review of Physical Chemistry, 1983.
34: p. 493–524.
[3] Mikhailov, A.S., Selected Topics in Fluctuational Kinetics of Reactions. Physics Reports-Review Section of
Physics Letters, 1989. 184(5-6): p. 307-374.
[4] Kotomin, E. and V. Kuzovkov, Phenomenological Kinetics of Frenkel Defect Recombination and Accumu-
lation in Ionic Solids. Reports on Progress in Physics, 1992. 55(12): p. 2079-2188.
[5] Privman, V., Nonequilibrium statistical mechanics in one dimension / edited by Vladimir Privman. 1997,
Cambridge: Cambridge Univ. Press.
[6] Konkoli, Z., A. Karlsson, and O. Orwar, The pair approach applied to kinetics in restricted geometries:
Strengths and weaknesses of the method. Journal of Physical Chemistry B, 2003. 107(50): p. 14077-14086.
[7] Benavraham, D., Computer-Simulation Methods for Diffusion-Controlled Reactions. Journal of Chemical
Physics, 1988. 88(2): p. 941-948
[8] Mattis, D.C. and M.L. Glasser, The uses of quantum ﬁeld theory in diffusion-limited reactions. Reviews of
Modern Physics, 1998. 70(3): p. 979-1001.
[9] Lee, B.P., Renormalization-Group Calculation for the Reaction Ka-]Circle-Divide. Journal of Physics a-
Mathematical and General, 1994. 27(8): p. 2633-2652.
[10] Toussaint, D. and F. Wilczek, Particle Antiparticle Annihilation in Diffusive Motion. Journal of Chemical
Physics, 1983. 78(5): p. 2642-2647.
[11] Lee, B.P. and J. Cardy, Renormalization group study of the A+B-¿0 diffusion-limited reaction (vol 80, pg
971, 1995). Journal of Statistical Physics, 1997. 87(3-4): p. 951-954.
[12] Lee, B.P. and J. Cardy, Renormalization-Group Study of the a+B-]Phi Diffusion-Limited Reaction. Journal
of Statistical Physics, 1995. 80(5-6): p. 971-1007.
[13] Howard, M., Fluctuation kinetics in a multispecies reaction-diffusion system. Journal of Physics a-
Mathematical and General, 1996. 29(13): p. 3437-3460.
[14] Konkoli, Z., H. Johannesson, and B.P. Lee, Fluctuation effects in steric reaction-diffusion systems. Physical
Review E, 1999. 59(4): p. R3787-R3790.
[15] Konkoli, Z. and H. Johannesson, Two-species reaction-diffusion system with equal diffusion constants:
Anomalous density decay at large times. Physical Review E, 2000. 62(3): p. 3276-3280.
[16] Konkoli, Z., Application of Bogolyubov’s theory of weakly nonideal Bose gases to the A+A, A+B, B+B
reaction-diffusion system. Physical Review E, 2004. 69(1): p. 011106.
[17] Khairutdinov, R.F. and N. Serpone, Kinetics of chemical reactions in restricted geometries. Progress in Re-
action Kinetics, 1996. 21(1): p. 1-68.
[18] Ramamurthy, V., Photochemistry in organized and constrained media, ed. V. Ramamurthy. 1991: New York
; Weinheim : VCH, cop. 1991.
[19] Tachiya, M., Diffusion-Controlled Reaction in a Micelle. Chemical Physics Letters, 1980. 69(3): p. 605-607.
[20] Konkoli, Z., Diffusion-controlled reactions in small and structured spaces as a tool for describing living cell
biochemistry. Journal of Physics-Condensed Matter, 2007. 19(6): p. 065149
[21] Konkoli, Z., Interplay between chemical reactions and transport in structured spaces. Physical Review E,
2005. 72(1): p. 011917.
[22] Bray, D., Signaling complexes: Biophysical constraints on intracellular communication. Annual Review of
Biophysics and Biomolecular Structure, 1998. 27: p. 59-75.
[23] Grima, R. and S. Schnell, A systematic investigation of the rate laws valid in intracellular environments.
Biophysical Chemistry, 2006. 124(1): p. 1-10.
[24] Berry, H., Monte Carlo simulations of enzyme reactions in two dimensions: Fractal kinetics and spatial
segregation. Biophysical Journal, 2002. 83(4): p. 1891-1901.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 0911_2330v1_diffusion_controlled_reactions_fluctuation_dominated_kinetics_and_living_cell
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2009/0911_2330V1_DIFFUSION_CONTROLLED_REACTIONS_FLUCTUATION_DOMINATED_KINETICS_AND_LIVING_CELL.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

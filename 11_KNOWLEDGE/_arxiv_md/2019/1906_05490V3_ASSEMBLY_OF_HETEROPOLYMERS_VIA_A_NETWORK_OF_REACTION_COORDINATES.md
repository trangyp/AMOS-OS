---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1906.05490v3
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 1906.05490v3_Assembly_of_heteropolymers_via_a_network_of_reaction_coordinates

> Source: 1906.05490v3_Assembly_of_heteropolymers_via_a_network_of_reaction_coordinates.pdf

> Pages: 23

---


## Page 1


arXiv:1906.05490v3  [cond-mat.stat-mech]  8 Oct 2019
Assembly of heteropolymers via a network of reaction coordinates
D. Chiuchi`u,1 James Ferrare,1, 2 and S. Pigolotti1, ∗
1Biological complexity unit, Okinawa Institute for Science and Technology,
1919-1 Tancha, Onna, Kunigami-gun, Okinawa 904-0412, Japan
2Tulane University, 6823 St Charles Ave, New Orleans, LA 70118, USA
(Dated: October 9, 2019)
Abstract
In biochemistry, heteropolymers encoding biological information are assembled out of equilibrium by
sequentially incorporating available monomers found in the environment. Current models of polymerization
treat monomer incorporation as a sequence of discrete chemical reactions between intermediate meta-stable
states. In this paper, we use ideas from reaction rate theory and describe non-equilibrium assembly of a
heteropolymer via a continuous reaction coordinate. Our approach allows to estimate the copy error and
incorporation speed from the Gibbs free energy landscape of the process. We apply our theory to several
examples, from a simple reaction characterized by a free energy barrier to more complex cases incorporating
error correction mechanisms such as kinetic proofreading.
∗simone.pigolotti@oist.jp
1


## Page 2


I.
INTRODUCTION
DNA, RNA, and proteins are the building blocks of all living systems. These heteropolymers
are assembled to match a template; only a very small number of mismatches with the template is
tolerable for maintaining biological information and for correct functioning of cells. However, the
binding energies of different monomers usually differ by only a few kBT, where kB is the Boltz-
mann constant and T the temperature. This means that, at physiological temperature, mismatches
can not be completely suppressed [1].
Our aim is to describe the chemical processes responsible for these errors. Speciﬁcally, we
consider sequential assembly of heteropolymers where each incorporated monomer can be a right
(r) or a wrong (w) match with a template. These two different outcomes can be represented as
competing chemical reactions
h
+w
-w
hw
+r
-r
hr
(1)
where h is the heteropolymer produced so far, and hr/hw are the same heteropolymer with an
addition of a r/w monomer at the tip, respectively. Each monomer incorporation is iteratively
followed by a new one, so that the whole polymerization process is described by the tree-shaped
network of chemical reactions [2, 3] in Fig. 1a.
To achieve accurate and fast assembly, the reactions in Eq.(1) involve several intermediate
steps, such as initial monomer discrimination [4], kinetic proofreading, [4–6], and mismatch repair
[7, 8].
In general, each one of these error-correction mechanisms contribute simultaneously to
polymerization accuracy, speed [9–17], and energetic cost [14, 18–21].
Two approaches can provide insight into the error-correction mechanisms underlying het-
eropolymer assembly. The ﬁrst approach is to measure their kinetic rates under different ex-
perimental conditions [9]. The second approach is to simulate heteropolymer assembly using
molecular dynamics [22]. From the molecular dynamics, one can project the numerous degrees
of freedom into a 1-dimensional collective variable called reaction coordinate [23]. The reaction
coordinate simpliﬁes a chemical process into a one-dimensional random motion [23–25]. The
parameters of this random motion depend on the underlying reactants dynamics [26–28] and on
the projection technique [23, 28, 29].
While successful in describing protein folding [24, 25, 30] and in modeling reaction rates
2


## Page 3


Polymerization
start
a)
b)
Gibbs f ee
ener y
Gibbs free
energy
FIG. 1. Synthesis of heteropolymers. a) Network of incorporation and removal reactions to synthesize a
heteropolymer. Each edge in the network represent the chemical reaction h ⇌hx where h is the heteropoly-
mer produced so far and hx is the same heteropolymer with addition of monomer x ∈{r,w} at the tip. Three
reactions compete at the nodes of the network: removal of the last incorporated monomer, incorporation of
a r monomer, and incorporation of a w monomer. b) Reaction coordinate description of the incorporation
and removal reactions. The initial and ﬁnal points of the free energy landscapes correspond to the reactants
and products of the incorporation and removal reactions, respectively.
[19, 30], approaches based on reaction coordinates found little use in studies of polymerization
speed and accuracy. In principle, both reactions in Eq. (1) can be described by means of a reaction
coordinate (Fig. 1b). However, to study the complete polymerization process we need to join
the reaction coordinates characterizing each branch in Fig. 1a. Mathematically, this amounts to
impose appropriate boundary conditions at the nodes of the reaction network.
In this paper, we develop a model of heteropolymer assembly based on reaction coordinates,
and use it to compute the accuracy and speed of polymerization in different conditions. The paper
is organized as follows. In Section II, we introduce our model. From the reaction coordinate,
we derive effective incorporation and removal probabilities of right and wrong monomers. In
Section III, we compute the accuracy and speed of a general heteropolymer assembly. In Section
IV we consider examples characterized by different Gibbs free energy landscapes. In Section
V, we generalize our results to a case where the reaction leading to monomer incorporation is
3


## Page 4


complemented by kinetic proofreading. Section VI is devoted to conclusions and perspectives.
II.
MODEL
We deﬁne our model of heteropolymer assembly with reaction coordinates through the fol-
lowing steps. We ﬁrst introduce the reaction coordinate and the free energy landscape in each
chemical reaction of the polymerization network. We then study the dynamics of the reaction co-
ordinate dynamics and its boundary conditions at the nodes of the network. Finally, we compute
the probabilities to incorporate/remove one monomer along each reaction coordinate.
A.
Reaction coordinate and Gibbs free energy of the heteropolymer
We introduce the continuous reaction coordinate y along each edge of the polymerization
network, Fig. 1a. Without loss of generality, we choose the units of the reaction coordinate so that
y ∈[0,1], where y = 0 and y = 1 correspond to h and hx respectively, i.e. to the states before and
after monomer incorporation, see Figure 1.b.
Each point along this reaction coordinate is characterized by a Gibbs free energy Ghx(y) (from
now on simply ”free energy”). Such free energy depends on the previously incorporated sequence
of monomers (h), on the candidate monomer to be incorporated (x) and on the stage of the incor-
poration process, i.e. the value of y. Implicitly, Ghx(y) also depends on the reactant and product
concentrations.
We introduce the free energy increments from the beginning of each incorporation reaction
∆Gx(y) = Ghx(y)−Ghx(0),
(2)
see Fig. 2. The free energy increments depend on the candidate monomer x but not on the whole
history of incorporated monomers h. With this notation, the (absolute) binding free energy of
monomer x is equal to −∆Gx(1).
The free energy must be a continuous function of y, and must also vary continuously when
crossing the nodes of the network in Fig. 1. This means that we can decompose the free energy at
4


## Page 5


Heteropolymer
Gibbs free
energy
FIG. 2. Free energy G...(y) of the heteropolymer depends on the reaction coordinate y, and the sequence of
incorporated monomers. The superscript of the free energy indicates the stage of the polymerization process
(either h, h˜x, or h˜xx in this case). The functions ∆G˜x(y) and ∆Gx(y) are the free energy increments along
the reaction coordinate to incorporate ˜x and x respectively. The total binding free energies for monomer ˜x
and x are −∆G˜x(1) and −∆Gx(1), respectively.
an arbitrary stage of the polymerization process as
Ghx(y) =Ghx(0)+∆Gx(y)
=Gh(1)+∆Gx(y)
=(∑
i∈h
∆Gi(1))+∆Gx(y).
(3)
B.
Stochastic dynamics of the reaction coordinate and boundary conditions
Because of thermal ﬂuctuations, the reaction coordinate y evolves according to a Langevin
equation
dy
dt = −µ d
dyGhx(y)+
√
2D ξ(t)
(4)
where µ is a mobility, D is a diffusion coefﬁcient, and ξ(t) is white noise with ⟨ξ(t)⟩= 0 and
⟨ξ(t)ξ(t′)⟩= δ(t −t′) [31]. We assume that D satisﬁes the Einstein relation D = kBTµ with tem-
perature T and Boltzmann constant kB.
We also assume that D, µ, and T are constant. When
5


## Page 6


the reaction coordinate reaches the boundaries, either y = 0 or y = 1, a new incorporation/removal
reaction is commenced.
Equation (4) needs to be complemented by rules to specify which reaction initiates at the nodes
of the reaction network. To this aim, we consider two intermediate values of the reaction coor-
dinate: y = ε and y = 1 −ε with ε ≪1. Using these values we coarse-grain the evolution of the
reaction coordinate y as
(y = 0)
πx
0,ε
ÐÐ⇀
↽ÐÐ
πx
ε,0
(y = ε)
πx
ε,1−ε
ÐÐÐ⇀
↽ÐÐÐ
πx
1−ε,ε
(y = 1−ε)
πx
1−ε,1
ÐÐÐ⇀
↽ÐÐÐ
πx
1,1−ε
(y = 1)
(5)
where the quantities πx
˜y,y are ﬁrst-passage probability from y to ˜y. For example, πx
1−ε,ε is the
probability that the reaction coordinate reaches y = 1−ε from y = ε without having reached y = 0
before.
The representation in Eq.(5) separates the dynamics in proximity of the nodes of Fig. 1.b,
from the dynamics in the interval [ε,1−ε]. Thanks to this separation, we use detailed balance,
probability conservation close to the nodes, and the continuity of Ghx(y) to compute the ﬁrst-
passage probabilities πx
ε,0 and πx
1−ε,1 (see Appendix A). This procedure results in
πx
ε,0 = πx
1−ε,1 = 1
3 +O(ε).
(6)
We compute the ﬁrst-passage probabilities in the interior applying standard techniques [31, 32] to
the Fokker-Planck equation associated to Eq. (4). We obtain
πx
0,ε = ∫
1−ε
ε
ψx(y)dy
∫
1−ε
0
ψx(y)dy
πx
ε,1−ε = ∫
1
1−ε ψx(y)dy
∫
1
ε ψx(y)dy
πx
1−ε,ε = ∫
ε
0 ψx(y)dy
∫
1−ε
0
ψx(y)dy
πx
1,1−ε = ∫
1−ε
ε
ψx(y)dy
∫
1
ε ψx(y)dy
(7)
with
ψx(y) =exp[∫
y
0
µ
D
∂∆Gx(z)
∂z
dz]
=exp[∆Gx(y)
kBT
]
(8)
where the last equality follows from the relation D = kBTµ.
6


## Page 7


C.
Effective probabilities of monomer incorporation/rejection
From the probabilities πx
˜y,y, we now compute the effective probabilities px→and px←to incor-
porate and reject monomer x along each edge of the reaction network in Figure 1. To this end,
we assume that the coarse grained dynamics in Eq.(5) is at steady state. We then use adiabatic
elimination [33] to obtain (see Appendix B)
px
→=ε
3
1
∫
1
0 exp[∆Gx(y)
kBT ]dy
+O(ε)
(9a)
px
←=ε
3
e
∆Gx(1)
kBT
∫
1
0 exp[∆Gx(y)
kBT ] dy
+O(ε)
(9b)
Equations (9) relate the free energy landscapes Gx(y) and the incorporation/removal probabil-
ities of the polymerization process. They are consistent with the detailed balance condition
px→
px←
= exp[−∆Gx(1)
kBT
].
(10)
which connects the ratios of forward and backward probabilities to the binding free energy
−∆Gx(1), see Fig. 2.
III.
RESULTS
We now address the accuracy and speed of a polymerization process in the reaction coordinate
framework. We consider a copy polymer made up of a number Nr of right monomers and Nw of
wrong monomers with N = Nr +Nw. For large N, we deﬁne the error rate
η = lim
N→∞
Nw
N .
(11)
To compute η from the incorporation and removal probabilities px→and px←, we ﬁrst recast Eq.(11)
into the implicit equation
η
1−η = lim
N→∞
Nw
Nr = lim
n→∞
nw→−nw←
nr→−nr←
(12)
where we have introduced the numbers nr→, nr←, nw→and nw←of r and w incorporation and removal
reactions which have occurred in the process, and n is the total number of observed chemical
reactions. For large n we have
nr
→∼nc pr
→
(13a)
7


## Page 8


nr
←∼nc(1−η) pr
←
(13b)
nw
→∼nc pw
→
(13c)
nw
←∼ncη pw
←
(13d)
where c=[pr→+(1−η)pr←+pw→+ηpw←]−1 is a normalization constant so that n =nr→+nr←+nw→+nw←=
n. Substituting Eqs. (13) into Eq. (12) gives
η
1−η =
pw→−ηpw←
pr→−(1−η)pr←
(14)
Equation (14) is a general ”self-consistency” relation for the error rate that holds also for dis-
crete models of polymerization [2, 3, 14]. In our case, we substitute Eqs. (9) in Eq. (14) and take
the limit ε →0, obtaining
η
1−η =
⎛
⎜
⎝
η −exp[−∆Gw(1)
kBT ]
1−η −exp[−∆Gr(1)
kBT ]
⎞
⎟
⎠
⎛
⎜
⎝
exp[∆Gw(1)−∆Gr(1)
kBT
] ∫
1
0 exp[∆Gr(y)
kBT ] dy
∫
1
0 exp[∆Gw(y)
kBT ] dy
⎞
⎟
⎠
.
(15)
Solving Eq. 15 for η yields an explicit expression of the error rate from the energy potentials.
Equation 15 identiﬁes different regimes of error correction. To identify a ﬁrst regime, we
observe that
η =
1
1+exp[∆Gw(1)−∆Gr(1)
kBT
]
if
exp[∆Gw(1)−∆Gr(1)
kBT
] ∫
1
0 exp[∆Gr(y)
kBT ] dy
∫
1
0 exp[∆Gw(y)
kBT ] dy
= 1,
(16)
In the regime where Eq. (16) holds, the error depends only on the binding free energy difference
∆Gw(1)−∆Gr(1). This regime is called energetic discrimination regime in the literature [3, 16].
Systems near equilibrium operates in this regime because the Boltzmann factors of the binding
free energies determine, via detailed balance, the probabilities to incorporate different monomers.
To identify a second error-correction regime in Eq. (15), we consider the case where ∆Gr(y)
and ∆Gw(y) are characterized by energy barriers with heights δ r and δ w respectively (see Figure
1.b and Kramers [19]). When such barriers are large, we can approximate the integrals in Eq. (15)
by using the Laplace method [34]
∫
1
0 exp[∆Gr(y)
kBT ] dy
∫
1
0 exp[∆Gw(y)
kBT ] dy
≈exp[δ r −δ w
kBT
]
√
Σw
Σr
(17)
where Σr and Σw are the curvatures of ∆Gr(y) and ∆Gw(y) at their maxima, respectively. Equation
17 implies that activation barriers suppress the polymerization error via the second term in round
8


## Page 9


brackets in Eq. (15). The regime where this suppression occurs is the kinetic discrimination
regime [3, 16]. The ﬁrst factor on the right-hand side of Eq. (17) represents the contribution of a
difference in activation energy barrier δ r −δ w to accuracy.
This effect is also present in models
based on discrete-step reactions [2, 3, 16, 18]. The factor
√
Σw/Σr is a correction to activation
energies based on the width of the activation barriers. This factor permits kinetic discrimination
at equal barrier heights, provided that the barrier for right monomers is signiﬁcantly more narrow
than for wrong monomers.
We estimate the average polymerization speed using a similar argument to that leading to Eq.
(15). For large number N of incorporated monomers, the average speed is equal to N divided the
total time T needed to assemble the polymer
v = lim
N→∞
N
T
= lim
N→∞
(nr→−nr←)+(nw→−nw←)
T
(18)
where we expressed N in terms of the number of incorporation/removal reactions. For large N we
can approximate the polymerization time as
T ∼n⟨τ⟩
(19)
where ⟨τ⟩is the average time it takes to either incorporate or remove a monomer. Substituting
Eqs. (13) and (19) into Eq. (18) gives the estimate for the polymerization speed
v = c[pr→−(1−η)pr←+ pw→−ηpw←]
⟨τ⟩
.
(20)
The numerator of Eq. (18) is the probability of an incorporation minus the probability of a
removal, while the denominator provides the timescale of these events. In practice, calculating
⟨τ⟩is not straightforward since one has to take into account contributions from incorporation
attempts that are not ﬁnalized. In Appendix C, we provide a more formal derivation of Eq. (20),
together with an explicit expression for ⟨τ⟩.
IV.
EXAMPLES
To address the validity and practical implications of Eqs. (15) and (20) we consider two exam-
ples of potentials ∆Gr(y) and ∆Gw(y).
In both cases, we work in dimensionless units by ﬁxing
D = 1, kBT = 1, and µ = 1.
9


## Page 10


A.
Linear potential
As ﬁrst example we consider linear free energy landscapes
∆Gr(y) = −mry
(21a)
∆Gw(y) = −mwy.
(21b)
Despite their simplicity, the potentials in Eq. (21) are useful to understand the physics of the
process. Upon increasing the slopes mr and mw, polymerization becomes increasingly irreversible.
Substituting the potentials Eq. (21) into the expression for the error, Eq. (15) and performing the
integrals we obtain
η
1−η =
mw(1−e−mr)[1−e−mwη]
mr(1−e−mw)[1+e−mr(1−η)],
(22)
which implies
η =
mw
mr +mw
for
mr,mw ≫1.
(23)
The exact solution of Eq. (22) shows that the error is approximately a function of mw/mr when
mr, mw are large, as predicted by Eq. (23), Fig. 3a. We compared the predictions from Eqs. (22)
and (20) with numerical simulations of the incorporation process from Eq.(4). Our theory yields
reliable predictions for a broad range of parameters, Fig. 3c and 3d.
B.
Potential with an activation barrier
As a second example we consider the potential
∆Gx(y) =ax
⎛
⎜
⎝
e
−
(y−1
2 )2
2c2x
−e
−1
8c2x
⎞
⎟
⎠
+ bx
2
⎛
⎜
⎝
2cx + 1
2 −y
√
(2cx + 1
2 −y)
2 +c2x
−
2cx + 1
2
√
(2cx + 1
2)
2 +c2x
⎞
⎟
⎠
(24)
where ax, bx and cx are monomer-dependent parameters that control the shape of the free energy
potentials. Key features of the potential of Eq. (24) are the binding energy −∆Gx(1), the height
of the activation barrier δ x and its width σx = 4cx, Fig. 4.
We study this model for different cases, corresponding to different parameter choices. In the
ﬁrst case we ﬁx −∆Gr(1) = −∆Gw(1) upon choosing br = bw = b and cr = cw = 1/20. This enforces
a kinetic discrimination regime [3] where the binding energy −∆Gr(1) quantiﬁes the degree of
irreversibility. For highly irreversible processes, the error η should mainly depend on the activation
energy difference δ r −δ r, see Eq. (17). We also expect that the reaction speed should increase for
10


## Page 11


b)
c)
a)
d)
30
20
10
0
0.1
0.1
0.2
0.2
0.2
0.3
0.3
0.3
0.4
0.4
0.4
0.5
0.5
0.5
0.5
0.6
0.6
0.6
0.7
0.7
0.8
0.8
0.9
0.9
30
20
10
0
5
10
10
15
15
15
20
20
20
25
25
30
20
10
0
30
20
10
0
=1
=8.5
=31
30
20
10
0
1.0
0.8
0.6
0.4
0.2
0
=16
=23.5
30
20
10
0
10
20
30
40
0
=1
=31
=8.5
=16
=23.5
FIG. 3. Error rate η and velocity v for linear free energy landscapes . (Top) surface plots of η and v from
Eqs. (15) and (20) when Gr(y) = −mry and Gw(y) = −mwy as a function of the irreversibility parameters mr
and mw. (Bottom) Error η and speed v as a function of mw for different values of mr. Crosses represent the
average η and v values measured from 700 numerical simulations of the stochastic incorporation process.
The Langevin dynamics of Eq. (4) was integrated with the Euler-Maruyama scheme [35].
more irreversible processes. Equations (15) and (20) conﬁrm such qualitative picture, see Figure
5a and b. Also in this case, numerical simulations are in excellent quantitative agreement with our
theory, Fig. 5c and 5d.
As a second case, we ﬁx ar = aw = 5 and br = bw = 1. In this way we have that −∆Gr(1) ≈
−∆Gw(1) and δ r ≈δ w. Energetics alone would not permit monomer discrimination in this case
[3]. However, Eq. (17) predicts that the difference in the barrier widths σr and σw should allow
to discriminate r and w monomers (see Figure 6.a). We conﬁrmed the existence of such kinetic
discrimination regime with numerical simulations, Fig. 6.c.
11


## Page 12


Energy
landscape
FIG. 4. Free energy potentials with a barrier for r and w monomers from Eq. (24) for r and w monomers.
We chose the parameters so that the free energy landscapes for r and w monomers have different binding
energies (−∆Gr(1) and −∆Gw(1)), different barrier heights (δ r and δ w), and different barrier widths (σ r
and σ w).
V.
KINETIC PROOFREADING
In this Section we sketch a generalization of our framework to include kinetic proofreading
[5, 6]. We assume that the reaction h ⇌hx can be decomposed into three sub-reactions
h
p1,x
→
p1,x
←
hx∗
p3,x
←
p3,x
→
h
p2,x
→
p2,x
←
hx
(25)
where each sub-reaction occurs with probabilities pi,x
→s and pi,x
←s, and hx∗is an intermediate meta-
stable complex. The extra pathway hx∗⇌h represents kinetic proofreading. Such reaction can
improve accuracy when driven towards the reactants h, so that wrong monomers undergo an addi-
tional checkpoint. [3, 5].
Every sub-reactions in Eq. (25) is described by its own reaction coordinate y which evolves
according to a Langevin equation
dy
dt = −µ d
dyGi,x(y)+
√
2D ξ(t)
(26)
where Gi,hx(y) is the free energy landscapes along the i-th sub-reaction. Also in this case we take
y ∈[0,1] for all sub-reactions, with y = 1 always in the direction of incorporation of monomer x.
12


## Page 13


a)
c)
1
5
10
0.05
0.05
0.05
0.1
0.1
0.1
0.2
0.2
0.2
0.3
0.3
0.3
0.4
0.4
0.4
0.5
0.5
0.5
0
2
4
6
8
10
0
2
4
6
8
10
0
2
4
6
8
10
0.1
0.2
0.4
0.5
0
0.3
d)
0.5
1
1
1.5
1.5
1.5
2
2
2
2.5
2.5
3
0
2
4
6
8
10
0
2
4
6
8
10
1
5
10
0
2
4
6
8
10
1
2
3
FIG. 5. Equations (15) and (20) predict η and v in a kinetic discrimination regime. (Top) contour plots
of η and v from Eqs. (15) and (20) as a function of the activation energy difference δ w −δ r and the
binding energy −∆Gr(1). In this example, we chose ar = 1, br = bw and cr = cw = 1/20 to ensure a kinetic
discrimination regime where ∆Gr(1) = ∆Gw(1). Large values of −∆Gr(1) correspond to highly irreversible
processes. (Bottom) Plots of η and v versus the activation energy difference δ w −δ r at ﬁxed values of
∆Gr(1). Crosses corresponds to the average values of η and v measured from 300 stochastic simulations of
the incorporation process with Eq.(4). The Langevin dynamics was simulated with a weak 2.0 Runge-Kutta
stochastic scheme [35].
Similarly to Eq. (3), we decompose the free energies for the sub-reactions as
G1,h˜xx(y) =∆G1,x(y)+G2,h˜x(1)
(27a)
G2,h˜xx(y) =∆G2,x(y)+G1,h˜xx(1)
(27b)
G3,h˜xx(y) =
⎧⎪⎪⎪⎪⎨⎪⎪⎪⎪⎩
∆G3,x(y)+G2,h˜x(1)
for hx∗→h
∆G3,x(y)+G1,h˜xx(1)
for hx∗←h
(27c)
where we speciﬁed that monomer ˜x was incorporated before attempting to incorporate monomer
13


## Page 14


a)
c)
d)
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
10-1
10-2
10-1
10-2
10-1
10-2
0.3
0.8
0.6
0.5
0.9
1.0
0.7
1.2
0.4
0.2
1.1
10-1
10-2
1.0
0.8
0.6
0.4
0.2
0
10-1
10-2
10-1
10-2
1.0
0.5
0
FIG. 6. Different barrier widths allow for kinetic discrimination in the absence of binding and activation
energy differences. (Top) surface plots of η and v from Eqs. (15) and (20) as a function of the barrier
widths σr and σw. To ensure that Gr(y) and Gw(y) have approximately the same binding and activation
energies we ﬁxed ar = aw = 5, br = bw = 1, and cr,cw ≤0.05. (Bottom) Plots of η and v versus σw for selected
values of σ r. Crosses corresponds to the average η and v values measured from 400 simulations of the
incorporation process with eq.(4). The Langevin dynamics was simulated with the weak 2.0 Runge-Kutta
stochastic scheme [35].
x. Here, G3,h˜xx(y) depend on the direction of the sub-reaction because the heteropolymer total
energy now depends also on the sequence of sub-reactions.
We now compute the probabilities pi,x
→s and pi,x
←with i ∈{1,2,3} from Eq. (26) with the same
procedure which leads to Eq.(9). This yields
pi,x
→=ε πi,x
ε,0
1
∫
1
0 exp[∆Gi,x(y)
kBT
]dy
+O(ε)
(28a)
pi,x
←=ε πi,x
1−ε,1
e
∆Gi,x(1)
kBT
∫
1
0 exp[∆Gi,x(y)
kBT
]dy
+O(ε).
(28b)
14


## Page 15


with
π1,x
ε,0 = π2,x
1−ε,1 = π3,x
ε,0 = 1
5
(29a)
p1,x
1−ε,1 = π2,x
ε,0 = π3,x
ε,0 = 1
3.
(29b)
Equations (29) state that the all sub-reactions from reactants h and hx∗respectively can start with
equal probabilities.
To obtain an equation for η, we need to compute the effective incorporation and removal prob-
abilities px→and px←in Eq. (14) from Eqs. (28) and (29). To this end we assume that the reactions
in Eq.(25) are at steady state. We then use adiabatic elimination [33] to obtain (see Appendix D)
px
→= p2,x
→(p1,x
→+ p3,x
→)
p1,x
←+ p3,x
←+ p2,x
→
(30a)
px
←= p2,x
←(p1,x
←+ p3,x
←)
p1,x
←+ p3,x
←+ p2,x
→
(30b)
Substituting Eqs. (28) and (30) in Eq. (14) ﬁnally provides an expression for η in terms of the
free energy landscapes Gi,x(y).
VI.
CONCLUSIONS
In this paper, we described assembly of heteropolymers by means of continuous reaction coor-
dinates. In the simplest cases, our results are consistent with those derived for reactions occurring
in discrete steps [2, 3, 10, 12–14, 16, 17]. Moreover, our formalism reveals discrimination mech-
anisms that are not easily described with discrete reactions. One example is the possibility to
discriminate according to barrier widths, as described by Eq. (17) and conﬁrmed in simulations,
Fig. 6c.
For simplicity, in this paper we developed our formalism by means of a reaction coordinate
characterized by a Markovian dynamic. In general, only speciﬁc projection techniques yield re-
action coordinates with negligible non-Markovian contributions [23, 28, 29, 36], and the resulting
Langevin equation might not be in the form of Eq. (4).
Our framework can be adapted to
such situations as well as to non-Markovian reaction coordinates, describing for example enzymes
undergoing slow conformational changes.
The framework described here is microscopically reversible. This allows to characterize non-
equilibrium work and heat exchanges during the polymerization process from the diffusive dy-
namics of the reaction coordinate, similarly to recent studies of the ATP synthase [37, 38] and
15


## Page 16


small-scale technological devices [39, 40]. This analysis would permit to characterize thermody-
namic limits of information processing of these processes [14, 41–43].
ACKNOWLEDGMENTS
This work was supported by JSPS KAKENHI Grant Number JP18K03473 (to DC and SP).
Appendix A: First passage time probabilities at the nodes
Because of detailed balance, the probabilities πx
ε,0 and πx
1−ε,1 are related to the free energy
difference when passing from one edge of the reaction network to another, i.e.
πx
ε,0 ∝exp[−Gh˜xx(ε)
kBT
]
π ˜x
1−ε,1 ∝exp[−Gh˜x(1−ε)
kBT
].
(A1)
where we speciﬁed that the monomer ˜x ∈{r,w} was incorporated before monomer x ∈{r,w}. After
the incorporation of ˜x, the enzyme can catalyze three reactions: removal of ˜x or incorporation of
either r or w. The probabilities of these three events must be normalized
π ˜x
1−ε,1 +πr
ε,0 +πw
ε,0 = 1.
(A2)
Combining Eqs.(A1)-(A2) gives
πx
ε,0 =
exp[−Gh˜xx(ε)−Gh˜x(1−ε)
kBT
]
1+exp[−Gh˜xr(ε)−Gh˜x(1−ε)
kBT
]+exp[−Gh˜xw(ε)−Gh˜x(1−ε)
kBT
]
(A3a)
π ˜x
1−ε,1 =
1
1+exp[−Gh˜xr(ε)−G˜x(1−ε)
kBT
]+exp[−Gh˜xw(ε)−Gh˜x(1−ε)
kBT
]
.
(A3b)
Substituting Eq.(3) into Eq.(A3), taking the limit of small ε, using the continuity of Gh˜xx(y) and
then renaming ˜x with x ﬁnally gives Eq.(6).
Appendix B: Effective incorporation and removal probabilities
The dynamics of the reaction coordinate y in the coarse grained description of Eq.(5) obeys a
Markov chain
Px
0(ν +1) =πx
0,εPx
ε (ν)+[1−πx
ε,0]Px
0(ν)+external ﬂuxes
(B1a)
16


## Page 17


Px
ε (ν +1) =πx
ε,0Px
0(ν)+πx
ε,1−εPx
1−ε(ν)+[1−(πx
0,ε +πx
1−ε,ε)]Px
ε (ν)
(B1b)
Px
1−ε(ν +1) =πx
1−ε,εPx
ε (ν)+πx
1−ε,1Px
1(ν)+[1−(πx
ε,1−ε +πx
1,1−ε)]Px
1−ε(ν)
(B1c)
Px
1(ν +1) =πx
1,1−εPx
1−ε(ν)+[1−πx
1−ε,1]Px
1(ν)+external ﬂuxes.
(B1d)
where the ﬁrst-passage probabilities appear as transition probabilities, and the quantities Px
0(ν),
Pε(ν), P1−ε(ν), and P1(ν) are the probabilities that the reaction coordinate reaches the point y = 0,
y = ε, y = 1−ε and y = 1 after ν consecutive transitions respectively. The external ﬂuxes in Eqs.
(B1a) and (B1d) are the probability ﬂuxes from the remaining reactions which originate from the
nodes y = 0 and y = 1 in the network of Figure 1.a.
To simplify Eq. (B1) we perform adiabatic elimination [33] of the intermediate states y = ε and
y = 1−ε: we impose the steady state regime Pxε (ν +1) = Pxε (ν) and Pxε (ν +1) = Pxε (ν) in Eqs.(B1b)
and (B1c) respectively, we solve Eqs.(B1b)-(B1c) for Pxε (ν) and Px
1−ε(ν), and we ﬁnally substitute
the result back into Eqs.(B1a), (B1d). This yield the effective Markov chain
Px
0(ν +1) =px
←Px
1(ν)+[1−px
→]Px
0(ν)+external ﬂuxes
(B2a)
Px
1(ν +1) =px
→Px
0(ν)+[1−px
←]Px
1(ν)+external ﬂuxes .
(B2b)
where we have deﬁned the effective probabilities px→and px←to incorporate a monomer (h →hx)
and remove a monomer (h ←hx) respectively as
px
→=
πx
1,1−επx
1−ε,επx
ε,0
πx
1,1−ε πx
1−ε,ε +πx
0,ε πx
ε,1−ε +πx
0,ε πx
1,1−ε
(B3a)
px
←=
πx
0,ε πx
ε,1−ε πx
1−ε,1
πx
1,1−ε πx
1−ε,ε +πx
0,ε πx
ε,1−ε +πx
0,ε πx
1,1−ε
.
(B3b)
Substituting Eq.(6)-(8) into Eq. (B3) and then expanding for small ε ﬁnally gives Eq. (9).
Appendix C: Derivation of the polymerization speed via reaction coordinates.
To derive the polymerization speed, we consider a mean ﬁeld formulation of the polymeriza-
tion process in Figure 1.a where the enzyme can remove any monomer in the copy heteropolymer.
Removal of r and w monomers occurs with probabilities 1−η and η respectively. This assumption
simpliﬁes the reaction tree of Figure 1.a into the closed network of Fig. 7.a, where the incorpora-
tion and removal probabilities px→and px←are deﬁned as in Eq. (9).
17


## Page 18


a)
FIG. 7. Mean ﬁeld representation of the polymerization process. a) Mean ﬁeld version of the heteropolymer
assembly in Figure 1.a where the enzyme can remove any monomer in h. Removal involves r and w
monomers (1 −η) and η times respectively. The probabilities px
→, px
←are deﬁned as in Eq. (9). The
constant c = [pr
→+ (1−η)pr
←+ pw
→+ η pw
←]−1 normalizes the probabilities and is deﬁned as in Eqs. (13).
b) Same as in panel a, but we have now explicitly introduced the intermediate reaction coordinate values
y = ε and y = 1−ε, as well as the transition probabilities πx
y,˜y deﬁned as in Eqs. (6) and (7). The constant
c′ = [πr
ε,0 +(1−η)πr
1−ε,1 +πw
ε,0 +ηπw
1−ε,1] normalizes the probabilities exiting from the central node.
We now introduce the reaction coordinate in this mean ﬁeld description, Fig. 7.b. For later
convenience, we also consider the values of the reaction coordinate y = 0 y = ε, y = 1−ε and y = 1
together with the probabilities πx
˜y,ys deﬁned in Eqs.(6) and (7).
Using the scheme in Figure 7.b, we deﬁne the probability P0,1(ζ) that y = 0 or y = 1 after ζ
consecutive transitions, and the probabilities Prε(ζ), Pr
1−ε(ζ), Pw
ε (ζ), Pw
1−ε(ζ) that y = ε or y = 1−ε
for the r and w monomer after ζ consecutive transitions. These probabilities evolves according to
the Markov chain
⃗P(ζ +1) = A ⃗P(ζ)
(C1)
where
⃗P(ζ) = (P0,1(ζ),Pr
ε(ζ),Pr
1−ε(ζ),Pw
ε (ζ),Pw
1−ε(ζ))
T
(C2)
18


## Page 19


and
A =
⎡⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣
0
πr
0,ε
πr
1,1−ε
πw
0,ε
πw
1,1−ε
c′πr
ε,0
0
πr
ε,1−ε
0
0
c′(1−η)πr
1−ε,1 πr
1−ε,ε
0
0
0
c′πw
ε,0
0
0
0
πw
ε,1−ε
c′ηπw
1−ε,1
0
0
πw
1−ε,ε
0
⎤⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦
(C3)
where c′ = [πr
ε,0 +(1−η)πr
1−ε,1 +πw
ε,0 +ηπw
1−ε,1] is a normalization constant. We now deﬁne the
matrices
JN = 1
3
⎡⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣
0 −1 +1 −1 +1
+1 0 −1 0
0
−1 +1 0
0
0
+1 0
0
0 −1
−1 0
0 +1 0
⎤⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦
(C4a)
JT =
⎡⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣
0
⟨dτ⟩r
0,ε
⟨dτ⟩r
1,1−ε
⟨dτ⟩w
0,ε
⟨dτ⟩w
1,1−ε
⟨dτ⟩r
ε,0
0
⟨dτ⟩r
ε,1−ε
0
0
⟨dτ⟩r
1−ε,1 ⟨dτ⟩r
1−ε,ε
0
0
0
⟨dτ⟩w
ε,0
0
0
0
⟨dτ⟩w
ε,1−ε
⟨dτ⟩w
1−ε,1
0
0
⟨dτ⟩1−ε,ε
0
⎤⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦
(C4b)
which contain the contribution of each transition to the heteropolymer length N and the polymer-
ization time T . The time increments ⟨dτ⟩x
y,˜y in JT are the ﬁrst passage times from ˜y to y [31]. In
particular we have that
⟨τ⟩x
0,ε = 1
D
⎛
⎝Φx
→(0)−∫
1
0 Φx→(y)dy
∫
1
0 ψx(y)dy
⎞
⎠ε +O(ε2)
(C5a)
⟨τ⟩1−ε,ε = 1
D ∫
1
0 Φx
←(y)dy+O(ε)
(C5b)
⟨τ⟩ε,1−ε = 1
D ∫
1
0 Φx
→(y)dy+O(ε)
(C5c)
⟨τ⟩x
1,1−ε = 1
D
⎛
⎝Φx
←(1)−(e
∆Gx(1)
kBT ) ∫
1
0 Φx←(y)dy
∫
1
0 ψx(y)dy
⎞
⎠ε +O(ε2)
(C5d)
with
Φx
→(y) =
ψx(y)∫
1
y ∫
1
u
ψx(z)
ψx(u)dzdu
∫
1
0 ψx(y)dy
(C6a)
19


## Page 20


Φx
←(y) =
ψx(y)∫
y
0 ∫
u
0
ψx(z)
ψx(u)dzdu
∫
1
0 ψx(y)dy
.
(C6b)
The remaining ﬁrst passage times ⟨dτ⟩r
ε,0, ⟨dτ⟩r
1−ε,1, ⟨dτ⟩w
ε,0 and ⟨dτ⟩w
1−ε,1, are assumed equal
to zero for simplicity. Physically, this assumption is justiﬁed when binding and unbinding of
monomers is much faster than processing a monomer into a ﬁnalized incorporation.
Using Eq.(C4) we deﬁne the tilted matrix B with components
Bi, j = Ai, j exp[qNJN
i, j +qτJτ
i, j]
(C7)
and dummy variables qN, and qτ. For large values of ζ, the largest eigenvalue of B coincides with
the scaled cumulant generating function of N and T , see [44]. The implicit function theorem then
implies
N ≈−ζ ∂qN det[B−λI]
∂λ det[B−λI] ∣
qN=qτ=0,λ=1
(C8a)
T ≈−ζ ∂qτ det[B−λI]
∂λ det[B−λI] ∣
qN=qτ=0,λ=1
(C8b)
where det[B−λI] is the characteristic polynomial of B. To compute v we ﬁnally use that
v = N
T = ∂qN det[B−λI]
∂qτ det[B−λI] ∣
qN=qτ=0,λ=1
.
(C9)
which is equivalent to Eq.(18). Substituting Eqs.(6), (7), (C3), (C4) and (C7) into Eqs.(C9) and
then taking the leading order for small ε yields Eq. (20), where
⟨τ⟩D
c
=(pr
→−(1−η)pr
←)(∫
1
0 [Φr
←(y)−Φr
→(y)]dy)+(pw
→−ηpw
←)(∫
1
0 [Φw
←(y)−Φw
→(y)]dy)
+ε
3
⎛
⎝Φr
→(0)+Φw
→(0)+(1−η)Φr
←(1)+ηΦw
←(1)⎞
⎠+O(ε2)
(C10)
and c is deﬁned as in Eq. (13).
Appendix D: Effetive incorporation and removal probabilities for the Kinetic proofreading exam-
ple
To compute the incorporation and removal probabilities for the Kinetic proofreading case we
mimic the procedure that leads to Eq.(9). We consider the probabilities Ph(ξ), Phx∗(ξ) and Phx(ξ)
20


## Page 21


to obtain the reactants h, hx∗, and hx after ξ sub-reactions of Eq. (25). These probabilities evolve
according to the Markov chain
Ph(ξ +1) = p1,x
←Phxx(ξ)+[1−(p1,x
→+ p3,x
→)]Ph(ξ)+external ﬂuxes
(D1a)
Phx∗(ξ +1) = p1,x
→Ph(ξ)+ p2,x
←Phx(ξ)+ p3,x
→Ph(ξ)+[1−(p1,x
←+ p2,x
→+ p3,x
←)]Phx∗(ξ)
(D1b)
Phx(ξ +1) = p2,x
→Phx∗(ξ)+[1−p2,x
←]Phx(ξ)+external ﬂuxes,
(D1c)
where the external ﬂuxes are the probability ﬂuxes of the other sub-reactions entering the nodes
y = 0 and y = 1. At steady state, we simplify Eq. (D1) with adiabatic elimination[33]: we impose
Phx∗(ξ +1) = Phx∗(ξ) into Eq. (D1b), solve it for Phx∗(ξ) and substitute the solution in Eqs. (D1a)
and (D1c). This yields, after some rearrangements,
Ph+x(ξ +1) = px
←Phx(ξ)+[1−px
→]Ph+x(ξ)
(D2a)
Phx(ξ +1) = px
→Ph+x(ξ)+[1−px
←]Phx(ξ)
(D2b)
with effective incorporation/removal probabilities px→and px←deﬁned as in Eq.(30).
[1] N. M. Reynolds, B. A. Lazazzera, and M. Ibba, Nature Reviews Microbiology 8, 849 (2010).
[2] C. H. Bennett, BioSystems 11, 85 (1979).
[3] S. Pigolotti and P. Sartori, Journal of Statistical Physics 162, 1167 (2016).
[4] T. A. Kunkel and K. Bebenek, Annual Review of Biochemistry 69, 497 (2000), pMID: 10966467.
[5] J. J. Hopﬁeld, Proceedings of the National Academy of Sciences 71, 4135 (1974).
[6] J. Ninio, Biochimie 57, 587 (1975).
[7] M. ODonnell, L. Langston, and B. Stillman, Cold Spring Harbor Perspectives in Biology 5 (2013), 10.1101/cshperspec
[8] T. A. Kunkel and D. A. Erie, Annual Review of Genetics 49, 291 (2015), pMID: 26436461.
[9] M. V. Rodnina and W. Wintermeyer, Annual Review of Biochemistry 70, 415 (2001), pMID:
11395413.
[10] D. Andrieux and P. Gaspard, Proceedings of the National Academy of Sciences 105, 9516 (2008).
[11] M. Johansson, M. Lovmar, and M. Ehrenberg, Current Opinion in Microbiology 11, 141 (2008), cell
Regulation.
[12] P. Gaspard and D. Andrieux, The Journal of Chemical Physics 141, 044908 (2014).
[13] K. Banerjee, A. B. Kolomeisky, and O. A. Igoshin, Proceedings of the National Academy of Sciences 114, 5183 (2017)
21


## Page 22


[14] P. Sartori and S. Pigolotti, Phys. Rev. X 5, 041039 (2015).
[15] Y. Savir and T. Tlusty, Cell 153, 471 (2013).
[16] P. Sartori and S. Pigolotti, Phys. Rev. Lett. 110, 188101 (2013).
[17] A. Murugan, D. A. Huse, and S. Leibler, Proceedings of the National Academy of Sciences 109,
12034 (2012).
[18] F. Cady and H. Qian, Physical biology 6, 036011 (2009).
[19] H. Kramers, Physica 7, 284 (1940).
[20] R. Rao and L. Peliti, Journal of Statistical Mechanics: Theory and Experiment 2015, P06001 (2015).
[21] J. A. Wagoner and K. A. Dill, Proceedings of the National Academy of Sciences 116, 5902 (2019),
https://www.pnas.org/content/116/13/5902.full.pdf.
[22] L. V. Bock, M. H. Kol, and H. Grubmller, Current Opinion in Structural Biology 49, 27 (2018).
[23] P. V. Banushkina and S. V. Krivov, Wiley Interdisciplinary Reviews: Computational Molecular Science 6, 748 (2016),
https://onlinelibrary.wiley.com/doi/pdf/10.1002/wcms.1276.
[24] N. D. Socci, J. N. Onuchic, and P. G. Wolynes, The Journal of Chemical Physics 104, 5860 (1996).
[25] R. B. Best and G. Hummer, Phys. Rev. Lett. 96, 228104 (2006).
[26] R. Zwanzig, Phys. Rev. 124, 983 (1961).
[27] A. M. Berezhkovskii and A. Szabo, The Journal of Physical Chemistry B 117, 13115 (2013).
[28] J. Lu and E. Vanden-Eijnden, The Journal of Chemical Physics 141, 044109 (2014).
[29] S. V. Krivov and M. Karplus, The Journal of Physical Chemistry B 110, 12689 (2006), pMID:
16800603.
[30] D. K. Klimov and D. Thirumalai, Phys. Rev. Lett. 79, 317 (1997).
[31] C. Gardiner, Stochastic Methods: A Handbook for the Natural and Social Sciences, Springer Series in
Synergetics (Springer Berlin Heidelberg, 2009).
[32] S.
Iyer-Biswas
and
A.
Zilman,
“First-passage
processes
in
cellular
biology,”
in
Advances in Chemical Physics (John Wiley and Sons, Ltd, 2016) Chap. NONE, pp. 261–306.
[33] S. Pigolotti and A. Vulpiani, The Journal of Chemical Physics 128, 154114 (2008).
[34] C. Bender and S. Orszag, Advanced Mathematical Methods for Scientists and Engineers I: Asymptotic
Methods and Perturbation Theory, Advanced Mathematical Methods for Scientists and Engineers
(Springer, 1978).
[35] P. Kloeden and E. Platen, Numerical Solution of Stochastic Differential Equations, Stochastic Mod-
elling and Applied Probability (Springer Berlin Heidelberg, 2011).
22


## Page 23


[36] S. V. Krivov, Journal of Chemical Theory and Computation 14, 3418 (2018).
[37] J. N. E. Lucero, A. Mehdizadeh, and D. A. Sivak, Phys. Rev. E 99, 012119 (2019).
[38] A. K. S. Kasper and D. A. Sivak, , 1 (2019), arXiv:1905.10640.
[39] I.
Neri,
M.
Lopez-Suarez,
D.
Chiuchi´u,
and
L.
Gammaitoni,
EPL (Europhysics Letters) 111, 10004 (2015).
[40] M. L´opez-Su´arez, I. Neri, and L. Gammaitoni, Nature Communications 7, 12068 EP (2016), article.
[41] A. B´erut,
A. Arakelyan,
A. Petrosyan,
S. Ciliberto,
R. Dillenschneider,
and E. Lutz,
Nature 483, 187 EP (2012).
[42] Y. Jun, M. c. v. Gavrilov, and J. Bechhoefer, Phys. Rev. Lett. 113, 190601 (2014).
[43] D. Chiuchi´u, EPL (Europhysics Letters) 109, 30002 (2015).
[44] H. Touchette, Physics Reports 478, 1 (2009).
[45] T. Pape, W. Wintermeyer, and M. Rodnina, The EMBO Journal 18, 3800 (1999).
[46] S. Redner, A Guide to First-Passage Processes, A Guide to First-passage Processes (Cambridge Uni-
versity Press, 2001).
[47] K. B. Gromadski and M. V. Rodnina, Molecular Cell 13, 191 (2004).
[48] H. S. Zaher and R. Green, Cell 136, 746 (2009).
[49] M.
F.
Goodman,
S.
Creighton,
L.
B.
Bloom,
J.
Petruska,
and
D.
T.
A.
Kunkel,
Critical Reviews in Biochemistry and Molecular Biology 28, 83 (1993), pMID: 8485987.
[50] D. N. Wilson and J. H. Doudna Cate, Cold Spring Harbor Perspectives in Biology 4 (2012), 10.1101/cshperspect.a0115
[51] U. Hbscher, G. Maga,
and S. Spadari, Annual Review of Biochemistry 71, 133 (2002), pMID:
12045093.
[52] S. S. Patel, I. Wong, and K. A. Johnson, Biochemistry 30, 511 (1991).
[53] C. A. Brautigam and T. A. Steitz, Current Opinion in Structural Biology 8, 54 (1998).
[54] K. Sekimoto, Stochastic Energetics, Lecture Notes in Physics (Springer Berlin Heidelberg, 2010).
[55] U. Seifert, Physica A: Statistical Mechanics and its Applications 504, 176 (2018), lecture Notes of
the 14th International Summer School on Fundamental Problems in Statistical Physics.
[56] U. Seifert, Reports on Progress in Physics 75, 126001 (2012).
[57] M. Gavrilov and J. Bechhoefer, Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engine
https://royalsocietypublishing.org/doi/pdf/10.1098/rsta.2016.0217.
23

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1906_05490v3_assembly_of_heteropolymers_via_a_network_of_reaction_coordinates
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1906_05490V3_ASSEMBLY_OF_HETEROPOLYMERS_VIA_A_NETWORK_OF_REACTION_COORDINATES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

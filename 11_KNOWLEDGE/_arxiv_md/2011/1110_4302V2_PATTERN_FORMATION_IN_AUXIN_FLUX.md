---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1110.4302v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1110.4302v2_Pattern_formation_in_auxin_flux

> Source: 1110.4302v2_Pattern_formation_in_auxin_flux.pdf

> Pages: 27

---


## Page 1


Pattern formation in auxin ﬂux
Chrystel Feller, Jean-Pierre Gabriel, Christian Mazza∗and Florence Yerly
November 27, 2021
Abstract
The plant hormone auxin is fundamental for plant growth, and its spatial distribution in plant
tissues is critical for plant morphogenesis. We consider a leading model of the polar auxin ﬂux, and
study in full detail the stability of the possible equilibrium conﬁgurations. We show that the critical
states of the auxin transport process are composed of basic building blocks, which are isolated in a
background of auxin depleted cells, and are not geometrically regular in general. The same model
was considered recently through a continuous limit and a coupling to the von Karman equations, to
model the interplay of biochemistry and mechanics during plant growth. Our conclusions might be
of interest in this setting, since, for example, we establish the existence of Lyapunov functions for the
auxin ﬂux, proving in this way the convergence of pure transport processes toward the set of critical
conﬁgurations.
1
Introduction
The plant hormone auxin plays a fundamental role in plant development (Reinhardt et al., 2000, 2003),
and its spatial distribution in plants tissues is critical for plant morphogenesis. Auxin accumulation is
spatially localized in speciﬁc set of cells, where it induces the emergence of new primordia (Reinhardt
et al., 2000). A fundamental problem consists in understanding how such auxin maxima appear, and
how they induce the regular pattern observed in plants (see e.g. Hamant and Traas, (2009)). On the
other hand, experiments show that phyllotaxis strongly depends on the plant physical properties, more
precisely on elasticity (Green, 1980; Dumais and Steele, 2000; Dumais, 2007), and physical forces provide
information for plant patterning (Hamant and Traas, 2009). Basically, turgor pressure induces stress,
which is related to the associated deformation or strain through Young constants: see e.g. Boudaoud,
(2010) where these notions are explained in the context of plant growth. Experiments have shown that
lowering the stiﬀness of cell walls in the meristem leads to the emergence of new primordia (Hamant
et al., 2008). However, the interactions between physics-based and biochemical control of phyllotaxis is
still poorly understood.
Recently, new biologically plausible mathematical models of auxin transport have been proposed (Bar-
bier de Reuille et al., 2006; Heisler, 2006; Jönsson et al., 2006; Smith et al., 2006), each of them being able
to reproduce some aspects of phyllotaxis in simulations. New mathematical models were also proposed for
the plant mechanics (Mjolsness, 2006), and for the interaction between mechanics and biochemistry (Ship-
man and Newell, 2005; Newell et al., 2008). In the latter, the authors use the model for the polar auxin
ﬂux proposed in Jönsson et al., (2006) for modelling the stress ﬁeld in their mechanical model. It should
be stressed that all these models are based on hypotheses that have not been veriﬁed experimentally;
however they provide new scenari for understanding plant growth that can be tested experimentally.
∗Corresponding author, Département de Mathématique, Université de Fribourg, Chemin du Musée 23, CH-1700 Fribourg,
Suisse, christian.mazza@unifr.ch
1
arXiv:1110.4302v2  [q-bio.TO]  24 Oct 2011


## Page 2


Figure 1: Inﬂorescence shoot apical meristem of Arabidopsis thaliana. Zones with high auxin concen-
tration are highlighted by the ﬂuorescent yellow signal auxin reporter from DR5::YFP. The red signal is
highlighting cell walls stain, using propidium iodide.
Auxin occurs in various plant tissues, where it is transported by polar cellular transport in various
directions and can explain developmental patterning phenomena such as vein formation, see e.g. Scarpella
et al., (2006) or Bayer et al., (2009).
In the following, we consider the models in Jönsson et al., (2006) and Smith et al., (2006), based on
polar auxin ﬂux. Polar auxin ﬂux results from uneven accumulation of the auxin transport regulator
PIN in cell membranes.
An essential component is a positive feedback between auxin ﬂux and PIN
localization, resulting in the reinforcement of polar auxin transport to dedicated routes which develop
into vascular tissues. We will not enter here into these considerations, but focus on simple models of
transport processes (see e.g. the discussion in Jönsson et al., (2006) and Shipman and Newell, (2005)),
where a quasi-equilibrium is assumed for PIN proteins. The molecules present in some cell i may be
transported to any neighbouring cell j, but they are preferentially transported to the neighbours with
the highest auxin concentrations.
Traditionally, models of patterning and morphogenesis have used reaction-diﬀusion theory. Turing demon-
strated how, under some hypotheses, the regular patterns observed in phyllotaxis can be predicted (Tur-
ing, 1952). He showed that a combination of diﬀusion and a chemical reaction could give rise to regular
patterns. Interesting models are described in Meinhardt, (1982); Thornley, (1975) which can, under some
hypotheses, predict phyllotactic patterns. As stated previously, the auxin ﬂux is strongly polarized, a
phenomenon that cannot be described with reaction-diﬀusion models. The recent mathematical models
given in Barbier de Reuille et al., (2006); Jönsson et al., (2006); Smith et al., (2006) are based on trans-
port processes. Mathematically, mass transport processes are not well understood, and their study is a
challenging problem. We propose here a mathematical study of related dynamical systems. We focus on
their critical points and analyse their geometrical structure and stability.
Besides stable auxin peaks, the model generates intervening areas of auxin depletion, as it is observed
experimentally. These auxin depleted sites reﬂect an indirect repulsion mechanism since auxin molecules
diﬀusing through the tissue will be attracted to the peaks, and diverted from the depleted areas. This
idea of repulsion or spacing mechanism was already considered a long time ago (Hofmeister, 1868).
The auxin ﬂux is present everywhere in the plant, so that we choose to describe the various plant cells
as a connected graph (Λ, E). The node set Λ represents the cells and E the set of edges. Any edge
e = (i →j), i, j ∈Λ indicates that some auxin molecule can move from cell i to cell j. This graph is
undirected, and we write i ∼j to denote that cells i and j are nearest neighbours, so that auxin can move
from cell i to cell j, at some rate qij. These transition rates are not well understood at present time and
one must rely on simple models. They should capture the fact that an auxin molecule present in some
cell i has the tendency to move to a cell j ∼i when the concentration aj of auxin molecules present in
2


## Page 3


cell j is high. The simplest model accounting for this idea is given by Jönsson et al., (2006)
qij =
aj
κ + P
k∼i ak
,
(1)
for some positive constant κ, which is of Michaelis-Menten or Monod type. Let L = |Λ| be the number
of cells. In the model given in Jönsson et al., (2006) (see also Smith et al., (2006); Sahlin et al., (2009)),
ai(t), for i = 1, · · · , L, denotes the concentration or the number of auxin molecules in cell i at time t,
and is assumed to evolve according to the diﬀerential equations
dai
dt = fi(a) = D
X
k∼i
(ak −ai) + T
X
k∼i

ak
ai
κ + P
j∼k aj
|
{z
}
=qki(a)
−ai
ak
κ + P
j∼i aj
|
{z
}
=qik(a)

,
(2)
for i = 1, . . . , L. The term aiqik gives the mean number of auxin molecules moving from cell i to cell k
per unit time, and D P
k∼i(ak −ai) is a diﬀusive part, usually assumed to be weak with a small diﬀusion
coeﬃcient D. The second term corresponds to the mass transport process, which is known to be the
main actor of the patterning process in plants. One can add auxin production and degradation terms,
but, there is no clear biological evidence about where auxin is produced, and experiments show that it is
not produced in the meristem, but imported from the leaves (Reinhardt et al., 2000, 2005).
1.1
Results
Direct quantitative measurements of auxin distribution in plant tissues are very diﬃcult due to the small
size of the meristematic tissues at the time of patterning. Therefore, biologists rely on indirect markers
based on auxin-regulated genes that encode ﬂuorescent proteins. Figure 1 shows a typical output, where
domains rich in auxin appear as regions of strong green ﬂuorescence. The pattern is quite noisy; this
might be due either to the indirect experiments, or to the fact that the number of auxin molecules is
not too high. (2) might model the limiting behavior of this random particle system when the number of
molecules tends to inﬁnity. We introduce such a particle system in Section 2 and justify equations like
(2) using law of large numbers.
We then focus on the properties of (2), like the non-negativity of the solutions (see Proposition 3.1). This
dynamical system can be written in the compact form
da
dt = f(a),
where a(t) = (ai(t))1≤i≤L is the vector of auxin concentrations. The related critical points are the vectors
a∗satisfying f(a∗) = 0. They are the candidates for describing the equilibrium auxin concentrations.
For example, ai = 0 means that there is (almost) no auxin molecules in cell i, while a subset of cells J
such that aj > 0 for j ∈J indicates a hot spot which might correspond to an auxin peak.
The critical points play a fundamental role in the dynamic, and one can suspect that any solution a(t) of
(2) will approach such critical points as t is large. Of course, this is wrong for general dynamical systems,
but here, the model is supposed to catch pieces of biological reality, and the robustness of the regular
geometries observed in plants suggests that this might well be the case. Some of these critical points are
repulsive or unstable, that is, the orbits or the solutions of (2) will avoid them. In the contrary, some of
them will be attractive. Given a critical point a∗, a mathematical way of checking the stability or the
unstability of a∗is to compute the Jacobian df(a∗), by retaining only its spectrum, that is the set of
all eigenvalues of df(a∗). For example, a∗is unstable when there is an eigenvalue having a positive real
part.
Deﬁnition 1.1 We say that a critical point a is stable when all the eigenvalues of the Jacobian evaluated
at a have non-positive real parts.
3


## Page 4


Section 5 is concerned with the characterization of the set of critical points, mainly focusing on pure
transport processes.
For D = 0, we ﬁrst consider critical points a > 0, meaning that ai > 0 for all i. Corollary 5.3 shows that
such elements are precisely the positive solutions of the linear equation
Γa = c 1, c constant,
(3)
where Γ is the adjacency matrix of the graph G, with entries Γij ∈{0, 1} such that Γij = 1 if and only
if cells i and j are nearest neighbours, and 1 is the vector having all components equal to 1.
Next, we focus on critical points such that ai = 0 for i belonging to some subset I ⊂Λ = {1, · · · , L}.
They correspond to auxin depleted cells. The graph decomposes into a product of sub-graphs γ, which
are the connected components of the sub-graph of G induced by the node set J = Λ\I. We thus look for
a having positive components aj > 0 for j ∈J, which should correspond in some sense to auxin peaks.
We obtain the distribution of auxin in such components, denoted by a|γ, by solving the linear systems
Γγa|γ = cγ1|γ. A typical example of such conﬁgurations is given in Figure 3, where the elements of I are
black and the various components γ red.
We then turn to the asymptotic behavior of the solutions of system (2), and establish in Proposition
6.3 that every solution converges toward the set of critical points. Our technique is based on Lyapunov
functions, that is, we look for a function H(a) which should be decreasing along the orbits of (2), like
energy in physics. We proved that, for pure transport processes with D = 0, the function
H(a) = −κ⟨1, a⟩−1
2⟨a, Γa⟩,
where ⟨·, ·⟩denotes the scalar product, satisﬁes
dH(a(t))
dt
≤0
for any solution of (2). Newell et al., (2008) also considered the diﬀerential system (2) by taking a spatial
continuous limit, and showed that the limiting equation is a p.d.e. similar to the von Karman equations
from nonlinear elasticity theory:
∂w
∂t = △2w + P△w + const · w + nonlinear terms.
The von Karman equations are of gradient type (see e.g.
Shipman and Newell, (2005)), where the
potential is given by the elastic energy. These energy functionals were then used in Newell et al., (2008)
and Newell and Shipman, (2005) to provide a very interesting mechanical explanation of the appearance
of Fibonacci numbers in plant patterns based on buckling. However, the limiting equations associated
with the auxin ﬂux are not of gradient type, see the discussion in Newell et al., (2008). For the basic
dynamical system (2), our result shows that the system is minimizing the energy H, without being of
gradient type.
Section 7 considers stability, and Proposition 7.1 shows that the Jacobian df(a) = (∂fi/∂aj) evaluated
at a is given by
df(a) =
1
N 2 d(a)Γ

c id −d(a)Γ

,
where d(a) is the diagonal matrix of diagonal given by a. This permits to check the stability of the
critical points for various graphs. We present various results on graphs of interest for plant patterning
questions, like the circle or the two-dimensional grid. As stated previously, the positive solutions a|γ to
the linear system Γγa|γ = cγ1|γ provide restrictions of the critical points to the connected components
γ. We give a particularly simple condition on the sub-graph γ of G induced by the set J = Λ\I ensuring
the non-stability of a|γ. Let Ni, i ∈Λ be the neighbourhood of i, that is the set of nodes j such that
4


## Page 5


j ̸= i and j ∼i. The conﬁguration a|γ is unstable when the sub-graph γ contains a path of length 4, of
the form
i0 →i1 →i2 →i3,
such that
i1 ∈Ni0, i2 ̸∈Ni0 and i3 ̸∈Ni0.
Figure 2: Example of components γ of the two-dimensional grid that can potentially yield stable conﬁg-
urations, see Corollary 7.3.
For example, if G is a two-dimensional grid, any stable conﬁguration is composed of patches of the basic
building blocks given in Figure 2; These patterns are however not geometrically regular in general, see
Figure 3. The more involved model of Smith et al., (2006), which uses PIN proteins in a direct way (here
we assume a quasi-equilibrium, see Jönsson et al., (2006)), produces more regular patterns in simulations.
In this setting, the transition rates are forced to follow exponential distributions. Hence, a strong selection
based on rates of the form exp(bai), b > 0 instead of the linear function ai seems to regularize the critical
points. Of course, it might be interesting to justify such a choice biologically. We also argue in what
follows that the critical conﬁgurations produced by the auxin ﬂux might be more regular when coupled
to periodic potentials.
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
Figure 3: A potentially stable conﬁguration when the graph G is a rectangular grid, for the pure transport
process. The black circles correspond to the values ai = 0, i ∈I (the set auxin depleted cells), while the
red circles are such that ai > 0, corresponding to auxin peaks. One can construct the set of all stable
conﬁgurations by playing with the building block given by the square, the star, and the various parts of
the star. This shows that dynamical system (2) does not necessarily produce regular patterns. We can
however give examples where such conﬁgurations are unstable, see Section 7.3
It might well be that the auxin ﬂux self-organize in regular patterns when coupled to mechanical forces,
for example, as already stated in the Introduction, see Newell et al., (2008).
In the same spirit, we
introduce a simple model coupling the auxin ﬂux to a potential φ, which might model deformations,
5


## Page 6


(a) a(t) for t ≈0
(b) a(t) for large t.
Figure 4: Simulation of the orbits of the diﬀerential equation (4) with T = 1, D = 0 and a potential
φ(x, y) = sin(4πx/A) sin(4πy/B) on a torus, where x = 1, · · · , A and y = 1, · · · , B. The initial state is
ﬂat. (b) shows the state a(t) for large t: one sees regularly spaced auxin peaks, which are isolated in
a background of auxin depleted cells. The potential and transport terms drift thus the process toward
more regular patterns, while the transport process creates domains of auxin depletion.
curvature or eﬀects related to the meristem elasticity. We provide an example of the form
dai(t)
dt
= fi(a) +
X
j∼i
(ajφi −aiφj),
(4)
i = 1, . . . , L. If the potential itself has some regularities, as it is the case in speciﬁc model given in Newell
et al., (2008), the auxin ﬂux will exhibit much more regular patterns, see e.g. Figure 4.
Finally, the model provides an interesting conclusion: for most graphs, stable conﬁguration are composed
of building blocks isolated in a sea of auxin depleted cells. This might be the basis for repulsion between
primordia: auxin molecules will not have the tendency to move toward them, leading to indirect repulsion.
The idea of such repulsive force appeared a long time ago in the work of Hofmeister, (1868). Many authors
have used this hypothesis to develop very interesting mathematical models, all leading to phyllotactic
patterns observed in nature, like Fibonacci numbers, the Golden Angle or helical lattices, see Adler,
(1974); Atela et al., (2002); Douady and Couder, (1996); Kunz, (1995); Levitov, (1991).
2
A stochastic model of auxin transport
We consider a stochastic process related to diﬀerential equation (2), describing the random numbers of
auxin molecules ηt(i) ∈N present in cell i at time t, i = 1, · · · , L. The state space of this stochastic
process is denoted by ΩL = NΛ, where Λ is the set of L cells (the nodes of the graph). Looking at
equation (2), we deﬁne transitions by supposing that any auxin molecule present in cell i at time t can
be transported to a neighboring cell j at rate ¯qij(η) of the form
¯qij(η) =
η(j)
¯κ + P
k∼i η(k),
(5)
when η(i) ≥1. This deﬁnes a Markov process with state space ΩL, describing the stochastic moves of
the various auxin molecules. Let M denote the total number of molecules. It turns out that the ordinary
diﬀerential equation (2) describes the large M limit of the stochastic process (weak noise limit). This
random particle system is then described as a gaussian process XM(t) ≈ηt/M in RL drifted by the
solution a(t) of (2) for some covariance function. This approximation will be mathematically rigourous
if the constants κ and ¯κ are related in such a way that ¯κ = Mκ, and the limiting behavior of the rescaled
number of auxin molecules is such that ηt(i)/M ≈ai(t), where a(t) solves (2), with P
i∈Λ ai(t) ≡1.
6


## Page 7


Such stochastic particle systems are known as density dependent population processes, and the above
limit has been treated in detail in Ethier and Kurtz, (1986), and corresponds to a law of large numbers.
Notice that diﬀerent kinds of limits can also be considered. Stochastic mass transport processes of this
type have also appeared in physics, and are known as generalized zero range processes, see e.g. Evans
et al., (2006); Luck and Godrèche, (2007); Grosskinsky et al., (2011); Kipnis and Landim, (1999). In this
setting, hydrodynamical limits are considered, when both M and L tend simultaneously to ∞in such a
way that M = ρL, for a ﬁxed density. Simulations show the appearance of condensates when ρ is larger
than a critical threshold ρc, which might represent auxin peaks in some way. Mathematically, the theory
of condensation is not developed at present time for these general processes, so that we here focus on the
weak noise limit.
The gaussian approximation of ηt/M is deﬁned as follows: for i = 1, · · · , L, consider the unit vectors ei
with ei(j) = 0 when j ̸= i and ei(i) = 1. Let df be the Jacobian df = (∂fi/∂aj))i,j=1,··· ,L.
For simplicity, we illustrate the transition rates for cells arranged along a circle: the rate functions are
given by functions βl(a), l ∈Zl, satisfying
βei+1−ei(a) = (Dai + T
ai+1ai
κ + ai−1 + ai+1
) ;
for i = 1, . . . , L,
βei−1−ei(a) = (Dai + T
ai−1ai
κ + ai−1 + ai+1
) ;
for i = 1, . . . , L,
βl(a) = 0
for ; l ̸= ei−1 −ei, ei+1 −ei.
For example ei+1 −ei means that an auxin molecule of cell i has been transported in cell i + 1. For
arbitrary graphs, the deﬁnitions of the rates βl are similar.
With these notations, we can deﬁne the matrix G
G(a) =
X
l∈ZL
βl(a)ll∗,
which will be an essential element of the covariance matrix associated with the gaussian approximation.
Consider the following matrix valued diﬀerential equation
∂φ(t, s)
∂t
= df(a(t))φ(t, s),
φ(s, s) = id.
Then, as M is large, one gets that (see e.g. (Ethier and Kurtz, 1986))
ηt
M = a(t) +
1
√
M
Vt,
where Vt is a gaussian process of mean φ(t, 0)V (0) and of covariance function
Cov(V (t), V (r)) =
Z min{t,r}
0
φ(t, s)G(a(s))φ(r, s)∗ds.
3
Basic properties of the auxin ﬂux
Proposition 3.1 Every solution a of (2) starting in RL
≥0 remains non-negative, and is conservative,
that is,
∀t ∈R≥0,
L
X
i
ai(t) =
L
X
i
ai(0) = ρL.
Moreover, the system (2) admits a unique solution deﬁned over [0, +∞). When ai(0) > 0, then ai(t) > 0,
∀t > 0. For pure transport processes with D = 0, ai(0) = 0 ⇒ai(t) ≡0, ∀t > 0.
7


## Page 8


The proof of proposition 3.1 is given in Section 8.
Let us rewrite the system (2), for 1 ≤i ≤L
˙ai = D
X
k∼i
ak + T
X
k∼i
(
ak
κ + P
j∼k aj
−
ak
κ + P
j∼i aj
−D
T )ai,
(6)
with the initial condition a(0) ∈RL
+.
Proposition 3.2 If the graph is connected and D > 0, the only critical point of (6) in RL
+ admitting
zero components is the origin.
Proof :
Let ai = 0 where ai is the i-th component of a critical point a ∈RL
+ of (6). Clearly (6) entails P
k∼i ak = 0
and the non-negativity of each term, ak = 0 for all k ∼i. Since the graph is connected we deduce that
ak = 0 for all 1 ≤k ≤L. □
Proposition 3.3 Let us assume that the graph is connected and D > 0. If PL
k=1 ak(0) > 0, then for all
i ∈{1, ..., L}, we have limt→+∞ai(t) > 0.
To prove the previous proposition, we will use the following Proposition, see Gabriel et al., (1989).
Proposition 3.4 Let f : R+ →R be twice diﬀerentiable and bounded together with ¨f. If, as n →+∞,
tn ↑+∞and f(tn) →limt→+∞f(t) (or f(tn) →limt→+∞f(t)), then ˙f(tn) →0.
Remark 3.5
(1) The boundedness of f and ¨f implies the one of ˙f.
(2) The assumptions in the preceding proposition can be weakened without changing essentially the proof:
"f : R+ →R be twice diﬀerentiable and bounded together with ¨f " can be replaced by "f : R+ →R
is bounded and diﬀerentiable and ˙f is uniformly continuous".
Proof :
If ak(0) = 0 for all 1 ≤k ≤L, then the unique solution is identically zero. Otherwise PL
k=1 ak(0) > 0.
Let us suppose that for some i ∈{1, ..., L},
limt→+∞ai(t) = 0.
Let us introduce the notation ai = limt→+∞ai(t).
Since ai(t) is bounded together with its second
derivative, the preceding proposition applies and for any sequence tn ↑+∞such that ai(tn) →ai, we
have ˙ai(tn) →0 as n →+∞. Every ak(tn) being bounded in the right-hand member of the equation
for ˙ai(tn), we conclude that limn→+∞D P
k∼i ak(tn) = 0. The non-negativity of each ak(tn) entails
limn→+∞ak(tn) = 0 = ak for every k ∼i. According to the above proposition, limn→+∞˙ak(tn) = 0 for
every k ∼i and since the graph is connected, repeating the same argument provides limn→+∞˙aj(tn) = 0
for every j ∈{1, ..., L}. Thus 0 = limn→+∞
P
1≤j≤L aj(tn) = PL
k=1 ak(0) > 0, a contradiction.
As a consequence, for D > 0, it is impossible to have limt→+∞ai(t) = 0, and thus none of the com-
partments can become empty asymptotically. □
8


## Page 9


4
Tools from Markov Chain theory
We will use notions from Markov chain theory, and hence consider generators Q :
Λ x Λ −→R,
Q = {qij, i, j ∈Λ}, such that
qij ≥0,
for i ̸= j and qii = −
X
j̸=i
qij.
For example, the auxin ﬂux described by (2) contains implicitly a generator Q(D, T, a) given by





qij(D, T, a) = D + Tqij(a),
i ∼j,
qij(D, T, a) = 0,
i ≁j, i ̸= j.
qii(D, T, a) = −P
j̸=i qij(D, T, a),
(7)
where we set
qij(a) =
aj
κ + P
k∼i ak
.
Q is irreducible when for any pair of nodes (i, j), there is a path i0 = i →i1 →i2 →· · · →ik = j such
that qinin+1 > 0, n = 0, · · · , k −1. When Q is irreducible, one can prove that there is a unique invariant
probability measure π satisfying π∗Q = 0.
An irreducible transition kernel Q of invariant probability measure π is said to be reversible when
πiqij ≡πjqji, ∀i ̸= j.
5
Characterization of the critical points
We can write (2) in the more compact form
dai
dt = fi(a) =
X
j∼i
(ajqji(D, T, a) −aiqij(D, T, a)),
da
dt = f(a) = a∗Q(D, T, a).
Our ﬁrst aim is to look for the critical points of the above dynamical system, that is, to ﬁnd the element
a ∈RL solving the equations f(a) = 0, which can be rewritten as a∗Q(D, T, a) = 0. Hence, any solution
to f(a) = 0 is an invariant measure associated with the transition function Q(D, T, a). We will use the
following facts:
• When D > 0, the generator Q(D, T, a) is irreducible.
• For pure transport processes where D = 0 and T > 0, Q(0, T, a) is irreducible if and only if ai > 0
∀i.
In the irreducible case, let π(a) denote the associated positive invariant probability measure. We thus
look for a > 0 such that
a
P
i∈Λ ai
= π(a).
(8)
5.1
The irreducible case
Pure transport processes
If Q(0, T, a) is reversible, the equation f(a) = 0 is equivalent to the set of equations
aiqij(0, T, a) ≡ajqji(0, T, a),
i ̸= j.
(9)
9


## Page 10


In what follows, we will use the functions
Nk = Nk(a) = κ +
X
j∼k
aj.
(10)
Lemma 5.1 Let G be a connected graph. Assume that D = 0 and T > 0. Then Q(0, T, a) is reversible
∀a > 0, of invariant probability measure given by
π(a) =
 aiNi
Z(a)

i∈Λ,
(11)
where
Z(a) =
X
i∈Λ
aiNi = κ
X
i∈Λ
ai +
X
i∈Λ
X
j∼i
aiaj.
In this case, a > 0 is a critical point with f(a) = 0 if and only if Ni(a) does not depend on i, with
Ni(a) ≡
Z(a)
P
i∈Λ ai
= κ +
P
i∈Λ
P
j∼i aiaj
P
i∈Λ ai
.
(12)
Remark 5.2 The transition rates qij(a) are similar to the rates associated with a family of Markov chains
used in the study of vertex-reinforced random walks, see Benaïm, (1997); Benaïm and Tarrès, (2008) and
Pemantle, (1992), and Lemma 5.1 is an adaptation of these results. Interestingly, such vertex-reinforced
random walks are approximated by deterministic dynamical systems called replicator dynamics, of the
form
dai
dt = ai(N ′
i(a) −H′(a)),
where N ′
i(a) = Ni(a) −κ and H′(a) = P
i∈Λ aiN ′
i. In this setting, the function H′ plays the role of a
Lyapunov function. We will also ﬁnd a similar Lyapunov function, see Section 6.
Proof :
Assume, without loss of generality, that T = 1. First notice that
X
j∼i
π(a)jqji(0, T, a)
=
X
j∼i
ajNj
Z(a)
ai
Nj
=
1
Z(a)
X
j∼i
aiaj =
ai
Z(a)
X
j∼i
aj = ai(Ni −κ)
Z(a)
.
The identity
π(a)iqii(0, T, a) = −aiNi
Z(a)
X
j∼i
aj
Ni
= −ai(Ni −κ)
Z(a)
,
shows that
X
j∼i
π(a)jqji(0, T, a) + π(a)iqii(0, T, a) = 0,
so that π(a) is a invariant probability measure for Q(0, T, a). a > 0 is a critical point with f(a) = 0 if
and only if
a
P
i∈Λ ai is an invariant measure for Q(0, T, a). Because of the unicity of the invariant measure,
we obtain
Ni(a) ≡
Z(a)
P
i∈Λ ai
.
□
Let Γ be the adjacency matrix of the graph G = (Λ, E), that is, the matrix with entries given by Γij = 1,
when i ̸= j and i ∼j, and Γij = 0 otherwise. We summarize the above results in the following
10


## Page 11


Corollary 5.3 (Pure Transport Processes) Assume that D = 0 and T > 0 (no diﬀusion), and con-
sider only positive a > 0. Then,
f(a) = 0 if and only if Γa = c(a)1, 1 = (1, · · · , 1)∗,
(13)
where
c(a) =
P
i∈Λ
P
j∼i aiaj
P
i∈Λ ai
= ⟨a, Γa⟩
⟨a, 1⟩.
(14)
Remark 5.4 Let c be a constant, and let a (if it exists) be such that Γa = c1 and a ≥0. Then a is a
critical point and c is given by (14).
Example 5.5 (The one-dimensional cycle) Assume that the L cells are arranged on a cycle. The
pure transport process (D = 0) is reversible, so that the critical points a > 0 of dynamical system (2)
are solutions of linear system (13). We illustrate some results given in Section 7.4. When L > 4 is a
multiple of 4, the set of critical points a ∈RL forms a two dimensional sub-manifold Mc of RL given by,
when ρ = 1/L,
Mc = {(a1, a2, −a1 + 2ρ, −a2 + 2ρ, a1, a2, −a1 + 2ρ, −a2 + 2ρ, · · · ); ak ∈(0, 2ρ), k = 1, 2}.
When L > 4 is not a multiple of 4, Mc is reduced to the uniform conﬁguration Mc = {(ρ, ρ, · · · , ρ)}. We
will see that the uniform conﬁguration is always unstable, and that the other critical points are unstable
when a > 0. However, the boundary points are all stable.
General transport processes
Lemma 5.6 Assume that G is connected, and that both D and T are positive. For a > 0, f(a) = 0 if
and only if there exists a constant c such that a solves the following system of quadratic equations:
(ai −D
T )Ni(a) + ai = c aiNi(a), i = 1, · · · , Λ.
(15)
Proof :
Let µi = (ai −D/T)Ni, i = 1, · · · , Λ. Then µ = (µi)1≤i≤Λ behave
(µQ(0, T, a))i
=
X
j∼i
µjqji(a) + µiqii(a)
=
T
X
j∼i
(aj −D
T )Nj
ai
Nj
−T(ai −D
T )Ni
X
j∼i
aj
Ni
=
T
X
j∼i
(aj −D
T )ai −T(ai −D
T )
X
j∼i
aj
=
T D
T
X
j∼i
(aj −ai),
which gives the diﬀusion term contained in f. Hence, one can rewrite the equation f(a) = 0 as
(µ + a)Q(0, T, a) = 0.
By assumption, a > 0 so that Q(0, T, a) is irreducible as a Markov generator, and hence has only one
invariant probability measure. The linear space composed of invariant measures is one-dimensional, so
that the measure µ + a is proportional to π(a). The result is a consequence of expression for π(a) given
in (11). □
The next paragraph generalizes the diﬀusive part to model the eﬀect of potentials on the auxin ﬂux.
11


## Page 12


Inclusion of potentials
As stated in the Introduction, experiments have shown that both mechanical and biochemical processes
play a role in plant patterning. We here adapt some ideas of Newell et al., (2008) and Newell and Shipman,
(2005) to our discrete setting. The former considered the discrete model (2) by taking a continuous limit,
resulting in a p.d.e. describing the time evolution of auxin concentrations, which is coupled to the von
Karman equations from elasticity theory. These equations describe the deformations of an elastic shell or
plate subject to various loading conditions. Usually, the in-plane stress is described using Airy functions
which are potential for the stress ﬁeld. Here, we will simply suppose that this potential is given by some
function (φi)1≤i≤L. We also suppose that the auxin ﬂux is directed in part by these potentials and assume
a model of the form
dai(t)
dt
= fi(a) +
X
j∼i
(ajφi −aiφj),
(16)
i = 1, . . . , L. We will see in the sequel that the critical points associated to (2) exhibit regular geometrical
patterns locally, but not necessarily globally. The potential might be deﬁned in such a way to reproduce
the patterns obtained when considering mechanical buckling, and the model deﬁned by (16) might then
lead to more regularly spaced auxin peaks, see Figure 4.
Lemma 5.7 Assume a model of the form (16), with D > 0 and T > 0. Let a > 0. Then fi(a) +
P
j∼i(ajφi −aiφj) = 0 if and only if there exists a constant c ∈R such that
(ai −D
T −1
T φi)Ni(a) + ai = c aiNi(a), i = 1, · · · , Λ.
The proof of Lemma 5.7 is identical to the proof of Lemma 5.6.
5.2
The reducible case
We can adapt the previous notions to the case D = 0 and reducible transition kernel Q(0, T, a), that is
when some ai vanish. In this case, there is a pair of nodes i and j such that
m
Y
k=1
qik−1ik(a) = 0,
for all paths γ : i0 = i →i1 →· · · →im = j taking i to j in the graph G = (Λ, E).
Example 5.5 shows that the critical points associated with (2) on a circle form a manifold when L is a
multiple of 4. We also assert that the boundary points obtained from Mc by setting a1 = 0 are stable.
We will thus consider subsets I ⊂{1, · · · , L} corresponding to the sites i where ai = 0. We will denote
by a|I the restriction of any a to I. The same notations apply for generators and adjacency matrices,
where one conserves only the transitions rates qij(a) such that i, j ∈Λ \ I. According to Lemma 5.1,
these sub-transition kernels are reversible for a such that a|Λ\I > 0. If one removes the nodes i ∈I, the
graphs decomposes as a product of connected components γ, which form the sub-graph of G induced by
the nodes of J = Λ \ I. The special form of the vector ﬁeld associated with (2) ensures however that
the set of critical values such that a|I = 0, I ⊂{1, · · · , L}, can be obtained by considering a family of
transitions functions Qγ(0, T, a|γ). For each component γ, Corollary 5.3 shows that the related critical
points are obtained by solving linear systems of the form
Γγa|γ = cγ1|γ,
(17)
where Γγ is the adjacency matrix of the sub-graph γ, and the cγ are normalization constants chosen in
such a way that P
i ai = ρL. The set of critical points is then obtained by taking the direct product of
the sets of critical values associated with the sub-graphs γ.
12


## Page 13


6
Asymptotic properties of the auxin ﬂux for pure transport pro-
cesses
We consider the convergence of the dynamical system (2) when D = 0 using the method of Lyapunov
functions. Suppose without loss of generality that T = 1. We look for a function H(a) such that
dH(a(t))
dt
= ⟨∇H(a(t)), da(t)
dt
⟩≤0, ∀t ≥0.
If furthermore this function is bounded, then H(a(t)) converges, and we can in this way get useful
information concerning the convergence (e.g. toward the set of critical points) of a(t) solution of (2).
Lemma 6.1 Assume that D = 0 and set T = 1. Let
H(a) = −1
2
X
k∈Λ
ak(Nk(a) + κ) = −κ
X
k∈Λ
ak −1
2
X
k
X
j∼k
ajak,
(18)
where the functions Nk(a) have been deﬁned in (10). Let a(t) be a solution of the o.d.e. (2) such that
ai(0) ≥0. Then
dH(a(t))
dt
= −1
2
X
k∈Λ
X
j∼k
qkjqjk(Nk −Nj)2 ≤0, ∀t ≥0.
(19)
Notice that
∂H
∂ak
(a) = −Nk(a).
since the function Nk = Nk(a) = κ + P
j∼k aj does not depend on the variable ak.
Proof :
One can write
dH(a(t))
dt
=
−
X
k∈Λ
Nk
X
j∼k
(aj
ak
Nj
−ak
aj
Nk
) = −
X
k∈Λ
Nk
X
j∼k
aj
Nk
ak
Nj
(Nk −Nj)
=
−
X
k∈Λ
Nk
X
j∼k
qkjqjk(Nk −Nj)
=
−1
2
X
k∈Λ
X
j∼k
qkjqjk

Nk(Nk −Nj) + Nj(Nj −Nk)

=
−1
2
X
k∈Λ
X
j∼k
qkjqjk(Nk −Nj)2.
By Proposition 3.1, ai(0) ≥0, ∀i, implies that ai(t) ≥0, ∀i, ∀t > 0, so that qkj ≥0 and qjk ≥0, ∀k ∼j,
and ∀t > 0, proving the assertion. □
To prove the convergence of the auxin ﬂux, we use a Theorem of Lyapunov- LaSalle (see LaSalle, (1976)).
Introduce the notation
˙H(x) =
L
X
i=1
∂H
∂xi
fi(x) = −1
2
X
k∈Λ
X
j∼k
qkjqjk(Nk −Nj)2.
Consider the sets
Ω= {x ∈[0, 2ρ]L |
X
i
xi = ρL} and EΩ= {x ∈Ω|
˙H(x) = 0}.
13


## Page 14


Lemma 6.2 The set EΩis the set of critical points.
Proof :
Let x ∈Ω. Then ˙H(x) = 0 if and only if for all pairs j ∼k, either xj = 0, xk = 0 or Nj = Nk. Let
Ix := {i ∈Λ; xi = 0}. Then ˙H(x) = 0 if and only if, for all pairs of neighbours j ∼k such that j ∈Λ\Ix
and k ∈Λ \ Ix, one has that Nj = Nk. Let γ be the connected component of the graph containing
this pair (see Section 5.2), with Nj = Nk = cγ, for some positive constant cγ. Then, Ni ≡cγ, ∀i ∈γ.
One then gets that ˙H(x) = 0 if and only if the function N is constant on the connected components
γ associated with Ix. Hence, for each such component, one has that Γγx|γ = cγ1|γ. The results is a
consequence of Corollary 5.3 and of the results of Section 5.2. □
Let MΩbe the largest invariant subset of EΩ. As EΩcontains only the critical points of f, EΩis invariant.
Hence, MΩ= EΩ.
Proposition 6.3 Let a(t) be the unique solution of the o.d.e. (2) with a(0) ∈Ω. Then a(t) ∈Ω, ∀t > 0
and a(t) converges to MΩas t →∞.
Proof :
Proposition 3.1 shows that the compact set Ωis invariant. The continuously diﬀerentiable function H is
such that ˙H(x) ≤0, ∀x ∈Ω. The results then follows from a result of LaSalle, (1976). □
Corollary 6.4 Every limit point of a trajectory a(t) is a critical point i.e. if for tn ↗∞, a(tn) →a∞
then a∞∈MΩ.
Proof :
If a∞̸∈Ω, as EΩ= MΩis a closed set then d() > 0. It’s a contradiction with the proposition 6.3. □
Remark 6.5 (Global minimizers of H) The literature contains results on the set µ(G) of minimizers
of H when P
i∈Λ ai = 1. The authors of (Motzkin and Straus, 1965) proved that maxa⟨a, Γa⟩= (ω(G) −
1)/ω(G), where ω(G) is the clique number of G, that is the order of the largest complete sub-graph of
G. Moreover, they obtained that the absolute minimum of H is achieved at an interior point of the unit
simplex if and only if G is a complete multipartite graph. Various results were then obtained in (Waller,
1977). where for example it is proved that µ(G) is a simplicial complex, having an automorphism group
similar to that of G. In some sense, µ(G) mirrors some of the geometry of the graph G.
Proposition 6.6 If D = 0, then system (6) does not admit non-constant periodic solutions.
Proof :
Every point of a periodic solution is a limit point and, according to our preceding results (corollary 6.4),
it is a critical point. Unicity of a solution provides a contradiction. □
Proposition 6.7 If D = 0, then the set of critical points of system (6) is non-countable.
Proof :
Let PL
k=1 ak(0) = C > 0. We know that the corresponding solution has to remain in the hyperplane
(Π) : PL
k=1 xk = C. Since the path is bounded it admits at least one limit point and, according to our
preceding results (corollary 6.4), the latter is a critical point belonging to (Π). Consequently, for every
positive value of C, we obtain distinct critical points. □
14


## Page 15


7
Stability of pure transport processes
7.1
The irreducible case
We consider pure transport processes (i.e. D = 0) on general graphs. We ﬁrst discuss the stability of the
special class of critical points a > 0 solving equations of the form Γa = c1. Without loss of generality,
we set T = 1. For such a, Ni(a) ≡N = κ + c, and therefore, when the graph is regular, one obtains for
example the uniform solution a = (ρ) = (ρ, . . . , ρ). When G is the complete graph KL of L nodes, where
every pair of nodes i ̸= j are nearest neighbours, a simple computation shows that the Jacobian df((ρ))
associated with (2) and evaluated at the uniform conﬁguration (ρ), is given by
∂fi((ρ))
∂aj
= ρ2
N 2 , ∂fi((ρ))
∂ai
= −
X
j̸=i
ρ2
N 2 .
Consequently, df((ρ)) is a symmetric generator, and thus admits only non-positive real eigenvalues. The
uniform conﬁguration is then stable for the complete graph.
Proposition 7.1 Let a > 0 be such that Γa = c1, for some positive constant c > 0. According to Lemma
5.3, a is a critical point, with Ni(a) ≡N = c + κ. Assume that D = 0 and set T = 1. The Jacobian
df(a) = (∂fi/∂aj) evaluated at a is then given by
df(a) =
1
N 2 d(a)Γ

c id −d(a)Γ

,
where d(a) is the diagonal matrix of diagonal given by a, and where Γ is the adjacency of the graph.
The proof of Proposition 7.1 is given in Section 8.
We now characterize the set of stable conﬁgurations using the spectral gap of the matrix P(a) = Γd(a)/c.
Let P be a stochastic matrix associated with a Markov chain on the state space Λ. We assume that P
is reversible with invariant probability measure π. Let A be the matrix deﬁned by Aij = πipij ≡πjpji,
i ̸= j. The eigenvalues of P are real, given by −1 ≤βL ≤· · · β2 < β1 = 1, and the spectral gap is
given by C = 1 −β2. Let L = id −P be the associated Laplace operator, of eigenvalues λk = 1 −βk,
k = 1, · · · , L. Then (see e.g. (Diaconis and Stroock, 1991))
C = λ2 = inf{Eπ(φ, φ)
Varπ(φ) : φ is nonconstant},
(20)
where
Eπ(φ, φ) = 1
2
X
i,j
(φ(j) −φ(i))2Aij,
is the Dirichlet form associated with L, and where Varπ(φ) is the variance of the random variable φ with
respect to the invariant probability measure π. One can check that
Varπ(φ) = 1
2
X
i,j
(φ(j) −φ(i))2πiπj.
We can also reformulate the above variational problem in a diﬀerent way: set ⟨φ⟩π = P
i∈Λ φ(i)πi. Then
C = inf{Eπ(φ, φ)
Varπ(φ) : ⟨φ⟩π = 0}.
(21)
15


## Page 16


Lemma 7.2 Let G be a connected graph of adjacency matrix Γ, and let a > 0 satisfy Γa = c 1 for some
c > 0. The matrix P(a) deﬁned by
P(a) = 1
c Γd(a),
(22)
is stochastic, irreducible, reversible, of invariant measure π′(a) given by π′(a)i = ai/(ρL), and with a
real spectrum −1 ≤βΛ ≤βΛ−1 ≤· · · ≤β2 < β1 = 1. Let C(a) be the spectral gap of P(a), deﬁned by
C(a) = 1 −β2. a is stable if and only if C(a) ≥1. Moreover, the spectral gap is given by
C(a) = δ inf
φ
P
i,j(φ(j) −φ(i))2γijπ′(a)iπ′(a)j
P
i,j(φ(j) −φ(i))2π′(a)iπ′(a)j
≤δ,
where δ = ρL/c > 1, and where the inﬁmum is taken over all nonconstant functions φ.
Proof :
The matrix is stochastic since by assumption Γa = c1.
Let π′(a) =

ai
ρL

i∈Λ. Then P(a) is reversible of invariant measure given by π′. Notice next that
Aij = π′(a)iP(a)ij = δγijπ′(a)iπ′(a)j,
where we recall that γij ∈{0, 1} is the (i, j) entry of the adjacency matrix Γ. Hence, using the variational
characterization of the spectral gap given in (20),
C ≤Eπ′(a)(φ, φ)
Varπ′(a)(φ) = δ
P
i,j(φ(j) −φ(i))2γijπ′(a)iπ′(a)j
P
i,j(φ(j) −φ(i))2π′(a)iπ′(a)j
≤δ,
when φ is non-constant. The conﬁguration a is stable if and only if the eigenvalues of the Jacobian
matrix df(a) given in the proposition 7.1 are all non-positive. The adjacency matrix Γ is symmetric, so
that (Γd(a))∗= d(a)Γ. It follows that the eigenvalues ˜βi of d(a)Γ are equal to cβi, i = 1, · · · , L. The
eigenvalues of N 2df(a) are given by ˜βi(c −˜βi) = βi(1 −βi)c. Hence, a is stable if and only if β2 < 0,
that is if and only if C ≥1. □
Corollary 7.3 Let G be a connected graph of adjacency matrix Γ, and let a > 0 satisfy Γa = c 1 for
some c > 0. For i ∈Λ, let Vi = {j ∈Λ; j ∼i} be the neighbourhood of i. Assume that there exist
elements i0, i1, i2 and i3 of Λ such that
i1 ∈Vi0, i2 ∈Vi1 \ Vi0 \ {i0}, i3 ∈Vi2 \ Vi0 \ {i0}.
(23)
Then a is unstable.
Example 7.4 When G is a sub-graph of a two-dimensional grid, a solution to the linear system Γa = c1
can possibly to be stable only when G belongs to the list given in Figure 2, which consists in the square,
the star, and all the various parts of the star.
Proof :
We use Lemma 7.2 to express the spectral gap of P(a) as
C(a)
=
δ
inf
⟨φ⟩π′(a)=0
P
i φ(i)2π′(a)i
P
j γij
aj
ρL −P
i,j γijφ(i)φ(j)π′(a)iπ′(a)j
P
i φ(i)2π′(a)i
=
δ
inf
⟨φ⟩π′(a)=0
P
i φ(i)2π′(a)i c
ρL −P
i,j γijφ(i)φ(j)π′(a)iπ′(a)j
P
i φ(i)2π′(a)i
=
δ
inf
⟨φ⟩π′(a)=0
P
i φ(i)2π′(a)iδ−1 −P
i,j γijφ(i)φ(j)π′(a)iπ′(a)j
P
i φ(i)2π′(a)i
16


## Page 17


We will prove that C(a) < 1 by choosing a test function φ satisfying ⟨φ⟩π′(a) = 0 for which
δ
P
i φ(i)2π′(a)iδ−1 −P
i,j γijφ(i)φ(j)π′(a)iπ′(a)j
P
i φ(i)2π′(a)i
< 1,
which is equivalent to require that
X
i,j
γijφ(i)φ(j)π′(a)iπ′(a)j > 0.
We set φ(j) = 0, ∀j ∈Vi0. For j ∈Λ \ Vi0 \ {i0}, we choose φ(j) to be arbitrary but positive. For j = i0,
we choose φ(i0) so that
ai0φ(i0) = −
X
j̸=i0
ajφ(j).
Consequently ⟨φ⟩π′(a) = 0 and P
i,j γijφ(i)φ(j)aiaj > 0. □
Corollary 7.3 provides a simple condition ensuring the non-stability of conﬁgurations a satisfying Γa = c1.
We next consider the reducible case where ai = 0 for i ∈I ⊂Λ. Set J = Λ \ I, and let {γ1, · · · , γP } be
the collection of sub-graphs of G induced by the nodes of J, of node set Jγp and of adjacency matrices
Γγp, p = 1, · · · , P. We again assume that Γγpa|γp = cγp1 for some cγp > 0.
7.2
The reducible case
We consider the stability of critical points a such that ai = 0, for i ∈I ⊂Λ with I ̸= ∅.
Proposition 7.5 Assume that D = 0 and set T = 1. Let a be a critical point of (2) such that ai = 0
for i ∈I. Let {γ1, · · · , γP } be the collection of sub-graphs of G obtained by deleting the nodes of I, of
adjacency matrices Γγp, p = 1, · · · , P. The critical points a are obtained by solving linear systems of the
form Γγpa|γp = cγp1|γp for some cγp > 0 (see Section 5.2). The spectrum of the Jacobian evaluated at a
is given by
spec(df(a)) =
P[
p=1
spec
 df|γp(a|γp)

∪
(X
k∼i
ak
Nk
−Ni −κ
Ni
, i ∈I
)
(24)
The proof of Proposition 7.5 is given in Section 8.
Proposition 7.5 shows that such conﬁgurations are stable when 1) each a|γp is stable and 2) when
P
k∼i ak/Nk(a) −(Ni(a) −κ)/Ni(a) < 0, i ∈I. Here, if k ∼i, i ∈I, k ∈Λ \ I, Nk(a) is given by
the constant κ + cγp when k ∈Jγp. To go further, we need the following
Deﬁnition 7.6 Let J ⊂Λ. The outer boundary of J, denoted by ∂J, is the subset of Λ given by
∂J = {j ∈Λ \ J; j ∼J}.
7.3
Example: the rectangular grid
We now illustrate the various stable patches we can form by using the building blocks, as given in Figures
2 and 3. It is easy to provide examples of unstable conﬁgurations when the outer boundary of some
component γ is such that
∂

∂Jγ

∩Jγ′ ̸= ∅, for some component γ′ ̸= γ,
(25)
as illustrated in Figure 5(a).
17


## Page 18


b
b
b
b
b
b
b
b
b
b
b
b
b
r
r
r
r
r
r
r
r
r
r
l
l
(a) Unstable conﬁguration
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
b
r
r
r
r
r
r
r
r
r
r
r
r
r
r
(b) Stable conﬁguration
Figure 5: (a) One can check in this example that (25) implies the non-stability of the conﬁguration for
well chosen parameters. Red dots indicates cells with ai ̸= 0. (b) One can check in this example that
(26) is satisﬁed, ensuring the stability of the conﬁguration.
Next, the reader can verify, using Proposition 7.5, that any patch composed of building blocks disposed
in such a way that
∂

∂Jp ∪Jp

∩

∪p′̸=p Jp′

= ∅, ∀p = 1, · · · , P,
(26)
is stable. Figure 5(b) exhibits a typical example of a stable conﬁguration in this setting.
7.4
Example: the pure transport process on the circle
We here assume that D = 0 and T = 1. Corollary 7.3 yields the instability of uniform solution (ρ) =
(ρ, . . . , ρ) when the length L of the cycle is larger than 4. The adjacency matrix of the circle is circulant,
with eigenvalues given by
µk = e2πi k
L + e2πi (L−1)k
L
= 2 cos

2π k
L

.
The determinant of Γ vanishes if and only if there exists j ∈{1, ..., L} such that µj = 0, that is if
cos

2π j
L

= 0 ⇔2π j
L = π
2 + kπ for k ∈N,
or equivalently if there is a k ∈N such that j = L
4 + k L
2 ∈N. Hence, the determinant of Γ vanishes if
and only if L is a multiple of 4. In this case, the set Mc of critical values a (that is satisfying Γa = c1)
such that ai > 0, ∀i ∈Λ, is such that
a3 = c −a1, a4 = c −a2, a5 = a1, a6 = a2, a7 = c −a1, ...
with a1 ̸= 0 ̸= a2. Recalling that we impose the following normalization PL
i=1 ai = ρL, we obtain
L
X
i=1
ai = ρL ⇔2cL
4 = ρL ⇔c = 2ρ.
The set of critical values Mc is then composed of conﬁgurations of the form
a = (a1, a2, 2ρ −a1, 2ρ −a2, a1, a2, 2ρ −a1, 2ρ −a2, ..., a1, a2, 2ρ −a1, 2ρ −a2)
with (a1, a2) ∈(0, 2ρ) × (0, 2ρ). Corollary 7.3 then implies that this set contains only unstable points
when L > 4. For L = 4, the critical point a = (a1, a2, 2ρ −a1, 2ρ −a2) is stable since the eigenvalues of
the Jacobian matrix are such that
λ1 = λ2 = λ3 = 0 and λ4 = −
2c
(κ + c)2
18


## Page 19


We can summarize these results in the following corollary:
Corollary 7.7 Assume that the nodes are arranged on a circle of size L. The set Mc of critical values
a > 0 such that f(a) = 0 contains only the uniform conﬁguration (ρ, ..., ρ) if L is not a multiple of 4. In
the case where L = 4n, for some n ∈N with n ≥1, Mc is given by
Mc = {(a1, a2, −a1 + 2ρ, −a2 + 2ρ, a1, a2, −a1 + 2ρ, −a2 + 2ρ, · · · ); ak ∈(0, 2ρ), k = 1, 2}.
Any element of Mc is unstable except for L = 4.
The set M tot
c
of all critical points is obtained by decomposing the circle into sub-graph γ such a|γ > 0
and by solving the system
Γγa|γ = cγ1|γ,
for these sub-graphs. We can prove that this system has positive solution a|γ if and only |I| < 4 (|I| :=
length of the path), because for |I| ≥4, we see that a4 = 0 (which is in contradiction with the hypothesis).
When |I| = 3, the critical points take the form a|γ = (z1, cγ, cγ −z1), with z1 ∈(0, cγ) and when |I| = 2,
a|γ = (cγ, cγ). In these two cases, the critical points are stable as the Lyapunov function H deﬁned in
(18) takes its minimal value H(a) = −(κ + ρL
4 )ρL. The global minimum of H is obtained by adapting
the result of Motzkin and Straus, (1965), see Remark 6.5. Finally, if |I| = 1, we have a|γ = (cγ); H is
maximal and hence a is unstable.
The set M tot
c
of critical points is then obtained by taking the direct product of the sets of critical values
associated with the paths γ. For example, if L is a multiple of 4, the subset of M tot
c
deﬁned by
˜
Mc = {(a1, a2, −a1 + 2ρ, −a2 + 2ρ, a1, a2, −a1 + 2ρ, −a2 + 2ρ, · · · ); a1 = 0, a2 ∈(0, 2ρ)},
is composed of critical values which are stable since
λ = 0 with multiplicity 3L
4 and λ =
−2c2
(κ + c)2 with multiplicity L
4
7.5
An explicit computation when D = 0 on the circle
As we have seen, when |I| = 3, the stable conﬁgurations are given by triplets of the form (z1, cγ, cγ −z1),
where z1 is such that z1 ∈(0, cγ), for some positive constant cγ > 0.
Consider a path composed of ﬁve cells i −1, i, i + 1, i + 2 and i + 3 such that ai−1 = ai+3 = 0, so that
the dynamical system (2) associated with these cells becomes
dai
dt
=
ai+1ai
κ + ai + ai+2
−
aiai+1
κ + ai+1
,
(27)
dai+2
dt
=
ai+1ai+2
κ + ai + ai+2
−ai+2ai+1
κ + ai+1
,
(28)
dai+1
dt
=
aiai+1
κ + ai+1
+ ai+2ai+1
κ + ai+1
−
ai+1ai
κ + ai + ai+2
−
ai+1ai+2
κ + ai + ai+2
.
(29)
Dividing (27) by (28) yields that
dai
dt
dai+2
dt
=
ai
ai+2
.
Thus there is a positive constant c > 0 such that
ai+2 = cai.
(30)
19


## Page 20


Plugging this identity in (29), one obtains
dai+1
dt
= (1 + c)aiai+1(
1
κ + ai+1
−
1
κ + ai + ai+2
),
and ﬁnally
dai+1
dt
dai
dt
= −(1 + c).
Hence there exists a constant d such that ai+1 = d −(1 + c)ai. Normalizing the total mass in such a way
that ai + ai+1 + ai+2 = 3ρ, one gets that 3ρ = d and
ai+1 = 3ρ −(1 + c)ai.
(31)
Plugging (30) and (31) in equation (27) yields the diﬀerential equation
dai
dt = ai(3ρ −(1 + c)ai)(3ρ −2(1 + c)ai)
(κ + ai(1 + c))(3ρ + κ −(1 + c)ai).
Setting u = (1 + c)ai, one gets the o.d.e.
du
dt = u(3ρ −u)(3ρ −2u)
(κ + u)(3ρ + κ −u).
Solving by partial fractions expansions, one obtains
3κρ + κ2
9ρ2
(ln(u) + ln(3ρ −u)) −9ρ2 + 4(κ2 + 3ρκ)
18ρ2
ln(3ρ −2u) = t + α,
for some constant α. Clearly one must have u < 3ρ/2.
Lemma 7.8 As t →∞, u(t) = (1 + c)ai(t) −→3ρ
2 .
Proof :
The preceding considerations show that we have to consider only initial conditions of the form 0 ≤u(0) ≤
3ρ. Clearly 0, 3ρ
2 and 3ρ are critical points of our equation.
We can easily ﬁnd a compact interval I whose interior contains J = [0, 3ρ] and so that f ′(u) is continuous
and thus bounded over I.
As a consequence f satisﬁes a Lipschitz-condition over I.
According to
the general theory, for any initial condition u(0) ∈J our equation admits a unique solution deﬁned
over a maximal interval Im. If u(0) = 0, then u ≡0 is the corresponding solution. If u(0) ∈]0, 3ρ
2 [, then
˙u(0) > 0. Due to unicity, the solution can not reach a critical point in a ﬁnite time and thus the boundary
of ]0, 3ρ
2 [. Moreover the solution is obviously bounded entailing Im = [0, +∞[. For the preceding reasons
the derivative of u(t) is never 0 and thus always positive since ˙u(0) > 0. Thus u(t) increases to 3ρ
2 as
t →+∞. The same reasoning shows that u(t) decreases to 3ρ
2 as t →+∞for u(0) ∈] 3ρ
2 , 3ρ[. Finally if
u(0) = 3ρ, then u ≡3ρ. □
Furthermore, (30) yields
c = ai+2(0)
ai(0) .
As (1 + c)ai = ai + ai+2 tends to cγ as time goes to inﬁnity, Lemma 7.8 yields that cγ = 3ρ/2, and
ai(t) −→
3ρ
2(1 + c) =
cγ
1 + c,
20


## Page 21


as t →∞. (30) and (31) show that
ai+1 = 3ρ −(1 + c)ai −→3ρ
2 = cγ and ai+2 = cai −→
c
1 + ccγ = cγ −
cγ
1 + c.
In summary, one obtains that an orbit deﬁned by initial conditions of the form
(ai−1(0), ai(0), ai+1(0), ai+2(0), ai+3(0)) with ai−1(0) = ai+3(0) = 0
converges to the critical point (z1, cγ, cγ −z1), with z1 =
cγ
1+c, cγ = 3ρ
2 and c = ai+2(0)
ai(0) . Finally, if the
system starts from a symmetric initial state ai(0) = ai+2(0), the constant c is egal to 1 and the system
tends to (0, 3ρ
4 , 3ρ
2 , 3ρ
4 , 0) as t →∞.
8
Appendix
8.1
Proof of Theorem 3.1
First, we easily check that the system ˙a = f(a) is conservative, i.e.
∀t ∈R≥0,
L
X
i
ai(t) =
L
X
i
ai(0).
In the following, we use the notation ˙a instead of da
dt . The latter is equivalent to
L
X
i
˙ai(t) =
L
X
i
fi(a) = 0.
In fact, one can write
X
i
˙ai(t)
=
D
X
i
X
k∼i
(ak −ai) + T
X
i
X
k∼i
akai
Ni −Nk
NkNi

=
D
X
i
(diai −diai) + 2T
X
k∼i
akai
NkNi
((Ni −Nk) −(Nk −Ni)) = 0,
where Nk = κ + P
j∼k ak, and where di is the degree of i (that is the number of neighbours of i).
Next, system (2) can be written as
˙ai = D
X
k∼i
ak + T
X
k∼i
 
ak
κ + P
j∼k aj
−
ak
κ + P
j∼i aj
−D
T
!
ai.
(32)
Let a a solution of (32) with a(0) ∈RL
≥0.
We say that the function f : R+ →R is instantaneously positive (i.p.) if there exists δ > 0 so that f
is strictly positive over (0, δ). If f(0) > 0 and f is continuous to the right at 0, then f is i.p.. It is also
clear that if f admits a strictly positive right-hand derivative at 0, then it is i.p..
Let U be the open set U = {x = (x1, x2, ..., xL) ∈RL; −κ
2L < xi}. Since the right-hand member of
(32) is continous over U, the general theory of o.d.e.’s provides the existence of a solution deﬁned over
a maximal interval 0 ∈J+ ⊂R+ for any initial condition a(0) ∈U. Moreover, the solution is unique
because the right-hand member of (32) locally lipschitzian. Set for convenience
hi(t)
=
D
X
k∼i
ak(t)
and
gi(t)
=
T
X
k∼i
 
ak(t)
κ + P
j∼k aj(t) −
ak(t)
κ + P
j∼i aj(t) −D
T
!
.
21


## Page 22


The variation of constants formula allows us to write , ∀t ∈J+,
ai(t) = ai(0)e
R t
0 gi(s)ds +
Z t
0
hi(u)e−
R t
u gi(v)dvdu.
(33)
Since ai(0) ≥0, the ﬁrst term in (33) is non-negative. Moreover if ak(t) is i.p. for some k ∼i, then
according to (33), the same property holds for ai(t). In particular, if ak(0) > 0 for some k ∼i, then by
continuity ak(t) is i.p. and thus also ai(t).
The case D > 0:
Clearly, if a(0) = 0, then the unique solution is identically 0. Otherwise, there exists 1 ≤i0 ≤L with
ai0(0) > 0 and ∀j ∼i0, aj(t) is i.p.. Since our graph is supposed to be connected, every i admits a
neighbor k ∼i with ak(t) i.p.. Hence, ai(t) is i.p. ∀i, 1 ≤i ≤L.
The preceding arguments show that for any initial condition a(0) ∈RL
≥0 ⊂U, all components of the
solution of (32) are i.p..
Let us suppose that one of them admits the value 0 in J+\{0}.
Since all
components are continuous and their number is ﬁnite, there exists a ﬁrst time t0 > 0 for which at least
one component ai0(t0) = 0 and all of them are strictly positive over (0, t0). According to (33), we have
ai0(t0) = 0 = ai(0)e
R t0
0
gi(s)ds +
Z t0
0
hi(u)e−
R t0
u
gi(v)dvdu.
Clearly hi(t) > 0 over J+\{0} and since the ﬁrst term is non-negative, we conclude to ai0(t0) > 0, a
contradiction. Therefore all ai(t) are strictly positive over J+\{0}.
The case D = 0:
If ai(0) = 0, the homogeneous equation for ai(t) admits only the zero solution, and we remove the
related ith component from (32). Otherwise ai(0) > 0 and, by continuity, ai(t) is i.p.. In that case
ai(t) = ai(0)e
R t
0 gi(s)ds > 0 over J+.
In both cases the solution of (32) have strictly positive components over J+.
We also proved that
∀t ∈J+ we have:
X
1≤i≤L
ai(t) =
X
1≤i≤L
ai(0).
As a consequence the solution of (32) is bounded and thus the unique solution of our problem is deﬁned
over J+ = [0, +∞).
8.2
Proof of Proposition 7.1
We ﬁrst give the Jacobian, for general a. We have
∂fi(a)
∂aj
= ai
Nj
−ai
Ni
+
X
k∼i
aiak
N 2
i
−
X
k∼i,k∼j
ak
ai
N 2
k
,
(34)
(where the last term is due to the triangles in the graph) when j ∼i, that is, i and j are nearest
neighbours. When i = j, one gets
∂fi(a)
∂ai
=
X
k∼i
ak
Nk
−ai
X
k∼i
ak
N 2
k
−
P
k∼i ak
Ni
.
(35)
The remaining non-vanishing partial derivatives correspond to nodes j located at distance 2 of i in the
graph, that is, to nodes j such that j ∼k for some k ∼i, j ̸= i but i ̸∼j. Then
∂fi(a)
∂aj
= −
X
j∼k, k∼i
aiak
N 2
k
.
(36)
22


## Page 23


When Ni = N, ∀i, these expressions simplify to
∂fi(a)
∂aj
=
X
k∼i
aiak
N 2
i
= N −κ
N 2
ai −ai
N 2
X
k∼i,k∼j
ak.
If j ∼i,
∂fi(a)
∂ai
= −N −κ
N 2
ai,
and
∂fi(a)
∂aj
= −
X
k∼i,k∼j
aiak
N 2
k
= −ai
N 2
X
k∼i,k∼j
ak,
if j ∼k for some k ∼i, j ̸= i but i ̸∼j.
Consider the sub-matrix L given by L = (∂fi(a)/∂aj)j∼i. Let d(a) be the diagonal matrix of diagonal
given by a. The perturbation associated with the triangles contained in the graph is represented by the
term −ai
N 2
P
k∼i,k∼j ak in ∂fi(a)
∂aj
for j ∼i, and the related matrix is given by

−ai
N 2
X
k∼i,k∼j
ak

γij
=
 
−ai
N 2
X
k
γikakγkj
!
γij
=

−1
N 2 (d(a)Γd(a)Γ −diag(d(a)Γd(a)Γ))ij

γij
=

−1
N 2 (d(a)Γd(a)Γ)ij + N −κ
N 2
d(a)ij

γij.
The matrix L is now given by
L = d(a)
N 2 (N −κ)(Γ −id) −1
N 2 (d(a)Γd(a)Γ −(N −κ)d(a)) ◦Γ,
where ◦represents the Hadamard product, i.e. the multiplication component by component.
Likewise, the perturbation of L by

∂fi(a)
∂aj

i∼k,k∼j,i̸∼j,i̸=j can be written as



−ai
N 2
X
k∼i,k∼j,
i̸∼j,i̸=j
ak



γij
=
 
−ai
N 2
X
k
γikakγkj
!
(1 −γij −idij)
=

−1
N 2 (d(a)Γd(a)Γ)ij + N −κ
N 2
d(a)ij

(1 −γij −idij).
The related Jacobian is thus given by L +

∂fi(a)
∂aj

i∼k,k∼j,i̸∼j,i̸=j, that is
df(a)
=
d(a)
N 2 (N −κ)(Γ −id) −1
N 2 (d(a)Γd(a)Γ −(N −κ)d(a)) ◦Γ
−1
N 2 (d(a)Γd(a)Γ −(N −κ)d(a)) ◦(1 −Γ −id)
=
d(a)
N 2 (N −κ)(Γ −id) −1
N 2 (d(a)Γd(a)Γ −(N −κ)d(a)) ◦(1 −id)
=
d(a)
N 2 (N −κ)(Γ −id) −1
N 2 (d(a)Γd(a)Γ −(N −κ)d(a)),
23


## Page 24


where 1 is the matrix composed only of ones. The last equality is a consequence of the fact that the
diagonal of d(a)Γd(a)Γ −(N −κ)d(a) vanishes. Hence,
df(a) = d(a)Γ
N 2 ((N −κ)id −d(a)Γ) = d(a)Γ
N 2 (c id −d(a)Γ),
proving the result.
8.3
Proof of Proposition 7.5
Set I = {i ∈Λ : ai = 0}, and consider the sub-graphs γp of G induced by the nodes of J = Λ \ I, with
γp = (Λp, Ep), 1 ≤p ≤P. The related critical points a are such that the restrictions a|γp satisfy the
linear systems Γγpa|γp = cγp1|γp. Set Nγp = cγp + κ.
(34) - (36) permit to compute the entries of the Jacobian matrix, by ﬁrst looking at the diagonal entries:
When i ∈Λp, one has
∂fi(a)
∂ai
= −ai
Nγp −κ
N 2γp
,
providing the diagonal entry of the Jacobian of f|γp(a|γp). When i ̸∈Λp, a similar computation yields
∂fi(a)
∂ai
=
X
k∼i
ak
Nk
−Ni −κ
Ni
.
We then compute the entries (i, j) for j ∼i:
∂fi(a)
∂aj
= ai
Nγp −κ
N 2γp
−
X
k∼i,k∼j
ak
ai
N 2
k
= ai
Nγp −κ
N 2γp
−
X
k∼i,k∼j,k∈Λp
akai
N 2γp
,
for i, j ∈Λp and 1 ≤p ≤P, which corresponds to the (i, j) entry of the Jacobian of f|γp(a|γp). Likewise,
∂fi(a)
∂aj
= ai
Nj
−ai
Nγp
+
X
k∼i
aiak
N 2γp
−
X
k∼i,k∼j,
k∈Λp
akai
N 2γp
= ai
Nj
−ai
κ
N 2γp
−ai
N 2γp
X
k∼i,k∼j,
k∈Λp
ak,
when i ∈Λp for some p and j ̸∈Λp. Finally,
∂fi(a)
∂aj
= 0,
when i, j ̸∈∪pΛp, or equivalently when both i and j belongs to I.
We next consider (i, j) entries where j is at a distance 2 of i in the graph G, that is when j is such that
j ∼k for some k ∼i, j ̸= i and j ̸∼i. One obtains that
∂fi(a)
∂aj
= −ai
X
j∼k,k∼i
ak
N 2γp
,
when i, j, k ∈Λp, which is the (i, j) entry of the Jacobian of f|γp(a|γp).
Likewise,
∂fi(a)
∂aj
= −ai
X
j∼k,k∼i
ak
N 2γp
,
when i, k ∈Λp, j ̸∈Λp (⇒j ∈I).
24


## Page 25


Next,
∂fi(a)
∂aj
= 0.
when i or k ̸∈Λp, ∀j ∈Λ.
Permuting conveniently the indices, the Jacobian df(a) can be written as
df(a) =
dn
0
∗
df γ

(37)
where dn is a diagonal matrix n × n with entries given by λi := P
k∼i
ak
Nk −Ni−κ
Ni , for i ∈I, and hence
df γ is a block diagonal matrix, each block being equal to the Jacobian of f restricted on each sub-graph
γp. The permutation allows us to group all indices i ∈I in the same block, and all indices related to
the sub-graphs γp are also arranged together. It follows that the eigenvalues of df(a) are given by the
diagonal entries (λi)i∈I, and by the eigenvalues of all Jacobian matrices.
Acknowledgements This work was supported by the University of Fribourg, and by the SystemsX
"Plant growth in changing environments" project funding.
Many thanks to D. Kierzkowski and C.
Kuhlemeier for providing us the picture given in Figure 1 and to Aleš Janka for its help in Matlab
programming. We are very grateful to Patrick Favre and Didier Reinhardt for giving us the opportunity
to learn parts of the actual knowledge on the role of the auxin ﬂux in plant patterning.
References
Adler I (1974) A Model of Contact Pressure in Phyllotaxis. J. Theor. Biol. 1:1–79.
Atela P, Golé C, Hotton C (2002)
A dynamical system for plant pattern formation.
J. Nonlin. Sci
12:641–676.
Barbier de Reuille P, Bohn-Courseau I, Ljung K, Morin H, Carraro N, Godin C, Traas J (2006) Computer
Simulations Reveal Properties of the Cell-cell Signaling Network At the Shoot Apex in Arabidopsis.
Proc. Natl. Acad. Sci. USA 103:1627–1632.
Bayer E, Smith R, Mandel T, Nakayama N, Sauer M, Prusinkiewicz P, Kuhlemeier C (2009) Integration of
Transport-based Models for Phyllotaxis and Midvein Formation. Genes and Development 23:373–384.
Benaïm M (1997) Vertex-reinforced Random Walks and a Conjecture of Pemantle. Ann. Prob. 25:361–
392.
Benaïm M and Tarrès P (2008)
Dynamics of Vertex-Reinforced Random Walks.
ArXiv e-prints
0809.2739v3.
Boudaoud A (2010) An Introduction to the Mechanics of Morphogenesis for Plant Biologists. Trends in
Plant Science 15:353–360.
Diaconis P, Stroock D (1991) Geometric Bounds for Eigenvalues of Markov Chains. Ann. Appl. Proba.
1:36–61.
Douady S, Couder Y (1996) Phyllotaxis As a Dynamical Self Organizing Process (Part I, II, III). J.
Theor. Biol. 178:255–312.
Dumais J (2007) Can mechanics control pattern in plants ? Current Opinion in Plant Biology 10:58–62.
Dumais J, Steele C (2000) New Evidence for the Role of Mechanical Forces in the Shoot Apex Meristem.
Journal of Plant Growth Regulation 19:7–18.
25


## Page 26


Ethier SN, Kurtz TG (1986)
Markov processes: characterization and convergence.
Wiley series in
probability and mathematical statistics.
Evans, M., Hanney, T. and Majumdar, S. (2006) Interaction-Driven Real-Space Condensation. Physical
Review Letters 97:010603.
Gabriel JP, Hanisch H, Hirsch W (1988-1989)
Prepatency and sexuality of parasitic worms :
the
hermaphroditic case. Atti del colloquio di matematica, Edizione Cerﬁm Locarno, Anno 3, vol 4.
Green P (1980) Organogenesis- a Biophysical View. Annual Review of Plant Physiology 31:51–82.
Grosskinsky S, Redig F, Vafayi K (2011) Condensation in the Inclusion Process and Related Models. J.
Stat. Phys. 142:952–974.
Hamant O, Heisler MG, Jönsson H, Krupinski P, Uytterwaal M, Bokov P, Corson F, Sahlin P, Boudaoud
A, Meyerowitz E, Couder Y, Traas J (2008)
Developmental Patterning by Mechanical Signals in
Arabidopsis. Science 322:1650–1655.
Hamant O, Traas J (2009) The Mechanics Behind Plant Development. New Phytologist 185:369–385.
Heisler MG, Jönsson H (2006) Modeling Auxin Transport and Plant Development. J. Plant Growth
Regul. 25:302–312.
Hofmeister W (1868) Handbuch der Physiologischen Botanik: Allgemeine Morphologie der Gewächse,
405–664. Engelmann, Leipzig.
Jönsson H, Heisler MG, Shapiro BE, Mjolsness E, Meyerowitz EM (2006) An Auxin-driven Polarized
Transport Model for Phyllotaxis. Proc. Natl. Acad. Sci. USA , 103:1633–1638.
Kipnis C, Landim C (1999) Scaling limits of interacting particle systems, vol. 320, of Grundlehren der
Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences]. Springer-Verlag,
Berlin.
Kunz M (1995) Some Analytical Results About Two Physical Models of Phyllotaxis. Commun. Math.
Phys. 169:261–295.
LaSalle JP (1976) The stability of dynamical systems. SIAM, Philadelphia.
Levitov LS (1991) Energetics Approach to Phyllotaxis. Europhys. Lett. 14:533–539.
Luck JM, Godrèche C (2007) Structure of the stationary state of the asymmetric target process. J. Stat.
Mech. Theory Exp. P08005 (electronic).
Meinhardt H (1982) Models of Biological Pattern Formation. Academic Press.
Mjolsness E (2006) The Growth and Development of some Recent Plant Models: a Viewpoint. J. Plant
Growth Regul. 25:270–277
Motzkin T, Straus G (1965) Maxima for Graphs a New Proof of a Theorem of Turán. Canad. J. Math.
17:533–540.
Newell A, Shipman P (2005) Plant and Fibonacci. J. Stat. Phys. 121:937–968.
Newell AC, Shipman PD, Sun Z (2008) Phyllotaxis: Cooperation and Competition Between Mechanical
and Biochemical Processes. Journal of Theor. Biol. 251:421–439.
Pemantle R (1992) Vertex-reinforced random walk. Probab. Theory Related Fields 92:117–136.
Reinhardt D, Mandel T, Kuhlemeier C (2000) Auxin Regulates the Initiation and Radial Position of
Lateral Organs. Plant Cell 12:501–518.
26


## Page 27


Reinhardt D, Pesce E, Stieger P, Mandel T, Baltensperger K, Bennett M, Traas J, Friml J, Kuhlemeier
C (2003) Regulation of Phyllotaxis by Polar Auxin Transport. Nature 426:255–260.
Reinhardt D (2005) Phyllotaxis - a new chapter in an old tale about beauty and magic numbers. Current
Opinion in Plant Biology 8:487–493.
Sahlin P, Söderberg B, Jönsson H (2009) Regulated transport as a mechanism for pattern generation :
Capabilities for phyllotaxis and beyond. Journal of Theoretical Biology 258:60–70.
Scarpella E, Marcos D, Friml J, Berleth T (2006) Control of Leaf Vascular Patterning by Polar Auxin
Transport. Genes Dev. 20:1015–1017.
Shipman PD, Newell AC (2005) Polygonal Plantform and Phyllotaxis on Plants. Journal of Theor. Biol.
236:154–197.
Smith RS, Guyomarch’s S, Mandel T, Reinhardt D, Kuhlemeier C et al. (2006) A Plausible Model of
Phyllotaxis. Proc. Natl. Acad. Sci. USA 103:1301–1306.
Thornley J (1975) Phyllotaxis I. A mechanistic model. Annals of Botany 39:491–507.
Turing A (1952) The Chemical Basis of Morphogenesis. Philo. Trans. Roy. Soc. London 237:37–72.
Waller D (1977) Optimisation of Quadratic Forms Associated with Graphs. Glasgow Math. J. 18:79–85.
27

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
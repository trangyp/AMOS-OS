---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1610.04844v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1610.04844v1_Complete_coverage_of_space_favors_modularity_of_the_grid_system_in_the_brain

> Source: 1610.04844v1_Complete_coverage_of_space_favors_modularity_of_the_grid_system_in_the_brain.pdf

> Pages: 10

---


## Page 1


Complete coverage of space favors modularity
of the grid system in the brain
A. Sanzeni,1, 2 V. Balasubramanian,3 G. Tiana,4 and M. Vergassola2
1Department of Physics, University of Milan and INFN, Via Celoria 13, 20133 Milano, Italy
2Department of Physics, University of California San Diego, La Jolla, CA 92093-0374, USA
3David Rittenhouse Laboratory, University of Pennsylvania, Philadelphia, PA 19104, USA
4Centre for Complexity & Biosystems and Department of Physics,
University of Milan and INFN, University of Milan, via Celoria 16, 20133 Milano, Italy
Grid cells in the entorhinal cortex ﬁre when animals that are exploring a certain region of space
occupy the vertices of a triangular grid that spans the environment.
Diﬀerent neurons feature
triangular grids that diﬀer in their properties of periodicity, orientation and ellipticity.
Taken
together, these grids allow the animal to maintain an internal, mental representation of physical
space.
Experiments show that grid cells are modular, i.e.
there are groups of neurons which
have grids with similar periodicity, orientation and ellipticity. We use statistical physics methods
to derive a relation between variability of the properties of the grids within a module and the
range of space that can be covered completely (i.e. without gaps) by the grid system with high
probability. Larger variability shrinks the range of representation, providing a functional rationale
for the experimentally observed co-modularity of grid cell periodicity, orientation and ellipticity.
We obtain a scaling relation between the number of neurons and the period of a module, given
the variability and coverage range. Speciﬁcally, we predict how many more neurons are required at
smaller grid scales than at larger ones.
I.
INTRODUCTION
Classical behavioral experiments show that the navi-
gation of mammals relies on an internal representation
of space called a “cognitive map” [1]. Research on the
neural basis of this internal representation started with
the discovery of place cells in the hippocampus of rats,
neurons that have their activity controlled by the phys-
ical position occupied by the animal [2]. The discovery
of place cells generated an extensive investigation of the
spatial representation system in the brain, which led to
the discovery of grid cells [3], as well as diﬀerent types
of neurons whose activity codes for head direction [4],
speed [5], and borders of the environment [6, 7] (see [8]
for a recent review). The discovery of cells that consti-
tute a positioning system in the brain was the motivation
for the Nobel Prize in Physiology awarded in 2014.
One of the most striking elements composing the cog-
nitive map is in the entorhinal cortex (EC) [3], where
grid cells respond when the animal occupies one of the
vertices of a triangular grid that tessellates space.
It
is widely believed that these neurons provide a metric
for the spatial representation system, since their relation
with physical position does not reshuﬄe in diﬀerent en-
vironments, unlike what happens for place cells where
“remapping”’ occurs [9].
Grid cells are organized in modules – grids in a mod-
ule are clustered around a discrete period which increases
along the dorso-ventral axis of the EC [10, 11]. Grids in
a module also share similar orientations and ellipticities
while varying in spatial phase [11]. Experimentally, there
is a power-law relation between the periodicities of dif-
ferent modules – a rationale for the power law was given
in [12, 13].
The term “module” for grid cells diﬀers fundamentally
from the same term used in the context of brain (or city)
networks [14]. There, neurons correspond to the nodes of
a network whose edges correspond to axonal connections
among the neurons. Modularity refers to the formation of
clusters of nodes that are more densely connected among
themselves than to nodes in other modules. The reason
for modularity in these networks is that edges have costs
that scale with their length, so that spatial aspects are
important and commonly lead to cluster formation. By
contrast, the triangular lattices in the EC grid system de-
scribe ﬁring patterns of individual grid cell neurons as an
animal explores the environment. In other words, there
is no physical edge between vertices of the triangular ﬁr-
ing lattices of grid cells, and no cost associated to their
length. Hence, physical proximity is not relevant for grid
cells and has no bearing on the problem of explaining the
modular organization of grid cells in the EC.
Why is the grid system modular? The key point un-
derlying our arguments in the sequel is that behavioral
deﬁcits in orientation and navigation result if the neural
representation has gaps, i.e. complete coverage of space is
a fundamental requirement for the cognitive map to func-
tion. Speciﬁcally, we use statistical physics methods to
show that variability in period, orientation or ellipticity
randomizes the relative phases of ﬁring ﬁelds, and leads
to failure of spatial coverage. Larger variability entails a
smaller physical range that can be covered without gaps
(which would lead to behavioral deﬁcits). Hence, opti-
mizing spatial coverage gives a functional argument for
reduced variability and for the observed co-modularity
of grid cells. We also predict a scaling law relating the
period and number of neurons in a module.
arXiv:1610.04844v1  [q-bio.NC]  16 Oct 2016


## Page 2


2
II.
RESULTS
A.
A model of grid cells’ activity
For our speciﬁc purpose of analyzing eﬃcient coverage
of space, the ﬁring ﬁeld of grid cells can be simpliﬁed as
follows. After thresholding for noise, the smooth lumps
formed by ﬁring ﬁelds are treated as being uniformly ac-
tive inside a localized region and inactive outside (Fig. 1).
Noise and ﬁring inhomogeneity inside the active region
only degrade the uniformity of coverage relative to this
model. Thus, treating ﬁring ﬁelds as step functions al-
lows us to derive bounds on how well a given grid archi-
tecture can cover space.
Speciﬁcally, we represent the activity of grid cells as
a(x) =
X
n,m∈Z
χ
|φ + R(θ) [nv + mu)] −x|
ℓ/2

,
(1)
where x is the vector locating the position of the an-
imal in two dimensions, v = λ1(cos(β), sin(β)) and
u = λ2(1, 0) are the elementary vectors that generate
the grid, ℓis the diameter of a ﬁring ﬁeld, and n and m
are integers indexing the vertices of the grid. R(θ) is an
overall rotation of the grid by an angle θ, the angle β
describes the relative rotation of the grid basis vector v
relative to u, and the phase φ represents a shift with re-
spect to a reference point. The activity of an equilateral,
unrotated triangular grid has λ1 = λ2 = λ, β = π/3 and
θ = 0. The set of the six vertices deﬁned by the triplet
u, v, u −v and their opposite vectors forms an hexagon
that can be inscribed into an ellipse. The ratio between
the axes of the ellipse deﬁnes the ellipticity ϵ of the grid
(ϵ = 1 for equilateral grids). Hereafter, we study isosceles
grids, where the relation cos β = 1/
√
1 + 3ϵ2 holds, but
our conclusions hold generally (see Appendix A). Finally,
for the purpose of analyzing coverage we take χ = 1 when
its argument is < 1 and χ = 0 otherwise, i.e. we are in-
terested in whether a neuron is active or not at a given
point (disregarding its strength of activity).
In a module, grid cells with similar spacing have similar
orientation, ellipticity and ﬁring ﬁeld size [11]. However,
parameters of the grids have an appreciable variability,
which we quantify using experimental data reported in
Stensola et al. [11] as follows.
For each animal where
the distribution of grid parameters is available, we ﬁt the
data with a sum of Gaussians. For each module, we used
one Gaussian for the period (mean λ, standard devia-
tion σλ) and one for the orientation (mean θ, standard
deviation σθ.) The two standard deviations are roughly
constant in the various modules.
Indeed, the Pearson
correlation coeﬃcient is 0.21 between σλ and λ and 0.28
between σθ and λ. The standard deviation of the grid pe-
riod is about 6 cm. Assuming 10 modules and that the
smallest is about 40cm, the ratio σλ/λ goes from 0.01
to 0.15. The standard deviation of the orientation in a
module is about 0.03 rad. In the literature we were not
able to ﬁnd the distribution of ellipticity in the popu-
lation within a single module. We know that ellipticity
also has a modular structure and that across a population
(all modules) the mean ellipticity is around 1.16 ± 0.003
[11]. In the following analysis we assume a standard de-
viation in ellipticity in the range 0.01-0.15, i.e. similar
to variability in grid spacing. Finally, we ﬁxed the ratio
between the ﬁring ﬁeld width and the grid spacing at the
experimental value λ/ℓ∼1.63 ± 0.04 [15].
θ
λ’ l’
c
λ
l
λ1
λ2
U1
U2
a
b
a
b
d
A
B
c
θ
FIG. 1. Deformations in grid parameters induce de-
phasing. (A) Spatial activity of a grid cell (a) and its pos-
sible deformations: dilation (b), rotation (c) and ellipticity
transformation (d). The activity after transformation (green)
is superimposed on the reference activity (gray). (B) Using
a set of grid parameters we divide space into unit cells repre-
sented by gray hexagons. A neuron with the same set of grid
parameters (a) has constant relative phase (black arrows) in
each unit cell. A neuron with diﬀerent grid parameters (b)
has variable phases in diﬀerent unit cells, e.g.
the grid is
rotated as in panel (A.c) and the center of the unit cell is
covered by a ﬁring ﬁeld in U1 but not in U2.
B.
Dephasing and decorrelation of neuronal
activity
In order to cover an environment with grid cells, there
must be at least one active neuron at each point. The
average orientation θ, ellipticity ϵ and period λ within
a module deﬁne a tessellation of the plane into periodic
unit cells. Perfect periodicity would imply that once a
unit cell is covered, all of space is covered.
However,
perfect periodicity is broken by the variability discussed
above, which results in deviations from the average grid.
Indeed, as shown in Fig. 1B, the pattern of ﬁring ﬁelds
changes across unit cells, a phenomenon that we call “de-
phasing”. Here we characterize this eﬀect by computing
the correlation coeﬃcient between the number of neurons
that are active at the center of two unit cells.
The number of neurons active at a spatial point x is
given by n(x) = PN
i=1 ai(x), where ai is the spatial ac-
tivity of the i−th neuron given by Eq. (1) and N is the
number of neurons in the system. Consider a set of neu-
rons whose grid parameters are drawn from Gaussian dis-
tributions with standard deviations σλ, σθ and σϵ. We


## Page 3


3
compute numerically the correlation (normalized to 1 for
coincident points) between the numbers of neurons n(x)
and n(y) active at diﬀerent points x and y, by averag-
ing over statistical realizations (Fig. 2). The correlation
declines systematically with the separation in the grid
lattice. The corresponding correlation length L (deﬁned
as the distance at which the correlation drops to 1/e)
decreases with the variance in the parameters of the grid
cells (Fig. 2) and is in the meter scale for the smallest
modules, which is within the behavioral range of a few
tens of meters found in rats [16–18].
We can understand the asymptotic behavior of the cor-
relation function of the number of neurons active at two
spatial points at large separations as follows.
We are
assuming that grid cells in a module ﬁre independently.
Therefore, the correlation function of the number of neu-
rons active at x and y, ρ(n(x), n(y)), is equal to the cor-
relation function of the activity of a single generic neuron
a(x), averaged over the distribution of grid parameters,
ρ(a(x), a(y)). The mean activity of a single neuron is
obtained from Eq. (1) by averaging over the grid param-
eters. This quantity can be written as
⟨a(x)⟩=
Z
a(x) dPθdPλdPϵdPφ ,
(2)
where dP(∗) represents the probability distribution for
the parameter (∗). As discussed above, orientation, pe-
riod and ellipticity of the grids follow a Gaussian distri-
bution whilst the spatial phase is uniformly distributed
in a unit cell. To compute the integral, we divide space
into unit cells and consider the center of the cell contain-
ing x as a reference point for the phase of the grid φ.
Because φ is uniformly distributed in the unit cell, and
because χ = 1 within the ﬁring ﬁeld and χ = 0 outside,
the integral over φ is a constant equal to the ratio be-
tween the area of a ﬁring ﬁeld and that of a unit cell,
i.e. π/2
√
3 (ℓ/λ)2. The remaining integrals are equal to
unity and we ﬁnally obtain ⟨a(x)⟩= π/2
√
3 (ℓ/λ)2.
In order to compute the correlation function we need to
determine the quantity ⟨a(y)a(x)⟩. which can be written
as
⟨a(y)a(x)⟩=
Z
Qφ(y, x)dPφ ;
Qφ(y, x) ≡
Z
a(y)a(x) dPθdPλdPϵ ,
(3)
where Qφ(y, x) is the joint probability distribution that
a neuron is active both at y and at x. The distribution
depends parametrically on φ. The joint probability can
be computed as
Qφ(y, x) = Qφ(y|x)Qφ(x) ,
(4)
where Qφ(y|x) is the conditional probability that a neu-
ron is active at y if it is active at x (for a given φ). The
quantity Qφ(x) is the probability that a neuron is active
at x, again for a given φ.
In
order
to
evaluate
the
conditional
probability
Qφ(y|x), we divide space into unit cells using the mean
grid parameters. We consider a neuron with φ = (0, 0),
i.e. with a ﬁring ﬁeld centered at the origin, and analyze
the evolution of its phase φn in the unit cells centered
at y = (nλ, 0), n = 0, 1, . . . . If the grid cell has the
same grid properties as the average grid, its phase will
be invariant, i.e. φn = φ, hence Qφ(y|x) = 1 and the
correlation function will be a constant that does not de-
pend y. If there is variability, the phase of the grid will
be randomly distributed in the two-dimensional area of
the unit cell centered at (nλ, 0) as n increases. It follows
that Qφ(y|x) →π/2
√
3 (ℓ/λ)2; ⟨a(y)a(x)⟩→⟨a(x)⟩2
and the correlation asymptotically goes to zero as shown
in Fig. 2.
In Appendix B we discuss the behavior of the correla-
tion function in the absence of orientation variance. This
analysis is not relevant to describe the biological sys-
tem, where orientation variance is estimated to be about
0.03 rad, but constrains the deﬁnition of the correlation
length. In particular, we show that the threshold used
to deﬁne the correlation length ought to be in the range
[0.28, 1], which includes our choice of a threshold equal
to 1/e.
C.
Coverage drives modularity
In order to cover an environment with a set of grid
cells, there has to be at least one active neuron at every
point. The correlation length L characterizes the scale
beyond which the numbers of active neurons become ap-
proximately independent. A region of size R is thereby
decomposed in R2/L2 regions whose coverage probabil-
ities are roughly independent of each other. If each of
these is covered with probability p, the probability P of
covering the whole environment is
log(P) = γ R2
L2 log(p) ,
(5)
where γ is a constant that depends on the geometry of
the system.
The probability p of covering a correlation volume of
linear size L as a function of the probability of covering
a unit cell puc, was obtained numerically as follows. We
computed the covering probability of a circular environ-
ment of radius R using sets of grid cells characterized
by diﬀerent puc. Results of the simulations are shown in
Fig. 3. For every value of the radius R the logarithm of
the covering probability rescaled over log(puc) does not
depend on puc (Fig. 3B). It follows that the probability
p of covering a correlation volume of linear size L can be
expressed as
log(p) = K log(puc) ,
(6)
where K is a function that depends only on L/λ for di-
mensional reasons.


## Page 4


4
2
5
10
20
σ θ = 0. 0 1
σ λ /λ
0
0.1
0.1
0
σ
σ θ
= 0. 0
σ λ /λ
0
0.1
0.1
0
σ θ
= 0. 0 1
0
0.1
0.1
0
σ
σ λ /λ
σ
0
10
20
10
−2
10
−1
10
0
x / λ
ρ ( n( x) , n( 0 ) )
0
10
20
x / λ
0
10
20
x / λ
A
B
σλ/ λ= 0.0 3,σ = 0
σλ/ λ= 0.0 2,σθ= 0.0 2
σ = 0,σθ= 0.0 2
C
=
σθ 0.0 2, 0.0 4, 0.0 6
=
σ
0.0, 0.0 7, 0. 1 5
= 0.0 2, 0.0 4, 0.1 2
σλ/ λ
D
E
F
FIG. 2. Variability of grid parameters induces decor-
relation in grid cells activity. The correlation coeﬃcient
of the number of neurons active at the center of two unit cells
along the line x = nλ(1, 0), n ∈{0, 1, . . . } for diﬀerent values
of the standard deviations in the parameters of the grid cells.
In the plots x = |x|. Colors in the ﬁrst row represent diﬀer-
ent values of one of the variances (orientation (A), ellipticity
(B), period (C)) while the other two are ﬁxed (σλ/λ = 0.03,
σϵ = 0(A), σλ/λ = 0.02, σθ = 0.02 (B), σθ = 0.02, σϵ = 0
(C)). The case with no noise is represented in black. Larger
variances lead to a rapid decrease in the correlation as a func-
tion of separation. (See Appendix B for details on panel C.)
The correlation length depends on three variances which we
varied in pairs obtaining contour plots (σθ = 0.01 (D), σϵ = 0
(E), σλ/λ = 0.01 (F)). The white points in panel (E) cor-
respond to the values of the standard deviations measured
in [11].
Over a range of grid variances that includes the ex-
perimentally measured values, we found that L/λ ≲20
(Fig. 2). In this range, we found numerically that
K (x) = c1 + c2 log(x)
(7)
(c1 = 0.73, c2 = 13) gives a good description of the data
(see Fig. 3C) .
Combining Eqs. (5), (6) and (7), we obtain :
log(P) = γ R2
L2 K
L
λ

log(puc) .
(8)
To test this estimate, we numerically analyzed the cover-
ing probability of a circular environment of radius R by
N neurons whose grid parameters are drawn from Gaus-
sian distributions. We then checked if every point in the
environment is covered by at least one grid cell and we
averaged over realizations. Fig. 4 conﬁrms the validity of
Eq. (8), with a proportionality constant γ = 0.804.
Fig. 4 and Eq. (8) show that the covering probability
of a region increases with the correlation length. In this
sense, a set of grid cells with a larger correlation length is
10
0
10
1
10
2
10
0
10
1
10
2
10
3
10
4
R/ λ
l o g ( P ) / l o g ( p   )
10
0
10
1
10
2
R/ λ
−l o g(P)
10
−6
10
−4
10
−2
10
0
- l o g(pu c)= 10
−6
- l o g(pu c)= 410
−5
- l o g(pu c)= 10
−3
5
10
15
10
20
30
40
L / λ
u c
K = l o g ( p ) / l o g ( p   )
u c
A
B
C
FIG. 3. Covering probability of a correlation volume
of linear size L. (A) Covering probability P of a circular en-
vironment of linear size R computed numerically for diﬀerent
environment size and covering probability of the unit cell puc.
The diﬀerent values of puc have been obtained using sets of
grid cells made of a diﬀerent number of neurons. (B) Results
of panel (A) collapse on a common curve when their loga-
rithm is rescaled by log(puc), justifying the functional form
introduced in Eq. 6. (C) Numerical covering probability p of
a correlation volume of linear size L have been used to obtain
an empirical description of the function K (L/λ) described in
Eq. 6 (red dots).
The best ﬁt (black line) is given by the
function K (x) = 0.73 + 13 log(x).
Simulations parameters
are λ/ℓ=1.63, σθ = 0.04, σϵ = 0. In panels (A-B) we ﬁxed
σλ/λ = 0.08 whilst the number of neurons N is 30 (magenta,
squares), 40 (light blue, circles), 50 (brown, stars). In panel
(C) we ﬁxed N = 30 and σλ/λ has been varied to span the
diﬀerent values of L observed in the biological system as de-
scribed in Fig 2E.
0
20
40
0
0.2
0.4
0.6
0.8
1
R/ λ
P
0
20
40
R/ λ
0
20
40
R/ λ
A
B
σλ/ λ= 0.0 3,σ = 0
σλ/ λ= 0.0 2,σθ= 0.0 2
σ = 0,σθ= 0.0 2
C
=
σθ 0.0 2, 0.0 4, 0.0 6
= 0.0, 0.0 7, 0. 1 5
= 0.0 2, 0.0 4, 0.1 2
σλ/ λ
σ
FIG. 4. The covering probability P decreases with the
variance of grid parameters and the size of the envi-
ronment. P is computed for circular environments of radius
R and for diﬀerent grid variances.
Colors represent diﬀer-
ent values of one of the variances (orientation (A), ellipticity
(B), period (C)) while the other two are ﬁxed (σλ/λ = 0.03,
σϵ = 0(A), σλ/λ = 0.02, σθ = 0.02 (B), σθ = 0.02, σϵ = 0
(C)). The case with no noise is in black. Numerical results
(colored symbols) match theoretical predictions (continuous
line) obtained by Eq. (8). The number of neurons N = 30.
more eﬃcient, because with the same number of neurons,
and hence a ﬁxed puc, it will have fewer gaps. Since the
correlation length decreases if the standard deviations
increase, we conclude that coverage drives modularity –
grid cells with similar period should have similar orien-
tations and ellipticities as observed experimentally [11].


## Page 5


5
D.
Gaps decline exponentially with the number of
neurons
We now quantify how the number of neurons N in a
module aﬀects the probability of covering a range R. The
dependence on N in Eq. (8) occurs through the factor
puc. The random distribution of phases of grid cells [3]
dictates an exponential dependence between the proba-
bility puc and the number of neurons N. Indeed, con-
sider N neurons that cover a unit cell of a d-dimensional
grid with a single gap. An additional neuron added with
a random phase will fail to overlap the gap with some
probability h < 1. If we add Q additional neurons inde-
pendently, the probability that they all miss the gap is
hQ, i.e. the probability of gap persistence declines expo-
nentially with the number of added neurons. Subleading
terms are captured by analyzing partial coverage with
each additional neuron (see Appendix C).
Thus,
for a large number of neurons in a two-
dimensional grid module, we expect that puc ∼1 −
exp (−αN), where α is a positive constant that depends,
by dimensional analysis, on the ratio ℓ/λ. In the oppo-
site limit, when N is smaller than the area of the unit cell
divided by the area of the ﬁring ﬁeld, coverage cannot be
achieved and puc = 0, as conﬁrmed numerically in Fig. 5.
In summary, the estimate for the probability P of cov-
ering a two dimensional circular region of radius R is
log(P) = γ R2
L2 K (L/λ) log(1 −eF(N)) ,
(9)
where the function F (N) behave as just discussed, which
is validated by numerical simulations (Figs. 4, 5). On
the one hand, the probability of gaps in coverage declines
exponentially with N. On the other hand, the probability
of gaps in coverage of a range R increases exponentially
as (R/L)2K (L/λ), where L decreases as the variability
in a module increases. Hereafter, we balance these two
eﬀects to estimate the number of neurons required to
cover space in modules of diﬀerent mean periods.
E.
Prediction: smaller period modules need more
neurons
Eq. (9) gives the relation between the number of neu-
rons Ni and the parameters of the i-th module. Since the
diﬀerent modules vary systematically in their period, this
relation predicts an associated variation in the number of
neurons.
Assume that an animal encodes position within a re-
gion of size R2 that is common to all the modules, and
that the probability of covering space is the same at all
scales. As we showed above, the probability of gaps in
coverage declines exponentially with the number of neu-
rons, and the coeﬃcient in the exponent depends on the
ratio ℓ/λ between the grid ﬁeld width and the period.
It is established experimentally that this ratio is ﬁxed
A
B
0
20
40
N
1 −P
unit cell
R/ λ = 2 0
10
0
10
1
10
2
R/ λ
−
l o g( P )
N=3 0
N=4 0
N=5 0
10
−6
10
−4
10
−2
10
0
10
10
0
−5
FIG. 5.
The covering probability P increases with the
number of neurons N. (A) The numerical computation of
P for a unit cell (black dots) is combined with Eq. (9) to
predict P for an environment of size R/λ = 20 (black line).
Results of numerical simulations are in green. The function
1 −P asymptotically decays as exp(−αN) with α ≈0.4 (red
line).
(B) The probability P vs.
the environment size R
for diﬀerent N. Results of the simulations (colored symbols)
match predictions (black lines) by Eq. (9). Parameters are
λ/ℓ=1.63, σθ = 0.04, σλ/λ = 0.08, σϵ = 0.
among modules [10, 11]. Thus we can evaluate the pre-
dicted fraction of neurons in a given module, Ni/ P
i Ni,
where the denominator is a sum over modules, and Ni is
obtained by inverting Eq. (9).
The results of this prediction and a comparison with
the extant experimental data are shown in Fig. 6. The
theoretical predictions are given for a variety of ranges
and coverage probabilities, with the grid periods and
variabilities ﬁxed from experimental data. Qualitatively,
the theory predicts for any choice of parameters that the
number of neurons should decline with the period of the
module, as also suggested by the data.
Responses from 4–5 modules spanning up to 50% of
the dorsoventral extent of mEC feature a smallest period
of about 40cm and a ratio of 1.42 between consecutive
scales [11]. This suggests that there should be about 10
modules in total in the rat grid system with a maximum
period of about 10m. Fitting our theoretical predictions
to experimental data [11], we found that a range of a few
tens of meters can indeed be covered with a high cover-
age probability in the range 80-90%. Within the range
of parameters that allows this coverage in our model,
we predict a decrease of about 50 −70% in the num-
ber of neurons between the ﬁrst and the tenth module
(Fig. 6). Experimental uncertainties and possible biases
in recording from harder-to-reach modules with larger
periods, prevent stringent ﬁts. Nevertheless, our theory
robustly states that the number of neurons should decline
with the period of the grid module.
III.
DISCUSSION
A striking experimental observation about the grid sys-
tem in the entorhinal cortex is that it is organized in
discrete modules that share similar periods, orientations
and ellipticities [11]. Given this modular structure, the


## Page 6


6
A
B
50
100
150
0
1
2
λ (cm)
N/N1
0
5
10
0.4
0.6
0.8
1
module
N/N1
R=10m,  P=0.8
R=30m,  P=0.8
R=10m,  P=0.9
R=30m,  P=0.9
FIG. 6. Number of neurons required for coverage de-
creases with the spatial period. (A) We used experimen-
tal data in [11] to estimate the number of recorded neurons vs
their spatial period (circles). We applied k–means clustering
to identify four modules according to the spatial period. For
each module we computed the associated number of neurons
and plotted the mean and the standard deviation of the num-
ber of neurons N normalized over the number N1 of neurons
for the ﬁrst modulus (black squares and lines). Theoretical
predictions given by Eq. (9) obtained with diﬀerent values
of R and P (lines) are compatible with experimental data.
(B) We extrapolated the number of neurons over ten mod-
ules for diﬀerent values of R, P. Simulation parameters are
λ/ℓ= 1.63, σθ = 0.04, σϵ = 0 and σλ = 6cm.
geometric progression of grid periods can be shown to
minimize the number of neurons required to provide a
speciﬁed spatial resolution [12, 13]. However, why would
a modular architecture be necessary in the ﬁrst place?
In this paper, we have shown that eﬃcient coverage of
space favors modularity.
To study how variability in the grid parameters within
a module would aﬀect the probability of holes in cover-
age, we simply asked whether each neuron did or did not
ﬁre above threshold at a given location. Alternatively,
we could sum ﬁring proﬁles of grid cells to assess how
grid variability aﬀects homogeneity of the population ﬁr-
ing across space. Again, the key variable would be the
correlation in the expected number of action potentials
at each point in space. The overall probability of cov-
erage would be determined by a product of factors over
each correlation volume, leading to the same conclusion.
We chose to analyze coverage because any grid coding
scheme, e.g., [12, 13, 19–23], requires neurons to be ac-
tive at each point in space. Thus, we view our approach
as setting a minimal requirement for a functioning grid
system for encoding location. Our model predicted that
there would be fewer neurons in modules with larger peri-
ods. We compared our theory with the actual numbers of
neurons recorded across modules, which should be taken
with caution because of potential biases in the recording
methods, especially for deeper structures in the brains.
Some additional evidence for a decrease of neurons with
the period of modules stems from the relatively smaller
size of the ventral entorhinal cortex (which is enriched
in large periods) relative to the dorsal region. Indirect
evidence also comes from the larger drifts seen in the
activity of grid cells with larger periods [24] : attractor
models indeed predict that networks with smaller num-
bers of neurons will drift more. Further data is needed to
conﬁrm these indirect lines of evidence. Comprehensive
recordings from many grid modules are challenging be-
cause modules of a given period are not strictly localized
anatomically, and because ventral regions are harder to
record from. But such data will greatly illuminate mod-
els of the functional logic of the grid system, and will
further test our quantitative predictions.
ACKNOWLEDGMENTS
VB was supported by the Fondation P.G. de Gennes
at the ENS, Paris; by NSF grant PHY-1066293 at the
Aspen Center for Physics; and by NSF PoLS grant PHY-
1058202.
VB and MV were supported by NSF Grant
PHY11-25915 at the KITP, Santa Barbara.
Appendix A: Covering probability of non-isosceles
grids
In the main text we analyzed the covering probability
of the grid system assuming isosceles grids; in this Section
we show that our results hold also in the case of general
grids.
The triangular lattice deﬁning the spatial activity of
a grid cell is determined by linear combinations of two
elementary vectors v and u. The reference frame can be
chosen to have the vector u coinciding with the x-axis,
i.e. u = λ2(1, 0) and the vector v = λ1(cos(β), sin(β)),
where β is the angle formed by the two elementary vec-
tors (which can be restricted to the ﬁrst quadrant). The
two positive numbers λ2 and λ1 are the moduli of the
two elementary vectors. The set of the six vertices de-
ﬁned by the triplet u, v, u −v and their opposite vec-
tors, forms an hexagon that can be inscribed into an el-
lipse centered at the origin, whose general equation is
Ax2 + 2Bxy + Cy2 = 1 (see Fig. S1A). The (inverse
squared) length of the two axes of the ellipse is deter-
mined by the eigenvalues of the quadratic form and their
orthogonal directions are determined by the correspond-
ing eigenvectors.
An alternative parametrization of the ellipse is given
by : 1) the direction δ of the axes of the ellipse with
respect to the axes of the reference frame ; 2) the ratio
ϵ between the length of the two axes (i.e. the ellipticity
of the grid as deﬁned in [11]) ; 3) the length λ/√ϵ of the
axis parallel to the x-axis when δ = 0 (the other axis has
length √ϵ λ). By requiring that the ellipse pass through
the three independent vertices u, v, u−v, we obtain the
relations
λ2 =
λ
√F1 ;
λ1 sin β =
√
3
2 λ2F1 ;
λ1 cos β = λ2F2
2
;
F1 ≡ϵ cos2 δ + 1
ϵ sin2 δ ;
F2 ≡1 −
√
3
 ϵ −1
ϵ

sin δ cos δ ,
(A1)


## Page 7


7
which provide a general mapping between the free pa-
rameters λ, ϵ, δ of the ellipse and the free parameters λ1,
λ2, β of the vectors u and v. Ellipses with δ = 0 have
axes aligned with the coordinate system.
Elementary
algebra shows that this condition corresponds to isosce-
les triangles with |v| = |u −v|, i.e. 2λ1 cos β = λ2 or
cos β = 1/
√
1 + 3ϵ2.
The special case of ϵ = 1 ﬁxes
λ1 = λ2 = λ and cos β = 1/2, i.e. corresponds to equilat-
eral triangles. Note that the direction δ is related only to
the deformation of the hexagon deﬁned by the elemen-
tary vectors and its variations do no aﬀect the orientation
θ of the grid.
We generalize the analysis of the main text to cases
where the axes of the ellipse are not aligned with the
coordinate system (δ ̸= 0), which generally corresponds
to scalene triangles. We choose a parametrization where
ϵ, δ and λ vary independently. The upshot is that the
results presented in the main text still hold. Speciﬁcally,
for ﬁxed σλ/λ and σθ we compute the correlation coef-
ﬁcient between the number of neurons that are active
at the center of two unit cells, as described in the main
text. Fig. S1 illustrates the results of the simulations for
diﬀerent values of σϵ and σδ using general grids. As for
the other sources of variability, the correlation decreases
rapidly with the separation between the two centers and
the correlation length decreases as σϵ and σδ increase.
Finally, Fig. S1D also shows that the covering probabil-
ity conforms to the relation (5) presented in the main
text.
Appendix B: Analysis of the correlation function
with no orientation variance
In the main text we showed that, as long as there is
some variability in the orientation, the correlation func-
tion of the number of neurons active at two spatial points
tends to zero as the distance increases. Here we discuss
the asymptotic behavior of the correlation function in the
case without orientation variance in the grid parameters.
The derivation of the asymptotic correlation has been
outlined in Section II B; the absence of orientation vari-
ance aﬀects the computation of the conditional probabil-
ity as follows. We divide space into unit cells using the
mean grid parameters and indicate with φn the phase in
the unit cells centered at y = (nλ, 0), n = 0, 1, . . . . In
the case in which the grid has the same orientation as
the mean grid but diﬀerent period (λ′ ̸= λ), the phase
φn will gradually shift along the x−axis as n increases
but it will always belong to a one dimensional surface
with ﬁxed y component equal to φy
0.
For large n the
phase becomes randomly distributed along the segment
[(n −1/2)λ, (n + 1/2)λ]. The resulting probability that
the point y is covered, given that x = (0, 0) is covered,
depends on φy
0. In particular, a grid that covers the point
x will have an intersection of length 2
q
ℓ2/4 −(φy
0)2 be-
tween its ﬁring ﬁeld and the segment [−1/2λ, +1/2λ].
A
B
C
D
σ δ = 0. 0 3
σ δ = 0. 0 6
σ δ = 0. 1 0
σθ = 0.01, σλ / λ
, σ
= 0.01
= 0.06
σ δ = 0. 0 3
σ δ = 0. 0 6
σ δ = 0. 1 0
0
10
20
30
10
−2
10
0
x / λ
ρ ( n( x) , n( 0 ) )
0
20
40
0
0.5
1
R/ λ
P
σθ = 0.01, σλ / λ
, σ
= 0.01
= 0.06
u
v
v-u
δ
σ θ = 0 . 0 1, σ λ / λ = 0.01
σ δ
σ
L /λ
0
0.05
0.1
0
0.05
0.1
0.15
3
5
10
15
0.15
FIG. S1. Variability in ellipticity ϵ and direction δ in-
duces decorrelation of activity and decreases the cov-
ering probability. We perform the same analysis as in the
main text for the more general case δ ̸= 0. (A) Represen-
tation of the grid activity with δ ̸= 0. The six ﬁring ﬁelds
deﬁned by the triplet u, v, u −v and their opposite vectors
(green circles) have centers belonging to an ellipses (curved
red line), the ellipse axes (straight red lines) are rotated ro-
tated by an angle δ respect to the vector u aligned with the
x-axis. (B) The Pearson correlation coeﬃcient is computed as
in Fig. 2 (σλ/λ = 0.01, σθ = 0.01, σϵ = 0.06). (C) Correlation
length for diﬀerent values of σϵ and σδ computed as in Fig. 2
(σλ/λ = 0.01, σθ = 0.01).
(D) Covering probability com-
puted as in Fig. 4 (σλ/λ = 0.01, σθ = 0.01, σϵ = 0.06). We
ﬁnd that increasing variability reduces the correlation length
and decreases the covering probability. Eq. (8) correctly de-
scribes the covering probability as a function of variance and
environment size.
Because of the previous argument, for large n this in-
terval will be uniformly distributed along the segment
[(n −1/2)λ, (n + 1/2)λ] so it will cover the point y with
probability
Qφ(y|x) =
2
q
ℓ2/4 −(φy
0)2
λ
.
(B1)
Furthermore, the probability to have a neuron active at


## Page 8


8
x is
Qφ(x) =
(
0
if (φx
0)2 + (φy
0)2 > (ℓ/2)2 ,
1
(φx
0)2 + (φy
0)2 ≤(ℓ/2)2 .
(B2)
Combining the previous results we obtain ⟨a(y)a(x)⟩→
4
√
3ℓ3
9λ3 . Hence, if the orientation variance is zero the corre-
lation coeﬃcient between two distant points reaches the
asymptotic value
ρ(a(∞), a(0)) =
8ℓ
3πλ −
πℓ2
2
√
3λ2
1 −
πℓ2
2
√
3λ2
.
(B3)
This has been conﬁrmed numerically in Fig. S2.
The
same argument holds if ellipticity variance is present.
In the main text we deﬁned the correlation length of
a grid system as the distance at which the correlation
in the number of active cells falls below the threshold
1/e. Results of the present Section qualify the range in
which this threshold could be chosen. Indeed, for a given
ℓ/λ, Eq. (B3) gives the asymptotic value of the corre-
lation function when no variance in the orientation is
present, e.g. in the biological system ℓ/λ ≈1/1.63 and
the asymptotic value of the correlation is about 0.28 (see
Fig. S2B). Because of the eﬀect described above, if the
threshold used to deﬁne the correlation length is chosen
below this value, the correlation length will depend only
on the orientation variance. Hence, in order to assess the
length scale of correlation that is aﬀected by the variance
in all the grid parameters, a threshold slightly above the
asymptotic value should be chosen (in the main text we
used 1/e.)
This choice is relevant because it captures
the dependence of the covering probability on the vari-
ance in the grid parameters. In fact, if our deﬁnition of
the correlation length is used to analyze the covering of
a system, the analytical results obtained from our ap-
proach are in agreement with direct numerical analysis
performed with (see Fig. 4) and without (see Fig. S2D)
orientation variance.
Appendix C: Covering probability of a unit cell
We discuss the covering probability of a unit cell in one
dimension. We take each grid cell to be active in intervals
of length ℓ, regularly spaced with centers at distance λ
apart. A unit cell is given by an interval of length λ.
The covering probability of a unit cell by N grid cells is
analogous of that of covering a region of length λ by N
intervals of length ℓwith periodic boundary conditions
on the region.
This probability distribution has been
computed analytically in [25] and reads
P

N, ℓ
λ

=
N
X
k=0
(−1)k
N
k

f(k) ,
(C1)
where f(k) = (1 −kℓ/λ)N−1 if kℓ< λ and f(k) = 0
otherwise. For large N this relation reduces to the result
used in the main text P = 1 −N (1 −ℓ/λ)N−1.
0
10
20
10
0
σ θ= 0, σ = 0 , σλ / λ= 0.0 7
x / λ
ρ ( n ( x ) , n ( 0 ) )
= 0 . 1 2
= 0 . 6 1
= 0 . 8 6
0
0.5
1
0
0.1
0.2
0.3
0.4
ρ ( n ( ∞) , n ( 0 ) )
0
10
20
10
0
x / λ
ρ ( n ( x ) , n ( 0 ) )
σ λ / λ= 0 . 0 2
σ λ / λ = 0 . 0 7
σ λ / λ
= 0 . 1 2
0
20
40
0
0.5
1
R/ λ
P c( R )
σ θ= 0, σ = 0 ,
= 0.6 1
10
-1
10
-1
A
B
C
D
FIG. S2. The correlation length depends on the be-
havior above the asymptotic value of the correlation.
(A) When there is no variance in grid orientations, the corre-
lation function between the number of active cells at two lo-
cations, ρ(n(x), n(0)), approaches a nonzero asymptotic value
that depends on ℓ/λ. The solid lines indicate the theoretical
prediction of the asymptotic values from Eq. (B3). Simula-
tion parameters are σλ/λ = 0.07, σθ = 0, σϵ = 0. (B) The
asymptotic value of the correlation in the absence of orien-
tation variance is predicted by Eq. (B3) (black line). Rep-
resentative values corresponding to the three curves in panel
A are marked by the colored symbles. Note that there is a
maximum value in the asymptotic correlation as a function of
l/λ. (C) The correlation decreases faster when the variance
in the period increases (ℓ/λ = 0.61, σθ = 0, σϵ = 0). (D) Nu-
merical simulations (colored symbols) determine the covering
probability of the environment for the diﬀerent variances in
the grid parameters and environment sizes. The numerics are
accurately predicted by Eq. (9) of the main text (solid lines)
in which the correlation length for a grid system was assessed
as the distance at which ρ in panel C decreased to 1/e. This
threshold is always larger than the asymptotic value of the
correlation (see main text).
The proof of (C1) is presented below for the sake of
completeness. Because we have periodic boundary con-
ditions on the region to be covered, we can regard it as
a circle of unit length and we can take the intervals of
length ζ = ℓ/λ to be arcs on this circle. The arcs are la-
belled by their order of occurrence in the anti-clockwise


## Page 9


9
direction around the circle, starting by convention from
the north pole. The arcs are identiﬁed by their initial
position ; there is a gap after the r-th arc if the distance
between the initial positions of the r-th and the r + 1-th
arcs is larger than the size of the arcs. For convenience,
we rigidly translate all the arcs so that the ﬁrst one is
positioned at the north pole – this convention does not
aﬀect the probability of coverage.
Consider N random arcs of length ζ on the circle.
Draw k arbitrary arcs from this set (say (r1, r2, . . . rk),
with k ≤N). Let f(k) be the probability that each arc
in this randomly selected subset is followed by a gap, ir-
respective of the state (followed by a gap or not) of all the
other arcs. From the f(k)’s, the probability (C1) of leav-
ing no gaps is computed as follows. First, let Q(ng, nu) be
the probability that ng prescribed arcs are each followed
by a gap and nu prescribed arcs are each not followed by
a gap, with the rest of the N arcs in unspeciﬁed states.
Then, Q(ng, 1) = f(ng) −f(ng + 1) because f(ng) in-
cludes the probability that the extra arc might be gapped
or ungapped, while f(ng + 1) subtracts the probability
that the extra arc is in fact gapped. By a similar reason-
ing we obtain Q(ng, 2) = Q(ng, 1) −Q(ng + 1, 1) and so
on recursively up to ng + nu = N. Simple algebra shows
then that the probability of leaving no gaps is
P

N, ℓ
λ

= Q(0, N) =
N
X
k=0
(−1)k
N
k

f(k) .
(C2)
The formula (C2) leaves us to determine the expres-
sion of f(k), which is done as follows. When an arc, say
r, is followed by a gap, we rigidly shift backward (clock-
wise) all the following arcs up to the last (N-th) by an
amount ζ. Because the r-th arc is followed by a gap, the
state of all the arcs other than r is not aﬀected by this
backward shift and we are left with a ﬁnal region of size
ζ that does not contain any initial position of the arcs
(see Fig. S3). Note that whether the N-th arc is gapped
or ungapped before this shift corresponds to whether or
not the last arc partially overlaps with the ﬁnal region
of size ζ. The probability of distributing N −1 initial
positions of the arcs (other than the ﬁrst one ﬁxed at the
origin) in a region of size 1 −ζ gives f(1) = (1 −ζ)N−1.
The reasoning for f(2) is similar. If the two prescribed
gapped arcs are r1 and r2 > r1, we ﬁrst shift backward
by ζ all the arcs following r1 and then again by ζ those
following r2. We are then left with a ﬁnal unoccupied
region of size 2ζ. The crucial point is that the state of all
the arcs other than r1 and r2 is again unaﬀected. We can
then compute f(2) = (1 −2ζ)N−1 as the probability of
distributing N −1 initial positions of the arcs in the avail-
able region of size 1 −2ζ. Generalizing the reasoning to
k arcs gives the expression f(k) = (1 −kζ)N−1, provided
the total length of the arcs is smaller than the length of
the circumference, i.e. kζ ≤1, otherwise f(k) = 0. That
completes the proof and yields Eq. (C1).
[1] E. C. Tolman, Psych. Review 55, 189 (1948).
[2] J. D. J. O’Keefe, Brain Research 34, 171 (1971).
[3] T. Hafting, M. Fyhn, S. Molden, M.-B. Moser, and E. I.
Moser, Nature 436, 801 (2005).
[4] J. B. Ranck, Society for Neuroscience Abstracts 10
(1984).
[5] E. Kropﬀ, J. E. Carmichael, M.-B. Moser,
and E. I.
Moser, Nature 523, 419 (2015).
[6] F. Savelli, D. Yoganarasimha,
and J. J. Knierim, Hip-
pocampus 18, 1270 (2008).
[7] T. Solstad, C. N. Boccara, E. Kropﬀ, M.-B. Moser, and
E. I. Moser, Science 322, 1865 (2008).
[8] E. I. Moser, Y. Roudi, M. P. Witter,
and C. Kentros,
Nature Publishing Group 15, 466 (2014).
[9] R. Muller and J. Kubie, Journal of Neuroscience 7, 1951
(1987), cited By 651.
[10] C. Barry, R. Hayman, N. Burgess,
and K. J. Jeﬀery,
Nature neuroscience 10, 682 (2007).
[11] H. Stensola, T. Stensola, T. Solstad, K. Froland, M.-B.
Moser, and E. I. Moser, Nature 492, 72 (2012).
[12] X.-x. Wei, J. Prentice, and V. Balasubramanian, eLife ,
e08362 (2015).
[13] A. Mathis, A. V. Herz, and M. Stemmler, Neural Comp.
24, 2280 (2012).
[14] M. Barth´elemy, Physics Reports 499, 1 (2-11).
[15] L. M. Giocomo, S. a. Hussaini, F. Zheng, E. R. Kandel,
M.-B. Moser, and E. I. Moser, Cell 147, 1159 (2011).
[16] D. E. Davis, J. T. Emlen, and A. W. Stokes, Journal of
Mammalogy , 207 (1948).
A
B
7r
6r
5r
4r
3r
2r
1r
7r
6r
5r
4r
3r
2r
1r
FIG. S3.
Shift of the arcs following the gap aﬀects
only the covering of the arc that is followed by the
gap. (A) Circle of unit length with seven arcs of which only
the initial position has been represented (red lines at angle
rk). Each arc has length ζ = 1/4 and the 5-th arc is followed
by a gap (green region). (B) the 6-th and 7-th arc have been
rotated clockwise by an angle π/2 that corresponds to an arc
of length ζ. The rotation shifts the gap to the region before
the ﬁrst arc and does not aﬀect the state of the 6-th and 7-th
arc.
[17] S. E. Braun, Journal of Mammalogy 66, 1 (1985).
[18] N. A. Slade and R. K. Swihart, Journal of Mammalogy
64, 580 (1983).
[19] I. R. Fiete, Y. Burak,
and T. Brookings, J. Neurosci.
28, 6858 (2008).
[20] Y. Burak and I. R. Fiete, PLoS Comp. Bio. 5, e1000291
(2009).
[21] S. Sreenivasan and I. R. Fiete, Nature 14, 1330 (2011).
[22] M. Stemmler, A. Mathis,
and A. V. Herz, bioRxiv


## Page 10


10
(2015).
[23] D. Bush, C. Barry, D. Manson, and N. Burgess, Neuron
87, 507 (2015).
[24] K. Hardcastle, S. Ganguli, and L. M. Giocomo, Neuron
86, 827 (2015).
[25] W. L. Stevens, Ann. Eugenics 9, 315 (1939).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1610_04844v1_complete_coverage_of_space_favors_modularity_of_the_grid_system_in_the_brain
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2016/1610_04844V1_COMPLETE_COVERAGE_OF_SPACE_FAVORS_MODULARITY_OF_THE_GRID_SYSTEM_IN_THE_BRAIN.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

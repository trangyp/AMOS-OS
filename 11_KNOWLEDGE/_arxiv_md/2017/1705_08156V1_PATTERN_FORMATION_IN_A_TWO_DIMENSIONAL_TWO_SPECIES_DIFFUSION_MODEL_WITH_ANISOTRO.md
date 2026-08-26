---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1705.08156v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1705.08156v1_Pattern_formation_in_a_two-dimensional_two-species_diffusion_model_with_anisotro

> Source: 1705.08156v1_Pattern_formation_in_a_two-dimensional_two-species_diffusion_model_with_anisotro.pdf

> Pages: 18

---


## Page 1


Pattern formation in a two-dimensional two-species
diﬀusion model with anisotropic nonlinear
diﬀusivities: a lattice approach
Yuri Yu Tarasevich1, Valeri V Laptev1,2, Andrei S Burmistrov1,
Nikolai I Lebovka3,4
1Astrakhan State University, 20A Tatishchev Street, Astrakhan, 414056, Russia
2Astrakhan State Technical University, 16 Tatishchev Street, Astrakhan, 414025,
Russia
3F. D. Ovcharenko Institute of Biocolloidal Chemistry, NAS of Ukraine, 42 Boulevard
Vernadskogo, 03142 Kiev, Ukraine
4Taras Shevchenko Kiev National University, Department of Physics, 64/13
Volodymyrska Street, 01601 Kiev, Ukraine
E-mail: tarasevich@asu.edu.ru
June 2017
Abstract.
Diﬀusion in a two-species two-dimensional system has been simulated
using a lattice approach. Rodlike particles were considered as linear k-mers of two
mutually perpendicular orientations (kx- and ky-mers) on a square lattice. These kx-
and ky-mers were treated as species of two kinds. A random sequential adsorption
model was used to produce an initial homogeneous distribution of k-mers.
The
concentration of k-mers, p, was varied in the range from 0.1 to the jamming
concentration, pj.
By means of the Monte Carlo technique, translational diﬀusion
of the k-mers was simulated as a random walk, while rotational diﬀusion was ignored.
We demonstrated that the diﬀusion coeﬃcients are strongly anisotropic and nonlinearly
concentration-dependent. For suﬃciently large concentrations (packing densities) and
k ≥6, the system tends toward a well-organized steady state. Boundary conditions
predetermine the ﬁnal state of the system. When periodic boundary conditions are
applied along both directions of the square lattice, the system tends to a steady state
in the form of diagonal stripes. The formation of stripe domains takes longer time
the larger the lattice size, and is observed only for concentrations above a particular
critical value. When insulating (zero ﬂux) boundary conditions are applied along both
directions of the square lattice, each kind of k-mer tries to completely occupy a half
of the lattice divided by a diagonal, e.g., kx-mers locate in the upper left corner, while
the ky-mers are situated in the lower right corner (“yin-yang” pattern). From time
to time, regions built of kx- and ky-mers exchange their locations through irregular
patterns. When mixed boundary conditions are used (periodic boundary conditions
are applied along one direction whereas insulating boundary conditions are applied
along the other one), the system still tends to form the stripes, but they are unstable
and change their spatial orientation.
PACS numbers: 05.40.-a, 64.60.De, 05.10.Ln
arXiv:1705.08156v1  [cond-mat.stat-mech]  23 May 2017


## Page 2


Pattern formation in a two-dimensional two-species diﬀusion model
2
Keywords: pattern formation, Monte Carlo method, nonlinear concentration-dependent
diﬀusion, anisotropic diﬀusion, lattice model, rodlike particles
Submitted to: J. Phys. A: Math. Theor.
1. Introduction
Since Turing’s pioneering work regarding pattern formation [1], numerous research
papers have been devoted to two-species reaction-diﬀusion (RD) systems. The Turing
instability of a homogeneous steady state is one of the best understood theoretical
mechanisms for pattern formation.
Nonequilibrium pattern formation in chemical
systems is based on the interplay between the reactions and diﬀusion (see, e.g., [2]
for a review). In any set of RD partial diﬀerential equations, the reaction terms provide
a nonlinear coupling between equations. Nevertheless, a chemical reaction is not the
sole mechanism that can induce such nonlinear feedback [3]. For instance, cross-diﬀusion
may be quite important in pattern formation [4]. Pattern formation in RD systems can
be considered using a lattice approach [5].
Systems composed of shape-anisotropic (particularly, rodlike) particles demonstrate
orientational order and self-organization [6]. A range of experimental studies for two-
dimensional (2D) systems of vertically vibrated rodlike particles revealed diﬀerent kind
of rearrangement and pattern formation in such systems. For example, a horizontal
monolayer of macroscopic elongated particles of various shapes with aspect ratios
k ranging from 4 to 12.6 have been experimentally tested [7].
These experiments
demonstrated that, at high packing fraction, the shape of the particles is important
for the orientational ordering.
The orientational order in vertically agitated granular-rod monolayers has also been
investigated experimentally [8]. The results have been compared quantitatively using
both equilibrium Monte Carlo (MC) simulations and density functional theory. When
the density is suﬃciently high, short rods form tetratic arrangements, while long rods
form uniaxial nematic state. In both experiments and simulations, the length-to-width
ratio at which the order changes from tetratic to uniaxial was about 7.3. The universality
of this agreement has been illustrated for the ordering of rod-like particles across
equilibrium and nonequilibrium systems. The assembly of granular rods into ordered
states has been found to be independent of either agitation frequency or strength. This
suggests that the speciﬁc nature of energy injection into such a nonequilibrium system
does not play a crucial role [8].
Stainless steel rods with aspect ratios of k = 20, 40, and 60 conﬁned to 2D containers
have been analysed [9, 10]. At high packing densities, the distinct patterns reﬂected
competition between bulk nematic and boundary alignments. In a container of circular
geometry, this competition produced a bipolar conﬁguration with two diametrically
opposed point defects. As packing density increased, the patterning shifted from bipolar
to a uniform alignment [10]. The presence of large-scale collective swirl motions has been


## Page 3


Pattern formation in a two-dimensional two-species diﬀusion model
3
revealed in monolayers of vibrated granular rods (a range of rice species, mustard seeds
and stainless steel rods with aspect ratios from ≈1 to ≈8) [11]. The authors speculated
that the very strong sensitivity of swirling to the shape of the particles could be related
to the formation of tetratic structures.
The self-diﬀusion of colloidal rodlike virus in an isotropic and nematic phase has
been experimentally studied [12].
The ratio D∥/D⊥increases monotonically with
increasing virus concentration, where D∥and D⊥are the diﬀusivities parallel and
perpendicular to the nematic director, respectively. Similar results were obtained for
granular rods on a substrate with experiments using a mono-layer of bead chains in
a vibrated container [13]. Numerous additional examples of patterns and of collective
behaviour in granular media together with appropriate references can be found in the
review [14].
Thus, pattern formation is observed not only in RD systems but also in systems
without any chemical reactions between the species.
The question is which eﬀect
provides nonlinear feedback? Nonlinear cross-diﬀusion may be considered as a possible
candidate.
This suggestion is based on a number of experiments [13].
When the
diﬀusion of granular rod in two dimensions was studied using linked chains on a vibrated
substrate, it was shown that aspect ratio and packing density have signiﬁcant eﬀects on
the diﬀusivity [13].
In recent decades, much attention has been paid to the study of self-assembly in
systems of linear k-mers (particles occupying k adjacent adsorption sites) deposited on
2D lattices. A linear k-mer represents the simplest model of an elongated particle with
an aspect ratio of k. Computer simulations have been extensively applied to investigate
percolation and jamming phenomena for the random sequential absorption (RSA) of
k-mers (see, e.g., [15, 16, 17] and the references therein).
Recently, diﬀusion-driven pattern formation in a 2D system of k-mers has been
studied by means of MC simulation [18]. Periodic boundary conditions (PBCs) were
applied along both directions of a square lattice. Equal numbers of kx-mers and ky-
mers were assumed. The concentration of k-mers was the maximal obtainable for an
RSA mechanism, i.e., systems at jammed states were considered. Notice, that other
mechanisms, e.g., RSA with diﬀusional relaxation can produce more dense systems [19].
Pattern formation as stripe domains was observed only for k ≥6. Nevertheless, some
important questions still remain:
(i) Why is k = 6 the critical length? Which characteristics change critically when k
is changed from 5 to 6? (As a potentially interesting characteristic, the diﬀusion
coeﬃcient is particularly prominent.
Its anisotropy can have an eﬀect on self-
organization.)
(ii) What is the eﬀect of concentration on such pattern formation? Is self-organization
possible in fairly dilute systems?
(iii) Is the ﬁnite-size eﬀect crucial? It is not yet completely clear, whether patterns form
for L ≫k. Although there are clear signs of reorganization, there is no reliable


## Page 4


Pattern formation in a two-dimensional two-species diﬀusion model
4
evidence that patterns arise as a result of any particular initial conditions. What
happens in the continuous limit k/L →0? Does the increase in the size of the
system only lead to an increase in the relaxation time, or do qualitative changes in
its behaviour arise?
(iv) What happens when the number of kx-mers is not equal to the number of ky-mers?
(v) What is the eﬀect of topology on the pattern formation? What happens when the
boundary conditions change? (PBCs are radically diﬀerent from other types of
boundary conditions, since they introduce translational symmetry into the system
in two directions.)
(vi) Is it possible to construct a continuous analogue of the model that has similar
behaviour to the lattice model?
We can speculate that, for rodlike particles with two mutually perpendicular
orientations on a square lattice, pattern formation is the result of nonlinearity in the
diﬀusion coeﬃcients. In the present research, our main goal is to elicit whether random
walks provide nonlinear feedback and produce self-organization. Additionally, this paper
analyses how diﬀerent kinds of boundary conditions aﬀect the pattern formation in a
two-species diﬀusion system. We suggest that pattern formation is a result of correlation
of the movements of the k-mers. These correlations can occur only in fairly dense systems
of moderate size in the presence of translational symmetry (PBCs). For this reason, we
examine the eﬀect of concentration (packing density) and lattice size on the pattern
formation.
In our study, a lattice approach is used.
The diﬀusion of rodlike particles is
simulated by means of kinetic MC simulation. The rest of the paper is constructed
as follows. In section 2, the technical details of the simulations are described and all
necessary quantities are introduced. Section 3 presents our principal ﬁndings. Section 4
summarizes the main results.
2. Details of simulation
2.1. Lattice model
The problem was approached using a square lattice of size L × L. Most calculations
were performed using L = 256. For one particular value of k (k = 12), we examined
the scaling eﬀect using L = 256, 512, 1024, and 2048. We used a range of boundary
conditions:
(i) toroidal boundary conditions, i.e., periodic boundary conditions along both the x
and y axes (PBCs),
(ii) insulating (zero ﬂux) boundary conditions along both the x and y axes (IBCs),
(iii) mixed boundary conditions, i.e., periodic boundary conditions along the x axis and
insulating boundary conditions along the y axis (MBCs).


## Page 5


Pattern formation in a two-dimensional two-species diﬀusion model
5
The RSA model [20] was used to produce an initial homogeneous distribution of
linear k-mers (i.e., rodlike particles occupying k adjacent sites) in a 2D ﬁlm.
The
rodlike particles were deposited randomly and sequentially, and their overlapping with
previously placed particles was forbidden.
In most experiments, the concentration
of the particles corresponded to the jamming state, pj. In this state, no additional
k-mer can be placed because the presented voids are too small or of inappropriate
shape. We additionally studied the eﬀect of concentration on self-organization using
the concentrations p ∈[0.1, pj].
The length of the k-mers (aspect ratio) was varied from 2 to 12. Generally, isotropic
orientation of the k-mers was assumed, i.e., that k-mers oriented along the x and y
directions (kx-mers and ky-mers, respectively) were equiprobable in their deposition.
This corresponded to the zero value of a mean order parameter of the system, deﬁned
as
s = Ny −Nx
N
,
(1)
where Nx and Ny are the numbers of kx-mers and ky-mers, respectively, and N = Ny+Nx
is the total number of k-mers. We also investigated the eﬀect of anisotropy on pattern
formation.
The diﬀusion of k-mers was simulated using the kinetic MC procedure.
In our
simulation, only translational diﬀusion was taken into consideration. This is essentially
the case for fairly dense systems in the jamming state, where rotational diﬀusion is
impeded, especially for large values of k. Undoubtedly, for dilute systems, rotational
diﬀusion can occur, however, this was ignored in our study.
Since our goal is not only to obtain the static equilibrium properties but also the
dynamic correlation functions of the model, we did not consider every k-mer at each
MC step [21, pp. 71,72]. By contrast, an arbitrary k-mer was randomly chosen at each
step and a translational shift by one lattice unit along either the longitudinal (∥) or the
transverse (⊥) axis of the k-mer was attempted. Equal probabilities to choose any of
all the four possible directions to shift the k-mer were assumed. One time step of the
MC computation, which corresponds to an attempted displacement of the total number
of k-mers in the system, N, was taken as the MC time unit. Time counting was started
from the value of tMC = 0, being the initial moment (before diﬀusion), and the total
duration of the simulation was typically 107 MC time units.
2.2. Determination of diﬀusivities
To determinate the components of the diﬀusivity tensor, Einstein–Smoluchovski formula
has been applied
⟨∆i2⟩= 2Dit,
(2)
where i = x, y corresponds to the two possible directions, t is the time, and Di is the
diﬀusion coeﬃcient (diﬀusivity) in the x or y direction, respectively. The left-hand side
of (2) is the mean square displacement (MSD) of a particle from its original position.


## Page 6


Pattern formation in a two-dimensional two-species diﬀusion model
6
Due to the ﬁnite-size of the system under consideration, the total displacement of the
particle cannot exceed L/2 along a direction with PBCs and L along a direction with
IBCs.
To elicit the coeﬃcients of diﬀusion, we considered strongly anisotropic systems,
s = 1. To compute the components of the coeﬃcient of self-diﬀusion, Ds
i , the lattice
was ﬁlled with kx-mers until a given concentration. After that, the displacements of all
the kx-mers were monitored at each given MC step. The MSD is a result of averaging
over 102 independent runs and all kx-mers. ⟨∆x2⟩= 2Ds
xtMC and ⟨∆y2⟩= 2Ds
ytMC
have been ﬁtted by a linear function using the least-square method.
To compute the components of the coeﬃcient of cross-diﬀusion, Dc
i, a single ky-
mer (tracer) has been deposited onto the lattice and, after that, the lattice has been
ﬁlled with kx-mers until a given concentration.
Then, at each given MC step, the
displacement of the tracer has been determined. The MSD is a result of averaging over
104 independent runs.
2.3. Quantities under consideration
For characterization of the rearrangement of the system under consideration, several
quantities were monitored at each given MC step:
(i) The number of clusters, n, built of the same kinds of k-mers, i.e., clusters of kx-mers
and clusters of ky-mers. We used the Hoshen–Kopelman algorithm [22] to ﬁnd the
cluster distribution. To facilitate comparison of the curves for the diﬀerent values
of k, we used normalized numbers of clusters, i.e., the current value divided by the
value at the initial state, tMC = 0.
(ii) The local anisotropy, s, i.e., the order parameter s (1) calculated in a window of
l × l sites and averaged over the entirely set of windows.
(iii) The fraction of interspeciﬁc contacts n∗
xy = nxy/(nxy + nx + ny), where nxy is the
number of interspeciﬁc contacts between the diﬀerent sorts of k-mers (i.e., kx–ky),
nx and ny are the numbers of intraspeciﬁc contacts between k-mers of the same
kind (i.e., kx–kx and ky–ky, respectively).
(iv) The shift ratio, R, i.e., the ratio of the number of shifts of the k-mers along the
transverse axes to the number of shifts along their longitudinal axes during one MC
step.
(v) The electrical conductivities, σ. We used the model described in [18] to transform
the system under consideration into a random resistor network (RRN). The Frank–
Lobb algorithm [23] was applied to calculate the electrical conductivity of such
RRNs.
All the quantities under consideration were averaged over 100 independent statistical
runs, unless otherwise explicitly speciﬁed in the text.


## Page 7


Pattern formation in a two-dimensional two-species diﬀusion model
7
2.4. Estimation of the ﬁnite-size eﬀect
To determine if there were any ﬁnite-size eﬀect, we performed computations for diﬀerent
lattices sizes, L = 256, 512, 1024, and 2048, and a ﬁxed value of k, k = 12, when
PBCs were applied. We chose the largest value of k because the ﬁnite-size eﬀect was
expected to be more pronounced for this case. The results presented in ﬁgure 1 suggest
that the ﬁnite-size eﬀect is important only during the last stage of the transient mode,
105 ≲tMC ≲108.
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
10
5
10
6
10
7
10
8
0.0
0.5
1.0
1.5
2.0
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
10
5
10
6
10
7
10
8
0.00
0.01
0.02
0.03
0.04
0.05
(b)
 
 L = 256
 L = 512
 L = 1024
 L = 2048
n
t
MC
 + 1
(a)
 L = 256
 L = 512
 L = 1024
 L = 2048
R
t
MC
 + 1
Figure 1. Normalized number of clusters, n, and shift ration, R, vs MC steps, tMC,
for diﬀerent lattice sizes when PBCs are applied. k = 12, L = 256 (100 independent
runs), 512 (25 independent runs), 1024 (5 independent runs), and 2048 (one run).
Since simulation using large lattices such as L = 2048 is quite time-consuming,
this makes it diﬃcult to obtain suﬃcient statistical data, we basically used lattices of
moderate size L = 256 to collect the statistics for the principal investigations.
3. Results
3.1. Diﬀusion coeﬃcients
The simulations gave clear evidence that self-diﬀusion is strongly anisotropic.
Both
for self-diﬀusion and for cross-diﬀusion, the diﬀusion coeﬃcients are strongly nonlinear
concentration-dependent (ﬁgure 2). The transversal coeﬃcients of self-diﬀusion, Ds
⊥,
progressively decreased with increasing concentration, whereas the longitudinal ones,
Ds
∥, went through a maximum at p ≈0.45, where Ds
∥and Dc
∥are the coeﬃcients
of diﬀusion when the particle moves along its axis (longitudinal shifts), Ds
⊥and Dc
⊥
are the coeﬃcients of diﬀusion when the particle moves perpendicular to its axis
(transversal shifts).
Thereby, the system under consideration is nonlinear and the
diﬀusion coeﬃcients are anisotropic.


## Page 8


Pattern formation in a two-dimensional two-species diﬀusion model
8
0.0
0.2
0.4
0.6
0.8
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
D
||
        D
 
  k = 12
 
  k = 6
 
  k = 2
0.0
0.2
0.4
0.6
0.8
0.0
0.2
0.4
0.6
0.8
1.0
D /D
0
p
(b)
D /D
0
p
(a)
Figure
2.
Examples of the dependencies of the coeﬃcients of diﬀusion on
concentration, p. D0 is the coeﬃcient of diﬀusion of the monomer. L = 256, PBCs
are applied.
(a) self-diﬀusion, (b) cross-diﬀusion.
The legend corresponds to both
subﬁgures. For clarity view, the results for intermediate values of k have been omitted.
3.2. Periodic boundary conditions
The results presented in this section have been obtained for L = 256, p = pj, s = 0,
unless otherwise explicitly speciﬁed in the text. For all values of k, a transient mode
and a steady state were observed.
Transition mode.
During the transient mode, the initial homogeneous jammed state
transforms into a new state.
For k ≥6, the transient mode is clearly divided into several stages of diﬀusive
reorganization of the system under consideration. We can identify the following stages.
Fluidization. During the ﬁrst stage, the system undergoes drastic changes, namely, the
jammed state (ﬁgure 3a) turns into an unjammed state. Some k-mers play the role
of capstones, i.e., when such a k-mer shifts from its initial position, the whole system
of k-mers becomes more mobile. It is noteworthy that the initial jammed state
(ﬁgure 3a) and unjammed state (ﬁgure 3b) are visually almost indistinguishable,
nevertheless, a number of clusters, n, (ﬁgure 4(a)) clearly evidences that these states
have very diﬀerent connectivity. Upon the transition, the number of clusters, n,
increases (ﬁgure 4(a)), and the shift ratio, R, increases (ﬁgure 4(d)). The end of
this stage corresponds to the maxima of the curves in ﬁgure 4(a) and ﬁgure 4(d).
Its duration is of the order of 100 MC steps for large values of k and of the order
of 10 MC steps for small values of k. By contrast, the local anisotropy, s, does not
change during this stage (ﬁgure 4(c)).
Coarsening. During the second stage, the clusters coarsen and a labyrinthine structure


## Page 9


Pattern formation in a two-dimensional two-species diﬀusion model
9
(a)
(b)
(c)
(d)
(e)
(f)
(g)
Figure 3. Temporal evolution of the system, k = 10, L = 256, PBCs. (a) tMC = 0,
initial jammed state, (b) tMC = 100, end of ﬂuidization, (c) tMC = 104, labyrinth
patterns, (d) tMC = 105, labyrinth patterns are transforming into stripes, (e) tMC =
106, ﬁnal stage of stripe formation, (f) tMC = 107, steady state in the form of diagonal
stripes, (g) ﬁnal “yin-yang” pattern on a torus (the same pattern as in (f)); for clarity,
the major radius of the torus is signiﬁcantly exaggerated.
forms (ﬁgure 3c), the number of clusters, n, decreases (ﬁgure 4a), the shift ratio,
R, decreases (ﬁgure 4d), and the local anisotropy, s, increases (ﬁgure 4c). The
coarsening is complete after a time in the order of 105 MC steps.
Mainland formation. This stage is clearly recognizable only when the lattice size
is large enough. During this stage, the labyrinth patterns transform into compact
areas with irregular borders (‘mainlands’). For L = 256, the narrow step in ﬁgure 4a
at tMC ∼105 corresponds to this stage. For larger values of L, this step is more
easily distinguished, e.g., for L = 1024, it lasts from tMC = 105 up to tMC = 107
(ﬁgure 1).
Pattern formation. During the last stage, regular patterns begin to form. At the
plane, these patterns appear as stripes.
For L = 256, the stripe formation is


## Page 10


Pattern formation in a two-dimensional two-species diﬀusion model
10
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
10
5
10
6
10
7
0.0
0.5
1.0
1.5
2.0
2.5
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
10
5
10
6
10
7
0.00
0.05
0.10
0.15
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
10
5
10
6
10
7
0.0
0.2
0.4
0.6
0.8
1.0
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
10
5
10
6
10
7
10
-2
10
-1
(d)
(c)
(b)
 
 k = 12
 k = 6
 k = 5
 k = 2
 
n
t
MC
 + 1
 
 k = 12
 k = 6
 k = 5
 k = 2
R
t
MC
 + 1
 
 k = 12
 k = 6
 k = 5
 k = 2
s
t
MC
 + 1
(a)
 k = 12
 k = 6
 k = 5
 k = 2
n
*
xy
t
MC
 + 1
Figure 4. Examples of diﬀerent quantities vs MC steps, tMC, when PBCs are applied.
(a) Normalized number of clusters, n.
(b) Fraction of interspeciﬁc contacts, n∗
xy.
(c) Local anisotropy, s. (d) Shift ratio, R.
complete at a time in the order of 106 MC steps.
Its end corresponds to the
transitions to horizontal of the curves in ﬁgures 4a, 4d, 4c, and 4b.
The fraction of interspeciﬁc contacts, n∗
xy, decreases during the entirely transient mode
(ﬁgure 4b).
It is quite remarkable that the durations of the ﬁrst two stages, i.e.,
ﬂuidization and coarsening, are independent of the lattice size when the value of k
is ﬁxed. By contrast, the mainland and stripe formation stages require more time the
larger the size of the system (ﬁgure 1).
Steady state
During this stage, none of the quantities under consideration demonstrate
any tendency to increase or decrease but have essential ﬂuctuations (ﬁnal horizontal
parts of all the curves), the normalized number of clusters, n, and the fraction of
interspeciﬁc contacts, n∗
xy, are very low, while the shift ratio, R, is stable (ﬁgures 4a,
4d, 4c, and 4b). Local anisotropy is large, reﬂecting the occurrence of stripes, with a
typical width of L/2, built of k-mers of the same orientation (ﬁgure 3f). The stripes
become fairly stable, and on a plane, this pattern corresponds to a torus divided into
two equal parts (ﬁgure 3g).


## Page 11


Pattern formation in a two-dimensional two-species diﬀusion model
11
For k < 6, the number of observed stages is fewer than for the larger k-mers. Only
the normalized number of clusters, n, and the shift ratio, R, allow clear identiﬁcation
of the transient mode and the steady state (ﬁgures 4(a) and (d)). The other quantities
vary only insigniﬁcantly with time.
For k = 2, the quantities n and R increase during tMC ≲10, after that no obvious
changes can be observed. For k = 3, 4, and 5, the quantities n and R increase during
tMC ≲10, but after that n decreases during tMC ≲100 when k = 3, 4 and during
tMC ≲105 when k = 5. For k = 5, a smooth decreas of n until ≈0.9 is observed. In
contrast, for k = 2, 3, and 4, n never goes below 1. Moreover, n increases monotonically
up to 1.05 when k = 2. In the ﬁnal stage, n is ﬁxed for values of k = 2, 3, 4, and 5, and
this corresponds to a steady state.
3.3. Eﬀect of concentration
We examined the eﬀect of concentration on pattern formation.
Figure 5 presents
examples of pattern formations at diﬀerent values of p for k = 12.
We found that
the stripes are observed only for fairly dense systems.
(a)
(b)
(c)
(d)
(e)
(f)
Figure 5. Examples of steady-state patterns for diﬀerent concentrations, p. k = 12,
L = 256, tMC = 107, PBCs. (a) p = 0.1, (b) p = 0.2, (c) p = 0.3, (d) p = 0.4,
(e) p = 0.5, (f) p = 0.6.
A transition from a homogeneous steady-state to a patterned steady-state
is continuous, i.e., the stripe domains become less pronounced when the initial
concentration of k-mers decreases. At some initial concentration, the steady-state looks


## Page 12


Pattern formation in a two-dimensional two-species diﬀusion model
12
quite homogeneous. For instance, for the critical concentration, p∗, 0.3 < p∗< 0.4 when
k = 12. For p ≥0.4, the normalized number of clusters clearly demonstrates several
stages of reorganization, while, for p ≤0.3, the curve looks similar to the curves for
k < 6, and for p = pj when stripe domain formation is absent (ﬁgure 6). Figure 6b
presents a phase diagram for the systems under study in a (k, p)-plane, when PBCs are
applied. Here, the curves pc(k) and pj(k) show the dependencies of the initial percolation
threshold and jamming concentrations at tMC = 0. The region with diagonal stripe
formation in the steady state at tMC ≳106 is shown in the phase diagram as the grey-
shaded region. The diagonal stripes are not observed above the jamming concentration
pj nor at small concentrations below some limiting value ps(k). The data show that
at k < 6 the initial jamming suppresses the diagonal stripe formation. However, the
value of ps continuously decreases with increased k and at k > 9; it becomes smaller
than the percolation threshold pc for the given value of k. Previous data have evidenced
that pc(k) dependencies go through a minimum at k ≈16, but then the percolation
threshold, pc, increases at larger values of k [24]. The character of the ps(k) dependence
at large values of k is still unclear and requires further investigations.
(a)
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
10
5
10
6
10
7
0.2
0.4
0.6
0.8
1.0
1.2
k = 12, L = 256
 p = 0.1
 p = 0.2
 p = 0.3
 p = 0.4
 p = 0.5
 p = 0.6
n
t
MC
 + 1
(b)
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
11
12
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
 p
j
 p
c
p
k
p
s
stripe domains
Figure 6.
(a) Normalized number of clusters, n, vs MC steps, tMC, for diﬀerent
concentrations of the k-mers, L = 256, k = 12, PBCs are applied.
(b) phase
diagram in a (k, p)-plane; grey-shaded region corresponds to the values of k and p
when stripe formation occurs; additionally, the percolation threshold and the jamming
concentration are indicated for each value of k.
It is noticeable that pattern formation is accompanied by changes of electrical
conductivity.
When the concentration of particles slightly exceeds the percolation
threshold, the system in its initial state, i.e., a disordered system, is a conductor.
Diﬀusional reorganization leads to a decrease in the electrical conductivity. Figure 7
demonstrates the conductor–insulator phase transition for k = 12 and p = 0.5. This
concentration is a little greater than the percolation threshold, pc ≈0.46. In contrast,
for p = 0.6 (somewhat greater than the percolation threshold) and p = 0.4 (below the
percolation threshold), diﬀusion does not lead to a phase transition from conductor to
insulator.


## Page 13


Pattern formation in a two-dimensional two-species diﬀusion model
13
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
10
5
10
6
10
7
1
2
3
4
5
 p = 0.6
 p = 0.5
 p = 0.4
lg 
t
MC
Figure 7. Examples of the temporal dynamics of electrical conductivity for k = 12
and diﬀerent values of concentration, p.
3.4. Eﬀect of anisotropy
In two-species systems, stripe formation occurs not only in isotropic systems (s = 0) but
also in those systems with unequal numbers of kx-mers and of ky-mers (s ̸= 0). Thus,
for k = 12, the stripe domains occur up to Ny/Nx = 3 (s = 0.5). For larger values of the
ratio, no steady pattern forms until tMC = 107. Instead, a dynamic picture of moveable
wormlike domains can be observed (ﬁgure 8).
(a)
(b)
(c)
Figure 8.
Examples of steady-state patterns for diﬀerent values of the order
parameter, s. (a) s = 0.33, stripe domains; (b) s = 0.5, stripe domains; (c) s = 0.667,
wormlike domains. k = 12, L = 256, tMC = 107, PBCs.
3.5. Eﬀect of boundary conditions
When IBCs are applied, only two stages can be observed during the transient mode,
viz., ﬂuidization and coarsening.
The steady state demonstrates a spatial-temporal
reorganization, i.e., each kind of k-mer tries to completely occupy one half of the lattice
divided by a diagonal, e.g. the kx-mers are located in the upper left corner while the
ky-mers are situated in the lower right corner (“yin-yang” pattern). From time to time,


## Page 14


Pattern formation in a two-dimensional two-species diﬀusion model
14
regions built of kx- and ky-mers exchange their locations through irregular patterns (see
video clip in Supplemental Materials).
For k < 6, all quantities vary with time in almost the same manner as in the
case with PBCs. Nevertheless, for k ≥6 one essential diﬀerence is observed, namely, a
stepwise decrease in the quantities as n, R, and n∗
xy are absent between 105 < tMC < 106
(ﬁgure 9). Only the curves for the particular value of k when stripe formation occurs are
presented. For the smaller values of k, no stripe formation is observed; changes in any of
the quantities with time are insigniﬁcant for these values of k. The conductor–insulator
phase transition does not occur. Although the local anisotropy increases with time, its
ﬁnal value is lower than in the case with PBCs (ﬁgure 9).
For MBCs, when periodic boundary conditions are applied along one direction
(horizontal) while insulating boundary conditions are applied along the perpendicular
direction (vertical) of the square lattice, after the two-stages of the transient mode,
the system tends to form stripes. The stripes are unstable and change their spatial
orientation (see video clip in Supplemental Materials).
Figure 9 compares the variations of the principal quantities with time. Here, the
examples of curves for k = 10 when stripe formation occurs are presented. For values of
k < 6, no stripe formation is observed; changes in n with time are insigniﬁcant for these
values of k. Only two stages of the transient mode are clearly seen. The local anisotropy,
s, increases with time and this reﬂects the formation of the stripes. However, its ﬁnal
value is lower than in the case with PBCs (ﬁgure 9(c)).
3.6. Continuous model
A simplest oﬀ-lattice 2D model of two-species diﬀusion with anisotropic nonlinear
concentration-dependent diﬀusivities can be described by the set of equations
∂u
∂t = ∂
∂x

Ds
1(u)∂u
∂x

+ ∂
∂y

Ds
2(u)∂u
∂y

+ ∂
∂x

Dc
1(v)∂v
∂x

+ ∂
∂y

Dc
2(v)∂v
∂y

, (3)
∂v
∂t = ∂
∂x

Ds
2(v)∂v
∂x

+ ∂
∂y

Ds
1(v)∂v
∂y

+ ∂
∂x

Dc
2(u)∂u
∂x

+ ∂
∂y

Dc
1(u)∂u
∂y

, (4)
where u and v are the concentrations of the components, Ds
i are the coeﬃcients of
self-diﬀusion, and Dc
i are the coeﬃcients of cross-diﬀusion. All diﬀusion coeﬃcients are
concentration-dependent. The ﬁrst two terms on the right-hand sides of (3) and (4)
correspond to self-diﬀusion, while the last two terms describe cross-diﬀusion.
Conceivably, the properties of this model might be similar to the properties of the
lattice model described in section 2. To examine the behaviour of the oﬀ-lattice model,
we took the concentration-dependent diﬀusion coeﬃcients corresponding to the case
k = 12 for the lattice model (ﬁgure 2).
Ds
1(w) = 0.5 exp(−0.09/w),
Ds
2(w) = 0.5 + 0.3w + 1.6w2 −3.2w3,
Dc
1(w) = 0.5 exp(−0.18/w),
Dc
2(w) = 0.5 exp(−0.23/w),


## Page 15


Pattern formation in a two-dimensional two-species diﬀusion model
15
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
10
5
10
6
10
7
0.0
0.5
1.0
1.5
2.0
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
10
5
10
6
10
7
0.00
0.02
0.04
0.06
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
10
5
10
6
10
7
0.0
0.2
0.4
0.6
0.8
1.0
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
10
5
10
6
10
7
0.00
0.01
0.02
0.03
0.04
0.05
(d)
(b)
(c)
 k = 10, PBC's
 k = 10, IBC's
 k = 10, MBC's
n
t
MC
 + 1
(a)
 k = 10, PBC's
 k = 10, IBC's
 k = 10, MBC's
n
*
x y
t
MC
 + 1
 k = 10, PBC's
 k = 10, IBC's
 k = 10, MBC's
s
t
MC
 + 1
 k = 10, PBC's
 k = 10, IBC's
 k = 10, MBC's
R
t
MC
 + 1
Figure 9.
Comparison of behaviour of diﬀerent quantities for diﬀerent kinds of
boundary conditions vs MC steps, tMC, k = 10, L = 256. (a) Normalized number
of clusters, n.
(b) Fraction of interspeciﬁc contacts, n∗
xy.
(c) Local anisotropy, s.
(d) Shift ratio, R.
where w is either u or v.
Using the ﬁnite element method, we have solved the set of equations (3), (4) in a
square region with PBCs. For homogeneous distributions of the concentrations u and
v, the ﬁnal concentration corresponded to the homogeneous distribution.
4. Conclusion
We investigated a 2D lattice model of two-species diﬀusion. The species were considered
as hard-core (completely rigid) rodlike particles of two mutually perpendicular
orientations.
We found that the diﬀusion coeﬃcients of both self-diﬀusion and
cross-diﬀusion are strongly nonlinear concentration-dependent.
A non-monotonic
concentration dependence of the coeﬃcient of self-diﬀusion along the longitudinal axis
of the k-mer is rather surprising. We can speculate that such a feature reﬂects a quasi-
one-dimensional behaviour of the system. No qualitative changes in the coeﬃcients of
diﬀusion have been observed when k increases from 5 to 6. Since Ds
∥is much greater
than Ds
⊥, Dc
∥, and Dc
⊥, any boundary between a region ﬁlled with kx-mers and a region


## Page 16


Pattern formation in a two-dimensional two-species diﬀusion model
16
ﬁlled with ky-mers tends to unbend, i.e. the curvature of the boundary decreases. At
an interface between two regions ﬁlled with the diﬀerent species, any protruding k-
mer retracts into a region with the same orientation of k-mers because movement in
this direction is most probable. This fact can explain both cluster coarsening and the
formation of stripes as well as the wormlike clusters. The larger a cluster, the smaller
is the mean curvature of its boundary; the curvature of an ideal stripe boundary is
equal to zero. Very small values of the coeﬃcients of cross-diﬀusion at the jamming
concentrations explain the presence of long-lived defects when the lattice sizes are large
(L = 1024, 2048) [18]. For a single k-mer, or a compact group the same species trapped
inside a region of another species (e.g., kx-mers inside a region of ky-mers, or vice versa)
their movement to an interface between the regions of the diﬀerent species is restricted
and can take a rather long time. Detailed investigation of eﬀect of boundary condition
on the behaviour of the system was performed for the lattice size L = 256 and the
jamming concentrations, p = pj. We found that, for any boundary conditions under
consideration, no oscillations or patterns were observed when k < 6. In contrast, for
k ≥6, spatial or spatial-temporal pattern formation occurred, i.e., after a transient
mode, the system came into a steady state with stable or periodically changed spatial
patterns.
For those systems with equal number of species belonging to two diﬀerent kinds,
i.e., kx-mers and ky-mers, (s = 0),
(i) for an initial homogeneous spatial distribution of k-mers, stripe domains form even
for L/k ≳103; the ﬁnite-size eﬀect is important only for the last stages of pattern
formation: although initial stages of reorganization are independent of the lattice
size, the last stages, i.e., the stripe formation, are sensitive to the lattice size;
nevertheless, steady state is independent on the lattice size;
(ii) boundary conditions play a crucial role, namely, steady patterns in the form of
stripe domains have been observed only for PBCs ;
(iii) the self-organization is possible only in fairly dense systems;
(iv) when the concentration of particles is slightly above the percolation threshold,
an aging can be observed, i.e., a decrease in the electrical conductivity and the
conductor–insulator phase transition at tMC ≈102.
Moreover, self-organization can occur in the systems with unequal numbers of kx-mers
and ky-mers (s ̸= 0).
An absence of pattern formation in the continuous model may be considered as
indirect evidence that pattern formation in the lattice model is not the result of sole
nonlinearity but also a hard-core (excluded volume) eﬀect. We can assume that some
implicit correlations in the movements of the particles play an important role in the
pattern formation.
These correlations are more prominent when a system is dense
and of moderate size, and the rodlike particles are long enough. We suppose that these
correlations are a result of hard-core (excluded volume) interaction between the particles
in the lattice model. These correlations are absent in the continuous model. This is a


## Page 17


Pattern formation in a two-dimensional two-species diﬀusion model
17
cause of the homogeneous ﬁnal state in the continuous model. The discovery of such
correlations is a particular problem.
The obvious shortcomings of our study are
(i) only relatively short particles (k ≤12) were examined;
(ii) only relatively small lattices (up to L = 2048) were studied;
(iii) a ﬁnite-size eﬀect has been revealed, but this has not been studied in detail;
(iv) long-time behaviour (tMC ≳108) has not been explored.
These shortcomings are a consequence of the fact that MC simulation is quite time-
consuming even at a high-performance computer.
In future studies, one should keep in mind that, among the diﬀerent quantities, the
number of clusters isthe most sensitive to changes of the internal structure of the system
and, hence, it is a particularly useful quantity to use to classify diﬀerent stages of the
reorganization of the system.
Acknowledgments
The reported study was supported by the Ministry of Education and Science of the
Russian Federation, Project No. 3.959.2017/4.6, and the National Academy of Sciences
of Ukraine, Project No. 43/17-H.
References
[1] Turing A M 1952 Phil. Trans. R. Soc. Lond. B 237(641) 37–72 ISSN 00804622
[2] Mikhailov A S and Ertl G 2009 ChemPhysChem 10 86–100 ISSN 1439-7641
[3] Andelman D and Rosensweig R E 2009 J. Phys. Chem. B 113 3785–3798 ISSN 1520-6106
[4] Vanag V K and Epstein I R 2009 Phys. Chem. Chem. Phys. 11(6) 897–912 ISSN 1463-9076
[5] ´Odor G 2004 Rev. Mod. Phys. 76(3) 663–724 ISSN 0034-6861
[6] B¨orzs¨onyi T and Stannarius R 2013 Soft Matter 9 7401–7418 ISSN 1744-6848
[7] Narayan V, Menon N and Ramaswamy S 2006 J. Stat. Mech. – Theory E. 2006 P01005 ISSN
1742-5468
[8] M¨uller T, de las Heras D, Rehberg I and Huang K 2015 Phys. Rev. E 91(6) 062207 ISSN 2470-0045
[9] Galanis J, Harries D, Sackett D L, Losert W and Nossal R 2006 Phys. Rev. Lett. 96 028002 ISSN
0031-9007
[10] Galanis J, Nossal R, Losert W and Harries D 2010 Phys. Rev. Lett. 105 168001 ISSN 0031-9007
[11] Aranson I S, Volfson D and Tsimring L S 2007 Phys. Rev. E 75 051301
[12] Lettinga M P, Barry E and Dogic Z 2005 EPL (Europhysics Letters) 71 692 ISSN 1286-4854
[13] Yadav V and Kudrolli A 2012 Eur. Phys. J. E 35 104 ISSN 1292-895X
[14] Aranson I S and Tsimring L S 2006 Rev. Mod. Phys. 78(2) 641–692 ISSN 0034-6861
[15] Centres P M and Ramirez-Pastor A J 2015 J. Stat. Mech. Theory E. 2015 P10011 ISSN 1742-5468
[16] Kuriata A, Polanowski P and Sikorski A 2016 Macromol. Theor. Simul. 25 360–368 ISSN 1521-3919
[17] Budinski-Petkovi´c L, Lonˇcarevi´c I, Dujak D, Karaˇc A, ˇS´cepanovi´c J R, Jakˇs´c Z M and Vrhovac
S B 2017 Phys. Rev. E 95(2) 022114 ISSN 2470-0045
[18] Lebovka N I, Tarasevich Y Y, Gigiberiya V A and Vygornitskii N V 2017 Phys. Rev. E 95(5)
052130 ISSN 2470-0045
[19] Fusco C, Gallo P and Petri A and Rovere M 2001 J. Chem. Phys. 114 7563–7569 ISSN 0021-9606


## Page 18


Pattern formation in a two-dimensional two-species diﬀusion model
18
[20] Evans J W 1993 Rev. Mod. Phys. 65(4) 1281–1329 ISSN 0034-68611
[21] Landau D P and Binder K 2014 A Guide to Monte Carlo Simulations in Statistical Physics 4th
ed (Cambridge: Cambridge University Press) ISBN 9781107074026
[22] Hoshen J and Kopelman R 1976 Phys. Rev. B 14(8) 3438–3445 ISSN 2469-9950
[23] Frank D J and Lobb C J 1988 Phys. Rev. B 37(1) 302–307 ISSN 2469-9950
[24] Tarasevich Y Y, Lebovka N I and Laptev V V 2012 Phys. Rev. E 86(6) 061116 ISSN 2470-0045

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
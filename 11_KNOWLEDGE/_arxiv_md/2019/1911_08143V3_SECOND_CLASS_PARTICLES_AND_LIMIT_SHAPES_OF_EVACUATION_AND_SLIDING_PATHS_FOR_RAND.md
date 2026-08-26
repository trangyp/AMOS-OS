---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.08143v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1911.08143v3_Second_class_particles_and_limit_shapes_of_evacuation_and_sliding_paths_for_rand

> Source: 1911.08143v3_Second_class_particles_and_limit_shapes_of_evacuation_and_sliding_paths_for_rand.pdf

> Pages: 92

---


## Page 1


arXiv:1911.08143v3  [math.CO]  23 Mar 2022
SECOND CLASS PARTICLES
AND LIMIT SHAPES OF EVACUATION AND SLIDING PATHS
FOR RANDOM TABLEAUX
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
ABSTRACT. We investigate two closely related setups. In the ﬁrst one
we consider a TASEP-style system of particles with speciﬁed initial and
ﬁnal conﬁgurations. The probability of each history of the system is
assumed to be equal. We show that the rescaled trajectory of the second
class particle converges (as the size of the system tends to inﬁnity) to a
random arc of an ellipse.
In the second setup we consider a uniformly random Young tableau
of square shape and look for typical (in the sense of probability) sliding
paths and evacuation paths in the asymptotic setting as the size of the
square tends to inﬁnity. We show that the probability distribution of such
paths converges to a random meridian connecting the opposite corners
of the square. We also discuss analogous results for non-square Young
tableaux.
1. INTRODUCTION
This article is the full version of a 12-page extended abstract [M´S20]
which was published in the proceedings of the 32nd International Confer-
ence on Formal Power Series and Algebraic Combinatorics, FPSAC 2020.
The results of the current paper concern two distinct setups which are
closely connected. The ﬁrst one, presented in Section 1.1, involves a cer-
tain interacting particle system. The second one, presented in Section 1.3,
involves random Young tableaux.
1.1. TASEP system with the uniform distribution over histories.
1.1.1. The setup. For given integers N, M ≥1 we consider the particle
system depicted on Figure 1. There are N + M −1 nodes, labeled by the
2020 Mathematics Subject Classiﬁcation. 60C05 (Primary), 05E10, 60K35, 82C22
(Secondary).
Key words and phrases. second class particles, interacting particle systems, TASEP, ran-
dom Young tableaux, limit shape, jeu de taquin, promotion, Schützenberger’s evacuation,
square Young tableaux.
1


## Page 2


2
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
x
−N + 1
−2
−1
0
1
2
M −1
M −N
(a)
x
−N + 1
−2
−1
0
1
2
M −1
M −N
(b)
Figure 1. (a) The initial conﬁguration of the particle system.
The ﬁrst class particles are depicted as ﬁlled blue circles, the
holes are depicted as empty circles. The striped red circle
denotes the second class particle. (b) The ﬁnal conﬁguration
of the particle system.
⇓
(a)
⇓
(b)
⇓
(c)
Figure 2. Three allowed types of transitions: (a) a ﬁrst class
particle can jump to the right if the next node is free, (b) the
second class particle can jump to the right if the next node
is free, (c) the ﬁrst class particle can jump to the right if the
next node is occupied by the second class particle; in this
case the second class particle has to yield and the particles
exchange their places.
integers from the set
(1.1)
{−N + 1, . . . , 0, 1, . . . , M −1}.
In the initial conﬁguration (which corresponds to the time t = 1) the N −1
nodes which correspond to the negative integers are occupied by the ﬁrst
class particles, the M −1 nodes which correspond to the positive integers
are empty (or, equivalently, are occupied by holes), and the node which
corresponds to zero is occupied by the second class particle, see Figure 1a.


## Page 3


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
3
In each step exactly one of the following transitions occurs:
• any particle (ﬁrst or second class) may jump right to the next node
provided that this node is empty, see Figures 2a and 2b, or
• a ﬁrst class particle may jump right to the next node provided that
this node is occupied by the second class particle. In this case the
second class particle has to yield and jumps one node to the left, see
Figure 2c.
The second class particle is an analogue of a passenger with a cheap second
class ticket who has to yield the seat to any passenger with a more expensive
ﬁrst class ticket.
It is not very difﬁcult to show that no matter which transitions occur, the
system terminates at time tmax = MN (that is after MN −1 transitions)
in the conﬁguration shown on Figure 1b in which no additional transition is
allowed.
By the history we will understand the information about the state of the
particle system over all values of the time t ∈{1, . . . , tmax}, see Figure 3
for an example. We consider the ﬁnite set of all possible histories of the par-
ticle system and associate to each such a history equal probability. In other
words, we consider a version of the TASEP (which is an acronym for To-
tally Asymmetric Simple Exclusion Process) system [Spi70] with modiﬁed
transition probabilities.
1.1.2. Why second class particles? Macroscopic quantities describing an
interacting particle system (such as particle density) are usually described
by nonlinear partial differential equations (PDEs for short). For example,
the famous Burgers equation [Bur48] describes the density proﬁle in the hy-
drodynamical limit for the asymmetric simple exclusion process [BF87].
Weak solutions of nonlinear PDEs can develop singularities, often referred
to as shocks. The shocks can be found by looking for the crossings of
the characteristic lines of the PDE.
Ferrari [Fer92] discovered that a second class particle, depending on
the place in which it begins its journey, can identify microscopically the
location of the shock or describe the behavior of the characteristic lines of
the limiting hydrodynamic equation. Ferrari and Fontes showed in [FF94]
that this hydrodynamical limit converges to the traveling wave solution of
the inviscid Burgers equation. This connection was later transferred to more
general settings by Rezakhanlou [Rez95], Ferrari and Kipnis [FK95], Sep-
päläinen [Sep01] and others. Furthermore, the second class particle enters
naturally in the study of the ﬂuctuations of the current of particles [FF94].


## Page 4


4
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
X
T
1
0
1
−1
√
θ
−1
√
θ
Figure 3. Sample history of the particle system for N = 4
and M = 8. The trajectories of the ﬁrst class particles are
shown as solid blue lines, the trajectory of the second class
particle is shown as the thick red line. The thick green rec-
tangle indicates the bounding box. The dashed line indicates
the arctic ellipse which corresponds to the shape parameter
θ = M
N = 2.
A pictorial interpretation of TASEP as a trafﬁc model is given in [MG05].
The particles are interpreted as cars on a single-line highway with no possi-
bility of passing (which corresponds to the exclusion rule) and the shock cor-
responds to the front of the trafﬁc jam. The motion of the shock is referred
to as the propagation of the shock or the rarefaction wave (or rarefaction
fan) depending whether the shock moves to the left or is being resorpted.
The second class particle identiﬁes the shock and allows to qualitatively
describe its motion.
Mountford and Guiol [MG05] studied in fact a more advanced physi-
cal interpretation of the TASEP model as a moving interface on the plane
(space-time). This gave them a powerful tool to analyze the shocks in the
TASEP process in terms of the last passage percolation.


## Page 5


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
5
X
T
1
0
1
−1
√
θ
−1
√
θ
Figure 4. An analogue of Figure 3 for N = 15 and M = 30.
A nice heuristic (as well as rigorous) explanation of the shocks behavior
and the importance of the second class particles in this context can be found
in the book of Liggett [Lig99, Part III].
1.1.3. The asymptotic setup. We assume that (Mi) and (Ni) are two se-
quences of positive integers which tend to inﬁnity and such that their ratio
lim
i→∞
Mi
Ni
= θ > 0
converges to some positive limit which we call the shape parameter. For
t ∈{1, . . . , MiNi} we denote by ui(t) ∈{−Ni + 1, . . . , Mi −1} the
position of the second class particle at time t. In order to keep the notation
lightweight we will sometimes omit the index i and instead of Mi, Ni, ui(t)
we will write shortly M, N, u(t).
Until now we parameterized the space using the integer parameter x ∈
{−N+1, . . . , M−1} and the time using the integer parameter t ∈{1, . . . , MN},
however for asymptotic questions it is more convenient to pass to the rescaled


## Page 6


6
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
coordinates
X =
x
√
MN
∈
"
−
1
p
M/N
,
p
M/N
#
,
T =
t
tmax
∈[0, 1],
see Figures 3 and 4. The rectangle
(1.2)
Bθ =
(
(X, T) : X ∈

−1
√
θ
,
√
θ

,
T ∈[0, 1]
)
which shows the range in which the coordinates X and T vary asymptoti-
cally will be called the bounding box; on Figures 3 to 5 it is shown as the
green rectangle.
For each value of the parameter s ∈[−1, 1] we deﬁne a function
Ξs : [0, 1] →

−1
√
θ
,
√
θ

given by
Ξs(T) = 2
p
T(1 −T) s + θ −1
√
θ
T,
see Figure 5.
1.1.4. The main result 1: the trajectory of the second class particle.
Theorem 1.1. We keep the assumptions and notations from Section 1.1.3.
Then there exists a sequence (Si) of random variables with the property
that the supremum distance
sup
T∈[0,1]

1
√MiNi
ui
 ⌈TMiNi⌉

−ΞSi(T)

converges in probability to zero, as i →∞.
The probability distribution of Si is supported on the interval [−1, 1] and
for i →∞it converges to the standard semicircular distribution with the
density
(1.3)
fSC(x) = 2
π
√
1 −x2
for x ∈[−1, 1].
This theorem is illustrated on Figure 5. Its proof is postponed to Sec-
tion 11. This result is analogous to the results of Ferrari and Kipnis [FK95],
as well as Mountford and Guiol [MG05] for the usual TASEP system start-
ing from a decreasing shock proﬁle.


## Page 7


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
7
X
T
θ−1
√
θ
1
1
1+θ
θ
1+θ
1
−1
−1
√
θ
√
θ
Figure 5. The dashed lines are arcs of ellipses Ξs for the
shape parameter θ = 2. The shown values of the parameter
s ∈F −1
SC

0/10, 1/10, . . . , 10/10
	
are the deciles of the semi-
circle distribution (above FSC : [−1, 1] →[0, 1] denotes the
cumulative distribution function of the semicircle distribu-
tion (1.3)). The shaded region forms the arctic ellipse. The
four black dots are the points where the arctic ellipse is tan-
gent to the bounding box. The solid zigzag lines are trajecto-
ries of the second class particle for N = 500 and M = 1000.
These trajectories were selected from a sample of 1000 sim-
ulations; each of them corresponds to an appropriate empir-
ical decile of the distribution of the second class particle at
time T = 1
2.
1.1.5. The limit trajectories. Each curve Ξs for the parameter s ∈[−1, 1] \ {0}
is an arc of an ellipse which ﬁts into the bounding box Bθ, passes through
the points
(1.4)
(0, 0),
θ −1
√
θ
, 1

,


## Page 8


8
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
and is tangent there to the bottom and the top edge of the bounding box Bθ.
In the degenerate case s = 0 the curve Ξ0 is a straight line connecting
the aforementioned two points (1.4). The union of the two extreme curves
Ξ−1 and Ξ1 is the unique ellipse (which we call the arctic ellipse) which is
inscribed into the bounding box Bθ and is tangent to its bottom and its top
side in the aforementioned two points (1.4), see Figure 5. In the special case
θ = 1 the scaling of the axes can be chosen in such a way that the arctic
ellipse becomes a circle which we call the “the arctic circle”. Our use of
this name is not a coincidence since it turns out to be indeed related to the
celebrated arctic circle theorem [Rom12].
1.2. Random sorting networks. Theorem 1.1 can be regarded as the solu-
tion to a toy version of the problem of random sorting networks considered
by Angel, Holroyd, Romik, and Virág [AHRV07]. More speciﬁcally, we
consider the symmetric group SN+M−1 viewed as the set of permutations
of the set of nodes (1.1) and the permutation ρN,M ∈SN+M−1 deﬁned as
ρN,M(i) =





i + M
if i ∈{−N + 1, . . . , −1},
M −N
if i = 0,
i −N
if i ∈{1, . . . , M −1}
which describes the change of the positions of the particles and holes during
the passage from the initial conﬁguration shown on Figure 1a to the ﬁnal
conﬁguration shown on Figure 1b. For an integer s ∈{−N +1, . . . , M −2}
denote the adjacent transposition at location s by τs = (s, s+1) ∈SN+M−1.
Any history of the particle system considered in Section 1.1.1 can be
encoded by the sequence s1, . . . , stmax−1 ∈{−N + 1, . . . , M −2}, where
st and st + 1 are the nodes which are interchanged in t-th transition. It is
easy to check that
(1.5)
ρN,M = τstmax−1τstmax−2 · · · τs2 τs1
and the corresponding sequence of partial products
(1.6)
id,
τs1,
τs2τs1,
. . . ,
τstmax−1τstmax−2 · · · τs2 τs1
is a shortest path from the identity permutation id to ρN,M in the Cayley
graph of the symmetric group SN+M−1 generated by adjacent transposi-
tions.
Conversely, each shortest path (1.6) in the Cayley graph gives a valid
history of the particle system. Any such a shortest path will be called a
sorting network. The trajectory of the second class particle
(1.7)
 u(t) : t ∈{1, . . . , tmax}

=
 0,
τs1(0),
τs2τs1(0),
. . . ,
τstmax−1 · · · τs2τs1(0)



## Page 9


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
9
corresponds in this language to the sequence of images of 0 under the action
of the entries of the sequence (1.6).
Angel, Holroyd, Romik, and Virág [AHRV07] considered a more difﬁ-
cult version of this setup in which the permutation ρN,M is replaced by the
reverse permutation ρ ∈SN+M−1 given by
ρ(i) = M −N −i
and—among several other results—stated some conjectures concerning the
asymptotic behavior of the right-hand side of (1.7) for a random sorting
network, i.e., a random shortest path from the identity permutation id to
the reverse permutation ρ, sampled with the uniform distribution. We fo-
cus today on [AHRV07, Conjecture 1] which is a direct analogue of our
Theorem 1.1. A minor difference is that the limit curves which appear in
Theorem 1.1 form a one-parameter family of arcs of ellipses while the limit
curves which appear in [AHRV07, Conjecture 1] form a one-parameter fam-
ily of sine curves. (At ﬁrst sight it might appear that the family of curves
in [AHRV07] has two parameters, but one of these parameters can be elim-
inated by the requirement about the positions of the endpoints.)
The aforementioned conjecture [AHRV07, Conjecture 1] was proved only
very recently by Dauvergne and Virág [DV20] who used methods quite dif-
ferent from those which we use in the current paper.
1.3. Sliding paths and evacuation paths in random tableaux. As promised,
we turn now to the second interest area of the current paper, namely to ran-
dom Young tableaux.
1.3.1. Notations related to Young diagrams and tableaux. We assume the
reader’s basic knowledge of tableaux theory, including partitions, (skew)
Young diagrams, standard (skew) Young tableaux, RSK algorithm, jeu de
taquin, rectiﬁcation, Littlewood–Richardson coefﬁcients and basics of the
representation theory of the symmetric groups.
We denote the set of partitions of n by Yn. We draw Young diagrams
on the Cartesian plane using the French convention, that is, we draw them
from the bottom to the top, see Figure 6a.
For any Young diagram λ we denote the set of standard Young tableaux
of shape λ by Tλ. The shape of a tableau T will be denoted by sh(T) and
its size by | sh(T)|, or shortly |T|.
Let T be a tableau. If p is a number which appears exactly once in T
(which will always be the case in our considerations), we deﬁne the position
of the box with the number p as the Cartesian coordinates of the bottom-
left corner of the unique square which contains p; we denote this position
by posp(T). For example, for T from Figure 6b, pos5(T) = (2, 0).


## Page 10


10
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
x
y
1
2
3
4
5
1
2
3
4
5
(a)
x
y
1
2
3
4
5
1
2
3
4
5
1
3
2
5
9
4
6
8
7
(b)
Figure 6. (a) The Young diagram λ = (4, 3, 1, 1) shown in
the Cartesian coordinate system. (b) Example of a standard
Young tableau of shape λ.
We will have a particular interest in Young diagrams and tableaux of
square shape. By □N ∈YN2 we denote the square diagram with side of
length N.
1.3.2. Sliding paths and evacuation paths. One of the operations heavily
used in the study of Young tableaux is jeu de taquin [Ful97, Section 1.2],
which acts on Young tableaux in the following way (see Figures 8a and 8b):
we remove the bottom-left box of the given tableau T and obtain a hole in
its place. Then we look at the two boxes: the one to the right and the one
above the hole, and choose the one which contains the smaller number. We
slide this smaller box into the location of the hole, see Figure 7. As a result,
the hole moves in the opposite direction. We continue this operation as long
as there is some box to the right or above the hole. The path which was tra-
versed by the ‘traveling hole’ will be called the sliding path, see Figure 8a.
The result of jeu de taquin applied to a tableau T will be denoted by j(T),
see Figure 8b.
If T is a standard tableau then j(T) is no longer standard because the num-
bering of its boxes starts with 2; however, if we decrease each entry of
j(T) by 1 then it becomes standard. This observation allows us to deﬁne
the dual promotion ∂∗: Tλ →Tλ which is a bijection on the set of stan-
dard Young tableaux of any ﬁxed shape λ. The idea is to put once again
the box with the number |T| to the aforementioned standardized version of
the tableau j(T) in the place where we removed a box during jeu de taquin,
see Figure 8c.


## Page 11


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
11
r
s
(a)
r
s
(b)
r
s
(c)
Figure 7. Elementary step of the jeu de taquin transforma-
tion: (a) the initial conﬁguration of boxes, (b) the outcome of
the slide in the case when r < s, (c) the outcome of the slide
in the case when s < r. Copyright ©2014 Society for Indus-
trial and Applied Mathematics. Reprinted from [´Sni14] with
permission. All rights reserved.
1
2
3
7
10 13
4
5
6
8
11
9
12
(a)
2
4
3
7
10 13
6
5
9
8
11
12
(b)
1
3
2
6
9
12
5
4
8
7
10
11
13
(c)
Figure 8. (a) A standard Young tableau T of shape λ =
(5, 4, 2, 1). The highlighted boxes form the sliding path. (b)
The outcome j(T) of the jeu de taquin transformation. (c)
The result ∂∗(T) of the dual promotion applied to T.
For a given tableau T ∈Tλ with n = |λ| boxes the jeu de taquin trans-
formation j can be iterated n times until we end with the empty tableau.
During each iteration the box with the biggest number n either moves one
node left or down, or stays put. Its trajectory
(1.8)
evac(T) =

posn(T), posn
 j(T)

, . . . , posn
 jn−1(T)

will be called the evacuation path.
1.3.3. The main results 2 and 3: asymptotics of sliding paths and evacu-
ation paths. Observe that if we draw the boxes of a given square tableau
T ∈T□N as little squares of size
1
N then the corresponding sliding path
is a zigzag line connecting the opposite corners of the unit square [0, 1]2.


## Page 12


12
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
Let T ∈T□N be a random standard Young tableau of square shape (sam-
pled with the uniform probability distribution on T□N which will be denoted
PN). Our goal is to ﬁnd asymptotics of such random zigzag lines in the
limit as N →∞, see Figure 9. We will show that there exists a family of
smooth lines, called meridians, which connect the opposite corners of the
unit square, with the property that the probability distribution of the scaled
sliding path for a random tableau converges, as N →∞, to a random
meridian.
An analogous result holds true for the scaled evacuation path for a ran-
dom square tableau: during iteratively applied jeu de taquin operations j,
the biggest box of the tableau asymptotically moves along a random merid-
ian.
A version of this result applies also to the other boxes of the tableau; it
follows that the time evolution of the tableau in the iterated applications of
jeu de taquin
(1.9)
T, j(T), j2(T), . . . , jN2(T)
converges in probability, as N →∞, to dynamics of an incompressible
liquid which ﬂows along the meridians.
For the details of our results, see Theorems 2.3 and 2.4 in Section 2.
1.3.4. Not only squares. For simplicity and concreteness we stated our main
results concerning random Young tableaux only for large random Young
tableaux of square shape. However, analogous results hold true also for ran-
dom tableaux of shape which is a balanced Young diagram (see Section 3
for the deﬁnition and Figure 10 for a teaser). In Section 10 we present a way
in which the results obtained in this paper can be used (or generalized) in
order to cover the class of balanced Young diagrams.
1.4. The content of the paper. The paper is organized as follows.
In Section 2 we state the main results (Theorems 2.3 and 2.4) about the
typical shapes of the evacuation paths and sliding paths in square Young
tableaux.
In Section 3 we give basic deﬁnitions on permutations and representation
theory.
In Section 4 we introduce a ‘surfers’ language which we will use to de-
scribe dynamics of the box with the biggest entry (which we will call ‘the
surfer’) and the smaller boxes (‘the water’). In this spirit we also introduce
the story of the multisurfers which will play a crucial role in our proofs and
considerations. We will use this new multisurfer story later as a point of
reference for the original problem of the (single) surfer in order to prove


## Page 13


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
13
x
y
1
1
Figure 9. The nine zigzag lines are sample sliding paths
for random square tableaux of size N
= 100, selected
so that they cross the anti-diagonal near the correspond-
ing meridians (smooth thick curves) with the longitudes
ψ ∈{1/10, 2/10, . . . , 9/10}. The gray lines are the meridians
with the longitudes ψ ∈{2/100, 4/100, . . . , 98/100}. See also the
blue-to-red family of curves on Figure 13.
Theorem 4.1 concerning the position of the surfer along its journey. We
sketch the proof in Section 4.4.
In Section 5 we show the way in which we will embed simultaneously
both the story of the single surfer and the story of the multisurfers into a
common universe.
In Section 6 we provide Theorem 6.2 concerning the distribution of the
multisurfers on the water. We use here the Jucys–Murphy elements to give
a direct link between the statistical properties of the multisurfers and the


## Page 14


14
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
Figure 10. Sample sliding paths in random Young tableaux
of an L-shape with 3600 boxes.
symmetric group characters evaluated on certain polynomials in the Jucys–
Murphy elements.
In Section 7 we use the aforementioned results from Sections 5 and 6 to
prove Theorem 4.1.
In Section 8 we prove Theorem 2.3 concerning typical evacuation paths.
Section 9 is devoted to the proof of Proposition 9.1 which shows the
equivalence between the problems of ﬁnding the sliding paths and the evac-
uation paths in random Young tableaux of given shape.
In Section 10 we extend our main results (Theorem 10.5) concerning
typical evacuation and sliding paths to some subset of C-balanced Young
tableaux.
In Section 11 we provide the link between the trajectory of the second
class particle in an interacting particle system and the sliding path for a
random Young tableau and prove Theorem 1.1.
2. THE LIMIT SHAPE OF SLIDING PATHS AND EVACUATION PATHS
2.1. Asymptotics of a single box in the evacuation trajectory. As we
mentioned in Section 1.3, we will focus on random standard Young tableaux
of square shape □N sampled according to the uniform measure PN. The
symbol TN will be reserved for such a uniformly random square Young
tableau of shape □N.
The position of each of the boxes in the evacuation path (1.8) coincides
with the position of a speciﬁc box in the standard Young tableau obtained


## Page 15


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
15
x
y
1
2
3
4
1
2
3
4
−1
1
2
3
1
2
3
4
5
u = x −y
v = x + y
Figure 11. The Cartesian and the Russian coordinate sys-
tems on the plane.
by iterating the dual promotion ∂∗:
(2.1)
posN2
 ji(TN)

= posN2−i
 ∂∗i(TN)

.
Since ∂∗: T□N →T□N is a bijection, for each i ≥0 the latter standard
tableaux ∂∗i(TN) is also a uniformly random square Young tableau. It fol-
lows that the solution to the (much simpler) problem of understanding the
asymptotics of a single element of the evacuation trajectory (1.8) follows
from the work of Pittel and Romik [PR07], see also Section 2.3 below. In
the current section we will recall the details of their work and we will use
it to state our second main result, Theorem 2.3 (which addresses the more
complex problem of understanding the whole evacuation trajectory (1.8))
and the third main result, Theorem 2.4.
2.2. The circles of latitude gα. The Russian coordinate system is given by
the following transformation of the Cartesian plane (warning: our notations
differ from those of Pittel and Romik [PR07] who scale the coordinates
below by an additional factor 1/
√
2):
u := x −y,
v := x + y,
see Figure 11.


## Page 16


16
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
For each 0 ≤α ≤1 and u ∈
h
−2
p
α(1 −α), 2
p
α(1 −α)
i
deﬁne
kα,u :=
p
4α(1 −α) −u2
and for any 0 < α < 1 the function
hα :
h
−2
p
α(1 −α), 2
p
α(1 −α)
i
→R
given by
(2.2)
hα(u) :=







2u
π arctan

1−2α
kα,u · u

+ 2
π arctan

kα,u
1−2α

if 0 < α < 1
2,
2 −2u
π arctan

2α−1
kα,u · u

−2
π arctan

kα,u
2α−1

if
1
2 < α < 1,
1
if α = 1
2.
In the expression above there may occur kα,u = 0 in the denominator; in
such case (for ﬁxed α ∈(0, 1)) we consider the appropriate limit: if u0 =
±2
p
α(1 −α) then
hα(u0) := lim
u→u0 hα(u) =
(
u0
for 0 < α < 1
2,
2 −u0
for 1
2 < α < 1.
Additionally we deﬁne the one-point functions h0(0) := 0 and h1(0) := 2.
For any α ∈[0, 1] we consider the curve which in the Russian coordinate
system is deﬁned as
(2.3)
gRus
α
:=
n u, hα(u)
 : |u| ≤2
p
α(1 −α)
o
⊂R2
and, equivalently, in the Cartesian coordinates is given by (see Figures 12
and 13)
gα :=
(u + hα(u)
2
, hα(u) −u
2

: |u| ≤2
p
α(1 −α)
)
⊂[0, 1]2.
We call gα the circle of latitude with the latitude α.
Roughly speaking, for each α ∈[0, 1] the (scaled down) α-level curve
(which separates the boxes with entries ≤αN2 from the boxes bigger than
this threshold, see Figure 12) in a uniformly random square tableau TN
converges in probability, as N →∞, to the circle of latitude gα, see [PR07,
Theorem 1] for a precise statement.


## Page 17


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
17
x
y
1
1
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
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
Figure 12. A scaled down sample random square tableau of
size N = 10. The zigzag lines are the level curves for α ∈
{1/4, 2/4, 3/4}. The smooth lines are the corresponding circles
of latitude gα, see also the orange-to-green family of curves
on Figure 13.
2.3. The random position of the box ⌊αN2⌋, the limit measure να. Pittel
and Romik [PR07, Theorem 2] also found the explicit formula for the limit
distribution of the scaled down location
1
N pos⌊αN2⌋(TN)
of the entry ⌊αN2⌋in a uniformly random square Young tableau TN, as
N →∞. This limit distribution turns out to be supported on the circle of
latitude gα and thus it is uniquely determined by the probability distribution


## Page 18


18
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
of the u-coordinate. The latter, denoted by να, turns out to be the semicir-
cular distribution on the interval
h
−2
p
α(1 −α), 2
p
α(1 −α)
i
with the
density
(2.4)
fνα(u) :=
kα,u
2πα(1 −α).
2.4. Geographic coordinates on the square. For any point p = (x, y) ∈
[0, 1]2 of the unit square there is exactly one α = α(p) ∈[0, 1] such that p
lies on the curve gα. We say that the latitude of p is equal to α. With the
notations of Pittel and Romik [PR07] the latitude α(x, y) = L(x, y) is just
the limit height function of random square standard Young tableaux.
The longitude of p, which we denote by
ψ(p) = να
 (−∞, x −y]

= Fνα(x −y),
is deﬁned as the mass of the points on the curve gα which have their u-coordinate
not greater than the u-coordinate of the point p or, equivalently, in terms of
the cumulative distribution function Fνα of the measure να. Notice that
ψ((0, 0)) = ψ((1, 1)) = 1. The set of points of the unit square [0, 1]2 with
equal longitude ψ is a curve called the meridian ψ, see Figures 9 and 13.
For given α ∈(0, 1) and ψ ∈[0, 1] we denote by
Pα,ψ =

xψ
α, yψ
α

∈[0, 1]2
the unique point of the unit square [0, 1]2 with the latitude α and the lon-
gitude ψ. We set additionally P0,ψ = (0, 0) and P1,ψ = (1, 1) for any
ψ ∈[0, 1]. We denote by
uψ
α := xψ
α −yψ
α
and
vψ
α := xψ
α + yψ
α
the u- and v-coordinate of the point
 xψ
α, yψ
α

= Pα,ψ.
Remark 2.1. We will not use the following observation, but fans of car-
tography may ﬁnd it interesting: for reasons which will hopefully become
obvious later on, the map
[0, 1]2 ∋(α, ψ) 7→Pα,ψ ∈[0, 1]2
is equiareal which manifests by equality of the areas of the curvilinear rect-
angles on Figure 13.
Remark 2.2. The result of Pittel and Romik [PR07, Theorem 2] is a special
case of a general phenomenon of existence of the level curves (circles of
latitudes) for random Young tableaux of speciﬁed shape. Biane [Bia98]
proved that such level curves exist for any balanced sequence of Young
diagrams, see Section 10 for more information.


## Page 19


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
19
x
y
1
1
Figure 13. The geographic coordinate system on the unit
square [0, 1]2. The blue-to-red family of thick colored curves
connecting the bottom left and the upper right corner are
the meridians with the longitudes ψ ∈{1/10, 2/10, . . . , 9/10}.
The gray lines are the meridians with the longitudes
ψ ∈{2/100, 4/100, . . . , 98/100}, cf. Figure 9.
The orange-to-
green family of thick colored curves are the circles of lat-
itudes gα with the latitudes α ∈{1/10, 2/10, . . . , 9/10}. The
thin, gray lines are the circles of latitude gα with the lati-
tudes α ∈{2/100, 4/100, . . . , 98/100}, see Figure 12. The shown
meridians and circles of latitude split the square into a 50×50
grid of curvilinear rectangles with equal areas.


## Page 20


20
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
2.5. The second main result. Typical evacuation path. For a given tableau
TN ∈T□N and t ∈[0, 1) we denote by
(2.5)
Xt = Xt(TN) = 1
N posN2

j⌊tN2⌋(TN)

∈[0, 1]2
the scaled down position of the point from the evacuation path evac(TN),
cf. (1.8). Clearly, the parameter t indicates how many boxes were removed
so far and therefore we can relate to it as the time.
Our second main result states that, asymptotically, the scaled evacuation
path in a random square tableau is a random meridian, see Figure 9.
Theorem 2.3. For each N ∈N there exists a random variable ΨN : T□N →
[0, 1] such that the supremum distance
(2.6)
sup
t∈[0,1]
Xt(TN) −P1−t,ΨN(TN )

converges in probability to zero, as N →∞. More explicitly: for each
ε > 0
lim
N→∞PN
n
TN ∈T□N : sup
t∈[0,1]
Xt(TN) −P1−t,ΨN(TN)
 > ε
o
= 0.
The probability distribution of the random variable ΨN converges, as
N →∞, to the uniform distribution on the unit interval [0, 1].
In other words (with a small abuse of notation), the random trajectory
 Xt(TN)

t∈[0,1] with respect to the supremum norm converges in distribu-
tion to a random meridian
 P1−t,ψ

t∈[0,1] when N →∞, that is shortly,
 Xt(TN)

t∈[0,1]
d
−−−→
N→∞
 P1−t,ψ

t∈[0,1] ,
where ψ is a random variable with the uniform U(0, 1) distribution.
The proof is postponed to Section 8 and the preparations to it will take
the majority of time.
2.6. The third main result. Typical sliding path. Let T be a standard
Young tableau with n boxes. Sometimes when investigating the sliding path,
we are concerned not only about its shape, but also we would like to be able
to tell which entries were placed in the rearranged boxes. This motivates
the notion of the sliding path in the lazy parametrization (or shortly the
lazy sliding path) which is a sequence of boxes q(T) := (q1, . . . , qn) ⊂N2
where qi is the last box along the sliding path corresponding to T (cf. Fig-
ure 8a) which contains a number ≤i, cf. [R´S15, Section 3.3].
Our third main result is stated in the language of lazy sliding path and
says that, asymptotically, the scaled sliding path in a random square tableau
is, just like in Theorem 2.3, a random meridian, see Figure 9.


## Page 21


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
21
Theorem 2.4. For each N ∈N there exists a random variable eΨN : T□N →
[0, 1] such that the supremum distance
sup
t∈[0,1]

1
N q⌈tN2⌉(TN) −Pt,eΨN(TN )

converges in probability to zero, as N →∞.
The probability distribution of the random variable eΨN converges, as
N →∞, to the uniform distribution on the unit interval [0, 1].
In other words (with a small abuse of notation), the lazy sliding path
 q⌈tN2⌉(TN)

t∈[0,1] with respect to the supremum norm converges in distri-
bution to a random meridian
 Pt,ψ

t∈[0,1] when N →∞, that is shortly,
1
N q⌈tN2⌉(TN)
d
−−−→
N→∞Pt,ψ
where ψ is a random variable with the uniform U(0, 1) distribution.
The proof is postponed to Section 9.2 and is based on showing that the
random lazy sliding path and the (reversed) random evacuation path have
the same distribution, cf. Proposition 9.1. In other words, we show that
the problem of ﬁnding typical sliding paths is equivalent to the problem of
ﬁnding typical evacuation paths from Theorem 2.3.
2.7. Conjecture on the independence of the iterated sliding paths. Re-
call from Section 1.3.2 that the dual promotion ∂∗is a bijection deﬁned by
a two-step procedure in which ﬁrst we apply the jeu de taquin and then we
add the box which was removed from the initial tableau T. We can iterate
∂∗on the random tableau TN and get the sequence of iterated sliding paths
(2.7)
q(TN) ,
q
 ∂∗(TN)

,
q
 (∂∗)2(TN)

,
. . . .
Since ∂∗is a bijection, Theorem 2.4 provides asymptotics of the distribution
of each element of the sequence (2.7) separately. The following conjecture
aims to provide asymptotic information about their joint distribution.
Conjecture 2.5. For each integer k ≥1 the probability distribution of the
random vector

eΨN(TN),
eΨN
 ∂∗(TN)

,
. . . ,
eΨN
 (∂∗)k−1(TN)

converges, as N →∞, to the uniform distribution on the unit cube [0, 1]k.
Romik and the second named author proved an analogue of this conjec-
ture in the case of the Plancherel-distributed random inﬁnite tableaux, see
[R´S15, the comment below Theorem 1.5] and Section 2.8 for more details.


## Page 22


22
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
2.8. Something old, something new, something borrowed: sliding paths
for random inﬁnite tableaux. The problem of the asymptotic shape of
a sliding path (analogous to the one from Theorem 2.4) was studied be-
fore by Romik and the second named author [R´S15, Section 1.3] for a
certain inﬁnite random Young tableau, more speciﬁcally for the recording
tableau Q(x1, x2, . . . ) obtained by applying the Robinson–Schensted corre-
spondence to an inﬁnite sequence (x1, x2, . . . ) of independent, identically
distributed random variables with the uniform distribution on the unit inter-
val [0, 1]. Such a choice corresponds to sampling the random Young tableau
according to, so called, the Plancherel measure.
In such a setting the sliding path happens to converge almost surely to
a straight line with a random direction [R´S15, Theorem 1.1], in other words
the analogue of our meridians in the context of the Plancherel measure is
given by the straight lines emanating from the origin of the coordinate sys-
tem.
One of the main difﬁculties in the proof of Theorem 2.4 will be the con-
struction of the random variables eΨN which provide the longitude of the
meridian along which the sliding path travels. This difﬁculty is absent in
[R´S15] because in that context the analogue of the longitude turns out to
be simply equal to x1, the ﬁrst entry of the random sequence to which the
Robinson–Schensted correspondence is applied.
It would be tempting to repeat the approach from [R´S15] in our context,
for example one could proceed as follows. Let
π(N) =

π(N)
1
, . . . , π(N)
N2

be a uniformly random element of the set of extremal Erd˝os–Szekeres per-
mutations, i.e., permutations with the property that the corresponding tableaux
associated via the Robinson–Schensted correspondence have the square shape □N.
Then the corresponding recording tableau TN = Q(π(N)) is, as required, a
uniformly random standard Young tableau of square shape □N. A naive
guess would be that one possible choice for the random variable eΨN is
again (a rescaled version of) the ﬁrst entry of the permutation, i.e., π(N)
1
.
Uniformly random extremal Erd˝os–Szekeres permutations were investi-
gated by Romik [Rom06] who proved, among other results, that the prob-
ability distribution of
1
N2π(N)
1
converges to the point measure concentrated
in 1
2. For this reason it seems that the random variables π(N)
1
do not carry any
information which would be useful for our purposes, hence the approach
from [R´S15] is not applicable here directly, and the construction of the ran-
dom variables eΨN must follow different ideas.


## Page 23


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
23
Despite this fundamental difference, an astute reader may notice that our
proof of Theorem 2.3 follows a path parallel to the one of [R´S15, Theo-
rem 5.1]. For example, the counterpart of our Proposition 6.5 (which can
be viewed as a result about a certain random process of removal of boxes
from a Young diagram) is [R´S15, Theorem 4.4] (which concerns a certain
random process of addition of boxes to a Young diagram).
3. PRELIMINARIES
3.1. Permutations, Young diagrams and Young tableaux, continued.
We continue Section 1.3.1 where some basic deﬁnitions were introduced.
By N we denote the set of positive integers and we denote N0 := N ∪
{0}. For any natural number n, we deﬁne the set [n] := {1, . . . , n}. From
the following on (unlike in Section 1.2) we will view the symmetric group
Sn as the group of permutations of the set [n]. We deﬁne the length of a
permutation π to be the minimal number of factors necessary to write π as
a product of (arbitrary, not necessarily adjacent!) transpositions, and denote
it by |π|.
For any Young diagram λ, we denote the number of standard Young
tableaux of shape λ by f λ = |Tλ|. If T ∈Tλ and 0 ≤p ≤|λ| we con-
sider the restriction of T to its p least boxes by removing the entries which
are bigger than p, and denote the obtained tableau by T|≤p (clearly, it is also
a standard Young tableau).
For C ≥1 we say that a Young diagram λ is C-balanced if λ has at most
C
p
|λ| rows and at most C
p
|λ| columns.
For a tableau T and an integer p which appears exactly once in T (which
will always be the case in our considerations) we deﬁne the u-coordinate of
the box with the entry p as
uT
p := x −y
for (x, y) = posp(T).
Note that in the literature, for instance in [CSST10], such a u-coordinate is
called the content.
We will also consider skew tableaux obtained by removing some boxes
from Young tableaux. Let T ∈Tλ be a standard Young tableau. If T with
the boxes with entries a1, . . . , ai removed is a skew tableau, we denote it by
T \ {a1, . . . , ai}. Clearly, T \ {p + 1, . . . , |λ|} = T|≤p is also a standard
Young tableau.
3.2. Representation theory. If G is a ﬁnite group and ρ: G →End V is
its representation on a ﬁnite-dimensional complex linear space V , then by
ξV (g) := Tr ρ(g),
g ∈G,


## Page 24


24
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
we denote its character (we write just ξ if it is clear which representation we
consider). We also consider the normalized character χV : G →C given
by
χV :=
1
dim V · ξV =
1
ξV (id) · ξV .
Additionally, for any element of the group algebra
f =
X
g∈G
fgg ∈CG
we denote by χV (f) the extension of the character by linearity given by
χV (f) :=
X
g∈G
fg χV (g) ∈C.
On the vector space of functions G := {f : G →C} we consider the
standard scalar product given by
⟨f, g⟩:= 1
|G|
X
h∈G
f(h) g(h),
for f, g ∈G,
where c denotes the complex conjugation.
We will denote by ˆG the family of irreducible representations (irreps for
short) of G. It is known that the system of irreducible characters {ξVx}x∈ˆG
is orthonormal. Therefore for the normalized irreducible characters the fol-
lowing holds:
D
χV1, χV2
E
=



1
dim V1
if χV1 = χV2,
0
otherwise.
Let V be a ﬁnite-dimensional representation and let
V =
M
x∈ˆG
mxVx
be its decomposition into irreducible components, where mx ∈N denotes
the multiplicity of x. By a random irreducible component of V we will
understand a random element of ˆG sampled according to the probability
measure PV which is proportional to the total dimension of all copies of a
given irrep in V :
(3.1)
PV (x) := mx dim Vx
dim V
= (dim Vx)2 ·

χV , χx

for x ∈ˆG.
The trivial representation will be denoted by triv. If H is a subgroup of
G then we denote by ρ ↓G
H the restriction of a representation ρ to H (if G is
ﬁxed we just write ρ ↓H).


## Page 25


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
25
For λ ∈Yn we denote by ρλ: Sn →End Vλ the irreducible representa-
tion of the symmetric group Sn corresponding to the Young diagram λ and
by χλ its normalized character.
3.3. Asymptotics of characters and the approximate factorization prop-
erty. We will use two results concerning asymptotics of characters. The
ﬁrst one, due to Feráy and the second named author, gives an upper bound
on the irreducible characters.
Fact 3.1 ([F´S11, Theorem 1]). There exists a constant a > 0 such that for
any Young diagram λ and any permutation π ∈S|λ|
(3.2)
χλ(π)
 ≤
"
a max
r(λ)
|λ| , c(λ)
|λ| , |π|
|λ|
#|π|
where r(λ) and c(λ) stand, accordingly, for the number of rows and the
number of columns of λ.
The second result, due to Biane (and its generalization due to the second-
named author), shows that the character calculated on the product of two
ﬁxed permutations with disjoint supports approximately factorizes.
Fact 3.2 ([Bia98, Corollary 1.3], [Bia01, Section 0], [´Sni06, Theorem 1]).
Let C ≥1 and m ∈N. There exists a constant K > 0 such that for each
C-balanced Young diagram λ and all permutations σ, τ ∈S|λ| with disjoint
supports and satisfying |σ|, |τ| ≤m we have
χλ(στ) −χλ(σ)χλ(τ)
 ≤
K
p
|λ|
|σ|+|τ|+2.
3.4. Jucys–Murphy elements. In the applications of Fact 3.1 and Fact 3.2
we will encounter the expressions in the left-hand-side of (3.4). The lemma
below gives an upper bound for their values.
Its proof uses Jucys–Murphy elements which often appear in the modern
approach to the representation theory of the symmetric groups (see [CSST10])
and are deﬁned as the following elements of the symmetric group algebra
CSn
(3.3) Jk :=
X
1≤i<k
(i, k) = (1, k)+· · ·+(k−1, k) ∈CSn
for 1 ≤k ≤n.
The elements J1, . . . , Jn ∈CSn form a commuting family in the symmetric
group algebra. We will use them intensively in Section 6.


## Page 26


26
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
Lemma 3.3. For any c > 0 and n ∈N
(3.4)
X
π∈Sn
c|π| < exp
 
n2c
2
!
.
Proof. For any c ∈C the following simple identity in the symmetric group
algebra holds true
X
π∈Sn
c|π|π = (1 + cJ1)(1 + cJ2) · · · (1 + cJn).
By applying the trivial representation to both sides of the above equality we
get that for c > 0
X
π∈Sn
c|π| = (1 + c)(1 + 2c) · · ·
 1 + (n −1)c

<
ece2c · · · e(n−1)c < exp
 
n2c
2
!
.
□
4. THE LONGITUDE AND SURFING
Our strategy towards the proof of Theorem 2.3 is to pass to the geographic
coordinates of the point Xt = Xt(TN) from the scaled evacuation trajec-
tory (2.5). Having the choice between the latitude and the longitude, we
start with the more challenging problem of understanding how the longi-
tude ψ(Xt) changes over time t.
Instead of considering the longitude ψ(Xt) directly, it will be more con-
venient to study the following random variable which we call the theoretical
longitude:
(4.1)
Ψth
N(t) := Fν1−t
 u(Xt)

,
where u(Xt) denotes the u-coordinate of Xt = Xt(TN), and Fν1−t is the
cumulative distribution function of the limit measure ν1−t which was de-
ﬁned in Section 2.3.
Notice that if in time t the box with the biggest
number is positioned exactly on the circle of latitude α = 1 −t, that is,
α(Xt) = 1 −t, then the theoretical longitude coincides with the longitude,
i.e., Ψth
N(t) = ψ(Xt). Heuristically one would expect that Ψth
N (t) ≈ψ(Xt)
for N →∞.
Roughly speaking, the following result states that (away from the polar
regions which correspond to t = 0 and t = 1) the theoretical longitude
of Xt does not change too much over time.


## Page 27


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
27
Theorem 4.1. Assume that 0 < t1 < t2 < 1. Then for each ε > 0
lim
N→∞PN

TN ∈T□N :
Ψth
N(t2) −Ψth
N(t1)
 > ε

= 0.
In other words, the difference Ψth
N (t2) −Ψth
N (t1) converges in probability
to 0 when N →∞, that is shortly,
Ψth
N(t2) −Ψth
N(t1)
P
−−−→
N→∞0.
The proof is quite involved; Sections 4 to 7.2 are a preparation while
the proof of Theorem 4.1 itself will be given in Sections 7.3 and 7.4. The
remaining part of the current section is devoted to a rough sketch of the
proof.
Clearly, Theorem 4.1 is equivalent to the conjunction of the following
two statements for ε > 0:
lim
N→∞PN

TN ∈T□N : Ψth
N (t2) −Ψth
N (t1) > ε

= 0,
(4.2)
lim
N→∞PN

TN ∈T□N : Ψth
N (t2) −Ψth
N (t1) < −ε

= 0.
(4.3)
We start with the proof of the upper bound (4.2). Then we will use the
symmetry of the problem in order to prove the lower bound (4.3).
4.1. The single surfer scenario. We would like to present the problem of
the evacuation path in a different, more vivid light. We will speak about
a square pool of side N (=the square Young diagram □N) ﬁlled with N2 −1
particles of water (=the Young tableau TN with the largest entry removed),
a passive surfer (=the box with the biggest entry N2) and its trajectory
(or behavior) when the pool is being drained (=iteratively applying jeu de
taquin). Our goal in Theorem 2.3 is to show that, when the pool is big
enough, the surfer has some typical paths along which he/she moves as the
pool is being drained.
In our proof of Theorem 4.1 we start our analysis at time t1 when jeu de
taquin was already applied
(4.4)
m1 := ⌊t1N2⌋
times. Our starting point is therefore the standard tableau
(4.5)
T ′
N := ∂∗m1(TN)

≤N2−m1
with N2 −m1 boxes (compare with (1.9)). We denote
(4.6)
w1 = N2 −m1 −1.


## Page 28


28
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
In this way the boxes with numbers 1, . . . , w1 correspond to the water and
the box with the maximal number w1 + 1 to the surfer. The position of the
latter box will be called the initial position of the surfer and we will refer
to the tableau T ′
N as the initial surfer conﬁguration. By removing the box
with the surfer
(4.7)
W ′
N := T ′
N \ {w1 + 1}
we get a standard Young tableau which encodes the initial conﬁguration of
the water.
As time goes by, at the time t2 the jeu de taquin was already applied
m2 := ⌊t2N2⌋
times and we investigate the tableau
T ′′
N = ∂∗m2(TN)

≤N2−m2 = ∂∗m2−m1(T ′
N)

≤N2−m2
with w2 + 1 boxes, where
(4.8)
w2 = N2 −m2 −1.
The boxes with the numbers 1, . . . , w2 correspond to the remaining particles
of water and the box with the maximal number w2 + 1 corresponds to the
surfer; the position of the latter box will be called the ﬁnal position of the
surfer.
Our aim is to relate the ﬁnal position of the surfer at the time t2 to its
initial position at the time t1, preferably in the language of the theoretical
longitude. As a point of reference we will introduce an additional multi-
surfer story which happens in a parallel universe in which we pay attention
to k surfers.
4.2. Pieri tableaux. We consider the partial order on the plane R2 deﬁned
by:
(x1, y1) ⪯(x2, y2) ⇐⇒(x1 ≤x2 ∧y1 ≥y2) .
Let k be a ﬁxed natural number and M be a tableau in which the k largest
entries are numbered by consecutive integers l + 1, . . . , l + k. We say that
the tableau M is a k-Pieri tableau if these k largest boxes are placed in
the increasing order with respect to ⪯(i.e., they are placed from north-west
to south-east) or, equivalently, their u-coordinates are ordered increasingly,
that is:
uM
l+1 < · · · < uM
l+k.
If the value of the number k is clear from the context, we will shortly say
that M is Pieri.
It is easy to check that if M has at least k + 1 boxes then M is a k-Pieri
tableau if and only if j(M) is a k-Pieri tableau.


## Page 29


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
29
For standard Young tableaux we will consider the following more general
notion. For a (skew) standard Young tableau T with n boxes and positive
integers w and k such that w+k ≤n we say that T is a (w+1, w+k)-Pieri
tableau if
(4.9)
uT
w+1 < · · · < uT
w+k.
The set of (w + 1, w + k)-Pieri standard tableaux of (skew) shape λ will be
denoted by eT (w+1,w+k)
λ
.
4.3. The multisurfer scenario. For the multisurfer scenario let k = k(N)
be a sequence of positive integers such that
(4.10)
lim
N→∞k = ∞
and
lim
N→∞
k2
N = 0.
For a ﬁxed value of N we consider the N ×N square pool ﬁlled with N2−k
particles of water on which k surfers (=k boxes with the biggest entries) are
positioned in the increasing order. Formally speaking, by
eT□N = eT (N2−k+1,N2)
□N
we denote the set of standard Young tableaux of the square shape □N which
are k-Pieri, and by ePN the uniform distribution on the set eT□N. We assume
that MN is a random tableau sampled with the uniform probability distribu-
tion ePN on the set eT□N In this scenario, in order to refer to the k surfers, we
will use the name multisurfers.
We start our analysis when jeu de taquin was already applied m1 + 1 −k
times with m1 given again by (4.4) (notice that m1 + 1 −k ≥0 for N big
enough). Our starting point is therefore the tableau
(4.11)
M′
N := ∂∗m1+1−k(MN)

≤N2−m1−1+k
with N2 −m1 −1 + k = w1 + k boxes. We will refer to this tableau as
the initial multisurfer conﬁguration. In this way, just as in the single surfer
scenario, the boxes with the numbers 1, . . . , w1 correspond to the water (in
particular, there is the same number of water particles as in the single surfer
scenario). On the other hand, the boxes with the numbers w1+1, . . . , w1+k
correspond to the multisurfers. By removing the multisurfers
(4.12)
f
W ′
N := M′
N \ {w1 + 1, . . . , w1 + k}
we get a standard Young tableau which encodes the initial conﬁguration of
the water.
As time goes by, at the time t2 the jeu de taquin was already applied
m2 + 1 −k times and we investigate the tableau
(4.13)
M′′
N = ∂∗m2+1−k(MN)

≤w2+k = ∂∗m2−m1(M′
N)

≤w2+k


## Page 30


30
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
which consists of w2 + k boxes which correspond to w2 particles of wa-
ter and k multisurfers; we will refer to this tableau as the ﬁnal multisurfer
conﬁguration.
4.4. Sketch of the proof of the upper bound (4.2).
4.4.1. The collective behavior of the multisurfers is not very random. Since
the number of the multisurfers is small in comparison to the number of
the rows/columns, as a ﬁrst-order approximation we may treat the set of
positions of k multisurfers at any ﬁxed time as a collection of k independent
copies of the position of a single surfer. We can expect therefore that the law
of large numbers is applicable and, as k →∞, the multisurfer empirical
measure (which is a random measure which encodes the scaled down u-
coordinates of the multisurfers) converges in probability to the probability
distribution of the position of the single surfer. In other words: the collective
behavior of the multisurfers is much less random than the behaviour of the
single surfer. This phenomenon is beneﬁcial and will allow us to use the
multisurfers as a moving frame of reference for tracing the position of the
single surfer over time.
The above naive ﬁrst-order approximation clearly cannot be true if k = k(N)
grows too fast with the size N of the square. Nevertheless, in Theorem 6.2
we will show that if k = k(N) grows at the right speed then a version of the
law of large numbers indeed holds true. The proof of Theorem 6.2 is quite
technically involved and the whole Section 6 is devoted to its proof.
4.4.2. The multisurfers provide information about the surfer. Let us ﬁx
some common initial conﬁguration of the water for both the surfer and the
multisurfers. In another ﬁrst-order approximation let us assume for a mo-
ment that the density of the multisurfers is small enough that during the
time interval [t1, t2] all neighboring pairs of multisurfers are separated so
that the multisurfers do not touch each other. If this is indeed the case and
there are no interferences between the multisurfers then the time evolution
of each multisurfer clearly coincides with the time evolution of the single
surfer who would have the same initial position; by reversing the optics
this means that we have a very direct information about some speciﬁc sin-
gle surfer trajectories (namely, the ones which start from the positions of
the multisurfers) in terms of the dynamics of the multisurfers, which we
understand pretty well thanks to the aforementioned Theorem 6.2.
It is very convenient that for a ﬁxed initial conﬁguration of the water, the
trajectory of the single surfer depends in a monotonic way on the initial
position of the surfer. For this reason it is possible to get some partial
information also about the single surfer trajectories starting from the points
between the initial positions of two multisurfers. If the number k = k(N) of


## Page 31


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
31
the multisurfers tends to inﬁnity as N →∞such neighboring multisurfers
should not be too far (in comparison to the size N of the square) which is
enough to prove Theorem 4.1.
4.4.3. The single surfer and the multisurfer scenario on the same water
conﬁguration. Above we used the idea of considering the single surfer sce-
nario and the multisurfer scenario on the same conﬁguration of water. This
idea sounds self-contradictory because each of these two scenarios gives
rise to a different probability distribution on the set of conﬁgurations of the
water. In Section 5 we shall explain how to overcome this difﬁculty and to
(asymptotically) couple the surfer and the multisurfers on a single probabil-
ity space. The resulting object can be visualized as water on which in two
parallel universes there is (i) a single surfer, and (ii) k multisurfers. The
single surfer and the multisurfers are like ghosts to one another and do not
interact. Furthermore, as long as the multisurfers do not touch each other,
the relative position (with respect to the partial order ≺on the plane) of the
surfer and the ghosts of the multisurfers does not change over time: over-
taking of the surfer by the multisurfers is not allowed.
4.4.4. Overtaking is allowed in one direction only. The above discussion
was based on a simplistic assumption that the multisurfers do not touch each
other. Regretfully, in the real world this is not the case; multisurfers might
inﬂuence each other and hence the multisurfer trajectories might differ from
the single surfer trajectories on the same conﬁguration of the water.
On the bright side, the assumption that the multisurfers are ordered as in
the deﬁnition of the Pieri tableaux implies that the movement of each mul-
tisurfer depends only on (1) the conﬁguration of the water, and (2) on these
multisurfers which are to the north-west; the other multisurfers which are
south-east have no inﬂuence on its dynamics. Furthermore, the impact of
the multisurfers is unidirectional: the presence of the north-west multisurfer-
neighbor can only push the multisurfer in the south-east direction. For the
‘coupling’ of the stories of the single surfer and the multisurfers on the com-
mon water this means that the ghosts of the multisurfers are allowed to
overtake the surfer, but only in one direction. More precisely, the number
of the multisurfers which are north-west to the single surfer can only de-
crease over time (see Lemma 7.1 for the formal description of the above
heuristics).
4.4.5. The order in which the proof of the upper bound (4.2) will be con-
ducted. The rigorous proof of (4.2) will be conducted in the following or-
der. First in Section 5 we will develop the content of Section 4.4.3. Then
in Section 6 we will deal with the collective behavior of the multisurfers
described in Section 4.4.1. In Section 7.1 we will work out the dynamics


## Page 32


32
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
contained in Section 4.4.4. Finally, in the rest of Section 7 we will formally
justify the heuristics from Section 4.4.2 and complete the proof.
5. SINGLE SURFER VERSUS THE MULTISURFER SCENARIO
In Sections 4.1 and 4.3 we considered two random tableaux: T ′
N and M′
N
deﬁned on two different probability spaces (which correspond to the single
surfer and the multisurfer scenario respectively). In order to proceed with
the ideas sketched in Section 4.4.3 we need to deﬁne some random tableaux
T′
N and M′
N on a common probability space with (almost) the same distri-
butions as T ′
N and M′
N and such that the corresponding conﬁgurations of
water coincide. A solution to this problem is provided by Proposition 5.1
below which is also the main result of the current section. We will compare
the distributions with respect to the total variation distance.
Suppose that X and Y are random variables (possibly deﬁned on differ-
ent probability spaces) taking values in some ﬁnite set S with probability
distributions PX and PY respectively. We deﬁne the total variation distance
between the random variables X and Y [Dur10, Section 3.6.1] (or, alterna-
tively, between the probability distributions PX and PY ) as
(5.1)
δ(X, Y ) = δ(PX, PY ) :=
1
2
X
s∈S
PX(s) −PY (s)
 = max
Z⊂S
PX(Z) −PY (Z)
 .
Sometimes we will also denote this quantity by δ(X, PY ), etc.
Proposition 5.1. For each C ≥1 and ∆∈(0, 1) there exists a con-
stant d > 0 with the following property.
Let λ be a C-balanced Young diagram and let k, w, a be positive integers
such that w < (1 −∆) |λ| and w ≤a ≤|λ| −k.
Then there exists a pair of random tableaux T and M which are deﬁned
on the same probability space with the following properties:
(a) T is a uniformly random element of Tλ;
(b) M is a random element of eT (a+1,a+k)
λ
;
(c) the total variation distance between the distribution of M and the uni-
form distribution on eT (a+1,a+k)
λ
fulﬁlls the bound
(5.2)
δ

M, P eT (a+1,a+k)
λ

< d
k2
p
|λ| −w
;
(d) T

≤w = M

≤w holds true almost surely.


## Page 33


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
33
The proof is postponed to Section 5.3. In the next two subsections we
prepare to it by proving general lemmas on the probabilities of some par-
ticular events in the multisurfers scenario (Section 5.1) and comparing the
distributions of water beneath surfer(s) in both scenarios (Section 5.2). It
turns out that these distributions are similar in terms of the total variation
distance which asymptotically converges to 0, see Lemma 5.4.
5.1. Probability that a random tableau is Pieri.
Lemma 5.2. Let λ/µ be a skew Young diagram with n boxes and let 1 ≤k ≤n.
Then the cardinality of the set
(5.3)
eT (w+1,w+k)
λ/µ
for w ∈{0, . . . , n −k}
does not depend on the choice of w.
Proof. There is a simple bijection between the set eT (w+1,w+k)
λ/µ
and the set
of semistandard skew tableaux of shape λ/µ and of weight (1w, k, 1n−w−k)
which is deﬁned as follows. For a tableau T ∈eT (w+1,w+k)
λ/µ
we replace each
entry from the set {w + 1, . . . , w + k} by the same number w + 1, and we
replace each entry i ∈{w + k + 1, . . . , n} by i + 1 −k. It follows therefore
that the cardinality of (5.3) is equal to the coefﬁcient
h
x1 · · ·xwxk
w+1xw+2 · · · xn+1−k
i
sλ/µ
in the expansion of the skew Schur function in the basis of monomials.
Since the skew Schur function is a symmetric polynomial, the proof is com-
pleted.
□
Some notions deﬁned for ordinary Young diagrams have their natural
counterparts in the skew setup, given as follows. For C ≥1 we say that a
skew Young diagram λ/µ is C-balanced if λ/µ has at most C
p
|λ/µ| rows
and at most C
p
|λ/µ| columns. Moreover we denote by Pλ/µ the uniform
measure on the set of standard Young tableaux of skew shape λ/µ.
We calculate now the probability of choosing a Pieri tableau from the set
of standard Young tableaux of a speciﬁed skew shape.
Lemma 5.3. For each C ≥1 there exists a constant c > 0 with the follow-
ing property. Let λ/µ be a C-balanced skew Young diagram with n boxes.
Let k and w be integers such that 1 ≤k <
4√n and 0 ≤w ≤n −k. Then
(5.4)
k! Pλ/µ

eT (w+1,w+k)
λ/µ

−1
 < c k2
√n.


## Page 34


34
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
Proof. Let T be a uniformly random standard tableau of skew shape λ/µ.
It is easy to check that T is (w + 1, w + k)-Pieri if and only if the rectiﬁed
tableau rect T is (w + 1, w + k)-Pieri (see Section 4.2 for the deﬁnition of
Pieri tableaux). In the following we will describe the probability distribu-
tion of rect T.
Recall that the plactic skew Schur polynomial Sλ/µ is the formal sum of
the elements in the plactic monoid which correspond to all semistandard
tableaux of shape λ/µ. The relations in the plactic monoid [Ful97, Sec-
tion 2, Corollary 1] allow us to identify a skew tableau with its rectiﬁcation
and to express the skew plactic Schur polynomial as a linear combination
of (non-skew) plactic Schur polynomials [Ful97, Section 5.1, Corollary 4]:
(5.5)
Sλ/µ
f λ/µ =
X
ν
cλ
µνf ν
f λ/µ · Sν
f ν ,
where cλ
µν is the Littlewood–Richardson coefﬁcient. If we restrict our atten-
tion only to the summands which correspond to (skew) standard tableaux,
the left-hand side can be identiﬁed with the probability distribution of rect T.
The right-hand can be interpreted as a linear combination (over some Young
diagrams ν) of the uniform measure on the set Tν.
In this way we proved that a random tableau with the same distribution
as rect T can be generated by the following two step procedure. Firstly, we
select a random Young diagram ν with the probability distribution
P(ν) = cλ
µνf ν
f λ/µ .
Secondly, we select a uniformly random standard tableau with the shape ν.
In particular, the probability that rect T is a (w+1, w+k)-Pieri tableau is
a weighted arithmetic mean (over certain diagrams ν) of the probability that
a uniformly random element of Tν is a (w+1, w+k)-Pieri tableau. It follows
that it is enough to prove a version of the inequality (5.4) in which the skew
diagram λ/µ is replaced by any diagram ν which contributes to (5.5); we
will do it in the following.
We start with an observation that in the process of rectiﬁcation the num-
ber of rows and the number of columns of a tableau cannot increase. Since
λ/µ is C-balanced, it follows that any Young diagram ν which contributes
to (5.5) is also C-balanced.
By Lemma 5.2 it is enough to consider the case w = 0. Let T be a
uniformly random standard tableau of shape ν and let ξ = sh T|≤k be the
positions of the ﬁrst k boxes of T. The tableau T is (1, k)-Pieri if and only
if ξ = (k) is the one-row diagram. The remaining difﬁculty is therefore to
identify the probability distribution of ξ.


## Page 35


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
35
The link between the combinatorics of standard Young tableaux and the
irreducible representations of the symmetric groups (in particular, the branch-
ing rule) implies that the probability distribution of ξ coincides with the
measure PVν↓Sk on the irreducible components of Vν↓Sk which was deﬁned
in (3.1). Equation (3.1) gives therefore an exact formula
(5.6)
k! P

T ∈eT (1,k)
ν

= k! PVν↓Sk(triv) = k!
D
χν↓Sk , χtriv
E
=
X
π∈Sk
χν(π) χtriv(π) = 1 +
X
π∈Sk
π̸=id
χν(π).
In the following we will ﬁnd an asymptotic bound for the second summand
on the right-hand side.
By Fact 3.1 there exists a universal constant a > 0 (which depends only
on C) such that for any π ∈Sk
(5.7)
χν(π)
 ≤
 a
√n
|π|
.
It follows that the second summand on the right-hand side of (5.6) is bounded
by

X
π∈Sk
π̸=id
χν(π)
 ≤
X
π∈Sk
 a
√n
|π|
−1 ≤e
ak2
√n −1 = O
 
k2
√n
!
,
where we used Lemma 3.3 and the assumption that k2
√n = O(1).
□
5.2. Comparison of distributions of water beneath surfer(s) in both sce-
narios. The following lemma shows that in the asymptotic setting the prob-
ability distributions of water beneath surfer(s) in the single surfer and the
multisurfer scenarios are nearly equal.
Lemma 5.4. For each C ≥1 and ∆∈(0, 1) there exists a constant d > 0
with the following property.
Let λ be a C-balanced Young diagram and k, w and a be positive inte-
gers such that w < (1 −∆) |λ| and w ≤a ≤|λ| −k. Denote by T
a uniformly random element of Tλ and by M a uniformly random element
of eT (a+1,a+k)
λ
. The total variation distance between the distributions of the
restricted tableaux T

≤w and M

≤w fulﬁlls the bound
(5.8)
δ

T

≤w, M

≤w

< d
k2
p
|λ| −w
.


## Page 36


36
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
Proof. We start with an observation that the total variation distance is triv-
ially bounded from above by 1. It follows that (provided d ≥1) it is enough
to consider the case when k4 ≤|λ| −w.
Notice that the probability distribution P eT (a+1,a+k)
λ
(·) coincides with the
conditional probability PTλ

·
 eT (a+1,a+k)
λ

. Therefore, for any µ ∈Yw
such that µ ⊆λ and any S ∈Tµ we have, by the Bayes rule, that
P eT (a+1,a+k)
λ

M

≤w = S

=
PTλ

M ∈eT (a+1,a+k)
λ
 M

≤w = S

PTλ

eT (a+1,a+k)
λ

· PTλ

M

≤w = S

.
By elementary algebra this equality can be rewritten as
(5.9)
P eT (a+1,a+k)
λ

M

≤w = S

−PTλ

M

≤w = S

=
= P eT (a+1,a+k)
λ

M

≤w = S

1 −k! PTλ

eT (a+1,a+k)
λ

+
+ PTλ

M

≤w = S
"
k! PTλ

M ∈eT (a+1,a+k)
λ
 M

≤w = S

−1
#
.
Our strategy is to ﬁnd an upper bound for the absolute value of the right-
hand side.
The conditional probability in the second summand on the right-hand
side, i.e.,
(5.10)
PTλ

M ∈eT (a+1,a+k)
λ
 M

≤w = S

,
is equal to the conditional probability that the restricted tableau M|>w is an
(a + 1, a + k)-Pieri tableau. In order to calculate this conditional probabil-
ity we notice that the conditional probability distribution of the restricted
tableau M|>w (under the condition M

≤w = S) is the uniform measure on
the set of tableaux of shape λ/µ such that their entries form the multiset
(w + 1, . . . , n). In other words, the probability distribution of the random
tableau
 M|>w

−w (which is obtained by decreasing each entry of M|>w
by w) is given by PTλ/µ. In this way we proved that (5.10) is equal to
(5.11)
PTλ/µ

eT (a+1−w,a+k−w)
λ/µ

.


## Page 37


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
37
By comparing the number of rows and columns, as well as the number of
boxes of the skew diagram λ/µ with their counterparts for λ it follows that
λ/µ is C′-balanced with
C′ = C
s
|λ|
|λ| −w <
C
√
∆
.
A fortiori λ and λ/µ are C′′-balanced, where C′′ is the right-hand side of
the above inequality.
We apply Lemma 5.3 twice: for both expressions in the square brack-
ets on the right-hand side of (5.9). It follows that there exists a universal
constant c > 0 (which depends only on C′′) such that
P eT (a+1,a+k)
λ

M

≤w = S

−PTλ

M

≤w = S
 ≤
≤P eT (a+1,a+k)
λ

M

≤w = S
 ck2
p
|λ|
+ PTλ

M

≤w = S

ck2
p
|λ| −w
.
By summing over all choices of S we get (5.8) for d := max(1, 2c), as
required.
□
5.3. Proof of Proposition 5.1.
Proof of Proposition 5.1. We will sample the random tableaux T and M by
the following two-step procedure. Firstly, we sample T with the uniform
probability measure on Tλ, that is P(T = T) := PTλ(T) for any T ∈Tλ.
After the tableau T was selected, we sample the tableau M with the condi-
tional probability
P

·
 T = T

:=
P eT (a+1,a+k)
λ

·

n
M ∈eT (a+1,a+k)
λ
: M|≤w = T|≤w
o
.
In this way the condition (d) is fulﬁlled trivially.
Therefore the probability distribution of M is given by
(5.12)
P (M = M) =
PTλ

T ∈Tλ : T|≤w = M|≤w
	
×
P eT (a+1,a+k)
λ

M

n
T ∈eT (a+1,a+k)
λ
: T|≤w = M|≤w
o
.


## Page 38


38
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
The probability measure P eT (a+1,a+k)
λ
can be written in an analogous way as
(5.13)
P eT (a+1,a+k)
λ
(M) =
P eT (a+1,a+k)
λ
n
T ∈eT (a+1,a+k)
λ
: T|≤w = M|≤w
o
×
P eT (a+1,a+k)
λ

M

n
T ∈eT (a+1,a+k)
λ
: T|≤w = M|≤w
o
.
It follows that the process of sampling M as well as the process of sampling
the uniformly random element of eT (a+1,a+k)
λ
can be viewed as a two-step
procedure: we ﬁrst sample the positions of the boxes 1, . . . , w and in the
second step the remaining boxes. Notice that in both sampling procedures
in the second step we sample the remaining boxes with the same condi-
tional distribution. It follows that the total variation distance between the
measures (5.12) and (5.13) is bounded from above by the total variation
distance (5.8) from Lemma 5.4 which completes the proof.
□
6. THE DISTRIBUTION OF THE u-COORDINATES OF
THE MULTISURFERS
Our main result in this section is Theorem 6.2 which shows that the
multisurfer empirical measure (i.e., the distribution of the u-coordinates of
the multisurfers) after draining a (1 −α)-fraction of the water converges to
the limit measure να (the limit distribution of the u-coordinate of the single
surfer on the level curve gα, cf. Section 2.3). Also Proposition 6.5 might be
interesting from the viewpoint of algebraic combinatorics as it provides a di-
rect link between the statistical properties of uniformly random (a, b)-Pieri
tableaux of some ﬁxed shape and the celebrated Jucys–Murphy elements.
The following assumption on the ‘amount of water’ and the number
of multisurfers will be central in the forthcoming results (Theorem 6.2
and Propositions 7.2 and 6.3).
Assumption 6.1. Let c > 0 be the constant in Lemma 5.3 obtained for
C = 1 for which (5.4) holds. We assume that k = k(N) and w = w(N) are
sequences of positive integers which fulﬁll
lim
N→∞k(N) = ∞
and
k <
r
N
2c
and
w + k < N2.
6.1. Counting multisurfers gives the longitude. Let w = w(N) and k =
k(N) be sequences of nonnegative integers such that 0 < w + k < N2.
Let MN be a uniformly random tableau from eT (w+1,w+k)
□N
. We use a short-
hand notation un := uMN
n
for the u-coordinate of the box with the number
n in the tableau MN. For u ∈R we deﬁne the random variable GN(u)


## Page 39


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
39
to be the fraction of the multisurfers which have their scaled u-coordinate
smaller than u, that is
(6.1)
GN(u) := 1
k max

p ∈{1, . . . , k} : 1
N uw+p ≤u

.
Clearly, GN is the cumulative distribution function of the random mea-
sure mN on R
mN := 1
k
X
1≤p≤k
δN−1 uw+p
where δx denotes the delta measure concentrated at x.
Theorem 6.2. Let α ∈(0, 1). Let w = w(N) and k = k(N) fulﬁll Assump-
tion 6.1 and
lim
N→∞
w
N2 = α.
Then for each ε > 0
P eT (w+1,w+k)
□N

MN : sup
u∈R
Fνα(x) −GN(x)
 > ε

= O
 
1
k + k2
N
!
with the constant in the O-notation depending only on α and ε.
In particular, if k(N) →∞and k(N) = o(
√
N), i.e., (4.10) is sat-
isﬁed, then the random sequence of cumulative distribution functions GN
with respect to the supremum norm converges in probability to the cumula-
tive distribution function Fνα when N →∞, that is shortly,
sup
x∈R
Fνα(x) −GN(x)
 P−→0.
In order to prove this result we will compare the (random) moments of the
empirical measure mN and the moments of the measure να which gives the
asymptotics of the u-coordinate of a single box, cf. Section 2.3. In Propo-
sition 6.3 below we shall calculate the moments of the empirical measure
mN. In Section 6.8 we will complete the proof of Theorem 6.2.
6.2. Moments of the empirical measure GN. For each β ∈N we deﬁne
the β-th moment of the random measure mN as
Mβ := Mβ(w, k) :=
Z
R
zβ dmN(z) = 1
kN−β X
1≤p≤k
uβ
w+p.
Notice that Mβ is also a random variable. The following result expresses
the ﬁrst two moments of the random variable Mβ(w, k) (which is related
to the problem of multisurfers) in terms of the ﬁrst moment of the random
variable Mβ(w, 1) (which is related to the much simpler problem of a single
surfer). This proposition is crucial to the proof of Theorem 6.2.


## Page 40


40
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
Proposition 6.3. Let w = w(N) and k = k(N) fulﬁll Assumption 6.1. For
each β ∈N, we have
EePNMβ(w, k) = EPNMβ(w, 1) + O
 
k2
N
!
;
(6.2)
VarePNMβ(w, k) = O
 
1
k + k2
N
!
(6.3)
with the constants in the O-notation depending only on β.
Remark 6.4. The counterpart of the above proposition in the paper of Romik
and the second named author is [R´S15, Theorem 4.6]. There the error terms
for the expected value and variance are much smaller, accordingly, O

k
N

and O

1
k + k
N

. There are two reasons for which our error terms are much
bigger, of the form, accordingly, O

k2
N

and O

1
k + k2
N

.
• In the proof of Proposition 6.5 we will view the probability distri-
bution of the multisurfers as a conditional distribution of the boxes
with certain numbers in a uniformly random standard skew tableau
with a speciﬁed shape under the condition that these boxes are suit-
ably ordered (i.e., the tableau is Pieri). Unfortunately, the probabil-
ity of the latter event depends heavily on the shape of the diagram
and we do not have a very good control over the error term, see
Lemma 5.3.
Using our terminology in their context, the placement of the mul-
tisurfers by Romik and the second named author can also be seen
as a conditional process: one ﬁrst adds k boxes to a given Young
diagram λ by k independent steps of the Plancherel growth process,
and then conditions that these boxes are suitably ordered. In this
case, however, the conditioning does not create additional difﬁcul-
ties because the probability of the event that the newly created boxes
are Pieri is equal to 1
k! and does not depend on the shape of λ.
• The error O

k2
N

also appears during the application of Proposi-
tion 6.9. Romik and the second named author make use of [R´S15,
Theorem 4.4] which is a counterpart of ours Proposition 6.5. They
deal with the character of the left-regular representation which ob-
viously is not troublesome and need not be estimated.
The proof of Proposition 6.3 is quite long. In Sections 6.3 to 6.5 we
gather some tools helpful in proving Proposition 6.3. In particular, the goal
of Section 6.3 is to provide a connection between the statistical properties


## Page 41


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
41
of the multisurfers and the representation theory (see Proposition 6.5). Sec-
tion 6.4 gives background for calculating the character χ□N of the cosets
appearing in (6.4). Section 6.5 is devoted mostly to an analysis of the per-
mutations arising from the powers of Jucys–Murphy elements. Eventually,
in Section 6.6 we give the proof of (6.2) and in Section 6.7 the proof of (6.3)
which completes the proof of Proposition 6.3.
6.3. Multisurfers and the representation theory. The following result,
Proposition 6.5, provides a link between the statistical properties of the mul-
tisurfers and the representation theory of the symmetric groups.
Let w, k, n be positive integers such that w+k ≤n. With a small abuse of
notation we denote by Sw the group of permutations of the set {1, . . . , w}
and by Sk the group of permutations of the set {w + 1, . . . , w + k}. In this
way Sw and Sk are commuting subgroups of Sw+k ⊂Sn. We deﬁne the
element of the symmetric group algebra
pSk = 1
k!
X
σ∈Sk
σ ∈CSn.
Recall from Section 3.4 that the Jucys–Murphy elements J1, . . . , Jn form
a commuting family in the symmetric group algebra CSn and are given by
Jk :=
X
1≤i<k
(i, k) = (1, k) + · · · + (k −1, k) ∈CSn
for 1 ≤k ≤n.
Proposition 6.5. Let w, k, n be positive integers such that w + k ≤n. Let
W(x1, . . . , xk) be a symmetric polynomial in k variables. Let λ ∈Yn
be a Young diagram and T be a random element (sampled with the uniform
distribution) of the set eT (w+1,w+k)
λ
of (w+1, w+k)-Pieri tableaux of shape λ.
Then
E W

uT
w+1, . . . , uT
w+k

=
χλ

W(Jw+1, . . . , Jw+k) · pSk

χλ
 pSk

(6.4)
=
χλ

W(Jw+1, . . . , Jw+k) · pSk

PTλ

eT (w+1,w+k)
λ

.
The proof is postponed until the end of the current section until we gather
the necessary tools.
We start with the following fundamental property of Jucys–Murphy ele-
ments.


## Page 42


42
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
Fact 6.6 ([Juc74]). Let λ ∈Yn be a Young diagram, and let u1, . . . , un be
the u-coordinates of its boxes (listed in an arbitrary order). Let W(x1, . . . , xn)
be a symmetric polynomial in n variables. Then:
• W(J1, . . . , Jn) ∈CSn belongs to the center of the group algebra.
• The operator ρλ
 W(J1, . . . , Jn)

is a multiple of the identity opera-
tor, so it can be identiﬁed with a complex number. The value of this
number is equal to
(6.5)
χλ

W(J1, . . . , Jn)

= W(u1, . . . , un).
Lemma 6.7. Let µ ∈Yw+k be a Young diagram and let W(x1, . . . , xk) be
a symmetric polynomial in k variables. Then the operator
ρµ
 W(Jw+1, . . . , Jw+k)

acts on each irreducible component Vν of the restriction Vµ
ySw+k
Sw
as a mul-
tiple of the identity operator and can be identiﬁed with the complex number
(6.6)
W

uµ/ν
w+1, . . . , uµ/ν
w+k

.
Above, for a diagram ν with w boxes such that ν ⊂µ we denote by uµ/ν
w+1, . . . , uµ/ν
w+k
the u-coordinates of the boxes of the skew diagram µ/ν (listed in an arbi-
trary order).
Proof. We will show that the lemma holds in the particular case when W is
the power-sum symmetric function, that is
W(x1, . . . , xk) := pβ(x1, . . . , xk) :=
X
1≤i≤k
xβ
i
for some β ∈N0. Since the power-sum symmetric functions generate the al-
gebra of the symmetric polynomials and the representation ρµ is an algebra
homomorphism, in this way we will prove that the lemma holds true in
general.
Clearly,
W(Jw+1, . . . , Jw+k) = pβ (Jw+1, . . . , Jw+k) =
= pβ (J1, . . . , Jw+k) −pβ (J1, . . . , Jw) .
By Fact 6.6, the operator pβ (J1, . . . , Jw+k) acts on the component Vµ as
multiplication by the factor
(6.7)
pβ
 uµ
1, . . . , uµ
w+k

=
X
1≤i≤w+k
 uµ
i
β .


## Page 43


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
43
Again by Fact 6.6, for any ν ∈Yw, the operator pβ (J1, . . . , Jw) acts on the
component Vν as multiplication by the factor
(6.8)
pβ (uν
1, . . . , uν
w) =
X
1≤i≤w
(uν
i )β .
Let ν ⊂µ. The multiset of the u-coordinates of the boxes of µ is the
union of (i) the multiset of the u-coordinates of the boxes of ν, and (ii) the
multiset of the u-coordinates of the boxes of µ/ν. Therefore, by subtracting
(6.8) from (6.7), we get that the operator pβ (Jw+1, . . . , Jw+k) acts on the
component Vν of the restriction Vµ ↓Sw+k
Sw
as multiplication by the scalar
pβ

uµ/ν
w+1, . . . , uµ/ν
w+k

=
X
1≤i≤k

uµ/µ
w+i
β
,
as required.
□
Proof of Proposition 6.5. Observe that any tableau T ∈eT (w+1,w+k)
λ
can be
split into the following three parts: (i) a standard tableau P with entries
from {1, . . . , w}; we denote its shape by ν, (ii) a skew tableau Q which is
k-Pieri with entries in {w + 1, . . . , w + k}; we denote its shape by µ/ν, and
(iii) a skew tableau R with the entries > w + k with shape λ/µ.
For ﬁxed partitions µ and ν it is easy to count the number of tableaux P
which contribute to (i) and the number of tableaux R which contribute
to (iii): their cardinalities are by deﬁnition given by f ν and f λ/µ respec-
tively.
The number of k-Pieri tableaux Q which contribute to (ii) is slightly more
challenging: it is equal to 1 if µ/ν has at most one box in each column and
is equal to zero otherwise. A combinatorial interpretation of the Littlewood–
Richardson coefﬁcient cµ
ν,(k) for a single-row partition (k) (or, nomen omen,
the Pieri rule) implies that this coefﬁcient coincides with the latter cardinal-
ity.
In this way we proved that the left-hand side of (6.4) is given by
(6.9)
E W

uT
w+1, . . . , uT
w+k

=
1
eT (w+1,w+k)
λ

X
T∈eT (w+1,w+k)
λ
W

uT
w+1, . . . , uT
w+k

=
1
eT (w+1,w+k)
λ

X
µ∈Yw+k
µ⊂λ
X
ν∈Yw
ν⊂µ
f λ/µ f ν cµ
ν,(k) W

uµ/ν
w+1, . . . , uµ/ν
w+k

.
We will now investigate the numerator on the right hand side of (6.4).
Each multiplicity f λ/µ in the decomposition of the restriction of Vλ into


## Page 44


44
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
irreducible components
Vλ
ySN2
Sw+k =
M
µ∈Yw
µ⊂λ
f λ/µVµ
is equal to the number of skew standard Young tableaux of shape λ/µ. Since
W(Jw+1, . . . , Jw+k) · pSk ∈CSw+k, we get that
(6.10)
Cλ := χλ

W (Jw+1, . . . , Jw+k) · pSk

=
1
dim Vλ
TrVλ ρλ

W (Jw+1, . . . , Jw+k) · pSk

=
= 1
f λ
X
µ∈Yw+k
µ⊂λ
f λ/µ TrVµ ρλ

W (Jw+1, . . . , Jw+k) · pSk

.
The multiplicities in the decomposition of the restricted representation
into irreducible components
Vµ
ySw+k
Sw×Sk =
M
ν∈Yw
ξ∈Yk
cµ
ν,ξVν ⊗Vξ
are given by Littlewood–Richardson coefﬁcients. Therefore, since pSk is
a projection to the trivial representation, its image is given by
(6.11)
pSk
 Vµ

= pSk

Vµ
ySw+k
Sw×Sk

=
M
ν∈Yw
cµ
ν,(k)Vν ⊗V(k) =
M
ν∈Yw
cµ
ν,(k)Vν.
By combining (6.10), (6.11), and Lemma 6.7 we get the following closed
formula for the numerator on the right-hand side of (6.4)
(6.12)
Cλ = 1
f λ
X
µ∈Yw+k
µ⊂λ
X
ν∈Yw
f λ/µ cµ
ν,(k) f ν W

uµ/ν
w+1, . . . , uµ/ν
w+k

.
On the other hand, by (6.12) evaluated for the constant polynomial W ≡
1, we get the following formula for the denominator on the right-hand side
of (6.4)
(6.13)
χλ
 pSk

= 1
f λ
X
µ∈Yw+k
µ⊂λ
X
ν∈Yw
f λ/µcµ
ν,(k)f ν = 1
f λ ·
eT (w+1,w+k)
λ


## Page 45


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
45
where the last equality comes from (6.9) evaluated for W ≡1. Observe
also that
(6.14)
PTλ

eT (w+1,w+k)
λ

=
f λ
eT (w+1,w+k)
λ

.
Equations (6.9), (6.12), (6.13) and (6.14) complete the proof of (6.4).
□
6.4. Character on a coset. Let us call small the elements of the set {1, . . . , w}
and big the elements of the set {w + 1, . . . , w + k}. As before, we view
the symmetric group Sk as the subgroup of Sw+k which consists of the
permutations which can permute only the big elements.
For a Young diagram λ ∈Yn and a permutation π ∈Sw+k we deﬁne the
value of the character χλ on a left coset πSk ∈Sw+k/Sk as an appropriate
sum over the coset, that is
χλ(πSk) :=
X
σ∈πSk
χλ(σ).
This deﬁnition is motivated by Proposition 6.5 because expressions of a
similar ﬂavor (up to the factor
1
k!) appear on the right-hand side of (6.4).
Our goal in this section is to understand the asymptotics of such characters
on cosets.
For a left coset πSk ∈Sw+k/Sk we deﬁne its length as
(6.15)
∥πSk∥:= w −#(cycles of π which consist of only small elements).
It is easy to check that if π1Sk = π2Sk then the cycles of π1 which consist
of only small elements coincide with the analogous cycles of π2; it follows
that the above deﬁnition does not depend on the choice of the representa-
tive π of the coset.
Remind that for a permutation π we denote by |π| the length of π, i.e., the
minimal number of transpositions required to write π as their product.
Lemma 6.8. For each left coset πSk
(6.16)
∥πSk∥= min

|σ| : σ ∈πSk
	
.
There exists a unique permutation π0 ∈πSk for which the minimum on
the right-hand side is achieved; the permutation π0 = π0(πSk) with this
property will be called minimal for the coset πSk.
This minimal permutation has the following additional properties:
(a) for each σ ∈Sk,
(6.17)
|π0σ| = ∥πSk∥+ |σ| .


## Page 46


46
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
(b) If π is such that each of its cycles permutes at most one big element,
then π = π0 is the minimal element.
Proof. We begin with the proof of the ﬁrst assertion of the lemma. The per-
mutation π can be written as a product of disjoint cycles π = π1 · · · πℓπℓ+1 · · · πL,
where π1, . . . , πℓare the cycles which permute at least one big element, and
πℓ+1, . . . , πL permute only small elements.
Fix i ∈{1, . . . , ℓ}. Then πi is a cycle of the form
πi =
 p1,1, . . . , p1,r1, q1,
p2,1, . . . , p2,r2, q2,
. . . ,
pn,1, . . . , pn,rn, qn

,
for some n ∈N and r1, . . . , rn ∈N0, some big numbers q1, . . . , qn and
some small numbers pr,s. Deﬁne
τi := (qn, qn−1, . . . , q1) ∈Sk
as the cycle permuting (in the reverse direction) the big elements of the
cycle πi. Clearly,
πiτi =
 p1,1, . . . , p1,r1, q1

· · ·
 pn,1, . . . , pn,rn, qn

gives a product of disjoint cycles, each permuting exactly one big element.
Then
(6.18)
π0 := (π1τ1) · · · (πℓτℓ) πℓ+1 · · · πL ∈πSk
provides a decomposition into disjoint cycles which has the property that
each cycle permutes at most one big element. Hence for any σ ∈Sk which
permutes only big elements, the decomposition into disjoint cycles of the
product π0σ ∈πSk is obtained by merging appropriate cycles of π0, it
follows therefore that
(6.19)
|π0σ| = |π0| + |σ| .
As a consequence, the minimum on the right-hand side of (6.16) is achieved
on π0 and it is the unique permutation with this property, as required.
We shall now show that the equality (6.16) holds true. It is enough to
prove it in the special case when as the coset representative we take π0
given by (6.18). In this special case (6.16) is equivalent to
(6.20)
∥π0Sk∥= |π0| .
The explicit decomposition into disjoint cycles (6.18) implies that the
left-hand side is equal to
w −(L −ℓ).


## Page 47


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
47
On the other hand, (6.18) implies that π0 has exactly L −ℓcycles which
permute only small elements and k additional cycles, one for each big ele-
ment. It follows that the right-hand side of (6.20) is equal to
|π0| = (w + k) −
 L −ℓ+ k

= w −(L −ℓ)
which concludes the proof of (6.16).
Property (a) is now a direct consequence of (6.19) and (6.20).
For the proof of property (b), if π is such that each of its cycles permutes
at most one big element then our construction gives π = π0 so π is the
minimal representative of the coset.
□
The next proposition gives an insight to the irreducible characters corre-
sponding to square diagrams evaluated on left cosets.
Proposition 6.9. For each positive integer L there exists a constant CL with
the following property.
Let positive integers w and k be arbitrary and let π0 ∈πSk be the min-
imal representative of a left coset πSk ∈Sw+k/Sk. If ∥πSk∥≤L and
N2 ≥w + k and N > k2 then
χ□N (πSk) −χ□N (π0)
 <
CLk2
N∥πSk∥+1,
(6.21)
χ□N (πSk)
 <
2CL
N∥πSk∥.
(6.22)
Proof. Let d = d(L) ≥1 be a constant (which depends only on L) big
enough so that it guarantees that
L + k ≤dN.
By Fact 3.1, Lemma 6.8(a) and Lemma 3.3 we have
χ□N (πSk) −χ□N (π0)
 ≤
X
σ∈Sk
σ̸=id
χ□N (π0σ)
 ≤
X
σ∈Sk
σ̸=id
ad
N
|π0σ|
≤
ad
N
∥πSk∥

exp
 
adk2
2N
!
−1

=
(ad)∥πSk∥+1
2
k2
N∥πSk∥+1
exp

adk2
2N

−1
adk2
2N
.
Since ex−1
x
is a bounded function on the interval

0, ad
2
i
, we get (6.21) as
required.


## Page 48


48
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
By (6.21) and Fact 3.1 we get
χ□N (πSk)
 <
CLk2
N∥πSk∥+1 +
ad
N
|π0|
=
1
N∥πSk∥
 
CL
k2
N + (ad)∥πSk∥
!
.
It follows that we can increase the value of the constant CL in such a way
that both (6.21) and (6.22) are fulﬁlled.
□
6.5. Products of Jucys–Murphy elements.
6.5.1. Set partitions. For calculations of the moments (6.2) and (6.3) we
will need to better understand the sum of products Pk
p=1 Jβ
w+p. We will use
similar concepts and notions to the ones from [R´S15, Section 4.9]. Notice
that
(6.23)
Jβ
w+p =
X
1≤j1,...,jβ≤w+p−1
(j1, w + p) · · ·(jβ, w + p).
We denote the summands contributing to the right-hand side of (6.23) in
the following way. For any p and a sequence j = (j1, . . . , jβ) ∈[w+p−1]β
deﬁne
(6.24)
σp,j := (j1, w + p) · · ·(jβ, w + p).
We also denote
ZΣ(j) :=

r ∈{1, . . . , β} : jr ≤w
	
;
ZΠ(j) :=

r ∈{1, . . . , β} : jr > w
	
.
The sets ZΣ(j) and ZΠ(j) indicate which elements of the sequence j are,
respectively, small and big. Notice that ZΣ ∪ZΠ = {1, . . . , β} and, since
ZΣ(j) and ZΠ(j) are disjoint,
ZΣ(j)
 +
ZΠ(j)
 = β.
We consider the equivalence relation ∼on ZΣ(j) (respectively, on ZΠ(j))
given by
m ∼n ⇐⇒jm = jn.
We denote by Σ(j) and Π(j) the sets of the equivalence classes of the rela-
tion ∼on, respectively, ZΣ(j) and ZΠ(j). Then the numbers of the equiva-
lence classes Σ(j)
 =
{j1, . . . , jβ} ∩{1, . . . , w}
 ,
Π(j)
 =
{j1, . . . , jβ} ∩{w + 1, . . . , w + k}

indicate how many different small / big elements appear in the sequence j.
We say that A is a set a set-partition of X, and denote it by A ∈SPar(X),
if A is a collection of disjoint non-empty subsets of X such that S A = X.


## Page 49


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
49
We call (A, B) a pair of complementary set-partitions of X if A ∪B is a
set-partition of X such that
[
A

∩
[
B

= ∅.
This terminology may be a bit misleading since neither A nor B need to be
a set-partition of X. Note also that we allow the situations when A = ∅or
B = ∅. For example, consider a sequence j ∈[w + p −1]β, then the pair
 Σ(j), Π(j)

is a pair of complementary set-partitions of [β].
For a pair (Σ, Π) of complementary set-partitions of [β] we will say that
the sequence j ∈[w + p −1]β is of type (Σ, Π) if Σ = Σ(j) and Π = Π(j).
If this is the case, we will use a shorthand notation j ∈(Σ, Π).
Lemma 6.10. Let p1, p2 ∈{1, . . . , k} and s ∈[w + p1 −1]β, and t ∈
[w +p2 −1]β. Suppose that s and t are of the same type. Denote σ1 := σp1,s
and σ2 := σp2,t. Then
(a) There exists a permutation g ∈Sw × Sk such that g(w + p1) =
w + p2 and g(sm) = tm for m ∈{1, . . . , β};
(b) Permutations σ1 and σ2 are conjugate by g, that is σ1 = g−1σ2g;
(c) ∥σ1Sk∥= ∥σ2Sk∥.
Proof. Denote
A≤w := [w] \ {sm : m = 1, . . . , β};
B≤w := [w] \ {tm : m = 1, . . . , β}.
Since Σ(s) = Σ(t), we have
A≤w
 =
B≤w
, so there exists a bijection
δ1: A≤w →B≤w. For the same reason, there exists a bijection δ2: A>w →
B>w between analogously deﬁned sets
A>w := {w + 1, . . . , w + k} \
 {sm : m = 1, . . . , β} ∪{w + p1}

;
B>w := {w + 1, . . . , w + k} \
 {tm : m = 1, . . . , β} ∪{w + p2}

.
Then g : Sw+k →Sw+k given by
g(x) :=







w + p2
if x = w + p1,
tm
if x = sm for some m ∈{1, . . . , β},
δ1(x)
if x ∈A≤w,
δ2(x)
if x ∈A>w.
clearly fulﬁlls the properties required in (a) and it is easy to check that (b)
indeed holds true.
In order to prove (c) it is enough to notice that (b) implies that σ1 and σ2
have the same number of cycles permuting only small elements.
□


## Page 50


50
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
6.5.2. Inequalities concerning the character of Jβ
w+p. In the proof of Propo-
sition 6.3 we will deal with the numbers of the form O(Nx) where the ex-
ponent is given by the right-hand-side of (6.25). Our next aim is to show
that these exponents are always nonpositive and only in some special cases
are equal to 0.
Lemma 6.11. Let x1, x2, . . . ∈{1, . . . , w + k} and y1, y2, . . . ∈{w +
1, . . . , w + k} be inﬁnite sequences. Deﬁne a function f : N0 →Z by
(6.25)
f(ℓ) := 2#
 {x1, . . . , xℓ} ∩{1, . . . , w}

+
#
 {x1, . . . , xℓ} ∩{w + 1, . . . , w + k}

−
∥(x1, y1) · · ·(xℓ, yℓ)Sk∥−ℓ.
Then f ≤0 and f is weakly decreasing.
Moreover, suppose that ℓ∈N is such that xℓ+1 ∈{x1, . . . , xℓ} and xℓ+1
and yℓ+1 belong to different cycles in the cycle decomposition of the product
(x1, y1) · · ·(xℓ, yℓ). Then f(ℓ+ 1) < f(ℓ) and, in particular, f(n) < 0 for
all n ≥ℓ+ 1.
Proof. Let ℓbe a non-negative integer; we will show that f(ℓ+ 1) ≤f(ℓ).
Consider ﬁrst the case xℓ+1 > w. Then
(x1, y1) · · ·(xℓ+1, yℓ+1)Sk = (x1, y1) · · · (xℓ, yℓ)Sk
so
(6.26)
f(ℓ+ 1) =
(
f(ℓ) −1
if xℓ+1 ∈{xi : i ≤ℓ},
f(ℓ)
otherwise,
thus f(ℓ+ 1) ≤f(ℓ), as required.
Assume now that xℓ+1 ≤w. Our strategy is to compare the cycle decom-
position of the products
(6.27)
(x1, y1) · · ·(xℓ, yℓ)
and
(x1, y1) · · · (xℓ+1, yℓ+1)
and to deduce in this way (via the deﬁnition (6.15)) the relationship between
the coset lengths
∥(x1, y1) · · ·(xℓ+1, yℓ+1)Sk∥
and
∥(x1, y1) · · · (xℓ, yℓ)Sk∥.
Consider the following two cases.
• Suppose xℓ+1 /∈{xi : i ≤ℓ}. Then the cycle decomposition of the
permutation on the right-hand side of (6.27) arises from its coun-
terpart on the left-hand side by merging the ﬁxpoint xℓ+1 with the
cycle which contains yℓ+1. It follows that
∥(x1, y1) · · ·(xℓ+1, yℓ+1)Sk∥= ∥(x1, y1) · · ·(xℓ, yℓ)Sk∥+ 1


## Page 51


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
51
hence f(ℓ+ 1) = f(ℓ), as required.
• Suppose xℓ+1 ∈{xi : i ≤ℓ}. The cycle decomposition of the
right-hand side of (6.27) is obtained from its counterpart on the left-
hand side either by merging two cycles or by splitting one cycle into
two cycles. Each of these two operations can change the number of
cycles which permute only small elements by at most 1. It follows
that
∥(x1, y1) · · · (xℓ+1, yℓ+1)Sk∥≥∥(x1, y1) · · ·(xℓ, yℓ)Sk∥−1
so f(ℓ+ 1) ≤f(ℓ), as required.
This completes the proof that f is weakly decreasing.
Since f(0) = 0 it follows that f ≤0 and the proof of the ﬁrst part of the
lemma is complete.
We will prove the second part of the lemma by revisiting the above proof.
If xℓ+1 > w then by (6.26), f(ℓ) = f(ℓ−1) −1, as required.
On the other hand, when xℓ+1 ≤w the cycle decomposition of the right-
hand side of (6.27) is obtained from its counterpart on the left-hand side by
merging two cycles: the one containing xℓ+1 with the one containing yℓ+1.
Therefore the number of cycles which consist of only small elements at the
right-hand side of (6.27) is bounded from above by its counterpart for the
left-hand side of (6.27). Hence
∥(x1, y1) · · · (xℓ+1, yℓ+1)Sk∥≥∥(x1, y1) · · ·(xℓ, yℓ)Sk∥
and so f(ℓ+ 1) ≤f(ℓ) −1, as required.
□
Corollary 6.12. Let x1, . . . , xℓ∈{1, . . . , w + k} and y1, . . . , yℓ∈{w +
1, . . . , w + k}. Denote
|Σ| := #
 {x1, . . . , xℓ} ∩{1, . . . , w}

;
|Π| := #
 {x1, . . . , xℓ} ∩{w + 1, . . . , w + k}

;
∥σSk∥:= ∥(x1, y1) · · ·(xℓ, yℓ)Sk∥.
Then for N ≥1
N2 |Σ| k|Π| N−∥σSk∥−ℓ≤
 k
N
|Π|
.
6.6. The mean value of Mβ – the proof of (6.2).


## Page 52


52
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
Proof of (6.2). Our goal is to calculate the expected value of the moment
Mβ(w, k) (recall Section 6.2). By Proposition 6.5,
(6.28)
EePNMβ (w, k) =
1
PN

eT (w+1,w+k)
□N
 · 1
kN−βχ□N
 J pSk

=
=
1
k! PN

eT (w+1,w+k)
□N
 · 1
kN−βχ□N (J Sk)
where (recall the deﬁnition (6.24) of σp,j)
J :=
k
X
p=1
Jβ
w+p =
k
X
p=1
X
j∈[w+p−1]β
σp,j ∈CSw+k.
Since □N is C-balanced with C = 1, by Lemma 5.3 the denominator on
the right-hand side of (6.28) fulﬁlls
k! PN

eT (w+1,w+k)
□N

= 1 + O
 
k2
N
!
with the constant in the O-notation equal to c from Lemma 5.3. By Assump-
tion 6.1 the right hand side is separated from 0 and therefore
(6.29)
1
k! PN

eT (w+1,w+k)
□N
 = 1 + O
 
k2
N
!
.
Equation (6.32) from Proposition 6.13 below provides the necessary asymp-
totics of the numerator and completes the proof of (6.2).
□
We consider an analogue of J in which each summand is replaced by the
minimal element of the appropriate coset
J0 := π0 (J ) =
k
X
p=1
X
j∈[w+p−1]β
π0
 σp,j

∈CSw+k.
The following proposition provides the missing element of the above proof
of (6.2).


## Page 53


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
53
Proposition 6.13. Let β ∈N be ﬁxed. Let k, N ∈N be such that N2 > w + k
and k2 < N. Then
χ□N (J0) = kNβ
"
EPNMβ(w, 1) + O
 k
N
#
;
(6.30)
χ□N (J Sk) = χ□N (J0) + O
 
kNβ k2
N
!
;
(6.31)
χ□N (J Sk) = kNβ

EPNMβ(w, 1) + O
 
k2
N
!

(6.32)
with the constants in the O-notation depending only on β.
The remaining part of this section is devoted to its proof.
6.6.1. Decomposition of χ□N (J0). Denote
A :=
k
X
p=1
X
j∈[w]β
χ□N

π0
 σp,j

;
and for a pair of complementary set-partitions (Σ, Π) of [β] let us also de-
note
B(Σ,Π) :=
k
X
p=1
X
j∈(Σ,Π)
χ□N

π0
 σp,j

.
(6.33)
With these notations
(6.34)
χ□N (J0) = A +
X
(Σ,Π)
Π̸=∅
B(Σ,Π).
Notice that the number of summands is ﬁnite, depends only on β and does
not depend on N or k. Therefore, it is enough to ﬁnd the asymptotics for
each individual summand on the right-hand side.
6.6.2. Asymptotics of A. By Lemma 6.8(b), π0
 σp,j

= σp,j for all j ∈
[w]β. Since the character is constant on each conjugacy class, the contribu-
tion of the summands in A to the character is the same for each value of p
and
A =
k
X
p=1
χ□N

X
j∈[w]β
σp,j

= k · χ□N

Jβ
w+1

.


## Page 54


54
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
We apply Proposition 6.5 for k = 1; in this special case pS1 = id and
χ□N (pS1) = 1, thus
(6.35)
A = k EPNuβ
w+1 = kNβ EPNMβ(w, 1).
6.6.3. Asymptotics of B(Σ,Π). Let j ∈[w + p −1]β. By Lemma 6.8 the
coset length
∥σp,jSk∥≤∥σp,j∥≤β
is uniformly bounded from above by the number of factors in (6.24). By Fact 3.1
and Lemma 6.8 it follows that there exists a universal constant Cβ such that
χ□N

π0
 σp,j
 ≤CβN−∥σp,jSk∥
holds true for each j ∈[w + p −1]β.
Let us ﬁx a pair (Σ, Π) of complementary set-partitions of [β]. The num-
ber of the summands on the right-hand side of (6.33) is equal to the follow-
ing sum of falling factorials
k
X
p=1
(w)|Σ| · (p)|Π| ≤N2|Σ| k|Π|+1.
By combining these observations with Corollary 6.12 we conclude that
(6.36)
B(Σ,Π) ≤CβN−∥σp,jSk∥· N2|Σ| k|Π|+1 ≤Cβ kNβ
 k
N
|Π|
.
The last two arguments imply also that for any p ∈{1, . . . , k}
(6.37)
X
j∈(Σ,Π)
k2
N∥σp,jSk∥+1 ≤k2
N Nβ
 k
N
|Π|
.
6.6.4. Proof of Proposition 6.13.
Proof of Proposition 6.13. The asymptotics of the summands which con-
tribute to the right-hand side of (6.34) is provided by the equality (6.35)
and the estimate (6.36) (for pairs (Σ, Π) of complementary set-partitions of
[β] with Π ̸= ∅). In this way the proof of (6.30) is complete.
By Proposition 6.9 there exists Hβ > 0 such that
(6.38)
χ□N (J Sk) −χ□N (J0)
 ≤Hβ
k
X
p=1
X
j∈[w+p−1]β
k2
N∥σp,jSk∥+1.
The summands on the right-hand side can be grouped according to the type
(Σ, Π) of the sequence j. For a ﬁxed value of β there are only ﬁnitely many
possible types, and the total contribution of the sequences j of a speciﬁc


## Page 55


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
55
type (Σ, Π) is bounded from above by (6.37) which completes the proof of
(6.31).
Equation (6.32) is a direct consequence of (6.30) and (6.31).
□
6.7. The variance of Mβ – the proof of (6.3). We will mimic the concepts
from Section 6.6, however, the calculations will be more involved.
Proof of (6.3). We ﬁrst calculate the second moment of Mβ. By Proposi-
tion 6.5 and then (6.29)
(6.39)
EePNMβ(w, k)2 =
1
k! PN

eT (w+1,w+k)
□N
 · 1
k2N−2βχ□N
 J 2Sk

=

1 + O
 
k2
N
!
1
k2N−2βχ□N
 J 2Sk

where (recall the deﬁnition (6.24) of σp,j)
J 2 :=


k
X
p=1
Jβ
w+p


2
=
k
X
p1,p2=1
X
s∈[w+p1−1]β
t∈[w+p2−1]β
σp1,sσp2,t ∈CSw+k.
Equation (6.42) from Proposition 6.14 below provides the necessary asymp-
totics of the numerator in (6.39) and gives us
EePNMβ(w, k)2 = 1
kEPNM2β(w, 1)+

1 −1
k
  EPNMβ(w, 1)
2+O
 
k2
N
!
with the constant in the O-notation depending only on β. By (6.2) we ﬁnally
get
VarePNMβ(w, k) = EePNMβ(w, k)2 −

EePNMβ(w, k)
2
=
1
k
h
EPNM2β (w, 1) −
 EPNMβ (w, 1)
2i
+ O
 
k2
N
!
= O
 
1
k + k2
N
!
with the constant in the O-notation depending only on β. This completes
the proof of (6.3) (and Proposition 6.3).
□
We consider an analogue of J 2 in which each summand is replaced by
the minimal element of the appropriate coset
J 2
∗:= π0
 J 2
=
k
X
p1,p2=1
X
s∈[w+p1−1]β
t∈[w+p2−1]β
π0
 σp1,sσp2,t

∈CSw+k.


## Page 56


56
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
The following proposition provides the missing component of the above
proof of (6.3).
Proposition 6.14. Let β ∈N and k, N ∈N be such that N2 ≥w + k and
k2 < N. Then
(6.40)
χ□N
 J 2
∗

= k2N2β
"
1
kEPNM2β (w, 1) +

1 −1
k
  EPNMβ(w, 1)
2 + O
 k
N
 #
;
(6.41)
χ□N
 J 2Sk

= χ□N
 J 2
∗

+ O
 
k2N2β k2
N
!
;
(6.42)
χ□N
 J 2Sk

= k2N2β
"
1
kEPNM2β (w, 1) +

1 −1
k
  EPNMβ(w, 1)
2 + O
 
k2
N
! #
with the constants in the O-notation depending only on β.
The remaining part of this section is devoted to its proof.
6.7.1. Decomposition of χ□N
 J 2
∗

. For any p1, p2 ∈{1, . . . , k} denote
Pp1,p2(β) := [w + p1 −1]β × [w + p2 −1]β
and let
A :=
k
X
p=1
X
s,t∈[w]β
χ□N

π0
 σp,sσp,t

;
Let us deﬁne the concatenation of sequences a = (a1, . . . , ax) and b =
(b1, . . . , by) as the sequence a ⊔b := (a1, . . . , ax, b1, . . . , by). For any pair
of complementary set-partitions (Σ, Π) of the set [2β] let us denote
(6.43)
B(Σ,Π) :=
k
X
p1,p2=1
X
(s,t)∈Pp1,p2(β),
s⊔t ∈(Σ,Π)
χ□N

π0
 σp1,sσp2,t

and if Σ is a set-partition of [2β] denote
(6.44)
CΣ :=
X
p1,p2∈{1,...,k},
p1̸=p2
X
s,t∈[w]β,
s⊔t∈(Σ,∅)
χ□N

π0
 σp1,sσp2,t

.


## Page 57


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
57
With these notations
(6.45)
χ□N
 J 2
∗

= A +
X
(Σ,Π)
Π̸=∅
B(Σ,Π) +
X
Σ
CΣ.
Notice that the number of summands on the right hand side of (6.45) is ﬁnite,
depends only on β and does not depend on N or k. Therefore, it is enough
to ﬁnd the asymptotics for each individual summand on the right-hand side.
6.7.2. Asymptotics of A. We proceed in the same way as in Section 6.6.2
to get an exact formula
(6.46)
A = kN2β EPNM2β(w, 1).
6.7.3. Asymptotics of B(Σ,Π). We follow the lines from Section 6.6.3.
Let us ﬁx some pair (Σ, Π) of complementary set-partitions of [2β]. By
Fact 3.1 and Lemma 6.8 there exists Cβ > 0 such that each summand corre-
sponding to (s, t) ∈Pp1,p2(β) such that s⊔t ∈(Σ, Π) fulﬁlls the asymptotic
bound
χ□N

π0
 σp1,sσp2,t
 ≤CβN−∥σp1,sσp2,tSk∥.
On the other hand, the number of the summands on the right-hand side
of (6.43) is bounded from above by
k
X
p1,p2=1
w|Σ| · max{p1, p2}|Π| ≤N2|Σ| k|Π|+2.
By combining these observations with Corollary 6.12 used for the concate-
nated sequence s ⊔t we conclude that
(6.47)
B(Σ,Π) ≤Cβ k2N2β
 k
N
|Π|
.
The last two arguments imply also that
(6.48)
k
X
p1,p2=1
X
(s,t)∈Pp1,p2(β),
s⊔t ∈(Σ,Π)
k2
N∥σp1,sσp2,tSk∥+1 ≤k2
N · k2N2β
 k
N
|Π|
.
These estimations show that if a pair (Σ, Π) of complementary set-partitions
of [2β] is such that Π ̸= ∅then the contribution of B(Σ,Π) to (6.45) is of rel-
atively small order.


## Page 58


58
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
6.7.4. Asymptotics of CΣ. Connected set-partitions of [2β]. We will need
to be much more subtle in calculating (and estimating) the summand CΣ.
We will treat the summand CΣ in two different ways depending on the struc-
ture of Σ.
Let Σ be a set-partition of [2β]. We say that Σ is connected if there exists
a block π ∈Σ which contains simultaneously some element of the set
{1, . . . , β} and some element of the set {β + 1, . . . , 2β}, that is formally,
π ∩[β] ̸= ∅and π ∩{β + 1, . . . , 2β} ̸= ∅. Each such a block π ∈Σ
will be called a link. If Σ does not have any links then we say that Σ is
disconnected.
6.7.5. Asymptotics of CΣ for connected Σ. Let us ﬁx a connected set-partition
Σ of [2β]. We set
nΣ := min

i ∈{β + 1, . . . , 2β} : ∃π∈Σ (i ∈π and π is a link in Σ)
	
.
In other words, nΣ indicates the least number i > β belonging to some link
π of Σ.
Notice that for distinct p1, p2 and a pair of sequences (s, t) such that s ⊔
t ∈(Σ, ∅) the assumptions of the second part of Lemma 6.11 are fulﬁlled
for the sequences (xi) = s ⊔t and (yi) = (p1, . . . , p1, p2, . . . , p2), and
ℓ:= β + nΣ −1. Therefore an inequality
2 |Σ| −∥σp1,sσp2,tSk∥−2β ≤−1
holds for any (s, t) such that s ⊔t ∈(Σ, ∅) with Σ connected.
We now follow the lines in Section 6.7.3 to get the upper bound
(6.49)
CΣ ≤Cβ (k2 −k)N2β−1
which holds for each connected set-partition Σ of the set [2β]. This shows
that the contribution of CΣ with connected Σ to (6.45) is of relatively small
order.
6.7.6. Asymptotics of CΣ for disconnected Σ. We will show that
(6.50)
X
Σ:
Σ is disconnected
CΣ = (k2 −k)N2β EPNMβ(w, 1)
2 + O
 N−2
with the constant in the O-notation depending only on β.
Recall that the CΣ, deﬁned in (6.44), is the sum of characters χ□N evalu-
ated on the minimal permutations π0
 σp1,sσp2,t

. When Σ is disconnected
and p1 ̸= p2, in the permutation σp1,sσp2,t each cycle permutes at most
one big element, so by Lemma 6.8(b) σp1,sσp2,t is the minimal permutation.


## Page 59


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
59
Hence whenever Σ is disconnected
CΣ =
X
p1,p2∈{1,...,k},
p1̸=p2
X
s,t∈[w]β,
s⊔t∈(Σ,∅)
χ□N
 σp1,sσp2,t

.
For any set partition Σ of [2β] let us deﬁne
eCΣ :=
X
p1,p2∈{1,...,k},
p1̸=p2
X
s,t∈[w]β,
s⊔t∈(Σ,∅)
χ□N
 σp1,s

χ□N
 σp2,t

.
Then by Proposition 6.5 applied twice for k = 1
(6.51)
X
Σ
eCΣ =
X
p1,p2∈{1,...,k},
p1̸=p2

X
s∈[w]β
χ□N
 σp1,s




X
t∈[w]β
χ□N
 σp2,t


=
(k2 −k)N2β EPNMβ(w, 1)
2.
Our aim is to show that (6.51) is a good approximation for the left-hand-side
of (6.50).
By Fact 3.2 there exists a constant Kβ > 0 which depends only on β (in
particular it does not depend on N or k) such that for any distinct p1, p2 and
a pair of sequences (s, t) such that s ⊔t ∈(Σ, ∅) with Σ disconnected
χ□N
 σp1,sσp2,t

−χ□N
 σp1,s

χ□N
 σp2,t
 ≤Kβ

N−|σp1,s|−|σp2,t|−2
.
Let us denote for any set-partition Σ of [2β]
RΣ :=
X
p1,p2∈{1,...,k},
p1̸=p2
X
s,t∈[w]β,
s⊔t∈(Σ,∅)
N−|σp1,s|−|σp2,t|−2.
With the introduced notation the following inequality holds
(6.52)

X
Σ
eCΣ −
X
Σ:
Σ is disconnected
CΣ

≤
X
Σ:
Σ is disconnected
KβRΣ +
X
Σ:
Σ is connected
 eCΣ .
We now investigate the asymptotics of the sums on the right-hand-side
of (6.52).


## Page 60


60
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
6.7.7. Asymptotics of the right-hand-side of (6.52). Observe that if Σ is
connected and (s, t) is a pair of sequence such that s ⊔t ∈(Σ, ∅) then
|Σ| = |Σ(s ⊔t)| ≤|Σ(s)| + |Σ(t)| −1.
We follow the lines from Section 6.6.3 to get the upper bound
(6.53)
 eCΣ ≤C2
β (k2 −k)N2β−2
for any connected Σ with universal constant Cβ > 0 depending only on β.
On the other hand, by Lemma 6.8(b) and (6.37) for any set-partition Σ of
[2β]
(6.54)
RΣ ≤(k2 −k)

X
s∈[w]β
N−|σp1,s|−1


2
≤(k2 −k)N2β−2.
Inserting approximations (6.53) for connected Σ and (6.54) for discon-
nected Σ into (6.52) and taking into account (6.51) proves (6.50).
6.7.8. Asymptotics of the sum
X
Σ
CΣ. By (6.49) and (6.50) we get
(6.55)
X
Σ
CΣ = (k2 −k)N2β EPNMβ(w, 1)
2 + O
 N−1
.
6.7.9. Finishing the proof of Proposition 6.14.
Proof of Proposition 6.14. Inserting the equality (6.46) and approximations
(6.47) (for complementary set-partitions (Σ, Π) with Π ̸= ∅) and (6.55) into
(6.45) we conclude that (6.40) holds true.
By Proposition 6.9 there exists Cβ > 0 such that
(6.56)
χ□N
 J 2Sk

−χ□N
 J 2
∗
 ≤Cβ
k
X
p1,p2=1
X
(s,t)∈Pp1,p2(β)
k2
N∥σp1,sσp2,tSk∥+1.
The summands on the right-hand side can be grouped according to the types
(Σ, Π) of the sequences s ⊔t. By (6.48) the right-hand side of (6.56) esti-
mates by k2
N k2N2β which ends the proof of (6.41).
Equation (6.42) is a direct consequence of (6.40) and (6.41).
□
This ﬁnishes the proof of Proposition 6.3


## Page 61


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
61
6.8. Proof of Theorem 6.2. The proof is based on [R´S15, Section 4.10].
We start with a general fact.
Lemma 6.15. Let ε > 0 and µ be a compactly supported probability mea-
sure on R. Let x ∈R be a continuity point of the cumulative distribution
function Fµ of µ. Then there exist δ > 0 and an integer A > 0 with the
following property:
if m is a probability measure on R such that its moments (up to order A)
are δ-close to the moments of µ then
Fµ(x) −Fm(x)
 ≤ε
where Fm is the cumulative distribution function of m.
Proof. If this would not be the case, there would exist a sequence of proba-
bility measures which converges to µ in moments, but would not converge
to µ in the weak topology of probability measures. This is not possible,
since µ is compactly supported and therefore uniquely determined by its
moments [Dur10, Section 3.3.5].
□
We now prove Theorem 6.2.
Proof of Theorem 6.2. We mimic the proof of [R´S15, Theorem 4.1]. Pittel
and Romik [PR07, Theorem 2] found explicitly the limit distribution να
which describes the u-coordinate of the (scaled) position of the box with
the entry ⌊αN2⌋in a uniformly random tableau TN ∈T□N as the semicircle
distribution (2.4) (recall Section 2.3). In our setting this result describes the
u-coordinate of the surfer after draining 1 −α fraction of water. Since ‘the
amount of remaining water w’ is such that
w
N2 →α, the β-th moment γβ of
the distribution να equals
γβ :=
Z
xβ dνα(x) = lim
N→∞EPNMβ(w, 1).
By Proposition 6.3 we get using Chebyshev’s inequality that for any ε >
0 and β ∈N
P eT (w+1,w+k)
□N
Mβ(w, k) −γβ
 > ε

= O
 
1
k + k2
N
!
.
The cumulative distribution function Fνα of the semicircle measure να
is continuous and therefore any x ∈R is its continuity point. Let x ∈R
and let A and δ be the constants given by Lemma 6.15. Then by the union


## Page 62


62
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
bound
(6.57)
P eT (w+1,w+k)
□N
 Fνα(x) −GN(x)
 > ε

≤
A
X
β=1
P eT (w+1,w+k)
□N
Mβ(w, k) −γβ
 > δ

= O
 
1
k + k2
N
!
with the constant in the O-notation depending only on ε.
For the proof of Theorem 6.2 we need to obtain the uniform version
of (6.57) in which the event on the left hand side is taken with supremum
over u ∈R. This can be easily done by choosing a ﬁnite set X ⊆R with
the property that its image Fνα is an ǫ-net for the interval [0, 1]; such a set
exists because Fνα is continuous. The pointwise result (6.57) implies that
the following estimate for the supremum over the ﬁnite set X holds true:
(6.58) P eT (w+1,w+k)
□N

MN : sup
x∈X
Fνα(x) −GN(x)
 > ε

= O
 
1
k + k2
N
!
.
Let x1 < · · · < xℓbe the elements of X. The assumption about the set
X implies that
(6.59) Fνα(x1) < ǫ,
Fνα(xi+1) < Fνα(xi)+2ǫ,
Fνα(xℓ) > 1−ǫ.
The elements of X divide the real line into ℓ+ 1 intervals:
(−∞, x1], [x1, x2], . . . , [xℓ−1, xℓ], [xℓ, ∞).
By considering each interval separately, using monotonicity of the cumula-
tive distribution function Fνα and the monotonicity of GN, as well as (6.59)
it follows that
sup
x∈R
Fνα(x) −GN(x)
 < 2ǫ + sup
x∈X
Fνα(x) −GN(x)
 .
In this way (6.58) completes the proof.
□
7. PROOF OF THEOREM 4.1
The current section is devoted to the proof of Theorem 4.1.
7.1. Overtaking only in one direction. We start with a precise statement
of the heuristic ideas from Section 4.4.4.
Lemma 7.1. Fix k, n ∈N. Let tableaux T ∈Tµ of shape µ with n+1 boxes
and M ∈eT (n+1,n+k)
ν
of shape ν with n + k boxes be such that
T|≤n = M|≤n.


## Page 63


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
63
If 1 ≤p ≤k is such that
posT(n + 1) ⪯posM(n + p) ⪯· · · ⪯posM(n + k)
then jeu de taquin preserves the latter relations, that is
posj(T)(n + 1) ⪯posj(M)(n + p) ⪯· · · ⪯posj(M)(n + k).
Proof. Clearly, j(T)

≤n = j(M)

≤n. Notice also that the boxes in jeu de
taquin paths for tableaux T and M match at least to the boxes ≤n. As
mentioned in Section 4.2, j(M) is a k-Pieri tableau, so
posj(M)(n + p) ⪯· · · ⪯posj(M)(n + k)
and therefore it remains to prove that
(7.1)
posj(T)(n + 1) ⪯posj(M)(n + p).
We consider the following two cases:
1. The box n + 1 in T slid during jeu de taquin, i.e., posT(n + 1) ̸=
posj(T)(n + 1). Consider two subcases:
1a) The box n+1 in T slid to the left; in this case it does not matter
how (and if) the box n + p in M slid and (7.1) holds.
1b) The box n+1 in T slid to the bottom. Then we use the assump-
tion that M is k-Pieri to show that if posM(n+p) = posT(n+1)
then n + p in M also slid to the bottom and (7.1) holds. On the
other hand if posT(n + 1) ≺posM(n + p) then the box n + p
in M must be strictly to the right of n + 1 in T and it does not
matter if it slides or not, so (7.1) also holds.
2. The box n+1 in T did not slide, i.e., posT(n+1) = posj(T)(n+1).
In this case, the JDT path in T ends on some box ≤n which is
strictly left-top or strictly right-bottom to the posT(n + 1). Hence,
if posT(n + 1) = posM(n + p) then the box n + p in M does not
slide. Otherwise, (by the initial relation) it must be strictly to the
right (and weakly to the bottom) of posT(n + 1) and it does not
matter if it slides or not. All in all, (7.1) holds.
□
7.2. Relative position of the surfer. We recommend the reader to recall
the notions in Section 4 and heuristics for the proof of Theorem 4.1 in Sec-
tion 4.4.
Let 0 < t1 < t2 < 1 and denote
w := ⌈(1 −t1)N2⌉−1.
Let k be a positive integer such that w + k ≤N2. By Proposition 5.1 used
for C = 1, ∆= t1, a = w and λ = □N there exists a pair of random
tableaux T, M deﬁned on the same probability space with the following
properties:


## Page 64


64
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
(A1) T is a uniformly random element of T□N;
(A2) M is a random element of eT (w+1,w+k)
□N
sampled according to the dis-
tribution which fulﬁlls the following total variation distance bound
δ

M, P eT (w+1,w+k)
□N

≤d
k2
√
N2 −w
for some universal constant d > 0 which depends only on t1;
(A3) T

≤w = M

≤w holds true almost surely.
Since the dual promotion ∂∗is a bijection, by (A1) the tableau T|≤w+1 has
the same distribution as the initial conﬁguration of the single surfer T ′
N (see
(4.5)) and by (A2) the tableau M

≤w+k has approximately the same distri-
bution (up to the total variation distance in (A2)) as the initial conﬁguration
of the multisurfers M′
N (see (4.11)). Moreover, by (A3) the initial conﬁg-
urations of water are the same for both stories. Therefore we will refer to
the box w + 1 in T as the surfer and to the boxes w + 1, . . . , w + k in M as
the multisurfers.
Recall that the deﬁnition (6.1) of the random variable GN(u) depends
implicitly on the choice of the tableau MN. For an integer 0 ≤q ≤w we
denote by Gq
N(u) this random variable obtained by substituting MN with
jq(M). We underline here that MN and jq(M) need not have the same
distribution. We also deﬁne eG q
N to be the fraction of the multisurfers which
are to the left of the surfer, more precisely
(7.2)
eG q
N := Gq
N
 1
N ujq(T)
w+1

= 1
k max
n
p ∈{1, . . . , k} : ujq(M)
w+p
≤ujq(T)
w+1
o
.
The following proposition gives a relation between eG q
N and the theoretical
longitude of the surfer on the common probability space of the surfer and
multisurfers deﬁned in the beginning of this section.
Proposition 7.2. Let s ≥0 and t > 0 be such that s + t < 1. Let w(N) =
⌈(1 −t)N2⌉−1 for N ∈N and let k = k(N) fulﬁll Assumption 6.1. Let
q = q(N) be a sequence of non-negative integers such that
0 ≤q(N) ≤⌊(1 −t)N2⌋
and
lim
N→∞
q
N2 = s.
Then for any ε > 0
P

(T, M) :

eG q
N −Fν1−t−s
 1
N ujq(T)
w+1
 > ε

= O
 
1
k + k2
N
!
and the constant in the O-notation depends only on s, t + s and ε.


## Page 65


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
65
Proof. By the discussion below Equation (7.2)
P

(T, M) :

eG q
N −Fν1−t−s
 1
N ujq(T)
w+1
 > ε

=
P

(T, M) :
Gq
N
 1
N ujq(T)
w+1

−Fν1−t−s
 1
N ujq(T)
w+1
 > ε

.
The latter is bounded from above by
(7.3)
P
 
(T, M) : sup
x∈R
Gq
N(x) −Fν1−t−s(x)
 > ε
!
.
The random event in (7.3) is expressed purely in terms of the random tableau jq(M)
and does not involve the random tableau T. For this reason the probability
in (7.3), due to the condition (A2) on page 64 and the bijectivity of the dual
promotion ∂∗, is equal to
P eT (w−q+1,w−q+k)
□N
 
MN : sup
x∈R
GN(x) −Fν1−t−s(x)
 > ε
!
+ O
 
k2
N
!
with the constant in the O-notation depending only on t. Since lim w−q
N2 =
1 −t −s > 0 we can apply Theorem 6.2 which completes the proof.
□
7.3. Proof of the upper bound (4.2) in Theorem 4.1. Let k = k(N) be
such that k(N) →∞and k(N) = o(
√
N), i.e., (4.10) is satisﬁed. We
will use the results from Section 7.2 to prove the upper bound (4.2). Let
q := ⌊t2N2⌋−⌊t1N2⌋. Recall that w = ⌈(1 −t1)N2⌉−1 (cf. Section 7.2).
By (A1) from Section 7.2 we can translate the probability on the left-
hand-side of (4.2) into the setting of T in the following way
PN

T ∈T□N : Ψth
N (t2) −Ψth
N (t1) > ε

=
P
 
(T, M) : Fν1−t2
 1
N ujq(T)
w+1

−Fν1−t1
 1
N uT
w+1

> ε
!
;
note that the event on the right-hand side does not involve the tableau M.
The latter probability can be estimated from above via the union bound by
the sum of probabilities of the following three events:
• the fraction of the multisurfers in the ﬁnal position (i.e., in time t2)
which are to the left of the surfer is ‘unusually small’, that is
A :=
(
(T, M) : Fν1−t2
 1
N ujq(T)
w+1

−eG q
N > ε
2
)
;


## Page 66


66
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
• the number of the multisurfers which are to the left of the surfer
increases over time, more precisely
B :=
n
(T, M) : eG q
N −eG 0
N > 0
o
;
• the fraction of the multisurfers in the initial position (i.e, in time t1)
which are to the left of the surfer is ‘unusually big’, that is
C :=
(
(T, M) : eG 0
N −Fν1−t1
 1
N uT
w+1

> ε
2
)
.
By Proposition 7.2 the probabilities of the events A and C are of order
O

1
k + k2
N

. By Lemma 7.1 the event B = ∅is impossible. The choice of
the sequence k as in the beginning of this subsection implies that the upper
bound (4.2) holds.
7.4. Proof of the lower bound (4.3) in Theorem 4.1. For any Young dia-
gram λ and tableau T ∈Tλ we will denote by λtr and T tr, respectively, the
diagram and the tableau obtained by a transposition of the diagram λ and
the tableau T.
The transposition of tableaux gives a natural bijection between the sets Tλ
and Tλtr of standard tableaux, respectively, of shape λ and its transpose λtr.
Moreover, under the transposition the u-coordinate of the given box in a
standard tableau T changes its sign, namely for any n ∈{1, . . . , |T|}
(7.4)
uT
n = −uT tr
n .
In particular, the u-coordinate of the surfer u(Xt) changes its sign under the
transposition, i.e., u(Xt) = −u(Xtr
t ) where Xtr
t denotes the position of the
surfer in the transposed tableau T tr.
Recall that for any α ∈(0, 1) by να we denote the limit measure found
by Pittel and Romik on the circle of latitude α, see Section 2.3. The push-
forward of the measure να under the involution R ∋z 7→−z is a measure
˜να which fulﬁlls the following equality
(7.5)
˜να
 (−∞, u]

= να
 [−u, ∞)

for all u ∈R.
Notice that by (7.4) the measure ˜να is the limit measure on the circle of
latitude α for the transposed sequence of Young diagrams (□tr
N).
Let us denote the position of the surfer in the transposed tableau by X∗
t ,
cf. (2.5), and the theoretical longitude of the surfer in the transposed tableau
by η, i.e.,
η(t) := F˜ν1−t
 u(X∗
t )

for t ∈[0, 1].
Observe that by (7.5) and the continuity of Fν1−t
(7.6)
η(t) = 1 −Fν1−t
 −u(X∗
t )

.


## Page 67


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
67
Equation (4.2) applied to the transposed tableaux gives
lim
N→∞PN

T ∈T□tr
N : η(t2) −η(t1) > ε

= 0.
On the other hand by (7.6) and then (7.4) we get
η(t2) −η(t1) =

1 −Fν1−t2
 −u(X∗
t2)

−

1 −Fν1−t1
 −u(X∗
t1)

=
Fν1−t1

u
 (X∗
t1)tr
−Fν1−t2

u
 (X∗
t2)tr
.
Since (X∗
t )tr reﬂects the position of the surfer in the original (not-transposed)
tableau we have
η(t2) −η(t1) = Ψth
N (t1) −Ψth
N (t2).
Since we consider the uniform distribution on the set of tableaux, this ends
the proof of the lower bound (4.3) and completes the proof of Theorem 4.1.
8. PROOF OF THEOREM 2.3
8.1. Plan for the proof of Theorem 2.3. We will make the following steps
in the proof of Theorem 2.3:
(S1) Pick a candidate for the random variable ΨN : T□N →[0, 1].
(S2) Prove a pointwise version of Theorem 2.3: with the help of Lemma 8.1
and Theorem 4.1 we will show that the chosen candidate gives a good
approximation of surfer’s position for an arbitrary t ∈(0, 1), i.e.,
(8.1) ∀t∈(0,1)
lim
N→∞PN

TN ∈T□N :
Xt(TN) −P1−t,ΨN(TN)
 > ε

= 0.
The proof will be given in Section 8.5.
(S3) Prove the full (i.e., the original) version of Theorem 2.3, i.e.,
lim
N→∞PN
 
TN ∈T□N : sup
t∈[0,1]
Xt(TN) −P1−t,ΨN(TN)
 > ε
!
= 0.
We will start with a ﬁnite ε-net of the family of level curves {hα :
α ∈[0, 1]} parameterized by 0 = α0 < α1 < · · · < αp < αp+1 = 1.
By the previous point, (8.1) holds uniformly for t ∈{α0, . . . , αp+1}
in a ﬁnite set. Then for the intermediate moments of time αi < t < αi+1
we will use the monotonicity of the sliding path and in this way jus-
tify that (8.1) holds uniformly over t ∈(0, 1). This proof will be
given in Section 8.6.
In the very end, in Section 8.7, we will show that the probability distri-
bution of the random variable ΨN converges to the uniform distribution on
the unit interval [0, 1].


## Page 68


68
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
8.2. Auxiliary notation. In the proof we will switch between the position
of the surfer in the XY and the UV coordinate systems as well as in the
geographic coordinates. For any t ∈(0, 1) let us introduce the notation for
the true and the theoretical u−and v−coordinate; namely we deﬁne the
following functions T□N →R by
ut := u(Xt) ,
vt := v(Xt)
and
uth
t :=

Fν1−t
−1 Ψth
N(t)

,
vth
t := h1−t
 uth
t

(recall that Ψth
N (t) = Fν1−t(ut), cf. (4.1), and see Section 2.2 for the deﬁni-
tion of ht). Denote additionally for any t ∈[0, 1]
(xt, yt) := Xt
and

xth
t , yth
t

:=
 
vth
t −uth
t
2
, uth
t + vth
t
2
!
.
8.3. The surfer’s position can be asymptotically recovered from the the-
oretical longitude. We start with the result which shows that, in principle,
it is possible to recover the the true position of the surfer Xt in the time
t ∈(0, 1) from its theoretical longitude Ψth
N (t).
Lemma 8.1. Let 0 < t < 1. For any ε > 0
lim
N→∞PN

TN ∈T□N : ut(TN) ̸= uth
t (TN)

= 0
(8.2)
and
lim
N→∞PN

TN ∈T□N :
vt(TN) −vth
t (TN)
 > ε

= 0.
(8.3)
Proof. Let 0 < t < 1 and ε > 0. We start with the proof of (8.2). Recall
that the position of the surfer Xt corresponds to the position of the box with
the number ⌈(1 −t)N2⌉in the tableau (∂∗)⌊tN2⌋(TN), cf. (2.5), and so by
[PR07, Theorem 2] the random variable ut converges in distribution to the
measure ν1−t which has no atoms and has a compact connected support
supp(ν1−t) =
h
−2
p
t(1 −t), 2
p
t(1 −t)
i
.
Observe that since ν1−t has no atoms, whenever ut ∈supp(ν1−t) then by
the deﬁnition
(8.4)
uth
t = F −1
ν1−t

Ψth
N (t)

= ut.
On the other hand
(8.5)
PN
 TN ∈T□N : ut(TN) /∈supp(ν1−t)
 N→∞
−−−→0.


## Page 69


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
69
Indeed, for any ε > 0 consider the function fε : R →R given by
fε(x) := 1 −min

1, 1
ε dist
 x, R \ supp(ν1−t)

,
x ∈R,
where dist(x, A) := inf{d(x, y) : y ∈A} is the Hausdorff distance of the
point x from a set A. Clearly fε is continuous and bounded.
The distribution of the random variable ut is a pushforward of the mea-
sure PN under the mapping TN 7→ut(TN). Therefore by the convergence
in distribution of the random variable ut to the distribution given by the
measure ν1−t we get for any ε > 0
(8.6)
PN
 TN ∈T□N : ut(TN) /∈supp(ν1−t)

≤
Z
T□N
fε(ut) dPN
N→∞
−−−→
Z
R
fε dν1−t.
Clearly, fε converges pointwise as ε →0 to the indicator function 1R\supp(ν1−t),
therefore by the Lebesgue dominated convergence theorem
lim
ε→0
Z
R
fε dν1−t = ν1−t

R \ supp(ν1−t)

= ν1−t

∂
 supp(ν1−t)

= 0.
This together with (8.6) implies (8.5).
A conjunction of (8.4) and (8.5) proves (8.2).
Equation (8.3) follows from the result of Biane [Bia98, Theorem 1.5.1].
We will shortly describe it here, but the more developed discussion and
precise statements formulated using our notation are placed in Section 10.
The boundary of a Young diagram λ seen in the (u, v)-coordinate system
can be viewed as a non-negative 1-Lipschitz function ωλ, see Figure 14. The
function ωλ is initially deﬁned on the interval I given by the range of the
u-coordinates of λ, but it can be extended to a function deﬁned on the real
line R by gluing ωλ|I with the modulus function x 7→|x|. This extended
function ωλ: R →R+ is called the proﬁle of λ, cf. Section 10.1.
The restriction T|≤⌈(1−t)N2⌉of the random tableau T has a (random)
shape
λ1−t := sh T|≤⌈(1−t)N2⌉
whose (random) proﬁle ωλ1−t is such that the following equality in terms of
the u- and v-coordinates of the surfer (in time t) holds true:
vt(TN) = ωλ1−t
 ut(TN)

.
On the other hand if ut(TN) = uth
t (TN) then
vth
t (TN) = h1−t(uth
t (TN)) = h1−t(ut(TN)).


## Page 70


70
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
u
−4
−3
−2
−1
1
2
3
4
5
v
1
2
3
4
5
x
1
2
3
4
5
y
1
2
3
4
Figure 14. A Young diagram λ = (4, 3, 1) shown in the Rus-
sian convention. The blue solid line represents its proﬁle ωλ.
The (u, v)-coordinate system corresponding to the Russian
convention and the XY - coordinate system corresponding
to the French convention are shown.
We proved in (8.2) that the set of tableaux TN ∈T□N for which ut(TN) =
uth
t (TN) has asymptotically full probability. Therefore with asymptotically
full probability the following inequality holds
(8.7)
vt(TN) −vth
t (TN)
 ≤sup
x∈R
ωλ1−t(x) −h1−t(x)
 .
By the aforementioned result [Bia98, Theorem 1.5.1] (see Proposition 10.1
for the precise general statement) the right-hand-side of (8.7) converges in
probability to 0. This completes the proof of (8.3) and Lemma 8.1.
□
8.4. A candidate for the random variable ΨN(TN), development of (S1).
Pick any t0 ∈(0, 1) and deﬁne for TN ∈T□N
ΨN(TN) := Ψth
N(t0)(TN).
We will show that the random variable ΨN has the desired properties from
Theorem 2.3.
For any t ∈[0, 1] we deﬁne the approximated u- and v-coordinate of the
surfer as
uΨ
t :=

Fν1−t
−1
(ΨN) ,
vΨ
t := h1−t
 uΨ
t

.


## Page 71


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
71
These deﬁnitions were chosen in such a way that that the approximated
position of the surfer in the XY coordinate system

xΨ
t , yΨ
t

:=
 
vΨ
t −uΨ
t
2
, uΨ
t + vΨ
t
2
!
= P1−t,ΨN(TN)
is the point which appears in the statement of Theorem 2.3 and Eq. (8.1).
With this notation the expression in the modulus in the event in (8.1)
takes the form
Xt(TN) −P1−t,ΨN(TN)
 =
1
√
2
(ut, vt) −

uΨ
t , vΨ
t
 .
8.5. The proof of (S2) – the pointwise version of Theorem 2.3. Let ε > 0
and t ∈(0, 1). By the triangle inequality,
ut(TN) −uΨ
t (TN)
 ≤
ut(TN) −uth
t (TN)
 +
uth
t (TN) −uΨ
t (TN)

(8.8)
and
vt(TN) −vth
t (TN)
 ≤
vt(TN) −vth
t (TN)
 +
vth
t (TN) −vΨ
t (TN)
 .
(8.9)
By Lemma 8.1, in each of the above two inequalities the ﬁrst summand
on the right-hand side converges in probability to 0, that is,
ut(TN) −uth
t (TN)

P−→0
and
vt(TN) −vth
t (TN)

P−→0.
The second summands on the right hand side of (8.8) and (8.9) are the dis-
tances between the values of uniformly continuous functions, respectively,
ψ 7→uψ
t and the composition ψ 7→h1−t(uψ
t ) evaluated at the arguments
Ψth
N (t)
and
Ψth
N (t0) = ΨN.
By Theorem 4.1 with t1 = min(t, t0) and t2 = max(t, t0) the distance
between these two arguments converges in probability to 0, i.e.,
Ψth
N (t) −ΨN
P−→0.
Therefore we get
uth
t (TN) −uΨ
t (TN)

P−→0
and
vth
t (TN) −vΨ
t (TN)

P−→0.
As the result
ut(TN) −uΨ
t (TN)

P−→0
and
vt(TN) −vΨ
t (TN)

P−→0
which completes the proof (8.1) which is the pointwise version of Theo-
rem 2.3.
8.6. The proof of (S3) – the full version of Theorem 2.3.


## Page 72


72
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
8.6.1. Uniform continuity of the geographic coordinate system. We start
with showing that the geographic coordinate system on the square (recall
Section 2.4) is uniformly continuous.
Lemma 8.2. The function
[0, 1] × [0, 1] ∋(α, ψ) 7→Pα,ψ =

xψ
α, yψ
α

is uniformly continuous.
Proof. Since the mapping
 xψ
α, yψ
α

7→
1
√
2
 uψ
α, vψ
α

is an isometry (as a
rotation in R2) it is enough to show that each coordinate of the function
[0, 1] × [0, 1] ∋(α, ψ) 7→

uψ
α, vψ
α

=

uψ
α, h1−α

uψ
α

is uniformly continuous.
Recall that the limit distribution να has density (2.4). It is easy to show
that for any α ∈(0, 1) the cumulative distribution function Fνα of να fulﬁlls
the equation
Fνα(u) = FSC
 
u
2
p
α(1 −α)
!
for all |u| ≤2
p
α(1 −α)
where FSC denotes the cumulative distribution function of the standard semi-
circle distribution with the density (1.3). This implies that for any ψ ∈[0, 1]
and α ∈(0, 1) we get
ψ = Fν1−α

uψ
α

= FSC
 
uψ
α
2
p
α(1 −α)
!
,
which after applying F −1
SC gives
(8.10)
uψ
α = 2
p
α(1 −α) · F −1
SC (ψ).
Moreover, by the deﬁnition P0,ψ = (0, 0) ∈R2 and P1,ψ = (1, 1) ∈R2
(cf. Section 2.4), hence (8.10) holds for all ψ ∈[0, 1] and α ∈[0, 1].
Therefore the mapping (α, ψ) 7→uψ
α is uniformly continuous since ψ 7→
F −1
SC (ψ) is uniformly continuous. Indeed, F −1
SC is the inverse function of
FSC which is injective on
h
−2
p
α(1 −α), 2
p
α(1 −α)
i
, continuous and
has compact domain and range.
The function (α, u) 7→hα(u) is uniformly continuous on the domain
♦:=
n
(α, u) : α ∈[0, 1] and |u| ≤2
p
α(1 −α)
o


## Page 73


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
73
(as a continuous mapping on the compact set ♦). Hence the function (α, ψ) 7→
vψ
α is uniformly continuous as the composition of two uniformly continuous
functions:
♦∋(α, u) 7→hα(u)
and
(α, ψ) 7→(1 −α, uψ
α) ∈♦.
□
8.6.2. The proof of (S3) – the full version of Theorem 2.3. Let ε > 0. By
Lemma 8.2 the function
[0, 1] × [0, 1] ∋(α, ψ) 7→Pα,ψ
is uniformly continuous, so there exists δ > 0 such that
(8.11)
∀s,t∈[0,1] |s −t| < δ =⇒∀ψ∈[0,1]
Ps,ψ −Pt,ψ
 < ε.
Let us take a ﬁnite δ-net 0 = α1 < · · · < αn = 1 of the interval [0, 1]. By
the pointwise version (S2) of Theorem 2.3, which we proved in Section 8.5,
(8.12)
Xαi(TN) −P1−αi,ΨN(TN)
 P−→0
for i ∈{1, . . . , n}
(the latter holds for i = 1 and i = n by the deﬁnition of Pα,ψ, cf. Sec-
tion 2.4). Therefore there exists a subset T ∗
N ⊆T□N of asymptotically
full measure which consists of tableaux TN with the property that for each
i ∈{1, . . . , n}
(8.13)
xαi(TN) −xΨ
αi(TN)
 < ε
and
yαi(TN) −yΨ
αi(TN)
 < ε.
By the monotonicity of the sliding path for any i ∈{1, . . . , n −1} and
t ∈[αi, αi+1]
(8.14)
xαi+1 ≤xt ≤xαi
and
yαi+1 ≤yt ≤yαi.
By (8.13) and (8.14) for any TN ∈T ∗
N and any i ∈{1, . . . , n −1} and
t ∈[αi, αi+1] the following system of inequalities is satisﬁed:





−ε +

xΨ
αi+1 −xΨ
t

≤xt −xΨ
t ≤

xΨ
αi −xΨ
t

+ ε;
−ε +

yΨ
αi+1 −yΨ
t

≤yt −yΨ
t ≤

yΨ
αi −yΨ
t

+ ε.
Since for any t ∈[0, 1]
Xt = (xt, yt)
and
P1−t,ΨN(TN) =

xΨ
t , yΨ
t

and by (8.11) for any i ∈{1, . . . , n −1} and t ∈[αi, αi+1]
max
xΨ
αi −xΨ
t
 ,
xΨ
αi+1 −xΨ
t
 ,
yΨ
αi −yΨ
t
 ,
yΨ
αi+1 −yΨ
t


< ε
we infer that for TN ∈T ∗
N
sup
t∈[0,1]
Xt(TN) −P1−t,ΨN(TN)
 < 2ε.


## Page 74


74
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
This completes the proof of (S3) since T ∗
N has asymptotically full probabil-
ity.
8.7. Limit distribution of the random variable ΨN. We will show the
second component of Theorem 2.3, namely that the random variable ΨN
converges in distribution to the uniform distribution on the unit interval [0, 1].
Let GN denote the cumulative distribution function of the random vari-
able ΨN : T□N →[0, 1]. For any z ∈[0, 1] we have (recall (4.1))
(8.15)
GN(z) = PN

TN : Fν1−t0
 ut0(TN)

≤z

=
PN

TN ∈T□N : ut0(TN) ≤

Fν1−t0
−1
(z)

.
By [PR07, Theorem 2], the distribution of the random variable ut0 con-
verges weakly (as N →∞) to the measure ν1−t0 which has no atoms, so
the right-hand side of (8.15) converges to
Fν1−t0

F −1
ν1−t0 (z)

= z
which is the cumulative distribution function of the uniform measure U(0, 1).
This completes the proof of the second component of Theorem 2.3, and
hence the proof of Theorem 2.3.
9. THE CORRESPONDENCE BETWEEN EVACUATION AND SLIDING
PATHS
The results which we consider in this section hold for general, not neces-
sarily square tableaux. For a tableau T ∈Tλ with n = |λ| boxes we denote
by
revevac(T) =

posn
 jn−1(T)

, . . . , posn
 j1(T)

, posn(T)

the evacuation path (1.8) written in the reverse order.
The following result shows an intimate relationship between the sliding
paths and the evacuation paths and, in particular, implies equivalence of
Theorems 2.3 and 2.4 (see Section 9.2 for the proof).
Proposition 9.1. Let λ be a ﬁxed Young diagram and let T ∈Tλ be a
random standard Young tableau sampled according to the uniform measure
on Tλ. Then the probability distributions of the lazy sliding path q(T) and
the evacuation path revevac(T) coincide.
Proof. We will construct a certain bijection ε∗: Tλ →Tλ on the set of
tableaux of shape λ. Clearly, the random tableaux T and ε∗(T) have the same
distribution. An application of Proposition 9.3 below completes the proof.
□


## Page 75


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
75
In the remaining part of this section we will present the details of the map ε∗
and we will prove that Proposition 9.3 indeed holds true.
9.1. Dual evacuation. The dual evacuation has a beautiful algorithmic de-
scription in terms of the manipulations of the boxes of T, cf. [PW11, Def-
inition 2.10], however we will not make use of it. For our purposes it is
more convenient to deﬁne the dual evacuation ε∗implicitly by Robinson–
Schensted–Knuth correspondence as follows. For a permutation σ = (σ1, . . . , σn) ∈
Sn we denote
σ♯:= (n + 1 −σn, . . . , n + 1 −σ1) ∈Sn.
If σ corresponds to a pair (P, Q) under RSK, then σ♯corresponds to
 ε∗(P), ε∗(Q)

under RSK, see [Sta99, A1.2.10].
We will use the following fact (see [Sag01, Proposition 3.9.3] for the
proof).
Fact 9.2 ([Sch63]). For any σ ∈Sn, the following identity holds up to
renumbering of the boxes on the left-hand side, so that the resulting tableau
becomes standard
(9.1)
(j ◦Q) (σ) = (Q ◦s) (σ)
for σ = (σ1, . . . , σn) ∈Sn
where s(σ) = s(σ1, σ2, . . . , σn) := (σ2, . . . , σn) is a shift.
Proposition 9.3.
q(T) = revevac
 ε∗(T)

.
Proof. For any tableaux R, S we will use a shorthand notation
R/S = sh R/ sh S
for the skew diagram obtained by subtracting their shapes. In all examples
below this skew diagram R/S = {□} consists of a single box; we will
write shortly □= R/S.
Let T = Q(σ) be a recording tableau of some permutation σ; with these
notations ε∗(T) = Q
 σ♯
.
By (9.1), the lazy sliding path fulﬁlls for i ∈[n]
(9.2)
qi(T) = Q (σ1, . . . , σi) /j
 Q (σ1, . . . , σi)

=
Q (σ1, σ2, . . . , σi) /Q (σ2, . . . , σi) .
On the other hand, by (9.1), applying jeu de taquin n−i times to ε∗(T) =
Q
 σ♯
, leads to the tableau (up to renumbering boxes on the left-hand side
so that the tableau becomes standard)
jn−i  ε∗(T)

= Q (n + 1 −σi, . . . , n + 1 −σ2, n + 1 −σ1) .


## Page 76


76
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
The position of the box with the maximal entry in a recording tableau can
be found by comparing this tableau to the recording tableau of a truncated
sequence; it follows that
(9.3)
posn jn−i  ε∗(T)

= Q (n + 1 −σi, . . . , n + 1 −σ2, n + 1 −σ1) /
Q (n + 1 −σi, . . . , n + 1 −σ2) .
By the result of Schensted [Sch61, Lemma 7] and Greene theorem [Gre74,
Theorem 3.1] the shapes of the tableaux which contribute to the right-hand
sides of (9.2) and (9.3) are equal which concludes the proof.
□
9.2. Proof of Theorem 2.4.
Proof of Theorem 2.4. Let N ∈N. Let ΨN : T□N →[0, 1] be the random
variable which is given by Theorem 2.3. We deﬁne the random variable
eΨN : T□N →[0, 1] by
eΨN(TN) := ΨN(ε∗(TN)).
Since ε∗is a bijection,
PN
n
TN ∈T□N : sup
t∈[0,1)
Xt(TN) −P1−t,ΨN(TN )
 > ε
o
=
PN
n
TN ∈T□N : sup
t∈[0,1)
Xt(ε∗(TN)) −P1−t,ΨN(ε∗(TN))
 > ε
o
=
PN
n
TN ∈T□N : sup
t∈[0,1)

1
N q⌈(1−t)N2⌉(TN) −P1−t,eΨN(TN)
 > ε
o
=
PN
n
TN ∈T□N : sup
t∈(0,1]

1
N q⌈tN2⌉(TN) −Pt,ΨN(TN)
 > ε
o
,
where the second equality is a consequence of Proposition 9.3. By The-
orem 2.3 the left-hand side converges to 0 in the limit N →∞; on the
other hand the right-hand side is the probability which appears in Theo-
rem 2.4.
□
10. GENERALIZATIONS OF THE MAIN RESULTS
FOR NON-SQUARE TABLEAUX
10.1. Continuous diagrams. We call a function ω : R →R a continuous
diagram [Ker93a; Ker98] if
• ω is a 1-Lipschitz function, i.e.,
|ω(u1) −ω(u2)| ≤|u1 −u2|
for all u1, u2 ∈R;
• ω(u) = |u| for sufﬁciently large |u|.


## Page 77


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
77
We will denote the set of continuous diagrams by CY; we endow this set
with the L∞-metric. (Our deﬁnition is more speciﬁc than the one of Kerov
[Ker93a] who allows to additionally translate our centered continuous dia-
grams along the real line.)
Any (usual) Young diagram λ seen in the (u, v)-coordinate system is a
1-Lipschitz function deﬁned on some interval (given by the range of the u-
coordinates of λ) and has slopes equal to ±1. It can be extended outside its
initial domain by a modulus function x 7→|x|. In this way we obtain a con-
tinuous diagram ωλ to which we will refer as the proﬁle of λ, see Figure 14.
Let s > 0. For a continuous diagram ω we deﬁne the scaling of ω by s as
the following continuous diagram denoted by sω
sω : R ∋u 7→s · ω
 s−1u

.
Let (λN) be a sequence of Young diagrams with the property that the
sequence of the corresponding rescaled proﬁles
 
1
p
|λN|
ωλN
!
converges to a continuous diagram Λ in the L∞-metric, that is,
sup
u∈R

1
p
|λN|
ωλN
p
|λN| u

−Λ(u)

N→∞
−−−→0.
We will call Λ the limit shape for the sequence of Young diagrams (λN) and
denote such convergence by
1
√
|λN|λN →Λ.
10.2. The asymptotic setup. Let C ≥1 be a ﬁxed constant. For each
integer N ≥1 let λN be a C-balanced Young diagram. We assume that
lim
N→∞|λN| = ∞
and that there exists a limit shape Λ ∈CY for the sequence (λN), i.e., that
1
√
|λN|λN →Λ.
Our goal in Section 10 is to ﬁnd counterparts of Theorems 2.3 and 2.4 in
which the sequence (□N) of square diagrams is replaced by the sequence
(λN) of C-balanced Young diagrams.
10.3. The limit curves. The result of Pittel and Romik concerning the exis-
tence of the level curves [PR07, Theorem 1(i)], cf. Section 2.2, is a special
case of a more general phenomenon. Using the results of Biane [Bia98,
Theorem 1.2 and Theorem 1.5.1] one can show that under the assumptions
from Section 10.2 there exists a family of level curves for a uniformly ran-
dom Young tableau of the shape λN (in the limit as N →∞). The following
proposition describes precisely this result.


## Page 78


78
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
Proposition 10.1. Let (λN) be a sequence of C-balanced Young diagrams
such that |λN| →∞and
1
√
|λN|λN →Λ for some continuous diagram Λ ∈
CY (i.e., (λN) fulﬁlls the assumptions in Section 10.2). For any α ∈[0, 1]
there exists a continuous diagram Λα ∈CY such that
1
p
|λN|
sh

TN

≤⌊α·|λN|⌋

P−→Λα
where TN is a uniformly random element of TλN.
We will say that Λα is the α-level curve for the sequence (λN) or, shortly,
the α-level curve for the diagram Λ. Note that Λ0 is the empty diagram and
Λ1 = Λ.
For example, in the case when λN = □N is a square Young diagram, the
α-level curve for (λN) is the curve hα, cf. Section 2.2.
Remark 10.2. Biane proved his results [Bia98, Theorem 1.2 and Theorem 1.5.1]
with the tools of the free probability theory [MS17], but Proposition 10.1
can be also showed using the beam models [Sun18] or by solving a gradient
variational problem [KP21].
10.4. The limit measures on the level curves. The second result of Pittel
and Romik which gives explicitly the limit measure on the α-level curve for
the square diagram [PR07, Theorem 2], cf. Section 2.3, is a special case of
another general result. It turns out that to every continuous diagram we can
associate two natural measures – the transition measure and the cotransition
measure – which have very natural interpretations in the case of the usual
Young diagrams.
10.4.1. Transition measure of a continuous diagram. To any continuous di-
agram ω ∈CY, one can associate a probability measure µω, called the tran-
sition measure of ω [Ker93b; Bia98], as the unique compactly supported
measure on R such that its Cauchy transform
Gµω(z) :=
Z
R
1
z −x dµω(x)
is given by the equation
Gµω(z) = 1
z exp
Z
R
1
x −zσ′(x) dx = 1
z exp
Z
R
1
(x −z)2σ(x) dx
where σ(u) := (ω(u) −|u|)/2.
The motivations for this notion are related to random walks on the set
of Young diagrams: the atoms of the transition measure µωλ of a usual
Young diagram λ correspond to the Markov’s transition probabilities in the
Plancherel growth process starting in λ [Ker93b, Section 3.2].


## Page 79


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
79
The mapping which to a continuous diagram ω assigns the transition mea-
sure µω is a homeomorphism [Ker93b, Section 2.3]. Moreover, a continuous
diagram is uniquely determined by its transition measure.
10.4.2. Cotransition measure of a continuous diagram. For a continuous
diagram ω ∈CY we deﬁne its area as the area of the region between the
proﬁle and the x- and the y-axis:
A(ω) =
Z
R
 ω(x) −|x|

dx.
The cotransition measure νω of ω is deﬁned as the unique probability mea-
sure with the Cauchy transform Gνω given by the following equation [Rom04,
Equation (8)]:
(10.1)
A(ω)
2
Gνω(x) = x −
1
Gµω(x).
By convention, the cotransition measure of the empty diagram νω∅= δ0 is
deﬁned to be the measure concentrated in 0.
The cotransition measure νωλ of a usual Young diagram λ is the distribu-
tion of the u-coordinate of the box with the maximal entry |λ| in a uniformly
random standard tableau of shape λ, cf. [Rom04, page 628 and the comment
below Eq. (6)]. In particular, the measure να introduced in Section 2.3 to
which we referred as the limit measure is the cotransition measure corre-
sponding to the continuous diagram hα (more precisely, to the proper exten-
sion of the function hα given by (2.2) by x 7→|x| and x 7→2 −|x|).
Be advised that diagrams of different shape may have the same cotran-
sition measure. For example, the square Young diagram □N has the same
cotransition measure νω□N = δ0 concentrated at the point u = 0, no matter
which size of the square N ∈N we choose. However, if we restrict our
considerations to the set of (centered) continuous diagrams of ﬁxed positive
area, then any diagram is uniquely determined by its cotransition measure
and this correspondence is a homeomorphism, [Rom04, Theorem 6].
10.4.3. The limit measures on the level curves of continuous diagram. We
will refer to the cotransition measure νΛα corresponding to the α-level curve
Λα for a continuous diagram Λ as the limit (or cotransition) measure on the
level curve Λα.
The cumulative distribution function of the limit measure νΛα will be
denoted by FΛα, i.e.,
FΛα(u) := νΛα
 (−∞, u]

for each u ∈R.
The density of the limit measure νΛα will be denoted by fΛα, whenever this
density exists.


## Page 80


80
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
10.5. The geographic coordinate system. We will endow a continuous
diagram Λ with the system of geographic coordinates, cf. Section 2.4. For
this purpose we view the shape Λ as the following compact subset of the
(x, y)-Cartesian plane
ΛCart :=

(x, y) ∈R2 : |x −y| < x + y < Λ(x −y)
	
=

(x, y) ∈[0, ∞)2 : x + y < Λ(x −y)
	
.
(Recall that u = x −y and v = x + y are the (u, v) coordinates, cf. Sec-
tion 2.2.)
For any α ∈[0, 1] we deﬁne the quantile function for the limit measure
νΛα by the formula
(10.2)
QΛα(ψ) := inf

u ∈supp(νΛα) : FΛα(u) ≥ψ
	
for ψ ∈[0, 1]
where supp(µ) denotes the support of the measure µ. In particular, QΛ0 ≡
0.
For given α ∈[0, 1] and ψ ∈[0, 1] there is exactly one point p = (x, y) ∈
ΛCart such that
• p lies on the level curve Λα seen in the XY -coordinates system, i.e.,
x + y = Λα(x −y);
• the u-coordinate of p is given by the quantile function:
u(p) = x −y = QΛα(ψ).
We will denote this point by Pα,ψ := (xψ
α, yψ
α) ∈ΛCart. In particular, by
the deﬁnition of νΛ0 = δ0 we have P0,ψ = (0, 0) ∈R2 for any ψ ∈[0, 1].
Additionally we denote by
uψ
α := xψ
α −yψ
α
and
vψ
α := xψ
α + yψ
α
the u- and v-coordinate of the point Pα,ψ.
We will refer to the mapping [0, 1]2 ∋(α, ψ) 7→Pα,ψ ∈ΛCart as to the
geographic coordinates system.
Remark 10.3. There may be some problem with deﬁning the counterparts
of the longitude and the latitude (the geographic coordinates) of the point
p ∈ΛCart like we did in Section 2.4. We deﬁned the latitude as the unique
α ∈[0, 1] for which p lies on the level curve hα (more precisely, on the
restriction of the level curve hα to the support of the corresponding cotran-
sition measure να). We are not sure if such uniqueness holds in a general
case when Λ is an arbitrary continuous diagram. To make things worse,
the deﬁnition of the longitude depends on the limit measure νΛα(p) corre-
sponding to the α(p)-level curve (circle of latitude with the latitude α(p),
cf. Sections 2.2 and 2.4). In the worst scenario, not only we shall pick some


## Page 81


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
81
latitude α(p), but also the limit measure νΛα(p) may have atoms. In partic-
ular, an attempt of using these direct counterparts of the deﬁnitions from
Section 2.4 in the more general context may lead to the situation in which
several points have the same geographic coordinates or some geographic
coordinates (α, ψ) are not used. The case of the L-shape diagram, see Fig-
ure 10, is an example of the ﬁrst problem.
Problem 10.4. Let Λ be a continuous diagram. Show that for any point
p ∈ΛUV :=

(u, v) : u ∈R and |u| < v < Λ(u)
	
there is a unique α ∈[0, 1] with the property that
p ∈

(u, Λα(u)) : u ∈supp(νΛα)
	
.
In other words, show that for any point p ∈ΛUV there exists a unique
level curve Λα (for some α ∈[0, 1]) which restricted to the support of the
corresponding cotransition measure νΛα contains p.
10.6. Extension of the main results.
Theorem 10.5. Let (λN) fulﬁll the assumptions in Section 10.2) and assume
that
(⋆) the geographic coordinates system is continuous, i.e., the map [0, 1]2 ∋
(α, ψ) 7→Pα,ψ, is continuous.
Then the analogues of Theorems 2.3 and 2.4 hold true, i.e., if TN is a
uniformly random element of TλN then:
• there exists a family of random variables ΨN : TλN →[0, 1] indexed
by N ∈N such that
(10.3)
sup
t∈[0,1]
Xt(TN) −P1−t,ΨN(TN)
 P−→0,
• there exists a family of random variables eΨN : TλN →[0, 1] indexed
by N ∈N such that
sup
t∈[0,1]

1
N q⌈t|λN |⌉(TN) −Pt,eΨN(TN )

P−→0.
The probability distribution of the random variable ΨN (respectively,
eΨN) converges, as N →∞, to the uniform distribution on the unit inter-
val [0, 1].
Proof. The proof of Theorem 2.3 is applicable in this more general case
– one shall replace all occurrences of the □N by λN and change the refer-
ences to the limit measures. We enumerate the properties of square Young
diagrams which played the crucial role in the proof of Theorem 2.3.


## Page 82


82
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
• □N is a 1-balanced Young diagram (we used this property in Propo-
sition 5.1 and Theorem 6.2);
• the cotransition measure να corresponding to the level curve hα has
no atoms and has a connected support (we used this property in
Theorem 4.1 and Proposition 5.1);
• the distribution of uα – the u-coordinate of the surfer in time α –
converges to the cotransition measure ν1−α (we used this property
in Lemma 8.1);
• the uniform continuity of the geographic coordinates system, i.e.,
the uniform continuity of the mapping (α, ψ) 7→Pα,ψ, cf. Lemma 8.2.
Notice that the counterparts of all these properties are present in our new
setting. In particular, the distribution of the u-coordinate of the surfer con-
verges to the proper limit measure since the correspondence between the
(centered) continuous diagrams of ﬁxed positive area and the cotransition
measures is a homeomorphism, cf. Section 10.4.2. Moreover, the assump-
tion (⋆) on the continuity of the geographic coordinates system assures that
for any α ∈[0, 1] the support of the limit measure νΛα is connected.
□
10.7. Example: random rectangular tableaux. For any real numbers a, b > 0
let □a×b denote the rectangle with the left bottom corner positioned in
(0, 0) ∈R2 and with sides a and b (on X and Y axis, respectively, when
seen in the (x, y)-coordinates system).
Let (Mi) and (Ni) be two sequences of positive integers which fulﬁll the
conditions from Section 1.1.3, i.e., Mi →∞and Ni →∞, and there is
some (shape parameter) θ > 0 such that
lim
i→∞
Mi
Ni
= θ.
We deﬁne for i ∈N
λi := □Mi×Ni
to be the rectangular Young diagram which has Mi rows and Ni columns.
The following theorem generalizes Theorem 2.4 (which is a special case
for Mi = Ni = i).
Corollary 10.6. For i ∈N let Ti be a uniformly random tableau of the
shape □Mi×Ni. Then the rescaled lazy sliding path
1
√MiNiq(Ti) with respect
to the supremum norm converges in probability to the random function
(10.4)
t 7→ΞS(t) = 2
p
t(1 −t) S + θ −1
√
θ
t
where S denotes the random variable with the standard semicircular distri-
bution, cf. (1.3).


## Page 83


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
83
Proof. We will check that the assumptions of Theorem 10.5 are fulﬁlled
and ﬁnd the explicit formula for the geographic coordinates system.
Clearly, the sequence

1
√MiNi□Mi×Ni

converge to the limit shape Λ =
□√
θ×1/
√
θ. We apply Lemma 10.7 below with a := 1/
√
θ and b :=
√
θ to
see that
• the geographic coordinates system on □√
θ×1/
√
θ is continuous,
• for any ψ ∈[0, 1] and α ∈[0, 1] the ψ-th quantile uψ of the cotran-
sition measure νΛα is given by
uψ = 2
p
α(1 −α)F −1
SC (ψ) + θ −1
√
θ
α
where FSC denotes the cumulative distribution function of the stan-
dard semicircle distribution, cf. (1.3).
Notice that if U is a random variable with the uniform U(0, 1) distribution
then F −1
SC (U) has the standard semicircle distribution.
By Theorem 10.5 (its second and third part) the (rescaled) lazy sliding
path
1
√MiNiq(Ti) with respect to the supremum norm converges in probabil-
ity to the random function (10.4).
□
Lemma 10.7. Let a, b > 0 and Λ := ω□a×b be the proﬁle of □a×b. Then for
any α ∈(0, 1) the cotransition measure νΛα corresponding to the α-level
curve Λα has the density
(10.5)
fνΛα(x) =
1
2
p
ab · α(1 −α)
fSC
 
x + α(a −b)
2
p
ab · α(1 −α)
!
where fSC is the density of the standard semicircular distribution, cf. (1.3).
Proof. The following calculations use (10.1) and some relations between
the R-transform and the Cauchy transform of the appropriate transition mea-
sures, see [MS17, Section 3] for the theory.
The Cauchy transform of the transition measure µΛ of the rectangular
diagram is given by [Rom04, Equation (2)]
(10.6)
G(z) := GµΛ(z) =
z −(b −a)
(z + a)(z −b).
It is an analytic function and in some neighborhood of ∞it is invertible
[MS17, Section 3, Theorem 17(i)]. Moreover, there exists a neighborhood
U ⊂C of 0 for which G|G−1(U) is invertible [MS17, Section 3, Theo-
rem 17(ii)] and we can calculate the R-transform of the measure µΛ with
the formula [MS17, Section 3, Theorem 17(iii)]
R(z) := RµΛ(z) = G−1(z) −1
z
for z ∈U \ {0}.


## Page 84


84
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
Substituting in the latter z with G(z′) (for some z′ ∈G−1(U \ {0})) we get
the relation
(10.7)
z = R
 G(z)

+
1
G(z)
for z ∈G−1(U \ {0}).
We use this equality in order to substitute each occurrence of the variable z
on the right-hand side of (10.6); by clearing of the denominator we obtain
(10.8) R(G) + 1
G −(b −a) = G ·

R(G) + 1
G + a

R(G) + 1
G −b

,
where we used the shorthand notation G = G(z). By the choice of U as
the neighborhood of 0 we get that (10.8) is fulﬁlled with G replaced by any
complex number z ∈U \ {0}, i.e., the R-transform fulﬁlls the following
quadratic equation for any z ∈U \ {0}
(10.9)
R(z) + 1
z −(b −a) = z ·

R(z) + 1
z + a

R(z) + 1
z −b

.
Now, we will calculate the Cauchy transform of the transition measure µΛα
on the level curve Λα. Denote by Rα and Gα, respectively, the R-transform
and the G-transform of µΛα. The R-transforms of the transition measures
µΛ and µΛα are related by the following correspondence [Bia98, Theo-
rem 1.2]
Rα(z) := RµΛα(z) = R(α · z)
for z ∈U \ {0}.
Let us put α · z instead of z in (10.9) (this substitution is legal since the
neighborhood U can be taken to be a convex set). Equation (10.9) implies
therefore that Rα(z) is a solution to the following quadratic equation
(10.10)
Rα(z) + 1
αz −(b −a) =
αz

Rα(z) + 1
αz + a

Rα(z) + 1
αz −b

for any z ∈U \ {0}.
In (10.10) we substitute each occurrence of the variable z by Gα(z); this
substitution is valid as long as |z| is big enough so that Gα(z) ∈U \ {0}.
Let us denote additionally Hα =
1
Gα; then we use the relation (10.7) and
substitute each occurrence of Rα
 Gα(z)

by z −Hα(z). Then (10.10) takes


## Page 85


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
85
the form
(10.11)
Hα(z)
 
z −(b −a) +
 1
α −1

Hα(z)
!
=
α
 
z + a +
 1
α −1

Hα(z)
! 
z −b +
 1
α −1

Hα(z)
!
which holds if |z| is big enough. For any z big enough, the latter is a qua-
dratic equation in Hα(z) which has two solutions given by explicit (but
complicated, so we omit writing them here) formulas. These solutions come
from two branches of the complex square root. The function Hα must be
analytic in some neighborhood of ∞and therefore can be given by only one
(family) of these solutions. Moreover, Hα must have a proper asymptotics,
more precisely [MS17, Section 3.1, Lemma 3]
lim
y→∞
Hα(iy)
y
= i,
which allows us to choose the proper solution.
The formula for Hα gives also an explicit formula for the Cauchy trans-
form of the cotransition measure νΛα on the level curve Λα as (cf. (10.1))
GνΛα(z) =
1
αab
 z −Hα(z)

.
The function GνΛα is analytic (since Hα is analytic); we will use its analytic
continuation to the upper halfplane C+.
With this (complicated) formula for GνΛα we can now recover the density
of the cotransition measure νΛα using the Stieltjes inversion formula [MS17,
Section 3, Theorem 6]. One can easily show that this density is the properly
rescaled and translated standard semicircle distribution, cf. (1.3).
□
10.8. What if the geographic coordinates system is not uniformly con-
tinuous? The situation when the geographic coordinates system (α, ψ) 7→
Pα,ψ ∈ΛCart (recall Section 10.5) is not uniformly continuous is not rare.
One among many examples is the limit shape Λ which is the L-shape,
cf. Figure 10. In this case there are some α-level curves (for α big enough)
for which the corresponding cotransition measure is supported on two dis-
joint intervals. This forces the function ψ 7→Pα,ψ to have a discontinuity
related to the hole between the intervals. Therefore in such situation Theo-
rem 10.5 does not apply since the assumption (⋆) is not fulﬁlled.
Problem 10.8. Find a counterpart of the assumption (⋆) for which the con-
clusion of Theorem 10.5 holds true.


## Page 86


86
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
u
u
−5
−4
−3
−2
−1
0
1
2
3
4
5
Figure 15. Above: the Young diagram (4, 4, 2) and its
marked inner corner in the second row. In the middle: the
corresponding conﬁguration of particles on the shifted lat-
tice Z′ via Rost’s mapping. The marked inner corner cor-
responds to the pair of nodes in the rectangle. Below: the
corresponding conﬁguration of particles (including the sec-
ond class particle) on the lattice Z.
11. THE CORRESPONDENCE BETWEEN YOUNG TABLEAUX AND
PARTICLE SYSTEMS. PROOF OF THEOREM 1.1
We will ﬁrst describe a bijection which links a recording tableau with a
unique history of a particular Totally Asymmetric Simple Exclusion Pro-
cess, recall Section 1.1. We will base on the articles of Rost [Ros81], as
well as Romik and the second named author [R´S15, Section 7]. Then, in
Section 11.3 we will prove Theorem 1.1.
11.1. The correspondence between a Young diagram with a distinguished
corner and a conﬁguration of particles – Rost’s mapping. Let λ be a
non-empty Young diagram and □be one of its inner corners, i.e., □is a
cell of λ such that the shape λ \ □is still a Young diagram, see Figure 15.
Following [R´S15, Section 7.1], we will present the two-step algorithm in
which to the pair (λ, □) we assign a conﬁguration of holes and particles
with exactly one second class particle. To our best knowledge the founda-
tions for this mapping were ﬁrst laid in [Ros81, Remark 1], and therefore
we will call it Rost’s mapping.
In the ﬁrst step of the Rost’s mapping, given a Young diagram λ we
draw its proﬁle ωλ in the Russian coordinates system (see Figure 14 and


## Page 87


SECOND CLASS PARTICLES, EVACUATION AND SLIDING PATHS
87
Section 10.1 for the deﬁnition of the proﬁle). To the proﬁle ωλ there corre-
sponds a unique conﬁguration of holes and (ﬁrst class) particles on Z′ :=
Z + 1
2 which appears in the following way. For each m ∈Z exactly one of
the following two cases holds true:
• in the case when the slope of the proﬁle ωλ on the interval [m, m+1]
is equal to −1 then we put a (ﬁrst class) particle at the site m + 1
2 of
the lattice Z′ := Z + 1
2;
• in the case when the slope of the proﬁle ωλ on the interval [m, m+1]
is equal to +1 then we put a hole at the site m + 1
2 (in other words,
the site m + 1
2 is vacant).
The distinguished inner corner □corresponds in the above particle system
to a hole–particle pair. We outline this hole–particle pair with a red rectan-
gle, see the top and the middle part of Figure 15.
In the second step of Rost’s mapping we deﬁne a particle conﬁguration
on Z. We start with merging the hole–particle pair outlined in the red rec-
tangle into the single particle which we will call the second class particle.
We put it in the middle of the initial interval containing the hole-particle
pair. Then we translate all holes and particles which are placed to the left
of the second class particle by + 1
2 and we translate all holes and particles
which are placed to the right of the second class particle by −1
2. These steps
are illustrated in the middle and bottom part of Figure 15. In this way we
end up with the conﬁguration of particles on Z with a single second class
particle.
11.2. The correspondence between the standard tableaux and the histo-
ries of TASEP. Recall that for a standard tableau T and a positive integer
p ≤|T| we deﬁne the restricted tableau T|≤p to be the tableau which con-
sists of only these boxes of T which have entries ≤p.
For a standard tableau T with n ≥1 boxes and any p ∈{1, . . . , n} let us
deﬁne
λ(p) := λ(p)(T) := sh
 T|≤p

,
□(p) := □(p)(T) := qp(T),
that is,
 λ(p), □(p)
is the pair which consists of the Young diagram λ(p)(T)
which is the shape of the restricted tableau T|≤p and the last box along the
sliding path in T which contains a number ≤p, cf. Section 2.6.
Let T be a standard tableau with n ≥1 boxes. For any t ∈{1, . . . , n} let
us consider the system of particles Pt := Pt(T) which corresponds to the
pair (λ(t), □(t)) via Rost’s mapping deﬁned in Section 11.1. Notice that the
initial conﬁguration P1 is such that the second class particle is located at the
site u = 0, all negative nodes are occupied by the ﬁrst class particles and


## Page 88


88
ŁUKASZ MA´SLANKA AND PIOTR ´SNIADY
all positive nodes are occupied by holes. Such conﬁguration is called the
Dirac sea. Observe that for any t ∈{1, . . . , n −1} the neighboring states
Pt and Pt+1 differ by one of the three transitions described in Section 1.1.1
(cf. Figure 2, see [R´S15, Sections 7.2 and 7.3] for a step-by-step proof).
Therefore the family (Pt)t∈{1,...,n} is a history of the particle system starting
from the Dirac sea.
Given the above observation, it is easy to see that the mapping which to
the standard tableau T with n boxes associates the history
 Pt(T)

t∈{1,...,n}
of the particle system is a bijection between the set of standard tableaux
with n boxes and the possible n-step histories of particle systems starting
from the Dirac sea. Moreover, for a tableau T and any t ∈{1, . . . , |T|}
the u-coordinate of the box qt(T) in the lazy sliding path is the position of
the second class particle in time t in the corresponding TASEP, see [R´S15,
Proposition 7.1].
11.3. Proof of Theorem 1.1.
Proof of Theorem 1.1. Let us denote by TM×N the set of standard tableaux
of M × N rectangular shape (where M is a number of rows and N is a
number of columns).
In the following we discard the particles and holes which do not occupy
the nodes (1.1). In this way the correspondence deﬁned in Section 11.2
gives a bijection between TMi×Ni and the set of histories of the particle
system considered in Section 1.1.1. In this correspondence for any t ∈
{1, . . . , MiNi} the position of the second class particle in time t in the
TASEP corresponds to the u-coordinate of the box qt(T) in the lazy sliding
path. In the special case Mi = Ni = i when Mi × Ni = □i an appli-
cation of Theorem 2.4 completes the proof. In the general case we apply
Corollary 10.6 instead.
□
ACKNOWLEDGMENTS
Research is supported by Narodowe Centrum Nauki, grant number
2017/26/A/ST1/00189. We thank Dan Romik and Serban Belinschi for
valuable discussions.
REFERENCES
[AHRV07]
O. Angel, A. E. Holroyd, D. Romik, and B. Virág. “Random
sorting networks”. In: Adv. Math. 215.2 (2007), pp. 839–868.
DOI: 10.1016/j.aim.2007.05.019.
[BF87]
A. Benassi and J.-P. Fouque. “Hydrodynamical limit for the
asymmetric simple exclusion process”. In: Ann. Probab. 15.2
(1987), pp. 546–560. DOI: 10.1214/aop/1176992158.


## Page 89


REFERENCES
89
[Bia01]
P. Biane. “Approximate factorization and concentration for char-
acters of symmetric groups”. In: Internat. Math. Res. Notices 4
(2001), pp. 179–192. DOI: 10.1155/S1073792801000113.
[Bia98]
P. Biane. “Representations of symmetric groups and free prob-
ability”. In: Adv. Math. 138.1 (1998), pp. 126–181. DOI: 10.1006/aima.1998.1745
[Bur48]
J. M. Burgers. “A mathematical model illustrating the theory
of turbulence”. In: Advances in Applied Mechanics. edited by
Richard von Mises and Theodore von Kármán, Academic Press,
Inc., New York, 1948, pp. 171–199.
[CSST10]
T. Ceccherini-Silberstein, F. Scarabotti, and F. Tolli. Represen-
tation theory of the symmetric groups. Vol. 121. Cambridge
Studies in Advanced Mathematics. The Okounkov-Vershik ap-
proach, character formulas, and partition algebras. Cambridge:
Cambridge University Press, 2010, pp. xvi+412.
[Dur10]
R. Durrett. Probability: theory and examples. Fourth. Cam-
bridge Series in Statistical and Probabilistic Mathematics. Cam-
bridge: Cambridge University Press, 2010, pp. x+428.
[DV20]
D. Dauvergne and B. Virág. “Circular support in random sort-
ing networks”. In: Trans. Amer. Math. Soc. 373.3 (2020), pp. 1529–
1553. DOI: 10.1090/tran/7819.
[Fer92]
P. A. Ferrari. “Shock ﬂuctuations in asymmetric simple exclu-
sion”. In: Probab. Theory Related Fields 91.1 (1992), pp. 81–
101. DOI: 10.1007/BF01194491.
[FF94]
P. A. Ferrari and L. R. G. Fontes. “Current ﬂuctuations for the
asymmetric simple exclusion process”. In: Ann. Probab. 22.2
(1994), pp. 820–832. DOI: 10.1214/aop/1176988731.
[FK95]
P. A. Ferrari and C. Kipnis. “Second class particles in the rar-
efaction fan”. In: Ann. Inst. H. Poincaré Probab. Statist. 31.1
(1995), pp. 143–154. URL: http://www.numdam.org/item?id=AIHPB_1995__
[F´S11]
V. Féray and P. ´Sniady. “Asymptotics of characters of symmet-
ric groups related to Stanley character formula”. In: Ann. of
Math. (2) 173.2 (2011), pp. 887–906. DOI: 10.4007/annals.2011.173.2.6.
[Ful97]
W. Fulton. Young tableaux. Vol. 35. London Mathematical So-
ciety Student Texts. With applications to representation theory
and geometry. Cambridge University Press, Cambridge, 1997,
pp. x+260.
[Gre74]
C. Greene. “An extension of Schensted’s theorem”. In: Ad-
vances in Math. 14 (1974), pp. 254–265. DOI: 10.1016/0001-8708(74)90031-0.
[Juc74]
A.-A. A. Jucys. “Symmetric polynomials and the center of
the symmetric group ring”. In: Rep. Mathematical Phys. 5.1
(1974), pp. 107–112.


## Page 90


90
REFERENCES
[Ker93a]
S. Kerov. “The asymptotics of interlacing sequences and the
growth of continual Young diagrams”. In: vol. 205. Nauka,
St. Petersburg, 1993, pp. 21–29, DOI: 10.1007/BF02362775.
[Ker93b]
S. V. Kerov. “Transition probabilities of continual Young di-
agrams and the Markov moment problem”. In: Funktsional.
Anal. i Prilozhen. 27.2 (1993), pp. 32–49, 96. DOI: 10.1007/BF01085981.
[Ker98]
S. Kerov. “Interlacing measures”. In: Kirillov’s seminar on
representation theory. Vol. 181. Amer. Math. Soc. Transl. Ser.
2. Amer. Math. Soc., Providence, RI, 1998, pp. 35–83. DOI:
10.1090/trans2/181/02.
[KP21]
R. Kenyon and I. Prause. Gradient variational problems in R2.
2021. arXiv: 2006.01219 [math.AP].
[Lig99]
T. M. Liggett. Stochastic interacting systems: contact, voter
and exclusion processes. Vol. 324. Grundlehren der Mathe-
matischen Wissenschaften [Fundamental Principles of Mathe-
matical Sciences]. Springer-Verlag, Berlin, 1999, pp. xii+332.
DOI: 10.1007/978-3-662-03990-8.
[MG05]
T. Mountford and H. Guiol. “The motion of a second class
particle for the TASEP starting from a decreasing shock pro-
ﬁle”. In: Ann. Appl. Probab. 15.2 (2005), pp. 1227–1259. DOI:
10.1214/105051605000000151.
[MS17]
J. A. Mingo and R. Speicher. Free probability and random
matrices. Vol. 35. Fields Institute Monographs. Springer, New
York; Fields Institute for Research in Mathematical Sciences,
Toronto, ON, 2017, pp. xiv+336. DOI: 10.1007/978-1-4939-6942-5.
[M´S20]
Ł. Ma´slanka and P. ´Sniady. “Limit shapes of evacuation and
jeu de taquin paths in random square tableaux”. In: Sém. Lothar.
Combin. 84B (2020), Art. 8, 12. URL: https://www.mat.univie.ac.at/~slc/
[PR07]
B. Pittel and D. Romik. “Limit shapes for random square Young
tableaux”. In: Adv. in Appl. Math. 38.2 (2007), pp. 164–209.
DOI: 10.1016/j.aam.2005.12.005.
[PW11]
S. Pon and Q. Wang. “Promotion and evacuation on standard
Young tableaux of rectangle and staircase shape”. In: Electron.
J. Combin. 18.1 (2011), Paper 18, 18.
[Rez95]
F. Rezakhanlou. “Microscopic structure of shocks in one con-
servation laws”. In: Ann. Inst. H. Poincaré Anal. Non Linéaire
12.2 (1995), pp. 119–153. DOI: 10.1016/S0294-1449(16)30161-5.
[Rom04]
D. Romik. “Explicit formulas for hook walks on continual
Young diagrams”. In: Adv. in Appl. Math. 32.4 (2004), pp. 625–
654. DOI: 10.1016/S0196-8858(03)00096-4.


## Page 91


REFERENCES
91
[Rom06]
D. Romik. “Permutations with short monotone subsequences”.
In: Adv. in Appl. Math. 37.4 (2006), pp. 501–510. DOI: 10.1016/j.aam.2005.08.0
[Rom12]
D. Romik. “Arctic circles, domino tilings and square Young
tableaux”. In: Ann. Probab. 40.2 (2012), pp. 611–647. DOI:
10.1214/10-AOP628.
[Ros81]
H. Rost. “Nonequilibrium behaviour of a many particle pro-
cess: density proﬁle and local equilibria”. In: Z. Wahrsch. Verw.
Gebiete 58.1 (1981), pp. 41–53. DOI: 10.1007/BF00536194.
[R´S15]
D. Romik and P. ´Sniady. “Jeu de taquin dynamics on inﬁnite
Young tableaux and second class particles”. In: Ann. Probab.
43.2 (2015), pp. 682–737. DOI: 10.1214/13-AOP873.
[Sag01]
B. E. Sagan. The Symmetric Group: Representations, combina-
torial algorithms, and symmetric functions. Second. Vol. 203.
Graduate Texts in Mathematics. Representations, combinato-
rial algorithms, and symmetric functions. New York: Springer-
Verlag, 2001, pp. xvi+238. DOI: 10.1007/978-1-4757-6804-6.
[Sch61]
C. Schensted. “Longest increasing and decreasing subsequences”.
In: Canadian J. Math. 13 (1961), pp. 179–191. DOI: 10.4153/CJM-1961-015-3.
[Sch63]
M. P. Schützenberger. “Quelques remarques sur une construc-
tion de Schensted”. In: Math. Scand. 12 (1963), pp. 117–128.
[Sep01]
T. Seppäläinen. “Second class particles as microscopic charac-
teristics in totally asymmetric nearest-neighbor K-exclusion
processes”. In: Trans. Amer. Math. Soc. 353.12 (2001), pp. 4801–
4829. DOI: 10.1090/S0002-9947-01-02872-0.
[´Sni06]
P. ´Sniady. “Gaussian ﬂuctuations of characters of symmetric
groups and of Young diagrams”. In: Probab. Theory Related
Fields 136.2 (2006), pp. 263–297. DOI: 10.1007/s00440-005-0483-y.
[´Sni14]
P. ´Sniady. “Robinson–Schensted–Knuth algorithm, jeu de taquin,
and Kerov–Vershik measures on inﬁnite tableaux”. In: SIAM J.
Discrete Math. 28.2 (2014), pp. 598–630. DOI: 10.1137/130930169.
[Spi70]
F. Spitzer. “Interaction of Markov processes”. In: Advances in
Math. 5 (1970), 246–290 (1970).
[Sta99]
R. P. Stanley. Enumerative combinatorics. Vol. 2. Vol. 62. Cam-
bridge Studies in Advanced Mathematics. With a foreword
by Gian-Carlo Rota and appendix 1 by Sergey Fomin. Cam-
bridge: Cambridge University Press, 1999, pp. xii+581. DOI:
10.1017/CBO9780511609589.
[Sun18]
W. Sun. Dimer model, bead model and standard Young tableaux:
ﬁnite cases and limit shapes. 2018. arXiv: 1804.03414 [math.PR].


## Page 92


92
REFERENCES
INSTITUTE OF MATHEMATICS, POLISH ACADEMY OF SCIENCES, ´SNIADECKICH 8,
00-656 WARSZAWA, POLAND
Email address: lmaslanka@impan.pl
INSTITUTE OF MATHEMATICS, POLISH ACADEMY OF SCIENCES, ´SNIADECKICH 8,
00-656 WARSZAWA, POLAND
Email address: psniady@impan.pl

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
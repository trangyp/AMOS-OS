---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1903.11540v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1903.11540v1_Coordinate-independent_singular_perturbation_reduction_for_systems_with_three_ti

> Source: 1903.11540v1_Coordinate-independent_singular_perturbation_reduction_for_systems_with_three_ti.pdf

> Pages: 30

---


## Page 1


arXiv:1903.11540v1  [math.DS]  27 Mar 2019
Coordinate-independent singular perturbation
reduction for systems with three time scales
Niclas Kruﬀ, Sebastian Walcher
Mathematik A, RWTH Aachen
52056 Aachen, Germany
niclas.kruﬀ@matha.rwth-aachen.de,
walcher@matha.rwth-aachen.de
Abstract
On the basis of recent work by Cardin and Teixeira on ordinary diﬀer-
ential equations with more than two time scales, we devise a coordinate-
independent reduction for systems with three time scales; thus no a priori
separation of variables into fast, slow etc. is required. Moreover we con-
sider arbitrary parameter dependent systems and extend earlier work on
Tikhonov-Fenichel parameter values – i.e. parameter values from which
singularly perturbed systems emanate upon small perturbations – to the
three time-scale setting. We apply our results to two standard systems
from biochemistry.
MSC (2010): 92C45, 34E15, 37D10
Key words: Reaction network, dimension reduction, invariant set, mul-
tiple time scales.
1
Introduction and overview
Ordinary diﬀerential equations involving a small parameter appear frequently in
mathematics and in science. Their principal use in chemistry and biochemistry
– which is the main topic of the present paper – is to ﬁnd certain (attracting)
invariant sets and to achieve reduction of dimension. The mathematical basis is
singular perturbation theory, originally due to Tikhonov [18] and Fenichel [4],
for systems with one small parameter ε (or, in other words, for systems with
two time scales).
While Tikhonov’s and Fenichel’s theory is concerned with ﬁrst order approxi-
mations in ε, there exist approaches to include higher order terms in ε, e.g. to
improve accuracy in the approximation of invariant manifolds; see for instance
the critical survey in Kaper and Kaper [10]. More recently, Noel et al. [13],
Radulescu et al. [15], Samal et al. [16, 17] developed an algorithmic method
1


## Page 2


to compute slow-fast scenarios in chemical reaction networks, using tropical ge-
ometry. Concerning the existence (or persistence) of invariant sets obtained
by such (a priori formal) calculations one may invoke hyperbolicity properties;
for instance Theorem 4.1 in Chicone [1] is very useful in this respect. A di-
rect method for chemical reaction networks involving diﬀerent orders of a single
small parameter, given certain properties of the system, is due to Cappeletti
and Wiuf [2].
A diﬀerent perspective is the consideration of systems with more than two time
scales by introducing, cum grano salis, several small parameters ε1, ε2, . . ., and
to obtain invariant manifolds and reduction on this basis. (One has the option
to set all parameters equal in the end.)
Recently Cardin and Teixeira [3] generalized Fenichel’s fundamental theo-
rems, proving results on invariant sets and reductions of systems with more
than two time scales. Here, the diﬀerential equation systems are assumed to
have variables separated into blocks of fast, slow, “very slow” ones, and so on.
The present paper is based, on the one hand, on Cardin and Teixeira [3]. On
the other hand, we extend earlier work [7, 8] that is concerned with coordinate-
independent reduction (not requiring an a priori separation of slow and fast
variables), as well as with the basic question of ﬁnding – in arbitrary parameter
dependent systems – critical parameter values from which singular perturbation
reductions emanate.
We will focus on the three time-scale setting, essentially to keep notation man-
ageable, and will only brieﬂy sketch extensions to more than three time scales.
Furthermore we will mostly consider systems that satisfy not only the normal
hyperbolicity conditions from [3] but have the stronger feature of exponential at-
tractivity. One reason for this restriction lies in our interest in chemical reaction
networks. But beyond this practical consideration, the algorithms to compute
critical parameter values for singular perturbation scenarios indeed requires this
additional property.
The paper is organized as follows. In Section 2 we review the work by Cardin
and Teixeira [3]. Section 3 generalizes the coordinate-independent reduction al-
gorithm from [7] to three-timescale systems. In Section 4 we start from a general
parameter dependent system and extend the work from [8] on critical parame-
ter values (Tikhonov-Fenichel parameter values) to three time scales (resp. two
“small parameters”), and in Section 5 we discuss two classical examples (co-
operativity with two complexes, competitive inhibition) from biochemistry in
detail. Section 6 contains a few remarks about more than three time scales, and
ﬁnally, for the reader’s convenience, we prove some essentially known facts in
an Appendix.
2


## Page 3


2
Separated fast and slow variables
In this section we review and specialize results from Cardin and Teixeira [3] for
a parameter dependent ordinary diﬀerential equation system
(1)
˙x1
=
f1(x, ε1, ε2)
˙x2
=
ε1f2(x, ε1, ε2)
˙x3
=
ε1ε2f3(x, ε1, ε2)
;
brieﬂy ˙x = f(x, ε1, ε2).
Here x = (x1, x2, x3)tr ∈Rn with x1 ∈Rn1, x2 ∈Rn2, and x3 ∈Rn3, and f is
smooth on an open neighborhood of U × [0, δ1) × [0, δ2), with U ⊆Rn open and
nonempty, and δ1 > 0, δ2 > 0.
We deﬁne
(2)
M1 := {x ∈U; f1(x, 0, 0) = 0}
and
(3)
M2 := {x ∈U; f1(x, 0, 0) = f2(x, 0, 0) = 0} ,
and we will assume throughout that these sets are nonempty.
Cardin and
Teixeira require some hyperbolicity conditions, which we state here in slightly
stronger versions, for the sake of simplicity:
• First hyperbolicity condition: For every x ∈M1, all the eigenvalues of
Dx1f1(x, 0, 0)1 have nonzero real parts.
For suﬃciently small ε1, ε2 this condition implies local solvability of the
implicit equation f1(x, ε1, ε2) = 0 in the form x1 = g(x2, x3, ε1, ε2), and
one may furthermore write
f2(x, ε1, ε2) = ef2(x2, x3, ε1, ε2) := f2(g(x2, x3, ε1, ε2), x2, x3, ε1, ε2).
• Second hyperbolicity condition: For every x ∈M2, all the eigenvalues of
Dx2 ef2(x, 0, 0) have nonzero real parts.2
By suitable choice of U, δ1 and δ2 we may assume that M1 and M2 are sub-
manifolds.
Continuing to follow [3] we introduce the auxiliary system
(4)
0
=
f1(x, 0, ε2)
˙x2
=
f2(x, 0, ε2)
˙x3
=
ε2f3(x, 0, ε2)
on
Mε2
2 := {x ∈U; f1(x, 0, ε2) = 0} ,
1For a smooth function g = g(x, y, . . .) we denote the partial derivatives by Dxg, Dyg etc.
2In [3] the second hyperbolicity condition is erroneously written for f2 rather than ef2. The
authors are aware of this and will publish a corrigendum.
3


## Page 4


and the intermediate reduced system
(5)
0
=
f1(x, 0, 0)
˙x2
=
f2(x, 0, 0)
˙x3
=
0
on M1. In both equations (4) and (5) above the dot denotes diﬀerentiation with
respect to τ2 := ε1t. By suitable choice of δ2 we may also assume that every
Mε2
2 is a submanifold of Rn.
Finally we deﬁne the completely reduced system
(6)
0
=
f1(x, 0, 0)
0
=
f2(x, 0, 0)
˙x3
=
f3(x, 0, 0)
on M2, where the dot in (6) denotes diﬀerentiation with respect to τ3 := ε1ε2t.
We replace the hyperbolicity conditions from [3] by stronger requirements,
since in our applications we focus on attracting invariant manifolds.
Deﬁnition 1. We say that system (1) satisﬁes the hyperbolic attractivity con-
dition (HA) if Dx1f1(x, 0, 0) has only eigenvalues with negative real part on M1
and if furthermore Dx2 ef2(x, 0, 0) has only eigenvalues with negative real part on
M2.
Our starting point is the following theorem, specialized from Cardin and
Teixeira [3], Theorems A, B and Corollary A. Some of our statements are infor-
mal; for rigorous statements and pertinent deﬁnitions we refer to [3].
Theorem 1. Let system (1) be given, with (HA) satisﬁed.
(a) Let N ⊆M2 be a compact submanifold (with nonempty interior in the rel-
ative topology, and possibly with boundary). Then for all suﬃciently small
ε1, ε2 there exists a locally invariant manifold Nε1,ε2 for system (1) which is
O(ε1 + ε2) close to N, diﬀeomorphic to N and locally exponentially attract-
ing. Given the appropriate time scales, solutions of (1) on Nε1,ε2 converge
to solutions of (6) on N.
(b) Let ε2 be suﬃciently small and let L ⊆Mε2
2
be a compact submanifold
(with nonempty interior in the relative topology, and possibly with bound-
ary). Then for all suﬃciently small ε1 there exists a locally invariant man-
ifold Lε1,ε2 for system (1) which is O(ε1 + ε2) close to L, diﬀeomorphic to
L and locally exponentially attracting. Given the appropriate time scales,
solutions of (1) on Lε1,ε2 converge to solutions of (5) on L.
As given, the part regarding ef2 in condition (HA) is not ready to use in
applications. We provide two equivalent versions.
Proposition 1. Condition (HA) is equivalent to either of the following condi-
tions.
4


## Page 5


(i) Dx1f1(x, 0, 0) has only eigenvalues with negative real parts on M1, and
B1(x) := −Dx1f2(x, 0, 0)Dx1f1(x, 0, 0)−1Dx2f1(x, 0, 0) + Dx2f2(x, 0, 0)
has only eigenvalues with negative real parts on M2.
(ii) Dx1f1(x, 0, 0) has only eigenvalues with negative real parts on M1, and
for all suﬃciently small ε > 0 the matrix
B2(x, ε) :=
 Dx1f1(x, 0, 0)
Dx2f1(x, 0, 0)
εDx1f2(x, 0, 0)
εDx2f2(x, 0, 0)

has only eigenvalues with negative real parts on M2.
Proof. We use the notions introduced with the hyperbolicity condition (H) and
Deﬁnition 1. From
f1(g(x2, x3, ε1, ε2), x2, x3, ε1, ε2) = 0
one gets by the chain rule
Dx2g(x2, x3) = −Dx1f1(x, , ε1, ε2)−1Dx2f1(x, , ε1, ε2)
when f1(g(x2, x3, ε1, ε2), x2, x3, ε1, ε2) = 0, and a further application of the
chain rule shows the equivalence of (HA) and (i). The equivalence of (i) and (ii)
follows from Lemma 3 in the Appendix.
Remark 1. (a) One may rewrite systems (1) through (6) to some extent, with
no eﬀect on the reductions. Using Hadamard’s lemma, one may restate (1)
as
˙x1
=
bf1(x, ε2)
+ε1 bf1,1(x, ε1)
+ε1ε2 bf1,2(x, ε1, ε2)
˙x2
=
ε1 bf2(x, ε1)
+ε1ε2 bf2,2(x, ε1, ε2)
˙x3
=
ε1ε2 bf3(x, ε1, ε2)
with only the bfi remaining in the subsequent reductions. Thus the auxiliary
system becomes
0
=
bf1(x, ε2)
˙x2
=
bf2(x, 0)
˙x3
=
ε2f3(x, 0, ε2)
and there are analogous modiﬁcations for the intermediate and the fully
reduced system.
(b) The passage from (1) to the completely reduced system (6) can evidently be
obtained in the following manner: Fix ε1 > 0 and reduce (1) with respect to
the small parameter ε2 (in time scale ε2t). Then let ε1 →0, rescaling time
once more to τ3. We will use this observation later on.
5


## Page 6


3
Coordinate-free reduction
In the present section we generalize the coordinate-independent reduction proce-
dure from [14, 7] to the three-timescale setting. The ﬁrst task is to intrinsically
characterize those systems which admit a transformation to “standard form”
(1). Reversing matters, applying a (local) smooth coordinate transformation to
equation (1) yields a smooth system
(7)
˙x = g(0,0)(x, ε1, ε2) + ε1

g(1,0)(x, ε1, ε2) + ε2g(1,1)(x, ε1, ε2)

on an open neighborhood of eU × [0, δ1) × [0, δ2) ⊆Rn × R × R (eU ⊆Rn open),
evidently satisfying the following conditions:
(i) For all suﬃciently small ε1 ≥0, ε2 ≥0, the zeros of g(0,0)(x, ε1, ε2) form a
submanifold f
M1 ⊆eU, of codimension n1, 1 ≤n1 < n. Given any compact
submanifold P1 ⊆f
M1, there exists θ1 > 0 such that at every y ∈P1
the derivative Dxg(y, ε1, ε2) admits the eigenvalue zero with algebraic and
geometric multiplicity n −n1, and the remaining eigenvalues have real
parts ≤−θ1.
(ii) For all suﬃciently small ε1 > 0, ε2 ≥0 the zeros of
g(0,0)(x, ε1, ε2) + ε1g(1,0)(x, ε1, ε2)
form a submanifold g
M2 ⊆eU, of codimension n1 + n2, 1 ≤n2 < n −
n1.
Moreover, for any compact submanifold P2 ⊆f
M2 there exists a
θ2 > 0 with the following property: At every y ∈P2 the derivative
Dxg(0,0)(y, ε1, ε2) + ε1Dxg(1,0)(y, ε1, ε2) admits the eigenvalue zero with
algebraic and geometric multiplicity n−n1 −n2, and the remaining eigen-
values have real parts ≤−θ2ε1.
By Remark 1 one may assume that system (7) is in the special form
(8)
˙x = g(0,0)(x, ε2) + ε1

g(1,0)(x, ε1) + ε2g(1,1)(x)

+ O(ε2(ε1 + ε2)),
adjusting conditions (i) and (ii) accordingly. Conditions (i) and (ii) are certainly
necessary for (7) or (8) to be a transformed version of (1). The ﬁrst part of the
next lemma shows suﬃciency.
Lemma 1. (a) There exists a local diﬀeomorphism transforming system (8) to
a system of type (1) with condition (HA) if and only if conditions (i) and
(ii) above hold.
(b) Condition (i) for system (8) is equivalent to the following: For any y ∈g
M1
there exist a neighborhood U1,y, a smooth map P1 : U1,y →Rn×n1 such
that P1(y, ε2) has rank n1, and a smooth map µ1 : U1,y →Rn1 such that
Dxµ1(y, ε2) has rank n1, yielding a decomposition
g(0,0)(x, ε2) = P1(x, ε2)µ1(x, ε2),
6


## Page 7


and moreover there is a θ1 > 0 such that
A1(x, ε2) := Dµ1(x, ε2)P1(x, ε2)
has only eigenvalues with real part ≤−θ1, for all x ∈U1,y.
(c) In presence of condition (i), condition (ii) for system (8) is equivalent to
the following: For every (suﬃciently small) ε1 > 0 and any y ∈g
M2 there
exist a neighborhood U2,y, a smooth map P2 : U2,y →Rn×n2 such that
(P1(y, ε2), ε1P2(y, ε1)) has rank n1+n2, and a smooth map µ2 : U2,y →Rn2
such that (Dxµ1(y, ε2), Dxµ2(y, ε2))tr has rank n1 + n2, yielding a decom-
position
g(0,0)(x, ε2) + ε1g(1,0)(x, ε1) = P1(x, ε2)µ1(x, ε2) + ε1P2(x, ε1)µ2(x, ε1),
and moreover there is a θ2 > 0 such that
A2(x, ε1, ε2) :=
Dµ1(x, ε2)
Dµ2(x, ε1)
  P1(x, ε2)
ε1P2(x, ε1)
has only eigenvalues with real part ≤−θ2ε1, for all x ∈U2,y.
Proof. The nontrivial assertion of part (a) follows from the existence of n −n1
independent ﬁrst integrals of g(0,0) in a neighborhood of y, which was noted by
Fenichel [4], Lemma 5.3 for smooth vector ﬁelds, and shown in [14], Proposition
2.2 for the analytic setting, and likewise from the existence of n −n1 −n2
independent ﬁrst integrals of g(0,0) + ε1g(1,0) in a neighborhood of y. These
ﬁrst integrals determine slow and “very slow” variables. Parts (b) and (c) are
straightforward applications of [7], Theorem 1, Remark 4 and Remark 2.
Remark 2. The existence of the decomposition g(0,0) = P1 µ1 in part (b) (as
well as the decomposition in part (c)) is a consequence of the implicit function
theorem in the smooth or analytic case. For polynomial or rational vector ﬁelds
there exists a decomposition with rational functions as entries of P1 and µ1, and
there is an algorithmic approach to its computation. See [7] for details.
Next we use the decompositions to compute reductions.
Proposition 2. (a) In arbitrary coordinates the reduction corresponding to the
passage from system (1) to the auxiliary system may be obtained as follows:
Given ε2 ≥0, determine the projection matrix
Q1(x, ε2) := In −P1(x, ε2)A1(x, ε2)−1Dxµ1(x, ε2).
The auxiliary system (4) for ε2 > 0 then corresponds to
˙x = Q1(x, ε2)

g(1,0)(x, 0) + ε2g(1,1)(x)

on the local invariant manifold deﬁned by µ1(x, ε2) = 0.
The equation
corresponding to the intermediate reduced system (5) is obtained by setting
ε2 = 0.
7


## Page 8


(b) In arbitrary coordinates the reduction corresponding to the passage from
system (1) to the completely reduced system (6) may be obtained as follows:
Given ε1 > 0, determine the projection matrix
eQ2(x, ε1) := In −
 P1(x, 0),
ε1P2(x, 0)
A2(x, ε1, 0)−1
Dxµ1(x, 0)
Dxµ2(x, 0)

.
Then eQ2(x, ε1) extends smoothly to a matrix valued function Q2(x) at ε1 =
0. The equation corresponding to the completely reduced system in arbitrary
coordinates is given by
˙x = Q2(x) g(1,1)(x)
on the local invariant manifold deﬁned by µ1(x, 0) = µ2(x, 0) = 0.
Proof. Part (a) is a direct application of [7], Theorem 1.
For part (b) this
theorem is also applicable, but there is a technical problem involving eQ2 as
ε1 →0, since A2(x, 0) is non-invertible. To resolve this diﬃculty, recall that
eQ2(x, ε1) is the projection map onto the kernel of
Dxg(0,0)(x, 0) + ε1Dxg(1,0)(x, ε1)
along the image, for x ∈f
M2 (see [7], Remark 1). With the conditions given
in Lemma 1 (c) the image is equal to the column space of (P1, ε1P2), which in
turn equals the column space W1 of (P1, P2). The latter matrix has full rank
at ε1 = 0, and its entries depend smoothly on ε1 and x. Moreover the kernel is
equal to the kernel of (Dxµ1, Dxµ2)tr, and we may assume w.l.o.g. that

Dxµ1
Dxµ2

=
 A1
A2

with invertible A1, whence the kernel is equal to the column space W2 of the
matrix

−A−1
1 A2
I

with entries depending smoothly on ε1. Thus there remains to verify that the
matrix of the projection onto W2 along W1 depends smoothly on ε1. For the
sake of completeness we give a proof of this fact in Lemma 4, Appendix.
We note that the reduction also works, including convergence properties,
under the weaker assumption corresponding to (H) rather than (AH) for A1
and A2 in Lemma 1.
Remark 3. While Proposition 2 provides the reduced equations, one also needs
initial values for these, which may be obtained from an initial value y of system
8 with the help of the ﬁrst integrals noted in the proof of Lemma 1(a); see [7],
Proposition 2:
8


## Page 9


• Assuming that y is suﬃciently close to f
M1 , the corresponding initial
value (up to an error of order ε1 + ε2) for the auxiliary system and for
the intermediate reduced system is the (locally unique) intersection of f
M1
and the level sets of n −n1 independent ﬁrst integrals of ˙x = g(0,0)(x, 0)
which contain y.
• Assuming that y is suﬃciently close to f
M2 , the corresponding initial
value (up to an error of order ε1 + ε2) for the auxiliary system and for
the intermediate reduced system is the (locally unique) intersection of f
M2
and the level sets of n−n1 −n2 independent common ﬁrst integrals of ˙x =
g(0,0)(x, 0) and ˙x = g(1,0)(x, 0, 0) which contain y. (A direct application
of Proposition 2 in [7] would lead to simultaneous ﬁrst integrals of ˙x =
g(0,0)(x, 0)+ε1g(1,0)(x, ε1, 0) for all ε1. This is equivalent to the condition
stated.)
To illustrate the procedure with an example, we recall the competitive in-
hibition network with substrate S, enzyme E, inhibitor I and two complexes
C1, C2; see for instance Keener and Sneyd [11]. The reaction scheme is given
by
E + S
k1
⇋
k−1
C1
k2
⇀
E + P,
E + I
k3
⇋
k−3
C2
which leads (with the usual assumptions of mass action kinetics, spatial homo-
geneity and constant thermodynamical parameters) to the diﬀerential equation
system
(9)
˙s
=
k−1c1 −k1s(e0 −c1 −c2)
˙c1
=
k1s(e0 −c1 −c2) −(k−1 + k2)c1
˙c2
=
k3(e0 −c1 −c2)(i0 −c2) −k−3c2
for the concentrations. (The original system is ﬁve dimensional; the two linear
ﬁrst integrals e + c1 + c2 and i + c2 yield reduction to dimension three.)
Example 1. In system (9) set x = (s, c1, c2)tr and assume k2 = ε1ε2k∗
2, k3 =
ε1k∗
3 and k−3 = ε1k∗
−3.
(Coloquially speaking, binding to the inhibitor and
degradation from the inhibitor complex are slow, while degradation from the
substrate complex to enzyme and product is very slow.) This is of the type (8),
9


## Page 10


with
g(0,0)(x) =


k−1c1 −k1s(e0 −c1 −c2)
k1s(e0 −c1 −c2) −k−1c1
0

,
g(1,0)(x, ε1) =


0
0
k∗
3(e0 −c1 −c2)(i0 −c2) −k∗
−3c2

,
g(1,1)(x, ε1, ε2) =


0
−k∗
2c1
0

.
Moreover f
M2 is contained in the common zero set of
µ1 = k−1c1 −k1s(e0 −c1 −c2) and µ2 = k∗
3(e0 −c1 −c2)(i0 −c2) −k∗
−3c2,
f
M1 is contained in the zero set of µ1, and we have
P1(x, ε2) =


1
−1
0

,
P2(x, ε1) =


0
0
1

.
We determine the auxiliary system and the intermediate reduced system. With
Dµ1 = (−k1(e0 −c1 −c2, k1s + k−1, k1s)
one has
Dµ1P1 = −k1(e0 −c1 −c2 −(k1s + k−1) =: −ν1
and furthermore
Q1
=
I3 + 1
ν1


∗
k1s + k−1
k1s
∗
−(k1s + k−1)
−k1s
0
0
0


=
1
ν1


∗
k1s + k−1
k1s
∗
k1(e0 −c1 −c2)
−k1s
0
0
ν1

.
Application to
g(1,0) + ε2g(1,1) = µ2


0
0
1

−ε2k∗
2c1


0
0
1


yields the auxiliary system (in time scale ε1t) on f
M1:


˙s
˙c1
˙c2

= µ2
ν1


k1s
−k1s
ν1

−ε2
k∗
2c1
ν1


k1s + k−1
k1(e0 −c1 −c2)
0

.
10


## Page 11


Setting ε2 = 0 one obtains the intermediate reduced system.
When the initial values for system (9) are given by (s0, c1,0, c2,0), to obtain the
approximate initial values (s∗
0, c∗
1,0, c∗
2,0) on g
M1 one uses (according to Remark
3) the two ﬁrst integrals s + c1 and c2 of g(0,0) and the deﬁning equation for
g
M1, thus the system
s + c1
=
s0 + c1,0
c2
=
c2,0
k−1c1 −k1s(e0 −c1 −c2)
=
0
which leads to quadratic equations for s and c1.
To ﬁnd the fully reduced system one ﬁrst computes
Dµ2 =
 0, −k∗
3(i0 −c2), −k∗
3(e0 + i0 −c1 −2c2) −k∗
−3

and
A2
=
Dµ1
Dµ2
  P1,
ε1P2

=
−k1(e0 −c1 −c2) −k1s −k−1
ε1 · k1s
k∗
3(i0 −c2)
−ε1 · (k∗
3(e0 + i0 −c1 −2c2) + k∗
−3)

.
The computation of the projection matrix is straightforward (although a soft-
ware system is helpful) but the output is sizeable. We just record the fully
reduced system (in time scale ε1ε2t). It is given by
˙x = 1
ν2
·


ξ1
ξ2
ξ3


with
ν2 =sc1k1k∗
3 + sc2k1k∗
3 −se0k1k∗
3 −c2
1k1k∗
3 −3c1c2k1k∗
3 + 2c1e0k1k∗
3 + c1i0k1k∗
3 −2c2
2k1k∗
3
+ 3c2e0k1k∗
3 + c2i0k1k∗
3 −e2
0k1k∗
3 −e0i0k1k∗
3 −sk∗
−3k1 + c1k∗
−3k1 + c1k−1k∗
3 + c2k∗
−3k1
+ 2c2k−1k∗
3 −e0k∗
−3k1 −e0k−1k∗
3 −i0k−1k∗
3 −k∗
−3k−1
and
ξ1 =k∗
2(se0k∗
−3k1 + c1e0k−1k∗
3 −c1i0k−1k∗
3 + c2
2k−1k∗
3 −c2e0k−1k∗
3 −c2i0k−1k∗
3
+ e0i0k−1k∗
3 −c2k∗
−3k−1),
ξ2 =k1k∗
2
k∗
3
(c3
1(k∗
3)2 −2c2
1e0(k∗
3)2 + 2c2
1i0(k∗
3)2 + c1e2
0(k∗
3)2 −2c1e0i0(k∗
3)2
+ c1i2
0(k∗
3)2 + c3
2(k∗
3)2 −c2
2e0(k∗
3)2 −2c2
2i0(k∗
3)2 + 2c2e0i0(k∗
3)2 + c2i2
0(k∗
3)2 −e0i2
0(k∗
3)2
−c2
1k∗
−3k∗
3 + c1e0k∗
−3k∗
3 + 2c1i0k∗
−3k∗
3 −3c2
2k∗
−3k∗
3 + 2c2e0k∗
−3k∗
3 + 3c2i0k∗
−3k∗
3
−2e0i0k∗
−3k∗
3 + 2c2(k∗
−3)2),
ξ3 = −k∗
−3k1k∗
2
k∗
3
(c1i0k∗
3 −c2
2k∗
3 + c2e0k∗
3 + c2i0k∗
3 −e0i0k∗
3 + c2k∗
−3)
11


## Page 12


restricted to the invariant curve f
M2.
Finally, given initial values (s0, c1,0, c2,0) for system (9), approximate initial
values for the fully reduced system may be determined by solving the algebraic
equations s + c1 = s0 + c1,0, µ1 = 0 and µ2 = 0.
4
Critical parameter values
Typically in applications one starts with a general parameter dependent system,
rather than a system of type (1) or (7) with pre-assigned “small parameters”.
Therefore the ﬁrst task is to determine critical parameter values, for which
small perturbations lead to singular perturbation scenarios. Thus we consider
Tikhonov-Fenichel parameter values, as deﬁned in [8] for two time scales, and
extend the notion to the three time scale setting.
4.1
Tikhonov-Fenichel parameter values
Tikhonov-Fenichel parameter values (TFPV) were introduced in [8] for polyno-
mial (or rational) parameter dependent systems
(10)
˙x = h(x, π),
x ∈Rn, π ∈Π ⊆Rm.
A TFPV bπ is characterized by the property that small perturbations π = bπ +
ερ + · · · along a smooth curve in parameter space Π give rise to a singular
perturbation reduction for
˙x = h(x, bπ + ερ + · · · ) = h(x, bπ) + εDπh(x, bπ)ρ + · · ·
with locally exponentially attracting critical manifold. (The deﬁnition extends
easily to smooth systems but the algorithmic approach relies on the stronger as-
sumption.) There exists an intrinsic characterization of TFPV’s, see [8] Lemmas
1 and 2, for which the characteristic polynomial
(11)
χ(τ, x, π) = τ n + σn−1(x, π)τ n−1 + · · · + σ1(x, π)τ + σ0(x, π)
of the Jacobian Dxh(x, π) is relevant. We recall:
Lemma 2. Given 0 < s < n, a parameter value bπ is a TFPV with locally
exponentially attracting critical manifold Zs (depending on bπ) of dimension s,
and x0 ∈Zs, if and only if the following hold:
• h(x0, bπ) = 0.
• The characteristic polynomial χ(τ, x, π) from (11)) satisﬁes
(i) σ0(x0, bπ) = · · · = σs−1(x0, bπ) = 0;
(ii) all roots of χ(τ, x0, bπ)/τ s have negative real parts.
• The system ˙x = h(x, bπ) admits s independent local analytic ﬁrst integrals
at x0.
12


## Page 13


All the conditions in the lemma can be represented by polynomial equations
and inequalities. The condition on the roots of χ(τ, x0, bπ)/τ s is characterized by
inequalities: There exist n −s Hurwitz determinants (see e.g. Gantmacher [5],
Ch. V, §6, Thm. 4 ﬀ.) which must attain values > 0. Moreover, the existence
requirement for s independent ﬁrst integrals leads to a series of polynomial equa-
tions via degree by degree evaluation of Taylor expansions. More precisely, for
every d > 0 there is an induced action of Dxh(x, π) on the space S1 +· · ·+Sd of
polynomials in n variables with zero constant term and of degree ≤d. Extend-
ing condition (i), the characteristic polynomial of this action (which coincides
with (11) for d = 1) must have vanishing coeﬃcients for all suﬃciently small
powers of the indeterminate. (No further inequalities appear, due to the struc-
ture of the eigenvalues for this action.) Thanks to Hilbert’s Basissatz, ﬁnitely
many of these equations suﬃce. A full account is given in [8].
For the remainder of this section we assume that Π ⊆Rm
+ is a semi-algebraic
set, and that system (10) admits the positively invariant subset Rn
+.
Then,
as was shown in [8], the Tikhonov-Fenichel parameter values for dimension s,
1 ≤s < n form a semi-algebraic subset Πs ⊆Rm. We will denote the Zariski
closure of Πs by Ws. Thus the elements of Ws satisfy all deﬁning equations for
Πs but not necessarily the deﬁning inequalities.
4.2
Nested Tikhonov-Fenichel parameter values
Generalizing the approach to TFPV in [8]), and taking into account the special
form of (7), it seems reasonable to consider surfaces in parameter space. Thus
consider a smooth surface of the special form
γ(ε1, ε2) = bπ + ε1 (ρ1(ε1) + ε2ρ2(ε1, ε2))
deﬁned in some nighborhood of (0, 0). Substitute γ(ε1, ε2) for π in (10) to get
(12)
h (x, γ(ε1, ε2))
=
h(x, bπ)
| {z }
=:g(0,0)
+ h (x, γ(ε1, 0)) −h(x, bπ)
|
{z
}
=:ε1·g(1,0)
+
(h(x, γ(ε1, ε2)) −h(x, bπ)) −(h(x, γ(ε1, 0)) −h(x, bπ))
|
{z
}
=:ε1ε2g(1,1)
with the g(i,j) smooth by Hadamard’s lemma. In order to obtain a system (7)
that also satisﬁes the conditions (i) and (ii) preceding Lemma 1, the following
is necessary: There exist s > 0 and k > 0 such that bπ ∈Πs+k, and bπ + ε1 ·
ρ1(ε1) ∈Πs for all suﬃciently small ε1 > 0. (Note that ε2 plays no role in these
conditions.) This observation gives rise to:
Deﬁnition 2. Given system (10) and s, k > 0 with s + k < n, let δ > 0 and let
β : (−δ, δ) −→Π, ε1 7→β(ε1)
be a smooth curve such that
13


## Page 14


(i) β(ε1) ∈Πs for all ε1 > 0,
(ii) bπ := β(0) ∈Πs+k.
Then we call bπ a Tikhonov-parameter value (for dimension s + k) nested in Πs.
We note some properties of nested TFPV.
Proposition 3. (a) Any TFPV bπ ∈Πs+k which is nested in Πs lies in the
boundary of Πs relative to its Zariski closure Ws.
(b) Let β as in Deﬁnition 2, and for ε1 > 0 consider the decomposition
h(x, β(ε1)) = P ∗(x, ε1)µ∗(x, ε1)
according to [7], Theorem 1. Then
det Dµ∗(x, 0) P ∗(x, 0)) = 0
on the critical manifold.
Proof. Part (a) is a direct consequence of the deﬁnition. As for part (b), at
ε1 = 0, with bπ ∈Πs+k and x0 ∈Zs+k (using notation from Lemma 2), the
coeﬃcient σs(x0, bπ) of the characteristic polynomial (11) of
Dxh(x0, bπ) = P ∗(x0, 0)Dµ∗(x0, 0)
must vanish. This is equivalent to non-invertibility of Dµ∗(x, 0) P ∗(x, 0)); see
e.g. [7], Remark 4.
Remark 4. Proposition 3 opens a starting point for the computation of nested
TFPV: Start with system (10) corresponding to “generic” parameter values in
Πs, i.e. parameter values in the intersection of Πs with an irreducible compo-
nent of the Zariski closure Ws. In order to ﬁnd nested parameters for higher
dimension one only needs to look at the boundary of Πs, and one can use part
(b) in order to obtain necessary conditions. Practically this may be realized by
determining the decomposition P ·µ for generic π ∈Πs and then looking at zeros
of Dµ · P, with parameters in the boundary. (The boundary may also contain
further parameter values in Πs.)
4.3
Special settings for chemical reaction networks
For chemical reaction networks (CRN) the parameter region is usually given by
Π = Rm
+, thus
π =



π1
...
πm


∈Rm
+,
and for many such systems and given s, the irreducible components of Ws are
just determined by the vanishing of certain of the πi; see e.g. [6, 8, 9]. (The
underlying reason for this fact is the subject of forthcoming work.) Thus we
have, for π in a given irreducible component:
14


## Page 15


(i) Upon relabelling, there is an ℓ, 0 < ℓ< m such that πi = 0 for all
i ∈{ℓ+ 1, · · · m};
(ii) the remaining parameters are nonnegative.
In other words, the intersection of Πs with the given irreducible component of
Ws corresponds to some subset of Rℓ
+, with boundary Rℓ
+ \ Rℓ
+. This leads to
an obvious case-by-case analysis. Note that boundary points may or may not
be contained in Πs, but there is no loss in starting with “generic” parameter
values in the interior Rℓ
>0. We look at a particular example.
Example 2. We again consider competitive inhibition; see equation (9). Here
the parameters are of the form
π =










e0
k1
k−1
k2
i0
k3
k−3










∈R7
+.
From [8], Proposition 8 we have the necessary condition e0k1k2k−3 = 0 for a
TFPV in Π1, with each of the four cases (e.g. e0 = 0 and all other parame-
ter values ≥0) yielding a singular perturbation reduction with attracting one
dimensional critical manifold. Hence W1 has four irreducible components. In
order to ﬁnd nested TFPV’s for dimension 2 we perform a case-by-case investi-
gation. We only consider one case here; see Section 5 for the remaining ones.
For the case k2 = 0 the system is given by
˙s = k−1c1 −k1se
˙c1 = k1se −k−1c1
˙c2 = k3ei −k−3c2,
where we have used the abbreviations e = e0 −c1 −c2 and i = i0 −c2; note
that e ≥0 and i ≥0 by design of (9). By Remark 4, nested TFPV’s for di-
mension two and corresponding points in the critical manifold necesarily satisfy
det (Dµ · P) = 0, with
µ =
k−1c1 −k1se
k3ei −k−3c2

, P =


1
0
−1
0
0
1

,
Dµ =
−k1e
k1s + k−1
k1s
0
−k3i
−(k3i + k3e + k−3)

.
Proceeding according to Remark 4, we determine the vanishing set of
det

−(k1e + k1s + k−1)
k1s
k3i
−(k3i + k3e + k−3)

=k1k3ie + k1k3e2 + k1k−3e + k1k3se + k1k−3s + k−1k3i + k−1k3e + k−1k−3.
15


## Page 16


Since all the variables and parameters are nonnegative, this sum equals zero if
and only if every summand vanishes. In particular, k−1 · k−3 has to vanish for
any nested TFPV. We look at the two ensuing cases.
(i) k−1 = 0: Then the remaining conditions are
k1k3ie = k1k3e2 = k1k−3e = k1k3se = k1k−3s = 0.
If k1 = 0 or k3 = k−3 = 0 we obtain a two dimensional variety of stationary
points. Checking the attractivity conditions (HA), one ﬁnds that these
cases yield nested TFPV. If e = s = 0 holds then we get e0−c1−c2 = 0 = s
which corresponds to a one dimensional variety. In case e = k−3 = 0 we
get c1 = 0 while c2 and s are arbitrary, thus we have a two dimensional
(attracting) variety of stationary points.
(ii) k−3 = 0: In this case there remains
k1k3ie = k1k3e2 = k1k3se = k−1k3i = k−1k3e = 0.
In view of case (i) we only have to check k3 = 0 or e = i = 0. In both
cases we get a variety of dimension two.
The case k3 = k−3 = 0 leads to system (9) with k3 = ε1k∗
3, k−3 = ε1k∗
−3 and
k2 = ε1ε2k∗
2, the reduction of which was discussed in Example 1.
5
Further examples
In this section we continue the discussion of the competitive inhibitor network,
to some extent, and furthermore present a fairly complete investigation of a co-
operative system with two complexes, following the strategy outlined in Remark
4. Missing from a complete analysis are some cases concerned with boundary
points in Π1 ⊆W1 which themselves belong to Π1, as well as certain degen-
erate cases for Π2. Moreover we will not generally record routine calculations
to verify conditions such as (HA), and for ease of notation we will frequently
use the term “critical manifold” for the Zariski closure of this object, without
mentioning the inequalities to be satisﬁed.
5.1
Competitive inhibition (cont.)
We continue to investigate the competitive inhibition network; see equation (9),
Examples 1 and 2. The analysis of TFPV which was started in Example 2 will
be ﬁnished here. For Π1 there are three remaining cases, viz. e0 = 0, k1 = 0
and k−3 = 0.
(a) For e0 = 0, the system is given by
(13)
˙s
=
(k1s + k−1)c1 + k1sc2
˙c1
=
−(k1s + k−1 + k2)c1 −k1sc2
˙c2
=
−k3ic1 −(k3i + k−3)c2
16


## Page 17


We only consider the generic case for Π1, thus all the remaining parameters
are > 0. Then the (only possible) decomposition P · µ for the right hand
side is given by
µ =
c1
c2

,
P =


k1s + k−1
k1s
−(k1s + k−1 + k2)
−k1s
−k3i
−(k3i + k−3)

.
For nested TFPV, a simple computation yields the necessary condition
0 = det(Dµ · P) = ik−1k3 + ik2k3 + sk−3k1 + k−3k−1 + k−3k2,
with all terms positive; thus every summand must vanish, and in particular
det(Dµ · P) = 0 ⇒(k−1 + k2)k−3 = 0 ⇒k−1 = k2 = 0 or k−3 = 0.
In case k−1 = k2 = 0 system (13) admits a two dimensional variety of
stationary points, with k1s ̸= 0 only if c1 + c2 = 0. The intersection of this
variety with the positive orthant is only one dimensional, thus we do not
obtain a two dimensional critical manifold. The cases with k1s = 0 translate
to k1 = εk∗
1 for the system with small parameters. (Otherwise the critical
manifold would be given by s = 0, which does not contain the line given
by c1 = c2 = 0.) Moreover we have e0 = ε1ε2e∗
0, hence every term k1e0s
is of the form ε2
1ε2 · (· · · ), and the completely reduced system is necessarily
trivial. Likewise, the case k−3 = 0 in system (13) leads to k1s = 0.
To summarize, the case e0 = 0 yields no interesting reductions for the three
time scale setting, in marked contrast to the familiar (quasi-steady state)
reduction for small initial enzyme concentration with two time scales.
(b) Next we consider the system with k1 = 0, i.e.
˙s = k−1c1
˙c1 = −(k−1 + k2)c1
˙c2 = k3ei −k−3c2.
Because of Example 2 we may assume that k2 ̸= 0, which yields c1 = 0 for
stationary points.
In case k−3 = k3 = 0 we indeed have a two dimensional critical manifold.
Turning to small parameters we have k1 = ε1ε2k∗
1, k3 = ε1k∗
3 and k−3 =
ε1k∗
−3, and (9) becomes
(14)


˙s
˙c1
˙c2

=


k−1c1
−(k−1 + k2)c1
0

+ ε1


0
0
k∗
3ei −k∗
−3c2

+ ε1ε2k∗
1es


−1
1
0


We compute the reductions for this case. For the auxiliary system (on the
critical variety deﬁned by c1 = 0) we obtain the decomposition


k−1c1
−(k−1 + k2)c1
0

=


k−1
−(k−1 + k2)
0


|
{z
}
P1
· c1
|{z}
µ1
,
17


## Page 18


and a straightforward computation yields the projection matrix
Q1 =


1
k−1/(k−1 + k2)
0
0
0
0
0
0
1


and the auxiliary system


˙s
˙c1
˙c2

=


0
0
k∗
3ei −k−3∗c2

+ ε2
k∗
1k2es
k−1 + k2


−1
0
0


on the variety deﬁned by c1 = 0.
The intermediate reduced system is
obtained setting ε2 = 0.
Turning to the complete reduction, the decomposition of the “fast part” of
(14) is given by


k−1
0
−(k−1 + k2)
0
0
ε1



c1
µ2

,
with µ2 = k∗
3ei −k∗
−3c2.
One obtains
A2 =
 −(k−1 + k2)
0
(k−1 + k2)k3i
−ε1 (k3(e + i) + k−3c2)

and may continue as prescribed by Proposition 2.
There are shortcuts,
though: First note that the critical manifold is given by c1 = 0, and c2
constant and equal to the smaller solution ec2 of the quadratic equation
0 = µ2(0, c2) = k∗
3(e0 −c2)(i0 −c2) −k∗
−3c2.
The completely reduced system will automatically yield ˙c1 = 0 and ˙c2 = 0,
hence only the ﬁrst row of the projection matrix needs to be computed. As
the ﬁnal result of the reduction procedure we get the equation
˙s = −
k∗
1k2
k−1 + k2
(e0 −ec2)s,
with the dot denoting diﬀerentiation with respect to ε1ε2t.
(c) Finally, we deal with the case k−3 = 0, which does not automatically yield
a one dimensional variety of stationary points. System (9) becomes
˙s = k−1c1 −k1se
˙c1 = k1se −(k−1 + k2)c1
˙c2 = k3ei.
We may assume that k1 ̸= 0 and k2 ̸= 0, otherwise one would arrive at
(non-generic) subcases of previously discussed systems. From this we ob-
tain c1 = 0 and es = 0 as necessary conditions. Now e = 0 and nonnega-
tivity of varaibles imply e0 = 0; a previously discussed case, therefore every
18


## Page 19


stationary point satisﬁes s = 0. If k3 ̸= 0 then i = 0 forces c2 = i0; the
corresponding parameter values are not in Π1. So the only case remaining
is k3 = k−3 = 0 (very slow binding to the inhibitor, very slow degradation
of the inhibitor complex), with system
˙s = k−1c1 −k1se
˙c1 = k1se −(k−1 + k2)c1
˙c2 = 0.
To obtain a two dimensional variety of stationary points one has to check
the boundary of Π1 for nested TFPV, which splits into four cases. We only
discuss the case k1 = 0 here, thus (9) with small parameters becomes
(15)


˙s
˙c1
˙c2

=


k−1c1
−(k−1 + k2)c1
0

+ ε1k∗
1es


−1
1
0

+ ε1ε2


0
0
k∗
3ei −k∗
−3c2


The computation of the auxiliary system runs similar to the reduction of
(14) and yields


˙s
˙c1
˙c2

=
k∗
1k2es
k−1 + k2


−1
0
0

+ ε2


0
0
k∗
3ei −k−3∗c2

,
on the invariant variety given by c1 = 0. Finally, the completely reduced
system lives on the variety deﬁned by c1 = s = 0 (a coordinate subspace),
and therefore by [9], Proposition 5 the reduced system may be directly
obtained via “classical” QSS reduction; yielding
˙c2 = k∗
3(e0 −c2)(i0 −c2) −k∗
−3c2.
5.2
A cooperative system
In this subsection we study the standard cooperative system involving substrate
S, two complexes C1, C2, enzyme E and product P. The reaction scheme
S + E
k1
⇋
k−1
C1
k2
⇀
E + P
S + C1
k3
⇋
k−3
C2
k4
⇀
C1 + P
yields, with the usual assumptions and stoichiometry, the diﬀerential equation
(16)
˙s
=
−k1e0s + (k−1 + k1s −k3s)c1 + (k1s + k−3)c2
˙c1
=
k1e0s −(k−1 + k2 + k1s + k3s)c1 + (k−3 + k4 −k1s)c2
˙c2
=
k3sc1 −(k−3 + k4)c2
where all appearing constants are non-negative. According to Goeke [6], Kap.
9.4, necessary conditions for TFPV are given by
e0k1k2(k−3 + k4) = 0.
19


## Page 20


5.2.1
Case k1 = 0
When we substitute k1 = 0 in equation (16) we obtain
˙s = (k−1 −k3s)c1 + k−3c2
˙c1 = −(k−1 + k2 + k3s)c1 + (k−3 + k4)c2
˙c2 = k3sc1 −(k−3 + k4)c2.
Hence considering the generic case (all remaining parameters > 0) we obtain an
irreducible component of W1 given by k1 = 0, and the critical manifold is given
by c1 = c2 = 0. We get a decomposition with
P =


−sk3 + k−1
k−3
−(sk3 + k−1 + k2)
k−3 + k4
sk3
−(k−3 + k4)

,
µ =
c1
c2

,
and necessary conditions for nested TFPV from
0 = det Dµ · P = (k−1 + k2)(k−3 + k4) ⇒k−1 = k2 = 0 or k−3 = k4 = 0.
Thie ﬁrst set of conditions does not, by itself, yield a two dimensional crit-
ical manifold, and we will not pursue it further here.
The second set, i.e.
k−3 = k4 = 0, yields the two dimensional variety given by c1 = 0.
Considering this setting, we introduce the small parameters in our original sys-
tem by substituting k1 = ε1ε2k∗
1, k−3 = ε1k∗
−3, k4 = ε1k∗
4 .
Ordering the
parameters as e0, k1, k−1, k2, , k3, k−3, k4 , we thus consider the surface in pa-
rameter space given by
γ(ε1, ε2) =










e0
0
k−1
k2
k3
0
0










+ ε1 ·




















0
0
0
0
0
k∗
−3
k∗
4










+ ε2










0
k∗
1
0
0
0
0
0




















,
and with x = (s, c1, c2)tr we get
(17)
h(x, ε1, ε2) = g(0,0)(x) + ε1 ·

g(1,0)(x, ε1) + ε2 · g(1,1)(x, ε1, ε2)

with
g(0,0)(x) =


(−sk3 + k−1)c1
−(sk3 + k−1 + k2)c1
k3sc1


g(1,0)(x, ε1) =


k∗
−3c2
(k∗
−3 + k∗
4)c2
−(k∗
−3 + k∗
4)c2


g(1,1)(x, ε1, ε2) =


sk∗
1c1 + sk∗
1c2 −k∗
1e0s
−(sk∗
1c1 + sk∗
1c2 −k∗
1e0s)
0

.
20


## Page 21


For this system we compute the complete reduction on c1 = c2 = 0 and the
intermediate reduction on c1 = 0. In order to compute the completely reduced
system, a factorization of g(0,0) + ε1g(1,0) is given by
 P1,
ε1P2

·

µ1
µ2

with µ1 = c1, µ2 = c2, and
P1 =


−sk3 + k−1
−(sk3 + k−1 + k2)
k3s

,
P2 =


k∗
−3
k∗
−3 + k∗
4
−(k∗
−3 + k∗
4)

.
The projection matrix is
Q2 =



1
−
−sk3k∗
4−k∗
−3k−1−k−1k∗
4
k∗
−3k−1+k2k∗
−3+k−1k∗
4+k2k∗
4
−
−sk3k∗
4−2k∗
−3k−1−k2k∗
−3−k−1k∗
4
k∗
−3k−1+k2k∗
−3+k−1k∗
4+k2k∗
4
0
0
0
0
0
0


,
and the fully reduced system in very slow time on the invariant manifold c1 =
c2 = 0 is given by the equation
˙s = −
k3k∗
4s + k∗
−3k2 + k∗
4k2
k∗
−3k−1 + k2k∗
−3 + k−1k∗
4 + k2k∗
4
· k∗
1e0s.
Similarly one computes the intermediate system on the two dimensional variety
given by c1 = 0 from the decomposition P1 · µ1:


˙s
˙c1
˙c2

=
1
sk∗
3 + k−1 + k2


−(sc2k3k∗
4 + 2k−1c2k∗
−3 + k2k∗
−3c2 + c2k∗
4k−1)
0
−(k−1c2k∗
−3 + k2k∗
−3c2 + c2k∗
4k−1 + c2k2k∗
4)

.
5.2.2
Case e0 = 0
From e0 = 0 one also obtains a component of W1, and system (16) specializes
to
˙s = (k−1 + k1s −k3s)c1 + (k1s + k−3)c2
˙c1 = −(k−1 + k2 + k1s + k3s)c1 + (k−3 + k4 −k1s)c2
˙c2 = k3sc1 −(k−3 + k4)c2.
The right hand side has a factorization P · µ with
µ =
c1
c2

,
P =


sk1 −sk3 + k−1
sk1 + k−3
−sk1 −sk3 −k−1 −k2
−sk1 + k−3 + k4
sk3
−k−3 −k4

,
21


## Page 22


and in order to obtain nested TFPV we examine all variable-parameter conﬁg-
urations that satisfy
0 = det(Dµ · P) = sk1 · (sk3 + k−3 + k4) + (k−1 + k2) · (k−3 + k4).
The plane given by s = 0 is not a viable candidate for a two dimensional critical
manifold since it does not contain the line c1 = c2 = 0. This leaves the cases
k1 = k−1 = k2 = 0, k1 = k−3 = k4 = 0 and k3 = k−3 = k4 = 0.
The ﬁrst of these yields a two dimensional variety (deﬁned by k3sc1−k−3c2 = 0)
only under the additional condition k4 = 0. The second case, whenever k1 ̸= 0,
yields a variety whose intersection with the positive orthant has dimension one,
hence is of no relevance. For the third case we obtain a two dimensional variety
only if k1 = 0 or k2 = 0.
With the exception of this very last case, the completely reduced system will al-
ways be trivial, due to k1 = ε1k∗
1 and e0 = ε1ε2e∗
0, which implies k1e0 = O(ε2
1ε2).
We consider one spacial case, viz. the intermediate reduction coresponding to
the nested TFPV with k1 = k3 = k−3 = k4 = 0; here c1 = 0 deﬁnes the two
dimensional critical manifold. Considering
γ (ε1, ε2) =










0
0
k−1
k2
0
0
0










+ ε1 ·




















0
k∗
1
0
0
k∗
3
k∗
−3
k∗
4










+ ε2










e∗
0
0
0
0
0
0
0




















,
we compute:
g(0,0) =


c1k−1
−(k−1 + k2)c1
0


g(1,0) =


(sk∗
1 −sk∗
3)c1 + (sk∗
1 + k∗
−3)c2
−(sk∗
1 + sk∗
3)c1 + (−sk∗
1 + k∗
−3 + k∗
4)c2
k∗
3sc1 −(k∗
−3 + k∗
4)c2


g(1,1) =


−ε1k∗
1e∗
0s
ε1k∗
1e∗
0s
0

.
The intermediate reduced system on the invariant variety c1 = 0 is then:


˙s
˙c1
˙c2

=


 sc2k∗
1k2 + 2c2k∗
−3k−1 + c2k∗
−3k2 + c2k−1k∗
4

(k−1 + k2)
0
−(k∗
−3 + k∗
4)c2

.
22


## Page 23


5.2.3
Case k−3 = k4 = 0
These conditions deﬁne a component of W1, and generically the critical manifold
is given by s = c1 = 0. System (16) is given by
˙s
=
−k1e0s + (k−1 + k1s −k3s)c1 + k1sc2
˙c1
=
k1e0s −(k−1 + k2 + k1s + k3s)c1 −k1sc2
˙c2
=
k3sc1
and the product decomposition (which we do not write down here) yields
0 = det Dµ · P = k1(e0 −c2)(k2 + 2k3s).
as necessary conditions for nested TFPV. One possible case is k1 = 0 with
critical manifold c1 = 0. The remaining cases are:
(i) k2 = k−1 = 0 with variety s = 0;
(ii) k2 = k3 = 0 with variety k1(e0 −c1 −c2)s −k−1c1 = 0.
Note that the condition e0 −c2 = 0 does not yield a two dimensional critical
variety.
5.2.4
Case k2 = 0
In this situation system (16) simpliﬁes to
˙s
=
−k1e0s + (k−1 + k1s −k3s)c1 + (k1s + k−3)c2
˙c1
=
k1e0s −(k−1 + k1s + k3s)c1 + (k−3 + k4 −k1s)c2
˙c2
=
k3sc1 −(k−3 + k4)c2.
The condition k2 = 0 by itself does not deﬁne an irreducible component of W1;
in other words it does not guarantee the existence of a one dimensional variety
of stationary points. Therefore we ﬁrst investigate suﬃcient conditions, using
the observation ˙s + ˙c1 + 2˙c2 = −k4c2.
(a) For k4 ̸= 0 this observation implies that any stationary point satisﬁes c2 = 0,
and the remaining condition is k3sc1 = 0.
(i) In case k3 ̸= 0 we have either s = 0, with the variety of stationary
points given by s = c2 = 0; in turn this yields the parameter conﬁgu-
ration
k−1 = k2 = 0.
(ii) Alternatively we have c1 = 0, the variety is given by c1 = c2 = 0, and
one must have k1e0 = 0. We obtain the possible parameter conﬁgura-
tions
k1 = k2 = 0 or e0 = k2 = 0.
23


## Page 24


(b) In case k4 = 0 the remaining system is
˙s
=
−k1es + k−1c1 −k3sc1 + k−3c2
˙c1
=
k1es −k−1c1 + k3sc1 + k−3c2
˙c2
=
k3sc1 −k−3c2.
Adding the ﬁrst two equations for stationary points shows that k−3c2 = 0,
and combining this with the third equation yields k3sc1 = 0; in addition one
has k1es −k−1c1 = 0. Thus there are further conditions for the existence
of a one dimensional critical variety.
(i) Given that k3 ̸= 0 and k−3 ̸= 0, the variety is given either by c2 = s =
0, which yields the parameter conditions
k2 = k−1 = k4 = 0;
or the variety is given by c1 = c2 = 0, with parameter conditions
k2 = k4 = k1 = 0 or k2 = k4 = e0 = 0;
all of these are special cases from (a).
(ii) In case k3 = 0 we obtain the one dimensional variety given by c2 = 0
and k1(e0 −c1)s −k−1c1 = 0; thus we have the parameter condition
k2 = k3 = k4 = 0
which deﬁnes a component of W1.
(iii) In case k−3 = 0 one obtains the variety s = c1 = 0, with parameter
conditions
k2 = k4 = k−3 = 0.
For all these parameters the next task is to discuss conditions for embedded
TFPV. We will only do so for two cases.
1. In the case k−1 = k2 = 0 one has a decomposition


−k1e −k3c1
k−3
k1e −k3c1
k−3 + k4
k3c1
−(k−3 + k4)

·

s
c2

which yields
det Dµ · P = k1(k−3 + k4)e + k3k4c1.
We take a closer look at the case k1 = k3 = 0, with critical variety c2 = 0.
The surface in parameter space
γ (ε1, ε2) =










e0
0
0
0
0
k−3
k4










+ ε1 ·




















0
k∗
1
0
0
k∗
3
0
0










+ ε2










0
0
k∗
−1
k∗
2
0
0
0




















24


## Page 25


yields
g(0,0) =


c2k−3
(k−3 + k4)c2
−(k−3 + k4)c2


g(1,0) =


−k∗
1e0s + (sk∗
1 −sk∗
3)c1 + sk∗
1c2
k∗
1e0s −(k∗
1s + k∗
3s)c1 −k∗
1sc2
k∗
3sc1


g(1,1) =


k∗
−1c1
−(k∗
−1 + k∗
2)c1
0

.
The intermediate reduced system is as follows:
˙s = sc1k−3k∗
1 + k4k∗
1c1s −sc1k∗
3k4 −k∗
1e0sk−3 −k∗
1e0sk4
k−3 + k4
˙c1 = −sc1k∗
1 + k∗
1e0s
˙c2 = 0,
and the completely reduced system (on s = c2 = 0) is given by:
˙c1 = −c1(c1k−3k∗
1k∗
2 −c1k∗
−1k∗
3k4 + c1k∗
1k∗
2k4 −c1k∗
2k∗
3k4 −e0k−3k∗
1k∗
2 −e0k∗
1k∗
2k4)
c1k−3k∗
1 + c1k∗
1k4 −c1k∗
3k4 −e0k∗
1k−3 −e0k∗
1k4
2. In the case k2 = k3 = k4 = 0 we have the one dimensional critical manifold
k1s · (e0 −c1) −k−1c1 = 0, c2 = 0
and the right hand side of the system at k2 = k3 = k4 = 0 can be
decomposed into P · µ, with
P =


1
sk1 + k−3
−1
−sk1 + k−3
0
−k−3


µ =
k1s · (e0 −c1) −k−1c1
c2

.
This yields
det(Dµ · P) = (k1(e0 −c1) + k1s + k−4) · k−3.
We investigate the case k−3 = 0. Additionally setting k−3 = 0 we obtain
the two dimensional critical manifold deﬁned by
µ2 := −k1e0s + (k−1 + k1s)c1 + k1sc2 = 0.
25


## Page 26


Following the usual procedure we consider the surface
γ (ε1, ε2) =










e0
k1
k−1
0
0
0
0










+ ε1 ·




















0
0
0
0
0
k∗
−3
0










+ ε2










0
0
0
k∗
2
k∗
3
0
k∗
4




















in parameter space, and thus
g(0,0) =


−k1e0s + (sk1 + k−1)c1 + k1sc2
k1e0s −(sk1 + k−1)c1 + −k1sc2
0


g(1,0) =


k∗
−3c2
k∗
−3c2
−k∗
−3c2


g(1,1) =


−sk∗
3c1
−(sk∗
3 + k∗
2)c1 + k∗
4c2
sk∗
3c1 −k∗
4c2

.
Here the intermediate reduced system is given by
˙s =
1
sk1 + k1(e0 −c1 −c2) + k−1
·
 sc2k∗
−3k1 + 2c2k∗
−3k−1

˙c1 =
1
sk1 + k1(e0 −c1 −c2) + k−1
·
 sc2k∗
−3k1 −2k1c2k∗
−3c1 −2k1k∗
−3c2
2 + 2e0k1k∗
−3c2

˙c2 = −c2k∗
−3
on µ2 = 0, and the fully reduced system is given by
˙s =
1
sk1 + k1(e0 −c1) + k−1
· (−se0k1k∗
2)
˙c1 =
1
sk1 + k1(e0 −c1) + k−1
·
 k1k∗
2c2
1 −k∗
2e0k1c1

˙c2 = 0.
6
More time scales
In this section we give a brief outline on extending the coordinate-free approach
to more than three time scales. Thus let N ≥3 and ﬁrst consider a system with
N −1 small parameters of the form
(18) ˙xi =

Y
1≤j<i
εj

· fi(x, ε1, . . . , εN−1),
1 ≤i ≤N;
brieﬂy ˙x = f(x, ε)
26


## Page 27


with separated variables. By a smooth coordinate transformation this becomes
(19)
˙x = g(0,...,0) + ε1

g(1,0,...0) + ε2

g(1,1,0,...,0) + ε3 (· · · )

with the very last term in the embedded brackets being εN−1g(1,...,1).
Here
all g(i1,...,iN−1) are functions of (x, ε1, . . . , εN−1). Moreover conditions (i), (ii)
preceding Lemma 1 generalize in an obvious manner to the vanishing sets of
g(0,...,0)
g(0,...,0)
+
ε1g(1,0,...0)
g(0,...,0)
+
ε1
 g(1,0,...0) + ε2g(1,1,0,...,0)
etc.
and as in Proposition 2 one obtains decompositions
g(0,...,0)
=
P1µ1
g(0,...,0) + ε1g(1,0,...0)
=
 P1,
ε1P2
 µ1
µ2

g(0,...,0) + ε1
 g(1,0,...0) + ε2g(1,1,0,...,0)
=
 P1,
ε1P2,
ε1ε2P3



µ1
µ2
µ3


etc.
Likewise, one generalizes the deﬁnitions of A1, A2 and the constructions of the
projection matrices Qj, the latter extending smoothly to ε1 = · · · εN−1 = 0.
This yields the various (intermediate) reductions.
Given a general parameter dependent system (10), nested Tikhonov-Fenichel
parameter values may be found via the ansatz
γ : (ε1, . . . , εN−1) 7→bπ + ε1 (ρ1(x, ε1) + ε2 (ρ2(x, ε1, ε2) + ε3 (· · · )))
and the ensuing decomposition of h(x, γ(ε1, . . . , εN−1)) analogous to the one in
(12). Thus the problem is to ﬁnd s > 0, 0 < k1 < · · · < kN−1 with s+kN−1 < n
and a smooth map
β : (ε1, . . . , εN−2) →Π,
deﬁned in some neighborhood of 0, such that
β(ε1, . . . , εN−2)
∈
Πs
β(ε1, . . . , εN−3, 0)
∈
Πs+k1
...
β(0, . . . , 0)
∈
Πs+kN−1
whenever all εj > 0. Rather obvious generalizations of Proposition 3 hold, and
the strategy outlined in Remark 4 remains applicable.
27


## Page 28


Appendix
For the reader’s convenience we state and prove here two lemmas.
Lemma 3. Let r1, r2 be positive integers and
A ∈Rr1×r1,
B ∈Rr1×r2,
C ∈Rr2×r1,
D ∈Rr2×r2.
Moreover assume that all eigenvalues of A have real part < 0. Then the following
are equivalent.
(i) All eigenvalues of −CA−1B + D have real part < 0.
(ii) There exists δ > 0 such that, for every ε ∈(0, δ), all eigenvalues of

A
B
εC
εD

have real part < 0.
Proof. Consider the singularly perturbed linear diﬀerential equation
˙x
=
Ax
+
By
˙y
=
εCx
+
εDy
Introducing z := x + A−1By one can rewrite this as
˙z
=
Az + ε(· · · )
˙y
=
ε
 (−CA−1B + D)y + Cz

Here the fast system is just given by ˙z = Az, and the slow system (on the
critical manifold deﬁned by z = 0) is given by
˙y = ε(−CA−1B + D)y.
Using Tikhonov’s theorem (in the form given e.g. in Verhulst [19], Ch. 8), one
sees that both conditions (i), (ii) are equivalent to exponential attractivity of
the stationary point 0 for the linear system.
Lemma 4. Let V ⊆Rn be open and nonempty, 0 < r < n, δ > 0 and
B1 :
V × [0, δ) →Rn×r,
(x, ε) 7→B1(x, ε)
B2 :
V × [0, δ) →Rn×(n−r),
(x, ε) 7→B2(x, ε)
be smooth functions (deﬁned in some neighborhood of V × [0, δ)) such that Rn
is the sum of the image W1 of B1 and the image W2 of B2, for every (x, ε).
Then the entries of the matrix Q(x, ε) ∈Rn×n which sends v ∈Rn to its
W2-component with respect to the direct sum decomposition W1 ⊕W2 depend
smoothly on (x, ε).
28


## Page 29


Proof. We suppress the arguments (x, ε) in the notation. By assumption C :=
 B1,
B2

is invertible, and the entries of C−1 depend smoothly on (x, ε). With
the projection matrix given by
Q =
 0
B2

C−1,
the assertion is obvious.
Acknowledgement. The work of both authors has been supported by the
bilateral project ANR-17-CE40-0036 and DFG-391322026 SYMBIONT.
References
[1] C. Chicone: Ordinary diﬀerential equations with applications. Second edi-
tion. Texts in Applied Mathematics 34, Springer, New York (2006).
[2] D. Capelletti, C. Wiuf: Uniform approximation of solutions by elimination
of intermediate species in deterministic reaction networks. SIAM J. Appl.
Dyn. Syst. 16, 2259 - 2286 (2017).
[3] P.T. Cardin, M.A. Texeira: Fenichel theory for multiple time scale singular
perturbation problems. SIAM J. Appl. Dyn. Sys. 16, 1452-1452 (2017)
[4] N. Fenichel: Geometric singular perturbation theory for ordinary diﬀeren-
tial equations. J. Diﬀerential Equations 31(1), 53–98 (1979).
[5] F.R. Gantmacher: Applications of the theory of matrices. Dover, Mineola
(2005).
[6] A. Goeke:
Reduktion und asymptotische Reduktion von Reaktionsglei-
chungen. Doctoral dissertation, RWTH Aachen (2013). URL:
http://darwin.bth.rwth-aachen.de/opus3/volltexte/2013/4814/pdf/4814.pdf
[7] A. Goeke, S. Walcher: A constructive approach to quasi-steady state reduc-
tion. J. Math. Chem. 52, 2596 - 2626 (2014).
[8] A. Goeke, S. Walcher, E. Zerz: Determining “small parameters” for quasi-
steady state. J. Diﬀ. Equations 259, 1149–1180 (2015).
[9] A. Goeke, S. Walcher, E. Zerz: Classical quasi-steady state reduction – A
mathematical characterization. Physica D 345, 11 - 26 (2017).
[10] H.G. Kaper, T.J. Kaper: Asymptotic analysis of two reduction methods for
systems of chemical reactions. Physica D 165, 66 - 93 (2002).
[11] J. Keener, J. Sneyd: Mathematical physiology I: Cellular physiology, Second
Ed. Springer-Verlag, New York (2009).
29


## Page 30


[12] C. Lax, S. Walcher:
Singular perturbations and scaling. To appear in
Discrete Contin. Dyn. Syst. Ser. B. http://arxiv.org/abs/1807.03107
(2018).
[13] V. Noel, D. Grigoriev, S. Vakulenko, O. Radulescu: Tropicalization and
tropical equilibrium of chemical reactions. In: G.L. Litvinov, S.N. Sergeev
(eds): Tropical and idempotent mathematics and applications. Contempo-
rary Math. 616, pp. 261 - 275. Amer. Math. Soc., Providence (2014).
[14] L. Noethen, S. Walcher: Tikhonov’s theorem and quasi-steady state. Dis-
crete Contin. Dyn. Syst. Ser. B 16(3), 945–961 (2011).
[15] O. Radulescu, S. Vakulenko, D. Grigoriev: Model reduction of biochemical
reactions networks by tropical analysis methods. Math. Model. Nat. Phe-
nom. 10, 124–138 (2015).
[16] S.S. Samal, D. Grigoriev, H. Fr¨ohlich, O. Radulescu: Analysis of reac-
tion network systems using tropical geometry. In: V.P. Gerdt, W. Koepf,
W.M. Seiler, E.V. Vorozhtsov (eds.): Computer Algebra in Scientiﬁc Com-
puting. 17th International Workshop, CASC 2015. Lecture Notes in Com-
puter Science 9301, Springer-Verlag, Cham (2015), pp. 424–439.
[17] S.S. Samal, D. Grigoriev, H. Fr¨ohlich, A. Weber, O. Radulescu: A geometric
method for model reduction of biochemical networks with polynomial rate
functions. Bull. Math. Biol., DOI 10.1007/s11538-015-0118-0 (2015).
[18] A.N. Tikhonov: Systems of diﬀerential equations containing a small param-
eter multiplying the derivative (in Russian). Math. Sb. 31, 575–586 (1952).
[19] F. Verhulst: Methods and Applications of Singular Perturbations. Boundary
Layers and Multiple Timescale Dynamics, Springer, New York (2005).
30

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
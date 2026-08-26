---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1801.04766v4
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1801.04766v4_A_Markov_theorem_for_generalized_plat_decomposition

> Source: 1801.04766v4_A_Markov_theorem_for_generalized_plat_decomposition.pdf

> Pages: 30

---


## Page 1


A Markov theorem for generalized plat
decomposition
Alessia Cattabriga∗- Bostjan Gabrovšek†
February 18, 2019
Abstract
We prove a Markov theorem for tame links in a connected closed
orientable 3-manifold M with respect to a plat-like representation.
More precisely, given a genus g Heegaard surface Σg for M we repre-
sent each link in M as the plat closure of a braid in the surface braid
group Bg,2n = π1(C2n(Σg)) and analyze how to translate the equiva-
lence of links in M under ambient isotopy into an algebraic equivalence
in Bg,2n. First, we study the equivalence problem in Σg × [0, 1], and
then, to obtain the equivalence in M, we investigate how isotopies
corresponding to “sliding” along meridian discs change the braid rep-
resentative. At the end we provide explicit constructions for Heegaard
genus 1 manifolds, i.e. lens spaces and S2 × S1.
Mathematics Subject Classiﬁcation 2010: Primary 57M27, 20F38; Sec-
ondary 57M25.
∗A. Cattabriga has been supported by the "National Group for Algebraic and Geometric
Structures, and their Applications" (GNSAGA-INdAM) and University of Bologna, funds
for selected research topics.
†B. Gabrovšek has been supported by Slovenian Research Agency grants J1-8131, J1-
7025, and N1-0064.
1
arXiv:1801.04766v4  [math.GT]  15 Feb 2019


## Page 2


1
Introduction and preliminaries
The connection among links and braids dates back to the thirties when
the results of Alexander ([1]) and Markov ([22]) showed that it is possible
to represent each link using a braid, by “closing it up”, and described the
equivalence moves connecting two diﬀerent braids representing the same link.
Forty years later in [6] Joan Birman investigated another way to use braids
with an even number of strands to represent links: closing them in the so
called “plat” way. She proved that each link is the plat closure of a braid and
that two diﬀerent braids representing the same link are connected through a
stabilization move and moves corresponding to the generators of a subgroup
of the braid group studied by Hilden in [19].
After these pioneer works many important results succeeded one another,
as for example the use of braid representations to construct links invariants.
In this direction an interesting result is a description of the Jones polynomial
of a link in terms of the action of a braid, having the link as plat closure,
over a homological pairing deﬁned on a covering of the conﬁguration space
of n points into the 2n-punctured disc (see [4]).
In the light of these fruitful connections, many authors investigated the
possibility to use braids to represent links also in connected closed orientable
3-manifolds diﬀerent from S3. A ﬁrst generalization of Markov’s and Alexan-
der’s results was presented in [28], using the idea of ﬁbered knots, while in
[12, 20, 21] another generalization is reached via mixed braids, i.e., braids
having a part of the strands representing the ambient 3-manifold, via Dehn
surgery.
With respect to plat closure, the ﬁrst attempt to generalize Birman’s
and Hilden’s results was done in [3], using the notion of generalized bridge
decomposition, i.e., plat closure with respect to Heegaard surfaces. More
precisely, the authors proved that given a connected closed orientable 3-
manifold M and a Heegaard surface Σ in M, each link can be represented
as the plat closure of an element of B2n(Σ), the braid group on 2n strings
of Σ. Moreover, they studied a subgroup of B2n(Σ), that they named the
2


## Page 3


generalized Hilden group, acting trivially in the representation and asked
whether, as in the classical case, this group, up to a stabilization move, is
enough to describe the equivalence.
In this paper we refer to this question by generalizing Birman’s equiva-
lence theorem in this setting, i.e., presenting a ﬁnite set of moves connecting
two braids in B2n(Σ) representing isotopic links in the manifold (see Theo-
rem 3). The result is reached in two steps: ﬁrst we study the equivalence
problem in Σ × I, then we add “slide like” moves to take care of isotopies
that are deﬁned in the whole manifold. While the moves arising in the ﬁrst
step do depend only on the genus of Σ, and so are the same in each manifold
having Heegaard genus at most g, the nature of both the manifold and the
Heegaard surface involved in the representation are encoded in the slide like
moves. In order to represent the moves geometrically we borrow the idea of
arrow diagrams used in [15, 25, 26].
Our approach seems to be quite ﬂexible, since, once the manifold and the
Heegaard surface are ﬁxed, in order to describe explicitly the equivalence, it
is enough to ﬁnd the words in B2n(Σ) whose plat closures are the boundaries
of two systems of meridian disks of the Heegaard decomposition associated
to Σ.
Further development on the topic may include studying the connection
among surface braids when the Heegaard splitting is not ﬁxed, e.g., studying
the algebraic relation between braid representatives of a link with respect
to the stabilization of Heegaard splittings.
Another open question is the
construction of new link invariants or the revision of old ones in terms of the
braid representative. Finally, it could also be interesting to expand the set
of examples, worked out in this paper for Heegaard genus one manifolds, to
higher Heegaard genus manifolds.
The paper is organized as follows: in Section 2 we review the notion of
generalized plat decomposition and how a link can be represented through
elements of surface braid groups; in Section 3 we investigate the equivalence
in thickened surfaces while in Section 4 we prove the main theorem of the
3


## Page 4


paper, that is, we describe the moves connecting braids representing isotopic
links. The last section is devoted to the explicit algebraic description of the
equivalence moves in manifolds with Heegaard genus at most one: S3, where
we obtain Birman’s result, lens spaces and S2 × S1.
We end this section by recalling some well-known facts about link iso-
topy in 3-manifolds in order to ﬁx our notations and conventions. Through-
out the text all the 3-manifolds are supposed to be connected, closed and
orientable and we will consider only tame links (i.e., 1-dimensional closed
PL-submanifolds).
Two links L and L′ in a 3-manifold M are equivalent if there exists an
ambient isotopy of M taking L into L′, i.e., there exist a PL-map H : M ×
[0, 1] →M such that: H(·, t) is a PL-homeomorphism of M for each t ∈[0, 1],
H(·, 0) = idM and H(L, 1) = L′.
In the PL-category ambient isotopy is realized through a ﬁnite sequence
of the so called ∆-moves. A ∆-move (and its inverse) on a link L in M is
a local elementary combinatorial isotopy move, realized as follows: (1) take
a closed ball B3 embedded into M and such that L ∩B3 is a trivial arc
a properly embedded in B3 (i.e., an arc that co-bounds an embedded disk
with another arc on ∂B3); (2) replace the arc a by two other arcs such that
all three arcs span an embedded triangle in B3 intersecting L only in a. If
[V1, . . . , Vn] denotes the (n −1)-simplex having V1, . . . , Vn as vertices, the
previous move can be combinatorially described as
L ←→(L −[P, Q]) ∪[P, R] ∪[R, Q]
with {P, Q} = ∂a and [P, Q, R] ∩L = [P, Q].
Acknowledgement: A. Cattabriga has been supported by the “National Group
for Algebraic and Geometric Structures, and their Applications” (GNSAGA-
INdAM) and University of Bologna. B. Gabrovšek was ﬁnancially supported
by the Slovenian Research Agency grants J1-8131, J1-7025, and N1-0064.
4


## Page 5


2
Heegaard surfaces and generalized plat de-
compositions
In this section we review the notion of generalized plat decomposition,
introduced in [13], and describe how a link can be represented through ele-
ments of surface braid groups (see [3]). We end the section by describing the
set of generators of surface braid groups given in [2].
A Heegaard surface for a 3-manifold M is a connected closed orientable
surface Σ embedded in M such that M \Σ is the disjoint union of two handle-
bodies (of the same genus). From an extrinsic point of view, we can say that
M is homeomorphic to H1∪hH2, where H1 and H2 are two oriented copies of
a standard handlebody in R3 (see Figure 1) and h : ∂H2 −→∂H1 is an ori-
entation reversing homeomorphism. The triple (H1, H2, h) is called Heegaard
splitting of M and the Heegaard surface is ∂H1 ∪h ∂H2. Each 3-manifold
admits Heegaard splittings (see [18]), moreover, Heegaard splittings are 3-
dimensional cases of symmetric version handle decomposition, that holds for
each diﬀerentiable manifolds of odd dimension (see [23]). Indeed, one han-
dlebody is obtained by attaching g 1-handles to a 0-handle, while attaching
g 2-handles to one 3-handle, gives, up to duality, the other handlebody. The
Heegaard genus of a 3-manifold M is the minimal genus of a Heegaard surface
for M: the 3-sphere S3 is the only 3-manifold with Heegaard genus 0, while
the manifolds with Heegaard genus 1 are lens spaces (i.e., cyclic quotients
of S3) and S2 × S1. While S3, as well as lens spaces, have, up to isotopy,
only one Heegaard surface of minimal genus (and those of higher genera are
stabilizations of that of minimal genus), in general, a manifold may admit
non isotopic Heegaard surfaces of the same genus (see for example [24] for
the case of Seifert manifolds).
Heegaard surfaces are the tool that leads to a generalization of the clas-
sical notion of bridge decomposition for links in R3 (or S3) to the case of
5


## Page 6


3-manifolds (see [13]). Given a handlebody H, we say that a set of n properly
embedded disjoint arcs {A1, . . . , An} is a trivial system of arcs if there exist
n mutually disjoint embedded discs, called trivializing discs, D1, . . . , Dn ⊂H
such that Ai ∩Di = Ai ∩∂Di = Ai, Ai ∩Dj = ∅and ∂Di −Ai ⊂∂H for
all i, j = 1, . . . , n and i ̸= j. We say that the arc Ai projects onto the arc
∂Di −int(Ai) ⊂∂H (via Di). Let Σ be a Heegaard surface for M. We say
that a link L in M is in bridge position with respect to Σ if:
(i) L intersects Σ transversally and
(ii) the intersection of L with both handlebodies, obtained splitting M by
Σ, is a trivial system of arcs.
Such a decomposition for L is called (g, n)-decomposition or n-bridge decom-
position of genus g, where g is the genus of Σ and n is the cardinality of the
trivial system. The minimal n such that L admits a (g, n)-decomposition is
called the genus g bridge number of L. Clearly if g = 0, the manifold M is
the 3-sphere and we get the usual notion of bridge decomposition and bridge
number of links in the 3-sphere (or in R3). The notion of (g, b)-decomposition
is a useful tool to study links in 3-manifolds (see for example [7, 8, 10, 16]).
As bridge decompositions of links in S3 (or R3) are connected to plat
closures of classical braids, (g, b)-decompositions can be used to represent
links in 3-manifolds via braid groups of surfaces as follows (see also [3, 9]).
Let Σg be a genus g Heegaard surface for a 3-manifold M and let c =
{c1, . . . , cg} and c∗= {c∗
1, . . . , c∗
g} be the boundaries of two systems of merid-
ian discs of the two handlebodies.1
In terms of handle decomposition we
can think of c as the attaching circles of the 2-handles and of c∗as the
dual attaching circles of the 1-handles, i.e., the attaching circles of the dual
2-handles in the “upside down” decomposition (see [17]). Starting from the
data (Σg, c, c∗) we can reconstruct M by: considering the thickened surface
1Recall that a genus g handlebody is uniquely determined, by the boundary surface
and the boundaries of a system of g disjoint meridian discs whose complement is (homeo-
morphic to) the 3-ball.
6


## Page 7


Σg ×[0, 1], gluing 2-handles along the curves c×{1} ⊂Σg ×{1} and another
set of (dual) 2-handles along the curves c∗× {0} ⊂Σg × {0}, and closing the
resulting manifold by attaching a 3-handle and a (dual) 3-handle. Given a
Heegaard splitting of a 3-manifold M, we call the triple (Σg, c, c∗) Heegaard
diagram of the splitting.
Up to homeomorphism, we can always suppose
that Σg and c∗are as depicted in Figure 1, while c depends on M and on
the chosen Heegaard surface.
Referring to Figure 1, let P2n = {P1, . . . , P2n} be a set of 2n distinct
points on Σg and denote with Bg,2n, the braid group on 2n-strands of Σg, i.e,
the fundamental group of the conﬁguration space of the 2n points in Σg. Fix
a set of n arcs γ1, . . . , γn embedded into Σg, such that γi ∩γj = ∅if i ̸= j and
∂γi = {P2i−1, P2i}, for i, j = 1, . . . , n. Given an element β ∈Bg,2n, realize
it as a geometric braid, that is, as a set of 2n disjoint paths in Σg × [0, 1]
connecting P2n × {0} to P2n × {1}. The plat closure bβ ⊂M of β is the link
obtained “closing” β by connecting P2i−1×{0} with P2i×{0} through γi×{0}
and P2i−1 × {1} with P2i × {1} through γi × {1}, for i = 1, . . . , n. Clearly, bβ
is in bridge position with respect to Σg and so it has genus g bridge number
at most n. Note that this closing procedure does not depend on the system
of meridian curves c, however, as we will see, c characterizes the manifold,
so the isotopy type of the resulting link does depend on it.
In Figure 2 an example is represented with g = 1 and n = 2, with
Σ1 ∼= S1 × S1 represented as a square with opposite sides identiﬁed.
c∗
1
c∗
2
· · ·
c∗
g
P1
P2
P3
P4 · · ·P2n−1 P2n
γ1
γ1
γn
Figure 1: The standard choice for Σg, c∗= {c∗
1, . . . , c∗
g} and γ1, . . . , γn.
As in the classical case, it is possible to prove an Alexander representation
theorem, i.e., each link in M is isotopic to the plat closure of a braid in Bg,2n.
This follows essentially from [3, Proposition 4.6], where, however, a slightly
7


## Page 8


β
−−−−−−−−−→
t = 0
t = 1
Figure 2: An example of a closure bβ with β ∈B1,4.
diﬀerent approach is used.
So here we describe a more topological proof
using techniques analogous to those used in [6, Lemma 2], that will be useful
throughout the rest of the text.
Theorem 1. Every link L in a 3-manifold M having Heegaard genus at most
g, may be braided to a geometric braid in Bg,2n, the plat closure of which is
equivalent to L.
Proof. Let (Σg, c, c∗) be a Heegaard diagram for M, where Σg and c∗are
those depicted in Figure 1. Up to isotopy, we can assume that L ⊂N(Σg),
where N(Σg) denotes a closed tubular neighborhood of Σg. We choose a
parametrization N(Σg) ∼= Σg × I, with I = [0, 1], such that L ⊂Σg ×
[0.25, 0.75] and ﬁx an orientation on each component of L. By projecting a
point of N(Σg) onto a boundary component of ∂(Σg × I), we mean moving
the point along the I trivial ﬁbration until the required boundary component
is reached. Let Q1, . . . , Qk, be the vertices in a PL-decomposition of L having
the following property:
given a triple of consecutive points (according to the
orientation of L) Qi−1, Qi, Qi+1 there exist an open
neighborhood Ni of the I ﬁbre trough Qi in N(Σg) whose
(*)
intersection with L is contained in [Qi−1Qi] ∪[QiQi+1].
8


## Page 9


0.75
0.25
t
1
0
Qi−1
Qi
Qi+1
Q′
i
Q+
i
Q′′
i
Qi−1
Qi
Qi+1
Q′
i
Q−
i
Q′′
i
Figure 3: The braiding process.
By a general position argument we can assume that L, up to isotopy,
contains no arcs which are horizontal with respect to the height function
associated to the projection onto the I factor. Moreover, we say that a subarc
of L is oriented upwards (resp. downwards) if moving along it, with respect
to the ﬁxed orientation, its projection over I is increasing (resp. decreasing).
Note that each component of L contains at least one arc oriented upwards
and one arc oriented downwards.
We will construct a link L′ isotopic to L such that:
(1) L′ is contained in N(Σg),
(2) the link L′ meets both Σg × {0} and Σg × {1} in n points, and meets
Σg × {t}, for each t ∈(0, 1) in exactly 2n points.
For each connected component of L, ﬁx a point inside it contained in an
arc oriented upwards and repeat the following process: moving along the
component according to the ﬁxed orientation and starting from the distin-
guished point let [Qi, Qi+1] be the ﬁrst arc which is oriented downwards;
consider the neighborhood Ni of Qi × I deﬁned in (*) and let Q′
i, Q′′
i be
the unique point of intersection of ∂Ni with, respectively, [Qi−1, Qi] and
[Qi, Qi+1] and Q+
i be the projection of Qi onto Σg × {1} (see Figure 3). Re-
place [Qi−1, Qi] ∪[Qi, Qi+1] with [Qi−1, Q′
i] ∪[Q′
i, Q+
i ] ∪[Q+
i , Q′′
i ] ∪[Q′′
i , Qi+1].
This move can be clearly decomposed into a sequence of ∆-moves. Now go
on, along the same component of the link, until you meet the ﬁrst subarc
9


## Page 10


[Qk, Qk+1] which is oriented upwards and replace [Qk−1, Qk]∪[Qk, Qk+1] with
[Qk−1, Q′
k]∪[Q′
k, Q−
k ]∪[Q−
k , Q′′
k]∪[Q′′
k, Qk+1], where now Q−
k is the projection
of Qk onto Σg × {0}. Let L′ be the link obtained at the end of the process:
clearly L′ is isotopic to L and L′ satisﬁes properties (1) and (2).
Let Q−= {Q−
1 , . . . , Q−
n } (resp. Q+ = {Q+
1 , . . . , Q+
n }) be the set of points
in Σg deﬁned by the condition L′ ∩(Σg × {0}) = Q−× {0} (resp.
L′ ∩
(Σg × {1}) = Q+ × {1}). Referring to Figure 1, for each arc γi, let Bi be an
internal point of the arc. Since the conﬁguration space Cn(Σg) of n point in
Σg is arc connected (see [5]) there exist two paths p−(t) : I →Cn(Σg) and
p+(t) : I →Cn(Σg) such that p−(0) = {B1, . . . , Bn} = p+(1), p−(1) = Q−
and p+(0) = Q+. Properly rescaling the interval I and deforming L′ along
the graph of such paths, we obtain an isotopic link L′′ satisfying (1) and (2)
and such that L′′ ∩(Σg × {0}) = {B1, . . . , Bn} × {0} and L′′ ∩(Σg × {1}) =
{B1, . . . , Bn}×{1}. Then there clearly exists an η > 0 such that L′′∩[η, 1−η]
is a well deﬁned element β ∈Bg,2n, with bβ equivalent to L′′.
Remark 1. The procedure described in the previous proof is called the
braiding process. Since the braiding process is realized in Σg × I, we have
that also each link in a thickened surface is equivalent to the plat closure of
a braid.
We end this section by recalling the presentation of Bg,2n given in [2]. The
generators are: σ1, . . . , σ2n−1, the standard braid ones, and a1, . . . , ag, b1, . . . , bg,
where ai (resp. bi) is the braid whose strands are all trivial except the ﬁrst
one which goes once along the i-th longitude (resp. i-th meridian) of Σg (see
Figure 4). The relations are the following ones:
ai
bi
σj
· · ·
· · ·
· · ·
· · ·
1
i
g
1
j
j+1
2n
Figure 4: The generators of Bg,2n.
10


## Page 11


- Braid relations:
σiσi+1σi = σi+1σiσi+1
(i = 1, . . . , 2n −2)
σiσj = σjσi
(i, j = 1, . . . , 2n −1, |i −j| ≥2)
- Mixed relations:
(R1)
arσi = σiar
(1 ≤r ≤g, i ̸= 1)
brσi = σibr
(1 ≤r ≤g, i ̸= 1)
(R2)
σ−1
1 arσ−1
1 ar = arσ−1
1 arσ−1
1
(1 ≤r ≤g)
σ−1
1 brσ−1
1 br = brσ−1
1 brσ−1
1
(1 ≤r ≤g)
(R3)
σ−1
1 asσ1ar = arσ−1
1 asσ1
(s < r)
σ−1
1 bsσ1br = brσ−1
1 bsσ1
(s < r)
σ−1
1 asσ1br = brσ−1
1 asσ1
(s < r)
σ−1
1 bsσ1ar = arσ−1
1 bsσ1
(s < r)
(R4)
σ−1
1 arσ−1
1 br = brσ−1
1 arσ1
(1 ≤r ≤g)
(TR)

a1, b−1
1

· · ·

ag, b−1
g

= σ1σ2 · · · σ2
2n−1 · · · σ2σ1
where [a, b] := aba−1b−1.
We will depict a braid in Bg,2n using a set of g ﬁxed strands on the left
(that intuitively represent the g holes of Σg) and 2n moving strands on the
right, which represent the braid. As depicted in Figure 5, we represent the
generator ai and its inverse by the ﬁrst moving strand winding around the
i-th ﬁxed strand and going over the rest of the ﬁxed strands on the right, for
i = 1, . . . , g. We represent bi (resp. b−1
i ), i = 1, . . . , g, by an arrow labelled i
on the ﬁrst moving strand pointing downwards (resp. upwards).
3
Markov theorem in thickened surfaces
In this section we study the combinatorial equivalence for links in a thick-
ened surface, generalizing results of [6]. Once the statement is established,
11


## Page 12


1
g
1
j j+1 2n
· · ·
· · ·
· · ·
σj
1
i
g
1
2n
· · ·
· · ·
· · ·
· · ·
· · ·
· · ·
ai
1
g
1
2
2n
· · ·
· · ·
i
bi
1
g
1
j j+1 2n
· · ·
· · ·
· · ·
σ−1
j
1
i
g
1
2n
· · ·
· · ·
· · ·
· · ·
· · ·
· · ·
a−1
i
1
g
1
2
2n
· · ·
· · ·
i
b−1
i
Figure 5: Representing the generators of Bg,2n and their inverses.
the proof given in [6] works almost without changes also in this more general
setting. Nevertheless, for readers’ convenience, we report here the main steps
of the proof, with the only exception of Lemma 8 of [6] (see Proposition 1),
which is really technical.
Let Σg be the genus g surface depicted in Figure 1. A link L ⊂Σg × I
is said to be in standard position if it intersects both Σg × {0} and Σg × {1}
in n points, and meets Σg × {t}, for each t ∈(0, 1) in exactly 2n points. We
call the points of Σg × {1} (resp. Σg × {0}) upper (resp. lower) boundary
points. A boundary point is either an upper or a lower boundary point, while
an interior point is a point in Σg × (0, 1).
The proof of Theorem 1, along with the Remark 1, shows that each link
in Σg × I is isotopic to a link in standard position. Moreover it shows that
each link L in standard position is equivalent to the plat closure of a braid
in Bg,2n, where n is the number of upper (or lower) boundary points of L.
Given a link L in standard position, ﬁx an orientation on it and consider
the following two moves, introduced in [6]:
• the spike move: referring to Figure 6, let Q, B, P be consecutive points
on L such that Q, P are interior points, B is a boundary point and
[Q, B, P] is an (embedded) triangle in Σg × I such that [Q, B, P] ∩L =
[Q, B] ∪[B, P]. Let B′ ̸= B be another boundary point on the same
12


## Page 13


boundary component as B and let Q′, P ′ be interior points satisfy-
ing the conditions [P, P ′, Q′] ∩L = {P}, [Q, P ′, Q′] ∩L = {Q} and
[P ′, B′, Q′] ∩L = ∅. We replace [Q, B] ∪[B, P] on L with [Q, Q′] ∪
[Q′, B′] ∪[B′, P ′] ∪[P ′, P]. Note that the spike move is executed by
retracting the “spike” at B to the “base” [P, Q] and shooting out a new
spike at B′, which will in general thread in and out of the other arcs of
the link. So, generally it will not be possible to get the same result by
moving the spike at B directly along the boundary surface toward B′,
since the other arcs of L may interfere with such a move.
1
0
B
B′
Q
P
Q′ P ′
←−→
1
0
B
B′
Q
P
Q′ P ′
Figure 6: The spike move on an upper boundary point.
• the stabilizing move: referring to Figure 7, let R be any internal point
on L. We can always assume, up to isotopy, that the three consecutive
points P, R, Q on L satisfy property (*). Let R′, R′′ be the unique
points of intersection of ∂N (see property (*)) with, respectively, [P, R]
and [R, Q] and R+, R−be the projection of R onto, respectively, Σg ×
{1} and Σg × {0}. We replace [R′, R] ∪[R, R′′] on L with [R′, R+] ∪
[R+, R−] ∪[R−, R′′].
Clearly both the moves do not alter the property of being in standard
position and are compositions of ∆-moves. As a consequence, if we apply
such moves to a link in standard position, we will obtain an equivalent link
still in standard position. Moreover, while a spike move does not change the
number of upper (or lower) boundary points, the stabilization move increases
or decreases it by one.
13


## Page 14


1
0
P
R′
R
R′′ Q
←−→
1
0
R+
R−
P
R′
R′′
Q
Figure 7: The stabilization move.
In [6, Lemma 8] the converse statement is proved in the case of g = 0,
that is to say, for the classical plat closure in D2 × I or S2 × I. The proof
extends without changes to the case of higher genus, so we get the following
result.
Lemma 1. Let L and L′ be two equivalent links in standard position. Then it
is possible to connect L with L′ by a ﬁnite sequence of spike and stabilization
moves.
Consider the arcs γ1, . . . , γn depicted in Figure 1.
In order to get an
algebraic equivalence among braids, we introduce some speciﬁc elements of
Bg,2n (see Figure 8):
- braid twists or intervals: are braids exchanging the endpoints of an arc
γi; in terms of the generators of Bg,2n they are the elements σ2i−1, for
i = 1, . . . , n;
- elementary exchanges of two arcs: are braids exchanging two arcs γi
and γj; it is possible to write them as products of elementary ex-
changes of neighborhood arcs, that is, as products of the elements
σ2iσ2i+1σ2i−1σ2i, exchanging γi and γi+1 for i = 1, . . . , n −1;
- slides of the i-th arc: is a braid obtained by moving the both the
endpoints P2i−1 and P2i of an arc γi along parallel paths; any slide of
the i-th arc can be written as cσc−1, where c is an elementary exchange
14


## Page 15


taking the i-th arc into the ﬁrst one and σ is a slide of the ﬁrst arc;
moreover, a slide of the ﬁrst arc can be written as a product of the
following slides
1) a slide under the second arc σ2σ2
1σ2;
2) a slide around the j-th longitude ajσ−1
1 ajσ−1
1 ;
3) a slide around the j-th meridian bjσ−1
1 bjσ−1
1 .
2i-1
2i
γi
(a)
2i-1
2i
γi
2i+1
2i+2
γi+1
(b)
1
2
γ1
3
4
γ2
(c)
1
j
g
1
2
γ1
(d)
1
2
γ1
j
j
(e)
Figure 8: (a) The braid twist of the i-th arc, (b) the elementary exchange of
the i-th and (i + 1)-th arc, (c) the slide of the ﬁst arc under the second one,
(d) the slide of the ﬁst arc around the j-th longitude, (e) the slide of the ﬁst
arc around the j-th meridian.
Note that the slide of the ﬁrst arc under the i-th one is the product of
dσ2σ2
1σ2d−1, where d is an elementary exchange taking the i-th arc into the
second one.
15


## Page 16


Remark 2. Let MCG2n(Σg) := π0(Homeo+(Σg, P2n)) and MCG(Σg) =
π0(Homeo+(Σg)) and consider the exact sequence (see [5])
· · · →Bg,2n →MCG2n(Σg) →MCG(Σg) →1.
The image of the above deﬁned elements of Bg,2n belong to the Hilden
braid group Hilg
n ⊂MCG2n(Σg) introduced in [3]. Such subgroup can be
characterized as that containing the elements admitting an extension to the
couple (H, A), where H is the handlebody corresponding to the system of
curves depicted in Figure 1 and A is a system of trivial arcs properly embed-
ded in H and projecting onto {γ1, . . . , γn}.
We are ready to state the main theorem of this section.
Theorem 2. Two elements of ∪n∈NBg,2n determine, via plat closure, equiv-
alent links in Σg × I if and only if they are connected by a ﬁnite sequence of
the following moves:
(M1)
σ1β ←→β ←→βσ1
(M2)
σ2iσ2i+1σ2i−1σ2iβ ←→β ←→βσ2iσ2i+1σ2i−1σ2i
(M3)
σ2σ2
1σ2β ←→β ←→βσ2σ2
1σ2
(M4)
ajσ−1
1 ajσ−1
1 β ←→β ←→βajσ−1
1 ajσ−1
1
for j = 1, . . . , g
(M5)
bjσ−1
1 bjσ−1
1 β ←→β ←→βbjσ−1
1 bjσ−1
1
for j = 1, . . . , g
(M6)
β ←→Tk(β)σ2k
where Tk : Bg,2n →Bg,2n+2 is deﬁned by Tk(ai) = ai, Tk(bi) = bi and
Tk(σi) =







σi
if i < 2k
σ2kσ2k+1σ2k+2σ−1
2k+1σ−1
2k
if i = 2k
σi+2
if i > 2k
.
Proof. Following the proof of Theorem 1, given L in standard position in
order to ﬁnd an element β ∈Bg,2n such that bβ = L, up to isotopy, we have
to choose two paths p−and p+ in Cn(Σg) connecting, respectively, the set
of lower boundary points of L and the set of upper boundary points of L to
16


## Page 17


{B1, . . . , Bn}, where Bi is an internal point of the arc γi, with i = 1, . . . , n.
Clearly the choice of such paths is not unique: however if p−and q−are
two possible choices for the set of lower boundary points, the composition of
p−with the inverse of q−determines an element in π1(Cn(Σg), {B1, . . . , Bn})
that could be realized as a composition of braid twists, exchanges and slides
of the arcs γi. An analogous remark holds for upper boundary points. So two
diﬀerent elements of Bg,2n obtained as above for the same link L in standard
position are connected by moves (M1), . . . , (M5).
By Lemma 1, in order to prove the statement, it is enough to describe
how a stabilization move and a spike move change a braid representative β
of a link bβ.
We start with the stabilization move. The eﬀect of a stabilization move
is to add a trivial loop to the plat bβ at any point.
As depicted in Fig-
ure 9, by “sliding the stabilization” along a connected component, we may
assume, up to spike moves, that the stabilization is done at the bottom right
of an even strand. We have four diﬀerent possibilities on how to perform
the stabilization move depending whether (i) we add a loop with a positive
or negative twist and (ii) the new strands pass in front or behind the old
ones. Up to spike moves, it is always possible to assume that the twist is
positive (see Figure 10) and that the new strands pass in front of the old
ones (see Figure 11). With these assumptions, it is straightforward to check
that the braid representative after the stabilization move will be Tk(β)σ2k if
the stabilization occurs on the 2k-th strand, that is the stabilization move
corresponds to a (M6) move.
Let bβ′ be the plat obtained from bβ by applying a spike move.
Sup-
pose that the spike move involves the i-th upper boundary point B+
i , with
i ∈{1, . . . , n}. We may assume that there exists t0 ∈(0, 1) such that the
segments [P, P ′] and [Q, Q′] lie in Σg ×{t0} and that the surface Σg ×{t0} di-
vides the braid β into an upper braid β1 and a lower braid β2, both contained
in Bg,2n, so that β = β1β2. Then there exists an element β′
1 ∈Bg,2n such that
β′ = β′
1β2. Consider the element β′β−1 = β′
1β−1
1
and denote by (β′β−1)k the
17


## Page 18


1
0
P1
P2
stab.
−−−−→
at P1
1
0
B1
stab.
−−−−−→
at P2
spike
−−−−−→
at B1
1
0
B′
2
spike
←−−−−
at B2
1
0
B′
1
B2
Figure 9: Normalizing the stabilization: always done at the bottom right of
an even strand.
k-th strand of the braid β′β−1. It follows from the deﬁnition of spike move
that (i) there exists an embedding of a band I ×I into Σg×I whose boundary
is given by γi×{1}∪(β′β−1)2i−1∪γj ×{0}∪(β′β−1)2i with i ∈{1, . . . , n} and
(ii) β′β is in the kernel of the map Bg,2n →Bg,2n−2 obtained by forgetting
the (2i −1)-th point and 2i-th point (see Figure 12). This means exactly
that the element β′β−1 can be written as a product of slides of arcs, braid
twists and exchanges of arcs that correspond to the moves (M1), . . . , (M5).
An analogue reasoning holds in the case of a spike move on a lower boundary
point.
Given two braids we say that they are Σ-equivalent if it is possible to
connect them by a ﬁnite sequence of the six M-moves (M1), . . . , (M6).
18


## Page 19


1
0
B′
1
B1
spike
−−−−→
at B1
1
0
B′
1
B1
isotopy
←−−−−−
1
0
B′
1
B1
spike
−−−−→
at B′
1
1
0
B′
1
B1
Figure 10: Normalizing the stabilization: adding always a positive twist.
4
The slide move and the Markov theorem
In this section we establish the main result of the paper, that is, we
describe the moves connecting braids representing isotopic links, by adding
slide like moves to Σ-equivalence.
Let L1 and L2 be two disjoint links in M and let b ∼= I×I be an embedded
band in M, such that b ∩L1 = e1 ∼= I × {0} and b ∩L2 = e2 ∼= I × {1}. The
band connected sum of L1 and L2 along b is the link
(L1 −e1) ∪(L2 −e2) ∪(∂b −e1 −e2),
denoted by L1#bL2.
Remark 3. In general the band connected sum L1#bL2 depends on the
choice of the band b. For an oriented split link L1 ∪L2 in S3, such that the
splitting sphere intersects b transversally in a single arc, we can argue by
19


## Page 20


1
0
B′
1
B1
spike
−−−−→
at B1
1
0
B′
1
B1
spike
←−−−−
at B′
1
1
0
B′
1
B1
Figure 11: Normalizing the stabilization: the new strands pass always in
front of the old ones.
t0
B+
i
γi
β1
(a)
t0
β′
1
(b)
β′
1
β−1
1
(c)
Figure 12: Braid interpretation of the spike move.
the lightbulb trick (see [27]) that the band connected sum is independent on
the choice of b (up to the choice of components to which b connects). For
a general 3-manifold M, a suﬃcient condition for the band connected sum
to be independent of b (up to the choice of the component in L1 to which b
20


## Page 21


connects) is that L2 is an unknot contained inside a 3-ball B3, that is disjoint
from L1, and b does not intersect the open disk which L2 bounds. We say
that such a band b is unlinked with L2.
Next we deﬁne a connected sum operation α#β for braids α and β so
that it holds [
α#β = bα#bbβ for some band b.
Let α ∈Bg,2m and β ∈Bg,2n be two braids. The plat sum of α and β is
the operation
α#β := α wm,n β ∈Bg,2(m+n−1),
where
wm,n =
2m−3
Y
i=0
2n−3
Y
j=0
σ2m−i+j,
see Figure 13 for a geometric interpretation.
α
β
···
···
1
g
1 2
3 4
5
6
7 8
Figure 13: The plat sum α#β.
Let again Σg be a genus g Heegaard surface of M and c = {c1, . . . , cg} the
collection of attaching circles in Σg ×{1} and c∗= {c∗
1, . . . , c∗
g} the collection
of dual attaching circles in Σg × {0}.
If we approach the attaching region of the i-th 2-handle in Σg × {1} with
an arc of a link L ⊂Σg × I, we can slide the arc along the 2-handle, which
has the eﬀect of making a connected sum with the attaching circle ci by a
small band b:
sli : L −→L#bci,
i = 1, . . . , g.
We call this operation the i-th slide move.
Similarly, if we approach the
attaching region of the dual i-th 2-handle in Σg × {0}, this gives rise to the
21


## Page 22


i-th dual slide move:
sl∗
i : L −→L#bc∗
i ,
i = 1, . . . , g.
Both types of slide moves are isotopy moves in M, since all ci and c∗
i
bound (meridian) discs in M and thus are trivial knots in M.
Lemma 2. The curves c and dual curves c∗can be expressed as closed plats
with two strands.
Proof. Let Q1, . . . , Qk be the collection of consecutive vertices in a PL-
decomposition of ci. Since ci lies on Σg×{1}, all arcs of ci are horizontal with
respect to the height function associated with Σg×I. By a small perturbation
we can isotope the points so that all arcs [Qi, Qi+1] are oriented downwards
and use a ∆-move to replace the arc [Qk, Q1] with [Qk, Q′
1] ∪[Q′
1, Q1], where
[Q′
1, Q1] is a vertical upward arc. By the braiding process described in the
proof of Theorem 1 (see also Figure 3), a knot with only one upward arc
can be braided with two strands. An analogue construction can be made for
c∗
i .
If β ∈Bg,2n is a braid representative of L and ci (resp. c∗
i ) is a braid
representative of ci (resp. c∗
i ), then the slide move (resp. dual slide move)
can be expressed in braid form by a plat connected sum as:
psli : β −→ci#β,
i = 1, . . . , g,
which we call the i-th plat slide move and
psl∗
i : β −→β#c∗
i ,
i = 1, . . . , g,
which we name the i-th dual plat slide move. Since ci can be braided with
two strands, both psli(β) and psl∗
i (β) are elements of Bg,2n.
There are several ways we can slide an arc across a 2-handle. Since we
are performing band sums with trivial knots, by Remark 3, we have to check
that the above plat slide moves include band connected sums where the band
starts at any position of bβ and any position of ci (resp. c∗
i ), assuming that
22


## Page 23


the band b is unlinked with ci (resp. c∗
i ). The following lemma shows that,
up to Σ-equivalence, plat slide moves include band connected sums where
the band starts at any position of bβ.
Lemma 3. Given a plat bβ, a plat slide move (resp. dual plat slide move)
can be always assumed to take place on top left strand (resp. bottom left
strand) of β as represented in Figure 14a. That is, for any braid β and any
band b starting from an arbitrary point in bβ, arbitrary linked with bβ and
connected to ci (resp. c∗
i ), there exists a Σ-equivalent braid β′ such that
ci#bbβ is isotopic to \
ci#β′ (resp. bβ#bc∗
i is isotopic to \
β′#c∗
i ).
Proof. We prove the statement in the non-dual case.
As the band b ap-
proaches ci (Figure 14b) we can cut b and obtain a link bβ′ isotopic to bβ
(Figure 14c). We use the braiding process described the proof of Theorem 1
(see also Figure 3) and put the new link in plat position with the braid β′
being Σ-equivalent to β and having the connecting arc at the top left.
···
···
1
g
1
2
3
2n
···
···
ci
β
(a) ci#β
ci
b
···
1
g
(b) ci#b bβ
···
1
g
(c) bβ′
Figure 14: Normalizing the plat slide move.
Next lemma shows that, up to Σ-equivalence, the plat slide moves psli
(resp. psl∗
i ) do not depend on the point where the band b is attached to ci
(resp. c∗
i ).
Lemma 4. Let ci#bbβ (resp. bβ#bc∗
i ) be the band connected sum, where b
is unlinked with ci (resp. c∗
i ) and connected to ci (resp. c∗
i ) at a small arc
23


## Page 24


e1. Let e′
1 be another small arc on ci (resp. c∗
i ), then there exists a braid β′
which is Σ-equivalent to β and a band b′ which is unlinked with ci (resp. c∗
i )
and connected to ci (resp. c∗
i ) at e′
1, such that ci#bbβ is isotopic to ci#b′ bβ′
(resp. bβ#bc∗
i is isotopic to bβ′#b′c∗
i ).
Proof. We prove the statement in the non-dual case. By Lemma 3 we can
assume that b is connected with the top-left arc of β. Observe that we can
slide the small arc e1 together with the band b along the knot ci towards e′
1
(see Figures 15a and 15b for the case g = 1). In this process it can happen
that the connecting band crosses a lateral surface of G × I, where G is the
fundamental polygon of Σg. If we keep track of the braiding process before
and after that the band crosses a lateral surface, we see that the two braids
diﬀer by either an (M4) or an (M5) move (see Figure 15b). When we reach
e′
1, we can push the braiding of the band to the braid and the entire process
gives rise to a braid β′ (see Figure 15c), which is Σ-equivalent to β so it holds
that ci#b′ bβ′ is isotopic to the original connected sum ci#bbβ.
ci
e1
Σ1 × {1}
b
(a) ci#b bβ
ci
e′
1
Σ1 × {1}
b
(b) sliding b towards e′
1
ci
e′
1
Σ1 × {1}
b′
(c) ci#b′ bβ
Figure 15: Normalizing the plat slide move.
We are ready to prove the main theorem of this paper.
Theorem 3 (Markov theorem). Let L1 and L2 be two links in M such that
bβi = Li with βi ∈∪n∈NBg,2n, with i = 1, 2. Then L1 and L2 are isotopic if and
only if β1 and β2 diﬀer by a ﬁnite sequence of braid isotopy moves (R1), . . . ,
(R4), (TR); M-moves (M1), . . . , (M6); plat slide moves psli, i = 1, . . . , g
and dual plat slide moves psl∗
i , i = 1, . . . , g.
24


## Page 25


Proof. An isotopy between two links in M can be obtained by an isotopy in
Σg × I with the additional freedom to slide across the 2-handles described
by c and the dual 2-handles described by c∗(sliding across 0-handles and
3-handles is of course trivial). Isotopy is thus, by Theorem 2, described by
the M-moves and slide moves along meridian discs. With Lemmas 3 and 4
we have shown that it is enough to consider only the plat slide move psli for
each 2-handle and the dual plat slide move psl∗
i for each dual 2-handle.
If we assume that c∗is the system corresponding to the curves depicted
in Figure 1, then we have c∗
i = bbi. In this case, as the following proposition
shows, the b-type generators are redundant in order to describe a link in M
as the plat closure of a braid β ∈Bg,2n.
Proposition 1. A braid β ∈Bg,2n is Σ-equivalent to a braid β′ ∈Bg,2n
with no b-type generators. Furthermore, all b-type generators can be removed
using M-moves and sl∗
i moves.
Proof. First observe that we can push a b-type generator through an a-type
generator using either (R4) or (R3). Pick the last b generator, i.e. a letter
b±1
i , in the word β (Figure 16a) and make a stabilization move right after the
generator (Figure 16b). For each a-type generator we choose the stabiliza-
tion strands to go either under or over the interfering strands of the a-type
generator in such a way that relations (R3) and (R4) can be applied. We can
now push b to the bottom and remove it by the sl∗
i move (Figures 16c and
16d). We repeat this process until all b-type generators are removed (Figures
16e and 16f)
5
The case of genus one Heegaard splittings
In this section we provide explicit examples of slide moves for manifolds
admitting genus one Heegaard splittings, that is lens spaces, S2 ×S1 and the
25


## Page 26


2
1
(a)
stab.
−−−→
2
1
(b)
(R3)
−−−→
2
1
(c)
psl−1
1
−−−→
2
(d)
stab.
−−−→
2
(e)
(R3), (R4), psl2
−−−−−−−−−−→
(f)
Figure 16: Removing b-type generators from a braid.
3-sphere.
If M is the lens space L(p, q), where p and q are coprime integers such that
0 < q < p, then M has a genus 1 Heegaard splitting, sending the meridian of
H2 to the (p, −q)-curve on the torus T = ∂H1, see Figure 17a for the L(5, 2)
case.
The (p, −q) torus knot is the plat closure of the braid with q generators
b−1
1
evenly distributed between p generators a1 (see also [14, 15]):
αp,q =
rY
i=1
b−1
1 a
⌈p
q ⌉
1
·
q−r
Y
i=1
b−1
1 a
⌊p
q ⌋
1
∈B1,2,
where r ≡p (mod q), see Figure 17b for the L(5, 2) case.
The plat slide move (resp. dual plat slide move) for L(p, q), which we
26


## Page 27


(a) The (5, −2)-knot on T.
1
1
(b) The braid α5,2.
Figure 17: Braiding of the torus knot (5, −2).
denote by pslp,q (resp. psl∗
p,q) is thus
pslp,q : β −→αp,q#β = αp,q β,
psl∗
p,q : β −→β#b1 = β b1.
In particular, for L(p, 1) we have
pslp,1 : β −→b−1
1 ap
1#β = b−1
1 ap
1β.
Beside lens spaces, the only other Heegaard genus one manifold is S2×S1,
which can be viewed as the degenerate lens space L(0, 1).
The manifold
S2 × S1 admits a Heegaard splitting (H1, H2, h), where h : ∂H2 −→∂H1
sends the meridian of H2 to the meridian of H1.
The plat slide moves in this case are:
psl0,1 : β −→b1#β = b1 β,
psl∗
0,1 : β −→β#b1 = β b1.
Lastly, the 3-sphere S3, viewed as the degenerate lens space L(1, 0), ad-
mits a genus 1 Heegaard splitting (H1, H2, h), where h : ∂H2 −→∂H1 is a
homeomorphism that sends the meridian of H2 to the longitude of H1. We
have the following two plat slide moves:
psl1,0 : β −→a1#β = a1β,
psl∗
1,0 : β −→β#b1 = β b1.
27


## Page 28


With the same methods of Proposition 1 we can kill all a1 generators
from a word β ∈B1,2n by moving them to the top and applying the plat slide
move. Every link L ⊂S3 can be thus represented as a closed braid without
a1 or b1 generators and the theory collapses to that of the the usual genus
zero Heegaard splitting of S3 introduced in [6].
References
[1] J. Alexander, A lemma on a system of knotted curves, Proc. Natl. Acad. Sci. USA. 9
(1923), 93–95.
[2] P. Bellingeri, On presentations of surface braid groups, J. Algebra 274 (2004), 543–
563.
[3] P. Bellingeri and A. Cattabriga, Hilden braid groups, J. Knot Theory Ramiﬁcations
21 (2012), 1250029-1–1250029-22.
[4] S. Bigelow, A homological deﬁnition of the Jones polynomial, Geom. Topol. Monogr.
4 (2002), 29–41.
[5] J. Birman, “Braid, links and mapping class group”, Princeton University Press,
Princeton, 1975.
[6] J. Birman, On the stable equivalence of plat representation of knots and links, Canad.
J. Math. 28 (1976), 264–290.
[7] A. Cattabriga, The Alexander polynomial of (1,1)-knots, J. Knot Theory Ramiﬁca-
tions 15 (2006), 1119–1129.
[8] A. Cattabriga and M. Mulazzani, All strongly-cyclic branched coverings of (1,1)-knots
are Dunwoody manifolds, J. Lond. Math. Soc. 70, (2004), 512–528.
[9] A. Cattabriga and M. Mulazzani, Extending homeomorphisms from punctured sur-
faces to handlebodies, Topol. Appl. 155 (2008), 610–621.
[10] P. Cristofori, M. Mulazzani and A. Vesnin: Strongly-cyclic branched coverings of
knots via (g,1)-decompositions, Acta Math. Hungar. 116 (2007), 163–176.
[11] I. Diamantis and S. Lambropoulou, Braid equivalence in 3-manifolds with rational
surgery description, Topol. Appl. 194 (2015), 269–295.
[12] I. Diamantis, S. Lambropoulou and J. Przytycki, Topological steps toward the Hom-
ﬂypt skein module of the lens spaces L(p, 1) via braids, J. Knot Theory Ramiﬁcations
25 (2016), 1650084.
28


## Page 29


[13] H. Doll, A generalized bridge number for links in 3-manifold, Math. Ann. 294 (1992),
701–717.
[14] B. Gabrovšek, Tabulation of Prime Knots in Lens Spaces, Mediterr. J. Math. 14:88
(2017).
[15] B. Gabrovšek and M. Mroczkowski, The HOMFLYPT skein module of the lens spaces
Lp,1, J. Knot Theory Ramiﬁcations 20 (2011), 159–170.
[16] H. Goda, H. Matsuda and T. Morifuji, Knot Floer homology of (1, 1)-knots, Geom.
Dedicata 112 (2005), 197–214.
[17] R. E. Gompf and A. Stipsicz, “4-Manifolds and Kirby Calculus”, American Mathe-
matical Society, Providence, 1999.
[18] P. Heegaard, Forstudier til en topologisk Teori for de algebraiske Fladers Sammen-
hang, Ph.D. thesis, Copenhagen, 1989.
[19] H. M. Hilden, Generators for two groups related to the braid groups, Pacif. J. Math.
59 (1975), 475–486.
[20] S. Lambropoulou and C. P. Rourke, Markov’s theorem in 3-manifolds, Topology
Appl.78 (1997), 95–122.
[21] S. Lambropoulou and C. P. Rourke, Algebraic Markov equivalence for links in 3-
manifolds, Compositio Math. 142 (2006), 1039–1062.
[22] A. A. Markov, Über die freie Äquivalenz geschlossener Zöpfe, Recusil Mathématique
Moscou 1 (1935), 73–78.
[23] J. Milnor, “Morse theory”, Princeton University Press, Princeton, 1963.
[24] Y. Moriah, Heegaard splittings of Seifert ﬁbered spaces, Invent. Math. 91, 465–481
(1988).
[25] M. Mroczkowski, Kauﬀman bracket skein module of a family of prism manifolds, J.
Knot Theory Ramiﬁcations 20 (2011), 159–170.
[26] M. Mroczkowski, Kauﬀman bracket skein module of the connected sum of two projec-
tive spaces, J. Knot Theory Ramiﬁcations 20 (2011), 651–675.
[27] D. Rolfsen, “Konts and Links”, Publish or Perish Press, Berkeley, 1976.
[28] R. Skora, Closed braids in 3-manifolds, Math. Z. 211 (1992), 173–187.
29


## Page 30


Alessia CATTABRIGA
Department of Mathematics, University of Bologna
Piazza di Porta San Donato 5, 40126 Bologna, ITALY
e-mail: alessia.cattabriga@unibo.it
Boštjan GABROVŠEK
Faculty of Mathematics and Physics, University of Ljubljana
Jadranska ulica 19, 1000 Ljubljana, SLOVENIA
e-mail: bostjan.gabrovsek@fmf.uni-lj.si
30

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1801_04766v4_a_markov_theorem_for_generalized_plat_decomposition
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1801_04766V4_A_MARKOV_THEOREM_FOR_GENERALIZED_PLAT_DECOMPOSITION.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

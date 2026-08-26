---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1103.3309
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1103.3309_Auspicious_tatami_mat_arrangements

> Source: 1103.3309_Auspicious_tatami_mat_arrangements.pdf

> Pages: 23

---


## Page 1


arXiv:1103.3309v1  [math.CO]  16 Mar 2011
Auspicious tatami mat arrangements
Alejandro Erickson
ate@uvic.ca
Department of Computer Science
Frank Ruskey
ruskey@uvic.ca
Department of Computer Science
Jennifer Woodcock
jwoodcoc@uvic.ca
Department of Computer Science
University of Victoria
PO BOX 3055, STN CSC, Victoria BC, V8W 3P6, Canada
Mark Schurch
mschurch@uvic.ca
Department of Mathematics and Statistics
University of Victoria
PO BOX 3060, STN CSC, Victoria BC, V8W 3R4, Canada
Submitted: March 4, 2011; Accepted: XX; Published: XX
Mathematics Subject Classiﬁcation: 05B45,05A19
Abstract
An auspicious tatami mat arrangement is a tiling of a rectilinear region with two
types of tiles, 1 × 2 tiles (dimers) and 1 × 1 tiles (monomers). The tiles must cover
the region and satisfy the constraint that no four corners of the tiles meet; such
tilings are called tatami tilings. The main focus of this paper is when the rectilinear
region is a rectangle. We provide a structural characterization of rectangular tatami
tilings and use it to prove that the tiling is completely determined by the tiles that
are on its border. We prove that the number of tatami tilings of an n × n square
with n monomers is n2n−1.
We also show that, for ﬁxed-height, the generating
function for the number of tatami tilings of a rectangle is a rational function, and
outline an algorithm that produces the generating function.
Keywords: tatami, monomer-dimer tiling, rational generating function
1
What is a tatami tiling?
Traditionally, a tatami mat is made from a rice straw core, with a covering of woven
soft rush straw.
Originally intended for nobility in Japan, they are now available in
the electronic journal of combinatorics 16 (2009), #R00
1


## Page 2


(a)
(b)
(c)
Figure 1: (a) Vertical bond pattern.
(b) Horizontal bond pattern.
(c) Herringbone
pattern.
mass-market stores. The typical tatami mat occurs in a 1 × 2 aspect ratio and various
conﬁgurations of them are used to cover ﬂoors in houses and temples. By parity consid-
erations it may be necessary to introduce mats with a 1 × 1 aspect ratio in order to cover
the ﬂoor of a room. Such a covering is said to be “auspicious” if no four corners of mats
meet at a point. Hereafter, we only consider auspicious arrangements, since without this
constraint the problem is the classical and well-studied dimer tiling problem ([6], [10]).
Following Knuth ([7]), we will call the auspicious tatami arrangements, tatami tilings.
The ﬁxed-height enumeration of tatami tilings that use only dimers (no monomers) was
considered in [9], and results for the single monomer case were given in [1].
Perhaps the most commonly occurring instance of tatami tilings is in paving stone
layouts of driveways and sidewalks, where the most frequently used paver has a rectangular
shape with a 1×2 aspect ratio. Two of the most common patterns, the “herringbone” and
the “running bond,” shown in Figure 1, have the tatami property. Consider a driveway
of the shape in Figure 2. How can it be tatami tiled with the least possible number of
monomers? The answer to this question could be interesting both because of aesthetic
appeal, and because it could save work, since to make a monomer a worker typically cuts
a 1 × 2 paver in half.
Before attempting to study tatami tilings in general orthogonal regions it is crucial
to understand them in rectangles, and our results are primarily about tatami tilings of
rectangles.
1.1
Outline
In Section 2 we determine the structure of tatami tilings in a rectangle. Our structural
characterization has important algorithmic implications, for example, it reduces the size
of the description of a tiling from Θ(rc) to O(max{r, c}) and may be used to generate
tilings quickly. The three theorems in Section 3 are the main results of the paper and are
also stated here. The ﬁrst of these concerns the maximum possible number of monomers.
Let T(r, c, m) be the number of tilings of the r × c grid, with m monomers (and the other
tiles being horizontal or vertical dimers).
Theorem 1. If T(r, c, m) > 0, then m has the same parity as rc and m ≤max(r+1, c+1).
the electronic journal of combinatorics 16 (2009), #R00
2


## Page 3


Figure 2: What is the least number of monomers among all tatami tilings of this region?
The answer is provided at the end of the paper in Figure 21.
Following this we prove a counting result for maximum-monomer tilings of square
grids.
Theorem 2. The number of n × n tilings with n monomers, n2n−1.
Our ﬁnal result concerns ﬁxed-height tilings with an unrestricted number of monomers.
Theorem 3. For a ﬁxed number of rows r, the ordinary generating function of the number
of tilings of an r × n rectangle is a rational function.
We also provide an algorithm which outputs this generating function for a given r and
explicitly give the generating function for r = 1, 2 and 3, along with the coeﬃcients of
the denominator for 1 ≤r ≤11. In Section 4 we return to the question of tatami tiling
general orthogonal regions and introduce the “magnetic water strider problem” along with
additional conjectures and open problems.
2
The structure of tatami tilings: T-diagrams
We show that all tatami tilings have an underlying structure which partitions the grid
into regions, where each region is ﬁlled with either the vertical or horizontal running bond
pattern (or is a monomer not touching the boundary). For example, in Figure 3 there are
11 regions, including the interior monomer. We will describe this structure precisely and
prove some results for tilings of rectangular grids.
Wherever a horizontal and vertical dimer share an edge
, either the placement of
another dimer is forced to preserve the tatami condition, or the tiles make a T with the
the electronic journal of combinatorics 16 (2009), #R00
3


## Page 4


Figure 3: A tiling showing all four types of sources. Coloured in magenta, from left to
right they are, a clockwise vortex, a vertical bidimer, a loner, a vee, and another loner.
Jagged edges are indicated by brackets.
(a)
A
loner
source.
(b) A vee source.
Figure 4: These two types of sources must have their coloured tiles on a boundary, as
shown, up to rotational symmetry.
boundary of the grid
. In the former case, the placement of the new dimer again
causes the sharing of an edge
, and so on
, until the boundary is reached.
The successive placement of dimers, described above gives rise to skinny herringbone
formations, which we call rays. They propagate from their source to the boundary of
the grid and cannot intersect one another. Between the rays, there are only vertical or
horizontal running bond patterns. The intersection of a running bond with the boundary is
called a segment. This segment is said to be jagged if it consists of alternating monomers
and dimers orthogonal to the boundary; otherwise it is said to be smooth because it
consists of dimers that are aligned with the boundary. Every jagged segment is marked
with square brackets in Figure 3.
We know that a ray, once it starts, propagates to the boundary. But how do they
start? In a rectangular grid, we will show that a ray starts at one of four possible types
of sources. In our discussion we use inline diagrams to depict the tiles that can cover the
grid squares at the start of a ray. We need not consider the case where the innermost
square (denoted by the circle)
is covered by a vertical dimer
because this would
move the start of the ray.
If it is covered by a horizontal dimer
, the source, which consists of the two dimers
that share a long edge, is called a bimer. Otherwise it is covered by a monomer
in
which case we consider the grid square beside it
. If it is covered by a monomer the
source is called a vee
; if it is covered by a vertical dimer the source is called a vortex
; if it is covered by a horizontal dimer it is called a loner
. Each of these four types
of sources forces at least one ray in the tiling and all rays begin at either a bidimer, vee,
the electronic journal of combinatorics 16 (2009), #R00
4


## Page 5


Figure 5: A vertical and a horizontal bidimer source. A bidimer may appear anywhere in
a tiling provided that the coloured tiles are within the boundaries of the grid.
Figure 6: A counter clockwise and a clockwise vortex source.
A vortex may appear
anywhere in a tiling provided that the coloured tiles are within the boundaries of the
grid.
vortex or loner. The diﬀerent types of features are depicted in Figures 4-6.
The coloured tiles in Figures 4-6 characterize the four types of sources. A bidimer
or vortex may appear anywhere in a tiling, as long as the coloured tiles are within its
boundaries. The vees and loners, on the other hand, must appear along a boundary, as
shown in Figure 4.
The collection of bold staircase-shaped curves in each of the four types of source-ray
drawings in Figures 4-6, is called a feature. These features do not intersect when drawn
on a tatami tiling because rays cannot intersect. A feature-diagram refers to a set of non-
intersecting features drawn in a grid. Not every feature-diagram admits a tatami tiling;
those that do are called T-diagrams. See Figure 7.
(a)
(b)
Figure 7: (a) The T-diagram of Figure 3. (b) A feature diagram that is not a T-diagram.
Recall that a tatami tiling consists of regions of horizontal and vertical running bond
patterns. A feature-diagram is a T-diagram if and only if each pair of rays bounding the
same region admit bond patterns of the same orientation and the distance between them
has the correct parity. The precise conditions are stated in Lemma 1.
the electronic journal of combinatorics 16 (2009), #R00
5


## Page 6


Features decompose into four types of rays, to which we assign the symbols NW, NE,
SW, and SE, indicating the direction of propagation. Two rays are said to be adjacent if
they can be connected by a horizontal or vertical line segment which intersects no other
ray. If (α, β) is an adjacent pair, then α is on the left when considering horizontally
adjacent pairs and on the bottom when considering vertically adjacent pairs.
Lemma 1. A feature diagram is a T-diagram if and only if the following four conditions
hold.
Horizontal Conditions:
(H1) There are no horizontal (αE, βE)-adjacencies, nor are there horizontal (αW, βW)-
adjacencies, where α and β are either N or S (Figure 8);
(H2) all distances are even, except for horizontal (NE, NW)-distances and horizontal
(SE, SW)-distances, which are odd (Figure 9).
Vertical Conditions:
(V1) There are no vertical (Sα, Sβ)-adjacencies, nor are there any vertical (Nα, Nβ)-
adjacencies, where α and β are either E or W;
(V2) all distances are even, except for vertical
(NW, SW)-distances and vertical (NE, SE)-distances, which are odd.
SE
SE
NE
Figure 8: Incompatible pairs of adjacent rays.
The region between the adjacent rays
would have to contain both horizontal and vertical dimers.
SE
SW
NE
SE
SW
NE
Figure 9: If the size of the gap between adjacent rays has the correct parity then it can be
properly tiled, as shown on the left. On the right, the red regions cannot be tiled because
the gaps have the wrong parities.
This characterization has some implications for the space and time complexity of a
tiling.
the electronic journal of combinatorics 16 (2009), #R00
6


## Page 7


Lemma 2. Let G be an r × c grid, with r < c.
(i) The storage requirement for a tatami tiling of G is O(c); that is, a tatami tiling can
be recovered from O(c) integers, each of size at most c.
(ii) A tatami tiling of G is uniquely determined by the tiles on its boundary.
(iii) Whether a feature diagram in G is a T-diagram can be determined in time O(c).
Proof. To prove (i), notice that a non-trivial T-diagram deﬁnes a tiling uniquely. In the
trivial case there are no features and exactly four possible running bond conﬁgurations,
two horizontal and two vertical.
Otherwise, each feature can be stored as a pair of
coordinates and a type. It is not possible to have more than O(c) compatible features in
a T-diagram in G, so at most O(c) integers of size at most c are needed, proving (i).
To prove (ii), we need to show that we can recover the T-diagram from the tiles that
touch the boundary. Those portions of the T-diagram corresponding to vees and loners,
as well as bidimers whose source tiles are both on the boundary
, are easy to recover.
The black rays in Figure 10 show their recovery. Imagine ﬁlling in the remaining red rays,
whose ends look like
, by following them na¨ıvely, backwards from their endings to the
boundary. The ends of the four rays emanating from a bidimer or vortex will always form
exactly one of the four patterns illustrated in Figure 11; in each case, it is straightforward
to recover the position and type of source. This proves (ii).
Figure 10: The same tiling as in Figure 3 with only the boundary tiles showing. Rays
emanating from sources on the boundary are in black and otherwise, they are drawn
na¨ıvely in red, to be matched with a candidate source from Figure 11.
Figure 11: The four types of vortices and bidimers are recoverable from the ends of their
rays, at the boundary of the grid. Given the ends of rays, they can be extended na¨ıvely
to form one of the two patterns in red. One occurs only for bidimers and the other for
vortices. The orientation of the source is determined by the ends of the rays.
the electronic journal of combinatorics 16 (2009), #R00
7


## Page 8


Claim (iii) is true provided that Lemma 1 only needs to be applied to O(c) ray-
adjacencies. Notice that a pair of rays can be adjacent and yet not be adjacent on the
boundary. For example, it happens in Figure 7.
Each ray bounds exactly two regions, each of which is bounded by at most three other
rays, and two rays must bound the same region to be adjacent. Thus, a ray is adjacent
to at most six other rays. Let the ray-adjacencies be the edges of a graph G = (V, E)
whose vertex set is the set of rays, so that G has maximum degree at most 6. Therefore,
the number of ray-adjacencies, |E|, and hence applications of Lemma 1, is linear in the
number of rays, |V |, which is at most four times the number of features, which is in O(c).
This proves (iii).
The T-diagram structure is a useful tool for enumerating and generating tatami tilings
as will be illustrated in the following sections.
3
Counting results
Let T(r, c, m) be the number of tatami tilings of a rectangular grid with r rows, c columns,
and m monomers. Also, T(r, c) will denote the sum
T(r, c) =
X
m≥0
T(r, c, m).
We begin by giving necessary conditions for T(r, c, m) to be non-zero.
Theorem 1. If T(r, c, m) > 0, then m has the same parity as rc and m ≤max(r+1, c+1).
Proof. Let r, c and m be such that T(r, c, m) > 0 and let d be the number of grid squares
covered by dimers in an r × c tatami tiling so that m = rc −d. Since d is even, m must
have the same parity as rc.
It suﬃces to assume that r ≤c, and prove that m ≤c + 1. The proof proceeds in two
steps. First, we will show that a monomer on a vertical boundary of any tiling can be
mapped to the top or bottom, without altering the position of any other monomer. Then
we can restrict our attention to tilings where all monomers appear on the top or bottom
boundaries, or in the interior. Secondly, we will show that there can be at most c + 1
monomers on the combined horizontal boundaries.
Let T be a tatami tiling of the r × c grid with a monomer µ on the left boundary,
touching neither the bottom nor the top boundary. The monomer µ is (a) part of a vee
or a loner, or (b) is on a jagged segment of a region of horizontal bond. Deﬁne a diagonal
to be µ together with a set of dimers in this region which form a stairway shape from
µ to either the top or bottom of the grid as shown in purple in Figure 12a. If such a
diagonal exists, a diagonal ﬂip can be applied, which changes the orientation of its dimers
and maps µ to the other end of the diagonal. In case (a) a diagonal clearly exists since it
is a source and its ray will hit a horizontal boundary because r ≤c.
If µ is on a jagged segment, then we argue by contradiction. Suppose neither diagonal
exists, then they must each be impeded by a distinct ray. Such rays have this horizontal
the electronic journal of combinatorics 16 (2009), #R00
8


## Page 9


(a) A diagonal ﬂip.
(b) The case for vees.
α
β
γ
δ
c′
(c)
Figure 12: (c) If both diagonals are blocked, then c < r. The tiling is at least this tall
and at most this wide.
region to the left so the upper one is directed SE and the lower NE and they meet the
right boundary (before intersecting). Referring to Figure 12c,
α + β + j =γ + δ + 1 ≤r
≤c ≤c′ = α + γ = β + δ,
where j is some odd number. Thus α + β + j ≤α + γ implying that β < γ. On the other
hand,
γ + δ + 1 = r ≤c ≤c′ = β + δ
implies that γ < β, which is a contradiction. Therefore at least one of the diagonals exists
and the monomer can be mapped to a horizontal boundary.
We may now assume that there are no monomers strictly on the vertical boundaries of
the tiling, and therefore all monomers are either in the top or bottom rows or in vortices.
Let v be the number of vortices. Encode the bottom and top rows of the tiling by length
c binary sequences P and Q, respectively. In the sequences, 1s represent monomers and
0s represent squares in dimers.
If Q contains a consecutive pair of 1s, this represents a vee in the top row; the vee has
a region of horizontal dimers directly below it. This region of horizontal bond must reach
the bottom row somewhere, otherwise, by an argument similar to one given previously,
we would have c < r (see Figure 13a). Therefore, there must be a consecutive pair or 0s
in P unique to these 1s in Q. Modify Q so that the 11 becomes a 1, and modify P so that
the 00 becomes 010. Do this for each consecutive pair of 1s in P and Q, as illustrated in
Figure 13b. The updated P and Q sequences contain no consecutive pairs of 1s, but the
total number of 1s remains unchanged.
Now we show that for each of the v vortices, a 00 can be removed from each of P and
Q and there will still be no consecutive pairs of 1s in the new sequences. Each vortex
generates 4 rays; at least one of these rays will hit the top boundary, and at least one will
hit the bottom boundary. In fact, a horizontal and a vertical dimer on either side of the
ray will lie on the upper boundary, and similarly for the bottom boundary. Figure 13a is
helpful in seeing why this is true. These dimers on either side of the ray induce a 000 in
P and another 000 in Q. (Although not used in this proof, note that the comments above
also apply to bidimers.) In total, there are at least v distinct triples of 0s in each sequence,
one for each vortex. Now remove 00 from each triple as in Figure 13b. The updated P and
the electronic journal of combinatorics 16 (2009), #R00
9


## Page 10


Q sequences have a combined length of 2c −4v and neither of them contains a 11. Thus
the total number of 1s is at most ⌈|P|/2⌉+ ⌈|Q|/2⌉, which is at most c −2v + 1. Adding
back the v vortex monomers, we conclude that there are at most c −v + 1 monomers in
total, which ﬁnishes the proof.
Note that, to acheive the bound of c + 1, we must have v = 0, and that the maximum
is achieved by a vertical bond pattern.
(a)
11
1×
00 · · ·
010 · · ·
000 · · ·
000 · · ·
0 × × · · ·
0 × × · · ·
T = · · ·
S = · · ·
T = · · ·
S = · · ·
(b)
Figure 13: Each vortex and vee is associated with segments of monomer-free grid squares
shown in purple. (a) Segments associated with vortices have length at least three. Those
associated with vees have at least two 0s. (b) The two types of updates to sequences P
and Q. The upper sequences are before the updates and the lower are after updates. The
symbol × represents a deletion from the sequence.
The converse of Theorem 1 is false, for example, Alhazov et al.
([1]) show that
T(9, 13, 1) = 0. We now state a couple of consequences of Theorem 1.
Corollary 1. The following three statements are true for tatami tilings of an r × c grid
with r ≤c.
(i) The maximum number of monomers in a r ×c grid is c+1 if r is even and c is odd;
otherwise it is c. There is a tatami tiling achieving this maximum.
(ii) A tatami tiling with the maximum number of monomers has no vortices.
(iii) A tatami tiling with the maximum number of monomers has no bidimers.
Proof. (i) That this is the correct maximum value can be inferred from Theorem 1. A
tiling consisting only of vertical running bond achieves it, for example.
(ii) This was noted at the end of the proof of Theorem 1.
(iii) We can again use the same sort of reasoning that was used for vortices in Theorem
1, but there is no need to “add back” the monomers, since bidimers do not contain one.
the electronic journal of combinatorics 16 (2009), #R00
10


## Page 11


ρ
γ
δ
A(T)
Figure 14: In the tiling T from Lemma 3, the ray ρ belongs to the corner γ and it is
associated with the diagonal δ.
The area A(T) counts the grid squares that are not
between any ray and its corner. The monomer that is moved in the diagonal ﬂip becomes
part of A(T ′) and is therefore moved only once in the sequence. The corner monomers
are never moved.
3.1
Square tatami tilings
In this section, we show that T(n, n, n) = n2n−1. Theorem 2 relies on the following lemma
and corollary.
Lemma 3. For each n × n tiling with n monomers, a trivial tiling can be obtained via a
ﬁnite sequence of diagonal ﬂips in which each monomer moves at most once. Reversing
this sequence returns us to the original tiling.
Proof. Let T be the T-diagram of an n × n tiling with n monomers. Each ray ρ in T
touches two adjacent boundaries which form a corner γ, so ρ and γ are said to belong to
each other. For each corner γ, choose the ray which belongs to it and is farthest away
from it; if a corner does not have a ray, then choose the corner itself. Between the four
chosen rays/corners, our tiling can only contain either horizontal or vertical running bond
(by Lemma 1). Let A(T) be the area of this central running bond.
We begin a sequence of diagonal ﬂips by choosing one ray ρ that is farthest from its
corner and ﬂipping the diagonal δ touching ρ that is between ρ and its corner. Let T ′ be
the resulting T-diagram. In T, δ is not part of the central running bond and in T ′, it is;
thus A(T ′) > A(T). Continuing this process yields a trivial tiling via a ﬁnite sequence of
diagonal ﬂips.
Corollary 2. Every n × n tiling with n monomers has two corner monomers and they
are in adjacent corners.
Proof. The sequence of diagonals chosen for diagonal ﬂips described in Lemma 3 never
includes a diagonal containing a corner monomer because such a diagonal is never between
a ray and its associated corner. As such, the corner monomers are ﬁxed throughout the
sequence of diagonal ﬂips yielding a trivial tiling.
Since a trivial n × n tiling with n
the electronic journal of combinatorics 16 (2009), #R00
11


## Page 12


monomers has two monomers in adjacent corners, then, so must every other n × n tiling
with n monomers.
Corollary 2 show that the four rotations of any n × n tiling with n monomers are
distinct. We call the rotation with monomers in the top two corners the canonical case.
Theorem 2. The number of n × n tilings with n monomers, T(n, n, n), is n2n−1.
Proof. We count the n×n tilings with n monomers up to rotational symmetry by counting
the canonical cases only. Let S(n) = T(n, n, n)/4. We will give a combinatorial proof
that S(n) satisﬁes the following recurrence:
S(n) = 2n−2 + 4S(n −2) = n2n−3 where S(1) = S(2) = 1.
(1)
In Theorem 1 we deﬁned a diagonal ﬂip which results in a monomer µ moving up or down
depending on the orientation of its diagonal. As such, we simplify our terminology by
referring to ﬂipping a monomer in a particular direction (up, down, left, or right).
We treat the even and odd cases separately, though the proofs are naturally similar.
In both cases, we begin with the canonical trivial case and consider all possible sequences
of ﬂips in which each monomer is moved at most once and the corner monomers are ﬁxed.
By Lemma 3 and its corollary, this counts the canonical tilings.
The canonical trivial case for even n, shown in Figure 15a for n = 8, is a horizontal
running bond tiling with ﬁxed (black) monomers in the top corners and n/2 (red and
yellow) monomers on both the left and right boundaries. We classify the tilings according
to what happens to the bottom (yellow) monomer on each of these boundaries, which we
will call w and e.
e
w
(a)
e
w
(b)
(c)
e
w
(d)
Figure 15: (a) Canonical trivial case for an 8 × 8 square with 8 monomers. (b) Flipping
w up. (c) 180 degree rotation of the canonical trivial case for a 6 × 6 square with 6
monomers. (d) An 8 × 8 tiling with its associated 6 × 6 tiling.
First, suppose µ ∈{w, e} is ﬂipped up as shown in Figure 15b. Because our tiling is
square, this ﬂip inhibits any orthogonal diagonal ﬂips and thus the monomers that shared
a boundary with µ before it was ﬂipped up can only be ﬂipped up and monomers on the
opposite boundary can only be ﬂipped down. There are n −3 such monomers that are
not ﬁxed and can be ﬂipped independently of each other. This gives 2n−3 possibilities
when either w or e is ﬂipped up, resulting in a total of 2n−2 tilings.
If neither w nor e is ﬂipped up, these monomers can be ﬂipped (or not) independently
of each other and of other non-ﬁxed monomers, as shown in Figure 16. As such, we can
the electronic journal of combinatorics 16 (2009), #R00
12


## Page 13


Figure 16: The four possibilities for ﬂipping w and/or e down.
now ignore what happens to w and e and consider them ﬁxed, keeping in mind that for
each such tiling, there are three others with w and e in diﬀerent positions. We will ﬁnd a
one-to-one correspondence between these tilings and one quarter of the (n −2) × (n −2)
tilings with n −2 monomers by mapping the monomers of the canonical trivial cases
(rotated by 180 degrees in the smaller case) and showing that any sequence of ﬂips in one
case can be applied to the equivalent monomers in the other.
There are n−4 (red) monomers on the left and right boundaries of the n×n canonical
case that we have not ﬁxed. Consider the 180 degree rotation of the canonical trivial case
for (n−2)×(n−2) tilings with n−2 monomers which has ﬁxed (black) monomers in the
bottom corners, as shown in Figure 15c for n −2 = 6. Associate the n −4 non-ﬁxed (red)
monomers of this tiling with the n −4 non-ﬁxed (red) monomers of the n × n canonical
trivial case in a natural way: pairing those in the same position relative to the bottom
ﬁxed monomers. Similarly, diagonals containing associated monomers are also associated.
We need to show that compatibility between diagonal ﬂips is preserved between the
smaller and larger cases: that is, if two diagonals cannot both be ﬂipped in the larger
square, the same is true for the corresponding diagonals in the smaller square, and vice
versa.
In both cases, two monomers on the same boundary can both be ﬂipped if and only if
they are either ﬂipped in the same direction or the top one is ﬂipped up and the bottom
one is ﬂipped down; compatibility is preserved.
For a pair of monomers on opposite boundaries, observe that a conﬂict between ﬂips
can only occur if we try to ﬂip them both in the same direction. Further, conﬂict depends
entirely on the distance of the monomers from the horizontal centerline of the grid. Let dw
and de respectively be the distances from the horizontal centerline, with negative values
below the line and positive values above. If dw + de > 0, then the two monomers cannot
both be ﬂipped down, and similarly, if dw + de < 0, they cannot both be ﬂipped up. This
distance is preserved between the associated monomers in the larger and smaller squares
and thus compatibility is also preserved.
There are S(n −2) ways of ﬂipping the monomers of the (rotated) (n −2) × (n −2)
canonical trivial case, and thus S(n −2) ways of ﬂipping the corresponding monomers
of the n × n canonical trivial case. This yields 4S(n −2) tilings, one for each way of
positioning w and e and establishes (1) for even n.
The canonical trivial case for odd n, shown in Figure 17a for n = 7, is a vertical
running bond tiling with (black) monomers in the top corners. It has ⌈n/2⌉monomers
on the top boundary and ⌊n/2⌋monomers on the bottom boundary. Label the bottom
left and bottom right monomers w and e respectively.
the electronic journal of combinatorics 16 (2009), #R00
13


## Page 14


w
e
(a)
w
e
(b)
(c)
e
w
(d)
Figure 17: (a) Canonical trivial case for a 7 × 7 square with 7 monomers. (b) Flipping w
to the right. (c) Canonical trivial case for a 5 × 5 square with 5 monomers. (d) An 7 × 7
tiling with its associated 5 × 5 tiling.
Figure 18: The four possibilities for ﬂipping (or not ﬂipping) w and e to the left and right
respectively.
Similar to the even case, if either w is ﬂipped right (as in Figure 17b) or e is ﬂipped
left, there are n −3 monomers which can be ﬂipped independently to obtain other tilings
and this yields 2n−2 tilings.
Otherwise, w and e can be ﬂipped left and right (respectively) independently of each
other and of other monomers, as shown in Figure 18. Again we ﬁx w and e, keeping in
mind that for each such tiling, there are three others with w and e in diﬀerent positions.
We will ﬁnd a similar one-to-one correspondence to the one in the even case.
There are n −4 (red) monomers on the top and bottom boundaries of the canonical
trivial case that we have not ﬁxed. Once again, we associate these monomers with those of
the 180 degree rotation of the (n−2)×(n−2) canonical trivial case with n−2 monomers
which has ﬁxed (black) monomers in the bottom corners. Arguing as in the even case, with
a vertical centerline rather than a horizontal one, we conclude that a pair of monomers in
the n × n tiling can be ﬂipped if and only if the corresponding ﬂips can be made in the
(n −2) × (n −2) tiling. Again this yields 4(S(n −2)) tilings and establishes (1) for odd
n.
3.2
Fixed height tatami tilings
In this section we show that for a ﬁxed number of rows r, the ordinary generating function
of the number of tilings of an r ×c rectangle is a rational function. We will show that, for
each value of r, the number of ﬁxed-height tilings satisﬁes a system of linear recurrences
with constant coeﬃcients. We will derive the recurrences for small values of r and then
discuss an algorithm which can be used for larger values of r.
the electronic journal of combinatorics 16 (2009), #R00
14


## Page 15


Let Tr(z) denote the generating function
Tr(z) =
X
c≥0
T(r, c)zc.
For c ≥2, a tatami tiling of a 1 × c rectangle begins with either a monomer or a dimer.
Thus, T(1, c) = T(1, c −1) + T(1, c −2) for c ≥2, where T(1, 0) = 1 and T(1, 1) = 1.
This is the well known Fibonnaci recurrence. Since it is a linear recurrence with constant
coeﬃcients, it is not a diﬃcult task to verify that
T1(z) =
1 + z
1 −z −z2.
For each r ≥2 we derive a recurrence based on partial tilings which can be solved using
mathematical software such as Maple. A partial tiling of an r × c grid is a minimal r × k
tiling if and only if the ﬁrst k columns are covered and no tile lies entirely outside of these
columns. The r and k may sometimes be omitted. Let Sr be the set of conﬁgurations
which correspond to a minimal r × 1 tiling.
For sv ∈Sr, let v be a ternary r-tuple
whose elements correspond to the grid squares of the ﬁrst column, ordered from top to
bottom. The elements 0, 1, and 2, each represent a grid square covered by a vertical dimer,
monomer, or horizontal dimer, respectively. Note that 0s always appear in consecutive
pairs. For example, s0012002 ∈S7 corresponds to the minimal 7 × 1 tiling shown in Figure
19a.
(a)
(b)
(c)
Figure 19: (a) The minimal 7×1 tiling corresponding to s0012002. (b) A possible extension
of the minimal tiling in (a). (c) Removing the ﬁrst column yields a new minimal tiling,
represented by s2001211.
For c ≥1, let tr,v(c) be the number of tilings of an r × c rectangle that begin with
the minimal r × 1 tiling sv. Note that tr,v(1) = 1 if v does not contain a 2, and is zero
otherwise. To derive a recurrence we determine all ways of extending each conﬁguration
in sv to a minimal r ×2 tiling. By taking each of these minimal r ×2 tilings and chopping
oﬀthe ﬁrst column we can match these tilings to an element in Sr which will deﬁne a
recurrence. Figure 19b shows an extension of the tiling s0012002 and Figure 19c shows that
this extension corresponds to the conﬁguration s2001211. Notice that Figure 19c can only
be extended once more.
Lemma 4. T2(z) =
1+2z2−z3
1−2z−2z3+z4.
the electronic journal of combinatorics 16 (2009), #R00
15


## Page 16


Proof. For r = 2, we have S2 = {s00, s11, s12, s21, s22}. Since S2 contains all possible ways
to start a tiling of an r × c rectangle, with c ≥2, it follows that
T(2, c) = t00(c) + t11(c) + t12(c) + t21(c) + t22(c).
(2)
The initial conditions are t00(1) = 1, t11(1) = 1, t12(1) = 0, t21(1) = 0, and t22(1) = 0. To
derive the recurrence we consider the ways of extending each of the minimal 2 × 1 tilings
in S2 to a minimal 2 × 2 tiling.
Start
Extensions
Recurrences
S00
t00(c) = t00(c −1) + t11(c −1) + t12(c −1) + t21(c −1) + t22(c −1)
S11
t11(c) = t00(c −1)
S12
t12(c) = t11(c −1) + t21(c −1)
S21
t21(c) = t11(c −1) + t12(c −1)
S22
t22(c) = t11(c −1)
By solving the system of recurrences deﬁned by these ﬁve cases and Equation (2) we
arrive at the stated result for r = 2.
The process outlined in the proof of Lemma 4 can be implemented in an algorithm.
We determine the set Sr with an exhaustive search. Then, for each element sv ∈Sr,
we list all extensions to a minimal r × 2 tiling. Each extension of sv produces a unique
sum-term in the recurrence for tv(c). Once again, the initial conditions are
tv(1) =
 1,
if v contains a 2,
0,
otherwise.
the electronic journal of combinatorics 16 (2009), #R00
16


## Page 17


We may reduce the number of equations in the system of recurrences by ignoring
elements of Sr which cannot be extended to a minimal r × 2 tiling. This may be taken
further by determining necessary conditions for an element of Sr to be extendible to an
r × c tiling.
The algorithm produces a system of linear recurrences with constant coeﬃcients. This
proves the following result.
Theorem 3. For a ﬁxed number of rows r, the ordinary generating function for the
number of tilings of an r × n rectangle is a rational generating function.
The output of our algorithm for r = 3 gives the following generating function:
T3(z) = 1 + 2z + 8z2 + 3z3 −6z4 −3z5 −4z6 + 2z7 + z8
1 −z −2z2 −2z4 + z5 + z6
.
It is impractical to include the complete generating function for any larger values of
r. The degrees for the numerators and denominators, however, as well as the coeﬃcients
in the denominators are given in Table 1 for r = 1, 2, ..., 11. The salient patterns in these
coeﬃcients are summarized in Conjectures 1 and 2. Note that Conjecture 1(a) implies
g(z) is a self-reciprocal polynomial for r ≡2 (mod 4).
Conjecture 1. Let Tr(z) = f(z)
g(z), where f(z) and g(z) are relatively prime polynomials,
and deg(g(z)) = n, and r ≥1. Then,
g(z) =
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


−zng
 1
z

,
if r ≡0
(mod 4),
−zng

−1
z

,
if r ≡1
(mod 4),
zng
 1
z

,
if r ≡2
(mod 4),
zng

−1
z

,
if r ≡3
(mod 4).
A mod 4 pattern also seems to occur in the degrees of the denominators of Tr(z). The
rigid structure we encounter in tatami tilings prompts us to infer this pattern upon all
values as well.
Conjecture 2. Let g(z) be the denominator of Tr(z). Then,
deg(g(z)) =









8m2 + 2m + 1,
if r ≡0
(mod 4),
8m2 + 4m + 2,
if r ≡1
(mod 4),
8m2 + 10m + 4,
if r ≡2
(mod 4),
8m2 + 8m + 6,
if r ≡3
(mod 4).
the electronic journal of combinatorics 16 (2009), #R00
17


## Page 18


r
p
q
Coeﬃcients of g(z) ordered from left to right by ascending degree and then
folded like these arrows;
for r ≤3,
for r = 4, 5, 6, 7, and
for r ≥8.
1
1
2
1,-1,1
2
3
4
1, -2, 0, -2, 1
3
8
6
1, -1, -2, 0, -2, 1, 1
4
14
11
-1, 1, 1, 1,-1, 7
1,-1,-1,-1, 1,-7
5
18
14
-1, 1, 1,-1, 3,-1, 5,-2
1, 1,-1,-1,-3,-1,-5
6
27
22
1,-1,-1, 1,-1,-2, 2,-10, 9,-1, 4, 6
1,-1,-1, 1,-1,-2, 2,-10, 9,-1, 4
7
28
22
1,-1,-3, 3, 4,-4,-9, 7, 6,-5, 2, 0
1, 1,-3,-3, 4, 4,-9,-7, 6, 5, 2
8
44
37
-1, 1, 1,-1, 1,-1, 1, 3,-3, 13,-12
1,-1,-1, 1,-1, 1,-1,-3, 3,-13, 12
34,-2, 6, 20,-6, 12, 0, 0
-34, 2,-6,-20, 6,-12, 0, 0
9
50
42
-1, 1, 1,-1, 1,-1, 1,-1, 5,-3, 11,-8
1, 1,-1,-1,-1,-1,-1,-1,-5,-3,-11,-8
10, 24, 2, 28, 2, 20, 8, 14, 4, 6
-24, 2,-28, 2,-20, 8,-14, 4,-6
10
65
56
1,-1,-1, 1,-1, 1,-1, 1,-1,-4, 4,-16, 15, 1,-1
1,-1,-1, 1,-1, 1,-1, 1,-1,-4, 4,-16, 15, 1,-1
-120, 68,-78,-18, 18,-66, 66,-2, 7, 41,-23, 33,-17, 17
68,-78,-18, 18,-66, 66,-2, 7, 41,-23, 33,-17, 17
11
64
54
1,-1,-5, 5, 13,-13,-27, 27, 48,-48,-83, 81, 125,-120,-160
1, 1,-5,-5, 13, 13,-27,-27, 48, 48,-83,-81, 125, 120,-160
-34, 83, 89,-156,-165, 199, 210,-202,-206, 185, 193,-154
-34,-83, 89, 156,-165,-199, 210, 202,-206,-185, 193, 154
Table 1: Summary of generating function attributes for ﬁxed height tilings, r = 1, ..., 11,
and where p and q are the degrees of the numerator and denominator of Tr(z), respectively.
The degree ordering shows the patterns of Conjecture 1.
the electronic journal of combinatorics 16 (2009), #R00
18


## Page 19


4
More conjectures and further research
The T-diagram structure removes much of the mystery from tatami tilings and motivates
considerable future work. In this section we list some open problems and conjectures,
beginning with another counting problem on rectangular grids.
4.1
Rectangular regions
Conjecture 3. For all d ≥0 and m ≥1 there is an n0 such that, for all n ≥n0.
T(n, n + d, m) = T(n0, n0 + d, m),
whenever n(n + d) has the same parity as m (otherwise T(n, n + d, m) = 0, by Theorem
1).
Experimentally, it appears that the smallest n0 is m + d + 4, if d ≥1.
The easiest case occurs when d = 0 and m = 1. It is not hard to show that for all odd
n ≥3 we have T(n, n, 1) = 10 (the single monomer must go at a corner or in the center).
In a subsequent paper we will show that for m < n,
T(n, n, m) = m2m + (m + 1)2m+1,
whenever m and n have the same parity.
Returning to the subject of generating functions, ignoring signs, it appears that the
denominators of Tr(z) in Section 3.2 are self-reciprocal. There must be a combinatorial
explanation for this. Similar questions in the non-tatami case are considered in [2].
Generating functions also appear in Conjecture 4, inspired by conversations with
Knuth. Let T(n, z) be the generating polynomial for the number of n × n tilings with n
monomers and i vertical dimers. Once again, to count such tilings we consider ﬂipping
diagonals, with the added precaution that the sum of the number of tiles in the ﬂipped
diagonals is a given constant. The relationship between this and subsets of {1, . . . , n}
which have a given sum is detailed in a subsequent publication.
Let φn(z) denote the nth cyclotomic polynomial. Recall that the roots of φn(z) are
the primitive roots of unity. One of their more well-known properties is that
1 −zn =
Y
d|n
φd(z).
(3)
Let Sn(z) denote the ordinary generating function of subsets of {1, . . . , n} which have
a given sum. That is, ⟨zk⟩Sn(z) is the number of subsets A of
{1, 2, . . . , n} such that the sum of the numbers in A is k. It is not diﬃcult to see that
Sn(z) = (1 + z)(1 + z2) · · ·(1 + zn) =
n
Y
k=1
(1 + zk).
(4)
the electronic journal of combinatorics 16 (2009), #R00
19


## Page 20


Let ν(n) denote the number of 2s in the prime factorization of n and note that
1 + zn = 1 −z2n
1 −zn =
Q
d|2n φd(z)
Q
d|n φd(z) =
Y
d|2n
d∤n
φd(z) =
Y
d|n
d odd
φ21+ν(n)d(z).
When this latter expression is used in Sn(z) some interesting simpliﬁcation occurs.
Lemma 5. For all n ≥1,
Sn(z) =
n
Y
j=1
(φ2j(z))⌊n+j
2j ⌋
Proof. The index 2j will occur for those ks in Equation (4) for which j = 2ν(k)d for some
odd d where d | k. This equation is satisﬁed for k = j, 3j, 5j, . . .. There are ⌊(n+ j)/(2j)⌋
such ks that are less than or equal to n (See Figure 20).
0
n
j
3j
7j
0
n + j
j
4j
8j
Figure 20: A visual aid for the last line of the proof of Lemma 5. The pink dots represent
the sequence, j, 3j, 5j, . . ., with ij ≤n. Adding j to n shows that the number of dots is
⌊(n + j)/(2j)⌋.
Conjecture 4. The generating polynomial T(n, z) has the factorization
T(n, z) = P(n, z)
Y
j≥1
S⌊n−1
2j ⌋(z)
where P(n, z) is an irreducible polynomial.
We return to the topic mentioned in the introduction: Tatami-tilings of orthogonal
regions.
the electronic journal of combinatorics 16 (2009), #R00
20


## Page 21


(a)
(b)
Figure 21: (a) The solution to the question posed in Figure 2; no monomers are required
to tatami tile the region. (b) A legal conﬁguration of six magnetic water striders in an
orthogonal “pond”. Note that no further striders may be added.
4.2
Orthogonal regions
We believe that the main structural components are the same as they were for rectangles,
but there are a few subtleties to be clariﬁed at inside corners, since a ray could begin at
such a place.
What is the computational complexity of determining the least number of monomers
that can be used to tile an orthogonal region given the segments that form the boundary
of the region and the unit size of each dimer/monomer? In the rectangular grid this is
answerable in polynomial time using T-diagrams, however, it appears to be NP-hard for
an arbitrary number of segments.
The problem of minimizing the number of monomers in a tiling inspires what we
call the “magnetic water strider problem”. This time the orthogonal region is a pond
populated by water striders. A water strider is an insect that rides atop water in ponds
by using surface tension. Its 4 longest legs jut out at 45 degrees from its body. In the
fancifully named magnetic water strider problem, we require the body to be aligned north-
south. Furthermore its legs support it, not by resting on the water, but by extending to
the boundary of the pond. Naturally, the legs of the striders are not allowed to intersect.
A legal conﬁguration of magnetic water striders in an orthogonal pond is shown Figure
21b.
There are two problems and a game here. The ﬁrst is a packing problem: What is the
largest number of magnetic waters striders that a pond can support? On the other hand,
one can ask what is the minimum number that can be placed so that no more can be added.
Placing and packing striders can be tricky, which gives rise to an adversarial game where
players take turns placing striders in an orthogonal region. Brian Wyvill has kindly imple-
mented a version of this game, available at http://www.theory.cs.uvic.ca/~cos/tatami/.
Interpreted as a matching problem on a subgraph of a grid graph G, a tatami tiling
is a matching M with the property that G −M contains no 4-cycles. Note that there is
always such a matching (e.g., take the “running bond” layout on the inﬁnite grid graph
and then restrict it to G). However, if we insist on a perfect matching, then the problem
is equivalent to our “perfect” driveway paving problem from the introduction.
the electronic journal of combinatorics 16 (2009), #R00
21


## Page 22


More generally, a matching whose removal destroys k-cycles is called Ck-transverse.
Ross Churchley proved that ﬁnding a Ck-transverse matching in an arbitrary graph is
NP-hard when k ≥4 (private communication [4]).
4.3
Combinatorial games
Consider the following game.
Given an orthogonal region, players take turns placing
dimers (or dimers and monomers); each placement must satisfy the tatami constraint
and the last player who can move wins. This game, called Oku!, is reminiscent of the
game called Nimm, in which players also win by making the last move, however a winning
strategy for our game is unknown and there are grid sizes in which the second player can
force a win. The name is a phonetic spelling of the Japanese word for “put”.
Another game applies tomography to rectangular tilings.
Tiling tomography is a rich and open area of complexity theory to which a good
introduction can be found in [3]. The relevant question is as follows: Given r + c triples
of numbers (h, v, m), one for each row and one for each column, is there a tatami tiling
which has h horizontal dimers, v vertical dimers, and m monomers in the respective row
or column?
Without the tatami condition this decision problem is NP-hard (Theorem 4, [5]).
Hard or not, the tatami condition gives considerable information in practice, however,
making the reconstruction of a tatami tiling an entertaining challenge.
Erickson, A.,
has created an online computer game out of this called Tomoku.
It is playable at
http://tomokupuzzle.com, complete with music, countdown timers and high scores.
Both of these games are at http://www.theory.cs.uvic.ca/~cos/tatami/, and it
should be noted that they can also be played with a pencil and paper.
5
Acknowledgements
Thanks to Donald Knuth for his comments on an earlier draft of this paper and to Martin
Matamala for pointing out the tomography problem.
References
[1] Alhazov, A., Morita, K., Iwamoto, C.: A Note on Tatami Tilings. Mathematical Foun-
dation of Algorithms and Computer Science (T. Tokuyama, Ed.), RIMS Kˆokyˆuroku
series, No. 1691, Research Institute for Mathematical Sciences, Kyoto, Japan, (2010),
1–7. http://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/kokyuroku.html
[2] Anzalone, N., Baldwin, J., Bronshtein, I., Petersen, T.K.: A reciprocity theorem for
monomer-dimer coverings. In Morvan, M., R´emila, ´E., eds.: Discrete Models for Com-
plex Systems, DMCS’03. Volume AB of DMTCS Proceedings., Discrete Mathematics
and Theoretical Computer Science (2003) 179–194
the electronic journal of combinatorics 16 (2009), #R00
22


## Page 23


Figure 22: The Tomoku web game.
The player is shown which tiles are completely
contained in each row and column, and the object is to reconstruct the tiling. Note that
each monomer appears twice in the projections.
[3] Chrobak, M., Couperus, P., D¨urr, C., Woeginger, G.: On tiling under tomographic
constraints Theoretical Computer Science Vol: 290 Issue: 3 ISSN: 0304-3975 Date:
01/2003 Pages: 2125 - 2136
[4] Churchley, R., Huang, J.: Private communication, November 2010
[5] D¨urr, C., Gui˜nez, F., Matamala, M.: Reconstructing 3-colored grids from horizontal
and vertical projections is NP-hard.
Algorithms - ESA 2009 LNCS 5757 (2009)
776–787
[6] Kenyon, R., Okounkov, A.: “What is . . . a dimer?”. Notices of the American Mathe-
matical Society 52 (2005) 342–343
[7] Knuth, D. E.: The Art of Computer Programming. Volume 4, fascicle 1B. Addison-
Wesley (2009)
[8] Pachter, L.:
Combinatorial approaches and conjectures for 2-divisibility problems
concerning domino tilings of polyominoes.
Electronic Journal of Combinatorics 4
(1997) 2–9
[9] Ruskey, F., Woodcock, J.: Counting ﬁxed-height tatami tilings. Electronic Journal of
Combinatorics 16 (2009) 20
[10] Stanley, R. P.:
On dimer coverings of rectangles of ﬁxed width. Discrete Applied
Mathematics 12(1) (1985) 81 – 87
the electronic journal of combinatorics 16 (2009), #R00
23

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
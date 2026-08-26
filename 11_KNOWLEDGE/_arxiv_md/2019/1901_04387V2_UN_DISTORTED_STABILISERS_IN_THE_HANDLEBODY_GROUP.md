---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1901.04387v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1901.04387v2__Un_distorted_stabilisers_in_the_handlebody_group

> Source: 1901.04387v2__Un_distorted_stabilisers_in_the_handlebody_group.pdf

> Pages: 34

---


## Page 1


(UN)DISTORTED STABILISERS IN THE HANDLEBODY
GROUP
SEBASTIAN HENSEL
Abstract. We study geometric properties of stabilisers in the handle-
body group. We ﬁnd that stabilisers of meridians are undistorted, while
stabilisers of primitive curves or annuli are exponentially distorted for
large enough genus.
1. Introduction
The handlebody group Mcg(V ) is the mapping class group of a 3–dimen-
sional handlebody V . In this article, we study the subgroup geometry of
stabilisers in Mcg(V ) of meridians and primitive curves. A curve δ on the
boundary of a handlebody is called a meridian, if it is the boundary of an
embedded disc. A curve β is called primitive, if there is a meridian δ which
intersects β in a single point.
Recall that a ﬁnitely generated subgroup H < G of a ﬁnitely generated
group G is undistorted if the inclusion homomorphism is a quasi-isometric
embedding. In contrast, we say that it is exponentially distorted, if the word
norm in H can be bounded by an exponential function of word norm in G,
and there is no such bound of sub-exponential growth type. We refer the
reader to e.g. [Far] for details on distortion functions of subgroups.
Our main results are:
Theorem 1.1. Suppose that V is a handlebody or compression body, and
that δ is a (multi)meridian in V . Then the stabiliser of δ is undistorted in
Mcg(V ).
Theorem 1.2. Let V be a handlebody of genus g.
i) Suppose that α is a primitive curve and g ≥3. Then the stabiliser of α
is exponentially distorted in Mcg(V ).
ii) Suppose A ⊂V is a properly embedded annulus so that ∂A consists of
primitive curves. Assume that g ≥3 (if A is non-separating) or g ≥4
(if A is separating). Then the stabiliser of A is exponentially distorted
in Mcg(V ).
To put these theorems into context, observe that the handlebody group is
directly related to mapping class groups of surfaces (via restriction of home-
omorphisms to the boundary) and to the outer automorphism group of free
Date: March 1, 2021.
1
arXiv:1901.04387v2  [math.GT]  26 Feb 2021


## Page 2


2
SEBASTIAN HENSEL
groups (via the action on the fundamental group). However, neither of these
connections is immediately useful to study the geometry of Mcg(V ): The
inclusion Mcg(V ) →Mcg(∂V ) may distort distances exponentially [HH1],
and the kernel of the map Mcg(V ) →Out(π1(V )) has an inﬁnitely gener-
ated kernel [Luf, McC1]. In other words, there is no a-priori reason to expect
that Mcg(V ) shares geometric features with surface mapping class groups
or outer automorphism groups of free groups.
It seems that its geometry, nevertheless, resembles that of outer automor-
phism groups of free groups. A ﬁrst instance of this was the computation of
its Dehn function in [HH2]: these are exponential for handlebody groups of
genus at least three, just like those of Out(Fn) for n ≥3.
The two main results of this article provide further evidence for this phi-
losophy. In the surface mapping class group Mcg(∂V ), stabilisers of curves
are undistorted for all curves (this follows e.g. immediately from the distance
formula of Masur-Minsky [MM]). On the other hand, Handel and Mosher
[HM] found that in the outer automorphism groups of free groups there is a
dichotomy – stabilisers of free splittings are undistorted, whereas stabilisers
of primitive conjugacy classes (and most other free factors) are exponentially
distorted. By the van-Kampen theorem, the stabiliser of a meridian maps
exactly to the stabiliser of a free splitting, while the stabiliser of a primitive
curve maps to the stabiliser of a primitive conjugacy class.
A properly embedded annulus in the handlebody induces, by Seifert-van
Kampen, a splitting of π1(V ), amalgamated about a cyclic subgroup gener-
ated by a primitive element of π1(V ). We call such a splitting a primitive
cyclic splitting. Hence, the stabiliser of an annulus in the handlebody group
maps to the stabiliser of a primitive cyclic splitting in Out(Fn). Here, an
exponential lower bound for distortion follows from the results in [HM] (al-
though it is not explicitly discussed in that reference). We extend this by a
similar upper bound, which shows that it has the same behaviour as in the
handlebody group case.
Proposition 1.3. For n ≥4, the stabiliser of a primitive cyclic splitting in
Out(Fn) is exponentially distorted in Out(Fn).
To prove Theorem 1.1, we deﬁne a projection of meridian systems of V to
meridian systems in sub-handlebodies. This is carried out in Section 3. We
recall the well-known fact that usual Masur-Minsky subsurface projections
of meridians to sub-handlebodies are usually not meridians again (compare
e.g. [Hen, Section 10]), and so our projection procedure is more involved
and depends on choices. The lower bounds in Theorem 1.2 are proved by
a reduction to the theorem by Handel-Mosher on stabilisers in the outer
automorphism group of free groups. Here, the key diﬃculty is to realise
certain free group automorphisms considered by Handel-Mosher as home-
omorphisms of handlebodies with comparable word norm.
This uses an
idea which was already employed in [HH2]. The upper distortion bounds in
Theorem 1.2 follow from a surgery procedure.


## Page 3


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
3
Acknowledgements The author would like to thank Ursula Hamenst¨adt,
Andy Putman, Saul Schleimer, and Ric Wade for interesting discussions
about stabilisers in diﬀerent contexts. The author would also like the anony-
mous referees for numerous helpful commets. Finally, he would like to thank
the mathematical institute of the University of Oxford, where part of this
work was carried out.
2. Preliminaries
In this section we collect some basic tools on surfaces, handlebodies, and
compression bodies that we will use throughout.
2.1. Surface Basics. Suppose that S is a surface. All curves are assumed
to be simple and essential. We usually identify a curve with the isotopy
class it deﬁnes. If α, β are two curves, we denote by i(α, β) the geometric
intersection number, i.e. the smallest number of intersections between α, β
up to isotopy.
A subsurface will always mean a (possibly disconnected) two-dimensional
submanifold with boundary, no component of which is an annulus. Unless
speciﬁed explicitly, we will assume that all curves and subsurfaces are in
minimal position with respect to each other; compare [FM]. If α is a curve
and Y is a subsurface, then we call the components of Y ∩α the α-arcs with
respect to Y .
If δ is a multicurve, then we denote (by slight abuse of notation) by S −δ
the complementary subsurface of δ, i.e. the metric closure of S \ δ with
respect to the path metric. Explicitly, this means that S −δ has boundary
components corresponding to the sides of the curves in δ. Equivalently, one
can think of S−δ as the complement of a small open, regular neighbourhood
of δ.
We will often call the components of the intersection α ∩(S −δ) which
are not closed curves the α-arcs with respect to δ.
If α is a curve which intersects δ transversely, then we denote by
πS−δ(α)
the subsurface projection, which we deﬁne to be a maximal subset of non-
homotopic arcs in the set (S −δ) ∩α of α-arcs of δ. We deﬁne πS−δ(α) = α
if δ, α are disjoint.
If A is a multicurve, the projection πS−δ(A) is deﬁned to be the union of
the projections of components:
πS−δ(A) =
[
α∈A
πS−δ(α).
We remark that the subsurface projection of a multicurve in general is a
union of (isotopy classes) of curves and proper arcs.


## Page 4


4
SEBASTIAN HENSEL
2.2. Handlebodies and Surgeries. A handlebody is the 3-manifold ob-
tained by attaching three-dimensional one-handles to a 3–ball. A compres-
sion body is the 3–manifold obtained from a handlebody by taking boundary
connect sums with a ﬁnite number of trivial interval bundles over surfaces.
A compression body has an outer boundary component, which is the unique
boundary component of highest genus.
Suppose that V is a handlebody or compression body.
A meridian is
a simple closed curve on ∂V (resp. the outer boundary component of the
compression body) which bounds a disc in V . A ﬁlling meridian system
is a collection ∆= {δ1, . . . , δk} of disjoint, non-isotopic meridians, bound-
ing disjoint discs Di with the property that each component of V −∪Di
is either a 3–ball or a trivial interval bundle. Note that as handlebodies
and compression bodies are aspherical, the disjointness of the discs Di can
always be arranged, if we suppose that the δi are disjoint. We remark that
the number of components of a ﬁlling meridian system is non-unique, but
bounded above by 3g −3.
For handlebodies a ﬁlling meridian system contains at least g curves. For
a handlebody V , we also use the notion of cut system, by which we mean a
ﬁlling meridian system with the smallest number of elements. Equivalently,
it is a ﬁlling meridian system with a single complementary component (which
is then necessarily a 2g–holed sphere).
Next, we describe surgery. Namely, we recall the following standard result
(compare e.g. the proof of Theorem 5.3 in [McC2]).
Lemma 2.1. Suppose that ∆is a ﬁlling meridian system, and that α is any
meridian which is not disjoint from ∆. Then there is a subarc a ⊂α, called
a wave (of α with respect to δ), with the following properties:
i) a ∩∆consists of two points on the same curve δ ∈∆. Call the compo-
nents of δ −a = δ−∪δ+. Then the set
{a ∪δ−, a ∪δ+} ∪∆\ {δ}
is a ﬁlling meridian system.
ii) If V is a handlebody, then there is δ∗= δ± so that
{a ∪δ∗} ∪∆\ {δ}
is a ﬁlling meridian system. If ∆is a cut system, then exactly one choice
of δ± yields a ﬁlling meridian system, and it is again a cut system.
In the case of handlebodies, any arc a which intersects ∆only in its endpoints
and returns to the same side of a curve in ∆is a wave. Furthermore, in the
case of handelbodies there are always two distinct (but possibly homotopic)
waves.
We call the result of i) full surgery, and the result of ii) surgery of ∆in
the direction of α. If ∆and the surgery of ∆are cut systems as in ii), we
also call the process cut system surgery.


## Page 5


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
5
If α, ∆are disjoint, we also say that ∆is obtained from ∆by surgery
in the direction of α (as this makes certain arguments later easier to state
without case distinctions).
If V is a handlebody, we let Mcg(V ) be its mapping class group, i.e. the
group of orientation preserving self-homeomorphisms of V up to isotopy.
Since such homeomorphisms and isotopies preserve the boundary, there is a
restriction map
Mcg(V ) →Mcg(∂V ),
where ∂V is the boundary surface. We deﬁne the handlebody group H(V )
as the image of this map. In other words, the handlebody group consists of
those mapping classes of the surface ∂V , which can be extended to homeo-
morphisms of V . It is well-known that the restriction map is injective, and
so H(V ) is in fact isomorphic to the mapping class group Mcg(V ). How-
ever, for us it will be more convenient to think of elements in the handlebody
group as surface mapping classes.
If S ⊂∂V is a subsurface, then we denote by H(S) the subgroup of H(V )
formed by all elements supported in S.
The following well-known lemma is central for us:
Lemma 2.2 (e.g. [Hen, Corollary 5.11]). Suppose that ϕ : ∂V →∂V is a
mapping class. If both C and f(C) are ﬁlling meridian systems, then ϕ is
contained in the handlebody group.
We deﬁne the compression body group similarly, replacing ∂V with the
outer boundary component of the compression body V .
3. Meridian Stabilisers
In this section we analyse stabilisers of meridians in handlebody and com-
pression body groups. For simplicity of exposition we focus on the proof in
the case of handlebody groups, and only indicate the necessary modiﬁcations
in the case of compression body groups at the end of the section.
From an algebraic perspective, the study of meridian stabilisers reduces
to the study of point-pushing and handlebody groups of smaller genus, just
as in the case of surface mapping class groups; compare [Hen, Section 3] for
details. In particular, this implies that multimeridian stabilisers are ﬁnitely
generated.
The main result of this section is the following theorem:
Theorem 3.1. Let V be a handlebody, and δ be a multimeridian. Then the
stabiliser of δ in the handlebody group is undistorted.
3.1. Distortion and Models. In this section, we describe the main mech-
anism by which we will exhibit (un-)distortion. This is the following relative
version of the ˇSvarc-Milnor lemma. While this is well-known to experts, we
provide a full formulation and proof for the beneﬁt of the reader. If X is a


## Page 6


6
SEBASTIAN HENSEL
graph and Y ⊂X is a connected subgraph, we deﬁne the distortion function
as
DY (n) = max{dY (v, w)|v, w ∈Y 0, dX(v, w) ≤n.}
Here dX, dY are the path-metrics on X, Y obtained by declaring each edge to
have length 1. It is well-known (and not hard to see) that the growth type
of DY is invariant under quasi-isometries of the pair (X, Y ). For ﬁnitely
subgroups H < G of ﬁnitely generated groups, we deﬁne the distortion
function of the subgroup H as the distortion function for (any) inclusion of
Cayley graphs.
Lemma 3.2. Suppose that G is a group, and H is a subgroup of G. Assume
that G is a connected, locally ﬁnite graph, on which G acts by isometries and
with ﬁnite quotient and ﬁnite stabilisers.
If GH ⊂G is a connected subgraph, which is preserved by H, and so that
GH/H is ﬁnite, then the distortion function of H in G has the same growth
type as the distortion function of GH in G.
Proof. Pick a basepoint o ∈GH. By the usual ˇSvarc-Milnor lemma, the
orbit maps
H →GH,
h 7→h · o
and
G →G,
g 7→g · o
are quasi-isometric embeddings. This shows that the pair (Cay(G), Cay(H))
is quasi-isometric to the pair (G, GH), which shows the lemma.
□
We will use two geometric models for the handlebody group in the proof
of Theorem 3.1 (and subsequent arguments). For the deﬁnition of the ﬁrst,
we need the notion of a discbusting curve: we say that l is discbusting, if l
is not disjoint (up to isotopy) to any meridian.
Deﬁnition 3.3. For numbers k0, k1 > 0, deﬁne a graph G(k0, k1) with
Vertices: corresponding to pairs (C, l) of a ﬁlling meridian system C
and a simple discbusting loop l (up to isotopy), so that i(C, l) ≤k0.
C-Edges: between vertices (C, l) and (C′, l) if C′ is disjoint from C.
l-Edges: between vertices (C, l) and (C, l′) if i(l, l′) ≤k1.
The following is a standard trick to obtain a geometric model for a group;
compare e.g. [HH1, Lemma 7.3].
Lemma 3.4. There are choices of k0, k1 so that G(k0, k1) is nonempty,
connected, locally ﬁnite, and the handlebody group acts on G(k0, k1) properly
discontinuously and cocompactly.
Proof. First, observe that there are ﬁnitely many ﬁlling meridian systems
C1, . . . Ck so that every ﬁlling meridian system is in the handlebody group
orbit of one of the Ci.
This follows from Lemma 2.2 and the fact that
there are only ﬁnitely many types of multicurves up to the action of the
mapping class group. As being discbusting is invariant under the action of


## Page 7


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
7
the handlebody group, this shows that there is a constant k0 so that for any
ﬁlling meridian system C there is a discbusting loop l so that i(C, l) ≤k0.
Next, we claim that the stabiliser of C in the handlebody group acts with
ﬁnitly many orbits on the set of (isotopy classes) of pairs (C, l) as in the
deﬁnition of the vertices. By the intersection number bound, l ∩(S −C) is
a collection of at most k0 embedded arcs. Up to the action of the mapping
class group of S −C, there are only ﬁnitely many such arc systems. By
Lemma 2.2, the same is therefore true for the action of the stabiliser of C in
the handlebody group. Up to Dehn twists about the curves in C, there are
only ﬁnitely many possible curves l which can be obtained by connecting
the arcs l ∩(S −C). Since the Dehn twists about C are contained in the
handlebody group as well, this implies the claim.
As a consequence, we ﬁrst claim that we can choose the constant k1 large
enough so that any two vertices of the form (C, l), (C, l′) are connected by
a path of l-edges. To see this, ﬁx a set l1, . . . , lr of orbit representatives of
such discbusting curves (for the action of the stabiliser of C), and a ﬁnite
generating set ϕ1, . . . , ϕk of the stabiliser of C in the handlebody group.
Now, if k1 > maxa,b,c i(la, ϕblc) the desired property holds.
Now, suppose that (C, l) and (C′, l′) are arbitrary. We claim that there is a
path between them. To show this, ﬁrst ﬁnd a sequence C = C0, C1, . . . , CN =
C′ of ﬁlling meridian systems so that Ci, Ci+1 are disjoint. This is possible
e.g. by surgery. Next, ﬁnd discbusting curves li so that (Ci, li), (Ci+1, li)
represent vertices of the graph. This is possible by the choice of k0 above.
In particular, (Ci, li), (Ci+1, li) are therefore joined by a C-edge. From this,
we can assemble the desired path as
(C0, l) →(C0, l0) →(C1, l0) →(C1, l1) →(C2, l1) →· · · →(CN, lN−1) →(CN, l′)
where every →denotes a l-edge or C-edge. This shows that the graph is
connected.
Next, observe that the graph is locally ﬁnite. This follows since for any
vertex (C, l) the curve system C ∪{l} is ﬁlling, and there are therefore
only ﬁnitely many isotopy classes of curves whose intersection number with
C ∪{l} is bounded by a given constant. By the same reason, the stabiliser
of any vertex is ﬁnite (indeed, the stabiliser of a ﬁlling curve system in the
mapping class group is ﬁnite). Thus, the action of the handlebody group is
properly discontinous.
Cocompactness of the action then follows immediately, since (by construc-
tion) there are only ﬁnitely many orbits of vertices.
□
In the sequel, we make choice of k0, k1 as in the lemma, and simply denote
the resulting graph by G. Observer that by the ˇSvarc-Milnor lemma, G will
then be equivariantly quasi-isometric to the handlebody group.
Deﬁnition 3.5. For a multimeridian δ, we let G(δ) be the full subgraph
spanned by all those vertices (C, l) whose meridian system contains δ.


## Page 8


8
SEBASTIAN HENSEL
Corollary 3.6. The subgraphs G(δ) are connected for all δ, and the stabiliser
of δ in the handlebody group acts on G(δ) cocompactly.
Proof. This is a corollary of the proof of Lemma 3.4. First, for connectivity,
we just have to observe that the sequence C0, . . . , CN can be chosen to
contain δ. This is automatic for surgery sequences (if both C, C′ contain δ,
then every step of the surgery sequence will have the same property).
For cocompactness, one observes that the stabiliser of δ acts with ﬁnitely
many orbits on the set of ﬁlling meridian systems which contain δ. One way
to see this is to note that the stabiliser of a multicurve δ in the mapping class
group acts with ﬁnitely many orbits on the set of multicurves containing δ,
and using again Lemma 2.2.
□
Now, Lemma 3.2 implies that in order to prove Theorem 3.1, it suﬃces
to show that the subgraph G(δ) is undistorted in G.
In the proof it will be useful to use a second model1, which is similar to
the graph of rigid racks employed in [HH1].
Deﬁnition 3.7. For numbers k0, k1, the graph R(k0, k1) has
Vertices: corresponding to (isotopy classes of) connected graphs Γ ⊂
∂V with at most k0 vertices, which contain a ﬁlling meridian sys-
tem C(Γ) as an embedded subgraph, and have simply connected
complementary regions.
Edges: between graphs Γ, Γ′ which intersect in at most k1 points (up
to isotopy).
Arguing as in the proof of Lemma 3.4, we can choose the constants k0, k1
so that the resulting graph is connected, locally ﬁnite, and the action of the
handlebody group is properly discontinuous and cocompact (here, the role
of l is played by the complement of the embeddded subgraph deﬁned by the
ﬁlling meridian system). Similar to the deﬁnition of G(δ), we deﬁne R(δ) to
be the full subgraph spanned by vertices corresponding to graphs Γ, to that
the ﬁlling meridian system C(Γ) also contains δ. Arguing as above, we may
assume that it is also connected, and the stabiliser of δ acts cocompactly.
By possibly increasing the constants deﬁning R, there is a natural map
U : G →R
which sends a vertex (C, l) to the union C ∪l (assuming that l is in minimal
position with respect to C).
Observe that the map U is equivariant for
the action of the handlebody group on G, R.
As a consequence, U is a
quasi-isometry, as the handlebody group acts cocompactly on both of these
graphs. The restriction
U : G(δ) →R(δ)
is also a quasi-isometry, as it is equivariant for the stabiliser of δ, which acts
cocompactly on both sides.
1The reason for using both models is that curves and curve pairs have easier to phrase
minimal position properties as opposed to embedded graphs.


## Page 9


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
9
The strategy to prove Theorem 3.1 is to start with any path γ : [0, n] →G,
and to “project” it to a path in R(δ) joining U(γ(0)) to U(γ(n)), taking
care that the length of the projected path is coarsely bounded by n. Since
U is a quasi-isometry, this will imply that G(δ) is undistorted in G, showing
Theorem 3.1.
3.2. Patterns and Surgery. In this section we will describe a systematic
way to simplify a cut system until it is disjoint from a given (multi)meridian
δ, which is assumed to be ﬁxed throughout the section. This will be the
core ingredient used to project paths in G to R(δ). Recall that a cut system
is a collection of g meridians α1, . . . , αg the complement of which is a 2g–
holed sphere. We could also perform these arguments with general ﬁlling
meridian systems, but the discussion is slightly more convenient in the cut
system case.
We use following terminology and setup throughout this section. Cut the
boundary surface ∂V of the handlebody at the meridian δ. The resulting
(possibly disconnected) surface with boundary has boundary components
δ+, δ−corresponding to the two sides of δ.
Suppose now that C is a cut system intersecting δ transversely and min-
imally. Then we call, by a slight abuse of notation, the set
(δ+ ∩C) ∪(δ−∩C)
the intersection points of C with δ. Recall that we call the connected compo-
nents of C ∩(S −δ) the C–arcs. Note that endpoints of C-arcs are precisely
the intersection points of C with δ.
An interval will mean a subarc I of δ+ ∪δ−whose endpoints lie in C.
Observe that for the two endpoints x, y there are uniquely determined
C–arcs γx, γy which intersect I in x, y (note that these arcs may coincide).
We call them C–arcs adjacent to I.
Deﬁnition 3.8. A partial pattern for C is a collection I of intervals satis-
fying the following properties:
N): Any two I, J ∈I are disjoint or nested (i.e. one is contained in
the interior of the other).
P): If γ is a C–arc adjacent to some I ∈I, then both endpoints of γ
are endpoints of intervals in I.
Deﬁnition 3.9. A chain of a partial pattern I is a sequence
c = (I1, γ1, I2, γ2, . . . , γk, I1)
of intervals in I and C–arcs so that
i) the intervals Ij can be oriented so that for each i, the right endpoint of
Ii is one endpoint of γi, and the other endpoint of γi is the left endpoint
of Ii+1, and
ii) the sequence does not contain a subsequence satisfying i).


## Page 10


10
SEBASTIAN HENSEL
An easy induction, using property P), shows that every interval in a
partial pattern is part of a chain which is unique up to cyclic reordering.
By concatenating the Ii and γi in a chain c, we obtain a closed loop on
the surface, which by abuse of notation we also call a chain of the partial
pattern.
This concatenation is not embedded, but we can homotope it into push-
oﬀposition, by pushing the intervals Ii slightly oﬀof δ+ ∪δ−into S −δ.
Property N) guarantees that we can choose push-oﬀpositions for all chains
so that the chains themselves are simple closed curves, and diﬀerent chains
do not intersect (push oﬀmore deeply nested intervals further oﬀof δ+∪δ−).
From now on we assume that, unless speciﬁed explicitly, all chains are in
push-oﬀposition.
A chain may be an inessential curve. To avoid this, we put
C(I) = {α|α is an essential curve deﬁned by a chain of I}.
Each c ∈C(I) is a concatenation of subarcs of C and (pushed oﬀcopies of)
intervals in I. We call the intervals I ∈I which appear in this way active
(intervals may be inactive if they lie on inessential chains deﬁned by the
pattern).
Deﬁnition 3.10. A pattern is a partial pattern I which additionally satis-
ﬁes:
F): The set C(I) ∪{δ} forms a ﬁlling meridian system for V .
Deﬁnition 3.11 (Compatible Patterns). If C′ is disjoint from C, then a
pattern I for C and a pattern I′ for C′ are compatible, if any intervals I ∈I
and I′ ∈I′ are either disjoint or nested.
Arguing as before with push-oﬀrepresentatives, we immediately obtain
the following:
Lemma 3.12. If C, C′ are disjoint cut systems, and I, I′ are compatible
patterns, then C(I) and C′(I′) are disjoint.
Our ﬁrst goal is to show that patterns always exist, and that for disjoint
cut systems there are compatible patterns. This will be done by a standard
surgery procedure, and the following lemma is analogous to various results
in the literature, compare e.g. [HH1, Lemma 5.4], [Hem, Lemma 1.3] or
[Mas, Lemma 1.1].
Lemma 3.13 ((Compatible) patterns exist).
i) For any ﬁlling meridian
system C in minimal position with respect to a multimeridian δ, there
is a pattern I for C, which we call a surgery pattern.
ii) If I is a surgery pattern (i.e. a pattern obtained by applying part i) of
this lemma) for C, and C′ is disjoint from C, then there is a surgery
pattern for C′ which is compatible with I.
Proof.
i) We ﬁnd the pattern inductively. Note that if an interval I is
innermost, i.e. it does not contain any other intersection points of C


## Page 11


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
11
Figure 1. Push-oﬀrepresentatives of a surgery move.
with δ, then it deﬁnes an δ–arc with respect to C. Thus it makes sense
to talk about intervals being a wave of δ with respect to C. Choose an
interval I1 which is a wave w of δ with respect to C and set C = C1. Let
C2 be the result of the cut system surgery of C1 at w (i.e. the surgery
of C1 at w so that the result is a cut system). In fact, C2 has a push-oﬀ
representative as well, so that each curve in C2 is a concatenation of
parts of C1 and the interval I1 (compare Figure 1). It might be the case
that this push-oﬀ-representative is not in minimal position with respect
to δ (if there are other waves isotopic to w), but there is a choice of I1
so that this problem does not occur (by choosing I1 outermost in the
sense that in the direction of the push-oﬀthere is no parallel copy of
w).
Now inductively repeat this procedure, deﬁning a surgery sequence Ci
and a sequence of intervals Ii, so that each curve in each Ci is obtained
as a concatenation of arcs in C and intervals Ik, k ≤i. The ﬁnal term
Cn of this surgery sequence is a cut system disjoint from δ. Let I be
the set of those intervals Ik which are still part of Cn. By construction,
we then have that C(I) = Cn. This implies that I is indeed a pattern.
Namely, following along the procedure we know that Cn is the push-oﬀ
representative of C(I). The fact that each component of C(I) closes
up to be a multicurve implies that I has property P), and the fact
that C(I) is simple implies it has property N), as, if this were not the
case, push-oﬀ-representatives would have self-intersections. Since Cn is
a ﬁlling meridian system, I is indeed a pattern.
ii) Suppose I is a surgery pattern. Recall that this means that I is formed
by the construction of part i), and let Ci, Ii denote the sequences con-
structed there. To deﬁne the desired pattern I′, we will follow a similar
construction as in part i), successively building intervals I′
i and merid-
ian systems C′
i, using the Ci, Ii. In each step of the procedure, we will
either build a new interval I′
j and a new meridian system C′
j, or we will


## Page 12


12
SEBASTIAN HENSEL
Figure 2. Nested intervals in a pattern deﬁne wings.
If
I ⊂J are directly nested, the wings can be made disjoint
from the system C(I), even if there are other intervals ˆI ⊂J.
show that the current interval is compatible with the next corresponding
interval in I.
We begin by putting C′
1 = C′. By assumption, C1 is then disjoint
from C′
1. Consider the interval I1: if I1 is disjoint from C′
1, then so is
C2 = C1(I1). If I1 intersects C′
1, then there is a subinterval I′
1 ⊂I1 with
endpoints on C′
1 which is also a wave of δ with respect to C′
1. In that
case, note that I′
1 is disjoint from C1, and therefore the same is true for
C′
2 := C′
1(I′
1).
Now suppose that I′
j, j < s, C′
s, j ≤s are deﬁned for some s, and
that there is a also a number r with the property that so that Ii, i ≤
r, I′
j, j < s are nested or disjoint, and so that Cr, C′
s are disjoint. In
the ﬁrst case of the previous case distinction, we have s = 0, r = 1 or
s = 1, r = 0 respectively.
Now consider Ir, and again distinguish two cases. If Ir is disjoint
from C′
s, then Cr+1 is also disjoint from C′
s, and Ir is nested or disjoint
from the I′
j, j ≤s. Hence, (r+1, s) again satisﬁes the assumption above.
Alternatively, if Ir is not disjoint from C′
s, then there is a sub-interval
I′
r ⊂Ir which deﬁnes a wave for C′
s. In that case, let C′
s+1 be the surgery
of C′
s at that sub-interval, and note that it is disjoint from Cr. Hence,
(r, s + 1) satisﬁes the assumption above.
After ﬁnitely many such steps, all surgery steps for the sequence Ci
have been taken, and we have constructed a partial pattern I′ compat-
ible with I. Now, we can complete the construction as in i) to build
the pattern I′ with the desired properties.
□
The surgery patterns produced by Lemma 3.13 are not yet suﬃcient for
our purposes. We will need a second move to improve patterns; to describe
it we use the following terminology:
Suppose that I is a pattern for C, and suppose that I ⊊J are two
active intervals in I. The two segments of J \ int(I), call them w,w+ can
be interpreted (up to a small homotopy) as arcs with endpoints on C(I),
and we call these arcs wings; compare Figure 2. Observe that the two wings
deﬁned by a nested pair of intervals are homotopic as arcs with endpoints
sliding on C(I). We say that I, J are directly nested if there is no active


## Page 13


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
13
I′ with I ⊊I′ ⊊J. Suppose now that I ⊊J are directly nested. In that
case, wings deﬁne arcs that intersect C(I) only in their endpoints (compare
again Figure 2 for this situation), since intersections of a wing with intervals
ˆI satisfying ˆI ⊂J −I can be removed up to homotopy.
Suppose now that D is any ﬁlling meridian system, and that w is an
embedded arc which has both endpoints on the same curve γ ∈D. Then w
deﬁnes an element in π1(V ) by connecting the endpoints of w in any way
along γ (observe that since γ is a meridian, the resulting element of π1(V )
does not depend on the choice of interval in γ, but only on w). We say
that w is a V -trivial arc if it has both endpoints on the same curve γ and
additionally it deﬁnes the trivial element in π1(V ).
Lemma 3.14. If D is a ﬁlling meridian system and w is an embedded V –
trivial arc with endpoints on a curve in D (which may intersect D in more
points than just its endpoints), then w contains a subarc w0 ⊂w which
deﬁnes a wave with respect to D.
Proof. We use a particular covering space of ∂V . Namely, consider the uni-
versal covering eV →V , and let Y →∂V be the restriction to the boundary.
By the lifting theorem, a closed (possibly nonembedded) loop on ∂V lifts to
a closed (possibly nonembedded) loop on Y exactly if it deﬁnes the trivial
element in π1(V ). In other words, the cover Y is the cover corresponding to
the subgroup π1(Y ) = ker(π1(∂V ) →π1(V )).
Every lift of a curve in D to Y is seperating (this can e.g. be seen by
observing that V is homotopy equivalent to a tree in a way so that each lift
of a curve in D maps to a point).
Now, choose a lift ew of w to Y . Since w is assumed to be V –trivial, this
lift joins some lift eδ of a curve δ in D to itself. Namely, choose a subarc
d ⊂δ ∈D so that the concatenation d ∗w is a (not necessarily embedded)
loop in V which is trivial in π1(V ). Hence, d ∗w lifts to a closed loop in Y
(which also need not be embedded), which has the form ed ∗ew, where ed is
contained in a lift eδ of the curve δ. In particular, ew has both endpoints on
that lift.
Since all lifts of curves in D are separating in Y , and we assume that w
(hence ew) is embedded, there is a subarc ew0 ⊂ew whose interior is disjoint
from all lifts of curves in D, and has both endpoints on the same lift.
The image w0 of ew0 under the covering map is a subarc of w which has
both endpoints on the same curve of D, and approaches it from the same
side at both endpoints. By the last part of Lemma 2.1, w0 is then the desired
wave.
□
Lemma 3.15. Let C be a cut system and I a pattern. Suppose that I ⊊J
are two active intervals of I, and that w is a wing of I ⊊J.
i) If w is V -trivial, then there are directly nested active intervals I′ ⊊J′
which have a wing w′ ⊂w that deﬁnes a wave.


## Page 14


14
SEBASTIAN HENSEL
ii) Suppose now that I ⊊J are directly nested, and that w deﬁnes a wave.
Let C′ be a ﬁlling meridian system which is disjoint from C and let I′
be a pattern for C′ which is compatible with I. Then either the wing w
can be made disjoint from C′(I′), or there is a pair I′ ⊊J′ of directly
nested intervals in I′ whose wing w′ is a wave and contained in w.
Proof.
i) Consider I = I1 ⊊I2 · · · ⊊Ik = J a maximal chain of nested
ﬁnal intervals in the pattern. Without loss of generality we may assume
that w connects the left endpoint of J to the left endpoint of I. We
can push w oﬀof the curve of C containing it a little bit to form an arc
w′, so that the intersections of w′ with C(I) exactly correspond to the
points p ∈w which are endpoints of intervals K ∈I.
If K is an interval both endpoints of which are contained in w, then
an isotopy of C(I) can remove both of these intersections (compare
Figure 2). After this modiﬁcation, the intersection points of w′ with
C(I) exactly correspond to the left endpoints of the Ij.
Since w′ is V -trivial loop, its intersection with the ﬁlling meridian
system C(I) ∪{δ} has a wave by Lemma 3.14. The endpoints of the
wave w0 ⊂w′ then correspond to the left endpoints of Ii, Ii+1 for some
i. This implies that Ii, Ii+1 are directly nested, and they have a wing
which is a wave as claimed.
ii) Arguing as in i), we see that an essential intersection of the wing w with
the system C′(I′) can only occur if there are intervals I ⊊I′ ⊊J with
I′ ∈I′. In fact, as above, the essential intersections of w then exactly
correspond to intervals I′
j ∈I′ with I ⊊I′
1 ⊊· · · ⊊I′
k ⊊J. Apply
Lemma 3.14 to w and the ﬁlling meridian system C(I) ∪C′(I′) ∪{δ}
as above. There is thus a wave w1 ⊂w of this arc. Its endpoints are
necessarily contained in C′(I′) since the interior of w is disjoint from
C(I) and δ, and so w1 deﬁnes the desired nested intervals as in i).
□
Finally, we choose once and for all a hyperbolic metric on the surface S.
This allows us to talk about the length of intervals. The length of a pattern
is the sum of the lengths of all intervals chosen by the pattern. We can now
describe the wave exchange move. Suppose that I is a pattern for some cut
system C, and suppose that I ⊊J are directly nested active intervals whose
wings w1, w2 are waves. The wave exchange I(w1, w2) is the set obtained
by replacing {I, J} by {w1, w2}; see Figure 3 for this construction.
Lemma 3.16. The wave exchange I(w1, w2) is a pattern of strictly smaller
length than I.
Proof. We begin by noting that I(w1, w2) satisﬁes property N) since the
intervals I ⊊J are supposed to be directly nested. Hence, any interval in
I \ {I, J} which intersects J −I is contained in J −I, and therefore nested
inside w1 or w2.
Property P) is obvious, since I and I(w1, w2) connect
the same intersection points of δ with C. To show property F), note that


## Page 15


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
15
Figure 3. Suppose I ⊂J are directly nested, with wings
deﬁning waves, depicted above. Below is the wave exchange.
C(I(w1, w2)) is the full surgery of C(I) at the wave w1 (or w2), and therefore
is still ﬁlling (compare Figure 3). The claim about length is due to the fact
that w1 ∪w2 ⊊J.
□
Deﬁnition 3.17. Call a pattern essential if no nested intervals have wings
which are V -trivial arcs.
Corollary 3.18. Any pattern I admits a ﬁnite sequence of waves exchanges
terminating in an essential pattern.
Proof. Since by the previous lemma each wave exchange strictly decreases
the length of the pattern, any sequence of wave exchanges starting in I
is ﬁnite, and terminates in a pattern I′ which does not admit any wave
exchanges. Then by Lemma 3.15, no nested pair of intervals of I′ has a wing
which deﬁnes a V -trivial arc, as otherwise there would be a pair deﬁning a
wave, and hence the pattern would admit another wave exchange. Hence,
I′ is essential as claimed.
□
Lemma 3.19. Suppose that I is a pattern for some cut system C, and
suppose that I ⊊J are directly nested active intervals whose wings w1, w2
are waves.
Suppose further that C′ is disjoint from C and that I′ is a
compatible pattern.
Then either I(w1, w2) is compatible with I′, or there is a wave exchange
I′(w′
1, w′
2) which is compatible with I.
Proof. If w1 (and thus w2) can be made disjoint from C′(I′), then the wave
exchange I(w1, w2) is compatible with I′. As in the proof of Lemma 3.15,
this happens exactly if there is no I′–interval nested between the I–intervals
deﬁning w1, w2. Otherwise, by Lemma 3.15, there are wave-wings w′
1, w′
2
contained in w1, w2, deﬁned by intervals I′, J′ ∈I′. Since we assumed that
I ⊂J are directly nested, no interval in I nests between I′ and J′. Hence,
by reversing the roles, I′(w′
1, w′
2) is compatible with I.
□


## Page 16


16
SEBASTIAN HENSEL
Lemma 3.20. Let C be a cut system, and I an essential pattern. Suppose
that I ⊊J are two active intervals, belonging to the same curve in C(I).
Let C′ be disjoint from C, and let I′ be a pattern for C′ which is compatible
with I. Then there is an interval K ∈I′ so that I ⊂K ⊂J.
Proof. By the deﬁnition of essential pattern, the wings of I ⊂J deﬁne
nontrivial elements of π1(V ). Hence, they cannot be disjoint from C′(I′)
(as, if they were, they would be disjoint from the ﬁlling meridian system
C′(I′) ∪{δ}, showing that they deﬁne trivial elements in π1(V )). This is
only possible if there is an interval K as desired (again, non-nested intervals
do not contribute intersections; compare Figure 2).
□
Corollary 3.21. There is a number D > 0 with the following property.
Suppose that C is a cut system, and I is an essential pattern for C. Let
I′ be a pattern for C′ which is compatible with I.
Suppose that I1 ⊊I2 ⊊· · · ⊊Ik is a chain of intervals in I with k ≥D.
Then there is an interval K ∈I′ so that I1 ⊂K ⊂Ik.
Proof. Since a cut system has at most g curves, if D is large enough, there
will be indices i, j so that Ii, Ij lie on the same curve of C(I).
Then
Lemma 3.20 applies and yields the desired interval.
□
3.3. Proof of undistortion. Before we can prove the main theorem, we
need the following two results that connect patterns to usual subsurface
projections.
Lemma 3.22. Suppose that C is a cut system and that C′ is a cut system
which is disjoint from C. Then for any K > 0 there is a constant L =
L(K) > 0 so that the following holds.
Let I be an essential pattern for C, and let I′ be a compatible, essential
pattern for C′. Suppose that a is a properly embedded arc in ∂V −(δ∪C(I)).
Assume that i(a, C′) ≤K. Then,
i(a, C′(I′)) < L
Proof. The ﬁrst step of the proof is to choose suitable representatives of the
isotopy classes of C(I), C′(I′) and a.
To this end, consider an embedded collar neighbourhood
N = (δ+ ∪δ−) × [0, 1)
of δ+ ∪δ−. We call the direction of the ﬁrst coordinate horizontal, and the
other one vertical. In particular, the copies of δ forming the boundary of
∂V −δ are horizontal.
Up to isotopy, we may assume that the intersections of C, C′ with the
neighbourhood consist only of vertical segments. Furthermore, we choose
pushoﬀpositions of C(I), C′(I′), which are disjoint from each other and
intersect N in a union of vertical segments (which are subsegments of the
intersections of C, C′ with N), and horizontal segments (corresponding to


## Page 17


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
17
Figure 4. Our setup in the proof of Lemma 3.22.
Here,
C′(I′) is shown as solid lines, but C′ continues as vertical
lines (drawn dashed) beyond the pieces used in C′(I′). The
rest of C′(I′) consists of horizontal segments corresponding
to the intervals in I′. For property (1): a subarc of a which
enters and leaves N is forced to intersect C′, or is not in
minimal position with respect to C′(I′).
Figure 5. Property (2) in the proof of Lemma 3.22.
As
before, C′(I′) is drawn in solid black. The arc a intersects
nested intervals in I′. If the number of such intervals is too
large, Corollary 3.21 yields the existence of a nested interval
J of I, which is then forced to intersect a.
the pushed-oﬀintervals in I, I′). Compare Figure 4 for an example of such
a local picture.
Now consider the arc a, put in minimal position with respect to C′. We
claim that (after possibly changing a by a further isotopy), the following
two properties hold:
(1) If a′ is a subarc of a in N, with both endpoints on ∂N, then a′
intersects C′.
(2) If a′ is a subarc of a, contained in N and with interior disjoint from
C′, then a′ intersects C′(I′) in at most D + 2 points (where D is the
constant from Corollary 3.21.
Before addressing why these claims hold, let us ﬁnish the proof of the lemma
assuming the claims. Namely, as we assume that i(a, C′) < K, we can write
a = a1 ∗· · · ∗ak,
k ≤K


## Page 18


18
SEBASTIAN HENSEL
into at most K subsegments whose interiors are disjoint from C′. In partic-
ular, the endpoints of the ai contribute at most K + 1 intersection points of
a with C′(I′), and any further intersection of a with C′(I′) which does not
correspond to one of the endpoints of the ai lies on one of the horizontal
segments of C′(I′) in N.
By (1), each ai can be written as a concatenation of at most three sub-
segments, each of which is either completely contained in N, or has interior
disjoint from N. The intersection points we have not yet accounted for are all
contained in subsegments lying in N. By (2), any such subsegment intersects
C′(I′) in at most D+2 points. This shows that L = (K +1)+3K(D+2)+1
has the property claimed in the lemma.
Finally, we explain why the properties (1) and (2) can be arranged. First,
suppose that a′ ⊂a is a subarc in N with endpoints in ∂N, and so that a′
does not intersect C′. Then, a′ bounds, together with a segment in ∂N, a
bigon B. Since the intersection of C′ with N consists of vertical segments,
and a′ is disjoint from C′, the whole bigon B is disjoint from C′ and C′(I′).
Hence, we can perform an isotopy pushing a over such a bigon, reducing the
number of intersections with ∂N, and without introducing intersection with
either C′ nor C′(I′). After a ﬁnite number of such modiﬁcations, property
(1) holds.
Next, consider a subarc a′ as in (2). Any intersection of the interior of
a′ with C′(I′) then lies on one of the horizontal segments corresponding
to an pushed-oﬀinterval in I′. To show (2), we need to show that there
are at most D such segments. So, suppose that there are at least D + 1
such intervals, call them I′
1, . . . , I′
D+1. Note that since the interior of a′ is
disjoint from C′, and therefore cannot cross the vertical lines bounded by
the endpoints of the I′
i, all these intervals are nested. Hence, Corollary 3.21
applies (with the roles of I, I′ reversed), and guarantees that there is an
interval J of I nested between two of the I′
i. But then a′ intersects C(I) in
the pushed-oﬀcopy of J, which contradicts the assumption on a. Compare
Figure 5 for this scenario.
□
We are now ready to prove the main theorem. The core is the following
lemma.
Lemma 3.23. Suppose that Cn is a sequence of cut systems, so that con-
secutive Ci are disjoint. Then there is a sequence In, so that for each n, In
is an essential pattern for Cn, and the patterns In, In+1 are compatible.
Proof. As a ﬁrst step, we apply Lemma 3.13 i) and ii) to obtain a sequence of
surgery patterns I1
n for Cn, so that for any n, the patterns I1
n, I1
n+1 are com-
patible. The strategy of the proof will be to inductively apply Lemma 3.19
to obtain sequences of patterns Ik
n where the next sequence (Ik+1
n
) is ob-
tained from the previous one (Ik
n) by applying a wave exchange to a single
pattern Ik
n. For brevity we will simply say that the new sequence is obtained
from the old one by a single wave exchange.


## Page 19


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
19
To begin, suppose that I1
1 admits a wave exchange, say with wings w1, w2.
As I1
2 is compatible with I1
1, we can apply Lemma 3.19. There are two
possible cases: First, if I1
1(w1, w2) is compatible with I1
2 we can set I2
1 =
I1
1(w1, w2) and I2
i = I2
i for i > 1. This new sequence is obtained from the
old one by a single wave exchange as desired.
The second case is that there is a wave exchange I1
2(w′
1, w′
2) which is
compatible with I1
1. In this case, we now need to apply Lemma 3.19 again,
this time for the exchange I1
2(w′
1, w′
2) and the pattern I1
3. If the ﬁrst case
happens here, we can deﬁne I2
2 = I1
2(w′
1, w′
2) and I2
i = I2
i for i ̸= 2, as the
exchange I1
2(w′
1, w′
2) is now compatible with both its neighbours I1
1, I1
3.
Otherwise, we need to restart the process with a wave exchange of I1
3.
Observe that since the sequence I1
n has ﬁnite length, this process terminates
either with the ﬁrst case of Lemma 3.19 at some index i, or by performing
a wave exchange on the last element of the sequence.
In both cases, we will have constructed I2
n, which is obtained from I1
n
by a single wave exchange. If I2
1 still admits a wave exchange, we restart
the process at the beginning, deﬁning I3
n. After ﬁnitely many iterations,
we obtain a sequence of patterns Im1
n
so that Im1
1
does not admit wave ex-
changes. Note that in this case, Lemma 3.19 implies that any wave exchange
of Im1
2
is compatible with Im1
1
(as otherwise, the latter would admit a wave
exchange).
Thus, we can restart the procedure, trying to perform wave exchanges at
Im1
2 . Arguing as above, after ﬁnitely many steps we will arrive at a sequence
Im2
n
where both Im2
1 , Im2
2
do not admit wave exchanges. After ﬁnitely many
steps, this yields desired sequence.
□
We are almost ready to start the proof. The last missing ingredient is the
following
Lemma 3.24. Suppose that (D, l), (D′, l′) ∈G(δ) are two vertices. Then
there is a geodesic (Cn, ln), n = 1, . . . , N in G connecting (D, l) to (D′, l′),
and so that for each 1 < i < N the meridian system Ci is a cut system.
Proof. Begin by taking any geodesic (Cn, ln) joining (D, l) to (D′, l′). Let
1 < i < N be the ﬁrst index so that Ci is not a cut system. By deﬁnition,
Ci is a ﬁlling meridian system, and therefore contains a cut system C′
i ⊂
Ci. Observe that (C′
i, li) is a vertex of G, which is still connected to both
(Ci−1, li−1) and (Ci+1, li+1). Replacing (Ci, li) by (C′
i, li) yields a geodesic
with fewer vertices whose ﬁlling meridian system is not a cut system. By
induction, the lemma follows.
□
Now let (D, l), (D′, l′) be arbitrary vertices of G(δ). Up to replacing the
endpoints by vertices of distance 1 (as in the proof of Lemma 3.24), we
may assume that D, D′ are the unions of δ with cut systems C, C′. Take a
geodesic (Ci, li) in G joining (D, l) to (D′, l′) as guaranteed by Lemma 3.24.
Apply Lemma 3.23 to C = C1, C2, . . . , CN−1, CN = C′ obtain a sequence
In of patterns as in that lemma.


## Page 20


20
SEBASTIAN HENSEL
Observe that for any 1 ≤n ≤N, the system Cn(In) is a meridian system
which is disjoint from δ. We let ˆCn be the ﬁlling meridian system obtained
from Cn(In) by adding every component of δ which is not already homotopic
to a component of Cn(In). Observe that since the empty pattern is the
only pattern for a cut system disjoint from δ, we have C1(I1) = C1 =
C, CN(IN) = CN = C′ and therefore ˆC1 = D, ˆCN = D′.
For each n, consider now
A′
n =

∂V −ˆCn

∩ln,
and choose for each n, a subset An ⊂A′
n containing a representative of each
homotopy class of arc in A′
n. Deﬁne
Γn = ˆCn ∪An,
and note that each Γn deﬁnes a vertex of R(δ) as ˆCn contains δ. Observe
that each arc a ∈An satisﬁes the prerequisites of Lemma 3.22 (for C =
Cn, C′ = Cn+1, I = In, I′ = In+1 and K depending on the constant used in
the deﬁnition of G), and therefore the intersection number of a with ˆCn+1 can
be bounded in terms of the L given by that lemma. Since the number of arcs
in An is bounded by the topology of the surface, and Cn(In), Cn+1(In+1) are
disjoint, this implies that there is a number M > 0 so that i(Γn, Γn+1) < M
for all n. Hence, Γn deﬁnes a path in R(δ) of length bounded above linearly
by N.
Furthermore, this path connects the image of (C1, l1) and (CN, lN) under
the map U : G(δ) →R(δ). Hence, the distance between (C1, l1) and (CN, lN)
is bounded above by a linear function in N = dG((D, l), (D′, l′)), showing
Theorem 3.1.
□
Remark 3.25. In order to prove the analogue of Theorem 3.1 for com-
pression body groups, only two minor modiﬁcations are necessary. First, in
Lemma 3.13, we have to do full surgeries, in order to keep the systems ﬁlling
meridian systems for the compression body. This is possible by Lemma 2.1.
Second, the model G needs to be adapted to compression bodies so that the
loop l is ﬁlling together with the ﬁlling meridian system (the model R need
not be modiﬁed).
4. Primitive and Annulus Stabilisers
In this section we encounter distorted stabilisers in the handlebody group.
There will be two classes of such stabilisers that we consider – those of
primitive curves, and those of primitive annuli.
Recall that a curve α on the boundary of a handlebody V is called prim-
itive if it deﬁnes a primitive element in the (free) fundamental group π1(V ).
Equivalently, α is primitive if there is a meridian δ which intersects α in a
single point.
A primitive annulus will mean a pair α1, α2 both of which are primitive,
and which bound a properly embedded annulus A in V .


## Page 21


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
21
Before beginning the discussion in earnest, we will ﬁrst summarise the
results that are proven in this section. In the statements of these results we
assume that the stabilisers in question are ﬁnitely generated; this is well-
known to experts, but we will give a quick proof below.
Theorem 4.1. Let Vg, g ≥3 be a handlebody of genus at least three, and
let α ⊂Vg be primitive. Then the stabiliser of α is exponentially distorted.
The genus requirement in Theorem 4.1 is necessary, as the following
proposition shows.
Proposition 4.2. Let V2 be a handlebody of genus 2, and let α be primitive.
Then the stabiliser of α is undistorted.
In fact, there are more distorted stabilisers in the handlebody group:
Theorem 4.3. Let Vg be a handlebody, and suppose that A is a primitive
annulus. Suppose that g ≥3 if A is non-separating, or that g ≥4 if A is
separating. Then the stabiliser of A is exponentially distorted.
Remark 4.4. It is not clear if the genus bound in Theorem 4.3 is optimal.
To the knowledge of the author, the analogous statement of Theorem 4.3
for Out(Fn) is new as well:
Proposition 4.5. The stabiliser of a primitive cyclic splitting in Out(Fn)
is exponentially distorted.
4.1. Algebraic description of primitive stabilisers. Stabilisers of prim-
itive curves, in contrast to the situation of meridians, cannot easily be re-
duced to lower-genus handlebody groups and point-pushing. In this subsec-
tion we discuss some of the diﬃculties encountered when trying to extend
the usual description of stabilisers using boundary pushing and a reduction
to smaller genus as for the mapping class group of a surface.
A reader
interested only in the geometry of stabilisers may safely skip to the next
subsection.
Throughout, α will be a primitive loop on ∂V . In particular, α is non-
separating. Let
∂V −α = Y,
where Y has two boundary components α+, α−corresponding to the two
sides of α. Recall that in the mapping class group of ∂V , we have a short
exact sequence
(1)
1 →Z →Mcg(Y ) →StabMcg(α) →1
where the ﬁrst map sends 1 to Tα+T −1
α−. Let ˆY be the surface gluing a disc to
the boundary component α−of Y . We also have a Birman exact sequence
(2)
1 →π1(U ˆY ) →Mcg(Y ) →Mcg( ˆY ) →1,


## Page 22


22
SEBASTIAN HENSEL
where U ˆY denotes the unit tangent bundle of ˆY .
We call the elements
of the kernel (boundary) pushes. This sequence splits, for example in the
following way: we deﬁne a α–splitting surface to be a subsurface S of Y so
that Y −S is a 3–holed sphere containing α−, α+ in its boundary. Then
the inclusion Mcg(S) →Mcg(Y ) yields the desired splitting. Hence, we can
identify Mcg(Y ) ∼= π1(U ˆY ) ⋊Mcg( ˆY ).
Since α is primitive, neither Y nor ˆY can be naturally identiﬁed with a
sub-handlebody. However, we can choose a α–splitting surface S which is
the boundary of a sub-handlebody, and use the splitting of the sequence (2)
to identify with quotient with Mcg(S). We then obtain an exact sequence
1 →π1(U ˆY ) ∩H(V ) →Mcg(Y ) ∩H(V ) →H(S) →1.
Recall that H(S) is deﬁned as the intersection of H(V ) with Mcg(S).
Therefore, describing the stabiliser of α relies on describing the subgroup
Γ = π1(U ˆY ) ∩H(V ) of the boundary pushing subgroup.
Recall that we have a short exact sequence
1 →Z →π1(U ˆY ) →π1(S) →1,
and under the identiﬁcation of π1(U ˆY ) with a subgroup of Mcg(Y ), the
kernel corresponds to the Dehn twist about α.
In particular, since the
twist about α is not contained in the handlebody group of V , the group Γ
intersects each ﬁbre of π1(U ˆY ) →π1(S) in at most one point.
Intuitively, it is clear that the group Γ is much smaller than π1(S).
Namely, consider a meridian δ which intersects α in a single point. If a ⊂Y
is an arc based at α−disjoint from δ except in its endpoints, then the push
about a maps δ to the curve obtained by concatenating δ∩Y with a. Hence,
in order for the push to be in H(V ), the arc a would have to deﬁne a merid-
ian as well. In fact, as the following lemma shows, Γ can be generated by
such elements.
Lemma 4.6. The intersection of π1(U ˆY ) with the handlebody group is
generated by the image of all loops in S −α which are embedded meridi-
ans. These elements correspond to annular twists TαT −1
β
where α, β are the
boundary of a properly embedded annulus in V , composed with Dehn twists
about meridians.
Before proving Lemma 4.6, we want to mention that although pushes
about embedded meridians generate Γ, the group does not simply consist of
pushes along V –trivial arcs. In fact, we have the following.
Lemma 4.7. For V of genus g ≥3, the group Γ is not normal in π1(U ˆY ).
We prove Lemma 4.7 in the appendix, since the proof only consists of
a careful, somewhat lengthy check of intersection patterns. However, we
want to emphasise the following consequence of Lemma 4.7 in combination


## Page 23


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
23
with Lemma 4.6, which may be of independent interest, and highlights an-
other diﬀerence between the complements of meridians and primitives in a
handlebody.
Corollary 4.8. The kernel ker(π1(S −α) →π1(V )) of the map induced by
inclusion is not generated by embedded curves.
Proof of Lemma 4.6. Recall that Γ = π1(U ˆY ) ∩H, and denote by Γ0 the
subgroup generated by the pushes as in the statement of the lemma. Pick a
point p ∈α, and note that it deﬁnes points p−, p+ ∈Y . Deﬁne A to be the
graph whose vertices correspond to homotopy classes of arcs a ⊂Y joining
p−to p+, so that a deﬁnes a meridian on ∂V . We join two vertices with an
edge, if the corresponding arcs are disjoint except at their endpoints. Note
that H(V ) ∩Mcg(Y ) acts on A as isometries.
Observe that there is an arc a as above, so that Y \ a is homotopy
equivalent to the splitting surface S.
Hence, the stabiliser of this arc a
in H(V ) ∩Mcg(Y ) is equal to (the image of) H(S).
To prove the lemma, it therefore suﬃces to show that Γ0 acts transitively
on the vertex set of A. To this end, ﬁrst consider two arcs a, a′ corresponding
to adjacent vertices of A. Then the concatenation l = a−1 ∗a′ is a loop
joining p−to itself, and furthermore it deﬁnes an embedded meridian in Y .
Hence, the push P(l) about l is an element of the handlebody group (it is
an annular twist). Furthermore, we have
P(l)(a′) = a
Hence, to prove the claim, it suﬃces to show that A is connected. This
follows from a standard surgery argument: suppose a, a′ are any two arcs
representing vertices that are not disjoint. Since they both deﬁne meridians
on ∂V , there is a wave w ⊂a′. A suitable surgery aw then intersects Y
in an arc still connecting p−to p+, which is otherwise disjoint from a, and
intersects a′ in strictly fewer points.
□
4.2. Upper distortion bounds. The upper distortion bounds in Theo-
rem 4.1, 4.3 and Proposition 4.5 follow from a surgery construction. We
begin by describing the case of an annulus A in a handlebody in detail; the
case of a primitive element is very similar. Then we discuss the case of a
primitive cyclic splitting in the free group.
We are again using the two complexes G and R which appeared in Sec-
tion 3. In fact, we consider the following sub-complex:
Deﬁnition 4.9. Let G(A) to be the full sub-complex of G of all those vertices
whose cut system C intersects each curve in ∂A in exactly one point, and
also so that l intersects each curve in A at most in one point.
Deﬁnition 4.10. Let R(A) be the full sub-complex of G of all those vertices
whose cut system C intersects each curve in ∂A in exactly one point, and
also so that ∂A embeds in the graph as an embedded subgraph.


## Page 24


24
SEBASTIAN HENSEL
Lemma 4.11. Suppose that C, C′ are cut systems both of which intersect
each component of A in exactly one point. If C and C′ are not disjoint, then
there is a surgery C1 of C in direction of C′ (i.e. deﬁned by a wave of a
component c′ ∈C′ with respect to C) which also intersects each component
of A in exactly one point. In addition, we may assume that this wave is
disjoint from A.
Proof. Let α be one of the boundary components of A. Since C′ intersects
C, there is are two distinct waves w1, w2 of some component of C′ with
respect to C.
Since α intersects C′ in a single point, we may assume without loss of
generality that w1 does not intersect α. Let C1 be the cut system surgery
deﬁned by that wave w1. As the wave w1 is disjoint from α, the result C1
intersects α in at most one point. As α is nontrivial in π1(V ), it cannot be
disjoint from a cut system – hence, α intersects C1 in a single point.
Consider now the second boundary component β of A. Since β intersects
both C and C′ in one point, it intersects C1 in at most two points. Let D1
be a collection of disjoint, properly embedded discs, bounded by C1. Then α
intersects D1 in a single point. As α, β are freely homotopic, β also intersects
D1 in an odd number of points (as the parity of intersection can be detected
by the algebraic intersection pairing, and therefore it is an invariant of free
homotopy classes). Hence, it is impossible that β intersects C1 in zero or
two points, and β intersects C1 in a single point as claimed.
□
As a consequence, we get the following two results
Corollary 4.12. Given two cut systems C, C′, both of which intersect each
component of A in a single point, there is a sequence
C = C0, C1, . . . , Cn, Cn+1 = C′
of cut systems so that all Ci intersect each component of A in a single point,
n ≤i(C, C′), and consecutive Ci, Ci+1 are obtained by surgery at a wave wi
disjoint from A.
Corollary 4.13. After possibly increasing the constants chosen in their
deﬁnitions, the graphs G(A), R(A) are connected. The stabiliser of A acts
on them properly discontinuously and cocompactly. Hence, this stabiliser is
in particular ﬁnitely generated.
Proof. By choosing the constants in the feﬁnition of R large enough, any
two vertices whose underlying ﬁlling meridian system is the same can be
joined by a path with the same meridian system (compare the proof of
Lemma 3.4).
Hence, the same is true in R(A) (as one can simply keep
the edges corresponding to A). Now, Corollary 4.12 implies connectivity by
arguing as in the proof of Lemma 3.4. The fact that the stabiliser of A acts
cocompactly is also shown exactly as in Lemma 3.4.
□
We also note the following (compare e.g.
[HH1, Corollary A.4] for a
similar result)


## Page 25


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
25
Proposition 4.14. There are numbers a, b so that the following holds. Let
(C, l) ∈G be any vertex, and f ∈H(V ) be a handlebody group element.
Then
i(C ∪l, f(C ∪l)) ≤a · b∥f∥H(V ).
Proof. Since G and H(V ) are quasi-isometric, it suﬃces to show that i(C ∪
l, C′ ∪l′) can be bounded by an exponential function of d((C, l), (C′, l′)). To
show this, it in turn suﬃces to show that there is a constant K so that
i(C ∪l, C′ ∪l′) ≤Ki( ˆC ∪ˆl, C′ ∪l′)
whenever ( ˆC, ˆl), (C, l) are adjacent in G. Denote by D1, . . . , Dk the comple-
mentary components of C ∪l. Observe that k can be bounded in terms of
i(C, l), which in turn is bounded by a constant chosen in the deﬁnition of G.
Denote by c′
1, . . . , c′
N, l′
1, . . . , l′
M the intersection arcs of C′, l′ with the Dj.
The total number N + M of these arcs is bounded by i(C ∪l, C′ ∪l′).
Now, since (C, l), ( ˆC, ˆl) are adjacent we can similarly write ˆC and ˆl as
concatenations of arcs ˆc1, . . . , ˆcr, ˆl1, . . . , ˆls in the Dj. Here, the total number
r + s is again uniformly bounded, dependent only on the constants deﬁning
G. Since all Di are discs, up to homotopy ﬁxing endpoints, any ˆci or ˆli and
any c′
j or l′
j intersect in at most one point. Hence, we have
i( ˆC ∪ˆl, C′ ∪l′) ≤(r + s)(N + M) ≤Ki(C ∪l, C′ ∪l′),
for a suitable choice of K. This shows the proposition.
□
The key to the upper distortion bound lies in the following two lemmas,
which we will use to inductively build a path.
For their formulation, suppose that Γ is a graph representing a vertex
of R. Recall that this means that, in particular, there is an embedded cut
system C ⊂Γ. We denote this system by C(Γ), and we call any edge of Γ
which is not contained in C a rope edge.
Lemma 4.15. Let C be a cut system, so that C intersects each component
of A in a single point. Suppose that Γi is a vertex of R(A), so that each
rope edge e of Γi intersects C in at most K points. Then there is a vertex
Γ′
i of R(A) with the following properties:
i) C(Γi) = C(Γ′
i).
ii) Each rope edge of Γ′
i intersects C in at most K points.
iii) Each arc in C ∩(∂V −C(Γ′
i)) which is disjoint from A, is disjoint from
the rope edges of Γ′
i up to homotopy.
iv) The distance between Γi and Γ′
i in R(A) is at most L1K. Here, L1 is a
constant depending only on the topological type of S, and the constants
deﬁning the graph R.
Proof. To obtain Γ′
i from Γi, we will successively replace rope edges using
surgery using segments in C. None of these moves change the underlying
meridian system, guaranteeing property i), and cannot introduce new inter-
sections with C, guaranteeing property ii).


## Page 26


26
SEBASTIAN HENSEL
For any pair of a C–arc disjoint from A, and rope edge, at most K surg-
eries are needed to make them disjoint (by assumption on the intersection
number of rope edges and C–arcs), and each surgery step stays in R(A).
Since the number of diﬀerent C–arcs is uniformly bounded by the genus of
∂V , and the same is true for the number of rope edges of Γi, this shows that
after at most L1K steps we arrive at the desired Γ′
i (where L1 just depends
on the number of possible topological types of rope edges and C–arcs).
□
Lemma 4.16. Suppose that Γ′
i is a vertex of R(A), and that Ci+1 is a cut
system obtained from Ci = C(Γ′
i) from a surgery move in the direction of
C, deﬁned by a wave w disjoint from A.
Further suppose that each rope edge of Γ′
i is disjoint from w, and that
each rope edge of Γ′
i intersects C in at most K points.
Then there is a vertex Γi+1 of R(A) with the following properties:
i) C(Γi+1) = Ci+1.
ii) Every rope edge of Γi+1 intersects C in at most max{K, i(C, Ci)} points.
iii) The distance between Γ′
i, Γi+1 in R(A) is at most 1.
Proof. First, by possibly adding w as an additional rope edge, we may re-
place Γ′
i by an adjacent vertex Γ′′
i so that w is a rope edge.
Then, Γ′′
i contains Ci+1 as a subgraph, and we deﬁne Γi+1 to be this
vertex, guaranteeing i). In particular, observe that w has ceased to be a
rope edge of Γi+1 (as it is now part of the meridian system), and Γi+1
instead has a rope edge c which is a subarc of Ci. In particular, that rope
edge intersects C in at most i(C, Ci) points. Any other rope edge of Γi+1 is
also a rope edge of Γ′
i, so by assumption it has at most K intersections with
C. Hence, property ii) holds.
Property iii) is clear from the construction.
□
Proof of the upper bound in Theorem 4.3. Fix a basepoint (C, l) ∈G(A), so
that the two A–arcs can be made disjoint from the l–arcs by homotopy. This
exists, assuming that the constants deﬁning G(A) are chosen large enough:
e.g. by starting with the A–arcs, and adding enough additional arcs so that
any boundary of S −C is joined to any other. The resulting l intersects
any curve in C, and every wave relative to C, and therefore is discbusting.
The number of arcs necessary depends only on the number of boundary
components of S −C (hence, the genus of S), and thus if the constant
deﬁning G is chosen large enough, (S, l) deﬁnes a vertex.
Now consider an element f ∈Stab(A). We then know, from Proposi-
tion 4.14 that
i(C ∪l, f(C ∪l)) ≤a · b∥f∥H(V ) = M.
Let Γ ⊂C ∪l be the vertex of R corresponding to (C, l), and let Γ0 = f(Γ)
be the image under f.


## Page 27


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
27
We begin by applying Corollary 4.12 to obtain a surgery sequence C1, . . . , CL
from f(C) to C, of length L ≤M. We have i(Cj, C) ≤M for all j, and
each surgery step in this sequence is done using a wave disjoint from A.
Next, we apply Lemma 4.15 to Γ0 and M as the intersection bound. We
obtain a vertex Γ′
1, with d(Γ0, Γ′
1) ≤L1M, and so that Γ′
1 satsiﬁes the
prerequisites of Lemma 4.16. Applying the latter lemma yields a vertex Γ2
of distance ≤1, with C(Γ2) = C2, and where each rope still has intersection
at most max{M, i(C1, C)} ≤M with C.
Thus, we can inductively build a path of length n(L1M+1) ≤M(L1M+1)
joining f(Γ) to a vertex Γn with C(Γn) = C. Recall that the stabiliser of C
in the handlebody group of V is equal to the stabiliser of C in the mapping
class group of ∂V . Hence, the stabiliser of C ∪A in the handlebody group
is also equal to the stabiliser of C ∪A in the mapping class group.
In
the mapping class group, stabilisers of curve systems, or arc systems, are
undistorted [MM]. Hence, the stabiliser of C ∪A is also undistorted in the
handlebody group, and therefore there is a path of length coarsely bounded
by M(L1M + L2) joining Γn to Γ in R(A).
As these length bounds are polynomial in M, the triangle inequality yields
that the distance between Γ and f(Γ) in R(A) can be bounded by an expo-
nential in ∥f∥H(V ), showing that R(A) is at most exponentially distorted.
This shows the upper bound in Theorem 4.3.
□
To prove Proposition 4.5, we work in a doubled handlebody. First, us-
ing surgeries of sphere systems instead of meridian systems we show the
following analogue of Corollary 4.12 with essentially the same argument.
Lemma 4.17. Let W = #gS1 × S2 be a doubled handlebody, and suppose
that T ⊂W is an embedded torus so that the image of π1(T) →π1(W) is a
cyclic group generated by an primitive element of the free group π1(W).
Suppose that σ, σ′ are two sphere systems in minimal position, each of
which intersects T in a single circle. Then there is a sequence
σ = σ0, σ1, . . . , σn, σn+1 = σ′
so that each σi intersects T in a single circle, and n is at most the number
of intersection circles in σ ∩σ′.
Proof. Consider σ ∩σ′, which is a collection of disjoint circles. Consider any
innermost circle C of this collection, i.e. a circle which bounds a disc D ⊂σ′
whose interior is disjoint from σ. As there are at least two such innermost
circles, we can choose one where D is disjoint from the torus T.
We deﬁne σ1 as the surgery of σ using this disc D. As T cannot become
disjoint from a ﬁlling sphere system (otherwise the image of π1(T) in π1(W)
would be trivial), T will intersect σ1 in a single circle as well.
Further, σ1 has at least one fewer intersection circle with σ′, and so the
lemma follows by induction.
□
We also have the following analog of Proposition 4.14:


## Page 28


28
SEBASTIAN HENSEL
Lemma 4.18. Let W = #gS1×S2 be a doubled handlebody. Then there are
numbers a, b so that the following holds. Let σ be any ﬁlling sphere system,
and f ∈Mcg(W) be arbitrary. Then, in minimal position, the number of
intersection circles in σ ∩f(σ) is at most
a · b∥f∥Mcg(W ).
Proof. To show the lemma, it suﬃces to show that there is a number C so
that if σ, σ′ are any two sphere systems, and σ′′ is disjoint from σ′, then
i(σ, σ′′) ≤Ci(σ, σ′) + C
This follows since σ′′ intersects each component of σ ∩(W −σ′) in at most
one circle.
□
Together with Lemma 4.17, this lemma proves the upper bound in Propo-
sition 4.5 by induction.
Finally, we prove the undistortion statement in genus 2 for primitive sta-
bilisers.
Proof of Proposition 4.2. As in Section 3, we aim to project paths in R
to R(α). First, we observe the following preliminary step. Suppose that
∆= {δ1, δ2} is any cut system. Then, since α is primitive, at least one of
ι(α, δ1), ι(α, δ2) is odd. In particular, there is a subarc d ⊂δ1∪δ2 connecting
the two diﬀerent sides of α. One component of the boundary of a regular
neighbourhood of d ∪α is a separating meridian δ(d). As V2 has genus 2,
there is a unique cut system ∆(d) disjoint from δ(d). Since α is disjoint from
δ(d), it intersects this cut system in a single point. Observe that if d′ is any
other possible choice of arc, the meridians δ(d), δ(d′) intersect in at most
four points, and thus ∆(d), ∆(d′) also intersect in uniformly few points.
The same argument shows that if ∆′ is a disjoint cut system, and d′ is an
admissible arc, then ∆(d), ∆′(d′) intersect in uniformly few points. Hence,
we can deﬁne a Lipschitz projection of H2 to the stabiliser of α.
□
4.3. Lower distortion bounds. The proofs of the lower distortion bounds
for all three results mentioned at the beginning of this section are very
similar, and rely on two main ingredients. On the one hand, we use the
following theorem, which is shown by Handel-Mosher ([HM, Section 4.3,
Case 1]):
Theorem 4.19. Let n ≥3 be given, and Fn is a free group with free basis
e1, . . . , en. Suppose that Θ : ⟨e1, e2⟩→⟨e1, e2⟩is an irreducible automor-
phism of exponential growth. Deﬁne an automorphism fk ∈Out(Fn) by the
rule
ei 7→ei,
i < n
en 7→enΘk(e1).
Then the norm of fk in the stabiliser of the conjugacy class [e1] grows expo-
nentially in k.


## Page 29


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
29
Figure 6. Left: The setup to construct distorted curve sta-
bilisers. Right: A non-separating annulus ﬁxed by the ele-
ments fk. A separating annulus with the same property could
be constructed by making ˆα1 surround both discs D−
g , D+
g
where the lower handle is attached.
The second ingredient is a construction similar to the one employed in
Section 3 of [HH2].
Namely, let X be a surface of genus 1 with one boundary component.
Consider the 3–manifold W = X × [0, 1], which is a handlebody of genus 2.
The boundary
∂W = X0 ∪A ∪X1,
Xi = {i} × X, A = ∂X × [0, 1]
consists of two copies of X and an annulus A. There is a map
ι : Mcg(X) →H(W),
which maps a homeomorphism f of X to the homeomorphism f × id of W.
Choose 2(g −2) disjoint discs D−
i , D+
i
⊂int(A), for i = 3, . . . , g and
for each i attach a three-dimensional 1-handle hi to D+
i , D−
i
to obtain a
handlebody V of genus g. Observe that homeomorphisms of X which have
the form f × id restrict to the identity on the annulus A, and therefore the
map ι yields a map
ι′ : Mcg(X) →H(V )
by sending f to the homeomorphism which restricts to f × id on W, and to
the identity on all handles hi.
Let α ⊂X be a non-separating simple closed curve, and denote by αj =
α × {j} for j = 0, 1.
Observe that α0, α1 are homotopic in V , and are
primitive. Let β0 ⊂(A \ ∪i(D+
i ∪D+
i )) ∪X0 be a simple closed curve which
bounds a pair of pants together with ∂D−
g
and α0 (compare Figure 6).
Consider the mapping class
P = Tα0T −1
β0 ∈H(V ),
which is a handle slide.
Choose a basis e1, . . . , eg for π1(V ), so that e1, e2 correspond to loops in
X0, the loop α0 deﬁnes the conjugacy class of e1, and the loops e3, . . . , eg
are dual to the handles hi, not entering X0 ∪X1.
We summarise some
important properties of P in the following lemma.


## Page 30


30
SEBASTIAN HENSEL
Lemma 4.20. The element P induces the following automorphism on π1(V )
with respect to the basis chosen above:
ei 7→ei, i < g
eg 7→ege1.
Furthermore, P ﬁxes the curve α0 and restricts to the identity on X1.
Let ψ be a pseudo-Anosov element of X which induces an irreducible,
exponentially growing automorphism Θ of π1(X) = F2. Recall that Ψ =
ι′(ψ) is then an element of the handlebody group of V , which restricts to ψ
on X. Deﬁne the elements
fk = ΨkPΨ−k
Each fk lies in the handlebody group, and we have the following
Lemma 4.21. The element fk induces the following automorphism on π1(V )
with respect to the basis chosen above:
ei 7→ei, i < g
eg 7→egΘk(e1).
Furthermore, each fk ﬁxes
i) the curve α1,
ii) a non-separating annulus A, one boundary component of which is α1,
iii) for each h = 1, . . . , g −2, a separating annulus Ah, one boundary com-
ponent of which is α1, and so that one complementary component of Ah
has genus h.
Here, the annuli A, Ah do not depend on k.
Proof. The claim on the action on fundamental group is clear from Lemma 4.20.
Also observe that since P acts as the identity on X1, the same is true for
fk. This immediately implies that the mapping class fk preserves the loop
α1 ⊂X1. Furthermore, we can choose a curve ˆα1 which is disjoint from
α0, β0 and bounds an annulus A together with α1 (compare Figure 6). By
choosing the ∂D±
i to lie on the correct side of ˆα1, α1, we can ensure that the
annulus A can be non-separating or separating, and in the latter case, we
can choose the genus separated oﬀfreely between 1 and g −2.
□
Now we are ready to prove the lower distortion parts of the theorems
mentioned at the beginning of this section.
Proof of the lower bound in Theorem 4.1. The stabiliser of any primitive curve
α is conjugate, in the handlebody group, to the stabiliser of α1. Hence, it
suﬃces to show that the stabiliser of α1 is at least exponentially distorted.
We use the elements fk as above.
Suppose that f ∈StabH(V )(α1) is given. Then, since α1 (and α0) de-
ﬁne the conjugacy class [e1] in π1(V ), the induced automorphism f∗∈


## Page 31


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
31
Out(π1(V )) ﬁxes the conjugacy class [e1]. In other words, there is a group
homomorphism
π : StabH(V )(α1) →StabOut(Fg)([e1]).
Recall that for any choice of word norms, group homomorphisms are Lips-
chitz maps. By Theorem 4.19, the elements π(fk) have norm growing expo-
nentially in k. Hence, the sequence fk has norms growing at least exponen-
tially in StabH(V )(α1). On the other hand, as fk = ΨkPΨk, the norm of fk
in H(V ) is clearly growing linearly in k. This shows that StabH(V )(α1) is at
least exponentially distorted in H(V ).
□
Proof of the lower bound in Theorem 4.3. The stabiliser of any annulus as
in that theorem is conjugate to an annulus A or Ah as in Lemma 4.21.
Now, we can ﬁnish the proof just like the previous argument. Namely, the
elements fk as above ﬁx A, Ah, and also the stabilisers of these annuli are
contained in the stabiliser of α1.
□
As mentionend in the introduction, the lower distortion bound in Propo-
sition 4.5 follows directly from [HM]. For completeness, we include a proof
(from a topological perspective).
Proof of the lower bound in Proposition 4.5. We use the connection of Out(Fn)
to the mapping class group of a the double of a handlebody. Let W be the
closed 3–manifold obtained by doubling V about its boundary. Recall the
short exact sequence [Lau, Th´eor`eme 4.3, Remarque 1)]
1 →K →Mcg(W) →Out(Fn) →1
where K is ﬁnite, and the right map is induced by the action on the fun-
damental group. We also have a natural map H →Mcg(W) obtained by
doubling, so that the composition H →Mcg(W) →Out(Fn) agrees with
the action on the fundamental group of the handlebody.
Under the doubling map H →Mcg(W), the stabiliser of an annulus A
as above in H maps to the stabiliser of a torus TA, so that the image of
π1(TA) in π1(W) is generated by [e1]. Under the map Mcg(W) →Out(Fn)
the stabiliser of TA maps to the stabiliser of a primitive cyclic splitting Z,
where the amalgamating group is generated by [e1]. The same argument
as above then shows that the image of the sequence fk has length growing
exponentially in k in the stabiliser of Z. As all primitive cyclic splittings
diﬀer by an element of Out(Fn), this shows that all stabilisers of primitive
cyclic splittings are at least exponentially distorted.
□


## Page 32


32
SEBASTIAN HENSEL
Figure 7. The left three pictures show the relevant curves
in the proof of Lemma 4.7. For ease of depiction, in all of
these pictures the handlebody structure is the “outside” han-
dlebody in the standard Heegaard splitting of S3. The three
pictures on the right depict the action of the twist product
on µ: the top shows Tγ1µ = Tγ1Tδ1µ, the middle one shows
T −1
δ1 Tγ1Tδ1µ and in the bottom one γ1 is shown superimposed.
Below is the basis used to compute the element after applying
all twists.
Appendix A. The proof of Lemma 4.7
We give the proof in the case of a genus 3 handlebody, but the method
extends to any genus ≥3.
Consider two disjoint loops γ, δ as in Figure 7 on the left, based at the
curve α−, i.e. loops so that under the identiﬁcation of ˆY with the split-
ting surface S, the loop δ is a separating meridian, while γ is a primitive
curve. We will show that the boundary push about any element in the ﬁ-
bre of π1(U ˆY ) →π1(S) over the commutator [δ, γ] is not contained in the
handlebody group. This is enough to prove the lemma.


## Page 33


(UN)DISTORTED STABILISERS IN THE HANDLEBODY GROUP
33
A push along δ will be of the form
Pδ = T −1
δ1 Tδ2T k
α
for some k, where δ1, δ2 are disjoint from δ and bound a pair of pants together
with α (see Figure 7 for this setup). Here and below, bounding a pair of
pants, and twists are meant as objects on S, before cutting at α. Similarly,
a push along γ will be of the form
T −1
γ1 Tγ2T l
α
for some l, and γ1, γ2 disjoint and bounding a pair of pants with α.
Since δ2, γ2 are disjoint from all other involved curves, and the correspond-
ing Dehn twists therefore commute with all others involved in the deﬁnition
of Pδ, Pγ, we can compute the commutator of the pushes as
Ψ = [Pγ, Pδ] = T −1
γ1 T −1
δ1 Tγ1Tδ1.
To prove the lemma, we therefore need to show that T n
α Ψ is not in the
handlebody group for any n. To show this claim, we will study the eﬀect of
T n
α Ψ on a meridian µ, which is disjoint from δ1 and intersects γ2 in a single
point. First note that µ itself, as well as δ1, γ1 are disjoint from α, and so
the image T n
α Ψ(µ) will not depend on n. Thus, we may assume n = 0.
The action of the ﬁrst three twists is shown in Figure 7 on the right.
Twists are executed right-to-left, Tx is a left-handed twist about the curve
x.
Instead of actually performing the ﬁnal twist, we can now determine the
resulting word in π1(V ) by recording intersections with a cut system as
follows. We choose a cut system consisting of three discs D1, D2, D3. Here,
D1 is freely homotopic to µ, D2 intersects α in a single point, and D3 is
disjoint from all curves involved. Compare the bottom picture in Figure 7.
We also choose transverse orientations, so that the cut system deﬁnes an
oriented basis x, y, z of π1(V ).
To ﬁnd the element which T −1
γ1 T −1
δ1 Tγ1Tδ1µ deﬁnes in π1(V ), we now follow
along the purple curve, starting at the solidly drawn basepoint, turn right
and follow γ1 whenever we encounter γ1, and keep track of intersections
with D1, D2. With the transverse orientations as in Figure 7, this yields the
following word (for readability, intersections due to γ1 are bracketed):
x(x−1y−1)(xy)y(y−1x−1)(yx)(y−1x−1) = y−1xyx−1yxy−1x−1
This is a nontrivial element in π1(V ), and therefore T −1
γ1 T −1
δ1 Tγ1Tδ1µ is not
a meridian.
References
[Far]
Benson Farb. The extrinsic geometry of subgroups and the generalized word prob-
lem. Proc. London Math. Soc. (3) 68(1994), 577–593.
[FM]
Benson Farb and Dan Margalit. A primer on mapping class groups, volume 49 of
Princeton Mathematical Series. Princeton University Press, Princeton, NJ, 2012.


## Page 34


34
SEBASTIAN HENSEL
[HH1]
Ursula Hamenst¨adt and Sebastian Hensel. The geometry of the handlebody groups
I: distortion. J. Topol. Anal. 4(2012), 71–97.
[HH2]
Ursula Hamenst¨adt and Sebastian Hensel. The geometry of the handlebody groups
II: Dehn functions. arXiv:1804.11133 (2018).
[HM]
Michael Handel and Lee Mosher. Lipschitz retraction and distortion for subgroups
of Out(Fn). Geom. Topol. 17(2013), 1535–1579.
[Hem]
John Hempel. 3-manifolds as viewed from the curve complex. Topology 40(2001),
631–657.
[Hen]
Sebastian Hensel. A primer on handlebody groups. preprint,
available at
http://www.mathematik.uni-muenchen.de/ hensel (2017).
[Lau]
Fran¸cois Laudenbach. Topologie de la dimension trois: homotopie et isotopie.
Soci´et´e Math´ematique de France, Paris, 1974. With an English summary and
table of contents, Ast´erisque, No. 12.
[Luf]
E. Luft. Actions of the homeotopy group of an orientable 3-dimensional handle-
body. Math. Ann. 234(1978), 279–292.
[MM]
H. A. Masur and Y. N. Minsky. Geometry of the complex of curves. II. Hierarchical
structure. Geom. Funct. Anal. 10(2000), 902–974.
[Mas]
Howard Masur. Measured foliations and handlebodies. Ergodic Theory Dynam.
Systems 6(1986), 99–116.
[McC1] Darryl McCullough. Twist groups of compact 3-manifolds. Topology 24(1985),
461–474.
[McC2] Darryl McCullough. Virtually geometrically ﬁnite mapping class groups of 3-
manifolds. J. Diﬀerential Geom. 33(1991), 1–65.
Sebastian Hensel
Mathematisches Institut der Universit¨at M¨unchen
Theresienstraße 39, 80333 M¨unchen
Email: hensel@math.lmu.de

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1901_04387v2_un_distorted_stabilisers_in_the_handlebody_group
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1901_04387V2_UN_DISTORTED_STABILISERS_IN_THE_HANDLEBODY_GROUP.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

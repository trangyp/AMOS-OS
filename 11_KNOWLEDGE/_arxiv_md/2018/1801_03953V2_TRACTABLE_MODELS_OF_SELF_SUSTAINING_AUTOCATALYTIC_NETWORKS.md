---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1801.03953v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1801.03953v2_Tractable_models_of_self-sustaining_autocatalytic_networks

> Source: 1801.03953v2_Tractable_models_of_self-sustaining_autocatalytic_networks.pdf

> Pages: 19

---


## Page 1


TRACTABLE MODELS OF SELF-SUSTAINING AUTOCATALYTIC
NETWORKS
MIKE STEEL∗AND WIM HORDIJK†
Abstract.
Self-sustaining autocatalytic networks play a central role in living systems, from
metabolism at the origin of life, simple RNA networks, and the modern cell, to ecology and cognition.
A collectively autocatalytic network that can be sustained from an ambient food set is also referred
to more formally as a ‘Reﬂexively Autocatalytic F-generated’ (RAF) set.
In this paper, we ﬁrst
investigate a simpliﬁed setting for studying RAFs, which are nevertheless relevant to real biochemistry
and allows for a more exact mathematical analysis based on graph-theoretic concepts.
This, in
turn, allows for the development of eﬃcient (polynomial-time) algorithms for questions that are
computationally NP-hard in the general RAF setting. We then show how this simpliﬁed setting for
RAF systems leads naturally to a more general notion of RAFs that are ‘generative’ (they can be
built up from simpler RAFs) and for which eﬃcient algorithms carry over to this more general setting.
Finally, we show how classical RAF theory can be extended to deal with ensembles of catalysts as well
as the assignment of rates to reactions according to which catalysts (or combinations of catalysts)
are available.
Key words.
autocatalytic network, directed graph, strongly-connected components, cycles,
closure, reaction rates
AMS subject classiﬁcations. 05C20, 05C38, 47N60, 68Q25, 68R10
1. Introduction. A central property of the chemistry of living systems is that
they combine two basic features: (i) the ability to survive on an ambient food source,
and (ii) each biochemical reaction in the system requires only reactants and a catalyst
that are provided by other reactions in the system (or are present in the food set).
The notion of a self-sustaining ‘collectively autocatalytic set’ tries to capture these
basic features formally, and was pioneered by Stuart Kauﬀman [13, 14], who investi-
gated a simple binary polymer model to address questions that relate to the origin
of life.
The notion of a collectively autocatalytic set was subsequently formalised
more precisely as ‘Reﬂexively Auto-catalytic and F-generated’ (RAF) sets (deﬁned
shortly) and explored by others [20, 8]. RAFs are related to other notions such as
Rosen’s (M;R) systems [12], and ‘organisations’ in Chemical Organisation Theory [9].
The application of RAFs has expanded beyond toy polymer models to analyse both
real living systems (e.g. the metabolic network of Escherichia coli [16]) and simple
autocatalytic RNA systems that have recently been generated in laboratory studies
by [19].
The generality of RAF theory also means that a ‘reaction’ need not refer specif-
ically to a chemical reaction, but to any process in which ‘items’ are combined and
transformed into new ‘items’, and where similar ‘items’ that are not used up in the
process facilitate (or ‘catalyse’) the process. This has led to application of RAF the-
ory to processes beyond biochemistry, including biodiversity [5], cognitive psychology
[4], and (more speculatively) economics [8].
In this paper, we show how RAF theory can be developed further to:
• provide an exact and tractable characterisation of RAFs and subRAFs when
reactants involve just food molecules;
∗Biomathematics Research Centre,
University of Canterbury,
Christchurch,
New Zealand
(mike.steel@canterbury.ac.nz).
†Institute
for
Advanced
Study,
University
of
Amsterdam,
The
Netherlands
(wim@WorldWideWanderings.net).
1
arXiv:1801.03953v2  [q-bio.MN]  27 Mar 2018


## Page 2


• extend this last concept to general catalytic reaction networks by deﬁning a
new type of RAF (‘generative’) which couples realism with tractability; and
• include reaction rates into RAF theory and show that an optimal RAF can
be calculated in polynomial time.
We begin with some deﬁnitions.
1.1. Catalytic reaction systems (CRSs). A catalytic reaction system (CRS)
consists of a set X of ‘molecule types’, a set R of ‘reactions’, an assignment C describ-
ing which molecule types catalyse which reactions, and a subset F of X consisting of
a ‘food set’ of basic building block molecule types freely available from the environ-
ment. Here, a ‘reaction’ refers to a process that takes one or more molecule types (the
‘reactants’) as input and produces one or more molecule types as output (‘products’).
C can be viewed as a subset of X × R.
A CRS can be represented mathematically in two essentially equivalent ways:
Firstly as a directed graph with two types of vertices (corresponding to molecule
types (some of which lie in the food set F) and reactions) and two types of arcs (arcs
from molecule types into and out of reaction vertices (as reactants and products,
respectively, and arcs from molecule types to reactions to denote catalysis). Fig. 1
provides a simple example of a CRS represented in this way.
Alternatively, one can list the reactions explicitly, writing each in the form
r : A
c1,c2,...
−−−−−→B,
where A denotes the set of reactants of reaction r, B the set of products of r, and
c1, c2, . . . are the possible catalysts for r. For example, for r2 and r3 in the CRS of
Fig. 1 we write:
r2 : f2 + f3
p3
−→p2,
r3 : f3 + f4
p2
−→p3,
to denote that r2 is catalysed by p3 and r3 is catalysed by p2.
r1
r2
r3
r4
p
2
p
3
p
1
p
4
r5
p
5
f1
f2
f3
f4
f5
Fig. 1.
A simple CRS involving ﬁve reactions (box vertices), r1, . . . , r5, and ten molecule
types (round vertices) namely, a food set F = {f1, . . . , f5} together with ﬁve other molecule types
p1, . . . , p5). Catalysation arcs are shown as dashed arrows. In this CRS, the subsets {r2, r3} and
{r1, r2, r3} are the two RAFS (the former is an irrRAF, the latter is the maxRAF). In this example,
each reaction has exactly two reactants, one product, and at most one catalyst, however a CRS can
have reactions with an arbitrary number of reactants, products and possible catalysts.
2


## Page 3


Deﬁnitions (RAFs, maxRAF).
Given a CRS Q = (X, R, C, F), a subset R′ of R is a said to be a RAF for Q if
R′ is nonempty and satisﬁes the following two conditions.
• Reﬂexively autocatalytic (RA): each reaction r ∈R′ is catalysed by at least
one molecule type that is either present in the food set or is generated by
another reaction in R′.
• Food-generated (F): for each reaction r ∈R′, each reactant of r is either
present in the food set F or can be generated by a sequence of reactions from
R′, each of which has each of its reactants present either in the food set or
as a product of an earlier reaction in the sequence.
In other words, a RAF is a subset of reactions that is both self-sustaining (from the
food set) and collectively autocatalytic. In forming a RAF from the food set, some
reactions may initially need to proceed uncatalysed (and thereby at a lower rate) but
once formed every reaction in the RAF will be catalysed. A simple example of a RAF
is the pair of reactions {r3, r4} shown in the CRS of Fig. 1. Note that in this example
either r3 or r4 must ﬁrst proceed uncatalysed, but once one reaction has occurred,
the system continues with both reactions catalysed.
The food-generated condition (F) can also be formalised as follows: For an arbi-
trary subset R′ of R let clR′(F) be the (unique) minimal subset W of X that contains
F and has the property that if r ∈R′ and all the reactants of r are in W then the
product(s) of r are also in W. The (F) condition now becomes the statement that each
reactant of each reaction in R′ is present in clR′(F). Note also that, assuming the
(F) condition holds, the (RA) condition becomes equivalent to the stronger condition
that each reaction r ∈R′ is catalysed by at least one molecule type that is present in
clR′(F).
Two fundamental combinatorial results concerning RAFs (from [6]) which will be
applied in this paper are the following:
• If Q has a RAF then it has a unique maximal RAF which contains all other
RAFs for Q (referred to as the maxRAF of Q, denoted maxRAF(Q)).
• Determining whether or not Q has a RAF, and if so constructing maxRAF(Q)
can be solved by an algorithm that is polynomial-time in the size of Q.
By contrast to the second point, ﬁnding a smallest RAF in a CRS Q has been
shown to be NP-hard [17]. The maxRAF of the CRS shown in Fig. 1 is {r1, r2, r3}.
Deﬁnitions: (subRAFs, irrRAFs, closure, closed RAFs, CAFs)
We now introduce some further notions related to diﬀerent types of RAFs.
The maxRAF of a CRS Q may contain one or more proper subsets of reactions
that are themselves RAFs for Q, in which case we call any such subset a subRAF of
the maxRAF.
A RAF R′ is said to be an irreducible RAF (irrRAF) if it contains no proper subset
of R′ that is a RAF. In other words, removing any single reaction from an irrRAF R′
gives a set of reactions that does not contain a RAF for Q. Constructing an irrRAF
for Q (or determining than none exists when Q has no RAFs) can also be carried
out in polynomial-time [6], however the number of irrRAFs can grow exponentially
with the size of the CRS [10]. To illustrate this notion, the RAF {r2, r3} is the only
irrRAF for the CRS in Fig. 1.
Given any subset R′ of reactions from R, the closure of R′ in Q, denoted R′ is
the (unique) minimal subset R′′ of R that contains R′ and satisﬁes the property that
if a reaction r from R has each of its reactants and at least one catalyst present in
the food set or as a product of a reaction from R′′ then r is in R′′. It is easily seen
3


## Page 4


that the closure of any RAF is always a RAF. We say that a RAF R′ is a closed RAF
if it is equal to its closure (i.e. R′ = R′). In particular, the maxRAF is always closed
(closed RAFs are the type of RAF that is most closely related to, but still diﬀerent
from, organisations in Chemical Organisation Theory [9]). Referring again to Fig. 1,
the closure of the RAF {r2, r3} is the maxRAF {r1, r2, r3}.
A minimal closed RAF for a CRS Q is a closed RAF R′ for Q that does not contain
any other closed RAF for Q as a strict subset. Any closed irrRAF is a minimal closed
RAF but a minimal closed RAF need not be an irrRAF. Once again Fig. 1 illustrates
this last concept: for this CRS, the minimal closed RAF is the maxRAF {r1, r2, r3}
but it is not an irrRAF since it contains the RAF {r2, r3}.
Given a CRS Q = (X, R, C, F), a stronger notion than a RAF is that of a con-
structively autocatalytic F-generated (CAF) set for Q (introduced in [15]). A CAF for
Q is a nonempty subset R′ of R for which the reactions in R′ can be ordered in such
a way that for each reaction r in R′, each reactant and at least one catalyst of r has
the property that it is either produced by an earlier reaction from R′ or is present in
the food set. In other words, a CAF is like a RAF with the extra requirement that no
spontaneous (uncatalysed) reactions are required for its formation (i.e. the catalyst
needs to be already present when it is ﬁrst needed). For example, both the RAFs in
Fig. 1 fail to be a CAF.
2. The structure of RAFs in ‘elementary’ catalytic reactions systems.
Let CRS Q = (X, R, C, F). We say that Q is elementary if it satisﬁes the following
condition:
• Each reaction r in R has all its reactants in F.
An elementary CRS is a very special type of CRS; however it has arisen both in
applications to real experimental chemical systems [1, 19] and in theoretical models
[11]. The CRS shown in Fig. 1 is not an elementary CRS, but it becomes so if reaction
r5 is removed. It is possible to extend the deﬁnition of elementary CRS to also allow
for reversible reactions, by requiring only one side of the reaction to contain molecule
types that are exclusively from F.
In this section, we show that elementary RAFs have suﬃcient structure to allow a
very concise classiﬁcation of their RAFs, closed subRAFs, irrRAFs, and ‘uninhibited’
closed RAFs (a notion described below), something which is problematic in general.
We then extend this analysis to more complicated types of RAFs in the next section.
Our analysis in this section relies heavily on some key notions from graph theory,
so we begin by recalling some concepts from that area.
2.1. Deﬁnitions. In this paper, all graphs will be ﬁnite. Given a directed graph
D = (V, A), recall that a strongly connected component of D is a maximal subset W
of V with the property that for any vertices u, v in W, there is a path from u to v
and a path from v to u.
It is a classical result that for any directed graph D = (V, A), the vertex set
V can be partitioned into strongly connected components. This, in turn, induces a
directed graph structure, called the condensation (digraph) of D, which we will denote
by D∗. In this directed graph, the vertex set is the collection of strongly connected
components of D and there is an arc (U, V ) in D∗if there is an arc (u, v) in D with
u ∈U and v ∈V . By deﬁnition, D∗is an acyclic directed graph. Moreover, the task
of partitioning V into strongly connected components and constructing the graph D∗
can both be carried out in polynomial time [18]. Note that the strongly connected
component containing v will consist just of v if v is not part of a cycle involving
another vertex.
4


## Page 5


We now introduce some further deﬁnitions. Given a directed graph D = (V, A):
• We say that a strongly connected component S of D is a core if either |S| > 1
or |S| = 1 (say S = {r}) and there is an arc from r to itself. Note that D has
a core if and only if D has a directed cycle.
• A chordless cycle in a directed graph D = (V, A) is a subset U of vertices of
D for which the induced graph D|U is a directed cycle (here D|U = (U, A′)
where the arc set A′ for D|U is given by A′ = {(u, v) ∈A : u, v ∈U}). Note
that if |U| = 1, this means that there is an arc from the vertex in U to itself.
• A vertex v in V is reachable from some subset S of V if there is a directed
path from some vertex in S to v. More generally, a subset U of V is reachable
from S if there is some vertex v ∈U that is reachable from S.
The terminology ‘core’ follows a similar usage by [20], in which the set of vertices
(molecule types) that are reachable from a core is referred to as the ‘periphery’ of the
core.
2.2. First main result. The following theorem provides graph-theoretic char-
acterisations of RAFs, irrRAFs, closed RAFs, and minimal closed RAFs within any
elementary CRS.
Given any CRS, Q, consider the directed graph DQ with vertex set R and with
an arc (r, r′) if a product of reaction r is a catalyst of reaction r′. In addition, for
any reaction r that has a catalyst in F, we add the arc (r, r) (i.e. a loop) into DQ if
this arc is not already present; this step is just a formal strategy to allow the results
to be stated more succinctly, and does not necessarily mean that a product of r is an
actual catalyst of r.
Theorem 1. Let Q be an elementary CRS. Then:
(i) Q has a RAF if and only if DQ has a directed cycle, and this holds if and
only if DQ contains a chordless directed cycle. The RAFs of Q correspond
to the subsets R′ of R for which the induced directed graph DQ|R′ has the
property that each vertex has in-degree at least 1.
(ii) The irrRAFs of Q are the chordless cycles in DQ. The closed irrRAFs of
Q are chordless cycles from which no other vertex of DQ is reachable. The
smallest RAFs of Q are the shortest directed cycles in DQ.
(iii) The closed RAFs of Q are the subsets of R obtained by taking the union of
any one or more cores of DQ and adding in all the reactions in R that are
reachable from this union.
(iv) Each minimal closed RAF of Q is obtained by taking any core C of DQ for
which no other core of DQ is reachable from C, and adding in all reactions
in R that are reachable from C.
(v) The number of minimal closed RAFs of Q is at most the number of cores in
DQ, and thus it is bounded above by |maxRAF(Q)|. These can all be found
and listed in polynomial time in |Q|.
(vi) The question of whether or not a given RAF for Q (e.g. the maxRAF) con-
tains a closed RAF as a strict subset can be solved in polynomial-time.
Proof.
A key observation throughout is that in an elementary CRS Q, any
nonempty subset R′ of reactions automatically satisﬁes the F–generated property,
so R′ forms a RAF for Q if and only if R′ satisﬁes the reﬂexively autocatalytic (RA)
property. By the manner in which DQ is constructed, the RA property means that
the induced subgraph DQ|R′ has the property that each vertex has in-degree at least
1.
5


## Page 6


In particular, R has a RAF if and only if DQ has a directed cycle.
The ‘if’
direction of this claim is clear. For the ‘only if’ direction, suppose that R′ is a RAF
and r ∈R′. By the assumption that each vertex in DQ has in-degree at least 1, there
is a directed walk of length k (for any k ≥1) involving vertices in R′ and ending in
r. Since R′ is ﬁnite if we take k > |R′| then two vertices on this directed walk must
coincide and the resulting sub-walk between this vertex to itself gives a directed cycle
in DQ. Moreover, DQ|R′ contains a directed cycle if and only if this sub-digraph
contains a chordless cycle (again, the ‘if’ direction is clear and the ‘only if’ direction
follows by the ﬁniteness of R, so shortening each directed cycle by following a chord
leads to a sequence of cycles of decreasing length that eventually terminates on a
chordless cycle). This establishes Part (i).
For Part (ii), a subset R′ of R has the property that DQ|R′ is a chordless cycle,
which implies (by Part (i)) that R′ is a RAF. It is also an irrRAF; otherwise, the cycle
would have a chord. Conversely, if R′ has the property that DQ|R′ is not a chordless
cycle, then either DQ does not contain a cycle (in which case it is not a RAF) or it
contains a cycle which either has a chord or has other vertices reachable from it, in
which case R′ is not an irrRAF. This establishes the ﬁrst sentence of Part (ii). The
arguments for the second and third sentences follow similar lines.
For Part (iii), it is clear that the union of one or more cores is a RAF; however,
the resulting set of reactions is closed if and only if all reactions that are reachable
from that set are also included.
For Part (iv), suppose that a core c′ is reachable from another core c (by deﬁnition,
c is not reachable from c′). Any closed RAF R′ that contains both c and c′ is thus
not minimal, since we could delete c′ and all the reactions that are reachable from
c′ but not from c and obtain a strict subset of R′ that is also a closed RAF. On the
other hand, if R′ has the property described in Part (iv), then it is a closed RAF by
Part (iii) and it is also minimal, since any closed RAF must contain at least one core,
alongside all the reactions that are reachable from it.
Part (v) follows from Part (iv), since each minimal closed RAF is associated with
exactly one core, and since cores are strongly connected components of DQ these cores
are vertex-disjoint (i.e. two cores share no reaction). Consequently, the number of
cores is bounded above by the number of reactions in the maxRAF of DQ. Moreover,
ﬁnding the strongly connected components of any digraph can be done in polynomial
time in the size of the digraph [18]. Each of these strongly connected components
can then be tested in polynomial time to determine if it is a core; if so, one can then
determine in polynomial time which other vertices are reachable from it. Thus the
minimal closed RAFs can be listed in polynomial time in the size of Q.
Part (vi) follows from Part (v) since Q contains a closed subRAF if and only if it
contains a minimal closed subRAF.
2
Figs. 2, 3 and 4 illustrate Parts (i)–(iv) of Theorem 1. Some of these examples
are based on reaction networks that come from actual experimental RAF sets.
6


## Page 7


r2
r6
r1
r3
r9
r5
r7
r8
r4
S1
S3
S2
S1
S2
S3
DQ
D∗
Q
Fig. 2. The directed graph DQ for an elementary CRS Q (adapted from an experimental system
of [1]) that has three strongly connected components (S1, S2, S3), of which S1 and S2 are cores. The
associated (acyclic) condensation digraph D∗
Q is shown on the right. The unique minimal closed
RAF is S2 ∪S3; the other closed RAF is the full set itself, namely S1 ∪S2 ∪S3. The reactions
subsets S1, S1 ∪S3, S1 ∪S2, S1 ∪S3, and S2 are all RAFs but not closed RAFs. A computer-based
search ﬁnds 305 RAFs altogether. There are six chordless cycles in this CRS, which correspond to
the six irrRAFs: {r2}, {r5}, {r8}, {r1, r4}, {r4, r7} and {r3, r7}. Note that this representation of the
CRS is in terms of the molecules produced by reactions that have reactants in the food set. However,
each reaction produces a single (and unique) product so we can identify the product with the reaction
in this example.
a1
b1
c1
a0
1
b0
1
a0
3
b0
3 b0
2
a0
2
a2
b2
b3
a3
c3
r1
r0
1
r0
3
r3
r2
r0
2
r1
r2
r3
r0
1
r0
2
r0
3
(i)
(ii)
c2
Fig. 3. (i) An elementary CRS (with food set F equal to the 12 elements labelled ai, a′
i, bi, b′
i
for i = 1, 2, 3) that has eight irrRAFs, each of which has size 3 (this example can be extended to
produce an elementary CRS with 2n reactions and 2n irrRAFs [10]). These irrRAFs correspond to
the eight chordless cycles in the graph DQ shown in (ii), with one of these chordless cycles indicated
by the three bold arcs. None of these irrRAFs is closed. There are 27 RAFs for Q in total.
Remarks:
• Parts (ii)–(vi) of Theorem 1 hold even when Q is not elementary, provided
that Q′ = (X, R′, C, F) is elementary where R′ is the maxRAF of Q.
• Although cores share no reactions in common, it is quite possible for minimal
closed RAFs to share reactions in common.
• The last sentence of Part (ii) implies that the size of the smallest RAF is equal
7


## Page 8


r2
r4
r5
r6
r7
r3
r1
S2
S3
S4
S1
S1
S2
S3
S4
DQ
D∗
Q
Fig. 4.
The directed graph DQ for an elementary CRS (from an experimental system [7]),
shown on the left, has 67 RAFs and two closed RAFs (the whole set and {r4, r5, r6, r7}).
The
strongly connected components of DQ are {r1}, {r2}, {r3} and {r4, r5, r6, r7}, two of which are cores
(namely, {r1} and {r4, r5, r6, r7}). The associated condensation digraph D∗
Q is shown on the right.
For this RAF, there are four irrRAFs, namely {r1}, {r5}, {r6}, and {r4, r7}.
to the length of the shortest directed cycle in DQ and this can be found in
polynomial time in |Q| (by a depth-ﬁrst-search or network ﬂow techniques).
This is in contrast to the problem of ﬁnding the size of a smallest RAF in a
general CRS, which has been shown to be NP-hard in [17].
• An important extension of the RAF concept allows for molecule types to
inhibit reactions (as well as being able to catalyse reactions). For a general
CRS Q it is known that determining whether or not a CRS Q has a RAF R′
for which no reaction is inhibited by any molecule produced by R′ is NP-hard
[15]. However, for any elementary CRS, Theorem 1(v) provides the following
positive result.
Corollary 1. When inhibition is also allowed in an elementary CRS Q, it
is possible to determine in polynomial time whether Q contains a closed RAF
R′ for which no reaction is inhibited by any molecule type produced by R′.
Proof. There is a closed RAF for Q that has no inhibition if and only if
there is a minimal closed RAF for Q that has no inhibition. By Part (v)
of Theorem 1, there are at most |maxRAF(Q)| minimal closed RAFs for
an elementary CRS Q, and these can all be checked in polynomial time to
determine if any of them have the property that no reaction is inhibited by
any molecule type produced by the reactions in the set.
• Part (v) of Theorem 1 raises the question of whether this result might apply
with the restriction that Q is elementary. In other words, is the number of
minimal closed RAFs in a (general, nonelementary) CRS bounded polyno-
mially in the size of Q? The answer turns out to be ‘no’ as the following
example shows.
Consider the CRS Qk := (X, R, C, F) where
X = {f, x, θ} ∪{x1, x′
1, . . . , xk, x′
k} ∪{θ1, . . . , θk}, F = {f},
and for [k] = {1, 2, . . . , k}, the reaction set is:
R = {rx, rθ} ∪{ri : i ∈[k]} ∪{r′
i, i ∈[k]} ∪{ri : i ∈[k]} ∪{r′
i : i ∈[k]},
where these reactions are described as follows (with catalysts indicated above
8


## Page 9


the arrows):
rx : f
θ−→x,
rθ : θ1 + θ2 + · · · + θk
θ−→θ,
and for all i ∈[k]:
ri : x
xi
−→xi, r′
i : x
x′
i
−→x′
i,
ri : xi
θi
−→θi, r′
i : x′
i
θi
−→θi.
Thus, Qk has a food set of size 1, a reaction set of size 4k + 2, and 3k + 3
molecule types. Fig. 5 provides a graphical representation of Q3.
x
f
x′
1
x1
x2
x′
2
x3
x′
3
θ1
θ2
θ3
θ
rx
r1
r1
r2
r2
r3
r3
r′
1
r′
1
r′
2
r′
2
r3′
r′
3
rθ
Fig. 5. The CRS Q3.
Proposition 1. The minimal closed RAFs of Qk coincide with the irrRAFs
for Qk, and there are 2k of them. More precisely, R′ is a minimal closed
RAF of Qk if and only if R′ contains rx and rθ and for each i ∈[k], R′
contains either (i) ri and ri but neither r′
i nor r′
i, or (ii) r′
i and r′
i but neither
ri nor ri.
Proof. The ‘if’ direction in the second sentence is clear, since any such R′
is easily seen to be a closed subRAF, as well as being an irrRAF, and thus
is a minimal closed RAF. For the ‘only if’ direction, a subset R′ of R is a
RAF of Qk precisely if the following two properties hold: (a) R′ contains
rx and rθ, and (b) for each i, R′ contains either ri and ri or r′
i and r′
i (in
order to generate θi, which is required by rθ). Unless R′ satisﬁes the stronger
condition (i) or (ii) (for each i ∈[k]) listed in the statement of Proposition 1,
R′ is not minimal.
Another question that Part (v) of Theorem 1 suggests is the following: does an
elementary CRS always have at most a polynomial number of closed RAFs? Again,
the answer is ‘no’, and the construction to show this is much simpler than the previous
example. Consider the elementary CRS with F = {f1, . . . , fn}, X = F ∪{x1, . . . , xn},
together with the set R of k catalysed reactions ri : fi
xi
−→xi for i = 1, . . . , k. This
CRS has 2k −1 closed RAFs, one for each nonempty subset of R.
2.3. The probability of a RAF in an elementary CRS. Given an elemen-
tary CRS Q, suppose that catalysis is assigned randomly as follows: each molecule
type catalyses each given reaction in R with a ﬁxed probability p, independently
9


## Page 10


across all pairs (x, r) of molecule type x and reaction r. The probability pQ that Q
has a RAF is simply the probability that DQ has a directed cycle (by Theorem 1(i)).
In the case where each reaction in R has just a single product, then the asymptotic
behaviour of pQ as |R| →∞is equivalent to the emergence of a directed cycle in a
large random directed graph, which has been previously studied in the random graph
literature by [2].
Here we provide a simple lower bound on pQ. Let λ = p|R| be the expected
number of reactions that each molecule type catalyses. The following result gives a
lower bound on pQ that depends only on λ and which converges towards 1 as λ grows.
Proposition 2. pQ ≥1 −

1 −
λ
|R|
|R|
∼1 −e−λ, where ∼denotes asymptotic
equality as |R| grows.
Proof. Consider the probability pr that a single reaction r has an arc to itself
(such an event is suﬃcient but not necessary for DQ to contain a directed cycle).
If r produces m ≥1 products, we have pr = 1 −(1 −p)m ≥pm ≥p = λ/|R|.
The probability that no reaction has an arc to itself is therefore

1 −
λ
|R|
|R|
. Since
(1 −x/n)n ∼e−x, we obtain the result claimed.
2.4. Eigenvector analysis. A previous study by [11] considered the dynamical
aspects of an ‘autocatalytic set’ in a CRS, which is closely related to the notion of
an RAF (our graph DQ diﬀers from theirs in two respects, ﬁrstly the vertices here
represent reactions rather than molecule types, and we also permit self-loops from a
reaction to itself). We now present the analogues of these earlier dynamical ﬁndings
in our setting (and formally, with proofs).
Given an elementary CRS Q, let AQ denote the adjacency matrix of the directed
graph DQ. Thus the rows and columns of AQ are indexed by the reactions in R in some
given order, and the entry of AQ corresponding to the pair (r, r′) is 1 precisely if (r, r′)
is an arc of DQ and is zero otherwise. By Perron-Frobenius theory for non-negative
matrices, AQ has a non-negative real eigenvalue λ of maximal modulus (amongst all
the eigenvalues) and if DQ is strongly-connected (i.e. AQ is irreducible), then AQ has
a left (and a right) eigenvector with eigenvalue λ whose components are all positive.
The following results are analogues of the former study by [11] to our setting.
Proposition 3.
(i) If Q contains no RAF, then λ = 0.
(ii) If Q contains a RAF, then λ ≥1.
(iii) If AQ has an eigenvalue > 0 with an associated left eigenvector w, then the
set of reactions r for which wr > 0 forms a RAF for Q.
Proof. Part (i) follows from Part (i) of Theorem 1, combined with the fact that
the adjacency matrix A of an acyclic directed graph is nilpotent (i.e. speciﬁcally, Al+1
is the all-zero matrix when l is the length of a longest path in the directed graph) and
thus all the eigenvalues of A are equal to zero [3]. For Part (ii), if Q contains a RAF,
then DQ has a minimal (chordless) directed cycle (which could just be a loop on a
vertex). Let w be the vector that has value 1 for each vertex in this minimal directed
cycle and is zero otherwise. Then w is both a left and right eigenvector for AQ with
eigenvalue 1. For Part (iii), let R′ = {r ∈R : wr > 0}. The condition wAQ = λw
translates as P
r∈R wrArr′ = λwr′. Since the right-hand side is non-zero for each
reaction r′ ∈R′, it follows that wrArr′ ̸= 0 for at least one reaction r ∈R′; In other
words, each reaction is R′ is catalysed by the product of at least one reaction in R′.
10


## Page 11


Since Q is elementary, this implies that R′ is a RAF.
To illustrate an application of Proposition 3, consider the system of 9 reactions
from Fig. 2. In this case, λ ≥1 since the system contains a RAF (cf. Proposition 3(ii)).
Regarding Part (iii), three of the eigenvalues of AQ are strictly positive, and for
the three corresponding left eigenvectors, one has strictly positive entries for the
three reactions r2, r6, r8, which form the subRAF S1 shown in Fig. 2. A second left
eigenvector has strictly positive entries for the reactions r1, r3, r4, r5, r7, r9, and these
form the minimal closed subRAF S2 ∪S3 shown in Fig. 2. The third left eigenvector
has strictly positive entries for the reactions r1, r4, r7 which forms a subRAF of S2.
We end this section by noting that Part (iii) of Proposition 3 does not hold if
left eigenvectors are substituted for right ones. A counterexample is given by the
elementary CRS for which AQ is the 2 × 2 matrix with both rows equal to [0, 1]; in
this case, AQ has a principal eigenvalue of +1 but the associated right eigenvector is
a column vector with strictly positive entries, but this does not correspond to a RAF
for Q.
3. Generative RAFs. We now introduce a new notion which describes how
simple RAFs can develop into more complex ones in a progressive way. This sec-
tion will build on, and apply the results concerning elementary CRSs, particularly
Theorem 1.
Given a CRS Q = (X, R, C, F) and a subset Y of X containing F, let R|Y be
the subset of reactions in R that have all their reactants in Y , and let
Q|Y := (X, R|Y, C, Y ).
In other words, Q|Y is the CRS obtained from Q by deleting each reaction from R
that does not have all its reactants in Y , and by expanding the food set to include all
of Y .
Deﬁnition (genRAFs): Given a CRS Q = (X, R, C, F), we say that a RAF
R′ for Q is a genRAF (or generative RAF) if there is a sequence R1, R2, . . . , Rk of
subsets of R with Rk = R′ and that satisfy the following properties:
(i) R1 is the closure in Q of a RAF of Q|F;
(ii) for each i > 1, Ri is the closure in Q of a RAF of Q|Yi where Yi = F ∪π(Ri−1),
and where π(Ri−1) refers to all molecule types that are produced by a reaction
from Ri−1.
Thus, a genRAF is any RAF for Q that can be formed by taking R1 to be the
closure (within Q) of a RAF within the elementary CRS Q|F, and for each i > 1,
adding the products of Ri−1 to the food set F of Q and taking Ri to be the closure
(within Q) of the the resulting (induced) elementary CRS. In other words, the next
closed RAF in the sequence is built upon an enlarged food set generated by the
previous closed RAFs in the sequence and considering just those reactions that use
this enlarged food set as reactants, and then forming the closure of this set in Q.
As an example, the CRS in Fig. 6(a) is itself a genRAF (but not a CAF), as it has
the generating sequence R1, R2 where R1 = {r1, r2, } and R2 = {r1, r2, r3}, however
the CRS in Fig. 6(b) is not a genRAF (even though it is an RAF).
The motivation for considering the notion of genRAFs is two-fold.
Firstly a
genRAF can be built up from simpler RAFs (starting with an elementary one) by
generating the required catalysts at each step (i.e.
some reactions may still need
to proceed initially uncatalysed, but a catalyst for the reaction will be generated
11


## Page 12


f1
f2
f3
(a)
f1
f2
f3
(b)
r2
r1
r3
Fig. 6. (a): This CRS that is a genRAF (a generating sequence starts with the elementary
closed RAF {r1, r2}, and then adds r3).
(b): A diﬀerent pattern of catalysis converts the three
reactions into a RAF that is no longer a genRAF. In both cases, the food set is F = {f1, f2, f3}.
by some other reaction by the end of the same step).
This avoids the possibility
of long chains of reactions that need to proceed uncatalysed until a catalyst for the
very ﬁrst link in the chain is produced, which seems less biochemically plausible. A
second motivation for considering genRAFs is that they combine two further desirable
properties: namely an emphasis on RAFs that are closed (i.e. all reactions that are
able to proceed and for which a catalyst is available will proceed), and genRAFs are
suﬃciently well-structured that some questions can be answered in polynomial time
that are problematic for general RAFs (Theorem 2(iv) provides an explicit example).
We will call the sequence R1, R2, . . . , Rk in the above deﬁnition a generating
sequence for R′. We now make two observations, that are formalized in the following
lemma.
Lemma 3.1. Suppose that a genRAF R′ has generating sequence R1, R2, . . . , Rk.
Then:
(i) R′ and each set in its generating sequence is a closed RAF for Q.
(ii) Ri is a nested increasing sequence (i.e. Ri ⊆Ri+1 for each i ∈{1, . . . , k−1}).
Proof. Part (i) follows by deﬁnition, since each set in the generating sequence is
the closure of a subRAF of Q and is therefore a closed RAF for Q, and a genRAF is
the ﬁnal set in its generating sequence.
Part (ii): For each reaction r ∈R, let ρ(r) denote the set of reactants of r. We
prove Part(ii) by induction on k. For k = 2, suppose that r ∈R1. Then ρ(r) ⊆F and
there exists some molecule type x ∈F ∪π(R1) that catalyses r. Since R2 is a closed
RAF, and since the reactants and at least one catalyst (namely x) are available in the
enlarged food set for R2, namely Y2 = F ∪π(R1), then r ∈R2. Thus Part (ii) holds
for k = 2. Suppose now that Part (ii) holds for k = m and that R1, R2, . . . , Rm+1 is a
generating sequence for Q. We need to show that Rm ⊆Rm+1. To this end, suppose
that r ∈Rm. Then ρ(r) ⊆π(Rm−1) and there exists a molecule type x ∈F ∪π(Rm)
that catalyses r. Now Rm−1 ⊆Rm by induction and so ρ(r) ⊆π(Rm). Thus the
reactants and at least one catalyst of r are in Ym+1 = F ∪π(Rm), and so, by the
closure property, r ∈Rm+1. This establishes the induction step, and thereby Part
(ii).
A natural question in the light of Lemma 3.1(i) is the following: Is every closed
12


## Page 13


RAF in a CRS generative? The answer to this is ‘no’ in general; for example, a CRS
may have a maxRAF that requires too much ‘jumping ahead’ with catalysis (chains
of initially spontaneous reactions) to be built up in this way, as in Fig. 6(b). Shortly
(Theorem 2) we will provide a precise, and eﬃciently checkable, characterisation for
when a closed RAF is a genRAF.
Another instructive example is the following maxRAF that arose in a study of
the binary polymer model from [8]:
r1 : 10 + 0
01100
−−−→100
r2 : 01 + 100
0−→01100
r3 : 10 + 1
0−→101
r4 : 11 + 10
101
−−→1110
r5 : 1110 + 0
101
−−→11100
where F = {0, 1, 00, 01, 10, 11}. This maxRAF contains six subRAFs, two of which
are closed, namely, the full set of all ﬁve reactions, which is not generative, and the
subset {r3, r4, r5}, which is a genRAF.
A maximal generative RAF: Given a CRS Q = (X, R, C, F), consider the
following sequence (Ri, i ≥1) of subsets of R. Let Q1 := Q|F, let Ri = maxRAF(Q1)
and let R1 be the closure of R1 in Q. For i > 1, let
Ri = maxRAF(Qi), where Qi := F ∪π(Ri−1),
and let Ri be the closure of Ri in Q.
Note that R1 may be empty even if Q has a RAF (as Fig. 6(b) shows), in which
case, Ri = ∅for all i ≥1. However, if R1 is nonempty, then Ri forms an increasing
nested sequence of closed RAFs for Q and so the sequence stabilises at some subset
of reactions that we denote by R(Q). Thus, R(Q) = ∪i≥1Ri, and this set is identical
to Rk for some suﬃciently large value of k (with k ≤|R|).
We can now state the main result of this section.
Theorem 2. Suppose that Q = (X, R, C, F) is a CRS.
(i) Q contains a genRAF if and only if R1 ̸= ∅, in which case R(Q) is a genRAF
for Q that contains all other genRAFs for Q.
(ii) If R′ is a closed RAF for Q then R′ is a genRAF for Q if and only if
R′ = R(Q′), where Q′ = (X, R′, C, F).
(iii) The construction of R(Q) and determining whether an arbitrary closed RAF
R′ for Q is generative can be determined in polynomial time in |Q|.
(iv) Determining whether a given closed genRAF R′ contains a strict subset that
is a closed RAF for Q can be solved in polynomial time in |Q|.
Proof. For the ﬁrst claim in Part (i), if R1 = ∅then Q|F contains no RAF and
so Q has no genRAF. Suppose that R1 ̸= ∅. Then R(Q) is a genRAF for Q since
it has the generating sequence Ri (i ≥1) (noting that Ri is the closure in Q of Ri
which is the maxRAF (and so a RAF) for Q|F when i = 1, and for Q|(F ∪π(Ri−1),
when i > 1). For the second claim in Part (i), suppose that R′ is a genRAF for Q;
will show that R′ ⊆R(Q). Let (R′
i, i ≥1) be a generating sequence for R′. We show
by induction on i that R′
i ⊆Ri for all i > 1. The base case i = 1 holds since R1 is
the maxRAF of Q|F which contains any other RAF of Q|F, and so the closure of R1
13


## Page 14


in Q, namely R1 contains the closure in Q of any other RAF of Q|F. Suppose the
induction hypothesis holds for all values of i up to j ≥1. Then Rj+1 is the maxRAF
of Q|(F ∪π(Rj)) and so it contains any RAF of Q|(F ∪π(R′
j)) since R′
j ⊆Rj (by
the induction hypothesis) and so F ∪π(R′
j) ⊆F ∪π(Rj). Consequently, the closure
of Rj+1 in Q, namely, Rj+1, contains the closure in Q of any RAF of Q|(F ∪π(R′
j)).
Thus the induction hypothesis holds, which establishes that R′ ⊆R(Q).
For Part (ii), observe that R(Q′) is a genRAF for Q′ (by Part (i)) and so if
R′ = R(Q′) then R′ is a genRAF for Q′. Since R′ is a closed RAF for Q, R′ is also
a genRAF for Q (since the closure in Q of any subset of reactions from R′ is a subset
of R′). Conversely, suppose that R′ is a genRAF for Q. Then since R′ is a closed
RAF for Q, R′ is also a genRAF for Q′. Now, R(Q′) ⊆R′, and since R(Q′) contains
any other genRAF for Q′ (in particular, R′) by Part (i), we have R(Q′) = R′, as
required.
For Part (iii), the proof of the claim (regarding the construction of R(Q)) follows
from the fact that the maxRAF (of Qi), and its closure (in Q) can be computed in
polynomial time in the size of the CRS [6]. The the second claim then follows from
Part (ii).
For Part (iv), consider the following algorithm. Given a closed RAF R′ for Q,
let R
′
1, R
′
2, . . . be the generating sequence for R(Q′) (described above, but with R
replaced by R′ and Q by Q′ = (X, R′, C, F)). From Part (ii) we have R(Q′) = R′,
and so R
′
1, R
′
2, . . . is a generating sequence for R′.
Now, let Q′
1 = Q′|F and for i > 1, let Q′
i = Q|(F ∪π(R
′
i−1)). Notice that Q′
1 is an
elementary CRS, and for i > 1 we can regard Q′
i as an elementary RAF with enlarged
food set F ∪π(R
′
i−1). Thus we can apply Part (v) of Theorem 1, and in polynomial
time in |Q| search all the minimal closed RAFs for Qj and determine whether the
closure in Q of any of these results in a strict subset (say R′′) of R′. When such a
set R′′ exists, its closure is clearly a closed RAF for Q that is a strict subset of R′.
However, if no such set R′′ is located then we claim that R′ contains no closed RAF
for Q as a strict subset. To see why, suppose that there is a closed RAF for Q that
is strictly contained within R′. In that case there exists a minimal closed RAF for Q
that is strictly contained in R′, and we denote such a minimal closed RAF as R∗. Let
j be the smallest value of i for which R∗is contained in R
′
i as a strict subset (this is
well deﬁned, since R∗is strictly contained in R′). Then R∗is a closed RAF for Qj
also, and its closure in Q is a strict subset of R′, so the closure in Q of any minimal
closed RAF for Qj that lies strictly within R∗would also be a strict subset of R′.
2
Remarks:
• If a CRS has a CAF (deﬁned at the end of the Introduction), then the (unique)
maximal CAF is generative. However, a genRAF need not necessarily corre-
spond to a maximal CAF.
• Part (iv) of Theorem 2 provides an interesting contrast to the general RAF
setting. There the question of determining whether a closed RAF (e.g. the
maxRAF) in an arbitrary CRS contains another closed RAF as a strict subset
has unknown complexity.
4. RAFs with reaction rates. In this section, we consider a further reﬁnement
of RAF theory, by explicitly incorporating reaction rates into the analysis. This conve-
niently addresses one shortcoming implicit in the generative RAF deﬁnition from the
14


## Page 15


last section – namely a generative RAF necessarily grows as a monotonically increas-
ing nested system with the length of its associative generating sequence (Lemma 3.1).
However, once a suﬃciently large generative RAF is established, one or more of its
subRAFs may then become dynamically favoured if it is more ‘eﬃcient’ (i.e. all its
reactions proceed at higher reaction rates than the generative RAF it lies within), as
we shortly illustrate with a simple example.
Suppose that we have a CRS Q = (X, R, C, F) and a function f : C →R≥0 that
assigns a non-negative real number to each pair (x, r) ∈C. The interpretation here
is that f(x, r) describes the rate at which reaction r proceeds when the catalyst x is
present.
Given Q and f, together with a RAF R′ for Q, let:
ϕ(R′) = min
r∈R′{max{f(x, r) : (x, r) ∈C, x ∈clR′(F)}}
In other words, ϕ(R′) is the rate of the slowest reaction in the RAF R′ under the
most optimal choice of catalyst for each reaction in R′ amongst those catalysts that
are present in clR′(F).
r3
r2
r1
f2
f1
f3
f4
1
1
2
2
(a)
(b)
fr1; r2; r3g
fr1; r2g
fr2; r3g
fr1g
Fig. 7.
(a) A RAF in which the catalysis arcs have associated rates (namely, the values 1
and 2 as indicated). The poset consisting of the maxRAF and its three subRAFs (partially ordered
by set inclusion) is shown by the Hasse diagram in (b). All four RAFs have ϕ–values of 1 except
for the subRAF {r2, r3}, which has a ϕ–value of 2. This optimal RAF {r2, r3} is not a generative
RAF (whereas the other three RAFs are generative; indeed, {r1} and {r1, r2} are elementary).
Nevertheless, once the generative maxRAF {r1, r2, r3} has formed, {r2, r3} can then emerge as the
dominant sub-RAF.
Example: Fig. 7 provides an example to illustrate the notions above. In this
CRS the three reactions comprises a RAF, with a ϕ–value equal to 1. However there
are three subRAFs, and one of these (namely {r2, r3}) has a higher ϕ–value. However,
the less optimal closed subRAF {r1, r2} is generative and likely to have formed before
the optimal one; otherwise {r2, r3} would require a chain of two reactions to occur
uncatalysed (r2 followed by r3) before the catalysts for them become available. The
closed RAF {r1, r2} may then expand to {r1, r2, r3} before this second closed RAF is
subsequently out-competed by its subRAF {r2, r3}, since the catalysed reactions in
this subRAF run twice as fast as the reaction r1.
Our main result in this section shows that ﬁnding a RAF to maximise ϕ can be
achieved by an algorithm that runs in polynomial time in the size of Q.
15


## Page 16


Theorem 3.
There is a polynomial-time algorithm to construct a RAF with
largest possible ϕ–value from any CRS Q that contains RAF. Moreover, this con-
structed RAF is the maximal RAF with this ϕ–value.
Proof. Let L = {f(x, r) : (x, r) ∈C}, and let M = max L. Consider the CRS
Q′ = (X′, R∗, C∗, F) obtained from Q by ﬁrst deleting any uncatalysed reaction and
then replacing each reaction r that is catalysed by (say) k ≥1 molecule types with
k distinct copies of this reaction r1, . . . , rk, each of which is catalysed by a diﬀerent
one of the k molecule types.
Thus each reaction r in R∗is catalysed by exactly
one molecule type, which we will denote as x(r). For the associated catalysis set
C∗= {(x(r), r) : r ∈R∗}, let f ′ be the rate function induced by f (i.e. if r ∈R is
replaced by r1, . . . , rk ∈R∗then f ′(x(ri), ri) := f(x(r), r)). For each ℓ∈L let:
R∗
ℓ= {r ∈R∗: f ′(x(r), r) ≥ℓ}.
In other words, R∗
ℓis the set of catalyst-reaction pairs (x(r), r) where the rate of
reaction r when catalysed by the molecule type x(r) is at least ℓ(as speciﬁed by the
rate function f).
Now, let eR be the maxRAF of R∗
ℓfor the largest value of ℓ∈L for which
maxRAF(R∗
ℓ) is nonempty. This set is well-deﬁned, since R∗= R∗
ℓwhen ℓ= 0,
and because R (and thereby R∗) is assumed to have a RAF. Notice that eR can
be eﬃciently determined, by starting at ℓ= M and decreasing ℓthrough the (at
most |L| ≤|C|) possible values it can take until a nonempty maxRAF ﬁrst appears
(alternatively, one could start at ℓ= 0 and increase ℓuntil the last value for which a
nonempty maxRAF is present).
Claim: eR is a RAF that has the largest possible ϕ–value of any RAF for Q′, and
eR contains any other RAF for Q′ with this maximal ϕ–value.
To establish this claim, suppose that eR = maxRAF(Rℓ) for ℓ= t and that
maxRAF(Rℓ) = ∅for ℓ> t (i.e. t is the largest value of ℓin L for which Rℓhas a
(nonempty) maxRAF). For each reaction r in eR, we then have f ′(x(r), r) ≥t, and
for at least one reaction r in eR, f ′(x(r), r) = t (otherwise, a larger value of ℓwould
support a maxRAF). It follows that ϕ( eR) = t. Now if R′ is any other RAF for Q′,
let t′ be the minimal value of f ′(x(r), r) over all choices of r ∈R′. Then t′ ≤t
otherwise, Rℓwould have a nonempty maxRAF for a value ℓ= t′ that is greater than
t, contradicting the maximality of t. Thus R′ ⊆R∗
t and so
R′ = maxRAF(R′) ⊆maxRAF(R∗
t ) = eR,
which shows that eR contains any other RAF with this maximal value.
This establishes the above Claim, and thereby Theorem 3 for Q′. However, the
subset of reactions of R whose copies are present in eR provides a RAF for Q that
has the largest possible ϕ–value (namely t) and which contains any other RAF for Q
with this ϕ–value.
2
Remark: For the example in Fig. 7, we have the subRAFs R1 = {r1}, R2 =
{r2, r3} with ϕ(R1) < ϕ(R2). In this case, there is a path in the poset from R1 to
R2 on which ϕ is non-decreasing (this path goes ‘up’ then ‘down’ in Fig. 7(b)). An
interesting question might be to determine when this holds: in other words, from a
sub-optimal RAF, can a more optimal RAF be reached by a chain of RAFs that, at
each stage, either adds certain reactions or deletes one or more reactions, and so that
the optimality score (as measured by ϕ) does not decrease?
16


## Page 17


4.1. Rates for ‘catalytic ensembles’. We can extend the results on rates in
the previous section to accommodate the following feature: a reaction for which a
combination of two or more catalysts is present may proceed at a rate that is higher
than if just one catalyst is present.
We formalize this as follows. Recall that in a CRS Q = (X, R, C, F), the set C
represents the pattern of catalysis and is a subset of X × R. Thus (x, r) ∈C means
that x catalyses reaction r. Now suppose we wish to allow a combination (ensemble)
of one or more molecules to act as a catalyst for a reaction. In this case, we can
represent the CRS as a quadruple Q = (X, R, C, F) where C ⊆(2X −∅) × R and
where (A, r) ∈C means that the ensemble of molecules in A acts as a (collective)
catalyst for r, provided they are all present. We refer to Q as a generalised CRS. The
notions of RAF, subRAF, CAF, and so on, can be generalized naturally. For example,
the RA condition for a subset R′ is that for each reaction r, there is a pair (A, r) ∈C
where each of the molecule types in A is in the closure of F relative to R′.
Note that an ordinary CRS can be viewed as a special case of a generalised CRS
by identifying (x, r) with the pair ({x}, r). Note also that each reaction may have
several ensembles of possible catalysts, and some (or all of these) may be just single
molecule types.
Given a generalised CRS Q = (X, R, C, F) we can associate an ordinary CRS
Q′ = (X′, R′, C′, F) to Q as follows. Let
AC := {A ⊆2X −∅: ∃r ∈R : (A, r) ∈C};
(so AC is the collection of catalyst ensembles in Q). For each A ∈AC, let xA be a
new molecule type, and let rA be the (formal) reaction A →xA. Now let
X′ :=X ˙∪{xA : A ∈AC};
R′ :=R ˙∪{rA : A ∈AC}; and
C′ :={(xA, r) : (A, r) ∈C} ˙∪{(xA, rA) : A ∈AC}.
Note that C′ ⊆X′ × R′.
In other words, Q′ is obtained from Q by replacing each catalytic ensemble A by
a new molecule type xA and adding in the reaction rA : A →xA catalysed by xA.
The proof of the following lemma is straightforward.
Lemma 4.1. A generalised CRS Q has a RAF if and only if the associated ordi-
nary CRS Q′ has a RAF that contains at least one reaction from R. Moreover, in
this case, the RAFs of Q correspond to the nonempty intersections of RAFs of Q′
with R.
Now suppose that we have a generalised CRS Q = (X, R, C, F) and a function
f : C →R≥0. The interpretation here is that f(A, r) describes the rate at which
reaction r proceeds when the catalyst ensemble A is present.
Given a RAF R′ for Q, let:
ϕ(R′) := min
r∈R′{max{f(A, r) : (A, r) ∈C, A ⊆clR′(F)}}
In other words, ϕ(R′) is the rate of the slowest reaction in the RAF R′ under the
most optimal choice of catalyst ensemble for each reaction in R′ amongst catalyst
ensembles that are subsets of clR′(F).
Lemma 4.1 now provides the following corollary of Theorem 3.
17


## Page 18


Corollary 2. There is a polynomial-time algorithm to construct a RAF for Q
with largest possible ϕ–value from any CRS Q that contains a RAF. Moreover, this
constructed RAF is the maximal RAF for Q with this ϕ–value.
5. Concluding comments. In this paper, we have considered special types
of RAFs that allow for exact yet tractable mathematical and algorithmic analysis,
and which also incorporate additional biochemical realism (restricting the depth of
uncatalysed reactions chains in generative RAFs and allowing reaction rates).
We ﬁrst considered the special setting of ‘elementary’ systems in which all re-
actions (or at least those present in the maxRAF) have all their reactants present
in the food set. This allows for the structure of the collection of RAFs, irrRAFs,
and closed subRAFs to be explicitly described graph-theoretically. As a result, some
problems that are computationally intractable in the general CRS setting turn out to
be polynomial-time for an elementary CRS. For example, one can eﬃciently ﬁnd the
smallest RAFs in an elementary CRS, which is an NP-hard problem in general [17].
Also, the number of minimal closed subRAF in an elementary CRS is linear in the
size of the set of reactions (for a general CRS, they can be exponential in number).
For future work, it may be of interest to determine if there are polynomial-time al-
gorithms that can answer the following questions for an elementary CRS: (i) What is
the size of the largest irrRAF? (ii) If inhibition is allowed, then is there a RAF that
has no inhibition?
The concept of an ‘elementary’ CRS is an all-or-nothing notion.
One way to
extend the results above could be to deﬁne the notion of ‘level’, whereby a CRS has
level k if the length of the longest path from the food set to any reaction product
goes through at most k reactions (an elementary CRS thus has level 1). We have not
explored this further here but instead, we consider the related alternative notion of a
generative RAF. Brieﬂy, a generative RAF allows a RAF to form by eﬀectively enlarg-
ing its ‘food set’ with products of reactions, so that each step only requires catalysts
that are either present or produced by reactions in the RAF at that stage. Although
generative RAFs are more complex than elementary ones, their close connection to
elementary RAFs (in a stratiﬁed way) allows for a more tractable analysis than for
general RAFs. Moreover, unlike elementary RAFs, no special assumption is required
on the underlying CRS; generative RAFs are just a special type of RAF that can be
generated in a certain sequential fashion in any CRS.
In the ﬁnal section, we considered the impact of rates of RAFs (which need
not be generative), and particularly the algorithmic question of ﬁnding a RAF that
maximises the rates of its slowest reaction. Not only is this problem solvable in the
size of the CRS, but it can also be extended to the slightly more general setting of
allowing ‘catalytic ensembles’. The introduction of rates allows for the study of how
a population of diﬀerent closed subRAFs might evolve over time, in which primitive
subRAF are replaced (out-competed) by eﬃcient ones that rely on new catalysts in
place of more primitive ones. We hope to explore this further in future work.
Acknowledgments. WH thanks the Institute for Advanced Study, Amsterdam,
for ﬁnancial support in the form of a fellowship.
REFERENCES
[1] G. Ashkenasy, R. Jegasia, M. Yadav, and M. R. Ghadiri, Design of a directed molecular
network, Proc. Natl. Acad. Sci. USA, 101 (2004), pp. 10872–10877.
18


## Page 19


[2] B. Bollobas and S. Rasmussen, First cycles in random directed graph processes, Discrete
Math., 75 (1989), pp. 55–68.
[3] D. M. Cvetkovi´c, M. Doob, and H. Sachs, Spectra of Graphs, third ed., Barth, Heidelberg,
1995.
[4] L. Gabora and M. Steel, Autocatalytic networks in cognition and the origin of culture, J.
Theor. Biol., 63 (2017), pp. 617–638.
[5] R. C. Gatti, W. Hordijk, and S. Kauffman, Biodiversity is autocatalytic, Ecol. Model., 346
(2017), pp. 70–76.
[6] W. Hordijk and M. Steel, Detecting autocatalyctic, self-sustaining sets in chemical reaction
systems, J. Theor. Biol., 227 (2004), pp. 451–461.
[7] W. Hordijk and M. Steel, A formal model of autocatalytic sets emerging in an RNA repli-
cator system, J. Syst. Chem., 4 (2013), p. 3.
[8] W. Hordijk and M. Steel, Chasing the tail: The emergence of autocatalytic networks, Biosys-
tems, 152 (2017), pp. 1–10.
[9] W. Hordijk, M. Steel, and P. Dittrich, Autocatalytic sets and chemical organizations:
Modeling self-sustaining reaction networks at the origin of life, New J. Phys., 20 (2018),
p. 015011.
[10] W. Hordijk, M. Steel, and S. Kauffman, The structure of autocatalytic sets: Evolvability,
enablement, and emergence, Acta Biotheor., 60 (2012), pp. 379–392.
[11] S. Jain and S. Krishna, Autocatalytic sets and the growth of complexity in an evolutionary
model, Phys. Rev. Lett., 81 (1998), pp. 5684–5687.
[12] S.
Jaramillo,
R.
Honorato-Zimmer,
U.
Pereira,
D.
Contreras,
B.
Reynaert,
V. Hern´andez, J. Soto-Andrade, M. L. C´ardenas, A. Cornish-Bowden, and J. C.
Letelier, (M,R) systems and RAF sets: common ideas, tools and projections, in Pro-
ceedings of the ALIFEXII Conference, Odense Denmark, August 2010, 2010, pp. 94–100.
[13] S. A. Kauffman, Autocatalytic sets of proteins, J. Theor. Biol., 19 (1986), pp. 1–24.
[14] S. A. Kauffman, The Origins of Order, Oxford University Press, 1993.
[15] E. Mossel and M. Steel, Random biochemical networks and the probability of self-sustaining
autocatalysis, J. Theor. Biol., 233 (2005), pp. 327–336.
[16] F. L. Sousa, W. Hordijk, M. Steel, and W. Martin, Autocatalytic sets in the metabolic
network of E. coli, J. Syst. Chem., 6 (2015), p. 4.
[17] M. Steel, W. Hordijk, and J. Smith, Minimal autocatalytic networks, J. Theor. Biol., 332
(2013), pp. 96–107.
[18] R. E. Tarjan, Depth-ﬁrst search and linear graph algorithms, SIAM J. Comput., 1 (1972),
pp. 146–160.
[19] N. Vaidya, M. L. Manapat, C. I. A., R. Xulvi-Brunet, and N. Hayden, E. J. Lehman,
Spontaneous network formation among cooperative RNA replicators, Nature, 491 (2012),
pp. 72–77.
[20] V. Vasas, C. Fernando, M. Mantos, S. Kauffman, and E. Szathm´ary, Evolution before
genes, Biology Direct, 7:1 (2012).
19

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
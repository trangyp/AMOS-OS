---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1705.08539v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1705.08539v1_Conscious_and_controlling_elements_in_combinatorial_group_testing_problems_with_

> Source: 1705.08539v1_Conscious_and_controlling_elements_in_combinatorial_group_testing_problems_with_.pdf

> Pages: 21

---


## Page 1


arXiv:1705.08539v1  [cs.DM]  23 May 2017
Conscious and controlling elements in combinatorial group
testing problems with more defectives
D´aniel Gerbner∗†
M´at´e Vizer‡
MTA R´enyi Institute
Hungary H-1053, Budapest, Re´altanoda utca 13-15.
gerbner@renyi.hu, vizermate@gmail.com
September 21, 2018
Abstract
In combinatorial group testing problems Questioner needs to ﬁnd a defective ele-
ment x ∈[n] by testing subsets of [n]. In [18] the authors introduced a new model,
where each element knows the answer for those queries that contain it and each element
should be able to identify the defective one.
In this article we continue to investigate this kind of models with more defective
elements. We also consider related models inspired by secret sharing models, where
the elements should share information among them to ﬁnd out the defectives. Finally
the adaptive versions of the diﬀerent models are also investigated.
Keywords: Combinatorial Group Testing, defectives, cancellative
AMS Subj. Class. (2010): 94A50
∗Research supported by the J´anos Bolyai Research Fellowship of the Hungarian Academy of Sciences.
†Research supported by the National Research, Development and Innovation Oﬃce – NKFIH, grant
K116769.
‡Research supported by the National Research, Development and Innovation Oﬃce – NKFIH, grant
SNN 116095.
1


## Page 2


1
Introduction
In the most basic model of combinatorial group testing Questioner needs to ﬁnd a special
element x of {1, 2, ..., n}(=: [n]) by asking minimal number of queries (or group tests or
pools) of type ”does x ∈F ⊂[n]?”.
Special elements are usually called defective (or
positive).
For every combinatorial group testing problem there are at least two main
approaches: whether it is adaptive (or sequential) or non-adaptive(or oblivious). In the
adaptive scenario Questioner asks queries depending on the answers for the previously
asked queries, however in the non-adaptive version Questioner needs to pose all the queries
at the beginning. We call the complexity of a speciﬁc combinatorial group testing problem
the number of the queries needed to ask by Questioner in the worst case during an optimal
strategy.
Combinatorial group testing problems were ﬁrst considered during the World War II
by Dorfman [10] in the context of mass blood testing. Since then group testing techniques
have had many diﬀerent applications, for example in fault diagnosis in optical networks
[20], in quality control in product testing [25] or failure detection in wireless sensor networks
[23]. In this article we will mainly discuss non-adaptive models. The interested reader can
ﬁnd many variants and generalizations of the basic non-adaptive model and also many
applications in the book [11].
Description of the new model
In [18] the authors introduced new combinatorial group testing models, inspired by the
results of Tapolcai et al. [28, 29].
The main novel ingredient of these combinatorial group testing models is that the
elements are conscious and they distrust the Questioner, thus they want to control the
tests they are involved in. So we introduced the following extra condition: each element
knows the answer for those queries that contain it, and the goal: each element
should be able to identify the defective one.
Motivated by secret sharing schemes (see e.g. [2]), we also consider the following variant:
the elements can work together and share their knowledge. In this case we require certain
sets of elements to be able to identify the defective, while we require other sets to be unable
2


## Page 3


to identify the defective element. We emphasize that we do not deal with the way the data
is transmitted. Information can not be distributed between diﬀerent groups.
We mention here some other motivation to introduce these models: it is often mentioned
in the group testing literature that an advantage of testing pools together is that it increases
privacy. However, systematical research on this property has only started recently, see e.g.
[1, 5, 16]. These papers focus on cryptographic versions of the problem. Here we deal with
a simple combinatorial version, where privacy only means that an unauthorized participant
cannot completely detect the defective element(s). In [18] the authors considered models
with one defective element. The main aim of this article is to continue these investigations
with more defectives.
Simple combinatorial models with d defectives
About Questioner’s strategy we remark that - as he should ﬁnd all the defectives - the
asked queries should form a d-separating family (see the next section for a deﬁnition) in
the non-adaptive case, so for the minimum number of tests the known lower bound is
Ω( d2
log d log n), while the best upper bound construction yields O(d2 log n). It is one of the
major open problems in the theory of combinatorial group testing models to close the gap
between the previous upper and lower bound.
In the adaptive case there is a multiplicative constant factor between the information
theoretic lower bound and the best existing algorithm. The known best lower bound is
d log n
d , while the upper bound is O(d log n).
Structure of the paper
We organize the paper as follows: in Section 2 we introduce some properties and related
results about families of sets, that we will need later. In Section 3 we introduce the non-
adaptive models that we investigate, while in Section 4 we prove the main results.
In
Section 5 we look at the adaptive scenario, and we ﬁnish the article with remarks and open
questions in Section 6.
We also mention that in this article we use standard asymptotic notation.
3


## Page 4


2
Finite set theory background
Our topic is connected to several areas of ﬁnite set theory. In this section we introduce
some notions on families of subsets and known results about them, that we will use during
the proofs.
In this article we use the notation of 2[n] for the power set of [n] and for any F ⊂2[n],
a ∈[n] we use Fa := {F ∈F : a ∈F}.
The complement of a family F ⊂2n is
F := {[n] \ F : F ∈F}, while the dual of a family F ⊂2n is F′ := {Fa : a ∈[n]}. It is
deﬁned on the underlying set F and has cardinality at most n. For a family F ⊂2[n] and
d ≥1 let Fd := {∪d
i=1Fi : Fi ∈F, Fi ̸= Fj for i ̸= j}.
Now we introduce some notions about families of subsets of [n].
Deﬁnition 1. We say that F ⊂2[n] is:
•1 intersection closed if F, G ∈F implies F ∩G ∈F.
•2 Sperner if there are no two diﬀerent F1, F2 ∈F with F1 ⊂F2.
•3 cancellative if for any three F1, F2, F3 ∈F we have
F1 ∪F2 = F1 ∪F3 ⇒F2 = F3.
•4 intersection cancellative if for any three F1, F2, F3 ∈F we have
F1 ∩F2 = F1 ∩F3 ⇒F2 = F3.
•5 d-separating for some 1 ≤d ≤n −1 positive integer, if for any two diﬀerent
X1, X2 ⊂[n] with |X1| = |X2| = d there is F ∈F with:
F ∩X1 ̸= ∅and F ∩X2 = ∅, or
F ∩X2 ̸= ∅and F ∩X1 = ∅.
•6 d-union-free for some d ≥1 if for diﬀerent F1, . . . , Fd ∈F and diﬀerent
G1, . . . , Gd ∈F
d[
i=1
Fi =
d[
i=1
Gi
4


## Page 5


implies {F1, . . . , Fd} = {G1, . . . , Gd}.
•7 d-cover-free for some d ≥1 positive integer if there are no (d + 1)
diﬀerent F1, F2, ..., Fd+1 ∈F with
Fd+1 ⊂
d[
i=1
Fi.
•8 (r,d)-cover-free for some rd ≥1 positive integers if there are no (d + r) diﬀerent
F1, F2, ..., Fd+r ∈F with
d+r
\
i=d+1
Fd+1 ⊂
d[
i=1
Fi.
Before deﬁning the last notion, we need some introduction. We will generalize a graph
property, so it is more comfortable to use the word hypergraph instead of family of subsets
of [n] (where F is the set of the hyperedges and [n] is the set of vertices of the hypergraph).
There are several ways to deﬁne cycles in hypergraphs. Here we use one due to Berge [4].
A Berge-cycle in a hypergraph of length k (a Berge-Ck) consists of k diﬀerent hyperedges
E1, . . . , Ek and k diﬀerent vertices x1, . . . xk such that Ei contains xi and xi+1 for 1 ≤i ≤k
(modulo k, so Ek contains xk and x1). Note that for a 2-uniform hypergraph (that is a
graph) this notion is the same as the ’usual’ cycle in a graph. The Berge-girth (that we call
just girth in this article) of a hypergraph H is the smallest length of a cycle in H (that is ∞
if there is no cycle in H). A hypergraph is d-regular if every vertex is contained in exactly
d hyperedges, r-uniform if every hyperedge has size r and linear if any two hyperedges
intersect in at most one vertex.
Some known results about these notions that we will use later
• The notion cancellative was ﬁrst introduced by Frankl and F¨uredi in [17].
Fact 2. F ⊂2[n] is intersection cancellative if and only if F is cancellative.
• The notion of separating family in the context of combinatorial search theory was intro-
duced and ﬁrst studied by R´enyi in [24]. The following fact is rather trivial, so we omit its
proof.
5


## Page 6


Fact 3. Suppose Fn ⊂2[n] is a minimal separating family. Then we have:
|Fn| ≤⌈log2 n⌉.
Fact 4. F ⊂2[n] ﬁnds d defectives if and only if F is d-separating. The dual of a d-
separating family is d-union-free.
• The notion of d-union-free families was introduced by Hwang and T. S´os in [21] under
the name of d-Sidon families. They proved the following:
Theorem 5. (Hwang, T. S´os, [21], Theorem 3) There exists a d-union-free family
Fn ⊂2[n] with:
1
2(1 +
1
(4d)2 )n ≤|Fn|.
• The notion of d-cover-free families was introduced by Kautz and Singleton in [22]. Note
that a d-cover-free family is also d-union-free. They proved the following lower bound.
Theorem 6. (Kautz, Singleton, [22]) There exists an d-cover-free family Fn ⊂2[n] with:
Ω( 1
d2 ) = log2 |Fn|
n
.
D’yachkov and Rykov proved the following upper bound on the size of d-cover-free families:
Theorem 7. (D’yachkov, Rykov, [12]) Suppose that Fn ⊂2[n] is an d-cover-free family.
Then we have:
log2 |Fn|
n
≤2 log2 d
d2
(1 + o(1)).
• The notion of (r, d)-cover-free families were introduced by D’yachkov, Macula, Torney
and Vilenkin in [13]. They showed that a result by Stinson, Wei and Zhu [27] implies the
following:
Theorem 8. If the dual of Fn ⊂2[n] is (r, d)-cover-free, then we have:
|Fn| = Ωd,r(log2 n).
6


## Page 7


• Ellis and Linial [15] studied regular uniform linear hypergraphs with large girth. They
mention that a result of Cooper, Frieze, Molloy and Reed [6] implies that for any d ≥2,
r, g ≥3 and suﬃciently large n, if r divides n, then there is an r-uniform, d-regular, n-
vertex linear hypergraph with girth at least g. Moreover the argument can be adapted to
show the same statement in the case r divides dn.
Theorem 9. Let d ≥2, r, g ≥3 and n large enough such that r divides dn. Then there
exists a linear, d-regular, r-uniform hypergraph with girth at least g on n vertices.
3
Models
In this section we start our investigations and give a systematic study of models with the
extra property that each element knows the answers for those queries that contain it.
In all the models in this section an input set [n] is given, and d of them are defectives
(d ≤n).
We are dealing with non-adaptive models, so Questioner needs to construct
a family F ⊂2[n]. A set F correspond to a query of the following type: ’is x ∈F ⊂
[n]?’. In each model we assume that knowing all the answers is enough information for
Questioner to ﬁnd the defective elements, i.e. F is d-separating. Note that this immediately
implies a lower bound of Ωd(log2 n) on the size of the query family in each model. We
mention whenever the query family satisﬁes another property that could improve the factor
depending only on d, but calculating the factors is outside the scope of this paper.
The main diﬀerence between the following models is what we want the elements to
ﬁnd out. Using only the information available to them, i.e. the answers to the queries
containing them, we can require that they ﬁnd out something about the defective elements,
or oppositely, that they cannot ﬁnd out something.
When we say that an element x knows the defective elements, we mean that the query
family satisﬁes the following property: no matter what the defective element is, after the
answers x can ﬁnd out the defective ones, i.e. the subfamily Fx is d-separating. In the
opposite when we say that x does not know any of the defective elements, we mean that the
query family satisﬁes the following property: no matter what the defective elements are,
after the answers x cannot identify any defective element. Equivalently, for any D ⊂[n],
y ∈D with |D| = d there is a D′ ⊂[n] with |D′| = d, y ̸∈D′, such that the same members
7


## Page 8


of Fx intersect D and D′.
Another variant of this problem is when elements can share information among them.
It is possible that in some model some element can not ﬁnd out the defective, however
if we pick two elements and they share their information among them, they can ﬁnd the
defective elements. We consider these kind of models.
We also assume that in each model the elements know the setup of the problem, i.e.
that n elements are given and exactly d of them are defectives. We use the expression that
a family solves a model if it satisﬁes the property that describes the model.
In each of the following models we ﬁrst give a property describing what the elements
should know, and then we examine if there is a query set that solves that speciﬁc model or
state results about the cardinality of such query sets. Then we consider models where we
require some information to remain hidden from the elements. Finally we mix these types
of properties.
In this section we assume that there are exactly d ≥2 defective elements (and every
element knows that). We consider models analogous to the ones introduced in [18].
3.1
Model 1d
Probably the most natural model is the following:
Property: all elements ﬁnd out if they are defective.
We note that some cryptographic problems concerning this model were investigated in [1],
where the authors observed that the dual of a d-cover-free family solves this model. Here
we show that only such families solve this model.
Theorem 10. F solves Model 1d if and only if its dual is d-cover-free.
By Theorem 10, Theorem 6 and Theorem 7 we have:
Corollary 11. If Fn ⊂2[n] solves Model 1d and has minimum cardinality, then we have:
Ω(
d2
log2 d log2 n) = |Fn| = O(d2 log2 n).
8


## Page 9


3.2
Model 2d
Another natural model is when the elements should ﬁnd out everything.
Property: every element ﬁnds all the defectives.
It is obvious that no F can solve Model 2d if 1 < d < n: a defective element cannot gather
any information about the other elements, as it gets only YES answers.
3.3
Model 2′
d
As defective elements cannot gather any information about the other elements, in the next
model we only require non-defective elements to ﬁnd the defective ones.
Property: every non-defective element ﬁnds all the defectives.
Theorem 12. Suppose Fn solves Model 2′
d and has minimum cardinality. Then we have
|Fn| = Θd(log2 n).
Proof. We claim that the solution is the dual of a d-cover-free family, and the dual of a
(2, d)-cover-free family is always a solution. This together with Theorem 7 and Theorem 7
implies the statement.
Suppose that the dual is not d-cover-free. Then there are F1, F2, ..., Fd+1 ∈F with
Fd+1 ⊂∪d
i=1Fi. For the corresponding elements in the primal version we have xd+1 such
that any set F ∈F contains one of the other elements x1, . . . , xd. Thus if x1, . . . , xd are
the defectives, xd+1 teceives only YES answers, thus cannot distinguish this case from the
case xd+1 and any d −1 other elements are the defectives.
On the other hand let us assume F is the dual of a (2, d)-cover-free family. Then for
every non-defective elements x, y there is a set F ∈F such that F contains both x and
y, but none of the defective elements, thus x ﬁnds out that y is not defective, F solves
Model 2′
d. Indeed, there is an element in the intersection of the duals of x and y that is
not contained by the duals of the defective elements by the (2, d)-cover-free property. That
element is the dual of a set F ∈F that has the desired properties.
9


## Page 10


3.4
Model 2′′
d
The fact that defective elements cannot gather any information about the other elements
shows that even d −1 elements together cannot always ﬁnd the defectives. However, if d
elements share information, then either they are all the defectives and they do not need
to gather information about the other elements, or at least one of them is not a defective,
and then there is a solution by Model 2′
d.
Property: d elements together know who the defective elements are.
Theorem 13. Fn solves Model 2′′
d if and only if its dual G is d-union-free and Gd is Sperner
and intersection-cancellative.
Note that we know the maximum possible size of a Sperner and intersection cancellative
family (by results of Frankl and F¨uredi [17] and Tolhuizen [30]), but we do not know if
that construction can be written as Gd for a d-union-free family G.
Theorem 14. Suppose Fn solves Model 2′′
d and has minimum cardinality. Then we have
|Fn| = Θd(log2 n).
Proof. It is easy to see that if a family solves both Model 1d and Model 2′
d, then it also
solves Model 2′′
d. As we have seen in the proof of Theorem 12, a solution for Model 2′
d is
the dual of a d-cover-free family, thus it also solves Model 1d by Theorem 10. This implies
the upper bound.
3.5
Model 3d
Let us now examine the case when we require that elements do not ﬁnd the defective. Note
that as always, we assume that knowing all the answers is enough to ﬁnd the defective
element.
Property: no element knows any of the defective ones.
Note that for d = 1 there is a solution for Model 2d and there is no solution for Model 3d
[18]. For d ≥2 the situation is just the opposite: we will show that there is a solution for
Model 3d for n large enough. We will use arguments similar to the ones used in [3].
10


## Page 11


Theorem 15. If d ≥2, r ≥3 and n ≥dr + 2, then an r-uniform, d-regular linear
hypergraph with girth at least 5 solves Model 3d.
Proof. Let us consider an r-uniform, d-regular linear hypergraph F of girth 5.
For an
arbitrary element x its neighborhood consists of d disjoint sets of size r −1. Also, there
are more than d elements not in its neighborhood. It is easy to see that by r ≥3 x cannot
identify any defective elements.
On the other hand, if we know all the answers, the YES answers form stars with
the defective elements in the centers. The elements that get only YES answers are the
candidates for being defective. Every candidate that is not defective has to be connected
to all the defectives.
Two such candidate would form a Berge-C4 with any two of the
defective elements, thus there is only one additional candidate. But then it is the only one
among the d + 1 candidates that is connected to the other candidates, otherwise we could
ﬁnd a Berge-C3.
Corollary 16. If n is large enough compared to d > 1, then there is a solution for Model
3d.
Proof. If d ≥3, let us choose r = d, then Theorem 9 shows that we can ﬁnd such a family.
If d = 2, then Theorem 9 with r = 4 shows we can ﬁnd such a family for n even. If n is
odd, we ﬁnd such a family for n + 1, and delete an element. The resulting family is not
4-uniform, but that property is not actually needed (in fact, we used only that every set
in F has size at least 3).
3.6
Model 4d
Now we start to investigate models where elements can share information among them. Let
i and j be integers with 1 ≤i < j ≤n. When we say that a set of j elements together know
the defective elements, we mean that knowing the answers to all the queries containing at
least one element from the set is enough to ﬁnd all the defectives. Similarly, when we say
that a set of i elements do not know any of the defectives, we mean that knowing the
answers to all the queries intersecting the set is not enough to identify any of the defective
elements.
11


## Page 12


Property: any j elements together know the defectives, but i elements together do
not know any of the defectives, for some i and j with 1 ≤i < j ≤n.
Note that Corollary 16 shows that there is a solution if d > 1, i = 1 and j = n, where
n is large enough compared to d. In fact any n −r + 1 elements together know the answer
to all the queries, thus it is enough to assume j ≥n −r + 1. A more precise version of
Theorem 9 (see [15], Theorem 5) shows that about n1/6
d
can be chosen as r, which shows
that j can be as small as n −n1/6
d .
Proposition 17. If i ≥d or j < d, then there is no solution.
Proof. Let us assume ﬁrst we are given j elements. If all of them are defectives, they only
get YES answers, and do not gather any information about the other elements.
If i ≥d, for a set X let FX := ∪x∈XFx. Let us consider among the d-element sets X
such that FX is maximal. We claim that if the elements of X are the defectives, they can
ﬁnd it out by sharing information. Indeed, they get only YES answers. If they cannot be
sure that they are the defective ones, then there is another d-set Y that could be the set
of defectives. It means all the answers to the queries in FX would still be YES if Y was
the set of defectives, i.e. FX ⊆FY . By the assumption on X we have FX = FY , but then
the family is not d-separating.
Proposition 18. If j = d, then there is no solution.
Proof. If x receives only YES answers, he cannot ﬁnd out he is defective, thus there is
a set D = {Y1, . . . , yd} no containing X that intersects every member of Fx.
On the
other hand, if x and y1, . . . , yd−1 are the defectives, they together can ﬁgure that out. In
particular, they know that the set of defectives is not D, thus there is a set intersecting
{x, y1, . . . , yd−1} but not D. Such a set would be a member of Fx that does not intersect
D, a contradiction.
12


## Page 13


4
Proofs
4.1
Proof of Theorem 10
The dual of the d-cover-free property is that for every elements x1, . . . , xd+1 we cannot
have that the sets that contain xd+1 all contain at least one of the other xi’s. Let
Hx := {F \ {x} : F ∈Fx},
and τ(Hx) be the size of the smallest set that intersects every member of Hx. With these
notation the following lemma ﬁnishes the proof of Theorem 10.
Lemma 19. An element x always ﬁnds out if he is defective if and only if τ(Hx) > d.
Proof. If x gets a NO answer, he learns he is not defective, thus we can assume he only
gets YES answers. If Hx cannot be covered by at most d elements diﬀerent from x, then
the only way to get YES answer to every element of Fx is if x is defective (as defective
elements cover the sets that get YES answers). On the other hand if Hx can be covered by
at most d elements diﬀerent from x, then x cannot exclude the possibility that those are
the defective elements, together with arbitrary additional elements to reach d defectives.
4.2
Proof of Theorem 13
Lemma 20. F ⊂2[n] solves Model 2′′
d if and only if the following two properties hold:
•1 for any two diﬀerent d-element sets X, Y ⊂[n] there is F ∈F with F ∩X ̸= ∅and
F ∩Y = ∅, and
•2 for any three diﬀerent d-element sets X, Y, Z ⊂[n] there is F ∈F with (F ∩X ̸= ∅
and F ∩Y ̸= ∅and F ∩Z = ∅) or (F ∩X ̸= ∅and F ∩Z ̸= ∅and F ∩Y = ∅).
Proof. 1. Note that the property that Questioner can ﬁnd out the answer is: for any two
diﬀerent d-element sets X, Y ⊂[n] there is F ∈F with (F ∩X ̸= ∅and F ∩Y = ∅) or
(F ∩Y ̸= ∅and F ∩X = ∅). This property is contained in •1.
Let us assume now X is a set of size d.
13


## Page 14


2. If X is the set of defectives, they have to ﬁnd this out. It means that for a diﬀerent
d-element set Y , there should be an F ∈F with X ∩F ̸= ∅and Y ∩F = ∅.
3. If X is not the set of defectives, then another set Y is, and they have to identify Y .
Thus for a third d-element set Z, there should be a set that intersects X (so they know
the answer for it), and distinguishes Y and Z, i.e. it intersects exactly one of them.
Lemma 21. F ⊂2[n] satisﬁes properties •1 and •2 if and only if its dual G is d-union-free
and Gd is Sperner and intersection cancellative.
Proof. The dual of •1 is the following statement:
•3 for two diﬀerent subfamilies each consisting of d sets {F1, ..., Fd}, {G1, ..., Gd} ⊂F
there is f ∈[n] with f ∈∪d
i=1Fi \ ∪d
i=1Gi.
The dual of •2 is the following statement:
•4 for three diﬀerent subfamilies each consisting of d sets
{F1, ..., Fd}, {G1, ..., Gd}, {H1, ..., Hd} ⊂F
there is f ∈[n] with either
f ∈(∪d
i=1Fi ∩∪d
i=1Gi) \ ∪d
i=1Hi, or
f ∈(∪d
i=1Fi ∩∪d
i=1Hi) \ ∪d
i=1Gi.
It is easy to see that •3 is equivalent to the statement that G is d-union-free and Gd is
Sperner. Now we claim that •4 means that Gd is intersection cancellative. Let us use the
following notation:
F := ∪d
i=1Fi,
G := ∪d
i=1Gi,
H := ∪d
i=1Hi.
Using these, the existence of f means either F ∩G ̸⊂H or F ∩H ̸⊂G. Let us deﬁne three
properties.
◦1 F ∩G ̸⊂H.
◦2 F ∩H ̸⊂G.
14


## Page 15


◦3 H ∩G ̸⊂F.
Property •2 (for these three sets in this order) means that at least one of ◦1 and ◦2 holds.
Considering the same three sets in diﬀerent orders we get that also at least one of ◦1 and
◦3 and one of ◦3 and ◦2 holds. It is true if and only if at least two of these three properties
hold.
To ﬁnish the proof of Lemma 21 we prove the following:
Claim 22. A family H ⊂2[n] is intersection cancellative if and only if at least two out of
◦1, ◦2 and ◦3 hold for any three members of it.
Proof. Let us assume F′ is intersection cancellative and let F, G, H ∈H. Let us assume at
most one, say ◦3 of the three properties holds, thus ◦1 and ◦2 do not hold. The ﬁrst one
implies F ∩G ⊂H, and obviously F ∩G ⊂F. Thus we have F ∩G ⊂F ∩H. Similarly
the second one implies F ∩H ⊂F ∩G, hence they together imply F ∩H = F ∩G,
which contradicts the intersection cancellative property and our assumption that F, G, H
are three diﬀerent sets.
Let us assume now that H is not intersection cancellative, thus we have F ∩G = F ∩H.
This implies both F ∩G ⊂H and F ∩H ⊂G, thus at most one of ◦1, ◦2 and ◦3 can hold.
We are done with the proof of Theorem 13.
5
Adaptive scenario
A natural idea is to consider the adaptive versions of these problems. Here we assume
the Questioner knows all the earlier answers, and then he can choose the next query. He
can ﬁnd the defective, and then use further queries to share some information with the
elements. However, there are two versions of this problem. The elements might know the
algorithm, and use the order of the queries to gain information, or they only receive the
answers to the queries at the end in no particular order.
For example in Model 2d in the second version we require that for every element x the
family Fx with the answers is enough to ﬁnd all the defectives, i.e. for two distinct sets
15


## Page 16


D, D′ of size d there is a query that contains x and intersects only one of D and D′. It
is still obviously not solvable, as every defective element only gets YES answers and no
information about the others. However, in the ﬁrst version Questioner may start with a
d-separating family, then ask the set of defectives and then the set of non-defectives. This
way every element has to look only at the last query that contains it. If the answer to that
is YES, then it is the set of defectives, if the answer is NO, it is the set of non-defectives.
In both cases the defectives are identiﬁed.
From now on we consider only the second version, i.e. the elements receive the answer
to the queries containing them at the end of the algorithm in no particular order, and
they only know the underlying set and the number of defectives. It is still possible for the
Questioner to ﬁnd the defective, and then share some information using further queries.
Let ta(d, n) denote the number of queries in the fastest adaptive algorithm that ﬁnds the
d defective (we mentioned some inequalities on ta(d, n) in the introduction), then ta(d, n)
is a lower bound in every model. On the other hand ta(d, n) + d + 1 queries are enough
in Model 1d, ta(d, n) + 1 queries are enough in Model 2′
d and ta(d, n) + d + 1 queries are
enough in Model 2′′
d: ﬁrst Questioner ﬁnds the d defectives, then ask them as singletons,
and/or the set of non-defectives.
Let us consider now Model 3d. By Corollary 16 there is a solution for n large enough,
but that solution is linear in n. On the other hand it can be seen easily that for n = d + 1
there is no solution even adaptively. Here we give a faster algorithm.
Theorem 23. There is an adaptive algorithm that solves Model 3d and uses at most
2d log2 n + 5d queries if n is large enough.
Proof. Questioner starts with asking a query Q of size ⌊n/2⌋and its complement. Then
in the next round he asks two complementing subsets of size diﬀering by at most one in
every query that was answered YES (say Q1 and Q2 with Q1 ∪Q2 = Q). He repeats this in
every round except if the subset has size at most 5, he stops and does not ask that subset
as a query. Since he asks disjoint sets in every round, he gets at most d YES answers, thus
there are at most 2d queries in the next round. There are obviously at most log2 n rounds.
After that we have a family D of at most d sets of size at most 5, each containing at least
one defective element. Let A := {a1, . . . , al} be their union (l ≤5d), we also know that
every defective is in A. Let Di ∈D be the set that contains ai. As n is large enough, we
16


## Page 17


can assume that there were two queries B and C that were answered NO and have size at
least 5d. Let b1, . . . , b5d be distinct elements of B and c1, . . . , c5d be distinct elements of
C. Then Questioner also asks the queries {ai, bi, ci} for i ≤l.
As we know bi and ci are not defective, Questioner ﬁnds out if ai is defective for every
i. On the other hand, if ai is defective, every query Q that contains ai also contains either
other elements of Di or contains bi, thus ai cannot be sure he is defective. If ai is not
defective, then all he knows is that another element of Di is defective, but there are more
than one such elements. Any other element x appears in a query Q1 that got answer NO.
At this point all they know is that there is another set Q2 that contains a defective. Q2
has size at least 3, thus x does not know at this point which one is defective. If x = bi or
x = ci for some i, he can get additional information about only one element of Q2, thus
there are two candidates remaining. Finally, if the answer to {ai, bi, ci} is YES, then x
does not know if ai or ci is the defective.
It is easy to see that Model 4d still cannot be solved if i ≥d or j < d. Indeed, the
defectives still get only YES answers, thus less than d of them cannot have any idea about
the remaining defectives. On the other hand we will show that there are possible answers
such that the defectives together will ﬁnd out they are the defectives, showing i ≥d is
impossible. Let us assume that every answer is YES, unless it is impossible. If Questioner
ﬁnds out that D is the set of defectives, it means that for every other set D′ of size d there
was a query at some point that intersected exactly one of D and D′. At that point YES
was a possible answer, thus the answer to that query was YES. Hence it intersected D and
was disjoint from D′. Then an element of D knows D′ is not the set of defectives, and this
holds for every set D′ ̸= D of size d.
6
Remarks
We ﬁnish this article with some possible directions that can be investigated:
• In some of the above models we proved that there is a family that solves the model,
but did not say anything about its possible size.
17


## Page 18


• In case of Model 4d our results can only be considered as the starting point of the
investigations. In particular, it would be interesting to see if i can go above 1. It is tempting
to try to extend the proof of Theorem 15 to this case, and use a linear hypergraph of large
girth. However, it does not work even for i = 2. The property that the defectives can be
identiﬁed forces the elements to be contained in many hyperedges, while the property that
no 2 elements can identify any of the defectives forces the opposite.
If the query hypergraph is linear and d-separating, it is easy to see that for two elements
contained by the same query there must be at least d other sets containing the two elements.
This implies almost every element has to be contained in more than (d + 1)/2 queries.
On the other hand let us consider two elements x, y that are not contained in the same
hyperedge. The large girth of the query hypergraph implies that there is at most one other
element z contained in a hyperedge Q together with x and another hyperedge together with
y (if there is no such z, then let Q be an arbitrary query containing x). Let us assume the
answer to Q is NO, and the answer to every other query containing x or y is YES. Then x
and y together know that x is not defective. If they cannot identify y as a defective, there
cannot be more than d hyperedges containing x or y besides Q. This implies almost every
element has to be contained in at most (d + 1)/2 queries.
• In [18] we considered the abstract version of the model introduced by Tapolcai et
al. [28, 29]. Here we extended our models to the case of more defectives. It would be
interesting to see if their model can be extended similarly.
• It is a phenomenon in combinatorial group testing that in most of the models the
adaptive version actually means two round version of the problem (see e.g. [8]) Recently
there was some interest in the r round (or multi-stage) versions of combinatorial group
testing problems, where this phenomenon does not hold (see e.g. [7, 19]). It would be
interesting to investigate these models in this context.
• One can consider a variant of these models, where instead of requiring that the
elements ﬁnd all (or none) of the defective elements, we require that they identify at least
i and/or at most j of them.
18


## Page 19


Acknowledgement
We would also like to thank all participants of the Combinatorial Search Seminar at the
Alfr´ed R´enyi Institute of Mathematics for fruitful discussions.
References
[1] M. J. Atallah, K. B. Frikken, M. Blanton, Y. Cho. Private combinatorial group testing.
In Proceedings of the 2008 ACM symposium on Information, computer and communi-
cations security, pp. 312–320, (2008).
[2] A. Beimel. Secret-sharing schemes: a survey, In International Conference on Coding
and Cryptology. Springer Berlin Heidelberg, pp. 11–46, (2011).
[3] F. S. Benevides, D. Gerbner, C. T. Palmer, D. K. Vu. Generalising separating families
of ﬁxed size. arXiv preprint arXiv:1509.00131, (2015).
[4] C. Berge. Hypergraphs, Combinatorics of Finite Sets. North-Holland, Amsterdam.
(1989).
[5] A. Cohen, A. Cohen, O. Gurewitz. Secure group testing. In IEEE International Sym-
posium on Information Theory, IEEE, pp. 1391–1395, (2016).
[6] C. Cooper, A. Frieze, M. Molloy, B. Reed. Perfect matchings in random r-regular,
s-uniform hypergraphs. Combin. Probab. Comput., 5(1), 1–14, (1996).
[7] P. Damaschke, A. S. Muhammad, E. Triesch. Two new perspectives on multi-stage
group testing. Algorithmica, 67(3), 324–354, (2013).
[8] A. De Bonis, L. Gasieniec, U. Vaccaro. Optimal two-stage algorithms for group testing
problems, SIAM Journal on Computing, 34(5), 1253–1270, (2005).
[9] T. J. Dickson. On a problem concerning separating systems of a ﬁnite set. Journal of
Combinatorial Theory, 7.3, 191–196, (1969).
[10] R. Dorfman. The detection of defective members of large populations. The Annals of
Mathematical Statistics, 14(4), 436–440, (1943).
19


## Page 20


[11] D.-Z. Du, F. K. Hwang. Pooling designs and nonadaptive group testing: important
tools for DNA sequencing. Vol. 18. World Scientiﬁc Publishing Company Incorporated.
(2006).
[12] A. D’yachkov, V. V. E. Rykov. Bounds on the length of disjunctive codes. Problemy
Peredachi Informatsii, 18(3), 7–13, (1982).
[13] A. D’yachkov, P. Vilenkin, D. Torney, A. Macula. Families of ﬁnite sets in which no
intersection of
sets is covered by the union of s others. Journal of Combinatorial
Theory, Series A, 99(2), 195–218 (2002).
[14] A. D’yachkov, P. Vilenkin, S. Yekhanin. Upper bounds on the rate of superimposed
(s,l)-codes based on Engels inequality. In Proceedings of the International Conf. on
Algebraic and Combinatorial Coding Theory (ACCT), pp. 95–99, (2002).
[15] D. Ellis, N. Linial. On regular hypergraphs of high girth. The Electronic Journal of
Combinatorics, 21(1)(P1.54), (2014).
[16] D. Eppstein, M. T. Goodrich, D. S. Hirschberg. Combinatorial pair testing:
dis-
tinguishing workers from slackers. In Workshop on Algorithms and Data Structures,
Springer Berlin Heidelberg, pp. 316–327, (2013).
[17] P. Frankl, Z. F¨uredi. Union-free hypergraphs and probability theory. European Journal
of Combinatorics, 5(2): 127–131, (1984).
[18] D. Gerbner, M. Vizer. Conscious and controlling elements in combinatorial group
testing problems. arXiv preprint, arXiv:1703.05398 (2017).
[19] D. Gerbner, M. Vizer. Rounds in a combinatorial search problem. arXiv preprint,
arXiv:1611.10133 (2016).
[20] N. J. Harvey, M. Patrascu, Y. Wen, S. Yekhanin, V. W. Chan. Non-adaptive fault
diagnosis for all-optical networks via combinatorial group testing on graphs. In INFO-
COM 2007. 26th IEEE International Conference on Computer Communications, pp.
697–705, (2007).
20


## Page 21


[21] F.K. Hwang, V. T. S´os. Non-adaptive hypergeometric group testing. Studia Sci. Math.
Hungar., 22:257–263 (1987).
[22] W. Kautz, R. Singleton. Nonrandom binary superimposed codes. IEEE Transactions
on Information Theory, 10(4), 363–377, (1964).
[23] C. Lo, M. Liu, J. P. Lynch, A. C. Gilbert. Eﬃcient sensor fault detection using com-
binatorial group testing. In IEEE International Conference on Distributed Computing
in Sensor Systems (DCOSS), 199–206, (2013).
[24] A. R´enyi. On random generating elements of a ﬁnite Boolean algebra. Acta Sci. Math.
Szeged, 22(4), 75–81, (1961).
[25] M. Sobel, P. A. Groll. Group testing to eliminate eﬃciently all defectives in a binomial
sample. Bell Labs Technical Journal, 38(5), 1179–1252, (1959).
[26] J. Spencer. Minimal completely separating systems. Journal of Combinatorial Theory,
8(4): 446–447, (1970).
[27] D.R. Stinson, R. Wei, L. Zhu. Some New Bounds for Cover-Free Families. Journal of
Combinatorial Theory, Series A, 90(1), 224–234, (2000).
[28] J. Tapolcai, L. R´onyai, ´E. Hosszu, P. Ho, S. Subramaniam. Signaling Free Localiza-
tion of Node Failures in All-Optical Networks. In Proc. IEEE INFOCOM, Toronto,
Canada, pp. 1860–1868, (2014).
[29] J. Tapolcai, L. R´onyai, ´E. Hosszu, L. Gyim´othi, P.-H. Ho, S. Subramaniam. Signaling
Free Localization of Node Failures in All-Optical Networks. IEEE Transactions on
Communications, 64(6), 2527–2538, (2016).
[30] L. M. Tolhuizen. New rate pairs in the zero-error capacity region of the binary multi-
plying channel without feedback. IEEE Transactions on Information Theory, 46(3),
1043–1046, (2000).
21

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1705_08539v1_conscious_and_controlling_elements_in_combinatorial_group_testing_problems_with
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1705_08539V1_CONSCIOUS_AND_CONTROLLING_ELEMENTS_IN_COMBINATORIAL_GROUP_TESTING_PROBLEMS_WITH.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

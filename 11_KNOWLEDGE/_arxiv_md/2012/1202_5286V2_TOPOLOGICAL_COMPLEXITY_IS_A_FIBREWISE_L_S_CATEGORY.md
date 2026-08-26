---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1202.5286v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1202.5286v2_Topological_Complexity_is_a_Fibrewise_L-S_Category

> Source: 1202.5286v2_Topological_Complexity_is_a_Fibrewise_L-S_Category.pdf

> Pages: 20

---


## Page 1


arXiv:1202.5286v2  [math.AT]  26 Feb 2012
ERRATA FOR :
TOPOLOGICAL COMPLEXITY IS A FIBREWISE L-S
CATEGORY
NORIO IWASE† AND MICHIHIRO SAKAI
Abstract. There is a problem with the proof of Theorem 1.13 of [2] which
states that for a ﬁbrewise well-pointed space X over B, we have catB
B(X) =
cat*
B(X) and that for a locally ﬁnite simplicial complex B, we have T C(B) =
T CM(B). While we still conjecture that Theorem 1.13 is true, this problem
means that, at present, no proof is given to exist. Alternatively, we show the
diﬀerence between two invariants cat*
B(X) and catB
B(X) is at most 1 and the
conjecture is true for some cases. We give further corrections mainly in the
proof of Theorem 1.12.
It was pointed out to the authors by Jose Calcines that there is a problem with
the proof of Theorem 1.13 of [2] which states that for a ﬁbrewise well-pointed space
X over B, we have catB
B(X) = cat*
B(X) and that for a locally ﬁnite simplicial
complex B, we have T C(B) = T CM(B), where cat*
B(X) and T CM(B) are new
versions of a ﬁbrewise L-S category and a topological complexity, respectively, which
are introduced in [2].
While we still conjecture that Theorem 1.13 of [2] is true, this problem means
that, at present, no proof is given to exist. It then results that “T C(B)” in Corollary
8.7 of [2] must be replaced with “T CM(B)” and the resulting inequality should be
presented in the following form:
Zπ(B) ≤wgtπ(B) ≤MwgtB
B(d(B)) ≤T CM(B)−1 ≤catlenB
B(d(B)) ≤CatB
B(d(B)).
The problem in the argument occurs on page 14 where a homotopy
ˆΦi : ˆUi × [0, 1] →ˆX
is given, while the deﬁnition of ˆΦi apparently is not well-deﬁned. Alternatively, we
show here the diﬀerence between two invariants cat*
B(X) and catB
B(X) is at most 1
and the conjecture is true for some cases.
Theorem 1. For a ﬁbrewise well-pointed space X over B, we have cat*
B(X) ≤
catB
B(X) ≤cat*
B(X) + 1 which implies that, for a locally ﬁnite simplicial complex
B, we have T C(B) ≤T CM(B) ≤T C(B) + 1.
Proof: The inequality of T C(B) and T CM(B) in Theorem 1 for a locally ﬁnite
simplicial complex B is, by Theorem 1.7 in [2], a special case of the inequality of
cat*
B(X) and catB
B(X) in Theorem 1 for a ﬁbrewise well-pointed space X. So it is
Date: October 22, 2018.
2000 Mathematics Subject Classiﬁcation. Primary 55M30, Secondary 55Q25.
Key words and phrases. Toplogical complexity, Lusternik-Schnirelmann category.
† supported by the Grant-in-Aid for Scientiﬁc Research #22340014 from Japan Society for the
Promotion of Science.
1


## Page 2


2
IWASE AND SAKAI
suﬃcient to show the inequality for X: because the inequality cat*
B(X) ≤catB
B(X)
is clear by deﬁnition, all we need to show is the inequality catB
B(X) ≤cat*
B(X) + 1.
Let X be a ﬁbrewise well-pointed space over B with a projection pX : X →B and a
section sX : B →X. Let (u, h) be a ﬁbrewise (strong) Strøm structure (see Crabb
and James [1]) on (X, sX(B)), i.e., u : X →[0, 1] is a map and h : X ×[0, 1] →X is
a ﬁbrewise pointed homotopy such that u−1(0) = sX(B), h(x, 0) = x for any x ∈X
and h(x, 1) = sX ◦pX(x) for any x ∈X with u(x) < 1. Assume cat*
B(X) = m and
the family {Ui ; 0≤i≤m} of open sets of X satisﬁes X =
mS
i=0
Ui and each open set Ui
is ﬁbrewise contractible (into sX(B)) by a ﬁbrewise homotopy Hi : Ui × [0, 1] →X.
Let Vi = U ′
i ∪V for 0 ≤i ≤m and Vm+1 = u−1([0, 2
3)) where U ′
i = Ui ∖u−1([0, 1
2])
and V = u−1([0, 1
3)). Then the restriction Hi|U′
i : U ′
i × [0, 1] →X gives a ﬁbrewise
contraction of U ′
i and the restriction of the ﬁbrewise (strong) Strøm structure h|V :
V × [0, 1] →X gives a ﬁbrewise pointed contraction of V . Since U ′
i and V are
obviously disjoint, we obtain that Vi = U ′
i ∪V ⊃∆(B) is a ﬁbrewise contractible
open set by a ﬁbrewise pointed homotopy. Similarly the restriction of the ﬁbrewise
(strong) Strøm structure h|Vm+1 : Vm+1 × [0, 1] →X gives a ﬁbrewise pointed
contraction of Vm+1 ⊃∆(B). Since Vi ∪Vm+1 = U ′
i ∪Vm+1 = Ui ∪Vm+1 ⊃Ui, we
obtain
m+1
S
i=0
Vi =
mS
i=0
(Vi ∪Vm+1) ⊃
mS
i=0
Ui = X. This implies catB
B(X) ≤m + 1 =
cat*
B(X) + 1 and it completes the proof of Theorem 1.
□
Theorem 2. Let X be a ﬁbrewise well-pointed space over B with cat*
B(X) = m
and {Ui ; 0≤i≤m} be an open cover of X, in which Ui is ﬁbrewise contractible (into
sX(B)) by a ﬁbrewise homotopy Hi : Ui×[0, 1] →X. Then we have catB
B(X) = m =
cat*
B(X) if one of the following conditions is satisﬁed.
(1) There exists i, 0 ≤i ≤m such that Ui does not intersect with sX(B).
(2) There exists i, 0 ≤i ≤m such that Ui includes sX ◦pX(Ui) ⊂X.
Theorem 2 immediately implies the following corollary.
Corollary 3. Let B be a locally ﬁnite simplicial complex with T C(B) = m and
{Ui ; 1≤i≤m} be an open cover of X, in which Ui is compressible into the image
∆(B) of diagonal map ∆: B →B×B. Then we have T CM(B) = m = T C(B) if
one of the following conditions is satisﬁed.
(1) There exists i, 1 ≤i ≤m such that Ui does not intersect with ∆(B).
(2) There exists i, 1 ≤i ≤m such that Ui includes ∆◦pr2(Ui) ⊂B×B.
Proof of Theorem 2: For simplicity, we assume that i = 0 in each cases. Let X be
a ﬁbrewise well-pointed space over B with a projection pX : X →B and a section
sX : B →X. Let (u, h) be a ﬁbrewise (strong) Strøm structure on (X, sX(B)), i.e.,
u : X →[0, 1] is a map and h : X ×[0, 1] →X is a ﬁbrewise pointed homotopy such
that u−1(0) = sX(B), h(x, 0) = x for any x ∈X and h(x, 1) = sX ◦pX(x) for any
x ∈X with u(x) < 1. Then the ﬁbrewise map r : X →X given by r(x) = h(x, 1)
satisﬁes the following.
i) X =
mS
i=0
r−1(Ui), since X =
mS
i=0
Ui.
ii) r is ﬁbrewise homotopic to the identity by h.
iii) r−1(sX(B)) ⊃U = u−1([0, 1)), where U is ﬁbrewise contractible by h|U.


## Page 3


ERRATA FOR :
TOPOLOGICAL COMPLEXITY IS A FIBREWISE L-S CATEGORY
3
iv) Each r−1(Ui) is ﬁbrewise contractible, since r is ﬁbrewise homotopic to the
identity by ii) and Ui is ﬁbrewise contractible.
Firstly, we consider the case (1): let V0 = r−1(U0)∪u−1([0, 2
3)) and Vi = (r−1(Ui)∖
u−1([0, 1
2]))∪u−1([0, 1
3)), 1 ≤i ≤m. Thus
mS
i=0
Vi = r−1(U0)∪
mS
i=1
(Vi∪u−1([0, 2
3))) ⊃
r−1(U0)∪
mS
i=1
r−1(Ui) =
mS
i=0
r−1(Ui) = X by i). Since r−1(Ui) is ﬁbrewise contractible
by iv), so is the open set r−1(Ui) ∖u−1([0, 1
2]) for every i ≥0, where r−1(U0) ∖
u−1([0, 1
2]) = r−1(U0) since U0 does not intersect with sX(B). On the other hand,
u−1([0, t
3)), t = 1, 2 are also ﬁbrewise contractible by ﬁbrewise pointed homotopies
by iii). Hence each Vi, 0 ≤i ≤m is ﬁbrewise contractible by a ﬁbrewise pointed
homotopy, and hence catB
B(X) ≤m = cat*
B(X). Thus we have cat*
B(X) = catB
B(X).
Secondly, we consider the case (2): let V0 = r−1(U0) ∪u−1([0, 2
3)) and Vi =
(r−1(Ui) ∖u−1([0, 1
2])) ∪u−1([0, 1
3)), 1 ≤i ≤m. Thus
mS
i=0
Vi = r−1(U0) ∪
mS
i=1
(Vi ∪
u−1([0, 2
3))) ⊃
mS
i=0
r−1(Ui) = X by i). Since r−1(Ui) is ﬁbrewise contractible by iv),
so is the open set r−1(Ui) ∖u−1([0, 1
2]) which does not intersect with u−1([0, 1
3)),
for every i > 0. On the other hand, each open set u−1([0, t
3)), t = 1, 2 is ﬁbrewise
contractible by a ﬁbrewise pointed homotopy by iii).
Hence each open set Vi,
1 ≤i ≤m is ﬁbrewise contractible by ﬁbrewise pointed homotopy. When i = 0,
we need to construct a ﬁbrewise pointed homotopy H : V0 × [0, 1] →X using the
ﬁbrewise homotopy H0 : U0 ×[0, 1] →X and the ﬁbrewise (strong) Strøm structure
(u, h) as follows:
H(x, t) =
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






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

x,
t = 0
h(x, 3t),
0 ≤t ≤1
3
r(x),
t = 1
3
H0(r(x), 3t−1),
1
3 ≤t ≤2
3
sX ◦pX(r(x)) = sX ◦pX(x) = sX(b),
t = 2
3
H0(sX(b), 3−3t),
2
3 ≤t ≤1
sX(b),
t = 1

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

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

,
x ∈V0 ∖U,
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

x,
t = 0
h(x, 3t),
0 ≤t ≤1
3
r(x) = sX(b),
t = 1
3
H0(sX(b), 3t−1),
1
3 ≤t ≤u(x)−1
3
H0(sX(b), 3u(x)−2),
u(x)−1
3 ≤t ≤5
3−u(x)
H0(sX(b), 3−3t),
5
3−u(x) ≤t ≤1
sX(b),
t = 1

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

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

,
2
3 ≤u(x) < 1,





x,
t = 0
h(x, 3t),
0 ≤t ≤1
3
r(x) = sX(b),
1
3 ≤t ≤1





,
0 ≤u(x) < 2
3,
sX(b),
x ∈sX(B),


## Page 4


4
IWASE AND SAKAI
where b = pX(x) = pX(r(x)), and hence for x ∈V0∖u−1([0, 2
3)) ⊂r−1(U0), we have
sX(b) = sX ◦pX(r(x)) ∈U0 since r(x) ∈U0. Thus we have cat*
B(X) = catB
B(X),
and it completes the proof of Theorem 2.
□
The following are corrections in [2].
• The part of Proof of Theorem 1.12 from page 13 line -3 to page 14 line 12
is not clearly given and must be rewritten completely:
Proof: For each vertex β of B, let Vβ be the star neighbourhood in B and
V = S
β Vβ×Vβ ⊂B×B. Then the closure ¯V = S
β ¯Vβ× ¯Vβ is a subcom-
plex of B×B.
For the barycentric coordinates {ξβ} and {ηβ} of x and
y, resp, we see that (x, y) ∈V if and only if P
β Min(ξβ, ηβ) > 0 and that
P
β Min(ξβ, ηβ) = 1 if and only if the barycentric coordinates of x and y are
the same, or equivalently, (x, y) ∈∆(B). Hence we can deﬁne a continuous
map v : B×B →[0, 3] by the following formula.
v(x, y) =
(
3 −3 P
β Min(ξβ, ηβ),
if (x, y) ∈¯V ,
3,
if (x, y) ̸∈V .
Since B is locally ﬁnite, v is well-deﬁned on B×B, and we have v−1(0) =
∆(B) and v−1([0, 3)) = V . Let U = v−1([0, 1)) an open neighbourhood
of ∆(B). In [3], Milnor deﬁned a map µ : V →B giving an ‘average’ of
(x, y) ∈V as follows.
µ(x, y) = (ζβ),
ζβ = Min(ξβ, ηβ)/
X
γ
Min(ξγ, ηγ),
where {ξβ} and {ηβ} are barycentric coodinates of x and y respectively,
and γ runs over all vertices in B. Since B is locally ﬁnite, µ is well-deﬁned
on V and satisﬁes µ(x, x) = x for any x ∈B. Using the map µ, Milnor
introduced a map λ : V ×[0, 1] →B as follows.
λ(x, y, t) =
(
(1−2t)x + 2tµ(x, y),
t ≤1
2,
(2−2t)µ(x, y) + (2t−1)y,
t ≥1
2.
Hence we have λ(x, x, t) = x for any x ∈B and t ∈[0, 1]. Using Milnor’s
map λ, we obtain a pair of maps (u, h) as follows:
u(x, y) = Min{1, v(x, y)}
and
h(x, y, t) =
(
(λ(x, y, Min{t, w(x, y)}), y),
if v(x, y) < 3,
(x, y),
if v(x, y) > 2,
where w : B×B →[0, 1] is given by
w(x, y) =





1,
v(x, y) ≤1,
2 −v(x, y),
1 ≤v(x, y) ≤2,
0,
v(x, y) ≥2.
If 2 < v(x, y) < 3, then, by deﬁnition, we have w(x, y) = 0 and
(λ(x, y, Min{t, w(x, y)}), y) = (λ(x, y, 0), y) = (x, y).
Thus h is also a well-deﬁned continuous map.
Then we have u−1(0) =
∆(B), u−1([0, 1)) = U and h(x, y, 0) = (x, y) for any (x, y) ∈B×B. If


## Page 5


ERRATA FOR :
TOPOLOGICAL COMPLEXITY IS A FIBREWISE L-S CATEGORY
5
(x, y) ∈U, we have w(x, y) = 1, h(x, y, t) = (λ(x, y, t), y) and h(x, y, 1) =
(y, y) ∈∆(B). Moreover, we have h(x, x, t) = (x, x) for any x ∈B and
t ∈[0, 1] and pr2 ◦h(x, y, t) = y for any (x, y, t) ∈B×B×[0, 1]. This implies
that h is a ﬁbrewise pointed homotopy.
Thus the data (u, h) gives the
ﬁbrewise (strong) Strøm structure on (B×B, ∆(B)).
□
• In page 19, line 34, “t = 0” must be replaced by “t = 1”.
• In page 20, line 17, “that” must be replaced by “that H(sZ(b), t) = sW (b)
for any b ∈B and”.
• In page 20, line 28, the formula “ ˇH(q(sZ(b), t), s) = sW (b),” must be added.
References
[1] M. C. Crabb. and I. M. James, “Fibrewise Homotopy Theory”, Springer Monographs in
Mathematics, Springer-Verlag London, Ltd., London, 1998.
[2] N. Iwase and M. Sakai, Topological complexity is a ﬁbrewise L-S category, Topology and its
Applications, 157 (2010), 10–21.
[3] J. Milnor, On Spaces Having the Homotopy Type of a CW -Complex, Trans. Amer.
Math. Soc. 90 (1959), 272–280.
E-mail address: iwase@math.kyushu-u.ac.jp
E-mail address, Sakai: sakai@kurume-nct.ac.jp
(Iwase) Faculty of Mathematics, Kyushu University, Fukuoka 810-8560, Japan
(Sakai) Kurume National College of Technology, Fukuoka 830-8555, Japan.


## Page 6


arXiv:1202.5286v2  [math.AT]  26 Feb 2012
TOPOLOGICAL COMPLEXITY IS A FIBREWISE L-S
CATEGORY
NORIO IWASE AND MICHIHIRO SAKAI
Abstract. Topological complexity T C(B) of a space B is introduced by M.
Farber to measure how much complex the space is, which is ﬁrst considered
on a conﬁguration space of a motion planning of a robot arm. We also con-
sider a stronger version T CM(B) of topological complexity with an additional
condition: in a robot motion planning, a motion must be stasis if the initial
and the terminal states are the same. Our main goal is to show the equalities
T C(B) = cat*
B(d(B))+1 and T CM(B) = catB
B(d(B))+1, where d(B) = B×B
is a ﬁbrewise pointed space over B whose projection and section are given by
pd(B) = pr2 : B×B →B the canonical projection to the second factor and
sd(B) = ∆B : B →B×B the diagonal. In addition, our method in studying
ﬁbrewise L-S category is able to treat a ﬁbrewise space with singular ﬁbres.
1. Introduction
We say a pair of spaces (X, A) is an NDR pair or A is an NDR subset of X, if
the inclusion map is a (closed) coﬁbration, in other words, the inclusion map has
the (strong) Strøm structure (see page 22 in G. Whitehead [24]). When the set of
the base point of a space is an NDR subset, the space is called well-pointed.
Let us recall the deﬁnition of a sectional category (see James [14]) which is
originally deﬁned and called by Schwarz ‘genus’.
Deﬁnition 1.1 (Schwarz [21], James [15]). For a ﬁbration p : E →X, the sectional
cateory secat(p) (= one less than the Schwarz genus Genus(p)) is the minimal
number m ≥0 such that there exists a cover of X by (m+1) open subsets Ui ⊂X
each of which admits a continuous section si : Ui →E.
The topological complexity of a robot motion planning is ﬁrst introduced by
M. Farber [2] in 2003 to measure the discontinuity of a robot motion planning
algorithm searching also the way to minimise the discontinuity. At a more general
view point, Farber deﬁned a numerical invariant T C(B) of any topological space
B: let P(B) be the space of all paths in B. Then there is a Serre path ﬁbration
π : P(B) →B×B given by π(ℓ) = (ℓ(0), ℓ(1)) for ℓ∈P(B).
Deﬁnition 1.2 (Farber). For a space B, the topological complexity T C(B) is the
minimal number m ≥1 such that there exists a cover of B×B by m open subsets Ui
each of which admits a continuous section si : Ui →P(B) for π : P(B) →B×B.
By deﬁnition, we can observe that the topological complexity is nothing but the
Schwartz genus or the sectional category.
Date: October 22, 2018, [First draft].
2000 Mathematics Subject Classiﬁcation. Primary 55M30, Secondary 55Q25.
Key words and phrases. Toplogical complexity, Lusternik-Schnirelmann category.
1


## Page 7


2
IWASE AND SAKAI
Farber has further introduced a new invariant restricting motions by giving two
additional conditions on the section s : U →P(B) (see Farber [3]).
(1) s(b, b) = cb the constant path at b for any b ∈B,
(2) s(b1, b2) = s(b2, b1)−1 if (b1, b2) ∈U.
It gives a stronger invariant than the topological complexity, and the Z/2-equivariant
theory must be applied as in Farber-Grant [4]. This new topological invariant, in
turn, suggests us another motion planning under the condition that a motion is sta-
sis if the initial and the terminal states are the same. Let us state more precisely.
Deﬁnition 1.3. For a space B, the ‘monoidal’ topological complexity T CM(B) is
the minimal number m ≥1 such that there exists a cover of B×B by m open subsets
Ui ⊃∆(B) each of which admits a continuous section si : Ui →P(B) for the Serre
path ﬁbration π : P(B) →B×B satisfying si(b, b) = cb for any b ∈B.
Remark 1.4. This new topological complexity T CM is not a homotopy invariant,
in general. However, it is a homotopy invariant if we restrict our working category
to the category of a space B such that the pair (B×B, ∆(B)) is NDR.
On the other hand, a ﬁbrewise pointed L-S category of a ﬁbrewise pointed space
is introduced and studied by James-Morris [13]. Let us recall the deﬁnition:
Deﬁnition 1.5 (James-Morris [13]).
(1) Let X be a ﬁbrewise pointed space
over B. The ﬁbrewise pointed L-S category catB
B(X) is the minimal num-
ber m ≥0 such that there exists a cover of X by (m + 1) open subsets
Ui ⊃sX(B) each of which is ﬁbrewise null-homotopic in X by a ﬁbrewise
pointed homotopy. If there are no such m, we say catB
B(X) = ∞.
(2) Let f : Y →X be a ﬁbrewise pointed map over B. The ﬁbrewise pointed
L-S category catB
B(f) is the minimal number m ≥0 such that there exists
a cover of Y by (m + 1) open subsets Ui ⊃sY (B), where the restriction
f|Ui to each subset is ﬁbrewise compressible into sX(B) in X by a ﬁbrewise
pointed homotopy. If there are no such m, we say catB
B(f) = ∞.
To describe our main result, we further introduce a new unpointed version of
ﬁbrewise L-S category: the ﬁbrewise L-S category catB( ) of an ﬁbrewise unpointed
space is also deﬁned by James and Morris [13] as the minimum number (minus one)
of open subsets which cover the given space and are ﬁbrewise null-homotopic (see
also James [14] and Crabb-James [1]). In this paper, we give a new version of a
ﬁbrewise unpointed L-S category of a ﬁbrewise pointed space as follows:
Deﬁnition 1.6.
(1) Let X be a ﬁbrewise pointed space over B. The ﬁbrewise
unpointed L-S category cat*
B(X) is the minimal number m ≥0 such that
there exists a cover of X by (m+1) open subsets Ui each of which is ﬁbrewise
compressible into sX(B) in X by a ﬁbrewise homotopy. If there are no such
m, we say cat*
B(X) = ∞.
(2) Let f : Y →X be a ﬁbrewise pointed map over B. The ﬁbrewise unpointed
L-S category cat*
B(f) is the minimal number m ≥0 such that there exists
a cover of Y by (m + 1) open subsets Ui, where the restriction f|Ui to each
subset is ﬁbrewise compressible into sX(B) in X by a ﬁbrewise homotopy.
If there are no such m, we say cat*
B(f) = ∞.
For a given space B, we deﬁne a ﬁbrewise pointed space d(B) by d(B) = B×B
with pd(B) = pr2 : B×B →B and sd(B) = ∆B : B →B×B the diagonal. One of
our main goals of this paper is to show the following theorem.


## Page 8


TOPOLOGICAL COMPLEXITY IS A FIBREWISE L-S CATEGORY
3
Theorem 1.7. For a space B, we have the following equalities.
(1) T C(B) = cat*
B(d(B)) + 1.
(2) T CM(B) = catB
B(d(B)) + 1.
Farber and Grant has also introduced lower bounds for the topological complex-
ity by using the cup length and category weight (see Rudyak [17, 18] for example)
on the ideal of zero-divisors, i.e, the kernel of ∆∗: H∗(B×B; R) →H∗(B; R).
Deﬁnition 1.8 (Farber [2] and Farber-Grant [4]). For a space B and a ring R ∋1,
the zero-divisors cup-length ZR(B) and the TC-weight wgtπ(u; R) for u ∈I =
ker ∆∗: H∗(B×B; R) →H∗(B; R) is deﬁned as follows.
(1) ZR(B) = Max {m≥0 H∗(B×B; R) ⊃Im ̸= 0}
(2) wgtπ(u; R) = Max {m≥0 ∀f : Y →B×B (secat(f ∗π) < m), f ∗(u) = 0}
In the category T B
B of ﬁbrewise pointed spaces with base space B and maps
between them, we also have corresponding deﬁnitions.
Deﬁnition 1.9. For a ﬁbrewise pointed space X over B and a ring R ∋1 and
u ∈I = H∗(X, B; R) ⊂H∗(X; R), we deﬁne
(1) cupB
B(X; R) = Max {m≥0 ∃{u1, · · ·, um ∈H∗(X, B; R)} s.t. u1· · ·um ̸= 0}
(2) wgtB
B(u; R) = Max
n
m≥0 ∀f : Y →X ∈T B
B (catB
B(f) < m), f ∗(u) = 0
o
This immediately implies the following.
Theorem 1.10. For a space B, we have ZR(B) = cupB
B(d(B); R) for a ring R ∋1.
Motivating by this equality, we proceed to obtain the following result.
Theorem 1.11. For any space B, any element u ∈H∗(B×B, ∆(B); R) and a ring
R ∋1, we have wgtπ(u; R) = wgtB
B(u; R).
Let us consider one technical condition on a ﬁbrewise pointed space:
Theorem 1.12. For any space B having the homotopy type of a locally ﬁnite sim-
plicial complex, we may assume that d(B) is ﬁbrewise well-pointed up to homotopy.
The following is the main result of our paper.
Theorem 1.13. For any ﬁbrewise well-pointed space X over B, we have catB
B(X) =
cat*
B(X). So, if B is a locally ﬁnite simplicial complex, we have T C(B) = T CM(B) =
catB
B(d(B)) + 1.
In [19], Sakai showed, in his study of the ﬁbrewise pointed L-S category of a
ﬁbrewise well-pointed spaces, using Whitehead style deﬁnition, that we can utilise
A∞methods used in the study of L-S category (see Iwase [7, 8]). Let us state the
Whitehead style deﬁnitions of ﬁbrewise L-S categories following [19].
Deﬁnition 1.14. Let X be a ﬁbrewise well-pointed space over B. The ﬁbrewise
pointed L-S category catB
B(X) is the minimal number m ≥0 such that the (m+1)-
fold ﬁbrewise diagonal ∆m+1
B
: X →
m+1
ΠB X is compressible into the ﬁbrewise fat
wedge
m+1
TB X in T B
B. If there are no such m, we say catB
B(X) = ∞.


## Page 9


4
IWASE AND SAKAI
We remark that this new deﬁnition coincides with the ordinary one, if the total
space X is a ﬁnite simplicial complex.
The above Whitehead-style deﬁnition allows us to deﬁne the module weight,
cone length and categorical length, and moreover, to give their relationship as in
Section 8. To show that, we need a criterion given by ﬁbrewise A∞structure on
the ﬁbrewise loop space (see Sections 6–7).
2. Proof of Theorem 1.7
First, we show the equality T CM(B) = catB
B(d(B))+1: assume T CM(B) = m+1,
m ≥0 and that there are an open cover Sm
i=0 Ui = B×B and a series of sections
si : Ui →P(B) of π : P(B) →d(B) satisfying si(b, b) = cb for b ∈B, since we are
considering monoidal topological complexity. Then each Ui is ﬁbrewise compressible
relative to ∆(B) into ∆(B) ⊂B×B = d(B) by a homotopy Hi : Ui×[0, 1] →B×B
given by the following:
Hi(a, b; t) = (si(a, b)(t), b),
(a, b) ∈Ui, t ∈[0, 1],
where we can easily check that Hi gives a ﬁbrewise compression of Ui relative to
∆(B) into ∆(B) ⊂B×B. Since S
i=0 Ui = B×B = d(B), we obtain catB
B(d(B)) ≤
m, and hence we have catB
B(d(B)) + 1 ≤T CM(B).
Conversely assume that catB
B(d(B)) = m, m ≥0 and there is an open cover
Sm
i=0 Ui = d(B) of d(B) = B×B where Ui is ﬁbrewise compressible relative to
∆(B) into ∆(B) ⊂d(B) = B×B: let us denote the compression homotopy of Ui
by Hi(a, b; t) = (σi(a, b; t), b) for (a, b) ∈Ui and t ∈[0, 1], where σi(a, b; 0) = a and
σi(a, b; 1) = b. Hence we can deﬁne a section si : Ui →P(B) by the formula
si(a, b)(t) = σi(a, b; t)
t ∈[0, 1].
Since S
i=0 Ui = B×B, we obtain T CM(B) ≤m+1 and hence we have T CM(B) ≤
catB
B(d(B)) + 1. Thus we have T CM(B) = catB
B(d(B)) + 1.
Second, we show the equality T C(B) = cat*
B(d(B)) + 1: assume T C(B) = m+1,
m ≥0 and that there is a open cover Sm
i=0 Ui = B×B and a section si : Ui →P(B)
of π : P(B) →d(B). Then each Ui is ﬁbrewise compressible into ∆(B) ⊂B×B =
d(B) by a homotopy Hi : Ui×[0, 1] →B×B which is given by
Hi(a, b; t) = (s(a, b)(t), b),
(a, b) ∈Ui, t ∈[0, 1],
where we can easily check that H gives a ﬁbrewise compression of Ui into ∆(B) ⊂
B×B = d(B). Since S
i=0 Ui = B×B = d(B), we obtain cat*
B(d(B)) ≤m, and
hence we have cat*
B(d(B)) + 1 ≤T C(B).
Conversely assume that cat*
B(d(B)) = m, m ≥0 and there is an open cover
Sm
i=0 Ui = d(B) of d(B) = B×B where Ui is ﬁbrewise compressible into ∆(B) ⊂
B×B = d(B): the compression homotopy is described as Hi(a, b; t) = (σi(a, b; t), b)
for (a, b) ∈Ui and t ∈[0, 1], such that σi(a, b; 0) = a and σi(a, b; 1) = b. Hence we
can deﬁne a section si : Ui →P(B) by the formula
si(a, b)(t) = σi(a, b; t)
t ∈[0, 1].
Since S
i=0 Ui = B×B, we obtain T C(B) ≤m+1 and hence we have T C(B) ≤
cat*
B(d(B)) + 1. Thus we have T C(B) = cat*
B(d(B)) + 1.
□


## Page 10


TOPOLOGICAL COMPLEXITY IS A FIBREWISE L-S CATEGORY
5
3. Proof of Theorem 1.11
Assume that wgtB
B(u; R) = m, where u ∈H∗(B×B, ∆(B)) and f : Y →d(B) =
B×B a map of secat(f ∗π) < m. Then there is an open cover Sm
i=1 Ui = Y and a
series of maps {σi : Ui →P(B) ; 1 ≤i ≤m} satisfying π◦σi = f|Ui. Let ˆY = Y ∐B
with projection p ˆY and section s ˆY given by
p ˆY |Y = pY ,
p ˆY |B = idB
and
s ˆY : B ֒→Y ∐B = ˆY .
Then we can extend f to a map ˆf : ˆY →d(B) by the formula
ˆf|Y = f,
ˆf|B = sd(B) = ∆.
By putting ˆUi = Ui ∐B which is open in ˆY , we obtain an open cover Sm
i=1 ˆUi = ˆY
and a series of maps ˆσi : ˆUi →P(B) satisfying π◦ˆσi = ˆf| ˆUi:
ˆσi|Ui = σi,
ˆσi|B = sP(B).
Hence there is a ﬁbrewise homotopy Φi : ˆUi×[0, 1] →d(B) such that Φi(y, 0) = ˆf(y)
and Φi(y, 1) ∈∆(B) given by the following formula.
Φi(y, t) = (ˆσi(y)(t), ˆσi(y)(1)),
(y, t) ∈ˆUi×[0, 1],
so that we have Φi(y, 0) = (ˆσi(y)(0), ˆσi(y)(1)) = π◦ˆσi(y) = ˆf(y) and Φi(y, 1) =
(ˆσi(y)(1), ˆσi(y)(1)) ∈∆(B). Moreover, for any (b, t) ∈B×[0, 1], we have Φi(b, t) =
(ˆσi(b)(t), ˆσi(b)(1)) = (sP(B)(t), sP(B)(1)) = (b, b). Thus Φi gives a ﬁbrewise pointed
compression homotopy of ˆf| ˆUi into ∆(B). Then it follows that catB
B( ˆf) < m and
hence we obtain f ∗(u) = 0 and wgtπ(u; R) ≥m. Thus we obtain wgtπ(u; R) ≥
m = wgtB
B(u; R).
Conversely assume that wgtπ(u; R) = m, where u ∈H∗(B×B, ∆(B)) and f :
Y →B×B such that catB
B(f) < m. Then there exists an open covering Sm
i=1 Ui = Y
with Ui ⊃sY (B) and a sequence of ﬁbrewise homotopies {φi : Ui×[0, 1] →B×B}
such that φi(y, 0) = f|Ui(y), φi(y, 1) ∈∆(B) and pr2◦φi(y, t) = pr2◦f(y) for
(y, t) ∈Ui×[0, 1]. Hence there is a sequence of maps {σi : Ui →P(B)} given by
σi(y)(t) = pr1◦φi(y, t),
y ∈Ui, t ∈[0, 1]
such that π◦σi(y) = (pr1◦φi(y, 0), pr1◦φi(y, 1)) = f(y) since pr2◦φi(y, t) = pr2◦f(y)
for (y, t) ∈Ui×[0, 1]. Thus we obtain secat(f ∗π) < m, and hence f ∗(u) = 0. This
implies wgtB
B(u; R) ≥m = wgtπ(u; R) and hence wgtB
B(u; R) = wgtπ(u; R).
□
4. Proof of Theorem 1.12
The proof of Lemma 2 in §2 of Milnor [16] implies the following:
Lemma 4.1. The pair (B×B, ∆(B)) is an NDR-pair.
Proof :
For each vertex β of B, let Vβ be the star neighbourhood in B and V =
S
β Vβ×Vβ ⊂B×B. Then the closure ¯V = S
β ¯Vβ× ¯Vβ is a subcomplex of B×B. For
the barycentric coordinates {ξβ} and {ηβ} of x and y, resp, we see that (x, y) ∈V
if and only if P
β Min(ξβ, ηβ) > 0 and that P
β Min(ξβ, ηβ) = 1 if and only if the
barycentric coordinates of x and y are the same, or equivalently, (x, y) ∈∆(B).
Hence we can deﬁne a continuous map v : B×B →[−1, 1] by the following formula.
v(x, y) =
(
2 P
β Min(ξβ, ηβ) −1,
if (x, y) ∈¯V ,
−1,
if (x, y) ̸∈V .


## Page 11


6
IWASE AND SAKAI
Then we have that v−1(1) = ∆(B). Let U = v−1((0, 1]) an open neighbourhood of
∆(B). Using Milnor’s map s, we obtain a pair of maps (u, h) as follows:
u(x, y) = Min{1, 1−v(x, y)}
and
h(x, y, t) = (s(x, y)(Min{t, w(x, y)}), y),
where w(x, y) = u(x, y) + v(x, y) = Min{1, 1+v(x, y)}. Note that w(x, y) = 1 if
(x, y) ∈U and that w(x, y) = 0 if (x, y) ̸∈V . Then u−1(0) = ∆(B), u−1([0, 1)) = U
and h(x, y, 1) = (y, y) ∈∆(B) if (x, y) ∈U. Moreover, pr2◦h(x, y, t) = y and
h(x, x, t) = (s(x, x)(t), x) = (x, x) for any x, y ∈B and t ∈[0, 1]. Thus the data
(u, h) gives the ﬁbrewise Strøm structure on (B×B, ∆(B)).
□
5. Proof of Theorem 1.13
Let X be a ﬁbrewise well-pointed space over B and ˆX the ﬁberwise pointed
space obtained from X by giving a ﬁbrewise whisker. More precisely, we deﬁne ˆX
be the mapping cylinder of sX,
ˆX = X ∪sX B×[0, 1],
X ∋sX(b) ∼(b, 0) ∈B×[0, 1] for any b ∈B,
with projection p ˆ
X and section s ˆ
X given by the formulas
p ˆ
X|X = pX,
p ˆ
X|B×[0,1](b, t) = b,
for (b, t) ∈B×[0, 1],
s ˆ
X(b) = (b, 1) ∈B×[0, 1] ⊂ˆX.
Then by the deﬁnition of Strøm structure, X is ﬁbrewise pointed homotopy equiv-
alent to ˆX the ﬁbrewise whiskered space over B. So we have catB
B(X) = catB
B( ˆX)
and cat*
B(X) = cat*
B( ˆX).
Assume that catB
B(X) = m ≥0. Then it is clear by deﬁnition that cat*
B(X) ≤
m = catB
B(X).
Conversely assume that cat*
B(X) = m ≥0.
Then there is an open cover
Sm
i=0 Ui = X such that Ui is compressible into sX(B) ⊂X. Hence there is a ﬁbre-
wise homotopy Φi : Ui×[0, 1] →X such that Φi(x, 0) = x, Φi(x, 1) = sX(pX(x))
and pX◦Φi(x, t) = pX(x). We deﬁne ˆUi as follows:
ˆUi = Ui ∪sX (sX)−1(Ui)×[0, 1] ∪B×(2
3, 1].
We also deﬁne a ﬁbrewise pointed homotopy ˆΦi : ˆUi×[0, 1] →ˆX as follows:
ˆΦi(ˆx, t) =

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

Φi(x, t),
ˆx = x ∈X,
Φi(sX(b), t−3s),
ˆx = (b, s) ∈(sX)−1(Ui)×(0, t
3),
sX(b),
ˆx = (b, t
3), b ∈(sX)−1(Ui),
(b, 6s−2t
6−3t ),
ˆx = (b, s) ∈(sX)−1(Ui)×( t
3, 2
3),
(b, 2
3),
ˆx = (b, 2
3), b ∈(sX)−1(Ui),
(b, s),
ˆx = (b, s) ∈B×( 2
3, 1].
It is then easy to see that ˆUi’s cover the entire X, and hence we have catB
B( ˆX) ≤
m = cat*
B(X).
Thus catB
B(X) ≤cat*
B(X) and hence catB
B(X) = cat*
B(X).
In
particular, we have T C(B) = T CM(B) for a locally ﬁnite simplicial complex B.
□


## Page 12


TOPOLOGICAL COMPLEXITY IS A FIBREWISE L-S CATEGORY
7
6. Fibrewise A∞structures
From now on, we work in the category T B
B. For any X a ﬁbrewise pointed space
over B, we denote by pX : X →B its projection and by sX : B →X its section.
We say that a pair (X, A) of ﬁbrewise pointed spaces over B is a ﬁbrewise NDR-
pair or that A is a ﬁbrewise NDR subset of X, if the inclusion map A ֒→X is a
ﬁbrewise coﬁbration, in other words, the inclusion has the ﬁbrewise (strong) Strøm
structure (see Crabb-James [1]). Since B is the zero object in T B
B, for any given
ﬁbrewise pointed space X over B, we always have a pair (X, B) in T B
B, where we
regard sX(B) = B. When the pair (X, B) is ﬁbrewise NDR, the space X is called
ﬁbrewise well-pointed.
Proposition 6.1 (Crabb-James [1]).
(1) If (X, A) and (X′, A′) are ﬁbrewise
NDR-pairs, then so is (X, A)×B(X′, A′) = (X×BX′, X×BA′∪A×BX′).
(2) If (X, A) is a ﬁbrewise NDR-pair, then so is (
m
ΠBX,
m
TB(X, A)), which is
deﬁned by induction for all m ≥1:
(
1
ΠBX,
1
TB(X, A)) = (X, A),
(
m+1
ΠB X,
m+1
TB (X, A)) = (
m
ΠBX,
m
TB(X, A))×B(X, A).
If X is a ﬁbrewise pointed space over B, then by taking A = B, we obtain a
ﬁbrewise subspace
m+1
TB (X, B) of
m+1
TB X, which is called an (m+1)-fold ﬁbrewise fat-
wedge of X, and is often denoted by
m+1
TB X. In addition, the pair (
m+1
ΠB X,
m+1
TB X) is
a ﬁbrewise NDR-pair for all m ≥0, if X is ﬁbrewise well-pointed.
Examples 6.2.
(1) Let X be a ﬁbrewise pointed space over B with pX = pr2 :
X = F×B →B the canonical projection to the second factor and sX =
in2 : B ֒→F×B = E the canonical inclusion to the second factor. Then X
is a ﬁbrewise pointed space over B.
(2) Let X = B×B, pX = pr2 : B×B →B the canonical projection to the
second factor and sX = ∆B : B ֒→B×B the diagonal.
Then X is a
ﬁbrewise pointed space over B.
(3) Let G be a topological group, EG the inﬁnite join of G with right G action
and BG = EG/G the classifying space of G. By considering G as a left
G space by the adjoint action, we obtain a ﬁbrewise pointed space X =
EG×GG with pX : EG×GG →BG with section sX : BG ֒→EG×G{e} ⊆
EG ×G G.
(4) Let B be a space, X = L(B) the space of free loops on B.
Then pX :
L(B) →B the evaluation map at 1 ∈S1 ⊂C is a ﬁbration with section
sX : B →L(B) given by the inclusion of constant loops. In view of Milnor’s
arguments, this example is homotopically equivalent to the example (3).
Deﬁnition 6.3. Let PB(X) =

ℓ: [0, 1] →X ∃b∈B s.t. ∀t∈[0,1] pX(ℓ(t))=b
	
the
ﬁbrewise free path space, LB(X) = {ℓ∈PB(X) ℓ(1)=ℓ(0)} the ﬁbrewise free loop
space and LB
B(X) = {ℓ∈PB(X) ℓ(1)=ℓ(0)=sX◦pX(ℓ(0))} the ﬁbrewise pointed loop
space. For any m ≥0, we deﬁne an A∞structure of LB
B(X) as follows.
(1) Em+1
B
(LB
B(X)) as the homotopy pull-back in T B
B of B ֒→
m+1
ΠB X ←֓
m+1
TB X,
(2) P m
B (LB
B(X)) as the homotopy pull-back in T B
B of X
∆m+1
B
−−−−→
m+1
ΠB X ←֓
m+1
TB X,


## Page 13


8
IWASE AND SAKAI
(3) eX
m : P m
B (LB
B(X)) →X as the induced map from the inclusion
m+1
TB X ֒→
m+1
ΠB X by the diagonal ∆m+1
B
: X →
m+1
ΠB X and
(4) pLB
B(X)
B
: Em+1
B
(LB
B(X)) →P m
B (LB
B(X)) as a map of ﬁbrewise pointed
spaces induced from the section sX : B →X, since the section B ֒→
m+1
ΠB X
is nothing but the composition ∆m+1
B
◦sX : B
s−→X
∆m+1
B
−−−−→
m+1
ΠB X.
We further investigate to understand an A∞stucture in a ﬁberwise view point,
using ﬁbrewise constructions.
Clearly, these constructions are not exactly the
Ganea-type ﬁbre-coﬁbre constructions but the following.
Proposition 6.4 (Sakai). Let X be a ﬁbrewise pointed space over B and m ≥0.
Then P m+1
B
(LB
B(X)) has the homotopy type of a push-out of pLB
B(X)
B
: Em+1
B
(LB
B(X))
→P m
B (LB
B(X)) and the projection Em+1
B
(LB
B(X)) →B.
This is a direct consequence of the following lemma.
Lemma 6.5. Let (X, A) and (X′, A′) be ﬁbrewise NDR-pairs of ﬁbrewise pointed
spaces over B and Z a ﬁbrewise pointed space over B with ﬁbrewise maps f : Z →X
and g : Z →X′.
Then the homotopy pull-back Ω(f,g),k of maps (f, g) : Z →
X×BX′ and k : X×BA′ ∪A×BX′ ֒→X×BX′ has naturally the homotopy type of
the reduced homotopy push-out W = Ωg,j ∪p2

Ω(f,g),i×j ∧B (B×J+)
	
∪p1 Ωf,i of
p1 : Ω(f,g),i×j →Ωf,i and p2 : Ω(f,g),i×j →Ωg,j, where J = [−1, 1] and
Ω(f,g),k =
n
(z, ℓ, ℓ′) ∈Z×B PB(X)×B PB(X′)
f(z)=ℓ(0), g(z)=ℓ′(0),
(ℓ(1),ℓ′(1))∈A×BX′∪X×BA′
o
,
Ω(f,g),i×j =

(z, ℓ, ℓ′) ∈Ω(f,g),k (ℓ(1), ℓ′(1)) ∈A×BA′	
,
Ωf,i = {(z, ℓ) ∈Z×B PB(X) f(z)=ℓ(0), ℓ(1)∈A} ,
Ωg,j = {(z, ℓ′) ∈Z×B PB(X′) g(z)=ℓ′(0), ℓ′(1)∈A′} ,
p1(z, ℓ, ℓ′) = (z, ℓ) and p2(z, ℓ, ℓ′) = (z, ℓ′).
Proof of Outline of the proof.
The proof of Lemma 6.5 is quite similar to that of
Theorem 1.1 in Sakai [20] (which is based on Iwase [7]) by replacing (Y, B) in [20]
by (X′, A′), deﬁning and using the following spaces.
c
W = Ω(f,g),i× idX′ ×{−1} ∪

Ω(f,g),i×j×J
	
∪Ω(f,g),idX ×j×{1} ⊂Ω(f,g),k×J,
Ω(f,g),idX ×j =

(z, ℓ, ℓ′) ∈Ω(f,g),k (ℓ(1), ℓ′(1)) ∈X×BA′	
,
Ω(f,g),i× idX′ =

(z, ℓ, ℓ′) ∈Ω(f,g),k (ℓ(1), ℓ′(1)) ∈A×BX′	
.
The precise construction of homotopy equivalences and homotopies is identical to
that in [20] and is left to the readers.
□
Theorem 6.6. Let X be a ﬁbrewise well-pointed space over B. Then the sequence
{pLB
B(X)
B
: Em+1
B
(LB
B(X)) →P m
B (LB
B(X))} gives a ﬁbrewise pointed version of A∞-
structure on the ﬁbrewise pointed loop space LB
B(X).
Thus in the case when X is a ﬁbrewise well-pointed space over B, we assume
that P m
B (LB
B(X)) is an increasing sequence given by homotopy push-outs with a
ﬁbrewise ﬁbration eX
m : P m
B (LB
B(X)) →X such that eX
1 : SB
B(LB
B(X)) →X is a
ﬁbrewise evaluation.


## Page 14


TOPOLOGICAL COMPLEXITY IS A FIBREWISE L-S CATEGORY
9
Examples 6.7.
(1) Let X be a ﬁbrewise pointed space over B with pX =
pr2 : F×B →B the canonical projection and sX = in2 : B ֒→F×B
the canonical inclusion. Then LB
B(X) = L(F)×B is given by pLB
B(X) =
pr2 : L(F)×B →B and sLB
B(X) = in2 : B ֒→L(F)×B.
(2) Let X = B×B be a ﬁbrewise pointed space over B with pX = pr2 : B×B →
B and sX = ∆B : B ֒→B×B the diagonal. Then LB
B(X) = L(B) the free
loop space on B, pLB
B(X) : L(B) →B the evalation map at 1 ∈S1 ⊂C and
sLB
B(X) : B ֒→L(B) the inclusion of constant loops.
Remark 6.8. When E is a cell-wise trivial ﬁbration on a polyhedron B (see [12]),
we can see that the canonical map eE
∞: P ∞
B (LB
B(E)) →E is a homotopy equivalence
by a similar arguments given in the proof of Theorem 2.9 of [12].
7. Fibrewise L-S categories of fibrewise pointed spaces
The ﬁbrewise pointed L-S category of an ﬁbrewise pointed space is ﬁrst deﬁned by
James and Morris [13] as the least number (minus one) of open subsets which cover
the given space and are contractible by a homotopy ﬁxing the base point in each ﬁbre
(see also James [14] and Crabb-James [1]) and is redeﬁned by Sakai in [19] as follows:
let X be a ﬁbrewise pointed space over B. For given k ≥0, we denote by
k+1
ΠBX
the (k+1)-fold ﬁbrewise product and by
k+1
TBX the (k+1)-fold ﬁbrewise fat wedge.
Then catB
B(X) ≤m if the (m+1)-fold ﬁbrewise diagonal map ∆m+1
B
: X →
m+1
ΠB X
is compressible into the ﬁbrewise fat wedge
m+1
TB X in T B
B. If there is no such m, we
say catB
B(X) = ∞. Let us consider the case when catB
B(X) < ∞. The deﬁnition of
a ﬁbrewise A∞structure yields the following criterion.
Theorem 7.1. Let X be a ﬁbrewise pointed space over B and m ≥0.
Then
catB
B(X) ≤m if and only if idX : X →X has a lift to P m
B (LB
B(X))
eX
m
→X in T B
B.
Proof :
If catB
B(X) ≤m, then the ﬁbrewise diagonal ∆m+1
B
: X →
m+1
ΠB X is com-
pressible into the ﬁbrewise fat wedge
m+1
TB X ⊂
m+1
ΠB X in T B
B. Hence there is a map
σ : X →P m
B (LB
B(X)) in T B
B such that eX
m◦σ ∼B 1X in T B
B. The converse is clear
by the deﬁnition of P m
B (LB
B(X)).
□
In the rest of this section, we work within the category T B of ﬁbrewise unpointed
spaces and maps between them. But we concentrate ourselves to consider its full
subcategory T ∗
B of all ﬁbrewise pointed spaces, so in T ∗
B, we have more maps than
in T B
B while we have just the same objects as in T B
B.
Let X be a ﬁbrewise pointed space over B. For given k ≥0, we denote by
k+1
ΠBX
the (k+1)-fold ﬁbrewise product and by
k+1
TBX the (k+1)-fold ﬁbrewise fat wedge.
Then cat*
B(X) ≤m if the (m+1)-fold ﬁbrewise diagonal map ∆m+1
B
: X →
m+1
ΠB X
is compressible into the ﬁbrewise fat wedge
m+1
TB X in T ∗
B. If there is no such m, we
say cat*
B(X) = ∞. Let us consider the case when cat*
B(X) < ∞. The deﬁnition of
a ﬁbrewise A∞structure yields the following.


## Page 15


10
IWASE AND SAKAI
Theorem 7.2. Let X be a ﬁbrewise pointed space over B and m ≥0.
Then
cat*
B(X) ≤m if and only if idX : X →X has a lift to P m
B (LB
B(X))
eX
m
→X in the
category T ∗
B.
Proof :
If cat*
B(X) ≤m, then the ﬁbrewise diagonal ∆m+1
B
: X →
m+1
ΠB X is com-
pressible into the ﬁbrewise fat wedge
m+1
TB X ⊂
m+1
ΠB X in T ∗
B. Hence there is a map
σ : X →P m
B (LB
B(X)) in T ∗
B such that eX
m◦σ ∼B 1X in T ∗
B. The converse is clear
by the deﬁnition of P m
B (LB
B(X)).
□
8. Upper and lower estimates
For X a ﬁbrewise pointed space over B, we deﬁne a ﬁbrewise version of Ganea’s
strong L-S category (see Ganea [6]) of X as CatB
B(X) and also a ﬁbrewise version
of Fox’s categorical length (see Fox [5] and Iwase [10]) of X as catlenB
B(X).
Deﬁnition 8.1. Let X be a ﬁbrewise pointed space over B.
(1) CatB
B(X) is the least number m ≥0 such that there exists a sequence
{(Xi, hi) hi : Ai→Xi−1, 0≤i≤m} of pairs of space and map satisfying X0 =
B and Xm ≃B X in T B
B with the following homotopy push-out diagrams:
Ai
B
Xi−1
Xi
✲
pAi
❄
hi
❄
sXi
✲
(2) catlenB
B(X) is the least number m ≥0 such that there exists a sequence
{Xi hi : Ai→Xi−1, 0≤i≤m} of spaces satisfying X0 = B and Xm ≃B X in
T B
B and that ∆B : Xi →Xi×BXi is compressible into Xi×BXi−1∪B×BXi
in Xm×BXm.
A lower bound for the ﬁbrewise L-S category of a ﬁbrewise pointed space X over
B can be described by a variant of cup length: since X is a ﬁbrewise pointed space
over B, there is a projection pX : X →B with its section sX : B →X. Hence we
can easily observe for any multiplicative cohomology theory h that
h∗(X) ∼= h∗(B)⊕h∗(X, B),
where we may identify h∗(X, B) with the ideal ker s∗
X : h∗(X) →h∗(B).
Deﬁnition 8.2. For a ﬁbrewise pointed space X over B and any multiplicative
cohomology theory h, we deﬁne
cupB
B(X; h) = Max {m≥0 ∃{u1, · · ·, um ∈h∗(X, B)} s.t. u1· · ·um ̸= 0} ,
cupB
B(X) = Max

cupB
B(X; h) h is a multiplicative cohomology theory
	
.
We often denote cupB
B( ; h) by cupB
B( ; R) when h∗( ) = H∗( ; R), where R is a
ring with unit.
Let us recall that the relationship between an A∞-structure and a Lusternik-
Schnirelmann category gives the key observation in [7, 8, 9].


## Page 16


TOPOLOGICAL COMPLEXITY IS A FIBREWISE L-S CATEGORY
11
On the other hand, Rudyak [17] and Strom [23] introduced a homotopy theo-
retical version of Fadell-Husseini’s category weight, which can be translated into our
setting as follows: for any ﬁbrewise pointed space X over B, let {pLB
B(X)
k
: Ek
B(LB
B(X))
→P k−1
B
(LB
B(X)) ; k≥1} be the ﬁbrewise A∞-structure of LB
B(X) in the sense of
Stasheﬀ[22] (see also [11] for some more properties). Let h be a generalisd coho-
mology theory.
Deﬁnition 8.3. For any u ∈h∗(X, B), we deﬁne
wgtB
B(u; h) = Min

m≥0
 (eX
m)∗(u) ̸= 0
	
,
where eX
m is the composition of ﬁbrewise maps P m
B (LB
B(X)) ֒→P ∞
B (LB
B(X))
eX
∞
−−→
≃B X.
Using this, we introduce some more invariants as follows.
Deﬁnition 8.4. For any ﬁbrewise pointed space X over B, we deﬁne
wgtπ(X; h) = Max {wgtπ(u; h) | u ∈h∗(X, B)} ,
wgtπ(X) = Max {wgtπ(X; h) h is a generalised cohomology theory} ,
wgtB
B(X; h) = Max

wgtB
B(u; h) | u ∈h∗(X, B)
	
,
wgtB
B(X) = Max

wgtB
B(X; h) h is a generalised cohomology theory
	
.
We often denote wgtπ( ; h) and wgtB
B( ; h) by wgtπ( ; R) and wgtB
B( ; R) respec-
tively when h∗( ) = H∗( ; R), where R is a ring with unit. We deﬁne versions of
module weight for a ﬁbrewise pointed space over B.
Deﬁnition 8.5. For a ﬁbrewise pointed space X over B, we deﬁne
(1) MwgtB
B(X; h) = Min

m≥0
 (eX
m)∗is a split mono of (unstable) h∗h-
modules

for
a generalisd cohomology theory h.
(2) MwgtB
B(X) = Max

MwgtB
B(X; h) h is a generalised cohomology theory
	
.
Then we immediately obtain the following result.
Theorem 8.6. For any ﬁbrewise pointed space X over B, we have
cupB
B(X) ≤wgtB
B(X) ≤MwgtB
B(X) ≤catB
B(X) ≤catlenB
B(X) ≤CatB
B(X).
By Lemma 4.1, we have the following as a corollary of Theorem 1.13.
Corollary 8.7. For any space B having the homotopy type of a locally ﬁnite sim-
plicial complex, we obtain
Zπ(B) ≤wgtπ(B) ≤MwgtB
B(d(B)) ≤T C(B)−1 ≤catlenB
B(d(B)) ≤CatB
B(d(B)).
9. Higher Hopf invariants
For any ﬁbrewise pointed map f : SB
B(V ) →X in T B
B, we have its adjoint
ad f : V →LB
B(X) such that
eX
1 ◦SB
B(ad f) = f : SB
B(V ) →X.
If catB
B(X) ≤m, then there is a ﬁbrewise pointed map σ : X →P m
B LB
B(X) in T B
B
such that
eX
1 ◦σ ≃B
B idX : X →X.


## Page 17


12
IWASE AND SAKAI
Hence both the ﬁbrewise maps eX
1 ◦(σ◦f) and eX
1 ◦SB
B(ad f) are ﬁbrewise pointed
homotopic to f in T B
B. Then we have
eX
1 ◦{SB
B(ad f) −(σ◦f)} ≃B
B ∗B,
where ≃B
B denotes the ﬁbrewise pointed homotopy and ∗B denotes the ﬁbrewise
trivial map in T B
B.
Thus there is a ﬁbrewise pointed map Hσ
m(f) : SB
B(V ) →
Em+1
B
LB
B(X) such that
pLB
B(X)
m
◦Hσ
m(f) ≃B
B SB
B(ad f) −(σ◦f).
Deﬁnition 9.1. Let X be of catB
B(X) ≤m, m ≥0. For f : SB
B(V ) →X, we deﬁne
(1) HB
m(f) =

Hσ
m(f) eX
1 ◦σ ≃B
B idX
	
⊂[SB
B(V ), X],
(2) HB
m(f) =

(SB
B)∞
∗Hσ
m(f) eX
1 ◦σ ≃B
B idX
	
⊂

SB
B(V ), X
	B
B,
where, for two ﬁbrewise spaces V and W, we denote by {V, W}B
B the homotopy set
of ﬁbrewise stable maps from V to W.
Appendix A. Fibrewise homotopy pull-backs and push-outs
In this paper, we are using A∞structures which is constructed using tools in T B
and T B
B — especially, ﬁnite homotopy limits and colimits, in other words, ﬁbrewise
homotopy pull-backs and push-outs in T B and T B
B. We show in this section that
such constructions are possible even when a ﬁbrewise space has some singular ﬁbres.
First we consider the ﬁbrewise homotopy pull-backs in T B
B: let X, Y , Z and E
be ﬁbrewise spaces over B and p : E →Z be a ﬁbrewise ﬁbration in T B. For any
ﬁbrewise map f : X →Z in T B, there exists a pull-back X
f ∗p
←−−f ∗E
ˆ
f−→E of
X
f−→Z
p
←−E as
f ∗E = {(x, e) ∈X×BE f(x) = p(e)}
a subspace of X×BE together with ﬁbrewise maps f ∗p : f ∗E →X and ˆf : f ∗E →
E given by restricting canonical projections:
(f ∗p)(x, e) = x,
ˆf(x, e) = e.
Theorem A.1 (Crabb-James [1]). Let p : E →Z be a ﬁbrewise ﬁbration. For any
ﬁbrewise map f : W →Z in T B, f ∗p : f ∗E →W is also a ﬁbrewise ﬁbration.
Let πt : PB(Z) →Z be ﬁbrewise ﬁbrations given by πt(ℓ) = ℓ(t), t = 0, 1 (see
also [1]). Then π0 and π1 induce a map π : PB(Z) →Z×BZ to the ﬁbre product
of two copies of pZ : Z →B.
Proposition A.2. π : PB(Z) →Z×BZ is a ﬁbrewise ﬁbration.
Proof :
For any ﬁbrewise map φ : W →PB(Z) and a ﬁbrewise homotopy H :
W×[0, 1] = W×B(IB) →Z×BZ such that H(w, 0) = π◦φ(w) for w ∈W, we


## Page 18


TOPOLOGICAL COMPLEXITY IS A FIBREWISE L-S CATEGORY
13
deﬁne a ﬁbrewise homotopy ˆH : W×[0, 1] = W×B(IB) →PB(Z)(⊂P(Z)) by
ˆH(w, s)(t) =
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

pr0◦H(w, s),
if t = 0,
pr0◦H(w, s−3t),
if 0 < t < s
3,
π0◦φ(w),
if t = s
3,
φ(w)( 3t−s
3−2s),
if s
3 < t < 3−s
3 ,
π1◦φ(w),
if t = 3−s
3 ,
pr1◦H(w, 3t−3+s),
if 3−s
3
< t < 1
pr1◦H(w, s),
if t = 0,
for (w, s) ∈W×BIB and t ∈[0, 1], where prk : Z×BZ ⊂Z×Z →Z denotes the
canonical projection given by prk(z0, z1) = zk, k = 0, 1 for any (z0, z1) ∈Z×BZ.
Then for any (w, s) ∈W×BIB, we clearly have
ˆH(w, 0)(t) = φ(w)(t),
t ∈[0, 1],
( ˆH(w, s)(0), ˆH(w, s)(1)) = (pr0◦H(w, s), pr1◦H(w, s)) = H(w, s),
and hence we have ˆH(w, 0) = φ(w) for any w ∈W and also π◦ˆH = H. This implies
that ˆH is a ﬁbrewise homotopy of φ covering H. Thus π is a ﬁbrewise ﬁbration.□
This yields the following corollary.
Corollary A.3. For any ﬁbrewise maps f : X →Z and g : Y →Z in T B, the
induced map (f×Bg)∗π : (f×Bg)∗PB(Z) →X×BY is a ﬁbrewise ﬁbration in T B.
We often call the ﬁbrewise space (f×Bg)∗PB(Z) together with the projections
prX◦(f×Bg)∗π : (f×Bg)∗PB(Z) →X and prY ◦(f×Bg)∗π : (f×Bg)∗PB(Z) →Y
the homotopy pull-back in T B of X
f−→Z
g←−Y .
We remark that the above
construction can be performed within T B
B if X, Y , Z, f and g are all in T B
B, so
that we have a pointed version of a ﬁbrewise homotopy pull-back:
Corollary A.4. For any ﬁbrewise maps f : X →Z and g : Y →Z in T B
B, the
induced map (f×Bg)∗π : (f×Bg)∗PB(Z) →X×BY is a ﬁbrewise ﬁbration in T B
B.
Second we consider the ﬁbrewise homotopy push-outs in T B
B: let X, Y , Z and W
be ﬁbrewise pointed spaces over B and i : Z →W be a ﬁbrewise coﬁbration in T B
B.
For any ﬁbrewise map f : Z →X over B, there exists a push-out X
f∗i
−−→f∗W
ˇf←−W
of X
f←−Z
i−→W as a quotient space of X∐BW by gluing f(z) with i(z) together
with ﬁbrewise maps f∗i and ˇf induced from the canonical inclusions.
Theorem A.5 (Crabb-James [1]). Let i : Z →W be a ﬁbrewise coﬁbration in T B
(or T B
B). For any ﬁbrewise map f : Z →X in T B (or T B
B, resp.), f∗i : X →f∗W
is also a ﬁbrewise coﬁbration in T B (or T B
B, resp.).
Let us recall that IB
B(Z) is obtained from IB(Z) = Z×B(B×[0, 1]) = Z×[0, 1]
by identifying the subspace sZ(B)×[0, 1] ⊂Z×[0, 1] with sZ(B) by the canonical
projection to the ﬁrst factor : sZ(B)×[0, 1] →sZ(B). Let ιt : Z →IB
B(Z) be
ﬁbrewise coﬁbration in T B
B given by ιt(z) = q(z, t), 0 ≤t ≤1, where q : Z×[0, 1] →
IB
B(Z) denotes the identiﬁcation map. Then ι0 and ι1 induce a map ι : Z∨BZ →
IB
B(Z) from Z∨BZ the push-out of two copies of sZ : B →Z.


## Page 19


14
IWASE AND SAKAI
Proposition A.6. ι : Z∨BZ →IB
B(Z) is a ﬁbrewise coﬁbration.
Proof :
For any ﬁbrewise map φ : IB
B(Z) →W and a ﬁbrewise homotopy H :
(Z∨BZ)×[0, 1] = (Z∨BZ)×BIB →W such that H(z, 0) = φ◦ι(z) for z ∈Z∨BZ,
we deﬁne a ﬁbrewise homotopy ˇH : IB
B(Z)×[0, 1] = IB
B(Z)×B(IB) →W by
ˇH(q(z, t), s) =

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

H(in0(z), s−3t),
if 0 ≤t < s
3,
φ◦ι0(z),
if t = s
3,
φ(q(z, 3t−s
3−2s)),
if s
3 < t < 3−s
3 ,
φ◦ι1(z),
if t = 3−s
3 ,
H(in1(z), 3t−3+s),
if 3−s
3
< t ≤1
for (q(z, t), s) ∈IB
B(Z)×BIB, where ink : Z ֒→Z∨BZ, k = 0, 1 denote the canonical
inclusion given by in0(z) = (z, ∗b) and in1(z) = (∗b, z), b = pZ(z) for any z ∈Z.
Then for any (q(z, t), s) ∈IB
B(Z)×BIB, we clearly have
ˇH(q(z, t))(0) = φ(q(z, t)),
ˇH(q(z, 0))(s) = H(in0(z), s),
ˇH(q(z, 1))(s) = H(in1(z), s),
and hence we have ˇH(q(z, t))(0) = φ(q(z, t)) for any q(z, t) ∈IB
B(Z) and also
ˇH◦(ι×B1IB) = H. This implies that ˇH is a ﬁbrewise homotopy of φ extending H.
Thus ι is a ﬁbrewise coﬁbration.
□
This yields the following corollary.
Corollary A.7. For any ﬁbrewise maps f : Z →X and g : Z →Y in T B
B, the
induced map (f∨Bg)∗ι : X∨BY →(f∨Bg)∗IB
B(Z) is a ﬁbrewise coﬁbration in T B
B.
We often call the ﬁbrewise space (f∨Bg)∗IB
B(Z) together with the inclusions
(f∨Bg)∗ι◦inX : X →(f∨Bg)∗IB
B(Z) and (f∨Bg)∗ι◦inY : Y →(f∨Bg)∗IB
B(Z) as
homotopy push-out in T B
B of X
f←−Z
g−→Y .
Quite similarly for a ﬁbrewise space Z in T B, we obtain a ﬁbrewise coﬁbration
ˆι : Z ∐Z = Z×{0} ∪Z×{1} ֒→Z×[0, 1] = IB(Z). Thus we have the following.
Corollary A.8. For any ﬁbrewise maps f : Z →X and g : Z →Y in T B, the
induced map (f∐g)∗ˆι : X∐Y →(f∐g)∗IB(Z) is a ﬁbrewise coﬁbration in T B.
Thus we also have an unpointed version of a ﬁbrewise homotopy push-out.
References
[1] M. C. Crabb. and I. M. James, “Fibrewise Homotopy Theory”, Springer Monographs in
Mathematics, Springer-Verlag London, Ltd., London, 1998.
[2] M. Farber, Topological complexity of motion planning, Discrete Comput. Geom. 29 (2003),
211–221.
[3] M. Farber, Topology of robot motion planning, “Morse theoretic methods in nonlinear analysis
and in symplectic topology”, 185–230, NATO Sci. Ser. II Math. Phys. Chem., 217, Springer,
Dordrecht, 2006.
[4] M. Farber and M. Grant, Symmetric Motion Planning, Topology and robotics, 85–104, Con-
temp. Math., 438, Amer. Math. Soc., Providence, RI, 2007.
[5] R. H. Fox, On the Lusternik-Schnirelmann category, Ann. of Math. (2) 42, (1941), 333–370.
[6] T. Ganea, Lusternik-Schnirelmann category and strong category, Illinois. J. Math. 11 (1967),
417–427.


## Page 20


TOPOLOGICAL COMPLEXITY IS A FIBREWISE L-S CATEGORY
15
[7] N. Iwase, Ganea’s conjecture on Lusternik-Schnirelmann category, Bull. Lon. Math. Soc., 30
(1998), 623–634.
[8] N. Iwase, A∞-method in Lusternik-Schnirelmann category, Topology 41 (2002), 695–723.
[9] N. Iwase, Lusternik-Schnirelmann category of a sphere-bundle over a sphere, Topology 42
(2003), 701–713.
[10] N. Iwase, Categorical length, relative L-S category and higher Hopf invariants, preprint.
[11] N. Iwase and M. Mimura, Higher homotopy associativity, Algebraic Topology, (Arcata CA
1986), Lect. Notes in Math. 1370, Springer Verlag, Berlin (1989) 193–220.
[12] N. Iwase and M. Sakai, Functors on the category of quasi-ﬁbrations, Topology Appl. 155
(2008), 1403–1409.
[13] I. M. James and J. R. Morris, Fibrewise category, Proc. Roy. Soc. Edinburgh. 119A (1991),
177–190.
[14] I. M. James, Introduction to ﬁbrewise homotopy theory, “Handbook of algebraic topology”,
169–194, North Holland, Amsterdam, 1995.
[15] I. M. James, Lusternik-Schnirelmann Category, “Handbook of algebraic topology”, 1293–
1310, North Holland, Amsterdam, 1995.
[16] J. Milnor, On Spaces Having the Homotopy Type of a CW -Complex, Trans. Amer. Math.
Soc. 90 (1959), 272–280.
[17] Y. B. Rudyak, On category weight and its applications, Topology 38 (1999), 37–55.
[18] Y. B. Rudyak, On analytical applications of stable homotopy (the Arnold conjecture, critical
points), Math. Z. 230(1999) 659–672.
[19] M. Sakai, The functor on the category of quasi-ﬁbrations, DSc Thesis (Kyushu University
1999), 1999.
[20] M. Sakai, A proof of the homotopy push-out and pull-back lemma, Proc. Amer. Math. Soc.
129 (2001), 2461–2466.
[21] A. S. Schwarz The genus of a ﬁber space, Amer. Math. Soc. Transl.(2) 55 (1966), 49–140.
[22] J. D. Stasheﬀ, Homotopy associativity of H-spaces, I, II, Trans. Amer. Math. Soc. 108 (1963),
275–292, 293–312.
[23] J. Strom, Essential category weight and phantom maps, Cohomological methods in homotopy
theory (Bellaterra, 1998), 409–415, Progr. Math., 196, Birkhauser, Basel, 2001.
[24] G. W. Whitehead, “Elements of Homotopy Theory”, Springer Verlag, Berlin, GTM series
61, 1978.
E-mail address: iwase@math.kyushu-u.ac.jp
E-mail address, Sakai: sakai@kurume-nct.ac.jp
(Iwase) Faculty of Mathematics, Kyushu University, Fukuoka 810-8560, Japan
(Sakai) Kurume National College of Technology, Fukuoka 830-8555, Japan.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
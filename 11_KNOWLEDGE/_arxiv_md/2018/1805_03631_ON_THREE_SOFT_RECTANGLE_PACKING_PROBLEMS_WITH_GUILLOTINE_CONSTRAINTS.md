---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1805.03631
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1805.03631_On_three_soft_rectangle_packing_problems_with_guillotine_constraints

> Source: 1805.03631_On_three_soft_rectangle_packing_problems_with_guillotine_constraints.pdf

> Pages: 22

---


## Page 1


arXiv:1805.03631v1  [math.OC]  9 May 2018
On three soft rectangle packing problems with guillotine
constraints
Quoc Trung Bui
Daily-Opt Joint Stock Company
trungbui@daily-opt.com
Thibaut Vidal
Departamento de Inform´atica, Pontif´ıcia Universidade Cat´olica do Rio de Janeiro
vidalt@inf.puc-rio.br
Minh Ho`ang H`a *
University of Engineering and Technology, Vietnam National University
minhhoang.ha@vnu.edu.vn
Abstract. We investigate how to partition a rectangular region of length L1 and height L2
into n rectangles of given areas (a1, . . . , an) using two-stage guillotine cuts, so as to minimize
either (i) the sum of the perimeters, (ii) the largest perimeter, or (iii) the maximum aspect
ratio of the rectangles. These problems play an important role in the ongoing Vietnamese land-
allocation reform, as well as in the optimization of matrix multiplication algorithms. We show
that the ﬁrst problem can be solved to optimality in O(n log n), while the two others are NP-
hard. We propose mixed integer programming (MIP) formulations and a binary search-based
approach for solving the NP-hard problems. Experimental analyses are conducted to compare
the solution approaches in terms of computational eﬃciency and solution quality, for diﬀerent
objectives.
Keywords.
Soft rectangle packing, guillotine constraints, complexity analysis, integer pro-
gramming.
1
Introduction
We consider a family of soft rectangle packing problems in which a rectangular region of
length L1 and height L2 must be partitioned into n rectangles of positive areas (a1, . . . , an),
where Pn
i=1 ai = L1 × L2. The areas of the rectangles are ﬁxed, and their position, length


## Page 2


and height constitute the decision variables of the problem.
Three diﬀerent objectives are
considered: minimizing the sum of the rectangle’s perimeters, the largest perimeter, or the
largest aspect ratio, leading to three problems called Col-Peri-Sum, Col-Peri-Max, and
Col-Aspect-Ratio respectively. Finally, the layout of the rectangles is subject to strict rules.
As illustrated in Figure 1, the rectangles should be delimited by two-stage guillotine cuts: ﬁrst
cutting the rectangular area horizontally to produce several layers (three on the ﬁgure), and
then cutting each layer vertically to obtain the rectangles (ten on the ﬁgure).
L1
L2
Figure 1: Partitioning the rectangular area by two-stage guillotine cuts – example solution.
Any solution of these problems can be described as a partition {S1, . . . , Sm} of the rectangle
set S = {1, . . . , n} into m layers. Since the length of each layer is ﬁxed to L1, the height w(Sk)
of a layer Sk (and therefore of all its contained rectangles) takes value
w(Sk) =
P
i∈Sk ai
L1
,
(1)
and the length of each rectangle i ∈Sk is ai/w(Sk). Based on this observation, the objective
of these problems is to ﬁnd {S1, . . . , Sm} so as to minimize:
Col-Peri-Sum:
Φ1 = 2 ×
m
X
k=1
X
i∈Sk

w(Sk) +
ai
w(Sk)

= 2 ×
m
X
k=1
(|Sk|w(Sk) + L1)
(2)
Col-Peri-Max:
Φ2 = 2 × max
k
max
i∈Sk

w(Sk) +
ai
w(Sk)

(3)
Col-Aspect-Ratio:
Φ3 = max
k
max
i∈Sk
max

ai
w(Sk)2 , w(Sk)2
ai

.
(4)
2


## Page 3


The main contribution of this paper is to characterize the computational complexity of these
problems, proposing an eﬃcient O(n log n) algorithm for Col-Peri-Sum, and demonstrating
that the two other problems are NP-hard. Moreover, we introduce mixed integer programming
(MIP) formulations for the NP-hard problems.
Finally, we conduct experimental analyzes
to determine the limit-size of the instances which can be eﬃciently solved, and compare the
solutions obtained with diﬀerent objectives.
2
Applications and related work
Land reform in Vietnam. Historically, the agricultural land of Vietnam has been classiﬁed
into several categories, and each household has been given one plot for each land category, such
that even a small agricultural ﬁeld can be distributed to many households.
These division
rules have been applied in most provinces of Vietnam to ensure equality among households.
However, this has led to a large fragmentation of the land in most provinces of Vietnam
(Sundqvist and Anderson 2006, Pham et al. 2007). In these provinces, each household owns
many small and scattered plots, located in diﬀerent ﬁelds. The province of Vinh Phuc is a
striking example: some households have up to 47 plots, and each plot has an average area of
only ten square meters (Journal of Rural Economy 2008).
The land fragmentation turned out to be detrimental in the industrialized era.
First,
households cannot use machines to cultivate small plots, leading to a high production cost.
Second, fragmented plots are costly to visit and maintain.
Third, the excessive number of
tracks separating the plots causes a waste of agricultural land (Heltberg 1998, Lam 2001,
General Statistical Oﬃce 2004, March and MacAulay 2006, Sundqvist and Anderson 2006). There-
fore, the Vietnamese government considers land fragmentation to be “a signiﬁcant barrier to
achieving further productivity gains in agriculture”, and initiated a land reform to deal with
the situation. This reform aims to reduce the number of land categories, to merge small plots
into large ﬁelds and ﬁnally to repartition these ﬁelds into larger plots for households. It has led
to successful results in some provinces, as characterized by a signiﬁcant increase in rice yield
attaining 25% in Quang Nam province (Sundqvist and Anderson 2006, Bui et al. 2013).
The land reform involves two critical tasks: merging small plots into larger ﬁelds, and
repartitioning these ﬁelds equitably while respecting the predeﬁned quantity of land attributed
to each household. In this study, we consider the case of rectangular ﬁelds, as this is the most
3


## Page 4


common in practice. The ﬁelds should be ﬁrst split by parallel edge-to-edge tracks to facilitate
the use of machines, and the resulting sections should then be separated into plots, leading to
the two-stage guillotine constraints discussed in the introduction of this paper.
Finally, farmers and local authorities may have distinct objectives and motivations. The
local authorities aim to minimize the amount of wasted land due to the creation of tracks, a
goal which is captured by the Col-Peri-Sum objective. In contrast, the farmers wish to have
their plots as square as possible to facilitate cultivation. To obtain equitable solutions, this
goal can be expressed as a worse-case optimization, leading to the Col-Peri-Max and Col-
Aspect-Ratio objectives. These objectives are not strongly conﬂicting, but they often lead
to diﬀerent land allocation decisions.
Land-consolidation strategies have been implemented in various other countries, e.g., in
Germany (Borgwardt et al. 2014, Brieden and Gritzmann 2004, Borgwardt et al. 2011), Turkey
(Cay et al. 2006, 2010, Cay and Uyan 2013, Hakli and Uuz 2017), Japan (Arimoto 2010), Cyprus
(Demetriou et al. 2013), China (Huang et al. 2011), and Brazil (Gliesch et al. 2017). However,
each country, depending on its own topology, culture, and practice has converged towards
a diﬀerent problem setting.
In particular, the two-stage guillotine-cut restrictions and the
objective functions relevant to the Vietnamese case have not yet been encountered in other
land-consolidation applications. Still, some related problems can be found in the operations
research and computer science literature, as discussed in the following.
Soft rectangle packing problems. Partitioning an area into polygons of ﬁxed shape or area
is a class of problems which has been regularly studied in the operations research and compu-
tational geometry literature. Beaumont et al. (2001, 2002) deﬁned two optimization problems
that seek to partition the unit square into a number of rectangles with given areas, so as to op-
timize parallel matrix-multiplication algorithms in heterogeneous parallel computing platforms.
The ﬁrst problem aims to minimize the sum of all rectangle perimeters, whereas the second
problem aims to minimize the largest perimeter. These problems are special cases of Peri-Sum
and Peri-Max where the general rectangular region is a square. The authors introduced an
7/4-approximate algorithm and an 2/
√
3-approximate algorithm for these problems, respectively.
Later on, Nagamochi and Abe (2007) considered the general Peri-Sum, Peri-Max and
Aspect-Ratio problems without guillotine constraints. They introduced an O(n log n)-time al-
4


## Page 5


gorithm which produces a 1.25-approximate solution for Peri-Sum, a 2/
√
3-approximate solution
for Peri-Max, and ﬁnds a solution with aspect ratio smaller than max{R, 3, 1 + max
i∈{1,...,n−1}
ai+1
ai }
for Aspect-Ratio where R denotes the aspect ratio of the original rectangular area. F¨ugenschuh et al.
(2014) also designed an 2/
√
3-approximate algorithm and a branch-and-cut algorithm for Peri-
Sum.
Other close variants of Peri-Sum have been studied. Kong et al. (1987, 1988) considered
the problem of decomposing a square or a rectangle into a number of rectangles of equal area so
as to minimize the maximum rectangle perimeter. VLSI ﬂoorplan design and facility location ap-
plications also led to a number of related studies (Young et al. 2001, Ji et al. 2017, Paes et al. 2017).
Ibaraki and Nakamura (2006) proposed a local search and mathematical programming algo-
rithm to solve rectangular packing problems where the shapes of the rectangles are adjustable
within given perimeter and area constraints.
Finally, Beaumont et al. (2002) considered Col-Peri-Sum and Col-Peri-Max as a build-
ing block to design approximation algorithms for Peri-Sum and Peri-Max when the general
rectangular region is a square.
The authors introduced an exact O(n2 log n) algorithm for
Col-Peri-Sum and two approximation algorithms for Col-Peri-Max. The complexity sta-
tus of Col-Peri-Max remained open. Moreover, Col-Aspect-ratio has not been studied
to this date. These methodological gaps along with the relevance of these problems for the
Vietnamese land reform are a strong motivation for additional research.
3
COL-PERI-SUM can be solved in O(n log n)
A polynomial-time algorithm in O(n2 log n) for Col-Peri-Sum was proposed in Beaumont et al.
(2002). In this section, we introduce a simple algorithm in O(n log n) for this problem. To that
extent, we show that after ordering the rectangles’ indices by non-decreasing area, the Col-
Peri-Sum problem can be reduced in O(n) to the concave least-weight subsequence problem
(CLWS), solvable to optimality in O(n) time (Wilber 1988).
Deﬁnition 1 (Concave real-value weight function). A real-value weight function w(i, j) deﬁned
for integers 0 ≤i < j ≤n is concave if and only if, for 0 ≤i0 < i1 < j0 < j1 ≤n,
w(i0, j0) + w(i1, j1) ≤w(i0, j1) + w(i1, j0).
5


## Page 6


Deﬁnition 2 (Concave least-weight subsequence problem). Let w(i, j) be a concave real-value
weight function deﬁned for integers 0 ≤i < j ≤n. Find an integer k ≥1 and a sequence of
integers 0 = l0 < l1 < · · · < lk−1 < lk = n such that Pk−1
i=0 w(li, li+1) is minimized.
To do this reduction, we ﬁrst assume that the indices of the rectangles have been ordered in
O(n log n) by non-decreasing area: a1 ≤· · · ≤an. We now highlight a property of Col-Peri-
Sum which allows to focus the search on a smaller subset of solutions.
Theorem 1. Consider a solution s of Col-Peri-Sum with cost Φ1(s), represented as a parti-
tion {S1, . . . , Sm} of the rectangle set. Let i ∈Sk and j ∈Sl be two rectangles from diﬀerent
subsets such that ai > aj. Any solution s′ obtained by swapping these two rectangles within
their respective subsets is such that:

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

Φ1(s′) < Φ1(s)
if |Sk| > |Sl|
Φ1(s′) = Φ1(s)
if |Sk| = |Sl|
Φ1(s′) > Φ1(s)
otherwise
Proof. Simply evaluate the cost diﬀerence using Equation (2):
∆= Φ1(s′) −Φ1(s)
= 2
L1

|Sk|

aj −ai +
X
x∈Sk
ax

+ |Sl|

ai −aj +
X
x∈Sl
ax

−|Sk|
X
x∈Sk
ax −|Sl|
X
x∈Sl
ax


= 2
L1
(|Sk| −|Sl|) (aj −ai).
This theorem deﬁnes some important features of the optimal solutions of Col-Peri-Sum:
• First, without loss of generality, any solution of Col-Peri-Sum can be presented in such a
way that |S1| ≥· · · ≥|Sm| (re-ordering the subsets according to their cardinality).
• With this representation, if k < l and |Sk| = |Sl|, there exists an optimal solution such that
ai ≤aj for all i ∈|Sk| and j ∈|Sl|.
• Finally, if k < l and |Sk| > |Sl|, all optimal solutions satisfy ai ≤aj for all i ∈|Sk| and j ∈|Sl|.
Following from these observations, there exists an optimal solution s∗= {S1, . . . , Sm} of Col-
Peri-Sum such that each Sk for k ∈{1, . . . , m} is a subsequence (of consecutive indices) of
the sequence ⟨a1, a2, . . . , an⟩. Therefore, we can ﬁnd an optimal solution of Col-Peri-Sum by
solving a least weight subsequence problem instance over the set of integers 0 ≤i < j ≤n with
6


## Page 7


the weight function:
wP(i, j) = 2
 
L1 + (j −i)
L1
j
X
k=i+1
ak
!
,
where wP(i, j) represents the sum of the perimeters of the rectangles of indices (i + 1, . . . , j)
when positioned in a single layer. Finally, Theorem 2 proves that this weight function is concave,
leading to an instance of CLWS.
Theorem 2. The weight function wP(i, j) is concave.
Proof. For 0 ≤i0 < i1 < j0 < j1 ≤n, one can directly verify that:
∆′ = w(i0, j1) + w(i1, j0) −w(i0, j0) −w(i1, j1)
= 2
L1
 
(j1 −i0)
j1
X
x=i0+1
ax + (j0 −i1)
j0
X
x=i1+1
ax −(j0 −i0)
j0
X
x=i0+1
ax −(j1 −i1)
j1
X
x=i1+1
ax
!
= 2
L1

(i1 −i0)
j1
X
x=j0+1
ax + (j1 −j0)
i1
X
x=i0+1
ax

> 0.
As a consequence, after prior ordering of the rectangles in O(n log n), an optimal solution of
Col-Peri-Sum can be found by solving an instance of CLWS, e.g., using the O(n) algorithm
of (Wilber 1988). Col-Peri-Sum can thus be solved in O(n log n) in the general case, and in
O(n) if the rectangles are ordered by non-decreasing (or non-increasing) area in the input.
4
NP-hardness results
In the previous section, we have seen that an eﬃcient O(n log n) algorithm can be designed for
Col-Peri-Sum. In contrast, we will show in the following that the “min-max” version of this
problem, Col-Peri-Max, as well as the Col-Aspect-Ratio problems are more diﬃcult.
Let Col-Peri-Max-Φ and Col-Aspect-Ratio-Φ be the decision problems in which one
must determine whether there exists a solution of value at most Φ for Col-Peri-Max, and
Col-Aspect-Ratio, respectively. We will show that these two problems are NP-complete, by
reduction from 2-Partition (Garey and Johnson 1990), hence establishing the NP-hardness
of Col-Peri-Max and Col-Aspect-Ratio.
7


## Page 8


Theorem 3. Col-Peri-Max-Φ is NP-complete.
Proof. In 2-Partition, we are given n positive integers c1, . . . , cn, and should determine
whether there is a partition S1 ∪S2 = {1, . . . , n}, S1 ∩S2 = ∅such that P
x∈S1 cx = P
x∈S2 cx.
Let cmax = maxi∈{1,...,n} ci, and consider the following Col-Peri-Max-Φ instance:
– a rectangular area of length L1 = 1
2
Pn
i=1 ci and height L2 = 2cmax;
– for i ∈{1, . . . , n}, rectangle i has an area ai = ci × cmax; and
– Φ = 4 × cmax.
Assume that 2-Partition is True: there exists a partition (S1, S2) such that P
x∈S1 cx =
P
x∈S2 cx. Consider a solution of Col-Peri-Max-Φ in which the set of rectangles has been
partitioned with (S1, S2) into two layers. Each layer has the same total area, forming a solution
in which all rectangles have one side of height L2
2 = cmax. With this conﬁguration, the rectangle
of largest area has the largest perimeter, equal to 4 × cmax = Φ, and thus Col-Peri-Max-
Φ is True.
Assume that the 2-Partition instance is False. Consider a solution of Col-Peri-Max,
and let Sk be the layer which contains the largest rectangle with area c2
max. The sum of areas
in Sk is diﬀerent from L1×L2
2
, and thus the height of this layer is diﬀerent from cmax. Hence,
the soft rectangle of area c2
max is not arranged as a square, its perimeter exceeds 4 × cmax, and
Col-Peri-Max-Φ is False.
Theorem 4. Col-Aspect-Ratio-Φ is NP-complete.
Proof. As previously, consider an instance of 2-Partition with n positive integers c1, . . . , cn.
Let C = Pn
i=1 ci and M =
2(C+1)2
mini∈{1,...,n} ci .
Deﬁne an instance of Col-Aspect-Ratio-Φ as
follows:
– a rectangular area of length L1 = M + 1
M + C
2 and height L2 = 2;
– n soft rectangles with areas c1, . . . , cn as well as two soft rectangles of area M and two soft
rectangles of area
1
M ; and
– Φ = M.
If 2-Partition is True, there exists a partition (S1, S2) such that P
x∈S1 cx = P
x∈S2 cx =
C
2 . We build a solution of Col-Aspect-Ratio with two layers containing the rectangles of
S1 and S2, respectively, as well as one pair of rectangles of area M and
1
M each. Each layer has
length M + 1
M + C
2 and height 1. In this conﬁguration, a maximum aspect ratio of M, is jointly
8


## Page 9


attained by the largest and smallest rectangles in each layer, and thus Col-Aspect-Ratio-Φ
is True.
Now, assume that 2-Partition is False, and discern three possible classes of solutions:
• Consider a solution of Col-Aspect-Ratio with one layer. The rectangle of size
1
M has
an aspect ratio of 4M, which exceeds Φ.
• Consider a solution of Col-Aspect-Ratio with two or more layers, where at least one
layer does not contain a rectangle of size M. Let c be the area of the largest element in
this layer. Two cases should be discerned:
– If c =
1
M , then the layer contains one or two small rectangles of area
1
M , and no
other rectangle.
The aspect ratio of one such rectangle can be computed as the
ratio of its length l1 ≥1
2(M + 1
M + C
2 ) over its height l2 ≤2 ×
2
M
2M+ 2
M +C . As such,
Φ ≥M ×
(M+ 1
M + C
2 )2
4
> M.
– Otherwise, there exists at least one rectangle ci in the layer, and the total area of
the layer does not exceed C +
2
M . The length l1 and height l2 of the rectangle of
area ci satisfy l1 ≥
ci
C+ 2
M × (M + 1
M + C
2 ) and l2 ≤2 ×
C+ 2
M
2M+ 2
M +C . As such,
Φ ≥ci(M + 1
M + C
2 )2
(C + 2
M )2
> minn
i=1ci × M2
(C + 1)2
= M.
• Finally, consider a solution of Col-Aspect-Ratio with two layers, where each layer con-
tains exactly one rectangle of size M. Since there is no feasible solution of 2-Partition,
the total areas of the layers are diﬀerent (the smaller rectangles cannot re-balance the
sum due to their small area 1/M). In the layer of smallest area, the rectangle of area M
has a length l1 > M and height l2 < 1, and thus an aspect ratio Φ = x
y > M.
In all cases, there is no solution with an aspect ratio smaller or equal to Φ, and thus Col-
Aspect-Ratio-Φ is False.
5
Mixed integer programming models
Since Col-Peri-Max and Col-Aspect-Ratio are NP-hard, this section proposes mixed in-
teger programming formulations of these problems, which can be solved to produce optimal
solutions for small and medium scale instances.
9


## Page 10


These models describe a solution with n layers in which some of the layers can be empty.
We associate one binary variable xik and one continuous variable wik for each rectangle i and
layer k. Variable xik takes value 1 if and only if rectangle i belongs to layer k, and variable wik
represents the length of the soft rectangle i when placed in layer k, and 0 otherwise. Finally,
each binary variable yk takes value 1 if layer k is non-empty, and 0 otherwise.
5.1
Formulation of COL-PERI-MAX
The mathematical formulation of Col-Peri-Max is given in Equations (5)–(17):
minimize Φ2
(5)
s.t. 2(L1 + L2)(xik −1) + 2

wik +
n
X
j=1
ajxjk
L1

≤Φ2
i, k ∈{1, . . . , n}
(6)
n
X
k=1
xik = 1
i ∈{1, . . . , n}
(7)
n
X
i=1
xik ≥yk
k ∈{1, . . . , n}
(8)
xik ≤yk
i, k ∈{1, . . . , n}
(9)
n
X
i=1
wik = L1yk
k ∈{1, . . . , n}
(10)
wik ≤L1xik
i, k ∈{1, . . . , n}
(11)
aixik ≤L2wik
i, k ∈{1, . . . , n}
(12)
ajwik −aiwjk ≤ajL1(2 −xik −xjk)
i, j, k ∈{1, . . . , n}, i ̸= j
(13)
aiwjk −ajwik ≤aiL1(2 −xik −xjk)
i, j, k ∈{1, . . . , n}, i ̸= j
(14)
xji ∈{0, 1}
i, j ∈{1, . . . , n}
(15)
wik ≥0
i, k ∈{1, . . . , n}
(16)
yk ∈{0, 1}
k ∈{1, . . . , n}
(17)
Φ2 ≥0
(18)
Constraints (7)–(9) ensure that every rectangle is included in a layer and that yk takes
value 1 when at least one rectangle is included in layer k. Constraints (10) state that the sum
of the length of the rectangles of each layer k equals L1 if this layer is used (yk = 1), and 0
10


## Page 11


otherwise. Constraints (11) and (12) impose that (wik = 0) ⇔(xik = 0). Finally, Constraints
(13) and (14) ensure that if two rectangles i and j are in the same layer k, then ai/wik = aj/wjk.
This formulation can be strengthened with the addition of some simple optimality cuts
which eliminate symmetrical solutions:
yk ≥yk+1
k ∈{1, . . . , n −1}
(19)
xik = 0
i ∈{1, . . . , n}, k ∈{i + 1, . . . , n}
(20)
The ﬁrst set of constraints forces the use of layers according to the order of their indices, while
the second set of constraints forces any rectangle i to belong to a layer of index k ∈{1, . . . , i}.
5.2
Formulation of COL-ASPECT-RATIO
The objective function Φ3 is nonlinear, and we did not ﬁnd a direct mixed integer programming
formulation of Col-Aspect-Ratio. Instead, we propose two alternative approaches to gener-
ate optimal solutions for this problem. The ﬁrst approach relies on a change of objective which
leads to a linear formulation returning the same optimal solutions as Col-Aspect-Ratio.
The second approach exploits the fact that the decision problem Col-Aspect-Ratio-Φ can
be formulated as a MIP. Solving this subproblem in a binary search allows to solve the original
optimization problem.
5.2.1
First approach – Change of objective function
We introduce an alternative objective function Φ4 for Col-Aspect-Ratio which can be mod-
eled in a linear formulation. This objective function can be computed as:
Φ4 = max
k
max
i∈Sk
|w(Sk) −
ai
w(Sk)|
√ai
.
(21)
The following lemma will be used to prove the equivalence between the two objectives:
Lemma 1. Given two soft rectangles i and j with side lengths (li, hi) and (lj, hj), we have
max(li, hi)
min(li, hi) ≥max(lj, hj)
min(lj, hj) ⇐⇒|li −hi|
√lihi
≥|lj −hj|
p
ljhj
.
11


## Page 12


Proof. Without loss of generality, we can assume that li ≥hi and lj ≥hj. Then,
max(li, hi)
min(li, hi) ≥max(lj, hj)
min(lj, hj)
⇐⇒
li
hi
≥lj
hj
⇐⇒
r
li
hi
≥
s
lj
hj
⇐⇒
 r
li
hi
−
s
lj
hj
! 
1 +
1
q
li
hi
lj
hj

≥0
⇐⇒
r
li
hi
−
r
hi
li
≥
s
lj
hj
−
s
hj
lj
⇐⇒li −hi
√lihi
≥lj −hj
p
ljhj
⇐⇒|li −hi|
√lihi
≥|lj −hj|
p
ljhj
Theorem 5.
Let s3 and s4 be two optimal solutions obtained with objectives Φ3 and Φ4,
respectively.
Then, Φ3(s3) = Φ3(s4), Φ4(s3) = Φ4(s4), and s3 and s4 are optimal for the
objectives Φ4 and Φ3, respectively.
Proof. For any solution s, as a consequence of Lemma 1, if Φ4(s) attains its minimum for a
rectangle i ∈{1, ..., n} of length li and height hi, then Φ3(s) attains its minimum for the same
rectangle, and vice-versa. Therefore Φ4(s) = |li−hi|
√lihi and Φ3(s) = max(li,hi)
min(li,hi) .
Now, assume that Φ4(s4) and Φ3(s3) attain their minimum for rectangles x and y, respectively.
Therefore,
Φ4(s4) = |lx −hx|
√lxhx
, Φ3(s4) = max(lx, hx)
min(lx, hx) ,
Φ4(s3) = |ly −hy|
p
lyhy
, Φ3(s3) = max(ly, hy)
min(ly, hy) .
Since s4 is an optimal solution for objective Φ4, Φ4(s4) ≤Φ4(s3) and:
|lx −hx|
√lxhx
≤|ly −hy|
p
lyhy
12


## Page 13


Therefore, as a consequence of Lemma 1, we have
max(lx, hx)
min(lx, hx) ≤max(ly, hy)
min(ly, hy)
Similarly, since s3 is an optimal solution for objective Φ3, Φ3(s3) ≤Φ3(s4) and:
max(ly, hy)
min(ly, hy) ≤max(lx, hx)
min(lx, hx)
Overall,
Φ3(s3) = max(ly, hy)
min(ly, hy) = max(lx, hx)
min(lx, hx) = Φ3(s4),
and s4 is an optimal solution for objective Φ3. A similar proof shows that s3 is an optimal
solution for objective Φ4.
Based on this change of objective function, Col-Aspect-Ratio can be formulated as:
min Φ
s.t. Constraints (7)–(15)
δik + L1(1 −xik) ≥wik −
n
X
j=1
ajxjk
L1
i, k ∈{1, . . . , n}
(22)
δik + L2(1 −xik) ≥−wik +
n
X
j=1
ajxjk
L1
i, k ∈{1, . . . , n}
(23)
Φ ≥δik
√ai
i, k ∈{1, . . . , n}
(24)
δk
i ≥0
i, k ∈{1, . . . , n}.
(25)
Solving this formulation to optimality generates an optimal solution of Col-Aspect-Ratio.
The value of this solution must be recomputed a-posteriori according to the original objective.
The model uses n2 additional continuous variables δik, as well as a continuous variable Φ
representing the value of the alternative objective function. According to Constraints (22) and
(23), if a rectangle i is in layer Sk, then δik = |li −hi| where li and hi represent the length and
height of the rectangle in the current solution, otherwise δik = 0.
13


## Page 14


5.2.2
Second approach – Binary search
Another solution approach consists in modeling the decision problem Col-Aspect-Ratio-Φ
as a MIP. In this case, a maximum aspect ratio Φ is set as a constraint, and the goal is to ﬁnd
a feasible solution. The feasibility model can be written as follows:
Constraints (7)–(15)
L1hk =
n
X
i=1
aixik
k ∈{1, . . . , n}
(26)
wik ≤Φhk
i, k ∈{1, . . . , n}
(27)
hk ≤Φwik
i, k ∈{1, . . . , n}
(28)
hk ∈R
k ∈{1, . . . , n}
(29)
In this model, each variable hk for k ∈{1, . . . , n} stores the height of layer Sk, and Con-
straints (27)–(28) force the aspect ratio to be no higher than Φ. To solve the original opti-
mization problem, we do a binary search over Φ and solve Col-Aspect-Ratio-Φ at each step.
The starting interval is set to [Φlow, Φup] where Φlow = 1 and Φup = Φ3(s1), where s1 is an
optimal solution of Col-Peri-Sum found in O(n log n) time. The binary search stops as soon
as Φup −Φlow < 0.01.
6
Computational Experiments
To complete the theoretical results of this article, we conducted computational experiments
to evaluate the eﬃciency of the solution methods for the three problems and compare their
solutions. All algorithms were implemented in C++ and the mathematical models were solved
with CPLEX version 12.4. The experiments were performed on a single thread of an Intel i7-
3615QM 2.3 GHz CPU with 10GB RAM, running Mac OS Sierra version 10.12.6, and subject
to a CPU time limit of one hour for each run.
We randomly generated benchmark instances with n ∈{10, 15, 20, 25, 30, 35, 40} soft rect-
angles. These instances are subdivided into three classes, and three instances were generated
for each class and size for a total of 63 instances.
• Class U – The area of each item is sampled in a uniform distribution: X ∼U(1, 200).
14


## Page 15


• Class MU – The area of each item is sampled in a mixture of three uniform distributions:
X ∼1
3 [U(1, 10) + U(11, 50) + U(51, 150)].
• Class MN – The area of each item is sampled in a mixture of three normal distributions:
X ∼1
3 [N(5, 2) + N(25, 10) + N(125, 50)], but another sample is taken whenever the area
is larger than 200.
Finally, the dimensions of the hard rectangle are generated as follows for each instance. Let A
be the sum of the areas of the soft rectangles.
Length L1 is randomly generated with uni-
form probability in {⌈
p
A/3⌉, . . . , ⌊
√
3A⌋}. The length of the other side is set to L2 = ⌊A/L1⌋.
Then, A −L1L2 soft rectangles are randomly selected, and the area of each rectangle is re-
duced by one unit in such a way that, after reduction, the area of the hard rectangle coincides
with the sum of the areas of the soft rectangles.
All benchmark instances are available at
https://w1.cirrelt.ca/~vidalt/en/research-data.html.
6.1
Performance analysis
This section compares the CPU time needed to solve Col-Peri-Sum, Col-Peri-Max, and
Col-Aspect-Ratio. As expected, the solution of Col-Peri-Sum in O(n log n) is extremely
fast, with a measured CPU time of the order of a few milliseconds for all considered instances,
such that we concentrate our analyzes on the mathematical programming algorithm for Col-
Peri-Max as well as the reformulation and binary search approaches for Col-Aspect-Ratio.
To speed up the solution methods, we always generate the optimal solution of Col-Peri-Sum
and use it as an initial feasible solution.
Tables 1 to 3 report, for each instance class and algorithm, the number of nodes in the search
tree (Nodes), the CPU time in seconds (Time), as well as the best found lower bound (LB) and
upper bound (UB). For the reformulation-based approach for Col-Aspect-Ratio, columns
LB4 and UB4 correspond to objective Φ4, and the value of the primal solution for objective
Φ3 is indicated in column UB3. TL in column Time means that the CPU time limit of 3600
seconds has been attained. Finally, for the binary search approach for Col-Aspect-Ratio,
we indicate the number of completed iterations in column ItBS.
As observed in these experiments, the proposed MIP models can be solved to optimality
for all benchmark instances with 10 soft rectangles, as well as a few instances with up to 30
rectangles for Col-Peri-Max and 40 rectangles for Col-Aspect-Ratio. Yet, the number of
15


## Page 16


Table 1: Class U – Performance comparisons
Data
Col-Peri-Max
Col-Aspect-Ratio – Reformulation
Col-Aspect-Ratio – B. Search
#
Size
Nodes
Time
LB
UB
Nodes
Time
LB4
UB4
UB3
ItBS
Time
LB
UB
p01
10
547
0.53
52.53
52.53
176
0.39
0.95
0.95
2.51
8
1.21
2.51
2.51
p02
10
27
0.20
55.17
55.17
68
0.22
1.72
1.72
4.75
10
1.38
4.75
4.75
p03
10
101
0.20
55.54
55.54
1
0.08
1.05
1.05
2.73
8
0.93
2.72
2.73
p04
15
5139k
TL
52.27
55.14
69
0.74
0.82
0.82
2.22
8
4.91
2.22
2.22
p05
15
38k
92.46
51.38
51.38
193
1.85
0.99
0.99
2.59
9
4.27
2.59
2.60
p06
15
8054k
TL
48.63
52.46
640k
479.41
1.98
1.98
5.76
10
560.23
5.75
5.76
p07
20
351k
TL
43.27
56.57
308
3.38
2.60
2.60
8.64
12
29.04
8.63
8.64
p08
20
2993k
TL
34.76
56.14
79k
202.12
0.47
0.47
1.59
7
174.54
1.59
1.59
p09
20
92
3.37
53.71
53.71
3k
12.31
1.46
1.46
3.86
9
35.94
3.85
3.86
p10
25
479k
TL
49.00
55.86
80k
851.98
0.74
0.74
2.07
8
679.89
2.06
2.07
p11
25
935k
TL
45.82
55.14
116
12.37
1.60
1.60
4.33
7
TL
4.29
4.37
p12
25
601k
TL
33.01
53.96
393k
TL
0.81
1.01
2.65
2
TL
2.62
4.25
p13
30
335k
TL
25.86
54.70
293k
TL
0.00
0.86
2.30
2
TL
2.20
3.41
p14
30
318k
TL
40.41
54.11
179k
TL
0.22
1.79
5.01
3
TL
1.00
7.22
p15
30
182k
TL
33.64
53.37
328k
TL
1.71
2.59
8.57
3
TL
1.00
17.06
p16
35
389k
TL
40.00
56.43
714k
TL
0.00
1.79
5.00
2
TL
1.00
5.34
p17
35
247k
TL
36.01
56.43
150k
TL
0.00
1.47
3.92
0
TL
1.00
8.34
p18
35
109k
TL
41.35
55.71
149k
TL
0.34
2.59
8.58
1
TL
1.00
28.70
p19
40
74k
TL
19.30
56.43
108k
TL
0.64
1.42
3.76
1
TL
1.00
5.86
p20
40
101k
TL
44.48
54.79
54k
TL
0.12
1.09
2.83
1
TL
1.93
2.86
p21
40
53k
TL
44.12
56.14
68k
TL
0.05
2.73
9.35
2
TL
1.00
21.33
Table 2: Class MU – Performance comparisons
Data
Col-Peri-Max
Col-Aspect-Ratio – Reformulation
Col-Aspect-Ratio – B. Search
#
Size
Nodes
Time
LB
UB
Nodes
Time
LB4
UB4
UB3
ItBS
Time
LB
UB
p01
10
179
0.31
55.29
55.29
17
0.24
1.39
1.39
3.65
9
1.03
3.64
3.65
p02
10
44
0.07
55.78
55.78
214
0.18
1.36
1.36
3.57
9
1.38
3.56
3.57
p03
10
4k
1.22
52.76
52.76
64
0.18
1.97
1.97
5.71
9
0.72
5.70
5.71
p04
15
1
0.49
56.17
56.17
720
1.67
2.20
2.20
6.67
11
12.05
6.66
6.67
p05
15
6938k
TL
43.43
51.23
294k
280.22
1.36
1.36
3.57
9
451.13
3.56
3.57
p06
15
185k
111.49
54.70
54.70
314
1.87
2.13
2.13
6.39
10
8.82
6.39
6.39
p07
20
1943k
TL
40.10
55.86
475k
1885.98
2.09
2.09
6.19
10
1450.33
6.19
6.19
p08
20
2223k
TL
28.26
53.81
1787k
TL
0.95
1.05
2.74
2
TL
2.69
4.38
p09
20
66k
285.98
55.86
55.86
142k
550.19
2.18
2.18
6.61
12
2355.92
6.61
6.61
p10
25
688k
TL
40.79
55.71
281k
TL
0.76
1.33
3.48
3
TL
2.98
3.96
p11
25
169k
TL
51.08
54.85
220k
TL
1.47
2.24
6.86
2
TL
1.00
12.49
p12
25
331k
TL
47.41
56.17
225k
TL
1.77
2.13
6.39
5
TL
5.72
6.66
p13
30
325k
TL
21.43
53.07
318k
TL
0.61
1.40
3.68
1
TL
1.00
7.02
p14
30
196k
TL
42.46
55.43
176k
TL
1.28
1.96
5.67
2
TL
3.69
6.38
p15
30
267k
TL
32.40
55.43
150k
TL
0.91
1.86
5.27
2
TL
1.00
7.10
p16
35
115k
TL
41.47
55.86
62k
TL
0.27
2.06
6.09
1
TL
4.94
8.89
p17
35
250k
TL
23.28
44.36
5k
297.25
1.39
1.39
3.67
9
471.57
3.67
3.67
p18
35
226k
TL
32.23
55.28
143k
TL
0.04
1.96
5.68
1
TL
1.00
7.20
p19
40
204k
TL
21.41
54.70
7k
181.11
1.48
1.48
3.92
4
TL
3.87
4.08
p20
40
290k
TL
29.09
56.00
72k
TL
0.11
1.53
4.11
3
TL
3.88
5.32
p21
40
154k
TL
15.76
52.76
75k
TL
0.00
1.30
3.39
0
TL
1.00
4.60
16


## Page 17


Table 3: Class MN – Performance comparisons
Data
Col-Peri-Max
Col-Aspect-Ratio – Reformulation
Col-Aspect-Ratio – B. Search
#
Size
Nodes
Time
LB
UB
Nodes
Time
LB4
UB4
UB3
ItBS
Time
LB
UB
p01
10
386
0.31
50.83
50.83
10
0.27
1.05
1.05
2.75
9
0.87
2.74
2.75
p02
10
62
0.10
51.50
51.50
1
0.06
0.82
0.82
2.22
7
0.41
2.21
2.22
p03
10
267
0.27
51.00
51.00
33
0.28
1.94
1.94
5.60
9
0.75
5.59
5.60
p04
15
38k
20.37
39.80
39.80
13k
18.08
1.55
1.55
4.17
9
147.71
4.17
4.17
p05
15
130k
94.84
40.99
40.99
2k
5.06
1.03
1.03
2.68
8
20.51
2.67
2.68
p06
15
4971k
TL
44.67
45.96
27
0.86
1.65
1.65
4.49
9
5.18
4.49
4.50
p07
20
364
9.13
53.17
53.17
23k
200.99
2.82
2.82
9.83
11
2866.39
9.83
9.83
p08
20
6k
35.00
53.38
53.38
31k
484.53
2.06
2.06
6.09
10
259.48
6.08
6.09
p09
20
1427k
TL
36.61
54.55
59k
290.84
1.05
1.05
2.73
8
554.92
2.73
2.73
p10
25
2188k
TL
29.04
43.08
987k
TL
0.56
0.67
1.94
4
TL
1.76
1.95
p11
25
233k
TL
40.91
54.55
156
11.20
2.49
2.49
8.09
10
76.60
8.08
8.09
p12
25
1341k
1699.02
53.67
53.67
429k
TL
0.55
0.93
2.45
8
661.27
2.44
2.45
p13
30
7k
139.13
54.12
54.12
285k
TL
1.39
2.08
6.18
5
TL
5.47
6.21
p14
30
843k
TL
35.00
54.41
316k
TL
0.80
1.18
3.06
2
TL
2.28
3.55
p15
30
3k
42.77
51.23
51.23
105k
TL
1.85
2.81
9.81
2
TL
6.85
12.69
p16
35
113k
TL
39.18
55.43
87k
TL
0.14
1.82
5.12
1
TL
1.00
14.14
p17
35
1526k
TL
40.41
53.33
272k
TL
0.14
0.56
1.73
2
TL
1.55
1.74
p18
35
169k
TL
44.24
52.57
80k
TL
0.55
1.91
5.48
1
TL
1.00
9.88
p19
40
137k
TL
34.26
56.43
49k
TL
0.59
1.93
5.53
0
TL
1.00
6.92
p20
40
294k
TL
30.57
55.28
251k
TL
0.84
1.00
2.62
3
TL
2.31
2.64
p21
40
141k
TL
9.94
54.55
137k
TL
1.09
1.71
4.70
0
TL
1.00
5.09
search nodes and CPU time grow very quickly with the number of soft rectangles n. Despite
the symmetry-breaking inequalities, some instances with 15 rectangles lead to over a million
search nodes. The reformulation approach and the binary search approach for Col-Aspect-
Ratio ﬁnd 31/63 and 30/63 optimal solutions, respectively. The reformulation approach is
generally faster than the binary search algorithm for small instances. Yet, a drawback of this
algorithm is that it searches for an optimal solution according to objective Φ4. When optimality
is attained, this solution is optimal for Φ3 due to Theorem 5. When an optimality gap remains,
the primal solution obtained from the algorithm gives a valid upper bound for objective Φ3,
but the dual information (and performance guarantee) is lost. Finally, we did not observe a
signiﬁcant diﬀerence of performance when comparing the results of the three instance classes
(U,MU and MN). We noted that two larger instances with 35 and 40 rectangles were solved
to optimality for class MU, a phenomenon which did not happen for U and MN.
In general, the diﬃculties encountered when solving instances with 10 to 40 rectangles
already show the limitations of available mathematical programming algorithms for Col-Peri-
Max and Col-Aspect-Ratio. Future progress on exact approaches for NP-hard problems
17


## Page 18


may allow to solve larger instances in the future, but years of research may be needed before
handling more realistic instances with over a hundred rectangles.
Alternatively, heuristics
and metaheuristics could be used to solve larger problems.
As we noted a complexity gap
between Col-Peri-Sum and the other two problems, in spite of the relations between the
three objectives, we are interested to see if the solution of Col-Peri-Sum can constitute a
viable heuristic for the two more diﬃcult objectives. This is the focus of the next section.
6.2
Solution evaluations in relation to other objectives
The objective functions of the three considered problems are diﬀerent but not strongly con-
ﬂicting.
Yet, Col-Peri-Sum can be solved in O(n log n), while Col-Peri-Max and Col-
Aspect-Ratio are NP-hard. In this last analysis, we investigate how close these problems
are from each other in practice. This is achieved by evaluating the optimal solution of one
problem according to the objective function of each other. In particular, we are interested to
see if the solution of Col-Peri-Sum can be used as a simple heuristic for Col-Peri-Max and
Col-Aspect-Ratio.
For this analysis, we gathered all instances that are solved to optimality for all three prob-
lems: all instances with n = 10; instances U-p05, MU-p04, MU-p06, MN-p04, and MN-p05
with n = 15; and instances U-p09, MU-p09, MN-p07, and MN-p08 with n = 20. For each
objective Φx, we evaluated the quality Φy(s∗
x) of its optimal solution s∗
x relatively to each other
objective y ∈{1, 2, 3}, and report the results as the performance ratio Φy(s∗
x)/Φy(s∗
y) in Table 4.
These experiments ﬁrst conﬁrm the fact that the three objectives produce signiﬁcantly
diﬀerent solutions. For these instances, the optimal solutions of Col-Peri-Sum are within an
average factor of 1.05 of the optimal solutions of Col-Peri-Max when evaluated according to
objective Φ2, and are better than the optimal solutions of Col-Aspect-Ratio with a factor
of 1.11. Similarly, the optimal solutions of Col-Peri-Sum give a better approximation of the
optimal solutions of Col-Aspect-Ratio than the optimal solutions of Col-Peri-Max (with
a factor of 1.50 compared to 14.01).
One likely explanation of these observations is that the objective of Col-Peri-Max mainly
concentrates the optimization on rectangles of large area, so as to minimize their perimeter.
In Col-Peri-Max, small rectangles almost never play a role as they are unlikely to realize
the maximum.
In Col-Aspect-Ratio, in contrast, small and large rectangles are equally
18


## Page 19


Table 4: Optimal solutions for one objective evaluated according to the other objectives
Evaluated as
Col-Peri-Sum – Φ1
Col-Peri-Max – Φ2
Col-Aspect-Ratio – Φ3
Solved as
Φ1
Φ2
Φ3
Φ1
Φ2
Φ3
Φ1
Φ2
Φ3
MN-p01
1.00
1.30
1.00
1.12
1.00
1.07
1.60
13.09
1.00
MN-p02
1.00
1.11
1.00
1.00
1.00
1.00
1.00
22.02
1.00
MN-p03
1.00
1.55
1.00
1.04
1.00
1.04
1.00
12.86
1.00
U-p01
1.00
1.06
1.00
1.08
1.00
1.09
1.01
4.27
1.00
U-p02
1.00
1.00
1.13
1.00
1.00
1.31
1.60
1.60
1.00
U-p03
1.00
1.00
1.00
1.00
1.00
1.00
1.00
1.00
1.00
MU-p01
1.00
1.23
1.05
1.05
1.00
1.13
1.07
5.97
1.00
MU-p02
1.00
1.06
1.01
1.00
1.00
1.00
1.00
22.69
1.00
MU-p03
1.00
1.19
1.00
1.05
1.00
1.05
1.00
7.09
1.00
MN-p04
1.00
1.41
1.08
1.00
1.00
1.09
1.08
38.85
1.00
MN-p05
1.00
1.24
1.02
1.00
1.00
1.04
1.00
9.76
1.00
U-p05
1.00
1.04
1.02
1.01
1.00
1.03
1.67
2.31
1.00
MU-p04
1.00
1.11
1.02
1.13
1.00
1.06
2.24
21.59
1.00
MU-p06
1.00
1.27
1.01
1.00
1.00
1.00
1.24
29.31
1.00
MN-p07
1.00
1.15
1.25
1.24
1.00
1.55
1.16
14.65
1.00
MN-p08
1.00
1.23
1.14
1.15
1.00
1.33
1.22
9.31
1.00
U-p09
1.00
1.06
1.00
1.06
1.00
1.10
1.37
6.35
1.00
MU-p09
1.00
1.24
1.04
1.00
1.00
1.07
5.74
29.47
1.00
Average
1.00
1.18
1.04
1.05
1.00
1.11
1.50
14.01
1.00
important, since the maximum aspect ratio can be attained regardless of the rectangle area.
Finally, Col-Peri-Sum must optimize the perimeter of all rectangles, regardless of their area,
so as to minimize the total sum. This objective leads to optimal solutions which tend to have
good overall aspect ratios, regardless of rectangle size.
Finally, a precise analysis of the solutions shows that Col-Peri-Sum produced ﬁve opti-
mal solutions for Col-Peri-Max and six optimal solutions for Col-Aspect-Ratio over 18
instances.
In one exceptional case (instance p03 of class U), the three methods converged
towards the same optimal solution. This situation happened because the optimal solution con-
tained a single layer, but other situations can lead to this behavior: e.g., if a feasible solution
exists in which all soft rectangles take the shape of a square, then this solution is indeed optimal
for the three objectives.
7
Conclusions
In this paper, we investigated three soft rectangle packing problems: Col-Peri-Sum, Col-
Peri-Max and Col-Aspect-Ratio. The eﬀective resolution of these problems is of foremost
19


## Page 20


importance for the ongoing land-allocation reform in Vietnam. The objectives considered in
these problems model diﬀerent aspects of fairness and wasted-land minimization. We introduced
an O(n log n) exact algorithm for Col-Peri-Sum. Then, we demonstrated that the two others
problems are NP-hard, and proposed compact MIP formulations to solve them. In the case of
Col-Aspect-Ratio, an objective reformulation and a binary search scheme were proposed to
overcome non-linearities. Through a set of experimental analyzes on 63 benchmark instances,
we observed that the resolution of the MIP formulations is currently practicable for problem
instances involving 10 to 40 soft rectangles. To solve larger instances of Col-Peri-Max and
Col-Aspect-Ratio, we may use the O(n log n)-time algorithm for Col-Peri-Sum as a simple
heuristic.
The research perspectives are numerous. The proposed MIP formulations can possibly be
improved with additional valid inequalities or optimality cuts, and the set-partitioning formula-
tion of the problem can certainly be exploited to develop eﬃcient branch-and-price algorithms.
Metaheuristics could also be developed to provide solutions for larger instances or integrate ad-
ditional restrictions or objectives. Finally, whether Col-Peri-Max and Col-Aspect-Ratio
are strongly NP-hard remains an interesting open question.
References
Arimoto, Y. 2010. Impact of land readjustment project on farmland use and structural adjustment:
The case of Niigata, Japan. Agricultural and Applied Economics Association 2010 AAEA, CAES,
WAEA Joint Annual Meeting,. Denver, USA.
Beaumont, O., V. Boudet, F. Rastello, Y. Robert. 2001. Matrix multiplication on heterogeneous plat-
forms. IEEE Transactions on Parallel and Distributed Systems 12(10) 1033–1051.
Beaumont, O., V. Boudet, F. Rastello, Y. Robert. 2002. Partitioning a square into rectangles: NP-
Completeness and approximation algorithms. Algorithmica 34(3) 217–239.
Borgwardt, S., A. Brieden, P. Gritzmann. 2011. Constrained minimum-k-star clustering and its applica-
tion to the consolidation of farmland. Operational Research 11(1) 1–17.
Borgwardt, S., A. Brieden, P. Gritzmann. 2014. Geometric clustering for the consolidation of farmland
and woodland. The Mathematical Intelligencer 36(2) 37–44.
Brieden, A., P. Gritzmann. 2004. A quadratic optimization model for the consolidation of farmland
by means of lend-lease agreements. D. Ahr, R. Fahrion, M. Oswald, G. Reinelt, eds., Operations
Research Proceedings 2003. Springer Berlin Heidelberg, 324–331.
20


## Page 21


Bui, Q. T., Q. D. Pham, Y. Deville. 2013. Solving the agricultural land allocation problem by constraint-
based local search. C. Schulte, ed., Principles and Practice of Constraint Programming, Lecture
Notes in Computer Science, vol. 8124. Springer Berlin Heidelberg, 749–757.
Cay, T., T. Ayten, F. Iscan. 2006. An investigation of reallocation model based on interview in land
consolidation. Proceeding of the 23rd FIG Congress, Shaping the Change. Munich, Germany.
Cay, T., T. Ayten, F. Iscan. 2010. Eﬀects of diﬀerent land reallocation models on the success of land
consolidation projects: Social and economic approaches. Land Use Policy 27(2) 262–269.
Cay, T., M. Uyan. 2013.
Evaluation of reallocation criteria in land consolidation studies using the
analytic hierarchy process (AHP). Land Use Policy 30(1) 541–548.
Demetriou, D., L. See, J. Stillwell. 2013. A spatial genetic algorithm for automating land partitioning.
International Journal of Geographical Information Science 27 2391–2409.
F¨ugenschuh, A, K. Junosza-Szaniawski, Z. Lonc. 2014. Exact and approximation algorithms for a soft
rectangle packing problem. Optimization 63(11) 1637–1663.
Garey, M. R., D. S. Johnson. 1990.
Computers and Intractability: A Guide to the Theory of NP-
Completeness. W. H. Freeman & Co., New York, NY, USA.
General Statistical Oﬃce. 2004. Statistical yearbook 2004. Statistical Publishing House.
Gliesch, A., M. Ritt, M. C. O. Moreira. 2017. A genetic algorithm for fair land allocation. Proceedings of
the Genetic and Evolutionary Computation Conference. GECCO ’17, ACM, New York, NY, USA,
793–800.
Hakli, H., H. Uuz. 2017. A novel approach for automated land partitioning using genetic algorithm.
Expert Systems with Applications 82(1) 10–18.
Heltberg, R. 1998. Rural market imperfections and the farm size-productivity relationship: Evidence
from Pakistan. World Development 26 1807–1826.
Huang, Q., M. Li, Z. Chen, F. Li. 2011. Land consolidation: An approach for sustainable development
in rural China. AMBIO 40(1) 93–95.
Ibaraki, T., K. Nakamura. 2006. Packing problems with soft rectangles. F. Almeida, M. J. Blesa Aguilera,
C. Blum, J. M. Moreno Vega, M. P´erez P´erez, A. Roli, M. Sampels, eds., Hybrid Metaheuristics.
Springer Berlin Heidelberg, Berlin, Heidelberg, 13–27.
Ji, P., K. He, Y. Jin, H. Lan, C. Li. 2017. An iterative merging algorithm for soft rectangle packing and
its extension for application of ﬁxed-outline ﬂoorplanning of soft modules. Computers & Operations
Research 86 110–123.
Journal of Rural Economy. 2008.
Agricultural mechanization:
When does it go over the start?
http://ipsard.gov.vn/mobile/tID2264_Co-gioi-hoa-nong-nghiep-Khi-nao-qua-buoc-khoi-dong-.html.
[Online; accessed 01-May-2018].
21


## Page 22


Kong, T. Y, D. M. Mount, M. Werman. 1987. The decomposition of a square into rectangles of minimal
perimeter. Discrete Applied Mathematics 16(3) 239–243.
Kong, T. Y., D. M. Mount, M. Werman. 1988. The decomposition of a rectangle into rectangles of
minimal perimeter. SIAM Journal on Computing 17(6) 1215–1231.
Lam, M-L. 2001. Land fragmentation–a constraint for Vietnam agriculture. Vietnam’s socio-economic
development 26 73–80.
March, S. P., T. G. MacAulay. 2006. Farm size and land use change in Vietnam following land reforms.
47th Annual Conference of the Australian Agricultural and Resource Economics Society. Fremantle,
Australia.
Nagamochi, H., Y. Abe. 2007. An approximation algorithm for dissecting a rectangle into rectangles
with speciﬁed areas. Discrete Applied Mathematics 155(4) 523–537.
Paes, F.G., A.A. Pessoa, T. Vidal. 2017. A hybrid genetic algorithm with decomposition phases for the
unequal area facility layout problem. European Journal of Operational Research 256(3) 742–756.
Pham, V-H., G. T. MacAulay, S. P. Marsh. 2007. The economics of land fragmentation in the north of
Vietnam*. Australian Journal of Agricultural and Resource Economics 51(2) 195–211.
Sundqvist, P., L. Anderson. 2006. A study of the impacts of land fragmentation on agricultural produc-
tivity in Northern Vietnam. Bachelor’s thesis, Uppsala University, Sweden.
Wilber, R. 1988. The concave least-weight subsequence problem revisited. Journal of Algorithms 9(3)
418–425.
Young, F. Y., C. C. N. Chu, W. S. Luk, Y. C. Wong. 2001. Handling soft modules in general nonslicing
ﬂoorplan using lagrangian relaxation. IEEE Transactions on Computer-Aided Design of Integrated
Circuits and Systems 20(5) 687–692.
22

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
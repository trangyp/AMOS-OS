---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1512.07815v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1512.07815v2_Truncated_Max-of-Convex_Models

> Source: 1512.07815v2_Truncated_Max-of-Convex_Models.pdf

> Pages: 37

---


## Page 1


Truncated Max-of-Convex Models
Pankaj Pansari
University of Oxford
pankaj@robots.ox.ac.uk
M. Pawan Kumar
University of Oxford
pawan@robots.ox.ac.uk
Abstract
Truncated convex models (TCM) are a special case of pairwise random ﬁelds that
have been widely used in computer vision. However, by restricting the order of
the potentials to be at most two, they fail to capture useful image statistics. We
propose a natural generalization of TCM to high-order random ﬁelds, which we call
truncated max-of-convex models (TMCM). The energy function of TMCM consists
of two types of potentials: (i) unary potential, which has no restriction on its
form; and (ii) clique potential, which is the sum of the 𝑚largest truncated convex
distances over all label pairs in a clique. The use of a convex distance function
encourages smoothness, while truncation allows for discontinuities in the labeling.
By using 𝑚> 1, TMCM provides robustness towards errors in the deﬁnition of
the cliques. In order to minimize the energy function of a TMCM over all possible
labelings, we design an efﬁcient 𝑠𝑡-MINCUT based range expansion algorithm. We
prove the accuracy of our algorithm by establishing strong multiplicative bounds
for several special cases of interest. Using standard real data sets, we demonstrate
the beneﬁt of our high-order TMCM over pairwise TCM, as well as the beneﬁt of
our range expansion algorithm over other 𝑠𝑡-MINCUT based approaches.
1
Introduction
Truncated convex models (TCM) are a special case of pairwise random ﬁelds that have been widely
used for low-level vision applications. A TCM is deﬁned over a set of random variables, each of
which can be assigned a value from a ﬁnite, discrete and ordered label set. In addition, a TCM also
speciﬁes a neighborhood relationship over the random variables. An assignment of values to all
the variables is referred to as a labeling. In order to quantitatively distinguish the labelings, a TCM
speciﬁes an energy function that consists of unary and pairwise potentials.
Given an input, the output is obtained by minimizing the energy function of a TCM over all possible
labelings. While this is an NP-hard problem, several approximate algorithms have been proposed in
the literature [3, 4, 12, 17, 20, 21, 24, 27, 30], which provide accurate solutions in practice [28].
Since we cannot reasonably expect to improve the optimization of TCM, any failure cases must be
addressed by modifying the model itself to better capture image statistics. To this end, we propose to
address one of the main deﬁciencies of TCM, namely, the restriction to potentials of order at most
two. Speciﬁcally, we propose a natural generalization of TCM to high-order random ﬁelds, which
we refer to as truncated max-of-convex models (TMCM). Similar to TCM, our model places no
restrictions on the unary potentials. Furthermore, unlike TCM, it allows us to deﬁne clique potentials
over an arbitrary number of random variables. The value of the clique potential is proportional to the
sum of the 𝑚largest truncated convex distances computed over disjoint pairs of random variables in
the clique. Here, disjoint pairs imply that the label of no random variable is used more than once
to compute the value of the clique potential. Figure 1 demonstrates how TMCM differs from TCM.
The exact mathematical form of the TMCM energy function will be presented in section 4. The
term 𝑚is a positive integer that is less than or equal to half the number of variables in the smallest
clique. Importantly, the constant of proportionality for each clique potential can depend on the input
arXiv:1512.07815v2  [cs.CV]  3 Dec 2016


## Page 2


(a) Truncated convex model
(b) Truncated max-of-convex model
Figure 1: TMCM as generalization of TCM. In (a), given an image, TCM considers pairwise 4-neighborhood
relationships and uses truncated convex distance function for pairwise potential. In (b), TMCM considers
superpixels as cliques. The clique potential for 𝑚=2 is the sum of the ﬁrst and second maximum over all the
pairwise truncated convex distances such that no variable is used more than once.
corresponding to all the random variables in the clique. This can help capture more interesting image
statistics, which in turn can lead to a more desirable output. For example, in image denoising, the
clique weights can depend on the variance of intensity over a superpixel (group of pixels with similar
semantic and perceptual characteristics).
In order to enable the use of TMCMs in practice, we require an efﬁcient and accurate energy
minimization algorithm that can compute the output for a given input. To this end, we extend the
range expansion algorithm for TCM to deal with arbitrary sized clique potentials. Our algorithm
retains the desirable property of iteratively solving an 𝑠𝑡-MINCUT problem over an appropriate
directed graph (where the number of vertices and arcs grows linearly with the number of random
variables and cliques, and quadratically with the number of labels). As the 𝑠𝑡-MINCUT problem
lends itself to several fast algorithms [2], this makes our overall approach computationally efﬁcient.
Furthermore, we provide strong theoretical guarantees on the quality of the solution for several
special cases of interest, which establishes its accuracy. Our multiplicative bounds are better than the
baselines for cases where comparison is possible. Using standard real data sets, we show the beneﬁt
of high-order TMCM over pairwise TCM, as well as the advantage of our range expansion algorithm
over other 𝑠𝑡-MINCUT based approaches.
2
Related Work
Pairwise TCM offer a natural framework to capture low-level cues for vision problems such as image
denoising, stereo correspondence, segmentation and optical ﬂow [28]. However, the restriction to
pairwise potentials limits their representational power.
For the past few years, there has been a growing interest in high-order models. Though other
inference algorithms such as message passing are possible [9, 19, 22, 26, 29, 31], in this work our
focus is on models that admit efﬁcient 𝑠𝑡-MINCUT based solutions and provide strong theoretical
guarantees on the quality of the solution. One early work was the 𝑃𝑛Potts model [15], which
encourages label consistency over a set of random variables. This work was extended in [16], which
introduced robustness in the 𝑃𝑛Potts model by taking into account the number of random variables
that disagreed with the majority label of a clique. Both the 𝑃𝑛Potts model and its robust version lend
themselves to efﬁcient optimization via the expansion algorithm [3], which solves one 𝑠𝑡-MINCUT
problem at each iteration. The expansion algorithm provides multiplicative bounds [11], which
measure the quality of the estimated labeling with respect to the optimal one. Our work generalizes
both the models, as well as the corresponding expansion algorithm. Speciﬁcally, when the truncation
factor of our models is set to 1, we recover the robust 𝑃𝑛model. Furthermore, a suitable setting of
the range expansion algorithm (setting the interval length to 1) recovers the expansion algorithm.
Jegelka and Bilmes [14] introduced a nonsubmodular high-order model which is based on edge
cooperation and is optimizable using 𝑠𝑡-MINCUT, but the algorithm has weak approximation bounds.
2


## Page 3


Delong et al. [6, 7] proposed a clique potential based on label costs that can also be handled via
the expansion algorithm. However, unlike the robust 𝑃𝑛Potts model, their model provides additive
bounds that are not invariant to reparameterizations of the energy function. This theoretical limitation
is addressed by the recent work of Dokania and Kumar [8] on parsimonious labeling. Here, the clique
potentials are deﬁned as being proportional to a diversity function of the set of unique labels present
in the clique labeling. Our work can be thought of as being complementary to parsimonious labeling.
Speciﬁcally, while parsimonious labeling is an extension of pairwise metric labeling to high-order
models, our work is an extension of TCM. The only metric that also results in a TCM is the truncated
linear distance. As our experiments will demonstrate, our specialized range expansion algorithm
provides signiﬁcantly better results for truncated max-of-linear models compared to the hierarchical
𝑠𝑡-MINCUT approach of [8].
We note that there have been several works that deal with more general high-order potentials and
design 𝑠𝑡-MINCUT style solutions for them. For example, Fix et al. [10] use the submodular max-
ﬂow algorithm [18], while Arora et al. [1] use generic cuts. However, the resulting algorithms are
exponential in the size of the cliques, which prevents their use in applications that require very
high-order cliques (with hundreds or even thousands of random variables). A notable exception to
this is the work of Ladicky et al. [25], who proposed a co-occurrence based clique potential whose
only requirement is that it should increase monotonically with the set of unique labels present in
the clique labeling. However, the use of such a general clique potential still results in an inaccurate
energy minimization algorithm, as will be seen in our experimental comparison.
3
Truncated Convex Models
A TCM is a random ﬁeld deﬁned by a set of discrete random variables X = {𝑋𝑎, 𝑎∈𝒱}, and
a neighborhood relationship ℰover them (that is, 𝑋𝑎and 𝑋𝑏are neighboring random variables if
(𝑎, 𝑏) ∈ℰ). Each random variable can take a value from a ﬁnite label set L, which is assumed to
be ordered to enable the use of convex distance functions. Without loss of generality, we deﬁne
𝒱= {1, 2, · · · , 𝑛} and L = {1, 2, · · · , ℎ}.
An assignment of values to all the random variables x ∈L𝑛is referred to as a labeling. To
quantitatively distinguish the ℎ𝑛possible labelings, a TCM deﬁnes an energy function that consists of
two types of potentials. First, the unary potentials 𝜃𝑎(𝑥𝑎) that depends on the label 𝑥𝑎of one random
variable 𝑋𝑎. Second, the pairwise potentials 𝜃𝑎𝑏(𝑥𝑎, 𝑥𝑏) that depends on the labels 𝑥𝑎and 𝑥𝑏of a
pair of neighboring random variables (𝑋𝑎, 𝑋𝑏). There are no restrictions on the form of the unary
potentials. However, the pairwise potentials are deﬁned using a truncated convex distance function
over the label set.
To provide a formal speciﬁcation of the pairwise potentials, we require some deﬁnitions. We denote
a convex distance function by 𝑑: Z →R (where Z is the set of integers and R is the set of real
numbers). Recall that a convex distance function satisﬁes the following properties: (i) 𝑑(𝑦) ≥0 for
all 𝑦∈Z and 𝑑(0) = 0; (ii) 𝑑(𝑦) = 𝑑(−𝑦) for all 𝑦∈Z; and (iii) 𝑑(𝑦+ 1) −2𝑑(𝑦) + 𝑑(𝑦−1) ≥0
for all 𝑦∈Z. Note that the above properties also imply that 𝑑(𝑦) ≥𝑑(𝑧) if |𝑦| ≥|𝑧|, for all 𝑦, 𝑧∈Z.
Examples of convex distance functions include the linear (that is, 𝑑(𝑦) = |𝑦|) and the quadratic
distance function (that is, 𝑑(𝑦) = 𝑦2) distance.
Given two labels 𝑙𝑖, 𝑙𝑗∈L, we use a convex function 𝑑(·) to measure the distance between them
as 𝑑(𝑙𝑖−𝑙𝑗), thereby encouraging smooth labelings. In order to prevent the overpenalization of the
discontinuities in an image, it is common practice to truncate the convex distance function [3, 23, 30].
Formally, a truncated convex function is deﬁned as min{𝑑(·), 𝑀}, where 𝑀is the truncation factor.
We now deﬁne the pairwise potential as 𝜃𝑎𝑏(𝑥𝑎, 𝑥𝑏) = 𝜔𝑎𝑏min{𝑑(𝑥𝑎−𝑥𝑏), 𝑀}, where 𝜔𝑎𝑏is a
(data-dependent) non-negative constant of proportionality.
Hence, a TCM speciﬁes an energy function 𝐸(·) over the labelings x ∈L𝑛as follows:
𝐸(x) =
∑︁
𝑎∈𝒱
𝜃𝑎(𝑥𝑎) +
∑︁
(𝑎,𝑏)∈ℰ
𝜔𝑎𝑏min{𝑑(𝑥𝑎−𝑥𝑏), 𝑀}.
(1)
The unary potentials are arbitrary, the edge weights 𝜔𝑎𝑏are non-negative, 𝑑(·) is a convex function
and 𝑀≥0 is the truncation factor. Given an input (which provides the values of the unary potentials
and the edge weights), the desired output is obtained by solving the following optimization problem:
3


## Page 4


minx∈L𝑛𝐸(x). While this optimization problem is NP-hard, we can obtain an accurate approximate
solution by using the efﬁcient range expansion algorithm [23], as well as several other approaches
based on 𝑠𝑡-MINCUT [3, 12, 21, 30] and linear programming [4, 17, 20].
4
Truncated Max-of-Convex Models
We now present a natural generalization of TCM to high-order random ﬁelds, which deﬁne potentials
over random variables that form a clique (where all the random variables in a clique are neighbors of
each other). Importantly, we do not place any restriction on the size of the clique.
Truncated Max-of-Convex Potentials.
Consider a high-order clique consisting of the random
variables Xc = {𝑋𝑎, 𝑎∈c ⊆𝒱}. We denote a labeling of the clique as xc ∈L𝑐, where we have
used the shorthand 𝑐= |c| to denote the size of the clique. In order to specify the value of the clique
potential for the labeling xc we require a sorted list of the (not necessarily unique) labels present in
xc. We denote this sorted list by p(xc) and access its 𝑖-th element as 𝑝𝑖(xc). For example, consider
a clique consisting of random variables Xc = {𝑋1, 𝑋2, 𝑋3, 𝑋4, 𝑋5, 𝑋6}. If the number of labels is
ℎ= 10, then one of the putative labelings of the clique is xc = {3, 2, 1, 4, 1, 3} (that is, 𝑋1 takes the
value 3, 𝑋2 takes the value 2 and so on). For this labeling, p(xc) = {1, 1, 2, 3, 3, 4}. The value of
𝑝1(xc) and 𝑝2(xc) is 1, the value of 𝑝3(xc) is 2 and so on. Given a convex function 𝑑(·), a truncation
factor 𝑀and an integer 𝑚∈[0, ⌊𝑐/2⌋], the clique potential 𝜃c(·) is deﬁned as
𝜃c(xc) = 𝜔c
𝑚
∑︁
𝑖=1
min{𝑑(𝑝𝑖(xc) −𝑝𝑐−𝑖+1(xc)), 𝑀}.
(2)
Here, 𝜔c ≥0 is the clique weight that does not depend on the labeling. However, it can be chosen
based on the observed data - for instance, we may want to assign small weights to cliques with large
variance of intensity or disparity. The term inside the summation is the truncated value of the 𝑖-th
largest distance between the labels of all pairs of random variables within the clique, subject to the
constraint that the label of no random variable is used more than once in the computation of the clique
potential value. In other words, our clique potential is proportional to the sum of the truncation of the
𝑚largest convex distance functions over disjoint pairs of random variables.
Given an input, the desired output is obtained by solving the following optimization problem:
minx∈L𝑛𝐸(x). Note that TMCM is a generalization of the 𝑃𝑛Potts model [15] (𝑚= 1, 𝑀= 1) as
well as its robust version [16] (𝑚> 1, 𝑀= 1). Furthermore, it is complementary to the recently
proposed parsimonious labeling, which generalizes metric labeling. Henceforth, we assume the unary
potentials are non-negative. This assumption is not restrictive as we can always add a constant to
the unary potentials of a random variable. This modiﬁcation would only result in the energy of all
labelings changing by the same constant. As we shall see, our algorithm as well as its theoretical
guarantees are invariant to such changes in the energy function.
5
Advantages of using TMCM
Labeling
𝑚= 1
𝑚= 2
𝑚= 3
(a) {1,1,1,1,2,2}
1
2
2
{1,2,3,4,5,6}
3
6
7
(b) {1,1,1,9,9,9}
3
6
9
{1,1,1,8,8,9}
3
6
9
(c) {1,1,1,1,1,7}
3
3
3
{1,1,1,2,3,4}
3
5
6
Table 1: Clique potential value 𝜃c(xc) deﬁned by a linear function with 𝑀= 3 and 𝜔c = 1 for various values
of 𝑚. Since clique size is 6, 0 ≤𝑚≤3. Pair (a) demonstrates why taking the largest convex distances favors
smoothness; (b) demonstrates how truncation prevents overpenalization of discontinuities; (c) demonstrates how
using 𝑚> 1 can provide some degree of robustness to errors in the deﬁnitions of the cliques.
We know show how TMCM encourages smooth labelings, does not overpenalize discontinuities and
is robust to erroneous clique deﬁnitions.
4


## Page 5


Smoothness.
The truncated max-of-convex potentials encourage smooth labelings. In order to
illustrate this, let us consider the example of a clique of six random variables Xc and a label set L of
size 10. We can deﬁne a truncated convex distance using a linear function 𝑑(𝑦) = |𝑦| and a truncation
factor of 𝑀= 3. Consider pair (a) of labelings shown in table 1. If the labeling is {1, 1, 1, 1, 2,
2} and 𝑀= 3, 𝑚= 3, 𝜔c = 1, 𝜃c(xc) = min(6-1, 3) + min(5 - 2, 6) + min(4 - 3, 3) = 3 + 3 + 1 = 7.
Clearly, the ﬁrst labeling of this pair is signiﬁcantly smoother than the second, which is reﬂected in
the value of the clique potential for all values of 𝑚. In contrast, if we were to consider the minimum
distance among all pairs of labels, both the labelings will provide a clique potential value of 0.
Discontinuities.
Similar to the pairwise case, the use of a truncation factor helps prevent overpe-
nalization of discontinuities. For example, let us consider the pair (b) of labelings in table 1. In
both cases, the six random variables appear to belong to two groups, one whose labels are low and
one whose labels are high. Without a truncation, such a discontinuity would have been penalized
heavily (for example, 8 for 𝑚= 1 for both the labelings). This in turn would discourage the clique
to be assigned this labeling even though this type of discontinuity is expected to occur in natural
images. However, with a truncation, the penalty is signiﬁcantly less (for example, 3 for 𝑚= 1 for
both the labelings), which can help preserve the discontinuities in the labeling obtained via energy
minimization.
Robustness.
In order to use a TMCM, we would be required to deﬁne the cliques. For example,
given an image, we could use a bottom-up oversegmentation approach to obtain superpixels, and
then set all the pixels in a superpixel to belong to a clique. However, oversegmentation can introduce
errors since it has no notion of the speciﬁc vision application we are interested in modeling. To add
robustness to errors in the clique deﬁnitions, we can set 𝑚> 1. For example, consider pair (c) of
labelings in table 1. The ﬁrst of these labelings contains a single random variable with a very high
label, which could be due to the fact that the corresponding pixel has been incorrectly grouped in
this superpixel. As can be seen from the values of the potential, the presence of such an erroneous
pixel in the superpixel is not heavily penalized when we use 𝑚> 1. For example, when 𝑚= 3 the
value of the clique potential for the ﬁrst labeling (with an erroneous pixel) is the same as the second
labeling (which is a fairly smooth labeling).
6
Optimization via Range Expansion
As TMCM is a generalization of TCM, it follows that the corresponding energy minimization problem
is NP-hard. However, we show that the efﬁcient and accurate range expansion algorithm can be
extended to handle this more general class of energy functions.
Algorithm 1 shows the main steps of range expansion. The algorithm starts by assigning the random
variables to an initial label (step 1). For example, all the random variables could be assigned to the
label 1. Next, it selects an interval of consecutive labels of size at most ℎ′ (steps 3-4), where ℎ′ is
speciﬁed as an input to the algorithm. We will see later in the section that the value of ℎ′ can be
chosen to obtain the optimal worst case bound for speciﬁc instances of the TMCM. Next, it minimizes
the energy over all the labelings that either allow a random variable to retain its current label, or
choose a new label in the selected interval (step 5). If the energy of the new labeling is lower than
that of the current labeling, then the solution is updated (steps 6-8). This process is repeated for all
the intervals of consecutive labels of size at most ℎ′. The entire algorithm stops when the energy
cannot be reduced further for any choice of the interval.
The crux of the range expansion algorithm is problem (3), which needs to be solved for any given
interval I and current labeling ˆx. Unfortunately, this problem itself is NP-hard for TMCM. Indeed,
when ℎ′ = ℎ, problem (3) is equivalent to the original energy minimization problem. In order
to operationalize the range expansion algorithm, we need to devise an approximate algorithm for
problem (3). We achieve this in two steps. First, we obtain an overestimate of the energy function
𝐸(·), which we denote by 𝐸′(·). The energy function 𝐸′(·) is restricted to the labels in the interval I
together with the labels speciﬁed by the current labeling ˆx. Second, we minimize the overestimated
energy 𝐸′(·) over all of its putative labelings by solving an equivalent 𝑠𝑡-MINCUT problem. We
describe our two-step algorithm in the next two subsections in detail. Speciﬁcally, subsection 6.1
describes the exact form of the energy function 𝐸′(·), while subsection 6.2 describes the construction
of the directed graph over which we solve the 𝑠𝑡-MINCUT problem to obtain the labeling x′.
5


## Page 6


𝑛
Number of random variables
ℎ
Number of labels
𝒱
{1, 2, . . . , n}
L
{1, 2, . . . , h}
X
Set of random variables {X𝑎, 𝑎∈𝒱}
Xc
Set of random variable belonging to a clique {𝑋𝑎, 𝑎∈c ⊆𝒱}
xc
Labeling of clique c
p(xc)
Sorted list of the labels present in xc
In
Interval of consecutive labels [𝑖𝑛+ 1, 𝑗𝑛]
h′
Length of interval, that is, h′ = 𝑗𝑛−𝑖𝑛
Γ𝑟
Set of intervals {[0, 𝑟], [𝑟+ 1, 𝑟+ L], . . . , [., ℎ−1]}
f
Labeling of the random ﬁeld (𝑣𝑎takes the label 𝑙𝑓(𝑎))
f *
An optimal (MAP) labeling of the random ﬁeld
𝜃𝑎(𝑖)
Unary potential of assigning label 𝑙𝑖to 𝑣𝑎
𝜔c
Weight for clique Xc
c
Size of clique Xc
d(.)
Convex function used to deﬁne distance between two labels
M
Truncation factor
𝜃c(xc)
Clique potential of assigning label 𝑙𝑖to 𝑣𝑎
E(f )
Energy of the labeling 𝑓
𝒜(𝑓, 𝐼𝑛)
{Xc ∈𝒞, 𝑓(𝑣) ∈𝐼𝑛∀𝑣∈Xc}
ℬ(𝑓, 𝐼𝑛)
{Xc ∈𝒞, ∃𝑋𝑣, 𝑋𝑤∈Xc|𝑓(𝑣) ∈𝐼𝑛∧𝑓(𝑤) /∈𝐼𝑛}
Table 2: Deﬁnitions of various symbols used in the supplementary document
Algorithm 1 The range expansion algorithm.
input Energy function 𝐸(·), initial labeling x0, interval length ℎ′.
1: Initialize the output labeling ˆx = x0.
2: repeat
3:
for all 𝑖𝑚∈[−ℎ′ + 2, ℎ] do
4:
Deﬁne an interval of labels I = {𝑓, · · · , 𝑙} where 𝑓= max{𝑖𝑚, 1} and 𝑙= min{𝑖𝑚+ℎ′ −
1, ℎ}.
5:
Obtain a new labeling x′ by solving the following optimization problem:
x′ =
argmin
x
𝐸(x),
s.t. 𝑥𝑎∈I ∪{ˆ𝑥𝑎}, ∀𝑎∈𝒱.
(3)
6:
if 𝐸(ˆx) > 𝐸(x′) then
7:
Update ˆx = x′.
8:
end if
9:
end for
10: until The labeling does not change for any value of 𝑖𝑚.
output The labeling ˆx.
6


## Page 7


6.1
Overestimation of the Energy Function
Given an interval I = {𝑓, · · · , 𝑙} of consecutive labels, and the current labeling ˆx, we deﬁne the new
energy function 𝐸′(·) over the set of random variables X. Unlike the original energy function, the
label set corresponding to 𝐸′(·) is equal to L′ = {0, 1, · · · , ℎ′}, where ℎ′ = 𝑙−𝑓+ 1. The label
0 in the set L′ corresponds to a random variable retaining its current label, while any other label
𝑖≥1 corresponds to a random variables taking the label 𝑓+ 𝑖−1 ∈I. A labeling of the energy
function 𝐸′(·) is denoted by y ∈(L′)𝑛in order to distinguish it from the labeling corresponding to
the original energy function. We say that a labeling x ∈L𝑛corresponds to the labeling y ∈(L′)𝑛if
𝑥𝑎=
{︂ˆ𝑥𝑎
if 𝑦𝑎= 0,
𝑦𝑎+ 𝑓−1
otherwise.
(4)
We deﬁne the unary potentials and the clique potentials of the energy function 𝐸′(·) as follows.
Unary Potentials.
The unary potential of a random variable 𝑋𝑎(where 𝑎∈𝒱) being assigned a
label 𝑦𝑎∈L′ is given by the following equation:
𝜃′
𝑎(𝑦𝑎) =
{︂
𝜃𝑎(ˆ𝑥𝑎) + 𝜅𝑎
if 𝑦𝑎= 0
𝜃𝑎(𝑦𝑎+ 𝑓−1) + 𝜅𝑎
otherwise.
(5)
In other words, if 𝑦𝑎= 0 then the unary potential corresponds to the random variable 𝑋𝑎retaining its
current label ˆ𝑥𝑎, and if 𝑦𝑎̸= 0 then the unary potential corresponds to the random variable 𝑋𝑎being
assigned the label 𝑦𝑎+ 𝑓−1 ∈I. The constant 𝜅𝑎is added to the unary potentials to ensure that
they are non-negative, which makes the description of the graph construction in the next subsection
simpler.
Clique Potentials.
In order to describe the high-order clique potentials of the new energy function
we require a function 𝛿𝑎,𝑏: L′ × L′ →R for each (𝑎, 𝑏) ∈ℰ, which is deﬁned as follows:
𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) =
⎧
⎪
⎨
⎪
⎩
min{𝑑(ˆ𝑥𝑎−ˆ𝑥𝑏), 𝑀}
if 𝑦𝑎= 𝑦𝑏= 0,
𝑀+ 𝑑(𝑦𝑏−1)
if 𝑦𝑎= 0, 𝑦𝑏̸= 0,
𝑀+ 𝑑(𝑦𝑎−1)
if 𝑦𝑎̸= 0, 𝑦𝑏= 0,
𝑑(𝑦𝑎−𝑦𝑏)
if 𝑦𝑎̸= 0, 𝑦𝑏̸= 0.
(6)
Here, 𝑑(·) is the convex function and 𝑀is the truncation factor associated with the original energy
function 𝐸(·).
Proposition 1. 𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) is submodular in the sense of label-set encoding used in [13]and is an
overestimate of the truncated convex distance min{𝑑(𝑥𝑎−𝑥𝑏), 𝑀} (Proof in Appendix A).
Given a labeling yc ∈(L′)𝑐of a clique c of size 𝑐, we denote a sorted list of the labels in yc as
p(yc). Furthermore, we denote the indices of the sorted list as q(yc). In other words, the random
variable corresponding to the 𝑖-th smallest label (that is, the 𝑖-th element of the list p(yc), which is
denoted by 𝑝𝑖(yc)) is given by 𝑋𝑎where 𝑎= 𝑞𝑖(yc). To avoid clutter, we will drop the argument yc
from p and q whenever it is clear from context.
Using the above deﬁnitions, the high-order clique potential for the new energy 𝐸′(·) can be concisely
speciﬁed as
𝜃′
c(yc) = 𝜔c
𝑚
∑︁
𝑖=1
𝛿𝑞𝑖,𝑞𝑐−𝑖+1(𝑝𝑖, 𝑝𝑐−𝑖+1).
(7)
Hence, the clique potentials in the energy function 𝐸′(·) are the sum of the 𝑚maximum submodular
functions over disjoint pairs of random variables in the clique.
6.2
Graph Construction
Our problem is to minimize the energy function 𝐸′(·) over all possible labelings y ∈(L′)𝑛. To this
end, we convert it into an equivalent 𝑠𝑡-MINCUT problem over a directed graph, which can be solved
efﬁciently if all arc capacities are non-negative [2].
7


## Page 8


Figure 2: Arcs and their capacities for representing the unary potentials for the random variable 𝑋𝑎. According
to the labeling deﬁned in equation (8), if 𝑥𝑎= ^𝑥𝑎, then the arc (𝑠, 𝑉𝑎
1 ) will be cut, which will contribute exactly
𝜃𝑎(^𝑥𝑎) to the capacity of the cut. If 𝑥𝑎= 𝑠+ 𝑖−1 where 𝑖∈{1, · · · , ℎ′ −1}, then the arc (𝑉𝑎
𝑖, 𝑉𝑎
𝑖+1) will
be cut, which will contribute exactly 𝜃𝑎(𝑠+ 𝑖−1) to the capacity of the cut. If 𝑥𝑎= 𝑙, then the arc (𝑉𝑎
ℎ′, 𝑡)
will be cut, which will contribute exactly 𝜃𝑎(𝑙) to the capacity of the cut. The arcs with inﬁnite capacity ensure
that exactly one of the arcs from the set (𝑠, 𝑉𝑎
1 ) ∪{(𝑉𝑎
𝑖, 𝑉𝑎
𝑖+1), 𝑖= 1, · · · , ℎ′ −1} ∪(𝑉𝑎
ℎ′, 𝑡) will be part of an
𝑠𝑡-cut with ﬁnite capacity, which will guarantee that we are able to obtain a valid labeling.
Figure 3: Arcs used to represent the high-order potentials for the clique Xc = {𝑋1, 𝑋2, · · · , 𝑋𝑐}. Left. The
term 𝑟𝑖𝑗is deﬁned in equation (9). The arcs represent the sum of the 𝑚maximum convex distance functions over
disjoint pairs of random variables when no random variable retains its old label. These arcs are speciﬁed only
for 𝑖≤𝑗and when either one or both of 𝑖and 𝑗are not equal to 1. Right. The terms 𝐴and 𝐵are deﬁned in
equation (10). The arcs represent an overestimation of the clique potential for the case where some or all the
random variables retain their old label.
We construct a directed graph over the set of vertices {𝑠, 𝑡} ∪V ∪U ∪W. The set of vertices V
model the random variables X. Speciﬁcally, for each random variable 𝑋𝑎we deﬁne ℎ′ = 𝑙−𝑓+ 1
vertices 𝑉𝑎
𝑖where 𝑖∈{1, · · · , ℎ′}. The sets U and W represent auxiliary vertices, whose role
in the graph construction will be explained later when we consider representing the high-order
clique potentials. We also deﬁne a set of arcs over the vertices, where each arc has a non-negative
capacity. We would like to assign arc capacities such that the 𝑠𝑡-cuts of the directed graph satisfy
two properties. First, all the 𝑠𝑡-cuts with a ﬁnite capacity should include exactly one arc from the
set (𝑠, 𝑉𝑎
1 ) ∪{(𝑉𝑎
𝑖, 𝑉𝑎
𝑖+1), 𝑖= 1, · · · , ℎ′ −1} ∪(𝑉𝑎
ℎ′, 𝑡) for each random variable 𝑋𝑎. This property
would allow us to deﬁne a labeling y such that
𝑦𝑎=
⎧
⎨
⎩
0
if the cut includes the arc (𝑠, 𝑉𝑎
1 )
𝑖
if the cut includes the arc (𝑉𝑎
𝑖, 𝑉𝑎
𝑖+1)
ℎ′
if the cut includes the arc (𝑉𝑎
ℎ′, 𝑡).
(8)
Second, we would like the energy of the labeling y deﬁned above to be as close as possible to the
capacity of the 𝑠𝑡-cut. This will allow us to obtain an optimal labeling with respect to the energy
function 𝐸′() by ﬁnding the 𝑠𝑡-MINCUT. We now specify the arcs and their capacities such that they
satisfy the above two properties. We consider two cases: (i) arcs that represent the unary potentials;
and (ii) arcs that represent the high-order clique potentials.
Representing Unary Potentials.
We will represent the unary potential of 𝑋𝑎using the arcs speci-
ﬁed in Figure 2. Since all the unary potentials are non-negative, it follows that the arc capacities in
Figure 2 are also non-negative.
8


## Page 9


Representing Clique Potentials.
Consider a set of random variables Xc that are used to deﬁne
a high-order clique potential. Without loss of generality, we assume Xc = {𝑋1, 𝑋2, · · · , 𝑋𝑐}. In
order to represent the potential value for a putative labeling xc of the clique, we introduce two types
of arcs, which are depicted in Figure 3. For the arcs shown in Figure 3 (left), the capacities are
speciﬁed using the term 𝑟𝑖𝑗that is deﬁned as follows:
𝑟𝑖𝑗=
{︃
𝜔c
𝑑(𝑖,𝑗)
2
if 𝑖= 𝑗
𝜔c𝑑(𝑖, 𝑗)
otherwise.
(9)
Here, the term 𝑑(𝑖, 𝑗) = 𝑑(𝑖−𝑗+1)+𝑑(𝑖−𝑗−1)−2𝑑(𝑖−𝑗) ≥0 since 𝑑(·) is convex, and 𝜔c ≥0
by deﬁnition. It follows that 𝑟𝑖𝑗≥0 for all 𝑖, 𝑗∈{1, · · · , ℎ′}. We have the following important
lemma which will be helpful in the discussion of graph properties later:
Lemma 1. Graph (a) of ﬁgure 3 exactly models clique potentials that are proportional to the sum
of 𝑚maximum convex distance functions over all disjoint pairs of random variables of the clique.
(Proof in Appendix B)
For the arcs shown in Figure 3 (right), the capacities are speciﬁed using the terms 𝐴and 𝐵that are
deﬁned as follows:
𝐴= 𝜔c𝑀, 𝐵=
(︂
𝜔c𝑀−𝜃c(^xc)
𝑚
)︂
.
(10)
Since 𝑀≥0, and 𝜃c(ˆxc) ≤𝜔c𝑚𝑀due to truncation, it follows that 𝐴, 𝐵≥0.
6.2.1
Properties of the Graph
This part describes the properties of the above graph construction which will facilitate the analysis of
our algorithm for the truncated max-of-linear models.
Property 1. The cost of the 𝑠𝑡−cut exactly represents the sum of the unary potentials associated
with the corresponding labeling 𝑓, that is, ∑︀
𝑣𝑎∈v 𝜃𝑎(𝑓(𝑎)).
This property follows from the description of the graph construction for unary potentials.
Property 2. For 𝑐∈𝒞, if for all 𝑋𝑎∈Xc, 𝑓(𝑎) = 𝑓𝑛(𝑎) /∈𝐼𝑛(all variables in a clique retain
their old labels), then the cost of the 𝑠𝑡−cut exactly represents the clique potential plus a constant
𝜅c = 𝜔𝑐𝑚· 𝑀−𝜃c( ˆxc).
Graph (a) of ﬁgure 3 assigns 0 cost. In graph (b), the vertices {𝑉1
1 , . . . , 𝑉𝑐
1 } ∈Vt and hence, the
𝑠−𝑈arc of capacity 𝑚𝐴is cut.
𝑚𝐴= 𝜔𝑐· 𝑚· 𝑀
= 𝜃c( ˆxc) + 𝜔𝑐𝑚· 𝑀−𝜃c( ˆxc)
= 𝜃c( ˆxc) + 𝜅c
Property 3. If all variables in a clique move to a label in the current interval and |𝑙𝑐−𝑙1| ≤𝑀, then
the cost of the 𝑠𝑡−cut exactly represents the clique potential plus a constant 𝜅c = 𝜔𝑐𝑚· 𝑀−𝜃c( ˆxc).
As proved in lemma 1, graph (a) of ﬁgure 3 assigns exactly 𝜃c(xc) cost. In graph (b), the vertices
{𝑉1
1 , . . . , 𝑉𝑐
1 } ∈Vs and hence, the 𝑊−𝑡arc of capacity 𝐵is cut, where
𝐵= 𝜔𝑐· 𝑚· 𝑀−𝜃c( ˆxc) = 𝜅c
Property 4. If all variables in a clique move to a label in the current interval and |𝑙𝑐−𝑙1| ≥𝑀,
then the cost of the 𝑠𝑡−cut overestimates the clique potential, being
𝜔𝑐
𝑚
∑︁
𝑖=1
𝑑(𝑝𝑖(xc −𝑝𝑐−𝑖+1(xc)
plus a constant 𝜅c = 𝜔𝑐𝑚· 𝑀−𝜃c( ˆxc).
9


## Page 10


Property 5. If 𝑘(< 𝑐) variables in a clique retains their old labels, then the cost of the 𝑠𝑡−cut
overestimates the clique potential, being.
𝜔𝑐
𝑘
∑︁
𝑖=1
𝑑(𝑝𝑐−𝑖+1(xc) −𝑖𝑛−1) + 𝜔𝑐· 𝑚· 𝑀
plus a constant 𝜅c = 𝜔𝑐𝑚· 𝑀−𝜃c( ˆxc).
The following proposition follows from the properties of the graph:
Proposition 2. Given a cut that partitions the vertices V into two disjoint sets V𝑠and V𝑡, and the
corresponding labeling y deﬁned in equation (8), the capacity of the cut is equal to the energy 𝐸′(y)
up to a constant.
Energy Minimization.
The above proposition implies that the labeling y′ corresponding to the
𝑠𝑡-MINCUT minimizes the energy 𝐸′(·) over all possible labelings y ∈(L′)𝑛. Since all the arc
capacities in the graph are non-negative, the labeling y′ can be computed efﬁciently by solving the
𝑠𝑡-MINCUT problem on the directed graph deﬁned above. Once the labeling y′ is computed, we ﬁnd
an approximate solution x′ to problem (3) using equation (4).
6.3
Multiplicative Bounds
We obtain multiplicative bounds for our algorithm by making use of the fact that our algorithm
terminates only when the energy cannot be reduced for any interval 𝐼𝑛. This implies that our
algorithm has found the local minimum of the large neigbourhood deﬁned by the intervals. We ﬁrst
obtain a lower bound on the reduction in energy for a given interval by making use of the graph
properties. Since the ﬁnal labeling 𝑓is a local minimum over the intervals, this lower bound is
non-positive when the algorithm completes. This fact enables us to get an upper bound on the energy
of the ﬁnal labeling.
We ﬁrst need to introduce some notation. Let 𝑓𝑛denote the labeling after the 𝑛-th iteration and 𝐸(𝑓𝑛)
denote the corresponding energy. Also, 𝑓* denotes optimal labeling of the MRF.
Let 𝑟∈[0, ℎ′ −1] be a uniformly distributed random integer and ℎ′ be the length of the interval.
Using 𝑟we deﬁne the following set of intervals
Γ𝑟= {[0, 𝑟], [𝑟+ 1, 𝑟+ ℎ′], [𝑟+ ℎ′ + 1, 𝑟+ 2ℎ′], ..., [., ℎ−1]}
where ℎis the total number of labels.
Let X(𝑓*, 𝐼𝑛) contain all the random variables that take an optimal labeling in 𝐼𝑛, 𝒜(𝑓, 𝐼𝑛) be the
set of all cliques for which all variables take optimum label in the interval 𝐼𝑛and ℬ(𝑓, 𝐼𝑛) be the set
of all cliques for which at least one, but not all, variable takes optimum label in the interval 𝐼𝑛(that
is, at least one but not all variables retains old label).
In order to make the analysis more readable, the following shorthand notation is introduced:
∙We denote 𝜔c max𝑎,𝑏∈Xc 𝑑(𝑓*(𝑎) −𝑓*(𝑏)) as 𝑡𝑛
𝑐
∙We denote 𝜔c max𝑎∈Xc 𝑑(𝑓*(𝑎) −(𝑖𝑛+ 1)) + 𝜔cM as 𝑠𝑛
𝑐
The following lemma establishes a lower bound in the reduction in energy for any given interval:
Lemma 2. At an iteration of our algorithm, given the current labeling 𝑓𝑛and an interval 𝐼𝑛=
[𝑖𝑛+ 1, 𝑗𝑛], the new labeling 𝑓𝑛+1 obtained by solving the st-mincut problem reduces the energy by
at least the following:
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓𝑛(𝑎)) +
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)∪ℬ(𝑓,𝐼𝑛)
𝜃c(xc)
−
⎛
⎝
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓*(𝑎)) +
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)
𝑡𝑛
𝑐+
∑︁
Xc∈ℬ(𝑓,𝐼𝑛)
𝑠𝑛
𝑐
⎞
⎠
(Proof in Appendix C)
10


## Page 11


The following equation can be deduced from the above deﬁnitions:
∑︁
𝑋𝑎∈X
𝜃𝑎(𝑓*(𝑎)) =
∑︁
𝐼𝑛∈ℐ𝑟
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓*(𝑎))
(11)
since 𝑓*(𝑎) belongs to exactly one interval in 𝐼𝑟for all 𝑋𝑎.
For the ﬁnal labeling 𝑓of the range expansion algorithm, the term in lemma 2 should be non-positive
for all intervals 𝐼𝑛because 𝑓is a local optimum. Hence,
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓(𝑎)) +
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)∪ℬ(𝑓,𝐼𝑛)
𝜃c(xc)
≤
⎛
⎝
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓*(𝑎)) +
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)
𝑡𝑛
𝑐+
∑︁
Xc∈ℬ(𝑓,𝐼𝑛)
𝑠𝑛
𝑐
⎞
⎠, ∀𝐼𝑛
We sum the above inequality over all 𝐼𝑛∈Γ𝑟. The summation of the LHS is at least 𝐸(𝑓). Also,
using (28), the summation of the above inequality can be written as:
𝐸(𝑓) ≤
∑︁
𝑋𝑎∈X
𝜃𝑎(𝑓*(𝑎)) +
∑︁
𝐼𝑛∈Γ𝑟
⎛
⎝
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)
𝑡𝑛
𝑐+
∑︁
Xc∈ℬ(𝑓,𝐼𝑛)
𝑠𝑛
𝑐
⎞
⎠
We now take the expectation of the above inequality over the uniformly distributed random integer
𝑟∈[0, ℎ′ −1]. The LHS of the inequality and the ﬁrst term on the RHS (that is, ∑︀𝜃𝑎(𝑓*(𝑎))) are
constants with respect to 𝑟. Hence, we get
𝐸(𝑓) ≤
∑︁
𝑋𝑎∈X
𝜃𝑎(𝑓*(𝑎)) + 1
ℎ′
∑︁
𝑟
∑︁
𝐼𝑛∈Γ𝑟
⎛
⎝
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)
𝑡𝑛
𝑐+
∑︁
Xc∈ℬ(𝑓,𝐼𝑛)
𝑠𝑛
𝑐
⎞
⎠
(12)
For linear distance function 𝑑(.), we have the following lemma:
Lemma 3. When 𝑑(.) is linear, that is, 𝑑(𝑥) = |𝑥|, the following inequality holds true:
1
ℎ′
∑︁
𝑟
∑︁
𝐼𝑛∈Γ𝑟
⎛
⎝
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)
𝑡𝑛
𝑐+
∑︁
Xc∈ℬ(𝑓,𝐼𝑛)
𝑠𝑛
𝑐
⎞
⎠
≤𝑚𝑎𝑥
{︂𝑐
2
(︂
2 + ℎ′
𝑀
)︂
,
(︂
2 + 2𝑀
ℎ′
)︂}︂∑︁
c∈𝒞
𝜃c(xc)
(13)
where c is the largest clique in the random ﬁeld (Proof in Appendix D).
Using lemma 3 in inequality 12, we obtain the multiplicative bound for max-of-linear models for
𝑚= 1:
Proposition 3. The range expansion algorithm with ℎ′ = 𝑀has a multiplicative bound of 𝑂(𝐶)
for truncated max-of-linear model when 𝑚= 1. The term 𝐶equals the size of the largest clique.
Hence, if x* is a labeling with minimum energy and ˆx is the labeling estimated by range expansion
algorithm then
∑︁
𝑎∈𝒱
𝜃𝑎(ˆ𝑥𝑎) +
∑︁
c∈𝒞
𝜃c(ˆxc) ≤
∑︁
𝑎∈𝒱
𝜃𝑎(𝑥*
𝑎) + 𝑂(𝐶)
∑︁
c∈𝒞
𝜃c(x*
c).
The above inequality holds for arbitrary set of unary potentials and non-negative clique weights
(Proof in Appendix E).
We now state the generalization for Proposition 3 for any given 𝑚:
11


## Page 12


Figure 4: Results for synthetic data using truncated linear distance function. The plots show the variation of
energy versus time, averaged over 50 lattices using 𝜔𝑐= 5. We use truncation factors as 𝑀= 5, 10 and 15 and
𝑚= 1, and for each we vary interval lengths for our algorithm. Parsimonious labeling performs well for 𝑀= 5,
but our approach outperforms for higher values of 𝑀. Red dot indicates convergence of parsimonious labeling
and dotted line indicates extrapolation.
Proposition 4. The range expansion algorithm with ℎ′ = 𝑀has a multiplicative bound of 𝑂(𝑚· 𝐶)
for truncated max-of-linear model for any general value of 𝑚. The term 𝐶equals the size of the
largest clique. Hence, if x* is a labeling with minimum energy and ˆx is the labeling estimated by
range expansion algorithm then
∑︁
𝑎∈𝒱
𝜃𝑎(ˆ𝑥𝑎) +
∑︁
c∈𝒞
𝜃c(ˆxc) ≤
∑︁
𝑎∈𝒱
𝜃𝑎(𝑥*
𝑎) + 𝑂(𝐶)
∑︁
c∈𝒞
𝜃c(x*
c).
The above inequality holds for arbitrary set of unary potentials and non-negative clique weights
(Proof in Appendix F).
Note that for 𝑚= 1, the bound of the move making algorithm for parsimonious labeling (which is
our baseline) is
(︁
𝑟
𝑟−1
)︁
(𝐶−1)𝑂(log ℎ) min(𝐶, ℎ) where 𝐶is the size of the largest clique and ℎis
the number of labels [8]. Our algorithm gives a better bound of 𝑂(𝐶) and does not depend on the
number of labels.
Similar to the case of max-of-linear models, by making use of Theorem 4 of [4], we obtain the bound
for max-of-quadratic models for 𝑚= 1:
Proposition 5. The range expansion algorithm with ℎ′ =
√
𝑀has a multiplicative bound of
𝑂(𝐶
√
𝑀) for the truncated max-of-quadratic model when 𝑚= 1.
7
Experiments
To demonstrate the efﬁcacy of our algorithm, we test it on the two problems of image inpainting
and denoising, and stereo matching. The ﬁnal labeling energy and convergence time are used as
evaluation criteria. We used the parsimonious labeling algorithm of Dokania et al. [8] and the move-
making algorithm for the co-occurrence based energy function of Ladicky et al. [25] as baselines.
For comparison, we restrict ourselves to max-of-linear models and 𝑚= 1, as the available code for
the baselines can only handle this special case. For completeness, we report the results of our range
expansion algorithm for other cases of TMCM and on synthetic data as well.
7.1
Synthetic Data
Data.
We generate lattices of size 100 × 100, where each lattice point represents a variable taking
one of 20 labels. The cliques are deﬁned as all 10 × 10 subwindows. The unary potentials are
12


## Page 13


Figure 5: Results for synthetic data using truncated linear distance function. The plots show the variation of
energy versus time, averaged over 50 lattices using 𝜔𝑐= 5. We use truncation factors as 𝑀= 5, 10 and 15 and
𝑚= 1, and for each we vary interval lengths for our algorithm. This plot is the same as shown in the paper, but
we include it here for the sake of comparison. Red dot indicates convergence of parsimonious labeling algorithm
and dotted line indicates extrapolation.
Figure 6: Results for synthetic data using truncated linear distance function. The plots show the variation of
energy versus time, averaged over 50 lattices using 𝜔𝑐= 5. We use truncation factors as 𝑀= 5, 10 and 15 and
𝑚= 1, and for each we vary interval lengths for our algorithm. This plot corresponds to the same experiment as
mentioned in the paper, but with results for co-occurrence included. Red and black dots indicate convergence of
respective algorithms and dotted line indicates extrapolation.
13


## Page 14


Figure 7: Results for synthetic data using truncated linear distance function. The plots show the variation of
energy versus time, averaged over 50 lattices using 𝜔𝑐= 10. We use truncation factors as 𝑀= 5, 10 and 15
and 𝑚= 1, and for each we vary interval lengths for our algorithm. Parsimonious labeling performs well for
𝑀= 5, but our approach outperforms for higher values of 𝑀. Red dot indicates convergence of parsimonious
labeling and dotted line indicates extrapolation.
Figure 8: Results for synthetic data using truncated linear distance function. The plots show the variation of
energy versus time, averaged over 50 lattices using 𝜔𝑐= 5. We use truncation factors as 𝑀= 5, 10 and 15 and
𝑚= 1, and for each we vary interval lengths for our algorithm. This plot corresponds to the same experiment as
in ﬁgure 7, but with results for co-occurrence included. Red and black dots indicate convergence of respective
algorithms and dotted line indicates extrapolation.
14


## Page 15


Figure 9: Results for synthetic data using truncated quadratic distance function. The plots show the variation
of energy versus time, averaged over 50 lattices using 𝜔𝑐= 3. We use 𝑀= 25, 100 and 225 and 𝑚= 1, and for
each we vary interval lengths for our algorithm.
Figure 10: Results for synthetic data using truncated quadratic distance function. The plots show the variation
of energy versus time, averaged over 50 lattices using 𝜔𝑐= 5. We use 𝑀= 25, 100 and 225, and for each we
vary interval lengths for our algorithm.
15


## Page 16


uniformly sampled in the range [1, 100]. The truncation factors for linear case are 𝑀∈{5, 10, 15}
and for quadratic case 𝑀∈{25, 100, 225}. In each energy function, all cliques were assumed to
have the same clique weight, being 5 and 10 for linear model and 3 and 5 for quadratic model. 𝑚
varies in the range {1, 3, 5}.
Method.
For each energy function obtained by a particular setting of the above parameters, we
vary the interval length up to 𝑀+ 1. We run [8] and [25] only for linear distance function and 𝑚= 1
and repeat the experiments for 50 randomly generated unaries for linear and quadratic cases.
Results.
The plots in Figure 6 and 5 show the average energy as a function of average time for
our algorithm and the baselines using weight as 5 for max-of-linear models, with and without the
results of [25] respectively. We see that the energy values of [25] are much higher as compared
to our algorithm. Our algorithm gives lower energy solutions than parsimonious labeling method
except when the truncation factor is low (𝑀= 5). The plots in Figures 8 and 7 shows the results for
max-of-linear models using weight as 10 with and without the cooccurrence results respectively. Our
algorithm gives better results than the baselines for all 𝑀. Both the baselines converge faster than
our method. In practice, intervals smaller than the optimum size give almost equally good results and
converge faster. Figure 10 shows the plot for max-of-quadratic cases using weight as 5.
7.2
Image Inpainting and Denoising
Data.
Given an image with noise and obscured/inpainted regions (regions with missing pixels), the
task is to denoise it and ﬁll the obscured regions in a way that is consistent with the surrounding regions.
The images ‘house’ and ‘penguin’ from the Middlebury data set were used for the experiments. Since
the images are grayscale, they have 256 labels in the interval [0, 255], each representing an intensity
value. The unary potential for each pixel corresponding to a particular label equals the squared
difference between the label and the intensity value at the pixel. We use high-order cliques as the
super-pixels obtained using the mean-shift method [5]. The parameters 𝜔𝑐, 𝑀and 𝑚are varied to
give different truncated max-of-linear energy functions.
Method.
For each parameter setting of 𝜔𝑐, 𝑀and 𝑚, we vary the interval lengths for our algorithm
and make a comparison with the baselines.
Results.
Results for 𝜔𝑐= 40, 𝑀= 40, and 𝑚= 1, 3 and 5 for ‘penguin’ and 𝜔𝑐= 50, 𝑀= 50, and
𝑚= 1, 3 and 5 for ‘house’ are shown in Figure 12 for varying interval lengths ℎ′ = {5, 10, 20}. Our
algorithm consistently gives lower energy labeling as compared to both [8] and [25] even for small
ℎ′. For ‘penguin’, our algorithm gives cleaner denoised image, preserving edges and details. On
the other hand, both [8] and [25] exhibit signiﬁcant blocking effect. Moreover, the output is more
natural for 𝑚= 3 as compared to 𝑚= 1. Even for ‘house’, our output looks more visually appealing
as compared to baselines.
16


## Page 17


(a) Penguin input
(b) Cooccurrence
(c) Parsimonious
(Energy, Time (s))
(14735411, 237)
(12585846, 456)
(d) 𝑚= 1, ℎ′ = 5
(e) 𝑚= 1, ℎ′ = 10
(f) 𝑚= 1, ℎ′ = 20
(12541999, 1694)
(123598999, 2633)
(123018999, 3963)
(g) 𝑚= 3, ℎ′ = 5
(h) 𝑚= 3, ℎ′ = 10
(i) 𝑚= 3, ℎ′ = 20
(126481999, 1379)
(125784999, 2499)
(124044999, 5018)
(j) 𝑚= 5, ℎ′ = 5
(k) 𝑚= 5, ℎ′ = 10
(l) 𝑚= 5, ℎ′ = 20
(127329999, 1357)
(125284999, 2367)
(124501999, 5706)
Figure 11: Image inpainting results for ‘penguin’. Note that comparison with (b) and (c) makes sense only for
𝑚= 1. Also, we restricted our experiments to smaller (and suboptimal) ℎ′ due to computational issues.
17


## Page 18


(a) Penguin input
(b) Cooccurrence
(c) Parsimonious
(Energy, Time (s))
(42018464, 486)
(37349032, 12024)
(d) 𝑚= 1, ℎ′ = 5
(e) 𝑚= 1, ℎ′ = 10
(f) 𝑚= 1, ℎ′ = 20
(37196999, 8084)
(370873999, 11356)
(369035999, 22752)
(g) 𝑚= 3, ℎ′ = 5
(h) 𝑚= 3, ℎ′ = 10
(i) 𝑚= 3, ℎ′ = 20
(373067999, 7744)
(37115999, 9547)
(370936999, 23261)
(j) 𝑚= 5, ℎ′ = 5
(k) 𝑚= 5, ℎ′ = 10
(l) 𝑚= 5, ℎ′ = 20
(374691999, 6476)
(372811999, 9949)
(375026999, 22985)
Figure 12: Image inpainting results for ‘house’. Note that comparison with (b) and (c) makes sense only for 𝑚
= 1. Also, we restricted our experiments to smaller (and suboptimal) ℎ′ due to computational issues.
18


## Page 19


7.3
Stereo Matching
Data.
In the stereo matching problem, we have two rectiﬁed images of the same scene from two
cameras set slightly apart. We are required to estimate the horizontal disparity between a pixel in the
right camera image from the corresponding pixel in the left camera. We use ‘tsukuba’ and ‘teddy’
data sets from the Middlebury stereo collection for our experiments. In each case, we have a pair
of RGB images and ground truth disparities. We assume the unary potentials to be the 𝐿1-norm of
the difference in RGB values of the left and right image pixels. There are 16 labels and 60 labels for
‘tsukuba’ and ‘teddy’ respectively. The high-order cliques are super-pixels obtained using mean-shift
method [5]. The parameters 𝜔𝑐, 𝑀and 𝑚are varied to give different truncated max-of-linear energy
functions.
Method.
For each parameter setting of 𝜔𝑐, 𝑀and 𝑚, we vary the interval lengths for our algorithm
and make a comparison with the baselines.
Results.
Results for 𝜔𝑐= 20, 𝑀= 5, and 𝑚= 1 and 3 for ‘tsukuba’, ‘venus’ and ‘cones’ and 𝜔𝑐=
20, 𝑀= 1, and 𝑚= 1 and 3 for ‘teddy’ are shown in Figure 13. We used interval length ℎ′ as 4 for
‘tsukuba’ and ‘venus’, 6 for ‘cones’ and 2 for ‘teddy’. Apart from ‘cones’, our algorithm consistently
gives lower energy labeling as compared to both [8] and [25]. For ‘tsukuba’, our algorithm captures
the details of the face better than [8] and [25]. For ‘venus’, we get smoother labeling for the front
plane. Moreover, our results for 𝑚= 3 exhibit robustness to inaccurate clique deﬁnitions.
Results.
Results for 𝜔𝑐= 20, 𝑀= 5, and 𝑚= 1 and 3 for ‘tsukuba’, ‘venus’ and ‘cones’, and 𝜔𝑐
= 20, 𝑀= 1, and 𝑚= 1 and 3 for ‘teddy’ are shown in Figure 13. We show the results for interval
length 3 for ‘teddy’, and 6 for others. Note that in our main paper, we used interval length ℎ′ as 4 for
‘tsukuba’ and ‘venus’, and 1 for ‘teddy’ and did not show the results for ‘cones’. Apart from ‘cones’,
our algorithm consistently gives lower energy labeling as compared to both [8] and [25].
19


## Page 20


(1a) Ground truth
(2a) Ground truth
(3a) Ground truth
(4a) Ground truth
(Energy, Time (s))
(Energy, Time (s))
(Energy, Time (s))
(Energy, Time (s))
(1b) Cooccurrence
(2b) Cooccurrence
(3b) Cooccurrence
(4b) Cooccurrence
(2098800, 101)
(3259900, 495)
(2343200, 261)
(8260100, 308)
(1c) Parsimonious
(2c) Parsimonious
(3c) Parsimonious
(4c) Parsimonious
(1364200, 225)
(3201300, 484)
(2262600, 482)
(4985639, 759)
(1d) 𝑚= 1, ℎ′ = 4
(2d) 𝑚= 1, ℎ′ = 2
(3d) 𝑚= 1, ℎ′ = 4
(4d) 𝑚= 1, ℎ′ = 6
(1257249, 256)
(3004059, 1304)
(2210629, 2700)
(5237919, 3711)
(1e) 𝑚= 1, ℎ′ = 6
(2e) 𝑚= 1, ℎ′ = 3
(3e) 𝑚= 1, ℎ′ = 6
(4e) 𝑚= 1, ℎ′ = 6
(1258499, 518)
(3202489, 6216)
(2207549, 4624)
(5237919, 3711)
(1f) 𝑚= 3, ℎ′ = 6
(2f) 𝑚= 3, ℎ′ = 3
(3f) 𝑚= 3, ℎ′ = 6
(4f) 𝑚= 3, ℎ′ = 6
(1391629*, 720)
(3211819*, 5043)
(2222299*, 4189)
(5258999*, 4137)
(1g) 𝑚= 3, ℎ′ = 4
(2g) 𝑚= 3, ℎ′ = 2
(3g) 𝑚= 3, ℎ′ = 4
(4g) 𝑚= 3, ℎ′ = 6
(1267449*, 335)
(3211829*, 1139)
(2235689*, 3032)
(5258999*, 4137)
Figure 13: Stereo matching results: Figures (1a), (1b), (1c) and (1d) are the ground truth disparity for ‘tsukuba’, ‘teddy’, ‘venus’ and ‘cones’ respectively.
Our results for 𝑚= 1 (1d), (2d), and (3d) are signiﬁcantly better than those of [25] (1b), (2b) and (3b), and of [8] (1c), (2c) and (3c) in terms of energy. For
‘cones’, [8] (4c) performs better than our algorithm. We also show results for 𝑚= 3. We use super-pixels obtained using mean-shift as cliques. *Note that 𝑚
= 3 uses a different energy function from other cases.
20


## Page 21


8
Discussion
We proposed a novel family of high-order random ﬁelds called truncated max-of-convex models (TMCM)
which are generalization of truncated convex models (TCM). To perform inference in TMCM, we developed
a novel range expansion algorithm for energy minimization that retains the efﬁciency of 𝑠𝑡-MINCUT and
provides provably accurate solutions. The algorithm relies on an exact graph representation of max-of-
convex models, a tight submodular overestimate of the energy function for any interval length and a graph
construction that represents this overestimate, allowing the inference problem to be solved using 𝑠𝑡-MINCUT.
From a theoretical point of view, our work can be thought of as a step towards the identiﬁcation of graph
representable submodular functions and automated construction of graphs for such functions.
References
[1] C. Arora and S. Maheshwari. Multi label generic cuts: Optimal infernce in multi label multi clique MRF-MAP
problems. In CVPR, 2014.
[2] Y. Boykov and V. Kolmogorov. An experimental comparison of min-cut/max-ﬂow algorithms for energy minimiza-
tion in vision. PAMI, 2004.
[3] Y. Boykov, O. Veksler, and R. Zabih. Fast approximate energy minimization via graph cuts. PAMI, 2001.
[4] C. Chekuri, S. Khanna, J. Naor, and L. Zosin. Approximation algorithms for the metric labeling problem via a new
linear programming formulation. In SODA, 2001.
[5] Dorin Comaniciu and Peter Meer. Mean shift: A robust approach toward feature space analysis. PAMI, 2002.
[6] A. Delong, L. Gorelick, O. Veksler, and Y. Boykov. Minimizing energies with hierarchical costs. IJCV, 2012.
[7] A. Delong, A. Osokin, H. Isack, and Y. Boykov. Fast approximate energy minimization with label costs. In CVPR,
2010.
[8] P. Dokania and M. P. Kumar. Parsimonious labeling. In ICCV, 2015.
[9] Pedro F Felzenszwalb and Daniel P Huttenlocher. Efﬁcient belief propagation for early vision. IJCV, 2006.
[10] A. Fix, C. Wang, and R. Zabih. A primal-dual algorithm for higher-order multilabel Markov random ﬁelds. In
CVPR, 2014.
[11] S. Gould, F. Amat, and D. Koller. Alphabet soup: A framework for approximate energy minimization. In CVPR,
2009.
[12] A. Gupta and E. Tardos. A constant factor approximation algorithm for a class of classiﬁcation problems. In STOC,
2000.
[13] H. Ishikawa. Exact optimization for Markov random ﬁelds with convex priors. PAMI, 2003.
[14] Stefanie Jegelka and Jeff Bilmes. Submodularity beyond submodular energies: coupling edges in graph cuts. In
CVPR, 2011.
[15] P. Kohli, M. P. Kumar, and P. Torr. P3 & beyond: Solving energies with higher order cliques. In CVPR, 2007.
[16] P. Kohli, L. Ladicky, and P. Torr. Robust higher order potentials for enforcing label consistency. In CVPR, 2008.
[17] V. Kolmogorov. Convergent tree-reweighted message passing for energy minimization. PAMI, 2006.
[18] V. Kolmogorov. Minimizing a sum of submodular functions. Discrete Applied Mathematics, 2012.
[19] Vladimir Kolmogorov. Convergent tree-reweighted message passing for energy minimization. PAMI, 2006.
[20] N. Komodakis, N. Paragios, and G. Tziritas. MRF optimization via dual decomposition: Message-passing revisited.
In ICCV, 2007.
[21] N. Komodakis, G. Tziritas, and N. Paragios. Fast, approximately optimal solutions for single and dynamic MRFs.
In CVPR, 2007.
[22] Nikos Komodakis, Nikos Paragios, and Georgios Tziritas. Mrf optimization via dual decomposition: Message-
passing revisited. In ICCV, 2007.
21


## Page 22


[23] M. P. Kumar and P. Torr. Improved moves for truncated convex models. In NIPS, 2008.
[24] M Pawan Kumar, Olga Veksler, and Philip HS Torr. Improved moves for truncated convex models. JMLR, 2011.
[25] L. Ladicky, C. Russell, P. Kohli, and P. Torr. Graph cut based inference with co-occurrence statistics. In ECCV,
2010.
[26] Ofer Meshi, David Sontag, Tommi S. Jaakkola, and Amir Globerson. Learning efﬁciently with approximate
inference via dual losses. In ICML, 2010.
[27] David Sontag, Talya Meltzer, Amir Globerson, Tommi S Jaakkola, and Yair Weiss. Tightening LP relaxations for
map using message passing. In UAI, 2008.
[28] R. Szeliski, R. Zabih, D. Scharstein, O. Veksler, V. Kolmogorov, A. Agarwala, M. Tappen, and C. Rother. A
comparative study of energy minimization methods for Markov random ﬁelds with smoothness-based priors. PAMI,
2008.
[29] Daniel Tarlow, Inmar E Givoni, and Richard S Zemel. Hop-map: Efﬁcient message passing with high order
potentials. In AISTATS, 2010.
[30] O. Veksler. Graph cut based optimization for MRFs with truncated convex priors. In CVPR, 2007.
[31] Martin J. Wainwright, Tommi S. Jaakkola, and Alan S. Willsky. MAP estimation via agreement on trees: message-
passing and linear programming. IEEE Trans. Information Theory, 2005.
22


## Page 23


A
Proof of Proposition 1
Proposition 1: 𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) is submodular in the sense of label-set encoding used in [13]and is an overestimate
of the truncated convex distance min{𝑑(𝑥𝑎−𝑥𝑏), 𝑀}.
Proof:
Note that to prove that 𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) is submodular, we need to show that the following inequality
holds:
𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) + 𝛿𝑎,𝑏(𝑦𝑎+ 1, 𝑦𝑏+ 1) ≤𝛿𝑎,𝑏(𝑦𝑎+ 1, 𝑦𝑏) + 𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏+ 1)
(14)
We consider the 4 cases corresponding to equation 6.
Case 1: 𝑦𝑎= 𝑦𝑏= 0
𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) = 𝛿𝑎,𝑏(0, 0) = min{𝑑(ˆ𝑥𝑎−ˆ𝑥𝑏), 𝑀}
min{𝑑(𝑥𝑎−𝑥𝑏), 𝑀} = min{𝑑(ˆ𝑥𝑎−ˆ𝑥𝑏), 𝑀}
Hence, 𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) = min{𝑑(𝑥𝑎−𝑥𝑏), 𝑀}.
To prove submodularity, consider L.H.S of inequality 14:
𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) + 𝛿𝑎,𝑏(𝑦𝑎+ 1, 𝑦𝑏+ 1) = 𝛿𝑎,𝑏(0, 0) + 𝛿𝑎,𝑏(1, 1)
= min{𝑑(ˆ𝑥𝑎−ˆ𝑥𝑏), 𝑀} + 0
The R.H.S of inequality 14 is given by:
𝛿𝑎,𝑏(𝑦𝑎+ 1, 𝑦𝑏) + 𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏+ 1) = 𝛿𝑎,𝑏(1, 0) + 𝛿𝑎,𝑏(0, 1)
= 𝑀+ 𝑑(𝑦𝑏−1) + 𝑀+ 𝑑(𝑦𝑎−1)
Clearly L.H.S < R.H.S for this case.
Case 2: 𝑦𝑎= 0, 𝑦𝑏̸= 0
𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) = 𝛿𝑎,𝑏(0, 𝑦𝑏) = 𝑀+ 𝑑(𝑦𝑏−1)
min{𝑑(𝑥𝑎−𝑥𝑏), 𝑀} = min{𝑑(ˆ𝑥𝑎−𝑥𝑏), 𝑀}
Hence, 𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) ≥min{𝑑(𝑥𝑎−𝑥𝑏), 𝑀}.
For submodularity, L.H.S of inequality 14 is given by:
𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) + 𝛿𝑎,𝑏(𝑦𝑎+ 1, 𝑦𝑏+ 1) = 𝛿𝑎,𝑏(0, 𝑦𝑏) + 𝛿𝑎,𝑏(1, 𝑦𝑏+ 1)
= 𝑀+ 𝑑(𝑦𝑏−1) + 𝑑(𝑦𝑏)
23


## Page 24


The R.H.S of inequality 14 can be written as:
𝛿𝑎,𝑏(𝑦𝑎+ 1, 𝑦𝑏) + 𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏+ 1) = 𝛿𝑎,𝑏(1, 𝑦𝑏) + 𝛿𝑎,𝑏(0, 𝑦𝑏+ 1)
= 𝑑(𝑦𝑏−1) + 𝑀+ 𝑑(𝑦𝑏)
Hence L.H.S = R.H.S for this case.
Case 3: 𝑦𝑎̸= 0, 𝑦𝑏= 0
𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) = 𝛿𝑎,𝑏(𝑦𝑎, 0) = 𝑀+ 𝑑(𝑦𝑎−1)
min{𝑑(𝑥𝑎−𝑥𝑏), 𝑀} = min{𝑑(𝑥𝑎−ˆ𝑥𝑏), 𝑀}
Hence, 𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) ≥min{𝑑(𝑥𝑎−𝑥𝑏), 𝑀}.
To prove submodularity, consider L.H.S of inequality 14:
𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) + 𝛿𝑎,𝑏(𝑦𝑎+ 1, 𝑦𝑏+ 1) = 𝛿𝑎,𝑏(𝑦𝑎, 0) + 𝛿𝑎,𝑏(𝑦𝑎+ 1, 1)
= 𝑀+ 𝑑(𝑦𝑎−1) + 𝑑(𝑦𝑎)
The R.H.S of inequality 14 is given by:
𝛿𝑎,𝑏(𝑦𝑎+ 1, 𝑦𝑏) + 𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏+ 1) = 𝛿𝑎,𝑏(𝑦𝑎+ 1, 0) + 𝛿𝑎,𝑏(𝑦𝑎, 1)
= 𝑀+ 𝑑(𝑦𝑎) + 𝑑(𝑦𝑎−1)
Hence L.H.S = R.H.S for this case.
Case 4: 𝑦𝑎̸= 0, 𝑦𝑏̸= 0
𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) = 𝑑(𝑦𝑎−𝑦𝑏)
Hence, 𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) ≥min{𝑑(𝑥𝑎−𝑥𝑏), 𝑀}.
To prove submodularity, consider L.H.S of inequality 14:
𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏) + 𝛿𝑎,𝑏(𝑦𝑎+ 1, 𝑦𝑏+ 1) = 2 · 𝑑(𝑦𝑎−𝑦𝑏)
The R.H.S of inequality 14 is given by:
𝛿𝑎,𝑏(𝑦𝑎+ 1, 𝑦𝑏) + 𝛿𝑎,𝑏(𝑦𝑎, 𝑦𝑏+ 1) = 𝑑(𝑦𝑎−𝑦𝑏−1) + 𝑑(𝑦𝑎−𝑦𝑏+ 1)
Since 𝑑() is convex, L.H.S ≤R.H.S for this case.
This completes our proof of proposition 1. ■
24


## Page 25


B
Proof of Lemma 1
Lemma 1: Graph (a) of ﬁgure 3 exactly models clique potentials that are proportional to the sum of 𝑚
maximum convex distance functions over all disjoint pairs of random variables of the clique.
Proof:
Let us arrange the labels assigned to Xc in increasing order as {𝑙𝑘1, . . . , 𝑙𝑘𝑐}, where 𝑐= |Xc|
indicates the size of the clique. The sum of 𝑚maximum convex distance functions over all disjoint pairs of
random variables of the clique is given by:
𝜔c(𝑑(𝑘𝑐−𝑘1) + 𝑑(𝑘𝑐−1 −𝑘2) + .... + 𝑑(𝑘𝑐−𝑚+1 −𝑘𝑚))
(15)
When 𝑖∈[𝑘𝑝+1, 𝑘𝑝+1], exactly 𝑝variables in Xc are assigned a label between [𝑙𝑘1, 𝑙𝑘𝑝] and the corresponding
𝑝vertices among {𝑉1
𝑖, 𝑉2
𝑖....𝑉𝑐
𝑖} will be in Vt (the remaining 𝑐−𝑡vertices will be in Vs). Similarly, when
𝑗∈[𝑘𝑐−𝑝+ 1, 𝑘𝑐−𝑝+1], exactly 𝑝variables in Xc are assigned a label in the range [𝑙𝑘𝑐−𝑝+1, 𝑙𝑘𝑐] and the
corresponding 𝑝vertices among {𝑉1
𝑗, 𝑉2
𝑗....𝑉𝑐
𝑗} will be in Vs (the remaining 𝑐−𝑝vertices will be in Vt).
𝑠𝑡-MINCUT includes either the arcs (𝑈𝑖𝑗, 𝑉𝑎
𝑖) for all 𝑉𝑎
𝑖∈Vt or the arcs (𝑉𝑎
𝑗, 𝑊𝑖𝑗) for all 𝑉𝑎
𝑗∈Vs or the
arc (𝑊𝑖𝑗, 𝑈𝑖𝑗), whichever contribute the smallest cost to the cut. Let 𝐶𝑖𝑗denote the sum of capacitites of arcs
cut by 𝑠𝑡-MINCUT in graph (a) of ﬁgure 3 for a given pair 𝑖, 𝑗. Clearly, 0 ≤𝐶𝑖𝑗≤𝑚· 𝑟𝑖𝑗.
Let us partition the interval [𝑘1 + 1, 𝑘𝑐] to 2𝑚−1 intervals [𝑘1 + 1, 𝑘2], [𝑘2 + 1, 𝑘3], ...[𝑘𝑚+
1, 𝑘𝑐−𝑚+1]..., [𝑘𝑐−2 + 1, 𝑘𝑐−1], [𝑘𝑐−1 + 1, 𝑘𝑐]. 𝐶𝑖𝑗depends on the intervals in which 𝑖and 𝑗lie. Given a
labeling xc, the total contribution of all the cut arcs is equal to
𝑘𝑐
∑︁
𝑖=𝑘1+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗=
𝑘2
∑︁
𝑖=𝑘1+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗+
𝑘3
∑︁
𝑖=𝑘2+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗
+ · · · +
𝑘𝑐−𝑚+1
∑︁
𝑖=𝑘𝑚+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗+ · · · +
𝑘𝑐
∑︁
𝑖=𝑘𝑐−1+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗
(16)
Consider the second term of the series in (16). When 𝑖∈[𝑘2 +1, 𝑘3], exactly 2 variables in Xc take up a label
in the range [𝑘1, 𝑘2] and hence, two vertices among {𝑉1
𝑖, 𝑉2
𝑖....𝑉𝑐
𝑖} belong to Vt. When 𝑗∈[𝑘𝑐−1 + 1, 𝑘𝑐],
only one vertex among {𝑉1
𝑗, 𝑉2
𝑗....𝑉𝑐
𝑗} belongs to Vs, giving 𝐶𝑖𝑗as 𝑟𝑖𝑗. For 𝑗in all other intervals, at least
two vertices among {𝑉1
𝑗, 𝑉2
𝑗....𝑉𝑐
𝑗} belong to Vs, and 𝐶𝑖𝑗equals 2 · 𝑟𝑖𝑗. Thus, the following holds
𝑘3
∑︁
𝑖=𝑘2+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗=
𝑘3
∑︁
𝑖=𝑘2+1
𝑘𝑐
∑︁
𝑗=𝑘𝑐−1+1
𝑟𝑖𝑗+
𝑘3
∑︁
𝑖=𝑘2+1
𝑘𝑐−1
∑︁
𝑗=𝑖
2𝑟𝑖𝑗
=
𝑘3
∑︁
𝑖=𝑘2+1
𝑘𝑐
∑︁
𝑗=𝑘𝑐−1+1
𝑟𝑖𝑗+
⎛
⎝
𝑘3
∑︁
𝑖=𝑘2+1
𝑘𝑐−1
∑︁
𝑗=𝑖
𝑟𝑖𝑗+
𝑘3
∑︁
𝑖=𝑘2+1
𝑘𝑐−1
∑︁
𝑗=𝑖
𝑟𝑖𝑗
⎞
⎠
=
𝑘3
∑︁
𝑖=𝑘2+1
𝑘𝑐
∑︁
𝑗=𝑖
𝑟𝑖𝑗+
𝑘3
∑︁
𝑖=𝑘2+1
𝑘𝑐−1
∑︁
𝑗=𝑖
𝑟𝑖𝑗
where the last step is obtained by combining the ﬁrst and the third terms in the summation.
25


## Page 26


In general, for 𝑝∈[1, 𝑚−1] we can write
𝑘𝑝+1
∑︁
𝑖=𝑘𝑝+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗=
𝑘𝑝+1
∑︁
𝑖=𝑘𝑝+1
𝑘𝑐
∑︁
𝑗=𝑖
𝑟𝑖𝑗+
𝑘𝑝+1
∑︁
𝑖=𝑘𝑝+1
𝑘𝑐−1
∑︁
𝑗=𝑖
𝑟𝑖𝑗+ · · · +
𝑘𝑝+1
∑︁
𝑖=𝑘𝑝+1
𝑘𝑐−𝑝+1
∑︁
𝑗=𝑖
𝑟𝑖𝑗
(17)
Similar argument can be extended for 𝑝∈[𝑐−𝑚+ 1, 𝑐−1]
Using (17), each term of (16) can be written as
𝑘2
∑︁
𝑖=𝑘1+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗=
𝑘2
∑︁
𝑖=𝑘1+1
𝑘𝑐
∑︁
𝑗=𝑖
𝑟𝑖𝑗
𝑘3
∑︁
𝑖=𝑘2+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗=
𝑘3
∑︁
𝑖=𝑘2+1
𝑘𝑐
∑︁
𝑗=𝑖
𝑟𝑖𝑗+
𝑘3
∑︁
𝑖=𝑘2+1
𝑘𝑐−1
∑︁
𝑗=𝑖
𝑟𝑖𝑗
𝑘4
∑︁
𝑖=𝑘3+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗=
𝑘4
∑︁
𝑖=𝑘3+1
𝑘𝑐
∑︁
𝑗=𝑖
𝑟𝑖𝑗+
𝑘4
∑︁
𝑖=𝑘3+1
𝑘𝑐−1
∑︁
𝑗=𝑖
𝑟𝑖𝑗+
𝑘4
∑︁
𝑖=𝑘3+1
𝑘𝑐−2
∑︁
𝑗=𝑖
𝑟𝑖𝑗
...
𝑘𝑐−𝑚+1
∑︁
𝑖=𝑘𝑚+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗=
𝑘𝑐−𝑚+1
∑︁
𝑖=𝑘𝑚+1
𝑘𝑐
∑︁
𝑗=𝑖
𝑟𝑖𝑗+
𝑘𝑐−𝑚+1
∑︁
𝑖=𝑘𝑚+1
𝑘𝑐−1
∑︁
𝑗=𝑖
𝑟𝑖𝑗+ · · · · · · +
𝑘𝑐−𝑚+1
∑︁
𝑖=𝑘𝑚+1
𝑘𝑐−𝑚+1
∑︁
𝑗=𝑖
𝑟𝑖𝑗
...
𝑘𝑐−2
∑︁
𝑖=𝑘𝑐−3+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗=
𝑘𝑐−2
∑︁
𝑖=𝑘𝑐−3+1
𝑘𝑐
∑︁
𝑗=𝑖
𝑟𝑖𝑗+
𝑘𝑐−2
∑︁
𝑖=𝑘𝑐−3+1
𝑘𝑐−1
∑︁
𝑗=𝑖
𝑟𝑖𝑗+
𝑘𝑐−2
∑︁
𝑖=𝑘𝑐−3+1
𝑘𝑐−2
∑︁
𝑗=𝑖
𝑟𝑖𝑗
𝑘𝑐−1
∑︁
𝑖=𝑘𝑐−2+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗=
𝑘𝑐−1
∑︁
𝑖=𝑘𝑐−2+1
𝑘𝑐
∑︁
𝑗=𝑖
𝑟𝑖𝑗+
𝑘𝑐−1
∑︁
𝑖=𝑘𝑐−2+1
𝑘𝑐−1
∑︁
𝑗=𝑖
𝑟𝑖𝑗
𝑘𝑐
∑︁
𝑖=𝑘𝑐−1+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗=
𝑘𝑐
∑︁
𝑖=𝑘𝑐−1+1
𝑘𝑐
∑︁
𝑗=𝑖
𝑟𝑖𝑗
Adding all the above equations by adding all terms vertically, we obtain
𝑘𝑐
∑︁
𝑖=𝑘1+1
𝑘𝑐
∑︁
𝑗=𝑖
𝐶𝑖𝑗=
𝑘𝑐
∑︁
𝑖=𝑘1+1
𝑘𝑐
∑︁
𝑗=𝑖
𝑟𝑖𝑗+
𝑘𝑐−1
∑︁
𝑖=𝑘2+1
𝑘𝑐−1
∑︁
𝑗=𝑖
𝑟𝑖𝑗+ · · · +
𝑘𝑐−𝑚+1
∑︁
𝑖=𝑘𝑚+1
𝑘𝑐−𝑚+1
∑︁
𝑗=𝑖
𝑟𝑖𝑗
= 𝜔c𝑑(𝑘𝑐−𝑘1) + 𝜔c𝑑(𝑘𝑐−1 −𝑘2) + · · · + 𝜔c𝑑(𝑘𝑐−𝑚+1 −𝑘𝑚)
Hence, graph (a) of ﬁgure 3 represents exactly clique potentials that are proportional to the sum of 𝑚
maximum convex distance functions over all disjoint pairs of random variables of the clique.
■
26


## Page 27


C
Proof of Lemma 2
Lemma 2: At an iteration of our algorithm, given the current labeling 𝑓𝑛and an interval 𝐼𝑛= [𝑖𝑛+ 1, 𝑗𝑛],
the new labeling 𝑓𝑛+1 obtained by solving the st-mincut problem reduces the energy by at least the following:
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓𝑛(𝑎)) +
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)∪ℬ(𝑓,𝐼𝑛)
𝜃c(xc)
−
⎛
⎝
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓*(𝑎)) +
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)
𝑡𝑛
𝑐+
∑︁
Xc∈ℬ(𝑓,𝐼𝑛)
𝑠𝑛
𝑐
⎞
⎠
Proof:
It is evident from the properties of the graph discussed in subsection 6.2.1 that the energy of the new
labeling 𝑓𝑛+1 is bounded from above by the cost of the 𝑠𝑡-mincut. The cost of the 𝑠𝑡-mincut itself is bounded
from above by the cost of any other 𝑠𝑡-cut in the graph. Consider one such 𝑠𝑡-cut that gives the following
labeling:
𝑓(𝑎) =
{︂𝑓*(𝑎)
𝑖𝑓𝑋𝑎∈X(𝑓*, 𝐼𝑛)
𝑓𝑛(𝑎)
𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒.
We can derive the cost of this 𝑠𝑡-cut using the properties of subsection 6.2.1. The energy of 𝑓equals the sum
of the terms in the properties minus ∑︀
𝑐∈𝒞𝜅𝑐. The energy of 𝑓𝑛+1 is less than that of 𝑓. Hence, the difference
between the energy of the current labeling 𝑓𝑛and the new labeling 𝑓𝑛+1, i.e 𝐸(𝑓𝑛) −𝐸(𝑓𝑛+1), is at least
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓𝑛(𝑎)) +
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)∪ℬ(𝑓,𝐼𝑛)
𝜃c(xc)
−
⎛
⎝
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓*(𝑎)) +
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)
𝑡𝑛
𝑐+
∑︁
Xc∈ℬ(𝑓,𝐼𝑛)
𝑠𝑛
𝑐
⎞
⎠
This proves the lemma.
■
27


## Page 28


D
Proof of Lemma 3
Lemma 3: When 𝑑(.) is linear, that is, 𝑑(𝑥) = |𝑥|, the following inequality holds true:
1
𝐿
∑︁
𝑟
∑︁
𝐼𝑛∈Γ𝑟
⎛
⎝
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)
𝑡𝑛
𝑐+
∑︁
Xc∈ℬ(𝑓,𝐼𝑛)
𝑠𝑛
𝑐
⎞
⎠
≤𝑚𝑎𝑥
{︂𝑐
2
(︂
2 + 𝐿
𝑀
)︂
,
(︂
2 + 2𝑀
𝐿
)︂}︂∑︁
c∈𝒞
𝜃c(xc)
(18)
where c is the largest clique in the random ﬁeld.
Proof:
Let us denote the set of optimum labels in a clique Xc arranged in an increasing order as
𝑙1, 𝑙2....., 𝑙𝑐−1, 𝑙𝑐. For notational simplicity, we introduce a new notation 𝐿= ℎ′. Since we are dealing
with the truncated linear metric, the terms 𝑡𝑛
𝑐and 𝑠𝑛
𝑐can be simpliﬁed as:
𝑡𝑛
𝑐= 𝜔𝑐(𝑙𝑐−𝑙1), 𝑠𝑛
𝑐= 𝜔𝑐(𝑙𝑐−𝑖𝑛−1 + 𝑀)
(19)
The LHS of inequality in lemma 3 can be written as:
1
𝐿
∑︁
c∈𝒞
⎛
⎝
∑︁
𝒜(𝑓,𝐼𝑛)∋c
𝑡𝑛
𝑐+
∑︁
ℬ(𝑓,𝐼𝑛)∋c
𝑠𝑛
𝑐
⎞
⎠
(20)
In order to prove the lemma, we consider the following three cases for each clique Xc:
𝐶𝑎𝑠𝑒−𝐼: |𝑙𝑐−𝑙1| ≥𝐿and hence 𝜃c(xc) = 𝜔c · M
In this case, Xc /∈𝒜(𝑓, 𝐼𝑛) for all intervals 𝐼𝑛since the length of each interval is 𝐿. Moreover, the conditions
for Xc ∈ℬ(𝑓, 𝐼𝑛) are given by
Xc ∈ℬ(𝑓, 𝐼𝑛) ⇐⇒𝑖𝑛∈[𝑙1 −𝐿, 𝑙𝑐−1]
We observe that
∑︁
𝒜(𝑓,𝐼𝑛)∋c
𝑡𝑛
𝑐+
∑︁
ℬ(𝑓,𝐼𝑛)∋c
𝑠𝑛
𝑐
≤𝜔𝑐
𝑐
∑︁
𝑝=1
𝑙𝑝−1
∑︁
𝑙𝑝−𝐿
(𝑀+ 𝑙𝑝−𝑖𝑛−1)
= 𝜔𝑐
𝑐
∑︁
𝑝=1
(︂
𝐿· 𝑀+ 𝐿· (𝐿−1)
2
)︂
= 𝐿· 𝑐
2
(︂
2 + 𝐿−1
𝑀
)︂
𝜃c(xc)
≤𝐿· 𝑐
2
(︂
2 + 𝐿
𝑀
)︂
𝜃c(xc)
(21)
28


## Page 29


𝐶𝑎𝑠𝑒−𝐼𝐼: 𝑀≤|𝑙𝑐−𝑙1| < 𝐿and hence 𝜃c(xc) = 𝜔c · M
In this case, the conditions for Xc ∈𝒜(𝑓, 𝐼𝑛) and 𝑋𝑐∈ℬ(𝑓, 𝐼𝑛) are given by
Xc ∈𝒜(𝑓, 𝐼𝑛) ⇐⇒𝑖𝑛∈[𝑙𝑐−𝐿, 𝑙1 −1]
Xc ∈ℬ(𝑓, 𝐼𝑛) ⇐⇒𝑖𝑛∈[𝑙1 −𝐿, 𝑙𝑐−𝐿−1] ∪[𝑙1, 𝑙𝑐−1]
We observe that
∑︁
𝒜(𝑓,𝐼𝑛)∋c
𝑡𝑛
𝑐+
∑︁
ℬ(𝑓,𝐼𝑛)∋c
𝑠𝑛
𝑐
= 𝜔𝑐
⎛
⎝
𝑙1−1
∑︁
𝑖𝑛=𝑙𝑐−𝐿
(𝑙𝑐−𝑙1) +
⎧
⎨
⎩
𝑐−1
∑︁
𝑝=1
𝑙𝑝+1−𝐿−1
∑︁
𝑖𝑛=𝑙𝑝−𝐿
(𝑀+ 𝑙𝑝−(𝑖𝑛+ 1))
+
𝑙𝑐−1
∑︁
𝑖𝑛=𝑙1
(𝑀+ 𝑙𝑐−(𝑖𝑛+ 1))
}︃)︃
= 𝜔𝑐(𝐴+ 𝐵+ 𝐶)
where
𝐴=
𝑙1−1
∑︁
𝑖𝑛=𝑙𝑐−𝐿
(𝑙𝑐−𝑙1)
𝐵=
𝑐−1
∑︁
𝑝=1
𝑙(𝑝+1)−𝐿−1
∑︁
𝑖𝑛=𝑙𝑝−𝐿
(𝑀+ 𝑙𝑝−(𝑖𝑛+ 1))
𝐶=
𝑙𝑐−1
∑︁
𝑖𝑛=𝑙1
(𝑀+ 𝑙𝑐−(𝑖𝑛+ 1))
Let (𝑙𝑐−𝑙1) = 𝑟. Hence, we have:
𝐴= (𝑙𝑐−𝑙1) · (𝐿−(𝑙𝑐−𝑙1))
= 𝑟· (𝐿−𝑟) = 𝐿· 𝑟−𝑟2
(22)
29


## Page 30


𝐵=
𝑐−1
∑︁
𝑝=1
𝑙(𝑝+1)−𝐿−1
∑︁
𝑖𝑛=𝑙𝑝−𝐿
(𝑀+ 𝑙𝑝−(𝑖𝑛+ 1))
=
𝑐−1
∑︁
𝑝=1
𝑙(𝑝+1)−𝐿−1
∑︁
𝑖𝑛=𝑙𝑝−𝐿
𝑀+
𝑐−1
∑︁
𝑝=1
𝑙(𝑝+1)−𝐿−1
∑︁
𝑖𝑛=𝑙𝑝−𝐿
(𝑙𝑝−(𝑖𝑛+ 1))
=
𝑐−1
∑︁
𝑝=1
𝑀· (𝑙(𝑝+1) −𝑙𝑝)+
𝑐−1
∑︁
𝑝=1
{(𝐿−1) + ..... + (𝐿−(𝑙𝑝+1 −𝑙𝑝))}
Let 𝑦𝑝= 𝑙(𝑝+1) −𝑙𝑝. Clearly
𝑐−1
∑︁
𝑝=1
𝑦𝑝= 𝑙𝑐−𝑙1
Hence,
𝐵= 𝑀· 𝑟+ 𝐿· 𝑟−
𝑐−1
∑︁
𝑝=1
𝑦𝑝· (𝑦𝑝+ 1)
2
= 𝑀· 𝑟+ 𝐿· 𝑟−𝑟
2 −
𝑐−1
∑︁
𝑝=1
(𝑦𝑝)2
2
(23)
𝐶=
𝑙𝑐−1
∑︁
𝑖𝑛=𝑙1
(𝑀+ 𝑙𝑐−(𝑖𝑛+ 1))
=
𝑙𝑐−1
∑︁
𝑖𝑛=𝑙1
𝑀+
𝑙𝑐−1
∑︁
𝑖𝑛=𝑙1
(𝑙𝑐−(𝑖𝑛+ 1))
= 𝑀· (𝑙𝑐−𝑙1) + {(𝑙𝑐−(𝑙1 + 1)) + (𝑙𝑐−(𝑙1 + 2))... + 1}
= 𝑀· (𝑙𝑐−𝑙1) + (𝑙𝑐−𝑙1 −1)(𝑙𝑐−𝑙1)
2
= 𝑀· 𝑟+ (𝑟−1) · 𝑟
2
= 𝑀· 𝑟+ 𝑟2
2 −𝑟
2
(24)
30


## Page 31


Using (22), (23), (24), we have
𝐴+ 𝐵+ 𝐶= (2𝐿+ 2𝑀−𝑟)𝑟+ 𝑟2
2 −𝑟−
𝑐−1
∑︁
𝑝=1
𝑦2
𝑝
2
(25)
We have
𝑐−1
∑︁
𝑝=1
𝑦𝑝2
2
≥
𝑟2
2(𝑐−1)
(Taking each 𝑦𝑝= 𝑟/(𝑐−1))
Hence,
𝐴+ 𝐵+ 𝐶≤
{︂
2𝐿+ 2𝑀−1 −𝑟
2
(︂
𝑐
𝑐−1
)︂}︂
· 𝑟
Let
𝑓(𝑟) =
{︂
2𝐿+ 2𝑀−1 −𝑟
2
(︂
𝑐
𝑐−1
)︂}︂
· 𝑟
Taking derivative of 𝑓(𝑟), we obtain
𝑓′(𝑟) = 2𝐿+ 2𝑀−1 −
𝑟· 𝑐
(𝑐−1)
𝑓(𝑟) is a quadratic function which opens downwards (coefﬁcient of 𝑟2 is negative). Also
𝑓′(𝐿) =
(︂𝑐−2
𝑐−1
)︂
· 𝐿+ 2𝑀−1 > 0
Hence, using 𝑟= 𝐿,
𝐴+ 𝐵+ 𝐶< 𝐿·
{︂
2𝐿+ 2𝑀−1 −𝐿
2 ·
(︂
𝑐
𝑐−1
)︂}︂
< 𝐿·
{︂2𝐿
𝑀+ 2 −𝐿
2𝑀·
(︂
𝑐
𝑐−1
)︂}︂
𝜃c(xc)
(26)
where the last expression is obtained using the fact that 𝜃c(xc) = 𝜔c · M.
𝐶𝑎𝑠𝑒−𝐼𝐼𝐼: |𝑙𝑐−𝑙1| < 𝑀and hence 𝜃c(xc) = 𝜔c(lc −l1)
In this case, the conditions for Xc ∈𝒜(𝑓, 𝐼𝑛) and Xc ∈ℬ(𝑓, 𝐼𝑛) are given by
Xc ∈𝒜(𝑓, 𝐼𝑛) ⇐⇒𝑖𝑛∈[𝑙𝑐−𝐿, 𝑙1 −1]
Xc ∈ℬ(𝑓, 𝐼𝑛) ⇐⇒𝑖𝑛∈[𝑙1 −𝐿, 𝑙𝑐−𝐿−1] ∪[𝑙1, 𝑙𝑐−1]
31


## Page 32


We observe that
∑︁
𝒜(𝑓,𝐼𝑛)∋c
𝑡𝑛
𝑐+
∑︁
ℬ(𝑓,𝐼𝑛)∋c
𝑠𝑛
𝑐
= 𝜔𝑐
⎛
⎝
𝑙1−1
∑︁
𝑖𝑛=𝑙𝑐−𝐿
(𝑙𝑐−𝑙1) +
⎧
⎨
⎩
𝑐−1
∑︁
𝑝=1
𝑙𝑝+1−𝐿−1
∑︁
𝑖𝑛=𝑙𝑝−𝐿
(𝑀+ 𝑙𝑝−(𝑖𝑛+ 1))
+
𝑙𝑐−1
∑︁
𝑖𝑛=𝑙1
(𝑀+ 𝑙𝑐−(𝑖𝑛+ 1))
}︃)︃
= 𝜔𝑐(𝐴+ 𝐵+ 𝐶)
Similar to case II, we can write
𝐴+ 𝐵+ 𝐶= (2𝐿+ 2𝑀−𝑟/2)𝑟−𝑟−
𝑐−1
∑︁
𝑝=1
𝑦2
𝑝
2
Since 𝑟< 𝑀
𝐴+ 𝐵+ 𝐶≤(2𝐿+ 2𝑀)(𝑙𝑐−𝑙1)
= 𝐿
(︂
2 + 2𝑀
𝐿
)︂
𝜃c(xc)
(27)
where the last expression is obtained using the fact that 𝜃c(xc) = 𝜔c · M.
Substituting inequalities (21), (26) and (27) in expression (20) and dividing both sides by 𝐿for all Xc, we
obtain inequality of lemma 3. This proves the lemma.
■
32


## Page 33


E
Proof of Proposition 3
Proposition 3: The range expansion algorithm with ℎ′ = 𝑀has a multiplicative bound of 𝑂(𝐶) for truncated
max-of-linear model when 𝑚= 1. The term 𝐶equals the size of the largest clique. Hence, if x* is a labeling
with minimum energy and ˆx is the labeling estimated by range expansion algorithm then
∑︁
𝑎∈𝒱
𝜃𝑎(ˆ𝑥𝑎) +
∑︁
c∈𝒞
𝜃c(ˆxc) ≤
∑︁
𝑎∈𝒱
𝜃𝑎(𝑥*
𝑎) + 𝑂(𝐶)
∑︁
c∈𝒞
𝜃c(x*
c).
The above inequality holds for arbitrary set of unary potentials and non-negative clique weights.
Proof:
The following equation can be deduced from the above deﬁnitions:
∑︁
𝑋𝑎∈X
𝜃𝑎(𝑓*(𝑎)) =
∑︁
𝐼𝑛∈ℐ𝑟
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓*(𝑎))
(28)
since 𝑓*(𝑎) belongs to exactly one interval in 𝐼𝑟for all 𝑋𝑎.
For the ﬁnal labeling 𝑓of the range expansion algorithm, the term in lemma 2 should be non-positive for all
intervals 𝐼𝑛because 𝑓is a local optimum. Hence,
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓(𝑎)) +
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)∪ℬ(𝑓,𝐼𝑛)
𝜃c(xc)
≤
⎛
⎝
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓*(𝑎)) +
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)
𝑡𝑛
𝑐+
∑︁
Xc∈ℬ(𝑓,𝐼𝑛)
𝑠𝑛
𝑐
⎞
⎠, ∀𝐼𝑛
We sum the above inequality over all 𝐼𝑛∈Γ𝑟. The summation of the LHS is at least 𝐸(𝑓). Also, using (28),
the summation of the above inequality can be written as:
𝐸(𝑓) ≤
∑︁
𝑋𝑎∈X
𝜃𝑎(𝑓*(𝑎)) +
∑︁
𝐼𝑛∈Γ𝑟
⎛
⎝
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)
𝑡𝑛
𝑐+
∑︁
Xc∈ℬ(𝑓,𝐼𝑛)
𝑠𝑛
𝑐
⎞
⎠
We now take the expectation of the above inequality over the uniformly distributed random integer 𝑟∈
[0, 𝐿−1]. The LHS of the inequality and the ﬁrst term on the RHS (that is, ∑︀𝜃𝑎(𝑓*(𝑎))) are constants with
respect to 𝑟. Hence, we get
𝐸(𝑓) ≤
∑︁
𝑋𝑎∈X
𝜃𝑎(𝑓*(𝑎)) + 1
𝐿
∑︁
𝑟
∑︁
𝐼𝑛∈Γ𝑟
⎛
⎝
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)
𝑡𝑛
𝑐+
∑︁
Xc∈ℬ(𝑓,𝐼𝑛)
𝑠𝑛
𝑐
⎞
⎠
(29)
Lemma 3 allows us to write the above inequality as
𝐸(𝑓) ≤
∑︁
𝑋𝑎∈X
𝜃𝑎(𝑓*(𝑎)) + 𝑚𝑎𝑥
{︂𝑐
2
(︂
2 + 𝐿
𝑀
)︂
,
(︂
2 + 2𝑀
𝐿
)︂}︂∑︁
c∈𝒞
𝜃c(xc)
(30)
The R.H.S of lemma 3 is minimum under the following condition:
33


## Page 34


𝑐
2
(︂
2 + 𝐿
𝑀
)︂
=
(︂
2 + 2𝑀
𝐿
)︂
(31)
The positive solution of the above quadratic equation gives the optimum value 𝐿𝑜𝑝𝑡of interval length:
𝐿𝑜𝑝𝑡=
{︃
2 −𝑐+
√
𝑐2 + 4
𝑐
}︃
· 𝑀
(32)
However, we bound the minimum value of L as M, giving:
𝐿𝑜𝑝𝑡= 𝑚𝑎𝑥
{︃{︃
2 −𝑐+
√
𝑐2 + 4
𝑐
}︃
· 𝑀, 𝑀
}︃
(33)
Note 𝐿𝑜𝑝𝑡equals
√
2𝑀for 𝑐= 2 and 𝑀for 𝑐> 2. Substituting the optimum value of L from equation 33 in
inequality of lemma 3 and simplifying inequality 12 gives the multiplicative bound for truncated max-of-linear
model as (𝑐+2)+
√
𝑐2+4
2
. Hence, the multiplicative bound is 𝑂(𝑐) where 𝑐is the size of the maximal clique.
For 𝑐= 2, this gives a bound of 2 +
√
2 using 𝐿=
√
2𝑀.
■
34


## Page 35


F
Proof of Proposition 4
Proposition 4: The range expansion algorithm with ℎ′ = 𝑀has a multiplicative bound of 𝑂(𝑚· 𝐶) for
truncated max-of-linear model for any general value of 𝑚. The term 𝐶equals the size of the largest clique.
Hence, if x* is a labeling with minimum energy and ˆx is the labeling estimated by range expansion algorithm
then
∑︁
𝑎∈𝒱
𝜃𝑎(ˆ𝑥𝑎) +
∑︁
c∈𝒞
𝜃c(ˆxc) ≤
∑︁
𝑎∈𝒱
𝜃𝑎(𝑥*
𝑎) + 𝑂(𝑚· 𝐶)
∑︁
c∈𝒞
𝜃c(x*
c).
The above inequality holds for arbitrary set of unary potentials and non-negative clique weights.
Proof:
We introduce some notations for our proof. Let 𝒜(𝑓, 𝐼𝑛) be the set of all cliques for which all
variables take optimum label in the interval 𝐼𝑛and ℬ𝑘(𝑓, 𝐼𝑛) where 𝑘∈[1, . . . , 𝑚−1] be the set of all
cliques for which exactly 𝑘variables retain their old label. Let ℬ𝑚(𝑓, 𝐼𝑛) be the set of all cliques for which
𝑚or more variables retain their old label.
We also introduce the following shorthand notation:
∙We denote 𝜔c{∑︀𝑚
𝑖=1 𝑑(𝑝𝑖(x𝑐) −𝑝𝑐−𝑖+1(x𝑐)} as 𝑡𝑛
𝑚,𝑐
∙We denote 𝜔c{∑︀𝑚−1
𝑖=2 𝑑(𝑝𝑖(x𝑐) −𝑝𝑐−𝑖+1(x𝑐) + 𝑑(𝑝𝑐(x𝑐) −𝑖𝑚−1)} + 𝜔c · 𝑀as 𝑠𝑛
1,𝑐
∙In general, we denote 𝜔c{∑︀𝑚−𝑘
𝑖=𝑘+1 𝑑(𝑝𝑖(x𝑐)−𝑝𝑐−𝑖+1(x𝑐)+∑︀𝑘
𝑖=1 𝑑(𝑝𝑐−𝑖+1(x𝑐)−𝑖𝑚−1)}+k·𝜔c·
𝑀as 𝑠𝑛
𝑘,𝑐
We state the following lemma which is a generalization of lemma 2.
Lemma 4. At an iteration of our algorithm, given the current labeling 𝑓𝑛and an interval 𝐼𝑛= [𝑖𝑛+ 1, 𝑗𝑛],
the new labeling 𝑓𝑛+1 obtained by solving the st-mincut problem reduces the energy by at least the following:
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓𝑛(𝑎)) +
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)∪ℬ1(𝑓,𝐼𝑛)∪···∪ℬ𝑚(𝑓,𝐼𝑛)
𝜃c(xc)
−
⎛
⎝
∑︁
𝑋𝑎∈X(𝑓*,𝐼𝑛)
𝜃𝑎(𝑓*(𝑎)) +
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)
𝑡𝑛
𝑚,𝑐+
∑︁
Xc∈ℬ1(𝑓,𝐼𝑛)
𝑠𝑛
1,𝑐+ · · · +
∑︁
Xc∈ℬ𝑚(𝑓,𝐼𝑛)
𝑠𝑛
𝑚,𝑐
⎞
⎠
We also make use of the following lemma which generalizes lemma 3:
Lemma 5. When 𝑑(.) is linear, that is, 𝑑(𝑥) = |𝑥|, the following inequality holds true:
1
𝐿
∑︁
𝑟
∑︁
𝐼𝑛∈Γ𝑟
⎛
⎝
∑︁
Xc∈𝒜(𝑓,𝐼𝑛)
𝑡𝑛
𝑚,𝑐+
∑︁
Xc∈ℬ1(𝑓,𝐼𝑛)
𝑠𝑛
1,𝑐+ · · · +
∑︁
Xc∈ℬ𝑚(𝑓,𝐼𝑛)
𝑠𝑛
𝑚,𝑐
⎞
⎠
≤𝑚𝑎𝑥
{︂
𝑚· 𝑐
2
(︂
2 + 𝐿
𝑀
)︂
,
(︂
2 + 2𝑀
𝐿
)︂}︂∑︁
c∈𝒞
𝜃c(xc)
(34)
where c is the largest clique in the random ﬁeld.
35


## Page 36


Let us denote the set of optimum labels in a clique Xc arranged in an increasing order as 𝑙1, 𝑙2....., 𝑙𝑐−1, 𝑙𝑐.
Since we are dealing with the truncated linear metric, the terms 𝑡𝑛
𝑚,𝑐and 𝑠𝑛
𝑘,𝑐can be simpliﬁed as:
𝑡𝑛
𝑚,𝑐= 𝜔𝑐{(𝑙𝑐−𝑙1) + (𝑙𝑐−1 −𝑙2) + · · · + (𝑙𝑐−𝑚+1 −𝑙𝑚)}
𝑠𝑛
1,𝑐= 𝜔𝑐{(𝑙𝑐−𝑖𝑛−1 + 𝑀) + (𝑙𝑐−1 −𝑙2) + · · · + (𝑙𝑐−𝑛+1 −𝑙𝑛)}
...
𝑠𝑛
𝑚,𝑐= 𝜔𝑐{(𝑙𝑐−𝑖𝑛−1 + 𝑀) + (𝑙𝑐−1 −𝑖𝑛−1 + 𝑀) + · · · + (𝑙𝑐−𝑛+1 −𝑖𝑛−1 + 𝑀)}
Since the labels are sorted in ascending order {𝑙1, . . . , 𝑙𝑐}, it follows that
𝑡𝑛
𝑚,𝑐≤𝜔𝑐· 𝑚· {𝑙𝑐−𝑙1}
𝑠𝑛
1,𝑐≤𝜔𝑐· 𝑚· {𝑙𝑐−𝑖𝑛−1 + 𝑀}
...
𝑠𝑛
𝑚,𝑐≤𝜔𝑐· 𝑚· {𝑙𝑐−𝑖𝑛−1 + 𝑀}
The LHS of inequality in lemma 5 can be written as:
1
𝐿
∑︁
c∈𝒞
⎛
⎝
∑︁
𝒜(𝑓,𝐼𝑛)∋c
𝑡𝑛
𝑚,𝑐+
∑︁
ℬ1(𝑓,𝐼𝑛)∋c
𝑠𝑛
1,𝑐+ · · · +
∑︁
ℬ𝑚(𝑓,𝐼𝑛)∋c
𝑠𝑛
𝑚,𝑐
⎞
⎠
≤1
𝐿
∑︁
c∈𝒞
⎛
⎝
∑︁
𝒜(𝑓,𝐼𝑛)∋c
𝜔𝑐· 𝑚· {𝑙𝑐−𝑙1} +
∑︁
ℬ1(𝑓,𝐼𝑛)∋c
𝜔𝑐· 𝑚· {𝑙𝑐−𝑖𝑛−1 + 𝑀} + . . .
+
∑︁
ℬ𝑚(𝑓,𝐼𝑛)∋c
𝜔𝑐· 𝑚· {𝑙𝑐−𝑖𝑛−1 + 𝑀}
⎞
⎠
≤1
𝐿
∑︁
c∈𝒞
⎛
⎝
∑︁
𝒜(𝑓,𝐼𝑛)∋c
𝜔𝑐· 𝑚· {𝑙𝑐−𝑙1} +
∑︁
ℬ1(𝑓,𝐼𝑛)∪···∪ℬ𝑚(𝑓,𝐼𝑛)∋c
𝜔𝑐· 𝑚· {𝑙𝑐−𝑖𝑛−1 + 𝑀}
⎞
⎠
= 𝑚· 1
𝐿
∑︁
c∈𝒞
⎛
⎝
∑︁
𝒜(𝑓,𝐼𝑛)∋c
𝜔𝑐· 𝑡𝑛
𝑐+
∑︁
ℬ(𝑓,𝐼𝑛)∋c
𝜔𝑐· 𝑠𝑛
𝑐
⎞
⎠
(35)
The last expression in equation 35 is 𝑚times expression 20. The analysis below follows the same steps as in
lemma 3.
In order to prove the lemma, we consider the following three cases for each clique Xc:
𝐶𝑎𝑠𝑒−𝐼: |𝑙𝑐−𝑙1| ≥𝐿and hence 𝜔𝑐· 𝑀≤𝜃c(xc) ≤𝜔𝑐· 𝑚· 𝑀
36


## Page 37


This results in
𝑚· 1
𝐿
∑︁
c∈𝒞
⎛
⎝
∑︁
𝒜(𝑓,𝐼𝑛)∋c
𝜔𝑐· 𝑡𝑛
𝑐+
∑︁
ℬ(𝑓,𝐼𝑛)∋c
𝜔𝑐· 𝑠𝑛
𝑐
⎞
⎠≤𝑚· 𝑐
2
(︂
2 + 𝐿
𝑀
)︂
𝜔𝑐· 𝑀
≤𝑚· 𝑐
2
(︂
2 + 𝐿
𝑀
)︂
𝜃c(xc)
(36)
𝐶𝑎𝑠𝑒−𝐼𝐼: 𝑀≤|𝑙𝑐−𝑙1| < 𝐿and hence 𝜔𝑐· 𝑀≤𝜃c(xc) ≤𝜔𝑐· 𝑚· 𝑀
This gives
𝑚· 1
𝐿
∑︁
c∈𝒞
⎛
⎝
∑︁
𝒜(𝑓,𝐼𝑛)∋c
𝜔𝑐· 𝑡𝑛
𝑐+
∑︁
ℬ(𝑓,𝐼𝑛)∋c
𝜔𝑐· 𝑠𝑛
𝑐
⎞
⎠≤𝑚·
{︂2𝐿
𝑀+ 2 −𝐿
2𝑀·
(︂
𝑐
𝑐−1
)︂}︂
𝜔𝑐· 𝑀
≤𝑚·
{︂2𝐿
𝑀+ 2 −𝐿
2𝑀·
(︂
𝑐
𝑐−1
)︂}︂
𝜃c(xc)
(37)
𝐶𝑎𝑠𝑒−𝐼𝐼𝐼: |𝑙𝑐−𝑙1| < 𝑀and hence 𝜔𝑐(𝑙𝑐−𝑙1) ≤𝜃c(xc) ≤𝑚· 𝜔𝑐(𝑙𝑐−𝑙1)
This leads to
oo
𝑚· 1
𝐿
∑︁
c∈𝒞
⎛
⎝
∑︁
𝒜(𝑓,𝐼𝑛)∋c
𝜔𝑐· 𝑡𝑛
𝑐+
∑︁
ℬ(𝑓,𝐼𝑛)∋c
𝜔𝑐· 𝑠𝑛
𝑐
⎞
⎠≤𝑚· (2𝐿+ 2𝑀)(𝑙𝑐−𝑙1)
≤𝑚· 𝐿
(︂
2 + 2𝑀
𝐿
)︂
𝜃c(xc)
(38)
Substituting inequalities (36), (37) and (38) in expression (35), we obtain inequality of lemma 5. This proves
the lemma. ■
Making use of lemmas 4 and 5, the proof of proposition 4 follows exactly the same steps as that of proposi-
tion 3.
37

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
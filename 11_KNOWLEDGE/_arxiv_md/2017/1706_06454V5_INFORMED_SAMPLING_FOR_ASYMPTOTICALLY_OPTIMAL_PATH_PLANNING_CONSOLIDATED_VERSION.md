---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1706.06454v5
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1706.06454v5_Informed_Sampling_for_Asymptotically_Optimal_Path_Planning__Consolidated_Version

> Source: 1706.06454v5_Informed_Sampling_for_Asymptotically_Optimal_Path_Planning__Consolidated_Version.pdf

> Pages: 24

---


## Page 1


Informed Sampling for Asymptotically Optimal
Path Planning (Consolidated Version)
Jonathan D. Gammell, Member, IEEE,
Timothy D. Barfoot, Senior Member, IEEE, and Siddhartha S. Srinivasa, Senior Member, IEEE
Abstract—Anytime almost-surely asymptotically optimal plan-
ners, such as RRT*, incrementally ﬁnd paths to every state in the
search domain. This is inefﬁcient once an initial solution is found
as then only states that can provide a better solution need to be
considered. Exact knowledge of these states requires solving the
problem but can be approximated with heuristics.
This paper formally deﬁnes these sets of states and demon-
strates how they can be used to analyze arbitrary planning
problems. It uses the well-known L2 norm (i.e., Euclidean dis-
tance) to analyze minimum-path-length problems and shows that
existing approaches decrease in effectiveness factorially (i.e., faster
than exponentially) with state dimension. It presents a method
to address this curse of dimensionality by directly sampling the
prolate hyperspheroids (i.e., symmetric n-dimensional ellipses)
that deﬁne the L2 informed set.
The importance of this direct informed sampling technique
is demonstrated with Informed RRT*. This extension of RRT*
has less theoretical dependence on state dimension and problem
size than existing techniques and allows for linear convergence
on some problems. It is shown experimentally to ﬁnd better so-
lutions faster than existing techniques on both abstract planning
problems and HERB, a two-arm manipulation robot.
Index Terms—path planning, sampling-based planning, opti-
mal path planning, informed sampling.
I. INTRODUCTION
T
HERE are many powerful path planning techniques
in robotics. Popular approaches include graph-based
searches, such as Dijkstra’s algorithm [1] and A* [2], and
sampling-based methods, such as Probabilistic Roadmaps
(PRM) [3], Expansive Space Trees (EST) [4], and Rapidly-
exploring Random Trees (RRT) [5]. While sampling-based
methods avoid the challenges of a priori discretizations, their
stochastic nature limits their formal performance. They are
said to be probabilistically complete if the probability of
ﬁnding a solution, if one exists, approaches unity with an
inﬁnite number of samples. They are also said to be almost-
surely asymptotically optimal if the probability of converging
asymptotically to the optimum, if one exists, approaches unity
with an inﬁnite number of samples (e.g., RRT* [6]).
J. D. Gammell performed this work as a member of the Autonomous Space
Robotics Lab at the University of Toronto Institute for Aerospace Studies. He
is now with the Oxford Robotics Institute at the University of Oxford, Oxford,
United Kingdom. Email: gammell@robots.ox.ac.uk
T. D. Barfoot is with the Autonomous Space Robotics Lab at the University
of Toronto Institute for Aerospace Studies, Toronto, Ontario, Canada. Email:
tim.barfoot@utoronto.ca
S. S. Srinivasa is with the School of Computer Science and En-
gineering, University of Washington, Seattle, Washington, USA. Email:
siddh@cs.uw.edu
Manuscript submitted June 20, 2017.
Boundary heuristic
(a)
(c)
(b)
Path heuristic
L2 heuristic
Omniscient set
Fig. 1. An illustration of how the set of states that can improve solution length
shrinks as better solutions are found. Common estimates of this omniscient
set are illustrated as informed sets. The L2 informed set always contains
the entire omniscient set (i.e., 100% recall) and shrinks along with it as a
function of the current solution (i.e., high precision). It is exactly equal to the
omniscient set in the absence of obstacles and constraints (i.e., 100% recall
and precision). This paper shows that direct sampling this L2 informed set
is a necessary condition for almost-surely asymptotically optimal planners to
scale effectively to high state dimensions. This technique is demonstrated with
Informed RRT*.
RRT searches a planning problem by incrementally building
a tree through free space. RRT* extends this procedure to incre-
mentally rewire the tree during its construction. This rewiring
locally optimizes every vertex in the tree and allows the algo-
rithm to almost-surely converge asymptotically to the optimal
path to every state in the problem domain. This is an inefﬁcient
way to ﬁnd the optimal solution to a single planning query.
The only states that need to be considered in single-query
scenarios are those that can provide a better solution [7]. While
exact knowledge of these states requires solving the planning
problem, they can often be approximated with heuristics
(Fig. 1). These heuristics have previously been used to focus
almost-surely asymptotically optimal search [8, 9] but can also
provide insight into the optimal planning problem.
This paper uses the set of states that can provide a better
solution to analyze incremental almost-surely asymptotically
optimal planning. It formally deﬁnes this shrinking set as
the omniscient set and shows that sampling it is a necessary
condition for RRT*-style planners to improve a solution. It
deﬁnes estimates of this set as informed sets and provides
metrics to quantify them in terms of their compactness (i.e.,
precision) and completeness (i.e., recall). It uses these results
to bound the probability of improving a solution to a holonomic
planning problem by the probability of sampling an informed
set with 100% recall.
The L2 norm (i.e., Euclidean distance) is a well-known
heuristic for problems seeking to minimize path length. It
describes the omniscient set exactly in the absence of obstacles
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.
arXiv:1706.06454v5  [cs.RO]  17 Aug 2018


## Page 2


and constraints (i.e., it is sharp1) and always contains the
omniscient set of a problem (i.e., it is universally admissible).
This paper uses it to analyze the minimum-path-length problem
and shows that existing focusing techniques (e.g., [8, 9])
are ineffective in high state dimensions. It is proven that
these rejection-sampling approaches have a probability of
improving a solution that goes to zero factorially (i.e., faster
than exponentially) as state dimension increases.
This paper demonstrates how this minimum-path-length
curse of dimensionality can be reduced by directly sampling the
symmetric n-dimensional ellipse (i.e., prolate hyperspheroid),
the L2 informed set. The presented direct sampling approach
always ﬁnds states that are believed to belong to a better
solution regardless of the relative size of the L2 informed
set. It outperforms existing focusing techniques by orders of
magnitude as state dimension increases.
The informed search approach is demonstrated with Informed
RRT*. This extension of RRT* uses direct informed sam-
pling and admissible graph pruning to focus the search for
improvements. It is shown analytically to outperform existing
techniques in terms of convergence rate, especially in high
state dimensions, and to result in linear convergence on some
problems. It is probabilistically complete and almost-surely
asymptotically optimal. When the L2 heuristic does not provide
additional information (e.g., small planning problems and/or
large informed sets) it is identical to RRT*. A version of
Informed RRT* is publicly available in the Open Motion
Planning Library (OMPL) [10].
Informed RRT* is evaluated experimentally on abstract prob-
lems and on the CMU Personal Robotic Lab’s Home Exploring
Robot Butler (HERB) [11], a 14-degree-of-freedom (DOF)
mobile manipulation platform. These experiments show that
it outperforms existing focusing techniques as state dimension
increases, especially in problems with large planning domains.
This paper is organized as follows. Section II deﬁnes
omniscient and informed sets and their associated precision
and recall in preparation for the literature review presented in
Section III. Section IV presents a direct informed sampling
technique for problems seeking to minimize path length which
is demonstrated with Informed RRT* in Section V. Section VI
analyzes the expected convergence rate of RRT* algorithms and
Section VII demonstrates the practical advantages of this im-
provement on abstract and simulated problems. Section VIII ﬁ-
nally presents a closing discussion and thoughts on future work.
A. Statement of Contributions
This paper is a continuation of ideas ﬁrst published in
[12] and associated technical reports [13, 14] and makes the
following speciﬁc contributions:
• Formally deﬁnes omniscient and informed sets (Deﬁni-
tions 3 and 7) and demonstrates how precision and recall
can be used to quantify the performance of informed
sampling (Deﬁnitions 8 and 9).
1A bound or estimate is said to be sharp if it is exactly equal to the true
value (i.e., has perfect precision and recall) in at least one case.
• Provides upper bounds on the probability that an incre-
mental sampling-based planner improves a solution to a
holonomic planning problem (Theorems 6 and 13).
• Bounds the expected next-iteration cost for RRT* algo-
rithms on any minimum-path-length planning problem
(Lemma 17) and shows that existing formulations of these
algorithms for holonomic planning have a probability of
improving a solution that decreases factorially with state
dimension (Theorem 14).
• Develops a method to reduce this minimum-path-length
curse of dimensionality by directly sampling the ellipsoidal
L2 informed set deﬁned by a goal or countable set of
goals and the current solution (Algs. 1–5).
• Proves that a planning algorithm using this approach,
Informed RRT*, has better theoretical convergence (Theo-
rems 18–20) and experimental performance than existing
focused planning algorithms on holonomic problems.
II. OMNISCIENT AND INFORMED SETS
A formal discussion of the optimal planning problem is
presented in support of the literature review. It includes
deﬁnitions of the states that can provide a better solution, the
omniscient set (Deﬁnition 3), and estimates of this set, informed
sets, quantiﬁed by precision and recall (Deﬁnitions 7–10).
These sets provide theoretical upper bounds on the probability
of improving a solution to a holonomic problem that are used
throughout the remainder of the paper (Theorems 6 and 13).
Finding the optimal path from a start to a goal is formally
deﬁned as the optimal planning problem (Deﬁnition 1). The
given deﬁnition is similar to [6].
Deﬁnition 1 (Optimal planning). Let X ⊆Rn be the state
space of the planning problem, Xobs ⊂X be the states in
collision with obstacles, and Xfree = cl (X \ Xobs) be the
resulting set of permissible states, where cl (·) represents the
closure of a set. Let xstart ∈Xfree be the initial state and
Xgoal ⊂Xfree be the set of desired goal states. Let σ : [0, 1] →
Xfree be a sequence of states through collision-free space that
can be executed by the robot (i.e., a collision-free feasible
path) and Σ be the set of all such nontrivial paths.
The optimal planning problem is then formally deﬁned as the
search for a path, σ∗∈Σ, that minimizes a given cost function,
c : Σ →R≥0, while connecting xstart to xgoal ∈Xgoal,
σ∗= arg min
σ∈Σ
{c (σ) | σ (0) = xstart, σ (1) ∈Xgoal} ,
where R≥0 is the set of non-negative real numbers.
Many sampling-based planners, such as RRT*, probabilisti-
cally converge towards the optimum of these problems. Such
planners are described as probabilistically complete and almost-
surely asymptotically optimal (Deﬁnition 2).
Deﬁnition 2 (Almost-sure asymptotic optimality). A planner
is said to be almost-surely asymptotically optimal if, with an
inﬁnite number of samples, the probability of converging asymp-
totically to the optimum (Deﬁnition 1), if one exists, is one,
P

lim sup
q→∞c (σq) = c (σ∗)

= 1,
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 3


(a)
(b)
Fig. 2. An example of how RRT* almost-surely converges asymptotically to the
optimum by incrementally building and rewiring a tree through the entire prob-
lem domain. RRT* incrementally expands the tree into the problem domain and
improve its connections. By continuing this process indeﬁnitely, it almost-surely
converges asymptotically to the optimal solution by asymptotically improving
every path in the tree. This is inefﬁcient in single-query planning scenarios.
where q is the number of samples, σq is the path found by
the planner from those samples, σ∗is the optimal solution
to the planning problem, and c (·) is the cost of a path.
Once any solution is found, the set of states that can
provide a better solution can be deﬁned as the omniscient
set (Deﬁnition 3).
Deﬁnition 3 (Omniscient set). Let g (x) be the cost of the
optimal path from the start to a state, x ∈Xfree, the optimal
cost-to-come,
g (x) := min
σ∈Σ {c (σ) | σ(0) = xstart, σ(1) = x} ,
and h (x) be the cost of the optimal path from x to the goal
region, the optimal cost-to-go,
h (x) := min
σ∈Σ {c (σ) | σ(0) = x, σ(1) ∈Xgoal} .
The cost of the optimal path from xstart to Xgoal constrained
to pass through x is then given by f (x) := g (x)+h (x). This
deﬁnes the subset of states that can belong to a solution better
than the current solution, ci, as
Xf := {x ∈Xfree | f (x) < ci} .
(1)
Exact knowledge of Xf requires exact knowledge of the entire
planning problem so we refer to it as the omniscient set.
RRT* builds a tree by incrementally adding states from
the problem domain (Fig. 2). A necessary condition for it to
improve a solution is that the newly added state belongs to the
omniscient set (Lemma 4).
Lemma 4 (The necessity of adding states in the omniscient set).
Adding a state from the omniscient set, xnew ∈Xf, is a nec-
essary condition for RRT* to improve the current solution, ci,
ci+1 < ci =⇒xnew ∈Xf.
This condition is necessary but not sufﬁcient to improve
the solution as the ability of states in Xf to provide better
solutions at any iteration depends on the structure of the tree
(i.e., its optimality).
Proof. The proof of Lemma 4 from the supplementary online
material appears in Appendix A-A.
The state added by RRT* at each iteration, xnew, is generated
from a randomly sampled state, xrand, and the nearest vertex
in the existing tree,
vnearest := arg min
v∈V
{∥xrand −v∥2} ,
(2)
through expansion and differential constraints (i.e., the Steer
function). Absent any constraints (i.e., in holonomic planning)
this takes the form
xnew := arg min
y∈X
{∥xrand −y∥2 | ∥y −vnearest∥2 ≤η} ,
(3)
where η is a user-selected maximum edge length.
The number of tree vertices in the problem domain increases
indeﬁnitely with RRT* iterations. With an inﬁnite number of
iterations, eventually all reachable states will be no more than
η away from the nearest vertex in the tree. After these κ
iterations, sampling the omniscient set is a necessary condition
to add a state from the omniscient set and improve the solution
(Lemma 5).
Lemma 5 (The necessity of sampling states in the omniscient
set in holonomic planning). Sampling the omniscient set,
xrand ∈Xf, is a necessary condition for RRT* to improve the
current solution to a holonomic problem, ci, after an initial κ
iterations,
∀i ≥κ, ci+1 < ci =⇒xrand ∈Xf,
for any sample distribution that maintains a nonzero probability
over the entire omniscient set.
For simplicity, this statement is limited to holonomic planning
but it can be extended to speciﬁc constraints with appropriate
assumptions.
Proof. The proof of Lemma 5 from the supplementary online
material appears in Appendix A-B.
This result provides an upper limit on the probability of
RRT* improving a solution at any iteration (Theorem 6).
Theorem 6 (An upper bound on the probability of improving
a solution to a holonomic planning problem given knowledge
of the omniscient set). The probability that an iteration of
RRT* improves the current solution to a holonomic problem,
ci, is bounded by the probability of sampling the omniscient
set, Xf,
∀i ≥κ, P (ci+1 < ci) ≤P (xrand ∈Xf) ,
for any iteration, i, after a sufﬁcient vertex density is achieved
in the initial κ iterations.
For simplicity, this statement is limited to holonomic planning
but it can be extended to speciﬁc constraints by expanding
Lemma 5.
Proof. Proof of Theorem 6 follows directly from Lemma 5.
Sampling a state in Xf is a necessary but not sufﬁcient
condition to improve the solution after κ iterations; therefore,
the probability of sampling such a state bounds the probability
of improving the solution.
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 4


Knowledge of an omniscient set requires solving the planning
problem; however, these results can be extended to estimates
of the omniscient set deﬁned by solution cost heuristics
(Deﬁnition 7).
Deﬁnition 7 (Informed set). Let bf (x) represent a heuristic
estimate of the solution cost constrained to go through a state,
x ∈X. A heuristic estimate of the omniscient set can then be
deﬁned as
X b
f :=
n
x ∈X
 bf (x) < ci
o
.
Such a set will be referred to as an informed set.
There are an inﬁnite number of potential informed sets for
any planning problem and choosing the ‘best’ set requires
methods to quantify their performance. In binary classiﬁcation,
estimates are evaluated in terms of their precision and recall
(Fig. 3). Analogue terms can be deﬁned in sampling-based
planning to quantify the ability of informed sets to estimate
the omniscient set (Deﬁnitions 8 and 9).
Deﬁnition 8 (Precision). The precision of an informed sam-
pling technique is the probability that random samples drawn
from the informed set could also be drawn from the omniscient
set (e.g., the percentage of states drawn from the informed
set, X b
f, that belong to the omniscient set, Xf). For uniform
sampling of an informed set, this is a ratio of measures,
Precision

X b
f

:=
λ

X b
f ∩Xf

λ

X b
f

.
Any informed set with nonzero sampling probability that is a
subset of the omniscient set will have 100% precision.
Deﬁnition 9 (Recall). The recall of an informed sampling
technique is the probability that random states drawn from the
omniscient set could also be sampled from the informed set
(e.g., the percentage of states that belong to the omniscient
set, Xf, with a nonzero probability of being sampled from the
informed set, X b
f). For uniform sampling of an informed set,
this is a ratio of measures,
Recall

X b
f

:=
λ

X b
f ∩Xf

λ (Xf)
.
Any informed set with nonzero sampling probability that is a
superset of the omniscient set will have 100% recall.
Informed sets with 100% recall (Deﬁnition 10) are important
in almost-surely asymptotically optimal planning as less-than-
perfect recall may exclude the optima to some problems.
Deﬁnition 10 (Admissible informed set). A heuristic is said
to be admissible if it never overestimates the true value of the
function,
∀x ∈X, bf (x) ≤f (x) .
Any informed set deﬁned by such an admissible heuristic will
contain all possibly better solutions and have 100% recall, i.e.,
X b
f ⊇Xf.
This set will be referred to as an admissible estimate of the
omniscient set, or an admissible informed set. If the heuristic
Xf
X b
f
Precision

X b
f

:=
λ

X b
f ∩Xf

λ

X b
f

≡
+
Recall

X b
f

:=
λ

X b
f ∩Xf

λ

Xf

≡
+
Fig. 3. An illustration of the precision and recall of estimating an oblong
omniscient set, Xf, with a rectangular informed set, X b
f. The informed set
is coloured to highlight where it is correct (light grey) incorrect (dark grey)
or missing the omniscient set (white). Precision is the likelihood of correctly
sampling the omniscient set by sampling the informed set. Recall is the
coverage of the omniscient set by the informed set. For uniform distributions,
both these terms are ratios of Lebesgue measures.
is an admissible estimate of the cost function for all possible
problems then the set will be referred to as a universally
admissible informed set.
These deﬁnitions allow the probability of improving a solu-
tion to a holonomic problem to be bounded by the probability
of sampling any admissible informed set (Lemmas 11 and 12
and Theorem 13). The tightness of this bound will depend on
the precision of the chosen estimate.
Lemma 11 (The necessity of adding states in an admissible
informed set). Adding a state from an admissible informed
set, xnew ∈X b
f ⊇Xf, is a necessary condition for RRT* to
improve the current solution, ci,
ci+1 < ci =⇒xnew ∈X b
f ⊇Xf.
Proof. Lemma 11 follows directly from Lemma 4 given that
X b
f ⊇Xf.
Lemma 12 (The necessity of sampling states in an admissible
informed set in holonomic planning). Sampling an admissible
informed set, xrand ∈X b
f ⊇Xf, is a necessary condition for
RRT* to improve the current solution to a holonomic problem,
ci, after an initial κ iterations,
∀i ≥κ, ci+1 < ci =⇒xrand ∈X b
f ⊇Xf,
for any sample distribution that maintains a nonzero probability
over the entire informed set.
For simplicity, this statement is limited to holonomic planning
but it can be extended to speciﬁc constraints by expanding
Lemma 5.
Proof. Lemma 12 follows directly from Lemma 5 given that
X b
f ⊇Xf.
Theorem 13 (An upper bound on the probability of improving
a solution to a holonomic planning problem given knowledge of
an admissible informed set). The probability that an iteration
of RRT* improves the current solution to a holonomic problem,
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 5


ci, is bounded by the probability of sampling an admissible
informed set, X b
f ⊇Xf,
∀i ≥κ, P (ci+1 < ci) ≤P (xrand ∈Xf) ≤P

xrand ∈X b
f

,
for any iteration, i, after an initial κ iterations.
For simplicity, this statement is limited to holonomic planning
but it can be extended to speciﬁc constraints by expanding
Lemma 5.
Proof. Theorem 13 follows directly from Theorem 6 given
that X b
f ⊇Xf.
III. PRIOR WORK ACCELERATING RRT* CONVERGENCE
A review of previous work to improve the convergence
rate of RRT* is presented using the results and terminology of
Section II. All these techniques attempt to increase the real-time
rate of searching the omniscient set by exploiting additional
information. Most can be viewed as versions of sample biasing,
sample rejection, and/or graph pruning (Sections III-A–III-D).
A. Sample Biasing
Increasing the likelihood of sampling an informed set
improves RRT* performance. This sample biasing creates a
nonuniform sample distribution that will increase exploration of
the informed set but invalidates the assumptions used to prove
almost-sure asymptotic optimality. One method to maintain
these formal performance guarantees is to calculate the random
geometric graph (RGG) connection limit from a subset of
samples that are uniformly distributed [16]. This maintains
almost-sure asymptotic optimality but increases the required
number of rewirings.
It is common to bias sampling around the current solution.
This path biasing increases the likelihood of sampling a state
that can improve the current solution but reduces the likelihood
of ﬁnding solutions in other homotopy classes (i.e., it increases
precision by decreasing recall; Fig 4a). The ratio of path biasing
to global search is frequently a user-chosen parameter that must
be tuned for each problem.
Akgun and Stilman [8] use path biasing in their dual-tree
version of RRT*. Once an initial solution is found the algorithm
spends a user-speciﬁed percentage of iterations reﬁning the
current solution. It does this by explicitly sampling near a
randomly selected state on the current path. This increases
the probability of improvement at the expense of decreasing
the exploration of other homotopy classes. Their algorithm
also employs sample rejection in exploring the state space (see
Section III-B).
Nasir et al. [17] combine path biasing with smoothing in
their RRT*-Smart algorithm. Solution paths are simpliﬁed and
then used as biases for further sampling around the solution.
Their path smoothing rapidly improves the current solution but
the path biasing decreases the likelihood of ﬁnding a solution
in a different homotopy class.
Kiesel et al. [18] use a two-stage sampling process in their f-
biasing technique. Samples are generated by randomly selecting
a region of the planning problem and then uniformly sampling
it. The probability of selecting a region is calculated by solving
(a) Path biasing
(c) L2 informed set
(b) Bounding box
X b
f
Xf
Xf
Xf
X b
f
X b
f
Fig. 4.
A illustration of the precision and recall of informed sampling
techniques on the omniscient set depicted in Fig. 1(b). The informed sets
are coloured to highlight where they are correct (light grey), incorrect (dark
grey), or missing the omniscient set (white). Path biasing, (a), generally
has high precision but low recall, especially in the presence of multiple
homotopy classes Global or bounded sampling, (b), generally has full recall
but low precision, especially in large relative planning problems or high state
dimensions. Direct sampling of the L2 informed set, (c), has full recall and
high precision, regardless of the size of the omniscient set and is exactly equal
to the omniscient set in the absence of obstacles and constraints.
a simple discretization of the planning problem with Dijkstra’s
algorithm [1]. The regions along the discrete solution are
given a higher selection probability but all regions maintain
a nonzero probability to compensate for the incompleteness of
the discretization. This technique provides a sampling bias for
the entire RRT* search but once a solution is found it continues
to sample states that cannot provide a better solution. It is stated
that almost-sure asymptotic optimality is maintained but it is not
discussed how to modify the rewiring neighbourhood to do so.
Kim et al. [19] also use a two-stage sampling process in their
Cloud RRT* algorithm. They generate uniform samples from
a series of collision-free, possibly overlapping, spheres deﬁned
by a generalized Voronoi graph [20]. New spheres are added on
solution paths and the probability of selecting them is updated
so that samples from the homotopy class of the solution are
biased around the path while maintaining the probability of
sampling other homotopy classes. Cloud RRT* successfully
ﬁnds better solutions faster than other algorithms but continues
to sample states that cannot improve the solution and its effect
on almost-sure asymptotic optimality is not discussed.
Unlike sample biasing methods, the direct informed sampling
used by Informed RRT* does not consider states that are
known to be unable to improve a solution. It does result in
a nonuniform sample distribution over the problem domain
but it is still almost-surely asymptotically optimal as it has a
uniform distribution in the informed set being searched.
B. Sample Rejection
Ignoring samples outside an informed set improves RRT*
performance. This sample rejection decreases the computational
cost of states that cannot improve a solution but does not
increase the probability of ﬁnding ones that can. If this
probability is low (i.e., if the informed set is small relative to
the sampling domain) then convergence will not be improved
(Fig. 4b). It is shown that this probability decreases factorially
with state dimension (i.e., faster than exponentially) in existing
formulations of the holonomic minimum-path-length problem
(Theorem 14).
Akgun and Stilman [8] use global rejection sampling in addi-
tion to sample biasing in their dual-tree algorithm. As samples
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 6


are drawn from the entire problem domain, performance will
decrease rapidly as the solution improves and/or in large or
high-dimensional planning problems.
Otte and Correll [9] use adaptive rejection sampling in their
parallelized Coupled Forest of Random Engrafting Search
Trees (C-FOREST) algorithm. Samples are generated from
a rectangular subset of the planning domain that bounds the
ellipsoidal L2 informed set and rejected using the L2 heuristic.
This increases sampling precision and improves performance
in large planning problems but its effectiveness still decreases
factorially with state dimension (Theorem 14).
Unlike sample rejection methods, the direct informed sam-
pling used by Informed RRT* maintains high precision and
100% recall regardless of the relative sizes of the informed
set and problem domain. It focuses its search in response to
solution improvements and does not decrease in effectiveness in
large planning domains. It scales more effectively than existing
approaches to high-dimensional planning problems
C. Graph Pruning
Limiting the tree to an informed set improves RRT* perfor-
mance. This graph pruning removes states that can no longer
improve the existing solution and reduces the computational
cost of basic operations (e.g., nearest neighbour searches).
It can also be used reject potential new states given their
connection and any constraints, e.g., (3). After a sufﬁcient
number of iterations, this incremental pruning is equivalent
in holonomic planning to rejection sampling with the same
heuristic (Lemma 12) but with the additional computational
costs of expanding towards the sample.
Karaman et al. [21] use graph pruning to implement an online
version of RRT* that improves solutions during path execution.
They remove vertices whose current cost-to-come plus a heuris-
tic estimate of cost-to-go is higher than the current solution. As
current cost-to-come overestimates a vertex’s optimal cost-to-
come (i.e., it is an inadmissible heuristic), this approach may
erroneously remove vertices that could provide a better solution.
Arslan and Tsiotras [22, 23] combine incremental graph-
pruning and incremental graph search techniques with Rapidly
exploring Random Graphs (RRG) [6] to reject samples in their
RRT# algorithm. This incremental pruning focuses the search
but its performance will also decrease rapidly as the solution
improves or when used on large or high-dimensional planning
problems. Some of the rejection criteria also use the current
cost-to-come of vertices and may reject samples that could
later improve the solution.
Unlike rejecting states with incremental graph pruning, the
direct informed sampling used by Informed RRT* wastes no
computational effort on states that are known to be unable to
improve the solution. Its admissible graph pruning algorithm
to remove unnecessary states also only removes vertices from
the tree if doing so does not negatively affect the search.
D. Other Techniques
Some techniques to improve RRT/RRT* performance do not
ﬁt neatly into the previous categories. Many of these methods
could be further accelerated through direct informed sampling.
Urmson and Simmons [24] uses rejection sampling to create
a “probabilistic implementation of heuristic search concepts”
in their Heuristically Guided RRT (hRRT). At each iteration, a
uniformly distributed sample is probabilistically kept or rejected
as a function of its heuristic value relative to the existing tree.
This iteratively biases RRT expansion towards regions of the
problem domain believed to contain high-quality solutions and
often ﬁnds better solutions than RRT, especially on problems
with continuous cost functions (e.g., path length [24]); however,
it results in nonuniform sample distributions.
Ferguson and Stentz [7] recognize that an existing solution
deﬁnes the set of states that could provide better solutions. Their
Anytime RRTs algorithm attempts to incrementally ﬁnd better
solutions by searching a decreasing series of these ellipses.
This shrinking search ignores some expensive solutions but
does not guarantee better ones will be found.
Alterovitz et al. [25] add path reﬁnement to RRT* in their
Rapidly exploring Roadmap (RRM) algorithm. Once an initial
solution is found, each iteration of RRM either samples a new
state or selects an existing state from the current solution and
reﬁnes it. Path reﬁnement connects the selected state to its
neighbours and results in a graph instead of a tree. The ratio
of reﬁnement to exploration is a user-tuned parameter.
Shan et al. [26] ﬁnd an initial solution with RRT, simplify
and rewire it using their RRT* S algorithm, and then continue
the search with RRT*. This can ﬁnd better solutions faster
than RRT* alone but the resulting search is not focused and
continues to consider states that cannot provide better solutions.
Salzman and Halperin [27] relax performance to asymptotic
near optimality in their Lower Bound Tree RRT (LBT-RRT).
Rewirings are only considered if they are required to main-
tain the desired tolerance to the optimum. This can reduce
computational complexity but does not focus the search.
Devaurs et al. [28] use ideas from stochastic optimization
to explore complex cost functions in their Transition-based
RRT* (T-RRT*) and Anytime Transition-based RRT (AT-RRT)
algorithms. Transition tests accept or reject a potential new
state depending on its cost relative to its parent. These tests
help reduce the integral or mechanical work of the path in a
cost space; however, for problems seeking to minimize path
length are equivalent to graph pruning.
These algorithms, and those designed for more advanced
purposes (e.g., RRTX [29]), can be improved with the direct
informed sampling and admissible graph pruning techniques
illustrated in Informed RRT*.
E. Direct Informed Sampling for Path Length
This paper presents Informed RRT* as a demonstration
of how direct sampling of L2 informed sets increases the
rate at which RRT* improves solutions for problems seek-
ing to minimize path length. Unlike sample biasing, this
approach considers all homotopy classes that could provide
better solutions (i.e., 100% recall) while maintaining uniform
sample distribution over a subplanning problem. Unlike sample
rejection or graph pruning, it is effective regardless of the
relative size of the informed set or the state dimension (i.e.,
high precision). In situations where the heuristic does not
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 7


xstart
xgoal
ci
q
c2
i −c2
min
cmin
Fig. 5. The L2 informed set, X b
f, for a R2 problem seeking to minimize path
length is an ellipse with the initial state, xstart, and the goal state, xgoal, as
focal points. The shape of the ellipse depends on both the initial and goal states,
the theoretical minimum cost between the two, cmin, and the cost of the best
solution found to date, ci. The eccentricity of the ellipse is given by cmin/ci.
provide substantial information (i.e., small planning problems
and/or large informed sets), it performs identically to RRT*.
IV. THE L2 INFORMED SET
A universally admissible heuristic is well deﬁned for prob-
lems seeking to minimize path length in Rn and is commonly
used in sampling-based planners (e.g., [7–9]). The cost of
a solution constrained to pass through any state, x ∈X, is
bounded from below by the L2 norm (i.e., Euclidean distance)
between it, the start, xstart, and the goal, xgoal,
bf (x) = ∥x −xstart∥2 + ∥xgoal −x∥2 .
(4)
The set of states that could provide a better solution than the
current solution cost, ci, can then be referred to as the L2
informed set,
X b
f =

x ∈Xfree
 ∥x −xstart∥2 + ∥xgoal −x∥2 < ci
	
.
This informed set is a universally admissible estimate of the
omniscient set and is exact in the absence of obstacles and
constraints (i.e., it is sharp over all minimum-path-length
problems). The size of this informed set will decrease as
solutions improve.
The L2 informed set is the intersection of the free space,
Xfree, and a n-dimensional hyperellipsoid symmetric about its
transverse axis (i.e., a prolate hyperspheroid),
X b
f = Xfree ∩XPHS,
where
XPHS :=

x ∈Rn  ∥x −xstart∥2 + ∥xgoal −x∥2 < ci
	
.
The prolate hyperspheroid has focal points at xstart and
xgoal, a transverse diameter of ci, and conjugate diameters of
p
c2
i −c2
min, where
cmin := ∥xgoal −xstart∥2 ,
is the theoretical minimum cost (Fig. 5). The Lebesgue measure
of the informed set is
λ

X b
f

≤λ (XPHS) = ci
 c2
i −c2
min
 n−1
2
ζn
2n
,
(5)
where ζn is the Lebesgue measure of a n-dimensional unit
ball,
ζn :=
π
n
2
Γ
  n
2 + 1
,
(6)
and Γ (·) is the gamma function, an extension of factorials to
real numbers [30].
The probability of uniformly sampling this informed set by
sampling any superset (e.g., a bounding box), Xsamp ⊇X b
f,
can be written as a ratio of measures,
P

xrand ∈X b
f
 xrand ∼U (Xsamp)

≤λ (XPHS)
λ (Xsamp)
=
π
n
2 ci
 c2
i −c2
min
 n−1
2
2nΓ
  n
2 + 1

λ (Xsamp), (7)
which can be combined with Theorem 13 to bound the
probability of improving a solution to a holonomic problem,
∀i ≥κ, P (ci+1 < ci | xrand ∼U (Xsamp))
≤
π
n
2 ci
 c2
i −c2
min
 n−1
2
2nΓ
  n
2 + 1

λ (Xsamp).
(8)
This probability becomes arbitrarily small for (i) costs, ci,
near the theoretical limit, cmin, (ii) large sampling domains,
λ (Xsamp), or (iii) high state dimensions, n. While the solution
cost and sampling domain size may vary during the search of
a problem, the state dimension is constant throughout. This
motivates investigating the effect of state dimension on existing
formulations of the holonomic minimum-path-length planning
problem (Theorem 14).
Theorem 14 (The minimum-path-length curse of dimension-
ality). The probability that RRT* improves a solution to
holonomic problems seeking to minimize path length decreases
factorially (i.e., faster than exponentially) as state dimension
increases,
∀i ≥κ, P (ci+1 < ci | xrand ∼U (Xrect)) ≤
π
n
2
2nΓ
  n
2 + 1
,
(9)
when uniformly sampling a (hyper)rectangle bounding the L2
informed set, Xrect ⊃XPHS ⊇X b
f ⊇Xf.
For simplicity, this statement is limited to holonomic planning
but it can be extended to speciﬁc constraints by expanding
Lemma 5.
Proof. Theorem 14 is proven for RRT* but holds for any
algorithm for which an equivalent to Theorem 13 exists.
The smallest possible Xrect that completely contains XPHS
is a (hyper)rectangle with widths corresponding to the diameters
of the prolate hyperspheroid (Fig. 6a). The measure of any
Xrect ⊃XPHS is therefore bounded from below as
λ (Xrect) ≥ci
 c2
i −c2
min
 n−1
2
.
(10)
When substituted into (8) this gives
∀i ≥κ, P (ci+1 < ci | xrand ∼U (Xrect)) ≤
π
n
2
2nΓ
  n
2 + 1
,
proving Theorem 14 for all rectangular sets, Xrect, such that
Xrect ⊃XPHS ⊇X b
f ⊇Xf.
Theorem 14 is an upper bound on the utility of rectangular
rejection sampling in holonomic planning and is illustrated
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 8


XPHS
Xrect
xstart
xgoal
Log. time per sample [s]
10−2
10−4
10−6
State dimension, n
2
4
6
8
10
12
14
16
Reject
Direct
(a)
(b)
(c)
State dimension, n
2
4
6
8
10
12
14
16
Log. rel. measure [%]
102
100
10−2
Fig. 6. An illustration of state dimension on problems seeking to minimize path length. The best case performance of an admissible rectangular sampling, e.g.,
[9], occurs when the rectangle tightly bounds the prolate hyperspheroid deﬁned by the current solution cost, Xrect ⊃XPHS ⊇X b
f, (a). The probability
of sampling this L2 informed set (i.e., its relative measure) decreases factorially (i.e., faster than exponentially) with state dimension, n, (b), meaning that
existing formulations of RRT* do not scale effectively to high state dimensions. Direct informed sampling, Alg. 1, scales more efﬁciently as illustrated by the
average per-sample time versus state dimension, (c). Samples in the unit n-ball for Alg. 2 were generated with Boost 1.58.
by plotting (9) versus state dimension (Fig. 6b). The results
show that while rectangular rejection sampling may be 79%
successful in R2, its success decreases factorially as state
dimension increases and is only 2% in R8 and 4 × 10−4% in
R16. These numbers represent the best-case for rectangular
rejection sampling and actual performance will depend on the
size and orientation of the informed set relative to the sampling
domain. This motivates a need for a direct method to sample
the prolate hyperspheroid regardless of size, orientation, and
state dimension.
A. Direct Sampling
A direct method to generate uniformly distributed samples
in the L2 informed set is adapted from techniques to sample
hyperellipsoids [31].
Let S ∈Rn×n be a symmetric, positive-deﬁnite matrix (the
hyperellipsoid matrix) such that the interior of a hyperellipsoid,
Xellipse, is deﬁned as
Xellipse :=
n
x ∈Rn  (x −xcentre)T S−1 (x −xcentre) < 1
o
,
(11)
where xcentre is the centre point of the hyperellipsoid. Uni-
formly distributed samples in the hyperellipsoid, xellipse ∼
U (Xellipse), can be generated from uniformly distributed
samples in the interior of a unit n-dimensional ball, xball ∼
U (Xball), by
xellipse = Lxball + xcentre,
(12)
where L ∈Rn×n is the lower-triangular Cholesky decomposi-
tion of the hyperellipsoid matrix such that
LLT ≡S
and
Xball := {x ∈Rn | ∥x∥2 < 1} .
For hyperellipsoids with orthogonal axes, there exists a
coordinate frame in which the hyperellipsoid matrix is diagonal,
S′ := diag
 r2
1, r2
2, . . . , r2
n

,
where rj is the radius of j-th axis of the hyperellipsoid
and diag (·) constructs a diagonal matrix. A rotation from
this hyperellipsoid-aligned frame to the world frame, Cwe ∈
SO (n), can be used to write (11) in terms of S′ as
Xellipse :=
n
x ∈Rn 
(x −xcentre)T CweS′−1CT
we (x −xcentre) < 1
o
,
and (12) as
xellipse = CweL′xball + xcentre,
(13)
given the orthogonality of rotation matrices, C−1
we ≡CT
we, and
that L′L′T ≡S′.
The rotation between frames can be solved directly as a
general Wahba problem [32] even when underspeciﬁed [33].
Generally, the rotation matrix from one set of axes, {aj}, to
another set of axes, {bj}, is given by
Cba = UΛVT ,
(14)
where Λ ∈Rn×n is
Λ := diag (1, . . . , 1, det (U) det (V)) ,
and det (·) is the matrix determinant. The terms U ∈Rn×n
and V ∈Rn×n are unitary matrices such that UΣVT ≡M
via singular value decomposition and M ∈Rn×n is given by
the outer product of the j ≤n corresponding axes,
M := [a1, a2, . . . , aj] [b1, b2, . . . bj]T .
(15)
In problems seeking to minimize path length, the hyperel-
lipsoid is a prolate hyperspheroid described by
xcentre := xstart + xgoal
2
,
(16)
S′ := diag
c2
i
4 , c2
i −c2
min
4
, . . . , c2
i −c2
min
4

,
and therefore,
L′ = diag
 
ci
2 ,
p
c2
i −c2
min
2
, . . . ,
p
c2
i −c2
min
2
!
. (17)
Its local coordinate system is underspeciﬁed in the conjugate
directions due to symmetry, making (15) just
M = a11T
1 ,
(18)
where 11 the ﬁrst column of the identity matrix and the
transverse axis in the world frame is
a1 = (xgoal −xstart) / ∥xgoal −xstart∥2 .
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 9


Alg. 1: Sample (xstart ∈X, xgoal ∈X, ci ∈R≥0)
1 repeat
2
if λ (XPHS) < λ (X) then
3
xrand ←SamplePHS (xstart, xgoal, ci);
4
else
5
xrand ←SampleProblem (X);
6 until xrand ∈Xfree ∩XPHS;
7 return xrand;
Alg. 2: SamplePHS (xstart ∈X, xgoal ∈X, ci ∈R≥0)
1 cmin ←∥xgoal −xstart∥2;
2 xcentre ←(xstart + xgoal) /2;
3 a1 ←(xgoal −xstart) /cmin;
4 {U, V} ←SVD
 a11T
1

;
5 Λ ←diag (1, . . . , 1, det (U) det (V));
6 Cwe ←UΛVT ;
7 r1 ←ci/2;
8 {rj}j=2,...,n ←
p
c2
i −c2
min

/2;
9 L ←diag (r1, r2, . . . , rn);
10 xball ←SampleUnitBall (n);
11 xrand ←CweLxball + xcentre;
12 return xrand;
Samples distributed uniformly in the L2 informed set,
X b
f = XPHS ∩Xfree, can therefore be generated by using
(13) to transform samples drawn uniformly from a unit n-ball.
These samples are mapped to the prolate hyperspheroid through
scaling, (17), rotation, (14) and (18), and translation, (16).
Sun and Farooq [31] investigate various methods to generate
samples in hyperellipsoids and provide the following lemma
regarding the uniform sample density of this technique.
Lemma 15 (The uniform distribution of samples transformed
into a hyperellipsoid from a unit n-ball. Originally Lemma 1
in [31]). If the random points distributed in a hyperellipsoid
are generated from the random points uniformly distributed
in a hypersphere through a linear invertible nonorthogonal
transformation, then the random points distributed in the
hyperellipsoid are also uniformly distributed.
Proof. For brevity, [31] only presents anecdotal proofs of
Lemma 15. The full proof from the supplementary online
material appears in Appendix B.
1) Algorithm: The L2 informed set is an arbitrary intersec-
tion of the prolate hyperspheroid and the problem domain. It
can be sampled efﬁciently by considering the relative measure
of the two sets and sampling the smaller set until a sample
belonging to both sets is found. These procedures are presented
algorithmically in Algs. 1 and 2 and are publicly available in
OMPL. Note that for most problems Alg. 2, Lines 1–6 are
constant and only need to be calculated once.
The function SVD (·) denotes the singular value decomposi-
tion of a matrix and SampleUnitBall (n) returns uniformly
distributed samples from the interior of an n-dimensional unit
ball. The measure of the prolate hyperspheroid, λ (XPHS), is
given by (5) and SampleProblem returns samples uniformly
distributed over the entire planning domain. Implementations
of SVD and SampleUnitBall can be found in common
C++ libraries.
2) Practical
Performance:
Direct
informed
sampling
(Alg. 1) is compared to the best-case performance of rectangular
rejection sampling. The average computational time required to
ﬁnd a sample in the L2 informed set is calculated by generating
106 samples at each dimension (Fig. 6c). The results show
that while rejection sampling may outperform direct informed
sampling in low state dimensions (e.g., R2: 7.3 × 10−8 vs.
3.5×10−7 seconds), it becomes orders of magnitude slower as
state dimension increases (e.g., R16: 4.0×10−2 vs. 7.2×10−7
seconds). These per-sample times are small but signiﬁcant.
Generating 105 samples in R16 requires less than a second
with direct informed sampling (7.2 × 10−2 seconds) but over
an hour with rectangular rejection sampling (3953 seconds).
This experiment represents optimistic results for both
constant (e.g., the problem domain) and adaptive (e.g., [9])
rectangular rejection sampling. Constant sampling domains
rarely provide tight bounds on the informed set and will
generally have higher rejection rates than the experiment.
Adaptive sampling domains may tightly bound the informed
set but must account for its alignment relative to the state space.
This requires either a larger rectangular sampling domain or
a rotation between frames that increases the rejection rate or
computational cost compared to the experiment, respectively.
B. Extension to Multiple Goals
Many planning problems seek the minimum-length path that
connects a start to any state in a goal region, Xgoal. In these
situations the omniscient set is all states that could provide a
better solution to any goal. The multigoal L2 informed set is
X b
f :=

x ∈Xfree
 ∥x −xstart∥2 + ∥xgoal,j −x∥2 < ci
for any xgoal,j ∈Xgoal
	
.
For a countable goal region, Xgoal := {xgoal,j}z
j=1, this set
is the union of the individual informed sets of each goal,
X b
f =
z[
j=1
X b
f,j,
where z is the number of goals and
X b
f,j :=

x ∈Xfree
 ∥x −xstart∥2 + ∥xgoal,j −x∥2 < ci
	
,
is the L2 informed set of an individual (xstart, xgoal,j) pair. If
the individual informed sets do not intersect, then a uniform
sample distribution can be generated by randomly selecting an
individual subset, j, in proportion to its relative measure,
p (1 ≤j ≤z) :=
λ

X b
f,j

Pz
k=1 λ

X b
f,k
,
and then generating a uniformly distributed sample inside the
selected subset, X b
f,j.
If individual sets do intersect, then this approach will
oversample states that belong to multiple sets (Fig. 7a). In
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 10


Alg. 3: Sample(xstart ∈X, Xgoal ⊂X, ci ∈R≥0)
1 repeat
2
if 1
z
Pz
j=1 λ (XPHS,j) < λ (X) then
3
xgoal,j ←RandomGoal (xstart, Xgoal, ci);
4
xrand ←SamplePHS (xstart, xgoal,j, ci);
5
else
6
xrand ←SampleProblem (X);
7 until xrand ∈Xfree ∩
Sz
j=1 XPHS,j

and
KeepSample (xrand, xstart, Xgoal, ci);
8 return xrand;
Alg. 4: RandomGoal (xstart ∈X, Xgoal ⊂X, ci ∈R≥0)
1 a ←0;
2 forall xgoal,k ∈Xgoal do
3
a ←a + λ (XPHS,k);
4 p ←U [0, 1];
5 j ←0;
6 repeat
7
j ←j + 1;
8
p ←p −λ (XPHS,j) /a;
9 until p ≤0;
10 return xgoal,j;
these situations, uniform sample density can be maintained
by probabilistically rejecting samples in proportion to their
membership in individual sets. This creates a uniform sample
distribution for multigoal L2 informed sets deﬁned by arbitrarily
overlapping individual informed sets (Fig. 7b).
1) Algorithm: The algorithm is described in Algs. 3–5
as modiﬁcations to the sampling technique for a single-
goal L2 informed set, with changes highlighted in red (cf.
Alg. 1). The measure of individual informed sets, λ (XPHS,j),
is calculated from (5) using the appropriate goal, xgoal,j.
This same technique can also be applied to problems with
a countable start region.
V. INFORMED RRT*
Informed RRT* is an extension of RRT* that demonstrates
how informed sets can be used to improve anytime almost-
surely asymptotically optimal planning. It performs the same as
RRT* until a solution is found after which the search is focused
to the informed set through direct informed sampling and
admissible graph pruning (Fig. 8). This increases the likelihood
of sampling states that can improve the solution and increases
the convergence rate towards the optimum regardless of the
relative size of the informed set (e.g., near-minimum solutions
or large problem domains) or the state dimension.
Informed RRT* uses direct informed sampling (Alg. 3),
admissible graph pruning (Section V-B), and an updated
calculation of the rewiring neighbourhood (Section V-C) to
focus the search. The complete algorithm is presented in Algs. 6
and 7 as modiﬁcations to RRT*, with changes highlighted in
red. It can also be integrated into other sampling-based planners,
such as RRTX [29] and Batch Informed Trees (BIT*) [34–36].
Alg. 5: KeepSample (xrand ∈X, xstart ∈X,
Xgoal ⊂X, ci ∈R≥0)
1 a ←0;
2 forall xgoal,k ∈Xgoal do
3
if ∥xrand −xstart∥2 + ∥xgoal,k −xrand∥2 < ci then
4
a ←a + 1;
5 p ←U [0, 1];
6 return p ≤1/a;
xstart
xgoal,2
xgoal,1
(a)
(b)
xgoal,3
Fig. 7.
An illustration of the multigoal L2 informed set for a problem
seeking to minimize path length from a start at [0, 0]T , to any of three goals at
[−0.75, 0]T , [0.25, 0]T , and [0.7, 0.7]T , and a current solution cost of ci =
1.05. Each ellipse illustrates the L2 informed set for a start-goal pair. Combin-
ing the uniform distributions of these individuals (light grey) would result in a
nonuniform distribution (dark grey), (a). By probabilistically rejecting samples
in proportion to their individual membership, Alg. 3 uniformly samples complex
sets of arbitrary intersections, as illustrated with 2500 random samples, (b).
At each iteration, Informed RRT* calculates the current best
solution (Alg. 6, Line 4) from the vertices in the goal region
(Alg. 6, Lines 2, 9–10). This deﬁnes a shrinking L2 informed
set that is used to both focus sampling (Alg. 6, Line 5; Alg. 3)
and prune the graph (Alg. 6, Line 27; Alg. 7). This process
continues for as long as time allows or until a suitable solution
is found.
Informed RRT* retains the probabilistic completeness and
almost-sure asymptotically optimality of RRT*. It is proba-
bilistically complete since it does not modify the search for
an initial solution. It is almost-surely asymptotically optimal
as it maintains a uniform sample distribution over a subset
of the planning problem in which it uses a local rewiring
neighbourhood that satisﬁes the bounds presented in [6].
A. Notation
The tree, T := (V, E), is deﬁned by a set of vertices, V ⊂
Xfree, and edges, E = {(v, w)}, for some v, w ∈V . The
function gT (v) represents the cost to reach a vertex, v ∈V ,
from the start given the current tree (the cost-to-come). The
function c (v, w) represents the cost of a path connecting the
states v, w ∈Xfree, and corresponds to the edge cost between
those two states if they are connected as vertices in the tree.
The notation X
+
←−{x} and X
−
←−{x} is used to compactly
represent the compounding set operations X ←X ∪{x} and
X ←X \ {x}, respectively. As is customary, the minimum of
an empty set is taken to be inﬁnity and a prolate hyperspheroid
deﬁned by an inﬁnite transverse diameter is taken to have
inﬁnite measure.
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 11


(a)
(b)
(c)
(d)
Fig. 8. An example of how Informed RRT* uses the current solution to focus search to the L2 informed set. After an unfocused search for an initial solution,
(a), Informed RRT* prunes the graph of unnecessary states and redeﬁnes the search domain to the current L2 informed set, (b). Samples are then generated
directly from this informed set, avoiding those that are known to be unable to improve the current solution. This reduced search space increases the likelihood
of ﬁnding an improved solution, which in turn further reduces the search space, (c). This results in an algorithm that focuses the search to the subproblem
given by the current solution, shown enlarged in (d), even as the subproblem decreases with further improvement.
Alg. 6: Informed RRT*(xstart ∈Xfree, Xgoal ⊂X)
1 V ←{xstart} ; E ←∅; T = (V, E);
2 Vsol’n ←∅;
3 for i = 1 . . . q do
4
ci ←minvgoal∈Vsol’n {gT (vgoal)};
5
xrand ←Sample (xstart, Xgoal, ci);
6
vnearest ←Nearest (V, xrand);
7
xnew ←Steer (vnearest, xrand);
8
if IsFree (vnearest, xnew) then
9
if xnew ∈Xgoal then
10
Vsol’n
+
←−{xnew};
11
V
+
←−{xnew};
12
Vnear ←Near (V, xnew, rrewire);
13
vmin ←vnearest;
14
forall vnear ∈Vnear do
15
cnew ←gT (vnear) + c (vnear, xnew);
16
if cnew < gT (vmin) + c (vmin, xnew) then
17
if IsFree (vnear, xnew) then
18
vmin ←vnear;
19
E
+
←−{(vmin, xnew)};
20
forall vnear ∈Vnear do
21
cnear ←gT (xnew) + c (xnew, vnear);
22
if cnear < gT (vnear) then
23
if IsFree (xnew, vnear) then
24
vparent ←Parent (vnear);
25
E
−
←−{(vparent, vnear)};
26
E
+
←−{(xnew, vnear)};
27
Prune (V, E, ci);
28 return T ;
B. Graph Pruning (Alg. 7)
Graph pruning simpliﬁes a tree by removing unnecessary
vertices. Vertices are often removed if their heuristic values
are larger than the current solution (i.e., they do not belong to
informed set). While this identiﬁes vertices that cannot provide
Alg. 7: Prune (V ⊆X, E ⊆V × V, ci ∈R≥0)
1 repeat
2
Vprune ←
n
v ∈V
 bf (v) > ci, and ∀w ∈V, (v, w) ̸∈E
o
;
3
E
−
←−{(u, v) ∈E | v ∈Vprune};
4
V
−
←−Vprune;
5 until Vprune = ∅;
a better solution, it is not a sufﬁcient condition to remove
them without negatively affecting the search. Their descendants
may still be capable of providing better solutions (i.e., they
may belong to the informed set; Fig. 9) in which case their
removal would negatively affect performance by decreasing
vertex density in the search domain (i.e., the informed set;
Fig. 10b).
An admissible pruning method that does not remove vertices
from the informed set is presented in Alg. 7. It iteratively
removes leaves of the tree that cannot provide a better solution
until no such leaves exist. This only removes vertices if they
and all their descendants cannot belong to a better solution (i.e.,
it only removes vertices from outside the informed set; Fig. 9).
This retains all possibly beneﬁcial vertices regardless of their
current connections and does not alter the vertex distribution
in areas being searched (Fig. 10c).
C. The Rewiring Neighbourhood
RRT* almost-surely converges asymptotically to the opti-
mum by incrementally rewiring the tree around new states.
In the r-disc variant this is the set of states within a radius,
rrewire, of the new state,
rrewire := min {η, rRRT∗} ,
(19)
where η is the maximum allowable edge length of the tree and
rRRT∗is a function of the problem measure and the number
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 12


xstart
xgoal
v
u
X b
f
Fig. 9. An illustration of Alg. 7 that shows the retained (black) and pruned
(grey) vertices given the L2 informed set (dashed grey line) deﬁned by the
current solution. Vertices are pruned if and only if they cannot improve
the current solution (i.e., they are not members of the L2 informed set)
and neither can their descendants. This pruning condition avoids removing
promising vertices (e.g., v) simply because they are currently descendants of
vertices outside the subset (e.g., u) and maintains the vertex distribution of
the L2 informed set (Fig. 10).
of vertices in the tree [6]. Speciﬁcally,
rRRT∗> r∗
RRT∗,
r∗
RRT∗:=

2

1 + 1
n
 λ (X)
ζn
 log (|V |)
|V |
 1
n
,
(20)
where λ (·) is the Lebesgue measure of a set (e.g., the volume),
ζn is the Lebesgue measure of an n-dimensional unit ball, i.e.,
(6), and |·| is the cardinality of a set.
The rewiring neighbourhood in the k-nearest variant is the
kRRT∗-closest states to the new state, where
kRRT∗> k∗
RRT∗,
k∗
RRT∗:= e

1 + 1
n

log (|V |) .
(21)
Informed RRT* searches a subset of the original planning
problem. The rewiring requirements to maintain almost-sure
asymptotic optimality in this shrinking domain will be a
function of the number of vertices in the informed set,
V ∩X b
f
, and its measure, λ

X b
f

. The L2 informed set
is not known in closed form (it is an intersection of a
prolate hyperspheroid and free space) but its measure can be
bounded from above by the minimum measure of the prolate
hyperspheroid and the problem domain,
λ

X b
f

≤min {λ (X) , λ (XPHS)} .
This updates (20) and (21) to
r∗
RRT∗≤

2

1 + 1
n
 min {λ (X) , λ (XPHS)}
ζn



log
V ∩X b
f


V ∩X b
f





1
n
(22)
and
k∗
RRT∗= e

1 + 1
n

log
V ∩X b
f


,
(23)
where λ (XPHS) is a function of the current solution, i.e., (5).
These rewiring neighbourhoods will be smaller than (20)
and (21) when they can contain fewer vertices (i.e., only those
in the informed set) and/or a smaller problem measure (i.e., the
measure of the informed set). Smaller rewiring neighbourhoods
(a)
(b)
(c)
Fig. 10. An illustration of pruning a graph found by RRT*, (a), with both
inadmissible, (b), and admissible, (c), methods. By removing all vertices that
cannot belong to a better solution, the inadmissible method may greedily
remove descendent vertices that will later provide a better solution once the
graph is improved. By only removing vertices that cannot improve a solution
if neither can their descendants, the admissible method (Alg. 7) maintains a
uniform sample density in the entire informed set.
reduce the computational cost of rewiring at each iteration and
improves the real-time performance of Informed RRT* while
maintaining almost-sure asymptotic optimality.
VI. RATES OF CONVERGENCE
Almost-sure asymptotic optimality provides no insight into
the rate at which solutions are improved. Previous work has
found probabilistic rates for PRM* [37] and Fast Marching
Tree (FMT*) [16] and estimated the expected length of RRT*
solutions as a function of computational time [37].
Performance can be quantiﬁed analytically by evaluating the
rate at which the sequence of solution costs converges to the
optimum. This rate can be classiﬁed as sublinear, linear, or
superlinear (Deﬁnition 16).
Deﬁnition 16 (Rate of convergence). A sequence of numbers,
(ai)∞
i=1, that monotonically and asymptotically approaches a
limit, a∞, has a rate of convergence given by
µ := lim
i→∞
|ai+1 −a∞|
|ai −a∞| .
The sequence is said to converge linearly if the rate is in the
range 0 < µ < 1, superlinearly (i.e., faster than linear) when
µ = 0, and sublinearly (i.e., slower than linear) when µ = 1.
The expected convergence rate of an algorithm depends on
its tuning and the planning problem. General rates can be
calculated for holonomic minimum-path-length problems for
RRT* with and without sample rejection and Informed RRT*
(Theorems 18–20) by ﬁrst calculating sharp bounds on the
expected next-iteration cost (Lemma 17).
Lemma
17 (Expected next-iteration cost of minimum–
path-length planning). The expected value of the next solution
to a minimum-path-length problem, E [ci+1], is bounded by
pf
nc2
i + c2
min
(n + 1) ci
+ (1 −pf) ci ≤E [ci+1] ≤ci,
(24)
where ci is the current solution cost, cmin is the theoretical
minimum solution cost, n is the state dimension of the planning
problem, and pf = P (xnew ∈Xf) is the probability of adding
a state that is a member of the omniscient set (i.e., that can
belong to a better solution). While not explicitly shown, the
subset, Xf, and the probability of improving the solution, pf,
are generally functions of the current solution cost.
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 13


This lower bound is sharp over the set of all possible
minimum-path-length planning problems and algorithm con-
ﬁgurations and is exact for versions of RRT* with an inﬁnite
rewiring radius (i.e., η = ∞, and rRRT∗= ∞) searching an
obstacle-free environment without constraints.
Proof. The proof of Lemma 17 from the supplementary online
material appears in Appendix C.
This result allows sharp bounds on the convergence rates
of RRT* (with and without rejection sampling) and Informed
RRT* to be calculated for any conﬁguration or holonomic
minimum-path-length planning problem. These bounds will be
exact in problems without obstacles and constraints and with an
inﬁnite rewiring neighbourhood (i.e., η = ∞, and rRRT∗= ∞)
and show that RRT* always has sublinear convergence to the
optimum (Theorem 18).
Theorem 18 (Sublinear convergence of RRT* in holonomic
minimum-path-length planning). RRT* converges sublinearly
towards the optimum of holonomic minimum-path-length
planning problems,
E [µRRT∗] = 1.
(25)
For simplicity, this statement is limited to holonomic planning
but it can be extended to speciﬁc constraints by expanding
Lemma 5.
Proof. The proof of Theorem 18 follows directly from
Lemma 17 when pf is given by (7) and appears from the
supplementary online material in Appendix D-A.
Rectangular rejection sampling improves the convergence
rate of RRT*. This improvement is maximized by sampling a
rectangle that tightly bounds the informed set (Fig. 6a). The
resulting adaptive rectangular rejection sampling (e.g., [9])
allows RRT* to converge linearly in the absence of obstacles
and constraints and with an inﬁnite rewiring neighbourhood
(Theorem 19).
Theorem 19 (Linear convergence of RRT* with adaptive rect-
angular rejection sampling in holonomic minimum-path-length
planning). RRT* with adaptive rectangular rejection sampling
converges at best linearly towards the optimum of holonomic
minimum-path-length planning problems but factorially ap-
proaches sublinear convergence with increasing state dimen-
sion,
1 −
π
n
2
(n + 1) 2n−1Γ
  n
2 + 1
 ≤E [µRect] ≤1.
(26)
For simplicity, this statement is limited to holonomic planning
but it can be extended to speciﬁc constraints by expanding
Lemma 5.
Proof. The proof of Theorem 19 follows directly from
Lemma 17 when pf is calculated by substituting (10) in
(7) and appears from the supplementary online material in
Appendix D-B.
This convergence rate diminishes factorially (i.e., quickly)
as state dimension increases due to the minimum-path-length
curse of dimensionality. Informed RRT* avoids this limitation
Better
10−5
State dimension, n
2
4
6
8
10
12
14
16
100
RRT* w/ rejection sampling
Informed RRT*
Log. linearity, log(E

1 −µ∗
)
Fig. 11. An illustration of the lower-bounds on linearity, E [1 −µ∗], of RRT*
with rejection sampling and Informed RRT* (Corollary 21). As predicted by
Theorems 19 and 20, the convergence rates bounds diverge as state dimensions
increase, with rejection sampling factorially approaching sublinear convergence.
with direct informed sampling. It also converges linearly in
the absence of obstacles and constraints and with an inﬁnite
rewiring neighbourhood but has a weaker dependence on state
dimension (Theorem 20).
Theorem 20 (Linear convergence of Informed RRT* in
holonomic minimum-path-length planning). Informed RRT*
converges at best linearly towards the optimum of holonomic
minimum-path-length planning problems,
n −1
n + 1 ≤E [µInf] ≤1,
(27)
where the lower-bound occurs exactly with an inﬁnite rewiring
neighbourhood in the absence of obstacles and constraints.
For simplicity, this statement is limited to holonomic planning
but it can be extended to speciﬁc constraints by expanding
Lemma 5.
Proof. The proof of Theorem 20 follows directly from
Lemma 17 when pf = 1 and appears from the supplementary
online material in Appendix D-C.
Theorems 18–20 result in the following corollary regarding
the relative convergence rates of the algorithms.
Corollary 21 (The faster convergence of Informed RRT*
in holonomic minimum-path-length planning). The best-case
convergence rate of Informed RRT*, µ∗
Inf, is always better than
that of RRT*, with or without rejection sampling in holonomic
minimum-path-length planning,
∀n ≥2, n −1
n + 1 = E [µ∗
Inf] ≤E [µ∗
Rect] ≤E [µ∗
RRT∗] = 1.
For simplicity, this statement is limited to holonomic planning
but it can be extended to speciﬁc constraints by expanding
Lemma 5.
Proof. The proof follows immediately from the lower bounds
in (25), (26), and (27). It is illustrated in Fig. 11.
A. Experimental Validation and Extension
Convergence rates are investigated experimentally for inﬁnite,
constant ﬁnite, and decreasing ﬁnite rewiring radii. To isolate
the effects of the rewiring parameters, Informed RRT* was run
on obstacle- and constraint-free problems in R2, R4, and R8
for 104 trials of each conﬁguration. Each trial started from the
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 14


Log. sol’n error
Log. sol’n error
Log. sol’n error
Mean
Theoretical prediction
Individual trial
Best ﬁt
10−15
10−10
10−5
55
60
65
70
75
80
90
180
190
200
210
220
230
240
250
Iteration
Iteration
140
160 180
200
220 240
260
280 300
85
Fit error [%]
50
100
Log. sol’n error
40
80
240
200
400
600
800
1000
1200
Iteration
1000
2000
3000
4000
120
200
160
Log. sol’n error
Log. sol’n error
Log. sol’n error
1000
2000
3000
4000
1000
2000
3000
4000
1000
2000
3000
4000
100
10−15
10−10
10−5
100
10−15
10−10
10−5
Fit error [%]
Fit error [%]
(a) R2: η = ∞, rRRT∗= ∞
(b) R4: η = ∞, rRRT∗= ∞
(c) R8: η = ∞, rRRT∗= ∞
Iteration
Iteration
0
50
100
0
50
100
0
100
10−15
10−10
10−5
100
10−15
10−10
10−5
100
10−15
10−10
10−5
100
10−15
10−10
10−5
100
10−15
10−10
10−5
100
10−15
10−10
10−5
Log. sol’n error
Log. sol’n error
Iteration
(d) R2: η = 0.4, rRRT∗= ∞
(e) R4: η = 0.4, rRRT∗= ∞
(f) R8: η = 0.4, rRRT∗= ∞
Iteration
Iteration
(g) R2: η = ∞, rRRT∗= 1.1r∗
RRT∗
(h) R4: η = ∞, rRRT∗= 1.1r∗
RRT∗
Iteration
(i) R8: η = ∞, rRRT∗= 1.1r∗
RRT∗
Better
Better
Better
100
Fig. 12. Experimental validation and extension of Lemma 17 and Theorem 20 in R2, R4 and R8. Informed RRT* was run from a common initial solution 104
times in R2, R4 and R8 with different pseudo-random seeds. The error relative to the known optimum, log (ci −c∗), was plotted for each instance at each
iteration (cyan lines) along with the mean error (blue circles), a line of best ﬁt (blue dashed line), and the lower-bound error predicted by Lemma 17 (black
line). The difference between the predicted lower bound and the mean errors (red lines),
 cmean,i −ctheory,i

/ (cmean,i −c∗)
, with inﬁnite rewiring
neighbourhoods, (a)–(c), conﬁrms experimentally that convergence is linear (Theorem 20). The mean error for a ﬁnite but constant rewiring neighbourhood,
(d)–(f), shows experimentally that convergence is slower but possibly still linear. The mean error for a ﬁnite and decreasing rewiring neighbourhood, (g)–(i),
shows experimentally that the is slower and sublinear. The results of (d)–(i) motivate further research on the effects of the RRT* rewiring neighbourhood.
same initial solution but used different pseudo-random seeds to
search for improvements. The logarithmic error relative to the
known optimum, log (ci −c∗), and the resulting mean were
calculated at each iteration of each trial and used to validate
Theorem 20 and illustrate the effects of rewiring parameters
on the convergence rate.
The experimental results for an inﬁnite rewiring neighbour-
hood (i.e., η = ∞and rRRT∗= ∞) show excellent agreement
with the theoretical predictions in Theorem 20 (Figs. 12a–c).
The mean solution cost converges linearly towards the optimum
and closely matches the lower-bound predicted by Lemma 17.
The experimental results for a constant ﬁnite rewiring
neighbourhood (i.e., η = 0.4 and rRRT∗= ∞) show that
the convergence rate is lower than predicted by Theorem 20
(Figs. 12d–f). The convergence rate appears to be initially
nonlinear but then become linear. It is hypothesized that this
is related to the density of samples relative to the maximum
edge length as reﬂected by κ in Theorem 6.
The experimental results for a decreasing ﬁnite rewiring
neighbourhood (i.e., η = ∞and rRRT∗= 1.1r∗
RRT∗) show that
the convergence rate appears to be sublinear (Figs. 12g–i). It is
hypothesized that this is a result of the rewiring neighbourhood
shrinking ‘too’ fast relative to the sample density.
These experiments suggest that further research is necessary
to study the tradeoff between per-iteration cost and the
number of iterations needed to ﬁnd a solution. While a shrink-
ing rewiring neighbourhood limits the number of rewirings,
the apparent resulting sublinear convergence would require
signiﬁcantly more iterations to ﬁnd high-quality solutions.
Alternatively, while linear convergence needs fewer iterations
to ﬁnd equivalent solutions, the required constant radius would
allow the number of rewirings to increase indeﬁnitely.
VII. EXPERIMENTS
Informed RRT* was evaluated on simulated problems in
R2, R4, and R8 (Sections VII-A and VII-B) and for HERB
(Section VII-C) using OMPL2. It was compared to the original
RRT* and versions that focus the search with graph pruning
(e.g., Alg. 7), heuristic rejection on xnew, heuristic rejection
on xrand, and all three techniques combined.
All planners used the same tuning parameters and the ordered
rewiring technique presented in [38]. Planners used a goal-
sampling bias of 5% and an RRT* radius of rRRT∗= 2r∗
RRT∗.
The maximum edge length was selected experimentally to
reduce the time required to ﬁnd an initial solution on a training
problem, with values of η = 0.3, 0.5, 0.9, and 1.3 used in R2,
2The experiments were run on a laptop with 16 GB of RAM and an Intel
i7-4810MQ processor. The abstract experiments were run in Ubuntu 12.04
(64-bit) with Boost 1.58, while the HERB experiments were run in Ubuntu
14.04 (64-bit).
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 15


R4, R8, and on HERB (R14), respectively. Available planning
time was limited for each state dimension to 3, 30, 150, and
600 seconds, respectively. Planners with heuristics used the L2
norm as estimates of cost-to-come and cost-to-go while those
with graph pruning delayed its application until solution cost
changed by more than 5%.
These experiments were designed to investigate admissi-
ble methods to focus search. More advanced extensions of
RRT* were not considered as they commonly include some
combination of the investigated techniques.
A. Toy Problems
Two separate experiments were run in R2, R4, and R8 on
randomized variants of the toy problem depicted in Fig. 13a
to investigate the effects of obstacles on convergence.
The problem consists of a (hyper)cube of width l with
a single start and goal located at [−0.5, 0, . . . , 0]T
and
[0.5, 0, . . . , 0]T , respectively. A single (hyper)cube obstacle
of width w ∼U [0.25, 0.5] sits between the start and goal in
the centre of the problem domain.
The ﬁrst experiment investigates ﬁnding near-optimal so-
lutions in the presence of obstacles. The time required for
each planner to ﬁnd a solution within various fractions of
the known optimum, c∗, was recorded over 100 trials with
different pseudo-random seeds for maps of width l = 2. The
percentage of trials that found a solution within the target
tolerance of the optimum and the median time necessary to do
so are presented for each planner in Figs. 14a–c. Trials that
did not ﬁnd a suitable solution were treated as having inﬁnite
time for the purpose of calculating the median. The results
show that Informed RRT* performs equivalently to rejection
sampling algorithms in low state dimensions but outperforms
all existing techniques in higher dimensions.
The second experiment investigates ﬁnding near-optimal
solutions in large planning problems. The time required for each
planner to ﬁnd a near-optimal solution was recorded over 100
trials with different pseudo-random seeds for maps of increasing
width, l. Planners sought a solution better than 1.01c∗, 1.05c∗,
and 1.15c∗in R2, R4, and R8, respectively. The percentage
of trials that found a sufﬁciently near-optimal solution and the
median time necessary to do so are presented for each planner
in Figs. 14d–f. Trials that did not ﬁnd a suitable solution were
treated as having inﬁnite time for the purpose of calculating
the median. The results show that Informed RRT* outperforms
all existing techniques in large-domain planning problems and
that the difference increases in higher state dimensions.
These experiments show that increasing problem size and
state dimension decreases the ability of nondirect sampling
methods to ﬁnd near-optimal solutions, as predicted by (8).
Informed RRT* limits these effects and outperforms existing
techniques by efﬁciently focusing its search to the L2 informed
set using direct informed sampling.
B. Worlds with Many Homotopy Classes
The algorithms were tested on more complicated problems
with many homotopy classes in R2, R4, and R8. The worlds
consisted of a (hyper)cube of width l = 4 with the start and goal
xstart
xgoal
l
l
w
(a)
(b)
w
1
l
xstart
xgoal
w
2w
1
Fig. 13. Illustrations of the planning problems used for Sections VII-A and
VII-B to study performance relative to a known optimum, the effect of map
width, l, and performance in problems with many homotopy classes. The
width of the obstacle in (a) is a random variable uniformly distributed over
the range [0.25, 0.5]. The regularly spaced obstacles in (b) are chosen in to
scale efﬁciently to high dimensions and their width is such that the start and
goal states are 5 ‘columns’ apart.
located at [−0.5, 0, . . . , 0]T and [0.5, 0, . . . , 0]T , respectively.
The problem domain was ﬁlled with a regular pattern of axis-
aligned (hyper)cube obstacles with a width such that the start
and goal were 5 ‘columns’ apart (Fig. 13b).
The planners were tested with 100 different pseudo-random
seeds on each world and state dimension. The solution cost of
each planner was recorded every 1 millisecond by a separate
thread and the median was calculated from the 100 trials by
interpolating each trial at a period of 1 millisecond. The absence
of a solution was considered an inﬁnite cost for the purpose
of calculating the median.
The results are presented in Figs. 14g–i, where the percent of
trials solved and the median solution cost are plotted versus run
time. They demonstrate how Informed RRT* has better real-
time convergence towards the optimum than existing techniques,
especially in higher state dimensions.
C. Motion Planning for HERB
Informed RRT* was demonstrated on a high-dimensional
problem using HERB, a 14-DOF mobile manipulation platform
[11]. Poses were deﬁned for the two arms to create a sequence
of three planning problems (Fig. 15) inspired by [39]. The
objective of these problems was to ﬁnd the minimum path
length through a 14-dimensional search space with strict limits
(each joint has no more than π–2π radians of travel). While
path length is not a common cost function for manipulation,
these experiments illustrate that direct informed sampling is
beneﬁcial in high-dimensional problem domains even with
strict search limits.
RRT*, RRT* with pruning and rejection, and Informed RRT*
were each run for 50 trials on each problem of the cycle. The
resulting median path lengths are presented in Fig. 16. Trials
that did not ﬁnd a solution were considered to have inﬁnite
length for the purpose of calculating the median. This only
occurred for the problem from (a) to (b), where the planners
found a solution on 94% of the trials.
RRT* with and without pruning and rejection sampling
both fail to improve the initial solutions on all three planning
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 16


100
50
Success [%]
0
100
50
Success [%]
100
50
Success [%]
Fraction of optimal cost, γc∗
Log. run time [s]
Log. run time [s]
Log. run time [s]
Fraction of optimal cost, γc∗
Fraction of optimal cost, γc∗
100
10−1
10−2
100
10−2
102
100
(a) R2: Performance vs. target cost
(b) R4: Performance vs. target cost
(c) R8: Performance vs. target cost
1.05
1.04
1.03
1.02
1
1.01
1.1
1.06
1.08
1.04
1.02
1
1.1
1.06
1.08
1.04
1.02
1
100
50
Success [%]
0
100
50
Success [%]
0
100
50
Success [%]
0
Map width, l
Log. run time [s]
Log. run time [s]
Log. run time [s]
2
3
4
5
6
7
8
10
9
Map width, l
2
3
4
5
6
7
8
10
9
Map width, l
100
10−2
100
10−2
102
100
(d) R2: Performance vs. map width
(e) R4: Performance vs. map width
(f) R8: Performance vs. map width
5
10
15
20
25
30
35
50
40
45
100
50
Success [%]
0
100
0
50
Success [%]
100
0
50
Success [%]
Log. run time [s]
Solution cost
Solution cost
Solution cost
10−2
(g) R2: Performance vs. time
RRT* w/ xrand rejection
RRT* w/ pruning & rejection
Informed RRT*
RRT*
RRT* w/ graph pruning
RRT* w/ xnew rejection
1.1
1.3
10−1
100
Log. run time [s]
10−2
(h) R4: Performance vs. time
10−1
100
Log. run time [s]
(i) R8: Performance vs. time
101
3
2.5
2
1.5
10−2
10−1
100
101
102
2.5
2.0
1.5
0
0
10−1
1.5
1.4
1.2
Better
Better
Better
Better
Fig. 14. Results for the experiments described in Sections VII-A and VII-B. Each planner was run 100 different times in R2, R4, and R8 on each problem for
3, 30, and 150 seconds, respectively. The percentage of trials that found the desired solution are plotted above and the median performance is plotted below
for each experiment. Unsuccessful trials were assigned an inﬁnite value for the purpose of calculating the median and the error bars denote a nonparamentric
99% conﬁdence interval on the median value. The times required to ﬁnd different near-optimal solutions, ci < γc∗, for the problem illustrated in Fig. 13a
with l = 2 are presented in (a)–(c). The times required to ﬁnd a solution within a fraction of the known optimum (1.01c∗, 1.05c∗, and 1.15c∗, respectively)
for the problem illustrated in Fig. 13a for various map widths are presented in (d)–(f). Solution cost is plotted versus run time for the problem illustrated in
Fig. 13b in (g)–(i). Taken together, these experiments demonstrate the beneﬁts of direct informed sampling even in large or high-dimensional problems, with a
high number of obstacles, and many homotopy classes.
problems but Informed RRT* is able to improve the path length
by 3.9%, 7.9%, and 28.2%, respectively. The improvement for
(a) to (b) is not statistically signiﬁcant but (b) to (c) and (c) to
(d) demonstrate the beneﬁts of considering the relative sizes of
the informed set and problem domain in high state dimensions.
VIII. DISCUSSION & CONCLUSION
RRT* almost-surely converges asymptotically to the opti-
mum by asymptotically ﬁnding the optimal paths to every
state in the problem domain. This is inefﬁcient in single-query
scenarios as, once a solution is found, searches only need to
consider states that can belong to a better solution (i.e., the om-
niscient set; Deﬁnition 3, Lemma 4). Previous work has focused
search to estimates of this set (i.e., informed sets; Deﬁnition 7)
but has not used these estimates to analyze performance. This
paper proves that for holonomic problems the probability of
sampling an admissible informed set provides an upper bound
on the probability of improving a solution (Theorem 13).
A popular admissible heuristic for problems seeking to
minimize path length is the L2 norm (i.e., Euclidean distance).
This paper shows that existing techniques to exploit it are
insufﬁcient. The majority of approaches either reduce the ability
to ﬁnd solutions in other homotopy classes (i.e., reduce recall;
Deﬁnition 9) or fail to account for the reduction of the L2
informed set in response to solution improvement (i.e., have
decreasing precision; Deﬁnition 8). Even existing adaptive tech-
niques that address these problems (e.g., [9]) fail to account for
its factorial decrease in measure with state dimension (i.e., the
minimum-path-length curse of dimensionality; Theorem 14).
This paper presents a method to avoid these limitations
through direct sampling of the L2 informed set (Algs. 1–5;
Section IV). This approach generates uniformly distributed
samples in the informed set regardless of its size relative to
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 17


(a)
(b)
(c)
(d)
Fig. 15. A motion planning problem for HERB inspired by [39]. Planners
must ﬁnd a collision-free path between each pair of subsequent poses, e.g., (a)
to (b). HERB’s 14 DOFs and large number of potential self-collisions make
this a nontrivial planning problem for RRT*. The planners were given 600
seconds for each phase of the planning problem and the results are presented
in Fig 16.
the problem domain or the state dimension (i.e., it has 100%
recall and high precision). This paper presents Informed RRT*
as a demonstration of how these techniques can be used in
sampling-based planning (Algs. 6 and 7; Section V).
Informed RRT* considers all homotopy classes that could
provide a better solution (i.e., 100% recall), unlike sample
biasing techniques. It is effective regardless of the relative
size of the informed set or the state dimension, unlike sample
rejection or graph pruning. When the heuristic does not provide
any information (e.g., small planning problems and/or large
informed sets) it is identical to RRT*.
This paper also uses the shape of the L2 informed set to
analyze the theoretical performance of RRT* on minimum-
path-length problems (Section VI) by bounding the expected
solution cost (Lemma 17) and convergence rates (Theorems 18–
20). The bounds are sharp over the set of all (Lemma 17) or all
holonomic (Theorems 18–20) minimum-path-length planning
problems and algorithm conﬁgurations with the lower bounds
exact for an inﬁnite rewiring radius in the absence of obstacles
and constraints. These results prove that RRT* converges
sublinearly (i.e., slower than linear) for all conﬁgurations and
holonomic minimum-path-length problems and that focused
variants (e.g., Informed RRT*) can have linear convergence.
This analysis is extended experimentally to different conﬁgu-
rations. The results conﬁrm the theoretical ﬁndings and suggest
that obstacle- and constraint-free convergence remains linear
when the rewiring radius is constant but becomes sublinear
when it decreases in the manner proposed by [6]. As previous
analysis of this radius has focused on per-iteration complexity,
we believe this result motivates future research into the trade
off between per-iteration cost and convergence rate.
The practical advantages of Informed RRT* are shown on a
variety of planning problems (Section VII). These experiments
demonstrate how its theoretical convergence rate corresponds
to better performance on real planning problems. The amount
of improvement depends on how efﬁciently the L2 informed
set decreases the search domain and may be limited in small
problem domains and/or long circuitous solutions (e.g., the
small/low-dimensional problems in Section VII-A and the ﬁrst
problem of Section VII-C). The design of Alg. 3 assures that in
these situations Informed RRT* performs no worse than other
methods to exploit the L2 heuristic (e.g., rejection sampling).
Designing these experiments highlighted the relationship be-
tween the maximum edge length, η, and algorithm performance.
This user-selected value not only affected the time required to
Path length
8
(a) to (b)
Planning phase
4
(b) to (c)
(c) to (d)
RRT*
Informed RRT*
RRT* w/ pruning & rejection
2
6
Fig. 16.
Median path length results from the motion planning problems
depicted in Fig. 15. Planners found a solution between each pose in every trial
after 600 seconds other than the transition from (a) to (b), where solutions
were only found in 94% of the 50 trials. For the purpose of calculating the
median, these unsolved trials were assigned an inﬁnite cost. Error bars denote
a nonparamentric 99% conﬁdence interval on the median value. The results
show that even in the presence of strict state-space limits, Informed RRT* can
outperform rejection sampling in high-dimensional problems.
ﬁnd an initial solution but, as a result of (19), also the quality
of the solution found in ﬁnite time. Speciﬁcally, large values
of η appeared to decrease the difference between algorithms;
however, also resulted in order of magnitude increases in the
time required to ﬁnd initial solutions. When coupled with
the results of Section VII, this result should further motivate
more research into the effects of the RRT* tuning parameters,
η and rRRT∗, on real-time performance. Given that anytime
improvement of a solution is a major feature of RRT*, we
tuned η for these experiments to minimize the initial-solution
time on a series of independent test problems.
We believe that deﬁning precise and admissible informed
sets is a fundamental challenge of using anytime almost-surely
asymptotically optimal planners in real-world applications. The
L2 informed set is a sharp, uniformly admissible estimate of the
omniscient set for problems seeking to minimize path length,
even in the presence of constraints, and is exact in the absence
of obstacles and constraints. This suggests that any informed
set that is more precise must either (i) exploit additional infor-
mation about the problem domain (e.g., obstacles, constraints),
and/or (ii) be inadmissible for some minimum-path-length
planning problems. Finding ways to deﬁne new admissible
heuristics from additional problem-speciﬁc information could
potentially allow focused search algorithms to converge linearly
in the presence of obstacles and/or constraints.
We ultimately believe that heuristics are a key component of
successful planning algorithms. To this end, we are currently
investigating methods to extend heuristics to entire sampling-
based searches, similar to how A* [2] extends Dijkstra’s algo-
rithm [1]. We accomplish this in BIT* [34–36] by extending the
ideas presented in this paper to batches of randomly generated
samples. These samples are limited to informed sets and
searched in order of potential solution quality. Information
on OMPL implementations of both Informed RRT* and BIT*
are available at http://asrl.utias.utoronto.ca/code.
APPENDIX A
PROOFS OF LEMMAS 4 AND 5
This section restates and proves Lemmas 4 and 5.
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 18


A. Proof of Lemma 4
Lemma 4 (The necessity of adding states in the omniscient set).
Adding a state from the omniscient set, xnew ∈Xf, is a nec-
essary condition for RRT* to improve the current solution, ci,
ci+1 < ci =⇒xnew ∈Xf.
This condition is necessary but not sufﬁcient to improve
the solution as the ability of states in Xf to provide better
solutions at any iteration depends on the structure of the tree
(i.e., its optimality).
Proof. At the end of iteration i+1, the cost of the best solution
found by RRT* will be the minimum of the previous best
solution, ci, and the best cost of any new or newly improved
solutions, cnew,
ci+1 = min {ci, cnew} .
(28)
Each iteration of RRT* only adds connections to or from the
newly added state, xnew, and therefore all new or modiﬁed
paths pass through this new state. The cost of any of these
new paths that extend to the goal region will be bounded from
below by the cost of the optimal solution of a path through
xnew,
cnew ≥f (xnew) .
(29)
Lemma 4 is now proven by contradiction. Assume that
RRT* has a solution with cost ci after iteration i and that it
is improved at iteration i + 1 by adding a state not in the
omniscient set, ci+1 < ci, xnew ̸∈Xf. By (1), the costs of
solutions through any xnew ̸∈Xf are bounded from below by
the current solution,
f (xnew) ≥ci,
which by (29) is also a bound on the cost of any new or
modiﬁed solutions,
cnew ≥f (xnew) ≥ci.
By (28), the cost of the best solution found by RRT* at the
end of iteration i + 1 must therefore be ci. This contradicts
the assumption that the solution was improved by a state not
in the omniscient set and proves Lemma 4.
B. Proof of Lemma 5
Lemma 5 (The necessity of sampling states in the omniscient
set in holonomic planning). Sampling the omniscient set,
xrand ∈Xf, is a necessary condition for RRT* to improve the
current solution to a holonomic problem, ci, after an initial κ
iterations,
∀i ≥κ, ci+1 < ci =⇒xrand ∈Xf,
for any sample distribution that maintains a nonzero probability
over the entire omniscient set.
For simplicity, this statement is limited to holonomic planning
but it can be extended to speciﬁc constraints with appropriate
assumptions.
Proof. In RRT (and therefore RRT*), the distribution of
vertices in the graph approaches the sample distribution as
the number of iterations approach inﬁnity [? ]. In the limit,
all reachable regions of the problem domain with a nonzero
sampling probability will therefore be sampled and the number
of vertices in these regions will increase indeﬁnitely with the
number of iterations. This ever increasing number of vertices
means that the worst-case distance between any state in a
sampled subset and the nearest vertex in the graph will decrease
indeﬁnitely and monotonically.
Lemma 5 is now proven by contradiction. Assume that by
iteration κ there are a sufﬁcient number and distribution of
vertices in the tree such that all possible states in Xf are no
further than η from a vertex,
∀x ∈Xf, ∃v ∈V s.t. ∥x −v∥2 < η,
(30)
and that RRT* has a solution with cost ci after iteration i ≥κ.
Now assume that RRT* improves the solution at iteration i + 1
without sampling the omniscient set, ci+1 < ci, xrand ̸∈Xf.
As improving a solution requires adding a state from the
omniscient set, xnew ∈Xf, (Lemma 4) this implies that the
state added to the graph is not the randomly sampled state,
xnew ̸= xrand. These two states are related in holonomic
planning by expansion constraints, (2) and (3), that ﬁnd a new
state as near as possible to xrand and no further than η from
the nearest vertex in the tree.
The triangle inequality implies that the nearest vertex to the
sample, vnearest, is also the nearest vertex to the proposed new
state,
vnearest := arg min
v∈V
{∥xrand −v∥2}
≡arg min
v∈V
{∥xnew −v∥2} ,
which from (30) is bounded in its distance from xnew by
∥xnew −vnearest∥2 < η.
(31)
Due to (3), the relationship in (31) is only satisﬁed in holonomic
planning when xnew ≡xrand. As by assumption the random
sample is not a member of the omniscient set, xrand ̸∈Xf,
then therefore neither is the newly added state, xnew ̸∈Xf,
and by Lemma 4 the solution is not improved, ci+1 = ci. This
contradicts the assumption that the solution was improved
by sampling a state not in the omniscient set and proves
Lemma 5.
APPENDIX B
PROOF OF LEMMA 15
This section restates Lemma 15 as presented by [31] along
with a full proof as presented in [14].
Lemma 15 (The uniform distribution of samples transformed
into a hyperellipsoid from a unit n-ball. Originally Lemma 1
in [31]). If the random points distributed in a hyperellipsoid
are generated from the random points uniformly distributed
in a hypersphere through a linear invertible nonorthogonal
transformation, then the random points distributed in the
hyperellipsoid are also uniformly distributed.
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 19


Proof. Let the sets Xball ⊂Rn and Xellipse ⊂Rn be the unit
n-dimensional ball and a n-dimensional hyperellipsoid with
radii {rj}n
j=1, respectively, having measures of
λ (Xball) = ζn,
λ (Xellipse) = ζn
n
Y
j=1
rj.
Let pball (·) be the probability density function of samples
drawn uniformly from the unit n-ball such that,
pball (x) :=



1
ζn
,
∀x ∈Xball
0,
otherwise.
(32)
Let τ (·) be an invertible transformation from the unit n-ball
to a hyperellipsoid such that,
τ : Xball →Xellipse,
τ −1 : Xellipse →Xball.
By deﬁnition, the probability density function in the hyperel-
lipsoid, pellipse (·), resulting from applying this transformation
to samples distributed in the unit n-ball is then
pellipse (x) := pball
 τ −1 (x)
 det

dτ −1
dxellipse

x
 .
(33)
The proposed transformation in (12) has the inverse
τ −1 (xellipse) = L−1 (xellipse −xcentre) ,
and the Jacobian
dτ −1
dxellipse
= L−1.
(34)
Substituting (34) and (32) into (33) gives,
pellipse (x) :=



1
ζn
det
 L−1 ,
∀x ∈Xellipse
0,
otherwise,
(35)
using the fact that τ −1 (x) ∈Xball
⇐⇒x ∈Xellipse. As
pellipse (·) is constant for all xellipse ∈Xellipse, this proves
that using (12) to transform uniformly distributed samples
in the unit n-ball results in a uniform distribution over the
hyperellipsoid and proves Lemma 15.
For hyperellipsoids whose axes are orthogonal (e.g., a prolate
hyperspheroid), (35) can be expressed in a more familiar and
intuitive form. Using (13) for τ (·) and the orthogonality of
rotation matrices makes (35)
pellipse (x) :=



1
ζn
det

L′−1CT
we
 ,
∀x ∈Xellipse
0,
otherwise.
(36)
where L′ = diag (r1, r2, . . . , rn) is a diagonal matrix which
then simpliﬁes (36) to
pellipse (x) :=



1
ζn
Qn
j=1 rj
,
∀x ∈Xellipse
0,
otherwise,
(37)
since the determinant is a linear operator, all rotation matrices
have a unity determinant, det (Cwe) = 1, and the determinant
of a diagonal matrix is the product of its diagonal entries. As
expected, (37) is the inverse of the volume of an n-dimensional
hyperellipsoid with radii {rj}n
j=1.
APPENDIX C
PROOF OF LEMMA 17
This section restates and proves Lemma 17, which is used
in support of Theorems 18–20. An earlier version of this proof
appeared in [13].
Lemma
17 (Expected next-iteration cost of minimum–
path-length planning). The expected value of the next solution
to a minimum-path-length problem, E [ci+1], is bounded by
pf
nc2
i + c2
min
(n + 1) ci
+ (1 −pf) ci ≤E [ci+1] ≤ci,
(24 redux)
where ci is the current solution cost, cmin is the theoretical
minimum solution cost, n is the state dimension of the planning
problem, and pf = P (xnew ∈Xf) is the probability of adding
a state that is a member of the omniscient set (i.e., that can
belong to a better solution). While not explicitly shown, the
subset, Xf, and the probability of improving the solution, pf,
are generally functions of the current solution cost.
This lower bound is sharp over the set of all possible
minimum-path-length planning problems and algorithm con-
ﬁgurations and is exact for versions of RRT* with an inﬁnite
rewiring radius (i.e., η = ∞, and rRRT∗= ∞) searching an
obstacle-free environment without constraints.
Proof. Proof of the upper bound is trivial. RRT* only accepts
new solutions that improve its existing solution, assuring that
the cost monotonically decreases,
ci+1 ≤ci.
(38)
Proof of the lower bound comes from ﬁnding an exact
expression for the expected value of the solution cost found
in the absence of obstacles and constraints with an inﬁnite
rewiring neighbourhood.
The expected solution cost of RRT* depends on the proba-
bility of sampling the omniscient set,
E [ci+1] = pfE [ci+1 | xnew ∈Xf]
+ (1 −pf) E [ci+1 | xnew ̸∈Xf] ,
(39)
where pf = P (xnew ∈Xf). Adding a state from the omni-
scient set, Xf, is a necessary condition to improve the solution
(Lemma 4) and any other state will not change the solution
cost, E [ci+1 | xnew ̸∈Xf] = ci. This simpliﬁes (39) to
E [ci+1] = pfE [ci+1 | xnew ∈Xf] + (1 −pf) ci.
(40)
The costs of solutions found by adding states inside the
omniscient are bounded from below by the optimal path through
the newly added state,
E [ci+1 | xnew ∈Xf] ≥E [f (xnew) | xnew ∈Xf] ,
(41)
where f (x) is the cost of the optimal path from the start
to the goal constrained to pass through a state, x. With a
uniform sample distribution over Xf the right-hand side of
(41) becomes
E [f (xnew) | xnew ∈Xf] =
1
λ (Xf)
Z
Xf
f (xnew) dV.
When RRT* uses an inﬁnite rewiring radius it attempts
connections between every new state and the start and goal.
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 20


In the absence of obstacles and constraints these paths will
be feasible and represent the optimal solutions using the state.
This makes the expected value of this best-case conﬁguration
of RRT* equivalent to the expected optimal solution cost in
the absence of obstacles,
E [ci+1 | xnew ∈Xf]∗≡E [f (xnew) | xnew ∈Xf] .
(42)
The lower bound provided by (41) is therefore sharp over the set
of all possible planning problems and algorithm conﬁgurations.
In this absence of obstacles and constraints, the optimal
solution using any state is given by (4) and the omniscient set
is the prolate hyperspheroid, Xf ≡X b
f ≡XPHS. The measure
of the omniscient set, λ (Xf) = λPHS, is given by (5). This
allows (42) to be written as
E [ci+1 | xnew ∈Xf]∗=
1
λPHS
Z
XPHS
 ∥x −xstart∥2
+ ∥xgoal −x∥2

dV. (43)
The prolate hyperspheroidal coordinates, µ, ν, ψ1, . . . , ψn−2,
x1 = a cosh µ cos ν,
x2 = a sinh µ sin ν cos ψ1,
x3 = a sinh µ sin ν sin ψ1 cos ψ2,
...
xn−1 = a sinh µ sin ν sin ψ1 sin ψ2 . . . sin ψn−3 cos ψn−2,
xn = a sinh µ sin ν sin ψ1 sin ψ2 . . . sin ψn−3 sin ψn−2,
and the parameterization a = 0.5cmin, simpliﬁes (4) to
f (x) = cmin cosh µ.
(44)
Substituting (44) and the prolate hyperspheroidal differential
volume,
dV = an  sinh2 µ + sin2 ν

sinhn−2 µ sinn−2 ν sinn−3 ψ1 . . .
sin ψn−3 dµ dν dψ1 . . . dψn−2,
into (43) results in
E [ci+1 | xnew ∈Xf]∗=
cn+1
min
2nλPHS
Z µi
µ=0
Z π
ν=0
Z π
ψ1=0
. . .
Z π
ψn−3=0
Z 2π
ψn−2=0
 sinh2 µ + sin2 ν

sinhn−2 µ cosh µ sinn−2 ν sinn−3 ψ1
. . . sin ψn−3 dµ dν dψ1, . . . dψn−2,
(45)
where the integration limit for µ is derived from (44) as
cosh µi :=
ci
cmin
.
(46)
Integrating (45) requires applying a series of identities, ﬁrst
(n −1) ζn−1 ≡
Z π
ψ1=0
. . .
Z π
ψn−3=0
Z 2π
ψn−2=0
sinn−3 ψ1
. . . sin ψn−3 dψ1 . . . dψn−2,
simpliﬁes (45) to
E [ci+1 | xnew ∈Xf]∗= (n −1) cn+1
min ζn−1
2nλPHS
Z µi
µ=0
Z π
ν=0
 sinh2 µ + sin2 ν

sinhn−2 µ cosh µ sinn−2 ν dµ dν. (47)
Next, the deﬁnite integral of the product of powers of sin and
cos,
Z π
0
sin2m−1 θ cos2n−1 θ dθ ≡B (m, n) ,
where B (·, ·) is the beta function,
B (m, n) :=
Z 1
0
tm−1 (1 −t)n−1 dt,
is used to evaluate the integral over ν in (47), giving
E [ci+1 | xnew ∈Xf]∗= (n −1) cn+1
min ζn−1
2nλPHS

B
n −1
2
, 1
2
 Z µi
µ=0
sinhn µ cosh µ dµ
+ B
n + 1
2
, 1
2
 Z µi
µ=0
sinhn−2 µ cosh µ dµ

. (48)
The identity,
B (m + 1, n) ≡
m
m + nB (m, n) ,
and the recursive nature of the n-dimensional unit ball,
ζn ≡B
n + 1
2
, 1
2

ζn−1,
simpliﬁes (48) to
E [ci+1 | xnew ∈Xf]∗= cn+1
min ζn
2nλPHS

n
Z µi
µ=0
sinhn µ cosh µ dµ
+ (n −1)
Z µi
µ=0
sinhn−2 µ cosh µ dµ

. (49)
The indeﬁnite integral,
Z
sinhm θ cosh θ dθ ≡sinhm+1 θ
m + 1
,
is then used to evaluate (49), giving
E [ci+1 | xnew ∈Xf]∗= cn+1
min ζn
2nλPHS

n
n + 1 sinhn+1 µi + sinhn−1 µi

.
(50)
Using (5) to expand the measure λPHS in (50) cancels the
measure of the unit n-ball, giving
E [ci+1 | xnew ∈Xf]∗=
cn+1
min
ci (c2
i −c2
min)
n−1
2

n
n + 1 sinhn+1 µi + sinhn−1 µi

.
(51)
Using the relationship
cosh µ = b ⇐⇒sinh µ =
p
b2 −1,
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 21


some algebraic manipulation, and (46) ﬁnally simpliﬁes (51)
to
E [ci+1 | xnew ∈Xf]∗= nc2
i + c2
min
(n + 1) ci
,
an exact value for the best-case expected solution cost of RRT*.
This result allows (40) to be written as the sharp bound,
E [ci+1] ≥pf
nc2
i + c2
min
(n + 1) ci
+ (1 −pf) ci,
which when combined with (38) proves Lemma 17.
APPENDIX D
PROOFS OF THEOREMS 18–20
This section restates and proves Theorems 18–20.
A. Proof of Theorem 18
Theorem 18 (Sublinear convergence of RRT* in holonomic
minimum-path-length planning). RRT* converges sublinearly
towards the optimum of holonomic minimum-path-length
planning problems,
E [µRRT∗] = 1.
(25 redux)
For simplicity, this statement is limited to holonomic planning
but it can be extended to speciﬁc constraints by expanding
Lemma 5.
Proof. The expected rate of convergence (Deﬁnition 16) of
RRT* is
E [µRRT∗] = E

lim
i→∞
ci −c∗
ci−1 −c∗

,
(52)
since ∀i, ci ≥c∗. As RRT* almost-surely converges asymp-
totically to the optimum, this sequence also almost-surely
converges to a ﬁnite value, 0 ≤µRRT∗≤1,
P

lim
i→∞
ci −c∗
ci−1 −c∗= µRRT∗

= 1.
By Lebesgue’s dominated convergence theorem this allows
the expectation operator to be brought inside the limit of (52),
giving
E [µRRT∗] = lim
i→∞
E [ci] −c∗
ci−1 −c∗,
(53)
since ci is the only random variable at iteration i.
Lemma 17 provides sharp bounds for the expected solution
cost at any iteration, E [ci], with the lower-bound corresponding
to an inﬁnite rewiring radius in the absence of obstacles and
constraints. Substituting this lower bound and that c∗= cmin
in the absence of obstacles into (53) and simplifying gives an
expression for the expected best-case convergence rate,
E [µ∗
RRT∗] = 1 +
1
(n + 1) lim
i→∞
pf
 c2
min −c2
i−1

 c2
i−1 −cminci−1
,
such that E [µ∗
RRT∗] ≤E [µRRT∗] is a sharp bound over
all possible planning problems and algorithm conﬁgurations.
Applying l’Hˆopital’s rule [? ] with respect to ci−1 gives
E [µ∗
RRT∗] = 1 +
1
(n + 1)
lim
i→∞
∂pf
∂ci−1
 c2
min −c2
i−1

−2pfci−1
(2ci−1 −cmin)
. (54)
As iterations go to inﬁnity the probability of adding a sample
in Xf becomes the probability of sampling it (Lemma 5). The
lower bound from Lemma 17 is for an obstacle- and constraint-
free problem and therefore the informed set is the omniscient
set, Xf ≡X b
f, and the probability of sampling it is given by
(7) with a partial derivative of
∂pf
∂ci−1
=
π
n
2
2nΓ
  n
2 + 1

λ (Xsamp)
 c2
i−1 −c2
min
 n−1
2
 
1 + (n −1) c2
i−1
 c2
i−1 −c2
min

!
.
Almost-sure convergence to cmin implies limi→∞ci−1 =
cmin and therefore limi→∞pf = 0 and limi→∞
∂pf
∂ci−1 = 0,
making (54),
E [µ∗
RRT∗] = 1.
As by deﬁnition the expected rate of convergence of RRT* is
bounded by,
E [µ∗
RRT∗] ≤E [µRRT∗] ≤1,
this result proves Theorem 18.
B. Proof of Theorem 19
Theorem 19 (Linear convergence of RRT* with adaptive rect-
angular rejection sampling in holonomic minimum-path-length
planning). RRT* with adaptive rectangular rejection sampling
converges at best linearly towards the optimum of holonomic
minimum-path-length planning problems but factorially ap-
proaches sublinear convergence with increasing state dimen-
sion,
1 −
π
n
2
(n + 1) 2n−1Γ
  n
2 + 1
 ≤E [µRect] ≤1.
(26 redux)
For simplicity, this statement is limited to holonomic planning
but it can be extended to speciﬁc constraints by expanding
Lemma 5.
Proof. Proof of Theorem 19 follows that of Theorem 18 but
with the probability of adding a new state from Xf instead
calculated from (7) using (10), as
pf ≤
π
n
2
2nΓ
  n
2 + 1
.
(55)
As
∂pf
∂ci−1 = 0, (54) becomes
E [µ∗
Rect] = 1 −
1
(n + 1) lim
i→∞
2pfci−1
(2ci−1 −cmin).
(56)
Noting
that
almost-sure
convergence
to
cmin
implies
limi→∞ci−1 = cmin and substituting (55) into (56) results
in
E [µ∗
Rect] = 1 −
2pf
(n + 1),
≥1 −
π
n
2
(n + 1) 2n−1Γ
  n
2 + 1
.
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 22


As by deﬁnition the expected rate of convergence of RRT*
with rectangular rejection sampling is bounded by,
E [µ∗
Rect] ≤E [µRect] ≤1.
This result proves Theorem 19 with sharp bounds over all
possible holonomic planning problems and algorithm conﬁgu-
rations.
C. Proof of Theorem 20
Theorem 20 (Linear convergence of Informed RRT* in
holonomic minimum-path-length planning). Informed RRT*
converges at best linearly towards the optimum of holonomic
minimum-path-length planning problems,
n −1
n + 1 ≤E [µInf] ≤1,
(27 redux)
where the lower-bound occurs exactly with an inﬁnite rewiring
neighbourhood in the absence of obstacles and constraints.
For simplicity, this statement is limited to holonomic planning
but it can be extended to speciﬁc constraints by expanding
Lemma 5.
Proof. Proof of Theorem 20 follows that of Theorem 18 but
with a unity probability of adding a new state from Xf. From
(54), the convergence rate of Informed RRT* is then,
E [µ∗
Inf] = 1 −
1
(n + 1) lim
i→∞
2ci−1
(2ci−1 −cmin).
As almost-sure convergence to cmin implies limi→∞ci−1 =
cmin, this gives,
E [µ∗
Inf] = n −1
n + 1.
As by deﬁnition the expected rate of convergence of RRT*
with rectangular rejection sampling is bounded by,
E [µ∗
Inf] ≤E [µInf] ≤1.
This result proves Theorem 20 with sharp bounds over all
possible holonomic planning problems and algorithm conﬁgu-
rations.
ACKNOWLEDGMENT
The authors would like to thank the editorial board and
reviewers for their helpful comments. We would also like to
thank Laszlo-Peter Berczi for discussions on precision and
recall, Christopher Dellin and Michael Koval for discussions
and insight on the sampling of arbitrarily overlapping shapes,
Jennifer King and Clinton Liddick for help running the HERB
experiments, and Paul Newman for providing the time to ﬁnish
this manuscript at the University of Oxford.
REFERENCES
[1] E. W. Dijkstra, “A note on two problems in connexion
with graphs,” Numerische Mathematik, vol. 1, no. 1, pp.
269–271, 1959.
[2] P. E. Hart, N. J. Nilsson, and B. Raphael, “A formal basis
for the heuristic determination of minimum cost paths,”
IEEE Transactions on Systems Science and Cybernetics,
vol. 4, no. 2, pp. 100–107, Jul. 1968.
[3] L. E. Kavraki, P. ˇSvestka, J.-C. Latombe, and M. H.
Overmars, “Probabilistic roadmaps for path planning in
high-dimensional conﬁguration spaces,” IEEE Transac-
tions on Robotics and Automation, vol. 12, no. 4, pp.
566–580, 1996.
[4] D. Hsu, R. Kindel, J.-C. Latombe, and S. Rock, “Random-
ized kinodynamic motion planning with moving obstacles,”
The International Journal of Robotics Research, vol. 21,
no. 3, pp. 233–255, 2002.
[5] S. M. LaValle and J. J. Kuffner Jr., “Randomized kinody-
namic planning,” The International Journal of Robotics
Research, vol. 20, no. 5, pp. 378–400, 2001.
[6] S. Karaman and E. Frazzoli, “Sampling-based algorithms
for optimal motion planning,” The International Journal
of Robotics Research, vol. 30, no. 7, pp. 846–894, 2011.
[7] D. Ferguson and A. Stentz, “Anytime RRTs,” in Pro-
ceedings of the IEEE/RSJ International Conference on
Intelligent Robots and Systems (IROS), 2006, pp. 5369–
5375.
[8] B. Akgun and M. Stilman, “Sampling heuristics for opti-
mal motion planning in high dimensions,” in Proceedings
of the IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), 2011, pp. 2640–2645.
[9] M. Otte and N. Correll, “C-FOREST: Parallel shortest
path planning with superlinear speedup,” IEEE Transac-
tions on Robotics (T-RO), vol. 29, no. 3, pp. 798–806,
Jun. 2013.
[10] I. A. S¸ucan, M. Moll, and L. E. Kavraki, “The Open
Motion Planning Library,” IEEE Robotics & Automation
Magazine, vol. 19, no. 4, pp. 72–82, Dec. 2012, library
available from http://ompl.kavrakilab.org.
[11] S. Srinivasa, D. Berenson, M. Cakmak, A. Collet Romea,
M. Dogar, A. Dragan, R. A. Knepper, T. D. Niemueller,
K. Strabala, J. M. Vandeweghe, and J. Ziegler, “HERB 2.0:
Lessons learned from developing a mobile manipulator
for the home,” Proceedings of the IEEE, vol. 100, no. 8,
pp. 1–19, Jul. 2012.
[12] J. D. Gammell, S. S. Srinivasa, and T. D. Barfoot,
“Informed RRT*: Optimal sampling-based path planning
focused via direct sampling of an admissible ellipsoidal
heuristic,” in Proceedings of the IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS),
Chicago, Illinois, USA, 14–18 Sep. 2014, pp. 2997–3004.
[13] ——, “On recursive random prolate hyperspheroids,”
Autonomous
Space
Robotics
Lab,
University
of
Toronto, Tech. Rep. TR-2014-JDG002, Mar. 2014,
arXiv:1403.7664 [math.ST].
[14] J. D. Gammell and T. D. Barfoot, “The probability
density function of a transformation-based hyperellipsoid
sampling technique,” Autonomous Space Robotics Lab,
University of Toronto, Tech. Rep. TR-2014-JDG004, Apr.
2014, arXiv:1404.1347 [math.ST].
[15] J. D. Gammell, T. D. Barfoot, and S. S. Srinivasa, “In-
formed sampling for asymptotically optimal path planning
(consolidated version),” Autonomous Space Robotics Lab,
University of Toronto, Tech. Rep., Jun. 2017, arXiv:
1706.06454 [cs.RO].
[16] L. Janson, E. Schmerling, A. Clark, and M. Pavone, “Fast
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 23


marching tree: A fast marching sampling-based method
for optimal motion planning in many dimensions,” The
International Journal of Robotics Research (IJRR), vol. 34,
no. 7, pp. 883–921, 2015.
[17] J. Nasir, F. Islam, U. Malik, Y. Ayaz, O. Hasan, M. Khan,
and M. S. Muhammad, “RRT*-SMART: A rapid conver-
gence implementation of RRT*,” International Journal
of Advanced Robotic Systems, vol. 10, p. 299, 2013.
[18] S. Kiesel, E. Burns, and W. Ruml, “Abstraction-guided
sampling for motion planning,” in Proceedings of the
Fifth Annual Symposium on Combinatorial Search (SoCS),
2012.
[19] D. Kim, J. Lee, and S.-E. Yoon, “Cloud RRT*: Sampling
cloud based RRT*,” in Proceedings of the IEEE Interna-
tional Conference on Robotics and Automation (ICRA),
May 2014, pp. 2519–2526.
[20] H. Choset and J. Burdick, “Sensor based planning, part
I: The generalized voronoi graph,” in Proceedings of
the IEEE International Conference on Robotics and
Automation (ICRA), vol. 2, May 1995, pp. 1649–1655.
[21] S. Karaman, M. R. Walter, A. Perez, E. Frazzoli, and
S. Teller, “Anytime motion planning using the RRT*,”
in Proceedings of the IEEE International Conference on
Robotics and Automation (ICRA), 2011, pp. 1478–1483.
[22] O. Arslan and P. Tsiotras, “Use of relaxation methods in
sampling-based algorithms for optimal motion planning,”
in Proceedings of the IEEE International Conference on
Robotics and Automation (ICRA), 2013.
[23] ——, “Dynamic programming guided exploration for
sampling-based motion planning algorithms,” in Proceed-
ings of the IEEE International Conference on Robotics
and Automation (ICRA), May 2015, pp. 4819–4826.
[24] C. Urmson and R. Simmons, “Approaches for heuristically
biasing RRT growth,” in Proceedings of the IEEE/RSJ In-
ternational Conference on Intelligent Robots and Systems
(IROS), vol. 2, 2003, pp. 1178–1183.
[25] R. Alterovitz, S. Patil, and A. Derbakova, “Rapidly-
exploring roadmaps: Weighing exploration vs. reﬁnement
in optimal motion planning,” in Proceedings of the IEEE
International Conference on Robotics and Automation
(ICRA), 2011, pp. 3706–3712.
[26] Y. X. Shan, B. J. Li, J. Zhou, and Y. Zhang, “An approach
to speed up RRT*,” in Proceedings of the IEEE Intelligent
Vehicles Symposium (IV), Jun. 2014, pp. 594–598.
[27] O. Salzman and D. Halperin, “Asymptotically near-
optimal RRT for fast, high-quality, motion planning,” in
Proceedings of the IEEE International Conference on
Robotics and Automation (ICRA), May 2014, pp. 4680–
4685.
[28] D. Devaurs, T. Sim´eon, and J. Cort´es, “Efﬁcient sampling-
based approaches to optimal path planning in complex
cost spaces,” in Algorithmic Foundations of Robotics XI,
ser. Springer Tracts in Advanced Robotics, H. L. Akin,
N. M. Amato, V. Isler, and A. F. van der Stappen, Eds.
Springer International Publishing, 2015, vol. 107, pp. 143–
159.
[29] M. Otte and E. Frazzoli, “RRTX: Asymptotically opti-
mal single-query sampling-based motion planning with
quick replanning,” The International Journal of Robotics
Research (IJRR), vol. 35, no. 7, pp. 797–822, 2016.
[30] L. Euler, “De progressionibus transcendentibus seu
quarum termini generales algebraice dari nequeunt,” Com-
mentarii academiae scientiarum Petropolitanae, vol. 5,
pp. 36–57, 1738.
[31] H. Sun and M. Farooq, “Note on the generation of
random points uniformly distributed in hyper-ellipsoids,”
in Proceedings of the Fifth International Conference on
Information Fusion, vol. 1, 2002, pp. 489–496.
[32] G. Wahba, “A least squares estimate of satellite attitude,”
Society for Industrial and Applied Mathematics (SIAM)
Review, vol. 7, p. 409, 1965.
[33] A. H. J. de Ruiter and J. R. Forbes, “On the solution
of Wahba’s problem on SO(n),” The Journal of the
Astronautical Sciences, vol. 60, no. 1, pp. 1–31, 2013.
[34] J. D. Gammell, S. S. Srinivasa, and T. D. Barfoot,
“Batch informed trees (BIT*): Sampling-based optimal
planning via the heuristically guided search of implicit
random geometric graphs,” in Proceedings of the IEEE
International Conference on Robotics and Automation
(ICRA), 2015, pp. 3067–3074.
[35] J. D. Gammell, “Informed anytime search for continuous
planning problems,” Ph.D. dissertation, University of
Toronto, Feb. 2017.
[36] J. D. Gammell, T. D. Barfoot, and S. S. Srinivasa,
“Informed asymptotically optimal anytime search,” The
International Journal of Robotics Research (IJRR), 2018,
manuscript #IJR-17-2980, in revision, arXiv: 1707.01888
[cs.RO].
[37] A. Dobson, G. V. Moustakides, and K. E. Bekris, “Ge-
ometric probability results for bounding path quality in
sampling-based roadmaps after ﬁnite computation,” in
Proceedings of the IEEE International Conference on
Robotics and Automation (ICRA), 2015, pp. 4180–4186.
[38] A. Perez, S. Karaman, A. Shkolnik, E. Frazzoli, S. Teller,
and M. R. Walter, “Asymptotically-optimal path planning
for manipulation using incremental sampling-based algo-
rithms,” in Proceedings of the IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS),
2011, pp. 4307–4313.
[39] J. Morali and V. Willis, “Y.M.C.A.” Cruisin’, Nov. 13
1978, Casablanca Records NBLP 7118.
[40] J. D. Gammell, T. D. Barfoot, and S. S. Srinivasa,
“Informed sampling for asymptotically optimal path plan-
ning,” IEEE Transactions on Robotics (T-RO), 2018.
Jonathan D. Gammell is a Departmental Lecturer in
Robotics with the Oxford Robotics Institute (ORI) at
the University of Oxford, Oxford, United Kingdom.
He performed this work at the Autonomous Space
Robotics Lab at the University of Toronto, Toronto,
Canada during his Ph. D. degree. He is interested in
developing conceptually sound approaches to the
fundamental problems of real-world autonomous
robotics.
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.


## Page 24


Timothy D. Barfoot is a Professor at the University
of Toronto Institute for Aerospace Studies (UTIAS).
He holds the Canada Research Chair (Tier II) in
Autonomous Space Robotics and works in the area
of guidance, navigation, and control of mobile robots
in a variety of applications. He is interested in
developing methods to allow mobile robots to operate
over long periods of time in large-scale, unstructured,
three-dimensional environments, using rich onboard
sensing (e.g., cameras and laser rangeﬁnders) and
computation.
Dr. Barfoot took up his position at UTIAS in May 2007, after spending
four years at MDA Space Missions, where he developed autonomous vehicle
navigation technologies for both planetary rovers and terrestrial applications
such as underground mining. He sits on the editorial boards of the International
Journal of Robotics Research and the Journal of Field Robotics. He recently
served as the General Chair of Field and Service Robotics (FSR) 2015, which
was held in Toronto.
Siddhartha S. Srinivasa is the Boeing Endowed
Professor at the School of Computer Science and
Engineering, University of Washington. He works
on robotic manipulation, with the goal of enabling
robots to perform complex manipulation tasks under
uncertainty and clutter, with and around people. To
this end, he founded the Personal Robotics Lab in
2005. Dr. Srinivasa is also passionate about building
end-to-end systems (HERB, ADA, HRP3, CHIMP,
Andy, among others) that integrate perception, plan-
ning, and control in the real world. Understanding
the interplay between system components has helped produce state of the
art algorithms for robotic manipulation, motion planning, object recognition
and pose estimation (MOPED), and dense 3D modelling (CHISEL, now
used by Google Project Tango), and mathematical models for Human-Robot
Collaboration.
This document consolidates the published paper [40] with its supplementary material and presents it as reviewed.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
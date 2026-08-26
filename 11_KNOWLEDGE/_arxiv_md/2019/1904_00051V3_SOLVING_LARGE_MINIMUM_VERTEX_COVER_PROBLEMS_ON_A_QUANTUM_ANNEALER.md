---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1904.00051v3
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1904.00051v3_Solving_large_Minimum_Vertex_Cover_problems_on_a_quantum_annealer

> Source: 1904.00051v3_Solving_large_Minimum_Vertex_Cover_problems_on_a_quantum_annealer.pdf

> Pages: 16

---


## Page 1


Solving large Minimum Vertex Cover problems on a quantum
annealer
Elijah Pelofske∗, Georg Hahn†, and Hristo Djidjev∗
Abstract
We consider the minimum vertex cover problem having applications in e.g. biochemistry
and network security. Quantum annealers can ﬁnd the optimum solution of such NP-hard
problems, given they can be embedded on the hardware. This is often infeasible due to
limitations of the hardware connectivity structure.
This paper presents a decomposition
algorithm for the minimum vertex cover problem: The algorithm recursively divides an arbi-
trary problem until the generated subproblems can be embedded and solved on the annealer.
To speed up the decomposition, we propose several pruning and reduction techniques. The
performance of our algorithm is assessed in a simulation study.
Keywords: Decomposition algorithm; D-Wave; Minimum Vertex Cover; Optimization.
1
Introduction
We consider the minimum vertex cover problem (abbreviated as MVC in the remainder of this
article), one of Karp’s 21 NP-complete problems. Formally, we are given an undirected graph
G = (V, E) with vertex set V and edge set E ⊆V × V . A subset V ′ ⊆V is called a vertex cover
if every edge in E has at least one endpoint in V ′, that is, if for every e = (u, v) ∈E it holds
true that u ∈V ′ or v ∈V ′. A minimum vertex cover is a vertex cover of minimum size.
For NP-hard (graph) problems, such as MVC, graph partitioning or the maximum clique
problem, novel technology allows us to obtain solutions which are very hard to ﬁnd classically
Chapuis et al. (2017). One such device is the quantum annealer of D-Wave Systems, Inc. (D-
Wave, 2016), which allows us to ﬁnd approximate solutions of quadratic unconstrained binary
optimization and Ising problems, given by the minimization min H(x1, . . . , xn), where
H(x1, . . . , xn) =
n
X
i=1
aixi +
X
i<j
aijxixj.
(1)
In (1), the ai ∈R, i ∈{1, . . . , n}, are linear weights and aij ∈R for i < j are quadratic
couplers.
The problem (1) is called a quadratic unconstrained binary optimization (QUBO)
problem if xi ∈{0, 1} and an Ising problem if xi ∈{−1, +1} for all i. The function (1) is
often called a QUBO or Ising Hamiltonian, respectively. Both QUBO and Ising formulations
are equivalent (Djidjev et al., 2016). The D-Wave quantum annealer aims to ﬁnd a minimum of
∗Los Alamos National Laboratory, Los Alamos, NM 87545, USA
†Lancaster University, Lancaster LA1 4YW, U.K.
1
arXiv:1904.00051v3  [quant-ph]  1 May 2019


## Page 2


the function (1) by mapping it to a physical quantum system, from which a solution is read oﬀ
after annealing is completed.
It is known that many NP-hard problems can be easily expressed as the minimization of
a Hamiltonian of the form (1) including, for instance, graph partitioning, graph coloring, or
maximum clique ﬁnding: see Lucas (2014) for a comprehensive overview of QUBO and Ising
Hamiltonians for a variety of NP-hard problems. According to (Lucas, 2014, Section 4.3), the
MVC Hamiltonian for a graph G = (V, E) is given by
H = A
X
(u,v)∈E
(1 −xu)(1 −xv) + B
X
v∈V
xv.
(2)
In (2), each xv ∈{0, 1} for v ∈V is a binary variable indicating if vertex v belongs to the MVC.
The ﬁrst term in (2) encodes the constraint that each edge in G is incident to at least one vertex
in the MVC, and the second term is simply the size of the MVC. As shown in Lucas (2014),
choosing 0 < B < A ensures that minimizing (2) is equivalent to solving the MVC problem. As
an explicit choice, we ﬁx B = 1 and A = 2 in the remainder of the article.
Our goal in this paper is to compute the minimum of (2) on a quantum annealer. However,
this is often not possible without preprocessing due to a variety of reasons: First, there is a
limitation on the input problem sizes we can solve due to the ﬁnite number of available qubits
(up to roughly 5000 qubits for the newest D-Wave generation). Second, even if the number of
qubits exceeds the number of variables, the current (D-Wave) technology provides only limited
qubit connectivity (D-Wave, 2016). It is thus not guaranteed that all the required quadratic
couplers in (2) needed to map MVC onto the annealer hardware are available. This problem can
be alleviated with a so-called minor embedding of the problem Hamiltonian onto the D-Wave
hardware, where each variable is embedded onto a set of connected qubits, rather than a single
one, at the expense, however, of a severe reduction in the number of available qubits (Chapuis
et al., 2017). For instance, the largest embeddable complete graph on D-Wave 2X has 46 vertices,
thus guaranteeing that arbitrary problems with 46 variables can be approximated on D-Wave.
In this article we propose a novel decomposition algorithm for MVC in order to allow larger
problems to be solved on D-Wave (for instance, problem sizes exceeding the number of available
qubits). The decomposition algorithm recursively splits a given instance of MVC into smaller
subproblems until, at a certain recursion level, the generated subproblems are small enough
to be solved directly, e.g., using a quantum annealer. The decomposition algorithm is exact,
meaning that the optimality of the solution is guaranteed provided all generated subproblems
are solved exactly. A variety of techniques outlined in Section 3 allows us to eliminate entire
subproblems during the recursion that cannot contribute to the MVC, or to reduce the size of
subproblems by removing vertices which cannot belong to the MVC.
This article is structured as follows. After a brief literature review in Section 1.1, Section 2
introduces our decomposition algorithm for MVC. To prune subproblems during the decom-
position, we discuss a variety of bounds on the size of the MVC in Section 3. We assess the
performance of our decomposition method in a detailed simulation study in Section 4. The
article concludes with a discussion of our results in Section 5.
2


## Page 3


v
G−
G+
Figure 1: Illustration of the vertex splitting at a vertex v.
1.1
Literature review
The development of exact algorithms for NP-hard problems has been an area of constant atten-
tion in the literature (Johnson and , Eds.; DIMACS, 2000; Woeginger, 2008).
In particular, the minimum vertex cover problem has been widely studied in the literature
from a variety of aspects (Downey and Fellows, 1992; Balasubramanian et al., 1998; Stege and
Fellows, 1999; Chen et al., 2000, 2001; Niedermeier and Rossmanith, 2003). For instance, Chen
et al. (2010) present a selection of techniques to reduce the size of an MVC instance and introduce
a polynomial space and exponential time algorithm of the order of O(1.27k), where k is the
sought maximal size of the MVC, thus improving over the O(1.29k) algorithm of Niedermeier
and Rossmanith (2007).
A variation of the MVC problem, the weighted MVC problem, is
studied in Xu et al. (2016).
Decomposition algorithms, such as the algorithm presented in this article, have already been
suggested in Tarjan (1985) and successfully applied to solve a variety of NP-hard problems (see
Rao (2008)) such as graph coloring.
A decomposition algorithm for another NP-hard graph problem, the maximum clique prob-
lem, has been proposed in Chapuis et al. (2017); Pelofske et al. (2019). In Pelofske et al. (2019),
the authors additionally investigate a variety of techniques to prune subproblems during the re-
cursive decomposition, for instance by computing bounds on the clique size. Similarly, to solve
the maximum independent set problem, an equivalent formulation of the maximum clique prob-
lem, several algorithms are known including some relying on graph decomposition (Giakoumakis
and Vanherpe, 1997; Courcelle et al., 2000).
2
A decomposition method for MVC
The focus of this article lies on a decomposition algorithm for MVC instances presented in this
section.
We are given a graph G = (V, E) for which we aim to compute a MVC. Let V ′ ⊆V denote
the (unknown) MVC. If G cannot be processed as a whole, we suggest the following technique
to split the problem into two subproblems. Select any vertex v ∈V . Then there are two cases:
3


## Page 4


Either v ∈V ′ or v /∈V ′, each case leading to a subproblem of reduced size (see Figure 1, top).
If v ∈V ′, we augment the set of vertices belonging to the MVC by v; afterwards, we can
remove v and all edges adjacent to v since those edges are already covered by the choice of v.
This is illustrated in Figure 1 with subgraph G+.
If v /∈V ′, we observe that for all edges with endpoint v, that is all (v, u) ∈E, it must hold
true that u ∈V ′. This is true since, if v /∈V ′, those edges must still be covered by their other
endpoint u in the MVC. Also, we can remove v from G since we know it is not in the MVC
(likewise we can remove all u with (u, v) ∈V and the adjacent edges of all such u since those
vertices are known to belong to the MVC). In Figure 1, under the assumption that v ̸∈V ′, all
vertices inside the blue circle must belong to the MVC. After removing v and all its adjacent
edges, and assigning all encircled vertices to the MVC, we are left with the subgraph G−.
Since the cases v ∈V ′ and v /∈V ′ are exhaustive, we split G into both G+ and G−and
continue to compute MVC on both subgraphs. If either graph is still too large to compute
an (exact) solution of MVC on it, the above decomposition can be recursively applied. In a
recursive application, some bookkeeping is needed to remember the current set of cover vertices
for each generated subgraph.
Since neither of the generated subgraphs G+ and G−contains v, the graph size is reduced
by at least one in each recursion level, thus guaranteeing the termination of the algorithm.
The algorithm as described will output the exact MVC given we employ an exact method
to solve MVC on the subgraphs at leaf level. Typically, for instance when applying D-Wave
at leaf level to compute MVC solutions for graphs of at most 46 vertices (see Section 1), an
exact solution is not guaranteed. However, our algorithm can also be applied probabilistically:
If the solver applied to the subgraphs at leaf level ﬁnds optimal solutions with probability p,
our decomposition algorithm will report the correct MVC for the original graph with the same
probability p.
3
Pruning techniques for MVC
The recursive decomposition proposed in Section 2 can be simpliﬁed and accelerated using a
variety of bounding and pruning techniques.
3.1
Upper and lower bounds
First, we bound the size of the MVC of each generated subgraph. If a lower bound on any
subgraph exceeds the current best vertex cover size, we do not need to consider that subproblem
for further decomposition as it cannot contain an optimal solution. We compute the following
lower bounds:
(i) First, we take the maximum of three easy to compute deterministic lower bounds.
• The function min weighted vertex cover of the NetworkX package (Hagberg et al.,
2008) computes an approximate vertex cover of at most twice the size of the optimal
cover using the algorithm of Bar-Yehuda and Even (1985). Hence, dividing its result
by a factor of two results in a lower bound on the size of the MVC.
4


## Page 5


• We employ the matrix rank upper bound on the order of the maximum independent
set of Budinich (2003) to any generated subgraph.
Since the complement of any
independent set of vertices is a vertex cover, any upper bound on the maximum
independent set size corresponds to a lower bound on the MVC size.
• We use the easy to compute minimum degree bound of (Willis, 2011, page 20).
(ii) Any graph coloring provides an upper bound on the chromatic number. Since all vertices
in a maximum clique need to be assigned diﬀerent colors, the chromatic number is again
an upper bound of the clique number. This means that it gives an upper bound of the
size of the maximum independent set of the complement graph and can thus be used
as described in the previous point.
To compute a graph coloring we use the heuristic
function greedy color of the NetworkX package (Hagberg et al., 2008), which is applied to
the complement G of G.
(iii) Lastly, we compute the Lov´asz number (Lov´asz, 1979) of G if the size of G is less than or
equal to 50. If G is larger than 50 we return instead the size of G, a trivial upper bound
of the Lov´asz number. The reason for this is the excessive computation time associated
with ﬁnding the Lov´asz number, as well as practical program memory limitations with the
implementation we adapted from Stahlke (2013). The Lov´asz number is an upper bound
for the maximum independent set number of G (Gr¨otschel et al., 1988), and consequently
a lower bound on the size of the MVC of G.
We compute upper bounds on the size of the MVC as follows:
(i) At any point in the decomposition tree, the best solution found so far in G+ (the larger
subgraph of the two generated subgraphs G+ and G−) is an upper bound on the size of the
MVC. Therefore, we follow the recursive G+ branches in the decomposition ﬁrst until we
can compute the MVC on any of the generated G+ subgraphs: its MVC size then becomes
a good upper bound for all the other (smaller) generated subgraphs. We call this strategy
the decomposition bound.
(ii) The size of the MVC of G added to the clique number of G equals the size of G. Conse-
quently, any heuristic solver that ﬁnds an approximate solution of the clique number in G
can be used to compute an upper bound on the size of the MVC of G. We apply the fmc
solver (Pattabiraman et al., 2013) in heuristic mode to G, thus giving us an upper bound
on the size of the MVC of G.
The above bounds are employed during the recursion to prune those subproblems which
cannot contain vertices belonging to the MVC of the input graph.
3.2
Reduction techniques
In addition to using upper and lower bounds, we also use three reduction techniques that allow
us to ﬁgure out a partial solution to the MVC by deciding for a subset of the vertices of G
whether they belong to V ′ or not. These reduction techniques are the following:
5


## Page 6


(i) We coin the ﬁrst method neighbor based vertex removal. Essentially, we search and remove
triangles, vertices of degree 1, and vertices of degree zero in any subgraph. Since in a triangle,
any two arbitrarily chosen degree 2 triangle vertices belong to the MVC, we add a contribution
of 2 to the overall size of the MVC and remove the triangle. Analogously, vertices of degree 1
are automatically in the MVC and can be removed, along with the only neighbor of that vertex,
after adding a contribution of 1 to the current size of the MVC. Vertices of degree zero can be
removed without further processing.
(ii) Another reduction technique works on the QUBO formulation of the MVC given in (2)
instead of on the graph itself. In particular, for any subgraph produced by our algorithm we
generate the corresponding MVC Hamiltonian (2), which is then analyzed. Several general-
purpose preprocessing techniques are capable to identify binary relations or persistencies in
QUBO or Ising Hamiltonians. Persistencies determine the value of certain variables in every
global minimum (strong persistencies) or at least one global minimum (weak persistencies). In
Boros and Hammer (2002), a comprehensive overview of such techniques is given.
Suppose
variable xv for vertex v (see Section 1) is assigned the value xv = 1 in the persistency analysis:
we can then add v to the current vertex cover and remove v and its adjacent edges from the
subgraph. If xv = 0 we can remove v and its adjacent edges without further processing. We
employ the qpbo Python bindings of Rother et al. (2007) to carry out the persistency analysis.
(iii) In Akiba and Iwata (2015a), the authors state a variety of reduction techniques for
MVC that have been used in the theoretical study of exponential-complexity branch-and-reduce
algorithms. For instance, those techniques include degree-one reductions, decomposition, domi-
nance rules, unconﬁned vertex reduction, LP- and packing reductions, as well as folding-, twin-,
funnel- and desk reductions. We employ only the reduction methods from the Java package
vertex cover-master (Akiba and Iwata, 2015b). For a given input graph, vertex cover-master
returns a superset of the MVC. This means that any vertex not contained in the output of
vertex cover-master is deﬁnitely not part of the MVC and can be removed. The code can be
applied repeatedly until no further vertices are found that can be removed.
The simulations in Section 4 assess the eﬀectiveness of the aforementioned techniques.
4
Experimental results
This section presents three performance analysis experiments. In Section 4.1, we evaluate four
diﬀerent choices for the selection of the vertex v used in the algorithm of Section 2 to split any
subgraph into two smaller parts. Moreover, in Section 4.1, we separately evaluate the bounds
on the size of the MVC discussed in Section 3.1, and the reduction techniques of Section 3.2.
Based on the assessment in Section 4.1, we select the best strategy of vertex selection for
splitting, lower and upper bounds on the MVC size of the generated subgraphs, and reduction
techniques, and call the resulting method the DBR algorithm (decomposition, bounds, reduc-
tion). Section 4.2 evaluates our DBR algorithm on simulated graphs, benchmark test graphs,
and real world graphs. In Section 4.3, we make a prediction on its behaviour on future D-Wave
architectures.
6


## Page 7


Figure 2: Preprocessing time (left) and solution time (right) for diﬀerent vertex selection strate-
gies.
We compare all algorithms using two measures, the preprocessing time, as well as the solution
time. The preprocessing time is the CPU clock time our algorithm needs to decompose a problem
instance into subproblems of size 46; the time to solve the subproblems then depends on the
solver being used, and is hence not included in the preprocessing time. We deﬁne the solution
time as the sum of the preprocessing time and an additional contribution of 1.6sec*N, where
1.6 seconds is the average QPU access time for 104 anneals on D-Wave 2X, and N is the number
of leaf subgraphs generated in a decomposition run.
All ﬁgures have logarithmic scale on the y-axis.
4.1
Evaluation of vertex selection, bounding and pruning techniques for
MVC
First, we compare four diﬀerent options for the selection of the vertex v used in Section 2 to
split any subgraph into two parts during the decomposition. Those choices are the selection of
a vertex of lowest degree, of highest degree, of median degree, and a random vertex. If several
vertices exist in each category, v is chosen at random among them.
For all ﬁgures presented in this section, we employ graphs of size |V | = 80 having a graph
density d ranging from 0.1 to 0.9 in steps of 0.1.
Experimental results for the vertex choice are presented in Figure 2 and show preprocessing
time (left plot) and solution time (right plot). Selecting the highest degree vertex yields the
both the lowest preprocessing and solution time. We therefore use the highest degree vertex
selection in our implementation of the algorithm of Section 2.
Next, we test all six diﬀerent options for combining the three lower and the two upper
bounds presented in Section 3.1 (against no bounds as seventh option). Here the picture is
more complex (Figure 3). With respect to the preprocessing time, the version with ”no bounds”
is the best, and close to it are the combinations labeled ”decomposition–deterministic” (the
decomposition upper bound and the lower deterministic bound) and ”decomposition-chrome”
(the decomposition upper bound and the chromatic number lower bound). The two Lov´asz-
based combinations take the longest preprocessing times. Although they produce the lowest
number of subgraphs, they also have the highest computational cost per bound (due to the
computationally intensive computation of the Lov´asz number already pointed out in Pelofske
et al. (2019)). In Figure 3 (left) we include in the total time only the preprocessing (CPU) time
7


## Page 8


Figure 3: Preprocessing time (left) and solution time (right) for diﬀerent combinations of lower
and upper bounds.
Figure 4: Preprocessing time (left) and solution time (right) for diﬀerent reduction techniques.
needed to decompose the original graph into subgraphs of suﬃciently small sizes, but do not
include the D-Wave time for solving these subproblems. In the next experiment, we do include
that time. In Figure 3 (right), we present solution time.
There is no clear winner in Figure 3 (right). The combinations ”fmc-determ” and ”fmc-
chrome” perform best for the most diﬃcult case, at 0.1 density. From density 0.2 the two Lov´asz-
based algorithms perform the best. The combination ”fmc-deterministic” does not work well.
At density 0.8 and 0.9, the combination ”fmc-chrome” behaves similarly to the Lov´asz-based
options. Taking into account both experiments, we concluded that ”fmc-chrome” oﬀers the most
balanced performance and we use this combination in our implementation of the algorithm of
Section 2. Although the bounds based on the Lov´asz number give excellent subgraph reduction,
both the calculation of the Lov´asz number as well as our implementation becomes intractable
to use in practice above the size limit (50) we used in Figure 3.
Scaling this approach to
larger D-Wave architectures as well as larger problem graphs would be entirely impractical for
any approach involving the computation of the Lov´asz number.
Therefore, the best bound
combination in terms of scalability as well as overall solution time is the decomposition upper
bound in connection with the chromatic number lower bound. We will use this combination in
the DBR algorithm in Section 4.2.
Third, we evaluate the reduction techniques of Section 3.2, where we apply any given re-
duction technique on every subgraph generated at each level of the decomposition tree. Results
are shown in Figure 4. We observe that all three reduction techniques are capable of decreasing
the number of generated subgraphs for low densities (in comparison to using no reduction in
8


## Page 9


50
60
70
80
90
100
110
120
130
Graph Size
10
2
10
1
100
101
102
Time [s]
10
20
30
40
50
60
70
80
90
100
110
120
130
Graph Size
100
101
102
103
104
Time [s]
10
20
30
40
Figure 5:
DBR algorithm applied to random graphs with average vertex degree d
∈
{10, 20, 30, 40}. Preprocessing time (left) and solution time (right).
the decomposition algorithm), with the neighbor based vertex removal yielding the best results.
Moreover, the neighbor based vertex removal is also the fastest technique, thus making it our
choice for the DBR algorithm presented in Section 4.2.
In all experiments, one can observe that upon increasing the graph density (and thereby the
size of the edge set of G) the running time decreases, which seems counter-intuitive. This can be
explained by the speciﬁcs of our decomposition algorithm, which beneﬁts from vertices of high
degrees. In Figure 1, the larger the degree of the vertex v, the smaller the size of graph G−. This
results in decomposition trees with some very short branches for dense graphs, which in some
cases may lead to nearly linear recursions. In contrast, for sparse graphs the decomposition trees
are balanced and thus might be of exponential size.
4.2
The DBR algorithm
We use our results from Section 4.1 in order to fully specify our decomposition algorithm pre-
sented in Section 2. In particular, we employ the decomposition from Section 2 with highest
degree vertex selection at each level of the decomposition. For each generated subproblem, we
bound the size of the MVC it contains using the decomposition upper bound and the chromatic
number lower bound (see Section 3.1).
We apply the DBR algorithm to random graphs of size |V | ∈{50, 60, . . . , 130} and record
the preprocessing time as well as the solution time. Figure 5 shows results for graphs with four
ﬁxed average vertex degrees d ∈{10, 20, 30, 40}. Those results are based on the average of 10
repetitions.
Due to the logarithmic scale on the y-axis, the results suggest an exponential increase in
both subgraph count and computation time. This is to be expected as the MVC is an NP-hard
problem. As outlined above, graphs with higher average vertex degrees yield lower numbers
of generated subgraphs and thus faster computation times due to the characteristics of our
decomposition algorithm.
Apart from random graphs, we also evaluate the DBR algorithm on DIMACS benchmarks
graphs (Bader et al., 2013). Results are given in Table 1. We observe that the DBR algorithm
is capable of computing the optimal solution of MVC on such benchmark graphs in reasonable
time.
9


## Page 10


Graph name
No. vertices
No. edges
CPU time
No. subgraphs
solution time
keller5
776
225990
672.54
654
1718.94
keller4
171
9435
2.24
30
50.24
mann-a45
1035
533115
842.42
1
844.02
p-hat300-2
300
21928
172.85
4276
7014.45
p-hat300-3
300
33390
12.35
195
324.35
p-hat500-3
500
93800
115.56
425
795.56
p-hat700-3
700
183010
524.76
1380
2732.76
brock200-1
200
21928
4
104
170.4
brock200-2
200
9876
31.51
715
1175.51
brock200-3
200
12048
8.26
134
222.66
gen400-p0.9-55
400
71820
33.62
3
38.42
c-fat200-5
200
8473
41.78
131
251.38
hamming8-4
256
20864
20.28
217
367.48
Table 1: Total solution time in seconds for DIMACS benchmark graphs based on a single run.
We also evaluate the DBR algorithm on several real world graphs provided in the Network
repository (Rossi and Ahmed, 2015) in a single run. We speciﬁcally selected graphs with undi-
rected and unweighted edges, and of a size of at most a few thousand vertices.
We selected graphs from the following categories in the Network repository (listed in the
order they appear in Table 2):
1. the ﬁrst ﬁve graphs in Table 2 belong to the Brain networks category (Amunts et al.,
2013),
2. the next two graphs contain data from the Retweet networks category (Rossi et al., 2014,
2012),
3. followed by two enzyme structure graphs in the Cheminformatics category,
4. two graphs from the Web graphs category (Adamic and Glance, 2005; Gleich et al., 2004),
5. two graphs from the Collaboration networks category (Newman, 2006; De Nooy et al.,
2011),
6. two graphs from the Interaction networks category (Cohen, 2009; Opsahl and Panzarasa,
2009),
7. one graph from the Infrastructure networks category (Opsahl, 2011),
8. one graph from the Biological networks category (Duch and Arenas, 2005),
9. one graph each from the category E-mail networks and Proximity networks,
10. one graph from the Technological networks category (Spring et al., 2002),
11. and a graph from the Road networks category.
10


## Page 11


Graph name
No. vertices
No. edges
CPU time
No. subgraphs
solution time
fmc solver
bn-macaque-rhesus-interareal-
93
2700
0.25
1
1.85
0.018
cortical-network-2
bn-mouse-visual-cortex-2
193
214
0.01
1
1.61
0.104
bn-macaque-rhesus-cerebral-
91
1401
0.14
1
1.74
0.022
cortex-1
bn-macaque-rhesus-brain-2
91
582
0.01
1
1.61
0.023
bn-macaque-rhesus-brain-1
242
3054
23.31
427
706.51
NA
rt-retweet
96
117
0.05
1
1.65
0.030
rt-twitter-copen
761
1029
0.94
1
2.54
NA
ENZYMES-g296
125
141
0.17
1
1.77
NA
ENZYMES-g103
59
115
0.02
1
1.62
0.012
web-polblogs
643
2280
6.4
1
8
NA
web-edu
3031
6474
51.35
518
880.15
NA
ca-netscience
379
941
1.71
66
107.31
NA
ca-CSphd
1882
1740
6.53
1
8.13
NA
ia-enron-only
143
623
0.99
10
16.99
NA
ia-fb-messages
1266
6451
3.71
1
5.31
NA
inf-openﬂights
2939
15677
7.87
1
9.47
NA
bio-celegans
453
2025
0.38
1
1.98
NA
email-enron-only
143
623
1.12
19
31.52
NA
infect-hyper
113
2196
1.22
36
58.82
0.033
tech-routers-rf
2113
6632
5.81
1
7.41
NA
road-euroroad
1174
1417
6.34
19
36.74
NA
Table 2: Total solution time in seconds for real world graphs based on a single run. NA indicates
that no result was produced after 19 hours of wall clock runtime.
Apart from applying the DBR algorithm, we solve each graph with the fmc solver of Pat-
tabiraman et al. (2013) (since fmc ﬁnds maximum cliques, we determine the vertex cover as
those vertices not belonging to the maximum clique of the complement of G). Another way
of solving for the optimal vertex cover is to apply a linear programming solver such as Gurobi
(Gurobi Optimization, 2018) or CPLEX (IBM, 2019) to the Hamiltonian in eq. (2). However,
as shown in (Chapuis et al., 2019, Table 1) for an equivalent classical NP-complete problem,
using the fmc solver (which is tailored to graph problems) is considerably faster than employing
a general-purpose solver such as Gurobi, and we thus report results for fmc only.
Results are given in Table 2. We never observed in our simulations that the fmc solver was
able to compute the optimal vertex cover when our DBR algorithm could not. We therefore only
display graphs which could be solved by the DBR algorithm in reasonable time (sixth column
of Table 2), and indicate the solution time (or NA if fmc had not produced a result after 19
hours of wall clock runtime) for fmc in the last column. Table 2 suggests two main conclusions:
First, the fmc solver is usually only able to compute the vertex cover for graphs with relatively
few vertices. If fmc is able to compute a solution, it does so around 100 times faster than the
DBR algorithm. Second, for graphs unsolvable with fmc, our DBR algorithm is able to compute
the vertex cover in seconds or minutes, with a maximal solve time of around 15 minutes which
seems reasonable for practical applications.
4.3
Performance on future D-Wave architectures
One way of using the DBR algorithm is to perform the described decomposition until the sub-
graphs are of a size that can be solved on one of the D-Wave quantum annealers. For D-Wave
2X, the largest graph of arbitrary density that can be embedded onto the quantum processing
unit may roughly contain 46 vertices (this number varies due to manufacturing errors of the
11


## Page 12


Figure 6: DBR algorithm applied to diﬀerent D-Wave architectures with ﬁxed average graph
degrees of 160. Preprocessing time (left) and solution time (right).
chip). For D-Wave 2000Q, arbitrary graphs of roughly 65 vertices can be embedded. The next
generation of D-Wave annealers (currently named Pegasus P16) has a higher number of qubits
(5640) and a higher connectivity (40484 couplers vs. 6000 for 2000Q) than the previous D-Wave
machines, resulting in a maximum complete graph size of 180 that can be embedded onto its
quantum processor. We refer to this machine as 5000Q in this paper.
We are interested in how the performance of the DBR algorithm changes for those architec-
tures. Figure 6 shows subgraph count and runtime for the three diﬀerent architectures (D-Wave
2X, 2000Q, and 5000Q) as a function of the graph size, while we ﬁxed the average degree at
160 in all generated graphs. All results are averages over 10 repetitions. The ﬁgure shows that
D-Wave 2X and 2000Q have a very similar behavior, which is to be expected as both use the
same low qubit-connectivity architectures (D-Wave, 2016), leading to very similar sizes of the
largest embeddable graph on the qubit chip (roughly 46 vs. 65 vertices) despite the roughly 1000
and 2000 nominal qubits, respectively. In contrast, the considerably larger embeddable graph
size on the next generation Pegasus architecture leads to a signiﬁcantly better scaling behavior
of our algorithm.
5
Discussion
This article proposed a novel decomposition algorithm for the MVC problem. The algorithm
recursively splits a given MVC instance into smaller subproblems until, at some recursion level,
the generated subproblems can be solved with any method of choice, including a quantum
annealer. The algorithm is exact, meaning that the optimal solution of MVC is guaranteed
given all subproblems can be solved exactly. If subproblems are solved probabilistically (with
error probability of at most ϵ), then this guarantee carries over to an error of at most ϵ for the
overall solution returned by our algorithm.
Several pruning and reduction techniques were investigated in order to reduce the number of
generated subproblems during the recursion. Our simulation study (a) evaluates possible choices
for vertex selection, bounds and reduction techniques for our DBR algorithm and (b) evaluates
the DBR algorithm on random and DIMACS graphs as well as on larger D-Wave architectures.
We summarize our ﬁndings as follows:
1. Selecting the highest degree vertex at each recursion level to split each graph further is
12


## Page 13


both fastest in terms of preprocessing time as well as overall solution time. The combi-
nation of decomposition upper bound and chromatic number lower bound yields the best
trade-oﬀbetween speed and reduction power. Reduction methods seem to only have an
impact at low graph densities which, however, are the most interesting one since they are
the hardest cases for our decomposition algorithm, and here the neighbor based vertex
removal performs best. We call the algorithm that uses the aforementioned choices in
the decomposition approach of Section 2 the DBR (decomposition, bounds, reduction)
algorithm.
2. The DBR algorithm has good predictable scaling behavior on random graphs of ﬁxed vertex
degree. DIMACS benchmark graphs (with as many as thousand vertices and hundreds
of thousands of edges), as well as real world graphs from the Network repository (with
thousands of vertices and more than ten thousand edges), can be solved exactly with DBR
in reasonable time.
3. One main application of DBR is to split vertex cover instances until they can be solved
on D-Wave. The similar architectures of D-Wave 2X and 2000Q exhibit worse scaling
behavior than the next generation D-Wave Pegasus P16, which has a much higher qubit
connectivity in addition to a higher qubit number.
Future work could include the investigation of further techniques to bound, reduce and prune
subproblems as well as an improved implementation of the DBR algorithm. In particular, if
it was possible to calculate the Lov´asz number for large graphs in an eﬃcient manner, using
the Lov´asz lower bound for MVC could greatly improve the capabilities of our decomposition
algorithm for solving large MVC problems on D-Wave.
References
Adamic, L. A. and Glance, N. (2005). The political blogosphere and the 2004 us election: divided
they blog. In Proceedings of the 3rd international workshop on Link discovery, pages 36–43.
ACM.
Akiba, T. and Iwata, Y. (2015a). Branch-and-reduce exponential/fpt algorithms in practice:
A case study of vertex cover. 2015 Proceedings of the Seventeenth Workshop on Algorithm
Engineering and Experiments (ALENEX), pages 1–12.
Akiba, T. and Iwata, Y. (2015b). Vertex cover solver. https://github.com/wata-orz/vertex_
cover.
Amunts, K., Lepage, C., Borgeat, L., Mohlberg, H., Dickscheid, T., Rousseau, M.-´E., Bludau,
S., Bazin, P.-L., Lewis, L. B., Oros-Peusquens, A.-M., Shah, N. J., Lippert, T., Zilles, K.,
and Evans, A. C. (2013). Bigbrain: An ultrahigh-resolution 3d human brain model. Science,
340(6139):1472–1475.
Bader, D. A., Meyerhenke, H., Sanders, P., and Wagner, D. (2013). Graph Partitioning and
Graph Clustering. 10th DIMACS Implementation Challenge Workshop February 13-14, 2012.
Contemp Math, 588.
13


## Page 14


Balasubramanian, R., Fellows, M., and Raman, V. (1998). An improved ﬁxed parameter algo-
rithm for vertex cover. Information Processing Letters, pages 163–168.
Bar-Yehuda, R. and Even, S. (1985). A local-ratio theorem for approximating the weighted
vertex cover problem. Annals of Discrete Mathematics, 25:27–46.
Boros, E. and Hammer, P. (2002). Pseudo-boolean optimization. Discrete Appl Math, 123(1–
3):155–225.
Budinich, M. (2003). Exact bounds on the order of the maximum clique of a graph. Discrete
Applied Mathematics, 127(3):535–543.
Chapuis, G., Djidjev, H., Hahn, G., and Rizk, G. (2017). Finding Maximum Cliques on the
D-Wave Quantum Annealer. Proceedings of the 2017 ACM International Conference on Com-
puting Frontiers (CF’17), pages 1–8.
Chapuis, G., Djidjev, H., Hahn, G., and Rizk, G. (2019). Finding Maximum Cliques on the
D-Wave Quantum Annealer. Journal of Signal Processing Systems, 91(3-4):363–377.
Chen, J., Kanj, I., and Jia, W. (2001). Vertex cover: further observations and further improve-
ments. Journal of Algorithms, 41:280–301.
Chen, J., Kanj, I., and Xia, G. (2010). Improved upper bounds for vertex cover. Theoretical
Computer Science, 411:3736–3756.
Chen, J., Liu, L., and Jia, W. (2000). Improvement on vertex cover for low degree graphs.
Networks, 35:253–259.
Cohen, W. (2009). Enron email dataset. https://www.cs.cmu.edu/~./enron/. Accessed in
2009.
Courcelle, B., Makowsky, J., and Rotics, U. (2000). Linear time solvable optimization problems
on graphs of bounded clique-width. Theor Comput Syst, 33(2):125–150.
D-Wave (2016). Technical Description of the D-Wave Quantum Processing Unit. D-Wave.
De Nooy, W., Mrvar, A., and Batagelj, V. (2011). Exploratory social network analysis with
Pajek, volume 27. Cambridge University Press.
DIMACS (2000). Workshop on faster exact algorithms for np-hard problems. Princeton, NJ.
Djidjev, H., Chapuis, G., Hahn, G., and Rizk, G. (2016). Eﬃcient Combinatorial Optimization
Using Quantum Annealing. LA-UR-16-27928. arXiv:1801.08653.
Downey, R. and Fellows, M. (1992). Fixed-parameter tractability and completeness. Congressus
Numerantium, 87:161–187.
Duch, J. and Arenas, A. (2005). Community identiﬁcation using extremal optimization phys.
Rev. E, 72:027104.
14


## Page 15


Giakoumakis, V. and Vanherpe, J. (1997). On extended P4-reducible and extended P4-sparse
graphs. Theoret Comput Sci, 180:269–286.
Gleich, D., Zhukov, L., and Berkhin, P. (2004). Fast parallel pagerank: A linear system approach.
Yahoo! Research Technical Report YRL-2004-038, 13:22.
Gr¨otschel, M., Lov´asz, L., and Schrijver, A. (1988). Geometric Algorithms and Combinatorial
Optimization, volume 2 of Algorithms and Combinatorics. Springer.
Gurobi Optimization, L. (2018). Gurobi optimizer reference manual.
Hagberg, A., Schult, D., and Swart, P. (2008). Exploring network structure, dynamics, and
function using NetworkX. Proceedings of SciPy2008, pages 11–15.
IBM (2019). IBM ILOG CPLEX Optimization Studio.
Johnson, D. and (Eds.), M. T. (1996). Cliques, Coloring and Satisﬁability, Second DIMACS
Implementation Challenges.
Lov´asz, L. (1979). On the Shannon Capacity of a Graph. IEEE Trans Inf Theory, IT-25(1):1–7.
Lucas, A. (2014). Ising formulations of many NP problems. Front Phys, 2(5):1–27.
Newman, M. E. (2006). Finding community structure in networks using the eigenvectors of
matrices. Physical review E, 74(3):036104.
Niedermeier, R. and Rossmanith, P. (2003). On eﬃcient ﬁxed-parameter algorithms for weighted
vertex cover. Journal of Algorithms, 47:63–77.
Niedermeier, R. and Rossmanith, P. (2007). Upper bounds for vertex cover further improved.
In Proceedings of the 16th Symposium on Theoretical Aspects of Computer Science (STACS).
Opsahl, T. (2011). Why anchorage is not (that) important: Binary ties and sample selection.
Opsahl, T. and Panzarasa, P. (2009).
Clustering in weighted networks.
Social networks,
31(2):155–163.
Pattabiraman, B., Patwary, M. M. A., Gebremedhin, A. H., Liao, W.-k., and Choudhary, A.
(2013). Fast algorithms for the maximum clique problem on massive sparse graphs. In Bonato,
A., Mitzenmacher, M., and Pra lat, P., editors, Algorithms and Models for the Web Graph,
pages 156–169, Cham. Springer International Publishing.
Pelofske, E., Hahn, G., and Djidjev, H. (2019). Solving large maximum clique problems on a
quantum annealer. LA-UR-18-30973. arXiv:1901.07657.
Rao, M. (2008). Solving some NP-complete problems using split decomposition. Discrete Appl
Math, 156(14):2768–2780.
Rossi, R. A. and Ahmed, N. K. (2015). The network data repository with interactive graph
analytics and visualization. In Proceedings of the Twenty-Ninth AAAI Conference on Artiﬁcial
Intelligence.
15


## Page 16


Rossi, R. A., Gleich, D. F., Gebremedhin, A. H., and Patwary, M. A. (2012). What if clique
were fast? maximum cliques in information networks and strong components in temporal
networks. arXiv:1210.5802, pages 1–11.
Rossi, R. A., Gleich, D. F., Gebremedhin, A. H., and Patwary, M. A. (2014). Fast maximum
clique algorithms for large graphs. In Proceedings of the 23rd International Conference on
World Wide Web (WWW).
Rother, C., Kolmogorov, V., Lempitsky, V., and Szummer, M. (2007). Optimizing binary mrfs
via extended roof duality.
Spring, N., Mahajan, R., and Wetherall, D. (2002). Measuring ISP topologies with rocketfuel.
In SIGCOMM, volume 32, pages 133–145.
Stahlke, D. (2013). Python code to compute the Lovasz, Schrijver, and Szegedy numbers for
graphs. https://gist.github.com/dstahlke/6895643.
Stege, U. and Fellows, M. (1999). An improved ﬁxed-parameter-tractable algorithm for vertex
cover.
Tarjan, R. (1985). Decomposition by clique separators. Discrete Math, 55(2):221–232.
Willis, W. (2011). Bounds for the independence number of a graph. Master’s thesis, Virginia
Commonwealth University. https://scholarscompass.vcu.edu/etd/2575.
Woeginger, G. (2008). Open problems around exact algorithms. Discrete Applied Mathematics,
156(3):397–405.
Xu, H., Kumar, T., and Koenig, S. (2016). A new solver for the minimum weighted vertex
cover problem. In: Quimper CG. (eds) Integration of AI and OR Techniques in Constraint
Programming. CPAIOR 2016. Lecture Notes in Computer Science, vol 9676. Springer, Cham.
16

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
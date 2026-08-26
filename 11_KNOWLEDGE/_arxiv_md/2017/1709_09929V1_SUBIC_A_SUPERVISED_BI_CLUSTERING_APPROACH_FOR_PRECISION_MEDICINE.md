---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1709.09929v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1709.09929v1_SUBIC__A_Supervised_Bi-Clustering_Approach_for_Precision_Medicine

> Source: 1709.09929v1_SUBIC__A_Supervised_Bi-Clustering_Approach_for_Precision_Medicine.pdf

> Pages: 8

---


## Page 1


ACCEPTED MANUSCRIPT IN IEEE INTERNATIONAL CONFERENCE ON MACHINE LEARNING AND APPLICATIONS (ICMLA 2017)
SUBIC: A Supervised Bi-Clustering Approach for
Precision Medicine
Milad Zafar Nezhada, Dongxiao Zhub,∗, Najibesadat Sadatia, Kai Yanga, Phillip Levyc
Department of Industrial and Systems Engineering, Wayne State Universitya
Department of Computer Science, Wayne State Universityb
Department of Emergency Medicine and Cardiovascular Research Institute, Medical School, Wayne State Universityc
Corresponding author∗, E-mail addresses: dzhu@wayne.edu
Abstract—Traditional
medicine
typically
applies
one-size-
ﬁts-all treatment for the entire patient population whereas
precision medicine develops tailored treatment schemes for
different patient subgroups. The fact that some factors may
be more signiﬁcant for a speciﬁc patient subgroup motivates
clinicians and medical researchers to develop new approaches
to subgroup detection and analysis, which is an effective
strategy to personalize treatment. In this study, we propose
a novel patient subgroup detection method, called Supervised
Biclustring (SUBIC) using convex optimization and apply our
approach to detect patient subgroups and prioritize risk factors
for hypertension (HTN) in a vulnerable demographic subgroup
(African-American).
Our
approach
not
only
ﬁnds
patient
subgroups with guidance of a clinically relevant target variable
but also identiﬁes and prioritizes risk factors by pursuing
sparsity of the input variables and encouraging similarity
among the input variables and between the input and target
variables.
Keywords—Precision medicine; subgroup identiﬁcation, biclus-
tering, regularized regression, cardiovascular disease.
I. INTRODUCTION
The explosive increase of Electronic Medical Records
(EMR) and emerge of precision (personalized) medicine in
recent years holds a great promise for greatly improving
quality of healthcare [8]. In fact, the paradigm in medicine and
healthcare is transferring from disease-centered (empirical) to
patient-centered, the latter is called Personalized Medicine.
The extensive and rich patient-centered data enables data
scientists and medical researchers to carry out their research in
the ﬁeld of personalized medicine [40]. Personalized medicine
is deﬁned as [43]: “use of combined knowledge (genetic or
otherwise) about an individual to predict disease susceptibility,
disease prognosis, or treatment response and thereby improve
that individual health.” In other words, the goal of personalized
medicine is to provide the right treatment policy to the right
patient at the right time.
A crucial step in personalized medicine is to discover the
most important input variables (disease risk factors) related to
each patient [17]. Since identiﬁcation of risk factors needs
multi-disciplinary knowledge including data science tools,
statistics techniques and medical knowledge, many machine
learning and data mining methods have been proposed to
identify, select and prioritize risk factors [2][46][44]. Some
popular methods such as linear model with shrinkage [53] and
random forest [10] effectively select signiﬁcant risk factors for
the entire patient population. However, these approaches are
not capable of detecting risk factors for each patient subgroup
because they are developed based on an assumption that the
patient population is homogeneous with a common set of risk
factors.
While the point of input variable selection is well taken, the
association with small subgroups, a key notion in personal-
ized medicine, is often neglected. As mentioned, personalized
healthcare aims to identify subgroup of patients who are simi-
lar with each other according to both target variables and input
variables. Discovering potential subgroups plays a signiﬁcant
role in designing personalized treatment schemes for each
subgroup. Therefore, it is essential to develop a core systematic
approach for patient subgroup detection based on both input
and target variables [24]. A number of data-driven approaches
have been developed for subgroup identiﬁcation. The more
popular methods can be divided in two categories: 1) Tree-
based approaches [20] (or so called recursive partitioning),
and 2) Biclustering approaches [41]. Tree based methods in
subgroup analysis are greatly developed in recent years, such
as Model-based recursive partitioning [59], Interaction Trees
[49], Simultaneous Threshold Interaction Modeling Algorithm
(STIMA) [21], Subgroup Identiﬁcation based on Differential
Effect Search (SIDES) [36], Virtual Twins [25], Qualitative
Interaction Tree (QUINT) [22] and Subgroup Detection Tree
[35]. The second approaches (Biclustering) have been exten-
sively developed and applied to analyze gene expression data.
Most of the biclustering algorithms developed up-to-date are
based on optimization procedures as the search heuristics to
ﬁnd the subgroup of genes or patients.
Tree-based methods detect patient subgroups using the rela-
tionship between input and target variables whereas bicluster-
ing methods just focus on clustering rows and columns of the
input variables simultaneously to identify different subgroups
arXiv:1709.09929v1  [cs.LG]  26 Sep 2017


## Page 2


with speciﬁc risk factors (prioritized input variables). The
former employs a target variable to guide subgroup detection
by selecting a common set of input variables. The latter selects
subgroup of speciﬁc input variables without guidance of a
target variable. Moreover, both approaches are heuristic in
nature that subgroup detection and risk factor identiﬁcation
are sensitive to choices of data sets and initializations hence
has a poor generalization performance. Our proposed method
combines the strength of the both approaches by using a
target variable to guide the subgroup detection and selecting
subgroup of speciﬁc risk factors. Meanwhile, our systematic
approach overcomes the stability limitation of both approaches
by casting the problem into a stable and mature convex
optimization framework. Figure 1 demonstrates consecutive
steps of our approach:
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Define the weights based on 
similarity among input 
variables (Unsupervised 
weights) 
Performance evaluation 
based on different tuning 
parameters 
Solve the Sparse Convex 
Optimization problem to find 
Biclusters 
Define the convex objective 
function with appropriate 
penalty term. 
Define the similarity weights 
(supervised and 
Unsupervised) 
Define the weights based on 
guidance of response 
variable (Supervised 
weights) 
Cleaning and Preprocessing 
of Input Data 
Fig. 1: The consecutive steps of
our approach
In this study, we propose a new supervised biclustering ap-
proach, called SUBIC, for solving patient subgroup detection
problem. Our approach is the generalized (supervised) version
of convex biclustering [16], which enables prediction of target
variables for new input variables. Moreover, we employ the
elastic-net penalty [61] (both l1 and l2 regularization terms)
that encourages sparsity of the correlated input variable groups
(X) with the guidance of a target value (Y ). Our model is
speciﬁcally designed for patient subgroup detection and target
variable prediction from high dimension data. To the best of
our knowledge, our model is the ﬁrst supervised biclustering
approach that can be applied in many domains such as person-
alized medicine. To demonstrate the performance of SUBIC
approach, we apply it to detect subgroups among hypertension
(HTN) patients with guidance of left ventricular mass indexed
to body surface area (LVMI), a clinically important target
variable.
The rest of this paper is organized as follows. Section II
reviews the related works in unsupervised biclustering ap-
proaches. Section III explains our proposed supervised biclus-
tering (SUBIC) approach. Section IV describes experimental
studies and model evaluation using simulation studies. Section
V reports the results of application of our method on patient at
the high risk of cardiovascular disease, and ﬁnally we conclude
this study in Section VI.
II. RELATED WORKS
Biclustering is deﬁned as simultaneous clustering of both
rows and columns in the input data matrix. Such clusters are
important since they not only discover the correlated rows, but
also identify the group of rows that do not behave similarly
in all columns [23]. In the context of precision medicine,
rows correspond to patients and columns correspond to input
variables measured in each patient. Biclustering was originally
introduced in 1972 [28], and Cheng and Church [15] were
the ﬁrst to develop a biclustering algorithm and applied it to
gene expression data analysis. There exist a wide range of
biclustering methods developed using different mathematical
and algorithmic approaches. Tanay et al. [51] proved that bi-
clustering is a NP-hard problem, and much more complicated
than clustering problem [19]. Therefore, most of methods are
developed based on heuristic optimization procedures [41].
Madeira and Oliveira [38], Busygin et al. [12], Eren et al. [23]
and Pontes et al. [41] provided four comprehensive reviews
about biclustering methods in 2004, 2008, 2012 and 2015
respectively. Based on the most recent review [41], biclustering
approaches can be divided in two main groups. The ﬁrst one
refers to methods based on evaluation measures, which means
some heuristic methods are developed using a measure of qual-
ity to reduce the solution space and complexity of biclustering
problem. Table I demonstrates different algorithmic categories
within this group:
TABLE I: Biclustering methods based on evaluation measure.
Algorithm
Description
Prosperous Methods
Iterative
greedy
search
These methods follow a greedy
strategy to ﬁnd an approxi-
mate solution. They improve
the measure of evaluation in
each step and construct a set of
objects from the smallest pos-
sible solution space recursively
or iteratively.
Direct Clustering [28], Cheng
and Church [15], HARP Algo-
rithm [58], Maximum Similarity
Bicluster[37]
Stochastic
iterative
greedy
search
These methods use a stochastic
strategy by adding a random
variable to the iterative greedy
search in order to speed up the
biclustering algorithm.
Flexible Overlapped Bicluster-
ing [55], Random Walk Biclus-
tering [3], Reactive GRASP Bi-
clustering [18], Pattern-Driven
Neighborhood Search[4]
Nature-
inspired
meta-
heuristics
These methods are developed
based
on
a
nature-inspired
meta-heuristic, such as sim-
ulated annealing, ants colony
and swarm optimization.
Simulated-Annealing
Biclustering [11], Evolutionary
Algorithms for Biclustering [7],
SEBI(Sequential
Evolutionary
Biclustering)
[19],
Multi-
objective-Evolutionary
Algorithms for Biclustering[39],
Bicluster
Ensemble
using
Mutual Information [1]
Clustering-
based
approach
These methods carry out their
search
based
on
traditional
clustering methods in one di-
mension and then use an addi-
tional approach to cluster sec-
ond dimension.
Possibilistic-Spectral
Biclustering. [13], Biclustering
with
SVD
and
Hierarchical
Clustering.[56]
The second group of approaches is called non metric-
based biclustering methods that do not use any measure
of quality (evaluation measure) for guiding the search.


## Page 3


These methods use graph-based or probabilistic algorithms
to identify the patterns of biclusters in data matrix. Table
II summarizes different algorithms of non metric-based group:
TABLE II: Biclustering methods based on non-metric.
Algorithm
Description
Prosperous Methods
Graph-
based
approaches
These methods are developed
based on the graph theory.
They
use
nodes
for
either
genes, samples or both gene
and sample representations, or
refer to nodes as representing
the whole biclusters.
Statistical-Algorithmic Method
for
Bicluster
Analysis
(SAMBA)[51],
Qualitative-
Biclustering
algorithm
(QUBIC)[34],
Pattern-based
Co-Regulated
Biclustering
(CoBi) [45], MicroCluster [60]
One-way
clustering-
based
approaches
These methods are developed
based on the same concept of
clustering-based
approached,
but
they
do
not
use
any
measure of quality in their
search path.
Coupled
Two-way
Clustering
[26],
Interrelated
Two-way
Clustering [52]
Probabilistic
search
These methods are created us-
ing statistical modeling and
probability theory.
Plaid Models [58], Rich Prob-
abilistic
Models
[47],
Gibbs
Sampling [48], Bayesian Biclus-
tering Model [27]
Linear alge-
bra
These methods use linear al-
gebra to apply linear map-
ping between vector spaces
for describing and identifying
the most correlated submatri-
ces from the original dataset.
Spectral Biclustering [32], Iter-
ative Signature Algorithm [6],
Non-smooth Non-negative Ma-
trix Factorization (nsNMF) [14]
Optimal
reordering
rows
and
columns
These methods are based on
the strategy of performing per-
mutations of the original rows
and columns in the data matrix,
to achieve a better arrangement
and make biclusters.
Pattern-based Biclustering [30],
Order-Preserving-Sub-Matrices
(OPSMs)[5]
One of the important aspects of bicluster structure is
overlapping, which means several biclusters share rows and
columns with each other. Because of the characteristic of
search strategy in biclustering methods, overlapping may or
may not be allowed among the biclusters. Most of the algo-
rithms mentioned in Table I and Table II allow overlapping
biclusters [41]. Since these algorithms use heuristic approach
for guiding search, ﬁnal biclusters may vary depending on how
the algorithm is initialized. Therefore, they don’t guarantee
a global optimum nor are they robust against even small
perturbations [16].
Recently, Chi et al. [16] formulated biclustering problem as
a convex optimization problem and solved it with an iterative
algorithm. Their convex biclustering model corresponds to
checkerboard mean model, which means each data matrix
component is assigned to one bicluster. They used the concept
of fused lasso [54] and generalized it with a new sparsity
penalty term corresponding to the problem of convex biclus-
tering. This method has some important advantages over the
previous heuristic-based methods, that is, it created a unique
global minimizer for biclustering problem, which maps data
to one biclustering structure, therefore the solution is stable
and unique. Also it used a single tuning parameter to con-
trol the number of biclusters. Authors performed simulation
studies to compare their algorithm with two other biclustering
algorithms, dynamic tree cutting algorithm [33] and sparse
biclustering algorithm [50], which assume the checkerboard
mean structure. Results showed that convex biclustering out-
performs the competing approaches in terms of Rand Index
[16].
Despite the improved performance, the convex biclustering
method, like other biclustering methods, does not exploit a tar-
get variable on subgroup detection and risk factor selection. As
a result, the detected biclusters do not link to target variables
of interest. Hence, it is unable to predict the target variable
for future input variables. Clearly, the target variable such as
LVMI provides a critical guidance for detection and selection
of the meaningful biclusters (patient subgroups). Moreover,
the l1 penalty term alone in convex biclustering encourages
the sparsity of individual input variables but overlooks the
fact that they are also correlated within variable groups.
To overcome both limitations, we introduce a new elastic-
net regularization term that seeks sparsity of the correlated
variable groups and employs a target variable to supervise the
biclustering optimization process. Consequently, our model is
truly a predictive model that is capable of predicting value of
the target variable for new patients. In the next section, we
describe our method in detail.
III. METHOD
A. The object function of the SUBIC method
Let’s assume that the input data matrix Xn×p represents
n instances with different p input variables and Yn is the
continuous target variable (e.g. LVMI), corresponds to nth
instance (patients). According to the checkerboard mean struc-
ture, we assume R and C are the sets of rows and columns
of the bicluster B respectively, and xi,j refers to elements
belong to the bicluster B, the observed value of xi,j can
be deﬁned as [16]: xi,j = µ0 + µRC + εi,j, where µ0 is a
baseline mean for all elements, µRC is the mean of bicluster
corresponds to R and C, and εi,j refers to error that is i.i.d
with N(0, σ). With considering non-overlapping biclusters,
this structure corresponds to a checkerboard mean model [32].
Without loss of generality, we ignore µ0 from all elements. The
goal of biclustering is to ﬁnd the partition indices with regard
to R and C then estimate the mean of each corresponding
bicluster (B). To achieve this goal, we minimize the following
convex objective function:
Fλ1,λ2 = 1
2 ∥X −T∥2
F + P(T),
(1)
where matrix T ∈Rn×p includes our optimization parameters,
which are the estimate of means matrix. The ﬁrst term is
frobenius norm of matrix X −T refers to error term and
P(T) = P1(T) + P2(T) is the elastic-net regularization
penalty term formulated as follows:
P1(T) = λ1[Σi<jwi,j∥T.i −T.j∥2
2 + Σi<jhi,j∥Ti. −Tj.∥2
2],
(2)
and
P2(T) = λ2[Σi<jwi,j∥T.i −T.j∥1 + Σi<jhi,j∥Ti. −Tj.∥1].
(3)
It is clear that this objective function is similar to subset
selection problem in regularized regression [53]. In the penalty
function λ1 and λ2 are tunning parameters. The ﬁrst term


## Page 4


penalized by λ1 is a l2-norm regularization term and the
second term penalized by λ2 is a l1-norm regularization term.
Therefore the penalty term P(T) acts as regression elastic-net
penalty [61]. Ti. and T.i refer to ith row and column of matrix
T, which can be considered as a cluster center (centroid) of
ith row and column respectively. By minimizing the objective
function deﬁned in Eq.1 with sparsity based regularization,
the cluster centroids are shrunk together when the tunning
parameters increase. It means that sparse optimization tries to
unify the similar rows and columns to speciﬁc centroid simul-
taneously. Finding the similarity between rows and columns is
guided by different weights (wi,j, hi,j), which are included in
objective function. These weights has been deﬁned based on
distance between input variables (X.i −X.j and Xi. −Xj.),
distance between target variables (Yi −Yj) and correlation
between input variables and target variable (X.i, Y.j). There-
fore both input variables and target variable play signiﬁcant
rule in guiding of sparsity to ﬁnd the best centroids. The ﬁrst
kind of weights (wi,j) proceeds the columns convergence and
the second one (hi,j) proceeds the rows convergence. The
weights are constructed from un-supervised and supervised
parts, where:
wi,j = w1
i,j + w2
i,j
and
hi,j = h1
i,j + h2
i,j.
(4)
The unsupervised part (w1
i,j, h1
i,j) attempts to converge rows
(columns) based on the similarity exists among input vari-
ables, and the supervised part (w2
i,j, h2
i,j) converges rows
and columns according to the similarity of input and target
variables. Since the rows and columns are in Rn and Rp spaces
respectively, it is required to normalize the weights (recom-
mended the sum of row weights and column weights to be
1
√n
and
1
√p respectively). We used the idea of sparse Gaussian
kernel weights [16] for deﬁning w1
i,j, w2
i,j, h1
i,j, h2
i,j. Table III
demonstrates the mathematical description of weights:
TABLE III: Description of the weights formula.
#
Weight Formula
1
w1
i,j = lk
i,j exp(−ϕ∥X.i−X.j ∥2
2)
∗This weight is to converge the similar columns in terms
of distance similarity measure. lk
i,j is 1 when jth column
is among the k-nearest neighbor of ith column, otherwise
it is zero. Therefore it guarantees the weights are sparse.
(0 ≤ϕ ≤1)
2
w2
i,j = lk
i,j exp(−ϕ|corr(x.i,Y )−corr(x.j ,Y )|)
∗This weight is the supervised part of wi,j, the goal is
to converge the columns that have similar correlation with target
variable. It means that the features which behave similarly with
target variable should be converged. In our model we used
Pearson correlation that assumes a linear relationship between
input variable and target variables. (0 ≤ϕ ≤1)
3
h1
i,j = lk
i,j exp(−ϕ∥Xi.−Xj.∥2
2)
∗This weight is the same as w1
i,j, which attempts to converge the
similar rows with lower distance from each other.(0 ≤ϕ ≤1)
4
h2
i,j = lk
i,j exp
(−ϕ
q
|(Yi−Yj)|)
∗This weight is supervised part of hi,j, and it converges
the rows that are similar in term of target variable value. This
weight considers the role of target variable in clustering of
similar rows.(0 ≤ϕ ≤1)
The way to deﬁne the weights has a substantial impact
on the quality of biclustering. The weights described above
guarantee the sparsity of the problem and employ the similarity
of all input and target variables in supervised and unsupervised
manner. According to deﬁned weights, the two columns (rows)
that are more similar with each other will get larger weight in
the convex penalty function, therefore in minimization process,
those columns (rows) should be in higher priority, and it means
that convex minimizer attempts to cluster the similar columns
(rows). The choice of elastic-net penalty term can overcome
the lasso limitations. While the l1-norm can generates a sparse
model, the quadratic part of the penalty term encourages
grouping effect and stabilizes the l1-norm regularization path.
Also the elastic-net regularization term would be very suitable
for high dimension data with correlated input variables [61].
B. The algorithm to train the SUBIC model
It can be proved easily that the objective function in Eq.1 is
a convex function. Therefore we need to develop appropriate
algorithm to solve this unconstrained convex optimization.
Since the second part of penalty function, P2(T) is undif-
ferentiated we use Split Bregman method [57] developed for
large-scale Fused Lasso. It can be shown that this method
is equivalent to the alternating direction method of multi-
pliers (ADMM) [9]. Readers can refer to Split Bregman
method [57] or ADMM algorithm [9] for more comprehensive
explanation. According to both methods we need to use
splitting variable and Lagrangian multiplier and then apply
augmented Lagrangian for undifferentiated part (P2(T)) of
objective function. First we need to transform our problem
to the equality-constrained convex optimization problem by
deﬁning two new variables (V ,S) and adding two constraints
correspond to P2(T) and then use Lagrangian multipliers:
min
Fλ1,λ2 = 1
2 ∥X −T∥2
F + λ1[Σi<jwi,j∥T.i −T.j∥2
2+
Σi<jhi,j∥Ti. −Tj.∥2
2] + λ2[Σi<jwi,j∥T.i −T.j∥1+
Σi<jhi,j∥Ti. −Tj.∥1],
subject to : wi,j(T.i −T.j) = Vi,j
∀i, j; i < j,
hi,j(Ti. −Tj.) = Si,j
∀i, j; i < j,
(5)
where V and S are matrices in Rn×p. Assuming the differenti-
ated part of objective function in (1) is F
′
λ1,λ2, the Lagrangian
Multiplier for the above problem is:
˜L(T, M, N, V, S) = F
′
λ1,λ2 + λ2[Σi<jwi,j∥Vi,j∥1 + Σi<jhi,j∥Si,j∥1]+
Σi<j ⟨Mi,j, wi,j(T.i −T.j) −Vi,j⟩+ Σi<j ⟨Ni,j, hi,j(Ti. −Tj.) −Si,j⟩,
(6)
where M and N are the vectors of dual variables (Lagrangian
Multipliers) corresponding with each constraints in Eq.5 (to-
tally there are
 n
2

+
 p
2

constraints). Finally the Augmented


## Page 5


Lagrangian function of Eq.5 is as following:
L(T, M, N, V, S) = F
′
λ1,λ2 + λ2[Σi<jwi,j∥Vi,j∥1 + Σi<jhi,j∥Si,j∥1]+
Σi<j ⟨Mi,j, wi,j(T.i −T.j) −Vi,j⟩+ Σi<j ⟨Ni,j, hi,j(Ti. −Tj.) −Si,j⟩+
µ1
2 [Σi<j∥wi,j(T.i −T.j) −Vi,j∥2
2] + µ2
2 [Σi<j∥hi,j(Ti. −Tj.) −Si,j∥2
2],
(7)
where µ1
>
0 and µ2
>
0 are two parameters. The
Split Bregman algorithm for supervised convex biclustering
problem described below:
Algorithm 1 Split Bregman algorithm for Training the SUBIC
model
1: Initialize T 0, V 0,S0, M 0, N0
2: repeat
3:
T k+1 = argminT
1
2 ∥X −T ∥2
F + λ1[Σi<jwi,j∥T.i −T.j∥2
2+
Σi<jhi,j∥Ti. −Tj.∥2
2] + Σi<j
D
M k
i,j, wi,j(T.i −T.j) −V k
i,j
E
+
Σi<j
D
N k
i,j, hi,j(Ti. −Tj.) −Sk
i,j
E
+ µ1
2 [Σi<j∥wi,j(T.i −T.j)
−V k
i,j∥2
2] + µ2
2 [Σi<j∥hi,j(Ti. −Tj.) −Sk
i,j∥2
2]
4:
V k+1
i,j
= τ λ2
µ1
(wi,j(T k+1
.i
−T k+1
.j
) + µ−1
1
M k
i,j)
i < j
5:
Sk+1
i,j
= τ λ2
µ2
(hi,j(T k+1
i.
−T k+1
j.
) + µ−1
2
Nk
i,j)
i < j
6:
M k+1
i,j
= M k
i,j+δ1(wi,j(T k+1
.i
−T k+1
.j
)−V k+1
i,j
)
i < j; 0 < δ1 ≤µ1
7:
Nk+1
i,j
= Nk
i,j + δ2(hi,j(T k+1
i.
−T k+1
j.
) −Sk+1
i,j )
i < j; 0 < δ2 ≤µ2
8: until
9: Convergence
τ acts as a soft thresholding operator deﬁned on vector space
and satisfying the following equation:
τλ(w) = [tλ(w1), tλ(w2), ...]T ,
where:
tλ(wi) = sgn(wi)max{0, |wi −λ|}.
(8)
C. The SUBIC based prediction approach
For prediction of the target variable based on supervised
biclustering framework, we introduce a simple yet effective
approach based generalized additive model (GAM) [29]. As-
suming that K biclusters {BC1,BC2,..., BCK } are detected
by training the SUBIC model, we consider K classiﬁers
corresponding to each biclusters, i.e., fk(y|xbck, xnew) = ybck.
It means that each classiﬁer predicts the target value as an
average of the target variables of the corresponding bicluster.
The proposed GAM model is as follows:
g(E(y)) = R1(xbc1) + R2(xbc2) + ... + Rk(xbck),
where
Rk(xbck) = qkfk(y|xbc, xnew).
(9)
qk is deﬁned as normalized weight based on posterior prob-
abilities. Assuming that each bicluster follows a Gaussian
distribution as N(µi, σ) and P(bck|xnew) is the posterior
probability which refers to the probability of each bicluster
given a new instance , we can deﬁne qk as below:
qk =
P(bck|xnew)
Pk
i=1 P(bci|xnew)
,
where:
P(bck|xnew) = P(xnew|bck) × P(bck).
(10)
P(xnew|bck) is conveniently calculated based on Gaussian
distribution assuming equal variance and zero covariance and
P(bck) is the prior that can be calculated by counting the
number of instances in each bicluster.
IV. EXPERIMENTAL STUDY AND MODEL EVALUATION
For assessing the performance of our approach, we carry out
simulation studies and use Rand Index (RI) [42] and Adjusted
rand index (ARI) [31] as two popular measures for evaluating
the quality of clustering. Since our biclustering method is
supervised, we simulate data for input and target variables
based on a checkerboard mean structure. We used normal
distribution with different means to generate simulated data.
Figure 2 illustrates an example simulation study.
As shown below, data was simulated in 20 × 20 matrix.
Data in each segment has different size and were created based
on a different normal distribution, all sections are generated
with low-noisy data (σ = 1.5). Input data in segments (2,
3, 4 and 5) are in high positive correlation with the target
variable and input data in segment (6, 7, 8 and 9) are in high
negative correlation with the target variable. Segments 1 and
10 in general, are similar with very low correlation with target
variable. Segments 1 and 3 of the target variable are positive
and the other two sections have negative values.
According to this assumptions and consider the effect of
target variable, it is clear that the true number of biclusters
should be 16 (not 10). It means that segments 1 and 10 include
4 biclusters within each. The results of SUBIC implementation
for different tuning parameters are displayed in Figure 3.
Design of simulated data 
Input Variables (X) 
 
 
 
 
 
 
 
 
 
 
(Y) 
1- N (-5,1.5) 
 
(20×4) 
2- N (-1.5,1.5) 
 
(6×6) 
6- N (4.5,1.5) 
 
(6×4) 
10- N (3,1.5) 
 
(20×4) 
1- N (15, 3) 
3- N (1.5,1.5) 
 
(4×6) 
7- N (-4.5,1.5) 
 
(4×4) 
2- N (-10, 3) 
4- N (-1.5,1.5) 
 
(6×6) 
8- N (4.5,1.5) 
 
(6×4) 
3- N (20, 3) 
5- N (1.5,1.5) 
 
(4×6) 
9- N (-4.5,1.5) 
 
(4×4) 
4- N (-15, 3) 
Heatmap of simulated input data (X) and response variable (Y) 
Input Variables (X) 
 
 
 
 
 
 
 
 
 
 
(Y) 
 
 
 
 
 
Fig. 2: The chessboard structure and the simulated data (top and down panel).
As depicted in Figure 3, tuning parameters provide a ﬂexible
mechanism to analyze data with both high and low variances.


## Page 6


𝐼𝑛𝑝𝑢𝑡𝑒 𝐷𝑎𝑡𝑎 
𝜆1 = 100, 𝜆2 = 50 
𝜆1 = 1000, 𝜆2 = 500 
 
 
𝜆1 = 500, 𝜆2 = 1000 
𝜆1 = 1000, 𝜆2 = 1000 
𝜆1 = 10000, 𝜆2 = 10000 
 
 
 
Fig. 3: Results of SUBIC method implementation on the simulated data
It is obvious that by increasing λ1 and λ2, rows and columns
are uniﬁed to mean in each bicluster but when λ1 and λ2 get
larger values such as 10000, bicluster patterns are “smoothed
out” and the number of biclusters reduces.
We consider different scenarios in Figure 4 to show that the
ﬂexibility and generalization of our method. Panel a shows
our supervised biclustering approach, SUBIC, with elastic-net
penalty (l1 and l2) as the most general case. By zeroing out λ1,
the l2 penalty (special case 1), SUBIC becomes the extended
(supervised) version of the convex biclustering approach [16]
(Panel b). If we instead zero out the supervised weight
components w2
i,j and h2
i,j (special case 2), SUBIC becomes
extended unsupervised convex biclsutering with elastic-net
penalty (Panel c). Finally, if we zero out both the l2 penalty
and the supervised weight components w2
i,j and h2
i,j (special
case 3), SUBIC becomes the bona ﬁde convex biclustering
method reported in [16].
𝑎) 𝜆1 = 1000, 𝜆2 = 1000, 𝑤𝑖,𝑗
2 ≠ ℎ𝑖,𝑗
2 ≠0 
SUBIC with Elastic-net penalty term 
𝑏) 𝜆1 = 0, 𝜆2 = 1000, 𝑤𝑖,𝑗
2 ≠ ℎ𝑖,𝑗
2 ≠0 
Supervised version of the Convex biclustering 
 
𝑐) 𝜆1 = 1000, 𝜆2 = 1000, 𝑤𝑖,𝑗
2 = ℎ𝑖,𝑗
2 = 0 
Convex biclustering via Elastic-net 
𝑑) 𝜆1 = 0, 𝜆2 = 1000, 𝑤𝑖,𝑗
2 = ℎ𝑖,𝑗
2 = 0 
Convex Biclustering (chi et al.) 
 
 
Fig. 4: Different scenarios which show the ﬂexibility of SUBIC method
Therefore, our SUBIC approach is sufﬁciently general and
ﬂexible that employs a target value to guide the subgroup
detection by encouraging sparsity of the number of variable
groups and variables within each group. Correspondingly, our
SUBIC approach most accurately detect the biclusters given
in the ground truth. Panel a and b in Figure 4 conﬁrm
that the impact of supervised weights (target value guidance)
in identifying of true biclusters in comparison with convex
biclustering approach [16] (Panels c and d). Also in both
cases the elastic-net regularization appears more accurate in
detecting true biclusters.
We extend the above simulation idea to 80 × 80 matrix and
consider different design (true biclusters) with two variance
levels (low and high) for assessment the performance of our
model. We use different tuning parameters in each design
and evaluate SUBIC method in terms of rand index and
adjusted rand index. The results of average RI and ARI over
10 replicates are displayed in Table IV and V for low-variance
and high-variance data respectively.
TABLE IV: RI and ARI for different designs with low noisy simulated data
Design
σ
λ1 = λ2 = 102
λ1 = λ2 = 103
λ1 = λ2 = 104
RI
ARI
RI
ARI
RI
ARI
2 × 4
1.5
0.85
0.71
0.99
0.96
0.79
0.65
4 × 4
1.5
0.79
0.62
0.98
0.95
0.76
0.64
4 × 8
1.5
0.73
0.56
0.98
0.97
0.68
0.59
8 × 8
1.5
0.82
0.69
0.96
0.93
0.72
0.61
TABLE V: RI and ARI for different designs with high noisy simulated data
Design
σ
λ1 = λ2 = 102
λ1 = λ2 = 103
λ1 = λ2 = 104
RI
ARI
RI
ARI
RI
ARI
2 × 4
3
0.65
0.53
0.90
0.88
0.99
0.96
4 × 4
3
0.68
0.58
0.85
0.81
0.99
0.97
4 × 8
3
0.59
0.49
0.93
0.90
0.98
0.93
8 × 8
3
0.55
0.43
0.87
0.82
0.99
0.95
As shown above, the performance of SUBIC is fully tunable
using the pair of tuning parameters in response to data with
different levels of variances. From Table IV and V, it is clear
that SUBIC’s superior performance is very stable for both low
and high variance data. In particular, the robust performance
against high-variance data is achieved by setting larger values
of tuning parameters.


## Page 7


V. APPLICATION IN PERSONALIZED MEDICINE
In this section we demonstrate how SUBIC method is
capable of identifying patient subgroups with guidance of the
target variable LVMI. We study the population of African-
Americans with hypertension and poor blood pressure control
who have high risk of cardiovascular disease.
Data are obtained from patients enrolled in the emergency
department of Detroit Receiving Hospital. After preprocessing
step, our data consists of 107 features including demographic
characteristics, previous medical history, patient medical con-
dition, laboratory test result, and CMR results related to 90
patients. To achieve a checkerboard pattern, we reorder rows
and columns (original data) at ﬁrst [16] using hierarchical clus-
tering and then apply SUBIC method. The results are shown
in the top panel of Figure 5. In addition, we implemented
convex biclustering method (COBRA) developed by Chi et
al. [16] using package “cvxbiclustr” in R for comparing with
our SUBIC method. Results obtain ed using different tuning
parameters (λ) are shown in the bottom panel of Figure 5.
Fig. 5: Results of SUBIC implementation (top panel) and COBRA method
(bottom panel) on the data related to African-American patients at- high
risk of cardiovascular disease.
In Figure 5, our SUBIC method detects 4 subgroups using
15 features for λ1 = λ2 = 104. These 15 features belong to 3
major groups of features including: 1) Waist Circumference
Levels (mm); 2) Average Weight (kg) and 3) Calculated
BMI. The statistics related to these risk factors based on 4
groups of patients is summarized in Table VI. It is worth
mentioning that other potential risk factors such as “Troponin
Level” or “Plasma Aldosterone” can be also signiﬁcant but
these three groups of features are sufﬁcient to describe the
disparity among patients based on guidance of the target
variable LVMI. On the contrary, COBRA method fails to
ﬁnd any patient subgroups for this data set based on different
tuning parameters.
TABLE VI: Average of three disparity factors and LVMI (along with standard
deviation) for subgroups detected by SUBIC
Subgroup
size
Waist Circumference (mm)
Average Weight (kg)
Calculated BMI
LVMI
A
24
1248.8 (104.7)
125.1 (13.2 )
41.6 (5.2)
85.7 (11.9)
B
28
1092.6 (74.5)
99.7 (11.1)
35.1 (3.8)
82.7 (13.7)
C
29
972.8 (89.6)
84.8 (10.2)
30.1 (4.9)
80.9 (13.7)
D
9
813.3 (123.7)
64.4 (10.6)
23.8 (4.3)
79.3 (11.8)
Total
90
1067.7 (163.5)
98.2 (22.2)
34.1 (7.2)
82.6 (12.9)
VI. DISCUSSION AND CONCLUSION
In this paper, we have developed a novel supervised sub-
group detection method called SUBIC based on convex op-
timization. SUBIC is a predictive model that combines the
strength of biclustering and tree-based methods. We introduced
a new elastic-net penalty term in our model and deﬁned
two new weights in our objective function to enable the
supervised training under the guidance of a clinically relevant
target variable in detecting biclusters. We further presented
a generalized additive model for predicting target variables
for new patients. We evaluated our SUBIC approach using
simulation studies and applied our approach to identify dis-
parities among African-American patients who are at high risk
of cardiovascular disease. Future directions include extending
our SUBIC approach to predict categorical target variables,
such as stages and subtypes of heart diseases.
REFERENCES
[1] Geeta Aggarwal and Neelima Gupta. Bemi bicluster ensemble using
mutual information. In Machine Learning and Applications (ICMLA),
2013 12th International Conference on, volume 1, pages 321–324. IEEE,
2013.
[2] Celestine Aguwa, Mohammad Hessam Olya, and Leslie Monplaisir.
Modeling of fuzzy-based voice of customer for business decision an-
alytics. Knowledge-Based Systems, 125:136–145, 2017.
[3] Fabrizio Angiulli, Eugenio Cesario, and Clara Pizzuti. Random walk
biclustering for microarray data.
Information Sciences, 178(6):1479–
1497, 2008.
[4] Wassim Ayadi, Mourad Elloumi, and Jin-Kao Hao. Pattern-driven neigh-
borhood search for biclustering of microarray data. BMC bioinformatics,
13(7):S11, 2012.
[5] Amir Ben-Dor, Benny Chor, Richard Karp, and Zohar Yakhini. Dis-
covering local structure in gene expression data: the order-preserving
submatrix problem. Journal of computational biology, 10(3-4):373–384,
2003.
[6] Sven Bergmann, Jan Ihmels, and Naama Barkai.
Iterative signature
algorithm for the analysis of large-scale gene expression data. Physical
review E, 67(3):031902, 2003.
[7] Stefan Bleuler, Amela Prelic, and Eckart Zitzler.
An ea framework
for biclustering of gene expression data. In Evolutionary Computation,
2004. CEC2004. Congress on, volume 1, pages 166–173. IEEE, 2004.
[8] Mario Bochicchio, Alfredo Cuzzocrea, and Lucia Vaira.
A big data
analytics framework for supporting multidimensional mining over big
healthcare data. In Machine Learning and Applications (ICMLA), 2016
15th IEEE International Conference on, pages 508–513. IEEE, 2016.
[9] Stephen Boyd, Neal Parikh, Eric Chu, Borja Peleato, and Jonathan
Eckstein.
Distributed optimization and statistical learning via the
alternating direction method of multipliers. Foundations and Trends R⃝
in Machine Learning, 3(1):1–122, 2011.
[10] Leo Breiman. Random forests. Machine learning, 45(1):5–32, 2001.
[11] Kenneth Bryan, P´adraig Cunningham, and Nadia Bolshakova. Applica-
tion of simulated annealing to the biclustering of gene expression data.
IEEE transactions on information technology in biomedicine, 10(3):519–
525, 2006.
[12] Stanislav Busygin, Oleg Prokopyev, and Panos M Pardalos. Biclustering
in data mining. Computers & Operations Research, 35(9):2964–2987,
2008.
[13] Carlos Cano, L Adarve, J L´opez, and Armando Blanco. Possibilistic
approach for biclustering microarray data. Computers in biology and
medicine, 37(10):1426–1436, 2007.


## Page 8


[14] Pedro Carmona-Saez, Roberto D Pascual-Marqui, Francisco Tirado,
Jose M Carazo, and Alberto Pascual-Montano.
Biclustering of gene
expression data by non-smooth non-negative matrix factorization. BMC
bioinformatics, 7(1):78, 2006.
[15] Yizong Cheng and George M Church. Biclustering of expression data.
In Ismb, volume 8, pages 93–103, 2000.
[16] Eric C Chi, Genevera I Allen, and Richard G Baraniuk.
Convex
biclustering. Biometrics, 2016.
[17] Kun Deng, Russ Greiner, and Susan Murphy. Budgeted learning for
developing personalized treatment.
In Machine Learning and Appli-
cations (ICMLA), 2014 13th International Conference on, pages 7–14.
IEEE, 2014.
[18] Smitha Dharan and Achuthsankar S Nair. Biclustering of gene expres-
sion data using reactive greedy randomized adaptive search procedure.
BMC bioinformatics, 10(1):S27, 2009.
[19] Federico Divina and Jesus S Aguilar-Ruiz. Biclustering of expression
data with evolutionary computation. IEEE transactions on knowledge
and data engineering, 18(5):590–602, 2006.
[20] LL Doove, Elise Dusseldorp, Katrijn Van Deun, and Iven Van Mechelen.
A comparison of ﬁve recursive partitioning methods to ﬁnd person
subgroups involved in meaningful treatment–subgroup interactions. Ad-
vances in Data Analysis and Classiﬁcation, 8(4):403–425, 2014.
[21] Elise Dusseldorp, Claudio Conversano, and Bart Jan Van Os. Combining
an additive and tree-based regression model simultaneously: Stima.
Journal of Computational and Graphical Statistics, 19(3):514–530,
2010.
[22] Elise Dusseldorp and Iven Van Mechelen. Qualitative interaction trees:
a tool to identify qualitative treatment–subgroup interactions. Statistics
in medicine, 33(2):219–237, 2014.
[23] Kemal Eren, Mehmet Deveci, Onur K¨uc¸¨uktunc¸, and ¨Umit V C¸ ataly¨urek.
A comparative analysis of biclustering algorithms for gene expression
data. Brieﬁngs in bioinformatics, 14(3):279–292, 2013.
[24] Ailin Fan et al. New statistical methods for precision medicine: Variable
selection for optimal dynamic treatment regimes and subgroup detection.
2016.
[25] Jared C Foster, Jeremy MG Taylor, and Stephen J Ruberg. Subgroup
identiﬁcation from randomized clinical trial data. Statistics in medicine,
30(24):2867–2880, 2011.
[26] Gad Getz, Erel Levine, and Eytan Domany. Coupled two-way clustering
analysis of gene microarray data. Proceedings of the National Academy
of Sciences, 97(22):12079–12084, 2000.
[27] Jiajun Gu and Jun S Liu. Bayesian biclustering of gene expression data.
BMC genomics, 9(1):S4, 2008.
[28] John A Hartigan. Direct clustering of a data matrix. Journal of the
american statistical association, 67(337):123–129, 1972.
[29] Trevor J Hastie and Robert J Tibshirani. Generalized additive models,
volume 43. CRC press, 1990.
[30] Rui Henriques and Sara C Madeira. Bicpam: Pattern-based biclustering
for biomedical data analysis. Algorithms for Molecular Biology, 9(1):27,
2014.
[31] Lawrence Hubert and Phipps Arabie. Comparing partitions. Journal of
classiﬁcation, 2(1):193–218, 1985.
[32] Yuval Kluger, Ronen Basri, Joseph T Chang, and Mark Gerstein. Spec-
tral biclustering of microarray data: coclustering genes and conditions.
Genome research, 13(4):703–716, 2003.
[33] Peter Langfelder, Bin Zhang, and Steve Horvath.
Deﬁning clusters
from a hierarchical cluster tree: the dynamic tree cut package for r.
Bioinformatics, 24(5):719–720, 2008.
[34] Guojun Li, Qin Ma, Haibao Tang, Andrew H Paterson, and Ying
Xu.
Qubic: a qualitative biclustering algorithm for analyses of gene
expression data. Nucleic acids research, page gkp491, 2009.
[35] Xiangrui Li, Dongxiao Zhu, Ming Dong, Milad Zafar Nezhad, Alexander
Janke, and Phillip Levy.
Sdt: A tree method for detecting patient
subgroups with personalized risk factors.
In Submmit on Clinical
Research Informatics, AMIA Conference, March 2017.
[36] Ilya Lipkovich, Alex Dmitrienko, Jonathan Denne, and Gregory Enas.
Subgroup identiﬁcation based on differential effect searcha recursive
partitioning method for establishing response to treatment in patient
subpopulations. Statistics in medicine, 30(21):2601–2621, 2011.
[37] Xiaowen Liu and Lusheng Wang. Computing the maximum similarity
bi-clusters of gene expression data. Bioinformatics, 23(1):50–56, 2007.
[38] Sara C Madeira and Arlindo L Oliveira.
Biclustering algorithms
for biological data analysis: a survey.
IEEE/ACM Transactions on
Computational Biology and Bioinformatics (TCBB), 1(1):24–45, 2004.
[39] Sushmita Mitra and Haider Banka. Multi-objective evolutionary biclus-
tering of gene expression data. Pattern Recognition, 39(12):2464–2477,
2006.
[40] Milad Zafar Nezhad, Dongxiao Zhu, Xiangrui Li, Kai Yang, and Phillip
Levy. Safs: A deep feature selection approach for precision medicine.
In Bioinformatics and Biomedicine (BIBM), 2016 IEEE International
Conference on, pages 501–506. IEEE, 2016.
[41] Beatriz Pontes, Ra´ul Gir´aldez, and Jes´us S Aguilar-Ruiz. Biclustering on
expression data: A review. Journal of biomedical informatics, 57:163–
180, 2015.
[42] William M Rand.
Objective criteria for the evaluation of clustering
methods. Journal of the American Statistical association, 66(336):846–
850, 1971.
[43] W Ken Redekop and Deirdre Mladsi.
The faces of personalized
medicine: a framework for understanding its meaning and scope. Value
in Health, 16(6):S4–S9, 2013.
[44] Javad Roostaei and Yongli Zhang. Spatially explicit life cycle assess-
ment: opportunities and challenges of wastewater-based algal biofuels
in the united states. Algal Research, 24:395–402, 2017.
[45] Swarup Roy, Dhruba K Bhattacharyya, and Jugal K Kalita.
Cobi:
pattern based co-regulated biclustering of gene expression data. Pattern
Recognition Letters, 34(14):1669–1678, 2013.
[46] Najibesadat Sadati, Ratna Babu Chinnam, and Milad Zafar Nezhad.
Observational data-driven modeling and optimization of manufacturing
processes. arXiv preprint arXiv:1705.06014, 2017.
[47] Eran Segal, Ben Taskar, Audrey Gasch, Nir Friedman, and Daphne
Koller. Rich probabilistic models for gene expression. Bioinformatics,
17(suppl 1):S243–S252, 2001.
[48] Qizheng Sheng, Yves Moreau, and Bart De Moor. Biclustering microar-
ray data by gibbs sampling. Bioinformatics, 19(suppl 2):ii196–ii205,
2003.
[49] Xiaogang Su, Tianni Zhou, Xin Yan, Juanjuan Fan, and Song Yang.
Interaction trees with censored survival data. The International Journal
of Biostatistics, 4(1), 2008.
[50] Kean Ming Tan and Daniela M Witten. Sparse biclustering of trans-
posable data.
Journal of Computational and Graphical Statistics,
23(4):985–1008, 2014.
[51] Amos Tanay, Roded Sharan, and Ron Shamir. Discovering statistically
signiﬁcant biclusters in gene expression data. Bioinformatics, 18(suppl
1):S136–S144, 2002.
[52] Chun Tang and Aidong Zhang. Interrelated two-way clustering and its
application on gene expression data. International Journal on Artiﬁcial
Intelligence Tools, 14(04):577–597, 2005.
[53] Robert Tibshirani.
Regression shrinkage and selection via the lasso.
Journal of the Royal Statistical Society. Series B (Methodological), pages
267–288, 1996.
[54] Robert Tibshirani, Michael Saunders, Saharon Rosset, Ji Zhu, and Keith
Knight. Sparsity and smoothness via the fused lasso. Journal of the
Royal Statistical Society: Series B (Statistical Methodology), 67(1):91–
108, 2005.
[55] Jiong Yang, Haixun Wang, Wei Wang, and Philip S Yu. An improved
biclustering method for analyzing gene expression proﬁles. International
Journal on Artiﬁcial Intelligence Tools, 14(05):771–789, 2005.
[56] Wen-Hui Yang, Dao-Qing Dai, and Hong Yan.
Finding correlated
biclusters from gene expression data. IEEE Transactions on Knowledge
and Data Engineering, 23(4):568–584, 2011.
[57] Gui-Bo Ye and Xiaohui Xie.
Split bregman method for large scale
fused lasso.
Computational Statistics & Data Analysis, 55(4):1552–
1569, 2011.
[58] Kevin Y Yip, David W Cheung, and Michael K Ng. Harp: A practical
projected clustering algorithm. IEEE Transactions on knowledge and
data engineering, 16(11):1387–1397, 2004.
[59] Achim Zeileis, Torsten Hothorn, and Kurt Hornik. Model-based recur-
sive partitioning. Journal of Computational and Graphical Statistics,
17(2):492–514, 2008.
[60] Lizhuang Zhao and Mohammed J Zaki. Microcluster: efﬁcient determin-
istic biclustering of microarray data. IEEE Intelligent Systems, 20(6):40–
49, 2005.
[61] Hui Zou and Trevor Hastie. Regularization and variable selection via the
elastic net. Journal of the Royal Statistical Society: Series B (Statistical
Methodology), 67(2):301–320, 2005.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1709_09929v1_subic_a_supervised_bi_clustering_approach_for_precision_medicine
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1709_09929V1_SUBIC_A_SUPERVISED_BI_CLUSTERING_APPROACH_FOR_PRECISION_MEDICINE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

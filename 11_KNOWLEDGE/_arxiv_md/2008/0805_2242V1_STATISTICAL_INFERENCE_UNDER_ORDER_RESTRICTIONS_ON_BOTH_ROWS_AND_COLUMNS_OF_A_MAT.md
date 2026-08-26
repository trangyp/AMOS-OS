---
canon-group: reference
rscf-state: source-claim
arxiv_id: 0805.2242v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 0805.2242v1_Statistical_inference_under_order_restrictions_on_both_rows_and_columns_of_a_mat

> Source: 0805.2242v1_Statistical_inference_under_order_restrictions_on_both_rows_and_columns_of_a_mat.pdf

> Pages: 16

---


## Page 1


arXiv:0805.2242v1  [math.ST]  15 May 2008
IMS Collections
Beyond Parametrics in Interdisciplinary Research: Festschrift in Honor of Professor
Pranab K. Sen
Vol. 1 (2008) 62–77
In the Public Domain
DOI: 10.1214/193940307000000059
Statistical inference under order
restrictions on both rows and columns of a
matrix, with an application in toxicology
Eric Teoh∗1, Abraham Nyska2, Uri Wormser3
and Shyamal D. Peddada†4
Insurance Institute for Highway Safety, Tel Aviv University,
The Hebrew University of Jerusalem and NIEHS
Abstract: We present a general methodology for performing statistical infer-
ence on the components of a real-valued matrix parameter for which rows and
columns are subject to order restrictions. The proposed estimation procedure
is based on an iterative algorithm developed by Dykstra and Robertson (1982)
for simple order restriction on rows and columns of a matrix. For any order re-
strictions on rows and columns of a matrix, suﬃcient conditions are derived for
the algorithm to converge in a single application of row and column operations.
The new algorithm is applicable to a broad collection of order restrictions. In
practice, it is easy to design a study such that the suﬃcient conditions derived
in this paper are satisﬁed. For instance, the suﬃcient conditions are satisﬁed
in a balanced design. Using the estimation procedure developed in this article,
a bootstrap test for order restrictions on rows and columns of a matrix is pro-
posed. Computer simulations for ordinal data were performed to compare the
proposed test with some existing test procedures in terms of size and power.
The new methodology is illustrated by applying it to a set of ordinal data
obtained from a toxicological study.
1. Introduction
In many applications the parameter of interest θ can be expressed as elements of a
real-valued I × J matrix such that the elements within rows and/or columns of the
matrix are subject to inequality restrictions called order restrictions. Researchers
are often interested in drawing statistical inferences on such parameters subject to
a variety of order restrictions. For a parameter vector η = (η1, η2, . . . , ηp)′, some
commonly encountered order restrictions are; simple order, where η1 ≤η2 ≤· · · ≤
∗This work was done while the author was a summer intern at the National Institute of En-
vironmental Health Sciences (NIEHS) and a graduate student in the Department of Biostatistics,
University of North Carolina, Chapel Hill, NC, USA.
†Supported by the Intramural Research Program of the NIH, National Institute of Environ-
mental Health Sciences.
1Insurance Institute for Highway Safety, Arlington, Virginia, USA, e-mail: eteoh@iihs.org
2Toxicologic Pathologist, Tel Aviv University, Tel Aviv, Israel, e-mail: anyska@bezeqint.net
3Department of Pharmacology, School of Pharmacy, Faculty of Medicine, Institute of Life
Sciences, The Hebrew University of Jerusalem, Jerusalem, Israel, e-mail: wormser@cc.huji.ac.il
4Biostatistics
Branch,
NIEHS,
Research
Triangle
Park,
NC,
USA,
e-mail:
peddada@niehs.nih.gov
AMS 2000 subject classiﬁcations: Primary 62F10; secondary 62G09, 62G10.
Keywords and phrases: linked parameters, matrix partial order, maximally-linked subgraph,
order-restriction, ordinal data, simple order, simple tree order, umbrella order.
62


## Page 2


Order restrictions on rows and columns of a matrix
63
Table 1
For each response variable, the data structure of the experiment in Wormser et al. [26]
Sample
Level of skin injury
Genotype
size
Unremarkable
Minimal
Mild
Moderate
Marked
Cox-2 deﬁcient
10
n1,1
n1,2
n1,3
n1,4
n1,5
Wild type
10
n2,1
n2,2
n2,3
n2,4
n2,5
Cox-1 deﬁcient
10
n3,1
n3,2
n3,3
n3,4
n3,5
ηp, umbrella order, where η1 ≤η2 ≤· · · ηi ≥ηi+1 ≥· · · ≥ηp and simple tree order,
where η1 ≤ηi, for all 2 ≤i ≤p.
Recently Wormser et al. [26] conducted an experiment to evaluate the diﬀer-
ences among three diﬀerent genotypes of mice, namely, the wild type (WT), the
cyclooxygenase-1 deﬁcient (COX-1-d) and the cyclooxygenase-2 deﬁcient (COX-2-
d) mice, when they were exposed to sulfur mustard (also known as mustard gas).
Depending upon the severity of injury to skin, each animal was categorized into
one of ﬁve ordered categories, namely, “unremarkable”, “minimal”, “mild”, “mod-
erate”, and “marked” (details in Section 5). In this experiment, a sample of n = 10
animals from each genotype was exposed to sulfur mustard. Let ni,j, i = 1, 2, 3,
j = 1, 2, . . . , 5, denote the number of animals in the ith genotype that belong to
jth response category, with E(ni,j) = nπi,j. Then the parameters of interest are
the cumulative probabilities θi,j = Pj
k=1 πi,k, i = 1, 2, 3, j = 1, 2, 3, 4. Note that
θi,5 = 1, i = 1, 2, 3. Table 1 summarizes the type of data obtained in Wormser et
al. [26]. Clearly, the rows of θ satisfy a simple order as they represent cumulative
probabilities. According to Wormser et al. [26], COX-2 deﬁciency has a protective
eﬀect against inﬂammatory processes while COX-1 deﬁciency has a negative eﬀect.
Consequently, each column of θ is also subject to simple order restriction. Thus in
this example the rows as well as columns of θ are subject to simple order restriction.
The above type of matrix order restrictions commonly arise in a variety contexts
such as the analysis of ordinal data (cf. Agresti and Coull [1], Grove [9], Nair [16]
and Wang [25]), survival analysis (Praestgaard [19]), Phase I clinical trials involving
“cocktail” of treatments (Conaway et al. [6]) and analysis of time-course and dose-
response gene expression microarray studies, etc.
For a given parametric family with matrix valued parameter θ ∈Θ ⊂RI×J,
where Θ is the parameter space deﬁned by order restrictions on the rows and/or
columns of θ, one may estimate θ using restricted maximum likelihood estimators
(RMLEs) and test alternative hypotheses using the likelihood ratio tests and their
modiﬁcations. Such methods have been well studied in the literature (cf. Barlow
et al. [2], Robertson et al. [21] and Silvapulle and Sen [23]). However, as seen from
Hwang and Peddada [11] and Lee [12], the RMLE is not always eﬃcient relative to
the unrestricted maximum likelihood estimator (UMLE). Also, the likelihood ratio
tests in the present context may not be computationally simple and the asymptotic
distribution under the null hypothesis may involve nuisance parameters (cf. Franck
[8], Grove [9], Robertson and Wright [20] and Wang [25]). Silvapulle [22] provided
an interesting explanation for why sometimes the RMLEs and the likelihood ratio
tests provide counter-intuitive results.
In view of the general concerns regarding RMLE and the likelihood ratio tests, in
Section 2 we introduce a computationally straightforward methodology for estimat-
ing a matrix valued parameter θ when the rows and/or columns are subject to order
restrictions. The proposed estimation procedure is based on the iterative procedure
of Dykstra and Robertson [7] and uses the method of Hwang and Peddada [11] for
general order restrictions. If the elements of the random matrix are independently


## Page 3


64
E. Teoh et al.
and normally distributed and if rows as well as columns of the matrix are subject
to simple order restriction then the proposed procedure is identical to the estimator
given in Dykstra and Robertson [7], but the two procedures may diﬀer for other
order restrictions. Using the proposed point estimators, in Section 3 we introduce
a Kolmogorov-Smirnov type test statistic and a bootstrap-based methodology for
determining signiﬁcance. The performance of the proposed test procedure is eval-
uated using computer simulations in Section 4 and in Section 5 it is illustrated by
analyzing the data in Wormser et al. [26] mentioned above. Concluding remarks
are provided in Section 6.
2. Estimation of parameters subject to order restrictions
2.1. Notations and a brief review
Throughout this paper Rp denotes the vector space of p × 1 real vectors and RI×J
denotes the vector space of I × J real matrices. Two components θi,j and θr,s of
θ ∈Θ ⊂RI×J are said to be linked if the inequality between them is known a priori.
A parameter is said to be a nodal parameter if it is linked to all IJ components of
θ ∈Θ ⊂RI×J. A subset of parameters M, formed by the components of θ ∈Θ ⊂
RI×J, is a linked subgraph if all parameters in M are linked, with at least one strict
inequality. Note that every linked subgraph represents a simple order-restriction
and conversely, every simple order is a linked subgraph. A linked subgraph M is
said to be maximally linked if for any linked subgraph N, M ⊂N =⇒M = N.
If a subset of parameters simultaneously satisﬁes two linked subgraphs M and
N, then we use the notation MΛN to describe the subset. As noted in Peddada
et al. [18], any order-restriction between parameters can be expressed in terms of
a collection of maximally linked subgraphs. Similarly, every parameter θi,j appears
in a ﬁnite collection of maximally linked subgraphs as a nodal parameter (within
each subgraph). Such maximally linked subgraphs are said to be associated with
θi,j.
If the rows of θ are subject to order restriction R ⊂RI and the columns are
subject to order restriction C ⊂RJ then we shall denote the joint order restriction
by RΛC ⊂RI×J.
The notation RΛRJ would indicate order restrictions R on the rows and no order
restrictions on the columns of θ. Similarly, the notation RIΛC would indicate order
restrictions C on the columns and no order restrictions on the rows of θ.
It is important to emphasize that in this article we only consider linked subgraphs
which are subsets of rows or which are subsets of columns of the parameter θ. Thus
we are not considering inequalities between arbitrary linear or non-linear functions
of the elements of θ.
Example 2.1 (Umbrella order restriction on the rows of θ). Suppose the ele-
ments of each row of θ are subject to an umbrella order with peak in the sth
column. That is, the components of the ith row of θ satisfy the inequalities θi,1 ≤
θi,2 ≤· · · ≤θi,s ≥θi,s+1 ≥· · · ≥θi,J, i = 1, 2, . . ., I. Then in this case the
parameters of the ith row can be expressed in terms of two maximally linked
subgraphs, namely, Mi,1:s = {(θi,1, θi,2, . . . θi,s) | θi,1 ≤θi,2 ≤· · · ≤θi,s} and
Mi,s:J = {(θi,s, θi,s+1, . . . , θi,J) | θi,s ≥θi,s+1 ≥· · · ≥θi,J}. Thus, the subset of
parameters in the ith row of θ, i = 1, 2, . . . , I, can be expressed as Mi,1:sΛMi,s:J.
Further, for r ≤s, the maximally linked subgraph associated with θi,r in the ith
row, i = 1, 2, . . . , I, is Mi,1:s.


## Page 4


Order restrictions on rows and columns of a matrix
65
For a vector x = (x1, x2, . . . , xp)′ ∈Rp, a simple order operator CS
w : Rp →S is
an orthogonal projection operator onto the simple order cone S = {x ∈Rp : x1 ≤
x2 ≤· · · ≤xp} where w is a vector of positive weights and the ith component of
CS
w(x) is given by
(2.1)
(CS
w(x))i = min
s≥i max
t≤i
Ps
j=t wjxj
Ps
j=t wj
.
We shall use the terminology simple order function to describe the min-max formula
used in (2.1).
Remark 2.1. For a ﬁxed weight vector w, CS
w is a monotonic operator in the sense
that if x ≤y then CS
w(x) ≤CS
w(y), where the inequality is componentwise.
When estimating a parameter η = (η1, η2, . . . , ηp)′ subject to arbitrary order
restrictions C ⊂Rp with at least one nodal parameter, Hwang and Peddada [11]
used the simple order operator CS
w, with a suitable weight vector w, for estimating
the nodal parameters. Typically the weights are proportional to the precision (or
sometimes the sample size) of UMLE. Once a parameter is estimated, then the
corresponding UMLE is replaced by the new restricted estimator and is assigned
arbitrarily large weight B, B →∞, in all subsequent calculations. To estimate
a non-nodal parameter, identify the collection of all maximally linked subgraphs
associated with that non-nodal parameter and apply the simple order operator
CS
w on the vector corresponding to the subgraph with a suitable weight vector w.
Suitable modiﬁcations were proposed for graphs with no nodal parameters.
Example 2.2 (Umbrella order restriction). Suppose η is a parameter satisfying
the order restriction η1 ≤η2 ≤η3 ≥η4 ≥η5 with UMLE ˆη. In this case the
only nodal parameter is η3. Suppose w = (w1, w2, w3, w4, w5)′ is the weight vector
associated with ˆη. According to Hwang and Peddada [11] the estimation procedure
begins with the nodal parameter η3. For i = 1, 2, denote w(i) = wi, ˆη(i) = ˆηi and let
w(3) = w5, w(4) = w4, w(5) = w3 and ˆη(3) = ˆη5, ˆη(4) = ˆη4, ˆη(5) = ˆη3. Then η3 may be
estimated by the following simple order formula
ˆˆη3 = max
i≤5
P5
j=i w(j)ˆη(j)
P5
j=i w(j)
.
Next, the non-nodal parameters η1, η2, η4 and η5 are estimated using the maximally
linked subgraphs η1 ≤η2 ≤η3 and η3 ≥η4 ≥η5, respectively. The estimators for
the non-nodal parameters η1, η2 are simpliﬁed as follows:
ˆˆη1 = min{ˆη1, w1ˆη1 + w2ˆη2
w1 + w2
, ˆˆη3},
ˆˆη2 = min{max(w1ˆη1 + w2ˆη2
w1 + w2
, ˆη2), ˆˆη3}.
In a similar manner η4 and η5 are estimated.
Remark 2.2. For a given w, CC
w is a function of several simple order functions and
therefore CC
w is a monotonic operator. That is, for all x ≤y, CC
w(x) ≤CC
w(y), where
the inequalities are componentwise.
2.2. Estimation of matrix valued parameters
We extend the notations from the previous section to matrix valued parameters
as follows. For a matrix X ∈RI×J and a weight matrix W, we denote the matrix


## Page 5


66
E. Teoh et al.
simple order column operator by CS
W . Each column x of X is orthogonally projected
onto the simple order cone S using CS
w, where w is a suitable column vector of W.
Similarly, the matrix simple order row operator is denoted by RS
W , which, with rows
of W, projects each row vector of matrix X ∈RI×J orthogonally onto the simple
order cone S. Analogously, for arbitrary order restrictions D, we deﬁne matrix
column and row operators using Hwang and Peddada methodology by CD
W and
RD
W , respectively.
We now describe the proposed algorithm for estimating θ ∈Θ = RΛC ⊂RI×J
using an unrestricted point estimator ˆθ. We use the weight matrix WR when op-
erating on the rows of ˆθ and weight matrix WC when operating on the columns
of ˆθ.
Step 1 (An unrestricted estimator):
Obtain an unrestricted estimator ˆθ for an I × J matrix parameter θ. Note that in
most situations a user may prefer to start with the unrestricted maximum likelihood
estimator (UMLE), although it is not required.
Step 2 (Estimation under order restrictions on the columns of θ):
Apply the procedure of Hwang and Peddada [11] on each column of ˆθ to obtain
estimates for θ under the order-restriction on the columns of θ. That is, apply the
operator CC
WC on the columns of ˆθ and denote the resulting estimator by CC
WC(ˆθ).
Note that the elements of CC
WC(ˆθ) may not satisfy the order-restriction on the rows
of θ.
Step 3 (Estimation under order restrictions on the rows of θ):
Apply the operator RR
WR on the rows of CC
WC(ˆθ) and denote the resulting estimator
by (RR
WR ◦CC
WC)(ˆθ).
Step 4 (Iterate to convergence):
Repeat Steps 2 and 3 to obtain the qth iterate, (RR
WR ◦CC
WC)
q(ˆθ). Stop when some
reasonable convergence criterion is reached. Denote limq→∞(RR
WR ◦CC
WC)
q(ˆθ) as
˜θ1.
Step 5 (Final estimate):
Since RR
WR and CC
WC do not necessarily commute for all order restrictions and
weights used in the calculated weighted averages, repeat the process beginning with
within-row order restrictions followed by within-column order restrictions. That is,
compute ˜θ2 = limq→∞(CC
WC ◦RR
WR)
q(ˆθ). The ﬁnal estimate of θ ∈Θ is taken to
be
(2.2)
ˆˆθ ≡1
2(˜θ1 + ˜θ2).
Remark 2.3. In general ˜θ1 ̸= ˜θ2. To illustrate this, consider the very special case
where θ is a 2 × 2 matrix with rows and columns both subject to the simple order
restriction θ1,j ≤θ2,j, θi,1 ≤θi,2, i = 1, 2, and j = 1, 2. Consider the extreme case
where ˆθ is a symmetric matrix with ˆθ1,1 ≤ˆθ1,2 = ˆθ2,1 ≥ˆθ2,2. Further, suppose
WC = WR = 11′. Thus we have a perfectly “symmetric” problem where we may
expect ˜θ1 = ˜θ2. However, even in this rather seemingly obvious situation ˜θ1 ̸= ˜θ2,
but ˜θ1 = ˜θ′
2. Hence the composition (RR
WR ◦CC
WC) is not commutative. For this
reason, we need to invoke Step 5 in all situations.
Before we discuss the convergence of the above algorithm in Steps 4 and 5, we
consider the following example which may be instructive.


## Page 6


Order restrictions on rows and columns of a matrix
67
Example 2.3. Consider a clinical trial comparing 3 new treatments with an ex-
isting treatment using 4 dose groups per treatment group. For the jth dose of the
ith treatment, i, j = 1, 2, . . . , 4, let ˆθi,j denote the sample mean response based on
ni,j = n observations. Further, for simplicity of illustration, let ˆθi,j ∼indep N(θi,j, c),
i, j = 1, 2, 3, 4. Without loss of generality, let the ﬁrst row of θ correspond to the ex-
isting treatment. Then the order restrictions of interest are θ1,j ≤θi,j, i ≥2, j ≥1,
i.e. simple tree order within each column of θ, and θi,j1 ≤θi,j2, 1 ≤j1 ≤j2 ≤4,
i ≥1, i.e. simple order within each row of θ. We choose WC = WR = 11′, where
1 = (1, 1, 1, 1)′.
We begin with Step 2 of the algorithm. Let Y = CC
WC(ˆθ). Thus columns of Y
satisfy simple tree order. That is,
Yi,j ≥Y1,j, ∀i = 2, 3, 4,
j = 1, 2, 3, 4.
Now applying Step 3 on Y = CC
WC(ˆθ) we obtain Z = RR
WR(Y ). The rows of Z
satisfy a simple order. That is,
Zi,j1 ≥Zi,j2, ∀j1, j2 = 1, 2, 3, 4, j1 > j2, i = 1, 2, 3, 4.
We now demonstrate that the columns of Z would also satisfy the simple tree order
restriction imposed on θ. That is, for any column j we need to demonstrate that
Zi,j ≥Z1,j, for all i = 2, 3, 4. Note that for each j = 1, 2, 3, 4,
Zi,j = min
t≥j max
s≤j
Pt
k=s Yi,k
t −s + 1 , ∀i = 1, 2, 3, 4.
Since Yi,k ≥Y1,k, ∀i = 2, 3, 4,
k = 1, 2, 3, 4 and since the above simple order
function is a monotonic function it follows that for all i = 2, 3, 4 and j = 1, 2, 3, 4,
Zi,j = min
t≥j max
s≤j
Pt
k=s Yi,k
t −s + 1 ≥min
t≥j max
s≤j
Pt
k=s Y1,k
t −s + 1 = Z1,j.
Thus ˜θ1 = (RR
WR ◦CC
WC)(ˆθ). Similarly, it can be demonstrated that ˜θ2 = (CC
WC ◦
RR
WR)(ˆθ). Thus in this example the algorithm converges after one application of
column and row operations and q = 1.
As will be demonstrated formally in the following theorem, one of the reasons
for the convergence observed in the above example is that WC = WR = 11′, where
1 is a column vector of 1’s of suitable length. Or more generally, WC and WR
are each of rank 1. In many applications, researchers use a balanced design for
all dose and treatment combinations. In such situations it is appropriate to take
WC = WR = 11′.
We now discuss convergence of Steps 4 and 5 in the above algorithm in the
following theorem.
Theorem 2.1. Suppose θ ∈Θ = RΛC ⊂RI×J, with every row subject to the same
order restriction and every column subject to the same order restriction. However,
the order restriction on a row need not be same as the order restriction on a column.
Further, suppose that the weight matrices WR and WC are each of rank 1. Then
for all X ∈RI×J,
(a) CC
WC ◦(RR
WR ◦CC
WC)(X) = (RR
WR ◦CC
WC)(X) ∈Θ.
(b) RR
WR ◦(CC
WC ◦RR
WR)(X) = (CC
WC ◦RR
WR)(X) ∈Θ.


## Page 7


68
E. Teoh et al.
Thus it takes one column operation and one row operation for the algorithm de-
scribed in Steps 4 and 5 to converge.
Proof. We prove the theorem for (a) since the proof of (b) follows similarly. The
main underlying idea of the proof is that, as stated in Remark 2.2, the row and
column operators RR
WR and CC
WC are monotonic and the simple order function used
in these operators is a function of suitable weighted averages of the elements of ˆθ.
Let Y = CC
WC(X). Thus, the columns of Y satisfy the order restriction C. That
is, for each j = 1, 2, . . . , J, and any two linked parameters θi1,j and θi2,j, with
θi1,j ≤θi2,j, we have Yi1,j ≤Yi2,j. Let Z = RR
WR(Y ) = (RR
WR ◦CC
WC)(X). Thus,
the rows of Z satisfy the order restriction R.
For each j = 1, 2, . . . , J, for any two linked parameters θi1,j and θi2,j, with
θi1,j ≤θi2,j, we demonstrate that Zi1,j ≤Zi2,j.
Recall from Remark 2.2 that the operators CC
WC and RR
WR are functions of several
simple order functions of suitable weighted averages of the components of ˆθ. For a
given row i1, let L denote the set of all subsets of J = {1, 2, 3, . . ., J} such that
ˆθ with column indices in these sets are used in the construction of Zi1,j. Further,
since the order restrictions in every column is the same, the same set of column
indices are used in the construction of Zi2,j. Thus Zi1,j and Zi2,j are functions of
P
k∈K(WR)i1,kYi1,k/ P
k∈K(WR)i1,k and P
k∈K(WR)i2,kYi2,k/ P
k∈K(WR)i2,k, re-
spectively, where K ⊂L.
Since RR
WR is a monotonic operator, it is suﬃcient to prove that
(2.3)
P
k∈K(WR)i1,kYi1,k
P
k∈K(WR)i1,k
≤
P
k∈K(WR)i2,kYi2,k
P
k∈K(WR)i2,k
, for all K ∈L.
Since WR is of rank 1, we can therefore express (WR)i1,k = αi2(WR)i2,k. There-
fore
(2.4)
P
k∈K(WR)i1,kYi1,k
P
k∈K(WR)i1,k
=
P
k∈K αi2(WR)i2,kYi1,k
P
k∈K αi2(WR)i2,k
=
P
k∈K(WR)i2,kYi1,k
P
k∈K(WR)i2,k
.
But since Yi1,j ≤Yi2,j for every j = 1, 2, . . ., J, (2.4) is bounded by
P
k∈K(WR)i2,kYi2,k
P
k∈K(WR)i2,k
.
Thus, by the monotonicity of the operator RR
WR, Zi1,j ≤Zi2,j. Hence (RR
WR
◦
CC
WC)(X) ∈Θ and therefore CC
WC is a left identity of (RR
WR ◦CC
WC)(X).
Hence the proof of the theorem.
Remark 2.4. An important consequence of the above theorem is that WC and WR
need not be limited to the matrix 11′, but I×J weight matrices of the type nij = nj,
i = 1, 2, . . ., I, j = 1, 2, . . ., J, can be considered. For example, in a treatment by
dose-response study, it is not required to have equal sample sizes in all treatment
by dose combinations, but the experimenter may conduct a study with a sample
of ni for the ith treatment, as long as within each treatment the same number of
observations are collected on each dose group or vise versa.
Remark 2.5. As can be seen from the following counter example, it is encouraging
to note that the suﬃcient condition stated in the above theorem is not necessary.
Let θ be a 2 × 2 matrix with θi,1 ≤θi,2, i = 1, 2, and θ1,j ≤θ2,j, j = 1, 2. Suppose
that ˆθ1,1 ≤ˆθ1,2, ˆθ1,1 ≤ˆθ2,1 ≤ˆθ2,2, and ˆθ1,2 ≥ˆθ2,2. In this case, for any non-singular


## Page 8


Order restrictions on rows and columns of a matrix
69
weight matrices WR and WC, the iterative algorithm converges in one cycle, i.e.
one column operation followed by one row operation.
Remark 2.6. In some situations, such as in the context of ordinal data, the rows
(or columns) of the unrestricted estimator ˆθ naturally satisfy the order restriction.
In such cases, under the conditions of Theorem 2.1, we need to apply CC
WC on ˆθ (or
RR
WR) only once.
2.3. A simulation study
For an I×J matrix ˆθ whose components are independently normally distributed, we
compared the performance of the proposed order-restricted matrix estimator ˆˆθ with
the UMLE ˆθ using a simulation study. Although we considered a variety of order
restrictions, patterns of means, sample sizes and weight matrices, in this article we
provide the results of a small subset since very similar results were obtained across
all patterns.
In the simulation study reported here, E(ˆθ) = θ with θi,j = i + j, 1 ≤i ≤I,
1 ≤j < J −2, and θi,j = i −j + J + 1, 1 ≤i ≤I, j ≥J −2. Thus we have
a simple order along the columns of θ, with θi1,j ≤θi2,j, for all 1 ≤i1 ≤i2 ≤I,
j = 1, 2, . . ., J, and a tree order along the rows of θ, with θi,1 ≤θi,j, for all 1 < j ≤J
and 1 ≤i ≤I. Each of the normal variables was generated with a standard deviation
of 1 and we chose sample sizes ni,j = i, i = 1, 2, . . ., I, and j = 1, 2, . . ., J so that
Variance (ˆθi,j) = 1/i. The (i, j)th element of the weight matrix WR is given by
√
i
and the weight matrix WC = W ′
R.
Our simulation study is based on 10,000 simulation runs and the results are
summarized in Table 2. In addition to comparing the average bias of ˆˆθ with that of
ˆθ, we also computed the percentage reduction in quadratic and quartic loss due to
ˆˆθ. The reduction in loss relative to ˆθ is deﬁned as 100×(1−
PI
i=1
PJ
j=1 E(ˆˆθi,j−θi,j)δ
PI
i=1
PJ
j=1 E(ˆθi,j−θi,j)δ ),
where δ = 2 corresponds to quadratic loss and δ = 4 corresponds to quartic loss.
Observe that the proposed procedure reduces the average quadratic loss and
quartic loss substantially, without costing much in terms of bias.
3. Testing hypotheses under order restrictions
In some applications, such as in Wormser et al. [26], researchers are interested in
performing tests of hypotheses regarding the elements of each column of θ when
the rows are subject to order restrictions. The order restrictions on the rows are
not part of the hypothesis, but they are present due to the underlying probability
model or for other reasons. Thus, the hypotheses of interest are
H0 : θ1,j = θ2,j = · · · = θI,j, 1 ≤j ≤J,
Table 2
Bias and reduction in loss due to the proposed estimator ˆˆθ relative to UMLE ˆθ
I
J
Average bias
Percentage reduction relative to ˆθ
ˆˆθ
ˆθ
Quadratic loss
Quartic loss
2
5
−0.0774
0.0014
29.80
53.54
2
10
−0.0608
−0.0009
22.38
41.41
5
5
−0.0612
0.0018
28.12
55.06
5
10
−0.0324
−0.0011
22.75
45.02


## Page 9


70
E. Teoh et al.
(3.1)
Ha : (θ1,j, θ2,j, . . . , θI,j)′ ∈Λp
k=1Mk, 1 ≤j ≤J,
where Mk are maximally linked subgraphs. However, each row of θ is itself subject
to the restriction (θi,1, θi,2, . . . , θi,J)′ ∈Λq
k=1Nk, 1 ≤i ≤I, where Nk are maximally
linked subgraphs.
In other examples researchers may be interested in testing
H0 : θi,j = θi′,j′ ∀(i, j) ̸= (i′, j′), 1 ≤i, i′ ≤I, 1 ≤j, j′ ≤J,
(3.2)
Ha : θ ∈RΛC,
where C = Λp
k=1Mk and R = Λq
k=1Nk, and each Mk and Nk are suitable maximally
linked subgraphs.
In both (3.1) and (3.2) the point estimators of θ are the same, and are obtained
under the order restrictions RΛC using the methodology introduced in Section 2,
although the test statistics are diﬀerent.
For a maximally linked subgraph Mk, deﬁned by θs,k ≤θs+1,k · · · ≤θr,k, the
two parameters θs,k and θr,k, which are at the ends of the graph, are said to be
farthest linked parameters of the subgraph. Under this maximally linked subgraph
let ˆˆθs,k, ˆˆθs+1,k . . . , ˆˆθr,k denote the estimated value of the parameter (θs,k, θs+1,k, . . . ,
θr,k)′ using the methodology described in Section 2. To test the hypotheses given
in (3.1), for each maximally linked subgraph, compute the estimated diﬀerence
between the two farthest linked parameters of the subgraph and divide it by the
standard error of the diﬀerence under the null hypothesis and take the largest
over all maximally linked subgraphs. More precisely we propose the following test
statistic for testing (3.1):
(3.3)
T1 = max
Mk
ˆˆθr,k −ˆˆθs,k
ˆse(ˆθr,k −ˆθs,k)
,
where θr,k and θs,k are the farthest linked parameters in the maximally linked
subgraph Mk and the max is taken over all maximally linked subgraphs Mk.
Similarly, we may test
H0 : θi,1 = θi,2 = · · · = θi,J, 1 ≤i ≤I,
(3.4)
Ha : (θi,1, θi,2, . . . , θi,J)′ ∈Λp
k=1Nk, 1 ≤i ≤I,
using the test statistic
(3.5)
T2 = max
Nk
ˆˆθk,r −ˆˆθk,s
ˆse(ˆθk,r −ˆθk,s)
,
where θk,r and θk,s are the farthest linked parameters in the maximally linked
subgraph Nk and the max is taken over all maximally linked subgraphs Nk. Then
the hypothesis on rows and columns (3.2) may be tested using T = max{T1, T2}. In
the above expressions ˆse is computed under H0. A suitable such estimate is derived
in Section 4 for the case of ordinal data. The critical values and p-values are obtained
by the bootstrap methodology as follows. For each bootstrapped dataset, the ith
independent group is formed by taking a simple random sample (with replacement),


## Page 10


Order restrictions on rows and columns of a matrix
71
of appropriate size, from the pooled sample of all subjects across all independent
groups. In this resampling procedure, we sample the entire record of a given subject.
For each bootstrap sample we compute the test statistic T , which is denoted by
T ∗. The sampling distribution of T ∗is obtained by generating a large number
of bootstrap samples, say 10,000. Then the bootstrap p-value is computed as the
proportion of times T ∗exceeded the observed T .
4. Simulation study
We conducted a simulation study to investigate the performance of the proposed
bootstrap test based on T1 for comparing I treatment groups when the responses
are measured on J ordered categories. In a random sample of n observations on
the ith treatment, i = 1, 2, . . . , I, let Xi,j denote the frequency of responses in
the jth ordered category, j = 1, 2, . . ., J. Further, let E(Xi,j) = nπi,j and let
θi,j = Pj
k=1 πi,k denote the cumulative probabilities with θi,J = 1. Let ˆπi,j denote
the sample proportion Xi,j/n and let ˆθi,j denote the corresponding cumulative sum
of sample proportions. Thus under the multinomial model ˆθ is the UMLE of θ. Note
that the rows of ˆπ, and hence the rows of ˆθ, are independently distributed.
We performed simulations to study the size and power of T1 when testing H0
against Ha −H0, where H0 :
θ ∈Θ0 = {θ | θr,j = θs,j, 1 ≤r, s ≤I, j =
1, 2, . . . , J}
and
Ha :
θ ∈Θ = {θ | r ≤s ⇒θr,j ≤θs,j}. Ordinal data was
generated for a variety of parameter conﬁgurations (Table 3) with sample sizes of
10, 20, and 50 subjects for each independent group.
Under the null hypothesis, we estimate the standard error of (ˆθr,j −ˆθs,j) re-
quired in T1 by ˆse(ˆθr,j −ˆθs,j) =
q
2 ˜Vj, where ˜Vj = 1
n
Pj
r=1
Pj
s=1[˜πr(1 −˜πr)I(r =
s) −˜πr˜πsI(r ̸= s)], and ˜πr =
PI
i=1 Xi,r+ I√n
J
nI+I√n
, r = 1, 2, . . . , J, a pooled Bayes esti-
mator under quadratic loss and suitable Dirichlet distribution prior (Lehmann [15],
page 293). Since the usual pooled MLE can take a value of 0 or 1 with a positive
probability, we prefer the above estimator over the MLE for calculating ˜Vj.
For each conﬁguration listed in Table 3, we performed 10,000 simulations to
evaluate the size and power of T1. Critical values of T1 were determined using
10,000 bootstrap samples for each simulation run. The nominal size was set at
α = 0.05. We compared the proposed test with the order-restricted methods of
Grove [9] and Nair [16] as well as with the one-sided Kolmogorov-Smirnov test. For
simplicity, we bootstrapped the critical values of Kolmogorov-Smirnov test. Since
the procedure of Grove [9] is designed for comparing only two groups, we compared
the performance our procedure with Grove [9] for I = 2 only. Similarly, comparisons
with the one-sided Kolmogorov-Smirnov test was limited to the case I = 2 only.
Results of the simulation study are summarized graphically in Figure 1 using
scatter plots. The top three panels correspond to the type 1 errors for the three
diﬀerent sample sizes per test group, i.e., n = 10, 20, 50. The bottom three panels
correspond to the power for the corresponding sample sizes. In each panel the ver-
tical axis represents the estimated probability of rejection of null hypothesis by the
proposed critical region, while the horizontal axis represents the estimated proba-
bility of rejection of null hypothesis by the three alternative procedures. Thus the
six scatter plots represent the comparison between the proposed and each of the
three competing test procedures. The ‘+’ symbol corresponds to the comparison
between the proposed test and Grove’s test (Grove [9]), ‘#’ corresponds to compar-
ison between the proposed test and Nair’s test (Nair [16]) and ‘*’ corresponds to


## Page 11


72
E. Teoh et al.
Table 3
Multinomial parameter conﬁgurations used in the simulation study
Group 1
Group 2
Group 3
π11 π12 π13 π14 π15 π21 π22 π23 π24 π25 π31 π32 π33 π34 π35
H0
I = 2, J = 3 0.33 0.33 0.33
0.33 0.33 0.33
0.10 0.40 0.50
0.10 0.40 0.50
0.40 0.40 0.20
0.40 0.40 0.20
0.01 0.49 0.50
0.01 0.49 0.50
0.49 0.01 0.50
0.49 0.01 0.50
0.98 0.01 0.01
0.98 0.01 0.01
0.01 0.98 0.01
0.01 0.98 0.01
0.01 0.01 0.98
0.01 0.01 0.98
I = 2, J = 4 0.25 0.25 0.25 0.25
0.25 0.25 0.25 0.25
0.20 0.10 0.30 0.40
0.20 0.10 0.30 0.40
0.97 0.01 0.01 0.01
0.97 0.01 0.01 0.01
0.01 0.97 0.01 0.01
0.01 0.97 0.01 0.01
0.01 0.01 0.97 0.01
0.01 0.01 0.97 0.01
0.01 0.01 0.01 0.97
0.01 0.01 0.01 0.97
I = 3, J = 4 0.25 0.25 0.25 0.25
0.25 0.25 0.25 0.25
0.25 0.25 0.25 0.25
0.10 0.20 0.30 0.40
0.10 0.20 0.30 0.40
0.10 0.20 0.30 0.40
0.40 0.30 0.20 0.10
0.40 0.30 0.20 0.10
0.40 0.30 0.20 0.10
0.01 0.49 0.49 0.01
0.01 0.49 0.49 0.01
0.01 0.49 0.49 0.01
0.49 0.01 0.49 0.01
0.49 0.01 0.49 0.01
0.49 0.01 0.49 0.01
0.97 0.01 0.01 0.01
0.97 0.01 0.01 0.01
0.97 0.01 0.01 0.01
0.01 0.97 0.01 0.01
0.01 0.97 0.01 0.01
0.01 0.97 0.01 0.01
0.01 0.01 0.97 0.01
0.01 0.01 0.97 0.01
0.01 0.01 0.97 0.01
0.01 0.01 0.01 097
0.01 0.01 0.01 0.97
0.01 0.01 0.01 0.97
I = 3, J = 5 0.20 0.20 0.20 0.20 0.20 0.20 0.20 0.20 0.20 0.20 0.20 0.20 0.20 0.20 0.20
0.01 0.48 0.01 0.49 0.01 0.01 0.48 0.01 0.49 0.01 0.01 0.48 0.01 0.49 0.01
H1 −H0 I = 2, J = 3 0.10 0.30 0.60
0.15 0.35 0.50
0.10 0.30 0.60
0.60 0.30 0.10
0.40 0.40 0.20
0.80 0.10 0.10
0.01 0.01 0.98
0.20 0.20 0.60
0.01 0.01 0.98
0.98 0.01 0.01
I = 2, J = 4 0.10 0.30 0.20 0.40
0.30 0.10 0.40 0.20
0.10 0.10 0.10 0.70
0.40 0.05 0.05 0.50
0.10 0.20 0.30 0.40
0.15 0.25 0.30 0.30
0.10 0.20 0.30 0.40
0.40 0.30 0.20 0.10
0.25 0.25 0.25 0.25
0.35 0.30 0.30 0.05
0.01 0.01 0.01 0.97
0.97 0.01 0.01 0.01
I = 3, J = 4 0.10 0.30 0.20 0.40
0.20 0.20 0.30 0.30
0.30 0.10 0.40 0.20
0.10 0.10 0.10 0.70
0.40 0.05 0.05 0.50
0.60 0.10 0.10 0.20
0.10 0.20 0.30 0.40
0.10 0.20 0.30 0.40
0.40 0.30 0.20 0.10
0.10 0.20 0.30 0.40
0.20 0.20 0.30 0.30
0.40 0.30 0.20 0.10
0.10 0.20 0.30 0.40
0.40 0.30 0.20 0.10
0.40 0.30 0.20 0.10
I=3, J=5
0.10 0.20 0.30 0.30 0.10 0.10 0.30 0.30 0.20 0.10 0.20 0.30 0.30 0.10 0.10
0.10 0.10 0.10 0.10 0.60 0.10 0.10 0.20 0.20 0.40 0.20 0.20 0.20 0.20 0.20
0.10 0.10 0.10 0.10 0.60 0.50 0.10 0.10 0.10 0.20 0.90 0.01 0.01 0.01 0.07
the comparison between the proposed test and the one-sided Kolmogorov-Smirnov
test. In each scatter plot the diagonal line corresponds to the line of equality. Ad-
ditionally, in the top three panels a horizontal and a vertical line is provided at
0.05 +
p
(.05 × .95)/10000 to indicate points that exceed the nominal value of 0.05
by at least one standard error.
We notice that in general all three test procedures approximately maintain the
nominal size of 0.05. In situations involving rare events (e.g. – probability vector
(0.01, 0.01, 0.98) all tests are conservative, but even in that case, relative to others,
the proposed test appears to recover the nominal size more quickly as the sample
size increases.
As indicated by the points above the diagonal line in the three bottom panels


## Page 12


Order restrictions on rows and columns of a matrix
73
Fig 1. Power and size comparisons of the proposed procedure with Grove’s test (+), Nair’s test
(#) and Kolmogorov-Smirnov test (*). Nominal size is 0.05. Results for the proposed method are
plotted on the vertical axis, and results for other methods are plotted on the horizontal axis.
of Figure 1, the proposed test seems to enjoy higher power than its competitors
in almost all situations considered in this simulation study. In particular, even for
parameter conﬁgurations that are very close to the null, the proposed procedure
has higher power than its competitors. Additionally, in these cases, the proposed
procedure appears to increase in power with sample size at a faster rate than its
competitors.
In addition to a gain in power, a distinct advantage of the proposed test over
likelihood ratio type procedures is the ease of implementation for any arbitrary
order restriction on the rows and columns. The procedure described in Grove [9] is
limited to two groups. As seen in Wang [25], the likelihood ratio type procedures
are very challenging to implement as the number of groups increases.
5. Illustration
In the experiment of Wormser et al. [26] mentioned in the introduction of this
paper, the eﬀect of mustard gas on the skin of mice was evaluated using 6 ordi-
nal variables, namely, subepidermal microblister formation, epidermal ulceration,
epidermal necrosis, acute inﬂammation, hemorrhage, and dermal necrosis. The ex-
periment consisted of exposing 10 mice of each genotype (i.e. COX-2-d, WT and
COX-1-d) to 0.317mg of sulfur mustard. Changes in skin condition of each animal
(as measured by the above 6 variables) were noted on ordinal scale ranging from
“unremarkable”, “minimal”, “mild”, “moderate”, to “marked”. For each response
variable and each genotype, in Table 4 we provide the sample cumulative proportion
of animals in each category.


## Page 13


74
E. Teoh et al.
Table 4
Cumulative relative frequencies for each genotype each for response variable
Level of skin injury
Response variable
Genotype
Unremarkable
Minimal
Mild
Moderate
Marked
Microblister
COX-1-d
0
0.2
1
1
1
WT
0
0.5
0.9
1
1
COX-2-d
0.3
0.8
1
1
1
Ulceration
COX-1-d
0.4
0.5
0.8
0.9
1
WT
0.8
0.9
1
1
1
COX-2-d
1
1
1
1
1
Epidermal necrosis
COX-1-d
0
0
0
0.3
1
WT
0
0
0.1
0.8
1
COX-2-d
0.1
0.2
0.7
0.8
1
Acute inﬂammation
COX-1-d
0
0
0.5
1
1
WT
0
0
0.6
1
1
COX-2-d
0.1
0.5
1
1
1
Hemorrhage
COX-1-d
0
0.1
0.9
1
1
WT
0
0
1
1
1
COX-2-d
0.1
0.4
1
1
1
Dermal necrosis
COX-1-d
0
0.1
0.8
1
1
WT
0
0.1
0.9
1
1
COX-2-d
0.2
0.4
1
1
1
For each response variable, the statistical hypothesis of interest was motivated by
the underlying biology. COX-2 is involved in a variety of inﬂammatory processes
caused by noxious stimuli. For instance, COX-2 is induced within 12 hours and
persists up to 3 days after excisional injury in rat skin. COX-2 expression is seen
in the basal cell layer, peripheral cells in the outer root sheath of hair follicles, and
in ﬁbroblast-like cells and capillaries near the wound edges Lee et al. [13].
Neutrophil COX-2 protein expression after burn-induced injury in mice signiﬁ-
cantly increased at 4 hours and dramatically decreased 36 hours after injury (He
et al. [10]). Due to the central role of COX-2 in the inﬂammatory processes, it is
believed that the eﬀect of mustard gas on COX-2 deﬁcient animals will tend to be
less severe than that on the Wild Type animals.
Nevertheless, COX-1 may have a protective eﬀect on the skin against sulfur
mustard as shown in other organs like the kidney and brain (Lin et al. [14]) and
Vane et al. [24]. COX-1 was suggested to confer protection on the epithelial cells
of the crypts of Lieberk¨uhn, through promotion of crypt stem cell survival and
proliferation, in the ileum of irradiated mice Cohn et al. [5].
As in our skin model case, Cohn et al. [5] also concluded that prostaglandins pro-
duced through the COX-1 pathway, may not be important in unstressed conditions,
but still may have a protective role in the response to epithelial injury. Therefore,
we expect mice with COX-1 deﬁciency to have a more severe response, on average,
than wild-type animals. Then, the experimental setting is the comparison of three
groups with six responses, each of which is measured on an ordinal scale with ﬁve
levels and subject to a simple order.
We analyzed each response variable separately but adjusted the p-value using
Bonferroni correction. The analysis of each response variable was carried out using
the methodology developed in this paper. Based on the above discussion, for each of
the 6 response variables, we tested the following hypotheses, where i = 1 represents
COX-1-d, i = 2 represents WT, and i = 3 represents COX-2-d:
H0 : θ1,j = θ2,j = θ3,j, j = 1, . . . , 4.
Ha : θ1,j ≤θ2,j ≤θ3,j, j = 1, . . . , 4.


## Page 14


Order restrictions on rows and columns of a matrix
75
We computed p-values by bootstrapping the test statistic with 50000 resamplings,
each time sampling the entire record of an animal to preserve the underlying de-
pendence structure between the 6 response variables.
After performing Bonferroni correction for 6 tests, signiﬁcant genotype trends
were found in subepidermal microblister formation (p = 0.0310), ulceration (p =
0.0077), epidermal necrosis (p = 0.0034), and acute inﬂammation (p = 0.0247). We
failed to see signiﬁcant trends in hemorrhage (p = 0.1181) and in dermal necrosis
(p = 0.5170).
6. Discussion
In this article we have extended the iterative algorithm of Dykstra and Robertson
[7] to arbitrary order restrictions on the rows and columns of a matrix as long as
each row is subject to the same order restriction and each column is subject to the
same order restriction. However, the order restrictions on the rows need not be same
as those on the columns. Within each row/column the new algorithm makes use
of the same estimation procedure introduced in Hwang and Peddada [11]. If rows
and columns are subject to a simple order then, for independently and normally
distributed data, the proposed algorithm is identical to the algorithm of Dykstra
and Robertson [7]. We derive a suﬃcient condition for the algorithm to converge in
a single application of Hwang and Peddada [11] method on rows and on columns.
As an example, the suﬃcient condition is satisﬁed in a balanced design.
Using the point estimators derived in this paper, we introduced a new test statis-
tic which is a Kolmogorov type distance on the graph of order restrictions as in
(Peddada et al. [17]). The new procedure is easy to implement and simulations per-
formed in this paper suggest that it has higher power in most cases than some of
the existing procedures. A part of the reason for the new procedure to perform bet-
ter than some of the standard procedures, such as the Kolmogorov-Smirnov test, is
because it uses improved order-restricted point estimators. As seen from our simula-
tion studies, the new estimator enjoys substantially smaller quadratic (and quartic)
risk than the unrestricted estimator, which is used in the Kolmogorov-Smirnov test.
An added advantage of the proposed methodology is that it is applicable to a
very broad collection of matrix order restrictions and is computationally easy to
implement.
Acknowledgments.
The authors wish to thank David Dunson, Grace Kissling,
the reviewers and the editor for providing useful comments that greatly improved
the presentation of the manuscript.
References
[1] Agresti, A. and Coull, B. A. (2002). The analysis of contingency tables un-
der inequality constraints. J. Statist. Plann. Inference 107 45–73. MR1927754
[2] Barlow, R., Bartholomew, D., Bremmer, J. and Brunk, H. (1972).
Statistical Inference Under Order Restrictions, 3rd ed. ed. Wiley, New York.
[3] Berger, V., Permutt, T. and Ivanova, A. (1998). Convex hull test for
ordered categorical data. Biometrics 54 1541–1550.


## Page 15


76
E. Teoh et al.
[4] Cohen, A., Kemperman, J. and Sackrowitz, H. (2000). Properties of
likelihood inference for order restricted models. J. Multivariate Anal. 72 50–
77. MR1747423
[5] Cohn, S., Schloemann, S., Tessner, T., Seibert, K. and Stenson, W.
(1997). Crypt stem cell survival in the mouse intestinal epithelium is regulated
by prostaglandins synthesized through cyclooxygenase-1. J. Clinical Investiga-
tion 99 1367–1379.
[6] Conaway, M. R., Dunbar, S. and Peddada, S. D. (2004). Designs for
single- or multiple-agent phase I trials. Biometrics 60 661–669. MR2089441
[7] Dykstra, R. L. and Robertson, T. (1982). An algorithm for isotonic
regression for two or more independent variables. Ann. Statist. 10 708–716.
MR0663427
[8] Franck, W. E. (1984). A likelihood ratio test for stochastic ordering. J.
Amer. Statist. Assoc. 79 686–691. MR0763587
[9] Grove, D. M. (1980). A test of independence against a class of ordered al-
ternatives in a 2 × C contingency table. J. Amer. Statist. Assoc. 75 454–459.
MR0577381
[10] He, L., Liu, L., Hahn, E. and Gamelli, R. (2001). he expression of cy-
clooxygenase and the production of prostaglandin E2 in neutrophils after burn
injury and infection. J. Burn Care Rehabilitation 22 58–64.
[11] Hwang, J. T. G. and Peddada, S. D. (1994). Conﬁdence interval estimation
subject to order restrictions. Ann. Statist. 22 67–93. MR1272076
[12] Lee, C.-I. C. (1988). Quadratic loss of order restricted estimators for treat-
ment means with a control. Ann. Statist. 16 751–758. MR0947575
[13] Lee, J., Mukhtar, H., Bickers, D., Kopelovich, L. and Athar, M.
(2003). Cyclooxygenases in the skin: Pharmacological and toxicological impli-
cations. Toxicology and Applied Pharmacology 192 294–306.
[14] Lin, H., Lin, T., Cheung, W., Nian, G., Tseng, P., Chen, S., Chen,
J., Shyue, S., Liou, J., Wu, C. and Wu, K. (2002). Cyclooxygenase-1
and bicistronic cyclooxygenase-1/prostacyclin synthase gene transfer protect
against ischemic cerebral infarction. Circulation 105 1962–1969.
[15] Lehmann, E. L. (1983). Theory of Point Estimation. Wiley, New York.
MR0702834
[16] Nair, V. N. (1987). Chi-squared-type tests for ordered alternatives in contin-
gency tables. J. Amer. Statist. Assoc. 82 283–291. MR0883357
[17] Peddada, S. D., Prescott, K. E. and Conaway, M. (2001). Tests for
order restrictions in binary data. Biometrics 57 1219–1227. MR1973822
[18] Peddada, S. D., Dunson, D. B. and Tan, X. (2005). Estimation of order-
restricted means from correlated data. Biometrika 92 703–715. MR2202656
[19] Præstgaard, J. T. and Huang, J. (1996). Asymptotic theory for nonpara-
metric estimation of survival curves under order restrictions. Ann. Statist. 24
1679–1716. MR1416656
[20] Robertson, T. and Wright, F. T. (1981). Likelihood ratio tests for and
against a stochastic ordering between multinomial populations. Ann. Statist.
9 1248–1257. MR0630107
[21] Robertson, T., Wright, F. T. and Dykstra, R. L. (1988). Order Re-
stricted Statistical Inference. Wiley, Chichester. MR0961262
[22] Silvapulle, M. J. (1997). A curious example involving the likelihood ratio
test against one-sided hypotheses. American Statistician 51 178–180.
[23] Silvapulle, M. J. and Sen, P. K. (2005). Constrained Statistical Inference.
Wiley, Hoboken, NJ. MR2099529


## Page 16


Order restrictions on rows and columns of a matrix
77
[24] Vane, J., Bakhle, Y. and Botting, R. (1998). Cyclooxygenases 1 and 2.
Annual Review of Pharmacology and Toxicology 38 97–120.
[25] Wang, Y. (1996). A likelihood ratio test against stochastic ordering in several
populations. J. Amer. Statist. Assoc. 91 1676–1683. MR1439109
[26] Wormser, U., Langenbach, R., Peddada, S., Sintov, A., Brodsky,
B. and Nyska, A. (2004). Reduced sulfur mustard-induced skin toxicity in
cyclooxygenase-2 knockout and celecoxib-treated mice. Toxicology and Applied
Pharmacology 200 40–47.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
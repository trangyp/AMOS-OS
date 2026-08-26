---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1103.0744v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1103.0744v1_Model_Identification_of_a_Network_as_Compressing_Sensing

> Source: 1103.0744v1_Model_Identification_of_a_Network_as_Compressing_Sensing.pdf

> Pages: 25

---


## Page 1


arXiv:1103.0744v1  [math.DS]  3 Mar 2011
Model Identiﬁcation of a network as compressing
sensing
D. Materassib, G. Innocentia, L. Giarréc, M. Salapakab
a Dipartimento di Ingegneria dell’Informazione
Universitá di Siena,
via Roma 56, 53100 Siena, Italy
E-mail: innocenti@dii.unisi.it
b Department of Electrical and Computer Engineering,
University of Minnesota,
200 Union St SE, 55455, Minneapolis (MN)
E-mail: mater013@umn.edu
c Dipartimento di Ingegneria Elettrica, Elettronica e delle Telecomunicazioni
Universitá di Palermo,
viale Delle Scienze, 90128 Palermo, Italy
E-mail: giarre@unipa.it
Abstract
In many applications, it is important to derive information about the topol-
ogy and the internal connections of dynamical systems interacting together.
Examples can be found in ﬁelds as diverse as Economics, Neuroscience and
Biochemistry. The paper deals with the problem of deriving a descriptive
model of a network, collecting the node outputs as time series with no use of
a priori insight on the topology, and unveiling an unknown structure as the
estimate of a “sparse Wiener ﬁlter”. A geometric interpretation of the prob-
lem in a pre-Hilbert space for wide-sense stochastic processes is provided.
We cast the problem as the optimization of a cost function where a set of
parameters are used to operate a trade-oﬀbetween accuracy and complexity
in the ﬁnal model. The problem of reducing the complexity is addressed by
ﬁxing a certain degree of sparsity and ﬁnding the solution that “better” satis-
ﬁes the constraints according to the criterion of approximation. Applications
starting from real data and numerical simulations are provided.
Keywords:
Identiﬁcation, Sparsiﬁcation, Reduced Models, Networks,
Compressive Sensing
Preprint submitted to Systems and Control letters
August 27, 2018


## Page 2


1. Introduction
The interest on networks of dynamical systems is increasing in recent
years, especially because of their capability of modeling and describing a
large variety of phenomena and behaviors. Remarkably, while networks of
dynamical systems are well studied and analyzed in physics [3, 12, 23] and
engineering [29, 24, 26], there are fewer results that address the problem
of reconstructing an unknown dynamical network, since it poses formidable
theoretical and practical challenges [14]. However, unraveling the intercon-
nectedness and the interdependency of a set of processes is of signiﬁcant
interest in many ﬁelds and the necessity for general tools is rapidly emerg-
ing (see [27, 2, 22] and the bibliography therein for recent results). In the
literature, authors have approached this problem in diﬀerent ways and with
various purposes, such as deriving a network topology from just sampled data
(see e.g. [17, 27, 22, 25]) or determining the presence of substructures in the
networked system (see e.g. [23, 2]). The Unweighted Pair Group Method
with Arithmetic mean (UPGMA) [21] is one of the ﬁrst techniques proposed
to reveal an unknown topology. It has found widespread use in the recon-
struction of phylogenetic trees and is widely employed in other areas such as
communication systems and resource allocation problems [9]. Another well-
known technique for the identiﬁcation of a tree network is developed in [17]
for the analysis of a stock portfolio. The authors identify a tree structure
according to the following procedure: i) a metric based on the correlation
index is deﬁned among the nodes; ii) such a metric is employed to extract the
Minimum Spanning Tree [8] which forms the reconstructed topology. How-
ever, in [13] a severe limit of this strategy is highlighted, where it is shown
that, even though the actual network is a tree, the presence of dynamical
connections or delays can lead to the identiﬁcation of a wrong topology. In
[20] a similar strategy, where the correlation metric is replaced by a metric
based on the coherence function, is numerically shown to provide an exact
reconstruction for tree topologies. Furthermore, in [18] it is also illustrated
that a correct reconstruction can be guaranteed for any topology with no
cycles.
An approach for the identiﬁcation of more general topologies is developed in
the area of Machine Learning for Bayesian dynamical networks [11, 10]. In
this case, however, a massive quantity of data needs to be collected in order
to accurately evaluate conditional probability distributions.
In [2] diﬀerent techniques to quantify and evaluate the modular structure of
2


## Page 3


a network are compared and a new one is proposed trying to combine both
the topological and dynamic information of the complex system. However,
the network topology is only qualitatively estimated in terms of “clusters”,
[1]. In [27] a method to identify a network of dynamical systems is described.
However, primary assumptions of the technique are the possibility to manip-
ulate the input of every single node and to conduct as many experiments as
needed to detect the link connectivity.
More recently, in [22] and [19] interesting equivalences between the identiﬁca-
tion of a dynamical network and a l0 sparsiﬁcation problem are highlighted,
suggesting the diﬃculty of the reconstruction procedure [4, 5].
In this paper, the main idea is to cast the problem of unveiling an un-
known structure as the estimate of a “sparse Wiener ﬁlter”. Given a set of
N stochastic processes X = {x1, ..., xn}, we consider each xj as the output
of an unknown dynamical system, the input of which is given by at most mj
stochastic processes {xαj,1, ..., xαj,mj } selected from X \ {xj}. The choice of
{xαj,1, ..., xαj,mj } is realized according to a criterion that takes into account
the mean square of a modeling error. The parameters mj can be a-priori
deﬁned, if we intend to impose a certain degree of sparsity on the network
or a strategy for self-tuning can be introduced penalizing the introduction of
any additional link, if it does not provide a signiﬁcant reduction of the cost.
For any possible choice of {xαj,1, ..., xαj,mj }, the computation of the related
Wiener Filter leads to the deﬁnition of a modeling error, which is a natural
way to measure the quality of the description of xj granted by the time series
{xαj,1, ..., xαj,mj } in terms of predictive/smoothing capability. Once this step
has been performed, each system is represented by a node of a graph and,
then, the arcs linking any xαj,mk to xj are introduced for each node xj. At
the end of this procedure a graph, modeling the network topology, has been
obtained.
We start introducing a pre-Hilbert space for wide-sense stochastic processes,
where the inner product deﬁnes the notion of perpendicularity between two
stochastic processes. We will show that this way of formulating the prob-
lem has strong similarities with l0-minimization problems, which have been
a very active topic of research in Signal Processing during the last few years.
Indeed, a standard l0-minimization problem amounts to ﬁnding the “spars-
est” solution of a set of linear equations in a ﬁnite dimension Hilbert space
[5]. With no additional assumptions on the solution, the problem is combi-
natorially intractable [5]. This has propelled the study of relaxed problems
3


## Page 4


involving, for example, the minimization of the ℓ1 norm, which is a convex
problem and it is known to provide solutions with at least a certain order of
sparsity [22]. Unfortunately, we will show that such a relaxation procedure
is not viable in our formulation. Indeed, it is not possible to deﬁne a suitable
norm in the space of transfer functions that guarantees a certain degree of
sparsity. For this reason, we resort to some greedy techniques in order to
ﬁnd a suboptimal solution with desired sparsity properties.
The rest of the paper is organized as follows.
In Section 2 the network topology identiﬁcation problem is formulated.
In Section 3 a geometric interpretation and the construction of a pre-Hilbert
space needed to deﬁne a distance and an inner product for stochastic pro-
cesses is addressed. In Section 4 the connection with the compressive sensing
problem is shown. In Section 5 a greedy algorithm addressing the problem is
presented along with an alternative approach based on iterated re-weighted
least squares. Finally, in Section 6 the results obtained by applying the tech-
niques to numerical data are discussed. In the Appendix most of the needed
deﬁnitions, propositions, lemmas and proofs needed for the construction of
the pre-Hilbert space are added.
Notation:
Z: the integer set;
R: the real set;
C: the complex set;
E[ · ]: the mean operator;
( · )T: the transponse operator.
2. Problem Formulation
In this section we provide the main deﬁnitions to cast the problem of mod-
eling a network structure. We consider M stochastic processes x1, . . . , xM
representing the output of M nodes in a network with an unknown topol-
ogy. In order to determine the links connecting the nodes, we follow a pro-
cedure based on estimation techniques. Given a process xj and a param-
eter mj ∈N, we search for the Mj processes xα1, . . . , xαk, . . . , xαmj with
αk ̸= j, ∀k = 1, . . . , mj, which provide the best estimate of xj according to a
quadratic criterion. The value mj is a tuning parameter allowing one to oper-
ate a trade-oﬀbetween the sparsity and the accuracy of the model. Thus, mj
can be a-priori chosen or, conversely, determined using a self-tuning strategy.
4


## Page 5


We introduce now some deﬁnitions and results, which turn out essential
for the rigorous formulation of the problem. For sake of clarity, we report in
the Appendix all the additional needed deﬁnitions and properties.
Deﬁnition 1. Let ei(t), with i = 1, ..., N and t ∈Z, be N scalar time-
discrete, zero-mean, jointly wide-sense stationary random processes in a prob-
ability space (Ω, σ, Π), where Ωis the sample space, σ is a sigma algebra on
Ωand Π is a probability measure on σ. Then, for any t ∈Z deﬁne the vec-
tor e(t) := (e1(t), .., eN(t))T, describing a N-dimensional time-discrete, zero-
mean, wide-sense stationary random process. Moreover, for any t1, t2 ∈Z
denote the (N × N) covariance matrix as
Re(t1, t2) := E[e(t1)eT(t2)].
(1)
The entry (i, j), with i, j ∈{1, ..., N} of Re(t1, t2) is given by
Reiej(t1, t2) := E[ei(t1)ej(t2)].
Since any two processes ei and ej are jointly wide-sense stationary by deﬁni-
tion, Reiej(t1, t2) only depends on τ := t2 −t1:
Reiej(0, t2 −t1) = Reiej(t1, t2),
∀t1, t2 ∈Z,
and, thus, Re(t1, t2) too depends only on t2 −t1, i.e.
Re(0, t2 −t1) = Re(t1, t2),
∀t1, t2 ∈Z .
Abusing the notation it is possible to write more concisely Re(τ) = Re(0, τ).
Deﬁnition 2. Consider a vector-valued sequence h(k) ∈R1×N with k ∈Z.
We deﬁne its Z-transform as:
H(z) :=
∞
X
k=−∞
h(k)z−k ,
and we assume that the sum converges for any z ∈C such that r1 < |z| <
r2 with r1 < 1 < r2. Besides, we also assume that any entry of the N-
dimensional vector H(z) is a real-rational function of z. By the properties
of the Z-transform, H(z), along with the convergence domain deﬁned by r1
and r2, uniquely identiﬁes the sequence h(k). Moreover, given a vector of
5


## Page 6


rationally related random processes e(t) := (e1(t), .., eN(t))T, denote for any
t ∈Z the random variable
yt :=
∞
X
k=−∞
h(k)e(t −k).
Then, we deﬁne by H(z)e the related stochastic process such that
(H(z)e)(t) = yt
∀t ∈Z .
Deﬁnition 3. Given a N-dimensional time-discrete, zero-mean, wide-sense
stationary random process e(t) := (e1(t), .., eN(t))T , we deﬁne its power spec-
tral density Φe(z) as:
Φe(z) :=
∞
X
τ=−∞
Re(τ)z−τ ,
having a certain domain of convergence D ⊆C in the variable z. Denoting
by Φeiej(z) the entry (i, j) of Φe(z), it follows that
Φeiej(z) :=
∞
X
τ=−∞
Reiej(τ)z−τ.
Besides, if for any i, j ∈{1, ..., N} the power spectral density Φeiej(z) exists
on the unit circle |z| = 1 of the complex plane and it is a real-rational function
of z, we formally write
Φeiej(z) = A(z)
B(z)
for i, j = 1, . . . , N,
with A(z), B(z) real coeﬃcient polynomials, such that B(z) ̸= 0 for any
z ∈C, |z| = 1. In such a case, we say that e is a vector of rationally related
random processes.
Finally, let us introduce the following sets:
F :={W(z)|W(z) is a real-rational scalar function
of z ∈C deﬁned for |z| = 1}
F m×n :={W(z)|W(z) ∈Cm×n and any
of its entries is in F}.
6


## Page 7


Problem 4. Consider a set X := {x1, ..., xn} ⊂Fe of n rationally related
processes with zero mean and known (cross)-power spectral densities Φxixj(z).
Then, in the above framework the mathematical formulation of the considered
problem can be stated as follows:
min
αj,1,...,αj,mj ̸=j
Wj,αj,k(z)∈F
E
(
xj −
mj
X
k=1
Wj,αj,k(z)xαj,k
)
,
(2)
where every Wj,αj,k(z), with k = 1, ..., mj, is a possibly non-causal transfer
function.
Remark 5. Fixed any set {αj,k}
mj
k=1, Problem 4 is immediately solved by a
multiple input Wiener ﬁlter. However, the determination of the parameters
αj,k makes the problem combinatorial.
3. A geometric interpretation
It is possible to give a geometrical interpretation of (2) by embedding the
processes x1, . . . , xM in a suitable vector space. This interpretation has the
main advantage of giving to the Wiener ﬁlter the meaning of a projective
operator in such a space.
Deﬁnition 6. Let e = (e1, ..., eN)T be a vector of N rationally related ran-
dom processes. We deﬁne the set Fe, as
Fe :=

x = H(z)e | H(z) ∈F 1×N	
.
Proposition 7. The ensemble (Fe, +, ·, R) is a vector space.
Proof.
Consider X1, X2, X3 ∈Fe, x1 ∈X1,x2 ∈X2, x3 ∈X3, and α1, α2 ∈
ℜ.
• Commutativity for the sum
Consider
x := x1 + x2 ∈X1 + X2.
(3)
Then, since x = x2 + x1, we also have that x ∈X2 + X1.
Since
(Fe, +, ·, R) is a partition, we obtain X1 + X2 = X2 + X1.
7


## Page 8


• Associativity for the sum
Consider
xa := x1 + (x2 + x3) ∈X1 + (X2 + X3)
(4)
xb := (x1 + x2) + x3 ∈(X1 + X2) + X3
(5)
(6)
Then, since xa = xb, for the property of a partition set, X1+(X2+X3) =
(X1 + X2) + X3.
• Additive identity
The process x0(t) = 0 for any t is in Fe, because the zero transfer
function is in F. Let the set X0 ∈Fe be the set that constains x0.
Since x1 + x0 = x1 for any x1, we have that X0 is the identity element
for the addition.
• Additive inverse
If x1 ∈Fe, then also −x1 ∈Fe, because the transfer function −1 ∈F.
• Scalar multiplication identity
Let x1 be a process in X1. The scalar 1 is the multiplication identity.
Indeed, we have
1 · x1 = x1 ∈X1.
(7)
Thus, it holds that 1 · X1 = X1.
• Associativity of the scalar multiplication
Since we have that x = α1(α2x1) = (α1α2)x1, we also have that
α1(α2X1) = (α1α2)X1.
• Distribuitivity of the scalar sum
Since we have (α1 + α2)x1 = α1x1 + α2x1, we also have (α1 + α2)X1 =
α1X1 + α2X1
• Distribuitivity of the vector sum
Since we have α1(x1 + x2) = α1x1 + α1x2, we also have α1(X1 + X2) =
α1X1 + α1X2.
□
8


## Page 9


Deﬁnition 8. For any x ∈Fe we denote the norm induced by the inner
product as
∥x∥:=< x, x > .
As shown in details in the Appendix, the set Fe, along with the operation
< ·, · > is a pre-Hilbert space (with the technical assumption that x1 and x2
are the same processes if x1 ∼x2).
We provide an ad-hoc version of the Wiener Filter (guaranteeing that
the ﬁlter will be real rational) with an interpretation in terms of the Hilbert
projection theorem. Indeed, given signals y, x1, ..., xn ∈Fe, the Wiener Filter
estimating y from x := (x1, ..., xn) can be interpreted as the operator that
determines the projection of y onto the subspace Fx
Proposition 9. Let e be a vector of rationally related processes. Let y and
x1, ..., xn be processes in the space Fe. Deﬁne x := (x1, ..., xn)T and consider
the problem
inf
W ∈F1×n ∥y −W(z)x∥2.
(8)
If Φx(ω) > 0, for all ω ∈[−π, π], the solution exists, is unique and has the
form
W(z) = Φyx(z)Φxx(z)−1.
Moreover, for any W ′(z) ∈F 1×nx, it holds that
< y −W(z)x, W ′(z)x >= 0.
(9)
Proof.
Observe that, since q ∈X, the cost function satisﬁes
∥y −W(z)x∥2 =
Z π
−π
Φyy(ω) + W(ω)Φxx(ω)W ∗(ω)+
−Φxy(ω)W ∗(ω) −W(ω)Φyx(ω)dω.
The integral is minimized by minimizing the integrand for all ω ∈[−π, π]. It
is straightforward to ﬁnd that the minimum is achieved for
W(ω) = Φyx(ω)Φ−1
xx(ω).
9


## Page 10


Deﬁning the ﬁlter W(z) = ΦxxI(z)ΦxIxI(z)−1 a real-rational transfer matrix
is obtained with no poles on the unit circle that has the speciﬁed frequency
response. Thus ˆx = W(z)xI ∈X minimizes the cost (8). Equation (9) is
an immediate consequence of the Hilbert projection theorem (for pre-Hilbert
spaces) [15].
Problem 10. The mathematical formulation of the problem can be seen now
as the following:
min
αj,1,...,αj,mj ̸=j
Wj,αj,k(z)∈F





xj −
mj
X
k=1
Wj,αj,k(z)xαj,k





2
,
(10)
4. Links with compressive sensing
In this section we highlight the connections between the problem of mod-
eling a network topology and the compressive sensing problem. Such a con-
nection is possible because of the pre-Hilbert structure constructed in Section
3 and Appendix. Indeed, the concept of inner product deﬁnes a notion of
“projection” among stochastic processes and makes it possible to seamlessly
import tools developed for the compressive sensing problem in order to tackle
that of describing a sparsiﬁed topology.
In the recent few years sparsity problems have attracted the attention of
researchers in the area of Signal Processing. The reason is mainly due to
the possibility of representing a signal using only few elements (words) of a
redundant base (dictionary). Applications are numerous, ranging from data-
compression to high-resolution interpolation, and noise ﬁltering [7], [28].
There are many formalizations of the problem, but one of the most common
is to cast it as
min
w ∥x0 −Ψw∥2
subject to
∥w∥0 ≤m ,
(11)
where n < p, x0 ∈Rp, Ψ ∈Rp×n is a matrix, whose columns represent a
redundant base employed to approximate x0 and the “zero-norm” (it is not
actually a norm)
∥w∥0 := |{i ∈N|wi ̸= 0}|
(12)
is deﬁned by the number of non-zero entries of a vector w. It can be said that
w is a “simple” way to express x0 as a linear combination of the columns of
10


## Page 11


Ψ, where the concept of “simplicity” is given by a constraint on the number
of non-zero entries of w.
For each j = 1, ..., n deﬁne the following sets:
W(j) = {W(z) ∈F 1×n|Wj(z) = 0} ,
(13)
where Wj(z) denotes the j-th component of W(z). For any W ∈W(j), deﬁne
the “zero-norm” as
∥W∥0 = {# of entries such that ∃z ∈C, Wi(z) ̸= 0}
and deﬁne the random vector
x = (x1, ..., xn)T.
(14)
Then, the problem (2) can be formally cast as
min
W ∈Wj ∥xj −Wx∥2
subject to
∥W∥0 ≤m
(15)
which is, from a formal point of view, equivalent to the standard l0 problem
as deﬁned in (11).
5. Solution via suboptimal algorithms
The problem of modeling network interconnections/complexity reduction
we have formulated in this paper is equivalent to the problem of determining
a sparse Wiener ﬁlter, as explained in the previous section, once a notion
of orthogonality is introduced. This formal equivalence shows how deriving
a suitable topology can immediately inherit a set of practical tools already
developed in the area of compressing sensing.
Here we present, as illustrative examples, modiﬁcations of algorithms and
strategies, well-known in the Signal Processing community, which can be
adopted to obtain suboptimal solutions to the problem of modeling the net-
work interconnections.
While formally identical to (11), the problem of a topology reconstruction
cast as in (15) still has its own characteristics. Since the “projection” proce-
dure in (15) is given by the estimation of a Wiener ﬁlter, it is computationally
more expensive than the standard projection in the space of vectors of real
numbers. For this reason greedy algorithms oﬀer a good approach to tackle
11


## Page 12


the problem since speed becomes a fundamental factor. Moreover, since the
complexity of the network model is here one of ﬁnal goal, greedy algorithms
are a suitable solution, since they allow one to specify explicitly the connec-
tion degree mj of every node xj. This feature is in general not provided by
other algorithms. As an alternative approach to greedy algorithms we also
describe a strategy based on iterated reweighted optimizations as described
in [5].
5.1. A modiﬁed Orthogonal Least Squares (Cycling OLS)
Orthogonal Least Squares (OLS) is a greedy algorithm proposed for the
ﬁrst time in [6] and in many ways it resembles the algorithm of Matching
Pursuit developed in [16]. It basically consists of iterated orthogonal pro-
jections on elements of a (possibly redundant) base to approximate a given
vector. For the details of this algorithm we remand the reader to [6]. How-
ever, for the sake of clarity, we reformulate it in terms of our problem. The
initialization occurs at the ﬁrst step setting the set of the chosen elements of
the dictionary to Γ(1) = ∅. At the l−th iteration step, OLS determines the
term ˆx(l,i)
j
to be added to the reduced dictionary by projecting xj onto the
space generated by Γ(l,i) := Γ(l−1) ∪{xi} for any i ̸= j. Then Γ(l) is deﬁned as
the Γ(l,i) for which ∥xj −ˆx(l,i)
j
∥is the smallest and the the algorithm moves to
the next iteration step. The standard OLS goes on at every step introducing
a new vector until a stopping condition is met (usually on the norm of the
residual rk or on the number of iterations).
We propose an algorithm which derives directly from OLS but it does not in-
crease the number of vectors xαj,k approximating xj above mj. The variation
from OLS is very simple. At any iteration, given the set of vectors Γ(l−1),
if it already contains mj vectors, the algorithm chooses a vector in Γ(l−1) to
be removed and tries to replace it with another vector in order to improve
the quality of the approximation and updates it. If such an improvement
is not possible by removing any of the vectors in the current selection, the
algorithm stops. The implementation can be described using the following
pseudocode.
Cycling Orthogonal Least Squares:
0. deﬁne x0 := 0 (null time series) and c = 0.
1. initialize the mj-tuple S = (x0, x0..., x0) and k = 1
12


## Page 13


2. while c ≤mj
2a. for i = 1, ..., n, i ̸= j
deﬁne Si as the mj-tuple where xi replaces the k-th element of S
and
deﬁne ˆx(i)
j
as the projection of xj on to Si
2b. α = arg maxi ∥xj −ˆx(i)
j ∥
2c. if xα = S[k] then c = c + 1
2d. else S[k] = xα, c = 1, k = k mod mj, k = k + 1
3. return S
The reason of our modiﬁcation is simple. COLS implements a coordinate
descent guaranteeing that the number of non-zero components of the solution
does not exceed mj. Once such a limit has been reached, it tries to improve
the quality of the approximation without reducing the sparsity of the current
solution.
5.2. Solution via Re-Weighted Least Squares (RWLS)
Another possible approach to “encourage” sparse solutions is provided by
reweighted minimization algorithms as proposed in [5] and [7]. A comparison
between reweighted norm-1 and norm-2 methods is performed in [28]. We
consider only reweighted least squares, because such an algorithm is easier
to implement, but the intuition behind the two techniques is basically the
same.
Using Parseval theorem, Problem 2, can be formulated as
min
αj,1,...,αj,mj ̸=j
Wj,αj,k(z)∈F
Z π
−π
Φ[xj−Pmj
k=1 Wj,αj,k(ω)xαj,k ](ω)dω.
(16)
Consider the following convex variation of the problem
min
Wj,k(z)∈F
Z π
−π
Φ[xj−P
k̸=j Wj,k(ω)xk](ω)

(17)
subject to
n
X
k=1
Z π
−π
µkW ∗
j,k(ω)Wj,k(ω)dω ≤1
13


## Page 14


where µk ∈Rn is a set of weights for the ﬁlters Wj,k(z). Using the compact
notation introduced in Section 4, we can equivalently write
min
W ∈Wj ∥xj −Wx∥2
subject to
∥W∥2
µ ≤1
(18)
where, for a vector µ = (µ1, ..., µn), we deﬁne
∥W∥2
µ := 1
mj
n
X
1
Z π
−π
µkW ∗
j,k(ω)Wj,k(ω)dω ≤1.
Let us assume that the αj,k’s and the relative Wαj,k solving (2) are known.
Technically, we could set
µl := 1
mj
Z π
−π
W ∗
l (ω)Wl(ω)dω
−1
,
(19)
if l = αj,k for some k = 1, ..., mj and µl = +∞otherwise. With such a choice
of weights, the two problems (2) and (18) would be equivalent since they
would provide the same solutions. However, Problem (18) has the advantage
of being convex. Of course, the values αj,k are not a-priori known, thus it
is not possible to evaluate (19). An iterative approach has been proposed
making use of the intuition that we have just formulated to estimate the
weights (19).
Reweighted Least Squares:
0. For all xj
1. initialize the weight vector µ := 0
2. while a stop criterion is met
2a. solve the convex problem
min
W ∈Wj ∥xj −Wx∥2
subject to
∥Wj∥2
µ ≤1
2b. compute the new weigths
µk = 1
mj
Z π
−π
∥Wj(ω)∥dω
14


## Page 15


3. return all the Wj’s.
At any iteration the convex relaxation of the problem is solved and new
weights are computed as a functions of the current solution. When a stopping
criterion is met (usually on the number of iterations), the ﬁnal solution can
be obtained by selecting the mj largest entries of each Wj.
6. Applications and examples
In this section we report numerical results obtained implementing the
algorithms described in the previous section. In order to evaluate the perfor-
mances provided by the two algorithms (COLS and RWLS) we have consid-
ered a network of 20 nodes as represented in Figure 1(true) . In the graph
every node Nj describes a stochastic process xj, while every directed arc form
a node Ni to a node Nj represents a transfer function Hji(z) ̸= 0 that has
been randomly selected from a class of causal FIR ﬁlters of order 5. The
absence of such an arc implies that Hji(z) = 0. Thus, each process xj follows
the dynamics
xj = ej +
X
i̸=j
Hji(z)xi .
(20)
Every node signal is also implicitly considered aﬀected by an additive white
Gaussian noise ej such that the Signal to Noise Ratio (SNR) is 4 (a very
noisy scenario). All the noise processes are independent from each other. The
network has been simulated for 2000 steps obtaining 20 time series. The time
series have been employed to estimate a non-causal FIR approximation of the
Wiener Filters of order 21 both in the COLS and in the RWLS algorithm.
In Figure 1 we report the results of the identiﬁcation. Using a global search
the global minima of (11) provide the topologies in Figure 1 (reduced 2)
and Figure 1 (reduced 3) for the case mj = 2 and mj = 3 for each node
respectively.
In Figure 1 (no reduction) we report the topology obtained
with no constraint on the maximum number of edges: a small threshold has
been introduced to remove any edge (Ni, Nj) associated with Wji(z) ≃0. In
the second row of graphs we have the results for COLS for the cases mj = 1,
mj = 2 and mj = 3. In Figure 1 (COLS variable) we report the result given
by the implementation of a strategy to automatically determine the number
of edges: the number of edges is increased only if gives a reduction of 20%
of the residual error. In the third row of graphs, we report the analogous
results for the RWLS algorithm.
15


## Page 16


1
2
4
5
7
1 3
3
6
1 5
8
9
1 4
1 6
1 0
1 7
1 1
1 2
1 8
1 9
2 0
1
2
4
5
7
1 8
3
6
1 4
1 1
1 3
1 7
1 5
8
9
1 6
1 2
1 0
1 9
2 0
1
2
4
5
6
7
1 8
3
1 3
1 7
1 4
1 1
1 5
8
9
1 6
1 0
1 2
1 9
2 0
1
2
4
6
1 8
5
7
3
1 3
1 7
1 1
1 2
1 5
8
9
1 0
1 6
1 4
1 9
2 0
(true)
(reduced 2)
(reduced 3)
(no reduction)
1
2
5
6
4
7
3
1 4
1 3
8
9
1 6
1 0
1 7
1 5
1 1
1 2
1 9
2 0
1 8
1
2
4
5
6
7
1 8
3
1 4
1 1
1 3
1 7
1 5
8
9
1 6
1 2
1 0
1 9
2 0
1
2
4
5
6
7
1 8
3
1 3
1 7
1 4
1 1
1 5
8
9
1 6
1 0
1 2
1 9
2 0
1
2
4
5
6
7
1 8
3
1 3
1 7
1 4
1 1
1 5
8
9
1 6
1 2
1 0
1 9
2 0
(COLS 1)
(COLS 2)
(COLS 3)
(COLS variable)
1
2
5
6
4
7
3
1 3
8
9
1 6
1 4
1 0
1 7
1 5
1 1
1 2
1 9
2 0
1 8
1
2
4
5
6
7
1 8
3
1 1
1 3
1 7
1 5
8
9
1 6
1 4
1 2
1 0
1 9
2 0
1
2
4
1 8
5
6
7
3
1 3
1 7
1 1
1 5
8
9
1 6
1 4
1 0
1 2
1 9
2 0
1
2
4
1 8
5
6
7
3
1 7
1 1
1 3
1 5
8
9
1 6
1 4
1 2
1 9
1 0
2 0
(RWLS 1)
(RWLS 2)
(RWLS 3)
(RWLS variable)
Figure 1: The actual network topology (true); the topology obtained by a global minimiza-
tion of (8) with mj = 2 for every node (reduced 2); the topology with mj = 3 for every
node (reduced 3); the topology with no constraint on mj but with a “small” threshold
imposed on a norm of the Wiener Filters to avoid a complete graph (no reduction); the
topologies obtained used the COLS suboptimal approach with mj = 1 (COLS 1), mj = 2
(COLS 2), mj = 3 (COLS 3), and a self-adjusting strategy for mj (COLS variable): a
link is introduced if gives at least a reduction of 20% of the residual error; the topologies
obtained by RWLS after 10 iterations and keeping only the mj ﬁlters with largest norm
(RWLS 1), (RWLS 2), (RWLS 3), or a self-adjusting strategy (RWLS variable).
16


## Page 17


Name
Code
Country
Australian Dollar
AUD
Australia
Brazil Real
BRL
Brazil
Canadian Dollar
CAD
Canada
Chinese Renminbi
CNY
China
Danish Krone
DKK
Denmark
Euro
EU
European Union
British Pound
GPB
Great Britain
Hong Kong Dollar
HKD
Hong Kong
Indian Rupee
INR
India
Japanese Yen
JPY
Japan
South Korean Won
KRW
South Korea
Sri Lankan rupee
LKR
Sri Lanka
Mexican Peso
MXN
Mexico
Malaysian Ringgit
MYR
Malaysia
Norwegian Krone
NOK
Norway
New Zealand Dollar
NZD
New Zealand
Swedish Krona
SEK
Sweden
Singapore Dollar
SGD
Singapore
Thai Baht
THB
Thailand
Taiwanese Dollar
TWD
Taiwan
American Dollar
USD
United States of America
South African Rand
ZAR
South Africa
Table 1: List of the currencies considered in the analysis.
6.1. An application to real data: currency exchange rates
In this section we also present the results obtained by applying our tech-
nique to real data. We have considered the daily exchange rate of 22 selected
currencies (reported in Table 1) from the last 7 years providing 1715 samples
for any of the time series. The missing data (the exchange rate on Satur-
days and Sundays) have been interpolated (by cubic splines) such that a
total number of 2400 daily points have been obtained for our analysis. The
Cycling OLS algorithm has been applied on the logarithmic returns of the
time series (a standard procedure in Finance,) with order 1,2 e 3 and the
estimated topologies are depicted in Figure 2 a, Figure 2 b and Figure 2 c.
17


## Page 18


SEK
NOK
DKK
EU
TWD
CAD
MXN
BRL
NZD
CNY
INR
HKD
USD
LKR
MYR
AUD
ZAR
JPY
GBP
SGD
THB
KRW
SEK
NOK
DKK
JPY
EU
TWD
KRW
CAD
AUD
MXN
BRL
ZAR
NZD
CNY
INR
HKD
USD
GBP
THB
LKR
MYR
SGD
SEK
CNY
ZAR
DKK
CAD
BRL
JPY
TWD
THB
AUD
MXN
NZD
INR
HKD
USD
GBP
LKR
NOK
MYR
SGD
EU
KRW
(a)
(b)
(c)
Figure 2: The reconstructed topologies obtaining applying the Cycling OLS to the ex-
change rate time series of the 22 selected currencies.
7. Final Remarks
We have formulated the problem of deriving a link structure from a set
of time series, obtained by sampling the output of as many interconnected
dynamical systems. Every time series is represented as a node in a graph
and their dependencies as connecting edges. The approach we follow in de-
termining the graph arcs relies on (linear) identiﬁcation techniques based on
an ad-hoc version of the Wiener Filter (guaranteeing that the ﬁlter will be
real rational) with an interpretation in terms of the Hilbert projection the-
orem. If a time series Xi turns outs “useful” to model the time series Xj,
then the directed arc (i, j) is introduced in the graph. In order to modulate
the complexity of the ﬁnal graph, a maximum number mj of arcs pointing at
Xj is assumed and a cost function is minimized to ﬁnd the most appropriate
arcs. The problem has a similar formulation and strong connections with the
problem of compressing sensing, which has been widely studied in the last
few years. Such a connection is possible because of the pre-Hilbert structure
we have constructed. Indeed, the concept of inner product deﬁnes a notion of
“projection” among stochastic processes and makes it possible to seamlessly
import tools developed for the compressive sensing problem in order to tackle
the problem of modeling a network topology.
The problem of topology reconstruction/complexity reduction is equivalent
to the problem of determining a sparse Wiener ﬁlter as explained. However,
since an optimization problem must be solved for any single node, we consider
the application of suboptimal solutions. In particular, we introduce a subop-
timal greedy algorithm obtained as a modiﬁcation of the Orthogonal Least
18


## Page 19


Squares (COLS) and an alternative approach based on iterated ReWeighted
Least Squares (RWLS). By the comparison of the two algorithms on numer-
ical data we have shown the eﬀectiveness of the proposed solutions. Note
that in the present paper no absolute error metric is provided.
Future work will investigate some measure criteria to judge the performance
of the algorithm. For instance, as a starting method we could count the
correct identiﬁed links and the wrong ones, when the underlying topology is
known, to deﬁne the "more accurate" topology and extend such a measure
of accuracy in some norms to the unknown topology case.
References
[1] Vincent D Blondel, Jean-Loup Guillaume, Renaud Lambiotte, and Eti-
enne Lefebvre. Fast unfolding of communities in large networks. Jour-
nal of Statistical Mechanics: Theory and Experiment, 2008(10):P10008,
2008.
[2] S. Boccaletti, M. Ivanchenko, V. Latora, A. Pluchino, and A. Rapisarda.
Detecting complex network modularity by dynamical clustering. Phys.
Rev. E, 75:045102, 2007.
[3] S. Boccaletti, V. Latora, Y. Moreno, M. Chavez, and D. U. Hwang.
Complex networks: Structure and dynamics. Physics Reports, 424(4-
5):175–308, February 2006.
[4] E. J. Candès and Terence Tao. Decoding by linear programming. IEEE
Transactions on Information Theory, 51(12):4203–4215, 2005.
[5] Emmanuel Candès, Michael Wakin, and Stephen Boyd. Enhancing spar-
sity by reweighted l1 minimization. Journal of Fourier Analysis and
Applications, 14:877–905, 2008.
[6] S. Chen, S. A. Billings, and W. Luo. Orthogonal least squares methods
and their application to non-linear system identiﬁcation. Intl. J. Control,
50(5):1873–1896, 1989.
[7] I. Daubechies, R. DeVore, M. Fornasier, C. S&idot, et al. Iteratively
reweighted least squares minimization for sparse recovery. Communica-
tions on Pure and Applied Mathematics, 63(1):1–38, 2009.
19


## Page 20


[8] R. Diestel. Graph Theory. Springer-Verlag, Berlin, Germany, 2006.
[9] R.B. Freckleton, P.H. Harvey, and M. Pagel. Phylogenetic analysis and
comparative data: A test and review of evidence. American Naturalist,
160:712–726, 2002.
[10] Nir Friedman and D. Koller. Being bayesian about network structure: A
bayesian approach tostructure discovery in bayesian networks. Machine
Learning, 50:95–126, 2003.
[11] L. Getoor, N. Friedman, B. Taskar, and D. Koller. Learning probabilistic
models of relational structure. Journal of Machine Learning Research,
3:679–707, 2002.
[12] M. Girvan and M. E. J. Newman. Community structure in social and
biological networks. Proceedings of the National Academy of Sciences,
99(12), 2002.
[13] G. Innocenti and D. Materassi. A modeling approach to multivariate
analysis and clusterization theory. Journal of Physics A, 41(20):205101,
2008.
[14] E.D. Kolaczyk. Statistical Analysis of Network Data: Methods and Mod-
els. Springer-Verlag, Berlin, Germany, 2009.
[15] David G. Luenberger. Optimization by vector space methods. John Wiley
& Sons Inc., Hoboken, New Jersey, 1969.
[16] S. Mallat and Z. Zhang. Matching pursuits with time-frequency dictio-
naries. IEEE Transactions on Signal Processing, 41(12), 1993.
[17] R.N. Mantegna and H.E. Stanley.
An Introduction to Econophysics:
Correlations and Complexity in Finance. Cambridge University Press,
Cambridge UK, 2000.
[18] D. Materassi and G. Innocenti. Topological identiﬁcation in networks of
dynamical systems. In Proc. of IEEE CDC, Cancun (Mexico), December
2008.
[19] D. Materassi, G. Innocenti, and L. Giarre. Reduced complexity models
in the identiﬁcation of dynamical networks: Links with sparsiﬁcation
20


## Page 21


problems. In Decision and Control, 2009 held jointly with the 2009 28th
Chinese Control Conference. CDC/CCC 2009. Proceedings of the 48th
IEEE Conference on, pages 4796 –4801, 2009.
[20] Donatello Materassi and Giacomo Innocenti. Unveiling the connectiv-
ity structure of ﬁnancial networks via high-frequency analysis. Physica
A: Statistical Mechanics and its Applications, 388(18):3866–3878, June
2009.
[21] C.D. Michener and R.R. Sokal. A quantitative approach to a problem
of classiﬁcation. Evolution, 11:490–499, 1957.
[22] D. Napoletani and T. Sauer. Reconstructing the topology of sparsely
connected dynamical networks. Phys. Rev. E, 77:026103, 2008.
[23] M. E. J. Newman and M. Girvan. Finding and evaluating community
structure in networks. Physical Review E, 69(2), 2004.
[24] R. Olfati-Saber. Distributed kalman ﬁltering for sensor networks. In
Proc. of IEEE CDC, pages 5492–5498, New Orleans, 2007.
[25] M. Ozer and M. Uzuntarla. Eﬀects of the network structure and coupling
strength on the noise-induced response delay of a neuronal network.
Physics Letters A, 375:4603–4609, 2008.
[26] I. Schizas, A. Ribeiro, and G. Giannakis. Consensus in ad hoc WSNs
with noisy links-part i: Distributed estimation of deterministic signals.
IEEE Trans. on Signal Processing, 56(1), 2008.
[27] M. Timme. Revealing network connectivity from response dynamics.
Phys. Rev. Lett., 98(22):224101, 2007.
[28] D. P. Wipf and S. Nagarajan. Iterative reweighted l1 and l2 methods
for ﬁnding sparse solutions. In Signal Processing with Adaptive Sparse
Structured Representations, Rennes, France, April 2009.
[29] H. Zhang, Z. Liu, M. Tang, and P.M. Hui. An adaptative routing strat-
egy for packet delivery in complex networks. Physics Letters A, 364:177–
182, 2007.
21


## Page 22


8. Appendix
We provided hereafter the deﬁnitions and propositions which are addi-
tionally needed for the construction of the pre-Hilbert space.
Deﬁnition 11. Given two time-discrete scalar, zero-mean, wide-sense jointly
stationary random processes x1(t) and x2(t), we write that x1 ∼x2 if and
only if, for any t ∈Z, E[(x2(t) −x1(t))2] = 0, that is x1(t)
a.s.
= x2(t) (that is
x1(t) = x2(t) almost surely for any t ∈Z).
Proposition 12. The relation ∼is an equivalence relation on any set X of
zero-mean time-discrete wide-sense jointly stationary scalar random processes
deﬁned on the time domain Z.
Proposition 13. Let x1 := H(1)(z)e, x2 := H(2)(z)e be two elements of
Fe. Then x1, x2 are scalar, zero-mean, wide-sense jointly stationary random
processes with rational power cross-spectral densities having no poles n the
set {z ∈C| |z| = 1}.
Proof.
The processes x1 and x2 are scalar by the deﬁnition of Fe. Since
H(1)(z), H(2)(z) ∈F 1×n, they are real-rational and deﬁned on the unit cir-
cle, and, as a consequence, they admit a unique representation in terms of
bilateral Z-transform
H(1)(z) =
+∞
X
k=−∞
h(1)
k z−k
(21)
H(2)(z) =
+∞
X
k=−∞
h(2)
k z−k,
(22)
with h(1)
k , h(2)
k
∈R1×n for k ∈Z, such that the convergence is guaranteed on
the unit circle |z| = 1.
First, let us evaluate the mean of x1(t), that is
E[x1(t)] = E
"
∞
X
k=−∞
h(1)
k e(t −k)
#
=
=
∞
X
k=−∞
h(1)
k E[e(t −k)] = H(1)(1)E[e(0)] = 0.
22


## Page 23


Thus, it does not depend on the time t. Analogously E[x2(t)] = 0. Now, let
us evaluate the cross-covariance function
Rx1x2(t, t + τ) := E[x1(t)x2(t + τ)T ] =
= E
" 
∞
X
k=−∞
h(1)(k)e(t −k)
!  
∞
X
l=−∞
eT(t + τ −l)(h(2)(l))T
!#
=
= E
"
∞
X
k=−∞
∞
X
l=−∞
h(1)(k)e(t −k)eT(t + τ −l)(h(2)(l))T
#
=
=
∞
X
k=−∞
∞
X
l=−∞
h(1)(k)E[e(t −k)eT (t + τ −l)](h(2)(l))T =
=
∞
X
k=−∞
∞
X
l=−∞
h(1)(k)Re(τ −l + k)(h(2)(l))T = Rx1x2(0, τ).
Thus, the cross-covariance does not depend on the time t and, abusing no-
tation, it is possible to deﬁne
Rx1x2(τ) := Rx1x2(0, τ)
(23)
Moreover, if we evaluate the bilateral Z-transform of Rx1x2(τ), we have
Φx1x2(z) :=
∞
X
τ=−∞
Rx1x2(τ)z−τ =
=
∞
X
τ=−∞
∞
X
k=−∞
∞
X
l=−∞
h(1)(k)Re(τ −l + k)(h(2)(l))Tz−τ−l+kz−kzl =
= H(1)(z)Φe(z)H(2)(z−1).
□
Proposition 14. Given a rationally related vector e, the set Fe is closed
with respect to addition, transformation by H(z) ∈F and multiplication
by scalar α ∈ℜ.
Moreover, it holds that, for x1 = H(1)(z)e ∈Fe and
x2 = H(2)(z)e ∈Fe,
H(1)(z)e + H(2)(z)e =

H(1)(z) + H(2)(z)

e
H(z)[H(1)(z)e] =

H(z)H(1)(z)

e
α[H(1)(z)e] =

αH(1)(z)

e.
23


## Page 24


Proof.
Let
H(z) =
+∞
X
k=−∞
h(k)z−k.
(24)
• Sum.
We have
x1(t) + x2(t) =
"
∞
X
k=−∞
h(1)
k e(t −k)
#
+
"
∞
X
k=−∞
h(2)
k e(t −k)
#
=
∞
X
k=−∞
[h(1)
k + h(2)
k ]e(t −k) = ([H(1)(z) + H(2)(z)]e)(t).
Since [H(1)(z) + H(2)(z)] has no poles on the set {z ∈C| |z| = 1},
x1 + x2 ∈Fe.
• Multiplication by H(z) ∈F.
Since x1 ∈Fe, it is a 1-dimensional rationally related vector. Then, it
makes sense to compute the random process H(z)x1 for H(z) ∈F =
F 1×1
(H(z)x1)(t) :=
∞
X
k=−∞
h(k)x1(t −k) =
(25)
=
∞
X
k=−∞
h(k)
∞
X
l=−∞
h(1)
l e(t −k −l) =
(26)
=
∞
X
k=−∞
h(k)
∞
X
l=−∞
h(1)
l−ke(t −l) =
(27)
=
∞
X
l=−∞
"
∞
X
k=−∞
h(k)h(1)
l−k
#
e(t −l) =
(28)
=
 
H(z)H(1)(z)

e

(t),
(29)
where the last equality comes from the properties of the convolution.
Since H(z)H(1)(z) has no poles in the set {z ∈C| |z| = 1}, H(z)x1 ∈
Fe
24


## Page 25


• Multiplication by scalar α ∈ℜ.
It is a special case of the previous property.
□
Deﬁnition 15. We deﬁne a scalar binary operation < ·, · > on Fe in the
following way
< x1, x2 >:= Rx1x2(0).
Proposition 16. The set Fe, along with the operation < ·, · > is a pre-
Hilbert space (with the technical assumption that x1 and x2 are the same
processes if x1 ∼x2).
Proof.
The proof is left to the reader, making use of the introduced nota-
tions and properties.
□
25

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
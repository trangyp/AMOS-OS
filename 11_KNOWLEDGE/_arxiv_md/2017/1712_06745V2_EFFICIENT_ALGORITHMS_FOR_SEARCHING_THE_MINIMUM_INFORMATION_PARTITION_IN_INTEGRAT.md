---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1712.06745v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1712.06745v2_Efficient_Algorithms_for_Searching_the_Minimum_Information_Partition_in_Integrat

> Source: 1712.06745v2_Efficient_Algorithms_for_Searching_the_Minimum_Information_Partition_in_Integrat.pdf

> Pages: 22

---


## Page 1


arXiv:1712.06745v2  [q-bio.NC]  13 Feb 2018
Article
Efﬁcient Algorithms for Searching the Minimum
Information Partition in Integrated Information
Theory
Jun Kitazono 1,2*, Ryota Kanai 1 and Masafumi Oizumi 1,3*
1
Araya, Inc., Toranomon 15 Mori Building 2-8-10 Toranomon Minato-ku Tokyo, 105-0001, JAPAN;
{kitazono, kanair, oizumi}@araya.org
2
Graduate School of Engineering, Kobe University, 1-1 Rokkodai-cho Nada-ku Kobe-shi Hyogo, 657-8501,
JAPAN
3
RIKEN Brain Science Institute, 2-1 Hirosawa Wako City Saitama, 351-0198, JAPAN
*
Correspondence: kitazono@araya.org, oizumi@araya.org; Tel.: +81-3-6550-9977
Academic Editor: name
Version February 14, 2018 submitted to Entropy; Typeset by LATEX using class ﬁle mdpi.cls
Abstract: The ability to integrate information in the brain is considered to be an essential property
for cognition and consciousness. Integrated Information Theory (IIT) hypothesizes that the amount
of integrated information (Φ) in the brain is related to the level of consciousness. IIT proposes that to
quantify information integration in a system as a whole, integrated information should be measured
across the partition of the system at which information loss caused by partitioning is minimized,
called the Minimum Information Partition (MIP). The computational cost for exhaustively searching
for the MIP grows exponentially with system size, making it difﬁcult to apply IIT to real neural
data.
It has been previously shown that if a measure of Φ satisﬁes a mathematical property,
submodularity, the MIP can be found in a polynomial order by an optimization algorithm. However,
although the ﬁrst version of Φ is submodular, the later versions are not. In this study, we empirically
explore to what extent the algorithm can be applied to the non-submodular measures of Φ by
evaluating the accuracy of the algorithm in simulated data and real neural data. We ﬁnd that the
algorithm identiﬁes the MIP in a nearly perfect manner even for the non-submodular measures. Our
results show that the algorithm allows us to measure Φ in large systems within a practical amount
of time.
Keywords: integrated information theory; integrated information; minimum information partition;
submodularity; Queyranne’s algorithm; consciousness.
1. Introduction
The brain receives various information from the external world. Integrating this information
is an essential property for cognition and consciousness [1].
In fact, phenomenologically, our
consciousness is uniﬁed. For example, when we see an object, we cannot experience only its shape
independently of its color. Or, we cannot experience only the left half of the visual ﬁeld independently
of the right half. Integrated Information Theory of consciousness (IIT) considers that the uniﬁcation
of consciousness should be realized by the ability of the brain to integrate information [2–4]. That
is, the brain has internal mechanisms to integrate information about the shape and color of an
object or information of the right and left visual ﬁeld, and therefore our visual experiences are
uniﬁed. IIT proposes to quantify the degree of information integration by an information theoretic
measure “integrated information” and hypothesizes that integrated information is related to the level
of consciousness. Although the hypothesis is indirectly supported by experiments which showed
Submitted to Entropy, pages 1 – 22
www.mdpi.com/journal/entropy


## Page 2


Version February 14, 2018 submitted to Entropy
2 of 22
the breakdown of effective connectivity in the brain during loss of consciousness [5,6], only a few
studies have directly quantiﬁed integrated information in real neural data [7–10] because of the
computational difﬁculties described below.
Conceptually, integrated information quantiﬁes the degree of interaction between parts or
equivalently, the amount of information loss caused by splitting a system into parts [11,12]. IIT
proposes that integrated information should be quantiﬁed between the least interdependent parts
so that it quantiﬁes information integration in a system as a whole. For example, if a system consists
of two independent subsystems, the two subsystems are the least interdependent parts. In this case,
integrated information is 0 because there is no information loss when the system is partitioned into
the two independent subsystems.
Such a critical partition of the system is called the Minimum
Information Partition (MIP), where information is minimally lost, or equivalently where integrated
information is minimized. In general, searching for the MIP requires an exponentially large amount of
computational time because the number of partitions exponentially grows with the arithmetic growth
of system size N. This computational difﬁculty hinders the application of IIT to experimental data,
despite its potential importance in consciousness research and even in broader ﬁelds of neuroscience.
In the present study, we exploit a mathematical concept called submodularity to resolve the
combinatorial explosion of ﬁnding the MIP. Submodularity is an important concept in set functions
which is analogous to convexity in continuous functions. It is known that an exponentially large
computational cost for minimizing an objective function is reduced to the polynomial order if
the objective function satisﬁes submodularity.
Previously, Hidaka and Oizumi showed that the
computational cost for ﬁnding the MIP is reduced to O(N3) [13] by utilizing Queyranne’s submodular
optimization algorithm [14]. They used mutual information as a measure of integrated information
that satisﬁes submodularity. The measure of integrated information used in the ﬁrst version of IIT
(IIT 1.0) [2] is based on mutual information. Thus, if we consider mutual information as a practical
approximation of the measure of integrated information in IIT 1.0, Queyranne’s algorithm can be
utilized for ﬁnding the MIP. However, the practical measures of integrated information in the later
versions of IIT [12,15–17] are not submodular.
In this paper, we aim to extend the applicability of submodular optimization to non-submodular
measures of integrated information.
We speciﬁcally consider the three measures of integrated
information; mutual information ΦMI [2], stochastic interaction ΦSI [15,18,19], and geometric
integrated information ΦG [12]. Mutual information is strictly submodular but the others are not.
Oizumi et al. previously showed a close relationship among these three measures [12,20]. From
this relationship, we speculate that Queyranne’s algorithm might work well for the non-submodular
measures. Here, we empirically explore to what extent Queyranne’s algorithm can be applied to the
two non-submodular measures of integrated information by evaluating the accuracy of the algorithm
in simulated data and real neural data. We ﬁnd that Queyranne’s algorithm identiﬁes the MIP in a
nearly perfect manner even for the non-submodular measures. Our results show that Queyranne’s
algorithm can be utilized even for non-submodular measures of integrated information and makes
it possible to practically compute integrated information across the MIP in real neural data, such
as multi-unit recordings used in EEG and ECoG, which typically consist of around 100 channels.
Although the MIP was originally proposed in IIT for understanding consciousness, it can be utilized
to analyze any system irrespective of consciousness such as biological networks, multi-agent systems,
and oscillator networks. Therefore, our work would be beneﬁcial not only for consciousness studies
but also to other research ﬁelds involving complex networks of random variables.
This paper is organized as follows.
We ﬁrst explain that the three measures of integrated
information, ΦMI, ΦSI, ΦG, are closely related from a uniﬁed theoretical framework [12,20] and there
is an order relation among the three measures; ΦMI ≥ΦSI ≥ΦG. Next, we compare the partition
found by Queyranne’s algorithm with the MIP found by exhaustive search in randomly generated
small networks (N = 14). We also evaluate the performance of Queyranne’s algorithm in larger
networks (N ∼20 and 50 for ΦSI and ΦG, respectively). Since the exhaustive search is intractable, we


## Page 3


Version February 14, 2018 submitted to Entropy
3 of 22
compare Queyranne’s algorithm with a different optimization algorithm called the replica exchange
Markov Chain Monte Carlo (REMCMC) method [21–24]. Finally, we evaluate the performance of
Queyranne’s algorithm in ECoG data recorded in monkeys and investigate the applicability of the
algorithm in real neural data.
2. Measures of integrated information
Figure 1. Measures of integrated information represented by the Kullback-Leibler divergence between
the actual distribution p and q. (a) Mutual information. (b) Stochastic interaction. (c) Geometric
integrated information.
The arrows indicate inﬂuences across different time points and the lines
without arrowheads indicate inﬂuences between elements at the same time. This ﬁgure is modiﬁed
from [12].
Let us consider a stochastic dynamical system consisting of N elements.
We represent
the past and present states of the system as X
=
(X1, . . . , XN) and X′
=
(X′
1, . . . , X′
N),
respectively. In the case of a neural system, the variable X can be signals of multi-unit recordings,
EEG, ECoG, and fMRI, etc.
Conceptually, integrated information is designed to quantify the
degree of spatio-temporal interactions between subsystems.
The previously proposed measures
of integrated information are generally expressed as the Kullback-Leibler divergence between the
actual probability distribution p (X, X′) and a “disconnected” probability distribution q (X, X′) where
interactions between subsystems are removed [12].
Φ = min
q
DKL
 p
 X, X′ ||q
 X, X′
,
(1)
= min
q ∑
x,x′
p
 x, x′
log p (x, x′)
q (x, x′) .
(2)
The Kullback-Leibler divergence measures the difference between the probability distributions, and
can be interpreted as the information loss when q (X, X′) is used to approximate p (X, X′) [25].
Thus, integrated information is interpreted as information loss caused by removing interactions. In
Eq. (2), the minimum over q should be taken to ﬁnd the best approximation of p, while satisfying the
constraint that the interactions between subsystems are removed [12].
There are many ways of removing interactions between units, which lead to different
disconnected probability distributions q, and also different measures of integrated information


## Page 4


Version February 14, 2018 submitted to Entropy
4 of 22
(Fig. 1). The arrows indicate inﬂuences across different time points and the lines without arrowheads
indicate inﬂuences between elements at the same time. Below, we will show that three different
measures of integrated information are derived from different probability distributions q.
2.1. Multi (Mutual) information ΦMI
First, consider the following partitioned probability distribution q,
q
 X, X′ = ∏
i
q
 Mi, M′
i

,
(3)
where Mi and M′
i are the past and present states of the i-th subsystem, respectively. In this model, all
of the interactions between the subsystems are removed, i.e., the subsystems are totally independent
(Fig. 1 (a)). In this case, the corresponding measure of integrated information is given by
ΦMI = ∑
i
H(Mi, M′
i) −H(X, X′),
(4)
where H(·, ·) represents the joint entropy.
This measure is called total correlation [26] or multi
information [27]. As a special case when the number of subsystems is two, this measure is simply
equivalent to the mutual information between the two subsystems,
ΦMI = H(M1, M′
1) + H(M2, M′
2) −H(X, X′).
(5)
The measure of integrated information used in the ﬁrst version of IIT is based on mutual information
but is not identical to mutual information Eq. (5). The critical difference is that the measures in
IIT are based on perturbation and those considered in this study are based on observation.
In
IIT, a perturbational approach is used for evaluating probability distributions, which attempts to
quantify actual causation by perturbing a system into all possible states [2,4,11,28]. The perturbational
approach requires full knowledge of the physical mechanisms of a system, i.e., how the system
behaves in response to all possible perturbations. The measure deﬁned in Eq. (5) is based on an
observational probability distribution that can be estimated from empirical data. Since we aim for the
empirical application of our method, we do not consider the perturbational approach in this study.
2.2. Stochastic interaction ΦSI
Second, consider the following partitioned probability distribution q,
q
 X′|X
 = ∏
i
q
 M′
i|Mi

,
(6)
which partitions the transition probability from the past X to the present X′ in the whole system into
the product of the transition probability in each subsystem. This corresponds to removing the causal
inﬂuences from Mi to M′
j (j ̸= i) as well as the equal time inﬂuences at present between M′
i and M′
j
(j ̸= i) (Fig. 1 (b)). In this case, the corresponding measure of integrated information is given by
ΦSI = ∑
i
H(M′
i|Mi) −H(X′|X),
(7)
where H(·|·) indicates the conditional entropy. This measure was proposed as a practical measure of
integrated information by Barrett & Seth [15] following the measure proposed in the second version
of IIT (IIT 2.0) [11]. This measure was also independently derived by Ay as a measure of complexity
[18,19].


## Page 5


Version February 14, 2018 submitted to Entropy
5 of 22
2.3. Geometric integrated information ΦG
Aiming at only the causal inﬂuences between parts, Oizumi et al. [12] proposed to measure
integrated information with the probability distribution that satisﬁes
q
 M′
i|X
 = q
 M′
i|Mi

, ∀i
(8)
which means the present state of a subsystem i, M′
i only depends on its past state Mi.
This
corresponds to removing only the causal inﬂuences between subsystems while retaining the
equal-time interactions between them (Fig. 1 (c)). The constraint Eq. (8) is equivalent to the Markov
condition
q(M′
i, Mc
i |Mi) = q(M′
i|Mi)q(Mc
i |Mi), ∀i
(9)
where Mc
i is the complement of Mi. This means when Mi is given, M′
i and Mc
i are independent. In
other words, the causal interaction between Mc
i and M′
i is only via Mi.
There is no closed-form expression for this measure in general. However, if the probability
distributions are Gaussian, we can analytically solve the minimization over q (see Appendix A).
3. Minimum Information Partition
In this section, we provide the mathematical deﬁnition of Minimum Information Partition (MIP).
Then, we formulate the search for MIP as an optimization problem of a set function.
The MIP
is the partition that divides a system into the least interdependent subsystems so that information
loss caused by removing interactions among the subsystems is minimized. The information loss is
quantiﬁed by the measure of integrated information. Thus, the MIP, πMIP, is deﬁned as a partition 1
where integrated information is minimized :
πMIP := arg min
π∈P
Φ(π),
(10)
where P is a set of partitions. In general, P is the universal set of partitions, including bi-partitions,
tri-partitions, and so on. In this study, however, we focus only on bi-partitions for simplicity and
computational time. By a bi-partition, a whole system Ωis divided into a subset S (S ⊂Ω, S ̸= ∅)
and its complement ¯S = Ω\ S. Since a bi-partition is uniquely determined by specifying a subset S,
integrated information can be considered as a function of a set S, Φ(S). Finding the MIP is equivalent
to ﬁnding the subset, SMIP, that achieves the minimum of integrated information:
SMIP := arg min
S⊂Ω,S̸=∅
Φ(S).
(11)
In this way, the search of the MIP is formulated as an optimization problem of a set function.
Since the number of bi-partitions for the system with N-elements is 2N−1 −1, exhaustive search
of the MIP in a large system is intractable. However, by formulating the MIP search as an optimization
of a set function as above, we can take advantage of a discrete optimization technique and can reduce
computational costs to a polynomial order, as described in the next section.
4. Submodular optimization
The submodularity is an important concept in set functions, which is an analogue of convexity
in continuous functions [29].
When objective functions are submodular, efﬁcient algorithms are
available for solving optimization problems. In particular, for symmetric submodular functions, there
1
Since the minimizer is not necessarily unique, strictly speaking, there could be multiple MIPs.


## Page 6


Version February 14, 2018 submitted to Entropy
6 of 22
is a well-known algorithm by Queyranne which minimizes them [14]. We utilize this method for
ﬁnding the MIP in this study.
4.1. Submodularity
Mathematically, the submodularity is deﬁned as follows.
Deﬁnition 1 (Submodularrity). Let Ωbe a ﬁnite set and 2Ωits power set. A set function f : 2Ω→R
is submodular if it satisﬁes the following inequality for any S, T ⊆Ω:
f(S) + f(T) ≥f(S ∪T) + f(S ∩T).
Equivalently, a set function f : 2Ω→R is submodular if it satisﬁes the following inequality for any
S, T ⊆Ωwith S ⊆T and for any u ∈Ω\ T:
f(S ∪{u}) −f(S) ≥f(T ∪{u}) −f(T).
The second inequality means that the function increases more when an element is added to a
smaller subset than when the element is added to a bigger subset.
4.2. Queyranne’s algorithm
A set function f is called symmetric if f(S) = f(Ω\ S) for any S ⊆Ω. Integrated information
Φ(S) computed by bi-partition is a symmetric function, because S and Ω\ S speciﬁes the same
bi-partition. If a function is symmetric and submodular, we can ﬁnd the minimum of the function
by Queyranne’s algorithm with O(N3) function calls [14].
4.3. Submodularity in measures of integrated information
In a previous study, Queyranne’s algorithm was utilized to ﬁnd the MIP when ΦMI is used
as the measure of integrated information [13].
As shown previously, ΦMI is submodular [13].
However, the other measures of integrated information are not submodular. In this study, we apply
Queyranne’s algorithm to non-submodular functions, ΦSI and ΦG. When the objective functions
are not submodular, Queyranne’s algorithm does not necessarily ﬁnd the MIP. We evaluate how
accurately Queyranne’s algorithm can ﬁnd the MIP when it is used for non-submodular measures of
integrated information. There is an order relation among the three measures of integrated information
[12],
ΦG ≤ΦSI ≤ΦMI.
(12)
This inequality can be graphically understood from Fig. 1. The more the connections are removed,
the larger the corresponding integrated information (the information loss) is. That is, ΦG measures
only the causal inﬂuences between subsystems, ΦSI measures the equal-time interactions between
the present states as well as the causal inﬂuences between subsystems, and ΦMI measures all the
interactions between the subsystems. Thus, ΦSI is closer to ΦMI than ΦG is. This relationship implies
that ΦSI would behave more similarly to a submodular measure ΦMI than ΦG does. Thus, one may
surmise that Queyranne’s algorithm would work more accurately for ΦSI than for ΦG. As we will
show in Subsection 6.2, this is indeed the case. However, the difference is rather small because
Queyranne’s algorithm works almost perfectly for both measures, ΦSI and ΦG.
5. Replica Exchange Markov Chain Monte Carlo Method
To evaluate the accuracy of Queyranne’s algorithm, we compare the partition found by
Queyranne’s algorithm with the MIP found by the exhaustive search when the number of elements n
is small enough (n ≲20). However, when n is large, we cannot know the MIP because the exhaustive
search is unfeasible. To evaluate the performance of Queyranne’s algorithm in a large system, we


## Page 7


Version February 14, 2018 submitted to Entropy
7 of 22
compare it with a different method, the Replica Exchange Markov Chain Monte Carlo (REMCMC)
method [21–24]. REMCMC, also known as parallel tempering, is a method to draw samples from
probability distributions.
REMCMC is an improved version of the MCMC methods.
Here, we
brieﬂy explain how the MIP search problem is represented as a problem of drawing samples from
a probability distribution. Details of the REMCMC method are given in Appendix B.
Let us deﬁne a probability distribution p(S; β) using integrated information Φ(S) as follows:
p(S; β) ∝exp(−βΦ(S)),
(13)
where β(> 0) is a parameter called inverse temperature. This probability is higher/lower when
Φ(S) is smaller/larger. The MIP gives the highest probability by deﬁnition. If we can draw samples
from this distribution, we can selectively scan subsets with low integrated information and efﬁciently
ﬁnd the MIP, compared to randomly exploring partitions independent of the value of integrated
information. Simple MCMC methods like the Metropolis method, which draw samples from Eq.
(13) with a single value of β, often suffer from the problem of slow convergence. That is, a sample
sequence is trapped in a local minimum and the sample distribution takes time to converge to the
target distribution.
REMCMC aims at overcoming this problem by drawing samples in parallel
from distributions with multiple values of β and by continually exchanging the sampled sequences
between neighboring β (See Appendix B for more details).
6. Results
We ﬁrst evaluated the performance of Queyranne’s algorithm in simulated networks.
Throughout the simulations below, we consider the case where the variable X obeys a Gaussian
distribution for the ease of computation.
As shown in Appendix A, the measures of integrated
information, ΦSI and ΦG can be analytically computed.
Note that although ΦSI and ΦG can be
computed in principle even when the distribution of X is not Gaussian, it is practically very hard to
compute them in large systems because the computation of Φ involves summation over all possible
X. Speciﬁcally, we consider the ﬁrst order autoregressive (AR) model,
X′ = AX + E,
(14)
where X and X′ are present states and past states of a system, A is the connectivity matrix, and
E is Gaussian noise. The stationary distribution of this AR model is considered. The stationary
distribution of p(X, X′) is a Gaussian distribution. The covariance matrix of p(X, X′) consists of
covariance of X, Σ(X), and cross-covariance of X and X′, Σ(X, X′). Σ(X) is computed by solving the
following equation,
Σ(X) = AΣ(X)AT + Σ(E).
(15)
Σ(X, X′) is given by
Σ(X, X′) = Σ(X)AT.
(16)
By using these covariance matrices, ΦSI and ΦG are analytically calculated [12] (see Appendix A). The
details of the parameter settings are described in each subsection.
6.1. Speed of Queyranne’s algorithm compared with exhaustive search
We ﬁrst evaluated the computation time of Queyranne’s algorithm and compared it with that
of the exhaustive search when the number of elements N changed. The connectivity matrices A
were randomly generated. Each element of the connection matrix A was sampled from a normal
distribution with mean 0 and variance 0.01/N. The covariance of Gaussian noise E was generated
from a Wishart distribution W(σI, 2N) with covariance σI and degrees of freedom 2N, where σ
corresponded to the amount of noise E and I was the identity matrix. The Wishart distribution is a
standard distribution for symmetric positive-semideﬁnite matrices [30,31]. Typically, the distribution


## Page 8


Version February 14, 2018 submitted to Entropy
8 of 22
10
0
10
1
10
2
10
-4
10
-2
10
0
10
2
10
4
10
6
10
8
10
10
10
0
10
1
10
2
10
-4
10
-2
10
0
10
2
10
4
10
6
10
8
10
10
(a)
(b)
Computational Time (sec.)
Computational Time (sec.)
Figure 2.
Computational time of Queyranne’s algorithm and the Exhaustive search.
The red
circles and the red solid lines indicate the computational time of Queyranne’s algorithm and their
approximate curves ((a) log10 T = 3.066 log10 N −3.838, (b) log10 T = 4.776 log10 N −4.255.) The
black triangles and the black dashed lines indicate the computational time of the exhaustive search
and their approximate curves ((a) log10 T = 0.2853N −3.468, (b) log10 T = 0.3132N −2.496.)
is used to generate covariance matrices and inverse covariance (precision) matrices.
For more
practical details, see for example, [31]. We set σ to 0.1. The number of elements N was changed
from 3 to 60. All computation times were measured on a machine with an Intel Xeon CPU E5-2680 at
2.70GHz. All the calculations were implemented in MATLAB.
Figure 2 (a) shows the results for ΦSI. The red circles, which indicate the computational time
of Queyranne’s algorithm, are ﬁt by the red solid line, log10 T = 3.066 log10 N −3.838. In contrast,
the black triangles, which indicate those of the exhaustive search, are ﬁt by the black dashed line,
log10 T = 0.2853N −3.468.
This means that the computational time of Queyranne’s algorithm
increases in polynomial order (T ∝N3.066), while that of the exhaustive search exponentially increases
(T ∝1.929N).
For example, when N = 100, Queyanne’s algorithm takes ∼197 sec while the
exhaustive search takes 1.16 × 1025 sec.
This is in practice impossible to compute even with a
supercomputer. Similarly, as shown in Fig. 2 (b), when ΦG is used, Queyranne’s algorithm roughly
takes T ∝N4.776 while the exhaustive search takes T ∝2.057N. Note that the reason why the order
of the computational time of Queyrannes algorithm for ΦG is higher than that for ΦSI is because the
multi-dimensional optimization is needed to compute ΦG (see Appendix A).
6.2. Accuracy of Queyranne’s algorithm
We evaluated the accuracy of Queyranne’s algorithm by comparing the partition found by
Queyranne’s algorithm with the MIP found by exhaustive search.
We used ΦSI and ΦG as the
measures of integrated information. We considered two different architectures in connectivity matrix
A of AR models. The ﬁrst one was just a random matrix: Each element of A was randomly sampled
from a normal distribution with mean 0 and variance 0.01/N. The other one was a block matrix
consisting of N/2 by N/2 sub-matrices, Aij(i, j = 1, 2). Each element of diagonal sub-matrices A11
and A22 was drawn from a normal distribution with mean 0 and variance 0.02/N. Off-diagonal


## Page 9


Version February 14, 2018 submitted to Entropy
9 of 22
Table 1. Accuracy of Queyranne’s algorithm
Model
ΦSI
ΦG
A
σ
CR
RA
ER
CORR
CR
RA
ER
CORR
Normal
0.01
100%
1
0
1
100%
1
0
1
0.1
100%
1
0
1
100%
1
0
1
Block
0.01
100%
1
0
1
97%
1.05
2.38e-3
0.978
0.1
100%
1
0
1
97%
1.03
9.11e-4
0.978
sub-matrices A12 and A21 were zero matrices. The covariance of Gaussian noise E in the AR model
was generated from a Wishart distribution W(σI, 2N). The parameter σ was set to 0.1 or 0.01. The
number of elements N was set to 14.
We randomly generated 100 connectivity matrices A and
Σ(E) for each setting and evaluated performance using the following four measures. The following
measures are averaged over 100 trials.
Correct rate (CR) Correct rate (CR) is the rate of correctly ﬁnding the MIP.
Rank (RA) Rank (RA) is the rank of the partition found by Queyranne’s algorithm among all possible
partitions. The rank is based on the Φ values computed at each partition. The partition that
gives the lowest Φ is rank 1. The highest rank is equal to the number of possible bi-partitions,
2N−1.
Error ratio (ER) Error ratio (ER) is the deviation of the value of integrated information computed
across the partition found by Queyranne’s algorithm from that computed across the MIP, which
is normalized by the mean error computed at all possible partitions. Error ratio is deﬁned by
Error Ratio = ΦQ −ΦMIP
¯Φ −ΦMIP
,
(17)
where ΦMIP, ΦQ, and ¯Φ are the amount of integrated information computed across the MIP, that
computed across the partition found by Queyranne’s algorithm, and the mean of the amounts
of integrated information computed across all possible partitions, respectively.
Correlation (CORR) Correlation (CORR) is the correlation between the partition found by
Queyranne’s algorithm and the MIP found by the exhaustive search.
Let us represent a
bi-partition of N-elements as an N-dimensional vector σ = (σ1, . . . , σN) ∈{−1, 1}N, where ±1
indicates one of the two subgroups. The absolute value of the correlation between the vector
given by the MIP (σMIP) and that given by the partition found by Queyranne’s algorithm (σQ)
is computed:
|corr(σMIP, σQ)| =

∑N
i=1(σMIP
i
−¯σMIP)(σQ
i −¯σQ)
q
∑N
i=1(σMIP
i
−¯σMIP)2 ∑N
i=1(σQ
i −¯σQ)2

,
(18)
where ¯σMIP and ¯σQ are the means of σMIP
i
and σQ
i , respectively.
The results are summarized in Table 1. This table shows that, when ΦSI was used, Queyranne’s
algorithm perfectly found the MIPs for all 100 trials, even though ΦSI is not strictly submodular.
Similarly, when ΦG was used, Queyranne’s algorithm almost perfectly found the MIPs. The correct
rate was 100% for the normal models and 97% for the block structured models. Additionally, even
when the algorithm missed the MIP, the rank of the partition found by the algorithm was 2 or 3. The
averaged rank over 100 trials were 1.03 and 1.05 for the block structured models. Also, the error ratio
in error trials were around 0.1 and the average error ratios were very small. See Appendix C for box
plots of the values of the integrated information at all the partitions. Thus, such miss trials would not


## Page 10


Version February 14, 2018 submitted to Entropy
10 of 22
affect evaluation of the amount of integrated information in practice. However, in terms of partitions,
the partitions found by Queyranne’s algorithm in error trials were markedly different from the MIPs.
In the block structured model, the MIP for ΦG was the partition that split the system in halves. In
contrast, the partitions found by Queyranne’s algorithm were one-vs-all partitions.
In summary, Queyranne’s algorithm perfectly worked for ΦSI. With regards to ΦG, although
Queyranne’s algorithm almost perfectly evaluated the amount of integrated information, we may
need to treat partitions found by the algorithm carefully.
This slight difference in performance
between ΦSI and ΦG can be explained by the order relation Eq. (12). ΦSI is closer to the strictly
submodular function ΦMI than ΦG is, which we consider to be why Queyranne’s algorithm worked
better for ΦSI than ΦG.
6.3. Comparison between Queyranne’s algorithm and REMCMC
Table 2. Comparison of Queyranne’s algorithm with REMCMC (ΦSI, N = 50)
Model
Winning percentage
Number of evaluations of Φ
REMCMC (mean±std)
A
σ
Queyranne’s
Even
REMCMC
Queyranne’s
Converged
Solution found
Normal
0.01
0%
100%
0%
41,699
274,257±107,969
8,172.6±6,291.0
0.1
0%
100%
0%
41,699
315,050±112,205
9,084.9±7,676.4
Block
0.01
0%
100%
0%
41,699
308,976±110,905
7,305.6±6,197.0
0.1
0%
100%
0%
41,699
339,869±154,161
4,533.4±3,004.8
Table 3. Comparison of Queyranne’s algorithm with REMCMC (ΦG, N = 20)
Model
Winning percentage
Number of evaluations of Φ
REMCMC (mean±std)
A
σ
Queyranne’s
Even
REMCMC
Queyranne’s
Converged
Solution found
Normal
0.01
0%
100%
0%
2,679
136,271±46,624
862.4±776.3
0.1
0%
100%
0%
2,679
122,202±46,795
894.3±780.2
Block
0.01
0%
100%
0%
2,679
129,770±88,483
245.2±194.3
0.1
0%
100%
0%
2,679
146,034±61,880
443.2±642.1
We evaluated the performance of Queyranne’s algorithm in large systems where an exhaustive
search is impossible. We compared it with the Replica Exchange Markov Chain Monte Carlo Method
(REMCMC). We applied the two algorithms to AR models generated similarly as in the previous
section. The number of elements was 50 for ΦSI and 20 for ΦG, respectively. The reason for the
difference in N is because ΦG requires much heavier computation than ΦSI (see Appendix A). We
randomly generated 20 connectivity matrices A and Σ(E) for each setting. We compared the two
algorithms in terms of the amount of integrated information and the number of evaluations of Φ.
REMCMC was run until a convergence criterion was satisﬁed. See Appendix B.3 for details of the
convergence criterion.
The results are shown in Tables 2 and 3. “Winning percentage” indicates the fraction of trials
each algorithm won in terms of the amount of integrated information at the partition found by
each algorithm. We can see that the partitions found by the two algorithms exactly matched for
all the trials.
We consider that the algorithms probably found the MIPs for the following three
reasons.
First, it is well known that REMCMC can ﬁnd a minima if it is run for a sufﬁciently


## Page 11


Version February 14, 2018 submitted to Entropy
11 of 22
long time in many applications [24,32–34]. Second, the two algorithms are so different that it is
unlikely that they both incorrectly identiﬁed the same partitions as the MIPs. Third, Queyranne’s
algorithm successfully ﬁnds the MIPs in smaller systems as shown in the previous section. This fact
suggests that Queyranne’s algorithm worked well also for the larger systems. Note that in the case
of ΦG, the half-and-half partition is the MIP in the block structured model because ΦG = 0 under
the half-and-half partition. We conﬁrmed that the partitions found by Queyanne’s algorithm and
REMCMC were both the half-and-half partition for all the 20 trials. Thus, in the block structured
case, it is certain that the true MIPs were successfully found by both algorithms.
We also evaluated the number of evaluations of Φ in both algorithms before the end of the
computational processes. In our simulations, the computational process of Queyranne’s algorithm
ended much faster than the convergence of REMCMC. Queyranne’s algorithm ends at a ﬁxed
number of evaluations of Φ depending only on N. In contrast, the number of the evaluations before
the convergence of REMCMC depends on many factors such as the network models, the initial
conditions, and pseudo random number sequences. Thus, the time of convergence varies among
different trials. Note that by “retrospectively” examining the sequence of the Monte Carlo search,
the solutions turned out to be found at earlier points of the Monte Carlo searches than Queyranne’s
algorithm (which are indicated as “solution found” in Tables 2 and 3). However, it is impossible to
stop the REMCMC algorithm at these points where the solutions were found because there is no way
to tell whether these points reach the solution until the algorithm is run for enough amount of time.
6.4. Evaluation with real neural data
Finally, to ensure the applicability of Queyranne’s algorithm to real neural data, we similarly
evaluated the performance with electrocorticogram (ECoG) data recorded in a macaque monkey. The
dataset is available at an open database, Neurotycho.org (http://neurotycho.org/). One hundred and
twenty-eight channel ECoG electrodes were implanted in the left hemisphere. The electrodes were
placed at 5-mm intervals, covering the frontal, parietal, temporal, and occipital lobes, and medial
frontal and parietal walls. Signals were sampled at a rate of 1 kHz and down-sampled to 100 Hz for
the analysis. The monkey “Chibi” was awake with the eyes covered by an eye-mask to restrain visual
responses. To remove line noise and artifacts, we performed bipolar re-referencing between nearest
neighbor electrode pairs. The number of re-referenced electrodes was 64 in total.
In the ﬁrst simulation, we evaluated the accuracy. We extracted a 1-minute length of the signals
of the 64 electrodes. Each 1-minute sequence consists of 100 Hz × 60 sec. = 6000 samples. Then,
we randomly selected 14 electrodes 100 times. We approximated the probability distribution of the
signals with multivariate Gaussian distributions. The covariance matrices were computed with a
time window of 1 min and a time step of 10 ms. We applied the algorithms to the 100 randomly
selected sets of electrodes and measured the accuracy similarly as in Subsection 6.2. The results are
summarized in Table 4. We can see that Queyranne’s algorithm worked perfectly for both ΦSI and
ΦG.
Next, we compared Queyranne’s algorithm with REMCMC. We applied the two algorithms to
the 64 re-referenced signals, and evaluated the performance in terms of the amount of integrated
information and the number of evaluations of Φ, as in Subsection 6.3.
We segmented 15
non-overlapping sequences of 1 minute each, and computed covariance matrices with a time step
of 10 ms. We measured the average performance over the 15 sets. Here, we only used ΦSI, because
ΦG requires heavy computations for 64 dimensional systems. The results are shown in Table 5. We
can see that the partitions selected by the two algorithms matched for all 15 sequences. In terms
of the amount of computation, Queyranne’s algorithm ended much faster than the convergence of
REMCMC.


## Page 12


Version February 14, 2018 submitted to Entropy
12 of 22
Table 4. Accuracy of Queyranne’s algorithm in ECoG data. Randomly-selected 14 electrodes were
used.
ΦSI
ΦG
CR
RA
ER
CORR
CR
RA
ER
CORR
100%
1
0
1
100%
1
0
1
Table 5. Comparison of Queyranne’s algorithm with REMCMC in ECoG data (SI)
Winning percentage
Number of evaluations of Φ
REMCMC (mean±std)
Queyranne’s
Even
REMCMC
Queyranne’s
Converged
Solution found
0%
100%
0%
87,423
607,797±410,588
15,859±10,497
7. Discussions
In this study, we proposed an efﬁcient algorithm for searching for the Minimum Information
Partition (MIP) in Integrated Information Theory (IIT). The computational time of an exhaustive
search for the MIP grows exponentially with the arithmetic growth of system size, which has been
an obstacle to applying IIT to experimental data.
We showed here that by using a submodular
optimization algorithm called Queyranne’s algorithm, the computational time was reduced to
O(N3.066) and O(N4.776) for stochastic interaction ΦSI and geometric integrated information ΦG,
respectively. These two measures of integrated information are non-submodular, and thus it is not
theoretically guaranteed that Queyranne’s algorithm will ﬁnd the MIP. We empirically evaluated
the accuracy of the algorithm by comparing it with an exhaustive search in simulated data and in
ECoG data recorded from monkeys. We found that Queyranne’s algorithm worked perfectly for ΦSI
and almost perfectly for ΦG. We also tested the performance of Queyranne’s algorithm in larger
systems (N = 20 and 50 for ΦSI and ΦG, respectively) where the exhaustive search is intractable
by comparing it with the Replica Exchange Markov Chain Monte Carlo method (REMCMC). We
found that the partitions found by these two algorithms perfectly matched, which suggests that both
algorithms most likely found the MIPs. In terms of the computational time, the number of evaluations
of Φ taken by Queyranne’s algorithm was much smaller than that taken by REMCMC before the
convergence. Our results indicate that Queyranne’s algorithm can be utilized to effectively estimate
MIP even for non-submodular measures of integrated information. Although the MIP is a concept
originally proposed in IIT for understanding consciousness, it can be utilized to general network
analysis irrespective of consciousness. Thus, the method for searching MIP proposed in this study
will be beneﬁcial not only for consciousness studies but for other research ﬁelds.
Here, we discuss the pros and cons of Queyranne’s algorithm in comparison with REMCMC.
Since the partitions found by both algorithms perfectly matched in our experiments, they were
equally good in terms of accuracy.
With regards to computational time, Queyranne’s algorithm
ended much faster than the convergence of REMCMC. Thus, Queyranne’s algorithm would be a
better choice in rather large systems (N ∼20 and 50 for ΦSI and ΦG, respectively). Note that if
we retrospectively examine the sampling sequence in REMCMC, we ﬁnd that REMCMC found the
partitions much earlier than its convergence and that the estimated MIPs did not change in the later
parts of sampling process. Thus, if we could introduce a heuristic criterion to determine when to
stop the sampling based on the time course of the estimated MIPs, REMCMC could be stopped
earlier than its convergence. However, setting such a heuristic criterion is a non-trivial problem.
Queyranne’s algorithm ends within a ﬁxed number of function calls regardless of the properties of


## Page 13


Version February 14, 2018 submitted to Entropy
13 of 22
data. If the system size is much larger (N ≳100), Queyranne’s algorithm will be computationally very
demanding because of O(N3) time complexity and may not practically work. In that case, REMCMC
would work better if the above-mentioned heuristics are introduced to stop the algorithm earlier than
the convergence.
As an alternative interesting approach for approximately ﬁnding the MIP, a graph-based
algorithm was proposed by Toker & Sommer [35]. In their method, to reduce the search space,
candidate partitions are selected by a spectral clustering method based on correlation. Then ΦG is
calculated for those candidate partitions, and the best partition is selected. A difference between our
method and theirs is whether the search method is fully based on the values of integrated information
or not. Our method uses no other quantities than Φ for searching the MIP, while their method uses
a graph theoretic measure, which may signiﬁcantly differ from Φ in some cases. It would be an
interesting future work to compare our method and the graph-theoretic methods or combine these
methods to develop better search algorithms.
In this study, we considered the three different measures of integrated information, ΦMI, ΦSI, and
ΦG. Of these, ΦMI is submodular but the other two measures, ΦSI and ΦG, are not. As we described
in Section 4.3, there is a clear order relation among them (Eq. (12)). ΦSI is closer to a submodular
function ΦMI than ΦG is. This relation implies that Queyranne’s algorithm would work better for
ΦSI than for ΦG. We found that it was actually the case in our experiments because there were a few
error trials for ΦG whereas there were no miss trials for ΦSI. For the practical use of these measures,
we note that there are two major differences among the three measures. One is what they quantify.
As shown in Fig. 1, ΦG measures only causal interactions between units across different time points.
In contrast, ΦSI and ΦMI also measure equal time interactions as well as causal interactions. ΦG
best follows the original concept of IIT in the sense that it measures only the “causal” interactions.
One needs to acknowledge the theoretical difference whenever applying one of these measures in
order to correctly interpret the obtained results. The other difference is in computational costs. The
computational costs of ΦMI and ΦSI are almost the same while that of ΦG is much larger, because
it requires multi-dimensional optimization. Thus, ΦG may not be practical for the analysis of large
systems. In that case, ΦMI or ΦSI may be used instead with care taken of the theoretical difference.
Although in this study we focused on bi-partitions, Queyranne’s algorithm can be extended
to higher-order partitions [13]. However, the algorithm becomes computationally demanding for
higher-order partitions, because the computational complexity of the algorithm for K-partitions is
O(N3(K−1)). This is the main reason why we focused on bi-partitions. Another reason is that there has
not been an established way to fairly compare partitions with different K. In IIT 2.0, it was proposed
that the integrated information should be normalized by the minimum of the entropy of partitioned
subsystems [3], while in IIT 3.0, it was not normalized [4]. Note that when integrated information
is not normalized, the MIP is always found in bi-partitions because integrated information becomes
larger when a system is partitioned into more subsystems.
Whether the integrated information should be normalized and how the integrated information
should be normalized are still open questions. In our study, the normalization used in IIT 2.0 is
not appropriate, because the entropy can be negative for continuous random variables. Additionally,
regardless of whether random variables are continuous or discrete, normalization signiﬁcantly affects
the submodularity of the measures of integrated information. For example, if we use normalization
proposed in IIT 2.0, even the submodular measure of integrated information, ΦMI, no longer satisﬁes
submodularity. Thus, Queyranne’s algorithm may not work well if Φ is normalized.
Although we resolved one of the major computational difﬁculties in IIT, an additional issue still
remains. Searching for the MIP is an intermediate step in identifying the informational core, called
the “complex”. The complex is the subnetwork in which integrated information is maximized, and is
hypothesized to be the locus of consciousness in IIT. Identifying the complex is also represented as a
discrete optimization problem which requires exponentially large computational costs. Queyranne’s
algorithm cannot be applied to the search for the complex because we cannot formulate it as a


## Page 14


Version February 14, 2018 submitted to Entropy
14 of 22
submodular optimization. We expect that REMCMC would be efﬁcient in searching for the complex
and will investigate its performance in a future study.
An important limitation of this study is that we only showed the nearly perfect performance
of Queyranne’s algorithm in limited simulated data and real neural data. In general, we cannot tell
whether Queyranne’s algorithm works well for other data beforehand. For real data analysis, we
recommend that the procedure below should be applied. First, as we did in Section 6.2, accuracy
should be checked by comparing it with the exhaustive search in small randomly selected subsets.
Next, if it works well, the performance should be checked by comparing it with REMCMC in
relatively large subsets, as we did in Section 6.3. If Queyranne’s algorithm works better than or
equally as well as REMCMC, it is reasonable to use Queyranne’s algorithm for the analysis. By
applying this procedure, we expect that Queyranne’s algorithm could be utilized to efﬁciently ﬁnd
the MIP in a wide range of time series data.
Acknowledgments: We thank Dr. Shohei Hidaka, Japan Advanced Institute of Science and Technology, for
providing us Queyranne’s algorithm codes. This work was partially supported by JST CREST Grant Number
JPMJCR15E2, Japan.
Author Contributions: J.K. and M.O. conceived and designed the experiments; J.K. performed the experiments;
J.K. and M.O. analyzed the data; and J.K., R.K. and M.O. wrote the paper.
Conﬂicts of Interest: The authors declare no conﬂict of interest. The founding sponsors had no role in the design
of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript, or in the
decision to publish the results.
Abbreviations
The following abbreviations are used in this manuscript:
IIT: integrated information theory
MIP: minimum information partition
MCMC: Markov chain Monte Carlo
REMCMC: replica exchange Markov chain Monte Carlo
ECoG: electrocorticogram
AR: autoregressive
CR: correct rate
RA: rank
ER: error ratio
CORR: correlation
MCS: Monte Carlo step
Appendix A. Analytical formula of Φ for Gaussian variables
We describe the analytical formula of three measures of integrated information, multi
information (ΦMI), stochastic interaction (ΦSI) and geometric integrated information (ΦG), when
the probability distribution is Gaussian.
For more details about the theoretical background, see
[12,15,18,19].
First, let us introduce the notation. We consider a stochastic dynamical system consisting of N
elements. We represent the past and present states of the system as X = (X1, . . . , XN) and X′ =
(X′
1, . . . , X′
N), respectively, and deﬁne a joint vector
˜X = (X, X′).
(19)
We assume that the joint probability distribution p (X, X′) is Gaussian:
p
 x, x′ = exp

−1
2

˜xTΣ( ˜X) ˜x −ψ

,
(20)


## Page 15


Version February 14, 2018 submitted to Entropy
15 of 22
where ψ is the normalizing factor and Σ( ˜X) is the covariance matrix of ˜X. Note that we can assume
the mean of the Gaussian distribution is zero without loss of generality because the mean value does
not affect the values of integrated information. This covariance matrix Σ( ˜X) is given by
Σ( ˜X) =
 
Σ(X)
Σ(X, X′)
Σ(X, X′)T
Σ(X′)
!
,
(21)
where Σ(X) and Σ(X′) are the equal time covariance at past and present, respectively, and Σ(X, X′)
is the cross covariance between X and X′. Below we will show the analytical expression of ΦMI, ΦSI
and ΦG.
Appendix A.1. Multi information
Let us consider the following partitioned probability distribution q,
q
 X, X′ = ∏
i
q
 Mi, M′
i

,
(22)
where Mi and M′
i are the past and present states of i-th subsystem. Then multi information is deﬁned
as
ΦMI = ∑
i
H(Mi, M′
i) −H(X, X′).
(23)
When the distribution is Gaussian, Eq. (23) is transformed to
ΦMI = ∑
i
log |Σ( ˜Mi)| −log |Σ( ˜X)|,
(24)
where ˜Mi = (Mi, M′
i) and Σ( ˜Mi) is the covariance of ˜Mi.
Appendix A.2. Stochastic interaction
We consider the following partitioned probability distribution q,
q
 X′|X
 = ∏
i
q
 M′
i|Mi

.
(25)
Then stochastic interaction [12,15,18,19] is deﬁned as
ΦSI = ∑
i
H(M′
i|Mi) −H(X′|X).
(26)
When the distribution is Gaussian, Eq. (26) is transformed to
ΦSI = ∑
i
log |Σ(M′
i|Mi)| −log |Σ(X′|X)|,
(27)
where Σ(M′
i|Mi) and Σ(X′|X) are covariance matrices of conditional distributions. These matrices
are represented as
Σ(M′
i|Mi) = Σ(M′
i) −Σ(Mi, M′
i)TΣ(Mi)−1Σ(Mi, M′
i),
Σ(X′|X) = Σ(X′) −Σ(X, X′)TΣ(X)−1Σ(X, X′),
(28)
where Σ(Mi) and Σ(M′
i) are the equal time covariance of subsystem i at past and present, respectively,
and Σ(Mi, M′
i) is the cross covariance between Mi and M′
i.


## Page 16


Version February 14, 2018 submitted to Entropy
16 of 22
Appendix A.3. Geometric integrated information
To calculate the geometric integrated information [12], we ﬁrst transform Eq. (20). Equation 20
is equivalently represented as an autoregressive model:
X′ = AX + E,
(29)
where A is the connectivity matrix and E is Gaussian random variables, which are uncorrelated over
time. By using this autoregressive model, the joint distribution p (X, X′) is expressed as
p
 x, x′ = exp

−1
2

xTΣ(X)x + (x′ −Ax)TΣ(E)−1(x′ −Ax) −ψ

,
(30)
and the covariance matrices as
Σ(X, X′) = Σ(X)AT,
Σ(X′) = Σ(E) + AΣ(X)AT,
(31)
where Σ(E) is the covariance of E. Similarly, the joint probability distribution in a partitioned model
is given by
q
 x, x′ = exp

−1
2

˜xTΣ( ˜X)p ˜x −ψ

= exp

−1
2

xTΣ(X)px + (x′ −Apx)TΣ(E)−1
p (x′ −Apx) −ψ

,
(32)
where Σ(X)p and Σ(E)p are the covariance matrices of X and E in the partitioned model, respectively,
and Ap is the connectivity matrix in the partitioned model.
The geometric integrated information is deﬁned as
ΦG = min
q
DKL
 p
 X, X′ ||q
 X, X′
,
(33)
DKL
 p
 X, X′ ||q
 X, X′ = 1
2
 
log |Σ( ˜X)p|
|Σ( ˜X)| + Tr(Σ( ˜X)Σ( ˜Xp)−1) −2N
!
,
(34)
such that
q
 M′
i|X
 = q
 M′
i|Mi

, ∀i.
(35)
This constraint (Eq. (35)) corresponds to setting the between-subsystem blocks of Ap to 0:
(Ap)ij = 0 (i ̸= j).
(36)
By transforming stationary point conditions, ∂DKL/∂Σ( ˜X)−1
p
=
0, ∂DKL/∂(Ap)ii
=
0, and
∂DKL/∂Σ(E)−1
p
= 0, we get
Σ(X)p = Σ(X),
(37)
(Σ(X)(A −Ap)Σ(E)−1
p )ii = 0,
(38)
Σ(E)p = Σ(E) + (A −Ap)Σ(X)(A −Ap)T.
(39)
By substituting Eqs. (37) and (39) into Eq. (33), ΦG is simpliﬁed as
ΦG = 1
2 log |Σ(E)p|
|Σ(E)| .
(40)


## Page 17


Version February 14, 2018 submitted to Entropy
17 of 22
To obtain the value of Eq. (40), we need to ﬁnd the value of Σ(E)p, which requires solving Eqs. (37),
(38) and (39). Thus, the calculation of ΦG requires solving multi-dimensional equations. The MALAB
codes for this computation of ΦG are available at [36].
Appendix B. Details of Replica Exchange Markov Chain Monte Carlo Method
The Replica Exchange Markov Chain Monte Carlo (REMCMC) method was originally proposed
to investigate physical systems [21–23], and was then rapidly utilized in other applications, including
combinatorial optimization problems [32–34,37,38]. For a more detailed history of REMCMC, see, for
example, [24].
We ﬁrst brieﬂy explain how the MIP search problem is dealt with by the Metropolis method.
Then, as an improvement of Metropolis method, we introduce REMCMC to more effectively search
for the global minimum while avoiding being trapped around at a local minimum. Next, we describe
the convergence criterion of MCMC sampling.
Finally we present the parameter settings in our
experiments.
Appendix B.1. Metropolis method
We consider the way to sample subsets from the probability distribution Eq. (13). An initial
subset S(0) is randomly selected, and then a sample sequence is drawn as follows.
Propose a candidate of the next sample An element e is randomly selected and if it is in the current
subset S(t), the candidate Sc is S(t) \ {e}. If not, the candidate is S(t) ∪{e}.
Determine whether to accept the candidate or not The candidate Sc is accepted (S(t+1) = Sc) or not
accepted (S(t+1) = S(t)) according to the following probability a(S(t) →Sc):
a(S(t) →Sc) = min(1, r),
r = p(Sc; β)
p(S(t); β) = exp
h
β
n
Φ(S(t)) −Φ(Sc)
oi
.
(41)
This probability means that if the integrated information decreases by stepping from S(t) to Sc,
the candidate Sc is always accepted, and otherwise it is accepted with the probability r.
By iterating these two steps with sufﬁcient time, the sample distribution converges to the probability
distribution given in Eq. (13). N steps of the sampling is referred to as one Monte Carlo step (MCS),
where N is the number of elements. In one MCS, each element is attempted to be added or removed
once on average.
Depending on the value of β, the behavior of the sample sequence changes. If β is small, the
probability distribution given by Eq. (13) is close to a uniform distribution and subsets are sampled
nearly independently of the value of Φ(S). If β is large, the candidate is more likely to be accepted
when the integrated information decreases. The sample sequence easily falls to a local minimum and
cannot explore many subsets. Thus, smaller and larger β have an advantage and a disadvantage:
Smaller β is better for exploring around many subsets while larger β is better for ﬁnding a (local)
minimum. In the Metropolis method, we need to set β to an appropriate value taking account of this
trade-off, but it is generally difﬁcult.
Appendix B.2. Replica Exchange Markov chain Monte Carlo
To overcome the difﬁculty in setting inverse temperature β,
REMCMC samples from
distributions at multiple values of β in parallel and the sampled sequences are exchanged between
nearby values of β. By this exchange, the sampled sequences at high inverse temperatures can escape
from local minima and can explore many subsets.


## Page 18


Version February 14, 2018 submitted to Entropy
18 of 22
We consider M-probabilities at different inverse temperatures β1 > β2 > · · · > βM and
introduce the following joint probability:
p(S1, . . . , SM; β1 . . . βM) =
M
∏
m=1
p(Sm; βm).
(42)
Then, the simulation process of the REMCMC consists of the following two steps.
Sampling from each distribution Samples are drawn from each distribution p(Sm; βm) separately
by using the Metropolis method as described in the previous subsection.
Exchange between neighboring inverse temperatures After a given number of samples are drawn,
subsets at neighboring inverse temperatures are swapped, according to the following
probability p(Sm ↔Sm+1):
p(Sm ↔Sm+1) = min(1, r′),
r′ = p(Sm+1; βm)p(Sm; βm+1)
p(Sm; βm)p(Sm+1; βm+1)
= exp [(βm+1 −βm) {Φ(Sm+1) −Φ(Sm)}] .
(43)
This probability indicates that if the integrated information at a higher inverse temperature is
larger than that at a lower inverse temperature, subsets are always swapped; and otherwise,
they are swapped with the probability r′.
By iterating these two steps for sufﬁcient time, the sample distribution converges to the joint
distribution Eq. (42).
To maximize the efﬁciency of the REMCMC, it is important to appropriately set the multiple
inverse temperatures. If the neighboring temperatures are far apart, the acceptance ratio of exchange
(Eq. (43)) becomes too small. The REMCMC is then reduced to just separately simulating distributions
at different temperatures without any exchange. In a previous study [39], it was recommended
to keep the average ratio higher than 0.2 for every temperature pair.
At the same time, the
highest/lowest inverse temperatures should be high/low enough so that sample sequence at the
highest inverse temperature can reach the tips of (local) minima and that at the lowest one can search
around many subsets. To satisfy these constraints, a sufﬁcient number M of inverse temperatures are
accommodated and the inverse temperatures are optimized to equalize the average of the acceptance
ratio of exchanges at all temperature pairs [39–43]. Details of temperature setting are described below.
Initial setting
Inverse temperatures βm(m = 1, . . . , M) are initially set as follows. First, a subset is randomly
selected for each m. Then, a randomly chosen element is added to or eliminated from each subset,
and the absolute value of the change ∆Φm in the amount of integrated information is taken. By using
these absolute values, the highest and lowest inverse temperatures are determined by a bisection
method so that the respective averages of the acceptance ratio exp(−β∆Φ1) and exp(−β∆ΦM) match
the predeﬁned values. The intermediate inverse temperatures are set to be a geometric progression:
βm = β1
 βM
β1
 m−1
M−1 .
Updating
The difference in the amount of integrated information between the candidate subset Φ(Sc)
and the current subset Φ(S(t)) is stored when the difference is positive (Φ(Sc) −Φ(S(t)) ≥0).
Then, by using the stored values at all the inverse temperatures, the highest and lowest inverse
temperatures are determined by a bisection method so that the average of the acceptance ratio
exp
h
β
n
Φ(S(t)) −Φ(Sc)
oi
matches the predeﬁned value, as in the initial setting. The intermediate


## Page 19


Version February 14, 2018 submitted to Entropy
19 of 22
inverse temperatures are set to approximately equalize the expected values of acceptance ratio of
the exchange at all temperature pairs [39–43]. The expected value is represented as a sum of two
probabilities:
E [p(Sm ↔Sm+1)] =
Z ∞
−∞
Z ∞
−∞

p(Φm ≥Φm+1)
+p(Φm < Φm+1)e(βm−βm+1)(Φm−Φm+1)o
dΦmdΦm+1.
(44)
In [43], this expected value is approximated as
E [p(Sm ↔Sm+1)] ≈1
2erfc
 
µ(Tm+1) −µ(Tm)
p
2 {σ2(Tm+1) + σ2(Tm)}
!
+
(
1 −1
2erfc
 
µ(Tm+1) −µ(Tm)
p
2 {σ2(Tm+1) + σ2(Tm)}
!)
e(βm−βm+1)(µ(Tm)−µ(Tm+1)),
(45)
where µ(T) and σ2(T) are the mean and variance of Φ, represented as functions of temperature T.
In [43], these functions are given by interpolating the sample mean and variance. In this study,
these functions are estimated using regression, because the sample mean and variance are highly
variable. The mean and variance at each temperature are computed at every update, and these
means and variances are regressed on temperature using a continuous piecewise linear function, the
T-axis of anchor points of which are current temperatures. The anchor points are interpolated using
piecewise cubic Hermite interpolating polynomials. Then, to roughly equalize the expected values of
the acceptance ratio of the exchange at all temperature pairs, we minimize the following cost function
by varying temperatures [43]:
Cost =
M−1
∑
m=1
E [p(Sm ↔Sm+1)]−4 .
(46)
The minimization is performed by a line-search method.
Appendix B.3. Convergence criterion
One of the most commonly used MCMC convergence criteria is potential scale reduction factor
(PSRF), which was proposed by Gelman & Rubin (1992) [44], and modiﬁed by Brooks & Gelman
(1998) [45]. In this criterion, multiple MCMC sequences are run. If all of them converge, statistics of
the sequences must be about the same. This is assessed by comparing between-sequence variance and
within-sequence variance of a random variable and calculating the PSRF, ˆRc. Large ˆRc suggests that
some of the sequences do not converge yet. If ˆRc is close to 1, we can diagnose them as converged.
In this study, we cut the sequence at each inverse temperature into the former and the latter halves,
and applied the criterion to these two half sequences. If ˆRc of all the temperatures were below a
predeﬁned threshold, we regarded the sequences as converged.
Appendix B.4. Parameter settings
The number of inverse temperatures M was ﬁxed at 6 throughout out the experiments. The
highest/lowest inverse temperatures were set so that the averages of acceptance ratio become 0.01
and 0.5, respectively.
The exchange process was done every 5 MCSs.
The update of inverse
temperatures was performed every 5 MCSs for the 200 initial MCSs. The threshold of ˆRc was set
to 1.01. When computing ˆRc, we discarded the ﬁrst 200 MCSs as a burn-in period and started to
computing it after 300 MCSs.


## Page 20


Version February 14, 2018 submitted to Entropy
20 of 22
Appendix C. Values of Φ
We show some examples of the distributions of the values of Φ in the experiments in Subsection
6.2. Figures 3 (a) and (b) are the box plots of ΦSI and ΦG for the block-structured models at σ = 0.01,
respectively. We can see that in Fig. 3 (a), ΦSI computed at the partition found by Queyranne’s
algorithm perfectly matched with that at the MIPs. In Fig. 3 (b), ΦG computed at the partition found
by Queyeranne’s algorithm did not match that at the MIPs in 3 trials (the trial numbers 11, 54 and 83)
but the deviations were very small.
Bibliography
1.
Tononi, G.; Sporns, O.; Edelman, G.M. A measure for brain complexity: relating functional segregation
and integration in the nervous system. Proc. Natl. Acad. Sci. U. S. A. 1994, 91, 5033–7.
2.
Tononi, G. An information integration theory of consciousness. BMC Neurosci. 2004, 5, 42.
3.
Tononi, G. Consciousness as integrated information: a provisional manifesto. The Biological Bulletin 2008,
215, 216–242.
4.
Oizumi, M.; Albantakis, L.; Tononi, G. From the phenomenology to the mechanisms of consciousness:
integrated information theory 3.0. PLoS Comput. Biol. 2014, 10, e1003588.
5.
Massimini, M.; Ferrarelli, F.; Huber, R.; Esser, S.K.; Singh, H.; Tononi, G. Breakdown of cortical effective
connectivity during sleep. Science 2005, 309, 2228–2232.
6.
Casali, A.G.; Gosseries, O.; Rosanova, M.; Boly, M.; Sarasso, S.; Casali, K.R.; Casarotto, S.; Bruno, M.A.;
Laureys, S.; Tononi, G.; Massimini, M.
A theoretically based index of consciousness independent of
sensory processing and behavior. Sci. Transl. Med. 2013, 5, 198ra105.
7.
Lee, U.; Mashour, G.A.; Kim, S.; Noh, G.J.; Choi, B.M.
Propofol induction reduces the capacity for
neural information integration: implications for the mechanism of consciousness and general anesthesia.
Consciousness and cognition 2009, 18, 56–64.
8.
Chang, J.Y.; Pigorini, A.; Massimini, M.; Tononi, G.; Nobili, L.; Van Veen, B.D. Multivariate autoregressive
models with exogenous inputs for intracerebral responses to direct electrical stimulation of the human
brain. Frontiers in human neuroscience 2012, 6.
9.
Boly, M.; Sasai, S.; Gosseries, O.; Oizumi, M.; Casali, A.; Massimini, M.; Tononi, G.
Stimulus set
meaningfulness and neurophysiological differentiation: a functional magnetic resonance imaging study.
PLoS One 2015, 10, e0125337.
10.
Haun, A.M.; Oizumi, M.; Kovach, C.K.; Kawasaki, H.; Oya, H.; Howard, M.A.; Adolphs, R.; Tsuchiya, N.
Conscious Perception as Integrated Information Patterns in Human Electrocorticography. eNeuro 2017,
4, ENEURO–0085.
11.
Balduzzi, D.; Tononi, G. Integrated information in discrete dynamical systems: motivation and theoretical
framework. PLoS Comput. Biol. 2008, 4, e1000091.
12.
Oizumi, M.; Tsuchiya, N.; Amari, S.i.
Uniﬁed framework for information integration based on
information geometry. Proceedings of the National Academy of Sciences 2016, 113, 14817–14822.
13.
Hidaka, S.; Oizumi, M. Fast and exact search for the partition with minimal information loss.
arXiv
preprint 2017.
14.
Queyranne, M. Minimizing symmetric submodular functions. Mathematical Programming 1998, 82, 3–12.
15.
Barrett, A.B.; Barnett, L.; Seth, A.K. Multivariate Granger causality and generalized variance. Phys. Rev.
E 2010, 81, 041907.
16.
Oizumi, M.; Amari, S.; Yanagawa, T.; Fujii, N.; Tsuchiya, N. Measuring integrated information from the
decoding perspective. PLoS Comput. Biol. 2016, 12, e1004654.
17.
Tegmark, M.
Improved measures of integrated information.
PLoS Computational Biology 2016,
12, e1005123.
18.
Ay, N. Information geometry on complexity and stochastic interaction. MPI MIS PREPRINT 95 2001.
19.
Ay, N. Information geometry on complexity and stochastic interaction. Entropy 2015, 17, 2432–2458.
20.
Amari, S.; Tsuchiya, N.; Oizumi, M. Geometry of information integration. arXiv preprint arXiv:1709.02050
2017.


## Page 21


Version February 14, 2018 submitted to Entropy
21 of 22
21.
Swendsen, R.H.; Wang, J.S. Replica Monte Carlo simulation of spin-glasses. Physical Review Letters 1986,
57, 2607.
22.
Geyer, C.J. Markov chain Monte Carlo maximum likelihood. Proceedings of the 23rd Symposium on the
Interface. Interface Foundation of North America, 1991, pp. 156–163.
23.
Hukushima, K.; Nemoto, K. Exchange Monte Carlo method and application to spin glass simulations.
Journal of the Physical Society of Japan 1996, 65, 1604–1608.
24.
Earl, D.J.; Deem, M.W. Parallel tempering: Theory, applications, and new perspectives. Physical Chemistry
Chemical Physics 2005, 7, 3910–3916.
25.
Burnham, K.P.; Anderson, D.R. Model selection and multimodel inference: a practical information-theoretic
approach; Springer Science & Business Media, 2003.
26.
Watanabe, S. Information theoretical analysis of multivariate correlation. IBM J. Res. Dev. 1960, 4, 66–82.
27.
Studený, M & Vejnarová, J., The multiinformation function as a tool for measuring stochastic dependence.;
MIT Press: Cambridge, MA, 1999.
28.
Pearl, J. Causality; Cambridge university press, 2009.
29.
Iwata, S. Submodular function minimization. Mathematical Programming 2008, 112, 45–64.
30.
Wishart, J.
The generalised product moment distribution in samples from a normal multivariate
population. Biometrika 1928, 20A, 32–52.
31.
Bishop, C.M. Pattern Recognition and Machine Learning; Springer-Verlag New York, 2006.
32.
Pinn, K.; Wieczerkowski, C. Number of magic squares from parallel tempering Monte Carlo. International
Journal of Modern Physics C 1998, 9, 541–546.
33.
Hukushima, K. Extended ensemble Monte Carlo approach to hardly relaxing problems. Computer physics
communications 2002, 147, 77–82.
34.
Nagata, K.; Kitazono, J.; Nakajima, S.; Eifuku, S.; Tamura, R.; Okada, M. An Exhaustive Search and
Stability of Sparse Estimation for Feature Selection Problem. IPSJ Online Transactions 2015, 8, 25–32.
35.
Toker, D.; Sommer, F. Information Integration In Large Brain Networks. arXiv preprint arXiv:1708.02967
2017.
36.
Kitazono, J.; Oizumi, M. phi_toolbox.zip 2017.
37.
Barthel, W.; Hartmann, A.K. Clustering analysis of the ground-state structure of the vertex-cover problem.
Phys. Rev. E 2004, 70, 066120.
38.
Wang, C., H.J.D.P.A.C.R. Parallel tempering for the traveling salesman problem. International Journal of
Modern Physics C, 20.
39.
Rathore, N.; Chopra, M.; de Pablo, J.J. Optimal allocation of replicas in parallel tempering simulations.
The Journal of chemical physics 2005, 122, 024111.
40.
Sugita, Y.; Okamoto, Y. Replica-exchange molecular dynamics method for protein folding.
Chemical
Physics Letters 1999, 314, 141 – 151.
41.
Kofke, D.A. On the acceptance probability of replica-exchange Monte Carlo trials. The Journal of chemical
physics 2002, 117, 6911–6914.
42.
Kofke, D.A. Erratum: “On the acceptance probability of replica-exchange Monte Carlo trials” [J. Chem.
Phys. 117, 6911 (2002)]. The Journal of chemical physics 2004, 120, 10852.
43.
Lee, M.S.; Olson, M.A. Comparison of two adaptive temperature-based replica exchange methods applied
to a sharp phase transition of protein unfolding-folding. The Journal of Chemical Physics 2011, 134, 244111,
[http://dx.doi.org/10.1063/1.3603964].
44.
Gelman, A.; Rubin, D.B. Inference from iterative simulation using multiple sequences. Statistical science
1992, pp. 457–472.
45.
Brooks, S.P.; Gelman, A. General methods for monitoring convergence of iterative simulations. Journal of
computational and graphical statistics 1998, 7, 434–455.
c⃝2018 by the authors.
Submitted to Entropy for possible open access publication under the terms and
conditions of the Creative Commons Attribution license (http://creativecommons.org/licenses/by/4.0/)


## Page 22


Version February 14, 2018 submitted to Entropy
22 of 22
0
0.02
0.04
0.06
0.08
0.1
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
Trial Number
ΦG
ΦG
0
0.02
0.04
0.06
0.08
0.1
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
Trial Number
ΦG
0
0.5
1
1.5
2
2.5
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
Trial Number
ΦSI
ΦSI
0
0.5
1
1.5
2
2.5
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
Trial Number
ΦSI
(a)
(b)
Figure 3. The values of Φ for the block-structured models at σ = 0.01. The box plots represent the
distribution of Φ at all the partitions. The red solid line indicates Φ at the MIP. The green circles
indicate Φ at the partitions found by Queyranne’s algorithm. (a) ΦSI, (b) ΦG.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
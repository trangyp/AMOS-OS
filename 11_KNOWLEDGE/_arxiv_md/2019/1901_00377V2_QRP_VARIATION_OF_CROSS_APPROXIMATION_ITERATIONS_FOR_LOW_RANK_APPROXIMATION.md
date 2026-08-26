---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1901.00377v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1901.00377v2_QRP_Variation_of_Cross--Approximation_Iterations_for_Low_Rank_Approximation

> Source: 1901.00377v2_QRP_Variation_of_Cross--Approximation_Iterations_for_Low_Rank_Approximation.pdf

> Pages: 6

---


## Page 1


arXiv:1901.00377v2  [math.NA]  31 Dec 2019
On the Superfast Multipole Method
Victor Y. Pan[1,2],[a] and John Svadlenka[2],[c]
[1] Department of Computer Science
Lehman College of the City University of New York
Bronx, NY 10468 USA
[2] Ph.D. Programs in Computer Science and Mathematics
The Graduate Center of of the City University of New York
New York, NY 10036 USA
[a] victor.pan@lehman.cuny.edu
http://comet.lehman.cuny.edu/vpan/
[b] jsvadlenka@gradcenter.cuny.edu
Abstract
We call matrix algorithms superfast if they involve much fewer memory cells and
ﬂops than the input matrix has entries.
Using such algorithms is indispensable for
Big Data Mining and Analysis, where the input matrices are so immense that realis-
tically one can only access a small fraction of all their entries. A natural remedy is
Low Rank Approximation of these matrices,1 which is routinely computed by means
of Cross–Approximation2 iterations for more than a decade of worldwide application
in computational practice. We point out and extensively test an important application
of superfast LRA to signiﬁcant acceleration of the celebrated Fast Multipole Method,
which turns it into Supefast Multipole Method.
Keywords:
Low Rank Approximation, Cross–Approximation, Fast Multipole Method.
2000 Math. Subject Classiﬁcation:
65F30, 68Q25, 15A52
1
Introduction: Superfast LRA
Low rank approximation (hereafter LRA) of a matrix is a fundamental subject of Numerical
Linear Algebra and Computer Science. An m×n matrix M admits its close approximation3
of rank r if and only if the matrix M has numerical rank r (then we write nrank(W) = r)
or equivalently if and only if
M = AB + E, ||E||/||M|| ≤ǫ,
(1)
for a small integer r, A ∈Cm×r, B ∈Cr×n, a ﬁxed matrix norm || · ||, and a small tolerance
ǫ. Such an LRA approximates the mn entries of M by using (m + n)r entries of A and B
1Hereafter we use the acronym LRA.
2Hereafter we use the acronym CA.
3Here and hereafter the concepts “low”, “large”, “small”, “far”, “close”, etc. are deﬁned in context. The
inequalities a ≪b and b ≫a show that |a/b| is small in context.
1


## Page 2


instead of mn entries of M, and one can operate with a low rank matrix, e.g., multiply it by
a vector superfast. This is a crucial beneﬁt in applications of LRA to Big Data Mining and
Analysis, where the input matrices M, e.g., unfolding matrices of multidimensional tensors,
are so immense that realistically one can only access a tiny fraction of all their entries. LRA
is a natural remedy, and for more than a decade the Cross–Approximation (C-A) iterations
have routinely been computing accurate LRA superfast in worldwide computational practice
( cf. [T96], [GTZ97], [T00], [B00], [BR03], [GOSTZ10], [B11], [O18], [OZ18]).
2
An Application – Superfast Multipole Method
Superfast LRA algorithms can be extended to numerous important computational problems
linked to LRA. Next we we point out and extensively test a simple but apparently unnoticed
application of superfast LRA to signiﬁcant acceleration of the celebrated Fast Multipole
Method (FMM), which turns it into Superfast Multipole Method.
2.1
Fast and Superfast Multipole Method
FMM enables superfast multiplication by a vector of so called HSS matrices provided that
low rank generators are available for its oﬀ-diagonal blocks. Such generators are not avail-
able in some important applications, however (see, e.g, [XXG12], [XXCB14], and [P15]),
but C–A algorithms compute them superfast, thus turning FMM into Superfast Multipole
Method. Since the method is highly important we supply some details of its bottleneck
stage of HSS computations, which we perform superfast by incorporating superfast LRA.
HSS matrices naturally extend the class of banded matrices and their inverses, are closely
linked to FMM, and are increasingly popular (see [BGH03], [GH03], [MRT05], [CGS07],
[VVGM05], [VVM07/08], [B10], [X12], [XXG12], [EGH13], [X13], [XXCB14], and the bib-
liography therein).
Deﬁnition 1. (Neutered Block Columns.
See [MRT05].)
With each diagonal block of
a block matrix associate its complement in its block column, and call this complement a
neutered block column.
Deﬁnition 2. (HSS matrices. See [CGS07], [X12], [X13], [XXCB14].)
A block matrix M of size m × n is called an r-HSS matrix, for a positive integer r,
(i) if all diagonal blocks of this matrix consist of O((m + n)r) entries overall and
(ii) if r is the maximal rank of its neutered block columns.
Remark 3. Many authors work with (l, u)-HSS (rather than r-HSS) matrices M for which l
and u are the maximal ranks of the sub- and super-diagonal blocks, respectively. The (l, u)-
HSS and r-HSS matrices are closely related. If a neutered block column N is the union
of a sub-diagonal block B−and a super-diagonal block B+, then rank(N) ≤rank(B−) +
rank(B+), and so an (l, u)-HSS matrix is an r-HSS matrix, for r ≤l + u, while clearly an
r-HSS matrix is a (r, r)-HSS matrix.
The FMM exploits the r-HSS structure of a matrix as follows:
(i) Cover all oﬀ-block-diagonal entries with a set of non-overlapping neutered block
columns.
(ii) Express every neutered block column N of this set as the product FH of two
generator matrices, F of size h × r and H of size r × k. Call the pair {F, H} a length r
generator of the neutered block column N.
2


## Page 3


(iii) Multiply the matrix M by a vector by separately multiplying generators and diag-
onal blocks by subvectors, involving O((m + n)r) ﬂops overall, and
(iv) in a more advanced application of FMM solve a nonsingular r-HSS linear system
of n equations by using O(nr log2(n)) ﬂops under some mild additional assumptions on the
input.
This approach is readily extended to the same operations with (r, ξ)-HSS matrices, that
is, matrices approximated by r-HSS matrices within a perturbation norm bound ξ where a
positive tolerance ξ is small in context (for example, is the unit round-oﬀ). Likewise, one
deﬁnes an (r, ξ)-HSS representation and (r, ξ)-generators.
(r, ξ)-HSS matrices (for r small in context) appear routinely in matrix computations, and
computations with such matrices are performed eﬃciently by using the above techniques.
In some applications of the FMM (see [BGP05], [VVVF10]) stage (ii) is omitted because
short generators for all neutered block columns are readily available, but this is not the case
in a variety of other important applications (see [XXG12], [XXCB14], and [P15]). This
stage of the computation of generators is precisely LRA of the neutered block columns,
which turns out to be the bottleneck stage of FMM in these applications, and superfast
LRA algorithms provide a remedy.
Indeed apply a fast algorithm at this stage, e.g., the algorithm of [HMT11] with a
Gaussian multiplier. Multiplication of a q × h matrix by an h × r Gaussian matrix requires
(2h −1)qr ﬂops, while standard HSS-representation of an n × n HSS matrix includes q × h
neutered block columns for q ≈m/2 and h ≈n/2. In this case the cost of computing an
r-HSS representation of the matrix M has at least order mnr. For r ≪min{m, n}, this is
much greater than O((m + n)r log2(n)) ﬂops, used at the other stages of the computations.
We alleviate such a problem, however, when we compute LRA of (r, ξ)-generators by
applying superfast algorithms.
3
Computation of LRAs for benchmark HSS matrices
In this section, the contribution of the secind author, we cover our tests of the Superfast
Multipole Method where we applied C–A iterations in order to compute LRA of the gen-
erators of the oﬀ-diagonal blocks of HSS matrices. Namely we tested HSS matrices that
approximate 1024 × 1024 Cauchy-like matrices derived from benchmark Toeplitz matrices
B, C, D, E, and F of [XXG12, Section 5]. For the computation of LRA we applied the
algorithm of [GOSTZ10].
Table 1 displays the relative errors of the approximation of the 1024 × 1024 HSS input
matrices in the spectral and Chebyshev norms averaged over 100 tests. Each approximation
was obtained by means of combining the exact diagonal blocks and LRA of the oﬀ-diagonal
blocks. We computed LRA of all these blocks superfast.
In good accordance with extnsive empirical evidence about the power of C–A iterations,
already the ﬁrst C–A loop have consistently yielded reasonably close LRA, but our further
improvement was achieved in ﬁve C–A loops in our tests for all but one of the ﬁve families
of input matrices.
The reported HSS rank is the larger of the numerical ranks for the 512×512 oﬀ-diagonal
blocks. This HSS rank was used as an upper bound in our binary search that determined
the numerical rank of each oﬀ-diagonal block for the purpose of computing its LRA. We
based the binary search on minimizing the diﬀerence (in the spectral norm) between each
oﬀ-diagonal block and its LRA.
3


## Page 4


The output error norms were quite low. Even in the case of the matrix C, obtained from
Prolate Toeplitz matrices – extremely ill-conditioned, they ranged from 10−3 to 10−6.
We have also performed further numerical experiments on all the HSS input matrices
by using a hybrid LRA algorithm: we used random pre-processing with Gaussian and
Hadamard (abridged and permuted) multipliers by incorporating Algorithm 4.1 of [HMT11],
but only for the oﬀ-diagonal blocks of smaller sizes while retaining our previous way for
computing LRA of the larger oﬀ-diagonal blocks. We have not displayed the results of these
experiments because they yielded no substantial improvement in accuracy in comparison to
the exclusive use of the less expensive LRA on all oﬀ-diagonal blocks.
Spectral Norm
Chebyshev Norm
Inputs
C–A loops
HSS rank
mean
std
mean
std
B B
1
26
8.11e-07
1.45e-06
3.19e-07
5.23e-07
5
26
4.60e-08
6.43e-08
7.33e-09
1.22e-08
C
1
16
5.62e-03
8.99e-03
3.00e-03
4.37e-03
5
16
3.37e-05
1.78e-05
8.77e-06
1.01e-05
D
1
13
1.12e-07
8.99e-08
1.35e-07
1.47e-07
5
13
1.50e-07
1.82e-07
2.09e-07
2.29e-07
E
1
14
5.35e-04
6.14e-04
2.90e-04
3.51e-04
5
14
1.90e-05
1.04e-05
5.49e-06
4.79e-06
F
1
37
1.14e-05
4.49e-05
6.02e-06
2.16e-05
5
37
4.92e-07
8.19e-07
1.12e-07
2.60e-07
Table 1: LRA approximation of HSS matrices from [XXG12]
Acknowledgements: Our research was supported by NSF Grants CCF–1116736, CCF–
1563942, and CCF–133834 and PSC CUNY Award 69813 00 48.
References
[B00]
M. Bebendorf, Approximation of Boundary Element Matrices, Numer. Math.,
86, 4, 565–589, 2000.
[B10]
S. B¨orm, Eﬃcient Numerical Methods for Non-local Operators: H2-Matrix Com-
pression, Algorithms and Analysis, European Math. Society, 2010.
[B11]
M. Bebendorf, Adaptive Cross Approximation of Multivariate Functions, Construc-
tive approximation, 34, 2, 149–179, 2011.
[BGH03] S. B¨orm, L. Grasedyck, W. Hackbusch, Introduction to Hierarchical Matrices with
Applications, Engineering Analysis with Boundary Elements, 27, 5, 405–422, 2003.
[BGP05] A. Bini, L. Gemignani, V. Y. Pan, Fast and Stable QR Eigenvalue Algorithms
for Generalized Semiseparable Matrices and Secular Equation, Numerische Math-
ematik, 100, 3, 373–408, 2005.
[BR03] M. Bebendorf, S. Rjasanow, Adaptive Low-Rank Approximation of Collocation
Matrices, Computing, 70, 1, 1–24, 2003.
4


## Page 5


[BY13] L. A. Barba, R. Yokota, How Will the Fast Multipole Method Fare in Exascale
Era? SIAM News, 46, 6, 1–3, July/August 2013.
[C00]
B. A. Cipra, The Best of the 20th Century: Editors Name Top 10 Algorithms,
SIAM News, 33, 4, 2, May 16, 2000.
[CGR88] J. Carrier, L. Greengard, V. Rokhlin, A Fast Adaptive Algorithm for Particle
Simulation, SIAM Journal on Scientiﬁc Computing, 9, 669–686, 1988.
[CGS07] S. Chandrasekaran, M. Gu, X. Sun, J. Xia, J. Zhu, A Superfast Algorithm for
Toeplitz Systems of Linear Equations, SIAM. J. on Matrix Analysis and Applica-
tions, 29, 4, 1247–1266, 2007.
[CML15] A. Cichocki, D. Mandic, L. D. Lathauwer, G. Zhou, Q. Zhao, C. Caiafa, H. A.
Phan, Tensor Decompositions for Signal Processing Applications: From Two-Way
to Multiway Component Analysis, IEEE Signal Processing Magazine, 32, 2, 145–
163, March 2015.
[EGH13] Y. Eidelman, I. Gohberg, I. Haimovici, Separable Type Representations of Matrices
and Fast Algorithms, volumes 1 and 2, Birkh¨auser, 2013.
[GH03] L. Grasedyck, W. Hackbusch, Construction and Arithmetics of H-Matrices, Com-
puting, 70, 4, 295–334, 2003.
[GOSTZ10] S. Goreinov, I. Oseledets, D. Savostyanov, E. Tyrtyshnikov, N. Zamarashkin,
How to Find a Good Submatrix, in Matrix Methods: Theory, Algorithms, Appli-
cations (dedicated to the Memory of Gene Golub, edited by V. Olshevsky and E.
Tyrtyshnikov), pages 247–256, World Scientiﬁc Publishing, New Jersey, ISBN-13
978-981-283-601-4, ISBN-10-981-283-601-2, 2010.
[GR87] L. Greengard, V. Rokhlin, A Fast Algorithm for Particle Simulation, Journal of
Computational Physics, 73, 325–348, 1987.
[GTZ97] S. A. Goreinov, E. E. Tyrtyshnikov, N. L. Zamarashkin, A Theory of Pseudo-
skeleton Approximations, Linear Algebra and Its Applications, 261, 1–21, 1997.
[HMT11] N. Halko, P. G. Martinsson, J. A. Tropp, Finding Structure with Randomness:
Probabilistic Algorithms for Constructing Approximate Matrix Decompositions,
SIAM Review, 53, 2, 217–288, 2011.
[KS17] N. Kishore Kumar, J. Schneider, Literature Survey on Low Rank Approxima-
tion of Matrices, Linear and Multilinear Algebra, 65, 11, 2212–2244, 2017, and
arXiv:1606.06511v1 [math.NA] 21 June 2016.
[MRT05] P. G. Martinsson, V. Rokhlin, M. Tygert, A Fast Algorithm for the Inversion of
General Toeplitz Matrices, Comput. Math. Appl., 50, 741–752, 2005.
[O18]
A.I. Osinsky, Rectangular Matrix Volume and Projective Volume Search Algo-
rithms, arXiv:1809.02334, September 17, 2018.
[OZ18] A.I. Osinsky, N. L. Zamarashkin, Pseudo-skeleton Approximations with Better Ac-
curacy Estimates, Linear Algebra and Its Applications, 537, 221–249, 2018.
5


## Page 6


[P15]
V. Y. Pan, Transformations of Matrix Structures Work Again, Linear Algebra and
Its Applications, 465, 1–32, 2015.
[T96]
E.E. Tyrtyshnikov, Mosaic-Skeleton Approximations, Calcolo, 33, 1, 47–57, 1996.
[T00]
E. Tyrtyshnikov, Incomplete Cross-Approximation in the Mosaic-Skeleton Method,
Computing, 64, 367–380, 2000.
[VVGM05] R. Vandebril, M. Van Barel, G. Golub, N. Mastronardi, A Bibliography on
Semiseparable Matrices, Calcolo, 42, 3–4, 249–270, 2005.
[VVM07/08] R. Vandebril, M. Van Barel, N. Mastronardi, Matrix Computations and
Semiseparable Matrices (Volumes 1 and 2), The Johns Hopkins University Press,
Baltimore, Maryland, 2007.
[VVVF10] M. Van Barel, R. Vandebril, P. Van Dooren, K. Frederix, Implicit Double Shift
QR-algorithm for Companion Matrices, Numerische Mathematik, 116, 177–212,
2010.
[X12]
J. Xia, On the Complexity of Some Hierarchical Structured Matrix Algorithms,
SIAM J. Matrix Anal. Appl., 33, 388–410, 2012.
[X13]
J. Xia, Randomized Sparse Direct Solvers, SIAM J. Matrix Anal. Appl., 34, 197–
227, 2013.
[XXCB14] J. Xia, Y. Xi, S. Cauley, V. Balakrishnan, Superfast and Stable Structured
Solvers for Toeplitz Least Squares via Randomized Sampling, SIAM J. Matrix
Anal. Appl., 35, 44–72, 2014.
[XXG12] J. Xia, Y. Xi, M. Gu, A Superfast Structured Solver for Toeplitz Linear Systems
via Randomized Sampling, SIAM J. Matrix Anal. Appl., 33, 837–858, 2012.
6

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
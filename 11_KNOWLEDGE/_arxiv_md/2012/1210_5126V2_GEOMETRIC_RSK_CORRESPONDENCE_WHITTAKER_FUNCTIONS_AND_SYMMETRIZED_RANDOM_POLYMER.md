---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1210.5126v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1210.5126v2_Geometric_RSK_correspondence__Whittaker_functions_and_symmetrized_random_polymer

> Source: 1210.5126v2_Geometric_RSK_correspondence__Whittaker_functions_and_symmetrized_random_polymer.pdf

> Pages: 45

---


## Page 1


arXiv:1210.5126v2  [math.PR]  6 Jun 2013
Geometric RSK correspondence, Whittaker functions and
symmetrized random polymers
Neil O’Connell, Timo Sepp¨al¨ainen, and Nikos Zygouras
Abstract. We show that the geometric lifting of the RSK correspondence introduced by A.N.
Kirillov (2001) is volume preserving with respect to a natural product measure on its domain, and
that the integrand in Givental’s integral formula for GL(n, R)-Whittaker functions arises naturally
in this context. Apart from providing further evidence that Whittaker functions are the natural
analogue of Schur polynomials in this setting, our results also provide a new ‘combinatorial’ frame-
work for the study of random polymers. When the input matrix consists of random inverse gamma
distributed weights, the probability distribution of a polymer partition function constructed from
these weights can be written down explicitly in terms of Whittaker functions. Next we restrict
the geometric RSK mapping to symmetric matrices and show that the volume preserving property
continues to hold. We determine the probability law of the polymer partition function with inverse
gamma weights that are constrained to be symmetric about the main diagonal, with an additional
factor on the main diagonal. The third combinatorial mapping studied is a variant of the geometric
RSK mapping for triangular arrays, which is again showed to be volume preserving. This leads
to a formula for the probability distribution of a polymer model whose paths are constrained to
stay below the diagonal. We also show that the analogues of the Cauchy-Littlewood identity in the
setting of this paper are equivalent to a collection of Whittaker integral identities conjectured by
Bump (1989) and Bump and Friedberg (1990) and proved by Stade (2001, 2002). Our approach
leads to new ‘combinatorial’ proofs and generalizations of these identities, with some restrictions
on the parameters.
Contents
1.
Introduction
2
2.
Whittaker functions and patterns
4
3.
Geometric RSK correspondence
8
4.
Equivalence of old and new description of geometric RSK
17
5.
Symmetric input matrix
19
6.
Geometric RSK for triangular arrays and paths below a hard wall
25
7.
Whittaker integral identities
37
8.
Tropicalization, last passage percolation and random matrices
40
References
43
1


## Page 2


1. Introduction
The Robinson-Schensted-Knuth (RSK) correspondence is a combinatorial mapping which plays
an important role in the theory of Young tableaux, symmetric functions and representation the-
ory [18, 40]. It is deeply connected with Schur functions and provides a combinatorial framework
for understanding the Cauchy-Littlewood identity and Schur measures on integer partitions. It is
also the basic structure which lies behind the solvability of a particular family of combinatorial
models in probability and statistical physics including longest increasing subsequence problems,
directed last passage percolation in 1+1 dimensions and the totally asymmetric simple exclusion
process, see for example [1, 3, 27, 35].
The RSK map is deﬁned on matrices with non-negative integer coeﬃcients and can be described
by expressions in the max-plus semi-ring.
This was extended to matrices with real entries by
Berenstein and Kirillov [8]. Replacing these expressions by their analogues in the usual algebra,
A.N. Kirillov [29] introduced a geometric lifting of the Berenstein-Kirillov correspondence which he
called the ‘tropical RSK correspondence’, in honour of M.-P. Sch¨utzenberger (1920–1996). However,
for many readers nowadays the word ‘tropical’ indicates just the opposite, so to avoid confusion we
will refer to Kirillov’s construction as the geometric RSK (gRSK) correspondence, as in the theory
of geometric crystals [6, 7], which is closely related.
The geometric RSK correspondence is a birational mapping from (R>0)n×m onto itself.
It
was introduced by Kirillov [29] for square matrices (n = m) and generalized to the rectangular
setting by Noumi and Yamada [32]. In the paper [15] it was shown that there is a fundamental
connection between the gRSK correspondence and GL(n, R)-Whittaker functions, analogous to the
well-known connection between the RSK correspondence and Schur functions. In particular, it is
explained there that the analogue of the Cauchy-Littlewood identity in the setting of gRSK can
be seen as a generalization of a Whittaker integral identity which was originally conjectured by
Bump [13] and later proved by Stade [38]. The connection to Whittaker functions gives rise to a
natural family of measures (Whittaker measures) which play a similar role in this setting to Schur
measures on integer partitions. It also has applications to random polymers. In the paper [15], an
explicit integral formula is obtained for the Laplace transform of the law of the partition function
associated with a random directed polymer model on the two-dimensional lattice with log-gamma
weights introduced in [37]. For related recent developments, see [33, 9, 10].
In the present work, we ﬁrst provide further insight into the results of [15] by showing:
(a) the gRSK mapping is volume preserving with respect to the product measure Q
ij dxij/xij
on (R>0)n×m, and
(b) the integrand in Givental’s integral formula for GL(n, R)-Whittaker functions [21, 26] arises
naturally through the application of the gRSK map (see Theorem 3.2 below).
The volume preserving property can be seen as a consequence of a new description of the
gRSK map as a composition of local moves which we introduce in this paper. This description
is a re-formulation of the geometric row-insertion algorithm introduced by Noumi and Yamada
in [32]. Combining (a) and (b) gives a direct ‘combinatorial’ proof of Stade’s identity (with some
2


## Page 3


restrictions on the parameters) analogous to the bijective proof of the Cauchy-Littlewood identity
via the classical RSK correspondence (see, for example, Fulton [18, §4.3]).
The second aim of this paper is to initiate a program of understanding the gRSK mapping in
the presence of symmetry constraints in much the same spirit as the work of Baik and Rains [4,
5, 2] on longest increasing subsequence and last passage percolation problems. Here we consider
one particular symmetry, namely the restriction of gRSK to symmetric matrices. We show that
the volume preserving property continues to hold in this setting and deduce the analogue of the
Whittaker measure. The corresponding Whittaker integral identity (Corollary 5.5) involves only a
single Whittaker function, and turns out to be equivalent to a formula for a certain Mellin transform
of the GL(n, R)-Whittaker function which was conjectured by Bump and Friedberg [14] and proved
by Stade [39], again with some restrictions on the parameters. We also consider a degeneration of
this model in which the diagonal entries of the input matrix vanish and the gRSK map rescales to
a new version of gRSK deﬁned on triangles. This model has a surprising and non-trivial connection
to the symmetric case.
As an application we determine the law of the partition function of a family of random polymer
models with log-gamma weights that are constrained to be symmetric about the main diagonal.
We also consider a degeneration of this model in which the polymer paths are constrained to stay
below the diagonal. This can be seen as a discrete version of the continuum random polymer above
a hard wall, which appeared recently in the physics literature [23]. Formally, our results yield
integral formulae for the Laplace transforms of these laws which can be used as a starting point
for further asymptotic development. Similar integral formulae obtained in [15] for the polymer
model without symmetry were used in [10] to prove Tracy-Widom GUE asymptotics for the law
of the partition function. The polymer models we consider also give rise to a positive temperature
version of the interpolating ensembles of Baik and Rains [4, 2]. In the KPZ scaling limit they
should correspond to the KPZ equation on the half-line with mixed boundary conditions at zero
and narrow wedge initial condition.
The outline of the paper is as follows.
• In the next section we give some background on Whittaker functions, introduce a general-
ization of these functions and explain how these functions can be regarded as generating func-
tions for patterns. This interpretation can be seen as a generalization of Givental’s integral for-
mula [21, 26, 19] and is analogous to the combinatorial interpretation of Schur functions as
generating functions for semistandard Young tableaux.
• In Section 3 we give a new description of the gRSK map as a composition of local moves
(based on Noumi and Yamada’s dynamical description of gRSK) and use this to establish several
basic results. In particular, we show that the gRSK mapping is volume-preserving with respect to
a natural product measure on (R>0)n×m and establish a fundamental identity (Theorem 3.2) which
provides an elementary explanation of the appearance of Whittaker functions in this setting. This
gives further insight into earlier results from [15] and yields a new proof and generalization of two
of Stade’s Whittaker integral identities (Theorems 7.1 and 7.3).
3


## Page 4


• In Section 4 we explain the relationship between the local-moves description of gRSK and the
geometric row-insertion algorithm of Noumi and Yamada [32].
• In Section 5 we consider the restriction of gRSK to symmetric matrices.
We show that
the volume preserving property continues to hold in this setting and deduce several consequences,
including a new proof (with some restriction on the parameters) of the Whittaker integral identity
(Theorem 7.5) involving a single Whittaker function due to Stade [39].
• In Section 6 we introduce gRSK for triangular arrays. Again we prove a fundamental identity
and the volume preserving property, and deduce the probability distribution of the shape vector
of the output array under inverse gamma distributed initial weights. The polymer version of the
problem describes paths restricted to lie below a hard wall.
• In Section 7 we explain how the results of this paper relate to some of the Whittaker integral
identities which have appeared previously in the automorphic forms literature.
• In Section 8 we explain how the Berenstein-Kirillov extension of the RSK correspondence
can be recovered by taking a limit (tropicalization). In statistical physics terminology this is a
zero-temperature limit that takes polymer partition functions to last-passage percolation values.
By analogy with Section 3, we give a description of the Berenstein-Kirillov mapping in terms of
local moves which shows that this map is also volume preserving. Under exponentially distributed
weights the probability distribution of the shape vector of the resulting pair of Gelfand-Tsetlin
patterns is given by a non-central Laguerre ensemble. This connection to random matrix theory
has had important applications to last passage percolation models [27, 4, 17, 11, 16].
Acknowledgements. Many thanks to Jinho Baik, Ivan Corwin, Anatol Kirillov, Eric Rains and
Eric Stade for helpful discussions. NO’C is partially supported by EPSRC grant EP/I014829/1. TS
is partially supported by National Science Foundation grants DMS-1003651 and DMS-1306777 and
by the Wisconsin Alumni Research Foundation. NZ is supported by a Marie Curie International
Reintegration Grant within the 7th European Community Framework Programme, IRG-246809.
2. Whittaker functions and patterns
We begin by deﬁning the following Baxter Q-type operators, as in [19, 20].
For λ ∈C,
x, y ∈(R>0)n, deﬁne
Qn
λ(x, y) =
 n
Y
i=1
yi
xi
!λ
exp
 
−
n
X
i=1
yi
xi
−
n−1
X
i=1
xi+1
yi
!
.
For λ ∈C, x ∈(R>0)n and y ∈(R>0)n−1, deﬁne
Qn,n−1
λ
(x, y) =
 Qn−1
i=1 yi
Qn
i=1 xi
!λ
exp
 
−
n−1
X
i=1
yi
xi
−
n−1
X
i=1
xi+1
yi
!
.
We regard these as integral operators: for suitable test functions,
Qn
λf(x) =
Z
(R>0)n Qn
λ(x, y)f(y)
n
Y
i=1
dyi
yi
,
4


## Page 5


Qn,n−1
λ
f(x) =
Z
(R>0)n−1 Qn,n−1
λ
(x, y)f(y)
n−1
Y
i=1
dyi
yi
.
Deﬁne Ψn
λ(x), λ ∈Cn, x ∈(R>0)n recursively by setting Ψ1
λ(x) = x−λ and, for n ≥2,
(2.1)
Ψn
λ1,...,λn = Qn,n−1
λn
Ψn−1
λ1,...,λn−1.
We note here, for later reference, some identities which follow easily from the deﬁnitions. For a > 0
we have
(2.2)
Ψn
α(ax) = a−P
i αiΨn
α(x).
If α′
i = αi + c for some c ∈C, then
(2.3)
Ψn
α′(x) =
 Y
i
x−c
i
!
Ψn
α(x).
Finally, if we set x′
i = 1/xn−i+1, then
(2.4)
Ψn
λ(x) = Ψn
−λ(x′).
The functions Ψn
λ are GL(n, R)-Whittaker functions. The above deﬁnition is essentially Givental’s
integral formula [21, 26] (see also [19, 20]). These functions were ﬁrst introduced by Jacquet [25].
They play an important role in the theory of automorphic forms [12, 13, 14, 38, 39, 22, 24]
and the quantum Toda lattice [31, 36, 21, 26, 19, 20, 28]. In the latter literature they arise as
eigenfunctions of the open quantum Toda chain with n particles with Hamiltonian given by
H = −
X
i
∂2
∂x2
i
+ 2
n−1
X
i=1
exi+1−xi.
If we deﬁne ψn
λ(x) = Ψn
−λ(z), where xi = log zi for i = 1, . . . , n, then
Hψn
λ = −
 X
i
λ2
i
!
ψn
λ.
See, for example, [19] for more details.
In the automorphic forms literature the standard ‘normalisation’ is slightly diﬀerent. In par-
ticular, in the notation of the paper [24], we have the relation, for n ≥2:
(2.5)
Ψn
−λ(x) =
 Y
i
xi
!(1/n) P
i λi 

n−1
Y
j=1
y−j(n−j)/2
j

Wn,a(y),
where ak = λk −(1/n) P
i λi for k = 1, . . . , n and πyj =
p
xn−j+1/xn−j, for j = 1, . . . , n −1. This
is easily veriﬁed by comparing the recursion (2.1) with a similar recursion obtained by Ishii and
Stade [24] for the functions Wn,a(y), and using the elementary relation (2.3). Indeed, ﬁrst note
that, by (2.3), we only need to check this for λ = a, that is, when P
i λi = 0. In the case n = 2 we
have, writing a = (a, −a) and y1 = y,
W2,a(y) = 2√yK2a(2πy) = √yΨ2
a(x1, x2)
5


## Page 6


where πy =
p
x2/x1 and Kν is the Macdonald function
Kν(z) = 1
2
Z ∞
0
tν−1e−z
2 (t+t−1)dt.
For n ≥3, in [24] it is shown that
Wn,a(y) =
n−1
Y
j=1
y(n−j)/2+2a1(n−j)/(n−1)
j
Z
(R>0)n−1 e−π Pn−1
j=1 y2
j uj+1/uj
n−1
Y
j=1
u(n−2j)/4+na1/(n−1)
j
Wn−1,b
 
y2
ru2
u1
, . . . , yn−1
s
dun−1
un−2
!
du1
u1
. . . dun−1
un−1
,
where
b =

a2 +
a1
n −1, . . . , an +
a1
n −1

.
Making the change of variables
πyj =
rxn−j+1
xn−j
,
π
uj
= xn−j
zn−j
,
πy2
j uj = zn−j+1
xn−j
,
for j = 1, . . . , n −1, and using (2.5) above, we see that this is equivalent to the recursion
Ψn
−a(x) =
Z
(R>0)n−1 Qn,n−1
−a1
(x, z)Ψn−1
−a2,...,−an(z)dz1
z1
. . . dzn−1
zn−1
,
which agrees with (2.1) above.
We will also consider the following generalization of the functions Ψn
λ. For λ ∈Cn, x ∈(R>0)n
and s ∈C, deﬁne
(2.6)
Ψn
λ;s(x) = e−s/xnΨn
λ(x);
for λ ∈Cn+k, k ≥1, and ℜs > 0, deﬁne
(2.7)
Ψn
λ;s = Qn
λn+kQn
λn+k−1 . . . Qn
λn+1Ψn
λ1,...,λn;s.
It is straightforward to see that Ψn
λ;s(x) is well-deﬁned, as an absolutely convergent integral, for
each x ∈Rn. The functions Ψn
λ;s can be regarded as generating functions for ‘patterns’, as we shall
now explain.
Let x ∈(R>0)n. We deﬁne a pattern P with shape sh P = x and height h ≥n to be an array
of positive real numbers
P =
z11
z22
z21
...
...
znn
. . .
zn1
...
...
zhn
. . .
zh1
(2.8)
with bottom row zh· = x. The range of indices is
L(n, h) = {(i, j) : 1 ≤i ≤h, 1 ≤j ≤i ∧n}.
6


## Page 7


If h = n then P is a triangle in the sense of Kirillov [29]. Fix a pattern P as above. Set ρ0 = 1
and, for 1 ≤i ≤h, ρi = Qi∧n
j=1 zij and τi = ρi/ρi−1. We shall refer to τ as the type of P and write
τ = type P. For α ∈Ch deﬁne
P α =
h
Y
i=1
τ αi
i .
(2.9)
For s ∈C, deﬁne
(2.10)
Fs(P) =
s
znn
+
X
(i,j)∈L(n,h)
zi−1,j + zi+1,j+1
zij
with the convention that zij = 0 if (i, j) /∈L(n, h). Denote by Πh(x) the set of patterns with shape
x and height h. Then, for λ ∈Ch and ℜs > 0 (this condition is only required if h > n)
(2.11)
Ψn
λ;s(x) =
Z
Πh(x)
P −λe−Fs(P )dP
where
dP =
Y
(i,j)∈L(n,h−1)
dzij
zij
.
This formula is just a re-writing of the above deﬁnition (2.7) of Ψn
λ;s.
We remark that, although it is not obvious from the above deﬁnition, the function Ψn
λ is invariant
under permutations of the indices λ1, . . . , λn [28, 20]. In fact, the same is true of the function Ψn
λ;s,
where λ ∈Cn+k, k ≥1 and ℜs > 0. That is, Ψn
λ;s is invariant under permutations of the indices
λ1, . . . , λn+k. This follows from the deﬁnition (2.7), using the relation
(2.12)
Qn
aRn
s Qn
b = Qn
b Rn
s Qn
a,
where Rs denotes multiplication by the function e−s/xn, and the invariance of Ψn
λ1,...,λn under
permutations of λ1, . . . , λn. The relation (2.12) is a straightforward extension of the commutativity
property Qn
aQn
b = Qn
b Qn
a obtained in [20, Theorem 2.3].
There is a Plancherel theorem for the Whittaker functions [41, 36, 28], which states that the
integral transform
ˆf(λ) =
Z
(R>0)n f(x)Ψn
λ(x)
n
Y
i=1
dxi
xi
deﬁnes an isometry from L2((R>0)n, Qn
i=1 dxi/xi) onto Lsym
2
(ιRn, sn(λ)dλ), where Lsym
2
is the space
of L2 functions which are symmetric in their variables, ι = √−1 and
sn(λ) =
1
(2πι)nn!
Y
i̸=j
Γ(λi −λj)−1,
is the Sklyanin measure.
7


## Page 8


3. Geometric RSK correspondence
The geometric RSK (gRSK) correspondence is a bijective mapping
T : (R>0)n×m →(R>0)n×m.
It is also birational in the sense that both T and its inverse are rational maps. It was introduced by
Kirillov [29] as a geometric lifting of the Berenstein-Kirillov correspondence and further studied by
Noumi and Yamada [32]. We will deﬁne it here via a sequence of ‘local moves’ on matrix elements.
This is essentially a reformulation of the row-insertion procedure introduced in [32], as will be
explained in Section 4 below.
For each 2 ≤i ≤n and 2 ≤j ≤m deﬁne a mapping lij which takes as input a matrix
X = (xij) ∈(R>0)n×m and replaces the submatrix
 
xi−1,j−1
xi−1,j
xi,j−1
xij
!
of X by its image under the map
(3.1)
 
a
b
c
d
!
7→
 
bc/(ab + ac)
b
c
d(b + c)
!
,
and leaves the other elements unchanged. For 2 ≤i ≤n and 2 ≤j ≤m, deﬁne li1 to be the
mapping that replaces the element xi1 by xi−1,1xi1 and l1j to be the mapping that replaces the
element x1j by x1,j−1x1j. For convenience deﬁne l11 to be the identity map. For 1 ≤i ≤n and
1 ≤j ≤m, set
πj
i = lij ◦· · · ◦li1,
and, for 1 ≤i ≤n,
(3.2)
Ri =



πm−i+1
1
◦· · · ◦πm
i
i ≤m
π1
i−m+1 ◦· · · ◦πm
i
i ≥m.
The mapping T is deﬁned by
(3.3)
T = Rn ◦· · · ◦R1.
For example, suppose n = m = 2. Then
R1 = π2
1 = l12 ◦l11 = l12,
R2 = π1
1 ◦π2
2 = l11 ◦l22 ◦l21 = l22 ◦l21
and so
T = R2 ◦R1 = l22 ◦l21 ◦l12.
Here is an illustration:
T :
 
a
b
c
d
!
l12
7−→
 
a
ab
c
d
!
l21
7−→
 
a
ab
ac
d
!
l22
7−→
 
bc/(b + c)
ab
ac
ad(b + c)
!
.
8


## Page 9


Note that each lij is birational. For example, the inverse of the map (3.1) is given by
 
a
b
c
d
!
7→
 
bc/(ab + ac)
b
c
d/(b + c)
!
.
The birational property of T can thus be seen directly from the above deﬁnition.
Each matrix X ∈(R>0)n×m can be identiﬁed with a pair of patterns (P, Q) with respective
heights m and n, and common shape
sh P = sh Q = (xnm, xn−1,m−1, . . . , xn−p+1,m−p+1),
where p = n ∧m, as illustrated in the following example:
X =
x31
x21
x32
x11
x22
x12
P =
x31
x21
x32
,
Q =
x12
x11
x22
x21
x32
sh P = sh Q = (x32, x21).
In the following, we will simply write X = (P, Q) to indicate that X is identiﬁed with the pair
(P, Q).
The mappings Ri deﬁned above can also be written as
Ri = ρi
m ◦· · · ◦ρi
2 ◦ρi
1
where
ρi
j =



l1,j−i+1 ◦· · · ◦li−1,j−1 ◦lij
i ≤j
li−j+1,1 ◦· · · ◦li−1,j−1 ◦lij
i ≥j.
(3.4)
Here we are just using the obvious fact that lij ◦li′j′ = li′j′ ◦lij whenever |i −i′| + |j −j′| > 2. This
representation is closely related to the Bender-Knuth transformations, as we shall now explain. For
each 1 ≤i ≤n and 1 ≤j ≤m, denote by bij the map on (R>0)n×m which takes a matrix X = (xqr)
and replaces the entry xij by
(3.5)
x′
ij = 1
xij
(xi,j−1 + xi−1,j)

1
xi+1,j
+
1
xi,j+1
−1
,
leaving the other entries unchanged, with the conventions that x0j = xi0 = 0, xn+1,j = xi,m+1 = ∞
for 1 < i < n and 1 < j < m, but x10 + x01 = x−1
n+1,m + x−1
n,m+1 = 1. Denote by rj the map
9


## Page 10


which replaces the entry xnj by xn,j+1/xnj if j < m and 1/xnm if j = m, leaving the other entries
unchanged. For j ≤m, deﬁne
(3.6)
hj =



bn−j+1,1 ◦· · · ◦bn−1,j−1 ◦bnj
j ≤n
b1,j−n+1 ◦· · · ◦bn−1,j−1 ◦bnj
j ≥n.
It is straightforward from the deﬁnitions to see that ρn
j = hj ◦rj. Now, observe that if X = (P, Q),
then for each j < m, hj(X) = (tj(P), Q) where tj is deﬁned by this relation. It is easy to see that
the mappings bij, hj and tj are all involutions.
In the case n = m, the mappings t1, . . . , tn−1 are the analogues of the Bender-Knuth transfor-
mations in this setting, as discussed in [29]. In this case, if we deﬁne, for i < n,
(3.7)
qi = t1 ◦(t2 ◦t1) ◦· · · ◦(ti ◦· · · ◦t1),
then, as explained in [29], the involutions si = qi ◦t1 ◦qi, i < n, satisfy the braid relations
(sisi+1)3 = Id., and hence deﬁne an action of Sn on the set of triangles of height n. The mapping
qn−1 is the analogue of Sch¨utzenberger’s involution in this setting.
An immediate consequence of the above re-formulation of gRSK is the following volume pre-
serving property. Denote the input matrix by W = (wij) ∈(R>0)n×m and the output matrix by
T = T(W) = (tij) ∈(R>0)n×m.
Theorem 3.1. The gRSK mapping in logarithmic variables
(log wij, 1 ≤i ≤n, 1 ≤j ≤m) 7→(log tij, 1 ≤i ≤n, 1 ≤j ≤m)
has Jacobian ±1.
Proof. It is easy to see that the Jacobians of the mappings lij in logarithmic variables are all
±1. This follows from the fact that the mappings
(log a, log b) 7→(log a, log a + log b)
(log a, log b, log c, log d) 7→(log(bc/(ab + ac)), log b, log c, log(db + dc))
each have Jacobian ±1. The result follows from the deﬁnition (3.3) of T.
□
We remark that, by a similar argument it can be seen that the involutions qi, i < n, on the set
of triangles of height n, all have Jacobian ±1 in logarithmic variables.
We recall here some basic properties of the gRSK map T, which are either obvious from the
deﬁnitions or proved in the papers [31, 32]. Suppose W ∈(R>0)n×m and T = T(W) = (P, Q).
If we deﬁne row and column products Ri = Q
j wij and Cj = Q
i wij, then type Q = R and
type P = C. Note that this implies, for λ ∈Cm and ν ∈Cn,
(3.8)
Y
ij
w−νi−λj
ij
=
Y
i
R−νi
i
Y
j
C−λj
j
= P −λQ−ν.
Also, the following symmetries hold:
T(W t) = T(W)t;
T(W) = (P, Q) ⇐⇒T(W t) = (Q, P);
10


## Page 11


(1, 1)
(n, k)
(n, m)
Figure 1.
Three paths (π1, π2, π3) of a particular 3-tuple in Π(3)
n,k in an n × m weight
matrix. Note that the picture is in Cartesian coordinates. The paths start at the lower left
at (1, 1), (1, 2) and (1, 3) and end at the upper right at (n, k −2), (n, k −1), (n, k).
W is symmetric ⇐⇒T is symmetric ⇐⇒P = Q;
W is symmetric across the anti-diagonal ⇐⇒Q = qn−1(P).
The connection to directed polymers is via the following formula for tnm:
tnm =
X
π∈Πn,m
Y
(i,j)∈π
wij,
where Πn,m is the set of directed nearest-neighbor lattice paths in Z2 from (1, 1) to (n, m), that is,
the set of paths π = {π(1), π(2), . . . , π(n + m −1)} such that π(1) = (1, 1), π(n + m −1) = (n, m)
and π(k + 1) −π(k) ∈{(1, 0), (0, 1)} for 1 ≤k < n + m −1. We shall refer to the variable tnm as
the polymer partition function. In this context it is natural to refer to the wij as weights and W as
the weight matrix. In fact, the remaining entries of T = (P, Q) can also be expressed in terms of
similar partition functions, as follows. For 1 ≤k ≤m and 1 ≤r ≤n ∧k,
(3.9)
tn−r+1,k−r+1 · · · tn−1,k−1tnk =
X
(π1,...,πr)∈Π(r)
n,k
Y
(i,j)∈π1∪···∪πr
wij,
where Π(r)
n,k denotes the set of r-tuples of non-intersecting directed nearest-neighbor lattice paths
π1, . . . , πr starting at positions (1, 1), (1, 2), . . . , (1, r) and ending at positions (n, k−r+1), . . . , (n, k−
1), (n, k).
(See Figure 1.
When we use the path representation we draw the weight matrix in
Cartesian coordinates.) This determines the entries of P. The entries of Q are given by similar
formulae using T(W t) = (Q, P). We note here the following identity, which follows from the above
lattice path representation for T: setting p = n ∧m, we have
(3.10)
p
X
i=1
1
wi,p−i+1
= 1
t11
.
To see this if n ≤m, take the ratio of (3.9) for Π(n−1)
n,n
and Π(n)
n,n. In the opposite case apply the
same to W t.
11


## Page 12


Now, for X ∈(R>0)n×m and s ∈C, deﬁne
(3.11)
Es(X) =
s
x11
+
X
ij
xi−1,j + xi,j−1
xij
,
where the summation is over 1 ≤i ≤n, 1 ≤j ≤m with the conventions xij = 0 for i = 0 or j = 0.
Note that, if X = (P, Q), then
Es(X) =



F0(P) + Fs(Q)
n ≥m
Fs(P) + F0(Q)
n ≤m
where Fs is deﬁned by (2.10). An important property of the maps bij deﬁned by (3.5) above is that
they preserve the quantity E0(X), that is, E0 ◦bij = E0. To see this, recall that the map bij takes a
matrix X = (xqr) and replaces the entry xij by
x′
ij = 1
xij
(xi,j−1 + xi−1,j)

1
xi+1,j
+
1
xi,j+1
−1
,
leaving the other entries unchanged, with the conventions that x0j = xi0 = 0, xn+1,j = xi,m+1 = ∞
for 1 < i < n and 1 < j < m, and x10 + x01 = x−1
n+1,m + x−1
n,m+1 = 1. It is readily veriﬁed that
(3.12)
x′
i,j−1 + x′
i−1,j
x′
ij
+
x′
ij
x′
i+1,j
+
x′
ij
x′
i,j+1
= xi,j−1 + xi−1,j
xij
+
xij
xi+1,j
+
xij
xi,j+1
with the conventions that x0j = xi0 = x′
0j = x′
i0 = 0 and xn+1,j = xi,m+1 = x′
n+1,j = x′
i,m+1 = ∞
for each i and j. This implies E0(bij(X)) = E0(X). We remark that, in particular, this implies
E0 ◦hj = E0, F0 ◦tj = F0 for all j < m and, in the case m = n, F0 ◦qn−1 = F0, where qn−1 is the
geometric analogue of Sch¨utzenberger’s involution deﬁned by (3.7).
The cornerstone of the present paper is the following identity which, combined with Theo-
rem 3.1, explains the appearance of GL(n, R)-Whittaker functions in the context of geometric
RSK.
Theorem 3.2. Let W ∈(R>0)n×m, T = T(W) and s ∈C. Then
p
X
i=1
s
wi,p−i+1
+
X ′ 1
wij
= Es(T),
where p = n ∧m and P′ denotes the sum over 1 ≤i ≤n, 1 ≤j ≤m such that j ̸= p −i + 1.
Proof. From the identity (3.10), we can assume without loss of generality that s = 1. We will
prove the theorem by induction on n and m. The statement is immediate in the case n = m = 1.
Write Ri = Rn,m
i
, T = T n,m and En,m
s
for the mappings deﬁned above. Recall that T m,n(W t) =
[T n,m(W)]t, for any values of m and n. It therefore suﬃces to show that the proposition holds for
T n,m, assuming that n ≥m and that the proposition holds for T n−1,m.
Write Wn−1,m = (wij, 1 ≤i ≤n −1, 1 ≤j ≤m), S = T n−1,m(Wn−1,m) and T = T n,m(W).
Then
T = Rn,m
n
 
S
wn1 . . . wnm
!
,
12


## Page 13


and we are required to show that
En,m
1
(T) = En−1,m
1
(S) +
m
X
j=1
1
wnj
.
Now,
Rn,m
n
= ρn
m ◦· · · ◦ρn
2 ◦ρn
1
where
ρn
k = hk ◦rk = bn−k+1,1 ◦· · · ◦bnk ◦rk.
Set
T (0) =
 
S
wn1 . . . wnm
!
and, for k = 1, . . . , m,
T (k) = ρn
k ◦· · · ◦ρn
2 ◦ρn
1(T (0)).
For X ∈(R>0)n×m and 0 ≤k ≤m, deﬁne
En,m;k(X) =
1
x11
+
(k)
X
ij
xi−1,j + xi,j−1
xij
+
m
X
j=k+1
1
xnj
,
where X = (xij) and the ﬁrst summation is over pairs of indices (i, j) such that either 1 ≤i < n
and 1 ≤j ≤m or i = n and 1 ≤j ≤k, with the conventions xij = 0 for i = 0 or j = 0. Note that
En,m;0(T (0)) = En−1,m
1
(T) +
m
X
j=1
1
wnj
,
En,m;m(T (m)) = En,m
1
(T).
We will show that
(3.13)
En,m;k ◦ρn
k = En,m;k−1
for each k = 1, . . . , m. Note that this implies
En,m;k(T (k)) = En,m;k−1(T (k−1))
for each k = 1, . . . , m, and the statement of the theorem follows.
Let X = (xij) ∈(R>0)n×m and write
X′ = (x′
ij) = ρn
k(X) = hk ◦rk(X).
Note that x′
ij = xij for all (i, j) except (n −q + 1, k −q + 1), 1 ≤q ≤k. Applying bnk ◦rk gives the
relation
x′
n,k−1 + x′
n−1,k
x′
nk
=
1
xnk
.
The next three relations follow from the invariance of E0 under the bij mappings as discussed earlier,
see (3.12). If (i, j) = (n −q + 1, k −q + 1) for some 1 < q < k, then
x′
i,j−1 + x′
i−1,j
x′
ij
+
x′
ij
x′
i+1,j
+
x′
ij
x′
i,j+1
= xi,j−1 + xi−1,j
xij
+
xij
xi+1,j
+
xij
xi,j+1
.
13


## Page 14


If k < n, then
x′
n−k,1
x′
n−k+1,1
+
x′
n−k+1,1
x′
n−k+2,1
+
x′
n−k+1,1
x′
n−k+1,2
=
xn−k,1
xn−k+1,1
+ xn−k+1,1
xn−k+2,1
+ xn−k+1,1
xn−k+1,2
;
If k = n (this can only occur if m = n), then
1
x′
11
+ x′
11
x′
21
+ x′
11
x′
12
=
1
x11
+ x11
x21
+ x11
x12
.
It follows that En,m;k(X′) = En,m;k−1(X), as required.
□
Let s > 0 and consider the measure on input matrices (wij) deﬁned by
νˆθ,θ;s(dw) =
Y
ij
w−ˆθi−θj
ij
exp
 
−
p
X
i=1
s
wi,p−i+1
−
X ′ 1
wij
! Y
ij
dwij
wij
,
where ˆθi + θj > 0 for each i and j. Note that
Z
(R>0)n×m νˆθ,θ;s(dw) = s−Pp
i=1(ˆθi+θp−i+1) Y
ij
Γ(ˆθi + θj).
Suppose W ∈(R>0)n×m and T = T(W) = (P, Q). Deﬁne a mapping σ : (R>0)n×m →(R>0)p by
(3.14)
σ(W) = sh P = sh Q = (tnm, tn−1,m−1, . . . , tn−p+1,m−p+1),
where p = n∧m. The next two corollaries are essentially a re-formulation of two of the main results
in [15].
Corollary 3.3. The push-forward of the measure νˆθ,θ;s under the geometric RSK map T is
given by
νˆθ,θ;s ◦T −1(dt) = P −θQ−ˆθe−Es(T) Y
ij
dtij
tij
.
Proof. This follows immediately from Theorems 3.1, 3.2 and the relation (3.8).
□
Corollary 3.4. The push-forward of νˆθ,θ;s under σ is given by
νˆθ,θ;s ◦σ−1(dx) =



Ψp
θ(x)Ψp
ˆθ;s(x) Qp
i=1
dxi
xi
n ≥m
Ψp
θ;s(x)Ψp
ˆθ(x) Qp
i=1
dxi
xi
n ≤m.
Proof. This follows from Corollary 3.3 and the integral formula (2.11) for Ψp
λ;s.
□
We also obtain from Theorems 3.1 and 3.2 the following integral identity. This is the analogue
of the Cauchy-Littlewood identity in this setting.
Corollary 3.5. Suppose s > 0, λ ∈Cm and ν ∈Cn, where n ≥m and ℜ(λi + νj) > 0 for all
i and j. Then
(3.15)
Z
(R>0)m Ψm
ν;s(x)Ψm
λ (x)
m
Y
i=1
dxi
xi
= s−Pm
i=1(νi+λi) Y
ij
Γ(νi + λj).
14


## Page 15


Proof. From the deﬁnitions (2.11), (3.11), the identity (3.8), Theorems 3.1 and 3.2, and
Fubini’s theorem,
s−Pm
i=1(νi+λi) Y
ij
Γ(νi + λj)
=
Z
(R>0)n×m
Y
ij
w−νi−λj−1
ij
exp
 
−
m
X
i=1
s
wi,m−i+1
−
X ′ 1
wij
! Y
ij
dwij
=
Z
(R>0)n×m P −λQ−νe−Es(T) Y
ij
dtij
tij
=
Z
(R>0)m
 Z
Πn(x)
Q−νe−Fs(Q)dQ
!  Z
Πm(x)
P −λe−F0(P )dP
! m
Y
i=1
dxi
xi
=
Z
(R>0)m Ψm
ν;s(x)Ψm
λ (x)
m
Y
i=1
dxi
xi
,
as required.
□
When m = n −1 this is equivalent to an integral identity which was conjectured by Bump [13]
and proved by Stade [39, Theorem 3.4], see Theorem 7.4 below. We note that in this case, the
identity is proved in [39] without assuming the condition ℜ(λi + νj) > 0 for all i and j.
In
this case, the integral is associated with archimedean L-factors of automorphic L-functions on
GL(n −1, R) × GL(n, R).
When n = m, (3.15) becomes:
Corollary 3.6. Suppose s > 0 and λ, ν ∈Cn, where ℜ(λi + νj) > 0 for all i and j. Then
Z
(R>0)n e−s/xnΨn
ν(x)Ψn
λ(x)
n
Y
i=1
dxi
xi
= s−Pn
i=1(νi+λi) Y
ij
Γ(νi + λj).
Using (2.4), this is equivalent to the following integral identity for GL(n, R)-Whittaker func-
tions, due to Stade [38], see Theorem 7.2 below.
Corollary 3.7 (Stade). Suppose r > 0 and λ, ν ∈Cn, where ℜ(λi + νj) > 0 for all i and j.
Then
Z
(R>0)n e−rx1Ψn
−ν(x)Ψn
−λ(x)
n
Y
i=1
dxi
xi
= r−Pn
i=1(νi+λi) Y
ij
Γ(νi + λj).
Again, we note that this identity is proved in [38] without assuming the condition ℜ(λi+νj) > 0
for all i and j.
In this case, the integral is associated, via the Rankin-Selberg method, with
Archimedean L-factors of automorphic L-functions on GL(n, R) × GL(n, R).
Corollary 3.8. Suppose s > 0 and ν ∈Cn with ℜνi > 0 for each i.
Then, for each
m ≤n, the function Ψm
ν;s is in L2((R>0)m, Qm
i=1 dxi/xi), and the function e−sx1Ψn
−ν(x) is in
L2((R>0)n, Qn
i=1 dxi/xi).
15


## Page 16


Proof. The ﬁrst claim follows from Corollary 3.5 and the Plancherel theorem, as follows. We
ﬁrst note that, under the above hypotheses,
ˆΨm
ν;s(λ) = s−Pm
i=1(νi+λi) Y
ij
Γ(νi + λj) ∈L2(ιRm, sm(λ)dλ).
This is easily veriﬁed using Stirling’s approximation
lim
b→∞|Γ(a + ιb)|e
π
2 |b||b|
1
2−a =
√
2π,
a, b ∈R.
Now, suppose f ∈L2((R>0)m, Qm
i=1 dxi/xi) such that ˆf is continuous and compactly supported
on ιRm. By the Plancherel theorem, such functions are dense in L2((R>0)m, Qm
i=1 dxi/xi) and,
moreover, satisfy
(3.16)
f(x) =
Z
ιRm
ˆf(λ)Ψm
λ (x)sm(λ)dλ
almost everwhere. Indeed, for any g ∈L2((R>0)m, Qm
i=1 dxi/xi) which is continuous and compactly
supported we have, by Fubini’s theorem,
Z
(R>0)m
Z
ιRm
ˆf(λ)Ψm
λ (x)sm(λ)dλ

g(x)
m
Y
i=1
dxi
xi
=
Z
ιRm
ˆf(λ)ˆg(λ)sm(λ)dλ
=
Z
(R>0)m f(x)g(x)
m
Y
i=1
dxi
xi
.
This implies (3.16). Now, by Corollary 3.5,
Z
(R>0)m |Ψm
ν;s(x)Ψm
λ (x)|
m
Y
i=1
dxi
xi
≤
Z
(R>0)m Ψm
ℜν;s(x)Ψm
0 (x)
m
Y
i=1
dxi
xi
< ∞.
It follows that, for f ∈L2((R>0)m, Qm
i=1 dxi/xi) such that ˆf is continuous and compactly supported
on ιRm, the integral
Z
(R>0)m
Z
ιRm Ψm
ν;s(x) ˆf(λ)Ψm
λ (x)sm(λ)dλdxi
xi
is absolutely convergent, and so, by Fubini’s theorem,
Z
(R>0)m Ψm
ν;s(x)f(x)
m
Y
i=1
dxi
xi
=
Z
(R>0)m Ψm
ν;s(x)
Z
ιRm
ˆf(λ)Ψm
λ (x)sm(λ)dλ
 m
Y
i=1
dxi
xi
=
Z
ιRm
ˆΨm
ν;s(λ) ˆf(λ)sm(λ)dλ.
Hence, using the Cauchy-Schwarz inequality,

Z
(R>0)m Ψm
ν;s(x)f(x)
m
Y
i=1
dxi
xi
 =

Z
ιRm
ˆΨm
ν;s(λ) ˆf(λ)sm(λ)dλ

≤
Z
ιRm |ˆΨm
ν;s(λ)|2sm(λ)dλ
1/2 Z
ιRm | ˆf(λ)|2sm(λ)dλ
1/2
.
This proves the ﬁrst claim.
The second claim follows from the ﬁrst, letting m = n and using
(2.4).
□
16


## Page 17


Consider the probability measure on input matrices W deﬁned by
˜νˆθ,θ;s(dw) = Z−1
ˆθ,θ;sνˆθ,θ;s(dw)
where
Zˆθ,θ;s = s−Pp
i=1(ˆθi+θi) Y
ij
Γ(ˆθi + θj).
The following result was obtained in [15].
Corollary 3.9. Suppose ˆθi + θj > 0 for each i and j, and (w.l.o.g.) that n ≥m, θi < 0 for
each i and ˆθj > 0 for each j. Then, the Laplace transform of the law ˜νˆθ,θ;s ◦t−1
nm of the polymer
partition function tnm under ˜νˆθ,θ;s is given by
Z
e−rtnm ˜νˆθ,θ;s(dw) =
Z
ιRm(rs)
Pm
i=1(θi−λi) Y
ij
Γ(λi −θj)
Y
ij
Γ(ˆθi + λj)
Γ(ˆθi + θj)
sn(λ)dλ.
Proof. By Corollary 3.4,
Z
e−rtnm˜νˆθ,θ;s(dw) = Z−1
ˆθ,θ;s
Z
(R>0)m e−rx1Ψm
θ (x)Ψm
ˆθ;s(x)
m
Y
i=1
dxi
xi
.
By Corollary 3.8, the functions e−rx1Ψm
θ (x) and Ψm
ˆθ;s(x) are in the space L2((R>0)m, Qm
i=1 dxi/xi).
The result follows, by Corollaries 3.6, 3.7 and the Plancherel theorem.
□
4. Equivalence of old and new description of geometric RSK
We explain here the equivalence of the Noumi-Yamada row insertion construction [32] and the
deﬁnition of geometric RSK given in Section 3. The input weight matrix (wij) is n × m, where m
is ﬁxed and n represents time. After n time steps the Noumi-Yamada process gives two patterns
P = {zkℓ} and Q = {z′
ij}.
P has height m, Q has height n, and their common shape vector
zm  = z′
n  is of length p = m ∧n. The rows of Q indexed by s = 1, . . . , n from top to bottom are
the successive shape vectors (bottom rows) zm (s) = (zm,ℓ(s))1≤ℓ≤m∧s of the temporal evolution
{z(s) : 1 ≤s ≤n} of the P pattern. Thus as in classic RSK the Q pattern serves as a recording
pattern.
The Noumi-Yamada process begins with an empty pattern at time n = 0. Then the following
step is repeated for n = 1, 2, 3, . . . .
Noumi-Yamada construction for time step n −1 →n. Let z = z(n −1) denote the P pattern
obtained after n −1 steps. Insertion of row wn  of weights into z transforms z into ˇz = z(n) as
follows.
(i) If n ≥m + 1 (in other words, the triangle was ﬁlled by time n −1), then
(4.1)
ak,1 = wn,k
for 1 ≤k ≤m
ak+1,ℓ+1 = ak+1,ℓ
zk+1,ℓˇzk,ℓ
ˇzk+1,ℓzk,ℓ
for 1 ≤ℓ≤k < m
ˇzk,ℓ= ak,ℓ(zk,ℓ+ ˇzk−1,ℓ)
for 1 ≤ℓ< k ≤m
ˇzk,k = ak,kzk,k
for 1 ≤k ≤m.
17


## Page 18


(ii) If n ≤m, then the equations above deﬁne ˇzk,ℓfor 1 ≤ℓ≤k ∧(n −1). Set
(4.2)
ˇzk,n = an,n · · · ak,n
for k = n, . . . , m,
while ˇzk,ℓfor ℓ≥n + 1 remain undeﬁned.
Proposition 4.1. Let (wij) be an n × m weight matrix and T = T(W) deﬁned by (3.3).
Then the output T is equivalent to the patterns (P, Q) obtained from n steps of the Noumi-Yamada
evolution, through these equations:
P pattern: zkℓ= tn−ℓ+1, k−ℓ+1,
1 ≤ℓ≤k ∧n, 1 ≤k ≤m
(4.3)
Q pattern: z′
sℓ= ts−ℓ+1, m−ℓ+1,
1 ≤ℓ≤m ∧s, 1 ≤s ≤n.
(4.4)
Note in particular the common shape vector zm  = z′
n  = (tn−ℓ+1,m−ℓ+1)1≤ℓ≤p. Here is an
illustration for n × m = 3 × 6.
(4.5)
T =


z33
z43
z53
z63 = z′
33
z′
22
z′
11
z22
z32
z42
z52
z62 = z′
32
z′
21
z11
z21
z31
z41
z51
z61 = z′
31


Proof of Proposition 4.1. We keep m ﬁxed and do induction on n. In the case n = 1, the
m-vector ˇz 1 described by equation (4.2) is the same as that obtained by applying R1 = πm
1
=
l1m ◦· · · ◦l11 to the top row w1  of the weight matrix.
Suppose the statement is true for T n−1,m. Add the nth weight row wn  to T n−1,m and call the
resulting n×m matrix eT n,m =
  T n−1,m
wn 

. Then T n,m = Rn( eT n,m). From the deﬁnition of Rn we see
that on row i ∈{1, . . . , n −1} it alters only elements ˜tij for j −i ≤m −n. Consequently after the
application of Rn, the induction assumption implies that (4.4) remains in force for 1 ≤s ≤n −1.
It only remains to check that (4.3) holds after the application of Rn.
Again we do induction, starting from the bottom row of T n,m and moving up row by row. This
corresponds to executing Rn = π(m−n)∨0+1
(n−m)∨0+1 ◦· · · ◦πm−1
n−1 ◦πm
n step by step.
Before applying πm
n , the two bottom rows of eT n,m are
eT n,m =


· · ·
· · ·
z11
z21
· · ·
zm1
wn1
wn2
· · ·
wnm

=


· · ·
· · ·
z11
z21
· · ·
zm1
a11
a21
· · ·
am1


18


## Page 19


where we used the ﬁrst row of (4.1). Apply πm
n = lnm ◦ln,m−1 ◦· · · ◦ln1. Only the bottom two rows
are impacted. Use the notation from (4.1).
"
z11
z21
z31
· · ·
zm1
a11
a21
a31
· · ·
am1
#
ln1
7−→
"
z11
z21
z31
· · ·
zm1
ˇz11
a21
a31
· · ·
am1
#
ln2
7−→
"
a22
z21
z31
· · ·
zm1
ˇz11
ˇz21
a31
· · ·
am1
#
ln3
7−→
"
a22
a32
z31
· · ·
zm1
ˇz11
ˇz21
ˇz31
· · ·
am1
#
ln4
7−→
· · ·
lnm
7−→
"
a22
a32
a42
· · ·
am2
zm1
ˇz11
ˇz21
ˇz31
· · ·
ˇzm−1,1
ˇzm1
#
Now the bottom row of T n,m is in place. Note that the transformations above left in place zm1 = z′
n1
as they should, for this entry is in accordance with (4.4).
Next, an application of πm−1
n−1 = ln−1,m−1 ◦ln−1,m−2 ◦· · · ◦ln−1,1 transforms rows n−2 and n−1
in this manner:


z22
z32
z42
· · ·
zm−1,2
z′
n2
z′
n−1,1
a22
a32
a42
· · ·
am−1,2
am2
z′
n1
ˇz11
ˇz21
ˇz31
· · ·
ˇzm−2,1
ˇzm−1,1
ˇzm1


πm−1
n−1
7−→


a33
a43
a53
· · ·
am−2,3
z′
n2
z′
n−1,1
ˇz22
ˇz32
ˇz42
· · ·
ˇzm−1,2
ˇzm2
z′
n1
ˇz11
ˇz21
ˇz31
· · ·
ˇzm−2,1
ˇzm−1,1
ˇzm1


The bottom two rows of T n,m are in place. These steps continue until we arrive at T n,m.
□
5. Symmetric input matrix
As it is needed in the following, we will write Rn,m
i
and T = T n,m for the mappings deﬁned
in (3.2)–(3.3), and note the following recursive structure. Let W = (wij) ∈(R>0)n×m and write
Wk,m = (wij, 1 ≤i ≤k, 1 ≤j ≤m). Recall that
T n,m = Rn,m
n
◦Rn,m
n−1 ◦· · · ◦Rn,m
1
.
Now, for each i ≤n, the mapping Rn,m
i
acts only on the ﬁrst i rows of W and leaves the remaining
rows of W unchanged. In fact, for each i ≤k ≤n, we have
Rn,m
i
(W) =
 
Rk,m
i
(Wk,m)
W c
k,m
!
,
where W c
k,m = (wij, k + 1 ≤i ≤n, 1 ≤j ≤m). This property is immediate from the deﬁnitions.
This gives the basic recursion
(5.1)
T n,m(W) = Rn,m
n
 
T n−1,m(Wn−1,m)
wn1 . . . wnm
!
.
Recall that
(5.2)
T m,n(W t) = [T n,m(W)]t.
19


## Page 20


In particular, if n = m and W is symmetric, then T n,n(W) is also symmetric.
Lemma 5.1. Suppose that n = m and W is symmetric.
(a) The following recursion holds:
(5.3)
T n,n(W) = Rn,n
n



"
Rn,n−1
n
 
T n−1,n−1(Wn−1,n−1)
w1n . . . wn−1,n
!#t
w1n . . . wnn


.
Moreover, if we denote by (sij) the elements of the (n −1) × n matrix
(5.4)
S =
"
Rn,n−1
n
 
T n−1,n−1(Wn−1,n−1)
w1n . . . wn−1,n
!#t
and by (tij) the elements of T n,n(W), then
(5.5)
tij = sij
for 1 ≤i < j ≤n
t11 = s12/2s11
tii = si,i+1si−1,i/sii
for 2 ≤i ≤n −1
tnn = 2sn−1,nwnn.
(b) For n ≥1 we have this identity:
(5.6)
4⌊n/2⌋
n
Y
i=1
wii =
⌊n−1
2 ⌋
Y
j=0
tn−2j, n−2j
⌊n−2
2
⌋
Y
j=0
tn−1−2j, n−1−2j
=
Y
i odd
zni
Y
i even
zni
.
Proof. Part (a). Using (5.1), (5.2) and the fact the W is symmetric,
T n,n(W) = Rn,n
n
 
T n−1,n(Wn−1,n)
wn1 . . . wnn
!
= Rn,n
n
 
T n,n−1([Wn−1,n]t)
t
wn1 . . . wnn
!
= Rn,n
n
 
T n,n−1(Wn,n−1)
t
wn1 . . . wnn
!
= Rn,n
n



"
Rn,n−1
n
 
T n−1,n−1(Wn−1,n−1)
wn1 . . . wn,n−1
!#t
wn1 . . . wnn



= Rn,n
n



"
Rn,n−1
n
 
T n−1,n−1(Wn−1,n−1)
w1n . . . wn−1,n
!#t
w1n . . . wnn


.
20


## Page 21


This proves the ﬁrst claim. So we have
T n,n(W) = Rn,n
n
 
S
w1n . . . wnn
!
,
where S ∈(R>0)(n−1)×n. To prove the second claim, ﬁrst note that the mapping Rn,n
n
leaves the
elements of its input matrix which are strictly above the diagonal unchanged. Thus, tij = sij for
1 ≤i < j ≤n. Using this, the symmetry of T, and recalling how the row insertion procedure works
(see Section 4), we see that
tnn = wnn(tn−1,n + sn−1,n) = 2sn−1,nwnn,
tn−1,n−1 =
tn−1,nsn−1,n
sn−1,n−1(tn−1,n + sn−1,n)(tn−2,n−1 + sn−2,n−1)
= sn−1,nsn−2,n−1/sn−1,n−1,
and so on; for 2 ≤i ≤n −1 we have tii = si,i+1si−1,i/sii and then ﬁnally,
t11 =
t12s12
s11(t12 + s12) = s12/2s11,
as required.
Part (b). The second equality in (5.6) is a consequence of (4.3). The ﬁrst equality is proved by
induction on n. Cases n = 2 and n = 3 are checked by hand.
Suppose (5.6) is true for n −1. Observe ﬁrst from the deﬁnition of the mappings that Rn,n−1
n
operating on
 T n−1,n−1
w1n ... wn−1,n

does not alter the diagonal {tn−1
ii
}1≤i≤n−1 of T n−1,n−1. Consequently
(5.4) implies that sii = tn−1
ii
for 1 ≤i ≤n −1.
Suppose n is even. Then the middle fraction of (5.6) develops as follows, through equations
(5.5), sii = tn−1
ii
and by induction:
tnntn−2,n−2 · · · t22
tn−1,n−1tn−3,n−3 · · · t11
=
2sn−1,nwnn · sn−2,n−1sn−3,n−2
sn−2,n−2
· · · s23s12
s22
sn−1,nsn−2,n−1
sn−1,n−1
· sn−3,n−2sn−4,n−3
sn−3,n−3
· · · s12
2s11
= 4wnn · sn−1,n−1sn−3,n−3 · · · s11
sn−2,n−2sn−4,n−4 · · · s22
= 4wnn · 4
n
2 −1
n−1
Y
i=1
wii = 4⌊n/2⌋
n
Y
i=1
wii.
The case of odd n develops similarly except that now the product in the numerator ﬁnishes with
s12/2s11 and consequently the factors of 2 cancel each other.
□
Theorem 5.2. Suppose that n = m and W is symmetric. Then T = T(W) = (tij) is also
symmetric, and the Jacobian of the map
(log wij, 1 ≤i ≤j ≤n) 7→(log tij, 1 ≤i ≤j ≤n)
is ±1.
21


## Page 22


Proof. We prove this by induction on n. When n = 2, we have t11 = w12/2, t12 = w11w12,
t22 = 2w11w12w22 and the result is immediate. Now, by the previous lemma,
T = Rn,n
n



"
Rn,n−1
n
 
T n−1,n−1(Wn−1,n−1)
w1n . . . wn−1,n
!#t
w1n . . . wn−1,n wnn


.
Denoting by (sij) the elements of the matrix
S =
"
Rn,n−1
n
 
T n−1,n−1(Wn−1,n−1)
w1n . . . wn−1,n
!#t
,
we have, by the previous lemma,
(5.7)
tij = sij
for 1 ≤i < j ≤n
t11 = s12/2s11
tii = si,i+1si−1,i/sii
for 2 ≤i ≤n −1
tnn = 2sn−1,nwnn
This expresses the n(n + 1)/2 variables tij, 1 ≤i ≤j ≤n as a function, which we shall denote by
F, of the n(n + 1)/2 variables sij, 1 ≤i < j ≤n and s11, . . . , sn−1,n−1, wnn.
Denote by tn−1
ij
the elements of the symmetric matrix T n−1,n−1(Wn−1,n−1). By the induction
hypothesis, the map
(log wij, 1 ≤i ≤j ≤n −1) 7→(log tn−1
ij
, 1 ≤i ≤j ≤n −1)
has Jacobian ±1. The mapping Rn,n−1
n
on the whole of (R>0)n×(n−1) is a composition of lij-maps
and hence has Jacobian ±1 in logarithmic variables; since it leaves matrix elements above the
diagonal unchanged, its restriction to the space of matrix elements on and below the diagonal also
has Jacobian ±1 in logarithmic variables. It follows that the mapping
(log wij, 1 ≤i ≤j < n; log win, 1 ≤i < n)
7→(log sij, 1 ≤i < j ≤n; log sii, 1 ≤i < n)
has Jacobian ±1. It therefore remains only to show that the Jacobian sub matrix of the map F
(in logarithmic variables) which corresponds to the variables (log s11, . . . , log sn−1,n−1, log wnn) and
(log t11, . . . , log tnn) has determinant ±1. From (5.7), this sub matrix is given by








log s11
log s22
· · ·
log sn−1,n−1
log wnn
log t11
−1
log t22
−1
...
...
log tn−1,n−1
−1
log tn,n
1








,
which completes the proof.
□
22


## Page 23


Consider the measure on symmetric input matrices with positive entries deﬁned by
να,ζ(dw) =
Y
i<j
w−αi−αj
ij
Y
i
w−αi−ζ
ii
exp

−
X
i<j
1
wij
−
X
1
2wii

Y
i≤j
dwij
wij
,
(5.8)
where α ∈Rn and ζ ∈R satisfy αi + ζ > 0 for each i and αi + αj > 0 for i ̸= j. Note that
Z
(R>0)n(n+1)/2 να,ζ(dw) = 2
Pn
i=1(αi+ζ) Y
i
Γ(αi + ζ)
Y
i<j
Γ(αi + αj).
In this setting we have R = C and so, using (3.8) and Lemma 5.1(b),
Y
i<j
w−αi−αj
ij
Y
i
w−αi−ζ
ii
= 4⌊n/2⌋ζ Y
i
z(−1)iζ
ni
R−α.
Thus, by Theorems 3.2 and 5.2, we obtain the following result.
Corollary 5.3. The push-forward of να,ζ under σ is given by
(5.9)
να,ζ ◦σ−1(dx) = 4⌊n/2⌋ζf(x)ζe−
1
2xn Ψn
α(x)
n
Y
i=1
dxi
xi
,
where
f(x) =
Y
i
x(−1)i
i
.
If λ ∈Cn and γ ∈C satisfy ℜ(λi + γ) > 0 for each i, and ℜ(λi + λj) > 0 for i ̸= j, then
Z
(R>0)n f(x)γe−
1
2xn Ψn
λ(x)
n
Y
i=1
dxi
xi
= 4−⌊n/2⌋γ2
Pn
i=1(λi+γ) Y
i
Γ(λi + γ)
Y
i<j
Γ(λi + λj).
Now, using (2.2) we can strengthen this to:
Corollary 5.4. Suppose λ ∈Cn and γ ∈C satisfy ℜ(λi+γ) > 0 for each i, and ℜ(λi+λj) > 0
for i ̸= j. Then, for s > 0,
Z
(R>0)nf(x)γe−s/xnΨn
λ(x)
n
Y
i=1
dxi
xi
= cn(s, γ)s−Pn
i=1 λi Y
i
Γ(λi + γ)
Y
i<j
Γ(λi + λj),
where
cn(s, γ) =



1
if n is even,
s−γ
if n is odd.
23


## Page 24


By (2.4) this is equivalent to the following identity which is equivalent to an integral identity
conjectured by Bump and Friedberg [14] and proved by Stade [39, Theorem 3.3], see Theorem 7.5
below. We note that in [39] the corresponding statement is proved without any restrictions on
the parameters. This integral is associated with an archimedean L-factor of an exterior square
automorphic L-function on GL(n, R).
Corollary 5.5 (Stade). Suppose λ ∈Cn and γ ∈C satisfy ℜ(λi + γ) > 0 for each i, and
ℜ(λi + λj) > 0 for i ̸= j. Then, for s > 0,
Z
(R>0)nf(x′)γe−sx1Ψn
−λ(x)
n
Y
i=1
dxi
xi
= cn(s, γ)s−Pn
i=1 λi Y
i
Γ(λi + γ)
Y
i<j
Γ(λi + λj),
where x′
i = 1/xn−i+1.
Note that f(x′) = f(x) if n is even and f(x′) = 1/f(x) if n is odd.
Now, consider the probability measure on symmetric matrices with positive entries deﬁned by
(5.10)
˜να,ζ(dw) = Z−1
α,ζνα,ζ(dw),
where
Zα,ζ = 2
Pn
i=1(αi+ζ) Y
i
Γ(αi + ζ)
Y
i<j
Γ(αi + αj).
From Corollary 5.3, we obtain:
Corollary 5.6. The Laplace transform of the law of the polymer partition function tnn under
˜να,ζ is given for r > 0 by
Z
e−rtnn ˜να,ζ(dw) = 4⌊n/2⌋ζZ−1
α,ζ
Z
(R>0)n f(x)ζe−rx1−
1
2xn Ψn
α(x)
n
Y
i=1
dxi
xi
.
Remark: A formal computation. We formally rewrite the above integral formula in terms
of a multiple contour integral that should be amenable to asymptotic analysis. Let ǫ > 0 and
set α′
i = αi + ǫ.
It follows from Corollary 3.6 (or 3.8) that the function e−
1
2xn Ψn
α′(x) is in
L2((R>0)n, Qn
i=1 dxi/xi). Moreover, by Corollary 3.6, for λ ∈ιRn,
(5.11)
Z
(R>0)n e−
1
2xn Ψn
α′(x)Ψn
λ(x)
n
Y
i=1
dxi
xi
= 2
P
i(λi+αi+ǫ) Y
i,j
Γ(αi + λj + ǫ).
Thus, by the Plancherel theorem, for any g ∈L2((R>0)n, Qn
i=1 dxi/xi) we can write
Z
(R>0)n g(x)e−
1
2xn Ψn
α′(x)
n
Y
i=1
dxi
xi
=
Z
ιRn ˆg(λ)2
P
i(λi+αi+ǫ) Y
i,j
Γ(αi + λj + ǫ)sn(λ)dλ.
(5.12)
24


## Page 25


Suppose n is even. By Corollary 5.5, if r > 0 and ℜλi > 0 for each i,
Z
(R>0)n f(x)ζe−rx1Ψn
−λ(x)
n
Y
i=1
dxi
xi
= r−Pn
i=1 λi Y
i
Γ(λi + ζ)
Y
i<j
Γ(λi + λj).
By (2.3) it follows that, for ǫ > 0 and λ ∈ιRn,
Z
(R>0)n f(x)ζe−rx1
 Y
i
xǫ
i
!
Ψn
−λ(x)
n
Y
i=1
dxi
xi
(5.13)
= r−Pn
i=1(λi+ǫ) Y
i
Γ(λi + ζ + ǫ)
Y
i<j
Γ(λi + λj + 2ǫ).
Formally, combining (5.11), (5.13) and (5.12) yields the following integral formula for the
Laplace transform of the law of the polymer partition function tnn under the probability mea-
sure ˜να,ζ :
Z
e−rtnn ˜να,ζ(dw) =
Z
ιRn
r
2
−P
i(λi+ǫ) Y
i
Γ(λi + ζ + ǫ)
Γ(αi + ζ)
Y
i,j
Γ(αi + λj + ǫ)
(5.14)
×
Y
i<j
Γ(λi + λj + 2ǫ)
Γ(αi + αj)
sn(λ)dλ
or, equivalently,
Z
e−rtnn ˜να,ζ(dw)
(5.15)
=
Z r
2
−P
i λi Y
i
Γ(λi + ζ)
Γ(αi + ζ)
Y
i,j
Γ(αi + λj)
Y
i<j
Γ(λi + λj)
Γ(αi + αj)sn(λ)dλ
where the integration is along vertical lines with ℜλi > 0 for each i. If n is odd, we similarly formally
obtain, this time using Theorem 7.4 instead of Corollary 5.5 because in this case f(x′)ζ = f(x)−ζ
and ζ > 0,
Z
e−rtnn ˜να,ζ(dw)
(5.16)
=
Z r
2
−P
i λi Y
i
Γ(λi −ζ)
Γ(αi + ζ)
Y
i,j
Γ(αi + λj)
Y
i<j
Γ(λi + λj)
Γ(αi + αj)sn(λ)dλ
where the integration is along vertical lines with ℜλi > 0 for each i. It seems reasonable to expect
the integral formulas (5.15) and (5.16) to be valid, at least in some suitably regularised sense.
6. Geometric RSK for triangular arrays and paths below a hard wall
In this section we introduce a birational, geometric RSK type mapping T △
n that maps triangular
arrays Xn = (xij, 1 ≤j < i ≤n) to triangular arrays T = (tij, 1 ≤j < i ≤n), both with positive
real entries. The motivation comes from the symmetric polymer of Section 5, with a (de)pinning
parameter ζ that tends to inﬁnity. This will become clear later on in Proposition 6.4 (see also the
25


## Page 26


remarks at the end of the section). Notions like the type and the shape can be deﬁned also for this
mapping. We prove that it satisﬁes a version of the fundamental identity (3.2) and preserves volume
in logarithmic variables. Moreover, we can relate the shape to partition functions of nonintersecting
paths below a “hard wall”, that is, paths restricted to {(i, j): j < i}.
For n = 2 the mapping is deﬁned by
T △
2 (x21) = x21.
(6.1)
For n ≥3 we deﬁne inductively
T △
n (Xn) = R△
n
 
T △
n−1(Xn−1)
xn1 . . . xn,n−1
!
,
(6.2)
with Xn−1 = (xij, 1 ≤j < i ≤n −1) and
R△
n = ρ△,n
n−1 ◦· · · ◦ρ△,n
1
(6.3)
where
(6.4)
ρ△,n
j
= ρn
j
for j = 1, . . . , n −2,
and
ρ△,n
n−1 = b△,n
2,1 ◦· · · ◦b△,n
n−1,n−2 ◦b△,n
n,n−1 ◦r△
n,n−1,
and ρn
j is deﬁned in (3.4). To complete the deﬁnition of T △
n
we deﬁne the mappings b△,n
j,j−1 and
r△
n,n−1 on a triangular array Xn = (xij, 1 ≤j < i ≤n). This is done as follows. The mapping
r△
n,n−1 replaces xn,n−1 by 1/xn,n−1. Observing the conventions xi0 = xn+1,n−1 = 1, make these
deﬁnitions:
• For k = 0, 1, 2, . . . , ⌊n
2 ⌋−1, b△,n
n−2k,n−2k−1 replaces xn−2k,n−2ki−1 with
x′
n−2k,n−2k−1
=
xn−2k+1,n−2k−1 xn−2k,n−2k−2
xn−2k,n−2k−1
.
(6.5)
• For k = 1, 2, . . . , ⌊n−1
2 ⌋, b△,n
n−2k+1,n−2k is the identity mapping.
We present explicitly the cases n = 3, 4 to clarify the deﬁnitions. For n = 3,
T △
3
 
x21
x31
x32
!
= ρ△,3
2
◦ρ△,3
1
 
T △
2 (x21)
x31
x32
!
= ρ△,3
2
◦ρ△,3
1
 
x21
x31
x32
!
= ρ△,3
2
 
x21
x21x31
x32
!
=
 
x21
x21x31
x21x31x32
!
.
26


## Page 27


For n = 4,
T △
4



x21
x31
x32
x41
x42
x43


= ρ△,4
3
◦ρ△,4
2
◦ρ△,4
1



T △
3
 
x21
x31
x32
!
x41
x42
x43



= ρ△,4
3
◦ρ△,4
2
◦ρ△,4
1



x21
x21x31
x21x31x32
x41
x42
x43



= ρ△,4
3
◦ρ△,4
2



x21
x21x31
x21x31x32
x21x31x41
x42
x43



= ρ△,4
3



x21
x21x32x41
x32+x41
x21x31x32
x21x31x41
x21x31x42(x32 + x41)
x43



=



x32x41
x32+x41
x21x32x41
x32+x41
x21x31x32
x21x31x41
x21x31x42(x32 + x41)
x21x31x42x43(x32 + x41)


.
For a triangular array X = (xij, 1 ≤j < i ≤n) deﬁne
E△(X) =
1
x21
+
X
j≤i−1
xi−1,j + xi,j−1
xij
,
with the convention that xi0 = xii = 0 for i = 1, . . . , n. Here is the analogue of Theorem 3.2 for
triangular arrays.
Theorem 6.1. Let Wn = (wij, 1 ≤j < i ≤n ) with wij ∈R>0.
Then the output array
Tn = T △
n (W) satisﬁes
E△(Tn) =
X
1≤j<i≤n
1
wij
.
(6.6)
Proof. We will show that
E△(Tn) = E△(T △
n−1(Wn−1)) +
n−1
X
j=1
1
wnj
.
To this end, let T 0 = T △
n−1(Wn−1) and T k = ρ△,n
k
◦· · · ◦ρ△,n
1
(T △
n−1(Wn−1)) for k = 1, 2, . . . , n −1.
For a triangular array X deﬁne
E△,n,k(X) =
1
x21
+
(k)
X
i,j
xi−1,j + xi,j−1
xij
+
n−1
X
j=k+1
1
xij
,
27


## Page 28


where summation P(k)
ij
is over all indices (i, j) such that 1 ≤j < i ≤n, but (i, j) ̸= (n, k +
1), . . . , (n, n −1). The boundary conventions xi0 = xii = 0 are still in force. We will show that
E△,n,k(T k) = E△,n,k−1(T k−1)
for k = 1, 2, . . . , n −1,
and this will conclude the proof. Notice that for k = 1, 2, . . . , n −2 this fact is already included in
the proof of Theorem 3.2, since ρ△,n
i
= ρn
i for i ≤n −2. To check the case k = n −1, let X = T n−2
and X′ = ρ△,n
n−1(X) = T n−1. Since ρ△,n
n−1 alters only the elements xi,i−1, i = 2, . . . , n, and leaves the
rest unchanged,
E△,n,n−1(X′) = E△,n,n−1(ρ△,n
n−1(X)) =
1
x′
2,1
+
X
j<i
x′
i−1,j + x′
i,j−1
x′
ij
= ˜
X
j<i−1
xi−1,j + xi,j−1
xij
+
1
x′
2,1
+
x′
2,1
x3,1
+
n−1
X
i=3
xi,i−2
x′
i,i−1
+
x′
i,i−1
xi+1,i−1

+ xn,n−2
x′
n,n−1
(6.7)
where in the summation ˜P we set appearances of terms xi,i−1, i = 2, . . . , n, equal to zero. Consider
the three parts of line (6.7).
First
1
x′
21
+ x′
21
x31
=
1
x21
+ x21
x31
because either n is odd and x′
21 = x21, or n is even and x′
21 = x31/x21. The middle terms satisfy
xi,i−2
x′
i,i−1
+
x′
i,i−1
xi+1,i−1
= xi,i−2
xi,i−1
+
xi,i−1
xi+1,i−1
,
either by virtue of (6.5) if i = n −2k, or because x′
i,i−1 = xi,i−1 when i = n −2k + 1. Finally,
x′
n,n−2
x′
n,n−1
=
1
xn,n−1
by (6.5) and the deﬁnition of r△
n,n−1. Making these substitutions on line (6.7) converts E△,n,n−1(X′)
into E△,n,n−2(X) and completes the proof.
□
The following theorem states the volume preserving property of the map T △
n . It follows from
the volume preservation of the individual steps in (6.4).
Theorem 6.2. Let W = (wij, 1 ≤j < i ≤n) ∈(R>0)n(n−1)/2 as above, and consider the
mapping W 7→T △
n (W) = (tij, 1 ≤j < i ≤n). In logarithmic variables
(log wij, 1 ≤j < i ≤n) 7→(log tij, 1 ≤j < i ≤n)
has Jacobian equal to ±1.
28


## Page 29


Figure 2. A pair (π1, π2) ∈Π(2)
8 . We have used matrix representation, as opposed to
Cartesian coordinates. On the upper left the paths begin at (2, 1) and (3, 2). On the lower
right the paths end at (8, 7) and (7, 6). The diagonal (dashed line) runs from (1, 1) to (8, 8).
Consider a triangular array W = (wij, 1 ≤j < i ≤n) and the output pattern P △= T △
n (W) =
(tij, 1 ≤j < i ≤n). The shape of the pattern P △is deﬁned as
sh P △
=
sh T △
n (W) = (tn,n−1, tn−1,n−2, . . . , t21)
Our next goal is to relate the shape to ratios of partition functions. Let Π(r)
n
be the collec-
tion of r-tuples of non-intesecting nearest-neighbor lattice paths π1, . . . , πr that start at positions
(2, 1), (3, 2), . . . , (r + 1, r), end at positions (n, n −1), (n −1, n −2), . . . , (n −r + 1, n −r), and stay
strictly below the diagonal in the matrix picture, i.e. never leave the set {(i, j) : 1 ≤j < i ≤n}.
See Figure 2. Naturally 1 ≤r ≤n/2. Denote the partition sums by
zr =
X
(π1,...,πr)∈Π(r)
n
Y
(i,j)∈π1∪···∪πr
wij.
(6.8)
The deﬁnition includes the case of a path consisting of a single point, which happens when n is
even and r = n/2.
The next theorem states that the odd coordinates of the shape vector sh P △are given by ratios
of partition functions.
Theorem 6.3. Consider a triangular array W = (wij, 1 ≤j < i ≤n) ∈(R>0)n(n−1)/2,
the output pattern P △= T △
n (W) = (tij, 1 ≤j < i ≤n) and the partition functions zr, r =
1, 2, . . . , ⌊n/2⌋as deﬁned in (6.8). Then
(tn,n−1, tn−2,n−3, . . . , tn−2⌊n/2⌋+2,n−2⌊n/2⌋+1) = (z1, z2/z1, . . . , z⌊n/2⌋/z⌊n/2⌋−1).
29


## Page 30


The proof of this theorem will be presented after Proposition 6.4 below. Deﬁne an operator Λε
n
acting on n × n matrices W by
wij
7→
εwij,
i ̸= j
wn−2i,n−2i
7→
2ε2wwn−2i,n−2i,
i = 0, 1, . . . , ⌊n/2⌋−1
wn−2i+1,n−2i+1
7→
1
2wn−2i+1,n−2i+1,
i = 1, 2, . . . , ⌊n/2⌋−1,
and w11 7→1
2w11, if n is even, while w11 7→εw11, if n is odd.
Let W △
n
= (w△,n
ij
, 1 ≤j < i ≤n) be a given triangular array. Let W ε
n be the symmetric
n × n matrix with wε
ii = ε for 1 ≤i ≤n and wε
ij = w△,n
ij
for 1 ≤j < i ≤n. Finally, denote
by T ⋄
n(W △
n ) = (w⋄,n
ij , 1 ≤i, j ≤n) a symmetric n × n output matrix whose lower triangular part
(tij, 1 ≤j < i ≤n) agrees with the output array T △
n (W △
n ), while the diagonal elements (tii)i=1,...,n
are determined by
(6.9)
tn−2k,n−2k = tn−2k−1,n−2k−1 = tn−2k,n−2k−1
for k = 0, 1, . . .
and
t11 = 1
if n is odd.
Proposition 6.4. Let T n,n be the geometric RSK mapping on n × n matrices with positive
entries, deﬁned in (3.3), and W ε
n, Λε
n, T ⋄
n, W △
n as above. Then, as ε ց 0,
T n,n(W ε
n) = Λε
n ◦T ⋄
n(W △
n ) + Sε
n
(6.10)
where Sε
n is an n × n matrix of lower order terms, speciﬁcally
(6.11)
(Sε
n)ij = o(ε),
i ̸= j
(Sε
n)n−2i,n−2i = o(ε2),
i = 0, 1, . . . , ⌊n/2⌋−1
(Sε
n)n−2i+1,n−2i+1 = o(1),
i = 1, 2, . . . , ⌊n/2⌋−1
(Sε
n)1,1 =



o(ε),
n is odd
o(1),
n is even.
Proof. From (5.3) we have this recursion:
(6.12)
T n,n(W ε
n) = ρn
n ◦(ρn
n−1 ◦· · · ◦ρn
1)



"
Rn,n−1
n
 
T n−1,n−1(W ε
n−1)
wn1 . . . wn,n−1
!#t
w1n . . . wn,n−1 ε


.
Symmetry of W ε
n makes T n,n(W ε
n) also symmetric. Since ρn
n alters only diagonal elements, the
matrix must be symmetric just before the last application of ρn
n. The mappings ρn
n−1 ◦· · · ◦ρn
1
alter only entries strictly below the diagonal. Consequently we can skip the steps ρn
n−1 ◦· · · ◦ρn
1 if
we simply take the upper triangular part of the matrix just before and extend it to a symmetric
matrix. We insert one extra transposition and then keep the lower triangular instead of the upper
triangular part. In other words, let
W ′ = Rn,n−1
n
 
T n−1,n−1(W ε
n−1)
wn1 . . . wn,n−1
!
(an n × (n −1) matrix)
30


## Page 31


and deﬁne the symmetric matrix ˜W = { ˜wij, 1 ≤i, j ≤n} by ˜wij = w′
ij for 1 ≤j ≤i ∧(n −1) and
˜wnn = ε. Then T n,n(W ε
n) = ρn
n( ˜W). In particular, the part of T n,n(W ε
n) strictly below the diagonal
is already present in W ′.
We prove (6.10) by induction on n. Case n = 2 begins with W △
2 = (w21), from which
Λε
2 ◦T ⋄
2 (W △
2 ) =
 
1
2w21
εw21
εw21
2ε2w21
!
= T 2,2
 
ε
w21
w21
ε
!
= T 2,2(W ε
2 ).
Assume that
T n−1,n−1(W ε
n−1) = Λε
n−1 ◦T ⋄
n−1(W △
n−1) + Sε
n−1.
Abbreviate T ε = (tε
ij, 1 ≤i, j ≤n −1) = T n−1,n−1(W ε
n−1) so that the induction assumption reads:
tε
ij
=
εw⋄,n−1
ij
+ o(ε),
i ̸= j
tε
n−2i−1,n−2i−1
=
2ε2w⋄,n−1
n−2i−1,n−2i−1 + o(ε2),
i = 0, 1, . . .
tε
n−2i,n−2i
=
1
2w⋄,n−1
n−2i,n−2i + o(1),
i = 1, . . .
tε
11
=
εw⋄,n−1
11
+ o(ε),
if (n −1) is odd
=
1
2w⋄,n−1
11
+ o(1),
if (n −1) is even
We now perform the mapping
W ′ = ρn
n−1 ◦· · · ◦ρn
1
 
T n−1,n−1(W ε
n−1)
wn1 . . . wn,n−1
!
inductively. Assume that we have applied the transformations
ρn
k−1 ◦· · · ◦ρn
1,
k < n −1,
and this has resulted in output entries
w′
ij = εw⋄,n
ij + o(ε),
1 ≤j < k −(n −i), n −k + 1 < i ≤n,
where w⋄,n
ij
denotes the entries of the matrix T ⋄
n(W △
n ) (recall that the lower triangular part of
T ⋄
n(W △
n ) is identical to T △
n (W △
n )). This is readily checked when k −1 = 1. We will show that this
is also true after the transformation ρn
k. To this end, using the relations (3.6) and (3.5), we have
31


## Page 32


that
w′
nk
=
wnk(w′
n,k−1 + tε
n−1,k) = εwnk(w⋄,n
n,k−1 + w⋄,n−1
n−1,k) + o(ε) = εw⋄,n
n,k + o(ε),
w′
n−j,k−j
=
w′
n+1−j,k−j tε
n−j,k−j+1
tε
n−j,k−j
w′
n−j,k−j−1 + tε
n−j−1,k−j
w′
n+1−j,k−j + tε
n−j,k−j+1
=
(εw⋄,n
n+1−j,k−j + o(ε)) (εw⋄,n−1
n−j,k−j+1 + o(ε))
εw⋄,n−1
n−j,k−j + o(ε)
ε(w⋄,n
n−j,k−j−1 + w⋄,n−1
n−j−1,k−j) + o(ε)
ε(w⋄,n
n+1−j,k−j + w⋄,n−1
n−j,k−j+1) + o(ε)
=
ε
w⋄,n
n+1−j,k−j w⋄,n−1
n−j,k−j+1
w⋄,n−1
n−j,k−j
w⋄,n
n−j,k−j−1 + w⋄,n−1
n−j−1,k−j
w⋄,n
n+1−j,k−j + w⋄,n−1
n−j,k−j+1
+ o(ε)
=
εw⋄,n
n−j,k−j + o(ε),
and this veriﬁes the proposition for the above entries. The next step is to conﬁrm that w′
n−j,n−j−1 =
εw⋄,n
n−j,n−j−1 + o(ε) for j = 0, . . . , n −2. To this end, assume that we have performed the transfor-
mations ρn
n−2 ◦· · · ◦ρn
1 and then we operate with ρn
n−1. First for j = 0,
w′
n,n−1
=
wn,n−1(w′
n,n−2 + tε
n−1,n−1)
=
wn,n−1(εw⋄,n
n,n−2 + 2ε2w⋄,n−1
n−1,n−1 + o(ε))
=
εwn,n−1w⋄,n
n,n−2 + o(ε)
=
εw⋄,n
n,n−1 + o(ε).
For j > 0
w′
n−j,n−j−1 =
w′
n+1−j,n−j−1 tε
n−j,n−j
tε
n−j,n−j−1
w′
n−j,n−j−2 + tε
n−j−1,n−j−1
w′
n+1−j,n−j−1 + tε
n−j,n−j
.
To develop this further we distinguish between odd and even j. For even j,
w′
n−j,n−j−1
=
(εw⋄,n
n+1−j,n−j−1 + o(ε)) (1
2w⋄,n−1
n−j,n−j + o(1))
εw⋄,n−1
n−j,n−j−1 + o(ε)
×
εw⋄,n
n−j,n−j−2 + o(ε) + 2ε2w⋄,n−1
n−j−1,n−j−1 + o(ε2)
εw⋄,n
n+1−j,n−j−1 + o(ε) + 1
2w⋄,n−1
n−j,n−j + o(1)
=
ε
w⋄,n
n+1−j,n−j−1 w⋄,n
n−j,n−j−2
w⋄,n−1
n−j,n−j−1
+ o(ε)
=
εw⋄,n
n−j,n−j−1 + o(ε)
32


## Page 33


where the last step came from (6.5). In the odd case
w′
n−j,n−j−1
=
(εw⋄,n
n+1−j,n−j−1 + o(ε)) (2ε2w⋄,n−1
n−j,n−j + o(ε2))
εw⋄,n−1
n−j,n−j−1 + o(ε)
×
εw⋄,n
n−j,n−j−2 + o(ε) + 1
2w⋄,n−1
n−j−1,n−j−1 + o(1)
εw⋄,n
n+1−j,n−j−1 + o(ε) + 2ε2w⋄,n−1
n−j,n−j + o(ε2)
=
ε
w⋄,n−1
n−j,n−j w⋄,n−1
n−j−1,n−j−1
w⋄,n−1
n−j,n−j−1
+ o(ε)
=
εw⋄,n−1
n−j,n−j−1 + o(ε) = εw⋄,n
n−j,n−j−1 + o(ε).
The second last equality follows from the fact that T ⋄
n−1(W △
n−1) satisﬁes (6.9) with n replaced by
n −1. The last equality comes from the deﬁnition of b△,n
n−j,n−j−1 as the identity mapping (see the
bullet below (6.5)). In the case (n −j, n −j −1) = (2, 1) we need to distinguish between the case
n is even or odd. In the even case we have
w′
21
=
tε
11
w′
31tε
22
tε
21(w′
31 + tε
22)
=
(εw⋄,n−1
11
+ o(ε))
(εw⋄,n
31 + o(ε))(1
2w⋄,n−1
22
+ o(1))
(εw⋄,n−1
21
+ o(ε))(εw⋄,n
31 + o(ε) + 1
2w⋄,n−1
22
+ o(1))
=
εw⋄,n−1
11
w⋄,n
31
w⋄,n−1
21
+ o(ε) = ε w⋄,n
31
w⋄,n−1
21
+ o(ε) = εw⋄,n
21 + o(ε),
where the second to last equality follows from (6.9), since (n −1) is odd and therefore w⋄,n−1
11
= 1.
The case that n is odd follows similarly.
To complete the construction of T n,n(W ε
n), extend W ′ to the symmetric matrix ˜W as explained
above and deﬁne W ′′ = ρn
n( ˜W). By computations similar to the ones above and by symmetry,
the diagonal elements (w′′
ii)i=1,...,n satisfy w′′
n−2k,n−2k = 2ε2w⋄,n
n−2k,n−2k−1 and w′′
n−2k−1,n−2k−1 =
1
2w⋄,n
n−2k,n−2k−1 for k = 0, 1, . . . . The proof is then complete.
□
Proof of Theorem 6.3. Consider a symmetric, n × n, matrix, W ε
n, with diagonal weights,
wii = ε, i = 1, 2, . . . , n. Let vr denote the partition sum introduced in (3.9) with k = m = n:
(6.13)
vr =
X
(π1,...,πr)∈Π(r)
n,n
Y
(i,j)∈π1∪···∪πr
wij.
The key observation is the following. For 1 ≤k ≤⌊n/2⌋,
(6.14)
v2k =

k
Y
i=1
wiiwn−i+1,n−i+1

z2
k + V (2k + 1)
and
(6.15)
v2k−1 =

k
Y
i=1
wiiwn−i+1,n−i+1

2zk−1zk + V (2k + 1)
33


## Page 34


where z0 = 1, zr is deﬁned by (6.8), and the unspeciﬁc notation V (ℓ) represents any sum of products
of weights where each term contains at least ℓdiagonal weights wii.
To see the origin of (6.14)–(6.15), consider ﬁrst v1, the sum of products Q
(i,j)∈π wij over all
paths π from (1, 1) to (n, n). Those products that contain only weights w11wnn from the diagonal
correspond to paths that stay either strictly above or strictly below the diagonal, except at points
(1, 1) and (n, n). By the symmetry of the weights this gives two copies of z1. Similarly for v2, pairs
(π1, π2) that intersect the diagonal only at {(1, 1), (n, n)} correspond to pairs such that π2 connects
(1, 2) to (n −1, n) above the diagonal and π1 connects (2, 1) to (n, n −1) below the diagonal.
Weights of paths are multiplied, and so symmetry gives z2
1. The higher cases work the same way.
For the symmetric weight matrix the shape vector x = (x1, . . . , xn) is given by
(6.16)
x1 = v1,
xi = zn,i =
vi
vi−1
for 2 ≤i ≤n.
Here we recalled that the shape vector is the bottom row zn· of the P pattern, see (2.8), and
combined (3.9) with (4.3).
Since wii = ε, equations (6.14)–(6.16) combine to give the following asymptotics for k =
1, 2, . . . , ⌊n/2⌋as ε ց 0:
x1
=
v1
= 2ε2z1 + o(ε2),
x2k
=
v2k
v2k−1
=
ε2kz2
k + o(ε2k)
ε2k 2zk−1zk + o(ε2k) = 1
2
zk
zk−1
+ o(1),
x2k+1
=
v2k+1
v2k
= ε2(k+1) 2zkzk+1 + o(ε2(k+1))
ε2k z2
k + o(ε2k)
= 2ε2 zk+1
zk
+ o(ε2).
The proof can be now completed by comparing to (6.10) and using (6.9).
□
For a triangular array X = (xij, 1 ≤j < i ≤n) ∈(R>0)n(n−1)/2 we deﬁne its type, τ =
(τ n
j )0≤j≤n−1 = type X, as the vector with entries
τ n
j (X) =
Dnj(X)
Dn,j−1(X)
where
Dn0(X)
=
1
and
Dnj(X)
=
xnjxn−1,j−1 · · · xn−j+1,1,
j = 1, 2, . . . , n −1.
Proposition 6.5. Let Wn = (wij, 1 ≤j < i ≤n) with wij ∈R>0. We have
τ n
j (T △
n (Wn)) =
j−1
Y
ℓ=1
wj,ℓ
n
Y
k=j+1
wkj,
1 ≤j ≤n −1.
(6.17)
34


## Page 35


Proof. Let us ﬁrst notice that if X = (xij, 1 ≤j < i ≤n) is a triangular array and X′ =
ρ△,n
j
(X), then
x′
nj · · · x′
n−j+1,1
x′
n,j−1 · · · x′
n−j+2,1
= xnj
xn−1,j · · · xn−j,1
xn−1,j−1 · · · xn−j+1,1
,
j < n −1.
(6.18)
To check this we notice that ρ△,n
j
= ρn
j = hj ◦rj, where hj and rj are deﬁned in (3.6) via the
Bender-Knuth transformations. Let us recall that
(bij(X))ij = x′
ij = xi+1,j xi,j+1
xij
xi,j−1 + xi−1,j
xi+1,j + xi,j+1
,
(6.19)
with the same convention as in (3.5). Multiplying the various relations (6.19) for (i, j) = (n, j), . . . , (n−
j + 1, 1) leads to (6.18). Iterating this leads to
τ n
j (T △
n (Wn))
=
wn,j τ n−1
j
(T △
n−1(Wn−1))
=
wn,j · · · wj+2,j τ j+1
j
(T △
j+1(Wj+1)).
(6.20)
Denoting by w′
ij the elements of T △
j+1(Wj+1), by w†
ij the elements of T △
j (Wj) and using the trans-
formations in (6.5) we obtain that
τ j+1
j
(T △
j+1(Wj+1))
=
w′
j+1,j · · · w′
21
w′
j+1,j−1 · · · w′
31
=
wj+1,j
Q⌊j/2⌋−1
ℓ=0
w†
j−2ℓ,j−2ℓ−1
Q⌊(j−1)/2⌋−1
ℓ=0
w†
j−2ℓ−1,j−2ℓ−2
.
Using Theorem 6.3 we have that
⌊j/2⌋−1
Y
ℓ=0
w†
j−2ℓ,j−2ℓ−1 =
Y
1≤ℓ<k≤j
wkℓ.
The deﬁnition below (6.5) implies that w†
j−2ℓ−1,j−2ℓ−2 = T △
j−1(Wj−1)(j−1)−2ℓ,(j−1)−2ℓ−1 for ℓ=
0, . . . , ⌊(j −1)/2⌋−1 and using again Theorem 6.3 we obtain
⌊(j−1)/2⌋−1
Y
ℓ=0
w†
j−2ℓ−1,j−2ℓ−2 =
Y
1≤ℓ<k≤j−1
wkℓ.
Combining the last three relations gives
τ j+1
j
(T △
j+1(Wj+1)) = wj+1,j
Y
1≤ℓ<j
wjℓ,
and this completes the proof.
□
By combining Theorems 6.1 and 6.2 and Proposition 6.5 we identify the probability distribution
of the shape vector of the triangular array under inverse gamma weights. The mapping that gives
the shape vector is σ△: (R>0)n(n−1)/2 →(R>0)n−1 deﬁned by
σ△(W) = sh T △
n (W)
=
(tn,n−1, tn−1,n−2, . . . , t2,1).
(6.21)
35


## Page 36


Consider the probability measure
λα(dw) = Z−1
α
Y
1≤j<i≤n
w−αi−αj
ij
exp

−
X
1≤j<i≤n
1
wij

Y
1≤j<i≤n
dwij
wij
(6.22)
on the space of triangular arrays (wij, 1 ≤j < i ≤n) ∈(R>0)n(n−1)/2, where α = (α1, . . . , αn),
αi + αj > 0 and the normalisation is
Zα =
Y
1≤j<i≤n
Γ(αi + αj).
Corollary 6.6. For the λα-distributed triangular array of weights, the distribution of the shape
vector is given by
λα ◦(σ△)−1(dt)
=
Y
1≤j<i≤n
Γ(αi + αj)−1


Q⌊n−1
2
⌋−1
ℓ=0
tn−2ℓ−1,n−2ℓ−2
Q⌊n
2 ⌋−1
ℓ=0
tn−2ℓ,n−2ℓ−1


αn
e
−
1
t2,1 Ψn−1
α′
(t)
Y
0≤i≤n−2
dtn−i,n−i−1
tn−i,n−i−1
where α′ = (α1, . . . , αn−1).
Proof. Let T = (tij, 1 ≤j < i ≤n) = T △
n (W).
We convert the density (6.22) into tij
variables. By Proposition 6.5,
Y
j<i
w−αi−αj
ij
=
n
Y
j=1


j−1
Y
ℓ=1
wjℓ·
n
Y
k=j+1
wkj


−αj
=
n−1
Y
j=1
(τ n
j )−αj ·


n−1
Y
j=1
wnj


−αn
.
From the proof of Proposition 6.5 (after relation (6.20)),
⌊n/2⌋−1
Y
ℓ=0
tn−2ℓ,n−2ℓ−1
=
Y
1≤j<i≤n
wij
and
⌊(n−1)/2⌋−1
Y
ℓ=0
tn−2ℓ−1,n−2ℓ−2
=
Y
1≤j<i≤n−1
wij.
Combine these with Theorem 6.1 to obtain
Y
j<i
w−αi−αj
ij
exp

−
X
j<i
1
wij

=


Q⌊n−1
2 ⌋−1
ℓ=0
tn−2ℓ−1,n−2ℓ−2
Q⌊n
2 ⌋−1
ℓ=0
tn−2ℓ,n−2ℓ−1


αn
n−1
Y
j=1
(τ n
j )−αj e−E△(T).
By the volume preserving property of the W 7→T map (Theorem 6.2),
λα ◦(T △)−1(dt) =


Q⌊n−1
2 ⌋−1
ℓ=0
tn−2ℓ−1,n−2ℓ−2
Q⌊n
2 ⌋−1
ℓ=0
tn−2ℓ,n−2ℓ−1


αn
n−1
Y
j=1
(τ n
j )−αj e−E△(T) Y
j<i
dtij
tij
.
The result then follows by integrating over the variables (tij, 1 ≤j < i −1, 1 ≤i ≤n) and the
deﬁnition of the Whittaker function.
□
As a further corollary we record the distribution of the vector (z1, z2/z1, . . . , z⌊n/2⌋/z⌊n/2⌋−1) of
ratios of partition functions zr deﬁned by (6.8). The result comes by combining Corollary 6.6 with
Theorem 6.3.
36


## Page 37


Corollary 6.7. Let the array of weights (wij, 1 ≤j < i ≤n) have distribution λα of (6.22),
and as before α = (α1, . . . , αn) = (α′, αn). Then the distribution of the vector (z1, z2/z1, . . . , z⌊n/2⌋/z⌊n/2⌋−1),
with the partition functions zr deﬁned in (6.8), is given as follows in terms of the integral of a
bounded Borel function ϕ:
(6.23)
Z
ϕ(z1, z2/z1, . . . , z⌊n/2⌋/z⌊n/2⌋−1) λα(dw)
=
Y
1≤j<i≤n
Γ(αi + αj)−1
Z
(R>0)⌊n
2 ⌋
Y
0≤i≤n−2:
i even
dtn−i,n−i−1
tn−i,n−i−1
ϕ(tn,n−1, tn−2,n−3, . . . , tn−2⌊n
2 ⌋+2,n−2⌊n
2 ⌋+1)
×
Z
(R>0)⌈n/2⌉−1


Q⌊n−1
2
⌋−1
k=0
tn−2k−1,n−2k−2
Q⌊n
2 ⌋−1
k=0
tn−2k,n−2k−1


αn
e
−
1
t2,1 Ψn−1
α′
(t)
Y
1≤i≤n−2:
i odd
dtn−i,n−i−1
tn−i,n−i−1
.
The results above are related to those of symmetric weight matrices in several ways.
(i) Replace n with n −1 in Corollary 5.3 and consider a symmetric (n −1) × (n −1) weight
matrix with distribution (5.10), and set ζ = αn.
Let σ1 = tn−1,n−1 be the polymer partition
function of the symmetric matrix, or equivalently, the front element of its shape vector. Then a
comparison of (6.23) and (5.9) reveals that the distribution of the partition function z1 is identical
to the distribution of 2tn−1,n−1.
(ii) Corollary 6.6 can be obtained as the ζ →∞limit of Corollary 5.3. Using the recursive
structure (2.1) of Whittaker functions, namely Ψn
α = Qn,n−1
αn
Ψn−1
α′
, one can show that
˜να,ζ ◦σ−1
=⇒λα ◦(σ△)−1
as ζ →∞,
where “=⇒” denotes weak convergence of probability measures. Under the measure ˜να,ζ the diag-
onal element wii of the symmetric input matrix has probability distribution
ρii(du) = u−αi−ζ e−1/(2u)
2αi+ζΓ(αi + ζ) · du
u
on 0 < u < ∞,
and hence its reciprocal w−1
ii
is twice a gamma variable with parameter αi + ζ.
Consequently
ζwii →1/2 almost everywhere as ζ →∞. Thus wii decays as (1/2)ζ−1. This corresponds to the
appearance, in our proof, of triangular arrays with diagonal elements ε →0.
(iii) The limit ζ →∞, or equivalently ε →0, introduces a depinning eﬀect on the polymer,
which is responsible for the appearance of the hard wall phenomenon. It is also worth noting that
the structure of the measure λα ◦(σ△)−1 is similar to that of ˜να,ζ ◦σ−1. In other words it appears
that the hard wall produces also a “pinning” eﬀect along the line {(j, n), 1 ≤j ≤n}.
7. Whittaker integral identities
In this section, we recall three integral identities for Whittaker functions which were proved
in the papers [38, 39], and explain how they are equivalent to (and in fact generalized by) those
which have appeared naturally in the context of the present paper (Corollaries 3.5, 3.7 and 5.5).
We ﬁrst note that the functions Wn,a(y) introduced in Section 2 are denoted by Wn,2a(y) in the
37


## Page 38


papers [38, 39]. The following identity was conjectured by Bump [13] and proved by Stade [38,
Theorem 1.1].
Theorem 7.1 (Stade). For s ∈C, a, b ∈Cn with P
i ai = P
i bi = 0,
Z
(R>0)n−1 Wn,a(y)Wn,b(y)
n−1
Y
j=1
(πyj)2js(2y−j(n−j)
j
)dyj
yj
= Γ(ns)−1 Y
j,k
Γ(s + aj + bk).
(7.1)
This integral is associated, via the Rankin-Selberg method, with Archimedean L-factors of
automorphic L-functions on GL(n, R)×GL(n, R). Using (2.5), it is straightforward to see that this
is equivalent to:
Theorem 7.2 (Stade). Suppose r > 0 and λ, ν ∈Cn. Then
(7.2)
Z
(R>0)n e−rx1Ψn
−ν(x)Ψn
−λ(x)
n
Y
i=1
dxi
xi
= r−Pn
i=1(νi+λi) Y
ij
Γ(νi + λj).
Indeed, if we let
aj = λj −(1/n)
X
i
λi,
bj = νj −(1/n)
X
i
νi
and s = (1/n) P
i(λi + νi) then, using (2.5) and (2.3), (7.1) becomes
Γ(ns)
Z
(R>0)n−1 Ψn
−ν(x)Ψn
−λ(x)x−ns
1
2n−1
n−1
Y
j=1
dyj
yj
=
Y
ij
Γ(νi + λj),
where πyj =
p
xn−j+1/xn−j for j = 1, . . . , n−1. It is important to note here that we are regarding
Ψn
−ν(x)Ψn
−λ(x)x−ns
1
as a function of y1, . . . , yn−1. Now, writing
Γ(ns) =
Z ∞
0
xns
1 e−x1 dx1
x1
we can absorb this into the integral, changing variables from y1, . . . , yn−1, x1 to x1, . . . , xn, to obtain
Z
(R>0)n e−x1Ψn
−ν(x)Ψn
−λ(x)
n
Y
i=1
dxi
xi
=
Y
ij
Γ(νi + λj).
The identity (7.2) follows, using (2.2).
The second identity is a formula for the Mellin transform
Nn,b,a(s) =
Z
(R>0)n−1Wn,a(y1, . . . , yn−1)Wn−1,b(y1, . . . , yn−2)
n−1
Y
j=1
(πyj)2js(2y−j(n−j−1/2)
j
)dyj
yj
,
for s ∈C, n ≥3 and a ∈Cn, b ∈Cn−1 with P
i ai = P
j bj = 0. This integral is associated
with archimedean L-factors of automorphic L-functions on GL(n−1, R)×GL(n, R). The following
identity was conjectured by Bump [13] and proved by Stade [39, Theorem 3.4].
38


## Page 39


Theorem 7.3 (Stade).
Nn,b,a(s) =
Y
i,j
Γ(s + ai + bj).
Now, for λ ∈Cn and r > 0,
Ψn−1
λ;r (x1, . . . , xn−1) = rλnΨn
λ(x1, . . . , xn−1, r).
Using this, and the relations (2.5) and (2.4), it is straightforward to see that Theorem 7.3 is
equivalent to:
Theorem 7.4 (Stade). Let r > 0, λ ∈Cn−1 and ν ∈Cn. Then
(7.3)
Z
(R>0)n−1 Ψn−1
ν;r (x)Ψn−1
λ
(x)
n−1
Y
i=1
dxi
xi
= r−Pn−1
i=1 (νi+λi) Y
ij
Γ(νi + λj).
The third identity is a formula for the Mellin transform
Mn,a(s) =
Z
(R>0)n−1 Wn,a(y)
n−1
Y
j=1
(πyj)2sj(2y−j(n−j)/2
j
)dyj
yj
,
for particular values of s = (s1, . . . , sn−1) lying on a two-dimensional subspace of Cn−1.
This
integral is associated with an archimedean L-factor of an exterior square automorphic L-function
on GL(n, R). The following identity was conjectured by Bump and Friedberg [14] and proved by
Stade [39, Theorem 3.3].
Theorem 7.5 (Stade). Let s1, s2 ∈C and a ∈Cn with P
i ai = 0. Suppose that, for 2 <
j ≤n −1, sj = ǫ(j)s1 + (j −ǫ(j))s2/2, where ǫ(j) = 1 if j is odd and 0 otherwise. Set sn =
ǫ(n)s1 + (n −ǫ(n))s2/2. Then for s = (s1, . . . , sn−1),
(7.4)
Γ(sn)Mn,a(s) =
Y
i
Γ(s1 + ai)
Y
i<j
Γ(s2 + ai + aj).
In terms of the Ψn
λ, this is equivalent to the following identity, which is straightforward to verify
using (2.5) and (2.2) as above.
Theorem 7.6 (Stade). Suppose r > 0, λ ∈Cn and γ ∈C. Then
Z
(R>0)nf(x′)γe−rx1Ψn
−λ(x)
n
Y
i=1
dxi
xi
= cn(r, γ)r−Pn
i=1 λi Y
i
Γ(λi + γ)
Y
i<j
Γ(λi + λj),
where x′
i = 1/xn−i+1, f(x) = Q
i x(−1)i
i
and
cn(s, γ) =



1
if n is even,
s−γ
if n is odd.
Note that f(x′) = f(x) if n is even and f(x′) = 1/f(x) if n is odd.
39


## Page 40


8. Tropicalization, last passage percolation and random matrices
The geometric RSK correspondence is a geometric lifting of the (Berenstein-Kirillov extension
of the) RSK correspondence. Going the other way, let xǫ
ij = eyij/ǫ where Y = (yij) ∈Rn×m and
ǫ > 0. Let Xǫ = (xǫ
ij) and T ǫ = (tǫ
ij) = T(Xǫ). Then the mapping U : Rn×m →Rn×m deﬁned
by U(Y ) = (uij) where uij = limǫ→0 ǫ log tǫ
ij is the extension of the RSK mapping to matrices with
real entries introduced by Berenstein and Kirillov [8]. We identify the output U(Y ) with a pair of
patterns as before, but now the entries are allowed to take real values. In this context, we deﬁne a
real pattern of height h and shape x ∈Rn as an array of real numbers
R =
r11
r22
r21
...
...
rnn
. . .
rn1
...
...
rhn
. . .
rh1
with bottom row rh· = x. The range of indices is
L(n, h) = {(i, j) : 1 ≤i ≤h, 1 ≤j ≤i ∧n}.
Fix a real pattern R as above. Set s0 = 1 and, for 1 ≤i ≤h, si = Pi∧n
j=1 rij and ci = si −si−1. We
shall refer to c as the type of R and write c = type(R). Denote by Σh(x) the set of real patterns
with shape x and height h. We say that a real pattern R is a (generalized) Gelfand-Tsetlin pattern
if rnn ≥0 and it satisﬁes the interlacing property ri+1,j+1 ≤rij ≤ri+1,j for all (i, j) ∈L(n, h)
with i < h, with the conventions ri+1,n+1 = 0 for i = n, . . . , h −1. Denote the set of generalized
Gelfand-Tsetlin patterns with height h and shape x ∈Rn
+ by GT h(x). This is a Euclidean polytope
of dimension d = n(n −1)/2 + (h −n + 1)n. Denote the corresponding Euclidean measure by dR.
The analogue of the Whittaker functions in this setting are the functions Jλ(x) deﬁned, for λ ∈Ch
and x ∈Rn
+ by
Jλ(x) =
Z
GT h(x)
e−λ·type(R)dR.
Note that, from (2.11), we have
lim
ǫ→0 ǫdΨn
ǫλ;1(ex/ǫ) = Jλ(x).
If h = n then Jλ(x) = det(e−λixj)/∆(λ) where ∆(λ) = Q
i>j(λi −λj) (see, for example, [34]).
The analogue of Theorem 3.2 in this setting is the following. This result can be inferred directly
from results of [8] (see Property 8 after the statement of Theorem 1.1) or seen as a consequence of
Theorem 3.2. We identify the output U(Y ) with a pair of real patterns (R, S) of respective heights
m and n, and common shape (unm, . . . , un−p+1.n−p+1), where p = n ∧m.
Corollary 8.1. The output U(Y ) = (R, S) is a pair of generalized Gelfand-Tsetlin patterns
if, and only if, all of the entries of Y are non-negative.
40


## Page 41


We note that the corresponding statement for matrices with integer entries follows as a particu-
lar case. If Y has non-negative integer entries then the pair of generalized Gelfand-Tsetlin patterns
obtained can be interpreted in the usual way as the pair of semistandard tableaux obtained via the
RSK correspondence.
The Berenstein-Kirillov [8] deﬁnition of U in terms of lattice paths is given as follows. For
1 ≤k ≤m and 1 ≤r ≤n ∧k,
(8.1)
un−r+1,k−r+1 + · · · + un−1,k−1 + unk =
max
(π1,...,πr)∈Π(r)
n,k
X
(i,j)∈π1∪···∪πr
yij,
where Π(r)
n,k denotes the set of r-tuples of non-intersecting directed nearest-neighbor lattice paths
π1, . . . , πr starting at positions (1, 1), (1, 2), . . . , (1, r) and ending at positions (n, k−r+1), . . . , (n, k−
1), (n, k). (See Figure 1.) This determines the entries of R. The entries of S are given by similar
formulae using U(Y t) = (S, R). In particular,
(8.2)
unm = max
π∈Π(1)
n,m
X
(i,j)∈π
yij,
where Π(1)
n,m is the set of directed nearest-neighbor lattice paths in Z2 from (1, 1) to (n, m). This
formula provides a connection to last passage directed percolation which we will discuss shortly.
The formula (8.1) is the analogue of Greene’s theorem in this setting (see, for example, [18, §3.1]).
The local move description of Section 3 carries over to the tropical setting, as follows. For
convenience and clarity we adopt the same notation as in the geometric setting. For each 2 ≤i ≤n
and 2 ≤j ≤m deﬁne a mapping lij which takes as input a matrix Y = (yij) ∈Rn×m and replaces
the submatrix
 
yi−1,j−1
yi−1,j
yi,j−1
yij
!
of Y by its image under the map
(8.3)
 
a
b
c
d
!
7→
 
b ∧c −a
b
c
d + b ∨c
!
,
and leaves the other elements unchanged. For 2 ≤i ≤n and 2 ≤j ≤m, deﬁne li1 to be the
mapping that replaces the element yi1 by yi−1,1 + yi1 and l1j to be the mapping that replaces the
element y1j by y1,j−1 + y1j. As before we deﬁne l11 to be the identity map. For 1 ≤i ≤n and
1 ≤j ≤m, set
πj
i = lij ◦· · · ◦li1,
and, for 1 ≤i ≤n,
Ri =



πm−i+1
1
◦· · · ◦πm
i
i ≤m
π1
i−m+1 ◦· · · ◦πm
i
i ≥m.
Then the Berenstein-Kirillov map is given by
(8.4)
U = Rn ◦· · · ◦R1.
41


## Page 42


Now observe that each lij is invertible. Indeed, the inverse of the map (8.3) is given by
(8.5)
 
a
b
c
d
!
7→
 
b ∧c −a
b
c
d −b ∨c
!
,
and the boundary moves l1j, li1 are clearly invertible.
It follows that the map U is invertible.
Moreover, U preserves the Lebesgue measure on Rn×m. The Jacobians of the lij are clearly almost
everywhere equal to ±1. Combining this with Corollary 8.1 we conclude that the restriction of U
to Rn×m
+
is volume preserving with respect to the Euclidean measure, injective and its image is
given by the Euclidean set of pairs of generalized Gelfand-Tsetlin patterns with respective heights
m and n, having the same shape in
C(p) = {x ∈Rp
+ : x1 ≥· · · ≥xp}.
Finally, we recall the following straightforward fact. If we deﬁne row and column sums ri = P
j yij
and cj = P
i yij, then type(S) = r and type(R) = c. Note that this implies, for λ ∈Cm and ν ∈Cn,
(8.6)
X
ij
(νi + λj)yij =
X
i
νiri +
X
j
λjcj.
The analogue of the Cauchy-Littlewood identity in this setting (cf. Corollary 3.5) is thus given as
follows.
Proposition 8.2. Suppose λ ∈Cm and ν ∈Cn, where n ≥m and ℜ(λi + νj) > 0 for all i and
j. Then
(8.7)
Z
C(m) Jν(x)Jλ(x)
m
Y
i=1
dxi =
Y
ij
(νi + λj)−1.
This basic structure has been exploited in the papers [27, 4, 17, 11, 16] to study last passage
percolation models with exponential weights, as we shall now explain. We note that the development
in those papers is via a discrete approximation and as such diﬀers from the present framework, but
the main ideas are the same. Let a ∈Rn and b ∈Rm such that ai + bj > 0 for all i and j. Consider
the measure on input matrices (yij) ∈Rn×m
+
deﬁned by
νa,b(dy) =
Y
i,j
e−(ai+bj)yijdyij.
From the above, it follows that the push-forward of νa,b under the map U is given by
νa,b ◦U −1(du) = e−a·type(S)−b·type(R) Y
i,j
duij.
Now, the variable unm deﬁned by (8.2) has the interpretation as a last passage time in the percola-
tion model on the lattice with weights given by the yij. Choosing these weights at random so that
they are independent and exponentially distributed with respective parameters ai + bj corresponds
to choosing the input matrix (yij) according to the probability measure
˜νa,b(dy) =
Y
ij
(ai + bj)νa,b(dy).
42


## Page 43


From the above, under this probability measure, the law of the random variable unm is the same,
assuming n ≥m, as the ﬁrst marginal of the probability measure on C(m) deﬁned by
µa,b(dx) =
Y
ij
(ai + bj)Ja(x)Jb(x)
m
Y
i=1
dxi.
In other words, for bounded continuous f,
Z
Rn×m
+
f(umn)˜νa,b(dy) =
Z
C(m) f(x1)µa,b(dx).
The probability measures µa,b are non-central Laguerre (or complex Wishart) ensembles and the
integrals (8.7) are the corresponding Selberg-type integrals [27, 4, 17, 11, 16].
Similarly, in the symmetric case, one arrives at the interpolating ensembles of Baik and Rains [4,
2]. These are probability measures on Rn
+ deﬁned for α ∈Rn
+ and ζ ∈R+ by
µα;ζ(dx) =
Y
i<j
(αi + αj)Jα(x)
n
Y
i=1
(αi + ζ)e(−1)iζxidxi.
We note that, in the notation of Section 5, as ǫ →0,
νǫα;ǫζ ◦σ−1(dex/ǫ) =⇒µα;ζ(dx),
where “ =⇒” denotes weak convergence of probability measures. In this setting (see [4]) if the
input matrix (yij) ∈Rn×n
+
is symmetric and chosen according to the probability measure
Y
i<j
(αi + αj)e−(αi+αj)yijdyij
Y
i
(αi + ζ)e−(αi+ζ)yiidyii
then the last passage time unn is distributed as the ﬁrst marginal of µα;ζ.
References
[1] D. Aldous, P. Diaconis. Longest increasing subsequences: From patience sorting to the Baik-Deift-Johansson
theorem. Bull. Amer. Math. Soc., 36: 413–432 (1999).
[2] J. Baik. Painlev´e expressions for LOE, LSE, and interpolating ensembles. Int. Math. Res. Not. 33 (2002) 1739–
1789.
[3] J. Baik, P.A. Deift, K. Johansson. On the distribution of the length of the longest increasing subsequence of
random permutations. J. Amer. Math. Soc., 12:1119–1178 (1999).
[4] J. Baik and E. Rains. Algebraic aspects of increasing subsequences. Duke Math. J. 109 (2001) 1–65.
[5] J. Baik and E. M. Rains. Symmetrized random permutations. MSRI Publications, 40 (2001) 1–19.
[6] A. Berenstein and D. Kazhdan. Geometric and unipotent crystals. Geom. Funct. Anal., Special Volume, Part I
(2000) 188–236.
[7] A. Berenstein and D. Kazhdan. Lecture notes on geometric crystals and their combinatorial analogues. Combi-
natorial aspect of integrable systems, MSJ Memoirs, 17, Mathematical Society of Japan, Tokyo, 2007.
[8] A. Berenstein and A.N. Kirillov. The Robinson-Schensted-Knuth bijection, quantum matrices and piece-wise
linear combinatorics. Proceedings of 13th International Conference on Formal Power Series and Algebraic Com-
binatorics, Arizona State University, May 20-26, 2001.
[9] A. Borodin and I. Corwin. Macdonald processes. arXiv:1111.4408.
[10] A. Borodin, I. Corwin and D. Remenik. Log-Gamma polymer free energy ﬂuctuations via a Fredholm determinant
identity. arXiv:1206.4573.
43


## Page 44


[11] A. Borodin and S. P´ech´e. Airy kernel with two sets of parameters in directed percolation and random matrix
theory. J. Stat. Phys. 132 (2008) 275–290.
[12] D. Bump. Automorphic forms on GL(3,R). Lecture Notes in Mathematics, 1083. Springer-Verlag, Berlin, 1984.
[13] D. Bump. The Rankin Selberg method: a survey, in Number Theory, Trace Formulas, and Discrete Groups (K.
E. Aubert, E. Bombieri and D. Goldfeld, eds.). Academic Press, New York, 1989.
[14] D. Bump and S. Friedberg. The exterior square automorphic L-functions on GL(n). Festschrift in Honor of
Piatetski-Shapiro, Part II, Weizmann, Jerusalem, 1990, pp. 4765.
[15] I. Corwin, N. O’Connell, T. Sepp¨al¨ainen and N. Zygouras. Tropical combinatorics and Whittaker functions.
arXiv:1110.3489.
[16] E. Dieker and J. Warren. On the largest-eigenvalue process for generalized Wishart random matrices. ALEA 6
(2009) 369–376.
[17] P. Forrester and E. Rains. Interpretations of some parameter depen- dent generalizations of classical matrix
ensembles. Probab. Th. Rel. Fields 131 (2005) 1–61.
[18] W. Fulton. Young Tableaux, volume 35 of London Mathematical Society Student Texts. Cambridge University
Press, 1997.
[19] A. Gerasimov, S. Kharchev, D. Lebedev and S. Oblezin. On a Gauss-Givental representation of quantum Toda
chain wave equation. Int. Math. Res. Not. (2006) 1–23.
[20] A. Gerasimov, D. Lebedev and S. Oblezin. Baxter Operator and Archimedean Hecke Algebra. Commun. Math.
Phys. 284 (2008) 867–896.
[21] A. Givental. Stationary phase integrals, quantum Toda lattices, ﬂag manifolds and the mirror conjecture. Topics
in Singularity Theory, AMS Transl. Ser. 2, vol. 180, AMS, Rhode Island (1997) 103–115.
[22] D. Goldfeld. Automorphic Forms and L-Functions for the Group GL(n, R). Cambridge University Press, 2006.
[23] T. Gueudre,
P. Le Doussal. Directed polymer near a hard wall and KPZ equation in the half-space.
arxiv:1208.5669v2
[24] T. Ishii and E. Stade. New formulas for Whittaker functions on GL(n, R). J. Fun. Anal. 244 (2007) 289–314.
[25] H. Jacquet. Fonctions de Whittaker associ´ees aux groupes de Chevalley. Bulletin de la Soci´et´e Math´ematique de
France 95 (1967) 243–309.
[26] D. Joe and B. Kim. Equivariant mirrors and the Virasoro conjecture for ﬂag manifolds. Int. Math. Res. Notices
15 (2003) 859–882.
[27] K. Johansson. Shape ﬂuctuations and random matrices. Comm. Math. Phys., 209:437–476 (2000).
[28] S. Kharchev and D. Lebedev. Integral representations for the eigenfunctions of quantum open and periodic Toda
chains from the QISM formalism. J. Phys. A 34 (2001) 2247–2258.
[29] A. N. Kirillov. Introduction to tropical combinatorics. Physics and Combinatorics. Proc. Nagoya 2000 2nd
Internat.Workshop (A. N. Kirillov and N. Liskova, eds.), World Scientiﬁc, Singapore, 2001, pp. 82–150.
[30] A.N. Kirillov and A. Berenstein. Groups generated by involutions, Gelfand-Tsetlin patterns, and combinatorics
of Young tableaux. Algebra i Analiz 7 (1995) 92–152.
[31] B. Kostant. Quantisation and representation theory. In: Representation Theory of Lie Groups, Proc. SRC/LMS
Research Symposium, Oxford 1977, LMS Lecture Notes 34, Cambridge University Press, 1977, pp. 287–316.
[32] M. Noumi and Y. Yamada. Tropical Robinson-Schensted-Knuth correspondence and birational Weyl group ac-
tions. Adv. Stud. Pure Math. 40 (2004) 371442.
[33] N. O’Connell. Directed polymers and the quantum Toda lattice. Ann. Probab. 40 (2012) 437–458.
[34] N. O’Connell. Whittaker functions and related stochastic processes. To appear in proceedings of Fall 2010 MSRI
semester Random matrices, interacting particle systems and integrable systems. arXiv:1201.4849
[35] A. Okounkov. Inﬁnite wedge and random partitions Selecta Math.,7:57–81 (2001).
[36] M. Semenov-Tian-Shansky. Quantisation of open Toda lattices. In: Dynamical systems VII: Integrable systems,
nonholonomic dynamical systems. Edited by V. I. Arnol’d and S. P. Novikov. Encyclopaedia of Mathematical
Sciences, 16. Springer-Verlag, 1994.
44


## Page 45


[37] T. Sepp¨al¨ainen. Scaling for a one-dimensional directed polymer with boundary conditions. Ann. Probab. 40
(2012) 19–73.
[38] E. Stade. Archimedean L-factors on GL(n)×GL(n) and generalized Barnes integrals. Israel J. Math. 127 (2002)
201–219.
[39] E. Stade. Mellin transforms of GL(n, R) Whittaker functions. Amer. J. Math. 123 (2001) 121–161.
[40] R. Stanley. Enumerative Combinatorics, volume 2. Cambridge University Press, 2001.
[41] N. Wallach. Real reductive groups II. Academic Press. San Diego CA, 1992.
Mathematics Institute, University of Warwick, Coventry CV4 7AL, UK
E-mail address: n.m.o-connell@warwick.ac.uk
Department of Mathematics, University of Wisconsin-Madison, Madison, WI 53706-1388, USA
E-mail address: seppalai@math.wisc.edu
Department of Statistics, University of Warwick, Coventry CV4 7AL, UK
E-mail address: n.zygouras@warwick.ac.uk
45

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
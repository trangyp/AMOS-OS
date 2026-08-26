---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1407.2955v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1407.2955v2_Injectivity__multiple_zeros__and_multistationarity_in_reaction_networks

> Source: 1407.2955v2_Injectivity__multiple_zeros__and_multistationarity_in_reaction_networks.pdf

> Pages: 19

---


## Page 1


arXiv:1407.2955v2  [math.AG]  28 Dec 2014
Injectivity, multiple zeros, and multistationarity in reaction
networks
Elisenda Feliu
May 4, 2019
Abstract
Polynomial dynamical systems are widely used to model and study real phenomena.
In biochemistry, they are the preferred choice for modelling the concentration of chemical
species in reaction networks with mass-action kinetics. These systems are typically pa-
rameterised by many (unknown) parameters. A goal is to understand how properties of
the dynamical systems depend on the parameters.
Qualitative properties relating to the behaviour of a dynamical system are locally in-
ferred from the system at steady state. Here we focus on steady states that are the positive
solutions to a parameterised system of generalised polynomial equations. In recent years,
methods from computational algebra have been developed to understand these solutions,
but our knowledge is limited: for example, we cannot eﬃciently decide how many positive
solutions the system has as a function of the parameters. Even deciding whether there is
one or more solutions is non-trivial.
We present a new method, based on so-called injectivity, to preclude or assert that
multiple positive solutions exist. The results apply to generalised polynomials and variables
can be restricted to the linear, parameter-independent ﬁrst integrals of the dynamical
system. The method has been tested in a wide range of systems.
1
Introduction
The cell’s ability to respond on-oﬀto gradual changes in a signal is linked to bistability, the
ability of a dynamical system to admit two diﬀerent stable steady states [1, 2]. Speciﬁcally,
bistability underlies the emergence of hysteresis and switch-like behavior.
In the context of molecular biology, models usually depend on unknown parameters and
one is interested in determining whether there exists a choice of parameter values for which
the system has two stable steady states. In particular, the concentration of the species in
a (bio)chemical reaction network is typically modelled with a system of ordinary diﬀerential
equations (ODEs):
dx
dt = fκ(x),
x ∈Rn
≥0,
where κ is a vector of parameters. Bistability arises when the equation fκ(x) = 0 admits
two (positive) solutions that correspond to stable steady states. For unknown parameters,
determining whether a steady state is stable is highly non-trivial. Therefore, the focus has
mainly been on determining whether the equation fκ(x) = 0 admits multiple solutions for
some parameter values κ.
E. Feliu (efeliu@math.ku.dk). Dept. of Mathematical Sciences, University of Copenhagen, Universitetsparken 5,
2100 Denmark
1


## Page 2


Determining the number and stability of steady states has been an important problem in
the context of chemical reaction networks in the 20th century, and there is a rich literature
covering both theoretical and experimental aspects. The majority of the studies date back
to the seventies and eighties (see for example the review [3] and the references therein). In
particular, several foundational theoretical studies on determining the number and stability
of steady states of generic chemical reaction networks were developed in that period. These
studies address diﬀerent broad classes of reaction networks, e.g. detailed or complex balanced
networks or reaction networks with a speciﬁc form. Of these foundational works we highlight
the so-called Chemical Reaction Network Theory (CRNT) of Jackson, Horn, and Feinberg,
e.g. [4–9], the work of Clarke, e.g. [10,11], the work of Vol’pert, e.g. [12,13] and several other
works [14–17].
Since the advent of systems biology in the late nineties, complex and high-dimensional
reaction networks involving biochemical entities have become the object of study.
In this
context the methods developed for chemical reaction networks are often not applicable, due to
the complexity of the networks. For instance, most networks modelling cell signalling events
are neither detailed nor complex balanced. A new generation of methods has been developed,
often within the framework of CRNT, incorporating new formalism and approaches from
computational algebra, e.g. [18–22].
The extensive list of existing methods apply under diﬀerent assumptions and to diﬀerent
modelling strategies. Most methods specialise to the steady states with positive coordinates,
that is, the methods decide whether the function fκ admits multiple positive zeros and exclude
the zeros at the boundary.
Unfortunately, there does not exist a single method that can
satisfactorily handle any given reaction network.
In this paper, we develop a new method to address the existence or preclusion of multiple
steady states. The method builds on so-called injectivity-based methods, which underly several
earlier approaches, for instance [19, 20, 23–27].
For polynomial equations, the setting was
introduced in [23], and subsequently extended in [20,28–31].
The idea underlying injectivity methods is simple: Consider a map f : Rn
>0 →Rn. If f is
injective, then there do not exist distinct x, y in Rn
>0 such that f(x) = f(y). In particular, f
does not have two distinct zeros in Rn
>0.
The converse is false. For instance, consider the map f : R2
>0 →R2 given by
f1(x1, x2) = x1x2 −10x1 + 0.1x2,
f2(x1, x2) = x1x2 + 0.1x1 −10x2.
The only positive zero of f is (9.9, 9.9), but f is not injective on R2
>0 since
f(5.9, 2) = f(7.9, 4) = (−47, −7.61).
Thus, in this case, we cannot conclude that f does not have multiple positive zeros by checking
whether f is injective. However, we can make another simple observation: The positive zeros
of f are also the positive solutions to:
x1 −10x1x−1
2
= −0.1,
x2 −10x−1
1 x2 = −0.1.
(1)
An easy check shows that the map g: R2
>0 →R2 deﬁned by
g(x1, x2) = (x1 −10x1x−1
2 , x2 −10x−1
1 x2)
(2)
2


## Page 3


is injective on R2
>0 and hence we conclude that neither (1) nor f = 0 have multiple positive
solutions. Observe that positivity of the solutions is critical here, because g is obtained by
dividing its two components by x2 and x1, respectively.
This simple example illustrates the approach introduced here: By checking the injectivity of
a new map g constructed from f, we conclude that f does not have more than one positive zero.
We focus on the positive zeros of so-called generalised polynomial maps, that is, polynomials
with real exponents. For example, g in (2) is a generalised polynomial map. More generally,
we consider families of parameterised generalised polynomial maps (cf. (6)) and use the idea
above to preclude or determine the existence of multiple zeros on the positive part of aﬃne
subspaces x∗+ S, where x∗∈Rn
>0 and S ⊆Rn is a vector subspace.
The method is designed to address multistationarity in reaction networks (see Section 3).
However, the method focuses generally on the positive zeros of generalised polynomial maps.
Therefore, we start by presenting the method in a mathematical framework in Section 2. In
particular we explain how injectivity can be used both to preclude and to assert the existence
of multiple positive zeros. We proceed to exemplify how the method can be used to address
multistationarity for a wide range of reaction networks in Section 3. The steps of the method
are summarised in subsection 22.4.
Given a positive integer n, we let [n] := {1, . . . , n}.
2
Mathematical framework
2.1
Injectivity and multiple zeros
S-injectivity.
Given a vector subspace S ⊆Rn, we ﬁrst deﬁne the notion of injectivity on
the positive part of the aﬃne subspaces x∗+ S with x∗∈Rn
>0, cf. [30].
Deﬁnition 2.1. Let f : Rn
>0 →Rm be a map and S ⊆Rn a vector subspace. We say that
• f is S-injective if for all distinct x, y ∈Rn
>0 such that x −y ∈S we have f(x) ̸= f(y).
• f has multiple S-zeros if there exist distinct x, y ∈Rn
>0 such that x −y ∈S and
f(x) = f(y) = 0.
Equivalently, f does not have multiple S-zeros if f does not have two distinct zeros in
some set (x∗+ S) ∩Rn
>0 with x∗∈Rn
>0. Clearly, if f is S-injective, then f does not have
multiple S-zeros.
Deﬁnition 2.2. Let S ⊆Rn be a vector subspace and F ⊆{f : Rn
>0 →Rm} be a set of
functions. We say that
• F is S-injective, if f is S-injective for all f ∈F.
• F has multiple S-zeros, if there exists f ∈F such that f has multiple S-zeros.
Generalised polynomial maps.
We consider families of generalised polynomial maps
given by two real matrices: A = (aij) ∈Rm×r (coeﬃcient matrix) and V = (vij) ∈Rn×r
(exponent matrix). We denote the j-th column of V by vj and deﬁne, for x ∈Rn
>0, the vector
xV ∈Rr
>0 as
 xV 
j = xvj = xv1j
1
· . . . · xvnj
n ,
j ∈[r].
3


## Page 4


The vector xV is a vector of generalised monomials, whose exponents are given by the columns
of V . For a positive vector κ ∈Rr
>0, we deﬁne the map fκ : Rn
>0 →Rm as
fκ(x) = A
 κ ◦xV 
,
(3)
where ◦denotes the product componentwise (or Hadamard product). The coeﬃcient κj of
each monomial will be treated as a parameter. Since
fκ(x) = fκ(y)
if and only if
A
 κ ◦
 xV −yV 
= 0,
then S-injectivity of fκ is unchanged if the matrix A is replaced by a matrix eA with the same
kernel as eA.
For example, the map
fκ(x) =
κ1x1x2 −κ2x2x3 + κ3x1x4
κ2x2x3 −κ3x1x4 −κ4x2x4

,
(4)
takes the form (3) with
A =

1
−1
1
0
0
1
−1
−1

,
V =



1
0
1
0
1
1
0
1
0
1
0
0
0
0
1
1


,
(5)
such that κ ◦xV = (κ1x1x2, κ2x2x3, κ3x1x4, κ4x2x4)t.
Any generalised polynomial map can be written in the form (3), possibly for more than one
choice of A, V , and κ. For instance, a generalised polynomial map f : Rn
>0 →Rm involving
monomials xv1, . . . , xvr can be written componentwise as
fi(x) =
r
X
j=1
aijxvj,
aij ∈R,
i ∈[n].
Hence, f is of the form (3) with κ = (1, . . . , 1)t, A = (aij) and V having columns v1, . . . , vr.
We let
FA,V :=

fκ: Rn
>0 →Rm | fκ(x) = A
 κ ◦xV 
, κ ∈Rr
>0
	
(6)
be the family of all generalised polynomial maps (3) obtained by varying the vector of param-
eters κ. Here, we address the question of determining whether FA,V has multiple S-zeros. If
the family FA,V is S-injective, then FA,V does not have multiple S-zeros, but the converse is
not true.
In [30], a characterisation of the families of generalised polynomial maps FA,V that are
S-injective is given in terms of sign vectors and symbolic determinants. Namely, the family
is S-injective if and only if some particular sets of signs do not intersect.
These sets are
constructed from the orthants of Rn and Rr that certain subspaces, deﬁned from A, V, S,
intersect.
When dim(S) ≥rank(A), S-injectivity of FA,V can also be decided based on the signs of
the coeﬃcients of the determinant of a symbolic matrix. The latter scenario is applicable when
studying steady states of chemical reaction networks. Due to its simplicity and applicability,
we describe only the determinant-based criterion for injectivity here. The reader is referred
to [30] for the sign criterion.
4


## Page 5


Determinant criterion for injectivity
Let S ⊆Rn be a vector subspace of dimension s
and A ∈Rm×r such that s ≥rank(A). Let Z ∈R(n−s)×n be any matrix whose rows are a
basis of S⊥and choose eA ∈Rs×r such that ker(A) = ker
  eA

. For example, we can choose a
set of s rows of A with the same rank as A.
For κ ∈Rr
>0 and λ ∈Rn
>0, let Mκ,λ be the square matrix given in block form as
Mκ,λ =

Z
eA diag(κ)V t diag(λ)

,
(7)
where, for a vector w, diag(w) denotes the diagonal matrix with diagonal w. By considering
κ, λ as indeterminates, the determinant of Mκ,λ is a polynomial p(κ, λ) in κ, λ. It is a result
of [20,30], that the family FA,V is S-injective if and only if p(κ, λ) is not identically zero and,
further, all its coeﬃcients have the same sign.
Note than when rank(A) < s, then p(κ, λ) is identically zero and the family FA,V is not
S-injective.
2.2
Gauss reduction and injectivity
In this subsection we present the steps of the method that can be used to conclude that FA,V
does not have multiple S-zeros.
The family GA,V .
Let S ⊆Rn be a vector subspace of dimension s and assume that A
has rank s. We choose as above a matrix eA ∈Rs×r such that ker(A) = ker
  eA

and let B be
the Gauss reduction of eA. Since the kernel of A and B agree, the family FB,V is S-injective
or has multiple S-zeros if and only if this is the case for FA,V . By reordering the columns
if necessary, we can assume that columns 1 to s of eA are linearly independent. Therefore,
without loss of generality, we restrict to families FA,V with
A =
 ids | A1

,
(8)
where ids is the identity matrix of size s and A1 ∈Rs×(r−s). Then fκ ∈FA,V satisﬁes fκ(x) = 0
if and only if



κ1xv1
...
κsxvs


= −A1



κs+1xvs+1
...
κrxvr


,
and this equality holds for x ∈Rn
>0 if and only if



κ1
...
κs


= gbκ(x),
where
gbκ(x) = −



x−v1
...
x−vs


◦A1



κs+1xvs+1
...
κrxvr


,
(9)
with bκ = (κs+1, . . . , κr).
If the map gbκ(x) is S-injective, then fκ does not have multiple
S-zeros. Therefore, by deﬁning
GA,V := {gbκ : Rn
>0 →Rs | bκ ∈Rr−s
>0 },
we have that FA,V does not have multiple S-zeros if GA,V is S-injective.
5


## Page 6


Example 1.
Consider the family FA,V deﬁned by (5) and let
S = ⟨(1, −1, 0, 0), (0, 0, 1, −1)⟩⊆R4.
(10)
Both the dimension of S and the rank of A are 2. Hence we take eA = A and replace A by its
Gauss reduction:
A =
 1
0
0
−1
0
1
−1
−1

.
(11)
The determinant criterion tells us that the family FA,V is not S-injective. The map gbκ in (9)
is
gκ3,κ4(x) = −
x−1
1 x−1
2
x−1
2 x−1
3

◦

0
−1
−1
−1
 κ3x1x4
κ4x2x4

=

κ4x−1
1 x4
κ3x1x−1
2 x−1
3 x4 + κ4x−1
3 x4

=
1
0
0
0
1
1
 

κ4x−1
1 x4
κ3x1x−1
2 x−1
3 x4
κ4x−1
3 x4

.
(12)
The family GA,V is not of the form (6), since two diﬀerent monomials have the same parameter
as coeﬃcient. However, observe that
GA,V =

fη ∈FA′,V ′ | η ∈R3
>0, η1 = η3
	
⊆FA′,V ′
with
A′ =

1
0
0
0
1
1

,
V ′ =



−1
1
0
0
−1
0
0
−1
−1
1
1
1


.
(13)
We use the determinant criterion to decide whether the family FA′,V ′ is S-injective.
For
suitable Z, the matrix Mκ,λ is
Mκ,λ =



1
1
0
0
0
0
1
1
−κ1λ1
0
0
κ1λ4
κ2λ1
−κ2λ2
−(κ2 + κ3)λ3
(κ2 + κ3)λ4


.
The determinant of this matrix is
det(Mκ,λ) = −κ1(κ2λ1λ3 + 2 κ2λ1λ4 + κ2λ2λ4 + κ3λ1λ3 + κ3λ1λ4).
Since all coeﬃcients have the same sign, the family FA′,V ′ is S-injective. Hence, so is the
family GA,V and it follows that FA,V does not have multiple S-zeros.
The family FA′,V ′.
Although the family GA,V might not be of the type (6), one can always
ﬁnd a family FA′,V ′, with A′ ∈Rs×r′, V ′ ∈Rn×r′, and such that
GA,V ⊆FA′,V ′.
Indeed, one ﬁrst identiﬁes the diﬀerent generalised monomials in bκ, and x of gbκ(x).
The
exponents of the monomials in x deﬁne V ′. The matrix A′ is the matrix of coeﬃcients. When
doing so, some parameter κj might be multiplying two diﬀerent generalised monomials in x,
say xw1 and xw2, as it is the case in the example. This occurs whenever a column j of A1
6


## Page 7


contains two nonzero entries at rows i1, i2 such that vi1 ̸= vi2. Then the monomial κs+jxvs+j
appears as a summand in two diﬀerent rows of the product
A1
 κ ◦
 xvs+1, . . . , xvrt,
and these rows are multiplied by diﬀerent monomials x−vi1, x−vi2 when constructing gbκ. In
general, there exists a partition [r′] = I1 ∪· · · ∪Iq and matrices A′ ∈Rs×r′ and V ′ ∈Rn×r′
such that
GA,V =

fη ∈FA′,V ′ | η ∈Rr′
>0, ηi = ηj if i, j ∈Ik, for some k ∈[q]
	
.
(14)
In the example above, r′ = 3 and we let I1 = {2}, I2 = {1, 3}.
Summary of the steps.
Given a family of generalised polynomial maps FA,V such that
A is Gauss reduced and of the form (8), then we construct the families GA,V and FA′,V ′. Since
the matrix A′ has s rows, we apply the determinant criterion to determine whether FA′,V ′ is
S-injective. If this is the case, then we conclude that FA,V does not have multiple S-zeros.
Observe that when constructing GA,V , the parameters κ1, . . . , κs are selected and “elim-
inated”. We could have selected any other set of s parameters κi1, . . . , κis, as long as the
columns i1, . . . , is of A are linearly independent. In this case, the parameters κi1, . . . , κis are
eliminated if we ﬁrst permute the columns of A and V , and the entries of κ simultaneously such
that the indices i1, . . . , is are the ﬁrst indices. We then apply Gauss reduction and proceed as
above with the new data.
Therefore, if FA′,V ′ is not S-injective, then we repeat the described process after simulta-
neously permuting the columns of A and V , and the entries of κ. We do this for all possible
permutations such that the ﬁrst s columns of A are linearly independent, unless for some
permutation we conclude that FA,V does not have multiple S-zeros and the procedure stops.
The family F b
A,bV .
In preparation for the next section, in particular for the proof of
Proposition 2.1, we embed GA,V into an even larger family F b
A,bV where:
• The matrix bA ∈Rs×s(r−s) is the block diagonal matrix with diagonal blocks given by
minus the rows of A1 = (aij):
bai,(i−1)(r−s)+j = −aij,
for
i ∈[s], j ∈[r −s],
and zero otherwise.
• The ℓ-th column of bV ∈Rn×s(r−s) is
vj+s −vi,
if
ℓ= (i −1)(r −s) + j,
with
i ∈[s], j ∈[r −s].
Given ϕ = fη ∈F b
A,bV with η ∈Rs(r−s)
>0
, then ϕ ∈GA,V if and only if
ηj+(b−1)(r−s) = ηj+(c−1)(r−s)
for all j ∈[r −s] and b, c ∈[s] such that abjacj ̸= 0.
For each j ∈[r −s], let αj ⊆{1, . . . , s} be the support of the j-th column of A1. Then,
GA,V = {fη ∈F b
A,bV | ηj+(b−1)(r−s) = ηj+(c−1)(r−s), if b, c ∈αj}.
(15)
7


## Page 8


Observe that only the sets αj with cardinality at least 2 are relevant. Further, we have
GA,V ⊆FA′,V ′ ⊆F b
A,bV .
For example, consider the matrix V in (5) and A in (11), where s = 2, r = 4, and n = 4.
We have
−A1 =
 0
1
1
1

,
bA =
 0
1
0
0
0
0
1
1

,
and
bV =



0
−1
1
0
−1
0
−1
0
0
0
−1
−1
1
1
1
1


.
A map fη ∈F e
A,eV is of the form
fη(x) = eA
 (η1x−1
2 x4, η2x−1
1 x4, η3x1x−1
2 x−1
3 x4, η4x−1
3 x4)t
= (η2x−1
1 x4, η3x1x−1
2 x−1
3 x4 + η4x−1
3 x4)t.
The supports of the columns of A1 are given by α1 = {2}, α2 = {1, 2}. Then, the description
of GA,V according to (15) is
GA,V = {fη ∈F b
A,bV | η2 = η4},
which agrees with (12).
2.3
Gauss reduction and multiple zeros
There exist families FA,V that do not have multiple S-zeros but for which the families FA′,V ′ are
not S-injective for all possible column permutations of A. Therefore, the steps outlined above
do not guarantee the existence of multiple S-zeros for some member of FA,V . However, under
some extra conditions, the existence of multiple S-zeros can be asserted. These conditions are
described in this section.
Example 2.
Let A be as in (11) and let V be
V =



1
0
1
−1
1
1
0
0
0
1
0
0
0
0
1
1


.
(16)
With this matrix V , the map gbκ(x) in (12) becomes
gκ3,κ4(x) =
1
0
0
0
1
1
 

κ4x−1
1 x4
κ3x1x−1
2 x−1
3 x4
κ4x−1
1 x−1
2 x−1
3 x4

.
(17)
Then, GA,V is included in FA′,V ′ with A′ and V ′ = (v′
ij) given in (13), except for the last
column of V ′ where v′
13 = v′
23 = −1. With S given in (10), the family FA′,V ′ is not S-injective.
Indeed, for a suitable Z, the matrix Mκ,λ is
Mκ,λ =



1
1
0
0
0
0
1
1
κ1λ1
0
0
κ1λ4
(κ2 −κ3)λ1
−(κ2 + κ3)λ2
−(κ2 + κ3)λ3
(κ2 + κ3)λ4


.
8


## Page 9


We have that
det(Mκ,λ) = κ1(κ2λ1λ3 + 2 κ3λ1λ4 −κ2λ2λ4 + κ3λ1λ3 −κ3λ2λ4),
which has both positive and negative coeﬃcients. Therefore, there exist η ∈R3
>0 and distinct
x, y ∈R4
>0 such that x −y ∈S and A′ η ◦xV ′
= A′ η ◦yV ′
. That is,
η1x−1
1 x4 = η1y−1
1 y4
η2x1x−1
2 x−1
3 x4 + η3x−1
1 x−1
2 x−1
3 x4 = η2y1y−1
2 y−1
3 y4 + η3y−1
1 y−1
2 y−1
3 y4.
The ﬁrst equality holds independently of η1.
Hence for κ3 = η2 and κ4 = η3, we have
gκ3,κ4(x) = gκ3,κ4(y). We deﬁne κ1, κ2 > 0 as
κ1
κ2

= gκ3,κ4(x)
(= gκ3,κ4(y)).
Reversing the steps from fκ to gbκ, it follows that
A(κ ◦xV ) = A(κ ◦yV ) = 0,
x −y ∈S,
x ̸= y,
and thus FA,V has multiple S-zeros.
Asserting multiple S-zeros.
Assume that there exist parameters bκ ∈Rr−s
>0 and distinct
x, y ∈Rn
>0 with x −y ∈S such that
gbκ(x) = gbκ(y),
(18)
gbκ(x) ∈Rs
>0.
(19)
Deﬁne κ ∈Rr
>0 by (κ1, . . . , κs) = gbκ(x) and (κs+1, . . . , κr) = bκ. Then we have that A(κ◦xV ) =
A(κ ◦yV ) = 0, and hence the family FA,V has multiple S-zeros.
To check whether there exist bκ, x, y such that (18) and (19) are fulﬁlled, we follow the
following strategy.
Checking (18).
Assume that FA′,V ′ is not S-injective. Then neither is F b
A,bV and there exist
parameters η ∈Rs(r−s)
>0
and distinct x, y ∈Rn
>0 with x −y ∈S such that fη(x) = fη(y), for
fη ∈F b
A,bV . We can manually inspect the form of such a vector η and obtain one such that fη
belongs to GA,V .
A suﬃcient and implementable condition for (18) is given by the next proposition. The
idea is that in order to conclude that (18) holds for some bκ ∈Rr−s
>0 , we need suﬃcient freedom
to modify η to satisfy the relations in (15).
By modify we mean the following. Given ǫ ∈Rs
>0, deﬁne bǫ ∈Rs(r−s)
>0
by
bǫℓ= ǫi,
if
ℓ= j + (i −1)(r −s),
with i ∈[s], j ∈[r −s],
that is, bǫ = (ǫ1, . . . , ǫ1, . . . , ǫs, . . . , ǫs) such that each ǫi is repeated r −s times.
Let bη = bǫ ◦η ∈Rs(r−s)
>0
. If fη ∈F b
A,bV , then ǫfη = fbη ∈F b
A,bV . Therefore, if bη fulﬁls the
conditions in (15), then fbη ∈GA,V , fbη(x) = fbη(y), and (18) is fulﬁlled.
9


## Page 10


Proposition 2.1. Let η ∈Rs(r−s)
>0
. Assume that for each j ∈[r −s] there exists ℓj ∈[s] such
that αj ∩αj′ = {ℓj} = {ℓj′} for all j, j′ such that the cardinality of αj, αj′ is at least two and
such that αj ∩αj′ ̸= ∅.
Then there exists ǫ ∈Rs
>0 such that the vector bǫ ◦η ∈Rs(r−s)
>0
fulﬁls the conditions in (15).
Proof.
Let b ∈[s]. If b ∈S
{j|#αj>1} αj, choose j such that b ∈αj and deﬁne
ǫb =
ηj+(ℓj−1)(r−s)
ηj+(b−1)(r−s)
.
This is well deﬁned because if b ∈αj ∩αj′ then b = ℓj = ℓj′ and ǫb = 1. Deﬁne ǫb = 1
otherwise. Let bη = bǫ ◦η. If b ∈αj and #αj > 1, then
bηj+(b−1)(r−s) =
ηj+(ℓj−1)(r−s)
ηj+(b−1)(r−s)
ηj+(b−1)(r−s) = ηj+(ℓj−1)(r−s)
and hence the conditions in (15) are fulﬁlled.
Therefore, if FA′,V ′ is not S-injective and the assumptions in Proposition 2.1 are fulﬁlled,
then there exists bκ ∈Rr−s
>0 such that (18) holds. The conditions of the statement of Proposi-
tion 2.1 are clearly fulﬁlled if the columns of A1 have disjoint supports.
Checking (19).
If the non-zero entries of A1 are all negative and each row has at least one
negative entry, then condition (19) is fulﬁlled for all bκ. This is the case in the example above.
If this is not the case, then we can resort to the following result, which is adapted from Lemma
4.1 in [23].
Proposition 2.2. Let A′ ∈Rs×r′, V ′ ∈Rn×r′, S ⊆Rn a vector subspace, and Mκ,λ as deﬁned
in (7) for some choice of Z. Let η ∈Rr′
>0 such that
A′η ∈Rs
>0
and
det(Mη,λ) = 0,
for some λ ∈Rn
>0.
Then there exist distinct x, y ∈Rn
>0 and κ ∈Rr′
>0 such that x −y ∈S and
A′(κ ◦xV ′) = A′(κ ◦yV ′) ∈Rs
>0.
Proof.
The matrix A′ diag(η)V ′t diag(λ) has nontrivial kernel in S, since det(Mη,λ) = 0.
That is, there exists γ ∈ker(A′ diag(η)V ′t diag(λ)) ∩S, γ ̸= 0. We deﬁne x, y ∈Rn
>0 and
κ ∈Rr′
>0 by
xi =
(
γi/(eγiλi −1)
if γi ̸= 0
1
otherwise
yi = xieγiλi
κ =
 η ◦V ′t(λ ◦γ)

/
 yV ′ −xV ′
,
where division is componentwise and 0/0 = 1. It is easy to check that y −x = γ ∈S, κ ∈Rr′
>0,
and A′ κ ◦
 yV ′ −xV ′
= 0, cf. [5, Section 7], [29, Th. 5.6]. By replacing γ by ǫγ for ǫ > 0
in the deﬁnitions above, deﬁne analogously xǫ, yǫ. We have
A′ κ ◦xV ′
ǫ

= A′η ◦V ′t(λ ◦ǫγ) ◦xV ′
ǫ
yV ′
ǫ
−xV ′
ǫ

= A′η ◦V ′t(λ ◦ǫγ)
eV ′t(λ◦ǫγ) −1

ǫ→0
−−→A′(η ◦(1, . . . , 1)t) = A′η ∈Rs
>0.
Therefore, for ǫ small enough, we get the desired result.
10


## Page 11


2.4
The method
The procedures described in subsections 22.2 and 22.3 give a new injectivity-based method to
determine whether a set of functions deﬁned by generalised polynomial maps in the positive
orthant admit more than one zero on the positive part of x∗+ S for varying x∗.
Speciﬁcally, given A, V, S, we proceed as follows:
0. Check whether FA,V is S-injective using the determinant criterion with the matrix (7).
If yes the family FA,V does not admit multiple S-zeros and stop. If not, proceed.
1. Compute the Gauss reduction of A and the function gbκ.
2. Identify matrices A′, V ′ such that gbκ ∈FA′,V ′.
3. Check whether the family FA′,V ′ is S-injective. If yes, the family FA,V does not admit
multiple S-zeros and stop. If not, proceed.
4. Check whether the assumptions in Proposition 2.1 are fulﬁlled. If not, go to step 7. If
yes, proceed.
5. If all nonzero entries of A1 in (8) are negative and each row contains a nonzero entry,
then the family FA,V has multiple S-zeros and stop. If not, proceed.
6. Check whether the assumptions in Proposition 2.2 are fulﬁlled. If yes, the family FA,V
has multiple S-zeros and stop. If not, proceed.
7. Permute the columns of A, V and the entries of κ simultaneously such that the ﬁrst s×s
minor of A is nonzero and go back to step 1.
We refer to the step 0. as the standard injectivity method, since it is the approach under-
lying the previous methods. For step 3. we use the determinant criterion if the rank of A and
the dimension of S are appropriate. This is the case in the applications in the next section.
For step 7, we ﬁx an order of the set of subsets of [r] with s elements. At the i-th iteration
of the method, we consider the permutation that sends the i-th subset to the front, such that
the set of the ﬁrst s indices and the set of last r −s indices each remain ordered. We check
whether the ﬁrst s × s minor of A is nonzero. Initial dependencies of the columns of A can be
taken into account beforehand, to reduce the number of checks. For example, if two columns
of A are linearly dependent, as is often the case for reaction networks, then subsets of [r] with
s elements containing the two columns are disregarded.
Except for step 6, which is non-trivial, all the other steps are easily implemented using
any mathematical software that allows for symbolic computations. We have automatised steps
1-5 and 7 in Maple and applied the method to a number of situations in the next section.
Only when these steps were inconclusive, was it checked whether step 6 would give a positive
answer (see Section 3).
The steps of the method are illustrated for one of the small examples in the next section
(cf. (22)).
3
Application to chemical reaction networks
The main application of the method is to determine whether a given chemical reaction network
admits multiple steady states. We follow the formalism of CRNT [32,33].
11


## Page 12


Setting.
A (chemical) reaction network over a set X = {X1, . . . , Xn} is a ﬁnite collection
of reactions
n
X
ℓ=1
µℓiXℓ→
n
X
ℓ=1
βℓiXℓ,
i ∈[r],
where µℓi, βℓi ∈Z≥0 and the two sides of a reaction are diﬀerent. Let A be the n × r matrix
whose (ℓ, i)-th entry is βℓi −µℓi, that is, the net production of Xℓin the i-th reaction.
The elements Xℓcorrespond to chemical species. We denote the concentration of Xℓby
xℓ. The vector of concentrations is x = (x1, . . . , xn) ∈Rn
≥0 and the concentration at time t is
denoted by x(t), although reference to time is often omitted from the notation.
It is custom to model the evolution of the concentrations in time using ODEs. A typical
choice of ODE system is based on so-called mass-action kinetics, which is a special case of
power-law kinetics. In this setting, the j-th reaction is assigned a vector vj ∈Rn, and the
monomial xvj is assumed to be proportional to the rate of the j-th reaction when the system
has concentration x.
Let V be the n × r matrix with columns v1, . . . , vr and let κ ∈Rr
>0 be ﬁxed constants.
Then the system of ODEs is given by
dx
dt = fκ(x),
fκ(x) = A
 κ ◦xV 
.
(20)
This ODE system is deﬁned for x ∈ΩV , where Rn
>0 ⊆ΩV ⊆Rn
≥0 is obtained by removing
from Rn
≥0 the ℓ-th hyperplane orthant whenever the ℓ-th row of V contains a negative entry.
The vector κ is called the vector of reaction rate constants.
In mass-action kinetics, the matrix V = (vij) is deﬁned by vℓi = µℓi. That is, the i-th
column of V consists of the coeﬃcients in the left-hand side of the i-th reaction.
The subspace S = im(A) ⊆Rn is called the stoichiometric subspace. Because the derivative
of x belongs to S, the trajectories of (20) are conﬁned to sets (x∗+S)∩Rn
≥0 with x∗∈Rn
≥0 the
initial condition of the system. These sets are called stoichiometric compatibility classes. We
study therefore the dynamics of (20) conﬁned to the stoichiometric compatibility classes and
determine the steady states within each stoichiometric compatibility class. In this context, if
the family FA,V has multiple S-zeros, then one says that the reaction network is multistationary
or admits multiple steady states.
In the following examples we provide a series of reaction networks and use our method to
determine whether multiple steady states can exist in some stoichiometric compatibility class
for some choice of reaction rate constants κ.
Two-component systems.
Consider the reaction network
X1
κ1
−→X2
X2 + X3
κ2
−−⇀
↽−−
κ3 X1 + X4
X4
κ4
−→X3,
(21)
where, as it is custom, reaction rate constants are written as reaction labels. This network
models a simple bacterial two-component system in which X1, X2 (resp.
X3, X4) are the
unphosphorylated and phosphorylated forms of a histidine kinase (resp. response regulator).
Using mass-action kinetics, the ODE system (20) of network (21) has matrices
A =



−1
1
−1
0
1
−1
1
0
0
−1
1
1
0
1
−1
−1


,
V =



1
0
1
0
0
1
0
0
0
1
0
0
0
0
1
1


,
12


## Page 13


such that
fκ(x) = A(κ1x1, κ2x2x3, κ3x1x4, κ4x4)t.
The family FA,V is S-injective, and hence there is not a choice of constants for which a
stoichiometric compatibility class has multiple steady states.
The matrix A has rank 2, and notice that the second and fourth row are precisely the matrix
A in (5). Further, the vector subspace S in (10) is precisely the stoichiometric subspace of
this network, that is, the image of A. The matrix of exponents V in (5) provides another
kinetics for network (21), which is not mass-action. By the results above, network (21) with
the kinetics given by V is not multistationary.
On the other hand, we have shown that with V given in (16), network (21) admits multiple
steady states in one stoichiometric compatibility class for some choice of reaction rate constants
κ ∈R4
>0. Hence the network is multistationary.
The Langmuir-Hinselwood mechanism.
Our second example is the catalytic oxidation
of CO on a Pt(111) surface, which follows the Langmuir-Hinselwood mechanism, and is known
to admit multiple steady states. The Langmuir-Hinselwood generally describes the adsorption
of one or more reactants on a surface, cf. [3, Eq. (19)].
Using [34, Eq. (1)] and [3, Eq. (19)], the catalytic oxidation of CO is described by the
reactions
CO + S
κ1
−−⇀
↽−−
κ2 COad
O2 + 2S κ3
−→2Oad
COad + Oad
κ4
−→CO2 + 2S,
where S represents the active catalytic site on the surface. The gases CO, O2 and CO2 are
assumed constant. By letting X1 = S, X2 =COad, and X3 =Oad, the reaction scheme is thus
reduced to
X1
κ1
−−⇀
↽−−
κ2 X2
2X1
κ3
−→2X3
X2 + X3
κ4
−→2X1.
(22)
Assuming mass-action kinetics, the ODE system in (20) modelling the evolution of the con-
centrations of X1, X2, X3 in time is
dx1
dt = −κ1x1 + κ2x2 −2κ3x2
1 + 2κ4x2x3,
dx2
dt = κ1x1 −κ2x2 −κ4x2x3,
dx3
dt = κ3x2
1 −κ4x2x3.
The matrices A, V in (20) are
A =
 −1
1
−2
2
1
−1
0
−1
0
0
2
−1
!
,
V =
 1
0
2
0
0
1
0
1
0
0
0
1
!
.
We let S = im(A). The matrix A has rank 2. Since the ﬁrst two rows of A are linearly
independent, we redeﬁne A to be the submatrix of A that consists of the ﬁrst two rows. We
now go through steps 0.-7. of the method. The matrix Mκ,λ in (7) is
Mκ,λ =
 
1
1
1
κ1λ1
−κ2λ2 −κ4λ2
−κ4λ3
4κ3λ1
−κ4λ2
−κ4λ3
!
13


## Page 14


and its determinant is
−κ1κ4λ1λ2 + κ1κ4λ1λ3 + 4κ2κ3λ1λ2 + κ2κ4λ2λ3 + 4κ3κ4λ1λ2 −4κ3κ4λ1λ3.
Since the determinant, seen as a polynomial in κ, λ, has coeﬃcients with opposite signs, the
family FA,V is not S-injective (step 0.). The Gauss reduction of A is the matrix

1
−1
0
−1
0
0
1
−1
2

,
from where we ﬁnd
A1 =

−1
−1
0
−1
2

,
after permuting the second and third columns of the Gauss reduction of A. The map gbκ(x)
in (9) becomes (step 1.):
gbκ(x) =
κ2x−1
1 x2 + κ4x−1
1 x2x3
1
2κ4x−2
1 x2x3

=

1
1
0
0
0
1
2
 

κ2x−1
1 x2
κ4x−1
1 x2x3
κ4x−2
1 x2x3

.
The matrices A′, V ′ are thus (step 2.):
A′ =

1
1
0
0
0
1
2

,
V ′ =
 −1
−1
−2
1
1
1
0
1
1
!
.
We compute the new matrix Mκ,λ from A′, V ′ and S:
Mκ,λ =
 
1
1
1
−κ1λ1 + κ2λ1
−κ1λ2 + κ2λ2
−2κ1λ3 + κ2λ3
0
1
2κ3λ2
1
2κ3λ3
!
and its determinant
1
2κ3(κ1λ2λ3 + κ1λ1λ3 −κ2λ1λ3 −κ1λ1λ2 + κ2λ1λ2).
Since the determinant has coeﬃcients with opposite sign, the family FA′,V ′ is not S-injective
(step 3.). Since the support of each of the columns of bA = A′ contains only one element,
the assumptions in Proposition 2.1 are fulﬁlled (step 4.). The nonzero entries of A1 are all
negative and each row has nonzero entries. By step 5. we conclude that the family FA,V
admits multiple S-zeros and therefore the network admits multiple steady states in some
stoichiometric compatibility class.
Bifunctional kinase.
Consider the following reaction network:
X1
κ1
−→X2
X2 + X3
κ2
−−⇀
↽−−
κ3 X1 + X4
X4 + X5
κ4
−−⇀
↽−−
κ5 X3 + X6
X4
κ8
−→X3
X6 + X7
κ6
−−⇀
↽−−
κ7 X5 + X8
X1 + X4
κ10
−−⇀
↽−−
κ11 X9
κ12
−−→X1 + X3
X8
κ9
−→X7
14


## Page 15


This network models a phosphorelay signalling system with bifunctional kinase [35]. Using
mass-action kinetics, the matrices A, V in (20) are given as
A =














−1
1
−1
0
0
0
0
0
0
−1
1
1
1
−1
1
0
0
0
0
0
0
0
0
0
0
−1
1
1
−1
0
0
1
0
0
0
1
0
1
−1
−1
1
0
0
−1
0
−1
1
0
0
0
0
−1
1
1
−1
0
0
0
0
0
0
0
0
1
−1
−1
1
0
0
0
0
0
0
0
0
0
0
−1
1
0
1
0
0
0
0
0
0
0
0
1
−1
0
−1
0
0
0
0
0
0
0
0
0
0
0
0
1
−1
−1














and
V =












1
0
1
0
0
0
0
0
0
1
0
0
0
1
0
0
0
0
0
0
0
0
0
0
0
1
0
0
1
0
0
0
0
0
0
0
0
0
1
1
0
0
0
1
0
1
0
0
0
0
0
1
0
0
1
0
0
0
0
0
0
0
0
0
1
1
0
0
0
0
0
0
0
0
0
0
0
1
0
0
0
0
0
0
0
0
0
0
0
0
1
0
1
0
0
0
0
0
0
0
0
0
0
0
0
0
1
1












.
The family FA,V is not S-injective. Since the rank of the stoichiometric matrix A is 5, we
redeﬁne A to be the submatrix of A consisting of rows 2, 4, 6, 8, 9. Using steps 1-3, we conclude
that the network does not admit multiple steady states. In other words, Gauss reduction of
this submatrix of A gives two matrices A′, V ′ such that the family FA′,V ′ is S-injective.
Apoptosis.
We next consider a reaction network, which is a basic model of caspase acti-
vation for apoptosis [36]:
X2 + X3
κ1
−→X2 + X4
0 κ7
−→X1
κ6
−→0
X2
k12
−−→0
X1 + X4
κ2
−→X2 + X4
0 κ9
−→X3
κ8
−→0
X4
k13
−−→0
X4 + X5
κ3
−−⇀
↽−−
κ14 X2 + X4
0 κ11
−−→X5
κ10
−−→0
X6
κ4
−→0
X4 + X5
κ5
−→X4.
With mass-action kinetics, this network is known to admit multiple steady states [36]. The
rank of the stoichiometric subspace is maximal, that is, S = R6. For this network, steps 1-5
are inconclusive, for all possible column permutations, that is, we can neither assert nor reject
that multiple steady states exist.
We permute the columns of A, V such that the columns 7, 9, 11, 12, 13, 14 are ﬁrst and
apply Gauss reduction. The matrix A1 in (8) becomes
A1 =







0
−1
0
0
0
−1
0
0
−1
0
0
0
0
0
−1
0
0
0
0
−1
−1
0
0
−1
0
−1
0
0
0
0
0
0
−1
0
0
1
0
0
0
0
0
0
−1
1
0
0
0
0







.
15


## Page 16


Observe that A1 fulﬁls the assumptions in Proposition 2.1. We check step 6. The matrices
A′, V ′ are in this case
A′ =







1
1
0
0
0
0
0
0
0
0
0
0
0
0
1
1
0
0
0
0
0
0
0
0
0
0
0
0
1
1
1
0
0
0
0
0
0
0
0
0
0
0
0
1
0
0
0
0
0
0
0
0
0
0
0
0
1
−1
0
0
0
0
0
0
0
0
0
0
0
0
1
−1







and
V ′ =







1
1
0
0
0
0
0
1
0
0
0
0
0
0
1
0
0
0
0
−1
1
0
0
0
0
0
1
1
0
0
0
0
1
0
0
0
1
0
0
0
0
1
0
1
−1
−1
1
0
0
0
0
0
0
1
1
0
0
0
1
0
0
0
0
0
1
0
0
0
0
1
−1
0







.
The vector η = (1, 3, 1, 1, 1, 1, 1, 1, 16/15, 1, 1, 1/2) fulﬁls A′η ∈R6
>0 and that the determinant
of Mη,λ vanishes for all λ ∈R6
>0. Therefore, by Proposition 2.2 and step 6, we conclude that
this network admits multiple steady states.
Networks of gene regulation.
In [37] a total of 40,680 reaction networks modelling gene
regulatory systems with mass-action kinetics are considered and analysed for multistationarity.
The authors use the CRNT toolbox [7] together with a method termed network ancestry,
justiﬁed by theoretical results in [38].
The authors determine that 2,654 out of the 40,680 networks cannot have multiple steady
states. The standard injectivity method correctly precludes multistationarity for 691 of these
2,654 and is inconclusive for the remaining networks. Using the method presented here we
can conclude that all 2,654 networks are not multistationary.
Interestingly, the authors cannot decide whether multiple steady states occur for 1,050 out
of the 40,680 networks. The method successfully classiﬁes these 1,050 networks and we can
conclude that 47 of them are multistationary, while the remaining 1,003 cannot have multiple
steady states. The remaining 36,976 networks are shown to be multistationary in [37]. The
method is applied to the smallest 2,000 of these, and we reach the same conclusion.
Atoms of multistationarity.
In [38], all possible networks consisting of two reactions
and at most two molecules at each side of a reaction are considered. Here each reaction can
be either irreversible −−→or reversible −−⇀
↽−−. So-called ﬂow reactions 0 −−⇀
↽−−X are added for
each chemical species, such that S = Rn. The authors determine which of these networks are
multistationary when taken with mass-action kinetics.
We considered the 142 networks for which the standard injectivity criterion does not rule
out multistationarity. Among these, the authors show that precisely 35 are multistationary
and hence 107 are not multistationary. The new method does not perform as good as in the
other test cases. Indeed, only 24 networks are identiﬁed as non-multistationary, while the
remaining 118 are left unclassiﬁed.
A plausible explanation for the failure is the following.
With mass-action kinetics, a
reaction of the form 0 →X, called inﬂow, contributes a constant term κi to the i-th component
of fκ in (20). Therefore, we can write fκ(x) = efη(x) + eκ, for some vector eκ ∈Rn
>0. It follows
that fκ(x) = fκ(y) if and only if efη(x) = efη(y) and hence the standard injectivity method
16


## Page 17


checks for injectivity of efη. In fact, efη is gbκ in our method, if the reactions are ordered such
that the inﬂow reactions are ﬁrst.
4
Discussion
Injectivity-based methods are used to preclude multistationarity in reaction networks [19,20,
23–30,39]. The rationale behind the methods is that multiple zeros cannot occur if the map
is injective. In [20,23,28,29,39] the modelling framework is either mass-action or power-law
kinetics, similar to what is used here. A common aspect of these works is that the mathematical
development focuses on the vector subspace S being the image of the coeﬃcient matrix A.
In [19, 26], injectivity of a monomial map is studied in order to assert or preclude multi-
stationarity. In both works, the authors are interested in determining whether a generalised
binomial map, that is, a generalised polynomial map with two terms, admits multiple posi-
tive zeros. The positive zeros of a binomial map can be parameterised by a monomial map
obtained by dividing one term of the binomial by the other term. In this way, there is passage
from the non-existence of multiple positive zeros of the binomial map to the injectivity of the
monomial map, which is identical to the passage from the study of fκ to the study of gbκ here.
The connection between [19,26] and [20,23,28,29] is clariﬁed in [30], where unifying sign
and determinant conditions for the injectivity of generalised polynomial maps are given. An
important novelty of [30] is that S is given independently of the image of A, in contrast to
earlier work. This uncoupling is key in the results presented here.
We have demonstrated by examples that the new method can be applied to a vast amount of
networks for which standard injectivity approaches are inconclusive. We have further applied
the method to the ﬁve basic building blocks in cell signalling in [40] that are shown to admit
multiple steady states. The method correctly classiﬁes the networks as multistationary as
well. However, we are not guaranteed that the method will classify any given network, as we
discussed for the two-reaction networks in [38].
We focus on Gauss reduction of the generalised polynomial maps. Gauss reduction pre-
serves the number of equations, which implies that the determinant criterion can be used to
check step 3, when applying the method to reaction networks. Further, the method can be
applied as a black box. However, the steps presented here also apply if we replace fκ by any
set of generalised polynomial maps with the same positive zeros as fκ. For example, if fκ is
polynomial, one might consider a Gr¨obner basis of the system. In this sense, our work is a
generalisation of [19] to the case where the Gr¨obner basis is not binomial. If the new set of
equations diﬀers from fκ in number of equations, then the sign criterion is to be used at step
3, which can also be computationally checked [30].
Finally, the method has been presented in connection with reaction networks. However,
the mathematical framework is given in full generality and can be used to obtain information
on the number of positive zeros of generalised polynomial maps, independently of the context
in which the question arises. In particular, since any polynomial can be embedded into a family
FA,V , the method can be applied to preclude the existence of multiple positive solutions to
any polynomial equation by letting S = Rn.
Acknowledgments
B. Joshi, A. Shiu, and D. Siegal-Gaskins are thanked for providing raw data and discussions of
their results in [38] and [37]. C. Wiuf is thanked for useful discussions and comments on earlier
17


## Page 18


versions of this manuscript. My co-authors in [30] are thanked for interesting discussions on
injectivity. An anonymous referee is thanked for interesting comments and pointing the author
to relevant literature and examples.
This work has been partially supported by project MTM2012-38122-C03-01/FEDER from
the Ministerio de Econom´ıa y Competitividad, Spain, the Carlsberg Foundation, and the
Lundbeck Foundation.
References
[1] Markevich, N. I., Hoek, J. B. & Kholodenko, B. N., 2004 Signaling switches and bistability arising from
multisite phosphorylation in protein kinase cascades. J. Cell Biol. 164, 353–359.
[2] Thomson, M. & Gunawardena, J., 2009 Unlimited multistability in multisite phosphorylation systems.
Nature 460, 274–277.
[3] Raz´on, L. F. & Schmitz, R. A., 1987 Multiplicities and Instabilities in Chemically Reacting Systems - a
Review. Chem Eng Sci 42, 1005–1047.
[4] Feinberg, M., 1987 Chemical reaction network structure and the stability of complex isothermal reactors
I. The deﬁciency zero and deﬁciency one theorems. Chem. Eng. Sci. 42, 2229–68.
[5] Feinberg, M., 1988 Chemical reaction network structure and the stability of complex isothermal reactors–
II. Multiple steady states for networks of deﬁciency one. Chem. Eng. Sci. 43, 1–25.
[6] Feinberg, M. & Horn, F. J. M., 1977 Chemical mechanism structure and the coincidence of the stoichio-
metric and kinetic subspaces. Arch. Rational. Mech. Anal. 66, 83–97.
[7] Ellison, P., Feinberg, M., Ji, H. & Knight, D., 2012. Chemical reaction network toolbox, version 2.2.
Available online at http://www.crnt.osu.edu/CRNTWin.
[8] Horn, F. J. M., 1972 Necessary and suﬃcient conditions for complex balance in chemical kinetics. Arch.
Rational Mech. Anal. 49, 172–186.
[9] Horn, F. J. M. & Jackson, R., 1972 General mass action kinetics. Arch. Rational Mech. Anal. 47, 81–116.
[10] Clarke, B. L., 1980 Stability of Complex Reaction Networks, volume 43 of Advances in Chemical Physics.
Hoboken, NJ, USA: John Wiley & Sons, Inc.
[11] Clarke, B. L., 1975 Theorems on chemical network stability. The Journal of Chemical Physics 62, 773.
[12] Vol’pert, A. I., 1972 Diﬀerential equations on graphs. Math. USSR-Sb 17, 571582.
[13] Vol’pert, A. I. & Hudjaev, S. I., 1985 Analysis in classes of discontinuous functions and equations of
mathematical physics, volume 8 of Mechanics: Analysis. Martinus NijhoﬀPublishers, Dordrecht.
[14] Gorban, A. N., Bykov, V. I. & Yabloskii, G. S., 1986 Thermodynamic function analogue for reactions
proceeding without interaction of various substances. Chemical Engineering Science 41, 2739–2745.
[15] Fedotov, V. K., Alekseev, B. V., Koltsov, N. I. & Kiperman, S. L., 1984 On the multiplicity criterion for
steady states in catalytic reactions. Reaction Kinetics and Catalysis Letters 26, 25–29.
[16] Ivanova, A., 1979 Conditions for uniqueness of stationary state of kinetic systems related to structural
scheme of reactions. Kinet. Katal. 20, 1019–1023.
[17] Bykov, V. I. & Yablonskii, G. S., 1981 Steady-state multiplicity in heterogeneous catalytic reactions. Int.
Chem. Engng. 21, 142–155.
[18] Bykov, V. I., Kytmanov, A. & Lazman, M., 1998 Elimination Methods in Polynomial Computer Algebra
Mathematics and Its Applications, volume 448. Springer.
[19] P´erez Mill´an, M., Dickenstein, A., Shiu, A. & Conradi, C., 2012 Chemical reaction systems with toric
steady states. Bull. Math. Biol. 74, 1027–1065.
[20] Wiuf, C. & Feliu, E., 2013 Power-law kinetics and determinant criteria for the preclusion of multistation-
arity in networks of interacting species. SIAM J. Appl. Dyn. Syst. 12, 1685–1721.
[21] Gatermann, K., 2001 Counting stable solutions of sparse polynomial systems in chemistry. In Symbolic
Computation: Solving Equations in Algebra, Geometry and Engineering, volume 286 of Contemporary
Mathematics, pp. 53–69.
18


## Page 19


[22] Conradi, C., Flockerzi, D., Raisch, J. & Stelling, J., 2007 Subnetwork analysis reveals dynamic features of
complex (bio)chemical networks. Proc. Nat. Acad. Sci. 104, 19175–80.
[23] Craciun, G. & Feinberg, M., 2005 Multiple equilibria in complex chemical reaction networks. I. The
injectivity property. SIAM J. Appl. Math. 65, 1526–1546.
[24] Banaji, M. & Craciun, G., 2009 Graph-theoretic approaches to injectivity and multiple equilibria in systems
of interacting elements. Commun. Math. Sci. 7, 867–900.
[25] Soul´e, C., 2003 Graphic requirements for multistationarity. ComPlexUs 1, 123–133.
[26] M¨uller, S. & Regensburger, G., 2012 Generalized mass action systems: Complex balancing equilibria and
sign vectors of the stoichiometric and kinetic-order subspaces. SIAM J. Appl. Math. 72, 1926–1947.
[27] Shinar, G. & Feinberg, M., 2012 Concordant chemical reaction networks. Math. Biosci. 240, 92–113.
[28] Craciun, G. & Feinberg, M., 2010 Multiple equilibria in complex chemical reaction networks: semiopen
mass action systems. SIAM J. Appl. Math. 70, 1859–1877.
[29] Feliu, E. & Wiuf, C., 2012 Preclusion of switch behavior in reaction networks with mass-action kinetics.
Appl. Math. Comput. 219, 1449–1467.
[30] M¨uller, S., Feliu, E., Regensburger, G., Conradi, C., Shiu, A. & Dickenstein, A., 2014 Sign conditions
for the injectivity of polynomial maps in chemical kinetics and real algebraic geometry. Foundations of
Computational Mathematics. In press.
[31] Craciun, G., Garcia-Puente, L. & Sottile, F., 2010 Some geometrical aspects of control points for toric
patches. In Mathematical Methods for Curves and Surfaces (eds. M. Dæhlen, M. S. Floater, T. Lyche,
J.-L. Merrien, K. Morken & L. L. Schumaker), volume 5862 of Lecture Notes in Comput. Sci., pp. 111–135.
Heidelberg: Springer.
[32] Feinberg,
M.,
1980.
Lectures
on
chemical
reaction
networks.
Available
online
at
http://www.crnt.osu.edu/LecturesOnReactionNetworks.
[33] Gunawardena, J., 2003.
Chemical reaction network theory for in-silico biologists.
Available online at
http://vcp.med.harvard.edu/papers/crnt.pdf.
[34] Campbell, C. T., Ertl, G., Kuipers, H. & Segner, J., 1980 A molecular beam study of the catalytic oxidation
of CO on a Pt (111) surface. J. Chem. Phys. 73, 5862–5873.
[35] Kothamachu, V. B., Feliu, E., Wiuf, C., Cardelli, L. & Soyer, O. S., 2013 Phosphorelays provide tunable
signal processing capabilities for the cell. Plos Comp. Biol. doi:10.1371/journal.pcbi.1003322.
[36] Eissing, T., Conzelmann, H., Gilles, E. D., Allgower, F., Bullinger, E. & Scheurich, P., 2004 Bistability
analyses of a caspase activation model for receptor-induced apoptosis. J. Biol. Chem. 279, 36892–36897.
[37] Siegal-Gaskins, D., Mejia-Guerra, M., Smith, G. & Grotewold, E., 2010 Emergence of switch-like behavior
in a large family of simple biochemical networks. PLoS Comput. Biol. 7, e1002039.
[38] Joshi, B. & Shiu, A., 2013 Atoms of multistationarity in chemical reaction networks. J. Math. Chem. 51,
153–178.
[39] Joshi, B. & Shiu, A., 2012 Simplifying the Jacobian criterion for precluding multistationarity in chemical
reaction networks. SIAM J. Appl. Math. 72, 857–876.
[40] Feliu, E. & Wiuf, C., 2012 Enzyme-sharing as a cause of multi-stationarity in signalling systems. J. R. S.
Interface 9, 1224–32.
19

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1407_2955v2_injectivity_multiple_zeros_and_multistationarity_in_reaction_networks
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2014/1407_2955V2_INJECTIVITY_MULTIPLE_ZEROS_AND_MULTISTATIONARITY_IN_REACTION_NETWORKS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

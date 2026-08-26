---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1701.02912
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1701.02912_A_property_of_discriminants

> Source: 1701.02912_A_property_of_discriminants.pdf

> Pages: 8

---


## Page 1


arXiv:1701.02912v1  [math.CA]  11 Jan 2017
A property of discriminants
Vladimir Petrov Kostov
Universit´e Cˆote d’Azur, CNRS, LJAD, France
e-mail: kostov@math.unice.fr
Abstract
For the family P := xn + a1xn−1 + · · · + an of complex polynomials in the variable x we
study its discriminant R :=Res(P, P ′, x), R ∈C[a], a = (a1, . . . , an). When R is regarded as
a polynomial in ak, one can consider its discriminant ˜Dk :=Res(R, ∂R/∂ak, ak). We show
that ˜Dk = ck(an)d(n,k)M 2
kT 3
k , where ck ∈Q∗, d(n, k) := min(1, n −k) + max(0, n −k −2),
the polynomials Mk, Tk ∈C[ak] have integer coeﬃcients, ak = (a1, . . . , ak−1, ak+1, . . . , an),
the sets {Mk = 0} and {Tk = 0} are the projections in the space of the variables ak of the
closures of the strata of the variety {R = 0} on which P has respectively two double roots
or a triple root. Set Pk := P −xP ′/(n −k) for 1 ≤k ≤n −1 and Pn := P ′. One has
Tk =Res(Pk, P ′
k, x) for k ̸= n −1 and Tn−1 =Res(Pn−1, P ′
n−1, x)/an.
AMS classiﬁcation: 12E05; 12D05
Key words: polynomial in one variable; discriminant set; resultant; multiple root
1
Introduction
In the present paper we consider the general family of monic degree n complex polynomials in
one variable P := xn +a1xn−1 +· · ·+an. (For a1 = 0 this is the versal deformation of the An−1-
singularity, see [2]). Its discriminant is the resultant R :=Res(P, P ′, x), i.e. the determinant of
the Sylvester matrix S(P, P ′, x). We remind that S(P, P ′, x) is (2n−1)×(2n−1), its ﬁrst (resp.
nth) row equals
(1, a1, . . . , an, 0, . . . , 0)
(resp.
(n, (n −1)a1, . . . , an−1, 0, . . . , 0) ) ,
its second (resp. (n+1)st) row is obtained by shifting the ﬁrst (resp. the nth) one to the right by
one position while adding 0 to the left etc. Set a := (a1, . . . , an), ak := (a1, . . . , ak−1, ak+1, . . . , an)
and Rak := ∂R/∂ak. It is well-known that:
A) R is a quasi-homogeneous polynomial in the coeﬃcients aj, where the quasi-homogeneous
weight of aj equals j. It is a degree n polynomial in each of the variables aj, 1 ≤j ≤n −1, and
a degree n −1 polynomial in an.
B) The set {R = 0} is the set of values of the coeﬃcients aj for which P has a multiple
root. It contains the subsets Σ and ˜
M (the Maxwell stratum) such that for a ∈Σ (resp. a ∈˜
M)
the polynomial P has a root of multiplicity 3 (resp.
has two diﬀerent double roots).
The
semi-algebraic sets Σ and ˜
M are irreducible. Indeed, the closure of Σ is the image of the map
Cn−2 →Cn−2, (z1, z4, z5, . . . , zn) 7→a, where in the computation of (−1)jaj as jth elementary
symmetric function of z1, . . ., zn one sets z2 = z3 = z1; the closure of ˜
M is the image of the map
Cn−2 →Cn−2, (z1, z3, z5, z6 . . . , zn) 7→a, where in the computation of a one sets z2 = z1 and
1


## Page 2


z4 = z3. It is easy to see that the intersections of the sets Σ and ˜
M with each of the subspaces
{aj = 0} are proper subsets of Σ and ˜
M.
One can consider R as a polynomial in ak, with coeﬃcients in C[ak]. Thus one is led to
consider the repeated resultants ˜Dk :=Res(R, Rak, ak). The following result is proved in [5] (see
Proposition 7 there):
Lemma 1. Set d(n, k) := min(1, n −k) + max(0, n −k −2).
The polynomial
˜Dk equals
(an)d(n,k) ˜
D0
k, where ˜
D0
k ∈C[a] is not divisible by any of the variables ai, 1 ≤i ≤n.
Example 2. For n = 3 one has P := x3 + ax2 + bx + c, P ′ = 3x2 + 2ax + b and
R := Res(P, P ′, x) = 4a3c −a2b2 −18abc + 4b3 + 27c2 .
Set ˜Da :=Res(R, ∂R/∂a, a) and similarly for ˜Db and ˜Dc. Hence
˜Da = −64c(b3 −27c2)3 ,
˜Db = −64c(a3 −27c)3 and
˜Dc = −432(−3b + a2)3 .
Example 3. For n = 4 one has P := x4 + ax3 + bx2 + cx + d, P ′ = 4x3 + 3ax2 + 2bx + c and
R
:=
Res(P, P ′, x)
=
−27a4d2 + 18a3bcd −4a3c3 + a2b2c2 + 144a2bd2 −4a2b3d
−6a2c2d −80ab2cd + 18abc3 −192acd2 + 16b4d
−4b3c2 −128b2d2 + 144bc2d −27c4 + 256d3 .
One ﬁnds that
˜Da = 6912d2M2
aT 3
a
,
˜Db = −4096dM2
b T 3
b
,
˜Dc = 6912dM2
c T 3
c
and
˜Dd = 4096M2
d T 3
d
,
where the factors Ma, Ta, Mb, . . ., Td are irreducible:
Ma = 16b2d2 −8bc2d + c4 −64d3
,
Ta = 3b4d −b3c2 + 72b2d2 −108bc2d + 27c4 + 432d3
Mb = a2d −c2
,
Tb = 27a4d2 −a3c3 −6a2c2d −768acd2 + 27c4 + 4096d3
Mc = a4 −8a2b + 16b2 −64d
,
Tc = 27a4d −a2b3 −108a2bd + 3b4 + 72b2d + 432d2
Md = a3 −4ab + 8c
,
Td = 27a3c −9a2b2 −108abc + 32b3 + 108c2 .
One can notice that the equation Mb = 0 deﬁnes the Whitney umbrella.
We prove the following theorem:
Theorem 4. For n ≥4 the polynomial ˜Dk is of the form ck(an)d(n,k)M2
kT 3
k , where ck ∈Q∗,
the degree d(n, k) is deﬁned in Lemma 1 and the polynomials Mk, Tk ∈C[ak] are with integer
coeﬃcients and irreducible. The zero sets of these polynomials are the closures of the projections
in the space of the variables ak of the sets ˜
M and Σ.
The proofs of Theorem 4, Lemma 7 and Lemma 8 are to be found in Section 3.
Acknowledgement. The author is grateful to B.Z. Shapiro from the University of Stock-
holm for the formulation of the problem and its subsequent discussions.
2


## Page 3


2
Comments and lemmas
Theorem 4 is formulated for n ≥4 because for n < 4 the set ˜
M does not exist. In Example 2
only the cubes of the factors Tk and the powers of an (i.e. of c) are present.
It is well-known that R = Q
1≤i<j≤n(zi −zj)2.
Denote by ∆the union of hyperplanes
{zi = zj} in the space Cn of the roots of the polynomial P.
In the last presentation of R
as a product it is necessary to have the diﬀerences of roots zi −zj squared because when the
roots change continuously along a loop avoiding the set ∆so that in the end two of them are
exchanged, then such an exchange should not change the value of R.
By analogy, the fact that the power of the factor Tk in the formula for ˜Dk in Theorem 4) is a
multiple of 3 can be explained like this. At a point a = a∗∈Σ (we assume that a∗̸∈¯Σ\Σ) three
roots z1, z2, z3 of P coalesce. For ﬁxed nearby values of ak the polynomial R (when considered
as a polynomial in ak) has two roots ζ1 and ζ2 that coalesce for ak = a∗k (the projection of a∗
in the space of the variables ak). These roots correspond to equalities and inequalities between
the roots of P of the form z1 = z2 ̸= z3 and z1 ̸= z2 = z3 for ak ̸= a∗k, and to z1 = z2 = z3
for ak = a∗k. When the (n −1)-tuple of coeﬃcients ak circumvents the projection Σk of Σ
in the space of the variables ak along a generic loop, the three roots zi of P undergo a cyclic
permutation of order 3 and now the roots ζ1 and ζ2 of R correspond to other equalities and
inequalities between the roots zi, namely, to z3 = z1 ̸= z2 and z3 ̸= z1 = z2. In order ˜Dk to be
invariant w.r.t. such permutations the power of Tk dividing the resultant ˜Dk must be a multiple
of 3.
For the power of Mk being even a similar explanation exists. To this end we remind ﬁrst
some facts about R for n = 4. The formula for R was obtained in Example 3. On Fig. 1 we
show for real values of c and d the sets {R = 0}|a=0,b=−1, {R = 0}|a=b=0 and {R = 0}|a=0,b=1
(from left to right) which are symmetric w.r.t. the d-axis. This ﬁgure can be compared with the
well-known picture of the swallowtail catastrophe, see [7]. Fig. 1 gives a suﬃcient idea about the
set {R = 0}|a=0 because the set {R = 0} is invariant under the quasi-homogeneous dilatations
a 7→ta, b 7→t2b, c 7→t3c, d 7→t4d, t ̸= 0.
At the points U and V the polynomial P has a triple real and a simple real root (U and V
are ordinary 2/3-cusp points for the real curve {R = 0}|a=0,b=−1). One has
Σ ∩{a = 0, b = −1} = {U, V }
,
˜
M ∩{a = 0, b = −1} = {S} .
At the point S (with d-coordinate equal to 1/4) the curve {R = 0}|a=0,b=−1 has transversal
self-intersection and the polynomial P has two double real roots.
At the point T (which is
an isolated double point of the real curve {R = 0}|a=0,b=1, with d-coordinate equal to 1/4) the
polynomial P has a double complex conjugate pair. At the points I, J and K one has c = d = 0.
The real curves {R = 0}|a=0,b=−1 and {R = 0}|a=0,b=1 are smooth at I and K respectively while
{R = 0}|a=b=0 has a 4/3-type singularity at J.
From now on we keep in mind that the set {R = 0} can be deﬁned in both contexts – the
ones of real or of complex variables x, a, b, c and d. In this sense we make use of Fig. 1 as an
illustration of the real case and as a hint for the complex one. Why for n = 4 the powers of the
factors Mk should be even is suggested by the following lemma. For n > 4 the analogs of the
loops ¯γ and Γ of the lemma exist in a neighbourhood of any value of the parameters aj for which
the polynomial P has a quadruple root, but their explicit construction is harder to describe.
Lemma 5. In the complex case there exists a loop ¯γ belonging to the space of variables (b, c)
which can be lifted to a loop Γ ⊂{R = 0}|a=0 circumventing the set Σ ∪˜
M such that any ﬁbre
3


## Page 4


A
B
E
D
U
V
F
C
I
S
G
c
d
d
J
d
c
c
K
T
Figure 1: The sets {R = 0}|a=0,b=−1, {R = 0}|a=b=0 and {R = 0}|a=0,b=1 for n = 4.
of the projection Γ →¯γ consists of two points and the monodromy deﬁned on the ﬁbre after one
turn along ¯γ is nontrivial.
Proof. In what follows an additional index d denotes the projection of a given set in the space
of variables (b, c, d) (a is presumed equal to 0) into the space of variables (b, c). Consider the
point A on Fig. 1. We are going to construct a continuous path γ ⊂{R = 0}|a=0 leading from
A to G, one of the two points of {R = 0}|a=0 which share with A the same b- and c-coordinates
as shown on Fig. 1. As b increases from −1 to 1, the point A becomes the point B for b = 0 and
then C for b = 1. Then we decrease c by keeping the same value of b – this gives the arc CKD.
Then we ﬁx c and decrese b – this gives the arc DEF. Finally we add the arc FG. The thus
constructed path is real. Three remarks will be needed for what follows:
1) The path γ, in its part between the points A and F, can be constructed as symmetric
w.r.t. the plane {c = 0}.
2) The projection Σd of Σ is deﬁned by 32b3 + 108c2 = 0, i.e. 8b3 + 27c2 = 0; the equation of
this semi-cubic parabola is obtained from the equation Td = 0 by setting a = 0, see Example 3.
There exists a unique number b0 ∈(−1, 0) such that for b = b0 the projection γd of γ intersects
Σd at two points (b0, ±c0).
3) In the real case the path γ has to pass through the point S ∈˜
M, but in the complex one
γ can be modiﬁed so that it circumvent S. The points of the modiﬁed path γ which are close
to S do not have all their coordinates real.
Now we construct (in the complex case) a path γ1 ⊂{R = 0}|a=0 leading from G to A and
satisfying the condition γ1
d = γd. At the same time we modify the path γ in order to have this
condition. If the path γ1 is deﬁned such that γ1
d = γd, then for b = b0, γ1 will intersect the set
Σ. Therefore for b close to b0 we modify γ1 and γ so that γ1 avoid the set Σ. (We make two
such modiﬁcations, corresponding to points of γd and γ1
d close to (b0, c0) and to (b0, −c0). The
modiﬁcations can be made symmetrically w.r.t. the plane {c = 0}.)
For the values of b close to b0 the points of γ do not have all their coordinates real. As for γ1,
its points do not have all coordinates real not only for b close to b0, but also for b ∈[b0, 1] (recall
the construction of the arcs ABC and DEF of γ) and for b = 1, c ̸= 0 (recall the construction
of its arc CKD). Indeed, as R is a degree 3 polynomial in d, then in the real case it has either
three real roots (see for instance the vertical line on the left part of Fig. 1 which intersects the
set {R = 0} at three points two of which are A and G) or one real and two complex conjugate
ones; this is, in particular, the case of any vertical line diﬀerent from the d-axis for b = 1, see
4


## Page 5


the right part of Fig. 1. (The d-axis on the right part of the ﬁgure corresponds to one simple
root at 0 and a double one at 1/4. One simple and one double real root is also the situation
observed on the vertical lines passing through the points U and V .)
To obtain the proof of the lemma one sets ¯γ = γd = γ1
d and one deﬁnes the loop Γ as the
concatenation of γ and γ1. For points of γ and γ1 close to the point S one has γd = γ1
d and no
self-intersection of Γ takes place.
Remarks 6. (1) To prove Theorem 4 we need to recall some notation and results from [5].
Suppose that G1 and G2 are polynomials in several variables one of which is denoted by y. By
S(G1, G2, y) we denote the Sylvester matrix of G1 and G2 when considered as polynomials in y.
We set Pk := P −xP ′/(n −k) for 1 ≤k ≤n −1 and Pn := P ′.
(2) It is shown in [5] that for k ̸= n −1 the polynomial Vk :=Res(Pk, P ′
k, x) is irreducible
and that the polynomial Res(Pn−1, P ′
n−1, x) is the product of an and an irreducible polynomial
in an−1. We set Vn−1 :=Res(Pn−1, P ′
n−1, x)/an. It follows from Theorem 12 of [5] that Vk = Tk,
k = 1, . . . , n. Theorem 4 allows to ﬁnd the polynomials Mk and Tk; however the deﬁnition of
Tk as Tk = Vk is an easier way to ﬁnd Tk.
(3) We denote by QHD(U) the quasi-homogeneous degree of a quasi-homogeneous polynomial
U ∈C[a], where the quasi-homogeneous weight of ak is k.
(4) Set Qk := (n −k)Pk = (n −k)P −xP ′, k ≤n −1, Qn := P ′.
When we compare
polynomials Pk, Qk, R or Vk for two consecutive values of n (i.e. for n and n + 1) we write P n
k ,
P n+1
k
, Qn
k, Qn+1
k
, Rn, Rn+1 or V n
k , V n+1
k
. Notice that as Qk = −kxn + Pn
j=1(j −k)ajxn−j, one
has
Qn+1
k
= xQn
k + (n + 1 −k)an+1 and (Qn+1
k
)′ = x(Qn
k)′ + Qn
k .
(1)
In the following lemma and its proof Ωdenotes nonspeciﬁed nonzero rational numbers.
Lemma 7. (1) One has V∗:= V n+1
k
|an+1=0 = Ω(an)2V n
k for 1 ≤k ≤n −2, V∗= Ω(an)3V n
k for
k = n −1 and V∗= Ω(an−1)3V n
k for k = n.
(2) One has Rn+1|an+1=0 = ±a2
nRn.
The following lemma announces the quasi-homogeneous degrees of certain polynomials that
appear in this text:
Lemma 8. For n ≥4 one has the following quasi-homogeneous degrees of polynomials:
(1) QHD(R) =QHD(Vk) = n(n −1), 1 ≤k ≤n −2.
(2) QHD(Vn−1) = n(n −2).
(3) QHD(Vn) = (n −1)(n −2).
(4) QHD(Rak) = n(n −1) −k, 1 ≤k ≤n −2, QHD(Ran−1) = n2 −3n + 1, QHD(Ran) =
n2 −4n + 2.
(5) QHD( ˜Dk) = n(n −1)2 + n2(n −k −1), 1 ≤k ≤n −1, QHD( ˜Dn) = n(n −1)(n −2).
(6) QHD(Mk) = n3 −3n2 + 2n −(n2 −n)(k + 1)/2, 1 ≤k ≤n −2, QHD(Mn−1) =
n(n −2)(n −3)/2, QHD(Mn) = (n −1)(n −2)(n −3)/2.
3
Proofs
Proof of Lemma 7. The equality A = [B]ℓ,r means that the matrix A is obtained from the matrix
B by deleting its ℓth row and rth column. Prove part (1). In the proof of the lemma we use the
polynomials Qk instead of Pk. For 1 ≤k ≤n −2 set Q∗:= Qn+1
k
|an+1=0 = xQn
k. Consider the
(2n + 1, 2n + 1)-Sylvester matrix S∗:= S(Q∗, Q′
∗, x). The only nonzero entry in its last column
5


## Page 6


is Ωan in position (2n + 1, 2n + 1). Hence when ﬁnding its determinant ΩV∗one can develop it
w.r.t. the last column to obtain V∗= ΩanV∗∗, where V∗∗= det S∗∗, S∗∗= [S∗]2n+1,2n+1.
Subtract for j = 1, . . . , n the jth row of S∗∗from its (n + j)th row. This doesn’t change
V∗∗. Hence the terms Ωan disappear in the (n + 1)st, . . ., (2n)th rows of S∗∗, see (1). The
only nonzero entry of the new matrix (denoted by S∗∗∗) in its last column is Ωan in position
(n, 2n). It is easy to see that [S∗∗∗]n,2n = S(Qn
k, (Qn
k)′, x) (this can be deduced from (1)). Hence
V∗∗= det S∗∗∗= ΩanV n
k and V∗= Ω(an)2V n
k .
For k = n −1 the above reasoning diﬀers only in the end – one deﬁnes V n
n−1 not as
det([S∗∗∗]n,2n) (the latter is divisible by an), but as det([S∗∗∗]n,2n)/an. Hence V∗= Ω(an)3V n
n−1.
For k = n consider the (2n + 1) × (2n + 1)-matrix S0 := S(Qn+1
n
, (Qn+1
n
)′, x).
Its last
column contains a single nonzero entry (Ωan+1 in position (n, 2n + 1)). By deﬁnition det S0 =
Ωan+1V n+1
n
. Hence V∗= Ωdet S†, where S† = ([S0]n,2n+1)|an+1=0.
The last column of S† contains a single nonzero entry (Ωan−1 in position (2n, 2n)), so to
ﬁnd det S† one can develop it w.r.t. the last column. This gives V∗= Ωan−1 det S†0, where
S†0 = [S†]2n,2n.
Subtract the jth row of S†0 from its (n −1 + j)th one, j = 1, . . . , n −1; hence the terms
Ωan−1 disappear in the nth, . . ., (2n −2)nd rows (see (1)). This gives the matrix S†∗such that
det S†∗= det S†0.
The only nonzero entry in the last column of S†∗is Ωan−1 in position (2n −1, 2n −1).
Hence det S†∗= Ωan−1 det S††, where S†† = [S†∗]2n−1,2n−1. The only nonzero entry of S†† in
its last column is in position (n −1, 2n −2) and equals Ωan−1. Thus V∗= Ω(an−1)3 det S††0,
where S††0 = [S††]n−1,2n−2. The (2n −3) × (2n −3)-matrix S††0 equals S(Qn
n/x, (Qn
n/x)′, x), i.e.
ΩS((P n)′, (P n)′′, x).
To prove part (2) one notices that for an+1 = 0 one has P n+1 = xP n and the Sylvester
matrix S1 := S(xP n, (xP n)′, x) contains a single nonzero entry in its last column, namely an
in position (2n + 1, 2n + 1). Set S2 := [S1]2n+1,2n+1. Hence Rn+1|an+1=0 = det S1 = an det S2.
For j = 1, . . ., n subtract the jth row of S2 from its (n + j)th one. The newly obtained matrix
(denoted by S3) has a single nonzero entry in its last column. This is an in position (n, 2n). Set
S3 := [S2]n,2n. Hence det S2 = ±an det S3, i.e. Rn+1|an+1=0 = ±a2
n det S3. On the other hand
S3 = S(P n, (P n)′, x) from which part (2) follows.
Proof of Lemma 8. We denote by W any of the polynomials R, Vk, k ≤n −2, or anVn−1 and
we remind that Tk = Vk, see Remarks 6.
Any polynomial W contains a monomial βan−1
n
,
β ̸= 0. Indeed, the only positions in which the matrix S(W, W ′, x) contains the variable an
are (i, n + i), i = 1, . . . , n −1; in these positions the matrix has terms of the form ηan, η ̸=
0. When det(S(W, W ′, x)) is computed, these terms are multiplied by the constant nonzero
terms in positions (n −1 + j, j), j = 1, . . . , n to give the only monomial of the form βan−1
n
in
det(S(W, W ′, x)). Hence QHD(R) =QHD(Vk) =QHD(anVn−1) = n(n −1) which proves parts
(1) and (2). The proof of part (3) is analogous (one considers polynomials W of degree n −1
instead of n and an−1 plays the role of an).
Part (4) follows from parts (1), (2) and (3) – when R is diﬀerentiated w.r.t. ak, its quasi-
homogeneous degree decreases by k.
Prove part (5).
For ai = 0, k ̸= i ̸= n, k < n, one has R = Ω1an
kan−k−1
n
+ Ω2an−1
n
,
Ω1 ̸= 0 ̸= Ω2, see Statement 8 in [5]. Therefore the Sylvester matrix S(R, Rak, ak) has only the
following nonzero entries, in the following positions:
6


## Page 7


Ω1an−k−1
n
at (i, i)
,
Ω2an−1
n
at (i, n + i)
,
i = 1, . . . , n −1
and
nΩ1an−k−1
n
at (n −1 + j, j)
,
j = 1, . . . , n .
Hence its determinant equals Ωa(n−1)2+n(n−k−1)
n
, Ω̸= 0 which proves part (5) for k < n.
If k = n and ai = 0 for i ≤n −2, then R = Ω3an−1
n
+ Ω4an
n−1, Ω3 ̸= 0 ̸= Ω4. Indeed,
the presence of the monomials Ω3an−1
n
and Ω4an
n−1 in R is easy to deduce from the form of
the matrix S(P, P ′, x), and for ai = 0 (i ≤n −2) there exist no other monomials of quasi-
homogeneous weight n(n−1) in Res(P, P ′, x). Hence the Sylvester matrix S(R, Ran, an) (of size
(2n −3) × (2n −3)) has only the following nonzero entries, in the following positions:
Ω3
at (i, i)
,
Ω4an
n−1
at (i, n −1 + i)
,
i = 1, . . . , n −2
and
(n −1)Ω3
at (n −2 + j, j)
,
j = 1, . . . , n −1 .
Hence its determinant equals ˜Ωan(n−2)
n−1
, ˜Ω̸= 0. Part (5) is proved.
Part (6) follows from the previous parts, from Lemma 1 and from Theorem 4. Indeed, for
k ≤n −2 one has
QHD(Mk)
=
(QHD( ˜Dk) −3QHD(Vk) −n(n −k −1))/2
=
(n(n −1)2 + n2(n −k −1) −3n(n −1) −n(n −k −1))/2
=
n3 −3n2 + 2n −(n2 −n)(k + 1)/2 .
For k = n −1 one obtains
QHD(Mn−1)
=
(QHD( ˜Dn−1) −3QHD(Vn−1) −n)/2
=
(n(n −1)2 −3n(n −2) −n)/2
=
n(n −2)(n −3)/2 .
Finally for k = n one gets
QHD(Mn) = (QHD( ˜Dn) −3QHD(Vn))/2 = (n −1)(n −2)(n −3)/2 .
Proof of Theorem 4. At a point of the set {R = 0}, where P has one double nonzero root and
n −2 simple roots, this set is locally the graph of a function analytic in the variables ak, for
any 1 ≤k ≤n; if the double root is at 0, then this property holds for k = n and fails for
1 ≤k ≤n −1; at a point of this set for which P has a root of multiplicity ≥3 the set is
not smooth (see Theorem 4 in [5]). It is not smooth also at points for which P has m ≥2
double roots and n −2m simple ones; at such points the set {R = 0} is locally the transversal
intersection of m smooth hypersurfaces (see part (1) of Remarks 6 in [5]).
Hence a priori the polynomial ˜Dk is of the form (an)skMαk
k T βk
k , where sk ∈N∪0, αk, βk ∈N,
{Mk = 0} (resp. {Tk = 0}) is the projection of the set ˜
M (resp. of Σ) in the space of the variables
ak. The equality sk = d(n, k) follows from Lemma 1.
Further we prove the theorem by induction on n. For n = 4 its proof follows from Example 3.
Suppose that for some a ∈Cn+1 the polynomial P n+1 has a simple root h ∈C. Set x 7→x + h.
The new polynomial P n+1 has a simple root at 0 hence an+1 = 0.
The discriminant Rn+1
depends only on the diﬀerences between the roots of P n+1 hence it remains invariant under
shifts of the variable x. For an+1 = 0 one can apply Lemma 7. The lemma implies that for
k ≤n −1 the discriminant Res(Rn+1, ∂Rn+1/∂ak, ak) is of the form atk
n M2
kT 3
k , tk ∈N, i.e. one
7


## Page 8


has αk = 2 and βk = 3 for k ≤n −1, an ̸= 0 and an−1 ̸= 0. The sets ˜
M and Σ are irreducible
and their intersections with each of the subspaces {aj = 0} are their proper subsets. Therefore
the restriction an ̸= 0 and an−1 ̸= 0 can be lifted and one concludes that αk = 2 and βk = 3 for
k ≤n−1. The number h ∈C is arbitrary and for n > 4 the set of polynomials P n without simple
roots is a variety in the space of variables a of codimension ≥3. Hence the above reasoning is
the proof that for n + 1 the claim of the theorem is true if k ≤n −1.
To perform the induction also for k = n and k = n + 1 we consider the discriminant of the
family of polynomials P n+1
∗
:= a0xn+1 + a1xn + · · · + an+1. For its discriminant (denoted also
by Rn+1) one has Rn+1 = (a0)2n Q
1≤i<j≤n+1(zi −zj)2 (zi being the roots of P n+1
∗
, see [8]).
Consider the polynomial P n+1
r
:= xn+1P n+1
∗
(1/x) (the index r stands for “reverted”). Its roots
equal 1/zi. Hence its discriminant Rn+1
r
equals
(an+1)2n
Y
1≤i<j≤n+1
(1/zi −1/zj)2 = (a0)2n
Y
1≤i<j≤n+1
(zi −zj)2 = Rn+1 .
For P n+1
r
the coeﬃcient a0 plays the same role as an+1 plays for P n+1. Denote by ˜αk, ˜βk the
quantities αk, βk when deﬁned for the polynomial P n+1
r
instead of P n+1. Hence one can make
a shift x 7→x + ˜h, where ˜h is a simple root of P n+1
r
, and in the same way as above conclude
that ˜αk = 2 and ˜βk = 3 for k ≤n −1. This is tantamount to αk = 2 and βk = 3 for k ≥2. As
n ≥4, this means in particular that αn = αn+1 = 2 and βn = βn+1 = 3.
The polynomials ˜Dk and Vk are determinants of Sylvester matrices deﬁned after polynomials
with integer coeﬃcients. Hence ˜Dk and Vk have also integer coeﬃcients. Hence the polynomials
Mk can also be chosen with integer coeﬃcients which implies ck ∈Q∗.
References
[1] A. Albouy and Y. Fu, Some Remarks About Descartes Rule of Signs, Elemente der Math-
ematik 69 (2014), 186194.
[2] V.I. Arnold, S.M. Gusein-Zade and A.N. Varchenko, Singularities of diﬀerentiable maps.
Volume 1. Classiﬁcation of critical points, caustics and wave fronts. Translated from the
Russian by Ian Porteous based on a previous translation by Mark Reynolds. Reprint of the
1985 edition. Modern Birkhuser Classics. Birkhuser/Springer, New York, 2012. xii+382 pp.
[3] J. Forsg˚ard, V.P. Kostov and B.Z. Shapiro, Could Ren´e Descartes have known this?, Ex-
perimental Mathematics vol. 24, issue 4 (2015) 438-448.
[4] V.P. Kostov, Topics on hyperbolic polynomials in one variable. Panoramas et Synth`eses 33
(2011), vi + 141 p. SMF.
[5] V.P. Kostov, Some facts about discriminants, Comptes Rendus Acad. Bulg. Sci. (to appear).
[6] I. M´eguerditchian, G´eom´etrie du Discriminant R´eel et des Polynˆomes Hyperboliques, Th`ese
de Doctorat (soutenue le 24 janvier 1991 `a Rennes).
[7] T. Poston and I. Stewart, Catastrophe theory and its applications. With an appendix by D.
R. Olsen, S. R. Carter and A. Rockwood. Reprint of the 1978 original. Dover Publications,
Inc., Mineola, NY, 1996. xviii+491 pp.
[8] Wikipedia. Discriminant.
8

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1701_02912_a_property_of_discriminants
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1701_02912_A_PROPERTY_OF_DISCRIMINANTS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1809.0916
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1809.09160_Polynomial_functions_on_non-commutative_rings_-_a_link_between_ringsets_and_null

> Source: 1809.09160_Polynomial_functions_on_non-commutative_rings_-_a_link_between_ringsets_and_null.pdf

> Pages: 9

---


## Page 1


arXiv:1809.09160v1  [math.RA]  24 Sep 2018
POLYNOMIAL FUNCTIONS ON SUBSETS OF
NON-COMMUTATIVE RINGS — A LINK BETWEEN
RINGSETS AND NULL-IDEAL SETS
SOPHIE FRISCH
Abstract. Regarding polynomial functions on a subset S of a non-commutative
ring R, that is, functions induced by polynomials in R[x] (whose variable com-
mutes with the coeﬃcients), we show connections between, on one hand, sets S
such that the integer-valued polynomials on S form a ring, and, on the other
hand, sets S such that the set of polynomials in R[x] that are zero on S is an
ideal of R[x].
1. Introduction
In the theory of polynomial mappings on commutative rings, there are two
notable subtopics, namely, polynomial functions on ﬁnite rings, and rings of integer-
valued polynomials.
Here, we are concerned with generalizations of these two
topics to polynomial mappings on non-commutative rings, as proposed by Loper
and Werner [8], and developed further by Werner [11–14], Peruginelli [9,10], and
the present author [3–5], among others.
More particularly, we will investigate
connections between null ideals of polynomials on ﬁnite non-commutative rings
and integer-valued polynomials on non-commutative rings.
When we talk about polynomial functions on a non-commutative ring R, we
mean functions induced by elements of the usual polynomial ring R[x] whose inde-
terminate x commutes with the elements of R. Non-commutative rings R for which
polynomial functions have been studied include rings of quaternions [7,11,14], and
matrix algebras [4,5,12].
To begin, we introduce the two objects we want to relate, null ideals and rings
of integer-valued polynomials, in their original, commutative setting:
When considering polynomial functions on a ﬁnite commutative ring R, the
ﬁrst thing one likes to know is the so called null ideal N(R) of R[x] consisting of
all null-polynomials, that is, polynomials such that the function induced on R by
substitution of the variable is zero. The null ideal is important, because the residue
classes of R[x] mod N(R) correspond to the diﬀerent polynomial mappings on R
2010 Mathematics Subject Classiﬁcation. 13F20, 16D25, 16P10, 16S99.
Key words and phrases. polynomial mappings, polynomial functions, integer-valued poly-
nomials, null polynomials, null ideals, matrix algebras, triangular matrices, ﬁnite rings, non-
commutative rings, ringsets .
S. Frisch is supported by the Austrian Science Fund (FWF): P 27816-N26.
1


## Page 2


POLYNOMIAL FUNCTIONS ON NON-COMMUTATIVE RINGS
2
and hence the index [R[x]: N(R)] indicates the number of diﬀerent polynomial
mappings on R.
Regarding integer-valued polynomials, they are deﬁned, for a domain D with
quotient ﬁeld K, as those polynomials f in K[x] such that the polynomial function
deﬁned by f on K takes every element of D to an element of D [1].
We now generalize polynomial functions to non-commutative rings.
Let R be a (possibly non-commutative) ring and
f =
X
k
ckxk =
X
k
xkck ∈R[x].
Then, f induces two polynomial functions on R, namely, the right polynomial
function fr : R →R and the left polynomial function fl : R →R, where
fr(s) =
X
k
cksk
and
fl(s) =
X
k
skck.
There are other generalizations of polynomial functions to polynomials with co-
eﬃcients in non-commutative rings, using polynomials whose indeterminate does
not commute with the coeﬃcients. We are not concerned with this kind of gener-
alized polynomials here. Our topic are left and right polynomial functions deﬁned,
as above, on a non-commutative ring by polynomials in the usual polynomial ring
R[x] whose indeterminate x commutes with the elements of R.
Regarding these left and right polynomial functions on a non-commutative ring
R, we notice that they do not, in general, admit a substitution homomorphism.
It may happen, for some s in R, and f, g ∈R[x] that
fr(s)gr(s) ̸= (fg)r(s)
and also
fl(s)gl(s) ̸= (fg)l(s).
In order to generalize null-ideals to polynomials on ﬁnite non-commutative rings,
we consider the sets of right and left null-polynomials, respectively, on R. We note
that, in the absence of a substitution homomorphism, neither set is necessarily an
ideal of R[x].
Deﬁnition 1.1. Let R a ring and f ∈R[x]. The polynomial f is called a right
null-polynomial on R in case fr(s) = 0 for all s ∈R, and a left null-polynomial on
R in case fl(s) = 0 for all s ∈R.
We denote the sets of right and left null polynomials on R, respectively, by
Nr(R) = {f ∈R[x] | ∀s ∈S fr(s) = 0}
and
Nl(R) = {f ∈R[x] | ∀s ∈S fl(s) = 0}
It is immediately clear that
Fact 1.2 (Werner [13]). For every ring R,
(1) Nr(R) is a left ideal of R[x],
(2) Nl(R) is a right ideal of R[x].


## Page 3


POLYNOMIAL FUNCTIONS ON NON-COMMUTATIVE RINGS
3
Proof. Indeed, if f, g ∈R[x], f = P
k akxk, g = P
k bkxk, and s ∈R, then
(gf)r(s) =
X
k,l
bkalsk+l =
X
k,l
bkalslsk =
X
k
bk
 X
l
alsl
!
sk =
X
k
bk (fr(s)) sk
(1)
The last expression is zero whenever fr(s) = 0, which makes Nr(R) a left ideal
of R[x]. Similarly, by interchanging left and right, we see that Nl(R) is always a
right ideal of R[x].
□
Whether Nr(R) is also a right ideal of R[x], and thus an ideal, for any ﬁnite ring
R, is an open question, and similarly the question whether Nl(R) is a left ideal
and therefore an ideal. There are no known counterexamples.
Werner has found many suﬃcient conditions on R for Nr(R) to be a right ideal
[13], but none of them are necessary. If we take R as the ring of upper triangular
matrices over a commutative ring T, we can, by judicious choice of T, ﬁnd examples
of rings violating all of Werner’s necessary conditions, which nevertheless satisfy
that Nr(R) is a right ideal and Nl(R) is a left ideal of R[x] [5]. Such examples can
also be found among rings of integer-valued polynomials on quaternions [14].
Now, when we generalize integer-valued polynomials to polynomials with coeﬃ-
cients in a non-commutative ring, the usual setup (as introduced in [4]) is
Deﬁnition 1.3. Let D be a domain with quotient ﬁeld K and A a ﬁnitely gener-
ated, torsion-free D-algebra. Let B = A ⊗D K. To avoid certain pathologies, we
stipulate that A ∩K = D when A and K are canonically embedded in B.
Then, the set of right integer-valued polynomials (with coeﬃcients in B) on A
is
Intr
B(A) = {f ∈B[x] | ∀a ∈A fr(a) ∈A}
and the set of left integer-valued polynomials (with coeﬃcients in B) on A is
Intl
B(A) = {f ∈B[x] | ∀a ∈A fl(a) ∈A}.
We remark that it is not a priori clear that IntrB(A) and IntlB(A) are rings,
because, in the absence of a substitution homomorphism, closure under multiplica-
tion is not a given. Yet, there are no known counterexamples. Whether IntrB(A)
and IntlB(A) are rings for any D-algebra A as in Deﬁnition 1.3 remains an open
question.
In some cases it is possible to describe IntrB(A) and IntlB(A) via their relation to
the commutative ring IntK(A) = IntrB(A) ∩K[x] = IntlB(A) ∩K[x], for instance,
when A = Mn(D) is the ring of n × n matrices over D. Here, IntlMn(K)(Mn(D))
coincides with IntrMn(K)(Mn(D)) (shown to be a ring by Werner [12]), and is
canonically isomorphic to Mn(IntK(Mn(D))) [4]. The algebras for which IntB(A) ≃
IntK(A) ⊗D A thus holds have been characterized by Peruginelli and Werner [10].
For Tn(D) the ring of n × n upper triangular matrices with entries in D,
IntrTn(K)(Tn(D)) is isomorphic to the algebra of matrices whose entries in position
(j, k) are in IntK(Tn−k+1(D)), and IntlTn(K)(Tn(D)) is isomorphic to the algebra


## Page 4


POLYNOMIAL FUNCTIONS ON NON-COMMUTATIVE RINGS
4
of matrices whose entries in position (j, k) are from IntK(Tj(D)) [5]. The commu-
tative rings of integer-valued polynomials on upper (or lower) triangular matrices
(with coeﬃcients in K), IntK(Tn(D)), are of interest in their own right [2].
Again, Werner has given diﬀerent suﬃcient conditions on A for IntrB(A) to be
a ring, but we know that these conditions are not necessary. Taking A as the
ring of upper triangular matrices over a judiciously chosen domain D we can ﬁnd
examples where IntrB(A) and IntlB(A) are rings, but all known suﬃcient conditions
are violated [5]. Also, such examples can be found among rings of integer-valued
polynomials over quaternion algebras [14].
2. A connection between ringsets and null-ideal sets
We do not know whether IntrB(A) is always closed under multiplication; nor
do we know whether Nr(R) is always an ideal of R[x].
As a way out of this
quandary, we widen the scope of our investigation.
Following Werner [14], we
consider integer-valued polynomials on subsets of A.
Here, in addition to integer-valued polynomials on subsets, we will also consider
null-polynomials on subsets, and demonstrate a connection between the two.
In what follows, we will often conﬁne ourselves to right polynomial functions,
with the understanding that everything also holds, mutatis mutandis, for left poly-
nomial functions. In the context of right polynomial functions, f(c) means fr(c).
Deﬁnition 2.1. Let A be a D-algebra and everything as in Deﬁnition 1.3 and
S ⊆A. The set of right integer-valued polynomials on S is
Intr
B(S, A) = {f ∈B[x] | ∀s ∈S fr(s) ∈A}.
S is called a right ringset if IntrB(S, A) is closed under multiplication, and hence
a ring.
Likewise, the set of left integer-valued polynomials on S is
Intl
B(S, A) = {f ∈B[x] | ∀s ∈S fl(s) ∈A}.
S is called a left ringset if IntlB(S, A) is closed under multiplication, and hence a
ring.
It is easy to give examples, both of ringsets and of sets that are not ringsets:
For any D-algebra satisfying that
T
d∈D\{0} dA = (0), which is, for instance, the
case if A is a free D-module and D is a Noetherian or Krull domain, Werner [14]
showed that a singleton {s} ⊆A is a right ringset if and only if s is in the center
of A. To see “only if,” suppose that s does not commute with some t ∈A. Let
d ∈D \ {0} such that ts −st /∈dA, and let f(x) = d−1(x −s). Then, both
f and t are in IntrB({s}, A), but ft is not. Indeed, (ft)(x) = d−1(tx −st) and
(ft)(s) = d−1(ts −st) /∈A.
Note that an arbitrary union of ringsets is always a ringset, by the fact that an
intersection of rings is a ring.


## Page 5


POLYNOMIAL FUNCTIONS ON NON-COMMUTATIVE RINGS
5
Deﬁnition 2.2. Let R be a ring and S a subset of R. We denote by Nr
R(S) the
set of polynomials f ∈R[x] such that for all s ∈S, fr(s) = 0. We abbreviate
Nr
R(R) by Nr(R).
Likewise, we denote by Nl
R(S) the set of polynomials f ∈R[x] such that for all
s ∈S, fl(s) = 0 and abbreviate Nl
R(R) by Nl(R).
Remark 2.3. Note that Nr
R(S) is always a left ideal of R[x]. This is demonstrated,
just like the fact that Nr(R) is a left ideal, by equation 1.
The question is: for which sets S is Nr
R(S) a right ideal?
Likewise, Nl
R(S) is always a right ideal of R[x], and the question is: for which
sets S is Nl
R(S) a left ideal?
Deﬁnition 2.4. We say that S (as a subset of R) is a right null-ideal set if Nr
R(S)
is a right ideal of R[x], and hence an ideal of R[x].
We say that S (as a subset of R) is a left null-ideal set if Nl
R(S) is a left ideal
of R[x], and hence an ideal of R[x].
We will now give a criterion for ringsets in terms of null-ideal sets. For this
purpose, we introduce null-polynomials modulo an ideal. We will later rephrase
everything using null polynomials in the strict sense.
Deﬁnition 2.5. Let R be a ring and S a subset of R and I an ideal of R.
A polynomial f ∈R[x] is called a right null polynomial modulo I on S if
fr(s) ∈I for every s ∈S.
A polynomial f ∈R[x] is called a left null-polynomial modulo I on S if fl(s) ∈I
for every s ∈S.
We denote by Nr
(R mod I)(S) the set of right null-polynomials mod I on S and
by Nl
(R mod I)(S) the set of left null-polynomials mod I on S.
Note that Nr
(R mod I)(S) is always a left ideal of R[x] – again, this can be seen
by equation 1 – and that Nl
(R mod I)(S) is always a right ideal of R[x].
Deﬁnition 2.6. We call a subset S of R a right null-ideal set modulo I if Nr
(R mod I)(S)
is a right ideal, and hence an ideal, of R[x].
We call a subset S of R a left null-ideal set modulo I if Nl
(R mod I)(S) is a left
ideal, and hence an ideal, of R[x].
For basic facts about division with remainder in rings of polynomials over non-
commutative rings, we refer to Hungerford [6]. In particular, recall that a polyno-
mial f has a right factor (x −s) if and only if fr(s) = 0, and that the remainder
of f under polynomial division by (x −s) from the right is fr(s).
In the special case of D = Z and S = A the following has been shown, by a
diﬀerent argument, by Werner [13, Thm. 2.4]


## Page 6


POLYNOMIAL FUNCTIONS ON NON-COMMUTATIVE RINGS
6
Theorem 2.7. Let A be a D-algebra and everything as in Deﬁnition 1.3. Let
S ⊆A.
Then, S is a right ringset if and only if S is a right null-ideal-set modulo dA
for all non-zero d ∈D.
Similarly, S is a left ringset if and only if S is a left null-ideal-set modulo dA
for all non-zero d ∈D.
Proof. We show the statement for right polynomial mappings. We write f(c) for
fr(c) in this context. (The left case is similar.)
Suppose S is a right null-ideal-set modulo dA for all non-zero d ∈D.
Let
F, G ∈IntrB(S, A). To show: (FG) ∈IntrB(S, A).
We write F and G as F = f/d, G = g/c, such that f, g ∈A[x], c, d ∈D \ {0}.
For every s ∈S, f(s) ∈dA, and g(s) ∈cA. Note, in particular, that f is a right
null-polynomial modulo dA on S. Having represented FG as FG = (fg)/(dc), we
need to show, for an arbitrary s ∈S, that (fg)(s) ∈dcA.
By division with remainder in A[x] by (x −s) from the right, we get
g(x) = q(x)(x −s) + g(s)
for some q ∈A[x]. We know that g(s) = ca = ac for some a ∈A. For this a ∈A,
(fg)(x) = f(x)q(x)(x −s) + f(x)ac.
We set h(x) = f(x)a.
f being a right null-polynomial modulo dA on S implies, by the fact that S is a
right null-ideal-set modulo dA, that h = fa is also a right null-polynomial modulo
dA on S, and that, therefore, h(s) ∈dA. Finally, we see that (fg)(s) = h(s)c is
in dcA, as required.
For the reverse implication, suppose that S is not a right null-ideal-set modulo
dA for some ﬁxed d ∈D \ {0}. To show: S is not a right ringset.
Let f, g in A[x] such that f is a right null-polynomial modulo dA on S, but (fg)
is not. Now consider F = d−1f ∈B[x] and G = g ∈A[x]. Both F and G are in
IntrB(S, A), but their product FG = d−1fg is not.
□
We now rephrase the link between ring sets and null ideal sets using null poly-
nomials in the strict sense. Let S ⊆R and I an ideal of R. We denote by S + I
the set of residue classes of elements of S in A/I, that is, S + I := {s + I | s ∈S}.
Let f ∈R[x], and ¯f image of f in (R/I)[x] under canonical projection. Then f
is a right null polynomial modulo I on S if and only if ¯f ∈N(A/I)(S + I). In other
words,
Nr
(R
mod I)(S) = π−1(N(A/I)(S + I)),
where π: R[x] →(R/I)[x] is the canonical projection.
This shows that S is a right null-ideal set modulo I if and only if S + I =
{s + I | s ∈S}, as a subset of R/I, is a right null ideal set (and similarly with
right replaced by left).


## Page 7


POLYNOMIAL FUNCTIONS ON NON-COMMUTATIVE RINGS
7
Theorem 2.8 (Version of Thm 2.7). Let A be a D-algebra and everything as in
Deﬁnition 1.3. Let S ⊆A. Then, S is a right ringset if and only if, for all non-zero
d ∈D, S + dA as a subset of A/dA is a right null-ideal-set.
3. A common framework for ringsets and null-ideal sets
We state most facts of this section only for right polynomial functions, with
the understanding that everything also holds when left is interchanged with right
throughout. From now on, f(c) abbreviates fr(c), the result of substituting c for
x in f to the right of the coeﬃcients.
Among the known suﬃcient conditions on A and R, respectively, for Intr
B(A) to
be a ring, and for Nr(R) to be an ideal of R[x], there are identical properties that
have been shown, independently, to be suﬃcient conditions for both questions.
We will now sketch a common generalization for Intr
B(A) and Nr(R) that allows
a uniﬁed treatment of both objects.
Deﬁnition 3.1. Let R be a ring, T a subring of R, and I an ideal of T. We denote
by polr
R(T, I) the set of polynomials in R[x] that map every element of T to an
element of I, under right substitution.
polr
R(T, I) = {f ∈R[x] | ∀t ∈T fr(t) ∈I}
More generally, let S be a subset of T. Then we deﬁne
polr
R(S, I) = {f ∈R[x] | ∀s ∈S fr(s) ∈I}
Note that the subring T of R is still subtly present in the deﬁnition of polr
R(S, I),
since I is assumed to be an ideal of T.
In the special case where R = T and I = (0), we get polr
R(R, (0)) = Nr(R), the
set of right null-polynomials on R.
When R = T, S ⊆T and I = (0), we get polr
R(S, (0)) = Nr
R(S), the set of right
null-polynomials on a subset S of R.
When A is a D-algebra and B = A⊗D K, as in Deﬁnition 1.3, and we set R = B
and T = I = A, we have polr
B(A, A) = IntrB(A), the set of right integer-valued
polynomials on A.
Likewise, to recover integer-valued polynomials on subsets, we set R = B and
T = I = A, and let S be a subset of A. Then, polr
B(S, A) = IntrB(S, A) is the set
of right integer-valued polynomials on S.
We now give an example of how integer-valued polynomials and null polynomials
can be treated together in a more general setting.
Theorem 3.2. Let C ⊆R[x] and S ⊆T. Then, for polr
R(S, I) to be closed under
right multiplication by elements of C, it is suﬃcient that it is closed under right
multiplication by the images cr(s) with c ∈C and s ∈S.


## Page 8


POLYNOMIAL FUNCTIONS ON NON-COMMUTATIVE RINGS
8
Proof. Assume polr
R(S, I) is closed under right multiplication by elements of the
form c(s) with c ∈C and s ∈S. Let f ∈polr
R(S, I) and c ∈C. For an arbitrary
s ∈S, we have to show that (fc)(s) ∈I.
By division with remainder in R[x] of c by (x −s) from the right, we get
c(x) = q(x)(x −s) + c(s)
for some q ∈R[x]. Now
(fc)(x) = f(x)q(x)(x −s) + f(x)c(s).
Let h(x) = f(x)c(s). Then (fc)(s) = h(s). By assumption, h ∈polr
R(S, I), and,
therefore, (fc)(s) ∈I.
□
Corollary 3.3 (Werner [14, Prop. 6.13]). IntrB(S, A) is a ring if and only if
IntrB(S, A) is closed under right multiplication by elements of A.
Corollary 3.4 (Werner [13, Lemma 2.3]). Nr
R(S) is an ideal if and only if it is
closed under right multiplication by elements of R.
By the above corollaries, the two questions,
(1) whether IntrB(A) is a ring, and
(2) whether Nr
R(R) is an ideal of R[x],
can now be subsumed under a single question
(3) is polr
R(T, I) a right T-module (with the restricion of the multiplication of
R[x] as scalar multiplication)?
We illustrate the principle of treating null-ideals and rings of integer-valued poly-
nomials in one common setting by another one of Werner’s suﬃcient conditions.
Theorem 3.5. Let R be a ring, T a subring of R and I an ideal of T. If T is
generated by units as an algebra over its center, then
(1) polr
R(T, I) is a right T-module.
(2) More generally, for every subset S of T that is closed under conjugation by
units of T, polr
R(S, I) is a right T-module.
Proof. Let f = P
k ckxk ∈polr
R(T, I), and u a unit of T. Then fu ∈polr
R(S, I),
because, for any t ∈S, t can be written as t = u−1τu with τ = utu−1 ∈S, and
then
(fu)(t) =
X
k
ckutk =
X
k
ckuu−1τ ku = f(τ)u,
where f(τ)u ∈I, because f(τ) ∈I and I is an ideal of T.
Therefore, polr
R(S, I) is closed under multiplication from the right by units of T.
Also, polr
R(S, I) is certainly closed under multiplication from the right by elements
in the center of T (thanks to the fact that S is a subset of T), and closed under
addition and subtraction. Since every element of T is a ﬁnite sum of products of


## Page 9


POLYNOMIAL FUNCTIONS ON NON-COMMUTATIVE RINGS
9
central elements and units of T, we may conclude that polr
R(T, I) is closed under
multiplication from the right by elements of T.
□
Corollary 3.6 (Werner [14, Prop. 6.13]). If A is generated by units as an alge-
bra over its center and S ⊆A is closed under conjugation by units of A, then
IntrB(S, A) is a ring, i.e., S is a right ringset.
Corollary 3.7. If R is generated by units as an algebra over its center and S ⊆R
is closed under conjugation by units of R, then Nr
R(S) is an ideal of R[x], i.e., S
is a right null-ideal set.
References
[1] P.-J. Cahen and J.-L. Chabert, Integer-valued polynomials, vol. 48 of Mathematical
Surveys and Monographs, Amer. Math. Soc., 1997.
[2] S. Evrard, Y. Fares, and K. Johnson, Integer valued polynomials on lower triangular
integer matrices, Monatsh. Math. 170 (2013), 147–160.
[3] S. Frisch, Integer-valued polynomials on algebras – a survey, Actes des rencontres du CIRM
(electronic) 2 (2010), 27–32.
[4] S. Frisch, Integer-valued polynomials on algebras, J. Algebra 373 (2013), 414–425, see also
the corrigendum 412(2014) p282.
[5] S. Frisch, Polynomial functions on upper triangular matrix algebras, Monatsh. Math. 184
(2017), 201–215.
[6] T. W. Hungerford, Algebra, vol. 73 of Graduate Texts in Mathematics, Springer-Verlag,
New York-Berlin, 1980. Reprint of the 1974 original.
[7] K. Johnson and M. Pavlovski, Integer-valued polynomials on the Hurwitz ring of integral
quaternions, Comm. Algebra 40 (2012), 4171–4176.
[8] K. A. Loper and N. J. Werner, Generalized rings of integer-valued polynomials, J.
Number Theory 132 (2012), 2481–2490.
[9] G. Peruginelli and N. J. Werner, Non-triviality conditions for integer-valued polyno-
mial rings on algebras, Monatsh. Math. 183 (2017), 177–189.
[10] G. Peruginelli and N. J. Werner, Decomposition of integer-valued polynomial algebras,
J. Pure Appl. Algebra 222 (2018), 2562–2579.
[11] N. J. Werner, Integer-valued polynomials over quaternion rings, J. Algebra 324 (2010),
1754–1769.
[12] N. J. Werner, Integer-valued polynomials over matrix rings, Comm. Algebra 40 (2012),
4717 – 4726.
[13] N. J. Werner, Polynomials that kill each element of a ﬁnite ring, J. Algebra Appl. 13
(2014), 1350111, 12.
[14] N. J. Werner, Integer-valued polynomials on algebras: a survey of recent results and open
questions, in Rings, polynomials, and modules, Springer, Cham, 2017, 353–375.
Institut f¨ur Analysis und Zahlentheorie, Technische Universit¨at Graz, Kopernikus-
gasse 24, 8010 Graz, Austria
E-mail address: frisch@math.tugraz.at

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
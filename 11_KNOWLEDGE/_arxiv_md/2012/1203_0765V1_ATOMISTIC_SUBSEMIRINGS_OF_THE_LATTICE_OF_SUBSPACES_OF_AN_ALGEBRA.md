---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1203.0765v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1203.0765v1_Atomistic_subsemirings_of_the_lattice_of_subspaces_of_an_algebra

> Source: 1203.0765v1_Atomistic_subsemirings_of_the_lattice_of_subspaces_of_an_algebra.pdf

> Pages: 14

---


## Page 1


arXiv:1203.0765v1  [math.RA]  4 Mar 2012
ATOMISTIC SUBSEMIRINGS OF THE LATTICE OF
SUBSPACES OF AN ALGEBRA
DANIEL S. SAGE
Abstract. Let A be an associative algebra with identity over a ﬁeld k. An
atomistic subsemiring R of the lattice of subspaces of A, endowed with the
natural product, is a subsemiring which is a closed atomistic sublattice. When
R has no zero divisors, the set of atoms of R is endowed with a multivalued
product. We introduce an equivalence relation on the set of atoms such that
the quotient set with the induced product is a monoid, called the condensation
monoid. Under suitable hypotheses on R, we show that this monoid is a group
and the class of k1A is the set of atoms of a subalgebra of A called the focal
subalgebra. This construction can be iterated to obtain higher condensation
groups and focal subalgebras. We apply these results to G-algebras for G a
group; in particular, we use them to deﬁne new invariants for ﬁnite-dimensional
irreducible projective representations.
1. Introduction
Let A be an associative algebra with identity over a ﬁeld k, and let S(A) be
the complete lattice of subspaces of A. The algebra multiplication on A induces
a product on S(A) given by EF = span{ef | e ∈E, f ∈F}. The lattice S thus
becomes an additively idempotent semiring, with {0} and k = k1A (which we will
often denote by 0 and 1) as the additive and multiplicative identities.
Let R be a closed sublattice of S(A) which is also a subsemiring, i.e., R contains
0 and k and is closed under arbitrary sums and intersections and ﬁnite products.
(We do not require the maximum element of R to be A.)
A nonzero element
X ∈R is called decomposable (or join-reducible) if there exists U, V ⊊R such that
X = U + V and indecomposable otherwise. It is immediate that the multiplication
in R is determined by the product of indecomposable elements. In other words, the
semiring structure is determined by the structure constants cW
U,V for U, V, W ∈R
indecomposable, where cW
U,V is 1 if W ⊂UV and 0 otherwise.
In this paper, we consider subsemirings R whose product is determined by its
minimal nonzero elements–the atoms of the lattice. This means that the indecom-
posable elements of R are precisely the atoms, so that every nonzero element is a
join of atoms, i.e., R is an atomistic lattice1.
Deﬁnition 1.1. A subsemiring R ⊂S(A) is called an atomistic subsemiring of
S(A) if it is also a closed atomistic sublattice.
Note that k is always an atom in R.
2000 Mathematics Subject Classiﬁcation. Primary: 16Y60, 20N20; Secondary: 16W22.
The author gratefully acknowledges support from NSF grant DMS-0606300 and NSA
grant H98230-09-1-0059.
1In the usual deﬁnition, every nonzero element of an atomistic lattice is a ﬁnite join of atoms.
In this paper, we allow arbitrary joins of atoms.
1


## Page 2


2
DANIEL S. SAGE
Example 1.2. For any A, S(A) and {0, 1} are atomistic subsemirings.
Example 1.3. Let X be any proper subspace with X + k1A = A.
Then R =
{0, 1, X, A} is an atomistic subsemiring if and only if X2 ∈R. All four possible
values for X2 can occur. Indeed, if we let X = k¯t in the three two-dimensional
algebras k[t]/(t2), k[t]/(t2 −1), and k[t]/(t2 −t), we obtain X2 equal to 0, 1, and
X respectively. On the other hand, if X = span(¯t, ¯t2) in A = k[t]/(t3 −1), then
X2 = A. (Note that there are never any atomistic subsemirings of size 3.)
Example 1.4. Let V be a vector space with dim V ≥2, and suppose (char k, dim V ) =
1. Let A = End(V ), and let X = {x ∈End(V ) | tr(x) = 0}. Then R = {0, 1, X, A}
is atomistic with X2 = A. To see this, simply note that every matrix unit lies in
X2: Eii = EijEji and Eij = Eij(Eii −Ejj) where i ̸= j.
Our primary motivation for considering atomistic subsemirings comes from rep-
resentation theory. Let G be a group which acts on A by algebra automorphisms.
This means that A is a k[G]-module such that g ·1A = 1A and g ·(ab) = (g ·a)(g ·b)
for all g ∈G and a, b ∈A. We let SG(A) ⊂S(A) be the set of all k[G]-submodules
of A.
This set, called the subrepresentation semiring of A, is simultaneously a
subsemiring and complete sublattice of S(A); such semirings were introduced and
studied in [9, 10]. If A is a completely reducible representation, i.e., a direct sum of
irreducible representations, then SG(A) is an atomistic subsemiring. For example,
this occurs when G is ﬁnite, A is ﬁnite-dimensional, and k has characteristic zero.
When G = SU(2) (or more generally, G is a quasi-simply reducible group), then
the subrepresentation semirings for the G-algebras End(V ) (with V a representation
of G) have had important applications in materials science and physics [5, 4, 9].
The structure of such semirings is intimately related to the theory of 6j-coeﬃcients
from the quantum theory of angular momentum [9, 10, 11, 6].
Our goal in this paper is to study the set of atoms Q(R) of an atomistic sub-
semiring and to use it to deﬁne new invariants for appropriate R–the condensation
group, the focus, the focal subalgebra, and higher analogues. Our methods are
motivated by the theory of hypergroups.
We now give a brief outline of the contents of the paper. In Section 2, we deﬁne
a multivalued product on the set Q(R) of atoms of an atomistic subsemiring R.
In the next section, we introduce an equivalence relation ζ∗on Q(R). We show
that if R has no zero-divisors, then the quotient set Q(R)/ζ∗is naturally a monoid
(called the condensation monoid) while if R is weakly reproducible, the condensation
monoid is in fact a group. In Section 4, we deﬁne the focus ̟R ⊂Q(R) and focal
subalgebra F(R) ⊂A of R. The main result is Theorem 4.3, which states that if R
is weakly reproducible of ﬁnite length, then [0, F(R)] is an atomistic subsemiring
with the same properties and whose set of atoms is ̟R. This allows us to iterate
our construction to obtain higher order versions of our invariants. In Section 5, we
prove Theorem 4.3 by analyzing complete subsets of Q(R). We apply our results
to G-algebras in the ﬁnal section. In particular, we show how to associate new
invariants to irreducible projective representations.
2. A hyperproduct on the set of atoms
From now on, R will always be an atomistic subsemiring of S(A). Let Q(R)
denote the set of atoms of R. If R = SG(A) for a G-algebra A, we write QG(A)


## Page 3


ATOMISTIC SUBSEMIRINGS
3
instead of Q(SG(A)). We make the notational convention that, unless otherwise
speciﬁed, capital letters towards the end of the alphabet will denote atoms.
There is a natural operation Q(R) × Q(R) →P(Q(R)) given by X ◦Y = {Z ∈
Q(R) | Z ⊂XY }. Our ﬁrst goal is to ﬁnd a natural equivalence relation on Q(R)
(for appropriate R) for which ◦induces a monoid (or group) structure on the set
of equivalence classes.
Before proceeding, we need to recall some deﬁnitions from the theory of hyper-
groups. A set H is called a hypergroupoid if it is endowed with a binary operation
◦: H × H →P∗(H), where P∗(H) is the set of nonempty subsets of H. If this
operation is associative, then H is called a semihypergroup; if H also satisﬁes the
reproductive law H ◦x = H = x ◦H for all x ∈H, then H is called a hypergroup.
(For more details on hypergroups, see the books by Corsini [1] and Vougiouklis [12].)
An element e of the hypergroupoid H is called a scalar identity if e ◦x = {x} =
x◦e for all x ∈H; if a scalar identity exists, it is unique. For later use, we introduce
a weak version of the reproductive law. A hypergroupoid with scalar identity e
satisﬁes the weak reproductive law if for any x ∈H, there exists u, v ∈H such that
e ∈x ◦u ∩v ◦x. Note that a semihypergroup that satisﬁes the weak reproductive
law is a hypergroup. Indeed, given y ∈H, y ∈y ◦e ⊂y ◦(v ◦x) = (y ◦v) ◦x,
so there exists w ∈y ◦v such that y ∈w ◦x. Similarly, there exists w′ such that
y ∈x ◦w′.
In general, Q(R) is not even a hypergroupoid. However, we have the following
result:
Proposition 2.1. Let R be an atomistic subsemiring. Then (Q(R), ◦) is a hyper-
groupoid if and only if R is an entire semiring (i.e., R has no left or right zero
divisors).
Proof. Suppose R is entire. If X, Y ∈Q(R), then the nonzero subspace XY must
contain an atom, so X ◦Y ̸= ∅. Conversely, if E, F are nonzero elements of R such
that EF = 0, then choosing X, Y ∈Q(R) such that X ⊂E and Y ⊂F implies
that XY = 0, i.e., X ◦Y = ∅.
□
In particular, if A has zero divisors, then Q(S(A)) is not a hypergroupoid. We will
only be interested in atomistic subsemirings R for which Q(R) is a hypergroupoid,
so, from now on, we assume that R is entire, unless otherwise speciﬁed. Note that
k is a scalar identity for Q(R).
We begin by considering a motivating example. We need to recall some basic
properties of semisimple, multiplicity-free representations. This class of G-modules
is closed under taking submodules and quotients. Any such representation V is the
direct sum of its irreducible submodules, and this is the only way of decomposing V
as the internal direct sum of irreducible submodules. Moreover, there is a bijection
between the power set of the set of irreducible submodules of V and the set of
subrepresentations of V given by J 7→P
X∈J X. It follows that if {Vi | i ∈I} is a
collection of submodules of V and W = P
i∈I Vi, then for X irreducible, X ⊂W if
and only if X ⊂Vj for some j ∈I.
Proposition 2.2. Let A be a multiplicity-free G-algebra with no proper, nontrivial
left (or right) invariant ideals. Then QG(A) is a hypergroup.
Proof. First, we show that the multiplication on QG(A) is associative. Fix X, Y, Z ∈
QG(A). Since A is multiplicity-free, XY = P
j∈J Uj, where X ◦Y = {Uj | j ∈J}.


## Page 4


4
DANIEL S. SAGE
As discussed above, an irreducible submodule W lies in (XY )Z = P UjZ if and
only if it is contained in UiZ for some i, i.e., W ∈Ui◦Z. We thus see that (X◦Y )◦Z
is the set of irreducible submodules of XY Z. A similar argument shows that the
same holds for X ◦(Y ◦Z).
Next, we show that X ◦Y ̸= ∅for any X, Y ∈QG(A). It suﬃces to show that
XY ̸= 0 for all X, Y . Let Y ⊥= {a ∈A | ay = 0 for all y ∈Y }. The subspace Y ⊥
is clearly a left ideal. Moreover, it is a subrepresentation: given g ∈G, u ∈Y ⊥,
(g · a)u = g · (a(g−1 · u)) = g · 0 = 0. Since Y ⊥̸= A, our hypothesis on invariant
left ideals implies that Y ⊥= 0 and XY ̸= 0 for all X.
Finally, we show that X ◦QG(A) = QG(A) = QG(A) ◦X for any X.
The
subspace AX is a nonzero left ideal which is obviously a subrepresentation, so
AX = A. Writing A as a sum of irreducible submodules A = P
i∈I Ui, we have
A = P UiX. The usual multiplicity-free argument shows that each Uj lies in some
UijX, so Uj ∈Uij ◦X. The other equality uses the condition on invariant right
ideals.
□
Matrix algebras give an important class of examples. If V is a ﬁnite-dimensional
vector space and End(V ) is a G-algebra, then V is naturally a projective represen-
tation of G [8]. It was further shown in [8] that End(V ) for such representations
has no proper, nontrivial invariant left or right ideals if and only if V is irreducible.
Hence, we obtain:
Corollary 2.3. If V is a ﬁnite-dimensional irreducible projective representation of
a group such that End(V ) is multiplicity free, then QG(End(V )) is a hypergroup.
This corollary applies, for example, to every irreducible complex representation
of SU(2).
The importance of Proposition 2.2 stems from the fact that there is a group nat-
urally associated to every hypergroup. More generally, let H be a semihypergroup.
Consider the relation β deﬁned by x β y if and only if there exists z1, . . . , zn ∈H
such that x, y ∈z1 ◦· · · ◦zn. Koskas showed that if β∗is the transitive closure
of β, then the induced multiplication makes H/β∗into a semigroup, and β∗is the
largest equivalence relation on H with this property [7]. If H is a hypergroup, then
Freni proved that β is automatically transitive [2]; thus, H/β is a group.
We are led to the following provisional deﬁnition.
Deﬁnition 2.4. Let A be a G-algebra satisfying the hypotheses of Proposition 2.2.
The group QG(A) = QG(A)/β is called the condensation group of A.
We will generalize this deﬁnition to a much broader class of atomistic subsemir-
ings below. However, before continuing we provide a few examples.
Example 2.5. If k denotes the trivial G-algebra, then QG(k) is the trivial group.
Example 2.6. If V is any irreducible representation of SU(2), then QSU(2)(End(V )) =
1. The proof is a special case of Theorem 6.6 below.
Example 2.7. Let V be the standard representation of S3 over the complex numbers.
The corresponding S3-algebra decomposes as End(V ) = C ⊕σ ⊕V , where σ is the
sign representation. Since σ2 = C, σV = V σ = V , and V 2 = C ⊕σ, we see that
the classes of β are {C, σ} and {V }; hence, the condensation group has order 2.
Example 2.8. If F is a ﬁnite Galois extension of k with abelian Galois group G,
then QG(F) = G.


## Page 5


ATOMISTIC SUBSEMIRINGS
5
We remark that if the relation β is replaced by Freni’s relation γ [3], one gets
an abelian group canonically related to any hypergroup.
However, we will not
attempt to generalize the abelian group QG(A)/γ to other atomistic subsemirings
in this paper.
3. The equivalence relation ζ∗
It is not true in general that the hypergroupoid Q(R) is a hypergroup or even
a semihypergroup.
For example, the binary operation on QA4(End(W)) is not
associative, where W is the three-dimensional irreducible representation of A4.
Moreover, the reproductive law is not satisﬁed. (See Example 6.5 below.) We can
thus no longer use the relation β∗to associate a monoid or group to R. Instead,
we will do so by introducing a new relation ζ. This relation will coincide with β in
the situation of Proposition 2.2.
Deﬁnition 3.1. The relation ζ on Q(R) is deﬁned by X ζ Y if and only if there
exists Z1, . . . , Zn ∈Q(R) such that X, Y ⊂Qn
i=1 Zi. We let ζ∗denote the transitive
closure of ζ.
It is obvious that ζ∗is an equivalence relation. We will let ¯X denote the equiv-
alence class of X ∈Q(R).
Remark 3.2. If Z is an atom contained in the ◦product of Z1, . . . , Zn with any
choice of parentheses, then Z ⊂Qn
i=1 Zi. In fact, the relation β can be deﬁned
for hypergroupoids, and this observation just says that β ⊂ζ. However, the set of
β∗-equivalence classes is not necessarily a monoid.
Deﬁnition 3.3. Let R be an entire, atomistic subsemiring of S(A).
(1) R is called weakly reproducible if the hypergroupoid Q(R) satisﬁes the weak
reproductive law, i.e., for all X ∈Q(R), there exists Y, Z ∈Q(R) such that
k ∈X ◦Y ∩Z ◦X.
(2) R is called reproducible if Q(R) satisﬁes the reproductive law, i.e., for all
X ∈Q(R), Q(R) ◦X = Q(R) = X ◦Q(R).
Remark 3.4. One can deﬁne an atomistic subsemiring R to be weakly reproducible
without the assumption that R is entire. However, R is then entire automatically.
Indeed, if XY = 0 for X, Y ∈Q(R), then weak reproducibility implies the existence
of Z such that k ⊂ZX, so Y = kY ⊂ZXY = 0, a contradiction.
Theorem 3.5. Let R be an entire, atomistic semiring of S(A). Then
(1) The induced multiplication on classes makes Q(R)
def
= Q(R)/ζ∗into a monoid.
(2) If R is weakly reproducible, then Q(R) is a group.
Deﬁnition 3.6. The monoid Q(R) is called the condensation monoid (or group)
of R.
The following lemma shows that this terminology does not conﬂict with our
previous deﬁnition.
Lemma 3.7. If A satisﬁes the hypotheses of Proposition 2.2, then β and ζ coincide
on QG(A).
Proof. A similar argument to that used to demonstrate the associativity of QG(A)
shows that Z1◦· · ·◦Zn is the set of irreducible submodules of Qn
i=1 Zi, so β = ζ.
□


## Page 6


6
DANIEL S. SAGE
Recall that an equivalence relation ∼on a hypergroupoid H is called strongly
regular if, for any x, y such that z ∼y and any w ∈H, then u ∈x ◦w and v ∈y ◦w
(resp. u ∈w ◦x and v ∈w ◦y) implies that u∼v. It is a standard fact that for such
∼, ◦induces a binary operation on H/∼via ¯x ◦¯y = ¯z, where z ∈x ◦y [1]. Indeed,
strong regularity implies that the set {¯z | z ∈x′ ◦y′ for some x′ ∈¯x, y′ ∈¯y} is a
singleton.
Lemma 3.8. The equivalence relation ζ∗is strongly regular.
Proof. First, suppose that X ζ Y , so X, Y ⊂Qn
i=1 Zi for some Zi’s. If U ∈X ◦W
and V ∈Y ◦W, then U ⊂XW and V ⊂Y W. Thus, U, V ⊂(Qn
i=1 Zi)W, i.e.,
U ζ W. If X ζ∗Y , then there exists X0, . . . , Xs ∈Q(R) with X = X0, Y = Xs, and
Xi ζ Xi+1 for all i. Taking Ui ∈Xi ◦W with U = U0 and V = Us, the previous case
shows that Ui ζ Ui+1 for all i, i.e., U ζ∗V . The opposite direction in the deﬁnition
of strong regularity is proved similarly.
□
We now verify that the induced binary operation makes Q(R) into a monoid.
The identity is given by ¯k; indeed, this follows immediately from the fact that
k◦X = X = X◦k. Next, we check that ( ¯X◦¯Y )◦¯Z = ¯X◦( ¯Y ◦¯Z). Choose U ∈X◦Y
and V ∈U◦Z, so that ¯V = ( ¯X◦¯Y )◦¯Z. Since U ⊂XY , V ⊂UZ ⊂XY Z. Similarly,
choosing T ∈Y ◦Z and W ∈X ◦T gives ¯W = ¯X ◦( ¯Y ◦¯Z) and W ⊂XT ⊂XY Z.
By deﬁnition, V ζ W, so Q(R) is associative.
Remark 3.9. If we allow R to be an atomistic hemiring of S(A), i.e., we do not
require that k ∈R, then the same argument shows that Q(R) is a semigroup.
Finally, assume that R is weakly reproducible. Given X ∈Q(R), choose Y, Z
such that k ⊂XY ∩ZX. By deﬁnition of the product on Q(R), we obtain ¯X ◦¯Y =
¯k = ¯Z ◦¯X, so ¯X is left and right invertible. This shows that Q(R) is a group and
ﬁnishes the proof of the theorem.
Remark 3.10. Any monoid can be realized as the condensation monoid of an atom-
istic subsemiring. Indeed, given a monoid M, let kM be the corresponding monoid
algebra over k with basis elements {ex|x ∈M}. Let R = {span{ex | x ∈F} | F ⊂
M}. This is an entire atomistic subsemiring of S(kM) with Q(R) = {kex | x ∈M}.
It is now easy to see that Q(R) = M.
4. The focus and the focal subalgebra
Recall that if H is a hypergroup, the heart ωH of H is the kernel of the canonical
homomorphism φ : H →H/β∗; it is a subhypergroup of H. Returning to the
context of Proposition 2.2, let A be a multiplicity-free G-algebra with no proper,
nonzero left or right invariant ideals. We may then use the heart ω of the hypergroup
QG(A) to deﬁne an invariant subalgebra with the same properties.
Proposition 4.1. Let A be a multiplicity-free G-algebra with no proper, nontrivial
one-sided invariant ideals. Then B = P{X | X ∈ω} is a multiplicity-free G-
subalgebra with no proper one-sided invariant ideals.
Proof. It is trivial that B is a multiplicity-free subrepresentation that contains k.
Moreover, if X, Y ∈ω and Z ⊂XY is irreducible, then φ(Z) = φ(X)φ(Y ) = 1, i.e.,
Z ∈ω. This means that Z and hence XY are subspaces of B. It remains to show
that BX = B = XB for any X ∈ω. Choose Z ∈ω. Since QG(A) is a hypergroup,


## Page 7


ATOMISTIC SUBSEMIRINGS
7
there exists Y irreducible such that Z ∈Y ◦X. Since 1 = φ(Z) = φ(Y )φ(X) =
φ(Y ), we see that Y ∈ω, so Z ⊂BX. The proof that Z ⊂XB is similar.
□
This result allows us to iterate the construction of the condensation group. In-
deed, the hypergroup structure on QG(B) = ω gives rise to the group QG(B) and an
invariant subalgebra B′ ⊂B such that QG(B′) is again a hypergroup. See Section 6
for examples.
Motivated by this situation, we make the following deﬁnitions.
Deﬁnition 4.2. Let R be an entire atomistic subsemiring.
(1) The focus ̟R of R is the kernel of the homomorphism ψR : Q(R) →Q(R).
Equivalently, it is the equivalence class of k.
(2) The subspace F(R) = P{X | X ∈̟R} ∈R is called the focal subalgebra
associated to R.
We can now state one of the main results of the paper.
Theorem 4.3. Let R be an entire atomistic subsemiring of S(A).
(1) The focal subspace F(R) is a unital subalgebra of A.
(2) The sublattice [0, F(R)] ⊂R is an entire atomistic subsemiring of S(F(A))
with ̟R ⊂Q([0, F(R)]).
(3) If R is weakly reproducible and has ﬁnite length, then Q([0, F(R)]) = ̟R.
(4) If R is weakly reproducible (resp. reproducible) of ﬁnite length, then the
same holds for [0, F(R)].
We remark that part (3) is very useful in computations as it is often easier to
calculate F(R) than to compute ̟R directly.
We will only prove the ﬁrst two parts of the theorem now. The proof of the other
parts requires a more detailed study of the relation ζ∗and will be given at the end
of Section 5.
Proof of parts (1) and (2). If X, Y ∈̟R and Z ∈X ◦Y , then 1 = ψ(X)ψ(Y ) =
ψ(Z).
This means that Z ∈̟, so XY ⊂F(R).
Since k ⊂F(R), F(R) is
a subalgebra.
This implies that F(R)2 = F(R), so if E, E′ ∈[0, F(R)], then
E + E′ ⊂F(R) and EE′ ⊂F(R).
Thus, the closed sublattice [0, F(R)] ⊂R
is a subsemiring of R, and it is immediate that it is entire and atomistic. The
atoms of [0, F(R)] are precisely the atoms of R which are contained in F(R), so
̟R ⊂Q([0, F(R)]).
□
Corollary 4.4. If R is weakly reproducible and has ﬁnite length, then Q(R) = 1 if
and only if F(R) is the maximum element of R, i.e., [0, F(R)] = R.
Proof. If Q(R) = 1, then ̟R = Q(R). Thus, F(R) contains every atom in R, hence
is the maximum element of R. Conversely, if F(R) is the maximum of R, then
part (3) of the theorem implies that ̟R = Q(R). This gives Q(R) = 1.
□
Remark 4.5. The forward implication in the corollary holds for any entire atomistic
subsemiring.
The theorem shows that we can iterate the construction of the invariants asso-
ciated to R.
Deﬁnition 4.6. The higher foci, focal subalgebras, and condensation monoids (or
groups) for R are deﬁned recursively as follows:


## Page 8


8
DANIEL S. SAGE
• ̟1
R = ̟R, F 1(R) = F(R), and Q1(R) = Q(R);
• ̟n+1
R
= ̟[0,F n(R)], F n+1(R) = F([0, F n(R)]), and Qn+1(R) = Q([0, F n(R)]).
We observe that if R is weakly reproducible and has ﬁnite length, then Qn(R)
is a group for all n.
5. Complete subsets of Q(R)
In order to prove Theorem 4.3, we need a better understanding of the equivalence
relation ζ∗. In this section, we deﬁne complete subsets of Q(R) and use them to
investigate the ζ∗-equivalence classes. Our analysis of ζ∗follows a similar pattern
to that of β∗carried out by Corsini and Freni [1, 2]. In the end, we will show that
if R is weakly reproducible, then every element of ̟R is ζ-related (and not just
ζ∗-related) to k; this will be the key ingredient in the proof of Theorem 4.3.
Deﬁnition 5.1.
(1) A subset E ⊂Q(R) is called complete if for all X1, . . . , Xn ∈Q(R), if there
exists X ∈E such that X ⊂Qn
i=1 Xi, then for any Y ⊂Qn
i=1 Xi, Y ∈E.
(2) If E is a nonempty subset of Q(R), then the intersection of all complete
subsets containing E is denoted by C(E); it is called the complete closure
of E.
It is obvious that C(E) is the smallest closed subset containing E.
Remark 5.2. This is not the usual notion of a complete subset of a semihyper-
group [1, 7], though it coincides in the context of Proposition 2.2. In this paper,
we only consider completeness in the sense given above.
The basic examples of closed subsets are the ζ∗-equivalence classes.
Proposition 5.3. Any ζ∗-equivalence class is closed.
Proof. Consider the class of Z. Suppose that X ζ∗Z and X, Y ⊂Qn
i=1 Xi. Then
Y ζ X, so Y ζ∗Z.
□
The complete closure may be computed inductively. Indeed, given E ̸= ∅, deﬁne
a sequence of subsets κn(E) ⊂Q(R) recursively as follows: κ1(E) = E and
κn+1(E) = {X ∈Q(R) | ∃Y1, . . . , Ys ∈Q(R) and Y ∈κn(E) such that X, Y ⊂
s
Y
i=1
Yi}.
Set κ(E) = ∪n≥1κn(E).
Proposition 5.4. For any nonempty E ⊂Q(R), C(E) = κ(E).
Proof. Suppose Y ∈κ(E), say Y ∈κn(E), and X, Y ⊂Qs
i=1 Yi.
Then X ∈
κn+1(E) ⊂κ(E), so κ(E) is complete. Since E ⊂κ(E), C(E) ⊂κ(E). Conversely,
suppose that F ⊃E and F is complete. We show inductively that κn(E) ⊂F.
This is obvious for n = 1. Suppose κn(E) ⊂F. If X ∈κn+1(E), then we can ﬁnd
Y1, . . . , Ys ∈Q(R) and Y ∈κn(E) such that X, Y ⊂Qs
i=1 Yi. Completeness of F
now shows that X ∈F as desired.
□
We can now give a new characterization of ζ∗. Deﬁne a relation κ on Q(R) by
X κ Y if and only if X ∈C(Y ), where C(Y ) = C({Y }).
Theorem 5.5. The relations κ and ζ∗coincide.


## Page 9


ATOMISTIC SUBSEMIRINGS
9
Before beginning the proof, we will need a lemma.
Lemma 5.6.
(1) For any X ∈Q(R) and n ≥2, κn+1(E) = κn(κ2(X)).
(2) For X, Y ∈Q(R), X ∈κn(Y ) if and only if Y ∈κn(X).
Proof. Note that κn(κ2(X)) consists of those atoms Z for which there exists Yi’s and
Y ∈κn−1(κ2(X)) such that Y, Z ⊂Qs
i=1 Yi. If n = 2, then κn−1(κ2(X)) = κ2(X),
and this is precisely the deﬁning property of κ3(X). If n > 2, then κn−1(κ2(X)) =
κn(X) by inductive hypothesis, and we see that such atoms are precisely the ele-
ments of κn+1(X). This proves part (1).
The second assertion is also proven by induction. Suppose X ∈κ2(Y ). Then
there exist Yi’s such that X, Y ⊂Qs
i=1 Yi, so Y ∈κ2(X). Next, assume that the
statement holds for n. If X ∈κn+1(Y ), then X, Z ⊂Qs
i=1 Yi for some Yi’s and
Z ∈κn(Y ).
By deﬁnition, Z ∈κ2(X), and Y ∈κn(Z) by induction.
Hence,
Y ∈κn(κ2(X)) = κn+1(X).
□
Proof of Theorem 5.5. First, we show that κ is an equivalence relation. It is clear
that κ is reﬂexive. If X κ Y and Y κ Z, then X ∈C(Y ) and Y ∈C(Z). Since C(Z)
is complete and contains Y , C(Y ) ⊂C(Z), so X ∈C(Z), i.e., X κ Z. Finally, if
X κ Y , then Proposition 5.4 implies that X ∈κn(Y ) for some n. By the lemma,
Y ∈κn(X) ⊂κ(X), and another application of Proposition 5.4 gives Y κ X.
Next, suppose that X ζ Y . Then X, Y ⊂Qs
i=1 Xi for some Xi’s, so X κY . Since
κ is an equivalence relation, it follows that ζ∗⊂κ.
Conversely, assume that X κ Y , say X ∈κn+1(Y ). Set X0 = X. We recursively
construct Xj ∈κn+1−j(Y ) for 0 ≤j ≤n satisfying Xj κXj+1. Choose X1 ∈κn(Y )
such that X, X1 ⊂Qs1
i=1 Y1,i for some Y1,i’s. This means that X ζ X1. Suppose that
we have constructed the desired atoms up through Xr with r < n. Again, we can
choose Xr+1 ∈κn−r(Y ) satisfying Xr, Xr+1 ⊂Qsr+1
i=1 Yr+1,i for some Yr+1,i’s, and
this gives Xr ζ Xr+1. Note that Xn ∈κ1(Y ) = {Y }, i.e., Xn = Y . We conclude
that X ζ∗Y as desired.
□
Corollary 5.7. For any E ⊂Q(R) nonempty, ψ−1(ψ(E)) = ∪X∈EC(X) = C(E).
In particular, the ζ∗-equivalence class of X is C(X).
Proof. The set ψ−1(ψ(E)) consists of those atoms equivalent to an atom in E,
hence is the union of the ζ∗= κ equivalence classes of atoms in E. This gives the
ﬁrst equality. The second follows immediately from the fact that a union of closed
subsets is closed.
□
To proceed further, we need to impose additional conditions on R.
Proposition 5.8.
(1) If R is reproducible, then for all X ∈Q(R), C(X) = ̟R ◦X = X ◦̟R. In
particular, the subhypergroupoid ̟R satisﬁes the reproductive law.
(2) If R is weakly reproducible, then ̟R satisﬁes the weak reproductive law.
Proof. First, assume that R is reproducible. Suppose that Y ∈C(X), so Y ζ∗X.
By reproducibility, there exist U such that Y ⊂XU, i.e., Y ∈X ◦U. Hence,
ψ(Y ) = ψ(X)ψ(U), so ψ(U) = 1. This shows that U ∈̟R, giving Y ∈X ◦̟R.
Conversely, if Z ∈X ◦̟R, then ψ(Z) = ψ(X). This means that Z ∈C(X). The


## Page 10


10
DANIEL S. SAGE
equality C(X) = ̟R ◦X is proved in the same way. When X ∈̟R, the ﬁrst
statement says that ̟R = ̟R ◦X = X ◦̟R, which is the reproductive law.
If R is weakly reproducible, then the argument given above (with Y = k and
X ∈̟R) shows that there exists U, V ∈̟R such that k ⊂U ◦X ∩X ◦V as
desired.
□
Given Z ∈Q(R), deﬁne
M(Z) = {X ∈Q(R) | ∃Y1, . . . , Ys ∈Q(R) such that X, Z ⊂
s
Y
i=1
Yi}.
Lemma 5.9. If R is reproducible (resp.
weakly reproducible), then M(Z) is a
complete part for all Z (resp. for Z = k).
Proof. Assume that R is reproducible. Take Y ∈M(Z), so Y, Z ⊂Qs
i=1 Yi for
some Yi’s. Suppose that Y ⊂Qn
j=1 Zj. By reproducibility, choose V, W such that
Z ⊂Y V and Zn ⊂WZ. Now, suppose that X ⊂Qn
j=1 Zj also. Then
X ⊂
n
Y
j=1
Zj ⊂


n−1
Y
j=1
Zj

WZ ⊂


n−1
Y
j=1
Zj

WY V ⊂


n−1
Y
j=1
Zj

W
 s
Y
i=1
Yi
!
V.
On the other hand,
Z ⊂Y V ⊂


n
Y
j=1
Zj

V ⊂


n−1
Y
j=1
Zj

WZV ⊂


n−1
Y
j=1
Zj

W
 s
Y
i=1
Yi
!
V.
Thus, Y ∈M(Z), so M(Z) is complete.
If R is weakly reproducible, then the same argument works with Z = k. Indeed,
we need only set W = Zn and use weak reproducibility to choose V such that
k ⊂Y V .
□
Corollary 5.10. If R is reproducible (resp. weakly reproducible), then M(Z) = ̟R
for any Z ∈̟R (resp. for Z = k).
Proof. Suppose that Z ∈̟R. If X ∈M(Z), then X ζ Z by deﬁnition, so X ∈̟R.
Thus, M(Z) ⊂̟R. Conversely, the lemma shows that, under the hypothesis on R,
M(Z) is a complete subset containing Z, so C(Z) = ̟R ⊂M(Z).
□
Theorem 5.11.
(1) If R is reproducible, then ζ is transitive.
(2) If R is weakly reproducible, then X ζ∗k implies that X ζ k.
Proof. Assume that R is reproducible, and take X ζ∗Y . By Proposition 5.8, there
exists U ∈̟R such that Y ∈X ◦U. Since M(k) = ̟R, Corollary 5.10 implies the
existence of Yi’s such that U, k ⊂Qs
i=1 Yi. Thus, Y ⊂XU ⊂X Qs
i=1 Yi ⊃Xk = X,
so Y ζ X. If R is weakly reproducible, the same argument works for Y = k.
□
We are now ready to return to the proof of Theorem 4.3.
We ﬁrst state a
proposition.
Proposition 5.12. Let R be weakly reproducible of ﬁnite length. Then there exists
X1, . . . , Xn ∈Q(R) such that F(R) = Qn
i=1 Xi.


## Page 11


ATOMISTIC SUBSEMIRINGS
11
Proof. First, note that if k ⊂Qn
i=1 Xi, then Qn
i=1 Xi ⊂F(R). Indeed, if Z ⊂
Qn
i=1 Xi is an atom, then Z ζ k, so Z ⊂F(R). The claim follows because Qn
i=1 Xi
is the sum of the atoms it contains.
Choose E = Qn
i=1 Xi containing k such that [E, F(R)] has minimal length. If this
length is 0, then E = F(R), so suppose it is positive, i.e., E ⊊F(R). Take Y ∈̟R
such that Y ⊊E. By Theorem 5.11, Y ζ 1, so there exist Y1, . . . , Ym ∈Q(R) such
that k, Y ⊂E′ = Qm
j=1 Yj. This implies that E = Ek ⊂EE′ and Y = kY ⊂EE′,
and the previous paragraph shows that EE′ ⊂F(R). We obtain E ⊊EE′ ⊂F(R),
contradicting the minimality of the length of [E, F(R)].
□
We apply the proposition to prove part (3) of the theorem. Indeed, if Z ∈Q(R)
and Z ⊂F(R) = Qn
i=1 Xi, then Z ζ 1 by deﬁnition. This means that Z ∈̟R as
desired.
Finally, we prove part (4). Suppose that R is reproducible of ﬁnite length, and
X, Y ⊂F(R) are atoms. By part (3), X, Y ∈̟R. By hypothesis, there exists Z ∈
Q(R) such that Y ∈X ◦Z. Since 1 = ψ(Y ) = ψ(X)ψ(Z) = ψ(Z), Z ⊂F(R) and so
Q([0, F(R)]) = X ◦Q[0, F(R)]). Similarly, one shows Q([0, F(R)]) = Q[0, F(R)])◦X,
so Q([0, F(R)]) is reproducible.
The same argument applies when R is weakly
reproducible; here, one takes Y = k. This completes the proof of Theorem 4.3.
6. Applications to G-algebras
In this section, we apply our results on atomistic semirings to subrepresen-
tation semirings.
We assume throughout that A is a G-algebra which is com-
pletely reducible as a representation. We write QG(A) (resp. FG(A)) instead of
Q(SG(A)) (resp. F(SG(A))). We will now be able to generalize our earlier results
on multiplicity-free G-algebras.
Proposition 6.1. Let A be a G-algebra in which the trivial representation has
multiplicity one. Then A has no proper, nontrivial one-sided invariant ideals if and
only if SG(A) is weakly reproducible.
Remark 6.2. Note that both conditions imply that SG(A) is entire.
Indeed, if
the condition on invariant ideals holds, then the argument given in the proof of
Proposition 2.2 shows that SG(A) is entire.
The analogous statement for weak
reproducibility was shown in Remark 3.4.
Proof. Assume that A has no proper, nontrivial invariant ideals. Fix X ∈QG(A),
and express A as a direct sum of irreducible subrepresentations A = L
i∈I Yi. The
subspace AX is a nonzero invariant left ideal, so we obtain A = AX = P
i∈I XYi.
The trivial representation must accordingly be an irreducible component of some
XYj. The fact that the trivial representation has multiplicity one in A implies that
k ⊂XYj as desired. Similarly, since A = XA, there exists Yl such that k ⊂YlX.
Conversely, suppose that 0 ̸= L ̸= A is an invariant left ideal. Let X ⊂L be an
irreducible submodule. For any Y ∈QG(A), we have Y X ⊂L; since k ∩L = 0,
SG(A) is not weakly reproducible. A similar argument works for right ideals.
□
Corollary 6.3. The atomistic semiring SG(A) is weakly reproducible of ﬁnite
length if
(1) A is a ﬁnite Galois extension of k and G is the Galois group; or
(2) A = End(V ) is a ﬁnite-dimensional G-algebra whose underlying projective
representation V is irreducible.


## Page 12


12
DANIEL S. SAGE
Proof. Schur’s lemma shows that End(V ) contains the trivial representation with
multiplicity one, and the statement about invariant ideals was proved in [8, Theorem
5.2]. The analogous veriﬁcations for the other case are obvious.
□
We are thus able to deﬁne invariants for any G-algebra satisfying the conditions
of Proposition 6.1, without our earlier assumption that the G-algebra is multiplicity-
free. In particular, our results determine two new sequences of invariants associ-
ated to any irreducible projective representation, namely, the condensation groups
Qn
G(End(V )) and the focal subalgebras F n
G(End(V )).
The focal subalgebras F n
G(A) are a decreasing sequence of invariant subalgebras
(i.e., subalgebras which are also subrepresentations) of A.
This is particularly
interesting for A = End(V ) with V irreducible and k algebraically closed because
in this case, there is a complete classiﬁcation of such invariant subalgebras in terms
of representation-theoretic data [8, Theorem 3.23].
For the rest of the paper, we assume that either G is ﬁnite and k is algebraically
closed of characteristic zero or G is a compact group and k = C. We let V be
an irreducible (linear) representation of G, and set A = End(V ). (We make these
assumptions on G and k to guarantee complete reducibility of End(V ); the classi-
ﬁcation of invariant subalgebras described below holds in general.)
An invariant subalgebra of A is determined by data consisting of a quadruple
(H, W, U, U ′); here, H is a ﬁnite index subgroup of G, W is a linear representation
of H such that V = IndG
H(W), and U, U ′ are a pair of projective representations of
H such that W ∼= U ⊗U ′. More precisely, there is a bijection between invariant
algebras and equivalence classes of such quadruples under conjugation by G. In
particular, there are a ﬁnite number of invariant subalgebras.
Given such a quadruple (H, W, U, U ′), we construct the corresponding invariant
subalgebra as follows: Let g1 = e, g2, . . . , gn be a left transversal for H in G. This
gives a direct sum decomposition V = Ln
i=1 giW and an associated block diagonal
invariant subalgebra IndG
H(End(W))
def
= Ln
i=1 End(giW). As an algebra, this is
just the direct product of n copies of End(W). Next, the isomorphism W ∼= U ⊗
U ′ shows that the endomorphism algebra factors (as H-algebras) into the tensor
product End(W) ∼= End(U) ⊗End(U ′). It is now immediate that End(U) ⊗k is
an H-invariant subalgebra of End(W). Finally, we obtain the invariant algebra
for the quadruple: IndG
H(End(U) ⊗k). We remark that the two obvious invariant
subalgebras k and End(V ) correspond to (G, V, k, V ) and (G, V, V, k) respectively.
It now follows that the sequence of focal subalgebras associated to the irreducible
representation V gives rise to a sequence of such quadruples.
The classiﬁcation of invariant subalgebras can be very helpful for computing
the F n
G(End(V )). For example, suppose that End(V ) has no nontrivial invariant
subalgebras, so that any irreducible representation generates End(V ). In order to
show that FG(End(V )) = End(V ), it is only necessary to check that FG(End(V ))
contains a nonscalar matrix.
However, it should be noted that computing the
invariant subalgebras is not necessarily straightforward. Even when G is ﬁnite, it
is not determined by the character table of G. In general, one needs to know the
character tables of a covering group for every subgroup of G whose index divides
dim(V ).
Example 6.4. Let V be the standard representation of S3. We have already seen
that Q1
G(End(V )) = Z2. The focal subalgebra F 1
G(End(V )) = C ⊕σ is isomorphic


## Page 13


ATOMISTIC SUBSEMIRINGS
13
to C⊕C as an algebra; it comes from the quadruple (A3, χ, χ, C), where χ is either
nontrivial character of A3. Since C and σ are not ζ∗-equivalent in QG(F 1
G(End(V ))),
we have Q2
G(End(V )) = Z2 and for m ≥2, F m
G (End(V )) = C (corresponding to
(S3, V, C, V )). Finally, Qn
G(End(V )) = 1 for n ≥3,
Example 6.5. Let W be the three-dimensional irreducible representation of A4. We
will show that QA4(End(W)) is not associative and does not satisfy the reproductive
law.
We have the direct sum decomposition End(W) = C ⊕Z ⊕Z′ ⊕X ⊕Y , where
Z and Z′ correspond to the two nontrivial characters of A4 and X and Y are
isomorphic to W. We can choose a basis for W with respect to which Y (resp.
X) consists of the skew-symmetric (resp. oﬀ-diagonal symmetric) matrices and the
diagonal T is the direct sum of C, Z, and Z′. There are an inﬁnite number of
atoms isomorphic to W, parameterized by [a : b] ∈P1(C); we set
U[a:b] = span{(a+b)E23+(a−b)E32, (a−b)E13+(a+b)E31, (a+b)E12+(a−b)E21}.
In this notation, X = U[1:0] and Y = U[0:1].
Let P = U[1:1]. It is easily checked that P 2 = U[1:−1]. We now calculate that
PC = PZ = PZ′ = P, P(P 2) = T , and PU[a:b] = T ⊕P 2 for [a : b] ̸= [1 : ±1].
We thus see that QA4(End(W)) does not satisfy the reproductive law; if [a : b] ̸=
[1 : ±1], there is no V for which U[a:b] ∈P ◦V . To verify that the associative
law does not hold, note that X ∈(P ◦P 2) ◦X = {C, Z, Z′} ◦X.
However,
P ◦(P 2 ◦X) = P ◦{C, Z, Z′, P} = {P, P 2} does not contain X.
Since PX = T ⊕P 2, we have C, Z, Z′, P 2 ∈̟.
Also, P 2X = T ⊕P, so
Q ∈̟. This implies that F n
A4(End(W)) = End(W) for all n, and by Corollary 4.4,
Qn
A4(End(W)) = 1 for all n.
The only nontrivial invariant subalgebra of End(W) is T . (It corresponds to
(H, χ, χ, C), where H ∼= Z2 × Z2 is the subgroup of order 4 and χ is any nontrivial
character of H.) Thus, one knows that FA4(End(W)) = End(W) as soon as one
know that P 2 ∈̟.
We conclude by computing the condensation groups and focal subalgebras of
endomorphism algebras for simple compact Lie groups.
Theorem 6.6. Let V be an irreducible representation of the simple compact Lie
group G. Then Qn
G(End(V )) = 1 and F n
G(End(V )) = End(V ) for all n.
Proof. If V = C, the statement is trivial. Any other V has dimension at least 2.
By Corollary 4.4, it suﬃces to show that FG(End(V )) = End(V ). Moreover, by
[8, Theorem 4.3], the only proper invariant subalgebra of End(V ) is C. Hence, we
need only show that FG(End(V )) contains a nonscalar matrix.
Let λ be the highest weight of V . The highest weight of the dual representation
V ∗is −w0λ, where w0 is the longest element in the Weyl group. The representation
End(V ) ∼= V ⊗V ∗has a unique irreducible submodule X with highest weight
λ −w0λ. We can write down a highest and lowest weight vector in X explicitly.
Let vλ (resp. wλ) be a highest (resp. lowest) weight vector in V . (The highest and
lowest weights are diﬀerent since dim V ≥2.) Extend the set {vλ, wλ} to a basis of
weight vectors for V , and let v∗
λ, w∗
λ be the corresponding dual basis vectors in V ∗.
Then w∗
λ (resp. v∗
λ) is a highest (resp. lowest) weight vector in V ∗. It follows that
vλ ⊗w∗
λ (resp. wλ ⊗v∗
λ) is a highest (resp. lowest) weight vector in X.


## Page 14


14
DANIEL S. SAGE
Multiplying, we obtain z = (vλ ⊗w∗
λ)(wλ ⊗v∗
λ) = vλ ⊗v∗
λ ∈X2. The matrix z
has rank one, so is not a scalar matrix. Thus, X2 ̸= C. However, tr(z) = 1, so z is
not orthogonal to C. This implies that C ⊂X2. We conclude that ̟ contains at
least two elements, so FG(End(V )) ̸= C.
□
References
[1] P. Corsini, Prolegomena of hypergroup theory, Supplement to Riv. Mat. Pura. Appl., Aviani
Editore, Tricesimo, 1993.
[2] D. Freni, Une note sur le coeur d’un hypergroupe et sur la clˆoture transitive β∗de β, Riv.
Mat. Pura Appl. 8 (1991), 153–156.
[3] D. Freni, A new characterization of the derived hypergroup via strongly regular equivalences,
Comm. Algebra 32 (2002), 3977–3989.
[4] Y. Grabovsky, G. Milton, and D. S. Sage, Exact relations for eﬀective tensors of polycrystals:
Necessary and suﬃcient conditions, Comm. Pure. Appl. Math. 53 (2000), 300–353.
[5] Y. Grabovsky and D. S. Sage, Exact relations for eﬀective tensors of polycrystals. II: Appli-
cations to elasticity and piezoelectricity, Arch. Rat. Mech. Anal. 143 (1998), 331–356.
[6] N. Kwon and D. S. Sage, Subrepresentation semirings and an analogue of 6j-coeﬃcients, J.
Math. Phys. 49 (2008), 063503.
[7] M. Koskas, Groupo¨ıdes, demi-hypergroupes et hypergroupes, J. Math. Pures Appl. 49 (1970),
155–192.
[8] D. S. Sage, Group actions on central simple algebras, J. Algebra 250 (2002), 18–43.
[9] D. S. Sage, Racah coeﬃcients, subrepresentation semirings, and composite materials, Adv.
App. Math 34 (2005), 335–357.
[10] D. S. Sage, Quantum Racah coeﬃcients and subrepresentation semirings, J. Lie Theory 15
(2005), 321–333.
[11] D. S. Sage, Subrepresentation semirings and 3nj-symbols for simply reducible groups,
preprint.
[12] T. Vougiouklis, Hyperstructures and their representations, Hadronic Press, Inc., Palm Har-
bor, Fl, 1994.
Department of Mathematics, Louisiana State University, Baton Rouge, LA 70803
E-mail address: sage@math.lsu.edu

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
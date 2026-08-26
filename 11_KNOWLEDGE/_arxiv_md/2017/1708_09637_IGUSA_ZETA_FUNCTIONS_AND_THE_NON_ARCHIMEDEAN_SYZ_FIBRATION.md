---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1708.09637
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1708.09637_Igusa_zeta_functions_and_the_non-archimedean_SYZ_fibration

> Source: 1708.09637_Igusa_zeta_functions_and_the_non-archimedean_SYZ_fibration.pdf

> Pages: 14

---


## Page 1


IGUSA ZETA FUNCTIONS AND THE NON-ARCHIMEDEAN
SYZ FIBRATION
JOHANNES NICAISE
Abstract. We explain the proof, obtained in collaboration with Chenyang
Xu, of a 1999 conjecture of Veys about poles of maximal order of Igusa zeta
functions.
The proof technique is based on the Minimal Model Program
in birational geometry, but the proof was heavily inspired by ideas coming
from non-archimedean geometry and mirror symmetry; we will outline these
relations at the end of the paper.
This text is intended to be a low-tech
introduction to these topics; we only assume that the reader has a basic
knowledge of algebraic geometry.
1. Introduction
Let f be a non-constant polynomial in Z[x1, . . . , xn], for some n ≥1, with
f(0) = 0. For every prime number p, Igusa’s p-adic zeta function Zf,p(s) of f
at 0 is a meromorphic function on C that encodes the numbers of solutions of
the congruences f ≡0 modulo powers of p that reduce to the origin 0 modulo p.
The precise deﬁnition will be recalled in Section 2. Igusa has proven that Zf,p(s)
is a rational function in p−s by performing a local computation of Zf,p(s) on a
log-resolution of f over Q.
This proof provides a relation between the poles of Zf,p(s) and the geometry of
a log-resolution; see Section 3. However, many fundamental questions about these
poles are still unanswered, the principal one being Igusa’s Monodromy Conjecture,
which relates the poles of Zf,p(s) to roots of the Bernstein polynomial of f – see
(3.3). Igusa’s proof also implies that the order of a pole of Zf,p(s) is at most n,
and that, if p is suﬃciently large, the real part of a pole is at most −lct0(f), the
opposite of the log canonical threshold of f at 0. In 1999, Veys conjectured that the
real part of every pole of order n is equal to −lct0(f). This implies, in particular,
that such poles of maximal order always satisfy the Monodromy Conjecture.
We have proven Veys’s conjecture in collaboration with Chenyang Xu in [NX16a].
The main lines of the proof are explained in Section 4. Although the proof makes
heavy use of the Minimal Model Program in birational geometry, an important
source of inspiration was provided by a combination of non-archimedean geometry
and the theory of mirror symmetry, more precisely Kontsevich and Soibelman’s
non-archimedean interpretation of the SYZ conjecture. This will be explained in
Section 5.
Acknowledgements. I would like to thank the organizers of the VIASM Annual
Meeting 2017 for the invitation to deliver a lecture at the meeting and to write this
survey article for the proceedings. The results presented here are a result of joint
Johannes Nicaise is supported by the ERC Starting Grant MOTZETA (project 306610) of the
European Research Council.
1
arXiv:1708.09637v1  [math.AG]  31 Aug 2017


## Page 2


2
JOHANNES NICAISE
work with Mircea Mustat¸˘a and Chenyang Xu, and it is a pleasure to thank them
both for the pleasant and interesting collaboration. I am also indebted to Wim
Veys for sharing his ideas on the conjecture that constitutes the main subject of
this text.
2. Igusa’s p-adic zeta functions
(2.1) We ﬁx a non-constant polynomial f in Z[x1, . . . , xn], for some n ≥1, with
f(0) = 0. For every prime number p and every integer d ≥0, we set
Nf,p(d) = ♯{x ∈(pZ/pd+1Z)n | f(x) ≡0
mod pd+1}.
Thus Nf,p(d) is the number of solutions of the congruence f ≡0 modulo pd+1 that
reduce to the origin modulo p. To study the asymptotic behaviour of these numbers
as d →∞, we introduce the generating series
Pf,p(T) =
X
d≥0
Nf,p(d)T d
∈Z[[T]].
Now it is natural to ask the following question.
Question 1 (Borevich-Shafarevich, Problem 9 in Ch.1§5 of [BS66]). Is Pf,p(T) a
rational function? That is, can we write it as a quotient of two polynomials in
Z[T]?
Recall that the rationality of Pf,p(T) is equivalent to the existence of a linear
recursion pattern in the sequence of coeﬃcients (Nf,p(d))d≥0.
(2.2) The series Pf,p(T) is easy to compute if the zero locus of f in An
Z is smooth
over Z at the origin of An
Fp: by Hensel’s lemma, every solution modulo pd+1 lifts
to precisely pn−1 solutions modulo pd+2, for all d ≥0, so that Nf,p(d + 1) =
pn−1Nf,p(d). This leads to the formula
Pf,p(T) =
1
1 −pn−1T .
However, the computation is substantially more diﬃcult if f has a singularity,
already in the case of the plane cusp.
Example 1. If f = (x1)2 −(x2)3 and p > 3, the generating series Pf,p(T) is given
by the formula
Pf,p(p−2T) = 1 + (p −1)p−1T + (p −1)p−4T 5 −p−5T 6
(1 −p−1T)(1 −p−5T 6)
.
The reason for rescaling the variable T by a factor p−2 will become apparent
below (spoiler: the exponents 5 and 6 that appear in the denominator are related
to the so-called log canonical threshold 5/6 of the plane cusp singularity).
We
can expect in general that Pf,p(T) will reﬂect some interesting properties of the
singularity of f at 0.


## Page 3


IGUSA ZETA FUNCTIONS AND THE NON-ARCHIMEDEAN SYZ FIBRATION
3
(2.3) Igusa has proven in [Ig75] that Pf,p(T) is always rational. A key step in the
proof is to rewrite the generating series Pf,p(T) as a p-adic integral
Zf,p(s) =
Z
(pZp)n |f|s
p|dx|
where s is a complex variable and |dx| is the normalized Haar measure on Zn
p. This
p-adic integral converges if ℜ(s) > 0 and deﬁnes a analytic function on the complex
right half-plane, which is called Igusa’s p-adic zeta function of f at the origin 0. It
is an easy exercise in p-adic integration to express Zf,p(s) in terms of Pf,p(T): one
has
(1)
Pf,p(p−n−s) = 1 −pnZf,p(s)
1 −p−s
.
Thus it is enough to prove that Zf,p(s) is a rational function in p−s (and, in
particular, extends to a meromorphic function on C). Igusa proved this by taking a
resolution of singularities for f over Q and using the change of variables formula for
p-adic integrals to reduce to the case where f is a monomial, which can be solved
by a simple computation.
(2.4) Igusa’s proof not only establishes the rationality of Zf,p(s) but also provides
some interesting information about the possible poles of Zf,p(s) and their expected
orders in terms of the geometry of a resolution of singularities for f.
This is
a striking result, because it relates arithmetic properties of f (the poles of the
zeta function) with geometric properties of f (the geometry of a resolution of
singularities). A completely explicit formula for Zf,p(s) in terms of a resolution
of f was later given by Denef, for p ≫0. In the next section, we will review the
precise formulations of Igusa’s theorem and Denef’s formula.
3. Igusa’s theorem and Denef’s formula
(3.1) First, we need to introduce some notation.
Let h : Y →An
Q be a log-
resolution for the morphism f : An
Q →A1
Q deﬁned by the polynomial f. This means
that Y is a smooth Q-variety, h is a projective morphism of Q-varieties that is an
isomorphism over An
Q \ div(f), and div(f ◦h) is a strict normal crossings divisor
on Y . Such a morphism h always exists, by Hironaka’s embedded resolution of
singularities in characteristic zero.
(3.2) To every log-resolution h, we associate the following numerical invariants.
We write
div(f ◦h) =
X
i∈I
NiEi
where Ei, i ∈I are the prime components of the divisor div(f ◦h), and the Ni are
their multiplicities. Since h is an isomorphism over the complement of div(f), we
can write the relative canonical divisor of h as
KY/X =
X
i∈I
(νi −1)Ei.
The number νi is called the log-discrepancy of X at the divisor Ei; these are
fundamental invariants in birational geometry. Roughly speaking, the multiplicities


## Page 4


4
JOHANNES NICAISE
Ni measure the complexity of f and the log-discrepancies νi measure the complexity
of the resolution h. For every non-empty subset J of I, we set
EJ = ∩j∈JEj,
Eo
J = EJ \ (∪i/∈JEi).
The sets Eo
J form a stratiﬁcation of div(f ◦h) into locally closed subsets.
Theorem 1 (Igusa [Ig75]). For every prime number p, the zeta function Zf,p(s)
lies in the ring
Q

1
pas+b −1

a,b∈Z>0
.
If s0 is a pole of order m of Zf,p(s), then there exists a subset J of I of cardinality
m such that Eo
J(Qp) ∩h−1(pZn
p) ̸= ∅and ℜ(s0) = −νj/Nj for every j in J.
Theorem 2 (Denef [De91]). If the prime number p is suﬃciently large, then
Zf,p(s) = p−n X
∅̸=J⊂I
♯(E
o
J(Fp) ∩h
−1(0))
Y
j∈J
p −1
pNjs+νj −1
where (·) denotes reduction modulo p.
To be precise, Denef’s formula is valid when the resolution h has “good reduction
modulo p” in a certain technical sense; for our purposes, it suﬃces to know that
this condition is always satisﬁed for p ≫0.
Example 2. A log-resolution h for f = (x1)2−(x2)3 can be constructed by means of
three consecutive point blow-ups (see Figure 1). Then div(f ◦h) has four irreducible
components: the strict transform E0 of div(f), with numerical data N0 = ν0 =
1, and three exceptional components E1, E2, E3 whose numerical data (Ni, νi)
are given by (2, 2), (3, 3) and (6, 5), respectively. The log resolution h has good
reduction modulo p for all primes p > 3; in those cases, Denef’s formula yields
p2
p −1Zf,p(s)
=
p
p−2−2s
1 −p−2−2s + p
p−3−3s
1 −p−3−3s + (p −2)
p−5−6s
1 −p−5−6s
+(p −1)
p−5−6s
1 −p−5−6s

p−1−s
1 −p−1−s +
p−2−2s
1 −p−2−2s +
p−3−3s
1 −p−3−3s

which is compatible with the comparison formula (1) and our expression for
Pf,p(p−2T) in Example 1.
E3 (6,5)
E2 (3,3)
E0 (1,1) 
E1 (2,2) 
Figure 1. Log-resolution of the plane cusp


## Page 5


IGUSA ZETA FUNCTIONS AND THE NON-ARCHIMEDEAN SYZ FIBRATION
5
(3.3) We can draw some immediate consequences from Igusa and Denef’s results.
Igusa’s theorem implies that the real parts of the poles of Zf,p(s) are all contained
in the ﬁnite set
{−νi
Ni
| i ∈I, Ei(Qp) ∩h−1(pZn
p) ̸= ∅}.
In practice, most of these candidates will not be real parts of actual poles of Zf,p(s).
For one thing, the list of candidates strongly depends on the choice of the resolution
h, whereas Zf,p(s) only depends on f and p. But even if n = 2, when there exists a
minimal log-resolution h of f, most of the candidates will not appear as real parts
of poles of the zeta function. A partial explanation of this phenomenon would be
given by the so-called Monodromy Conjecture, which puts an additional restriction
on the poles of Zf,p(s).
Conjecture 1 (Igusa’s Monodromy Conjecture). If p is suﬃciently large and s0
is a pole of Zf,p(s), then ℜ(s0) is a root of the Bernstein polynomial of f at
0. In particular, exp(2πiℜ(s0)) is a local monodromy eigenvalue of the complex
hypersurface deﬁned by the equation f = 0.
The Monodromy Conjecture quantiﬁes how the singularities of the complex
hypersurface deﬁned by f = 0 inﬂuence the poles of the p-adic zeta function
Zf,p(s), and thus the asymptotic behaviour of the coeﬃcients of the generating
series Pf,p(T). This conjecture has been solved if n = 2 by Loeser [Lo88], and
also for some special classes of singularities, but the general case is wide open. We
refer to [Ni10] for an overview of results that were known around 2010; a signiﬁcant
breakthrough since that time was the proof for Newton non-degenerate polynomials
in three variables – see [LVP11] and [BV16].
(3.4) Igusa’s theorem also implies that the order of a pole s0 of Zf,p(s) is at most
max{♯J | J ⊂I, ℜ(s0) = −νj/Nj for all j ∈J, EJ(Qp) ∩h−1(pZn
p) ̸= ∅}.
In particular, it is at most n, since EJ is empty if J has more than n elements
(n + 1 diﬀerent prime components of a strict normal crossings divisor on a variety
of dimension n can never intersect in a point).
(3.5) Finally, from Denef’s formula, it also follows that the real part of a pole of
Zf,p(s) is at most
−min{ νi
Ni
| i ∈I, Ei ∩h−1(0) ̸= ∅}
when p is suﬃciently large (if Ei ∩h−1(0) is empty, then Ei ∩h
−1(0) is empty for
p ≫0). The number
lct0(f) = min{ νi
Ni
| i ∈I, Ei ∩h−1(0) ̸= ∅}
is an important invariant in birational geometry, called the log-canonical threshold
of f at 0. It is independent of the choice of a log-resolution h. It is used to measure
the degree of the singularity of f at 0, and to divide the singularities into diﬀerent
types in the Minimal Model Program.


## Page 6


6
JOHANNES NICAISE
(3.6) The main subject of this survey is the following conjecture.
Conjecture 2 (Veys 1999). Assume that p is suﬃciently large. If s0 is a pole of
Zf,p(s) of order n, then ℜ(s0) = −lct0(f).
Thus if Zf,p(s) has a pole of the largest possible order (namely, n), then its real
part is also as large as possible. Veys’s conjecture was originally stated in [LV99]
for a diﬀerent type of zeta function (the so-called topological zeta function), but
the proof we will present is valid for the topological and motivic zeta functions, as
well; see [NX16b, §3]. Veys’s conjecture implies, in particular, that poles of order
n satisfy Igusa’s Monodromy Conjecture, because it is known that −lct0(f) is the
largest root of the Bernstein polynomial of f at 0 (see for instance Theorem 10.6
in [Ko97]).
4. Proof of Veys’s conjecture
(4.1) We will deduce Veys’s conjecture from a more general result about the
geometry of log-resolutions. Let k be a ﬁeld of characteristic zero, X a smooth
k-variety, f : X →A1
k a dominant morphism and h : Y →X a log-resolution of f
as above. We ﬁx a closed point x on X such that f(x) = 0. The situation we have
studied so far corresponds to the case k = Q, X = An
Q, x = 0. We will continue to
use the notations Ni, νi, EJ etc. The result that we will prove is local on X at the
point x; shrinking X around x, we may assume that EJ ∩h−1(x) ̸= ∅as soon as
EJ ̸= ∅, for every non-empty subset J of I. This assumption simpliﬁes some of the
notations we will use.
(4.2) For every i ∈I, we set wtf(Ei) = νi/Ni and we call this value the weight of
f at Ei. The log-canonical threshold of f at x is then given by
lctx(f) = min{wtf(Ei) | i ∈I}.
We write Y0 for the divisor
div(f ◦h) =
X
i∈I
NiEi,
and we denote by ∆(Y0) its dual intersection complex. This is a ﬁnite ∆-complex
whose vertices correspond bijectively to the components Ei, i ∈I, and such that
for every subset J of I, the number of faces spanned by the vertices vj with j ∈J
is equal to the number of connected components of EJ. We introduce a function
wtf : ∆(Y0) →R
that is completely characterized by the following properties:
• for every i ∈I, the value of wtf at the vertex of ∆(Y0) corresponding to
Ei is given by wtf(Ei) = νi/Ni;
• the function wtf is aﬃne on every face of ∆(Y0).
Example 3. In the case of the minimal log-resolution of the plane cusp (Example
2) we can immediately recover the dual intersection complex ∆(Y0) and the
weight function wtf from Figure 1.
Since the dimension of Y0 equals one, the
dual intersection complex is nothing else than the dual graph of Y0, with four
vertices v0, . . . , v3 corresponding to the irreducible components E0, . . . , E3 and three
edges corresponding to the intersection points of these components. The weight


## Page 7


IGUSA ZETA FUNCTIONS AND THE NON-ARCHIMEDEAN SYZ FIBRATION
7
function wtf is characterized by its values wtf(v0) = wtf(v1) = wtf(v2) = 1 and
wtf(v3) = 5/6, and the property that wtf is aﬃne on every edge.
v3
v2
v1
v0
E3 (6,5) 
E2 (3,3) 
E1 (2,2) 
E0 (1,1) 
Y0
 
1 
1 
5/6 
1 
Δ(Y0)
Figure 2. The weight function of the minimal log-resolution of
the plane cusp
(4.3) The key observation is that wtf seems to induce a ﬂow on ∆(Y0) in the
direction of decreasing weights, and that this ﬂow collapses ∆(Y0) onto the locus
where wtf is minimal, that is, equal to lctx(f). Recall that a collapse if a particular
type of strong deformation retraction that can be deﬁned in a combinatorial way
for ∆-complexes. This observation can be made precise in the case n = 2 (see for
instance Example 3 and Figure 2) but it is not clear what the correct notion of
a ﬂow on a ∆-complex would be in higher dimensions. We will explain the origin
of this observation in Section 5: it has roots in Kontsevich and Soibelman’s non-
archimedean SYZ ﬁbration for degenerations of Calabi-Yau varieties in the theory
of mirror symmetry.
(4.4) In [NX16b], Chenyang Xu and the author have proven two results that
provide compelling evidence for the above observation. We denote by ∆(Y0)=lctx(f)
the locus where wtf reaches its minimal value lctx(f); this is a union of faces of
∆(Y0). The ﬁrst result can be understood as follows: if we place ourselves at any
point of ∆(Y0), then the weight function should somehow select a path along which
the weight decreases and which ends in ∆(Y0)=lctx(f), the locus of minimal weight.
If our starting point lies in the interior of a maximal face σ of ∆(Y0) and the weight
function wtf is constant on σ, then wtf does not single out any direction at all.
So, if our observation is valid, this can only happen when σ is already contained in
the locus of minimal weight. This property is conﬁrmed by the following theorem.
Theorem 3 (Nicaise–Xu, Theorem 2.4 in [NX16b]). If wtf is constant on a
maximal face σ of ∆(Y0), then its value on σ is the minimal value lctx(f) of wtf.
The proof of the theorem uses sophisticated techniques from the Minimal Model
Program (MMP) in birational geometry; the main idea is to run a well-chosen MMP
algorithm on the pair (Y, Y0) and to study the behaviour of Y near the stratum of
Y0 corresponding to the face σ.


## Page 8


8
JOHANNES NICAISE
(4.5) Now we consider the homotopy types of the intermediate level sets of the
function wtf. A small technical complication (which will disappear in the SYZ
picture in Section 5) is that the components of Y0 come in two ﬂavours:
the
exceptional components of h and the components of the strict transform of div(f).
The following theorem reﬁnes a fundamental result of de Fernex, Koll´ar and Xu
[dFKX17].
Theorem 4 (Nicaise–Xu, Theorem 4.10 in [NX16b]). Assume that div(f) is
reduced. We denote by ∆(Y0)exc the subcomplex of ∆(Y0) spanned by the vertices
that correspond to exceptional components of h. For every w ∈R, we denote by
∆(Y0)≤w the subcomplex of ∆(Y0) spanned by the vertices v such that wtf(v) ≤w,
and we deﬁne ∆(Y0)≤w
exc accordingly.
• Assume that lctx(f) = 1 (that is, (X, div(f)) is log-canonical at x). There
exists a collapse of ∆(Y0) onto ∆(Y0)=lctx(f) that simultaneously collapses
∆(Y0)≤w onto ∆(Y0)=lctx(f) for every w ≥lctx(f).
In particular, the
inclusion maps of ∆(Y0)=lctx(f) and ∆(Y0)≤w into ∆(Y0) are homotopy
equivalences.
• Assume that lctx(f) ̸= 1.
There exists a collapse of ∆(Y0)exc onto
∆(Y0)=lctx(f) that simultaneously collapses ∆(Y0)≤w
exc onto ∆(Y0)=lctx(f) for
every w ≥lctx(f). In particular, the inclusion maps of ∆(Y0)=lctx(f) and
∆(Y0)≤w
exc into ∆(Y0)exc are homotopy equivalences.
Note that in the second case of Theorem 4, we have lctx(f) < 1 so that
∆(Y0)=lctx(f) is contained in ∆(Y0)exc (components Ei in the strict transform of
div(f) all have Ni = νi = 1 because we assumed that div(f) is reduced).
(4.6) Now let us explain how Theorem 3 implies Veys’ conjecture. Let f be a non-
constant polynomial in Z[x1, . . . , xn] and let h : Y →An
Q be a log-resolution for the
morphism f : An
Q →A1
Q. Suppose that s0 is a pole of order n of Zf,p(s), for some
suﬃciently large prime number p. Denef’s formula then implies that there exists a
subset J of I of cardinality n such that EJ ∩h−1(0) ̸= ∅and ℜ(s0) = −νj/Nj for
every j ∈J. Then EJ is a ﬁnite set of points, and each of these points corresponds
to a face of ∆(Y0) of dimension n −1 on which wtf is constant with value −ℜ(s0).
Since the dimension of ∆(Y0) is at most n −1, such a face is always maximal. Now
Theorem 3 implies that ℜ(s0) = −lct0(f), which conﬁrms Veys’ conjecture.
5. The non-archimedean SYZ fibration
(5.1) To conclude this survey, we explain how the observation in (4.3) originated
from the non-archimedean SYZ ﬁbration of Kontsevich and Soibelman.
The
starting point of this story is the theory of mirror symmetry, which has grown out
of mathematical physics (string theory) and has led to fascinating developments in
algebraic geometry. For lack of competence, we will only superﬁcially discuss the
physical background. According to string theory, our universe can be described as
a 10-dimensional real manifold: the 4 dimensions of space-time and an additional
6 dimensions coming from a complex Calabi-Yau 3-fold. Towards the end of the
80s, physicists realized that the Calabi-Yau manifold was not uniquely determined
by the physical theory; rather, Calabi-Yau 3-folds seemed to come in mirror pairs
giving rise to equivalent physical theories. One famous property of mirror 3-folds


## Page 9


IGUSA ZETA FUNCTIONS AND THE NON-ARCHIMEDEAN SYZ FIBRATION
9
(X, ˇX) is the following symmetry of their Hodge diamonds:
hp,q(X) = h3−p,q( ˇX).
Systematic searches in databases of Calabi-Yau 3-folds supplied empirical evidence
for the mirror phenomenon.
(5.2) Mirror symmetry caught the attention of algebraic geometers through a
spectacular application to enumerative geometry by Candelas, de la Ossa, Green
and Parkes around 1990. They managed to compute numbers of rational curves
of ﬁxed degrees on the quintic threefold X; these are now known as Gromov-
Witten invariants. Their calculation relied on the insight that the complex and
symplectic geometries of X and its mirror partner ˇX are swapped: the Gromov-
Witten invariants of X (which are symplectic in nature) can be recovered from
certain period integrals on ˇX (which live in complex geometry and are easier to
compute). At that time, there was no mathematical framework available to explain
these results; a rigorous mathematical conﬁrmation was given only around 1995.
(5.3) An important challenge for algebraic geometers was then to give an exact
deﬁnition of what it means to be a mirror pair and to devise techniques to construct
such pairs.
In recent years, much progress has been made, in particular by
Kontsevich–Soibelman and Gross–Siebert. Both of these programs are based on
a conjectural geometric explanation of mirror symmetry due to Strominger, Yau
and Zaslow, known as the SYZ conjecture (1996). Let X ∗be a projective family of
n-dimensional complex Calabi-Yau manifolds over a punctured disk D∗in C, and
assume that this family has semistable reduction over the unpunctured disk D and
that it is maximally degenerate. The latter condition means that the monodromy
transformation on the degree n cohomology of the general ﬁber Xt of X ∗has a
Jordan block of rank n + 1. Then Xt should admit a ﬁbration ρ : Xt →S where
S is an n-dimensional topological manifold and the ﬁbers of ρ are so-called speical
Lagrangian tori in Xt. As the parameter t ∈D∗tends to 0, the ﬁbers of ρ are
contracted (in the sense of Gromov-Hasudorﬀconvergence of metric spaces) and we
are left with the base S. The mirror partner of Xt is then constructed by dualizing
the torus ﬁbration ρ over the locus where it is smooth and compactifying the result
in a suitable way (this involves deforming the dual ﬁbration by so-called quantum
corrections, which is the most subtle part of the picture). We refer to the excellent
survey paper [Gr13] for a more precise statement and additional background on the
SYZ conjecture, as well as the Gross–Siebert program.
(5.4) The SYZ conjecture seems very diﬃcult to solve in its original diﬀerential-
geometric set-up. A fundamental insight of Kontsevich and Soibelman in [KS06]
is that a close analog of the SYZ ﬁbration can be found in the world of non-
archimedean geometry, more precisely in the context of Berkovich spaces. Here, the
base S of the ﬁbration arises as a so-called skeleton and it is intimately related to the
geometry of minimal models of the degeneration X ∗in the sense of the Minimal
Model Program.
We will now explain the construction of the non-archimedean
SYZ ﬁbration, as well as its relation with the results in Section 4. Let us emphasize
right away that the non-archimedean SYZ ﬁbration is not merely an analog of the
conjectural structure in a diﬀerent context; it can eﬀectively be used to realize the
original goal of deﬁning an constructing mirror partners over the complex numbers,
by means of non-archimedean GAGA and algebraization techniques. The case of


## Page 10


10
JOHANNES NICAISE
K3 surfaces was discussed in [KS06], but substantial technical diﬃculties are still
obstructing this approach in higher dimensions.
(5.5) We will work over an algebraic model of the complex disk D, namely, the
spectrum Spec R of the ring R = k[[t]] of formal power series over an algebraically
closed ﬁeld k of characteristic zero. We write K = k((t)) for the quotient ﬁeld of R;
then Spec K is the algebraic analog of the punctured disk D∗. The t-adic absolute
value on K, deﬁned by |a| = exp(−ordta) for all non-zero elements a in K, endows
K with an analytic structure and allows one to develop a theory of analytic functions
and analytic spaces over K. The theory that is most suited for our purposes is
Berkovich’s theory of K-analytic spaces, ﬁrst presented in [Be90]. To every K-
scheme of ﬁnite type X, one can attach a K-analytic space Xan which is called the
analytiﬁcation of X, in analogy with the situation over the complex numbers. If
X is proper over K, then the non-archimedean GAGA principle guarantees that
Xan completely determines the geometry of X; the upshot is that we can apply
additional tools to analyze Xan coming from analytic geometry.
(5.6) Now let Z be a smooth, projective, geometrically connected K-scheme with
trivial canonical line bundle.
For instance, if X ∗is the family of Calabi-Yau
manifolds considered above, we get such an object Z over K = C((t)) by base
change to the quotient ﬁeld of the completed local ring of D at the origin. An snc
model for Z is a regular ﬂat projective R-scheme Z endowed with an isomorphism of
K-schemes ZK →Z such that the special ﬁber Zk is a divisor with strict normal
crossings. Then we can attach to Zk a dual intersection complex ∆(Zk) in the
same way as before. A fundamental theorem of Berkovich implies that there exists
a canonical topological embedding of ∆(Zk) into Zan, whose image is called the
skeleton of Z and is denoted by Sk(Z ). Moreover, this embedding has a canonical
retraction ρZ : Zan →Sk(Z ) that extends to a strong deformation retraction
of Zan onto Sk(Z ). We refer to [Ni16, §2.5] for an explicit example. Thus Zan
is homotopy equivalent to ∆(Zk), for every snc model Z of Z. We can use the
retraction maps ρZ to organize the skeleta Sk(Z ) into a projective system, indexed
by the snc models Z ordered by the dominance relation. Then one can show that
the natural continuous map
Zan →lim
←−
Z
Sk(Z )
induced by the retractions ρZ is a homeomorphism. This result gives a complete
description of the topology of Zan in terms of the birational geometry of its snc
models. It also provides a natural bridge between birational geometry and non-
archimedean geometry.
(5.7) Let ω be a volume form on Z. In a joint work with Mircea Mustat¸˘a [MN15],
we deﬁned a weight function
wtω : Xan →R ∪{+∞}
which reﬁnes a construction of Kontsevich and Soibelman in [KS06] and is also
related to work of Boucksom, Favre and Jonsson in [BFJ08]. Let Z be an snc
model of Z. Then we can view ω as a rational section of the relative log canonical
line bundle ωZ /R(Zk,red); we denote the associated Cartier divisor by divZ (ω). The
restriction of wtω to the skeleton Sk(Z ) of Z can be computed in the following
way. It is aﬃne on every face, so that it is completely determined by its values at


## Page 11


IGUSA ZETA FUNCTIONS AND THE NON-ARCHIMEDEAN SYZ FIBRATION
11
the vertices of Sk(Z ). Each vertex v corresponds to a prime component E of the
special ﬁber Zk; the value of wtω at v equals ν/N, where N is the multiplicity of
E in Zk and ν is the multiplicity of E in divZ (ω). Note the similarity with the
deﬁnition of the weight function wtf in (4.2). The weight function wtf can also be
interpreted as the weight function of a volume form on a suitable K-analytic space;
see [MN15, §6].
(5.8) The essential skeleton Sk(Z) of Z is the set of points in Zan where wtω
reaches its minimal value. This is a non-empty compact subspace of Zan. One can
show that the weight function wtω is strictly decreasing under the retraction map
ρZ , for every snc model Z of Z, so that Sk(Z) is always contained in Sk(Z ). More
precisely, since wtω is aﬃne on every face of Sk(Z ), the essential skeleton Sk(Z)
is a union of faces of Sk(Z ). The crucial point is that, whereas Sk(Z ) obviously
depends on Z , the essential skeleton Sk(Z) does not depend on the choice of an
snc model. It is also independent of ω, because multiplying ω with a constant in
K∗shifts the weight function by a constant integer. In Kontsevich and Soibelman’s
vision of the non-archimedean SYZ ﬁbration, the base of the ﬁbration is precisely
the essential skeleton Sk(Z). In general, there does not exist any snc model Z of
Z such that the essential skeleton Sk(Z) coincides with Sk(Z ). However, it was
shown by Chenyang Xu and the author in [NX16a] that we can identify Sk(Z) with
the skeleton of a suitable model of Z if we enlarge the class of models by considering
so-called divisorially log terminal (dlt) models. For such (good) dlt models, one can
generalize the construction of the skeleton Sk(Z ) (which is still homeomorphic to
the dual intersection complex of Zk) and the retraction map ρZ : Zan →Sk(Z ).
If Z is a minimal dlt model of Z in the sense of the Minimal Model Program, then
Sk(Z) = Sk(Z ).
(5.9) This interpretation of Sk(Z) has two important advantages: it provides
us with a map ρZ : Zan →Sk(Z), which plays the role of the SYZ ﬁbration in
the non-archimedean context (beware that it depends on the choice of a minimal
dlt model, which is not unique in general). Moreover, we can use tools from the
Minimal Model Program to study the properties of the essential skeleton Sk(Z) and
the map ρZ . According the the SYZ heuristic, the ﬁbers of the non-archimedean
SYZ ﬁbration ρZ should be contracted in the limit t →0, in a suitable sense, so
that Zan collapses onto the locus Sk(Z) where the weight function wtω reaches
its minimal value. Then it is tempting to speculate that the weight function wtω
induces a ﬂow on Zan towards Sk(Z), along paths of decreasing weight. It is not
yet clear what an appropriate deﬁnition of ﬂow would be in this context (except if
dim(Z) = 1; see Example 4). However, this heuristic has led us to formulate and
prove the following theorems, which at their turn were the source of Theorems 3
and 4 above.
Theorem 5 (Nicaise–Xu, Theorem 5.4 in [NX16b]). Let Z be an snc model of Z.
If wtω is constant on a maximal face σ of Sk(Z ), then its value on σ is the minimal
value of wtω. In other words, σ is contained in the essential skeleton Sk(Z) of Z.
Theorem 6 (Nicaise–Xu, Theorem 5.6 in [NX16b]). Denote by wmin the minimal
value of wtω on Zan, and let Z be an snc model of Z. For every w ∈R, we denote
by Sk(Z )≤w the subcomplex of Z spanned by the vertices v such that wtω(v) ≤w.
There exists a collapse of Sk(Z ) onto Sk(Z) that simultaneously collapses Sk(Z )≤w


## Page 12


12
JOHANNES NICAISE
for every w ≥wmin. In particular, the inclusion maps of Sk(Z) and Sk(Z )≤w into
Sk(Z ) are homotopy equivalences.
Combining Theorem 6 with Berkovich’s strong deformation retraction of Zan onto
Sk(Z ), one can then show that for every minimal dlt model Z of Z, the retraction
map ρZ : Zan →Sk(Z) can be extended to a strong deformation retraction of Zan
onto the essential skeleton Sk(Z), which is in line with the SYZ heuristic.
(5.10) There are some interesting open questions related to the shape of the
essential skeleton Sk(Z). Assume that Z has semi-stable reduction over R (that is,
it has an snc model with reduced special ﬁber) and that it is maximally degenerate
(meaning that the monodromy transformation on the ℓ-adic cohomology of Z in
degree n = dim(Z) has a Jordan block of size n+1). Then it was shown in [NX16a,
4.2.4] that Sk(Z) is a closed pseudo-manifold of dimension n. If Z is an abelian
variety, then Sk(Z) is homeomorphic to a real torus of dimension n, by [HN17,
4.3.3].
Now assume that Z is Calabi-Yau, in the sense that it is geometrically
simply connected and the Hodge numbers h0,i(Z) vanish for 0 < i < n. Then
Sk(Z) has the rational homology of the n-sphere Sn by [NX16a, 4.2.4], and its
fundamental group has trivial proﬁnite completion [HN17, 6.1.3]. It is expected
that Sk(Z) is homeomorphic to Sn, but this appears to be a very hard question; it
has been solved by Koll´ar and Xu in [KX16] for n ≥3, and for n = 4 assuming that
Z has a minimal dlt model that is snc. A crucial diﬃculty is proving that Sk(Z) is
a topological manifold.
Example 4. The easiest example of a non-archimedean SYZ ﬁbration is provided
by a Tate elliptic curve over K. This is an elliptic curve E over K with Kodaira–
N´eron reduction type In, for some n > 0. Every smooth and proper K-curve of
positive genus has a unique minimal snc model; the condition of having reduction
type In with n ≥2 is then equivalent with the property that the special ﬁber of the
minimal snc model E of E is a reduced cycle of n rational curves (for simplicity we
exclude the case n = 1: then the minimal normal crossings model has a reduced
special ﬁber which is a rational curve intersecting itself at one point).
In this case, E is also a minimal dlt model of E. Thus the essential skeleton
Sk(E) equals the skeleton Sk(E ) of E , which we can identify with the dual graph
of Ek; this is a circle subdivided by n vertices (see Figure 3 for an example where
n = 3).
To reconstruct the entire K-analytic space Ean, we take the projective limit of
the dual graphs Sk(E ′) where E ′ →E is a composition of blow-ups of points in
the special ﬁber. The eﬀect of such a point blow-up can take two forms: either the
center of the blow-up is an intersection point of components in the special ﬁber, in
which case the corresponding edge of the skeleton is subdivided by adding a vertex
in its interior; or the center lies on a unique component of the special ﬁber, in which
case a new edge is attached to the vertex of the dual graph corresponding to this
unique component. This is illustrated in Figure 3.
Repeatedly blowing up points and passing to the projective limit, what appears
is a circle Sk(E) with inﬁnitely many trees growing out of it, each tree splitting into
inﬁnitely many branches at inﬁnitely many points (Figure 4). The non-archimedean
SYZ ﬁbration ρE contracts all of these trees onto the circle. For every volume form
ω on E, the weight function wtω is constant along the circle Sk(E) and strictly
increasing as we move away from Sk(E) along one of the branches.


## Page 13


IGUSA ZETA FUNCTIONS AND THE NON-ARCHIMEDEAN SYZ FIBRATION
13
Figure 3. Eﬀect of point blow-ups on the dual graphs
Figure 4. Analytiﬁcation of a Tate elliptic curve; the essential
skeleton is the circle in the middle
References
[Be90] V. G. Berkovich. Spectral theory and analytic geometry over non-archimedean ﬁelds.
Volume
33
of
Mathematical
Surveys
and
Monographs.
American
Mathematical
Society,
Providence, RI (1990)
[BS66] A.I. Borevich and I.R. Shafarevich. Number theory. Volume 20 of Pure and Applied
Mathematics. Academic Press, New York-London (1966)
[BV16] B. Bories and W. Veys. Igusa’s p-adic local zeta function and the monodromy conjecture
for non-degenerate surface singularities. Mem. Amer. Math. Soc. 242 (2016)
[BFJ08] S. Boucksom, C. Favre and M. Jonsson. Valuations and plurisubharmonic singularities.
Publ. Res. Inst. Math. Sci. 44(2), pages 449–494 (2008)
[dFKX17] T. de Fernex, J. Koll´ar and C. Xu. The dual complex of singularities. In: Higher
dimensional algebraic geometry, in honour of Professor Yujiro Kawamatas 60th birthday.
Volume 74 of Adv. Stud. Pure Math., pages 103–130. Amer. Math. Soc., Providence, RI (2017)
[De91] J. Denef. Local zeta functions and Euler characteristics. Duke Math. J. 63(3), pages 713–
721 (1991)
[Gr13] M. Gross. Mirror symmetry and the Strominger-Yau-Zaslow conjecture. In:
Current
developments in mathematics 2012, pages 133–191. Int. Press, Somerville, MA (2013)
[HN17] L.H. Halle and J. Nicaise. Motivic zeta functions of degenerating Calabi-Yau varieties.
Preprint, arXiv:1701.09155.
[Ig75] J. Igusa. Complex powers and asymptotic expansions. II. J. Reine Angew. Math. 278/279,
pages 307–321 (1975)
[Ko97] J. Koll´ar. Singularities of pairs. In: Algebraic geometry – Santa Cruz 1995. Volume 62 of
Proc. Sympos. Pure Math., Part 1, pages 221–287. Amer. Math. Soc., Providence, RI (1997)


## Page 14


14
JOHANNES NICAISE
[KX16] J. Koll´ar and C. Xu. The dual complex of Calabi-Yau pairs. Invent. Math. 205(3), pages
527–557 (2016)
[KS06] M. Kontsevich and Y. Soibelman. Aﬃne structures and non-archimedean analytic spaces.
In: P. Etingof, V. Retakh and I.M. Singer (eds). The unity of mathematics. In honor of the
ninetieth birthday of I. M. Gelfand. Volume 244 of Progress in Mathematics, pages 312–385.
Birkh¨auser Boston, Inc., Boston, MA (2006)
[LV99] A. Laeremans and W. Veys. On the poles of maximal order of the topological zeta function.
Bull. London Math. Soc. 31, pages 441–449 (1999)
[LVP11] A. Lemahieu and L. Van Proeyen. Monodromy conjecture for nondegenerate surface
singularities. Trans. Amer. Math. Soc. 363(9), pages 4801–4829 (2011)
[Lo88] F. Loeser. Fonctions d’Igusa p-adiques et polynˆomes de Bernstein. Amer. J. Math. 110(1),
pages 1–21 (1988)
[MN15] M. Mustat¸˘a and J. Nicaise. Weight functions on non-archimedean analytic spaces and the
Kontsevich-Soibelman skeleton. Alg. Geom. 2(3), pages 365–404 (2015)
[Ni10] J. Nicaise. An introduction to p-adic and motivic zeta functions and the monodromy
conjecture. In: G. Bhowmik, K. Matsumoto and H. Tsumura (eds.), Algebraic and analytic
aspects of zeta functions and L-functions. Volume 21 of MSJ Memoirs, pages 115–140.
Math. Soc. of Japan (2010)
[Ni16] J. Nicaise. Berkovich skeleta and birational geometry. In: M. Baker and S. Payne (eds.),
Nonarchimedean and Tropical Geometry. Simons Symposia, pages 173–194. Springer, Cham.
(2016)
[NX16a] J. Nicaise and C. Xu. The essential skeleton of a degeneration of algebraic varieties.
Amer. Math. J., 138(6):1645–1667, 2016.
[NX16b] J. Nicaise and C. Xu. Poles of maximal order of motivic zeta functions. Duke Math. J.
165:2, pages 217–243 (2016)
Imperial College, Department of Mathematics, South Kensington Campus, London
SW72AZ, UK, and KU Leuven, Department of Mathematics, Celestijnenlaan 200B, 3001
Heverlee, Belgium
E-mail address: j.nicaise@imperial.ac.uk

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
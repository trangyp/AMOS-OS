---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1711.08939v7
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1711.08939v7_On_the_mathematical_and_foundational_significance_of_the_uncountable

> Source: 1711.08939v7_On_the_mathematical_and_foundational_significance_of_the_uncountable.pdf

> Pages: 39

---


## Page 1


arXiv:1711.08939v7  [math.LO]  11 Mar 2019
ON THE MATHEMATICAL AND FOUNDATIONAL
SIGNIFICANCE OF THE UNCOUNTABLE
DAG NORMANN AND SAM SANDERS
Abstract. We study the logical and computational properties of basic theo-
rems of uncountable mathematics, including the Cousin and Lindel¨of lemma
published in 1895 and 1903. Historically, these lemmas were among the ﬁrst
formulations of open-cover compactness and the Lindel¨of property, respec-
tively. These notions are of great conceptual importance: the former is com-
monly viewed as a way of treating uncountable sets like e.g. [0, 1] as ‘almost
ﬁnite’, while the latter allows one to treat uncountable sets like e.g. R as ‘almost
countable’. This reduction of the uncountable to the ﬁnite/countable turns out
to have a considerable logical and computational cost: we show that the afore-
mentioned lemmas, and many related theorems, are extremely hard to prove,
while the associated sub-covers are extremely hard to compute.
Indeed, in
terms of the standard scale (based on comprehension axioms), a proof of these
lemmas requires at least the full extent of second-order arithmetic, a system
originating from Hilbert-Bernays’ Grundlagen der Mathematik. This obser-
vation has far-reaching implications for the Grundlagen’s spiritual successor,
the program of Reverse Mathematics, and the associated G¨odel hierachy. We
also show that the Cousin lemma is essential for the development of the gauge
integral, a generalisation of the Lebesgue and improper Riemann integrals that
also uniquely provides a direct formalisation of Feynman’s path integral.
The content of this paper extends [70] in that Sections 3.3.4 and 3.4 below are
new. Small corrections/additions have also been made to reﬂect new developments.
1. Introduction
1.1. Inﬁnity: hubris and catharsis. It is a commonplace that ﬁnite and count-
able sets exhibit many useful properties that uncountable sets lack. Conveniently,
there are properties that allow one to treat uncountable sets as though they were
ﬁnite or countable, namely open-cover compactness and the Lindel¨of property, i.e.
the statement that an open cover has a ﬁnite, respectively countable, sub-cover.
These notions are well-established: the Cousin lemma ([15, p. 22]) on the open-
cover compactness of subsets of R2, dates back1 135 years, while the Lindel¨of lemma
([50, p. 698]) on the Lindel¨of property of Rn, dates back about 115 years. Despite
their basic nature, their central role in analysis, and a long history, little is known
about the logical and computational properties of the Cousin and Lindel¨of lemmas.
In a nutshell, we aim to ﬁll this hole in the literature in this paper. We discuss our
motivations and goals in detail in Sections 1.2 and 1.3 respectively.
Department of Mathematics, The University of Oslo, P.O. Box 1053, Blindern N-0316
School of Mathematics, University of Leeds & Dept. of Mathematics, TU Darmstadt
E-mail addresses: dnormann@math.uio.no, sasander@me.com.
1The collected works of Pincherle contain a footnote by the editors (See [72, p. 67]) which
states that the associated Teorema (published in 1882) corresponds to the Heine-Borel theorem.
Moreover, Weierstrass proves the Heine-Borel theorem (without explicitly formulating it) in 1880
in [101, p. 204]. A detailed motivation for these claims may be found in [52, p. 96-97].


## Page 2


2
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
As it tuns out, the hubris of reducing the uncountable to the ﬁnite/countable as
in the Cousin and Lindel¨of lemmas, comes at great logical and computational cost.
Indeed, we establish below that these lemmas are extremely hard to prove, while
the sub-covers from these lemmas are similarly hard to compute. Now, ‘hardness
of proof’ is measured by what comprehension2 axioms are necessary to prove the
theorem. In this sense, a proof of the Cousin and Lindel¨of lemmas requires (com-
prehension axioms as strong as) second-order arithmetic, as is clear from Figure 1,
where the latter originates from Hilbert-Bernays’ Grundlagen der Mathematik [36].
Moreover, the Cousin and Lindel¨of lemmas are not isolated events: we provide
a list of basic theorems (See Section 1.3) with the same ‘extreme’ logical and com-
putational properties. Some of the listed theorems are even of great conceptual
importance as they pertain to the gauge integral ([6]), which provides a general-
isation of the Lebesgue and improper Riemann integrals, and (to the best of our
knowledge) the only direct formalisation of the Feynman path integral ([13,59,60]).
By way of catharsis, our results call into question various empirical claims from
the foundation of mathematics, such as the ‘Big Five’ classiﬁcation from Reverse
Mathematics (See Section 2.1) and the linear nature of the G¨odel hierarchy (See
Section 2.2).
Nonetheless, we obtain in Section 3.3 Reverse Mathematics style
equivalences involving the Cousin lemma and basic properties of the gauge integral.
Finally, Reverse Mathematics is intimately connected to classical computability
theory (See e.g. [91, II.7.5]); similarly, our results have an (almost) equivalent refor-
mulation in higher-order computability theory, and are even (often) obtained via
the latter. Furthermore, in light of this correspondence, we investigate in Section 4.1
the strength of the Cousin and Lindel¨of lemmas when combined with fundamental
objects from computability theory. This study yields surprising results reaching all
the way up to Gandy’s superjump ([30]), a ‘higher-order’ version of Turing’s Halting
problem ([97]), the prototypical non-computable object.
1.2. Foundational and mathematical motivations. We discuss the motiva-
tions for this paper. Items (i) and (ii) motivate the study of mathematics beyond
the language of second-order arithmetic L2, the framework for ‘classical’ Reverse
Mathematics, while a notable consequence is provided by item (iii).
(i) The gauge integral is a generalisation of the Lebesgue and (improper) Rie-
mann integral, and formalises Feynman’s path integral (See Section 1.2.1).
The language L2 cannot accommodate (basic) gauge integration.
(ii) The foundational studies of mathematics led by Hilbert take place in a
logical framework richer than the language L2 (See Section 1.2.2). It is
natural to ask if anything is lost by restricting to L2.
(iii) The compatibility problem for Nelson’s predicative arithmetic ([67]) was
solved in the negative ([14]). We solve the compatibility problem for Weyl-
Feferman predicative mathematics in the negative (See Section 1.2.3).
As an example of how items (i) and (ii) are intimately related: the uniqueness of
the gauge integral requires (Heine-Borel) compactness for uncountable covers. The
latter compactness cannot be formulated in L2, and will be seen to have completely
diﬀerent logical and computational properties compared to the ‘countable/second-
order’ substitute, i.e. (Heine-Borel) compactness for countable covers.
2Intuitively speaking, a comprehension axiom states that the set {x ∈X : ϕ(x)} exists for all
formulas ϕ in a certain class, and with the variable x in the domain X.


## Page 3


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
3
1.2.1. Mathematical motivations. In this section, we discuss the mathematical mo-
tivations for this paper, provided by the study of the gauge integral. As will be-
come clear, the latter cannot be (directly) formulated in the language of second-
order arithmetic, yielding a measure of motivation for our adoption of Kohlenbach’s
higher-order framework involving all ﬁnite types.
First of all, the gauge integral (aka Henstock-Kurzweil integral) was introduced
around 1912 by Denjoy (in a diﬀerent form) and constitutes a simultaneous gen-
eralisation of the Lebesgue and improper Riemann integral. The gauge integral
provides (to the best of our knowledge) the only formal framework close to the
original development of the Feynman path integral ([13,59,60]), i.e. gauge integrals
are highly relevant in (the foundations of) physics. As expected, the gauge integral
can handle discontinuous functions, which were around at the time: Dirichlet dis-
cusses the characteristic function of Q around 1829 in [17], while Riemann deﬁnes
a function with countably many discontinuities in his Habilitationsschrift [44].
Secondly, since Lebesgue integration is studied in Reverse Mathematics (See
[91, X.1]), it is a natural next step to study the gauge integral.
However, this
study cannot take place in the language of second-order arithmetic for the following
reasons: on one hand (general) discontinuous functions are essential for proving
basic results of the gauge integral by Remark 3.21 and Corollary 3.24.
On the
other hand, by Theorem 3.20, the uniqueness of the gauge integral requires the
Cousin lemma ([15, p. 22]), which deals with uncountable covers, and the latter
cannot be formulated in the language of second-order arithmetic.
In conclusion, the gauge integral seems to require a logical framework richer than
second-order arithmetic. Now, this richer framework yields surprising results: the
Cousin lemma expresses compactness for uncountable open covers; this lemma turns
out to have completely diﬀerent logical and computational properties compared to
compactness restricted to countable covers as in Reverse Mathematics ([91, IV.1]).
1.2.2. Foundational motivations. We show that the foundational studies of math-
ematics led by Hilbert took place in a framework richer than second-order arith-
metic.
First of all, in his 1917-1933 lectures on the foundations of mathemat-
ics ([37]), Hilbert used a logical system involving third-order 3 Funktionfunktionen.
Ackermann’s 1924 dissertation (supervised by Hilbert) starts with an overview of
Hilbertsche Beweistheorie, i.e. Hilbertian proof theory, which explicitly includes
third-order3 parameters and the ‘epsilon’ operator.
Secondly, Hilbert and Bernays introduce4 the formal system H in [36, Supple-
ment IV], and use it to formalise parts of mathematics, again based on the ‘epsilon’
operator. Now, Hilbert and Bernays in [36, p. 495] use the epsilon operator to de-
ﬁne a certain object ξ which maps functions to functions, i.e. a third-order object.
Similarly, Feferman’s ‘µ’ operator (See Section 2.4) is deﬁned with the same name
in [36, p. 476], while the ‘ν’ operator from [36, p. 479] is only a slight variation
of the Suslin functional (See Section 2.4). Hence, one could develop large parts of
Kohlenbach’s higher-order Reverse Mathematics (See Section 2.3.2) in H.
3In the notation of this paper, to be introduced in Section 2.3.2, n + 1-th order objects (n ≥0)
correspond to objects of type n.
4All other systems in [36, Suppl. IV] are either a variation of H or more limited than H.


## Page 4


4
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
Thirdly, Simpson positions Reverse Mathematics (See Section 2.1) in [91, p. 6]
as a continuation of Hilbert-Bernays’ research, namely as follows:
The development of a portion of ordinary mathematics within [second-
order arithmetic] Z2 is outlined in Supplement IV of Hilbert/Bernays
[. . . ]. The present book may be regarded as a continuation of the
research begun by Hilbert and Bernays.
In conclusion, the foundational studies of Hilbert-Bernays-Ackermann take place in
a language richer than L2, and it is a natural foundational question if anything is
lost by restricting to the latter. By Theorem 3.1, the loss can be extreme: in terms
of comprehension axioms, a proof of the Cousin lemma requires a system as strong
as second-order arithmetic, while this lemma restricted to countable covers/the lan-
guage of second-order arithmetic is provable in a weak system by [91, IV.1].
1.2.3. Foundational consequences. We discuss the compatibility problem for pred-
icative mathematics `a la Weyl-Fefermann. As it turns out, our results solve this
problem in the negative, providing another motivation for this paper.
Russell famously identiﬁed an inconsistency in early set theory, known as Rus-
sel’s paradox, based on the ‘set of all sets’ ([98]). According to Russel, the source
of this paradox was circular reasoning: in deﬁning the ‘set of all sets’, one quanti-
ﬁes over all sets, including the one that is being deﬁned. To avoid such problems,
Russel suggested banning any impredicative deﬁnition, i.e. a deﬁnition in which one
quantiﬁes over the object being deﬁned. The textbook example of an impredicative
deﬁnition is the supremum of a bounded set of reals, deﬁned as the least upper
bound of that set. Weyl, a student of Hilbert, initiated the development of pred-
icative mathematics ([102]), i.e. avoiding impredicative deﬁnitions, which Feferman
continued ([22–24]). Finally, the fourth ‘Big Five’ system of Reverse Mathematics
is considered the ‘upper limit’ of predicative mathematics (See [91, §I.12]).
In an (similar but much more strict) eﬀort to develop mathematics based on
a predicative notion of number, Nelson introduced predicative arithmetic ([67]).
Unfortunately, predicative arithmetic suﬀers from the compatibility problem: If two
theorems A, B are both acceptable from the point of view of predicative arithmetic,
it is possible that A ∧B is not ([14]). In this light, the development of predicative
arithmetic seems somewhat arbitrary. It is then a natural question whether Weyl-
Feferman predicative mathematics suﬀers from the same compatibility problem.
We show that this is the case in Section 4.1. A detailed discussion, also explaining
our notion ‘acceptable in predicative mathematics’, may be found in Remark 4.18.
1.3. Overview of main results. Our main result is that, in terms of the usual
scale of comprehension axioms, a proof of the Cousin and Lindel¨of lemmas requires
a system as strong as second-order arithmetic. The same result for the other theo-
rems in Remark 1.1 follows from our main result, as discussed in Section 3.2.2. A
precise statement of our results is found at the end of this section.
Remark 1.1 (Basic theorems).
(i) Cousin lemma: any open cover of [0, 1] has a ﬁnite sub-cover ([15]).
(ii) Lindel¨of lemma: any open cover of R has a countable sub-cover ([50]).
(iii) Besicovitsch and Vitali covering lemmas as in e.g. [1, §2].
(iv) Basic properties of the gauge integral ([6]), like uniqueness, Hake’s theorem,
and extension of the Riemann integral.


## Page 5


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
5
(v) Neighbourhood Function Principle NFP ([96, p. 215]).
(vi) The existence of Lebesgue numbers for any open cover ([32]).
(vii) The Banach-Alaoglu theorem for any open cover ([91, X.2.4], [11, p. 140]).
(viii) The Heine-Young and Lusin-Young theorems, the tile theorem [38, 104],
and the latter’s generalisation due to Rademacher ([74, p. 190]).
(ix) The Bolzano-Weierstrass, Dini, and Arzel`a theorems for nets ([43,58]).
According to Bourbaki’s historical note in [10, Ch. I], the by far most impor-
tant ‘acquisition’ of Schoenﬂies’ monograph [87] is a theorem which constitutes a
generalisation of the Cousin lemma. Another historical note is that Cousin (and
Lindel¨of in [50, p. 698]) talks about (uncountable) covers on [15, p. 22] as follows:
if for each s ∈S there is a circle of ﬁnite non-zero radius with s as center
(1.1)
In particular, any f : S →R+ gives rise to a cover in the sense of the previous
quote by Cousin as follows: ∪x∈S(x −f(x), x + f(x)) covers S ⊂R. A rich history
notwithstanding, the Cousin lemma does not show its age: there are recent attempts
to develop elementary real analysis with this lemma as the ‘centerpiece’ ([94,95]).
We now make our main results precise, for which some deﬁnitions are needed.
Detailed deﬁnitions may be found in Sections 2.3 and 2.4.
Deﬁnition 1.2. Let Z2 be second-order arithmetic as deﬁned in [91, I.2.4] and let
Π1
k-CA0 be the fragment of Z2 with comprehension restricted to Π1
k-formulas.
As noted above, to formulate the theorems from the list, we require a richer
language than that of Z2. We shall make use of RCAω
0 , Kohlenbach’s ‘base theory’
of higher-order Reverse Mathematics ([48, §2]), and the associated language of all
ﬁnite types. We introduce this framework in detail in Section 2.3.
Deﬁnition 1.3. Let (∃3) state the existence of 3E from [7, p. 713, §12.3]; see
Section 2.4 for the exact deﬁnition. The functional 3E intuitively speaking decides
any Π1
∞-formula. Let (S2
k) similarly state the existence of a functional deciding Π1
k-
formulas. For k = 1, the subscript is omitted and (S2) is called the Suslin functional.
We deﬁne Π1
k-CAω
0 ≡RCAω
0 + (S2
k), Zω
2 := ∪kΠ1
k-CAω
0 , and ZΩ
2 ≡RCAω
0 + (∃3).
We discuss in Remark 2.8 why Deﬁnition 1.3 furnishes the ‘right’ (or at least
‘good’) higher-order analogues of the respective second-order systems.
Our main results, to be proved in Section 3, are now as follows:
(i) The Cousin and Lindel¨of lemmas are provable in ZΩ
2 plus a minimal frag-
ment of the axiom of choice.
(ii) The system Π1
k-CAω
0 (any k ≥1) cannot prove any theorem in Remark 1.1.
(iii) The Cousin lemma is equivalent to basic properties of the gauge integral in
Kohlenbach’s aforementioned framework.
We discuss the (considerable) implications for the G¨odel hierarchy in Section 2.2.
Finally, as noted above, Reverse Mathematics is intimately connected to com-
putability theory, and the same holds for our results; for instance, the functional
deﬁned by (∃3) (resp. (S2
k)) can (resp. cannot) compute, in the sense of Section 2.4,
a ﬁnite sub-cover from the Cousin lemma on input an open cover of [0, 1].
Our main results in Section 4.1 are then as follows: inspired by the aforemen-
tioned connection, we study the interaction between the theorems from the above
list and the Big Five of Reverse Mathematics given by the Suslin functional S and


## Page 6


6
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
Feferman’s search functional µ from Section 2.4. This leads to surprising results in
(higher-order) Reverse Mathematics, as follows:
(1) The combination of the Cousin lemma and Feferman’s µ yields transﬁnite
recursion for arithmetical formulas, i.e. the fourth Big Five system. We
derive novel theorems about Borel functions from this result.
(2) The combination of the Cousin lemma and the Suslin functional S yields
Gandy’s superjump, the aforementioned ‘higher-order’ Halting problem.
(3) The combination of the Lindel¨of lemma for Baire space (resp. a realiser for
the latter) and Feferman’s µ yields Π1
1-CA0 (resp. the Suslin functional).
As will become clear in Section 4.1.2, the third item solves the compatibility problem
of Weyl-Feferman predicativist mathematics from Section 1.2.3 in the negative. We
also point out that the Lindel¨of lemma (resp. the Cousin lemma) and Feferman’s
µ are rather weak in isolation, and only become strong when combined.
2. Preliminaries
We sketch the program Reverse Mathematics in Section 2.1, discuss the associ-
ated G¨odel hierarchy in Section 2.2, and introduce second-order and higher-order
arithmetic in Section 2.3. As our main results are proved using techniques from
computability theory, we discuss some essential elements of the latter in Section 2.4.
2.1. Introducing Reverse Mathematics. Reverse Mathematics (RM) is a pro-
gram in the foundations of mathematics initiated around 1975 by Friedman ([26,27])
and developed extensively by Simpson ([91]) and others. We refer to [91] for an
overview of RM and introduce the required deﬁnitions (like the ‘base theory’ RCA0)
in Section 2.3.1; we now sketch some of the aspects of RM essential to this paper.
The aim of RM is to ﬁnd the axioms necessary to prove a statement of ordinary,
i.e. non-set theoretical, mathematics. The classical base theory RCA0 of ‘computable
mathematics’, introduced in Section 2.3.1, is always assumed. Thus, the aim is:
The aim of RM is to ﬁnd the minimal axioms A such that RCA0
proves [A →T ] for statements T of ordinary mathematics.
Surprisingly, once the minimal A are known, we almost always also have RCA0 ⊢
[A ↔T ], i.e. we derive the theorem T from the axioms A (the ‘usual’ way of doing
mathematics), but we can also derive the axiom A from the theorem T (the ‘reverse’
way). In light of these ‘reversals’, the ﬁeld was baptised ‘Reverse Mathematics’.
Perhaps even more surprisingly, in the majority of cases, for a statement T of
ordinary mathematics, either T is provable in RCA0, or the latter proves T ↔Ai,
where Ai is one of the logical systems WKL0, ACA0, ATR0 or Π1
1-CA0, which are
all introduced in Section 2.3.1. The latter four together with RCA0 form the ‘Big
Five’ and the aforementioned observation that most mathematical theorems fall into
one of the Big Five categories, is called the Big Five phenomenon ([54, p. 432]).
Furthermore, each of the Big Five has a natural formulation in terms of (Turing)
computability (See [91, I]). As noted by Simpson in [91, I.12], each of the Big Five
also corresponds (sometimes loosely) to a foundational program in mathematics.
Finally, we note that the Big Five systems of RM yield a linear order:
Π1
1-CA0 →ATR0 →ACA0 →WKL0 →RCA0.
(2.1)
By contrast, there are many incomparable logical statements in second-order arith-
metic. For instance, a regular plethora of such statements may be found in the


## Page 7


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
7
Reverse Mathematics zoo in [21]. The latter is intended as a collection of (some-
what natural) theorems outside of the Big Five classiﬁcation of RM.
2.2. Reverse Mathematics and the G¨odel hierarchy. The G¨odel hierarchy is
a collection of logical systems ordered via consistency strength or (essentially equiv-
alent) inclusion5. This hierarchy is claimed by Simpson to capture most systems
that are natural and/or have foundational import, as follows.
It is striking that a great many foundational theories are linearly
ordered by <. Of course it is possible to construct pairs of artiﬁcial
theories which are incomparable under <. However, this is not the
case for the “natural” or non-artiﬁcial theories which are usually
regarded as signiﬁcant in the foundations of mathematics. ([92])
Burgess and Koelner make essentially the same claims in [12, §1.5] and [45, 46].
However, our results imply that the theorems in Remark 1.1 do not ﬁt the G¨odel
hierarchy (with the latter based on inclusion5). In particular, we obtain a branch
that is independent of the medium range of the G¨odel hierarchy, depicted below.
strong





























...
supercompact cardinal
...
measurable cardinal
...
ZFC
ZC
simple type theory
ZΩ
2 + QF-AC0,1
medium

















Zω
2 ≡∪kΠ1
k-CAω
0
...
Π1
2-CAω
0
Π1
1-CAω
0
ATRω
0
ACAω
0

Cousin and Lindel¨of lemmas
basic prop. of gauge integral

weak











WKLω
0
RCAω
0
PRA
EFA
bounded arithmetic
Figure 1. The G¨odel hierarchy with a side-branch for the medium range
✑
✑
✑
✑
✑
✑
✑
✑
✑
✑
✑
✑
✑
✰
✑
✑
✑
✑
✑
✑
✰
✲
✑✑✑✑✑
✸
❜
❜
5Simpson claims in [92, p. 112] that inclusion and consistency strength yield the same (G¨odel)
hierarchy as depicted in [92, Table 1], i.e. this choice does not matter.


## Page 8


8
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
Arguably, the G¨odel hierarchy is a central object of study in mathematical logic,
as e.g. stated by Simpson in [92, p. 112] or Burgess in [12, p. 40]. Some remarks on
the technical details concerning Figure 1 are as follows.
(1) Note that we use a non-essential modiﬁcation of the G¨odel hierarchy,
namely involving systems of higher-order arithmetic, like e.g. ACAω
0 instead
of ACA0; these systems are (at least) Π1
2-conservative over the associated
second-order system (See e.g. [81, Theorem 2.2]).
(2) In the spirit of RM, we show in [71] that the Cousin lemma and (a version
of) the Lindel¨of lemma are provable without the use of QF-AC0,1, as also
discussed in Remark 3.16.
(3) The system ZΩ
2 is placed between the medium and strong range, as the
combination of the recursor R2 from G¨odel’s T and ∃3 yields a system
stronger than ZΩ
2 . The system Π1
k-CAω
0 is more robust in this sense.
(4) Despite Simpson’s grand claim in the above quote, there are now some
examples of logical systems that fall outside of the G¨odel hierarchy, like
special cases of Ramsey’s theorem and the axiom of determinacy ([39,53]).
Finally, in light of the equivalences involving the gauge integral and the Cousin
lemma (See Section 3.3), the latter seriously challenges the ‘Big Five’ classiﬁcation
from RM, the linear nature of the G¨odel hierarchy, as well as Feferman’s claim
that the mathematics necessary for the development of physics can be formalised
in relatively weak logical systems (See Remark 3.29 for the latter claim).
2.3. The framework of Reverse Mathematics. We introduce axiomatic sys-
tems essential to RM. We start with a sketch of second-order arithmetic (See
[91, I.2.4]), the framework of Friedman-Simpson RM, and ﬁnish with higher-order
artihmetic, the framework of Kohlenbach’s higher-order RM (See [48]).
2.3.1. Second-order arithmetic and fragments. The language L2 of second-order
arithmetic Z2 has two sorts of variables: number variables n, m, k, l, . . . intended
to range over the natural numbers, and set variables X, Y, Z, . . . intended to range
over sets of natural numbers. The constants of L2 are 0, 1, <N, +N, ×N, =N and ∈,
which are intended to have their usual meaning (by the axioms introduced below).
Formulas and terms are built up from these constants in the usual way.
Deﬁnition 2.1. Second-order arithmetic Z2 consists of three axiom schemas:
(1) Basic axioms expressing that 0, 1, <N, +N, ×N form an ordered semi-ring
with equality =N.
(2) Induction: For any X,
 0 ∈X∧(∀n)(n ∈X →n+1 ∈X)

→(∀n)(n ∈X).
(3) Comprehension: For any formula ϕ(n) of L2 which does not involve the
variable X, we have (∃X)(∀n)(n ∈X ↔ϕ(n)).
Induction is well-known, while comprehension intuitively expresses that any L2-
formula ϕ(n) yields a set X = {n ∈N : ϕ(n)} consisting of exactly those numbers
n ∈N satisfying ϕ(n). Now, fragments of Z2 are obtained by restricting compre-
hension (and induction), for which the following deﬁnition is needed.
Deﬁnition 2.2. [Formula classes]
(1) A formula of L2 is quantiﬁer-free (Σ0
0 or Π0
0) if it does not involve quantiﬁers.
To be clear: variables are allowed; only quantiﬁers are banned.


## Page 9


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
9
(2) A formula of L2 is arithmetical (Σ1
0 or Π1
0) if it only involves quantiﬁers over
number variables, i.e. set quantiﬁers like (∃X) and (∀Y ) are not allowed.
(3) An arithmetical formula is Σ0
k+1 (resp. Π0
k+1) if it has the form (∃n)ϕ(n)
(resp. (∀n)ϕ(n)) with ϕ in Π0
k (resp. in Σ0
k).
(4) A formula of L2 is Σ1
k+1 (resp. Π1
k+1) if it has the form (∃X)ϕ(X) (resp.
(∀X)ϕ(X)) with ϕ in Π1
k (resp. in Σ1
k).
(5) A formula of L2 is ∆i
k+1 if it is both Πi
k+1 and Σi
k+1 for i = 0, 1.
Intuitively, a Σ0
k-formula is a quantiﬁer-free formula pre-ﬁxed by k alternating
number quantiﬁers, starting with an existential one; a Σ1
k-formula is an arithmetical
formula pre-ﬁxed by k alternating set quantiﬁers, starting with an existential one.
The Π-formulas are (equivalent to) negations of the corresponding Σ-versions.
Using the above, the third and ﬁfth ‘Big Five’ systems ACA0 and Π1
1-CA0 are
just Z2 with comprehension restricted to resp. arithmetical and Π1
1-formulas. Al-
ternatively, ACA0 allows one to build sets using ﬁnite iterations of Turing’s Halting
problem ([97]), aka the Turing jump; intuitively, ATR0 extends this to transﬁnite
recursion, i.e. the unbounded iteration of the Turing jump along any countable
well-ordering. Furthermore, the ‘base theory’ RCA0 is Z2 with comprehension re-
stricted to ∆0
1-formulas, plus induction for Σ0
1-formulas. As discussed in [91, II
and IX.3], ∆0
1-comprehension essentially expresses that ‘all computable sets exists’,
while Σ0
1-induction corresponds to primitive recursion in the sense of Hilbert’s ﬁni-
tistic mathematics. The system WKL0 is just RCA0 extended by the weak K¨onig’s
lemma6 (WKL hereafter) which states that an inﬁnite binary tree has a path.
Finally, in light of the previous and (2.1), the Big Five only constitute a very tiny
fragment of Z2; on a related note, the RM of topology does give rise to theorems
equivalent to Π1
2-CA0 ([61]), but that is the current upper bound of RM to the best
of our knowledge. In particular, if Π1
k-CA0 is Z2 restricted to Π1
k-comprehension,
then this system can be said to ‘go beyond Friedman-Simpson RM’ for k ≥3.
2.3.2. Higher-order arithmetic and fragments. As suggested by its name, higher-
order arithmetic extends second-order arithmetic. Indeed, while the latter is re-
stricted to numbers and sets of numbers, higher-order arithmetic also has sets of
sets of numbers, sets of sets of sets of numbers, et cetera. To formalise this idea,
we introduce the collection of all ﬁnite types T, deﬁned by the two clauses:
(i) 0 ∈T and (ii) If σ, τ ∈T then (σ →τ) ∈T,
where 0 is the type of natural numbers, and σ →τ is the type of mappings from
objects of type σ to objects of type τ. In this way, 1 ≡0 →0 is the type of functions
from numbers to numbers, and where n + 1 ≡n →0. Viewing sets as given by
their characteristic function, we note that Z2 only includes objects of type 0 and 1.
The language of Lω consists of variables xρ, yρ, zρ, . . . of any ﬁnite type ρ ∈T.
Types may be omitted when they can be inferred from context. The constants of
Lω includes the type 0 objects 0, 1 and <0, +0, ×0, =0 which are intended to have
the same meaning as their N-subscript counterparts in Z2. Equality at higher types
is deﬁned in terms of ‘=0’ as follows: for any objects xτ, yτ, we have
[x =τ y] ≡(∀zτ1
1 . . . zτk
k )[xz1 . . . zk =0 yz1 . . . zk],
(2.2)
6To be absolutely clear, we take ‘WKL’ to be the L2-sentence every inﬁnite binary tree has a
path as in [91], while the Big Five system WKL0 is RCA0 + WKL, and WKLω
0 is RCAω
0 + WKL.


## Page 10


10
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
if the type τ is composed as τ ≡(τ1 →. . . →τk →0). Furthermore, Lω also
includes the recursor constant Rσ for any σ ∈T, which allows for iteration on type
σ-objects as in the special case (2.3). Formulas and terms are deﬁned as usual.
Deﬁnition 2.3. The base theory RCAω
0 consists of the following axioms:
(1) Basic axioms expressing that 0, 1, <0, +0, ×0 form an ordered semi-ring with
equality =0.
(2) Basic axioms deﬁning the well-known Π and Σ combinators (aka K and S
in [2]), which allow for the deﬁnition of λ-abstraction.
(3) The deﬁning axiom of the recursor constant R0: For m0 and f 1:
R0(f, m, 0) := m and R0(f, m, n + 1) := f(R0(f, m, n)).
(2.3)
(4) The axiom of extensionality: for all ρ, τ ∈T, we have:
(∀xρ, yρ, ϕρ→τ)

x =ρ y →ϕ(x) =τ ϕ(y)

.
(Eρ,τ)
(5) The induction axiom for quantiﬁer-free7 formulas.
(6) QF-AC1,0: The quantiﬁer-free axiom of choice as in Deﬁnition 2.4.
Deﬁnition 2.4. The axiom QF-AC consists of the following for all σ, τ ∈T:
(∀xσ)(∃yτ)A(x, y) →(∃Y σ→τ)(∀xσ)A(x, Y (x))
(QF-ACσ,τ)
for any quantiﬁer-free formula A in the language of Lω.
As discussed in [48, §2], RCAω
0 and RCA0 prove the same sentences ‘up to lan-
guage’ as the latter is set-based and the former function-based.
Furthermore, recursion as in (2.3) is called primitive recursion; the class of func-
tionals obtained from Rρ for all ρ ∈T is called G¨odel’s system T of all (higher-
order) primitive recursive functionals.
We use the usual notations for natural, rational, and real numbers, and the
associated functions, as introduced in [48, p. 288-289].
Deﬁnition 2.5 (Real numbers and related notions in RCAω
0 ).
(i) Natural numbers correspond to type zero objects, and we use ‘n0’ and
‘n ∈N’ interchangeably. Rational numbers are deﬁned as signed quotients
of natural numbers, and ‘q ∈Q’ and ‘<Q’ have their usual meaning.
(ii) Real numbers are coded by fast-converging Cauchy sequences q(·) : N →Q,
i.e. such that (∀n0, i0)(|qn −qn+i)| <Q
1
2n ).
We use Kohlenbach’s ‘hat
function’ from [48, p. 289] to guarantee that every f 1 deﬁnes a real number.
(iii) We write ‘x ∈R’ to express that x1 := (q1
(·)) represents a real as in the
previous item and write [x](k) := qk for the k-th approximation of x.
(iv) Two reals x, y represented by q(·) and r(·) are equal, denoted x =R y, if
(∀n0)(|qn −rn| ≤
1
2n−1 ). Inequality ‘<R’ is deﬁned similarly.
(v) Functions F : R →R mapping reals to reals are represented by Φ1→1
mapping equal reals to equal reals, i.e. (∀x, y)(x =R y →Φ(x) =R Φ(y)).
(vi) The relation ‘x ≤τ y’ is deﬁned as in (2.2) but with ‘≤0’ instead of ‘=0’.
(vii) Sets of type ρ objects Xρ→0, Y ρ→0, . . . are given by their characteristic
functions f ρ→0
X
, i.e. (∀xρ)[x ∈X ↔fX(x) =0 1], where f ρ→0
X
≤ρ→0 1.
7To be absolutely clear, similar to Deﬁnition 2.2, variables (of any ﬁnite type) are allowed in
quantiﬁer-free formulas: only quantiﬁers are banned.


## Page 11


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
11
We sometimes omit the subscript ‘R’ if it is clear from context. We also introduce
some notation to handle ﬁnite sequences nicely.
Notation 2.6 (Finite sequences). We assume a dedicated type for ‘ﬁnite sequences
of objects of type ρ’, namely ρ∗. Since the usual coding of pairs of numbers goes
through in RCAω
0 , we shall not always distinguish between 0 and 0∗. Similarly, we
do not always distinguish between ‘sρ’ and ‘⟨sρ⟩’, where the former is ‘the object
s of type ρ’, and the latter is ‘the sequence of type ρ∗with only element sρ’. The
empty sequence for the type ρ∗is denoted by ‘⟨⟩ρ’, usually with the typing omitted.
Furthermore, we denote by ‘|s| = n’ the length of the ﬁnite sequence sρ∗=
⟨sρ
0, sρ
1, . . . , sρ
n−1⟩, where |⟨⟩| = 0, i.e. the empty sequence has length zero.
For
sequences sρ∗, tρ∗, we denote by ‘s∗t’ the concatenation of s and t, i.e. (s∗t)(i) = s(i)
for i < |s| and (s∗t)(j) = t(|s|−j) for |s| ≤j < |s|+|t|. For a sequence sρ∗, we deﬁne
sN := ⟨s(0), s(1), . . . , s(N −1)⟩for N 0 < |s|. For a sequence α0→ρ, we also write
αN = ⟨α(0), α(1), . . . , α(N−1)⟩for any N 0. By way of shorthand, (∀qρ ∈Qρ∗)A(q)
abbreviates (∀i0 < |Q|)A(Q(i)), which is (equivalent to) quantiﬁer-free if A is.
2.4. Higher-order computability theory. As noted above, our main results
will be proved using techniques from computability theory. Thus, we ﬁrst make our
notion of ‘computability’ precise as follows.
(I) We adopt ZFC, i.e. Zermelo-Fraenkel set theory with the Axiom of Choice,
as the oﬃcial metatheory for all results, unless explicitly stated otherwise.
(II) We adopt Kleene’s notion of higher-order computation as given by his nine
clauses S1-S9 (See [51,80]) as our oﬃcial notion of ‘computable’.
For the rest of this section, we introduce some existing functionals which will be
used below. These functionals constitute the counterparts of Z2, and some of the
Big Five systems, in higher-order RM. First of all, ACA0 is readily derived from:
(∃µ2)

(∀f 1)((∃n)(f(n) = 0) →f(µ(f)) = 0)

,
(µ2)
and ACAω
0 ≡RCAω
0 + (µ2) proves the same Π1
2-sentences as ACA0 by [81, Theo-
rem 2.2]. The functional µ2 in (µ2) is also called Feferman’s µ ([2]), and is clearly
discontinuous at f =1 11 . . . ; in fact, (µ2) is equivalent to the existence of F : R →R
such that F(x) = 1 if x >R 0, and 0 otherwise ([48, §3]).
Secondly, Π1
1-CA0 is readily derived from the following sentence:
(∃S2 ≤2 1)(∀f 1)

(∃g1)(∀x0)(f(gn) = 0) ↔S(f) = 0

,
(S2)
and Π1
1-CAω
0 ≡RCAω
0 + (S2) proves the same Π1
3-sentences as Π1
1-CA0 by [81, The-
orem 2.2]. The functional S2 in (S2) is also called the Suslin functional ([48]).
By deﬁnition, the Suslin functional S2 can decide whether a Σ1
1-formula (as in the
left-hand side of (S2)) is true or false. We similarly deﬁne the functional S2
k which
decides the truth or falsity of Σ1
k-formulas; we also deﬁne the system Π1
k-CAω
0 as
RCAω
0 + (S2
k), where (S2
k) expresses that the functional S2
k exists.
Thirdly, full second-order arithmetic Z2 is readily derived from the sentence:
(∃E3 ≤3 1)(∀Y 2)

(∃f 1)Y (f) = 0 ↔E(Y ) = 0

,
(∃3)
and we deﬁne ZΩ
2 ≡RCAω
0 + (∃3), which is a conservative extension of Z2 by
[41, Cor. 2.6]. The (unique) functional from (∃3) is also called ‘∃3’, and we will use
a similar convention for other functionals.


## Page 12


12
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
Fourth, there is primitive recursive function U such that ‘U(e, k, n) =0 m + 1’
expresses that the e-th Turing machine with input k halts after n steps with output
m. By deﬁnition, Feferman’s µ2 provides an upper bound on this n if it exists, i.e.
we can use µ2 to solve the Halting problem. Similarly, Gandy’s superjump solves
the Halting problem for higher-order computability as follows:
S(F 2, e0) :=
(
0
if {e}(F) terminates
1
otherwise
,
(S3)
where e is an S1-S9-index. A characterisation of S in terms of discontinuities may be
found in [34]. Clearly, the above functionals are natural counterparts of (set-based)
comprehension axioms in a functional-based language.
Fifth, recall that the Cousin lemma from Remark 1.1 states the existence of
a ﬁnite sub-cover for an open cover of the unit interval.
Since Cantor space is
homeomorphic to a closed subset of [0, 1], the former inherits the same property. In
particular, for any G2, the corresponding ‘canonical cover’ of 2N is ∪f∈2N[fG(f)]
where [σ0∗] is the set of all binary extensions of σ.
By compactness, there is
a ﬁnite sequence ⟨f0, . . . , fn⟩such that the set of ∪i≤n[ ¯fiG(fi)] still covers 2N.
We now introduce the speciﬁcation SCF(Θ) for a (non-unique) functional Θ which
computes such a ﬁnite sequence. We refer to such a functional Θ as a realiser for
the compactness of Cantor space, and simplify its type to ‘3’ to improve readability.
Deﬁnition 2.7. The formula SCF(Θ) is as follows for Θ2→1∗:
(∀G2)(∀f 1 ≤1 1)(∃g ∈Θ(G))(f ∈[gG(g)]).
(2.4)
where ‘f ∈[gG(g)]’ is the quantiﬁer-free formula fG(g) =0∗gG(g).
Clearly, there is no unique Θ as in (2.4) (just add more binary sequences to
Θ(G)); nonetheless, we have in the past referred to any Θ satisfying SCF(Θ) as
‘the’ special fan functional Θ, and we will continue this abuse of language. We
shall however repeatedly point out the non-unique nature of the special fan func-
tional Θ in the following.
While Θ may appear exotic at ﬁrst, it provides the
only method we can think of for computing gauge integrals in general, as discussed
in Remark 3.27. As to its provenance, Θ was introduced as part of the study of
the Gandy-Hyland functional in [82, §2] via a slightly diﬀerent deﬁnition. These
deﬁnitions are identical up to a term of G¨odel’s T of low complexity.
Finally, we should discuss why the above systems involving the ‘ω’ superscripts
are the ‘right’ (or at least ‘good’) higher-order analogues of the correspoding second-
order systems. We also discuss the special case of ZΩ
2 and second-order arithmetic.
Remark 2.8. First of all, Kohlenbach introduces RCAω
0 in [48] as the base theory
for higher-order RM and proves that it is conservative over RCA0 up to language.
Hence, it makes sense to similarly use the superscript ‘ω’ to denote the higher-order
counterparts of subsystems of second-order arithmetic Z2
Secondly, most of the aforementioned systems with superscript ‘ω’ are known
conservative extensions (for at least Π1
2-formulas) of their second-order counter-
parts. For RCAω
0 , this follows from [48, Prop. 3.1]. For ACAω
0 and Π1
1-CAω
0 , this
follows from [81, Theorem 2.2], while for Zω
2 and ZΩ
2 this follows from [41, Cor. 2.6].
Similar results for Π1
k-CAω
0 can be obtained in the same way.


## Page 13


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
13
Thirdly, as noted below Figure 1 in Section 2.2, ZΩ
2 is placed between the medium
and strong range. The motivation is that the combination of the recursor R2 from
G¨odel’s T and ∃3 yields a system stronger than ZΩ
2 . On the other hand, the system
Zω
2 does not suﬀer from this problem, and we therefore believe that the latter is the
‘right’ higher-order analogue of second-order arithmetic Z2.
3. Main results I
We establish our main results as sketched in Section 1.3. We treat the Cousin
lemma in full detail in Section 3.1, while similar ‘covering theorems’ from Re-
mark 1.1 are treated analogously in Section 3.2. We show in Section 3.3 that the
Cousin lemma is equivalent to various basic properties of the gauge integral. In
Section 3.4, we derive the Cousin lemma from the following generalisation of the
Bolzano-Weierstrass theorem: every net in the unit interval has a convergent sub-
net. Nets (aka Moore-Smith sequences) provide a generalisation of the concept of
sequences beyond countable index sets, going back a century ([57,58]).
3.1. Cousin lemma. Cousin ﬁrst proved (what is now known as) the Cousin
lemma before 1893 ([20]).
This lemma essentially expresses that I = [0, 1] is
Heine-Borel compact, i.e. that any open cover of I has a ﬁnite sub-cover. The
goal of this section is to establish that, despite its seemingly elementary nature,
the Cousin lemma can only be proved in full second-order arithmetic, as sketched
in Section 1.3. This should be contrasted with the restriction to countable covers,
which may be proved in the weak fragment WKL0 by [91, IV.1.2]).
First of all, a functional Ψ : R →R+ gives rise to the (uncountable) canonical
open cover ∪x∈IIΨ
x where IΨ
x is the open interval (x −Ψ(x), x + Ψ(x)). Hence, the
Cousin lemma implies that ∪x∈IIΨ
x has a ﬁnite sub-cover; in symbols:
(∀Ψ : R →R+)(∃⟨y1, . . . , yk⟩)(∀x ∈I)(∃i ≤k)(x ∈IΨ
yi).
(HBU)
Note that HBU makes use of the original formulation by Cousin as in (1.1). We
show in [83, §3.4] that HBU sports a certain robustness, in that its logical properties
do not depend on the exact choice of deﬁnition of cover.
The main goal of this section is to prove the following theorem, which establishes
that full second-order arithmetic is needed to prove the Cousin lemma as in HBU.
Theorem 3.1. ZΩ
2 + QF-AC0,1 proves HBU; no system Π1
k-CAω
0 proves HBU.
The ﬁrst part is a necessity as otherwise the designation “analysis” for Z2 would
be meaningless ([88, p. 291]). The second part constitutes a surprise: the restriction
of HBU to countable covers is equivalent to WKL0 ([91, IV.1]), a system with the
(ﬁrst-order) strength of RCAω
0 . Kohlenbach has introduced generalisations of WKL0
with properties similar to HBU ([47, §5-6]), but these axioms do not stem from
mathematics, i.e. are ‘purely logical’. Furthermore, HBU is robust ([54, p. 432]) in
that restricting the variable x to the (Turing) computable reals or the rationals in
I does not make a diﬀerence. We now prove the ﬁrst part of Theorem 3.1.
Theorem 3.2. The system ZΩ
2 + QF-AC0,1 proves HBU.
Proof. We only sketch the proof as it makes use of items from Remark 1.1 to be
studied in Section 3.2. A full proof may be found in Theorem 3.14. Now, to derive
HBU, we note that the Lindel¨of lemma provides a countable sub-cover for any open
cover of I.
Since (∃3) immediately implies Z2, we may use [91, IV.1.2], which


## Page 14


14
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
implies that every countable open cover has a ﬁnite sub-cover. What remains is to
prove the Lindel¨of lemma, which readily follows from the Neighbourhood function
principle NFP, i.e. item (v) in Remark 1.1, as will become clear in the proof of
Theorem 3.14. In turn, NFP has a straightforward proof in ZΩ
2 + QF-AC0,1, as will
also become clear in the proof of Theorem 3.14.
□
As noted above, we shall make use of computability theory to establish Theo-
rem 3.1. Hence, we ﬁrst show that HBU is equivalent to the existence of the special
fan functional Θ in Theorem 3.3. Theorem 3.1 will then be established by showing
that models of Π1
k-CAω
0 do not always contain Θ as in Theorem 3.4. Note that the
functional Ωas in (3.1) is called a realiser for HBU.
Theorem 3.3. ACAω
0 + QF-AC2,1 proves (∃Θ)SCF(Θ) ↔HBU ↔(3.1), where
(∃Ω2→1∗)(∀Ψ : R →R+)(∀x ∈[0, 1])(∃y ∈Ω(Ψ)(x ∈IΨ
y ).
(3.1)
Proof. We ﬁrst point out two useful properties of Feferman’s µ: the axiom (µ2)
deﬁning the latter functional is equivalent to the existence of F : R →R such that
F(x) = 1 if x >R 0, and 0 otherwise ([48, §3]). Furthermore, by repeatedly applying
µ, we can show that any arithmetical formula is equivalent to a quantiﬁer-free one.
We also recall the notation ‘f ∈[σ]’ for covers of Cantor space from Deﬁnition 2.7.
Based on the previous, given Ψ, y1, . . . , yk as in HBU, we can decide if the inter-
vals IΨ
yi form an open covering or not: we just check (using µ) how the end-points
of these intervals are interleaved. Thus, using µ as a parameter, we can deduce
(3.1) from HBU by QF-AC2,1. Likewise, given f1, . . . , fn ≤1 1 and k1, . . . , kn in N,
we can decide if the set of neighbourhoods [ ¯fiki] form a covering or not; hence, we
may use QF-AC2,1 to similarly obtain Θ from the compactness of Cantor space.
Now deﬁne ξ(f) = P
i∈N f(i) · 2−(i+1) and ζ(f) = P
i∈N 2f(i) · 3−(i+1) for f ∈
{0, 1}N; note that ξ is a continuous projection of {0, 1}N to [0, 1], while ζ is the
homeomorphism between {0, 1}N and the classical Cantor space Cc. Using ξ and
ζ, we can convert canonical covers between I and Cantor space as follows:
• For Ψ : [0, 1] →R+, deﬁne FΨ(f) as the least n such that [ ¯fn] ⊆ξ−1(IΨ
ξ(f)).
• For F : {0, 1}N →N, we deﬁne ΨF (x) as the distance from x to Cc if
x ̸∈Cc, and as the least rational (in some canonical enumeration of Q+) q
such that ζ−1((x −q, x + q)) ⊆[ζ−1(x)F(ζ−1(x))] if x ∈Cc.
These constructions are arithmetical, and the compactness property for the associ-
ated coverings are transferred from one space to the other in both directions.
□
From the proof, we may also conclude that there is a term t such that if SCF(Θ)
and Ω:= t(Θ, µ) then Ωsatisﬁes (3.1), and conversely, there is a term s such that if
Ωsatisﬁes (3.1) and Θ := s(Ω, µ), then SCF(Θ). The proof makes use of the Axiom
of Choice (as in QF-AC) to obtain a functional Θ as in SCF(Θ), resp. Ωsatisfying
(3.1), from the existence of ﬁnite sub-coverings. Nonetheless, a careful analysis of
known proofs of HBU yields such functionals Θ and Ωwithout the Axiom of Choice.
We discuss this in more detail in Remark 3.9 below. Finally, we point out that
ACAω
0 + QF-AC is also Π1
2-conservative over ACA0 by [81, Theorem 2.2].
To establish Theorem 3.1, we now exhibit a model (aka type structure) of Π1
k-CAω
0
in which there is no special fan functional and in which HBU fails; hence Π1
k-CAω
0
cannot prove HBU by the soundness theorem.


## Page 15


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
15
Theorem 3.4. There is a type structure validating Π1
k-CAω
0 (for all k), and at the
same time satisfying (∀Θ3)¬SCF(Θ) and ¬HBU.
Proof. We introduce a family of type structures validating (∀Θ3)¬SCF(Θ). The-
orem 3.8 below tells us that one of those structures contains all S1
k and is closed
under S1-S9, establishing the theorem. Intuitively speaking, we start from a β-
model A and have that any functional G : A →N which is computable in some S2
k
and elements from A will be total over NN by the same algorithm. By absoluteness,
there are f1, . . . , fn in A inducing a covering of 2N of the standard form. Since it is
ﬂexible which objects of type 2 we include in an extension of A to a typed structure,
A together with the S2
k’s cannot “decide” whether there is Θ as in SCF(Θ).
Let A ⊆NN be a countable set such that all Π1
k-statements with parameters from
A are absolute for A. Also, let S2
k be the characteristic function of a complete Π1
k-
set for each k; we also write S2
k for the restriction of this functional to A. Clearly,
for f ∈NN computable in any S2
k and some f1, . . . , fn from A, f is also in A.
Convention 3.5. Since A is countable, we write A as the increasing union S
k∈N An
where A0 consists of the hyperarithmetical functions and for k > 0 we have:
• There is an element in Ak enumerating Ak−1.
• Ak is the closure of a ﬁnite set g1, . . . , gnk under computability in S2
k.
For the sake of uniform terminology, we rename ∃2 to S2
0 and let the associated
ﬁnite sequence g1, . . . , gn0 be the empty list.
We now deﬁne the functional F 2 on A as follows.
Deﬁnition 3.6. [The functional F] Deﬁne F(f) for f ∈A as follows:
• If f ̸∈2N, put F(f) := 0.
• If f ∈2N, let k be minimal such that f ∈Ak. We put F(f) := 2−(k+2+e).
where e is a ‘minimal’ index for computing f from S2
k and {g1, . . . , gnk}
as follows: the ordinal rank of this computation of f is minimal and e is
minimal among the indices for f of the same ordinal rank.
By deﬁnition, F as in Deﬁnition 3.6 is injective on A0 and on each set Ak+1 \Ak.
Moreover, if m is the usual measure on 2N, we see that
m
  S
f∈A0[ ¯fF(f)]

≤2−1 and m
  S
f∈Ak+1\Ak[ ¯fF(f)]

≤2−(k+2).
(3.2)
As a consequence, if F is extended to a total functional G and Θ satisﬁes SCF(Θ),
then Θ(G) cannot be a ﬁnite list from A. Similarly, a ﬁnite sequence ⟨f1, . . . , fn⟩in
A is already in some ∪k≤mAk, and (3.2) implies that ∪i≤n[fiG(fi)] does not cover
Cantor space, for any total extension G of F.
Thus, for any type structure Tp = {Tpn}n∈N where Tp0 = N, Tp1 = A and
F ∈Tp2, there is no instance of Θ as in SCF(Θ) in Tp3. To establish the theorem,
we require one such type structure, containing each S2
k and F, and closed under
Kleene’s S1-S9; such a type structure is provided by Theorem 3.8, i.e. the latter
establishes the theorem, and we are done.
□
For Theorem 3.8, we require some properties of F 2 from Deﬁnition 3.6.
Lemma 3.7 (Properties of the functional F).
(1) For each k, the restriction of F to Ak is computable in the functions
g1, . . . , gnk from Convention 3.5, and the functional S2
k.


## Page 16


16
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
(2) Let G be any total extension of F, let f1, . . . , fm ∈A, and assume that the
function f is computable in G, f1, . . . , fm and some S2
k. Then also f ∈A.
Proof. For the ﬁrst part, we use induction on k. For k = 0, we use Gandy se-
lection ([51, p. 210]) for ∃2 which permits us to compute an ∃2 index for each
hyperarithmetical function. For k > 0, we use that S2
l is computable in S2
k when
l < k and that we have enumerations of each of the sets A0, . . . , Ak−1 computable
in g1, . . . , gnk and S2
k. Then we can apply the induction hypothesis for f ∈Al for
some l < k and the Gandy selection method relative to S2
k for f ∈Ak \ Ak−1. For
the second part, without loss of generality, we may assume that f1, . . . , fm are all
in Ak. By the ﬁrst part of this lemma, G restricted to Ak is computable in S2
k, and
Ak is closed under computations relative to S2
k. The claim now follows.
□
Theorem 3.8. There is a type structure {Tpn}n∈N, closed under Kleene’s S1-S9,
such that Tp0 = N and:
(1) Tp1 is a countable subset A of NN such that all analytical statements (i.e.
any Π1
m-sentence, for any m) are absolute for A.
(2) Tp2 contains the restrictions of all S2
k to A.
(3) There exists F ∈Tp2 inducing an open covering of A for which there is no
ﬁnite sub-covering in the type structure.
Proof. The theorem expresses exactly what Tpn has to be for n = 0 and n = 1. For
n > 1, we recursively let Tpn consist of all functionals φ : Tpn−1 →N that are S1-
S9-computable in F, some S2
k, and elements from A, where F is as in Deﬁnition 3.6.
This type structure has the desired property. Note that Feferman’s µ is S1-S9-
computable from ∃2, and the former immediately yields QF-AC1,0.
□
The proof of Theorem 3.1 is now done. As to the role of QF-AC0,1, we show in
[71, §4] that HBU is provable in ZΩ
2 , i.e. without QF-AC0,1, as well as the construction
of a type structure of Π1
k-CAω
0 + QF-AC0,1 in which ¬HBU holds. Thus, QF-AC0,1
is not essential for obtaining HBU. We ﬁnish this section with a remark.
Remark 3.9 (The Axiom of Choice and Θ). First of all, the (quantiﬁer-free)
Axiom of Choice is used to establish the existence of Θ in Theorem 3.3, while by
[84, Cor. 3.29], Θ can be computed (via a term from G¨odel’s T ) from a version of ∃3
enriched with quantiﬁer-free choice. However, Borel’s construction from [9, p. 52]
can be applied to our notion of canonical cover, yielding a countable sub-cover
without using the Axiom of Choice. Furthermore, the instance Θ0 of the special
fan functional from [69, §5.1] is deﬁned using Borel’s construction.
3.2. Lindel¨of lemma and similar theorems. We establish results analogous to
Theorem 3.1 for some of the other theorems from Remark 1.1. We discuss how
these theorems are used in mathematics in Remark 3.17.
3.2.1. Lindel¨of lemma. We recall that Lindel¨of proved the Lindel¨of lemma in 1903
([50]), while Young and Riesz proved a similar theorem in 1902 and 1905 ([79,103]);
this lemma expresses that any open cover of any subset of Rn has a countable sub-
cover.
We study variations of this lemma restricted to R, while Baire space is
studied in Section 4.1.2. We believe LIND is the closest to Lindel¨of’s original8.
8Lindel¨of formulates his lemma in [50, p. 698] as follows: Soit (P) un ensemble quelconque
situ´e dans l’espace Rn et, de chaque point P comme centre, construisons une sph`ere SP d’un
rayon ρP qui peut varier de l’un point `a l’autre; il existe une inﬁnit´e d´enombrable de ces sph`eres


## Page 17


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
17
Deﬁnition 3.10. [LIND] For every Ψ : R →R+, there is a sequence of open
intervals ∪n∈N(an, bn) covering R such that (∀n ∈N)(∃x ∈R)[(an, bn) = IΨ
x ].
Deﬁnition 3.11. [LIND2] (∀Ψ : R →R+)(∃Φ0→1)(∀x ∈R)(∃n0)(x ∈IΨ
Φ(n)).
Deﬁnition 3.12. [LIND3] (∃Ξ)(∀Ψ : R →R+)(∀x ∈R)(∃n0)(x ∈IΨ
Ξ(Ψ)(n)).
The following theorem establishes the connection between LIND and HBU, while
also showing that the introduction of Ξ or Φ does not change LIND much.
Theorem 3.13. The system RCAω
0 + QF-AC0,1 proves [LIND + WKL] ↔HBU and
ACAω
0 + QF-AC0,1 proves LIND ↔LIND2 ↔LIND3.
Proof. For the ﬁrst part, WKL0 implies that every countable cover of I has a ﬁnite
sub-cover by [91, IV.1.2]. Hence, LIND + WKL0 →HBU →WKL0 is immediate,
while HBU clearly generalises to [−N, N] for any natural number N 0. Putting all
the ﬁnite sub-covers of [−N, N] together (using µ2 and QF-AC0,1), one obtains the
countable cover needed for LIND, assuming (µ2). On the other hand, if ¬(µ2) then
all functions on the reals are continuous by [48, Prop. 3.9 and 3.12]. But ∪q∈QIΨ
q is
a countable sub-cover of the canonical sub-cover for continuous Ψ : R →R+, and
hence LIND follows. The law of excluded middle (µ2)∨¬(µ2) now ﬁnishes this part.
For the second part, we only need to prove the forward implications. So assume
LIND and note that the formula ‘(an, bn) = IΨ
x ’ is just an =R x −Ψ(x) ∧bn =R
x+ Ψ(x), which is Π0
1, i.e. this formula is decidable using µ2, and we can treat it as
quantiﬁer-free in ACAω
0 . Now apply QF-AC0,1 to (∀n ∈N)(∃x ∈R)[(an, bn) = IΨ
x ]
to obtain LIND2. For the ﬁnal implication, we use the same argument as in the
ﬁrst part, establishing HBU relativised to [−N, N], and now combined with the
existence of the functional Ωas in (3.1).
□
The local equivalence of ‘epsilon-delta’ and sequential continuity is not provable
in ZF, while QF-AC0,1 suﬃces to establish the equivalence in a general context
(See [48, Rem. 3.13] for details). It is then a natural question whether the use of
QF-AC0,1 in the theorem is similarly essential. This question is deviously subtle, as
discussed in Remark 3.16. We show in [71, §4] that ACAω
0 in Theorems 3.3 and 3.13
can be weakened to RCAω
0 plus the existence of the classical fan functional.
Theorem 3.14. ZΩ
2 + QF-AC0,1 proves LIND; no system Π1
k-CAω
0 proves LIND.
Proof. The second part is immediate from Theorems 3.1 and 3.13. The ﬁrst part
is proved by proving item (v) from Remark 1.1 in ZΩ
2 , and deriving LIND from this
item. Thus, consider the following for any Π1
∞-formula A with any parameter:
(∀f 1)(∃n0)A(fn) →(∃γ1 ∈K0)(∀f 1)A(fγ(f)).
(NFP)
Here, ‘γ1 ∈K0’ expresses that γ1 is an associate, which is the same as a code from
RM by [47, Prop. 4.4]. Formally, ‘γ1 ∈K0’ is the following formula:
(∀f 1)(∃n0)(γ(fn) >0 0) ∧(∀n0, m0, f 1, )(m > n ∧γ(fn) > 0 →γ(fn) =0 γ(fm)).
The value γ(f) for γ ∈K0 is deﬁned as the unique γ(fn) −1 for n large enough.
Now, since A as in NFP is a Π1
k-formula for some k, we may treat it as quantiﬁer-
free given (∃3). Applying QF-AC1,0 to the antecedent of NFP, there is Y 2 such
de telle sorte que tout point de l’ensemble donn´e soit int´erieur `a au moins l’une d’elles. Applying
QF-AC0,1 to LIND, one could obtain Φ0→1 such that (∀n ∈N)[(an, bn) = IΨ
Φ(n)], but such a
functional is nowhere to be found in Lindel¨of’s original formulation.


## Page 18


18
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
that (∀f 1)A(fY (f)). Deﬁne Z2 using (∃3) as follows: Z(f) is the least n ≤Y (f)
such that A(fn) if it exists, and zero otherwise. Note that Z is continuous on NN
and hence has an associate by [47, Prop. 4.7]. Alternatively, deﬁne the associate
γ1 directly as follows: for w0∗, deﬁne γ(w) as the least n ≤|w| such that A(wn) if
such there is, and zero otherwise. Clearly, we have γ ∈K0 and (∀f 1)A(fγ(f)), i.e.
NFP follows. Finally, LIND follows from the latter by considering:
(∀x ∈R)(∃n ∈N)

(∃y ∈R)(([x]( 1
2n ) −1
n, [x]( 1
2n ) + 1
n) ⊂IΨ
y )

(3.3)
for Ψ : R →R+, and where the formula in square brackets is abbreviated A(xn).
This is a slight abuse of notation, as (only) the ﬁrst 2n elements in the sequence x1
are being used in (3.3). Applying NFP to (3.3), we obtain γ ∈K0 such that:
(∀x ∈R)(∃y ∈R)

([x](
1
2γ(x) ) −
1
γ(x), [x](
1
2γ(x) ) +
1
γ(x)) ⊂IΨ
y

.
(3.4)
Note that the formula in square brackets in (3.4) is arithmetical (including the
formula needed to make the notation γ(x) work). Hence, using QF-AC0,1 and (µ2),
there is a functional Φ which provides the real y from (3.4) on input x ∈Q. The
countable sub-cover of ∪x∈RIΨ
x can then be found by enumerating Φ(qw) for all ﬁnite
sequences w0∗of rationals which represent rationals q0
w and are such that γ(w) >0 0.
In particular, every x ∈R is in some IΨ
y by (3.4), and since v0∗:= x2γ(x) is in the
aforementioned enumeration, we also have x ∈IΨ
Φ(qv).
□
By the ﬁrst part of Theorem 3.13, the results regarding LIND have to be some-
what similar to those for HBU. However, the Lindel¨of theorem for the Baire space
behaves quite diﬀerently, as will be established in Section 4.1. Furthermore, while
HBU implies WKL, LIND does not by the following corollary.
Corollary 3.15. The system RCAω
0 +LIND proves the same L2-sentences as RCA0.
Proof. By the proof of [48, Prop. 3.1], if for a sentence A ∈Lω, the system RCAω
0
proves A, then RCA0 proves [A]ECF, where ‘[ · ]ECF’ is a syntactic translation which
-intuitively- replaces any object of type 2 or higher by a code γ1 ∈K0. Thus,
to establish the corollary, it suﬃces to show that [LIND]ECF is provable in RCA0.
However, LIND only involves objects of type 0 and 1, except for the leading quan-
tiﬁer. Hence, [LIND]ECF is nothing more than LIND with ‘(∀Ψ1→1)’ replaced by
‘(∀γ1 ∈K0)’.
Thus, by enumerating γ(w) as in the proof of the theorem, we
immediately obtain a countable sub-cover, and [LIND]ECF is provable in RCA0.
□
Finally, we discuss the Lindel¨of lemma in the grand scheme of things, and asso-
ciated results to be proved in [71].
Remark 3.16. The following are equivalent over ZF by [35]: (i) R is a Lindel¨of
space, and (ii) the axiom of countable choice (for subsets of R). This resonates with
the use of QF-AC0,1 in Theorem 3.14, but is not the entire story: we introduce a
weak and a strong version of LIND (and HBU) in [71] based on the 1895 and 1899
proofs of the Heine-Borel theorem by Borel ([9]) and Schoenﬂies ([86]). The weak
version of LIND (and HBU) is provable in ZΩ
2 (and hence in ZF). This is possible as
the weak version only provides the existence of a countable sub-cover as in LIND,
while the strong version additionally identiﬁes a sequence of reals which yield the
countable sub-cover, as in LIND2 via Φ0→1.


## Page 19


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
19
3.2.2. Other theorems. We discuss how the theorems in Remark 1.1 imply either
LIND or HBU, and hence have similar properties to the latter.
(1) The Besicovitsch and Vitali9 covering lemmas as in [1, §2] start from a
cover of open balls, one for each x ∈E ⊂Rn, and states the existence of a
countable sub-cover of E with nice properties, i.e. LIND follows. Note that
Vitali already (explicitly) discussed uncountable covers in [99, p. 236].
(2) The existence of Lebesgue numbers for any open cover is equivalent to HBU,
in the same way the countable case is equivalent to WKL0 ([32, Theo-
rem 5.5]). The same holds for the Banach-Alaoglu theorem; the equivalence
between the countable case and WKL0 is established in [11, p. 140].
(3) The principle NFP implies LIND by the proof of Theorem 3.14.
(4) The Heine-Young and Lusin-Young theorems from [104] are clearly reﬁne-
ments of HBU, while the tile theorem [38,104], and the latter’s generalisa-
tion due to Rademacher ([74, p. 190]) are clearly reﬁnements of LIND.
(5) Basic properties of the gauge integral, like uniqueness and its extension of
the Riemann integral, are equivalent to HBU over the system ACAω
0 , as
shown in Section 3.3. Note that ACAω
0 is very weak compared to ZΩ
2 , which
is in turn required to prove HBU by Theorem 3.1.
(6) In Section 3.4, we derive HBU from the following generalisation of the
Bolzano-Weierstrass theorem: every net in the unit interval has a conver-
gent sub-net. Nets (aka Moore-Smith sequences) provide a generalisation
of the concept of sequences beyond countable index sets.
Finally, we discuss how some of the ‘countable covering theorems’, like the Lindel¨of
and Vitali lemmas, from Remark 1.1 are used in mathematics.
Remark 3.17. The Cousin lemma is special because it deals with bounded sets (es-
sentially the unit interval), while the other covering theorems apply to unbounded
sets (e.g. Rn). Now, a cover of the latter is generally diﬃcult to handle, but any
countable sub-cover ‘automatically’ has nice properties: e.g. the countable sub-
additivity of the Lebesgue measure. In fact, the proofs of Sard’s theorem and the
maximal theorem in [1], and of the Lebesgue density theorem in [89] are based on
this idea. In other words, the non-local character of some of the covering theorems
in Remark 1.1 is important for some real applications of these theorems.
Similarly, for properties which hold in the unit interval minus a measure zero
set, like the diﬀerentiation theorem for gauge integrals ([6, p. 80]), one uses the
Vitali covering theorem to provide a countable sub-cover in which the complement
of a ﬁnite sub-sub-cover has small length. Hence, one can neglect this complement
and the ﬁnite nature of the sub-sub-cover then makes the proof straightforward.
3.3. The gauge integral.
3.3.1. Introduction. We provide a brief introduction to the gauge integral (Sec-
tion 3.3.2) and establish that basic properties of this integral, like uniqueness and
the fact it extends the Riemann and Lebesgue integral, are equivalent to HBU
(Section 3.3.3) over the (relatively weak) system ACAω
0 . The gauge integral is not
an isolated incident: the Henstock variational measure is a generalisation of the
9Not to be confused with the Vitali covering theorem ([6, p. 79]), which does follow from the
Vitali covering lemma via Banach’s proof from [63, p. 81]; we believe that the Vitali covering
theorem is weaker than HBU, but nonetheless requires full second-order arithmetic ZΩ
2 to prove.


## Page 20


20
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
Lebesgue outer measure (see [49, Ch. 5]), and its basic properties are equivalent
to HBU as well, as will be shown in future work. We address a possible criticism
that may be levelled at our results in Section 3.3.4. For the rest of this section, we
motivate the RM-study of the gauge integral.
As will become clear below, the gauge integral enjoys the conceptual simplicity of
the Riemann integral, but also has greater generality than the Lebesgue integral. In
fact, the gauge integral boasts the most general version of the fundamental theorem
of calculus (see Theorem 3.28) and is ‘maximally’ closed under improper integrals
(Hake’s theorem; see Theorem 3.23 for a special case). For these reasons, there
have been calls for (a somewhat stripped-down version of) the gauge integral to
replace the Riemann and Lebesgue integral (and the associated measure theory) in
the undergraduate curriculum ([3–5]). In a nutshell, the gauge integral can only be
called natural and mainstream from the point of view of mathematics.
Regarding the connection between physics and the gauge integral, Muldowney
has expressed the following opinion in a private communication.
There are a number of diﬀerent approaches to the formalisation of
Feynman’s path integral. However, if one requires the formalisa-
tion to be close to Feynman’s original formulation, then the gauge
integral is really the only approach.
Arguments for this opinion, including major contributions to Rota’s program for
the Feyman integral, may be found in [60, §A.2]. Another argument in favour of
the gauge integral is that this formalism gives rise to so-called physical solutions,
i.e. in line with the observations from physics (see [64–66,73]). For instance, most
path integral formalisms somehow require the concept of imaginary time, while
the gauge integral provides a more natural framework based on real time. A major
problem with imaginary time is namely the lack of an arrow/direction of time ([42]),
where the latter is proscribed by thermodynamics (see also [16]).
Finally, another argument for the RM study of the gauge integral is as follows:
the study of the equivalent10 Denjoy integral in descriptive set theory in [100, §2]
makes essential use of fundamental results from [31,93], like Hake’s theorem for the
gauge integral (see Theorem 3.23). We note that the treatment in [100] assumes the
measurability of the integrand in the fundamental theorem of calculus, a condition
that ﬂies in the face of the generality the gauge integral enjoys (see Theorem 3.28).
3.3.2. Introducing the gauge integral. The gauge integral is a generalisation of the
Lebesgue and (improper) Riemann integral; it was introduced by Denjoy (in a
diﬀerent from) around 1912 and studied by Lusin, Perron, Henstock, and Kurzweil.
The exact deﬁnition is in Deﬁnition 3.18, which we intuitively motivate as follows.
A limitation of the ‘ε-δ-deﬁnition’ of the Riemann integral is that near a singu-
larity of a function f : [0, 1] →R, changes smaller than any ﬁxed δ > 0 in x can
still result in huge changes in f(x), guaranteeing that the associated Riemann sums
vary (much) more than the given ε > 0. The gauge integral solves this problem by
replacing the ﬁxed δ > 0 with a gauge function δ : R →R+; the latter can single out
those partitions with ‘many’ partition points near singularities to compensate for
the extreme behaviour there. Similarly, δ : R →R+ can single out partitions which
10The gauge integral is equivalent to the (much older) Denjoy integral; see [6,31] for details.


## Page 21


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
21
avoid ‘small’ sets whose contribution to the Riemann sums should be negligible. We
study
1
√x and Dirichlet’s function in Example 3.19 after the following deﬁnition.
Deﬁnition 3.18. [Gauge integral]
(i) A gauge on I ≡[0, 1] is any function δ : R →R+.
(ii) A sequence P := (t0, I0, . . . , tk, Ik) is a tagged partition of I, written ‘P ∈
tp’, if the ‘tag’ ti ∈R is in the interval Ii for i ≤k, and the Ii partition I.
(iii) If δ is a gauge on I and P = (ti, Ii)i≤k is a tagged partition of I, then P is
δ-ﬁne if Ii ⊆[ti −δ(ti), ti + δ(ti)] for i ≤k.
(iv) For a tagged partition P = (ti, Ii)i≤k of I and any f, the Riemann sum
S(f, P) is Pn
i=0 f(ti)|Ii|, while the mesh ∥P∥is maxi≤n |Ii|.
(v) A function f : I →R is Riemann integrable on I if there is A ∈R such that
(∀ε >R 0)(∃δ >R 0)(∀P ∈tp)(∥P∥≤R δ →|S(f, P) −A| <R ε).
(vi) A function f : I →R is gauge integrable on I if there is A ∈R such that
(∀ε >R 0)(∃δ : R →R+)(∀P ∈tp)(P is δ-ﬁne →|S(f, P) −A| <R ε).
(vii) A gauge modulus for f is a function Φ : R →(R →R+) such that Φ(ε) is a
gauge as in the previous item for all ε >R 0.
The real A from items (v) and (vi) in Deﬁnition 3.18 is resp. called the Riemann
and gauge integral. We will always interpret
R b
a f as a gauge integral, unless ex-
plicitly stated otherwise. We abbreviate ‘Riemann integration’ to ‘R-integration’,
and the same for related notions. The following examples are well-known.
Example 3.19 (Two examples). Let f be the function 1/√x for x > 0, and zero
otherwise. It is easy to show
R 1
0 f =R 2 using the gauge modulus δε(x) := εx2 for
x > 0 and ε2 otherwise. Let g be constant 1 for x ∈Q, and zero otherwise. It is
easy to show
R 1
0 g =R 0 using the gauge modulus δε(x) := 1 if x ̸∈Q and ε/2k+1 if
x equals the k-th rational (for some enumeration of the rationals ﬁxed in advance).
Now, using the Axiom of Choice, a gauge integrable function always has a gauge
modulus, but this is not the case in weak systems like RCAω
0 . However, to establish
the Cauchy criterion for gauge integrals as in Theorem 3.22, a gauge modulus is
essential. For this reason, we sometimes assume a gauge modulus when studying
the RM of the gauge integral in Section 3.3.3. Similar ‘constructive enrichments’
or ‘extra data’ exist in Friedman-Simpson RM, as established by Kohlenbach in
[47, §4]. Finally, the ‘standard’ proof of the fundamental theorem of calculus for
the gauge integral (see [6, 49, 59, 93] and Theorem 3.28) readily establishes the
existence of a gauge modulus in terms of other11 extra data.
3.3.3. Reverse Mathematics of the gauge integral. We show that basic properties
of the gauge integral are equivalent to HBU. We have based this development on
Bartle’s introductory monograph [6].
First of all, we show that HBU is equivalent to the uniqueness of the gauge
integral, and to the fact that the latter extends the R-integral.
Note that the
names of the two items in the theorem are from [6, p. 13-14].
Theorem 3.20. Over ACAω
0 , the following are equivalent to HBU:
11The proofs in [6,49,59,93] establish that a gauge modulus for the integral in the fundamental
theorem of calculus
R b
a F ′ = F (b) −F (a) is simply any modulus of diﬀerentiability of F .


## Page 22


22
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
(i) Uniqueness: If a function is gauge integrable on [0, 1], then the gauge inte-
gral is unique.
(ii) Consistency: If a function is R-integrable on [0, 1], then it is gauge inte-
grable there, and the two integrals are equal.
Proof. We prove HBU →(i) →(ii) →HBU, where only the ﬁrst implication re-
quires (µ2). To prove that HBU implies Uniqueness, we assume the former and ﬁrst
prove that for every δ : R →R+ there exists a δ-ﬁne tagged partition. To this end,
apply HBU to ∪x∈I(x−δ(x), x+δ(x)) to obtain a ﬁnite sub-cover w := (y0, . . . , yk),
i.e. we have I ⊂∪x∈w(x−δ(x), x+ δ(x)). The latter cover is readily converted into
a tagged partition P0 := (zj, Ij)j≤l (with l ≤k and zj ∈w for j ≤l) by remov-
ing overlapping segments and omitting redundant intervals ‘from left to right’. By
deﬁnition, zj ∈Ij ⊂(zj −δ(zj), zj + δ(zj)) for j ≤l, i.e. P0 is δ-ﬁne.
Now let f be gauge integrable on I and suppose we have for i = 1, 2 (Ai ∈R) that:
(∀ε > 0)(∃δ1
i : R →R+)(∀P ∈tp)(P is δi-ﬁne →|S(f, P) −Ai| < ε).
(3.5)
Fix ε > 0 and δi : R →R+ in (3.5) for i = 1, 2.
We deﬁne δ3 : R →R+ as
δ3(x) := min(δ1(x), δ2(x)). By deﬁnition, a partition which is δ3-ﬁne, is also δi-
ﬁnite for i = 1, 2. Now let the partition P0 ∈tp be δ3-ﬁne, and derive the following:
|A1−A2| =R |A1−S(f, P0)+S(f, P0)−A2| ≤R |A1−S(f, P0)|+|S(f, P0)−A2| ≤R 2ε.
Hence, we must have A1 =R A2, and Uniqueness follows.
To prove that Uniqueness implies Consistency, note that ‘P is dδ-ﬁne’ is equiv-
alent to ‘∥P∥≤δ’ for the gauge dδ : R →R+ which is constant δ > 0. Rewriting
the deﬁnition of Riemann integration with this equivalence, we observe that an
R-integrable function f is also gauge integrable (with a constant gauge dδ for every
choice of ε > 0). The assumption Uniqueness then guarantees that the number A
is the only possible gauge integral for f on I, i.e. the two integrals are equal.
To prove that Consistency implies HBU, suppose the latter is false, i.e. there is
Ψ0 : R →R+ such that ∪x∈IIΨ0
x
does not have a ﬁnite sub-cover. Now let f : I →R
be R-integrable with R-integral A ∈R. Deﬁne the gauge δ0 as δ0(x) := Ψ0(x) and
note that for any P ∈tp, we have that P is not δ0-ﬁne, as ∪x∈IIΨ0
x
would otherwise
have a ﬁnite sub-cover (provided by the tags of P). Hence, the following statement
is vacuously true, as the underlined part is false:
(∀ε > 0)(∀P ∈tp)(P is δ0-ﬁne →|S(f, P) −(A + 1)| < ε).
(3.6)
However, (3.6) implies that f is gauge integrable with gauge δ0 and gauge integral
A+1, i.e. Consistency is false as the Riemann and gauge integrals of f diﬀer. Note
that δ0 also provides a gauge modulus by (3.6) in case ¬HBU.
□
By the above, the role of HBU in making the gauge integral well-behaved, con-
sists in avoiding (3.5) and (3.6) being vacuously true due to the absence of δi-ﬁne
partitions (for i = 0, 1, 2). Thus, the Cousin lemma is called Fineness theorem
in [6]. As will become clear below, this is the sole role of HBU in this context.
Nonetheless, HBU features in the RM of topology and uniform theorems in [71,83],
and Remark 3.27 suggest an important role for the special fan functional, a realiser
for HBU, in gauge integration.
In passing, we discuss the question if ACAω
0 in the previous (and subsequent)
theorem can be weakened to RCAω
0 . In our opinion, this weakening would not be


## Page 23


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
23
spectacular, given that HBU requires ZΩ
2 for a proof, as established above. Further-
more, even very basic properties of the gauge integral require ACAω
0 , as follows.
Example 3.21 (Splitting the domain). As it turns out, proving
R 1
0 f =R
R x
0 f+
R 1
x f
for 0 <R x <R 1 in general seems to require a discontinuous gauge. Indeed, if for
ε > 0 the functions δ1, δ2 are gauges for the right-hand side of the equation, a gauge
for the left-hand side is as follows ([6, p. 45]):
δ3(y) :=





min(δ1(y), 1
2(x −y))
y ∈[0, x)
min(δ1(x), δ2(x))
y =R x
min(δ2(y), 1
2(y −x))
y ∈(x, 1]
(3.7)
The function δ3 is discontinuous in general, but can be deﬁned in ACAω
0 .
Secondly, we prove the Cauchy criterion for gauge integrals, as this theorem is
needed below. Our proof is based on [6, p. 40] and illuminates the role of Θ.
Theorem 3.22 (ACAω
0 +HBU+QF-AC2,1; Cauchy criterion). A function f : I →R
is gauge integrable with a modulus if and only if there is Φ : R+ →(R →R+) with
(∀ε >R 0)(∀P, Q ∈tp)(P, Q are Φ(ε)-ﬁne →|S(f, P) −S(f, Q)| <R ε).
(3.8)
Proof. The forward implication follows by considering a gauge modulus Φ for f and
|S(f, P)−S(f, Q)| = |S(f, P)−A+A−S(f, Q)| ≤|S(f, P)−A|+|A−S(f, Q)| ≤ε
where P, Q are Φ(ε/2)-ﬁne and A is the gauge integral of f over I. For the reverse
implication let Φ be as in (3.8); we need to ﬁnd the real A from the deﬁnition of
gauge integration. This real A can be obtained as the limit of the sequence S(f, Qn)
where Qn is a Φ( 1
2n )-ﬁne partition. Now, these partitions Qn can in turn be deﬁned
by applying the functional Ωfrom Theorem 3.3 to the canonical cover associated to
Φ( 1
2n ) and using Feferman’s µ to convert the resulting ﬁnite sub-cover to a suitable
partition. Finally, (3.8) guarantees that the sequence S(f, Qn) is Cauchy, while
ACA0 proves that a Cauchy sequence has a limit by [91, III.2.2].
□
The previous proof explains the need for a gauge modulus: the latter is essential
in ‘reconstructing’ the gauge integral A as the limit in the proof, if A is not given.
Thirdly, we show that HBU is equivalent to the fact that the gauge integral en-
compasses the improper R-integral. The latter is a (usual) R-integral
R b
a f(x)d(x)
where additionally a limit operation like lima→0 or limb→∞is applied. This method
allows one to consider unbounded domains or use singularities as end points; as sug-
gested by its name, an improper R-integral is (generally) not an actual R-integral.
Now, Hake’s theorem ([6, p. 195]) implies that improper R-integrals (and the same
for improper gauge integrals) are automatically gauge integrals. Thus, Hake’s theo-
rem implies that the gauge integral is (maximally) closed under improper integrals.
We consider special cases of Hake’s theorem, including item (iii) below which
does mention gauge integrability but does not mention gauge integrals or their
uniqueness. As a result, it is fair to say that the following equivalences are not
(only) based on the uniqueness of the gauge integral. Note that Hake’s theorem in
general (see [6, §12 and §16]) comes with no restrictions.
Theorem 3.23. Over ACAω
0 + QF-AC2,1, the following are equivalent to HBU:
(i) There exists a function which is not gauge integrable with a modulus.


## Page 24


24
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
(ii) (Hake) If f is gauge integrable on I with a modulus and R-integrable on
[x, 1] for x >R 0, then the limit of R-integrals limx→0+
R 1
x f is
R 1
0 f.
(iii) (weak Hake) If f is gauge integrable with a modulus on I and R-integrable
on [x, 1] for x >R 0, then the limit of R-integrals limx→0+
R 1
x f exists.
Proof. We shall prove HBU →(ii) →(iii) →(i) →HBU. Note that the second
implication is trivial. Now assume item (iii) and consider the function g : I →R
which is 0 if x =R 0, and
1
x otherwise.
This function exists in ACAω
0 by [48,
Prop. 3.12]. By the development of integration theory in [91, IV.2], the R-integral
R 1
x g exists for x > 0 and is readily seen to equal ln(x), the natural logarithm.
However, the limit x →0+ of this function is −∞. Thus, the limit limx→0+
R 1
x g
does not exist, and by the contraposition of weak Hake’s theorem, we conclude that
g is not gauge integrable with a modulus on I, i.e. item (i) follows.
The implication (i) →HBU follows from the proof of Theorem 3.20: in the last
part of the latter proof, it is shown that ¬HBU allows us to deﬁne a gauge δ0 for
which there are no δ0-ﬁne partitions. Hence, the underlined part in (3.6) is false,
making the formula trivially true for any f and A, i.e. every function is gauge
integrable (with a modulus). Contraposition now yields the desired implication.
Finally, we prove item (ii) in ACAω
0 + HBU + QF-AC2,1 based on the proof
in [6, p. 195]. In a nutshell, the latter uses the Saks-Henstock lemma to prove
that the indeﬁnite integral F(x) :=
R 1
x f is (ε-δ-)continuous in x on I.
Hence
limx→0+ F(x) =R F(0), which is exactly as required for item (ii).
First of all,
the Saks-Henstock lemma intuitively states that if one considers a sub-partition
of a δ-ﬁne partition, one inherets all the ‘nice’ properties of the original partition.
The proof of this lemma is a straight-forward ‘epsilon-delta’ argument, with one
subtlety: the Cauchy criterion (as is Theorem 3.22) for gauge integrals requires
a gauge modulus, which we (therefore) assumed in item (ii). The proof that the
Saks-Henstock lemma yields the continuity of F(x) :=
R 1
x f is also a straight-forward
‘epsilon-delta’ argument.
□
The gauge integral is a proper extension of the Lebesgue and (improper) Riemann
integral. As it turns out, this claim is of considerable logical strength, as follows.
Corollary 3.24 (RCAω
0 + WKL + QF-AC2,1). The below combination yields ATR0:
(i) There exists a function that is not gauge integrable with a modulus.
(ii) There exists a function that is not Riemann integrable, but gauge integrable.
Proof. By [48, Prop. 3.7], ¬(∃2) implies that all F : R →R are continuous, and
hence uniformly continuous on [0, 1] by WKL and [47, Prop. 4.10].
Hence, any
gauge integrable function is also Riemann integrable, as the gauge has an upper
bound on [0, 1]. By contraposition, item (ii) from the theorem implies (∃2). By
Theorem 3.23, item (i) now yields HBU. The combination HBU + (∃2) yields ATR0
by [69, Cor. 6.7] and Theorem 3.3.
□
Fourth, we show that HBU is equivalent to the fact that the gauge integral
is a proper extension of the Lebesgue integral. In fact, f : [0, 1] →R is Lebesgue
integrable if and only if |f|, f are gauge integrable ([6, §7, p. 102]). We use the latter
variant as introducing the Lebesgue integral is beyond the scope of this paper.
Theorem 3.25. Over ACAω
0 , HBU is equivalent to the following statement: There
exists a function κ : I →R which is gauge integrable with a modulus but |κ| is not.


## Page 25


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
25
Proof. The reverse implication is immediate by Theorem 3.23. For the forward
implication, deﬁne ak := 1 −
1
2k and κ(x) := (−1)k+1 2k
k if x ∈[ak−1, ak) (k0 ≥1),
and 0 otherwise. Then for x >R 0, the area between the horizontal axis and the
graph of |κ| on [0, x] is just a ﬁnite collection of (bounded) rectangles, i.e. |κ| is
deﬁnitely R-integrable on [0, x] for x < 1. In particular, if x ≥R 1 −1
2k , there are at
least k rectangles to the left of x; the ﬁrst has base 1/2 and area 1, the second one
base 1/4 and area 1/2, . . . , the k-th one has base 1/2k and area 1/k. The R-integral
R x
0 |κ| is thus at least Pk
i=1
1
i . The limit of the latter is the divergent harmonic
series, and item (iii) from Theorem 3.23 yields that |κ| is not gauge integrable on
I with a modulus. To prove that κ is gauge integrable on I, note that (3.7) allows
us to ‘piece together’ gauges. The following gauge modulus is based on that idea:
δε(x) :=





d(x, E)
x ∈[0, 1] \ E
ε
4(k+1)
x =R ak
2−m(ε)
x =R 1
,
where E is the set consisting of the real 1 and all ak, and where m(ε) is such that
m(ε) ≥1
ε and the tail of the alternating harmonic series satisﬁes | P∞
k=n
−1k+1
k
| ≤ε
for n ≥m(ε). We leave it as an exercise that this gauge can be deﬁned in ACAω
0 .
The proof that δε is a gauge for κ is completely straightforward and elementary, but
somewhat long and tedious. Hence, we omit this proof and refer to [6, p. 35].
□
Example 3.21 notwithstanding, we now prove that the base theory in Theo-
rem 3.20 can be weakened to weak K¨onig’s lemma.
Corollary 3.26. The equivalences in Theorem 3.20 can be proved in RCAω
0 +WKL.
Proof. As noted in the proof, only HBU →(i) in Theorem 3.20 requires (µ2). To
prove this implication in RCAω
0 + WKL, note that in case (µ2), we may use the
proof of Theorem 3.20. In case of ¬(µ2), all R →R-functions are continuous by
[48, Prop.˜3.12]. Thanks to WKL, all R →R-functions are uniformly continuous on
[0, 1] by [47, Prop. 4.10]. Hence, the deﬁnition of gauge integral reduces to that
of Riemann integral, and the latter is even unique in RCA0. The law of excluded
middle as in (µ2) ∨¬(µ2) now ﬁnishes the proof.
□
Fifth, we discuss in what sense we may evaluate (general) gauge integrals.
Remark 3.27 (Computing integrals). In the case of the R-integral, a modulus (of
R-integration) computes a δ > 0 in terms of any ε > 0 as in Deﬁnition 3.18. Hence,
if Pn is the equidistant partition of I with mesh 1/2n, we know that S(Pn, f) con-
verges to the R-integral of f on I, and the modulus provides a rate of convergence.
For the gauge integral, there is no analogue of the equidistant partition: even given
a gauge modulus δ(ε, x), we need to ﬁnd, say for every ε > 0, a δ(ε, ·)-ﬁne partition
Qε; only then can we consider the limit of S(Qε, f) for ε →0, which converges
to the gauge integral of f on I as in Theorem 3.22. To ﬁnd such a partition, the
only option (we can imagine) is to consider ∪x∈I(x −δ(ε, x), x + δ(ε, x)) and apply
the realiser Ωfor HBU as in (3.1) to obtain a ﬁnite sub-cover. The latter can be
modiﬁed using µ2 into a δ(ε, ·)-ﬁne partition.
Sixth, two of the redeeming features of the gauge integral are its simplicity
(via the similarity to the Riemann integral) and its generality. Indeed, the gauge
integral boasts the most general version of the fundamental theorem of calculus and


## Page 26


26
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
is ‘maximally’ closed under improper integrals via Hake’s theorem. We now consider
the former theorem, which indeed only requires a modulus of diﬀerentiability.
Theorem 3.28 (RCAω
0 + HBU). Let f : R →R be diﬀerentiable with a modulus.
Then
R b
a f ′ = f(b) −f(a), and the latter modulus provides a gauge modulus.
Proof. The textbook proof (see e.g. [6, p. 58]) amounts to little more than manip-
ulation of deﬁnitions and of course goes through in RCAω
0 + HBU.
□
It goes without saying that restricting the fundamental theorem of calculus to
e.g. measurable functions (as is done in e.g. [100]) ﬂies in the face of the generality
the gauge integral enjoys.
Finally, we discuss some foundational implications of the above results.
Remark 3.29. Feferman discusses in [23, V] what fragments of mathematics are
necessary for the development of physics. He claims that the logical system W,
a conservative extension of Peano arithmetic, suﬃces for this purpose. Feferman
also discusses two purported (exotic) counterexamples involving non-measurable
sets and non-separable spaces; he shows that these are rather fringe in physics, if
part of the latter at all.
However, by contrast, Feynman’s path integral and the associated diagrammatic
approach are central to large parts of modern physics. To the best of our knowl-
edge, the gauge integral is unique in that it provides a formalisation (of part) of
Feynman’s formalism that remains close to Feyman’s development and ideas (based
on Riemann sums), as discussed in [60, §A.2] and [13, Ch. 10]. Moreover, the gauge
integral avoids the non-physical concept of imaginary time ([64–66,73]). Hence, if
one requires that a mathematical formalisation remains close to (the original treat-
ment in) physics, then there seems to be no choice other than the gauge integral
for the formalisation of Feynman’s path integral. As established in this section, the
basic development of the gauge integral requires HBU, and the latter is not provable
in any Π1
k-CAω
0 , a system much stronger than W. Thus, Feferman’s above claim
seems incorrect, assuming the aforementioned caveat concerning formalisations.
3.3.4. Extra data and the gauge integral. We address a possible criticism that may
be levelled at the results in the previous section.
In particular, it is a natural
question (from the pov of computability theory) whether adding ‘extra data’ to the
deﬁnition of the gauge integral leads to an integration theory in weaker systems.
Before we answer this question, we emphasise that the deﬁnition of the gauge
integral as in Deﬁnition 3.18 is taken verbatim from the literature, except the ﬁnal
item, the existence of which is however taken for granted throughout the literature.
Moreover, the ﬁrst step in the development of the gauge integral is always the use
of Cousin’s lemma (or open-cover compactness) to show that the deﬁnition of the
gauge integral ‘makes sense’. For instance, Swartz writes the following.
In order for [the deﬁnition of the gauge integral] to make sense,
there is one matter that needs to be addressed. We must show that
every gauge γ has at least one γ-ﬁne tagged partition. ([93, p. 6])
The next step is then always to show that the gauge integral is unique, and this
proof is based on the existence of γ-ﬁne partitions (see again [93, p. 6]). The same
approach may be found in [6, 59]. Thus, the previous section deals with ‘actual


## Page 27


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
27
mathematics’ or ‘theorems as they stand’, i.e. we have avoided the use of ‘extra
data’ to the maximal extent possible, as mandated by Simpson in [91, I.8.9].
Nonetheless, for a variety of reasons, one may wish to ‘constructivise’ the def-
inition of the gauge integral, i.e. build in extra data to guarantee a development
in weaker systems (than ZΩ
2 ). We consider one possible/obvious such ‘richer’ def-
inition, and show that one still readily obtains HBU. Now, the latter is needed in
the proof of Theorem 3.20 to guarantee the existence of δ-ﬁne partitions for arbi-
trary gauges δ. Hence, it seems that the most obvious piece of ‘extra data’ is the
requirement that such a partition is given together with the gauge, as follows.
Deﬁnition 3.30. A function f : I →R is strongly gauge integrable on I if there is
A ∈R such that for all ε > 0, there is a gauge δ : R →R+ such that
(∀P ∈tp)(P is δ-ﬁne →|S(f, P) −A| <R ε) ∧(∃Q ∈tp)(Q is δ-ﬁne).
(3.9)
The notion of strong gauge modulus is deﬁned similarly.
Note that the second conjunct in (3.9) guarantees that the antecedent in the
ﬁrst conjunct of (3.9) cannot be vacuously true. One may cherish the hope that
this ‘extra data’ obviates the use of HBU, but we now show that the latter is still
readily obtained from basic properties of the gauge integral.
To this end, we now turn to the fundamental theorem of calculus for the gauge
integral; this is the most general formulation of the well-known phenomenon that
integration and diﬀerentiation cancel out. As noted above, the ‘standard’ proof
of the fundamental theorem of calculus in [6, p. 58], [49, p. 6], [59, Ch. 2.4], and
[93, Ch. 1] also establishes that a gauge modulus for the integral in
R b
a F ′ = F(b) −
F(a) is simply any modulus of diﬀerentiability of F; this modulus provides the
‘delta’ in terms of the ‘epsilon’ and the point at which the derivative is taken.
Similar constructs and results exist12 in e.g. Bishop’s constructive analysis, and
other computational approaches to mathematics.
Theorem 3.31 (FTCstrong). If F : R →R is diﬀerentiable with a modulus on I and
derivative F ′, then the latter is strongly gauge integrable with the same modulus
and we have F(1) −F(0) =R
R 1
0 F ′.
Theorem 3.32. The system RCAω
0 proves HBU ↔FTCstrong.
Proof. The forward direction follows by the usual proof from the literature; in a
nutshell, for the modulus of diﬀerentiability λx.δε(x) of F, any δε-ﬁne partition
P satisﬁes |F(1) −F(0) −S(F ′, P)| < ε using standard calculus tricks, known as
‘telescoping sums’ and the ‘straddle lemma’ (see e.g. [6, p. 57-58]). Note that HBU
implies the equivalence between ‘normal’ and strong gauge integrability.
For the reverse direction, ﬁx Ψ : R →R+ and pick any function F : R →R with
derivative F ′ and modulus of diﬀerentiability G : R2 →R. Then deﬁne G0(x, ε) as
the minimum of G(x, ε) and Ψ(x). Clearly, G0 is also a modulus of diﬀerentiability
for F, and FTCstrong implies that there is a G0-ﬁne partition of the unit interval,
immediately yielding a ﬁnite sub-cover for the canonical cover associated to Ψ. In
this way, HBU follows, and we are done.
□
12As detailed in [8], a modulus function is part and parcel of the deﬁnition of a (uniformly)
continuous and diﬀerentiable functions. Any modulus of uniform continuity is also a modulus of
Riemann integrability, as can be gleaned from [8, p. 47].


## Page 28


28
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
While the previous theorem is not particularly deep, it does suggest that a
constructive treatment of the gauge integral is not entirely trivial.
3.4. Nets and compactness. We show that the Bolzano-Weierstrass theorem for
nets implies HBU. More results of this nature, e.g. for the monotone convergence
theorem and the Dini and Arzel`a theorems, may be found in [85].
The move to more and and more abstract mathematics can be quite concrete
and speciﬁc: Moore presented a framework called General Analysis at the 1908
ICM in Rome ([55]) that was to be a ‘unifying abstract theory’ for various parts
of analysis. For instance, Moore’s framework captures various limit notions in one
abstract concept ([56]). This theory also included a generalisation of the concept
of sequence beyond countable index sets, nowadays called nets or Moore-Smith
sequences. These were ﬁrst described in [57] and formally introduced by Moore
and his student Smith in [58]. In this section, we derive HBU from the Bolzano-
Weierstrass theorem for nets in [0, 1] and indexed by Baire space. Since nets are a
generalisation of sequences, the latter theorem thus provides a ‘uniﬁed’ notion of
compactness, implying both sequential and open-cover compactness.
We ﬁrst need the following standard deﬁnition (see e.g. [43, Ch. 2])
Deﬁnition 3.33. [Nets] A set D ̸= ∅with a binary relation ‘⪯’ is directed if
(a) The relation ⪯is transitive, i.e. (∀x, y, z ∈D)([x ⪯y ∧y ⪯z] →x ⪯z).
(b) The relation ⪯is reﬂexive, i.e. (∀x ∈D)(x ⪯x).
(c) For x, y ∈D, there is z ∈D such that x ⪯z ∧y ⪯z.
For such (D, ⪯) and topological space X, any mapping xd : D →X is a net in X.
The relation ‘⪯’ is often not mentioned together with the net; we also write
d1, . . . , dk ⪰d as short for (∀i ≤k)(di ⪰d).
Deﬁnition 3.34. [Convergence of nets] If xd is a net in X, we say that xd converges
to the limit limd xd = y ∈X if for every neighbourhood U of y, there is d ∈D such
that for all e ⪰d, xe ∈U.
Deﬁnition 3.35. [Sub-nets] A sub-net of a net xd with directed set (D, ⪯D), is a
net yb with directed set (B, ⪯B) such that there is a function φ : B →D such that:
(a) the function φ satisﬁes yb = xφ(b),
(b) (∀d ∈D)(∃b0 ∈B)(∀b ⪰B b0)(φ(b) ⪰D d).
In this section, we only study directed sets that are subsets of Baire space, i.e.
as given by Deﬁnition 3.36. Similarly, we only study nets xd : D →R where D is
a subset of Baire space. Thus, a net xd in R is just a type 1 →1 functional with
extra structure on its domain D provided by ‘⪯’ as in Deﬁnition 3.36.
Deﬁnition 3.36. [RCAω
0 ] A ‘subset D of NN’ is given by its characteristic function
F 2
D ≤2 1, i.e. we write ‘f ∈D’ for FD(f) = 1 for any f ∈NN. A ‘binary relation ⪯
on a subset D of NN’ is given by the associated characteristic function G(1×1)→0
⪯
,
i.e. we write ‘f ⪯g’ for G⪯(f, g) = 1 and any f, g ∈D. Assuming extensionality
on the reals as in item (v) of Deﬁnition 2.5, we obtain characteristic functions that
represent subsets of R and relations thereon. Using pairing functions, it is clear we
can also represent sets of ﬁnite sequences (of reals), and relations thereon.


## Page 29


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
29
A basic result is that a topological space X is compact if and only if every net
in X has a convergent sub-net. Let BWnet be the Bolzano-Weierstrass theorem for
nets, i.e. the statement that every net in the unit interval has a convergent sub-net,
as can be found in e.g. [78, p. 98]. Note that BWnet is assumed to be restricted as
in Deﬁnition 3.36. We have the following theorem.
Theorem 3.37. The system RCAω
0 + BWnet proves HBU.
Proof. Note that BWnet implies the monotone convergence theorem, as sequences
are clearly nets. Hence, we have access to ACA0 by [91, III.2.2]. Now, in case ¬(∃2),
all functions on R are continuous by [48, Prop. 3.12], and HBU reduces to WKL by
[47, §4]. We now prove HBU in case (∃2), which ﬁnishes the proof using the law of
excluded middle. Thus, suppose ¬HBU and ﬁx some Ψ : I →R+ for which ∪x∈IIΨ
x
does not have a ﬁnite sub-cover. Let D be the set of all ﬁnite sequences of reals
in the unit interval, and deﬁne ‘v ⪯D w’ for w, v ∈D if ∪i<|v|Iψ
v(i) ⊆∪i<|w|Iψ
w(i),
i.e. the set generated by w includes the set generated by v. Note that (∃2) suﬃces
to deﬁne ⪯D. Clearly, the latter is transitive and reﬂexiv, also satisﬁes item (c) in
Deﬁnition 3.33. To deﬁne a net, consider
(∀w1∗∈[0, 1])(∃q ∈Q ∩[0, 1])(q ̸∈∪i<|w|IΨ
w(i)),
(3.10)
which again holds by assumption. Note that the underlined formula in (3.10) is
decidable thanks to (∃2). Applying QF-AC1,0 to (3.10), we obtain a net xw in [0, 1],
which has a convergent (say to z0 ∈I) sub-net yb = xφ(b) for some directed set
(B, ⪯B) and φ : B →D, by BWnet. By deﬁnition, the neighbourhood U0 = IΨ
z0
contains all yb for b ⪰B b1 for some b1 ∈B. However, taking d = ⟨z0⟩in the second
item in Deﬁnition 3.35, there is also b0 ∈B such that (∀b ⪰B b0)(φ(b) ⪰D ⟨z0⟩). By
the deﬁnition of ‘⪯B’, φ(b) is hence such that ∪i<|φ(b)|IΨ
φ(b)(i) contains U0, for any
b ⪰B b0. Now use item (c) from Deﬁnition 3.33 to ﬁnd b2 ∈B satisfying b2 ⪰B b0
and b2 ⪰B b1. Hence, yb2 = xφ(b2) is in U0, but ∪i<|φ(b2)|IΨ
φ(b2)(i) also contains U0,
i.e. xφ(b2) must be outside of U0 by the deﬁnition of xw, a contradiction. In this
way, we obtain HBU in case (∃2), and we are done.
□
Finally, we note that Moore and Smith already proved versions of the Bolzano-
Weierstrass, Dini, and Arzel`a theorem in [58].
4. Main results II
4.1. Jumping to the superjump. We show that the Lindel¨of lemma for Baire
space and Feferman’s µ2 together give rise to the Suslin functional S and the su-
perjump S. We introduce the latter in Section 4.1.1, while the Lindel¨of lemma for
Baire space and the associated functional Ξ (computing the countable sub-cover)
are introduced in Section 4.1.2. The following results are established below.
(1) The superjump S is computable in the special fan functional Θ and the
Suslin functional S (Section 4.1.1).
(2) The Suslin functional S is (uniformly) computable in Feferman’s µ and
the functional Ξ which computes the countable sub-cover from the Lindel¨of
lemma for Baire space (Section 4.1.2).
As a consequence, the combination of Feferman’s µ and any such Ξ computes the
superjump S. We recall the fact that the special fan functional Θ is not unique,
and neither is ‘the’ aforementioned functional Ξ.


## Page 30


30
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
4.1.1. Computing the superjump. We show that the combination of the Suslin func-
tional S and the special fan functional Θ computes the superjump. The latter cor-
responds to the Halting problem for computability on type two inputs. Indeed, the
superjump S3 was introduced in [30] by Gandy (essentially) as follows:
S(F 2, e0) :=
(
0
if {e}(F) terminates
1
otherwise
,
(S3)
where the formula ‘{e}(F) terminates’ is a Π1
1-formula deﬁned by Kleene’s S1-S9.
As to its history, Harrington has proved that the ﬁrst ordinal not computable in
S is the ﬁrst recursively Mahlo ordinal ([33]). In turn, the latter ordinal appears
in the study of constructive set and type theory and the associated proof theory
([75–77]).
In particular, {R ⊆N : R is computable from S} is the smallest β-
model of ∆1
2-CA0 + (M), where (M) expresses that every true Π1
3-sentence with
parameters already holds in a β-model of ∆1
2-comprehension ([77]). As discussed
in Remark 4.18, S lives far outside of predicative mathematics.
Theorem 4.1. The superjump S is computable in any Θ satisfying SCF(Θ) and
the Suslin functional S.
Proof. We ﬁrst provide a sketch of the proof as follows. Recall that if σ is a ﬁnite
binary sequence, then [σ] is the set of total binary extensions of σ.
(1) Given F 2, let αF (e) = {e}(F, e) whenever the value is in {0, 1}, and let XF
be the set of total binary extensions of αF .
(2) Compute GF from F and S with the properties
i) if f ̸∈X, then GF (f) > 0
ii) if GF (f) > 0, then [ ¯fGF (f)] does not intersect XF
iii) for f ∈XF , GF (f) = 0.
(3) Show that S(F) is uniformly computable in S and f ∈XF .
(4) Since Θ(GF ) has to intersect XF , and we can decide where, S(F) is com-
putable in Θ and S, uniformly in F.
We work out the proof in full detail below.
□
We will now list some basic lemmas needed for the detailed proof of Theorem 4.1.
We ﬁrst deﬁne an important concept relating to S1-S9 computability with type two
inputs. Its importance stems from the fact that it is independent of the choice of
input functional F 2, as follows.
Lemma 4.2. There is a primitive recursive ξ of type level 1, independent of
the choice of F 2, such that {ξ(e,⃗a)}(F, ξ(e,⃗a)) is resp. (0, 1, undeﬁned) whenever
{e}(F,⃗a) is resp. (= 0, > 0, undeﬁned).
Lemma 4.3. There is a primitive recursive function η such that for all e,⃗a, F
{η(e)}(F,⃗a) ≃{e}(F,⃗a) ·−1,
where ‘≃’ means that both sides are undeﬁned or both sides are deﬁned and equal.
Deﬁnition 4.4. Let f be a total binary function. By an application of the recursion
theorem for Turing computations in oracles we deﬁne
[e]f(⃗a) :=
(
0
if f(ξ(e,⃗a)) = 0
1 + [η(e)]f(⃗a)
if f(ξ(e,⃗a)) = 1 .
Clearly, if the recursion goes on forever, [e]f(⃗a) will be undeﬁned.


## Page 31


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
31
Intuitively speaking and from the outside, [·]f may look like an indexing of some
partial functions computable in some functional of type 2, but to what extent this
is correct, will depend on the choice of f.
We will now use F to deﬁne a relation, mimicking the subcomputation relation
relative to F, as far as possible. As a cheap trick, we will let an alleged computation
tuple be a subcomputation of its own if it is clear that something is wrong, in order
to force such objects into the non-well-founded part of the relation.
Deﬁnition 4.5. Given f, we let Ωf be the set of triples (e,⃗a, b) such that [e]f(⃗a) =
b. Given F as well, deﬁne the relation ‘⪯’ (short for ⪯f,F) on Ωf as follows:
• If e is not a Kleene index for any of S1-S9, we put (e,⃗a, b) ⪯(e,⃗a, b).
• If e is an index for an initial computation, we let (e,⃗a, b) be a leaf in our
ordering if {e}(F,⃗a) = b, and its own sub-node otherwise. This decision
will be independent of the choice of the functional F.
• We treat the case S4. The rest of the cases, except S8, are similar or void
(e.g. S6). If e is an index for composition {e}(F,⃗a) = {e1}({e2}(⃗a),⃗a), c is
given and there is a b such that [e2]f(⃗a) = b, [e1]f(b,⃗a) = c and [e]f(⃗a) = c,
then we deﬁne (e2,⃗a, b) ⪯(e,⃗a, c) and (e1, b,⃗a, c) ⪯(e,⃗a, c). If there is no
such b , we let (e,⃗a, c) ⪯(e,⃗a, c).
• For the case S8, if we have {e}(F,⃗a) = F(λb.{d}(F, b,⃗a)), we let (e,⃗a, c) ⪯
(e,⃗a, c) unless h(b) = [d]f(b,⃗a) is a total function and F(h) = c. In the
latter case, we let (d, b,⃗a, h(b)) ⪯(e,⃗a, c) for all b.
The intuitive explanation of Deﬁnition 4.5 is as follows: The set of ﬁnite se-
quences (e,⃗a, b) such that {e}(F,⃗a) = b is deﬁned by a strictly positive inductive
deﬁnition, so whenever a sequence is added to the set it is either initial or there is
a unique set of other sequences in the set causing that we accept the one chosen.
These are called immediate predecessors in the computation tree. The relation ‘⪯’
is deﬁned on the set of (e,⃗a, b) where [e]f(⃗a) = b as the immediate predecessor
relation wherever the inductive deﬁnition of the computation tree is locally correct.
Lemma 4.6. For any function f, the well-founded segment of ⟨Ωf, ⪯f,F ⟩is an
initial segment of the full computation relation of F.
Proof. This is trivial by induction over this well-founded segment.
□
Lemma 4.7. For any f ∈XF , if {e}(F,⃗a) = b, then [e]f(⃗a) = b.
Proof. We prove this by induction on b. If b = 0, then {ξ(e,⃗a)}(F, ξ(e,⃗a)) = 0, so
f(ξ(e,⃗a)) = 0 = [e]f(⃗a). If b > 0, we use the induction hypothesis on b ·−1 for the
index η(e) and the fact that [e]f(⃗a) = b in this case.
□
Lemma 4.8. If f ∈XF and {e}(F,⃗a) = b, then (e,⃗a, b) is in the ⪯f,F -well-founded
part of Ωf. Moreover, this well-founded part is exactly the full tree of terminating
computations {e}(F,⃗a) = b relative to F.
Proof. That the computation tree for computations relative to F is contained in
the well-founded part is proved by induction over the tree of real computations.
Now, if the well-founded part of ⟨Ωf, ⪯f,F⟩contains more, we may consider one
alleged computation (e,⃗a, b) in Ωf that is not a real F-computation, but that is
minimal as such. Since it is in the well-founded part, (e,⃗a, b) is locally correct, so
either it is an initial computation or it has subcomputations that are real (because


## Page 32


32
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
we consider a minimal one). Being locally correct, we see in each case that (e,⃗a, b)
must be genuine after all.
□
Lemma 4.9. If f ∈XF , then S(F) is uniformly computable in f, F and S.
Proof. From the data, we can compute the characteristic function of {(e,⃗a, b) |
{e}(⃗a) = b}, and S(F) is primitive recursive in this characteristic function.
□
We are now ready to provide the proof of Theorem 4.1 as follows.
Proof. We see from Lemma 4.6 that if the ⪯f,F -well-founded part of Ωf is closed
under the Kleene schemes S1-S9 relative to F, then S(F) is computable in f, F
and S as above. We need S to isolate the well-founded part, and (only) F and µ2
to decide if we have the closure.
Now, assume that f is such that the ⪯f,F-well-founded part is not S1-S9-closed.
Let {e}(F,⃗a) = b be a computation of minimal rank such that we do not have
[e]f(⃗a) = b. By induction on b we see that there must be an index d such that
{d}(F, d) ∈{0, 1} and {d}(F, d) ̸= f(d). If we then put GF (f) := d + 1 we have
ensured that there will be no extension of fGF (f) in XF . Using Gandy selection
for F, µ and f, we can trivially ﬁnd a d with this property from the well-founded
part of Ωf. In order to show that GF is deﬁnable from S, F, µ via a term in G¨odel’s
T , we proceed as follows:
Given the well-founded part W of ΩF , we may arithmetically decide
if it respects S1-S9. If it does not, let Γ be the, arithmetically in
F, inductive deﬁnition of the computation tuples for computing
relative to F, and by one application of µ on Γ(W) \ W, we may
ﬁnd the (e,⃗a, b) that leads us to the d we need.
In light of the previous, we put GF (f) := 0 if the ⪯f,F -well-founded part of Ωf is a
ﬁxed point of the inductive deﬁnition of computations relative to F, while we put
GF (f) := d + 1 for the d selected as above otherwise. Thus, Θ(GF ) must contain
a function from which, together with F and S, we can compute S(F).
□
Some of the methods in this proof have been expanded in [68, 71], where even
sharper results are obtained.
4.1.2. Computing the Suslin functional. We show that the Suslin functional S can
be computed by the combination of Feferman’s µ and the functional Ξ arising from
the Lindel¨of lemma for NN. Furthermore, the Lindel¨of lemma for NN (not involving
Ξ) and the axiom (µ2) are seen to imply Π1
1-CA0.
Regarding the Linde¨of lemma, we recall that Lindel¨of already proved that Eu-
clidean space is hereditarily Lindel¨of in [50] around 1903. Now, the latter hereditary
property implies that NN has the Lindel¨of property, since NN is homeomorphic to
the irrationals in [0, 1] using continued fractions expansion. Thus, for any Ψ2, the
corresponding ‘canonical cover’ of NN is ∪f∈NN

fΨ(f)

where [σ0∗] is the set of all
extensions in NN of σ. By the Lindel¨of lemma for NN, there is a sequence f 0→1
(·)
such that the set of ∪i∈N[ ¯fiΨ(fi)] still covers NN, i.e.
(∀Ψ2)(∃f 0→1
(·)
)(∀g1)(∃n0)(g ∈

fnΨ(fn)

).
(LIND4)
Similar to the speciﬁcation SCF(Θ) for the special fan functional Θ, we introduce
the following speciﬁcation based on LIND4. As for the former speciﬁcation, the


## Page 33


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
33
functional Ξ2→(0→1) satisfying LIN(Ξ) is not unique.
(∀Ψ2)(∀g1)(∃n0)(g ∈

Ξ(Ψ)(n)Ψ(Ξ(Ψ)(n))

).
(LIN(Ξ))
As for the special fan functional Θ in Theorem 3.3, the existence of Ξ as in LIN(Ξ)
amounts to the Lindel¨of lemma LIND4 itself.
Theorem 4.10. The system Π1
1-CAω
0 + QF-AC2,1 proves LIND4 ↔(∃Ξ)LIN(Ξ).
Proof. We only need to prove the forward direction. We rephrase LIND4 to
(∀G2)(∃f 0→1
(·)
)

(∀g1)(∃n0)(g ∈

f +
n fn(0)

) ∧(∀m0)(fm(0) = G(f +
m))

,
(4.1)
where f +(k) = f(k + 1). Using the Suslin functional S and µ we see that the part
of (4.1) inside the (outermost) square brackets can be viewed as quantiﬁer-free, and
thus the existence of Ξ follows from QF-AC2,1.
□
For a (much) weaker base theory, we need the following functional from [69,71].
(∃κ3
0 ≤3 1)(∀Y 2)

κ0(Y ) = 0 ↔(∃f ∈C)Y (f) = 0

.
(κ3
0)
Here, RCAω
0 + WKL + (κ3
0) + QF-AC0,1 is conservative up to language13 over WKL0
by [48, Prop. 3.15], while RCAω
0 proves that [(∃2)+(κ3
0)] ↔(∃3) by [69, Rem. 6.13].
Corollary 4.11. The system RCAω
0 +(κ3
0)+QF-AC2,1 proves LIND4 ↔(∃Ξ)LIN(Ξ).
Proof. Consider (∃2) ∨¬(∃2) and note that ∃3 follows in the former case, while all
functions on Baire space are continuous in the latter case by [48, Prop. 3.7]. Hence,
we may deﬁne Ξ3 in the latter case as the functional that lists all ﬁnite sequences
of natural numbers on input any (by assumption continuous) functional.
□
The functional Ξ is weak in insolation, by the following theorem.
Theorem 4.12. RCAω
0 + (∃Ξ)LIN(Ξ) proves the same L2-sentences as RCA0.
Proof. As in the proof of Corollary 3.15, it suﬃces to show that [(∃Ξ)LIN(Ξ)]ECF
is provable in RCA0. However, (∃Ξ)LIN(Ξ) only involves objects of type 0 and 1
except for the two leading quantiﬁers. Hence, [(∃Ξ)LIN(Ξ)]ECF is as follows:
(∃ξ1 ∈K0)(∀γ1 ∈K0)(∀g1)(∃n0)(g ∈

ξ(γ)(n)γ(ξ(γ)(n))

).
Thus, by deﬁning ξ as the enumeration of γ(w) as in the proof of Theorem 3.14,
we obtain an associate for a functional producing a countable sub-cover, and the
sentence [(∃Ξ)LIN(Ξ)]ECF is therefore provable in RCA0.
□
The functional Ξ becomes strong when combined with µ2, as follows.
Theorem 4.13. The Suslin functional S is uniformly computable in Feferman’s µ
and any Ξ satisfying LIN(Ξ). Furthermore, ACAω
0 + (∃Ξ)LIN(Ξ) proves (S2).
Proof. Recall the deﬁnition of the Suslin functional S as follows:
S(f) =

0
if (∃g1)(∀n0)(f(¯gn) = 0)
1
otherwise
.
Deﬁne F 2
f (g) as n + 1 if n is minimal such that f(¯gn) > 0, and 0 if there is no such
n. Note that Ff is readily deﬁned from f (in terms of µ2) inside ACAω
0 , and note
13The fundamental objects in the language of RCAω
0 are functions, with sets being deﬁnable
from these, while it is exactly the opposite for RCA0. This however makes no diﬀerence.


## Page 34


34
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
that if Ff(h) > 0 and ¯gFf(h) = ¯hFf(h), then Ff(g) = Ff(h). Let Ξ be such that
LIN(Ξ), and consider the following formula
S(f) = 0 ↔(∃i0)(Ff(Ξ(Ff )(i)) = 0).
(4.2)
The reverse direction in (4.2) is immediate by the deﬁnition of Ff. For the forward
direction, assume S(f) = 0 and let g1 satisfy (∀n0)(f(¯gn) = 0), i.e. Ff(g) = 0. As
observed above, if Ff(h) > 0, we have g ̸∈[¯hFf(h)]; hence if Ff(hn) > 0 for all
n ∈N where hn = Ξ(Ff)(n), the corresponding countable subset of the covering
induced by Ff will not be a covering. Thus Ff(Ξ(Ff)(n)) = 0 must hold for some
n, i.e. the right-hand side of (4.2) follows. Finally, (4.2) clearly characterises S(f)
in terms of µ, f and Ξ (via a term in G¨odel’s T ), and we are done.
□
The reader can readily verify that the proof in the theorem also goes through
using intuitionistic logic. Combining the previous results, we get the following.
Corollary 4.14. RCAω
0 + QF-AC2,1 proves [(S2) + LIND4] ↔[(∃Ξ)LIN(Ξ) + (µ2)].
Corollary 4.15. The superjump S is computable in any Ξ satisfying LIN(Ξ) and
Feferman’s µ, by a term in G¨odel’s T .
Proof. Given such Ξ, there are terms t1, t2 such that SCF(t1(Ξ, µ)) (i.e. Θ is given
by t1(Ξ, µ)), and S =2 t2(Ξ, µ). Checking the details of the proof of Theorem 4.1
and the construction of GF , we see that there is a term t3 such that GF (f) =
t3(F, f, S, µ). Since S(F) is primitive recursive in Θ(GF ), the theorem follows.
□
Finally, the presence of Ξ is not necessary if one is only interested in Π1
1-CA0. In
particular, the following version of the Lindel¨of lemma expresses that for a sequence
of open covers of Baire space, there is a sequence of countable sub-covers.
(∀Ψ0→2
(·) )(∃f (0×0)→1
(·,·)
)(∀m0)

(∀g1)(∃n0)
 g ∈[fn,mΨm(fn,m)]

.
(LINDseq)
Note that such ‘sequential’ theorems are well-studied in RM, starting with [91,
IV.2.12], and can also be found in e.g. [18, 19, 28, 29, 40]. The following corollary
was ﬁrst published in [71].
Corollary 4.16. The system ACAω
0 + LINDseq proves Π1
1-CA0.
Proof. The proof of Theorem 4.13 goes through with minor modiﬁcation. Due to
the below ‘grand claims’ based on this corollary, we do provide the proof in some
detail. First of all, by [91, V.1.4], any Σ1
1-formula can be brought into the ‘normal
form’ (∃g1)(∀n0)(f(gn) = 0), given arithmetical comprehension. Thus, suppose
ϕ(m) ∈Σ1
1 has normal form (∃g1)(∀n0)(f(gn, m) = 0) and deﬁne F 2
m as follows:
Fm(g) is n + 1 if n is minimal such that f(¯gn, m) > 0, and 0 if there is no such n.
Note that Fm is based on Ff from the theorem. Apply LINDseq for Ψ2
(·) = F(·) and
let f(·,·) be the sequence thus obtained. We deﬁne X ⊂N as follows:
X := {m0 : (∃n0)(Fm(fn,m) = 0)},
(4.3)
using (µ2).
We now prove (∀m0)(m ∈X ↔ϕ(m)), establishing the corollary.
If m ∈X, then there is g1 such that Fm(g) = 0, i.e. (∀n0)(f(gn, m) = 0) by
deﬁnition, and hence ϕ(m). Now assume ϕ(m0) for ﬁxed m0, i.e. let g0 be such
that (∀n0)(f(g0n, m0) = 0), and note that for any m0, g1, h1, if Fm(h) > 0 and
¯gFm(h) = ¯hFm(h), then Fm(g) = Fm(h). In particular, if Fm0(h) > 0, we have
g0 ̸∈[¯hFm0(h)]. Hence, if Fm0(fn,m0) > 0 for all n0, g0 is not in the covering


## Page 35


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
35
consisting of the union of [fn,m0Fm0(fn,m0)] for all n0, contradicting LINDseq. Thus,
we must have (∃n0)(Fm0(fn,m0) = 0), implying that m0 ∈X by (4.3).
□
Due to he fact that N×NN is trivially homeomorphic to NN, LINDseq is derivable
from (and hence equivalent to) LIND4, and we obtain the following result.
Corollary 4.17. The system ACAω
0 + LIND4 proves Π1
1-CA0.
Remark 4.18 (On predicativist mathematics). We have discussed the compati-
bility problem for Nelson’s predicative arithmetic (and its negative answer) in Sec-
tion 1.2.3. We now argue that Corollary 4.17 also settles the compatibility problem
for Weyl-Feferman predicative mathematics in the negative. To this end, we exhibit
two natural theorems A and B which are both acceptable in predicative mathemat-
ics but A∧B is not. In a nutshell, ATR0 is considered the ‘upper limit’ of predicative
mathematics; both RCAω
0 +LIND4 and ACAω
0 fall ‘well below’ this upper limit, while
the combination ACAω
0 +LIND4 falls ‘well above’ the upper limit. Hence, ACAω
0 and
RCAω
0 + LIND4 are acceptable in predicative mathematics, but the combination is
not: Π1
1-CA0 is even the textbook example of an impredicative system ([91, §I.12]).
A detailed discussion (including technicalities) is as follows.
First of all, we elaborate on the notion of ‘acceptable in predicative mathemat-
ics’. On one hand there is Feferman’s notion of predicative provability ([22, 25]),
which is rather limited and clumsy when dealing with ordinary mathematics, ac-
cording to Simpson ([90, p. 154]). On the other hand, the weaker notion of pred-
icative reducibility is more ﬂexible: a formal system T is predicatively reducible if
-intuitively speaking- it is not stronger than a system S which is predicatively prov-
able. Thus, while T may involve impredicative notions, the latter are ‘safe’ from
the point of view of predicative mathematics as these notions only provide as much
strength/power as S, and the latter’s ‘predicative status’ is well-known.
Secondly, Feferman and Sch¨utte have shown (independently) that the least non-
predicatively provable ordinal is Γ0 (See [25, p. 607] for details and references).
Hence, a formal system T is called predicatively reducible if its ordinal |T | satisﬁes
|T | < Γ0. Note that |ATR0| = Γ0, which motivates the status of ATR0 as the upper
limit of predicative mathematics.
Now, the proof-theoretic ordinal of RCAω
0 +
LIND4 (resp. ACAω
0 ) is ωω (resp. ε0) by Theorem 4.12 (resp. [81, Theorem 2.2]) and
[91, IX.5]. Since ωω < ε0 < Γ0, both these systems are predicatively reducible. By
contrast, the combination of these systems, namely ACAω
0 + LIND4 implies Π1
1-CA0
by Corollary 4.17, and the ordinal for the latter system is far beyond Γ0. We refer
to [91, IX.5] for background concerning the cited results and further references.
Finally, we believe there to be many purely logical statements C and D that
are predicatively reducible, while C ∧D is not. Nonetheless, to the best of our
knowledge, our result as in Corollary 4.17 is unique in that it provides two natural
theorems A and B that are predicatively reducible, while A∧B is not. As a bonus,
the proof of Theorem 4.13 also goes through using only intuitionistic logic. While
LIN4 is quite natural (and implied by Lindel¨of’s 1903 lemma), the same is not
immediately clear for (∃Ξ)LIN(Ξ), though a case can be made: Ξ is essentially a
realiser for paracompactness (as shown in [83]), and the latter seems to be essential
for proving metrisation theorems, as suggested by the results in [62, Lemma 4.10].


## Page 36


36
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
Acknowledgement 4.19. Our research was supported by the John Templeton
Foundation, the Alexander von Humboldt Foundation, LMU Munich (via the Ex-
cellence Initiative and the Center for Advanced Studies of LMU), and the Univer-
sity of Oslo. We express our gratitude towards these institutions. We thank Ulrich
Kohlenbach, Karel Hrbacek, and Anil Nerode for their valuable advice. We also
thank the anonymous referee for the helpful suggestions. Opinions expressed in this
paper do not necessarily reﬂect those of the John Templeton Foundation.
References
[1] Pascal Auscher and Lashi Bandara, Real Harmonic Analysis, ANU Press, 2010.
[2] Jeremy Avigad and Solomon Feferman, G¨odel’s functional (“Dialectica”) interpretation,
Handbook of proof theory, Stud. Logic Found. Math., vol. 137, 1998, pp. 337–405.
[3] Robert G. Bartle, Book Review: The general theory of integration, Bull. Amer. Math. Soc.
(N.S.) 29 (1993), no. 1, 136–139.
[4]
, Return to the Riemann integral, Amer. Math. Monthly 103 (1996), no. 8.
[5] Robert
G.
Bartle,
Ralph
Henstock,
Jaroslav
Kurzweil,
Eric
Schechter,
Stefan
Schwabik,
and
Rudolf
V´yborn´y,
An
open
letter,
Website:
https://math.vanderbilt.edu/schectex/ccc/gauge/letter/ (1997).
[6] Robert G. Bartle, A modern theory of integration, Graduate Studies in Mathematics, vol. 32,
American Mathematical Society, 2001.
[7] Jon Barwise (Ed.), Handbook of mathematical logic, North-Holland, 1977. Studies in Logic
and the Foundations of Mathematics, Vol. 90.
[8] Errett Bishop, Foundations of constructive analysis, McGraw-Hill, 1967.
[9] Emile Borel, Sur quelques points de la th´eorie des fonctions, Ann. Sci. ´Ecole Norm. Sup.
(3) 12 (1895), 9–55.
[10] Nicolas Bourbaki, General topology. Chapters 1–4, Springer, 1998.
[11] Douglas K. Brown, Functional analysis in weak subsystems of second-order arithmetic, PhD
Thesis, The Pennsylvania State University, ProQuest LLC, 1987.
[12] John P. Burgess, Fixing Frege, Princeton Monographs in Philosophy, Princeton University
Press, 2005.
[13] Frank E. Burk, A garden of integrals, The Dolciani Mathematical Expositions, vol. 31,
Mathematical Association of America, Washington, DC, 2007.
[14] Samuel R. Buss, Nelson’s work on logic and foundations and other reﬂections on the foun-
dations of mathematics, Diﬀusion, quantum theory, and radically elementary mathematics,
Math. Notes, vol. 47, Princeton Univ. Press, Princeton, NJ, 2006, pp. 183–208.
[15] Pierre Cousin, Sur les fonctions de n variables complexes, Acta Math. 19 (1895), 1–61.
[16] Robert J. Deltete and Reed A. Guy, Emerging from imaginary time, Synthese 108 (1996),
no. 2, 185–203.
[17] L.
P.
G.
Dirichlet,
Sur
la
convergence
des
s´eries
trigonom´etriques
qui
ser-
vent
`a
repr´esenter
une
fonction
arbitraire
entre
des
limites
donn´ees
(2008).
https://arxiv.org/abs/0806.1294.
[18] Franc.ois G. Dorais, Classical consequences of continuous choice principles from intuition-
istic analysis, Notre Dame J. Form. Log. 55 (2014), no. 1, 25–39.
[19] Franc.ois G. Dorais, Damir D. Dzhafarov, Jeﬀry L. Hirst, Joseph R. Mileti, and Paul Shafer,
On uniform relationships between combinatorial problems, Trans. Amer. Math. Soc. 368
(2016), no. 2, 1321–1359.
[20] Pierre Dugac,
Sur la correspondance
de
Borel
et
le th´eor`eme
de
Dirichlet-Heine-
Weierstrass-Borel-Schoenﬂies-Lebesgue, Arch. Internat. Hist. Sci. 39 (1989), no. 122, 69–
110.
[21] Damir D. Dzhafarov, Reverse Mathematics Zoo. http://rmzoo.uconn.edu/.
[22] Solomon Feferman, Systems of predicative analysis, J. Symbolic Logic 29 (1964), 1–30.
[23]
, In the light of logic, Logic and Computation in Philosophy, OUP, 1998.
[24]
, The signiﬁcance of Weyl’s Das Kontinuum, Proof theory (Roskilde, 1997), Synthese
Lib., vol. 292, Kluwer Acad. Publ., Dordrecht, 2000, pp. 179–194.
[25]
, Predicativity, The Oxford Handbook of the Philosophy of Mathematics and Logic,
Oxford University Press, 2005, pp. 590-624.


## Page 37


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
37
[26] Harvey Friedman, Some systems of second order arithmetic and their use, Proceedings
of the International Congress of Mathematicians (Vancouver, B. C., 1974), Vol. 1, 1975,
pp. 235–242.
[27]
, Systems of second order arithmetic with restricted induction, I & II (Abstracts),
Journal of Symbolic Logic 41 (1976), 557–559.
[28] Makoto Fujiwara, Kojiro Higuchi, and Takayuki Kihara, On the strength of marriage theo-
rems and uniformity, MLQ Math. Log. Q. 60 (2014), no. 3.
[29] Makoto Fujiwara and Keita Yokoyama, A note on the sequential version of Π1
2 statements,
The nature of computation, Lecture Notes in Comput. Sci., vol. 7921, Springer, Heidelberg,
2013, pp. 171–180.
[30] Robin Gandy, General recursive functionals of ﬁnite type and hierarchies of functions, Ann.
Fac. Sci. Univ. Clermont-Ferrand No. 35 (1967), 5–24.
[31] Russell A. Gordon, The integrals of Lebesgue, Denjoy, Perron, and Henstock, Graduate
Studies in Mathematics, vol. 4, American Mathematical Society, 1994.
[32] Mariagnese Giusto and Alberto Marcone, Lebesgue numbers and Atsuji spaces in subsystems
of second-order arithmetic, Arch. Math. Logic 37 (1998), no. 5-6, 343–362.
[33] Leo Harrington, The superjump and the ﬁrst recursively Mahlo ordinal, Generalized re-
cursion theory (Proc. Sympos., Univ. Oslo, Oslo, 1972), North-Holland, 1974, pp. 43–52.
Studies in Logic and the Foundations of Math., Vol. 79.
[34] John P. Hartley, Eﬀective discontinuity and a characterisation of the superjump, J. Symbolic
Logic 50 (1985), no. 2, 349–358.
[35] Horst Herrlich, Choice principles in elementary topology and analysis., Commentat. Math.
Univ. Carol. 38 (1997), no. 3, 545–552.
[36] David Hilbert and Paul Bernays, Grundlagen der Mathematik. II, Zweite Auﬂage. Die
Grundlehren der mathematischen Wissenschaften, Band 50, Springer, 1970.
[37] David Hilbert, David Hilbert’s lectures on the foundations of arithmetic and logic, 1917–
1933, Springer, 2013. Edited by William Ewald, Wilfried Sieg and Michael Hallett.
[38] T. H. Hildebrandt, The Borel theorem and its generalizations, Bull. Amer. Math. Soc. 32
(1926), no. 5, 423–474.
[39] Denis R. Hirschfeldt, Slicing the truth, Lecture Notes Series, Institute for Mathematical
Sciences, National University of Singapore, vol. 28, World Scientiﬁc Publishing, 2015.
[40] Jeﬀry L. Hirst and Carl Mummert, Reverse mathematics and uniformity in proofs without
excluded middle, Notre Dame J. Form. Log. 52 (2011), no. 2, 149–162.
[41] James Hunter, Higher-order reverse topology, ProQuest LLC, Ann Arbor, MI, 2008. Thesis
(Ph.D.)–The University of Wisconsin - Madison.
[42] George Jaroszkiewicz, Images of Time Mind, Science, Reality, Oxford University Press UK,
2016.
[43] John L. Kelley, General topology, Springer-Verlag, 1975. Reprint of the 1955 edition; Grad-
uate Texts in Mathematics, No. 27.
[44] Israel Kleiner, Excursions in the history of mathematics, Birkh¨auser/Springer, 2012.
[45] Peter Koellner, Strong logics of ﬁrst and second order, Bull. Symbolic Logic 16 (2010), no. 1,
1–36.
[46]
, Large Cardinals and Determinacy, The Stanford Encyclopedia of Philosophy, 2014.
https://plato.stanford.edu/archives/spr2014/entries/large-cardinals-determinacy/.
[47] Ulrich Kohlenbach, Foundational and mathematical uses of higher types, Reﬂections on the
foundations of mathematics, Lect. Notes Log., vol. 15, ASL, 2002, pp. 92–116.
[48]
, Higher order reverse mathematics, Reverse mathematics 2001, Lect. Notes Log.,
vol. 21, ASL, 2005, pp. 281–295.
[49] Tuo Yeong Lee, Henstock-Kurzweil integration on Euclidean spaces, Series in Real Analysis,
vol. 12, World Scientiﬁc, 2011.
[50] Ernst Lindel¨of, Sur Quelques Points De La Th´eorie Des Ensembles, Comptes Rendus (1903),
697–700.
[51] John Longley and Dag Normann, Higher-order Computability, Theory and Applications of
Computability, Springer, 2015.
[52] Fyodor A. Medvedev, Scenes from the history of real functions, Science Networks. Historical
Studies, vol. 7, Birkh¨auser Verlag, Basel, 1991.
[53] Antonio Montalb´an and Richard A. Shore, The limits of determinacy in second-order arith-
metic, Proc. Lond. Math. Soc. (3) 104 (2012), no. 2, 223–252.


## Page 38


38
ON THE SIGNIFICANCE OF THE UNCOUNTABLE
[54] Antonio Montalb´an, Open questions in reverse mathematics, Bull. Sym. Logic 17 (2011),
no. 3, 431–454.
[55] E. H. Moore, On a Form of General Analysis with Aplication to Linear Diﬀerential and
Integral Equations, Atti IV Cong. Inter. Mat. (Roma,1908) 2 (1909), 98–114.
[56]
, Introduction to a Form of General Analysis, The New Haven Mathematical Collo-
quium (1910), 1–150.
[57]
, Deﬁnition of Limit in General Integral Analysis, Proceedings of the National Acad-
emy of Sciences of the United States of America 1 (1915), no. 12, 628–632.
[58] E. H. Moore and H. L. Smith, A General Theory of Limits, Amer. J. Math. 44 (1922), no. 2,
102–121.
[59] P. Muldowney, A general theory of integration in function spaces, including Wiener and
Feynman integration, Vol. 153, Longman Scientiﬁc & Technical, Harlow; John Wiley, 1987.
[60] Pat Muldowney, A modern theory of random variation, Wiley & Sons, 2012.
[61] Carl Mummert and Stephen G. Simpson, Reverse mathematics and Π1
2 comprehension, Bull.
Symbolic Logic 11 (2005), no. 4, 526–533.
[62] Carl Mummert, Reverse mathematics of MF spaces, J. Math. Log. 6 (2006), no. 2, 203–232.
[63] I. P. Natanson, Theory of functions of a real variable, Frederick Ungar, 1955.
[64] E.
Nathanson,
Path
integration
with
non-positive
distributions
and
applications
to
the
Schr¨dinger
equation,
PhD
(Doctor
of
Philosophy)
thesis,
University
of
Iowa,
https://doi.org/10.17077/etd.k483ok3i. (2014).
[65] E. Nathanson and P. Jørgensen, A global solution to the Schr¨dinger equation: From Henstock
to Feynman, Journal of Mathematical Physics 56 (2015).
[66]
, Trotter’s limit formula for the Schr¨odinger equation with singular potential, Journal
of Mathematical Physics 58 (2017).
[67] Edward Nelson, Predicative arithmetic, Mathematical Notes, vol. 32, Princeton University
Press, Princeton, NJ, 1986.
[68] Dag Normann, Functionals of Type 3 as Realisers of Classical Theorems in Analysis, Pro-
ceedings of CiE18, Lecture Notes in Computer Science 10936 (2018), 318–327.
[69] Dag Normann and Sam Sanders, Nonstandard Analysis, Computability Theory, and their
connections, Submitted; arXiv: https://arxiv.org/abs/1702.06556 (2017).
[70]
, On the mathematical and foundational signiﬁcance of the uncountable, Journal for
Mathematical Logic, doi: 10.1142/S0219061319500016 (2018).
[71]
,
Uniformity
in
mathematics,
Submitted,
arXiv:
https://arxiv.org/abs/1808.09783 (2018).
[72] Salvatore Pincherle, Sopra alcuni sviluppi in serie per funzioni analitiche (1882), Opere
Scelte, I, Roma (1954), 64–91.
[73] W. N. Polyzou and Ekaterina Nathanson, Scattering using real-time path integrals, arXiv:
https://arxiv.org/abs/1712.00046 (2017).
[74] Hans Rademacher, Eineindeutige Abbildungen und Meßbarkeit, Monatsh. Math. Phys. 27
(1916), no. 1, 183–235.
[75] Michael Rathjen, The superjump in Martin-L¨of type theory, Logic Colloquium ’98 (Prague),
Lect. Notes Log., vol. 13, Assoc. Symbol. Logic, Urbana, IL, 2000.
[76]
, Ordinal notations based on a weakly Mahlo cardinal, Arch. Math. Logic 29 (1990),
no. 4, 249–263.
[77]
, The recursively Mahlo property in second order arithmetic, Math. Logic Quart. 42
(1996), no. 1, 59–66.
[78] Michael Reed and Barry Simon, Methods of modern mathematical physics. IV. Analysis of
operators, Academic Press, 1978.
[79] F. Riesz, Sur un th´eor`eme de M. Borel, Comptes rendus de l’Acad´emie des Sciences, Paris,
Gauthier-Villars 140 (1905), 224–226.
[80] Gerald E. Sacks, Higher recursion theory, Perspectives in Mathematical Logic, Springer,
1990.
[81] Nobuyuki Sakamoto and Takeshi Yamazaki, Uniform versions of some axioms of second
order arithmetic, MLQ Math. Log. Q. 50 (2004), no. 6, 587–593.
[82] Sam Sanders, The Gandy-Hyland functional and a computational aspect of Nonstandard
Analysis, Computability 7 (2018), 7-43.
[83]
, Reverse Mathematics of topology: dimension, paracompactness, and splittings,
arXiv: https://arxiv.org/abs/1808.08785 (2018), pp. 17.


## Page 39


ON THE SIGNIFICANCE OF THE UNCOUNTABLE
39
[84]
, Metastability and higher-order computability, Proceedings of LFCS18, Lecture
Notes in Computer Science 10703, Springer (2018).
[85]
, Nets and Reverse Mathematics, Submitted (2019), pp. 15.
[86] Arthur Schoenﬂies, Die Entwickelung der Lehre von den Punktmannigfaltigkeiten, Jahres-
bericht der deutschen Mathematiker-Vereinigung, vol 8,b Leipzig: B.G. Teubner, 1900.
[87]
, Entwicklungen der Mengenlehre und ihrer Anwendungen, Part I, 2nd edition,
Leipzig-Berlin (Teubner), 1913.
[88] Wilfried Sieg, Hilbert’s programs and beyond, Oxford University Press, Oxford, 2013.
[89] Waclaw Sierpi´nski, D´emonstration ´el´ementaire du th´eor`eme sur la densit´e des ensembles,
Fund. Math. 4 (1923), 167-171.
[90] Stephen G. Simpson, Friedman’s research on subsystems of second-order arithmetic, Harvey
Friedman’s research on the foundations of mathematics, Stud. Logic Found. Math., vol. 117,
North-Holland, 1985, pp. 137–159.
[91]
, Subsystems of second order arithmetic, 2nd ed., Perspectives in Logic, CUP, 2009.
[92]
, The G¨odel hierarchy and reverse mathematics., Kurt G¨odel. Essays for his centen-
nial, 2010, pp. 109–127.
[93] Charles Swartz, Introduction to gauge integrals, World Scientiﬁc, 2001.
[94] B. Thomson, J. Bruckner, and A. Bruckner, Elementary real analysis, Prentice Hall, 2001.
[95] B. Thomson, Rethinking the elementary real analysis course, Amer. Math. Monthly 114
(2007), no. 6, 469–490.
[96] Anne Sjerp Troelstra and Dirk van Dalen, Constructivism in mathematics. Vol. I, Studies
in Logic and the Foundations of Mathematics, vol. 121, North-Holland, 1988.
[97] Alan Turing, On computable numbers, with an application to the Entscheidungs-problem,
Proceedings of the London Mathematical Society 42 (1936), 230-265.
[98] Jean van Heijenoort, From Frege to G¨odel. A source book in mathematical logic, 1879–1931,
Harvard University Press, Cambridge, Mass., 1967.
[99] Guiseppe Vitali, Sui gruppi di punti e sulle funzioni di variabili reali., Atti della Accademia
delle Scienze di Torino, vol XLIII 4 (1907), 229–247.
[100] Sean Walsh, Deﬁnability aspects of the Denjoy integral, Fund. Math. 237 (2017), no. 1,
1–29.
[101] K. Weierstraß, Ausgew¨ahlte Kapitel aus der Funktionenlehre, Teubner-Archiv zur Mathe-
matik [Teubner Archive on Mathematics], vol. 9, BSB B. G. Teubner Verlagsgesellschaft,
Leipzig, 1988.
[102] Hermann Weyl, Das Kontinuum, von Veit & Comp., Leipzig, 1918.
[103] W. H. Young, Overlapping intervals, Bulletin of the London Mathematical Society 35 (1902),
384-388.
[104] W. H. Young and G. H. Young, On The Reduction Of Sets Of Intervals, Proc. Lond. Math.
Soc. 14 (1915), 111–130.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1711_08939v7_on_the_mathematical_and_foundational_significance_of_the_uncountable
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1711_08939V7_ON_THE_MATHEMATICAL_AND_FOUNDATIONAL_SIGNIFICANCE_OF_THE_UNCOUNTABLE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

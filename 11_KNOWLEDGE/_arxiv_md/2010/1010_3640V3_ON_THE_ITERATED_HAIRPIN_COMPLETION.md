---
tags: [knowledge, _arxiv_md, 2010, note, reference, arxiv]
---
arxiv_id: 1010.3640v3
source: arxiv
rscf-state: source-claim
canon-group: reference

# 1010.3640v3_On_the_Iterated_Hairpin_Completion

> Source: 1010.3640v3_On_the_Iterated_Hairpin_Completion.pdf

> Pages: 14

---


## Page 1


arXiv:1010.3640v3  [cs.FL]  9 Mar 2011
On the Iterated Hairpin Completion
Steﬀen Kopecki
kopecki@fmi.uni-stuttgart.de
University of Stuttgart, Institute for Formal Methods in Computer Science (FMI),
Universit¨atsstraße 38, D-70569 Stuttgart
August 10, 2018
Abstract
The (bounded) hairpin completion and its iterated versions are operations on formal lan-
guages which have been inspired by the hairpin formation in DNA-biochemistry. The paper
answers two questions asked in the literature about the iterated hairpin completion.
The ﬁrst question is whether the class of regular languages is closed under iterated bounded
hairpin completion. Here we show that this is true by providing a more general result which
applies to all the classes of languages which are closed under ﬁnite union, intersection with
regular sets, and concatenation with regular sets. In particular, all Chomsky classes and all
standard complexity classes are closed under iterated bounded hairpin completion.
In the second part of the paper we address the question whether the iterated hairpin
completion of a singleton is always regular. In contrast to the ﬁrst question, this one has
a negative answer. We exhibit an example of a singleton language whose iterated hairpin
completion is not regular, actually it is not context-free, but context-sensitive.
Keywords: Formal languages, Finite automata, Hairpin completion, Bounded hairpin completion
1
Introduction
The hairpin completion is an operation on formal languages which is inspired by DNA-computing
and biochemistry where it appears naturally in chemical reactions. It turned out that the corre-
sponding operation on formal languages gives rise to very interesting and quite subtle decidability
and computational problems. The focus of this paper is on these formal language theoretical
results. However, let us sketch the biochemical origin of this operation ﬁrst.
A DNA strand is a polymer composed of nucleotides which diﬀer from each other by their
bases A (adenine), C (cytosine), G (guanine), and T (thymine). For our purposes a strand can
be seen as a ﬁnite sequence of bases. By Watson-Crick base pairing two base sequences can bind
to each other if they are pairwise complementary, where A is complementary to T and C to G.
The hairpin completion is best explained by Figure 1. By a sequence w we always mean to read
w from right to left and to complement base by base, i.e., a1 · · · an = an · · · a1. During a chemical
process, called annealing, a strand which contains a sequence α and ends on the complementary
sequence α, Fig. 1(a), can form an intramolecular base-pairing which is known as hairpin (in case
α is not too short, say |α| ≥10), see Fig. 1(b). By complementing the unbound sequence γ, the
hairpin completion arises, Fig. 1(c).
Hairpin completions of strands develop naturally during a technique called Polymerase Chain
Reaction (PCR). The PCR is often used in DNA algorithms to amplify DNA strands with certain
1


## Page 2


γ
α
β
α
(a) strand
γ
α
β
α
(b) hairpin
γ
α
β
α
γ
(c) hairpin completion
Figure 1: Hairpin completion of a DNA-strand.
properties. In many algorithms which use PCR the hairpin completions are by-products which
cannot be used for the subsequent computation. Therefore, sets of strands which are unlikely
to build hairpins (or lead to other bad hybridizations) have been examined in many papers, see
e.g., [2,4,5,10,11].
On the other hand, some DNA-based computations rely on the fact that DNA strands can form
hairpins. An example are algorithms using the Whiplash PCR in which strands are designed to
build hairpins. This technique can be used to solve combinatorial problems, including NP-complete
ones like Satisfiability and Hamiltonian Path, see [6,18,19].
On an abstract level a strand can be seen as a word and a (possibly inﬁnite) set of strands is
a language. The hairpin completion of formal languages has been introduced in [1] by Cheptea,
Mart´ın-Vide, and Mitrana. In several papers the hairpin completion and some familiar operations
have been studied, see e.g., [1, 3, 14–17].
The focus of this paper is on closure properties of
language classes concerning the iterated versions of the hairpin completion and the bounded hairpin
completion. For the latter operation we assume the length of the γ-part to be bounded. This
variant of the hairpin completion was introduced and analyzed in [8, 9] by Ito, Leupold, Manea,
and Mitrana. A formal deﬁnition of both operations is given in Section 2.1.
In [1] the closure properties of diﬀerent language classes under the non-iterated and iterated
hairpin completion have been analyzed. It follows that neither regular nor context-free languages
are closed under hairpin completion whereas the family of context-sensitive languages is closed
under this function. Actually, from [1] we can derive that the class DSPACE(f) (resp. the class
NSPACE(f)) is closed under hairpin completion (resp. closed under iterated hairpin completion)
for every function f ∈Ω(log). (By the class DSPACE(f) (resp. NSPACE(f)) we mean, as usual,
the class of languages that can be accepted by a deterministic (resp. non-deterministic) Turing
machine which uses f(n) work space on input length n.) In particular, the class of context-sensitive
languages is closed under iterated hairpin completion, too. Furthermore, if we apply the iterated
hairpin completion to a regular (resp. context-free) language we stay inside NL(= NSPACE(log))
(resp. NSPACE(log2), by Lewis, Stearns, and Hartmanis [13]) which is in terms of space complexity
far below the class of deterministic context-sensitive languages.
The situation changes if we consider the bounded hairpin completion, which can be seen as a
weaker variant of the hairpin completion. All classes in the Chomsky Hierarchy are closed under
bounded hairpin completion and the classes of context-free, context-sensitive, and recursively
enumerable languages are closed under the iterated operation, see [8,9]. But the status for regular
languages remained unknown and was stated as an open problem in [9]. In Section 3 we solve
this problem. We state a general representation for the iterated bounded hairpin completion of
a formal language using the operations union, intersection with regular sets, and concatenation
with regular sets (Theorem 3.1). As a consequence all language classes which are closed under
these basic operations are also closed under iterated bounded hairpin completion.
Furthermore, for a given non-deterministic ﬁnite automaton (NFA) accepting a language L, we
give exponential lower and upper bounds for the size of an NFA accepting the iterated bounded
hairpin completion of L in Theorem 4.1. Thus, if we ignore constants, the NFA leads us to a linear
2


## Page 3


time membership test for the iterated bounded hairpin completion of a ﬁxed regular language. This
improves a quadratic bound which was known before. Indeed, the best known time complexity of
the membership problem for the iterated (unbounded) hairpin completion of a regular language
L is still quadric time by an algorithm from [14]. See Section 4 for a more detailed discussion.
The class of iterated hairpin completions of singletons (HCS) has been investigated in [17]
by Manea, Mitrana, and Yokomori (which is the journal version of a paper that appeared at
AFL 2008). Obviously, HCS is included in the class of context-sensitive languages. However,
the questions if HCS contains non-regular or non-context-free languages has been unsolved. In
Section 5 we answer this question by stating a singleton whose iterated hairpin completion is not
context-free.
This paper is the journal version of results which appeared as a poster at DLT 2010, [12].
2
Deﬁnitions and Notation
We assume the reader to be familiar with the fundamental concepts of formal language and
automata theory, see [7].
An alphabet is a ﬁnite set of letters. In this paper the alphabet is always Σ. The set of words
over Σ is denoted by Σ∗, as usual, and the empty word is denoted by ε. We consider Σ with an
involution; this is a bijection
: Σ →Σ such that a = a for all letters a ∈Σ (in DNA-biochemistry:
Σ = {A, C, G, T } with A = T and C = G). We extend the involution to words w = a1 · · · an by
w = an · · · a1. (Just like taking inverses in groups.) For a formal language L by L we denote the
language {w | w ∈L}.
Given a word w, we denote by |w| its length. For a length bound ℓ≥0 the set Σ≤ℓcontains
all words of length at most ℓ. If w = xyz for some x, y, z ∈Σ∗, then x, y, and z are called preﬁx,
factor, and suﬃx of the word w, respectively. For the preﬁx relation we also use the notation
x ≤w. Note that if z is a suﬃx of w, then z is a preﬁx of w (or z ≤w).
A common way to describe regular languages are non-deterministic ﬁnite automata (NFAs).
An NFA A is a tuple (Q, Σ, E, I, F) where Q is the ﬁnite set of states, I ⊆Q is the set of initial
states, F ⊆Q is the set of ﬁnal states, and E ⊆Q×Σ×Q is the set of labelled edges or transitions.
The language accepted by the automaton, denoted by L(A), contains all words w such that there
is a path labelled by w which leads from an initial state to a ﬁnal state. By the size of an NFA
we mean the number of states |Q|.
2.1
The Hairpin Completion
Let w ∈Σ∗be a word. If w has a factorization w = γαβα, it can form a hairpin and γαβαγ is a
right hairpin completion of w (again, see Figure 1). Since a hairpin in biochemistry is stable only
if α is long enough, we ﬁx a constant k ≥1 and ask |α| = k. (Note that the deﬁnition does not
change if we ask |α| ≥k.)
Symmetrically, if w has a factorization αβαγ with |α| = k, then γαβαγ is a left hairpin
completion of w. For the bounded hairpin completion we assume that the length of the factor γ
is bounded by some constant.
The hairpin completion of a formal language L is the union of all hairpin completions of
all words in L.
Before we state the formal deﬁnition of the unbounded and bounded hairpin
completion of a language, we introduce a more general variant of the hairpin completion, namely
the parameterized hairpin completion.
The parameterized hairpin completion covers the other
operations as special cases.
3


## Page 4


Let ℓ, r ∈N ∪{∞} be two length bounds and let L be a formal language. Considering a left
hairpin completion with the factorization γαβαγ as above, then the bound ℓlimits the length
of γ; respectively, the bound r limits the length of γ in a right hairpin completion. For a word
α ∈Σk the parameterized hairpin completion is deﬁned as
Hα(L, ℓ, 0) =
[
γ∈Σ≤ℓ
γ (αΣ∗αγ ∩L)
Hα(L, 0, r) =
[
γ∈Σ≤r
(γαΣ∗α ∩L) γ
Hα(L, ℓ, r) = Hα(L, ℓ, 0) ∪Hα(L, 0, r).
For the constant k we deﬁne
Hk(L, ℓ, r) =
[
α∈Σk
Hα(L, ℓ, r).
In the unbounded case we distinguish two operations: The (two-sided) hairpin completion is
deﬁned as Hk(L) = Hk(L, ∞, ∞) and the right-sided hairpin completion is deﬁned as RHk(L) =
Hk(L, 0, ∞). For the latter case we allow right hairpin completions, only. In the same way we
might deﬁne the left-sided hairpin completion of a language, but for convenience we will treat the
right-sided operation, only, and also refer to it as the one-sided hairpin completion. It is plain,
that our results also hold for the left-sided case.
The bounded hairpin completion H(L, m, m) arises if we choose the same ﬁnite bound m ∈N
for left and right hairpin completions.
Note that if both bounds ℓ, r are ﬁnite and L is regular, then the parameterized hairpin
completion Hk(L, ℓ, r) is regular as well. This does not hold if ℓ= ∞or r = ∞as one of the
unions becomes inﬁnite. It is known that the unbounded hairpin completion of a regular language
is not necessarily regular but always linear context-free, see e.g., [1].
In this paper we examine the iterated versions of the operations we deﬁned so far. The iterated
hairpin completion of a language L contains all words which belong to a sequence w0, . . . , wn where
w0 ∈L and where wi is a right or left hairpin completion of wi−1 and the bound r (resp. ℓ) applies
for all i such that 1 ≤i ≤n. More formal, let ℓ, r ∈N ∪{∞} and
H0
α(L, ℓ, r) = L,
Hi
α(L, ℓ, r) = Hα(Hi−1
α
(L, ℓ, r), ℓ, r),
H0
k(L, ℓ, r) = L,
Hi
k(L, ℓ, r) = Hk(Hi−1
k
(L, ℓ, r), ℓ, r)
for i ≥1. The iterated parameterized hairpin completion of L is the union
H∗
α(L, ℓ, r) =
[
i≥0
Hi
α(L, ℓ, r)
resp.
H∗
k(L, ℓ, r) =
[
i≥0
Hi
k(L, ℓ, r).
If a word z is included in Hi
k({w} , ℓ, r), we say z is an i-iterated hairpin completion of w, and
if z ∈H∗
k({w} , ℓ, r), we say z is an iterated hairpin completion of w. (It will be clear from the
context which length bounds apply.)
The iterated unbounded hairpin completions are denoted by H∗
k(L) = H∗
k(L, ∞, ∞) and
RH∗
k(L) = H∗
k(L, 0, ∞).
Example. Figure 2 shows a 3-iterated hairpin completion of αuαvα where |α| = k. In each step
the dotted part is the newly created preﬁx or suﬃx.
4


## Page 5


|α
| u
|α
|
v
|
α
|
|
α
|
u
|α
| u
|α
| v
|α
|
u
|
α
|
|
α
|
u
|
α
|
v
|
α
|
u
|
α
|
v
|
α
|
uαvαu
|
α
|
|α
| u
|α
| v
Figure 2: Example for the iterated hairpin completion.
3
The Iterated Bounded Hairpin Completion
In this section we will give a general representation for the iterated parameterized hairpin com-
pletion with ﬁnite bounds. Our main result is the proof of the following theorem which can be
found in Section 3.2.
Theorem 3.1. Let L be a formal language and ℓ, r ∈N. The iterated parameterized hairpin
completion H∗
k(L, ℓ, r) can be eﬀectively represented by an expression using L and the operations
union, intersection with regular sets, and concatenation with regular sets.
Consequentially, all language classes which are closed under these operations are also closed
under iterated parameterized hairpin completion with ﬁnite bounds, and if the closure under all
three operations is eﬀective, then the closure under iterated parameterized hairpin completion
with ﬁnite bounds is eﬀective, too; this applies to all four Chomsky classes. From [9] it is known
that the classes of context-free, context-sensitive, and recursively enumerable languages are closed
under iterated bounded hairpin completion, but the status for regular languages was unknown.
Since the iterated bounded hairpin completion is a special case of the iterated parameterized
hairpin completion with ﬁnite bounds we can answer this question now.
Corollary 3.2. Let C be a class of languages. If C is closed under union, intersection with regular
sets, and concatenation with regular sets, then C is also closed under iterated bounded hairpin
completion. Moreover, if C is eﬀectively closed under union, intersection with regular sets, and
concatenation with regular sets, then the closure under iterated bounded hairpin completion is
eﬀective.
In particular, the class of regular languages is eﬀectively closed under iterated bounded hairpin
completion.
The next two sections are devoted to the proof of Theorem 3.1. First we introduce the impor-
tant concept of α-preﬁxes.
3.1
α-Preﬁxes
Let α be a word of length k. For v, w ∈Σ∗we say v is an α-preﬁx of w if vα ≤w. We denote the
set of all α-preﬁxes of length at most ℓby
Pα(w, ℓ) = {v | vα ≤w ∧|v| ≤ℓ} .
The idea behind this notation is: For a word w ∈αΣ∗α with |w| −k ≥ℓ, r, the set of
(non-iterated) parameterized hairpin completions of w is given by
Hα({w} , ℓ, 0) = Pα(w, ℓ)w
and
Hα({w} , 0, r) = wPα(w, r).
In the following proof we are interested in α-preﬁxes of words which have α as a preﬁx. This
leads to some useful properties.
Lemma 3.3. Let α ∈Σk, ℓ∈N, and w ∈αΣ∗.
5


## Page 6


1. For all v ∈Pα(w, ℓ) we have α ≤vα.
2. For all u, v ∈Pα(w, ℓ) we have
|u| ≤|v| ⇔uα ≤vα ⇔u ∈Pα(vα, ℓ).
3. If vα is a preﬁx of some word in Pα(w, ℓ)∗α, then v ∈Pα(w, ℓ)∗.
Proof. If two words x, y are preﬁxes of w and |x| ≤|y|, then x ≤y. This yields properties 1 and
2.
For property 3 let vα ≤x1 · · · xmα where x1, . . . , xm ∈Pα(w, ℓ).
We can factorize v =
x1 · · · xi−1y such that y ≤xi for some i with 1 ≤i ≤m. By property 1 and induction, we see that
α is a preﬁx of xi+1 · · · xmα and hence yα ≤xiα ≤w which implies y ∈Pα(w, ℓ) and, moreover,
v ∈Pα(w, ℓ)∗.
3.2
Proof of Theorem 3.1
Let L be a formal language and ℓ, r ∈N. We will state a representation for H∗
k(L, ℓ, r) using L
and the operations union, intersection with regular sets, and concatenation with regular sets.
Let us begin with a basic observation. Every word w which is a hairpin completion of some
other word has a factorization w = δβδ with |δ| ≥k, therefore, the preﬁx of w of length k and the
suﬃx of w of length k are complementary. Let us call this preﬁx α, hence, we have w ∈αΣ∗α.
Every word which is a right hairpin completion of w has still the preﬁx α and since the suﬃx
of length k is complementary, it has the suﬃx α as well. For left hairpin completions we have a
symmetric argument and, by induction, every word which is an iterated hairpin completion of w
has preﬁx α and suﬃx α.
Thus, we can split up the (non-iterated) parameterized hairpin completion Hk(L, ℓ, r) into
ﬁnitely many languages Lα = Hk(L, ℓ, r) ∩αΣ∗α where α ∈Σk, and each of them has a eﬀective
representation using L and the operations union, intersection with regular sets, and concatenation
with regular sets. Moreover,
H∗
k(Lα, ℓ, r) = H∗
α(Lα, ℓ, r) ⊆αΣ∗α
and the iterated parameterized hairpin completion equals
H∗
k(L, ℓ, r) = L ∪H∗
k(Hk(L, ℓ, r), ℓ, r)
= L ∪H∗
k
 [
α∈Σk
Lα, ℓ, r

= L ∪
[
α∈Σk
H∗
α(Lα, ℓ, r).
Henceforth, let α ∈Σk be ﬁxed.
In order to prove Theorem 3.1 we will state a suitable
representation for H∗
α(Lα, ℓ, r). For the rest of the proof we will heavily rely on the fact that every
word in H∗
α(Lα, ℓ, r) has the preﬁx α and the suﬃx α. The representation is deﬁned recursively.
We have
H∗
α(Lα, 0, 0) = Lα.
By symmetry, we may assume that ℓ≥r and ℓ≥1.
We will state a representation for
H∗
α(Lα, ℓ, r) using H∗
α(Lα, ℓ−1, r) and the operations union, intersection with regular sets, and
concatenation with regular sets. Therefore, consider a word
z ∈H∗
α(Lα, ℓ, r) \ H∗
α(Lα, ℓ−1, r).
6


## Page 7


For some n ≥1 there is a sequence w0, . . . , wn = z where w0 ∈Lα and for all i such that
1 ≤i ≤n either wi is a left hairpin completion of wi−1 and |wi| ≤|wi−1| + ℓor wi is a right
hairpin completion of wi−1 and |wi| ≤|wi−1| + r. Furthermore, there is an index j ≥1 such that
wj−1 = w ∈H∗
α(Lα, ℓ−1, r) and wj = vw /∈H∗
α(Lα, ℓ−1, r). Note that this implies |v| = ℓand
w ∈αΣ∗αv. Let s = n −j and consider the factorization
z = xs · · · x1vwy1 · · · ys
where xi · · · x1vwy1 · · · yi = wj+i and either
1. yi = ε, |xi| ≤ℓ, and xiα ≤yi−1 · · · y1vα or
2. xi = ε, |yi| ≤r, and yiα ≤xi−1 · · · x1vα.
for all i such that 0 ≤i ≤s.
The crucial point is that vw has the preﬁx vα, the suﬃx αv, and |v| = ℓ≥r. Therefore, the
factors x1, . . . , xs and y1, . . . , ys are controlled by the triple (v, ℓ, r) in the following way.
Lemma 3.4. xi ∈Pα(vα, ℓ)∗and yi ∈Pα(vα, r)∗for all i such that 1 ≤i ≤s.
Proof. We prove the claim by induction on i. Let i such that 1 ≤i ≤s. Our induction hypothesis
is xj ∈Pα(vα, ℓ)∗and yj ∈Pα(vα, r)∗for all j such that 1 ≤j < i. We distinguish between the
two cases above:
1. We have yi = ε ∈Pα(vα, r)∗and, by induction hypothesis,
xiα ≤yi−1 · · · y1vα ∈Pα(vα, r)∗vα ⊆Pα(vα, ℓ)∗α.
In combination with Lemma 3.3 this yields xi ∈Pα(vα, ℓ)∗.
2. We have xi = ε ∈Pα(vα, ℓ)∗and
yiα ≤xi−1 · · · x1vα ∈Pα(vα, ℓ)∗α,
hence yi ∈Pα(vα, ℓ)∗. Since |yi| ≤r, all factors of yi are at most of length r, too, and
yi ∈Pα(vα, r)∗.
For u ∈Σℓlet us deﬁne the language
Lα(u, ℓ, r) = Pα(uα, ℓ)∗u (H∗
α(Lα, ℓ−1, r) ∩αΣ∗αu) Pα(uα, r)
∗.
Note that, by induction, for every u the representation for Lα(u, ℓ, r) is eﬀectively given. By
Lemma 3.4, the word z is included in Lα(v, ℓ, r) and for every word z′ ∈H∗
α(Lα, ℓ, r) \ H∗
α(Lα, ℓ−
1, r) it exists v′ ∈Σℓsuch that z′ ∈Lα(v′, ℓ, r). Therefore,
H∗
α(Lα, ℓ, r) ⊆H∗
α(Lα, ℓ−1, r) ∪
[
u∈Σℓ
Lα(u, ℓ, r)
and for the right hand side we have an eﬀective representation. Of course, we intend to replace
the inclusion by an equality sign.
Lemma 3.5. Lα(u, ℓ, r) ⊆H∗
α(Lα, ℓ, r) for all u ∈Σℓ.
7


## Page 8


Proof. We start by proving a special case of the claim that is successfully used later to derive the
result. Consider a word w′ together with the factorization
w′ = xm · · · x1wy1 · · · yn
with m ≥0, n ≥1 and where for some word u ∈Σ∗
1. w ∈H∗
α(Lα, ℓ, r) ∩uαΣ∗αu,
2. x1, . . . , xm ∈Pα(uα, ℓ),
3. y1, . . . , yn ∈Pα(uα, r), and
4. m = 0 or |yj| ≤|xm| for all j such that 1 ≤j ≤n.
We claim w′ ∈H∗
α(Lα, ℓ, r), too. Indeed, if m = 0, it is plain that w′ is an n-iterated right hairpin
completion of w. Otherwise xm · · · x1w is an m-iterated left hairpin completion of w. By the
fourth property and Lemma 3.3, we have y1, . . . , yn ∈Pα(xmα, r). Hence, w′ is an n-iterated
right hairpin completion of xm · · · x1w and we conclude w′ ∈H∗
α(Lα, ℓ, r).
Now, let u ∈Σℓand z ∈Lα(u, ℓ, r). There is a factorization
z = xs · · · x1wy1 · · · yt
where
1. w ∈u (H∗
α(L, ℓ−1, r) ∩αΣ∗αu) ⊆H∗
α(Lα, ℓ, r) ∩uαΣ∗αu,
2. x1, . . . , xs ∈Pα(uα, ℓ), and
3. y1, . . . , yt ∈Pα(uα, r).
If t = 0, the word z is an s-iterated left hairpin completion of w. Otherwise, let n ≥1 be the
maximal index such that |yn| ≥|yj| for all 1 ≤j ≤t, and let m be the maximal index such that
|yn| ≤|xm| or 0 if no such index exists. Let w′ = xm · · · x1wy1 · · · yn. Note that w′ satisﬁes the
conditions of the special case we discussed above and hence w′ ∈H∗
α(Lα, ℓ, r).
With u′ = yn we obtain
z = xs · · · xm+1w′yn+1 · · · yt
where, by the choice of n, m and by Lemma 3.3,
1. w′ ∈H∗
α(Lα, ℓ, r) ∩u′αΣ∗αu′,
2. xm+1, . . . , xs ∈Pα(u′α, ℓ), and
3. yn+1, . . . , yt ∈Pα(u′α, r).
At this point we may continue inductively and deduce z ∈H∗
α(Lα, ℓ, r).
The previous lemma tells us, if ℓ≥r, the iterated parameterized hairpin completion of Lα can
be represented by
H∗
α(Lα, ℓ, r) = H∗
α(Lα, ℓ−1, r) ∪
[
u∈Σℓ
Lα(u, ℓ, r).
Symmetrically, if r > ℓ, let us deﬁne
Rα(u, ℓ, r) = Pα(uα, ℓ)∗(H∗
α(Lα, ℓ, r −1) ∩uαΣ∗α) uPα(uα, r)
∗.
8


## Page 9


The iterated parameterized hairpin completion of Lα can be represented by
H∗
α(Lα, ℓ, r) = H∗
α(Lα, ℓ, r −1) ∪
[
u∈Σr
Rα(u, ℓ, r).
We conclude, the iterated parameterized hairpin completion of a language L can be repre-
sented by an expression using L and the operations union, intersection with regular sets, and
concatenation with regular sets.
4
The size of NFAs accepting iterated parameterized hair-
pin completions
Let L be a regular language and ℓ, r ∈N be ﬁnite bounds. In this section we analyze the size of
NFAs accepting the iterated parameterized hairpin completion H∗
k(L, ℓ, r) with respect to the size
of an NFA accepting L and the bounds ℓand r. By the size of an NFA we mean its number of
states. Recall that k is treated as a constant. (Assuming k ≤ℓor k ≤r would induce the same
complexity, but this is not shown here.) Our results are the following.
Theorem 4.1.
1. Let m ≥1. There is a regular language L such that neither the language Hk(L, m, m) nor
the language H∗
k(L, m, m) can be detected by an NFA with less than 2m states.
2. Let L be a regular language which is accepted by an NFA of size n. Let ℓ, r ∈N and let
m = max {ℓ, r}. There is an NFA accepting the iterated parameterized hairpin completion
H∗
k(L, ℓ, r) whose size is in 2O(m2)n.
Proof of 1. Let Σ = {a, a, b, b, c, c} and L = c{a, b}∗akak.
For any word w ∈L there is no
possibility of building a left hairpin and the only possible right hairpin is to bind the suﬃx ak to
ak if |w| ≤m + 2k. Therefore, we have
Hk(L, m, m) =
[
v∈{a,b}≤m−1
cvakakvc.
Now let w = cvakakvc with v ∈{a, b}≤m−1. The only way to build a hairpin is to bind its
preﬁx to its suﬃx, hence
H∗
k(L, m, m) = L ∪Hk(L, m, m).
We claim that an NFA accepting Hk(L, m, m) or H∗
k(L, m, m) has a size of at least 2m. We
prove the claim for the language Hk(L, m, m); the argumentation for H∗
k(L, m, m) is exactly the
same.
Consider an NFA accepting Hk(L, m, m) and let Q denote its set of states. For a word u ∈Σ∗we
denote by P(u) ⊆Q the set of states which are reachable from an initial state with a path labelled
by u. Now let v ∈{a, b}≤m−1. Since cvakakvc ∈Hk(L, m, m), there is a state q ∈P(cvakak) such
that a path from q to a ﬁnal state exists which is labelled by vc. For all words u ∈{a, b}≤m−1
with u ̸= v the state q does not belong to P(cuakak) because cuakakvc /∈Hk(L, m, m). Each
word v ∈{a, b}≤m−1 yields such a state q, they are mutually diﬀerent, and none of them is an
initial state (as vc /∈Hk(L, m, m)). Therefore, the number of states |Q| has to be greater than
{a, b}≤m−1 = 2m −1.
9


## Page 10


In order to prove the second claim of Theorem 4.1 we implicitly use some well-known construc-
tions of NFAs which accept concatenation, union, or intersection of regular languages. Consider
two NFAs which accept the languages L1, L2 and which are of size n1, n2, respectively. There is
an NFA accepting the concatenation L1L2 which is of size n1 + n2, an NFA accepting the union
L1 ∪L2 which is of size n1 + n2, and an NFA accepting the intersection L1 ∩L2 which is of size
n1 · n2. For details on how these NFAs are constructed see, e.g., [7].
Proof of 2. Let L be a regular language which is accepted by an automaton of size n and let
ℓ, r ∈N. The parameterized hairpin completion of L is given by
Hk(L, ℓ, r) =
[
α∈Σk
[
γ∈Σ≤ℓ
γ(αΣ∗αγ ∩L) ∪
[
α∈Σk
[
γ∈Σ≤r
(γαΣ∗α ∩L)γ.
For γ, α ∈Σ∗there is an NFA accepting γ(αΣ∗αγ ∩L) which has a size in O(|γα| · n). Hence, the
parameterized hairpin completion of L can be accepted by an NFA which has a size in O(|Σ|m m ·
n) ⊆2O(m)n where m = max {ℓ, r}.
For α ∈Σk the language Lα = Hk(L, ℓ, r) ∩αΣ∗α can also be accepted by an NFA which has
a size in 2O(m)n. Let Ni,j denote the minimal size of an NFA accepting H∗
α(Lα, i, j) for i, j ∈N.
Since Hk(Lα, 0, 0) = Lα, we have N0,0 ∈2O(m)n. For i ≥j let us recall that
H∗
α(Lα, i, j) = H∗
α(Lα, i −1, j) ∪
[
u∈Σi
Lα(u, i, j),
Lα(u, i, j) = Pα(uα, ℓ)∗u (H∗
α(Lα, i −1, j) ∩αΣ∗αu) Pα(uα, r)
∗.
The size of a minimal NFA accepting Lα(u, i, j) is in O(i · Ni−1,j) whence
Ni,j ∈O(|Σ|i i · Ni−1,j) ⊆2O(i)Ni−1,j.
Symmetrically, for j > i we have Ni,j ∈2O(i)Ni,j−1. By unfolding the recursion we obtain
Nℓ,r ∈
ℓ
Y
i=1
2O(i) ·
r
Y
j=1
2O(j) · 2O(m)n =
m
Y
i=1
2O(i) · n = 2O(Pm
i=1 i)n = 2O(m2)n.
Now, the iterated parameterized hairpin completion is given by
H∗
k(L, ℓ, r) = L ∪
[
α∈Σk
H∗
α(Lα, ℓ, r).
and there is an NFA accepting H∗
k(L, ℓ, r) which has a size in O(Nℓ,r + n) ⊆2O(m2)n.
Statement 2 of Theorem 4.1 also yields an algorithm to solve the membership problem for the
iterated bounded hairpin completion of a regular language.
Corollary 4.2. Let L be a regular language, given by an NFA of size n, and let ℓ, r ∈N. The
problem whether an input word w belongs to H∗
k(L, ℓ, r) can be decided in linear time c · |w|, where
the constant c depends on the size n and the bounds ℓ, r. More precisely, for m = max{ℓ, r} we
have c ∈2O(m2)n2.
Proof. Following the proof of Statement 2 of Theorem 4.1, we can construct an NFA A =
(Q, Σ, E, I, F) accepting the iterated hairpin completion H∗
k(L, ℓ, r) which is of a size in 2O(m2)n.
10


## Page 11


Let us denote the size of this NFA by N. Note that the construction can be preformed in time
O(|E|) ⊆O(N 2) ⊆2O(m2)n2.
The input w can be accepted by an online power-set construction of the NFA A: We start with
the set of states P0 = I. When we read the i-th letter a of the input w we construct the set Pi by
following all outgoing edges of states in Pi−1 which are labelled by a. As every state in Pi−1 has
at most N outgoing edges labelled by a, one step can be performed in O(N 2) ⊆2O(m2)n2 time.
The algorithm stops after w is read and P|w| is computed. The input w belongs to H∗
k(L, ℓ, r) if
and only if P|w| contains a ﬁnal state from F.
So far, the best known time complexity of the membership problem for the iterated (un-
bounded) hairpin completion of a regular language L is quadratic with respect to the length of
the input word, by an algorithm from [14]. This algorithm can easily be adapted to solve the
membership problem for the iterated bounded hairpin completion in quadratic time. Hence, if
we measure the time complexity with respect to the length of the input word only, we have an
improvement from quadratic to linear time (in the bounded case).
5
The Iterated Hairpin Completion of Singletons
The class of iterated hairpin completions of singletons is deﬁned as
HCSk = {H∗
k({w}) | w ∈Σ∗} .
We solve the problem whether HCSk includes non-regular or non-context-free languages which
was asked in [17]. Furthermore, we will show that the result also holds if we consider the iterated
one-sided hairpin completion.
Let us recall that, as we are treating the unbounded hairpin completion now, for the usual
factorization γαβαγ of a hairpin completion, the length of the factor γ is not bounded by a
constant anymore. By the results of the previous section it is obvious, that the possibility of
creating arbitrary long preﬁxes and suﬃxes plays an essential role in following proof.
Theorem 5.1. The iterated one- and two-sided hairpin completions of a singleton are in NL but
not context-free, in general.
Proof. The membership to NL follows by the fact that NL is closed under iterated bounded hairpin
completion, which has been proved in [1]. For convenience, we give a sketch of the proof, here.
Consider a language L ∈NL. The iterated hairpin completion H∗
k(L) can be accepted by a
non-deterministic Turing machine that works as follows. We use two pointers i and j which mark
the beginning and the end of a factor of the input w, respectively. By w(i, j) we denote the factor
beginning at position i and ending at position j.
1. We start with i = 1 and j = |w|.
2. Non-deterministically either continue with step 3 or skip to step 5.
3. Either guess i′ such that i < i′ < j and verify that w(i, j) is a left hairpin completion of
w(i′, j) or guess j′ such that i < j′ < j and verify that w(i, j) is a right hairpin completion
of w(i, j′). If the veriﬁcation is successful, continue with i = i′ (resp. j = j′).
4. Repeat step 2.
5. Accept if and only if w(i, j) ∈L.
11


## Page 12


Obviously, this Turing machine accepts H∗
k(L). In order to perform step 1-4, we only have to
store some pointers on the input word; this can be done in log |w| space. Since L ∈NL step 5 can
be performed in log |w| space, too, and hence H∗
k(L) ∈NL.
For the one-sided hairpin completion RHk(L) we can use almost the same algorithm. The only
diﬀerence is that the pointer i always is 1.
Now, let Σ = {a, a, b, b, c, c}, α = ak, and
w = αbαααcα.
We will prove that H∗
k({w}) and RH∗
k({w}) are not context-free.
Since context-free languages are closed under intersection with regular languages, it suﬃces
to show for a regular language R that the intersections R ∩H∗
k({w}) and R ∩RH∗
k({w}) are not
context-free. Let u = bα and v = ααbα. Note that uα ≤vα ≤w. Deﬁne
R = wu+vu+wu+w
and consider a word z ∈R:
z = αbαααcα
|
{z
}
w
(bα)r
| {z }
ur
ααbα
| {z }
v
(αb)s
| {z }
us
αcαααbα
|
{z
}
w
(αb)t
| {z }
ut
αcαααbα
|
{z
}
w
with r, s, t ≥1. At ﬁrst, note that w is a preﬁx of z and it does not occur as another factor in
z (there is only one c in z). Thus, if z belongs to H∗
k({w}), it must be an iterated right hairpin
completion of w and hence
R ∩H∗
k({w}) = R ∩RH∗
k({w}).
Next, we will show that z is an iterated hairpin completion of w if and only if r = s = t. The
proof is a straight forward construction of z. We try to ﬁnd a sequence w = w0, w1, . . . , wn = z
for some n ≥0 where wi ̸= wi−1 is a right hairpin completion of wi−1 for 1 ≤i ≤n. This implies
that every wi is a preﬁx of z.
Fortunately, for each of the words w0, . . . , wr+1 there is exactly one choice which satisﬁes these
conditions:
w0 = w
= αbαααcα
w1 = wu
= αbαααcαbα
w2 = wu2
= αbαααcα(bα)2
...
...
wr = wur
= αbαααcα(bα)r
wr+1 = wurv = αbαααcα(bα)rααbα
If s ̸= r, none of the right hairpin completions of wr+1 is a preﬁx of z (except for wr+1 itself).
Otherwise, we ﬁnd exactly one right hairpin completion which satisﬁes the conditions:
wr+2 = wurvurw = αbαααcα(bα)rααbα(αb)rαcαααbα.
The argument for the last step is the same. If and only if t = r, we ﬁnd a preﬁx of z which is
a right hairpin completion of wr+2 and this is wr+3 = z.
12


## Page 13


We conclude z is an iterated hairpin completion of w if and only if r = s = t and hence
R ∩H∗
k({w}) = {wurvurwurw | r ≥1} .
The intersection R ∩H∗
k({w}) belongs to a family of context-sensitive languages which are well
known to be non-context-free. From this it follows that H∗
k({w}) and RH∗
k({w}) are non-context-
free, too.
6
Final Remarks and Open Problems
We proved that language classes which have very basic closure properties are closed under iterated
bounded hairpin completion. With the techniques used in our proof we obtain a better insight
on the structure of the iterated bounded hairpin completion.
This might help to design new
algorithms which decide the membership of a word to the iterated bounded hairpin completion of
a given language and also for the unbounded version since for a given word there is an implicit
given length bound.
Another interesting problem regarding the hairpin completion is whether the iterated hairpin
completion of two languages have a common element. Even for two given singletons it is not
known, if this problem is decidable at all, see [17]. The result of Section 5 proves that this is a
non-trivial question. However, in the bounded case we can decide this problem for two regular
languages now. We just need to create the NFAs and test whether the intersection is empty. As
the size of the NFAs is quite large with respect to the length bounds, this does not seem to be the
best way to decide the problem.
We proved the existence of non-context-free languages in the language class HCS. Here, two
new questions arise naturally:
1. Does a singleton exist whose iterated hairpin completion is context-free but not regular?
2. Can we decide for a given singleton whether its iterated hairpin completion is non-regular
(or non-context-free)?
References
[1] D. Cheptea, C. Mart´ın-Vide, and V. Mitrana. A new operation on words suggested by DNA
biochemistry: Hairpin completion. Transgressive Computing, pages 216–228, 2006.
[2] R. Deaton, R. Murphy, M. Garzon, D. Franceschetti, and S. Stevens. Good encodings for
DNA-based solutions to combinatorial problems. Proc. of DNA-based computers DIMACS
Series, 44:247–258, 1998.
[3] V. Diekert, S. Kopecki, and V. Mitrana. On the hairpin completion of regular languages.
In M. Leucker and C. Morgan, editors, ICTAC, volume 5684 of Lecture Notes in Computer
Science, pages 170–184. Springer, 2009.
[4] M. Garzon, R. Deaton, P. Neathery, R. Murphy, D. Franceschetti, and E. Stevens.
On
the encoding problem for DNA computing. The Third DIMACS Workshop on DNA-Based
Computing, pages 230–237, 1997.
[5] M. Garzon, R. Deaton, L. Nino, S. Stevens Jr., and M. Wittner. Genome encoding for DNA
computing. Proc. Third Genetic Programming Conference, pages 684–690, 1998.
13


## Page 14


[6] M. Hagiya, M. Arita, D. Kiga, K. Sakamoto, and S. Yokoyama. Towards parallel evaluation
and learning of boolean µ-formulas with molecules. In Second Annual Genetic Programming
Conf., pages 105–114, 1997.
[7] J. E. Hopcroft and J. D. Ulman. Introduction to Automata Theory, Languages and Compu-
tation. Addison-Wesley, 1979.
[8] M. Ito, P. Leupold, F. Manea, and V. Mitrana. Bounded hairpin completion. Information
and Computation, In Press, Accepted Manuscript:–, 2010.
[9] M. Ito, P. Leupold, and V. Mitrana. Bounded hairpin completion. In LATA ’09: Proceedings
of the 3rd International Conference on Language and Automata Theory and Applications,
pages 434–445, Berlin, Heidelberg, 2009. Springer-Verlag.
[10] L. Kari, S. Konstantinidis, E. Losseva, P. Sos´ık, and G. Thierrin. Hairpin structures in DNA
words. In A. Carbone and N. A. Pierce, editors, DNA, volume 3892 of Lecture Notes in
Computer Science, pages 158–170. Springer, 2005.
[11] L. Kari, K. Mahalingam, and G. Thierrin. The syntactic monoid of hairpin-free languages.
Acta Inf., 44(3-4):153–166, 2007.
[12] S. Kopecki. On the iterated hairpin completion. In Y. Gao, H. Lu, S. Seki, and S. Yu, editors,
Developments in Language Theory, volume 6224 of Lecture Notes in Computer Science, pages
438–439. Springer Berlin / Heidelberg, 2010.
[13] P. M. Lewis, R. E. Stearns, and J. Hartmanis. Memory bounds for recognition of context-free
and context-sensitive languages. In Proceedings of the 6th Annual Symposium on Switching
Circuit Theory and Logical Design (SWCT 1965), FOCS ’65, pages 191–202, Washington,
DC, USA, 1965. IEEE Computer Society.
[14] F. Manea, C. Mart´ın-Vide, and V. Mitrana. On some algorithmic problems regarding the
hairpin completion. Discrete Applied Mathematics, 157(9):2143–2152, 2009.
[15] F. Manea and V. Mitrana. Hairpin completion versus hairpin reduction. In S. B. Cooper,
B. L¨owe, and A. Sorbi, editors, CiE, volume 4497 of Lecture Notes in Computer Science,
pages 532–541. Springer, 2007.
[16] F. Manea, V. Mitrana, and T. Yokomori. Two complementary operations inspired by the
DNA hairpin formation: Completion and reduction. Theor. Comput. Sci., 410(4-5):417–425,
2009.
[17] F. Manea, V. Mitrana, and T. Yokomori. Some remarks on the hairpin completion. Int. J.
Found. Comput. Sci., 21(5):859–872, 2010.
[18] K. Sakamoto, D. Kiga, K. Komiya, H. Gouzu, S. Yokoyama, S. Ikeda, and M. Hagiya. State
transitions by molecules, 1998.
[19] E. Winfree. Whiplash PCR for O(1) computing. In University of Pennsylvania, pages 175–
188, 1998.
14

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

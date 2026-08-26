---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1108.2427v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1108.2427v1_Deciding_Regularity_of_Hairpin_Completions_of_Regular_Languages_in_Polynomial_Ti

> Source: 1108.2427v1_Deciding_Regularity_of_Hairpin_Completions_of_Regular_Languages_in_Polynomial_Ti.pdf

> Pages: 28

---


## Page 1


arXiv:1108.2427v1  [cs.FL]  11 Aug 2011
Deciding Regularity of Hairpin Completions of
Regular Languages in Polynomial Time
Volker Diekert
Steﬀen Kopecki
Victor Mitrana
Abstract
The hairpin completion is an operation on formal languages that has
been inspired by the hairpin formation in DNA biochemistry and by DNA
computing. In this paper we investigate the hairpin completion of regular
languages.
It is well known that hairpin completions of regular languages are
linear context-free and not necessarily regular. As regularity of a (lin-
ear) context-free language is not decidable, the question arose whether
regularity of a hairpin completion of regular languages is decidable. We
prove that this problem is decidable and we provide a polynomial time
algorithm.
Furthermore, we prove that the hairpin completion of regular lan-
guages is an unambiguous linear context-free language and, as such, it
has an eﬀectively computable growth function. Moreover, we show that
the growth of the hairpin completion is exponential if and only if the
growth of the underlying languages is exponential and, in case the hair-
pin completion is regular, then the hairpin completion and the underlying
languages have the same growth indicator.
Keywords: Hairpin completion, regular languages and ﬁnite automata,
unambiguous linear languages, rational growth
1
Introduction
A DNA strand can be seen as a word over the four-letter alphabet {A, C, G, T}
where the letters represent the nucleobases Adenine, Cytosine, Guanine, and
Thymine, respectively. By Watson-Crick base pairing two strands may bond
to each other if they have opposite orientation and their bases are pairwise
complementary, where A is complementary to T and C to G; see Fig. 1 for
a graphic example.
Throughout the paper we use the bar-notation for the
Watson-Crick complement and its language theoretic pendant, i. e., A = T and
C = G. For base sequences (or words) we let a1 · · · am = am · · · a1; thus,
is an
antimorphic involution.
The polymerase chain reaction (PCR) is an technique which is often used
in DNA computing to amplify a template strand or a fragment of the template
strand. Short DNA sequences, so-called primers, bond to a part of the template
1


## Page 2


5′
C
G
G
T
T
T
C
A
T
C
A
3′
3′
G
C
C
A
A
A
G
T
A
G
T
5′
Figure 1: Bonding of two strands: The strands are base-wise complementary and
the ﬁrst strand has 5′-to-3′ orientation whereas the second strand has 3′-to-5′
orientation.
and thusly select where the extension, the process where template is comple-
mented, will start.
The hairpin completion of a strand can naturally develop during the PCR.
Suppose a strand σ can be written as σ = γαβα. Therefore, its suﬃx α can
act as a primer to the strand and form an intramolecular base-pairing which
is known as hairpin formation. After the extension process we obtain a new
strand γαβαγ which we call a hairpin completion of σ; see Fig. 2. Referring to
[27], α should consist of at least 9 bases, otherwise the bond between α and α
is too weak.
γ
α
β
α
γ
α
β
α
γ
extension
γ
α
β
α
γ
hairpin completion
Figure 2: Hairpin completion of a strand or a word.
Hairpin completions are often seen as undesirable byproducts that occur
during DNA computations and, therefore, sets of DNA strands have been in-
vestigated that do not tend to form hairpins or other undesired hybridizations,
see e. g., [4, 7, 8, 13, 14] and the references within. On the other hand, DNA
algorithms have been designed that make good use of hairpins and hairpin com-
pletions. For example, the whiplash PCR is a technique where a single DNA
strand computes one run of a non-deterministic GOTO-machine by repetitive
hairpin completions, where the length of the extended part is controlled by stop-
per sequences. Starting with a huge set of strands, all runs of such a machine
can be computed in parallel. Whiplash PCR can be used to solve NP-complete
problems like the Hamiltonian path problem [10, 24, 28].
Motivated by the hairpin formation in biochemistry, the hairpin completion
of formal languages has been introduced in 2006 by Cheptea, Mart´ın-Vide, and
2


## Page 3


Mitrana [3]. This paper continues the investigation of hairpin formation from
a purely formal language theoretical viewpoint. The hairpin completion of lan-
guages L1 and L2 contains all right hairpin completions (as in Fig. 2) of all words
in L1 and all left hairpin completions (a word αβαγ is extended to the left by
γ) of all words in L2. A formal deﬁnition of this operation is given in Sect. 2.1.
The hairpin completion and some related operations have been investigated in
a series of papers, see e. g., [12, 16, 18, 19, 20, 21, 22].
It is known from [3] that the hairpin completion of regular languages is not
necessarily regular but it is always linear context-free. As regularity of a linear
context-free language (given as grammar) is undecidable, the question arose if
regularity of the hairpin completion of regular languages can be decided. This
question was ﬁrst posed in 2006 [3]. We answered this question positively at
ICTAC 2009 [6] when we proved that the problem is decidable in polynomial
time. In this ﬁrst approach we were not precise about the degree of the polyno-
mial; it was about 20. In a later approach, which was presented at CIAA 2010
[5], we improved the decision algorithm and provided, that the problem is solv-
able in O(n8), where n bounds the size of the two input DFAs (deterministic
ﬁnite automata), accepting L1 and L2, respectively. Furthermore, for L2 = ∅
we provided a time complexity of O(n2) and for L1 = L2 we provided O(n6).
In the second paper we also showed that the problem is NL-complete (NL is
the class of problems that are solvable by a non-deterministic algorithm using
logarithmic space), in particular, the problem is contained in Nick’s Class which
means it is eﬃciently solvable in parallel, see e. g., [23]. Moreover, we proved
that the hairpin completion of regular languages has an unambiguous linear rep-
resentation. Thus, its generating function is an eﬀectively computable rational
function.
This paper is organized as follows. In Sect. 2, we formally deﬁne the hairpin
completion operation, we lay down our notation, and we brieﬂy introduce the
concepts of formal language theory that we will use later. Then, we start our
investigation of hairpin completions of regular languages, in Sect. 3, by providing
an unambiguous linear grammar generating the hairpin completion of two given
regular languages. Sect. 4 is devoted to the polynomial time algorithm that
decides the regularity of the hairpin completion of regular languages. In the ﬁnal
chapter, Sect. 5, we discuss the relation of the growth of the hairpin completion
with the growths of the underlying regular languages.
This paper is the journal version of results that have been presented at
ICTAC 2009. It uses the improvements which were presented at CIAA 2010
and it contains some additional results.
2
Preliminaries and Notation
We assume the reader to be familiar with the fundamental concepts of formal
language theory and automata theory, see [11].
By Σ we denote a ﬁnite alphabet with at least two letters which is equipped
with an involution
: Σ →Σ. An involution for a set is a bijection such that
3


## Page 4


a = a for all a ∈Σ. (In a biological setting we may think of Σ = {A, C, G, T }
with A = T and C = G.)
We extend this involution to words a1 · · · an by
a1 · · · an = an · · · a1. (Just like taking inverses in groups.) For languages L
denotes the set {w | w ∈L}. The set of words over Σ is denoted Σ∗; and the
empty word is denoted by 1. By Σ≤m we mean the set of all words with length
at most m.
Given a word w, we denote by |w| its length, by w[i] ∈Σ its i-th letter, and
by w[i, j] we mean w[i]w[i + 1] · · · w[j]. If w = xyz for some x, y, z ∈Σ∗, then x
and z are called preﬁx and suﬃx, respectively. A preﬁx or suﬃx x of w is said
to be proper if x ̸= w. The (proper) preﬁx relation between words x and w is
denoted by x ≤w (respectively, x < w).
2.1
Haiprin completion
Let L1 and L2 be languages in Σ∗. By κ we denote a (small) constant that
gives a lower bound for the length of primers. We deﬁne the hairpin completion
Hκ(L1, L2) by
Hκ(L1, L2) = {γαβαγ | (γαβα ∈L1 ∨αβαγ ∈L2) ∧|α| ≥κ} .
Three cases are of main interest:
1.) L1 = L2,
2.) L1 = L2, and
3.) L1 = ∅or L2 = ∅.
Compared to the deﬁnition of the hairpin completion in [3, 21] case 1 corresponds
to the the two-sided hairpin completion and case 3 to the one-sided hairpin
completion.
In many biochemical applications a strand and its complement
always co-occur, thus, the assumption L1 = L1 = L2 is natural, too, and it is a
covered by case 2.
2.2
Linear Context-free Grammars and Unambiguity
A grammar G is a tuple G = (V, Σ, P, S) where V is the ﬁnite set of non-
terminals, Σ is the alphabet (the set of terminals), P is the ﬁnite set of pro-
duction rules, and S ⊆V is the set of axioms. (Note that we allow a set of
axioms rather than the more usual restriction to have exactly one axiom S.) A
grammar is called context-free, if every rule in P is of the form A →w where
A ∈V and w ∈(V ∪Σ)∗; a grammar is called linear context-free, or simply
linear, if, in addition, w contains at most one non-terminal. For a context-free
grammar G, a derivation step is denoted by uAv =⇒
G
uwv, where A →w is a
production rule in P and u, v ∈(V ∪Σ)∗. By
∗
=⇒
G , we denote the reﬂexive and
4


## Page 5


transitive closure of =⇒
G
and we call u
∗
=⇒
G v (with u, v ∈(V, Σ)∗) a derivation.
The language generated by G is the set of terminal words
L(G) =
n
w ∈Σ∗ ∃A ∈S : A
∗
=⇒
G w
o
.
A linear grammar G is said to be unambiguous if for every word w ∈L(G),
there is exactly one derivation A
∗
=⇒
G w where A ∈S; in particular, there is only
one axiom A that derivates w. (For general context-free grammars we would
require that there is exactly one left-most derivation A
∗
=⇒
G
w; but in case of
linear grammars, these deﬁnitions coincide.)
A language L is called (unambiguous) linear if it is generated by an (unam-
biguous) linear grammar.
2.3
Generating Functions
For a profound discussion of formal power series and how the growth of regular
and unambiguous linear languages can be calculated we refer to [1, 2, 9, 17].
We content ourselves with a few basic facts. The growth or generating function
gL of a formal language L is deﬁned as
gL(z) =
X
m≥0
|L ∩Σm| zm.
We can view gL as a formal power series or as an analytic function in one
complex variable where the radius of convergence is strictly positive. The radius
of convergence is at least 1/ |Σ|.
It is well-known that the growth of a regular language L is eﬀectively rational,
i. e., it is a quotient of two polynomials, which can be eﬀectively calculated. The
same is true for unambiguous linear languages as soon as we know a generating
unambiguous linear grammar. In particular, the growth is either polynomial
or exponential.
If the growth is exponential, then there exists an algebraic
number λL ∈R≥0, its growth indicator, such that |L ∩Σm| behaves essentially
as λm
L . More precisely, for a language L, its growth indicator is deﬁned as the
non-negative real number λL where
λL = inf

λ ∈R≥0  ∃c > 0, ∀m ∈N: |L ∩Σm| ≤cλm	
.
The growth of a language L is
1.) exponential if 1 < λL ≤|Σ|,
2.) sub-exponential but inﬁnite if λL = 1, and
3.) ﬁnite if λL = 0.
Note that other values for λL do not occur and that λL is the inverse of the
convergence radius of gL(z). As we discussed above, the growth of an unam-
biguous linear language L is either polynomial or exponential; thus, if λL = 1,
5


## Page 6


the growth of L can be considered polynomial. Note that regular languages of
polynomial growth have a very restricted form: It is well known that a regular
language has polynomial growth if and only if it can be written as a ﬁnite union
of languages of the form u0u∗
1u2 · · · u∗
2k−1u2k where ui are words, see e. g., [25].
Thus, the more interesting situation occurs when a language has exponential
growths. It is then when the growth indicator becomes signiﬁcant.
2.4
Regular Languages and Finite Automata
Regular languages can be speciﬁed by non-deterministic ﬁnite automata (NFA)
A = (Q, Σ, E, I, F), where Q is the ﬁnite set of states, I ⊆Q is the set of
initial states, and F ⊆Q is the set of ﬁnal states. The set E contains labeled
transitions (or arcs), it is a subset of Q × Σ × Q. For a word w ∈Σ∗we write
p
w
−→q, if there is a path from state p to q which is labeled by w. Thus, the
accepted language becomes
L(A) =
n
w ∈Σ∗ ∃p ∈I, ∃q ∈F : p
w
−→q
o
.
Later it will be crucial to use also paths which avoid ﬁnal states. For this
we introduce a special notation. First remove all arcs (p, a, q) where q ∈F is a
ﬁnal state. Thus, ﬁnal states do not have incoming arcs anymore in this reduced
automaton. Let us write p
w
=⇒q, if there is a path in this reduced automaton
from state p to q which is labeled by the word w. Note that for such a path
p
w
=⇒q we allow p ∈F, but on the path we never meet any ﬁnal state again.
An NFA is called a deterministic ﬁnite automaton (DFA), if it has one initial
state and for every state p ∈Q and every letter a ∈Σ there is exactly one arc
(p, a, q) ∈E. In particular, a DFA in this paper is always complete, thus we
can read every word to its end. We also write p · w = q, if p
w
−→q. This yields
a (totally deﬁned) function Q × Σ∗→Q, which deﬁnes an action of Σ∗on Q
on the right.
2.5
Notation
Throughout the paper, L1 and L2 denote ﬁxed regular languages in Σ∗. We
use a DFA accepting L1 as well as a DFA accepting L2, which works from
right-to-left. However, instead of introducing this concept we use a DFA (work-
ing as usual from left-to-right), which accepts L2.
This automaton has the
same number of states (and is structurally isomorphic to) as a DFA accept-
ing the reversal language of L2.
Our input is therefore given by two DFAs
Ai = (Qi, Σ, Ei, {q0i}, Fi) for i = 1, 2 which accept the languages L1 and L2,
respectively. We let n1 = |Q1|, n2 = |Q2|, and we let n = max {n1, n2} be the
input size.
6


## Page 7


3
Unambiguity of Hκ(L1, L2)
In this section we prove that the hairpin completion Hκ(L1, L2) is an unambigu-
ous linear context-free language. The result is not needed for deciding regularity
of Hκ(L1, L2), but it came out as a byproduct of the decision procedure. How-
ever, the result turned out to be rather fundamental for the understanding of
hairpin completions of regular languages, in general. In particular, it allows to
compute the growths of Hκ(L1, L2) and to compare it with the growths of the
languages L1 and L2, see Sect. 5. Moreover, ideas of this section, will be reused
when we provide the algorithm deciding the regularity of Hκ(L1, L2). Therefore
we begin with the following result.
Theorem 3.1. The hairpin completion is unambiguous linear context-free. More-
over, there is an eﬀective construction of a generating unambiguous linear gram-
mar G for Hκ(L1, L2) such that the size of the grammar G is in O(n2
1n2
2) ⊆
O(n4).
Proof. The basic observation is that every word π ∈Hκ(L1, L2) has a unique
factorization π = γαβαγ such that
1.) γαβα ∈L1 or αβαγ ∈L2,
2.) |α| = κ,
3.) if a preﬁx of π belongs to L1, then it is a preﬁx of γαβα, and
4.) if a suﬃx of π belongs to L2, then it is a suﬃx of αβαγ.
In other words, among all factorizations which satisfy the ﬁrst condition and
where |α| ≥κ, we choose the factorization where |α| = κ and the length of γ
is minimal. In such a factorization we call γα ≤π the minimal gamma-alpha-
preﬁx of π. This factorization yields runs in the DFAs A1 and A2 as in Fig. 3.
(Recall that A2 accepts L2 and π = γαβαγ.) As π determines the factors γ
and α, the states ci, di, ei, fi, and q′
i (for i = 1, 2) are determined by π as well.
A1 :
q01
γ
−→c1
α
−→d1
β
−→e1
α
−→f1
γ
=⇒q′
1
A2 :
q02
γ
−→c2
α
−→d2
β
−→e2
α
−→f2
γ
=⇒q′
2
Figure 3: The runs deﬁned by π ∈Hκ(L1, L2) where γα is the minimal gamma-
alpha-preﬁx and, therefore, f1 ∈F1 or f2 ∈F2.
Vice versa, every path of this form (where |α| = κ) deﬁnes one word π =
γαβαγ from the hairpin completion Hκ(L1, L2) such that γα is its minimal
gamma-alpha-preﬁx.
By this observation, we can use quadruples of states in order to deﬁne the un-
ambiguous linear grammar G that generates the hairpin completion Hκ(L1, L2).
7


## Page 8


For every (p1, p2, q1, q2) ∈Q1 × Q2 × Q1 × Q2 we deﬁne a regular language
B(p1, p2, q1, q2) = {w ∈Σ∗| p1 · w = q1 ∧p2 · w = q2} .
Thus, in Fig. 3 we have π ∈B(q01, q02, q′
1, q′
2), αβα ∈B(c1, c2, f1, f2), and
β ∈B(d1, d2, e1, e2). Later a tuple (p1, p2, q1, q2) with B(p1, p2, q1, q2) ̸= ∅is
called a basic bridge, see Sect. 4.1.
Furthermore, in our grammar G, we let B(p1, p2, q1, q2) be the non-terminal
that derives all words from the language B(p1, p2, q1, q2). Compared to Fig. 3,
we intend that B(d1, d2, e1, e2)
∗
=⇒
G
β. In order to achieve this, it suﬃces to
introduce the production rules
B(p1, p2, q1, q2 · a) →a B(p1 · a, p2, q1, q2),
B(p1, p2, p1, p2) →1
for p1, q1 ∈Q1, p2, q2 ∈Q2, and a ∈Σ. Observe that every derivation from
B(p1, p2, q1, q2) to a terminal word must use the rule B(q1, p2, q1, p2) →1 as
last step. Thus, B(p1, p2, q1, q2)
∗
=⇒
G
w implies p1 · w = q1 and p2 · w = q2 as
desired. Furthermore, for all words w ∈B(p1, p2, q1, q2) and all factorizations
w = uv (i. e., (p1 · u) · v = q1 and (p2 · v) · u = q2) there is a derivation
B(p1, p2, q1, q2)
∗
=⇒
G u B(p1 · u, p2, q2, p2 · v)
∗
=⇒
G uv B(q1, p2, q1, p2) =⇒
G uv
where the non-terminal reached after |u| steps is determined. We conclude, the
non-terminal B(p1, p2, q1, q2) derives all words from the language B(p1, p2, q1, q2)
and the derivation of each word is unambiguous.
The linear context-free part of the grammar G are the derivations of the min-
imal gamma-alpha-preﬁxes and the corresponding suﬃxes. In a similar man-
ner as above, for every quadruple (p1, p2, q1, q2) ∈Q1 × Q2 × Q1 × Q2 we let
R(p1, p2, q1, q2) be a non-terminal in G and for p1, q1 ∈Q1, p2, q2 ∈Q2, and
a ∈Σ we deﬁne a rule
R(p1, p2, q1 · a, q2 · a) →a R(p1 · a, p2 · a, q1, q2) a
if q1 · a /∈F1 and q2 · a /∈F2; and for p1, q1 ∈Q1, p2, q2 ∈Q2, and α ∈Σκ we
deﬁne a rule
R(p1, p2, q1 · α, q2 · α) →α B(p1 · α, p2 · α, q1, q2) α
if q1 ·α ∈F1 or q2 ·α ∈F2. Observe that the derivations we introduce are again
unambiguous since on a derivation
R(q01, q02, q′
1, q′
2)
∗
=⇒
G u R(p1, p2, q1, q2) u
∗
=⇒
G uv R(c1, c2, f1, f2) vu
the non-terminal R(p1, p2, q1, q2) is determined by pi = q0i · u and qi = fi · v
(for i = 1, 2). Furthermore, the states q′
1, q′
2, q1, and q2 cannot be ﬁnal states
8


## Page 9


(if v ̸= 1) and if f1 ∈F1 or f2 ∈F2, then we have to use a production rule of
the second form in the next derivation step.
We conclude, there is a situation as in Fig. 3 if and only if
R(q01, q02, q′
1, q′
2)
∗
=⇒
G γ R(c1, c2, f1, f2) γ
=⇒
G γα B(d1, d2, e1, e2) αγ
∗
=⇒
G γαβαγ = π
and the derivation of π is unambiguous. Thus, we let R(q01, q02, q′
1, q′
2) be the ax-
ioms in the grammar G for all q′
1 ∈Q1 and q′
2 ∈Q2. Since for each word π there
exists at most one axiom with R(q01, q02, q′
1, q′
2) such that R(q01, q02, q′
1, q′
2)
∗
=⇒
G
π (namely, q′
1 = q01 · π and q′
2 = q02 · π), we see that G is unambiguous linear.
As for the size of the grammar, observe that the number of non-terminals is
bounded by 2n2
1n2
2 and the number of production rules is bounded by

|Σ|κ + 2 |Σ| +
1
n1n2

n2
1n2
2 ∈O(n4).
4
Polynomial Time Decision Algorithm
We consider the following decision problem:
Input: DFAs A1 and A2 (with state sets Q1 and Q2) accepting the languages
L1 and L2, respectively.
The input size is n = max {|Q1| , |Q2|}.
Question: Is the hairpin completion Hκ(L1, L2) regular?
The purpose of this section is to prove the following theorem.
Theorem 4.1. The problem whether the hairpin completion Hκ(L1, L2) is reg-
ular is decidable in time
i.) O(n2) if L1 = ∅or L2 = ∅.
ii.) O(n6) if L1 = L2.
iii.) O(n8) in general.
The algorithm deciding this problem is divided in Test 1, 2, and 3. Test 0
yields the time performance in case when L1 = ∅or L2 = ∅, yet it is redundant
for the other cases. The tests check properties of an automaton A which accepts
the minimal gamma-alpha-preﬁxes, introduced in Sect. 3. We will start with
the construction of A.
9


## Page 10


4.1
The Automaton A
The non-deterministic automaton A, we are about to construct, will accept
those words that are a minimal gamma-alpha-preﬁx of some word π = γαβαγ
and the ﬁnal states of the automatons will determine from which language
B(d1, d2, e1, e2) we have to choose the factor β. The construction is analogous
to the deﬁnition of rules for the non-terminals R(p1, p2, q1, q2) in Sect. 3.
In order to improve the time bound in case when L1 = L2, we introduce the
usual product automaton of A1 and A2 with state set
Q12 = {(p1, p2) ∈Q | ∃w ∈Σ∗: q01 · w = p1 ∧q02 · w = p2}
and operation (p1, p2) · w = (p1 · w, p2 · w) for (p1, p2) ∈Q12 and w ∈Σ∗.
Furthermore, we let n12 = |Q12|.
Note that if L2 = ∅or L1 = L2, then
n12 = n1 = n and in general n ≤n12 ≤n2. (Recall that ni = |Qi| for i = 1, 2.)
Note ﬁrst that a non-terminal R(p1, p2, q1, q2) is reachable from an axiom
only if (p1, p2) ∈Q12; hence, we will consider states from Q12 × Q1 × Q2 ⊆
Q1×Q2×Q1×Q2 for the construction of A. From now on, we call (p1, p2, q1, q2)
a basic bridge if B(p1, p2, q1, q2) ̸= ∅. This notation is due to the fact, that
there is some word that connects the state pairs (p1, p2) and (q1, q2).
It is
easy to see that in case when (p1, p2, q1, q2) is not a basic bridge, neither the
non-terminal R(p1, p2, q1, q2) nor the non-terminal B(p1, p2, q1, q2) is productive
in the grammar G.
In order to accept the α-factor, we also need levels for
0 ≤ℓ≤κ; hence there are κ + 1 levels. By [κ] we denote in this paper the set
{0, . . . , κ}. Deﬁne
{((p1, p2), q1, q2, ℓ) ∈Q12 × Q1 × Q2 × [κ] | (p1, p2, q1, q2) is a basic bridge}
as the state space of A. For N = n12n1n2 ≤n4 the size of A is bounded by
N · (κ + 1) ∈O(N) ⊆O(n4). We have N ≤n2 for L1 = ∅or L2 = ∅, and
N ≤n3 for L2 = L1.
By a slight abuse of languages we call a state ((p1, p2), q1, q2, ℓ) a bridge.
Bridges are frequently denoted by (P, q1, q2, ℓ) with P = (p1, p2) ∈Q12, q1 ∈Q1,
q2 ∈Q2, and ℓ∈[κ]. Bridges are a central concept in the following.
The a-transitions in the NFA for a ∈Σ are given by the following arcs:
(P, q1 · a, q2 · a, 0)
a
−→(P · a, q1, q2, 0)
for qi · a /∈Fi, i = 1, 2,
(P, q1 · a, q2 · a, 0)
a
−→(P · a, q1, q2, 1)
for q1 · a ∈F1 or q2 · a ∈F2,
(P, q1 · a, q2 · a, ℓ)
a
−→(P · a, q1, q2, ℓ+ 1)
for 1 ≤ℓ< κ.
Observe that no state of the form (P, q1, q2, 0) with q1 ∈F1 or q2 ∈F2
has an outgoing arc to level zero; we must switch to level one. There are no
outgoing arcs on level κ, and for each (a, P, q1, q2, ℓ) ∈Σ×Q12×Q1×Q2×[κ−1]
there exists at most one arc (P, q′
1, q′
2, ℓ)
a
−→(P · a, q1, q2, ℓ′). Indeed, the triple
(q′
1, q′
2, ℓ′) is determined by (q1, q2, ℓ) and the letter a. Not all arcs exist because
(P, q′
1, q′
2, ℓ) can be a bridge whereas (P · a, q1, q2, ℓ′) is not. Thus, there are at
most |Σ| · N · κ ∈O(N) arcs in the NFA.
10


## Page 11


The set of initial states I contains all bridges of the form (Q0, q′
1, q′
2, 0) where
Q0 = (q01, q02). The set of ﬁnal states F is given by all bridges (P, q1, q2, κ) on
level κ.
For an example and a graphical presentation of the NFA, see Fig. 4.
q01
p1
f1
t1
L1 = a∗(b | b)a
a
b, b
a
a
a, b, b
Σ
Σ
q02
p2
f2
t2
L2 = a∗ba
a
b
a, b
a
a, b, b
Σ
Σ
(Q0, t1, t2, 0)
(Q0, f1, f2, 0)
(Q0, p1, p2, 1)
B(q01, q02, p1, p2) = b
(Q0, f1, t2, 0)
(Q0, p1, t2, 1)
B(q01, q02, p1, t2) = aa+b | a∗b
(Q0, p1, f2, 1)
B(q01, q02, p1, f2) = ab
(Q0, t1, f2, 0)
(Q0, t1, p2, 1)
B(q01, q02, t1, p2) = baa+
(Q0, f1, p2, 1)
B(q01, q02, f1, p2) = ba
A:
a
a
a
a
a
a
a
a
a
Figure 4: DFAs for L1 and L2 and the resulting NFA A with 4 initial states
and 5 ﬁnal states associated to the (linear context-free) hairpin completion
Hκ(L1, L2) = a+ba+ ∪{aibaj | i ≥j ≥1} with κ = 1.
Next, we show that the automaton A encodes the minimal gamma-alpha-
preﬁxes and that we obtain the hairpin completion Hκ(L1, L2) in a natural way
from A. For languages B and R we denote by BR the language
BR = {vβv | β ∈B ∧v ∈R} .
(This notation is adopted from group theory where exponentiation denotes con-
jugation and the canonical involution refers to taking inverses.) Clearly, if B
and R are regular, then BR is linear context-free, but not regular in general.
Also note that if R is ﬁnite, then BR is regular.
Lemma 4.2. Let M = I × F.
For each pair µ = (I, F) ∈M with F =
((d1, d2), e1, e2, κ) let Rµ be the (regular) set of words which label a path from
the initial state I to the ﬁnal state F, and let Bµ = B(d1, d2, e1, e2).
11


## Page 12


The hairpin completion Hκ(L1, L2) is the disjoint union
Hκ(L1, L2) =
[
µ∈M
BRµ
µ .
Moreover, for µ ∈I × F and for all words β ∈Bµ and v ∈Rµ, the minimal
gamma-alpha-preﬁx of vβv is v.
Proof. Let π ∈Hκ(L1, L2). Let γα be the minimal gamma-alpha-preﬁx of π
with |α| = κ and factorize π = γαβαγ. There are runs in the DFAs
A1 :
q01
γ
−→c1
α
−→d1
β
−→e1
α
−→f1
γ
=⇒q′
1,
A2 :
q02
γ
−→c2
α
−→d2
β
−→e2
α
−→f2
γ
=⇒q′
2
where f1 ∈F1 or f2 ∈F2 (cf. Fig. 3). Recall that all states on these paths are
determined by π.
By the deﬁnition of the NFA A, we ﬁnd a path I
γ
−→A
α
−→F where
I = (Q0, q′
1, q′
2, 0), A = ((c1, c2), f1, f2, 0), and F = ((d1, d2), e1, e2, κ).
As
β ∈B(d1, d2, e1, e2), there is a unique µ = (I, F) ∈I × F with π ∈BRµ
µ .
Conversely, let µ = (I, F) ∈I × F, let β ∈Bµ, and let I
γ
−→A
α
−→F
with |α| = κ be a path in A. As F is a ﬁnal state it is on level κ and A =
((c1, c2), f1, f2, 0) is the last state on level zero, whence f1 ∈F1 or f2 ∈F2.
Therefore, we ﬁnd runs in the DFAs just like above where I = (Q0, q′
1, q′
2, 0)
and F = ((d1, d2), e1, e2, κ). We conclude γα is the minimal gamma preﬁx of
γαβαγ and γαβαγ ∈Hκ(L1, L2).
The next Lemma tells us that the paths in the automaton are unambiguous.
The arguments are essentially the same as used in Sect. 3. The unambiguity of
paths will become crucial later.
Lemma 4.3. Let w ∈Σ∗be the label of a path in A from a bridge A =
(P, p1, p2, ℓ) to A′ = (P ′, p′
1, p′
2, ℓ′), then the path is unique. This means that
B = B′ whenever w = uv and
A
u
−→B
v
−→A′,
A
u
−→B′
v
−→A′.
Proof. It is enough to consider u = a ∈Σ. Let B = (Q, q1, q2, m). Then we
have Q = P ·a and qi = p′
i ·v. If ℓ= 0 and pi /∈Fi for i = 1, 2, then m = 0, too;
otherwise m = ℓ+ 1. Thus, B is determined by A, A′, and u, v. We conclude
B = B′.
For the decision algorithm we need to construct the automaton A within
the time bounds. The automaton can be constructed in time O(n2
1n2
2); that
is O(n2) in case L1 = ∅or L2 = ∅and O(n4) otherwise.
Recall that the
number of states and the number of transitions are in O(N) ⊆O(n2
1n2
2) and
that the tuple (a, P, q1, q2, ℓ) ∈Σ×Q12 ×Q1 ×Q2 ×[κ−1] deﬁnes one transition
(P, q1 · a, q2 · a, ℓ)
a
−→(P · a, q1, q2, ℓ′) (where ℓ′ is determined by ℓ, q1 · a, and
12


## Page 13


q2 · a) if and only if (P · a, q1, q2, ℓ′) is a bridge. Thus, it suﬃces to show that
we can compute the set of bridges in time O(n2
1n2
2).
Furthermore, at this stage, we compute the set of all a-bridges for a ∈Σ,
where a basic bridge B(d1, d2, e1, e2) is called an a-bridge if B(d1, d2, e1, e2) ∩
aΣ∗̸= ∅. Later, we need the precomputed sets containing all a-bridges.
Lemma 4.4. The set containing all basic bridges and the sets containing all
a-bridges for a ∈Σ, respectively, can be computed in time O(n2
1n2
2).
Proof. Consider a transition system with state set Q1 × Q2 and transitions
(p1, q2)
a
−→(q1, p2) for all p1 · a = q1 and p2 · a = q2 (we use forward edges in
A1 and backwards edges in A2). Note that there are n1n2 · |Σ| transitions and
the transition system can be constructed in O(n1n2).
There is a path (p1, q2)
w
−→(q1, p2) with w ∈Σ∗if and only if p1 · w = q1
and p2 ·w = q2. Thus, a quadruple (p1, p2, q1, q2) ∈Q1 ×Q2 ×Q1 ×Q2 is a basic
bridge if and only if a path from (p1, q2) to (q1, p2) exists and it is an a-bridge
if and only if such a path exists that starts with an a-transition.
In order to compute the sets of bridges, we run a depth-ﬁrst reachability
search for all triples (p1, q2, a) ∈Q1 × Q2 × Σ; for each pair (q1, p2) ∈Q1 × Q2
that is reachable from (p1, q2) by a path starting with an a-transition, we mark
(p1, p2, q1, q2) as basic bridge and as a-bridge. Since every depth-ﬁrst search can
be performed in O(n1n2), the whole computation can be done in O(n2
1n2
2).
Remark 4.5. For convenience, we will henceforth assume that all states in the
automaton are reachable from an initial state and lead to some ﬁnal state. Such
an reachability test can easily be performed in O(n2
1n2
2); thus, this will not
breach the time bounds.
4.2
Test 0
We consider the case when L1 or L2 is ﬁnite. In this case we are able provide a
simple necessary and suﬃcient condition for the regularity of Hκ(L1, L2).
Proposition 4.6.
i.) If the language L(A) is ﬁnite, then Hκ(L1, L2) is regular.
ii.) If the language L(A) is inﬁnite and either L1 is ﬁnite or L2 is ﬁnite,
then Hκ(L1, L2) is not regular.
Proof. Statement i.) follows directly by Lem. 4.2.
For ii.) let L(A) be inﬁnite. There is a path
I
u
−→A
v
−→A
w
−→F
in A where I is an initial bridge, F = ((d1, d2), e1, e2) is a ﬁnal bridge, and
A
v
−→A is a non-trivial loop (by non-trivial we mean v ̸= 1). Note that A is on
level 0 and hence |w| ≥k. Let α be the suﬃx of w of length κ and let β be a word
13


## Page 14


from the language B(d1, d2, e1, e2). We have πi = uviwβwviu ∈Hκ(L1, L2) for
all i ≥0. Moreover, if a preﬁx of πi belongs to L1, it is a preﬁx of uviwβα and
if a suﬃx of πi belongs to L2, it is a suﬃx of αβwviu.
By contradiction, assume Hκ(L1, L2) is regular and L1 is ﬁnite. Let j ≥1
such that the power vj is idempotent in the syntactic monoid of Hκ(L1, L2),
hence
π = uvjkwβwvsu ∈Hκ(L1, L2)
for t ≥1. We consider t to be huge. More precisely, we assume that π is at least
twice as long as the longest word in L1 and that vjk covers more than half of π.
The longest suﬃx of π that belongs to L2 is still a suﬃx of αβwvju which is far
too short to build the hairpin; hence a preﬁx from L1 has to build the hairpin
and it has to cover more than half of π — a contradiction. By a symmetric
argument L2 is inﬁnite, too.
We check this property. Although, strictly speaking, Test 0 is redundant for
the general case.
Test 0: Decide whether or not L(A) is ﬁnite. If it is ﬁnite, then stop with the
output that Hκ(L1, L2) is regular. If it is not ﬁnite but L1 or L2 is ﬁnite, then
stop with the output that Hκ(L1, L2) is not regular.
In case when L1 = ∅or L2 = ∅the time complexity follows by the next
lemma as in these cases we can consider n1 = 1 or n2 = 1, respectively.
Lemma 4.7. Test 0 can be performed in time O(n2
1n2
2).
Proof. Recall that every state in A is reachable and co-reachable, by Rem. 4.5.
The language L(A) is inﬁnite if and only if A contains at least one non-trivial
loop A
v
−→A By the well-known algorithm of Tarjan [26] we can decompose
a directed graph (as well as a ﬁnite automaton) into its strongly connected
components in linear time with respect to the number of transitions. As the
automaton A has O(n2
1n2
2) transitions, this yields the time complexity.
4.3
Test 1
By Test 0, we may assume in the following that A accepts an inﬁnite language
and that the set S of non-trivial strongly connected components of the automa-
ton A has been computed. Every non-trivial strongly connected component is
on level 0 and, moreover, as A accepts an inﬁnite language, there is at least
one. For s ∈S let Ns be the number of states in the component s. Note that
P
s∈S Ns ≤N. By putting some linear order on the set of bridges, we assign to
each s ∈S the least bridge As and some shortest, non-empty word vs such that
As
vs
−→As.
The next lemma tells us that for a regular hairpin completion Hκ(L1, L2)
every strongly connected component s ∈S is a simple cycle, and hence, the
word vs is uniquely deﬁned.
14


## Page 15


Lemma 4.8. Let the hairpin completion Hκ(L1, L2) be regular, s ∈S be a
strongly connected component, and As
w
−→F be a path from As to a ﬁnal bridge
F. Then the word w is a preﬁx of some word in v+
s .
In addition, the word vs is uniquely deﬁned and the loop As
vs
−→As visits
every other bridge B ∈s \ {A} exactly once. Thus it forms a Hamiltonian cycle
of s and |vs| = Ns.
Proof. Let A = As and v = vs. Consider a path labeled by w from A to a ﬁnal
bridge F = ((d1, d2), e1, e2, k). As all bridges are reachable, we ﬁnd a word u
and an initial bridge I such that
I
u
−→A
v
−→A
w
−→F.
As the automaton A accepts uviw for all i ≥0, we see that uviwβwviu ∈
Hκ(L1, L2) for all i ≥0 and all β ∈B(d1, d2, e1, e2). As Hκ(L1, L2) is regular,
there are j ≥1 and k > |wβ| such that uvjkwβwvju ∈Hκ(L1, L2), by pumping.
Due to the deﬁnition of A, the longest suﬃx of π belonging to L2 is a suﬃx of
αβwvju, where α is the suﬃx of w of length κ, and this suﬃx is too short to
create the hairpin completion. This means that the hairpin completion is forced
to use a preﬁx in L1 and that has to be a preﬁx of uvjkwβα. Therefore, the
suﬃx wvju is complementary to a preﬁx of uvjk, whence w must be a preﬁx of
vj(k−1) (see Fig. 5) and, thus, concludes the ﬁrst statement of our lemma.
u
vj
vj(k−1)
w
β
w
vj
u
Figure 5: The hairpin of π (Read the upper part from left to right and the lower
part from right to left).
Recall that A
v
−→A is a shortest, non-trivial loop around A; hence |v| ≤Ns
is obvious. Let B ∈s \ {A} and x = x1x2 such that A
x1
−→B
x2
−→A. For
some i, j ≥1 we have
vi =
xj. Thus, vi = xj by the ﬁrst statement. By the
unique-path-property stated in Lem. 4.3 we obtain that the loop A
xj
−→A just
uses the shortest loop A
v
−→A several times. In particular, B is on the shortest
loop around A. This yields |v| ≥Ns and hence the second statement.
Example 4.9. In the example given in Fig. 4 the state (Q0, t1, t2, 0) forms the
only strongly connected component and the corresponding path is labeled with
a. As one can easily observe, the automaton A satisﬁes the properties stated in
Lem. 4.8 (even though the hairpin completion is not regular).
The next test tries to falsify the property of Lem. 4.8.
Hence it gives a
suﬃcient condition that Hκ(L1, L2) is not regular.
Test 1: Decide whether there is s ∈S and a path As
w
−→F such that w is not
a preﬁx of a word in v+
s . If there is such a path, then stop with the output that
Hκ(L1, L2) is not regular.
15


## Page 16


Lemma 4.10. Test 1 can be performed in time O(N 2).
Proof. For s ∈S, let A = As and compute a shortest non-empty word v such
that A
v
−→A. If |v| ̸= Ns, stop with the output that Hκ(L1, L2) is not regular.
Otherwise, assign to each bridge that is reachable from A a subset of marks from
{0, . . . , Ns −1}. A mark i is assigned to a bridge B if B is reachable from A with
a word from v∗v[1, i]. Test 1 yields that Hκ(L1, L2) is not regular if and only if
there is a bridge that is marked by i and that has an outgoing a-transition where
a ̸= v[i + 1]. The marking algorithm can be performed by a depth-ﬁrst search
that runs in time O(N · Ns). Summing over all strongly connected components
we deduce a time complexity in O
 P
s∈S N · Ns

⊆O(N 2).
4.4
Test 2 and 3
Henceforth, we assume that Test 1 was successful (i. e., Test 1 did not yield that
Hκ(L1, L2) is not regular). We ﬁx a strongly connected component s ∈S of A.
We let A = As = ((p1, p2), q1, q2, 0), we let v = vs, and we assume A
v
−→A
forms an Hamiltonian cycle in s. By u we denote some word leading from an
initial bridge ((q01, q02), q′
1, q′
2, 0) to A. (For the following test we do not need
to know u we just need to know it exists.) The main idea is to investigate runs
through the DFAs A1 and A2 where k, ℓ≥n according to Fig. 6.
L1 :
q01
u
−→p1
vk
−→p1
xy
−→c1
z
−→d1
x
−→e1
vn1
=⇒q1
v∗
=⇒q1
u
=⇒q′
1
L2 :
q02
u
−→p2
vℓ
−→p2
x
−→c2
z
−→d2
yx
−→e2
vn2
=⇒q2
v∗
=⇒q2
u
=⇒q′
2
Figure 6: Runs through A1 and A2 based on the loop A
v
−→A.
We investigate the case when uvkxyzxvℓu ∈Hκ(L1, L2) for all k ≥ℓand
where (by symmetry) this property is due to the longest preﬁx belonging to L1.
The following lemma is rather technical. However, the notations are chosen
to ﬁt exactly to Fig. 6.
Lemma 4.11. Let x, y, z ∈Σ∗be words and (d1, d2) ∈Q1 × Q2 with the
following properties:
1.) κ ≤|x| < |v| + κ and x is a preﬁx of some word in v+.
2.) 0 ≤|y| < |v| and xy is the longest common preﬁx of xyz and some word
in v+.
3.) z ∈B(c1, c2, d1, d2), where c1 = p1 · xy and c2 = p2 · x.
4.) q1 = d1 ·xvn1 and during the computation of d1 ·xvn1 we see after exactly
κ steps a ﬁnal state in F1 and then never again.
16


## Page 17


5.) q2 = d2 · yxvn2 and, let e2 = d2 · yx, during the computation of e2 · vn2
we do not see a ﬁnal state in F2.
If Hκ(L1, L2) is regular, then there exists a factorization xyzxv = µδβδµ where
|δ| = κ and p2 · µδβδ ∈F2 (which implies δβδµv∗u ⊆L2).
Proof. The conditions say that uvkxyzxvℓu ∈Hκ(L1, L2) for all k ≥ℓ≥n.
Moreover, by condition 4, the hairpin completion can be achieved with a preﬁx in
L1, and the longest preﬁx of uvkxyzxvℓu belonging to L1 is the preﬁx uvkxyzα
where α is the preﬁx of x of length κ.
If Hκ(L1, L2) is regular, then we have uvkxyzxvk+1u ∈Hκ(L1, L2), too, as
soon as k is large enough, by a simple pumping argument. For this hairpin
completion we must use a suﬃx belonging to L2. For z = 1, this follows from
|y| < |v|. For z ̸= 1 we use |y| < |v| and, in addition, that xya with a = z[1] is
not a preﬁx of vx by condition 2.
By 5 the longest suﬃx of uvkxyzxvk+1u belonging to L2 is a suﬃx of
xyzxvk+1u. Thus, we can write
uvkxyzxvk+1u = uvkxyzxvvku = uvkµδβδµvku
where δβδµvku ∈L2 and |δ| = κ. We obtain xyzxv = µδβδµ. As p2 = q02 · u
and p2 = p2 · v, we conclude p2 · µδβδ ∈F2 as desired. (Recall that our second
DFA A2 accepts L2.)
Example 4.12. Let us take a look at Fig. 4 again. Let A = (Q0, t1, t2, 0), v = a
and u = 1. If we choose x = a, y = 1, z = b, and (d1, d2) = (p1, p2) we can
see that conditions 1 to 5 of Lem. 4.11 are satisﬁed but there is no factorization
abaa = µδβδµ with |δ| = κ = 1 such that q02 · µδβδ /∈F2. Hence, the hairpin
completion is not regular.
We perform Test 2 and 3 which, again, try to falsify the property given by
Lem. 4.11 for a regular hairpin completion. The tests distinguish whether the
word z is empty or non-empty.
Test 2: Decide the existence of words x, y ∈Σ∗and states (d1, d2) ∈Q1 ×
Q2 satisfying conditions 1 to 5 of Lem. 4.11 with z = 1, but where for all
factorizations xyxv = µδβδµ with |δ| = κ we have p2 · µδβδ /∈F2. If we ﬁnd
such a situation, then stop with the output that Hκ(L1, L2) is not regular.
Test 3: Decide the existence of words x, y, z ∈Σ∗with z ̸= 1 and states
(d1, d2) ∈Q1 × Q2 satisfying conditions 1 to 5 of Lem. 4.11, but where for all
factorizations xyzxv = µδβδµ with |δ| = κ we have p2 · µδβδ /∈F2. If we ﬁnd
such a situation, then stop with the output that Hκ(L1, L2) is not regular.
Before we analyze the time complexity of Test 2 an Test 3 we will prove
that if languages L1 and L2 pass the tests we described so far, then the hair-
pin completion Hκ(L1, L2) is regular. Thus, the properties given by Lem. 4.8
and Lem. 4.11 together are suﬃcient for the regularity of Hκ(L1, L2). The time
complexity analysis of Test 2 and Test 3 can be found in Sect. 4.5.
17


## Page 18


Lemma 4.13. Suppose no outcome of Tests 1, Test 2, and Test 3 is that
Hκ(L1, L2) is not regular. Then the hairpin completion Hκ(L1, L2) is regular.
Proof. Let π ∈Hκ(L1, L2). Write π = γαβαγ such that γα is the minimal
gamma-alpha-preﬁx of π and |α| = κ. Therefore, either γαβα ∈L1 or αβαγ ∈
L2; we assume γαβα ∈L1, by symmetry. In addition, we may assume that
|γ| > n4 (cf. Prop. 4.6 and Test 0). We can factorize γ = uvw with |uv| ≤n4
and |v| ≥1 such that there are runs as in Fig. 7 where f1 ∈F1.
L1 :
q01
u
−→p1
v
−→p1
wαβα
−→f1
w
=⇒q1
v
=⇒q1
u
=⇒q′
1
L2 :
q02
u
−→p2
v
−→p2
wαβα
−→f2
w
=⇒q2
v
=⇒q2
u
=⇒q′
2
Figure 7: Runs through A1 and A2 for the word π.
We infer from Test 1 that wα is a preﬁx of some word in v+. Hence, we can
write wαβ = vixyz with i ≥0 such that vixy is the maximal common preﬁx of
wαβ and some word in v+, wα ∈v∗x with κ ≤|x| < |v| + κ, and |y| < |v|.
We see that for some k ≥ℓ≥0 we can write
π = uvkxyzxvℓu.
Moreover, uvkxyzxvℓu ∈Hκ(L1, L2) for all k ≥ℓ≥0.
There are only
ﬁnitely many choices for u, v, x, y (due to the lengths bounds) and for each of
them there is a regular set Rz associated to the ﬁnite collection of bridges such
that
π ∈

uvkxyRzxvℓu
 k ≥ℓ≥0
	
⊆Hκ(L1, L2).
More precisely, we can choose Rz = {1} for z = 1 and otherwise we can
choose
Rz ∈{B(c1, c2, d1, d2) ∩aΣ∗| (c1, c2, d1, d2) is a bridge and a ∈Σ} .
Note that the sets

uvkxyRzxvℓu
 k ≥ℓ≥0
	
are not regular in general. If
we bound however ℓby n, then the ﬁnite union
[
0≤ℓ≤n

uvkxyRzxvℓu
 k ≥ℓ
	
is regular. Thus, we may assume that ℓ> n. Let e2 = p2 · xzyx. We have
e2 · vn = q2 and if we see a ﬁnal state during the computation of e2 · vn, then
for all ℓ> k ≥n and z ∈Rz we see that uvkxyzxvℓu ∈Hκ(L1, L2), due to a
suﬃx in L2 and
uvnv+xyRzxv+vnu ⊆Hκ(L1, L2).
Otherwise, Test 2 or Test 3 tells us that for all z ∈Rz the word xyzxv has a
factorization µδνδµ such that |δ| = κ and p2 · µδνδ ∈F2. The paths q02 · u = p2
and p2 · v = p2 yield δνδµv∗u ⊆L2 and, again,
uvnv+xyRzxv+vnu ⊆Hκ(L1, L2).
18


## Page 19


Hence, the hairpin completion Hκ(L1, L2) is a ﬁnite union of regular lan-
guages and, therefore, regular itself.
4.5
Time Complexity of Test 2 and Test 3
In this section we provide the ﬁnal step of the proof of Thm. 4.1. We show that
Test 2 can be performed in time O(N 2) and that Test 3 can be performed in
time O(n12n2
1n2
2n). Thus, in case when L1 = L2 both tests run in O(n6) and in
general Test 2 runs in O(n8) and Test 3 runs in O(n7).
Test 2: Decide the existence of words x, y ∈Σ∗and states (d1, d2) ∈Q1 × Q2
satisfying
1.) k ≤|x| < |v| + κ and x is a preﬁx of some word in v+,
2.) 0 ≤|y| < |v| and xy is a preﬁx of some word in v+,
3.) d1 = p1 · xy and d2 = p2 · x,
4.) q1 = d1 ·xvn1 and during the computation of d1 ·xvn1 we see after exactly
κ steps a ﬁnal state in F1 and then never again, and
5.) q2 = d2 · yxvn2 and, let e2 = d2 · yx, during the computation of e2 · vn2
we do not see a ﬁnal state in F2
but where for all factorizations xyxv = µδβδµ with |δ| = κ we have p2 · µδβδ /∈
F2. If we ﬁnd such a situation, then stop with the output that Hκ(L1, L2) is
not regular.
Lemma 4.14. Test 2 can be performed in time O(N 2).
Proof. For a strongly connected component s ∈S with As = ((p1, p2), q1, q2)
and vs = v, we have to compute all words x and y such that there are runs
p1
xy
−→d1
xvn1
−→q1,
p2
x
−→d2
yxvn2
−→q2
and the conditions 1 to 5 are satisﬁed. In addition, we demand that during the
computation of d2 · yxvn2 we do not meet any ﬁnal state in F2 after more than
κ −1 steps. (In case such a ﬁnal state exists, either condition 5 is breached
or a factorization xyxv = µδβδµ with |δ| = κ and p2 · µδβδ ∈F2 exists.) By
backwards searches in A1 and A2 starting at states q1 and q2, respectively,
and searching for paths labelled by suﬃxes of v+, we compute all pairs (x, xy)
satisfying these conditions in time O(N · Ns).
At this stage we also compute the position ℓ(x, xy) of the last ﬁnal state
during the run p2 · vxyx and we let ℓ(x, xy) = 0 if no such state exists. Note
that 0 ≤ℓ(x, xy) < Ns + |x| + κ. If a factorization xyxv = µδβδµ with |δ| = κ
and p2 · µδβδ ∈F2 exists, then |xyxv| −ℓ(x, xy) gives us a lower bound for the
length of µ.
19


## Page 20


Let m(x, xy) be the length of the longest µ such that a factorization xyxv =
µδβδµ with |δ| = κ exists (without the condition p2 · µδβδ ∈F2).
There is a factorization xyxv = µδβδµ with |δ| = κ and p2 · µδβδ ∈F2 if
and only if m(x, xy) ≥|xyxv| −ℓ(x, xy) and ℓ(x, xy) −κ ≥|xyxv| /2.
We need to precompute the values m(x, xy) eﬃciently, which turns out to be
a little bit tricky. For 0 ≤i < Ns we let vi = v[i + 1, Ns]v[1, i] be the conjugate
of v starting at the (i + 1)-st letter. We wish to match position in v2
i with
positions in v2. For each 0 ≤j < Ns we store the maximal k ≤Ns such that
v2
i [j, j + k] = v2[j, j + k] in a table entry M(i, j), see Fig. 8. For each i one run
(from right to left) over the words v2
i and v2 is enough. It takes O(N 2
s ) time
to build the table M. Now, if we know the length m′ of the longest common
preﬁx of v|xy| and xv, then m(x, xy) = |xy|+m′ −κ (yet at most |xyxv| /2−κ).
The length of m′ is stored in M(|xyx| mod Ns, (−|x|) mod Ns), hence we have
access to m(x, xy) in constant time.
v
v
v
v
v
i
j
k
maximal
overlap
Figure 8: Matching positions of v2
i with v2.
All in all Test 4 can be performed in O(P
s∈S N · Ns) ⊆O(N 2).
Test 3: Decide the existence of words x, y, z ∈Σ∗with z ̸= 1 and states
(d1, d2) ∈Q1 × Q2 satisfying
1.) k ≤|x| < |v| + κ and x is a preﬁx of some word in v+,
2.) 0 ≤|y| < |v| and xy is the longest common preﬁx of xyz and some word
in v+,
3.) z ∈B(c1, c2, d1, d2), where c1 = p1 · xy and c2 = p2 · x,
4.) q1 = d1 ·xvn1 and during the computation of d1 ·xvn1 we see after exactly
κ steps a ﬁnal state in F1 and then never again, and
5.) q2 = d2 · yxvn2 and, let e2 = d2 · yx, during the computation of e2 · vn2
we do not see a ﬁnal state in F2
but where for all factorizations xyzxv = µδβδµ with |δ| = κ we have p2 ·µδβδ /∈
F2. If we ﬁnd such a situation, then stop with the output that Hκ(L1, L2) is
not regular.
Lemma 4.15. Test 3 can be performed in time O(n12n2
1n2
2n).
Proof. For s ∈S with As = ((p1, p2), q1, q2) and vs = v, we create two tables
T1 and T2. The table T1 holds all pairs (c2, d1) ∈Q2 × Q1 such that a word x
exists with
20


## Page 21


1.) κ ≤|x| < |v| + κ and x is a preﬁx of a word in v+,
2.) p2 · x = c2,
3.) d1 ·xvn1 = q1, and during the computation of d1 ·xvn1 we see a ﬁnal state
after exactly κ steps and then never again.
We call x a witness for (c2, d1) ∈T1. The table T2 holds all triples (c1, d2, a) ∈
Q1 × Q2 × Σ such that a proper preﬁx y′ < v exists with
1.) y′a is no preﬁx of v,
2.) p1 · y′ = c1,
3.) d2 · y′vn2 = q2, and during the computation of d2 · y′vn2 we do not see a
ﬁnal state after κ or more steps.
We call y′ a witness for (c1, d2, a) ∈T2. By backwards computing in the second
component, the tables T1 and T2 can be created in O(Nsn1) and O(Nsn2),
respectively.
We claim that Test 3 yields that Hκ(L1, L2) is not regular if and only if there
exists a pair (c2, d1) ∈T1 and a triple (c1, d2, a) ∈T2 such that (c1, c2, d1, d2) is
an a-bridge. Recall that the list of a-bridges is precomputed.
First, assume (c2, d1) ∈T1, (c1, d2, a) ∈T2, and (c1, c2, d1, d2) is indeed an
a-bridge. Let x and y′ be the the witnesses for (c2, d1) ∈T1 and (c1, d2, a) ∈T2,
respectively. Choose z ∈B(c1, c2, d1, d2) ∩aΣ∗and y such that xy is a preﬁx
of some word in v+, |xy| ≡|y′| (mod |v|), and |y| < |v|. Verify that x, y, z and
(d1, d2) satisfy the conditions 1 to 5 of Test 3. However, for any factorization
xyzxv = µδβδµ with |δ| = κ, the word µδ has to be a preﬁx of xy, since xya is
no preﬁx of vx. During the computation of d2 ·y′vn2 we did not see a ﬁnal state
after more than κ −1 steps. The same holds for the computation of d2 · yxvn2
and, therefore, we have p2 · µδβδ /∈F2.
Now assume that x, y, z ∈Σ∗, z ̸= 1, and (d1, d2) ∈Q1 × Q2 exist, which
satisfy the conditions 1 to 5 of Test 3 but where for all factorizations xyzxv =
µδβδµ with |δ| = κ we have p2 · µδβδ /∈F2. Choose y′ < v such that |xy| ≡|y′|
(mod |v|).
Let c2 = p2 · x, c1 = p1 · y′ and a ∈Σ be the ﬁrst letter of z.
Obviously, (c1, c2, d1, d2) is an a-bridge and x is a witness for (c2, d1) ∈T1. If
we saw a ﬁnal state after more than κ −1 steps during the computation of
d2 · y′vn2, then a factorization xyzxv = µδβδµ where |δ| = κ and p2 · µδβδ ∈F2
would exist. Thus, y′ is a witness for (c1, d2, a) ∈T2.
Since the table of a-bridges is precomputed (see Lem. 4.4), this test can be
performed in time O(|T1| · |T2|). The set of all ﬁrst components of T1 (respec-
tively, T2) is bounded by both, the size Ns and n2 (respectively, n1). Therefore,
we have |T1| ∈O(n1·min(Ns, n2)) and |T2| ∈O(n2·min(Ns, n1)). By symmetry,
assume n2 ≤n1.
21


## Page 22


Test 3 can be performed in time
O
 X
s∈S
 Nsn1 + Nsn2 + n1n2 · min(Ns, n1) · min(Ns, n2)

!
⊆
O
 
n12n2
1n2 + n12n1n2
2 +
X
s∈S,Ns≥n2
n2
1n2
2 +
X
s∈S,Ns<n2
N 2
s n1n2
!
(Recall that n1 ≤n ≤n12 ≤n1n2 ≤n2 and P
s∈S Ns ≤N = n12n1n2.)
Since there are at most n12n1 strongly connected components with a size of
n2 or more states,
X
s∈S,Ns≥n2
n2
1n2
2 ≤n12n3
1n2
2.
For the last term we can use the approximation
X
s∈S,Ns<n2
N 2
s n1n2 ≤
X
s∈S,Ns<n2
Nsn1n2
2 ≤n12n2
1n3
2.
We conclude, Test 3 can be performed in time O(n12n2
1n2
2n).
5
Rational Growth
Let L′
1 = L1 ∩S
α∈Σκ Σ∗αΣ∗α and L′
2 = L2 ∩S
α∈Σκ αΣ∗αΣ∗.
Obviously,
Hκ(L′
1, L′
2) = Hκ(L1, L2). Thus, the growths of Hκ(L1, L2) should be compared
with the growths of L′
1 and L′
2 rather than with the growths of L1 and L2.
The languages L′
1 and L′
2 are still regular and we can compute their growths.
However, to simplify the notation, it is more convenient to assume from the very
beginning that L1 and L2 contains only words that can form hairpins. Formally,
we assume throughout this section that
L1 ⊆
[
α∈Σκ
Σ∗αΣ∗α,
L2 ⊆
[
α∈Σκ
αΣ∗αΣ∗.
Remember (Sect. 2.3) that the growth indicator λL of a language L says
that |L ∩Σm| behaves essentially as λm
L .
Theorem 5.1. Let λ = max {λL1, λL2} be the maximum growth indicator of
L1 and L2, and let η be the growth indicator of Hκ(L1, L2).
i.) The value lies within
√
λ ≤η ≤λ.
In particular, the growth of Hκ(L1, L2) is exponential (respectively, poly-
nomial, ﬁnite) if and only if the maximum growth of L1 and L2 is expo-
nential (respectively, polynomial, ﬁnite).
ii.) If Hκ(L1, L2) is regular, then we have η = λ. Thus, the growth indicator
of Hκ(L1, L2) is the maximum growth indicator of L1 and L2.
22


## Page 23


The theorem will follow by Lem. 5.3 and Lem. 5.4 in Sect. 5.2 which compare
the growth indicators λ and η with the growth indicators of the languages
Bµ and Rµ for µ ∈M. Before we can prove theses lemmas, we need some
preliminary observations on growth indicators of (regular) languages.
5.1
Basic Facts about Growth Indicators
Consider two languages K1 and K2. It is well known that the growth indicator
of their union is λK1∪K2 = max {λK1, λK2}. Furthermore, if K1 ̸= ∅̸= K2 the
growth indicator of their concatenation is λK1K2 = max {λK1, λK2}, too.
Now, let K be a regular language. The preﬁx closure of K is deﬁned as
Pref(K) = {u ∈Σ∗| ∃v ∈Σ∗: uv ∈K} .
The next lemma shows that the growth indicators of K and its preﬁx closure
coincide. Note that this does not necessarily hold if K is (unambiguous) linear.
Lemma 5.2. Let K be a regular language, then λK = λPref(K).
Proof. As K ⊆Pref(K), the inequation λK ≤λPref(K) is obvious.
Conversely, let k be a constant such that K is accepted by a DFA of size k
and let m ∈N. For a word u ∈Pref(K) ∩Σm, there is some word v such that
uv ∈K and, moreover, we may assume |v| ≤k. Let h be a mapping h: u 7→uv
for u ∈Pref(K) ∩Σm such that uv ∈K and |v| ≤k. Note that h is injective
(for a ﬁxed m). Thus, we see that
|Pref(K) ∩Σm| ≤
m+k
X
i=m
K ∩Σi .
For all ν > λK there exists c such that |K ∩Σm| ≤cνm for all m ∈N.
Therefore,
|Pref(K) ∩Σm| ≤
m+k
X
i=m
cνi ≤c(k + 1)νkνm.
We conclude λPref(K) ≤ν and as such λPref(K) = λK.
5.2
Proof of Theorem 5.1
Recall from Lem. 4.2, that the hairpin completion is the disjoint union
Hκ(L1, L2) =
[
µ∈M
BRµ
µ .
We let σµ and ρµ be the growth indicators of Bµ and Rµ, respectively. By
σ = max {σµ | µ ∈M} and ρ = max {ρµ | µ ∈M} we denote the maximum
growth indicators of all Bµ and all Rµ, respectively. The next lemma compares
the growth indicator λ with the growth indicators σ and ρ.
23


## Page 24


Lemma 5.3. λ = max {σ, ρ}.
Proof. We start by proving λ ≥max {σ, ρ}. Let µ ∈M be ﬁxed. For γα ∈Rµ
with |α| = κ, and β ∈Bµ either γαβα ∈L1 or αβαγ ∈L2. Thus, we may
deﬁne a mapping h: (Rµ × Bµ) →L1 ∪L2 such that
h(γα, β) =
(
γαβα
if γαβα ∈L1
αβαγ
otherwise.
Obviously, |γα| + |β| = |h(γα, β)| −κ. Also note that a word w ∈L1 ∪L2 of
length m can form less than 2m hairpin completions. Therefore, the cardinality
of the inverse image is
h−1(w)
 < 2m. Using the mapping h, we can compare
the growth rm = |RµBµ ∩Σm| with the growth ℓm = |(L1 ∪L2) ∩Σm|; that is
rm ≤2(m + κ) · ℓm+κ for m ∈N.
For ν > λ = λL1∪L2 we chose ν′ from the open interval (λ, ν). There exists
c′ > 0 such that rm ≤2(m + κ)c′ν′κν′m for all m ∈N and, as the function νm
growth faster than ν′m, there is some c > 0 such that rm ≤cνm for all m ∈N.
Therefore, max {σµ, ρµ} ≤ν for all ν > λ, whence max {σµ, ρµ} ≤λ. As this
inequation holds for all µ ∈M, we deduce λ ≥max {σ, ρ}.
Conversely, we will prove that L1 is included in a language K whose growth
indicator is max {σ, ρ}.
As there is a symmetric language that includes L2,
this yields λ ≤max {σ, ρ}. Let B = S
µ∈M Bµ and R = S
µ∈M Rµ. We let K
be the preﬁx closure K = Pref(RBΣκ). As the growth indicator of RBΣκ is
λRBΣκ = max {σ, ρ} and by Lem. 5.2, we deduce λK = max {σ, ρ}.
Now, consider w ∈L1. By assumption, w can form a hairpin on its right
side. We let π ∈Hκ({w} , ∅) be a hairpin completion of w.
Let γα be the
minimal gamma-alpha-preﬁx of π with |α| = κ and β such that π = γαβαγ.
Note that w has to be a preﬁx of γαβα ∈RBΣκ (by the minimality of |γ|).
Thus, we may conclude L1 ⊆K as desired.
Now, let us compare the growth indicator η with the growth indicators σ
and ρ.
Lemma 5.4. η = max

σ, √ρ
	
.
Proof. Let τµ be the growth indicator of BRµ
µ
for µ ∈M. Since Hκ(L1, L2) =
S
µ∈M BRµ
µ , we see that η = max {τµ | µ ∈M}. Thus, in order to prove the
claim, it suﬃces to show that τµ = max

σµ, √ρµ
	
for µ ∈M. Let µ ∈M be
ﬁxed from here on and recall that Bµ and Rµ are non-empty. We let
gBµ(z) =
X
m≥0
bmzm
with bm = |Bµ ∩Σm| ,
gRµ(z) =
X
m≥0
rmzm
with rm = |Rµ ∩Σm| .
It will be convenient to let ri+1/2 = 0 for i ∈N.
24


## Page 25


First, let us prove τµ ≥σµ. Let v ∈Rµ and consider K = vBµv. Obviously,
K ⊆BRµ
µ
and hence τµ ≥λK = σµ.
Next, we prove τµ ≥√ρµ.
Let K = {β}Rµ ⊆BRµ
µ
for some β ∈Bµ.
The generating function of K is given as gK(z) = P
m≥0 r(m−|β|)/2zm. For all
ν > λK there exists c > 0 such that
∀m ∈N: r(m−|β|)/2 ≤cνm
⇐⇒
∀m ∈N: rm ≤cν|β|(ν2)m
and, therefore, ν2 ≥ρµ. We conclude τµ ≥λK ≥√ρµ.
Finally, we need to prove τµ ≤max

σµ, √ρµ
	
. As BRµ
µ
is unambiguous, by
Lem. 4.2,
gB
Rµ
µ (z) =
X
m≥0
dmzm
with dm =
X
k+ℓ=m
bkrℓ/2.
For ν > max

σµ, √ρµ
	
we choose ν′ from the open interval
 max

σµ, √ρµ
	
, ν

.
By that choice, νm grows faster than ν′m and there is c′ > 0 such that for all
m ∈N and k + ℓ= m, we have bkrℓ/2 ≤c′ν′m. Thus, there is c > 0 such that
for all m ∈N, the inequality dm ≤mc′ν′m ≤cνm holds. This deduces the last
step in the proof, τµ ≤max

σµ, √ρµ
	
.
Lem. 5.3 and Lem. 5.4 yields a development of the growth indicators λ and
η as shown in Fig. 9.
ρ
σ
ρ
λ
√ρ
σ
√ρ
η
Figure 9: Growth indicators λ and η in dependency of σ and ρ.
It is easy to see that η is at least
√
λ and at most λ and, therefore, we deduce
the ﬁrst statement of Thm. 5.1. The second statement of Thm. 5.1 claims that
if the hairpin completion is regular, then λ = η. In case when Hκ(L1, L2) is
regular, we infer from Lem. 4.8 that if the hairpin completion of Hκ(L1, L2) is
regular, then the growth of all Rµ is polynomial (more precisely, linear) or ﬁnite
(i. e., ρ = 1 or ρ = 0). We conclude λ = max {σ, ρ} = max

σ, √ρ
	
= η.
Final Remarks
We proved that regularity of a hairpin completion of regular languages is de-
cidable in polynomial time. Considering the two-sided hairpin completion of
regular languages, the decision algorithm, we presented, can be performed in
25


## Page 26


time O(n8) (respectively, O(n6) in case when L1 = L2) which, at ﬁrst, seems to
be a high degree for a polynomial time algorithm. However, the ﬁrst step of the
algorithm is the construction of an automaton A which is already of size O(n4)
(respectively, O(n3)). Thus, when speaking of time complexity with respect
to the size of A, the algorithm uses quadratic time, only. Furthermore, as we
take into account all pairs of states of A, the time bound seems optimal for
this approach and further improvement of the time complexity would probably
call for a completely new approach. For the one-sided hairpin completion of a
regular language, we provide a faster algorithm which runs in quadratic time.
The polynomial time bounds are due to the fact that we use DFAs for the
speciﬁcation of L1 and L2. We do not know what happens if L1 and L2 are
given by NFAs. We suspect that deciding regularity if Hκ(L1, L2) might become
PSPACE-complete. But this has not been investigated yet.
By our second result, that the hairpin completion of regular languages is
always an unambiguous linear language, we are able to eﬀectively compute the
growth function of the hairpin completion. Moreover, we showed that the hair-
pin completion has an exponential growth if and only if one of the underlying
languages has an exponential growth (given that every word from the underly-
ing languages can form a hairpin). More precisely, the growth indicator of the
hairpin completion is at most as large as the maximum growth indicator of the
underlying languages and at least as large as its square root. In case when the
hairpin completion is regular, we provided an even stronger relationship between
the growth indicators. In that case, the growth indicator of the hairpin comple-
tion coincides with the maximum growth indicator of the underlying languages.
Our results about growths are trivial in case that L1 and L2 have polynomial
growths. However, the structure of regular languages with polynomial growths
is well-understood [25] (Sect. 2.3). We believe that a study of hairpin comple-
tions for this class of regular languages might lead to interesting results. We
leave this to future research.
Another interesting problem concerns the hairpin lengthening of regular
languages, which is an operation familiar to the hairpin completion. We call
γ1αβαγ2 a (right) hairpin lengthening of γ1αβα if γ2 is a suﬃx of γ1 and we
call it a (left) hairpin lengthening of αβαγ2 if γ1 is a preﬁx of γ2. The hairpin
lengthening HLκ(L1, L2) of languages L1 and L2 is introduced analogously to
the hairpin completion. It is known that the hairpin lengthening of regular lan-
guages is linear, but in contrast to the hairpin completion it is not unambiguous,
in general, see [15]. This might indicate that deciding regularity of the hairpin
lengthening HLκ(L1, L2) is more diﬃcult than for the hairpin completion. To
date it is not known whether regularity of HLκ(L1, L2) is decidable.
References
[1] J. Berstel and C. Reutenauer. Noncommutative Rational Series with Ap-
plications. Encyclopedia of Mathematics and its Applications. Cambridge
University Press, 2010.
26


## Page 27


[2] T. Ceccherini-Silberstein. On the growth of linear languages. Advances in
Applied Mathematics, 35(3):243 – 253, 2005.
[3] D. Cheptea, C. Mart´ın-Vide, and V. Mitrana. A new operation on words
suggested by DNA biochemistry: Hairpin completion. Transgressive Com-
puting, pages 216–228, 2006.
[4] R. Deaton, R. Murphy, M. Garzon, D. Franceschetti, and S. Stevens. Good
encodings for DNA-based solutions to combinatorial problems. Proc. of
DNA-based computers DIMACS Series, 44:247–258, 1998.
[5] V. Diekert and S. Kopecki. Complexity results and the growths of hairpin
completions of regular languages (extended abstract). In M. Domaratzki
and K. Salomaa, editors, CIAA, volume 6482 of Lecture Notes in Computer
Science, pages 105–114. Springer, 2010.
[6] V. Diekert, S. Kopecki, and V. Mitrana. On the hairpin completion of
regular languages. In M. Leucker and C. Morgan, editors, ICTAC, volume
5684 of Lecture Notes in Computer Science, pages 170–184. Springer, 2009.
[7] M. Garzon, R. Deaton, P. Neathery, R. Murphy, D. Franceschetti, and
E. Stevens.
On the encoding problem for DNA computing.
The Third
DIMACS Workshop on DNA-Based Computing, pages 230–237, 1997.
[8] M. Garzon, R. Deaton, L. Nino, S. Stevens Jr., and M. Wittner. Genome
encoding for DNA computing. Proc. Third Genetic Programming Confer-
ence, pages 684–690, 1998.
[9] P. Gawrychowski, D. Krieger, N. Rampersad, and J. Shallit. Finding the
growth rate of a regular or context-free language in polynomial time. In
Developments in Language Theory, pages 339–358, 2008.
[10] M. Hagiya, M. Arita, D. Kiga, K. Sakamoto, and S. Yokoyama. Towards
parallel evaluation and learning of boolean µ-formulas with molecules. In
Second Annual Genetic Programming Conf., pages 105–114, 1997.
[11] J. E. Hopcroft and J. D. Ulman. Introduction to Automata Theory, Lan-
guages and Computation. Addison-Wesley, 1979.
[12] M. Ito, P. Leupold, F. Manea, and V. Mitrana. Bounded hairpin com-
pletion. Information and Computation, In Press, Accepted Manuscript:–,
2010.
[13] L. Kari, S. Konstantinidis, E. Losseva, P. Sos´ık, and G. Thierrin. Hair-
pin structures in DNA words. In A. Carbone and N. A. Pierce, editors,
DNA, volume 3892 of Lecture Notes in Computer Science, pages 158–170.
Springer, 2005.
[14] L. Kari, K. Mahalingam, and G. Thierrin. The syntactic monoid of hairpin-
free languages. Acta Inf., 44(3-4):153–166, 2007.
27


## Page 28


[15] S. Kopecki. Formal language theory of hairpin formations. PhD thesis,
University of Stuttgart, Holzgartenstr. 16, 70174 Stuttgart, 2011.
[16] S. Kopecki. On iterated hairpin completion. Theoretical Computer Science,
412(29):3629–3638, July 2011.
[17] W. Kuich.
On the entropy of context-free languages.
Information and
Control, 16:173–200, 1970.
[18] F. Manea, C. Mart´ın-Vide, and V. Mitrana. On some algorithmic prob-
lems regarding the hairpin completion.
Discrete Applied Mathematics,
157(9):2143–2152, 2009.
[19] F. Manea, C. Mart´ın-Vide, and V. Mitrana. Hairpin lengthening. In F. Fer-
reira, B. L¨owe, E. Mayordomo, and L. M. Gomes, editors, CiE, volume 6158
of Lecture Notes in Computer Science, pages 296–306. Springer, 2010.
[20] F. Manea and V. Mitrana. Hairpin completion versus hairpin reduction. In
S. B. Cooper, B. L¨owe, and A. Sorbi, editors, CiE, volume 4497 of Lecture
Notes in Computer Science, pages 532–541. Springer, 2007.
[21] F. Manea, V. Mitrana, and T. Yokomori. Two complementary operations
inspired by the DNA hairpin formation: Completion and reduction. Theor.
Comput. Sci., 410(4-5):417–425, 2009.
[22] F. Manea, V. Mitrana, and T. Yokomori. Some remarks on the hairpin
completion. Int. J. Found. Comput. Sci., 21(5):859–872, 2010.
[23] Ch. H. Papadimitriou. Computatational Complexity. Addison Wesley, 1994.
[24] K. Sakamoto, D. Kiga, K. Komiya, H. Gouzu, S. Yokoyama, S. Ikeda, and
M. Hagiya. State transitions by molecules, 1998.
[25] A. Szilard, S. Yu, K. Zhang, and J. Shallit. Characterizing regular lan-
guages with polynomial densities.
In I. Havel and V. Koubek, editors,
Mathematical Foundations of Computer Science 1992, volume 629 of Lec-
ture Notes in Computer Science, pages 494–503. Springer Berlin / Heidel-
berg, 1992. 10.1007/3-540-55808-X 48.
[26] R. E. Tarjan. Depth-ﬁrst search and linear graph algorithms. SIAM J.
Comput., 1(2):146–160, 1972.
[27] J. G. Williams, A. R. Kubelik, K. J. Livak, J. A. Rafalski, and S. V. Tingey.
DNA polymorphisms ampliﬁed by arbitrary primers are useful as genetic
markers. Nucleic acids research, 18(22):6531–6535, Nov. 1990.
[28] E. Winfree. Whiplash PCR for O(1) computing. In University of Pennsyl-
vania, pages 175–188, 1998.
28

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1108_2427v1_deciding_regularity_of_hairpin_completions_of_regular_languages_in_polynomial_ti
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2011/1108_2427V1_DECIDING_REGULARITY_OF_HAIRPIN_COMPLETIONS_OF_REGULAR_LANGUAGES_IN_POLYNOMIAL_TI.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

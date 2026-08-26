---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1101.4824v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1101.4824v1_It_Is_NL-complete_to_Decide_Whether_a_Hairpin_Completion_of_Regular_Languages_Is

> Source: 1101.4824v1_It_Is_NL-complete_to_Decide_Whether_a_Hairpin_Completion_of_Regular_Languages_Is.pdf

> Pages: 13

---


## Page 1


arXiv:1101.4824v1  [cs.FL]  25 Jan 2011
It Is NL-complete to Decide Whether a Hairpin Completion
of Regular Languages Is Regular
Volker Diekert, Steﬀen Kopecki
{diekert,kopecki}@fmi.uni-stuttgart.de
University of Stuttgart, Institute for Formal Methods in Computer Science (FMI),
Universit¨atsstraße 38, D-70569 Stuttgart
November 10, 2018
Abstract
The hairpin completion is an operation on formal languages which is inspired by the hairpin
formation in biochemistry. Hairpin formations occur naturally within DNA-computing. It has
been known that the hairpin completion of a regular language is linear context-free, but not
regular, in general. However, for some time it is was open whether the regularity of the hairpin
completion of a regular language is is decidable. In 2009 this decidability problem has been
solved positively in [5] by providing a polynomial time algorithm. In this paper we improve
the complexity bound by showing that the decision problem is actually NL-complete. This
complexity bound holds for both, the one-sided and the two-sided hairpin completions.
Keywords: Automata and Formal Languages; Regular Languages, Finite Automata; NL-
Complete Problems; DNA-Computing; Hairpin Completion.
1
Introduction
The hairpin completion is a natural operation of formal languages which has been inspired by
molecular phenomena in biology and which occurs naturally during DNA-computing.
An in-
tramolecular base pairing, known as a hairpin, is a pattern that can occur in single-stranded DNA
and, more commonly, in RNA. Hairpin or hairpin-free structures have numerous applications to
DNA computing and molecular genetics, see [3,6,7,10,11] and the references within for a detailed
discussion. For example, an instance of 3-Sat has been solved with a DNA-algorithm and one of
the main concepts was to eliminate all molecules with a hairpin structure, see [19].
In this paper we study the hairpin completion from a purely formal language viewpoint. The
hairpin completion of a formal language was ﬁrst deﬁned by Cheptea, Mart´ın-Vide, and Mitrana
in [2]; here we use a slightly more general deﬁnition which was introduced in [5]. The hairpin
completion and some related operations have been studied in a series of papers from language
theoretic and algorithmic point of view, see e.g., [9, 12–17]. The formal operation of the hairpin
completion on words is best explained in Figure 1. In that picture as in the rest of the paper we
mean by putting a bar on a word (like α) to read it from right-to-left and in addition to replace
a letter a with the (Watson-Crick) complement a. The hairpin completion of a regular language
is linear context-free, but not regular, in general [2].
For some time it was not known whether regularity of the hairpin completion of a regular
language is decidable. It was only in 2009 when we presented in [5] a decision algorithm. Actually,
we proved a better result by providing a polynomial time algorithm with a (rough) runtime
estimation of about O(n20).
1


## Page 2


γ
α
β
α
annealing
γ
α
β
α
lengthening
γ
α
β
α
γ
strand
hairpin
hairpin completion
Figure 1: Hairpin completion of a DNA-strand (or a word).
In an extended abstract which appeared at the CIAA 2010 we presented a modiﬁed approach
to solve the same problem [4] which led, in particular, to the following two new results: First,
the time complexity of the new decision algorithm is in O(n8). Second, the decision problem is
NLOGSPACE-complete, i.e., NL-complete.
This paper is the journal version of [4] for the second result. We decided to focus on the space
complexity since, in terms of complexity, NL-completeness yields a precise characterization and
because the given page limit did not allow to include full proofs for all results of [4]. Moreover,
our proofs are still rather technical and the focus on the NL-algorithm simpliﬁes the presentation.
We consider the one-sided and the two-sided hairpin completions simultaneously. It turns out
that NL-completeness holds in both cases.
The paper is organized as follows. In Section 2 we ﬁx the notation used throughout. We give
the formal deﬁnition of the hairpin completion Hk(L1, L2) and we discuss our input model using
appropriate deterministic automata.
In Section 3 we state the main result (Theorem 3.1) and we give a full proof in the subsequent
subsections. A main technical tool is the use of single-valued non-deterministic log-space trans-
ductions, which might be not fairly standard. They are explained in Section 3.1. In Section 4 we
give a short conclusion and we state some open problems.
2
Preliminaries and Notation
We assume the reader to be familiar with the basic concepts of formal language theory, automata
theory, and complexity theory, as one can ﬁnd in the text books [8, 18]. By NL we mean the
complexity class NLOGSPACE, which contains the problems which can be decided by a non-
deterministic Turing machine using O(log n) work space.
Throughout we use the well-known
result that NL is closed under complementation, see e.g. [18]. We also use the fact that if L can
be reduced to L′ via some single-valued non-deterministic log-space transduction and L′ ∈NL,
then we have L ∈NL, see [1] and Section 3.1 for more details.
By Σ we denote a ﬁnite alphabet with at least two letters. The set of words over Σ is denoted
Σ∗; and the empty word is denoted by 1.
Given a word w, we denote by |w| its length and
w(m) ∈Σ its m-th letter. If w = xyz for some x, y, z ∈Σ∗, then x and z are called preﬁx and
suﬃx of w, respectively. By a proper preﬁx x of w we mean a preﬁx such that x ̸= w (but we
allow x = 1). The preﬁx relation between words x and w is denoted by x ≤w and for proper
preﬁxes by x < w.
We assume that the alphabet Σ is equipped with an involution
: Σ →Σ. An involution for
a set is a bijection such that a = a. We extend the involution to words a1 · · · an by a1 · · · an =
an · · · a1 where the ai’s are letters. This convention is like taking inverses in groups. For languages
L ⊆Σ∗we denote by L the set
L = {w | w ∈L} .
2


## Page 3


Throughout the paper L1, L2 are two regular languages in Σ∗and by k we mean a (small) constant.
(In a biological setting k ∼10 yields a reasonable value.) According to Figure 1 we deﬁne the
hairpin completion Hk(L1, L2) by
Hk(L1, L2) = {γαβαγ | (γαβα ∈L1 ∨αβαγ ∈L2) ∧|α| = k} .
This deﬁnition is slightly more general than the original deﬁnition in [2,16]. It allows us to treat
the two-sided hairpin completion (L1 = L2) and the one-sided hairpin completion (either L1 = ∅
or L2 = ∅) simultaneously.
A regular language can be speciﬁed by a non-deterministic ﬁnite automaton (NFA) A =
(Q, Σ, E, I, F), where Q is the ﬁnite set of states, I ⊆Q is the set of initial states, and F ⊆Q is
the set of ﬁnal states. The set E contains labeled edges (or arcs), it is a subset of Q × Σ × Q. For
a word u ∈Σ∗we write p
u
−→q, if there is a path from state p to q which is labeled by the word
u. Thus, the accepted language becomes
L(A) =
n
u ∈Σ∗ ∃p ∈I ∃q ∈F : p
u
−→q
o
.
Later it will be crucial to use also paths which avoid ﬁnal states. For this we introduce a
special notation. First remove all arcs (p, a, q) where q ∈F is a ﬁnal state. Thus, ﬁnal states do
not have incoming arcs anymore. Let us write p
u
=⇒q, if there is a path from state p to q which
is labeled by the word u in this new automaton after removing these arcs. Note that for such a
path p
u
=⇒q we allow p ∈F, but on the path we never enter any ﬁnal state again.
An NFA is called a deterministic ﬁnite automaton (DFA), if it has exactly one initial state and
for every state p ∈Q and every letter a ∈Σ there is exactly one arc (p, a, q) ∈E. In particular,
in this paper a DFA is always complete. Thus, we can read every word to its end. We also write
p · u = q, if p
u
−→q. This yields a (totally deﬁned) function Q × Σ∗→Q. (It deﬁnes an action of
Σ∗on Q on the right.)
In the following we use a DFA accepting L1 as well as a DFA accepting L2, but the DFA for
L2 has to work from right-to-left. Instead of introducing this concept we use a DFA (working as
usual from left-to-right), which accepts L2. This automaton has the same number of states as
(and is structurally isomorphic to) a DFA accepting the reversal language of L2.
As input we assume that the regular languages L1 and L2 are speciﬁed by DFAs A1 and A2
with state set Qi, state q0i ∈Qi as initial state, and Fi ⊆Qi as ﬁnal states. By n we denote the
input size
n = |Q1| + |Q2| .
We also need the usual product DFA with state space
Q = {(p1, p2) ∈Q1 × Q2 | ∃w ∈Σ∗: (p1, p2) = (q01 · w, q02 · w)} .
The action is given by (p1, p2) · a = (p1 · a, p2 · a). As Q contains only reachable states, the
size of Q might be smaller than |Q1| · |Q2|. In the following we work simultaneously in all three
automata deﬁned so far. Moreover, in Q1 and Q2 we are going to work backwards. This leads to
nondeterminism.
3
Main result
The purpose of this paper is to prove the following result:
Theorem 3.1. The following problem is NL-complete:
Input:
Two DFAs A1 and A2 recognizing L1 and L2 with state sets Q1 and Q2 resp. such
that n = |Q1| + |Q2|.
Question: Is Hk(L1, L2) regular?
3


## Page 4


Since NL is included in P we obtain the following result from [5] as a corollary.
Corollary 3.2. The problem whether the hairpin completion Hk(L1, L2) is regular is decidable in
polynomial time.
We now turn to the proof of Theorem 3.1. The NL-hardness is immediate:
Lemma 3.3. The problem whether the hairpin completion Hk(L1, L2) is regular is NL-hard, even
for L2 = ∅.
Proof. The well-known NL-complete Graph-Accessibility-Problem [18] can easily be reduced to
the following problem for DFAs:
Let Σ =

a, a, b, b
	
be an alphabet with four letters. Decide for a given DFA, which accepts a
language L ⊆

b, b
	∗, whether or not L is empty.
Now let L1 = a∗Lak. The hairpin completion
Hk(L1, ∅) =

aiwaj  i ≥j ≥k ∧w ∈L
	
is regular if and only if L is empty (because L ⊆

b, b
	∗).
The diﬃcult part is to show that deciding regularity of Hk(L1, L2) is in NL. This is subject
of the rest of this section.
3.1
Single-valued non-deterministic log-space transductions
A single-valued non-deterministic log-space transduction is performed by a non-deterministic log-
space Turing machine which may stop on every input w with some output r(w). Single-valued
means that, in case that the machine stops on input w, the output is always the same, indepen-
dently of non-deterministic moves during the computation. Thus, w 7→r(w) is a well-deﬁned
function from words to words. A single-valued non-deterministic log-space transduction is a re-
duction from a language L to L′, if we have w ∈L ⇐⇒r(w) ∈L′.
The following lemma belongs to folklore. Its proof is exactly the same as for the standard case
of deterministic log-space reductions [8] and therefore omitted.
Lemma 3.4. Let L′ ∈NL and assume that there exists a single-valued non-deterministic log-space
transduction from L to L′. Then we have L ∈NL, too.
Due to Lemma 3.4 we are free to use several single-valued non-deterministic log-space trans-
ductions in order to enrich the input.
3.2
Bridges
Let Q1, Q2 be the state sets as ﬁxed by Theorem 3.1.
For every quadruple (p1, p2, q1, q2) ∈
Q1 × Q2 × Q1 × Q2 we deﬁne a regular language B(p1, p2, q1, q2) as follows:
B(p1, p2, q1, q2) =

β ∈Σ∗ p1 · β = q1 ∧p2 · β = q2
	
.
We say that a quadruple (p1, p2, q1, q2) is a bridge, if B(p1, p2, q1, q2) ̸= ∅. The idea behind
this notation is that B(p1, p2, q1, q2) closes a gap between pairs (p1, p2) and (q1, q2). For a bridge
(p1, p2, q1, q2) the words β ∈B(p1, p2, q1, q2) correspond later exactly to the β-part in Figure 1.
Lemma 3.5. There is a single-valued non-deterministic log-space transduction which outputs the
table of all bridges.
Proof. Graph reachability and its complement are solvable in NL. Therefore we can decide for
each quadruple (p1, p2, q1, q2) ∈Q1×Q2×Q1×Q2 if it is a bridge, and we can output (p1, p2, q1, q2)
in the aﬃrmative case.
4


## Page 5


3.3
The NFA A
Next, we construct an NFA, which is called simply A, and we explore properties of this NFA. The
NFA A uses k+1 levels (or layers) of a product automaton over Q×Q1 ×Q2 ⊆Q1 ×Q2 ×Q1×Q2
where Q has been deﬁned as in Section 2. Hence, the number of states is at most (k + 1)n4 which
is in O(n4).
Formally, we use a level for each ℓwith 0 ≤ℓ≤k, hence there are k + 1 levels. By [k] we
denote in this paper the set {0, . . . , k}. Deﬁne
QA = {((p1, p2), q1, q2, ℓ) ∈Q × Q1 × Q2 × [k] | (p1, p2, q1, q2) is a bridge}
as the state space of an NFA called A.
We call a state ((p1, p2), q1, q2, ℓ) a bridge at level ℓ, and we keep in mind that there exists a
word w such that p1·w = q1 and p2·w = q2. Frequently (and by a slight abuse of language) we call
a state ((p1, p2), q1, q2, ℓ) simply a bridge, too. Bridges at level ℓare also denoted by (P, q1, q2, ℓ)
with P = (p1, p2) ∈Q, qi ∈Qi, i = 1, 2, and ℓ∈[k]. Bridges at diﬀerent levels play a central rˆole
in the following.
Let a ∈Σ. The a-transitions in the NFA are given by the following arcs:
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
for 1 ≤ℓ< k.
Thus, for the P-component an a-transition behaves as in a usual product automaton, but for
the q1- and q2-components we move backwards using the a-transitions in the original automata.
This is why the resulting automaton A is non-deterministic.
Observe that no state of the form (P, q1, q2, 0) with q1 ∈F1 or q2 ∈F2 has an outgoing arc to
level zero; we must switch to level one. There are no outgoing arcs on level k, and for each tuple
(a, P, q1, q2, ℓ) ∈Σ×Q×Q1×Q2×[k−1] there exists at most one arc (P, q′
1, q′
2, ℓ)
a
−→(P·a, q1, q2, ℓ′).
Indeed, the P · a is determined by P and the letter a, and the triple (q′
1, q′
2, ℓ′) is determined by
(q1, q2, ℓ) and the letter a. Not all such arcs exist in A, because (P, q′
1, q′
2, ℓ) might be a bridge
whereas (P ·a, q1, q2, ℓ′) is not. (Observe however that if (P ·a, q1, q2, ℓ′) is a bridge, then (P, q′
1, q′
2, ℓ)
is a bridge, too.)
The set of initial states I contains all bridges at level zero of the form (Q0, q′
1, q′
2, 0) with
Q0 = (q01, q02). The set of ﬁnal states F is given by all bridges (P, q1, q2, k) at level k.
This concludes the deﬁnition of the NFA A. For an example and a graphical presentation of
the NFA, see Figure 2.
Remark 3.6. By Lemma 3.5, the NFA A can be computed by a single-valued non-deterministic
log-space transduction. Thus, we have direct access to A and henceforth we assume that A is also
written on the input tape.
The next result shows the unambiguity of paths in the automaton A. It is a crucial property.
Lemma 3.7. Let w ∈Σ∗be the label of a path in A from a bridge A = (P, p1, p2, ℓ) to A′ =
(P ′, p′
1, p′
2, ℓ′), then the path is unique. This means that B = B′ whenever w = uv and
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
Proof. It is enough to consider u = a ∈Σ. Let B = (Q, q1, q2, m). Then we have Q = P · a and
qi = p′
i · v. If ℓ= 0 and pi /∈Fi for i = 1, 2, then m = 0, too; otherwise m = ℓ+ 1. Thus, B is
determined by A, A′, and u, v. We conclude B = B′.
5


## Page 6


q01
p1
f1
t1
L1 = a∗(b + b)a
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
B(q01, q02, p1, t2) = aa+b + a∗b
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
Figure 2: DFAs for L1 and L2 and the resulting NFA A with 4 initial states and 5 ﬁnal states
associated to the (linear context-free) hairpin completion Hk(L1, L2) = a+ba+∪{asbat | s ≥t ≥1}
with k = 1.
We will now show that the automaton A encodes the hairpin completion in a natural way. For
languages U and V we deﬁne the language V U as follows:
V U = {uvu | u ∈U, v ∈V } .
Clearly, if U and V are regular, then V U is linear context-free, but not regular, in general. (The
notation V U is adopted from group theory where exponentiation denotes conjugation and the
canonical involution refers to taking inverses.)
Lemma 3.8. For each pair τ = (I, F) ∈I × F with F = ((d1, d2), e1, e2, k) let Rτ be the
(regular) set of words which label a path from the initial bridge I to the ﬁnal bridge F, and let
Bτ = B(d1, d2, e1, e2).
The hairpin completion Hk(L1, L2) is a disjoint union
Hk(L1, L2) =
[
τ∈I×F
BRτ
τ .
Moreover, for each word w ∈BRτ
τ
there is a unique factorization w = ρβρ with ρ ∈Rτ and
β ∈Bτ.
Proof. Let w ∈Hk(L1, L2). There exists some factorization w = γαβαγ such that |α| = k and
there are runs as in Figure 3 in the original DFAs A1 and A2 where f ′
1 ∈F1 or f ′
2 ∈F2 (or both):
Choosing among all these runs the length |γ| to be minimal, we see that we actually ﬁnd the
following picture according to Figure 4. In other words, either γαβα is the longest preﬁx of w
belonging to L1 or αβαγ is the longest suﬃx of w belonging to L2, or both. The diﬀerence to
the precedent ﬁgure is is that between fi and q′
i (i = 1, 2) we never enter a ﬁnal state. By the
deﬁnition of the NFA A we see that ρ = γα is the unique preﬁx of w such that w = ρβρ with
6


## Page 7


L1 :
q01
γ
−→c′
1
α
−→d′
1
β
−→e′
1
α
−→f ′
1
γ
−→q′
1,
L2 :
q02
γ
−→c′
2
α
−→d′
2
β
−→e′
2
α
−→f ′
2
γ
−→q′
2
Figure 3: Some run deﬁned by w ∈Hk(L1, L2)
L1 :
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
L2 :
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
Figure 4: The unique run deﬁned by w ∈Hk(L1, L2) with |γ| minimal
ρ ∈Rτ and β ∈Bτ for some τ. Now, as the length |γ| is ﬁxed by w, we see that all states ci,
di, ei, fi, and q′
i are uniquely deﬁned by w for i = 1, 2. Thus, there is a unique τ ∈I × F with
w ∈BRτ
τ . More precisely, we have:
τ = (((q01, q02), q′
1, q′
2, 0), ((d1, d2), e1, e2, k)).
3.4
First Tests
By construction, the automaton A accepts the union of the languages Rτ as deﬁned in Lemma 3.8.
If the accepted language is ﬁnite then all Rτ are ﬁnite and hence all BRτ
τ
are regular. This leads
immediately to the following result:
Proposition 3.9. It can be decided in NL whether or not the accepted language of the NFA A is
ﬁnite. If the accepted language is ﬁnite, then the hairpin completion Hk(L1, L2) is regular.
Proof. To see that the accepted language is inﬁnite it is enough to guess a path from an initial
state to ﬁnal one which uses some (guessed) state at least twice.
Since NL is closed under
complementation the ﬁniteness test is possible in NL, too. The second assertion follows from
Lemma 3.8.
We check this property (although strictly speaking Test 0 is redundant):
Test 0: Decide in NL whether or not L(A) is ﬁnite. If it is ﬁnite, then stop with the output that
Hk(L1, L2) is regular.
For convenience we may assume in the following that A accepts an inﬁnite language and that
all states are reachable from an initial bridge and lead to some ﬁnal bridge.
For sake of completeness let us state another result which shows that deciding regularity of the
one-sided hairpin completion is somewhat easier, because the ﬁniteness condition is also necessary
in this case. However, as we neither use this result nor does it change the NL-completeness of the
problem, we leave the proof of Proposition 3.10 to the interested reader.
Proposition 3.10. If L1 or L2 is ﬁnite, but the accepted language of A is inﬁnite, then the
hairpin completion Hk(L1, L2) is not regular.
7


## Page 8


Let K be the set of non-trivial strongly connected components of the automaton A (read as a
directed graph). Every non-trivial strongly connected component is on level 0 and, moreover, as
A accepts an inﬁnite language, there is at least one. For κ ∈K let Nκ be the number of states in
the component κ. We have Nκ = |κ| ≤n4.
The next lemma tells us that for a regular hairpin completion Hk(L1, L2) every strongly con-
nected component κ ∈K is a simple cycle.
Lemma 3.11. Let the hairpin completion Hk(L1, L2) be regular, A
vA
−→A be a path in a strongly
connected component κ with 1 ≤|vA| ≤Nκ, and let A
w
−→F be a path in A from A to a ﬁnal
bridge F. Then the word w is a preﬁx of some word in v+
A.
In addition, the word vA is uniquely deﬁned by the conditions A
vA
−→A and 1 ≤|v|A ≤Nκ.
The loop A
vA
−→A visits every other state B ∈κ exactly once. Thus it builds a Hamiltonian cycle
of κ and |vA| = Nκ.
Proof. Let A
v
−→A be some non-trivial loop. We see that A is on level zero. Consider a path
labeled by w from A to a ﬁnal bridge F = ((p1, p2), q1, q2, k). By assumption, all states in A are
reachable from some initial state. Thus, we ﬁnd a word u such that the automaton A accepts uviw
for all i ≥0. We see next that uviwβwviu ∈Hk(L1, L2) for all i ≥0 and all β ∈B(p1, p2, q1, q2).
As Hk(L1, L2) is regular, there are s, t ∈N with uvswβwvs+tu ∈Hk(L1, L2) and t > |wβ|, by
pumping. This means that the hairpin completion is forced to use a suﬃx in L2, because the
longest preﬁx belonging to L1 is too short to create the hairpin completion. Due to the deﬁnition
of A we conclude that uvsw must be a preﬁx of uvs+tw. This implies that w is a preﬁx of vt and
thus the ﬁrst statement of our lemma.
Let vA be some shortest word such that A
vA
−→A. Observe ﬁrst that |vA| ≤Nκ. Now, let
A ̸= B ∈κ and A
v′
−→B
v′′
−→A. For some i, j > 0 we have
vi
A
 =
(v′v′′)j. Thus, vi
A = (v′v′′)j
by the ﬁrst statement. By the unique-path-property stated in Lemma 3.7 we obtain that the loop
A
(v′v′′)j
−→
A just uses the shortest loop A
vA
−→A several times. In particular, B is on the shortest
loop around A. This yields |vA| ≥Nκ and hence the second statement.
Example 3.12. In the example given in Figure 2 the state (Q0, t1, t2, 0) forms the only strongly
connected component and the corresponding path is labeled with a. As one can easily observe the
automaton A satisﬁes the properties stated in Lemma 3.11 (even though the hairpin completion
is not regular).
Due to the technique of single-valued non-deterministic log-space transductions we may assume
that the set of non-trivial strongly connected components K is part of the input. Moreover, for
each state A and κ ∈K we know whether or not A ∈κ, and we know Nκ = |κ|.
The next test tries to falsify the property of Lemma 3.11. Hence it gives a suﬃcient condition
that Hk(L1, L2) is not regular.
Test 1: Guess some state A and κ ∈K with A ∈κ, a letter a ∈Σ, and a position 1 ≤m ≤Nκ
such that:
1.) There is a path A
v
−→A where m ≤|v| ≤Nκ and v(m) = a.
2.) There is a path A
w
−→F where w(i · |v| + m) ̸= a for some i ∈N with 1 ≤i · |v| + m ≤|w|.
If such a triple (A, a, m) exists, then output that Hk(L1, L2) is not regular.
The correctness of Test 1 follows by Lemma 3.11 and, because for the existence of paths 1.)
and 2.) we only have to remember the triple (A, a, m), Test 1 can be performed in NL.
8


## Page 9


Remark 3.13. We can perform Test 1 in NL and in case it yields that the hairpin completion
Hk(L1, L2) is not regular, we can stop. Henceforth, we assume that the algorithm did not stop
during Test 1 and that every strongly connected component κ ∈K is a simple cycle. Performing
another single-valued non-deterministic log-space transduction we may assume that for each A ∈κ
the word vA is attached to A and each vA is part of the input.
3.5
Second and Third Test
We ﬁx a bridge A = ((p1, p2), q1, q2) in a strongly connected component.
We let v = vA as
deﬁned in Lemma 3.11 and let α be the preﬁx of length k of some long enough word in v+. (By
Remark 3.13 the word v is written in plain form on the input tape.) By u we denote some word
leading from an initial bridge to A. (The NL algorithm does not know u, but it knows that it
exists.) The main idea is to investigate runs through the DFAs for L1 and L2 where s, t ≥n
according to Figure 5. Recall that n refers to the original input size, thus n ≥|Qi| for i = 1, 2.
L1 :
q01
u
−→p1
vs
−→p1
x
−→c1
y
−→d1
α
−→e1
vn
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
vt
−→p2
α
−→c2
y
−→d2
x
−→e2
vn
=⇒q2
v∗
=⇒q2
u
=⇒q′
2
Figure 5: Runs through A1 and A2 based on the loop A
v
−→A
We investigate the case where uvsxyαvtu ∈Hk(L1, L2) for all s ≥t and where (by symmetry)
this property is due to the longest preﬁx belonging to L1 (hence e1 ∈F1).
The following lemma is rather technical. The notations are however chosen to ﬁt exactly to
Figure 5.
Lemma 3.14. Let x, y ∈Σ∗be words and (d1, d2) ∈Q1 × Q2 with the following properties:
1.) α ≤x and x < vα.
2.) y ∈B(c1, c2, d1, d2), where c1 = p1 · x and c2 = p2 · α, and x is the longest common preﬁx of
xy and vα.
3.) e1 = d1 · α ∈F1 is a ﬁnal state, q1 = e1 · vn, and during the computation of e1 · vn we do not
enter a ﬁnal state in F1.
4.) e2 = d2 · x and q2 = e2 · vn. Moreover, during the computation of e2 · vn we do not enter a
ﬁnal state in F2 (but e2 ∈F2 is possible).
If Hk(L1, L2) is regular, then there exists a factorization xyαv = µδβδµ where |δ| = k and
p2 · µδβδ ∈F2 (which implies δβδµv∗u ⊆L2).
Proof. The conditions imply that uvsxyαvtu ∈Hk(L1, L2) for all s ≥t ≥n. Moreover, by 3.)
the hairpin completion can be achieved with a preﬁx in L1 and the longest preﬁx of uvsxyαvtu
belonging to L1 is uvsxyα.
If Hk(L1, L2) is regular, then we have uvsxyαvs+1u ∈Hk(L1, L2), too, as soon as s is large
enough, by a simple pumping argument. For this hairpin completion we must use a suﬃx belonging
to L2. For y = 1 this follows from x < vα. For y ̸= 1 we use x < vα and additionally that the
word xa with a = y(1) is not a preﬁx of vα.
By 4.) the longest suﬃx of uvsxyαvs+1u belonging to L2 is a suﬃx of xyαvs+1u. Thus, we
can write
uvsxyαvs+1u = uvsxyαvvsu = uvsµδβδµvsu
9


## Page 10


where δβδµvsu ∈L2 and |δ| = k. We obtain xyαv = µδβδµ.
(Recall that our second DFA A2 accepts L2.) Hence, as p2 = q02 · u and p2 = p2 · v, we see
that p2 · µδβδ ∈F2.
We conclude as desired: if Hk(L1, L2) is regular, then p2 · µδβδ ∈F2.
Example 3.15. Let us take a look at Figure 2 again. Let A = (Q0, t1, t2, 0), v = a and u = 1. If
we choose x = a, y = b and (d1, d2) = (p1, p2) we can see, that conditions 1.) to 4.) of Lemma 3.14
are satisﬁed but there is no factorization abaa = µδβδµ with |δ| = k such that δβδµu ∈L2. Hence,
the hairpin completion is not regular.
The next lemma yields another suﬃcient condition that Hk(L1, L2) is not regular.
Lemma 3.16. The existence of words x, y ∈Σ∗and states (d1, d2) ∈Q1 × Q2 satisfying 1.) to
4.) of Lemma 3.14, but where for all factorizations xyαv = µδβδµ we have p2 · µδβδ /∈F2 can be
decided in NL.
Proof. It is enough to perform either Test 2 or 3 below (non-deterministically chosen) and to
prove the NL performance of these tests. The tests distinguish whether the word y is empty or
non-empty.
Test 2: Decide the existence of a word x ∈Σ∗and states (d1, d2) ∈Q1 × Q2 satisfying 1.) to 4.)
of Lemma 3.14 with y = 1, but where for all factorizations xαv = µδβδµ we have p2 · µδβδ /∈F2.
If we ﬁnd such a situation, then output that Hk(L1, L2) is not regular.
Test 3: Decide the existence of words x, y ∈Σ∗with y ̸= 1 and states (d1, d2) ∈Q1×Q2 satisfying
1.) to 4.) of Lemma 3.14, but where for all factorizations xyαv = µδβδµ we have p2 · µδβδ /∈F2.
If we ﬁnd such a situation, then output that Hk(L1, L2) is not regular.
The correctness of both tests follows by Lemma 3.14 and they can be performed as follows: For
both tests we guess the length of a word x which satisﬁes 1.) and which is therefore a preﬁx of vα.
Thus we can remember x, because vα is available by the input. We guess states (d1, d2) ∈Q1×Q2,
and verify that conditions 3.) and 4.) hold, which is easy because we can reconstruct x. For Test 2
we check that p1 · x = d1 and p2 · α = d2. Then we have to test whether for all factorizations
xαv = µδβδµ with |δ| = k the condition p2 · µδβδ /∈F2 holds. This can easily be done in NL
because we have full access to the word xαv.
Test 3 is a bit more tricky. We guess a ∈Σ and we check that xa is not a preﬁx of vα.
We have to verify that a path from c1 to d1 exists which is labelled by some non-empty word
y ∈aΣ∗and that a path from c2 to d2 exists which is labelled by y. This can be achieved by a
graph reachability algorithm which uses forward edges in the DFA of L1 and simultaneously uses
backwards edges in the DFA of L2. Now, in a factorization xyαv = µδβδµ we cannot have that
x is a proper preﬁx of µδ otherwise xa would be a preﬁx of vα. But this was excluded by the
choice of a. Thus, µδ is a preﬁx of x and δµ is a suﬃx of x. This means, to ensure that there is
no factorization with p2 · µδβδ ∈F2, we do not need to remember the word y. We just compute
d2 · x and during this computation we validate that there are no ﬁnal states in F2 after k or more
steps.
We claim that, if all three tests did not yield that the hairpin completion Hk(L1, L2) is not
regular, then the hairpin completion is indeed regular. This will complete the proof of Theorem 3.1.
Lemma 3.17. Suppose no outcome of Tests 1, 2, and 3 is “not regular”.
Then the hairpin
completion Hk(L1, L2) is regular.
10


## Page 11


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
Figure 6: Runs through A1 and A2 for the word π. We assume f1 ∈F1.
Proof. Let π ∈Hk(L1, L2). Write π = γαβαγ with |γ| minimal such that either γαβα ∈L1
or αβαγ ∈L2. By symmetry we assume γαβα ∈L1. We may also assume that |γ| > 2n4 (cf.
Proposition 3.9 and Test 0). We can factorize γ = uvw with |uv| ≤n4 and 1 ≤|v| ≤|w| such that
there are runs as in Figure 6.
We infer from Test 1 that wα is a preﬁx of some word in v+. We may assume that w ∈v+ by
adjusting the choices of u, v, and w. (Possibly, u gets longer but it is still shorter than n4, v is
transposed, and w gets shorter.)
Hence, we can write wαβ = vmxy with m ≥0 such that vmx is the maximal common preﬁx
of wαβ and some word in v+ with α ≤x < vα.
We see that for some s ≥t ≥0 we can write
π = uvsxyαvtu.
Moreover, uvsxyαvtu ∈Hk(L1, L2) for all s ≥t ≥0. There are only ﬁnitely many choices for
u, v, x (due to the lengths bounds) and for each of them there is a regular set Ry associated to the
ﬁnite collection of bridges such that
π ∈

uvsxRyαvtu
 s ≥t ≥0
	
⊆Hk(L1, L2).
More precisely, we can choose Ry = {1} for y = 1, and otherwise we can choose
Ry ∈{B(c1, c2, d1, d2) ∩aΣ∗| (c1, c2, d1, d2) is a bridge and a ∈Σ} .
Note that the sets

uvsxRyαvtu
 s ≥t ≥0
	
are not regular, in general. If we bound however
the exponent t by n, then the ﬁnite union
[
0≤t≤n

uvsxRyαvtu
 s ≥t
	
becomes regular. Thus, we may assume that t > n. Let e2 = p2 · αyx. We have e2 · vn = q2 and,
if there is a ﬁnal state during the computation of e2 · vn, then for all t ≥s ≥n and y ∈Ry we
have that uvsxyαvtu ∈Hk(L1, L2), due to a suﬃx in L2, and uvnv+xRyαv+vnu ⊆Hk(L1, L2).
Otherwise Test 2 or 3 tells us that for all y ∈Ry the word xyαv has a factorization µδνδµ
such that |δ| = k and p2 · µδνδ ∈F2. The paths q02 · u = p2 and p2 · v = p2 yield δνδµv∗u ⊆L2
and, again, uvnv+xRyαv+vnu ⊆Hk(L1, L2).
The hairpin completion Hk(L1, L2) is a ﬁnite union of regular languages and hence it is regular
itself.
4
Conclusion and open problems
We have shown that the problem to decide the regularity of hairpin completion Hk(L1, L2) for
given regular languages L1 and L2 is NL-complete. In particular it can be solved eﬃciently in
parallel with Boolean circuits of polynomial size and poly-log depth, because NL is contained in
Nick’s Class NC2 (see e.g. [18, Thm. 16.1]).
11


## Page 12


Our NL-result is based on the fact that the input is given by DFAs accepting L1 and L2. It is
open, what happens if the input is given in a more concise form, say the input is given by NFAs
accepting L1 and L2 (or L2).
Another result of [4] says that the time complexity of the same problem is in O(n8). The full
proof of this fact is quite involved, and it employs diﬀerent ideas. It will appear elsewhere. It
is open whether the O(n8) time bound is optimal. A further improvement on this time bound
seems however to ask for quite diﬀerent ideas. So far, the best algorithm known (to us) considers
all pairs of states in the automaton A. There are Ω(n8) pairs and it is unclear how to avoid this
bound.
There is also a very natural variant of hairpin completion which was introduced in [5]. It has
been called partial hairpin completion and further investigated in [14], where the operation has
been called hairpin lengthening. The partial hairpin completion of L1 and L2 is given by the set
of words γαβαγ′, where γ′ is a preﬁx γ and γαβα ∈L1 or γ is a preﬁx γ′ and αβαγ′ ∈L2.
Again, the partial hairpin completion of a regular language is linear context-free, but not
regular, in general.
It is open whether regularity of the partial hairpin completion of regular
languages is decidable.
References
[1] C. `Alvarez and B. Jenner. A note on logspace optimization. Comput. Complex., 5:155–166,
April 1995.
[2] D. Cheptea, C. Mart´ın-Vide, and V. Mitrana. A new operation on words suggested by DNA
biochemistry: Hairpin completion. Transgressive Computing, pages 216–228, 2006.
[3] R. Deaton, R. Murphy, M. Garzon, D. Franceschetti, and S. Stevens. Good encodings for
DNA-based solutions to combinatorial problems. Proc. of DNA-based computers DIMACS
Series, 44:247–258, 1998.
[4] V. Diekert and S. Kopecki. Complexity results and the growths of regular languages (extended
abstract). In M. Domaratzki and K. Salomaa, editors, CIAA 2010, number 6482 in Lecture
Notes in Computer Science, pages 105–114. Springer-Verlag, 2011.
[5] V. Diekert, S. Kopecki, and V. Mitrana. On the hairpin completion of regular languages.
In M. Leucker and C. Morgan, editors, ICTAC, volume 5684 of Lecture Notes in Computer
Science, pages 170–184. Springer, 2009.
[6] M. Garzon, R. Deaton, P. Neathery, R. Murphy, D. Franceschetti, and E. Stevens.
On
the encoding problem for DNA computing. The Third DIMACS Workshop on DNA-Based
Computing, pages 230–237, 1997.
[7] M. Garzon, R. Deaton, L. Nino, S. Stevens Jr., and M. Wittner. Genome encoding for DNA
computing. Proc. Third Genetic Programming Conference, pages 684–690, 1998.
[8] J. E. Hopcroft and J. D. Ulman. Introduction to Automata Theory, Languages and Compu-
tation. Addison-Wesley, 1979.
[9] M. Ito, P. Leupold, F. Manea, and V. Mitrana. Bounded hairpin completion. Information
and Computation, In Press, Accepted Manuscript:–, 2010.
[10] L. Kari, S. Konstantinidis, E. Losseva, P. Sos´ık, and G. Thierrin. Hairpin structures in DNA
words. In A. Carbone and N. A. Pierce, editors, DNA, volume 3892 of Lecture Notes in
Computer Science, pages 158–170. Springer, 2005.
12


## Page 13


[11] L. Kari, K. Mahalingam, and G. Thierrin. The syntactic monoid of hairpin-free languages.
Acta Inf., 44(3-4):153–166, 2007.
[12] S. Kopecki. On the iterated hairpin completion. In Y. Gao, H. Lu, S. Seki, and S. Yu, editors,
Developments in Language Theory, volume 6224 of Lecture Notes in Computer Science, pages
438–439. Springer Berlin / Heidelberg, 2010.
[13] F. Manea, C. Mart´ın-Vide, and V. Mitrana. On some algorithmic problems regarding the
hairpin completion. Discrete Applied Mathematics, 157(9):2143–2152, 2009.
[14] F. Manea, C. Mart´ın-Vide, and V. Mitrana. Hairpin lengthening. In F. Ferreira, B. L¨owe,
E. Mayordomo, and L. M. Gomes, editors, CiE, volume 6158 of Lecture Notes in Computer
Science, pages 296–306. Springer, 2010.
[15] F. Manea and V. Mitrana. Hairpin completion versus hairpin reduction. In S. B. Cooper,
B. L¨owe, and A. Sorbi, editors, CiE, volume 4497 of Lecture Notes in Computer Science,
pages 532–541. Springer, 2007.
[16] F. Manea, V. Mitrana, and T. Yokomori. Two complementary operations inspired by the
DNA hairpin formation: Completion and reduction. Theor. Comput. Sci., 410(4-5):417–425,
2009.
[17] F. Manea, V. Mitrana, and T. Yokomori. Some remarks on the hairpin completion. Int. J.
Found. Comput. Sci., 21(5):859–872, 2010.
[18] Ch. H. Papadimitriou. Computatational Complexity. Addison Wesley, 1994.
[19] K. Sakamoto, H. Gouzu, K. Komiya, D. Kiga, S. Yokoyama, T. Yokomori, and M. Hagiya.
Molecular Computation by DNA Hairpin Formation. Science, 288(5469):1223–1226, 2000.
13

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
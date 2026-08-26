---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1906.11742v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1906.11742v1_A_Game_Model_for_Proofs_with_Costs

> Source: 1906.11742v1_A_Game_Model_for_Proofs_with_Costs.pdf

> Pages: 21

---


## Page 1


arXiv:1906.11742v1  [cs.LO]  27 Jun 2019
A Game Model for Proofs with Costs
Timo Lang1 and Carlos Olarte2 and Elaine Pimentel2
and Christian G. Ferm¨uller1 ⋆
1 TU-Wien, Austria
2 Universidade Federal do Rio Grande do Norte, Brazil
Abstract. We look at substructural calculi from a game semantic point
of view, guided by certain intuitions about resource conscious and, more
speciﬁcally, cost conscious reasoning. To this aim, we start with a game,
where player P defends a claim corresponding to a (single-conclusion)
sequent, while player O tries to refute that claim. Branching rules for ad-
ditive connectives are modeled by choices of O, while branching for mul-
tiplicative connectives leads to splitting the game into parallel subgames,
all of which have to be won by player P to succeed. The game comes
into full swing by adding cost labels to assumptions, and a corresponding
budget. Diﬀerent proofs of the same end-sequent are interpreted as more
or less expensive strategies for P to defend the corresponding claim. This
leads to a new kind of labelled calculus, which can be seen as a fragment
of SELL (subexponential linear logic). Finally, we generalize the concept
of costs in proofs by using a semiring structure, illustrate our interpre-
tation by examples and investigate some proof-theoretical properties.
1
Introduction
Various kinds of game semantics have been introduced to characterize compu-
tational features of substructural logics, in particular fragments and variants of
linear logic (LL) [11]. This line of research can be traced back to the works of
Blass [5,6], Abramsky and Jagadeesan [1], Hyland and Ong [12], Lamarche [14],
Japaridze [13], Melli`es [16], Delande et al. [8], among several others.
Our particular view of game semantics is that it is not just a technical tool
for characterizing provability in certain calculi, but rather a playground for illu-
minating speciﬁc semantic intuitions underlying certain proof systems. Specially,
we aim at a better understanding of resource conscious reasoning, which is often
cited as a motivation for substructural logics.
In a ﬁrst step, we characterize a version of linear logic (exponential-free aﬃne
inuitionistic linear logic aIMALL, or, equivalently, Full Lambek Calculus with
exchange and weakening FLew) by a game, where the diﬀerence between additive
and multiplicative connectives is modeled as sequential versus parallel continu-
ation in game states that directly correspond to sequents. More precisely, every
branching rule for a multiplicative connective corresponds to a game rule that
⋆Olarte and Pimentel are funded by CNPq, CAPES and the project FWF START
Y544-N23. Lang is supported by FWF project W1255-N23.


## Page 2


2
Lang, Olarte, Pimentel and Ferm¨uller
splits the current run of the game into two independent subgames. Player P, who
seeks to establish the validity of a given sequent, has to win all the resulting sub-
games. In contrast, a branching rule for an additive connective is modeled by a
choice of player O between two possible succeeding game states, corresponding
to the premises of the sequent rule in question. Note that this amounts to a
deviation from the paradigm “formulas as games”, underlying the game seman-
tic tradition initiated by Blass [5]. Our games are, at least structurally, closer to
Lorenzen’s game for intuitionistic logic [15], where a state roughly corresponds to
a situation in which a proponent seeks to defend a particular statement against
attacks from an opponent, who, in general, has already granted a bunch of other
statements. This kind of semantics for linear logic (but without the sequen-
tial/parallel distinction) was ﬁrst explored in [10].
As long as we only care about the existence of winning strategies, the distinc-
tion between sequential and parallel subgames is redundant. However, our model
not only highlights the intended semantics, but it also has concrete eﬀects once
we introduce prices for resources (represented by formulas) into the game. This
is done via unary operators ▼a and ▽a, a ∈R+, which share some characteristic
features with subexponentials in LL (SELL [7,18]). The intuition is that a formula
▽aA is a single use resource with price a: By paying a, we can “unpack” ▽aA
to obtain the formula A, and ▽aA is destroyed in the process. On the other
hand, ▼aA denotes a permanent resource: From ▼aA we can obtain A as often
as we want, each time paying the price a. We lift our game to the extended
language by enriching game states with a budget that is decreased whenever a
price is paid. Diﬀerent strategies for proving the same endsequent can then be
compared by the budget which they require to be run safely, i.e. without getting
into debts. This form of resource consciousness not only enhances the game, but
it also translates into a novel sequent system, where cost bounds for proofs are
attached as labels to sequents.
We observe that, up to this point, we only considered resources in assump-
tions. This is translated to sequents by restricting negatively the occurrences of
the modalities ▼a and ▽a. Thus a promotion rule is not present and the proof-
theoretic properties of the proposed systems, such as cut-elimination, can be
mimicked by the ones of aIMALL. We hence move towards two possible gen-
eralizations. First, we propose a broader notion of cost and prices (for both the
game and corresponding calculi) beyond the domain of the non-negative real
numbers. For this, we organize the labels/prices in a semiring structure that
enables for the instantiation of several interesting concrete examples, having the
same game-theoretic characterization. Second, we discuss the quest of allowing
modalities also in positive contexts, showing the limitations of such approach.
Organization and contributions. Section 2 deﬁnes the basic game for aIMALL
and establishes the correspondence between winning strategies and proofs. Sec-
tion 3 introduces the concept of prices and budgets into the game. The exis-
tence of cost-minimal strategies is shown in Section 3.1 and cut-admissibility is
discussed in Section 3.2. In Section 4, the concept of prices is generalized and
several examples of our interpretation of costs in proofs are presented. In Section


## Page 3


Derivations with Costs
3
Sequent System for C
Γ, A, B −→C
Γ, A ⊗B −→C ⊗L
∆1 −→A
∆2 −→B
∆1, ∆2 −→A ⊗B
⊗R
∆1 −→A
∆2, B −→C
∆1, ∆2, A −◦B −→C
−◦L
Γ, A −→B
Γ −→A −◦B −◦R
Γ, Ai −→B
Γ, A1 & A2 −→B &Li
Γ −→A
Γ −→B
Γ −→A & B
&R
Γ, A −→C
Γ, B −→C
Γ, A ⊕B −→C
⊕L
Γ −→Ai
Γ −→A1 ⊕A2
⊕Ri
Γ, p −→p I
Γ −→1 1R
Γ, 0 −→A 0L
Sequent System for C(R+)
▼Γ, ∆1 −→A
▼Γ, ∆2 −→B
▼Γ, ∆1, ∆2 −→A ⊗B
⊗R
▼Γ, ∆1 −→A
▼Γ, ∆2, B −→C
▼Γ, ∆1, ∆2, A −◦B −→C
−◦L
Γ, ▼aA, A −→C
Γ, ▼aA −→C
▼L
Γ, A −→C
Γ, ▽aA −→C ▽L
Fig. 1. Sequent systems C and C(R+)
5, the challenge of extending the semantics to full subexponential linear logic is
discussed. Section 6 concludes the paper.
2
A game model of branching
Our starting point is a calculus for aﬃne intuitionistic linear logic without ex-
ponentials (aIMALL) [11], whose calculus is also equivalent to FLew, the Full
Lambek calculus with exchange and weakening. We denote this calculus simply
by C for brevity. Formulas in C are built from the grammar
A ::= p | 0 | 1 | A1 −◦A2 | A1 ⊗A2 | A1 & A2 | A1 ⊕A2.
where p stands for atomic propositions (variables); 0/1 are the false/true units;
−◦denotes linear implication; ⊗/& are the multiplicative/additive conjunctions;
and ⊕is the additive disjunction.
We shall use A, B, C (resp. Γ, ∆) to range over formulas (resp. multisets of
formulas). The rules are in Fig. 1. Note that the cut rule is not included in our
presentation of C and that weakening is present only implicitly, via the context
Γ in the initial sequents. Furthermore, in rule I, p is a propositional variable.
We shall write ⊢C S if the sequent S is provable in C.
We shall characterize C proofs as winning strategies (w.s.) in a certain game.
Usually, one can interpret bottom-up proof search in sequent systems as a game,
where at any given state, player P ﬁrst chooses a formula of a sequent and, in
the next step, either P moves to the premise sequent of the corresponding in-
troduction rule (if the rule has only one premise); or player O chooses a premise
sequent in which the game continues (if the rule has more than one premise).
Alternatively, rather than letting player O choose the subgame, one may stipu-
late that the game splits into independent subgames, all of which player P has
to win. At ﬁrst glance, these two approaches might seem diﬀerent. However, the


## Page 4


4
Lang, Olarte, Pimentel and Ferm¨uller
diﬀerence is only of interpretation and it does not aﬀect the (non-)existence of
w.s.’s for P. To see this, note that, by deﬁnition of a w.s., player P has to be
prepared to answer to every possible choice of her opponent O. Therefore, it does
not matter whether we require P to actually win every subgame or whether we
image P to play a single run where she wins irrespectively of O’s choices. Hence,
the two interpretations are equivalent in terms of P’s w.s.’s but they provide
diﬀerent viewpoints of branching sequent rules. Going more into detail, we can
see that this equivalence holds as long as the parallel games are independent. We
will break this independence later on by introducing a budget which is shared
among parallel games (see Section 3).
The distinguishing feature of the game GC below is: branching in additive rules
is modeled as choices of O, whereas in branching multiplicative rules, P splits
the context into two disjoint parts, which then form the corresponding contexts
of two subgames to be played in parallel. Consequently, a state of the game is
represented by a multiset of sequents, each belonging to a separate subgame.
Deﬁnition 1 (The game GC). GC is a game of two players, P and O. Game
states (denoted by G, H) are ﬁnite multisets of sequents. GC proceeds in rounds,
initiated by P’s selection of a sequent S from the current game state. The succes-
sor state is determined according to rules that ﬁt one of the following schemes:
(1) G ∪{S}
⇝
G ∪{S′}
(2) G ∪{S}
⇝
G ∪{S1} ∪{S2}
In (1), the subgame S changes to S′. In (2), the subgame S splits into two
subgames S1 and S2. Here is the complete description of a round: After P has
chosen a sequent S among the current game state, she chooses a principal for-
mula in S and a matching rule instance r of C such that S is the conclusion of
that rule. Depending on r, the round proceeds as follows:
1. If r is a unary rule with premise S′, then the game proceeds in the game
state G ∪{S′} (no interaction of O is required).
2. Parallelism: If r is a binary rule with premises S1, S2 pertaining to a multi-
plicative connective, then the game proceeds in the game state G∪{S1}∪{S2}
(again, no interaction of O is required).
3. O-choice: If r is a binary rule with premises S1, S2 pertaining to an additive
connective, then O chooses S′ ∈{S1, S2} and the game proceeds in the game
state G ∪{S′}.
A winning state (for P) is a game state consisting of initial sequents of C only,
that is, sequents having one of the forms (Γ, p −→p), (Γ, 0 −→A), (Γ −→1).
Example 2. As an example of a round in GC, assume that the game starts with
∆−→A ⊗B. P might select A ⊗B as the principal formula. For the choice of a
matching instance of the rule ⊗R, she also has to choose a partition ∆= ∆1∪∆2.
The game then continues in the state {(∆1 −→A), (∆2 −→B)}.
The following deﬁnitions are standard in game theory.


## Page 5


Derivations with Costs
5
Deﬁnition 3 (Plays and strategies). A play of GC on a game state H is a
sequence H1, H2, . . . , Hn of game states, where H1 = H and each Hi+1 arises
by playing one round on Hi. A strategy (for P) on a game state H is deﬁned
as a function telling P how to move in any given state. A strategy on H is a
winning strategy (w.s.) if all plays following it eventually reach a winning
state. We shall write |=GC H if P has a w.s. on the game state H.
Given w.s.’s π1, . . . , πn for sequents S1, . . . , Sn, there is an obvious w.s. for
the game state {S1, . . . , Sn} which could be speciﬁed as “play according to πi
in the subgame Si”. Not all w.s.’s for {S1, . . . , Sn} need to arise in such a way
though, since in principle it is allowed that moves in a subgame Si depend on the
moves in another subgame Sj. Nevertheless, since in the game GC valid moves
and the winning conditions in all subgames are independent, we can restrict to
strategies of the former kind. This observation is encapsulated as follows.
Lemma 4 (Independence ). |=GC {S1, . . . , Sn}
iﬀ
for all i ≤n, |=GC Si
Strategies in a game can be pictured as trees of game states, and therefore strate-
gies share a common form with proofs. In our case, game states are multisets of
sequents. However, by virtue of the above lemma, we obtain a notation of win-
ning strategies which uses single sequents as nodes, at least if the initial state of
the game is a sequent.
Theorem 5 (Adequacy for GC). Let S be a sequent. Then |=GC {S} iﬀ⊢C S.
Proof:
(⇐) is a straightforward induction on the length of proofs. (⇒) is
proved by induction on a w.s. (the maximal number of moves which can occur
following it). We only present the case where Lemma 4 comes into play. Assume
that the state is ∆1, ∆2 −→A ⊗B and π tells P to choose the instance of ⊗R
with premises ∆1 −→A and ∆2 −→B. By parallelism, the successor state is
{(∆1 −→A), (∆2 −→B)}. Since π is a w.s., it must contain a substrategy π′
for {(∆1 −→A), (∆2 −→B)}. By Lemma 4, we may assume that π′ is of the
form: “Use π1 to play in the subgame ∆1 −→A and π2 to play in ∆2 −→B”
for some w.s.’s π1, π2 for ∆1 −→A and ∆2 −→B respectively. By induction,
there are C-proofs Ξ1, Ξ2 for the sequents ∆1 −→A and ∆2 −→B. Applying
⊗R below Ξ1 and Ξ2, we obtain a C-proof Ξ of ∆1, ∆2 −→A ⊗B.
⊓⊔
3
Adding costs
To increase the expressiveness of our framework, we now augment assumptions
with costs, where assumptions are formulas occurring negatively on sequents.
Costs will be modeled—for now—by elements of R+, the set of non-negative
real numbers. Formally, we add the unary modal operators ▼a and ▽a for each
a ∈R+ to our language and call the resulting formulas extended formulas. An
extended formula ▽aA can be considered as a single use resource with price a:
By paying a, we can “unpack” ▽aA to A (and ▽aA is destroyed in the process).
On the other hand, ▼aA is a permanent resource: We can obtain as many copies
of A from it as we want, each time paying the price a.


## Page 6


6
Lang, Olarte, Pimentel and Ferm¨uller
Deﬁnition 6. An extended sequent is a sequent built from extended formulas
in which subformulas ▼aA and ▽aA occur only in negative polarity.
The notion of polarity is the standard one: A subformula occurrence in the
antecedent of a sequent is negative if it occurs in the scope of an even number
(including 0) of contexts ([·] −◦B), and otherwise it is positive. For occurrences
of a subformula in the consequent, one replaces “even” by “odd”. For instance,
▽ap⊗p′, (▼bq−◦q′)−◦q′′ −→▼cr−◦r′ is an extended sequent. We denote by ▼Γ
a set of formulas preﬁxed with ▼a for some (not necessarily the same) a ∈R+.
We introduce a game GC(R+) similarly as we did for GC. The rules of GC(R+)
make reference to the calculus C(R+) of Fig. 1. It is obtained by interpreting all
sequents as extended sequents, replacing the rules ⊗R and −◦L as indicated in
Fig. 1 (for internalizing contraction) and adding the dereliction rules
Γ, ▼aA, A −→C
Γ, ▼aA −→C
▼L
Γ, A −→C
Γ, ▽aA −→C ▽L
Note that there is no right rules for ▼and ▽in C(R+) since they only appear
in negative polarity.
Remark 7. C(R+) can be naturally seen as a fragment of subexponential linear
logic (SELL [7]). More speciﬁcally, let aSELL(Ru
b) be a single conclusion calculus
for SELL with weakening, and let Σ = ⟨R+ × {b, u}, ⪯, U⟩be the subexponential
signature where the set of unbounded subexponentials (that can be weakened
and contracted at will) is U = {(a, u) | a ∈R+}, and ⪯is any partial order on
R+×{b, u} in which, as standardly required in SELL, no bounded subexponential
is above an unbounded one. We identify the subexponential !(a,b) with ▽a and
!(a,u) with ▼a. Then C(R+) is precisely the subsystem of aSELL(Ru
b) given by
the syntactic restriction that subexponentials occur only in negative polarity. We
will exploit this relation between C(R+) and aSELL(Ru
b) later in Section 3.2.
For some remarks on the system without the syntactic restriction, see Section 5.
Let us return to the game now. The main diﬀerence between GC and GC(R+)
is that game states in the latter will involve a budget (modeled as a real number)
which will decrease whenever rules ▼L and ▽L are invoked.
Deﬁnition 8 (The game GC(R+)). GC(R+) is a game of two players, P and
O. Game states are tuples (H, b), where H is a ﬁnite multiset of extended se-
quents and b ∈R is a “budget”. GC proceeds in rounds, initiated by P’s selection
of an extended sequent S from the current game state. The successor state is
determined according to rules that ﬁt one of the two following schemes:
(1) (G ∪{S}, b)
⇝
(G ∪{S′}, b′)
(2) (G ∪{S}, b)
⇝
(G ∪{S1} ∪{S2}, b)
A round proceeds as follows: After P has chosen an extended sequent S ∈H
among the current game state, she chooses a rule instance r of C(R+) such that
S is the conclusion of that rule. Depending on r, the round proceeds as follows:


## Page 7


Derivations with Costs
7
1. If r is a unary rule diﬀerent from ▼L, ▽L with premise S′, then the game
proceeds in the game state (G ∪{S′}, b).
2. Budget decrease: If r ∈{▼L, ▽L} with premise S′ and principal formula
▼aA or ▽aA, then the game proceeds in the game state (G ∪{S′}, b −a).
3. Parallelism: If r is a binary rule with premises S1, S2 pertaining to a mul-
tiplicative connective, then the game proceeds as (G ∪{S1} ∪{S2}, b).
4. O-choice: If r is a binary rule with premises S1, S2 pertaining to an additive
connective, then O chooses S′ ∈{S1, S2} and the game proceeds in the game
state (G ∪{S′}, b).
A winning state (for P) is a game state (H, b) such that all S ∈H are initial
sequents of C(R+) and b ≥0.
Plays and strategies are deﬁned as in GC. We write |=GC(R+) (H, b) if P has a w.s.
in the GC(R+)-game starting on (H, b). The intuitive reading of |=GC(R+) (H, b) is:
The budget b suﬃces to win the game H. From now on, we will just say “sequent”
and “formula” instead of “extended sequent” and “extended formula”.
Example 9. Consider the state ({▼1p, ▽3q −→p ⊗q}, 5). In a ﬁrst move, P
picks p ⊗q and she ﬁnds a partition of the premises not preﬁxed with ▼and
decides that ▽3q goes to the right premise of ⊗R. So by parallelism, the new
state is ({(▼1p −→p), (▼1p, ▽3q −→q)}, 5). She now chooses to pick ▼1p of
the ﬁrst component and, by budget decrease, her budget decreases and the
next state is ({(▼1p, p −→p), (▼1p, ▽3q −→q)}, 4). Now P picks ▽3q leading to
({(▼1p, p −→p), (▼1p, q −→q)}, 1). Since both components are initial sequents
and budget ≥0, this is a winning state for P.
Similarly to GC, it is not necessary to consider all possible strategies in
GC(R+): For example, P never needs to take the budget into account when
deciding the next move. (A rule of thumb for P could be: always play econom-
ical, i.e. avoid the rules ▼L and ▽L whenever possible.) It is easy to see that
a C(R+)-proof Ξ of a sequent S translates to a w.s. in (S, b) for some suﬃciently
large budget b. Taking these observations together, one can prove the following:
Theorem 10 (Weak adequacy for GC(R+)). Let S be a sequent. Then
∃b

|=GC(R+) ({S}, b)

iﬀ
⊢C(R+) S
The proof is similar to the one of Theorem 5. We call this theorem weak adequacy
since information about the budget b is lost in the proof theoretic representation.
In other words, the game GC(R+) is more expressive than the calculus C(R+). To
overcome this discrepancy, we now introduce a labelled extension of C(R+) that
we call Cℓ(R+). A Cℓ(R+)-proof is build from labelled sequents Γ −→b A where
Γ −→A is an extended sequent and b ∈R+. The complete system is given in
Fig. 2. Our aim is to prove that |=GC(R+) ({Γ −→A}, b)
iﬀ
⊢Cℓ(R+) Γ −→b A.
To this end, we need an analogue of Lemma 4 (independency of subgames in
GC) for GC(R+). Note that crucially, the naive analogue
|=GC(R+) ({S1, . . . , Sn}, b)
iﬀ
for all i ≤n, |=GC(R+) ({Si}, b)


## Page 8


8
Lang, Olarte, Pimentel and Ferm¨uller
labelled sequent system for Cℓ(R+)
Γ, A, B −→b C
Γ, A ⊗B −→b C ⊗L
▼Γ, ∆1 −→a A
▼Γ, ∆2 −→b B
▼Γ, ∆1, ∆2 −→a+b A ⊗B
⊗R
▼Γ, ∆1 −→a A
▼Γ, ∆2, B −→b C
▼Γ, ∆1, ∆2, A −◦B −→a+b C
−◦L
Γ, A −→b B
Γ −→b A −◦B −◦R
Γ, Ai −→b B
Γ, A1 & A2 −→b B &Li
Γ −→a A
Γ −→b B
Γ −→max{a,b} A & B &R
Γ, A −→a C
Γ, B −→b C
Γ, A ⊕B −→max{a,b} C
⊕L
Γ −→b Ai
Γ −→b A1 ⊕A2
⊕Ri
Γ, ▼aA, A −→c C
Γ, ▼aA −→c+a C ▼L
Γ, A −→c C
Γ, ▽aA −→c+a C ▽L
Γ, p −→0 p I
Γ −→0 1 1R
Γ, 0 −→0 A 0L
Γ −→a A
Γ −→b A wℓ(b ≥a)
Fig. 2. The labelled sequent system Cℓ(R+)
does not hold: Having a w.s. in ({S1, . . . , Sn}, b) is not the same as having
w.s.’s in all ({Si}, b)’s, since the budget b is shared between the subgames in
GC(R+). However, one can prove that there are strategies in GC(R+) which are
independent up to a partition of the budget. More precisely,
Lemma 11 (Quasi-independency of subgames in GC(R+)).
|=GC(R+) ({S1, . . . , Sn}, b) iﬀ
∃b1, . . . , bn ≥0 s.t. Pn
i=1 bi ≤b and for all i ≤n, |=GC(R+) ({Si}, bi).
Proof:
The direction from right to left is obvious. For the other direction,
assume that P has a w.s. π for ({S1, . . . , Sn}, b). We may assume wlog that this
strategy is composed of strategies π1, . . . , πn for the subgames S1, . . . , Sn which
are both independent from each other and from the budget. In each subgame
Si, let τi be a strategy for O which maximizes the cost bi (the total decrease of
the budget) of playing πi against τi. Then |=GC(R+) ({Si}, bi). Furthermore, from
τ1, . . . , τn player O can compose a strategy τ such that when played against π
in the parallel game {S1, . . . , Sn}, the costs for P sum up to Pn
i=1 bi. Since π is
a w.s. for ({S1, . . . , Sn}, b), it must be the case that Pn
i=1 bi ≤b.
⊓⊔
We emphasize that the game rules of GC(R+) do not force P to know a par-
tition of the budget in order to play parallel subgames. Nevertheless, Lemma 11
tells us that ﬁnding such a partition is always possible in principle (for an om-
nipotent player P). Now we can prove the desired correspondence.
Theorem 12 (strong adequacy for GC(R+)).
|=GC(R+) ({Γ −→A}, b)
iﬀ
⊢Cℓ(R+) Γ −→b A.


## Page 9


Derivations with Costs
9
Proof:
(⇐) By induction on the length of a proof Ξ of Γ −→b A. We highlight
two cases. Consider the following two possible ends for Ξ:
(1)
Γ −→c C
Γ −→d D
Γ −→max{c,d} C & D &R
(2)
∆1 −→c C
∆2 −→d D
∆1, ∆2 −→c+d C ⊗D
⊗R
In both cases, by induction, there are w.s.’s π1 and π2 for: (1) the game states
({Γ −→C}, c) and ({Γ −→D}, d); and (2) the game states ({∆1 −→C}, c) and
({∆2 −→D}, d) respectively. The needed w.s.’s π& for the game state ({Γ −→
C & D}, max{c, d}) and π⊗for the game state ({∆1, ∆2 −→C ⊗D}, c + d) are:
(1)π&: Choose the instance of &R as above. By O-choice, the successor
game state is either ({Γ −→C}, max{c, d}) or ({Γ −→D}, max{c, d}).
In any case, the budget in the successor state is greater or equal than
both c and d, so P can continue playing according to π1 resp. π2.
(2)π⊗: Choose the instance of ⊗R as above. By parallelism, the succes-
sor state is ({∆1 −→C, ∆2 −→D}, c + d). Use π1 to play the subgame
∆1 −→C and π2 to play in ∆2 −→D. By assumption on π1 and π2, the
total costs when playing both strategies in parallel cannot exceed c + d.
(⇒) By induction on the length of a strategy π . We present only the case where
Lemma 11 is used. Assume that the state is ({∆1, ∆2 −→C ⊗D}, b) and π tells
P to choose the instance of ⊗R with premises ∆1 −→C and ∆2 −→D. By
parallelism, the successor state is ({∆1 −→C, ∆2 −→D}, b). Since π is a w.s.,
it must contain a substrategy π′ for this state. By Lemma 11, we may assume
that π′ is composed of substrategies π1, π2 for the game states ({∆1 −→C}, c)
and ({∆2 −→D}, d) where c + d ≤b. By induction, there are C-proofs Ξ1, Ξ2
for the sequents ∆1 −→c C and ∆2 −→d D. Applying ⊗R and wℓbelow Ξ1 and
Ξ2, we obtain a C-proof Ξ of ∆1, ∆2 −→b C ⊗D.
⊓⊔
Let Sb denote the labelled sequent corresponding to the sequent S with la-
bel b. Given Π a Cℓ(R+)-proof of Sb, we deﬁne the many-to-one onto skeleton
function SK(Π) as the C(R+)-proof Ξ of S obtained by removing all labels and
applications of wℓfrom Π. Conversely, we deﬁne the one-to-one decoration func-
tion D(Ξ) as the Cℓ(R+)-proof Πℓof Sa, obtained by assigning the label 0 to
all initial sequents of Ξ and propagating the labels downwards according to the
rules of Cℓ(R+). We deﬁne cost(Ξ) := a. Let Λ ∈SK−1(Ξ) be a proof of Sc.
It is easy to see that a ≤c, that is, cost(Ξ) is the minimal label which can be
attached to S w.r.t. Ξ. In game theoretic terms, this means the following.
Theorem 13. Given a C(R+)-proof Ξ of a sequent S, cost(Ξ) is the smallest
budget which suﬃces to win the game GC(R+) on S when following the strategy
corresponding to Ξ.
Example 14. Consider the following well-known riddle:
You have white and black socks in a drawer in a completely dark room.
How many socks do you have to take out blindly to be sure of having a
matching pair?


## Page 10


10
Lang, Olarte, Pimentel and Ferm¨uller
We can model the matching pair by the disjunction (w⊗w)⊕(b⊗b), and the act
of drawing a random sock by the labelled formula ▼1(w⊕b). The above question
then becomes:
For which n is the sequent ▼1(w ⊕b) −→n (w ⊗w) ⊕(b ⊗b) provable?
The following proof shows that n = 3 suﬃces:
G, w, w, w ⊕b −→0 w ⊗w ⊗R, I
G, w, w, w ⊕b −→0 F
⊕R
G, w, b, w −→0 (w ⊗w) ⊗R, I
G, w, b, w −→0 F
⊕R
G, w, b, b −→0 b ⊗b ⊗R, I
G, w, b, b −→0 F
⊕R
G, w, b, w ⊕b −→0 F
⊕L
G, w, w ⊕b, w ⊕b −→0 F
⊕L
Ξ
G, w ⊕b, w ⊕b, w ⊕b −→0 F
⊕L
G −→3 F
3 × ▼L
where derivation Ξ is symmetric, F = (w ⊗w) ⊕(b ⊗b) and G = ▼1(w ⊕b).
3.1
The spectrum of a provable sequent
Due to weakening on labels, many proofs in Cℓ(R+) of labelled sequents of the
form Sb correspond to one skeleton proof in C(R+) of the sequent S. On the
other hand, S may have, itself, many proofs in C(R+), each of them having a
cost, uniquely determined by the decoration D. In this section we will consider
the spectrum of such costs and prove the existence of a minimal one.
Deﬁnition 15. spec(S) := {cost(Ξ) | Ξ is a C(R+)-proof of S}.
For example, spec(▼1p, ▽0.8p, ▽0.8p −→p⊗p) consists of the numbers {1.6, 1.8, 2.6}
and all combinations n+k·0.8 where n, k are natural numbers and n ≥2, k ≤2.
A subset X ⊆R is called discrete if, for every x ∈X, there is an open interval
I ⊆R such that I ∩X = {x}. We can prove:
Theorem 16. For any sequent S, spec(S) ⊆R+ is discrete and closed.
Proof:
Let a1, . . . , an denote all real numbers appearing as ▼a or ▽a in S, and
let us denote by Ω(a1, . . . , an) the set of all linear combinations of a1, . . . , an
over N, i.e., Ω(a1, . . . , an) := {k1 · a1 + . . . + kn · an | k1, . . . , kn ∈N}. By
inspecting the rules of Cℓ(R+) and since wℓis not applied in D(Ξ), it is easy to
see that cost(Ξ) ∈Ω(a1, . . . , an), and hence spec(S) ⊆Ω(a1, . . . , an). It suﬃces
to show that each bounded monotone sequence in Ω(a1, . . . , an) is eventually
constant. We may assume wlog that all the ai’s are nonzero. Now consider a
sequence (ki
1 · a1 + . . . + ki
n · an)i≥1 in Ω(a1, . . . , an), and assume that B is an
upper bound for it (a trivial lower bound is always 0). Pick a number K such
that K · min{a1, . . . , an} > B. It follows that for all i, j we have ki
j < K. In
particular, there are only ﬁnitely many diﬀerent terms in the sequence, from
which our claim follows.
⊓⊔
Since any bounded below, closed set in R has an minimum, we obtain:
Corollary 17. If ⊢C(R+) Γ −→A, then spec(Γ −→A) has a least element. In
other words, there is a smallest b such that ⊢Cℓ(R+) Γ −→b A.


## Page 11


Derivations with Costs
11
Corollary 17 tells us that cost-optimal strategies for all provable sequents exist,
but note that the proof is not constructive. Nevertheless, we may now deﬁne:
cost(S) :=
(
min(spec(S))
if ⊢C(R+) S
∞
otherwise
3.2
Cut admissibility
So far, the results about our game semantics GC(R+) did not depend essentially
on the chosen calculus C(R+). We now want to relate proof-theoretic properties
of C(R+) and Cℓ(R+) to the game semantics. Recall that C(R+) can be seen as
a fragment of aSELL(Ru
b), arising from the syntactic restriction that the modal
operators ▽a, ▼a occur only negatively in sequents (Remark 7); consequently,
there is no corresponding right rule (promotion) in C(R+). This has the eﬀect
that—even though (implicit) contraction on formulas ▼aA is present in C(R+)—
the proof theory of C(R+) is closer to aIMALL than to aSELL(Ru
b).
C(R+) inherits the admissibility of the following cut rule from aSELL(Ru
b)
▼Γ, ∆1 −→A
▼Γ, ∆2, A −→C
▼Γ, ∆1, ∆2 −→C
cut
Note that, appearing both in a positive and a negative context, the cut formula A
cannot contain any modal operator.
Now, let us extend cut admissibility to the labelled system Cℓ(R+). Assume
that both ▼Γ, ∆1 −→a A and ▼Γ, ∆2, A −→b C are provable in Cℓ(R+). For-
getting labels a and b, we can conclude, from cut-admissibility in C(R+), that
⊢C(R+) ▼Γ, ∆1, ∆2 −→C. But then, ▼Γ, ∆1, ∆2 −→c C is also provable in
Cℓ(R+) with, e.g., c = cost(▼Γ, ∆1, ∆2 −→C) (see Cor. 17). Hence, stating
cut-admissibility in Cℓ(R+) strongly depends on the possibility of deﬁning a
computable function f relating c with the labels of the premises of the cut rule.
We show that f(a, b) = a + b is the minimal such function.
Theorem 18. For f(a, b) = a+b, the following cut rule is admissible in Cℓ(R+):
▼Γ, ∆1 −→a A
▼Γ, ∆2, A −→b C
▼Γ, ∆1, ∆2 −→f(a,b) C
cutℓ
Moreover, whenever cutℓis admissible w.r.t. a given f ′, then a + b ≤f ′(a, b).
Proof:
For cut admissibility, one can follow the standard cut reduction strat-
egy of aIMALL and observe that it is compatible with the proposed labelling
of the cut rule. Consider for instance the following reduction (note that max{a+
c, a + d} = a + max{c, d}):
▼Γ, ∆1 −→a A
▼Γ, ∆2, A −→c C
▼Γ, ∆2, A −→d D
▼Γ, ∆2, A −→max{c,d} C & D
&R
▼Γ, ∆1, ∆2 −→a+max{c,d} C & D
cutℓ
⇝


## Page 12


12
Lang, Olarte, Pimentel and Ferm¨uller
▼Γ, ∆1, −→a A
▼Γ, ∆2, A −→c C
▼Γ, ∆1, ∆2 −→a+c C
cutℓ
▼Γ, ∆1, −→a A
▼Γ, ∆2, A −→d D
▼Γ, ∆1, ∆2 −→a+d D
cutℓ
▼Γ, ∆1, ∆2 −→max{a+c,a+d} C & D
&R
For the minimality, let p, q be distinct propositional variables. For any a, b ∈
R+ we have proofs of ▼ap −→a p
and
p, ▼bq −→b p⊗q. Applying cut, we get
▼ap, ▼bq −→c p ⊗q. Now, ▼ap, ▼bq −→c p ⊗q is provable (without cut) only if
a + b ≤c. Hence if f makes the cut rule admissible, a + b ≤f(a, b).
⊓⊔
One can easily show that also weakening in the antecedent is admissible
in Cℓ(R+) and does not lead to an increased label. Similarly, generalized axioms
Γ, A −→0 A are admissible: Appearing both positively and negatively, A does not
contain modal operators, and hence cost(Γ, A −→A) = cost(A −→A) = 0.
Example 19. Consider a labelled transition system (T, =⇒) where T is a set of
states and =⇒⊆T ×R+×T is the transition relation on states. In (ti, ai, t′
i) ∈=⇒,
simply written as ti
ai
=⇒t′
i, ai is interpreted as the time needed for the transition
to happen. We use distinct propositional variables to represent states. Moreover,
the formula ▼ai(ti −◦t′
i) models the transition ti
ai
=⇒t′
i. We shall use ∆=⇒to
denote the set of such formulas. Given two sets of states Sstart, Send ⊆T , it is
easy to see that the following sentences are equivalent:
1. From every state in Sstart, there is a state in Send reachable in time ≤a
2. |=GC(R+) ({∆=⇒, L Sstart −→L Send}, a)
Hence by Theorem 12, both are equivalent to
3. ⊢Cℓ(R+) ∆=⇒, L Sstart −→a
L Send.
One common way to obtain (1) is by ﬁnding a set of intermediary states Si
and a splitting of the time a1 + a2 = a such that we can go from each state
in Sstart to some state in Si in time a1, and from each state in Si to some
state in Send in time a2. In terms of (3), this strategy corresponds to a cut:
Assume we have proofs Ξ1 and Ξ2 of the sequents ∆=⇒, L Sstart −→a1
L Si
and ∆=⇒, L Si −→a2
L Send. By cut admissibility (Theorem 18) we obtain the
desired ∆=⇒, L Sstart −→a1+a2
L Send as the result of the “concatenation”of
the paths encoded in Ξ1 with the paths encoded in Ξ2.
4
Alternative cost structures
We have used non-negative real numbers for representing costs and budgets,
together with basic operations for accumulating (+) and comparing (≥) them.
This allowed us to give a more interesting perspective of resource consumption
in linear logic: we know that the cost of using a formula marked with cost 3 is
not the same as derelicting a formula marked with cost 7. A natural question
that arises is whether it is possible to consider other systems governing the way
we understand costs and budgets. In this section, we consider sequent systems
Cℓ(K) in which the real numbers of Cℓ(R+) (see Fig. 2) are replaced by elements


## Page 13


Derivations with Costs
13
of a semiring K. As we shall see, the structure of K determines the behavior of
the system and the interpretation of costs and budgets.
A commutative semiring is a tuple K = ⟨A, +A, ×A , ⊥A, ⊤A⟩satisfying: (S1)
A is a set and ⊥A, ⊤A ∈A; (S2) +A and ×A are binary operators that make the
triples ⟨A, +A, ⊥A⟩and ⟨A, ×A, ⊤A⟩commutative monoids; (S3) ×A distributes
over +A (i.e., a ×A (b +A c) = (a ×A b) +A (a ×A c)); and (S4) ⊥A is absorbing
for ×A (i.e., a ×A ⊥A = ⊥A); K is absorptive if it additionally satisﬁes (S5)
a+A (a×A b) = a; in absorptive semirings, +A is idempotent, that is, a+A a = a.
This allows for the deﬁnition of the following partial order: a ⪯A b iﬀa +A b = b
(and then, a ×A b ⪯A a); an absorptive semiring K is idempotent whenever its
×A operator is idempotent.
Absorptive semirings satisfy some additional properties [3]: ⊥A (resp. ⊤A) is
the bottom (resp. top) of A; a +A ⊤A = ⊤A; +A coincides with the lubA (least
upper bound) operator; if a +A b ∈{a, b}, ∀a, b ∈A then (A, ⪯A) is a total
order; a ×A b ⪯A glbA(a, b), where glbA is the greatest lower bound operator; if
K is idempotent, then +A distributes over ×A and ×A coincides with glbA.
We identify costs as elements of A. We can naturally consider ⊤A (resp. ⊥A)
as the “best” (resp. “worst”) cost. Dually, ⊤A (resp. ⊥A) is the “worst” (resp.
“best”) budget. Also, we expect the accumulating operator to be commutative
and associative (S2). Moreover, accumulating costs gives rise to a “worse” cost
(S5). Hence, the ×A operator is used to combine costs (+, on R+, in Fig. 2). On
the other hand, +A is used to select which is the “best” value, in the sense that
a +A b = a iﬀb ⪯A a iﬀa is “better” than b (i.e., ⪯A will replace ≥in Fig. 2).
Finally, we generalize max (in Fig. 2) as glbA. As mentioned above, in the case of
idempotent semirings, ×A coincides with the glbA while in the non-idempotent
case accumulating costs often gives a “worse” result than the glbA.
Note that the rules ▽a
L and ▼a
L, in Fig. 2, the budget c in the conclusion
must be of the form a + b. In the particular case of R+, we know that b = c −a
whenever c ≥a. Hence, from a conclusion with budget c we obtain a premise with
decreased budget c −a. In the general case, we guarantee that such splitting
of the budget (also present in rules ⊗R and −◦L) is possible by requiring K to
be invertible in the following sense: K is invertible if for all b ⪯A a, the set
I(b, a) = {x ∈A | a ×A x = b} is non-empty and admits a minimum. We then
denote this minimum by b÷Aa. Observe that, in all our examples, if b ⪯A a then
the set I(b, a) is a singleton except when a = b = ⊥A. In that case, I(b, a) = A
and we set ⊥A ÷A ⊥A = ⊥A. In Remark 22 we explain and clarify this choice.
In what follows, K will always denote an absorptive and invertible semiring.
Deﬁnition 20 (System Cℓ(K)). Let K = ⟨A, +A, ×A, ⊥A, ⊤A⟩be an absorptive
and invertible semiring. The system Cℓ(K) is obtained from Cℓ(R+) (Fig. 2) by
replacing 0 with ⊤A, + with ×A, max with glbA, and ≥with ⪯A. Similarly, we
obtain C(K) as a generalization of C(R+) (Fig. 1).
Just as C(R+) can be seen as a fragment of aSELL(Ru
b), the system C(K) is
a fragment of aSELL(Ku
b), i.e. aﬃne subexponential linear logic with subex-
ponentials taken from the set K × {u, b}. We omit the (rather straightforward)
formulation of the corresponding game semantics.


## Page 14


14
Lang, Olarte, Pimentel and Ferm¨uller
Next we present some instances of Cℓ(K) and their intended behavior.
Example 21 (Costs). Kc = ⟨R∞
+ , minR, +R, ∞, 0⟩, where R∞
+ is the completion
of R+ with ∞, reﬂects the meaning of costs in Section 3. If a, b ̸= ∞and b ≥a
(i.e., b ⪯A a), there is a unique way of splitting b into a + b′, namely, b′ = b −a
(i.e., b′ = b ÷A a). Alternatively, we may interpret the elements in Kc as 2D
areas. Then, a label b ̸= ∞in a sequent can be understood as the total area
available to place some objects. Each time an object of size a is placed (using
▼aL or ▽aL) we observe, bottom-up, that the total area is decreased to b −a.
Remark 22 (Meaning of ÷ and ∞). Consider the semiring Kc above (where
⊥A = ∞and ⊤A = 0). If the label in the sequent is b = ⊥A, regardless the
value a in an application of ▽a
L or ▼a
L, the premise will be labelled with ∞.
This is because, according to our deﬁnition, ⊥A ÷ ⊥A = ⊥A. This makes sense
since we select the most “generous” budget to continue the derivation. Of course,
smaller suitable budgets are also allowed due to rule wℓ. For instance, the sequent
▽⊥p, ▽⊥(p −◦q) −→b q is provable in Cℓ(Kc) only if b = ⊥A. The same sequent
(removing the label b) is also provable in aSELL(Ku
b). Note that if we decree
that ⊥A ÷ ⊥A = ⊤A (as in [3]), then the sequent above would not be provable
for any b.
Example 23 (Protected resources). Let Kc/p = ⟨{pub, conf}, +, ×, pub, conf⟩and
deﬁne a + b = pub iﬀa = b = pub and a × b = conf iﬀa = b = conf. The
intuition is that ▼pubF represents public information (and then not conﬁden-
tial) and ▼confF represents secret information. Observe that no derivation of
Γ, ▼pubF −→conf G can apply ▼L on ▼pubF (since conf ̸⪯pub). This means
that only conﬁdential (or protected) resources can be used in such a derivation.
Alternatively, we can show that, if Γ −→conf G is provable then Γ ′ −→conf G′
is also provable where Γ ′ is as Γ but replacing any formula of the form ▼pubF
with the constant 1 (similarly for G and ▽pubF). Kc/p is nothing less that the
structure Sc = ⟨{false, true}, ∨, ∧, false, true⟩[4].
Example 24 (Maximum amount of resources). Consider now the situation where
labels in sequents represents a certain amount of computational resources, e.g.,
RAM, available to process a series of tasks. Moreover, let us interpret ▽cF as
the fact that, in order to produce F, c resources need to be used. As expected,
once F is produced, the c resources can be released and freed to be used in other
tasks. The idea is to know what is the least amount of resources b s.t. some jobs
Γ can be all of them executed, sequentially if needed.
Consider Kmax = ⟨R∞
+ , min, max, ∞, 0⟩where b ÷ a = b (if b ≥a). Let t1, t2
be atomic propositions representing tasks and let Γ = {▽at1, ▽ct2}. Clearly, the
sequents Γ −→b t1 ⊗t2 and Γ −→b t1 & t2 are both provable if b = max(a, c).
Of course, if we start with more resources, e.g., b = a + c, the sequent is still
provable (rule wℓ). Interestingly, from the point of view of costs, the diﬀerence
between concurrent (⊗) and sequential choices (&) vanishes in this particular
scenario, since Kmax is idempotent (and hence glbA and ×A coincide).


## Page 15


Derivations with Costs
15
Example 25 (Transition systems revisited). Consider the formulas of the shape
▼ai(ti −◦t′
i) and the sequent ∆=⇒, t −→b t′ in Example 19. The interpretation
there, of b as the time needed to observe a transition from t to t′, can be captured
with the semiring Kc (Example 21). As expected, according to +A (and then ⪯A),
we prefer “faster” paths when there are diﬀerent ways of going from t to t′.
Another possible interpretation for b is the probability of the diﬀerent inde-
pendent events (transitions) to happen. Hence, given a speciﬁc path from t to t′,
the possible values for b must be less or equal to the product of the probabilities
ai involved in that path. This behavior can be captured with the probabilistic
semiring [4] Kp = ⟨[0, 1], max, ×, 0, 1⟩.
For yet another example of Kp, consider the typical probabilistic choice in
process calculi: the process P +α Q chooses P with probability α and Q with
probability 1−α. Following the process-as-formulas interpretation [17,9], relating
process constructors with logical connectives and reductions with proof steps,
the system Cℓ(Kp) oﬀers a very natural interpretation of the process P +α Q as
the formula (▽αP) & (▽1−αQ), that we can write as P &α Q. For instance, if
Γ = {t1 &α t2, t1 −◦t3, t2 −◦t4}, then, the sequent Γ −→b t3 (resp. Γ −→b t4) is
provable whenever α ≥b (resp. 1 −α ≥b).
5
Modalities in positive contexts
We have considered modalities appearing only in negative polarity. In this sec-
tion, we show some problems and limitations that arise when trying to extend
the labelled sequent approach to consider also positive occurrences of modali-
ties as in the full system of subexponential linear logic (see e.g., [18]). Let us
call CPℓ(R+) the system resulting from Cℓ(R+) by adding the following labelled
promotion rules
Γ ≤▽a −→b A
Γ −→b ▽aA
Γ ≤▼a −→b A
Γ −→b ▼aA
where Γ ≤▽a denotes all formulas in Γ which are of the form ▽cB or ▼cB and
a ≥c; and Γ ≤▼a denotes all formulas in Γ which are of the form ▼cB where
a ≥c. These rules follow the standard formulation of the promotion rule in SELL:
the promotion of !aA requires all formulas of the context to be of the form !cB
where a ⪯c and ⪯is the underlying preorder on the subexponential signature.
The following result shows that it is not possible to deﬁne a labelled cut rule
for CPℓ(R+) where the label of the conclusion depends exclusively on the labels
of the premises.
Theorem 26. There is no function f : R+ × R+ →R+ such that the rule
▼Γ, ∆1 −→a A
▼Γ, ∆2, A −→b C
▼Γ, ∆1, ∆2 −→f(a,b) C
cut
is admissible in CPℓ(R+).


## Page 16


16
Lang, Olarte, Pimentel and Ferm¨uller
Proof:
Let p, q be diﬀerent propositional variables, and let A⊗n denote the
n-fold multiplicative conjunction of a formula A. The sequents
▼1/kp −→a ▼1/kp⊗(k·a)
and
▼1/kp⊗(k·a) −→b p⊗(k·k·a·b)
are provable in CPℓ(R+) for all natural numbers a, b, k. The smallest label f
which makes their cut conclusion ▼1/kp −→f p⊗(k·k·a·b) provable in CPℓ(R+)
is k · a · b, which is not a function on the premise labels a, b.
⊓⊔
Note that Thm. 26 leaves open the possibility that cut is admissible w.r.t. a
function f which takes more information of the premises into account than just
their labels. Please refer to the appendix for a more detailed discussion.
6
Concluding remarks and future work
We have introduced game semantics for fragments of (aﬃne intuitionistic) linear
logic with subexponentials (SELL [7,18,20]), culminating in labelled extensions
of such systems so that Γ −→b A is interpreted as: “Resource A can be obtained
from the resources Γ with a budget b” or, alternatively, “The budget b suﬃces to
win the game Γ −→A”. For achieving that, we proposed a new interpretation
for the dereliction rule, opposing to the standard controls in the promotion rule:
derelicting on ▽aB, ▼aB means “paying a to obtain (a copy of) B”. Hence our
games and systems oﬀer a neater control of the resources appearing negatively
on sequents.
There are several ways of extending and continuing this work. First of all,
as signalized in Sec. 5, the quest of extending the cost conscious reasoning to
modalities occurring positively in sequents is not trivial. Despite the obvious
game interpretation of promotion that could be given in the style of [10], Thm. 26
shows that this would not be followed with a proof theoretical notion of cut-
elimination, due to the impossibility of deﬁning a functional notion of the cut-
label. In the appendix we discuss some possible paths to trail in this direction.
On the other side, a philosophical discussion on the need of compositionally of
dialogue games driven by a cut rule can also be done [19].
Finally, we expect that the study of costs of proofs and cut-elimination in la-
belled fragments of SELL may indicate a relationship between labels and bounds
of computation [2], as well as give a diﬀerent approach to study the complex-
ity of cut-elimination process, specially in the multiplicative-(sub)exponential
fragment [21,22].
References
1. Samson Abramsky and Radha Jagadeesan. Games and full completeness for mul-
tiplicative linear logic. J. Symb. Log., 59(2):543–574, 1994.
2. Beniamino Accattoli, St´ephane Graham-Lengrand, and Delia Kesner. Tight typ-
ings and split bounds. PACMPL, 2(ICFP):94:1–94:30, 2018.


## Page 17


Derivations with Costs
17
3. Stefano Bistarelli and Fabio Gadducci.
Enhancing constraints manipulation in
semiring-based formalisms. In Gerhard Brewka, Silvia Coradeschi, Anna Perini,
and Paolo Traverso, editors, ECAI 2006, 17th European Conference on Artiﬁcial
Intelligence, Including Prestigious Applications of Intelligent Systems (PAIS 2006),
Proceedings, volume 141 of Frontiers in Artiﬁcial Intelligence and Applications,
pages 63–67. IOS Press, 2006.
4. Stefano Bistarelli, Ugo Montanari, Francesca Rossi, Thomas Schiex, G´erard Ver-
faillie, and H´el`ene Fargier.
Semiring-based csps and valued csps: Frameworks,
properties, and comparison. Constraints, 4(3):199–240, 1999.
5. Andreas Blass. A game semantics for linear logic. Ann. Pure Appl. Logic, 56(1-
3):183–220, 1992.
6. Andreas Blass. Some semantical aspects of linear logic. Logic Journal of the IGPL,
5(4):487–503, 1997.
7. Vincent Danos, Jean-Baptiste Joinet, and Harold Schellinx. The structure of ex-
ponentials: Uncovering the dynamics of linear logic proofs.
In Georg Gottlob,
Alexander Leitsch, and Daniele Mundici, editors, Kurt G¨odel Colloquium, volume
713 of Lecture Notes in Computer Science, pages 159–171. Springer, 1993.
8. Olivier Delande, Dale Miller, and Alexis Saurin. Proof and refutation in MALL as
a game. Ann. Pure Appl. Logic, 161(5):654–672, 2010.
9. Yuxin Deng, Robert J. Simmons, and Iliano Cervesato. Relating reasoning method-
ologies in linear logic and process algebra. Mathematical Structures in Computer
Science, 26(5):868–906, 2016.
10. Christian G. Ferm¨uller and Timo Lang. Interpreting sequent calculi as client-server
games.
In Renate A. Schmidt and Cl´audia Nalon, editors, Automated Reason-
ing with Analytic Tableaux and Related Methods - 26th International Conference,
TABLEAUX 2017, Bras´ılia, Brazil, September 25-28, 2017, Proceedings, volume
10501 of Lecture Notes in Computer Science, pages 98–113. Springer, 2017.
11. Jean-Yves Girard. Linear logic. Theor. Comput. Sci., 50:1–102, 1987.
12. J.M.E. Hyland and C. h. L. Ong. Fair games and full completeness for multiplica-
tive linear logic without the mix-rule, 1993.
13. Giorgi Japaridze. A constructive game semantics for the language of linear logic.
Ann. Pure Appl. Logic, 85(2):87–156, 1997.
14. Fran¸cois Lamarche. Games semantics for full propositional linear logic. In Pro-
ceedings, 10th Annual IEEE Symposium on Logic in Computer Science, San Diego,
California, USA, June 26-29, 1995, pages 464–473. IEEE Computer Society, 1995.
15. Paul Lorenzen. Logik und agon. Atti Del XII Congresso Internazionale di Filosoﬁa,
4:187–194, 1960.
16. Paul-Andr´e Melli`es. Asynchronous games 4: A fully complete model of proposi-
tional linear logic. In 20th IEEE Symposium on Logic in Computer Science (LICS
2005), 26-29 June 2005, Chicago, IL, USA, Proceedings, pages 386–395. IEEE
Computer Society, 2005.
17. Dale Miller. The pi-calculus as a theory in linear logic: Preliminary results. In
Evelina Lamma and Paola Mello, editors, Extensions of Logic Programming, Third
International Workshop, ELP’92, Bologna, Italy, February 26-28, 1992, Proceed-
ings, volume 660 of Lecture Notes in Computer Science, pages 242–264. Springer,
1992.
18. Vivek Nigam and Dale Miller. Algorithmic speciﬁcations in linear logic with subex-
ponentials. In Ant´onio Porto and Francisco Javier L´opez-Fraguas, editors, PPDP,
pages 129–140. ACM, 2009.
19. Catarina Dutilh Novaes and Rohan French. Paradoxes and structural rules from
a dialogue perspective. Philosophical Issues, 28:129–158, 2018.


## Page 18


18
Lang, Olarte, Pimentel and Ferm¨uller
20. Elaine Pimentel, Carlos Olarte, and Vivek Nigam. A proof theoretic study of soft
concurrent constraint programming. TPLP, 14(4-5):649–663, 2014.
21. Lutz Straßburger. MELL in the calculus of structures. Theor. Comput. Sci., 309(1-
3):213–285, 2003.
22. Lutz Straßburger and Alessio Guglielmi. A system of interaction and structure IV:
the exponentials and decomposition. ACM Trans. Comput. Log., 12(4):23:1–23:39,
2011.


## Page 19


Derivations with Costs
19
A
Appendix
A.1
Cut elimination for CPℓ(K)
Consider the labelled sequent system CPℓ(K) built from Cℓ(K) (see Def. 20) by
dropping the restriction on occurrences of modalities and adding the following
labelled promotion rules (see Section 5)
Γ ⪯▽a −→b A
Γ −→b ▽aA
Γ ⪯▼a −→b A
Γ −→b ▼aA
where Γ ⪯▽a denotes all formulas in Γ which are of the form ▽cB or ▼cB and
a ⪯A c; and Γ ⪯▼a denotes all formulas in Γ which are of the form ▼cB where
a ⪯A c. We shall explore diﬀerent fragments and (admissible) cut-like rules
that can be proposed for such a calculus. For concreteness, we consider the case
K = Kc (Example 21). But note, however, the discussion below applies for any
absorptive, invertible semiring K.
We start by observing that the inclusion of “worse costs” (∞in the reals,
⊥A in the semiring) entails a trivial labelling that makes cut admissible. In
the following theorem, the cut formula F is an arbitrary formula (containing,
possibly, positive and/or negative occurrences of the modalities ▼a or ▽a).
Theorem 27 (cut∞Rule). The following rule is admissible in CPℓ(K)
▼Γ, ∆1 −→a F
▼Γ, ∆2, F −→b C
▼Γ, ∆1, ∆2 −→∞C
cut∞
The proof follows the same steps of the cut-elimination proof for SELL, using
natural extensions of invertibility and permutability of rules to the labelled case.
It is worth noticing that the sole responsible for the impossibility result of
Thm. 26 is the explosive combination of the use of tensor/implication and con-
traction, that is, SELL’s multiplicative-(sub)exponential fragment. Hence, lim-
iting the occurrence of one or the other leads to more amenable results. For
example, Thm. 18 can be straightforwardly extended for formulas not contain-
ing the modality ▼a (but ▽a may occur).
Theorem 28 (Linear cuts). Let F be a formula with no occurrences of ▼a.
Then, the following rule is admissible in CPℓ(K)
▼Γ, ∆1 −→a F
▼Γ, ∆2, F −→b C
▼Γ, ∆1, ∆2 −→a+b C
cutL
Moreover, if Γ −→a C is provable using cutL, then there is a cut-free proof of
Γ −→a′ C with a ≥a′.
Proof:
The cut-elimination procedure is rather standard. Let us present the
case when the cut formula is ▽cF:
(▼Γ, ∆1)≤▽c −→a F
▼Γ, ∆1 −→a ▽cF
▼Γ, ∆2, F −→b C
▼Γ, ∆2, ▽cF −→b+c C
▼Γ, ∆1, ∆2 −→a+b+c C
cutL


## Page 20


20
Lang, Olarte, Pimentel and Ferm¨uller
reduces to
(▼Γ, ∆1)≤▽c −→a F
▼Γ, ∆2, F −→b C
▼Γ, ∆1, ∆2 −→a+b C
cutL
⊓⊔
Still, forcing cut formulas to be linear seems to be a very severe restriction to
impose. A better approach is given by keeping an exact track of the use of
contraction in the cut-elimination process. The idea is that, if proving F costs
a, then any use of F must pay this “extra cost”. In order to keep track of this
extra cost, we introduce the following notation.
Deﬁnition 29. Let E = {ab | a, b ∈R∞
+ } be such that
1. ab +E cd = a + b + c + d.
2. ab ≥E ac (i.e., the ordering ≥E ignores the subindices).
3. ab >E cd iﬀa > c.
For any formula F ∈CPℓ(K), we deﬁne [F]c as the formula that substitutes any
modality ▼ab with ▼ab+c.
Hence CPℓ(K) can be slightly modiﬁed so that sequent labels belong to R∞
+ ,
while modal labels belong to E. Due to the ordering above, the promotion of
▼a0 has the same eﬀect/constraints that the promotion of ▼ab. However, the
dereliction of the latter requires a greater budget (a + b instead of a). Moreover,
the equivalence ▼abF ≡▼acF can be proven, each direction requiring a diﬀerent
budget. Finally, note that E0 = {a0 | a ∈R∞
+ } ≃R∞
+ , that is, each element
a ∈R∞
+ can be seen as the equivalence class of a0 in R∞
+ × R∞
+ modulo R∞
+ .
We will abuse the notation and continue representing the resulting system by
CPℓ(K), also unchanging the representation of sequents.
The following lemma has a straightforward proof.
Lemma 30. If Γ, [F]c −→b G then Γ, F −→b′ G with b ≥b′. More generally, if
Γ, [F]c −→b C and c ≥c′ then Γ, [F]c′ −→b′ C with b ≥b′.
The next deﬁnition restricts the appearance of unbounded modalities only under
linear implication.
Deﬁnition 31 (−◦-linear). We say that F is −◦-linear if for all subformulas
of the form A −◦B in F, A does not have occurrences of ▼a.
The following result presents the admissibility of an extended form of the cut
rule, where the budget information from the left premise is passed to the cut-
formula in the right premise. Observe that the label of the conclusion is now a
function of the labels of the premises. Moreover, the cut-reduction is label pre-
serving, meaning that the budget monotonically decreases in the cut-elimination
process.
Theorem 32 (−◦-linear cut). The following rule is admissible
▼Γ, ∆1 −→a F
▼Γ, ∆2, [F]a −→b C
▼Γ, ∆1, ∆2 −→a+b C
cutLL
F is a −◦-linear formula


## Page 21


Derivations with Costs
21
Moreover, if Γ −→a C is provable using cutLL, then there is a cut-free proof of
Γ −→a′ C with a ≥a′.
Proof:
We will illustrate some cases.
– Note that: [▼abF]c = ▼ab+c[F]c; the promotion of ▼abF, bottom-up, results
in a context of ▼formulas (that can be contracted at will); and the dereliction
of ▼ab[F]c decreases the budget in a + b. Hence,
(▼Γ)≤▼ab −→c F
▼Γ, ∆1 −→c ▼abF
▼Γ, ∆2, [F]c, ▼ab+c[F]c −→d C
▼Γ, ∆2, ▼ab+c[F]c −→a+b+c+d C
▼Γ, ∆1, ∆2 −→a+b+2c+d C
reduces to
(▼Γ)≤▼ab −→c F
▼Γ −→c ▼abF
▼Γ, ▼ab+c[F]c, ∆2, [F]c −→d C
▼Γ, ∆2, [F]c −→c+d C
▼Γ, ∆1, ∆2 −→2c+d C
where the “extra cost” ab disappears after the reduction.
– Note that [F ⊗G]c = [F]c ⊗[G]c. Here, let c = c1 + c2:
▼Γ, ∆′
1 −→c1 F
▼Γ, ∆′′
1 −→c2 G
▼Γ, ∆1 −→c F ⊗G
▼Γ, ∆2, [F]c, [G]c −→b C
▼Γ, ∆2, [F ⊗G]c −→b C
▼Γ, ∆1, ∆2 −→b+c C
reduces to
▼Γ, ∆′
1 −→c1 F
▼Γ, ∆′′
1 −→c2 G
▼Γ, ∆2, [F]c1, [G]c2 −→b C
▼Γ, ∆′′
1, ∆2, [F]c1 −→b+c2 C
▼Γ, ∆1, ∆2 −→b+c C
It is worth noticing that in the ﬁrst derivation, the cost c = c1 + c2 is
“charged” to F ⊗G (in the formula [F ⊗G]c) while in the second one, in a
ﬁner way, the cost c1 is charged to F and c2 to G.
– The case of implication explains the restriction we impose. Here b = b1 + b2:
▼Γ, ∆1, F −→c G
▼Γ, ∆1 −→c F −◦G
▼Γ, ∆′
2 −→b1 [F]c
▼Γ, ∆′′
2, [G]c −→b2 C
▼Γ, ∆2, [F −◦G]c −→b C
▼Γ, ∆1, ∆2 −→c+b C
reduces to
▼Γ, ∆′
2 −→b1 F
▼Γ, ∆1, [F]b1 −→c G
▼Γ, ∆′′
2, [G]c −→b2 C
▼Γ, ∆1, ∆′′
2, [F]b1 −→c+b2 C
▼Γ, ∆1, ∆2 −→c+b C
Note that the reduction above is correct since F does not have occurrences
of ▼a and then [F]c = [F]b1 = F.
⊓⊔
This kind of analysis seems to be related with ﬂowgraphs in MELL [21,22].

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1906_11742v1_a_game_model_for_proofs_with_costs
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1906_11742V1_A_GAME_MODEL_FOR_PROOFS_WITH_COSTS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

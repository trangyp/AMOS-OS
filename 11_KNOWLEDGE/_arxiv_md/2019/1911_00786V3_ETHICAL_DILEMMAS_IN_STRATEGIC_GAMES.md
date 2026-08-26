---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.00786v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1911.00786v3_Ethical_Dilemmas_in_Strategic_Games

> Source: 1911.00786v3_Ethical_Dilemmas_in_Strategic_Games.pdf

> Pages: 9

---


## Page 1


Ethical Dilemmas in Strategic Games
Pavel Naumov,1 Rui-Jie Yew2
1 King’s College, Pennsylvania, USA
2 Scripps College, California, USA
pgn2@cornell.edu, ryew8098@scrippscollege.edu
Abstract
An agent, or a coalition of agents, faces an ethical dilemma
between several statements if she is forced to make a con-
scious choice between which of these statements will be true.
This paper proposes to capture ethical dilemmas as a modal-
ity in strategic game settings with and without limit on sac-
riﬁce and for perfect and imperfect information games. The
authors show that the dilemma modality cannot be deﬁned
through the earlier proposed blameworthiness modality. The
main technical result is a sound and complete axiomatization
of the properties of this modality with sacriﬁce in games with
perfect information.
Introduction
In this paper we study ethical dilemmas faced by agents and
coalitions of agents in multiagent systems. As an example,
consider the two diagrams in Figure 1. In the situation de-
picted in the left diagram, an agent must choose between
action left (L) and action right (R). These actions will re-
sult in the death of Alice and Bob, respectively. The right
diagram adds an additional neutral action (N) that results in
the system nondeterministically transitioning either in state
u or state v and killing Alice or Bob, respectively.
w
u
v
L
R
Alice is dead
Bob is dead 
w
u
v
L, N
R, N
Alice is dead
Bob is dead 
Figure 1: Two situations.
The situations represented by these two diagrams are sim-
ilar in many respects. In both of them, in state w the agent
has a strategy to kill Alice (action L) and a strategy to kill
Bob (action R). Additionally, in both settings, the agent will
be blamed for the same outcomes. To claim this, we use
an oft-cited (Widerker 2017) deﬁnition of blameworthiness
through the principle of alternative possibilities: “a person is
morally responsible for what he has done only if he could
Copyright © 2021, Association for the Advancement of Artiﬁcial
Intelligence (www.aaai.org). All rights reserved.
have done otherwise” (Frankfurt 1969). For example, if the
system transitions from state w to state u on either of the di-
agrams, then the agent will be blamed for the death of Alice
because the agent had a strategy (action R) to prevent Alice’s
death. However, the agent is not blamable for the statement
“either Alice or Bob is dead”, because, in both diagrams, the
agent does not have a strategy to prevent the statement from
being true.
However, there is a difference in the types of choices the
agent must make in these two diagrams. In the left diagram,
the agent has to make a hard choice between either con-
sciously killing Alice or consciously killing Bob. On the
right diagram, the agent can avoid this choice by selecting
action N. We say that, on the left diagram, the agent is fac-
ing a moral dilemma between killing Alice and killing Bob,
while on the second diagram the agent does not.
a
b
c
d
Figure 2: Road trafﬁc situation.
As another example, consider the trafﬁc situation depicted
in Figure 2. Here, four pedestrians (red circles in the middle)
are stranded on a busy four-lane highway. Self-driving cars a
and b are on the path to run them over. It is too late for either
of the cars to stop. Car a has three options: to pull left, to
keep driving straight, or to pull right into bus c. Similarly,
car b can pull left, drive straight, or pull right into bus d.
a\b
left
straight
right
left
ϕp
ϕa ∧ϕb
ϕb ∧ϕd
straight
ϕa ∧ϕb
ϕp
ϕb ∧ϕd
right
ϕa ∧ϕc
ϕa ∧ϕc
ϕa ∧ϕb ∧ϕc ∧ϕd
Table 1: Strategic game between cars a and b.
Table 1 shows different outcomes of this strategic game
between players a and b. In this table, letters ϕp, ϕa, ϕb, ϕc,
arXiv:1911.00786v3  [cs.AI]  2 Mar 2021


## Page 2


and ϕd represent the death of the pedestrians, the passengers
in car a, the passengers in car b, some of the passengers in
bus c, and some of the passengers in bus d, respectively.
In this situation car a faces a choice: it can either pull
right or not pull right. In the former case, it is guaranteed to
kill its own passengers as well as some of the passengers in
bus c. In the latter case one of the following is guaranteed
to happen: either pedestrians will die, cars a and car b will
collide, or car b and bus d will collide. In other words, car a
is facing a dilemma between an action that will force ϕa∧ϕc
and the action that will force ϕp ∨(ϕa ∧ϕb) ∨(ϕb ∧ϕd).
We denote this dilemma of car a by formula
[a : ϕa ∧ϕc, ϕp ∨(ϕa ∧ϕb) ∨(ϕb ∧ϕd)].
Similarly, car b is facing dilemma
[b : ϕp ∨(ϕa ∧ϕb) ∨(ϕa ∧ϕc), ϕb ∧ϕd].
(1)
Philosophers distinguish several approaches to morality.
Consequential ethicists judge the moral acceptability of ac-
tions based on their outcomes. For example, a utilitarian
(consequential) ethicist might say that it is morally unac-
ceptable to kill more than a certain number of civil casu-
alties in a military operation. On the other hand, absolute
ethicists ﬁnd certain actions morally unacceptable no matter
what their results are. For example, a Kantian ethicist might
object to pushing the lever in a trolley dilemma in order to
sacriﬁce one person and save ﬁve. Many of such moral con-
straints can be modeled using the cost of sacriﬁce approach
that we propose in this paper. We assign a cost of sacriﬁce to
each action and specify the limit on the acceptable sacriﬁce
for each agent as a subscript of the dilemma modality. For
a utilitarian facing an ethical dilemma, the sacriﬁce is the
number of civil casualties. For the absolute ethicist, sacriﬁce
is +∞for all actions that are not morally acceptable.
The same approach can be used to model constraints im-
posed by laws, regulations, or company policies. For exam-
ple, recently introduced German regulations for autonomous
vehicles state that, when confronted with the choice between
the death of a human being and damage to property, a self-
driving car must always choose the latter (Fabio et al. 2017).
In this case, cost of an action can be deﬁned as the minimal
number of people the action is guaranteed to kill above the
unavoidable minimum. For example, if a hypothetical car is
choosing between four actions that are guaranteed to kill 5,
9, 5, and 7 people respectively, then the costs of these ac-
tions are 0, 4, 0, and 2. The German rule would require a car
to select one of the two actions with zero cost.
According to Car and Driver magazine, Mercedes-Benz
manager of driver assistance systems and active safety
Christoph von Hugo stated that “If you know you can save
at least one person, at least save that one. Save the one in the
car. ... If all you know for sure is that one death can be pre-
vented, then that’s your ﬁrst priority.” (Taylor 2016). This
potential policy for future Mercedes-Benz self-driving ve-
hicles deﬁnes the cost of an action as the minimal number
of people inside the vehicle the action is guaranteed to kill
above the unavoidable minimum. The policy also sets the
allowed sacriﬁce in terms of this cost to zero.
Let us now assume that car a (but not car b) in Figure 2
is a self-driving vehicle made by Mercedes-Benz. Under the
above policy1, the car will never choose to pull into bus c.
Thus, car a is now facing a vacuous one-option dilemma that
any action that the car takes will result in statement ϕp ∨
(ϕa ∧ϕb) ∨(ϕb ∧ϕd) being true. We write this as
[a : ϕp ∨(ϕa ∧ϕb) ∨(ϕb ∧ϕd)]a,b7→0,+∞,
where sacriﬁce function a, b 7→0, +∞assigns the maximal
sacriﬁce that each agent is ready to tolerate. In our case, the
limit on the number of people inside the vehicle that car a
is ready to sacriﬁce is 0. Car b does not have any ﬁxed sac-
riﬁce limit, which we interpret as the value of the sacriﬁce
function for agent b being +∞. Note that although agent b
in this situation does not have a sacriﬁce limit, the limit on
the sacriﬁce of agent a modiﬁes not only a’s dilemma but b’s
as well. Compare the following statement to statement (1):
[b : ϕp ∨(ϕa ∧ϕb), ϕb ∧ϕd]a,b7→0,+∞.
If self-driving cars a and b decide to cooperate and make a
joint decision, then instead of two individual dilemmas they
face a single multiagent ethical dilemma. Let us ﬁrst assume
that neither of these two vehicles is a Mercedes-Benz. Thus,
they can either (i) kill all pedestrians by driving in two dif-
ferent lanes, (ii) kill passengers in cars a and b by sending
both vehicles for a head-on collision, (iii) collide car a with
bus c, or (iv) collide car b with bus d:
[a, b : ϕp, ϕa ∧ϕb, ϕa ∧ϕc, ϕb ∧ϕd]a,b7→+∞,+∞.
Recall that if a is a Mercedes-Benz car, then it is restricted
from pulling right into bus c because this action is guar-
anteed to kill passengers inside car a. Note, however, that,
though there is always the chance that car b pulls left and
crashes into car a, there is no guarantee that car a will col-
lide with car b. Thus, the same Mercedes-Benz policy does
not restrict car a from pulling left. Let us now consider the
case where both a and b are Mercedes-Benz vehicles making
a joint decision. Does the policy restrict them from a joint
decision under which car a drives straight and car b pulls
left? In other words, is the policy a restriction on individual
actions of Mercedes-Benz cars or a restriction on joint deci-
sions of all Mercedes-Benz vehicles? If the former is true, as
it is in the formal model described in this paper, then coali-
tion {a, b} is facing a dilemma between killing all pedestri-
ans and a head-on collision: [a, b : ϕp, ϕa∧ϕb]a,b7→0,0. If the
latter is true, then the two vehicles must either drive straight
or both of them must pull left. In any case, the pedestrians
will die: [a, b : ϕp]a,b7→0,0. Although Christoph von Hugo
did not explicitly specify that this policy applies to individ-
ual vehicles, we think this is the case. If the policy were
to apply to coalitions, then one might face a new version
of the trolley dilemma when a ﬂeet of Mercedes-Benz ve-
hicles might choose to sacriﬁce the life of a passenger in
a Mercedes-Benz vehicle in order to safe the lives of two
passengers in another Mercedes-Benz vehicle. This seems
1Mercedes-Benz later retracted this policy stating that “to make
a decision in favor of one person and thus against another is not
legally permissible in Germany” (Orlove 2016).


## Page 3


to contradict von Hugo’s claim that the ﬁrst priority should
be the prevention of even one death of a passenger in a
Mercedes-Benz self-driving vehicle.
Overview
The rest of this paper is organized as follows. First, we
describe the syntax and formal semantics of the ethical
dilemma modality [C : ϕ1, . . . , ϕn]s in a strategic game
setting. Then, we review literature on ethical dilemmas and
compare the dilemma modality to the earlier studied blame-
worthiness and coalition power modalities. In particular, we
show that the dilemma modality cannot be deﬁned through
the blameworthiness modality even in the single-agent set-
ting without sacriﬁce. We also demonstrate how our deﬁ-
nition of ethical dilemma can be extended to games with
imperfect information. Finally, we give a complete axiom-
atization of our modality in the perfect information case.
The proof of completeness is in the full version of this pa-
per (Naumov and Yew 2019).
Strategic Game with Normalized Costs
Recall from the introduction that if an autonomous vehicle
is confronted with the choice between four actions that are
guaranteed to kill 5, 9, 5, and 7 people respectively, then the
costs of these actions are 0, 4, 0, and 2. In other words, we
assume that costs are “normalized” so that at least one of
them is zero.
Deﬁnition 1 A function f : X →[0, +∞] is normalized if
there is an element x ∈X such that f(x) = 0.
The strategic games with normalized costs that we de-
ﬁne bellow are very similar to “resource-bounded action
frames” used in the semantics of Resource Bounded Coali-
tion Logic (Alechina et al. 2011). By XY we denote the set
of all functions from set Y to set X. Throughout the paper
we assume a ﬁxed set of propositional variables and a ﬁxed
set of agents A.
Deﬁnition 2 A game is a tuple (W, M, ∆, | · |, π), where
1. W is a set of states,
2. ∆is a set of “actions”,
3. M ⊆W × ∆A × W is a relation, called “mechanism”,
4. |d|a
w ∈[0, +∞] is the “cost” of action d ∈∆for a ∈A in
state w ∈W, such that |d|a
w is normalized as a function
of action d for any ﬁxed values a ∈A and w ∈W,
5. π(p) is a subset of W for each propositional variable p.
We refer to functions in set ∆A as complete action pro-
ﬁles of the game. Informally, mechanism M captures the
rules of the game. Namely, (w, δ, u) ∈M if under com-
plete action proﬁle δ the game can transition from state w
to state u. Our semantics is slightly more general than in
(Alechina et al. 2011) because we assume that mechanism
is a relation and not necessarily a function. In other words,
we allow a complete action proﬁle to transition the game
into one of several different states. Our approach also allows
some complete action proﬁles to result in no next state at all.
We interpret this as a termination of the game. We normal-
ize the costs of actions in order to avoid a situation when,
for a given sacriﬁce, an agent would not have any actions to
choose from. Note that Deﬁnition 2 allows actions with inﬁ-
nite costs. We further discuss such actions in the conclusion.
Syntax
In this paper we assume a ﬁxed set A of agents. By a coali-
tion we mean any nonempty subset of A. By a sacriﬁce
function we mean an arbitrary function from set A to set
[0, +∞]. It represents the maximal cost of the sacriﬁce that
each individual agent is ready to bear.
The language Φ of our logical system is deﬁned by the
grammar ϕ := p | ¬ϕ | ϕ →ϕ | [C : X]s, where C
is a coalition, X is a nonempty ﬁnite set of formulae, and
s is a sacriﬁce function. We read [C : X]s as “coalition
C under sacriﬁce constraints deﬁned by function s has a
dilemma between consciously forcing one of the statements
in set X to be true”. For the sake of simplicity, we abbrevi-
ate [C :{ϕ1, . . . , ϕn}]s as [C :ϕ1, . . . , ϕn]s. We assume that
Boolean connectives ∧and ∨as well as constants truth ⊤
and false ⊥are deﬁned as usual. By ∧X and ∨X we denote
the conjunction and the disjunction of all formulae in X re-
spectively. As usual, ∧∅and ∨∅are deﬁned to be ⊤and ⊥,
respectively.
Semantics
Throughout this paper, we write f =X g if f(x) = g(x) for
each x ∈X. We also use shorthand notation captured in the
following deﬁnition.
Deﬁnition 3 For any game, any complete action proﬁle δ,
any state w, and any sacriﬁce function s, we write |δ|w ≤s
if |δ(a)|a
w ≤s(a) for each agent a ∈A.
By a strategy of a coalition C in a given game we mean
any function from the set ∆A that assigns an action to each
member of the coalition.
Now, we introduce a key deﬁnition of this paper. Its part
(4) speciﬁes the formal meaning of the multiagent dilemma
modality [C :X]s. Item 4(a) states that any strategy of coali-
tion C forces a speciﬁc statement ϕ ∈X to be true. Item
4(b) states that X is a minimal set with such property.
Deﬁnition 4 For each game (W, ∆, | · |, M, π), each state
w ∈W, and each formula ϕ ∈Φ, the satisfaction relation
w ⊩ϕ is deﬁned recursively:
1. w ⊩p, if w ∈π(p), where p is a propositional variable,
2. w ⊩¬ϕ, if w ⊮ϕ,
3. w ⊩ϕ →ψ, if w ⊮ϕ or w ⊩ψ,
4. w ⊩[C :X]s, if
(a) for any strategy t ∈∆C of coalition C there is a for-
mula ϕ ∈X such that for any action proﬁle δ ∈∆A
and any state u ∈W if |δ|w ≤s, t =C δ, and
(w, δ, u) ∈M, then u ⊩ϕ,
(b) for any nonempty subset Y ⊊X there is a strategy
t ∈∆C of coalition C such that for any formula ϕ ∈Y
there is an action proﬁle δ ∈∆A and a state u ∈W
where |δ|w ≤s, t =C δ, (w, δ, u) ∈M, and u ⊮ϕ.


## Page 4


We added the minimality condition 4(b) to the above def-
inition in order to eliminate arbitrary irrelevant alternatives
being added to set X. We believe that with this condition the
deﬁnition better reﬂects our intuition of what a dilemma is.
Without item 4(b) the deﬁnition would capture the notion of
weak dilemma that we discuss later.
Recall that we allow a game to terminate as a result of
agents’ actions. For example, suppose that in a state w an
agent a has three actions d1, d2, d3 all of which have a cost
of 1. Let action d1 transition the system into a state in which
statement ϕ1 is true, action d2 transition the system into a
state in which statement ϕ2 is true, and action d3 be an action
that terminates the game. Then, w ⊩[a:ϕ1, ϕ2]a7→1 is true,
because each action of agent a predetermines a speciﬁc ϕi
to be true in each outcome state. In other words, being able
to terminate the system does not provide a way for an agent
to “escape” the dilemma.
We allow set X in statement [C : X]s to be singleton. In
such a case, [C :X]s is not a dilemma in the common sense
of the world, but a “necessary” modality.
Literature Review
The dilemmas that we study in this paper are usually referred
to in the literature as variations of the “trolley dilemma”.
The original trolley dilemma is proposed in (Foot 1967) as a
dilemma faced by an agent who must choose between allow-
ing ﬁve people to die and killing one person to prevent the
death of those ﬁve. The distinction between letting one die
and killing someone is also emphasised in (Thomson 1976,
1984) as well as in (Bruers and Braeckman 2014). Navar-
rete et al. study the same distinction in a virtual reality envi-
ronment (2012).
At the same time, others shift the focus of the trolley
dilemma away from the distinction between letting things
happen and making things happen. Marczyk and Marks
empirically study whether perceived moral permissibility
changed when the person making a decision in the trolley
dilemma stands to beneﬁt from or be harmed by one of the
outcomes (2014). Pan and Slater analyse participants’ eth-
ical reasoning when they were confronted with the trolley
dilemma through an online survey versus through immersive
virtual realities (2011). Chen et al. examine the differences
in brain activity of Chinese undergraduates who experienced
the great Sichuan earthquake when confronted with trolley
dilemmic situations where they must choose to rescue one of
two relatives and one of two strangers (2009). Indick et al.
investigate how the gender of a person affects the decision
that she makes in the trolley dilemma-like settings (2000).
Bleske-Rechek et al. observe that people are less likely to
sacriﬁce the life of one person for the lives of ﬁve if the
one person is young, a genetic relative, or a current romantic
partner (2010). In a related work, Kawai, Kubo, and Kubo-
Kawai show that most people are inclined to sacriﬁce an
older person over a younger one (2014). In this paper, we
also consider trolley-like dilemmas in this broader sense.
Although we are not aware of any works treating dilemma
as a modality, there are papers that use existing logical for-
malism to capture ethical dilemmas. Berreby, Bourgne, and
Ganascia use simpliﬁed event calculus to model dilemmas
within answer set programming (2015). Horty suggests us-
ing nonmonotonic logic for reasoning about moral dilem-
mas (1994). Bonnemains, Saurel, and Tessier propose for-
mal notations for capturing different ethical norms that can
be used in dilemmic settings (2018).
Finally, in this paper we use the cost of a sacriﬁce as a
constraint on agent’s available actions. In a related work,
Halpern and Kleiman-Weiner propose to use the cost of a
sacriﬁce as a degree of blameworthiness (2018).
Ethical Dilemma vs Blameworthiness
In this section we compare the ethical dilemma modality
with blameworthiness modality. We show that the notion of
ethical dilemma proposed in this paper cannot be expressed
through blameworthiness, as deﬁned through the principle
of alternative possibilities: “a person is morally responsi-
ble for what he has done only if he could have done other-
wise” (Frankfurt 1969). In other words, we say that an agent
(or a coalition of agents) is responsible for statement ϕ if ϕ
is true and the agent had a strategy to prevent ϕ. Several for-
mal semantics for blameworthiness as a modality have been
proposed in (Naumov and Tao 2019, 2020a,b).
The ethical dilemma modality, just like most other modal-
ities in logic, captures a property of a state. Blameworthiness
is not a property of a state, but rather of a transition between
states: statement ϕ is true at a current state u, but the agent
had a strategy to prevent it in the previous state w. As a
result, if the language contains blameworthiness modality,
the deﬁnition of satisfaction relation ⊩given in Deﬁnition 4
should be modiﬁed to be a ternary relation (w, u) ⊩ϕ be-
tween two states and a formula.
The goal of this section is to show that the dilemma
modality cannot be deﬁned through blameworthiness modal-
ity. To do this, we ﬁrst translate the deﬁnition of ethical
dilemma given in Deﬁnition 4 into the setting of the two-
state satisfaction relation (w, u) ⊩ϕ. While doing this, we
omit the sacriﬁce subscript, assume that the set of agents A
contains a single ﬁxed agent a, and the set of propositional
variables contains a single variable p. We do this with the
intent to show a stronger result that the dilemma modality
is not expressible through blameworthiness modality even
in this simple case. In this single-agent setting, we denote
coalition strategies and action proﬁles simply by the action
of that ﬁxed agent a.
In this section we consider language Φ0 described by the
grammar ϕ := p | ¬ϕ | ϕ →ϕ | [a : X] | Baϕ, where X
is any nonempty ﬁnite set of formulae in the language Φ0.
We read Baϕ as “agent a is blamable for ϕ”. The formal
semantics for this language is given below.
Deﬁnition 5 For each game (W, ∆, M, π), any states
w, u ∈W, and each formula ϕ ∈Φ0, the satisfaction rela-
tion (w, u) ⊩ϕ is deﬁned recursively:
1. (w, u) ⊩p, if u ∈π(p),
2. (w, u) ⊩¬ϕ, if w ⊮ϕ,
3. (w, u) ⊩ϕ →ψ, if w ⊮ϕ or w ⊩ψ,
4. (w, u) ⊩[a:X], if


## Page 5


(a) for any action t ∈∆there is ϕ ∈X such that for any
state u′ ∈W if (w, t, u′) ∈M, then (w, u′) ⊩ϕ,
(b) for any nonempty set Y ⊊X there is an action t ∈∆
such that for any formula ϕ ∈Y there is a state u′ ∈
W where (w, t, u′) ∈M, and (w, u′) ⊮ϕ,
5. (w, u) ⊩Baϕ, if (w, u) ⊩ϕ and there is t ∈∆such that
for any state u′ ∈W if (w, t, u′) ∈M, then (w, u′) ⊮ϕ.
Note that items 1 through 4 above are straightforward modi-
ﬁcations of corresponding items in Deﬁnition 4 for a single-
agent no-sacriﬁce language Φ0. Item 5 captures the principle
of alternative possibilities in the same way as in (Naumov
and Tao 2019).
In addition to language Φ0, we also consider a fragment
Φ-[ ]
0
of Φ0 that does not use the ethical dilemma modality.
w
u1
u2
L
R
p
¬p
w
u1
u2
L, N
R, N
p
¬p
¬p
¬p
Figure 3: A game.
To show that ethical dilemma modality cannot be de-
ﬁned through the blameworthiness modality, we construct
two single-player games that are indistinguishable in lan-
guage Φ−[ ]
0
but are distinguishable in language Φ0. The two
games are depicted in Figure 3. These are essentially the
same as in our introductory example in Figure 1. We will re-
fer to these games as “left” and “right” games. Both games
have three states: w, u1, and u2. In both games, proposi-
tional variable p is true in state u1 only. In other words,
πl(p) = {u1} = πr(p), where πl and πr are valuation func-
tions for the left and the right games respectively. The set
of actions in the left game consists of two actions: L and
R. The right game includes action N in addition to actions
L and R. The mechanisms Ml and Mr of the left and the
right games respectively are shown in the diagrams using
directed edges. For example, the edge from state w to state
u1 is labeled with action L on both diagrams. This means
that (w, L, u1) ∈Ml and (w, L, u1) ∈Mr. We will refer to
the satisfaction relations for the left and the right games as
⊩l and ⊩r respectively.
The next lemma shows that the left and the right games
are not distinguishable in language Φ-[ ]
0 .
Lemma 1 (w, u) ⊩l ϕ iff (w, u) ⊩r ϕ for any state u ∈
{u1, u2} and formula ϕ ∈Φ-[ ]
0 .
PROOF. We prove the statement of the lemma by struc-
tural induction on formula ϕ. To prove the statement in
case when formula ϕ is propositional variable p, note that
πl(p) = {u1} = πr(p), see Figure 3. Thus, (w, u1) ⊩l p iff
(w, u1) ⊩l p by item 1 of Deﬁnition 5.
If ϕ is a negation or an implication, the desired follows
from the induction hypothesis and items 2 and 3 of Deﬁni-
tion 5 in the standard way. Suppose now that formula ϕ has
the form Baψ.
(⇒) : Let (w, u) ⊩l Baψ. Thus, by item 5 of Deﬁnition 5,
(w, u) ⊩l ψ
(2)
and there is an action t ∈{L, R} such that (w, u′) ⊮l ψ
for any state u ∈{u1, u2} such that (w, t, u) ∈Ml. Ob-
serve that {(w, t, u) ∈Mr | t ∈{L, R}} = Ml, see
Figure 3. Thus, (w, u′) ⊮l ψ for any state u ∈{u1, u2}
such that (w, t, u) ∈Mr. Hence, by the induction hypoth-
esis, (w, u′) ⊮r ψ for any state u ∈{u1, u2} such that
(w, t, u) ∈Mr. At the same time, also by the induction hy-
pothesis, statement (2) implies that (w, u) ⊩r ψ. Therefore,
(w, u) ⊩r Baψ by item 5 of Deﬁnition 5.
(⇐) : Assume that (w, u) ⊩r Baψ. Thus, by item 5 of Def-
inition 5,
(w, u) ⊩r ψ
(3)
and there is an action t ∈{L, N, R} such that (w, u′) ⊮r ψ
for any state u ∈{u1, u2} such that (w, t, u) ∈Mr. If t ̸=
N, then the prove is similar to the one for the case (⇒).
Assume now that t = N. In other words, (w, u′) ⊮r ψ for
any state u ∈{u1, u2} such that (w, N, u) ∈Mr. Hence,
(w, u′) ⊮r ψ for any state u ∈{u1, u2}, see Figure 3.
Thus, by the induction hypothesis, (w, u′) ⊮l ψ for any
state u ∈{u1, u2}. In particular, (w, u′) ⊮l ψ for any
state u ∈{u1, u2} such that (w, L, u) ∈Ml. At the same
time, by the induction hypothesis, statement (3) implies
that (w, u) ⊩l ψ. Therefore, (w, u) ⊩l Baψ by item 5 of
Deﬁnition 5.
⊠
The next two lemmas show that the left and the right mod-
els are distinguishable in the language that contains ethical
dilemma modality.
Lemma 2 (w, u) ⊩l [a:p, ¬p] for any state u ∈{u1, u2}.
PROOF. We verify the two conditions of item 4 of Deﬁni-
tion 5 separately.
Condition (a): Consider any t ∈{L, R}. Without loss of
generality, let t = L. Consider any state u′ ∈{w, u1, u2}
where (w, L, u′) ∈Ml. To verify the condition, it sufﬁces to
show that (w, u′) ⊩l p.
Indeed, assumption (w, L, u′) ∈Ml implies u′ = u1, see
Figure 5. Thus, u′ ∈πl(p), see Figure 5. Then, (w, u′) ⊩l p
by item 1 of Deﬁnition 5.
Condition (b): Consider any nonempty set Y ⊆{p, ¬p}.
Without loss of generality, assume that Y
= {p}. Let
t = R. To verify the condition, it sufﬁces to prove that
there is a state u′ ∈{w, u1, u2} such that (w, t, u′) ∈Ml
and (w, u′) ⊮p. Indeed, u2 /∈πl(p), see Figure 5. Thus,
u2 ⊮l p by item 1 of Deﬁnition 5. At the same time,
(w, R, u2) ∈Ml, see Figure 5.
⊠
Lemma 3 (w, u) ⊮r [a:p, ¬p] for any state u ∈{u1, u2}.
PROOF. We will show that condition 4(a) of Deﬁnition 5
does not hold. Indeed, consider strategy t = N and any
formula ϕ ∈{p, ¬p}. To show that the condition does not
hold, it sufﬁces to ﬁnd state u′ ∈{w, u1, u2} such that
(w, N, u′) ∈Mr and u′ ⊮r ϕ. Without loss of generality,


## Page 6


let ϕ = p. Note that u2
/∈πr(p), see Figure 5. Thus,
u2 ⊮r p by item 1 of Deﬁnition 5. At the same time
(w, N, u2) ∈Mr, see Figure 5.
⊠
The next theorem follows the three previous lemmas.
Theorem 1 Ethical dilemma modality [ ] is not deﬁnable in
language Φ-[ ]
0 .
⊠
Ethical Dilemma vs Coalition Power
Marc Pauly proposed a logic of coalition power that cap-
tures properties of modality “coalition C has a strategy
to achieve ϕ” (Pauly 2001, 2002). His approach has been
widely studied in the literature (Goranko 2001; van der
Hoek and Wooldridge 2005; Borgo 2007; Sauro et al. 2006;
˚Agotnes et al. 2010; ˚Agotnes, van der Hoek, and Wooldridge
2009; Belardinelli 2014; Goranko, Jamroga, and Turrini
2013; Naumov and Ros 2018). Alur, Henzinger, and Kupfer-
man introduced Alternating-Time Temporal Logic (ATL)
that combines temporal and coalition modalities (2002).
Goranko and van Drimmelen gave a complete axiomati-
zation of ATL (2006). (Alechina et al. 2011) introduce
resource-bounded coalitional logic (RBCL). A logical sys-
tem with a modality labeled by budget and proﬁt is intro-
duced in (Cao and Naumov 2017).
The dilemma modality [C : X]s, even without the sacri-
ﬁce subscript s, cannot be expressed in the original logic
of coalition power. This can be shown using the same
two models from Figure 3 that we used to prove Theo-
rem 1. However, this modality, without the sacriﬁce sub-
script, can be expressed via socially friendly coalition power
modality introduced in (Goranko and Enqvist 2018). Its au-
thors proposed several versions of socially friendly modal-
ity. The basic one, [C](ϕ; ψ1, . . . , ψn) stands for “coali-
tion C has an action proﬁle that guarantees ϕ and en-
ables the complementary coalition C to realize any one
of ψ1, . . . , ψk by a suitable action proﬁle”. Our modality
[C :ϕ1, . . . , ϕn] without the sacriﬁce function is expressible
through socially friendly modality as [C](⊤; ϕ1, . . . , ϕn) ∧
V
D⊊C ¬[D](⊤; ϕ1, . . . , ϕn).
Unlike ours, the logical system proposed in (Goranko and
Enqvist 2018) does not consider cost of actions. Thus, our
modality [C :X]s with the sacriﬁce function s is not express-
ible in their system. They sketch the proof that their axiom-
atization of socially friendly modality is complete, but, un-
like us, do not claim strong completeness. The completeness
proofs here and in (Goranko and Enqvist 2018) use differ-
ent constructions – see our discussion in (Naumov and Yew
2019). Additionally, none of the axioms in (Goranko and
Enqvist 2018) is similar to our main axiom, the Combina-
tion axiom. Also, recall that the mechanism in Deﬁnition 2 is
nondeterministic. This means that statement [C :ϕ1, . . . , ϕ2]
does not imply that the complement of coalition C has a
strategy to force each of the statements ϕ1, . . . , ϕ2. Goranko
and Enqvist’s statement [C](⊤, ϕ1, . . . , ϕn) does imply this.
Ethical Dilemma and Imperfect Information
Recall our introductory example in which an agent is facing
a dilemma because she has to make a hard choice between
consciously killing Alice and consciously killing Bob. As
we discuss there, the agent does not face a dilemma if she
can avoid the hard choice by using action N and leaving the
outcome up to chance. The other case when the agent does
not have to make a hard choice between consciously killing
Alice and consciously killing Bob is when she is unaware of
the possible outcomes of her actions.
w
u
v
L
R
Alice is dead
Bob is dead 
w
L
R
w
u
v
L
R
Alice is dead
Bob is dead 
w
R
L
Figure 4: Two settings with imperfect information.
Consider, for example, the left diagram in Figure 4. This
diagram depicts an imperfect information game with states
w and w′ indistinguishable to the agent. In state w the agent
has a choice between action L and action R. The ﬁrst of
these actions results in Alice’s death, the second in Bob’s
death. However, the agent does not know which action re-
sults in whose death because she cannot distinguish state w
from state w′ where the same actions have the opposite ef-
fect. Thus, by choosing one of the two actions in state w,
the agent does not make a hard choice between consciously
killing Alice and consciously killing Bob. We say that she
does not face a dilemma in this setting. At the same time,
the agent does face a dilemma in the setting depicted in the
right diagram in Figure 4 because in both indistinguishable
states the actions lead to the same outcome.
To formally deﬁne ethical dilemma modalities in imper-
fect information game settings, one needs to add an indistin-
guishability equivalence relation ∼a between states to Def-
inition 2 of the game. Furthermore, because this deﬁnition
allows costs of actions to vary from state to state, we need to
assume that the cost of the action to an agent a is the same
in all a-indistinguishable states. In other words, we need to
assume that the cost of the action is known to the agent.
After the above changes are done to Deﬁnition 2, one can
modify item 4 of Deﬁnition 4 to capture ethical dilemma in
imperfect information setting as as shown below. We write
w ∼C u if w ∼a u for all agents a ∈C.
Deﬁnition 6 For each game (W, {∼a}a∈A, ∆, | · |, M, π)
with imperfect information, each state w ∈W, and each
formula ϕ ∈Φ, the satisfaction relation w ⊩ϕ is deﬁned
recursively:
4. w ⊩[C :X]s, if
(a) for any strategy t ∈∆C of coalition C there is a for-
mula ϕ ∈X such that for any action proﬁle δ ∈∆A
and any states w′, u ∈W if w ∼C w′, |δ|w ≤s,
t =C δ, and (w′, δ, u) ∈M, then u ⊩ϕ,
(b) for any nonempty subset Y ⊊X there is a strategy
t ∈∆C of coalition C such that for any formula ϕ ∈Y
there is an action proﬁle δ ∈∆A and states w′, u ∈W


## Page 7


where w ∼C w′, |δ|w ≤s, t =C δ, (w′, δ, u) ∈M,
and u ⊮ϕ.
Later in this paper we propose a sound and complete log-
ical system for ethical dilemma modality with sacriﬁce in a
perfect information setting. A logical system that describes
an interplay between distributed knowledge and blamewor-
thiness in an imperfect information setting is introduced
in (Naumov and Tao 2020b). We leave the development of a
similar system for knowledge and dilemmas for the future.
Weak Dilemma
In the next section we state the axioms of our logical system
that capture the properties of modality [C : X]s. When stat-
ing these axioms, it will be convenient to deﬁne JC : XKs
as an abbreviation for formula W
∅̸=Z⊆X[C : Z]s. In other
words, JC : XKs means that each action proﬁle of coalition
C forces a speciﬁc formula in set X to be true, but set X
is not necessarily a minimal such set. We call expression
JC : XKs a weak dilemma. Alternatively, JC : XKs could be
deﬁned by omitting condition 4(b) from Deﬁnition 4.
Axioms
In this section we list and discuss the axioms and inference
rules of our logical system. The ﬁrst of these axioms uses
the notation X ⊗Y . For any two sets of formulae X and Y ,
let X ⊗Y be the set of formulae {ϕ ∧ψ | ϕ ∈X, ψ ∈Y }.
In addition to propositional tautologies in language Φ, our
logical system contains the following axioms:
1. Combination: [C :X]s →([C :Y ]s →JC :X ⊗Y Ks),
2. Monotonicity: [C : X]s′ →JD : XKs, where C ⊆D and
s ≤s′,
3. Minimality: [C :X]s →¬[C :Y ]s, where Y ⊊X,
4. No Alternatives: [C :X]s →[D:X]s, where |X| = 1.
We write ⊢ϕ if formula ϕ ∈Φ is derivable in our logical
system using the Modus Ponens, the Necessitation, and the
Substitution inference rules
ϕ,
ϕ →ψ
ψ
ϕ
[C :ϕ]s
{ϕ →τ(ϕ) | ϕ ∈X}
[C :X]s →JC :τ(X)Ks
,
for each function τ that maps set Φ into set Φ. If ⊢ϕ, then
we say that formula ϕ is a theorem of our system. We write
X ⊢ϕ if formula ϕ is provable from all theorems of our
logical system and an additional set of formulae X using the
Modus Ponens inference rule only.
The Combination axiom states that if each action proﬁle
of coalition C forces a speciﬁc formula in set X to be true
and a speciﬁc formula in set Y to be true, then each action
proﬁle of coalition C forces a speciﬁc formula in set X ⊗Y
to be true. Indeed, if a particular action proﬁle forces ϕ ∈X
to be true and ψ ∈Y to be true, then this proﬁle also forces
ϕ ∧ψ to be true. A hypothetical Combination axiom with
the single bracket modality in the conclusion is not sound.
The Monotonicity axiom states that if each action proﬁle
of coalition C forces a speciﬁc formula in set X to be true
under a more relaxed constraint s′ on sacriﬁce, then each ac-
tion proﬁle of a larger coalition D forces a speciﬁc formula
in set X to be true under a stronger constraint s. A hypothet-
ical Monotonicity axiom with single bracket modality in the
conclusion is also not sound. The Minimality axiom captures
the minimality requirement of item 4(b) in Deﬁnition 4.
The No Alternatives axiom deals with the extreme case
of a singleton set X = {ϕ}. Note that statement [C : ϕ]s
means that statement ϕ is predetermined to be true under
any action proﬁle of coalition C as long as actions of all
agents are constrained by s. In other words, ϕ is true as
long as actions of all agents are constrained by s. Since the
last statement does not depend on the coalition C, we may
conclude that validity of statement [C :ϕ]s does not depend
on the choice of coalition C. This observation is captured in
the No Alternatives axiom.
The Necessitation rule states that if formula ϕ is true in
all states of all games, then statement ϕ is predetermined
to be true under any action proﬁle of coalition C and any
constraint s. Note that in this case the minimality condition
4(b) of Deﬁnition 4 is vacuously satisﬁed because singleton
set {ϕ} has no nonempty proper subsets.
The Substitution rule says that if [C : X]s and statement
ϕ in set X is replaced with a logically weaker statement
τ(ϕ), then each action proﬁle of coalition C still forces a
speciﬁc formula in the set τ(X) to be true, but τ(X) is not
necessarily the smallest such set. An example of an instance
of this rule is
¬¬ϕ →ϕ,
ψ →(χ →ψ)
[C :¬¬ϕ, ψ]s →JC :ϕ, χ →ψKs
.
Note that X and τ(X) are sets, not lists. Thus, set τ(X)
might have fewer elements than set X:
ϕ →(ϕ ∨ψ),
ψ →(ϕ ∨ψ)
[C :ϕ, ψ]s →JC :ϕ ∨ψKs
.
Theorem 2 (strong soundness) If X ⊢ϕ and w is a state
of a model such that w ⊩χ for each formula χ ∈X, then
w ⊩ϕ.
⊠
The proof of the following completeness theorem can be
found in (Naumov and Yew 2019).
Theorem 3 (strong completeness) For any set of formulae
X and any formula ϕ, if X ⊬ϕ, then there is a game and
a state w of this game such that w ⊩χ for each formula
χ ∈X and w ⊮ϕ.
Conclusion
The contribution of this paper is three-fold. First, we intro-
duce a formal semantics for ethical dilemmas in a strategic
game setting expressed through the modality [C : X]s. Sec-
ond, we show that this modality is not deﬁnable through the
blameworthiness modality. Finally, we give a complete ax-
iomatization of the properties of the dilemma modality.
Our completeness result is the strong completeness theo-
rem with respect to the proposed semantics. We believe that
the standard ﬁltration technique could be used to prove weak
completeness with respect to the class of ﬁnite games. This
would imply decidability of our logical system, assuming
the sacriﬁce function is rational-valued functions.


## Page 8


References
˚Agotnes, T.; Balbiani, P.; van Ditmarsch, H.; and Seban, P.
2010. Group announcement logic. Journal of Applied Logic
8(1):62 – 81.
˚Agotnes, T.; van der Hoek, W.; and Wooldridge, M. 2009.
Reasoning about coalitional games. Artiﬁcial Intelligence
173(1):45 – 79.
Alechina, N.; Logan, B.; Nguyen, H. N.; and Rakib, A.
2011. Logic for coalitions with bounded resources. Jour-
nal of Logic and Computation 21(6):907–937.
Alur, R.; Henzinger, T. A.; and Kupferman, O.
2002.
Alternating-time temporal logic.
Journal of the ACM
49(5):672–713.
Belardinelli, F.
2014.
Reasoning about knowledge and
strategies: Epistemic strategy logic.
In Proceedings 2nd
International Workshop on Strategic Reasoning, SR 2014,
Grenoble, France, April 5-6, 2014, volume 146 of EPTCS,
27–33.
Berreby, F.; Bourgne, G.; and Ganascia, J.-G. 2015. Mod-
elling moral reasoning and ethical responsibility with logic
programming. In Logic for programming, artiﬁcial intelli-
gence, and reasoning, 532–548. Springer.
Bleske-Rechek, A.; Nelson, L. A.; Baker, J. P.; Remiker,
M. W.; and Brandt, S. J. 2010. Evolution and the trolley
problem: People save ﬁve over one unless the one is young,
genetically related, or a romantic partner. Journal of Social,
Evolutionary, and Cultural Psychology 4(3):115.
Bonnemains, V.; Saurel, C.; and Tessier, C. 2018. Embedded
ethics: some technical and ethical challenges. Ethics and
Information Technology 20(1):41–58.
Borgo, S. 2007. Coalitions in action logic. In 20th Inter-
national Joint Conference on Artiﬁcial Intelligence, 1822–
1827.
Bruers, S., and Braeckman, J. 2014. A review and systemati-
zation of the trolley problem. Philosophia 42(2):251–269.
Cao, R., and Naumov, P. 2017. Budget-constrained dynam-
ics in multiagent systems. In Proceedings of the Twenty-
Sixth International Joint Conference on Artiﬁcial Intelli-
gence, IJCAI 2017, Melbourne, Australia, August 19-25,
2017, 915–921.
Chen, P.; Qiu, J.; Li, H.; and Zhang, Q. 2009. Spatiotempo-
ral cortical activation underlying dilemma decision-making:
an event-related potential study.
Biological Psychology
82(2):111–115.
Fabio, U. D.; Broy, M.; Br¨ungger, J.; Eichhorn, U.; Grun-
wald, A.; Heckmann, D.; Hilgendorf, E.; Kagermann, H.;
Losinger, A.; Lutz-Bachmann, M.; L¨utge, C.; Markl, A.;
M¨uller, K.; and Nehm, K. 2017. Automated and connected
driving.
Technical report, Ethics Commission, German
Federal Ministry of Transport and Digital Infrastructure.
https://www.bmvi.de/SharedDocs/EN/publications/report-
ethics-commission.pdf? blob=publicationFile.
Foot, P. 1967. The problem of abortion and the doctrine of
the double effect. Oxford Review (5).
Frankfurt, H. G. 1969. Alternate possibilities and moral
responsibility. The Journal of Philosophy 66(23):829–839.
Goranko, V., and Enqvist, S. 2018. Socially friendly and
group protecting coalition logics. In Proceedings of the 17th
International Conference on Autonomous Agents and Multi-
agent Systems, 372–380. International Foundation for Au-
tonomous Agents and Multiagent Systems.
Goranko, V., and van Drimmelen, G. 2006. Complete ax-
iomatization and decidability of alternating-time temporal
logic. Theoretical Computer Science 353(1):93 – 117.
Goranko, V.; Jamroga, W.; and Turrini, P. 2013. Strategic
games and truly playable effectivity functions. Autonomous
Agents and Multi-Agent Systems 26(2):288–314.
Goranko, V. 2001. Coalition games and alternating tempo-
ral logics. In Proceedings of the 8th conference on Theoreti-
cal aspects of rationality and knowledge, 259–272. Morgan
Kaufmann Publishers Inc.
Halpern, J. Y., and Kleiman-Weiner, M.
2018.
Towards
formal deﬁnitions of blameworthiness, intention, and moral
responsibility. In Proceedings of the Thirty-Second AAAI
Conference on Artiﬁcial Intelligence (AAAI-18).
Horty, J. F. 1994. Moral dilemmas and nonmonotonic logic.
Journal of philosophical logic 23(1):35–65.
Indick, W.; Kim, J.; Oelberger, B.; and Semino, L.
2000.
Gender differences in moral judgement: is non-
consequential reasoning a factor. Current Research in Social
Psychology 5(20):285–298.
Kawai, N.; Kubo, K.; and Kubo-Kawai, N. 2014. “granny
dumping”: Acceptability of sacriﬁcing the elderly in a sim-
ulated moral dilemma.
Japanese Psychological Research
56(3):254–262.
Marczyk, J., and Marks, M. J. 2014. Does it matter who
pulls the switch? perceptions of intentions in the trolley
dilemma. Evolution and Human Behavior 35(4):272–278.
Naumov, P., and Ros, K. 2018. Strategic coalitions in sys-
tems with catastrophic failures (extended abstract). In Pro-
ceedings of the 16th International Conference on Principles
of Knowledge Representation and Reasoning, 659–660.
Naumov, P., and Tao, J. 2019. Blameworthiness in strategic
games. In Proceedings of Thirty-third AAAI Conference on
Artiﬁcial Intelligence (AAAI-19).
Naumov, P., and Tao, J. 2020a. Blameworthiness in security
games. In Proceedings of Thirty-Fourth AAAI Conference
on Artiﬁcial Intelligence (AAAI-20).
Naumov, P., and Tao, J. 2020b. An epistemic logic of blame-
worthiness. Artiﬁcial Intelligence 283. 103269.
Naumov, P., and Yew, R.-J. 2019. Ethical dilemmas in strate-
gic games. arXiv:1911.00786.
Navarrete, C. D.; McDonald, M. M.; Mott, M. L.; and Asher,
B. 2012. Virtual morality: Emotion and action in a simulated
three-dimensional “trolley problem”. Emotion 12(2):364.


## Page 9


Orlove, R. 2016. Now Mercedes says its driverless cars
won’t run over pedestrians, that would be illegal.
Jalop-
nik. https://jalopnik.com/now-mercedes-says-its-driverless-
cars-wont-run-over-ped-1787890432.
Pan, X., and Slater, M. 2011. Confronting a moral dilemma
in virtual reality: a pilot study. In Proceedings of the 25th
BCS Conference on Human-Computer Interaction, 46–51.
British Computer Society.
Pauly, M. 2001. Logic for Social Software. Ph.D. Disserta-
tion, Institute for Logic, Language, and Computation.
Pauly, M. 2002. A modal logic for coalitional power in
games. Journal of Logic and Computation 12(1):149–166.
Sauro, L.; Gerbrandy, J.; van der Hoek, W.; and Wooldridge,
M.
2006.
Reasoning about action and cooperation.
In
Proceedings of the Fifth International Joint Conference on
Autonomous Agents and Multiagent Systems, AAMAS ’06,
185–192. New York, NY, USA: ACM.
Taylor, M.
2016.
Self-driving Mercedes-Benzes will
prioritize occupant safety over pedestrians. Car and Driver.
https://www.caranddriver.com/news/a15344706/self-
driving-mercedes-will-prioritize-occupant-safety-over-
pedestrians/.
Thomson, J. J. 1976. Killing, letting die, and the trolley
problem. The Monist 59:204–217.
Thomson, J. J. 1984. The trolley problem. Yale LJ 94:1395.
van der Hoek, W., and Wooldridge, M. 2005. On the logic of
cooperation and propositional control. Artiﬁcial Intelligence
164(1):81 – 119.
Widerker, D. 2017. Moral responsibility and alternative
possibilities: Essays on the importance of alternative possi-
bilities. Routledge.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1911_00786v3_ethical_dilemmas_in_strategic_games
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1911_00786V3_ETHICAL_DILEMMAS_IN_STRATEGIC_GAMES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

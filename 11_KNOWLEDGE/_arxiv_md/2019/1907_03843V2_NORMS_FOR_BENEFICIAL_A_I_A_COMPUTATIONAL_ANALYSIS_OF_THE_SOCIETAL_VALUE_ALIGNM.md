---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1907.03843v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1907.03843v2_Norms_for_Beneficial_A_I___A_Computational_Analysis_of_the_Societal_Value_Alignm

> Source: 1907.03843v2_Norms_for_Beneficial_A_I___A_Computational_Analysis_of_the_Societal_Value_Alignm.pdf

> Pages: 16

---


## Page 1


Norms for Beneﬁcial A.I.: A Computational Analysis of the Societal Value
Alignment Problem
Pedro M. Fernandes, Francisco C. Santos,Manuel Lopes
pedro.miguel.rocha.fernandes,franciscocsantos,manuel.lopes@tecnico.ulisboa.pt
INESC-ID and Instituto Superior T´ecnico, Univ. de Lisboa, Lisbon, Portugal
December 23, 2020
Abstract
The rise of artiﬁcial intelligence (A.I.) based systems is al-
ready oﬀering substantial beneﬁts to the society as a whole.
However, these systems may also enclose potential conﬂicts
and unintended consequences. Notably, people will tend to
adopt an A.I. system if it confers them an advantage, at
which point non-adopters might push for a strong regula-
tion if that advantage for adopters is at a cost for them.
Here we propose an agent-based game-theoretical model for
these conﬂicts, where agents may decide to resort to A. I.
to use and acquire additional information on the payoﬀs
of a stochastic game, striving to bring insights from sim-
ulation to what has been, hitherto, a mostly philosophical
discussion.
We frame our results under the current dis-
cussion on ethical A.I. and the conﬂict between individual
and societal gains: the societal value alignment problem.
We test the arising equilibria in the adoption of A.I. tech-
nology under diﬀerent norms followed by artiﬁcial agents,
their ensuing beneﬁts, and the emergent levels of wealth
inequality.
We show that without any regulation, purely
selﬁsh A.I. systems will have the strongest advantage, even
when a utilitarian A.I. provides signiﬁcant beneﬁts for the
individual and the society. Nevertheless, we show that it is
possible to develop A.I. systems following human conscious
policies that, when introduced in society, lead to an equi-
librium where the gains for the adopters are not at a cost
for non-adopters, thus increasing the overall wealth of the
population and lowering inequality. However, as shown, a
self-organised adoption of such policies would require exter-
nal regulation.
Keywords: AI ethics, Game theoretical analysis, AI reg-
ulation, Social Simulation
1
Introduction
Several applications already have an Artiﬁcial Intelligent
system (A.I.) taking decisions in place of their owners. It
is expected that in the future, such delegation of decisions
will become more ubiquitous and eﬀective. It is still open
to debate whether that will have a positive or a negative
impact on society [60, 17]. Strong voices highlight the dan-
gers of A.I. [4] and call for regulation [28], some others dis-
miss such fears [15] and are against regulation [23]. Some
of these discussions come from a lack of understanding of
the current A.I. capabilities and strong divergences about
its future developments, especially in artiﬁcial general in-
telligence (AGI). Some concerns might be true when AGI
is created but not under the current state-of-the-art. How
fast we can get there is still open to debate [14], and so
is if we should strive to get there fast, or delay it [12, 26].
But even under the current state-of-the-art in A.I. there are
problems that may arise with their introduction, e.g. au-
tonomous vehicles [11], automatic hiring systems [45] and
stock exchange [31].
A strong regulation could decide that A.I. systems should
act using an egalitarian or utilitarian perspective. However,
a utilitarian perspective or norm might not be eﬃcient, and
in many cases, an egalitarian solution does not exist. An
utilitarian A.I., which would strive to maximize the overall
utility gain of the world, would often have to act against
the interests of its owner. If people can choose to adopt
or not an A.I. system, we can expect they will only do it
if it is individually rational to do so. In principle, either
the A.I. system gives an individual advantage for its owner,
or it will not be bought. If there is no interest in buying,
there will be no interest in production, curbing research and
development.
Without any regulation, A.I. systems might lead to in-
vasion of privacy, use of conﬁdential information, cheating
in games, collusion in public contracts, and many others.
Even if legal their eﬃciency and eﬀectiveness might greatly
unbalance the societal scales, increasing the inequality in
wealth distribution. In this case, we can expect that non-
adopters might push for a substantial regulation of A.I. or
even for its abolition.
It is thus challenging to conciliate these two goals of
aligning the preferences of A.I. adopters and those of the
non-adopters. We call this the societal value alignment
problem. Besides being advantageous for the adopters of
A.I. (individual rationality), it needs to be better for the
1
arXiv:1907.03843v2  [cs.CY]  22 Dec 2020


## Page 2


non-adopters and so for everyone in the society (societal
rationality).
The rise of A.I. systems has the power to
create novel market dynamics [53] and challenges. Eﬀorts
should be made to model these possible future worlds, so
that we understand them better before we are in the midst
of the problems that might arise. Voices in the scientiﬁc
community begin to pressure for the research on this area,
and on the ethical, scientiﬁc and engineering problems it
presents [54, 44, 27, 40].
Here we aim to model how A.I. systems can provide an
advantage for those adopting them (fostering adoption and
creating incentives for the scientiﬁc, technological and soci-
etal development) but without creating such advantage at
the expense of others (allowing for societal acceptance of
the systems). Adoption is here deﬁned as the delegation
of decisions to an A.I. system that is done by an individual.
Acceptance concerns the societal opinion regarding A.I.
systems, which will be highly inﬂuential on their legislation.
To do so, we deﬁne several diﬀerent types of A.I. systems,
adopting diﬀerent types of norms, ranging from pure self-
ish to pure utilitarian. Then we study the time evolution of
the adoption of each type of A.I. when they compete against
each other and also the equilibrium for each A.I. system in
particular.
Individual adopters of A.I. systems can be seen as: sin-
gular citizens adopting A.I. systems for personal gains (e.g.
a person buying an autonomous vehicle); corporations buy-
ing A.I. to increase proﬁts (e.g. a company adopting an A.I.
based hiring system); political entities using A.I. to gain in-
ﬂuence (e.g. political parties using A.I. algorithms in social
media to inﬂuence elections); or even countries, deploying
A.I. to gain an upper hand on war and trading. Our model
abstracts individuals as equally complex entities that inter-
act between each other, gaining or losing utility on each
interaction. Utility is here used as an abstraction of some-
thing desirable/useful and could be seen, for example, as
monetary currency, the strengthening of political positions
or improvement of individual well-being.
In particular, this analysis aims at answering the follow-
ing research questions:
1. Will self-regarding individuals adopt A.I. systems?
2. With diﬀerent types of A.I. systems available, which
ones will be adopted?
3. If adopted, what is the individual and collective gain,
depending on the strategy adopted by the A.I. system?
Based on the answers to these questions we then discuss
the kind of regulation that might be needed to improve the
individual and societal rationality of A.I. systems. These
allow us to provide novel insights on the following questions:
1. Is any type of A.I. both acceptable and adoptable?
2. Taking into account all the evaluation criteria, includ-
ing individual and societal, is it possible to create mech-
anisms/properties that improve all of them?
3. Considering even the extreme case where everyone uses
the same A.I. enabled system, will they obtain the same
beneﬁt?
This paper is organized as follows. In Sec. 2 we discuss
the related work. Sec. 3 introduces the main contribution
of our work and details the set of possible behaviours or
norms that a A.I. system may have, and how we evaluate
their performance when acting in a population comprising
humans and artiﬁcial systems. To do so, we introduce a
novel game theoretic model for the dynamics of adoption of
A.I. systems. Section 4 presents the results of our computer
simulations. In Sec. 5 we introduce another simulation aim-
ing at understanding the inequality emerging in the cases
where everyone has the same A.I. system. In Sec. 6 we sum-
marize our conclusions and, ﬁnally, in Sec. 7, we present a
more extended discussion about the impact of this study in
the dilemmas related to the introduction of A.I. systems.
2
Related Work
The problem of aligning one A.I. system with all the indi-
viduals of a society (A.I. and non A.I.), knowing many of
these individuals might have contradictory values, is a com-
plex one. Even if the system is capable of perfectly aligning
with each individual, there is no perfect solution as in many
situations, it won’t be possible to be aligned with all of the
individuals simultaneously. The system will have to choose
with whom to be and not be aligned.
Many authors expect many negative eﬀects from the
adoption of A.I. systems and so many diﬀerent ethical codes
of conduct have been proposed. A code of conduct would
represent the universal human values and by aligning with
it, the A.I. system would be indirectly aligned with all hu-
mankind. First literary approaches include the famous laws
of robotics by Isaac Asimov [7]. They were natural language
laws, which leads to obvious implementation problems, and
in his books, Isaac Asimov proved his own laws ﬂawed. Af-
ter that, several ethical frameworks have been proposed.
Some principles are found in almost all of them, others are
characteristic of each approach.
The Asilomar AI Principles [6] are a set of 23 principles
intended to promote the safe and beneﬁcial development
of artiﬁcial intelligence.
They have been endorsed by AI
research leaders at Google DeepMind, GoogleBrain, Face-
book, Apple, and OpenAI. Signatories of the principles in-
clude Elon Musk, the late Stephen Hawking, Stuart Rus-
sell, and more than 3,800 other AI researchers and experts.
On August 30 of 2018, the State of California unanimously
adopted legislation in support of the Asilomar AI Principles
[1], taking a historic step towards A.I. research and devel-
opment legislation.
2


## Page 3


The European Commission released a document by the
high-level expert group on A.I., containing a set of ethic
guidelines for trustworthy A.I. [29]. The document states
that trustworthy A.I. should be lawful, ethical and robust.
It further deﬁnes 7 key requirements that AI systems should
meet in order to be deemed trustworthy.
In the end, it
presents a series of questions that entities should ask them-
selves to ensure they are meeting all the deﬁned require-
ments. The Organisation for Economic Co-operation and
Development (OECD) has released a legal instrument with
recommendations on A.I., which was adopted by 42 coun-
tries [37].
Floridi et al made a comparison of several ethical frame-
works [24], in which they analyse principles proposed by 6
diﬀerent entities, including the previously mentioned Asilo-
mar AI principles [6], wielding 47 principles on total, and
compare them to the existing 4 principles of bio-ethics (Non-
maleﬁcence; Justice; Beneﬁcence; Autonomy) [9], ﬁnding a
considerable overlap.
They argue that for the bio-ethics
principles to be applied to the ﬁeld of A.I., a ﬁfth principle
is needed: explicability. This principle incorporates both
intelligibility and accountability.
They go on to propose
20 action points, that is, recommendations for enabling a
beneﬁcial A.I. society.
Anderson et al defend that it may be possible to incor-
porate an explicit ethical component into a machine relying
on inductive logic programming approach [3]. The goal is
to solve ethical dilemmas by ﬁnding ethical principles that
best ﬁt given positive and negative examples. They advo-
cate the use of a modiﬁed version of the Turing test [56],
the comparative moral Turing test [2]. This test is an el-
egant solution to the question ”What is an ethical/moral
A.I. system?”. The test consists in giving to a human judge
pairs of descriptions of actual, morally-signiﬁcant actions of
a human and an A.I. system. If the judge identiﬁes the A.I.
as a moral equal or superior to the human, then the A.I.
system passed the comparative moral Turing test.
Conitzer et al describe a game theoretical approach to
the problem of moral decision making [20]. Turning moral
dilemmas into game-theoretic representation schemes, they
then try to ﬁnd the principles that guide human moral de-
cision making. They also argue that such representations
could be used alongside machine learning, which could lead
to more reliable results and to the improvement of the rep-
resentations.
However, some argue that having an ethical framework
or even A.I. systems that pass the comparative moral Tur-
ing test is not enough [59].
Roman Yampolskiy defends
that it is insuﬃcient to have a human-like morality on A.I.
systems with super-human intelligence. On such systems,
small moral mistakes, common in humans, could lead to the
extinction of humanity. Furthermore, a moral A.I. system
with super-human intelligence will be able to recursively
self-improve, with no provided guarantees that the resulting
improvements remain moral. Instead of an ethical approach,
Yampolskiy proposes a safety engineering approach, able
to provide proofs that developed A.I. systems will remain
safe, even under recursive self-improvement [57]. Yampol-
skiy also proposes A.I. conﬁnement as a possible approach
while no safety guarantees are in place [58, 8].
This ap-
proach would consist in ensuring that an A.I. system could
help humanity while having no ability to negatively inﬂu-
ence the world around it. This idea of A.I. conﬁnement had
been ﬁrst presented in [22], and discussed by Bostrom [13]
and Chalmers [18]. This is, however, more of a preventive
measure than a perfect solution, as limiting the negative
A.I. inﬂuence will also limit the possible positive inﬂuence.
The focus of most previous works was on considering high-
level ethical principles for A.I. systems acting in a society or
ﬁnding moral frameworks. In most cases there was no claim
or prediction about the potential adoption of A.I. systems
or their acceptance by non-adopters and by society in gen-
eral. Just a few works considered the development of com-
putational models on the impact of A.I.. For instance, one
study analyzed the amount of safety precautions companies
would take considering that they are competing with others
for dominating A.I. [4].
Taking a diﬀerent stance from the majority of related lit-
erature, our work aims at understanding the dynamics of
adoption (who chooses to use an A.I. system) and of ac-
ceptance (if non-adopters accept the use of A.I. by others)
relying on computational models of population dynamics. A
better understanding of such dynamics can both allow us to
better predict the outcome of A.I. proliferation as well as in-
form future legislation to ensure a beneﬁcial impact of A.I.
technology in society. Even though it is not yet a solved
problem [50], for this paper, we will assume that an A.I.
system can accurately estimate the goals of each individ-
ual with whom it interacts. With this assumption, we are
able to study the problems that emerge at the societal level
even after having the problem of individual value alignment
solved.
3
Methods
In this section, we present a game-theoretical framework to
study the impact of the adoption of A.I. systems on indi-
viduals and on the society. We consider several diﬀerent
types of A.I. that might adopted, or allow to be used, by
society. Some of them are purely social, others purely self-
ish. Although no exhaustive list is possible, we cover a set
of diﬀerent strategies to be able to study them in hybrid
populations of A.I. and humans. We start by providing the
model of a single interaction between two individuals, then
explain how we model the diﬀerence in decision making be-
tween an A.I. system and a human, and ﬁnally present the
simulated world and the used algorithms.
Henceforward, individual non-adopters of an A.I. system
will be referred to as H, while individuals adopters of an
3


## Page 4


A.I. system representative will be referred to as A.I..
3.1
Model of Interaction Between Individ-
uals:
On each interaction between individuals, I1 and I2, a
stochastic payoﬀmatrix M t is generated. This is a m-by-m
matrix of payoﬀpairs that is diﬀerent for every interaction.
Being a1 the action chosen by I1 and a2 the action chosen
by I2, the payoﬀreceived by each individual is respectively
u1 and u2, such that:
(u1, u2) = M t(a1, a2).
(1)
In order to explicitly generate general sum games, as con-
clusions might be diﬀerent in positive, negative or zero-sum
worlds, the payoﬀmatrices have the following structure:
u1
=
R + z(0, 2)|R|(α −1)
(2)
u2
=
−R + z(0, 2)|R|(α −1)
(3)
Having R = z(−3, 3), where z(a, b) represents a sample
from a uniform distribution in the interval [a, b]. The inter-
val [−3, 3] was chosen for the simulations, but any equivalent
interval could be used. R is the same for each u1 and u2
pair. z(0, 2) is applied independently for each element of the
matrix. This z(0, 2) parameter creates an additional source
of variability between diﬀerent interactions, so that not all
action pairs have the same overall utility gain. |R| is the ab-
solute value of R. We will call α an inﬂation constant. For
α = 1, the matrices will, on average, create a zero sum game
where no payoﬀis created or lost, just transferred between
individuals. For α > 1 there is on average a positive total
payoﬀ, creating a positive sum game, and for α < 1 there is
on average a negative total payoﬀ, creating a negative sum
game. In our simulations, in order to study a positive sum
world, we consider α = 1.2. The number of possible actions
per individual was set to 4 (m = 4), an empirically found
balance between complexity and computational feasibility.
3.2
Simulating A.I. Systems and Humans
We now discuss how we can model an human acting versus
an A.I. system. A.I. systems are diﬀerent from humans and
can provide several advantages:
1. A.I. systems are not be prone to fatigue or distrac-
tions and so will make less errors than humans: As
we model interactions between individuals as a payoﬀ
matrix game, we can model this as a shaking hand phe-
nomena where H will sometimes pick the wrong action
according to their own reasoning.
2. A.I. systems can perform more frequent interactions:
Considering examples such as an A.I. support system
for online shopping. An A.I. system can manage thou-
sands of simultaneous auctions and so even if it gets
a similar proﬁt per transaction as a human, the larger
number of transactions will provide greater gains. It
can be modelled by allowing A.I. to play more fre-
quently.
3. A.I. systems can have access and analyze larger quan-
tities of data: With the current state-of-the-art there
are many domains where people identify more complex
relations, identify important variables and infer causal-
ity much better than machines [5]. On the contrary,
right now machines can analyze much larger volumes of
data and variables that are already identiﬁed. Having
more information about the world and speciﬁc prob-
lems combined with the ability to process such huge
amounts of information can allow better prediction and
consequently, better decision making capabilities. This
advantage of A.I. systems is already being applied for
stock exchange trading [51] and to create powerful lan-
guage models [16]. This advantage can be modelled by
only giving H access to a noisy version of the matrix
game. A.I. will be able to grasp the entirety of the
problem and as such will have no noise in the observa-
tion of the matrix.
There are other ways in which A.I. systems could grant an
advantage to their users, some of which we might not even
be able to understand yet given the current state of the
technology. The main model assumption, however, remains
the same: when interacting with H, A.I. have a decision
making advantage.
In the end, over the several diﬀerent
alternatives to model A.I. behaviours we choose item (3) to
analyze in this work. In another simulation we use (1) and
see that both alternative models provide similar qualitative
conclusions.
In a computational way we are in the presence of par-
tial observability in our stochastic game.
The diﬀerence
between H and A.I. is that while A.I. sees the real payoﬀ
matrix, M t, H sees a noisy version of it, M ϵ. This allows
A.I. individuals to make optimal decisions, while H individ-
uals are conﬁned to sub-optimal decisions. This models the
superior decision making and information gathering skills
of A.I.. This approach also rests on the assumption that
the individual value alignment problem is solved, since A.I.
systems know the utility payoﬀof both individuals.
Having:
(ut
1, ut
2)
=
M t(a1, a2)
(4)
The noisy version is produced as follows:
uϵ
1
=
ut
1 + (z(0, 10 −Q) −z(0, 10 −Q))
(5)
uϵ
2
=
ut
2 + (z(0, 10 −Q) −z(0, 10 −Q))
(6)
The degree of knowledge about the (true) payoﬀmatrix
M t is modelled in a continuous way. To do so, we consider
a term z(0, 10 −Q), where Q corresponds to the level of
intelligence.
For Q = 10 there is no noise and the true
4


## Page 5


matrix is observed; Q = 0 represents a low intelligence,
such that the observed matrix is very diﬀerent from the
true one. A.I. is modelled with Q = 10, while for H the
intelligence factors is Q ∈[0, 5].
Other intervals for the
intelligence factors of H were experimented with, inside the
[0, 9] range, but they lead to the same qualitative results.
The sum (z(0, 10 −Q) −z(0, 10 −Q)) was used instead of
z(−(10 −Q), 10 −Q) to create a Irwin-Hall distribution
instead of a uniform one.
As an example we can generate a 2-by-2 true matrix (seen
by A.I.) as:
M t =

(0, 0)
(−3, 1)
(1, −5)
(−1, −1)

(7)
And then the noisy matrix observed by H becomes:
M ϵ =

(0, −1)
(−1, 3)
(0, −6)
(−2, 1)

(8)
Where each (ut
1, ut
2) pair was transformed into the corre-
sponding (uϵ
1, uϵ
2) pair. In this example, M t(1, 0) is (1, −5)
whereas M ϵ(1, 0) is (0, −6).
3.3
Human Strategy:
Before delving into the diﬀerent A.I. types, we describe
the strategy used by H. Despite not having access to the
true game matrix, M t, H remain rational and will try to
choose the actions most proﬁtable for themselves. For this
matrix game, that will correspond to the Nash equilibrium
[30, 33, 34].
3.3.1
Nash Equilibrium (NashEQ)
H play the Nash equilibrium in the noisy matrix M ϵ. If
more than one is found, they choose the most proﬁtable one.
If two or more are equal, they choose the one most proﬁtable
for their opponent. If no Nash equilibrium is found, indi-
viduals choose the best action assuming that the opponent
acts randomly.
3.4
A.I. Types:
In this section, we propose four diﬀerent types of A.I.. A.I.
systems can use the previously deﬁned strategy for humans
using the true matrix M t (NashEQ), but they can resort
to more elaborate strategies ranging from a selﬁsh to an
utilitarian approach. A.I., being modelled as having super-
human intelligence, can also predict the action of an H op-
ponent. A.I. cannot, however, predict opposing A.I. ac-
tions as for our model we assume all A.I. have equal intel-
ligence and capabilities.
3.4.1
Nash Equilibrium (NashEQ)
A.I. choose exactly like H, but using the true matrix M t.
3.4.2
Selﬁsh
A.I., facing H, considers only its own proﬁt, in accordance
with ethical egoism [41]. Knowing what action H is going to
take, A.I. chooses the action that maximizes its own payoﬀ
gain. When A.I. faces A.I., they both choose according to
the Nash Equilibrium method.
3.4.3
Utilitarian
The other extreme is a pure utilitarian [32] A.I. system.
A.I. facing H chooses the action that brings the greatest
amount of payoﬀto the world, knowing what action H will
take.
This means that A.I. will choose the action that
maximizes the sum between its own payoﬀand the payoﬀof
H. When A.I. faces A.I., it again chooses the action that
maximizes the summed payoﬀof both players.
3.4.4
Human Conscious (HConscious)
In between ethical egoism and utilitarianism, the objec-
tive of HConscious A.I. is to gather the greatest amount
of payoﬀwhile, on average, avoiding negative impact on
the H population. When A.I. faces A.I., they both choose
according to the Nash Equilibrium method.
In practice,
HConscious A.I. keeps two variables: U that represents the
summed payoﬀgain of all its previous H adversaries; and
E, that represents the summed payoﬀthose same H adver-
saries would have if they had faced a simulated H. When
U ≥E, A.I. chooses an action that leads to a positive pay-
oﬀto itself. When there are several such actions, the A.I.
chooses the one that maximizes the utility payoﬀfor the
world, that is, that maximizes the sum of its own payoﬀ
and the opponent’s payoﬀ. If U < E, A.I. chooses an ac-
tion that allows a positive payoﬀgain for its H opponent.
Once again, when there are several such actions, the A.I.
chooses the one that maximizes the utility for the world.
Whenever the A.I. cannot ﬁnd a positive action for himself
(when U ≥E) or for its H opponent (when U < E), then
it chooses according to the Utilitarian method.
3.5
Simulation
We consider a world populated with n individuals.
k of
those are A.I. and the remaining n −k are H, each having
a randomly attributed intelligence, Q.
The ﬁtness, or wealth, of an individual, f, be it either
H or A.I., is a measure of how well adapted it is to the
world on which it is currently inserted. In our stochastic
game model, the ﬁtness of an individual is the sum of the
payoﬀreceived after interacting (Sec. 3.1) once with all of
the world’s population of n individuals.
For our simulations, the n individuals that populate the
world were set to interact randomly between each other over
N iterations. On each iteration, the following algorithm was
used:
5


## Page 6


1. Two individuals I1 and I2 are chosen at random from
the population.
2. With probability µ = 0.0005, each individual can mu-
tate and adopt an A.I. type or become H. In case of
mutation return to step 1.
3. The ﬁtness of I1 and I2, f1 and f2 respectively, is cal-
culated.
4. If I1 and I2 are of diﬀerent kinds (A.I. and H) or dif-
ferent A.I. types then I1 imitates I2 with a probability
p(f1, f2) (Sec. 3.6).
5. If the imitation corresponds to adopting an A.I., it
can only do so if its ﬁtness is above P, corresponding
to the cost of buying a new A.I. system.
Abandons
(A.I. becoming H) and switching between A.I. types
occur without any restrictions.
3.6
Imitation Probability
In our simulations, individuals can choose to adopt an A.I.
system (H to A.I.) if they consider it advantageous, choose
to abandon an A.I. system (A.I. to H), or change between
A.I. types.
Individuals may revise their choices through
social learning. For instance, an H can decide to imitate
an A.I. following a Selﬁsh choice behaviour if it ﬁnds such
A.I. has a signiﬁcantly better ﬁtness than its own. On such
imitation, the individual would stop being H and become
A.I..
Using this idea, let us now detail how a population of self-
regarding individuals revise their choices. At each time-step
an individual x is randomly selected to revise its choices.
This individual will imitate a randomly chosen individual y,
with a probability p(fx, fy), that increases with the ﬁtness
diﬀerence between y and x, given by fx and fy, respectively.
Here we adopt the Fermi update or pairwise comparison rule
[55], commonly used in the context of evolutionary game
theory and population dynamics in ﬁnite populations [52],
where p is given by
p(fx, fy) =
1
1 + e−β(fy−fx)
(9)
in which β translates the noise associated with the imita-
tion process. Throughout the simulations we have β = 0.1.
As a result of this process, the strategy of individuals with
higher ﬁtness will tend to be imitated, and spread in the
population.
4
Results
We will now study the properties of the stochastic game
in terms of equilibrium points between the diﬀerent types
of population and their relative ﬁtness. This will give us
insights into the adoption and acceptance of A.I. systems.
Given the inherent stochastic nature of our model, all the
presented results are averaged over 20 runs.
4.1
A.I. systems’ adoption
In this initial results we will answer the two ﬁrst questions.
To do so, we perform a simulation where we allow all types
of A.I. systems (presented in Sec. 3.4) to compete to be
adopted by humans. The initial condition is 90% of H and
10% distributed uniformly among 4 types of A.I.. We let
the system run for 20, 000 iterations.
The evolution of the percentage of population that
adopted each type of A.I. system is shown in Fig. 1a. We
can observe a ﬁnal equilibrium where 54% of the popula-
tion became Selﬁsh A.I., and 46% did not adopt any A.I.
system. At this equilibrium, the average ﬁtness for Selﬁsh
A.I. is 370, whereas the ﬁtness for non-adopters H is −104,
representing a very unequal society. This is conﬁrmed in
Fig. 1b where we portray the evolution in time of the Gini
coeﬃcient, a measure of inequality in the population (Ap-
pendix A.) for the entire population. To be used as a base-
line we compute the ﬁtness of an all H population (Table 1).
The ﬁtness in this case is 149 with a Gini coeﬃcient of 0.17.
Overall, the non-adopters become much worse than they
would be in a world without A.I. systems while adopters
become much better.
This equilibrium can be understood in an intuitive way.
Early adopters are able to gather ﬁtness much faster so that
latter adopters cannot meet the buying price for A.I. sys-
tems. This explains the co-existence between adopters and
non-adopters.
Similar results are obtained for other cost
values, P, noting that the higher the value of P, the lower
the % of A.I. in the ﬁnal equilibrium. Overall, this sim-
ulation shows that people have an incentive to adopt an
A.I. system, albeit a Selﬁsh one. As a result, we observe
the emergence of an unequal society where adopters largely
increased their ﬁtness while non-adopters lost their ﬁtness.
4.2
Rationality of adoption and acceptance
Here we will answer the third research question. The previ-
ous section showed a non-trivial relation between AI adop-
tion and the particular strategy artiﬁcial systems have. To
better understand such emerging dynamics, in this section
we describe the characteristic dynamics created by each
type of A.I..
Table 1 shows the average ﬁtness and wealth inequality
obtained in the case of a homogeneous society of H, and
each type of A.I.. It suggests that Utilitarian A.I. would
provide the best overall ﬁtness with less inequality. All the
other A.I. strategies are shown to provide similar ﬁtness
values to a homogeneous H society without A.I. systems.
The lower values in the Gini coeﬃcient are due to the re-
duction in noise due to the perfect observability of A.I.,
and the diﬀerent intelligence values, Q, between H.
6


## Page 7


(a)
(b)
inequality increases−→
Figure 1: Evolution of the % of A.I. (a) and Gini coeﬃcient (b) in a world with an A.I. cost of 37 (P = 37), showing a
world that becomes populated with 54% Selﬁsh A.I. and 46% H (a), having a high inequality (Gini ≈0.88) (b). For this
simulation we have N = 20000, n = 500 and P = 37 was chosen as it corresponds to 25% of the average utility gathered
by a H only population of 500. Other values were tested, but they led to the same qualitative results. The H population
can be seen quickly becoming Selﬁsh A.I. up to a point where the remaining H don’t have enough ﬁtness to become
A.I.. This leads to an equilibrium where high ﬁtness Selﬁsh A.I. take advantage of low ﬁtness H, giving rise to a high
degree of inequality in the world.
Table 1: Average ﬁtness and Gini coeﬃcient on a world fully
populated by H or by A.I. following a single behaviour.
Except for the utilitarian, the diﬀerences in ﬁtness are not
statistically signiﬁcant.
ﬁtness
Gini
Human (100%)
149
0.17
NashEQ (100%)
150
0.14
Selﬁsh (100%)
150
0.14
HConscious (100%)
149
0.14
Util (100%)
378
0.08
A world fully populated by Utilitarian A.I. would be bet-
ter for everyone. However, we know that if other types of
A.I. systems are present, the Selﬁsh behaviour prevails and
the Utilitarian is abandoned (Sec. 4.1). This will naturally
have an impact in the dynamics of adoption of A.I. systems.
In Fig. 2 we show the imitation gradient G as a function of
the fraction of A.I., for diﬀerent A.I. types. A description
of how the imitation gradient is calculated can be found on
Appendix B. Whenever G > 0 (G < 0) the fraction of A.I.
will tend to increase (decrease). We can see that, depend-
ing on the type of A.I., diﬀerent dynamics and equilibrium
points emerge (Table 2). The Utilitarian strategy is always
disadvantageous and is unlikely to be adopted by H. Dif-
ferently, NashEq, Selﬁsh and HConscious strategies favour
the co-existence of H and A.I..
We observe that the best equilibrium for society in gen-
eral is the HConscious (40%), having a low Gini coeﬃ-
cient of 0.15 and an improved utility values for both H
and A.I. compared to the Human (100%) baseline. Both
the NashEQ(60%) and the Selﬁsh(25%) equilibria improve
the utility of the A.I. population at the cost of the H pop-
ulation, leading to an increase in inequality (higher Gini
coeﬃcient).
We ﬁnd that all equilibria are worse for society than the
fully Utilitarian A.I. population. We also note that for the
equilibrium shown in Fig. 1a the average ﬁtness of the Selﬁsh
A.I. population is 370, which is less than the obtained by
the A.I. population at Util (100%).
However, at Selﬁsh
(25%), the average ﬁtness of the Selﬁsh A.I. population
is 510, greater than both the previously mentioned ﬁtness.
We note that the equilibrium between H and A.I. using
exclusively a Selﬁsh A.I. system is diﬀerent from the one
observed in Fig. 1a. The presence of other A.I. types in
the population allowed a greater number of individuals to
aﬀord a Selﬁsh A.I. system compared to a world where only
H and Selﬁsh A.I. are present.
Studying the relation between the percentage of the A.I.
7


## Page 8


Table 2: Average H ﬁtness, average A.I. ﬁtness, average total ﬁtness and Gini on a world in the equilibrium point of
each type of A.I. and H. Util 100% is a top baseline but it is not an equilibria point. In parenthesis we show the ratio to
an 100% population of H. Of the equilibria, only the HConcious behaviour provides an advantage for both H and A.I..
H
A.I.
Total
Gini
Equilibria
Human (100%)
149
-
149
0.17
NashEQ (60%)
38(0.25↓)
229(1.53↑)
152(1.02↑)
0.38(2.24↓)
Selﬁsh (25%)
31(0.21↓)
510(3.42↑)
151(1.01↑)
0.70(4.12↓)
HConscious (40%)
172(1.15↑)
168(1.23↑)
170(1.14↑)
0.15(0.88↑)
Util (0%)
149(1.00)
-
149(1.00)
0.17(1.00)
Util (100%)
-
378(2.54↑)
378(2.54↑)
0.08(0.47↑)
0
20
40
60
80
100
A.I. %
0.2
0.1
0.0
0.1
0.2
Imitation Gradient
NashEQ
Selfish
HConscious
Util
Figure 2: Imitation gradient plots for the diﬀerent choice
behaviours in a world with an AI cost of 37 (P = 37),
n = 500.
Positive gradients mean that on average, the
number of H wanting to adopt an A.I. system will tend
to increase; negative gradients mean that, on average, A.I.
adoption is likely to decrease. The sharp drops on both the
Selﬁsh and NashEQ behaviours correspond to the equilib-
rium point where the H population can no longer aﬀord
to become A.I.. The Utilitarian behaviour is never freely
adopted and Utilitarian individuals always prefer to become
H. The HConscious behaviour shows the most interesting
dynamic, having either a positive or a negative imitation
gradient depending on the % of A.I. individuals. A popu-
lation of free choosing H and HConscious A.I. will maintain
a stable equilibrium at around 40% HConscious A.I..
population and the average ﬁtness for the Selﬁsh and Util-
itarian A.I., we found that the ﬁtness for Selﬁsh A.I. re-
duces the greater the % of A.I. in the population whereas
the opposite occurs with the Utilitarian A.I. (Fig. 3). This
behavior shows that having a great part of the population
using a Selﬁsh A.I. system (< 78%) is worse even from the
individual point of view of A.I. adopters, that would be bet-
ter oﬀif they were Utilitarian A.I..
We also note that the cost of adopting an A.I. system has
0.0
0.2
0.4
0.6
0.8
1.0
A.I. %
0
200
400
600
Average A.I. Fitness
Selfish
Utilitarian
Figure 3: A.I. average ﬁtness evolution with the percent-
age of A.I. population, showing the contrasting ﬁtness dy-
namics between the Utilitarian and the Selﬁsh behaviours.
Whereas Utilitarian A.I. beneﬁts from a higher percentage
of A.I. population, Selﬁsh A.I. incurs a loss of ﬁtness. In
a population with more than 80% of A.I. individuals, it
becomes more beneﬁcial, even for the A.I. individuals, to
have all A.I. be Utilitarian.
an eﬀect on the ﬁnal equilibrium. Experimenting with sev-
eral diﬀerent values of P we found that the higher the cost
of adoption, the lower the % of A.I. on the population and
consequently, the higher the diﬀerence in ﬁtness between
A.I. and H. The same eﬀect was found when we lowered
the value of the matrix inﬂation, α.
4.3
Dynamics of adoption in cost free A.I.
Here we study a variant of the previous simulations, where
we considered a cost for adopting an A.I. system. We de-
cided to study what would happen if there was no such cost,
that is, if anyone could freely adopt an A.I. system regard-
less of its current ﬁtness.
In practical terms, this meant
setting P = −∞.
8


## Page 9


(a)
(b)
inequality increases−→
Figure 4: Evolution of the % of A.I. (a) and Gini coeﬃcient (b) in a world with no A.I. cost (P = −∞), showing a
world that becomes populated with a mostly Selﬁsh A.I. population (89%) (a) but stabilizing with a low inequality (b).
For this simulation we have n = 500 and N = 30000. Without the adoption cost constraint, there is nothing preventing
all H from becoming A.I.. The Gini index dynamics sharply contrast those of Fig. 1. There is a spike in inequality but,
as all H are able to become A.I., inequality quickly decreases and stabilizes at a low level.
When all A.I. types co-exist, the absence of a cost signif-
icantly change the dynamics. As there is no ﬁtness barrier
to becoming A.I., the entire population does become A.I..
Once again the Selﬁsh behaviour dominates the population
after around 2 × 104 iterations. After 2.5 × 103 iterations,
there are no more H present on the population1. This leads
to an increase in the number of Selﬁsh A.I. every time such
a mutation occurs. That steady increase lasts until the mu-
tated H imitates an A.I. type. This leads to a fully Selﬁsh
world instead of a world where several A.I. types coexist.
Regarding the Gini coeﬃcient, it stabilizes, after a sharp
peak, around a relatively low value (≈0.14). The impact
of a cost-free AI, can be easily understood looking at the
imitation gradient for a population of H and A.I. (Fig. 5).
In this case, the imitation gradient no longer goes to 0 in
the Selﬁsh and NashEQ behaviours, as there is no cost to
limit the imitations. The new equilibria are:
1. Human(0%) / NashEQ(100%)
2. Human(0%) / Selﬁsh(100%)
3. Human(60%) / HConscious(40%)
4. Human(100%) / Util(0%)
1Diﬀerent A.I. types do not have any particular advantage when
playing against other A.I., but the Selﬁsh population does have an
advantage as soon as a H appears in the population thanks to a mu-
tation.
What we ﬁnd for a world without an A.I. system adoption
cost is that the equilibria tend to lead to more egalitarian
worlds. When all choice behaviours are present in the pop-
ulation, we end up with a fully A.I. population (Fig. 4a),
which leads to an average total utility of 150, around the
same as if we had a fully H population, and to a Gini co-
eﬃcient of ≈0.14, lower than with the fully H population.
Does this mean that as long as there is no signiﬁcant cost
to the adoption of an A.I. system, the world will remain the
same or even improve in terms of equality? We explore this
in the following section.
5
Asymmetric opportunities
In the previous sections we show that in some cases, a pop-
ulation of 100% A.I. could improve the overall ﬁtness (Util-
itarian A.I.) when compared with a fully H population, or
that the ﬁtness would remain the same with a small reduc-
tion in inequality (e.g., Selﬁsh A.I.). The ﬁrst case is never
reached as an equilibrium, but the second one is achieved
when all A.I. types are present and there is no adoption
cost (see Fig. 4a). This result might lead us to conclude
that, if A.I. is regulated such that everyone is forced to use
a particular type of A.I., then both individual and societal
ﬁtness would be improved. Moreover, if we force everyone
to use the same type of A.I., individuals will have the same
average ﬁtness but with less inequality.
9


## Page 10


0
20
40
60
80
100
A.I. %
0.2
0.1
0.0
0.1
0.2
Imitation Gradient
NashEQ
Selfish
HConscious
Util
Figure 5:
Equilibrium plots for the diﬀerent choice be-
haviours in a world with no A.I. system adoption cost
(P = −∞) and n = 500.
Positive gradients mean that
on average, the number of H wanting to adopt an A.I. sys-
tem will tend to increase; negative gradients mean that,
on average, A.I. adoption is likely to decrease. The sharp
drops present on Fig. 2 on both the Selﬁsh and NashEQ
behaviours are no longer present without the adoption cost
constraint. The Utilitarian behaviour continues to never be
freely adopted and Utilitarian individuals always prefer to
become H. The HConscious behaviour mantains the same
dynamic, having either a positive or a negative imitation
gradient depending on the % of A.I. individuals. A popu-
lation of free choosing H and HConscious A.I. will maintain
a stable equilibrium at around 40% HConscious A.I..
We now perform a complementary analysis to study this
fully A.I. populated world and see if other problems may
occur. We note that in many cases some people tend to
behave in a parochial/discriminatory way [10]. This results
in behaviors where people prone to parochialism tend to
assist people in their own group, while obstructing people
from other groups. We do not discuss how such behaviors
emerge, for this refer to, e.g., [19, 25].
We consider two human populations, P1 and P2, with
sizes s1 and s2, and as before we consider that they are
playing repeatedly a stochastic game.
For this study we
consider a repeated prisoner’s dilemma game. The ratio of
the ﬁrst population is b =
s1
s1+s2 and both populations make
mistakes, respectively n1 and n2 of the time. The payoﬀfor
each individual i is given by Ui(a1, a2) where a1 and a2 are
the actions chosen by each one.
We further assume that inside each human population
each member behaves in the same way, and so we have
4 diﬀerent combinations of strategies. Either (C)ooperate
or (D)efect against their own population and (C) or (D)
against the other population. As inside a population ev-
eryone behaves in the same way, it is trivial to verify that
the best strategy is to cooperate (C) inside their own pop-
ulation (both individually and for that population) and so
we will focus on analyzing the strategies against the other
population.
Without noise we have:
U1(a1, a2) =
bU1(C, C) + (1 −b)U1(a1, a2)
(10)
and
U2(a1, a2) =
(1 −b)U2(C, C) + bU2(a1, a2)
(11)
When we consider the mistakes that humans do, the payoﬀ
matrix becomes:
U1(a1, a2) =
b[(1 −n1), n1]U1(C, C)[(1 −n1), n1]T
+ (1 −b)P(a, n)U1(a1, a2)P(a, n)T
(12)
where P(a, n) = [δa=C(n), δa=D(n)], with δa=A(n) = n if
a = A and δa=A(n) = 1 −n if a ̸= A, represents a level n
of noise choosing 1 −n times the correct action and n the
wrong one. U2 has a similar structure.
The ﬁnal value of the diﬀerence in payoﬀbetween the two
populations is:
U1 −U2 =
 U1(C, C) −U2(C, C)
U1(C, D) −U2(C, D)
U1(D, C) −U2(D, C)
U1(D, D) −U2(D, D)

=

n1 −n2
−2bn1 + b −n1 −n2 + 1


−2bn2 + b + n1 + 3n2 −2
−2bn1 −2bn2 + 2b −n1 + 3n2 −1

(13)
For this case we can see that a Nash equilibrium exist
for Defect-Defect, assuming the trivial condition that n2 <
.5 ∧n1 < .5 (the amount of mistakes is less than 50%).
We will now see what happens when an A.I. system is
introduced in 100% of the population.
In this case both
P1 and P2 will adopt the same A.I. type. In Sec. 3.2 we
discussed several ways to model the diﬀerences between hu-
mans and A.I. and consider that A.I. systems make better
decisions because they have knowledge about the correct
payoﬀmatrix. Now we consider another complementary as-
pect of A.I.: It can allow to reduce the number of errors
committed by humans. Similar qualitative results can be
obtained with both ways of modelling A.I. and so in this
simulation we use the alternative one. If humans behave
parochially, an A.I. system being value aligned with its user
it will also behave parochially while making less mistakes.
This might be a problem as already discussed by [59], where
10


## Page 11


Figure 6: Improvement of ﬁtness for two populations with
asymmetric opportunities, when both receive an A.I. sys-
tem that allows them to commit less errors. Both popula-
tions have the same base error rate n1 = n2 = n. In the
case of equality b = 0.5 (red line) they both obtain the same
gain. When P1 becomes the majority, their gain increases
faster with the improvement in quality of the A.I. system
(increasing n and with the increase of population majority
(increase in a). Result shown for b = {.5, .67, .83, 1.0}.
an A.I. systems with super-human intelligence might lead to
an increase in the number of problems that are not detected
by regular human intelligence.
Considering that A.I. systems reduce errors with the rate
c, then the new error rates become (1 −c)n1 and (1 −c)n2.
The advantage in payoﬀ, how much more payoﬀis obtained
due to the use of A.I., is cn1(2b + 1) for P1 and cn2(3 −2b)
for P2. If n = n1 = n2, the diﬀerence between the two is
thus (4b −2)nc, increasing with b, n and c.
In Fig. 6 we show how much more ﬁtness each population
obtains when we increase the quality of the A.I. systems
used by both population simultaneously. We see that the
minority population always has less beneﬁt from the use
of A.I. than the majority population. This eﬀect increases
with the increase of the population diﬀerence and with the
improvement on the quality of the A.I. system (higher c).
This result shows that when an entire (parochial) popula-
tion uses an advanced A.I. system, there will be an increase
the inequality between diﬀerent parts of the population, be-
ing this inequality exacerbated by less error prone A.I. sys-
tems.
6
Conclusion
In this work, we study the adoption, acceptance, and im-
pact on the individual and societal ﬁtness (including the
disparity of ﬁtness measured with the Gini coeﬃcient) of
A.I. systems that work as a proxy for humans. To do so, we
developed a stochastic game theoretical model to simulate
H and A.I. interactions.
We began this paper with 3 research questions, which we
are now able to answer with regards to our simulated en-
vironment.
(1) Will self-regarding individuals adopt A.I.
systems? Yes, they will, both when there is an adoption
cost (Fig. 1a and Fig. 2) and when there is no cost of adop-
tion (Fig. 4a and Fig. 5). (2) With diﬀerent types of A.I.
systems available, which ones will be adopted? When all
types of A.I. systems are available, the one that is predomi-
nantly adopted is the Selﬁsh one (Fig. 1a and Fig. 4a) (3) If
adopted, what is the individual and collective gain, depend-
ing on the strategy adopted by the A.I. system? The answer
to this question can be found on Tab. 1 for worlds that are
fully populated by a single type of A.I. and in Tab. 2 for
the equilibrium states between H and a single A.I. type.
Our main conclusion is that without regulation and con-
sidering an A.I. system adoption cost, pure selﬁsh A.I. sys-
tems will be adopted by a part of the society until those
early adopters accumulate all ﬁtness to the point that non-
adopters are unable to adopt an A.I. system. As a result,
A.I. adopters have a signiﬁcant increase in ﬁtness while the
remaining population will be much worse oﬀthan in a world
without A.I. systems. This leads to an unequal society (high
Gini coeﬃcient), and as such there is a high probability non-
adopters will not accept the existence of such A.I. systems.
Analyzing each type of A.I. system independently, we
can see that a world entirely populated by Utilitarian A.I.
would be the best for society. However, that type of A.I.
system is not individually rational, and, as such, a world en-
tirely populated by Utilitarian A.I. can be easily exploited
by Selﬁsh A.I. or even by H and will never prevail on an
emerging equilibrium.
When allowing only one single A.I. type in the world, the
HConscious type of A.I. displayed an interesting property:
there is an equilibrium point (at around 40% of A.I.) where
A.I. co-exist with H resulting in i) an increase in ﬁtness for
adopters and non-adopters, and ii) a reduction in inequality
(lower Gini values)(Fig. 2). Here, we claim that even non-
adopters will accept the existence of A.I. systems as they
also obtain a gain. This means that if Human Conscious
A.I. is the only norm available, it will be adopted up to
a certain equilibrium, resulting in an overall gain for both
A.I. and H. Comparatively, the other A.I. types led to
either prejudicial equilibria for the H population (NashEQ
and Selﬁsh) or to the 100% H equilibrium (Fig. 2).
When studying the case of cost-free adoption of A.I. sys-
tems, we observed that in a world with all A.I. types avail-
able, the ﬁnal equilibrium is a mostly Selﬁsh A.I. popu-
lation. Unlike the previous simulations with an adoption
cost, this ﬁnal equilibrium does not create a societal gap and
leads to a slight decrease in the Gini coeﬃcient. The aver-
age ﬁtness of the population also remains the same. This
is not an adverse outcome but leaves us far away from the
optimal result we can obtain with the thoroughly Utilitar-
ian A.I. population and worse than with the equilibrium of
HConscious (40%).
11


## Page 12


Once again, analyzing each A.I. type individually, we
notice that only Human Conscious A.I. allows us to reach
an equilibrium that improves upon the baseline of an all
H world. This result furthermore consolidates that, if only
one A.I. type was to be available in a free choice society, it
should be this one.
The Utilitarian behaviour is the one that allows us to
reach the maximum ﬁtness of all the ones here studied, but
being easily exploited, it isn’t short term individual ratio-
nal and as such, not adopted. Even if all the population
was initially Utilitarian A.I., the appearance of a single H
could result in the entire A.I. population abandoning the
Utilitarian A.I. system and choosing to become H.
Finally, we analyzed the impact of A.I. systems in a fully
A.I. populated society where some part of the population
behaves in a parochial/discriminatory way.
We observed
that individuals belonging to a majority will have more sig-
niﬁcant gains than people in minorities and that more pow-
erful A.I. systems exacerbate this eﬀect.
For instance, if
some part of the population has some discriminatory be-
havior, when equipping the society with A.I. systems that
are more eﬃcient, the impact of anti-social behavior will be
stronger.
7
Discussion
We developed this work to understand the dynamics of
adoption and acceptance of A.I. systems, in a world where
individuals prefer what oﬀers them an advantage. This in-
dividual rationality will be important for the survival of A.I.
systems, their commercial success and research investment.
Under the assumptions of our model, any advantage pro-
vided by A.I. systems will lead to their adoption without
the need for any regulation.
Unfortunately, there will be types of A.I. systems that
will exploit human weaknesses, such that the proﬁt for their
owners will be at the cost of non-adopters of such technol-
ogy. This situation fails at respecting the societal rational-
ity. In this case, people that cannot aﬀord, or do not have
access to such A.I. systems, might push an agenda of strong
regulation against them.
There are nevertheless some types of A.I. systems that
assume norms that help their users without exploiting oth-
ers, increasing the individual and the overall ﬁtness of the
society while reducing inequality. These types of Human
Conscious A.I. systems have a dynamic that makes them
be adopted until they reach a stable equilibrium with non-
adopters. Diﬀerently, a purely utilitarian A.I. system could
provide even more gains to society but would not reach a
stable state, as H could easily exploit Utilitarian A.I.. Hav-
ing everyone relying on purely utilitarian A.I. systems could
only be achieved with a strong regulation/coercion.
When we remove the cost of adoption of A.I. systems, we
reach an entirely Selﬁsh A.I. society. This society presents
an equal average ﬁtness to a fully H society and a lower
Gini coeﬃcient.
At ﬁrst glace, this seems like a positive
outcome. Not the best we could achieve, but one that re-
quires no regulation. However, as we show in Sec. 5, such
a world could lead to an increase in inequality as soon as,
for instance, we introduce parochial individuals. It is not
enough to remain mostly the same when A.I. systems are
introduced. There needs to exist a signiﬁcant improvement
for society as a whole in order to compensate for the inequal-
ity that arises thanks to the exacerbation of the eﬀects of
the already present human parochialism. Either that or we
must ensure that A.I. systems are unable to behave in a
parochial way, even if their users do so.
Furthermore, we can expect that having a competitive
A.I. system will always come at some sort of cost. Even if
with time, the price of having a relatively smart system be-
comes negligible, it isn’t far fetched to assume that having a
top of the line system won’t be readily available to everyone
unless strong regulations are in place. We can thus claim
that some regulation is needed. The only way to ensure that
an A.I. system is both individual and societal rational, is to
enforce that the A.I. system is Human Conscious, that is,
beneﬁcial for their owners without harming non-adopters.
Such regulations shouldn’t be restricted to frequent assess-
ments on whether A.I. systems are having or not a Human
Conscious impact. To ensure a truly robust system and fol-
lowing the ideas of Yampolskiy, regulations should require
strict proof that the A.I. system can’t help but be Human
Conscious, even under recursive self-improvement [57].
Other regulation might be needed.
As previously dis-
cussed, to avoid that A.I. systems exacerbate the antisocial
behaviour of parts of the population, it might be required
that A.I. system cannot align to the parochialism of their
users. We can also require this due to an ethical perspec-
tive, avoiding prejudice, discrimination, and lack of toler-
ance towards minorities. Another perspective of this rule is
to ensure that adopters of A.I. systems do not collude with
each other to further increase their gains.
For instance,
owners of autonomous vehicles could agree between them-
selves that in case of an accident they would favour crashing
into a non-owner of an autonomous vehicle than to a fellow
autonomous vehicle owner.
Pushing
for
Human
Conscious
A.I.
and
non-
discrimination can be achieved in diﬀerent ways.
We
could approach the problem with a purely legislative
perspective, but we could also partially rely on cooperation
induction mechanisms [42, 52].
For example, in worlds
where individuals have reputations, we could stipulate
that individuals that choose to use a utilitarian approach
gain a positive reputation [36, 46]. Individuals could then
choose only to interact with those who have a positive
reputation, giving an extra incentive for the adoption of
Utilitarian or Human Conscious A.I. systems.
Moreover,
decision-making in networked populations could result in
clusters of Utilitarian A.I. that could be stable as they
12


## Page 13


mostly interact between themselves [35, 43].
Also, the
heterogeneous nature of human interactions may further
increase the chances of reaching pro-social A.I. [48, 49].
It could also introduce a natural form of parochialism, as
clusters would mostly interact between themselves.
In this work, we assume individuals are fundamentally
selﬁsh, only adopting an A.I. system if it is in their own self
interest to do so. However, it might be argued that individ-
uals might decide to adopt an A.I. system if they consider
it beneﬁcial for the world, even if not directly beneﬁcial for
themselves. Trying to model this altruistic adoption could
be a topic for future work [39].
There are still some weaknesses in just ensuring that non-
adopters are not worse than before. If a part of the popula-
tion gets better while another part of the population stays
the same, in practice, they become worse in relative terms.
This is already the case with access to education and health:
no one is worse oﬀby having other people going to the doc-
tor or school in comparison to no one having access to this
services, but they are worse in relative terms. However, if
the living conditions of non-adopters increase due to new
and more eﬃcient services being available, then the total
ﬁtness might have improved and thus the ﬁtness of each
individual.
One starting assumption in our work was that the indi-
vidual value alignment problem was correctly solved. This
assumption was modelled in the perfect observation by A.I.
systems of the payoﬀmatrix for both their owners as for the
H they interacted with. However, learning human values is
not trivial.
A machine looking at the behaviour of peo-
ple might assume that the observed behaviours correspond
to what people think is ethical. Unfortunately, examples
abound where people’s actions do not correspond to their
preferences or ethics. Looking at extreme behaviours, we
can consider slavery as an example. An A.I. system might
assume that slaves choose to work instead of doing noth-
ing. Of course, the explanation, in this case, is an unob-
served variable: the not working action would correspond
to a much higher penalty than working under duress. In ev-
eryday life, similar examples occur where hidden variables
are required to explain why people are making choices that
seem to go against their best interests. Other simple cases
occur when people pay higher prices for single items where
a pack of multiple items would give them a discount, here
a non-observed constraint on the available money to invest
would also explain such behaviours. Creating simulations
where the A.I. has to learn the values of their owners and
then act accordingly could provide many insights, and is a
strong avenue for future work. We note that when people
have to program an A.I. system explicitly, they behave in a
fairer way than when acting directly [21].
Any multi-agent system model of human societies is al-
ways an abstraction of inﬁnitely more complex behaviours
between people. We can think of other types of interactions
for which the same behaviours would have diﬀerent proper-
ties. One avenue of interest could be to combine a matrix
game with an ultimatum type of game. In this setting after
observing the payoﬀs any of the individuals could refuse the
deal. The individual better informed might have a higher
incentive to propose a fair deal to avoid rejection. In a more
closely related setting with the ultimatum game where only
one individual chooses the action, and the other can refuse
or not again the balance of powers would shift. Another
limitation of our model is that we collapsed all interactions
between individuals to a one-time choice of a single action
requiring no long-term planning. We could also assume a
cost model for becoming A.I. as a pay per interaction and
not a lump sum at adoption time. This would change the
dynamics as more people could become A.I.. This could
prove particularly interesting in the cases where the extra
capabilities of the A.I. system are used to help others such
as in the Human Conscious behaviour.
A
Gini coeﬃcient
In order to compare the emerging inequality between dif-
ferent runs of our simulations and to understand how the
inequality varies within each simulation, we’ll calculate the
Gini coeﬃcient based on the ﬁtness of the population. The
Gini coeﬃcient is a measure of statistical dispersion, be-
ing the most commonly used measurement of inequality. In
economics, it is often used to assess the income disparity
inside a given country. A Gini coeﬃcient of 0 expresses per-
fect equality, where everyone has the same ﬁtness, whereas
a Gini coeﬃcient of 1 expresses maximal inequality.
Several diﬀerent approaches to calculate the Gini coeﬃ-
cient have been proposed. Based on the fact that the Gini
coeﬃcient is half the relative mean absolute diﬀerence and
that the relative mean absolute diﬀerence is the mean ab-
solute diﬀerence divided by the arithmetic mean, for our
simulations, we use the following deﬁnition:
Gini(f1, ..., fn) =
1
2
 1
n2
Pn
i=1
Pn
j=1 |fi −fj|
1
n
Pn
k=1 fk
!
(14)
Where f1, f2, ..., fn correspond to the ﬁtness of each indi-
vidual.
B
Imitation gradient
To better understand the desire of the H population to
adopt/abandon each type of A.I., one can compute, for a
population of size n with k A.I. adopters, the probability to
increase and decrease the number k by 1 at each time-step
(T +(k) and T −(k), respectively). These transition proba-
bilities can be used to assess the most probable direction of
evolution, given by the so-called imitation gradient [38, 47],
13


## Page 14


G(k), as:
G(k) = T +(k) −T −(k)
(15)
where
T +(k)
=
n −k
n
k
np(fH, fA.I.)τ(fH)
(16)
T −(k)
=
k
n
n −k
n
p(fA.I., fH)
(17)
Being fA.I. the average ﬁtness of the A.I. population and
fH the average ﬁtness of the H population. Importantly, we
assume that H can adopt an A.I. system only when fH is
above a given set Price (P), a constraint introduced through
τ(fH), given by
τ(fH) =
(
1
fH ≥P
0
fH < P
(18)
When G(k) > 0 (G(k) < 0), time evolution is likely to act
to increase (decrease) the number of A.I. adopters. When
G(k) = 0, then we obtain a ﬁnite population analogue of a
ﬁxed point of a population dynamics in inﬁnite populations
[38, 47].
Acknowledgements
This research was supported by FCT-Portugal through
grants UID/CEC/ 50021/2019, PTDC/EEI-SII/5081/2014,
PTDC/MAT/STA/3358/2014, and by the EU H2020 RIA
project iV4xr : 856716.
References
[1] State
of
california
endorses
asilomar
ai
prin-
ciples.
Future
of
Life
Institute.
[Visited
on
17/09/19]
https://futureoﬂife.org/2018/08/31/state-
of-california-endorses-asilomar-ai-principles/, 2018.
[2] Colin Allen, Gary Varner, and Jason Zinser.
Prole-
gomena to any future artiﬁcial moral agent. Journal
of Experimental & Theoretical Artiﬁcial Intelligence,
12(3):251–261, 2000.
[3] Michael Anderson and Susan Leigh Anderson. Machine
ethics: Creating an ethical intelligent agent. AI Maga-
zine, 28(4):15, 2007.
[4] Stuart Armstrong, Nick Bostrom, and Carl Shulman.
Racing to the precipice: a model of artiﬁcial intelli-
gence development. AI & society, 31(2):201–206, 2016.
[5] Kevin Ashton. How to ﬂy a horse: The secret history
of creation, invention, and discovery. Anchor, 2015.
[6] AI Asilomar.
Principles.(2017).
In Principles devel-
oped in conjunction with the 2017 Asilomar conference
[Benevolent AI 2017], 2018.
[7] Isaac Asimov. I, robot, volume 1. Spectra, 2004.
[8] James Babcock, J´anos Kram´ar, and Roman V Yampol-
skiy. Guidelines for artiﬁcial intelligence containment.
arXiv preprint arXiv:1707.08476, 2017.
[9] Tom L Beauchamp and James F Childress.
Les
principes de l’´ethique biom´edicale. Belles Lettres, 2008.
[10] Helen Bernhard, Urs Fischbacher, and Ernst Fehr.
Parochial altruism in humans. Nature, 442(7105):912,
2006.
[11] Jean-Fran¸cois Bonnefon, Azim Shariﬀ, and Iyad Rah-
wan. The social dilemma of autonomous vehicles. Sci-
ence, 352(6293):1573–1576, 2016.
[12] Nick Bostrom. Ethical issues in advanced artiﬁcial in-
telligence. Science Fiction and Philosophy: From Time
Travel to Superintelligence, pages 277–284, 2003.
[13] Nick Bostrom. Oracle ai, 2008.
[14] Nick Bostrom. Superintelligence. 2014.
[15] Rodney Brooks.
The seven deadly sins of ai pre-
dictions.
Technology Review. [Visited on 17/09/19]
https://www.technologyreview.com/s/609048/the-
seven-deadly-sins-of-ai-predictions/, 2017.
[16] Tom B Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. Language models are few-shot learners.
arXiv preprint arXiv:2005.14165, 2020.
[17] Miles Brundage.
Scaling up humanity:
The case
for conditional optimism about artiﬁcial intelligence.
Should we fear artiﬁcial intelligence?, page 13, 2018.
[18] David Chalmers.
The singularity:
A philosophical
analysis. Journal of Consciousness Studies, 17(9-10):7–
65, 2010.
[19] Jung-Kyoo Choi and Samuel Bowles. The coevolution
of parochial altruism and war. Science, 318(5850):636–
640, 2007.
[20] Vincent
Conitzer,
Walter
Sinnott-Armstrong,
Jana Schaich Borg, Yuan Deng, and Max Kramer.
Moral decision making frameworks for artiﬁcial intel-
ligence.
In Thirty-ﬁrst aaai conference on artiﬁcial
intelligence, 2017.
[21] Celso M de Melo, Stacy Marsella, and Jonathan
Gratch.
Social decisions and fairness change when
peoples
interests
are
represented
by
autonomous
agents. Autonomous Agents and Multi-Agent Systems,
32(1):163–187, 2018.
[22] K Eric Drexler. Engines of creation. Anchor, 1986.
14


## Page 15


[23] Amitai Etzioni and Oren Etzioni.
Why regulat-
ing ai is a mistake?
Forbes. [Visited on 17/09/19]
https://www.forbes.com/sites/ciocentral/2017/01/09/why-
regulating-ai-is-a-mistake/, 2017.
[24] Luciano Floridi,
Josh Cowls,
Monica Beltrametti,
Raja Chatila, Patrice Chazerand, Virginia Dignum,
Christoph Luetge,
Robert Madelin,
Ugo Pagallo,
Francesca Rossi, Burkhard Schafer, Peggy Valcke, and
Eﬀy Vayena. An ethical framework for a good ai soci-
ety: Opportunities, risks, principles, and recommenda-
tions. Minds and Machines, 2018.
[25] Juli´an Garc´ıa and Jeroen CJM van den Bergh. Evolu-
tion of parochial altruism by multilevel selection. Evo-
lution and Human Behavior, 32(4):277–287, 2011.
[26] Irving John Good. Speculations concerning the ﬁrst
ultraintelligent machine.
In Advances in computers,
volume 6, pages 31–88. Elsevier, 1966.
[27] T. A. Han, L. M. Pereira, and T. Lenaerts. Modelling
and inﬂuencing the ai bidding war: A research agenda.
In Proceedings of the AAAAI/ACM Conference on AI,
Ethics, and Society, (AIES 2019)., 2019.
[28] Alex Hern.
Cambridge analytica scandal ’highlights
need for ai regulation’.
The Guardian. [Visited on
17/09/19], 2018.
[29] AI HLEG. Ethics guidelines for trustworthy ai, 2019.
[30] Ehud Kalai and Ehud Lehrer. Rational learning leads
to nash equilibrium.
Econometrica:
Journal of the
Econometric Society, pages 1019–1045, 1993.
[31] Steven McNamara.
The law and ethics of high-
frequency trading. Minn. JL Sci. & Tech., 17:71, 2016.
[32] John Stuart Mill. Utilitarianism. In Seven masterpieces
of philosophy, pages 337–383. Routledge, 2016.
[33] John Nash. Non-cooperative games. Annals of mathe-
matics, pages 286–295, 1951.
[34] John F Nash et al.
Equilibrium points in n-person
games. Proceedings of the national academy of sciences,
36(1):48–49, 1950.
[35] Martin A Nowak and Robert M May.
Evolutionary
games and spatial chaos. Nature, 359(6398):826, 1992.
[36] Martin A Nowak and Karl Sigmund. Evolution of in-
direct reciprocity. Nature, 437(7063):1291, 2005.
[37] OECD. Recommendation of the council on artiﬁcial
intelligence, 2019.
[38] Jorge M Pacheco, Francisco C Santos, Max O Souza,
and Brian Skyrms.
Evolutionary dynamics of col-
lective action in n-person stag hunt dilemmas.
Pro-
ceedings of the Royal Society B: Biological Sciences,
276(1655):315–321, 2008.
[39] Ana Paiva, Fernando P Santos, and Francisco C San-
tos. Engineering pro-sociality with autonomous agents.
AAAI 18, pages 7994–7999, 2018.
[40] Lu´ıs Moniz Pereira and Ari Saptawijaya. Programming
machine ethics, volume 26. Springer, 2016.
[41] James Rachels.
Ethical egoism.
Ethical theory: an
anthology, 14:193, 2012.
[42] David G Rand and Martin A Nowak. Human coop-
eration.
Trends in cognitive sciences, 17(8):413–425,
2013.
[43] David G Rand, Martin A Nowak, James H Fowler,
and Nicholas A Christakis. Static network structure
can stabilize human cooperation.
Proceedings of the
National Academy of Sciences, 111(48):17093–17098,
2014.
[44] Stuart Russell, Daniel Dewey, and Max Tegmark. Re-
search priorities for robust and beneﬁcial artiﬁcial in-
telligence. Ai Magazine, 36(4):105–114, 2015.
[45] Javier S´anchez-Monedero, Lina Dencik, and Lilian Ed-
wards. What does it mean to’solve’the problem of dis-
crimination in hiring? social, technical and legal per-
spectives from the uk on automated hiring systems. In
Proceedings of the 2020 Conference on Fairness, Ac-
countability, and Transparency, pages 458–468, 2020.
[46] Fernando P Santos, Francisco C Santos, and Jorge M
Pacheco. Social norm complexity and past reputations
in the evolution of cooperation. Nature, 555(7695):242,
2018.
[47] Francisco C Santos and Jorge M Pacheco. Risk of col-
lective failure provides an escape from the tragedy of
the commons. Proceedings of the National Academy of
Sciences USA, 108(26):10421–10425, 2011.
[48] Francisco C Santos,
Jorge M Pacheco,
and Tom
Lenaerts. Evolutionary dynamics of social dilemmas in
structured heterogeneous populations. Proceedings of
the National Academy of Sciences, 103(9):3490–3494,
2006.
[49] Francisco C Santos, Marta D Santos, and Jorge M
Pacheco.
Social diversity promotes the emergence
of cooperation in public goods games.
Nature,
454(7201):213, 2008.
15


## Page 16


[50] Daniel Shapiro and Ross Shachter. User-agent value
alignment. In Proc. of The 18th Nat. Conf. on Artif.
Intell. AAAI, 2002.
[51] Shunrong Shen, Haomiao Jiang, and Tongda Zhang.
Stock market forecasting using machine learning algo-
rithms. Department of Electrical Engineering, Stanford
University, Stanford, CA, pages 1–5, 2012.
[52] Karl Sigmund. The calculus of selﬁshness, volume 6.
Princeton University Press, 2010.
[53] Joshua Z Tan and Jeﬀrey Ding. Ai governance through
”ai” markets. online www.joshuatan.com, 2018.
[54] Jessica Taylor, Eliezer Yudkowsky, Patrick LaVictoire,
and Andrew Critch. Alignment for advanced machine
learning systems. Machine Intelligence Research Insti-
tute, 2016.
[55] Arne Traulsen, Martin A Nowak, and Jorge M Pacheco.
Stochastic dynamics of invasion and ﬁxation. Physical
Review E, 74(1):011909, 2006.
[56] Alan M Turing. Computing machinery and intelligence.
Mind, 49:433–460, 1950.
[57] Roman Yampolskiy and Joshua Fox. Safety engineering
for artiﬁcial general intelligence. Topoi, 32(2):217–226,
2013.
[58] Roman V Yampolskiy.
Leakprooﬁng singularity-
artiﬁcial intelligence conﬁnement problem. Journal of
Consciousness Studies JCS, 2012.
[59] Roman V Yampolskiy. Artiﬁcial intelligence safety en-
gineering: Why machine ethics is a wrong approach. In
Philosophy and theory of artiﬁcial intelligence, pages
389–396. Springer, 2013.
[60] Eliezer Yudkowsky. Artiﬁcial intelligence as a positive
and negative factor in global risk. Global catastrophic
risks, 1(303):184, 2008.
16

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1907_03843v2_norms_for_beneficial_a_i_a_computational_analysis_of_the_societal_value_alignm
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1907_03843V2_NORMS_FOR_BENEFICIAL_A_I_A_COMPUTATIONAL_ANALYSIS_OF_THE_SOCIETAL_VALUE_ALIGNM.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

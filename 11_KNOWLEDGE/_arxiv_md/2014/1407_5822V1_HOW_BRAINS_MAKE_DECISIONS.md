---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1407.5822v1
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1407.5822v1_How_brains_make_decisions

> Source: 1407.5822v1_How_brains_make_decisions.pdf

> Pages: 20

---


## Page 1


arXiv:1407.5822v1  [physics.bio-ph]  22 Jul 2014
How brains make decisions
V.I. Yukalov1,2 and D. Sornette1,3
1Department of Management, Technology and Economics,
ETH Z¨urich, Swiss Federal Institute of Technology,
Z¨urich CH-8092, Switzerland
2Bogolubov Laboratory of Theoretical Physics,
Joint Institute for Nuclear Research, Dubna 141980, Russia
3Swiss Finance Institute, c/o University of Geneva,
40 blvd. Du Pont d’Arve, CH 1211 Geneva 4, Switzerland
Abstract
This chapter, dedicated to the memory of Mino Freund, summarizes the Quantum
Decision Theory (QDT) that we have developed in a series of publications since 2008.
We formulate a general mathematical scheme of how decisions are taken, using the
point of view of psychological and cognitive sciences, without touching physiological
aspects. The basic principles of how intelligence acts are discussed. The human brain
processes involved in decisions are argued to be principally diﬀerent from straightfor-
ward computer operations. The diﬀerence lies in the conscious-subconscious duality
of the decision making process and the role of emotions that compete with utility
optimization. The most general approach for characterizing the process of decision
making, taking into account the conscious-subconscious duality, uses the framework of
functional analysis in Hilbert spaces, similarly to that used in the quantum theory of
measurements. This does not imply that the brain is a quantum system, but just allows
for the simplest and most general extension of classical decision theory. The resulting
theory of quantum decision making, based on the rules of quantum measurements,
solves all paradoxes of classical decision making, allowing for quantitative predictions
that are in excellent agreement with experiments. Finally, we provide a novel applica-
tion by comparing the predictions of QDT with experiments on the prisoner dilemma
game. The developed theory can serve as a guide for creating artiﬁcial intelligence
acting by quantum rules.
1


## Page 2


1
What is brain intelligence
The brain is the center of the nervous system in all vertebrates and most invertebrates.
Only a few invertebrates, such as sponges, jellyﬁsh, sea squirts, and starﬁsh do not have one,
though they have diﬀuse neural tissue. The brain of a vertebrate is the most complex organ
of its body. In a typical human, the cerebral cortex is estimated to contain 86 ± 8 billion
neurons [1], each connected by synapses to several thousand other neurons.
The functioning of the brain can be considered from two diﬀerent perspectives, physio-
logical and psychological. We do not touch here the physiological side of the problem that is
studied in neurobiology, medicine, and is also modeled by neuron networks [2–4]. Our aim
is to model the functioning of the psychological brain, which is studied in cognitive sciences.
The ability of the brain to take decisions is termed intelligence. There exist numerous
and rather lengthy discussions attempting to describe what intelligence is [5–12]. Summa-
rizing these discussions, the basic feature of intelligence, which can be accepted as its brief
deﬁnition, is the ability of adaptation to the environment by the process of making optimal
decisions. This implies that the notion of intelligence is foremost the ability of making de-
cisions. It is generally accepted that humans possess the highest level of intelligence in the
animal kingdom. But animals also are able to take decisions, to adapt to their environment
and to solve problems [13]. Thence, animals also possess intelligence.
This concerns all
animals, such as birds, ﬁsh, reptiles, amphibians, and insects. Moreover, other living beings,
say plants, in some sense, do adapt to surrounding by making decisions [14]. Therefore, we
need to accept that, to some degree, all alive beings have a kind of intelligence, since all of
them adjust to their environment by reacting to external signals. Thus, one can talk of the
intelligence of plants, fungi, bacteria, protista, amoebae, algae, and so on. In that sense,
any entity that is able to take decisions, adapting to surrounding signals, can be assumed
to have something like intelligence. If such an entity that is able to take optimal decisions
is created by humans, it is called artiﬁcial intelligence [15].
In the following, we shall be mostly concerned with the functioning of the human brain,
though many parts of our considerations could be applied to the functioning of the brains
and nervous systems of other alive beings. The human brain, being the most developed and
complex, exhibits in the most explicit way the features that could be met in the behavior
of other animals. The aim of this paper is to demonstrate that the human brain makes
decisions in a rather intricate way that cannot be described by the classical utility or prospect
theory used in economics. We argue that decisions made by brains are not the same as
straightforward computer-like calculations. Human decisions are based on the functioning
of and interplay between conscious as well as subconscious processes of the brain.
This
complex behavior can be represented by the techniques of quantum theory, which seems
to be the most general and simplest framework for realistically characterizing the decision
making process of human brains.
The plan of the paper is as follows. In Sec. 2, we recall how decisions are supposed to be
made by fully rational decision makers who evaluate the utility of prospects and choose the
one with the largest utility. Such a strictly deterministic behavior is a strong simpliﬁcation
of the reality. Empirical observations show that there always exists a distribution of choices
made by diﬀerent subjects, rather a single optimal behavior. Even the same subject, under
varying conditions or time, can make diﬀerent choices when confronted with the same set of
competing prospects.
2


## Page 3


This implies that the ﬁrst step towards a realistic representation of decision making
is the reformulation of classical utility theory within a probabilistic framework, which is
accomplished in Sec.
3.
Analyzing the signals, the subject formulates a set of possible
actions, πj, termed prospects that are weighted with probabilities p(πj). Taking a decision
means the selection of an optimal prospect π∗characterized by the largest probability, though
other prospects can also be chosen, with lower probabilities, that is, with lower frequency.
The possible actions are always weighted with a probability distribution. This describes
the probability weighted diversity of choices among a population of similar decision makers.
There always exists a probability that some of the members choose one prospect, while
others choose another prospect, although the majority prefers the optimal prospect. This is
the essence of the probability weight that is associated with the frequentist interpretation,
which deﬁnes the fraction of those who choose the related prospect.
Although the probabilistic utility theory that we introduce in Sec.
3 generalizes the
standard deterministic utility theory, it does not take into account that real decision makers
are not fully rational. Moreover, they experience a variety of emotions and behavioral biases.
As a result, decisions are taken not by a simple evaluation of utilities but are essentially
inﬂuenced by these biases and emotions. In taking decisions, two brain processes are involved,
conscious and subconscious. This dual functioning of the brain makes its principally distinct
from the straightforward calculations by a computer, as is discussed in Sec. 4.
To take into account this complex dual behavior, Sec. 5 presents a generalization of
decision theory, which invokes the techniques of the quantum theory of measurements. The
developed Quantum Decision Theory (QDT) contains none of the paradoxes that are so
numerous in classical decision making. Importantly, we show that classical decision theory
constitutes a particular case of QDT. The latter reduces to the former under a process
that can be called “decoherence”, which describes how the addition of reliable information
decreases the emotional component of a decision, thus making it more and more controlled
by the rational utility component.
To illustrate how QDT describes how decisions are made, avoiding the paradoxes of
classical decision making and providing quantitative predictions, we treat in Sec.
6 the
prisoner dilemma game.
Section 7 summarizes the results, stressing that the developed QDT is, to our knowledge,
the sole decision theory that not merely removes classical paradoxes, but provides quantita-
tive predictions, with no adjustable parameters, which are in good agreement with empirical
observations.
Concluding this introduction, our main hypothesis is that the brain makes decisions
through a procedure that is similar to quantum measurements. This does not require the
brain to be a quantum object, but merely takes into account the dual nature of the decision
process, involving both conscious logical evaluations as well as subconscious intuitive feelings.
This chapter summarizes the Quantum Decision Theory (QDT) that we have developed in a
series of publications [16–21]. We also provide a novel application on the prisoner dilemma
game, comparing the predictions of QDT with experiments.
3


## Page 4


2
Choosing a prospect on fully rational grounds
Assuming that the subject is fully rational and possesses the whole necessary information for
making decisions, it is reasonable to suppose that such decisions are based on the evaluation
of the utility of the results following the corresponding action. This is the central assumption
of expected utility theory, which prescribes a normative framework on how decisions are
made. The basic mathematical rules of expected utility theory have been compiled by von
Neumann and Morgenstern [22] and Savage [23]. Below, we give a brief sketch of the main
features of utility theory in order to introduce the terminology to be used in the following
sections, where the generalizations of this theory will be considered.
The outcomes of actions, that is, the consequences of events, are measured by payoﬀs
composing a set
X ≡{xn ∈R : n = 1, 2, . . . , Nout} .
(1)
The number of outcomes Nout can be as small as two or asymptotically large.
Positive
outcomes correspond to gains, while negative ones to losses.
Payoﬀs xn can come with
diﬀerent probabilities pj(xn), being labeled by an index j = 1, 2, . . . , L, and satisfying the
normalization condition
Nout
X
n=1
pj(xn) = 1 ,
0 ≤pj(xn) ≤1 .
(2)
The ensemble of payoﬀs and their probabilities is called a lottery, or a prospect
πj = {xn, pj(xn) : n = 1, 2, . . . , Nout} .
(3)
One also uses the notion of compound lotteries that are the linear combinations of a given set
of lotteries, with the same payoﬀs and with the linear combinations of the related weights.
There can exist several prospects forming a family
L = {πj : j = 1, 2, . . . , L} .
(4)
The task of decision making is to decide between the prospects πj, choosing one out of the
given family.
The choice involves the classiﬁcation of outcomes according to their utility for the decision
maker. One deﬁnes a utility function u(x) : X →R that can also be called pleasure function,
satisfaction function, or proﬁt function. By deﬁnition, the utility function is nondecreasing
(more is always preferred), so that u(x1) ≥u(x2) for x1 ≥x2 and concave (diminishing
marginal utility), such that u(α1x1 + α2x2) ≥α1u(x1) + α2u(x2) for non-negative αi’s nor-
malized to one. The ﬁrst derivative u′(x) ≡du(x)/dx is termed the marginal utility that
is non-negative for a non-decreasing function. The second derivative u′′(x) ≡d2u(x)/dx2 is
non-positive for a concave function. Hence, the marginal utility u′(x) does not increase. This
implies that, with increasing payoﬀx, the utility function decelerates. Such a function is
termed risk averse [24,25], since a sure payoﬀis always preferred to diﬀerent random payoﬀs
with the same mean value. The risk aversion can be captured by the so-called degree of
risk aversion r(x) ≡−u′′(x)/u′(x), which is non-negative. Examples of utility functions are
linear, power-law, logarithmic or exponential functions. Usually, the utility of nothing is set
to zero, u(0) = 0, but the absolute utility level is inconsequential.
4


## Page 5


Generally, a payoﬀxn can be either positive, representing a gain, or negative correspond-
ing to a loss. Strictly speaking, it is impossible to lose something, while having nothing.
Even the poorest person can lose a gamble and go in debt, having an instantaneous negative
net worth. However, taking into account the value of future incomes gives in general a pos-
itive net value and the debt then constitutes a loss of a part of future incomes. There can
be however situations where debt reaches levels beyond the most optimistic expectations of
future incomes, so that one has lost what one did not own now or will ever have in the future.
In its encyclopedic review of the history of debt in human societies, Graeber documents that
such situations were quite common [26]. They were usually followed by slavery (and are still
in various explicit or disguised forms followed by some kind of slavery), where the person in
debt sells his children, wife or himself. A loss is then backed up by the ultimate reservoir of
wealth, being stored in the value of oneself [26]. Formally, this implies that, before losing xn,
one has an initial given amount x0 ≥xn. Then, shifting all payoﬀs by x0, one can redeﬁne
the lottery so that all its payoﬀs be non-negative.
Each prospect is characterized by the expected utility
U(πj) =
Nout
X
n=1
u(xn)pj(xn).
(5)
This notion was introduced by Bernoulli [27] and an axiomatic theory was developed by
von Neumann and Morgenstern [22], where the payoﬀweights were treated as objective.
Savage [23] extended the notion to subjective probabilities evaluated by decision makers.
Expected utility can be interpreted either as a cardinal or ordinal quantity. Cardinal
utility is assumed to be precisely measured and the magnitude of the measurement is mean-
ingful. It can be measured in some chosen units, similarly to how distance is measured in
meters, or time in hours, or weight in kilograms. However, such a deﬁnition in precise units is
often impossible and, actually, not necessary. It is suﬃcient to interpret the expected utility
as ordinal utility, for which its precise magnitude is not important, but the magnitude of the
ratios between diﬀerent utilities carries suﬃcient meaning.
The prospect uncertainty is described by the prospect variance
var(πj) ≡
1
Nout
Nout
X
n=1

x2
npj(xn) −[x(πj)]2	
,
(6)
whose square root can also be called the prospect volatility or spread. We have used the
following notation for the prospect mean
x(πj) ≡
1
Nout
Nout
X
n=1
xnpj(xn) .
(7)
The ordering of the prospects is prescribed by the relations between their expected utili-
ties. One says that a prospect is preferable to another one if its utility is larger than that of
the latter. Two prospects are termed indiﬀerent when their utilities coincide. The properties
of the utility function u(x) prescribe the properties of the expected utility.
(i) Completeness: For any two prospects π1 and π2, one of the following relations neces-
sarily holds, either π1 = π2, or π1 < π2, or π1 > π2, or π1 ≤π2, or π1 ≥π2, understood as
the corresponding relations between their expected utilities.
5


## Page 6


(ii) Transitivity: For any three prospects, such that π1 ≤π2 and π2 ≤π3, it follows that
π1 ≤π3.
(iii) Continuity: For any three prospects ordered so that π1 ≤π2 ≤π3, there exists
α ∈[0, 1] such that π2 = απ1 + (1 −α)π3.
(iv) Independence: For any π1 ≤π2 and an arbitrary π3, there exists α ∈[0, 1] such that
απ1 + (1 −α)π3 ≤απ2 + (1 −α)π3.
The central aim of expected utility theory is to calculate the expected utilities for all
prospects from the given family L and, comparing their values, to ﬁnd the prospect possessing
the largest utility. Then the decision is taken by selecting this prospect corresponding to the
largest utility, which is called the most useful prospect. The decision making scheme based
on expected utility theory is given in Fig. 1.
3
Probabilistic approach to expected utility theory
According to the expected utility theory delineated above, the choice of a prospect is with
certainty prescribed by the utility of the prospects. This theory is deterministic, since the
choice, with probability one, is required to correspond to the prospect with the largest ex-
pected utility. Such a completely deterministic formulation contradicts the known empirical
facts demonstrating that, under the same conditions, diﬀerent persons often choose diﬀerent
prospects. Of course, one could salvage the deterministic theory by introducing heterogenous
utility functions that describe the variety of tastes of diﬀerent people [28]. While this cap-
tures the evident observation that tastes exhibit some heterogeneity, extending utility theory
to heterogeneous or random utility theory comes at the cost of a proliferation of parameters,
making the approach descriptive at best, while being non-parsimonious and non predictive.
An even more convincing attack to the deterministic approach comes from the observation
that the same person, under the same conditions, may choose diﬀerent prospects at diﬀerent
times. This “intra-observer variation” has been largely documented in the medical litera-
ture [29,30]. This suggests to view the brain of a decision maker as deliberating on the set
of admissible prospects and evaluating them by involving some probabilistic weighting. This
is the motivation to reformulate utility theory by generalizing it to a probabilistic approach.
The probabilistic weighting of prospects can be formalized by invoking the principle of
minimal information that allows one to ﬁnd a probability distribution under the minimal
given information. The idea of this principle goes back to Gibbs [31–33], who formulated it
as a conditional maximization of entropy under the given set of constraints. This principle
is widely used in information science [34] and in physics [35,36]. A general convenient form
of an information functional is given by the Kullback-Leibler relative information [37,38].
In order to weight the prospects according to their utility, let us consider a family of
prospects L. Assume that they can be weighted by means of a distribution deﬁned by utility
factors f(πj) that are normalized,
L
X
j=1
f(πj) = 1 ,
0 ≤f(πj) ≤1 .
(8)
By deﬁnition, the utility factor of zero utility is to be zero,
f(πj) = 0 ,
U(πj) = 0 .
(9)
6


## Page 7


Since the utility factors f(πj) weight the ﬁnite utilities U(πj), the total ﬁnite expected utility
deﬁned by
U =
L
X
j=1
U(πj)f(πj)
(10)
should exist, given a ﬁnite number L of prospects.
Under these conditions, we can deﬁne the Kullback-Leibler information as
I[f] =
X
j
f(πj) ln f(πj)
f0(πj) + λ
"X
j
f(πj) −1
#
−β
"X
j
U(πj)f(πj) −U
#
,
(11)
with a trial distribution f0(πj) proportional to the expected utility U(πj) in order to take into
account condition (9). The parameters λ and β are the Lagrange multipliers guaranteeing
the validity of the imposed constraints (normalization (8) and existence of a well-deﬁned
ﬁnite expected utility (10)) .
Minimizing the information functional (11) yields the utility factor
f(πj) = U(πj)
Z
exp{βU(πj)} ,
(12)
with a normalization coeﬃcient
Z =
X
j
U(πj) exp{βU(πj)} .
The parameter β characterizes the level of belief or conﬁdence of the decision maker in the
correct selection of the prospect set. Requiring that the utility factor, by its deﬁnition, be
an increasing function of utility makes the belief parameter non-negative (β ≥0).
In the case of no conﬁdence in the given set of prospects, we have
f(πj) =
U(πj)
P
j U(πj)
(β = 0) .
(13)
In the opposite case of absolute conﬁdence, we get
f(πj) =

1,
πj = maxj πj
0,
πj < maxj πj
(β →∞) ,
(14)
where maxj πj is the prospect whose expected utility is the largest. Thus, the latter situation
(β →∞) retrieves the deterministic utility theory, which hence can be seen as a particular
case of the more general probabilistic approach.
The prospect utility factors {f(πj) : j = 1, 2, ..., L} give the fractions of decision makers
selecting the corresponding prospects {πj : j = 1, 2, ..., L}. The ordering of prospects in the
probabilistic approach is the same as in the standard expected utility theory. But now, not
all subjects are forced to choose the most useful prospect, though it is the prospect whose
choice is the most probable. There can exist a fraction of decision makers choosing other
prospects with lower utility. The probabilistic decision making scheme is summarized in Fig.
2.
7


## Page 8


4
Human decision making and computer operations
It is widely believed that the human brain operates, during a decision making process, as a
complex and powerful computer. The network of neurons within the brain accepts external
signals and transforms them into decisions of the subject by accomplishing the corresponding
actions [39]. Such a procedure could correspond to the schemes depicted in Fig. 1 or Fig. 2.
However, if the brain would act as just described, this would correspond to making
decisions only on the basis of a well deﬁned deterministic objective function, called util-
ity. But there exist numerous empirical studies demonstrating that humans often deviate
from and even contradict the choices prescribed by utility theory. Such contradictions are
known as decision-making paradoxes. As examples, we can mention the Allais paradox [40],
the Ellsberg paradox [41], the Kahneman-Tversky paradox [42], the Rabin paradox [43],
the Ariely paradox [44], the disjunction eﬀect [45], the conjunction fallacy [46], the plan-
ning paradox [47], and many others [48, 49]. These paradoxes cannot be resolved by the
approaches consisting in modifying the expected utility theory into so-called non-expected
utility theories, as has been proved in Refs. [50,51].
The appearance of numerous paradoxes in decision making, based on utility theory, is
caused by the fact that this theory does not take into account the emotional components
always present in decision makers, which often compete and modify the decisions that would
result purely from utility-based processes. A human decision maker not merely evaluates
the objective utility of the prospects, but also is inﬂuenced by subjective feelings, emotions,
and behavioral biases that are produced by subconscious brain activity. The brain takes
decisions by combining (i) the objective knowledge of the prospect utility, by evaluating the
utility factors, with (ii) the subjective attractiveness of the prospects, which is hinted by
subconscious feelings. The latter means that, in addition to the utility factors measured by
conscious logical operations, there should exist attraction factors produced by subconscious
feelings. Then, the resulting weights of the prospects p(πj) are deﬁned not merely by the
utility factors f(πj), but are also dependent on some attraction factors q(πj).
We thus
suggest that the correct representation of the brain function during a decision process is
given by the scheme represented in Fig. 3, which should correct and replace those of Figs.
1 or 2.
Our theory views the human brain not just a powerful computer accomplishing a great
number of straightforward logical operations, but as an object that must include parallel
functioning on two levels. One part, representing conscious logical operations evaluating the
utility factors, can be organized as a powerful computer. And the other part, representing
subconscious activity producing the attraction factors, should be a very diﬀerent device that
functions not as a straightforward computer calculating numbers, but as an object estimating
qualitative features of the prospects.
In the sequel, we do not touch on the technical issues of how the devices, discussed above,
are actually structurally realized, or how they could be constructed in an artiﬁcial brain.
Instead, we describe how their functioning can be represented mathematically, characterizing
the split dual action of evaluating the prospect utilities and estimating their attractiveness.
8


## Page 9


5
Quantum decision making by human brain
The dualism of the brain, combining objective conscious operations with subjective subcon-
scious activity, suggests that its functions could be described by generalizing the real-valued
way of deﬁning the prospect weights to an approach involving complex-valued quantities. In
turn, this immediately points to quantum-theory techniques, where the probability weights
are deﬁned through complex-valued quantities, such as wave functions.
The idea of employing quantum theory for describing brain functions was advanced by
Bohr [52,53]. Analyzing the quantum theory of measurements, von Neumann [54] mentioned
that the action of measuring observables could be interpreted, to some extent, as taking
decisions.
Using these ideas, we have developed [16–21] the Quantum Decision Theory
(QDT), using the mathematical techniques of quantum theory of measurements.
Before formulating this theory, we would like to stress that the quantum approach to
describing human decision making does not assume that the brain is a quantum object.
The quantum techniques just provide the most straightforward way of generalizing decision
making by taking into account the dual functioning of the human brain.
The main points of QDT are as follows.
We consider a set of elementary prospects,
represented by vectors |n⟩, whose closed linear envelope
H ≡Span{|n⟩}
(15)
composes the space of mind. The prospects πj from the given set L are represented by the
vectors |πj⟩in the space of mind. The prospect operators are deﬁned as
ˆP(πj) ≡|πj⟩⟨πj| .
(16)
These operators play the same role as the operators from the algebra of local observables in
quantum theory.
The state of a decision maker is characterized by a non-negative operator ρ acting on the
space of mind and normalized as
Trˆρ = 1 ,
with the trace taken over the space of mind. Deﬁning the decision-maker state by a statistical
operator, but not by a simple wave function, takes into account that this decision maker is
not an absolutely isolated subject, but can be inﬂuenced by its environment.
The prospect probabilities, playing the role of observable quantities, are deﬁned as the
averages of the prospect operators
p(πj) ≡Trˆρ ˆP(πj) ,
(17)
with the trace again taken over the space of mind. Writing down the explicit expression for
the trace over the elementary prospect states and separating the diagonal and oﬀ-diagonal
parts leads to the sum
p(πj) = f(πj) + q(πj) ,
(18)
in which the ﬁrst term comes from the diagonal part and the second term, from the oﬀ-
diagonal part. The ﬁrst term represents the classical utility factor, while the second term,
9


## Page 10


caused by the prospect quantum interference, is the attraction factor. By deﬁnition, the
prospect probability is non-negative and normalized, so that
L
X
j=1
p(πj) = 1
0 ≤p(πj) ≤1 .
(19)
In view of the normalization condition for the utility factor (8), the attraction factor lies in
the range
−1 ≤q(πj) ≤1
(20)
and satisﬁes the alternation law
L
X
j=1
q(πj) = 0 .
(21)
Generally, the attraction factor is a contextual quantity that can vary for diﬀerent decision
makers and even for the same decision maker at diﬀerent times. This looks as an obstacle
for the ability to give quantitative predictions for the prospect probabilities. However, it is
possible to show [18, 21] that the aggregate attraction factor, averaged over many decision
makers, enjoys the property called quarter law:
1
L
L
X
j=1
|q(πj)| = 1
4 .
(22)
Since the utility factor is uniquely deﬁned by the corresponding expected utility, it is possible
to estimate quantitatively the prospect probabilities, assuming that the typical attraction
factor satisﬁes the quarter law.
When the decision maker is a member of a society from which he/she gets additional
information, then the attraction factor varies depending on the amount µ of the received
information.
The attraction factor, as a function of the information measure µ, can be
presented [55] in the form
q(πj, µ) = q(πj, 0)e−γµ .
(23)
The information can be positive, with µ > 0 as well as negative, or misleading, with µ <
0. Respectively, the attraction factor can either decrease or increase. The attenuation of
behavioral biases with the receipt of additional information has been conﬁrmed by empirical
studies [56,57].
The reduction of QDT to the probabilistic variant of classical decision theory corresponds
to the attraction factor tending to zero. This is similar to the reduction of quantum theory
to classical statistical theory in the process of decoherence.
6
Cooperation paradox in prisoner dilemma games
Let us brieﬂy summarize the status of QDT with respect to its empirical support. First,
the disjunction eﬀect, studied in diﬀerent forms in a variety of experiments [45], has been
analyzed in details in [18,21], where we found that the empirically determined absolute value
of the aggregate attraction factor |q(πj)| was found to coincide with the value 0.25 predicted
by expression (22), within the typical statistical error of the order of 20% characterizing these
10


## Page 11


experiments. The same agreement, between the QDT prediction for the absolute value of the
attraction factors and empirical values, holds for experiments testing the conjunction fallacy.
The planning paradox has also found a natural explanation within QDT [17]. Moreover, it
has been shown [20] that QDT explains practically all typical paradoxes of classical decision
making, arising when decisions are taken by separate individuals.
In order to illustrate how QDT resolves classical paradoxes, let us consider a typical
paradox happening in decision making. In game theory, there is a series of games, in which
several subjects can choose either to cooperate with each other or to defect. Such setups
have the general name of prisoner dilemma games. The cooperation paradox consists in the
real behavior of game participants who often incline to cooperate despite the prescription
of utility theory for defection. Below, we show that this paradox is easily resolved within
QDT, which gives correct quantitative predictions.
The generic structure of the prisoner dilemma game is as follows. Two participants can
either cooperate with each other or defect from cooperation. Let the cooperation action of
one of them be denoted by C1 and the defection by D1. Similarly, the cooperation of the
second subject is denoted by C2 and the defection by D2. Depending on their actions, the
participants receive payoﬀs from the set
X = {x1, x2, x3, x4} ,
(24)
whose values are arranged according to the inequality
x3 > x1 > x4 > x2 .
(25)
There are four admissible cases: both participants cooperate (C1C2), one cooperates and
another defects (C1D2), the ﬁrst defects but the second cooperates (D1C2), and both defect
(D1D2). The payoﬀs to each of them, depending on their actions, are given according to the
rule

C1C2
C1D2
D1C2
D1D2

→

x1x1
x2x3
x3x2
x4x4

.
(26)
As is clear, the enumeration of the participants is arbitrary, so that it is possible to analyze
the actions of any of them.
Each subject has to decide what to do, to cooperate or to defect, when he/she is not
aware about the choice of the opponent. Then, for each of the participants, there are two
prospects, either to cooperate,
π1 = C1(C2 + D2) ,
(27)
or to defect,
π2 = D1(C2 + D2) .
(28)
In the absence of any information on the action chosen by the opponent, the probability
for each of these actions is 1/2 (non-informative prior). Assuming for simplicity the linear
utility as a utility function of the payoﬀs, the expected utility of cooperation for the ﬁrst
subject is
U(π1) = 1
2 x1 + 1
2 x2 ,
(29)
11


## Page 12


while the utility of defection is
U(π2) = 1
2 x3 + 1
2 x4 .
(30)
The assumption of linear utility is not crucial, and can be removed by reinterpreting the
payoﬀset (24) as the utility set. Because of condition (25), the utility of defection is always
larger than that of cooperation, U(π2) > U(π1). According to utility theory, this means that
all subjects have always to prefer defection.
However, numerous empirical studies demonstrate that an essential fraction of partic-
ipants choose to cooperate despite the prescription of utility theory.
This contradiction
between reality and the theoretical prescription constitutes the cooperation paradox [58,59].
Considering the same game within the framework of QDT, we have the probabilities of
the two prospects,
p(π1) = f(π1) + q(π1) ,
p(π2) = f(π2) + q(π2) .
(31)
The propensity to cooperation and the presumption of innocence propose that the attraction
factor for cooperative prospect is larger than that for the defecting prospect, that is, q(π1) >
q(π2). In view of the alternation law (21) and quarter law (22), we have
q(π1) = −q(π2) = 1
4 .
(32)
Hence, we can estimate the considered prospects by the equations
p(π1) = f(π1) + 0.25 ,
p(π2) = f(π2) −0.25 .
(33)
From here, we see that, even if defection seems to be more useful than cooperation, so that
f(π2) > f(π1), the cooperative prospect can be preferred by some of the participants.
To illustrate numerically how this paradox is resolved, let us take the data from the
experimental realization of the prisoner dilemma game by Tversky and Shaﬁr [45]. Subjects
played a series of prisoner dilemma games, without feedback. Three types of setups were
used: (i) when the subjects knew that the opponent had defected, (ii) when they knew that
the opponent had cooperated, and (iii) when subjects did not know whether their opponent
had cooperated or defected.
The rate of cooperation was 3% when subjects knew that
the opponent had defected, and 16% when they knew that the opponent had cooperated.
However, when subjects did not know whether their opponent had cooperated or defected,
the rate of cooperation was 37%.
Treating the utility factors as classical probabilities, we have
f(π1) = 1
2 f(C1|C2) + 1
2 f(C1|D2) ,
f(π2) = 1
2 f(D1|C2) + 1
2 f(D1|D2) .
According to the Tversky-Shaﬁr data,
f(C1|C2) = 0.16 ,
f(C1|D2) = 0.03 .
12


## Page 13


Hence,
f(π1) = 0.095 ,
f(π2) = 0.905 .
(34)
Then, for the prospect probabilities (33), we get
p(π1) = 0.345 ,
p(π2) = 0.655 .
(35)
In this way, the fraction of subjects choosing cooperation is predicted to be about 35%.
This is in remarkable agreement with the empirical data of 37% by Tversky and Shaﬁr.
Actually, within the statistical accuracy of the experiment, the predicted and empirical
numbers are indistinguishable.
If we would follow the classical approach, the fraction of cooperators should be not larger
than 10% (f(π1)), which is much smaller than the observed 37%. But in QDT, there are no
paradoxes and its predictions are in quantitative agreement with empirical observations.
7
Conclusion
We have presented the Quantum Decision Theory that we have developed in the last four
years, which is based on combining utility-like calculations with emotional inﬂuences in
the representation of the decision making processes.
We have emphasized that decision
making by humans is principally diﬀerent from the direct calculations by, even the most
powerful, computers. This basic diﬀerence is in the duality of the human decision-making
procedure.
The brain makes decisions by a parallel processing of two diﬀerent jobs: by
consciously estimating the utility of the available prospects and by subconsciously evaluating
their attractiveness.
We have shown how the duality of the brain functioning can be adequately represented
by the techniques of quantum theory. The process of decision making has been described
as mathematically similar to the procedure of quantum measurement. The self-consistent
mathematical theory of human decision making that we have been developed contains no
paradoxes typical of classical decision making. It is important to stress that this theory is
the ﬁrst theory allowing for it quantitative predictions taking into account behavioral biases.
We stress that the description of the functioning of the human brain by means of quantum
techniques does not require that the brain be a quantum object, but this approach serves as
an appropriate mathematical tool for characterizing the conscious-subconscious duality of
the brain processes. This duality must be taken into account when one attempts to create
an artiﬁcial intelligence imitating the human brain. Such an artiﬁcial intelligence has to be
quantum in the sense explained above [60].
Acknowledgment
The authors are grateful for many discussions with and advice from M. Favre and E.P.
Yukalova. Financial support form the Swiss National Science Foundation is appreciated.
13


## Page 14


References
[1] F.A.C. Azevedo, L.R.B. Carvalho, L.T. Grinberg, J.M. Farfel, R.E.L. Ferretti, R.E.P.
Leite, W.J. Filho, R. Lent and S. Herculano-Houzel, Equal numbers of neuronal and
non-neuronal cells make the human brain an isometrically scaled-up primate brain. J.
Compar. Neurol. 513, 532–541 (2009).
[2] G.M. Shepherd, Neurobiology (Oxford University, Oxford, 1994).
[3] E.R. Kandel, J.H. Schwartz, and T.M. Jessel, Principles of Neural Science (McGraw-
Hill, New York, 2000).
[4] O. Sporns, Networks of the Brain (Massachusetts Institute of Technology, New York,
2011).
[5] A.R. Luria, Higher Cortical Functions in Man (Basic Books, New York, 1966).
[6] D. Elkind and J. Flavell, Studies in Cognitive Development (Oxford University, New
York, 1969).
[7] R.J. Sternberg and W. Salter, Handbook of Human Intelligence (Cambridge University,
Cambridge, 1982).
[8] J.P. Das, J.A. Naglieri, and J.R. Kirby, Assessment of Cognitive Processes (Allyn and
Bacon, Needham Heights, 1994).
[9] W.K. Wake, H. Gardner, and M.L. Kornhaber, Intelligence: Multiple Perspectives (Har-
court Brace College, Fort Worth, 1996).
[10] K. Richardson, The Making of Intelligence (Columbia University, New York, 2000).
[11] R.J. Sternberg, ed. International Handbook of Intelligence (Cambridge University, Cam-
bridge, 2004).
[12] K. Stanovich, What Intelligence Tests Miss: The Psychology of Rational Thought (Yale
University, New Haven, 2009).
[13] S. Coren, The Intelligence of Dogs (Bantam Books, New York, 1995).
[14] A. Trewavas, Green plants as intelligent organisms. Trends Plant Sci. 10, 413–419
(2005).
[15] J. Canny, S.J. Russell, and P. Norvig, Artiﬁcial Intelligence: A Modern Approach (Pren-
tice Hall, Englewood Cliﬀs, 2003).
[16] V.I. Yukalov and D. Sornette, Quantum decision theory as quantum theory of measure-
ment. Phys. Lett. A 372, 6867–6871 (2008).
[17] V.I. Yukalov and D. Sornette, Physics of risk and uncertainty in quantum decision
making. Eur. Phys. J. B 71, 533–548 (2009).
14


## Page 15


[18] V.I. Yukalov and D. Sornette, Processing information in quantum decision theory. En-
tropy 11, 1073–1120 (2009).
[19] V.I. Yukalov and D. Sornette, Entanglement production in quantum decision making.
Phys. At. Nucl. 73, 559–562 (2010).
[20] V.I. Yukalov and D. Sornette, Mathematical structure of quantum decision theory. Adv.
Complex Syst. 13, 659–698 (2010).
[21] V.I. Yukalov and D. Sornette, Decision theory with prospect interference and entangle-
ment. Theor. Dec. 70, 283–328 (2011).
[22] J. von Neumann and O. Morgenstern, Theory of Games and Economic Behavior (Prince-
ton University, Princeton, 1953).
[23] L.J. Savage, The Foundations of Statistics (Wiley, New York, 1954).
[24] J.W. Pratt, Risk aversion in the small and in the large. Econometrica 32, 122–136
(1964).
[25] K.J. Arrow, Essays in the Theory of Risk Bearing (Markham, Chicago, 1971).
[26] D. Graeber, Debt: The First 5,000 Years (Melville House, New York, 2011).
[27] D. Bernoulli, Exposition of a new theory on the measurement of risk. Proc. Imper.
Acad. Sci. St. Petersburg 5, 175–192 (1738).
[28] D. McFadden, Econometric models of probabilistic choice. In Structural Analysis of
Discrete Data with Econometric Applications, C.F. Manski and D. McFadden (eds.)
(Massachusetts Institute of Technology, Cambridge, 1981), p. 198–272.
[29] I.M. Rutkow, Surgical decision making, the reproducibility of clinical judgment. Arch.
Surg. 117, 337–340 (1982).
[30] J.O. Nielsen, H. Dons-Jensen, and H.T. Sarrensen, Lauge-Hansen classiﬁcation of malle-
olar fractures, an assessment of the reproducibility in 118 cases. Acra Orthop. Scand.
61, 385–387 (1990).
[31] J.W. Gibbs, Elementary Principles in Statistical Mechanics (Oxford University, Oxford,
1902).
[32] J.W. Gibbs, Collected Works (Longmans, New York, 1928) Vol. 1.
[33] J.W. Gibbs, Collected Works (Longmans, New York, 1931) Vol. 2.
[34] C.E. Shannon and W. Weaver, Mathematical Theory of Communication (University of
Illinois, Urban, 1949).
[35] E.T. Jaynes, Information theory and statistical mechanics. Phys. Rev. 106, 620–630
(1957).
15


## Page 16


[36] V.I. Yukalov, Phase transitions and heterophase ﬂuctuations. Phys. Rep. 208 395–492
(1991).
[37] S. Kullback and R.A. Leibler, On information and suﬃciency. Ann. Math. Stat. 22
79–86 (1951).
[38] S. Kullback, Information Theory and Statistics (Wiley, New York, 1959).
[39] K. Mainzer, Thinking in Complexity (Springer, Berlin, 2007).
[40] M. Allais, Le comportement de l’homme rationnel devant le risque: critique des postu-
lats et axiomes de l’ecole Americaine. Econometrica 21, 503–546 (1953).
[41] D. Ellsberg, Risk, ambiguity, and the Savage axioms. Quart. J. Econ. 75, 643–669
(1961).
[42] D. Kahneman and A. Tversky, Prospect theory: an analysis of decision under risk.
Econometrica 47, 263–291 (1979).
[43] M. Rabin, Risk aversion and expected-utility theory: a calibration theorem. Economet-
rica 68, 1281–1292 (2000).
[44] D. Ariely, Predictably Irrational (Harper, New York, 2008).
[45] A. Tversky and E. Shaﬁr, The disjunction eﬀect in choice under uncertainty. Psychol.
Sci. 3, 305–309 (1992).
[46] A. Tversky and D. Kahneman, Extensional versus intuitive reasoning: the conjunction
fallacy in probability judgement. Psychol. Rev. 90, 293–315 (1983).
[47] F.E. Kydland and E.C. Prescott, Rules rather than discretion: the inconsistency of
optimal plans. J. Polit. Econ. 85, 473–492 (1977).
[48] C.F. Camerer, G. Loewenstein, and R. Rabin, eds., Advances in Behavioral Economics
(Princeton University, Princeton, 2003).
[49] M.J. Machina, Non-expected utility theory. In: New Palgrave Dictionary of Economics.
S.N. Durlauf and L.E. Blume, eds., (Macmillan, New York, 2008).
[50] Z. Safra and U. Segal, Calibration results for non-expected utility theories. Econometrica
76, 1143–1166 (2008).
[51] N.I. Al-Najjar and J. Weinstein, The ambiguity aversion literature: a critical assessment.
Econ. Philos. 25, 249–284 (2009).
[52] N. Bohr, Light and life. Nature 131, 421–423, 457–459 (1933).
[53] N. Bohr, Atomic Physics and Human Knowledge (Wiley, New York, 1958).
[54] J. von Neumann, Mathematical Foundations of Quantum Mechanics (Princeton Univer-
sity, Princeton, 1955).
16


## Page 17


[55] V.I. Yukalov and D. Sornette, Theory of behavioral decision biases of social agents,
http://ssrn.com/abstract=2018270 (2012).
[56] A. K¨uhberger, D. Komunska, and J. Perner, The disjunction eﬀect: does it exist for
two-step gambles? Org. Behav. Human Decis. Proc. 85, 250–264 (2001).
[57] G. Charness, E. Karni, and D. Levin, On the conjunction fallacy in probability judge-
ment: new experimental evidence regarding Linda. Games Econ. Behav. 68, 551–556
(2010).
[58] C. Camerer, Behavioral Game Theory (Princeton University, Princeton, 2003).
[59] A. Tversky, Preference, Belief, and Similarity: Selected Writings (Massachusetts Insti-
tute of Technology, Cambrideg, 2004).
[60] V.I. Yukalov and D. Sornette, Scheme of thinking quantum systems. Laser Phys. Lett.
6, 833–839 (2009).
17


## Page 18


Figure captions
Fig. 1. Scheme of the deterministic decision making process based on the choice of the
most useful prospect with the largest expected utility.
Fig. 2. Scheme of the probabilistic decision making process based on the evaluation
of the prospect utility factors characterizing the fraction of decision makers choosing the
related prospect.
Fig. 3. Scheme of human decision making, which is at the basis of the Quantum Decision
Theory proposed here.
18


## Page 19


Figure 1: Scheme of the deterministic decision making process based on the choice of the
most useful prospect with the largest expected utility.
19


## Page 20


Figure 2: Scheme of the probabilistic decision making process based on the evaluation of the
prospect utility factors characterizing the fraction of decision makers choosing the related
prospect.
Figure 3: Scheme of human decision making, which is at the basis of the Quantum Decision
Theory proposed here.
20

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1709.01024v5
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1709.01024v5_Payoff_Information_and_Learning_in_Signaling_Games

> Source: 1709.01024v5_Payoff_Information_and_Learning_in_Signaling_Games.pdf

> Pages: 55

---


## Page 1


PayoﬀInformation and Learning in Signaling
Games∗
Drew Fudenberg†
Kevin He‡
First version:
August 31, 2017
This version:
November 25, 2019
Abstract
We add the assumption that players know their opponents’ pay-
oﬀfunctions and rationality to a model of non-equilibrium learn-
ing in signaling games.
Agents are born into player roles and
play against random opponents every period. Inexperienced agents
are uncertain about the prevailing distribution of opponents’ play,
but believe that opponents never choose conditionally dominated
strategies.
Agents engage in active learning and update beliefs
based on personal observations. Payoﬀinformation can reﬁne or
expand learning predictions, since patient young senders’ experi-
mentation incentives depend on which receiver responses they deem
plausible. We show that with payoﬀknowledge, the limiting set
of long-run learning outcomes is bounded above by rationality-
compatible equilibria (RCE), and bounded below by uniform RCE.
RCE reﬁne the Intuitive Criterion (Cho and Kreps, 1987) and in-
clude all divine equilibria (Banks and Sobel, 1987). Uniform RCE
sometimes but not always exists, and implies universally divine
equilibrium.
Keywords: learning, equilibrium reﬁnements, bandit problems, pay-
oﬀinformation, signaling games.
JEL classiﬁcation codes C72, C73, D83
∗We thank Laura Doval, Glenn Ellison, Lorens Imhof, Yuichiro Kamada, Robert Klein-
berg, David K. Levine, Kevin K. Li, Eric Maskin, Dilip Mookherjee, Harry Pei, Matthew
Rabin, Bill Sandholm, Lones Smith, Joel Sobel, Philipp Strack, Bruno Strulovici, Tomasz
Strzalecki, Jean Tirole, Juuso Toikka, and two anonymous referees for helpful comments and
conversations, and National Science Foundation grant SES 1643517 for ﬁnancial support.
†Department of Economics, MIT. Email: drew.fudenberg@gmail.com
‡California
Institute
of
Technology
and
University
of
Pennsylvania.
Email:
hesichao@gmail.com
arXiv:1709.01024v5  [econ.TH]  14 Jan 2020


## Page 2


1
Introduction
Signaling games typically have many perfect Bayesian equilibria, because Bayes
rule does not pin down the receiver’s oﬀ-path beliefs about the sender’s type.
Diﬀerent oﬀ-path beliefs for the receiver can justify diﬀerent oﬀ-path receiver
behaviors, which in turn sustain equilibria with a variety of on-path outcomes.
For this reason, applied work using signaling games typically invokes some
equilibrium reﬁnement to obtain a smaller and (hopefully) more accurate sub-
set of predictions.
However, most reﬁnements impose restrictions on the oﬀ-path beliefs with-
out any reference to the process that might lead to equilibrium. As in our
earlier paper, Fudenberg and He (2018), this paper uses a learning model to
derive restrictions on out-of-equilibrium beliefs and thus restrict the equilib-
rium set. The innovation here is to restrict the agents’ initial beliefs about
opponents’ strategies to reﬂect knowledge of the opponents’ utility functions
(and that the opponents act to maximize their expected utility). This gener-
ates restrictions on long-run play that reﬁne the Intuitive Criterion (Cho and
Kreps, 1987) and include all divine equilibria (Banks and Sobel, 1987).
In our learning model, agents repeatedly play the same signaling game
against random opponents each period. Agents are Bayesians who believe they
face a ﬁxed but unknown distribution of the opposing players’ strategies. Im-
portantly, the senders start with independent prior beliefs about how receivers
respond to diﬀerent signals, so they cannot use the response to one signal to
infer anything about the distribution of responses to a diﬀerent signal. This
introduces an exploration-exploitation trade-oﬀ, as each sender only observes
the response to the one signal she sends each period. Long-lived and patient
senders will therefore experiment with every signal that they think might yield
a substantially higher payoﬀthan the myopically optimal signal. Thus, “out
of equilibrium” signals actually arise with positive probability as experiments.
The key to our results is that diﬀerent types of senders have diﬀerent incen-
tives for experimenting with various signals, so that some of the sender types
will send certain signals more often than other types do. Consequently, even
though long-lived senders only experiment for a vanishingly small fraction of
1


## Page 3


their lifetimes, the play of the long-lived receivers will best respond to be-
liefs about the senders’ types that reﬂects this diﬀerence in experimentation
probabilities.
Of course, the senders’ experimentation incentives depend on their prior
beliefs about which receiver responses are plausible after each signal.
The
set of learning outcomes depends on the assumptions we make on the set
of “allowable” priors over opponents’ strategies.
Fudenberg and He (2018)
restricted the set of allowable priors to be non-doctrinaire, which implies that
agents always assign a strictly positive probability to their opponents playing
strictly dominated strategies. An equilibrium proﬁle is patiently stable if it is a
long-run outcome with patient and long-lived agents for some non-doctrinaire
prior; Fudenberg and He (2018) shows that patiently stable proﬁles of signaling
games must satisfy a condition called the compatibility criterion (CC).
In this paper, we instead assume that the players’ prior beliefs encode
knowledge of their opponents’ payoﬀfunctions, so in particular the senders
assign zero probability to the event that the receivers choose conditionally
dominated actions after any signal.1 Inexperienced senders with full-support
beliefs about the receivers’ play may experiment with a signal in the hope that
the receivers respond with a certain favorable action, not knowing that this
action will never be played as it is not a best response to any receiver belief.
With payoﬀinformation, even very patient senders will never undertake such
experiments. Conversely, receivers know that no sender type would ever want
to play a signal that does not best respond to any receiver strategy, because no
possible response by the receiver would make playing that signal worthwhile.
For this reason, the receivers’ beliefs after each signal assign probability zero
to the types for whom that signal is dominated.
We introduce equilibrium reﬁnements for signaling games that provide up-
per and lower bounds on the set of rationally patiently stable learning out-
comes, the analog of patient stability when the allowable priors reﬂect payoﬀ
knowledge and are otherwise non-doctrinaire. Theorem 1 shows that every
rationally patient learning outcome where receivers have strict best responses
1An action is conditionally dominated after a given signal if it does not best respond to
any belief about the sender’s type.
2


## Page 4


to the on-path signals must be a “rationality compatible equilibrium” (RCE);
this is an equilibrium where oﬀ-path beliefs satisfy restrictions derived from the
comparative experimentation frequencies of diﬀerent sender types when they
know the receiver’s payoﬀfunction. Conversely, Theorem 2 shows that every
equilibrium that satisﬁes a uniform version of rational compatibility (uRCE)
and some strictness assumptions can arise as a patient learning outcome. That
is, for equilibria satisfying the relevant strictness assumptions, we have
uRCE ⊆rationally patiently stable proﬁles ⊆RCE
Importantly, the set of allowable priors with payoﬀinformation are not
nested with the priors we considered in Fudenberg and He (2018): Payoﬀin-
formation rules out priors that assign positive probability to strictly dominated
actions, while the full-support priors of Fudenberg and He (2018) require that
strictly dominated strategies receive positive probability. Thus the sets of pa-
tiently stable proﬁles and rationally patiently stable proﬁles are not in general
nested. Through a pair of examples, we illustrate that RCE better tracks the
set of rationally patiently stable outcomes than the solution concepts from
Fudenberg and He (2018) do.
In Example 2, the sender can be either strong or weak. The sender has
a safe option Out with a known payoﬀ, and a risky option In whose payoﬀ
depends on the receiver’s response. The receiver has three responses to In:
Up, which is optimal against the strong sender; Down, which is optimal
against the weak sender, and X, which is never optimal. We show that RCE
reﬁnes Fudenberg and He (2018)’s CC, and identiﬁes the unique rationally
patiently stable strategy proﬁle. Intuitively, this is because when priors encode
payoﬀinformation, the strong types experiment more with In than the weak
types do against any play of the receivers, which is not true when senders do
not know the receivers’ payoﬀfunctions.
In some other games, the set of rationally patiently stable proﬁles is larger
than that of patiently stable proﬁles, because payoﬀinformation leads to some
experiments not being taken at all. In Example 3, there is a signal that is never
used as an experiment when senders have payoﬀinformation, so the receivers’
3


## Page 5


beliefs and behavior after this signal are arbitrary. On the other hand, when
senders are ignorant of the receivers’ payoﬀfunctions, one sender type will
experiment much more frequently with this signal than the other type, leading
to a restriction on the receivers’ oﬀ-path beliefs and oﬀ-path behavior after
the signal. In this game, RCE exactly identiﬁes the set of rationally patiently
stable strategy proﬁles, while the strong CC (which is shown by Fudenberg
and He (2018) to be necessary for patient stability without payoﬀknowledge)
rules out some rationally patiently stable proﬁles.
Like RCE and uRCE, standard equilibrium reﬁnements do reﬂect the idea
that players know that their opponents will not play strictly dominated strate-
gies. Moreover, as we explain in Section 3, the nesting relationships
uRCE ⊊universally divine ⊊divine ⊊RCE ⊊Intuitive Criterion ⊊Nash.
hold for all equilibria where the receiver has strict incentives after all on-path
signals.
In particular, our learning-based belief restrictions resemble those
imposed by divine equilibrium (Banks and Sobel, 1987): Every divine equilib-
rium is also an RCE and every uRCE is path-equivalent to a universally divine
equilibrium. We should point out, though, that while every game has at least
one rationally patiently stable proﬁle, a uRCE need not exist; Example 4 is
one simple case where one does not.
1.1
Related Literature
This paper is most closely related to the work of Fudenberg and Levine (1993),
Fudenberg and Levine (2006), and Fudenberg and He (2018) on patient learn-
ing by Bayesian agents who believe they face a steady-state distribution of
play. Except for the support of the agents’ priors, our learning model is ex-
actly the same as that of Fudenberg and He (2018), and the proof of Theorem
1 follows the lines of our results there. Theorem 2 is the main technical inno-
vation. It establishes a suﬃcient condition for an equilibrium to be rationally
patiently stable.
The proof of this suﬃcient condition for rational patient
stability constructs a suitable prior and analyzes the corresponding rationally
4


## Page 6


patiently stable proﬁles. The only other constructive suﬃcient condition2 for
strategy proﬁles to be patiently stable is Theorem 5.5 of Fudenberg and Levine
(2006), which only applies to a subclass of perfect-information games. In such
games the relative probabilities of various oﬀ-path actions do not matter, be-
cause each oﬀ-path experiment is perfectly revealed when it occurs. Indeed,
the central lemma leading to Theorem 2 constructs a prior belief to ensure
that the receivers correctly learn the relative frequencies that diﬀerent types
undertake various oﬀ-path experiments. This lemma deals with an issue spe-
ciﬁc to signaling games, and is not implied by any result in Fudenberg and
Levine (2006).
Like this paper, Cho and Kreps (1987) and Banks and Sobel (1987) study
equilibrium reﬁnements in signaling games. We compare our learning-based
equilibrium reﬁnements with their reﬁnements, which implicitly assume that
players are certain of the payoﬀfunctions of their opponents.
Our paper is also related to other models of Bayesian non-equilibrium learn-
ing, such as Kalai and Lehrer (1993) and Esponda and Pouzo (2016), though
these papers do not study optimal experimentation and do not reﬁne the Nash
equilibrium set. Finally, Dekel, Fudenberg, and Levine (1999), Fudenberg and
Kamada (2015), and Fudenberg and Kamada (2018) develop equilibrium re-
ﬁnements that combine the idea of equilibrium arising from learning with the
assumption that players know one another’s payoﬀfunctions and feedback
structures. These paper do no provide explicit learning models, but the im-
plicit models they have in mind would feature impatient learners who do little
or no experimentation.
2“Constructive,” as opposed to proofs that rule out all but one equilibrium using neces-
sary conditions and then appeal to an existence theorem for patiently stable steady states.
Constructive suﬃcient conditions allow us to characterize learning outcomes more precisely
in games where multiple equilibria satisfy the necessary conditions, such as Example 1.
5


## Page 7


2
Two Equilibrium Reﬁnements for Signaling
Games
2.1
Signaling Game Notation
A signaling game has two players, a sender (“she,” player 1) and a receiver
(“he,” player 2). At the start of the game, the sender learns her type θ ∈Θ,
but the receiver only knows the sender’s type distribution3 λ ∈∆(Θ). Next,
the sender chooses a signal s ∈S. The receiver observes s and chooses an
action a ∈A in response. We assume that Θ, S, A are ﬁnite and that λ(θ) > 0
for all θ.
The players’ payoﬀs depend on the triple (θ, s, a). Let u1 : Θ × S × A →R
and u2 : Θ × S × A →R denote the utility functions of the sender and the
receiver, respectively.
For P ⊆∆(Θ), we have
BR(P, s) :=
[
p∈P
 
arg max
a∈A
Eθ∼p [u2(θ, s, a)]
!
as the set of best responses to s supported by some belief in P.
Letting
P = ∆(Θ), the set ABR
s
:= BR(∆(Θ), s) ⊆A contains the receiver actions
that best respond to some belief about the sender’s type after s.
We say
that actions in ABR
s
are conditionally undominated after signal s, and that
actions in A\ABR
s
are conditionally dominated after signal s. We denote by
Π•
2 := ×s∈S∆(ABR
s ) the rational receiver strategies; these are the strategies that
assign probability 0 to conditionally dominated actions.4 The rational receiver
strategies form a subset of Π2 := ×s∈S∆(A), the set of all receiver strategies. A
sender who knows the receiver’s payoﬀfunction expects the receiver to choose
a strategy in Π•
2.
A sender strategy π1 = (π1(· | θ))θ∈Θ ∈Π1 speciﬁes a distribution on S for
each type, π1(· | θ) ∈∆(S). For a given π1, signal s is‘ oﬀthe path of play if
3The notation ∆(X) means the set of all probability distributions on X.
4Throughout we adopt the terminology “strategies” to mean behavior strategies, not
mixed strategies.
6


## Page 8


it has probability 0, i.e. π1(s | θ) = 0 for all θ. Let
Sθ :=
[
π2∈Π2
 
arg max
s∈S
u1(θ, s, π2(· | s))
!
.
be the set of signals that best respond to some (not necessarily rational) re-
ceiver strategy for type θ.
Signals in S\Sθ are dominated for type θ, and
Π•
1 := ×θ∆(Sθ) denotes the rational sender strategies where no type ever
sends a dominated signal. We also write Θs for the types θ for whom s ∈S is
not dominated. A receiver who knows the sender’s payoﬀfunction expects the
sender to choose a strategy in Π•
1 and only expects types in Θs to play signal
s.
2.2
Rationality-Compatible Equilibria
We now introduce rationality-compatible equilibrium (RCE) and uniform rationality-
compatible equilibrium (uRCE), two reﬁnements of Nash equilibrium in sig-
naling games.
In Section 4, we develop a steady-state learning model where populations
of senders and receivers, initially uncertain as to the aggregate play of the op-
ponent population, undergo random anonymous matching each period to play
the signaling game. We study the steady states when agents are patient and
long lived, which we term rationally patiently stable. Under some strictness
assumptions, we show that only RCE can be rationally patiently stable (The-
orem 1) and that every uRCE is “path-equivalent”5 to a rationally patiently
stable proﬁle (Theorem 2). Thus we provide a learning foundation for these
solution concepts.
Our learning foundation will assume that agents know other agents’ utility
functions and know that other agents are rational in the sense of playing
strategies that maximize the corresponding expected utilities. We will not
however iteratively assume higher orders of payoﬀknowledge and rationality,
so that we model “rationality” as opposed to “rationalizability.”6
5Roughly speaking, this means equivalent up to changing some of the receiver’s oﬀ-path
behavior, see Subsection 3.3.
6It is straightforward to extend our results about RCE to priors that reﬂect higher-
7


## Page 9


In the learning model, this implies senders’ uncertainty about receivers’
play is always supported on Π•
2 instead of Π2, and similarly receivers’ uncer-
tainty about senders’ play is supported on Π•
1 instead of Π1. In Section 2.3,
we discuss heuristically how our solution concepts capture some of the ways in
which payoﬀinformation aﬀects learning outcomes. This discussion will later
be formalized in the context of the learning model we develop in Section 4.
Deﬁnition 1. Signal s is more rationally-compatible with θ
′ than θ
′′, written
as θ
′ ≿s θ
′′, if for every π2 ∈Π•
2 such that
u1(θ
′′, s, π2(·|s)) ≥max
s′̸=s u1(θ
′′, s
′, π2(·|s
′)),
we have
u1(θ
′, s, π2(·|s)) > max
s′̸=s u1(θ
′, s
′, π2(·|s
′)).
In words, θ
′ ≿s θ
′′ means whenever s is a weak best response for θ
′′ against
some rational receiver behavior strategy π2, it is a strict best response for θ
′
against π2.
The next proposition shows that ≿s is transitive and “almost” asymmetric.
A signal s is rationally strictly dominant for θ if it is a strict best response
against any rational receiver strategy, π2 ∈Π•
2. A signal s is rationally strictly
dominated for θ if it is not a weak best response against any rational receiver
strategy.
Proposition 1. We have
1. ≿s′ is transitive.
2. Except when s
′ is either rationally strictly dominant for both θ
′ and θ
′′
or rationally strictly dominated for both θ
′ and θ
′′, θ
′ ≿s′ θ
′′ implies
θ
′′ ̸≿s′ θ
′.
order knowledge of the rationality and payoﬀfunctions of the other player. The resulting
equilibrium reﬁnement always exists, and like RCE is implied by universal divinity. We
do not include it here both because we are unaware of any interesting examples where the
additional power has bite, and because we are skeptical about the hypothesis of iterated
rationality.
8


## Page 10


The Appendix provides proofs for all of our results except where otherwise
noted.
We require two auxiliary deﬁnitions before deﬁning RCE.
Deﬁnition 2. For any two types θ
′, θ
′′, let Pθ′▷θ′′ be the set of beliefs where
the odds ratio of θ
′ to θ
′′ exceeds their prior odds ratio, that is7
Pθ′▷θ′′ :=
(
p ∈∆(Θ) : p(θ
′′)
p(θ
′) ≤λ(θ
′′)
λ(θ
′)
)
.
(1)
Note that if π1(s|θ
′) ≥π1(s|θ
′′), π1(s|θ
′) > 0, and the receiver updates
beliefs using π1, then the receiver’s posterior belief about the sender’s type
after observing s falls in the set Pθ′▷θ′′. In particular, in any Bayesian Nash
equilibrium, the receiver’s on-path belief falls in Pθ′▷θ′′ after any on-path signal
s with θ
′ ≿s θ
′′.
We now introduce some additional deﬁnitions to let us investigate the im-
plications of the agents’ knowledge of their opponent’s payoﬀfunction. For a
strategy proﬁle π∗, let Eπ∗[u1 | θ] denote type θ’s expected payoﬀunder π∗.
Deﬁnition 3. For any strategy proﬁle π∗, let
eJ(s, π∗) :=
(
θ ∈Θ : max
a∈ABR
s
u1(θ, s, a) ≥Eπ∗[u1 | θ]
)
.
This is the set of types for which some best response to signal s is at least
as good as their payoﬀunder π∗. For all other types, the signal s is equilibrium
dominated in the sense of Cho and Kreps (1987).
Deﬁnition 4. The set of rationality-compatible beliefs for the receiver at strat-
egy proﬁle π∗,
 ˜P(s, π∗)

s , is deﬁned as follows:









˜P(s, π∗) := ∆( eJ(s, π∗)) T


T
(θ′,θ′′) s.t. θ′≿sθ′′ Pθ′▷θ′′


if eJ(s, π∗) ̸= ∅
˜P(s, π∗) := ∆(Θs)
if eJ(s, π∗) = ∅.
7With the convention 0
0 := 0.
9


## Page 11


The main idea behind the rationality-compatible beliefs is that the re-
ceiver’s posterior likelihood ratio for types θ
′ and θ
′′ dominates the prior like-
lihood ratio whenever θ
′ ≿s θ
′′. A second feature involves equilibrium domi-
nance. Note that eP assigns probability 0 to equilibrium-dominated types; this
is similar to the belief restriction of the Intuitive Criterion. Note that this def-
inition imposes no belief restrictions based on θ
′ ≿s θ
′′ when s is equilibrium
dominated for every type. As we illustrate in Example 3, the receiver needs
not learn the rational compatibility relation when equilibrium dominance leads
to steady states where no type ever experiments with a certain signal.
Deﬁnition 5. Strategy proﬁle π∗is a rationality-compatible equilibrium (RCE)
if it is a Nash equilibrium and π∗
2(· | s) ∈∆(BR( ˜P(s, π∗), s)) for every s.
RCE requires that the receiver only plays best responses to rationality-
compatible beliefs after each signal. This solution concept allows for the pos-
sibility that after oﬀ-path signals the receiver’s strategy π∗
2(· | s) may not
correspond to a single belief about the sender’s type. We show below that
rationally patiently stable proﬁles exist and that every rationally patiently
stable proﬁle is a RCE, so that RCE exist as well.
Theorem 1 shows that RCE is a necessary condition for a strategy proﬁle
where receivers have strict preferences after each on-path signal to be rationally
patiently stable. Intuitively, this result holds because the optimal experimen-
tation behavior of the senders respects the compatibility order, and because,
since players eventually learn the equilibrium path, types will not experiment
much with signals that are equilibrium dominated. As we show in Section 3,
RCE rules out the implausible equilibria in a number of games, but is weaker
than some past signaling game reﬁnements in the literature. However, RCE
is only a necessary condition for rational patient stability, which leaves open
the question of whether patient learning has additional implications. For this
reason, we now deﬁne uRCE, a subset of RCE (up to path-equivalence). As
we show below, uRCE is a suﬃcient condition for rational patient stability.
Deﬁnition 6. The set of uniformly rationality-compatible beliefs for the re-
10


## Page 12


ceiver is
 ˆP(s)

s where
ˆP(s) := ∆(Θs)
\



\
(θ′,θ′′) s.t. θ′≿sθ′′
Pθ′▷θ′′


.
Note that
 ˆP(s)

s makes no reference to a particular strategy proﬁle, unlike
 ˜P(s, π∗)

s.
Since ∆(Θs) contains types for whom s is undominated and
eJ(s, π∗) contains types for whom s is equilibrium-undominated (relative to
the proﬁle π∗), we have ˜P(s, π∗) ⊆ˆP(s) whenever eJ(s, π∗) ̸= ∅.
Deﬁnition 7. A Nash equilibrium strategy proﬁle π∗is called a uniform
rationality-compatible equilibrium (uRCE) if for all θ, all oﬀ-path signals s
and all a ∈BR( ˆP(s), s), we have Eπ∗[u1 | θ] ≥u1(θ, s, a).
The “uniformity” in uniform RCE comes from the requirement that every
best response to every belief in ˆP(s) deters every type from deviating to the
oﬀ-path s. By contrast, a RCE is a Nash equilibrium where some best response
to ˜P(s, π∗) deters every type from deviating to s. Unlike with RCE, uRCE
need not exist (see Example 4).
As the names imply, uRCE is a stronger solution concept than RCE, up to
path-equivalence.
Proposition 2. Every uRCE is path-equivalent to an RCE.
2.3
Examples
In this subsection, we show how to apply RCE and uRCE in speciﬁc games,
and compare them to the solution concepts from Fudenberg and He (2018),
which are based on necessary conditions for patient stability with full-support
priors.
The following example illustrates that uRCE is a strict subset of RCE in
some games.
Example 1. Suppose a worker has either high ability (θH) or low ability (θL).
She chooses between three levels of higher education: None (N), College (C),
or Ph.D. (D). An employer observes the worker’s education level and pays
11


## Page 13


a wage, a ∈{low, med, high}. The worker’s utility function is separable
between wage and (ability, education) pair, with u1(θ, s, a) = z(a) + v(θ, s)
where z(low) = 0, z(med) = 6, z(high) = 9 and v(θH, N) = 0, v(θL, N) = 0,
v(θH, C) = 2, v(θL, C) = 1, v(θH, D) = −2, v(θL, D) = −4. (With this payoﬀ
function, going to college has a consumption value while getting a Ph.D. is
costly.) The employer’s payoﬀs reﬂect a desire to pay a wage corresponding
to the worker’s ability and increased productivity with education, given in the
tables below.
N
low
med
high
θH
0,-2
6,0
9,1
θL
0,1
6,0
9,-2
C
low
med
high
θH
2,-1
8,1
11,2
θL
1,2
7,1
10,-1
D
low
med
high
θH
-2,0
4,2
7,3
θL
-4,3
2,2
5,0
No education level is dominated for either type and no wage is conditionally
dominated after any signal. Since v(θH, ·) −v(θL, ·) is maximized at D, it is
simple to verify that θH ≿D θL. Similarly, θL ≿N θH. There is no compatibility
relation at signal C.
When the prior is λ(θH) = 0.5, the strategy proﬁle where the employer al-
ways pays a medium wage and both types of worker choose C is a uRCE. This is
because ˆP(N) contains only those beliefs with p(θH) ≤0.5, so BR( ˆP(N), N) =
{low, med}. Both of these wages deter every type from deviating to N. At
the same time, no type wants to deviate to D, even if she gets paid the best
wage.
On the other hand, the equilibrium π∗where the employer pays low wages
for N and C, a medium wage for D, and both types choose D is an RCE
but not a uRCE. The belief that puts probability 1 on the worker being θL
belongs to ˜P(N, π∗) and ˜P(C, π∗) and induces the employer to choose low
wage. However, medium salary is a best response to λ ∈ˆP(N) and medium
wage would tempt type θL to deviate to N.
♦
In the learning model of Fudenberg and He (2018), agents do not know
others’ utility functions and have full-support prior beliefs about others’ play.
12


## Page 14


That paper’s compatibility criterion (CC) is based on a family of binary rela-
tions on types (one for each signal s) that are less complete than the rational
compatibility relations, because the CC requires the condition that “whenever
s is a weak best response for θ
′′, it is also a strict best response for θ
′” for
all π2 ∈Π2 instead of only for π2 ∈Π•
2. Hence, RCE is always at least as
restrictive as the CC, and RCE can eliminate some equilibria that the CC
allows.
Example 2. Consider a game where the sender has type distribution λ(θstrong) =
0.9, λ(θweak) = 0.1 and chooses between two signals In or Out. The game ends
with payoﬀs (0,0) if the sender chooses Out. If the sender chooses In, the re-
ceiver then chooses Up, Down, or X. Up is the receiver’s optimal response
if the sender is more likely to be θstrong, Down is optimal when the sender is
more likely to be θweak, and X is never optimal.8 This game has two sequential
equilibrium outcomes: one involving both types choosing Out, and another
where both types go In and the receiver responds with Up.
The sequential equilibrium outcome Out satisﬁes the CC, because the
compatibility relation of Fudenberg and He (2018) does not rank the two types
8This is a modiﬁed version of Cho and Kreps (1987)’s “beer-quiche game,” where an
outside option with certain payoﬀs (Out) replaces the Quiche signal. The responses Up
and Down correspond to Not Fight and Fight in the beer-quiche game, while X is a
conditionally dominated response for the receiver following In. Also, while our deﬁnition
of signaling games requires that the receiver has the same action set after every signal, this
situation is clearly equivalent to one where the receiver chooses Up, Down, or X after Out,
but all of these choices lead to the payoﬀs (0,0).
13


## Page 15


after signal In. (For example, if π2(Down | In) = 2/3 and π2(X | In) = 1/3,
θweak ﬁnds In optimal but θstrong does not.)
However, since the stronger rational compatibility relation ranks θstrong ≿In
θweak, the unique RCE is the equilibrium where both types go In, which implies
that this is also the unique rationally patiently stable outcome.9
♦
The previous example shows how RCE can exclude some equilibria that
satisfy the CC. The next one cautions that RCE may allow more equilibrium
proﬁles than the strong compatibility criterion (strong CC), which Fudenberg
and He (2018) show to be another necessary condition for patient stability
(with full-support priors). The strong CC requires the receiver to put zero
probability after signal s on sender types for whom s is equilibrium dominated,
but unlike in Deﬁnition 3, in the strong CC equilibrium dominance is computed
by comparing the type’s equilibrium payoﬀto that of any response to the
unsent signal, including responses that are conditionally dominated.
Example 3. Consider a game with two sender types, θ1 and θ2, equally likely,
and two possible signals, L or R. Payoﬀs are given in the tables below.
signal: L
action: a1
action: a2
action: a3
type: θ1
−2, 0
2, 2
2, 1
type: θ2
−2, 1
2, 0
2, -1
signal: R
action: a1
action: a2
action: a3
type: θ1
5, -1
-3, 2
-4, 0
type: θ2
-2, -1
1, 0
0, 1
Action a1 is conditionally dominated for the receiver after signal R. It
is easy to see that in every perfect Bayesian equilibrium π∗, we must have
π∗
1(L | θ1) = π∗
1(L | θ2) = 1, π∗
2(a2 | L) = 1, and that π∗
2(· | R) must be
supported on ABR
R = {a2, a3}. This means the oﬀ-path signal R is equilibrium
dominated for every type in π∗(when they know the receiver’s payoﬀs), i.e.
˜J(R, π∗) = ∅. So, ˜P(R, π∗) = ∆(ΘR) = ∆(Θ) and RCE permits the receiver
9RCE requires that that p(θstrong | In) ≥λ(θstrong) = 0.9, which implies that π2(Up |
In) = 1 in every RCE. Therefore both types must be playing In in RCE.
14


## Page 16


to play either a2 or a3 after R. (This is despite the fact that θ2 is more rationally
compatible with R than θ1 is. As we discussed after Deﬁnition 4, RCE does
not restrict the receiver’s belief based on rational type compatibility after an
oﬀ-path signal that is equilibrium dominated for every type.)
By contrast, the strong CC from Fudenberg and He (2018) requires that
the receiver plays a2 after R: the equilibrium payoﬀof both types is 2. Type
θ1 has maxa∈A u1(θ1, R, a) ≥2 but this is not true for θ2. So the strong CC
requires the receiver to put probability 1 on θ1 after R, which pins down the
receiver’s oﬀ-path play.
We will show in Section 7 that when learners have payoﬀinformation, there
is a rationally patiently stable proﬁle where the receivers play a2 after R and
another rationally patiently stable proﬁle where the receivers respond to R
with a3. However, we will also show that without payoﬀinformation, patient
stability requires that the receivers play a2 after R.
♦
Finally, we show that uRCE may not exist.
Example 4.
In Cho and Kreps (1987)’s “beer-quiche game,” it is easy to verify that
the pooling equilibrium on Beer is the unique RCE. This equilibrium is not
a uRCE because ˆP(Quiche) = {p : p(θweak) ≥0.1}, so NotFight is a best
response to a belief in ˆP(Quiche) that does not deter θweak from deviating.
So the game does not have any uRCE. Moreover, it is easy to see that the
same conclusions hold with slightly diﬀerent assignments of payoﬀs to terminal
nodes, so that the non-existence result applies to an open set of games.
♦
15


## Page 17


3
Comparison to Other Equilibrium Reﬁne-
ments
This section compares RCE to other equilibrium reﬁnement concepts in the
literature.
3.1
Iterated dominance
We ﬁrst relate RCE to a form of iterated dominance in the ex-ante strategic
form of the game, where the sender chooses a signal π1 as function of her
type. We show that every sender strategy that speciﬁes playing signal s as a
less compatible type θ
′′ but not as a more compatible type θ
′ will be removed
by iterated deletion. The idea is that such a strategy is never a weak best
response to any receiver strategy in Π•
2: if the less compatible θ
′′ does not
have a proﬁtable deviation, then the more compatible type strictly prefers
deviating to s.
Proposition 3. Suppose θ
′ ≿s θ
′′. Then any ex-ante strategy of the sender
π1 with π1(s|θ
′′) > 0 but π1(s|θ
′) < 1 is removed by strict dominance once the
receiver is restricted to using strategies in Π•
2.
3.2
The Intuitive Criterion
We next relate RCE to the Intuitive Criterion.
Proposition 4. Every RCE satisﬁes the Intuitive Criterion.
The next example shows that the set of RCE is strictly smaller than the set
of equilibria that pass the Intuitive Criterion.10 The idea is that the Intuitive
Criterion does not impose any restriction on the relative likelihood of two types
after a signal that is not equilibrium dominated for either of them, but RCE
can.
10Fudenberg and He (2018)’s compatibility criterion is not always more stringent than
the Intuitive Criterion, but the strong compatibility criterion studied in the same paper is.
16


## Page 18


Example 5. Consider a signaling game where the prior probabilities of the
two types are λ(θ
′) = 3/4 and λ(θ
′′) = 1/4, and the payoﬀs are:
signal: s
′
action: a
′
action: a
′′
type: θ
′
4, 1
0, 0
type: θ
′′
6, 0
2, 1
signal: s
′′
action: a
′
action: a
′′
type: θ
′
7, 1
3, 0
type: θ
′′
7, 0
3, 1
Against any receiver strategy, the two types θ
′ and θ
′′ get the same payoﬀs
from s
′′, but θ
′′ gets strictly higher payoﬀs than θ
′ from s
′. So, θ
′ ≿s′′ θ
′′.
Consider now the Nash equilibrium in which the types pool on s
′, i.e.
π∗
1(s
′|θ
′) = π∗
1(s
′|θ
′′) = 1, π∗
2(a
′|s
′) = 1, and π∗
2(a
′′|s
′′) = 1. It passes the
Intuitive Criterion since the oﬀ-path signal s
′′ is not equilibrium dominated
for either type. On the other hand, RCE requires that every action played with
positive probability in π∗
2(·|s
′′) best responds to some belief p about sender’s
type satisfying p(θ
′′)
p(θ′) ≤λ(θ
′′)
λ(θ′) = 1
3. But action a
′′ does not best respond to any
such belief, so π∗is not an RCE.
♦
3.3
Divine Equilibrium
Next, we compare divine equilibrium with RCE and uRCE. For a strategy
proﬁle π∗, let
D(θ, s; π∗) := {α ∈MBR(s) s.t. Eπ∗[u1 | θ] < u1(θ, s, α)}
be the subset of mixed best responses11 to s that would make type θ strictly
prefer deviating from the strategy π∗
1(· | θ). Similarly let
D◦(θ, s; π∗) := {α ∈MBR(s) s.t. Eπ∗[u1 | θ] = u1(θ, s, α)}
be the set of mixed best responses that would make θ indiﬀerent to deviating.
Intuitively, RCE and uRCE are “close” to divine equilibrium because both
the deﬁnition of ≿s and the divine equilibrium belief restriction involve a
11To
be
precise,
MBR(p, s)
:=
arg max
α∈∆(A)
(Eθ∼p[u2(θ, s, α)])
and
MBR(s)
:=
∪p∈∆(Θ)MBR(p, s).
17


## Page 19


condition of the form “any receiver play that makes one type weakly prefer
s must make another type strictly prefer s.” Propositions 5 and 6 make this
relationship precise.
Proposition 5.
1. If π∗is a Nash equilibrium where s
′ is oﬀ-path, and
θ
′ ≿s′ θ
′′, then D(θ
′′, s
′; π∗) ∪D◦(θ
′′, s
′; π∗) ⊆D(θ
′, s
′; π∗).
2. Every divine equilibrium is a RCE.
However, the converse is not true, as the following example illustrates.
Example 6. Consider the following signaling game with two types and three
signals, with prior λ(θ1) = 2/3.
s
′
a
′
a
′′
θ
′
0, 1
-1, 0
θ
′′
0, 0
-1, 1
s
′′
a
′
a
′′
θ
′
2, 1
-1, 0
θ
′′
1, 0
-1, 1
s
′′′
a
′
a
′′
θ
′
5, 0
-3, 1
θ
′′
0, 1
-2, 0
We check that the following is a pure-strategy RCE: π1(s
′|θ
′) = π1(s
′|θ
′′) =
1, π2(a
′|s
′) = 1, π2(a
′′|s
′′) = 1, π2(a
′′|s
′′′) = 1. Evidently π is a Nash equilibrium
and no type is equilibrium-dominated at any oﬀ-path signal. We now check
that we do not have θ
′ ≿s′′ θ
′′ or θ
′′ ≿s′′′ θ
′. Observe that against the receiver
strategy ˜π2(a
′|s) = 1
2 for every s, s
′′ is strictly optimal for θ
′′ but s
′′′ is strictly
optimal for θ
′, so θ
′ ̸≿s′′ θ
′′. And for the receiver strategy ˆπ2(a
′|s) = 1 for every
s, s
′′′ is strictly optimal for θ
′ but s
′′ is strictly optimal for θ
′′, so θ
′′ ̸≿s′′′ θ
′.
This shows the strategy proﬁle is an RCE.
However, D(θ
′′, s
′′; π) ∪D◦(θ
′′, s
′′; π) is the set of distributions on {a
′, a
′′}
that put at least weight 0.5 on a
′. Any such distribution is in D(θ
′, s
′′; π). So
in every divine equilibrium, the receiver plays a best response to a belief that
puts weight no less than 2/3 on θ
′ after signal s
′′, which can only be a
′.12
♦
This example illustrates one diﬀerence between divine equilibrium and
RCE: Under divine equilibrium, the beliefs after signal s
′′ only depend on
12As noted by Van Damme (1987), it may seem more natural to replace the set α ∈
MBR(m) in the deﬁnitions of D and D0 with the larger set α ∈co(BR(s)), which leads to
the weaker equilibrium reﬁnement that Sobel, Stole, and Zapater (1990) call “co-divinity”.
This example also shows that RCE need not be co-divine.
18


## Page 20


the comparison between the payoﬀs to s
′′ with those of the equilibrium signal
s
′, while the compatibility criterion also considers the payoﬀs to a third signal
s
′′′. In the learning model, this corresponds to the possibility that θ
′ chooses
to experiment with s
′′′ at beliefs that induce θ
′′ to experiment with s
′′.
RCE diﬀers from divine equilibrium in another way, as divine equilibrium
involves an iterative application of a belief restriction.
The next example
illustrates this diﬀerence13.
Example 7. There are three types, θ
′, θ
′′, θ
′′′, all equally likely. The signal
space is S = {s
′, s
′′}, and the set of receiver actions is A = {a1, a2, a3, a4}.
When any sender type chooses the signal s
′, all parties get a payoﬀof 0 re-
gardless of the receiver’s action. When the sender chooses s
′′, the payoﬀs are
determined by the following matrix.
s
′′
a1
a2
a3
a4
θ
′
1, 0.9
-1, 0
-2, 0
-7, 0
θ
′′
5, 0
3, 1
-1, 0
-5, 0.8
θ
′′′
-3, 0
5, 0
1, 1.7
-3, 0.8
Consider the pure strategy proﬁle π∗
1(s
′|θ) = 1 for all θ ∈Θ and π∗
2(a4|s) =
1 for all s ∈S. Since θ
′′ gains more from deviating to s
′′ than θ
′ does, applying
the divine belief restriction for the oﬀ-path signal s
′′ eliminates the action a1,
since it is not a best response to any belief p ∈∆(Θ) with p(θ
′′) ≥p(θ
′).
But after action a1 is deleted for the receiver after signal s
′′, type θ
′′′ now
gains more from deviating to s
′′ than θ
′′ does. So, applying the divine belief
restriction again eliminates actions a2 and a4, since it is not a best response
against any p ∈∆(Θ) with p(θ
′) = 0 (for now s
′′ is equilibrium dominated for
θ
′) and p(θ
′′′) ≥p(θ
′′). So π∗is not a divine equilibrium.
On the other hand, no type is equilibrium dominated at s
′′ and the only
rational compatibility order is θ
′′ ≿s′′ θ
′. But a4 is a best response against
the belief p(θ
′) = 0, p(θ
′′) = 0.6, p(θ
′′′) = 0.4, which belongs to the set
∆(Θs′′) T Pθ′′▷θ′. So π∗is an RCE.
♦
Finally, we show that every uRCE is path-equivalent to an equilibrium that
is not ruled out by the “NWBR in signaling games” test (Banks and Sobel,
13We thank Joel Sobel for this example.
19


## Page 21


1987; Cho and Kreps, 1987),14 which comes from iterative applications of the
following pruning procedure: after signal s the receiver is required to put 0
probability on those types θ such that
D◦(θ, s; π∗) ⊆∪θ′̸=θD(θ
′, s; π∗).
If this would delete every type, then the procedure instead puts no restriction
on receiver’s beliefs and no type is deleted.
By “path-equivalent” we mean that by modifying some of the receiver’s
oﬀ-path responses, but without altering the sender’s strategy or the receiver’s
on-path responses, we can change the uRCE into another uRCE that passes the
NWBR test. Since every equilibrium passing the NWBR test is universally di-
vine15 (Cho and Kreps, 1987), this implies that every uRCE is path-equivalent
to a universally divine equilibrium.
Proposition 6. Every uRCE is path-equivalent to a uRCE that passes the
NWBR test.
Corollary 1. Every uRCE is path-equivalent to a universally divine equilib-
rium.
3.4
Summary
To summarize this subsection, we note that for strategy proﬁles that are on-
path strict for the receiver, we have the following inclusion relationships. The
ﬁrst inclusion should be understood as inclusion up to path-equivalence. We
use the symbol “⊊” to mean that the former solution set is always nested
within the latter one in every signaling game, and that there exist games
14This is closely related to, but not the same as, the NWBR property of Kohlberg and
Mertens (1986).
15Universal divinity is deﬁned as the iterative application of the following procedure: after
signal s the receiver is required to put 0 probability on those types θ such that
D◦(θ, s; π∗) ∪D(θ, s; π∗) ⊆∪θ′̸=θD(θ
′, s; π∗).
20


## Page 22


where the nesting relationship is strict.
uRCE ⊊universally divine ⊊divine ⊊RCE ⊊Intuitive Criterion ⊊Nash.
In interpreting these inclusions, it is important to remember that a univer-
sally divine equilibrium generically exists. In contrast, we showed in Example
4 that uRCE can fail to exist for an open set of signaling games.16
4
Steady-State Learning in Signaling Games
4.1
Random Matching and Aggregate Play
We study the same discrete-time steady-state learning model as Fudenberg
and He (2018) except for a diﬀerent restriction on the players’ prior beliefs
over other players’ strategies.
There is a continuum of agents in the society, with a unit mass of receivers
and λ(θ) mass of type θ senders. Each population is further stratiﬁed by age,
with a fraction (1−γ)·γt of each population age t for t = 0, 1, 2, ... At the end
of each period, each agent has probability 0 ≤γ < 1 of surviving into the next
period, increasing their age by 1. With complementary probability, the agent
dies. Each agent’s survival is independent of calendar time and independent
of the survival of other agents. At the start of the next period, (1 −γ) new
receivers and λ(θ)(1 −γ) new type θ senders are born into the society, thus
preserving population sizes and the age distribution.
Agents play the signaling game every period against a randomly matched
opponent. Each sender has probability (1 −γ)γt of matching with a receiver
of age t, while each receiver has probability λ(θ)(1 −γ)γt of matching with a
type θ sender of age t.
16That is, for an open set of payoﬀvectors at the terminal nodes of the game.
21


## Page 23


4.2
Learning by Individual Agents with PayoﬀKnowl-
edge
Each agent is born into a player role in the signaling game: either a receiver
or a type θ sender. Agents know their role, which is ﬁxed for life. The agents’
payoﬀeach period is determined by the outcome of the signaling game they
played, which consists of the sender’s type, the signal sent, and the action
played in response. The agents observe this outcome, but the sender does not
observe how her matched receiver would have played had she sent a diﬀerent
signal.
In addition to only surviving to the next period with probability 0 ≤γ < 1,
agents discount17 future utility ﬂows by 0 ≤δ < 1 and seek to maximize
expected discounted utility. Letting ut represent the payoﬀt periods from
today, each agent’s objective function is E[P∞
t=0(γδ)t · ut]. (Deﬁne 00 := 1, so
that a myopic agent just maximizes current period’s expected payoﬀin every
period.)
Agents believe they face a ﬁxed but unknown distribution of opponents’
aggregate play, updating their beliefs at the end of every period based on
the outcome in their own game. Formally, each sender is born with a prior
density function over receivers’ behavior strategies, g1 : Π2 →R+ . Similarly,
each receiver is born with a prior density over the senders’ behavior strategies,
g2 : Π1 →R+.
We denote the marginal distribution of g1 on signal s as
g(s)
1
: ∆(A) →R+, so that g(s)
1 (π2(·|s)) is the density of the new senders’ prior
over how receivers respond to signal s. Similarly, we denote the θ marginal of
g2 as g(θ)
2
: ∆(S) →R+, so that g(θ)
2 (π1(·|θ)) is the new receivers’ prior density
over the signal choice of type θ.
We now state a regularity assumption on agents’ priors that will be main-
tained throughout.
Deﬁnition 8. A prior g = (g1, g2) is regular if
17We separately consider survival probability and patience so that we may consider agents
who are impatient relative to their expected lifespan. Such agents experiment early in their
life cycle, but spend most of their life myopically best responding to their beliefs, which
makes our analysis more tractable.
22


## Page 24


(a). [independence] g1(π2) = Q
s∈Sg(s)
1 (π2(·|s)) and g2(π1) = Q
θ∈Θg(θ)
2 (π1(·|θ)).
(b). [payoﬀknowledge] g1 puts probability 1 on Π•
2 and g2 puts probability 1
on Π•
1.
(c). [g1 non-doctrinaire] g1 is continuous and strictly positive on the interior
of Π•
2.
(d). [g2 nice] For each type θ, there are positive constants

α(θ)
s

s∈S such that
π1(·|θ) 7→
g(θ)
2 (π1(·|θ))
Q
s∈S π1(s|θ)α(θ)
s
−1
is uniformly continuous and bounded away from zero on the relative
interior of Π•
θ, the set of rational behavior strategies of type θ.
This assumption bears the same name as the regularity assumption in Fu-
denberg and He (2018), and is identical except that agents now know others’
payoﬀs and others’ rationality. In the learning model, this payoﬀknowledge
translates into a restriction on the supports of the priors g1, g2, reﬂecting a
dogmatic belief that senders will never play dominated signals and receivers
will never play conditionally dominated actions. (These beliefs are correct in
the learning model.)
Even with payoﬀknowledge, the receiver’s prior can assign positive prob-
ability to ex-ante dominated sender strategies. For instance, in the signaling
game below,
23


## Page 25


the sender strategy π1(s
′′ | θ
′) = π1(s
′′ | θ
′′) = 1 belongs to the set Π•
1, and
so must belong to the support of any regular receiver prior. But, even though
s
′′ ∈Sθ′ and s
′′ ∈Sθ′′, the receiver strategies to which they respectively
best respond form disjoint sets, and π1 is ex-ante dominated because it is not
a best response to any single receiver strategy. It is nevertheless consistent
for a receiver who knows the sender’s payoﬀas a function of their type to
assign positive density to π1, because diﬀerent types of agents can choose best
responses to diﬀerent beliefs about receiver play.
4.3
History and Aggregate Play
Let Yθ[t] := (∪s∈S(s×ABR
s ))t represent the set of possible histories for a type θ
sender with age t. Note that a valid history encodes the signal that θ sent each
period and the (conditionally undominated) action that her opponent played
in response. Let Yθ := S∞
t=0 Yθ[t] be the set of all histories for type θ.
Similarly, write Y2[t] := (Θ × Sθ)t for the set of possible histories for a
receiver with age t. Each period, his history encodes the type of the matched
sender and the (undominated) signal observed. The union Y2 := S∞
t=0 Y2[t]
then stands for the set of all receiver histories.
The agents’ dynamic optimization problems discussed in Subsection 4.2
give rise to optimal policies18 σθ : Yθ →Sθ and σ2 : Y2 →×s(ABR
s ). Here,
σθ(yθ) is the signal that a type θ sender with history yθ would send the next
time she plays the signaling game. Analogously, σ2(y2) is the pure extensive-
form strategy that a receiver with history y2 would commit to next time he
plays the game.
In the learning model, each agent solves a (single-agent)
dynamic optimization problem, and chooses a deterministic optimal policy.
A state ψ of the learning model is a demographic description of how many
agents have each possible history. It can be viewed as a distribution
ψ ∈(×θ∈Θ∆(Yθ)) × ∆(Y2),
and its components are denoted by ψθ ∈∆(Yθ) and ψ2 ∈∆(Y2).
18For notational simplicity, we suppress the dependence of these optimal policies on the
eﬀective discount factor δγ and on the priors.
24


## Page 26


Since each state ψ is a distribution over histories and optimal policies map
histories to play, ψ induces a distribution over play (i.e., a rational behavior
strategy) in the signaling game σ(ψ) ∈Π•, given by
σθ(ψθ)(s) := ψθ {yθ ∈Yθ : σθ(yθ) = s}
and
σ2(ψ2)(a | s) := ψ2 {y2 ∈Y2 : σ2(y2)(s) = a} .
Here, σθ(ψθ) and σ2(ψ2) are the aggregate behaviors of the type θ and
receiver populations in state ψ, respectively. Note that the aggregate play of
a population can be stochastic even if the entire population uses the same
deterministic optimal policy, because diﬀerent senders will be matched with
diﬀerent receivers, and so diﬀerent agents on the same side will observe diﬀer-
ent histories and play diﬀerently.
Of particular interest are the steady states, to be deﬁned more precisely in
Section 5. Loosely speaking, a steady state induces a time-invariant distribu-
tion over how the signaling game is played in the society.
5
Aggregate Responses and Steady State
This section deﬁnes the notion of a steady state using the “aggregate re-
sponses” of one population to the distribution of play in the other. These
responses are deﬁned using the “one-period forward” maps that describe how
the agents’ policies induce a map from current distributions over histories to
what the distributions will be after the agents are matched and play the game
using the strategies their policies prescribe.
5.1
The Aggregate Sender Response
Fix the receivers’ aggregate play at π2 ∈Π•
2 and ﬁx an optimal policy σθ for
each type θ. The one-period-forward map for type θ, fθ, describes the distribu-
tion over histories that will prevail next period when the current distributions
25


## Page 27


over histories in the type-θ population is ψθ. The next deﬁnition speciﬁes the
probability that fθ[ψθ, π2] assigns to the history (yθ, (s, a)) ∈Yθ[t + 1], that is
to say a one-period concatenation of (s, a) onto the history yθ ∈Yθ[t].
Deﬁnition 9. The one-period-forward map for type θ, fθ : ∆(Yθ) × Π•
2 →
∆(Yθ) is
fθ[ψθ, π2](yθ, (s, a)) := ψθ(yθ) · γ · 1{σθ(yθ) = s} · π2(a | s)
and fθ(∅) := 1 −γ.
To interpret, of the ψθ(yθ) fraction of the type-θ population with history
yθ, a γ fraction survives into the next period. The survivors all choose σθ(yθ)
next period, which is met with response a with probability π2(a | σθ(yθ)).
Write f T
θ for the T-fold application of fθ on ∆(Yθ), holding ﬁxed some π2.
It is easy to show that limT→∞f T
θ (ψθ, π2) exists and is independent of the
initial ψθ. (This is because for any two states ψθ, ψ
′
θ, the two distributions
over histories f T
θ (ψθ, π2) and f T
θ (ψ
′
θ, π2) agree on all Yθ[t] for t < T. As T
grows large, the two resulting distributions must converge to each other since
the fraction of very old agents with very long histories is rare.) Denote this
limit as ˜ψπ2
θ . It is the distribution over type-θ history induced by the receivers’
aggregate play π2.
Deﬁnition 10. The aggregate sender response R1 : Π•
2 →Π•
1 is deﬁned by
R1[π2](s | θ) := ˜ψπ2
θ (yθ : σθ(yθ) = s)
That is, R1[π2](· | θ) describes the asymptotic aggregate play of the type-θ
population when the the aggregate play of the receiver population is ﬁxed at
π2 each period. Note that R1 maps into Π•
1 because no type ever wants to send
a dominated signal, even as an experiment, regardless of their beliefs about
the receiver’s response.
Technically, R1 depends on g1, δ, and γ, just like σθ does. When relevant,
we will make these dependencies clear by adding the appropriate parameters
as superscripts to R1, but we will mostly suppress them to lighten notation.
26


## Page 28


5.2
The Aggregate Receiver Response
We now turn to the receivers, who have a passive learning problem. They
always observe the sender’s type and signal at the end of each period, so their
optimal policy σ2 myopically best responds to the posterior belief at every
history y2.
Deﬁnition 11. The one-period-forward map for the receivers f2 : ∆(Y2) ×
Π•
1 →∆(Y2) is
f2[ψ2, π1](y2, (θ, s)) := ψ2(y2) · γ · λ(θ) · π1(s|θ)
and f2(∅) := 1 −γ.
As with the one-period-forward maps fθ for senders, f2[ψ2, π1] describes the
distribution over receiver histories next period starting with a society where
the distribution is ψ2 and the sender population’s aggregate play is π1. We
write ˜ψπ1
2 := limT→∞f T
2 (ψ2, π1) for the long-run distribution over Y2 induced
by ﬁxing sender population’s play at π1. (This limit is again independent of
the initial state ψ2.)
Deﬁnition 12. The aggregate receiver response R2 : Π•
1 →Π•
2 is
R2[π1](a | s) := ˜ψπ1
2 (y2 : σ2(y2)(s) = a)
5.3
Steady States and Rational Patient Stability
A steady-state strategy proﬁle is a pair of mutual aggregate replies, so it is
time-invariant under learning.19
Deﬁnition 13. π∗is a steady-state strategy proﬁle if Rg,δ,γ
1
(π∗
2) = π∗
1 and
Rg,δ,γ
2
(π∗
1) = π∗
2. Denote the set of all such strategy proﬁles as Π∗(g, δ, γ).
We now state two results about these steady states. We do not provide a
proof because they follow easily from analogous results in Fudenberg and He
(2018).
19We focus on the steady states of the learning system, and do not study convergence to
steady states.
27


## Page 29


First, steady-state proﬁles always exist.
Proposition 7. For any regular prior g and any 0 ≤δ, γ < 1, Π∗(g, δ, γ) is
non-empty and compact in the norm topology.
The rationally patiently stable strategy proﬁles correspond to the set
lim
δ→1 lim
γ→1 Π∗(g, δ, γ).
This order of limits was ﬁrst introduced in Fudenberg and Levine (1993).
It ensures agents spend most of their lifetime playing myopically instead of
experimenting, which is important for proving that rationally patiently stable
proﬁles are Nash equilibria.
Deﬁnition 14. For each 0 ≤δ < 1, a strategy proﬁle π∗is δ-stable under
g if there is a sequence γk →1 and an associated sequence of steady-state
strategy proﬁles π(k) ∈Π∗(g, δ, γk), such that π(k) →π∗.
Strategy proﬁle
π∗is rationally patiently stable under g if there is a sequence δk →1 and
an associated sequence of strategy proﬁles π(k) where each π(k) is δk-stable
under g and π(k) →π∗. Strategy proﬁle π∗is rationally patiently stable if it is
rationally patiently stable under some regular prior g.
Note that δ-stable proﬁles always exist, since the space of strategy proﬁles
is compact so we can always extract a convergent subsequence from a sequence
of steady-state strategy proﬁles π(k) ∈Π∗(g, δ, γk) with γk →1. For the same
reason, a rationally patiently stable proﬁle always exists.
Proposition 8. If strategy proﬁle π∗is rationally patiently stable, then it is a
Nash equilibrium.
Note that Propositions 7 and 8 apply even if all of the Nash equilibria
of the game are in mixed strategies; as noted above, the randomization here
arises from the random matching process.
28


## Page 30


6
Rational Patient Stability, PayoﬀKnowledge,
and Equilibrium Reﬁnements
In this section, we relate the equilibrium reﬁnements proposed in Section 2
to the steady-state learning model. We show that under certain strictness
assumptions, RCE is necessary for rational patient stability while uRCE is
suﬃcient for rational patient stability. We also discuss how payoﬀknowledge
matters for learning outcomes.
6.1
RCE Is Necessary for Rational Patient Stability
We show that any rationally patiently stable strategy proﬁle satisfying a strict-
ness assumption must be an RCE. The key lemma is analogous to Lemma 1
from Fudenberg and He (2018), so we will omit its proof.
Lemma 1. Suppose θ
′ ≿s θ
′′. Then for any regular prior g1, 0 ≤δ, γ < 1,
and any π2 ∈Π•
2, we have R1[π2](s | θ
′) ≥R1[π2](s | θ
′′).
This result says over their lifetimes, the relative frequencies with which
diﬀerent sender types experiment with signal s respect the rational compatible
order ≿s. This follows from the fact that sender types who are more compatible
with a signal will play it at least as often. The payoﬀknowledge embedded
in g1’s support implies that senders never experiment in the hopes of seeing
a response which is highly proﬁtable for the sender but dominated for the
receiver, such as the X action in Example 2 for θweak. This extra assumption
leads to a stronger result than Lemma 1 from Fudenberg and He (2018), which
is stated in terms of the less-complete compatibility order.
For a ﬁxed strategy proﬁle π and on-path signal s∗, let Eθ|π1,s∗[u2(θ, s∗, a)]
denote the receiver’s expected utility from responding to s∗with a, where the
expectation over the sender’s type θ is taken with respect to the posterior type
distribution after signal s∗given the sender’s strategy π1(· | θ).
Deﬁnition 15. A Nash equilibrium π∗is on-path strict for the receiver if for
every on-path signal s∗, π2(a∗| s∗) = 1 for some a∗∈A and Eθ|π1,s∗[u2(θ, s∗, a∗)] >
maxa̸=a∗Eθ|π1,s∗[u2(θ, s∗, a)].
29


## Page 31


We call this condition “on-path” strict for the receiver because we do not
make assumptions about the receiver’s incentives after oﬀ-path signals. For
generic payoﬀs, all pure-strategy equilibria will be on-path strict for the re-
ceiver.
Theorem 1. Every strategy proﬁle that is rationally patiently stable and on-
path strict for the receiver is an RCE.
RCE rules out two kinds of receiver beliefs after signal s: those that assign
non-zero probability to equilibrium-dominated sender types, and those that
violate the rational compatibility order. The restriction on equilibrium dom-
inated types uses the assumption that the receiver has a strict best response
to each on-path signal to put a lower bound on how slowly aggregate receiver
play at on-path signals converges to its limit.20 The fact that the receiver be-
liefs respect the rational compatibility order comes from Lemma 1, which uses
our assumptions about prior g to derive restrictions on the aggregate sender
response R1, and show that these are reﬂected in the aggregate receiver re-
sponse. The proof of Theorem 1 closely follows the the analogous proof in
Fudenberg and He (2018) and is omitted.
6.2
Quasi-Strict uRCE is Suﬃcient for Rational Patient
Stability
We now prove our main result: as a partial converse to Theorem 1, we show
that under additional strictness conditions, every uRCE is path-equivalent to
a rationally patiently stable strategy proﬁle.
Deﬁnition 16. A quasi-strict uRCE π∗is a uRCE that is on-path strict for
the receiver, strict for the sender (that is, there exists an equilibrium signal
s∗for each type θ with u1(θ, s∗, π∗
2(·|s∗)) > maxs̸=s∗u1(θ, s, π∗
2(·|s)), so every
type strictly prefers its equilibrium signal to any other), and satisﬁes Eπ∗[u1 |
θ] > u1(θ, s
′, a) for all θ, all oﬀ-path signals s
′ and all a ∈BR( ˆP(s
′), s
′).
20If the receiver mixes after some equilibrium signal s for type θ, then our techniques for
showing that θ does not experiment very much with equilibrium dominated signals do not
go through, but we do not have a counterexample.
30


## Page 32


The last condition in the deﬁnition of quasi-strictness requires that every
best response to ˆP(s
′) strictly deters every type from deviating to s
′, whenever
s
′ is oﬀ-path. Every uRCE satisﬁes the weaker version of this condition where
“strictly deters” is replaced with “weakly deters.”
Theorem 2. If π∗is a quasi-strict uRCE, then it is path-equivalent to a ra-
tionally patiently stable strategy proﬁle.
Theorem 2 provides a constructive argument for an equilibrium being ratio-
nally patiently stable in signaling games with multiple RCE, such as Example
1. It follows from three lemmas on R1 and R2 that are stated and proved in
the rest of this subsection. Indeed, the theorem remains valid in any modiﬁed
learning model where R1 and R2 satisfy the conclusions of these lemmas.
Recall that Example 4 showed a signaling game with a unique RCE that is
not a uRCE. As noted before, a rationally patiently stable proﬁle always exists.
By Theorem 1, the unique RCE of the game must be rationally patiently stable.
This shows uRCE is not a necessary condition for rational patient stability.
6.2.1
R1 under a conﬁdent prior
The ﬁrst lemma shows that under a suitable prior, the aggregate sender re-
sponse of the dynamic learning model approximates the sender’s static best
response function when applied to certain receiver strategies, namely strategies
that are “close” to one inducing a unique optimal signal for each sender type.
The precise meaning of “close” that we use treats on- and oﬀ-path responses
diﬀerently, so it requires some auxiliary deﬁnitions.
Deﬁnition 17. Let π∗be a strategy proﬁle where every type plays a pure
strategy and the receiver plays a pure action after each on-path signal. Say π∗
induces a unique optimal signal for each sender type if
Eπ∗[u1 | θ] > max
s̸=π∗
1(θ) u1(θ, s, π∗
2(·|s))
for every type θ.
Starting with a strategy proﬁle π∗that induces a unique optimal signal for
each sender type, deﬁne for each oﬀ-path s in π∗the set of receiver actions
31


## Page 33


˜A(s) := {a : Eπ∗[u1 | θ] > u1(θ, s, a) ∀θ} that strictly deter every type from
deviation. Because π∗
2 induces a unique optimal signal, each ˜A(s) must contain
at least one element in the support of π∗
2(·|s), but could also contain other
actions. It is clear that if π∗
2 were modiﬁed oﬀ-path by changing each π∗
2(·|s)
to be an arbitrary mixture over ˜A(s), then the resulting strategy proﬁle would
continue to induce (the same) unique optimal signal for each sender type.
For π∗that induces a unique optimal signal for each sender type, write
Bon
2 (π∗, ϵ) for the elements of Π•
2 no more than ϵ away from π∗
2 at the on-path
signals in π∗
1, that is
Bon
2 (π∗, ϵ) := {π2 ∈Π•
2 : |π2(a|s) −π∗
2(a|s)| ≤ϵ, ∀a, on-path s in π∗} .
Similarly, deﬁne Boﬀ
2 (π∗, ϵ) as the elements of Π•
2 putting no more than ϵ
probability on actions outside of ˜A(s) after each oﬀ-path s, where ˜A(s) is the
set of actions that would deter every type from deviating to s, as above.
Boﬀ
2 (π∗, ϵ) :=
n
π2 ∈Π•
2 : π2( ˜A(s)|s) ≥1 −ϵ, ∀oﬀ-path s in π∗o
.
Lemma 2. Suppose π∗induces a unique optimal signal for each sender type.
Then there exists a regular prior g1, some 0 < ϵoﬀ< 1, and a function γ(δ, ϵ)
valued in (0, 1), such that for every 0 < δ < 1, 0 < ϵ < ϵoﬀ, and γ(δ, ϵ) < γ < 1,
if π2 ∈Bon
2 (π∗, ϵ) ∩Boﬀ
2 (π∗, ϵoﬀ), then |Rg1,δ,γ
1
[π2](s|θ) −π∗
1(s|θ)| < ϵ for every
θ and s.
Note that the same ϵ appears in the hypothesis π2 ∈Bon
2 (π∗, ϵ) as in the
conclusion. That is, the aggregate sender response gets closer to π∗
1 as receivers’
play gets closer to π∗
2.
The idea is to specify a sender prior g1 that is highly conﬁdent and correct
about the receiver’s response to on-path signals, and is also conﬁdent that the
receiver responds to each oﬀ-path signal s with actions in ˜A(s). Take a signal
s
′ other than the one that θ sends in π∗
1. If θ has not experimented much
with s
′, then her belief is close to the prior and she thinks deviation does not
pay. If θ has experimented a lot with s
′, then by the law of large numbers
her belief is likely to be concentrated in ˜A(s
′), so again she thinks deviation
32


## Page 34


does not pay. Since the option value for experimentation eventually goes to 0,
at most histories all sender types are playing a myopic best response to their
beliefs, meaning they will not deviate from π∗
1. The intuition is similar to that
of Lemmas 6.1 and 6.4 from Fudenberg and Levine (2006), which says that
we can construct a highly concentrated and correct prior so that in the steady
state, most agents have correct beliefs about opponents’ play both on and one
step oﬀthe equilibrium path.
This lemma requires the assumption that π∗is strict for the sender. If
s∗were only weakly optimal for θ in π∗, there could be receiver strategies
arbitrarily close to π∗
2 that make some other signal s
′ ̸= s∗strictly optimal
for θ. In that case, we cannot rule out that a non-negligible fraction of the θ
population will rationally play s
′ forever when the receiver population plays
close to π∗
2.
6.2.2
R2 and learning rational compatibility
Let C be the set of sender strategies that respect the rational compatibility
order, that is
C := {π1 ∈Π•
1 : π1(s|θ) ≥π1(s|θ
′) whenever θ ≿s θ
′}.
The next lemma shows that there is a prior for the receivers so that when
the aggregate sender play is any strategy in C, almost all receivers end up with
beliefs consistent with the rational compatibility order. This lemma is the
main technical contribution of the paper and enables us to provide a suﬃcient
condition for rational patient stability when the relative frequencies of oﬀ-path
experiments matter.
Lemma 3. For each ϵ > 0, there exists a regular receiver prior g2 and 0 <
γ < 1 so that for any γ < γ < 1, 0 < δ < 1, and π1 ∈C,
Rg2,δ,γ
2
[π1](BR( ˆP(s), s) | s) ≥1 −ϵ
for each signal s.
The key step in the proof is constructing a prior belief for the receivers
33


## Page 35


so that when the senders’ aggregate play is suﬃciently close to the target
equilibrium, the receiver beliefs respect the compatibility order. This step was
not necessary in Fudenberg and Levine (2006), which is the only other paper
that has given a suﬃcient condition for rational patient stability in a class of
games.21
To prove Lemma 3, we construct a Dirichlet prior g2 so that for any s such
that θ
′ ≿s θ
′′, g2 assigns much greater prior weight to θ
′ playing s than to θ
′′
playing s..22 In the absence of data, the receiver strongly believes that the
senders are using strategies π1 such that p(θ
′′|s)/p(θ
′|s) ≤λ(θ
′′)/λ(θ
′). This
strong prior belief can only be overturned by a very large number of observa-
tions to the contrary. But because π1 ∈C respects the rational compatibility
order, if the receiver has a very large number of observations of senders choos-
ing s, the law of large numbers implies this large sample is unlikely to lead
the receiver to have a belief outside of ˆP(s). So we can ensure that with high
probability suﬃciently long-lived receivers play a best response to ˆP(s) after
the oﬀ-path s.
Finally, we state a lemma that says for any Dirichlet receiver prior, when
lifetimes are long enough, the aggregate receiver response approximates the
receiver’s best response function on-path when applied to a sender strategy
that provides strict incentives after every on-path signal. Write Bon
1 (π∗, ϵ) for
the elements of Π•
1 where each type θ plays ϵ-close to π∗
1(·|θ) , that is
Bon
1 (π∗, ϵ) := {π1 ∈Π•
1 : |π1(s|θ) −π∗
1(s|θ)| ≤ϵ, ∀θ, s} .
Lemma 4. Fix a strategy proﬁle π∗where the receiver has strict incentives
after every on-path signal. For each regular Dirichlet receiver prior g2, there
exists ϵ1 > 0 and a function γ(ϵ) valued in (0, 1), so that whenever π1 ∈
21Their result guarantees that the receivers’ beliefs about the frequency of type θ sending
signal s is within ϵ of the truth. This is not suﬃcient for purposes, because when signal s
has probability 0 under a given sender strategy, perturbing the strategy of every type by up
to ϵ can generate arbitrary oﬀ-path beliefs about the sender’s type.
22The Dirichlet prior is the conjugate prior to multinomial data, and corresponds to the
updating used in ﬁctitious play (Fudenberg and Kreps, 1993). It is readily veriﬁed that if
each of g(θ)
1
and g(s)
2
is Dirichlet and independent of the other components, then g is regular.
In the proof, we work with Dirichlet priors since they give tractable closed-form expressions
for the posterior mean belief of the opponent’s strategy after a given history.
34


## Page 36


Bon
1 (π∗, ϵ1), 0 < δ < 1, and γ(ϵ) < γ < 1, we have Rg2,δ,γ
2
[π1](a|s)−π∗
2(a|s)| < ϵ
for every on-path signal s in π∗and a.
The intuition is that when the aggregate sender strategy is close to π∗
1,
the law of large numbers implies that after each signal that π∗
1 gives positive
probability, a receiver with enough data is likely to have a belief close to the
Bayesian belief assigned by π∗
1. Coupled with the fact that π∗
1 is on-path strict
for the receiver, this lets us conclude that long-lived receivers play π∗
2(·|s) after
every on-path s with high probability.
7
PayoﬀInformation and Steady-State Learn-
ing
We revisit the examples from Section 2.3 and discuss how prior beliefs reﬂecting
knowledge or ignorance of payoﬀinformation lead to diﬀerent implications for
learning.
7.1
Example 2
In Example 2, it follows from Lemma 1 that for any 0 ≤δ, γ < 1, any re-
ceiver play π2 ∈Π•
2, and any regular prior g, we have Rg1
1 [π2](In | θstrong) ≥
Rg1
1 [π2](In | θweak). In the absence of payoﬀinformation, we show that there
exists a full-support prior g1 so that, ﬁxing π2 to always play Down, we get
Rg1
1 [π2](In | θstrong) ≤Rg1
1 [π2](In | θweak) for any 0 ≤δ, γ < 1, with strict
inequality for an open set of parameter values.
Underlying this is the fact that if the conditionally dominated response X
is removed from the game tree, then θstrong will experiment more frequently
with In than θweak does because θstrong potentially has more to gain. This
story breaks down if senders do not know receivers’ payoﬀs and thus suspect
that X might be used after In. We now show that for some full-support prior
beliefs, θweak experiments more with In than θstrong does under any patience
level when receivers always play Down.
Let g(In)
1
be Dirichlet with weights (1, K, 1) on (Up, Down, X) for arbitrary
K ≥4. After observing k ≥0 instances of receivers responding to In with
35


## Page 37


Down, a sender would have the posterior Dirichlet(1, K + k, 1). The θweak
type’s Gittins index for In would be unchanged if her payoﬀs to (Up, Down,
X) were (3, −1, 1) instead of (1, −1, 3), by symmetry of her beliefs about Up
and X. This observation shows her Gittins index for In is at least as large
as θstrong’s, whose payoﬀs to (Up, Down, X) are (2, −1, 1). So the strong
type switches away from In after fewer observations of Down than the weak
type does (this includes the case of “switching away” after 0 observations of
Down, i.e. the strong type never experimenting with In.) We have proven
Rg1
1 [π2](In | θstrong) ≤Rg1
1 [π2](In | θweak) for any 0 ≤δ, γ < 1.
Signal In is myopically suboptimal for both types, and by the previous
argument, the minimum eﬀective discount factor δγ that would induce at
least one period of experimentation with In is strictly higher for the strong
type than the weak type.
This shows for an open set of δ, γ parameters,
Rg1
1 [π2](In | θstrong) = 0 but Rg1
1 [π2](In | θweak) > 0.
7.2
Example 3
In Example 3 we showed that there is an RCE in which the receivers play a3
after R. Because RCE is not a suﬃcient condition for rational patient stability,
this leaves open the question of whether this strategy can arise in our learning
model. Here we verify that it can, and also show that “a3 after R” cannot
be part of a patiently stable outcome in the absence of payoﬀinformation.
This is because patient but inexperienced θ1’s without payoﬀinformation ﬁnd
it plausible that receivers choose a1 after R, so they will experiment much
more frequently with the oﬀ-path signal R than θ2’s, for whom every possible
response to R leads to worse payoﬀs than their equilibrium payoﬀof 2. As a
result, receivers learn that R-senders have type θ1 so they respond with a2. On
the other hand, when senders know ex-ante that receivers will never choose a1
after R, for some priors there are steady states where no one ever experiments
with R. When this happens, the receivers’ belief about the likelihood ratio of
the types following the oﬀ-path R is governed by their initial beliefs about the
distribution of sender play at the start of learning, which may be arbitrary
and thus support a richer class of equilibrium proﬁles.
36


## Page 38


Speciﬁcally, in Example 3, suppose g(L)
1
is Dirichlet (1, 10, 1) over all three
responses to L, while g(R)
1
is Dirichlet(1, 1) on ABR
R = {a2, a3}, which reﬂects
the sender’s knowledge that a1 is a conditionally dominated response to R.
And suppose that gθ1
2 is the Dirichlet(2, 1) distribution on {L, R} and gθ2
2 is
the Dirichlet(2, x) distribution, where x > 0 is a free parameter.
For any
0 ≤δ, γ < 1, there exists a steady state where senders always choose L and
receivers always respond to L with a2. This is because the Gittins index for R
is no larger than −3 for θ1 and no larger than 1 for θ2 after any history, while
the myopic expected payoﬀof L already exceeds these values in the ﬁrst period.
The expected payoﬀof L only increases with additional observations of a2 after
L. On the receiver side, every positive-probability history y2 must involve the
senders playing L every period. Following such a history, the receiver believes
θ1 plays L with probability at least 2
3, hence an L-sender is the θ1 type with
probability at least
2/3
1+2/3 = 2
5. We have a2 ∈BR({p}, L) whenever p(θ1) ≥2
5,
so we have shown that in the steady state receivers always play a2 after L.
In this steady state, signal R is never sent, so by choosing diﬀerent values
of x > 0, we can sustain either a2 or a3 after R as part of a rationally patiently
stable proﬁle. To be more precise, let n1 and n2 count the number of times the
two types of senders appear in a positive-probability history y2. The receiver’s
posterior assigns the following likelihood ratio to the type of an R-sender:
1
3 + n1
/
x
2 + x + n2
= 1
x ·
2 + x + n2
3 + n1

.
Since the two types are equally likely, the fraction of receivers with histories y2
so that 0.9 ≤

2+x+n2
3+n1

≤1.1 approaches 1 as γ →1. Depending on whether
x = 1/4 or x = 4, these receivers will play a2 or a3 after R, so π2(a2 | R) = 1
and π2(a3 | R) = 1 are both δ-stable for any δ ≥0, under two diﬀerent regular
priors reﬂecting payoﬀknowledge.
By contrast, Theorem 3 of Fudenberg and He (2018) implies that if priors
g1, g2 have full support on Π2 and Π1 respectively, then we must have a2 after
R in every patiently stable proﬁle. The idea is that when senders are patient
and long-lived, new θ1 start oﬀby trying R but new θ2 start oﬀby trying L.
When receivers play a2 after L with high probability, it is very unlikely that
37


## Page 39


θ2 ever switches away from L, providing a bound on their frequency of playing
R. On the other hand, as their eﬀective discount factor increases, θ1 will spend
arbitrarily many periods of its early life playing R in hopes of getting the best
payoﬀof 5, lacking the payoﬀknowledge that a1 is conditionally dominated
for the receivers after R. Receivers therefore end up learning that R-senders
have type θ1.
8
Conclusion
This paper studies non-equilibrium learning about other players’ strategies in
the setting of signaling games.
When the agents’ prior beliefs about their
opponents’ play reﬂect prior knowledge of others’ payoﬀfunctions, the steady
states of societies of Bayesian learners can be bounded by two equilibrium
reﬁnements, RCE and uRCE, that is we get
uRCE ⊆rationally patiently stable proﬁles ⊆RCE.
Furthermore, every divine equilibrium is an RCE. This is not true for all of
the equilibria that satisfy the Intuitive Criterion, which suggests that divine
equilibrium does a better job of capturing the implications of learning. That
said, we do not know the exact relationship between rational patient stability
and divine equilibrium, and there is scope for sharpening our conclusions.
Divine equilibrium and RCE are only deﬁned for signaling games. In gen-
eral extensive-form games, agents may ﬁnd it optimal to play strictly domi-
nated strategies as experiments to learn about the consequences of their other
strategies, so requiring prior beliefs to be supported on opponents’ undomi-
nated strategies can lead to situations where agents observe play that they
had assigned zero prior probability. We leave the associated complications for
future work.
38


## Page 40


References
Banks, J. S. and J. Sobel (1987): “Equilibrium Selection in Signaling
Games,” Econometrica, 55, 647–661.
Cho, I.-K. and D. M. Kreps (1987): “Signaling Games and Stable Equi-
libria,” Quarterly Journal of Economics, 102, 179–221.
Dekel, E., D. Fudenberg, and D. K. Levine (1999): “PayoﬀInformation
and Self-Conﬁrming Equilibrium,” Journal of Economic Theory, 89, 165–
185.
Esponda, I. and D. Pouzo (2016): “Berk-Nash Equilibrium: A Framework
for Modeling Agents With Misspeciﬁed Models,” Econometrica, 84, 1093–
1130.
Fudenberg, D. and K. He (2018): “Learning and Type Compatibility in
Signaling Games,” Econometrica, 86, 1215–1255.
Fudenberg,
D. and Y. Kamada (2015):
“Rationalizable partition-
conﬁrmed equilibrium,” Theoretical Economics, 10, 775–806.
——— (2018): “Rationalizable partition-conﬁrmed equilibrium with hetero-
geneous beliefs,” Games and Economic Behavior, 109, 364–381.
Fudenberg, D. and D. M. Kreps (1993): “Learning Mixed Equilibria,”
Games and Economic Behavior, 5, 320–367.
Fudenberg, D. and D. K. Levine (1993): “Steady State Learning and
Nash Equilibrium,” Econometrica, 61, 547–573.
——— (2006): “Superstition and Rational Learning,” American Economic
Review, 96, 630–651.
Kalai, E. and E. Lehrer (1993): “Rational Learning Leads to Nash Equi-
librium,” Econometrica, 61, 1019–1045.
Kohlberg, E. and J.-F. Mertens (1986): “On the Strategic Stability of
Equilibria,” Econometrica, 54, 1003–1037.
39


## Page 41


Sobel, J., L. Stole, and I. Zapater (1990): “Fixed-Equilibrium Ratio-
nalizability in Signaling Games,” Journal of Economic Theory, 52, 304–331.
Van Damme, E. (1987): Stability and Perfection of Nash Equilibria, Springer-
Verlag.
A
Appendix
A.1
Proof of Proposition 1
Proof. To show (1), suppose θ
′ ≿s′ θ
′′ and θ
′′ ≿s′ θ
′′′. For any π2 ∈Π•
2 where s
′
is weakly optimal for θ
′′′, it must be strictly optimal for θ
′′, hence also strictly
optimal for θ
′. This shows θ
′ ≿s′ θ
′′′.
To establish (2), partition the set of rational receiver strategies as Π•
2 =
Π+
2 ∪Π0
2 ∪Π−
2 , where the three subsets refer to receiver strategies that make
s
′ strictly better, indiﬀerent, or strictly worse than the best alternative signal
for θ
′′. If the set Π0
2 is nonempty, then θ
′ ≿s′ θ
′′ implies θ
′′ ̸≿s′ θ
′. This
is because against any π2 ∈Π0
2, signal s
′ is strictly optimal for θ
′ but only
weakly optimal for θ
′′. At the same time, if both Π+
2 and Π−
2 are nonempty,
then Π0
2 is nonempty. This is because both π2 7→u1(θ
′′, s
′, π2(·|s
′)) and π2 7→
maxs′′̸=s′ u1(θ
′′, s
′′, π2(·|s
′′)) are continuous functions, so for any π+
2 ∈Π+
2 and
π−
2 ∈Π−
2 , there exists α ∈(0, 1) so that απ+
2 + (1 −α)π−
2 ∈Π0
2. (Note that
π+
2 and π−
2 must be supported on ABR
s
after every signal s, so the same must
hold for the mixture απ+
2 + (1 −α)π−
2 . Thus, this mixture also belongs to Π•
2.)
If only Π+
2 is nonempty and θ
′ ≿s′ θ
′′, then s
′ is rationally strictly dominant
for both θ
′ and θ
′′. If only Π−
2 is nonempty, then we can have θ
′′ ≿s′ θ
′ only
when s
′ is never a weak best response for θ
′ against any π2 ∈Π•
2.
A.2
Proof of Proposition 2
Proof. Let π∗be a uRCE. We construct a path-equivalent RCE, π◦as follows.
Set π◦
1 = π∗
1 and set π◦
2(· | s) = π∗
2(· | s) for every on-path signal s.At each
oﬀ-path signal s where ˜J(s, π∗) ̸= ∅, let π◦
2(· | s) prescribe some best response
40


## Page 42


to a belief in ˜P(s, π∗).At each oﬀ-path signal s where ˜J(s, π∗) = ∅, let π◦
2(· | s)
prescribe some best response to a belief in ∆(Θs).
In this strategy proﬁle, the receiver’s play is a best response to rationality-
compatible beliefs after every oﬀ-path s by construction, and because the
sender’s play is the same as before the receiver is still playing best responses
to on-path signals.
Because the on-path play of the receivers did not change, no sender type
wishes to deviate to any on-path signal. Now we check that no sender type
wishes to deviate to any oﬀ-path signal.
Consider ﬁrst oﬀ-path s where
˜J(s, π∗) ̸= ∅. Here we have ˜J(s, π∗) ⊆Θs, which implies that ˜P(s, π∗) ⊆ˆP(s).
By the deﬁnition of uRCE, π◦
2(· | s) must deter every type from deviating to
such s. Finally, no sender type wishes to deviate to any s where ˜J(s, π∗) = ∅,
by the deﬁnition of equilibrium dominance.
A.3
Proof of Proposition 3
Proof. Fix a π1 with π1(s|θ
′′) > 0 but π1(s|θ
′) < 1. Because the space of
rational receiver strategies Π•
2 is convex, it suﬃces to show there is no receiver
strategy π2 ∈Π•
2 such that π1 is a best response to π2 in the ex-ante strategic
form. If π1 is an ex-ante best response, then it needs to be at least weakly
optimal for type θ
′′ to play s against π2. By θ
′ ≿s θ
′′, this implies s is strictly
optimal for type θ
′. This shows π1 is not a best response to π2, as the sender
can increase her ex-ante expected payoﬀs by playing s with probability 1 when
her type is θ
′.
A.4
Proof of Proposition 4
Proof. Suppose π∗does not pass the Intuitive Criterion. Then there exists a
type θ and a signal s
′ such that
u1(θ; π∗) <
min
a∈BR(∆(e
J(s′,π∗)),s)
u1(θ, s
′, a).
41


## Page 43


If π∗were an RCE, then we would have π∗
2(·|s
′) ∈∆(BR( ˜P(s, π∗), s)). Since
˜P(s, π∗) ⊆∆( eJ(s
′, π∗)), we have
u1(θ; π∗) < u1(θ, s
′, π∗
2(·|s
′)).
This means π∗is not a Nash equilibrium, contradiction.
A.5
Proof of Proposition 5
Proof. To show (a), note ﬁrst that if D(θ
′′, s
′; π∗) ∪D◦(θ
′′, s
′; π∗) = ∅the
conclusion holds vacuously. If D(θ
′′, s
′; π∗) ∪D◦(θ
′′, s
′; π∗)is not empty, take
any α
′ ∈D(θ
′′, s
′; π∗) ∪D◦(θ
′′, s
′; π∗) and deﬁne π
′
2 ∈Π•
2 by π
′
2(·|s
′) = α
′,
π
′
2(·|s) = π∗
2(·|s) for s ̸= s
′. Then
u1(θ
′′; π∗) = max
s̸=s′ u1(θ
′′, s, π
′
2(·|s)) ≤u1(θ
′′, s
′, π
′
2(·|s
′)) = u1(θ
′′, s
′, α
′),
and when θ
′ ≿s′ θ
′′, this implies that
u1(θ
′; π∗) = max
s̸=s′ u1(θ
′, s, π
′
2(·|s)) < u1(θ
′, s
′, π
′
2(·|s
′)) = u1(θ
′, s, α
′).
Hence α
′ ∈D(θ
′, s
′; π∗).
To show (b), suppose π∗is a divine equilibrium. Then it is a Nash equilib-
rium, and furthermore for any oﬀ-path signal s
′ where θ
′ ≿s′ θ
′′, Proposition
5(a) implies that
D(θ
′′, s
′; π∗) ∪D◦(θ
′′, s
′; π∗) ⊆D(θ
′, s
′; π∗).
Since π∗is a divine equilibrium, π∗
2(·|s
′) must then best respond to some belief
p ∈∆(Θ) with p(θ
′′)
p(θ
′) ≤λ(θ
′′)
λ(θ
′) . Considering all (θ
′, θ
′′) pairs, we see that in a
divine equilibrium π∗
2(·|s
′) best responds to some belief in
\
(θ′,θ′′) s.t. θ′≿s′ θ′′
Pθ′▷θ′′.
42


## Page 44


At the same time, in every divine equilibrium, belief after oﬀ-path s
′ puts zero
probability on equilibrium-dominated types, meaning π∗
2(· | s
′) best responds
∆( eJ(s
′, π∗)). This shows π∗is an RCE.
A.6
Proof of Proposition 6
Proof. Consider a uRCE π∗. For every oﬀ-path s, perform the following mod-
iﬁcations on π∗
2(·|s): if the ﬁrst-round application of the NWBR procedure
would have deleted every type, then do not modify π∗
2(·|s). Otherwise, ﬁnd
some θs not deleted by the iterated NWBR procedure, then change π∗
2(·|s) to
some action in BR({θs}, s), i.e. a best response to the belief putting probabil-
ity 1 on θs.
This modiﬁed strategy proﬁle passes the NWBR test. We now establish
that it remains a uRCE by checking that for those oﬀ-path s where π∗
2(·|s) was
modiﬁed, the modiﬁed version is still a best response to ˆP(s). (By uniformity,
this would ensure that the modiﬁed receiver play continues to deter every type
from deviating to s.)
Type θs satisﬁes θs ∈Θs. Otherwise, D◦(θs, s; π∗) = ∅and θs would have
been deleted by NWBR in the ﬁrst round.
Now it suﬃces to argue there
is no θ
′ such that θ
′ ≿s θs, which implies the belief putting probability 1
on θs is in ˆP(s). If there were such θ
′, by Proposition 5(a) we would have
D◦(θs, s; π∗) ⊆D(θ
′, s; π∗), so θs should have been deleted by NWBR in the
ﬁrst round, contradicting the fact that θs survives all iterations of the NWBR
procedure.
A.7
Proof of Corollary 1
Proof. This is follows from Proposition 6 because every NWBR equilibrium is
a universally divine equilibrium.
A.8
Proof of Lemma 2
Proof. Here are three lemmas from Fudenberg and Levine (2006):
43


## Page 45


FL06 Lemma A.1: Suppose {Xk} is a sequence of i.i.d. Bernoulli random
variables with E[Xk] = µ, and deﬁne for each n the random variable
Sn := | Pn
k=1(Xk −µ)|
n
.
Then for any n, ¯n ∈N,
P

max
n≤n≤¯n Sn > ϵ

≤27
3 · 1
n · µ
ϵ4.
FL06 Lemma A.2: For all ϵ, ϵ′ > 0, there is an N > 0 so that for all
δ, γ, g, π, signal s and action a ∈A,
ψπ2;(g,δ,γ)
θ
{yθ : |ˆπ2(a|s; yθ) −π2(a|s)| > ϵ, #(s|yθ) > N} < ϵ′.
(Here, ˆπ2(a|s; yθ) is the empirical frequency of receiver playing a after signal
m in history yθ, that is to say ˆπ2(a|s; yθ) = #((a, s), yθ)/#(s, yθ).)
FL06 Lemma A.4: For all ϵ, ϵ′ > 0 and δ < 1, there exists N such that
for all π, g, and γ, we get
ψπ2;(g,δ,γ)
θ
{yθ /∈Yθ(ϵ), #(σθ(yθ), yθ) > N} ≤ϵ′
where Yθ(ϵ) ⊆Yθ are those histories yθ where
max
s∈S u1(θ, s|yθ) ≤u1(σθ(yθ)|yθ) + ϵ,
that is, type θ is playing a myopic ϵ best response according to posterior belief
after history yθ.
Now we proceed with our argument.
Since π∗is strict on-path , there exist ξ1, ξ2 > 0 such that whenever π2
satisﬁes |π2(a|s) −π∗
2(a|s)| ≤ξ1 for every on-path s and action a, while for
every oﬀ-path s we have π2( ˜A(s)|s) ≥1 −ξ1, then for each type θ we get
u1(θ, π∗
1(θ), π2) > ξ2 + max
s̸=π∗
1(θ) u1(θ, s, πR).
That is, if receiver plays ξ1-close to π∗on-path and ξ1-close to ˜A(s) oﬀ-path,
44


## Page 46


then for every type of sender, playing the prescribed equilibrium signal is
strictly better than any other signal by at least ξ2 > 0.
Following Fudenberg and Levine (2006), consider a prior g1 such that when-
ever sender has fewer than n := 211/ξ4
1 observations of playing signal s, her
belief as to receiver’s probability of taking action a after signal s diﬀers from
π∗
1(a|s) by no more than ξ1 if s is on-path, while her belief as to the probability
that receiver strategy assigns to ˜A(s) is at least 1 −ξ if s is oﬀ-path. Also, let
ϵoﬀ:= ξ1/2.
Now let δ ∈(0, 1) and 0 < ϵ < ϵoﬀbe given. We construct γ(δ, ϵ) satisfying
the conclusion of the lemma.
To do this, in FL06 Lemma A.4 put ϵ = ξ2 and ϵ
′ = ϵ/6, to obtain a
N1(ϵ). Next, in FL06 Lemma A.2 put ϵ = ξ1/2, ϵ
′ = ϵ/6, to obtain N2(ϵ). Let
N(ϵ) := N1(ϵ) ∨N2(ϵ). There are 5 classes of exceptional histories for type θ
that can lead to playing some signal ˆs other than the one prescribed by the
equilibrium strategy, s∗:= π∗
1(θ).
Exception 1: θ has played ˆs fewer than N(ϵ) times before, that is σθ(yθ) =
ˆs but #(ˆs, yθ) < N(ϵ). Such histories can be made to have mass no larger than
ϵ/6 by taking γ(δ, ϵ) large enough.
Exception 2: yθ is in the exceptional set described in FL06 Lemma A.4.
But by choice of N(ϵ) ≥N1(ϵ), we know that
ψπ2;(g,δ,γ)
θ
{yθ /∈Yθ(ξ2), #(σθ(yθ), yθ) > N(ϵ)} ≤ϵ/6.
Exception 3: θ has played ˆs more than N(ϵ) times, but has a misleading
sample. By FL93 Lemma A.2,
ψπ2;(g,δ,γ)
θ
{yθ : |ˆπ2(a|ˆs; yθ) −π2(a|ˆs)| > ξ1/2, #(ˆs|yθ) > N(ϵ)} < ϵ/6.
Since we have chosen π ∈Bon
2 (π∗, ϵ) ∩Boﬀ
2 (π∗, ϵoﬀ), we know π2 diﬀers from
π∗
2 by no more than ϵoﬀ= ξ1/2 after every on-path signal, and puts no more
45


## Page 47


weight than ξ1/2 on actions not in ˜A(s) after oﬀ-path signal s. So in particular,
ψπ2;(g,δ,γ)
θ







yθ :
|ˆπ2(a|ˆs; yθ) −π∗
2(a|ˆs)| > ξ1 if ˆs on-path, or
ˆπ2( ˜A(ˆs)|ˆs) < 1 −ξ1 if ˆs oﬀ-path
#(ˆs|yθ) > N(ϵ)







< ϵ/6.
Exception 4: θ has played the equilibrium signal s∗more than N(ϵ) times,
but has a misleading sample. As before, we get
ψπ2;(g,δ,γ)
θ
{yθ : |ˆπ2(a|s∗; yθ) −π∗
2(a|s∗)| > ξ1, #(s∗|yθ) > N(ϵ)} < ϵ/6.
Exception 5: θ has played the equilibrium signal s∗between n and N(ϵ)
times, but has a misleading sample. Let Xk ∈{0, 1} denote whether θ sees
the equilibrium response π∗
2(s∗) the k-th time she plays s∗(Xk = 0) or whether
she sees instead a diﬀerent response (Xk = 1). As in FL06 Lemma A.1, deﬁne
Sn := |
Pn
k=1(Xk −µ)|
n
where µ = 1 −π2(π∗
2(s∗)|s∗) < ϵ since s∗is an on-path signal in π∗.
The probability that the fraction of responses other than π∗
1(s∗) exceeds ξ1
between then-th time and N(ϵ)-th time that θ plays s∗is bounded above by
FL06 Lemma A.1,
P
"
max
n≤n≤N(ϵ) Sn > ξ1/2
#
≤
27
3 · 1
n ·
µ
(ξ1/2)4
≤
1
3 · µ (by choice of n)
≤
ϵ1/3.
Finally, at a history yθ that does not belong to those exceptions, we must
have σθ(yθ) = m∗. This is because yθ is not in exception 1, so θ has played
σθ(yθ) at least N(ϵ) times before, and it is not in exception 2, so σθ(yθ) is a
ξ2 myopic best response to current beliefs. Yet the empirical frequency for
response after signal σθ(yθ) is no more than ξ1 away from π∗
2(σθ(yθ)) as yθ is
not in exception 3 . Since the prior is Dirichlet and also has this property, this
46


## Page 48


means the current posterior belief about response after signal σθ(yθ) also has
this property. If #(s∗, yθ) > n, then yθ not being in exceptions 4 or 5 implies
belief as to response after signal s∗is also no more than ξ1 away from π∗
2(s∗),
while if #(s∗, yθ) < n then choice of prior implies the same. In short, beliefs
on both responses after s∗and responses after σθ(yθ) are no more than ξ1 away
from their π∗
2 counterparts. But in that case, no signal other than s∗can be
an ξ2 best response.
A.9
Proof of Lemma 3
Proof. For each ξ > 0, consider the approximation to Pθ′▷θ′′,
P ξ
θ′▷θ′′ :=
(
p ∈∆(Θ) : p(θ
′′)
p(θ
′) ≤(1 + ξ)λ(θ
′′)
λ(θ
′)
)
and hence the approximation to ˆP(s),
ˆPξ(s) := ∆(Θs′)
\ n
P ξ
θ′▷θ′′ : θ
′ ≿s′ θ
′′o
.
Since the BR correspondence has a closed graph, there is an ξ > 0 such that
BR( ˆPξ(s), s) = BR( ˆP(s), s).
Take some such ξ. Next we will choose a series of constants.
• Pick 0 < h < 1 such that 1−h
1+h > (1 −ξ)1/3.
• Pick G > 0 such that for every θ ∈Θ, 1/(h2 · G · (1 −h) · λ(θ)) <
ϵ/(4 · |S| · |Θ|2).
• For each θ, construct a Dirichlet prior on Sθ with parameters α(θ, s) ≥0.
Pick Dirichlet prior parameters α(θ, s) ≥0 so that whenever θ ≿s θ′, we
have
α(θ, s) −α(θ
′, s) > (
q
(4 · |S| · |Θ|2)/ϵ + 1) · G.
(2)
In the event that θ ≿s θ
′ and θ
′ ≿s θ, put α(θ, s) = α(θ
′, s).
47


## Page 49


• Pick N ∈N so that for any N > N, θ, θ
′ ∈Θ, we have
P[(1 −h) · N · λ(θ) ≤Binom(N, λ(θ)) ≤(1 + h) · N · λ(θ)] > 1 −
ϵ
4 · |Θ|
and
(1 −h) · N · λ(θ
′)
(1 + h) · N · λ(θ) + maxθ
P
s∈S α(θ, s) > (1 −ξ)1/3λ(θ
′)
λ(θ) .
• Pick γ ∈(0, 1) such that 1 −(γ)N+1 < ϵ/4.
Suppose the receiver’s prior over the strategy of typeθ is Dirichlet with pa-
rameters (α(θ, s))s∈S. We claim that the conclusion of the lemma holds.
Fix some strategy π1 ∈C. Write #(θ|y2) for the number of times the
sender has been of θ type in history y2, while #(θ, s|y2) counts the number
of times type θ has sent signal s in history y2. Put ψ2 = ψπ1;(g,δ,γ)
2
and write
E ⊆Y2 for those receiver histories with length at least N satisfying
(1 −h) · N · λ(θ) ≤#(θ|y2) ≤(1 + h) · N · λ(θ)
for every θ ∈Θ. By the choice of N and γ, whenever γ > γ we have ψ(E) ≥
1 −ϵ/2.
We now show that given E, the conditional probability that the
receiver’s posterior belief after every oﬀ-equilibrium signal s lies in ˆPξ(s) is at
least 1 −ϵ/2. To do this, ﬁx signal s and two types with θ ≿s θ
′.
If s is strictly dominated for both θ and θ
′, then according to the receivers’
Dirichlet prior, θ and θ
′ each sends s with zero probability. Since π ∈Π•
1,
we have π1(s|θ) = π1(s|θ
′) = 0. So after every positive-probability history,
receiver’s belief falls in ˆPξ(s) as it puts zero probability on the s-sender being
θ or θ
′. Henceforth we only consider the case where s is not strictly dominated
for both.
After history y2, the receiver’s updated posterior likelihood ratio for types
48


## Page 50


θ and θ′ upon seeing signal s is
λ(θ)
λ(θ′) ·
 
α(θ, s) + #(θ, s|y2)
#(θ|y2) + P
s∈S α(θ, s)/
α(θ
′, s) + #(θ
′, s|y2)
#(θ
′|y2) + P
s∈S α(θ
′, s)
!
= λ(θ)
λ(θ′) · α(θ, s) + #(θ, s|y2)
α(θ
′, s) + #(θ
′, s|y2) · #(θ
′|y2) +
P
s∈S α(θ
′, s)
#(θ|y2) + P
s∈S α(θ, s) .
Since we have #(θ
′|y2) ≥(1 −h) · N · λ(θ
′) while #(θ|y2) ≤(1 + h) · N · λ(θ),
we get
#(θ
′|y2) + P
s∈S α(θ
′, s)
#(θ|y2) + P
s∈S α(θ, s) ≥
(1 −h) · N · λ(θ
′)
(1 + h) · N · λ(θ) + P
s∈S α(θ, s) > (1−ξ)1/3·λ(θ′)
λ(θ) .
If s is strictly dominant for both θ and θ
′, then π1 ∈Π•
1 means that π1(s|θ) =
π1(s|θ
′) = 1. In this case, #(θ, s|y2) = #(θ|y2) and #(θ
′, s|y2) = #(θ
′|y2).
Since #(θ|y2) ≥(1 −h) · N · λ(θ), #(θ
′|y2) ≤(1 + h) · N · λ(θ
′), we have:
α(θ, s) + #(θ, s|y2)
α(θ
′, s) + #(θ
′, s|y2) ≥
(1 −h) · N · λ(θ)
P
s∈S α(θ
′, s) + (1 + h) · N · λ(θ
′) ≥(1 −ξ)1/3 λ(θ)
λ(θ
′).
This shows the product is no smaller than (1 −ξ)2/3 λ(θ)
λ(θ′), so receiver believes
in P ξ
θ▷θ′ after every history in E.
Now we analyze the term
α(θ,s)+#(θ,s|y2)
α(θ′,s)+#(θ′,s|y2) for the case where s is not strictly
dominant for both θ and θ
′. We consider two cases, depending on whether N is
“large enough” so that the compatible type θ experiments enough on average
in a receiver history of length N under sender strategy π1.
Case A: π1(s|θ) · N < G. In this case, since π ∈C and θ ≿s θ′, we must
also have π1(s|θ
′)·N < G. Then #(θ′, s|y2) is distributed as a binomial random
variable with mean smaller than G, hence standard deviation smaller than
√
G.
By Chebyshev’s inequality, the probability that it exceeds (
q
(4 · |S| · |Θ|2)/ϵ+
1) · G is no larger than
1
G · (4 · |S| · |Θ|2)/ϵ <
ϵ
4|S| · |Θ|2.
But in any history y2 where #(θ′, s|yR) does not exceed this number, we would
49


## Page 51


have
α(θ
′, s) + #(θ
′, s|y2) ≤α(θ, s) ≤α(θ, s) + #(θ, s|y2)
by choice of the diﬀerence between prior parameters α(θ′, s) and α(θ, s). There-
fore
α(θ,s)+#(θ,s|y2)
α(θ′,s)+#(θ′,s|y2) ≥1. In summary, under Case A, there is probability no
smaller than 1 −
ϵ
4|S|·|Θ|2 that
α(θ,s)+#(θ,s|y2)
α(θ′,s)+#(θ′,s|y2) ≥1.
Case B: π1(s|θ) · N ≥G. In this case, we can bound the probability that
#(θ, s|y2)/#(θ
′, s|y2) ≤λ(θ)
λ(θ′) · (1 −h
1 + h)2.
Let p := π1(s|θ). Given that #(θ|y2) ≥(1 −h) · N · λ(θ), the distribution of
#(θ, s|y2) ﬁrst order stochastically dominates Binom((1 −h) · N · λ(θ), p).
On the other hand, given that #(θ|y2) ≤(1+h)·N ·λ(θ′) and furthermore
π1(s|θ′) ≤π1(s|θ) = p, the distribution of #(θ′, s|y1) is ﬁrst order stochastically
dominated by Binom((1 + h) · N · λ(θ′), p).
The ﬁrst distribution has mean (1−h)·N ·λ(θ)·p with standard deviation
no larger than
q
(1 −h) · N · λ(θ) · p. Thus
P [Binom((1 −h) · N · λ(θ), p) < (1 −h) · (1 −h) · N · λ(θ) · p]
< 1/(h ·
q
p(1 −h)Nλ(θ))2 ≤1/(h ·
q
G · (1 −h) · λ(θ))2 < ϵ/(4 · |S| · |Θ|2)
where we used the fact that pN ≥G in the second-to-last inequality, while
the choice of G ensured the ﬁnal inequality.
At the same time, the second distribution has mean (1 + h) · N · λ(θ′) · p
with standard deviation no larger than
q
(1 + h) · N · λ(θ′) · p, so
P [Binom((1 + h) · N · λ(θ′), p) > (1 + h) · (1 + h) · N · λ(θ′) · p]
< 1/(h ·
q
p(1 + h)Nλ(θ′))2 ≤1/(h ·
q
G · (1 + h) · λ(θ′))2 < ϵ/(4 · |S| · |Θ|2)
by the same arguments. Combining the bounds on these two binomial random
variables,
P
" Binom((1 −h) · N · λ(θ), p)
Binom((1 + h) · N · λ(θ′), p) ≤λ(θ)
λ(θ′) · (1 −h
1 + h)2
#
< ϵ/(2 · |S| · |Θ|2).
50


## Page 52


Via stochastic dominance, this shows a fortiori
P
"
#(θ, s|y2)/#(θ
′, s|y2) ≤λ(θ)
λ(θ′) · (1 −h
1 + h)2
#
< ϵ/(2 · |S| · |Θ|2).
Therefore, for any s, θ, θ′ such that θ ≿s θ′,
ψ
 
y2 : α(θ, s) + #(θ, s|y2)
α(θ
′, s) + #(θ
′, s|y2) ≥λ(θ)
λ(θ′) · (1 −h
1 + h)2 | E
!
≥1 −ϵ/(2 · |S| · |Θ|2).
This concludes case B.
In either case, at a history y2 with (1−h)·N ·λ(θ) ≤#(θ|y2) ≤(1+h)·N ·
λ(θ) for every θ, for every pair θ, θ′ such that θ ≿s θ′, we get
α(θ,s)+#(θ,s|y2)
α(θ′,s)+#(θ′,s|y2) ≥
λ(θ)
λ(θ′) · (1−h
1+h)2 with probability at least 1 −ϵ/(2 · |S| · |Θ|2).
But at any history y2 where this happens, the receiver’s posterior likelihood
ratio for types θ and θ′ after signal s satisﬁes
λ(θ)
λ(θ′) · α(θ, s) + #(θ, s|y2)
α(θ
′, s) + #(θ
′, s|y2) · #(θ
′|y2) +
P
s∈S α(θ
′, s)
#(θ|y2) + P
s∈S α(θ, s)
≥
λ(θ)
λ(θ′) · λ(θ)
λ(θ′) ·
 1 −h
1 + h
!
2 · (1 −ξ)1/3 · λ(θ′)
λ(θ)
≥
λ(θ)
λ(θ′) · (1 −ξ)2/3 · (1 −ξ)1/3 ≥λ(θ)
λ(θ′) · (1 −ξ).
As there are at most |Θ|2 such pairs for each signal s and |S| total signals,
ψ


y2 :
λ(θ)
λ(θ′) ·
α(θ,s)+#(θ,s|y2)
α(θ′,s)+#(θ′,s|y2) ·
#(θ
′|y2)+P
s∈S α(θ
′,s)
#(θ|y2)+P
s∈S α(θ,s)
≥λ(θ)
λ(θ′) · (1 −ξ)
∀s, θ ≿s θ′ |E


≥1 −ϵ/2
as claimed. As the event E has ψ-probability no smaller than 1 −ϵ/2, there
is ψ probability at least 1 −ϵ that receiver’s posterior belief is in ˆPξ(s) after
every oﬀ-path s.
51


## Page 53


A.10
Proof of Lemma 4
Proof. Since π∗is on-path strict for the receiver, there exists some ξ > 0 such
that for every on-path signal s and every belief p ∈∆(Θ) with
|p(θ) −p(θ; s, π∗)| < ξ, ∀θ ∈Θ
(3)
(where p(·; s, π∗) is the Bayesian belief after on-path signal s induced by the
equilibrium π∗), we have BR(p, s) = {π∗
2(s)}. For each s, we show that there
is a large enough N(s, ϵ) and small enough ζ(s) so that when receiver observes
history y2 generated by any π ∈Bon(π∗, ϵ
′) with ϵ
′ < ζ(s)/4 and length at
least N(s, ϵ), there is probability at least 1 −
ϵ
2|S| that receiver’s posterior
belief satisﬁes (3). Hence, conditional on having a history length of at least
N(s, ϵ), there is 1 −
ϵ
2|S| chance that receiver will play as in π∗
2 after s. By
taking the maximum N ∗(ϵ) := maxs(N(s, ϵ1)) and minimum ϵ1 := mins ζ(s),
we see that whenever history is length N ∗(ϵ) or more, and π ∈Bon(π∗, ϵ
′) with
ϵ
′ < ϵ1, there is at least 1 −ϵ/2 chance that the receiver’s strategy matches π∗
2
after every on-path signal . Since we can pick γ(ϵ) large enough that 1 −ϵ/2
measure of the receiver population is age N ∗(ϵ) or older, we are done.
To construct N(s, ϵ) and ζ(s), let Λ(s) := λ{θ : π∗
1(s|θ) = 1}. Find small
enough ζ(s) ∈(0, 1) so that:
• |
λ(θ)
Λ(s)·(1−ζ(s)) −λ(θ)
Λ(s)| < ξ
• |
λ(θ)·(1−ζ(s))
Λ(s)+(1−Λ(s))·ζ(s) −λ(θ)
Λ(s)| < ξ
•
ζ(s)
1−ζ(s) · λ(θ)
Λ(s) < ξ
for every θ ∈Θ. After a history y2, the receiver’s posterior belief as to the
type of sender who sends signal s satisﬁes
p(θ|s; y2) ∝λ(θ) · #(θ, s|y2) + α(θ, s)
#(θ|y2) + A(θ)
,
where α(θ, s) is the Dirichlet prior parameter on signal s for type θ and A(θ) :=
P
s∈S α(θ, s). By the law of large numbers, for long enough history length, we
52


## Page 54


can ensure that if π1(s|θ) > 1 −ζ(s)
4 , then
#(θ, s|y2) + α(θ, s)
#(θ|y2) + A(θ)
≥1 −ζ(s)
with probability at least 1 −
ϵ
2|S|2, while if π1(s|θ) < ζ(s)/4, then
#(θ, s|y2) + α(θ, s)
#(θ|y2) + A(θ)
< ζ(s)
with probability at least 1−
ϵ
2|S|2. Moreover there is some N(s, ϵ) so that there
is probability at least 1 −
ϵ
2|S| that a history y2 with length at least N(s, ϵ)
satisﬁes above for all θ. But at such a history, for any θ such that π∗
1(s|θ) = 1,
p(θ|s; y2) ≥
λ(θ) · (1 −ζ(s))
Λ(s) + (1 −Λ(s)) · ζ(s)
and
p(θ|s; y2) ≤
λ(θ)
Λ(s) · (1 −ζ(s)),
while for some θ such that π∗
1(s|θ) = 0,
p(θ|s; y2) ≤
ζ(s)
1 −ζ(s) · λ(θ)
Λ(s).
Therefore the belief p(·|s; yR) is no more than ξ away from p(θ; s, π∗), as
desired.
A.11
Proof of Theorem 2
Proof. We will construct a regular prior g. We will then show that for every
0 < δ < 1, there exists convex and compact sets of strategy proﬁles Ej ⊆Π•
with Ej ↓E∗⊆Bon
1 (π∗, 0)∩Bon
2 (π∗, 0) and a corresponding sequence of survival
probabilities γj →1 so that (R
g,δ,γj
1
[π2], R
g,δ,γj
2
[π1]) ∈Ej whenever π ∈Ej.
We proved in Fudenberg and He (2018) that R1 and R2 are continuous maps,
so a ﬁxed point theorem implies that for each j, some strategy proﬁle in Ej is
a steady state proﬁle under parameters (g, δ, γj). Any convergent subsequence
53


## Page 55


of these j-indexed steady state proﬁles has a limit in E∗, so this limit agrees
with π∗on path. This shows that for every δ there is a δ-stable strategy proﬁle
path-equivalent to π∗, so there is a rationally patiently stable strategy proﬁle
with the same property.
Step 1: Constructing g and some thresholds.
Since π∗induces a unique optimal signal for each sender type, by Lemma
2 ﬁnd a regular sender prior g1, 0 < ϵoﬀ< 0, and a function γLM1(δ, ϵ).
In Lemma 3, substitute ϵ = ϵoﬀto ﬁnd a regular receiver prior g2 and
0 < γLM2 < 1.
Finally, in Lemma 4 let g2 be as constructed above to ﬁnd ϵLM3 > 0 and a
function γLM3(ϵ).
Step 2: Constructing the sets Ej.
For each j, let
Ej := C ∩Bon
1 (π∗, ϵoﬀ∧ϵLM3
j
) ∩Bon
2 (π∗, ϵoﬀ∧ϵLM3
j
) ∩Boﬀ
2 (π∗, ϵoﬀ).
That is, Ej is the set of strategy proﬁles that respect rational compatibility,
diﬀer by no more than ϵoﬀ/j from π∗on path, and diﬀer by no more than ϵoﬀ
from π∗oﬀpath. It is clear that each Ej is convex and compact, and that
limj→∞Ej ⊆Bon
1 (π∗, 0) ∩Bon
2 (π∗, 0) as claimed.
We may ﬁnd an accompanying sequence of survival probabilities satisfying
γj > γLM1(δ, ϵoﬀ∧ϵLM3
j
) ∨γLM2 ∨γLM3(ϵoﬀ∧ϵLM3
j
)
with γj ↑1.
Step 3: Rg,δ,γj maps Ej into itself.
Let some π ∈Ej be given.
By Lemma 1 , R
g,δ,γj
1
[π2] ∈C.
By Lemma 3, R
g,δ,γj
2
[π1] ∈Boﬀ
2 (π∗, ϵoﬀ), because uniformity of π∗means
BR( ˆP(s), s) ⊆˜A(s) for each oﬀ-path s.
By Lemma 4, R
g,δ,γj
2
[π1] ∈Bon
2 (π∗, ϵoﬀ∧ϵLM3
j
).
Finally, from Lemma 2 and the fact that π2 ∈Bon
2 (π∗, ϵoﬀ∧ϵLM3
j
)∩Boﬀ
2 (π∗, ϵoﬀ),
we have R
g,δ,γj
1
[π2] ∈Bon
1 (π∗, ϵoﬀ∧ϵLM3
j
).
54

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1709_01024v5_payoff_information_and_learning_in_signaling_games
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1709_01024V5_PAYOFF_INFORMATION_AND_LEARNING_IN_SIGNALING_GAMES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

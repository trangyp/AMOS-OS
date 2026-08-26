---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1705.04885v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1705.04885v1_Awareness_improves_problem-solving_performance

> Source: 1705.04885v1_Awareness_improves_problem-solving_performance.pdf

> Pages: 7

---


## Page 1


Awareness improves problem-solving performance
Jos´e F. Fontanari
Instituto de F´ısica de S˜ao Carlos, Universidade de S˜ao Paulo,
Caixa Postal 369, 13560-970 S˜ao Carlos, S˜ao Paulo, Brazil
The brain’s self-monitoring of activities, including internal activities – a functionality that we
refer to as awareness – has been suggested as a key element of consciousness. Here we investigate
whether the presence of an inner-eye-like process (monitor) that supervises the activities of a number
of subsystems (operative agents) engaged in the solution of a problem can improve the problem-
solving eﬃciency of the system. The problem is to ﬁnd the global maximum of a NK ﬁtness landscape
and the performance is measured by the time required to ﬁnd that maximum. The operative agents
explore blindly the ﬁtness landscape and the monitor provides them with feedback on the quality
(ﬁtness) of the proposed solutions. This feedback is then used by the operative agents to bias their
searches towards the ﬁttest regions of the landscape. We ﬁnd that a weak feedback between the
monitor and the operative agents improves the performance of the system, regardless of the diﬃculty
of the problem, which is gauged by the number of local maxima in the landscape. For easy problems
(i.e., landscapes without local maxima), the performance improves monotonically as the feedback
strength increases, but for diﬃcult problems, there is an optimal value of the feedback strength
beyond which the system performance degrades very rapidly.
I.
INTRODUCTION
What is consciousness for? From a biological perspec-
tive, an auspicious answer to this mind-opening question
(see [1] for a thorough discussion of the theories of con-
sciousness) views consciousness as a source of informa-
tion about brain states – a brain’s schematic description
of those states – and suggests that the evolutionary use-
fulness of such inner eye is to provide human beings with
an eﬀective tool for doing natural psychology, i.e., for
imagining what might be happening inside another per-
son’s head [2]. Hence, the conception of other people as
beings with minds originates from the way each individ-
ual sees himself and, in that sense, solely extraordinar-
ily social creatures, probably humans only, would evolve
consciousness as a response to the pressures to handle
interpersonal relationships [2]. There is an alternative,
equally attractive, possibility that we may ﬁrst uncon-
sciously suppose other consciousness, and then infer our
own by generalization [3].
We note that the hypothe-
sis that consciousness is closely related to social ability
has been suggested in many forms by many authors (see,
e.g., [4–7]), but the original insight that consciousness
and cognition are products of social behaviors probably
dates back to Vygostsky in the 1930s [8].
This approach, however, is not very helpful to the en-
gineer who wants to build a conscious machine. Fortu-
nately, the recently proposed attention schema theory
of consciousness [9, 10] oﬀers some hope to our engi-
neer by positing that awareness is simply a schematic
model of one’s state of attention, i.e., awareness is an
internal model of attention.
(The intimate connection
between awareness and consciousness is expressed best
by the view that consciousness is simply the awareness
of what we have done or said, reﬂected back to us [3].)
Building a functioning attention schema is a feasible soft-
ware project today, which could then be coupled to the
existing perceptual schemas [11] to create a conscious
machine. As before, the selective value of such internal
model stems from the possibility of attributing the same
model to other people, i.e, of doing natural psychology
[10].
Internal models or inner eyes keep track of processes
that, within an evolutionary perspective, are useful to
monitor and provide feedback to (or report on) those very
same processes. This feedback can be thought of as the
mechanism by which ‘mind’ inﬂuences matter [10]. Here
we show that the inner monitoring can be useful in a more
general problem-solving scenario. (The word awareness
in the title of this paper is used with the meaning of in-
ner monitoring.) In particular, we consider a number L
of subsystems or operative agents that search randomly
for the solution of a problem, viz.
ﬁnding the global
maximum of a rugged ﬁtness landscape (see Section II),
and a single monitor that tracks the quality of the solu-
tion found by each agent (i.e., its ﬁtness) and records the
best solution at each time. The feedback to the operative
agents occurs with frequency p ≤1, i.e., on the average
each agent receives feedback from the monitor p × ∆t
times during the time interval ∆t. The feedback consists
of displaying the best solution among all agents at that
time, so the operative agents can copy small pieces of
that solution (see Section III for details).
The performance of the system composed of L oper-
ative agents and a monitor is measured, essentially, by
the time it takes to ﬁnd the global maximum of the ﬁt-
ness landscape. (Since we may want to compare perfor-
mances for diﬀerent values of L, the actual performance
measure must be properly scaled by L, as discussed in
Section III) The relevant comparison is between the case
p = 0 where the monitor has no eﬀect on the operation
of the system (a scenario akin to the doctrine of epiphe-
nomenalism [1]), and the case p > 0 where the system
receives feedback from the monitor. If the speed to solve
problems has a survival value to the individuals and if
that speed increases in the presence of feedback from the
arXiv:1705.04885v1  [cs.AI]  13 May 2017


## Page 2


2
monitor, then one may argue for the plausibility of the
evolution, as well as for the commonplaceness, of such
inner-eyes-like processes in the brain.
We ﬁnd that the performance of the system for small
values of the feedback frequency or strength p, which is
likely the most realistic scenario, is superior to the perfor-
mance in absence of feedback, regardless of the diﬃculty
of the task and of the size of the system.
This ﬁnd-
ing lends support to the inner-eye scenario for brain pro-
cesses. In the case of easy tasks (i.e., landscapes without
local maxima), the performance always improves with
increasing p, but for rugged landscapes the situation is
more complicated: there exists an optimal value of p,
which depends both on the complexity of the task and
on the system size, beyond which the system performance
deteriorates abruptly.
The rest of this paper is organized as follows. Since
the tasks of varying complexity presented to the problem-
solving system are ﬁnding the global maxima of rugged
ﬁtness landscapes generated by the NK model, in Section
II we oﬀer an outline of that classic model [12].
The
problem-solving system is then described in great detail
in Section III. We explore the space of parameters of the
problem-solving system as well as of the NK model in
Section IV, where we present and analyze the results of
our simulations.
Finally, Section V is reserved to our
concluding remarks.
II.
TASK
The task posed to a system of L agents is to ﬁnd the
unique global maximum of a ﬁtness landscape generated
using the NK model [12]. For our purposes, the advan-
tage of using the NK model is that it allows the tuning
of the ruggedness of the landscape – and hence of the
diﬃculty of the task – by changing the integer param-
eters N and K. More speciﬁcally, the NK landscape is
deﬁned in the space of binary strings x = (x1, . . . , xN)
with xi = 0, 1 and so the parameter N determines the size
of the state space, given by 2N. For each bit string x is
assigned a distinct real-valued ﬁtness value Φ (x) ∈[0, 1]
which is an average of the contributions from each ele-
ment i of the string, i.e.,
Φ (x) = 1
N
N
X
i=1
φi (x) ,
(1)
where φi is the contribution of element i to the ﬁtness of
string x.
It is assumed that φi depends on the state
xi as well as on the states of the K right neighbors
of i, i.e., φi = φi (xi, xi+1, . . . , xi+K) with the arith-
metic in the subscripts done modulo N. The parameter
K = 0, . . . , N −1 is called the degree of epistasis and
determines the ruggedness of the landscape for ﬁxed N.
The functions φi are N distinct real-valued functions on
{0, 1}K+1 and, as usual, we assign to each φi a uniformly
TABLE I. Statistics of the number of maxima in the sam-
ple of 100 NK-ﬁtness landscapes used in the computational
experiments.
N
K
mean
min max
16
0
1
1
1
16
1
8.4
1
32
16
3
84.7
26
161
16
5
292.1
235 354
12
2
13.1
4
29
20
4
633.0
403 981
distributed random number in the unit interval so that
Φ ∈(0, 1) has a unique global maximum [12].
The increase of the parameter K from 0 to N −1 de-
creases the correlation between the ﬁtness of neighboring
strings (i.e., strings that diﬀer at a single bit) in the state
space. In particular, the local ﬁtness correlation is given
by corr (x, ˜xi) = 1 −(K + 1) /N where ˜xi is the string x
with bit i ﬂipped. Hence for K = N −1 the ﬁtness values
are uncorrelated and the NK model reduces to the Ran-
dom Energy model [13, 14]. Finding the global maximum
of the NK model for K > 0 is an NP-complete problem
[15], which means that the time required to solve all re-
alizations of that landscape using any currently known
deterministic algorithm increases exponentially fast with
the length N of the strings.
However, for K = 0 the
(smooth) landscape has a single maximum that is eas-
ily located by picking for each string element i the state
xi = 0 if φi (0) > φi (1) or the state xi = 1, otherwise.
On the average, the number of local maxima increases
with increasing K. This number can be associated with
the diﬃculty of the task provided the search heuristic ex-
plores the local correlations of ﬁtness values to locate the
global maximum of the ﬁtness landscape, which is the
case of the search heuristic used in our simulations.
Since the ﬁtness values Φ (x) are random, the number
of local maxima varies considerably between landscapes
characterized by the same values of N and K > 0, which
makes the performance of any search heuristic based on
the local correlations of the ﬁtness landscape strongly
dependent on the particular realization of the landscape.
Hence we evaluate the system performance in a sample of
100 distinct realizations of the NK ﬁtness landscape for
ﬁxed N and K. In particular, we ﬁx the string length to
N = 16 and allow the degree of epistasis to take on the
values K = 0, 1, 3 and 5. In addition, in order to study
landscapes with diﬀerent state space sizes but the same
correlation between the ﬁtness of neighboring states we
consider also strings of length N = 12 and N = 20.
Table I shows the mean number of maxima, as well
as two extreme statistics, namely, the minimum and the
maximum number of maxima, in the sample of 100 land-
scapes used in the computational experiments. Although
the landscapes (N = 12, K = 2), (N = 16, K = 3) and
(N = 20, K = 4) exhibit the same local ﬁtness correla-


## Page 3


3
tion, viz. corr (x, ˜xi) = 3/4, the number of local maxima
diﬀers widely. We note, however, that the density of local
maxima decreases with increasing N provided the local
ﬁtness correlation is kept ﬁxed.
III.
MODEL
Once the task is speciﬁed we can decide on the best
representation for the operative agents that will explore
the state space of the problem.
Clearly, an appropri-
ate representation for searching NK landscapes is to por-
tray those agents as binary strings, and so henceforth we
will use the terms agent and string interchangeably. The
agents are organized on a star topology and can interact
only with a central agent – the monitor – that does not
search the state space but simply surveys and displays
the best performing string at a given moment. Figure
1 illustrates the topology of the communication network
used in the computational experiments.
FIG. 1. (Color online) Star network topology composed of L
peripheral operative agents that interact with a central agent
– the monitor. The peripheral agents search the state space
and the monitor displays the ﬁttest string at a given time.
The ﬁgure illustrates the topology for L = 20.
The L peripheral strings are initialized randomly with
equal probability for the bits 0 and 1 and the central
node displays the ﬁttest string produced in this random
setup. The search begins with the selection of one of the
peripheral agents at random – the target agent.
This
agent can choose between two distinct processes to move
on the state space.
The ﬁrst process, which happens with probability p,
is the copy of a single bit of the string displayed by the
monitor. The copy procedure is implemented as follows.
First, the monitor string and the target string are com-
pared and the diﬀerent bits are singled out. Then one of
the distinct bits of the target string is selected at random
and ﬂipped, so this bit is now the same in both strings.
The second process, which happens with probability 1−p,
is the elementary move in the state space, which consists
of picking a bit at random from the target string and
ﬂipping it. This elementary move allows the agents to
explore in an incremental way the 2N-dimensional state
space. In the case the target string is identical to the
monitor string (i.e., the ﬁttest string in the network at
that time), the target agent ﬂips a randomly chosen bit
with probability one.
After the target agent is updated, we increment the
time t by the quantity ∆t = 1/L. Since a string oper-
ation always results in a change of ﬁtness, we need to
recalculate the best string and, in case of change, update
the display of the central node.
Then another target
agent is selected at random and the procedure described
above is repeated. Note that during the increment from
t to t + 1 exactly L, not necessarily distinct, peripheral
strings are updated.
The search ends when one of the agents hits the global
maximum and we denote by t∗the halting time. The
eﬃciency of the search is measured by the total number
of peripheral string updates necessary to ﬁnd that maxi-
mum, i.e., Lt∗[16, 17] and so the computational cost of a
search is deﬁned as C ≡Lt∗/2N, where for convenience
we have rescaled t∗by the size of the state space 2N.
The parameter p measures the frequency or strength of
the feedback from the monitor (inner eye) to the periph-
eral operative agents. We note that the peripheral agents
are not programmed to solve any task: they just ﬂip bits
at random and occasionally copy a bit from the string
displayed in the central node. Only the central agent is
capable to evaluate the goodness of the solutions. But it
is not allowed to search the state space itself; its role is
simply to evaluate and display the solutions found by the
peripheral agents. This approach is akin to the Actor-
Critic model of reinforcement learning [18], in which one
part of the program – the Actor – chooses the action to
perform and the other part – the Critic – indicates how
good this action was.
The case p = 0 corresponds to
the baseline situation in which the peripheral agents do
not receive any feedback from the central agent, which,
however, still evaluates the goodness of the solutions and
halts the search when the global maximum is found.
Our model may be viewed as a simple reinterpreta-
tion of the well-studied model of distributed cooperative
problem-solving systems based on imitative learning [19–
21]. In fact, the scenario presented above is identical to
the situation where there is no central agent but each
peripheral agent is linked to all others and can imitate
the best agent in the network with probability p. In that
imitative learning scenario, any agent is able to search
the state space and evaluate the quality of its solution
as well as those of the other agents in the network. The
advantage of the present interpretation is that only one
special agent is endowed with the ability to evaluate the
quality of the solutions, which is clearly a very sophis-
ticated process that should be kept separated from the
more mechanical state space search. Following the so-
cial brain reasoning line, the organisms have probably
ﬁrst evolved variants of this evaluative process to access
their external environment, which includes the other or-


## Page 4


4
ganisms, and then modiﬁed those processes for internal
evaluation. In the present interpretation, the system ex-
hibited in Fig. 1 is a module of the cognitive system of
a single organism, whereas in the imitative learning sce-
nario each agent is seen as an independent organism.
IV.
RESULTS
As a measure of the performance of the system in
searching for the global maximum of the NK landscapes,
we consider the mean computational cost ⟨C⟩, which is
obtained by averaging the computational cost over 105
distinct searches for each landscape realization, and the
result is then averaged over 100 landscape realizations.
In addition to this performance measure, we carry out
diverse measurements to get insight on the diversity of
the strings at the halting time t∗. In particular, deﬁn-
ing the normalized Hamming distance between the bit
strings xα and xβ as
d
 xα, xβ
= 1
2 −1
2N
N
X
i=1
(1 −2xα
i )

1 −2xβ
i

,
(2)
we can introduce the mean pairwise distance between the
L strings in the system,
¯d =
2
L (L −1)
L−1
X
α=1
L
X
β=α+1
d
 xα, xβ
.
(3)
This distance can be interpreted as follows: if we pick
two strings at random, they will diﬀer by N ¯d bits on
average. Hence ¯d yields a measure of the dispersion of
the strings in the state space. The distance ¯d must also
be averaged over the independent searches and landscape
realizations, resulting in the measure ⟨¯d⟩.
We note that many applications of social heuristics to
solve combinatorial problems (see, e.g., [16, 17, 22, 23])
resort to circuitous representations for the agents as well
as for their moves on the state space, making it diﬃcult to
gauge the complexity, or lack thereof, of the tasks solved
by those heuristics. The advantage of using NK land-
scapes is that we can control the diﬃculty of the tasks
and, accordingly, in Fig. 2 we show the mean computa-
tional cost for tasks of diﬀerent complexities.
In the case of single-maximum landscapes (K = 0),
copying the ﬁttest string displayed by the central node
is an optimal strategy since it guarantees, on the aver-
age, a move towards the maximum. This is the reason
that for a ﬁxed system size L the best performance is
achieved for p = 1. However, the regime of small p is
probably the more relevant since one expects that the
feedback between the monitor and the operative agents
should happen much less frequently than the motion in
the state space.
The presence of local maxima (K > 0) makes copying
the central node string a risky strategy since that string
may display misleading information about the location of
 0.003
 0.01
 0.1
 1
 2
 0
 0.2
 0.4
 0.6
 0.8
 1
< C >
p
FIG. 2. (Color online) Mean computational cost ⟨C⟩as func-
tion of the strength p of the feedback between the monitor
and the operative agents for the system size L = 20 and (bot-
tom to top) K = 0, 1, 3 and 5. The length of the bit strings is
N = 16. Note the logarithmic scale of the axis of ordinates.
the global maximum. In fact, the disastrous performance
observed for large p is caused by the trapping in the local
maxima, from which escape can be extremely costly. The
culprit of the bad performance is a groupthink-like phe-
nomenon, which occurs when people put unlimited faith
in a leader and so everyone in the group starts thinking
alike [24]. Interestingly, the results of Fig. 2 shows that
for K > 0 there is a value p = popt that minimizes the
computational cost and is practically unaﬀected by the
complexity of the task. However, as we will see in the
following, popt decreases with increasing L and increases
with increasing N.
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0
 0.2
 0.4
 0.6
 0.8
 1
< d- >
p
FIG. 3. (Color online) Mean pairwise Hamming distance ⟨¯d⟩
measured when the search halts as function of the feedback
strength p for the system size L = 20 and (bottom to top at
p = 0.4) K = 0, 1, 3 and 5. The length of the bit strings is
N = 16.
Figure 3 oﬀers a view of the distribution of strings in
the state space at the moment t = t∗that the global
maximum is found.
For a ﬁxed task complexity (i.e.,
for a ﬁxed K), the mean pairwise Hamming distance ⟨¯d⟩


## Page 5


5
is a monotonically decreasing function of p, so that the
strings become more similar to each other as p increases,
as expected. In addition, for K > 0 this function has
an inﬂection point at p ≈popt. Somewhat surprisingly,
these results show that for p < popt the spreading of the
strings in the state space is greater in the case of diﬃcult
tasks, which is clearly a good strategy to circumvent the
local maxima.
This behavior is reversed in the region
where the computational cost is extremely high, indicat-
ing that a large number of strings are close to the local
maxima when the global maximum is found. We know
that because we have measured also the mean Hamming
distance to the global maximum and found that this dis-
tance is greater than the typical distance between two
strings.
 0
 0.4
 0.8
 1.2
 1.6
 2
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
< C >
p
FIG. 4. (Color online) Mean computational cost ⟨C⟩as func-
tion of the strength p of the feedback between the monitor and
the operative agents for three families of NK landscapes (left
to right at ⟨C⟩= 1.2): (N = 12, K = 2), (N = 16, K = 3)
and (N = 20, K = 4) which exhibit the same mean local ﬁt-
ness correlation. The mean density of local maxima is 0.0032,
0.0013 and 0.0006, respectively. The system size is L = 20.
To look at the eﬀect of the state space size N on the
performance of the system it is convenient to vary K
as well so as to keep the local ﬁtness correlation of the
landscapes unchanged. Figure 4 shows the mean com-
putational cost for three families of NK landscapes with
local ﬁtness correlation equal to 3/4 for a ﬁxed system
size. Since variation of K does not aﬀect the value of the
optimal feedback strength (see Fig. 2), the change of popt
observed in the ﬁgure is due to the variation of the pa-
rameter N. The ﬁnding that popt, as well as the quality
of the optimal computational cost, increases with the size
of the problem space indicates that the trapping eﬀect of
the local maxima is due to the density of those maxima
and not to their absolute number (see Table I). We note
that the case p = 0 can be solved analytically (see [20])
and the reason that for ﬁxed L ≪2N the computational
cost decreases with N is that the chance of reverting spin
ﬂips (and hence wasting moves) decreases as the length
of the strings increases. Only in the limit N →∞the
probability of reverting ﬂips is zero, so that ⟨C⟩= 1 in
that limit.
 0
 0.4
 0.8
 1.2
 1.6
 2
 0
 0.2
 0.4
 0.6
 0.8
< C >
p
FIG. 5. (Color online) Mean computational cost ⟨C⟩as func-
tion of the strength p of the feedback between the monitor and
the operative agents for diﬀerent system sizes (top to bottom
at p = 0.2) L = 10, 20, 40 and 80.
The parameters of the
rugged NK landscape are N = 16 and K = 3.
In order to oﬀer the reader a complete view of the be-
havior of the system, in Fig. 5 we show the computational
cost for diﬀerent system sizes L. The results show that
the optimal feedback popt decreases with increasing L but
the quality of the optimal cost is not very sensitive to the
system size. This ﬁgure reveals also the nontrivial inter-
play between the system size L and the feedback strength
p. In fact, for each p there is an optimal system size that
minimizes the computational cost [20]. This optimal size
decreases from inﬁnity for p →0 to L = 2 for p = 1.
Finally, we note that since ﬁnding the global maxima of
NK landscapes with K > 0 is an NP-Complete problem
[15], one should not expect that the imitative search (or
any other search strategy, for that matter) would ﬁnd
those maxima much more rapidly than the independent
search for a large sample of landscape realizations as that
considered here.
V.
DISCUSSION
Theories of consciousness are typically expressed ver-
bally and stated in somewhat vague and general terms
even by the standards of philosophical theories. For in-
stance, many notorious thought experiments of the ﬁeld
(e.g., Mary’s room [25] and the philosopher’s zombie [26])
have multiple interpretations because their speciﬁcations
are unclear [27] and even the so-called ‘hard problem’ of
consciousness (i.e., how physical processes in the brain
give rise to subjective experience [26]) is viewed by some
researchers as a hornswoggle problem [28] and a major
misdirection of attention [29].
Perhaps what is missing is an eﬀort to express theories
of consciousness, or at least some of their premises, as
computer programs [30]. This would require a complete
and detailed speciﬁcation of all assumptions, otherwise


## Page 6


6
the program would not run in the computer [31]. (Of
course, this research program does not apply to those the-
ories that are built on the premise of the impossibility of
such a computer simulation.) With very few exceptions
(see, e.g., [32]) computer simulations and mathematical
models have greatly aided the elucidation of nonintuitive
issues on Evolutionary Biology [33], and we see no in-
trinsic reason that could prevent the use of those tools
to verify assumptions and predictions of theories of con-
sciousness, particularly of those theories that grant a se-
lective value to consciousness.
In this paper we explore a key element of the theo-
ries that view consciousness as a schematic description of
the brain’s states, namely, the existence of inner-eye-like
processes that monitor those states and provide feedback
on their suitability to the attainment of the organism’s
goals [2, 10]. We use a cartoonish model of this scenario,
in which a group of operative agents search blindly for
the global maximum of a ﬁtness landscape and a monitor
provides them with feedback on the quality (ﬁtness) of
the proposed solutions. This feedback is then used by
the operative agents to bias their searches towards the
(hopefully) ﬁttest regions of the landscape. We interpret
this self-monitoring as the awareness of the system about
the computation it is carrying out.
We ﬁnd that a weak feedback between the monitor
and the operative agents improves the performance of
the system, regardless of the diﬃculty of the task, which
is gauged by the number of local maxima in the land-
scape. In the case of easy tasks (i.e., landscapes without
local maxima), the performance improves monotonically
as the feedback strength increases, but for diﬃcult tasks
too much feedback leads to a disastrous performance (see
Fig. 2). Of course, one expects that the value of the feed-
back strength, which measures the inﬂuence of the inner-
eye process on the low-level cognitive processes, will be
determined by natural selection and so it is likely to be
set to an optimal value that guarantees the maximization
of the system performance.
In closing, our ﬁndings suggest that the inner-monitor-
ing of the system behavior (computations, in our case),
which is a key element in some theories of consciousness
[2, 10], results in an improved general problem-solving
capacity. However, if a system that, in the words of Den-
nett [27], “... monitors its own activities, including even
its own internal activities, in an indeﬁnite upward spiral
of reﬂexivity” can be said to be conscious is an issue that
is best left to the philosophers,
ACKNOWLEDGMENTS
The research of JFF was supported in part by grant
15/21689-2, S˜ao Paulo Research Foundation (FAPESP)
and by grant 303979/2013-5, Conselho Nacional de De-
senvolvimento Cient´ıﬁco e Tecnol´ogico (CNPq).
[1] Blackmore, S., 2003. Consciousness:
An Introduction.
Oxford University Press, Oxford.
[2] Humphrey, N., 1999. A History of the Mind: Evolution
and the Birth of Consciousness. Copernicus Press, New
York.
[3] Jaynes, J., 1976. The origin of consciousness in the break-
down of the bicameral mind. Houghton Miﬄin, Boston.
[4] Frith, C., 1995. Consciousness is for other people. Behav.
Brain. Sci. 18, 682–683.
[5] Perlovsky, L., 2006. Toward physics of the mind: Con-
cepts, emotions, consciousness, and symbols. Phys. Life
Rev. 3, 23–55.
[6] Carruthers, P., 2009. How we know our own minds:
the relationship between mindreading and metacogni-
tion. Behav. Brain. Sci. 32, 121–138.
[7] Baumeister, R.F., Masicampo, E.J., 2010. Conscious
thought is for facilitating social and cultural interactions:
how mental simulations serve the animal-culture inter-
face. Psychol. Rev. 117, 945–971.
[8] Vygotsky, L.S., 1986. Thought and Language. The MIT
Press, Cambridge, MA.
[9] Graziano, M., Kastner, S., 2011. Human consciousness
and its relationship to social neuroscience: A novel hy-
pothesis. Cogn. Neurosci. 2, 98–113.
[10] Graziano, M., 2013. Consciousness and the Social Brain.
Oxford University Press, Oxford, UK.
[11] Murphy, R.R., 2000. Introduction to AI Robotics. MIT
Press, Cambridge, MA.
[12] Kauﬀman, S.A., Levin, S., 1987. Towards a general the-
ory of adaptive walks on rugged landscapes. J. Theor.
Biol. 128, 11–45.
[13] Derrida, B., 1981. Random-energy Model: An Exactly
Solvable Model of Disordered Systems. Phys. Rev. B 24,
2613–2626.
[14] Saakian, D.B., Fontanari, J.F., 2009. Evolutionary dy-
namics on rugged ﬁtness landscapes: exact dynamics and
information theoretical aspects, Phys. Rev. E 80, 041903.
[15] Solow, D., Burnetas, A., Tsai, M., Greenspan, N.S., 2000.
On the Expected Performance of Systems with Complex
Interactions Among Components. Complex Systems 12,
423–456.
[16] Clearwater, S.H., Huberman, B.A., Hogg, T., 1991. Co-
operative Solution of Constraint Satisfaction Problems.
Science 254, 1181–1183.
[17] Clearwater, S.H., Hogg, T., Huberman, B.A., 1992. Co-
operative Problem Solving. In: Huberman, B.A. (Ed.),
Computation: The Micro and the Macro View. World
Scientiﬁc, Singapore, pp. 33–70.
[18] Barto, A.G., 1995. Adaptive critic and the basal ganglia.
In: Houk, J.C., Davis, J.L., Beiser D.G. (Eds.), Models of
information processing in the basal ganglia. MIT Press,
Cambridge, pp. 215 –232.
[19] Fontanari, J.F., 2014. Imitative Learning as a Connector
of Collective Brains. PLoS ONE 9, e110517.
[20] Fontanari, J.F., 2015. Exploring NK Fitness Landscapes
Using Imitative Learning. Eur. Phys. J. B 88, 251.


## Page 7


7
[21] Fontanari, J.F., 2016. When more of the same is better.
EPL 113, 28009.
[22] Kennedy, J., 1998. Thinking is social: Experiments with
the adaptive culture model. J. Conﬂict Res. 42, 56–76.
[23] Fontanari, J.F., 2010. Social interaction as a heuristic
for combinatorial optimization problems. Phys. Rev. E
82, 056118.
[24] Janis, I.L., 1982. Groupthink: psychological studies of
policy decisions and ﬁascoes. Houghton Miﬄin, Boston.
[25] Jackson, F., 1982. Epiphenomenal Qualia. Phil. Q. 32,
127–136.
[26] Chalmers, D., 1996. The Conscious Mind: In Search of a
Fundamental Theory. Oxford University Press, Oxford.
[27] Dennett, D.C., 1991. Consciousness Explained. Little,
Brown and Company, Boston.
[28] Churchland, P.S., 1996. The Hornswoggle problem. J.
Conscious. Stud. 3, 402–408.
[29] Dennett, D.C., 1996. Facing backwards on the problem
of consciousness. J. Conscious. Stud. 3, 4–6.
[30] Perlovsky, L., 2001. Neural Networks and Intellect: Using
Model-Based Concepts. Oxford University Press, Oxford.
[31] Cangelosi, A., Parisi, D., 2002. Computer Simulation: A
New Scientiﬁc Approach to the Study of Language Evo-
lution. In: Cangelosi, A., Parisi, D. (Eds.), Simulating
the Evolution of Language. Springer, London, pp. 3–28.
[32] Santos, M., Szathm´ary, E., Fontanari, J.F., 2015. Pheno-
typic Plasticity, the Baldwin Eﬀect, and the Speeding up
of Evolution: the Computational Roots of an Illusion. J.
Theor. Biol. 371, 127–136.
[33] Dawkins, R., 1986. The Blind Watchmaker. Oxford Uni-
versity Press, Oxford.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1705_04885v1_awareness_improves_problem_solving_performance
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1705_04885V1_AWARENESS_IMPROVES_PROBLEM_SOLVING_PERFORMANCE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

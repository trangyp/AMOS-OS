---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1812.00718v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1812.00718v1_Finding_Continuity_and_Discontinuity_in_Fish_Schools_via_Integrated_Information_

> Source: 1812.00718v1_Finding_Continuity_and_Discontinuity_in_Fish_Schools_via_Integrated_Information_.pdf

> Pages: 32

---


## Page 1


FINDING CONTINUITY AND DISCONTINUITY IN FISH SCHOOLS
VIA INTEGRATED INFORMATION THEORY
A PREPRINT
Takayuki Niizato
Faculty of Engineering, Information and Systems
University of Tsukuba, Japan
t_niizato@yahoo.co.jp
Kotaro Sakamoto∗
Human Biology Program
University of Tsukuba, Japan
sakamoto@ccs.tsukuba.ac.jp
Yoh-ichi Mototake
Graduate School of Frontier Sciences
University of Tokyo, Japan
Hisashi Murakami
Research Center for Advanced Science and Technology
University of Tokyo, Japan
Takenori Tomaru
Department of Computer Science and Engineering
Toyohashi University of Technology, Japan
Tomotaro Hoshika
Faculty of Engineering, Information and Systems
University of Tsukuba, Japan
Toshiki Fukushima
Faculty of Engineering, Information and Systems
University of Tsukuba, Japan
December 4, 2018
ABSTRACT
Collective behaviour is known to be the result of diverse dynamics and is sometimes likened to a
living system. Although many studies have revealed the dynamics of various collective behaviours,
their main focus was on the information process inside the collective, not on the whole system
itself. For example, the qualitative difference between two elements and three elements as a system
has rarely been investigated. Tononi et al. have proposed Integrated Information Theory (IIT) to
measure the degree of consciousness Φ. IIT postulates that the amount of information loss caused by
certain partitions is equivalent to the degree of information integration in the system. This measure is
not only useful for estimating the degree of consciousness but can also be applied to more general
network systems. Here we applied IIT (in particular, IIT 3.0 using PyPhi) to analyse real ﬁsh
schools (Plecoglossus altivelis). Our hypothesis in this study is a very simple one: a living system
evolves to raise its Φ value. If we accept this hypothesis, IIT reveals the existence of continuous and
discontinuous properties as group size varies. For example, leadership in the ﬁsh school emerged for
a school size of four or above; but not below three. Furthermore, this transition was not observed
by measuring mutual information or in a simple Boids model. This result suggests that integrated
information Φ can reveal some inherent properties which cannot be observed using other measures.
We also discuss how the ﬁsh recognition of the ﬁgure-ground relation, that is, what determines the
relevant ON and OFF states, may reveal various optimal paths for obtaining the functional evolution
of collective behaviour.
Keywords Collective Behaviour, · Integrated Information Theory
∗This author contributed equally to this work.
arXiv:1812.00718v1  [physics.soc-ph]  3 Dec 2018


## Page 2


A PREPRINT - DECEMBER 4, 2018
1
Introduction
Collective behaviour, such as swarming [1, 2, 3, 4, 5, 6], ﬁsh schooling[7, 8, 9, 10, 11] and bird ﬂocking [12, 13, 14, 15,
16, 17] has been widely observed in nature [18, 19, 20, 21]. In some instances, individuals respond to the changing
environment rapidly as one collective [14, 15, 16] and, in other cases, relatively good decision-making is achieved as
a group [22, 23, 24]. Conﬂicts among individuals, as seen by an external observer, do not necessarily lead to group
disruption; instead, they show the way to more an effective response as a group [25, 26]. The unity of this kind of
animal behaviour remains one of the mysteries of nature [18].
Self-organised criticality (SOC) has been a good metaphor for interpreting these collective animal behaviours. If
the group is in the intermediate state between order and disorder, it becomes possible to achieve enough ﬂexibility
and robustness as one system [27, 28, 29, 30, 31, 32]. For example, the perturbations of ﬂocks (or swarms) in SOC
models optimise the effective correlation range of each bird and make it possible to accomplish fast information transfer
[13, 14, 15, 16]. However, when it comes to considering small groups, the same method cannot be applied, because,
it is hard to assume that the interactions of individuals are homogeneous [33, 34]. In particular, with regard to the
subject of this study, it is conceivable that the interactions of two- and three-ﬁsh groups may be different [35, 36].
Many researchers, therefore, have considered information transfer (or causal relationships) among individuals in small
groups[37, 38, 39]. The (local) transfer entropy is the preferred measure to use in this case[40, 41, 42, 43, 44, 45]. For
example, Crosato et al. [39] showed that the transfer of misinformation happens in ﬁve-ﬁsh school when the whole
school changes direction. Other studies suggest that active information storage can predict the timing when nontrivial
information transfer happens [46, 47]. Although the latter approaches also promise to give us a tremendous amount
of information about what is happening in the group, they will not give us the information about what the system
of collective behaviour is [48]. The SOC approach certainly captures some aspects of what the system of collective
behaviour is, but it gives little information about the causal structures inside the groups.
Before we go into detail about the difference between what is happening and what the system is, we need to introduce
the concept of integrated information theory (IIT). IIT, which Tononi and other researchers have proposed, has been a
rapidly developing area over the last two decades [49, 50, 51, 52, 53, 54, 55]. The original aim was to estimate the
degree of consciousness from brain activity [49, 50]. Recent studies suggest that IIT can capture and discriminate
between various states of lost consciousness, such as dreamless sleep [56], general anaesthesia [57] or vegetative states
[58]. Although IIT has several versions, its core concept is the same in principle, that is, the integrated information (Φ)
is deﬁned as the degree of information loss caused by a certain partition of the system [50, 54](in the case of Barrett and
Seth’s version of IIT, Φ is the degree of the increase of uncertainty caused by a certain partition[51]. A computational
comparison of many versions of IIT has been made by Mediano [59]). It is worth noting that Ito [60, 61] has pointed
out the fact that there are some intimate relations between the second law of information thermodynamics and IIT in
terms of a projection onto a local reversible manifold. These structural resemblances suggest the possibility of unifying
the concept of non-equilibrium thermodynamics and IIT.
The key concept of IIT is that the whole cannot be reduced into its separated parts because the lost information would
contain synergetic information produced by those parts. In this respect, the concept of IIT resonates with that of
complex systems [62], for which the statement ”the whole is more than the sum of its parts” has long been a slogan
[63]. Since the intrinsic causal structures make the system irreducible into its parts, the integrated information (or Φ)
also can be a measure of the degree of wholeness as a single autonomous system[64].
There have been some applications of IIT to cellular automaton[48], animat [65] and Boolean networks [66]. For
example, Albantakis et al. [48] showed that average Φ values for 5 to 6 cells correlated well with their complexity,
such as class III and IV, despite the very small number of cell sets. (The behaviours of 5 and 6 cells can be hardly
discriminated on the basis of the behaviours of their constituent cells and, in general, the behaviours of small numbers
of cellular automata are very similar to an external observer.) They also showed that all rules of class IV have all orders
of concepts (i.e. irreducible subsets in the system) unlike other classes.
The example of cellular automata illuminates the meaning of intrinsic properties for IIT. IIT reveals the differences
among systems arising from different intrinsic causal structures (rules), rather than considering differences based on
external behaviour. That is why we said previous approaches (especially, transfer entropy) captured not what the system
is but what is happening. Now we can ask the following question: What is the difference of collective behaviour in terms
of the intrinsic causal structure perspective? In this paper, we ask the following: Does the number of agents in a system
make its intrinsic properties different? In other words, if the group size changes, what remains the same (continuous)
and what changes (discontinuous) in the group? Also, are any new factors introduced, which were not present before?
This kind of question is rarely asked in animal collective behaviour, but one study suggests that schools of three ﬁsh and
schools of two ﬁsh have different kinds of interactions [35, 36]. Another suggests that the search strategies of ﬁsh in
groups of different sizes are essentially different when they are in an unfamiliar environment [11]. However, all these
2


## Page 3


A PREPRINT - DECEMBER 4, 2018
studies constrain the number of individuals in the group to three or less and their methods are difﬁcult to generalise
to larger groups. Furthermore, these methods never indicate any differences in terms of the group’s intrinsic causal
structure.
In this paper, we apply IIT (in particular, IIT 3.0 using PyPhi [52, 55]) to schools of two to ﬁve ﬁsh (Plecoglossus
altivelis) and show the intrinsic differences between these groups. To apply IIT to the collective behaviour of animals,
we propose a simple hypothesis, namely, that a living system evolves to raise its integrated information. This hypothesis
is not a peculiar one because some studies have suggested that, for some artiﬁcial systems selected by their ﬁtness,
Φ values were correlated with ﬁtness [48]. Thus, to raise Φ means to raise ﬁtness in a given environment. Adopting
this hypothesis, we found that there is a kind of continuity and discontinuity with respect to school size. The main
ﬁnding is that there is a discontinuity between three- and four-ﬁsh schools, which is a difference that hasn’t received
a lot of attention previously. Interestingly, the difference between these two systems corresponds to the existence of
leadership (more precisely, reducing the ﬁeld of view for ﬁsh’s recognition introduces the existence of the leadership).
Furthermore, our results are never replicated by a Boids-type model for the same conditions.
2
Results
2.1
Deﬁnition to apply IIT to ﬁsh schools
To apply IIT 3.0, we deﬁne ON and OFF states of an individual in a ﬁsh school. In this paper, the ON state means some
interaction would occur in a given context. For example, if two individuals are within a certain radius, the state of both
individuals are ON (some information transfer would occur between them). This is a symmetric interaction. In the same
way, we consider two other interactions to deﬁne ON and OFF states for ﬁsh in the school: visual ﬁeld and turning rate
interactions (see Fig. 1). A visual ﬁeld interaction means the individual is in the ON state when some other agents are
within its visual ﬁeld. This allows us to consider asymmetrical relations in contrast to the symmetric distance condition.
The turning rate interaction is one in which a direction change above a certain value puts the individual in the ON
state. This ON state transfers information to other agents in the next time step, so the interaction between individuals
is a delayed one. The direction changing rate is a very important measure for collective behaviour, empirically and
theoretically [67, 21, 8].
In this paper, we assume a ﬁsh always evaluates these three kinds of information simultaneously. So, we take conjugation
(i.e. AND) of the obtained 3 bits of information (for instance, IF Distance:ON, Visual ﬁeld:ON, Turning rate:OFF,
THEN state OFF) to produce an overall state for a ﬁsh. Applying the same process to each ﬁsh at a time t, we obtain
the time series of the states of the n-ﬁsh. Then we can compute Φ and other values (the number of concept) from the
obtained time series. One time step, in this paper, is deﬁned as 0.05 (0.10, 0.20) s. This value roughly corresponds to
the ﬁsh’s reaction timescale [39].
To compute Φ, we also deﬁne the network structure in the school. In this paper, we postulate the completely connected
network not including self-loops. This assumption comes from the experimental fact that each ﬁsh has some contact
with (or falls within the visual ﬁeld of) all individuals in the group during the long series of recorded events (10-15
min). Therefore, it is natural to assume that some interactions happened among all members (In Table S1, we give the
minimal distance throughout the events. The data shows all ﬁsh have a contact within 5mm).
Before we go into detail about our analysis, it is necessary to understand what the states ON and OFF mean for the ﬁsh.
Biological information systems, such as the brain have an explicit ON state, that is, ﬁring neurons. In contrast, the ON
state for each ﬁsh is its recognition of a certain environment, that is, it is the state of a characteristic factor to which
each ﬁsh pays attention. Since there are various kinds of information to take into account, there is no explicit ON state
in ﬁsh school. (This kind of ambiguity is not a demerit of our analysis. We will come back this issue in the Discussion.)
2.2
Φ values for local parameter settings
First, we conﬁrmed the fact that Φ increases with group size (from two to ﬁve ﬁsh) on average. This trend is also
observed in the Boids model (with the same parameter setting, see Table S2) but values are higher than those for real
ﬁsh schools. This result is a very natural one because the degree of integrity becomes high when each agent keeps their
distance almost constant and moves as one collective throughout the series of events. Compared with the Boids model,
ﬁsh in the real ﬁsh school connect more loosely with each other. As a result, Φ for real ﬁsh schools is smaller than in
models.
Fig. 2 shows that a qualitative change occurs when group size increases from three to four. Apparently, Φ values in two-
and three-ﬁsh groups depend only on the distance threshold and not on the visual ﬁeld. It appears that the leadership
relation is not so important for ﬁsh groups smaller than 4 (an enlarged version of Fig. 2 is given as ??). Leadership
3


## Page 4


A PREPRINT - DECEMBER 4, 2018
emerges when the group size is four or more. Interestingly, this trend is not observed in the Boids model and in the
mutual information model. (See Figs. 6 and 8(a). Fig. 10 shows other parameter settings.) Furthermore, if we take a
time step of 0.1 and 0.2 s instead of 0.05 s, the same tendency observed in almost cases (from Figs.11 to 13). Two-ﬁsh
groups show high values around Field of View = (1/5)π (rad) and Distance=200(mm) (Fig. 11 and 13). The leadership
relation that emerges is, however, essentially different from that in large groups. This kind of behaviour may be called
“followership” because the very narrow visual ﬁelds lead individuals to target the ﬁsh swimming ahead of him.
Fig. 3 is an example of a time series of Φ. The abrupt reductions of Φ values correspond to the emergence of leadership.
In IIT 3.0, the emergence of leadership never raises the Φ value; it always decreases it. Leadership decreases the
integrity of the school because, if we cut between a leader and its followers, the integrity of the whole will be disrupted.
So, the emergence of leadership itself raises Φ values on average (the highest Φ value corresponds when all ﬁsh are in
the ON state); however, they decrease Φ values as a single state.
We also ﬁnd that the turning rate is not so important for determining Φ values for cases with a short timescale (∆t = 0.05
s). However, turning rate becomes important information for long timescale events (see Fig. 11 and 13). Over a short
timescale, relative positional information seems the most important for raising Φ values.
The other intriguing measure is the number of concepts. Concepts are one of the critical notions in IIT 3.0 because Φ
values are determined by their distribution in a conceptual space. A concept is, in short, the ability of “difference makes
difference” as a subsystem. (Further explanation is given in the”Integrated information Φ” and ”Concept” sections in
the Supporting Information). If a system contains many concepts (up to 2n −1 concepts exist for n elements), that
system has many irreducible components (i.e. it cannot be decomposed into its parts) as subsystems. The importance of
the number of concepts can be observed in elementary cellular automata. The rule which shows class IV behaviour has
all orders of concept unlike other classes [48].
We found that there are areas that are rich in concepts despite low Φ values (Figs.S10 and S11). Combined with the
results shown Fig. 2, we can distinguish three types of combination, that is, low Φ and few concepts, high Φ and many
concepts, and low Φ and many concepts (there are no examples of the combination of high Φ and few concepts in our
study). The most interesting case is the combination of low Φ and many concepts. These areas tend to get high Φ values
if the number of ﬁsh increases. This observation suggests that low Φ values and many concepts provides the possibility
of evolution if the condition (or environment) changes. (We also examined other measures. See 15 to Fig. 16.)
2.3
Φ values for global parameter settings
Next, we deﬁned the ON and OFF states globally rather locally. That is, the states are determined by global measures
of interaction rather than local ones, as previously. For this, we considered the average direction and the centre of
mass. When the difference between a ﬁsh’s direction and the average direction of the ﬁsh school is within a certain
speciﬁed value, its state is ON (see Fig. 4). Similarly, when each ﬁsh’s distance from the centre of mass of the school is
smaller than a certain speciﬁed value, its state is ON. The main difference from the previous state deﬁnition is that
these parameters require the existence of a single group to be postulated a priori. These values will make no sense
if the group is divided into two groups. (It is possible that two independent coherent groups will be incoherent when
considered as a whole.)
As in the local case, Φ values also rise with group size (Fig. 5). This tendency is also observed in the Boids model.
(Note, in particular, that the distribution of two-ﬁsh groups in the Boids model is very different from that of real two-ﬁsh
schooling. See Fig. 8(b)). The main difference between local and global measures is the discontinuity occurs at a
different point, that is, between two ﬁsh and three ﬁsh. The discontinuity between three- and four-ﬁsh schools is never
observed for the global parameters. In this sense, three- and four-ﬁsh schools are continuous with respect to the global
parameters.
3
Discussion
In this study, we applied IIT 3.0 to real ﬁsh schools and compared the results with those for another measure (mutual
information) and another model (Boids) under the same conditions. Our results suggest the degree of integration Φ
might pick up some unique information about real ﬁsh schools. From the Φ distributions derived with a certain set of
parameters, we found a discontinuity between three- and four-ﬁsh school with local parameter setting but continuity
with global setting: the recognition of leadership raises the degree of integrity above four but not below three. Changing
the timescale from 0.05s to 0.2s, we conﬁrmed the emergence of “followership” rather than leadership in two-ﬁsh
groups (Fig. 11 and 13). Therefore, their intrinsic causal structures are clearly distinct in terms of IIT, although two-
and four-ﬁsh schools may exhibit leadership as a group.
4


## Page 5


A PREPRINT - DECEMBER 4, 2018
This result is consistent with Albantakis’s argument that IIT captures “what a dynamical system is from its own intrinsic
perspective” (or “how much and in which way it exists for itself, independent of an external observer”) rather than
“what is happening in a system from extrinsic perspective of an observer”[48]. Along the lines of this statement, we can
say the emergence of leadership represents what the system of a ﬁsh school is with respect to its group size. It is worth
noting that IIT discriminates between three- and four-ﬁsh groups, which is a comparison that is rarely considered in
the context of collective animal behaviour, although there are some studies that suggest a difference between two- and
three-ﬁsh groups in terms of each ﬁsh’s interactions with others (i.e. a difference in what is happening in the system
from an extrinsic perspective’) [35, 36, 11].
Finally, we comment on the relation between animal recognition systems and the evolution of collective animal
behaviour. In this paper, we have hypothesised that living systems evolve to raise their Φ value. This hypothesis itself is
not a peculiar one because some studies have shown that the ﬁtness of artiﬁcial systems, such as Animats and genetic
Boolean networks, is correlated with Φ [65, 48, 66]. Simple biological systems also show some connections between
their functional units and Φ values (or their concepts) [66]. For example, in our study, the emergence of leadership in
groups of four ﬁsh or more means each individual chooses to reduce its ﬁeld of view in the group to raise Φ values
(Fig. 2 shows the peak of Φ values of a ﬁve-ﬁsh group, indeed, shifting to make the ﬁeld of view smaller than that of a
four-ﬁsh group).
In our analysis, the factor which determines what is ON and OFF is a ﬁsh’s recognition of its environment. In contrast
with brain systems, ON states are dominant in a ﬁsh school. This fact means the OFF states are more informative than
the ON states. The ON states, especially for local parameter settings, are important because the all-ON state for a
school means all ﬁsh recognise that they are part of the same group. That is why the state of leadership (one ﬁsh in the
group is the OFF state) reduces Φ.
We have conﬁrmed that leadership never raises Φ when the group size is three or less. This fact indicates the two- and
three-ﬁsh groups tend to show ﬁssion-fusion behaviour rather than leadership. In addition to this, three-ﬁsh schools can
be said to be a kind of tipping point from a local to a global collective. From the view of the local perspective (local
parameter settings), there seems to be no advantage for the group when a two-ﬁsh school becomes a three-ﬁsh school
because Φ values never rise in this condition. On the other hand, from the global perspective (global parameter settings),
increasing the group size from two to three means increasing Φ values. Therefore, the recognition of what is ON or
OFF in those systems would change the Φ values radically and help the group to ﬁnd its way to other optimal states of
Φ values for other recognition. Our results suggest the evolution of real autonomic systems would become possible
through IIT.
In this study, we avoided going deeply into the problem of timescale (we only used a relatively small timescale, which
is roughly equal to a general ﬁsh’s reaction time). Over longer timescales, other patterns of continuity and discontinuity
may be found. Increasing the number of individuals may also give other results. However, the present practical
computational limit of IIT 3.0 is around 7 or 8 individuals/neurons [55], so some approximations will be needed to
implement further analysis. Another area we didn’t address is network structure. We supposed an all-connected network
without self-loops in this paper because all ﬁsh came into contact with each other throughout the event. This will not
always be true for large groups. Furthermore, some studies suggests that the network structure of real schools of ﬁsh is
radically different from the Boids model one, and that they make a stable network called the α-lattice [68, 69]. This
type of network may prevent Φ-raising trends observed in the Boids model.
4
Methods
4.1
Ethics statement
This study was carried out in strict accordance with the recommendations in the Guide for the Care and Use of
Laboratory Animals of the National Institutes of Health. The protocol was approved by the Committee on the Ethics
of Animal Experiments of the University of Tsukuba (Permit Number: 14-386). All efforts were made to minimize
suffering.
4.2
Φ computation
All
computations,
in
this
paper,
were
performed
using
the
PyPhi
software
package
with
the
CUT_ONE_APPROXIMATION to Φ.
5


## Page 6


A PREPRINT - DECEMBER 4, 2018
4.3
Experimental Settings
We studied ayus (Plecoglossus altivelis), also known as sweetﬁsh, which live throughout Japan and are widely farmed
in Japan. Juvenile ayus (approximately 7-14 cm in body length) display typical schooling behaviour, though adult
ayus tend to show territorial behaviour in environments where ﬁsh density is low. We purchased juveniles from
Tarumiyoushoku (Kasumigaura, Ibaraki, Japan) and housed them in a controlled laboratory. Approximately 150 ﬁsh
lived in a 0.8 m3 tank of continuously ﬁltered and recycled fresh water with a temperature maintained at 16.4◦C, and
were fed commercial food pellets. Immediately before each experiment was conducted, randomly chosen ﬁsh were
separated to form a school of each size and were moved to an experimental arena without pre-training. The experimental
arena consisted of a 3×3m2 shallow white tank. The water depth was approximately 15 cm so that schools would be
approximately 2D. The ﬁsh were recorded with an overhead grey-scale video camera (Library GE 60; Library Co. Ltd.,
Tokyo, Japan) at a spatial resolution of 640 ×480 pixels and a temporal resolution of 120 frames per second.
4.4
The deﬁnition of ON and OFF state for each parameter
We deﬁne a function for each parameter that returns either 0 (OFF) or 1 (ON) for given input values. Generally, we
denote a function as F t
i (·), where F is the name of the function, i is the index of the individual and t is the time. The
arguments of the function can be either in the position vectors xi(t) or the velocity vectors vi(t) of each individual
at time t. In general, the dimensions of these vectors are d ≤3; the experimental setup used here gives d = 2. The
number of individuals is n.
4.4.1
Local parameters
• Distance function Dt
i(x1(t), x2(t), · · · , xn(t)): Rd × Rd × · · · × Rd −→{0, 1}
For each individual i we obtain a set St
i
= {j|d(xi(t), xj(t)) < ζ, j ̸= i} of all other individu-
als within a speciﬁed distance ζ. Here d(x, y) gives the Euclidean distance between x and y. Then,
Dt
i(x1(t), x2(t), . . . , xn(t)) = 1 when |St
i| > 0 and is 0 otherwise, where |S| denotes the number of
elements of a set S.
• Blind sight function Bt
i(v1(t), v2(t), · · · , vn(t)) : Rd × Rd × · · · × Rd −→{0, 1}
For each individual we form the set Ot
i = {j| arg(vi(t), vj(t)) < η, j ̸= i} of all other individuals whose
velocity vectors point in a direction within an angle η of that of the focal individual. The function arg(v1(t),
v2(t)) gives the angle between two vectors. Then, Bt
i(v1(t), v2(t), · · · , vn(t)) = 1 when |Ot
i| > 0 and is 0
otherwise.
• Turning rate function T t
i (vi(t), vi(t −∆t)) : Rd × Rd −→{0, 1}
The turning rate function returns 1 when an individual’s turning rate exceeds a speciﬁed thresholdδ. That is,
T t
i (vi(t), vi(t −∆t)) = 1 when arg(vi(t), vi(t −∆t)) ≥δ and is 0 otherwise. The time step used in this
paper is ∆t = 0.05, ∆t = 0.1 or ∆t = 0.2 s.
To
obtain
the
states
of
the
ﬁsh
school,
we
take
a
conjunction
of
these
result,
that
is,
Dt
i(x1(t), x2(t), · · · , xn(t)) ∧Bt
i(v1(t), v2(t), · · · , vn(t)) ∧T t
i (vi(t), vi(t −∆t)) for each individual i.
The conjunction is given as ∧: {0, 1}2 −→{0, 1} where 1 ∧1 = 1 and is 0 otherwise. Thus the state of each
individual i at time t is si(t; ζ, η, δ) ∈{0, 1} which depends on the triplet of parameter values (ζ, η, δ). The
state of the school at time t is then a vector s(t) = (s1(t), s2(t), . . . , sn(t)) ∈{0, 1}n, where the parameter
dependence has been omitted for simplicity.
4.4.2
Global parameters
• Average direction function Avdt
i(V (t), vi(t)) : Rd × Rd −→{0, 1}
V (t) is the average of {v1(t), v2(t), ..., vn(t)}. If an individual’s direction of motion deviates from the average
by more than a threshold amount Θ then the individual is in the OFF state: that is, Avdt
i(V (t), vi(t)) = 1
when arg(V (t), vi(t)) ≤Θ, and is 0 otherwise.
• Centre of mass function Comt
i(X(t), xi(t)) : Rd × Rd −→{0, 1}
X(t) is the average of {x1(t), x2(t), · · · , xn(t)}. If an individual is further from X(t) than a speciﬁed
threshold Ωthen the individual is in the OFF state: that is, Comt
i(X(t), xi(t)) = 1 when d(X(t), xi(t)) ≤Ω
and is 0 otherwise.
To obtain the state of the ﬁsh school, we take a conjunction of these results to obtain a state for each individual
which depends on the pair (Θ, Ω):, si(t; Θ, Ω) = Avdt
i(V (t), vi(t)) ∧Comt
i(X(t), xi(t)) ∈{0, 1}. The
state of the school at time t is then a vector s(t) = (s1(t), s2(t), . . . , sn(t)) ∈{0, 1}n, where the parameter
dependence has been omitted for simplicity.
6


## Page 7


A PREPRINT - DECEMBER 4, 2018
References
[1] J Buhl, DJT Sumpter, ID Couzin, JJ Hale, E Despland, ER Miller, and SJ Simpson. From disorder to order in
marching locusts. Science, 312(5778):1402–1406, 2006.
[2] CA Yates, R Erban, C Escudero, ID Couzin, and J Buhl. Inherent noise can facilitate coherence in collective
swarm motion. PNAS, 106(14):5464–5469, 2009.
[3] Sepideh Bazazi, Frederic Bartumeus, Joseph J. Hale, and Iain D. Couzin. Intermittent motion in desert locusts:
Behavioural complexity in simple environments. PLoS Computational Biology, 2012.
[4] A Attanasi, A Cavagna, DL Castello, I Giardina, S Melillo, L Parisi, O Pohl, R Rossaro, E Shen, E Silvestri, and
M Viale. Finite-size scaling as a way to probe near-criticality in natural swarms. Phys. Rev. Lett, 113:238102,
2014.
[5] Alessandro Attanasi, Andrea Cavagna, Lorenzo Del Castello, Irene Giardina, Stefania Melillo, Leonardo Parisi,
Oliver Pohl, Bruno Rossaro, Edward Shen, Edmondo Silvestri, and Massimiliano Viale. Collective Behaviour
without Collective Order in Wild Swarms of Midges. PLoS Computational Biology, 10(7), 2014.
[6] Hisashi Murakami, Takenori Tomaru, Yuta Nishiyama, Toru Moriyama, Takayuki Niizato, and Yukio Pegio Gunji.
Emergent runaway into an avoidance area in a swarm of soldier crabs. PLoS ONE, 2014.
[7] C. C. Ioannou, V. Guttal, and I. D. Couzin. Predatory ﬁsh select for coordinated collective motion in virtual prey.
Science, 2012.
[8] Ariana Strandburg-Peshkin, Colin R. Twomey, Nikolai W.F. Bode, Albert B. Kao, Yael Katz, Christos C. Ioannou,
Sara B. Rosenthal, Colin J. Torney, Hai Shan Wu, Simon A. Levin, and Iain D. Couzin. Visual sensory networks
and effective information transfer in animal groups. Current Biology, 2013.
[9] Andrew Berdahl, Colin J. Torney, Christos C. Ioannou, Jolyon J. Faria, and Iain D. Couzin. Emergent sensing of
complex environments by mobile animal groups. Science, 2013.
[10] Hisashi Murakami, Takayuki Niizato, Takenori Tomaru, Yuta Nishiyama, and Yukio Pegio Gunji. Inherent noise
appears as a Lévy walk in ﬁsh schools. Scientiﬁc Reports, 2015.
[11] Takayuki Niizato, Hisashi Murakami, Kazuki Sangu, Takenori Tomaru, Kohei Sonoda, Yuta Nishiyama, and
Yukio Pegio Gunji. Local perspectives of Plecoglossusaltivelis determine searching strategy. In AIP Conference
Proceedings, 2017.
[12] Michele Ballerini, Nicola Cabibbo, Raphael Candelier, Andrea Cavagna, Evaristo Cisbani, Irene Giardina, Alberto
Orlandi, Giorgio Parisi, Andrea Procaccini, Massimiliano Viale, and Vladimir Zdravkovic. Empirical investigation
of starling ﬂocks: a benchmark study in collective animal behaviour. Animal Behaviour, 2008.
[13] A. Cavagna, A. Cimarelli, I. Giardina, G. Parisi, R. Santagati, F. Stefanini, and M. Viale. Scale-free correlations in
starling ﬂocks. Proceedings of the National Academy of Sciences, 2010.
[14] A. Cavagna, S. M. Duarte Queirós, I. Giardina, F. Stefanini, and M. Viale. Diffusion of individual birds in starling
ﬂocks. Proceedings of the Royal Society B: Biological Sciences, 2013.
[15] W. Bialek, A. Cavagna, I. Giardina, T. Mora, O. Pohl, E. Silvestri, M. Viale, and A. M. Walczak. Social interactions
dominate speed control in poising natural ﬂocks near criticality. Proceedings of the National Academy of Sciences,
2014.
[16] Alessandro Attanasi, Andrea Cavagna, Lorenzo Del Castello, Irene Giardina, Asja Jelic, Stefania Melillo, Leonardo
Parisi, Oliver Pohl, Edward Shen, and Massimiliano Viale. Emergence of collective changes in travel direction of
starling ﬂocks from individual birds’ ﬂuctuations. Journal of the Royal Society Interface, 2015.
[17] Thierry Mora, Aleksandra M. Walczak, Lorenzo Del Castello, Francesco Ginelli, Stefania Melillo, Leonardo
Parisi, Massimiliano Viale, Andrea Cavagna, and Irene Giardina. Local equilibrium in bird ﬂocks. Nature Physics,
2016.
[18] Iain Couzin. Collective minds. Nature, 2007.
[19] Iain D. Couzin. Collective cognition in animal groups, 2009.
7


## Page 8


A PREPRINT - DECEMBER 4, 2018
[20] DJT Sumpter. Collective animal behavior. Princeton University Press, 2010.
[21] Tamás Vicsek and Anna Zafeiris. Collective motion, 2012.
[22] Nigel R. Franks, Anna Dornhaus, Jon P. Fitzsimmons, and Martin Stevens. Speed versus accuracy in collective
decision making. Proceedings of the Royal Society B: Biological Sciences, 2003.
[23] John R.G. Dyer, Anders Johansson, Dirk Helbing, Iain D. Couzin, and Jens Krause. Leadership, consensus
decision making and collective behaviour in humans. Philosophical Transactions of the Royal Society B: Biological
Sciences, 2009.
[24] Thomas Bose, Andreagiovanni Reina, and James AR Marshall. Collective decision-making, 2017.
[25] Iain D. Couzin, Christos C. Ioannou, Güven Demirel, Thilo Gross, Colin J. Torney, Andrew Hartnett, Larissa
Conradt, Simon A. Levin, and Naomi E. Leonard. Uninformed individuals promote democratic consensus in
animal groups. Science, 2011.
[26] Itai Pinkoviezky, Iain D. Couzin, and Nir S. Gov. Collective conﬂict resolution in groups on the move. Physical
Review E, 2018.
[27] Per Bak, Chao Tang, and Kurt Wiesenfeld. Self-organized criticality. Physical Review A, 1988.
[28] Christian Tetzlaff, Samora Okujeni, Ulrich Egert, Florentin Wörgötter, and Markus Butz. Self-organized criticality
in developing neuronal networks. PLoS Computational Biology, 2010.
[29] Takayuki Niizato and Yukio Pegio Gunji. Fluctuation-driven ﬂocking movement in three dimensions and scale-free
correlation. PLoS ONE, 2012.
[30] Yukio Pegio Gunji. Self-organized criticality in asynchronously tuned elementary cellular automata. Complex
Systems, 2014.
[31] Yukio Pegio Gunji, Tomoko Sakiyama, and Hisashi Murakami. Punctuated equilibrium based on a locally
ambiguous niche. BioSystems, 2014.
[32] Takayuki Niizato and Hisashi Murakami. Entangled time in ﬂocking : Multi-time-scale interaction reveals
emergence of inherent noise. PLoS ONE, 13(4):1–21, 2018.
[33] J. E. Herbert-Read, S. Krause, L. J. Morrell, T. M. Schaerf, J. Krause, and A. J.W. Ward. The role of individuality
in collective group movement. Proceedings of the Royal Society B: Biological Sciences, 2013.
[34] Jolle W. Jolles, Neeltje J. Boogert, Vivek H. Sridhar, Iain D. Couzin, and Andrea Manica. Consistent Individual
Differences Drive Collective Behavior and Group Functioning of Schooling Fish. Current Biology, 2017.
[35] Y. Katz, K. Tunstrom, C. C. Ioannou, C. Huepe, and I. D. Couzin. Inferring the structure and dynamics of
interactions in schooling ﬁsh. Proceedings of the National Academy of Sciences, 2011.
[36] Jacques Gautrais, Francesco Ginelli, Richard Fournier, Stéphane Blanco, Marc Soria, Hugues Chaté, and Guy
Theraulaz. Deciphering Interactions in Moving Animal Groups. PLoS Computational Biology, 2012.
[37] Matthäus Staniek and Klaus Lehnertz. Symbolic transfer entropy. Physical Review Letters, 2008.
[38] Sachit Butail, Violet Mwaffo, and Maurizio Porﬁri. Model-free information-theoretic approach to infer leadership
in pairs of zebraﬁsh. Physical Review E, 2016.
[39] Emanuele Crosato, Li Jiang, Valentin Lecheval, Joseph T. Lizier, X. Rosalind Wang, Pierre Tichit, Guy Theraulaz,
and Mikhail Prokopenko. Informative and misinformative interactions in a school of ﬁsh, 2018.
[40] Joseph T. Lizier, Mikhail Prokopenko, and Albert Y. Zomaya. Local information transfer as a spatiotemporal ﬁlter
for complex systems. Physical Review E - Statistical, Nonlinear, and Soft Matter Physics, 2008.
[41] Joseph T. Lizier, Mikhail Prokopenko, and Albert Y. Zomaya. Local measures of information storage in complex
distributed computation. Information Sciences, 2012.
[42] Jie Sun and Erik M. Bollt. Causation entropy identiﬁes indirect inﬂuences, dominance of neighbors and anticipatory
couplings. Physica D: Nonlinear Phenomena, 2014.
8


## Page 9


A PREPRINT - DECEMBER 4, 2018
[43] Ryan G. James, Nix Barnett, and James P. Crutchﬁeld. Information Flows? A Critique of Transfer Entropies.
Physical Review Letters, 2016.
[44] Takenori Tomaru, Hisashi Murakami, Takayuki Niizato, Yuta Nishiyama, Kohei Sonoda, Toru Moriyama, and
Yukio Pegio Gunji. Information transfer in a swarm of soldier crabs. Artiﬁcial Life and Robotics, 2016.
[45] E. Yagmur Erten, Joseph T. Lizier, Mahendra Piraveenan, and Mikhail Prokopenko. Criticality and information
dynamics in epidemiological models. Entropy, 2017.
[46] X. Rosalind Wang, Jennifer M. Miller, Joseph T. Lizier, Mikhail Prokopenko, and Louis F. Rossi. Quantifying and
tracing information cascades in swarms. PLoS ONE, 2012.
[47] X. Rosalind Wang, Jennifer M. Miller, Joseph T. Lizier, Mikhail Prokopenko, and Louis F. Rossi. Measuring
information storage and transfer in swarms. Proceedings of the Eleventh European Conference on the Synthesis
and Simulation of Living Systems (ECAL 2011), 2011.
[48] Larissa Albantakis and Giulio Tononi. The intrinsic cause-effect power of discrete dynamical systems-from
elementary cellular automata to adapting animats. Entropy, 2015.
[49] David Balduzzi and Giulio Tononi. Qualia: The geometry of integrated information. PLoS Computational Biology,
2009.
[50] G. Tononi. An Integrated iNformation Theory of Consciousness. In Encyclopedia of Consciousness. 2010.
[51] Adam B. Barrett and Anil K. Seth. Practical measures of integrated information for time- series data. PLoS
Computational Biology, 2011.
[52] Masafumi Oizumi, Larissa Albantakis, and Giulio Tononi. From the Phenomenology to the Mechanisms of
Consciousness: Integrated Information Theory 3.0. PLoS Computational Biology, 2014.
[53] Masafumi Oizumi, Naotsugu Tsuchiya, and Shun-ichi Amari. A uniﬁed framework for information integration
based on information geometry. 113(51), 2015.
[54] Masafumi Oizumi, Shun Ichi Amari, Toru Yanagawa, Naotaka Fujii, and Naotsugu Tsuchiya. Measuring Integrated
Information from the Decoding Perspective. PLoS Computational Biology, 2016.
[55] WGP Mayner, W Marshall, L Albantakis, G Findlay, R Marchman, and G Tononi. Pyphi: A toolbox for integrated
information theory. PLoS Computational Biology, 2018.
[56] Marcello Massimini, Fabio Ferrarelli, Reto Huber, Steve K. Esser, Harpreet Singh, and Giulio Tononi. Neuro-
science: Breakdown of cortical effective connectivity during sleep. Science, 2005.
[57] M T Alkire, Anthony G Hudetz, and Giulio Tononi. Consciousness and anesthesia. Science (New York, N.Y.),
2008.
[58] Olivia Gosseries, Haibo Di, Steven Laureys, and Mélanie Boly. Measuring Consciousness in Severely Damaged
Brains. Annual Review of Neuroscience, 2014.
[59] Pedro Mediano, Anil Seth, and Adam Barrett. Measuring integrated information: Comparison of candidate
measures in theory and simulation. 2018.
[60] Sosuke Ito. Stochastic Thermodynamic Interpretation of Information Geometry. Physical Review Letters, 2018.
[61] Sosuke Ito. Uniﬁed framework for the second law of thermodynamics and information thermodynamics based on
information geometry. 2018.
[62] Ludwig Bertalanffy. General system theory: foundations, development, applications (Revised Edition). George
Braziller, 1969.
[63] Cliff Hooker. Philosophy of Complex Systems (Handbook of the Philosophy of Science, vol. 10). North Holland,
2011.
[64] Keith Farnsworth. How Organisms Gained Causal Independence and How It Might Be Quantiﬁed. Biology, 2018.
[65] Jeffrey A. Edlund, Nicolas Chaumont, Arend Hintze, Christof Koch, Giulio Tononi, and Christoph Adami.
Integrated information increases with ﬁtness in the evolution of animats. PLoS Computational Biology, 2011.
9


## Page 10


A PREPRINT - DECEMBER 4, 2018
[66] William Marshall, Hyunju Kim, Sara I. Walker, Giulio Tononi, and Larissa Albantakis. How causal analysis
can reveal autonomy in models of biological systems. Philosophical Transactions of the Royal Society A:
Mathematical, Physical and Engineering Sciences, 2017.
[67] Iain D. Couzin, Jens Krause, Richard James, Graeme D. Ruxton, and Nigel R. Franks. Collective memory and
spatial sorting in animal groups. Journal of Theoretical Biology, 2002.
[68] Reza Olfati-Saber. Flocking for multi-agent dynamic systems: Algorithms and theory. IEEE Transactions on
Automatic Control, 2006.
[69] Reza Olfati-Saber, J. Alex Fax, and Richard M. Murray. Consensus and cooperation in networked multi-agent
systems. Proceedings of the IEEE, 2007.
[70] S Khajehabdollahi. Phase transitions of integrated information in the generalized ising model of the brain.
Electronic Thesis and Dissertation Repository, 5241, 2018.
10


## Page 11


A PREPRINT - DECEMBER 4, 2018

2132#
	 !2
-"4!2
 



 



 



 
!!23	 !2

2!2
!!23
213
2#
2!2
!!23-"4
!2
2!2


 !!2 32!2 2!!4 
A"!
 



 



%
%
-2 22 3!!2 
Figure 1: The deﬁnition of ON and OFF states for local parameter settings. Three parameters determine a school’s
state (Yellow: distance, Blue: Field of View, Purple: Turning rate). Coloured individuals are in the ON state. We take a
conjunction of the three school states to obtain the ﬁnal school state at time t. Then we compute Φ from a time series of
these states by using PyPhi.
11


## Page 12


A PREPRINT - DECEMBER 4, 2018
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π (rad))
0.22
0.22
0.23
0.23
0.22
0.13
0.13
0.13
0.13
0.13
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.02
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
N = 2
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π (rad))
0.18
0.19
0.19
0.21
0.14
0.05
0.05
0.07
0.02
0.03
0.00
0.00
0.00
0.01
0.02
0.04
0.05
0.05
0.05
0.06
0.00
0.00
0.00
0.01
0.01
0.01
0.01
0.02
0.02
0.02
0.00
0.00
0.00
0.01
0.02
0.01
0.01
0.01
0.01
0.01
0.00
0.00
0.00
0.01
0.01
0.01
0.01
0.01
0.02
0.02
0.00
0.00
0.00
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.10
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.01
N = 3
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π (rad))
0.25
0.29
0.23
0.31
0.11
0.00
0.01
0.01
0.01
0.01
0.00
0.08
0.40
0.52
0.62
0.70
0.70
0.72
0.72
0.72
0.00
0.02
0.11
0.36
0.50
0.51
0.51
0.51
0.51
0.51
0.00
0.01
0.07
0.11
0.29
0.29
0.30
0.30
0.30
0.30
0.00
0.02
0.03
0.09
0.10
0.11
0.11
0.12
0.12
0.12
0.00
0.01
0.02
0.06
0.06
0.06
0.06
0.06
0.06
0.07
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.04
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.12
0.05
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
N = 4
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π (rad))
0.27
1.45
0.98
0.78
0.39
0.04
0.00
0.00
0.00
0.00
0.01
0.78
1.34
1.66
1.65
1.69
1.89
1.90
1.89
1.90
0.00
0.43
1.30
1.56
1.59
1.84
1.91
1.82
1.84
1.84
0.00
0.41
1.22
1.61
1.70
1.83
1.86
1.79
1.80
1.80
0.00
0.26
0.81
0.77
0.82
0.96
0.94
0.94
0.93
1.05
0.00
0.07
0.33
0.50
0.52
0.55
0.54
0.54
0.54
0.56
0.00
0.03
0.09
0.07
0.09
0.09
0.09
0.09
0.09
0.10
0.00
0.01
0.01
0.01
0.02
0.02
0.02
0.02
0.02
0.02
0.05
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.32
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
N = 5
0.04
0.08
0.12
0.16
0.20
0.04
0.08
0.12
0.16
0.20
0.15
0.30
0.45
0.60
0.4
0.8
1.2
1.6
Figure 2: The heat map shows Φ values for distance (horizontal axis) and ﬁeld of view (vertical axis) parameter values.
The value of Φ for two- and three-ﬁsh schools depends only on distance; whereas it depends on both parameters in four-
and ﬁve-ﬁsh schools. The time step is ∆t = 0.05 s. All other cases are described in the Supporting Information.
12


## Page 13


A PREPRINT - DECEMBER 4, 2018
0
200
400
600
800
1000
time (sec)
0
1
2
3
4
5
6
7
Φ
Figure 3: An example of a time series of Φ obtained from real ﬁsh data (N = 5). The reduction of Φ at various points
means that leadership emerges in the group. Average Φ becomes higher when the group has a leader. Note that the
average Φ in this ﬁgure is averaged from Φ values of 32 states in this case. The local parameter setting is Distance=
1000 (mm), Field of View = 6.02 (rad) Turning rate = 0 (rad), respectively.
13


## Page 14


A PREPRINT - DECEMBER 4, 2018
 
-1
1-
-1!-2
	33



-12---32
"4 3
 



 



A
A
331-

 



#1 -
	
 



	#!-2	33
Figure 4: The deﬁnition of ON and OFF states for global parameter settings. Two parameters determine a school’s state
(Yellow: Centre of Mass, Blue: Average Direction). Coloured individuals are in the ON state. We take a conjunction of
the two school states and obtain the ﬁnal school state at time t. Then we compute Φ from a time series of these states by
using PyPhi.
14


## Page 15


A PREPRINT - DECEMBER 4, 2018
30
60
90
120
150
180
210
240
270
300
330
360
390
420
450
480
510
540
570
600
3000
Centre of Mass (mm)
360
324
288
252
216
180
144
108
72
36
Mean Direction (π rad)
0.21
0.22
0.22
0.22
0.23
0.23
0.23
0.23
0.23
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.13
0.21
0.22
0.22
0.22
0.23
0.23
0.23
0.23
0.23
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.13
0.21
0.22
0.22
0.22
0.23
0.23
0.23
0.23
0.23
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.13
0.21
0.22
0.22
0.22
0.23
0.23
0.23
0.23
0.23
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.13
0.21
0.22
0.22
0.22
0.23
0.23
0.23
0.23
0.23
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.13
0.21
0.22
0.22
0.22
0.23
0.23
0.23
0.23
0.23
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.17
0.13
0.20
0.21
0.19
0.18
0.17
0.17
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.14
0.20
0.20
0.19
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.17
0.19
0.20
0.19
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.17
0.17
0.18
0.17
0.17
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
N = 2
30
60
90
120
150
180
210
240
270
300
330
360
390
420
450
480
510
540
570
600
3000
Centre of Mass (mm)
360
324
288
252
216
180
144
108
72
36
Mean Direction (π rad)
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.03
0.01
0.00
0.00
0.02
0.05
0.04
0.04
0.05
0.02
0.00
0.03
0.01
0.00
0.00
0.00
0.00
0.01
0.01
0.01
0.02
0.04
0.04
0.06
0.10
0.13
0.18
0.36
0.38
0.40
0.41
0.40
0.57
0.01
0.00
0.00
0.00
0.00
0.00
0.01
0.01
0.01
0.03
0.03
0.04
0.06
0.09
0.15
0.25
0.25
0.26
0.26
0.26
0.46
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.01
0.01
0.03
0.02
0.04
0.07
0.13
0.22
0.22
0.22
0.22
0.22
0.39
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.01
0.02
0.04
0.03
0.08
0.09
0.12
0.13
0.13
0.13
0.13
0.18
0.02
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.01
0.02
0.03
0.03
0.03
0.04
0.04
0.05
0.05
0.05
0.05
0.05
0.07
0.06
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.02
0.01
0.01
0.01
0.02
0.02
0.02
0.02
0.02
0.02
0.03
0.02
0.06
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.08
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.07
0.00
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.02
0.01
0.01
0.01
0.01
0.02
0.02
0.02
0.02
0.02
0.02
N = 3
30
60
90
120
150
180
210
240
270
300
330
360
390
420
450
480
510
540
570
600
3000
Centre of Mass (mm)
360
324
288
252
216
180
144
108
72
36
Mean Direction (π rad)
0.30
0.00
0.00
0.00
0.01
0.01
0.11
0.12
0.14
0.11
0.14
0.22
0.11
0.24
0.14
0.15
0.00
0.01
0.01
0.01
0.01
0.30
0.00
0.00
0.00
0.01
0.04
0.14
0.28
0.40
0.65
0.76
0.89
1.00
1.08
1.04
0.93
0.94
0.94
0.94
0.94
1.14
0.30
0.00
0.00
0.00
0.01
0.04
0.10
0.24
0.38
0.51
0.55
0.67
0.79
0.78
0.81
0.79
0.86
0.86
0.86
0.86
0.86
0.31
0.00
0.00
0.00
0.01
0.04
0.09
0.18
0.34
0.53
0.57
0.63
0.73
0.76
0.88
0.83
0.84
0.84
0.84
0.84
0.94
0.32
0.00
0.00
0.00
0.01
0.04
0.08
0.10
0.28
0.42
0.41
0.46
0.56
0.58
0.65
0.64
0.64
0.64
0.64
0.64
0.73
0.36
0.00
0.00
0.00
0.01
0.04
0.07
0.09
0.16
0.26
0.28
0.39
0.50
0.50
0.51
0.52
0.48
0.48
0.48
0.48
0.59
0.38
0.00
0.00
0.00
0.01
0.01
0.02
0.02
0.03
0.03
0.03
0.03
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.06
0.40
0.00
0.00
0.00
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.49
0.00
0.00
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.57
0.02
0.00
0.01
0.01
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
N = 4
30
60
90
120
150
180
210
240
270
300
330
360
390
420
450
480
510
540
570
600
3000
Centre of Mass (mm)
360
324
288
252
216
180
144
108
72
36
Mean Direction (π rad)
1.02
0.00
0.00
0.00
0.04
0.29
0.49
0.87
0.78
0.86
1.30
1.43
0.91
0.79
0.62
0.43
0.54
0.51
0.42
0.34
0.00
1.01
0.00
0.00
0.00
0.05
0.38
0.67
1.27
1.52
1.78
2.24
2.34
2.65
2.83
2.92
2.89
3.18
3.25
3.28
3.27
3.47
1.01
0.00
0.00
0.00
0.04
0.35
0.60
0.95
1.31
1.58
1.84
1.97
2.15
2.18
2.28
2.31
2.58
2.56
2.65
2.79
2.94
1.01
0.01
0.00
0.00
0.03
0.32
0.54
0.91
1.18
1.37
1.57
1.64
1.83
1.82
1.94
1.98
2.07
2.14
2.31
2.34
2.45
1.01
0.01
0.00
0.00
0.03
0.25
0.45
0.76
0.95
1.03
1.22
1.22
1.35
1.26
1.40
1.44
1.65
1.68
1.76
1.89
2.05
1.03
0.01
0.00
0.00
0.02
0.10
0.18
0.28
0.39
0.45
0.47
0.46
0.48
0.52
0.57
0.65
0.85
0.90
0.91
0.91
1.05
1.11
0.04
0.00
0.00
0.02
0.04
0.06
0.06
0.08
0.09
0.09
0.10
0.10
0.09
0.10
0.11
0.11
0.11
0.11
0.11
0.12
1.19
0.05
0.00
0.00
0.01
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.03
0.03
0.03
0.03
0.03
1.19
0.14
0.00
0.01
0.01
0.02
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
1.13
0.35
0.01
0.02
0.03
0.04
0.05
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.07
N = 5
0.14
0.16
0.18
0.20
0.22
0.1
0.2
0.3
0.4
0.5
0.2
0.4
0.6
0.8
1.0
0.6
1.2
1.8
2.4
3.0
Figure 5: The heat map shows Φ values with distance from the centre of mass (horizontal axis) and the difference from
the average direction (vertical axis). Only two-ﬁsh schools show a different distribution. When the group size is above
three, the distribution of Φ values becomes wider. The time step is ∆t = 0.05 s.
15


## Page 16


A PREPRINT - DECEMBER 4, 2018
5
Supporting Information
5.1
Mutual Information
The mutual information (Eq. 1) [54] was also calculated in the same manner as Φ to characterise the susceptibility
of Φ. The past and present states of the system are given by the binary variables X = {x1, x2, · · · , xN} and
Y = {y1, y2, · · · , yN}, respectively, where N is the number of elements in the system. The mutual information
between the two variables X and Y is expressed by the Kullback-Leibler divergence of the product of their marginal
densities from their joint distribution. Intuitively speaking, in our study, the mutual information was used to measure
the amount of information shared by the given binary states of ﬁsh school over temporal change: Xt, Xt−∆t, where
∆t = 0.05 s.
min
q(Xt,Xt−∆t) DKL[p || q] =
X
Xt,Xt−∆t
p(Xt, Xt−∆t) log p(Xt, Xt−∆t)
p(Xt)p(Xt−∆t)
= H(Xt) + H(Xt−∆t) −H(Xt−∆t | Xt)
= I(Xt; Xt−∆t)
(1)
0
1
2
3
4
5
6
7
8
9
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π (rad))
0.71
0.25
0.12
0.08
0.07
0.06
0.06
0.06
0.05
0.05
1.10
1.04
0.95
0.92
0.91
0.91
0.90
0.90
0.90
0.90
1.32
1.35
1.28
1.26
1.25
1.25
1.25
1.24
1.24
1.24
1.34
1.38
1.31
1.29
1.29
1.28
1.28
1.28
1.28
1.28
1.29
1.31
1.26
1.24
1.24
1.24
1.23
1.23
1.23
1.23
1.22
1.26
1.22
1.21
1.20
1.20
1.20
1.20
1.20
1.20
1.15
1.26
1.23
1.23
1.23
1.23
1.22
1.22
1.22
1.22
1.07
1.26
1.26
1.25
1.25
1.25
1.25
1.25
1.25
1.25
0.89
1.18
1.19
1.20
1.20
1.20
1.20
1.20
1.20
1.20
0.51
0.83
0.86
0.87
0.87
0.87
0.87
0.87
0.87
0.87
N = 2
0
1
2
3
4
5
6
7
8
9
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π (rad))
1.69
0.83
0.35
0.13
0.08
0.00
0.00
0.00
0.00
0.00
1.79
1.25
0.82
0.68
0.61
0.57
0.56
0.55
0.55
0.55
1.91
1.72
1.43
1.32
1.30
1.29
1.28
1.27
1.27
1.26
1.94
1.98
1.74
1.65
1.63
1.61
1.60
1.59
1.59
1.59
1.91
2.08
1.86
1.79
1.77
1.76
1.75
1.75
1.74
1.73
1.82
2.11
1.93
1.87
1.85
1.84
1.84
1.83
1.83
1.83
1.66
2.15
2.04
1.99
1.98
1.98
1.98
1.97
1.97
1.97
1.43
2.17
2.13
2.11
2.11
2.11
2.10
2.10
2.10
2.10
1.10
2.03
2.09
2.09
2.10
2.10
2.10
2.10
2.10
2.10
0.54
1.46
1.65
1.69
1.70
1.70
1.71
1.71
1.71
1.71
N = 3
0
1
2
3
4
5
6
7
8
9
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π (rad))
2.46
0.57
0.05
0.02
0.01
0.00
0.00
0.00
0.00
0.00
2.51
0.98
0.50
0.39
0.29
0.27
0.26
0.26
0.26
0.26
2.71
1.61
1.27
1.19
1.17
1.17
1.17
1.16
1.16
1.16
2.82
2.05
1.78
1.73
1.71
1.71
1.71
1.71
1.71
1.71
2.85
2.29
2.07
2.01
1.99
1.98
1.98
1.98
1.98
1.98
2.79
2.46
2.26
2.22
2.20
2.20
2.20
2.20
2.20
2.20
2.63
2.65
2.51
2.48
2.47
2.47
2.47
2.47
2.47
2.47
2.37
2.81
2.74
2.72
2.72
2.72
2.72
2.72
2.72
2.72
1.87
2.76
2.78
2.78
2.78
2.78
2.78
2.78
2.78
2.78
1.02
2.08
2.26
2.29
2.29
2.29
2.29
2.29
2.29
2.29
N = 4
0
1
2
3
4
5
6
7
8
9
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π (rad))
3.11
0.60
0.16
0.05
0.03
0.00
0.00
0.00
0.00
0.00
3.11
0.99
0.42
0.30
0.27
0.20
0.19
0.19
0.18
0.18
3.30
1.60
1.18
1.09
1.06
1.05
1.04
1.04
1.04
1.03
3.45
2.16
1.85
1.78
1.75
1.73
1.72
1.72
1.71
1.71
3.53
2.48
2.20
2.14
2.11
2.09
2.08
2.08
2.08
2.08
3.52
2.73
2.47
2.41
2.39
2.37
2.36
2.36
2.36
2.36
3.37
3.00
2.80
2.75
2.73
2.71
2.71
2.71
2.70
2.70
3.05
3.27
3.13
3.10
3.08
3.07
3.06
3.06
3.06
3.06
2.40
3.35
3.31
3.30
3.29
3.28
3.28
3.28
3.28
3.28
1.27
2.68
2.88
2.91
2.92
2.92
2.92
2.92
2.92
2.92
N = 5
0.25
0.50
0.75
1.00
1.25
0.0
0.4
0.8
1.2
1.6
2.0
0.0
0.5
1.0
1.5
2.0
2.5
0.0
0.6
1.2
1.8
2.4
3.0
Figure 6: Mutual Information I(X; Y ), as given by the colour bar.
The heatmap representations of mutual information values versus various ﬁring thresholds (Fig. 6) show different patterns
from the heatmap of Φ values (Fig. 2). First, the results were consistent with the general inequality 0 ≤Φ ≤I(X; Y )
16


## Page 17


A PREPRINT - DECEMBER 4, 2018
shown by Oizumi, et al. [54]. Any peak values of mutual information were higher than the peak values of Φ. Second,
the discontinuity between the school size of 3 (N = 3) and the school size of 4 (N = 4) was not observed. Third, the
exact opposite trends were observed. The values were appeared to be very homogeneous over different settings of ﬁring
thresholds. The low and high areas were not so distinguishable as Φ.
The integrated information Φ can capture some emergent information dynamics of the ﬁsh school which mutual
information cannot measure. They essentially have different information: Mutual information or Shannon information
is observational and extrinsic, whereas Φ is causal and intrinsic [50]. We saw here this essential differences of the two
information quantities.
5.2
Boids Model
For comparison, simulated trajectories based on the Boids model ([67]) were analysed in the same manner as the
trajectories of the real ﬁsh school. Boids was developed by Reynolds and the complex and realistic looking behaviour
of a group of agents as a whole is determined entirely by local interaction of individual agent choices based on a
set of simple rules: Repulsion (Eq. 2), Alignment (Eq. 3), and Attraction (Eq. 4) . In this study, N agents with
position vectors xi and unit direction vectors vi were simulated in continuous two-dimensional space (3000 × 2500)
(the same size as the experimental ﬁsh tank). Time was discretised into t computational time steps with a regular
spacing ∆t = 0.05 s. When there are nr agents in the neighbourhood of the agent i, the following rules were applied to
update the variables of agents at each t:
dr(t + ∆t) = −
nr
X
j̸=i
rij(t)
|rij(t)|
(2)
do(t + ∆t) =
nj
X
j=1
vj(t)
|vj(t)|
(3)
da(t + ∆t) =
na
X
i̸=j
rij(t)
|rij(t)|
(4)
where nr = {j | rij(t) ≤R}, no = {j | rij(t) ≤O}, na = {j | O ≤rij(t) ≤A} and rij =
(xj−xi)
|(xj−xi)| is the unit
vector in the direction of neighbour j. The above rules were summed and averaged with the additive Gaussian noise to
determine the trajectories of agents. The update of variables were done synchronously.
5.2.1
Model parameters
Parameters are the key to determine the dynamics of the model. In the present study, the model parameters were set to
simulate the real experimental data. The average distances were approximately 80 to 140 mm so we set O = 120 (mm)
and R = 10 (mm) (= the body length), and A = ∞. Thus, the ﬁsh school should not part less than 140 mm. This
setting was necessary for the swarm to become separated by the boundary conditions. The boundary conditions mimic
and reﬂect the real data. The amplitudes of noise are set to be proportional to the averaged angle change so each agent
should have a different noise size.
5.2.2
Comparison of trajectories of Real ﬁsh and Boid model
The constructed boid model (Fig. 7(a)) showed very similar trajectories in terms of the complexity as real ﬁsh (Fig. 7(b)).
Both Boids and real ﬁsh had similar trajectories; however, the Boids’ Φ heatmaps showed different patterns (Fig. 8(a)).
The Φ values of the Boids had large standard deviations. The discontinuity between the N = 3 and the N = 4 was not
observed. The N = 2 of Boids were especially different from the N = 2 of real ﬁsh. Similarly, the values of Φ values
for Boids model were large across the different ﬁring setups (Fig. 8(b)).
17


## Page 18


A PREPRINT - DECEMBER 4, 2018
N
Average distance (mm)
Average velocity (mm/s)
Error (S.D.)
Minimum distance (mm)
2
166.3
11.2
0.18
1.90
90.67
11.32
0.23
0.10
122.0
10.67
0.18
1.60
3
170.8
12.55
0.23
1.80
159.1
14.3
0.14
1.83
173.1
12.5
0.13
2.82
132.0
10.0
0.19
1.67
4
164.3
11.28
0.14
1.18
141.5
7.95
0.12
1.38
114.9
6.19
0.38
1.83
5
143.8
10.83
0.28
0.79
146.0
8.88
0.12
1.16
143.7
10.8
0.28
1.44
Table 1: Real ﬁsh data summary. N: Number of individuals (Unit: None), x: Average distance (Unit: (mm)), v:
Average velocity (Unit: (mm) per second), Error (S.D.) (Unit: Degrees (rad)), dmin: Minimum distance (Unit: (mm))
N
R
O
A
v
Error (S.D.)
2
10
120
∞
11.1
0.20
3
10
120
∞
12.4
0.17
4
10
120
∞
8.47
0.21
5
10
120
∞
10.2
0.23
Table 2: Summary of model parameters. The averaged values of x, v, σ, dminM for each N were used for the model
parameters: N (Unit: None), x (Unit: Units), v (Unit: Units per second), Error (S.D.) (Unit: Degrees (rad)), dmin (Unit:
Units).
(a) Boid model
(b) Real ﬁsh
Figure 7: Comparison of Trajectories. For T = 20000 time steps.
18


## Page 19


A PREPRINT - DECEMBER 4, 2018
50
100
150
200
250
300
350
400
450
500
Distance (mm)
360
324
288
252
216
180
144
108
72
36
Field of View (π(rad))
0.23
0.24
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.01
0.01
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.00
0.00
0.19
0.19
0.19
0.19
0.19
0.19
0.19
0.19
0.00
0.00
0.22
0.22
0.22
0.22
0.22
0.22
0.22
0.22
0.00
0.01
0.19
0.19
0.19
0.19
0.19
0.19
0.19
0.19
0.05
0.09
0.22
0.22
0.22
0.22
0.22
0.22
0.22
0.22
0.13
0.16
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.20
0.21
0.21
0.21
0.21
0.21
0.21
0.21
0.21
0.19
0.20
0.20
0.20
0.20
0.20
0.20
0.20
0.20
0.20
0.13
0.14
0.14
0.14
0.14
0.14
0.14
0.14
0.14
0.14
N = 2
50
100
150
200
250
300
350
400
450
500
Distance (mm)
360
324
288
252
216
180
144
108
72
36
Field of View (π(rad))
0.19
0.16
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.00
0.10
0.48
0.48
0.48
0.48
0.48
0.48
0.48
0.48
0.00
0.02
0.21
0.21
0.21
0.21
0.21
0.21
0.21
0.21
0.00
0.11
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.00
0.12
0.32
0.32
0.32
0.32
0.32
0.32
0.32
0.32
0.02
0.14
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.18
0.05
0.07
0.07
0.07
0.07
0.07
0.07
0.07
0.07
0.07
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.09
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
N = 3
50
100
150
200
250
300
350
400
450
500
Distance (mm)
360
324
288
252
216
180
144
108
72
36
Field of View (π(rad))
0.26
0.38
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
1.00
1.36
1.36
1.36
1.36
1.36
1.36
1.36
1.36
0.00
0.67
1.03
1.03
1.03
1.03
1.03
1.03
1.03
1.03
0.00
0.85
1.31
1.31
1.31
1.31
1.31
1.31
1.31
1.31
0.00
0.50
1.06
1.06
1.06
1.06
1.06
1.06
1.06
1.06
0.02
0.33
0.43
0.43
0.43
0.43
0.43
0.43
0.43
0.43
0.04
0.09
0.09
0.09
0.09
0.09
0.09
0.09
0.09
0.09
0.05
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.10
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.13
0.11
0.11
0.11
0.11
0.11
0.11
0.11
0.11
0.11
N = 4
50
100
150
200
250
300
350
400
450
500
Distance (mm)
360
324
288
252
216
180
144
108
72
36
Field of View (π(rad))
0.33
0.68
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.03
2.33
2.57
2.57
2.57
2.57
2.57
2.57
2.57
2.57
0.01
2.64
2.13
2.13
2.13
2.13
2.13
2.13
2.13
2.13
0.01
2.95
2.91
2.91
2.91
2.91
2.91
2.91
2.91
2.91
0.01
2.61
4.12
4.12
4.12
4.12
4.12
4.12
4.12
4.12
0.03
1.65
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
0.04
0.39
0.39
0.39
0.39
0.39
0.39
0.39
0.39
0.39
0.05
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.14
0.12
0.12
0.12
0.12
0.12
0.12
0.12
0.12
0.24
0.20
0.20
0.20
0.20
0.20
0.20
0.20
0.20
0.20
N = 5
0.04
0.08
0.12
0.16
0.20
0.1
0.2
0.3
0.4
0.25
0.50
0.75
1.00
1.25
0.8
1.6
2.4
3.2
4.0
(a) Distance vs. Field of View heatmap
30
60
90
120
150
180
210
240
270
300
Centre of Mass (mm)
1.0
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
Average Direction (π(rad))
0.24
0.22
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.24
0.22
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.24
0.22
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.24
0.22
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.24
0.22
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.24
0.22
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.13
0.23
0.19
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.23
0.16
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.22
0.12
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.19
0.05
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
N = 2
30
60
90
120
150
180
210
240
270
300
Centre of Mass (mm)
1.0
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
Average Direction (π(rad))
0.00
0.00
0.02
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.00
0.01
0.80
0.82
0.82
0.82
0.82
0.82
0.82
0.82
0.00
0.01
0.83
0.84
0.84
0.84
0.84
0.84
0.84
0.84
0.00
0.01
0.81
0.82
0.82
0.82
0.82
0.82
0.82
0.82
0.00
0.01
0.79
0.79
0.79
0.79
0.79
0.79
0.79
0.79
0.00
0.02
0.32
0.32
0.32
0.32
0.32
0.32
0.32
0.32
0.00
0.03
0.26
0.26
0.26
0.26
0.26
0.26
0.26
0.26
0.01
0.04
0.31
0.31
0.31
0.31
0.31
0.31
0.31
0.31
0.01
0.04
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.01
0.03
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
N = 3
30
60
90
120
150
180
210
240
270
300
Centre of Mass (mm)
1.0
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
Average Direction (π(rad))
0.00
0.12
0.12
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.00
0.12
1.40
1.55
1.55
1.55
1.55
1.55
1.55
1.55
0.00
0.11
1.41
1.53
1.53
1.53
1.53
1.53
1.53
1.53
0.00
0.13
1.41
1.51
1.51
1.51
1.51
1.51
1.51
1.51
0.00
0.15
1.31
1.39
1.39
1.39
1.39
1.39
1.39
1.39
0.00
0.12
1.05
1.07
1.07
1.07
1.07
1.07
1.07
1.07
0.00
0.20
0.76
0.76
0.76
0.76
0.76
0.76
0.76
0.76
0.00
0.23
0.45
0.45
0.45
0.45
0.45
0.45
0.45
0.45
0.00
0.18
0.14
0.14
0.14
0.14
0.14
0.14
0.14
0.14
0.01
0.02
0.09
0.09
0.09
0.09
0.09
0.09
0.09
0.09
N = 4
30
60
90
120
150
180
210
240
270
300
Centre of Mass (mm)
1.0
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
Average Direction (π(rad))
0.02
0.14
1.16
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.02
0.14
2.51
2.91
2.91
2.91
2.91
2.91
2.91
2.91
0.02
0.15
2.92
2.94
2.94
2.94
2.94
2.94
2.94
2.94
0.02
0.16
3.54
3.54
3.54
3.54
3.54
3.54
3.54
3.54
0.02
0.16
4.15
4.11
4.11
4.11
4.11
4.11
4.11
4.11
0.02
0.20
4.51
4.61
4.61
4.61
4.61
4.61
4.61
4.61
0.03
0.27
3.89
3.96
3.96
3.96
3.96
3.96
3.96
3.96
0.04
0.33
2.11
2.17
2.17
2.17
2.17
2.17
2.17
2.17
0.07
0.28
0.48
0.53
0.53
0.53
0.53
0.53
0.53
0.53
0.13
0.04
0.11
0.12
0.12
0.12
0.12
0.12
0.12
0.12
N = 5
0.04
0.08
0.12
0.16
0.20
0.15
0.30
0.45
0.60
0.75
0.3
0.6
0.9
1.2
1.5
0.8
1.6
2.4
3.2
4.0
(b) The average direction vs. the centre of mass
Figure 8: Φ values of Boids model.
Dynamics of the Boids model and real ﬁsh appeared to be very similar; however, when we looked at the Φ values,
those of Boids had large variances, lacked the discontinuity between N = 3 and N = 4, and also there were signiﬁcant
differences especially comparing the N = 2. The Boids N = 2 had loose and wide distributions of Φ; however, on the
other hand, the real N = 2 had very narrow and susceptible peaks.
19


## Page 20


A PREPRINT - DECEMBER 4, 2018
5.3
Analysis of Discontinuity with other parameter settings
5.3.1
The enlarged view around Field of View = 2π (rad)
230
260
290
320
350
380
410
440
470
500
Distance (mm)
2.0
1.98
1.96
1.94
1.92
1.9
1.88
1.86
1.84
1.82
Field of View (π(rad))
0.22
0.23
0.23
0.22
0.23
0.23
0.23
0.22
0.22
0.22
0.09
0.09
0.09
0.08
0.08
0.09
0.08
0.08
0.08
0.08
0.04
0.04
0.04
0.04
0.04
0.04
0.03
0.03
0.03
0.03
0.02
0.02
0.02
0.02
0.02
0.02
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
N = 2
320
340
360
380
400
420
440
460
480
500
Distance (mm)
2.0
1.98
1.96
1.94
1.92
1.9
1.88
1.86
1.84
1.82
Field of View (π(rad))
0.19
0.18
0.19
0.18
0.21
0.20
0.20
0.22
0.16
0.14
0.12
0.14
0.16
0.09
0.08
0.10
0.09
0.09
0.11
0.13
0.06
0.07
0.07
0.06
0.05
0.06
0.08
0.08
0.07
0.09
0.05
0.04
0.05
0.03
0.04
0.05
0.06
0.06
0.06
0.08
0.03
0.03
0.03
0.03
0.04
0.04
0.05
0.06
0.05
0.07
0.02
0.02
0.02
0.03
0.03
0.04
0.05
0.05
0.05
0.06
0.02
0.02
0.02
0.02
0.03
0.04
0.05
0.04
0.04
0.05
0.02
0.02
0.02
0.02
0.02
0.02
0.04
0.04
0.04
0.04
0.01
0.01
0.01
0.02
0.02
0.02
0.02
0.02
0.02
0.03
0.01
0.01
0.01
0.01
0.01
0.01
0.02
0.02
0.02
0.02
N = 3
820
840
860
880
900
920
940
960
980
1000
Distance (mm)
2.0
1.96
1.92
1.88
1.84
1.8
1.76
1.72
1.68
1.64
Field of View (π(rad))
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.88
0.88
0.88
0.88
0.88
0.88
0.88
0.88
0.88
0.88
1.21
1.21
1.21
1.21
1.21
1.21
1.21
1.21
1.21
1.21
1.05
1.05
1.05
1.05
1.05
1.05
1.05
1.05
1.05
1.05
0.90
0.90
0.90
0.90
0.90
0.90
0.90
0.90
0.90
0.90
0.72
0.72
0.72
0.72
0.72
0.72
0.72
0.72
0.72
0.72
0.53
0.53
0.53
0.53
0.53
0.53
0.53
0.53
0.53
0.53
0.45
0.45
0.45
0.45
0.45
0.45
0.45
0.45
0.45
0.45
0.49
0.49
0.49
0.49
0.49
0.49
0.49
0.49
0.49
0.49
0.48
0.48
0.48
0.48
0.48
0.48
0.48
0.48
0.48
0.48
N = 4
820
840
860
880
900
920
940
960
980
1000
Distance (mm)
2.0
1.96
1.92
1.88
1.84
1.8
1.76
1.72
1.68
1.64
Field of View (π(rad))
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
1.09
1.09
1.09
1.10
1.10
1.10
1.10
1.10
1.10
1.10
1.81
1.81
1.80
1.82
1.81
1.81
1.81
1.81
1.81
1.81
2.10
2.10
2.11
2.11
2.11
2.11
2.11
2.11
2.11
2.11
2.05
2.05
2.02
2.03
2.02
2.03
2.03
2.03
2.03
2.03
1.90
1.89
1.91
1.91
1.89
1.89
1.90
1.90
1.90
1.90
1.95
1.95
1.97
1.97
1.97
1.96
1.97
1.97
1.97
1.97
1.82
1.83
1.83
1.83
1.83
1.83
1.83
1.83
1.83
1.85
1.84
1.84
1.84
1.84
1.84
1.84
1.84
1.84
1.84
1.84
1.86
1.86
1.86
1.86
1.86
1.86
1.86
1.86
1.86
1.86
N = 5
0.04
0.08
0.12
0.16
0.20
0.04
0.08
0.12
0.16
0.20
0.25
0.50
0.75
1.00
0.4
0.8
1.2
1.6
2.0
Figure 9: The enlarged view around Field of View = 2π (rad). The Φ distributions around Field of View = 2π rad
were enlarged to investigate the detailed behaviour of Φ values. The Φ for N = 2 and N = 3 were discontinued even if
we zoomed in at 2π rad. On the other hand, the Φ values for N = 4 and N = 5 around 2π rad were almost zero.
20


## Page 21


A PREPRINT - DECEMBER 4, 2018
5.3.2
Other parameter settings
In addition to Fig. 2, we here visualised Φ heatmap views for other parameter settings: The Field of View and Turing
Rate, and the Distance and Turing Rate.
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π (rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π (rad))
0.00
0.00
0.00
0.00
0.01
0.01
0.04
0.06
0.06
0.06
0.00
0.01
0.02
0.01
0.02
0.01
0.01
0.00
0.00
0.00
0.03
0.00
0.01
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.00
0.00
0.00
0.00
0.00
0.01
0.02
0.02
0.03
0.03
0.03
0.02
0.01
0.02
0.00
0.01
0.02
0.02
0.03
0.03
0.03
0.02
0.01
0.05
0.00
0.01
0.01
0.02
0.02
0.02
0.02
0.02
0.01
0.05
0.00
0.01
0.01
0.01
0.01
0.01
0.00
0.00
0.00
0.13
N = 2
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π (rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π (rad))
0.00
0.00
0.00
0.00
0.01
0.01
0.02
0.02
0.02
0.02
0.00
0.02
0.04
0.03
0.02
0.04
0.04
0.04
0.04
0.04
0.07
0.02
0.01
0.00
0.00
0.00
0.00
0.01
0.01
0.01
0.03
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.02
0.01
0.01
0.02
0.03
0.03
0.02
0.01
0.00
0.00
0.01
0.01
0.01
0.02
0.03
0.04
0.04
0.03
0.00
0.01
0.01
0.00
0.00
0.01
0.02
0.02
0.04
0.05
0.03
0.18
0.01
0.00
0.00
0.00
0.01
0.02
0.01
0.02
0.06
0.03
N = 3
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π (rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π (rad))
0.00
0.02
0.04
0.04
0.05
0.06
0.06
0.05
0.05
0.05
0.01
0.06
0.07
0.11
0.10
0.11
0.12
0.12
0.10
0.12
0.11
0.06
0.02
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.09
0.01
0.01
0.01
0.00
0.00
0.00
0.00
0.01
0.01
0.03
0.01
0.02
0.02
0.04
0.04
0.03
0.01
0.01
0.01
0.02
0.01
0.01
0.02
0.03
0.03
0.07
0.04
0.05
0.05
0.02
0.01
0.01
0.01
0.03
0.07
0.12
0.19
0.23
0.53
0.01
0.00
0.00
0.01
0.07
0.12
0.30
0.51
0.72
0.01
N = 4
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π (rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π (rad))
0.04
0.10
0.16
0.23
0.32
0.33
0.37
0.37
0.37
0.37
0.07
0.17
0.25
0.29
0.40
0.53
0.55
0.51
0.50
0.50
0.39
0.21
0.07
0.03
0.02
0.03
0.04
0.04
0.04
0.04
0.14
0.03
0.02
0.01
0.01
0.01
0.02
0.02
0.03
0.03
0.06
0.02
0.03
0.05
0.07
0.07
0.07
0.08
0.19
0.30
0.05
0.02
0.03
0.06
0.09
0.13
0.19
0.25
0.43
0.67
0.04
0.01
0.02
0.05
0.09
0.29
0.49
0.74
1.03
1.10
0.04
0.01
0.02
0.10
0.56
1.05
1.80
1.84
1.90
0.00
N = 5
0.025
0.050
0.075
0.100
0.125
0.04
0.08
0.12
0.16
0.15
0.30
0.45
0.60
0.4
0.8
1.2
1.6
(a) Field of View vs. Turning Rate
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π (rad))
0.06
0.05
0.05
0.05
0.06
0.06
0.06
0.06
0.06
0.06
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.02
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.04
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.11
0.07
0.04
0.03
0.02
0.02
0.02
0.02
0.02
0.02
0.12
0.10
0.07
0.06
0.05
0.05
0.05
0.05
0.05
0.05
0.11
0.10
0.08
0.07
0.06
0.06
0.05
0.06
0.06
0.05
0.22
0.22
0.23
0.23
0.22
0.13
0.13
0.13
0.13
0.13
N = 2
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π (rad))
0.02
0.02
0.01
0.01
0.01
0.02
0.02
0.02
0.02
0.02
0.03
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.06
0.07
0.04
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.07
0.10
0.10
0.03
0.01
0.01
0.01
0.01
0.01
0.01
0.08
0.10
0.13
0.17
0.16
0.16
0.18
0.18
0.18
0.18
0.18
0.19
0.19
0.21
0.14
0.05
0.05
0.07
0.02
0.03
N = 3
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π (rad))
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.10
0.11
0.12
0.12
0.12
0.12
0.12
0.12
0.12
0.12
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.02
0.06
0.02
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.03
0.07
0.07
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.03
0.09
0.27
0.44
0.52
0.52
0.53
0.53
0.53
0.53
0.25
0.29
0.23
0.31
0.11
0.00
0.01
0.01
0.01
0.01
N = 4
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π (rad))
0.38
0.37
0.37
0.37
0.37
0.37
0.37
0.37
0.37
0.37
0.60
0.53
0.53
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.16
0.19
0.28
0.29
0.30
0.30
0.30
0.30
0.30
0.03
0.42
0.57
0.66
0.66
0.67
0.67
0.67
0.67
0.67
0.03
0.84
1.05
1.08
1.09
1.10
1.10
1.10
1.10
1.10
0.27
1.45
0.98
0.78
0.39
0.04
0.00
0.00
0.00
0.00
N = 5
0.04
0.08
0.12
0.16
0.20
0.04
0.08
0.12
0.16
0.20
0.1
0.2
0.3
0.4
0.5
0.25
0.50
0.75
1.00
1.25
(b) Distance vs. Turning Rate
Figure 10: Other parameter settings in the same manner as Fig. 2.
21


## Page 22


A PREPRINT - DECEMBER 4, 2018
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
0.15
0.15
0.16
0.16
0.17
0.17
0.17
0.17
0.17
0.17
0.00
0.00
0.00
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.01
0.02
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.04
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.08
0.09
0.08
0.07
0.07
0.07
0.06
0.06
0.07
0.07
0.17
0.16
0.09
0.07
0.07
0.07
0.07
0.07
0.07
0.07
0.19
0.17
0.09
0.07
0.07
0.07
0.07
0.07
0.07
0.07
0.15
0.20
0.16
0.11
0.11
0.11
0.11
0.11
0.11
0.11
N = 2
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
0.22
0.26
0.22
0.32
0.21
0.07
0.08
0.03
0.03
0.03
0.01
0.01
0.02
0.05
0.05
0.14
0.16
0.18
0.17
0.17
0.00
0.01
0.02
0.08
0.04
0.04
0.06
0.07
0.07
0.08
0.00
0.01
0.01
0.04
0.07
0.04
0.04
0.04
0.05
0.05
0.00
0.01
0.02
0.05
0.10
0.11
0.12
0.12
0.12
0.12
0.00
0.02
0.02
0.03
0.03
0.03
0.04
0.04
0.04
0.04
0.01
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.01
0.01
0.01
0.01
0.01
0.01
0.09
0.03
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.11
0.08
0.09
0.09
0.09
0.09
0.09
0.09
0.09
0.09
N = 3
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
0.27
0.37
0.29
0.39
0.13
0.00
0.01
0.01
0.01
0.01
0.00
0.21
0.44
0.55
0.80
0.87
0.88
0.88
0.88
0.88
0.00
0.04
0.18
0.32
0.50
0.52
0.52
0.52
0.52
0.52
0.00
0.02
0.07
0.23
0.32
0.33
0.34
0.34
0.34
0.34
0.00
0.02
0.04
0.10
0.10
0.09
0.09
0.09
0.09
0.09
0.00
0.02
0.04
0.05
0.06
0.06
0.04
0.04
0.04
0.05
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.05
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.15
0.06
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
N = 4
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
0.33
1.48
0.77
0.32
0.34
0.03
0.00
0.00
0.00
0.00
0.01
1.42
1.89
1.77
1.88
1.86
2.04
2.03
2.03
2.04
0.01
0.76
1.84
1.74
1.59
1.73
1.80
1.64
1.66
1.67
0.01
0.63
1.78
1.90
1.95
2.13
2.21
2.15
2.15
2.15
0.00
0.42
1.37
1.41
1.42
1.52
1.53
1.53
1.53
1.57
0.00
0.20
0.44
0.51
0.55
0.63
0.63
0.63
0.63
0.70
0.01
0.06
0.11
0.11
0.12
0.10
0.10
0.10
0.10
0.10
0.01
0.02
0.02
0.02
0.02
0.03
0.03
0.03
0.03
0.03
0.08
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.55
0.07
0.06
0.05
0.05
0.05
0.05
0.05
0.05
0.05
N = 5
0.04
0.08
0.12
0.16
0.20
0.06
0.12
0.18
0.24
0.30
0.15
0.30
0.45
0.60
0.75
0.4
0.8
1.2
1.6
2.0
Figure 11: Distance vs. Field of View with Time scale ∆t = 0.1. The most remarkable point here was that when
N = 2 Φ heatmap of The Distance vs. Field of View showed the followership instead of leadership seen in Fig. 2.
22


## Page 23


A PREPRINT - DECEMBER 4, 2018
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.03
0.03
0.03
0.01
0.03
0.04
0.04
0.01
0.00
0.00
0.01
0.01
0.01
0.08
0.03
0.02
0.03
0.03
0.01
0.01
0.00
0.00
0.02
0.11
0.07
0.06
0.06
0.06
0.03
0.02
0.01
0.00
0.02
0.10
0.06
0.06
0.07
0.08
0.05
0.04
0.04
0.02
0.06
0.11
0.07
0.07
0.07
0.07
0.04
0.04
0.03
0.02
0.07
0.11
0.07
0.07
0.07
0.06
0.03
0.03
0.02
0.02
0.19
0.11
0.07
0.07
0.07
0.06
0.03
0.02
0.01
0.01
0.17
N = 2
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.00
0.02
0.03
0.04
0.03
0.04
0.07
0.07
0.07
0.03
0.07
0.14
0.09
0.04
0.02
0.02
0.01
0.01
0.01
0.12
0.03
0.01
0.01
0.01
0.01
0.01
0.02
0.03
0.03
0.09
0.02
0.02
0.02
0.02
0.01
0.01
0.00
0.01
0.02
0.09
0.02
0.02
0.03
0.06
0.07
0.06
0.05
0.03
0.19
0.10
0.02
0.02
0.02
0.04
0.09
0.11
0.10
0.14
0.26
0.09
0.02
0.01
0.02
0.04
0.08
0.09
0.10
0.12
0.50
0.09
0.02
0.01
0.02
0.04
0.12
0.05
0.08
0.17
0.03
N = 3
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.01
0.01
0.01
0.02
0.02
0.02
0.06
0.06
0.06
0.01
0.05
0.10
0.15
0.24
0.24
0.27
0.26
0.25
0.24
0.13
0.03
0.02
0.01
0.01
0.01
0.02
0.02
0.02
0.02
0.09
0.01
0.01
0.01
0.01
0.00
0.00
0.01
0.01
0.01
0.06
0.01
0.02
0.03
0.05
0.06
0.06
0.05
0.12
0.24
0.06
0.01
0.01
0.02
0.08
0.08
0.16
0.15
0.27
0.57
0.06
0.01
0.01
0.02
0.06
0.07
0.18
0.30
0.80
1.09
0.05
0.01
0.01
0.01
0.05
0.09
0.34
0.52
0.88
0.01
N = 4
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.03
0.03
0.09
0.11
0.17
0.18
0.16
0.16
0.16
0.06
0.29
0.41
0.47
0.47
0.61
0.58
0.60
0.60
0.59
0.45
0.13
0.05
0.04
0.06
0.08
0.10
0.12
0.12
0.11
0.19
0.07
0.02
0.02
0.02
0.02
0.04
0.06
0.06
0.06
0.06
0.03
0.04
0.10
0.19
0.21
0.25
0.29
0.51
0.90
0.06
0.02
0.03
0.11
0.29
0.45
0.54
0.68
1.52
1.84
0.05
0.01
0.03
0.09
0.25
0.73
1.11
1.38
1.82
1.88
0.05
0.01
0.03
0.10
0.70
1.57
2.15
1.67
2.04
0.00
N = 5
0.04
0.08
0.12
0.16
0.1
0.2
0.3
0.4
0.5
0.2
0.4
0.6
0.8
1.0
0.4
0.8
1.2
1.6
2.0
(a) Field of View vs. Turning Rate
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.01
0.02
0.02
0.03
0.03
0.03
0.03
0.03
0.03
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.05
0.03
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.08
0.04
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.13
0.13
0.11
0.09
0.08
0.06
0.06
0.06
0.06
0.06
0.13
0.15
0.15
0.15
0.13
0.07
0.07
0.07
0.07
0.07
0.14
0.16
0.17
0.17
0.17
0.18
0.19
0.19
0.19
0.19
0.15
0.15
0.16
0.16
0.17
0.17
0.17
0.17
0.17
0.17
N = 2
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.06
0.06
0.06
0.07
0.07
0.07
0.07
0.07
0.07
0.07
0.02
0.02
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.02
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.06
0.10
0.15
0.24
0.21
0.21
0.20
0.19
0.19
0.19
0.06
0.09
0.18
0.20
0.24
0.24
0.27
0.27
0.26
0.26
0.08
0.17
0.21
0.32
0.30
0.32
0.43
0.42
0.45
0.50
0.22
0.26
0.22
0.32
0.21
0.07
0.08
0.03
0.03
0.03
N = 3
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.07
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.24
0.23
0.25
0.25
0.25
0.24
0.24
0.24
0.24
0.24
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.03
0.10
0.18
0.20
0.21
0.22
0.24
0.24
0.24
0.24
0.03
0.12
0.31
0.54
0.56
0.57
0.57
0.57
0.57
0.57
0.04
0.15
0.68
0.94
1.04
1.03
1.09
1.09
1.09
1.09
0.27
0.37
0.29
0.39
0.13
0.00
0.01
0.01
0.01
0.01
N = 4
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.15
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.16
0.59
0.57
0.59
0.59
0.59
0.59
0.59
0.59
0.59
0.59
0.09
0.11
0.11
0.11
0.11
0.11
0.11
0.11
0.11
0.11
0.07
0.05
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.04
0.58
0.86
0.87
0.88
0.89
0.89
0.89
0.89
0.90
0.04
1.61
1.77
1.80
1.82
1.83
1.83
1.84
1.84
1.84
0.07
1.76
1.80
1.85
1.86
1.87
1.88
1.88
1.88
1.88
0.33
1.48
0.77
0.32
0.34
0.03
0.00
0.00
0.00
0.00
N = 5
0.04
0.08
0.12
0.16
0.1
0.2
0.3
0.4
0.5
0.2
0.4
0.6
0.8
1.0
0.4
0.8
1.2
1.6
(b) Distance vs. Turning Rate
Figure 12: Time scale ∆t = 0.1. with other parameter settings.
23


## Page 24


A PREPRINT - DECEMBER 4, 2018
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
0.15
0.15
0.16
0.16
0.17
0.17
0.17
0.17
0.17
0.17
0.00
0.00
0.00
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.01
0.02
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.04
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.08
0.09
0.08
0.07
0.07
0.07
0.06
0.06
0.07
0.07
0.17
0.16
0.09
0.07
0.07
0.07
0.07
0.07
0.07
0.07
0.19
0.17
0.09
0.07
0.07
0.07
0.07
0.07
0.07
0.07
0.15
0.20
0.16
0.11
0.11
0.11
0.11
0.11
0.11
0.11
N = 2
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
0.22
0.26
0.22
0.32
0.21
0.07
0.08
0.03
0.03
0.03
0.01
0.01
0.02
0.05
0.05
0.14
0.16
0.18
0.17
0.17
0.00
0.01
0.02
0.08
0.04
0.04
0.06
0.07
0.07
0.08
0.00
0.01
0.01
0.04
0.07
0.04
0.04
0.04
0.05
0.05
0.00
0.01
0.02
0.05
0.10
0.11
0.12
0.12
0.12
0.12
0.00
0.02
0.02
0.03
0.03
0.03
0.04
0.04
0.04
0.04
0.01
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.01
0.01
0.01
0.01
0.01
0.01
0.09
0.03
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.11
0.08
0.09
0.09
0.09
0.09
0.09
0.09
0.09
0.09
N = 3
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
0.30
0.50
0.44
0.56
0.15
0.01
0.01
0.01
0.01
0.01
0.01
0.32
0.46
0.79
1.09
1.07
1.07
1.07
1.07
1.07
0.01
0.07
0.32
0.46
0.60
0.58
0.59
0.60
0.60
0.60
0.00
0.08
0.23
0.36
0.54
0.55
0.56
0.56
0.56
0.56
0.00
0.05
0.12
0.16
0.18
0.18
0.18
0.18
0.18
0.18
0.01
0.07
0.10
0.12
0.11
0.13
0.09
0.09
0.09
0.09
0.01
0.03
0.03
0.03
0.03
0.03
0.04
0.04
0.04
0.04
0.05
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.07
0.02
0.02
0.02
0.01
0.01
0.01
0.01
0.01
0.01
0.22
0.11
0.10
0.10
0.09
0.09
0.09
0.09
0.09
0.09
N = 4
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
0.43
2.06
1.00
0.64
0.35
0.11
0.00
0.00
0.00
0.00
0.04
1.21
1.96
2.00
2.15
2.11
2.15
2.17
2.18
2.19
0.02
0.65
1.96
1.60
1.96
2.10
2.05
2.04
2.13
2.12
0.02
0.71
1.91
2.21
2.52
2.58
2.65
2.66
2.68
2.68
0.01
0.46
1.30
1.54
1.71
1.77
1.78
1.78
1.78
1.82
0.01
0.24
0.59
0.73
0.76
0.85
0.85
0.85
0.86
1.04
0.01
0.09
0.18
0.22
0.22
0.24
0.24
0.24
0.24
0.25
0.04
0.04
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.06
0.13
0.02
0.03
0.02
0.03
0.02
0.02
0.02
0.02
0.02
0.74
0.14
0.10
0.03
0.03
0.03
0.03
0.03
0.03
0.03
N = 5
0.04
0.08
0.12
0.16
0.20
0.06
0.12
0.18
0.24
0.30
0.2
0.4
0.6
0.8
1.0
0.5
1.0
1.5
2.0
2.5
Figure 13: Distance vs. Field of View with Time scale ∆t = 0.2.
24


## Page 25


A PREPRINT - DECEMBER 4, 2018
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.03
0.03
0.03
0.01
0.03
0.04
0.04
0.01
0.00
0.00
0.01
0.01
0.01
0.08
0.03
0.02
0.03
0.03
0.01
0.01
0.00
0.00
0.02
0.11
0.07
0.06
0.06
0.06
0.03
0.02
0.01
0.00
0.02
0.10
0.06
0.06
0.07
0.08
0.05
0.04
0.04
0.02
0.06
0.11
0.07
0.07
0.07
0.07
0.04
0.04
0.03
0.02
0.07
0.11
0.07
0.07
0.07
0.06
0.03
0.03
0.02
0.02
0.19
0.11
0.07
0.07
0.07
0.06
0.03
0.02
0.01
0.01
0.17
N = 2
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.00
0.02
0.03
0.04
0.03
0.04
0.07
0.07
0.07
0.03
0.07
0.14
0.09
0.04
0.02
0.02
0.01
0.01
0.01
0.12
0.03
0.01
0.01
0.01
0.01
0.01
0.02
0.03
0.03
0.09
0.02
0.02
0.02
0.02
0.01
0.01
0.00
0.01
0.02
0.09
0.02
0.02
0.03
0.06
0.07
0.06
0.05
0.03
0.19
0.10
0.02
0.02
0.02
0.04
0.09
0.11
0.10
0.14
0.26
0.09
0.02
0.01
0.02
0.04
0.08
0.09
0.10
0.12
0.50
0.09
0.02
0.01
0.02
0.04
0.12
0.05
0.08
0.17
0.03
N = 3
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.00
0.00
0.01
0.01
0.01
0.02
0.02
0.02
0.02
0.10
0.22
0.28
0.36
0.28
0.23
0.20
0.23
0.23
0.21
0.13
0.03
0.01
0.01
0.01
0.02
0.03
0.05
0.06
0.05
0.10
0.02
0.02
0.02
0.02
0.01
0.01
0.02
0.03
0.03
0.09
0.02
0.03
0.05
0.09
0.17
0.16
0.20
0.53
0.80
0.09
0.02
0.02
0.04
0.19
0.23
0.34
0.45
0.66
1.16
0.09
0.02
0.02
0.04
0.10
0.20
0.44
0.81
1.23
1.39
0.09
0.01
0.02
0.04
0.09
0.18
0.56
0.60
1.07
0.01
N = 4
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.00
0.02
0.03
0.06
0.07
0.08
0.09
0.09
0.09
0.19
0.83
0.94
0.90
0.84
0.82
0.72
0.70
0.67
0.66
0.28
0.06
0.04
0.05
0.07
0.12
0.17
0.24
0.27
0.25
0.15
0.04
0.03
0.05
0.06
0.07
0.10
0.17
0.24
0.21
0.08
0.02
0.04
0.16
0.29
0.57
0.71
1.11
1.84
1.95
0.03
0.03
0.08
0.22
0.67
1.20
1.89
2.14
3.04
5.37
0.03
0.02
0.07
0.19
0.68
1.75
2.20
2.61
4.36
4.70
0.03
0.02
0.06
0.25
1.04
1.82
2.68
2.12
2.19
0.00
N = 5
0.04
0.08
0.12
0.16
0.1
0.2
0.3
0.4
0.5
0.25
0.50
0.75
1.00
1.25
1
2
3
4
5
(a) Field of View vs. Turning Rate
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.01
0.02
0.02
0.03
0.03
0.03
0.03
0.03
0.03
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.05
0.03
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.08
0.04
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.13
0.13
0.11
0.09
0.08
0.06
0.06
0.06
0.06
0.06
0.13
0.15
0.15
0.15
0.13
0.07
0.07
0.07
0.07
0.07
0.14
0.16
0.17
0.17
0.17
0.18
0.19
0.19
0.19
0.19
0.15
0.15
0.16
0.16
0.17
0.17
0.17
0.17
0.17
0.17
N = 2
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.06
0.06
0.06
0.07
0.07
0.07
0.07
0.07
0.07
0.07
0.02
0.02
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.02
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.06
0.10
0.15
0.24
0.21
0.21
0.20
0.19
0.19
0.19
0.06
0.09
0.18
0.20
0.24
0.24
0.27
0.27
0.26
0.26
0.08
0.17
0.21
0.32
0.30
0.32
0.43
0.42
0.45
0.50
0.22
0.26
0.22
0.32
0.21
0.07
0.08
0.03
0.03
0.03
N = 3
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.01
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.02
0.25
0.19
0.18
0.20
0.21
0.21
0.21
0.21
0.21
0.21
0.04
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.03
0.02
0.32
0.82
0.84
0.80
0.80
0.80
0.80
0.80
0.80
0.03
0.56
0.84
1.08
1.10
1.13
1.16
1.16
1.16
1.16
0.10
0.70
1.16
1.17
1.22
1.29
1.39
1.39
1.39
1.39
0.30
0.50
0.44
0.56
0.15
0.01
0.01
0.01
0.01
0.01
N = 4
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.06
0.08
0.09
0.09
0.09
0.09
0.09
0.09
0.09
0.09
0.85
0.67
0.68
0.66
0.66
0.66
0.66
0.66
0.66
0.66
0.16
0.24
0.25
0.26
0.25
0.25
0.25
0.25
0.25
0.25
0.12
0.22
0.22
0.22
0.22
0.21
0.21
0.21
0.21
0.21
0.05
1.66
1.99
2.01
2.02
2.03
1.92
1.93
1.95
1.95
0.09
2.45
3.74
4.39
4.44
4.60
5.33
5.33
5.37
5.37
0.18
2.91
4.13
4.42
4.52
4.56
4.69
4.69
4.70
4.70
0.43
2.06
1.00
0.64
0.35
0.11
0.00
0.00
0.00
0.00
N = 5
0.04
0.08
0.12
0.16
0.1
0.2
0.3
0.4
0.5
0.25
0.50
0.75
1.00
1.25
1
2
3
4
5
(b) Distance vs. Turning Rate
Figure 14: Time scale ∆t = 0.2. with other parameter settings.
25


## Page 26


A PREPRINT - DECEMBER 4, 2018
5.3.3
Concept
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
2.00
2.00
2.00
2.00
2.00
1.67
1.67
1.67
1.67
1.67
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
N = 2
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
7.00
7.00
7.00
7.00
5.31
2.91
2.91
2.91
1.47
1.47
7.00
7.00
7.00
7.00
6.50
6.38
6.50
6.50
6.50
6.50
7.00
7.00
7.00
7.00
6.88
6.88
6.88
6.88
6.88
6.88
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
N = 3
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
15.00 14.56 10.52
8.56
3.00
0.54
0.50
0.50
0.50
0.50
15.00 14.96 14.71 14.19 13.65 13.85 13.85 13.85 13.85 13.85
15.00 14.96 15.00 14.96 14.94 14.94 14.94 14.94 14.94 14.94
15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00
15.00 15.00 15.00 14.96 14.92 14.92 14.92 14.92 14.92 14.92
15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00
15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00
15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00
15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00
15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00 15.00
N = 4
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
31.00 30.42 17.30 12.32
7.89
2.48
0.33
0.33
0.33
0.33
31.00 30.85 29.20 28.78 28.51 28.12 28.57 28.57 28.47 28.47
31.00 30.81 30.28 29.77 29.65 29.71 29.54 29.21 29.21 29.21
31.00 30.85 30.75 30.70 30.69 30.67 30.67 30.77 30.77 30.77
31.00 30.97 30.92 30.52 30.52 30.58 30.55 30.55 30.55 30.68
31.00 30.98 30.98 30.98 30.98 30.98 30.98 30.98 30.98 30.98
31.00 31.00 31.00 31.00 31.00 31.00 31.00 31.00 31.00 31.00
31.00 31.00 31.00 31.00 31.00 31.00 31.00 31.00 31.00 31.00
31.00 31.00 31.00 31.00 31.00 31.00 31.00 31.00 31.00 31.00
31.00 31.00 31.00 31.00 31.00 31.00 31.00 31.00 31.00 31.00
N = 5
1.68
1.74
1.80
1.86
1.92
1.98
2
3
4
5
6
7
2.5
5.0
7.5
10.0
12.5
15.0
6
12
18
24
30
Figure 15: The Number of Concepts: Mechanisms that specify maximally irreducible cause and effect (MICE)
repertoires: Distance vs. Field of View. "PyPhi.Subsystem.concept()" was used to comupute Concepts. The number
of concepts were assessed here. Some of parameter settings have a large number of concepts; the Φ values still remain
low. This perhaps implies a potential of having larger Φ’s.
26


## Page 27


A PREPRINT - DECEMBER 4, 2018
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
1.67
N = 2
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
2.91
4.16
4.34
4.44
4.72
4.72
4.72
4.72
4.72
4.72
4.84
5.31
5.69
6.12
6.50
6.62
6.62
6.62
6.88
6.88
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
6.88
6.50
1.47
N = 3
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
8.73
9.27
9.31
9.85
10.27
10.27
10.27
10.27
10.27
10.27
9.94
12.00
12.00
13.27
13.35
14.27
14.65
14.65
14.65
14.65
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
14.92
15.00
14.94
13.85
0.50
N = 4
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
19.02
20.79
22.06
22.54
23.08
23.10
23.10
23.11
23.11
23.11
23.19
23.81
25.50
25.95
27.51
27.44
29.23
29.32
29.56
29.56
30.97
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
30.98
30.68
30.77
29.21
28.47
0.33
N = 5
1.68
1.74
1.80
1.86
1.92
1.98
2
3
4
5
6
7
2.5
5.0
7.5
10.0
12.5
15.0
6
12
18
24
30
(a) Field of View vs. Turning Rate
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
2.00
1.67
1.67
1.67
1.67
1.67
N = 2
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
4.62
4.62
4.62
4.62
4.62
4.72
4.72
4.72
4.72
4.72
6.69
6.75
6.88
6.88
6.88
6.88
6.88
6.88
6.88
6.88
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
7.00
5.31
2.91
2.91
2.91
1.47
1.47
N = 3
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
10.27
10.27
10.27
10.27
10.27
10.27
10.27
10.27
10.27
10.27
14.46
14.65
14.65
14.65
14.65
14.65
14.65
14.65
14.65
14.65
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
15.00
14.56
10.52
8.56
3.00
0.54
0.50
0.50
0.50
0.50
N = 4
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
22.73
23.11
23.11
23.11
23.11
23.11
23.11
23.11
23.11
23.11
29.56
29.56
29.56
29.56
29.56
29.56
29.56
29.56
29.56
29.56
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
31.00
30.42
17.30
12.32
7.89
2.48
0.33
0.33
0.33
0.33
N = 5
1.68
1.74
1.80
1.86
1.92
1.98
2
3
4
5
6
7
2.5
5.0
7.5
10.0
12.5
15.0
6
12
18
24
30
(b) Distance vs. Turning Rate
Figure 16: The Number of Concepts: Mechanisms that specify maximally irreducible cause and effect (MICE)
repertoires: Other parameter settings. "PyPhi.Subsystem.concept()" was used to comupute Concepts.
27


## Page 28


A PREPRINT - DECEMBER 4, 2018
5.3.4
Susceptibility
Susceptibility is the measure of ﬂuctuations or the response of an extensive property such as the order parameter to
a small external perturbation to give variation of an intensive property. Power-law divergences of quantities like the
magnetic susceptibility in the ferromagnetic phase transition in critical phenomena are well-known. The magnetic
susceptibility per spin of Ising model (Eq. 5) is deﬁned as the derivative of the average total magnetisation with respect
to the external ﬁeld at ﬁxed temperature and related to the variance of the average total magnetisation through the
ﬂuctuation-dissipation theorem,
χ : = 1
N
∂⟨M⟩
∂H

T
= kBT
N
 ⟨M 2⟩−⟨M⟩2
(5)
In the recent work by Khajehabdollahi [70], Φ of the small Ising model was interpreted as an order parameter and the
author discovered that the critical temperature maximises the susceptibility of Φ (Eq. 6).
σ2(Φ) = ⟨Φ2⟩−⟨Φ⟩2
(6)
Φ susceptibility of real ﬁsh school was assessed here. The large susceptibilities of Φ are mostly corresponding to the
large Φ values; however, it is interesting to see they do not simply correspond to each other.
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
0.00
0.00
0.00
0.01
0.00
0.01
0.01
0.01
0.01
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
N = 2
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
0.03
0.04
0.04
0.05
0.02
0.00
0.00
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.02
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
N = 3
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
0.13
0.10
0.03
0.08
0.05
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.07
0.09
0.07
0.10
0.10
0.10
0.10
0.10
0.00
0.00
0.01
0.18
0.31
0.32
0.32
0.32
0.32
0.32
0.00
0.00
0.00
0.00
0.15
0.15
0.15
0.15
0.15
0.15
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
N = 4
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
Field of View (π(rad))
0.37
0.40
0.89
0.71
0.60
0.02
0.00
0.00
0.00
0.00
0.00
0.16
0.52
0.78
0.96
1.15
1.35
1.33
1.39
1.39
0.00
0.07
0.31
0.52
0.54
0.62
0.70
0.57
0.57
0.57
0.00
0.07
0.27
0.44
0.52
0.54
0.56
0.49
0.49
0.49
0.00
0.06
0.40
0.33
0.34
0.39
0.23
0.23
0.23
0.26
0.00
0.00
0.09
0.49
0.51
0.54
0.54
0.54
0.54
0.56
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.05
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
N = 5
0.002
0.004
0.006
0.008
0.010
0.008
0.016
0.024
0.032
0.040
0.06
0.12
0.18
0.24
0.30
0.25
0.50
0.75
1.00
1.25
Figure 17: Susceptibility: Distance vs. Field of View.
28


## Page 29


A PREPRINT - DECEMBER 4, 2018
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
N = 2
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.04
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
N = 3
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.01
0.01
0.01
0.00
0.01
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.04
0.03
0.16
0.00
0.00
0.00
0.00
0.00
0.00
0.15
0.32
0.10
0.00
N = 4
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Field of View (π(rad))
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.00
0.01
0.01
0.02
0.03
0.04
0.04
0.04
0.04
0.00
0.01
0.02
0.02
0.05
0.12
0.12
0.10
0.10
0.10
0.06
0.04
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.02
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.17
0.36
0.00
0.00
0.00
0.00
0.00
0.01
0.02
0.06
0.31
0.55
0.00
0.00
0.00
0.00
0.00
0.08
0.22
0.49
0.55
0.48
0.00
0.00
0.00
0.00
0.56
0.26
0.49
0.57
1.39
0.00
N = 5
0.002
0.004
0.006
0.008
0.010
0.008
0.016
0.024
0.032
0.040
0.06
0.12
0.18
0.24
0.30
0.25
0.50
0.75
1.00
1.25
(a) Field of View vs. Turning Rate
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.01
0.01
0.01
0.01
0.01
N = 2
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.02
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.02
0.03
0.04
0.04
0.05
0.04
0.05
0.04
0.03
0.04
0.04
0.05
0.02
0.00
0.00
0.01
0.00
0.00
N = 3
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.01
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.07
0.11
0.12
0.13
0.16
0.16
0.16
0.16
0.13
0.10
0.03
0.08
0.05
0.00
0.00
0.00
0.00
0.00
N = 4
100
200
300
400
500
600
700
800
900
1000
Distance (mm)
1.0
0.5
0.1
0.05
0.01
0.005
0.001
0.0
Turning Rate (π(rad))
0.05
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.14
0.11
0.11
0.10
0.10
0.10
0.10
0.10
0.10
0.10
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.00
0.12
0.18
0.33
0.36
0.38
0.36
0.36
0.36
0.36
0.00
0.17
0.42
0.54
0.55
0.55
0.55
0.55
0.55
0.55
0.00
0.56
0.38
0.46
0.48
0.48
0.48
0.48
0.48
0.48
0.37
0.40
0.89
0.71
0.60
0.02
0.00
0.00
0.00
0.00
N = 5
0.002
0.004
0.006
0.008
0.010
0.008
0.016
0.024
0.032
0.040
0.03
0.06
0.09
0.12
0.15
0.15
0.30
0.45
0.60
0.75
(b) Distance vs. Turning Rate
Figure 18: Susceptibility with other parameter settings.
29


## Page 30


A PREPRINT - DECEMBER 4, 2018
5.4
Φ(N) increase with the group size N
The mean values and the standard deviations of integrate information Φ increase as the size of ﬁsh school N increases.
2
3
4
5
N
0.0
0.5
1.0
1.5
2.0
2.5
Mean PHI value
2
3
4
5
N
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Std PHI value
2
3
4
5
N
0
1
2
3
4
5
6
7
8
Max PHI value
2
3
4
5
N
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Min PHI value
Figure 19: Mean Values ¯ΦN , Standard deviation σ(Φ)N, Max Values max{Φ}N, and Min Values min{Φ}N. The
value was calculated for each group. Groups N = 2, N = 4,N = 5 have 3 samples and Group N = 3 has 4 samples.
Parameters were picked up from the peak values of Φ-dist map
30


## Page 31


A PREPRINT - DECEMBER 4, 2018
5.5
A short summary of integrated information Φ
Integrated information theory models a system S by a discrete time multivariate stochastic process:
p(X0, X∆t, . . . , Xt, Xt+∆t, . . . , XT )
(7)
that fulﬁls the Markov property:
p(X0, X∆t, . . . , Xt, Xt+∆t, . . . , XT ) = p(X0)
T
Y
t=∆t
p(Xt | Xt−∆t)
(8)
Such a discrete dynamical system S is deﬁned by a directed graph of interconnected nodes (in this study we assumed a
complete graph.) and its transition probability matrix (TPM). The TPM speciﬁes the conditional probability distribution
p(Xt | Xt−∆t). Each state vector Xt comprises binary variables xti,i = 1, 2, . . . , n(n ∈N).
A joint distribution pcasue−eﬀect is deﬁned
pcause−eﬀect(Xt−∆t, Xt) := pu(Xt−∆t)peﬀect(Xt | Xt−∆t)
(9)
The marginal distribution pu(Xt−∆t) is an uniform distribution to give the maximum entropy distribution.
From the joint probability above
the backward transitional probability distribution
peﬀect(Xt−∆t | Xt) :=
pcasue−eﬀect(Xt−∆t, Xt)
P
Xt−∆t pcasue−eﬀect(Xt−∆t, Xt)
(10)
and the forward transitional probability distribution
pcause(Xt | Xt−∆t) := p((Xt | Xt−∆t))
(11)
are constructed and referred to as the cause repertoire and the effect repertoire of state Xt, respectively. The cause
repertoire and the effect repertoire are calculated for a set of nodes within the subsystem, or a mechanism M ⊆S, over
another set of nodes within the subsystem, or a purview of the mechanism.
After assessing the information of a mechanism over a purview we next consider its integrated information φcause−eﬀect
of a set of system elements in a state X deﬁned as
φcause−eﬀect := min{φeﬀect, φcause}
(12)
φeﬀect := min
i∈I {D

peﬀect || p(i)
eﬀect

}
(13)
φcause := min
i∈I {D

pcause || p(i)
cause

}
(14)
where the system is decomposed by all possible ways into I.
The integrated information φ is assessed by quantifying the extent to which the cause and effect repertoires of the
mechanism-purview pair can be reduced to the repertoires of its parts. The amount of irreducibility of a mechanism
over a purview with respect to a partition is quantiﬁed as the divergence between the unpartioned repertoire p and
the partitioned repertoire p(i). The partition that yields the minimum irreducibility is called the minimum-information
partition (MIP). The integrated information φ of a mechanism-purview pair is deﬁned as the divergence between the
unpartitioned repertoire and the repertoires partitioned by MIP. The maximum φ value is then searched over all possible
purviews to ﬁnd maximally-irreducible cause (MIC) and maximally-irreducible effect (MIE) speciﬁed by a mechanism.
φmax
cause := max
j∈C {φj
cause}, φmax
eﬀect := max
j∈C {φj
eﬀect}
(15)
where C = 2N −1 (In this paper we adopted a "cut one" approximation which only evaluates 2N bipartitions severing
the edges from a single node to the rest of the network.).
31


## Page 32


A PREPRINT - DECEMBER 4, 2018
The φ value of the concept as a whole or the maximally integrated cause-effect information is the minimum of maximally
integrated cause information φcause and maximally integrated effect information φeﬀect.
φmax
cause−eﬀect := min{φmax
cause, φmax
eﬀect}
(16)
If the mechanism’s MIC has φcause > 0 and its MIE has φeﬀect > 0, (equivalently φmax
cause−eﬀect > 0) then the
mechanism is said to specify a concept.
We then compute the cause-effect structure (CES), the set of all concepts speciﬁed by the subsystem characterising
all of the causal constraints intrinsic to the physical system, by simply iterating the computation of concepts over all
mechanisms M ∈P(S), where P(S) is the power set of subsystem nodes.
Integrated conceptual information Φ (Big Phi), a measure of the system’s strong/integration irreducibility, is assessed
by partitioning the set of elements into subsets with unidirectional cuts. Unidirectional bipartitions P→= {S(1); S(2)}
of the physical system S are performed by partitioning the subsystem into two parts S(1) and S(2) and cutting the edges
going from one part S(1) to another S(2) (the connections are substituted by noise). We then calculate the CES of the
partitioned system C(SP→) and compare it to C(S) to evaluate the difference made by the partition. MIP, a search
over all possible directed partitions is then performed to identify the one that makes the least difference to the CES.
Integrated information Φ (Big Phi) measures the irreducibility of a cause-effect structure, by quantifying the difference
the MIP makes to the concepts and their φ values of the system.
Φ = min
P→D
 C(S), C(SP→)

(17)
The difference D between two cause-effect structures is evaluated by an extended version of the Earth Mover’s Distance:
the cost of transforming one cause-effect structure C(S) into another C(SP→) in concept space.
32

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1812_00718v1_finding_continuity_and_discontinuity_in_fish_schools_via_integrated_information
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1812_00718V1_FINDING_CONTINUITY_AND_DISCONTINUITY_IN_FISH_SCHOOLS_VIA_INTEGRATED_INFORMATION.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

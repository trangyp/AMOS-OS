---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1502.06430v4
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1502.06430v4_Consensus_Emerging_from_the_Bottom-up__the_Role_of_Cognitive_Variables_in_Opinio

> Source: 1502.06430v4_Consensus_Emerging_from_the_Bottom-up__the_Role_of_Cognitive_Variables_in_Opinio.pdf

> Pages: 20

---


## Page 1


arXiv:1502.06430v4  [physics.soc-ph]  2 Sep 2015
Consensus Emerging from the Bottom-up: the Role
of Cognitive Variables in Opinion Dynamics
Francesca Giardini1, Daniele Vilone1,∗, Rosaria Conte1
1 Laboratory of Agent Based Social Simulation, Institute of Cognitive Science and
Technology, National Research Council (CNR), Via Palestro 32, 00185 Rome, Italy.
∗Correspondence and requests for materials should be addressed to D.V. (email:
daniele.vilone@gmail.com).
Abstract.
The study of opinions −e.g., their formation and change, and their
eﬀects on our society −by means of theoretical and numerical models has been
one of the main goals of sociophysics until now, but it is one of the deﬁning topics
addressed by social psychology and complexity science.
Despite the ﬂourishing of
diﬀerent models and theories, several key questions still remain unanswered.
The
aim of this paper is to provide a cognitively grounded computational model of
opinions in which they are described as mental representations and deﬁned in terms
of distinctive mental features.
We also deﬁne how these representations change
dynamically through diﬀerent processes, describing the interplay between mental and
social dynamics of opinions. We present two versions of the model, one with discrete
opinions (voter model-like), and one with continuous ones (Deﬀuant-like). By means
of numerical simulations, we compare the behaviour of our cognitive model with the
classical sociophysical models, and we identify interesting diﬀerences in the dynamics
of consensus for each of the models considered.
KEYWORDS: Opinion dynamics, cognitive modeling, social inﬂuence, agent-based
modeling, sociophysics.


## Page 2


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics2
1. Introduction
Opinions represent a large part of human mental representations, and a large part of our
everyday social interactions consist in exchanging, evaluating, revising and comparing
opinions with our family, friends, acquaintances, or even strangers.
Understanding
opinions, describing how they are generated and revised, and how far opinions travel
across social space both as a consequence of social inﬂuence and as one of the main means
through which social inﬂuence unfolds, is crucial for grasping a deeper understanding
of human social cognition and behaviours.
Since the beginning of the last century, sociologists and psychologists have been
interested in understanding opinions, focusing in particular on the multiplicity of
dimensions that characterise this phenomenon [1, 2]. Other disciplines have also been
interested in the topic, like sociophysics and complexity science [3,4]. In the last decades,
the study of social phenomena as opinion formation and dynamics has become of great
interest in physics.
Due to similarities between spreading and ordering phenomena,
opinion dynamics has been studied from a mathematical and numerical point of view
by means of the tools of statistical and computational physics [5, 6]. In particular, in
the physics community, opinions have been so far considered dynamic elements that
can be approximated as spin systems or by similar statistical-mechanical methods [7].
Moreover, the possibilities oﬀered by Big Data Science to collect and analyze huge
amounts of digital traces humans leave on the web and other media, has made opinion
change and consensus achievement exceeds disciplinary boundaries and become one of
our century’s grand scientiﬁc challenges [8].
Nonetheless, a theory explaining micro-foundations of opinion dynamics is still
missing.
In cognitive terms, opinions are highly dynamical mental representations
resulting from the interplay between diﬀerent mental objects within individuals’ minds.
Another distinguishing feature is their being easily aﬀected by opinions of other
individuals in the same network, as we will show in our model. Without explaining how
opinions are formed and manipulated within the individuals’ minds, it is very diﬃcult
to account for the way in which they change as an eﬀect of social inﬂuence.
Even
more diﬃcult is to predict consensus or to identify mechanisms leading to polarization
or to isolation and/or integration of minorities. This means that when explaining the
emergence of macro-social phenomena we need to know what happens at the micro-level,
i.e., what drives human actions and decisions in order to understand how individuals’
representations and behaviours can give rise to socially complex phenomena and how
those aﬀect agents’ actions. Deﬁning an opinion in terms of its mental ingredients and
specifying how human cognition promotes opinion change or resistance provides not only
a more realistic description of the phenomenon of interest, but it represents an attempt
to model the bottom-up emergence of opinions’ persistence, the eﬀects of contrasting
forces on them and the generation of alternative paths of diﬀusion.


## Page 3


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics3
We aim at developing a cognitively grounded model of opinion dynamics that will
allow us to answer the following questions: can we identify the distinctive features of
opinions, and model them as interacting representations that get inﬂuenced by others’
mental states? How can heterogeneous agents, endowed with diﬀerent representations of
the external world, come to share a given viewpoint and what consequences this sharing
has on individuals’ beliefs and their related behaviours?
Aim of this paper is to put forward a new model of opinion dynamics in which
opinions are deﬁned by three main features that interact and support opinion revision
and change.
We test our model through simulation experiments with two diﬀerent
network topologies and we try to identify how changes at the micro-level of agents’
cognition can give rise to changes in opinions at the collective level. In order to check
for our models’ robustness and reliability, we will also compare our results with existing
models, in particular the Voter [9] model and the work of Deﬀuant [10].
1.1. Opinions in the Social Sciences
The study of opinions’ formation and spreading originated within the ﬁeld of social
science, in which several important contributions were developed.
A comprehensive
review of the social and psychological literature on the topic is beyond the scope of
this work, but in this section we will tackle the background and we will review some of
the main theories that social scientists put forward about opinions and opinion change
with the aim of situating our inter-disciplinary model in the wider context of the social
sciences.
In general, opinions are treated as synonyms for diﬀerent mental objects, as beliefs
[11], or more frequently, attitudes [2, 12, 13].
In general, opinions and attitudes are
used as interchangeable terms referring to a mental object liable to social inﬂuence
and persuasion [14].
The speciﬁcity of attitudes and the fact that they cannot be
considered opinions is made clear in Allport’s work [15].
In this account, attitudes
deﬁne and shape people’s perceptions, whereas opinions result from a more articulated
process in which beliefs, goals, intentions and knowledge play a role. An attitude can be
regarded as a necessary element in opinion formation, but it is not suﬃcient. Allport [16]
recognizes the diﬀerence between attitudes and opinions, but he nonetheless considers
the measurement of opinions as one way of identifying the strength and values of personal
attitudes. An alternative view contrastss the aﬀective content of attitudes with the more
cognitive quality of opinions that involve some kinds of conscious judgments [17]. In
general, it is possible to identify two main trends in the relevant literature.
On one hand, researchers focus on attitudes, considered as implicit evaluations that
allow to access individuals’ positive or negative views about given matters, and that are
supposed to be stable across time and relevant enough to predict individuals’ behaviors
and actions.
On the other hand, explicit theories of opinions are more centered on
conscious reasoning and judgment, through which individuals are supposed to form and
express measurable opinions.


## Page 4


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics4
Another general feature of the social and psychological approach is the preminence
given to measuring, rather than conceptualizing opinions. As a result, many studies
(for a review, see [18]) tried to develop reliable and ﬁne-tuned ways to measure people’s
approaches to general questions, partially abandoning the issue of deﬁning what an
opinion is, and focusing on how it should be measured.
Quantifying opinions and
measuring their diﬀusion in a given population is important in order to understand,
monitor and predict social and political events, but it is not yet an answer to the
question: What is an opinion?
Answering this question is essential to deﬁne good
measures, to identify the right tools and also to get insights from the results. If the
measurement does not take into account the main features of opinions, then we will
never know what we are exactly measuring and how good our predictions can be, based
on that measure.
In political science, Crespi [19] considers individual opinions as ”judgmental
outcomes
of
an
individual’s
transactions
with
the
surrounding
world”
(p.19),
emphasizing the interplay between what he calls an attitudinal system and the external
world characterized by the presence of other agents and diﬀerent subjective perceptions.
Opinions are the outcomes of a judging process but this does not mean that they
are necessarily rational or reasoned, although Crespi recognizes that they need to be
consistent with the individual’s beliefs, values and aﬀective states. It is worth noticing
that many contributions are speciﬁcally oriented to understand ”public opinion” [20],
as the collective result of integration of opinions and attitudes coming from diﬀerent
sources and exposed to diﬀerent kinds of inﬂuencing.
As other authors already pointed out [21], many models of opinion and social
inﬂuence do not provide careful deﬁnitions of what an opinion is and how it is aﬀected
by social inﬂuence. This happens to be true also for theories of persuasion, like the social
impact theory [22], a theory of how social processes operate at the level of the individual
at a given point in time. Part of this theory has been developed using computational
modeling by Nowak, Szamrej and Latan´e [23]. In their model, individuals change their
attitudes as a consequence of other individuals’ inﬂuence. In parallel with the idea that
social inﬂuence is proportional to a multiplicative function of the strength, immediacy,
and number of sources in a social force ﬁeld [20, 22] suggest that each attitude within
a cognitive structure is jointly determined by the strength, immediacy, and number
of linked attitudes as individuals seek harmony, balance, or consistency among them.
Therefore, a single opinion does not exist in a ”vacuum” and its change depends on the
interplay of several factors. Their results show that group dynamics are dependent upon
initial spatial conﬁgurations, as well as from the diﬀerent parameters, hence opinion
change is completely dependent upon interactions happening at the group level.
1.2. Tackling the sociophysical background
The ﬁrst sociophysical approach to opinion dynamics was the voter model (VM). It was
originally conceived [9] as a model of competition of species, but it was soon adapted


## Page 5


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics5
to model an electoral competition between two candidates [24]. The VM dynamics is
extremely simple: each agent is endowed with a binary variable which can assume one
of two distinct values. In each elementary interaction an agent is randomly selected
and assumes the opinion of one of its neghbours (again randomly selected).
Initial
conditions are also generally set at random. This model has been thoroughly considered
in sociophysics because it can be solved exactly in every dimension [6] and thanks to its
simplicity and ﬂexibility has been used as a starting point in the quantitative treatment
of social phenomena.
In general, the VM dynamics can freeze only with consensus, that is, when all the
agents come to share the same opinion. In fact, only in one and two regular dimensions
the system is actually driven towards consensus, following a power-law decay in 1D
and a logarithmic one in 2D. In higher dimensions and on many complex networks the
system is not able to reach consensus and remains in a disordered metastable state in
the thermodynamical limit [25] (ﬁnite size systems eventually reach consensus thanks
to statistical ﬂuctuations, after a freezing time which diverges rapidly with size).
Interestingly, on small-world networks, the level of cooperation of the metastable
state is proportional to the density of long-range connections among distant parts of the
system [26,27].
However, its simplicity is also one of the main limitations of the model. Attempts
to overcome its limits included the application of the original VM in more realistic
conﬁgurations, meaning that the VM was tested in diﬀerent kinds of complex
topologies [26, 28, 29]. Another interesting direction consisted in adding agents with
special features with the aim of explaining fundamentalisms [30] or the eﬀects of mass
media [31].
The presence of fundamentalists or “zealots” who never change opinion, in general
does not enhance consensus: actually, a zealot forces the whole system towards its
opinion in one and two regular dimensions, where consensus is anyway achieved. On
the contrary, in diﬀerent topologies we observe the presence of a small region of localized
consensus only in the neighborhood of the fundamentalist [30,32,33].
In the VM interactions are based on imitation, a drastic simpliﬁcation of human
interactions. In order to make interaction more realistic, [34] proposed a majority rule
(MR): at each elementary time step a group of individuals is picked up at random, then
all the members adopt the opinion of the majority of the group itself. This rule was
proposed to describe public debates and interactions among individuals belonging to
diﬀerent groups. Also with the majority rule, the system can end up to consensus or to
a metastable disordered state, depending on the details of the topology and the initial
conditions.
In socio-physics, a great deal of work focused on the operational deﬁnition of opinion
itself. For example, it can be allowed to assume more than two values [35] or deﬁned as
a continuous variable [6,10]. These models present a richer dynamics and the number
of possible active and frozen states accessible to the system is much larger, so that the
phenomena observed are in principle more realistic. Among these models, the Deﬀuant


## Page 6


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics6
Model (DM) [10] deserves attention.
Here, an opinion is deﬁned as a real number
ranging from 0 to 1: therefore, it can be somehow considered a generalization of the
VM. A fundamental feature of DM is the threshold in opinion distance for which only
agents whose opinions are less distant than a given threshold can interact and then
get even closer opinions. This mechanism resembles the Axelrod’s model of cultural
spreading [36], where agents are able to interact proportionally to their actual cultural
similarity. This leads to a ﬁnal state with a set of diﬀerent clusters, each one consisting
of agents sharing the same opinion. The number of ﬁnal clusters depends on the initial
conditions and on the model’s parameters, especially the distance threshold [10, 37].
Subsequently, the DM has been furtherly reﬁned, for example by deﬁning another
variable characterizing the “aﬃnity” among agents [38], so that opinions and aﬃnities
coevolve: if there is a suﬃcient aﬃnity between agents, their opinions become more
similar, and viceversa. In this version of the model, consensus is reached more easily
than in the original DM.
Although diﬀerent in several respects, the models mentioned above share the same
feature: opinions are given from the beginning and evolve exclusively in interaction with
other agents and on the basis of the environment, without any internal characterization.
No hint of what happens within individuals’ minds, how opinions may emerge and evolve
internally, is given: in practice, in sociophysics models we have interacting opinions
rather than interacting individuals.
Aim of this work is to overcome the limitations of the social sciences, in which no
operational models of opinions are provided, and the limitations of socio-physics just
discussed. Moving from a deﬁnition of opinions as cognitive representations, we will
use socio-physics tools in order to put forward an inter-disciplinary model of opinions
which takes into account the internal dynamics of individuals’ minds and can be used
to analyze opinion spreading and consensus formation.
1.3. A tripartite model of opinion: truth-value, conﬁdence and sharedness
In this work we want to propose an integrated account in which we identify not only
the speciﬁc cognitive features that characterise opinions, but also the way in which each
single feature gets modiﬁed by interacting with others’ opinions. A cognitive model
of opinions and their dynamics requires to provide a deﬁnition of opinions as mental
representations and to present speciﬁc features that make their revision and update
easy and enduring. Moreover, grounding opinions in the mind allows us to take into
account not only direct processes of revision due to the interactions with others (social
inﬂuence), but also revisions based upon changes in one’s own mental representations
supporting that opinion.
On the basis of the previous considerations, opinions are mental representations
characterised by the following features:
• subjective truth-value
• conﬁdence


## Page 7


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics7
• perceived sharedness.
We assume that objective truth value cannot be veriﬁed (or it is not relevant), so
we refer to a ”subjective truth-value” that expresses whether and how much someone
believes an opinion to be true. Opinions are epistemic representations that refer to
matters or events that cannot be deﬁned as either true or false because it is not possible
to verify alternative states of the world [39], as for example the consequences of an
event that did not happen, or the outcomes of an election which has not been held
yet. In many cases opinions are emotionally loaded, and individuals have positive or
negative attitudes that reinforce their opinions, as for instance about abortion [19]. In
that case there may be not any ascertainable truth about it, but people often have
strong opinions on the basis of their beliefs, culture or personal experience. In order to
convert a subjective truth-value into a practical quantity, we will express it as a variable
indicating how true an opinion is considered by a given agent.
The second deﬁning feature of our model is the degree of conﬁdence. This is a
subjective measure of the strength of an opinion and it expresses the exent to which
one’s opinion is resistant to change, like a sort of “opinion inertia”. When an individual
is highly conﬁdent, he has a number of reasons to believe that his/her opinion is right,
and the higher the conﬁdence, the more willing that individual is to defend his/her
opinion against others’. For the sake of simplicity, conﬁdence is currently expressed as
an arbitrarily assigned value. It is worth stressing the diﬀerence between subjective
truth-value and degree of conﬁdence: an individual can be somehow uncertain about
his/her opinion, but struggle ﬁercely for it (“right or wrong, it’s my country”); or,
viceversa, he can be absolutely certain about a given issue without defending it publicly
(for fear or lack of interest).
The third feature of our model is perceived sharedness, i.e., the extent to which a
given opinion is perceived to be shared. This subjective measure allows us to distinguish
between the actual number of individuals having the same opinion and the personal
experience that an agent can have. Believing that there are a number of other individuals
sharing my opinion does not mean that this is actually the case, actually I can be part
of a minority and not be aware of the opinion of the majority. Perceived sharedness
may heavily aﬀect degree of conﬁdence, making people feel more conﬁdent because they
might feel supported by the majority. On the other hand, this factor can also lead an
individual to revise his/her opinion because conﬁdence in it is low and it is also perceived
as a minority opinion.
Modeling opinions as results of the interplay among the above deﬁned internal
variables allows us to take into account their distinctive nature of mental objects.
Knowing how opinions change within individuals’ minds is essential to understand
whether this change can be robust, how far it can travel into a given social group and how
far it can spread. Unlike other models that treat opinion change as an eﬀect of plain
social inﬂuence [23], we are interested in modeling what happens inside individuals’
minds.
Opinions do not change suddenly, but they result from interacting internal
dynamics and external inﬂuences, as our model is aimed to show.


## Page 8


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics8
2. Discrete Opinion Model
2.1. Description
We set N individuals which are characterised, at every time step t, by their opinions
Oi(t) (i = 1, . . . , N). In the discrete version of the model, opinions can assume one of
two possible values, 0 or 1. Agents are characterised by three internal variables referring
to their opinions: subjective truth-value xi
1(t), degree of conﬁdence xi
2(t), and perceived
sharedness xi
3(t). These variables are deﬁned as continuous quantities, ranging from 0
to 1.
Agents are located on the nodes of a graph, with the relationships among them
given by the links. At the beginning of the simulation, agents are initialized as having
one of two opinions which are randomly assigned with equal probability (with some
exceptions which will be pointed out when needed). Internal variables are assigned at
random as well, following a uniform distribution. For each elementary time step, two
agents are randomly chosen and they are attributed one of two roles: a listener, say i,
and a speaker, j. Speakers are selected among listener’s neighbours. In each interaction,
evolution applies only to listeners, which, in our asymmetric model, are those who can
revise their opinions. It is worth noticing that in our model, even though two agents
share the same opinion, this can result from completely diﬀerent internal variables. In
particular, opinions and internal variables coevolve. People sharing the same opinion
reinforce their beliefs when they meet, conversely interacting with an agent of opposite
opinion may drive individuals to change it or at least to be less sure of their initial
opinion.
In our model, the subjective truth-value and the degree of conﬁdence of a listener
increase (or remain unchanged) when interacting with a speaker sharing the same
opinion. In formal terms, we implement the dynamics of these internal variables when
Oi(t) = Oj(t) as follows
(i) If xi
1(t) < xj
1(t) and xi
2(t) < xj
2(t) =⇒xi
1(t + ∆t) = xj
1(t);
(ii) If xi
1(t) ≥xj
1(t) =⇒xi
1(t + ∆t) = xi
1(t);
(iii) If xi
2(t) ≥xj
2(t) =⇒xi
2(t + ∆t) = xi
2(t);
(iv) If xi
2(t) < xj
2(t) =⇒xi
2(t + ∆t) = xi
2(t)+2xj
2(t)
3
.
In practice, when a listener is paired with a speaker sharing the same opinion, its
subjective truth-value cannot decrease. In particular, we assume that if the speaker
is more conﬁdent than the listener, the latter is reinforced in his/her opinion; vice
versa, a speaker with a low degree of conﬁdence can marginally inﬂuence a listener.
We implemented this rule in the simplest way: the listener will assume the speaker’s
subjective truth-value (xj
1) if and only if both conﬁdence and subjective truth-value are
larger in the speaker, otherwise xi
1 does not change. Rules 3 and 4 deﬁne how conﬁdence


## Page 9


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics9
changes as an eﬀect of interactions. If a listener meets a more conﬁdent speaker with the
same opinion, this will increase the listener’s conﬁdence, otherwise it will not be aﬀected.
Unlike subjective truth-value, the listener does not assume the speaker’s conﬁdence, but
there is an adjustment between the two values.
Let us now deﬁne the rules for the dynamics of the opinion and the internal
variables when a speaker j and a listener i of diﬀerent opinions meet. In this case,
opinion change depends on conﬁdence and perceived sharedness. In general, we assume
that people can be better persuaded by more conﬁdent speakers, in line with evidence
in social psychology showing that consistent and conﬁdent minorities can inﬂuence
majorities and make them revise their judgements [40]. We also consider that there is a
positive correlation between the speaker’s subjective truth value and the probability of
convincing the listener. Finally, humans are sensitive to social pressure, then believing
that one’s own opinion is shared by the majority makes opinion change less likely [41].
Therefore, we deﬁne a simpliﬁed rule such that the probability Pij that i assumes the
j’s opinion is zero if speaker’s conﬁdence is smaller than the listener’s, otherwise it is
directly proportional to the speaker’s subjective truth-value and to the quantity 1 minus
the perceived sharedness. This points to the fact that an agent is reluctant to change
its opinion if thinking to share it with the majority. Summarizing, it is
Pij =





xj
1(t)[1 −xi
3(t)]
if
xj
2 > xi
2
0
if
xj
2 ≤xi
2 ;
(1)
Afterwards, if the listener shifts towards the speaker’s opinion, we assume that the
former also acquires the subjective truth-value of the latter, but with a conﬁdence level
equaling half of the speaker’s conﬁdence.
xi
1(t + ∆t) = xj
1(t)
xi
2(t + ∆t) = xj
2(t)/2 .
(2)
On the contrary, if i does not change opinion, the listener’s subjective truth-
value remains unchanged, but the interaction aﬀects in any case the conﬁdence. More
precisely, we assume that interacting with someone with a diﬀerent opinion reduces the
listener’s degree of conﬁdence. Therefore, we set the new listener’s conﬁdence as the
average between its own conﬁdence before the interaction and the speaker’s conﬁdence
level in case the latter was smaller, to half its original value if initially it was xi
2 < xj
2.
xi
1(t + ∆t) = xi
1(t)
(3)
xi
2(t + ∆t) =





xi
2(t)+xj
2(t)
2
if
xi
2(t) > xj
2(t)
xi
2(t)
2
if
xi
2(t) ≤xj
2(t) .
(4)
Finally, we implemented perceived sharedness xi
3(t) as the total number of past
encounters with other agents sharing the same opinion an agent i has up to time t,


## Page 10


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics10
independently of the outcomes of each interaction. More precisely, each agent records all
past encounters as a listener, determining the frequency of both opinions: the perceived
sharedness at time t is the frequency of the opinion shared by the agent itself at the
same instant t.
Time is measured in Monte Carlo steps. This means that a single time unit is made
up by N single interactions, i.e. ∆t ≡1/N.
Certainly, this model must be seen as a ﬁrst step, and further studies and in-depth
analyses will be useful for a more precise deﬁnition of its parameters.
2.2. Topology
We tested the behaviour of our model on two diﬀerent topologies: a total connected
graph (mean ﬁeld) and a one-dimensional ring.
We chose them in accordance with
the relevant literature [6], in which these topologies are usually considered as starting
points.
Moreover, given the complexity of the relationships among agents’ internal
variables, even simple topologies can be useful in understanding the basical properties
of the model. More complex topologies will be used in future works.
2.3. Results
For each version of the model, we initially considered a system of N = 100 agents and
tested its behaviour starting from three diﬀerent initial distributions of agents holding
two diﬀerent opinions: ⟨O0⟩= 0.5, 0.75 and 0.9. The last two distributions represent an
attempt to model a situation in which there is a conﬂict between a majoritarian and a
minoritarian opinion. We stress the fact that every measure represents an average over
2000 independent realizations. More details are given in the following subsections.
2.3.1. Mean ﬁeld
In every simulation the system ends up to a substantial consensus.
At the end of each realization, all the agents share the same opinion, even if there are
interesting diﬀerences between individuals’ mental states.
In Figure 1 we show how average opinion behaves over time. It is worth noticing
that an initial asymmetry, even if small, allows the majoritarian opinion to invade the
whole system and to become dominant. That means that the opinion which at t = 0
is majoritarian, even slightly, always ends up being the only survived one. This result
contrasts with the classical mean ﬁeld voter model, in which the initial average opinion
is always conserved [6,7].
On the other hand, in Figure 2 we show the behaviour over time of the averaged
internal variables with ⟨O0⟩= 0.5.
Among these, perceived sharedness shows a
noticeable behaviour: it takes longer to reach its ﬁnal level (which equals 1 since all the
agents share the same opinion eventually). In other words, the system reaches consensus
even before agents realize they all agree, showing an interesting dynamics between the
micro- and the macro-level. This result is remarkable especially if we think of real-world
situations, in which there is usually a gap between what individuals know locally and the


## Page 11


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics11
1
10
100
t
0,5
0,75
1
<O>
<O0>=0.5
<O0>=0.75
<O0>=0.9
Figure 1. Average opinion as a function of time for a system of N = 100 on a totally
connected graph for three diﬀerent initial conditions. Figure presents values averaged
over 2000 independent realizations.
1
10
100
1000
10000
t
0,4
0,5
0,6
0,7
0,8
0,9
1
<x1>
<x2>
<x3>
Figure 2. Time behaviour of average internal variables for a system of N = 100 on
a totally connected graph and initial average opinion ⟨O0⟩= 0.5. Averages over 2000
independent realizations.
global and emergent behaviour of the system in which they are embedded. This delay
is due to the early encounters at the initial stages of the dynamics, kept in memory
by the agents, which drive the individuals to mantain a distorted idea of the others’


## Page 12


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics12
views for a longer time. It is worth to notice that the persistence of the initial opinion
and impressions in human mind is a well-known phenomenon, already discussed in the
psychological literature [42,43].
In order to be sure that the observed results do not depend on the size of the
system, we also repeated the same simulations with N = 250: we did not observe any
signiﬁcant diﬀerences increasing the number of agents in the population.
It must be noticed that even if this dynamics leads the system to consensus, in
half of the realizations there is one agent who maintains its minoritarian opinion. This
resistance to social inﬂuence happens when the agent with the largest initial degree of
conﬁdence has the opposite opinion of the majority: from Equation (1) follows that
such agent can never change opinion. Such a result could help explaining extremisms
in real-world scenarios, where no matter the kind of social inﬂuence and persuasion
someone is exposed to, there are always individuals who stick to their opinions.
2.3.2. One-dimensional ring
We tested our model also on a one-dimensional ring with
the same number of agents (N = 100).
1
10
100
1000
10000
t
0,5
0,6
0,7
0,8
0,9
1
<O>
<O0>=0.5
<O0>=0.75
<O0>=0.9
Figure 3. Average opinion as a function of time for a system of N = 100 on a one-
dimensional ring for three diﬀerent initial conditions. Averages over 2000 independent
realizations.
Figures 3 and 4 show how average opinion (for three diﬀerent initial conditions)
and internal variables (for ⟨O0⟩= 0.5) change over time, respectively. Concerning the
average opinion, qualitatively these results are similar to the mean ﬁeld case, even though
here the invasion of the initially majoritarian opinion is much slower. This behaviour is
conﬁrmed in Figure 5, where we compare the time behaviour of active bonds (i.e. the
links between two agents with opposite opinion) in our model and in the one-dimensional


## Page 13


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics13
1
10
100
1000
10000
t
0,5
0,6
0,7
0,8
0,9
1
<x1>
<x2>
<x3>
Figure 4. Behaviour over time of average internal variables for a system of N = 100
on a one-dimensional ring and initial average opinion ⟨O0⟩= 0.5. Averages over 2000
independent realizations.
voter model [6,27], in which, at each time step, a randomly selected agent simply imitates
the opinion of one of its neighbours. This makes the system reach consensus through
a power-law decay with exponent 1/2 (and a ﬁnal quick exponential convergence time
depending on the square of the system size), whereas a diﬀerent behaviour is observed in
our model. After an initial power-law decay with exponent β close to 2/3 (a numerical
ﬁt reports β = 0.65±0.01), the active bond density decreases much more slowly (maybe
tending to a steady state), as shown in the inset of the same ﬁgure.
3. Continuous Opinion Model
3.1. Description
We also present another version of the model in which opinions are continuous, so that
an opinion is a real variable ranging between 0 and 1 (initially randomly assigned to each
agent following a uniform probability distribution). The model dynamics is the same we
described above, but we extended its scope by adding a new rule for opinion revision.
Here, when the listener accepts the speaker’s opinion, opinion changes in accordance
with Deﬀuant’s rule [10,37]:
Oi(t + 1) = Oi(t) + µ[Oj(t) −Oi(t)] ;
(5)
with µ = 0.5. In order to determine the perceived sharedness, we consider opinions
up to 0.5 as of “negative” kind and from 0.5 as “positive”, so that xi
3(t) is the number


## Page 14


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics14
1
10
100
1000
t
0,001
0,01
0,1
1
na(t)
CM, N=100
VM, N=100
CM, N=1000
VM, N=1000
1
100
10000
t
0,001
0,01
0,1
1
na(t)
CM, N = 1000
(<O0>=0.75)
Figure 5. Behaviour over time of the (average) active bond density for the cognitive
opinion model (CM) on a one-dimensional ring and initial average opinion ⟨O0⟩= 0.75.
System size: N = 100 (full black line) and N = 1000 (full red line). Comparison with
the voter model with the same parameters (dashed lines: black for N = 100, red for
N = 1000). The blue dashed line represents a power decay with exponent 1/2, the blue
straight one a power decay with exponent 2/3. Inset: time behaviour of the active
bond density for CM with N = 100 up to t = 105. Averages over 2000 realizations.
of past encounters with other agents sharing the same kind of opinion an agent i has up
to time t, starting from t = 0. The internal variables are assigned at random, following
a uniform distribution, also in this version of the model.
3.2. Results
Mean ﬁeld
In the continuous version of the model, when the graph is totally connected,
the system reaches ﬁnal consensus, even though conserving the average initial opinion,
as we can see in Figure 6.
On the other hand, internal variables behave as in the
discrete case, as shown in Figure 7.
This means that when we apply a mean ﬁeld
topology, the model shows the same behaviour, regardless of the way in which opinions
are implemented (either as discrete or as continuous variable): the system achieves ﬁnal
consensus with high levels of subjective truth-value and degree of conﬁdence, reached
even before the agents realize they have already ended up sharing the same opinion.


## Page 15


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics15
0
10
20
30
t
0
0,2
0,4
0,6
0,8
1
<O>
<O0>=0.5
<O0>=0.6
<O0>=0.75
<O0>=0.45
0
10
20
30
t
0
0,2
0,4
0,6
0,8
1
O
A
B
D
C
0
10
20
30
t
0
0,2
0,4
0,6
0,8
1
O
0
0
0,2
0,4
0,6
0,8
1
0
10
20
30
t
0
0,2
0,4
0,6
0,8
1
O
0
10
20
30
0
Figure 6. Behaviour of the opinion for a system of N = 100 individuals on a totally
connected graph; continuous opinion. Averages over 2000 independent realizations. A:
Time evolution of the average opinion for four diﬀerent initial conditions (from top
to bottom of the ﬁgure: ⟨O0⟩= 0.75, 0.6, 0.5, 0.45, respectively), average over 2000
independent realizations. B, C, D: Evolution of the opinion of each agent during a
single realization, for initial average opinion ⟨O0⟩= 0.3, 0.5 and 0.7, respectively.
4. Discussion
Opinions are a complex issue for a variety of reasons and they represent a very interesting
case of the micro-macro link: opinions are mental objects that get modiﬁed by social
processes and then re-enter the mental space. More speciﬁcally, internal representations
of individuals, such as beliefs, goals, and intentions, give rise to the complex dynamics at
the macro-level, which feed backs into the lower level. However, pivotal to understanding
the dynamics of opinions is the deﬁnition of speciﬁc features, which characterise how
opinions are created and modiﬁed within individual minds.
In this work, we have outlined the micro-level of opinions and started to explore
their dynamics.
We identiﬁed three main constitutive features of opinions within
individuals’ minds.
The ﬁrst internal variable is the subjective truth-value, which
describes how much the individual believes her/his opinion to be true.
Saying that
opinions have a subjective truth-value does not mean that individuals do not believe
in them or that they cannot be strongly opinionated. This feature is crucial because it
accounts for the fact that opinions get more frequently inﬂuenced by interactions with
others through social inﬂuence, but they can also be easily revised according to changes
in one’s own mental representations, without any external inﬂuence. The second feature
is what we called degree of conﬁdence, which deﬁnes to what extent an individual trusts
his/her opinion and how much the opinion is resistant to change. The last variable we


## Page 16


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics16
1
10
100
1000
t
0,5
0,6
0,7
0,8
0,9
1
<x1>
<x2>
<x3>
Figure 7. Time behaviour of the average internal variables for a system of N = 100
on a totally connected graph and initial average opinion ⟨O0⟩= 0.5; continuous opinion.
Averages over 2000 independent realizations.
introduced is perceived sharedness, i.e., the extent to which one believes others share the
same opinion, thus providing support for it. Perceived sharedness does not necessarily
overlap with the actual sharedness, and there can be a gap between how much someone
believes an opinion to be shared and the actual number of individuals sharing it.
Our results show that the interaction of these variables at the micro-level generates
interesting macro-dynamics. Compared with the voter model, we observe interesting
diﬀerences. The voter model dynamics has two main features: the magnetization is
conserved, but in a mean ﬁeld topology and one dimension, consensus is reached for
every ﬁnite system size [6,7]. This means that, even though in each realization all agents
end up sharing the same opinion (0 or 1), the average over the ensemble always conserves
the initial average opinion. In our discrete model, instead, as shown in Figure 1, this is
true only for totally random initial conﬁgurations (i.e., ⟨O0⟩= 0.5). On the contrary,
if simulations start with an even small asymmetry between the two opinions, the most
spread one outcompetes the other.
Another diﬀerence between the voter dynamics and our cognitive model consists
in the amount of time needed to reach the ﬁnal totally ordered state, which strongly
depends on the system topology. On a totally connected graph our model is faster than
VM. Actually, even though the convergence to the ﬁnal conﬁguration is in both cases
exponential, the distribution of consensus times τ, i.e. the time needed to reach the
consensus, is rather diﬀerent, as shown in Figure (8). Both distributions have indeed
the same mode and an exponential tail, but due to its longer tail, the average τ for the
voter model is almost two times larger. Moreover, the latter has a much larger standard


## Page 17


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics17
deviation (στ ≃44 for the voter model, and (στ ≃5 for the cognitive one), meaning
that also consensus times very far away from the average are likely to be observed.
0
50
100
150
200
τ
0
0,025
0,05
0,075
Pτ
Cognitive Model;  < τ > =19
Voter Model; < τ > = 33
Figure 8. Probability distribution of the time needed to reach consensus τ for the
cognitive opinion model (black) and the voter model (red). Mean-ﬁeld case, system size
N = 100, initial average opinion ⟨O0⟩= 0.5.
Conversely, in one dimension we observe that our cognitive model is slower than the
voter one. Actually, as it is easy to understand from Figure 5, the active bond density
starts decaying similarly to the voter model (even though with a diﬀerent power-law
exponent), but after a certain time t∗it reaches a sort of plateau whose level decreases
slightly on the system size. In short, for our model the time behaviour of active links
can be written as follows:
na(t) ∝





t−β
if
t ≲t∗
g(t)
if
t ≳t∗,
(6)
where g(t) is a decreasing function of time. From Figure 5, it is possible to infer
that the decay exponent is β ≃0.65. On the other hand, the behaviour of g(t) and the
value of t∗, which a priori could also depend on N, are very hard to be assessed precisely.
Their determination would require the numerical study of much larger systems up to very
large times, averaged over more than thousands of realizations, but such eﬀort would
go beyond the scope of this work. Anyway, while an exact form of the Equation (6)
may be obtained only through further investigations, the main trend (that is, a slow
convergence to the consensus with cognitive dynamics of opinions) is already clear.
In mean ﬁeld topology our model shows that ﬁnal consensus is achieved faster,
and this is true even when taking into consideration continuous opinions.
Actually,
comparing Figure 7 with the results for similar systems reported in [37], it can be


## Page 18


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics18
easily noticed that the latter needs much more time to reach the ﬁnal ordered state, if
compared with our results.
Our work represents a ﬁrst attempt to merge two related but usually distant
approaches. Cognitive modeling allowed us to deﬁne the basic elements of an opinion
as a mental representation characterised by speciﬁc features, whereas we used the tools
of socio-physics to model the dynamics of opinion spreading. Further investigation is
needed in order to better understand opinion change and to set more properly the
parameters at stake, but also to predict whether these changes will be stable and
under what conditions.
In particular, we need to investigate more exstensively the
interplay among diﬀerent dynamics. Opinions change in the mind possibly under social
inﬂuence, and the social cognitive dynamics of opinions aﬀects the way they spread and
the conﬁguration of the space of opinions.
On the other hand, the initial topology may bear consequences on opinion change
and on mental features that characterise existing opinions. Furthermore, the interplay
between opinions and other mental objects, like other types of beliefs, ought to be
addressed, and the external validation of the cognitive model against real-world data
should be also achieved. Finally, a well-determined comparison between cognitive and
classical socio-physical opinion models, here outlined, would be useful to understand
more correctly merits and limits of both approaches.
Disclosure/Conﬂict-of-Interest Statement
The authors declare that the research was conducted in the absence of any commercial
or ﬁnancial relationships that could be construed as a potential conﬂict of interest.
Author Contributions
Francesca Giardini and Rosaria Conte developed the model, Daniele Vilone performed
numerical simulations and analyzed data, and all the authors wrote the paper.
Acknowledgments
This material is based upon work supported by CLARA (CLoud plAtform and smart
underground imaging for natural Risk Assessment), funded by the Italian Ministry of
Education and Research (PON 2007-2013: Smart Cities and Communities and Social
Innovation; Asse e Obiettivo: Asse II - Azione Integrata per la Societ`a dell’Informazione;
Ambito: Sicurezza del territorio).
References
[1] H. C. Kelman. Processes of opinion change. Public Opinion Quarterly, 25 (1):57–78, 1961.
[2] J. M. Olson and M. P. Zanna.
Attitudes and attitude change.
Annual Review of Psychology,
44:117–154, 1993.


## Page 19


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics19
[3] R. Hegselmann and U. Krause. Opinion dynamics and bounded conﬁdence models, analysis, and
simulation. Journal of Artiﬁcal Societies and Social Simulation, 5(3), 2002.
[4] Dirk Helbing.
Quantitative sociodynamics: stochastic methods and models of social interaction
processes. Springer, 2010.
[5] S. Galam. Sociophysics: A review of galam models. International Journal of Modern Physics C,
19:409–440, Mar 2008.
[6] C. Castellano, S. Fortunato, and V. Loreto.
Statistical physics of social dynamics.
Review of
Modern Physics, 81:591–646, 2009.
[7] Parongama Sen and Bikas K. Chakrabarti. Sociophysics - An Introduction. Oxford, 2014.
[8] D. Lazer, A. Pentland, L. Adamic, S. Aral, A.-L. Barab´asi, D. Brewer, N. Christakis, N. Contractor,
J. Fowler, M. Gutmann, T. Jebara, G. King, M. Macy, D. Roy, and M. Van Alstyne. Life in the
network: the coming age of computational social science. Science, 323(5915):721–723, 2009.
[9] P. Cliﬀord and A. W. Sudbury.
[10] G. Deﬀuant, D. Neau, F. Amblard, and G. Weisbuch. Mixing beliefs among interacting agents. In
2nd international conference on computer simulations and the social sciences, Paris, september
2000, number 00/0399 ; K IAS 11, pages 87–98, 2000.
[11] M. Fishbein and I. Ajzen. Belief, Attitude, Intention, and Behavior: An Introduction to Theory
and Research. Reading, MA: Addison-Wesley, 1975.
[12] W. McGuire.
The vicissitudes of attitudes and similar representational constructs in twentieth
century psychology. European Journal of Social Psychology, 16:89–139, 1986.
[13] V. Price. Communication concepts 4: Public opinion. Sage, 1992.
[14] R.E. Petty, D.T. Wegener, and L.R. Fabrigar. Attitudes and attitude change. Annual Review of
Psychology, 48:609–647, 1997.
[15] G. W. Allport. A Handbook of Social Psychology, pages 798–844. Clark University Press, 1935.
[16] G. W. Allport. Readings in attitude theory and measurement, chapter Attitude, pages 1–13. Wiley,
1967.
[17] D. Fleming. Attitude: The history of a concept. Perspectives in American History, 1:287–365,
1967.
[18] N. Schwarz and S. Sudman. Answering Questions: Methodology for Determining Cognitive and
Communicative Procesess in Survey Research. San Francisco: Jossey- Bass, 1996.
[19] I. Crespi. The public opinion process. How the people speak. Lawrence Erlbaum Associates, 1997.
[20] H. Lavine and B. Latan´e. A cognitivesocial theory of public opinion dynamic social impact and
cognitive structure. Journal of Communication, 46:48–56, 1996.
[21] A. Mason, F.Conrey, and E. Smith. Situating social inﬂuence processes: Dynamic, multidirectional
ﬂows of inﬂuence within social networks. Personality and Social Psychology Review, 11(279-300),
2007.
[22] B. Latan´e. The psychology of social impact. American Psychologist, 36:343–356, 1981.
[23] A. Nowak, J. Szamrej, and B. Latan´e. From private attitude to public opinion: A dynamic theory
of social impact. Psychological Review, 97:362–376, 1990.
[24] R. Holley and T. Liggett. Ergodic theorems for weakly interacting inﬁnite systems and the voter
model. Annals of Probability, 3:643, 1975.
[25] V. Sood, T. Antal, and S. Redner. Voter models on heterogeneous networks. Physical Review E,
77:041121, 2008.
[26] C. Castellano, D. Vilone, and A. Vespignani. Incomplete ordering of the voter model on small-
world networks. Europhysics Letters, 63:153, 2003.
[27] D. Vilone and C. Castellano. Solution of voter model dynamics on annealed small-world networks.
Physical Review E, 59:016109, 2004.
[28] F. Slanina and H. Lavi cka. Analytical results for the sznajd model of opinion formation. European
Physical Journal B, 35:279, 2003.
[29] K. Suchecki, V. M. Egu´ıluz, and M. San Miguel. Conservation laws for the voter model in complex
networks. Europhysics Letters, 69:228, 2005.


## Page 20


Consensus Emerging from the Bottom-up: the Role of Cognitive Variables in Opinion Dynamics20
[30] M. Mobilia.
Does a single zealot aﬀect an inﬁnite group of voters?
Physical Review Letters,
91:028701, 2003.
[31] J. C. Gonz´alez-Avella, M. G. Cosenza, and K. Tucci. Nonequilibrium transition induced by mass
media in a model for social inﬂuence. Physical Review E, 72:065102, 2005.
[32] M. Mobilia and I. T. Georgiev. Voting and catalytic processes with inhomogeneities.
Physical
Review E, 71:046102, 2005.
[33] M. Mobilia, A. Petersen, and S. Redner. On the role of zealotry in the voter model. Journal of
Statistical Mechanics, P08029, 2007.
[34] S. Galam. Minority opinion spreading in random geometry. European Physical Journal B, 25:403,
2002.
[35] F. Wu. The potts model. Review of Modern Physics, 54:235, 1982.
[36] R. Axelrod. The dissemination of culture a model with local convergence and global polarization.
Journal of Conﬂict Resolution, 41:203, 1997.
[37] G. Weisbuch, Deﬀuant G, F. Amblard, and J. P. Nada. Interacting agents and continuous opinions
dynamics. arXiv:cond-mat/0111494 [cond-mat.dis-nn], 2001.
[38] F. Bagnoli, T. Carletti, D. Fanelli, A. Guarino, and A. Guazzini. Dynamical aﬃnity in opinion
dynamics modeling. Physical Review E, 76:066105, 2007.
[39] F. Giardini, W. Quattrociocchi, and R. Conte. Understanding opinions. a cognitive and formal
account. arXiv:1106.4221 [cs.AI], 2011.
[40] Serge Moscovici. Social inﬂuence and social change. London Academic Press, 1976.
[41] H. C. Kelman. Compliance, identiﬁcation and internalization: Three processes of attitude change.
Journal of Conﬂict Resolution,, 1:51–60, 1958.
[42] Martin F. Davies. Belief persistence after evidential discrediting: The impact of generated versus
provided explanations on the likelihood of discredited outcomes. Journal of Experimental Social
Psychology, 33:561, 1997.
[43] Timothy J. Wood. Is it time to move beyond errors in clinical reasoning and discuss accuracy?
Advances in Health Sciences Education, 19:409, 2014.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
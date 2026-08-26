---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1106.4221v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1106.4221v1_Understanding_opinions__A_cognitive_and_formal_account

> Source: 1106.4221v1_Understanding_opinions__A_cognitive_and_formal_account.pdf

> Pages: 15

---


## Page 1


arXiv:1106.4221v1  [cs.AI]  21 Jun 2011
September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
Advances in Complex Systems
c⃝World Scientiﬁc Publishing Company
Understanding opinions. A cognitive and formal account
Francesca Giardini
Department of Cognitive Science, Central European University,
Budapest, Hungary, email: GiardiniF@ceu.hu ∗
GiardiniF@ceu.hu
Walter Quattrociocchi
Department of Mathematics and Computer Sciences,
University Of Siena, Italy †
walter.quattriocchi@unisi.it
Rosaria Conte
LABSS,
CNR - Institute of Cognitive Sciences and Technologies, Rome, Italy ‡
rosaria.conte@istc.cnr.it
Received (received date)
Revised (revised date)
The study of opinions, their formation and change, is one of the deﬁning topics addressed
by social psychology, but in recent years other disciplines, as computer science and
complexity, have addressed this challenge. Despite the ﬂourishing of diﬀerent models
and theories in both ﬁelds, several key questions still remain unanswered. The aim of
this paper is to challenge the current theories on opinion by putting forward a cognitively
grounded model where opinions are described as speciﬁc mental representations whose
main properties are put forward. A comparison with reputation will be also presented.
Keywords: opinion dynamics; social inﬂuence; gossip; media; agenda-setting
1. Introduction
Opinions represent a conspicuous part of our mental representations. A large part
of our social time is spent in exchanging, evaluating, revising and comparing our
opinions. We also say, about many diﬀerent issues, that we have opinions and we try
to convince others about the groundedness of our own opinions. Since the beginning
of the last century, social psychologists have been interested in understanding the
speciﬁcity of opinions, as compared to other kinds of mental representations, by fo-
cusing their attention on the multiplicity of dimensions, including attitudes, beliefs
∗Central European University, Hungary email: GiardiniF@ceu.hu
†University of Siena, Italy email: walter.quattriocchi@unisi.it
‡Labss-ISTC-CNR, Italy email: rosaria.conte@istc.cnr.it
1


## Page 2


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
2
Francesca Giardini, Walter Quattrociocchi, Rosaria Conte
and evaluations, that take part within this phenomenon. Also political science has
always been very attentive to what is considered as a way to measure people’s pref-
erences and beliefs about publicly relevant issues. Many of these contributions have
been directed towards understanding the so-called public opinion and the processes
through which it is possible to inﬂuence it, manipulating people’s awareness and
tendencies ([18]). More recently, other disciplines have shown a great interest re-
garding such an issue, ranging from computer science passing through socio-physics
([7, 13]) up to complexity science ([19]).
Despite the large amount of studies on opinions, the term itself and the un-
derlying concept are poorly speciﬁed and too general, since there are at least two
classes of mental representations that can be termed opinions but they diﬀer with
regard to important aspects. Moreover, relevant contributions coming from social
psychology and computer science try to model distinct issues, thus making the
analysis of opinions quite diﬃcult. This lack of sound theoretical contributions is
often compensated by giving more preeminence to transmission and communication
processes, thus partially putting aside the ontological issue. In this work we pro-
pose a theoretical account in which, starting from a critical review of approaches
coming from social psychology and computer science, the necessity of a cognitive
approach is claimed. Deﬁning the speciﬁc cognitive features that characterize an
opinion, thus distinguishing it from other mental representations, and introducing
also two diﬀerent kinds of opinions, evaluative and factual, we will claim for the
necessity of investigating the mental roots of opinions, in order to understand how
they are transformed and manipulated within and between minds. This means that
an opinion is speciﬁc with regard to other mental representations, that has special
features and is transformed through speciﬁc mental processes. Deﬁning an opinion
in terms of its mental ingredients permits to predict opinion change, its persis-
tence, the eﬀects of contrasting forces and alternative paths of diﬀusion, because
the diﬀerent forces are endogenously determined by speciﬁc rules. Understanding
opinions, describing how they are generated and revised, and how fare opinions
travel over the social space both as a consequence of social inﬂuence and as one
of the main means through which social inﬂuence unfolds, is crucial for grasping a
deeper understanding of human social cognition and behaviors. Moreover, our cog-
nitive analysis is supported by a preliminary formal description, in which a new tool
called Time Varying Graphs [8] is presented. This formalism has been developed
to deal with dynamically evolving systems[24, 23], and it allows to overcome some
of the limitations imposed by other instruments -e.g. metrics, formalisms that are
not suited to account for a) the relationships between opinions and other epistemic
representations and b) their dynamics both at social and individual level. In sec-
tion 2, a critical introduction to some of the main contributions about opinions is
provided. Section 3 is devoted to the description of our model, in which a deﬁnition
of opinions as speciﬁc mental representations and cognitively founded hypotheses
about their diﬀusion and change will be put forward. In section 4 a preliminary
formal account of how opinions are generated and how they can change is provided.


## Page 3


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
Understanding opinions. A cognitive and formal account
3
In section 5 some conclusions are drawn and future directions are suggested.
2. A critique to existing approaches
The understanding of opinions requires to take into account two levels of expla-
nation: the individual and the social level. As mental representations, opinions are
created within agents’ minds and they need to be integrated with the existing net-
work of beliefs, data, information, memories and evaluations. However, in opinion
change the social inﬂuence plays a major role and the sharedness of an opinion
can heavily aﬀect its persistence and resistance to change. These two dimensions
are tightly linked and their interplay is one of the deﬁning features of opinions,
but social psychology and computer science are usually interested in tackling only
one of these two aspects, without studying them in combination. We claim that
developing a cognitive theory of opinions allows us to combine the micro- and the
macro-level, understanding how macro-social phenomena emerge, unintentionally,
from micro-elements and their interactions. In this way we can see that opinions
derive from agents’ cognitive representations and states but they also exist in the
social space, in which they are transmitted and shared, and this social process af-
fects, in turn, individuals’ opinions. This complex loop requires a non-reductionist
approach in order to deal with both levels, without giving preeminence to one or
the other.
Social psychology mainly focuses on the individual side, trying to describe how
opinions are generated within the mind, devoting much attention to deﬁne attitudes
and evaluations, but paying little attention to the socially interactive dimension of
opinions. On the other hand, scholars from computer science and physics have tried
to explain how diﬀerent opinions can coexist or how they are modiﬁed through
communication, treating opinions as mere objects that are exchanged and revised
according to certain mechanisms that are quite far from the reality of cognitive and
social processes. In both cases there is a reductionist fallacy that works in diﬀerent
ways but in both cases results in a downgrading of a complex issue into either a
set of unrelated speciﬁc elements or a unidimensional object that is far from the
complexity of a cognitive representation.
2.1. Social psychology: individualistic fallacy
Social psychologists have devoted much attention to the study of opinions’ formation
and spreading, but a comprehensive and deﬁnite model allowing for an operational
and generative account is still missing. Providing a comprehensive review of social
psychology literature is beyond the scope of this work, but in this section we will
discuss some of the main theories in order to underline how partial is the picture of
opinions emerging from these studies.
In general, opinions are treated as synonyms for diﬀerent mental objects, as
beliefs [21], or more frequently, attitudes. Opinions are often conceptualized as atti-
tudes [20], [16], [22] or they are used as interchangeable terms that have in common


## Page 4


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
4
Francesca Giardini, Walter Quattrociocchi, Rosaria Conte
the fact of being aﬀected by social inﬂuence and persuasion [26]. It is worth notic-
ing that many contributions are speciﬁcally oriented to understand ”public opinion”
[14], as the integration of opinions and attitudes coming from diﬀerent sources and
exposed to diﬀerent kinds of inﬂuencing. Another general feature of the social psy-
chology approach to opinions is the preeminence given to measuring opinions, rather
than on conceptualizing them. As a result, many studies (for a review, see Schwarz
N, Sudman S, eds. 1996. Answering Questions: Methodology for Determining Cog-
nitive and Communicative Procesess in Survey Research. San Francisco: Jossey-
Bass) tried to develop reliable and ﬁne-tuned ways to measure people’s approaches
to general questions, partially abandoning the issue of deﬁning what an opinion is
and focusing on how it should be measured.
Allport [3] recognizes the diﬀerence between attitudes and opinions but he
nonetheless considers the measurement of opinions as one way of identifying the
strength and value of personal attitudes. An alternative view contrasts the aﬀective
content of attitudes with the more cognitive quality of opinions that involve some
kind of conscious judgments [12]. In general, it is possible to identify two main trends
in the relevant literature: one more focused on attitudes and the other more centered
on conscious reasoning and judgment. Crespi [9] considers individual opinions as ”
judgmental outcomes of an individual’s transactions with the surrounding world”
(p.19), emphasizing the interplay between what he calls an attitudinal system and
the external world characterized by the presence of other agents and diﬀerent sub-
jective perceptions. Opinions are the outcomes of a judging process but this does
not mean that they are necessarily rational or reasoned, although Crespi recognizes
that they need to be consistent with the individual’s beliefs, values and aﬀective
states.
As other authors already pointed out [1], many models of opinion and social
inﬂuence do not provide careful deﬁnitions of what an opinion is and how it is af-
fected by social inﬂuence. This happens to be true also for theories of persuasion,
like the social impact theory [17], a static theory of how social processes operate
at the level of the individual at a given point in time. Part of this theory has
been developed using computational modeling by Nowak, Szamrej and Latan [2].
In their model, individuals change their attitudes as a consequence of other indi-
viduals’ inﬂuence. In parallel with the idea that social inﬂuence is proportional to
a multiplicative function of the strength, immediacy, and number of sources in a
social force ﬁeld [17], [14] suggest that each attitude within a cognitive structure
is jointly determined by the strength, immediacy, and number of linked attitudes
as individuals seek harmony, balance, or consistency among them. Although very
interesting, this account fails to distinguish between attitudes and beliefs and does
not explain how inconsistencies can be resolved. The eﬀect of communication on
opinion formation has been addressed by diﬀerent disciplines from within the social
and the computational sciences, as well as complex systems science (for a review on
attitude change models, see [1]). One of the ﬁrst works on this topic has focused on


## Page 5


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
Understanding opinions. A cognitive and formal account
5
polarization, i.e. the concentration of opinions by means of interaction, as one main
eﬀect of the ”social inﬂuence” [11], whereas the Social Impact Theory’ [2] proposes
a more dynamic account, in which the amount of inﬂuence depends on the distance,
number, and strength (i.e., persuasiveness) of inﬂuence sources. As stated in ([7]),
an important variable, poorly controlled in current studies, is structure topology.
Interactions are invariably assumed as either all-to-all or based on a spatial regular
location (lattice), while more realistic scenarios are ignored.
Although very interesting, these studies fail to address the speciﬁcity of opinions,
treating them as generic mental objects that change as a consequence of social
inﬂuence, as it happens also to beliefs, or even goals. The question about what
an opinion is and what its main features are remains unanswered, as well as their
relationships with attitudes and their resistance to inﬂuencing.
2.2. Computer science and complex systems: hyper-simpliﬁcation
fallacy
Turning our attention to complex systems science, one of the most popular model
applied to the aggregation of opinions is the bounded conﬁdence model, presented
in [10]. Much like previous studies, in this work agents exchanging information
are modeled as likely to adjust their opinions only if the preceding and the re-
ceived information are close enough to each other. Such an aspect is modeled by
introducing a real number ǫ, which stands for tolerance or uncertainty ([7]) such
that an agent with opinion x interacts only with agents whose opinions is in the
interval ]x −ǫ, x + ǫ[. This hyper-simpliﬁcation helps in making this complex phe-
nomenon more tractable using computational tools but, at the same time, reduces
it to a simple exchange of values that stand for mental objects, without any kind
of relationship with mental representations. An analogous attempt to model social
inﬂuence has been done by Axelrod (1997), who focused on the spreading of given
cultural features through communication. Again, agents do not have internal repre-
sentations of what they transmit, and ﬁnal results are mainly due to initial topology
and to the distribution of traits, without a real exchange among agents.
The model we present in this paper extends the bounded conﬁdence model by
providing a cognitively plausible deﬁnition of opinion as mental representations and
identifying their constitutive elements and their relationships.
We claim that opinions are highly dynamical representations resulting from the
interplay of diﬀerent mental objects and aﬀected by the mental states of other in-
dividuals in the same network. Aim of this work is to provide an interdisciplinary
account to describe how social inﬂuence leads to opinion formation, evolution and
change. Moving from a characterization of opinions as mental representations with
speciﬁc features, we will try to model how opinions are generated within the agents’
minds (micro-level) and how they spread within a network of agents (macro-level).
When explaining the emergence of macro-social phenomena we need to know what
happens at the micro-level, i.e. what drives human actions and decisions in order to


## Page 6


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
6
Francesca Giardini, Walter Quattrociocchi, Rosaria Conte
understand how individuals’ representations and behaviors can give rise to socially
complex phenomena and how those aﬀect agents’ actions. Without explaining how
opinions are formed and manipulated within the individuals’ minds, it is very diﬃ-
cult to account for the way in which they change as an eﬀect of social inﬂuence. Our
aim is to understand whether and how heterogeneous agents, endowed with diﬀer-
ent beliefs and goals, may come to share a given viewpoint and what consequences
this sharing has on agents’ behaviors. We are interested in providing answers, at
least partially, to the following questions: What is an opinion? What mechanisms
lead people to change their opinions? How can individuals resist to changes? What
are the mechanisms of inﬂuence acting within and between individual minds? How
does social impact aﬀect agents’ elaboration of new or contrasting information?
3. A Cognitive Theory of Opinions
This work aims at outlining a non-reductionist cognitive model of opinions and their
dynamics. Diﬀerently from the models reviewed above, we ﬁrst provide a deﬁnition
of opinions as mental representations presenting speciﬁc features that make their
revision and updating more or less easy and enduring. Moreover, grounding opinions
in the minds allow us to take into account not only direct processes of revision
triggered by the comparison with others’ diﬀerent opinions, i.e. social inﬂuence, but
also revisions based upon changing in other mental representations supporting that
opinion.
The computational model introduced in this paper is intended to provide a pre-
liminary unifying framework to deﬁne opinions and to characterize their dynamics
in an easy but non-reductionist approach. Opinions in several models of opinion
dynamics are considered to change according to social inﬂuence, we try to outline
what is social inﬂuence and the way the social network structure aﬀects the agents’
opinions.
3.1. Facts and evaluations: two kinds of opinions
In everyday language the word opinion is often confronted with fact, stressing the
diﬀerence between something objective because it happened and there are proofs
of it, like in the latter case, and something that does not have any reference in
the external reality. This distinction is important, because it points to a prominent
feature of opinions, i.e. their being regarded as uncertain and not grounded in any
external proof. Opinions can be debated, compared, discussed, argumented, but
they can not be proven to be true, contrary to what happens with facts. However,
individuals continuously resort to their opinions as less stable but more versatile
mental objects whose relevance is not reduced because of their being uncertain.
This feature is speciﬁc of opinions and it also explains why opinions are more prone
to change and revision, especially when confronted with others’ opinions. Moreover,
identifying this and other traits as speciﬁc, allows us to place opinions among other


## Page 7


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
Understanding opinions. A cognitive and formal account
7
kinds of mental representations, describing the kinds of relationships opinions have
with epistemic and motivational mental objects.
Opinions can be described as conﬁgurations of an individual’s beliefs, values
and feelings that can be conditionally activated. Conditional activation points to
the ﬂexible and dynamic nature of these representations that are not grounded in
certainty and that usually come out from the merging and elaboration of other
representations and attitudes. Opinions are not only conditional, but also compo-
sitional. This means that, for instance, starting from my feeling of aversion toward
mathematics and as a consequence of having met a rude friend of friends who hap-
pened to teach math at school, when asked about my opinion on the time kids
should spend in studying mathematics, I can form or, better, activate an opinion
according to which the less time they spend the better it is.
Opinions stem from the conditional activation of diﬀerent kinds of mental repre-
sentations, that can have a propositional content or, as in the case of attitudes and
feelings, they can be more evaluative. However, there is a speciﬁc feature that dis-
tinguishes an opinion from other kinds of mental objects. An opinion is an epistemic
representation in which the truth-value is deemed to be uncertain. Opinions refer
to objects of the external world that can not be told to be either true or false. This
impossibility (or irrelevance) to say whether the content of a representation is true
or false, but only if it makes sense according to what someone believes and knows
is what makes a mental representation an opinion. This essential feature accounts
for the fact that opinions can be easily inﬂuenced not only by social inﬂuence, i.e.
an external force, but that they can also be easily revised according to the change
in one’s own mental representations.
This basic feature can be paired with the presence of an attitude, i.e. an evalu-
ative component that speciﬁes whether the individual likes or dislikes the topic. In
general, attitudes are present when the topic is somehow involving for the subject,
so he is positively or negatively inclined toward it.
When this is not the case, we have ”factual opinions”, like in the following
example. If someone is required to say when Mozart died, he can know the correct
answer or not, but this is not a moot point. On the contrary, the causes of Mozart’s
death are debatable because without knowing where he was buried it is impossible
to analyze the bones and to ascertain what killed him. This means that we know
that Mozart died in 1791 but there are contrasting opinions about the causes of his
death, and, even if there exist one true opinion, none can tell which is the truth.
On the other hand, when opinions involve also evaluative components or facts, the
opinions result from the activation of a pattern of related representations like beliefs,
knowledge, other opinions, but also goals. This view allows us to describe opinions
as non-static patterns of relationships in which diﬀerent representations are linked
through a variety of diﬀerent linkages. This work is meant to address the origin and
changing of opinions thanks to these inter-relationships.


## Page 8


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
8
Francesca Giardini, Walter Quattrociocchi, Rosaria Conte
3.2. A tripartite model of opinion: truth-value, conﬁdence and
sharedness
An opinion is characterized by the three following features. First, the truth value
can not be veriﬁed (or it is not relevant). In general, opinions are representations
whose truth value can not be assessed through direct experience. The topic of
the opinion can not be experienced and then it is impossible to say whether a
given object is true or false. If I ask someone about his opinion on the military
intervention in Afghanistan, he can not tell me that his opinion, whether positive
or negative, is true, because it is not possible to test an alternative state of the
world in which the intervention has not taken place and then asses which state was
the best. Nonetheless, he can tell me that he has a strong opinion or that he is very
conﬁdent in it because he has many supporting beliefs (e.g. Talibans’ regime had
to be ﬁghted, civilians needed the intervention, the world is a safer place after the
intervention, etc) and even some goals (for instance, feeling safer) related with that
opinion. We can have strong or weak opinions, but our conﬁdence does not depend
on the fact that something is known to be true, given the impossibility to assess
its truth-value. In other cases, assessing the truth-value is not relevant, because the
attitude and the supporting mental representations are stronger enough to support
the opinion, without caring for its being true or false. Going back to the example
about the time spent in studying math, I can build upon my negative experience at
school, supporting it with my negative attitude and recalling my experience with
the unfriendly friend of my friends who happens to be a math teacher, to build
up my negative opinion. Furthermore, notwithstanding the existence of statistics or
experts that can support or confute my opinion, I do not care about them, because
they are not relevant to me. A creationist’s opinion about Darwin and the theory
of natural selection is not aﬀected by the proofs of its validity, because he does not
care for those proofs and focus his attention on other kinds of knowledge (like that
coming from the Bible, for instance).
The second feature is the degree of conﬁdence which is a subjective measure of
the strength of belief and it expresses the exent to which one’s opinion is resistant to
change. This is to say that the lack of an assessable truth value is totally independent
from the conﬁdence one has in his opinions.The degree of conﬁdence depends on
the number of supporting representations, and the higher this number the stronger
an opinion will be. Castelfranchi, Poggi [6] made a distinction between conﬁdence
coming from the source and conﬁdence coming from the degree of compatibility
that a given belief has with pre-existing beliefs. It is interesting to notice that
representations do not need to be about the same topic or to belong to the same
set to form a coherent network. If we take the Afghanistan example, we can easily
imagine that a negative opinion about the military intervention could be supported
by a general belief about the right of other countries to intervene in internal disputes
or by negative evaluations about the US foreign policy, or even by knowledge about
the roles played by URSS and US in Afghanistan during the Cold War. These


## Page 9


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
Understanding opinions. A cognitive and formal account
9
beliefs are not exclusively related to the target opinion and they can have stronger
or weaker connections with other opinions. The stronger the conﬁdence in these
beliefs and the higher their number, the stronger will be the conﬁdence in that
opinion.
The degree of conﬁdence can also vary in accordance with the conﬁguration
activated by a certain opinion. Since opinions are dynamic conﬁgurations emerging
from the conditional activation of other representations, the path followed to link
diﬀerent beliefs, goals, data and memories can result in opinions that have the same
content but diﬀerent degrees of conﬁdence. I can be against the military intervention
in Afghanistan because I feel empathic with the civilians, thus focusing on the
attitudinal and evaluative aspects, or because I have strong beliefs about the US
foreign policy. In this latter case, my opinion is supported by facts and follows a
speciﬁc argumentative line, and it could lead me to be more conﬁdent.
Finally, the sharing of an opinion, i.e. the extent to which a given opinion is
considered shared, is another crucial feature. The sharing may heavily aﬀect the
degree of conﬁdence, making people feel more conﬁdent because many other indi-
viduals have the same opinion. The sharing is the outcome of a process of social
inﬂuence, through which agents’ opinion are circulated within the social space and
they can become more or less shared. This dimension is crucial, but it is also true
that it carachterizes other social beliefs, like reputation.
It is worth noticing that there are other kinds of beliefs that are really close
to opinions but, at a closer investigation, there are some important diﬀerences.
Reputation can be one of these, because it is shared and it is also carachterized by
a varying degree of conﬁdence. But, unlikely opinions, reputation has a truth value
because it refers to someone’s behaviors or actions that were actually exhibited (or
that were reported as such, but we do not want to address here the issue of lying)
and reported to other people. Reality matters in reputation, whereas it is much less
relevant in opinions, as witnessed also by the fact that reputation does not have to
be convincing (i.e. supported by some reasoning or arguments), whereas opinions
need.
4. Toward a Formal Deﬁnition
4.1. Preliminaries
4.1.1. Time Varying Graphs
As mentioned in previous section the temporal aspects of our opinion model is
based upon Time-Varying Graphs (TVG) formalism, an algorithmic framework [8]
designed to deal with the temporal dimension of networked data and to express
their dynamics from an interaction-centric point of view [27].
Consider a set of entities V (or nodes), a set of relations E between these entities
(edges), and an alphabet L accounting for any property such that a relation could
have (label); that is, E ⊆V × V × L. L can contain multi-valued elements.


## Page 10


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
10
Francesca Giardini, Walter Quattrociocchi, Rosaria Conte
The relations (interactions) among entities are assumed to take place over a time
dimension (continuos or discrete) T the lifetime of the system which is generally a
subset of N (discrete-time systems) or R (continuous-time systems). The dynamics
of the system can subsequently be described by a time-varying graph, or TVG,
G = (V, E, T , ρ, ζ), where
• ρ : E ×T →{0, 1}, called presence function, indicates whether a given edge
or node is available at a given time.
• ζ : E × T →T, called latency function, indicates the time it takes to cross
a given edge if starting at a given date (the latency of an edge could vary
in time).
4.1.2. The underlying graph
Given a TVG G = (V, E, T , ρ, ζ), the graph G = (V, E) is called underlying graph
of G. This static graph should be seen as a sort of footprint of G, which ﬂattens the
time dimension and indicates only the pairs of nodes that have relations at some
time in a given time interval T . In most studies and applications, G is assumed to
be connected; in general, this is not necessarily the case. Note that the connectivity
of G = (V, E) does not imply that G is connected at a given time instant; in
fact, G could be disconnected at all times. The lack of relationship, with regards to
connectivity, between G and its footprint G is even stronger: the fact that G = (V, E)
is connected does not even imply that G is “connected over time”.
4.1.3. Edge-centric evolution
From an edge point of view (relationships within epistemic representations), the
evolution derives from variations of the availability. TVG deﬁnes the available dates
of an edge e, noted I(e), as the union of all dates at which the edge is available,
that is, I(e) = {t ∈T : ρ(e, t) = 1}. Given a multi-interval of availability I(e) =
{[t1, t2) ∪[t3, t4)...}, the sequence of dates t1, t3, ... is called appearance dates of e,
noted App(e), and the sequence of dates t2, t4, ... is called disappearance dates of
e, noted Dis(e). Finally, the sequence t1, t2, t3, ... is called characteristic dates of e,
noted ST (e).
4.1.4. Graph-centric evolution
From a global standpoint, the evolution of the system can be derived by a sequence
of (static) graphs SG = G1, G2.. where every Gi corresponds to a static snapshot
of G such that e ∈EGi ⇐⇒ρ[ti,ti+1)(e) = 1, with two possible meanings for the
tis: either the sequence of tis is a discretization of time (for example ti = i); or
it corresponds to the set of particular dates when topological events occur in the
graph, in which case this sequence is equal to sort(∪{ST (e) : e ∈E}). In the latter
case, the sequence is called characteristic dates of G, and noted ST (G).


## Page 11


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
Understanding opinions. A cognitive and formal account
11
4.2. Modeling Epistemic Representations
An opinion is an epistemic representation of a state of the world with respect to a
given object p. It is deﬁned on a three dimensional space deﬁned by: a) the objective
truth value To, a subjective truth value, namely Ts and a degree of conﬁdence dc with
respect to the object p.
More formally we can state that:
Deﬁnition 1. an epistemic representation of a state of the world m ∈M is a
quadruplet p, To, Ts, dc deﬁned by a preposition p related to a given object O, and
two variable To and Ts deﬁned on R. The dc ∈R respectively quantifying the “real“
truth value of an information, namely the objective truth value, the perceived truth
values, and the degree of conﬁdence, with respect to the preposition p.
By varying the dimensions of the domain of To and Ts, we can deﬁne a taxonomy
of the epistemic representation of the world that can be summarised as follows:
Deﬁnition 2. An epistemic representation mk = {p, To, Ts, dc} is knowledge when
To = Ts.
Deﬁnition 3. An epistemic representation mb = {p, To, Ts, dc} is a belief when
0 < To < 1 ∧0 ≤Ts ≤1 .
Deﬁnition 4. An epistemic representation mo = {p, To, Ts, dc} is an opinion when
0 ≤To < 1 ∧0 ≤Ts ≤1.
4.3. Opinions and Individuals
We can deﬁne an epistemic representation graph as a network of epistemic repre-
sentation immerged in a dynamic network in a given time interval and the links
state the correlation among them. Let us consider a set V of mental representation
(or nodes), interacting with one another over time. Each relation among the mental
representation can be formalized by a quadruplet c = {u, v, t1, t2}, where u and v
are the involved mental representations (either beliefs, or knowledge or an opinion),
t1 is the time at which the correlation occurs, and t2 the time at which the relation
terminates. A given pair of nodes can naturally be subject to several such interac-
tions over time (and for generality, we allow these interactions to overlap). Given a
time interval T = [ta, tb) ⊆T (where ta and tb may be either two dates, or one date
and one inﬁnity, or both inﬁnities), the set C(T ) (or simply C) of all interactions
occurring during that time interval deﬁnes a set of intermittently-available edges
E(T ) ⊆V × V , such that:
∀u, v ∈V, (u, v) ∈E(T )
⇐⇒∃t′ ∈[ta, tb), (u, v, t1, t2) ∈C(T ) : t1 ≤t′ < t2
(1)
that is, an edge (u, v) exists iﬀat least one interaction between u and v occurs,
or terminates, between ta and tb. The intermittent availability of an edge e =


## Page 12


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
12
Francesca Giardini, Walter Quattrociocchi, Rosaria Conte
(u, v) ∈E(T ) is described by the presence function ρ : E(T ) × T →{0, 1} such
that ∀t ∈T , e ∈E(T ):
ρ(e, t) = 1 ⇐⇒∃(u, v, t1, t2) ∈C : t1 ≤t < t2
(2)
The triplet G = (V, E, ρ) is called an epistemic representation graph, and the
temporal domain T = [ta, tb) of the function ρ, is the lifetime of G. We denote by
G[t,t′) the mental representation subgraph of G covering the period [ta, tb) ∩[t, t′)
Hence, a sequence of couples J = {(e1, t1), (e2, t2), ...}, with ei ∈E and ti ∈T
for all i, is called a journey in G iﬀ{e1, e2, ...} is a walk in G and for all i, ρ(ei, ti) = 1
and ti+1 ≥ti. Journeys can be thought of as paths over time from a source node to
a destination node (if the journey is ﬁnite).
Let us denote by J ∗
G the set of all possible journeys in an epistemic representation
system G. We will say that G admits a journey from a node u to a node v, and note
∃J(u,v) ∈J ∗
G , if there exists at least one possible journey from u to v in G.
4.4. Opinion Dynamics and Society
One of the most famous formalisms aimed at describing the process of persuasion
is the “Bounded Conﬁdence Model” (BCM) where agents exchanging information
are modeled as likely to adjust their opinions only if the preceding and the received
information are close enough to each other. Such an aspect is modeled by introduc-
ing a real number ǫ , which stands for tolerance or uncertainty such that an agent
with opinion x interacts only with agents whose opinions is in the interval ]x ǫ ,
x + ǫ [. Neverthless the wide, massive and cross-disciplinary use of the BCM ([19,
15]) ranging from “viral marketing” to to the Italians’ opinions distortion played by
controlled mass media ([25, 4, 5, 15]). Such a model does not provide an explana-
tion of the phenomena yielding to the tolerance value, it is just assumed as a static
value.
In this work we will outline which are the factors aﬀecting the acceptance or the
refuse of one another opinion. In particular, how can we formalize comparison of two
or more opinions? Recalling that a mental representation is a preposition with the
truth value deﬁned by two variable To, Ts ∈R and dc ∈R respectively quantifying
the “real” and the perceived truth value and the degree of conﬁdence with respect
to a given object or proposition. And considering that such mental representations
are modeled as set of time connected entities of the form G = (V, E, ρ) we can now
provide some deﬁnitions aimed at describing the process of persuasion.
Assuming that an epistemic representation system, which is by nature adaptive,
when facing with external events, reacts to the stimulus by activating only a subset
of its components. For instance, consider the example where an agent x is questioned
by an agent y about his opinion on a given target.
What does happen in the x’s mental representation system? How can we quantify
x’s attitudes to change or not is opinions regarding a given matter of fact?


## Page 13


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
Understanding opinions. A cognitive and formal account
13
According to our model the epistemic representation system of x, as reaction to
the external stimulus posed by the y’s question, will perform journey within the
elements that in its mind are related with the target of the question and on this
base will be able to compare its opinion with the one owned by y.
Deﬁnition 5. (relational-)connected component induced by an external event in Gx
is deﬁned as a set of nodes V ′ ⊆V such that ∀u, v ∈V ′, ∃J(u,v) ∈J ∗
G . Then G is
said connected if it is itself a connected component (V ′ = V ).
Since all nodes in V ′ are deﬁned by an objective truth value T and a degree of
conﬁdence (perceived truth value) dg it is obvious that the resistence to an opinion
to change is denoted by these values in all the nodes in V ′.
5. Conclusions
In this preliminary work we tried to sketch a cognitively grounded dynamic model
of opinions, in which we deﬁned these mental representations as carachterized by
the presence of three speciﬁc features. Diﬀerently than psychological theories of
opinions that usually provide rich deﬁnitions that are too complex to be reduced to
measurable variables, we isolated three main constitutive elements that characterize
this kind of mental representations. On the other hand, we tried to overcome the
reductionist approach of opinion dynamic models, in which the richness of human
cognitive processes is substituted by easy-to-compute factors poorly related to ac-
tual human behaviors. For this reason, we proposed to apply time-varying-graph to
develop a formal model able to account for the way in which opinions are gener-
ated and change as a function of the presence and opinions of other agents in the
network.
We are perfectly aware of the complexity of this issue and this work represents a
preliminary attempt to merge the cognitive complexity of opinions with a rigorous
formal approach, but there are many problems that we need to address. First, the
cognitive model should be reﬁned and speciﬁc hypotheses about opinion revision
and diﬀusion should be put forward. Moreover, the robustness of the formal model
will be tested and such a model will be implemented in cognitive multi-agent system
in order to explore the parameter space upon which our model has been deﬁned.
Our ultimate aim is to build up a simulation environment in which agents endowed
with heterogeneous representations of the external world interact and this leads to
the creation of new opinions, the disappearing of some of the previous ones and, in
general, to diﬀerent distributions of representations in the population.
6. Acknowledgements
This work was supported by the European Community under the FP6 programme
(eRep project CIT5-028575). A particular thanks to Ilvo Diamanti, Federica Mattei,
Mario Paolucci, Federico Cecconi, Stefano Picascia, Geronimo Stilton and the Hyp-


## Page 14


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
14
Francesca Giardini, Walter Quattrociocchi, Rosaria Conte
notoad. In addition we are grateful to the biggest Italian anomaly and the Italian
media for the inspirations and insights.
References
[1] E. Smith A. Mason, F.Conrey. Situating social inﬂuence processes: Dynamic, multidi-
rectional ﬂows of inﬂuence within social networks. Personality and Social Psychology
Review, 11(279-300), 2007.
[2] B. Latan´e A. Nowak, J. Szamrej. From private attitude to public opinion: A dynamic
theory of social impact. Psychological Review, 97:362–376, 1990.
[3] G.W. Allport. Readings in attitude theory and measurement, chapter Attitude, pages
1–13. Wiley, 1967.
[4] S. Brunetti, E. Lodi, and W. Quattrociocchi. Multicolored dynamos on toroidal
meshes. CoRR, abs/1012.4404, 2010.
[5] S. Brunetti, E. Lodi, and W. Quattrociocchi. Dynamic monopolies in colored tori.
APDCM - Alaska, 2011.
[6] I. Poggi C. Castelfranchi C. Bugie, ﬁnzioni e sotterfugi. Per una scienza dell’inganno.
Carocci Editore, 1998.
[7] V. Loreto C. Castellano, S. Fortunato. Statistical physics of social dynamics. Reviews
of Modern Physics, 81(2):591+, June 2009.
[8] A. Casteigts, P. Flocchini, W. Quattrociocchi, and N. Santoro. Time-varying graphs
and dynamic networks. 10th International Conference on Ad Hoc Networks and Wire-
less (ADHOC-NOW 2011), 2010.
[9] I. Crespi. The public opinion process. How the people speak. Lawrence Erlbaum As-
sociates, 1997.
[10] G. Deﬀuant, D. Neau, F. Amblard, and G. Weisbuch. Mixing beliefs among interact-
ing agents. Advances in Complex Systems, 3:87–98, 2001.
[11] L. Festinger, S. Schachter, and K. Back. Social Pressures in Informal Groups: A Study
of Human Factors in Housing. Harper, New York, NY, USA, 1950.
[12] D. Fleming. Attitude: The history of a concept. Perspectives in American History,
1:287–365, 1967.
[13] S. Galam. Sociophysics: A review of galam models. International Journal of Modern
Physics C, 19:409–440, Mar 2008.
[14] B. Latan´e H. Lavine. A cognitive-social theory of public opinion: Dynamic impact
and cognitive structure. Journal of Communication, 46:48–56, 1996.
[15] H. Hu and X. Wang. Discrete opinion dynamics on networks based on social inﬂuence.
Journal of Physics A: Mathematical and Theoretical, 42(22):225005+, June 2009.
[16] M.P. Zanna J.M. Olson. Attitudes and attitude change. Annual Review of Psychology,
44:117–154, 1993.
[17] B. Latan´e. The psychology of social impact. American Psychologist, 36:343–356, 1981.
[18] W. Lippmann. Public opinion. Penguin Books, 1946.
[19] J. Lorenz. Continuous opinion dynamics of multidimensional allocation problems un-
der bounded conﬁdence: More dimensions lead to better chances for consensus. Aug
2007.
[20] W. McGuire. The vicissitudes of attitudes and similar representational constructs
in twentieth century psychology. European Journal of Social Psychology, 16:89–139,
1986.
[21] I. Ajzen M.Fishbein. Belief, Attitude, Intention, and Behavior: An Introduction to
Theory and Research. Reading, MA: Addison-Wesley, 1975.
[22] V. Price. Communication concepts 4: Public opinion. Sage, 1992.


## Page 15


September
21,
2018
7:14
WSPC/INSTRUCTION
FILE
OpinionsECCS˙ArxiV
Understanding opinions. A cognitive and formal account
15
[23] W. Quattrociocchi and F. Amblard. Emergence through selection: The evolution of
a scientiﬁc challenge. Arxiv arXiv:1102.0257, Dec 2010.
[24] W.
Quattrociocchi
and
F.
Amblard.
Selection
in
scientiﬁc
networks.
Arxiv
arXiv:1012.4396v1, Dec 2010.
[25] W. Quattrociocchi, R. Conte, and E. Lodi. Simulating opinion dynamics in hetero-
geneous communication systems. ECCS 2010 - Lisbon Portugal, 2010.
[26] L.R. Fabrigar R.E. Petty, D.T. Wegener. Attitudes and attitude change. Annual Re-
view of Psychology, 48:609–647, 1997.
[27] N. Santoro, W. Quattrociocchi, P. Flocchini, A. Casteigts, and F. Amblard. Time
varying graphs and social network analysis: Temporal indicators and metrics. SNA-
MAS 2011, 2010.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
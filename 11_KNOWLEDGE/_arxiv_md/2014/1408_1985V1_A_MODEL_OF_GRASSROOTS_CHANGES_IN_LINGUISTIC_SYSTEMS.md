---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1408.1985v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1408.1985v1_A_model_of_grassroots_changes_in_linguistic_systems

> Source: 1408.1985v1_A_model_of_grassroots_changes_in_linguistic_systems.pdf

> Pages: 30

---


## Page 1


arXiv:1408.1985v1  [cs.CL]  8 Aug 2014
1
A model of grassroots changes in linguistic systems
Janet B. Pierrehumbert1,2,3∗, Forrest Stonedahl4, Robert Daland5
1 Linguistics Department, Northwestern University, Evanston, IL, USA
2 Northwestern Institute on Complex Systems, Evanston, IL USA
3 New Zealand Institute of Language, Brain, and Behaviour, Univ. of
Canterbury, Christchurch, NZ
4 Computer Science, Augustana College, Rock Island, IL, USA
5 Linguistics Department, Univ. California Los Angeles, Los Angeles, CA,
USA
∗E-mail: jbp@northwestern.edu
Abstract
Linguistic norms emerge in human communities because people imitate each other. A
shared linguistic system provides people with the beneﬁts of shared knowledge and coor-
dinated planning. Once norms are in place, why would they ever change? This question,
echoing broad questions in the theory of social dynamics, has particular force in relation to
language. By deﬁnition, an innovator is in the minority when the innovation ﬁrst occurs.
In some areas of social dynamics, important minorities can strongly inﬂuence the majority
through their power, fame, or use of broadcast media. But most linguistic changes are
grassroots developments that originate with ordinary people. Here, we develop a novel
model of communicative behavior in communities, and identify a mechanism for arbitrary
innovations by ordinary people to have a good chance of being widely adopted.
To imitate each other, people must form a mental representation of what other peo-
ple do. Each time they speak, they must also decide which form to produce themselves.
We introduce a new decision function that enables us to smoothly explore the space be-
tween two types of behavior: probability matching (matching the probabilities of incoming
experience) and regularization (producing some forms disproportionately often). Using
Monte Carlo methods, we explore the interactions amongst the degree of regularization,
the distribution of biases in a network, and the network position of the innovator. We
identify two regimes for the widespread adoption of arbritrary innovations, viewed as in-
formational cascades in the network. With moderate regularization of experienced input,
average people (not well-connected people) are the most likely source of successful inno-
vations. Our results shed light on a major outstanding puzzle in the theory of language
change. The framework also holds promise for understanding the dynamics of other social
norms.


## Page 2


2
Introduction
Many human needs and goals are shared by people in diﬀerent cultures. But the social
norms for addressing them can be highly arbitrary in their details. This is especially true
for norms that promote communication and social cohesion. The value of such norms may
arise more from the existence of a consensus than from its speciﬁcs. A fax machine has
value only insofar as other people also have compatible fax machines. Facebook supports
social contact only insofar as one’s friends and relations are also on Facebook.
This
situation is epitomized in the most complex and highly evolved communication system
of all, namely human language. Relationships between word forms and word meanings
are very idiosyncratic across languages, and hence must be learned for any individual
language [1, 2]. The usefulness of language comes about because people come to agree
on ways to refer to entities, events, and abstractions. Agreement enables them to pool
individual knowledge and beneﬁt from cooperative activities over great expanses of time
and space.
Once a linguistic consensus is in place in a community, why and how can it ever
change? This question, the central focus of our paper, is a major challenge for models
of language dynamics. It is widely agreed that linguistic systems emerge through innate
propensities for people to imitate others in their communities [3–9].
Frequent forms,
and forms produced by many diﬀerent speakers, are at an advantage in being learned,
remembered, and used [10–13]. In contrast, infrequent forms are vulnerable to loss over
time [12, 14]. These basic ﬁndings all mitigate against linguistic innovations, which by
deﬁnition are rare and poorly disseminated when they ﬁrst occur. Nonetheless, natural
languages are never perfectly stable. They change at a wide range of time scales, and the
fastest changes (such as the adoption of new slang expressions and jargon) are exhibited on
time-scales of a few months or less within the speech of individual adults. In this regard,
linguistic systems resemble cultural norms in other domains such as fashion, dancing,
politics, and religion. In these domains as well, people are strongly inﬂuenced by the
consensus of their neighbors, but norms still evolve over time.
Complex patterns of
variation across groups emerge when distinct groups follow diﬀerent trajectories of cultural
evolution.
Here, we develop a new model of how linguistic innovations can become widely adopted
in a community. We focus on a type of changes that are particularly challenging to model:
changes that we characterize as fast, arbitrary, and egalitarian. By fast changes, we mean
ones that occur through learning and adaptation by individual speakers in the course
of repeated interaction with their peers, without any generational replacement. Ref [15]
characterizes within-generation changes in social norms as cases of horizontal transmis-
sion. The slow changes that occur during cross-generational transmission of language fall
outside of the scope of this paper; modeling them requires distinct mechanisms [6,16].
By arbitrary changes, we mean changes that involve no global functional advantage.
They may be neutral, oﬀering no identiﬁable functional advantage at all. Or, if there is any


## Page 3


3
advantage to some people from adopting them, it is balanced by some equal disadvantage
to others. We do not deny that some changes in language may be globally advantageous.
For example, human languages are shaped by a persistent bias to encode more predictable
information using shorter expressions, which improves the eﬃciency of communication
[17]. However, prior work in language evolution, drawing on evolutionary biology, already
reveals how positive utility can cause an innovation to spread. In contrast, for many
linguistic changes, no global advantage is apparent. Explaining how arbitrary changes
can take hold is essential to explain the vast profusion of apparently arbitrary detail that
is observed synchronically [1].
We use the term egalitarian to highlight our interest in changes that originate with
ordinary people and spread without regard to social status. Sociolinguistic ﬁeld work
has shown that people at the forefront of linguistic change typically belong to the lower
middle class or upper working class. Although imitation of upper-class people may play a
role in some conscious choices, such as product purchases, it cannot be the fundamental
mechanism for linguistic changes. Typically, upper-class speakers eventually adopt pat-
terns set by lower classes, rather than the other way around [18]. This pervasive pattern
could not arise if imitating the few people at the top of the social hierarchy (perhaps in
an eﬀort to increase social capital) is the engine of linguistic change. However, the em-
pirical ﬁndings do not necessarily indicate that people preferentially imitate lower-class
people. Ordinary people are far more numerous than upper-class people, and this factor
alone might explain the results. We thus take as a starting point the null hypothesis by
which listeners weight input from all speakers equally, without assigning more value or
prestige to some speakers than to others. Unlike Refs [3,4], we do not assume that people
with many social connections have more status than others, or are preferentially taken as
linguistic models. This null hypothesis takes us surprisingly far. We identify a conﬂuence
of social and cognitive factors that enables fast, arbitrary, and egalitarian innovations
to propagate with considerable probability. The key cognitive factor is the decision rule
relating the perception of linguistic norms to the choice of what form to produce on any
particular occasion. The key social factor is the distribution of biases over the members
of the community. If some people are conservative, and others love novelty, the linguistic
system is more likely to change than if nobody is biased in either direction. These ﬁnd-
ings challenge previous claims [3,4,19] that diﬀerences in social prestige are a necessary
component in a theory of how linguistic innovations can spread.
Our model of how innovations propagate integrates technical ingredients from work
in several disciplines. Following recent work in network theory, we consider the linguistic
community to be a social network in which nodes represent people and links represent
social relationships. Speciﬁcally, a link between two nodes means that the two communi-
cate with each other and are disposed to imitate each other in their choices of expression.
Social ties that do not involve this level of mutual inﬂuence exist of course, but these ties
are omitted from the model.
Next, we draw a careful distinction between the mental state of a node and the signals


## Page 4


4
that the node emits.
We assume that signals are categorical.
For example, on each
individual occasion when some speaker wishes to quote someone else, she either uses the
conservative form (e.g. he said) or an innovative form (e.g. he was like). Mental states,
in contrast, are numbers on a continuous scale of probabilities, representing the speaker’s
current estimate of the linguistic norm. They take values from 0 (“I don’t believe anybody
uses that expression”) to 1 (“I believe everybody uses that expression”). The value 0 will
be used here for the conservative norm, and 1 for the innovation, so that in this example,
a mental state of 0.6 would represent the speaker’s belief that people in general use like
to express quotation with P = 0.6. The model is applicable to any linguistic innovation
that can be described as a new category competing with a pre-existing one. Examples
include novel slang, such as lol in competition with ha-ha; novel aﬃxes such as uber-
in competition with super-, as well as new constructions, such as gonna in competition
with will for expressing the future. It does not encompass gradient changes in the signals
themselves, such as the gradual shifts in vowel quality explored in Ref [20].
Signals and mental states are linked by a decision function, whose input is the mental
state and whose output is the probability of emitting diﬀerent signals.
This decision
process is unconscious, but it is not trivial. To characterize variability in the decision
function, we adopt the concepts of temperature and bias from the ﬁeld of reinforcement
learning. The bias captures the extent to which an individual generally favors conservative
norms versus innovations. Temperature characterizes the extent to which the individual
chooses the optimal production based on input received so far, versus exploring other
options. A higher temperature means that individuals make more random choices, an
analogy to the behavior of gas molecules, which exhibit more random motion under higher
temperatures.
In this application, we construe the optimal signal to be the one that
others are most likely to accept as the norm. A central innovation of our model is a novel
mathematical treatment of the decision function. In standard treatments of temperature,
the decision function is the SoftMax function, which reduces to the logistic in the case
of binary choices. The logistic is a sigmoidal function that maps inputs on the interval
(−∞, ∞) to values on the interval (0, 1). Varying the free temperature parameter τ causes
its form to vary between a step function as τ →0 and a constant function as τ →∞.
We analyze the behavior of the logistic function in the context of the emergence of
linguistic norms, and identify serious problems with its behavior and interpretability.
Linguistic norms resemble other application areas for reinforcement learning, because
people learn them incrementally from experiences over time. However, a critical diﬀerence
is that the signals produced by each individual provide the input for the neighbors, so that
repeated signaling gives rise to positive feedback loops in the community. The logistic
equation does not display sensible behavior under such iteration. For any temperature
τ > 0, it cannot characterize the situation in which an absolute agreement in the linguistic
community is stable. It is also unable to capture probability-matching behavior, in which
people produce linguistic variants with the same relative frequencies that they experience
them. Since probability-matching behavior and stable agreement are two of the principle


## Page 5


5
phenomena we need to characterize, we develop a new sigmoidal decision function that
incorporates the broad insights behind the logistic, while also avoiding these problems.
This is the clog (‘cognitive logistic’) function. Like the logistic, the clog is a sigmoidal
function that reduces to a step function as τ →0. Unlike the logistic, it is designed to
map probabilities onto probabilities. It converges to the line y = x, and not a constant
function, as τ →∞. Variation in τ is usefully viewed as variation in the categoriality of
the decision process. As τ →0, the output approaches two categories, y = 1 (or Boolean
TRUE) and y = 0 (or Boolean FALSE).
The variation in the input is completely
regularized in the output. As τ →∞, the categorization vanishes as all experienced
probabilities become equally available to the production system. The output faithfully
reﬂects the input, without any regularization at all.
Finally, these ingredients come together in our treatment of the diﬀusion of innova-
tions as informational cascades [21]. Informational cascades occur in a social system when
a local change propagates through a large group as a result of people’s repeated interac-
tions and tendencies to conform to each other. Initially developed in the area of opinion
dynamics and product adoption [21–23], the concept is applicable to language dynamics
under the assumption that linguistic norms are collective opinions about how to express
concepts [4]. Figure 1, the result of one run of our model, illustrates a partial informa-
tional cascade in a social network in which people vary in their biases. At the beginning
of the run, the innovator (at the left edge) is the only person in the network who has
adopted the novel expression. Although the innovator is directly connected to only three
other people, the expression is adopted by many others in the network to varying degrees
after a large number of communicative interactions have occurred.
To explore the behavior of the clog in relation to likelihood of informational cascades in
social networks, we report simulations on networks of 256 nodes. This size corresponds to
a village, social club, or adolescent peer group that might adopt a new opinion, fashion,
or linguistic expression in a short time. The social network is idealized as a scale-free
network generated by a preferential attachment rule [24].
We have already said that bias heterogenity is a key factor in the successful propagation
of linguistic innovations. Variation in individual biases is generated by sampling from a
uniform distribution. However, values are sampled in pairs to ensure the overall functional
neutrality of the innovative variant: each individual who is biased toward the innovation is
balanced by a diﬀerent individual in the same run with an equal but opposite bias. In the
ﬁeld of opinion dynamics, the adoption of an innovation is typically treated as absolute
and irreversible (c.f. [16, 25]). Under these assumptions, bias heterogeneity has already
proven to be an important factor in the propagation of innovations [26]. In contrast to
these models, we treat individual changes as reversible, in the interests of empirical realism
in the language domain. Reversibility does not aﬀect which end states can be reached
by the system, but it does impact the likelihoods of the diﬀerent end states, which is our
primary interest. The previous observations about the importance of bias heterogeneity
generalize to this new model structure.


## Page 6


6
Figure 1. A partial cascade of a novel form of expression originating from a
low-degree innovator. For each individual i, the degree of preference m for the novel
opinion is represented as a probability from blue (mi = 0) to red (mi = 1). The network
layout is governed by the distance from the innovator. Heterogeneous individual biases
are assigned on the basis of this distance as described in the text for the nearby
scenario. The decision rule is absolutely categorical (model parameter τ = 0).
Our Monte Carlo simulation, implemented as an agent-based model, systematically
explores the interaction between categoriality, innovator degree, and the distribution of
biases in the population. We contrast two baseline scenarios, for which we expect rather
stable norms, to three novel scenarios in which change is more likely. In one baseline
scenario, people simply reproduce the frequencies they encounter. This scenario is compa-
rable to neutral evolution in evolutionary biology, and is already known to make incorrect
predictions about rates of language change [27]. In a second baseline, people categorize
the frequencies they encounter (to greater or lesser extents), but no one has any bias for
or against the change; the only heterogeneity in the population is in the number of social
connections in the network. This setup is known to be highly stable if the decision function
is a step function [22,26], and we will extend this result to less categorical decision func-
tions. Of greatest interest are the three other scenarios, in which people in the network
both categorize frequencies, and vary in their biases. We designate these as the random,
hubs, and nearby scenarios. In the random scenario, bias values are distributed randomly


## Page 7


7
in the community. In the hubs scenario, innovation-favoring bias is preferentially allocated
to high degree nodes (hubs), and bias against the innovation is allocated to low degree
nodes. In the nearby scenario, innovation-favoring bias is preferentially allocated to the
individuals topologically nearest to the innovator (regardless of the innovator’s degree),
and bias against the innovation is allocated to the individuals that are furthest from the
innovation.
Cascading is rare in the random scenario, though this scenario does support some
partial cascades beyond those that are observed in a neutral evolution model. Two dif-
ferent regimes in which change is far more likely are identiﬁed. In the hubs scenario, the
probability of a cascade increases monotonically with categoriality and innovator degree;
total cascades become certain for suﬃciently high categoriality and innovator degree. This
regime may be relevant for social phenomena in which a few highly connected individuals
are able to trigger sudden changes in collective opinion through their ability to broadcast
their preferences to a large number of people at once. However, it is less relevant to lan-
guage change than the nearby scenario. In the nearby scenario, cascades are most likely
at a moderate level of categoriality, and are most likely to be initiated by individuals
with low to middle degrees of connectivity. This novel result captures the phenomenon
of changes that are fast, arbitrary and egalitarian. It represents a previously unsuspected
regime for informational cascades. The discovery of this regime is due to our model’s
ability to formalize the concept of moderate categoriality and explore the interaction of
categoriality with heterogeneity in the population.
1
Model deﬁnition and justiﬁcation
1.1
Social network
We consider N individuals in a community whose network structure is represented by a
graph with adjacency matrix A. The matrix entry aij = 1 if individual i is a neighbor
of individual j (e.g., individuals i and j are connected) and 0 otherwise. As explained
above, the links are interpreted to mean that the two individuals communicate with each
other and are disposed to imitate each other; social connections that lack this force are
omitted. The number of neighbors of individual i, ni = P
j aij, deﬁnes the individual’s
degree in the network.
Individuals interact with their neighbors in the network, and
these interactions are assumed to be bidirectional and uniformly weighted. Adjacency
matrices are generated using preferential attachment [24], with an average degree of 4.
This represents an intermediate degree of network connectivity that falls within the range
for global cascades to occur [22]. Results for average degree 3 are similar, and are not
reported here.


## Page 8


8
1.2
Social norms and signals
Competing forms of expression are represented within the minds of individuals. With each
communicative action, an individual elects to use one of them. For example, to express
the past tense of slink, a speaker of English has a choice between slinked and slunk, but in
each speciﬁc utterance, only one of these is used. The choice of signal is treated as a binary
(Boolean) variable that assumes values of 0 (FALSE) or 1 (TRUE). In our simulations, 1
will always denote the innovation that may or may not cascade, and 0 will always denote
the pre-existing consensus. This binary treatment of the available choices entails little loss
of generality. If a new expression, such as snowpocalypse, competes against a variety of
pre-existing expressions, such as blizzard, large snowstorm and massive snowfall, 0 denotes
the use of any of the earlier forms.
We deﬁne the observable signal from individual i as a function of time as si(t). The
signal is communicated to all of the neighbors in the network at the same time. This
means that individuals with many neighbors (represented by nodes with high degrees)
are heard by many more people than individuals with few neighbors; however, by the
egalitarian assumptions of the model, these better-connected people also listen to more
people. The mental state mi(t) of an individual i represents his or her private beliefs
about norms of language, as these beliefs develop over time. The model is initialized
with mi(0) = 0 for all individuals except a single innovator v, for whom mv(0) = 1. The
innovator could deviate from the group consensus because his beliefs were formed before
joining the network, or through a mutation process whose details fall outside of the scope
of this paper. As individuals acquire experience over time, their mental states change
because they are inﬂuenced by their impressions of their neighbors’ norms.
We next
describe the learning rule that determines mi(t). We return later to the characterization
of the relationship between mi(t) and the signal output at time t + 1.
1.3
Social assimilation
In general, social learning is driven by general inclinations to assimilate one’s opinions
and behaviors to those of others in the community [16,23,28,29]. Applying these ideas to
language, individuals estimate the community norm from the relative frequency of each
signal type in their aggregate input. Taking Ni to be the set of neighbors of individual i
(e.g. {j|aij = 1}) and ni to be number of neighbors, the input to that individual at each
timepoint is thus the mean of the signals sj emanating from the members of Ni.
inputi(t) = 1
ni
X
j|j∈Ni
sj(t)
(1)
However, individuals do not instantaneously copy the current input as their new mental
state.
People’s beliefs generally reﬂect a combination of prior experience and current
input. Standard learning models capture this by using a weighted average of the prior


## Page 9


9
mental state and the current input as the update rule, with a learning rate parameter
0 ≤α ≤1 [15,30].
mi(t) = α · inputi(t) + (1 −α) · mi(t −1)
(2)
The memory term (1 −α) · mi(t) holds individual i back from slavishly following the
neighbors. α has no ﬁxed interpretation in relation to the time scale of learning, but rather
reﬂects the temporal granularity of a batch-processed approximation to social reality. We
will report model runs for α = 0.1, selected to give insightful results using the available
computational resources. With this value of α, individuals give 9 times more weight to
their existing knowledge than to the immediate input from their neighbors.
1.4
Unbiased decision rules
The mental state mi and the learning rule Eq. 2 capture the way in which the individual’s
beliefs about the ambient social norm evolve as input arrives. Now we turn to the question
of how individuals act on the basis of this knowledge, where action means making a choice
of which signals to express. We ﬁrst consider the case in which individuals act without
any kind of preference or bias.
1.4.1
Criterion or threshold decision rules
The criterion choice rule (also known as a threshold choice rule) maximizes the expected
utility in the case of perfect knowledge [31, 32].
As a consequence of its mathematic
deﬁnition, utility can assume values from −∞(an inﬁnite loss) to ∞(an inﬁnite gain).
Considering a binary choice between mutually exclusive alternatives a and ¬a, we deﬁne
Q(a) as the utility of a, and Q(¬a) as the utility of ¬a. The criterion choice rule then
takes the form:
P(a) =





0
if Q(a) < Q(¬a)
0.5
if Q(a) = Q(¬a)
1
if Q(a) > Q(¬a)
(3)
An individual should choose a if it oﬀers a net utility beneﬁt over ¬a. The same equation
can be also applied to perceptual decisions based on an inﬁnite scale of evidence; an
individual should reach conclusion a if the total evidence for a is greater than the evidence
for ¬a.
For language, let’s imagine that the individual wants to produce the signal that is most
likely to be accepted by any random member of the community. This means producing the
signal that most other people use, on the assumption that what people use is what they
will accept. This goal is similar to the goals of maximizing economic utility or reaching the
best-supported conclusion, except that the input to the decision is not a utility or scale
of evidence, but rather the mi, the mental estimate of community norms. The criterion
choice rule can be put into following form.


## Page 10


10
P(si = 1) =





0
if mi < 0.5
0.5
if mi = 0.5
1
if mi > 0.5
(4)
The individual i should choose s = 1 if, according to his beliefs, it is more likely than
s = 0 to be the general norm.
Eq. 3 and Eq. 4 are the same except for the range
of the input variable. Q(a) and Q(¬a) can take values anywhere in the interval (−∞,
∞), whereas m can only take values in the interval [0, 1]. This diﬀerence in range has
little importance if the decision function is a step function. However, for other decision
functions the diﬀerence in range has important consequences.
Eq. 4 is an absolutely categorical decision rule. Even if the input to the individual
has been variable, the individual treats one of the competing forms as normative, and the
other input as deviant, invariably producing the normative form as the output. This is
not what people do. If linguistic norms vary amongst individuals in a group (as happens
during periods of language change), then many individual speakers also vacillate in what
form they choose to express [33,34]. In experiments where some regularization of the input
is found, it is never absolute [35–37]. To model real linguistic behavior, a less categorical
decision rule is needed.
1.4.2
The SoftMax and logistic functions
In economics, a threshold decision rule is only guaranteed to be optimal in the case of
perfect knowledge. It may not be optimal in the case of imperfect knowledge, because
the threshold must be set on the basis of information already acquired, and it is possible
that some information about the real optimum has not yet come to light. Speakers in a
linguistic community also have imperfect knowledge of what other speakers do, because
they only receive input from communications they are involved in. The statistical prop-
erties of communications that take place in more distant parts of their social networks
are invisible to them, as are the communications that will take place in the future. These
observations lead naturally to the conjecture that the cognitive system processes the fre-
quencies of linguistic inputs in a manner that resembles reasoning under uncertainty in
other areas of cognition.
The theory of reinforcement learning provides a general framework for understanding
how learning proceeds incrementally as more and more evidence becomes available from
experience. The SoftMax equation contains a free temperature parameter τ that captures
the extent to which the learner makes the optimal choice based on the evidence so far,
or makes a random choice which may yield more information in the future [31]. If there
are only two choices, the SoftMax reduces to the logistic function Eq. 5, which is a
generalization of Eq. 3 and is expressed here in a form that emphasizes the parallelism.
P(a) =
eQ(a)/τ
eQ(a)/τ + eQ(¬a)/τ
(5)


## Page 11


11
The parameter τ captures the categoriality of the decision. As τ →0, the learning
system becomes completely categorical, rigidly applying a threshold based on past evi-
dence. This is the low temperature situation because the decision function can be viewed
intuitively as a frozen reﬂex of the past. As τ →∞, the decision becomes random without
regard to past evidence.
The logistic function is a sigmoidal function that is widely used in analyzing cognitive,
social, and biological processes that involve a competition between two states. Its many
applications include not only decisions under uncertainty in economics, but also analysis
of the time course of linguistic changes [38, 39], the categorization of perceptual inputs
[40,41], and binary choices as a function of a continuous and unbounded scale of evidence
[32].
The crux of the problem is whether it makes sense to add τ in just the same manner
to a decision function that maps mental probabilities onto signaling actions, as shown in
Eq. 6.
P(s = 1) =
em/τ
em/τ + e(1−m)/τ
(6)
The answer to this question rests on the behavior of Eq. 6 as it is iterated through
repeated social interactions. Figure 2 graphs Eq. 6 as the temperature τ is varied over its
full range. To understand the behavior of the function, it will be convenient to have an
equation for the angle φ at the inﬂection point.
φ = arctan
1
2 · τ
(7)
Varying τ is accomplished by varying φ from 90◦to 0◦. φ = 90◦in the limit as τ →0
and φ = 0◦in the limit as τ →∞. The points of most interest are the ﬁxed points, deﬁned
as the points for which the output and input are the same (eg. the points where Eq. 6
crosses the identity function P(si = 1) = mi). The stable ﬁxed points act as attractors;
that is, slight deviations in the vicinity of a stable ﬁxed point push the result back onto
the same point. The unstable ﬁxed points act as repellers; slight deviations send the result
away from the ﬁxed point. Thus, the stable ﬁxed points represent predictions about the
possible long-term states for the system.
The location and stability of the ﬁxed points for Eq. 6 vary as φ is varied.
For
45◦< φ < 90◦, there is an unstable ﬁxed point at (0.5, 0.5), which means that for
moderate temperatures, free variation between two competing forms is unstable towards
a system in which one variant is preferred. This behavior is somewhat realistic, but not
entirely so, because the location of the stable ﬁxed points is problematic. No value of φ
other than 90◦has a stable ﬁxed point at (0, 0) or (1, 1). For 45◦< φ < 90◦, there are
indeed two stable ﬁxed points. However, one is always located at 0 < mi < 0.5 and the
other is always located at 0.5 < mi < 1.


## Page 12


12
▲
Fixed points
▲
▲
▲
▲
▲
▲
▲
▲
▲
▲
▲
▲
mental state (      )
mii
mental state (      )
mi
(s  = 1)
i
P
(s  = 1)
i
P
▲
▲
▼
▼
▼
▼
Fixed points
Fixed points
stable
stable
unstable
unstable
Figure 2. Behavior of the logistic function as φ is varied. φ determines the
location and nature of the ﬁxed points. A: Except for φ = 90◦, the function lacks ﬁxed
points at (0, 0) and (1, 1). For φ ≤45◦, the unstable ﬁxed point at (0.5, 0.5) becomes a
stable ﬁxed point. B: Detailed view of behavior in the lower-left quadrant. φ varied in
5◦steps. For φ > 45◦, there is an unstable ﬁxed point at (0.5, 0.5). For φ ≤45◦, the
ﬁxed point at (0.5, 0.5) is stable.
This situation has the unfortunate consequence that inputs of mi = 0 and mi = 1
yield outputs that are shifted towards the center. It means that all binary competitions
in language continue to the end of time; no form or expression can ever truly go extinct.
To make a comparison to norms of attire, some 600 years ago, garments called chausses
were in competition with garments called breeches; breeches eventually won out. If neither
I nor anyone in my community has any knowledge or experience of chausses, then we have
all adopted the innovative form and a model of our speech community has mi = 1 for
all individuals i. A model using a logistic choice function would nonetheless predict that
the archaic form chausses has a predictable and persistent tendency to reappear as a
competitor to breeches, as we continue to interact with each other in the future. In fact in
language, just as in biology, something that is extinct is gone forever. New competitions
arise, but these are due to fresh innovations. The invention of trousers is what created later
competition for breeches, and not the persistent return of chausses from the graveyard of
fashion history.
A further problem is revealed for 0◦≤φ ≤45◦. In this case, the ﬁxed point at (0.5, 0.5)
becomes stable. At high temperatures, the system is predicted to converge towards free


## Page 13


13
variation. For language systems, this asymptotic behavior is highly questionable. This
would mean that if people weakly categorize the input they receive about two competing
words or constructions, their output persistently reverts towards completely free variation.
This would behavior would count as a tendency towards true synonymy (in which two
forms completely share their denotation and their range of use). But, in the psycholin-
guistic literature, avoidance of true synonymy is documented in people of all ages, and it
is argued to play a key role in the emergence of meaning categories in language [42–44].
The formalization of the concept of temperature in the context of language and collective
opinions needs to be reconsidered.
Note ﬁnally that the logistic never falls on the line y = x. For φ = 45◦, it tracks y = x
in the middle of the range, but curves away from this line for more extreme values. This
means that it cannot be used to model probability-matching behavior, which is widely
assumed to be relevant for language [45–48].
1.5
Introducing the clog function: categoriality and bias
The problems with the applicability of Eq 6 arise from the fact that it converges to
P(s = 1) = 0.5 as τ →∞. Although Eq. 3 and Eq. 4 have similar behavior as formulations
of a criterion (or expectation maximization) decision rule, this similarity disappears as
soon as nonzero temperatures are introduced. This problem is solved if we assume that
the sigmoidal function should instead approach P(si) = mi as τ →∞. We now develop
the mathematical apparatus to explore this assumption.
We deﬁne a new relative of the logistic, the clog (‘cognitive logistic’) function that
converges to the identity function as τ →∞:
clogτ(m) =
m · em/τ
m · em/τ + (1 −m) · e(1−m)/τ
(8)
Just as for the logistic, it will be convenient to characterize the degree of nonlinearity
in the clog function in terms of the slope φ at the inﬂection point, which we will denote
as m∗. It is:
φ = arctan (1 +
1
2 · τ )
(9)
In the limit of φ →45◦(i.e. τ →∞), clog reduces to the identity function; the
production probabilities are exactly the same as the current mental state. As φ →90◦
(i.e. τ →0), the function approaches a step function with the discontinuity at m∗. For
all τ < ∞(φ > 45◦), Eq. 8 has attracting ﬁxed points at (0, 0) and (1, 1). This means
that uncertain opinions tend to become polarized in the course of repeated interactions
towards more absolute opinions.
The stability of these ﬁxed points provides for the
ultimate extinction of losing competitors. The inﬂection point m∗in between m = 0 and
m = 1 (located at m = 0.5) is a repelling ﬁxed point. Because m∗is always unstable,
there is never a regime in which the system is attracted towards free variation.


## Page 14


14
The limiting case represented by φ = 45◦is studied in the literature under the name
of a probability-matching rule, a relative goodness rule or Luce’s Choice Rule [32].
Thus far, we have considered only unbiased decisions, which rest entirely on the balance
of utility, evidence, or likelihood of the two alternatives. In practice, biased decision-
making processes are frequently encountered. Such biases are normally accommodated in
Eq. 5 for the logistic by introducing a second free parameter β.
P(a) =
e(Q(a)−β)/τ
e(Q(a)−β)/τ + e(Q(¬a)+β)/τ
(10)
Varying β has the eﬀect of shifting the entire function. If β < 0, the individual is more
likely to pick the innovative variant than would be expected from its utility. If β > 0, he
is less likely to do so.
Figure 3 illustrates the results of attempting to recast Eq. 10 as a function from mental
probabilities to signaling actions, as shown in Eq. 11.
P(s = 1) =
e(m−β)/τ
e(m−β)/τ + e(1−m+β)/τ
(11)
mental state (      )
mi
P (s  = 1)
i
▲
▲
▼
▲
▲
Fixed points
▲
▲
▲
Stable
▼
Unstable
β = -0.2
β = 0.0
β = +0.2
β = 0.0
Figure 3. Behavior of the logistic function for φ = 60◦as β is varied. The
unstable ﬁxed point at (0.5, 0.5) is lost for small biases β = 0.2 and β = −0.2. Each of
these β values results in a system with a single stable ﬁxed point.


## Page 15


15
The shift in the function shifts the location of the inﬂection point occurring in the
unbiased case at mi = 0.5.
The number and stability of the ﬁxed points is greatly
aﬀected. A small positive bias gives rise to a single stable ﬁxed point representing a high
level of acceptance of the innovation, and a small negative bias yields a stable ﬁxed point
that represents a low level of acceptance of the innovation.
In contrast to the logistic, the clog can incorporate a bias parameter without restruc-
turing the ﬁxed points. Including a bias parameter β into the clog function yields the
following fully elaborated form.
clogτ,β(m) =
m · e(m−β)/τ
m · e(m−β)/τ + (1 −m) · e(1−m+β)/τ
(12)
For the clog, β controls the location of the unstable ﬁxed point m∗, which is always
located at mi = 0.5 + β. If βi < 0, m∗
i < 0.5, and individual i has a greater propensity to
produce 1 than the input from the neighbors would dictate. Similarly, if βi > 0, m∗
i > 0.5,
and the individual has a disproportionate tendency to produce 0. The stable ﬁxed points
are unaﬀected by the value of β. The introduction of a function that smoothly interpolates
between a criterion choice rule and a probability-matching choice rule, under under any
choice of bias, while always having ﬁxed points at (0, 0) and (1, 1), is a novel contribution
of this paper.
Heterogeneity amongst community members in β is the primary type of heterogeneity
that we explore. The diﬀerent scenarios for informational cascades depend on positive
and negative values of β being distributed in diﬀerent ways across the individuals in the
network.
Figure 4 illustrates the behavior of clog as φ and β are varied. In this ﬁgure, note
particularly that varying β has no eﬀect on the ﬁxed points at (0, 0) and (1, 1) for φ > 45◦.
This entails that the clog (unlike the logistic) cannot represent a uniform distribution on
the closed interval [0, 1]. Note also that the eﬀects of β are neutralized if φ = 45◦; the
concept of bias is only meaningful if the choice rule is at least somewhat categorical.
1.6
Implementation
The model is implemented in the NetLogo agent-based modeling environment [49]. It is
initialized at time t = 0 with mi(0) = 0 for all individuals i in A, except for a single
innovator v, for whom mv(0) = 1. During each model cycle t + 1, every individual ﬁrst
randomly produces an expression of opinion, 0 or 1, with probability:
P(si(t) = 1) = clogτ,β(mi(t))
(13)
Then they update their mental state from mi(t) to mi(t + 1) on the basis of the set of
signals emitted by their neighbors Ni (e.g. {sj(t)|j ∈Ni}), using Eq. 2. Each model
run is terminated when the population reaches a consensus (deﬁned as mi < 10−8 or
mi > 1 −10−8 for all i), or at the 10,000th iteration if no convergence has occurred.


## Page 16


16
▲
▲
▼
▼
▼
mental state (      )
mi
(s  = 1)
i
P
Fixed points
Stable
▲
β 
all
Unstable
▼
▼
▼
β = -0.3
β = 0.0
β = +0.3
for φ > 45
Figure 4. Behavior of the clog function as β and φ are varied. Blue: No bias.
Magenta: Bias against the pre-existing consensus, equivalent to bias toward the
innovation. Green: Bias toward the pre-existing consensus, equivalent to bias against
the innovation. When φ = 45◦, the clog reduces to the dashed line P(si = 1) = mi for all
values of β.
The probabilities of cascades as a function of innovator degree are estimated by a
Monte Carlo method, in which innovator degrees from 2 to 55 are sampled equally in the
form of 500 runs for each degree. Innovators with degrees of 1 and > 55 are not included
because the preferential attachment rule for network construction does not generate nodes
with such degrees frequently enough. A fresh network is generated for each run, and all
individuals share a value of φ. φ was smoothly varied from φ = 45◦(linear) to φ = 90◦
(categorical) by increments of 1◦. In both baseline scenarios, all individuals are unbiased.
(In the ﬁrst baseline, this is because they follow a probability-matching decision rule.
In the second baseline, the decision rule is more categorical and βi = 0). In all other
scenarios, heterogenous values of βi are assigned, as described in the text.
1.7
Summarizing outcomes
In our Monte Carlo simulations, we vary the categoriality, the degree of the innovator and
the way that bias values are distributed across the community. Each model conﬁguration
yields a distribution of cascade sizes; the size of a cascade is distinct from the likelihood


## Page 17


17
of a cascade. In order to summarize the results, however, we conﬂate these two factors.
We use the following classiﬁcations of the average mental state ¯m of all the individuals in
the network when the model run ends at time tfinal.
• Survival: The innovation avoids extinction, deﬁned as ¯m(tfinal) > 10−4.
• Dominance: The innovation becomes dominant by surpassing the established vari-
ant, i.e. ¯m(tfinal) ≥0.5.
• Completion: The innovation drives the previous consensus opinion to extinction i.e.
¯m(tfinal) ≥1 −10−4.
2
Results in diﬀerent scenarios
We ﬁrst present two baseline cases in which all individuals are unbiased. Then, we compare
three scenarios in which individuals have heterogeneous biases.
2.1
Baseline scenarios
If φ = 45◦, each individual expresses each opinion in direct proportion to their experience.
The model instantiates the case of neutral evolution (also known as random drift [27]). For
a fully continuous system, the population would converge to the average of the initial states
of the individuals; however, because emitting a signal is a discrete probabilistic event, the
mean state instead exhibits a random walk on the frequencies of the alternative signals 0
and 1 [27]. The probability of a complete cascade is low, and is directly proportional to
the innovator’s degree, as shown in Figure 5.
If φ > 45◦(e.g individuals have at least some tendency toward categorical behavior),
and all individuals are unbiased (βi = 0 for all i), then the innovation always becomes
extinct; no cascades of any size are found. This very strong result on the impossibility
of change without bias heterogeneity occurs because memory is included in the model of
learning. Eq. 2 entails that a single signal si = 1 from an innovator i can never cause the
mental state of a neighbor j to increase from its initial value mj = 0 to a value greater
than the repelling ﬁxed point at m∗
j = 0.5. The innovator cannot convert anyone else,
and is eventually reconverted to the original consensus.
2.2
Scenarios with heterogeneous biases
To explore the role of heterogeneous biases while maintaining overall functional neutrality,
bias values are generated through random sampling on a uniform distribution over the
interval [0, 0.5].
Neutrality is enforced by taking both the +β and −β for every |β|
that is selected.
The resulting set of values is distributed over the individuals in the
social network according to one of three diﬀerent methods. In the hubs scenario, the


## Page 18


18
0
10
20
30
40
50
innovator degree
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14
Probability
survival
dominance
completion
R2 ≈0.99
R2 ≈0.96
R2 ≈0.78
Figure 5. Relationship of innovator degree to cascade probability in the
neutral evolution model. For all three summary cases, the relationship is linear. The
probability of a complete cascade is extremely small.
bias against the pre-existing consensus is preferentially allocated as a function of degree
centrality. The highest degree individuals are most disposed to change, and the lowest
degree individuals are least disposed to change. In the nearby scenario, the bias against
the pre-existing consensus is allocated as a function of the distance from the innovator;
individuals nearest to the innovator are the most disposed to change, and those farthest
from the innovator are least disposed to change. In the random scenario, bias values are
randomly distributed.
The hubs and nearby scenarios idealize skewed patterns in the distribution of biases
in the network. To motivate these idealizations, let us consider what the bias β means.
The case of negative bias generalizes the concept of early adopters, deﬁned in [22, 23]
as individuals who will adopt an innovation after encountering a single example of it.
Negative bias means that an individual is inclined to abandon the old norm, even if most
of the neighbors do not. Positive bias is a generalization of the concept of late adopters.
It means that an individual is inclined to continue using the old expression, even if the
neighbors use its more innovative competitor.
Such individual biases could arise as a reﬂex of personality traits such as levels of
adventurousness and nonconformity, which are factors in the standard theory of person-
ality [50] and are partially innate in people and other animals [51]. The diﬀerences could
also arise from knowledge or habits that provide a latent potential or impediment to the
adoption of the innovation. As a simple example, the use of text messaging provides a
platform for the use of slang acronyms like lol (laughing out loud) and btw (by the way),
and it would not be surprising if heavy users of text messaging were among the ﬁrst
to adopt these expressions upon encountering them. In modern linguistic theories, the
adoption of one construction may also provide a foundation for further change through


## Page 19


19
its indirect impact on the encoding system [34]. It is possible to develop a connection
between such individual biases and the concept of utility. We already provided an inter-
pretation of τ in relation to the global value of addressing any member of the community
in a cooperative manner, using a form they are likely to accept. β encapsulates any sort
of subjective personal utility that is independent from the utility to the community as a
whole of having shared norms.
The distribution of biases in the hubs scenario thus can be understood as one in
which individuals with many social connections share any type of knowledge, practice, or
experience that makes it easy for a speciﬁc linguistic innovation to take root. The nearby
scenario is even more plausible, because people with shared traits tend to form social
connections to each other [52]. Field studies of Belfast English indicate that feelings of
group solidarity aﬀect people’s choice of modes of expression [53]. The rate of adoption of
linguistic innovations peaks in adolescence [39]. In choices of language, music, and attire,
adolescents tend to be most inﬂuenced by the central members of their immediate peer
group (rather than by the highest status people in their whole world of experience) [54–56].
A group of young people who share rebellious attitudes and a love of novelty is indeed
the very prototype of a group with innovative language.
Results for the three scenarios are shown in Figure 6.


## Page 20


20
10
20
30
40
50
45
60
75
90
φ
survival
10
20
30
40
50
dominance
10
20
30
40
50
completion
10
20
30
40
50
45
60
75
90
φ
10
20
30
40
50
10
20
30
40
50
0.0
0.2
0.4
0.6
0.8
1.0
10
20
30
40
50
innovator degree
45
60
75
90
φ
10
20
30
40
50
innovator degree
10
20
30
40
50
innovator degree
A
B
C
Figure 6. Interaction of bias distribution with innovator degree and
categoriality in determining the likelihood of cascades.
Non-zero likelihoods of a cascade in each of the three categories survival, dominance,
completion are color-coded as shown.
Black indicates the absence of any cascades in
the simulation results. A: Bias values are assigned to individuals as a function of degree
centrality under the hubs scenario. B: Bias values are assigned to individuals as a function
of proximity to the innovator under the nearby scenario. C: Bias values are assigned
randomly to individuals.


## Page 21


21
2.2.1
Results for the hubs scenario
In the hubs scenario (Figure 6A), cascading is frequent and consistent for high-degree
innovators and high φ values. As the innovator degree decreases, the likelihood of success
also decreases. Furthermore, cascading is basically an all-or-nothing phenomenon; if a
cascade avoids extinction, it is very likely to go all the way to completion. Intuitively, if
an innovation survives the initial stage in this scenario, it has done so by spreading to a
backbone of high-degree adopters. These in turn can dominate the overall signal to the
rest of the network, because each of their expressions of opinion is sent to many neighbors.
Interestingly, when the input-output relation is not strongly categorical (i.e., φ ⪅75◦),
assigning the favorable bias values to the hubs is not eﬀective for causing cascades (re-
gardless of innovator degree). As seen in Figure 6A, a phase transition occurs in the
high-φ regime (φ > 75◦). As categoriality increases, the outcome passes from invariable
cascade extinction, through degree-sensitive all-or-nothing cascades, to complete cascades
(apart from very low-degree innovators).
Just visible in blue at the bottom of the graph is a sporadic set of cascades arising
from neutral evolution (φ = 45◦), corresponding to those displayed in Figure 5.
2.2.2
Results for the nearby scenario
We identify three regimes in the nearby scenario (Figure 6B). For 45◦≤φ ⪅55◦, no
cascades occur, apart from the few previously discussed for the φ = 45◦neutral evolution
model. For 55◦⪅φ ⪅65◦, cascades are more frequent, and often go to completion. For
65◦⪅φ ≤90◦, cascades become increasingly likely, but do not go to completion even
if they succeed in dominating the network. In particular, in the fully categorical limit,
where φ = 90◦, the cascade proceeds only a little further than halfway: ¯m(tfinal) = 0.56
(with the standard deviation σ = 0.069). The network already displayed in Figure 1
is a ﬁnal conﬁguration (at the 10,000th time step) for this partial cascade situation. It
shows how the novel opinion diﬀuses through some (but not all) of the network, leaving
an entrenched opposition elsewhere. This means that for innovations occurring in a social
network with a nearby bias distribution, a highly categorical decision rule tends to split
the social network into subgroups with diﬀerent norms.
In-depth examination of the case φ = 60◦(Figure 7) reveals another striking point.
The likelihood of success in triggering a cascade peaks in the vicinity of innovator degrees
7 ≤ni ≤15 for this level of categoriality. The individuals with degrees in this range
are more likely to succeed than very low-degree individuals, an eﬀect also visible for
other values of φ at the left edge of the panels in Figure 6B. Surprisingly, they are also
somewhat more likely to succeed than high-degree individuals. With this combination of
categoriality and bias, it is clearly not appropriate to describe the best-connected nodes
as inﬂuentials; their inﬂuence is actually constrained by the variability of their many
neighbors. Taking the network’s degree distribution into account, we can also calculate
the probability of the innovator degree, given that a cascade occurred. As Figure 7 shows,


## Page 22


22
this probability peaks at innovator degree ni = 4, which is by construction the average
degree of the network. Thus in this scenario, a successful innovation is most likely to have
originated from Joe or Jane Average.
0
10
20
30
40
50
innovator degree
0.0
0.1
0.2
0.3
0.4
0.5
0.6
Probability
P(cascade|degree)
P(degree|cascade)
Figure 7. Relationship of innovator degree to complete cascades for the
nearby scenario with φ=60◦. Red: The probability of a complete cascade, given the
degree of the innovator. Blue: The probability of the innovator degree, given that a
complete cascade occurred. Each data point is estimated from the 500 runs per degree
in the Monte Carlos simulation. Results are highly similar for cascade survival and
dominance.
2.2.3
Results for the random scenario
The hubs and nearby scenarios are highly idealized, and yield exorbitantly high success
rates for innovation.
In reality, the bias distribution is probably less stringently tied
to network position, and very many innovations fail.
A perspective on this reality is
provided by results on the random scenario in Figure 6C. Survival of an innovation is
fairly common when φ ⪆70◦. The rate of survival is notably higher than in the neutral
evolution model as shown in Figure 5, also visible in this ﬁgure panel as a blue line at
φ = 45◦. Dominating cascades are more rare. In addition to the few dominating cascades
found for φ = 45◦, a small cluster of dominating cascades is found for degree ni ⪆10
and φ ⪆80◦. Thus, moderate categoriality in combination with heterogeneity permits a
moderate to high degree innovator to have some chance of seeing an innovation widely
adopted. This likelihood becomes attenuated as φ approaches 90◦. Qualitatively, the
pattern suggests a mixture of cases skewed towards the nearby scenario and cases skewed
towards the hubs scenario. Complete cascades were not observed at all above φ = 45◦.
Of course, a complete cascade could occur if the random bias distribution happened to
distribute the bias in exactly the same way as in one of the more favorable scenarios in


## Page 23


23
Figure 6AB. The fact that this outcome is too rare to occur at all in our simulations
suggests that bias heterogeneity alone cannot fully explain how neutral innovations may
come to be adopted by an entire community. Instead, systematic patterns are needed in
the distribution of decision biases across individuals.
Discussion
We have presented a framework for exploring the interaction of categoriality, bias, and
innovator degree in permitting arbitrary linguistic innovations to succeed in a social net-
work. As anticipated from prior related models [23,26,27], model conﬁgurations in which
individuals are homogeneous and unbiased exhibit negligible success rates for innova-
tions. We identiﬁed two regimes involving heterogeneous biases that are conducive to
change. Under the hubs scenario, a highly categorical decision rule supports a mechanism
for the widespread adoption of innovations initiated by highly connected people. Under
the nearby scenario, a moderately categorical decision rule leads to a mechanism for the
grassroots changes to succeeed. This second regime, which was previously unsuspected
in research on informational cascades, is highly relevant to linguistic change because lin-
guistic changes typically originate with ordinary people.
Previous models of language dynamics have explored the ways that functional factors
can have major impacts on the linguistic structures through their iterated eﬀects in lan-
guage acquisition, perception, and production [46, 57]. Here we have shown that such
functional factors are not necessary for global changes to occur. Our results connect the
understanding of language dynamics with classic observations about the arbitrariness of
many words and expressions in human languages [1,2].
Statistical variability in language is pervasive and often persists through language
learning from one generation to the next [45]. Many researchers have assumed that the
cognitive system for language uses probability-matching decision rules [47,48]. However,
tendencies toward regularization of observed frequencies have been found in the area of
phonotactics [58, 59], and in some experiments involving learning of artiﬁcial languages
[35,36]. It has been argued that people discount ambiguous evidence in the acquisition of
morphology and syntax [60,61]. Ambiguity and vacillation may be cognitively costly for
linguistic processing. Categorical processing is argued to support fast, accurate encoding
and decoding, as well as the ability to create new words and sentences by recombining
basic elements [7].
Our results reconcile these disparate threads in the literature by developing a formal
apparatus for analyzing regularization as the categorization of experienced frequencies.
We then suggest that the cognitive processing of frequencies in language is moderately
categorical. The regime in which we observe grassroots changes has φ ≈60◦. As shown in
Figure 4, this is a level of categoriality that deviates only moderately from a probability-
matching decision rule. Although this moderate nonlinearity is suﬃcient to completely


## Page 24


24
change the prospects for an innovation to succeed, it is probably too weak to be detected
in a typical psycholinguistics experiment. Very large scale data collection over the entire
range of input probabilities would also be needed to assess the heterogeneity in individual
biases that also plays a key role in our model. In short, the statistical power needed to
rigorously compare a probability-matching (or neutral evolution) model with the regime
for complete cascades in the nearby scenario is much higher than has been available in
many classic experimental studies.
Why isn’t language processing strongly categorical? A probability-matching decision
rule can be optimal at the group level when coordinated actions are needed to divide up
resources [45]. Language presents a related case, because coordinated actions are needed
for a group to maintain a mutually intelligible language, which beneﬁts the group as a
whole by permitting knowledge to be transmitted from any person to any other. In the
nearby scenario, a completely categorical decision rule jeopardizes mutual intelligibility.
For 65◦⪅φ ≤90◦, arbitrary innovations dominate the system but do not go to comple-
tion. This outcome means that the social group has split into subgroups with distinct
norms. In contrast, the regime 55◦⪅φ ⪅65◦yields a greater likelihood that mutual in-
telligibility will be maintained through periods of change. Assuming that the distribution
of biases in the nearby scenario is empirically well-founded, language processing can be
understood as striking a balance between fast, accurate processing and the maintenance
of a shared linguistic code.
In research on opinion dynamics, an early and prominent hypothesis held that a small
number of individuals with high degree in a social network had disproportionate impor-
tance in triggering global cascades. That is, hubs in the network were thought to have
special importance as so-called inﬂuentials [23]. Some previous models of language change
achieve realistic cascade rates by assuming that people weight positively the input from
highly-connected people, who are also assumed to be high-status [3, 4]. In the extreme,
these assumptions lead to the conjecture that broadcast media should be a major factor
in language change, since the media transmit the linguistic patterns of political leaders
and celebrities to such large numbers of people. This conjecture is not well supported.
For example, establishing any eﬀect whatsoever of television on local dialects has been
an elusive goal, and only recently has such an eﬀect been found. In a detailed ﬁeld study
of Glaswegian English, some TV watchers were found to be inﬂuenced by the East End
dialect of London, but only if they had personal ties to the East End or felt strong psy-
chological engagement with characters in a popular TV soap drama that is set there [62].
In our model of egalitarian changes (the nearby scenario), informational cascades
occur without any positive weighting of input from highly connected individuals. These
individuals do play an important role, in that successful innovations succeed in part by
being adopted by one or more highly connected individuals, who then broadcast them
to many people. On the average, however, the highest degree individuals are somewhat
conservative compared to less connected individuals, because their linguistic patterns
are stabilized by the large number of incoming signals. Individuals who are far from the


## Page 25


25
innovator, and biased against the change, eventually adopt it with some probability simply
because a core of positively biased individuals near the innovator allows the change to
gain traction and in some cases eventually dominate the signal to the whole community.
Some previous work has argued that the concept of covert prestige (understood as an
implicit value system that countervails overt norms) is necessary to explain why high
status people often adopt stigmatized expressions originating in lower status circles [63].
However eﬀorts to substantiate this notion in terms of perceived lower-class attributes
such as toughness or friendliness have enjoyed mixed success [18]. Our model can explain
why high degree or high status people eventually adopt grassroots linguistic innovations
without recourse to a covert value system. Overall, our results support claims that social
solidarity, and not diﬀerences in status, is the dominant factor in the adoption of linguistic
innovations [53,55].
We saw that categorical decisions in the hubs scenario permit a well-connected group
of people to eﬀect a rapid and complete change that it favors. Less well-connected people
may be initially biased against the change, but are swept along. This scenario does not
appear to be relevant for linguistic changes. Is the model appropriate for some other
type of change in social norms or collective opinions? A categorical decision function
maximizes an individual’s statistical expectations [32] in the case of perfect knowledge.
This low-temperature decision rule is normally used in economic models [32], a reﬂex of
economists’ assumption that individuals have complete information and make independent
and rational decisions to maximize their gains. A recent example of a shift in public
opinion in the economic domain was the 1999 repeal of Glass-Steagall Act provisions that
separated investment banking from commercial banking. Our model shows how a well-
connected network of investment bankers who were biased in favor of opportunities for
investment banking could cause this change to be widely accepted (even if other people
held the opposite bias). More generally, a categorical decision rule is adaptive if the utility
of the competing options is well-deﬁned and generally known, or if the cost of waiting for
more information is great. In times of revolution or war, it may be clear that people who
delay or vacillate in their allegiances are less safe than people who take a side. Insofar
as political behavior reﬂects this perception of the risks, our model predicts people would
apply a highly categorical decision process, be strongly inﬂuenced by a slight advantage of
one option over the other, and that as a result public opinion in a time of crisis could be
eﬀectively controlled by a well-connected minority with shared biases. Insofar as political
behavior strikes a balance between taking a stand and waiting for more information, our
model suggests that grassroots political changes could take place without any deﬁnitive
evidence about their ultimate utility.


## Page 26


26
Acknowledgments
We thank L.A.N Amaral for time on his computing cluster. We are also grateful to P.J.
Lamberson and Daniel Lassiter for useful discussions about decision functions, and to
Simon Todd for incisive feedback on the mathematical exposition.
We are also grateful for ﬁnancial support from JSMF Grant No. 21002061 and John
Templeton Foundation Award No. 36617 . The opinions expressed in this publication
are those of the authors and do not necessarily reﬂect the views of the John Templeton
Foundation.
References
1. Newmeyer FJ (1992) Iconicity and generative grammar. Language 68: 756–796.
2. Saussure F (1916) In: C Bally C, A Sechehaye A, editors, Cours de linguistique
g´en´erale, Lausanne and Paris: Payot.
3. Nettle D (1999) Using social impact theory to simulate language change. Lingua
108: 95–117.
4. Fagyal Z, Escobar A, Swarup S, Gasser L, Lakkaraju K (2010) Centers and periph-
eries: network roles in language change. Lingua 120: 2061–2079.
5. Ke J, Gong T, Wang WSY (2008) Language change and social networks. Comm
Comput Phys 3: 935–949.
6. Niyogi P (2006) The Computational Nature of Language Learning and Evolution.
Cambridge, MA: The MIT Press.
7. de Boer B, Zuidema W (2010) Multi-agent simulations of the evolution of combi-
natorial phonology. Adapt Behav 18: 141–154.
8. Lacerda F (2003) Phonology: An emergent consequence of memory constraints and
sensory input. Reading and Writing: An Interdisciplinary Journal 16: 41-59.
9. Caldwell CA, Smith K (2012) Cultural evolution and perpetuation of arbitrary
communicative conventions in experimental microsocieties.
PLoS ONE DOI:
10.1371/journal.pone.0043807.
10. MacWhinney B (1978) The acquisition of morpho-phonology, volume 43. Mono-
graphs of the Society for Research in Child Development.
11. Ellis NC (2002) Frequency eﬀects in language processing. Studies in second language
acquisition 24: 143-188.


## Page 27


27
12. Lieberman E, Michel JP, Jackson J, Tang T, Nowak MA (2007) Quantifying the
evolutionary dynamics of language. Nature 449: 713–716.
13. Altmann EG, Pierrehumbert JB, Motter AE (2011) Niche as a determinant of word
fate in on-line groups. PLoS ONE DOI: 10.1371/journal.pone.0019009.
14. Bybee J (1984) Morphology: A Study of the Relation between Meaning and Form.
Amsterdam/Philadelphia: John Benjamins.
15. Lenaerts T, Jansen B, Tuyls K, De Vylder B (2005) The evolutionary language
game, an orthogonal approach. J Theor Biol 235: 566–582.
16. Castellano C, Fortunato S, Loreto V (2009) Statistical physics of social dynamics.
Rev Mod Phys 81: 591–646.
17. Piantadosi ST, Tily H, Gibson E (2011) Word lengths are optimized for eﬃcient
communication. Proc Natl Acad Sci USA 108: 3526-3529.
18. Labov W (2001) Principles of Linguistic Change. Volume II: Social Factors. Oxford:
Blackwell.
19. Bloomﬁeld L (1933) Language. New York: Holt.
20. Kirby J, Sonderegger M (2013) A model of population dynamics applied to language
change. In: Proceedings of the 35th Annual Conference of the Cognitive Society.
Cognitive Science Society, pp. 776-781.
21. Bikhchandani S, Hirschleifer D, Welch I (1998) Learning from the behavior of oth-
ers; conformity, fads, and informational cascades. J Econ Perspect 12: 151–170.
22. Watts DJ (2002) A simple model of global cascades on random networks. Proc
Natl Acad Sci USA 99: 5766–5771.
23. Watts DJ, Dodds PS (2007) Inﬂuentials, networks, and public opinion formation.
J Consum Res 34: 441–458.
24. Albert R, Barab´asi AL (2002) Statistical mechanics of complex networks. Rev Mod
Phys 74: 47–97.
25. Kleinberg J (2007) Cascading behavior in networks: algorithmic and economic
issues. In: Nisan N, Roughgarden T, Tardos E, Vazirani V, editors, Algorithmic
Game Theory, Cambridge: Cambridge University Press. pp. 613–632.
26. Delre SA, Jager W, Janssen MA (2006) Diﬀusion dynamics in small-world networks
with heterogeneous consumers. Comput Math Organiz Theor 13: 185–202.


## Page 28


28
27. Baxter GJ, Blythe RA, Croft W, McKane AJ (2009) Modeling language change:
An evaluation of Trudgill’s theory of the emergence of New Zealand English. Lang
Var Change 21: 275–296.
28. Bourhis RY, Giles H (1977) The language of intergroup distinctiveness. In: Giles
H, editor, Language, Ethnicity & Intergroup Relations, London: Academic. pp.
119–135.
29. Dijksterhuis A, Bargh JA (2001) The perception-behavior expressway: Automatic
eﬀects of social perception on social behavior. Adv Exp Soc Psychol 33: 1-40.
30. Bush R, Mosteller F (1951) A mathematical model for simple learning. Psychol
Rev 58: 313-323.
31. Sutton RS, Barto AG (1998) Reinforcement Learning: An Introduction. Cambridge
MA: MIT Press.
32. Friedman D, Massaro DW (1998) Understanding variability in binary and contin-
uous choice. Psychon Bul Rev 5: 370-398.
33. Clark B (2004) A Stochastic Optimality Theory Approach to Syntactic Change.
Stanford, CA: Stanford University Ph.D Disseration.
34. Kroch A (2001) Syntactic change. In: Baltin M, Collins C, editors, The Handbook
of Contemporary Syntactic Theory, Oxford: Blackwell. pp. 699-729.
35. Culbertson J, Smolensky P, Legendre G (2012) Learning biases predict a word order
universal. Cognition 122: 306–329.
36. Hudson Kam CL, Newport EL (2005) Regularizing unpredictable variation: The
roles of adult and child learners in language variation and change. Lang Learn Dev
1: 151-195.
37. Schumacher RA, Pierrehumbert JB, LaShell P (2014) Reconciling inconsistency in
encoded morphological distinctions in an artiﬁcial language. In: Proceedings of
the 36th Annual Conference of the Cognitive Science Society. Cognitive Science
Society.
38. Chambers JK (2004) Patterns of variation including change.
In: Chambers J,
Trudgill P, Schilling-Estes N, editors, The Handbook of Language Variation and
Change, Malden MA: Blackwell. p. 349372.
39. Tagliamonte SA, D’Arcy A (2009) Peaks beyond phonology: Adolescence, incre-
mentation, and language change. Language 85: 58-108.


## Page 29


29
40. Falmagne JC (2002) Elements of psychophysical theory. Oxford: Oxford University
Press.
41. Bogacz R, Usher M, Zhang J, McClelland J (2007) Extending a biologically inspired
model of choice: multi-alternatives, nonlinearity and value-based multidimensional
choice. Philos T Roy Soc B 362: 1655-1670.
42. Clark EV (1990) On the pragmatics of contrast. J Child Lang 17: 417-431.
43. Davis MH, Gaskell MG (2009) A complementary systems account of word learning:
Neural and behavioral evidence. Phil Trans R Soc B 364: 3773-3800.
44. Baronchelli A, Gong T, Puglisi A, Loreto V (2010) Modeling the emergence of
universality in color naming patterns. Proc Natl Acad Sci USA 107: 2403-2407.
45. Labov W (1994) Principles of Linguistic Change. Volume I: Internal Factors. Ox-
ford: Blackwell.
46. Griﬃths TL, Kalish ML (2007) Language evolution by iterated learning with
bayesian agents. Cog Sci 31: 441–480.
47. Reali F, Griﬃths TL (2009) The evolution of frequency distributions: Relating
regularization to inductive biases through iterated learning. Cognition 111: 317–
328.
48. Luce PA, Pisoni DB (1998) Recognizing spoken words: The neighborhood activa-
tion model. Ear and Hearing 19: 1–36.
49. Wilensky U (1999) NetLogo: http://ccl.northwestern.edu/netlogo/. Evanston, IL:
Center for Connected Learning and Computer-Based Modeling, Northwestern Uni-
versity.
50. John OP, Srivastava S (1999) The big ﬁve trait taxonomy: History, measurement
and theoretical perspectives. In: Pervin L, John O, editors, Handbook of person-
ality: Theory and Research, New York: Guilford Press. pp. 102-138.
51. Wilson DS, Clark AB, Coleman K, Dearstyne T (1994) Shyness and boldness in
humans and other animals. Trends Ecol Evol 9: 442-446.
52. Wasserman S, Faust K (1994) Social Network Analysis: Methods and Applications.
Cambridge UK: Cambridge University Press.
53. Milroy J (1992) Social network and prestige arguments in sociolinguistics.
In:
Bolton K, Kwok H, editors, Sociolinguistics Today: International Perspectives,
London, New York: Routledge. pp. 146-162.


## Page 30


30
54. Labov W (1972) Language in the Inner City: Studies in Black English Vernacular.
Philadelphia: University of Pennsylvania Press.
55. Eckert P (1989) Jocks and Burnouts: Social Categories and Identity in the High
School. New York: Teachers College, Columbia University.
56. Mendoza-Denton N (2008) Home Girls. Oxford, UK and Cambridge, MA: Black-
well.
57. Croft W (2000) Explaining Language Change: an Evolutionary Approach. New
York: Longman.
58. Frisch SA (1997) Similarity and frequency in phonology. Evanston, IL: Northwest-
ern University.
59. Hudson Kam CL, Newport EL (2009) Getting it right by getting it wrong: When
learners change languages. Cognit Psychol 59: 30-66.
60. Kirby S, Cornish H, Smith K (2008) Cumulative cultural evolution in the labo-
ratory: An experimental approach to the origins of structure in human language.
Proc Natl Acad Sci USA 105: 10681–10686.
61. Pearl L, Weinberg A (2007) Input ﬁltering in syntactic acquisition: Answers from
language change modeling. Lang Learn Dev 3: 43–72.
62. Stuart-Smith J, Pryce G, Timmins C, Gunter B (2013) Television can be a factor
in language change: Evidence from an urban dialect. Language 89: 501-536.
63. Trudgill P (1972) Sex, covert prestige and linguistic change in the urban British
English of Norwich. Language in Society 1: 179–195.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
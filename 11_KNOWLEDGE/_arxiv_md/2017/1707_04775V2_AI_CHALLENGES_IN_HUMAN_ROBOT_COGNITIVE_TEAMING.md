---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1707.04775v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1707.04775v2_AI_Challenges_in_Human-Robot_Cognitive_Teaming

> Source: 1707.04775v2_AI_Challenges_in_Human-Robot_Cognitive_Teaming.pdf

> Pages: 10

---


## Page 1


1
AI Challenges in Human-Robot Cognitive Teaming
Tathagata Chakraborti1, Subbarao Kambhampati1, Matthias Scheutz2, Yu Zhang1
1 Department of Computer Science, Arizona State University, Tempe, AZ 85281 USA
{ tchakra2, rao, yzhan442 } @ asu.edu
2 Department of Computer Science, Tufts University, Medford, MA 02155 USA
matthias.scheutz@tufts.edu
Abstract—Among the many anticipated roles for robots in the
future is that of being a human teammate. Aside from all the
technological hurdles that have to be overcome with respect to
hardware and control to make robots ﬁt to work with humans,
the added complication here is that humans have many conscious
and subconscious expectations of their teammates – indeed, we
argue that teaming is mostly a cognitive rather than physical
coordination activity. This introduces new challenges for the AI
and robotics community and requires fundamental changes to
the traditional approach to the design of autonomy. With this
in mind, we propose an update to the classical view of the
intelligent agent architecture, highlighting the requirements for
mental modeling of the human in the deliberative process of the
autonomous agent. In this article, we outline brieﬂy the recent
efforts of ours, and others in the community, towards developing
cognitive teammates along these guidelines.
I. INTRODUCTION
An increasing number of applications demand that humans
and robots work together. Although a few of these applications
can be handled through “teleoperation”, technologies that act
in concert with the humans in a teaming relationship with
increasing levels of autonomy are often desirable if not re-
quired. Even with a sufﬁciently robust human-robot interface,
robots will still need to exhibit characteristics common in
human-human teams in order to be good team players. This
includes the ability to recognize the intentions of the human
teammates, and to interact in a way that is comprehensible
and relevant to them - autonomous robots need to understand
and adapt to human behavior in an efﬁcient manner, much like
humans adapt to the behavior of other humans. Humans are
often able to produce such teaming behavior proactively due
to their ability (developed through centuries of evolution of a
variety of implicit or explicit visual, auditory and contextual
cues) to quickly (1) recognize teaming context in terms of the
current status of the team task and states of the teammates,
(2) anticipate next team behavior under the current context to
decide individual subgoals to be achieved for the team, and
(3) take proper actions to support the advancement of those
subgoals with the consideration of the other teammates.
The three steps above form a tightly coupled integrated loop
during the coordination process, which is constantly evolving
during teaming experience. Critically, humans will likely ex-
pect all of the above capabilities from a robotic teammate,
as otherwise team dynamics will suffer. As such, the chal-
lenge in human-robot teaming is primarily cognitive, rather
than physical. Cognitive teaming allows the robots to adapt
more proactively to the many conscious and subconscious
expectations of their human teammates. At the same time,
improper design of such robot autonomy could increase the
human’s cognitive load, leading to the loss of teaming situation
awareness, misaligned coordination, poorly calibrated trust,
and ultimately slow decision making, deteriorated teaming
performance, and even safety risks to the humans. As designers
of robotic control architectures, we thus have to ﬁrst isolate the
necessary functional capabilities that are common to realizing
such autonomy for teaming robots. The aim of the article is
to do just that and thus provide a framework that can serve as
the basis for the development of cognitive robotic teammates.
II. RELATED WORK
In human-human teams, it is well understood that ev-
ery team member maintains a cognitive model of the other
teammates they interact with [22]. These models not only
captures their physical states, but also mental states such as the
teammate intentions and preferences, which can signiﬁcantly
inﬂuence how an agent interacts with the other agents in
the team. Although such modeling has been identiﬁed as an
important characteristic of effective teaming [21], [23], [37],
it is less clear how it is maintained at the individual level.
Furthermore, the relative importance of different aspects of
such models cannot be easily isolated in experiments with hu-
man teammates, but must be separately considered for robots
since they often require very different modeling technologies.
Such forms of modeling allows the robots to understand
their human partners, and in turn use this knowledge to plan
their coordination to improve teaming experience. However,
although there exists work that has investigated the various
aspects of this modeling [29], [75], [86], a systematic summary
of the important challenges is still missing.
Next, we provide a review of the related work in terms of
agent types (Figure 1) that can be used to implement robotic
teammates, following the categorization in [82]. The ﬁrst two
types correspond to classical agent architectures in robotics
and artiﬁcial intelligence. We list them to facilitate the com-
parison of earlier teaming agents and cognitive teaming agents.
We show that all of them fall within a spectrum of agents that
differ based on the extent to which the agent interaction with
the external world and other agents is modeled.
A. Behavior-based agent
Behavior-based agents [8] have been an important design
paradigm for embodied agents (especially robots), in which
arXiv:1707.04775v2  [cs.AI]  13 Aug 2017


## Page 2


2
Fig. 1. An categorical view of different types of agents. Each type is deeper than the previous types in terms of modeling complexity (from left to right).
complex behaviors result from a collection of basic behav-
iors interacting with each other. These basic behaviors often
operate in parallel via cooperative or competitive arbitration
schemes [70]. Behavior-based agents have been applied to
various tasks such as formation control [4], [5], box pushing
[58], [34], navigation [59], and surveillance [83]. One issue
with behavior-based agent is that the interactions between
basic behaviors often have to be provided manually. This
can quickly become impractical when complex interactions
are desired. Furthermore, since this type of agent does not
maintain a model of the world, it cannot reason about its
dynamics and hence is often purely reactive.
B. Goal-based agent
In contrast to behavior-based agents, a goal-based agent
maintains a model of the world (Fig. 2) and how its actions can
change the state of the world. As a result, it can predict how the
world will respond before it executes any action. The earliest
agent of this type is Shakey [56]. The model that is maintained
is often speciﬁed at a factored level using planning languages,
such as STRIPS [30], PDDL [31] or its probabilistic extensions
[67], or at the atomic level using MDP speciﬁcation [62], [29].
A goal-based agent can also maintain its own epistemic state
[32], such as beliefs and desires [64], [33]. Goal-based agents
typically assume that the given model is complete, which may
not be realistic in open world domains [76].
Both behavior and goal based agent can handle multi-agent
coordination [83], [59], [4], [57], [38]. However, it is often
assumed that the team is given a speciﬁc goal, and the team
members either are provided information about each other a
priori, or can explicitly exchange such information. As a result,
agents can readily maintain a model of the others in teaming.
While this assumption may be true for robots teaming with
robots, we would deﬁnitely not observe such convenience in
human-robot teams (e.g., requiring humans to provide the in-
formation constantly can signiﬁcantly increase their cognitive
load); furthermore, the goal is often spontaneous rather than
given. As a result, a robotic teammate that is solely behavior
or goal based can only handle speciﬁc tasks and will rely on
human inputs for task assignments.
C. Proactive agent
A proactive agent, on the other hand, is supposed to
maintain a model of the others through both observations and
communication (if available and necessary). This model is
not only about the others’ physical state (e.g., location), but
also mental state which includes their goals [77], capabilities
[85] (which include the consideration of physical capabilities),
preferences [54], and knowledge [6].
Given that none of these are directly available, they must
be inferred [63] or learned [85], [1], [9] from observations.
As a result, the model of the other agents is often subject to a
high-level of incompleteness and uncertainty. This is especially
true when human teammates are involved. Nevertheless, even
such an approximate model of other agents can be important
for efﬁcient teaming when used properly. For example, it can
be used by the agents to plan for coordination to exploit
opportunities to help the humans in a proactive way [11], [29]
while avoiding conﬂicts [18], [17].
In addition to using the model of the others to plan for
coordination, a proactive agent can also act proactively to
change the others’ modeling of itself when necessary [6]. For
example, a robot can explicitly convey its intention through
natural languages [79] or gestures [61] to let the human
understand its intention to help or request for help.
D. Social agent
A deeper level of modeling is not only about the other
agents, but also the other agents’ modeling of the agent itself
[86]. This includes, for example, the others’ expectation and
trust of the agent itself. Such modeling allows the robot, for
example, to infer the human expectation of its own behavior
and in turn choose behaviors that are consistent with this
expectation. Expectation and trust, in particular, represent the
social aspects of agent interactions since they are particularly
relevant when agents form groups or teams together. An agent
that behaves socially [47], [27], [86] allows the other agents to
better understand and anticipate its behavior, thus contributing
to the maintenance of teaming situation awareness [21]. In
human-human teams, social behaviors contribute signiﬁcantly
to ﬂuent teaming [69].
Similar to a proactive agent, a social agent often has to learn
and maintain a model about the various social aspects from
observations [86]. In addition to using these social aspects
to guide its behavior generation, a social agent can also act
to change these aspects (via informing the others about the
discrepancies in their modeling about itself and updating the


## Page 3


3
Fig. 2.
Traditional view of the goal-based intelligent agent architecture
[66] that describes how the agent models the world, senses changes in the
environment, plans to achieve goals and acts to execute the plans.
same in its model of the others). For example, a robot can
maintain its trust from the human by constructing excuses
when a task cannot be achieved [35] to provide explanations
to the human from the robot’s own perspective, while taking
into account the human’s understanding of itself.
Although various types of agents can be used to realize a
robotic teammate, based on the above discussion, the chal-
lenges that are introduced by the humans in the loop lie in
particular in the implementation of a proactive and social
agents. A common characteristics among these two types of
agents is that both require the notion of mental modeling of
the other teammates, which cannot be directly observed and
must be inferred cognitively. This is the key requirement of a
cognitive teaming capability.
III. TRANSITIONING TO A COGNITIVE TEAMING AGENT
In this section, we characterize how each step in the “Sense-
Model-Plan-Act” (SMPA) cycle of the classical goal-based
agent view in [66] (shown in Figure 2) has to be updated
to facilitate the mental modeling of the human in the loop
in order to enable a truly cognitive teaming agent (shown in
Figure 3). Speciﬁcally, we introduce the Human Model (HuM)
and the Human Mental Model (HuMM) as key components in
the agent’s deliberative process. Changes to Model in Figure
3 is a direct result of the requirement of human mental
modeling. Coarsely speaking, changes to Sense contribute to
the recognition of teaming context, changes to Plan contribute
to the anticipation of team behavior and Act, and changes
to Act contribute to the determination of proper actions at
both the action and motion levels. In practice, these four
functionalities are tightly integrated in the behavior loop.
Sense – The agent can no longer sense passively to check
that the preconditions of an action are satisﬁed, or after it
applies an action to the world to conﬁrm that it is updated
accordingly (“what the world is like now” in Figure 2).
In teaming scenarios, the agent needs to proactively make
complex sensing plans that interact closely with other func-
tionalities – Model and Plan – to maintain the correct mental
Fig. 3.
An updated view of the architecture of a cognitive teaming agent
acknowledging the need to account for the human’s mental state by means of
what we refer to as Human Mental Modeling or HuMM.
state (such as intentions, knowledge and beliefs) of its human
teammates in order to infer their needs. For example, how
the robot should behave is dependent on how much and what
type of help the human requires, which in turn depends on
the observations about the human teammates such as their
behavior and workload. Furthermore, the inference about the
human mental state should be informed by the human model
that the robot maintains about the human’s capabilities and
preferences. Note that directly asking humans (i.e. explicit
communication) is a speciﬁc form of sensing.
Model – Correspondingly, the state, i.e. “what the world is
like now”, needs to include not only environmental states, but
also mental states of the team members which may not only
include cognitive and affective states such as the human’s
task-relevant beliefs, goals, preferences, and intentions, but
also, more generally, emotions, workload, expectations, trust
and etc. “What my actions do to the world” then needs to
include the effects of the robot’s actions on the team member’s
mental state, in addition to the effects on their physiological
and physical states and the observable environment; “How
the world evolves” now also requires rules that govern the
evolution of agent mental states based on their interactions
with the world (including information exchange through com-
munication); “What it will be like” will thus be an updated
state representation that not only captures the world state,
agent physiological and physical state changes based on their
actions and current states, but also those mental state changes
caused by the agent itself and other team members.
Plan – “What action I should do” now involves more com-
plex decision-making that must again also consider human
mental state. Furthermore, since the robot actions now can
inﬂuence not only the state of the world but also the mental
state of the humans, the planning process must also consider
how the actions may inﬂuence their mental state and even
how to affect/manipulate such mental state. For example, in
teaming scenarios, it is important to maintain a shared mental
state between the teammates. This may require the robots to
generate behavior that is expected or predictable to the human


## Page 4


4
teammates such that they would be able to understand the
robot’s intention. This can, in fact, be considered an implicit
form of signaling or communication. On the other hand, a
shared mental state does not necessarily mean that every
piece of information needs to be synchronized. Given the
limitation on human cognitive load, sharing only necessary
information is more practical between different teammates
working on different parts of the team task. A properly
maintained shared mental state between the teammates can
contribute signiﬁcantly to the efﬁciency of teaming since it
can reduce the necessity of explicit communication.
Act – In addition to physical actions, we now also have
communication actions that can change the mental state of
the humans by changing their beliefs, intents, etc. Actions to
affect the human’s mental state do not have to be linguistic
(direct); stigmergic actions to instrument the environment can
also inform the humans such that their mental states can be
changed. Given that an action plan is eventually realized via
the activation of effectors by providing motor commands, Act
must be tightly integrated with Plan. While Plan generates
the sequence of actions to be realized, motor commands can
create different motion trajectories to implement each action
and can in turn impact how the plan would be interpreted
since different realizations can exert different inﬂuences on
the human’s mental states based on the context.
An Exemplary Human-Robot Teaming Scenario
To better illustrate how mental modeling of teammates can
contribute to the different capabilities needed for cognitive
teaming agents, we will now consider scenarios from a human-
robot team performing an USAR task where each subteam i
consists of one human Hi and one robot Ri.
For subteam 1: Based on the ﬂoor plan of the building
in its search area, R1 realizes that the team needs to use an
entrance to a hallway to start the exploration. R1 notices that
a heavy object blocks the entrance to the hallway. Based on its
capability model of H1 (i.e., what H1 can and cannot lift) and
H1’s goal, R1 decides to interrupt its current activity and move
the block out of the way. H1 and R1 then continue exploring
different parts of the area independently when H1 discovered
a victim and informs R1. R1 understands that H1 needs to
get a medical kit to be able conduct triage on this victim as
soon as possible but knows that H1 does not know where a
medical kit is located. Since R1 has a medical kit already,
but cannot deliver it due to other commitments, it places its
medical kit along the hallway that it expects H1 to go through,
and informs H1 of the presence of the kit.
For subteam 2: Based on the ﬂoor plan of the building in
its search area, R2 ﬁnds that all the entrances are automatic
doors that are controlled from the inside. Since the connection
cannot be established due to power lost, the team needs to
break a door open ﬁrst. R2 infers that H2 is about to break a
door open based on the teaming context and its observations.
Since it knows that breaking the door open may cause a board
to fall on H2, R2 moves to catch the board preventatively.
Once H2 and R2 are inside, however, H2 is uncertain about
the structural integrity and has no information on which parts
may easily collapse. R2 has access to the building structure
information and proposes a plan to split the search in a way
that minimizes human risk.
For both subteams: As both teams are searching their areas,
they receive information about a third area to be explored.
Since neither H1 nor H2 are ﬁnished with their current search
task, they assume that the other will take care of the third
area. Since R1 understands H1 and H2’s current situation,
and expects itself to be done with its part of the task soon,
R1 decides to work on the third area since it does not expect
H1 to need any help. R1 informs H1. H1 is OK with it and
informs H2 that team 1 is working on the third area. When
R1 arrives at the third area, it notices new situations which
require certain equipment from team 2. R1 communicates with
R2 about the availability of the missing items. R2 quickly
predicts equipment needs and anticipates that those items are
not needed for a while. After getting the OK from H2 to lend
the equipment to R1, R2 drives off to meet R1 half-way, hand
over the equipment, and R1 returns to the third area with the
newly acquired equipment. H1 was not informed during this
process since R1 understands that H1 has a high workload.
Once the equipment is no longer needed, R1 meets up with
R2 again, returning the equipment in time for use by H2.
Based on the above scenario, we can see that the mental
modeling of the others on a cognitive robotic teammate is
critical to the ﬂuent operation of the team For example, R1
needs to understand the capabilities of H1 (i.e., what H1 can
and cannot lift); both R1 and R2 need to be able to infer about
the intention of the human teammates. The modeling may
also include the human’s knowledge, belief, mental workload,
trust, etc. This human mental modeling for cognitive teaming
between humans and robots connect with the three capabilities
we introduced in Section I as critical to the functioning of
human-human teams and form the basis of the updated agent
architecture in Fig. 3 as follows -
C1. Recognizing teaming context to identify the status
of the team task and states of the teammates: For example,
based on the ﬂoor plan of the building, R1 realizes that
the team needs to use an entrance to a hallway to start the
exploration. R2 ﬁnds that all the entrances are automatic doors
that are controlled from the inside. Consequently, it infers that
the team needs to break a door open ﬁrst. This inference
process takes into account the modeling of the teammate’s
state (e.g., the intention to enter the building).
C2. Anticipate team behavior under the current context:
For example, given that a heavy object blocks the entrance to
the hallway, R1 infers that the human will be ﬁnding a way
to clear the object. R2 infers that H2 is going to break a door
open based on the teaming context and its observations. This
prediction takes into account of the modeling of the human’s
capabilities and knowledge about the teaming context.
C3. Take proper actions to advance the team goal
while taking into account the teammates: For example, after
anticipating the human’s plan, the robots should proactively
help the humans (e.g., R1 helps H1 move the block away and


## Page 5


5
Fig. 4.
Figure [73] illustrating the expanding scope of the “human-aware”
decision making process of an autonomous agent to account for the human
model (HuM) and the human mental model (HuMM).
R2 catches the board preventively that can potentially hurt the
human), while taking the account the modeling of the human’s
capabilities, mental workload, and expectation.
Remark: C3 above not only includes actions that con-
tribute to the team goal, but also actions for maintaining
teaming situation awareness (e.g., making explanations). As
such, C3 feeds back to C1 and the three capabilities in turn
form a loop that should be constantly exercised to achieve
ﬂuent teaming. Furthermore, although we have been focusing
on implicit communication (e.g., through observing behaviors)
to emphasize the importance of mental modeling, explicit com-
munication (e.g., using natural language) is also an important
part of the loop. Another note is that since both implicit and
explicit communication can update the modeling of the other
teammates’ mental states as discussed, they are anticipated to
evolve the teaming process in the long term.
IV. CHALLENGES
The capabilities reﬂected in the updated agent architecture
present several challenges for the design of cognitive robotic
teammates – at the core of these issues is the need for an
autonomous agent to consider not only its own model but
also the human teammate’s mental model in its deliberative
process. In the following discussion, we will outline a few of
our recent works in this direction, outline processes by which
the agent can deal with such models, and end with a discussion
on our work on learning and evaluating these models.
A. Human Aware Planning
Most traditional approaches to planning focus on one-shot
planning in closed worlds given complete domain models.
While even this problem is quite challenging, and signiﬁcant
Fig. 5.
Figure [73] illustrating explanation generation [14] via the model
reconciliation process, and explicable plan generation [87] by sacriﬁcing
optimality in the robot’s own model.
strides have been made in taming its combinatorics, planners
for robots in human-robot teaming scenarios require the ability
to be human-aware. We postulate then a departure from
traditional notions of automated planning to account for with
humans – many of the challenges that arise from it are
summarized in our work [14] under the umbrella of “Multi-
Model Planning”. The term alludes to the fact that a cognitive
agent, in course of its deliberative process, must now consider
not only the model M that it has on its own but also the
model HuM of the human in the loop, including the (often
misaligned) mental model HuMM of the same task that the
human might have. This setting is illustrated in Figure 4. Here,
by the term “model” of an robot, we include its action or
domain model as well as its state information or beliefs and
its goals or intentions. The human model allows the robot to
account for the human’s participation in the consumption of
a plan, while the human mental model enables the robot to
anticipate how the the plan will be perceived by the human as
well as interactions that arise thereof.
Human-Robot Teaming / Cohabitation: Incorporation of
the human model HuM in the planning process allows the
robot to take into consideration possible human participation
in the task and thus identify its appropriate role in it. This
can relevant both when the robot is explicitly teaming [77],
[52], [84], [78] with the human, or when it is just sharing
or cohabiting [11], [17], [12], [16] the same workspace
withouts shared goals and commitments. We have explored
the typical roles of the robot in each of these scenarios –
e.g. in planning for serendipity [11] and in planning with
resource conﬂicts [17] we looked at how a robot can plan
for passive coordination with minimal prior communication,
while in [52], [84] we explored the effects of proactive support
on the human teammate. Indeed, much of existing literature


## Page 6


6
Fig. 6. Figure [80] showing a schematic view of different classes of incomplete models and relationships between them in the spectrum of incompleteness.
on human-aware planning [2], [3], [20], [41], [81], [19], [11],
[11], [12] has focused on this setting; we will now explore
additional challenges to the human-aware planning problem
in the context of the human mental model HuMM.
Explicable Task Planning: One immediate effect of model
differences between the robot and the human is that a robot
even when optimal on its own can be suboptimal, and hence
inexplicable, in the model of the human. This situation is
illustrated in Figure 5. When faced with such a situation the
robot can choose to produce plans π that are likely to be
more comprehensible to the human by being closer to the
human expectations πHuMM. This is referred to as explicable
planning – here the robot thus sacriﬁces optimality in its own
model in order to produce more human-aware plans. There
exists some recent work on motion planning while considering
the human expectation both while computing trajectories [27],
[25], [26]. In recent work [87], [43], [86] we have explored
how this can be achieved in the context of task both when the
human model is perfectly known, or when it has to be learned
in the course of interactions. The latter work introduces a
plan explicability measure [87] learned approximately from
labeled plan traces as a proxy to the human model. This
captures the human’s expectation of the robot, which can be
used by the robot to proactively choose, or directly incorporate
into the planning process to generate, plans that are more
comprehensible without signiﬁcantly affecting its quality.
Explanation Generation: Such plans, of course, may not
always be desirable – e.g. if the plan expected by the human
is too costly (or even unsafe or infeasible) in the robot’s
model. Then the robot can choose to be optimal (πM) in itself,
and explain [14], [74] its decisions to the human in terms of
the model differences. This process of model reconciliation
ensures that the human and the planner remain on the same
page in course of prolonged interactions. At the end of the
model reconciliation process, the optimal plan in the agent’s
model become optimal in the update human model
\
HuMM
as well, as shown in Figure 5. The ability to explain itself is a
crucial part of the design of a cognitive teammate, especially
for developing trust and transparency among teammates. We
argue [14] that such explanations cannot be a soliloquy – i.e.
the planner must base its explanations on the human mental
model. This is usually an implicit assumption in the explana-
tion generation process; e.g. imagine a teacher explaining to
a student - this is done in a manner so that the student can
make sense of the information in their model.
Human-Aware Planning Revisited: Sometimes the process
of explanation, i.e. the cost of communication overhead, might
be too high. However, at the same time, for reasons we
explained above, there might not be any explicable plans
available either. An ideal middle ground then is to strike a
balance between the explicable planning and explanations.
We attempt to do this by employing model-space search [73]
during the planning process. From the perspective of design
of autonomy, this has two important implications - (1) as
mentioned before, an agent can now not only explain but also
plan in the multi-model setting with the trade-off between
compromise on its optimality and possible explanations in
mind; and (2) the argumentation process is known [51] to be
a crucial function of the reasoning capabilities of humans, and
now by extension of autonomous agents as well, as a result of
algorithms that incorporate the explanation generation process
into the decision making process of an agent itself.
B. Learning Human (Mental) Models
Of course, both the previous challenges were built on the
premise that the human (mental) models are available or at
least learned so as to facilitate the decision making process
with these model in mind. Acquiring of such models, taken
for granted among human teammates through centuries of
evolution, is perhaps the hardest challenge to be overcome to
realize truly cognitive teaming. The difﬁculty of this problem
is exacerbated by the fact that much (speciﬁcally, HuMM)
of these models cannot be learned from observations directly
but only from continued interactions with the human.
However, while much of the work on planning has till now
focused on complete world models, most real-world scenarios,
especially when they involve humans, are open-ended in that
planning agents typically do not have sufﬁcient knowledge
about all task-relevant information (e.g., human models) at
planning time – in other words, the planning models would
be incomplete. Despite being incomplete, such models must
also support reasoning as well as be improvable from sensing,
i.e. learnable. Hence, an important challenge is to develop
representations of approximate and incomplete models that are


## Page 7


7
Fig. 7. Testbeds developed to study the dynamics of trust and teamwork between autonomous agents and their human teammates.
easy to learn (for human mental modeling) and can support
planning/decision-making (for anticipating human behavior).
Existing work on incomplete models (Figure 6) differ in
the information that is available for model learning, as well as
how planning is performed. Some of them start with complete
action models and annotate them with possible conditions to
support incompleteness [53], [88], [89]. Although these mod-
els support principled approaches for robust planning, they are
still quite difﬁcult to learn. On the other end of the spectrum,
are very shallow models [80] that assume no structured infor-
mation at all which are used mainly in short-term planning
support such as action recommendation. Partial models, that
are somewhere in between, having more structured information
while still being easy to learn [85] can prove to be powerful
support for goal recognition. However, planning under such
models is incomplete. In our work on explanation generation
[74] we demonstrated how annotated models such as above can
be used to deal with model uncertainty, while for explicable
planning [87], [43] we showed how CRF/Regression/LSTM-
based models can be used to learn human preferences in terms
of plan similarity metrics.
This is, however, only a start in this research direction.
Performing human-aware planning with incomplete models
remains an important challenge in human-aware planning,
especially given that we do not yet understand how these
different human models interact. For example, different human
models capture different aspects of the human (e.g., capabili-
ties [85], intentions [75] and emotions [68]) which are closely
inter-related, and it is not clear how they can be combined.
C. Communication and Evolution of Mental Models
All these processes are aimed at bringing the robot’s model
and the human expectation of it closer over continued interac-
tions. We have so far only discussed how a robot can maintain
the human mental models. However, in teaming, this modeling
is bi-directional. When robots do not have certain information,
the robot can plan to sense and communicate with the human.
In cases when the human is suspected to have insufﬁcient
information about the robot, the robot needs to proactively
communicate its model to the human. This communication
can be, for example, about the intention, plan, explanations
and excuses of behavior [35] for the robot; or explanations
that can not only make sense of the plan generation process
itself [40], [72], [44], but must also make sense from the
(robot’s understanding of the) human’s perspective [14]. This
is especially relevant in the case of human-robot teams, where
the human’s understanding of the robot may not be accurate.
Such explanations must not only be able to justify failure [36],
[39], [50], [28] but also the rationale behind a successful plan
in order for the human to be able to reason about the situation
and contrast among alternative hypotheses [14], [46], [45].
Further, explanations must be communicated at a level
understandable to the human [60], [65]. Communication can
thus involve different modalities such as visual projection,
natural languages, gesture signaling, and a mixture of them
[13]. This capability is important for the human and robot to
evolve their mental models to improve teaming in the long
term. Note that the models (i.e., the human actual model and
its representation on the robot) are not required to be aligned,
which is often only applicable for repetitive tasks [55]. Much
existing work on robots communicating with humans using
different modalities can be utilized [42], [79]. However, a more
critical challenge for the robot is to compute when, what, and
how to communicate for model adaptation - communicating
too much information can increase the cognitive load of the
human teammates while communicating too little can decrease
the teaming situation awareness. Existing literature on decision
support and human-in-the-loop planning [71], [48], [15] can


## Page 8


8
provide insightful clues to dealing with such challenges in
communication on information among teammates.
It must also be realized that many human-robot teaming
tasks are not only complex, but can also span multiple episodes
for an extended period of time. In such scenarios, the system’s
performance is dependent on how the teams perform in the
current task, as well as how they perform in future tasks.
A prerequisite to consider long-term teaming is to maintain
mental states of the agents (e.g., trust) that inﬂuence their
interactions, and analyze how these states dynamically affect
the teaming performance and how they evolve over time.
D. Evaluation / Microworlds
The design of human-machine systems is, of course, largely
incomplete unless tested and validated in the proper settings.
Although the existing teamwork literature [24] on human-
human and human-animal teams has identiﬁed characteristics
of effective teams – in terms of shared mental models [10],
[49], team situational awareness [37], and interaction [22] – it
is less clear how much of those lessons carry over to human-
robot teams. To this end, we have developed a suite of testbeds
or microworlds for generation and testing of hypothesis and
rapid prototyping of solutions. Figure 7 illustrate some of the
microworlds we have used so far – anticlockwise from the left,
this includes [1-2] a shared workspace [13] between humans
and semi-autonomous agents that supports communication
across various modalities such as speech, brainwaves (EEG)
and augmented reality (AR) [video: https://goo.gl/KdsEgr]; [4-
5] simulated Urban Search and Rescue scenarios [52], [84],
[73], [74] with internal semi-autonomous agents (humans and
robots) supervised by external human teammates [video: https:
//goo.gl/BKHnSZ]; and [3,6] simulated (such as autonomous
driving and collaborative assembly) domains for the study
of multi-model planning [87], [43], [84], [52] with humans
in the loop [video: https://goo.gl/UpEmzG]. The aim here
is to conduct human-human or Wizard of Oz studies [7] in
controlled settings and replicate desired behavior in the design
of cognitive teammates.
V. CONCLUSION
In this paper, we discussed the challenges in design of
autonomous robots that are cognizant of the cognitive aspects
of working with human teammates. We argued that tradi-
tional goal-based and behavior-based agent architectures are
insufﬁcient for building robotic teammates. Starting with the
traditional view of a goal-based agent, we expand it to include
a critical missing component: human mental modeling. We
discussed the various tasks that are involved when such models
are present, along with the challenges that need to be addressed
to achieve these tasks. We hope that this article can serve
as guidance for the development of robotic systems that can
enable more natural teaming with humans.
REFERENCES
[1] Pieter Abbeel and Andrew Y. Ng. Apprenticeship learning via inverse
reinforcement learning. In Proceedings of the Twenty-ﬁrst International
Conference on Machine Learning, ICML ’04, pages 1–, New York, NY,
USA, 2004. ACM.
[2] Rachid Alami, Aur´elie Clodic, Vincent Montreuil, Emrah Akin Sisbot,
and Raja Chatila. Toward Human-Aware Robot Task Planning. In AAAI
Spring Symposium: To Boldly Go Where No Human-Robot Team Has
Gone Before, 2006.
[3] Rachid Alami, Mamoun Gharbi, Benjamin Vadant, Rapha¨el Lallement,
and Adolfo Suarez. On human-aware task and motion planning abilities
for a teammate robot.
In Human-Robot Collaboration for Industrial
Manufacturing Workshop, RSS, 2014.
[4] R.C. Arkin. Motor Schema – Based Mobile Robot Navigation. Inter-
national Journal of Robotics Research, 8(4):92–112, Aug. 1989.
[5] T. Balch and R.C. Arkin.
Behavior-based formation control for
multirobot teams.
IEEE Transactions on Robotics and Automation,
14(6):926–939, Dec. 1998.
[6] Chitta Baral, Gregory Gelfond, Enrico Pontelli, and Tran Cao Son. An
action language for multi-agent domains: Foundations. under submission
to Artiﬁcial Intelligence, 2015.
[7] Cade Earl Bartlett. Communication between Teammates in Urban Search
and Rescue. Thesis, 2015.
[8] Rodney Brooks. Intelligence without representation. Artiﬁcial Intelli-
gence, 47:139–159, 1991.
[9] Benjamin Burchﬁel, Carlo Tomasi, and Ronald Parr. Distance minimiza-
tion for reward learning from scored trajectories. In National Conference
on Artiﬁcial Intelligence.
[10] J.A. Cannon-Bowers, E. Salas, and S. Converse. Shared mental models
in expert team decision making. Current issues in individual and group
decision making.
[11] Tathagata Chakraborti, Gordon Briggs, Kartik Talamadupula, Yu Zhang,
Matthias Scheutz, David Smith, and Subbarao Kambhampati. Planning
for serendipity. In IROS, 2015.
[12] Tathagata Chakraborti, Vivek Dondeti, Venkata Vamsikrishna Meduri,
and Subbarao Kambhampati.
A game theoretic approach to ad-hoc
coalition formation in human-robot societies.
In AAAI Workshop on
Multi-Agent Interaction without Prior Coordination (MIPC), 2016.
[13] Tathagata Chakraborti, Sarath Sreedharan, Anagha Kulkarni, and Sub-
barao Kambhampati.
Alternative Modes of Interaction in Proximal
Human-in-the-Loop Operation of Robots. CoRR, abs/1703.08930, 2017.
[14] Tathagata Chakraborti, Sarath Sreedharan, Yu Zhang, and Subbarao
Kambhampati.
Plan explanations as model reconciliation: Moving
beyond explanation as soliloquy. In IJCAI, 2017.
[15] Tathagata Chakraborti, Kartik Talamadupula, Kshitij P Fadnis, Murray
Campbell, and Subbarao Kambhampati.
UbuntuWorld 1.0 LTS-A
Platform for Automated Problem Solving & Troubleshooting in the
Ubuntu OS. In AAAI, 2017.
[16] Tathagata Chakraborti, Kartik Talamadupula, Yu Zhang, and Subbarao
Kambhampati. A formal framework for studying interaction in human-
robot societies.
In AAAI Workshop on Symbiotic Cognitive Systems
(SCS), 2016.
[17] Tathagata Chakraborti, Yu Zhang, David Smith, and Subbarao Kamb-
hampati. Planning with resource conﬂicts in human-robot cohabitation.
In AAMAS, 2016.
[18] M. Cirillo, L. Karlsson, and A. Safﬁotti. Human-aware task planning for
mobile robots. In Advanced Robotics, 2009. ICAR 2009. International
Conference on, pages 1–7, June 2009.
[19] Marcello Cirillo. Planning in inhabited environments: human-aware task
planning and activity recognition. PhD thesis, ¨Orebro university, 2010.
[20] Marcello Cirillo, Lars Karlsson, and Alessandro Safﬁotti. Human-aware
task planning: An application to mobile robots. ACM Trans. Intell. Syst.
Technol., 1(2):15:1–15:26, December 2010.
[21] N. J. Cooke.
Team cognition as interaction.
Current Directions in
Psychological Science, 2015.
[22] N. J. Cooke, J. C. Gorman, C. W. Myers, and J.L. Duran. Interactive
team cognition. Cognitive Science, 2013.
[23] N. J. Cooke and M. L. Hilton. Enhancing the effectiveness of team
science. National Academies Press, 2015.
[24] Nancy J Cooke, Jamie C Gorman, Christopher W Myers, and Jasmine L
Duran. Interactive team cognition. Cognitive science, 37(2):255–285,
2013.
[25] Anca Dragan, Shira Bauman, Jodi Forlizzi, and Siddhartha Srinivasa.
Effects of robot motion on human-robot collaboration. In Human-Robot
Interaction, March 2015.
[26] Anca Dragan, Rachel Holladay , and Siddhartha Srinivasa. Deceptive
robot motion: Synthesis, analysis and experiments. Autonomous Robots,
July 2015.
[27] Anca Dragan and Siddhartha Srinivasa. Generating legible motion. In
Proceedings of Robotics: Science and Systems, 2013.
[28] Thomas Eiter, Esra Erdem, Michael Fink, and J´an Senko.
Updating
action domain descriptions. Artiﬁcial intelligence, 2010.


## Page 9


9
[29] Alan Fern, Sriraam Natarajan, Kshitij Judah, and Prasad Tadepalli. A
decision-theoretic model of assistance. J. Artif. Int. Res., 50(1):71–104,
May 2014.
[30] Richard E. Fikes and Nils J. Nilsson. Strips: A new approach to the
application of theorem proving to problem solving. In Proceedings of the
2Nd International Joint Conference on Artiﬁcial Intelligence, IJCAI’71,
pages 608–620, San Francisco, CA, USA, 1971. Morgan Kaufmann
Publishers Inc.
[31] M. Fox and D. Long. PDDL2. 1: An extension to PDDL for expressing
temporal planning domains. Journal of Artiﬁcial Intelligence Research,
20(2003):61–124, 2003.
[32] Andr Fuhrmann.
The Journal of Symbolic Logic, 57(4):1479–1481,
1992.
[33] Michael Georgeff, Barney Pell, Martha Pollack, Milind Tambe, and
Michael Wooldridge.
The Belief-Desire-Intention Model of Agency,
pages 1–10. Springer Berlin Heidelberg, Berlin, Heidelberg, 1999.
[34] B.P. Gerkey and M.J. Mataric. Sold!: Auction methods for multi-robot
coordination. IEEE Transactions on Robotics and Automation, Special
Issue on Multi-robot Systems, 18(5):758–768, 2001.
[35] Moritz G¨obelbecker, Thomas Keller, Patrick Eyerich, Michael Brenner,
and Bernhard Nebel. Coming up with good excuses: What to do when
no plan can be found. In ICAPS, pages 81–88, 2010.
[36] M. Goebelbecker, T. Keller, P. Eyerich, M. Brenner, and B. Nebel.
Coming up With Good Excuses: What to do When no Plan Can be
Found. 2010.
[37] J.C. Gorman, N.J. Cooke, and J.L. Winner. Measuring team situation
awareness in decentralized command and control environments.
Er-
gonomics, 49:1312–1325, 2006.
[38] Barbara J. Grosz and Sarit Kraus. Collaborative plans for complex group
action. Artif. Intell., 86(2):269–357, October 1996.
[39] Andreas Herzig, Viviane Menezes, Leliane Nunes de Barros, and Renata
Wassermann. On the revision of planning tasks. In Proceedings of the
Twenty-ﬁrst European Conference on Artiﬁcial Intelligence, ECAI, 2014.
[40] Subbarao Kambhampati. A classiﬁcation of plan modiﬁcation strategies
based on coverage and information requirements. In AAAI 1990 Spring
Symposium on Case Based Reasoning, 1990.
[41] Uwe Koeckemann, Federico Pecora, and Lars Karlsson. Grandpa hates
robots - interaction constraints for planning in inhabited environments.
In Proc. AAAI-2010, 2014.
[42] Thomas Kollar, Stefanie Tellex, Deb Roy, and Nick Roy.
Toward
understanding natural language directions. In International IEEE/ACM
Conference on Human-Robot Interaction, 2010.
[43] Anagha Kulkarni, Tathagata Chakraborti, Yantian Zha, Satya Gautam
Vadlamudi, Yu Zhang, and Subbarao Kambhampati. Explicable robot
planning as minimizing distance from expected behavior.
CoRR,
abs/1611.05497, 2016.
[44] Pat Langley. Explainable agency in human-robot interaction. In AAAI
Fall Symposium Series, 2016.
[45] Tania Lombrozo. The structure and function of explanations. Trends in
Cognitive Sciences, 10(10):464 – 470, 2006.
[46] Tania Lombrozo. Explanation and abductive inference. Oxford handbook
of thinking and reasoning, pages 260–276, 2012.
[47] Jim Mainprice, E Akin Sisbot, Thierry Sim´eon, and Rachid Alami. Plan-
ning safe and legible hand-over motions for human-robot interaction.
IARP workshop on technical challenges for dependable robots in human
environments, 2(6):7, 2010.
[48] Lydia Manikonda, Tathagata Chakraborti, Kartik Talamadupula, and
Subbarao Kambhampati. Herding the Crowd: Using Automated Planning
for Better Crowdsourced Planning.
Journal of Human Computation,
2017.
[49] J. E. Mathieu, T. S. Heffner, G. F. Goodwin, E. Salas, and J. A. Cannon-
Bowers. The inﬂuence of shared mental models on team process and
performance. Journal of Applied Psychology, 2000.
[50] M Viviane Menezes, Leliane N de Barros, and Silvio do Lago Pereira.
Planning task validation. In Proc. of the ICAPS Workshop on Scheduling
and Planning Applications, pages 48–55, 2012.
[51] Hugo Mercier and Dan Sperber. Why Do Humans Reason? Arguments
for an Argumentative Theory. Behavioral and Brain Sciences, 2010.
[52] Vignesh Narayanan, Yu Zhang, Nathaniel Mendoza, and Subbarao
Kambhampati.
Automated planning for peer-to-peer teaming and its
evaluation in remote human-robot interaction. In HRI, 2015.
[53] Tuan Nguyen, Subbarao Kambhampati, and Sarath Sreedharan. Robust
planning with incomplete domain models. Artiﬁcial Intelligence, 2017.
[54] Tuan Anh Nguyen, Minh Do, Alfonso Emilio Gerevini, Ivan Serina,
Biplav Srivastava, and Subbarao Kambhampati. Generating diverse plans
to handle unknown and partially known user preferences.
Artiﬁcial
Intelligence, 190(0):1 – 31, 2012.
[55] Stefanos Nikolaidis and Julie Shah. Human-robot cross-training: Com-
putational formulation, modeling and evaluation of a human team
training strategy. In Proceedings of the 8th ACM/IEEE International
Conference on Human-robot Interaction, HRI ’13, pages 33–40, Piscat-
away, NJ, USA, 2013. IEEE Press.
[56] Nils J. Nilsson. Shakey the robot. Technical report.
[57] Raz Nissim, Ronen I. Brafman, and Carmel Domshlak. A general, fully
distributed multi-agent planning algorithm.
In AAMAS, pages 1323–
1330, Richland, SC, 2010. International Foundation for Autonomous
Agents and Multiagent Systems.
[58] L.E. Parker. ALLIANCE: an architecture for fault tolerant multirobot co-
operation. IEEE Transactions on Robotics and Automation, 14(2):220–
240, 1998.
[59] L.E. Parker and F. Tang.
Building multirobot coalitions through
automated task solution synthesis. Proceedings of the IEEE, 94(7):1289–
1305, Jul. 2006.
[60] Vittorio Perera, Sai P. Selvaraj, Stephanie Rosenthal, and Manuela
Veloso. Dynamic Generation and Reﬁnement of Robot Verbalization.
In Proceedings of RO-MAN’16, the IEEE International Symposium on
Robot and Human Interactive Communication, Columbia University,
NY, August 2016.
[61] Dennis Perzanowski, Alan C. Schultz, and William Adams. Integrating
natural language and gesture in a robotics domain. In Proceedings of
the 1998 IEEE International Symposium on Intelligent Control, 1998.
[62] Martin L. Puterman. Markov Decision Processes: Discrete Stochastic
Dynamic Programming. John Wiley & Sons, Inc., New York, NY, USA,
1st edition, 1994.
[63] Miquel Ram´ırez and Hector Geffner. Plan recognition as planning. In
IJCAI, pages 1778–1783, 2009.
[64] Anand S. Rao and Michael P. Georgeff.
BDI Agents: From Theory
to Practice. In Proceedings of the First International Conference on
Multi-Agent Systems (ICMAS-95, pages 312–319, 1995.
[65] Stephanie Rosenthal, Sai P. Selvaraj, and Manuela Veloso. Verbalization:
Narration of Autonomous Mobile Robot Experience. In Proceedings
of IJCAI’16, the 26th International Joint Conference on Artiﬁcial
Intelligence, New York City, NY, July 2016.
[66] Stuart J Russell, Peter Norvig, and Ernest Davis. Artiﬁcial intelligence:
a modern approach. Prentice Hall, 3 edition, 2010.
[67] Scott Sanner. Relational dynamic inﬂuence diagram language (rddl):
Language description, 2011.
[68] M. Scheutz and P. Schermerhorn. Affective goal and task selection for
social robots. In J. Vallverd´u and D. Casacuberta, editors, Handbook
of Research on Synthetic Emotions and Sociable Robotics: New Appli-
cations in Affective Computing and Artiﬁcial Intelligence. Idea Group
Inc., 2009.
[69] Matthias Scheutz, Julie Adams, and Scott DeLoach.
A framework
for developing and using shared mental models in human-agent teams.
JCEDM, forthcoming.
[70] Matthias Scheutz and Virgil Andronache.
Architectural mechanisms
for dynamic changes of behavior selection strategies in behavior-based
systems. IEEE Transactions of System, Man, and Cybernetics Part B:
Cybernetics, 34(6):2377–2395, 2004.
[71] Sailik Sengupta, Tathagata Chakraborti, Sarath Sreedharan, and Sub-
barao Kambhampati. RADAR - A Proactive Decision Support System
for Human-in-the-Loop Planning. In ICAPS Workshop on User Inter-
faces for Scheduling and Planning, 2017.
[72] Shirin Sohrabi, Jorge A. Baier, and Sheila A. McIlraith.
Preferred
explanations: Theory and generation via planning. In Proceedings of
the 25th Conference on Artiﬁcial Intelligence (AAAI-11), pages 261–
267, San Francisco, USA, August 2011.
[73] Sarath Sreedharan, Tathagata Chakraborti, and Subbarao Kambhampati.
Balancing Explicability and Explanation in Human-Aware Planning. In
AAAI Fall Symposium on AI for HRI, 2017.
[74] Sarath Sreedharan, Tathagata Chakraborti, and Subbarao Kambhampati.
Explanations as Model Reconciliation - A Mutli-Agent Perspective. In
AAAI Fall Symposium on Human-Agent Groups, 2017.
[75] K. Talamadupula, G. Briggs, T. Chakraborti, M. Scheutz, and S. Kamb-
hampati. Coordination in human-robot teams using mental modeling and
plan recognition. In Intelligent Robots and Systems (IROS 2014), 2014
IEEE/RSJ International Conference on, pages 2957–2962, Sept 2014.
[76] Kartik Talamadupula, J. Benton, Subbarao Kambhampati, Paul Scher-
merhorn, and Matthias Scheutz. Planning for human-robot teaming in
open worlds. ACM Transactions on Intelligent Systems and Technology.
(Special Issue on Applications of Automated Planning), 1(2), 2010.
[77] Kartik Talamadupula, Gordon Briggs, Tathagata Chakraborti, Matthias
Scheutz, and Subbarao Kambhampati.
Coordination in human-robot
teams using mental modeling and plan recognition. In IROS, 2014.


## Page 10


10
[78] Kartik Talamadupula, Gordon Briggs, Matthias Scheutz, and Subbarao
Kambhampati. Architectural mechanisms for handling human instruc-
tions in open-world mixed-initiative team tasks. To Appear in Advances
in Cognitive Systems, 6, 2017.
[79] Stefanie Tellex, Adrian Li, Daniela Rus, and Nicholas Roy. Asking for
help using inverse semantics. In In RSS, 2014.
[80] Xin Tian, Hankz Hankui Zhuo, and Subbarao kambhampati. Discovering
Underlying Plans Based on Distributed Representations of Actions. In
AAMAS, 2016.
[81] Stevan Tomic, Federico Pecora, and Alessandro Safﬁotti. Too cool for
school ??? adding social constraints in human aware planning. In Proc
of the International Workshop on Cognitive Robotics (CogRob), 2014.
[82] Michael Wooldridge. An Introduction to MultiAgent Systems. Wiley
Publishing, 2nd edition, 2009.
[83] Y. Zhang and Parker, L.E. IQ-ASyMTRe: Forming executable coalitions
for tightly coupled multirobot tasks. IEEE Transactions on Robotics,
29(2):400–416, 2013.
[84] Yu Zhang, Vignesh Narayanan, Tathagata Chakraborti, and Subbarao
Kambhampati.
A human factors analysis of proactive assistance in
human-robot teaming. In IROS, 2015.
[85] Yu Zhang, Sarath Sreedharan, and Subbarao Kambhampati. Capability
models and their applications in planning. In AAMAS, 2015.
[86] Yu Zhang, Sarath Sreedharan, Anagha Kulkarni, Tathagata Chakraborti,
Hankz Hankui Zhuo, and Subbarao Kambhampati. Plan explicability for
robot task planning. In Proceedings of the RSS Workshop on Planning
for Human-Robot Interaction: Shared Autonomy and Collaborative
Robotics, 2016.
[87] Yu Zhang, Sarath Sreedharan, Anagha Kulkarni, Tathagata Chakraborti,
Hankz Hankui Zhuo, and Subbarao Kambhampati. Plan explicability
and predictability for robot task planning. In ICRA, 2017.
[88] Hankz Hankui Zhuo and Subbarao Kambhampati. Model-Lite Planning:
Case-Based vs. Model-Based Approaches. Artiﬁcial Intelligence, 2017.
[89] Hankz Hankui Zhuo, Tuan Anh Nguyen, and Subbarao Kambhampati.
Reﬁning incomplete planning domain models through plan traces. In
IJCAI, 2013.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1707_04775v2_ai_challenges_in_human_robot_cognitive_teaming
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1707_04775V2_AI_CHALLENGES_IN_HUMAN_ROBOT_COGNITIVE_TEAMING.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

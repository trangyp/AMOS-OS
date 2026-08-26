---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1912.13490v4
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1912.13490v4_A_Neurocomputational_Account_of_Flexible_Goal-directed_Cognition_and_Consciousne

> Source: 1912.13490v4_A_Neurocomputational_Account_of_Flexible_Goal-directed_Cognition_and_Consciousne.pdf

> Pages: 39

---


## Page 1


A Neurocomputational Account of Flexible Goal-directed
Cognition and Consciousness: The Goal-Aligning Representation
Internal Manipulation Theory (GARIM)
Giovanni Granatoa,∗, Gianluca Baldassarrea
aLaboratory of Embodied Natural and Artificial Intelligence, Institute of Cognitive Sciences and Technologies, National
Research Council of Italy, Rome, Italy
Abstract
Goal-directed manipulation of representations is a key element of human flexible behaviour, while con-
sciousness is often related to several aspects of higher-order cognition and human flexibility.
Currently
these two phenomena are only partially integrated (e.g., see Neurorepresentationalism) and this (a) limits
our understanding of neuro-computational processes that lead conscious states to produce flexible goal-
directed behaviours, (b) prevents a computational formalisation of conscious goal-directed manipulations
of representations occurring in the brain, and (c) inhibits the exploitation of this knowledge for modelling
and technological purposes. Addressing these issues, here we extend our ‘three-component theory of flex-
ible cognition’ by proposing the ‘Goal-Aligning Representations Internal Manipulation’ (GARIM) theory
of conscious and flexible goal-directed cognition. The central idea of the theory is that conscious states
support the active manipulation of goal-relevant internal representations (e.g., of world states, objects, and
action sequences) to make them more aligned with the pursued goals. This leads to the generation of the
knowledge which is necessary to face novel situations/goals, thus increasing the flexibility of goal-directed be-
haviours. The GARIM theory integrates key aspects of the main theories of consciousness into the functional
neuro-computational framework of goal-directed behaviour. Moreover, it takes into account the subjective
sensation of agency that accompanies conscious goal-directed processes (‘GARIM agency’). The proposal
has also implications for experimental studies on consciousness and clinical aspects of conscious goal-directed
behaviour. Finally, the GARIM theory can benefit technological fields such as autonomous robotics and
machine learning (e.g., the manipulation process may describe the operations performed by systems based
on transformers).
1 The authors have equally contributed to the
paper.
1. Introduction
Goal-directed processes are at the basis of human
flexible behaviour. We recently proposed and vali-
dated the ‘three-component theory of flexible cog-
nition’ (Granato et al., 2020; Granato and Baldas-
sarre, 2021; Granato et al., 2022a; Granato et al.),
∗I am corresponding author
Email addresses: giovanni.granato@istc.cnr.it
(Giovanni Granato), gianluca.baldassarre@istc.cnr.it
(Gianluca Baldassarre)
highlighting that a goal-directed top-down manip-
ulation of representations is at the basis of cogni-
tive flexibility.
Although the our theory success-
fully describes the neuro-cognitive processes at the
basis of cognitive flexibility, it does not focus on the
higher-order processes underpinning flexible cogni-
tion (e.g., Planning and Problem Solving) nor on
the role of consciousness in such processes.
Consciousness is a vastly debated concept and
many theories formalise its key features (Seth and
Bayne, 2022), which focus on different aspects such
as the integration of information (Tononi, 2008;
Tononi et al., 2016; Koch et al., 2016; Tononi, 2004);
the hierarchical convergence and divergence zones
elaborating cognitive/emotional brain information
(Damasio, 1989; Meyer and Damasio, 2009; Dama-
Preprint submitted to Neural Networks
October 30, 2023
arXiv:1912.13490v4  [cs.AI]  27 Oct 2023


## Page 2


sio and Meyer, 2009a); the selection of relevant in-
formation into a central workspace and its ‘broad-
casting’ to peripheral areas (Baars, 1997; Baars
et al., 2003; Baars, 2005; Baars et al., 2013); the
top-down activation of multiple hierarchical brain
systems by the frontoparietal system (Dehaene
et al., 1998a; Dehaene and Naccache, 2001; De-
haene and Changeux, 2011); the difference between
first-order and higher-order representations (Brown
et al., 2019; Cleeremans, 2011); the coordination
of effective brain-body-environment sensorimotor
interactions (O’Regan and Noe, 2001; O’Regan
et al., 2005); the emergence of multi-modal/multi-
level representations that subserve goal-directed be-
haviours (Pennartz, 2015, 2018, 2022); the dynamic
loops that generate and adjust predictions based
on an inferential process (Clark, 2013; Hohwy and
Seth, 2020; Friston, 2018).
These theories con-
sider some key aspects that are commonly related
to goal-directed cognition such as information hi-
erarchies, top-down information selection, sensory-
motor interactions, multi-modal integration. How-
ever, with the exception of neurorepresentational-
ism (Pennartz, 2022), most theories capture only
few elements of goal-directed cognition.
This general poor integration leads to several
scientific and technological issues. First, it limits
the emergence of integrated frameworks that estab-
lish the relationships between consciousness, goal-
directed cognition and flexible behaviour. In par-
ticular, it limits the understanding of the neuro-
computational processes that lead conscious states
to produce a more flexible goal-directed behaviour.
Second, most theories of consciousness do not anal-
yse the fine computational processes that support a
conscious and goal-directed manipulation of infor-
mation. Although some theories have led to com-
putational models of consciousness (e.g., Dehaene
et al., 1998b; Pasquali et al., 2010; Tononi, 2008),
there is not yet a clear description of the system-
level manipulations of information that occur dur-
ing conscious goal-directed processing. Third, these
limitations inhibit an effective and broad exploita-
tion of these models and formalisations for tech-
nological scopes.
Although the emergence of in-
terdisciplinary fields such as machine consciousness
(Reggia, 2013) and consciousness-inspired machine
learning (e.g., Bengio, 2017), artificial intelligence
(AI) and autonomous robot systems have till re-
cently shown rigid behaviours and processes, in par-
ticular have failed to face novel conditions or goals
(Baldassarre and Granato, 2020; Hassabis et al.,
2017; Lake et al., 2017; Bubeck et al., 2023). Only
recently some AI systems have exhibited examples
of flexible general-purpose cognition (Li et al., 2022;
Driess et al., 2023; Park et al., 2023). Interestingly,
these models rely on new algorithms (‘transform-
ers’) that have notable links with the manipula-
tion of internal representations. However, the func-
tioning of these systems is still poorly understood
(Yun et al., 2021; Abdou et al., 2021; Ag¨uera y
Arcas, 2022; Srivastava and al., 2022).
Overall,
these limitations negatively impact both scientific
and technological advancements, which would ben-
efit from a adequate integration between studies on
goal-directed behaviour and higher-order aspects of
consciousness.
Addressing these issues, we extend here our
‘three-component theory of flexible cognition’ to
higher-order aspects of goal-directed cognition and
consciousness, thus introducing the Goal-Aligning
Representation Internal Manipulation (GARIM)
theory of higher-order cognition and consciousness.
The core idea of the GARIM theory is that con-
scious processes enhance the flexibility of goal-
directed behaviour by supporting the manipula-
tion of goal-relevant internal representations (e.g.,
of world states, objects, and action sequences).
These manipulations generate the knowledge that
the agent lacks to improve the alignment of such
representations with the target goals, especially
when these are new or are pursued in novel condi-
tions. Therefore, a higher goal-oriented ‘alignment’
makes active representations more likely to gener-
ate successfully goal-oriented actions.
The GARIM theory is based on five key features:
(1) an adaptive function of consciousness; (2) spe-
cific representations at the basis of conscious and
flexible goal-directed behaviours (Goal-based Inte-
grated Neural Patterns; GINPs); (3) four interact-
ing neurofunctional systems supported by cortical
networks and basal ganglia (hierarchical perceptual
working-memories, abstract working memory, in-
ternal manipulator, motivational systems) at the
basis of conscious goal-directed manipulations of
GINPs; (4) four macro-classes of representation ma-
nipulations which generate the goal-oriented miss-
ing knowledge (‘abstraction’, ‘specification’, ‘de-
composition’, ‘composition’); (5) the emergence of
a subjective sensation of agency related to the rep-
resentation manipulations (‘GARIM agency’). This
last feature contributes to differentiate the concept
of agency that emerges during a goal-directed be-
haviour from those related to consciousness and
2


## Page 3


conscious states. Although the GARIM theory in-
troduces many considerations about low-order cog-
nition (e.g., motivational and emotional aspects of
conscious flexible behaviour), it mainly focuses on
higher-order aspects of conscious cognition (e.g.,
top-down attention and planning).
This is con-
sistent with the theory functionalist approach and
technological implications, as we show by linking it
to concepts on higher-order human cognition and
artificial intelligence (see section ‘GARIM theory
and intelligence’).
For the same reason, here we
focus on meso-scale aspects of the brain (e.g. in-
teractions of brain macro-systems and broad neu-
ral representations) rather then on neuron-level as-
pects of it. This level of analysis is suitable for ad-
dressing the functions and computations targeted
here, thus both for studying human cognition and
for the development of artificial intelligent systems
and robots.
The GARIM theory primarily aims to clarify the
neuro-computational processes that actively lead
to more flexible goal-directed behaviours. In this
respect, the theory can be conceived as a neuro-
computational framework of conscious and flexi-
ble goal-directed cognition.
Moreover, the theory
gives four specific theoretical contributions. First,
it clarifies some aspects of subjective experience and
agency.
In particular, it proposes the concept of
the GARIM agency to explain the different subjec-
tive experiences that accompany conscious states.
Second, the theory contributes to specify the neu-
rocomputational mechanisms underlying the main
theories on consciousness. This allows the integra-
tion of those mechanisms within a common func-
tional and computational framework that pivots on
goal-directed processes.
Third, the theory gener-
ates insights for the experimental and clinical fields
related to conscious states and goal-directed be-
haviours.
In particular, the theory is shown to
be compatible with relevant experimental predic-
tions of other theories on consciousness. Moreover,
the theory gives indications for building new exper-
imental paradigms for testing consciousness. Last,
the theory offers an interpretation of the relation-
ships between certain clinical impairments and con-
scious goal-directed behaviours.
Fourth, the the-
ory provides some insights that could be useful for
building new computational models, ML-based sys-
tems, and robotic architectures. Also, it can be use-
ful to analyze existing ones. In this regard, compu-
tational models can operationalise the theory, al-
lowing it to be corroborated with specific empirical
data and more detailed comparisons with other the-
ories. On the other hand, indications towards ML
and robotics could improve the goal-directed flex-
ibility of current systems and their interpretations
(Baldassarre and Granato, 2020; Hassabis et al.,
2017; Lake et al., 2017).
Figure 1 summarises the main contributions of
the GARIM theory and the organisation of this
work. We first describe the three-component the-
ory of flexible cognition, highlighting its key fea-
tures, limitations, and also related technological
fields (in particular AI and robotics). Building on
such theory, we then introduce the key features of
the GARIM theory. Next, we compare our proposal
with the major theories of consciousness, showing
that key higher-order aspects of consciousness are
captured by our integrated neuro-computational
framework. We then analyse the empirical implica-
tions of the theory by considering both experimen-
tal and clinical evidence. Finally, we consider the
implications for the design of new computational
models, AI systems and robotic architectures.
Figure 1: The schema shows the key fields leading to the de-
velopment of the GARIM theory and its main contributions.
This schema also represents the overall organisation of this
work.
2. The three-component theory of flexible
cognition:
key features, limitations and
related fields
The three-component theory of flexible cogni-
tion formalises the neuro-cognitive processes that
boost cognitive flexibility during goal-directed be-
haviours (Granato and Baldassarre, 2021; Granato
et al., 2020).
In particular, the theory describes
behaviours based on learnt action-outcome associ-
ations and goals (Balleine and Ostlund, 2007; Thill
et al., 2013; Passingham and Wise, 2012; Tsujimoto
et al., 2011). In this context, ‘goals’ are defined as
3


## Page 4


representations of desirable future states that (a)
can be stored and internally re-activated and (b)
can lead to select actions directed to achieve them.
Moreover, the theory operationalises ‘cognitive flex-
ibility’, an executive function that is defined as the
capacity of switching between different representa-
tions depending on external and internal feedback
(Diamond, 2013).
The main idea of the three-component the-
ory is that flexible cognition depends on the top-
down goal-directed manipulation of representations.
These manipulated representations better support
sensory–motor interactions with the environment,
thereby boosting cognitive flexibility and goal-
directed behaviour.
The theory proposes that three main elements
are at the basis of flexible goal-directed behaviour
(Table 1).
Main elements
Explanation
Three key
components
Three neuro-functional systems
support the goal-directed top-down
manipulation of representations:
· Executive Working-Memory
· Hierarchical perceptual systems
· Top-down manipulator
First-order and second-order
representations/manipulations
Two levels of representations
and manipulations:
· First-order (e.g., perceptions
and selective attention)
· Second-order (e.g., abstract
goals and inner-speech)
Embodied
sensory-motor loops
Representation manipulations and
sensory-motor embodied loops
support goal-directed behaviours
Table 1: The table shows the main elements of the three-
component theory of flexible goal-directed cognition.
First, three neuro-functional systems support the
goal-directed representation manipulation. An Ex-
ecutive Working-Memory, supported by the pre-
frontal cortices (PFC) and frontal-striatal loops,
stores the goals/sub-goals (Hartley and Speer, 2000;
Braver and Bongiolatti, 2002). Multiple hierarchi-
cal perceptual systems, supported by cortical per-
ceptual pathways, extract and store the goal-related
representations (Rizzolatti and Matelli, 2003; Gaz-
zaley and Nobre, 2012; Raffone et al., 2014a).
A top-down manipulator, supported by frontal-
parietal cortical system and basal ganglia-thalamo-
cortical loops, applies a goal-directed manipulation
of the stored representations at different stages of
hierarchical systems (Vossel et al., 2014; Parks and
Madden, 2013; Redgrave et al., 1999; Seger, 2008;
Chelazzi et al., 2013; Pessoa, 2015). Note that fur-
ther systems can act as a top-down manipulator
(e.g., the inner-speech system; Granato et al., 2020,
2022a; Granato et al.).
Second, the theory distinguishes between ‘first-
order’ and ‘second-order’ representations and ma-
nipulations (Granato et al., 2020). The first term
refers to perceptual representations and their ma-
nipulations (e.g., visual selective attentional pro-
cesses). The second term refers to abstract/amodal
representations (e.g., goals/sub-goals, actions) and
their manipulations (e.g., splitting of goals into sub-
goals). Both refer to a self-directed form of manip-
ulation at different levels of abstraction.
Third, a synergistic interplay between the goal-
directed representation manipulation and embod-
ied sensory-motor loops is central to express flex-
ible goal-directed behaviour.
In particular, goal-
directed behaviour is supported by multiple manip-
ulations of internal representations and the external
world.
The three-component theory is validated trough
an integrated theory-driven/data-driven computa-
tional approach.
In particular, we developed a
neuro-inspired computational model based on this
theory and we tested it with a neuropsychological
test of cognitive flexibility (for further details see
the section ‘Towards computational models of the
GARIM theory’). The computational model has re-
produced the behavioural data obtained from vari-
ous cohorts of human participants, both in healthy
and clinical conditions (Granato and Baldassarre,
2021; Granato et al., 2020, 2022a; Granato et al.).
2.1. Beyond the three-component theory
Although the three-component theory has re-
ceived an experimental and computational valida-
tion, it shows limitations. First, although execu-
tive functions and goal-directed behaviours are of-
ten linked to explicit cognition and consciousness,
the three-component theory does not take into ac-
count the role of conscious processes in flexible
cognition. Despite this limitation, the theory for-
malises some key neurocognitive processes that are
central to the emergence of conscious states, such
as information hierarchies (Damasio and Meyer,
2009b), top-down information selection (Dehaene
4


## Page 5


et al., 2011), sensory-motor interactions (O’Regan
et al., 2005), and first-order/second-order repre-
sentations (Brown et al., 2019). Second, the the-
ory does not formalise monitoring processes and
related higher-order goal-directed behaviours such
as ‘planning’, defined as a flexible assembling of
new action sequences to accomplish goals (Pfeif-
fer and Foster, 2013; Delatour and Gisquet-Verrier,
2000), and ‘problem solving’, defined as a planning
process that involves partial knowledge (Newman
et al., 2003). These limitations are due to the fact
that the theory does not take into consideration
three key aspects of higher-order cognition: world
models, ‘motivations’, and ‘emotions’. The follow-
ing paragraphs briefly articulate these concepts and
their role in goal-directed behaviour.
World models. The theory takes into account the
concept of ‘goals’, formalised as stored working-
memory representations that change over time, but
it does not consider the concept of world model
(Mars et al., 2011; Passingham and Wise, 2012;
Fuster and Bressler, 2015). World models are rep-
resentations of the spatiotemporal dynamics of the
environment, integrating knowledge on the evolu-
tion of the physical environment and the effects
that actions cause on it (Soltani and Koechlin,
2022). World models support planning and prob-
lem solving as they allow the agent to internally
simulate the dynamic transitions of the environ-
ment, from a starting state to final goals. There-
fore, by integrating percept, goals and spatiotempo-
ral simulations, they support monitoring/ conflict
resolution processes and drive goal-directed plans
(Huddy and Mansell, 2023; Powers, 2016). World
model representations and processes are mostly
supported by PFC systems and their loops with
sub-cortical structures (in particular basal ganglia-
thalamus and hippocampal systems; Houk et al.,
1995; Fuster, 2008; Tang et al., 2021; Patai and
Spiers, 2021; Hasz and Redish, 2020).
Motivations and emotions. Although the three-
component theory implicitly assumes that motiva-
tional signals act as feedback to change the stored
goals, it does not explicitly examine the role of mo-
tivations and emotions at the basis of flexible cogni-
tion. Motivations support the formation and reacti-
vation of goal representations during goal-directed
behaviours, guide learning, contribute to select be-
haviors to perform and energise them (Mars et al.,
2011).
Motivations can be divided into extrin-
sic/physiological motivations (e.g., for safety, wa-
ter, and food), social motivations (e.g., for belong-
ing to a group), and intrinsic motivations (e.g.,
novelty, surprise, competence improvement, serving
knowledge and skills acquisition) (Panksepp, 1998;
Gangestad and Grebe, 2017; Ryan and Deci, 2000;
Mirolli et al., 2010). The role of emotions is still
a debated topic (Scherer, 2005; Cabanac, 2002).
Many studies suggest that they promote the pro-
duction of adaptive behaviours (e.g., engagement,
avoidance, and social communication; Panksepp,
1998; Ekman and Davidson, 1994; Damasio, 1998).
In general, emotions predispose the body and brain
to get into specific adaptive overall modes of func-
tioning. A bulk of studies investigated neural corre-
lates of motivations and emotions (Panksepp, 1998;
Schultz, 2002; Frith, 2007; Amaral, 2002; Rolls,
2004; Lisman and Grace, 2005; Paus, 2001; O’Reilly
et al., 2013; Ribas-Fernandes et al., 2011). These
studies show that they are supported by many inter-
acting sub-cortical structures (e.g., hypothalamus,
amygdala, insula, hippocampus) and cortical struc-
tures (e.g., medial/temporal cortex, orbitofrontal
cortex, anterior cingulate cortex, prefrontal cortex).
Note that the terms ‘motivations’ and ‘emo-
tions’ can refer to a global brain state (motivational
state; e.g. schizophrenia patients show a low mo-
tivational state defined ‘apathy’; Bortolon et al.,
2018) or localised events (motivational signal; e.g.,
dopamine bursts support information selection and
learning; Berke, 2018).
The two elements inter-
act (e.g., apathy in schizophrenic patients lead to
an inefficient information selection; Bortolon et al.,
2018) and contribute to shape conscious states and
goal-directed cognition. However, in this work we
particularly refers to the second function (motiva-
tional/emotional signals at the basis of the infor-
mation selection components).
2.1.1. Contributions of Artificial Intelligence and
Robotics
AI and autonomous robotics give important in-
puts to extend the three-component theory towards
the GARIM theory. In particular, they both con-
tribute to the investigation of brain and cogni-
tion by supporting their computational modelling
(see section ‘Towards computational models of the
GARIM theory’). At the same time, as discussed in
section ‘Towards AI systems and robotics architec-
tures inspired by the GARIM theory’, they might
benefit from the scientific knowledge on brain and
cognition to build more efficient and flexible intelli-
5


## Page 6


gent machines (Baldassarre et al., 2017; Baldassarre
and Granato, 2020).
Artificial intelligence, machine learning, and neu-
ral networks. Goal-oriented processes have always
played a central role in artificial intelligence (Rus-
sell and Norvig, 2016). In particular, AI has always
attributed to human intelligence the primarily role
of accomplishing goals through the search of the
most suitable starting state-goal sequence (Simon,
1975).
Interestingly, the type of encoding of the rep-
resentations of planning elements strongly affected
the evolution of the field. In particular, initial prob-
lem solving systems used ‘atomic’ representations
(i.e., distinct symbols for states and actions), which
made the action sequence search inefficient due to
combinatorial explosion. Later, studies on planning
(Russell and Norvig, 2016) ‘factorised’ the repre-
sentations of states into elements (e.g., ‘objects’)
and relations between elements (e.g., ‘being part
of’, ‘being on’). This change reduced the compu-
tational costs at the basis of the action-sequence
search.
In parallel,
‘connectionist approaches’ based
on neural-networks proposed alternative systems
based on ‘sub-symbolic representations’, namely
representations of features encoded in neural pat-
terns (McClelland and the PDPResearchGroup,
1986). Neural networks, initially used in machine
learning to implement ‘reactive processes’, have
been recently used to implement goal-directed pro-
cesses such as planning (e.g., Rehder et al., 2018;
Wayne et al., 2018). Furthermore, recent research
has proposed that ‘deep neural networks’ could
model key processes underlying human conscious-
ness (Bengio, 2017).
Overall, artificial intelligence studies highlight
how higher-order cognition can benefit of disentan-
gled and factored representations that can (a) be
combined into new ones and (b) represent interde-
pendencies among their sub-parts.
Machine consciousness: key elements at the basis
of higher-order cognition and consciousness. Ma-
chine consciousness (MC) is a research field aiming
to define the key elements that artificial-intelligence
and robotic systems should have to exhibit a certain
level of consciousness (Aleksander, 1995; Gamez,
2008). MC adopts both scientific and technologi-
cal approaches to accomplish this objective (Reg-
gia, 2013).
The scientific approach aims to de-
velop and validate computational models built on
the basis of the main theories of consciousness.
The technological approach aims to integrate el-
ements of consciousness into AI and robotic sys-
tems to improve their flexibility and adaptability.
Aleksander and Dunmall (2003) proposes fives ‘ax-
ioms’, stating which fundamental capabilities an in-
telligent system should have to exhibit a minimal
level of consciousness:‘depiction’ (i.e. the capacity
to represent elements of the world), imagination,
attention, planning, emotions. On the other hand,
Gamez (2008) proposes that MC systems can be
grouped into four classes based on their ‘conscious-
ness simulation level’. A first class (MC1) involves
the systems that exhibit a ‘conscious like’ exter-
nal behaviour, such as AIs that exhibit human-
level competence in playing complex games (Fer-
rucci, 2012; Lewis, 2012).
A second class (MC2)
encompasses systems that are generally inspired by
theories of consciousness and show internal ‘cogni-
tive processes’ similar to those of conscious agents
(e.g., attentional processes, motivation, world mod-
els; Kugele and Franklin, 2021; Franklin et al.,
2012; Holland, 2007; Marques and Holland, 2009;
J¨antsch et al., 2010).
The third class (MC3) in-
volves systems that are inspired by theories of con-
sciousness and show brain-inspired architectures
(Dehaene et al., 2003; Gamez, 2010). The fourth
and final class (MC4) encompasses systems able
to engage in phenomenological forms of conscious
subjective experience.
There is a hot debate re-
garding the implementation of this kind of artificial
systems (Carter et al., 2018; Reggia, 2013), but for
now no artificial system seems to be able to un-
dergo a human-like conscious internal experience.
At last, a relevant review (Reggia, 2013) highlights
that the proposals of MC can be categorised in five
key classes, built on specific core principles: (1) in-
ternal models of the agent itself (self-modelling);
(2) information broadcasting; (3) higher-order rep-
resentations; (4) attention processes; (5) informa-
tion integration.
These frameworks (the fundamental axioms, the
levels of simulation, and the main implementa-
tion principles) support the formalisation of higher-
order cognition and consciousness.
All these ele-
ments have been taken into account to develop the
GARIM theory.
6


## Page 7


3. The Goal-Aligning Representation Inter-
nal Manipulation theory
This section presents the five major elements
of the GARIM theory (see Table 2):
(a) the
adaptive function that consciousness plays in goal-
directed processes; (b) specific neural patterns that
form conscious goal-related representations;
(c)
four anatomo-functional macro-systems that sup-
port the manipulation of representations; (d) four
classes of computational operations that describe
such manipulations; (e) an explanation, based on
the concept of GARIM agency, that links agency
and subjective conscious experience. The following
sections present these elements in detail.
Main elements
Explanation
Adaptive function
of consciousness
Consciousness improves flexibility: conscious
states and processes support representation
manipulations in order to increase their alignment
with pursued goals, thereby enhancing
goal-directed behaviours.
Goal-related
representations
Conscious goal-directed behaviours are supported
by goal-directed integrated neural patterns (GINPs)
having two key dimensions, i.e. goal-relevance and
consciousness level.
Four key
components
Four neuro-functional systems support the goal-
directed representation manipulation: abstract
working-memory, perceptual working-memory,
internal manipulator, motivational system.
GARIM
operations
Goal-directed manipulations modify the GINPs
and are subjectively experienced as intentionally
directed operations. They are divided in four
classes of operations: abstraction, specification
decomposition, composition.
GARIM
agency
GARIM agency emerges during the execution
of conscious flexible goal-directed represen-
-tation manipulations. These generate a sub-
-jective internal reality featured by three key
elements: self-models, emotional and
perceptual vividness, and manipulation control.
Table 2: The five major elements of the GARIM theory.
3.1. The adaptive function of consciousness
The GARIM theory postulates that the adap-
tive function of consciousness is the improvement
of flexibility during the expression of goal-directed
behaviours.
In particular, conscious states en-
able agents to manipulate their internal represen-
tations (e.g., perceptions, thoughts and actions) in
order to generate knowledge more aligned with the
set goal; the higher goal-related alignment leads
to more successful goal-oriented actions in famil-
iar or novel situations, thereby enhancing goal-
directed behaviours (e.g., decision-making, planning
and problem-solving).
This feature is consistent with the commonly
recognised role of goal-directed cognition for hu-
man daily-life behaviours. Indeed, in case of new
goals or situations habitual behaviours are often
no longer suitable or efficient.
Moreover, also in
case of behaviours that successfully lead to specific
sub-goals (e.g., an improvement of physical perfor-
mance due to doping substances), they could show a
misalignment with higher-level goals (e.g., honestly
get an Olympics medal).
Our proposal specifies
that representation manipulations generate more
suitable knowledge (e.g., plans, objects’ represen-
tations, sub-goals) to face these conditions.
Most theories of consciousness highlight that
conscious processes have an adaptive role for hu-
man behaviours (see section ‘Comparisons of the
GARIM theory with other theories’). For example,
global workspace theories link conscious states to
information sharing and amplification at the basis
of decision making.
On the other hand, Predic-
tive Processing theories link conscious processes to
a continuous optimisation of inference/prediction
mechanisms related to goal-directed behaviours.
Importantly, the Neurorepresentationalism’s frame-
work explicitly links Consciousness to goal-directed
behaviours.
In particular, it suggests that con-
scious processes generate the best representations
that serve goal-directed processes.
Our proposal is compatible with studies on goal-
directed behaviour and consciousness. However, it
proposes a specific focus on higher-order processes.
For example, Neurorepresentationalism focuses on
the emergence of representations that are subse-
quently exploited by goal-directed processes.
In-
stead, the GARIM theory formalises mechanisms
that operate and constitute goal-directed cognition
(i.e., goal-directed representation manipulations).
3.2. Goal-based
Integrated
Neural
Patterns
(GINPs):
conscious
representations
at
the basis of flexible goal-directed behaviour
The GARIM theory describes brain states that
support higher-order conscious cognition, leading to
the expression of flexible goal-directed behaviour.
To adequately represent the peculiarities of these
7


## Page 8


states, we introduce the concept of ‘Goal-based In-
tegrated Neural Pattern’ (GINP; see Figure 2). Al-
though we cannot present direct experimental evi-
dence for GINPs, their existence is compatible with
studies on goal-directed behaviour and other theo-
ries of consciousness (see the paragraph ‘GINPs and
other definitions of conscious representations’).
Definition, features and brain correlates. We define
a GINP as an active distributed neural represen-
tation that is characterised by two features: (a)
consciousness level: it is consciously perceived and
thus intentionally manipulable; (b) goal-relevance:
it is functionally relevant for the pursued goals.
GINPs are integrated representations that have a
compound nature, in particular are formed by sub-
parts (‘sub-GINPs’). These sub-GINPs encode dif-
ferent aspects of goal-directed contents (e.g., per-
cepts, affordances, actions, goals).
We hypothesise that GINPs are encoded at mul-
tiple levels by many structures in the brain hier-
archies (see figure 2).
A GINP related to a spe-
cific goal (e.g., ‘patting a dog’, encoded in the
PFC) could be formed by sub-GINPs related to
visual appearance (e.g., the dog aspect, encoded
by visual areas), an overt sound (e.g., the bark-
ing, encoded by auditive areas), a inner-speech
production (e.g., the word ‘dog’, encoded by lan-
guage areas), and possible related actions (e.g.,
‘patting’, encoded by motor areas). We expect that
the strength of physical/functional connections be-
tween sub-GINPs (i.e., neural integration) varies
depending on their consciousness level and goal-
relevance.
Dynamically, only one GINP can become con-
scious at a certain moment. This is consistent with
the commonly accepted fact that only a limited
representation can access consciousness at a time.
However, the GINP continually evolves under the
effect that representation manipulations have on
its sub-GINPs. The integration between the sub-
GINPs could be supported by both physical connec-
tions and functional connectivity. Sub-GINPs can
have such a low level of integration that they stop
forming integrated representations. In this case, for
simplicity, we still keep the ‘-GINP’ word ending
(see ‘Non-GINPs’ in the next paragraph).
Non-GINPs,
Pre-GINPs,
Temp-GINPs
and
GINPs:
from unconscious to stably conscious
representations, and vice versa. We hypothesise
that GINPs enable representation manipulations,
and
thus
conscious
and
flexible
goal-directed
behaviours.
However, on the basis of their con-
sciousness level and goal-relevance, we define four
kinds of representations that can emerge under the
operation of consciousness processes.
GINPs:
whole conscious representations that
have a high level of goal-relevance and stability
in time, and thus strongly affect goal-directed be-
haviour. Temp-GINPs: representations that have
a low goal-relevance, but nevertheless temporar-
ily access consciousness (e.g., salient stimuli such
as unexpected skin pressure or distracting internal
thoughts). They can acquire goal-relevance, thus
becoming GINPs, or can be suppressed by top-
down attention.
Pre-GINPs: unconscious repre-
sentations that have a high level of goal-relevance
but do not have the support of top-down attention,
thus remaining unconscious. They can be activated
by background processes (e.g., priming) and can in-
directly influence conscious representations. Non-
GINPs: unconscious representations that have lit-
tle or no goal-relevance, but are activated by ex-
ternal events or related internal active represen-
tations. Depending on their features, Non-GINPs
could have a very low integration. Therefore, they
could stop being ‘integrated global representations’
and becoming ‘scattered local representations’.
In our descriptions, we will generally refer to
the whole brain representations (GINPs) but their
sub-parts (sub-GINPs) will often inherit their
consciousness-level/goal-relevance properties.
For
example, when we refer to a GINP as a ‘goal-
relevant consciously perceived representation’, we
also imply its specific sub-GINPs are goal-relevant
and accessible by consciousness processes. Instead,
when we consider the different status of the cur-
rently active sub-GINPs, we refer to them sepa-
rately.
Figure 2 (box C) shows that the four types of rep-
resentations can exhibit a sequential dynamic rela-
tionship. For example, a non-GINP could progres-
sively acquire goal-relevance until becomes a pre-
GINP and then a GINP. Conversely, a GINP can
be de-activated and become a pre-GINP; and in
case it loses most of its goal-relevance it becomes
a non-GINP. On the other hand, a non-GINP can
temporally access consciousness with a low goal-
relatedness, becoming a temp-GINP (e.g., repre-
senting an object that suddenly enters the field of
view). However, unless it is later recognised as rel-
evant for the set goal, thus becoming a GINP, it is
discarded and becomes a non-GINP.
8


## Page 9


Figure 2:
(A) Different kinds of Goal-based Integrated Neural Patterns (GINPs), classified on the basis of their key dimensions:
goal-relevance and conscious level. (B) Possible neural correlates of a GINP; the figure shows four sub-GINPs (orange, grey,
violet, yellow), encoding different goal-relevant elements (e.g., perceptual features of objects, affordances, actions, abstract
representations of goals).
(C) Possible sequential relationship between different kinds of GINPs; green arrows indicate an
‘unconscious-to-conscious’ change (e.g., a pre-GINP that becomes a GINP) while red arrows indicate the inverse change. Note
that a curved arrow, on top of each box, indicates the level of goal-relatedness/goal-based representation manipulation (e.g.,
absent, temporary, prolonged).
The difference between non-GINPs/pre-GINPs
and temp-GINPs/GINPs accounts for the differ-
ences between subliminal/implicit/unconscious and
supraliminal/explicit/conscious
representations
highlighted by many brain studies (Meneguzzo
et al., 2014). In addition, and importantly, these
concepts
can
highlight
the
difference
between
awareness and consciousness. Indeed, non-GINPs
and pre-GINPs can temporarily access conscious-
ness, thus becoming temp-GINPs or stable GINPs
that the agent can report about (awareness). On
the other hand, only GINPs can be the target
of active manipulation operations that, thereby
supporting higher-order consciousness and flexible
goal-directed behaviour.
Therefore, this distinc-
tion implies that awareness plays a ‘preparatory’
role for conscious goal-directed processes, while
consciousness involves the core operative stage of
conscious goal-directed processes.
In section ‘A
GARIM agency scale’ we refer to these different
concepts as ‘phenomenal consciousness’ (aware-
ness), ‘access consciousness’, and ‘manipulative
consciousness’. The scale implies that Awareness
and Consciousness are two poles of conscious
goal-directed cognition.
GINPs and other definitions of conscious repre-
sentations. Many theories of consciousness expect
that only specific representations have the proper-
ties needed to be consciously processed (see section
‘Comparisons of the GARIM theory with other the-
ories’ for more detailed comparisons). For exam-
ple, the IIT proposes that conscious states show
a high level of integration and specification. The
GWT/GNWT propose that consciousness is sup-
ported by stable activations of highly integrated
systems, dispatching information to short-range
sub-modules. The Radical Plasticity Theory (part
9


## Page 10


of the Higher-Order Theories of consciousness) sug-
gests that only the meta-representations, featuring
stability, strength and distinctiveness, are perceived
as conscious contents.
Finally, Neurorepresenta-
tionalism postulates that conscious states depend
on multimodal/multi-level representations subserv-
ing goal-directed behaviours.
While the GARIM theory focuses on a subset
of conscious representations (i.e., those that sup-
port goal-directed behaviours), the definitions re-
lated to the different types of GINPs is compati-
ble with those proposed by several theories of con-
sciousness. In addition, however, the definition of
GINPs explicitly requires their active goal-oriented
manipulation to become stably conscious.
3.3. Four key components at the basis of goal-
directed manipulations of representations
The GARIM theory postulates that conscious
higher-order cognition is supported by goal-oriented
manipulations of representations.
These manip-
ulations rely on four key ‘components’ (Figure
3), namely four partially overlapping anatomo-
functional brain macro systems.
Note that the
GARIM theory inherits some key components from
its precursor theory, extending them (in particular,
by adding a fourth motivational component) and
further specifying their functioning (e.g., see the
section ‘The four classes of GARIM computational
operations’).
(1) Perceptual working memory component. The
three-component theory proposes that perceptual
hierarchies play a key role in goal-directed be-
haviours. Moreover, various theories of conscious-
ness postulate that hierarchical perceptual sys-
tems and perceptual working-memories support the
emergence of conscious states (see section ‘Compar-
isons of the GARIM theory with other theories’).
In the GARIM theory, the perceptual working
memory component plays a key role for the emer-
gence of GINPs.
The component corresponds to
partially segregated ‘unimodal’ sub-systems that
perform bottom-up sensory processing. These op-
erations support the formation of increasingly ab-
stract perceptual sub-GINPs (e.g., from low-level
features to high-level representations).
In par-
ticular, the bottom-up information flows convey
pre-GINPs/non-GINPs representations to higher-
level cognitive areas.
The component also sup-
ports a top-down information flow, causing the re-
activation of the peripheral sub-GINPs (e.g., goal
imagination and mental simulations during visual
planning). These manipulation processes can con-
tribute to transform pre-GINPs into GINPs and
to inhibit temp-GINPs (non-GINPs that temporary
access consciousness). The component also imple-
ments peripheral modal working memories. These
maintain active perceptual representations having
a short duration and a high level of detail (e.g., the
perceptual representation of a goal).
In the brain, the component is supported by cor-
tical hierarchical pathways. These encode bottom-
up information at multiple levels of abstraction, in-
stantiating extensive associative networks linking
sub-GINPs encoded in different cortices.
At the
same time, fronto-parietal cortical pathways acti-
vate in a top-down goal-directed fashion the con-
tents of the modal working memories.
(2) Abstract working memory component. The
three-component theory proposes that an abstract
working memory plays a key role in goal-directed
behaviours (e.g., storage of abstract goals). More-
over, most theories of consciousness ascribe a cen-
tral role to working memory (see section ‘Compar-
isons of the GARIM theory with other theories’).
In the GARIM theory, the abstract working-
memory component supports the active mainte-
nance and integration of different goal-relevant
sub-GINPs (e.g., related to contexts, behavioural
strategies, predictions, and values).
These sub-
GINPs are related to low-level sub-GINPs (e.g., be-
havioural strategies can be related to movement
representations and expected somatosensory and
visual feedback) but encode more abstract informa-
tion with respect to perceptual sub-GINPs. This
feature makes them a form of meta-knowledge.
Importantly, abstract sub-GINPs dynamically
integrate both spatiotemporal relations of the world
elements (e.g., own body parts, objects, other
agents) and agent’s predictions (e.g., goal-related
action outcomes) in world models. Thus, the ab-
stract working-memory component exploits world
models to monitor plans (i.e., check the predic-
tion correctness based on percept and goals/sub-
goals), to counter internal (self) and external (en-
vironment) disturbances, and finally to generate the
missing knowledge (e.g., new points of view on ob-
jects, new solutions).
Within the brain,
abstract multimodal sub-
GINPs are encoded by different prefrontal cortices
(e.g., dorsolateral PFC, ventrolateral PFC, and an-
terior cingulate cortex) and related subcortical ar-
10


## Page 11


Figure 3:
Schema showing the ‘components’ of the GARIM theory, and their relation with brain anatomo-functional systems.
The red-to-blue coloured gradient indicates the decreasing involvement of motivational/emotional processes.
eas (e.g., basal ganglia-thalamo-cortical loops and
hippocampal system). Within each cortical area,
neural winner-take-all mechanisms allow the acti-
vation of only one or few possible patterns at a
time. Importantly, the abstract working memory
component plays a ‘hub role’ by putting in rela-
tion sub-GINPs in different areas (e.g., different re-
gions of the fronto-parietal network). In particu-
lar, it dynamically integrates abstract sub-GINPs
with perceptual sub-GINPs, thus realising a close
interaction with perceptual working memory. This
coupling supports perceptual monitoring underly-
ing conflict resolution, goal-alignment (e.g., percep-
tual monitoring of goal-prediction matching), and
sub-GINP sequences activations at the basis of vi-
sual planning (images of world states traversed to
reach the goal).
(3) Internal manipulator component. The three-
component theory proposes that goal-directed be-
haviours are supported by a top-down manipulator
of representations. Several theories of consciousness
attribute a central importance to attentional pro-
cesses and their top-down influence on conscious in-
formation (see section ‘Comparisons of the GARIM
theory with other theories’).
The GARIM theory proposes that an internal
manipulator component manipulates the contents
of abstract and perceptual working-memories. In
particular, it selects and warps perceptual and ab-
stract sub-GINPs to generate sequences of GINPs
with increasing goal-alignment. Importantly, these
manipulations support (a) monitoring and align-
ment of goals, sub-goals and world models (ab-
stract sub-GINPs) with perceptions (perceptual
sub-GINPs) to solve conflicts and internal/external
disturbance and (b) the subsequent generation of
new knowledge needed in case of novel situations
and goals.
In the brain, the manipulator’s operations are
11


## Page 12


supported by two major selection mechanisms. One
corresponds to local inhibitory circuits of cortex,
in particular those composing the cortical fronto-
parietal system.
The second corresponds to the
disinhibition mechanisms of basal ganglia-thalamo-
cortical loops.
The influence of basal ganglia on
the cortex has a diminishing gradient, moving from
frontal to posterior cortical areas.
Although the
GARIM theory focuses on these manipulation brain
systems, others could contribute to goal-directed
manipulations. For example, the three-component
theory proposes that the language system acts as
an internal manipulator of abstract goals (e.g., in-
ner speech; Granato et al., 2020, 2022a; Granato
et al.).
(4) Motivational component. Motivational systems
play a key role in the expression of goal-directed
behaviours, from goal formation to action selection
(see section ‘Beyond the three-component theory’).
Various theories of consciousness take into consid-
eration the role of motivational and emotional pro-
cesses for consciousness (see section ‘Comparisons
of the GARIM theory with other theories’).
In particular, the GARIM theory proposes that
a motivational component indirectly guides the ma-
nipulator, contributing to select goals at different
levels of abstraction within the abstract working
memory.
Moreover, the motivational component
also directly contribute to the manipulator oper-
ations, giving different salience to perceptual and
abstract sub-GINPs (see Figure 3).
To this pur-
pose, the motivational component closely interacts
with the perceptual and abstract working memories
to perform goal-monitoring and goal-aligning oper-
ations based on the manipulation of percepts, world
models and plans.
The motivational component also contributes to
giving an emotional subjective nuance to conscious
representations.
In particular, perceptual sub-
GINPs (e.g., representations of external stimuli and
anticipated outcomes) are evaluated (appraisal) on
the basis of their contribution to the achievement of
goals (goal-alignment). This process contributes to
integrate cognitive and emotional aspects of goal-
directed behaviour, and plays a key role for the
agent’s subjective experience accompanying con-
sciousness (see section ‘GARIM agency and the
subjective experience of consciousness’).
In the brain, motivational and emotional evalua-
tions drive the selection processes of basal ganglia
and cortical winner-take-all mechanisms. In partic-
ular, evaluations generated in subcortical structures
(e.g., the hypothalamus, amygdala, hippocampus)
reach the basal ganglia starting from the the limbic
loop. Moreover, they reach various cortical areas
starting from the PFC ventral areas (e.g., orbital,
medial, and insular cortex).
3.4. Four classes of GARIM operations
The interaction of the four components supports
goal-directed manipulations of internal representa-
tions.
These manipulations are divided in four
GARIM operations (Figure 4).
These operations
modify the GINPs and are subjectively experienced
by the agent as intentionally directed operations
(see section ‘GARIM agency and the subjective ex-
perience of consciousness’).
The four classes are
now considered in detail.
Figure 4: The four classes of GARIM operations that the
manipulator performs on GINPs.
(1) Abstraction. Abstraction causes the generation
of sub-GINPs at different levels of abstraction, from
perceptual sub-GINPs to abstract sub-GINPs. Ab-
straction also executes goal-dependent dimensional
reductions, preserving only goal-relevant aspects of
low-level sub-GINPs.
For example, in addressing
the goal ‘grasping the cup’, abstraction operations
might change the detailed sub-GINP related to the
perceptual representation of the cup into a more ab-
stract goal-oriented sub-GINP (e.g., a shape-based
representation, ignoring colour because it is not use-
ful for the pursued goal).
In the brain, abstraction relies on the hierarchi-
cally organised stages of cortical pathways. Basal
ganglia-thalamo-cortical macro loops (limbic, asso-
ciative, motor) operate the selection of patterns at
suitable levels of abstraction.
12


## Page 13


(2) Specification. Specification performs the in-
verse operations with respect to abstraction. For
example, starting from an abstract sub-GINP (e.g.,
‘something to drink with’) it can generate a sub-
GINP corresponding to a specific object (e.g., ‘my
preferred tea cup’).
Since specification involves mappings from a few
to many features, it requires a goal-directed and
contextualised generation of suitable information
(e.g., the perceptual details of ‘my preferred cup’
when the goal is ‘drink tea at home’). These opera-
tions are made possible by the manipulator’s selec-
tions and by the generative networks of perceptual
and abstract working memories.
In the brain, specification relies on the top-
down ‘inverse’ activation of cortical pathways, mov-
ing from multimodal representations in the frontal
cortices to modality-specific representations in the
lower sensory cortices. The generation of more de-
tailed representations is guided by the cortical and
basal-ganglia selection processes.
(3) Decomposition. Decomposition performs the
separation of representations (GINPs and sub-
GINPs) into sub-parts. This operation executes a
different kind of manipulation with respect to ab-
straction and specification. While the latter per-
form a ‘vertical manipulation’ that changes the ab-
straction level, decomposition performs a ‘horizon-
tal manipulation’ at a fixed level of abstraction. For
example, decomposition could extract the represen-
tation of an object (e.g., ‘a tea cup’) from the back-
ground, or the representation of a part of the object
(e.g., ‘the handle’) from other parts (e.g., ‘the cup
container’).
In the brain, decomposition could be supported
by neural structures similar to those of specifica-
tion, thus involving the cortex and basal ganglia-
thalamo-cortical loops.
However, it might more
strongly involve the channels and sub-channels
within those loops to disinhibit specific cortical con-
tents.
Cortical local winner-take-all mechanisms
should facilitate the selection of sub-parts of neural
patterns.
(4) Composition. Composition performs the in-
verse operations with respect to decomposition, in-
tegrating many sub-GINPs into larger sub-GINPs
or into a coherent whole GINP. Through composi-
tion, the agent can build global items starting from
its parts (e.g., to consider a ‘cup container’, ‘han-
dle’, ‘tea’, and ‘tea spoon’, as a whole ‘tea cup’).
Composition supports various aspects of goal-
directed processes.
For example, it supports the
generation of plans (e.g., by chunking a sequence
of actions and their effects) or imaginary processes
leading to solve a problem (e.g., building a new
tool by aggregating various parts).
Composition
performs a different manipulation with respect to
abstraction.
Abstraction performs a dimensional
reduction (loss of information) while composition
‘chunks representations’ at the same level of ab-
straction.
However, composition and abstraction
could give rise to adaptive synergies.
For exam-
ple, they could lead to integrating many sub-GINPs
at the same abstraction level, then transforming
the resulting sub-GINP into a more abstract one
(e.g., chunking ‘reaching’, ‘grasping’, ‘transport-
ing’, ‘drinking’ to generate the abstract goal ‘taking
a tea’).
In the brain, composition might rely on func-
tional connectivity between different networks.
Moreover, it might rely on physical connectivity
linking semantically related neural patterns (e.g.,
two different colours within the visual cortex, or
the ‘red’ colour in the visual cortex and ‘alertness’
in an affective area).
The integrated functioning of the GARIM opera-
tions: representation manipulations boost flexibil-
ity during problem solving. The GARIM operations
give rise to a super-ordinate function we call Con-
scious Knowledge Transfer (CKT). CKT refers to
a transfer of knowledge from familiar contexts to
novel contexts, thus supporting flexible human cog-
nition and behaviour.
In particular, CKT oper-
ates by flexibly abstracting, specifying, decompos-
ing, and composing the sub-GINPs that encode the
current knowledge (e.g., related to objects, goals,
actions, and expected outcomes). Therefore, on the
basis of multi-level goal-monitoring/goal-alignment
evaluations, CKT allows the agent to generate the
necessary knowledge to improve performance, to
successfully act in changed conditions, or to ac-
complish novel goals. Differently from the concept
of generalisation, CKT leads to the generation of
new knowledge beyond previous experiences. While
generalisation involves interpolation processes (e.g.,
the imagination of a goal position that involves an
object positioned between two previously experi-
enced positions), CKT involves extrapolation pro-
cesses (e.g., the imagination of an object located
anywhere in a known space; or the generation of a
new tool based on composing elements). These op-
13


## Page 14


erations are based on the extraction of relevant reg-
ularities from previous experiences, and their trans-
formation to generate knowledge to address novel
challenges (decisions, plans, problems).
Problem solving tasks are best suited to illus-
trate the CKT and the GARIM operations. Such
problems are challenging because their solution re-
quires the generation of missing knowledge on ill de-
fined components. For instance, consider the clas-
sic Duncker’s problem (Duncker, 1945). In this task
participants are required to fix a candle on a wall.
They can only use some pins, available in a box, and
some matches to solve the problem. The solution
requires to pin the cardboard box on the wall and
then set the candle on it. This solution requires a
‘change of perspective’ on the elements of the prob-
lem (Guilford, 1967; Chrysikou et al., 2016).
In-
deed, participants generally consider the box only
as a container, but this change of perspective leads
them to focus on its properties (e.g., ‘cardboard can
be pinned’). Thus, they discover that the box can
serve as a candle holder. As highlighted by the ‘rep-
resentational change theory’ (Ohlsson, 1992), the
solution requires the participant to generate a new
suitable representation of the key problem’s sub-
components (e.g., of the box).
The GARIM theory can explain the manipula-
tion and generation of knowledge that leads to the
solution of the Duncker’s problem. For example, an
agent could use decomposition to parse the scene,
and then sequentially activate the sub-GINPs that
encode the different objects of the task. When fo-
cusing on the cardboard, the agent might use de-
composition and specification to analyse the dif-
ferent feature-based sub-GINPs of the cardboard
(e.g., the usual function, the shape, and the mate-
rial). These sub-GINPs, potentially influenced by a
context-dependent priming effect (e.g., a pre-GINP
encoding the pin), can recall the representation of
a previous experience (e.g., the agent that used
pins to stick cardboard drawings on the wall). Ex-
ploiting composition, the agent might then trans-
fer the piece of knowledge ‘cardboard things can
be pinned on walls’ (a sub-GINP) to the cardboard
box (another sub-GINP). At last, the resulting sub-
GINP could be abstracted (abstraction) and com-
pared with the initial goal of ‘attaching the can-
dle to the wall’.
A high correspondence between
the two would imply a high goal-alignment of the
GINP, achieved thanks to the CKT.
3.5. Subjective experiences during conscious goal-
directed behaviours: the GARIM agency
The nature of subjective experiences is widely
debated in the literature, which commonly refers
to them as the ‘hard problem of consciousness’
(Chalmers, 1995).
Although the GARIM theory
does not offer a solution to the hard problem of con-
sciousness, it proposes its own perspective on this
topic. In particular, the theory relates the activity
of the internal manipulator with the emergence of a
subjective experience of agency. Therefore, we in-
troduce the concept of GARIM agency to identify
the sense of agency that emerges during the expres-
sion of conscious flexible goal-directed behaviours.
In particular, the theory proposes that the ma-
nipulation of representations generates an internal
simulated reality having three key features: self-
models, emotional/perceptual vividness, and ma-
nipulation control.
First, the simulated reality involves some aspects
of the agent itself. This self-simulation can be en-
hanced based on previous experiences with other
intentional agents (Fernandez-Duque et al., 2000).
Second, the manipulator activates low-level sub-
GINPs that enrich the GINPs with detailed per-
ceptual representations. The GINPs are continu-
ously evaluated with respect to their goal-related
alignment and thus they are emotionally charged.
These GINPs hence exhibit perceptual and emo-
tional features similar to those that the agent ex-
periences when acting in the environment. For this
reason, the internally simulated and manipulated
reality is vividly perceived and felt similarly to the
real experience. Third, the intentional manipula-
tion of representations cause imagined effects simi-
lar to those caused by motor actions performed in
the external environment. Therefore, the manipu-
lations produce a sense of agency (Jeannerod, 2003)
for which the agent perceives itself as the cause of
‘internal actions’ (GARIM operations) and of the
effects they produce.
Note that the concept of GARIM agency is com-
patible with other concepts proposed by the litera-
ture. For example, Metzinger (2013) highlights the
concept of mental action and cognitive agency to
identify the capacity to control own goal-directed
conscious processes. Moreover, mental action and
self-control are concepts approached by the active
inference framework (Metzinger, 2017; Hohwy and
Seth, 2020).
Thus, the GARIM theory captures
many aspects of conscious goal-directed cognition
14


## Page 15


and agency that are considered fundamental by
other studies in the field.
3.5.1. A GARIM agency scale
The GARIM agency is a suitable concept for
generating a quantitative scale, which takes into
account the different levels of consciousness and
flexible goal-directed behaviours.
In particular,
the three features of the GARIM agency (self-
model, emotional/perceptual vividness, and manip-
ulation control) lead to the emergence of three ‘lev-
els of Consciousness’ during the expression of goal-
directed behaviours: phenomenal consciousness, ac-
cess consciousness, and manipulation consciousness
(Figure 5).
We explain these three levels by de-
scribing examples of human cognition.
Figure 5: A scale of consciousness based on the concept of
GARIM agency.
Phenomenal consciousness pivots on the pe-
ripheral activations of perceptual/emotional sub-
GINPs.
They are triggered by either external
perceptual inputs or internal bottom-up processes
(e.g., emotional/motivational events).
The emer-
gence of an unexpected, goal-irrelevant percep-
tual event is an example of this GARIM agency
level.
Indeed, while possibly showing some emo-
tional/perceptual vividness, this event activates a
temp-GINP (conscious goal-irrelevant representa-
tion). It is accompanied by a low level of GARIM
agency and it is soon discarded. In case the repre-
sentation is a pre-GINP (unconscious goal-relevant
representation), it can be transformed into a GINP
thus leading to a higher level of GARIM agency.
Access consciousness involves a mild top-down
selection that leads to a weak competition between
different sub-GINPs.
This GARIM agency level
can be exemplified by the state of mind-wandering
(Gruberger et al., 2011).
This is a brain state,
usually accompanying the performance of routines,
that generates conscious sequential thoughts rep-
resenting temp-GINPs (e.g., thoughts on possible
actions). In this respect, Christoff et al. (2016) sug-
gest that mind-wandering involves a shallow “delib-
erate constraint”, that is, a partially deliberate cog-
nitive control on own thoughts. Based on our pro-
posal, this process should involve continuous trans-
formations of pre-GINPs into GINPs and vice versa,
and non-GINPs into temp-GINPs and vice versa.
These processes would be the effect of a weak top-
down control, and indeed mind-wandering can take
place without awareness (Schooler et al., 2011).
Manipulation consciousness is characterised by
a high control on internal representations.
This
state is exemplified by specific forms of mindfulness
achieved in meditation (Kabat-Zinn, 1990; Mali-
nowski, 2013).
For example, focused meditation
aims to induce a high goal-directed attentional fo-
cus (e.g., on own breath). This amplifies the ac-
cess to consciousness of goal-relevant information
(GINPs), and leads to a non-judmental state by
strategically suppressing internal/external distrac-
tions (temp-GINPs) and ruminations (Tang et al.,
2015; Yates and Immergut, 2015). Note that even in
the case of unfocused non-judgmental states (e.g.,
some forms of mindfulness) a higher-level goal can
be active, namely ‘to keep the whole state of med-
itation intact from distraction’.
Similar features
can be shared by brain states supporting a high at-
tentional engagement in competitive sport sessions
(He et al., 2018; Miller and Clapp, 2011; Memmert,
2009) or intellectual games (e.g., chess; Atherton
et al., 2003; Wang et al., 2020; H¨anggi et al., 2014).
Overall, the GARIM agency is expected to con-
tinuously fluctuate along the different levels of con-
sciousness. Healthy awake people might likely re-
main most of the time within middle levels of con-
sciousness, for example when carrying out daily
routines (e.g., house reordering and shopping). The
rest of the time they might have transitory phases
into the lower levels of consciousness, and limited
periods of time into the highest levels. The follow-
ing section proposes that there are states of con-
sciousness accompanied by altered GARIM agency
15


## Page 16


levels, falling between the middle and the low levels
of consciousness.
Altered states of the GARIM agency. The GARIM
theory and the scale presented in the previous sec-
tion describe specific states of consciousness during
the expression of goal-directed behaviours. Some
of them may result in an altered state of GARIM
agency (Figure 5). For example, alterations of the
GARIM agency could involve pseudo-hallucinations
and hallucinations (Telles-Correia et al., 2015).
Both states are experienced in the absence of ex-
ternal stimuli. However, pseudo-hallucinations are
perceived as unreal dummy perceptions whereas
hallucinations are perceived as real perceptions. In-
terestingly, the two show different levels of sensory
controllability and vividness, which are higher in
pseudo-hallucinations (van der Zwaard and Polak,
2001). These evidence are compatible with an al-
teration of the GARIM agency.
Dreams and lucid dreams are other conscious-
ness states that could involve an altered GARIM
agency. Dreams involve an uncontrolled imagina-
tion during the REM sleep while lucid dreams in-
volve a partially controlled imagination (Stumbrys
et al., 2012). Both states correspond to the genera-
tion of a vivid internally simulated reality (Revon-
suo, 2006). However, a higher level of control dis-
tinguishes lucid dreams from dreams (Voss et al.,
2009), also suggesting that a stronger activation of
frontal areas could cause this difference. Our pro-
posal is compatible with this evidence as the alter-
ations of the GARIM agency should depend on the
influence of the top-down manipulator.
4. Comparisons of the GARIM theory with
other theories
The GARIM theory proposes an integrated
framework that takes into account conscious and
higher-order cognition, and thus it is compati-
ble with most theories of consciousness (Seth and
Bayne, 2022). In particular, it accounts for several
key aspects that are considered fundamental for the
emergence of conscious states (see Table 3). Here
we briefly describe these theories and we compare
them with the GARIM theory.
Integrated
Information
theory
(IIT). The
IIT
(Tononi, 2008; Tononi et al., 2016; Koch et al.,
2016; Tononi, 2004) proposes that systems exhibit-
ing high capacity of discrimination (to encode sev-
eral alternative neural representations of cognitive
contents, e.g. percepts) and integration (to encode
several different associations between different as-
pects of neural representations, e.g.
stimuli) po-
tentially have a high level of consciousness. This
theory also proposes the Φ coefficient, a quantita-
tive measure of the level of information integration.
The thalamo-cortical system should have a key role
in conscious states - thus an high Φ - due to its high
synaptic integration and interconnection. A recent
update of the theory (Koch et al., 2016) has identi-
fied a ‘hot zone’, located within the parietal cortex,
that supports the formation of conscious contents.
On the other hand, the frontoparietal system would
have a control role of cognitive contents but not a
central role for the emergence of a conscious state.
The GARIM theory does not delve into specific
aspects of information theory, but it takes into ac-
count key features of the IIT such as discriminabil-
ity and integration.
For example, the perceptual
and abstract working memory components are ex-
pected to perform a high ‘discrimination’ of expe-
riences. In particular, the manipulator component
selects specific sub-GINPs between several alterna-
tive ones, thus assigning a specific and stable mean-
ing to experiences (high discrimination).
At the
same time, the generation of stable GINPs requires
a dynamic highly flexible ‘assembling’ of sub-GINPs
based on suitable functional and anatomical con-
nectivity (high integration).
The GARIM theory, however, has also impor-
tant differences with respect to the IIT theory.
First, the IIT theory lacks a functional explanation
of conscious processes, fundamental for developing
a comprehensive theory of consciousness (Cerullo,
2015). Indeed, computational systems can exhibit
a high Φ while performing dull calculations (Seth
et al., 2006; Aaronson, 2014). Second, the GARIM
theory emphasises the importance of a top-down
and goal-directed manipulation of representations,
while the IIT argues that a top-down control is not
fundamental for the emergence of conscious con-
tents. However, the two theories may focus on dif-
ferent conscious states. Indeed, the GARIM theory
focuses on higher-order conscious states based on
representation manipulation, but it expects the ex-
istence of conscious states with a temporary lower
level of top-down control (temp-GINP). These lat-
ter states appear to be the focus of the IIT theory.
16


## Page 17


Convergence-Divergence
Zones
theory
(CDZT).
The CDZT (Damasio, 1989; Meyer and Dama-
sio, 2009; Damasio and Meyer, 2009a) proposes
that the brain is organised on multiple periph-
eral CDZs (P-CDZs; e.g., sensory cortices) and
major central CDZs (C-CDZs; e.g, associative ar-
eas such as prefrontal, parietal, and temporal cor-
tices). The P-CDZs transmit a bottom-up informa-
tion flow to the C-CDZs, which perform a top-down
retro-activation on them. In particular, the retro-
activation increases the meaningful integration of
bottom-up peripheral representations, resulting in
conscious perception and imagination. Conversely,
if the P-CDZs fail to activate the associated pat-
terns in the C-CDZs, there is no retro-activation
and the peripheral representations remain uncon-
scious. The CDZs theory also proposes that low-
level somatic reactions assign an emotional valence
to the representations within the C-CDZs, giving
them sufficient priority to enter consciousness pro-
cessing (‘somatic marker hypothesis’; Bechara and
Damasio, 2005; Verdejo-Garc´ıa et al., 2006).
At
last, the theory proposes that the representations at
the basis of subjective experience (C-CDZs) encode
sensorimotor relations between the agent, objects,
and events in the external environment (‘embodi-
ment approach’; Damasio and Meyer, 2009a).
The GARIM theory takes into account key el-
ements of the CDZ theory (Damasio, 1989), fur-
ther specifying them with neuroscientific and com-
putational details. The GARIM theory attributes
a key role to the neural hierarchies of the brain.
Indeed, P-CDZs and C-CDZs correspond to brain
structures that should support perceptual and ab-
stract sub-GINPs, respectively. Furthermore, the
GARIM theory proposes that these sub-GINPs are
generated by bottom-up and top-down informa-
tion flows. Bottom-up flows support the encoding
of perceptions in perceptual and abstract working
memories at increasing levels of abstraction. Top-
down flows generate sub-GINPs that are functional
to the achievement of goals. Both flows are con-
trolled by the top-down manipulator, guided by mo-
tivations and goals.
The manipulator selects the
relevant information that travels along cortical hi-
erarchies, thus improving the goal alignment of rep-
resentations.
In line with the CDZT, the GARIM theory also
takes into account the role of emotions and mo-
tivations for the assignment of valence to expe-
rience.
The GARIM theory specifies that moti-
vational systems support sub-GINPs prioritisation
through the GARIM computational operations. Fi-
nally, in line with the CDZT, the GARIM the-
ory emphasises the role of emotions and motiva-
tions for subjective experience.
In particular, it
proposes that top-down manipulation processes ac-
tivate peripheral sensory areas (imagination) and
emotional/motivational systems (similar to the so-
matic marker hypothesis; Damasio, 1989). The re-
sulting activations then send a feedback to the cen-
tral areas, associating a high level of perceptual
vividness and emotional valence to subjective ex-
perience (see Section ‘GARIM agency and the sub-
jective experience of consciousness’).
Global Workspace Theory (GWT) and Global Neu-
ronal Workspace Theory (GNWT). The GWT
(Baars, 1997; Baars et al., 2003; Baars, 2005; Baars
et al., 2013) proposes that consciousness relies on
a set of interacting cognitive elements, which are
metaphorically associated with the elements of a
theatre:
conscious contents (e.g., percepts and
thoughts; the ‘actors in the stage’); the global
workspace of working memory (the ‘theatre stage’);
selective attention (the ‘theatre spotlight’); exec-
utive functions (the ‘director’); and unconscious
background processes that interact with the global
workspace (the ‘audience’).
The theory proposes
that alternative contents compete to enter the
global workspace and thereby become conscious.
Selective attention processes, guided by the exec-
utive functions - in turn guided by motivations and
goals - choose which conscious contents win the
competition. The winner contents are broadcasted
from the global space to the other processes to sup-
port higher-order processes (e.g., decision making
and self-monitoring).
The GNWT (Dehaene et al., 1998a; Dehaene
and Naccache, 2001; Dehaene and Changeux, 2011)
was initially proposed to specify the neural cor-
relates of the GWT based on extensive empiri-
cal support (Mashour et al., 2020) and compu-
tational formalisations (Dehaene and Changeux,
2005; Dehaene et al., 2017). The hypothesis pro-
poses the existence of two computational spaces
in the brain. A first space is supported by high-
density short/medium range connections and in-
cludes many specialised functional modules (e.g.,
sensory areas, motor systems, memory areas, eval-
uative components). A second space, called ‘neu-
ronal global workspace’, is supported by long-range
excitatory projections (Dehaene and Changeux,
2011) and includes a distributed set of associative
17


## Page 18


areas (the prefrontal, parietal, temporal and cin-
gulate cortices) and cortical-subcortical networks
(e.g., the fibres of the corpus callosum and the
cortico-thalamic system). This architecture allows
the global workspace to generate global activation
patterns with variable duration (ignitions), involv-
ing distributed interconnected networks.
These
patterns strongly compete and inhibit or favour re-
lated patterns within peripheral specialised mod-
ules (e.g., perceptions, emotions and actions related
to an object). The frontal-parietal system plays a
key role in supporting this top-down amplification
of information. The biological underpinnings of the
GNWT have been extended to envisage the exis-
tence of ‘buffers’ (working memories) between the
sensorial cortices and the neuronal workspace (Raf-
fone et al., 2014b, 2015). At last, the GNWT has re-
cently been integrated with inferential frameworks
(Mashour et al., 2020), suggesting that top-down
amplification corresponds to an inferential process
applied on bottom-up sensory inputs.
The GARIM theory integrates the main con-
cepts of the GWT (Baars, 1997) and the GNWT
(Dehaene and Changeux, 2011).
In addition, it
enriches those concepts by specifying the possi-
ble goal-directed computations (e.g., manipulation
functions) and the brain mechanisms that might
underlie them.
First, as the GWT and GNWT,
the GARIM theory assumes a ‘centre-periphery’
architecture underlying conscious states as well as
goal-directed behaviours. In particular, it proposes
multiple perceptual working memories that trans-
mit information to the abstract working memory.
Therefore, it integrates such information and dis-
patches the result back to the peripheral struc-
tures (the ‘broadcasting’ of GWT and GNWT).
Second, the mechanisms underlying the generation
of GINPs are compatible with those supporting ‘ig-
nitions’. Indeed, an ignition is a coherent activation
of linked local neural patterns in central and periph-
eral areas. Third, the GARIM theory ascribes a key
role to the fronto-parietal brain system, proposing
that it is fundamental for the top-down and goal-
directed control of sensorimotor cortical pathways.
While sharing these important elements with
the GWT and GNWT, the GARIM theory fur-
ther specifies them.
First, in the GWT the pat-
terns activated by ignitions are mainly generated
by percepts.
Instead, the GARIM theory postu-
lates that the volitional goal-directed generation of
GINPs depends on the selection of sub-GINPs by
the top-down manipulator. Second, while assign-
ing an important role to the cortical fronto-parietal
system, the GARIM theory highlights the pivotal
role that the basal ganglia-thalamo-cortical system
plays in the manipulation of sub-GINPs. Finally,
the GARIM theory specifies the functioning of the
bottom-up and top-down information flows in terms
of computational manipulation operations (abstrac-
tion and specification/generative mechanisms).
Higher-order theories (HOTs). HOTs represent a
family of theories originally formulated in philos-
ophy (for a review, see Brown et al., 2019).
All
HOTs share the idea that first-order representa-
tions, for example the activation of patterns within
the early stages of the visual cortex, are necessary
but not sufficient to have a conscious experience.
In particular, an agent can generate conscious con-
tents only after first-order states have been evalu-
ated and meta-represented by higher-order repre-
sentations. The Radical Plasticity theory (Cleere-
mans, 2007, 2011), an instance of the HOTs, pro-
poses that meta-representations show three specific
features: robustness, stability and distinctiveness.
The theory has been recently integrated with in-
ferential processes (Cleeremans et al., 2020). Most
HOTs suggest that a certain level of ‘inner aware-
ness’ of one’s ongoing mental processes is necessary
to have consciousness.
The claims of the HOTs
have been supported by empirical evidence, high-
lighting the contribution of frontal networks in the
formation of conscious higher-order representations
(Lau and Rosenthal, 2011).
At last, the HOTs
propose that first-order and second-order represen-
tations involve the interaction between subcortical
and cortical systems, leading to an explanation of
emotional aspects of conscious experience (LeDoux
and Brown, 2017).
The GARIM theory specifies the key concepts of
the HOTs (Brown et al., 2019) in terms of computa-
tional brain mechanisms. First, the GARIM theory
proposes that the interaction of four components
leads to the encoding and selection of sub-GINPs at
increasing levels of abstraction. The abstract sub-
GINPs hence integrate the contents of lower-level
perceptual sub-GINPs at a more abstract level, thus
representing a form of meta-representations. More-
over, in agreement with the Radical Plasticity The-
ory (Cleeremans, 2011), GINPs should exhibit the
three key features of robustness, stability and dis-
tinctiveness because they tend to (a) encode dis-
tinctive elements of goal-directed processes and (b)
remain stable over time as long as they are relevant
18


## Page 19


for the set goal. On the other hand, unconscious
representations (e.g., non-GINPs) can briefly access
consciousness (temp-GINPs) but then quickly fade
away (low stability). Finally, the GARIM theory
can also account for the ‘inner awareness’ postu-
lated by HOTs. In particular, the goal-directed in-
ternal manipulation of representations give rise to
a sense of agency that can accompany inner aware-
ness (see Section ‘Subjective experiences during
conscious goal-directed behaviours:
the GARIM
agency’).
Sensori-motor theory (SMT). The SMT proposes
that conscious experience pivots on the interactions
between the brain, the body, and the environment
(O’Regan and Noe, 2001; O’Regan et al., 2005).
The theory was developed within the theoretical
frameworks of embodied cognition (Anderson, 2003;
Garbarini and Adenzato, 2004; Borghi and Cimatti,
2010) and enactivism (Hutto, 2005). The theory
substantially diverges from the other theories as it
de-emphasises the role of brain processes and rep-
resentations, highlighting instead the importance of
sensorimotor experience. The theory proposes that
sensorimotor contingencies (the events linking ac-
tions to sensory changes; Jacquey et al., 2019) are
fundamental in determining the phenomenal sen-
sations that accompany conscious experience. Dif-
ferences in these sensorimotor activities distinguish
sensory experience and reasoning/imagination pro-
cesses. In particular, sensory experience has ‘alert-
ness’ - the capacity to exogenously attract our at-
tention - and ‘corporality’ - the fact that bodily
actions immediately modify the sensory input.
In agreement with the SMT (O’Regan and Noe,
2001), the GARIM theory supports the idea that
consciousness plays a fundamental function for
adaptation. However, the SMT proposes that the
key function of consciousness is the generation of
a close coupling between motor action and its per-
ceived effects. Instead, the GARIM theory proposes
that the key function of consciousness is to enhance
goal-directed processes to increase behavioural flex-
ibility. Moreover, the SMT pushes the embodied
view of cognition towards anti-representationalist
positions (Pennartz, 2018).
The GARIM theory
departs from these positions as ‘representations’
and ‘manipulation of representations’ are key con-
cepts for it.
However, key theoretical aspects at
the basis of both theories have been recently rec-
onciled by highlighting that goal representations
could support a link between actions and their per-
ceived effects (sensory-motor contingencies) (Bal-
dassarre et al., 2018; Jacquey et al., 2019; Mannella
et al., 2018). Finally, in line within the SMT, the
GARIM theory clearly emphasises the importance
of agency for the generation of subjective conscious
experience. However, the GARIM agency is cen-
tred on goal-directed representation manipulations
while the SMT is focused on sensory-motor inter-
action with the environment.
Predictive Processing theories (PPTs). The PPTs
(for a review, see Hohwy and Seth, 2020) are a fam-
ily of theories that link conscious states to the con-
cepts of ‘predictive coding’, ‘error minimisation’,
and ‘world model’.
According to the theory, the
brain implements internal world models based on
stacked dynamic neural loops. At each loop, the
higher levels produce predictions about the acti-
vation of the lower levels (hence ‘predictive cod-
ing’), which in the lowest loops directly predict
the percepts of the world.
On the other hand,
the lower levels flow information upward and com-
pute prediction-errors by comparing the top-down
predictions and their bottom-up activations. The
prediction errors support a perpetual refinement of
the world models.
The Active Inference Frame-
work (AIF), an instance of PPTs, proposes that the
prediction-error can be minimised also by perform-
ing actions (e.g., ocular movements) to produce
expected sensory data (predictive control). Over-
all, the brain correlates of PPTs correspond to the
bottom-up hierarchical flows, for example from sen-
sory cortices to prefrontal systems, and top-down
feedback flows, from higher-order brain systems to
lower sensory areas.
The GARIM theory shares some important el-
ements with the PPTs.
Both theories highlight
the important role for consciousness of bidirectional
brain hierarchies. In particular, the GARIM theory
proposes that top-down information flows along the
hierarchies implement generative processes recon-
structing representations at lower-levels. This pro-
cess is fully in line with the generative mechanisms
of predictive coding. In addition, both the GARIM
and the AIF explicitly refers to an active top-down
control of action.
Although these common points, the GARIM the-
ory has additional elements and some divergent po-
sitions. First, the GARIM top-down manipulator
performs several goal-oriented operations on knowl-
edge, at different abstraction levels.
These pro-
cesses generate new knowledge not only by inter-
19


## Page 20


polating previously acquired knowledge, but also
by extrapolating it to produce more creative de-
viant representations (e.g., imagining a new tool).
Instead, the PPTs and AIF, pivoting on the mech-
anism of prediction error, are more closely linked to
interpolation processes. Second, the GARIM the-
ory ascribes a central role to goal-directed cognition
and behaviour while initial PPTs proposals did not
do so. However, recent proposals of the AIF have
started to interpret goal-directed processes (Pez-
zulo et al., 2015; Matsumoto et al., 2022; Hohwy
and Seth, 2020; Friston et al., 2016), thus produc-
ing a potential common ground with the GARIM
theory. At last, although the GARIM theory as-
cribes a key role to information flows in cortex, it
also proposes that basal-ganglia and cortical selec-
tion mechanisms play a key role to instantiate the
manipulator’s operations.
Neurorepresentationalism theory (NRT). The NRT
(Pennartz, 2015, 2018, 2022) is a theoretical frame-
work that defines Consciousness as a ‘multimodal
and situational survey’.
It proposes that con-
scious states depend on multimodal/multi-level rep-
resentations, which are fundamental to sub-serve
goal-directed behaviours (e.g., planning).
This
framework proposes five features that describe con-
scious experience: ‘multimodal richness’, the emer-
gence of sensations in multiple distinct modali-
ties; ‘situatedness/immersion’, the sensation that
our body is immersed in the space and has a cen-
tral position with respect to the surrounding stim-
uli; ‘unity/integration’, the emergence of a sin-
gle undivided and multi-modal representation; ‘dy-
namics/stability’, the emergence of dynamic per-
ceptions (e.g., external environment changes) and
static perceptions (e.g., stationary objects); ‘inten-
tionality’, the generation of signals that are in-
terpreted as something other than ourselves.
At
last, the NRT highlights that predictive processing
is a suitable framework for describing the neuro-
computational basis of conscious states.
In par-
ticular, it proposes that multi-level representa-
tions emergently lead to multimodal and spatially
wide ‘super-inferences’, corresponding to phenome-
nal experiences.
The GARIM theory and the NRT share the idea
that conscious states have the scope to support
goal-directed behaviours.
Notably, they are the
only two theories that explicitly and systemati-
cally propose this bridge. Moreover, the two the-
ories share some hallmarks that describe conscious
states.
In particular, some features of conscious
representations proposed by the NRT are consis-
tent with the definition of GINPs.
For example,
GINPs are defined as integrated systemic represen-
tations whose sub-parts encode different aspects of
goal-directed processes (e.g., motivations, percep-
tions, actions).
Moreover, GINPs are formed by
sub-GINPs at different levels of abstraction, from
modality-specific working memories to multi-modal
abstract working memories.
At last, GINPs are
‘embodied representations’ that integrate aspects
of the environment, the agent and their relation-
ships (e.g., action outcomes). Therefore, the ‘multi-
modal/multilevel representations’ proposed by the
NRT partially overlaps with the concept of GINPs.
Despite these commonalities, the GARIM theory
shows key differences with the NRT. First, GINPs
and sub-GINPs are characterised by a specific di-
mension defined ‘goal-relatedness’ (i.e. their relat-
edness with respect to the set goal), not considered
by the NRT. Second, the two theories tend to focus
on two different aspects of goal-directed behaviour.
In particular, the NRT focuses on the emergence of
the best representations which then subserve goal-
directed processes.
Instead, the GARIM theory
mostly focuses on the representation manipulation
operations that constitute goal-directed processes
and behaviour.
4.1. Integrating key aspects of Consciousness into
a neuro-functional framework of flexible goal-
directed behaviour.
Recent works propose an analysis and compar-
ison of the main theories of consciousness (Seth
and Bayne, 2022; Del Pin et al., 2021). Above we
have compared these theories with the GARIM the-
ory, highlighting their similarities and differences
(for a summary, see Table 3).
Due to its func-
tionalist systemic approach, the GARIM theory
contributes to integrate the other theories on con-
sciousness at two levels: a ‘background integration’
level and a ‘focused integration’ level. Concerning
the first level, multiple concepts from previous the-
ories describe ‘brain functioning/organisation prin-
ciples’ with which the GARIM theory is compatible
(e.g., ‘information integration/discrimination’, ‘em-
bodiment and sensory-motor contingencies’, and
‘predictive inferential processes’). Concerning the
second level, some concepts proposed by other the-
ories are central also for the GARIM theory (e.g.,
‘first/second order representations and inner aware-
ness’, ‘hierarchical bidirectional flows’, ‘broadcast-
20


## Page 21


Theories
Key concepts
Information
integration and
discrimination
Hierarchical
bidirectional
flows
Broadcasting,
Ignitions
First/second order
representations,
Inner awareness
Embodiment,
Sensorimotor
contingencies
Predictive
inferential
processes
Multi-modal and
multi-level situated
representations
Goal-aligning
representation
manipulations
IIT
✓✓
✗
✗
✗
✗
✗
✗
✗
CDZT
✗/✓
✓✓
✗
✗
✓
✗
✓
✗
GWT/GNWT
✗
✓
✓✓
✗
✗
✓
✗/✓
✗/✓
HOTs
✗
✗/✓
✗
✓✓
✗
✗/✓
✗
✗
SMT
✗
✗
✗
✗
✓✓
✗
✗
✗
PPTs
✗/✓
✓
✗
✗
✗/✓
✓✓
✗/✓
✗
NRT
✗/✓
✓
✗
✗
✗/✓
✓
✓✓
✗
GARIM theory
✓
✓
✓
✓
✓
✓
✓
✓✓
Table 3: Main concepts of the theories of consciousness considered in this work. Symbols: ✓✓: concept pivotal for this theory;
✓: concept compatible/encompassed by this theory; ✗/✓: concept partially compatible/encompassed by this theory; ✗: concept
not compatible/encompassed by this theory.
ing/ignitions’, and ‘multi-modal/multi-level situ-
ated representations’).
Overall,
the GARIM theory highlights that
higher-order cognition and consciousness necessar-
ily require all these elements. However, the two dif-
ferent levels of integration could differentially ben-
efit scientific and technological fields. For example,
elements of the focused integration could aid the
design of computational models. Indeed, they usu-
ally reproduce specific functions and neural mecha-
nisms to explain brain and behaviour. On the other
hand, elements drawn from background integration
could aid the design of AI/robotic architectures. In-
deed, these systems can also benefit from algorith-
mic solutions that are only conceptually inspired
by higher-order human cognition and consciousness
(see section ‘Implications of the GARIM theory for
computational modelling, AI and Robotics’).
5. Experimental and clinical implications of
the GARIM
The GARIM theory represents a theoretical
framework that has implications for several fields.
In this section we first consider its contribution to
the understanding of the concept of ‘Intelligence’.
Then we proposes interpretations of psychological
and neuropsychological evidence on goal-directed
behaviours and consciousness.
5.1. GARIM theory and Intelligence
The GARIM theory focuses on the higher-order
goal-directed cognition involving conscious states.
These same processes could be at the basis of the
expression of ‘intelligent processes and behaviours’.
Although the investigation of intelligence is beyond
the scope of this work, the GARIM theory can con-
tribute to its understanding, in particular to clarify
its relationship with flexible goal-directed cognition
and consciousness.
The term ‘intelligence’ refers to a composite con-
struct encompassing multiple areas of competence
(Gardner, 2000) and is measured with different
scales of intelligence (e.g., WAIS; Benson et al.,
2010). Recently, new theoretical frameworks have
stressed the difference between domain-general and
domain-specific intelligence (Burkart et al., 2017),
also strengthening the relationship between intel-
ligence and goal-directed behaviour (Chiappe and
MacDonald, 2005; Tegmark, 2017).
In our previous computational proposals we mod-
elled the interaction between domain-general pro-
cesses (e.g., working memory and motivational sys-
tems) and domain-specific competence (e.g., sen-
sory and motor learning). This allowed the study of
task-related representation learning (Granato et al.,
2022b) and goal-directed representation manipu-
lation (Granato and Baldassarre, 2021; Granato
et al., 2020, 2022a; Granato et al.). On the basis
of these works, we explicitly proposed the idea that
the flexibility characterising domain-general intel-
ligence rests on the goal-directed manipulation of
representations (Baldassarre and Granato, 2020).
The GARIM theory extends these ideas to higher-
order cognition and consciousness. In particular, it
proposes that consciousness boosts flexibility, a key
21


## Page 22


aspect of general-domain intelligence.
This flexi-
bility might aid the acquisition of domain-specific
competences (e.g., motor skills) through the top-
down guidance of the learning processes. Further-
more, flexibility might support the on-shot selec-
tive performance of previously acquired automatic
behaviours.
This proposal is compatible with some impor-
tant features of other theories of consciousness. For
example, the Radical Plasticity Theory (belonging
to the HOTs) suggests that consciousness boosts
learning processes.
Moreover, the GWT and the
GNWT suggest that the global-workspace informa-
tion broadcasting improves the local learning of rep-
resentations within peripheral brain sub-modules
(e.g., motor modules). Moreover, the proposal is
compatible with the concept of information integra-
tion proposed by the IIT. Indeed, flexible intelligent
behaviour should require a high information inte-
gration within higher-order brain areas (e.g., the
abstract working-memory), in turn influencing the
lower-order ones (e.g., the motor and perceptual ar-
eas).
5.2. An interpretation of experimental and clinical
evidence based on the GARIM theory
The GARIM theory may be useful in interpreting
psychological and neuropsychological evidence on
goal-directed behaviours and consciousness.
Fur-
thermore, it may stimulate the development of
new experimental paradigms investigating the func-
tional role of conscious states in flexible cognition.
5.2.1. Lesion studies, goal-directed cognition, and
conscious states
The relationship between brain lesions and con-
sciousness disorders is still not fully clear. In par-
ticular, there is no research that systematically
links impairments of frontal systems and basal
ganglia, which play a key role for our proposal,
with consciousness disorders.
However, the em-
pirical support of HOTs indicates that PFC le-
sions cause a deficit in consciousness-related pro-
cesses (e.g., metacognitive capabilities; Lau and
Rosenthal, 2011). Moreover, recent proposals sug-
gest that PFC lesions could influence consciousness
in unnoticeable ways (Fox et al., 2020).
On the
other hand, various studies show that basal gan-
glia lesions cause a general consciousness impair-
ment (e.g., Rohaut et al., 2019). Moreover, a bulk
of studies (Ell et al., 2006, 2010; Ward et al., 2013;
Price et al., 2009) show that focal damages of basal
ganglia impair explicit/conscious reasoning but not
implicit/unconscious categorisation. These studies
do not explicitly investigate consciousness, but they
put in relation impairments of key elements of goal-
directed cognition and explicit/conscious processes.
In general, the GARIM theory does not pro-
pose a conclusive explanation regarding the relation
between consciousness disorders and frontal/basal
ganglia lesions.
However, it proposes a link be-
tween these lesions, the possible alterations of
explicit/conscious cognitive processes and goal-
directed flexible behaviours.
For example, the
GARIM theory predicts that extended lesions to
PFC systems and associative portions of basal gan-
glia would impair abstract working memory and the
top-down manipulator.
Their impairment should
corrupt the manipulation of GINPs.
In particu-
lar, this alteration should lead to a reduced abil-
ity to transform pre-GINPs in GINPs or to sup-
press temp-GINPs (e.g., distractors).
Therefore,
these alterations should make an agent less gen-
erative and focused. These predictions are consis-
tent with the clinical literature on goal-directed be-
haviour. Indeed, alterations of PFC and basal gan-
glia cause cognitive inertia, namely a reduced ca-
pacity to intentionally generate/activate strategies
required to successfully complete a given program
of actions (Levy, 2012, 2021). Despite these studies
do not explicitly refer to consciousness, our theory
proposes a link between conscious states and the
above deficits. Indeed, cognitive inertia should alter
the generation of GINPs, thus the exploitation of
conscious and generative processes to express flexi-
ble behaviours. Moreover, the impairment of these
structures could alter the GARIM agency, explain-
ing the emergence of hallucinatory perceptual rep-
resentations after frontal and basal ganglia lesions
(Fornazzari et al., 1992; Frith, 1996; Wodarz et al.,
1995; McMurtray et al., 2014).
Note
that
these
alterations
do
not
corre-
spond to global alterations of consciousness (vigi-
lance/awareness). Indeed, the GARIM theory pre-
dicts that a focused lesion of PFC systems and basal
ganglia would not cause a general loss of conscious-
ness (e.g., coma). Moreover, they would not pre-
vent the access of stimuli to consciousness (phenom-
enal consciousness).
In summary, the GARIM theory predicts that
the frontal cortex and basal-ganglia impairments
alter the link between consciousness and flexi-
ble behaviours.
In particular, they impede an
22


## Page 23


adequate emergence/management/manipulation of
GINPs (access consciousness and manipulative con-
sciousness). This corresponds to an inefficient ex-
ploitation of conscious processes for generating new
knowledge and new perspectives during the expres-
sion of goal-directed behaviours (e.g. problem solv-
ing).
5.2.2. Experimental evidence: the predictions of the
GARIM theory
The GARIM theory does not yet have direct em-
pirical support, but it produces specific experimen-
tal predictions. Importantly, these predictions are
in line with the experimental evidence provided by
other theories of consciousness.
First, the GARIM theory predicts that percep-
tual sub-GINPs, involving the posterior higher-
order
sensory
cortices,
should
remain
active
throughout
the
performance
of
explicit
tasks.
These activations should support bottom-up ab-
straction and top-down generative processes. This
prediction matches the experimental evidence at
the basis of the IIT. Indeed, by contrasting stim-
ulation effects during coma and wakefulness, ev-
idence shows that a sustained activation of the
posterior ‘hot-zone’ is necessary for consciousness
(Koch et al., 2016).
Second, the GARIM theory also predicts that
the emergence of GINPs is preceded by the activity
of the top-down manipulator, involving the syner-
gistic activation of the fronto-parietal system and
the basal ganglia. This prediction agrees with the
evidence produced by the GNWT on contrastive
tasks (e.g., masking, binocular rivalry, attentional
blinking; Aru et al., 2012), highlighting that con-
sciousness emerges due to a strong activation of
the fronto-parietal areas (‘ignitions’; Dehaene et al.,
2011). The activation of the top-down manipulator
and the emergence of GINPs would correspond to
the ignition processes recorded in these studies. In
addition, the GARIM theory further predicts that,
given the same stimuli, different ignitions (GINPs)
would emerge when different goals are pursued.
Third, some studies argue that there can be a dis-
sociation between attention and explicit/conscious
processing (Koch and Tsuchiya, 2007). These pro-
posals are usually linked to bottom-up attention
rather than top-down attention.
Indeed, atten-
tion processes are generally considered ‘necessary’
to pass from unconscious to conscious processing
(Van Boxtel et al., 2010; Raffone et al., 2014a;
Pitts et al., 2018), but they may not be ‘sufficient’.
In this respect, the GARIM theory predicts that:
(a) stimuli having a high relevance for the pursued
goals have a higher chance to be selected by atten-
tion and thus to access consciousness (pre-GINPs);
(b) stimuli with a high bottom-up saliency may be
able to enter consciousness (temp-GINPs) but they
fade in case of a lack of support from top-down
goal-directed mechanisms.
Finally, the GARIM theory predicts that a basal-
ganglia/prefrontal cortex activation is necessary to
generate a goal representation. This prefrontal ac-
tivation precedes and guides the GINP generation
and conscious goal-directed behaviour. This predic-
tion agrees with evidence reported by the HOTs. In
particular, these show that a prefrontal activation is
necessary to support second-order activations and
the evaluation of own knowledge (Lau and Rosen-
thal, 2011). Our proposal agrees with these inter-
pretations, as GINPs involve second-order represen-
tations integrating perceptual, motivational, and
motor representations. Moreover, the GARIM the-
ory specifies that conscious processes involve both
the manipulation of representations and the evalu-
ation of their alignment with the pursued goal.
Overall, however, we believe that the tasks on
consciousness proposed so far can only partially test
the basic principles of the GARIM theory. The next
section elaborates on this idea.
5.2.3. Towards new tasks and protocols that test
GARIM theory more directly
Notwithstanding the growing evidence, empirical
support of the major theories of consciousness is
still unsatisfying (Yaron et al., 2022; Del Pin et al.,
2021; Doerig et al., 2021; Melloni et al., 2021). The
GARIM theory can contribute to identify the prob-
lems that prevent the collection of more solid em-
pirical evidence on consciousness.
Common
experimental
protocols
(e.g.,
con-
trastive methods; Aru et al., 2012) mostly focus
on the first stage of conscious processing consid-
ered by the GARIM theory, requiring experimental
participants to detect a stimulus and to perform
simple actions in response to it (e.g., reply ‘yes/no’
or choose one between few options, e.g. by voice
or by pressing buttons). According to the GARIM
theory, these tasks are not sufficient to test manip-
ulative consciousness. In particular they focus only
on awareness, explained by the GARIM theory as
the initial passage from non-GINPs/pre-GINPs to
temp-GINPs (phenomenal consciousness). Instead,
23


## Page 24


these tests are not sufficient to dissociate phenom-
enal consciousness and manipulative consciousness,
the latter of which requires sustained manipulative
processes.
Indeed, experiments capable of mak-
ing this distinction should involve new goals or
new conditions that require goal-directed processes
(planning or problem-solving). Alternatively, they
should require the re-evaluation of relationships di-
rected to increase goal-alignment, for example in
relation to action-subgoal or subgoal-goal relation-
ships. For example, Weiskrantz (1995) discussed a
possible experimental approach potentially testing
goal-directed conscious processes. The author con-
siders how blindsight patients can successfully dis-
criminate stimuli without awareness (P¨oppel et al.,
1973; Weiskrantz, 2004). Moreover, paraplegic pa-
tients can produce limb responses again without
awareness (Weiskrantz, 1991). With both these pa-
tients, ‘commentary actions’ (e.g., ‘press a button’
or ‘verbally report your experience’) are necessary
to check the presence of awareness. Similarly, to
test these processes in animals it is necessary to pre-
train them in the use of commentary actions (e.g.,
press a button; Cowey and Stoerig, 1995). The key
point is that both humans’ and animals’ commen-
tary actions might involve habitual processes rather
than intentional conscious processes. To avoid this
problem, new experimental paradigms have been
developed to explicitly test the presence of goal-
directed processes (e.g., devaluation; Balleine and
Dickinson, 1998; Mannella et al., 2016). This pro-
posal supports the idea that an effective experi-
mental verification of goal-directed manipulations
of representations can be a key step to check the
operation of consciousness.
We started to investigate the concept of repre-
sentation manipulation with computational mod-
els (Granato et al., 2020; Granato and Baldassarre,
2021; Granato et al., 2022a; Granato et al.) by us-
ing the Wisconsin Card Sorting test (Heaton et al.,
1993). Even if this test measures executive func-
tions and not consciousness, it involves an explicit
categorisation and requires important representa-
tion manipulation processes (e.g., the selection of
different representations to best support a flexi-
ble goal-direct behaviour in a changing environ-
ment). Despite its relevant features, however, the
test is not yet able to check various aspects of con-
sciousness considered relevant by the GARIM the-
ory (e.g., multi-stage planning or problem solving).
Overall, adequate tasks testing the GARIM pro-
cesses should complement existing paradigms fo-
cused on testing awareness. In particular, an ideal
task should have these elements:
(a) test per-
ceptual awareness, for example require to iden-
tify/categorise input patterns based on explicit
rules; (b) request the achievement of new goals,
face new conditions, or improve goal-alignment so
as to require the internal manipulation of repre-
sentations to produce new knowledge; (c) test the
specific use of the GARIM manipulation operations
(abstraction, specification, decomposition, compo-
sition); (d) test the processes of monitoring of goal-
alignment; (e) test the key elements of the GARIM
agency: self-model, emotional/perceptual vividness,
and manipulation control.
6. Implications of the GARIM theory for
computational modelling, and for AI and
Robotics
The GARIM theory takes into account both neu-
ral and computational aspects of conscious and
goal-directed behaviour.
Indeed, it has both sci-
entific and technological implications.
First, the
theory paves the way to the development of new
computational models. In particular, these could
capture computational operations at the basis of
conscious and flexible goal-directed behaviour (e.g.,
top-down manipulation) and related neural mecha-
nisms (e.g., competitive cortical and sub-cortical se-
lection mechanisms). These models could produce
quantitative predictions to be tested against spe-
cific empirical data, thus corroborating our theory.
Second, the theory provides a guideline to possibly
enhance the current AI and robotic systems. These
systems might be empowered with functions and
components proposed by the GARIM theory. The
upgraded systems should be evaluated for their abil-
ity to improve performance with respect to current
systems (e.g., in terms of goal-oriented flexibility
and learning speed).
6.1. Towards computational models of the GARIM
theory
We already operationalised the three-component
theory with a computational model (Figure 6;
Granato and Baldassarre, 2021; Granato et al.,
2020, 2022a; Granato et al.). This model is sup-
ported by a neuro-inspired system architecture
based on machine learning elements (generative
models, recurrent neural networks, and reinforce-
ment learning) and novel brain-inspired algorithms.
24


## Page 25


The model was validated with human experimen-
tal data in various conditions (e.g., frontal pa-
tients, Parkinson, Autism) and ages (e.g., chil-
dren, teenagers, young adults, and middle adults).
In particular, the model reproduced data from
many cohorts of human participants performing the
Wisconsin card sorting test (WCST; Berg, 1948;
Heaton et al., 1993). We used the WCST to test
the model because, although it was initially pro-
posed to test executive functions in general, it has
now become the most commonly used neuropsy-
chological test of cognitive flexibility (Miles et al.,
2021). In this respect, the test requires a top-down
switching of internal representations to successfully
accomplish a goal when the environment changes
(Granato and Baldassarre, 2021).
Figure 6:
Schema of an already published computational
model of the three-component theory (Granato and Baldas-
sarre, 2021; Granato et al., 2020, 2022a; Granato et al.). The
model is a starting point for building GARIM-inspired com-
putational models.
Overall, the model emulates human flexible goal-
directed cognition and behaviour. Since it is based
on the three-component theory, it emulates three of
the four components postulated by the GARIM the-
ory (a hierarchical perceptual system, an executive
working memory, and a top-down manipulator),
sensory-motor loops, and first-order/second order
representations and manipulations. Although the
model specifically aimed to solve the WCST and did
not consider conscious processing, it could still cap-
ture the C1 and C2 levels of simulation proposed by
machine consciousness (Gamez, 2008). In particu-
lar, the model shows an explicit rule-based categori-
sation process relevant for consciousness functions.
Moreover, the model presents various architectural
and functional elements supporting consciousness
in the brain.
For these reasons, this model rep-
resents a possible starting point for building new
computational models following the principles of
the GARIM theory. To this end, we now propose a
‘blueprint architecture’ giving guidance to this pur-
pose (Figure 7).
The architecture should be supported by an ade-
quate interaction of the four key components (per-
ceptual hierarchies, working memory, manipulator,
and motivation components). However, their im-
plementation could follow different approaches that
emulate the brain mechanisms at different levels of
detail.
For example, the models could be imple-
mented with neuro-inspired algorithms (e.g., neural
networks and reinforcement learning methods) ab-
stracting from the details of the brain mechanisms
(as we done in Granato and Baldassarre, 2021). On
the other hand, the models could emulate finer bi-
ological details of the brain (e.g., spiking neurons
and neuronal connectivity; Dehaene and Changeux,
2005; Dayan and Abbott, 2001).
The following
paragraphs examine potential approaches to imple-
ment each component of blueprint architecture.
6.1.1. Perceptual component: generating perceptual
and higher-order GINPs
The perceptual hierarchical component should be
able to perform both abstraction and specification
based on generative mechanisms. Deep Belief Net-
works (DBNs; Hinton et al., 2006; Hinton, 2012)
are suitable for implementing this function. They
can learn input representations at increasing lev-
els of abstraction based on statistical regularities
and task demands (Granato et al., 2022b). More-
over, they are able to generate representations on
the basis of previous inputs and top-down gener-
ative processes (Granato and Baldassarre, 2021).
Spiking-neuron neural networks are another ap-
proach that can be used to perform representation
learning of key elements and timed chains (Kap-
pel et al., 2014). These methods can also be used
to implement world models encoding sequences of
world states within planning architectures (Rueck-
ert et al., 2016; Basanisi et al., 2020). Predictive
coding is another suitable approach to implement
this function (Rao and Ballard, 1999; Pezzulo, 2014;
Donnarumma et al., 2017). In this respect, recent
approaches integrate predictive coding with goal-
oriented systems (Pezzulo et al., 2015; Matsumoto
et al., 2022; Jung et al., 2019a).
A key aspect of computation models of the
GARIM theory involve the mechanisms used to
25


## Page 26


Figure 7: The GARIM blueprint architecture aiding the realisation of specific implementations of models following the GARIM
theory principles.
Italics in brackets: main brain neural mechanisms (structure and processes) possibly implementing the
components.
support the encoding and dynamics of sub-GINPs
and GINPs.
The activation of sub-GINPs could
rely on local neural biased competitions taking
place at different levels of abstraction (e.g., as
modelled in competitive neural circuits and self-
organising maps; Mysore and Kothari, 2020; Koho-
nen, 2001; Diehl and Cook, 2015). The generation
of GINPs could rely on local winning populations,
encoding sub-GINPs, that could excite other win-
ning populations in distal areas through long-range
excitatory connections (e.g., as modelled in Miikku-
lainen et al., 2006). Neural mechanisms analogous
to these have been already used in models proposed
within the GNWT Dehaene and Changeux, 2005.
6.1.2. Working memory component:
the long-
lasting activation of GINPs
The working memory component should support
the long-lasting activation of GINPs in the absence
of their initial internal and external triggers. Recur-
rent Neural Networks (RNNs; Barak and Tsodyks,
2014) are suitable models to emulate these func-
tions. Indeed, they emulate the dynamic re-entrant
circuits of PFC systems and basal ganglia-thalamo-
cortical loops.
At the same time, basal ganglia-
like selection mechanisms of the manipulator could
upload/down information from such recurrent cir-
cuits (e.g., OReilly and Frank, 2006; Holcman and
Tsodyks, 2006). Reservoir computing (for a review
see Lukoˇseviˇcius and Jaeger, 2009) is another suit-
able approach to implement dynamic working mem-
ories. In particular, it exploits recurrent stochastic
networks of which activity is ‘read-out’ by exter-
nal units. These units project back to the recur-
rent networks, learning to induce in them the de-
sired dynamic pattern. Reservoir networks are suit-
able to emulate different details of the brain, indeed
they can be implemented with firing-rate neurons
(e.g., ‘echo-state networks’; Jaeger, 2001) or spiking
neurons (e.g., ‘liquid state machines’; Maass et al.,
2002).
6.1.3. Manipulator component:
selection mecha-
nisms sculpting GINPs
The manipulator component should be able to
implement the GARIM operations, thus sculpting
26


## Page 27


GINPs to generate knowledge. Computational ap-
proaches that emulate the functioning of the basal
ganglia-thalamo-cortical loops could be a starting
point (Schroll and Hamker, 2013).
In particular,
they could emulate the double-inhibition mecha-
nisms of the basal ganglia (Gurney et al., 2001),
dynamically tuned selection processes, random ex-
ploratory selections, and focused ‘locking-in’ selec-
tions (e.g., see Schroll and Hamker, 2013; Prescott
et al., 2006; Fiore et al., 2014). At the same time,
cortical winner-take-all processes could contribute
to tune selections at finer levels (e.g., Mysore and
Kothari, 2020; Arber and Costa, 2022).
At last,
lock-in mechanisms could support the prolonged ac-
tivation of specific sub-GINPs (e.g., a distal goal
during planning; Baldassarre et al., 2013).
6.1.4. Motivation component: guiding the manipu-
lation of GINPs
The motivation component should guide the ma-
nipulator operations on the sub-GINPs both di-
rectly and indirectly via goals.
Low-level moti-
vations (e.g., extrinsic motivations) could directly
bias the operations of the manipulator sub-GINPs.
In addition, motivations could guide the forma-
tion/activation of goal representations, in turn
guiding the manipulator to perform goal-directed
manipulations (e.g., during planning or problem
solving; Santucci et al., 2016; Rueckert et al., 2016;
Basanisi et al., 2020; Baldassarre et al., 2013). Mo-
tivations could also bias the acquisition of task-
directed representations and not only guide their
selection (Granato et al., 2021).
Different types of motivations could play differ-
ent roles.
Extrinsic motivations could be imple-
mented with different mechanisms assigning valence
to stimuli and other cognitive contents based on
primary (innate) values related to the acquisition
of material resources (Tye, 2018).
These valence
should bias both selection and learning processes.
On this basis, Pavlovian associative learning mech-
anisms could assign a secondary valence to previ-
ously neutral stimuli (as done in Mannella et al.,
2016; Mattera et al., 2020).
Social motivations
could work on the basis of similar mechanisms but
rely on social stimuli having a primary valence (e.g.,
see Alfieri et al., 2022).
Intrinsic
motivations
would
require
different
mechanisms where the primary-valence stimuli orig-
inate in the system itself when it acquires knowl-
edge and skills (Baldassarre, 2011; Baldassarre
and Mirolli, 2013).
Novelty could be supported
by pattern recognition mechanisms while surprise
by mechanisms based on predictors (Barto et al.,
2013), similarly to what might happens in the hip-
pocampus (Kumaran and Maguire, 2007).
Com-
petence mechanisms could rely on ‘goal-matching
processes’ that compare the pursued goal with the
achieved world states (Baldassarre et al., 2013.
Emotions have more rarely been the subject of
computational models (Marsella et al., 2010). Mod-
els of emotional ‘appraisal’ could be for example
be used to evaluate the outcomes of internal sim-
ulations happening within the architecture (Paiva
et al., 2012).
6.2. Towards AI systems and robotic architectures
inspired by the GARIM theory
This section illustrates the indications that the
GARIM theory can provide to enhance the auton-
omy and effectiveness of AI and robotic systems.
6.2.1. Adaptive functions of conscious and goal-
oriented states for AI and robotic systems
The introduction of consciousness-like and goal-
oriented processes into AI and robotic architectures
could contribute to enhance several aspects of them.
The following paragraphs consider the major limi-
tations of the current AI and robotic systems, show-
ing how mechanisms and functions inspired by the
GARIM theory might contribute to face them.
Flexibility. Flexibility is still a relevant limitation
of current AI systems. In particular, they are usu-
ally incapable of coping with new tasks or new con-
ditions and to solve problems with partial knowl-
edge (Hassabis et al., 2017; Lake et al., 2017; Mar-
cus and Davis, 2019), although things might be
changing with the most recent Large Language
Models (LLM) discussed below. The GARIM the-
ory proposes that human behaviour flexibility de-
pends on the brain capacity to internally manip-
ulate the representations of goal-relevant elements
(e.g., objects, goals, actions). These manipulations
give humans the ability to actively adjust and inte-
grate the knowledge gained in previous experiences
to cope with novel goals and conditions and to im-
prove the alignment of behaviour to goals and of
these to ultimate values. Therefore, the integration
of mechanisms inspired by the GARIM theory could
boost the flexibility of AI and robotic architectures.
27


## Page 28


Learning speed. The learning efficiency is a second
major limitation of current AI and robotic systems.
In particular, they are time consuming and need
very large datasets to learn (Lake et al., 2017; Mar-
cus and Davis, 2019; Ullman, 2019). The GARIM
theory introduces the super-ordinate representation
manipulation function called Conscious Knowledge
Transfer (CKT). Based on the four GARIM op-
erations (abstraction, specification, decomposition,
composition), CKT should make the system able
to transfer knowledge between tasks and domains.
In particular, the introduction of this function into
AI and robotic architectures could accelerate their
learning processes. In addition, it might allow the
solution of tasks with few or no direct experience
on them (‘few/zero shot learning’, Pourpanah et al.,
2022).
Creativity. Creativity and imagination are strongly
limited in AI/robotic systems (Hassabis et al., 2017;
Lake et al., 2017; Marcus and Davis, 2019). The
GARIM theory postulates that goal-directed top-
down manipulations of perceptual and working-
memory representations lead to generative and cre-
ative processes.
The development of AI/robotic
architectures with these manipulation functions
should boost their skills, for example making them
able to elaborate creative solutions for problems.
Human-AI value alignment. Many authors argue
that AI systems should be able to interact safely
with humans, aligning their values and goals with
ours (Harari, 2016; Bostrom, 2014; Gabriel, 2020).
The GARIM theory provides some suggestions on
how this could be done. First, new architectures
based on the GARIM theory would be more flexible,
thus facilitating interactions with humans.
Mre-
over, they would have a motivation component,
thus facilitating the design of human-like value sys-
tems (Dignum, 2018). In addition, they would be
able to consider emotional issues, an important ele-
ment to have appropriate interactions with humans
(Huang et al., 2019).
Finally, the very function
of consciousness proposed by the GARIM theory
(alignment of own actions, goals and values through
the manipulation of internal representations) might
provide AI systems/robotic architectures with the
fundamental cognitive abilities to align with human
values (Brian, 2020).
6.2.2. Cognitive Robotics and Machine Conscious-
ness: designing AI and Robotics systems on
the basis of the GARIM theory
This section gives initial indications on how im-
plementing functions inspired by the GARIM the-
ory in current AI/robotic algorithms and architec-
tures.
Figure 8 illustrates a general scheme that
might be followed to design specific AI and robotics
systems based on the GARIM theory.
Perceptual component. This component should im-
plement abstraction and generativity mechanisms.
Regarding abstraction, ‘convolutional neural net-
works’ (CNNs; Goodfellow et al., 2017) and ‘deep
belief networks’ (DBNs; Hinton et al., 2006; Hin-
ton, 2002) are suitable approaches.
Indeed, they
can learn ‘features’ of input patterns at multi-
ple levels of abstraction.
Regarding generativity,
three relevant ‘families’ of models have been pro-
posed (Goodfellow et al., 2017): DBNs, considered
above, ‘variational autoencoders’ (VAEs; Kingma
and Welling, 2013), and ‘generative adversarial net-
works’ (GANs; Goodfellow et al., 2014).
Although these models can be exploited to solve
several tasks, they still show limitations that might
prevent their use to implement manipulative func-
tions proposed by the GARIM theory. CNNs are
not generative and are trained with a supervised
algorithm. This feature makes these networks less
useful for autonomous agents. VAEs are based on
two distinct components, a bottom-up abstraction
component (‘encoder’) and a top-down generative
component (‘decoder’).
As a consequence, they
cannot easily integrate manipulative processes be-
cause they would require two distinct manipula-
tors. GANs are formed by a ‘discriminator com-
ponent’ and a ‘generator component’: the latter
could be useful to implement manipulative func-
tionalities, while the former could be used to dis-
tinguish between imagined and perceived stimuli.
Unfortunately, the ‘generative stochastic engine’ of
both VAEs and GANs is limited. In particular, it
is located in the latent space of VAEs and in the
discriminator of GANs.
Therefore, the two net-
works cannot have generativity at multiple levels
of abstraction.
Interestingly, DBNs show a bidi-
rectional architecture implementing both bottom-
up abstraction and top-down generative processes.
Moreover, they show two interesting features: (a)
their ‘generative engine’ is distributed into all its
stochastic-units, thus supporting generativity at
multiple levels of abstraction and (b) their unsuper-
28


## Page 29


Figure 8:
Blueprint of an AI architecture based on the GARIM theory. The figure shows some AI algorithms that could be
used to implement the functions of the GARIM theory components. Bold text: names of the components; Plain text: functions;
Italics text, in brackets: algorithms/models; Dash-highlighted text: representations on which consciousness processes operate.
vised learning mechanisms can be integrated with
reinforcement learning mechanisms, thus balancing
representational requirements and task demands
(Granato et al., 2022b).
Working
memory
component. This
component
should support the information reverberation in the
absence of the corresponding patterns from sensors
or internal processes.
The component should be
able to learn which patterns to store and which not,
also on the basis of goals.
RNNs, introduced above, are a first powerful tool
usable to implement working memory. This capac-
ity is based on an architecture having re-entrant
connections and thus capable of dynamically stor-
ing information (Choi et al., 2018).
Long-short
term memories (LSTM; Hochreiter and Schmid-
huber, 1997) are networks based on units with a
‘gated self-connection’ and gates in input and out-
put connections. The opening/closing of the gates
can upload/download information in the unit, mak-
ing it capable of storing memories for long times.
These networks are commonly used to solve classi-
fication and regression tasks with input sequences.
However, they have recently been updated with ad-
ditional mechanisms that can support deliberative
(goal-directed) processes as needed by the GARIM
theory (e.g., see Jung et al., 2019b). Neural Turing
machines (Graves et al., 2014; Wayne et al., 2018)
are neural networks that support deliberative pro-
cesses. These networks use ‘working memory slots’
that are based on numerical vectors. These slots are
read/written by ‘neural heads’ that are trainable
with gradient-based algorithms. These features al-
low these networks to implement trainable logic-like
reasoning.
However, the pre-defined level of ab-
straction of these memory slots make them unsuit-
able to implement the GARIM operations of com-
position/decomposition, thus limiting their flexibil-
ity.
Manipulator component. This component should
implement two main functions.
First, it should
support the autonomous learning and performance
of the goal-directed manipulation of representations
(states, goals, actions, etc.). Second, it should sup-
port the goal-directed adaptation/tuning of these
manipulation processes.
A number of AI mech-
anisms, introduced above, can be used to imple-
ment working memories and ‘neural heads’, or other
mechanisms, to ‘read/write’ such memories. These
mechanisms can be important means to implement
the manipulation of representations.
The implementation of goal-directed processes
29


## Page 30


also requires the performance of a number of
structured and temporised operations, such as the
goals/sub-goals activation/de-activation.
Exam-
ples of these are: the generation and search of cor-
rect action sequences, the prediction of actions out-
comes, the exchange of information between the
different components of the system. These opera-
tions are relatively easy to implement with symbolic
representations and programming controls (e.g., ‘if-
then’ and ‘loop’ operations; Russell and Norvig,
2016) but very difficult to implement with neu-
ral mechanisms. Current systems thus tend to be
based on hybrid neural/symbolic mechanisms. This
is an important open problem as the non-neural
parts of the models could obstacle the information
integration capabilities of the system. Hybrid sys-
tems (Sun, 2016; Konidaris et al., 2018; Oddi et al.,
2019) implement low-level cognitive processes based
on neural representations and learning algorithms.
At the same time, they implement high-level cog-
nitive processes based on symbolic representations.
This double representation format allows them, for
example, to implement symbolic PDDL planning
while using neural mechanisms to implement sen-
sorimotor processes.
These approaches have lim-
itations for our scope.
In particular, they intro-
duce inhomogeneous representations at the low and
high representation levels, requiring different mech-
anisms to manipulate them.
Neural Turing ma-
chines and models like MERLIN (Graves et al.,
2014; Wayne et al., 2018) use memory slots and neu-
ral heads to perform complex tasks that require the
achievement of multiple subgoals. This approach
is mainly used to solve single reactive tasks but
it can also be used to solve deliberative problems
(Chaplot et al., 2021).
Neurosymbolic AI (for a
review see Garcez and Lamb, 2020), and in par-
ticular recent visual planning systems (Jung et al.,
2019b; Nair et al., 2018), perform planning task on
the basis of goal-directed processes and distributed
representations (states, goals, actions, etc.). These
processes allow high flexibility, supporting gener-
alisation capabilities that cannot be achieved by
symbolic planning/problem solving. However, for
now they cannot compose/decompose the manipu-
lated elements. Transformers (Vaswani et al., 2017)
implement neural internal attention mechanisms
and dynamic circuits.
Their memory and atten-
tion units are integrated within the trainable input-
output layers of neural networks. These models are
very effective in recalling any learnt or acquired in-
formation, even if experienced much earlier. Trans-
formers have been mainly used to successfully solve
natural language processing tasks but require mas-
sive supervised-learning training (Blakeman and
Mareschal, 2022). These systems have the poten-
tial to also support deliberative processes (Chaplot
et al., 2021) and to be hybridised with sensorimo-
tor components (Driess et al., 2023). In addition,
they have been indicated as relevant to implement
consciousness-like processes (Bengio, 2017). How-
ever, the functioning of AI systems based on trans-
formers is still poorly understood (Ag¨uera y Arcas,
2022; Srivastava and al., 2022). In this respect, in
the future it might be interesting to evaluate if ma-
nipulation operations similar to those proposed by
the GARIM theory actually take place within AI
systems based on transformers.
Motivation component. Extrinsic motivations are
usually emulated trough reward signals (Sutton
and Barto, 1998). Moreover, ‘pseudo-rewards’ can
be used to guide model-based hierarchical rein-
forcement learning based on goal-matching events
(Botvinick et al., 2008).
Intrinsic motivations have demonstrated to effec-
tively support the autonomous acquisition of knowl-
edge of robots (Baldassarre and Mirolli, 2013). In-
deed, intrinsic motivation mechanisms can drive the
investigation and learning of novel/surprising ex-
periences, leading to the acquisition of new state
representations and models (Schmidhuber, 1991;
Oudeyer et al., 2007; Barto et al., 2013; Cartoni
and Baldassarre, 2018). Moreover, they can lead
to the acquisition of ‘intrinsic goals’ (autonomously
found) and motor skills to accomplish them (Barto
et al., 2004; Santucci et al., 2016; Nair et al., 2018).
Intrinsic motivations are commonly used to guide
intelligent machines and robots to seek knowledge
in the external environment. Instead, according to
the GARIM proposal they could guide the internal
building of the knowledge that the agent lacks.
There are few AI approaches that emulate the
generation of emotions (for reviews see Paiva et al.,
2012; Mirolli et al., 2010; Sun et al., 2016). These
models could be used as a starting point for imple-
menting emotion-based evaluation of internal rep-
resentations.
Open challenges: what is missing?. The two ar-
chitecture schemes we proposed for guiding the
development of computational models (Figure 7)
and AI/robotic architectures (Figure 8) include
the main elements that should support conscious
30


## Page 31


and flexible artificial systems. For example, they
include the main features of machine conscious-
ness systems (self-modelling, information broad-
casting, higher-level representations, attention pro-
cesses, and information integration; Reggia, 2013).
Moreover, they include the fundamentals axioms
of Machine Consciousness (world models, imagina-
tion, attention, planning, and affective evaluation;
Aleksander, 1995) . However, critical elements for
building conscious machines may still be missing.
First, the four macro-systems proposed by the
GARIM theory require important low-level func-
tions to support the emergence of GINPs. For ex-
ample, the brain shows a high capacity for gen-
erating associations and avoiding unbounded ac-
tivations. These capacities are based on grid-like
circuits and finely regulated inhibitory processes.
These features are missing in common artificial neu-
ral network architectures, which favour bottom-
up/top-down directional information flows with few
recurrences (Lynn and Bassett, 2019). Second, the
brain exhibits highly dynamic processes that could
be based on fixed-point/cycle/strange attractors.
ANNs are still not able to fully emulate these pro-
cesses. These elements might be needed to imple-
ment the GARIM operations on sub-GINPs (Break-
spear, 2017).
Third, the flexible selection func-
tions implemented by the basal ganglia-thalamo-
cortical loops are only partially captured by cur-
rent neural systems. Fourth, strongly-coupled sen-
sorimotor loops engaged by animals with the en-
vironment are often absent in AI systems. More-
over, current robots have still a very limited au-
tonomy to interact with the environment. Agent-
environment interactions might instead be very im-
portant to acquire internal representations strongly
coupled with the real environment.
Last, till re-
cently AI/robotic systems lacked the capacity to
suitably integrate language with sensorimotor ex-
perience, in particular they lacked a meaning and
understanding grounded on sensorimotor experi-
ence.
Recently, however, large language models
have been argued to acquire some meaning even
without sensorimotor grounding (Yun et al., 2021;
Abdou et al., 2021; Ag¨uera y Arcas, 2022; Srivas-
tava and al., 2022), and grounding might be re-
alised very soon with systems integrating language
and sensorimotor capabilities (Driess et al., 2023).
The fact that these models are based on transform-
ers, which might perform operations very similar
to the representation manipulations postulated by
the GARIM theory, hence represents an interesting
topic for future investigations.
Overall, the realisation and integration of all
these elements is still a great open challenge. Much
of the flexibility of the brain is based on its highly
structured and integrated architecture, which seems
difficult to reproduce in artificial systems. Indeed,
the brain integrates habitual and goal-directed pro-
cesses and it is the product of a long evolution-
ary process that is hard to reproduce in machines
(Baldassarre et al., 2017; Baldassarre and Granato,
2020; Caligiore et al., 2019; Ullman, 2019). Produc-
ing conscious intelligent machines without relying
on such a highly integrated architecture is there-
fore a great challenge.
7. Conclusions
In this work we introduce the Goal-Aligning Rep-
resentation Internal Manipulation (GARIM) the-
ory of flexible goal-directed cognition and con-
sciousness.
The central idea of the GARIM the-
ory is that conscious states support the active
manipulation of internal representations, making
them more aligned with the goals pursued.
This
goal-oriented alignment leads to the generation
of the necessary knowledge to face novel situa-
tions and goals and to make goal-directed be-
haviour more flexible and effective. The GARIM
theory postulates that a conscious goal-directed
behaviour is characterised by five distinctive el-
ements.
First, consciousness serves the adapta-
tion of goal-directed behaviours.
In particular,
consciousness processes support the goal-aligning
manipulation of internal representations, in turn
boosting the flexibility of goal-directed behaviour.
Second, the theory hypotheses the existence of
‘Goal-based Integrated Neural Patterns’ (GINPs).
These are distributed active neural representations
that (a) are consciously perceived and thus in-
tentionally manipulable (consciousness level), and
(b) are closely related the pursued goals (goal-
relevance).
Different levels of these two dimen-
sions lead to representations characterised by dif-
ferent levels of consciousness (Non-GINPs, Pre-
GINPs, Temp-GINPs, GINPs) and representational
proprieties (e.g., information integration). Third,
the GARIM theory specifies that goal-directed ma-
nipulations rely on four key ‘components’, namely
four partially overlapping anatomo-functional brain
macro systems (perceptual working-memory, ab-
stract working-memory, internal manipulator, mo-
tivational component).
Fourth, previous systems
31


## Page 32


give rise to four classes of computational opera-
tions (GARIM operations) that support the repre-
sentation manipulations (abstraction, specification,
decomposition, composition).
Fifth and last, the
GARIM theory introduces the concept of ‘GARIM
agency’, a sense of agency that emerges from con-
scious goal-directed processes and, in particular,
representation manipulations.
These manipula-
tions lead to the generation of a subjective inter-
nal reality supported by three key features: self-
model, emotional/perceptual vividness, and manip-
ulation control. On the basis of the GARIM agency
and its key features, the theory proposes different
levels of conscious states (from reactive behaviours
to highly flexible goal-directed behaviours). In ad-
diction to clarifying neuro-computational processes
at the basis of conscious and flexible goal-directed
behaviours, the GARIM theory has both scien-
tific and technological implications. For example,
it clarifies some aspects of subjective experience
and agency, also introducing a potential quanti-
tative scale. Moreover, it accounts for several el-
ements of current theories of consciousness, inte-
grating them into a common functional and com-
putational framework that focuses on goal-directed
processes. The GARIM theory also generates in-
sights for experimental and clinical fields. In par-
ticular, it proposes clinical insights, experimental
predictions and new ideas for building experimental
protocol of goal-directed behaviour and conscious-
ness. At last, the GARIM theory furnishes indica-
tions for building new computational models, and
AI/robotic architectures. In particular, it proposes
that conscious goal-aligning manipulations of rep-
resentations could enable AI/robotic architectures
to achieve human-like flexibility and general intel-
ligence.
8. Acknowledgements
This work has received funding from the Eu-
ropean Union’s Horizon 2020 Research and In-
novation
Program
with
the
projects
‘GOAL-
Robots – Goal-based Open-ended Autonomous
Learning Robots’, GA N. 713010, ‘HBP – Hu-
man Brain Project SGA3’, GA N. 945539; and
from the Horizon Europe Program with projects
‘PILLAR-Robots - Purposeful Intrinsically moti-
vated Lifelong Learning Autonomous Robots’, GA
N. 101070381, and ‘EBRAINS-Italy - European
Brain ReseArch INfrastructureS Italy’, PNRR N.
IR000001, CUP B51E22000150006.
We thank
Emilio Cartoni and Andrea Mattera for the useful
feedback on the early versions of the manuscript.
References
Aaronson, S., 2014. Why i am not an integrated information
theorist (or, the unconscious expander). Shtetl Optimized:
The Blog of Scott Aaronson .
Abdou, M., Kulmizev, A., Hershcovich, D., Frank, S.,
Pavlick, E., Søgaard, A., 2021. Can Language Models En-
code Perceptual Structure Without Grounding? A Case
Study in Color. Technical Report. arXiv. doi:10.48550/
arXiv.2109.06129, arXiv:2109.06129.
Aleksander, I., 1995.
Artificial neuroconsciousness an up-
date, in: International Workshop on Artificial Neural Net-
works, Springer. pp. 566–583.
Aleksander, I., Dunmall, B., 2003. Axioms and tests for the
presence of minimal consciousness in agents. Journal of
Consciousness Studies 10, 7–18.
Alfieri, V., Mattera, A., Baldassarre, G., 2022. Neural cir-
cuits underlying social fear in rodents:
An integrative
computational model. Frontiers in systems neuroscience
16, 841085. doi:10.3389/fnsys.2022.841085.
Amaral, D.G., 2002. The primate amygdala and the neuro-
biology of social behavior: implications for understanding
social anxiety. Biol Psychiatry 51, 11–17.
Anderson, M.L., 2003. Embodied cognition: A field guide.
Artificial intelligence 149, 91–130.
Arber, S., Costa, R.M., 2022.
Networking brainstem and
basal ganglia circuits for movement. Nature reviews Neu-
roscience 23, 342–360. doi:10.1038/s41583-022-00581-w.
Ag¨uera y Arcas, B., 2022. Do large language models under-
stand us? Daedalus 151, 183–197.
Aru, J., Bachmann, T., Singer, W., Melloni, L., 2012. Dis-
tilling the neural correlates of consciousness. Neuroscience
& Biobehavioral Reviews 36, 737–746.
Atherton, M., Zhuang, J., Bart, W.M., Hu, X., He, S., 2003.
A functional mri study of high-level cognition. i. the game
of chess. Cognitive Brain Research 16, 26–31.
Baars, B.J., 1997.
In the theatre of consciousness. global
workspace theory, a rigorous scientific theory of conscious-
ness. Journal of Consciousness Studies 4, 292–309.
Baars, B.J., 2005.
Global workspace theory of conscious-
ness: toward a cognitive neuroscience of human experi-
ence. Progress in brain research 150, 45–53.
Baars, B.J., Franklin, S., Ramsoy, T.Z., 2013.
Global
workspace dynamics: cortical ”binding and propagation”
enables conscious contents. Frontiers in psychology 4.
Baars, B.J., Ramsøy, T.Z., Laureys, S., 2003. Brain, con-
scious experience and the observing self. Trends in neu-
rosciences 26, 671–675.
Baldassarre, G., 2011. What are intrinsic motivations? a bi-
ological perspective, in: Cangelosi, A., Triesch, J., Fasel,
I., Rohlfing, K., Nori, F., Oudeyer, P.Y., Schlesinger,
M., Nagai, Y. (Eds.), Proceedings of the International
Conference on Development and Learning and Epigenetic
Robotics (ICDL-EpiRob-2011), Frankfurt Institute of Ad-
vanced Studies (FIAS). IEEE, New York, NY. pp. e1–8.
Frankfurt am Main, Germany, 24–27/08/11.
Baldassarre, G., Granato, G., 2020. Goal-directed manip-
ulation of internal representations is the core of general-
domain intelligence. Journal of Artificial General Intelli-
gence 11, 19–23.
32


## Page 33


Baldassarre, G., Mannella, F., Fiore, V.G., Redgrave, P.,
Gurney, K., Mirolli, M., 2013.
Intrinsically motivated
action-outcome learning and goal-based action recall: A
system-level bio-constrained computational model. Neu-
ral Networks 41, 168–187.
Baldassarre, G., Mannella, F., Santucci, V.G., Somogyi, E.,
Jacquey, L., Hamilton, M., O’Regan, J.K., 2018. Action-
outcome contingencies as the engine of open-ended learn-
ing:
computational models and developmental experi-
ments, in: The 8th IEEE International Conference on De-
velopment and Learning and Epigenetic Robotics (ICDL-
EpiRob2018), pp. E1–8. Tokyo, Japan, 16–20 September
2018.
Baldassarre, G., Mirolli, M. (Eds.), 2013. Intrinsically moti-
vated learning in natural and artificial systems. Springer,
Berlin. Cost 91.62 euros, pp. 458, 82 illustrations, 55 il-
lustrations in color.
Baldassarre, G., Santucci, V.G., Cartoni, E., Caligiore,
D., 2017.
The architecture challenge: Future artificial-
intelligence systems will require sophisticated architec-
tures, and knowledge of the brain might guide their
construction.
Behavioral and Brain Sciences 40, e254.
doi:10.1017/s0140525x17000036.
Balleine, B.W., Dickinson, A., 1998. Goal-directed instru-
mental action:
contingency and incentive learning and
their cortical substrates.
Neuropharmacology 37, 407–
419.
Balleine, B.W., Ostlund, S.B., 2007. Still at the choice-point:
action selection and initiation in instrumental condition-
ing.
Ann N Y Acad Sci 1104, 147–171.
doi:10.1196/
annals.1390.006.
Barak, O., Tsodyks, M., 2014. Working models of working
memory. Current Opinion in Neurobiology 25, 20–24.
Barto, A.G., Mirolli, M., Baldassarre, G., 2013. Novelty or
surprise? Frontiers in Psychology – Cognitive Science 4,
e1–15. Edited by: Tom Stafford, University of Sheffield,
UK Reviewed by: Karl Friston, University College Lon-
don, UK; Nathan F.Lepora, The University of Sheffield,
UK.
Barto, A.G., Singh, S., Chentanez, N., 2004. Intrinsically
motivated learning of hierarchical collections of skills, in:
Triesch, J., Jebara, T. (Eds.), International Conference
on Developmental Learning (ICDL2004), New York, NY.
pp. 112–119.
Basanisi, R., Brovelli, A., Cartoni, E., Baldassarre, G.,
2020.
A spiking neural-network model of goal-directed
behaviour. Plos Computational Biology .
Bechara, A., Damasio, A.R., 2005. The somatic marker hy-
pothesis: A neural theory of economic decision. Games
and economic behavior 52, 336–372.
Bengio, Y., 2017. The consciousness prior. arXiv preprint
arXiv:1709.08568 .
Benson, N., Hulac, D.M., Kranzler, J.H., 2010.
Inde-
pendent examination of the wechsler adult intelligence
scale—fourth edition (wais-iv):
what does the wais-iv
measure? Psychological Assessment 22, 121.
Berg, E.A., 1948. A simple objective technique for measuring
flexibility in thinking. The Journal of general psychology
39, 15–22.
Berke, J.D., 2018.
What does dopamine mean?
Nature
neuroscience 21, 787–793.
Blakeman, S., Mareschal, D., 2022.
Selective particle at-
tention: Rapidly and flexibly selecting features for deep
reinforcement learning. Neural Networks 150, 408–421.
Borghi, A.M., Cimatti, F., 2010. Embodied cognition and
beyond: acting and sensing the body. Neuropsychologia
48, 763–773.
Bortolon, C., Macgregor, A., Capdevielle, D., Raffard, S.,
2018. Apathy in schizophrenia: A review of neuropsycho-
logical and neuroanatomical studies.
Neuropsychologia
118, 22–33.
Bostrom, N., 2014.
Superintelligence:
Paths, Dangers,
Strategies. Oxford University Press, Oxford.
Botvinick, M.M., Niv, Y., Barto, A., 2008.
Hierarchi-
cally organized behavior and its neural foundations: A
reinforcement-learning perspective. Cognition 113, 262–
280.
Braver, T.S., Bongiolatti, S.R., 2002. The role of frontopo-
lar cortex in subgoal processing during working memory.
Neuroimage 15, 523–536.
Breakspear, M., 2017. Dynamic models of large-scale brain
activity. Nature Neuroscience 20, 340–352.
Brian, C., 2020. The Alignment Problem: Machine Learning
and Human Values. W.W. Norton & Company, New York.
Brown, R., Lau, H., LeDoux, J.E., 2019.
Understanding
the higher-order approach to consciousness.
Trends in
cognitive sciences 23, 754–768.
Bubeck, S., Chandrasekaran, V., Eldan, R., Gehrke, J.,
Horvitz, E., Kamar, E., Lee, P., Lee, Y.T., Li, Y., Lund-
berg, S., Nori, H., Palangi, H., Ribeiro, M.T., Zhang, Y.,
2023. Sparks of artificial general intelligence: Early ex-
periments with gpt-4. doi:10.48550/ARXIV.2303.12712.
Burkart, J.M., Schubiger, M.N., van Schaik, C.P., 2017. The
evolution of general intelligence.
Behavioral and Brain
Sciences 40.
Cabanac, M., 2002. What is emotion? Behavioural processes
60, 69–83.
Caligiore, D., Arbib, M.A., Miall, C.R., Baldassarre, G.,
2019. The super-learning hypothesis: Integrating learn-
ing processes across cortex, cerebellum and basal ganglia.
Neuroscience and Biobehavioral Reviews 100, 19–34.
Carter, O., Hohwy, J., Van Boxtel, J., Lamme, V., Block,
N., Koch, C., Tsuchiya, N., 2018. Conscious machines:
Defining questions. Science 359, 400–400.
Cartoni, E., Baldassarre, G., 2018. Autonomous discovery
of the goal space to learn a parameterized skill. Preprint
arXiv 1805.07547v1. arXiv. 19 May 2018.
Cerullo, M.A., 2015. The Problem with Phi: A Critique of
Integrated Information Theory. PLoS Comput Biol 11,
e1004286.
Chalmers, D.J., 1995. Facing up to the problem of conscious-
ness. Journal of consciousness studies 2, 200–219.
Chaplot, D.S., Pathak, D., Malik, J., 2021. Differentiable
Spatial Planning using Transformers.
ArXiv Preprint
abs/2112.01010.
Chelazzi, L., Perlato, A., Santandrea, E., Della Libera, C.,
2013.
Rewards teach visual selective attention.
Vision
research 85, 58–72.
Chiappe, D., MacDonald, K., 2005.
The evolution of
domain-general mechanisms in intelligence and learning.
The Journal of general psychology 132, 5–40.
Choi, M., Matsumoto, T., Jung, M., Tani, J., 2018. Gener-
ating Goal-Directed Visuomotor Plans Based on Learning
Using a Predictive Coding-type Deep Visuomotor Recur-
rent Neural Network Model. arXiv abs/1803.02578v2.
Christoff,
K.,
Irving,
Z.C.,
Fox,
K.C.,
Spreng,
R.N.,
Andrews-Hanna, J.R., 2016.
Mind-wandering as spon-
taneous thought: a dynamic framework. Nature Reviews
Neuroscience 17, 718–731.
Chrysikou,
E.G.,
Motyka,
K.,
Nigro,
C.,
Yang,
S.I.,
33


## Page 34


Thompson-Schill, S.L., 2016. Functional fixedness in cre-
ative thinking tasks depends on stimulus modality. Psy-
chology of Aesthetics, Creativity, and the Arts 10, 425.
Clark, A., 2013. Whatever next? predictive brains, situated
agents, and the future of cognitive science.
Behavioral
and brain sciences 36, 181–204.
Cleeremans, A., 2007. Consciousness: the radical plasticity
thesis. Progress in brain research 168, 19–33.
Cleeremans, A., 2011. The radical plasticity thesis: how the
brain learns to be conscious. Frontiers in psychology 2,
86.
Cleeremans, A., Achoui, D., Beauny, A., Keuninckx, L.,
Martin, J.R., Mu˜noz-Moldes, S., Vuillaume, L., De Heer-
ing, A., 2020. Learning to be conscious. Trends in cogni-
tive sciences 24, 112–123.
Cowey, A., Stoerig, P., 1995. Blindsight in monkeys. Nature
373, 247–249.
Damasio, A.R., 1989. The brain binds entities and events by
multiregional activation from convergence zones. Neural
Computation 1, 123–132.
Damasio, A.R., 1998. Emotion in the perspective of an inte-
grated nervous system. Brain research reviews 26, 83–86.
Damasio, A.R., Meyer, K., 2009a.
Consciousness:
An
overview of the phenomenon and of its possible neural
basis. The neurology of consciousness: Cognitive neuro-
science and neuropathology , 3–14.
Damasio, A.R., Meyer, K., 2009b.
Consciousness:
An
overview of the phenomenon and of its possible neural
basis. The neurology of consciousness: Cognitive neuro-
science and neuropathology , 3–14.
Dayan, P., Abbott, L.F., 2001.
Theoretical Neuroscience.
The MIT Press, Cambridge, MA.
Dehaene, S., Changeux, J.P., 2005.
Ongoing spontaneous
activity controls access to consciousness:
a neuronal
model for inattentional blindness. PLoS biology 3, e141.
doi:10.1371/journal.pbio.0030141.
Dehaene, S., Changeux, J.P., 2011. Experimental and the-
oretical approaches to conscious processing. Neuron 70,
200–227.
Dehaene, S., Changeux, J.P., Naccache, L., 2011. The global
neuronal workspace model of conscious access: from neu-
ronal architectures to clinical applications, in:
Char-
acterizing consciousness:
from cognition to the clinic?.
Springer, pp. 55–84.
Dehaene, S., Kerszberg, M., Changeux, J.P., 1998a. A neu-
ronal model of a global workspace in effortful cognitive
tasks. Proceedings of the National Academy of Sciences
of the United States of America 95, 14529–14534.
Dehaene, S., Kerszberg, M., Changeux, J.P., 1998b. A neu-
ronal model of a global workspace in effortful cognitive
tasks. Proceedings of the national Academy of Sciences
95, 14529–14534.
Dehaene, S., Lau, H., Kouider, S., 2017. What is conscious-
ness, and could machines have it?
Science (New York,
N.Y.) 358, 486–492. doi:10.1126/science.aan8871.
Dehaene, S., Naccache, L., 2001. Towards a cognitive neuro-
science of consciousness: basic evidence and a workspace
framework. Cognition 79, 1–37.
Dehaene, S., Sergent, C., Changeux, J.P., 2003. A neuronal
network model linking subjective reports and objective
physiological data during conscious perception. Proceed-
ings of the National Academy of Sciences 100, 8520–8525.
Del Pin, S.H., Sk´ora, Z., Sandberg, K., Overgaard, M.,
Wierzcho´n, M., 2021. Comparing theories of conscious-
ness: why it matters and how to do it. Neuroscience of
Consciousness 2021, niab019.
Delatour, B., Gisquet-Verrier, P., 2000. Functional role of
rat prelimbic-infralimbic cortices in spatial memory: evi-
dence for their involvement in attention and behavioural
flexibility. Behavioural brain research 109, 113–128.
Diamond, A., 2013. Executive functions. Annu Rev Psychol
64, 135–168.
Diehl, P.U., Cook, M., 2015. Unsupervised learning of digit
recognition using spike-timing-dependent plasticity. Fron-
tiers in Computational Neuroscience 9, 99. doi:10.3389/
fncom.2015.00099.
Dignum, V., 2018. Ethics in artificial intelligence: introduc-
tion to the special issue. Ethics and Information Technol-
ogy 20, 1–3.
Doerig, A., Schurger, A., Herzog, M.H., 2021. Hard criteria
for empirical theories of consciousness. Cognitive neuro-
science 12, 41–62.
Donnarumma, F., Costantini, M., Ambrosini, E., Friston,
K., Pezzulo, G., 2017. Action perception as hypothesis
testing. Cortex 89, 45–60.
Driess, D., Xia, F., Sajjadi, M.S.M., Lynch, C., Chowdh-
ery, A., Ichter, B., Wahid, A., Tompson, J., Vuong, Q.,
Yu, T., Huang, W., Chebotar, Y., Sermanet, P., Duck-
worth, D., Levine, S., Vanhoucke, V., Hausman, K., Tou-
ssaint, M., Greff, K., Zeng, A., Mordatch, I., Florence,
P., 2023. PaLM-E: An Embodied Multimodal Language
Model. Technical Report 2303.03378. arXiv.
Duncker, K., 1945.
On Problem Solving.
Number 58 in
Psychological Monographs, American Psychological As-
sociation.
Ekman, P., Davidson, R.J., 1994. The Nature of emotion:
fundamental questions.
Oxford University Press, New
York.
Ell, S.W., Marchant, N.L., Ivry, R.B., 2006. Focal putamen
lesions impair learning in rule-based, but not information-
integration categorization tasks.
Neuropsychologia 44,
1737–1751.
Ell, S.W., Weinstein, A., Ivry, R.B., 2010. Rule-based cate-
gorization deficits in focal basal ganglia lesion and parkin-
son’s disease patients. Neuropsychologia 48, 2974–2986.
Fernandez-Duque, D., Baird, J.A., Posner, M.I., 2000. Exec-
utive attention and metacognitive regulation. Conscious-
ness and cognition 9, 288–307.
Ferrucci, D.A., 2012. Introduction to “this is watson”. IBM
Journal of Research and Development 56, 1–1.
Fiore, V.G., Sperati, V., Mannella, F., Mirolli, M., Gurney,
K., Firston, K., Dolan, R.J., Baldassarre, G., 2014. Keep
focussing: striatal dopamine multiple functions resolved
in a single mechanism tested in a simulated humanoid
robot.
Frontiers in Psychology 5, e1–17.
doi:10.3389/
fpsyg.2014.00124.
Fornazzari, L., Farcnik, K., Smith, I., Heasman, G.A., Ichise,
M., 1992. Violent visual hallucinations and aggression in
frontal lobe dysfunction: clinical manifestations of deep
orbitofrontal foci.
The Journal of Neuropsychiatry and
Clinical Neurosciences .
Fox, K.C., Shi, L., Baek, S., Raccah, O., Foster, B.L., Saha,
S., Margulies, D.S., Kucyi, A., Parvizi, J., 2020. Intrinsic
network architecture predicts the effects elicited by in-
tracranial electrical stimulation of the human brain. Na-
ture human behaviour 4, 1039–1052.
Franklin, S., Strain, S., Snaider, J., McCall, R., Faghihi, U.,
2012.
Global workspace theory, its lida model and the
underlying neuroscience. Biologically Inspired Cognitive
Architectures 1, 32–43.
34


## Page 35


Friston,
K.,
2018.
Am i self-conscious?(or does self-
organization entail self-consciousness?). Frontiers in psy-
chology 9, 579.
Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P.,
Pezzulo, G., et al., 2016. Active inference and learning.
Neuroscience & Biobehavioral Reviews 68, 862–879.
Frith, C., 1996.
The role of the prefrontal cortex in self-
consciousness: the case of auditory hallucinations. Philo-
sophical Transactions of the Royal Society of London. Se-
ries B: Biological Sciences 351, 1505–1512.
Frith, C.D., 2007. The social brain?
Philosophical Trans-
actions of the Royal Society B: Biological Sciences 362,
671–678.
Fuster, J.M., 2008. The prefrontal cortex. Fourth ed., Else-
vier, Oxford.
Fuster, J.M., Bressler, S.L., 2015. Past makes future: role
of pfc in prediction. Journal of cognitive neuroscience 27,
639–654.
Gabriel, I., 2020. Artificial intelligence, values, and align-
ment.
Minds and machines 30, 411–437.
doi:10.1007/
s11023-020-09539-2.
Gamez, D., 2008. Progress in machine consciousness. Con-
sciousness and cognition 17, 887–910.
Gamez, D., 2010. Information integration based predictions
about the conscious states of a spiking neural network.
Consciousness and cognition 19, 294–310.
Gangestad, S.W., Grebe, N.M., 2017.
Hormonal systems,
human social bonding, and affiliation. Horm Behav 91,
122–135.
Garbarini, F., Adenzato, M., 2004. At the root of embodied
cognition: cognitive science meets neurophysiology. Brain
and cognition 56, 100–106.
Garcez, A.d., Lamb, L.C., 2020. Neurosymbolic ai: the 3rd
wave. arXiv preprint arXiv:2012.05876 .
Gardner, H.E., 2000. Intelligence reframed: Multiple intelli-
gences for the 21st century. Hachette UK.
Gazzaley, A., Nobre, A.C., 2012.
Top-down modulation:
bridging selective attention and working memory. Trends
in cognitive sciences 16, 129–135.
Goodfellow, I., Bengio, Y., Courville, A., 2017. Deep Learn-
ing. The MIT Press, Boston, MA.
Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B.,
Warde-Farley, D., Ozair, S., Courville, A., Bengio, Y.,
2014. Generative adversarial nets, in: Advances in Neu-
ral Information Processing Systems, pp. 2672–2680.
10
Jun 2014.
Granato, G., Baldassarre, G., 2021. Internal manipulation
of perceptual representations in human flexible cognition:
A computational model. Neural Networks 143, 572–594.
doi:10.1016/j.neunet.2021.07.013.
Granato, G., Borghi, A.M., Baldassarre, G., 2020. A com-
putational model of language functions in flexible goal-
directed behaviour. Scientific reports 10, 1–13.
Granato, G., Borghi, A.M., Mattera, A., Baldassarre, G.,
2022a. A computational model of inner speech support-
ing flexible goal-directed behaviour in autism. Scientific
Reports 12, 14198.
Granato, G., Cartoni, E., Da Rold, F., Mattera, A., Bal-
dassarre, G., 2021.
A Computational Model of Repre-
sentation Learning in the Brain Cortex, Integrating Un-
supervised and Reinforcement Learning. arXiv preprint,
arXiv:2106.03688.
Granato, G., Cartoni, E., Da Rold, F., Mattera, A., Baldas-
sarre, G., 2022b. Integrating unsupervised and reinforce-
ment learning in human categorical perception: A com-
putational model.
PLOS ONE 17, 1–32.
doi:10.1371/
journal.pone.0267838.
Granato, G., Costanzo, R., Borghi, A.M., Mattera, A., Car-
ruthers, S., Rossell, S., Baldassarre, G., . Flexible cog-
nition and inner-speech in schizophrenia spectrum disor-
der: Applying machine learning and modelling in compu-
tational psychiatry .
Graves, A., Wayne, G., Danihelka, I., 2014. Neural Turing
Machines. arXiv preprint 1410.5401.
Gruberger, M., Ben-Simon, E., Levkovitz, Y., Zangen, A.,
Hendler, T., 2011.
Towards a neuroscience of mind-
wandering. Frontiers in human neuroscience 5, 56.
Guilford, J.P., 1967.
The nature of human intelligence.
McGraw-Hill.
Gurney, K., Prescott, T.J., Redgrave, P., 2001. A compu-
tational model of action selection in the basal ganglia. ii.
analysis and simulation of behaviour. Biological Cyber-
netics 84, 411–423.
H¨anggi, J., Br¨utsch, K., Siegel, A.M., J¨ancke, L., 2014. The
architecture of the chess player’s brain. Neuropsychologia
62, 152–162.
Harari, Y.N., 2016. Homo Deus: A brief history of tomorrow.
Random House.
Hartley, A.A., Speer, N.K., 2000. Locating and fractionat-
ing working memory using functional neuroimaging: stor-
age, maintenance, and executive functions.
Microscopy
research and technique 51, 45–53.
Hassabis, D., Kumaran, D., Summerfield, C., Botvinick, M.,
2017. Neuroscience-inspired artificial intelligence. Neuron
95, 245–258. doi:10.1016/j.neuron.2017.06.011.
Hasz, B.M., Redish, A.D., 2020. Spatial encoding in dorso-
medial prefrontal cortex and hippocampus is related dur-
ing deliberation.
Hippocampus 30, 1194–1208.
doi:10.
1002/hipo.23250.
He, M., Qi, C., Lu, Y., Song, A., Hayat, S.Z., Xu, X., 2018.
The sport expert’s attention superiority on skill-related
scene dynamic by the activation of left medial frontal
gyrus: an erp and loreta study.
Neuroscience 379, 93–
102.
Heaton, R.K., Chelune, G.J., Talley, J.L., Kay, G.G., Cur-
tiss, G., 1993. WCST: Wisconsin card sorting test. Psy-
chological Assessment resources.
Hinton, G.E., 2002. Training products of experts by min-
imizing contrastive divergence. Neural computation 14,
1771–1800.
Hinton, G.E., 2012. A practical guide to training restricted
boltzmann machines, in: Neural networks: Tricks of the
trade. Springer, pp. 599–619.
Hinton, G.E., Osindero, S., Teh, Y.W., 2006. A fast learning
algorithm for deep belief nets.
Neural computation 18,
1527–1554.
Hochreiter, S., Schmidhuber, J., 1997.
Long short-term
memory. Neural computation 9, 1735–1780.
Hohwy, J., Seth, A., 2020. Predictive processing as a sys-
tematic basis for identifying the neural correlates of con-
sciousness. Philosophy and the Mind Sciences 1.
Holcman, D., Tsodyks, M., 2006. The emergence of up and
down states in cortical networks.
PLoS Computational
Biology 2, e23. doi:10.1371/journal.pcbi.0020023.
Holland, O., 2007. A strongly embodied approach to machine
consciousness. Journal of Consciousness Studies 14, 97–
110.
Houk, J.C., Davids, J.L., Beiser, D.G. (Eds.), 1995. Models
of Information Processing in the Basal Ganglia. The MIT
Press, Cambridge, MA.
35


## Page 36


Huang, M.H., Rust, R., Maksimovic, V., 2019. The feeling
economy: Managing in the next generation of artificial
intelligence (ai). California Management Review 61, 43–
65.
Huddy, V., Mansell, W., 2023. Loss and restoration of con-
trol: A perceptual control theory perspective on the role
of mental simulation, in: The Interdisciplinary Handbook
of Perceptual Control Theory, Volume II. Elsevier, pp.
59–74.
Hutto, D.D., 2005. Knowing what? radical versus conserva-
tive enactivism. Phenomenology and the Cognitive Sci-
ences 4, 389–405.
Jacquey, L., Baldassarre, G., Santucci, V.G., O’Regan, J.K.,
2019.
Sensorimotor contingencies as a key drive of de-
velopment: from babies to robots . Frontiers in Neuro-
robotics 13, e1–20. doi:10.3389/fnbot.2019.00098.
Jaeger, H., 2001. The ‘echo state’ approach to analysing and
training recurrent neural networks-with an erratum note.
GMD Report 48. German National Research Center for
Information Technology. Bonn, Germany.
J¨antsch, M., Wittmeier, S., Knoll, A., 2010. Distributed con-
trol for an anthropomimetic robot, in: 2010 IEEE/RSJ
International Conference on Intelligent Robots and Sys-
tems, IEEE. pp. 5466–5471.
Jeannerod, M., 2003. The mechanism of self-recognition in
humans. Behavioural brain research 142, 1–15.
Jung, M., Matsumoto, T., Tani, J., 2019a.
Goal-directed
behavior under variational predictive coding:
Dynamic
organization of visual attention and working memory, in:
2019 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), IEEE. pp. 1040–1047.
Jung, M., Matsumoto, T., Tani, J., 2019b. Goal-Directed
Behavior under Variational Predictive Coding: Dynamic
Organization of Visual Attention and Working Memory.
Preprint arXiv 1903.04932v1.
Kabat-Zinn, J., 1990.
Full catastrophe living: Using the
wisdom of your body and mind to face stress, pain, and
illness. Delta Trade Paperbacks. New edition 2013, with
prevace by Thich Nhat Hanh.
Kappel, D., Nessler, B., Maass, W., 2014. Stdp installs in
winner-take-all circuits an online approximation to hidden
markov model learning. PLoS Comput Biol 10, e1003511.
doi:10.1371/journal.pcbi.1003511.
Kingma, D.P., Welling, M., 2013. Auto-encoding variational
bayes. arXiv .
Koch, C., Massimini, M., Boly, M., Tononi, G., 2016. Neural
correlates of consciousness: progress and problems. Na-
ture Reviews Neuroscience 17, 307.
Koch, C., Tsuchiya, N., 2007. Attention and consciousness:
two distinct brain processes. Trends in cognitive sciences
11, 16–22.
Kohonen, T., 2001.
Self-organizing maps.
Third ed.,
Springer, Berlin.
Konidaris, G., Kaelbling, L.P., Lozano-Perez, T., 2018. From
skills to symbols: Learning symbolic representations for
abstract high-level planning. Journal of Artificial Intelli-
gence Research 61, 215–289.
Kugele, S., Franklin, S., 2021. Learning in lida. Cognitive
Systems Research 66, 176–200.
Kumaran, D., Maguire, E.A., 2007. Match mismatch pro-
cesses underlie human hippocampal responses to associa-
tive novelty. J Neurosci 27, 8517–8524.
Lake, B.M., Ullman, T.D., Tenenbaum, J.B., Gershman,
S.J., 2017. Building machines that learn and think like
people. Brain and Behavioural Sciences 40, 1–72.
Lau, H., Rosenthal, D., 2011. Empirical support for higher-
order theories of conscious awareness. Trends in cognitive
sciences 15, 365–373.
LeDoux, J.E., Brown, R., 2017.
A higher-order theory of
emotional consciousness.
Proceedings of the National
Academy of Sciences 114, E2016–E2025.
Levy, R., 2012.
Apathy: a pathology of goal-directed be-
haviour. a new concept of the clinic and pathophysiology
of apathy. Revue neurologique 168, 585–597.
Levy, R., 2021. A pathology of goal-directed behaviour and
prefrontal cortex–basal ganglia circuits. Apathy: Clini-
cal and Neuroscientific Perspectives from Neurology and
Psychiatry , 156.
Lewis, B.L., 2012. In the game: The interface between wat-
son and jeopardy!
IBM Journal of Research and Devel-
opment 56, 17–1.
Li, J., Li, D., Xiong, C., Hoi, S., 2022. Blip: Bootstrapping
language-image pre-training for unified vision-language
understanding and generation, in: International Confer-
ence on Machine Learning, PMLR. pp. 12888–12900.
Lisman, J.E., Grace, A.A., 2005. The hippocampal-vta loop:
controlling the entry of information into long-term mem-
ory. Neuron 46, 703–713.
Lukoˇseviˇcius, M., Jaeger, H., 2009. Reservoir computing ap-
proaches to recurrent neural network training. Computer
science review 3, 127–149.
Lynn, C.W., Bassett, D.S., 2019. The physics of brain net-
work structure, function and control.
Nature Reviews
Physics 1, 318–332.
Maass, W., Natschl¨ager, T., Markram, H., 2002. Real-time
computing without stable states: a new framework for
neural computation based on perturbations. Neural Com-
put 14, 2531–2560. doi:10.1162/089976602760407955.
Malinowski, P., 2013. Neural mechanisms of attentional con-
trol in mindfulness meditation. Frontiers in neuroscience
7, 8.
Mannella, F., Mirolli, M., Baldassarre, G., 2016.
Goal-
directed behavior and instrumental devaluation: A neural
system-level computational model.
Frontiers in Behav-
ioral Neuroscience 10, e1–27.
doi:10.3389/fnbeh.2016.
00181.
Mannella, F., Santucci, V.G., Eszter, S., Jacquey, L.,
O’Regan, K.J., Baldassarre, G., 2018. Know your body
through intrinsic goals. Frontiers in neurorobotics 12, E1–
17. doi:10.3389/fnbot.2018.00030.
Marcus, G., Davis, E., 2019.
Rebooting AI: Building ar-
tificial intelligence we can trust. Pantheon Books, New
York.
Marques, H.G., Holland, O., 2009. Architectures for func-
tional imagination. Neurocomputing 72, 743–759.
Mars, R.B., Sallet, J., Rushworth, M.F., Yeung, N. (Eds.),
2011. Neural basis of motivational and cognitive control.
MIT Press.
Marsella, S., Gratch, J., Petta, P., 2010.
Computational
models of emotion, in: A Blueprint for Affective Comput-
ing - A sourcebook and manual. Oxford University Press,
New York, NY, USA. volume 11, pp. 21–46.
Mashour, G.A., Roelfsema, P., Changeux, J.P., Dehaene,
S., 2020. Conscious processing and the global neuronal
workspace hypothesis. Neuron 105, 776–798. doi:10.1016/
j.neuron.2020.01.026.
Matsumoto, T., Ohata, W., Benureau, F.C., Tani, J., 2022.
Goal-directed planning and goal understanding by ex-
tended active inference:
Evaluation through simulated
and physical robot experiments. Entropy 24, 469.
36


## Page 37


Mattera, A., Pagani, M., Baldassarre, G., 2020. A computa-
tional model integrating multiple phenomena on cued fear
conditioning, extinction, and reinstatement. Frontiers in
systems neuroscience 14, 65.
McClelland, James L. andRumelhart, D.E., the PDPRe-
searchGroup, 1986. Parallel distributed processing: ex-
plorations in the microstructure of cognition. volume 1.
The MIT Press, Cambridge,MA.
McMurtray, A., Tseng, B., Diaz, N., Chung, J., Mehta, B.,
Saito, E., 2014. Acute psychosis associated with subcor-
tical stroke: comparison between basal ganglia and mid-
brain lesions. Case Reports in Neurological Medicine 2014.
Melloni, L., Mudrik, L., Pitts, M., Koch, C., 2021. Making
the hard problem of consciousness easier.
Science 372,
911–912.
Memmert, D., 2009. Pay attention! a review of visual atten-
tional expertise in sport. International Review of Sport
and Exercise Psychology 2, 119–138.
Meneguzzo, P., Tsakiris, M., Schioth, H.B., Stein, D.J.,
Brooks, S.J., 2014. Subliminal versus supraliminal stim-
uli activate neural responses in anterior cingulate cortex,
fusiform gyrus and insula: a meta-analysis of fMRI stud-
ies. BMC Psychol 2, 52.
Metzinger, T., 2013.
The myth of cognitive agency: sub-
personal thinking as a cyclically recurring loss of mental
autonomy. Frontiers in psychology 4, 931.
Metzinger, T.K., 2017.
The problem of mental action,
in:
Metzinger,
T.K.,
Wiese,
W. (Eds.),
Philosophy
and Predictive Processing. MIND Group, Frankfurt am
Main. chapter 19. URL: https://predictive-mind.net/
papers/the-problem-of-mental-action,
doi:10.15502/
9783958573208.
Meyer, K., Damasio, A.R., 2009.
Convergence and diver-
gence in a neural architecture for recognition and memory.
Trends Neurosci 32, 376–382.
Miikkulainen, R., Bednar, J.A., Choe, Y., Sirosh, J., 2006.
Computational maps in the visual cortex. Springer Sci-
ence & Business Media.
Miles, S., Howlett, C.A., Berryman, C., Nedeljkovic, M.,
Moseley, G.L., Phillipou, A., 2021.
Considerations for
using the wisconsin card sorting test to assess cognitive
flexibility. Behavior research methods 53, 2083–2091.
Miller, B.T., Clapp, W.C., 2011. From vision to decision:
the role of visual attention in elite sports performance.
Eye & contact lens 37, 131–139.
Mirolli, M., Mannella, F., Baldassarre, G., 2010. The roles
of the amygdala in the affective regulation of body, brain,
and behaviour. Connection Science 22, 215–245.
Mysore, S.P., Kothari, N.B., 2020. Mechanisms of competi-
tive selection: A canonical neural circuit framework. Elife
9.
Nair, A., Pong, V., Dalal, M., Bahl, S., Lin, S., Levine,
S.,
2018.
Visual reinforcement learning with imag-
ined goals, in: The Second Lifelong Learning: A Rein-
forcement Learning Approach Workshop (LLRLA2018 at
FAIM2018). 14/07/2018, Stockholm, Sweden.
Newman, S.D., Carpenter, P.A., Varma, S., Just, M.A.,
2003. Frontal and parietal participation in problem solv-
ing in the tower of london: fmri and computational mod-
eling of planning and high-level perception.
Neuropsy-
chologia 41, 1668–1682.
Oddi, A., Rasconi, R., Santucci, V.G., Sartor, G., Cartoni,
E., Mannella, F., Baldassarre, G., 2019.
An intrinsi-
cally motivated planning architecture for curiosity-driven
robots., in: AIRO@ AI*IA, pp. 19–24.
Ohlsson, S., 1992.
Information-processing explanations of
insight and related phenomena, in: Keane, M., Gilhooly,
K. (Eds.), Advances in the Psychology of Thinking.
Harvester-Wheatsheaf.
O’Regan, J.K., Noe, A., 2001. A sensorimotor account of
vision and visual consciousness. Behav Brain Sci 24, 939–
73; discussion 973–1031.
O’Reilly, J.X., Sch¨uffelgen, U., Cuell, S.F., Behrens, T.E.,
Mars, R.B., Rushworth, M.F., 2013. Dissociable effects
of surprise and model update in parietal and anterior cin-
gulate cortex. Proceedings of the National Academy of
Sciences , 201305373.
OReilly, R.C., Frank, M.J., 2006. Making working memory
work: a computational model of learning in the prefrontal
cortex and basal ganglia. Neural computation 18, 283–
328.
Oudeyer, P.Y., Kaplan, F., Hafner, V.V., 2007.
Intrinsic
motivation systems for autonomous mental development.
IEEE transactions on evolutionary computation 11, 265–
286. doi:10.1109/tevc.2006.890271.
O’Regan, J.K., Myin, E., No¨e, A., 2005. Sensory conscious-
ness explained (better) in terms of corporality and alerting
capacity. Phenomenology and the Cognitive Sciences 4,
369–387.
Paiva, A., Leite, I., Ribeiro, T., 2012. Emotion modelling
for social robots, Oxford: Oxford University Press.
Panksepp, J., 1998. Affective neuroscience: the foundations
of human and animal emotions. Oxford Unversity Press,
Oxford.
Park, J.S., O’Brien, J.C., Cai, C.J., Morris, M.R., Liang,
P., Bernstein, M.S., 2023.
Generative Agents: Interac-
tive Simulacra of Human Behavior.
Technical Report
2304.03442. arXiv. doi:10.48550/ARXIV.2304.03442.
Parks, E.L., Madden, D.J., 2013.
Brain connectivity and
visual attention. Brain Connectivity 3, 317–338.
Pasquali, A., Timmermans, B., Cleeremans, A., 2010. Know
thyself:
Metacognitive networks and measures of con-
sciousness. Cognition 117, 182–190.
Passingham, R.E., Wise, S.P., 2012. The neurobiology of the
prefrontal cortex: anatomy, evolution, and the origin of
insight. 50, Oxford University Press.
Patai, E.Z., Spiers, H.J., 2021.
The Versatile Wayfinder:
Prefrontal Contributions to Spatial Navigation.
Trends
Cogn Sci 25, 520–533. doi:10.1016/j.tics.2021.02.010.
Paus, T., 2001.
Primate anterior cingulate cortex: where
motor control, drive and cognition interface.
Nat Rev
Neurosci 2, 417–424.
Pennartz, C.M., 2015. The brain’s representational power:
on consciousness and the integration of modalities. MIT
Press.
Pennartz, C.M., 2018. Consciousness, representation, action:
the importance of being goal-directed. Trends in cognitive
sciences 22, 137–153.
Pennartz, C.M., 2022.
What is neurorepresentationalism?
from neural activity and predictive processing to multi-
level representations and consciousness.
Behavioural
Brain Research 432, 113969.
Pessoa, L., 2015. Multiple influences of reward on perception
and attention. Visual cognition 23, 272–290.
Pezzulo, G., 2014.
Why do you fear the bogeyman?
an
embodied predictive coding model of perceptual inference.
Cognitive, Affective, & Behavioral Neuroscience 14, 902–
911.
Pezzulo, G., Rigoli, F., Friston, K., 2015. Active inference,
homeostatic regulation and adaptive behavioural control.
37


## Page 38


Progress in neurobiology 134, 17–35.
Pfeiffer, B.E., Foster, D.J., 2013. Hippocampal place-cell se-
quences depict future paths to remembered goals. Nature
497, 74.
Pitts,
M.A.,
Lutsyshyna,
L.A.,
Hillyard,
S.A.,
2018.
The
relationship
between
attention
and
conscious-
ness: an expanded taxonomy and implications for ‘no-
report’paradigms. Philosophical Transactions of the Royal
Society B: Biological Sciences 373, 20170348.
P¨oppel, E., Held, R., Frost, D., 1973. Residual visual func-
tion after brain wounds involving the central visual path-
ways in man. Nature 243, 295–296.
Pourpanah, F., Abdar, M., Luo, Y., Zhou, X., Wang, R.,
Lim, C.P., Wang, X.Z., Wu, Q.M.J., 2022.
A review
of generalized zero-shot learning methods , 1–20URL:
https://doi.org/10.1109/TPAMI.2022.3191696, doi:10.
1109/tpami.2022.3191696.
Powers, W.T., 2016.
Perceptual Control Theory:
An
Overview
of
the
Third
Grand
Theory
in
Psychol-
ogy—Introductions, Readings, and Resources.
Living
Control Systems Publ.
Prescott, T.J., Gonzalez, F.M.M., Gurney, K., Humphries,
M.D., Redgrave, P., 2006. A robot model of the basal gan-
glia: behavior and intrinsic processing. Neural Networks
19, 31–61. doi:10.1016/j.neunet.2005.06.049.
Price, A., Filoteo, J.V., Maddox, W.T., 2009. Rule-based
category learning in patients with parkinson’s disease.
Neuropsychologia 47, 1213–1226.
Raffone, A., Srinivasan, N., van Leeuwen, C., 2014a. The in-
terplay of attention and consciousness in visual search, at-
tentional blink and working memory consolidation. Philo-
sophical Transactions of the Royal Society B: Biological
Sciences 369, 20130215.
Raffone, A., Srinivasan, N., van Leeuwen, C., 2014b. Percep-
tual awareness and its neural basis: bridging experimental
and theoretical paradigms. Philos Trans R Soc Lond B
Biol Sci 369, 20130203.
Raffone, A., Srinivasan, N., van Leeuwen, C., 2015. Rapid
switching and complementary evidence accumulation en-
able flexibility of an all-or-none global workspace for con-
trol of attentional and conscious processing: a reply to
wyble et al.
Philos Trans R Soc Lond B Biol Sci 370,
20140315.
Rao, R.P., Ballard, D.H., 1999.
Predictive coding in the
visual cortex: a functional interpretation of some extra-
classical receptive-field effects. Nature Neuroscience 2, 79–
87. doi:10.1038/4580.
Redgrave, P., Prescott, T.J., Gurney, K., 1999. The basal
ganglia: a vertebrate solution to the selection problem?
Neuroscience 89, 1009–1023.
Reggia, J.A., 2013.
The rise of machine consciousness:
Studying consciousness with computational models. Neu-
ral Networks 44, 112–131.
Rehder, E., Wirth, F., Lauer, M., Stiller, C., 2018. Pedes-
trian prediction by planning using deep neural networks,
in: 2018 IEEE International Conference on Robotics and
Automation (ICRA), IEEE. pp. 1–5.
Revonsuo, A., 2006.
Inner presence:
Consciousness as a
biological phenomenon. Mit Press.
Ribas-Fernandes, J.J.F., Solway, A., Diuk, C., McGuire,
J.T., Barto, A.G., Niv, Y., Botvinick, M.M., 2011. A neu-
ral signature of hierarchical reinforcement learning. Neu-
ron 71, 370–379. doi:10.1016/j.neuron.2011.05.042.
Rizzolatti, G., Matelli, M., 2003. Two different streams form
the dorsal visual system: anatomy and functions.
Exp
Brain Res 153, 146–157.
Rohaut, B., Doyle, K.W., Reynolds, A.S., Igwe, K., Couch,
C., Matory, A., Rizvi, B., Roh, D., Velazquez, A.,
Megjhani, M., et al., 2019. Deep structural brain lesions
associated with consciousness impairment early after hem-
orrhagic stroke. Scientific reports 9, 1–9.
Rolls, E.T., 2004.
The functions of the orbitofrontal cor-
tex. Brain Cogn 55, 11–29. doi:10.1016/S0278-2626(03)
00277-X.
Rueckert, E., Kappel, D., Tanneberg, D., Pecevski, D., Pe-
ters, J., 2016.
Recurrent spiking networks solve plan-
ning tasks.
Scientific Reports 6, 21142.
doi:10.1038/
srep21142.
Russell, S.J., Norvig, P., 2016.
Artificial Intelligence:
A
Modern Approach. Third edition ed., Pearson Education,
Harlow, UK.
Ryan, R.M., Deci, E.L., 2000. Self-determination theory and
the facilitation of intrinsic motivation, social development,
and well-being. Am Psychol 55, 68–78.
Santucci, V.G., Baldassarre, G., Mirolli, M., 2016.
Grail:
A goal-discovering robotic architecture for intrinsically-
motivated learning. IEEE Transactions on Cognitive and
Developmental Systems 8, 214–231.
Scherer, K.R., 2005. What are emotions? and how can they
be measured?
Social science information 44, 695–729.
doi:10.1177/0539018405058216.
Schmidhuber, J., 1991. A possibility for implementing cu-
riosity and boredom in model-building neural controllers,
in: Proc. of the international conference on simulation of
adaptive behavior: From animals to animats, pp. 222–227.
Schooler, J.W., Smallwood, J., Christoff, K., Handy, T.C.,
Reichle, E.D., Sayette, M.A., 2011. Meta-awareness, per-
ceptual decoupling and the wandering mind. Trends in
cognitive sciences 15, 319–326.
Schroll, H., Hamker, F.H., 2013.
Computational models
of basal-ganglia pathway functions: focus on functional
neuroanatomy. Frontiers in System Neuroscience 7, 122.
doi:10.3389/fnsys.2013.00122.
Schultz, W., 2002. Getting formal with dopamine and re-
ward. Neuron 36, 241–263.
Seger, C.A., 2008. How do the basal ganglia contribute to
categorization? their roles in generalization, response se-
lection, and learning via feedback. Neuroscience & Biobe-
havioral Reviews 32, 265–278.
Seth, A.K., Bayne, T., 2022. Theories of consciousness. Na-
ture Reviews Neuroscience , 1–14.
Seth, A.K., Izhikevich, E., Reeke, G.N., Edelman, G.M.,
2006.
Theories and measures of consciousness: an ex-
tended framework. Proc Natl Acad Sci U S A 103, 10799–
10804.
Simon, H.A., 1975. The functional equivalence of problem
solving skills. Cognitive psychology 7, 268–288.
Soltani, A., Koechlin, E., 2022.
Computational models
of adaptive behavior and prefrontal cortex.
Neuropsy-
chopharmacology 47, 58–71.
Srivastava, A., al., 2022.
Beyond the Imitation Game:
Quantifying and extrapolating the capabilities of language
models. Technical Report. arXiv:2206.04615.
Stumbrys, T., Erlacher, D., Sch¨adlich, M., Schredl, M., 2012.
Induction of lucid dreams: A systematic review of evi-
dence. Consciousness and Cognition 21, 1456–1475.
Sun, R., 2016. The clarion cognitive architecture: Toward
a comprehensive theory of the mind, Oxford University
Press. chapter 6, pp. 117–133.
Sun, R., Wilson, N., Lynch, M., 2016. Emotion: A unified
38


## Page 39


mechanistic interpretation from a cognitive architecture.
Cognitive Computation 8, 1–14.
Sutton, R.S., Barto, A.G., 1998. Introduction to reinforce-
ment learning. volume 135. MIT press Cambridge.
Tang, W., Shin, J.D., Jadhav, S.P., 2021.
Multiple time-
scales of decision-making in the hippocampus and pre-
frontal cortex. Elife 10, e66227.
Tang, Y.Y., Holzel, B.K., Posner, M.I., 2015. The neuro-
science of mindfulness meditation. Nature Reviews Neu-
roscience 16, 213–225. doi:10.1038/nrn3916.
Tegmark, M., 2017.
Life 3.0: Being human in the age of
artificial intelligence. Knopf.
Telles-Correia, D., Moreira, A.L., Goncalves, J.S., 2015. Hal-
lucinations and related concepts-their conceptual back-
ground. Frontiers in psychology 6, 991.
Thill, S., Caligiore, D., Borghi, A.M., Ziemke, T., Baldas-
sarre, G., 2013. Theories and computational models of af-
fordance and mirror systems: An integrative review. Neu-
roscience and Biobehavioral Reviews 37, 491–521.
Tononi, G., 2004. An information integration theory of con-
sciousness. BMC Neurosci 5, 42.
Tononi, G., 2008. Consciousness as integrated information:
a provisional manifesto. Biol Bull 215, 216–242.
Tononi, G., Boly, M., Massimini, M., Koch, C., 2016. Inte-
grated information theory: from consciousness to its phys-
ical substrate. Nat Rev Neurosci 17, 450–461.
Tsujimoto, S., Genovesio, A., Wise, S.P., 2011. Frontal pole
cortex: encoding ends at the end of the endbrain. Trends
in cognitive sciences 15, 169–176.
Tye, K.M., 2018. Neural Circuit Motifs in Valence Process-
ing. Neuron 100, 436–452. doi:10.1016/j.neuron.2018.
10.001.
Ullman, S., 2019.
Using neuroscience to develop artificial
intelligence. Science 363, 692–693.
Van Boxtel, J.J., Tsuchiya, N., Koch, C., 2010. Conscious-
ness and attention: on sufficiency and necessity. Frontiers
in Psychology 1, 217.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones,
L., Gomez, A.N., Kaiser, L., Polosukhin, I., 2017.
At-
tention is all you need. arXiv preprint arXiv:1706.03762
.
Verdejo-Garc´ıa, A., P´erez-Garc´ıa, M., Bechara, A., 2006.
Emotion, decision-making and substance dependence: a
somatic-marker model of addiction. Curr Neuropharmacol
4, 17–31.
Voss, U., Holzmann, R., Tuin, I., Hobson, A.J., 2009. Lucid
dreaming: a state of consciousness with features of both
waking and non-lucid dreaming. Sleep 32, 1191–1200.
Vossel, S., Geng, J.J., Fink, G.R., 2014. Dorsal and ventral
attention systems: distinct neural circuits but collabora-
tive roles. The Neuroscientist 20, 150–159.
Wang, Y., Zuo, C., Wang, D., Tao, S., Hao, L., 2020.
Reduced thalamus volume and enhanced thalamus and
fronto-parietal network integration in the chess experts.
Cerebral Cortex 30, 5560–5569.
Ward, P., Cavanna, A.E., et al., 2013.
Functional neu-
roanatomy and behavioural correlates of the basal gan-
glia: evidence from lesion studies. Behavioural neurology
26, 219–223.
Wayne, G., Hung, C.C., Amos, D., Mirza, M., Ahuja, A.,
Grabska-Barwinska, A., Rae, J., Mirowski, P., Leibo,
J.Z., Santoro, A., Gemici, M., Reynolds, M., Harley,
T., Abramson, J., Mohamed, S., Rezende, D., Saxton,
D., Cain, A., Hillier, C., Silver, D., Kavukcuoglu, K.,
Botvinick, M., Hassabis, D., Lillicrap, T., 2018. Unsuper-
vised predictive memory in a goal-directed agent. arXiv
preprint arXiv:1803.10760 .
Weiskrantz, L., 1991.
Disconnected awareness for detect-
ing, processing, and remembering in neurological patients.
Journal of the Royal Society of Medicine 84, 466–470.
Weiskrantz, L., 1995. The problem of animal consciousness
in relation to neuropsychology. Behavioural brain research
71, 171–175.
Weiskrantz, L., 2004. Roots of blindsight. Progress in brain
research 144, 227–241.
Wodarz, N., Becker, T., Deckert, J., 1995. Musical halluci-
nations associated with post-thyroidectomy hypoparathy-
roidism and symmetric basal ganglia calcifications. Jour-
nal of Neurology, Neurosurgery, and Psychiatry 58, 763.
Yaron, I., Melloni, L., Pitts, M., Mudrik, L., 2022.
The
contrast database for analysing and comparing empiri-
cal studies of consciousness theories. Nature Human Be-
haviour 6, 593–604.
Yates, J.C., Immergut, M., 2015.
The Mind Illuminated:
A Complete Meditation Guide Integrating Buddhist Wis-
dom and Brain Science.
Yun,
T.,
Sun,
C.,
Pavlick,
E.,
2021.
Does Vision-
and-Language Pretraining Improve Lexical Grounding?
preprint 2109.10246. arXiv.
van der Zwaard, R., Polak, M.A., 2001. Pseudohallucina-
tions: a pseudoconcept? a review of the validity of the
concept, related to associated symptomatology. Compre-
hensive Psychiatry 42, 42–50.
39

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
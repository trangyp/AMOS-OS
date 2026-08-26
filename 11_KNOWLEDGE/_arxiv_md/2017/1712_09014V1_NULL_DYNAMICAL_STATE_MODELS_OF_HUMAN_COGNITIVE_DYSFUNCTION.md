---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1712.09014v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1712.09014v1_Null_Dynamical_State_Models_of_Human_Cognitive_Dysfunction

> Source: 1712.09014v1_Null_Dynamical_State_Models_of_Human_Cognitive_Dysfunction.pdf

> Pages: 17

---


## Page 1


arXiv:1712.09014v1  [cs.AI]  25 Dec 2017
Null Dynamical State Models of Human Cognitive Dysfunction
Michael J. Gagen
Email:
mjgagen@gmail.com
(Dated: December 27, 2017)
The hard problem in artiﬁcial intelligence asks how the shuﬄing of syntactical symbols in a pro-
gram can lead to systems which experience semantics and qualia. We address this question in three
stages. First, we introduce a new class of human semantic symbols which appears when unexpected
and drastic environmental change causes humans to become surprised, confused, uncertain, and
in extreme cases, unresponsive, passive and dysfunctional. For this class of symbols, pre-learned
programs become inoperative so these syntactical programs cannot be the source of experienced
qualia. Second, we model the dysfunctional human response to a radically changed environment as
being the natural response of any learning machine facing novel inputs from well outside its previous
training set. In this situation, learning machines are unable to extract information from their input
and will typically enter a dynamical state characterized by null outputs and a lack of response. This
state immediately predicts and explains the characteristics of the semantic experiences of humans
in similar circumstances. In the third stage, we consider learning machines trained to implement
multiple functions in simple sequential programs using environmental data to specify subroutine
names, control ﬂow instructions, memory calls, and so on. Drastic change in any of these environ-
mental inputs can again lead to inoperative programs. By examining changes speciﬁc to people or
locations we can model human cognitive symbols featuring these dependencies, such as attachment
and grief. Our approach links known dynamical machines states with human qualia and thus oﬀers
new insight into the hard problem of artiﬁcial intelligence.
I.
INTRODUCTION
Artiﬁcial intelligence seeks to understand how a ma-
chine interacting with its environment, processing syn-
tactical symbols, and changing from one causal dynam-
ical state to another, can generate semantic symbols,
meaning, intentionality, and understanding. This is the
hard problem of artiﬁcial intelligence [1, 2]. There are
two contrasting approaches to modeling artiﬁcial intelli-
gence, both grounded in work by Turing. In the ﬁrst ap-
proach, Turing deﬁned a universal computer and its set
of computable functions which, with the beneﬁt of hind-
sight, raises the question of whether intelligence is itself a
computable function [3]. However, rather than address-
ing this question, Turing settled for the simpler claim
that merely simulating intelligent behaviour was a com-
putable function and proposed the imitation game, now
called the Turing Test, as the only practical approach to
discerning intelligence whether natural or artiﬁcial [4].
The hypothesis that intelligence itself is computable
was most strongly presented in 1976 with the physical
symbol systems hypothesis (PSSH) holding that syntac-
tical symbol manipulations are necessary and suﬃcient to
explain and reproduce human and machine intelligence
[5]. This approach posits a system of symbol structures,
each consisting of many atomic symbols which are pro-
cessed according to a set of creation, reproduction, mod-
iﬁcation and destruction rules. This system inhabits a
world of external objects, where symbols can “designate”
an object if that symbol can inﬂuence or be inﬂuenced by
the object, and where symbols are “interpreted” if they
designate a process which the system can carry out. For
many decades, this approach has been interpreted in ex-
tremely narrow and limited terms. However, broadly in-
terpreted, the PSSH subsumes many subsequent research
programs [6, 7]. An invocative and poetic treatment of
the potential of a symbolic approach sees future conscious
programs as being based on active symbols equivalent to
self-contained programs possessing multiple simultaneous
interpretations on many diﬀerent levels, with symbols
causally linked with internal and external environments,
and eventually combining to form a self-referential model
of consciousness [8].
The PSSH approach has been critiqued by many au-
thors. In 1978, it was argued that however accurately
a syntactical symbol system modeled human physiology,
that system (a computer or the Chinese nation) would
never feel pain [9, 10].
Just afterwards, Searle intro-
duced a human into a syntactical symbol system, the
Chinese Room, to show that no amount of syntactical
symbol processing would ever lead to semantic mean-
ing and qualia as experienced in human cognition [11].
In the subsequent widespread and ongoing debate, some
have argued that consciousness doesn’t exist [12, 13], or
that consciousness can only be explained by extensions
to currently understood physics [2, 14].
The systems reply to the Chinese Room holds that
these perceived limitations reﬂect a failure of human in-
tuition about just what syntactical symbolic programs
can achieve. For instance, simple dynamical systems with
only three degrees of freedom [15], and simple train net-
works [16], can implement undecidable computations and
hence have totally unpredictable outcomes. In 1988, Bo-
den noted that intuitions about the capacities of com-
puter programs couldn’t be trusted, and argued that
computer programs are not merely formal systems or syn-
tax alone as they can, given a suitable hardware context,
cause procedures to be implemented, which builds or ac-
tivates symbols, which can alter external objects creating
a causal semantics [17]. Exactly how syntactical symbols
grounded in sensory inputs can combine to form higher
level semantic symbols is the still open symbol grounding
problem[18, 19]. It can be argued that these latter state-
ments of the problem essentially reprise the designated
and interpreted symbols of the physical symbol systems
hypothesis [5]. Researchers have been building on our
understandings to formulate models of human level or
artiﬁcial general intelligence [20–23].
Despite our diﬃculties in understanding the hard prob-
lem of artiﬁcial intelligence, there has been considerable


## Page 2


2
progress lately in artiﬁcial intelligence systems. Massive
data tables and number crunching allowed Deep Blue to
be crowned as world chess champion [24], while Wat-
son employed big data and natural language process-
ing to defeat human Jeapardy champions [25].
Deep
learning neural networks [26–28] and deep neural net-
works undertaking partially unsupervised and reinforce-
ment learning have seen computers master video games
such as ATARI [29], and seen AlphaGo, AlphaGo Zero,
and AlphaZero achieve superhuman performance at Go,
Chess, and Shogi [30–32]. Neuroscience is increasingly
optimistic about locating the neural correlates of con-
sciousness [33, 34], while the growing power of comput-
ers is being exploited to implement cortical simulators
[35, 36] leading to whole brain emulators for C. elegans
[37], ﬂy [38], mouse [39], and eventually it is hoped, hu-
man. Interestingly, the ability to visualize reconstructed
human visual brain experiences has been demonstrated
[40].
However, despite all the progress being made, few
would argue that these programs possess understanding
or experience qualia. Further, the size and complexity of
these programs suggests that any putative artiﬁcial in-
telligence program able to mimic a full range of human
capacities will be both enormous and complex. In turn,
the need for complex programs to model artiﬁcial intel-
ligence implies that there is nothing to be learned from
small systems lacking size or complexity or code.
In this paper, we wish to present a new approach to
artiﬁcial intelligence which exploits small systems lacking
both code and capacity, and yet which are able to gen-
erate dynamical states whose characteristics predict and
explain the semantic experiences of a particular class of
human semantic symbols. In this new class, humans be-
come cognitively dysfunctional when faced with radical
environmental change as in a disaster. Because humans
are largely dysfunctional, then an accurate model of hu-
man cognition in these circumstances does not require
large and complex code. For this class of semantic sym-
bols, we claim that simple learning machine models can
predict and explain aspects of the human semantic ex-
perience.
We make no claims that our simple models
will themselves have semantic experiences. We turn to
consider how this approach will be implemented here.
In this paper, we introduce a new class of cognitive se-
mantic symbols which humans typically experience when
faced with radical and unexpected environmental change
as in a disaster. This class is introduced in Sect. II. In
a disaster, humans will continue to experience seman-
tics and qualia but many of them will become cogni-
tively unaware, passive, unmotivated, and unresponsive.
They will be unable to access any of their pre-existing
or pre-learned functional capacities so, as noted above,
these pre-learned capacities cannot be the source of hu-
man qualia and do not need to be included in our small
models. Our approach breaks the linkage from syntax to
semantics.
It is also relatively straightforward to model the dys-
functional human response to a disaster using a learning
machine. In particular, every learning machine presented
with input data well outside its previous training set will
generally become dysfunctional—an example of “garbage
in, garbage out”. More interestingly, a suﬃciently com-
plicated learning machine will generally enter a partic-
ular dynamical state when presented with novel inputs.
Because the machine can’t extract information from the
unknown input, the machine ends up processing zero in-
formation and so exhibits a “null” dynamical state. This
null dynamical state serves as a close model of the un-
responsive cognitive state of humans in similar circum-
stances. In Sect. III, we show that the characteristics
of this null dynamical state can be used to predict and
explain the characteristics of human semantic symbols
in similar circumstances. This learning machine model is
then used to explain the shocked and confused behaviour
of Searle’s Chinese Room when placed in a disaster sce-
nario. (Because the Room is an accurate simulation of
a human, it will respond like a human and appear to
be passive and unresponsive.) The objectively observ-
able dynamical null state of the Room will predict and
explain the subjective experience (if any) of the Room
and of humans in disaster situations. We will ﬁnish this
section by discussing how a dynamical null state model
addresses the subjective-objective explanatory gap be-
tween a computational state and semantic experiences,
and the properties of qualia as experienced by humans.
In Sect. IV, we provide a mathematical speciﬁcation of
the dynamical null state typically exhibited by learning
machines when presented with data well outside their
training sets.
We focus principally on artiﬁcial neural
networks as their dynamics are reasonably well under-
stood. The result is a mathematically speciﬁed dynam-
ical null state whose characteristics predict and explain
the semantic cognitive experiences of humans in similar
situations.
We apply these dynamical null states to model human
semantic symbols in Sect. V where we ask what hap-
pens when a large percentage (80% or so) of a learning
machine’s functional capacities have been learned in the
presence of a single teacher (Alice say) and at a single lo-
cation (Alice’s laboratory). The lack of variation in the
environment during the learning period makes it likely
that environmental information unique to the teacher or
to the location will be deeply embedded within the ma-
chine’s learned functions—rather than learning a generic
“Say Good Morning” function, the machine might learn
a speciﬁc “Say Good Morning to Alice” function. Conse-
quently, if Alice is absent and Bob says “Good Morning”
to the machine, then it will be unable to respond as it has
no learned function speciﬁc to Bob. In our approach, we
consider how a learning machine can build environmental
location and person dependencies into its functionality,
so that drastic changes to the environment can cause dys-
function. We apply this approach to model a number of
human cognitive semantic symbols.
Finally, a concluding summary appears in Sect. VI.
II.
A NEW CLASS OF SEMANTIC SYMBOLS:
HUMAN DISASTER RESPONSE
We have no idea how to even begin coding a program
to understand, to intend, or, for instance, to experience
“redness” on observing red photons. However, it might
be possible to make progress by considering a new class
of human cognitive symbols which arise when humans
face unexpected radical environmental change and gen-
erate qualia like surprise and confusion.
Because the


## Page 3


3
changed environment is unexpected, we claim that the
qualia don’t result from pre-existing programs, but arise
from the altered dynamical state of the underlying cog-
nitive architecture.
The responses of people to unexpected drastic envi-
ronmental change is often not as cool, calm and collected
as we would hope, or as panicked as we might suspect.
Disaster response organizations have labeled many com-
mon beliefs about how people respond as myths.
In
particular, “Most disaster victims are psychologically re-
silient and engage in socially integrative—rather than
destructive—responses” [41]. However, a small percent-
age of the population (of order 14%) can display disaster
shock and respond with docility, disoriented thinking, ap-
athy, confusion and disbelief when facing “sudden onset,
low forewarning events involving widespread physical de-
struction” [41].
Anthropological studies of disasters led Wallace to
summarize a typical human response to “unexpected,
sudden and overpowering trauma” as the disaster syn-
drome [42–44].
A “large proportion of persons in the
impact area” (up to 33%) may “appear to the observer
to be ‘dazed,’ ‘stunned,’ ‘apathetic,’ ‘passive,’ ‘immobile,’
or ‘aimlessly puttering around’.” Wallace concluded that
the “determinants of the syndrome are, in my opinion,
not primarily physical injuries, physical shock, . . . they
are psychological” as a person displays the “syndrome
whether or not he has been injured.” Wallace felt the
“precipitating factor in the disaster syndrome seems to
be “the perception that . . . practically the entire visible
community is in ruins.” In response to this realization,
victims exhibit “withdrawal from perceptual contact with
this grim reality and regression to an almost infantile
level of adaptive behavior characterized by random move-
ment, relative incapacity to evaluate danger or to insti-
tute protective action, inability to concentrate attention,
to remember, or to follow instructions.” [42–44].
The disaster syndrome, as described by Wallace, is
nowadays seen to be part of a broader suite including
disaster response, psychological shock and physiological
conservation-withdrawal syndrome [45]. Victims of dis-
aster can exhibit shock, stupor, being dazed, stunned
and numb, and can exhibit immobility, quiescence and
unresponsiveness, constricted attention and detachment.
In this paper, we will be emphasizing the importance of
psychological factors (rather than those caused by phys-
ical injury or physiological hormonal responses) in sud-
den disasters when victims glimpse “a part of the human
condition that most of us never see” [46].
These fac-
tors are clearly indicated by the ﬁrst-person report of
an evacuee from the towers on the “9/11” attacks. Elia
Zede˜no felt the plane impact the tower, and even after
a colleague screamed at her to get out, still found her-
self collecting belongings and wandering in circles at her
desk, and feeling in a trance. Roughly 40% of survivors
gathered belongings before evacuating.
Zede˜no’s later
reported response to seeing bodies lying motionless out-
side the building lobby illustrates “how the human mind
processes overwhelming peril”:
I’m slowing down because I’m starting to re-
alize I’m not just looking at debris. My mind
says, “It’s the wrong color.” That was the
ﬁrst thing.
Then I start saying, “It’s the
wrong shape.” Over and over in my mind.
. . . It was like I was trying to keep the infor-
mation out. My eyes were not allowing me
to understand. I couldn’t aﬀord it. . . . Then
when I ﬁnally realized what it meant to see
the wrong color, the wrong shape, that’s
when I realized, I’m seeing bodies.
That’s
when I froze.
“Zede˜no went temporarily blind at that moment,” and
felt numb, and had to be led outside the building. As
the tower came down, her vision returned when needed,
and she survived [46].
Similar responses to disaster have been collated by
Leach. An “engine ﬁre aboard a Boeing-737 airliner at
Manchester airport in 1985 that resulted in 55 deaths
found some passengers sitting immobile in their seats
until overtaken by smoke and toxic fumes” [47]. Simi-
lar passivity substantially increased the death toll in the
Piper Alpha oil platform ﬁre in which “A large num-
ber of people apparently made no attempt to leave the
accommodation” [48]. Even prepared people can suﬀer
unexpected passivity under stress—11% of parachuting
fatalities result from “no-pull” events where after fail-
ure of the main chute the reserve chute is not pulled [49].
Leach concluded that victim passivity results from a “dif-
ﬁculty in integrating information from the new survival
environment, through multimodal systems, to informa-
tion stored in long-term memory” so that “victims perish
unnecessarily because the threat environment restricts
both the storage and processing capacities of working
memory coupled with a form of temporary, environmen-
tally induced dysexecutive syndrome” [47]. After subse-
quent investigations, Leach found that victim immobility
or freezing is a “common response to unfolding emergen-
cies” resulting from an “impaired response that delays
evacuation, establishing a closed-loop process that leads
to fatalities in otherwise survivable situations” [50]. Ex-
amples cited included
• volunteers who were “behaviorally inactive” in
practice airline evacuations,
• passengers in the Manchester crash “were seen to
remain in their seats until they became engulfed in
ﬂames,”
• survivors of the Piper Alpha oil rig ﬁre reported
that victims could not be made to move and “just
slumped down,”
• some victims of the Estonia ferry sinking were “pas-
sive and stiﬀdespite reasonable possibilities for es-
caping,” while many apparently perished because
they simply did nothing to save themselves. Sur-
vivors reported that victims “were standing still
apparently in shock,” or “some paralyzed and ex-
hausted passengers were standing on the staircase”
or were “sitting in corners, incapable of doing any-
thing,” while “people were beyond reach and did
not react when other passengers tried to guide
them, not even when they used force or shouted at
them.” One survivor reported that “I didn’t think.
Shock is so disorienting it doesn’t allow us to think
clearly.
. . . People just sitting in complete shock
and me not understanding why they’re not doing
something to help themselves. They just sat there


## Page 4


4
and being swamped by the water when it came in.”
Another survivor reported seeing “around 10 per-
sons lying on the deck near the bulkhead. They
seemed apathetic and he threw life jackets to them.
He did not see them react or put on the lifejackets.”
Leach concluded that about 10-15% of people in a dis-
aster will remain relatively calm, able to collect their
thoughts and their judgment and reasoning abilities will
remain relatively unimpaired. A second group of about
75% will “be stunned and bewildered, showing impaired
reasoning and sluggish thinking.
They will behave in
a reﬂexive, almost automatic manner.”
A ﬁnal group
of about 10-15% of the population “will tend to show
a high degree of counterproductive behavior adding to
their danger, such as uncontrolled weeping, confusion,
screaming, and paralyzing anxiety.”
[50].
In seeking
to explain these behaviours, Leach proposed a model in
which human working memory has limited capacity and
a maximum rate at which novel information can be pro-
cessed. This “helps to explain the slowing or absence of
response during the critical impact phase of a disaster.”
In addition, Leach proposes that over time people learn
complex behaviours as pre-learned behavioural responses
or schemas. In an emergency however, if no pre-learned
schema exists then a new temporary schema has to be
created and this can take longer than the duration of the
emergency. The “result is that no behavioral schema will
be triggered from the schemata database and no tempo-
rary schema can be created within the time available.
This produces a cognitively induced paralysis or ‘freez-
ing’ behavior” [50].
Leach later developed theoretical
models to explain this maladaptive behaviour [51].
These human responses to disaster have been widely
studied with the view of ﬁnding an adaptive explana-
tion for this disaster response [45, 52, 53]. For instance,
an adaptive acute stress response to danger sees animals
ﬁrst freezing to hide and assess the situation, then ﬂeeing
danger if possible, ﬁghting if not, and fainting to “play
dead” and exhibit tonic immobility if caught by a preda-
tor [54]. These added fainting stages feature a dissocia-
tive “shut-down” exhibiting a “partial or complete loss
of the normal integration, . . . immediate sensations, and
control of bodily movements” and losses of function such
as “hysterical blindness” with no evident organic basis
[55]. Tonic immobility has been linked to rape-induced
paralysis wherein a high percentage of victims feel par-
alyzed and unable to act despite no loss of conscious-
ness [56]. Experiments into tonic immobility are ongoing
[57, 58].
While few people will experience a major disaster and
the associated response, many have experience a range
of lesser events involving an unexpectedly changed en-
vironment. These lesser shocks lie on a spectrum and
all involve a response to sudden environmental change.
These changes can range in severity from grief and be-
reavement, to shame and humiliation, to being simply
surprised and startled. On the more innocuous end of
the spectrum, surprise and startle become pleasurable
and sought after as in amusement parks, and can form
the basis of humour which depends on a punch line in-
troducing sudden and unexpected setting changes in a
joke.
In more detail, grief and bereavement can be a de-
bilitating response to the deaths of loved ones.
Re-
sponses to bereavement have been described as an “as-
sault,” a “blow to the face, head, or guts,” of being “over-
whelmed”, of “not being able to take it, the world shat-
tering around one, and sinking into a black hole,” with
defenses including “disbelief, and dissociation,” and of
feeling numb [45]. More general grief symptoms can in-
clude fear of losing one’s mind, hallucinations, feeling
hopeless, fatigue and loss of interest and ability to con-
centrate [59]. About 10-20% of people can suﬀer compli-
cated grief and be overwhelmed by “thoughts of the de-
ceased, disbelief, feeling stunned, and lack of acceptance
of the death; . . . with enduring functional impairments”
[60]. Suﬀerers experience a “persistent disturbing sense
of disbelief regarding the death” and a “resistance to ac-
ceptance of the painful reality” [61].
In everyday life, an acute stress response can be caused
in situations featuring shame, humiliation and embar-
rassment. Victims of humiliation can report that “they
felt wiped out, helpless, confused, sick in the gut, para-
lyzed, or ﬁlled with rage,” or had been “stabbed in the
heart, or hit in the solar plexus,” so much so that they
“wished they could disappear” [62]. Who hasn’t expe-
rienced the mind-numbing eﬀects of being the unwanted
center of attention in a humiliating situation.
The sensation of surprise results from a “mismatch be-
tween ones mental expectations and perceptions of ones
environment” [63] which then causes something similar
to the ﬂight or ﬁght reaction with an “interruption of
ongoing information processing and the reallocation of
processing resources to the unexpected event” in order
to update the relevant schemas [63, 64]. For instance, pi-
lots can be lulled into such a sense of security because of
modern aircraft reliability that “when unexpected criti-
cal events occur, pilots are often genuinely surprised and
don’t have readily accessible action plans on how to deal
with them” [65].
These surprise events can lead to a
startle response and even to acute stress where pilots
have sometimes “taken no action at all” because of a
“signiﬁcant impairment to both cognitive and psychomo-
tor performance” [65].
An investigation into these re-
sponses showed a third of pilots in ﬂight simulator exper-
iments exhibited “pathological reactions” when startled,
and they froze and were unable to respond to unfolding
events [65]. However, as noted previously, surprise and
startle can sometimes be pleasurable and sought after
as when we seek it out in amusement parks, or arrange
to surprise friends in order to please them—many adults
have played “peek-a-boo” with a child and enjoyed their
happy response.
And everyone enjoys the pleasure of humour which is
itself based on the human surprise and startle reactions.
In the incongruity-resolution model for humour, an audi-
ence initially interprets a joke using one mental schema
which is disrupted when the punchline presents an in-
congruity whose resolution requires a mental shift and
re-evaluation of previously assumed knowledge [66]. This
approach has been widely applied in, for example, chil-
dren’s humour and advertising [67, 68]. Deeper expla-
nations for why these incongruity-resolutions are found
pleasant can be based on locating neural correlates in
which one neural pattern is unexpectedly replaced by
another [69, 70], or broader evolutionary models [71], or
cognitive approaches [72].


## Page 5


5
III.
A SHOCKED AND CONFUSED CHINESE
ROOM
When faced with drastic and unexpected environmen-
tal change, humans sometimes cannot process novel en-
vironmental information, cannot access pre-learned pro-
gramming, and cannot invent new responses in the time
available. Their cognition can eﬀectively cease and they
can become passive, unresponsive and unaware. By de-
sign, the Chinese Room will react just like a human in
a disaster and so can also become unresponsive. In this
section, we will present a learning machine model of this
disaster response in the Chinese Room and in humans.
A.
A learning machine model
In a disaster humans lose access to most pre-existing
and prelearned functionalities and yet still experience se-
mantic content, so these prelearned functionalities can-
not be the source of human semantic content in a dis-
aster.
Consequently, modeling a human disaster re-
sponse in an artiﬁcial intelligence does not need to in-
clude these unused functionalities. (To illustrate, when
modeling how a chess program performs in an altered
environment—when put in charge of an autonomous ve-
hicle for instance—we don’t need to actually include the
thousands of lines of chess playing code that will never
be called.) Similarly, our artiﬁcial intelligence model does
not need to include any syntactical programs or learned
functions that are uncalled in a disaster scenario. A small
scale model suﬃces to model the human disaster response
allowing us to break the link between syntactical code
and semantic symbols and drastically simplify our ap-
proach to artiﬁcial intelligence.
We can further simplify our approach by noting that
essentially all suﬃciently complicated learning machines
will generate a passive and unresponsive state when faced
with a novel or radically changed environment well out-
side their prior training sets.
It takes a long time for
learning machines to master their training sets, and no
learning machine can instantly master a new training set
corresponding to a radically altered environment. Con-
sequently, all learning machines will ﬂounder when faced
with novel inputs well outside their existing training set.
In this paper, we are using a broad deﬁnition of learning
machine as being any machine optimized for a particular
environment whether by evolutionary selection, by train-
ing and learning, by iterated human design, or by any
generalized Darwinian algorithm incorporating replica-
tion, variation and selection which increasingly ﬁts the
machine to its environment [73–75]. Once a learning ma-
chine has been ﬁtted to an environment, its training set,
then radical changes to that training set will prevent it
from extracting information from the new training set. It
will then have nothing to pass to later information pro-
cessing stages, and the machine will generally output null
vectors. (These claims will be justiﬁed in more detail be-
low.) Hence, a simple learning machine model predicts
that radically changed environments will cause a learn-
ing machine to continually output null vectors and so
exhibit a dynamical state in which it essentially appears
“oﬀ”. The machine itself is “on” and fully operational;
it is just that it cannot process the information from the
radically changed environment. In this dynamical null
state, the learning machine becomes passive, unrespon-
sive and “unaware” of its surroundings. It is immediately
apparent that the dynamical state of the learning ma-
chine in a radically changed environment closely mimics,
and predicts and explains the semantic content of human
learning machines in similar situations. Emphatically, we
are not writing subroutines to simulate passivity, we are
ﬁnding those circumstances that render all learning ma-
chines passive, and using this learning machine response
to model the same passivity in human learning machines.
We are using the dynamical state of the machine, its sys-
tem state, as a predictor of the semantic content expe-
rienced by humans in similar situations. This approach
supports the systems reply to the Chinese Room argu-
ment.
Another important aspect of our approach is that hu-
man brains learn without having external designers op-
timizing the details of the neural architecture. For hu-
mans, no designer chooses the number of neural modules
used, or the number of neural layers and neurons and
their activation functions, or the network data represen-
tations used to learn a function. These network architec-
tural choices can radically eﬀect the operation of a neural
network—an unstructured learning task such as backing
up a lorry [76] can be learned signiﬁcantly faster and by a
smaller network when using external programmers to de-
compose the task into subproblems [77]. Also, possibly
the very “formation of appropriate representations lies
at the heart of human high-level cognitive abilities . . . of
understanding how to draw meaning out of the world”
[78]. Having external designers impose their own high
level representations on a network might well prevent it
from modeling high level cognitive abilities. In this pa-
per, we will model learning machines which have trainers
but lack external designers. Our machines will (some-
how) determine their own modular structures, decide the
number of neural layers and neurons to devote to a task,
and formulate their own high level data representations.
If, as is likely, they make mistakes then these mistakes
can be used to model the same mistakes made in the de-
velopment of human neural networks. If too few neurons
are assigned the machine (and the human) will be unable
to either learn a task or generalize it, while if too many
neurons are assigned then the machine (and human) will
overﬁt to the task and also be unable to generalize.
For a speciﬁc example, consider how a learning ma-
chine or a human must learn to acquire data from their
environment by developing their own application pro-
gramming interfaces (APIs)—to read today’s tempera-
ture the machine or the human might learn to move their
visual input system to a certain position to locate a par-
ticular rectangular shape and to correlate this mark with
that number. APIs are generally speciﬁc to a particular
hardware environment implying again that radical envi-
ronmental change can render APIs inoperative to destroy
the machine’s input and output channels.
We will also task our machines with learning multi-
ple functions simultaneously (just as humans do) and
with recurrently passing information from one function to
another to implement sequential processing. To accom-
plish this, our machine must use environmental informa-
tion to deﬁne the equivalents of subroutine names, func-
tion names, variable names, memory and data addressing


## Page 6


6
schemes, and the usual control structures like conditional
tests and loop counters. Essentially, our learning machine
(and humans) must invent their own new computational
architecture and dedicated programming language solely
from their interactions with their trainer and their envi-
ronment. This is a diﬃcult task, and it is to be expected
that environmental data will inappropriately populate all
aspects of the learned architecture.
This again means
that a radically changed environment can be expected to
destroy the learned computer architecture and its pro-
grams. In our approach, a learning machine faced with
radical environmental change will be attempting to run
barely functional program code and will exhibit passivity,
hesitations, repeated loops, glitches, and stutters, just
as do humans. The generated null dynamical state was
never learned or pre-programmed, just as with humans,
and it is this state that provides our model for the se-
mantic experiences of humans in these situations.
B.
Learning Machine Responses to Environmental
Change
A ﬁnal part of our modeling approach notes that learn-
ing machines can respond to radically altered environ-
ments in three main ways. First, the learning machine
might seek to restore the environment to its original con-
dition. Second, the learning machine might embark on
some lengthy and diﬃcult retraining to ﬁt to the new
environment. Finally, the machine might adopt the eas-
ier approach of changing the input data coming from the
altered environment back into a form suitable for process-
ing by its original network. In other words, the machine
might “spoof” or alter its own input data to allow pro-
cessing of the changed environment by its original net-
work [79]. (A fourth approach might involve the machine
undertaking an automatic “freeze, ﬂight, ﬁght” response
whenever they are startled by environmental change. We
do not include such automatic responses here.) In this
paper, each of these three possible responses to the ini-
tial stimulus, the unexpected environmental change, will
be used to predict and explain semantic experiences of
humans in similar circumstances.
Before considering how the Chinese Room responds
to a radically changed environment, it is worthwhile ex-
amining some simpler systems. We will consider model
learning machines which receive input data packets from
the environment and process and recurrently address
them across a network to diﬀerent functional modules
until a sequential program is complete.
For a ﬁrst example, consider the post oﬃce which is of-
ten used as an introduction to packet switched computer
networking [79]. A post oﬃce using optical sensors to sort
envelopes might well stop working if the spectrum of the
room lighting is changed. The machines will be inter-
nally fully functional but unable to work in the changed
environment and the system will stop and enter a null dy-
namical state. Restarting the system will involve either
ﬁxing the room lighting to return the environment to its
original state, or changing the machine’s optical sensors
to suit the new environment, or by spooﬁng the old sen-
sors using ﬁlters (say) to allow the original machine to
process information from the new environment.
For a second example, consider the packet switched
internet
which
is
undergoing
a
designed
shift
in
addressing protocol from the IPv4 (32
bits:
e.g.
172.16.254.1) to the IPv6 Internet Protocol (128 bits: e.g.
2001:0db8:85a3:0000:0000:8a2e:0370:7334) [79].
Those
parts of the internet using the older protocol can only
operate in the new environment by either forcing the en-
tire internet to return to the old IPv4 protocol, or by
updating itself to the new IPv6 protocol, or by spoof-
ing incoming and outgoing packets by either using dual
stack routers capable of handling both protocols or by
using network address translation or by tunneling and
embedding schemes [79].
Our third example considers a cellular signal transduc-
tion network which uses many molecular interactions to
implement combinatorial logic functions and alter pro-
tein production dynamics [80]. A change in cell salinity
(say) might alter the eﬃcacy of the signaling pathway,
and this can be repaired only by either returning salin-
ity to normal, re-evolving the entire pathway to suit the
changed salinity, or perhaps by introducing new medicine
molecules to alter existing molecular binding sites to suit
the changed salinity conditions and restore function.
For a ﬁnal example, consider a bureaucracy exchanging
memos or information packets across its network. Ev-
ery large organization in history has faced the challenge
of authenticating its memos [81] and detecting forgeries
[82], including in modern internet based commerce [83].
A forged information packet uses spoofed authentication
codes to subvert the normal operation of the network
for illicit gain. An interesting example occurred in the
last days of the Ching Dynasty [84] where the mother
of the new child Emperor fooled the council of regents
into passing a law requiring that all future oﬃcial edicts
needed a stamp held only by the mother. After that, the
regents could not issue oﬃcial edicts to rescind that pre-
vious decision and return the environment to its initial
state, could not alter their own state by gaining access to
the required stamp, and could not legally spoof or forge
the use of the new stamp. As a result, they lost power.
C.
A Shocked and Confused Chinese Room
Based on the above discussion, it is now possible to
consider how an unexpected and radical environmental
change might put the Chinese Room [11] or the Chinese
Nation [10] or a simulated nervous system [9] into an un-
planned dynamical state characterized by “null” outputs.
These systems, by design, will respond as humans do and
so will likely exhibit a disaster response. Applying tradi-
tional ideas, we might presume that the Room encodes
some syntactical code which, when implemented by the
man within the fully functional Room, causes the inter-
nally fully functional Room to externally simulate dys-
functional cognition. This starkly conﬁrms that merely
simulated behaviours carry no implications whatsoever
about internal computational states (or experiences). In
contrast, our approach seeks to actually duplicate hu-
man cognitive dysfunction in a learning machine, and
use this to model human cognition. When the Chinese
Room faces a disaster, then all pre-existing syntactical
code is either irrelevant (it won’t be called) or becomes
dysfunctional, and the Room likely enters a null dynam-
ical state. The characteristics of this null state can then


## Page 7


7
predict and explain the characteristics of the semantic
shock and confusion experienced by humans in similar
circumstances.
It is diﬃcult to be precise, but a short story about
this situation might be useful.
We ﬁrst note that the
program encoded in the book in the Room would be de-
signed for a ﬁnite set of possible environments (as with
humans), and would include only a fraction of the possi-
ble Chinese characters (as with most Chinese speakers).
Suppose now that the Chinese Room is located within
a sinking and burning ship (similar to examples given
previously) and that consequently, the input slot for the
Chinese characters partially ﬁlls with water and smoke,
and the input symbols coming through the slot are burnt
and smudged and unclear, or are entirely new Chinese
characters unknown to the book program. Because the
characters cannot be identiﬁed, the man in the Room
cannot match the characters to the book and he will be
left fruitlessly leaﬁng through the book looking for some
hint about what symbols to process. Both the man and
the database are still fully functional, and yet no out-
put symbols are being produced.
It is only the alter-
ation of the input data which causes the man and the
Room to cease to operate, and both of them separately
enter a dynamical “null” state. The man is fully oper-
ational and cognitively aware, but with no instructions
to do anything, he becomes passive and unresponsive.
The combined man-book system is fully operational, but
the changed input symbols cannot be processed and the
entire system freezes. The man is part of the frozen dy-
namical state and will experience his own qualia associ-
ated with being in such a state—likely he will be bored.
However, the man’s qualia are in no way related to any
qualia which are, or are not, experienced by the Chinese
Room. Whether or not the room experiences anything,
it will not complain of boredom. Like humans in a disas-
ter situation, the Chinese Room is unable to process or
respond meaningfully to the changed environmental sym-
bols. The characteristics of the Room’s dynamical null
state suggest that the Room is displaying a typical dis-
aster response and, to outside observers, the Room will
appear to be cognitively impaired, dysfunctional, lacking
direction, unresponsive, shocked and confused. Anyone
making objective observations of the components within
the room, i.e.
the man and the book, will be able to
make inferences to predict and explain the semantic expe-
riences that might be experienced by the Chinese Room
should it be so capable. The same objectively observable
dynamical state characteristics can also be used to pre-
dict and explain the subjective semantic experiences of
humans in similar disaster situations.
In our approach, we agree with Searle’s claim that
syntax is not suﬃcient for semantics [85]. We contend
however, that programs are not just syntax as suggested
by the systems reply to the Chinese Room.
We jus-
tify these claims by focusing on a new class of human
semantic symbols invoked during disasters, in which all
prelearned or pre-programmed syntactical programs are
uncalled. In these situations, humans and the Chinese
Room will exhibit a similar dynamical “null” state whose
objectively observed characteristics are reminiscent of the
subjective semantic experiences of humans in these situ-
ations. Our goal throughout has been to support the sys-
tems response to the Chinese Room argument, that there
are non-syntactical and non-preprogrammed dynamical
states that can arise unexpectedly within the Chinese
Room when the environment radically changes, and these
states give insight into human experienced qualia.
D.
The Subjective-Objective Explanatory Gap and
the Properties of Qualia
In 1974 Nagel held that “every subjective phenomenon
is essentially connected with a single point of view, and
it seems inevitable that an objective, physical theory will
abandon that point of view.” The implication was that
no presently available conception gives us a clue how a
physical theory of mind can account for the subjective
character of experience [86]. Later, in 1983, Levine ar-
gued “that psycho-physical identity statements leave a
signiﬁcant explanatory gap, and, as a corollary, that we
don’t have any way of determining exactly which psycho-
physical identity statements are true.”
Consequently,
“there seems to be nothing about [a physicalist state F]
which makes it naturally ‘ﬁt’ the phenomenal proper-
ties of pain, any more that it would ﬁt some other set
of phenomenal properties” [87]. Searle has raised simi-
lar concerns about the inability to bridge the subjective-
objective divide [85].
In our approach, we have argued that a radically
changed environment can place a learning machine into
a dynamical “null” state in which fully functional com-
ponents become quiescent.
We have argued that the
characteristics of this dynamical null state predict and
explain the cognitive response of humans in similar cir-
cumstances, who can be passive, unaware, unresponsive,
and cognitively impaired. We have been explicit through-
out that the objectively observable characteristics of the
null dynamical state of either the machine or the human
can be used to predict and explain the subjective ex-
perience of humans in similar disaster response circum-
stances. Thus, we argue that objectively observable facts
about a learning machine’s dynamical state can be used
to predict and explain the subjective content of humans
in similar circumstances. We thus take steps to partially
close the subjective-objective divide and the explanatory
gap.
Finally, in arguing for eliminativist materialism, Den-
nett summarized the normally understood properties of
qualia as being ineﬀable, intrinsic, private, and directly
apprehensible [88].
We now consider how our model
might explain some of these properties.
First, subjective experiences are considered ineﬀable,
or hard to describe. A person experiencing a null dy-
namical state has impaired functionality and will ﬁnd it
diﬃcult to describe their experiences. Any external ob-
servers observing a passive and unaware disaster response
victim will have non-null states in their own neural net-
works. The more observations made by the external ob-
servers, the richer their own semantic experiences and
the less they replicate victim. Should the observers wish
to experience a null dynamical state, they will have to
alter their own environment suﬃciently to generate their
own null states, and this will unfortunately, impair their
ability to describe their experience. Essentially, learning
a list of syntactical symbols describing a null dynami-
cal state generates a very diﬀerent, non-null, dynamical


## Page 8


8
state.
Second, qualia are considered to be intrinsic, or atomic
and unanalyzable. In our example, the null dynamical
state is not made up of a concatenation or superposition
of several other states, but rather by the absence of all
other dynamical states. Also, as noted above, being in a
null state inactivates analytical capabilities.
Third, qualia are supposed to be private. As discussed
above, making observations of the characteristics of a
null state does not duplicate the experience of running
a null state.
Learning about what it is like to run a
null state requires running the null state in your own
neural system. Others, observing your null state, would
learn some objective facts about your dynamical state,
but would not learn about your subjective experiences.
Finally, qualia are supposed to be directly and imme-
diately apprehensible. When a cognitive system is run-
ning a null state, then many aspects of its operation are
degraded, and this degradation immediately aﬀects any
remaining functional units, now! These units do not have
to read syntactical symbols from registers, and then com-
pare those symbols with lookup tables, and then call a
subroutine that mimics certain behaviours. Indeed, the
very presence of a null state precludes these normal com-
putational steps from occurring. A cognitive system run-
ning a null state immediately displays degraded perfor-
mance, and the associated subjective experience would
also be immediate.
IV.
DYNAMICAL “NULL” STATES IN
MULTIFUNCTIONAL SEQUENTIALLY
PROGRAMMED LEARNING MACHINES
When faced with radical and unexpected environmen-
tal change, humans can become cognitively quiescent—
apathetic, passive, non-responsive, forgetful, and unable
to process information.
We model this response using
learning machines which are unable to process data from
a changed environment and likely generate null dynam-
ical states. We will now examine diﬀerent ways to gen-
erate null dynamical states in neural network learning
machines in the ﬁrst part of this section. In the second
part of this section, we enrich our model by examining
how neural networks can learn to implement multiple
functions in simple programmed sequences as speciﬁed
by environmental data (just as humans do). This will
eﬀectively require the neural network to develop its own
internal computer architecture from scratch, and it will
naturally incorporate environmental data into its nam-
ing and addressing conventions, and into its control-ﬂow
and sequencing commands. This approach is useful as
humans likewise incorporate environmental information
into their internal computer architecture and their simple
programmed and sequenced actions. By modeling how a
network’s programming depends on environmental fac-
tors, we are better able to model a more sophisticated
range of human responses to environmental change.
A.
Neural Network Null States
We are interested in the dynamical state response of
neural networks to environmental change.
Many text-
books on artiﬁcial neural networks [89–91] and on deep
learning networks [92, 93] will implicitly include a dy-
namical equation governing a semi-recurrent feed forward
perceptron network as something like
aL
i
= φ(W L
ijaL−1
j
)
= φ[W L
ijφ(W L−1
jk
aL−2
k
)]
= φ
h
W L
ijφ

W L−1
jk
. . . φ[W 3
rsφ(W 2
sta1
t)]
i
.
(1)
Here, we show a network of L layers with layer 1 tak-
ing input from the environment, and also possibly recur-
rently from the lth layer with 2 ≤l ≤L. We assume the
lth layer contains nl neurons. The ith neuron of layer l,
with output al
i, will take information from the al−1
j
neu-
ron of the previous layer weighted by values W l
ij. The
input to neuron al
i is then W l
ijal−1
j
where we assume an
implied summation over repeated indices. As usual, if the
neuron’s total input exceeds its bias value, W l
ijal−1
j
> bl
i,
the neuron will ﬁre. The bias values can be folded into
the weight matrices by the usual process of adding an
extra weight into each neuron equal to the negative bias
W l
i(nl+1) = −bl
i and assuming an additional neuron in
every layer that is always active, al
nl+1 = 1. In general,
we desire our neurons to be quiescent in the absence of
input (though alternative choices could be made, as when
a self-initiating oscillatory circuit is required). This can
be achieved by setting all bias values to be positive, so
that in the absence of input each neuron remains oﬀand
quiescent. The total input to each neuron, W l
ijal−1
j
= x,
is then fed into a nonlinear sigmoid function
φ(x) =
1
1 + e−x ,
(2)
though other functions provide better performance for
deep networks. As usual, the neuron ﬁres iﬀthe argu-
ment x > 0.
It would generally be considered impossible to analyti-
cally “solve” the above dynamical equation as interesting
networks can have hundreds of millions of parameters.
We have argued however that even the largest and most
sophisticated of networks can enter a known state, a null
dynamical state, when faced with a radically changed
environment well outside its previous training set. This
novel data will cause the network to act just like any
other untrained network faced with unlearned data, and
it will produce random noise. It will be unable to extract
information from that novel data to pass to subsequent
layers, and in turn, these layers will be unable to extract
or process any useful information. Consequently, the net-
work enters a null dynamical state where each subsequent
layer of neurons switches oﬀ, one after the other. Irre-
spective of how complex the network is, and how well it is
trained, we can “solve” the network dynamics. We then
have a mathematically speciﬁed and objectively known
dynamical state which predicts and explains the subjec-
tive cognitive sensations experienced by people in similar
circumstances.
There are many diﬀerent ways to generate a null dy-
namical state in a neural network governed by Eq. 1.
Zero Propagation: al
i ≈0: Because the bias values
bl
i are positive, neurons will be quiescent in the absence
of input, and zero inputs to any layer will propagate to


## Page 9


9
generate a general dynamical null state in all downstream
regions.
In brief, when al−1
k
is a zero vector in some
region, then al
j = φ(W l
jkal−1
k
) = φ(−bl
j) = 0 as bl
j > 0.
Humans can experience this dynamical state by closing
their eyes and listening to silence. It may seem overly
simple, but the ﬁrst analytic models of human experience
should be simple.
Untrained Weights: W l
ij ≈0: When a region of our
network is untrained and has weights close to zero, then
all layer outputs in that region will be zero, and these
zeros will propagate. That is, when W l
ij ≈0 we have
al
i = φ(W l
ijal−1
j
) ≈φ(−bl
i) = 0 as bl
j > 0. Humans can
generate and experience this state simply by listening to
an unknown language. Humans will experience qualia as-
sociated with the absence of information processing, and
this semantic experience is predicted by the null dynam-
ical state.
Null States by Design: It also seems possible that
the human cognitive system will deliberately not process
information in a number of situations. For example, the
vision system doesn’t process data during eye saccades
(rapid eye movements across the ﬁeld of view), dream
experiences fade from memory and are generally unavail-
able for later processing, and having an attentional spot-
light focused on one stream of data means that many
other streams are unattended and are zeroed. Further,
the cognitive system suﬀers limitations which impact cog-
nitive processing. For example, humans can fail to pro-
cess environmental information in the two cases where
information either arrives so fast it averages to zero, or
so slowly that the many neural layers trained to identify
novelty and change cease to generate output. In either
case we have al
i ≈0. Humans can experience the ﬁrst
case by playing a fast-paced video game at too high a
level, and can experience the second case by becoming
bored perhaps.
Novel Inputs Outside the Training Set: a /∈T :
Our main focus of interest is how humans and learning
machines both fail to process novel inputs from well out-
side their previous training sets.
Because they cannot
extract information from their inputs they generate zero
output, and these zeros propagate throughout the net-
work. The generated null dynamical state predicts the
cognitive experiences of humans in these situations. An
example of this process will be given after we examine
how our networks can implement multiple functions in
simple programmed sequences as speciﬁed by environ-
mental information.
B.
Multifunctional Sequentially Programmed
Networks
We suppose that two researchers, denoted A for Alice
and B for Bob, are each training high capacity, recurrent,
deep neural networks with many layers (> 20) and with
each layer consisting of many (> 104) neurons.
Each
network will eventually be required to learn to imple-
ment multiple functions in programmed sequences, and
this normally requires a relatively sophisticated computer
architecture with control-ﬂow capabilities. Human chil-
dren take years to learn how to enact programmed se-
quences of actions. Like a human child, each network is
a sealed black box meaning that Alice and Bob are un-
able to specify any aspect of the design of their neural
network. For instance, they cannot shrink the size of a
particular hidden layer to force a data compression at
the cost of slower learning, or conversely, expand hidden
layer size to improve learning at the cost of a greater
chance of overﬁtting. The researchers cannot specify the
modular structure and connectivity of the network, data
encoding formats, or how the network is to sequence and
control data ﬂow between modules and functional units.
As a black box, Alice and Bob must face the fact that
their network will have many learning diﬃculties, just
as humans do. These learning diﬃculties can themselves
be used to model human learning disabilities. Because
the required computer architecture is not designed into
the hardware of the network, it has to be learned by
the network as a software emulation embedded within
the functions learned by the network. To add an em-
ulated computer architecture alongside the data being
processed requires the addition of identiﬁcation, sequenc-
ing, addressing, looping, and other control tags into each
processed data vector. We illustrate this now.
First, each network is tasked to learn many functions
simultaneously.
We suppose the network is embodied
with many input channels (left and right and front and
rear cameras and microphones) and that the machine has
the ability to speak or write its outputs. Within the ma-
chine, all the diﬀerent input data streams are addressed
under software control to many diﬀerent functional mod-
ules for processing and combination. Each layer of pro-
cessing interprets the data at a higher and higher level
and adds information to the data stream accompanied by
control tags to ensure appropriate downstream process-
ing. The embedded control tags within Alice’s machine
might indicate that a data stream is sourced from real-
ity (denoted by bit pattern R), that it was received at
the current time (indicated by a bit pattern T1), that it
shows Alice (denoted by bits A) in her laboratory (bits
L) holding a card containing symbols (with input bits
“say +, 4, 2”).
In this case, the network will learn to
process the input (R, T1, A, L, say, +, 4, 2), and say the
answer 6. Other example input-output pairs involving
four functions might include
Input →Output
R, T1, A, L, say, +, 4, 2 →say 6
R, T1, A, L, say, −, 4, 2 →say 2
R, T1, A, L, write, ∗, 4, 2 →write 8
R, T1, A, L, say, /, 4, 2 →say 2.
(3)
These examples illustrate a straightforward input-output
mapping that can readily be implemented in any suitable
network.
Second, the machine will need to learn to implement
simple sequential programs. We presume that once the
machine has learned the above four functions, Alice will
start teaching it other simple mathematical functions,
e.g. n2, as well as how to implement simple sequenced
operations as speciﬁed by input programs, e.g. 1+2∗3 or
1+2∗(3−4/2). To accomplish such sequential processing,
the machine will need to recognize the order of operator
precedence and recurrently route the input expression
through the machine multiple times in order to complete
its evaluation. To accomplish this, the machine will need
to add control instructions to the input data expression


## Page 10


10
to ensure appropriate addressing, looping, and termina-
tion procedures. Human children initially ﬁnd this very
diﬃcult, and are initially trained to use paper and pen-
cil to implement these controls. The association between
input data and control codes, essentially data packets
containing both data and processing and addressing in-
structions, leads naturally to a packet-switched network
architecture. In hypothesizing a packet switched learning
machine as a model for human cognition, we follow Ref.
[94, 95].
Third, we presume the network has an associative
memory that can eﬃciently store previous learning ses-
sions and can recall simultaneous multiple sessions on
demand to assist with solving current problems. For in-
stance, at a later time (T2) the machine’s memory can
generate a data stream (tagged by bits M) which encodes
the earlier real input-output packet via the bit pattern
[M, T2, (R, T1, A, L, say, +, 4, 2 →6)].
(4)
Further layers of recursive packet embedding might be
possible. At time T3, the machine can access a memory
of having a memory at time T2 of an earlier real event at
time T1 via
{M, T3, [M, T2, (R, T1, A, L, say, +, 4, 2 →6)]}.
(5)
Fourth, we expect the network to be able to apply
a broad range of analytical functions to its input. For
instance, the machine might learn to respond to ques-
tions like “Is Alice visible?” by polling its input vision
data streams for packets which are time stamped “now”
and embed Alice’s code A.
To questions like “Is Bob
present?”
the machine might poll its processed data
streams for packets like (R, Tnow, B) and answer “Yes” if
these packets exist. To questions like “Was Alice present
as time T1?” the machine might present a bit string like
(T1, A) to its memory to trigger associations that return
packets like [M, T2, (R, T1, A)]. If such packets exist, the
machine might answer “Yes.”
C.
Speciﬁc and General Function Names Learned
from the Environment
As seen above, our machine makes extensive use of
data packets containing data, function names, and con-
trol tags, though interpreting which bits belong in which
category is very ﬂuid. In the input packets given above,
the “say” or “+” bits could be interpreted as either plain
input data, or as function names, or as control tags spec-
ifying later sequential machine operations. A number of
diﬀerent viewpoints are possible, and examining these in
turn will suggest how we can embed a sequential program
within the data packets processed by a neural network,
and some of the diﬃculties which can arise.
For a ﬁrst viewpoint, the bit pattern “say, +, 4, 2” has
a natural interpretation as a multi-component function
name “say, +” being applied to the data “4, 2”.
As
the function name comes directly from the environment,
any environmental change can corrupt learned function
names and hence machine operation.
A second viewpoint takes the single four-input func-
tion learned by the network f(say, +, 4, 2) with four in-
puts, and applies a Currying operation to reduce dimen-
sionality to two via fsay,+(4, 2). Alternative inputs then
generate diﬀerent reduced functions, with f(say, −, 4, 2)
becoming fsay,−(4, 2). As noted in Ref. [96], the weights
of a neural network are normally considered to encode
a single function, but when using Currying operators
the weights instead encode an “interpreter” able to re-
conﬁgure the network to implement diﬀerent operations
under the control of the diﬀerent control codes in the in-
put data, just like any other stored program computer.
This viewpoint again makes it evident that environmen-
tal change altering the input data packets can disrupt
machine processing.
A third viewpoint sees these control codes as imple-
menting a combinatorial logic combining the multiple
functions learned by the network and selecting for exam-
ple, alternatives like (say, +) or (write, ∗). Incorporating
a combinatorial logic within function names allows a leap
in the computational complexity of a network—a simi-
lar idea was used to explain increased eukaryotic multi-
cellular complexity over that of single-celled prokaryotes
[97, 98]. Again, when a machine’s controlling combinato-
rial logic is sourced from the environment, this makes it
natural to expect that environmental change can disrupt
machine operations.
The ﬁnal fourth viewpoint recognizes that embedding
control codes and data within a single data packet intro-
duces a data ﬂow architecture [99, 100], currently posited
as one pathway to exascale computing [101–103]. The
data packets we have seen above (say, +, 4, 2) combine
operands and data, and these packets are actioned or ﬁre
when all operands are present and correct. Self-evidently,
unexpected environmental change can mean that these
operands are absent or incorrect so again the machine
will become dysfunctional. Other approaches to multi-
tasked neural networks include Refs. [104–106].
The above viewpoints make it clear that data packets
combining data and instructions can allow complex se-
quential programming. In parsing its input data packets,
the machine must learn by itself which input data is rel-
evant or irrelevant to the task at hand. In making these
decisions, there is a spectrum of possible choices that the
machine might make, with no one choice being deﬁni-
tively better than others in every circumstance. In partic-
ular, the machine might assume that the learned function
should have high generality, wide applicability and high
transferability, and can achieve this by having the short-
est name possible.
Given input R, T1, A, L, say, +, 4, 2,
the machine learns to ignore inputs R, T1, A, L to give the
shortest possible name to its learned function “say, +”
to achieve greatest generality. Conversely, the machine
could assume that a learned function is highly speciﬁc
to the current locality and to the current teacher, and
achieves this by having the longest name possible. That
is, given input R, T1, A, L, say, +, 4, 2, the machine might
name its learned function A, L, say, + so this function is
activated only when Alice is present in her laboratory.
Humans routinely face the same choice.
When learn-
ing a new function, human students must likewise choose
between generality and speciﬁcity, as some learned func-
tions will be highly general while others will be speciﬁc
to one location and one time and one person. As there is
no general rule, both the learning machine and the hu-
man can often choose incorrectly. Again, this choice can
lead to dysfunctionality, and this is the topic of interest
in this paper.


## Page 11


11
D.
A Learned Square Function Faces
Environmental Change
Our goal is to examine how our neural network can
become dysfunctional when facing environmental change.
We can illustrate this process by considering how Alice
might teach the network to implement an n2 function
applied to digits 0-9 via inputs like
Input →Output
R, T1, A, L, say, n2, 2 →say 4
R, T1, A, L, write, n2, 0 →write 0.
(6)
For illustrative purposes, suppose that the bit pattern
for R, Ti, A, L is decimal 16 = binary 10000, the pattern
for say in both the input and the output is decimal 4 =
binary 100 while write is decimal 6 = binary 110, and the
pattern for n2 is decimal 7 = 111. Assume the input and
output numbers have standard binary encodings. Alto-
gether, the bit patterns of the mappings to be learned
might be something like
Input →Output
R, Ti, A, L, say, n2, 2 →say 4
10000, 100, 111, 0010 →100, 00100,
(7)
or
Input →Output
R, Ti, A, L, write, n2, 2 →write 4
10000, 110, 111, 0010 →110, 00100.
(8)
Obviously, the most eﬃcient mapping would simply use
an identity to map the input verb “say” or “write” di-
rectly to the output, and another function to map the
input number i to the output number i2. However, the
network is large and powerful and performing a random
walk around weight space so it might not ﬁnd these ef-
ﬁcient maps, and might instead incorporate unnecessary
information into its learned mappings. For instance, the
verb mapping might incorporate the R, Ti, A, L ≡10000
value into its input via
Input →Output
10000, 1x0
|
{z
}, 111, 0010 →1x0
fverb(10000, 1x0) →1x0
f dec
verb(132 + 2x) →4 + 2x,
(9)
where x = 0 for “say” and x = 1 for “write”. That is, the
decimal function f dec
verb(132+2x) maps an input of decimal
132 + 2x ≡(10000, 1x0) to the desired output (4+2x).
Similarly, the “square” mapping might incorporate the
R, Ti, A, L ≡10000, the n2 ≡111, and the input digits
0010 into its input via
Input →Output
10000, 111, 0010
|
{z
} →00100
fn2(10000, 111, 0010) →00100
f dec
n2 (2160 + n) →n2.
(10)
Here, the decimal f dec
n2 (k) function maps an input of dec-
imal k = 2160 + n ≡(10000, 111, 0000) + n to the de-
sired output n2. Altogether, the machine has eﬀectively
learned two mappings equivalent to
fverb(k = 132 + 2x) = k −128 = 4 + 2x
fn2(k = 2160 + n) = (k −2160)2 = n2.
(11)
Suppose now that Alice has trained the network and
personally tested it within her laboratory and has shown
that it is able to say or write square numbers from 0
to 9 with 100% accuracy. Unfortunately, these learned
mappings fail as soon as the location or the person in-
put strings are changed from (R, Ti, A, L, say, n2, 2) to
(R, Ti, A′, L′, say, n2, 2). To illustrate, suppose the origi-
nal and altered inputs have encodings
(R, Ti, A, L, say, n2, 2) ≡(10000, 100, 111, 0010)
(R, Ti, A′, L′, say, n2, 2) ≡(10101, 100, 111, 0010).(12)
The
altered
input
10101, 100 asks
the
verb
func-
tion to process fverb(172) while the altered input
10101, 111, 0010 asks the square function to process
fn2(2802) in decimal, and these give
fverb(172) = 172 −128 = 44 ≡101100 ̸= say
fn2(2802) = (2802 −2160)2 = 6422 ̸= 4.
(13)
Here, we note that the output verb code is not well
formed and will be unable to activate any output mech-
anism. When naming and addressing codes are absent
or ill formed, then no information can ﬂow to subse-
quent layers. When humans and learning machines in-
corporate environmental information within their learned
functions, then environmental change can destroy those
learned mappings and drive outputs so far out-of-range
that no further functional processes can be called. The
human and the learning machine can then enter a null
dynamical state.
V.
ATTACHMENT, GRIEF, AND SPOOFING
THE NETWORK
Our path forward should now be clear—we have sug-
gested that multifunctional learning machines will often
learn functions which are speciﬁc to particular individu-
als and places so that unexpected environmental change
can destroy previously learned functions and generate
dynamical null states. Consequently, these learning ma-
chines will respond by either seeking to repair the envi-
ronment, by relearning the changed environment, or by
spooﬁng their original network addressing schemes to al-
low continued operation in the altered environment. We
now seek to model situations where human learning is
so dependent on people and places that environmental
change causes cognitive dysfunction, leading to attempts
to either repair the environment, to retrain to suit the
new environment, or to spoof their network. We turn to
model human experiences in cognitive symbols such as
transference, attachment, grief, and the human response
to grief.
A.
Transfer of Location or Context Based Learning
Students and people often exhibit an inability to
transfer learning between diﬀerent locations or contexts


## Page 12


12
[107, 108]. For example, students might ﬁnd it diﬃcult
to transfer trigonometric techniques learned in a mathe-
matics classroom to a science classroom, and fail to even
recognize that trigonometry is the basis of navigation and
construction methods used outside the classroom.
We suppose that Alice has spent some considerable
time in her laboratory training her network to implement
many varied functions (denoted fj) using input output
mappings like
Input →Output
R, Ti, A, L, say, fj, n →say fj(n).
(14)
We further suppose that, unbeknownst to Alice, many
of these learned functions have incorporated the location
code L into their naming and addressing schemes. How-
ever, this never becomes apparent to Alice as all testing
occurs within the laboratory where the machine is fully
functional. As soon as Alice takes the machine to a new
location though, L →L′ say, many of the functions fj(n)
could become dysfunctional causing the network to en-
ter something like a dynamical null state. In trying to
understand this, Alice might return the machine to the
original laboratory, L, where it instantly recovers its full
capabilities.
Our learning machine duplicates the learning transfer
diﬃculties faced by humans when they have improperly
and unknowingly incorporated location information into
their function names. Any environmental alteration can
then invalidate the calling of functions, and the learning
machine can enter a null dynamical state, equivalent to
the blank state experienced by humans in these situa-
tions. For example, a student can pass a trigonometry
test within the classroom, and become completely blank
when asked to determine a navigational bearing outside
the classroom. The characteristics of the machine’s dy-
namical null state predict and explain the sensations ex-
perienced by people in these situations.
Further, the
model suggests remedies commonly used by educators to
enable learning transfer—Alice and other teachers should
vary their location (or more generally, their context) dur-
ing learning to enable students to more broadly apply
their learning. This model duplicates human responses
in situations like classrooms, and can be readily gener-
alized to cases like culture shock [109] or future shock
[110].
B.
Attachment
Suppose now that Alice realizes she can correct the
location dependencies of her network by undertaking a
lengthy retraining process involving many new input-
output pairs like
Input →Output
R, T1, A, L, say, fj, n →say fj(n)
R, T1, A, L′, say, fj, n →say fj(n).
(15)
By varying locations, L, L′, L′′ . . . , the machine even-
tually learns that the location code is unrelated to the
function name or its domain of applicability. Unfortu-
nately, this new training set still leaves the machine with
function names that remain dependent on the code for
Alice A. As a result, when Alice is absent and Bob is
conducting tests, it is discovered that the machine’s per-
formance depends on Alice being present. In particular,
we suppose that when Alice is present and the machine is
fully functional, all of the machine’s input packets have
leading bits equivalent to R, Ti, A ≡10000 (after retrain-
ing to remove the location dependence) and these bits
have been incorporated into many function deﬁnitions.
In contrast, when Bob is testing the machine, the input
packets have leading bits equivalent to R, Ti, B ≡10110.
As shown previously, this can lead to inoperative func-
tions.
Suppose now that 80% of all the network’s learned
function names have incorporated the Alice code A. Con-
sequently, when Alice is present all functions are called
correctly and produce the correct outputs, while when
she is absent, the machine’s functionality is reduced to
20% and the machine mainly generates dynamical null
states.
As previously, the machine’s learned functions
and its hardware are perfectly operational; it is only that
the environmental change destroys the learned machine
naming and addressing architecture which generates dys-
functional null states. In some sense, the machine has
become attached to Alice.
To explore this idea further, suppose that Alice has
programmed the machine to optimize some score with
points being awarded for each correct answer to ques-
tions. Suppose further that the machine has noted that
keeping Alice centered in its ﬁeld of view maximizes its
score and it then learns to rotate its cameras to keep Alice
centered as she moves around the laboratory. On those
occasions when Alice has asked questions while ducking
out of sight behind a partition say, the machine noted
its declining performance and learned that activating its
wheel motors to keep her in view resulted in an increased
score. The machine might then generalize this and learn
to use its wheel motors to follow Alice when she leaves
the room in order to increase its score. It might then be
reasonable to predict that the machine will seek to follow
Alice everywhere she goes to the extent possible in order
to maintain its functionality. The machine has now be-
come overly attached to Alice, and will stalk Alice to the
extent possible.
Our network will experience and feel nothing as it lacks
these capacities. Further, our model leaves out the com-
plex interplay of the diﬀerent drivers—the sex drive, at-
traction, and attachment—and the diﬀerent emotion sys-
tems associated with speciﬁc hormones and neural struc-
tures in humans [111]. However, our machine will act as
if it is attached allowing the prediction that, when at-
tached, a machine or human will perform perfectly (eas-
ily, readily, ﬂuently, comfortably) while in the presence of
their signiﬁcant other, but will exhibit a null state (blank,
dysfunctional, vacant, listless, unmotivated) when their
signiﬁcant other is absent. It might also be predicted that
the machine and the human might only choose to perform
certain functions when their “partner” is present, and
will avoid those activities when they are absent. These
predicted behaviours are routinely observed in attached
mammals and humans who prefer the company of con-
speciﬁcs, maintain close body contact, display separation
anxiety, attempt to restore close contact after separation,
report feelings of comfort and reduced anxiety when in
contact with their partner, and have their lives deeply


## Page 13


13
entwined with their partners [111].
Interestingly, Bowlby’s attachment theory [112–114]
models organisms as being cybernetically controlled with
complexity ranging from primitive organisms possessing
reﬂex-like “ﬁxed action patterns” to organisms which are
behaviourally ﬂexible and able to adapt to changes in
their environment. Bowlby noted however, that this very
adaptability exacts a price as more complex organisms
can be more easily subverted from optimality [115]. In
this paper, it is precisely those networks with suﬃcient
complexity to learn their own naming and addressing ar-
chitecture that can become dysfunctional because that
very same architecture.
C.
Loss and Grief
After Alice and Bob note that the network appears to
be attached to Alice, and, knowing the linkages between
attachment theory and bereavement theory [61, 116, 117],
they decide to investigate whether the machine might
also be used to model grief. To engender this state, Alice
hands the machine over to Bob and never again enters
the laboratory to teach the machine.
Suppose again that the learning machine has about
80% of its functionality dependent on Alice being present
and visible, and that the machine becomes largely dys-
functional and non-responsive when Alice is permanently
absent.
Bob’s anthropomorphized description of the
“grieving” learning machine might be that it appears
vague, vacant, undirected, unmotivated, unable to con-
centrate, hopeless, and impaired. Based on these obser-
vations, Alice and Bob are able to make accurate pre-
dictions about the human response to grief and loss.
They might predict that grieving humans could expe-
rience numbness, a lack of energy, emptiness, heaviness,
disorganization, withdrawal, absentmindedness, forget-
fulness, and a lack of concentration; all symptoms noted
in Sect. II in this paper. Our network can exhibit a null
dynamical state with characteristics which predict and
explain the qualia experienced by grieving humans.
We ﬁnally note that humans were never trained how
to grieve—grief arises naturally and spontaneously. Sim-
ilarly, our network was never trained or programmed to
grieve, and its symptoms likewise appeared naturally and
spontaneously. This is because, we claim, our network
accurately models and duplicates human learning mech-
anisms rather than merely simulating human behaviours.
In turn, our model suggests that as humans learn mul-
tiple new functions from a parent or partner, they are
learning a naming and addressing architecture which in-
corporates environmental information about their part-
ners within their internal addressing schemes.
D.
Grief Response
Alice and Bob now decide to see how the machine
responds to its altered environment and its “grieving”
dynamical state, and to see if this response can predict
and explain aspects of the human response to grief. Al-
ice and Bob might well reason that a learning machine
might seek to restore its functionality in three diﬀer-
ent ways.
These are to either return the environment
to its original state by having Bob replaced by Alice,
R, Ti, B →R, Ti, A, or to retrain the network so all func-
tions operate when Bob is present, or to spoof the altered
input packets R, Ti, B ≡10110 so that they look like the
original R, Ti, A ≡10000 allowing them to be correctly
processed by the unchanged machine. This last option
merely involves rewriting some bits which should be fea-
sible.
With regard to the ﬁrst option, we have noted above
that the machine will indeed try to maintain Alice within
its environment to the extent possible, perhaps by stalk-
ing Alice to maximize its score. However, if Alice is per-
manently departed (to simulate death), then the machine
cannot avail itself of this option. The researchers might
still predict though, based on the machine’s “desire” for
Alice to return that humans suﬀering grief might also
pine for their loved one and desire their return.
With regard to the second retraining option, Alice and
Bob are aware that retraining all the inoperative func-
tions of the machine will take just as long as the origi-
nal training, perhaps many months. Based on this, they
might predict that human recovery from grief might also
involve months of slow retraining.
Finally, the third option does not involve making
changes to either the altered environment or the many
functions learned by the machine. Rather, this option
seeks to simply spoof the altered input packets from
R, Ti, B ≡10110 to the original R, Ti, A ≡10000 so they
can be processed by the existing machine without further
training. Alice and Bob are very interested in exploring
this option as it potentially could save months of work.
To spoof the input packets, Bob needs to provide another
source of the input code A to the learning machine. Bob
might ﬁrst try to use photographs of Alice (with bit code
A′) which perhaps causes the machine to perceive the
input bits R, Ti, A′ ≡10100 which is a little closer to
the desired R, Ti, A ≡10000. We might guess that some
more of the machine’s functions become operational—
rather than being 80% dysfunctional the machine might
be only 60% dysfunctional.
Based on this, Alice and
Bob might predict that grieving humans would ﬁnd pho-
tographs of their departed loved ones comforting because
of a partial return of functionality.
Refusing to give up, the researchers might realize that
the network contains one source which can give a high
ﬁdelity copy of Alice’s bit pattern as perceived by the
machine. The network’s memory, asked to recall Alice,
provides memory-tagged and time-stamped packets like
[M, Tj, (R, Ti, A)] ≡[11010(10000)] (say). Here we indi-
cate that the memory packet contains an exact copy of
the bit string generated by Alice in reality. It is possible
that some of the network’s trained functions will be able
to access the embedded A bit string and recover their
functionality. This leads to the prediction that grieving
humans might also take comfort from remembering their
departed loved ones, and that these memories will ease
the symptoms of grief and partially restore function.
Finally, Alice and Bob might consider teaching the
network a single new function to spoof its packets to
regain functionality.
Most of the functions learned by
the network can readily read, write, delete and alter the
control tags attached to their input and output data
packets.
The new spooﬁng function simply needs to
strip the memory control tags from the memory pack-


## Page 14


14
ets [M, Tj, (R, Ti, A)] ≡[11010(10000)] to generate new
packets (R, Ti, A) ≡10000.
The memory packets en-
code a memory of Alice in reality while the altered pack-
ets indicate that Alice is present in reality. As soon as
these packets are present within the network, function-
ality will be widely restored and approach 100% because
the machine now perceives Alice to be present in reality.
Of course, altering memory tags into reality tags is not
something that you want your machine to do often—if
this happened routinely then it wouldn’t be able to dis-
tinguish what is real from what is remembered. However,
when the costs of being dysfunctional are high, and re-
training times are long, then it might well be beneﬁcial
to occasionally alter a memory tag into a reality tag.
After the successful spooﬁng operation and the restora-
tion of functionality, the network might well respond to
questions like
Question
Response
Is Alice visible in the room?
No
Can you touch Alice?
No
Who is visible in the room?
Bob
Is Alice present in the room?
Yes
The network now has internal data packets giving evi-
dence Alice is currently present in the room but is invis-
ible and cannot be touched. In eﬀect, the network now
believes in the presence of invisible people, i.e. spirits.
Having been spoofed, the network’s perception of real-
ity now diﬀers from reality. A machine that cannot feel,
or think, or experience sensations can develop dynamical
states containing information that invisible people exist
and can be present in a room, and this dynamical state
instantly allows the machine to resume full functionality.
Alice and Bob are now in the position of being able
to predict that grieving humans might also learn new
functions to spoof their memory data packets and come
to believe in invisible and immaterial people who cannot
be seen or heard but who are nonetheless present. When
this new function is learned, it might be predicted that a
human will achieve an almost instantaneous restoration
of functionality, and that this restoration might be taken
as ample justiﬁcation for the validity of the new learned
function.
VI.
CONCLUSION
In this paper, we have modeled a new class of hu-
man semantic symbols experienced when humans become
dysfunctional on extreme environmental change. Rather
than having a fully functional machine merely simu-
late dysfunctional behaviour, we duplicated the mech-
anism causing human dysfunctionality. Human children
don’t spend months learning how to become attached or
to grieve, and our machines don’t get taught functions
called “attachment” or “grief”. Rather, our neural net-
work uses environmental inputs to learn a computer ar-
chitecture able to implement multiple functions and sim-
ple sequential programs. Because environmental infor-
mation is deeply embedded within the learned computer
architecture, it is natural that environmental change dis-
rupts machine operation and, we have argued, typically
generates a null dynamical state. The characteristics of
this null state can then predict and explain the charac-
teristics of human experiences of environmental change.
In its simplest representation, our machine learns to
apply a function f to environmental inputs E (containing
person A and location L information say) to generate
some desired output y via
y = f(E).
(16)
Unexpected environmental change E →E′ moves the
input well outside the machine’s prior training set which
disrupts internal operations suﬃciently to generate a null
dynamical state via
0 = f(E′).
(17)
We have argued there are three main ways that the ma-
chine may recover. The ﬁrst is to take physical steps to
restore the changed environment back to its original state
E′ →E to regain the machine functionality of Eq. 16.
The second is to spend time teaching the network a new
function f ′ to suit the altered environment via
y = f ′(E′).
(18)
The third approach is to have the machine learn a new
internal function g to preprocess and convert the al-
tered environmental input E′ back to its original form
g(E′) = E.
This means the internal machine percep-
tion of the environment now diﬀers from the actual envi-
ronment which restores machine operation via something
like
y = f(E) = f[g(E′)] = f ◦g(E′).
(19)
Our approach relating a dynamical state rather than
syntactical program code to cognitive semantic symbols
provides a concrete example of the systems reply to
Searle’s Chinese Room argument. In this approach, sym-
bols are not static neuron ﬁring patterns but dynamical
states of the entire learning machine. In this, we hope to
have partially captured Hofstadter’s idea of the “active”
dynamical symbols underlying Aunt Hillary’s cognition
[8]. And because the dynamical state is observable and
mathematically deﬁned, the gap between objective ob-
servations and subjective experience has been partially
closed. Lastly, by recognizing that the learned computer
architecture likely exploits packets of information con-
taining both data and control tags, we were able to con-
sider how diﬀerent changes in the environment might af-
fect the network, and were thus able to develop models
of a range of human cognitive symbols including trans-
ference, attachment, grief, and typical responses to grief.
We accomplished all this in a small and simple model
lacking complex abilities because we mimic humans who
are unable to access prior learning when facing environ-
mental change.
It has long been assumed that because human cog-
nition is complex and diﬃcult to understand, then any
successful artiﬁcial intelligence approach will likewise be
complex and diﬃcult to understand.
This assumption
reinforces our prejudices suspiciously well. However, the
success of our extremely simple approach implies that
human cognition is simple at its core, and a moments
thought suggests this is a more reasonable assumption to


## Page 15


15
make. Few people could design a set of function map-
pings to emulate a computer architecture and yet this
is what our neural networks must learn in a few short
years. Human cognition is likely based on the simplest
possible computer architecture capable of implementing
multiple functions in sequential programs. Needless to
say, this architecture will likely be highly error prone,
but it is these errors which will model many aspects of
human cognition.
Our modeling approach can retrodict, as a ﬁrst approx-
imation, the development of human cognitive capacities
over evolutionary timescales. Simple neural networks ap-
ply one function to data and have no need for control
tags or a combinatorial logic learned from the environ-
ment. Based on this, we would predict that simple ani-
mals neither exhibit nor experience attachment or grief.
More complex machines might possess control tags to
implement simple sequential programs learned from the
environment, and when these control tags incorporate
enough environmental information then these machines
can display attachment and grief behaviours. This allows
the prediction that animals which learn extensively from
their families and their environment can exhibit attach-
ment, grief and mourning behaviours.
These expecta-
tions seem reasonable. It does indeed appear that simple
animals lack complex cognition and show no attachment
or grief behaviours, while more complex animals appear
to possess a mind [118–121].
Chimpanzees appear to
exhibit grief and mourning behaviours [122, 123], and
show preliminary indications of the beginning of ritual
[124]. Further, archeological evidence appears to show
that small brained hominins were going to great lengths
to bury their dead [125–128], while showing little indica-
tion of complex symbolic cognitive capacities.
Eventually however, as animals become more complex
and oﬀspring learn vast numbers of functions and capac-
ities from their families, then grief might become so de-
bilitating that evolutionary pressures could tip to favour
the development of a spooﬁng ability. We can then pre-
dict that highly complex machines and animals might be
so aﬀected by grief that it becomes beneﬁcial to learn
new spooﬁng functions to relieve the symptoms of grief.
Machines and animals capable of control tag rewriting
will come to believe in spirits and will develop a sense
of spirituality. This delinking of perceived reality from
actual reality might then allow the development of the
enriched symbology that is such a feature of human cog-
nition. It is only when you can rewrite reality that you
can be truly creative—an imagined story becomes reality,
reality becomes imaginary, actual histories are reimag-
ined, a stone becomes jewelry becomes love, and so on.
Many have speculated about how homo sapiens under-
took a “great leap forward” [129], a “cognitive revolu-
tion” [130], and became behaviourally modern [131, 132]
about 100,000-70,000 years ago.
It has been hypoth-
esized that homo sapiens share a “ﬁctive language” in
which ﬁctional stories—money, religion, political and le-
gal structures—become reality [130]. It is possible that
having a machine develop illusions, a mismatch between
perception and reality, is a ﬁrst step in developing the
ability to experience qualia [133]. Here, we model this
cognitive leap as stemming from the development of a
spooﬁng ability equivalent to a control tag rewrite archi-
tecture in the human cognitive system, as a complement
to other approaches [134, 135].
[1] D. J. Chalmers, Journal of Consciousness Studies 2, 200
(1995).
[2] D. J. Chalmers, The Conscious Mind: In Search of a
Fundamental Theory (Oxford University Press, 1996).
[3] A. M. Turing, Proceedings of the London Mathematical
Society 42, 230 (1937).
[4] A. M. Turing, Mind 49, 433 (1950).
[5] A. Newell and H. A. Simon, Communications of the
ACM 19, 113 (1976).
[6] A. Newell, in The Impact of Herbert A. Simon, edited
by D. Klahr and K. Kotovsky (Erlbaum and Associates,
1988).
[7] N. J. Nilsson, in 50 Years of Artiﬁcial Intelligence: Es-
says Dedicated to the 50th Anniversary of Artiﬁcial In-
telligence, edited by M. Lungarella, F. Iida, J. Bongard,
and R. Pfeifer (Springer, 2007), vol. 4850, pp. 9–17.
[8] D. R. Hofstadter, G¨odel, Escher, Bach:
An Eternal
Golden Braid (Basic Books, 1979).
[9] D. C. Dennett, Synthese 38, 415 (1978).
[10] N. Block, in Perception and Cognition: Issues in the
Foundations of Psychology, edited by C. W. Savage
(University of Minnesota Press, 1978).
[11] J. Searle, Behavioral and Brain Sciences 3, 417 (1980).
[12] G. Rey, in The Nature of Consciousness, edited by
N. Block, O. Flanagan, and G. Gzeldere (MIT Press,
Cambridge, MA, 1997), pp. 461–482.
[13] D. C. Dennett, Consciousness Explained (Little, Brown,
and Co, Boston, 1991).
[14] R. Penrose, The Emperors New Mind:
Computers,
Minds and the Laws of Physics (Oxford University
Press, Oxford, 1989).
[15] C. Moore, Physical Review Letters 64, 2354 (1990).
[16] A. Chalcraft and M. Greene, Eureka 53, 5 (1994).
[17] M. A. Boden, in The Philosophy of Artiﬁcial Intelli-
gence, edited by M. A. Boden (Oxford University Press,
1990).
[18] S. Harnad, Physica D 42, 335 (1990).
[19] M. Taddeo and L. Floridi, Journal of Experimental and
Theoretical Artiﬁcial Intelligence 17, 419 (2005).
[20] S. S. Adams, I. Arel, J. Bach, R. Coop, R. Furlan,
B. Goertzel, J. S. Hall, A. Samsonovich, M. Scheutz,
M. Schlesinger, et al., AI Magazine 33, 25 (2012).
[21] B. Goertzel and C. Pennachin, eds., Artiﬁcial General
Intelligence, Cognitive Technologies (Springer, 2007).
[22] N. J. Nilsson, AI Magazine 26, 68 (2005).
[23] M. Minsky, P. Singh, and A. Sloman, AI Magazine 25,
113 (2004).
[24] M. Campbell, A. J. Hoane Jr., and F. Hsu, Artiﬁcial
Intelligence 134, 57 (2002).
[25] D.
Ferrucci,
E.
Brown,
J.
Chu-Carroll,
J.
Fan,
D. Gondek, A. A. Kalyanpur, A. Lally, J. W. Murdock,
E. Nyberg, J. Prager, et al., AI Magazine 31, 59 (2010).
[26] G. E. Hinton, S. Osindero, and Y. Teh, Neural Compu-
tation 18, 1527 (2006).
[27] L. Deng and D. Yu, Foundations and Trends in Signal
Processing 7, 197 (2013).
[28] Y. LeCun, Y. Bengio, and G. Hinton, Nature Review
521, 436 (2015).
[29] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Ve-
ness, M. G. Bellemare, A. Graves, M. Riedmiller, A. K.


## Page 16


16
Fidjeland, G. Ostrovski, et al., Nature 518, 529 (2015).
[30] D. Silver, A. Huang, C. J. Maddison, A. Guez, L. Sifre,
G. van den Driessche, J. Schrittwieser, I. Antonoglou,
V. Panneershelvam, S. D. Marc Lanctot, et al., Nature
529, 484 (2016).
[31] D. Silver, J. Schrittwieser, K. Simonyan, I. Antonoglou,
A. Huang, A. Guez, T. Hubert, L. Baker, M. Lai,
A. Bolton, et al., Nature 550, 354 (2017).
[32] D.
Silver,
T.
Hubert,
J.
Schrittwieser,
I.
Antonoglou,
M.
Lai,
A.
Guez,
M.
Lanc-
tot,
L.
Sifre,
D.
Kumaran,
T.
Graepel,
et
al.,
arXiv
preprint
p.
arXiv:1712.01815
(2017),
URL
https://arxiv.org/pdf/1712.01815.pdf.
[33] F. Crick, The Astonishing Hypothesis (Charles Scribn-
ers Sons, New York, 1994).
[34] C. Koch, The Quest for Consciousness: A Neurobiolog-
ical Approach (Roberts & Company, Englewood, CO,
2004).
[35] J. Hawkins and S. Blakeslee, On Intelligence:
How
a New Understanding of the Brain will Lead to the
Creation of Truly Intelligent Machines (Times Books,
2004).
[36] P. A. Merolla, J. V. Arthur, R. Alvarez-Icaza, A. S. Cas-
sidy, J. Sawada, F. Akopyan, B. L. Jackson, N. Imam,
C. Guo, Y. Nakamura, et al., Science 345, 668 (2014).
[37] E. K. Towlson, P. E. Vertes, S. E. Ahnert, W. R.
Schafer, and E. T. Bullmore, The Journal of Neuro-
science 33, 6380 (2013).
[38] L. E. Givon and A. A. Lazar, PLoS One 11, e0146581
(2016).
[39] S. W. Oh, J. A. Harris, L. Ng, B. Winslow, N. Cain,
S. Mihalas, Q. Wang, C. Lau, L. Kuan, A. M. Henry,
et al., Nature 508, 207 (2014).
[40] S. Nishimoto, A. T. Vu, T. Naselaris, Y. Benjamini,
B. Yu, and J. L. Gallant, Current Biology 21, 1641
(2011).
[41] M. K. Lindell, R. W. Perry, C. Prater, and W. C. Nichol-
son, Fundamentals of Emergency Management (Federal
Emergency Management Agency (FEMA), 2006).
[42] A. F. C. Wallace, Human Behavior in Extreme Situa-
tions: A Survey of the Literature and Suggestions for
further Research. Distaster Study Number 1., National
Research Council (U.S.) (Committee for Disaster Stud-
ies, National Academy of Sciences, National Research
Council, 1956).
[43] A. F. C. Wallace, Tornado in Worcester:
An Ex-
ploratory Study in Individual and Community Behavior
in an Extreme Situation. Distaster Study Number 3.,
National Research Council (U.S.) (Committee for Dis-
aster Studies, National Academy of Sciences, National
Research Council, 1956).
[44] A. F. C. Wallace and R. S. Grumet, Revitalizations and
Mazeways, Essays on culture change / Anthony F. C.
Wallace. Ed. by Robert S. Grumet (University of Ne-
braska Press, 2003).
[45] P. Valent, Encyclopedia of Stress (Elsevier Science,
2000), vol. 1 of Encyclopedia of Stress: A-D, chap. Dis-
aster Syndrome, pp. 706–708.
[46] A. Ripley, The Unthinkable: Who Survives When Dis-
aster Strikes - and Why (Random House, 2009).
[47] J. Leach, The Psychologist 24, 26 (2011).
[48] W. D. Cullen, The Public Inquiry into the Piper Alpha
Disaster, CM: 1310 (H.M.S.O., Department of Energy,
1990).
[49] J. D. Griﬃth and C. L. Hart, Perceptual and Motor
Skills 94, 1089 (2002).
[50] J. Leach, Aviation, Space, and Environmental Medicine
75, 539 (2004).
[51] J. Leach, Aviation, Space, and Environmental Medicine
83, 1152 (2012).
[52] D. H. Barlow, ed., Anxiety and its Disorders:
The
Nature and Treatment of Anxiety and Panic (Guilford
Press, New York, 2002).
[53] D. V. Baldwin, Neuroscience and Biobehavioral Re-
views 37, 1549 (2013).
[54] H. S. Bracha, CNS Spectrums 9, 679 (2004).
[55] M. Schauer and T. Elbert, Zeitschrift fur Psychologie /
Journal of Psychology 218, 109 (2010).
[56] J. M. Heidt, B. P. Marx, and J. P. Forsyth, Behavior
Research and Therapy 43, 1157 (2005).
[57] N. B. Schmidt, J. A. Richey, M. J. Zvolensky, and J. K.
Maner, Journal of Behavior Therapy and Experimental
Psychiatry 39, 292 (2008).
[58] E. Volchan, G. G. Souza, C. M. Franklin, C. E. Norte,
V. Rocha-Rego, J. M. Oliveira, I. A. David, M. V.
Mendlowicz, E. S. Coutinho, A. Fiszman, et al., Bio-
logical Psychology 88, 13 (2011).
[59] P. J. Clayton, Encyclopedia of Stress (Elsevier Science,
2000), vol. 1, chap. Bereavement, pp. 304–311.
[60] M. J. Horowitz, B. Siegel, A. Holen, G. A. Bonanno,
C. Milbrath, and C. H. Stinson, American Journal of
Psychiatry 154, 904 (1997).
[61] K. Shear and H. Shair, American Journal of Psychiatry
154, 253 (2005).
[62] D. C. Klein, Journal of Primary Prevention 12, 93
(1991).
[63] J. Rivera, A. B. Talone, C. T. Boesser, F. Jentsch,
and M. Yeh, in Proceedings of the Human Factors and
Ergonomics Society 58th Annual Meeting (2014), pp.
1047–1051.
[64] R. Reisenzein, S. Bordgen, T. Holtbernd, and D. Matz,
Journal of Personality and Social Psychology 91, 295
(2006).
[65] W. L. Martin, Ph.D. thesis, Griﬃth University, Qld.,
Australia (2014).
[66] G. Ritchie, in The Proceedings of the AISB Symposium
on Creative Language (Edinburgh, Scotland, 1999), pp.
78–85.
[67] T. R. Shultz, Journal of Experimental Child Psychology
13, 456 (1972).
[68] D. L. Alden, A. Mukherjee, and W. D. Hoyer, Journal
of Advertising 29, 1 (2000).
[69] B. Katz, Connection Science 5, 59 (1993).
[70] A. C. Samson, C. F. Hempelmann, O. Huber, and
S. Zysset, Neuropsychologia 47, 1023 (2009).
[71] J. Polimeni and J. P. Reiss, Evolutionary Psychology 4,
347 (2006).
[72] M. M. Hurley, D. C. Dennett, and R. B. Adams, In-
side Jokes: Using Humor to Reverse-Engineer the Mind
(MIT Press, 2011).
[73] J. H. Holland, Adaptation in Natural and Artiﬁcial Sys-
tems (MIT Press, Cambridge, MA., 1992).
[74] S.
A.
Kauﬀman,
The
Origins
of
Order:
Self-
Organization and Selection in Evolution (Oxford Uni-
versity Press, New York, 1993).
[75] D. C. Dennett, Darwin’s Dangerous Idea: Evolution and
the Meanings of Life (Simon & Schuster, 1995).
[76] D. Nguyen and B. Widrow, in Proc. SPIE 1293, Appli-
cations of Artiﬁcial Intelligence VIII (1990), pp. 596–
602.
[77] R. E. Jenkins and B. P. Yuhas, IEEE Transactions on
Neural Networks 4, 718 (1993).
[78] D. J. Chalmers, R. M. French, and D. R. Hofstadter,
Journal of Experimental and Theoretical Artiﬁcial In-
telligence 4, 185 (1992).
[79] P. L. Dordal,
An Introduction
to Computer Net-
works (Web Published, Open licence, 2016),
URL
http://intronetworks.cs.luc.edu/.
[80] J. D. Watson, T. A. Baker, S. P. Bell, A. Gann,
M. Levine, and R. Losick, Molecular Biology of the Gene


## Page 17


17
(Pearson, 2014).
[81] P. Schoﬁeld, Seals and their Context in the Middle Ages
(Oxbow Books, 2015).
[82] L. Hector, Palaeography and Forgery, no. 15 in Borth-
wick papers (St. Anthony’s Press, 1959).
[83] A. M. Balloon, Emory Law Journal 50, 905 (2001).
[84] J. Chang, Empress Dowager Cixi: The Concubine Who
Launched Modern China (Knopf, 2013).
[85] J. Searle, Minds, Brains and Science (Harvard Univer-
sity Press, Cambridge, Ma., 1984).
[86] T. Nagel, The Philosophical Review 83, 435 (1974).
[87] J. Levine, Paciﬁc Philosophical Quarterly 64, 354
(1983).
[88] D. C. Dennett, in Consciousness in Modern Science,
edited by A. Marcel and E. Bisiach (Oxford University
Press, 1988).
[89] R. Rojas, Neural Networks: A Systematic Introduction
(Springer, Berlin, 1996).
[90] S. Haykin, Neural Networks: A Comprehensive Foun-
dation (Pearson Prentice Hall, Singapore, 1999).
[91] M. T. Hagan, H. B. Demuth, M. H. Beale, and O. De
Jesus, Neural Network Design (ebook) (M. T. Hagan,
2017), URL hagan.okstate.edu/nnd.html.
[92] M.
A.
Nielsen,
Neural
Networks
and
Deep
Learning
(Determination
Press,
2015),
URL
http://neuralnetworksanddeeplearning.com.
[93] I.
Goodfellow,
Y.
Bengio,
and
A.
Courville,
Deep
Learning
(MIT
Press,
2016),
URL
http://www.deeplearningbook.org.
[94] D. J. Graham and D. N. Rockmore, Journal of Cognitive
Neuroscience 23, 267 (2011).
[95] D. J. Graham, Frontiers in Computational Neuroscience
8, 44:1 (2014).
[96] J. Wiles and A. Bloesch, in Advances in Neural Informa-
tion Processing Systems 4, edited by S. J. Hanson and
R. P. Lippman (Morgan Kaufmann, San Mateo, CA.,
1992), pp. 325–332.
[97] J. S. Mattick and M. J. Gagen, Science 307, 856 (2005).
[98] J. S. Mattick and M. J. Gagen, Molecular Biology and
Evolution 18, 1611 (2001).
[99] J. A. Sharp, Data Flow Computing: Theory and Prac-
tice (Intellect Books, 1992).
[100] K. Hwang and N. Jotwani, Advanced Computer Archi-
tecture: Parallelism, Scalability, Programmability (Tata
McGraw-Hill Education, 2010).
[101] J. Silc, B. Robic, and T. Ungerer, Processor Archi-
tecture:
From data ﬂow to Superscalar and Beyond
(Springer Science and Business Media, 2012).
[102] R. Giorgi, R. M. Badia, F. Bodin, A. Cohen, P. Evripi-
dou, P. Faraboschi, B. Fechner, G. R. Gao, A. Garbade,
R. Gayatri, et al., Microprocessors and Microsystems:
Embedded Hardware Design 38, 976 (2014).
[103] N. Trifunovic, V. Milutinovic, J. Salom, and A. Kos,
Journal of Big Data 2 (2015).
[104] R. Caruana, Machine Learning 28, 41 (1997).
[105] L. Kaiser, A. N. Gomez, N. Shazeer, A. Vaswani,
N. Parmar, L. Jones, and J. Uszkoreit, arXiv:1706.05137
[cs.LG] (2017).
[106] S. Ruder, arXiv:1706.05098 [cs.LG] (2017).
[107] J. Mestre, ed., Transfer of Learning from a Modern Mul-
tidisciplinary Perspective, Current Perspectives on Cog-
nition, Learning and Instruction (Information Age Pub-
lishing, Incorporated, 2005).
[108] A. McKeough, J. Lupart, and A. Marini, eds., Teach-
ing for Transfer: Fostering Generalization in Learning
(Routledge, 2013).
[109] C. Ward, S. Bochner, and A. Furnham, The Psychology
of Culture Shock (Routledge, 2005).
[110] A. Toﬄer, Future Shock (Bantam Books, 1971).
[111] H. E. Fisher, Human Nature 9, 23 (1998).
[112] J. Bowlby, Attachment and Loss, Vol. 1: Attachment
(Basic Books, 1969).
[113] J. Bowlby, Attachment and Loss, Vol. 2: Separation
(Basic Books, 1973).
[114] J. Bowlby, Attachment and Loss, Vol. 3: Loss, Sadness
and Depression (Basic Books, 1980).
[115] I. Bretherton,
Developmental Psychology
28,
759
(1992).
[116] C. M. Parkes and H. G. Prigerson, Bereavement: Stud-
ies of Grief in Adult Life (Routledge, 2013).
[117] C. Hall, Bereavement Care 33, 7 (2014).
[118] S. D. Suarez and G. G. Gallup Jr., Journal of Human
Evolution 10, 175 (1981).
[119] D. Reiss and L. Marino, PNAS 98, 5937 (2001).
[120] L. Chang, Q. Fang, S. Zhang, M.-M. Poo, and N. Gong,
Current Biology 25, 212 (2015).
[121] C.
Krupenye,
F. Kano,
S. Hirata,
J.
Call,
and
M. Tomasello, Science 354, 110 (2016).
[122] E. J. C. van Leeuwen, I. C. Mulenga, M. D. Bodamer,
and K. A. Cronin, American Journal of Primatology 78,
914 (2016).
[123] E. J. C. van Leeuwen, K. A. Cronin, and D. B. M. Haun,
Scientiﬁc Reports 13, 44091 (2017).
[124] H. S. Kuhl, A. K. Kalan, M. Arandjelovic, F. Aubert,
L. DAuvergne, A. Goedmakers, S. Jones, L. Kehoe,
S. Regnaut, A. Tickle, et al., Scientiﬁc Reports 6, 22219
(2016).
[125] L. R. Berger, J. Hawks, D. J. de Ruiter, S. E. Churchill,
P. Schmid, L. K. Delezene, T. L. Kivell, H. M. Garvin,
S. A. Williams, J. M. DeSilva, et al., eLife 4, e09560
(2015).
[126] P. H. Dirks, L. R. Berger, E. M. Roberts, J. D. Kramers,
J. Hawks, P. S. Randolph-Quinney, M. Elliott, C. M.
Musiba, S. E. Churchill, D. J. de Ruiter, et al., eLife 4,
e09561 (2015).
[127] L. R. Berger, J. Hawks, P. H. Dirks, M. Elliott, and
E. M. Roberts, eLife 6, e24234 (2017).
[128] P. H. Dirks, E. M. Roberts, H. Hilbert-Wolf, J. D.
Kramers, J. Hawks, A. Dosseto, M. Duval, M. Elliott,
M. Evans, R. Grn, et al., eLife 6, e24231 (2017).
[129] J. Diamond, Guns, Germs, and Steel: The Fates of Hu-
man Societies (Norton, New York, 1997).
[130] Y. N. Harari, Sapiens: A Brief History of Humankind
(Vintage, 2014).
[131] R. Caspari and M. H. Wolpoﬀ, in The Origins of Modern
Humans: Biology Reconsidered, edited by F. H. Smith
and J. C. M. Ahern (John Wiley & Sons, 2013), pp.
355–391.
[132] K. Sterelny and P. Hiscock, Biological Theory 9, 1
(2014).
[133] R.
Yampolskiy,
arXiv
preprint
p.
arXiv:1712.04020
(2017),
URL
https://arxiv.org/pdf/1712.04020.pdf.
[134] S. Mithen, The Prehistory of the Mind: A Search for
the Origins of Art, Religion and Science (Thames and
Hudson, London, 1996).
[135] S. Pinker, How the Mind Works (Norton, 1997).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1712_09014v1_null_dynamical_state_models_of_human_cognitive_dysfunction
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1712_09014V1_NULL_DYNAMICAL_STATE_MODELS_OF_HUMAN_COGNITIVE_DYSFUNCTION.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

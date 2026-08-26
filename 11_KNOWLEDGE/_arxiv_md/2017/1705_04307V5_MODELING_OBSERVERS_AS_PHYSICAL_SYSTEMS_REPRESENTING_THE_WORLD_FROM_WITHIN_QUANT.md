---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1705.04307v5
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1705.04307v5_Modeling_observers_as_physical_systems_representing_the_world_from_within__Quant

> Source: 1705.04307v5_Modeling_observers_as_physical_systems_representing_the_world_from_within__Quant.pdf

> Pages: 84

---


## Page 1


Modeling observers as physical systems representing the world from within:
Quantum theory as a physical and self-referential theory of inference
John Realpe-G´omez1∗
Theoretical Physics Group, School of Physics and Astronomy,
The University of Manchester†, Manchester M13 9PL, United Kingdom and
Instituto de Matem´aticas Aplicadas, Universidad de Cartagena, Bol´ıvar 130001, Colombia
(Dated: June 13, 2019)
In 1929 Szilard pointed out that the physics of the observer may play a role in the analysis of
experiments. The same year, Bohr pointed out that complementarity appears to arise naturally in
psychology where both the objects of perception and the perceiving subject belong to ‘our mental
content’. Here we argue that the formalism of quantum theory can be derived from two related intu-
itive principles: (i) inference is a classical physical process performed by classical physical systems,
observers, which are part of the experimental setup—this implies non-commutativity and imaginary-
time quantum mechanics; (ii) experiments must be described from a ﬁrst-person perspective—this
leads to self-reference, complementarity, and a quantum dynamics that is the iterative construction
of the observer’s subjective state. This approach suggests a natural explanation for the origin of
Planck’s constant as due to the physical interactions supporting the observer’s information process-
ing, and sheds new light on some conceptual issues associated to the foundations of quantum theory.
It also suggests that fundamental equations in physics are typically of second order, instead of the
more parsimonious ﬁrst-order equations, due to the physical nature of the observer. It furthermore
suggests some experimental conjectures: (i) the quantum of action could be understood as the re-
sult of the additional energy required to transition from unconscious to conscious perception—this
is consistent with available experimental data; (ii) humans can observe a single photon of visible
light—this is related to (i) and is consistent with existing psychophysics experiments; (iii) the neural
correlates of the self are composed of two complementary sub-processes that essentially model each
other, much like the DNA molecule is composed of two strands that essentially produce a copy of
each other—this may help explain why the brain is divided into hemispheres and suggests self-aware
systems should have a similar architecture. Moreover, by explicitly and consistently incorporating
us observers and our everyday ﬁrst-person perspective into the foundations of physics, this approach
may help bridge the gap between science and human experience. We discuss the potential implica-
tions of these ideas for the modern research program on consciousness championed by Nobel laureate
Francis Crick and the emerging ﬁeld of contemplative science. As side results: (i) we show that
message-passing algorithms and stochastic processes can be written in a quantum-like manner—
this may suggest novel ways to simulate quantum systems with message-passing algorithms or to
naturally implement these powerful distributed algorithms on quantum computers; (ii) we provide
evidence that non-stoquasticity, a quantum computational resource, in some cases may be related
to non-equilibrium phenomena—this suggests that some of the potential advantage of quantum
computers associated to non-stoquasticity may be related to the type of computational advantages
recently observed in non-equilibrium Monte Carlo methods where detailed balance is broken; (iii)
we provide a diﬀerent Hamiltonian function for a quantum particle in a classical electromagnetic
ﬁeld—this may suggest a probabilistic interpretation of electromagnetic phenomena.
“Describe the real factual situation.”
Albert Einstein
Contents
I. Introduction
2
II. Overview and related work
6
III. The big picture
7
†A substantial part of this work was developed while being
Research Associate at The University of Manchester.
∗Electronic address: john.realpe@gmail.com
A. Inference as a physical process
7
B. First-person perspective and
self-reference
9
IV. Quantum mechanics recasted
9
A. Von Neumann equation as a pair of real
matrix equations
9
B. Some examples of quantum dynamics in
terms of non-negative real kernels
11
1. Non-relativistic Schr¨odinger equation 11
2. From non-relativistic path integrals to
real convolutions
11
3. Particle in an electromagnetic ﬁeld
via asymmetric real kernels
12
V. Markov processes recasted
13
A. Principle of maximum caliber and factor
graphs
13
arXiv:1705.04307v5  [quant-ph]  12 Jun 2019


## Page 2


2
B. Quantum-like formulation of stochastic
processes via the cavity method
14
1. Cavity messages as imaginary-time
wave functions
14
2. Belief propagation as imaginary-time
quantum dynamics
15
C. Euclidean quantum mechanics: From
linear chains to cycles
16
VI. Third-person perspective
17
A. Observations as internal representations 17
B. Experiments as circular interactions
18
1. Simulation interpretation
18
2. Ideomotor interpretation
18
C. Imaginary-time von Neumann equation 20
1. Circularity entails
non-commutativity
20
2. Pure states and causality
21
VII. First-person perspective
22
A. Self-reference and complementarity
22
B. First-person observers and quantum
dynamics
23
1. General considerations
23
2. Equilibrium environment and
symmetric kernels
25
3. Nonequilibrium environment and
asymmetric kernels
25
VIII. Occam’s razor favors the reverse
paradigm
26
A. Some relevant assumptions in the
mainstream paradigm
26
B. Corresponding interpretation in the
reverse paradigm
27
C. Quantum foundations in reverse mode
27
IX. Quantumness and consciousness
29
A. Consciousness as a rigorous scientiﬁc
subject
29
B. The message of the quantum: observers
are physical
29
C. Planck constant from psychophysics
experiments
30
1. General considerations
30
2. ‘Classical’ pshycophysics experiments 31
3. ‘Quantum’ psychophysics
experiments
32
D. Self-reference and the global architecture
of self-aware systems and the self
33
X. Discusion
35
A. Summary of main points
35
B. Quantum computing, artiﬁcial general
intelligence, and quantum cognition
36
C. On science, our worldview, and how we
live
36
1. Enlarging our toolbox with
ﬁrst-person methods
37
2. Can the scientiﬁc and contemplative
worldviews converge?
39
3. Not just bare rationality: A call for
action
41
Acknowledgments
43
A. We as physical systems
43
B. The modern and well-respected
approach to consciousness
45
1. Third-person perspective and the ‘easy’
problem of consciousness
45
2. First-person perspective and the ‘hard’
problem of consciousness
46
C. Self-reference and the recursion
theorem
47
D. Derivation of real kernel
representaions in Sec. IV B
48
1. Non-relativistic Schr¨odinger equation
48
2. From non-relativistic path integrals to
real convolutions
49
3. Particle in an electromagnetic ﬁeld via
asymmetric real kernels
51
a. Prelude: Hermitian kernels via
complex Hamiltonian functions
51
b. Postlude: real asymmetric kernels via
real Hamiltonian functions
54
E. Eﬀective kernels with negative entries 55
F. Phase-less quantum-like formulation
of Markov processes
56
1. Time-symmetric evolution equations
56
2. Time-symmetric kernels are not
normalized
57
3. Future-past symmetry and quantum-like
Markov processes
57
References
59
I.
INTRODUCTION
Perhaps some of the most diﬃcult transitions in the
evolution of our understanding of the universe have
been those that removed our special status in some
way—like the resistance against the concept that our
planet is not the center of the universe, attributed to
Copernicus, or against the concept that we are not
as diﬀerent as we thought from other animals, at-
tributed to Darwin. Yet history has taught us again
and again that once we surrender and accept the
new status a previously hidden simplicity suddenly
emerges.
In part because our subjective biases are often mis-
leading, we have usually made an eﬀort to keep the


## Page 3


3
subjective, ourselves, out of our picture of the uni-
verse in search of an objective reality. Even studies
of the human brain have mostly focused on a third-
person perspective (see Fig. 2a), i.e. scientist usually
study others’ brains, not their own. This has granted
us the special status of being able to understand the
world as if we were not part of it, independently of our
everyday human experience. However, at the same
time that we gained the special status of doing sci-
ence without the scientist, we also created a deep
tension between science and human experience (see
below).
This work is a kind invitation to reconsider the re-
sistance that mainstream physics has understandably
developped against the role that human experience
might play on the foundations of science. Such type
of invitation is not new, of course. Indeed, a simi-
lar invitation made twenty ﬁve years ago by Varela,
Thompson, and Rosch [1] have proved very fruitful for
cognitive science. Let Varela, Thompson, and Rosch
clearly express the tension between science and hu-
man experience mentioned above (see Fig. 1):
“In our present world science is so dominant that we
give it the authority to explain even when it denies what
is most immediate and direct—our everyday, immediate
experience. Thus most people would hold as a fundamen-
tal truth the scientiﬁc account of matter/space as collec-
tions of atomic particles, while treating what is given in
their immediate experience, with all of its richness, as
less profound and ture. Yet when we relax into the im-
mediate bodily well-being of a sunny day or of the bodily
tension of anxiously running to catch a bus, such accounts
of space/matter fade into the background as abstract and
secondary. [...]
“To deny the truth of our own experience in the scien-
tiﬁc study of ourselves is not only unsatisfactory; it is to
render the scientiﬁc study of ourselves without a subject
matter. But to suppose that science cannot contribute to
an understanding of our experience may be to abandon,
within the modern context, the task of self-understanding.
Experience and scientiﬁc understanding are like two legs
without which we cannot walk.”
F. Varela, E. Thompson, E. Rosch, Ref. [1] (pag. 12-13)
Such type of invitation is not new in physics either:
the role of the observer in physics, for instance, has
been explored at least since Maxwell by many scien-
tist working in subjects such us the physics of infor-
mation and the foundations of quantum theory (see
Sec. II). There have also been several discussion about
the relationship that some peculiar aspects of quan-
tum theory might have with the admittedly fuzzy
concept of ‘consciousness’ (see Sec. II). Such explo-
rations, however, have not yet become mainstream
nor, in our opinion, gone far enough.
We hope to
make a case here for why we consider the time is ripe
and the stakes are high to bring this debate to the
forefront.
For more than a century, much has been debated
about what is the actual content of quantum theory.
Although substantial progress has been done (see e.g.
Refs. [2–10] and Sec. II), no general consensus has
been reached [11, 12]. This elusive character of quan-
tum theory contrasts with its outstanding success.
Here we argue that the resistance we have developed
against human experience as a key aspect for the sci-
entiﬁc understanding of nature has prevented us from
better grasping the essential message of quantum the-
ory [8, 13]. Indeed, there has usually been an under-
standable skepticism of any suggestion that observers
or consciousness might play a special role in quantum
theory. However, we are witnessing today a radical
shift in our understanding and control of aspects that
we previously thought were intrinsically human, per-
haps even unreachable to the powerful methods of
science (see Appendix A).
It is already common to read in the news that arti-
ﬁcial intelligence has outperformed humans in yet an-
other task we had deemed intractable before [14, 15].
Brain research scientists have now managed to read
and control thoughts, sensations and other aspects of
human experience, making the idea of living in a vir-
tual world, as depicted in the movie The Matrix, ap-
parently just a matter of technological maturity [16–
19] (see Fig. 3). Recent theoretical and experimental
developments, as well as a new respect for the sub-
jective (see Fig. 3 and Appendix B 1), have brought
the fuzzy concept of consciousness into the lab and
allowed scientists to start cracking some aspects of it
in ways that were unthinkable before [20, 21]. To-
day it is not strange to ﬁnd collaborations between
world-class research institutions and monks of diﬀer-
ent spiritual traditions. Such collaborations have led,
for instance, to ﬁnd evidence that some practices pre-
viously labelled ‘spiritual’, such as mindfulness med-
itation, can radically transform our brain and signiﬁ-
cantly improve the quality of our lives [22, 23]—these
studies are mostly concerned with the so-called neu-
ral correlates of consciousness [20, 21, 24], they are
studies from a third-person perspective (see Fig. 2a).
There have also been important developments
on the understanding of our subjective experience,
our ﬁrst-person perspective (see Fig. 2b and Ap-
pendix B 2). An interesting experiment in this regard
is the so-called rubber-hand illusion [25, 26] which
shows that we can experience a fake hand, discon-
nected from us, as if it were part of our own body.
This simple experiment, which can be carried out at
home, requires that we focus our attention on a rub-
ber hand while our real hand is concealed. Both the
artiﬁcial hand and the invisible real hand are stroked
repeatedly and synchronously with a probe. About
one or two minutes later the experience that the rub-
ber hand is our own emerges. We keep feeling strokes
which are given only to the rubber hand as if they
were actually given to our real hand. Furthermore, we
feel as if there were a connection between our shoul-
der and the artiﬁcial hand. Other experiments have


## Page 4


4
extended the illusion to the full body [27–29].
Metzinger [30, 31] argues that these experiments
are consistent with the idea that our experience of re-
ality is actually a mental simulation of the world tak-
ing place in our brains and that our phenomenal self,
i.e. what we call ‘I’, is a representational structure in
our brains, a self-model (see chapter 9 of Ref. [32] for
a review; for a short introduction to the most central
ideas see Metzinger’s talk ‘The transparent avatar in
your brain’ at TEDxBarcelona). To avoid the inﬁnite
regress of trying to represent a system that represents
a system that represents a system, and so on ad in-
ﬁnitum, the model of the world, which includes the
self-model, is taken to be the ultimate reality. Met-
zinger refers to this feature as ‘transparency’ (see also
Refs. [30, 32]):
“Transparency simply means that we are unaware of the
medium through which information reaches us. We do
not see the window but only the bird ﬂying by. We do
not see neurons ﬁring away in our brain but only what
they represent for us.
A conscious world-model active
in the brain is transparent if the brain has no chance of
discovering that it is a model—we look right through it,
directly onto the world, as it were.
The central claim
of [...] the self-model theory of subjectivity [...] is that
the conscious experience of being a self emerges because
a large part of the [phenomenological self-model] in your
brain is transparent.”
T. Metzinger, Ref. [31] (page 7)
Metzinger also argues that the self-model imple-
mented in our brain gives rise to the ﬁrst-person per-
spective (see Fig. 2b; see also Refs. [30, 32]):
“By placing the self-model within the world-model, a cen-
ter is created. That center is what we experience as our-
selves [...] It is the origin of what philosophers often call
the ﬁrst-person perspective. We are not in direct contact
with outside reality or with ourselves, but we do have an
inner perspective. We can use the word ‘I.”’
T. Metzinger, Ref. [31] (page 7)
These
scientiﬁc
advances
are
often
implicitly
grounded on the scientiﬁc worldview prevalent today,
i.e. on the idea that there is an objective mechani-
cal world and that we have the special status of un-
derstanding such a world as if we were an abstract
entity independent of it (see Fig. 4). Today it is al-
most taken for granted that physics, and in particular
quantum physics, provides the objective laws that lie
at the very foundation of the skyscraper of science.
The remaining scientiﬁc disciplines therefore emerge
from it (see Fig. 1).
For instance, chemistry is often considered as an
application of physics describing the eﬀective laws
that emerge at the molecular scale. In turn, biology
is often considered as an application of chemistry de-
scribing the eﬀective laws that emerge at the cellular
scale. And so on. At the end of such a hierarchy, ac-
cording to the mainstream paradigm, we ﬁnd human
experience as an illusion generated by the incessant
activity of billions of neurons distributed throughout
our brain and body. This worldview is nicely sum-
marized in Crick’s ‘Astonishing Hypothesis’:
“The Astonishing Hypothesis is that You, your joys and
your sorrows, your memories and your ambitions, your
sense of personal identity and free will, are in fact no
more than the behavior of a vast assembly of nerve cells
and their associated molecules.”
F. Crick, Ref. [33] (page 3)
Yet, similar in spirit to the so-called ‘science of sci-
ence’ [34], which uses the tools of science to study
the mechanisms underlying the doing of science, we
can ask what these recent advances on the under-
standing of our human nature have to say about the
scientists doing the science. If we take the view that
the doing of science relies in part on the physical pro-
cesses running on our brains, a natural question arises
(cf.
[1], page 10): shouldn’t our scientiﬁc descrip-
tion of the universe be inﬂuenced by the structure
of our own cognitive system? We are convinced that
in the current state of aﬀairs there is an opportunity
to more rigorously investigate the role that concepts
that have been largely considered taboos in physics
to date might play on the foundations of science.
In 1929 Szilard [35] already pointed out that the
physics of the observer may play a role in the analy-
sis of experiments. The same year, Bohr [36] pointed
out that complementarity appears to arise naturally
in psychology where both the objects of perception
and the perceiving subject belong to ‘our mental con-
tent’. About a year ago [37] we argued that quantum
theory could be understood from two related prin-
ciples. While in the mainstream scientiﬁc paradigm
we expect the observer to induce decoherence and
so destroy any potential quantum phenomena, here
we work in the reverse paradigm, where the world is
thought of as fundamentally classical and quantum
phenomena arises as a consequence of the physicality
of the observer, considered as another classical sys-
tem (see Fig. 4). Here we provide a more detailed,
hopefully clearer exposition of these ideas, as well as
a more thorough discussion of their potential impli-
cations (see Ref. [38] for a more compact and formal
discussion).
In particular, we discuss why we con-
sider these ideas hold the potential to bring physics
and human experience closer together.
Quantum dynamics can be described by the von
Neumann equation [39]
iℏ∂ρ
∂t = [H, ρ],
(1)
where ρ, H, ℏ, and i are the density matrix, Hamilto-
nian operator, Planck constant, and imaginary unit,


## Page 5


5
respectively; furthermore [H, ρ] = Hρ −ρH. Addi-
tionally, the diagonal elements of ρ encode the proba-
bility of observing the corresponding outcomes in an
experiment. More generally, if the Hermitian opera-
tor O represents the physical observable of interest,
its expected value ⟨O⟩, when the system is in state ρ,
is given by the Born rule
⟨O⟩= Tr [ρO] .
(2)
Key questions to understand quantum theory are:
Why is ρ a matrix? Why is ρ complex? Why does ρ
satisﬁes Eq. (1)? Why expected values are given by
Eq. (2)?
Let us now introduce the two principles put for-
ward in Ref. [37], and discuss more precisely what we
actually mean:
Principle I: Inference is a classical physical pro-
cess performed by classical physical systems,
observers, which are part of the experimental
setup.
Principle II: Experiments must be described from
a ﬁrst-person perspective.
First of all, by ‘physical’ here we only refer to the
textbook notion that there are certain events that
can be described by certain mathematical variables.
We do not attempt to make any claims beyond this
strictly operational notion.
Indeed, we will argue
elsewhere, where we will compare our approach to the
more common information-theoretical approach to
quantum foundations, that we could also use the la-
bel ‘information’ instead of the label ‘physical’. What
really matters for our approach is that we treat na-
ture as a whole in a consistent manner, i.e. either
everything is information or everything is physical.
The keyword in these expressions, that we shall ar-
gue elsewhere are equivalent, is neither the label ‘in-
formation’ nor the label ‘physical’, but rather the
term ‘everything’, which implies universality and self-
reference.
The term ‘observer’ here stands for a physical sys-
tem, e.g. a robot, that can carry out experiments in
a lab. While everything discussed in this manuscript
can be considered as referring only to artiﬁcial ob-
servers, i.e. robots, we will often refer to human ob-
servers too. Although using terms like ‘humans’, ‘we’,
‘ourselves’, etc, instead of terms like ‘robots’ through-
out our analysis might give the impression to some
that we are doing philosophy rather than physics, we
emphasize that both artiﬁcial and human observers
are considered here exclusively as physical systems
and nothing more—studying humans as physical sys-
tems is routinely done in neuroscience, for instance.
There are two main reasons why we insist in refer-
ring to humans in our analysis. On the one hand,
we think that the best place to ﬁnd intuition about
the ﬁrst-person perspective (see Fig. 2) mentioned in
Principle II is our own subjective experience. On
the other hand, we consider that the main implica-
tions of our work are related to us.
Principle I and Principle II can be considered
as two more assumptions added to our current phys-
ical description of the world. This manuscript can
be read in its entirety as an analysis of the impli-
cations of such ‘additional’ assumptions.
However,
we would like to argue that these two principles are
better thought of as two assumptions less.
Indeed, overwhelming experimental evidence sug-
gests that any observation requires an underlying
physical process. For instance, the electromagnetic
radiation reﬂected from this page interact with the
electric charges in our eyes and launch a highly com-
plex physical process in our brains that essentially
constitute the neural correlates of our experience of
reading these words (see Figs. 2a, 3 and 6).
Nev-
ertheless, our physical description of experiments has
largely neglected the physical processes related to the
observer.
Even in experiments that explicitly deal
with the phyics of the observer, such as those re-
lated to Maxwell’s demon, the physics of the scien-
tists performing the experiment is neglected (see e.g.
Refs. [40, 41]). There are good reasons for this, of
course. An accurate physical description of humans
seems to be overwhelmingly complicated, and scien-
tists have managed to do amazing progress anyways.
In this respect, Principle I asks us to drop the
assumption that we can neglect the physics of the
scientists doing the experiments. For the purposes of
this work, we can account for the observer as part
of the experimental setup by only adding an eﬀective
interaction that essentially turns the linear chain of
cause-eﬀect relationships into a circle. From this per-
spective, the interactions associated to the observer
could be considered colloquially as a missing link to
quantum theory.
The discussion above analyses the observer from
a third-person perspective, i.e. from the perspective
of an external observer that is not included in the
analysis (see Figs. 2 and 7).
However, overwhelming experimental evidence sug-
gests that we can only do science from a subjective
or ﬁrst-person perspective. At the risk of stating the
obvious we mention here a few examples. Indeed, to
the best of our knowledge, Galileo, Newton, Einstein,
Bohr, and all scientists we are aware of carried out
their analysis and wrote their scientiﬁc reports from
their own subjective perspective. When we read their
works and try to reproduce their results, we do it from
our own subjective perspective. Automated experi-
ments carried out by robots (see e.g. Ref. [42]) can
actually be considered as larger experiments where
the robots are part of the experimental setup. Such
larger experiments are carried out by scientists from
their own subjective perspective. If scientists launch
such automated experiments and never collect the re-


## Page 6


6
sults, whatever they claim that happened or did not
happen would be just an assumption made from their
own subjective perspective. When scientists perform
experiments where they study other humans observ-
ing a physical system [43], they do it from their own
subjective perspective. Even the feeling experienced
by some people [44] of being out of their own bod-
ies, which may appear as the phenomenon more con-
sistent with the assumption that we can observe the
world from the outside, is experienced from their own
subjective perspective (see Fig. 3).
As a by-product of the understandable and highly
successful assumption of neglecting the observer, a
further assumption has usually been made in physics:
that we can somehow describe the world from an ob-
jective or third-person perspective, as if we were not
part of it, even though every second of our lives, from
birth to death, we can only experience it from a ﬁrst-
person perspective. In this respect, Principle II asks
us to drop such an assumption and be consistent with
what we observe in our everyday lives until there is
experimental evidence that suggests otherwise. From
this perspective, the question would rather be how
the perception of objectivity emerges out of the in-
tersection of our subjectivities, i.e. out of the set of
perceptions that are common to all of us. On this
matter, all research done on the so-called quantum-
to-classical transition may have much to say.
In this sense we might consider that Principle I
and Principle II are in line with Einstein’s sugges-
tion that we should describe the ‘real factual situa-
tion’ [45] (page 85; see also Ref. [12]), a motto we
would call model what is, i.e. what we actually expe-
rience, not what we assume it is (see Fig. 9 and Ap-
pendix A). Interestingly, this motto is consistent with
the perspective from some contemplative traditions
which suggests that reality is like the blue sky, which
is obscured by the clouds of the vast amount of con-
ceptual constructs we have acquired during the course
of our lives. From this perspective, such clouds or
‘conceptual baggage’ makes diﬃcult for us to see the
‘real factual situation’. In this view, a scientiﬁc the-
ory should therefore be about how we do inferences
and build abstract concepts out of our direct hu-
man experience that allow us to reach inter-subjective
agreements with our peers about our shared human
experience.
A related question we ﬁnd of interest is why the
mathematical structure of fundamental physics equa-
tions are typically second-order diﬀerential equations
and not the most parsimonious ﬁrst-order diﬀerential
equations? We will argue that the observer has much
to do with it.
II.
OVERVIEW AND RELATED WORK
This work is organized as follows. In Secs.III-V we
set the framework and introduce the main conceptual
tools. In Sec. III we present a general discussion of the
ideas involved and why we consider they make sense;
in particular, we thoroughly discuss how we interpret
Principle I and Principle II—in Appendices B and
C we summarize, respectively, some relevant scientiﬁc
insights obtained via the modern approach to con-
sciousness and the formal analysis of self-reference
via the recursion theorem, for the reader who is not
familiar with these. In particular, we emphasize that
the main conceptual tool in the recursion theorem is
a pair of complementary Turing machines that essen-
tially print each other. In Sec. IV we rewrite Eq. (1)
as a pair of complementary matrix equations, which
are those that will be derived in Sec. VII from Prin-
ciple I an Principle II; furthermore, we provide a
couple of examples to illustrate that the kernels in-
volved hold potential to be interpreted in probabilis-
tic terms, as we will discuss in Secs. V, VI, and VII—
Appendix D provides some relevant technical details.
In Sec. V we show how stochastic process can be re-
casted in an Euclidean quantum-like manner; in par-
ticular, we show how message-passing algorithms can
be interpreted as an instance of imaginary-time quan-
tum mechanics. More precisely, if properly normal-
ized, the so-called cavity messages can be considered
as imaginary-time wave functions evolving forward
and backward in time, and the corresponding belief
propagation equations as an instance of imaginary-
time Schr¨odinger equation and its adjoint.
Yet, in
this case the phase is just an optional artiﬁcial con-
struct which can be taken equal to zero, as discussed
in Appendix F; moreover, the initial and ﬁnal condi-
tions are completely speciﬁed by the interactions in
the chain. We argue this is not true anymore once
we have stochastic process on a cycle rather than a
chain, where the na¨ıve belief propagation algorithm
is not exact anymore.
In Sec. VI we discuss the implementation of Prin-
ciple I; in particular, we show that considering the
observer as a physical system turns the traditional
chain of cause-eﬀect relationships into a loop. Fur-
thermore, we show that the class of stochastic pro-
cesses on a cycle relevant for this work, derived via
the so-called principle of maximum caliber, can be
described via the imaginary-time version of the von
Neuman equation. In Sec. VII we show that shifting
from the third-person perspective assumed in Sec. VI
to a ﬁrst-person perspective leads to the pair of ma-
trix equations derived in Sec. IV. So, the shift from
the third- to the ﬁrst-person perspective eﬀectively
implements a Wick rotation, turning the imaginary-
time von Neuman equation into Eq. (1). Although
our discussion is based on transition kernels with
non-negative entries, in Appendix E we discuss this


## Page 7


7
is not a restriction in our approach.
In Sec. VIII
we compare the mainstream paradigm to the reverse
paradigm assumed here.
Based on the results ob-
tained before, we argue that Occam’s razor favors
the reverse paradigm over the mainstream paradigm.
In Sec. IX we discuss some third-person perspective
psychophysics experiments and argue that we can
estimate Planck constant from them. Furthermore,
comparing to results from the ﬁrst-person perspec-
tive brieﬂy described in Appendix B, we suggest that
the neural architecture of self-aware systems and the
self should be composed of two complementary neu-
ral sub-systems that essentially model each other,
similar to the double-stranded structure of the DNA
molecule [46]; we conjecture this principle may un-
derly the division of our brains into hemispheres, i.e.
for the brain to be able to implement a self-model
and refer to itself. Finally, in Sec. X we discuss some
of the potential implications of this work.
The ideas presented here have been explored by
many authors even before the inception of quantum
theory. An exhaustive discussion is out of the capa-
bilities of the author. We here mention some authors
we are aware of.
The idea that the observer can play a role in physics
have been explored by Maxwell, Szilard, Landauer,
among many others (see e.g. Ref. [47] and references
therein). The question on whether the observer and
consciousness can play any role on quantum theory
have been discussed since the discovery of the theory
by Wigner [48], von Neumann [49], Bohm [50], Pen-
rose [51, 52], Hameroﬀ[53] among many others. Ex-
plorations on the mechanics of the observer have been
done by Bennett, Hoﬀman, and Prakkash [54], as well
as Fields [55–57] and Mueller [58]; these authors also
pointed out that modeling the observer leads to some
quantum-like phenomena.
The idea that quantum
theory could be related to seeing the world from the
inside has been explored by R¨ossler [59]. The idea
that a combination of forward and backward stochas-
tic processes could be described via quantum-like
equations has been explored by McKeon and Ord [60].
The idea of deriving aspects of quantum theory via
the principle of maximum caliber has been explored
by Caticha [61, 62]. The idea that non-equlibrium
phenomea could play a role on the derivation of quan-
tum theory has been explored by Gr¨ossing [63]. The
idea that quantum theory can be derived from pairs
of complementary variables has been explored by
Goyal [64], Kunth, and Skilling [9]. Explorations on
the potential relationships between quantum theory
and self-reference has been done by Kauﬀman [65],
who has also explored the idea that self-reference may
underly the fundamental equations of physics. More
indirect explorations of this relationship through the
G¨odel theorem and incompleteness have been done
by Dalla Chiara [66], Penrose [51, 52] Brukner [67],
Breuer [68], Calude [69]. The idea that quantum the-
ory and cognitive science may be related have been
explored by Bohr [36], Aerts [70], Khrennikov [71],
Bruza, Wang, and Bussemeyer [72]. The idea that
the self is composed of complementary systems has
been explored by Maturana and Varela [73] through
the concept of autopoiesis and more recently by Dea-
con [74]; Hofstadter [75, 76] has also explored the re-
lationship between the concept of self and the mathe-
matical formalism of self-reference via the G¨odel the-
orem. The idea that taking into account the observer
can help resolve some conceptual diﬃculties of quan-
tum theory has been explord by Fuchs, Schack [77],
and Mermin [13].
The idea that the subject may
play a fundamental role in our description of reality
have been explored by many, among which we have
Siddharta Gautama, best known a Buddha, about
twenty six centuries ago, by Varela, Thompson, and
Rosch [1] about twenty ﬁve years ago, by Fuchs and
Schack [8] as well as Rovelli [78] a few years ago, by
Mueller [58], Brukner [79], and Chiribella [80] a few
months ago.
III.
THE BIG PICTURE
A.
Inference as a physical process
In this section we discuss how we interpret Princi-
ple I. We essentially propose to upgrade the Maxwell
demon, a physical system with memory that inter-
acts with an experimental apparatus, with a classical
computer, a physical realization of a Turing machine,
that allows it to perform inferences about the envi-
ronment and implement self-reference. However, our
focus is not on the computations carried out on such
computer, but on the minimal physical requirements
necessary to implement them (see Figs. 16 and 17,
as well as item (vi) in Sec. B 1; see also Fig. 6 and
Appendix A for the extension of this discussion to
human observers).
To gain some early intuition on the ideas discussed
here, let us consider the physical requirements that al-
low a computer hardware to determine that two bits,
x and y, are equal, i.e. x = y (see Fig. 5). First, there
should be physical systems Sx and Sy representing
bits x and y, respectively. For instance, each physi-
cal system, say Sx, could be a magnet whose north
pole can point either upwards, representing x = 0,
or downwards, representing x = 1. Second, the com-
puter hardware needs to perform the comparison ‘=’.
Such comparison requires a physical interaction, in
hardware, between the two physical systems Sx and
Sy representing the corresponding bits. For instance,
we could perform this operation by implementing a
pairwise interaction with energy E(Sx, Sy) = −SxSy.
Such energy achieves its minimum value if and only
if the two magnets point in the same direction, i.e. if
x = y (see Fig. 5). So, depending on the value of the


## Page 8


8
energy the computer can determine whether the two
bits are equal or not.
More generally, the physical implementation of any
non-trivial gate or function requires the physical in-
teraction between the physical systems that represent
the bits that participate of the computation.
Similarly, how can a computer or a robot deter-
mine that there exists a correlation between the po-
sition of a switch and whether a lamp shines or not?
(See Fig. 17) First, the computer hardware needs two
physical systems representing the states of the switch,
i.e. on or oﬀ, and the lamp, i.e. shining or not. Let
the bit x = 1 if the switch is on, and x = 0 otherwise;
analogously, let the bit y = 1 if the lamp shines, and
y = 0 otherwise. Let us assume the robot has per-
formed n experiments with the switch and the lamp,
obtaining a dataset of pairs (xi, yi) with i = 1, . . . , n.
The robot can then compute, for instance, the Pear-
son correlation coeﬃcient
rxy =
Pn
i=1 xi yi −n ¯x ¯y
(n −1)σxσy
,
(3)
where ¯x
=
Pn
i=1 xi/n is the sample mean and
σx =
pPn
i=1(xi −¯x)2/(n −1) is the sample stan-
dard deviation, both corresponding to the state of
the switch. The sample mean ¯y and sample standard
deviation σy corresponding to the state of the lamp
are deﬁned in a similar way.
Again, the computation of rxy requires the inter-
action, whether direct or indirect, between the physi-
cal systems representing in hardware all variables in-
volved. Such computation can be performed, for in-
stance, by ﬁrst saving all data in memory using phys-
ical systems Sxi and Syi, for i = 1, . . . , n, and then
carrying out the corresponding physical interactions;
this is an instance of oﬄine learning. Alternatively,
the robot can receive each pair of data (xi, yi) one
by one and use it to update on the ﬂy the estima-
tion of rxy by performing the corresponding physical
interactions; this is an instance of online learning.
Now, how can a robot determine that turning the
switch on causes the lamp to shine? One way to do
this is via interventions [81–83].
For instance, the
robot can force the switch to be on or oﬀ, which is
denoted as do(x = x∗) , where x∗represents the ac-
tion taken by the robot (see for instance example 2
in Ref. [81]). Then the robot can estimate the corre-
sponding distribution P(y|do(x = x∗)) from experi-
mental data. If the condition
P(y = 1|do(x = 1)) ̸= P(y = 1|do(x = 0)),
(4)
is satisﬁed, for instance, the robot can infer that the
position of the switch causes the lamp to shine. In
this example we are assuming a simple scenario where
there are no latent variables and interventions are
possible; causal inference can be highly non-trivial in
more general situations [81–83]. The point we want to
make here, however, is that any computation made
above, including the comparison ‘̸=’ in Eq. (4), in-
volves a physical interaction in the hardware imple-
mentation.
In summary, there are two main physical require-
ments for a robot to determine the existence of causal
(or acausal) inﬂuences between two physical systems
X and Y (see Fig. 17). First, there must be inter-
nal physical systems SX and SY in the hardware of
the robot capable of representing the states of the
external systems X and Y , respectively. Second, the
two internal systems SX and SY must interact in one
way or another for the robot to be able to detect any
potential correlation between the external systems X
and Y .
Now, notice that each internal system al-
lows the robot to detect or ‘percieve’ the correspond-
ing external system that it represents. In this sense,
roughly speaking, while the robot is using internal
system SX to represent or percieve external system
X, the robot cannot detect or percieve the internal
system SX itself— a simple analogy of this is the fact
that an eye cannot see itself. This already suggests
that there is a ‘resolution restriction’ [11] that allows
the robot to percieve only one out of two physical sys-
tems. Such resolution restriction alone already leads
to several features of quantum theory [11, 84–86] (see
Sec. VIII C).
Furthermore, the external systems X and Y can
reﬀer to diﬀerent times, like when turning the switch
on at a given time causes the lamp to shine at a later
time (see Fig. 17).
In this case the corresponding
internal systems SX and SY refer to diﬀerent times,
say ‘past’ (initial state) and ‘future’ (ﬁnal state). The
interaction between these two internal physical sys-
tems, whose state can be described by variables which
are hidden to the robot in the sense discussed above,
is therefore an eﬀective interaction between ‘past’ and
‘future’. In this sense, the state of the internal sys-
tems are described by hidden variables which interact
non-locally. This already suggests how the locality
condition underlying Bell theorem can be broken (see
Sec. VIII C).
Finally, the physical interactions supporting the
observer’s information processing deﬁne an intrin-
sic energy scale which the external system being ob-
served should provide.
If the energy of the exter-
nal system is smaller than the energy associated to
the observer’s internal physical processes necessary to
generate a perception, the observer may not be able
to perceive anything. This might explain the origin of
the quantization of energy and suggests Planck con-
stant might be measured from psychophysics experi-
ments (see Sec. IX and Fig. 21).
As early as 1929, Leo Szilard [35] had already con-
sidered observers as physical systems to argue that
the Maxwell demon [47] could not violate the sec-
ond law of thermodynamics as Maxwell had suggested
back in 1871 [87]. Landauer argued [88] a few decades


## Page 9


9
later that the physical process of erasing information
from the demon’s memory could account for the non-
decrease in entropy postulated by the second law of
thermodynamics. A ﬁrst experimental demonstration
of a Maxwell demon was reported a few years ago in
Ref. [40].
B.
First-person perspective and self-reference
The previous discussion summarizes the intuitive
picture that can be derived from Principle I (see
Figs. 17 and 6). While this is enough to derive the for-
malism of imaginary-time quantum theory, it is not
enough to obtain the full formalism of quantum the-
ory (see Secs. V and VI). This is because our analysis
was from the perspective of an external observer: we
have been describing the robot from our own perspec-
tive (see Fig. 7). However, according to Principle II
experiments must be described from the perspective
of the robot itself as an internal observer. This is a
more subtle problem that involves self-reference (see
Figs. 7, 18, 19; see also Appendix C and Figs. 12, 14,
15).
To illustrate the kind of ideas involved in Princi-
ple II, let us consider the example of a program that
prints itself. A na¨ıve attempt would be to print the
program print ‘‘Hello world!’’; by simply doing
print ‘print ‘‘Hello world!’’;’. But the latter
does not coincide with the former; a new print oper-
ator has appeared. We can try to solve this problem
by adding a new print operator, but in this way we
actually end up in an inﬁnite regress. An example of
a program in Phyton that does print itself is [89]
s = ‘s = %r\nprint(s %% s)’
print(s % s)
This program is composed of two parts that,
roughly speaking, print each other (see Figs.
12,
14, 15 and Sec. C). Indeed, the ﬁrst line deﬁnes a
string s that contains the second line, while the sec-
ond line prints the string s deﬁned in the ﬁrst one.
This is a general feature of self-printing programs [90]
(see chapter 6), as we will discuss in more detail in
Sec. VII A. In this respect, self-reference leads to com-
plementary pairs. In Appendix C we brieﬂy review
the recursion theorem of computer science that for-
malize the construction of self-referential programs.
Another example is the sentence [90]:
Print two copies of the sentence below, the second copy in quotes
(5)
“Print two copies of the sentence below, the second copy in quotes”
(6)
If we do what is asked in this sentence we end up
printing the sentence itself. This again is composed
of two ‘complementary’ pairs: On the one hand, the
ﬁrst sentence plays an active role by instructing to
print the second one. On the other hand, the second
sentence plays a passive role by representing the ﬁrst
sentence in quotation marks; in a sense, the second
sentence could be considered as information about
the ﬁrst. Both sentences, however, are made of the
same ‘stuﬀ’: characters in an alphabet.
As we will discuss in Sec. VII B, something simi-
lar happens when a robot describes the world from
within, including itself: there should exist a pair of
complementary systems that, in a sense, mutually ob-
serve each other (see Figs. 8, 18, 19). This does not
imply that there is a misterious entity observing the
robot, rather the corresponding architecture of the
robot should support such a reﬂexive feature— a sim-
ple analogy of this is the fact that although an eye
cannot see itself if it is alone, it can do so with the aid
of a complementary system, like a mirror, that imple-
ments the required reﬂexive feature. Figure 8 shows
a simple experiment that we can do at home to get
some intuition of these ideas. (See Appendix A for
the extension of this discussion to human observers.)
IV.
QUANTUM MECHANICS RECASTED
A.
Von Neumann equation as a pair of real
matrix equations
Here we focus on ﬁnite-dimensional systems for
simplicity; so we can represent the adjoint opera-
tion † by the combination of transpose T and com-
plex conjugate ∗operations, i.e.
if µ is a generic
ﬁnite-dimensional matrix with complex entries, then
µ† = (µT )∗= (µ∗)T .
Notice that a generic Her-
mitian matrix can be written as µ = Ms + iMa,
where Ms = M T
s
is a real symmetric matrix and
Ma = −M T
a
is a real antisymmetric matrix; in-
deed µ† = M T
s −iM T
a = Ms + iMa = µ.
Further-
more, since any generic real matrix M can be decom-
posed into symmetric and antisymmetric parts, i.e.
M = Ms +Ma, then we can write Ms = (M +M T )/2
and Ma = (M −M T )/2. From this perspective, we


## Page 10


10
can consider a generic Hermitian matrix µ as a conve-
nient representation of a generic real matrix M that
allows us to keep explicit track of the symmetric and
antisymmetric parts of the latter via the the real and
imaginary parts of the former, respectively.
So, we can write ρ and H in Eq. (1) as ρ = Ps+iPa
and H = ℏJs + iℏJa. Here the symmetric and anti-
symmetric matrices corresponding to ρ and H can be
written in terms of real matrices P and J, respec-
tively, as done for the generic matrix M above. Since
Trρ = 1 and the diagonal elements of an antisym-
metric matrix are zero, we have Trρ = TrPs = TrP,
so TrP = 1. We have written H in terms of a real
matrix ℏJ so we do not have to worry about ℏin the
equations below. We will refer to J as the dynamical
matrix.
In this way, Eq. (1) can be written as
i ∂
∂t(Ps + iPa) = [Js + iJa, Ps + iPa],
(7)
where ℏhas been absorved in J = H/ℏ. Equating
the real and imaginary parts of Eq. (7) we get a pair
of equations
∂Ps
∂t
= [Ja, Ps] + [Js, Pa],
(8)
∂Pa
∂t
= [Ja, Pa] −[Js, Ps].
(9)
By adding and substracting Eqs. (8) and (9), we
obtain an equivalent pair of equations in terms of the
real matrix P, i.e.
∂P
∂t
= [Ja, P] −[Js, P T ],
(10)
∂P T
∂t
= [Ja, P T ] + [Js, P].
(11)
While Eq. (11) is the transpose of Eq. (10), we can
also write these two equations as corresponding to
two diﬀerent observers A and B who describe the
experiment with probability matrices PA and PB, re-
spectively; i.e.
∂PA
∂t
= [Ja, PA] −[Js, PB],
(12)
∂PB
∂t
= [Ja, PB] + [Js, PA],
(13)
under the condition that PA = PB at time t = 0,
which guarantees that at all next time steps we have
PA = P T
B (see Eqs. (10) and (11)). This condition is
satisﬁed for any experiment since any initial quantum
state ρ0 = UρdiagU † can be prepared by applying a
quantum operation U to a diagonal state ρdiag, and
such diagonal state would lead to diagonal probability
matrices PA = PB which are equal to each other.
So, without loss of generality the initial state of a
quantum experiment can always be considered to be
a diagonal density matrix, as long as we include the
quantum operation U as part of the experiment; since
the initial state is diagonal, the condition P = P T or
PA = PB is automatically satisﬁed at the beginning
of the experiment.
As we will describe in Sec. VII, A and B can indeed
be considered as two complementary third-person
sub-observers that essentially observe each other to
mutually build a ﬁrst-person observer, much as the
two photographers in Fig. 8b, or the self-printing pro-
grams described in Sec. III B, or the more general
programs described by the recursion theorem (see Ap-
pendix C). In Sec. IV B we recast some typical exam-
ples of quantum dynamics to show that these equa-
tions can be formulated in terms of real non-negative
kernels that therefore can in principle be interpreted
probabilistically (see also Secs. V, VI, VII).
Remark
1:
Notice that since for small time
steps ϵ we can write unitary evolution operators
as Uϵ = I −iϵH/ℏ.
So, we can write commuta-
tors with H in terms of commutators with Uϵ since
[Uϵ, ρ] = −iϵ[H, ρ]/ℏ; this is also true for other types
of evolution kernels. We can then write the von Neu-
mann equation, Eq. (1), as
∂ρ
∂t = 1
ϵ [Uϵ, ρ],
(14)
where the limit ϵ →0 is understood.
This observation is useful when dealing with Gaus-
sian kernels (see Secs. IV B 2 and IV B 3 as well as
Appendices D 2 and D 3), for instance, because a
Gaussian kernel K(x, x′) with vanishing variance σ2
cannot be expanded in a Taylor series as K(x, x′) ≈
δ(x−x′)+O(σ2), where δ(x) is the Dirac delta. How-
ever, we can straightforwardly write K(x, x′) = δ(x−
x′) −L(x, x′), where L(x, x′) = δ(x −x′) −K(x, x′).
Although L is not O(σ2), its convolution with a
smooth function yields a term O(σ2). In Secs. IV B 2
and IV B 3 (see also Appendices D 2 and D 3) we ob-
tain von Neumann-like equations similar to Eq. (14),
where commutators are directly written in terms of
real Gaussian kernels K with variance σ2 = O(ϵ).
Remark 2:
When the Hamiltonian is real, i.e.
H = ℏJs = ℏJ (since Ja = 0), Eqs. (10) and (11) be-
come
∂P
∂t
= −[Js, P T ],
(15)
∂P T
∂t
= [Js, P].
(16)
Furthermore, if the Hamiltonian is independent of
time, we can take the partial time derivative of
Eq. (15) and replace ∂P T /∂t in its right hand side
by the right hand side of Eq. (16) to obtain
∂2P
∂t2 = −[Js, [Js, P]],
(17)


## Page 11


11
which is a real second order diﬀerential equation in
the probability matrix P.
This contrasts with the
ﬁrst-order equations typically obtained for the evo-
lution of probabilities in Markov processes, e.g. the
master equation, which is usually a reﬂection of the
linearity of the Bayesian update [61, 62].
Equation (17) is similar to the equation describ-
ing the second law of Newtonian mechanics. Insist-
ing in the current paradigm (see Fig. 4), we could
attempt to interpret this as a reﬂection of the phys-
ical nature of the probabilities associated to a phys-
ical observer embedded in the system under study.
In other words, such physical probabilities not only
should represent the subjective beliefs the observer
has about the physical system being studied, but
they should also be objectively implemented in the
observer’s ‘hardware’ (e.g. as a population of neu-
rons). We will argue, however, that the structure of
physical laws themselves could be considered a result
of the self-referential problem of describing the world
from a ﬁrst-person perspective.
B.
Some examples of quantum dynamics in
terms of non-negative real kernels
Here we brieﬂy discuss how some well-known exam-
ples of quantum systems can be described in terms of
non-negative real kernels, including systems associ-
ated to complex non-stoquastic Hamiltonian opera-
tors. In Appendix D we provide the details of the
derivations. In Appendix E we discuss why the non-
negativity of the kernels is not a restriction in our
approach. Therein we show how we can obtain eﬀec-
tive kernels with negative entries, associated to real
non-stoquastic Hamiltonian operators.
1.
Non-relativistic Schr¨odinger equation
The Hamiltnoian of a single particle of mass m in
a one-dimensional non-relativistic potential V (x) is
given by H = −(ℏ2/2m)∂2/∂x2 + V (x) which, after
a suitable space discretization of x = ℓδ with lat-
ice constant δ and ℓ= . . . , −2, −1, 0, 1, 2, . . . , can be
represented by the matrix (see Appendix D 1 for all
technical details)
H ≡ℏJ =









...
...
...
...
...
· · ·
0
−
ℏ2
2mδ2
ℏ2
mδ2 + V−1
−
ℏ2
2mδ2
0
· · ·
· · ·
0
−
ℏ2
2mδ2
ℏ2
mδ2 + V0
−
ℏ2
2mδ2
0
· · ·
· · ·
0
−
ℏ2
2mδ2
ℏ2
mδ2 + V1 −
ℏ2
2mδ2
0
· · ·
...
...
...
... ...









,
(18)
2.
From non-relativistic path integrals to real
convolutions
In terms of the short-time path integral representa-
tion [91], with time step ϵ →0, the evolution equation
of the example in Sec. IV B 1 can be written as (see
Appendix D 2 for all technical details)
∂ρ
∂t = i
ϵ [(K ∗ρ) −(ρ ∗K)] ,
(19)
where ρ(x, x′, t) is the density matrix and K(x, x′) is
a real kernel given by
K(x, x′) =
1
|A| exp

−H(x, x′)ϵ
ℏ

,
(20)
with
H(x, x′) = m
2
(x −x′)2
ϵ2
+ V (x),
(21)
the corresponding Hamiltonian function and A =
p
i2πℏϵ/m (here we consider the Hamiltonian func-
tion as a function of position only).
Here we have introduced the convolutions


## Page 12


12
[K ∗ρ] (x, x′) =
1
|A|
Z
exp

−H(x, x′′)ϵ
ℏ

ρ(x′′, x′, t)dx′′,
(22)
[ρ ∗K] (x, x′) =
1
|A|
Z
ρ(x, x′′, t) exp

−H(x′′, x′)ϵ
ℏ

dx′′.
(23)
Notice that the integration variables in K∗ρ and ρ∗K
are, respectively, the ﬁrst and second arguments of ρ,
which yields the analogous of left and right matrix
multiplication.
Following the discussion in Sec. IV A, Eq. (19) can
be written as a pair of real matrix equations (see more
general example in Sec. IV B 3). The point we want
to make here is that the kernel appearing in such pair
of equations can be real and non-negative, as we can
see in Eq. (20). In the next section we show this is
also true in more general cases where the Hamiltonian
is complex.
Remark: While the kernel K deﬁned in Eq. (20) is
real and non-negative, it is not normalized. Indeed,
we have (e.g. take ψ(x′, t) = 1 in Eq. (D13))
Z
K(x, x′)dx = 1 −ϵV (x)/ℏ+ O(ϵ2).
(24)
This fact has sometimes been used to argue against
the viability of any probabilistic interpretation of the
Euclidean, or imaginary-time, Schr¨odinger equation
[92–94].
However, we will show in Sec. V and Appendix F
that the proper probabilistic analogous of K is not
a transition probability but something closer to the
squared root of the product of forward and backward
transition probabilities (cf. Eqs. (41) and (F8)). Fur-
thermore, we will show there that such a type of ker-
nel arises naturally in a less common, more symmetric
representation of standard Markov process.
3.
Particle in an electromagnetic ﬁeld via asymmetric
real kernels
The Schr¨odinger equation of a particle of charge e
interacting with an electromagnetic ﬁeld can be writ-
ten as
iℏ∂ψ(x, t)
∂t
= −ℏ2
2m

∇−i e
ℏcA
2
ψ(x, t)
+ eV (x, t)ψ(x, t),
(25)
where x denotes the position vector in three dimen-
sional space, while V and A denote the scalar and
vector ﬁelds respectively. Notice that the Hamilto-
nian associated to Eq. (25) now contains an imagi-
nary part given by the terms linear in A arising from
the expansion of (∇−ieA/ℏc)2ψ(x, t).
As shown in full detail in Appendix D 3, and fol-
lowing Sec. IV A, the von Neumann equation corre-
sponding to Eq. (25) can be written as a pair of real
matrix equations
∂PA
∂t
= −1
ϵ [Ka, PA] + 1
ϵ [Ks, PB],
(26)
∂PB
∂t
= −1
ϵ [Ka, PB] −1
ϵ [Ks, PA],
(27)
where the two probability matrices satisfy PA =
P, PB = P T , and ρ = (P + P T )/2 + i(P −P T )/2.
Here, Ks and Ka, are the symmetric and anti-
symmetric parts of a real kernel K = Ks + Ka given
by
K(x, x′) =
1
|AEM| exp
h
−ϵ
ℏHEM(x, x′)
i
,
(28)
where the real electromagnetic Hamiltonian function
is given by (here we consider the Hamiltonian func-
tion as a function of position only)
HEM(x, x′) = m
2
x −x′
ϵ
2
+ V
x + x′
2
, t

−e
c
x −x′
ϵ

· A
x + x′
2
, t

+ e2
mc2

A
x + x′
2
, t
2
= m
2
x −x′
ϵ
−e
mcA
x + x′
2
, t
2
+ V
x + x′
2
, t

+
e2
2mc2

A
x + x′
2
, t
2
,
(29)
As we will argue in Sec. VII these equations can
be interpreted in probabilistic terms. So, even in the


## Page 13


13
case of a charged particle in an electromagnetic ﬁeld,
whose Hamiltonian operator is complex (and so non-
stoquastic), can be thought of as arising from a real
non-negative kernel K. It is no clear at this point,
though, how to interpret HEM deﬁned in Eq. (29)
nor the real kernel K deﬁned in Eq. (28). It seems to
suggests a probabilistic interpretation of electromag-
netic phenomena. We leave this for future work.
Remark: We can see that the antisymmetric part
of the Hamiltonian funcion HEM deﬁned in Eq. (29)
comes from the term linear in A, which changes sign
when we transpose x and x′. Intuitively, this anti-
symmetric term is related to non-equilibrium irre-
versible phenomena since A can be thought of as an
eﬀective interaction generated by the collective mo-
tion of charged particles, while V can be generated by
charged particles at rest. (We shall argue in Sec. VII
this interpretation is valid in general.)
Indeed, from the classical electromagnetic La-
grangian
L = m
2 ˙x2 −V + e
c ˙x · A,
(30)
we get the expression for the canonical momentum
p = m ˙x + e
cA,
(31)
which implies that the Hamiltonian can be written as
H =
1
2m

p −e
cA
2
+ V
= m
2 ˙x2 + V,
(32)
which is the sum of the standard kinetic energy and
the static potential energy V . The term A appears
only when we write the kinetic energy in terms of the
canonical momentum.
V.
MARKOV PROCESSES RECASTED
A.
Principle of maximum caliber and factor
graphs
The principle of maximum Shannon entropy intro-
duced by Jaynes [95] to derive some common equilib-
rium probability distributions in statistical physics
can be extended to the so-called principle of maxi-
mum caliber to deal with non-equilibrium distribu-
tions on trajectories [96]. In particular Markov pro-
cesses can be derived from the principle of maximum
caliber (see e.g. Sec. IX B in Ref. [96]). We introduce
this principle here with an example relevant for our
discussion.
Consider
the
probability
distributions
P(x1, . . . , xn) on (discretized) paths (x1, . . . , xn),
where xℓrefers to the position at time t = ℓϵ.
Assume that we only have information about the
average energy on the (discretized) paths given by
Hav[P] =
Z
P(x1, . . . , xn)
"
1
T
n−1
X
ℓ=1
H(xℓ, xℓ+1)ϵ
#
n
Y
ℓ=1
dxℓ,
(33)
where T = nϵ is the total time duration of the path,
and H is the Hamiltonian function which, without
loss of generality, we will assume is given by Eq. (21);
all results in this section are valid for general Hamil-
tonian functions like, for instance, the one given by
Eq. (29).
The principle of maximum caliber tells us that
among all possible probability distributions we should
choose the one that both maximizes the entropy
S[P] = −
Z
P(x1, . . . , xn) ln P(x1, . . . , xn)d
n
Y
ℓ=1
dxℓ,
(34)
and is conistent with the information we have, i.e.
Hav[P] = Eav, where Eav is the ﬁxed value of the
average energy. Introducing a Lagrange multiplier λ
to enforce the constraint on the average energy, the
constrained maximization of S[P] becomes equivalent
to the maximization of the Lagrangian S −λHav[P].
The solution to this problem is the distribution
P(x1, . . . , xn) = 1
Z exp
"
−λ
T
n−1
X
ℓ=1
H(xℓ, xℓ+1)ϵ
#
,
(35)
where Z is the normalization factor.
Notice that P in Eq. (35) can be written as a prod-
uct of factors
P(x1, . . . , xn) = 1
Z
n−1
Y
ℓ=1
Fℓ(xℓ, xℓ+1).
(36)
To keep the analogy with Eq. (20) as close as possible,
we can choose the factors as
Fℓ(xℓ, xℓ+1) =
1
|A| exp

−λ
T H(xℓ, xℓ+1)ϵ

,
(37)
with |A|
=
p
2πTϵ/mλ, so Z
=
Z/|A|n−1 in
Eq. (36). Indeed, by writting ℏ= T/λ Eq. (37) is
the exact analogous of Eq. (20). Since Fℓis not a
probability distribution, it is not normalized in gen-
eral either.
The
probability
distribution
in
Eq.
(35),
or
Eq. (36), can also be interpreted as the Boltzmann
distribution of a system of particles interacting on a
chain. Now, any probability distribution of particles
interacting on a chain can be parametrized in terms
of the pairwise marginals Pℓ(xℓ, xℓ+1) of neighbor-
ing variables xℓand xℓ+1 on the chain and the single
marginals pℓ(xℓ) as (see e.g Eq. (14.22) in Ref. [97])
P(x1, . . . , xn) =
n−1
Y
ℓ=1
Pℓ(xℓ, xℓ+1)
,n−1
Y
ℓ=2
pℓ(xℓ) ;
(38)


## Page 14


14
notice the single marginals of the ﬁrst and last node
in the chain are excluded because they have only one
neighbor.
Now, using the product rule of probability theory
we can write the pairwise marginals in the three dif-
ferent ways
Pℓ(xℓ, xℓ+1) = P+
ℓ(xℓ+1|xℓ)pℓ(xℓ)
= P−
ℓ(xℓ|xℓ+1)pℓ+1(xℓ+1)
= θℓ(xℓ)Kℓ(xℓ, xℓ+1)θℓ+1(xℓ+1)
(39)
where P+
ℓand P−
ℓdenote the forward and backward
transition probabilities, respectively, and
θℓ(xℓ) =
p
pℓ(xℓ),
(40)
Kℓ(xℓ, xℓ+1) =
q
P+
ℓ(xℓ+1|xℓ)P−
ℓ(xℓ|xℓ+1).(41)
The less common, more symmetric alternative in
the third line of Eq. (39) is obtained by multiplaying
the ﬁrst two lines in Eq. (39) and taking the square
root. While this is just a more symmetric descrip-
tion of a Markov process, we show in Appendix F
that θℓand Kℓ, respectively, are similar to real wave
functions and to the real transition kernels appearing
in the modiﬁed formulation of quantum theory intro-
duced in Sec. IV (see e.g. Eqs. (D18) and (D47)).
Indeed, the third line in Eq. (39) could be considered
as a slightly more general presentation of the type of
stochastic processes originally studied by Schr¨odinger
[98, 99], known sometimes as Schr¨odinger bridges.
In such Schr¨odinger bridges we not only know the
initial probability distribution p1, but also the ﬁnal
one pn. We show in Appendix F that there are in-
deed some analogies with the so called Euclidean (or
imaginary-time) quantum mechanics and Bernstein
processes [92–94] built on Schr¨odinger’s work.
Al-
though θℓdoes not contain any ‘phase’ information,
we will see in Sec. V B that the analogous of a phase
can arise by using a formulation based on the cavity
method.
B.
Quantum-like formulation of stochastic
processes via the cavity method
1.
Cavity messages as imaginary-time wave functions
Here we show how the belief propagation algorithm
obtained via the cavity method [97] (see chapter 14)
can be naturally written in terms of the imaginary-
time Schr¨odinger equation and its conjugate.
First, notice that by marginalizing the probability
distribution deﬁned in Eq. (36) over all variables ex-
cept xℓand xℓ+1 we obtain
Pℓ(xℓ, xℓ+1) =
1
Z Fℓ(xℓ, xℓ+1)Z→ℓ(xℓ)Zℓ+1←(xℓ+1),
(42)
pℓ(xℓ) =
1
Z Z→ℓ(xℓ)Zℓ←(xℓ),
(43)
where the partial parition functions Z→ℓ(xℓ) and
Zℓ←(xℓ) of the original factor graph are given by the
partition functions of the modiﬁed factor graphs that
contain all factors Fℓ′ to the left (i.e. ℓ′ < ℓ) and to
the right (i.e. ℓ′ ≥ℓ) of variable xℓ, respectively; i.e.
(see Fig. 10a,b; cf. Eq. (14.2) in Ref. [97]).
Z→ℓ(xℓ) =
Z
ℓ−1
Y
ℓ′=1
Fℓ′(xℓ′, xℓ′+1)dxℓ′,
(44)
Zℓ←(xℓ) =
Z
n−1
Y
ℓ′=ℓ
Fℓ′(xℓ′, xℓ′+1)dxℓ′+1.
(45)
Z→ℓ(xℓ) and Zℓ←(xℓ) can be interpreted as informa-
tion that arrives to variable ℓfrom the left and from
the right side of the graph, respectively.
By separating factor Fℓ−1 and Fℓin Eqs. (44) and
(45), respectively, we can write these equations in
a recursive way as (see Fig. 10c; cf. Eq. (14.5) in
Ref. [97])
Z→ℓ(xℓ) =
Z
Fℓ−1(xℓ−1, xℓ)Z→ℓ−1(xℓ−1)dxℓ−1,
(46)
Zℓ←(xℓ) =
Z
Fℓ(xℓ, xℓ+1)Zℓ+1←(xℓ+1)dxℓ+1. (47)
These recursive equations are usually referred to as
the belief propagation algorithm.
Since the partial
partition functions are typically exponentially large,
Eqs. (46) and (47) are commonly written in terms
of normalized cavity messages ν→ℓ(x) = Z→ℓ(x)/Z→ℓ
and νℓ←(x) = Zℓ←(x)/Zℓ←, where Z→ℓand Zℓ←are
the corresponding normalization constants.
This
choice of normalization has at least two advantages:
(i) it allows us to interpret the messages as proba-
bility distributions and (ii) it keeps the information
traveling from left to right separated from the infor-
mation traveling from right to left.
We will now show that a diﬀerent choice of normal-


## Page 15


15
ization, i.e.
µ→ℓ(x) = Z→ℓ(x)
√
Z
,
µℓ←(x) = Zℓ←(x)
√
Z
,
(48)
which violates the features (i) and (ii) mentioned
above, allows us to connect the belief propagations
equations, i.e. Eqs. (46) and (47), with those of Eu-
clidean quantum mechanics. Indeed, let us write
µ→ℓ(x)µℓ←(x) = pℓ(x),
(49)
µ→ℓ(x)
µℓ←(x) = e2φℓ(x),
(50)
where Eq. (49) comes from Eq. (43) and Eq. (50) is a
deﬁnition of the ‘eﬀective ﬁeld’ or ‘phase’ φℓ. Equa-
tions (49) and (50) imply that we can parametrize
the cavity messages in terms of pℓand φℓas
µ→ℓ(x) =
p
pℓ(x)eφℓ(x),
(51)
µℓ←(x) =
p
pℓ(x)e−φℓ(x),
(52)
which are the exact analog of a ‘wave function’ in
imaginary time.
Remark: When x ∈{−1, +1} is a binary variable,
the cavity messages are usually parametrized in terms
of the the ratio µ→ℓ(+1)/µ→ℓ(−1) = e2u→ℓ, where
u→ℓis considered as an eﬀective ‘cavity ﬁeld’ (cf.
Eq. (14.6) in Ref. [97]). This choice follows the cus-
tom of not mixing information ﬂowing in opposite di-
rections. Instead, the phase φℓin Eq. (50) does mix
information ﬂowing in opposite directions.
2.
Belief propagation as imaginary-time quantum
dynamics
In terms of the quantum-like cavity messages µ→ℓ
and µℓ←, the belief propagation equations (46) and
(47) become
µ→ℓ(x) =
Z
Fℓ−1(x′, x)µ→ℓ−1(x′)dx′,
(53)
µℓ←(x) =
Z
Fℓ(x, x′)µℓ+1←(x′)dx′,
(54)
where we have done xℓ= x, xℓ−1 = x′ in Eq. (53),
and xℓ+1 = x′ in Eq. (54).
This contrasts with
the standard formulation in terms of the ν-messages
described after Eq. (47), where the messages must
be renormalized at each iteration of the belief prop-
agation equations (cf.
Eq.
(14.2) in Ref. [97]).
Such iterative renormalization is avoided here be-
cause the normalization constant
√
Z is the same for
all quantum-like cavity messages. Equations (53) and
(54) are the analogous of Eqs. (F2) and (F4) in Ap-
pendix F, and the exact equivalent of Eq. (2.16) in
Ref. [93] and its adjoint, respectively. (Indeed, the
integrals in the right hand side of Eqs. (53) and (54)
are the imaginary-time analogous to the integral in
Eq. (D13), where the cavity messages play the role of
wave functions and the kernel in Eq. (37) correspond
to the kernel in Eq. (D18); alternatively, we can also
use the kernel in Eq. (28) or any generic kernel.)
Due to the Gaussian term in the factors F (see
Eqs. (37), (20) and (21)), the integrals in Eqs. (53)
and (54) can be approximated to ﬁrst order in ϵ (in a
way similar to that of the integral in Eq. (D10)). In-
deed, since ϵ →0, the real Gaussian factor associated
to the kinetic term in Eq. (21) is exponentially small
except in the region where x −x′ = O(
p
ℏϵ/m). This
allow us to estimate the integral to ﬁrst order in
ϵ by expanding the µ terms in Eqs. (53) and (54)
around x up to second order in x −x′. Consistent
with this approximation to ﬁrst order in ϵ, we can
also do exp [−V (x)ϵ/ℏ] = 1 −V (x)ϵ/ℏ+ O(ϵ2) in fac-
tors F (see Eqs. (37), (20) and (21)). In this way we
get the equations (cf. Eqs. (D13) and (D29))
µ→ℓ(x) = µℓ−1(x) −λϵ
T Vℓ(x)µ→ℓ(x) + Tϵ
2mλ
∂2µ→ℓ(x)
∂x2
+ O(ϵ2),
(55)
µℓ←(x) = µℓ+1←(x) −λϵ
T Vℓ(x)µℓ←(x) + Tϵ
2mλ
∂2µℓ←(x)
∂x2
+ O(ϵ2).
(56)
Let µ→(x, ℓϵ) = µ→ℓ(x) and µ←(x, ℓϵ) = µℓ←(x), and
expand µ→(x, t −ϵ) = µ→(x, t) −ϵ ˙µ→(x, t) as well as
µ←(x, t + ϵ) = µ←+ ϵ ˙µ←(x, t), where t = ℓϵ and the
dot operator stands for time derivative. So, taking
ϵ →0 yield


## Page 16


16
−T
λ
∂µ→(x, t)
∂t
= −T 2
2mλ2
∂2µ→(x, t)
∂x2
+ V (x, t)µ→(x, t),
(57)
T
λ
∂µ←(x, t)
∂t
= −T 2
2mλ2
∂2µ←(x, t)
∂x2
+ V (x, t)µ←(x, t),
(58)
which
yields
precisely
the
imaginary-time
Schr¨odinger equation and its adjoint,
with T/λ
playing the role of Planck constant ℏ.
Indeed,
Eqs. (57) and (58) are equivalent to Eqs. (2.1) and
(2.17) in Ref. [92]; the analogous of θ and θ∗therein
are here µ←and µ→, respectively.
We can also use the kernel in Eq. (28) and obtain
the imaginary-time Schr¨odinger equation for a parti-
cle in an electromagnetic ﬁeld, or use any generic ker-
nel and obtain the corresponding Schr¨odinger equa-
tion.
Using Eq. (48) we can write Eqs. (42) and (43) as
Pℓ(xℓ, xℓ+1) = Fℓ(xℓ, xℓ+1)µ→ℓ(xℓ)µℓ+1←(xℓ+1),
(59)
pℓ(xℓ) = µ→ℓ(xℓ)µℓ←(xℓ).
(60)
So, the forward and backward transition probabilities
are given by
P+
ℓ(xℓ+1|xℓ) = Pℓ(xℓ, xℓ+1)
pℓ(xℓ)
= Fℓ(xℓ, xℓ+1)µℓ+1←(xℓ+1)
µℓ←(xℓ)
,
(61)
P−
ℓ(xℓ|xℓ+1) = Pℓ(xℓ, xℓ+1)
pℓ+1(xℓ+1) = Fℓ(xℓ, xℓ+1)
µ→ℓ(xℓ)
µ→ℓ+1(xℓ+1),
(62)
(63)
which are analogous to Eqs. (F1) and (F3) in Ap-
pendix F, and the exact equivalent of Eqs. (2.12) and
(2.11) in Ref. [92], respectively.
C.
Euclidean quantum mechanics: From linear
chains to cycles
As indicated by the third line of Eq. (39), and dis-
cussed in more detail in Appendix F, it is always
possible to choose the factors as Fℓ= Kℓand ob-
tain an equivalent description where the imaginary-
time wave functions θℓhave no phase. Moreover, in
the case of a chain the initial µ→1 and ﬁnal messages
µn←are completely determined by the factors F1 and
Fn−1 through Eqs. (53) and (54). This is not true,
however, when the stochastic process takes place on
a cycle, i.e. (see Fig. 11; cf. Eq. (36))
Pcycle(x1, . . . xn) =
n
Y
ℓ=1
Fℓ(xℓ, xℓ+1),
(64)
where xn+1 = x1 and the factor Fn closes the chain.
In contrast to what happen on a chain, the na¨ıve be-
lief propagation equations on a cycle, Eqs. (53) and
(54), are not exact anymore [100]. Indeed, while in
a chain there are two nodes that can be clearly iden-
tiﬁed as initial and ﬁnal points, in a cycle all nodes
are topologically equivalent, i.e. there is no intrinsic
distinction between ﬁrst and last because the whole
process is cyclical.
So, it is not possible in general to decompose the
joint distribution Pcycle(x1, . . . xn) as a Markov chain.
The best we can do in general is
Pcycle(x1, . . . , xn) = P1(x1, xn)
n−2
Y
ℓ=1
P+
ℓ(xℓ+1|xℓ, xn),
(65)
which has the structure of a Berstein process (see
e.g.
the integrand in Eq. (2.7) in Ref. [92], where
P(x1, xn) →m(x, y) therein and P+
ℓ
→h therein).
Equation (65) is related to the fact that we can turn a
cycle into a chain by removing a factor, say Fn(xn, x1)
(see Fig. 11), which requires to condition on the two
arguments of the factor, i.e. x1 and xn.
Furthermore, running the belief propagation dy-
namics described by Eqs. (57) and (58) on a cycle
does not lead to exact results anymore [100]. How-
ever, since removing a factor Fn(xn, x1) (see Fig. 11)
turns the cycle into a chain (with variables x1 and
xn clamped), Eqs. (57) and (58) become exact again
for ﬁxed values of x1 and xn. We can implement the
clamping of variables x1 and xn by keeping one of
the messages associated to each of the two variables
equal to a Dirac delta peaked at the value x∗
1 and x∗
n
to which the corresponding variables are clamped, i.e.


## Page 17


17
by keeping the messages always equal to
µ→1(x1) = µx∗
1
→1(x1) ≡δ(x1 −x∗
n),
(66)
µn←(xn) = µx∗
n
n←(xn) ≡δ(xn −x∗
n).
(67)
Now, messages µx∗
1
→1 and µx∗
n
n←are the imaginary-
time analogous of the quantum position eigenstates
|x∗
1⟩and ⟨x∗
n|, respectively, where ⟨x| x′⟩= δ(x −x′).
Furthermore, any quantum pure state |ψ⟩= U |x∗⟩
can be written as the product of an eigenstate |x∗⟩
and a unitary operator U = |ψ⟩⟨x∗|+P
x̸=x∗|φx⟩⟨x|,
where |ψ⟩⟨ψ| + P
x̸=x∗|φx⟩⟨φx| = I, which can be
implemented via a suitable Hamiltonian. Similarly,
any imaginary-time pure state can be written as the
product of an eigenstate, like µx∗
1
→1 or µx∗
n
n←above, and
a kernel given by some suitable factors F.
To summarize, for graphical models with circular
topology Eqs. (57) and (58) are exact as long as the
initial and ﬁnal states are the eigenstates µx∗
1
→1 and
µx∗
n
n←.
Furthermore, since it is not generally possi-
ble to factorize Pcycle(x1, . . . , xn) as a Markov chain,
the phase is non-trivial. So, this is somehow similar
to the imaginary-time version of the two-state vec-
tor formalism of quantum mechanics [101, 102]. In
Sec. VI we will use a diﬀerent approach to show that
a graphical model with circular topology also leads
to the imaginary-time version of von-Neumann equa-
tion, which only requires an initial condition.
VI.
THIRD-PERSON PERSPECTIVE
Here we will more thoroughly discuss how we can
interpret observations as internal representations (see
Fig. 16) and how taking into account the observer
leads to an interpretation of experiments as circular
interactions. If you dear reader already agree with
this view, you could skip straight to Sec. VI C, where
we more thoroughly discuss the arguments in Ref. [37]
that show that circularity entails non-commutativity
and the imaginary-time von Neumann equation (cf.
Sec. V C). Although our discussion here is restricted
to kernels, or factors, with non-negative entries, in
Appendix E we discuss how this discussion can be
extended to kernels with negative entries, associated
to real non-stoquastic Hamiltoinan operators.
A.
Observations as internal representations
To ﬁx ideas, consider an artiﬁcial observer, Alice,
whose ‘brain’ is a computer, i.e. a physical realiza-
tion of a Turing machine. A possible architecture of
such an artiﬁcial observer based on current machine
learning technology is discussed in detail in Fig. 16.
Generally speaking, such an artiﬁcial observer has
two major components: (i) a feature-extraction al-
gorithm which allows the observer to trim the raw
data provided by the external world to extract rel-
evant patterns from it, reducing its dimensionality;
(ii) a Turin machine that operates on the relevant fea-
tures extracted by the component described in (i), al-
lowing the artiﬁcial observer to detect potential rela-
tionships between features, manipulate such features,
generate actions based on those features to control
the external world, and implement self-reference (see
Appendix C).
According to recent research [21] we expect com-
ponents (i) and (ii) to be associated with unconscious
and conscious information processing, respectively, in
the case of humans (see Appendix B 1 for a sum-
mary of some relevant insights, particularly items (i)
and (vi)). More speciﬁcally, component (i) quickly
pre-process the external information to extract the
relevant features that have the potential to become
conscious percepts for the observer (see item (i) in
Appendix B 1); component (ii) provides a slower but
more powerful way to process the relevant informa-
tion extracted by component (i) (see item (vi) in Ap-
pendix B 1).
Suppose now that Alice receives, through her vi-
sion input channel, raw data generated by both the
light scattered from a switch and the light radiated
by a lamp (see Fig. 17a).
Suppose also that Alice
has access to some algorithm that allows her to ex-
tract the feature that both objects have two relevant
states, which can be labeled On and Off for the
switch, Light and Dark for the lamp—for a con-
crete example of a feature-extraction algorithm based
on deep learning see Fig. 16. We say that Alice has
observed the external system when she has acquired
an internal representation of it, denoted in Fig. 17a
by enclosing a replica of the system within (green)
quotation marks.
Such internal representation requires a physical im-
plementation in Alice’s hardware. Furthermore, as-
sume that Alice can have a causal model of the exter-
nal world, i.e. whether turning the switch On causes
the lamp to radiate Light. This information is rep-
resented in Fig. 17a by the green line joining Alice’s
internal representations of the switch and the lamp.
Such a line actually stands for an arrow whose di-
rection depends on whether we interpret Alice’s in-
ternal model as a simulation of the external system
(see Fig. 17b) or in the so-called ideomotor view [103],
where the cause-eﬀect relationship is, in a sense, re-
versed: Alice’s representation of the intended eﬀect
(e.g. lamp in state Light) of her action (e.g. turn
switch On) is the cause of the action. In other words,
it is not the action that produces the eﬀect, but rather
the internal representation of the eﬀect that produces
the action [103].
To be more precise, let v ∈V denote the state of the
external system under investigation and u ∈U denote


## Page 18


18
Alice’s internal representation of it (see Fig. 17d).
Here U and V denote the corresponding sets of states
for the systems that are internal and external to Al-
ice, respetively. For simplicity, we will assume that
U = V, i.e. we will describe only the features of the
external system considered relevant by Alice, rather
than the whole raw data (see Fig. 16). Indeed, both
the external world and Alice’s internal representation
of it are here described from the perspective of an
external observer that can also extract the same fea-
tures from both Alice’s internal and external world
(see Fig. 7).
B.
Experiments as circular interactions
1.
Simulation interpretation
In this section we formalize Principle I and show
that treating the observer as a physical system which
is part of the experimental setup implies that ex-
periments can be represented by graphical models
with circular topology (see Figs. 6, 11, and 17; cf.
Refs. [55, 104]). We will also show that such a cir-
cular topology naturally leads to a non-commutative
probability theory. Here, we are only interested in
the formal probabilistic structure of the theory, not in
the speciﬁc representation of each probability distri-
bution in terms of physical quantities, such as mass,
charge, etc. Finally, we will also show that when the
interactions associated to the observer are neglected,
we recover the standard representation of physical
systems by linear graphical models, i.e. chains.
Assume that external system is in an initial state
vi and that Alice’s corresponding internal represen-
tation is ui (see Fig. 17d). Similarly, assume the ﬁ-
nal state of the external system is vf and that Al-
ice’s corresponding internal representation is uf. Let
Pext(vf|vi) be the probability for the external system
to evolve from the initial state vi to the ﬁnal state vf
(pink arrow in Fig. 17d). Let Pprep(vi|ui) be the prob-
ability that the system is in state vi when Alice’s in-
ternal representation is ui (red arrow in Fig. 17d); this
can be interpreted as Alice’s (possibly noisy) prepa-
ration of the initial state.
Let Pmeas(uf|vf) be the
probability that, when the ﬁnal state of the external
system is vf, Alice’s corresponding internal represen-
tation is uf (blue arrow in Fig. 17d); this can be in-
terpreted as a (possibly noisy) measurement of the
ﬁnal state.
Now, in what we here refer to as the ‘simulation in-
terpretation’ (see Fig. 17b) we can deﬁne Psim(uf|ui)
as the probability that Alice’s internal representation
ui of the initial state evolves towards the represen-
tation uf of the ﬁnal state (green arrow). This dy-
namics is expected to be a faithful simulation of the
dynamical evolution of the external system. The joint
probability of all variables can therefore be written as
PSI(ui, vi, uf, vf) = Pprep(vi|ui)pprep(ui)Pext(vf|vi)Pmeas(uf|vf)Psim(uf|ui)
= Fprep(ui, vi)Fext(vi, vf)Fmeas(vf, uf)Fsim(uf, ui)
(68)
where psim(ui) stands for the probability that Alice’s
representation of the initial state is ui.
The second line of Eq. (68) emphasizes the factor
graph representation, where the factors correspond
to the probabilities with the same subscript.
The
most relevant feature of Eq. (68) is that it represent
a graphical model on a circular topology (see Figs. 6,
11, and 17). As ﬁrst discussed in Ref. [37], and re-
viewed in Sec. VI C 1 below, circularity entails non-
commutativity.
2.
Ideomotor interpretation
The simulation interpretation discussed in the pre-
vious section assumes the observer passively models
the external world; she does not have the opportunity
to interact with it, to control it. Here we describe a
more active interpretation of the observer, where she
can intervene the system (cf. Refs. [55, 104]). We ex-
pect this to be a more faithful representation of what
actually happens in an experiment and, as we shall
see in Sec. VII it is the one that is consistent with
quantum dynamics.
So, suppose that Alice performs an experiment to
learn whether the state of the switch (i.e. On or Off)
has a causal inﬂuence on the state of the lamp (i.e.
Light or Dark). Again, we say Alice has observed
the external system when she has acquired an inter-
nal representation of it, denoted by enclosing a replica
of the system within quotation marks (see Fig. 17a).
And such an internal representation requires a phys-
ical implementation in Alice’s hardware, as we have
already mentioned.
To perform the experiment, Alice ﬁrst ‘decides’
which intervention to do, i.e. where to position the
switch, and then ‘acts’ by moving the switch accord-
ingly; such action requires a physical interaction rep-
resented by a red arrow in Fig. 17a (cf. Fig. 6). Af-
ter preparing the system via her interventions, Alice


## Page 19


19
leaves the system evolve (see pink arrow in Fig. 17a)
and measure the state of the lamp. Such measure-
ment also requires a physical interaction represented
by the blue arrow in Fig. 17a (cf. Fig. 6).
Now, to test a probabilitic theory we need to re-
peat an experiment a number of times large enough to
have statistically signiﬁcant results; we need to do so
even if the theory is deterministic because otherwise
how can we be sure it is indeed deterministic? By
running the experiment m times Alice can obtain a
dataset D = {(u(1)
i
, u(1)
f
), . . . , u(m)
i
, u(m)
f
)}, where u(d)
i
and u(d)
f
respectively stand for Alice’s internal repre-
sentations of the state of the switch and the lamp at
the d-th run of the experiment. Alice can use D to
build a causal model represented by the green line
in Fig. 17a joining the two representations; this line
actually stands for an arrow whose direction depends
on whether we assume the simulation interpretation
discussed in the previous section or the ideomotor in-
terpretation discussed in this section. If we interpret
Alice’s causal model as a simulation of the external
system (see Fig. 17b), then the arrow corresponding
to the green line should point in the same direction
of the external (pink) arrow.
Alternatively, as we already mentioned above, in
the so-called ideomotor view [103], Alice’s causal
model is reversed (see Fig. 17c): Alice’s representa-
tion of the intended eﬀect (e.g. lamp in state Light)
of her action (e.g. turn switch On) is the cause of
the action. In other words, it is not the action that
produces the eﬀect, but rather the internal represen-
tation of the eﬀect that produces the action [103].
We expect this to be a more faithful representation
of the situation in an experiment. However, this leads
to a graphical model that is a directed loop represent-
ing reciprocal causation, a subject that to the best of
our knowledge is not as developed as the most stan-
dard models of causality based on directed acyclical
graphs, i.e. with no loops (see e.g. Ref. [105], chap-
ter 12.1). Nonetheless, circular causality is a common
theme in cognitive science [1].
However, we can use the principle of maximum cal-
iber introduced in Sec. V A to extend the derivation
of Markov chains [96] to cycles (see Sec. V A). This
yields a factor graph like the one in Fig. 11a. Alter-
natively, if Pdec(ui|uf) is the probability for the agent
to decide to prepare ui if she wants to observe uf we
could write (cf. Ref. [55])
PIM(ui, vi, uf, vf, u′
i) = Pprep(vi|ui)Pext(vf|vi)Pmeas(uf|vf)Pdec(u′
i|uf)
= ˜Fprep(ui, vi)Fext(vi, vf)Fmeas(vf, uf)Fdec(uf, u′
i),
(69)
for
the
probability
to
observe
a
path
ui →vi →vf →uf →u′
i
in one cycle.
However,
if we assume that for the observer to prepare
the external system in state vi she has to always
have
the
same
internal
representation
ui,
e.g.
Pprep(vi|ui) = δ(vi −ui), then ui = u′
i once the
experiment has stabilized; this is consistent with von
Foerster’s view [106] that the objects we percieve
can be considered as tokens for the behavior of the
organism that apparently creates stable forms [107].
Let us considere a thought experiment to better
illustrate this point.
Thought
experiment:
Imagine,
for instance,
recording all the research process that led to the de-
tection of the statistical regularity, or pattern, that
we call ‘Higgs boson’ in the massive dataset gener-
ated at the LHC [108, 109].
Imagine that we now
play such recording at a much faster speed to com-
press years of work into a few minutes of video. To
avoid any potential prejudice to interfere, imagine
that all researchers appearing in the video are instead
robots (see e.g. Ref. [42]). We could say that what
we observe in the video is itself a physical process
where some physical systems, to some of which we
perhaps attribute some notion of ‘agency’, interact
with others. We could also say that one of the out-
comes of such myriad interactions is that the robots
‘learn’ about the statistical regularities in the systems
they investigate. Finally, we could also say that, in
general, the robots would have to learn even what to
call a ‘system’, which experimental devices to built
and how to build them, from their repeated interac-
tions with the other ‘systems’, including the inter-
actions associated to the message passing or ‘discus-
sions’ among themselves. We are not concerned here
with the whole learning process, but only with the
last stage when the robots have already identiﬁed
some regularities, or stabilities, in their interaction
with the experimental devices.
An instance of such regularities or stabilities could
be that the agent is involved in a circular path
ui →vi →vf →uf →ui which always returns to the
same initial state ui. The corresponding probability
in this case would be given by


## Page 20


20
PIM(ui, vi, uf, vf) = Pprep(vi|ui)Pext(vf|vi)Pmeas(uf|vf)Pdec(ui|uf)
= eFprep(ui, vi)Fext(vi, vf)Fmeas(vf, uf)Fdec(uf, ui).
(70)
We can see that either the simulation interpretation
or the ideomotor view produce the same factor graph
topology (see Fig. 17d).
From now on we will as-
sume we can ﬁnd such a cyclic Markov process via
the maximum caliber principle (see Sec. V A).
In summary, the most relevant feature from this
analysis is that, once we take into account the ob-
server as part of the experimental set-up, the topol-
ogy of the interactions taking place in an experiment
is circular (see Figs. 6, 11, and 17; cf. Refs. [55, 104]).
In contrast, when the interactions associated to the
observer are neglected, the aparent topology of in-
teractions taking place in an experiment is that of a
chain (see Fig. 17e). Notice that the initial and ﬁnal
nodes of a chain (e.g. v1 and v3 in Fig. 17e) interact
with only one single node (e.g. v2 in Fig. 17e), while
the rest of the nodes (e.g. v2 in Fig. 17e) interact
with two nodes instead (e.g. v1 and v3 in Fig. 17e).
This allows us to specify well-deﬁned initial and ﬁnal
states and propagate them forward and backward in
time, respectively, through the chain via the transi-
tion probabilities. This contrasts with the case of a
circular topology (see Fig. 17d) where no single node
is special in this sense: there is neither beginning nor
end on a circle (see Sec. VIII C).
We will show in the following that this point of view
is indeed useful and allows us to derive the formal-
ism of quantum theory. Although these ideas could
in principle be formulated using the language of ac-
tive or reinforcement learning, we will stick here to
the more traditional and more general language of
probabilistic graphical models [97, 100, 110, 111].
C.
Imaginary-time von Neumann equation
1.
Circularity entails non-commutativity
We already discussed in Sec. V C that circularity
leads to something that looks somehow similar to the
imaginary-time version of the two-state vector for-
malism of quantum mechanics [101, 102]. Here we
will review the derivation of the imaginary time von
Neumann equation provided in Ref. [37] for factor
graphs with circular topologies (see Fig. 11). In this
case, the probability of observing a path of external
visible variables (v1, . . . , vn) is given by Eq. (64), i.e.
(see Fig. 11a; cf. Eq. (36)):
Pcycle(v1, . . . , vn) =
n
Y
ℓ=1
Fℓ(vℓ, vℓ+1),
(71)
where vn+1 = v1 and the factor Fn(vn, v1) summa-
rizes the chain of interactions usually ignored between
initial and ﬁnal states through the observer repre-
sented by the green chain in Figs. 11 and 17—here
we are assuming the normalization constant has been
absorbed into the factors Fℓto simplify the notation.
For instance, in the case illustrated in Fig. 17d we can
write Fn(vn, v1) as the product of all pairwise factors
involving at least one of the variables a1, ui, u1, uf, o1,
marginalized over all those variables. This leaves only
the dependence on the variables vi (through the fac-
tor involving variables vi and a1) and vf (through the
factor involving variables vf and o1), summarized by
the factor Fn(vn, v1).
With some abuse of notation we will denote by
Fℓthe matrix with elements Fℓ(vℓ, vℓ+1); so, the
marginal probability of a variable, say v1,
p1(v1) =
X
v2,...,vn
Pcycle(v1, . . . , vn),
(72)
according to Eq. (71) is given by the diagonal ele-
ments of the matrix product
P1 = F1 · · · Fn,
(73)
which deﬁnes the probability matrix P1; i.e. p1(v1) =
P1(v1, v1), much like the Born rule of quantum me-
chanics. Notice that P1, being a matrix product, also
contains oﬀ-diagonal terms P1(v1, v′
1). Similarly, the
marginal probability p2(v2) that the state of the ex-
ternal system is v2 at the next time step is given by
the diagonal elements of the probability matrix
P2 = F2 · · · FnF1,
(74)
and so on. In other words, the dynamical evolution
of the probability matrices Pℓis given by the cyclical
permutation of the factor matrices Fℓ(cf. Ref. [112]).
Now, if F1 is invertible we can multiply Eq. (73) by
F −1
1
and F1 from the left and from the right, respec-
tively (see Sec. VI C 2 for an alternative approach that
also works when some factors Fℓare non-invertible).
In this way we can see that P2 = F −1
1
P1F1 and, ex-
tending the argument for any ℓ, we can see that it is
valid in general, i.e.
Pℓ+1 = F −1
ℓ
PℓFℓ.
(75)
Equation (75) is analogous to a Markovian update
rule in the case of an open chain, in the sense that it
allows us to compute the probability matrix Pℓ+1 at
time step ℓ+ 1 from the probability matrix Pℓat the


## Page 21


21
previous time step ℓ. So, it is mathematically conve-
nient to interpret the state of the external system at
time step ℓby the matrix Pℓ. The oﬀ-diagonal ele-
ments of this probability matrix encode information
necessary to reconstruct all states step by step. In
this sense, the state contains kinematic and dynami-
cal information as suggested by Spekkens [113].
If we assume that changes in the system during
time steps of size ∆t > 0 are small, so we can
write Fℓ= I −Jℓ∆t + O(∆t2), where I is the iden-
tity matrix and Jℓis a matrix with non-positive
oﬀ-diagonal elements; without loss of generality, we
will assume Jℓ= J for all ℓof interest, and will
refer to J as the dynamical matrix.
Similarly,
F −1
ℓ
= I + J∆t + O(∆t2). In this way, Eq. (75) be-
comes Pℓ+1 = Pℓ+ [J∆t, Pℓ] or, in the continuous
limit
∂P
∂t = [J, P].
(76)
So, circularity entails non-commutativity.
2.
Pure states and causality
We will now present in more detail the argu-
ment outlined in Appendix A of Ref. [37] related
to the conditions enforced by the requirement that
the probability matrix is (the imaginary-time ver-
sion of) a pure state.
Recall that any quantum
pure state ρψ = |ψ⟩⟨ψ| = UρvU † can be written
as the evolution of an eigenstate ρv = |v⟩⟨v|, with
entries ⟨v′| ρv |v′′⟩= δvv′δvv′′, via a unitary operator
U = |ψ⟩⟨v| + P
v′̸=v |χv′⟩⟨v′|, where ⟨v| v′⟩= δvv′
and |ψ⟩⟨ψ| + P
v′̸=v |χv′⟩⟨χv′| = I. In the same way,
any imaginary-time pure state Ppure = F −1P vF (see
Eq. (75)) can be written as the evolution of a pure
state P v with only one single entry diﬀerent from
zero, i.e. an ‘eigenstate’, via the imaginary-time ver-
sion of U, which is F. Since the probability matrix
P v has only one entry diﬀerent from zero, at least one
of the factors that deﬁnes it (see Eqs. (73) and (74))
should be non-invertible, however, the approach that
follows do not require invertibility of all factors Fℓ,
only of the factor F deﬁning Ppure above.
So, without loss of generality, we will study the
evolution from an initial probability matrix P v
1 with
entries
P v
1 (v′, v′′) =
X
vn
Fext(v′, vn)Fn(vn, v′′) = δvv′δvv′′,
(77)
where the matrix Fext = F1 · · · Fn−1 summarizes the
product of the ﬁrst n −1 factors in the left hand side
of Eq. (73), which characterize the physical process
taking place on the external system. So, the sum in
Eq. (77) is equivalent to the whole product in the left
hand side of Eq. (73).
Since all factors Fℓare non-negative so is Fext and
the sum in Eq. (77) can be zero only if all its terms
are zero. So, if v′ ̸= v then Fext(v′, vn) = 0 for all
vn, i.e. the corresponding matrix Fext has all entries
equal to zero except for those in row v. Similarly,
if v′′ ̸= v then Fn(vn, v′′) = 0 for all vn, i.e.
the
corresponding matrix Fn has all entries equal to zero
except for those in column v. In other words, since
the matrix P v
1 = FextFn is a product of two matrices
with non-negative entries and P v
1 has only one entry
diﬀerent from zero, matrices Fext and Fn should only
have one row and one column with non-zero entries,
respectively. In other words, assuming the v variables
are discretized in steps of size ξ, we can write Eq. (77)
as








...
...
...
· · ·
0
0
0 · · ·
· · ·
0
1
0
· · ·
· · · 0
0
0
· · ·
...
... ...








=








...
...
...
· · ·
0
0
0
· · ·
· · · Fext(v, −ξ) Fext(v, 0) Fext(v, ξ) · · ·
· · ·
0
0
0
· · ·
...
...
...
















...
...
...
· · · 0 Fn(−ξ, v) 0 · · ·
· · · 0
Fn(0, v)
0 · · ·
· · · 0
Fn(ξ, v)
0 · · ·
...
...
...








(78)
Now, since the dynamical evolution of P v
1 is given
by the permutation of factors Fℓ(see Eqs. (73) and
(74)), the ﬁnal probability matrix Pn satisﬁes
Pn(v′, v′′) =
X
v1
Fn(v′, v1)Fext(v1, v′′) = Fn(v′, v)Fext(v, v′′);
(79)


## Page 22


22
the last equality follows because Fext and Fn are
equivalent to a row and a column vector, respectively,
and therefore only terms with v1 = v are diﬀerent
from zero (see Eq. (78)). Pn is obtained by permuting
the two matrices in the right hand side of Eq. (78).
As the diagonal elements yield the correspond-
ing probabilities, i.e.
Pn(v′, v′) = pn(v′) we can
parametrize the factors via (cf. Eqs. (49) and (50))
Fn(v′, v)Fext(v, v′) = pn(v′),
(80)
Fn(v′, v)
Fext(v, v′) = e2φn(v′).
(81)
Hence the factors can be written as
Fn(v′, v) =
p
pn(v′)eφn(v′),
(82)
Fext(v, v′) =
p
pn(v′)e−φn(v′),
(83)
which look as imaginary-time wave functions (cf.
Eqs. (51) and (52)). So, the probability matrix can
be written accordingly as
Pn(v′, v′′) =
p
pn(v′)pn(v′′), eφn(v′)−φn(v′′).
(84)
This analysis is valid for all initial eigenstates P v
1 cor-
responding to all possible values of v. We can there-
fore write Eq. (84) in terms of the imaginary-time
version of a uitary operator that includes the corre-
sponding transformation for all possible values of v,
in the same way it is usually done in quantum me-
chanics.
It might be tempting to use the additional degree
of freedom φn and apply the Madelung transforma-
tion [114] to get a perfect analogy with quantum me-
chanics (see e.g. [61, 62]).
However, this will add
further mathematical structure associated with the
periodicity of the wave function [115], which we will
argue in Sec. VII arises from the implementation of
the ﬁrst-person perpective.
Now, following the notation introduced in Sec. VI B
we can write Fext(v1, vn) = Pext(vn|v1).
So, that
Fext(v1, vn) = 0 for all v1 ̸= v could be interpreted
as an intervention done on the external system en-
forcing that v1 = v.
Using Pearl’s do calculus of
causal inference, we can represent this intervention
as do(v1 = v); thus we can write Fext(v1, vn) =
Pext(vn|do(v1 = v)), using the convention that the
right hand side, considered as a function of v1, is zero
for all v1 ̸= v.
Similarly, since factor Fn characterizes the physi-
cal processes related to the observer (see Figs. 11 and
17), following the notation introduced in Sec VI B we
can write Fn(vn, v1) = P
u1 Pprep(v1|u1)G(u1, vn),
where u1 is the observer’s representation of v1, and
G summarizes the remaining interactions regarding
the observer, i.e. measurement, and decision or sim-
ulation. So, that factor Fn(vn, v1) = 0 for all v1 ̸= v
could be interpreted as an intervention done by the
agent which, extending Pearl’s do calculus nota-
tion, we here write as Pprep(do(v1 = v)|u1).
We
can therefore write Fn(vn, v1) = P
u1 Pprep(do(v1 =
v)|u1)G(u1, vn), using the convention that the right
hand side, considered as a function of v1, is zero for
all v1 ̸= v. This could be interpreted as modeling
the agent’s intention of doing an intervention on the
system. This also suggest how causality may be en-
forced by the need to break the intrinsic circularity
of experiments (see Sec. V C and Fig. 11).
VII.
FIRST-PERSON PERSPECTIVE
Here we discuss how turning from the third- to the
ﬁrst-person perspective leads to genuine, real-time
quantum dynamics, eﬀectively implementing a Wick
rotation.
We ﬁrst discuss how the self-referential
problem of describing the world from within, includ-
ing ourselves, requires a complementary architecture
of the ﬁrst-person observer (Sec. VII A). Afterwards,
we discuss how implementing such a complementary
architecture leads to the von Neumann equation in
real-time. Although here we restric our attention to
transition kernels, or factors, with non-negative en-
tries, in Appendix E we discuss how eﬀective kernels
with negative entries can also be included in this ap-
proach.
A.
Self-reference and complementarity
Up to now our analysis has been based on Fig. 17,
which is from the perspective of an external third-
person observer not included in the ﬁgure: in this
case you dear reader that has been looking at it from
your own private ﬁrst-person perspective. To include
a model of you in the ﬁgure we would need a fourth
observer and so on (see Fig. 7); we get an inﬁnite
regress. A similar phenomenon happen when a sys-
tem, such as the DNA molecule [46], has to repro-
duce itself. A na¨ıve approach may suggest that such
a system must contain a copy of itself, and for such a
copy to be able to reproduce too, the copy must also
contain another copy; continuing with this argument
we may soon conclude that a self-reproducing sys-
tem must contain inﬁnite copies of itself. We know,
however, that the architecture of the DNA molecule
composed of two complementary strands, each gen-
erating a copy of the ohter strand, avoids such an
inﬁnite regress. Or like the painter, Alice, that wants
to make a painting of the whole Universe, but cannot
paint herself. A second painter, Bob, can paint the
Universe, including Alice but not himself, and so on.
Nevertheless, Alice and Bob could play complemen-
tary roles and mutually paint each other along with
the rest of the Universe (see Fig. 8). As we discussed
in Sec. III B (see also Appendix C), using comple-
mentary pairs is a standard technique to deal with
self-reference [74, 76, 90].


## Page 23


23
Consider the example of self-printing programs, or
quines, discussed in Sec. III B (see also Appendix C
for a detailed description based on chapter 6 of
Ref. [90]): A Turing machine Self = Alice ◦Bob
that ignores its input and prints out a copy of its
own description is composed of two parts, Alice and
Bob.
These two parts are complementary in the
sense that the task of Alice is to print out a de-
scription of Bob, and vice versa. While Alice di-
rectly prints out a description of Bob, the latter has
to compute or infer who Alice is from its output
to avoid a circular deﬁnition. In this sense, Alice
and Bob run in opposite directions. We will see in
Sec. VII B that something similar occurs in quantum
theory.
Furthermore, as we have already mentioned in
Sec. III B (see also Appendix C), an important as-
pect that allows a system to refer to itself is a ‘dual-
ity’ between the active and passive roles that it can
play. Consider, for instance, the active role played by
a Turing machine TM (the abstract version of an ex-
ecutable ﬁle) and the passive role played by a descrip-
tion of it “TM” (the abstract version of the code un-
derlying the executable ﬁle). A universal Turing ma-
chine can be deﬁned as UTM(“TM”, w) = TM(w),
where the ﬁrst argument, “TM”, is interpreted as
the description of a Turing machine TM and the
second argument, w, as an input to the Turing ma-
chine TM (see Ref. [116], chapter 7).
Such a uni-
versal Turing machine UTM runs the Turing ma-
chine TM described by its ﬁrst argument on the in-
put w on its second argument; this is represented
here as TM(w). If we chose w = “TM” we obtain
UTM(“TM”, “TM”) = TM(“TM”), i.e. a program
running on itself.
Something similar happens in logic where every
logical formula can be indexed by a number, a ‘G¨odel
number’ [117]. In this way, we can create a logical
formula F(¯n) that has a free variable ¯n, an integer,
which can be interpreted by the mathematician as the
G¨odel number of another logical formula. It is possi-
ble to set ¯n = ¯n∗to be equal to the G¨odel number ¯n∗
of the formula F(¯n) itself, and in this way F(¯n∗) can
be a self-referential logical statement.
In quantum
theory a physical observer can also play dual roles:
active when observing another system, and passive
when being observed.
Another example of self-reference is the so-called
autocell [118] or autogen [74] (chapter 10), which
consists of two molecular processes:
autocatalysis
and self-assembly.
These two processes are com-
plementary in the following sense: the autocataly-
sis produces molecules that tend to spontaneously
self-assemble, while such self-assembling molecules
can form closed structures that isolate the catalizers
from the environment and prevent them from get-
ting exhausted. If such container breaks, the catalyz-
ers can produce further self-assembling molecules and
re-generate or replicate themselves, if they are in a
suitable environment . This is a biological analogous
of von Neumann self-replicating machines [119]. It
is curious that von Neumann was aware of the in-
ﬁnite regress that plagued both the process of self-
replication [119] and the process of measurement
in quantum mechanics [49].
While he tamed self-
reference in the former he did not tackle the latter,
as far as we know.
B.
First-person observers and quantum
dynamics
1.
General considerations
Following the insights of self-printing programs,
formalized
by
the
recursion
theorem
(see
Ap-
pendix C), we here explore in more detail the assump-
tion that an observer capable to have a representation
of itself should be composed of two parts, Alice and
Bob, which play dual roles: active when observing
and passive when being observed (see Figs. 18 and 19;
cf. Fig. 8)—we are using here the ideomotor interpre-
tation described in Sec. VI B 2 which we will argue in
Sec. VII B 2 is the one consistent with quantum the-
ory, while the simulation interpretation described in
Sec. VI B 1 is not. We will use the name Self to refer
to a generic instance of such self-referential observers;
using a notation similar to that in Appendix C, we
could write Self = Alice ◦Bob. The intuition is
that Bob can help Alice infer her subjective state
by acting as a kind of mirror. In the case of humans
this mirroring mechanism might be implemented by
the so-colled mirror neuron system [120, 121]. As sug-
gested in Ref. [121], mirror neurons are usually ac-
tivated when we temporarily ‘adopt’ a third-person
perspective of ourselves, and self-awareness may be
understood as the use of these neurons for ‘looking
at myself as if someone else is looking at me’. As dis-
cussed further in Sec. IX D, the insights from the re-
cursion theorem suggest that the neural architecture
of the self is expected to be composed of two comple-
mentary systems, which might explain why our brain
is divided into hemispheres (see Fig. 20).
Figure 18 describes the architecture of such a self-
referential observer Self (cf. Fig. 8). As we said,
Self consists of two sub-observers, Alice and Bob,
that mutually observe each other, playing comple-
mentary roles as either observing subjects or observed
objects. Figures 18a, b show this mutual observation
form the perspective of an external, or third-person
observer, Chris, while Fig. 18c shows the ﬁrst-person
observer Self (cf. Fig. 8b). Notice that the physi-
cal process is one and the same for Chris, except for
the interpretation Chris does of the roles played by
Alice and Bob.
Here it is important to distinguish between the


## Page 24


24
ﬁrst- and third-person descriptions of the changes in
an observer’s state. For instance, Chris in Fig. 18
is an observer external to the system composed of
Alice and Bob.
So, Chris can apply the results
discussed in Sec. VI; in particular, Chris can de-
scribe the changes in the states of Alice and Bob
using Eq. (76) for each. To distinguish the third- and
ﬁrst-person perspectives, we here denote the changes
described by Eq. (76) with a superscript ‘3rd’. So,
we will denote the changes in the state of observer
O ∈{A, B} as ∆3rdPO which, according to Eq. (76),
for small time-intervals ∆t are given by
∆3rdPO = ∆t[J, PO].
(85)
Consider now Fig. 8 again. When Alice takes a
picture of Bob, which is a physical system, such a
picture has to be physically represented in Alice’s
camera’s hardware, i.e. both the system being ob-
served (i.e. Bob) and the corresponding representa-
tion in the observer’s ‘brain’ (i.e. the camera’s hard-
ware) are made of the same physical stuﬀ. Similarly
in Fig. 18, when Alice observes the changes in Bob’s
state—which should coincide with those observed by
Chris’, i.e. ∆3rdPB = ∆t[J, PB], because they are
both external to Bob—such changes should be repre-
sented in Alice’s hardware with a change in her own
state. Such internal changes in Alice’s state, which
represent for her the external changes she observes in
Bob’s state, are Alice’s ﬁrst-person changes ∆1stPA,
denoted here with a superscript ‘1st’ . So, while Al-
ice cannot directly observe the changes in her own
state, she can still infer them from the changes she
observes in Bob’s state.
So, the changes in state
associated to observer O ∈{A, B}, thought of as a
component of the ﬁrst-person observer Self, will be
denoted by ∆1stPO. In the next two sections we will
show how this strategy allows Alice and Bob to it-
eratively construct their subjective state. To do so,
it will be useful to remember a couple of things we
have already discussed.
First, as we mentioned in Sec. VI C 2 (see para-
graph before Eq. (77)), without loss of generality
we can assume that the initial states PA,0 and PB,0
for both Alice and Bob, respectively, are diago-
nal. Furthermore, such diagonal states are the same
for both Alice and Bob as they represent common-
knowledge ‘classical’ information, i.e. information ac-
cessible to all experimenters. In summary
PA,0 = PB,0 = diag(. . . , p−ξ, p0, pξ, . . . ),
(86)
where . . . , p−ξ, p0, pξ, . . . are the probabilities of the
variables v, which for illustrative purposes we assume
are discretized in steps of size ξ (cf. Sec. VI C 2).
Second, as illustrated in Fig. 16 (see also Ap-
pendix B 1) an observer has two components:
(i)
a feature-extraction algorithm that allows the ob-
server to extract high-level features from the raw
data provided by the external environment; (ii) a sort
of Turing machine, or recursive neural network (see
Sec. IX D), that can operate over those high-level fea-
tures to create, for instance, a dynamical model of the
external world, here characterized by the dynamical
matrix J.
According to recent research we expect
that, in the case of humans, components (i) and (ii)
are associated with unconscious and conscious infor-
mation processing respectively (see items (i) and (vi)
in Appendix B 1).
In particular, we assume here that observers can
only perceive the high-level features extracted by
component (i), as well as any relevant operations per-
formed with component (ii). This is consistent with
the fact that we do not perceive the raw data provided
by the bombardment of electromagnetic radiation re-
ﬂected from an image, but rather the high-level fea-
tures that characterize the image. Figures 18 and 19
only take into account component (ii), referring to the
raw data along with all information processing carried
out with component (i) as the environment.
Now,
the eﬀective dynamical model that can be created
by component (ii) can be reversible or irreversible,
i.e. the corresponding dynamical matrix is symmetric
J = JT or asymmetric J ̸= JT respectively. Much as
quasi-static thermodynamic processes, i.e. those that
are near equilibrium, are reversible, we expect that
an eﬀective reversible dynamical model is generated
by an environment at equilibrium. Similarly, much
as nonequilirbium thermodynamic processes produce
entropy and are therefore irreversible, we expect that
an eﬀective irreversible dynamical model is generated
by an environment out of equilibrium. Although we
will assume this is the case here (see Fig. 19), our
derivations only depend on the distinction between
reversible and irreversible eﬀective dynamical mod-
els, and not on whether the environment is in or out
of equilibrium.
In the next two sections we will describe in more de-
tail the architecture of such self-referential observers
(see Figs. 18 and 19) and argue they lead to the von
Neumann equation of quantum mechanics. To build
intuition we ﬁrst discuss the special case of symmet-
ric kernels, such as the kernel introduced in Eq. (20),
which we expect to be associated to equilibrium en-
vironments. Afterwards we discuss the general case
where kernels can be asymmetric, such as the kernel
introduced in Eq. (28), which we expect to be associ-
ated to environments that can be out of equilibrium.
Remark: Everything we discuss here is considered
physical, and so is the state P we associate to a phys-
ical system. Such state must be represented in the
‘hardware’ of the physical observer.
Although the
state is subjective for Alice in that it is information
she possesses, it is objective for Bob as it is phys-
ically represented in Alice’s brain, e.g.
as a popu-
lation of neurons.
In this sense, including the ob-
server in the description of the experiment merges the


## Page 25


25
Bayesian [8] and frequentist interpretation of proba-
bility theory [122].
2.
Equilibrium environment and symmetric kernels
In this section we assume the environment the self-
referential observer Self = Alice◦Bob is embedded
in (see Fig. 19; cf Fig. 16) is in equilibrium. So, there
are no irreversible contributions to the circular pro-
cess of mutual observation between Alice and Bob,
i.e. the dynamical matrix J = JT = Js is symmetric.
(see Ref. [38] for a more compact and formal discu-
sion)
In this case the ﬁrst-person changes in Alice’s
state, i.e. the changes in her state when she is the
observing subject and Bob is the observed object,
are equal in magnitude but opposite in sign to the
third-person changes observed by Chris in Bob’s
state, i.e. ∆1stPA = −∆3rdPB (see Fig. 18a). This
kind of action-reaction eﬀect is similar to the energy
exchanges that take place in an isolated system com-
posed of two subsystems: any change in energy in one
of the subsystems is equal and opposite to the energy
change in the other subsystem. We can see this more
clearly by noticing in Fig. 18a that the (green) verti-
cal arrow associated to ∆1stPA goes upwards, while
the (pink) vertical arrow associated to ∆3rdPB goes
downwards.
Something similar could be said for Bob’s ﬁrst-
person changes when the roles are reversed (see
Fig. 18b). However, while from Chris’ perspective
Alice sees the variable x evolving forward from time
step ℓto time step ℓ+1, Bob sees the variable x evolv-
ing backwards from time step ℓ+1 to time step ℓ(see
Fig. 18c). Since the physical process xℓ→xℓ+1 is the
same either way, for the ﬁrst-person observer Self
to consistently describe the transition xℓ→xℓ+1 we
must have an additional change in sign between Al-
ice’s and Bob’s descriptions, i.e. ∆1stPB = ∆3rdPA
(see Fig. 18c).
Notice that this additional minus
sign would not arise in the simulation interpretation
described in Sec. VI B 1 becuase the two arrows in
Fig. 18c will point in the same direction.
In summary, the ﬁrst-person changes in the state
of Alice and Bob, i.e.
when they are thought of
as components of the ﬁrst-person observer Self, are
given by:
∆1stPA = −∆3rdPB = −∆t[Js, PB],
(87)
∆1stPB = ∆3rdPA = ∆t[Js, PA].
(88)
Here we have used the notation Js instead of J to
emphasize that these equations are valid only when
there are no irreversible contributions, i.e. when J is
symmetric.
Equations (87) and (88) coincide with Eqs. (12)
and (13) when Ja = 0 as we are assuming here. Since
the initial states of Alice and Bob are equal (see
Eq. (86)), Eqs. (87) and (88) enforce that PB = P T
A
at all times (see Eqs. (10) and (11)). So, by reversing
the arguments in Sec. IV A we can see that Eqs. (87)
and (88), if written in terms of ρ = Ps + iPa, with
Ps = (PA + PB)/2 and Pa = (PA −PB)/2 the sym-
metric and anti-symmetric components of PA, are
equivalent to the von Neumann equation, Eq. (1),
restricted to real Hamiltonians because J is symmet-
ric. In the next section we discuss this derivation in
more detail in the context of the general case when
the environment can be out of equilibrium, so there
can also be irreversible contributions captured by Ja.
3.
Nonequilibrium environment and asymmetric kernels
If the environment is out of equilibrium, so J ̸= JT ,
there are irreversible contributions which are charac-
terized by the antisymmetric part Ja = (J −JT )/2
of the dynamical matrix J. In this case it is not true
anymore that changes in Bob’s state are equivalent
to changes in Alice’s state because we now have to
take into account also the asymmetric contributions
external to the self-referential observer Self. Since
Ja characterizes inﬂuences that are external to Self,
the ﬁrst-person change in the state of sub-observer
O ∈{A, B} due to Ja coincides with the third-person
change in the state of sub-observer O due to Ja, i.e.
as described by external observer Chris (see Figs. 18
and 19). (see Ref. [38] for a more compact and formal
discussion)
Let us make explicit in the ﬁrst- and third-person
changes of the state of sub-observer O,
∆1stPO = ∆1st
s PO + ∆1st
a PO,
(89)
∆3rdPO = ∆3rd
s
PO + ∆3rd
a PO,
(90)
the reversible and irreversible contributions due to Js
and Ja, respectively; these are denoted in Eqs. (89)
and (90), respectively, by subscripts ‘s’ and ‘a’. Ac-
cording to Eq. (85) the reversible and irreversible con-
tributions to the third-person changes are given re-
spectively by
∆3rd
s
PO = ∆t[Js, PO],
(91)
∆3rd
a PO = ∆t[Ja, PO].
(92)
Furthermore, as we said above, the ﬁrst- and third-
person changes associated to the irreversible contri-
butions due to Ja coincide because these are external
to the ﬁrst-person observer Self (see description of
Eqs. (101) and (102) below for another way to look
at this; see also Ref. [38]). So,
∆1st
a PO = ∆3rd
a PO = ∆t[Ja, PO].
(93)
On the other hand, the changes associated to the re-
versible contributions due to Js are internal to the
ﬁrst-person observer Self, so we can apply the anal-
ysis of Sec. VII B 2 to these. In other words, according


## Page 26


26
to the analysis of Sec. VII B 2 we have (cf. Eqs. (87)
and (88))
∆1st
s PA = −∆3rd
s
PB = −∆t[Js, PB],
(94)
∆1st
s PB = ∆3rd
s
PA = ∆t[Js, PA],
(95)
where the subscript ‘s’ indicates that the analysis ap-
plies only to the changes due to the reversible con-
tributions (see Eqs. (91) and (92)). Using Eq. (89)
we can write ∆1st
s PO = ∆1stPO −∆1st
a PO for sub-
observer O ∈{A, B}, which according to Eq. (93) is
equivalent to
∆1st
s PO = ∆1stPO −∆t[Ja, PO].
(96)
Replacing the left hand sides of Eqs. (94) and (95)
by the right hand side of Eq. (96) with O = A and
O = B, respectively, we obtain
∆1stPA −∆t[Ja, PA] = −∆t[Js, PB],
(97)
∆1stPB −∆t[Ja, PB] = ∆t[Js, PA],
(98)
where, again, the minus sign in the second equation
takes into account that if Alice observes the forward
process, Bob observes the backward (see Fig. 18).
These equations allows us to iteratively construct the
subjective states of Alice and Bob, and therefore of
Self.
Reorganizing Eqs. (97) and (98) we ﬁnally obtain
∆1stPA = ∆t[Ja, PA] −∆t[Js, PB],
(99)
∆1stPB = ∆t[Ja, PB] + ∆t[Js, PA],
(100)
which are equivalent to Eqs. (12) and (13) in
Sec. IV A, after taking the continuous time limit.
Again, the initial states PA,0 and PB,0 of Alice
and Bob, respectively, are diagonal and equal (see
Eq. (86)) since the observed initial state in an experi-
ment is common-knowledge ‘classical’ information to
all observers. So, as in Sec. VII B 2, Eqs. (99) and
(100) enforce the condition PA = P T
B , for all times
(see Eqs. (10) and (11)).
Another way to look at this is as follows. Imagine
that Chris in Fig. 8 observes Alice and Bob mov-
ing with velocity vA|C and vB|C.
However, Alice
and Bob see each other moving with relative veloci-
ties vA|B = vA|C −vC and vB|A = vB|C −vC, where
vC = (vA|C + vB|C)/2 is the extrinsic velocity that
Chris observes for the composed system of Alice and
Bob. In short, Alice and Bob can only see their rela-
tive motion (see Ref. [38] for a more formal discusion).
Similarly, we can write Eqs. (99) and (100) as
∆1stPA −∆t[Ja, PA] = −∆t[Js, PB],
(101)
∆1stPB −∆t[Ja, PB] = ∆t[Js, PA],
(102)
where we can interpret that we are removing the ex-
trinsic motion of the system because Alice and Bob
can only observe their relative motions.
Now, by adding and substracting Eqs. (99) and
(100), and dividing the so-obtained equations by half,
we obtain the equivalent equations (see Eqs. (8) and
(9))
∆1stPs = ∆t[Ja, Ps] + ∆t[Js, Pa],
(103)
∆1stPa = ∆t[Ja, Pa] −∆t[Js, Ps],
(104)
in terms of the matrices Ps = (PA + PB)/2 and
Pa = (PA−PB)/2, which are the symmetric and anti-
symmetric parts of PA, since PB = P T
A as we argued
above. Furthermore, by multiplying Eq. (104) by the
imaginary unit i, adding the resulting equation to
Eq. (103), and writing the so-obtained complex equa-
tion in terms of ρ = Ps +iPa and H = ℏJs +iℏJa, we
ﬁnally get Eq. (1) after taking the continuous limit.
VIII.
OCCAM’S RAZOR FAVORS THE
REVERSE PARADIGM
Apparently the analysis we have done here only
changes the interpretation of quantum theory and by
extension that of experiments too, as we will discuss
in Sec. IX. However, we will brieﬂy argue here that
Occam’s razor suggest we should favor the reverse
paradigm over the mainstream one (see Fig. 4). To
do so we explicitly state below some relevant assump-
tions made in the mainstream paradigm and contrast
them with the corresponding interpretation in the re-
verse paradigm presupposed in this work.
A.
Some relevant assumptions in the
mainstream paradigm
Let us now state some of the relevant assump-
tions implicitly made in the mainstream paradigm
(see Fig. 4):
(i) The world is fundamentally quantum for some
reason we do not yet understand.
(ii) The associated discreteness in the quantities
measured is characterized by a constant ℏ
whose origin we do not know yet.
(iii) Although in this paradigm we admit that our
body, brain, nervous system, etc, are made of
the same stuﬀthe rest of nature is made of,
e.g.
atoms, we implicitly assume that in an
experiment we can always neglect the physical
interactions associated to the experimenter.
(iv) Although every second of our lives we experi-
ence the world from a ﬁrst-person perspective,
our only perspective as far as we know, we as-
sume that we can somehow look at the world
from a supposedly objective third-person per-
spective, as if we were not part of it; or as if we


## Page 27


27
could somehow exit the universe and look at it
from the outside, as if we were abstract entities
devoid of matter.
Assumptions (i) and (ii) refer to aspects of quan-
tum theory that the mainstream paradigm still does
not have an answer to. Assumptions (iii) and (iv) are
inconsistent with our everyday experience; moreover,
assumption (iii) is inconsistent with the universality
expected from physics as a general theory of nature
that should therefore apply to everything, including
observers. In the next section we show how the re-
verse paradigm could help resolve all of these issues.
B.
Corresponding interpretation in the reverse
paradigm
Let us now see the potential explanations the re-
verse paradigm provides for the four assumptions im-
plicit in the mainstream paradigm stated above.
(i) The world can be modelled with classical prob-
ability; however, it appears to be quantum due
to the interactions associated to the observer’s
information processing.
(ii) Planck constant ℏcharacterizes the relevant in-
teractions taking place in the experimenter per-
forming the experiment, as we will discuss in
more detail in Sec. IX B.
(iii) Principle I asks us to treat consistently both
experiment and experimenter as physical sys-
tems and let the analysis alone tells us whether
the interactions associated to the experimenter
can indeed be neglected.
(iv) Principle II asks us to describe the world from
the only perspective we have, the ﬁrst-person
perspective. As a side result, Principle II has
the potential to explain the symplectic struc-
ture in the fundamental equations of physics,
as we will discuss in Sec. IX B.
Item (i) is consistent with our everyday experience
of the world as a classical system, and provides a po-
tential explanation as to why the world appears to
be quantum.
Item (ii) provides a potential expla-
nation for the origin of Planck constant ℏthat sug-
gests it can be determined from psychophysics ex-
periments, as we will argue in Sec. IX. These kind
of experiments are qualitatively diﬀerent to the kind
of experiments physicist typically use to estimate ℏ.
Items (iii) and (iv) are consistent with our everyday
experience; moreover, item (iii) is consistent with the
universality expected from a general theory of natural
phenomena, which should also apply to observers. So,
the reverse paradigm has both a higher explanatory
power and a higher consistency both with our human
experience and with itself, at least regarding the as-
sumptions here analyzed. We discuss in Sec. VIII C
how the reverse paradigm holds the potential to ex-
plain some characteristic quantum phenomena.
C.
Quantum foundations in reverse mode
We now sumarize how we implemented the Prin-
ciple I and Principle II and point out how some of
the conceptual diﬃculties of quantum theory become
less so from the perspective oﬀered in this work.
Principle I implies that experiments can be con-
ceived as circular interactions (see Figs. 6, 11, 17).
In other words, the linear chain of cause-eﬀect rela-
tionships linking a well-deﬁned initial state to a well-
deﬁned ﬁnal state, which we traditionally model ex-
periments with, has to be closed into a circle. The
additional link that turns the chain into a circle could
be understood as an eﬀective interaction summariz-
ing the myriad of physical interactions supporting the
observer’s information processing and control. Collo-
quially, we might say that this was a missing link to
quantum theory.
This principle alone allowed us to derive the formal-
ism of Euclidean or imaginary-time quantum mechan-
ics, which already leads to quantum-like phenomena
such as interference, superposition, entanglement, an
uncertainty principle, etc. (see e.g. Ref. [92]). In-
deed, Principle I is the one speciﬁc to quantum the-
ory, so it already has several conceptual implications
that we now describe.
First, while it is possible to identify the two ex-
treme nodes of a chain graph, i.e.
its leaves, with
an initial state completely independent of any past
interactions and a ﬁnal state completely independent
of any future interactions (see vi and vf in Fig. 17
e), this is not so in a circular graph.
Indeed, un-
like a chain graph, a circular graph has no intrinsic
distinctions between initial or ﬁnal nodes and those
that should be in between, i.e. any node has an in-
teraction with a node in the ‘past’ and a node in the
‘future’ (see Fig. 17d). This already suggests that we
might run into diﬃculties when attempting to asso-
ciate well-deﬁned states to the system at any given
time, providing a potential explanation for quantum
superpositions and (constructive) interference.
Second, the additional link summarizing the inter-
actions associated to the observer can be interpreted
as an interaction between ‘past’ and ‘future’ (e.g. the
green links in Fig. 11 or the combination of the red,
blue, and green links in Fig. 17).
In other words,
the circular interaction associated to an experiment
could be interpreted as a feedback mechanism that
eﬀectively introduce an interaction between the ini-
tial state prepared and the ﬁnal state measured by
the observer.
An observer that does not consider
herself as part of the experimental setup could inter-


## Page 28


28
pret this eﬀective interaction between ‘past’ and ‘fu-
ture’ as retrocausality. This makes retrocausality as
a plausible and intuitive explanation for Bell inequal-
ities, one of the more problematic conceptual aspects
of quantum theory. Alternatively, the variables asso-
ciated to the observer’s representation of the initial
and ﬁnal state of the system would be interpreted
by an observer that does not consider herself as part
of the experimental setup as hidden variables which
interact non-locally.
Third, it is natural to expect that the speciﬁcs of
the architecture of the observer, whether human or
mechanic, determines the energy scale associated to
the observer’s physical interactions. Any phenomena
whose energy is below such energy scale would be es-
sentially unable to generate a percept.
So, even if
energy might be fundamentally continuous it would
still appears as discrete to the observer due to the
threshold energy required to support all the physical
interactions underlying the generation of a percept.
This suggests a possible explanation for the quanti-
zation of energy and it is indeed consistent with psy-
chophysics experiments estimating the energetic as-
pects of conscious access, as we describe in Sec. IX C.
Fourth, although a probabilistic model with pair-
wise interactions on a circular graph does not neces-
sarily lead to a ﬁrst-order Markov process, but rather
to a Bernstein process (see Eq. (65)), we can still de-
ﬁne a Markovian-like update rule if we use probabil-
ity matrices rather than vectors (see Eq. (75)). The
oﬀ-diagonal elements of the probability matrix en-
code dynamical information necessary to obtain the
probability matrix at a given time from that from
the previous time. This suggests the imaginary-time
phase of the imaginary-time quantum state encodes
dynamical information since it characterizes the oﬀ-
diagonal elements of the probability matrix. Further-
more, the diagonal elements of the probability matrix
yield the probability of observing the associated out-
come, which could explain the origin of the Born rule.
Principle II leads us to ask what is the architec-
ture of agents with a ﬁrst-person perspective?
To
implement this principles we have made two assump-
tions: (i) such agents require self-modeling capabili-
ties; (ii) to avoid the inﬁnite regress associated to the
self-referential problem of describing the world from
within, such self-referential agents are composed of
two complementary systems that essentially model
each other (see Figs. 18 and 19; cf.
Fig. 8).
This
latter assumption builds on the insights of the re-
cursion theorem of computer science, which implies
that the architecture of a self-printing program, for
instance, is composed of two sub-programs that es-
sentially print each other (see Figs. 12, 14, 15 and
Secs. C and VII A). In particular, this leads us to
predict that the neural correlates of the experience
of being a self are composed of two complementary
sub-systems that observe each other; the division of
brains into hemispheres in healthy individuals can be
a reﬂection of this principle (see Fig. 20).
This principle allowed us to turn imaginary-time
quantum mechanics into its real-time counterpart, ef-
fectively implementing a Wick rotation. This princi-
ple is related to the symplectic structure of quantum
theory, and as such it is expected to apply beyond
it. It also has conceptual implications that we now
discuss.
First, we expect that at the root of complemen-
tarity lies the fact that self-referential observers are
composed of two sub-observers that play complemen-
tary roles as both observing subjects and observed
objects. This is in line with Bohr’s observation [36]
that complementarity appears to arise naturally in
psychology where both the objects of perception and
the perceiving subject belong to ‘our mental content’.
Second, the implementation of the ﬁrst-person ob-
server required by Principle II via the composi-
tion of two sub-observers essentially require that we
change the single real matrix equation that encode
Principle I into a pair of real matrix equations (see
Eqs. (99) and (100)).
Furthermore, the two sub-
observers observe the external phenomena in reversed
directions, which leads to a negative sign in one of the
matrix equations (see Fig. 18). Such negative sign
could explain the phenomenon of destructive inter-
ference as it holds the potential to reduce the values
of the diagonal elements and introduce negative oﬀ-
diagonal elements to the probability matrices.
Third, the implementation of Principle I natu-
rally led to the imaginary-time version of the Born
rule (see Sec. VI C 1), and Principle II essentially in-
corporated the implications of Principle I into the
ﬁrst-person perspective (see Sec. VII B). This in a
sense reverse the traditional reasoning that leads to
the so-called measurement problem, i.e.
the prob-
lem of explaining why if nature is fundamentally de-
scribed by a ‘wave function’ that evolves unitarily,
at the time of measurement such ‘wave function col-
lapses’ via the Born rule, breaking the fundamental
unitarity of quantum evolution. Our starting point,
instead, was a standard classical probabilistic model
on a circular graph that implemented Principle I
and naturally led to the imaginary-time version of the
Born rule, as a useful artifact to describe the update
rule. Principle II allowed us to eﬀectively perform a
Wick rotation to obtain the unitary evolution of the
quantum state. In short, ﬁrst Principle I naturally
leads to non-commutativy and the Born rule, and the
unitarity emerges from the combination of Principle
I and Principle II. In this sense, the measurement
problem is not a problem in this approach.
Remark 1: Even if an observer can build a model
of itself on its physical ‘hardware’, it is not expected
to access the very physical processes that allow the
construction of its self-model. This is similar to the


## Page 29


29
situation with a Turing machine that can print a de-
scription of itself but cannot access its inner work-
ing mechanisms to evaluate whether it will halt on a
certain input or not [116, 123]. In this sense, such
physical interactions are an intrinsic indeterminacy.
This seems to be related to Metzinger’s [30] concept
of transparency mentioned in the introducton. Para-
phrasing Deacon [74]: We are a hole, an absence in
the universe; nature is incomplete in terms of subject-
object relationships because the observing subject
cannot fully observe itself, yet it is completed via hu-
man experience because the subject can indeed fully
experience itself.
Remark 2: From a third-person perspective the link
that turns the linear chain of cause-eﬀect relation-
ships into a circle is just a concept summarizing the
myriad interactions going on in the observer’s brain
and body. From a ﬁrst-person perspective, instead,
such interactions summarized by a single link trans-
late into our complex human experience. Since the
eﬀective interaction represented by such a link con-
cern human experience, we can in principle access
them from a ﬁrst-person perspective, not in a subject-
object relationship but from direct experience. This
is analogous to the fact that we cannot directly see
our own eye, i.e. using our eye itself, but we can in-
deed experience its existence—e.g. it would be clear
to us when our eye has stopped working even if we
cannot directly see the damaged eye as an object of
observation. As we shall discuss in Sec. X, the ﬁrst-
person methods of contemplative traditions may turn
out to be a powerful tool to carry out this exploration.
IX.
QUANTUMNESS AND
CONSCIOUSNESS
A.
Consciousness as a rigorous scientiﬁc subject
Dehaene, one of the leading scientist on the mod-
ern approach to consciousness, pointed out that for a
long time the subject of consciousness was considered
a taboo that lied ‘outside the boundaries of normal
science’ [21] (page 7; see also Ref. [124]). There was a
strong reason for this, of course, as it is not clear yet
even how to clearly deﬁne the concept of conscious-
ness. Perhaps because of this ambiguity, attempts to
ﬁnd links between quantum theory and consciousness
have hardly reached mainstream physics debates. To-
day things are radically changing, though, thanks in
part to the eﬀorts of Nobel laureate Francis Crick
and his collaborator Christof Koch:
consciousness
has become a hot scientiﬁc research subject (see e.g.
Ref. [20] for a recent review).
In Appendix B we summarize some relevant sci-
entiﬁc results on consciousness for the reader that
may not be familiar. In Appendix B 1 we summa-
rize some relevant results concerning the information-
processing mechanisms underlying conscious percep-
tion, which is considered as one of the ‘easy’ problems
of consciousness [20, 21, 124]. These features do not
address the so-called ‘hard’ problem of consciousness,
which is closely related to our human experience. In
Appendix B 2 we brieﬂy discuss recent developments
on the latter, specially Metzinger’s self-model theory
of subjectivity mentioned in the introduction [30, 31]
(see also chapter 9 of Ref. [32] for a review; for a
short introduction to the most central ideas see Met-
zinger’s talk ‘The transparent avatar in your brain’ at
TEDxBarcelona).
B.
The message of the quantum: observers are
physical
Here we discuss in more detail the idea put forward
in Ref. [37] that Planck constant can be estimated
from psychophysics experiments that in a sense esti-
mate the energetics assocaited to conscious access.
We have discussed in previous sections how the
formalism of quantum theory can be understood as
encoding Principle I, i.e. taking into account the
physical interactions associated to the observer (see
Secs. III A and VI), and Principle II, i.e. tackling
the self-referential problem of representing the world
from a ﬁrst-person perspective (see Secs. III B and
VII). Now, Principle I leads to a non-commutative
Markovian update rule (see Eq. (75)), while Prin-
ciple II builds on the non-commutative equation
obtained via Principle I to get a pair of non-
commutative equations (see Eqs. (99) and (100)) that
can be encoded on a single complex equation deﬁned
on Hermitean matrices, i.e. the von Neumann equa-
tion.
So, we can say that Principle I essentially leads
to non-commutativity, while Principle II essentially
leads to complex numbers. However, complex num-
bers are related to the symplectic structure of fun-
damental physical equations. For instance, it is well-
known that we can write Hamilton equations
˙x = ∂e
H(x, p)
∂p
,
and
˙p = −∂e
H(x, p)
∂x
,
(105)
in terms of complex variables z = (x + ip)/
√
2 and
its conjugate z∗as
˙z = −i∂H(z, z∗)
∂z∗
,
(106)
where
H(z, z∗) = e
H
z + z∗
√
2
, z −z∗
i
√
2

;
(107)
notice that e
H in the right hand side of Eq. (107) is the
original Hamiltonian function in Eq. (105), as empha-
sized by the tilde. So Principle II is expected to ap-
ply more generally beyond quantum theory. Indeed,


## Page 30


30
as we will discuss in more detail elsewhere, the sym-
plectic structure of fundamental physical equations
can be understood as emerging from self-reference.
In contrast, non-commutativity is unique to quan-
tum theory.
Indeed, as discussed in Ref. [5] when
we restrict all density matrices to be diagonal the
quantum dynamics become commutative and coin-
cide with classical Markovian dynamics. Therefore,
according to Principle I the unique aspect of quan-
tum theory that distinguishes it from classical theo-
ries is the fact that the observer is physical.
Since quantum theory is characterized by Planck
constant ℏ, it is natural to expect that ℏis related to
the physical interactions associated to the processing
of information by the observer. So, from this perspec-
tive the classical theory is expected to yield accurate
predictions when the energy of the interactions as-
sociated to the observer is much smaller than that
related to the observed system.
This is consistent
with the observation that if we neglect the link that
summarizes the physical processes associated to the
observer, we recover standard Markov processes on
a chain (see e.g. Figs. 17d,e). In this sense, there
is not absolute notion of ‘micro’: something is small
relative [3] to an observer in precisely this way.
Remark: In the approach we have introduced in
Sec. IV (see also Appendix D) we can obtain Hamilto-
nian functions (see Eqs. (21) and (D26)) which coin-
cide (up to a sign) with the Wick rotation ϵ →−iϵ of
the corresponding Lagrangian. More precisely, in the
continuous limit ϵ →0 we can write (see Sec. V A)
SE =
n−1
X
ℓ=1
H(xℓ, xℓ+1)ϵ
−−−→
ϵ→0
Z tf
ti
H(x, ˙x)dt,
(108)
where t
=
ℓϵ,
˙x
=
limϵ→0(xℓ+1 −xℓ)/ϵ, and
ti and tf are the initial and ﬁnal times, respec-
tively; for instance, if L = m ˙x2/2 −V (x) then
H(x, ˙x) = m ˙x2/2 + V (x). Since the graphical model
that represents the observer interacting with the ex-
perimental system has the topology of a circle, we
need to condition on two variables (see Fig. 11), say
initial and ﬁnal states: xi = x(ti) and xf = x(tf), or
initial position xi and velocity ˙xi, to turn the circle
into a chain and analyze it in the traditional way.
So, the physicality of the observer naturally induces
the need to condition on two variables instead of one,
as it would be the case of a Markov process on the
position x.
Now, the most probable path (see Eq. (35)) would
be the one that minimizes the Euclidean action SE
condition to the initial and ﬁnal states remain ﬁxed.
It is well-known that this process leads to Euler-
Lagrange equations, here for an eﬀective Lagrangian
eL = H
d
dt
∂H
∂˙x = ∂H
∂x ,
(109)
which
in
turn
are
equivalent
to
the
Newton
equations in imaginary time.
For instance,
if
H(x, ˙x) = m ˙x2/2 + V (x) Eq. (109) becomes
¨x = ∂V
∂x ,
(110)
which is Newton equation in an inverted potential
−V . If we now invert back the Wick rotation, i.e.
we do t →it, we get ¨x →−¨x, which restores the
correct sign of the potential in Eq. (110). Although
this analysis already leads to a symplectic structure,
such symplectic structure is not the correct one. To
obtain the correct symplectic structure we need to
go through the self-referential process of representing
the world from within, even in the classical world.
In conclusion, the physicality of the observer alone
already implies the need of second-order diﬀerential
equations instead of the most parsimonious ﬁrst-order
diﬀerential equations.
C.
Planck constant from psychophysics
experiments
1.
General considerations
The discussion in the previous section suggests that
Planck constant can be derived from experiments
that directly or indirectly measure the interactions
associated to the observer. Now, as far as we know,
science happens at the conscious level, e.g.
scien-
tist always report their ﬁndings via research articles
or conference talks. This suggests that the relevant
physical processes taking place in the observer are
those associated to conscious information processing.
So, as we will argue here, psychophysics experiments
that estimate the energy requirements for conscious
access are strong candidates for measuring Planck
constant.
Unfortunately, we are aware of only one experi-
mental work [125] that explicitly addresses the en-
ergy requirements for conscious perception. So, there
is an opportunity for experimental physicists to de-
sign more careful experiments to test this prediction.
We will show here that available experiments suggest
it is correct. Although the experiment in Ref. [125]
studies monkeys, not humans, the authors argue that
‘similar psychophysical results [...] obtained in mon-
key and human for all three sensory stimuli studied
suggest that the cellular mechanisms underlying per-
ception are similar in the two species’ [125] (see dis-
cussion section therein). Since we will use this ex-
periment only to provide an estimate of the order of
magnitude of Planck constant, we will assume that


## Page 31


31
the results in Ref. [125] can indeed be extrapolated
to humans. A drawback, though, is that the authors
do not report actual absolute values, but only values
relative to those of unconscious information process-
ing. More precisely, the authors of Ref. [125] provide
evidence that the energy required to transition from
unconscious information processing to conscious per-
ception is about 6% of the energy required for un-
conscious processing alone (see below). However, as
we argued in Ref. [37], we can combine the results re-
ported in Ref. [125] with the results from experiments
reported in Ref. [126], which estimated the sensibil-
ity of the human eye using a classical source of light,
to provide an estimate of the order of magnitude of
Planck constant.
Moreover, we will also discuss in more detail the
idea put forward in Ref. [37], that a more recent ex-
periment [43], which uses a quantum source of light to
show that humans can detect one single photon with
a probability of 0.516 ± 0.010, can be reinterpreted
in the reverse paradigm (see Fig. 4) as an experiment
that directly measures the actual value of Planck con-
stant. Although the experimental results reported in
Ref. [43] has been recently challenged [127], we will
argue that our approach allows us to predict that once
such a debate is settled, the ﬁnal conclusion should be
that indeed humans can consciously perceive a single
photon. This is a precise theoretical prediction that
contrasts with the current motivation for these stud-
ies, which is essentially the curiosity on whether a
human can detect a single photon. Our approach al-
lows us to predict that humans must be able to do
so.
2.
‘Classical’ pshycophysics experiments
Experiment 1 (Visual motion detection):
To begin,
let us brieﬂy describe the experiment performed by
Sch¨olvinck, Howarth, and Attwell (SHA) [125] (see
‘Experiment 1’ in Fig. 21). While SHA investigated
three diﬀerent information pathways, i.e. visual, so-
matosensory, and auditory, we will only focus on the
visual part. In the SHA experiment, monkeys were
presented an array of moving dot stimuli (see Fig. 21
top), wherein a certain percentage C of dots, referred
to as ‘coherence of motion’, moved in the same di-
rection, while the remainig dots moved in random
directions. The monkeys were tasked to decide what
the general direction of motion was. The objective of
this experiment was to estimate the energy needed for
visual processing of dot stimuli moving suﬃciently co-
herently to generate a percept, relative to the energy
needed for processing the same number of dots mov-
ing randomly such that no percept of general move-
ment was generated. Since this experiment focuses on
the perception of movement, the intensity of the dot
stimuli was well above the visibility threshold. This
contrasts with the other two experiments [43, 126]
we will described below, whose focus is precisely on
identifying the visibility threshold of humans.
Figure 21 (bottom) sketches the qualitative form
of the so-called psychometric curve for visual motion
(see Fig.
2d in Ref. [125] for the actual curve de-
termined from the SHA experiment).
The psycho-
metric curve gives the probability p(C) that subjects
report seeing the correct direction of motion (verti-
cal axis) as a funtion of the coherence of motion C
(top horizontal axis), i.e. the percentage of dots that
moved in the speciﬁed direction. The authors speci-
ﬁed the threshold of detection CSHA to be the value
of coherence for which the probability for the mon-
keys to report the correct direction of motion was
p(CSHA) = 0.82. The choice of threshold is somehow
arbitrary and is diﬀerent for the three experiments
we will discuss in this section. This is something we
should take into account in the estimation of Planck
constant.
An ideal experiment would decrease the coherence
of motion C with a resolution and number of trials
large enough that it is possible to identify the min-
imum value Cmin just before subjects report a ran-
dom guess. The value Cmin is more precisely deﬁned
as the value of the coherence of motion such that
the probability to report the correct response satisfy
p(C) = 0.5 for C < Cmin and p(Cmin) = pmin. This
includes the case of a continuous transition, where
Cmin = 0 and pmin = 0.5. However, a discontinuous
jump with Cmin > 0 and pmin > 0.5 is more consistent
with experimental and theoretical studies suggesting
that conscious perception is all or none [128] and
that the transition from unconscious to conscious per-
ception is analogous to a discontinuous phase transi-
tion [129, 130] (see also Ref. [21], page 184). More-
over, we will argue below that the experiment by
Tinsley et al. [43] can also be interpreted in this way.
Such an ideal situation is hard to meet in practice,
though , so scientist usually deﬁne a suitable thresh-
old such as CSHA in the SHA experiment [125].
We will refer to the region where the discontinuous
jump takes place as ‘quantum’ (see Fig. 21 bottom)
for reasons we will describe later on when we discuss
Tinsley et al. experiment [43]; we will therefore re-
fer to the other region as ‘classical’ (see Fig. 21). In
particular, experiments such as the SHA experiment,
which do not have a resolution high enough to ob-
serve the region where a discrete jump is expected to
happen, allow us to explore only the ‘classical’ region.
As we will discuss in Sec. IX C 3, experiments such as
the experiment by Tinsley et al [43], instead, allow
us to explore the ‘quantum’ region.
Experiment 2 (Determination of the visibility thresh-
old with classical light): In 1942 Hecht, Schlaer, and
Pirenne (HSP) reported a set of landmark experi-
ments [126] intended to measure the threshold energy


## Page 32


32
for vision (see ‘Experiment 2’ in Fig. 21 bottom). In
the HSP experiment human subjects were exposed to
green light of frequency ν = 5.88 × 1014 Hz, whose
intensity was gradually decreased until te subjects re-
ported a random guess. In Fig. 21 (bottom) we sketch
the qualitative shape of the psychometric curve (cf.
Fig.
7 in Ref. [126]) that measure the probability
p(E) for the human subjects to report seeing a ﬂash
of light (vertical axis) as a function of the energy E at
the cornea (bottom horizontal axis). The relatively
low resolution of the experiment did not allow to re-
solve the ‘quanutm’ region of the psychometric curve,
so an arbitrary threshold EHSP was deﬁned such that
p(EHSP) = 0.6, diﬀerent from the choice of threshold
in the SHA experiment. According to the results of
the HSP experiment, EHSP was in the range
2.1 × 10−17J ≲EHSP ≲5.7 × 10−17J.
(111)
(See Table II in Ref. [126] for the values in units of
10−10 ergs; notice there is a typo therein.)
The authors of the HSP experiment interpret it
within the current mainstream paradigm in physics
(see Sec. VIII A and Fig. 4), i.e. they assume that
the energy of light is objectively quantized in pho-
tons for some reason we do not yet understand, and
ask ‘what is the minium number of photons that hu-
mans can report?’. Since the energy of a photon is
given by hν, the values for EHSP represent between 54
and 148 photons. However, HSP argued that at least
three corrections should be applied to those values:
reﬂection from the cornea, losses that occur between
the cornea and the retina, and energy absorbed by
the retina. By also taking into account the Poisson
statistics of the classical source of light they used,
HSP estimated that about 5 to 8 photons are required
at the retina to generate a visual perception.
Estimation of Planck constant’s order of magnitude:
However,
the reverse paradigm (see Sec. VIII B
and Fig. 4) presupposed in this work implies a
completely diﬀerent interpretation:
the energy of
light can in principle be continuous, as any classical
energy source, but due to the physical interactions
associated to the observer it looks quantized in
photons. So, from this perspective we can combine
HSP and SHA experiments to ask rather the question
‘what is the minimum amount of energy required for
humans to transition from unconscious processing to
conscious perception, i.e. what is the value of Emin
in Fig. 21 (bottom)?’.
Let us ﬁrst analyze the SHA experiment on mon-
keys’ visual motion detection. Let E0 and ESHA be,
respectively, the energy consumed by the relevant ﬁr-
ing neurons of a generic monkey when the dots are
moving at random, i.e.
C = 0, and at the SHA
coherence threshold CSHA, i.e.
when monkeys re-
port the correct direction of motion with a proba-
bility p(CSHA) = 0.82. According to the results re-
ported by SHA we have (ESHA −E0)/E0 ≈0.06 (see
paragraph following Eq. (2) in Ref. [125]). Writing
E0 = ESHA −(ESHA −E0) and doing some algebra
yields
(ESHA −E0) ≈0.04ESHA.
(112)
According to SHA E0 and ESHA are the energies cor-
responding to mean ﬁring rates of about 20 Hz and
21.4 Hz, respectively. While it is not clear to us how
to translate these numbers into the actual values of
energy, we will now combine this analysis with the
HSP experiment to obtain some estimates.
In Ref. [37] we used the minimum value of energy
measured by HSP (see Eq. (111)) as an estimate of
EHSP ≈2.1 × 10−17 J to have an estimate of Planck
constant. Here we will rather use the average value in
the range determined by HSP, i.e. EHSP ≈3.9×10−17
J since it is a better estimate of the typical value.
Let Eav be the amount of energy required for un-
conscious processing of electromagnetic stimuli, e.g.
for feature extraction, which is the analogous of E0
in the SHA experiment; although Eav was not mea-
sured in the HSP experiment, we do not require it
here. Assuming the results of the SHA experiment
in Eq. (112) can be extrapolated to the HSP ex-
periment, and neglecting the fact that the thresh-
olds in both experiments were deﬁned diﬀerently, we
have EHSP −Eav ≈0.04EHSP ≈1.6 × 10−18 J, which
is about four times the energy of the correspond-
ing photon Ephoton = hν ≈3.9 × 10−19 J. Since
Emin < EHPS, this implies that Emin in Fig. 21 (bot-
tom) is less than the energy associated to a few pho-
tons. As we will discuss in the next section, the ex-
periment of Tinsley et al. [43] provides evidence that
Emin is indeed the energy associated to a single pho-
ton.
3.
‘Quantum’ psychophysics experiments
By using a quantum source of light to expose hu-
man subjects to single photons and carrying out over
3 × 104 trials to collect enough statistics, Tinsley et
al. [43] signiﬁcantly improved on the HSP experi-
ment and determined that humans can indeed de-
tect one single photon with a probability of pmin =
0.516 ± 0.010 (however, see Ref. [127]).
Although
Tinsley et al.
did some more reﬁned statistics by
asking the human subjects about the level of conﬁ-
dence in their responses, we will focus on the simpler
experiment that request only one bit of information
as we expect that simpler is more fundamental.
Like HSP, Tinsley et al.
also interpret their ex-
periment within the current mainstream paradigm in
physics (see Fig. 4), i.e. Tinsley et al. [43] assume that
the energy of light is objectively quantized in photons
for some reason we do not yet understand, and ask
‘can humans perceive a single photon?’. From this


## Page 33


33
perspective we can interpret Emin in Fig. (21) (bot-
tom) as the fundamental minimum amount of energy
of green light that can exists in nature, i.e. any non-
zero value of energy that is below Emin simply does
not exist. In other words, in this paradigm we already
know Emin = hν. By focusing directly on estimating
pmin = p(Emin) in Fig. 21 (bottom), Tinsley et al. ad-
dressed what we called the ‘quantum’ regime of this
psychophysical experiment, while HSP addressed the
‘classical’ regime.
Estimation of Planck constant: However, the reverse
paradigm (see Fig. 4) presupposed in this work again
implies a completely diﬀerent interpretation: as we
said, in this paradigm the energy of light can in prin-
ciple be continuous, as any classical energy source,
but due to the physical interactions associated to the
observer it looks quantized in photons. So, from this
perspective we can turn Tinsley et al. question into
‘what is the minimum amount of (possibly continu-
ous) energy humans can perceive?’ In this case there
are no intrinsically forbidden energies as in the main-
stream paradigm interpretation.
Instead, we could imagine an experiment that
starts with light with energy Elarge large enough for
the human subjects to report seeing it with a proba-
bility close to 1 (see Fig. 21 bottom). Afterwards the
experimenters could progressively reduce the energy
of light, while constantly asking the human subjects
whether they still see the pulses of light.
The ex-
perimenters can decrease the energy until the human
subjects report seeing the pulses of light with prob-
ability 0.5, i.e. a random guess. The value Emin of
the energy just before reaching a random guess would
correspond to the minimum amount of energy of light
we can consciously percieve. In Tinsley et al. exper-
iment we have pmin = p(Emin) = 0.516 ± 0.010.
Of course, all the evidence we have from more than
a century of quantum experiments suggests that such
a value is the value we associate to a photon. How-
ever, the interpretation is completely diﬀerent. Any
value of energy below Emin could objectively exist,
yet its energy is below the value required to launch
the physical processes associated to conscious access.
Combining the predictions of quantum theory, whose
formalism we have derived here, with the so obtained
value of Emin, we could infer the precise value of
Planck constant. In the reverse paradigm, it is not
that the eye is so eﬃcient that it can detect a sin-
gle photon, but that the very deﬁnition of photon
is the minimum amount of light we can consciously
perceive. A possible criticism of this idea is that we
cannot directly observe X-rays, for instance, yet they
are also quantized. However, as illustrated in Fig. 6,
even in experiments with X-rays the observer is part
of the experimental set up; the interactions associated
to the observer can be considered as the bottleneck
of the whole process.
Notice that no other theory
predicts that humans should be able to perceive a
single photon; up to now this question has been an
experimental curiosity not guided by any theory [43].
D.
Self-reference and the global architecture of
self-aware systems and the self
There is active research in understanding the neu-
ral correlates of the self.
Studies focusing on self-
referential processing, i.e.
on the ability to think
about oneself, have identiﬁed regions located in the
midline of the human cerebral cortex to be cru-
cial for self-speciﬁc processing [131–135], which typi-
cally involves both brain hemispheres. It has been
argued [135, 136], however, that this type of self-
referential processing is related to the experience of
ourselves as a passive obsject, i.e. a ‘me’, and that the
experience of ourselves as active subjects, i.e. as an
‘I’, is more closely related to sensorimotor processes,
i.e. processes that integrate sensory information or
input with a related motor response or output in the
central nervous system [1].
A possible account of the sensorimotor perspective
is that humans have internal models which can be of
two types [137]: (i) forward models, which mimic the
causal ﬂow of a process by predicting its next state,
given the current state and the motor command; and
(ii) inverse models, which invert the causal ﬂow by
estimating the motor command that caused a partic-
ular state transition. So, an inverse model allows an
agent to estimate the motor command that will lead
to a desired sensory experience, much as in the ideo-
motor view [103] (see Sec. VI B 2). On the other hand,
a forward model allows an agent to predict which
would be the sensory consequences of implementing a
given motor command. These type of mechanism can
in principle allow for an intrinsic self/non-self distinc-
tion, i.e. a distinction made by the agent itself rather
than by another external agent. Let us use Christoﬀ
et al. [136] words:


## Page 34


34
“An organism needs to be able to distinguish between
sensory changes arising from its own motor actions (self)
and sensory changes arising from the environment (non-
self).
The central nervous system (CNS) distinguishes
the two by systematically relating the eﬀerent signals
(motor commands) for the production of an action (e.g.
eye, head or hand movements) to the aﬀerent (sensory)
signals arising from the execution of that action (e.g. the
ﬂow of visual or haptic sensory feedback). [... T]he ba-
sic mechanism of this integration is a comparator that
compares a copy of the motor command (information
about the action executed) with the sensory reaﬀerence
(information about the sensory modiﬁcations owing to
the action). Through such a mechanism, the organism
can register that it has executed a given movement, and
it can use this information to process the resulting sen-
sory reaﬀerence. The crucial point for our purposes is
that reaﬀerence is self-speciﬁc, because it is intrinsically
related to the agents own action (there is no such thing as
a non-self-speciﬁc reaﬀerence). Thus, by relating eﬀerent
signals to their aﬀerent consequences, the CNS marks the
diﬀerence between self-speciﬁc (reaﬀerent) and non-self-
speciﬁc (exaﬀerent) information in the perception-action
cycle.
In this way, the CNS implements a functional
self/non-self distinction that implicitly speciﬁes the self
as the perceiving subject and agent. [...]
“For example, consider the motor act of biting a lemon
and the resulting taste. This experience is characterized
by (i) a speciﬁc content (lemon, not chocolate); (ii) a spe-
ciﬁc mode of presentation (tasting, not seeing); and (iii) a
speciﬁc perspective (my experience of tasting). The pro-
cess of relating an eﬀerence (the biting) to a reaﬀerence
(the resulting taste of acidity) is what allows the percep-
tion to be characterized not only by a given content (the
acidity) but also by a self-speciﬁc perspective (I am the
one experiencing the acidity of the lemon juice)”
Christoﬀet al., in Ref. [136].
The idea that the notion of self is related to a for-
ward and an inverse model appears to be consistent
with the architecture of self-referential observers (see
Fig. 18), a subject that we plan to explore further in
the future.
There have also been explorations [138, 139] on
how the free energy principle [140] underlying the
framework of active learning could implement Met-
zinger’s notion of a self-model [29–31, 141]. As we
mentioned in the introduction, the idea that humans
rely on a self-model appears to be supported by ex-
periments that study the experience of ownership of
body parts and of the full body, such as the rubber
hand [25, 26] and full-body illusions [27–29, 142, 143]
respectively.
Metzinger [30] and Blanke [29] argue
that there are three necessary aspects underlying
the simplest notion of self, or self-consciousness: (i)
self-identiﬁcation, i.e.
the identiﬁcation of an or-
ganism with a global body representation; (ii) self-
location, i.e. the volume in space usually localized
within the represented body boundaries; and (iii) the
ﬁrst-person perspective. According to Metzinger and
Blanke, this notion of self arises when the brain en-
codes the origin of the ﬁrst-person perspective from
within a spatial frame of reference (i.e. self-location)
associated with self-identiﬁcation [142].
Similar to what happen with self-referential pro-
cessing, the three aspects mentioned above, i.e. self-
identiﬁcation, self-location, and the ﬁrst-person per-
spective, have been associated to neural activity in a
few brain regions that involve both hemispheres [142].
This appears to be consistent with the architecture
of self-referential observers as composed of two sub-
systems, in this case the two brain hemispheres and
perhaps also the left and right neural networks that
run through the spinal cord (see Fig. 20). In other
words, similar to what happens with self-replicating
molecules (e.g. the DNA) and self-printing machines,
self-reference imposes a global organizing principle for
a neural system to refer to itself: it must be com-
posed of two complementary sub-systems, much as
the global organization of the human central nervous
system.
Indeed, since Turing machines can be realized by
recurrent neural networks [144] (chapter 10) with ra-
tional weights [145–148], the results associated to self-
reference, such as the recursion theorem and the halt-
ing problem, can in principle be extended to recurrent
neural networks [147, 149]. For instance, consider the
recurrent neural network with M external input sig-
nals and N neurons deﬁned by the equation [146, 147]
xi(t + 1) = σ


N
X
j=1
aijxj(t) +
M
X
j=1
bijuj(t) + ci

,
(113)
where uj are the external inputs, xj are the neurons’
activations, aij, bij, ci are the parameters specifying
the network.
σ(x) =





0 if x < 0,
x if 0 ≤x ≤1,
1 if x > 1.
(114)
As part of the description of the network, a subset
of p < N neurons is singled out as the output neu-
rons which communicate the output of the network
to the environment. Although the output values can
take values in [0, 1] they can be constrained to binary
values only [147].
Here we are only interested in the formal properties
of these networks. So, let Nθ(x; u) denote a generic
reccurrent neural network deﬁned by the vector of ex-
ternal inputs u, the vector of neuron’s activations x,
and the description of the network θ which contains
the parameters of the networks and the indexes of
the output neurons. So, here Nθ is to θ what a Tur-
ing machine TM is to its description “TM” (see Ap-
pendix C). Since recurrent neural networks (with ra-
tional parameters) are equivalent to Turing machines,
we can in principle build a network N Self
θ
that out-
puts its own description θ. According to the recursion
theorem (see Appendix C), such network should be


## Page 35


35
composed of two neural networks N Alice
α
and N Bob
β
that essentially output a description of each other.
This therefore suggests that the neural architec-
ture of a system with the ability to refer to itself
should be composed of two complementary systems
that eﬀectively run in reverse directions. This prin-
ciple might help explain why the process of global
ignition underlying conscious access seems to be as-
sociated to the simultaneous presence of feedforward
and feedback propagations throughout the brain (see
e.g. Fig. 1b in Ref. [150] and the ﬁgure in Ref. [151];
see also Ref. [152]). It seems also natural to hypoth-
esize that the global architecture of the central ner-
vous system of humans and other animals, i.e. the
division of the brain in two hemispheres and the left
and right neural networks running through the spinal
cord (see Fi.g 20), may be the result of this con-
straint to implement self-reference.
Indeed, as we
pointed out above, the neural correlates associated
to self-referential processing and to the experience
of body ownership usually involve both brain hemi-
spheres [27–29, 131–135, 142, 143] (see also Fig. 4 in
Ref. [20]).
These two possibilities are not necessarily contra-
dictory, as we could expect that a neural system may
implement such architectural constraint at diﬀerent
scales to enhance its resilience to potential damage
of parts of its infrastructure, or to implement con-
sciousness or the experience of being a self associ-
ated to processes at diﬀerent scales. Although this
may seem to contradict the decades-old theory stat-
ing that split-brain patients, i.e. those whose corpus
callosum connecting the two brain hemispheres has
been severed, can have divided identities. However,
such a theory has been recently challenged [153, 154].
According to this new work, split-brain patients ac-
tually appear to experience divided perception but
undivided consciousness. Corballis et al. [154] argue
that subcortical connections may play a role in inte-
grating information from the two hemispheres.
Remark:
Schaefer and Northoﬀrecently sug-
gested [131] that, since we cannot think about oneself
without being conscious, the cortical mid-line struc-
tures involved in self-referential processing may be
related to a conscious part of the self.
These au-
thors further suggested that sensorimotor processes
may be related to an unconscious part of the self
based on automatic processes.
Similarly, subjec-
tive reports of experienced meditators suggest that,
by rigorously training our attention and turning it
within (see Secs. X C 1 and X C 2 as well as Fig. 22),
it is possible to access the deppest unconscious pro-
cesses underlying our sense of self. According to these
reports, such deep unconscious processes appear to
be related to processes happening around the spinal
cord and brain hemispheres.
X.
DISCUSION
A.
Summary of main points
Here we have thoroughly discussed how ideas from
cognitive science and artiﬁcial intelligence can pro-
vide a fresh perspective to reason more carefully
about the actual role observers play when they per-
form an experiment.
We have done so by provid-
ing a more extensive, hopefully clearer discussion of
the idea we put forward about a year ago [37] that
quantum theory can be understood from two intu-
itive principles (see Principle I and Principle II
in Sec. I). We can rephrase such two principles here
as: (i) experiments are composed of two interacting
subsystems, observer and apparatus; (ii) the system
composed of observer and apparatus should be rep-
resented by one of its subsystems, the ﬁrst-person
observer, not by another external (third-person) ob-
server.
We have shown that the conceptual framework de-
veloped here within the reverse paradigm (see Fig. 4)
has a higher explanatory power and consistency than
the current conceptual framework within the main-
stream paradigm (see Sec. VIII). In particular, it sug-
gests a natural physical explanation of the origin of
Planck constant as due to the physical interactions
supporting the observer’s information processing, and
could help resolve the conceptual issues associated to
the foundations of quantum theory (see Sec. VIII C).
Principle I and Principle II are also more con-
sistent with our everyday human experience by im-
plying we are also physical sub-systems of the uni-
verse, rather than something immaterial, that should
describe experiments from our everyday ﬁrst-person
perspective.
Moreover, the conceptual framework developed
here suggests two predictions that can be tested
experimentally:
(i) humans can observe a single
photon of visible light, so Planck constant can be
derived from psychophysics experiments—we have
shown that existing experiments are consistent with
this prediction [43, 125, 126] (see Sec. IX C), yet more
careful experiments should be performed to have a
more rigorous assessment of its validity; (ii) the neu-
ral correlates of the self are composed of two com-
plementary sub-processes that essentially observe or
represent each other—this may help guide the ongo-
ing search for the neural correlates of the self [27–
29, 131–135, 142, 143] (see Sec. IX D).
Prediction (ii) suggests that the neural architec-
ture of self-aware systems and the self follows a design
principle similar to the double-stranded structure of
the DNA molecule [46]. Much as this particular struc-
ture of DNA avoids the inﬁnite-regress seemingly as-
sociated to a system that reproduces itself—i.e. the
na¨ıve idea that a self-reproducing system should con-
tain a copy of the system within itself, and the copy


## Page 36


36
should also contain another copy within itself for it
to be able to reproduce too, and so on ad inﬁnitum—
the neural structure of the self as composed of two
complementary neural systems (e.g. two complemen-
tary neural networks, much as the architecture of
a Helmholtz machine [155, 156]) avoids the inﬁnite
regress seemingly associated to a system that has a
model of itself, which Metzinger attempted to cure
via his principle of transparency stated in the intro-
duction. This is also analogous to the architecture
of a Turing machine that prints a description of it-
self formalized by the recursion theorem of computer
science (see Appendix C).
B.
Quantum computing, artiﬁcial general
intelligence, and quantum cognition
This approach may help identify unexpected,
game-changing applications of quantum computing
technologies [157] to artiﬁcial general intelligence,
cognitive and social sciences, and the modern ap-
proach to consciousness.
Indeed, while recent re-
search at Google suggests that a quantum com-
puter with over 50 qubits might have enough power
to demonstrate quantum ‘supremacy’ over classical
supercomputers [158], the artiﬁcial problem set to
demonstrate it does not have any known applications
to date.
The approach proposed here may help in
the search of novel applications of emerging quantum
computing technologies where quantum ‘supremacy’
might be achieved.
For instance, the self-referential agents introduced
here could provide a solid foundation for the emerging
ﬁeld of quantum cognition [72], which has provided
evidence that quantum models might more parsimo-
niously describe cognitive phenomena. So, this ap-
proach may help identify datasets on human behav-
ior, for instance, where quantum machine learning is
superior to its classical counterpart (see Sec. II B in
Ref. [159]). It also suggests that quantum computers
might more naturally implement ‘self-aware’ systems,
i.e. systems with a model of themselves, one of the
key objectives of artiﬁcial general intelligence [160]
(see also Refs. [124, 161])—a subﬁeld also known as
machine consciousness [160, 162]. Such self-modeling
capabilities [136, 138] (see item (iv) in Appendix B 2)
along with the ability to model the discreteness asso-
ciated to conscious perception [21, 128] (see item (v)
in Appendix B 1) are features of quantum computers
that could also be relevant in cognitive science and
consciouness research.
Let us mention a couple more technical potential
implications of the ideas we have presented here,
before we move on to what we consider may be
the more relevant potential implications. First, the
link we provided between message-passing algorithms
and imaginary-time quantum mechanics might sug-
gests novel ways to implement these powerful dis-
tributed algorithms on quantum computers or to sim-
ulate quantum systems. Second, our approach sug-
gest that Hamiltonians with complex entries, which
are non-trivial instances of non-stoquastic Hamiltoni-
ans, might be related to non-equilibrium phenomena.
This suggests that some of the potential computa-
tional advantage due to non-stoquasticity, a quan-
tum computational resource, may be related to the
type of computational advantages recently observed
of irreversible Monte Carlo methods [163–165], where
detailed balance is broken, over the equilibrium coun-
terpart. This might also suggest novel ways to im-
plement such general Hamiltonians in quantum com-
puters.
Finally, the way we recasted the quantum
mechanics of a particle in an electromagnetic ﬁeld
might suggest a probabilistic derivation of Maxwell
equations.
Although we have framed our discussion in the rep-
resentationalist paradigm of cognitive science, we ex-
pect it is possible to reframe these ideas within the
context of enactivism [1].
We leave this for future
work.
C.
On science, our worldview, and how we live
However, we expect the more relevant potential im-
plications of these ideas are not related to machines
but rather to us humans: the way we do science, our
worldview, and how we live. We now turn to discuss
these ideas, which are framed within the emerging
ﬁeld of contemplative science [1, 22, 23, 166–170], i.e.
the fruitful collaboration that is emerging between
science and contemplative traditions (see Ref. [167]
for a related discussion). The theoretical and experi-
mental tools emerging at this intersection are consid-
ered rigorous enough to merit a review article in a top
journal such as Nature Reviews Neuroscience [22] on
a practice previously labelled ‘spiritual’, i.e. mind-
fulness meditation (see Fig. 22). We focus here on
the speciﬁc case of Buddhism but other contempla-
tive traditions may have similar concepts. While we
do not use mathematical language in this closing dis-
cussion section, the concepts we will describe can in
principle be modelled mathematically with the tools
explored in this work. Indeed, once we assume the ob-
server is physical as Principle I states, the observer
can also turn her attention within to study the physi-
cal procceses going on inside herself (see Fig. 22). So,
modeling the observer holds the potential to bridge
the ﬁrst- and third-person perspectives.
Although
research on this topic might be a high-risk endevor,
in the ﬁnal section we discuss why we consider the
potential returns to society might be high too.
Of course, at this stage this discussion is merely
speculative; it is done with the only purpose of sug-
gesting some ideas for debate, which could potentially


## Page 37


37
open up a realm of phenomena that has not been con-
sidered to date as a fruitful subject of study in main-
stream physics. These ideas might actually be found
to be wrong after a rigorous scientiﬁc analysis. But
this is precisely the point we want to make: today the-
oretical and experimental tools are emerging to reject
these type of ideas on a rigorous scientiﬁc basis rather
than out of long-held believes (see Fig. 22), or to re-
alize we may have been misled by partial or confusing
information [22, 23]—recall the strong rejection felt
against the concept of atom in the XIX century, or
against the idea that the Earth is not the center of
the universe before Copernicus. We are aware that in
the current state of aﬀairs it seems easier to ﬂow with
the understandable attitude of just automatically re-
jecting this discussion as total non-sense. Yet, we are
convinced we scientists have the social responsibility
to push against the view of the majority when we
believe there is a reason to do so [171], without any
regard for individual considerations. Otherwise, how
would have the concept of atom, for instance, reached
mainstream scientiﬁc debate if all scientists had pre-
ferred to conform to the view of the majority at the
time?
1.
Enlarging our toolbox with ﬁrst-person methods
To begin, scientists have understandably relied
mostly on third-person methods; even brain scien-
tists usually study others’ brains, not their own. Al-
though there are good reasons to doubt about the
usefulness of subjective research methods, the recent
advances in consciousness research (see Appendix B)
strongly suggest they can be very powerful if used
properly (see Fig. 3). Now, if the ﬁrst-person per-
spective lies at the core of fundamental physics, as
the approach we have explored here suggests, then
ﬁrst-person methods have the potential to play a key
role in fundamental physics research (see Fig. 22).
One of the key ideas that led Varela, Thompson
and Rosch, to write their highly inﬂuential book [1]
was to learn the language that Buddhism speaks
and afterwards carefully analyze what this millenar-
ian spiritual tradition may have to say about cogni-
tive science. Unfortunately, strong diﬀerences in lan-
guage have often hindered a communication between
physics and anything that could be labeled ‘spiri-
tual’, with the sad result that mainstream physics
has largely ignored, sometimes with disdain, such ex-
tremely rich traditions. We are convinced that in the
current state of aﬀairs physicist could greatly beneﬁt
by following the example of Varela, Thompson, and
Rosch, and assume what we would call Feynman’s at-
titude, who according to Penrose [51] (page 105) once
said:
“Don’t listen to what I say; listen to what I mean!”
R. Feynman, as quoted in Ref. [51] (page 105)
.
In other words, we suggest to avoid dismissing a
millenarian, profound and large collection of wisdom
just because it is labelled ‘spiritual’, or because we
do not understand yet the language used. Rather, a
more scientiﬁc attitude might be to ﬁrst try to un-
derstand the actual meaning behind the words be-
ing used, much as Varela, Thompson, and Rosch did
twenty ﬁve years ago, and only afterwards do a scien-
tiﬁc assessment of any claims made—we will brieﬂy
mention in Sec. X C 2 some ideas that might be useful
to start with.
Imagine, for instance, that a person who has not
had the opportunity to study the most abstract as-
pects of mathematics were to dismiss it because
he ﬁnds the idea of inﬁnite dimensions, or non-
commutativity as an hallucination.
Now imagine
there were not just one but millions of people with
such an attitude towards science. We contend that
this would be analogous to dismissing what some mil-
lenarian traditions have to say about our description
of reality when we have not had the opportunity to
investigate it with enough depth.
Perhaps one aspect that may have led mainstream
physics to largely dismiss contemplative traditions as
unscientiﬁc is that the latter sometimes tend to do
claims without any scientiﬁc basis. However, in part
thanks to the lead of the 14th Dalai Lama, on of the
most recognized Buddhist monks in the West, some
steps are being taken to alleviate this natural concern.
In 2005 the Dalai Lama wrote [172]
“My conﬁdence in venturing into science lies in my ba-
sic belief that as in science so in Buddhism, understand-
ing the nature of reality is pursued by means of critical
investigation: if scientiﬁc analysis were conclusively to
demonstrate certain claims in Buddhism to be false, then
we must accept the ﬁndings of science and abandon those
claims.”
D. Lama, Ref. [172]
Furthermore, today it is common to ﬁnd collabo-
rations between world-class research institutions and
monks, which have turned out to be very fruitful. The
scientiﬁc approach to mindfulness meditation [22, 23],
for instance, has led to the wide dissemination of such
an old technique. Much of the research to date has
been focused on the cognitive and health sciences, in
part because people tend to think these type of tech-
niques are just therapies to relieve stress and the like.
However, a careful reading of the books written
by highly experienced meditators suggests such tech-
niques are much deeper than that.
Insisting that
meditation techniques are just therapies would be
similar to insisting mathematics is just about the
arithmetics we do in everyday life. Instead, medita-
tion techniques could be considered as sophisticated
tools to carefully investigate our ﬁrst-person experi-
ence of reality. Thus, as Principle I and Principle


## Page 38


38
II are directly related to our human experience, we
are convinced physics may also beneﬁt from such ex-
plorations to study the role of agency in the physical
world, for instance.
Indeed, while physics has largely focused on sys-
tematically exploring an objective, third-person de-
scription of the universe, contemplative traditions
have systematically explored a subjective,
ﬁrst-
person description of human experience—from this
perspective, leading monks might be considered the
ﬁrst-person analogous of leading scientists. For in-
stance, while highly sophisticated machinery devel-
oped over many years allow scientists to analyze oth-
ers’ brains from a third-person perspective, monks
can study from a ﬁrst-person perspective their own
brains, which they can access for free! Of course, the
machinery developed by scientists could also be use-
ful for enhancing the ﬁrst-person study of our own
brains. On this regard the Dalai Lama wrote:
“A comprehensive scientiﬁc study of consciousness must
therefore embrace
both
third-person
and
ﬁrst-person
methods: it cannot ignore the phenomenological reality
of subjective experience but must observe all the rules of
scientiﬁc rigor: So the critical question is this: Can we
envision a scientiﬁc methodology for the study of con-
sciousness whereby a robust ﬁrst-person method, which
does full justice to the phenomenology of experience, can
be combined with objectivist perspective of the study of the
brain?
“Here I feel a close collaboration between modern sci-
ence and the contemplative traditions, such as Buddhism,
could prove beneﬁcial. Buddhism has a long history of
investigation into the nature of the mind and its var-
ious aspects—this is eﬀectively what Buddhist medita-
tion and its critical analysis constitute.
Unlike that of
modern science, Buddhism’s approach has been primarily
from ﬁrst-person experience. The contemplative method,
as developed by Buddhism, is an empirical use of intro-
spection, sustained by rigorous training in technique and
robust testing of the reliability of experience. All medita-
tively valid subjective experiences must be veriﬁable both
through repetition by the same practitioner and through
other individuals being able to attain the same state by
the same practice. If they are thus veriﬁed, such states
may be taken to be universal, at any rate for human be-
ings.”
D. Lama, Ref. [172] (page 134)
So, we would like to pose the following questions:
Can self-referential agents, or a more thoroughly sci-
entiﬁc investigation of agency, help bridge these two
complementary perspectives? Can physics and con-
templative traditions enrich each other? How? As
a possible example of the potential synergy between
fundamental science and contemplative traditions, let
us consider the strategy described in Fig. 22, which
is in line with the strategy described by Dehaene in
Ref. [21] and summarized in Fig. 3 (see also Sec. IX).
We will use as subjective report a piece of text writ-
ten by a representative monk, Gueshe Kelsang Gy-
atso [173], leader of the New Kadampa Tradition. We
emphasize once again that such a subjective report is
considered here exclusively as raw data and nothing
more; we are not suggesting in any way that this is
a valid scientiﬁc account of natural phenomena. Be
aware also that, since contemplative practices have
been developed many centuries ago, they tend to use
a diﬃcult symbolic language that is not necessarily to
be taken literally, but rather as a pointer to certain
subjective experiences that can be carefully investi-
gated via ﬁrst-person methods. The piece of text is
the following (emphasis is our own):
“There are three main channels: the central channel, the
right channel, and the left channel. [...] Other names
for the right channel are [...] the ‘speech channel’ and
the ‘channel of the subjective holder’. This last title in-
dicates that the winds ﬂowing through this channel cause
the generation of conceptions developed in terms of the
subjective mind. Other names for the left channel are
[...] the ‘body channel’ and the ‘channel of the held ob-
ject’, with the last title indicating that the winds ﬂowing
through this channel cause the generation of conceptions
developed in terms of the object.”
Gueshe Kelsang Gyatso, in Ref. [173] (see Appendix II)
Such left and right channels are considered by expe-
rienced meditators as fundamental for the formation
of our self-concepts—the central channel is sometimes
associated to something experience meditators usu-
ally call the ‘True Self’, which we are not considering
here. So, according to these subjetive reports the self-
concept is related to the combination of one process
related to the subject and another process related to
the object. This is consistent with the architecture of
self-referential observers in Figs. 18 and 19 (see also
Figs. 12, 14, 15). So, we might eventually consider
the latter as a physical correlate of such subjective
reports.
In principle, it should be possible to search also
for the neural correlates associated to these subjec-
tive reports. However, since meditators report that
such processes are deeply buried in the unconscious,
it might require more sophisticated technology than
the one currently available. Alternatively, we can also
run a ﬁrst-person experiment with ourselves, our own
physical system, by regularly practicing, for instance,
vipassana meditation. This would allow us to have
a direct experience of such inner phenomena rather
than having to trust the ﬁrst- and third-person re-
ports written by other mediators and scientists, re-
spectively. As a bonus, such practices have the po-
tential to greatly enhance the quality of our lives, ac-
cording to the reports of many meditators throughout
history. In the next section we point out some fur-
ther potential analogies between some concepts stud-
ied here and some concepts from contemplative tradi-
tions with the only purpose of suggesting some ideas
for debate.


## Page 39


39
2.
Can the scientiﬁc and contemplative worldviews
converge?
Here we discuss some potential analogies between
some fundamental concepts in contemplative tradi-
tions and concepts we have explored in this work.
Again, we focus here on the speciﬁc case of Buddhism
but other contemplative traditions may have similar
concepts. Although our discussion is about concepts,
a key aspect of contemplative traditions is that they
are not about theoretical concepts but about expe-
rience. So, from the perspective of the contempla-
tive traditions, the concepts we are about to discuss
could be considered as pointers to actual phenomena
that can only be experienced from a ﬁrst-person per-
spective, i.e. by carrying out ‘experiments’ with our-
selves such as practicing mindfulness meditation—see
Ref. [1] (chapter 10, page 217) for a scientiﬁc-friendly
description of some central ideas in Buddhism. From
this perspective, we might say contemplative tradi-
tions such as Buddhism are to traditional philosophy
what experimental physics is to theoretical physics:
it does not matter what the latter believes to be true,
only the former is rooted in experience and so has the
ﬁnal word.
As we pointed out in the introduction, the main-
stream scientiﬁc worldview today is that there is an
objective mechanical world and that we have the spe-
cial status of understanding such a world as if we
were an abstract entity independent of it. Today it
is almost taken for granted that physics, and in par-
ticular quantum physics, provides the objective laws
that lie at the very foundation of the skyscraper of
science.
The remaining scientiﬁc disciplines there-
fore emerge from it, and at the end of the scientiﬁc
hierarchy we ﬁnd human experience as an ‘illusion’
generated by the incessant activity of billions of neu-
rons distributed throughout our brain and body (see
Fig. 1).
In contrast, the approach here suggests that what
we call the fundamental laws of physics are intrinsi-
cally tied to our human experience, i.e. to our be-
longing to the universe as physical sub-systems of it
(Principle I) and to our everyday ﬁrst-person per-
spective (Principle II). When we take this into ac-
count, the mainstream paradigm nicely summarized
in Crick’s Astonishing Hypothesis (see Sec. I) loses its
ground, it becomes circular because now the subject
is at both the bottom and the top of the scientiﬁc hi-
erarchy (see Fig. 1). At the bottom, the subject gives
rise to the laws of nature, out of which that very same
subject emerges at the top as an ‘illusion’ generated
by an assembly of neurons behaving according to the
laws of nature. In short, the subject ‘emerges’ from
the subject! From this perspective, the ‘hard’ prob-
lem of consciousness may be ill-posed as we cannot
explain human experience by reducing it to some-
thing else; human experience is at the starting point
not at the end (see Fig. 1). In this perspective, laws
of nature are more like self-consistent stable regular-
ities that emerge out of the fundamental circularity
that is the interaction between observer and observed
(see Fig. 1 and Ref. [1], chapter 1).
This does not necessarily mean that we should
move to the other extreme of asserting the reality
of the subject and denying the reality of the world.
Rather, there is a sort of mutual causality between
subject and object: they co-dependently arise, as em-
phasized in Buddhism. Indeed, in our derivation we
did assume there is an external world that provides
the raw data to the observer (see Figs. 16, 18, 19);
furthermore, the self-referential observer is composed
of two sub-observers that play complementary roles
as both observing subjects and observed objects (see
e.g. Figs. 8, 12, 18).
At this point it is useful to follow the strategy de-
scribed by Dehaene [21] (see Figs. 3 and 22) and
take the subjective descriptions of highly experi-
enced meditators (e.g. monks) as raw data to exlore
whether there might be analogies with concepts in our
approach. We will look at the concepts of non-duality,
emptiness, impermanence, unconditioned mind, and
inter-dependence.
From the discussion above we could say that real-
ity is neither objective nor subjective, but non-dual.
There appears to be an analogy between the math-
ematics of self-reference, e.g. the recursion theorem,
and non-duality. Consider, for instance, the case of
the self-referential observer which is composed of two
sub-observers that play dual roles as subjects and ob-
jects. This seems to suggest that the self-referential
observer is non-dual in that both subject and object
play a role in its composition, while at the same time
it is built up of two dual entities.
It is as if both
duality and non-duality coexist. This may address
a common criticism of the concept of non-duality as
being itself dual because it discriminates between two
concepts: duality and non-duality.
The idea that things are co-dependently arising
is central in Buddhism and leads to the concept of
emptiness, i.e. the lack of inherent existence of the
objects we percieve.
To introduce the concept of
emptiness it might be useful to consider an analogy
with a dictionary [174–176] out of which we are sup-
posed to learn the meaning of every word. Now, to
understand the meaning of a word we need to look
up in the dictionary the meaning of the words used
to deﬁne it, and so on recursively.
However, if we
continue doing this sooner or later we will come full
circle, unless there are some words whose meaning
is grounded from outside the dictionary, e.g.
from
direct experience [174].
Our analogy is between a dictionary and the uni-
verse; since we cannot step outside the universe be-
cause by deﬁnition the universe is all there is, we
will insist that every word in the dictionary can only


## Page 40


40
be learned from inside it, i.e. the dictionary is com-
plete. This implies that we will never be able to learn
the meaning of any word! We could say that words
in a complete dictionary have no inherent meaning.
A complete dictionary is a collection of semantic
loops [175] which can only provide the relationship
between words, not their meaning in any objective
way. Similarly, the concept of emptiness refers to the
idea that everything in the universe only exists in re-
lationship to something else, and in particular to the
mind of the observer; i.e. nothing possesses inherent
existence. The analogy with the dictionary suggest
that loops are key and loops are also key in the ap-
proach we have explored here.
As we discussed in
Sec. VIII C, in contrast to what happen in a stochas-
tic process on a chain, in a stochastic process on a
circle there is no intrinsic beginning nor end, which
may imply that states do not posses inherent exis-
tence. In physics jargon we might say that nature
is fully relational, including everything related to the
observer itself.
Another important concept in Buddhism is that
of impermanence which essentially means that at ev-
ery unit of time things arise and then disappear to
arise again in the next unit of time. This implies, in
particular that the self along with its objects of ob-
servation arise and disappear every unit of time. This
seems consistent with the iterative construction of the
ﬁrst-person observer with her objects of observation
(see Fig. 18). Intuitively, we could say that the ﬁrst-
person observer must ﬁrst arise so there is someone
to have the experience of a unit of time. Imperma-
nence also appears to be consistent with an intrinsic
discretization of time as expected from a quantum
theory of gravity.
Let us now mention the concept of unconditioned
mind which essentially says that to experience reality
as it actually is, we should free ourselves of the many
assumptions or beliefs we have about the world. So,
we could say an unconditioned mind is a mind with
zero assumptions, which is reminiscent of Wheeler’s
‘law without law’.
To facilitate this discussion, consider again the ex-
ample of the complete dictionary above which turned
out to be full of semantic loops. One way we could
break such loops is by assuming we know some of the
words in the dictionary (cf. Fig. 11). This is similar
to what is done in mathematics, where the mathe-
matician must assume some statements, the axioms,
to be true. It is similar also to what is done in science,
where scientists ﬁrst have to make some assumptions
about nature that are then tested experimentally to
check the assumptions are not wrong. Without as-
sumptions, without axioms, we do not know how to
start using the methods of logical deduction. Since
in this work we are assuming the scientists are phys-
ical systems, we can consider the doing of science as
a physical process part of which take place in the sci-
entist’s brain. Similarly, we can consider the doing
of mathematics as a physical process going on the
mathematician’s brain when interacting with a set of
statements which are also represented physically on
the mathematician’s brain or in a piece of paper.
Consider as a toy model of this situation the sim-
ple example illustrated in Fig. 17 where an observer
is involved in a circular interaction with a switch and
a lamp. One way the observer can break such a circle
and turn it into a chain is by doing an assumption
about the state of the switch and lamp, for instance
(see Figs. 11 and 17).
This allows us to return to
the classical perspective where there is an inherent
existing state evolving forward in time and an inher-
ent existent self who is observing such a process in a
dual subject-object relationship. However, it might
be possible for the observer not to make any assump-
tions but rather dive deep into the experience of such
circularity in a non-dual way, i.e. through direct ex-
perience. Indeed, Buddhism emphasize that by con-
tinuously practicing certain activities such as mind-
fulness or vipassana meditation, the meditator even-
tually can have a direct experience of emptiness, i.e.
not just as a theoretical construct. As the analogy
with the dictionary suggests, emptiness might indeed
be related to circularity.
This discussion motivates us to ask the following
admittedly bold question:
Can we have a direct,
non-dual, experience of quantum phenomena, such
as quantum superposition or entanglement, by rig-
orously training our brains via the systematic ﬁrst-
person methods developed by contemplative tradi-
tions? This question can in principle be addressed ex-
perimentally by applying such ﬁrst-person methods.
There are subjective reports since many centuries ago
that appear to suggest this might be the case. For in-
stance, experienced meditators speak about a state of
non-discriminating mind; the possibility of perceiving
a bit without discriminating between its two states
sounds similar to the potential experience of a quan-
tum superposition.
It is understandable the usual tendency to auto-
matically dismiss these notions as total nonsense out
of long-held believes against anything that could be
labeled ‘spiritual’, much as XIX century scientists
used to do with the concept of atom. Fortunately,
today scientiﬁc tools are emerging to be able to re-
ject such notions in a more rigorous scientiﬁc basis,
not just out of a belief that risks to become dogma
(see Fig. 22). Once we accept the observer as a phys-
ical system which is part of the experimental setup,
as Principle I suggests, we have the opportunity
to explore a whole new realm of physical phenom-
ena by turning our attention within, which is a possi-
ble interpretation of what meditation techniques do.
Certainly, we may ﬁnd more convenient to avoid get-
ting involved in this type of research because we may
consider it is unlikely to yield interesting results, or


## Page 41


41
we may be concerned that practicing meditation may
harm us despite the many reports throughout his-
tory that it actually improves our well-being.
Al-
though such concerns are quite understandable, by
no means they constitute valid scientiﬁc arguments
to rigorously reject a set of ideas and empirical ob-
servations that have survived per centuries.
Finally, from the perspective explored in this work
whatever an observer can observe requires her to get
involved in a circular interaction with the objects of
observation. This suggests the observer acts as a kind
of hub that connects everything she can ever observe.
In other words, everything the observer can ever ex-
perience is connected to everything else through her-
self.
This is analogous to the Buddhist concept of
inter-dependence, the idea that we are all connected.
Again, Buddhism emphasize its focus is not on the
concepts but rather on the phenomena they point
to, which we can in principle experience via system-
atic ﬁrst-person experimental methods. We have in-
cluded this highly speculative discussion here to pro-
vide some ideas for debate which could potentially
open a realm of phenomena that has not been con-
sidered to date as a fruitful subject of study in main-
stream physics.
3.
Not just bare rationality: A call for action
We hope to have provided enough arguments in
this work to convince the reader that we already
have some tools to more rigorously address the role
of human experience on the foundations of science.
We now argue that the stakes are high for bringing
this debate to the forefront. Although at ﬁrst sight
the ideas discussed below may not seem to be about
physics, we contend that in a profound sense they
are. Moreover, we are convinced this debate might
oﬀer a great opportunity for concerned physicists to
enhance their contribution to the solution of some
of the biggest worldwide challenges, such as global
warming, income inequality, and the strong division
we face today.
Although focusing on the potential
technological applications of the ideas developed in
this article may be more proﬁtable or convenient, we
consider the debate on the potential implications of
the ideas we are about to discuss as far more urgent.
After all, any new technology, no matter how sophis-
ticated, can be used for good or for bad; in a sense,
with every new technology everything changes for ev-
erything to stay the same. What can really make a
diﬀerence is the mindset of the users of the technol-
ogy.
Indeed, by providing the ground on which we step
to understand the world around, scientiﬁc paradigms
have a huge impact on how we conceive businesses
and other socio-economic activities that shape peo-
ple’s lives (see Fig. 1). Oxford economist Kate Ra-
worth, well-known for his idea of the ‘Doughnut Eco-
nomics’ [177], put it nicely [178]:
“In the 1870s, a handful of aspiring economists hoped
to make economics a science as reputable as physics.
[...] The most pernicious legacy of this fake physics has
been to entice generations of economists into a misguided
search for economic laws of motion that dictate the path
of development. People and money are not as obedient
as gravity, so no such laws exist. Yet their false discov-
eries have been used to justify growth-ﬁrst policymaking.
[...] Thanks to more and better data, it has become clear
that such economic laws of motion simply don’t exist. Far
from being a necessary phase of development, extreme in-
equality and environmental degradation are the result of
policy choices, and these choices can be changed. In the
place of laws to be obeyed, there are design decisions to
be made.”
K. Raworth, Ref. [177]
We have suggested in this work that the main-
stream paradigm might have to be revised to put
our subjective human experience at the very founda-
tion of science. In this revised paradigm we are not
mere abstract entities helplessly subjected to the me-
chanical laws of a ruthless inherently existent exter-
nal world. Rather, our human experience takes cen-
ter stage. Given how authoritative physics is in the
modern world, bringing this debate to the forefront
of physics would give concerned physicists a unique
opportunity to join the ongoing push towards a more
human-centered society [179]. We foresee at least two
objectives of this research agenda
(i) Start
building
a
common
language
and
exchanging
methods
between
fundamental
physics and contemplative traditions [1].
To
succeed in physics we should sometimes overem-
phasize qualities such as rationality, ﬁerce com-
petition, and overworking [180]. The contem-
plative traditions seem to put a stronger em-
phasis on qualities such as mindfulness, gen-
erosity, love, as well as a simple and healthy life-
style; according to the contemplative traditions
such qualities are essential for a ﬁrst-person ex-
ploration of human experience because this re-
quires a very calm and equanimous mind. So,
a deeper convergence between science and con-
templative traditions holds the potential to fur-
ther improve the way we live.
(ii) Contribute to the ongoing transition towards
a more human-centered society by exploring
the potential disruption of the mainstream ma-
terialist paradigm, which sometimes seems to
overemphasize less human-centered concerns
such as competition, resource optimization, and
proﬁt maximization. This holds the potential
to further encourage the exploration of more
human-centered business models [179] (see also
Ref. [1], chapter 11, page 243).


## Page 42


42
Since the Age of Reason, or ‘Enlightenment’, rea-
son has been considered as the primary source of au-
thority and legitimacy [181]. Mathematics could be
considered as the very embodiedment of reason. In
mathematics, much as in the example of the dictio-
nary discussed in Sec. X C 2, we start from a given set
of statements called axioms and then we apply a set
of logical rules to essentially transform those state-
ments into new statements we call theorems. When
this can be done we say the theorem is true. Yet this
is similar to the traditional linear chain of cause-eﬀect
relationships that in physics connect an inherently ex-
istent intial state to an inherently existent ﬁnal state.
We have argued in this work that such a linear chain
must be closed into a circle to include the eﬀects of
the observer.
We expect something similar may happen in math-
ematics, where we may need to turn the linear chain
connecting axioms to theorems into a circle that ex-
plicitly includes the mathematician in an eﬀective
way. Indeed, since inference can be considered as a
physical process, we could in principle use the tools
discussed here to model the doing of mathematics
to get some sort of ‘quantum mathematics’ where
circularity, not linear reasoning, takes central stage.
Such type of circularity has been analyzed in eco-
nomics, for instance, by Soros [182]. Yet economics
has been largely built on the idea that we are en-
tities that mostly rely on linear rationality, which
has been sometimes equated to selﬁshness—although
there is growing evidence that humans not only care
about themselves when taking decisions [183], and
that balancing between individual and social consid-
erations might enhance the adaptability of human
groups [184].
Now, contemplative traditions not only have been
an inspiration for cognitive science and medicine, but
also in other ﬁelds such as economics. On this re-
gard, Clair Brown, Professor of Economics and Di-
rector of the Center for Work, Technology, and Soci-
ety at the University of California, Berkeley, recently
wrote [179]:
“Free market economics holds that human nature is self-
centered and that people care only about themselves as
they push ahead to maximize their incomes and fancy
life-styles.
According to this approach,
buying and
consuming—shopping for new shoes or playing a new
video game—will make you happy. Forget that soon you
will grow tired of the shoes, become disappointed with the
game, and be oﬀshopping again. In this endless cycle
of desire, we are continuously left wanting more with-
out ever ﬁnding lasting satisfaction.
Free market eco-
nomics is not guiding us toward living meaningful lives
in a healthy world, nor is it oﬀering solutions to our con-
cerns about global wars, income inequality, and environ-
mental threats.
“Buddhist economics, in contrast, provides guidance for
restructuring both our individual lives and the economy to
create a better world. ‘Practice compassion to be happy’
replaces ‘More is better’. ‘Everyone’s well-being is con-
nected’ replaces ‘Maximize your own position’. ‘The wel-
fare of humans and Nature is interdependent’ replaces
‘Pollution is a social cost that the individual can ignore”.
C. Brown, Ref. [179]
We therefore ﬁnd tempting to ask: Has perhaps the
strong emphasis of mainstream physics on getting rid
of the subjective, ourselves, unknowingly diverted our
attention mostly towards less human-centered con-
cepts such as resource optimization, automation, con-
sumption, competition, growth, etc., sometimes leav-
ing the more human-centered socio-ecological issues
as a side concern to be dealt with later? Isn’t it per-
haps the implicit ideal of mainstream science today
that we become rational machines and we are un-
aware of it? Perhaps it might be rational for a hy-
pothetical oil producer to hamper electric car adop-
tion, for instance, or for a hypothetical social network
company to sell sensible information that can be used
to manipulate voters in an election, as long as those
decisions generate revenue. But is it mindful about
current and future generations?
Physics has played a major role in shaping history
when physicists have challenged the view of the ma-
jority. The history of science is full of examples of our
astonishing human capacity to create and transform
our reality. We hope to have made a case for why we
consider the time is ripe and the stakes are high to
start more thoroughly exploring these ideas that are
already being explored in other ﬁelds of science.
One interesting aspect of contemplative traditions
such as Buddhism is that they do not point the ﬁnger
to anyone. Rather, they suggests that independently
of our political aﬃliation or belief system we all have
one common enemy: the selﬁsh tendencies that some-
times dominate our behavior and that very often we
are not aware of. According to Buddhism, such self-
ish tendencies are rooted in the fact that we have not
directly experienced that what we usually call ‘I’ do
not posses any intrinsic existence. This is consistent
with Metzinger’s view [30, 31] that such an ‘I’ can be
understood as a self-model, a representation in our


## Page 43


43
brains; a representation, not an intrinsically existing
object. More generally, in the Buddhist worldview
nothing possesses inherent existence, everything is re-
lational.
Here we have explored some ideas that may lead
to a physics-based approach to the study of the
self. More importantly, the same ﬁrst-person meth-
ods we suggest could be useful in fundamental physics
research, are also useful to counteract the selﬁsh
tendencies mentioned above;
so it is not about
moralisms. From this perspective, there is one war
that holds great potential to substantially improve
the way we live; it is a paciﬁc and lovely war against
our selves. We hope to have provided enough argu-
ments to suggest that we physicists might have some
important tools at hand to help the human race win
such a war.
Acknowledgments
The ﬁgures in this work were constructed from im-
ages found via Google Images with the option ‘la-
belled for reuse with modiﬁcation’, mostly obtained
from Wikimedia Commons and Pixabay. The pho-
tos in Fig. 8 were taken by Edwin Lemus in Bo-
got´a, Colombia, following the directions of the au-
thor. This work was given slots in the ‘2018 March
Meeting’ of the American Physical Society held at
Los Angeles, California, and the conference ‘The Sci-
ence of Consciousness 2018’ held at Tucson, Arizona.
Unfortunately, I was unable to attend for personal
reasons; a video will be uploaded for the people who
may have been interested.
I thank Marcela Certuche for making the comple-
tion of this project possible and for the many discus-
sions on these ideas. I thank also Harold Certuche
and Blanca Dominguez for their support in the last
part of this project. I thank also Addishiwot Wolde-
senbet Girma, Alejandro Perdomo-Ortiz, and Delﬁna
Garc´ıa Pintos for the support and the interesting dis-
cussions on this work. I thank Tobias Galla, Alan J.
McKane, and the University of Manchester for giv-
ing me the opportunity to work on this project while
being a Research Associate. I thank Buddhist monk
Kelsang Sangton from the Kadampa Meditation Cen-
ter in Bogot´a, Colombia, for very useful discussions
on this work. I thank Marcin Dziubi´nski for his short
but nice lessons on recursion and self-reference at the
University of Cambridge. I thank Diana Chapman
Walsh for interesting discussions on contemplative
science and for bringing my attention to the work of
Arthur Zajonc [168]. I also thank Michael R. Sheehy
for interesting discussions on these ideas.
I thank
Marcello Benedetti, Gonzalo Ordo˜nez, Maria Schuld,
and Alejandro Perdomo-Ortiz for useful comments on
the ﬁrst version of this manuscript. I also thank the
organizers of the conferences “Science and Nondual-
ity 2017” held at San Jose, California, the “Mind &
Life Summer Research Institute 2018” held at Gar-
rison, New York, and the “Second Workshop on Bi-
ological Mentality” held at Ann Arbor, USA, where
these ideas were presented. I thank Camila Sardeto
Deolindo and Cerys Tramontini for bringing my at-
tention to the work of Alan Wallace [167] I thank
as well Mario Chamorro and Laura Escobar for their
inivitation to discuss this work in the ‘AniMondays’
they organized in 2017 at Mountain View.
I thank Matteo Marsili, Luca Dall’Asta, and the
Abdus Salam ICTP for the hospitality during a visit
in 2010, where an early version of some of these
ideas was drafted. I also thank Valentina Lanza, Al-
fredo Braunstein, Abolfazl Ramezanpour, Riccardo
Zecchina, Fabrizio Altarelli for their support at the
Politecnico di Torino when the development of these
ideas started. I thank also Ralph Gebauer, Giuseppe
Santoro, Hernan Ocampo, and Efrain Solarte for
the excellent lessons and discussions on quantum
mechanics.
I thank John Henry Reina, Fabio Be-
natti, and Roberto Floreanini for useful discussions
on quantum theory. I thank Gerhard Gr¨ossing and
his wife for the hospitality at the conference “Emer-
gent Quantum Mechanics” of the “Heinz von Foerster
Congress” which took place at Vienna in 2011, and to
Garnet Ord for the interesting discussions held there.
I thank also Gerard ’t Hooft for the short but in-
teresting discussion on the foundations of quantum
mechanics at the “Euroscience Open Forum” held
at Turin in 2010. I thank Maria Schuld, Francesco
Petruccione and his wife, as well as Kriben Pillay for
the hospitality at the summer school on “Quantum
Machine Learning”, which took place at the Drak-
ensberg Mountains in 2017, and for the interesting
discussions related to these ideas.
I thank Narlinda Espinosa, Pedro Pablo Ortega,
Tommaso Biancalani, and Jaime G´omez G´omez for
listening to some of these ideas. I also thank Narlinda
Espinosa, Javier Montoya and Beatriz Cogollo for
their support at the Universidad de Cartagena that
facilitated the completion of this work.
I must thank Roberto Dotta, Luca Gilli, Johanna
Wirrer, Mario Andr´es Acero Ortega, Andrea Occhip-
inti, Fabio Ricciato, Diana Vanessa Realpe, and Ger-
ardo Paz-Silva for their support that contributed to
the development of this project.
Last but not least, I thank Mariela G´omez Ram´ırez
and Nelson Jaramillo G´omez for bringing my atten-
tion to these ideas.
Appendix A: We as physical systems
According to Principle I, anything that a robot
can perceive must be physically represented in its
hardware (see Fig. 17). Since we are also observers,
Principle I implies that the same happen to us (see


## Page 44


44
Fig. 6). In other words, it implies that we are not
the immaterial entities that classical physics has im-
plicitly assumed for so long.
We are physical, our
senses are physical, our brains are physical. From this
perspective, we are not conceptually diﬀerent from a
computer since anything we can percieve has a physi-
cal process associated in our brains, the so-called neu-
ral correlates [20, 21]. More clearly, although the way
in which our brains encode and process information
may be radically diﬀerent from the way state-of-the-
art computers do, the minimal physical requirements
identiﬁed above, i.e. physical representation and in-
teraction, cannot be avoided.
In this respect, according to Principle I, the brain
is the fabric of our reality. We are unable to distin-
guish reality from our perception of it in the sense
that what exists for us, what we can perceive, must
be physically represented in our ‘hardware’. There is
indeed experimental evidence to support this. Con-
sider, for instance, the experimental demonstration
reported in Ref. [16] where humans are able to play a
video game using only input from direct brain stim-
ulation, i.e.
without relying on any usual sensory
inputs like sight, hearing, or touch.
Another ex-
ample is the recent experimental demonstration re-
ported in Ref. [17], where humans can control robots
via the neural correlates of their thoughts (see also
Refs. [18, 19]). Neural correlates have been identi-
ﬁed even for hallucinations and out-of-body experi-
ences [21, 26–29] (see Fig. 3).
A diﬀerent type of evidence, however disturbing, is
Buddhist monk Thich Quang Duc, who remained in
deep meditation while burning in ﬂames until death
on 11 June 1963 [185, 186] (disturbing videos of this
are available in YouTube). For many of us, touching
with our ﬁngers the ﬂame of a candle may produce
a perception of extreme pain that would move us to
act almost instinctivly. However, the case of Thich
Quang Duc suggests that things are not necessarily
the way we are accustom to, and that our perception
of reality might be manipulated.
It is understandable the extreme caution that we
physicists have had with anything related to our-
selves.
But we now live in an era where machine
learning and artiﬁcial intelligence are doing amaz-
ing progress [14, 15], and scientists have found clever
ways to experimentally tackle certain aspects of con-
sciousness [20, 21].
We need to be careful of any
strong prejudices that may remain from the past and
that may prevent us from making further progress.
Indeed, the observation that our brain co-creates our
reality may be uncommon to some physicists, but not
so for brain research scientist— see e.g. Ref. [187],
chapter 2, for a recent presentation intended for a
general audience.
This has also been the position
of some millenarian spiritual traditions, like Bud-
dhism, and one of the tenets underlying mindfulness
meditation [22]— see e.g.
Ref. [23] for a modern
scientiﬁcally-minded presentation of these ideas (see
also Ref. [1], chapter 10).
Of course, this does not rule out the existence of
an objective world out there. What we perceive, e.g.
light, can be generated by an external physical pro-
cesses, e.g. a lamp shining. But what we perceive
is not the lamp itself, but the physical processes or
neural correlates that the lamp generates in our brain.
From this perspective, we could say that when scien-
tists discuss the results of an experiment what they
actually discuss are the perceptions they have (see
Fig. 9). For instance, when scientists read a num-
ber in the display of a machine, such perception is
actually a physical process happening in the scien-
tists’ brains. We often take for granted that, for in-
stance, the perception of a number on the display of
a machine is generated by a truly existing machine
displaying such a number. Indeed, this assumption
is quite consistent with our experience as scientists.
Yet, instead of using this robust assumption as the
starting point, here we start earlier by modelling the
very inference process that allows us to trust this as-
sumption (see Fig. 9).
Let us consider the following thought experiment:
Thought experiment: As we mentioned above, sci-
entist have already demonstrated that it is possible
to induce percepts, such as the experience of seeing a
simple video screen [16] or the feeling of being out of
the body [27–29], in human subjects by direct brain
stimulation without relying on any usual sensory in-
puts such as sight, audio, touch, etc. These proof-of-
principle experiments allow us to imagine that, as the
underlying technology progresses, it might be possi-
ble to induce more and more realistic percepts with-
out relying on the traditional sensory pathways. Let
us imagine a time when such technology is mature
enough to induce the experience that we are living in
a virtual world we cannot distinguish from the real
world, much as the situation depicted in the movie
The Matrix. In such a situation it can happen that
we go to sleep while experiencing the real world and
then some scientists plug our brains to such tech-
nology without us being aware of it. The scientists
could then induce the experience that we have wo-
ken up the next day in a virtual world we believe
is the real world. What experiment could we carry
out to realize we are experiencing a virtual world?
Consistent with the modern scientiﬁc insights that
our brain is the fabric of our reality, we expect there
is no experiment to distinguish our reality from our
perception of it (see Fig. 9 and Ref. [12]). While this
may be new and even shocking to some scientists,
this conclusion has been reached many centuries ago
by some contemplative traditions via rigorous ﬁrst-
person experimental methods (see Sec. X C). While
scientists have mostly focused their attention on phe-
nomena taking place in the external world—this is


## Page 45


45
the case even when scientists study others’ brains—
contemplative practitioners have mostly focused their
attention on phenomena taking place inside them-
selves (see Fig. 22).
The view we take here, which is consistent with
intersubjectivity, is that physics is about people, say
scientists, agreeing on a class of subjetive experiences.
Let us now, discuss a class of subjective experiences,
which is usually not considered part of the realm of
physics, that relates directly to the sense of ‘I’ and
the ﬁrst-person perspective, which is related to the
concepts explored in this work. From our personal
experience we know that we can experience ourselves
as subjects, i.e. as an ‘I’ that perceives the external
world; consider for instance the sentence
I observe a lamp.
(A1)
Similarly, we can also experience ourselves as an ob-
ject, a ‘me’ that is observed by someone else; consider
for instance the sentence
The government is observing me.
(A2)
We can even experience circular things like thinking
of the sentence
I am looking at myself.
(A3)
So, from a psychological point of view we have no
problem to deal with ourselves as both subjects and
objects.
Understanding this complex matter is out of reach
to the author of this work.
However, we can use
Principle I along with the veriﬁable fact that we
can think of (or observe) statements like those in
Eqs. (A1) to (A3) to conclude that there must be
physical processes representing such experiences of
ourselves as both subjects (e.g. Eq. (A1)) and ob-
jects (e.g. Eq. (A2)), as well as the kind of circular
experiences described by Eq. (A3). Indeed, there is
ongoing research on identifying the neural correlates
of the self [131, 188]. Our work suggests that the neu-
ral architecture of the self should be composed of two
neural sub-systems that essentially model each other,
which could potentially explain why our brains is di-
vided into hemispheres (see Sec. IX D and Fig. 20).
In this respect, the complementary pairs described
in Secs. III B and VII appear to be related to the
physical processes representing the perception of our-
selves as subjects, i.e. observers, and as objects, i.e.
observed. As early as 1929, Niels Bohr [36] had al-
ready considered this as the possible origin of com-
plementarity in quantum theory. Consider what Niels
Bohr wrote in Ref. [36] (as reproduced in Ref. [189]):
“For describing our mental activity, we require, on one
hand, an objectively given content to be placed in opposi-
tion to a perceiving subject, while, on the other hand, as
is already implied in such an assertion, no sharp separa-
tion between object and subject can be maintained, since
the perceiving subject also belongs to our mental con-
tent. From these circumstances follows not only the rel-
ative meaning of every concept, or rather of every word,
the meaning depending upon our arbitrary choice of view
point, but also that we must, in general, be prepared to
accept the fact that a complete elucidation of one and
the same object may require diverse points of view which
defy a unique description. Indeed, strictly speaking, the
conscious analysis of any concept stands in a relation of
exclusion to its immediate application. The necessity of
taking recourse to a complementary, or reciprocal, mode
of description is perhaps most familiar to us from psy-
chological problems.”
N. Bohr, Ref. [36]
As we discuss in Secs. VII A and VII B, Principle
II leads to complementarity when dealing with the
self-referential problem of describing the world from
within. This could help explain why quantum models
appear to parsimoniously describe cognitive phenom-
ena [72].
Appendix B: The modern and well-respected
approach to consciousness
1.
Third-person perspective and the ‘easy’
problem of consciousness
Dehaene discusess three key ingrediates that have
helped the subject of consciousness become a hot re-
search topic today [21] (page 8; see also Ref [124]): (i)
a better deﬁnition of consciousness that distinguishes
a minimum of three concepts: vigilance, attention,
and conscious access—among these, consciouss ac-
cess, i.e. ‘the fact that some of the attended infor-
mation eventually enters our awareness and becomes
reportable to others’, has been the main focus of ex-
perimental research, and is the focus of this work
too; (ii) the development of techniques to manipu-
late consciousness in the lab; (iii) taking subjective
introspection seriously, not as a research method but
as a source of raw data that can be contrasted with
measurements of neuronal activity to identify poten-
tial Neural Correlates of Consciousness (NCCs; see
Fig. 3).
One of the key aspects identiﬁed by this modern
approach to consciousness is that information can be
processed unconsciously. Another key aspect is the
identiﬁcation of certain features, the NCCs, that dis-
tinguishes conscious perception from unconsious in-
formation processing.
We now summarize some of
these insights for reference:
(i) Information can be processed unconsciously:


## Page 46


46
Many information processing tasks can be per-
formed unconsciously [21] (chapter 2); we can
even do some mathematical operations at the
unconscious level. Apparently unconscious in-
formation processing is carried out by myriad
processors working in paralllel. This appears to
be related to the feature-extraction component
of the artiﬁcial observer illustrated in Fig. 16.
(ii) Consciouss perception is a neural ‘tsunami’:
Conscious perception is distinguished by a rel-
evant ampliﬁcation factor in neural activity as
compared to unconscious information process-
ing [21] (chapter 4); in words of Dehaene:
“Subliminal perception can thus be compared to a surf
wave that looms large on the horizon but merely licks your
feet when it reaches the shore. By comprarison, conscious
perception is a tsunami—or perhaps an avalanche is a
better metaphor, because conscious activation seems to
pick strength as it progresses, much as minuscule snow-
ball gathers snow and ultimately triggers a landslde”
S. Dehaene, Ref. [21] (page 119)
(iii) Conscious perception is global neural activity:
Conscious perception is distinguished by a syn-
chronization of information exchanges across
distant brain regions (cf. Fig. 16c,d).
(iv) Conscious perception is bidirectional causality:
Conscious perception is distinguished by a mas-
sive increase in bidirectional causality through-
out the brain, producing a sustained state of
reverberating activity.
In other words, there
is a forward-moving wave which can be inter-
preted as the climbing of sensory information
from raw data to increasingly abstract repre-
sentations of the stimulus (cf. Fig. 16). Fur-
thermore, there is an opposite descending wave
whose function Dehaene suggests could be am-
plifying incomming activity or checking that
the input is consistent with the current interpre-
tation at a higher level. This bidirectional dy-
namics seems similar to the situation illustrated
in Fig. 18, which we expect to be a minimal ar-
chitectural requirement for a physical system
to implement a self-referential observer with a
ﬁrst-person perspective.
(v) Conscious access is discrete: Consciouss access
seems to be related to a discontinous phase
transition induced by the feedback mechanism
that arises when the neurons at the higer level
sent back excitatory signals to the very units
that activated them [21] (page 184). This seems
to be consistent with evidence suggesting that
conscious access is all-or-none [128] and, in the
perspective take in this work, might underlie
the quantization of energy (see Sec. IX C).
(vi) Consciouss processing resembles a computer:
Consciousness appears to give humans the
power of a Turing machine.
More precisely,
the brain’s behavior during long conscious
information-processing tasks, such as the per-
formance of complex mathematical calcula-
tions, is roughly captured by the ideal model of
a Turing machine [21] (page 104). This is con-
sistent with the second component of a physical
observer described in Fig. 16.
These features concern the information-processing
mechanisms underlying conscious perception, which
is considered as one of the ‘easy’ problems of con-
sciousness.
These features do not address the so-
called ‘hard’ problem of consciousness closely related
to our human experience.
In the next section, we
brieﬂy discuss recent developments on this front.
2.
First-person perspective and the ‘hard’
problem of consciousness
Edelman [32] (page 412) summarizes the so-called
‘hard’ problem of consciousness in three questions:
What makes a mere physical process an experience
for someone? What makes a mere physical system
a subject, or an experiencer?
What does having
a ﬁrst-person perspective on an experience consists
of? About ﬁfteen years ago, Metzinger [30] (see also
Ref. [31] and chapter 9 in Ref. [32]) put forward a
theory of subjectivity based on the concept of a self-
model, which provided a fresh approach to the ‘hard’
problem of consciousness. (For a short introduction
to the most central ideas see Metzinger’s talk ‘The
transparent avatar in your brain’ at TEDxBarcelona.)
Since we expect such a self-model to be closely related
to the self-referential observers discussed in this work,
we brieﬂy mention here some of the main concepts in-
volved.
Edelman [32] (chapter 9) summarizes four key com-
ponents in Metzinger’s theory [30]: (i) Agency, or
sense of initiative; minenes, or sense of ownership;
perspectivelness, or the perception of phenomenal
space as being organized around the self; selfhood, or
the conscious experience of being someone. In partic-
ular, Edelman [32] (see page 419) summarizes Met-
zinger’s ideas on selfhood in four steps that we cite
almost textually here:
(i) The experienced reality is virtual.
The ‘raw
data’ in the world is accessible to the brain ex-
clusively through the mediation of its sensory
apparatus (which includes both the ﬁve exter-
nal senses and the various interoceptive chan-
nels). No matter how veridical some of the in-
formation provided by these senses is, the rep-
resentations they feed into are necessarily ‘vir-
tual’ computational constructs. This seems to


## Page 47


47
be consistent with the architecture of physical
observers illustrated in Fig. 16.
(ii) The experienced reality is a simulation of the
world. Use of the virtual representations gen-
erated by the senses often involves ‘simulation’
of events or situations. Simulation is also cen-
tral to planning and control: intended actions,
for example, are represented by motor programs
whose eﬀects are simulated by a circuit that
gives rise to the phenomenal sense of agency
and ownership.
Note that an embodied and
situated agent is an integral part of the world,
and so must be simulated along with it by the
agent’s cognitive system.
(iii) The simulation is not recognized by the system
as such. To avoid inﬁnite regress (trying to rep-
resent a system that represents a system that
represents...; see Figs. 7 and 8), the model of
the world (which includes a model of the system
itself) is taken to be the ‘last word’—the ulti-
mate reality. This is essentially the concept of
transparency we mentioned in the introduction.
We here tackled the inﬁnite regress via ideas re-
lated to the recursion theorem, which suggests
that the minimal architecture of a self-model
should be composed of two complementary sys-
tems that essentially model each other. From
this perspective, it is tempting to think that in
the case of humans, such a minimal architec-
tural requirement is implemented via the divi-
sion of our brain into two hemispheres, which to
a large extent appears to perform certain com-
plementary tasks (see Fig. 20; cf. Fig. 12).
(iv) The part of the simulation that represents the
system itself is special. The represented real-
ity contains one component that diﬀers from
all others in being always present.
This
self-model—the only representational structure
that is fed by a continuous source of inter-
nally generated (interoceptive) input—is the
phenomenal self.
Appendix C: Self-reference and the recursion
theorem
Here we brieﬂy discuss the recursion theorem of
computer science, which can be considered as a math-
ematical formalization of the concept of self-reference.
Figure 12 illustrates the core concept underlying the
recursion theorem using the speciﬁc case of a self-
printing program, or quine, introduced in Sec. III B.
As we mentioned in Sec. III B, a self-printing pro-
gram, represented as a full computer in Fig. 12, is
composed of two complementary sub-programs, Al-
ice and Bob represented as the two halves of a com-
puter in Fig. 12, that essentially print each other (cf.
Fig. 8b).
We now formalize this concept following Ref. [90]
(chapter 6). Let Σ be an alphabet, i.e. a ﬁnite set of
characters, and let Σ∗denote the set of all possible
strings of characters from alphabet Σ, here referred to
as words. A Turing machine is an abstract machine
with no memory constraints which can manipulate
the characters in an alphabet Σ according to a pre-
speciﬁed set of rules. In other words, a Turing ma-
chine is the implementation of an abstract mechanical
process that transforms a given string of characters
into another, eﬀectively computing a given function
f : Σ∗→Σ∗.
It is possible to associate to every Turing machine
TM a unique string of characters “TM” ∈Σ∗, which
is referred to as the description of the Turing ma-
chine; the quotation marks “ ” can be considered
here as an operator that transform Turing machines
into strings in Σ∗. A Turing machine TM is the ab-
stract version of a program, e.g.
a search engine,
that can run on a computer to perform a given task,
e.g. search for websites related to a speciﬁc keyword.
A description of a Turing machine “TM”, instead,
is the abstract version of the code written in a spe-
ciﬁc programming language that is used to compile
the corresponding program. This ability to associate
a unique string of characters to a Turing machine
is what allows a Turing machine to implement self-
reference. Indeed, from this perspective we can think
of a Turing machine TM as a string of characters, i.e.
its description “TM”, that can manipulate any string
of characters w ∈Σ∗, including its own description,
i.e. w = “TM”. In this sense, it can manipulate (a
description of) itself.
An example relevant for our discussion is the Tur-
ing machine Q represented as a computer in Fig. 13a.
Given some input (e.g.
the image of a bulb in
Fig. 13a), the Turing machine Q prints the descrip-
tion of another Turing machine, represented by a
tablet within quotation marks in Fig. 13a, that prints
the given input. More formally, the Turing machine
Q implements a function fQ, represented by a box
in Fig. 13b, that takes as input any word w ∈Σ∗
and prints the description “Printw” of another Tur-
ing machine Printw that ignores its input and just
prints w. The existence of such a Turing machine is
proven in the
Lemma 6.1 of Ref. [90]: There is a computable
function fQ : Σ∗→Σ∗such that, for any string w,
fQ(w) = “Printw” is the description of a Turing
machine Printw that ignores its input, just print w
and halts.
The Turing machine Q is useful to build self-
printing Turing machines, as illustrated in Fig. 14
which is the formal version of Fig. 12. As we said


## Page 48


48
above, as well as in Sec. III B and Fig. 12, a self-
printing Turing machine
Self = Alice ◦Bob,
(C1)
is composed of two Turing machines, Alice and Bob,
that essentially print each other. Figure 14a shows
the Turing machine
Alice = Print“Bob”,
(C2)
which ignores its input, prints a description “Bob”
of the Turing machine Bob, and halts.
Now, if
Bob
?= Print“Alice” were to similarly ignore its in-
put, just print a description of Alice, and halt, we
would have a circular deﬁnition were the deﬁnition of
Alice depends on who Bob is, and viceversa.
To avoid such circular deﬁnition, Bob essentially
works backwards by inferring the description of Al-
ice from the output she produces, which is “Bob”
(see Fig. 14b). This is precisely what the Turing ma-
chine Q does: given an input w = “Bob” it prints
the description “Print“Bob”” of a Turing machine
Print“Bob” that ignores its input, prints w = “Bob”,
and halts. So, when Q takes the input “Bob” it out-
puts precisely “Alice”, since Print“Bob” = Alice.
But the full self-printing machine actually is
Self = Alice ◦Bob (see Fig. 14c), so Bob is de-
signed such that (see Fig. 14b): (i) it takes as input
the description “TM” of an arbitrary Turing machine
TM and infers via Q the description of a Turing ma-
chine that prints “TM”; (ii) it then generates the
composition Print“TM”◦TM of the Turing machines
associated to the description “Print“TM””, that it
inferred via Q from the given input “TM”, and to
the descritpion “TM” it receives as input; (iii) it
ﬁnally prints the description “Print“TM” ◦TM” of
such composition. This fully speciﬁes Bob in a way
that is independent of who Alice is, i.e.
Bob = “TM”Print“Print“TM”◦TM”.
(C3)
Notice that the ﬁrst Print operator in the deﬁnition
of Bob in Eq. (C3) has also a left subscript “TM”,
which indicates its input; this contrasts with the def-
inition of Alice which does not have such a left sub-
script indicating that it always ignores its input.
So, we can now fully specify Alice by replacing
Bob in Eq. (C2) by the left hand side of Eq. (C3).
With both Alice and Bob fully speciﬁed, we can
fully specify Self in Eq. (C1) too. See Fig. 14 and
Ref. [90] (chapter 6) for further details.
Now, a Turing machine not only can print its own
description, it can also use it as an input and per-
form general computational operations with it. Fur-
thermore, a Turing machine (illustrated in Fig. 15a
by a big computer) can take a combined input com-
posed of external data (e.g. the imagine of a bulb
in Fig. 15a) and its own description (illustrated in
Fig. 15a by a small computer printed within quation
marks on the screen of the big computer) and perform
general computational operations with it. Figure 15a
illustrates this by a computer that takes as external
input the image of a bulb and print a description of
a rotated version of itself printing a rotated version
of the bulb.
The architecture of such general Turing machine,
that we call here Recursion, is composed of three
Turing machines (see Fig. 15b): Alice and Bob,
which together generate the description of Recur-
sion, and another 2-argument Turing machine RT
that takes as inputs both an arbitrary word w ∈Σ∗
provided from the outside and the description of Re-
cursion generated from the inside of Recursion it-
self by the composition of Alice and Bob, i.e.
Recursion = Alice ◦Bob◦RT;
(C4)
here the superscript ◦indicates the ouput of Bob is
passed to the upper input channel of RT.
The deﬁnition of Alice is slightly modiﬁed to
take into account the new Turing machine RT (see
Fig. 15c), i.e.
Alice = Print“Bob◦RT”.
(C5)
The deﬁnition of Bob instead remains the same as
in Eq. (C3) since it was deﬁned in terms of a generic
Turing machine TM (see Fig. 15d). The 2-argument
Turing machine RT implements the actual computa-
tions according to a given 2-argument function fRT;
it is simlarly deﬁned in terms of a generic Turing ma-
chine TM whose description enters through the upper
input channel, leaving its lower input channel free to
receive external data w ∈Σ∗(see Fig. 15e). So, we
have (see Fig. 15f): where the lower input channel of
RT remains available to receive external data. This
proves the
Recursion theorem (Theorem 6.3 in Ref. [90]):
Let RT be a Turing machine that computes a 2-
argument function fRT : Σ∗× Σ∗→Σ∗. Then there
is another Turing machine Recursion that com-
putes a function fRecursion : Σ∗→Σ∗, where for ev-
ery w ∈Σ∗,
fRecursion(w) = fRT(“Recursion”, w).
See Fig. 15 and Ref. [90] (chapter 6) for further
details.
Appendix D: Derivation of real kernel
representaions in Sec. IV B
1.
Non-relativistic Schr¨odinger equation
The Schr¨odinger equation of a single particle of
mass m in a one-dimensional non-relativistic poten-


## Page 49


49
tial V (x) is given by
iℏ∂ψ(x, t)
∂t
=

−ℏ2
2m
∂2
∂x2 + V (x)

ψ(x, t),
(D1)
where ψ(x, t) is the wave function. If we discretize
x ≈kδ, with k = . . . , −2, −1, 0, 1, 2, . . ., in steps of
size δ, we can also discretize the second-order diﬀer-
ential opperator in a symmetric way via the second-
order central diﬀerence
∂2ψ(x, t)
∂x2
= ψ(x + δ, t) −2ψ(x, t) + ψ(x −δ, t)
δ2
.
(D2)
If we write the discretized wave function as a vector
ψ(t) =








...
ψ(−δ, t)
ψ(0, t)
ψ(δ, t)
...








,
(D3)
which we represent here with boldface notataion,
then the Laplace operator ∂2/∂x2 in Eq. (D2) can
be represented by the symmetric matrix
∆= 1
δ2








...
...
...
...
...
· · ·
0
1
−2
1
0
· · ·
· · ·
0
1
−2
1
0
· · ·
· · ·
0
1
−2
1
0
· · ·
...
...
...
... ...








,
(D4)
and the Hamiltonian H = −(ℏ2/2m)∂2/∂x2 + V (x)
in square brackets in Eq. (D1) can be represented by
the matrix
H =









...
...
...
...
...
· · ·
0
−
ℏ2
2mδ2
ℏ2
mδ2 + V−1
−
ℏ2
2mδ2
0
· · ·
· · ·
0
−
ℏ2
2mδ2
ℏ2
mδ2 + V0
−
ℏ2
2mδ2
0
· · ·
· · ·
0
−
ℏ2
2mδ2
ℏ2
mδ2 + V1 −
ℏ2
2mδ2
0
· · ·
...
...
...
... ...









,
(D5)
which is real and symmetric, so the dynamical matrix
is given by J = H/ℏ; here Vk = V (kδ).
2.
From non-relativistic path integrals to real
convolutions
As originally described by Feynman, the non-
relativistic Schr¨odinger equation, Eq. (D1), can be
derived from the path integral via (see e.g. Eq. (18)
in Ref [91])
ψ(xℓ+1, t + ϵ) = 1
A
Z
exp
 i
ℏS(xℓ+1, xℓ)

ψ(xℓ, t)dxℓ,
(D6)
where for the one-dimensional case in Eq. (D1) we
can set the short-time action as
S(xℓ+1, xℓ) = mϵ
2
xℓ+1 −xℓ
ϵ
2
−ϵV (xℓ+1), (D7)
and
A =
p
i2πℏϵ/m;
(D8)
furthermore, xℓrepresents the position of the particle
at time t = ℓϵ. Notice that by iterating Eq. (D22) we
can obtain the path integral representation.
By multiplying Eq. (D22) by its congugate we can
derive the corresponding equation for the density ma-
trix ρ(x, x′, t) = ψ(x, t)ψ∗(x′, t), i.e.
ρ(xℓ+1, x′
ℓ+1, t + ϵ) =
1
|A|2
Z
exp
 i
ℏ

S(xℓ+1, xℓ) −S(x′
ℓ+1, x′
ℓ)

ρ(xℓ, x′
ℓ, t)dxℓdx′
ℓ,
(D9)


## Page 50


50
where |A|2 = 2πℏϵ/m.
While we could tranform Eq. (D9) into a pair of
real equations as we did in Sec. IV A, this would
lead to oscillatory terms arising from the complex
exponential factor in the integrand. Such oscillatory
terms would be diﬃcult to interpret in probabilis-
tic terms later on. However, it is possible to rewrite
these equations in terms of real Gaussian convolu-
tions, which can be naturally interpreted in proba-
bilistic terms. Before we show how to do this, we will
outline the main steps in the derivation of Eq. (D1)
from Eq. (D22), described in detailed in e.g. Ref. [91],
which closely parallel the derivation in terms of real
Gaussian convolutions to be described afterwards.
First, expanding ψ(xℓ+1, t + ϵ) to ﬁrst order in ϵ,
we can write Eq. (D22) as
ϵ∂ψ(xℓ+1, t)
∂t
= 1
A
Z
exp
 i
ℏS(xℓ+1, xℓ)

ψ(xℓ, t)dxℓ
−ψ(xℓ+1, t).
(D10)
Since ϵ →0, the complex Gaussian factor associated
to the kinetic term in Eq. (D7) oscillates very fast
except in the region where xℓ+1 −xℓ= O(
p
ℏϵ/m).
So, to estimate the integral to ﬁrst order in ϵ, the term
ψ(xℓ, t) in the right hand side of Eq. (D10) need be
expanded around xℓ+1 to second order in xℓ+1 −xℓ.
Consistent with this approximation to ﬁrst order in
ϵ, we also do exp [−iV (x)ϵ/ℏ] = 1−iV (x)ϵ/ℏ+O(ϵ2).
This leads to Eq. (D1).
However,
as we know from the derivation of
the diﬀusion equation approximation for a random
walk [190, 191], a real Gaussian has an equivalent
cancelling eﬀect, not because of fast oscillations but
because of exponentially small terms. More precisely,
we will argue that if we introduce the Hamiltonian
function
H(x, x′) = m
2
(x −x′)2
ϵ2
+ V (x),
(D11)
we can do the replacement, which amounts to a Wick
rotation ϵ →−iϵ,
1
A exp
 i
ℏS(x, x′)

→
1
|A| exp

−H(x, x′)ϵ
ℏ

; (D12)
notice that the kinetic term in the right hand side
of Eq. (D12) leads to a real Gaussian with variance
ℏϵ/m and normalization constant given precisely by
|A|.
Due to this Gaussian term, the integral
1
|A|
Z
exp

−H(x, x′)ϵ
ℏ

ψ(x′, t)dx′ =
h
1 −ϵ
ℏV (x)
i 
ψ(x, t) + ℏϵ
2m
∂2ψ(x, t)
∂x2

+ O(ϵ2)
= ψ(x, t) −ϵ
ℏV (x)ψ(x, t) + ℏϵ
2m
∂2ψ(x, t)
∂x2
+ O(ϵ2),
(D13)
can be approximated to ﬁrst order in ϵ in a way simi-
lar to that of the integral in Eq. (D10). Indeed, since
ϵ →0, the real Gaussian factor associated to the
kinetic term in Eq. (D11) is exponentially small ex-
cept in the region where x −x′ = O(
p
ℏϵ/m). This
has allowed us to estimate the integral to ﬁrst or-
der in ϵ by expanding the term ψ(x′, t) in the left
hand side of Eq. (D13) around x up to second or-
der in x −x′. Consistent with this approximation to
ﬁrst order in ϵ, we have also done exp [−V (x)ϵ/ℏ] =
1 −V (x)ϵ/ℏ+ O(ϵ2).
This implies that Eq. (D1) can be written in terms
of real Gaussian convolutions in a way similar to
Eq. (D10) as
ϵ∂ψ(xℓ+1, t)
∂t
= i
 1
|A|
Z
exp

−H(xℓ+1, xℓ)ϵ
ℏ

ψ(xℓ, t)dxℓ−ψ(xℓ+1, t)

.
(D14)
Indeed, by replacing the term with the integral in
the right hand side of Eq. (D14) by the right hand side
of Eq. (D13), and multiplying both sides of Eq. (D14)
by iℏ/ϵ, we obtain Schrodinger equation (Eq. (D1)).
In this way we have essentially bring the imaginary
unit i from the exponential in Eq. (D10) down to
turn it into a linear factor in Eq. (D14). In contrast
to Eq. (D22), however, it does not seem possible to
obtain a (real) path integral by iterating Eq. (D14).
Finally,
we now show that Eq. (D14) leads


## Page 51


51
to
an
equation
analogous
to
the
von
Neum-
man equation (Eq. (1)) for the density matrix
ρ(x, x′, t) = ψ(x, t)ψ∗(x′, t), in terms of real Gaus-
sian convolutions instead of diﬀerential operators. In-
deed, taking the time derivative of this density matrix
yields
∂ρ(x, x′, t)
∂t
= ∂ψ(x, t)
∂t
ψ∗(x′, t) + ψ(x, t)∂ψ∗(x′, t)
∂t
;
(D15)
now, replacing the time derivatives of the wave func-
tion ψ and its conjugate ψ∗in Eq. (D15), respectively,
by the right hand side of Eq. (D14) and its conjugate
we obtain
∂ρ(x, x′, t)
∂t
= i
ϵ
 1
|A|
Z
exp

−H(x, x′′)ϵ
ℏ

ρ(x′′, x′, t)dx′′ −ρ(x, x′, t)

−i
ϵ
 1
|A|
Z
exp

−H(x′, x′′)ϵ
ℏ

ρ(x, x′′, t)dx′′ −ρ(x, x′, t)

.
(D16)
Clearly, the terms ρ(x, x′, t) in the right hand side
cancel out, and we can write Eq. (D16) in compact
form as
∂ρ
∂t = i
ϵ [(K ∗ρ) −(ρ ∗K)] ,
(D17)
where we have introduced the kernel
K(x, x′) =
1
|A| exp

−H(x, x′)ϵ
ℏ

,
(D18)
and the convolutions
[K ∗ρ] (x, x′, t) =
1
|A|
R
exp
h
−H(x,x′′)ϵ
ℏ
i
ρ(x′′, x′, t)dx′′,
(D19)
[ρ ∗K] (x′, x, t) =
1
|A|
R
exp
h
−H(x′,x′′)ϵ
ℏ
i
ρ(x, x′′, t)dx′′.
(D20)
to represent, respectively, the ﬁrst and second inte-
grals in the right hand side of Eq. (D16).
Notice
that the integration variables in (K ∗ρ) and (ρ ∗K)
are, respectively, the ﬁrst and second arguments of
ρ, which yields the analogous of left and right matrix
multiplication.
3.
Particle in an electromagnetic ﬁeld via
asymmetric real kernels
a.
Prelude: Hermitian kernels via complex Hamiltonian
functions
The Schr¨odinger equation of a particle of charge e
interacting with an electromagnetic ﬁeld can be writ-
ten as
iℏ∂ψ(x, t)
∂t
= −ℏ2
2m

∇−i e
ℏcA
2
ψ(x, t)
+ eV (x, t)ψ(x, t),
(D21)
where x denotes the position vector in three dimen-
sional space, while V and A denote the scalar and
vector ﬁelds respectively. Notice that the Hamilto-
nian associated to Eq. (D21) now contains an imagi-
nary part given by the terms linear in A arising from
the expansion of (∇−ieA/ℏc)2ψ(x, t).
Equation (D21) can be derived via the path inte-
gral formulation from the extension of Eq. (D22) to
three-dimensional space (i.e. by doing the substitu-


## Page 52


52
tion x →x)
ψ(xℓ+1, t+ϵ) =
1
AEM
Z
exp
 i
ℏSEM(xℓ+1, xℓ)

ψ(xℓ, t)d3xℓ,
(D22)
with action
SEM(xℓ+1, xℓ) = mϵ
2
xℓ+1 −xℓ
ϵ
2
+ eϵ
c
xℓ+1 −xℓ
ϵ

· A
xℓ+1 + xℓ
2
, t

−ϵV
xℓ+1 + xℓ
2
, t

,
(D23)
and
A →AEM ≡(i2πℏϵ/m)3/2;
(D24)
here we are using a midpoint discretization for the
action.
As in the previous section, it is possible to derive
Eq. (D21) by doing a replacement similar to that in
Eq. (D12), i.e.
1
AEM
exp
 i
ℏSEM(x, x′)

→
1
|AEM| exp
h
−ϵ
ℏ
e
HEM(x, x′)
i
,
(D25)
but with a complex Hamiltonian function
e
HEM(x, x′) = m
2
x −x′
ϵ
2
+ V
x + x′
2
, t

−ie
c
x −x′
ϵ

· A
x + x′
2
, t

.
(D26)
As with Eq. (D12), this corresponds to a Wick rota-
tion ϵ →−iϵ. We can recognize that the real part
is the three-dimensional version of the Hamiltonian
function deﬁned in Eq. (D11).
We could think of
HEM as a Hamiltonian function with a complex in-
teraction energy whose real and imaginary parts cor-
respond to the electric and magnetic ﬁelds, respec-
tively. This seems similar to writing the electromag-
netic ﬁeld as E + iB which allows to write Maxwell’s
equations in compact form (see e.g. Eq. (7.10) in
Ref. [192]).
As in the previous section, we can derive Eq. (D21)
from an equation analogous to Eq. (D14), i.e.
ϵ∂ψ(xℓ+1, t)
∂t
= i

1
|AEM|
Z
exp
h
−ϵ
ℏ
e
HEM(xℓ+1, xℓ)
i
ψ(xℓ, t)d3xℓ−ψ(xℓ+1, t)

.
(D27)
Indeed, as in the previous section, the Gaussian factor
in the complex kernel (see Eqs.(D24) and (D26))
C(x, x′) = exp
h
−ϵ
ℏ
e
HEM(x, x′)
i
/|AEM|,
(D28)
associated to the kinetic term in Eq. (D26) al-
lows us to expand the other factors in the in-
tegral
in
Eq.
(D27)
around
xℓ+1
up
to
sec-
ond order in |xℓ+1 −xℓ| or to ﬁrst order in
ϵ.
More precisely,
by introducing the variable


## Page 53


53
u = xℓ+1 −xℓ,
so
(xℓ+1 + xℓ)/2 = xℓ+1 −u/2
as
well as xℓ= xℓ+1 −u, and doing x = xℓ+1, x′ = xℓ
to avoid cluttering the equations with indexes, we can
write
[C ∗ψ](x, t) =
1
|AEM|
Z
exp

−mu2
2ℏϵ

f(x, u, t)

ψ(x, t) −u · ∇ψ(x, t) + 1
2u · Hψ(x, t) · u

+ O(ϵ2), (D29)
where the convolution C ∗ψ denotes the integral in
the right hand side of Eq. (D27), Hψ stands for the
Hessian or matrix of second derivatives of ψ. Fur-
thermore, the function
f(x, u, t) =

1 −ϵ
ℏV (x, t) + i e
ℏcu · A(x, t) −i e
2ℏcu · ∇A(x, t) · u −1
2
h e
ℏcu · A(x, t)
i2
,
(D30)
is the expansion up to ﬁrst order in ϵ or second order
in u of the exponential factors in the complex ker-
nel C, which correspond to the interaction terms in
Eq. (D26), i.e. those containing V and A.
Taking into account that the ﬁrst two moments
of u are ⟨uj⟩u = 0 and ⟨ujuk⟩u = δjkℏϵ/m, where
⟨·⟩u refers to the average taken with the Gaussian
exp(−mu2/2ℏϵ)/|AEM|, and that terms containing
ϵu2 and u3 or higher can be neglected, the integral
in Eq. (D29) yields
[C ∗ψ](x, t) =

1 −ϵ
ℏV

ψ + ℏϵ
2m∇2ψ −i eϵ
mcA · ∇ψ −i eϵ
2mc∇· Aψ −
e2ϵ
2ℏmc2 A2ψ
(D31)
Furthermore, taking into account that

∇−i e
ℏcA
2
ψ =∇2ψ −
 e
ℏc
2
A2ψ−
i e
ℏc [2A · ∇ψ + (∇· A)ψ] ,
(D32)
we obtain
[C ∗ψ](x, t) = ψ(x, t) + ϵ
ℏ
 ℏ2
2m

∇−i e
ℏcA
2
ψ(x, t) −V (x, t)ψ(x, t)

+ O(ϵ2).
(D33)
So, we can indeed write the Schr¨odinger equation
Eq. (D21) as
ϵ∂ψ
∂t = i[C ∗ψ −ψ],
(D34)
which is the analogous of Eq. (D14). To see this, we
can replace C∗ψ in Eq. (D34) by the right hand side of
Eq. (D33), cancel out the ψ terms, and multiply the
remaining equation by iℏ/ϵ, which yields Eq. (D21).
By doing the same analysis that led from Eq. (D14)
to Eqs. (D16) and (D17) we get
∂ρ
∂t = i
ϵ[C ∗ρ −ρ ∗C] ≡i
ϵ[C, ρ].
(D35)
Notice, however, that contrary to the kernel K in
Eq. (D17), which is real and symmetric, the kernel


## Page 54


54
C in Eq. (D35) is still complex and asymmetric. In-
deed, from Eqs.(D26) and (D28) we can see that by
exchanging the two arguments of C we get
C(x′, x) = [C(x, x′)]∗,
(D36)
which, considering C as a matrix, also shows that C
is Hermitean. We could also see that C is Hermitian
by writing Eq. (D28) as C = Ks + iKa with
Ks(x, x′) =
1
|AEM| exp

−m(x −x′)2
2ℏϵ
−ϵ
ℏV
x + x′
2
, t

cos
 e
ℏc (x −x′) · A
x + x′
2
, t

,
(D37)
Ka(x, x′) =
1
|AEM| exp

−m(x −x′)2
2ℏϵ
−ϵ
ℏV
x + x′
2
, t

sin
 e
ℏc (x −x′) · A
x + x′
2
, t

,
(D38)
which are clearly symmetric and antisymmetric, re-
spectively, due to the symmetry properties of the cos-
inusoidal and sinusoidal functions.
b.
Postlude: real asymmetric kernels via real
Hamiltonian functions
Since the kernel C deﬁned in Eq. (D28) is Hermitian
(see Eq. (D36)), Eq. (D35) has the same structure of
Eq. (1). So, as described in Sec. IV A (see also remark
1 therein), we can write Eq. (D35) as a pair of real
equations in terms of a real kernel K = Ks + Ka,
which in this case is given by the sum of the right
hand sides of Eqs. (D37) and (D38),
K(x, x′) =
1
|AEM| exp

−m(x −x′)2
2ℏϵ
−ϵ
ℏV
x + x′
2
, t

[cos z + sin z],
(D39)
where
z = ϵ
ℏ
e
c
x −x′
ϵ

· A
x + x′
2
, t

.
(D40)
Due to the very sharp Gaussian factor (since
ϵ →0), we can expand the sinusoidal and cosinusoidal
functions up to second order in their argument since
the rest gives contributions of order higher than ϵ.
Now, up to second order we have
cos z + sin z = exp(z −z2) + O(z3).
(D41)
Eqs. (D37)-(D40) shows that, even in the case
of a charged particle in an electromagnetic ﬁeld,
whose Hamiltonian operator is complex (and so non-
stoquastic), can be thought of as arising from a
real kernel K = Ks + Ka. More precisely, following
Sec. IV A the corresponding von Neumann equation
can be understood as a pair of real matrix equations
∂PA
∂t
= −1
ϵ [Ka, PA] + 1
ϵ [Ks, PB],
(D42)
∂PB
∂t
= −1
ϵ [Ka, PB] −1
ϵ [Ks, PA],
(D43)
where the two probability matrices satisfy PA = P,
PB = P T , and ρ = (P + P T )/2 + i(P −P T )/2. As
we argue later these equations can be interpreted in
probabilistic terms.
However, the term z2 in Eq. (D41) leads via
Eq. (D40) to a term with a quadratic factor (ϵ/ℏ)2,
which prevents us from writing K ∝exp (−ϵHEM/ℏ)
with a Hamiltonian function HEM independent of ϵ
and ℏ(cf. Eq. (D28)). It is possible to go around
this issue, though, by noticing that (remember that
u = x −x′, so (x + x′)/2 = x −u/2)

z2
u =
 e
ℏc
2 h
u · A

x −u
2 , t
i2
u
= ϵ
ℏ
e2
mc2 [A(x, t)]2 + O(ϵ2),
(D44)


## Page 55


55
where ⟨·⟩u refers to the average taken with the Gaus-
sian exp(−mu2/2ℏϵ)/|AEM|, and we have used the
results ⟨uj⟩u = 0 and ⟨ujuk⟩u = (ℏϵ/m)δjk.
Since the ﬁrst term in the right hand side of
Eq. (D44) is already of order ϵ, we can safely replace
z2 →ϵ
ℏ
e2
mc2

A
x + x′
2
, t
2
+ O(ϵ2),
(D45)
so
e−z2 →exp

−ϵ
ℏ
e2
mc2 A2

,
(D46)
in Eq. (D41), since when we expand in u only the
term independent of u remains as the other terms in
the expansion lead to terms of higher order in ϵ.
So, we can indeed write the asymmetric real kernel
K = Ks + Ka in Eq. (D39) associated to the complex
kernel C in Eq. (D28) as
K(x, x′) =
1
|AEM| exp
h
−ϵ
ℏHEM(x, x′)
i
(D47)
where the real electromagnetic Hamiltonian function
(with no tilde) is given by
HEM(x, x′) = m
2
x −x′
ϵ
2
+ V
x + x′
2
, t

−e
c
x −x′
ϵ

· A
x + x′
2
, t

+ e2
mc2

A
x + x′
2
, t
2
(D48)
It is no completely clear at this point, though, how
to interpret HEM deﬁned in Eq. (D48) nor the real
kernel K deﬁned in Eq. (D47). It seems to suggests
a probabilistic interpretation of electromagnetic phe-
nomena. We leave this for future work.
Appendix E: Eﬀective kernels with negative
entries
The derivation of genuine quantum-like dynamics
in the main text (see, e.g., Secs. VI C and VII B) was
built on factors Fℓwith non-negative entries. In prin-
ciple, quantum mechanics does not have this restric-
tion.
Here we will argue that our approach is not
restricted to factors with non-negative entries either.
We will discuss the well-known example of a non-
relativistic atom in a radiation ﬁeld.
This is an
inﬁnite-dimensional quantum system that, following
the approach discussed in Sec. IV and Appendix D,
can originally be described by factors with non-
negative entries. After a standard truncation of the
original model to its ﬁrst two energy levels, however,
it turns into an eﬀective two-dimensional system de-
scribed by factors with negative entries. The latter is
known as a two-level atom interacting with a coher-
ent radiation ﬁeld [193] (see Sec. 15.3 therein). Nev-
ertheless, it is the former system which is actually
implemented in the lab, where the experimenter has
to make sure certain near resonance conditions are
met for the eﬀective two-dimensional model to be a
good approximation of the actual system.
This discussion is restricted to non-relativistic
quantum mechanics. In relativistic quantum mechan-
ics there may be some intrinsic sources of negative
numbers in probabilistic expressions. We leave the
study of relativistic quantum mechanics for future
work.
Consider therefore the Hamiltonian of an atom
modelled as an electron, described by the momen-
tum operator iℏ∇r, moving in a potential ﬁeld V (r)
produced by the nucleus,
H0 = −ℏ2
2m∇2
r + V (r) =
∞
X
n=0
En |n⟩⟨n| .
(E1)
In the second equality we have expanded the Hamil-
tonian in terms of its eigenvalues En and its eigen-
vectors |n⟩, where n ∈Z, n ≥0.
Now consider a perturbation
U(r, t) = er · E(t) = er · E0 cos(ωt),
(E2)
where E(t) = E0 cos(ωt) is an oscillating electric ﬁeld
with frequency ω and amplitude E0. The perturbed
Hamiltonian, H = H0 + U, can be derived via a path
integral with Lagrangian
L = m
2 ˙r −V (r) −U(r, t).
(E3)
Following the approach discussed in Sec. IV and
Appendix D, we can also derive H via a real non-
negative kernel
Kϵ(r′, r) = e−ϵH(r′,r)/ℏ≥0,
(E4)
where the Hamiltonian function
H(r′, r) = m
2
r′ −r
ϵ
2
+V
|r′ + r|
2

+U(t), (E5)
is essentially the Wick rotation ϵ →−iϵ of the La-
grangian L in Eq. (E3) (appart from an irrelevant
global minus sign).


## Page 56


56
We will now see that, after a standard truncation
of the full Hamiltonian H = H0 + U (see Eqs. (E1)
and (E2)) into an eﬀective two-level system, we lose
the equivalence with the positive kernel given by
Eqs. (E4) and (E5).
Indeed, in the derivation of
the Hamiltonian of a two-level atom it is usually as-
sumed that the perturbation deﬁned in Eq. (E2) is
near resonance with two relevant energy levels of the
Hamiltonian H0, say E0 and E1, i.e. |ω −ω0| ≪ω0,
where ℏω0 = E1 −E0. In this case, it is usually as-
sumed that only the dynamics of these two energy
levels matter. So, we can write
H =E0 |0⟩⟨0| + E1 |1⟩⟨1| + U01 (|0⟩⟨1| + |1⟩⟨0|)
+ HR,
(E6)
where the ﬁrst three terms in the right hand side of
Eq. (E6) correspond to the transitions taking place
within the subspace spanned by {|0⟩, |1⟩}, and
HR =
∞
X
n=2
En |n⟩⟨n|
+
∞
X
m=0
∞
X
n>m,n̸=0,1
(Umn |m⟩⟨n| + Unm |n⟩⟨m|) ,
(E7)
collects all the remaining transitions. Here we have
written
Umn = U ∗
nm = ⟨m| U(t) |n⟩,
(E8)
for m, n ∈Z, m, n ≥0.
For simplicity, we are
restricting here to the case where U01 = U ∗
01 and
U00 = U11 = 0 [193] (see Sec. 15.3 therein); this ex-
plains the form of Eq. (E6).
At this point it is argued that we can neglect HR
since the system is near resonance. This yields the
eﬀective two-level Hamiltonian
Heﬀ= E1I(01) −ℏω0
2 σ(01)
Z
+ D cos(ωt)σ01
X ,
(E9)
where E = (E0 + E1)/2, D = ⟨0| r · E0 |1⟩, and
1I(01) = |0⟩⟨0| + |1⟩⟨1| ,
(E10)
σ(01)
X
= |0⟩⟨1| + |1⟩⟨0| ,
(E11)
σ(01)
Z
= |0⟩⟨0| −|1⟩⟨1| .
(E12)
If we now try to write this as a real kernel in the
way we did in Sec. IV and Appendix D
Feﬀ= 1I −ϵJeﬀ,
(E13)
with Jeﬀ= Heﬀ/ℏ, we end up with oﬀ-diagonal neg-
ative entries due to the factor cos(ωt) accompanying
σX in Eq. (E9). So, the full Hamiltonian H = H0+U
in Eq. (E6) can be represented in terms of the real
positive kernel given by Eqs. (E4) and (E5), but the
truncated eﬀective Hamiltonian Heﬀin Eq. (E9) can-
not. What happened? The eﬀective factor
Feﬀ= F −R
(E14)
in Eq. (E13) can be interpreted as the full factor F =
1I −ϵH/ℏassociated to kernel Kϵ (see Eqs. (E4) and
(E6)), which has only positive entries, relative to the
reference factor R = −ϵHR/ℏ.
Key in this example is the neglect of part of the
original system, which is then completely forgot. If
we keep in mind this fact, we can interpret the nega-
tive entries as indicators that we are describing prob-
abilistic expressions—e.g., probability distributions,
transition probabilities, or factors—relative to a sim-
ilar reference probabilistic expression [194]. The pres-
ence of negative numbers in general probabilistic ex-
pressions do not need to be an issue. It is in principle
possible to provide an operational interpretation to
linear algebra manipulations of probabilistic expres-
sions without the usual restrictions that all numbers
involved must be in the interval [0, 1] nor that all
probabilistic expressions need be properly normal-
ized [194–196].
Some of these ideas have recently
led [197] to classical quantum-inspired algorithms for
stochastic simulation that require much less memory
than the best classical algorithms known to date.
Appendix F: Phase-less quantum-like
formulation of Markov processes
Here we show in more detail that standard Markov
processes can be written as imaginary-time quantum
mechanics, but in terms of phaseless wave functions.
1.
Time-symmetric evolution equations
To begin let us notice that using Bayes rule in
Eq. (39) we can change P−
ℓin Eq. (41) for P+
ℓ, i.e.
Kℓ(xℓ, xℓ+1) =P+
ℓ(xℓ+1|xℓ)
s
pℓ(xℓ)
pℓ+1(xℓ+1)
=P+
ℓ(xℓ+1|xℓ)
θℓ(xℓ)
θℓ+1(xℓ+1),
(F1)
which is the analogous of Eq.
(2.12) in Ref. [92],
where Kℓhere plays the role of h there. So, since
pℓ+1(xℓ+1) =
R
P+
ℓ(xℓ+1|xℓ)pℓ(xℓ)dxℓ, we have
θℓ+1(xℓ+1) =
Z
Kℓ(xℓ, xℓ+1)θℓ(xℓ)dxℓ.
(F2)
which has the same structure of Eq. (D22) in
Sec. IV B 2 (see also Eq. (D14)); indeed, after car-
rying out a Wick rotation (t →it) and restricting


## Page 57


57
to (real) Wick-rotated wave functions with no phase,
i.e. ψℓ(xℓ) =
p
pℓ(xℓ), Eq. (D22) can be considered
as an instance of Eq. (F2).
Notice that, like the real kernels we obtained
in Sec. IV (see e.g.
Eqs. (20) and (28)), the
kernel Ki above, which is deﬁned in Eq. (41),
is in general not normalized.
Indeed, except for
special cases like P+
i (xℓ+1|xℓ) = P−
ℓ(xℓ|xℓ+1), when
Kℓ(xℓ, xℓ+1) = P+
ℓ(xℓ+1|xℓ) is actually a probability
distribution, the integral of the square root of the
product of two diﬀerent probability distributions is
not one in general. We will discuss this further in Ap-
pendix F 2, where we will also show there is a close
analogy with quantum mechanics, more speciﬁcally
with the ﬁnal remark in Sec. IV B 2.
Let us ﬁrst notice that by changing P−
ℓin Eq. (41)
for P+
ℓwe obtain
Kℓ(xℓ, xℓ+1) =P−
ℓ(xℓ+1|xℓ)
s
pℓ+1(xℓ+1)
pℓ(xℓ)
=P−
ℓ(xℓ|xℓ+1)θ∗
ℓ+1(xℓ+1)
θ∗
ℓ(xℓ)
,
(F3)
where we have introduced the asterisc notation θ∗
ℓ
just to emphasize that this equation is related to
the backward transition probability P−
ℓ. Indeed, this
leads to the the reversed version of Eq. (F2), i.e.
θ∗
ℓ(xℓ) =
Z
Kℓ(xℓ, xℓ+1)θ∗
ℓ+1(xℓ+1)dxℓ,
(F4)
which is the analogous of Eq. (2.11) in Ref. [92].
In this particular case we have θℓ= θ∗
ℓ, so we can
equally write pℓ(x) = θ2
ℓ(x) = θ∗
ℓ(x)θℓ(x). We will
emphasize the latter, however, which can be inter-
preted as the product of the solutions of an initial
value problem θt(x) and a ﬁnal value problem θ∗
ℓ(x),
much as the situation in Eqs. (49), (57) and (58).
2.
Time-symmetric kernels are not normalized
To see this analogy more closely, let us work with
the continuous time version of Eq. (F1), i.e. let us
change ℓ→t and ℓ+ 1 →t + ϵ with ϵ →0. Further-
more, since ϵ is very small P+
t+ϵ|t(x′|x) is very close to
a Dirac delta δ(x′ −x), so we can expand the fraction
θt(x)/θt+ϵ(x′) around t and x = x′ −ξ to yield
Z
Kt(x, x′)dx = 1 −ϵ
( ˙θt(x)
θt(x) + D+
t (x)
2
θ′′
t (x)
θt(x) + b+
t (x)θ′
t(x)
θt(x) −D+
t (x)
θ′
t(x)
θt(x)
2)
+ O(ϵ2),
(F5)
where
b+
t (x) = lim
ϵ→0
1
ϵ
Z
ξP+
t+ϵ|t(x + ξ|x)dξ,
(F6)
D+
t (x) = lim
ϵ→0
1
ϵ
Z
ξ2P+
t+ϵ|t(x + ξ|x)dξ,
(F7)
are the forward drift and difussion terms respectively;
here we are representing derivatives with respect to
x and t with prime and dot operators respectively.
Let us now consider the special case where the
diﬀusion coeﬃceint D+
t (x) = D
is constant and
the forward drift satisﬁes b+
t (x) = Dθ′
t(x)/θt(x) (cf.
Eq. (2.12’) in Ref. [92]; notice the prime), which
will be motivated and further discussed below in Ap-
pendix F 3. In this special case the last two terms in
Eq. (F5) cancel out and we get
Z
Kt(x, x′)dx = 1 −ϵVt(x)/D,
(F8)
where we have deﬁned the function
Vt(x) = D
˙θt(x)
θt(x) + D2
2
θ′′
t (x)
θt(x) ,
(F9)
which can be rewritten as
D ˙θt(x) = −D2
2 θ′′
t (x) + Vt(x)θt(x).
(F10)
Eq.
(F10)
is
the
exact
analogous
of
the
(ad-
joint) imaginary-time Schr¨odinger equation (see e.g.
Eqs. (2.1) and (2.17) in Ref. [92]), and similar also to
Eq. (24) in the ﬁnal remark of Sec. IV B 2.
3.
Future-past symmetry and quantum-like
Markov processes
Consider a Markov process with distribution P,
such that the joint distribution of the past and fu-
ture states, x′ and x′′ respectively, conditioned on
the present state x is symmetric, i.e.
P+
t+ϵ|t(x′′|x)P−
t−ϵ|t(x′|x) = P+
t+ϵ|t(x′|x)P−
t−ϵ|t(x′′|x).
(F11)
Assume such a distribution can be written as the sym-
metric part of a generic Markov process Q, i.e.


## Page 58


58
P+
t+ϵ|t(x′′|x)P−
t−ϵ|t(x′|x) = 1
2
h
Q+
t+ϵ|t(x′′|x)Q−
t−ϵ|t(x′|x) + Q+
t+ϵ|t(x′|x)Q−
t−ϵ|t(x′′|x)
i
,
(F12)
where Q+ and Q−refer to the corresponding forward
and backward transition probabilities of the generic
Markov process. Notice the exchange of x′ and x′′ in
the two terms in the right hand side.
Marginalizing Eq. (F12) over x′ we get
P+
t+ϵ|t(x′′|x) = 1
2
h
Q+
t+ϵ|t(x′′|x) + Q−
t−ϵ|t(x′′|x)
i
,
(F13)
and marginalizing over Eq. (F12) over x′ instead we
get
P−
t−ϵ|t(x′|x) = P+
t+ϵ|t(x′|x).
(F14)
Using Eqs. (F6) and (F13) we see that
b+
t (x) = 1
2

c+
t (x) −c−
t (x)

,
(F15)
where
c+
t (x) = lim
ϵ→0
1
ϵ
Z
(x′ −x)Q+
t+ϵ|t(x′|x)dx′,(F16)
c−
t (x) = lim
ϵ→0
1
ϵ
Z
(x −x′)Q−
t−ϵ|t(x′|x)dx′,(F17)
are the forward and backward drifts corresponding
to Markov process Q. It is known that the diﬀerence
between forward and backward drifts satisfy (see e.g.
Eq. (30) in Ref [61, 62] and references therein).
c+
t (x) −c−
t (x) = Dq′
t(x)
qt(x),
(F18)
where qt(x) is the single variable marginal associated
to the generic Markov process described by Q+ and
Q−, and q′
t(x) its derivative with respect to x.
In Eq. (F18) we can replace qt(x) by the sin-
gle variable marginal pt(x) corresponding to the
process described by distributions P+ and P−, up
to a correction that vanishes when ϵ →0, i.e.
pt(x) = qt(x) + O(ϵ). Indeed, multiplying Eq. (F13)
by qt(x) and using Bayes rule to invert Q+ and Q−
we get
P+
t+ϵ|t(x′|x)qt(x) = 1
2
h
Q−
t|t+ϵ(x|x′)qt+ϵ(x′) + Q+
t|t−ϵ(x|x′)qt−ϵ(x′)
i
.
(F19)
By expanding in t the functions qt−ϵ(x′) around t + ϵ
and Q+
t|t−ϵ(x|x′) around t + 2ϵ we obtain
P+
t+ϵ|t(x′|x)qt(x) = 1
2
h
Q−
t|t+ϵ(x|x′) + Q+
t+ϵ|t(x|x′)
i
qt+ϵ(x′) + O(ϵ) = P−
t|t+ϵ(x|x′)qt+ϵ(x′) + O(ϵ),
(F20)
which is Bayes rule for P+ and P−up to an error
term of order ϵ.
So, replacing qt by pt in Eq. (F18), Eq. (F15) can
be written as
b+(x) = D
2
p′
t(x)
pt(x) = Dθ′
t(x)
θt(x),
(F21)
where θt(x) =
p
pt(x), which is the analogous of
Eq. (2.12’) in Ref. [92]. Notice also that Eq. (F14) im-
plies that the backward drift, obtained from Eq. (F6)
by replacing the integrand (x′ −x)P+
t+ϵ(x′|x) with
(x −x′)P−
t−ϵ(x′|x) (see Eqs. (F16) and (F17)), is
given by
b−
t (x) = −b+
t (x) = −Dθ∗′
t(x)/θ∗
t (x).
(F22)
(Cf. Eqs. (2.11’) and (2.12’) in Ref. [92].) Here we
have used θ∗
t instead of θt = θ∗
t to emphasize that
we are dealing with the backward process. Such a
distinction becomes relevant when we deal with cy-
cles rather than chains, since then a phase arises and
θt ̸= θ∗
t in general.


## Page 59


59
[1] F. J. Varela, E. Thompson, and E. Rosch, The em-
bodied mind: Cognitive science and human experi-
ence (revised edition). MIT press, 2017.
[2] G. M. D’Ariano, G. Chiribella, and P. Perinotti,
Quantum Theory from First Principles: An infor-
mational approach.
Cambridge University Press,
2017.
[3] C. Rovelli, “Relational quantum mechanics,” Int. J.
of Theor. Phys., vol. 35, p. 1637, 1996.
[4] L. Hardy, “Reconstructing quantum theory,” arXiv
preprint arXiv:1303.1538, 2013.
[5] M. S. Leifer and R. W. Spekkens, “Towards a for-
mulation of quantum theory as a causally neutral
theory of bayesian inference,” Physical Review A,
vol. 88, no. 5, p. 052130, 2013.
[6] ˇC. Brukner, “Quantum causality,” Nature Physics,
vol. 10, no. 4, pp. 259–263, 2014.
[7] B. Coecke and R. W. Spekkens, “Picturing clas-
sical and quantum bayesian inference,” Synthese,
vol. 186, no. 3, pp. 651–696, 2012.
[8] C. A. Fuchs and R. Schack, “Quantum-bayesian co-
herence,” Reviews of Modern Physics, vol. 85, no. 4,
p. 1693, 2013.
[9] P. Goyal, K. H. Knuth, and J. Skilling, “Origin of
complex quantum amplitudes and feynmans rules,”
Physical Review A, vol. 81, no. 2, p. 022109, 2010.
[10] N. D. Mermin, “What is quantum mechanics trying
to tell us?,” American journal of physics, vol. 66,
no. 9, pp. 753–767, 1998.
[11] D. Jennings and M. Leifer, “No return to classi-
cal reality,” Contemporary Physics, vol. 57, no. 1,
pp. 60–82, 2016.
[12] A. Zeilinger, “The message of the quantum,” Na-
ture, vol. 438, p. 743, 2005.
[13] N. D. Mermin, “Physics:
Qbism puts the scien-
tist back into science,” Nature, vol. 507, no. 7493,
pp. 421–423, 2014.
[14] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu,
J. Veness, M. G. Bellemare, A. Graves, M. Ried-
miller,
A. K. Fidjeland,
G. Ostrovski,
et al.,
“Human-level control through deep reinforcement
learning,” Nature, vol. 518, no. 7540, p. 529, 2015.
[15] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learn-
ing,” nature, vol. 521, no. 7553, p. 436, 2015.
[16] D. M. Losey, A. Stocco, J. A. Abernethy, and R. P.
Rao, “Navigating a 2d virtual world using direct
brain stimulation,” Frontiers in Robotics and AI,
vol. 3, p. 72, 2016.
[17] A. F. Salazar-Gomez, J. DelPreto, S. Gil, F. H.
Guenther, and D. Rus, “Correcting robot mistakes
in real time using eeg signals,” ICRA. IEEE, 2017.
[18] O. Cohen, M. Koppel, R. Malach, and D. Friedman,
“Controlling an avatar by thought using real-time
fMRI,” Journal of neural engineering, vol. 11, no. 3,
p. 035006, 2014.
[19] O. Cohen, S. Druon, S. Lengagne, A. Mendelsohn,
R. Malach, A. Kheddar, and D. Friedman, “fMRI
robotic embodiment: a pilot study,” in Biomedical
Robotics and Biomechatronics (BioRob), 2012 4th
IEEE RAS & EMBS International Conference on,
pp. 314–319, IEEE, 2012.
[20] C. Koch, M. Massimini, M. Boly, and G. Tononi,
“Neural correlates of consciousness: progress and
problems,” Nature Reviews Neuroscience, vol. 17,
no. 5, pp. 307–321, 2016.
[21] S. Dehaene, Consciousness and the brain: Decipher-
ing how the brain codes our thoughts. Penguin, 2014.
[22] Y.-Y. Tang, B. K. H¨olzel, and M. I. Posner, “The
neuroscience of mindfulness meditation,” Nature
Reviews Neuroscience, vol. 16, no. 4, pp. 213–225,
2015.
[23] R. Hanson, Buddha’s brain:
The practical neu-
roscience of happiness, love, and wisdom.
New
Harbinger Publications, 2009.
[24] F. Crick and C. Koch, “Towards a neurobiological
theory of consciousness,” in Seminars in the Neu-
rosciences, vol. 2, pp. 263–275, Saunders Scientiﬁc
Publications, 1990.
[25] M. Botvinick and J. Cohen, “Rubber hands feel-
touch that eyes see,” Nature, vol. 391, no. 6669,
p. 756, 1998.
[26] H. H. Ehrsson, C. Spence, and R. E. Passing-
ham, “That’s my hand! activity in premotor cor-
tex reﬂects feeling of ownership of a limb,” Science,
vol. 305, no. 5685, pp. 875–877, 2004.
[27] B. Lenggenhager,
T. Tadi,
T. Metzinger,
and
O. Blanke, “Video ergo sum:
manipulating bod-
ily self-consciousness,” Science, vol. 317, no. 5841,
pp. 1096–1099, 2007.
[28] H. H. Ehrsson, “The experimental induction of out-
of-body experiences,” Science, vol. 317, no. 5841,
pp. 1048–1048, 2007.
[29] O. Blanke and T. Metzinger, “Full-body illusions
and minimal phenomenal selfhood,” Trends in cog-
nitive sciences, vol. 13, no. 1, pp. 7–13, 2009.
[30] T. Metzinger, Being no one: The self-model theory
of subjectivity. mit Press, 2004.
[31] T. Metzinger, The ego tunnel: The science of the
mind and the myth of the self. Basic Books (AZ),
2009.
[32] S. Edelman, Computing the mind: How the mind
really works. Oxford University Press, 2008.
[33] F. Crick, Astonishing Hypothesis:
The Scientiﬁc
Search for the Soul. A Touchstone Book, Scribner,
1995.
[34] S. Fortunato, C. T. Bergstrom, K. B¨orner, J. A.
Evans, D. Helbing, S. Milojevi´c, A. M. Petersen,
F. Radicchi, R. Sinatra, B. Uzzi, A. Vespignani,
L. Waltman, D. Wang, and A.-L. Barab´asi, “Sci-
ence of science,” Science, vol. 359, no. 6379, 2018.
[35] L. Szilard, “t”Uber die entropieverminderung in
einem thermodynamischen system bei eingriﬀen in-
telligenter wesen,” Zeitschrift f¨ur Physik A Hadrons
and Nuclei, vol. 53, no. 11, pp. 840–856, 1929.
[36] N. Bohr, “The quantum of action and the de-
scription of nature,” Philosophical Writings of Niels
Bohr, vol. 1, pp. 92–101, 1929.
[37] J. Realpe-G´omez,
“Quantum theory as a self-
referential theory of inference,”
arXiv preprint
arXiv:1705.04307v1, 2017.
[38] Realpe-G´omez, “Cognitive modeling of ﬁrst-person
observers can explain quantum theory,” To appear,


## Page 60


60
2018.
[39] F. Schwabl,
Quantum mechanics. 3rd Edition.
Springer-Verlag, 2002.
[40] S. Toyabe, T. Sagawa, M. Ueda, E. Muneyuki,
and M. Sano,
“Experimental demonstration of
information-to-energy conversion and validation of
the generalized jarzynski equality,” Nature Physics,
vol. 6, no. 12, pp. 988–992, 2010.
[41] D. Radin, L. Michel, K. Galdamez, P. Wendland,
R. Rickenbach, and A. Delorme, “Consciousness
and the double-slit interference pattern: Six exper-
iments.,” Physics Essays, vol. 25, no. 2, 2012.
[42] A. A. Melnikov, H. P. Nautrup, M. Krenn, V. Dun-
jko, M. Tiersch, A. Zeilinger, and H. J. Briegel, “Ac-
tive learning machine learns to create new quantum
experiments,” Proceedings of the National Academy
of Sciences, p. 201714936, 2018.
[43] J. N. Tinsley,
M. I. Molodtsov,
R. Prevedel,
D. Wartmann, J. Espigul´e-Pons, M. Lauwers, and
A. Vaziri, “Direct detection of a single photon by
humans,” Nature Communications, vol. 7, 2016.
[44] O. Blanke and S. Arzy, “The out-of-body expe-
rience:
disturbed self-processing at the temporo-
parietal junction,”
The Neuroscientist,
vol. 11,
no. 1, pp. 16–24, 2005.
[45] P. A. Schilpp, G. Kurt, et al., “Albert einstein:
philosopher-scientist,” 1949.
[46] J. D. Watson, F. H. Crick, et al., “Molecular struc-
ture of nucleic acids,” Nature, vol. 171, no. 4356,
pp. 737–738, 1953.
[47] H. Leﬀand A. Rex, Maxwell’s Demon: Entropy,
Information, Computing. A. Hilger, 1990.
[48] E. P. Wigner, “Remarks on the mind-body ques-
tion,” in Philosophical Reﬂections and Syntheses,
pp. 247–260, Springer, 1995.
[49] J. Von Neumann,
Mathematical foundations of
quantum mechanics.
No. 2, Princeton university
press, 1955.
[50] D. Bohm and M. Edwards, “Changing conscious-
ness,” San Fran-cisco: Harper, 1991.
[51] R. Penrose, Shadows of the Mind, vol. 4. Oxford
University Press Oxford, 1994.
[52] R. Penrose, The emperor’s new mind: Concerning
computers, minds, and the laws of physics. Oxford
Paperbacks, 1999.
[53] S. Hameroﬀand R. Penrose, “Consciousness in the
universe: A review of the Orch ORtheory,” Physics
of life reviews, vol. 11, no. 1, pp. 39–78, 2014.
[54] B. M. Bennett, D. D. Hoﬀman, and C. Prakash,
Observer mechanics: A formal theory of perception.
Academic Press, 2014.
[55] C. Fields, D. D. Hoﬀman, C. Prakash, and M. Singh,
“Conscious agent networks: Formal analysis and ap-
plication to cognition,” Cognitive Systems Research,
vol. 47, pp. 186–213, 2018.
[56] C. Fields, “If physics is an information science, what
is an observer?,” Information, vol. 3, no. 1, pp. 92–
123, 2012.
[57] C. Fields, “Building the observer into the system:
Toward a realistic description of human interaction
with the world,” Systems, vol. 4, no. 4, p. 32, 2016.
[58] M.
P.
Mueller,
“Could
the
physical
world
be emergent instead of fundamental,
and why
should
we
ask?(full
version),”
arXiv
preprint
arXiv:1712.01826, 2017.
[59] O. E. R¨ossler, Endophysics: the world as an inter-
face. World scientiﬁc, 1998.
[60] D. McKeon and G. Ord, “Time reversal in stochas-
tic processes and the Dirac equation,” Physical re-
view letters, vol. 69, no. 1, p. 3, 1992.
[61] A. Caticha, “From entropic dynamics to quantum
theory,” in AIP Conference Proceedings, vol. 1193,
pp. 48–59, AIP, 2009.
[62] A. Caticha, “Entropic dynamics, time and quantum
theory,” Journal of Physics A: Mathematical and
Theoretical, vol. 44, no. 22, p. 225303, 2011.
[63] G. Gr¨ossing, “Sub-quantum thermodynamics as a
basis of emergent quantum mechanics,” Entropy,
vol. 12, no. 9, pp. 1975–2044, 2010.
[64] P. Goyal, “Information-geometric reconstruction of
quantum theory,” Phys. Rev. A, vol. 78, p. 052120,
Nov 2008.
[65] L. H. Kauﬀman, “Reﬂexivity and foundations of
physics,” in AIP Conference Proceedings, vol. 1316,
pp. 48–89, 2010.
[66] M. L. Dalla Chiara, “Logical self reference, set the-
oretical paradoxes and the measurement problem
in quantum mechanics,” Journal of Philosophical
Logic, vol. 6, no. 1, pp. 331–347, 1977.
[67] ˇC. Brukner, “Quantum complementarity and logical
indeterminacy,” Natural Computing, vol. 8, no. 3,
pp. 449–453, 2009.
[68] T. Breuer, “The impossibility of accurate state
self-measurements,” Philosophy of Science, vol. 62,
no. 2, pp. 197–214, 1995.
[69] C. S. Calude, “Algorithmic randomness, quantum
physics, and incompleteness,” in International Con-
ference on Machines, Computations, and Universal-
ity, pp. 1–17, Springer, 2004.
[70] D. Aerts, “Quantum structure in cognition,” Jour-
nal of Mathematical Psychology, vol. 53, no. 5,
pp. 314–348, 2009.
[71] A. Khrennikov, “Quantum-like modeling of cogni-
tion,” Frontiers in Physics, vol. 3, p. 77, 2015.
[72] P. D. Bruza, Z. Wang, and J. R. Busemeyer, “Quan-
tum cognition: a new theoretical approach to psy-
chology,” Trends in cognitive sciences, vol. 19, no. 7,
pp. 383–393, 2015.
[73] H. R. Maturana and F. J. Varela, Autopoiesis and
cognition:
The realization of the living, vol. 42.
Springer Science & Business Media, 1991.
[74] T. W. Deacon,
Incomplete nature:
How mind
emerged from matter.
WW Norton & Company,
2011.
[75] D. R. Hofstadter, G¨odel, Escher, Bach.
Vintage
Books New York, 1980.
[76] D. R. Hofstadter, I am a strange loop. Basic books,
2013.
[77] C. A. Fuchs, N. D. Mermin, and R. Schack, “An
introduction to qbism with an application to the
locality of quantum mechanics,” American Journal
of Physics, vol. 82, no. 8, pp. 749–754, 2014.
[78] C. Rovelli, “Relative information at the foundation
of physics,” in It From Bit or Bit From It?, pp. 79–
86, Springer, 2015.
[79] C.
Brukner,
“A
no-go
theorem
for
observer-independent
facts,”
arXiv
preprint
arXiv:1804.00749, 2018.


## Page 61


61
[80] G.
Chiribella,
“Agents,
subsystems,
and
the
conservation
of
information,”
arXiv
preprint
arXiv:1804.01943, 2018.
[81] J. Winn, “Causality with gates,” in Artiﬁcial Intel-
ligence and Statistics, pp. 1314–1322, 2012.
[82] J. Pearl, Causality.
Cambridge university press,
2009.
[83] C. J. Wood and R. W. Spekkens, “The lesson of
causal discovery algorithms for quantum correla-
tions: Causal explanations of bell-inequality viola-
tions require ﬁne-tuning,” New Journal of Physics,
vol. 17, no. 3, p. 033002, 2015.
[84] R. W. Spekkens, “Quasi-quantization: classical sta-
tistical theories with an epistemic restriction,” in
Quantum Theory: Informational Foundations and
Foils, pp. 83–135, Springer, 2016.
[85] S. D. Bartlett, T. Rudolph, and R. W. Spekkens,
“Reconstruction of gaussian quantum mechanics
from liouville mechanics with an epistemic restric-
tion,” Physical Review A, vol. 86, no. 1, p. 012103,
2012.
[86] R. W. Spekkens, “Evidence for the epistemic view
of quantum states: A toy theory,” Physical Review
A, vol. 75, no. 3, p. 032110, 2007.
[87] J. Maxwell, Theory of Heat. Green & Co., Long-
mans, London, 1871.
[88] R. Landauer, “Dissipation and heat generation in
the computing,” IBM J. Res. Develop, vol. 5,
pp. 183–191, 1961.
[89] Wikipedia, “Quine (computing) — Wikipedia, The
Free Encyclopedia,” 2017. [Online; accessed 1-June-
2017 ].
[90] M. Sipser, Introduction to the Theory of Computa-
tion, vol. 2. Thomson Course Technology Boston,
2006.
[91] R. P. Feynman, “Space-time approach to non-
relativistic quantum mechanics,” Rev. Mod. Phys.,
vol. 20, pp. 367–387, Apr 1948.
[92] J. C. Zambrini, “Euclidean quantum mechanics,”
Phys. Rev. A, vol. 35, pp. 3631–3649, May 1987.
[93] J. Zambrini, “Stochastic mechanics according to
E. Schr¨odinger,” Physical review A, vol. 33, no. 3,
p. 1532, 1986.
[94] J.-C. Zambrini, “Variational processes and stochas-
tic versions of mechanics,” Journal of Mathematical
Physics, vol. 27, no. 9, pp. 2307–2330, 1986.
[95] E. T. Jaynes, Probability theory: the logic of science.
Cambridge university press, 2003.
[96] S. Press´e, K. Ghosh, J. Lee, and K. A. Dill, “Prin-
ciples of maximum entropy and maximum caliber
in statistical physics,” Reviews of Modern Physics,
vol. 85, no. 3, p. 1115, 2013.
[97] M.
Mezard
and
A.
Montanari,
Information,
Physics, and Computation. Oxford Graduate Texts,
Oxford University Press, USA, 2009.
[98] E. Schr¨odinger, ¨Uber die umkehrung der naturge-
setze. Verlag Akademie der wissenschaften in kom-
mission bei Walter de Gruyter u. Company, 1931.
[99] E.
Schr¨odinger,
“Sur
la
th´eorie
relativiste
de
l´electron et linterpr´etation de la m´ecanique quan-
tique,” Ann. Inst. H. Poincar´e, vol. 2, no. 4,
pp. 269–310, 1932.
[100] Y. Weiss, “Correctness of local probability propaga-
tion in graphical models with loops,” Neural Com-
putation, vol. 12, pp. 1–41, 2000.
[101] B. Reznik and Y. Aharonov, “Time-symmetric for-
mulation of quantum mechanics,” Physical Review
A, vol. 52, no. 4, p. 2538, 1995.
[102] Y. Aharonov, S. Popescu, and J. Tollaksen, “A
time-symmetric formulation of quantum mechan-
ics,” Physics today, vol. 63, no. 11, p. 27, 2010.
[103] G. Pezzulo, G. Baldassarre, M. V. Butz, C. Castel-
franchi, and J. Hoﬀmann, “From actions to goals
and vice-versa: Theoretical analysis and models of
the ideomotor principle and tote,” in Workshop on
Anticipatory Behavior in Adaptive Learning Sys-
tems, pp. 73–93, Springer, 2006.
[104] D. D. Hoﬀman and C. Prakash, “Objects of con-
sciousness,” Frontiers in Psychology, vol. 5, p. 577,
2014.
[105] P. Spirtes, C. N. Glymour, and R. Scheines, Causa-
tion, prediction, and search. Springer-Verlag, 1993.
[106] H. v. Foerster, “Observing systems,” Seaside, CA:
Intersystems, 1981.
[107] L. H. Kauﬀman,
“Cybernetics,
reﬂexivity and
second-order science,” Constructivist Foundations,
vol. 11, no. 3, pp. 489–504, 2016.
[108] G. Aad, T. Abajyan, B. Abbott, J. Abdallah,
S. A. Khalek, A. Abdelalim, O. Abdinov, R. Aben,
B. Abi, M. Abolins, et al., “Observation of a new
particle in the search for the standard model higgs
boson with the atlas detector at the lhc,” Physics
Letters B, vol. 716, no. 1, pp. 1–29, 2012.
[109] S. Chatrchyan, V. Khachatryan, A. M. Sirunyan,
A. Tumasyan, W. Adam, E. Aguilo, T. Bergauer,
M. Dragicevic, J. Er¨o, C. Fabjan, et al., “Obser-
vation of a new boson at a mass of 125 gev with
the cms experiment at the lhc,” Physics Letters B,
vol. 716, no. 1, pp. 30–61, 2012.
[110] D. Koller and N. Friedman, Probabilistic Graphical
Models: Principles and Techniques. Adaptive Com-
putation and Machine Learning, Mit Press, 2009.
[111] F. Kschischang, B. Frey, and H. Loeliger, “Fac-
tor graphs and the sum-product algorithm,” IEEE
Transaction on Information Theory, vol. 47, no. 2,
pp. 498–519, 2001.
[112] K. Svozil, “Evolution by permutation,” in Physical
(A) Causality, pp. 51–57, Springer, 2018.
[113] R. W. Spekkens, “The paradigm of kinematics
and dynamics must yield to causal structure,” in
Questioning the Foundations of Physics, pp. 5–16,
Springer, 2015.
[114] E. Madelung, “Quantentheorie in hydrodynamis-
cher form,” Zeitschrift f¨ur Physik A Hadrons and
Nuclei, vol. 40, no. 3, pp. 322–326, 1927.
[115] T.
C.
Wallstrom,
“Inequivalence
between
the
schr¨odinger equation and the madelung hydrody-
namic equations,” Phys. Rev. A, vol. 49, pp. 1613–
1617, Mar 1994.
[116] C. Moore and S. Mertens, The nature of computa-
tion. OUP Oxford, 2011.
[117] K. G¨odel, “¨Uber formal unentscheidbare s¨atze der
principia mathematica und verwandter systeme i,”
Monatshefte f¨ur mathematik und physik, vol. 38,
no. 1, pp. 173–198, 1931.
[118] T.
W.
Deacon,
“Reciprocal
linkage
between
self-organizing
processes
is
suﬃcient
for
self-
reproduction and evolvability,” Biological Theory,


## Page 62


62
vol. 1, no. 2, pp. 136–149, 2006.
[119] J. v. Neumann and A. W. Burks, “Theory of self-
reproducing automata,” 1966.
[120] F. Hamzei, M.-S. Vry, D. Saur, V. Glauche, M. Ho-
eren, I. Mader, C. Weiller, and M. Rijntjes, “The
dual-loop model and the human mirror neuron
system: an exploratory combined fMRI and DTI
study of the inferior frontal gyrus,” Cerebral Cor-
tex, vol. 26, no. 5, pp. 2215–2224, 2016.
[121] V. S. Ramachandran,
“The neurology of self-
awareness,” The Edge, 2007.
[122] R. E. Kass, “Statistical inference: The big picture,”
Statistical science: a review journal of the Institute
of Mathematical Statistics, vol. 26, no. 1, p. 1, 2011.
[123] A. M. Turing, “On computable numbers, with an
application to the entscheidungsproblem,” Proceed-
ings of the London mathematical society, vol. 2,
no. 1, pp. 230–265, 1937.
[124] S. Dehaene, H. Lau, and S. Kouider, “What is con-
sciousness, and could machines have it?,” Science,
vol. 358, no. 6362, pp. 486–492, 2017.
[125] M. L. Sch¨olvinck, C. Howarth, and D. Attwell, “The
cortical energy needed for conscious perception,”
Neuroimage, vol. 40, no. 4, pp. 1460–1468, 2008.
[126] S. Hecht, S. Shlaer, and M. H. Pirenne, “Energy,
quanta, and vision,” The Journal of general physi-
ology, vol. 25, no. 6, pp. 819–840, 1942.
[127] R. M. Holmes, R. F. Wang, and P. G. Kwiat, “Cor-
respondence: Still no evidence for single photon de-
tection by humans,” arXiv:1707.09341, 2017.
[128] K. Sekar, W. M. Findley, D. Poeppel, and R. R.
Llin´as, “Cortical response tracking the conscious
experience of threshold duration visual stimuli in-
dicates visual perception is all or none,” Proceed-
ings of the National Academy of Sciences, vol. 110,
no. 14, pp. 5642–5647, 2013.
[129] S. Dehaene and J.-P. Changeux, “Ongoing sponta-
neous activity controls access to consciousness: a
neuronal model for inattentional blindness,” PLoS
biology, vol. 3, no. 5, p. e141, 2005.
[130] S. Dehaene and J.-P. Changeux, “Experimental
and theoretical approaches to conscious processing,”
Neuron, vol. 70, no. 2, pp. 200–227, 2011.
[131] M. Schaefer and G. Northoﬀ, “Who Am I: The Con-
scious and the Unconscious Self,” Frontiers in Hu-
man Neuroscience, vol. 11, 2017.
[132] G. Northoﬀ, “Self and brain: what is self-related
processing?,” Trends in cognitive sciences, vol. 15,
no. 5, pp. 186–187, 2011.
[133] G. Northoﬀand F. Bermpohl, “Cortical midline
structures and the self,” Trends in cognitive sci-
ences, vol. 8, no. 3, pp. 102–107, 2004.
[134] D. A. Gusnard, E. Akbudak, G. L. Shulman, and
M. E. Raichle, “Medial prefrontal cortex and self-
referential mental activity:
relation to a default
mode of brain function,” Proceedings of the National
Academy of Sciences, vol. 98, no. 7, pp. 4259–4264,
2001.
[135] D. Legrand and P. Ruby, “What is self-speciﬁc?
theoretical investigation and critical review of neu-
roimaging results.,” Psychological review, vol. 116,
no. 1, p. 252, 2009.
[136] K.
Christoﬀ,
D.
Cosmelli,
D.
Legrand,
and
E. Thompson, “Specifying the self for cognitive neu-
roscience,” Trends in cognitive sciences, vol. 15,
no. 3, pp. 104–112, 2011.
[137] D. M. Wolpert, Z. Ghahramani, and M. I. Jordan,
“An internal model for sensorimotor integration,”
Science, vol. 269, no. 5232, pp. 1880–1882, 1995.
[138] J. Limanowski and F. Blankenburg, “Minimal self-
models and the free energy principle,” Frontiers in
human neuroscience, vol. 7, p. 547, 2013.
[139] J. Limanowski and K. Friston, “seeing the dark:
Grounding phenomenal transparency and opacity in
precision estimation for active inference,” Frontiers
in Psychology, vol. 9, p. 643, 2018.
[140] K. Friston, “The free-energy principle:
a uni-
ﬁed brain theory?,” Nature Reviews Neuroscience,
vol. 11, no. 2, pp. 127–138, 2010.
[141] T. Metzinger, “The self-model theory of subjectiv-
ity:
A brief summary with examples,” Humana
MenteQuarterly Journal of Philosophy,
vol. 14,
pp. 25–53, 2010.
[142] O. Blanke,
“Multisensory brain mechanisms of
bodily self-consciousness,” Nature Reviews Neuro-
science, vol. 13, no. 8, p. 556, 2012.
[143] O. Blanke, M. Slater, and A. Serino, “Behavioral,
neural, and computational principles of bodily self-
consciousness,” Neuron, vol. 88, no. 1, pp. 145–166,
2015.
[144] I. Goodfellow, Y. Bengio, and A. Courville, Deep
Learning.
MIT
Press,
2016.
http://www.
deeplearningbook.org.
[145] H. T. Siegelmann and E. D. Sontag, “Turing com-
putability with neural nets,” Applied Mathematics
Letters, vol. 4, no. 6, pp. 77–80, 1991.
[146] H. T. Siegelmann, “Computation beyond the tur-
ing limit,” Science, vol. 268, no. 5210, pp. 545–548,
1995.
[147] H. T. Siegelmann and E. D. Sontag, “On the compu-
tational power of neural nets,” Journal of computer
and system sciences, vol. 50, no. 1, pp. 132–150,
1995.
[148] H. Hy¨otyniemi, “Turing machines are recurrent neu-
ral networks,” Proceedings of STeP’96, vol. 96,
pp. 13–24, 1996.
[149] H. Hyotyniemi, “On unsolvability of nonlinear sys-
tem stability,” in Control Conference (ECC), 1997
European, pp. 2502–2507, IEEE, 1997.
[150] B. van Vugt, B. Dagnino, D. Vartak, H. Safaai,
S. Panzeri, S. Dehaene, and P. R. Roelfsema, “The
threshold for conscious report: Signal loss and re-
sponse bias in visual and frontal cortex,” Science,
vol. 360, no. 6388, pp. 537–542, 2018.
[151] G. A. Mashour, “The controversial correlates of con-
sciousness,” Science, vol. 360, no. 6388, pp. 493–
494, 2018.
[152] M. R. Joglekar, J. F. Mejias, G. R. Yang, and X.-J.
Wang, “Inter-areal balanced ampliﬁcation enhances
signal propagation in a large-scale circuit model of
the primate cortex,” bioRxiv, p. 186007, 2017.
[153] Y. Pinto, D. A. Neville, M. Otten, P. M. Cor-
ballis, V. A. Lamme, E. H. de Haan, N. Foschi,
and M. Fabri, “Split brain: divided perception but
undivided consciousness,” Brain, vol. 140, no. 5,
pp. 1231–1237, 2017.
[154] M. C. Corballis, P. M. Corballis, G. Berlucchi, and
C. A. Marzi, “Perceptual unity in the split brain:


## Page 63


63
the role of subcortical connections,” Brain, 2018.
[155] P. Dayan, G. E. Hinton, R. M. Neal, and R. S.
Zemel, “The helmholtz machine,” Neural computa-
tion, vol. 7, no. 5, pp. 889–904, 1995.
[156] M. Benedetti, J. Realpe-Gmez, and A. Perdomo-
Ortiz, “Quantum-assisted helmholtz machines: A
quantumclassical deep learning framework for in-
dustrial datasets in near-term devices,” Quantum
Science and Technology, vol. 3, no. 3, p. 034007,
2018.
[157] R. Biswas,
Z. Jiang,
K. Kechezhi,
S. Knysh,
S.
Mandr`a,
B.
OGorman,
A.
Perdomo-Ortiz,
A. Petukhov, J. Realpe-G´omez, E. Rieﬀel, et al., “A
NASA perspective on quantum computing: Oppor-
tunities and challenges,” Parallel Computing, 2016.
[158] S.
Boixo,
S.
V.
Isakov,
V.
N.
Smelyanskiy,
R. Babbush,
N. Ding,
Z. Jiang,
J. M. Mar-
tinis,
and H. Neven,
“Characterizing quantum
supremacy in near-term devices,” arXiv preprint
arXiv:1608.00263, 2016.
[159] A.
Perdomo-Ortiz,
M.
Benedetti,
J.
Realpe-
G´omez, and R. Biswas, “Opportunities and chal-
lenges for quantum-assisted machine learning in
near-term quantum computers,”
arXiv preprint
arXiv:1708.09757, 2017.
[160] J. A. Reggia, “The rise of machine consciousness:
Studying consciousness with computational mod-
els,” Neural Networks, vol. 44, pp. 112–131, 2013.
[161] O. Carter, J. Hohwy, J. van Boxtel, V. Lamme,
N. Block, C. Koch, and N. Tsuchiya, “Conscious
machines: Deﬁning questions,” Science, vol. 359,
no. 6374, pp. 400–400, 2018.
[162] D. Gamez, “Progress in machine consciousness,”
Consciousness and cognition, vol. 17, no. 3, pp. 887–
910, 2008.
[163] S. C. Kapfer and W. Krauth, “Irreversible local
markov chains with rapid convergence towards equi-
librium,” Physical review letters, vol. 119, no. 24,
p. 240603, 2017.
[164] Z. Lei and W. Krauth, “Irreversible markov chains
in spin models: Topological excitations,” EPL (Eu-
rophysics Letters), vol. 121, no. 1, p. 10008, 2018.
[165] Z. Lei and W. Krauth, “Mixing and perfect sam-
pling in one-dimensional particle systems,” arXiv
preprint arXiv:1806.06786, 2018.
[166] B. A. Wallace, Contemplative science: Where Bud-
dhism and neuroscience converge.
Columbia Uni-
versity Press, 2009.
[167] B. A. Wallace, Hidden dimensions: The uniﬁcation
of physics and consciousness. Columbia University
Press, 2007.
[168] A. Zajonc, ed., The new physics and cosmology: Di-
alogues with the Dalai Lama.
Oxford University
Press, 2004.
[169] M. Ricard, A. Lutz, and R. J. Davidson, “Mind of
the meditator,” Scientiﬁc American, vol. 311, no. 5,
pp. 38–45, 2014.
[170] G. Desbordes and L. T. Negi, “A new era for mind
studies: training investigators in both scientiﬁc and
contemplative methods of inquiry,” Frontiers in hu-
man neuroscience, vol. 7, p. 741, 2013.
[171] R. P. Mann and D. Helbing, “Optimal incentives for
collective intelligence,” Proceedings of the National
Academy of Sciences, vol. 114, no. 20, pp. 5077–
5082, 2017.
[172] D. Lama, The universe in a single atom: The con-
vergence of science and spirituality. Harmony, 2005.
[173] G. K. Gyatso, Mahamudra Tantra:
the supreme
heart jewel nectar. Tharpa Publications US, 2005.
[174] S. Harnad, “The symbol grounding problem,” Phys-
ica D: Nonlinear Phenomena, vol. 42, no. 1-3,
pp. 335–346, 1990.
[175] D. Levary, J.-P. Eckmann, E. Moses, and T. Tlusty,
“Loops and self-reference in the construction of
dictionaries,” Physical Review X, vol. 2, no. 3,
p. 031018, 2012.
[176] P. Vincent-Lamarre, M. Lord, A. Blondin-Mass´e,
O. Marcotte, M. Lopes, and S. Harnad, “Hidden
structure and function in the lexicon,” in Cognitive
Approach to Natural Language Processing, pp. 91–
108, Elsevier, 2017.
[177] K. Raworth, Doughnut economics: seven ways to
think like a 21st-century economist. Chelsea Green
Publishing, 2017.
[178] K. Raworth, “Old economics is based on false ‘laws
of physics’ new economics can save us,” 6 Apr 2017.
[179] C. Brown, Buddhist Economics:
An Enlightened
Approach to the Dismal Science. Bloomsbury Pub-
lishing USA, 2017.
[180] G. Miller, “The US Is the Most Overworked Devel-
oped Nation in the World—When Do We Draw the
Line?,” 20 Something Finance, 2010.
[181] Wikipedia contributors, “Age of enlightenment —
wikipedia, the free encyclopedia,” 2018.
[Online;
accessed 3-April-2018].
[182] G. soros, The Crash of 2008 and What it Means:
The New Paradigm for Financial Markets. Publi-
cAﬀairs, 2009.
[183] C. Declerck and C. Boone,
Neuroeconomics of
Prosocial Behavior:
The Compassionate Egoist.
Academic Press, 2015.
[184] J. Realpe-G´omez, G. Andrighetto, G. Nardin, and
J. A. Montoya, “Balancing selﬁshness and norm
conformity can explain human behavior in large-
scale prisoner’s dilemma games and can poise hu-
man groups near criticality,” Physical Review E,
vol. 97, p. 042321, 2018.
[185] “Monk suicide by ﬁre in anti-diem protest,” New
York Times, p. 6, 11 June 1963.
[186] M. Young, Vietnam Wars 1945-1990.
Harper
Collins, 1991.
[187] D. Eagleman, The Brain: The story of you. Pan-
theon, 2015.
[188] G. Northoﬀ, “Brain and self–a neurophilosophical
account,” Child and adolescent psychiatry and men-
tal health, vol. 7, no. 1, p. 28, 2013.
[189] Z. Wang and J. Busemeyer, “Reintroducing the con-
cept of complementarity into psychology,” Frontiers
in psychology, vol. 6, 2015.
[190] N. G. Van Kampen, Stochastic processes in physics
and chemistry, vol. 1. Elsevier, 1992.
[191] H. Risken and H. Haken, The Fokker-Planck Equa-
tion: Methods of Solution and Applications Second
Edition. Springer, 1989.
[192] C. Doran and A. Lasenby, Geometric algebra for
physicists. Cambridge University Press, 2003.
[193] H. Haken and H. C. Wolf, The physics of atoms
and quanta: introduction to experiments and theory,


## Page 64


64
vol. 1439. Springer Science & Business Media, 2005.
[194] Realpe-G´omez, ““negative probabilities” as relative
probabilistic expressions,” arXiv preprint to appear,
2019.
[195] M. Burgin, “Interpretations of negative probabili-
ties,” arXiv preprint arXiv:1008.1287, 2010.
[196] S. Abramsky and A. Brandenburger, “An opera-
tional interpretation of negative probabilities and
no-signalling models,” in Horizons of the mind. A
tribute to Prakash Panangaden, pp. 59–75, Springer,
2014.
[197] J. Realpe-G´omez and N. Killoran,
“Quantum-
inspired memory-enhanced stochastic algorithms,”
arXiv:1906.00263, 2019.
[198] H. Jung, S. Lee, J. Yim, S. Park, and J. Kim, “Joint
ﬁne-tuning in deep neural networks for facial ex-
pression recognition,” in Computer Vision (ICCV),
2015 IEEE International Conference on, pp. 2983–
2991, IEEE, 2015.
[199] Y. Bengio et al., “Learning deep architectures for
AI,” Foundations and trends R
⃝in Machine Learn-
ing, vol. 2, no. 1, pp. 1–127, 2009.
[200] M. Benedetti, J. Realpe-G´omez, R. Biswas, and
A. Perdomo-Ortiz, “Estimation of eﬀective temper-
atures in quantum annealers for sampling applica-
tions: A case study with possible applications in
deep learning,” Physical Review A, vol. 94, no. 2,
p. 022308, 2016.
[201] J. Ngiam, A. Khosla, M. Kim, J. Nam, H. Lee, and
A. Y. Ng, “Multimodal deep learning,” in Proceed-
ings of the 28th international conference on machine
learning (ICML-11), pp. 689–696, 2011.
[202] R. Salakhutdinov, Learning deep generative models.
PhD thesis, University of Toronto, 2009.
[203] C. Choi, “Strange but true: When half a brain is
better than a whole one,” Scientiﬁc American, May,
vol. 24, 2007.
Human experience as an illusion?
Varela et al. [1]
This work
Physics
Chemistry
Biology
Neuroscience
FIG. 1: Scientiﬁc hierarchy in the mainstream paradigm:
In the current scientiﬁc paradigm, physics is considered
the most fundamental theory that provides the objec-
tive laws of nature out of which all other scientiﬁc dis-
ciplines progressively emerge (see Sec. I and Fig. 4). At
the end of such a scientiﬁc hierarchy we ﬁnd human ex-
perience as an illusion generated by billions of neurons
ﬁring. Varela, Thompson, and Rosch [1] suggest human
experience should feedback into the foundations of neu-
roscience, creating a fundamental circularity that gives
rise to a more consistent theory of cognitive phenomena.
In this work we propose such a feedback should be ex-
tended to the very bottom of the scientiﬁc hierarchy, i.e.
physics itself. In this perspctive, the laws of nature might
be considered as self-consistent regularities that emerge
out of the interaction between subject and object (see
Sec. X C 2). At a rather subtle level scientiﬁc paradigms
set our conception of society. Has perhaps the emphasis
of the mainstream paradigm on getting rid of the subjec-
tive, ourselves, unkowingly diverted our attention towards
concerns on mechanisms, such as resource optimization
or automation, leaving the more human-centered socio-
ecological concerns for later? (see Sec. X C 3).


## Page 65


65
a
b
FIG. 2:
Perspectives used in this work.
(a) Third-person perspective analysis of human observers as performed,
for instance, in the modern research program on consciousness championed by Nobel laureate Francis Crick and his
collaborator Christof Koch [24] (see also Refs. [20, 21]).
The human observer under study is analyzed from the
perspective of an external observer which is not part of the experimental set-up. Subjective reports by the observer
under analysis are contrasted with the associated neural activity (see Fig. 3 and Appendix B 1).
(b) First-person
perspective as depicted by Ernst Mach self-portrait in 1886. This self-portrait will be used in this work to indicate the
analysis of physical systems from the perspective of the scientist performing the experiment, which is herself part of
the system being studied. Although it might be obvious for most people, we would like to emphasize that to the best of
our knowledge this is the only perspective human beings have, from birth to death. We argue here that this perspective
leads to self-reference, which can induce an inﬁnite regress if approached na¨ıvely (see Fig. 7 and Appendix B 2).


## Page 66


66
 
I feel I am 
out of my 
own body
FIRST-PERSON RAW DATA: 
SUBJECTIVE REPORTS OF 
SEVERAL INDIVIDUALS
THIRD-PERSON RAW DATA: 
PATTERNS OF NEURAL 
ACTIVITY
INFERENCE: Identify neural correlates of subjective experience.
CONTROL: Induce similar subjective experiences via interventions.
COMPARE
Inside the brain
FIG. 3:
Modern scientiﬁc strategy to study consciousness. Today even phenomena that were previously considered
unscientiﬁc, such as out of body experiences [27–29], can be studied and even induced at will in the lab; such type of
research is considered rigorous enough to deserve publication in top journals such as Science [27, 28]. The strategy for
doing this is a combination of subjective reports, taken as ﬁrst-person raw data, and third-person analysis of neural
activity. So, by collecting subjective reports of several individuals and recording the corresponding neural activity we
obtain a pair of correlated datasets from a ﬁrst- and third-person perspective on the same phenomena. By carefully
analysing these pair of datasets we can in principle identify the neural correlates of subjective experience. With that
knowledge we can perform interventions in an individual’s brain to induce such subjective experience, if the correlations
detected were causal. The example shown in the ﬁgure also suggests that even the feeling experienced by some people
of being out of their own body—which appears to be the phenomenon most consistent with the assumption implicitly
made in physics that we can observe the world from the outside as if we were not part of it—is experienced from those
people’s own subjective perspective.


## Page 67


67
Nature is fundamentally 
quantum for some reason 
we do not yet understand. 
MAINSTREAM PARADIGM
Nature looks classical to us 
observers due to decoherence 
that destroys quantumness.
Nature looks quantum because the 
observer is part of the experimental 
setup. Quantum effects are relevant 
when the observer's physical   
interactions cannot be neglected. 
REVERSE PARADIGM
Not quantum phenomena expected 
in a macroscopic complex system 
as a brain; rather, (third-person) 
observers "collapse quantum state".
DECOHERENCE
COHERENCE
Nature is fundamentally 
classical, i.e. described by 
classical probability theory,  
just as in everyday life.
Physical interactions and first-person 
perspective associated to the 
embedded observer is key to produce 
quantum coherent phenomena.
QUANTUM REALM
CLASSICAL REALM
FIG. 4:
Comparison between mainstream paradigm and the reverse paradigm followed in this work. The mainstream
paradigm in physics is that at the ‘microscopic’ level nature is quantum for some reason we do not yet understand (top).
In this paradigm, the act of observation can ‘collapse the wave function’ rendering the system classical; so, observers
induce decoherence of the quantum state. Furthermore, when observers are analyzed, such as in studies of the Maxwell
demon, they are analyzed from a third-person perspective, i.e. from the perspective of another observer external to
the system being analyzed (cf. Fig. 2a). In contrast, this work is placed within the context of the reverse paradigm
(bottom) wherein nature is fundamentally classical, i.e. it can be described with classical probability theory, yet due
to the physical interactions associated to the observer, considered as another classical system, quantum phenomena
arise. Thus, in this paradigm the observer instead of inducing decoherence actually becomes the cause that the world
appears quantum to her. Moreover, in this paradigm the observer is modelled as a ﬁrst-person observer which leads to
self-reference (cf. Fig. 2b).


## Page 68


68
x = 0     x = 1
y = ?
x = ?
NO
YES
Is x = y?  
y = 1
x = 1
NO
YES
Is x = y?  
y = 0
x = 1
NO
YES
Is x = y?  
y = 0     y = 1
a
b
c
d
FIG. 5: Information processing requires physical inter-
action. (a) Information is encoded in physical systems.
Here we show how two bits x and y can be encoded using
magnets: if the North pole of the magnet representing x
points up or down, respectively, then x = 0 or x = 1;
similarly for y. (b) The information processing required
to answer an apparently abstract question such as “Is
x = y?” can be implemented here by the interaction of
the two magnets representing x and y: (c) if x = y then
the two magnets attract each other; (d) else they repel
each other.


## Page 69


69
ℏ
Physical interactions for 
information processing: 
data comparison,    
conscious access,   
motor control. 
Experimental interventions (e.g. via electric interactions)
Typical depiction of experimental set-ups
Light 
X-rays
FIG. 6:
Illustration of Principle I. Experimental set-ups are typically depicted as shwon inside the dashed box on
the left, i.e. omitting the observer. If at all, to the best of our knowledge, the observer is included as a cartoon not
playing any dynamical role. This implicitly assumes that observers are something abstract, rather than something
material that should also be subject to the laws of physics. Principle I asks us to drop such an assumption and
consistently treat observers as physical systems that interact with the experimental set-up. Indeed, observers usually
get information about the system via visible electromagnetic radiation or light. Similarly, experimental interventions,
e.g. state preparations, also require some kind of interaction, typically pressing some buttons or a computer keyboard.
According to textbook physics, touching is also a physical interaction between the atoms of the body and the atoms
of the device being touched. Furthermore, the information processing necessary for an observer to detect or ‘be aware
of’ any correlation between the initial state prepared and the ﬁnal state observed requires the physical interaction of
at least some of the components of the information processing device (see Fig. 5), i.e. the brain in this case. Moreover,
since any statements we make about physics typically comprise relationships between data which ‘we are conscious’
about, we expect the information processing should include the process of conscious access. We argue in this work that
such previously neglected interactions can account for the quantum of action.


## Page 70


70
a
b
...
YOU!
YOU!
ℏ
ℏ
ℏ
ℏ
ℏ
ℏ
FIG. 7:
Illustration of Principle II. (a) In Fig. 6 there was something very important lacking: You! Indeed, the
observer in Fig. 6 was analyzed from the perspective of an external observer, in this case you, once again not included
in the picture. (b) Principle II asks us to drop the assumption, however successful, that we can observe the world
from a third-person perspective, as if we were not part of it. In other words, Principle II asks us to be consistent with
what we observe every single second of our lives, from birth to death, i.e. that we can only perceive the world from a
ﬁrst-person perspective, until there is experimental evidence that suggest otherwise. However, if we attempt to include
the new observer in (a) in the same way we did in Fig. 6 we end up with the same problem, only that with two observers
now. If we insist in doing this we end up with an inﬁnite regress. This problem is caused by self-reference, and can
be tackled using ideas from the recursion theorem in theoretical computer science. A simple conceptual explanation of
the central idea involved in the recursion theorem is illustrated in Fig. 12 (see also Fig. 8).


## Page 71


71
THIRD-PERSON PERSPECTIVE
FIRST-PERSON PERSPECTIVE
BOB's 
CAMERA
ALICE's 
CAMERA
CHRIS' 
CAMERA
a
b
BOB
ALICE
ALICE
BOB
FIG. 8:
Simple experiment illustrating the architecture of a ﬁrst-person observer. (a) A system composed of two
observers, Alice and Bob (here represented as photographers), observing each other as seen from the perspective of
another observer, Chris, external to the system composed of Alice and Bob. (b) System composed of Alice and Bob as
observed from the perspective of the composed system of Alice and Bob itself.


## Page 72


72
"    "
"    "
"      "
"      "
"    "
" "
Light 
Light 
Light 
Impaired subject unable to perceive, 
e.g. a brain-dead person
Scientists communicating their subjective perceptions
FIG. 9:
Illustration of the ‘model what is’ motto. An implicit assumption in physics is that measuring devices (here a
clock) take the subject out of the loop, allowing us to have an objective description of the world. This assumption is
indeed consistent with experimental evidence in the sense that our subjective perceptions of the readings of measuring
devices appear to be consistent, i.e. when we communicate our subjective perceptions to other scientists we usually
agree on them (bottom), as if they were objective. However, the ‘model what is’ motto asks us not to start our analysis
from this assumption, but rather from the very inferential process that allows us to test its validity in the ﬁrst place.
More precisely, the ‘model what is’ motto (see Sec. I and Appendix A) ask us to ﬁrst model what we actually experience
and only afterwards evaluate whether the communicated subjective experiences seem consistent with the assumption
that there is an objective world out there; this is a sort of intersubjectivity. According to recent research there are
physical processes in the brain (and body) associated to our subjective experiences, i.e. their neural correlates (here
represented by a replica of the external system within green quotation marks). Consider, for instance, a brain-dead
person (top; here represented with green quotation marks enclosing a blank space) in front of an experimental device:
even though he receives the same information (via light) as others observing the same device, his brain is unable to
construct a percept of it; i.e. no properly working brain no perceptions. Furthermore, consistent with textbook physics,
the neural correlates associated to an external system must be induced by physical interactions (e.g. light). Principle
I asks us to take such physical interactions into account and only afterwards evaluate whether they can be neglected
as usually done in physics. Principle II asks us to describe experiments from a subjective perspective, i.e. from
the perspective of the scientist actually carrying out the experiment. Since, as far as we know, the only ﬁrst-person
perspective we have access to is our own, Principle II essentially asks us to describe experiments from our own
perspective (see Fig. 7), i.e. from the perspective of each one of us. Since, in this view, physics is about agreeing on a
class of subjective experiences, we can in principle explore potential extensions of physics to other type of subjective
experiences (see Fig. 22). Indeed, subjective experiences such as emotions, for instance, appear to be associated to
certain physical processes (e.g. face expressions) consistent enough for computers to be able to recognize them with
good accuracy [198].


## Page 73


73
Fʎ  (xʎ , xʎ +1)
xʎ               xʎ +1
x1                                                                            xn     
Fʎ  (xʎ , xʎ +1)
xʎ      
xʎ +1
Z→ʎ  (xʎ  )
Zʎ +1← (xʎ  +1 )
xʎ               xʎ +1
Fʎ  (xʎ , xʎ +1)
xʎ      
Z→ʎ +1 (xʎ  +1 )
xʎ               xʎ +1
x1      
xn      
x1      
Z→ʎ  (xʎ  )
a
b
c
FIG. 10:
Illustration of the cavity method. (a) Factor graph associated to a Markov chain (see Eq. (36)). (b) Graphical
expression for the pairwise marginal Pℓ(xℓ, xℓ+1) (see Eq. (42)); the partial partition functions Z→ℓ(xℓ) (blue; see
Eq. (44)) and Zℓ+1←(xℓ+1) (red; see Eq. (45)) correspond to the sum over all variables on the cavity graphs inside
the dashed rectangles, except for xℓand xℓ+1 which are clamped to be able to recover the whole grapical model by
multiplying for Fℓ(xℓ, xℓ+1). (c) The partial partition function Z→ℓ+1(xℓ+1) (red) can be recursively computed by
multiplying the partial function Z→ℓ(xℓ) and the factor Fℓ(xℓ, xℓ+1) and tracing over xℓ(see Eq. (46)). This is the
content of the belief propagation algorithm [97] speciﬁed by Eqs. (46) and (47).


## Page 74


74
Fʎ  (xʎ , xʎ +1)
xʎ               xʎ +1
x1     
ᶞ→1(x1)
ᶞn←(xn )
a
b
xn    
Fn(xn , x1)
Fʎ  (xʎ , xʎ +1)
xʎ               xʎ +1
x1     
xn    
Fn(xn , x1)
x1     
xn    
FIG. 11:
Illustration of cavity method on cycles.
(a)
Factor graph with circular topology, where the new fac-
tor Fn(xn, x1) (green) closes the chain in Fig. 10a. While
this factor could be the product of other factors represent-
ing local interactions between additional variables (dotted
circles), it is enough for our purposes to consider only one.
In contrast to an open chain, it is in general not pos-
sible to write Pcycle(x1, . . . , xn) as a Markov chain (see
Sec. V C). Furthermore, the standard belief propagation
equations do not generally lead to the correct marginals
[100].
(b) By conditioning on x1 and xn (black ﬁlled
circles) we can remove factor Fn(xn, x1) to turn the cy-
cle into a chain with x1 and xn clamped to some given
values x∗
1 and x∗
n.
Such clamping can be implemented
via pure initial and ﬁnal messages µ→1(x1) = δ(x1 −x∗
1)
and µn←(xn) = δ(xn −x∗
n), where δ(x) denotes the Dirac
delta function.
Recall that any quantum pure state
|ψ⟩= U |x∗⟩can be prepared from a state with sup-
port on a single point obtained from a projective mea-
surement |x∗⟩, with ⟨x| x∗⟩= δ(x −x∗), and a uni-
tary transformation U = |ψ⟩⟨x∗| + P
x̸=x∗|φx⟩⟨x|, where
|ψ⟩⟨ψ| + P
x̸=x∗|φx⟩⟨φx| = I, which can be implemented
via certain Hamiltonian. Since the messages are closely
related to imaginary-time wave functions, this is somehow
similar to the imaginary-time two-vector state formalism
of quantum mechanics [101, 102], in which we deﬁne initial
and ﬁnal pure states (pre- and post-seection) and predict
the state in between (see Sec. V C).


## Page 75


75
ALICE
BOB
ALICE
BOB
b
c
d
a
FIG. 12:
Self-reference and complementarity. (a) The
goal is to build a Turing machine (represented here by
a computer) that prints (in the screen) a description of
itself (represented here by the same computer within quo-
tation marks). The recursion theorem in its full generality
is presented in Appendix C following Ref. [90]; here we
present a slightly modiﬁed, more symmetrical, and simpli-
ﬁed description of the main concepts involved. (b) This is
achieved by two complementary sub-machines, Alice and
Bob, that essentially print a description of each other,
here represented by drawings within (green) quotation
marks. To avoid circularity, while Alice directly prints or
generates a description of Bob, Bob actually infers a de-
scription of Alice from her output. This is reminiscent
of the free energy principle underlying the modern ap-
proach to brain modeling via active inference [140] or the
related architecture of a Helmholtz machine [155, 156].
(c) However, after Alice and Bob mutually print each
other they need to exchange their descriptions to obtain
a correct image; this is symbolized here by the colored
arrows. (d) In this way we obtain a Turing machine that,
when run, prints a description of itself.


## Page 76


76
Q
w
fQ(w) = "PRINTw"
a
b
FIG. 13:
Inferring the description of a printing machine. (a) Cartoon example of a Turing machine (represented here
by a computer) that, given some input (here a bulb), prints the description of a Turing machine (represented here by a
Tablet within quotation marks) that prints the given input. (b) A more formal representation of the Turing machine in
(a), here called Q. Ref. [90] uses Q to proof the recursion theorem. The input is a string w of characters from a suitable
alphabet, and the Turing machine that prints w is called Printw. The Turing machine Q basically infers Printw,
eﬀectively implementing the function fQ that maps w into “Printw”. Proving the existence of Q is straightforward
(see Ref. [90], chapter 6).
ALICE
BOB
"BOB"
"ΡRINT"TM"∘TM"
"TM"
BOB
"PRINT"BOB"∘BOB" = "ALICE∘BOB" 
ALICE
"BOB"
a
c
b
= "SELF" 
FIG. 14:
Self-printing Turing machine.
A more formal description of the Turing machine sketched in Fig. 12.
(a) The Turing machine Alice = Print“Bob” prints a description of the Turing machine Bob (see Eq. (C2)). But
how is Bob deﬁned? (b) Bob = “TM”Print“Print“TM”◦TM” takes as input the description “TM” of a generic Turing
machine TM and infers, via Q (see Fig. 13), the description of a Turing machine Print“TM” that prints “TM”. Bob
then composes the Turing machine Print“TM” with the Turing machine TM itself and outputs the corresponding
description, i.e. “Print“TM” ◦TM” (see Eq. (C3)); composition is represented here by the symbol ◦. (c) The Turing
machine Self = Alice ◦Bob that results from the composition of Alice and Bob outputs a description of itself, as
it can be seen by doing TM = Bob in (b) and using Alice = Print“Bob” (see Eq. (C1)).


## Page 77


77
= "RECURSION"
"ALICE  (BOB  RT)"
BOB
ALICE
RT
∘
∘
∘
BOB
∘
RT
"TM"
fRT("TM", w)
"TM"
a
w
"BOB  RT"
ALICE
∘
"BOB  RT"
BOB
ALICE
RT
b
c
d
e
w
f
"PRINT"TM"  TM"
fRT("RECURSION", w)
FIG. 15:
Recursion theorem. (a) The recursion theorem essentially states that a Turing machine (here a computer)
can access a description of itself and manipulate it, along with the input (here a bulb), to produce a certain output
(here a description of a rotated copy of itself printing a rotated bulb).
(b) The architecture of a generic Turing
machine, Recursion, that implements this idea is composed of three sub-machines: Alice and Bob, similar to those
in Fig. 14, along with a 2-input Turing machine RT, provided by the recursion theorem. We can write this Turing
machine as Recursion = Alice◦Bob◦RT, where the superindex ◦refers to composition along the upper input channel
of RT (see Eq. (C4)).
But how exactly are Alice, Bob, and RT deﬁned?
(c) Alice = Print“Bob◦RT” prints a
description of the composition of Bob and RT along the upper input channel of RT (see Eq. (C5)). (d) Bob is deﬁned
in the same way as in Fig. 14b, only that now TM is a 2-input Turing machine (see Eq. (C3)).
(e) RT takes as
inputs the description “TM” of a Turing machine TM and a string w and implements a general computable function
fRT(“TM”, w), that operates on both the description of TM and the input w to produce an output. (f) Proof of
the recursion theorem by putting all pieces together and using the deﬁnitions of the Turing machines in (c-e). Since
Recursion = Alice◦Bob◦RT and Alice = Print“Bob◦RT”, we can see that the whole Turing machine Recursion
implements a function fRT(“Recursion”, w) that can use its own description, “Recursion”, during the computation.


## Page 78


78
...
...
...
LOW LEVEL 
FEATURE:
EYE
LOW LEVEL 
FEATURE: 
NOSE
HIGH LEVEL 
FEATURE: 
FACE
HIGH LEVEL 
FEATURE: 
LAUGHING
PIXELS
VARIABLES 
ENCODING 
PIXELS' 
COLORS
RAW DATA
FEATURES
EXAMPLE: RESTRICTED BOLTZMANN MACHINE
u1
u2
u3
v1
v2
v3
v4
EXAMPLE: INFORMATION INTEGRATION 
VIA MULTIMODAL DEEP LEARNING
...
...
...
VISION
...
...
...
AUDIO
...
...
...
TOUCH
. . .
SHARED REPRESENTATION
a
b
c
RAW DATA FROM 
EXTERNAL WORLD
TOY EXAMPLE: ARTIFICIAL OBSERVER
d
INTERNAL PHYSICAL 
REPRESENTATION 
OF FEATURES
INTERNAL PHYSICAL 
REPRESENTATION  
OF RELATIONSHIPS 
DEEP LEARNING OF REPRESENTATIONS
FIG. 16:
Toy example of a more realistic artiﬁcial observer. (a) Example of a deep architecture that can be used
to learn hierarchical representations of data (cf. Fig. 1 of [199]). An image can be represented as an array of pixels
whose colors can be encoded as numbers. The pink variables at the bottom represent the pixels’ color. Such raw data
are then processed by the ﬁrst module to extract ﬁrst-level features, which represent a speciﬁc type of pattern, e.g. a
nose or an eye. Ideally, such features can be represented by a boolean variable which is equal to one if the feature it
represents is present on the input image, and zero otherwise. First-level features can be interpreted as new data that
can be processed by a second module to extract second-level features, e.g. a face or the facial expression associated
to laughing. (b) A restricted Boltzmann Machine (RBM) is a speciﬁc example of a module that can be recursively
stacked to build a deep architecture. The variables vk in the ﬁrst layer are the visible or observed variables, which
encode the raw data, while the variables uj in the second layer are the unobserved or hidden variables, which encode the
features. An RBM is a probabilistic graphical model characterized by a Boltzmann distribution PB(u, v) = e−βE(u,v)/Z
with an energy function E(u, v) = P
j,k Wjkujvk + P
j ajuj + P
k bkvk. To train an RBM means to ﬁnd values for the
parameters Wjk, aj, bk such that: (i) the marginal probability P(v) = P
u PB(u, v) resembles the emprical distribution
of the dataset, and (ii) P(v) can generalize to or predict new data that was not presented before to the RBM. The
implementation of an RBM on hardware requires physical systems that can represent the corresponding variables, and
the neccessary physical interaction between them. Such physical interactions can be direct like that between variables
v1 and u1, or indirect like that between variables v1 and v2— see e.g.
Ref. [200] for a discussion on the physical
implementation of a type of RBM on a quantum annealer (similar considerations hold for physical implementations on
classical hardware). (c) Deep architectures can in principle be combined to create multimodal architectures that can
integrate information arriving from diﬀerent pathways, e.g. the image of a car, the sound of a car, the word ‘car’, the
pattern of interactions associated to touching a car [201, 202]. In principle, the part dedicated to vision can extract
relevant features of images (e.g. cars), while the audio component can extract relevant features of related sounds (e.g.
sounds of engines). The intuition behind is that it is more eﬀective to encode the association between images and
their associated sounds at the level of high level features than at the level of raw data. Ideally, a feature at the top
layer can encode the analogous of a ‘concept’, e.g. the boolean variable associated can take value one when any of the
information pathways contain a pattern associated to the concept of a car. These high-level features are also called
‘shared representations’. (d) Toy example of an artiﬁcial observer, e.g. a robot, on a toy world. The external world is
modelled here as a source of raw data while the observer is modelled and the external observer as a robot with a neural
network implemented in hardware whose visible units encode the raw data of the external world. Such a network can be
composed of a multimodal deep architecture that hierarchically extracts features from diﬀerent information pathways,
e.g. vision, audio.


## Page 79


79
ui
uf
vi
vf
MEASURE
PREPARE
“     ”
“      ”
“   ”
“   ”
EXTERNAL WORLD
INTERNAL REPRESENTATION
a
b
EVOLVE
SIMULATE
ui
uf
vi
vf
MEASURE
PREPARE
“     ”
“      ”
EXTERNAL WORLD
INTERNAL REPRESENTATION
c
d
e
EVOLVE
DECIDE
ui
uf
vi
vf
MEASURE
PREPARE
EVOLVE
DECIDE?
SIMULATE?
a1
o1
v1
u1
vi
vf
EVOLVE
v1
FIG. 17:
Experiments as circular interactions. (a) An artiﬁcial observer, Alice, performing an experiment to determine
whether the state of a switch (i.e. On or Off) has a causal inﬂuence on the state of a lamp (i.e. Light or Dark).
We emphasize that this is a third-person perspective analysis. Alice’s ‘brain’ is a computer, a physical realization
of a Turing machine. We say Alice has observed the external system when she has build an internal representation
of it, denoted by enclosing a replica of the system within quotation marks.
Such internal representation requires
a physical implementation in Alice’s hardware.
To perform the experiment, Alice ﬁrst ‘decides’ which intervetion
to do, i.e. where to position the switch, and then ‘acts’ by moving the switch accordingly; such action requires a
physical interaction represented by a red arrow (cf. Fig. 6). After preparing the system via her interventions, Alice
leaves the system evolve (pink arrow) and measure the state of the lamp. Such measurement also requires a physical
interaction represented by the blue arrow (cf. Fig. 6). By running the experiment n times Alice can obtain a dataset
D = {(u(1)
i
, u(1)
f
), . . . , u(n)
i
, u(n)
f
)}, where u(d)
i
and u(d)
f
stand for, respectively, Alice’s internal representations of the
state of the switch and the lamp at the d-th run of the experiment. Alice can use D to build a causal model represented
by the green line joining the two representations; this line actually stands for an arrow whose direction we have not yet
deﬁned. (b) If we interpret Alice’s causal model as a simulation of the external system, then the arrow corresponding
to the green line should point in the same direction of the external (pink) arrow. (c) Alternatively, in the so-called
ideomotor view [103], Alice’s causal model is reversed: Alice’s representation of the intended eﬀect (e.g. lamp in state
Light) of her action (e.g. turn switch On) is the cause of the action. In other words, it is not the action that produces
the eﬀect, but rather the internal representation of the eﬀect that produces the action [103]. We expect this to be
a more faithful representation of the situation in an experiment. However, this leads to a graphical model that is a
directed loop representing reciprocal causation, a subject that to the best of our knowledge is not as developed as the
most standard models of causality based on directed acyclical graphs, i.e. with no loops (see e.g. Ref. [105], chapter
12.1). (d) The most relevant feature from this analysis is that, once we take into account the observer as part of the
experimental set-up, the topology of the interactions taking place in an experiment is circular. For this reason we will
not assign a direction to the green line, and will discuss both cases. (e) In contrast, when the interactions associated
to the observer are neglected, the apparent topology of interactions taking place in an experiment is that of a chain.
Notice that the initial and ﬁnal points of a chain (i.e. v1 and v3) interact with only one single point (here v2) while the
rest of the points (e.g. v2) interact with two other points. This allows us to specify a well-deﬁned initial (or ﬁnal) state
and propagate it through the chain via the transition probabilities. This contrasts with the case of a circular topology
as in (d) where no single point is special: there is neither intrinsic beginning nor intrinsic end on a circle.


## Page 80


80
ALICE AS THE
(THIRD- PERSON) 
OBSERVING SUBJECT 
BOB AS THE
OBJECT BEING 
OBSERVED
BOB AS THE 
(THIRD- PERSON) 
OBSERVING SUBJECT 
ALICE AS THE
OBJECT BEING 
OBSERVED
∆3rd PA
∆1st PB
xʎ
xʎ +1
xʎ
xʎ +1
ALICE AS 
THIRD-PERSON 
OBSERVER
BOB AS 
THIRD-PERSON 
OBSERVER
FIRST-PERSON OBSERVER
CHRIS' THIRD-PERSON PERSPECTIVE
CHRIS' THIRD-PERSON PERSPECTIVE
a
b
c
∆3rd PB
∆1st PA
FIG. 18: Architecture of self-referential observer with a ﬁrst-person perspective. (a, b) A third-person observer, Chris,
describes the mutual observation between observers Alice and Bob; this is the formal analogous of the situation in
Fig. 8a.
The same circular physical process observed by Chris can be interpreted as Alice observing Bob (a) or
viceversa (b). (a) When Alice is interpreted as the observing subject and Bob as the object being observed, the top
(red) and bottom (blue) horizontal arrows are interpreted as preparation and measurement, respectively (cf. Fig. 17).
Similarly the (green) left and (purple) right vertical arrows are interpreted, respectively, as Alice’s internal decision
process and the evolution of the external physical system (i.e. Bob). As we discuss in Sec. III B although a camera can
take a picture of any external object, it cannot take a picture of itself because a system cannot simultaneously behave
as both subject and object (i.e. they are complementary roles), unless there is a complementary system like a mirror or
another camera. Similarly, Alice can observe the changes in Bob’s state from a third-person perspective ∆3rdPB, but she
cannot observe her own changes ∆1stPA of state from a ﬁrst-person perspective. This is represented by writing ∆1stPA
inside a black box. However, if there are no external or irreversible contributions the changes are equal in magnitude
and opposite in sign, i.e. ∆1stPA = −∆3rdPB (see Fig. 19 for the extension to the general non-equilibrium case). This
is the formal analogous of Alice’s camera in Fig. 8b, with ∆1stPA playing the role of the memory of Alice’s camera
and ∆3rdPB playing the role of Bob as the object the camera is taking the picture of. (b) When Bob is interpreted
as the observing subject and Alice as the object being observed, all roles are reversed. In particular, top (blue) and
bottom (red) horizontal arrows are now interpreted as measurement and preparation, respectively (cf. Fig. 17), as well
as the (purple) left and (green) right vertical arrows are interpreted, respectively, as Bob’s internal decision process
and the evolution of the external physical system (i.e. Alice). However, while the external process observed by Bob
is in the reverse direction of the external process observed by Alice. This is more clearly seen in (c) where we traced
out the measurement and preparation parts. We can clearly see the external process observed by Alice (left) goes
from xℓ→xℓ+1, while that observed by Bob goes from xℓ+1 →xℓinstead. This is similar to the inversion of left and
right when we look at ourselves in a mirror. So, taking into account this inversion we have ∆1stPB = ∆3rdPA. (c)
The self-referential observer that has a ﬁrst person-perspective is composed of two sub-observers Alice and Bob that
mutually observe each other. We emphasize once again that the physical process is exactly one and the same but has
two diﬀerent interpretations depending on the role we asign to Alice and Bob as either subjects or objects; we draw the
same circular process twice in (c) to emphasize these dual roles. This is the formal analogous of the situation illustrated
in Fig. 8b.


## Page 81


81
xʎ
xʎ +1
xʎ
xʎ +1
ALICE AS 
THIRD-PERSON 
OBSERVER
BOB AS 
THIRD-PERSON 
OBSERVER
ENVIRONMENT POSSIBLY OUT OF EQUILIBRIUM 
RAW DATA WITH POSSIBLY INTRINSIC DIRECTIONALITY
ENTROPY FLOW
FIG. 19:
Self-referential observer embedded in an en-
vironment. As illustrated in Fig. 16, the variables (cir-
cles) and processes (arrows) ‘percieved’ by an observer
are here interpreted as high-level features extracted from
a raw data of an external world or environment. So, here
we make more explicit the environment which the self-
referential observer in Fig. 18c is interacting with. Such
environment can be interpreted as a physical system or as
raw data. Now, if such environment is in equilibrium, or
equivalently there is no intrinsic directionality in the raw
data, the high-lelvel representation as a circular process
in the self-referential observer is reversible and changes
in the state of one of the sub-observers (e.g. Alice) are
essentially equivalent to changes in the state of the other
sub-observer (e.g. Bob), as discussed in Fig. 18. How-
ever, when there are external inﬂuences, this is not true
any more since there is an intrinsic directionality aﬀect-
ing equally to Alice and Bob. In this case the changes
in Alice state are not equal only to changes in Bob’s
state because there is also an external contribution. This
is the analogous of the recursion theorem with external
data. To deal with this situation we notice that the ir-
reversible contributions with intrinsic directionality are
represented by the anti-symmetric parts of P and J. So,
we can still have equality between the symmetric parts,
i.e. ∆1stPA,s = −∆3rdPB,s and ∆1stPB,s = ∆3rdPA,s.


## Page 82


82
a
b
ALICE?
   BOB?
ALICE?
    BOB?
CAVITIES FOR SPINAL NERVES
FIG. 20:
Is global neural architecture the result of self-
reference?.
In this work we conjecture (see Sec. IX D)
that the two-hemisphere architecture of the brain in nor-
mal healthy humans is a large-scale feature that results
from the implementation of self-reference by the brain
(a), according to the general ideas of the recursion theo-
rem as sketched in Fig. 12 and discussed in more detail
in Appendix C. This does not imply that the two hemi-
spheres are a necessary feature for the brain to implement
self-reference. Indeed, there is evidence that removing an
hemisphere does not necessarily aﬀect a person [203]. A
possibility is that the brain implements self-reference at
diﬀerent scales. Although the decades-old theory stating
that split-brain patients, i.e. those whose corpus callo-
sum connecting the two brain hemispheres has been sev-
ered, can have divided identities has been recently chal-
lenged [153, 154], i.e. split-brain patients actually appear
to experience divided perception but undivided conscious-
ness, Corballis et al. [154] argue that subcortical connec-
tions may play a role in integrating information from the
two hemispheres. More generally, we may conjecture that
self-reference may constraint the global architecture of the
entire central nervous system, e.g. the left and right neu-
ral networks running through the spinal cord (b).


## Page 83


83
pmin
Emin
Energy of light pulse, E
Probability of correct response
Elarge
Coherence of motion, C
'Quantum' 
(Tinsley et al.)
'Classical'
(HSP)
1.00
0.50
EHSP
0.60
0.82
ESHA
CHSP
CSHA
C = 0% 
C = 50% 
C = 100% 
Experiment 1: Visual motion detection
Experiment 2: Light pulse detection
Cmin
FIG. 21: Psychophysics experiments and quantum of ac-
tion. The three dashed circles at the top illustrate the
experiment carried out by Sch¨olvinck, Howarth, and At-
twell (SHA) [125] called here ‘Experiment 1’. The small
circles with arrows illustrate the moving dots shown to the
monkeys, with the arrow specifying the direction of mo-
tion. Empty circles move randomly, while ﬁlled circles all
move upwards. The leftmost dashed circle illustrates the
case of zero coherence (C = 0), where all dots move ran-
domly; the dashed circle at the center illustrates the case
of 50% coherence (C = 50%), where half of the dots move
randomly and the other half move upwards; the right-
most dashed circle illustrates the case of full coherence
(C = 100%), where all dots move upwards. The curve at
the bottom sketches a generic psychophysics curve which
is qualitatively similar to those obtained in the three ex-
periments we analyze here (see Fig. 7 in Ref. [126] for the
HSP exeriment, Supplementary Fig. 3 in [43] for Tinsley
et al. experiment, and Fig. 2d,e,f in Ref. [125] for SHA
experiment). The top horizontal axis contains the values
of coherence C in SHA experiment. The bottom horizon-
tal axis contains values of energy that could be associated
to the coherences in SHA experiment, or to energies di-
rectly measured as in the HSP experiment [126] called
here ‘Experiment 2’ or in Tinsley et al. experiment [43].
The vertical axis contains the probability that the sub-
jects correctly respond to have seen the stimulus, i.e. the
direction of motion in SHA experiment, or energy pulses
in HSP and Tinsley et al. experiments. See Sec. IX C for
further details.


## Page 84


84
 
An Explanation 
of Channels
There are three 
main channels: 
the central 
channel, the 
right channel 
and the left 
channel. [...] 
Other names for 
the right [and left 
channels are] 
'channel of the 
subjective 
holder' [...] and 
'channel of the 
held object' [...]
Towards physical processes 
inside, e.g. via mindfulness or 
vipassana meditation
Inside the brain, CNS, 
CSF, etc. 
FIRST-PERSON RAW DATA: 
SUBJECTIVE REPORTS OF 
SEVERAL INDIVIDUALS
THIRD-PERSON RAW DATA: 
PATTERNS OF NEURAL 
ACTIVITY, PHYSICAL THEORY
INFERENCE: Identify physical correlates of subjective experience.
CONTROL: Induce similar subjective experiences via interventions.
COMPARE
ATTENTION TURNED WITHIN
FIG. 22:
Modern scientiﬁc approach to study contemplative traditions. While in the XIX century almost nobody
believed on the concept of atom, today physicists feel quite comfortable talking about such strange concepts as Higgs
bosons, antimatter, dark matter, etc. Conterintuitive concepts we never experience in everyday life. What would be
the exclamation of a XIX century scientist after hearing any of these concepts? Further theoretical and experimental
developments have been instumental for this change in attitude. Something similar might be happening today with the
almost automatic rejection some scientists feel against anything that could be labelled ‘spiritual’. Indeed, theoretical
and experimental tools are already emerging to do such a rejection on a rigorous scientiﬁc basis, or to realize we may
have been misled by partial or confusing information [22, 23]; some of those tools are considered rigorous enough
to merit a review in a top journal such as Nature Reviews Neuroscience [22].
Since contemplative traditions have
been developed many centuries ago, they tend to use a diﬃcult symbolic language that is not necessarily to be taken
literally, but rather as a pointer to certain subjective experiences that could in principle be explored with the strategy
described in Fig. 3. We could compare physical processes taking place in practitioners’ and non-practitioners’ brains,
central nervous system (CNS), cerebrospinal ﬂuid (CSF), etc, and contrast them to their subjective reports (see e.g.
Ref. [22]). Alternatively, we could follow an anthropology-like strategy and use as subjective reports books written by
representative practitioners along the centuries. Since such books have been written before our modern theories there
is no risk of self-suggested reports trying to conform to the latter. Now, Principle I tells us the observer is physical, so
we can also observe physical phenomena by turning our attention within. This is not as strange as it sounds; a simple
example is that we could have a rough estimate of our heart rate by paying attention to our own body. Much as science
has developed sophisticated tools to see beyond the capabilities of our own senses, some contemplative practices have
developed techniques, such as mindfulness and vipassana meditation, to sharpen our minds and objectively observe
internal physical processes we are not aware of in our everyday lives.
We can automatically dismiss this as total
nonsense based on long-held beliefs. Alternatively, we can try a more scientiﬁc strategy and run an experiment with
ourselves, with our own physical system, by attending a 10-day vipassana retreat, for instance.
According to the
subjective reports of many experienced meditators, deeply unconscious physical processes around the spinal cord and
brain hemispheres seem to be related to our self-concepts. Since such reports appear to have some coincidences with
the architecture of self-referential observers explored here (see Sec. X C 1), the latter might be considered a potential
physical correlate of the former. So, ﬁrst-person methods might help guide explorations on the foundations of science.
Although we can understandably worry about the faithfulness of subjective reports, the combination of these with
third-person methods can prove the consistency of the former by identifying a set of neural correlates common to most
reporting subjects. This strategy has proven useful in the study of mindfulness meditation [22], for instance, a practice
previously considered ‘spiritual’.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1705_04307v5_modeling_observers_as_physical_systems_representing_the_world_from_within_quant
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1705_04307V5_MODELING_OBSERVERS_AS_PHYSICAL_SYSTEMS_REPRESENTING_THE_WORLD_FROM_WITHIN_QUANT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

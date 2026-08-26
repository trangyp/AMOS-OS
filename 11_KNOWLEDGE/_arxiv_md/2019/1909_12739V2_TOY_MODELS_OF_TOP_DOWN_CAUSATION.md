---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1909.12739v2
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1909.12739v2_Toy_Models_of_Top_Down_Causation

> Source: 1909.12739v2_Toy_Models_of_Top_Down_Causation.pdf

> Pages: 9

---


## Page 1


Toy Models of Top Down Causation
Adrian Kent
Centre for Quantum Information and Foundations, DAMTP,
Centre for Mathematical Sciences, University of Cambridge,
Wilberforce Road, Cambridge, CB3 0WA, U.K. and
Perimeter Institute for Theoretical Physics, 31 Caroline Street North, Waterloo, ON N2L 2Y5, Canada.∗
(Dated: September 2019; updated September 2020)
Models in which causation arises from higher level structures as well as from microdynamics may
be relevant to unifying quantum theory with classical physics or general relativity. They also give a
way of deﬁning a form of panprotopsychist property dualism, in which consciousness and material
physics causally aﬀect one another. I describe probabilistic toy models based on cellular automata
that illustrate possibilities and diﬃculties with these ideas.
INTRODUCTION
The reductionist paradigm for theoretical physics suggests that the properties of complex structures, including their
dynamics, can be understood as a consequence of those of their elementary components. It is not easy to characterise
precisely what this means in all cases. Is a space-time or the vacuum state of a quantum ﬁeld a complex structure,
for example? And if so, what are their elementary components? Is a bare quark an elementary component or a
mathematical ﬁction? Is quantum entanglement a counter-example to reductionism or just an illustration that the
concept needs to be framed more carefully?
Nonetheless, it is widely agreed that some appropriately nuanced and qualiﬁed version of reductionism has been
extremely successful, so much so that many theorists seek uniﬁed theories in which all of physics is characterised by
some theory of the initial conditions together with relatively simple (though seemingly probabilistic) dynamical laws.
We should distinguish this strong but quite arguable stance from the stronger and fairly indefensible one that
understanding the fundamental laws is the only really important task in science. As Anderson compellingly argued
in his classic essay [1], solid-state physics, chemistry, biology, psychology and other higher-level theories produce new
behaviours and new laws that require great inspiration and creativity to ﬁnd and understand. But Anderson was
nonetheless a card-carrying reductionist:
The reductionist hypothesis may still be a topic for controversy among philosophers, but among the great
majority of active scientists I think it is accepted without question. The workings of our minds and bodies,
and of all the animate or inanimate matter of which we have any detailed knowledge, are assumed to be
controlled by the same set of fundamental laws, which except under certain extreme conditions we feel we
know pretty well.[1]
Chalmers’ [2] distinction between types of emergence is very helpful here. High-level phenomena are weakly emergent
when they are unexpected, but deducible in principle (even if not currently in practice) from fundamental theories.
They are strongly emergent if they are not deducible even in principle. Reductionists aim for a relatively simple
universal theory in which there are no examples of strong emergence, but should be comfortable with weak emergence.
A representative survey would be very interesting, but my guess is that Anderson’s characterisation still holds true
today: most scientists believe we already know enough of the fundamental theory to understand non-extreme regimes,
and in particular would deny that the emergence of (quasi-)classicality from quantum theory, or (pace Chalmers [2, 3])
of consciousness from classical or quantum physics, are clear examples of strong emergence. On the other hand, these
questions are hotly debated among scientists working on consciousness and on quantum foundations.
Although the boundaries of reductionism may be slightly fuzzy, we can certainly produce models or theories that are
clearly beyond them and unambiguously anti-reductionist. One example would be a theory that predicts qualitatively
diﬀerent dynamical equations for diﬀerent types of molecule.[47] Another would be a vitalist theory that predicts that
living creatures disobey some conservation law of classical mechanics. The general consensus is that we should assign
low priors to such theories, not only because reductionism has been successful, but also because reductionist theories
tend to be more elegant, and aligning credence with elegance has also been a very successful scientiﬁc methodology.
There is, though, more serious interest in better motivated models that do not ﬁt the current mainstream reduc-
tionist paradigm. Consciousness, the topic of this special issue, seems to give one than one causal narrative – mind
and matter seem to aﬀect both themselves and each other. Yet the causal eﬀects of matter on matter also seem
enough for a complete description of the material world: there is no physical evidence that the known fundamental
arXiv:1909.12739v2  [quant-ph]  21 Oct 2020


## Page 2


2
laws of physics don’t suﬃce to describe the behaviour of the brain. There are (controversial) mainstream reductionist
stances on this (e.g. [4]), but also well-known (also controversial) arguments (e.g. [3, 5–8]) against the reducibility of
consciousness to known physics. There has been an upsurge of interest lately in exploring alternative ideas involving
new (or non-standard) physical hypotheses (e.g. [9–17]). Several of these have drawn inspiration and motivation from
work on “integrated information theory” (IIT) [18] which, although open to many criticisms (e.g. [19–21], gives a
mathematical framework to explore and generalise as well as a connection to empirical data.
Ideas of top-down causation have been mooted in the context of quantum theory and more broadly (e.g. [22, 23]).
The scope for top-down causal models of consciousness has not been extensively explored, and even the meaning
and scope of top-down causation is not fully elaborated. This paper aims to give one framework for discussion, by
describing some simple toy models, inspired by cellular automata, which illustrate possible ways in which higher level
structures act causally on the microscopic components, as well as vice versa. It should be stressed that these are not
meant to capture most realistic features of the world. The aim is to illustrate scope for more realistic models that use
a similar mechanism to combine types of causation.
CELLULAR AUTOMATON 110
Our toy models are based on cellular automata, but are not meant in the spirit of the well-known research pro-
grammes aiming to describe nature at a fundamental level in terms of cellular automata [24, 25]. We use cellular
automata simply as convenient illustrations.
Wolfram [24, 26] classiﬁed the 256 elementary one-dimensional cellular automata. These are deﬁned by binary
states with a time step rule in which the states of cell n at time t are determined by those of cells n −1, n, n + 1 at
time (t −1). He noted the particularly interesting and complex behaviour of the automaton deﬁned by rule 110 in his
classiﬁcation. Again, we pick this out not out of any fundamental preference – higher-dimensional cellular automata
such the Game of Life [27] could equally well be used, for example – but for simplicity of illustration.
Rule 110 is deﬁned by
FIG. 1: The rule 110 cellular automaton. The states of cells n −1, n, n + 1 at time (t −1), given on the ﬁrst row, determine
that of cell n at time t, given on the second row.
Wolfram had previously suggested [28] that rule 110 is Turing complete, a result subsequently proved by Cook [29];
another discussion of the result is given in Ref. [24]. We review here some of its known properties, using results and
images generated by Wolfram Mathematica and resources [30] from the Wolfram Data Repository, which helpfully
includes routines that reproduce many interesting diagrams originally given in Ref. [24].
The rule generates a regular repeating array with period 14, known as the “ether”: We will take this to be the
analogue of a “vacuum” or “background state” in the toy models deﬁned below.
Some ﬁnite dislocations in the lattice-like 1D structure of a row of the ether can propagate regularly. These so-called
“gliders” generate quasi-particle-like tracks in the ether. Cook [29] classiﬁed a variety of rule 110 gliders, including some
inﬁnite classes: Colliding gliders undergo “interactions” that are superﬁcially [48] reminiscent of Feynman diagrams,
FIG. 2: The ether.


## Page 3


3
FIG. 3: Gliders.
FIG. 4: Interactions.
typically producing a ﬁnite number of stable new gliders after a ﬁnite interaction time: (For more discussion of the
general phenomena of glider “particles” and background “domains” in cellular automata, see e.g. Refs. [31–34].)
We can deﬁne a very simple model of errors or noise in these structures by considering the possibility of a single
bit ﬂip on the ﬁrst row. One might motivate this by supposing that there is something particular about the system
at t = 0 that makes errors or noise possible on the ﬁrst row, and only that row,[49] with error probability low enough
that we can neglect the possibility of two or more errors arising
If we consider a glider propagating in the ether, with a single bit of the initial state ﬂipped at a site in the ether
that is far from the glider, the eﬀect tends to be simply to cause some ripples in the ether that propagate for some
time and then peter out without interacting with the glider. The glider’s propagation is thus unaﬀected, as Fig. 5
illustrates.
However, if we ﬂip a bit close to a glider, it can interact in a way that permanently alters the number and type of
gliders. Fig. 6 shows the same glider states with one initial bit ﬂipped. Only the second is asymptotically unaﬀected.
FIG. 5: Perturbing the ether at a point distant from a glider.


## Page 4


4
FIG. 6: Perturbing the ether at a point close to a glider.
FIG. 7: Perturbations near interacting gliders. The highlighted examples leave the ﬁnal states asymptotically unchanged.
Perturbations aﬀect interacting gliders similarly. A perturbation distant from interacting gliders generally peters
out without aﬀecting them. However, perturbations in the vicinity of one or more interacting gliders may alter the
types and/or number of gliders in the ﬁnal or asymptotic state.
Fig. 7 shows a pair of interacting gliders with a single ﬂipped bit, whose site runs sequentially through 21 sites
initially located between the gliders. Of these perturbations, the 1st, 4th, 12th, 13th, 15th and 18th leave the ﬁnal
glider states, highlighted, are asymptotically unchanged. The 5th, 9th and 17th, highlighted in Fig. 8, all produce
the same new asymptotic ﬁnal state, consisting of a single glider.
PROBABILISTIC MODELS BASED ON CELLULAR AUTOMATA AND TOP-DOWN CAUSATION
A simple probabilistic model
We can formalise the model above as a 1D cellular automaton whose states are deﬁned on sites labelled by the
integers, at times also labelled by the integers. When the error probability p is zero, it is a deterministic type 110
automaton. The ether, or the ether with a single glider, then propagate indeﬁnitely without perturbation. A pair of
gliders may approach one another from inﬁnity, interact, and produce some number of outgoing gliders, which then
propagate indeﬁnitely.
We may also take the model to have ﬁnitely many spatial sites, with periodic boundary conditions. In this case,


## Page 5


5
FIG. 8: Perturbations near interacting gliders. The highlighted examples produce the same asymptotic ﬁnal state, a single
glider.
with appropriate numbers of sites, the ether and a single glider state may still propagate indeﬁnitely. If a pair of
gliders with diﬀerent velocities are evident during some time interval, they will, so to speak, interact in both the past
and future. If the interaction products contain two or more gliders with diﬀerent velocities, they in turn will interact,
and the asymptotic behaviour may be quite complex. We can avoid this by deﬁning the model only for a ﬁnite time
interval, short compared to N/v, where N is the number of sites and v the maximum glider speed.
We suppose that there is some probability p > 0 of an error occurring on the row of sites at t = 0. An error ﬂips
the bit value of a single site, so that it takes the opposite value to that predicted by the deterministic dynamics from
the state at t = −1. To simplify, we suppose that there is no probability of more than one error, and that errors are
restricted to sites x, where −M ≤x ≤M, where (2M + 1) ≤N if there are ﬁnitely many (N) sites. The errors in
this region have uniform probability, so that each site in the region has error probability
p
2M+1.
The discussion of the previous section then applies: errors suﬃciently far from any gliders at t = 0 will typically
peter out before interacting and have no eﬀect on the ﬁnal or asymptotic late time glider states; errors close to gliders
can alter the number and type of ﬁnal or asymptotic late time gliders.
Incorporating top down causation
We now consider modifying the dynamics by assigning probability weight factors to ﬁnal glider states conditional
on initial glider states.
One simple rule is to assign probability weight factor 1 to ﬁnal states that are the same as the initial state for single
glider propagation and two glider interactions, and weight factor 0 to distinct states. Formally,
pmod(Gf|Gi) = Cw(Gf|Gi)p(Gf|Gi) ,
(1)
pmod(G1
f, G2
f, . . . , Gn
f |Gi) = 0
for n ̸= 1 ,
(2)
pmod(G1
f, G2
f|G1
i , G2
i ) = C′w(G1
f, G2
f|G1
i , G2
i )p(G1
f, G2
f|G1
i , G2
i ) ,
(3)
pmod(G1
f, G2
f, . . . , Gn
f |G1
i , G2
i ) = 0
for n ̸= 2 .
(4)
Here
w(Gf|Gi) = δGf ,Gi .
(5)
Multiple glider states are listed from left to right and so
w(G1
f, G2
f|G1
i , G2
i ) = δG1
f ,G2
i δG2
f ,G1
i
(6)


## Page 6


6
for colliding gliders, while
w(G1
f, G2
f|G1
i , G2
i ) = δG1
f ,G1
i δG2
f ,G2
i
(7)
for gliders that never collide. The expression p(Gf|Gi) is the probability of the ﬁnal state containing (only) the
single glider Gf when the initial state contains glider Gi in the model of the last subsection; p(G1
f, G2
f|G1
i , G2
i ) is the
probability of the ﬁnal state containing (precisely) the pair G1
f, G2
f when the initial state contains the pair G1
i , G2
i ;
C and C′ are rescaling factors chosen so that the probabilities of all possible ﬁnal states sum to 1 for a given initial
state.
This rule is understood as applying to the system as a whole. It does not alter the deterministic dynamics of rule
110, and so its eﬀect is to alter the probabilities of errors in the state at t = 0, which are the only probabilistic feature
of the toy model. For example, for an initial state containing a single glider G, it slightly increases the probability
of errors at sites (such as those far from the glider) where they do not aﬀect the glider propagation, increases the
probability of no error, and eliminates the possibility of errors occurring at sites where they would alter the asymptotic
glider propagation. It has similar eﬀects for initial states containing two gliders G and G′. Eﬀectively, the rule acts
to suppress errors in glider propagation, ensuring the stability of one and two glider states, which would otherwise be
menaced by possible errors in the microdynamics.
A variation is to assign probability weight 1 to speciﬁed ﬁnal state outcomes of two glider interactions, and 0
otherwise, while retaining the weights above for single glider states Thus
w(Gf|Gi) = δGf ,Gi
(8)
as above but w(G1
f, G2
f, . . . , Gn
f |G1
i , G2
i ) may have a more general form. For example, we might take w(Gf|G1
i , G2
i ) = 1
for some speciﬁed ﬁnal state Gf, and zero for all other ﬁnal states. This ensures that initial glider states G1
i , G2
i always
produce ﬁnal state Gf. however small the unmodiﬁed probability of this outcome is, so long as it is nonzero.
Compatibility with standard temporal and Minkowski causation
Framed as above, these modiﬁed toy models may appear to involve something like instantaneous action at a distance,
since the probability of error at a given site at t = 0 eﬀectively depends on the type and number of gliders at distant
sites at the same time.
If we think of the models as capturing the behaviour of particles (modelled by gliders)
propagating in a background (the ether) with stochastic ﬂuctuations (the errors), in some non-relativistic limit of a
theory in relativistic space-time, this may seem to involve retrocausation: the probability of an error at a site depends
on the ﬁnal glider states in regions in its causal future.
While the models certainly could represent features of theories with non-standard causation, they are compatible
with standard causation, even for relativistic theories. We can take the relevant glider speeds to be below light speed
in such theories. The gliders contained in the state at t = 0 depend deterministically on those contained in the states
at t < 0. We can thus equally well understand the probability of error of any site at t = 0 as determined by the glider
states at suitably large negative t, when the gliders are within the site’s past light cone. Interpreted in this way, errors
at t = 0 are causally determined by glider states at large negative t, according to laws that ensure speciﬁc glider
states at large positive t. For example, one might imagine the models as capturing essential features of some deeper
theory in which this causal determination is made more explicit, by degrees of freedom that carry information away
non-superluminally from negative time glider states to sites throughout the ether and inﬂuence the error probabilities
at t = 0 appropriately.
DISCUSSION
Panprotopsychist models of consciousness
There are reasons to consider physical models of consciousness that feature top down causation (although, as with
every approach to consciousness, there are also problems and counterarguments).
One line of argument runs as
follows. There are evidently physical correlates of consciousness, namely human brains. If there is a fundamental
physical law associating conscious states to physical systems, it seems unlikely that it associates consciousness to
brains and to nothing simpler: brains seem too complex as physical systems to be the elementary referents of such


## Page 7


7
a law. Full-blown panpsychism, in which every elementary particle has an associated elementary consciousness, is a
possible alternative, but comes with many problems [35, 36] and does not seem to ﬁt naturally with neuroscientiﬁc
data and our conscious self-observations or those reported by others. The intermediate option of panprotopsychism
[37], according to which elementary consciousness is associated with some physical systems (whose nature remains to
be speciﬁed) larger than elementary particles and smaller than brains, shares some of the problems of panpsychism,
but allows more possibilities that might ﬁt with empirical observation. Taking panprotopsychism seriously means
accepting some sort of new physical law(s) associating the relevant systems with consciousness.
Our probabilistic models based on cellular automata can be taken as toy models of interactionist panprotopsychism.
In these toy models, the elementary bits at each site are meant to correspond to elementary components, and the
deterministic dynamics of rule 110 and unmodiﬁed error probability rules correspond to the elementary microdynamics.
The gliders represent physical systems associated with elements of consciousness, which we might take to be quales
or (if we stretch the present models even more unrealistically in order to illustrate how the idea might be extended)
thoughts that we can represent by a sentence such as “I see blue”. The ﬁrst modiﬁed versions of the model, in
which the error probabilities are redeﬁned to ensure that single gliders and pairs of gliders propagate unaﬀected
by errors, then correspond to toy models in which panprotopsychist consciousness ensures error suppression at the
level of consciousness, in the sense that quales (or thoughts) propagate unaﬀected in the substrate, despite errors
in the microdynamics. The second modiﬁed versions redeﬁne the error probabilities to ensure that pairs of gliders
produce speciﬁed outcomes that would not arise in the absence of errors. These correspond to toy models in which
panprotopsychist consciousness is equipped with its own dynamics, which overrides the dynamics of the substrate
when the two conﬂict.
An argument in favour of something like this picture is that, if particular physical structures are indeed singled
out as having an elementary proto-consciousness by fundamental physical laws, it is arguably natural that these
physical structures should also feature in the fundamental dynamical laws. One might even speculate that nature has
probabilistic laws because of the need to combine dual causalities, of matter and mind.
It is helpful to compare the pros and cons of this line of thought with those of a similarly panprotopsychist form
of epiphenomenalism. This would associate consciousness in a lawlike way to speciﬁed physical structures, without
modifying the microdynamics. The problem with this and other types of epiphenomenalism, as William James ﬁrst
pointed out [5], is that they leave all the apparently evolutionarily adaptive properties of consciousness unexplained.
If physical laws of consciousness do not aﬀect the microdynamics, then we and other creatures would function equally
well if we were unconscious zombies, or if pleasure and pain were uncorrelated with evolutionary advantage, or if
our consciousnesses were focussed on information that had no relevance to our survival or well-being, or if we had
“locked-in” consciousnesses disconnected from any of our communications. On this view, we have to accept that
not only the existence of consciousness, but the apparent ﬁne-tuning of its speciﬁc features, are just astonishingly
convenient coincidences.
In contrast, there is scope for more convincing explanations of the evolution of consciousness and of some of its
features if dynamics give it a genuinely causal role in behaviour. It seems plausible, for example, that eﬀectively
coupling two types of dynamical rule allows evolution to more easily produce stimulus-response circuits that are more
stable or follow higher-level reasoning. It also seems plausible that evolution would use this coupling to allow creatures
to communicate their conscious states to one another. This would allow them to coordinate their behaviour better
than communications that are inﬂuenced only by the microdynamics of their physical substrates, since in these models
their behaviour may be directly aﬀected by their conscious states. Models in which consciousness acts causally, via
laws involving its complex physical correlates, also seem to oﬀer some scope for explaining the correlation of pleasure
(pain) with evolutionary (dis)advantage.
A pain is something a conscious mind attempts to avoid, arguably by
deﬁnition, and if the dynamics of conscious states reﬂect this, then evolution could naturally exploit this dynamics
if disadvantageous physical situations created physical (brain) states that involved subsystems associated (via the
hypothesized laws) with avoidant conscious states.
Even if these arguments can be made convincing, it would still seem a surprising and fortunate coincidence that,
somewhere in the evolutionary chain, and perhaps very early, life took a material form that had proto-consciousness,
and that matter and consciousness were associated in such a way that evolution was able to make use of the dynamical
rules that give consciousness causal eﬀect (via its material correlates) on matter. A priori, one might imagine that, if
there are simple laws of psychophysical parallelism and simple associated dynamical laws, they need have nothing to
do with self-replicating chemicals or organic information processing systems. So it is fair to ask how much ﬁne-tuning
interactionist panprotopsychist theories could explain, and how much they would still leave unexplained. Still, a
partial explanation is better than none, and we also need to be clear whether we could possibly hope for a fuller
explanation given our present conceptual frameworks. After all, we are conscious. Anyone who ﬁnds conceivability
arguments [3, 38] persuasive has to accept this, and all the features of our consciousnesses, as marvellous yet contingent


## Page 8


8
features of our universe. On this view, we might hope that relatively simple laws characterise our consciousness and
explain its evolution, but we can’t hope for an argument that the laws must take the form they do.
Closer analysis of all these arguments would undoubtedly be valuable. It would also be interesting to develop more
sophisticated toy models, in which we can see rudimentary creatures evolving in a simple environment via modiﬁed
dynamics.
Quantum theory, gravity and classical physics
As these toy models illustrate, probabilistic theories of microdynamics can be simply modiﬁed so that structures at
two or more levels play roles in the fundamental laws. This makes it easy to build and explore models with top down
causation. Such models could also potentially be relevant to unifying quantum theory and gravity. For example, one
could imagine space-time emerging from a fundamentally quantum theory, within a theory in which it is equipped with
its own independent dynamical laws; in such a theory, both space-time and its quantum constituents would causally
aﬀect one another, with neither reducible to the other. The same type of relationship is possible between classical
and quantum degrees of freedom within a ﬁxed background space-time. Classical physics is normally thought of as
emerging from and reducible to quantum theory (by Everettians; see e.g. [39]) or some extension of quantum theory
that does not radically alter the dynamics (by non-Everettians who believe some extension is needed to resolve the
measurement problem). The latter looks plausible (e.g. [40, 41]) and the simplest possibility, but it is interesting to
ask how strongly empirical evidence constrains more general theories [41–44] that support this type of dual causation.
ACKNOWLEDGEMENTS
I am very grateful to the organisers and participants of the Oxford 2019 “Models of Consciousness” conference,
at which this work was presented; many of their comments and criticisms were very helpful. I would also like to
thank anonymous referees for constructive criticisms and suggestions. This work was supported by an FQXi grant,
by UK Quantum Communications Hub grant no. EP/T001011/1 and by Perimeter Institute for Theoretical Physics.
Research at Perimeter Institute is supported by the Government of Canada through Industry Canada and by the
Province of Ontario through the Ministry of Research and Innovation.
References
∗Electronic address: A.P.A.Kent@damtp.cam.ac.uk
[1] Philip W Anderson. More is diﬀerent. Science, 177(4047):393–396, 1972.
[2] David J. Chalmers. Strong and weak emergence. In P. Davies and P. Clayton, editors, The Re-Emergence of Emergence.
Oxford University Press, 2006.
[3] David Chalmers. The conscious mind: In search of a fundamental theory. Oxford University Press, USA, 1996.
[4] Daniel C Dennett. Consciousness explained. Penguin UK, 1993.
[5] William James. Are we automata? Mind, 4:1–22, 1879.
[6] Thomas Nagel. What is it like to be a bat? The Philosophical Review, 83(4):435–450, 1974.
[7] Roger Penrose. The Emperor’s New Mind: Concerning Computers, Minds, and the Laws of Physics. Oxford University
Press Oxford, 1989.
[8] Roger Penrose. Shadows of the Mind. Oxford University Press Oxford, 1994.
[9] D. Chalmers. Dirty secrets of consciousness. Talk at FQXi 5th International Conference, Banﬀ, August 2016, 2016.
[10] Lucien Hardy. Bell inequalities with retarded settings. arXiv preprint arXiv:1508.06900, 2015.
[11] Lucien Hardy. Proposal to use humans to switch settings in a Bell experiment. arXiv preprint arXiv:1705.04620, 2017.
[12] Max Tegmark. Consciousness as a state of matter. arXiv preprint arXiv:1401.1219, 2014.
[13] Max Tegmark. Consciousness is a state of matter, like a solid or gas. New Scientist, 222(2964):28–31, 2014.
[14] Max Tegmark. Improved measures of integrated information. PLoS computational biology, 12(11):e1005123, 2016.
[15] Kobi Kremnizer and Andr´e Ranchin. Integrated information-induced quantum collapse. Foundations of Physics, 45(8):
889–899, 2015.
[16] Elias Ok´on and Miguel Angel Sebasti´an. How to back up or refute quantum theories of consciousness. Mind and Matter,
14(1):25–49, 2016.


## Page 9


9
[17] David Chalmers and Kelvin McQueen.
Consciousness and the collapse of the wave function.
In Shan Gao, editor,
Consciousness and Quantum Mechanics. Oxford University Press, Forthcoming, expected 2021.
[18] Masafumi Oizumi, Larissa Albantakis, and Giulio Tononi. From the phenomenology to the mechanisms of consciousness:
integrated information theory 3.0. PLoS Comput Biol, 10(5):e1003588, 2014.
[19] Adam B Barrett. An integration of integrated information theory with fundamental physics. Frontiers in psychology, 5:
63, 2014.
[20] Michael A Cerullo. The problem with phi: a critique of integrated information theory. PLoS Comput Biol, 11(9):e1004286,
2015.
[21] Adam B Barrett and Pedro AM Mediano. The phi measure of integrated information is not well-deﬁned for general physical
systems. Journal of Consciousness Studies, 26(1-2):11–20, 2019.
[22] Yakir Aharonov, Eliahu Cohen, and JeﬀTollaksen. Completely top–down hierarchical structure in quantum mechanics.
Proceedings of the National Academy of Sciences, 115(46):11730–11735, 2018.
[23] George FR Ellis. Top-down causation and quantum physics. Proceedings of the National Academy of Sciences, 115(46):
11661–11663, 2018.
[24] Stephen Wolfram. A new kind of science. Wolfram Media, Champaign, IL, 2002.
[25] Gerard ’t Hooft. The cellular automaton interpretation of quantum mechanics. Springer Nature, 2016.
[26] Stephen Wolfram. Statistical mechanics of cellular automata. Reviews of modern physics, 55(3):601, 1983.
[27] Martin Gardner. Mathematical games: The fantastic combinations of John Conway’s new solitaire game ”life”. Scientiﬁc
American, 223(4):120–123, 1970.
[28] Stephen Wolfram. Theory and applications of cellular automata: including selected papers 1983-1986. World Scientiﬁc,
1986.
[29] Matthew Cook. Universality in elementary cellular automata. Complex systems, 15(1):1–40, 2004.
[30] Wolfram Research. Persistent structures in rule 110. In Wolfram Data Repository, 2017. URL https://doi.org/10.
24097/wolfram.75532.data.
[31] James P Crutchﬁeld and Karl Young. Inferring statistical complexity. Physical Review Letters, 63(2):105, 1989.
[32] James E Hanson and James P Crutchﬁeld. The attractor-basin portrait of a cellular automaton. Journal of statistical
physics, 66(5-6):1415–1462, 1992.
[33] James P Crutchﬁeld and James E Hanson. Turbulent pattern bases for cellular automata. Physica. D, Nonlinear phenom-
ena, 69(3-4):279–301, 1993.
[34] James P Crutchﬁeld and Melanie Mitchell. The evolution of emergent computation. Proceedings of the National Academy
of Sciences, 92(23):10742–10746, 1995.
[35] William Seager. Consciousness, information and panpsychism. Journal of Consciousness Studies, 2(3):272–288, 1995.
[36] David J Chalmers. The combination problem for panpsychism. In Godehard Bruntrup and Ludwig Jaskolla, editors,
Panpsychism: contemporary perspectives, volume 179, page 214. Oxford University Press Oxford, 2017.
[37] David Chalmers. Panpsychism and panprotopsychism. In Torin Alter and Yujin Nagasawa, editors, Consciousness in the
physical world: Perspectives on Russellian monism, pages 246–276. Oxford University Press, New York, 2015.
[38] Rocco J. Gennaro. Consciousness. The Internet Encyclopedia of Philosophy, 2018. URL http://www.iep.utm.edu/.
[39] Simon Saunders, Jonathan Barrett, Adrian Kent, and David Wallace. Many worlds?: Everett, quantum theory, & reality.
Oxford University Press, 2010.
[40] Adrian Kent. Lorentzian quantum reality: postulates and toy models. Phil. Trans. R. Soc. A, 373(2047):20140241, 2015.
[41] Adrian Kent. Quantum reality via late-time photodetection. Physical Review A, 96(6):062121, 2017.
[42] Adrian Kent. Beyond boundary conditions: General cosmological theories. In Leszek Roszkowski, editor, Particle Physics
and Cosmology: Proceedings of COSMO-97, pages 562–564. World Scientiﬁc, 1998.
[43] Adrian Kent. Beable-guided quantum theories: Generalizing quantum probability laws. Physical Review A, 87(2):022105,
2013.
[44] Adrian Kent. Hodology. arXiv preprint arXiv:2004.08223, 2020.
[45] Gian Carlo Ghirardi, Alberto Rimini, and Tullio Weber.
Uniﬁed dynamics for microscopic and macroscopic systems.
Physical Review D, 34(2):470, 1986.
[46] Gian Carlo Ghirardi, Philip Pearle, and Alberto Rimini. Markov processes in Hilbert space and continuous spontaneous
localization of systems of identical particles. Physical Review A, 42(1):78, 1990.
[47] For the theory to be unambiguously anti-reductionist, it should not be possible to derive these equations from some
simpler unifying principle. For example, dynamical collapse models [45, 46] are not anti-reductionist, although in a sense
they predict diﬀerent behaviours for molecules of low and high mass: these predictions all follow from the same stochastic
diﬀerential equation.
[48] Of course, these are deterministic classical interactions, not complex quantum interaction amplitudes.
[49] Or so much more likely that we can neglect the possibility of errors on other rows.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1909_12739v2_toy_models_of_top_down_causation
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1909_12739V2_TOY_MODELS_OF_TOP_DOWN_CAUSATION.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1903.04555v1
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1903.04555v1_Position_Measurements_and_the_Empirical_Status_of_Particles_in_Bohmian_Mechanics

> Source: 1903.04555v1_Position_Measurements_and_the_Empirical_Status_of_Particles_in_Bohmian_Mechanics.pdf

> Pages: 18

---


## Page 1


Position Measurements and the Empirical
Status of Particles in Bohmian Mechanics
Dustin Lazarovici∗
March 13, 2019
The paper addresses the debate about the empirical status of particles versus
wave functions in Bohmian quantum mechanics. It thereby clariﬁes ques-
tions and misconceptions about the role of the particles in the measurement
process, the (un)reliability of position measurements (“surrealistic trajec-
tories”), and the limited empirical access to particle positions (“absolute
uncertainty”). Taking the ontological commitment of Bohmian mechanics
seriously, all relevant empirical results follow from an analysis of the theory
in terms of particle motions. Finally, we address the question, why particle
motions rather than patterns in the wave function would be the superve-
nience base of conscious experience.
1 Introduction
Bohmian mechanics is a quantum theory based on a primitive ontology of particles and
two precise mathematical equations deﬁning their dynamics. These are the Schrödinger
equation
iℏ∂tψt = Hψt,
(1)
for the wave function, and the guiding equation
˙Xk = vψ
k,t(X) := ℏ
mk
Im∇kψt(X)
ψt(X) ,
(2)
∗Dustin.Lazarovici@unil.ch
1
arXiv:1903.04555v1  [quant-ph]  11 Mar 2019


## Page 2


in which the wave function enters to determine a velocity ﬁeld for N particles with
positions X = (X1, . . . , XN) ∈R3N. On the fundamental level, there is only one wave
function, the universal wave function, guiding the motion of all the particles together.
In many relevant situations, however, subsystems allow for an autonomous description
in terms of an eﬀective wave function determined by the universal wave function and the
actual positions of particles outside the subsystem. It can then be shown that Born’s
rule, applied to eﬀective wave functions, describes the typical distribution of particle
positions in an ensemble of identically prepared subsystems (Dürr et al., 2013, ch. 2).
With this quantum equilibrium hypothesis, the Bohmian theory reproduces the statis-
tical predictions of standard quantum mechanics (whenever the latter are well-deﬁned).
It does so by making correct statistical predictions about the outcome of measurement
experiments as recorded in the spatial conﬁguration of whatever plays the role of a
“measurement device” (Dürr et al., 2013, ch. 3).
While Bohmians generally insist that the empirical content of the theory is exhausted
by its predictions about particle motions, critics have questioned the empirical status of
the particles, usually advocating for a priority of the wave function when it comes to
relating the theory to observation (e.g. Zeh (1999); Bedard (1999); Brown and Wallace
(2005); Gao (2019b)). On this basis, it has even been argued that Bohmian mechanics
doesn’t solve the quantum measurement problem (Stone, 1994; Gao, 2019a), or that it
solves the measurement problem only by being a Many-Worlds theory in denial (Deutsch,
1996). The misleading terminology of “hidden variables” has probably done its part to
stir the debate about just how hidden the Bohmian particles actually are.
I will argue that these criticisms are based on misconceptions of the Bohmian theory
and the role of particles vis-a-vis wave functions in it. To the extent that valid questions
have been raised – in particular about the empirical accessibility of particle positions –
they are questions that can be answered. To this end, I will ﬁrst provide a brief review of
the Bohmian description of the measurement process. Section 3 will clarify the status of
particles and wave functions in Bohmian mechanics and address various worries about
the empirical (in)accessibility of particle positions.
In Section 4, I will (reluctantly)
address the issue of conscious experience and why, assuming a functionalist theory of
mind, mental states would be realized by the particles rather than the wave function.
I end with a short “dialogue” in Section 5, trying to put the discussion into a broader
perspective.
2


## Page 3


2 The measurement process in Bohmian mechanics
A prototypical measurement in Bohmian mechanics is an interaction between a system S
and a measurement device D resulting in one of several macroscopically discernible con-
ﬁgurations of D (“pointer positions”) which are correlated with certain possible quantum
states of S. Schematically, the interaction between the measured system and measure-
ment device is such that, under the Schrödinger evolution,
ϕiΦ0
Schrödinger evolution
−→
ϕiΦi ,
(3)
where the wave function Φ0 is concentrated on pointer conﬁgurations corresponding to
the “ready state” of the measurement device, and Φi are concentrated on conﬁgurations
indicating a particular measurement result, e.g., by a pointer pointing to a particular
value on a scale, a point-like region of a detector screen being darkened, a detector click-
ing or not clicking, etc. The Schrödinger time evolution is linear, so that a superposition
ϕ = c1ϕ1 + c2ϕ2,
c1, c2 ∈C,
|c1|2 + |c2|2 = 1,
leads to
ϕΦ0 = (c1ϕ1 + c2ϕ2)Φ0
Schrödinger evolution
−→
c1ϕ1Φ1 + c2ϕ2Φ2.
(4)
At this point, standard quantum mechanics is hit by the measurement problem (Maudlin,
1995a). In Bohmian mechanics, however, the system is described not only by the wave
function but also by the actual spatial conﬁguration (X, Y ) ∈Rk × Rm of measured
system and measurement device, given by the positions of their constituent particles. It
thus has a well-deﬁned conﬁguration at all times, regardless of whether or not its wave
function is in a superposition.
L
R
Φ1
Φ2
Figure 1: Sketch of the pointer wave functions on conﬁguration space.
3


## Page 4


For illustrative purposes, we assume that Φ1 is concentrated on a region L ⊂Rm of
the conﬁguration space of D corresponding to pointer-conﬁgurations pointing to the left,
while Φ2 is concentrated on a region R ⊂Rm corresponding to pointer-conﬁgurations
pointing to the right. Obviously, the two regions are disjoint, i.e. L∩R = ∅. By assump-
tion, Φ1 and Φ2 are well localized in the respective regions (otherwise, the measurement
device is no good), i.e., almost zero outside (see Fig. 1). In particular, we have
Z
L
|Φ1|2 dmy ≈1,
Z
L
|Φ2|2 dmy ≈0
(5a)
Z
R
|Φ1|2 dmy ≈0,
Z
R
|Φ2|2 dmy ≈1.
(5b)
Now, according to Bohmian mechanics, the probability of the pointer actually pointing
to the left is:
P(Y ∈L) =
Z
Rk×L
|c1ϕ1Φ1 + c2ϕ2Φ2|2 dkx dmy
= |c1|2
Z
Rk×L
|ϕ1Φ1|2dkx dmy
+ |c2|2
Z
Rk×L
|ϕ2Φ2|2dkx dmy
+ 2 Re

c1c2
Z
Rk×L
(ϕ1Φ1)∗ϕ2Φ2dkx dmy

≈|c1|2.
(6)
The ﬁnal approximation follows from eq. (5a) (together with the Cauchy-Schwarz in-
equality |
R
L Φ∗
1Φ2| ≤
qR
L |Φ1|2
qR
L |Φ2|2 ).
Similarly, the probability of the pointer
pointing to the right is P(Y ∈R) ≈|c2|2. If ϕ1 and ϕ2 are eigenstates of some quantum
observable, |c1|2 and |c2|2 are the statistical predictions of standard quantum mechanics
for an ideal measurement. (The better the pointer states Φ1 and Φ2 are localized in
disjoint regions of conﬁguration space, the closer the measurement is to “ideal”. )
Moreover, after the measurement (assuming it was not destructive), the measured
system S will be guided by the wave function ϕ1(x)Φ1(Y ) + ϕ2(x)Φ2(Y ). If the pointer
actually points left (let’s say), i.e. Y ∈L, we have Φ2(Y ) ≈0 and hence (after normal-
ization) the eﬀective wave function ϕ1 describing the system S at the end of the mea-
surement. In this way – that depends crucially on actual particle positions – Bohmian
mechanics vindicates the postulate of textbook quantum mechanics that a measurement
collapses the wave function of the measured system such that the previous outcome will
be reproduced by a repeated measurement. It does not, however, vindicate the (bad)
idea that the state ϕ1 or ϕ2 corresponds to some pre-existing property of the system
(“observable value”) that the measurement merely reveals (cf. Lazarovici et al. (2018)).
4


## Page 5


Bohmian particles have a position and nothing else, while the physical content of the
wave function is understood through its role for the dynamical and statistical description
of the particles.
3 The epistemic status of particles
Despite this central role of point particles in Bohmian mechanics – or maybe because of
it – there has been a lot of debate about their empirical status.
Some authors have suggested that Bohmian mechanics includes – or should include
– a postulate stating that measurement results are instantiated in particle positions, or
that observations “supervene” on particle positions (rather than the wave function), or
something like that (see e.g. Naaman-Marom et al. (2012)). Such a postulate is neither
helpful nor necessary, as I hope to clarify with this paper. In fact, Bohmians generally
insist (as did John Bell (2004, ch. 23)) that it is a bad idea to include postulates about
“observation” or “measurements” in any physical theory since those are much too vague
and physically complex notions.
Other authors suggest that “measurement results” in Bohmian mechanics correspond
ﬁrst and foremost to certain wave functions, while the role of the particle conﬁguration
is merely to “pick out” one part of a (decoherent) superposition as the actual result.
In particular, Brown and Wallace (2005) claim to identify such a “Result Assumption”
in the second part of David Bohm’s 1952 paper.1 I lack the historical competence to
provide a thorough exegesis of Bohm’s original work. I believe that Brown and Wallace
are reading too much into an innocuous statement, but can’t rule out the possibility
that Bohm had not yet appreciated the implications of his theory in full.
What I
can unequivocally say is that such a “Result Assumption” plays no role in the modern
understanding of Bohmian mechanics (that has been further developed by Bell, and
Dürr, Goldstein, Zanghì, among others).
Indeed, it would be a rather unproductive
assumption to make since it leaves open the critical question, how and why and in what
sense a particular wave function is supposed to “correspond to a measurement result” –
or any concrete physical fact at all.
Unsurprisingly, though, this ψ-centric reading has resonated in particular with modern
Everettians who are committed to the view that objects and events in physical space
(like measurement devices indicating a measurement result) can be recovered by some
sort of functional analysis in terms of internal degrees of freedom of the wave function
or quantum state. This, however, is not how the Bohmian theory relates to the physical
1Bohm (1952) writes: “[T]he packet entered by the apparatus variable y determines the actual result
of the measurement, which the observer will obtain when he looks at the apparatus.” (p. 182)
5


## Page 6


world, and there are legitimate questions as to whether the procedure can succeed in
general (see e.g. Monton (2006); Maudlin (2010); I will express some of my own concerns
in the course of this paper).
What Bohmian mechanics makes is an ontological commitment to particles. They are
the local beables (Bell, 2004, ch. 7) or primitive ontology (Allori et al., 2014), what
the theory postulates as the basic constituents of matter. The role of the wave function
is ﬁrst and foremost to determine the motion of particles and also (though this is a
theorem rather than an additional postulate) to describe their statistical distributions.
All our analyses of the theory are then consistent with the particles forming stable
conﬁgurations that move and behave, qualitatively and quantitatively, like the tables,
cats, measurement devices, etc. that we observe in the world. This is why the theory
is empirically adequate. In particular, the way in which the particle ontology solves
the measurement problem is not just by picking out certain parts or branches of the
wave function as guiding but by releasing the wave function from the undue burden of
representing matter in the ﬁrst place.
A point that Bohmians do repeatedly and emphatically insist on, is that making cor-
rect predictions about the spatio-temporal conﬁguration of matter – including pointer
positions, display readings, or whatever else is used to “record” the outcome of “mea-
surements” – is suﬃcient for the empirical adequacy of a physical theory (cf. Bell (2004,
p. 166)). But this is a claim about physics in general, not an additional postulate about
Bohmian measurements in particular. It is unfortunate since potentially misleading that
some authors (e.g. Gao (2019a)) mistake it for the latter.
As a nod to the neo-Everettians (and other wave function monists), it is worth pointing
out that Bohmians are also “macro-object functionalists” (Lewis (2007)) in the sense
that functionalist arguments are relevant to locating macroscopic objects in the particle
trajectories. However, while I understand how things moving and interacting in physical
space can be functionalized in terms of other things moving and interacting in physical
space, it is unintelligible to me how things moving and interacting in physical space could
be functionalized in terms of degrees of freedom of the wave function which (no matter
how you want to think about it) are not things moving and interacting in physical space.
I will return to this issue in Section 4.
3.1 Position Measurements
Some sceptics now say that this is all well and good, Bohmian mechanics may predict
that particles can form cats and tables and measurement devices that have a deﬁnite
conﬁguration at all times, but there is no good reason to believe that when we look where
6


## Page 7


a table is or whether the pointer points left or right, we will see them in the position
that the theory predicts for the particles.
The intuition behind this worry seems to be that observations are physical interactions
and that these interactions are ﬁrst and foremost described by the Schrödinger equation
for wave functions which makes no reference to Bohmian particle positions. Hence, it
may seem like observations are determined by the wave function after all, while the
particles are somehow epiphenomenal.
This reasoning is not correct, but since an observation is indeed a physical interaction,
the question here is ultimately a physical one, so let’s see what the theory actually
predicts. We recall the measurement procedure described in Section 2 with the ﬁnal
wave function of system and apparatus given by the right-hand-side of eq. (4). Now we
go one step further and consider a “measurement of the pointer position” by another
system C (we assume that the measurement device D was perfectly isolated up to this
point, so there is no environmental decoherence). We may think of an “observer” looking
at the measurement device, resulting, ultimately, in a certain particle conﬁguration of her
brain, though I prefer a camera or some other system under no suspicion of consciousness
(we will return to the issue of conscious experience in Section 4).
In any case, the
spatial resolution of such an observation can very well be ﬁner than the spread of the
“pointer states” Φi (thus corresponding to a Schrödinger evolution Φi −→P
j ΦijΨj,
where P
j Φij = Φi and the Ψj are the “record states” of C.) However, we shall consider
the simplest case in which the measurement interaction leads to a ﬁnal wave function of
the form
c1ϕ1Φ1Ψ1 + c2ϕ2Φ2Ψ2,
(7)
where Ψ1 is concentrated on a region L of the conﬁguration space of C corresponding
to the camera recording a pointer pointing left, and Ψ2 is concentrated on a region R
corresponding to the camera recording a pointer pointing right.
So what is the probability that the pointer actually points to the left, i.e. Y ∈L,
while the camera records a pointer pointing right, i.e. Z ∈R? We ﬁnd
P(Y ∈L, Z ∈R) =
Z
Rk×L×R
|c1ϕ1Φ1Ψ1 + c2ϕ2Φ2Ψ2|2 dkx dmy dnz ≈0,
(8)
since Φ2 is zero (or nearly so) on L, while Ψ1 is zero (or nearly so) on R, hence both
Φ1Ψ1 and Φ2Ψ2 are just about zero on L×R. Simply put: if you look where the pointer
is, you will typically see the pointer where it is.
How does this result square with the argument that particle positions do not matter
because interactions are described by the wave function and its Schrödinger evolution?
7


## Page 8


Figure 2: Sketch of position measurement in conﬁguration space. The dot indicates the
actual conﬁguration of the system.
Well, as I said, the argument is not correct (see also Maudlin (1995b)). It neglects the
fact that in the interaction between the systems D and C, the particle conﬁguration of
D is essential to determining which part of the wave function guides the conﬁguration
of C. It is instructive to consider an intermediate stage of the measurement interaction
(ΦL + ΦR)Ψ0 −→ΦLΨ◁+ ΦRΨ▷−→Φ1Ψ1 + Φ2Ψ2
(9)
in which the wave packets Ψ◁and Ψ▷are just beginning to separate in the conﬁguration
space of C and propagate towards the regions L and R, respecticely. Note that in the
full conﬁguration space of D + C, however, the entangled wave function ΦLΨ◁+ ΦRΨ▷
is already well-separated (decohered) along the y-coordinates (Fig. 2). Now, acccording
to the guiding equation (2), the velocity of the Z-variables is
˙Z ∝ImΦL(Y )∇zΨ◁(Z) + ΦR(Y )∇zΨ▷(Z)
ΦL(Y )Ψ◁(Z) + ΦR(Y )Ψ▷(Z)
.
(10)
Hence, if the pointer is actually left, i.e.
Y ∈L, we have ΦR(Y ) ≈0 and thus
˙Z ≈Im ∇zΨ◁(Z)
Ψ◁(Z) , so that the conﬁguration Z is eﬀectively guided by the wave packet Ψ◁
that moves towards L (i.e. towards conﬁgurations in which the photography shows the
pointer pointing left). Analogously, if the observed system is actually right, i.e. Y ∈R
the conﬁguration Z is eﬀectively guided by the wave packet Ψ▷that moves towards R
(i.e. conﬁgurations in which the photography shows the pointer pointing to the right).
Hence, the idea that the particles are causally inert, an “idle wheel”, is clearly wrong.
Indeed, it is misleading to say that interactions in Bohmian mechanics are described only
8


## Page 9


by the wave function and the Schrödinger equation; the wave function rather mediates
interactions between particles via the guiding law (2).
3.2 Atypical outcomes
If we return to the probability estimate, eq. (8), and suppose that the wave packets
Φi or Ψi have long “tails”, P(Y ∈L, Z ∈R) may indeed not be exactly zero but only
nearly so (as indicated by the ≈sign). Hence, there would be a very small, yet non-
zero probability that the pointer conﬁguration points to the left (at least for a short
period of time), while the camera – or “observer” – sees a pointer pointing to the right.
Realistically, this probability will be so small as to be practically negligible, but the
atypical outcome is still possible according to the theory. Would this mean that the
Bohmian particle conﬁguration Y does not correspond to the “real” pointer position?
No, it means precisely what the theory says, namely that there is an extremely small,
yet non-zero probability that the pointer points left, while the camera records a pointer
pointing right.
And this shouldn’t be all that surprising upon reﬂection. Also according to electro-
dynamics, it is possible, yet extremely unlikely, that I see the moon to my right while it
is actually to my left – because what I see is a very special, random ﬂuctuation in the
electromagnetic ﬁeld. It is also possible, yet extremely unlikely, that I hold a thermome-
ter (or my ﬁnger) in hot water but register a very low temperature because all the fast
particles happen to stay away from it.
Atypicality can always undermine the reliability of observations; consequently, any
inference from empirical evidence has to rely on the assumption that the evidence has
not been produced by an atypical or very-low-probability event. This is an important
insight about physics in general, not a mystery of Bohmian mechanics or quantum
mechanics in particular.
3.3 “Position measurements” that do not measure positions
There are also special measurement procedures in which the relevant “record states” Ψ1
and Ψ2 in eq. (8) would have a big overlap in the conﬁguration space of C. These include,
in particular, so-called weak measurements but also interactions that lead, for instance,
to a spin-ﬂip or the excitation of an atom, so that Ψ1 and Ψ2 are orthogonal in Hilbert
space but not separated in conﬁguration space. (This cannot be directly observed but
the “read out” that manifests in particle conﬁgurations can be delayed.) From the same
equation, it is evident that such procedures will not reliably reveal the actual particle
positions (Aharonov and Vaidman (1996); Naaman-Marom et al. (2012)). There are even
9


## Page 10


interferometer experiments, in which the naive reading of a detector is systematically
wrong about the path of a particle, in which a spin ﬂip (let’s say) is always produced
by a nonlocal eﬀect rather than a Bohmian trajectory passing nearby (nevertheless, the
measurement statistics are always correctly predicted by Bohmian mechanics).
This
has given rise to the catchy accusation that Bohmian mechanics predicts “surrealistic
trajectories” (Englert et al., 2014). In practice, decoherence prevents such situations
for macroscopic systems, but as Gisin (2018) rightly points out, there is nothing in the
Bohmian theory that makes it in principle impossible to perform such an experiment
with elephants. This is supposed to sound bad. However, stars are even bigger than
elephants and General Relativity tells us that they are not always where we see them
(literally). As Einstein reminded the young Heisenberg (2012, p. 80), it is always the
physical theory that has to tell us what can be measured and how, i.e., which physical
events are correlated in a way that allows us to infer one from the other. Bohmian
mechanics tells us that certain measurement procedures (which are much less trivial
than just “looking”) are not reliable ways to detect the position of a particle or an
elephant. Of course, concluding from this that we cannot trust observations of Bohmian
particles in general, is to commit a similar mistake as the American president when he
says that “you literally can’t see” the F-35 stealth ﬁghter.
Gisin (2018) summarizes the situation correctly by saying that not all measurements
which are called “position measurements” in standard quantum mechanics are actually
position measurements in Bohmian mechanics.2 Again, this is probably meant to sound
bad (for Bohmian mechanics). But what, in fact, is the justiﬁcation for calling these (or
any) experimental procedures “position measurements” in standard quantum mechanics?
Is it merely because their statistics can be described by some sort of “position operator”?
This is not a physical account of why and how the detector events in question should be
systematically correlated with the position of anything. Orthodox quantum mechanics is
unable to provide such an account. In fact, it doesn’t even contain localized objects with
deﬁnite positions, leading to the more basic question, what “position measurements” are
supposed to measure in the ﬁrst place.
3.4 Absolute Uncertainty
An unfortunate source of confusion about the empirical status of particle positions in
Bohmian mechnaics is the theorem of absolute uncertainty (Dürr et al., 2013, ch. 2).
This theorem states that if the eﬀective wave function of a subsystem S is ϕ, an external
observer cannot have more information about the particle conﬁguration of that system
2Another instructive example for this fact was already provided in Dürr et al. (2004, sec. 7.5).
10


## Page 11


than provided by the |ϕ|2-distribution. (“Information” here just refers to a correlation
between the conﬁguration of S and the conﬁguration of some other system – e.g. a brain
– that constitutes a “record”.) Lewis (2007, p. 757) then objects that
“this can’t be exactly right; the wavefunction, after all, doesn’t determine a
unique result for a measurement. So Bohmians note that since an observer
can know which wavepacket contains the particles, the lower bound on the
accuracy with which the particle conﬁguration can be known is actually the
squared amplitude of the occupied wave packet.”
The theorem is exactly right (it’s a theorem, after all). What Lewis seems to forget
is that in order to know the actual measurement result, an observer has to look at
(interact with) the measurement apparatus. This will eﬀectively collapse the apparatus
wave function into an “occupied” wave packet consistent with that measurement result
and the observer’s knowledge of it.3
To counter further misunderstandings, here are some things the theorem doesn’t imply:
i. Absolute uncertainty doesn’t prevent us from determining particle positions to ar-
bitrary precision (again, keeping in mind that whatever procedure we use to localize
the particle positions can also localize their wave function). Note that while one
usually states the reverse implication, we could just as well say that our knowledge
of the particle positions puts a limit on the spread of their wave function.
To measure a trajectory is, evidently, just to measure the position at diﬀerent times,
though one then has to keep in mind that since the measurement procedure can
change (eﬀectively collapse) the eﬀective wave function, it can also signiﬁcantly
change the trajectory, in particular for microscopic systems.
ii. Absolute uncertainty doesn’t prevent us from inferring additional information about
past trajectories or particle positions. For instance, in the double slit experiment
(assuming a suitably symmetric setup) we know on theoretical grounds that par-
ticles hitting the screen above/below the symmetry axis have passed through the
upper/lower slit (because Bohmian trajectories cannot cross).
iii. Absolute uncertainty sets a limit on our knowledge of a system’s particle conﬁgura-
tion in terms of its wave function. It does not say that our knowledge of a system
is limited to its wave function.
Indeed, what we can know about wave functions is an entirely diﬀerent question.
It seems evident to me that our knowledge of the wave function is usually much
3For another version of this misunderstanding, see Gao (2019a, footnote 1)).
11


## Page 12


more limited – and certainly much more indirect – than our knowledge of particle
positions. In fact, to the extent that we can measure the wave function (by so-called
“protective measurements”, see Aharonov and Vaidman (1993)), we infer it from
position measurements.
For all these reasons, attempts to use absolute uncertainty in an argument for the em-
pirical priority of wave functions over particles are thoroughly misguided.
4 Measurements and conscious experience
All that said, some authors insist that Bohmian mechanics runs into problems when the
description of the measurement process is supposed to end not with the pointer of a
measurement device (or maybe a photograph of the measurement device) but the brain
and conscious experience of an observer (e.g. Gao (2019b), see Oldofredi (2019) for a
good discussion). A priori, there are at least two reasons to be suspicious of such claims:
1. Most of the authors making them seem to misunderstand Bohmian mechanics
already as applied to measurement devices.
2. From the point of view of the physical theory, there is no essential diﬀerence be-
tween a measurement device and a brain (or whatever physical system is supposed
to be the supervenience base of conscious experience). The particle conﬁguration
of a brain records an observation in the same sense as the particle conﬁguration of
a measurement device or a photographic ﬁlm does. Everything else falls under the
mind-body problem, about which, I believe, quantum physics has nothing new to
say (cf. Loewer (2003)).
Of course, there is in general more to a “record” than a static particle conﬁguration. It
is also relevant how the system in question evolves and interacts, and this is determined
by the wave function. Thus, to the extent that there is a legitimate debate here, it comes
down to the following question (cf. Lewis (2007)):
If some functionalist theory of the mind is true, what makes it that mental
states are functionally realized by the particles rather than the wave function
which is also part of the Bohmian theory?
This objection is particularly popular among Everettians, who use it to argue that
Bohmian mechanics is a Many-Worlds theory in denial (see, in particular, Deutsch
(1996); Brown and Wallace (2005)).
Bohmian mechanics agrees, after all, that the
12


## Page 13


wave function of the universe never collapses, thus admitting all the branches that make
up the Everettian multiverse.
There are a few observations I can make in response:
a) I don’t know if any functionalist theory of the mind is true (and I wouldn’t want to
make my understanding of quantum mechanics contingent on it).
b) To apply functionalism, it must be clear what the basic objects and properties are
in terms of which the non-basic objects and properties are functionalized. In the
Bohmian theory, the basic terms are particle positions, while the wave function is
itself understood through its “functional” role for the motion of particles.
c) There are good arguments for substrate independence in the philosophy of mind, in
particular the “fading/dancing qualia” of Chalmers (1995), but I don’t see how they
would apply to particles and the wave function, even if the wave function were another
physical entity (which I don’t believe it is). It may be possible to gradually replace
a biological brain by a silicone brain while maintaining the functional organization,
but I don’t know what it would even mean to replace parts of a particle brain by
wave functions.
d) In more detail, the objection against taking particles as the physical correlates of
conscious experience is that “If the functionalist assumption is correct, for conscious-
ness to supervene on the Bohmian particles but not the wave function, the Bohmian
particles must have some functional property that the wave function do not share.
But the functional behaviour of the Bohmian particles is arguably identical to that
of the branch of the wave function in which they reside.” (Gao, 2019b, p. 306)
The last assertion is also arguably false. For instance, Bohmian mechanics allows
for the possibility that the universal wave function is stationary while all the change
in the world comes from particle motions. Changing in time versus not changing in
time is clearly a signiﬁcant functional diﬀerence. I’m not committing to a stationary
wave function, here; my point is that it cannot be a priori true that anything which
can be functionalized in terms of particles can also be functionalized in terms of the
wave function, even under a generous interpretation of functionalism.
e) On a more basic note: particles move relative to one another. The wave packets
guiding their motion (to the extent that they are even separable) don’t. They “live”
in diﬀerent dimensions of conﬁguration space and hence do not even stand in a
distance relation to one another.
13


## Page 14


Anything that allows for a functional deﬁnition in terms of matter in motion (this
arguably includes brains, though the critical question is, of course, whether it includes
“minds”) can, in principle, be realized by particles. It is not clear at all that it can
also be realized by degrees of freedom in the wave function.4
f) Another version of the objection against particles as the physical correlates of con-
scious experience is that a conscious agent would then have precise knowledge of
the particle conﬁguration of her brain, which leads to worries about faster-than-light
signaling as well as to the question, how the brain measures it’s own particle con-
ﬁguration Stone (1994). To be honest, I don’t even see how this objection gets oﬀ
the ground. Knowledge realized in (or supervenient on) brain conﬁgurations is not
knowledge about brain conﬁgurations.
In the upshot, to say that Bohmian mechanics cannot account for conscious experience
(to the extent that it is physical) is to say that particles moving in accordance with the
Bohmian laws cannot possibly be a “brain”. As far as I can tell, this claim has no basis
in physics, neuroscience, or anywhere else. On the other hand, the claim that “brains”
would have to be located in the undulating wave function rather than moving particles
is based on a variety of physical and metaphysical assumptions that are questionable, at
best. I don’t believe that physics can tell us why brain states are correlated with mental
states but I believe that physics must tell us what brains are made of. And the answer
of Bohmian mechanics is clearly and unequivocally: particles.
5 Epilogue
When all is said and done, I suspect that some readers will still insist on the question:
Supppose that Bohmian mechanics is true, how do I know that the tree in front of me is
a collection of particles rather than a pattern in the wave function?
In response, I could insist on a particular metaphysical interpretation of the wave
function and say that it is not physical stuﬀbut rather a nomological object (see e.g.
Esfeld et al. (2014)). I believe that this response is correct but doubt that it would
satisfy the questioner. Thus, if I may be more blunt, I would say: if you even ask this
4What some neo-Everettians seem to establish is nothing more than a mapping between patterns in the
wave function and trajectories in physical space. This is not even a mathematical isomorphism, let
alone a functional one. I ﬁnd it remarkable how the philosophical discussion turned to the question
whether the empirical content of Bohmian mechanics is really that of Everettian quantum mechanics
when it is not clear if Everettian quantum mechanics has any empirical content at all.
14


## Page 15


question, you still have some physical theory in mind that is not Bohmian mechanics. I
suppose that when you ﬁrst studied classical Hamiltonian mechanics, you didn’t wonder
why, according to that theory, a tree is a conﬁguration of particles rather than a pattern
in the Hamiltonian ﬂow on phase space. Physics has never been about locating trees
in an abstract mathematical formalism, only the confusions about quantum mechanics
lead to this business of “interpretation”. Instead, the scientiﬁc enterprise departs from
our “manifest image of the world” (Sellars, 1962), our observation of trees, tables, cats,
etc., and the question, what these objects are made of on the most fundamental level.
Once we have a hypothesis about the basic entities and the laws describing them, we
are in the business of locating trees (and cats, and measurement devices, etc.) in the
scientiﬁc image of the theory to see if it matches the world that we experience.
But if the world – including you – was just patterns in the wave function rather than
conﬁgurations of particles, your experience would be the same.
I doubt that this is true, and the people who claim it is, have, again, another theory
in mind than Bohmian mechanics. I agree that if trees were patterns in the wave func-
tion, Bohmian mechanics would not be the correct theory of the world. However, what
some physicists and philosophers have tried to argue is that even if Bohmian mechanics
were true, the tree in front of you would most likely be a pattern in the wave function
rather than a collection of particles. And these arguments don’t hold water; they are
question-begging at best and usually based on misconceptions of the physical theory.
I feel like you’re still avoiding the real issue, so let me rephrase it: How does it follow
FROM THE EQUATIONS of Bohmian mechanics that the tree in front of me is a con-
ﬁguration of particles rather than a pattern in the wave function?
Nothing physical follows from mathematics alone. This is why the primitive ontology
– the stuﬀthat trees are made of (or maybe instantiated in) – is a basic and indispens-
able part of any fundamental physical theory. A theory with a clear primitive ontology
can be wrong about what matters is, but it cannot be wrong about what it says that
matter is.
Acknowledgements: I am grateful to Andrea Oldofredi for helpful comments and to
Shan Gao for an inspiring discussion. I gratefully acknowledge funding by the Swiss
National Science Foundation (SNSF) Doc.Mobility Fellowship P1LAP1_184150.
15


## Page 16


References
Aharonov, Y. and Vaidman, L. (1993). Measurement of the Schrödinger wave of a single
particle. Physics Letters A, 178(1):38–42.
Aharonov, Y. and Vaidman, L. (1996). About Position Measurements Which do Not
Show the Bohmian Particle Position. In Cushing, J. T., Fine, A., and Goldstein, S.,
editors, Bohmian Mechanics and Quantum Theory: An Appraisal, Boston Studies in
the Philosophy of Science, pages 141–154. Springer Netherlands, Dordrecht.
Allori, V., Goldstein, S., Tumulka, R., and Zanghì, N. (2014). Predictions and primi-
tive ontology in quantum foundations: A study of examples. British Journal for the
Philosophy of Science, 65(2):323–352.
Bedard, K. (1999). Material Objects in Bohm’s Interpretation. Philosophy of Science,
66(2):221–242.
Bell, J. S. (2004).
Speakable and Unspeakable in Quantum Mechanics.
Cambridge:
Cambridge University Press, second edition.
Bohm, D. (1952). A suggested interpretation of the quantum theory in terms of “hidden”
variables. 2. Physical Review, 85(2):180–193.
Brown, H. and Wallace, D. (2005). Solving the Measurement Problem: De Broglie–Bohm
Loses Out to Everett. Foundations of Physics, 35(4):517–540.
Chalmers, D. J. (1995). Absent Qualia, Fading Qualia, Dancing Qualia. In Metzinger,
T., editor, Conscious Experience, pages 309–328. Ferdinand Schoningh.
Deutsch, D. (1996). Comment on Lockwood. The British Journal for the Philosophy of
Science, 47(2):222–228.
Dürr, D., Goldstein, S., and Zanghì, N. (2004). Quantum Equilibrium and the Role
of Operators as Observables in Quantum Theory.
Journal of Statistical Physics,
116(1):959–1055. Reprinted in Dürr et al. (2013, ch. 3).
Dürr, D., Goldstein, S., and Zanghì, N. (2013). Quantum Physics without Quantum
Philosophy. Berlin: Springer.
Englert, B.-G., Scully, M. O., Süssmann, G., and Walther, H. (2014). Surrealistic Bohm
Trajectories. Zeitschrift für Naturforschung A, 47(12):1175–1186.
16


## Page 17


Esfeld, M., Lazarovici, D., Hubert, M., and Dürr, D. (2014). The ontology of Bohmian
mechanics. British Journal for the Philosophy of Science, 65(4):773–796.
Gao, S. (2019a).
A contradiction in Bohm’s theory.
Preprint:
http://philsci-
archive.pitt.edu/15713/.
Gao, S. (2019b). The measurement problem revisited. Synthese, 196(1):299–311.
Gisin, N. (2018). Why Bohmian Mechanics? One- and Two-Time Position Measure-
ments, Bell Inequalities, Philosophy, and Physics. Entropy, 20(2):105.
Heisenberg, W. (2012). Der Teil und das Ganze: Gespräche im Umkreis der Atomphysik.
Piper Verlag, 9 edition.
Lazarovici, D., Oldofredi, A., and Esfeld, M. (2018). Observables and Unobservables in
Quantum Mechanics: How the No-Hidden-Variables Theorems Support the Bohmian
Particle Ontology. Entropy, 20(5):381.
Lewis, P. J. (2007). How Bohm’s Theory Solves the Measurement Problem. Philosophy
of Science, 74(5):749–760.
Loewer, B. M. (2003). Consciousness and Quantum Theory: Strange Bedfellows. In
Smith, Q. and Jokic, A., editors, Consciousness: New Philosophical Perspectives.
Oxford University Press.
Maudlin, T. (1995a). Three measurement problems. Topoi, 14(1):7–15.
Maudlin, T. (1995b). Why Bohm’s Theory Solves the Measurement Problem. Philosophy
of Science, 62(3):479–483.
Maudlin, T. (2010). Can the world be only wave-function?
In Saunders, S., Barrett,
J., Kent, A., and Wallace, D., editors, Many Worlds? Everett, Quantum Theory, and
Reality, pages 121–143. Oxford: Oxford University Press.
Monton, B. (2006).
Quantum mechanics and 3N-dimensional space.
Philosophy of
science, 73(5):778–789.
Naaman-Marom, G., Erez, N., and Vaidman, L. (2012). Position measurements in the de
Broglie–Bohm interpretation of quantum mechanics. Annals of Physics, 327(10):2522–
2542.
Oldofredi, A. (2019). Some remarks on the mentalistic reformulation of the measurement
problem: A reply to S. Gao. Synthese.
17


## Page 18


Sellars, W. (1962). Philosophy and the scientiﬁc image of man. In Colodny, R., editor,
Frontiers of Science and Philosophy, pages 35–78. Pittsburgh: University of Pittsburgh
Press.
Stone, A. D. (1994). Does the Bohm Theory Solve the Measurement Problem? Philos-
ophy of Science, 61(2):250–266.
Zeh, H. D. (1999). Why Bohm’s Quantum Theory?
Foundations of Physics Letters,
12(2):197–200.
18

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
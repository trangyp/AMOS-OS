---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1307.4628v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1307.4628v1_The_structure_of_infectious_disease_outbreaks_across_the_animal-human_interface

> Source: 1307.4628v1_The_structure_of_infectious_disease_outbreaks_across_the_animal-human_interface.pdf

> Pages: 18

---


## Page 1


The structure of infectious disease outbreaks across the animal–human interface
Sarabjeet Singh∗
Theoretical And Applied Mechanics, Sibley School of Mechanical and Aerospace Engineering, Cornell University
David J. Schneider†
Robert W. Holley Center for Agriculture and Health, Agricultural Research Service, United States Department of Agriculture,
and Department of Plant Pathology and Plant-Microbe Biology, Cornell University, Ithaca, NY 14853
Christopher R. Myers‡
Computational Biology Service Unit, Institute for Biotechnology and Life Science Technologies,
and Laboatory of Atomic and Solid State Physics, Department of Physics, Cornell University
Despite the enormous relevance of zoonotic infections to worldwide public health, and despite much effort in
modeling individual zoonoses, a fundamental understanding of the disease dynamics and the nature of outbreaks
arising in such systems is still lacking. We introduce a simple stochastic model of susceptible-infected-recovered
dynamics in a coupled animal-human metapopulation, and solve analytically for several important properties
of the coupled outbreaks. At early timescales, we solve for the probability and time of spillover, and the
disease prevalence in the animal population at spillover as a function of model parameters. At long times, we
characterize the distribution of outbreak sizes and the critical threshold for a large human outbreak, both of
which show a strong dependence on the basic reproduction number in the animal population. The coupling
of animal and human infection dynamics has several crucial implications, most importantly allowing for the
possibility of large human outbreaks even when human-to-human transmission is subcritical.
Keywords: epidemiology — zoonoses — metapopulation model — outbreak size distributions — epidemic probability —
stochastic process
I.
INTRODUCTION
Zoonoses – infectious diseases that spill over from animals
to humans – represent a major challenge in public health [1–
3]. More than half of all known human pathogens are be-
lieved to be zoonotic [1], and zoonotic pathogens are asso-
ciated with an overwhelming majority of emerging infectious
diseases [1, 4, 5]. With the conﬂuence of increased disruptions
to wildlife ecosystems and the globalization of human travel,
the threat of a zoonotic pandemic is not only heightened, but
is increasingly a part of the public’s consciousness.
Recent research has sought to characterize and classify the
salient features of zoonoses. Wolfe et al. proposed a frame-
work to describe evolutionary stages through which pathogens
might evolve from infecting only animals to infecting only
humans [9]. Lloyd-Smith et al. advocated a reﬁnement of
that framework emphasizing the importance of the value of
the basic reproduction number R0, the average number of
new human infections caused by an infectious human host
in a fully susceptible human population, in order to distin-
guish among intermediate stages that transmit to varying de-
grees in both animals and humans [3].
Morse et al. sug-
gested a different classiﬁcation that emphasizes the dynam-
ics of infection rather than pathogen properties, distinguishing
“pre-emergence” (typically spillover from one animal host to
another due to changes in habitat or land use) from “local-
ized emergence” (transmission into human populations) [10].
∗ss2365@cornell.edu
† dave.schneider@ars.usda.gov
‡ c.myers@cornell.edu
While these frameworks are all useful for suggesting further
inquiry (including ours), they are mostly descriptive in na-
ture, and since they are not tied to speciﬁc models of cross-
species infection, they cannot by themselves be probed in fur-
ther quantitative detail.
Mathematical models of zoonotic outbreaks are of increas-
ing interest, but many important gaps still remain. The compi-
lation of Lloyd-Smith et al. summarized 442 published math-
ematical models of various zoonotic diseases, concluding that
models that explicitly incorporate cross-species spillover dy-
namics are “dismayingly rare”, despite the fact that such
events are the deﬁning characteristic of zoonotic infection [3].
Many of the models summarized that do explicitly include
cross-species spillover are risk-based models describing food-
borne illness, with ﬂuxes of infection related to some un-
known level of initial contamination. These are essentially
static, and are thus not applicable in situations where infec-
tion prevalance in the animal population is itself dynamic,
as would be important for emerging zoonotic diseases. Fi-
nally, stochastic treatments of spillover dynamics are much
less common than deterministic models, a fact echoed in a
recent survey by Allen et al. [11]. Stochastic effects are ex-
pected to play dominant roles in outbreak dynamics imme-
diately after an initially unknown number of primary (cross-
species) infections have taken place. During this short period
of time, public ofﬁcials must make critical decisions based on
limited and incomplete data. Truly informed decision making
is not possible in the absence of appropriate quantiﬁcation of
uncertainties.
We address these gaps by analyzing a minimal stochastic
model of directly transmitted zoonoses that explicitly incor-
porates cross-species transmission. Our model is restricted to
arXiv:1307.4628v1  [q-bio.PE]  16 Jul 2013


## Page 2


2
epizootic situations where infection is dynamic in the animal
population, as might occur with the introduction of a disease
into an ampliﬁer animal host population [12, 13] or with the
emergence of a new, more virulent strain of an existing animal
pathogen [8, 14]. (Thus, the model is currently not applicable
to endemic animal diseases that present an approximately con-
stant force of infection to humans.) In these coupled animal-
human outbreaks, the degree of human-to-human transmis-
sion (Rhh
0
in our terminology, see below) is no longer the sole
determinant of infection prevalance in the human population,
but the degree of animal-to-animal transmission and animal-
to-human transmission also become important. Formally, our
model of zoonoses is an instance of a multitype branching pro-
cess, and using well-established mathematical techniques, we
obtain exact results for many important properties of cross-
species outbreaks without needing to examine extensive en-
sembles of stochastic numerical simulations. While a solution
to the full nonlinear problem is not forthcoming, analytical re-
sults can be derived in several important limits. At short times,
we solve for the distribution of time to spillover into the hu-
man population as well as the distribution of the prevalence of
animal infections at the time of spillover. Asymptotically at
long times where we can characterize the distribution of out-
break sizes in the human population, we identify a parameter
regime where large outbreaks are possible in human popula-
tions – sustained by repeated introductions from the animal
population – even if human-to-human transmission is subcrit-
ical (i.e., when Rhh
0
< 1). Information only about infection
in the human population is insufﬁcient to distinguish such a
scenario from one involving a single primary introduction fol-
lowed by extensive human-to-human transmission (see ﬁg. 1
bottom). Our systematic characterization of the spectrum of
possible behaviors helps to augment and clarify the previously
proposed frameworks. As with the classiﬁcation in [10], we
are ultimately interested the phenomenology of infection dy-
namics. But by tying those dynamics explicitly to a mechanis-
tic model for cross-species infection, we aim to connect that
phenomenology to particular regions in the model’s parame-
ter space, such as was advocated in [3]. We see our work as a
stepping stone toward more complex and realistic models that
might help others to address the spatial and ecological aspects
of zoonotic emergence, the evolution of virulence, and public
health interventions in the form of dynamic control strategies.
II.
MODEL
We focus here on spillover into humans from animal hosts
on relatively short timescales, where the prevalence of infec-
tion in animals changes quickly relative to other processes,
such as demographic changes in the host populations, host and
pathogen evolution, etc. We assume that the animal hosts are
not the natural reservoirs for the pathogen but receive the in-
fection through a rare event, and that infection can be passed
on directly to human hosts. The model does not include the
possibility of “spillback” or reverse infection from humans to
animals, an assumption which applies to most zoonoses.
Ours
is
a
multitype
stochastic
susceptible-infected-
Raa
0
Rah
0
⌫Rhh
0
(1 −⌫)Rhh
0
(1 −⌫)Rhh
0
⌫Rhh
0
Animal
Type 1 Human
Type 2 Human
+
+

Susceptible
Infected
Recovered
+
+
+
+
Multiple 
stuttering
chains
Single
large
outbreak




FIG. 1.
Top: Schematic of our zoonoses model (see Figure 6 in
Materials and Methods). The three–type metapopulation model con-
sists of animals, type 1 humans and type 2 humans. Type 1 humans
can receive both primary transmissions from animals and secondary
transmissions from other humans, whereas type 2 humans can only
receive a secondary transmission. Type 1 humans are fully mixed
with both animals and type 2 humans. The arrows denote R0s for
inter- and intra-population transmission. Bottom: Schematic depict-
ing two possible mechanisms for zoonotic outbreaks in human pop-
ulations: (Left) Infection spreads efﬁciently in the animal population
but inefﬁciently in humans, with each introduction into humans lead-
ing to a stuttering chain that goes extinct. (Right) An initial spillover
leads to a large outbreak sustained by human-to-human transmission.
recovered (SIR) model where the two host populations, an-
imal and human, are fully mixed within their respective
species, with a partial overlap between the species. The par-
tial overlap or the ‘mixing fraction’, ν, represents the frac-
tion of human hosts that are fully mixed with the animal hosts
(which we denote as ‘Type 1 humans’). Figure 1 (top) shows
a schematic of the model and of the underlying SIR reactions;
all reactions and reaction rates (probabilities per unit time)
are summarized in Materials and Methods. The three types of
possible infection transmission reactions are animal-to-animal
(aa), animal-to-human (ah), and human-to-human (hh).
Raa
0
and Rhh
0
are the basic reproduction numbers (average
number of new infections in a fully susceptible population)
corresponding to within-species infection (eq. 2a in Materials
and Methods). Rah
0
is deﬁned similarly for the cross-species
interaction, i.e., the average number of new infections pro-
duced by a single infected animal host in the partially-mixed,


## Page 3


3
fully-susceptible human population (eq. 2b in Materials and
Methods).
Our results are valid in the limit of large sys-
tem size for ﬁxed ratio of animal and human population size
(Na/Nh = ρ) , where the model reduces to a special case of
a multi-type branching process (see Materials and Methods).
The model includes no explicit time dependence and thus, the
time of introduction of infection into the animal population
can be taken as t = 0. This might occur, for example, fol-
lowing sudden ecological shifts that faciliate a species jump
from wildlife to livestock, or the appearance of a novel mu-
tation that provides a mechanism for an endemic pathogen to
transmit more effectively in the animal reservoir.
In the absence of cross-species infection, our model would
describe two uncoupled SIR processes. The stochastic SIR
model has been widely studied [15], and we recount here
some of its salient features.
An outbreak is deﬁned to be
small (or self-limiting) if the total number of hosts infected
is o(N) in the limit of inﬁnite system size, N →∞, i.e., its
relative size does not scale with N. Outbreaks are small with
probability 1 below the critical threshold of R0 = 1, whereas
above the critical threshold this probability is strictly positive
but less than 1. The corresponding defect in the probability
mass is the probability of large outbreaks with characteristic
sizes O(N). The average outbreak size diverges and the dis-
tribution of outbreak sizes shows a power-law scaling at the
critical threshold.
III.
RESULTS
A.
Probability of spillover
A spillover event involves one or more primary infections
in human hosts following the introduction of the disease into
the animal population at t = 0. The asymptotic (t →∞)
probability of spillover as a function of relevant model pa-
rameters (eq. A14 in Appendix) is shown in blue in Figure 2;
also shown in gray is the probability of spillover given that
there is a small outbreak in the animal population (eq. A20
in Appendix). The probability of spillover is less than 1 be-
cause the outbreak can die out in the animal population be-
fore any primary human infections occur. Deterministic mod-
els associate spillover events with large outbreaks in the an-
imal population. While large outbreaks do enhance the risk
of spillover, small outbreaks also contribute. This result indi-
cates that some spillovers may be almost impossible to trace
back in the animal population if they arise from a small out-
break where only a few animal hosts were infected and no
contact tracing data is available.
B.
Time to spillover (ﬁrst passage time)
In stochastic models, spillover between populations in-
volves a time delay, the so-called ﬁrst passage time for spread
into the human population. Figure 3 (top) shows the mean
(surface plot) and standard deviation (colormap) of the ﬁrst
passage time distribution (see Appendix for derivation). The
0
1
2
10−3
10−2
10−1
100
10−3
10−2
10−1
100
Spillover risk 
attributed to large 
animal outbreak
Probability of Spillover
FIG. 2.
Probability of spillover (blue) and the conditional proba-
bility of spillover given a small outbreak in the animal population
(gray). The dashed line marks the separation between the two sur-
faces at Raa
0
= 1. The difference between the two surfaces gives the
contribution of large animal outbreaks to spillover risk.
0
1
2
10−3
10−2
10−1
100
0
10
20
0
1
2
10−3
10−2
10−1
100
100
101
102
103
Mean First Passage Time
Mean Prevalence at Spillover
FIG. 3.
Top: The mean time to spillover (in units of the mean in-
fectious period of animal hosts) as a function of Raa
0
and Rah
0 . Col-
oring represents the standard deviation of the distribution (red:high,
blue:low spanning the range [0.4, 18.8] on a log scale). Bottom: The
number of infectious animal hosts at the time of ﬁrst primary human
infection, with coloring representing the standard deviation of the
distribution (red:high, blue:low spanning the range [10−2, 103] on a
log scale).


## Page 4


4
distribution is conditional on a spillover taking place, leading
to a non-monotonic dependence on Raa
0 . First passage times
for Raa
0
< 1 are limited by the timescale for the eventual ex-
tinction in the animal population: spillover must occur quickly
if it is going to happen at all. The expected time to extinction
in the animal population diverges as Raa
0
→1 leading to an
increase in the mean ﬁrst passage time. The mean also de-
creases with increasing Rah
0
because of the increasing rate of
animal-to-human transmission. The full distribution is use-
ful for understanding the relevant timescales of spillover and
their stochastic ﬂuctuations. This serves two important pur-
poses: ﬁrst, it indicates whether demography should be fac-
tored into the model (i.e., whether spillover will take place
on a timescale fast compared to demographic changes), and
more crucially, it suggests strategies for optimal surveillance
in the ﬁeld to pinpoint the relevant timescales and surveillance
frequencies needed to identify emerging zoonotic infections.
C.
Disease prevalence in animals at ﬁrst passage time
In the absence of animal surveillance, the ﬁrst spillover into
humans is usually the point at which the disease is ﬁrst de-
tected and control interventions are initiated [8]. While the
ﬁrst passage time reveals the timescale of spillover, the dis-
ease prevalence reveals the state of the system at spillover.
The mean and the standard deviation of the number of infec-
tious animal hosts at ﬁrst passage time Ia(T) are shown in
ﬁgure 3 (bottom). (A similar plot for the number of recov-
ered animal hosts is shown in Appendix ﬁgure A4). Given
Ia(T) = n, maximum-likelihood estimation using this distri-
bution yields a relationship among model parameters: Raa
0
=
(n −1)(Rah
0
+ 1/n). Assuming disease detection coincides
with the ﬁrst spillover event, interesting conclusions can be
drawn. For Raa
0 close to 1, the disease is likely to be detected
late, but there will be a low prevalence in the animal popula-
tion at that time. This is encouraging for public health inter-
ventions aimed at controlling the disease in the animal popu-
lation, although the long delay before detection might provide
the pathogen sufﬁcient time to evolve greater virulence. For
larger Raa
0
the spillover is likely to happen relatively early,
but the disease prevalence may be quite large, making control
difﬁcult. Our results indicate that the ﬂuctuations in the preva-
lence at spillover increase with Raa
0 , in contrast to the ﬁrst pas-
sage time which has the highest ﬂuctuations near Raa
0
= 1.
This highlights the intrinsic challenges to parameter estima-
tion in order to build predictive models based on prevalence
information.
D.
Small outbreaks and critical threshold
Unlike SIR dynamics in a single population, in our multi-
species SIR model the expected outbreak size diverges if
either Raa
0
or Rhh
0
exceeds 1 (i.e., the threshold is at
max(Raa
0 , Rhh
0 ) = 1; see Appendix). Thus, large outbreaks
in the human population are possible even if Rhh
0
< 1, which
introduces the notion of spillover-driven large outbreaks. As
in the case of the single-type SIR, small outbreaks occur
with nonzero probability throughout the parameter space of
our multitype model, albeit with decreasing probability as
the system moves beyond the critical threshold. Figure 4A
depicts the probability of a small outbreak plotted against
Raa
0
and Rhh
0
for a ﬁxed Rah
0 . Also plotted in Figure 4B-
D are the distributions of small outbreak sizes, which exhibit
power-law scaling behavior at the critical threshold bound-
ary max(Raa
0 , Rhh
0 ) = 1. There is a line of critical points at
Raa
0 = 1, 0 < Rhh
0 < 1 and at Rhh
0
= 1, 0 < Raa
0
< 1; along
both these lines, the scaling behavior is as in a simple SIR
model, with the probability of observing an outbreak of size
n decaying as P(n) ∼n−3/2 (Figure 4 B & D). While identi-
cal in the outbreak size scaling, the two lines of the threshold
boundary differ on the scaling of the average outbreak size
which scale as O(min(N 1/3
a
, N 1/2
h
)) for Raa
0 =1, 0<Rhh
0 <
1 and O(N 1/3
h
) for Rhh
0
= 1, 0 < Raa
0
< 1. This has im-
plications for determining whether the outbreak is spillover-
driven or intrinsically driven: for Nh ≫N 2/3
a
, the abun-
dance of animal hosts, rather than the human hosts, would be
a stronger predictor of the human outbreak size. Secondly, for
Nh ≪N 2/3
a
, a spillover-driven outbreak has a greater extent
of O(N 1/2
h
) as compared to an intrinsically driven outbreak
which is capped at O(N 1/3
h
). Figure 4C demonstrates that the
system exhibits a different scaling behavior, P(n) ∼n−5/4,
at the multicritical point Raa
0
= Rhh
0
= 1 with the aver-
age outbreak size scaling with population sizes Na and Nh
as O(min(N 3/4
h
, (NaN 3
h)1/7)). See Appendix for derivation
of these results, as well as comparisons between analytical re-
sults and simulations for ﬁnite-size systems. At the multicrit-
ical threshold, the outbreak sizes for the epidemics in the ani-
mal and human populations diverge simultaneously, resulting
in a new universality class with a different scaling behavior.
Our minimal model has washed out most of the small-scale
details underlying a zoonotic infection, but we expect – as is
the case with other continuous phase transitions in statistical
physics[16] – that many of those details will be irrelevant in
determining the scaling behavior near the critical threshold.
In this regard, we note that same n−5/4 scaling – arising from
one critical process driving another – has been reported re-
cently in a different, albeit related, multitype critical branch-
ing process intended to model multistage SIR infections [17].
E.
Large human outbreak
Above threshold, there is a nonzero probability of large out-
breaks in the human population. This probability (Eq. 6 in
Materials and Methods) is shown in Figure 5 (top) as a sur-
face plot in the Raa
0
– Rhh
0
plane for different values of Rah
0 .
Region B represents the probability of a spillover-driven large
outbreak.
As noted previously, these outbreaks are ‘large’
despite Rhh
0
< 1, which makes a classiﬁcation of zoonotic
infection based solely on Rhh
0
insufﬁcient for this system.
As demonstrated in Appendix (ﬁgure A10), the dynamics of


## Page 5


5
0
1
2
1
2
FIG. 4.
The distribution of sizes of small human outbreaks. (A)
Heat map for the probability that an outbreak in the human hosts is
small spanning the range [0.36 (blue), 1.0 (red)]. (B-D) Probability
of having a small outbreak of size n at different crossings of the
threshold boundary. All results are for ﬁxed Rah
0
= 0.1
a large outbreak driven by repeated spillover events can be
almost indistinguishable from one dominated by human-to-
human transmission. Region C in ﬁgure 5 (top) represents
the probability of a large human outbreak resulting from a ﬁ-
nite number (o(N)) of primary infections but sustained only
by human-to-human transmission (Rhh
0
> 1). The proba-
bility shows dependence on all three R′
0s, in contrast to the
simple SIR where the probability of large outbreak is simply
1 −1/Rhh
0 . Region D shows probability of a large outbreak
resulting from the conﬂuence of repeated spillovers and sus-
tained human-to-human transmission. The mean fraction of
hosts that are infected during a large outbreak is given by the
solution of the transcendental equations for fa (animals) and
fh (humans):
1 −fa = e−Raa
0 fa
(1a)
1 −fh = (1 −ν + νe−λfa)e−Rhh
0 fh
(1b)
λ ≡ρRah
0 /ν
(1c)
Equation 1a is the well-known equation for the ﬁnal size of a
single-type SIR. Note that equation 1b, in the limits of ν →0,
λ →0, or Raa
0
→0 reduces to the case a simple SIR as well.
All these limits represent an outbreak where the spillover only
acts as the conduit for introduction of pathogen in the human
hosts but does not affect the dynamics or ﬁnal size. As can be
veriﬁed in equation 1b, the ﬁnal size is positive for Rhh
0
< 1,
provided ν, λ, Raa
0
> 0. These are the necessary conditions
for a spillover-driven large outbreak to occur. Interestingly,
0
1
2
0
1
2
0.0
0.2
0.4
0.6
0.8
1.0
Probability of large outbreak
Mean final size of large outbreak
0
1
2
0
1
2
0.0
0.2
0.4
0.6
A
B
C
D
FIG. 5. Top: Probability of a large outbreak in humans for increas-
ing values of Rah
0
= [0.05, 0.4, 1.0]. The upper surface is parti-
tioned into 4 sections: (A) where all outbreaks are small, (B) where
spillover-driven large outbreaks are possible, (C) where large out-
breaks can only be sustained by human to human transmission, and
(D) where sustained spillover and human to human transmission re-
sult in a large outbreak. Bottom: The mean ﬁnal size of a large human
outbreak plotted against Raa
0 and Rhh
0 . The three surfaces are plotted
for ﬁxed ν = 0.5 and ρ = 1, and increasing Rah
0
= [0.05, 0.4, 1.0].
Increasing ν or λ (c.f. eq 1c) would result in the same qualitative
change in the shape of the surface. Heat map on the upper surface is
colored according to the log α (values: [0.5 (blue), 182 (red)]) where
α/√Nh is the standard deviation of relative ﬁnal size in the limit of
large Nh. The dashed lines on the uppermost surface represent the
contours at ﬁnal size = [0.2, 0.4, 0.6, 0.8]
primary infections directly transmitted from animals may not
always dominate the composition of human outbreaks even
when Rhh
0
< 1. Only for Rhh
0
< 1/2 do primary infec-
tions occur more frequently than secondary ones on average.
For 1/2 < Rhh
0
< 1, there are regions in parameter space
where secondary infections could dominate even though the
human outbreak is driven by the animal epidemic (see Ap-
pendix for proof and discussion). For small outbreaks, sec-
ondary infections strictly dominate when Rhh
0
> 1/2, a result
that has been noted previously (eq. 4 in [18]). We also cal-
culate the standard deviation of the ﬁnal size distribution as a
function of model parameters using established methods from
the theory of metapopulation models (see Appendix). Figure 5


## Page 6


6
(bottom) shows the surface plot for the mean ﬁnal size with a
colormap that is a function of the standard deviation, for one
set of model parameters. As expected, the ﬂuctuations are
the largest near the multicritical point and gradually decrease
away from it. The plot also shows how the ﬁnal outbreak size
changes as the parameters ν and λ are varied.
IV.
DISCUSSION
We have presented and analyzed a stochastic model of cou-
pled infection dynamics in an animal-human metapopulation.
While some of these results derive from the existing theory of
multitype birth-death processes [19–21], branching processes
[17, 22] and metapopulation models [23, 24], other results are
new, and this work represents the ﬁrst application of such re-
sults to the study of zoonoses. We have described spillover
from animal to human populations, but such a model – or a
variant of it – would be applicable to other cross-species infec-
tions, such as among different animal hosts. In metapopula-
tion models, the speciﬁc form of the inter-population coupling
arises from the particular processes or population structure
that one aims to address with such coupling. In our model, the
existence of a smaller, at-risk population of animal-exposed
humans is motivated in particular by the ecology of animal-
human interactions.
Different forms of coupling might be
more applicable to other cross-species infections.
The coupling of animal and human infectious disease dy-
namics results in important changes to the structure of out-
breaks in human populations as compared to those in a
human-only SIR model.
In the subcritical regime where
stuttering chains of transmission dominate, this coupling en-
hances the probability of longer chains (Figure 4C), which
could allow for greater opportunity for pathogen adaptation to
human hosts [3, 25]. The picture that emerges from our anal-
ysis of the coupled system is somewhat qualitatively different
than the zoonotic classiﬁcation schemes that have been previ-
ously proposed [3, 9]. In particular, a large outbreak can not
be attributed solely to Rhh
0
> 1: Stages II, III and IV dis-
cussed in [3, 9] can all support large outbreaks in the human
population if driven sufﬁciently hard by an animal outbreak.
This could have important ramiﬁcations for zoonotic diseases
where human-to-human transmission is not the crucial deter-
minant of the epidemic outcome such as rabies, Nipah, Hen-
dra and Menangle [8, 10]. The cross-species coupling also
complicates the problem of inference and parameter estima-
tion in the face of a new outbreak.
In addition, our analysis suggests the need to be precise
with other terminology. The term ‘stuttering chain’ has been
used in literature [3, 25] to describe a chain of infections start-
ing from a single infectious host that goes extinct without af-
fecting a signiﬁcant fraction of the host population. For the
single-type SIR model, the term is synonymous with ‘small
outbreak’ as we have deﬁned here, and the epidemic thresh-
old is the point in parameter space at which the average length
of one such chain diverges. But in our multitype SIR model,
the term ‘stuttering chain’ can not be used interchangeably
with ‘small outbreak’. Since multiple introductions can occur
in the human population, an outbreak is small if and only if
(1) a ﬁnite number of distinct infection chains occur in the hu-
man population, and (2) all such chains stutter to extinction.
A large outbreak in the human hosts occurs when any one of
these conditions is violated. Speciﬁcally, a spillover-driven
large outbreak occurs when the number of infection chains di-
verges, which can happen if Raa
0
> 1. Separately, the length
of any one such chain can diverge if Rhh
0
> 1.
The mechanistic details of our model allow us to capture
the phenomenology associated with a wide range of zoonoses.
Transmission rates reﬂect a number of ecological and im-
munological factors, which can be difﬁcult to disentangle.
We have taken a ﬁrst step in doing so by explicitly account-
ing for an at-risk human subpopulation through the ‘mixing
fraction’ ν, which describes the geographical or ecological
overlap between humans and animals. This overlap can vary
signiﬁcantly in different situations (e.g., bush-meat trade in
sub-Saharan Africa versus poultry and pig farming practices
in south-east Asia). The remaining details of animal-human
transmission remain embedded in the parameter Rah
0 , which
must be unraveled for any particular disease through further
research. Interestingly, the basic reproduction numbers are
sufﬁcient to describe the properties of an outbreak on short
timescales (e.g., time to spillover, the probability of spillover,
and distribution of sizes of small outbreaks), whereas the other
model parameters are relevant in determining the attributes of
the epidemic process at longer times (e.g., mean ﬁnal size and
variance of large outbreaks).
The community has advocated ‘model-guided ﬁeldwork’
[3, 7, 26], as well as increased collaboration between public
health scientists and ecologists in developing integrated ap-
proaches to predicting and preventing zoonotic epidemics[8].
Mathematical analysis needs to play a central role in such ac-
tivities, in order to assess the implications of model assump-
tions. The model we have analyzed certainly does not describe
all of the complexity of cross-species infection, and any more
comprehensive theory would need to account for other fac-
tors such as the ecology of interactions between wildlife and
domesticated animals, the encroachment of human develop-
ment into animal habitats, the evolution of virulence, and the
propensity for pathogens to successfully jump across species.
But in distilling some essential features of cross-species out-
breaks, we hope to identify key aspects of phenomenology,
highlight the role of important processes, and suggest further
inquiry into particular systems of interest.
V.
MATERIALS AND METHODS
A.
Model equations
See ﬁgure 6 for model reaction equations.


## Page 7


7
(Sa, Ia, Ra)
βaaSaIa/Na
−−−−−−−−→(Sa −1, Ia + 1, Ra)
(Sa, Ia, Ra)
γaIa
−−−→
(Sa, Ia −1, Ra + 1)
(Sh,1, Ih,1,p, Rh,1,p)
βahSh,1Ia/Na
−−−−−−−−−→(Sh,1 −1, Ih,1,p + 1, Rh,1,p)
(Sh,1, Ih,1,p, Rh,1,p)
γhIh,1,p
−−−−−→
(Sh,1, Ih,1,p −1, Rh,1,p + 1)
(Sh,1, Ih,1,s, Rh,1,s)
βhhSh,1Ih/Nh
−−−−−−−−−−→(Sh,1 −1, Ih,1,s + 1, Rh,1,s)
(Sh,1, Ih,1,s, Rh,1,s)
γhIh,1,s
−−−−−→
(Sh,1, Ih,1,s −1, Rh,1,s + 1)
(Sh,2, Ih,2, Rh,2)
βhhSh,2Ih/Nh
−−−−−−−−−−→(Sh,2 −1, Ih,2 + 1, Rh,2)
(Sh,2, Ih,2, Rh,2)
γhIh,2
−−−−→
(Sh,2, Ih,2 −1, Rh,2 + 1)
FIG. 6.
Model Reactions with rates (probabilities per unit time).
The subscripts ‘1’ and ‘2’ identify the type of human host. Type
1 humans can receive infection from both species.
Type 2 can
only receive infection from humans.
The subscripts ‘p’ and ‘s’
distinguish between primary and secondary infections, e.g., Ih,1,s
is the number of infected human hosts in type 1 infected via sec-
ondary transmission. Ih is the total number of human infections, i.e,
Ih = Ih,1,p + Ih,1,s + Ih,2.
B.
Basic reproduction numbers
Raa
0
= βaa
γa
,
Rhh
0
= βhh
γh
(2a)
Rah
0
= νβah
ργa
≡
ˆβah
γa
≡νλ
ρ
(2b)
C.
Multitype linear birth-death process
In the limit of large system size, a subset of the linearized
process can be summarized by the following reactions
(Ia, Ra)
βaaIa
−−−−→(Ia + 1, Ra)
(Ia, Ra)
γaIa
−−−→(Ia −1, Ra + 1)
(3)
(Ih, Zh,p, Zh,s)
ˆβahIa
−−−−→(Ih + 1, Zh,p + 1, Zh,s)
where Z⋆= I⋆+ R⋆in above process. The joint distribution of the
process (Ia, Ra, Zh,p) is generated from the following PGF (proba-
bility generating functions) which has an explicit analytical solution
[19, 22].
Gah(x, y, z; t) =
X
l,m,n
P[Ia(t)=l, Ra(t)=m, Zh,p(t)=n] xlymzn
Once the PGF Gah(x, y, z; t) is solved analytically (see Appendix),
the distribution of primary infections Zh,p(t) can be generated by
Gah(1, 1, z; t) and that of ﬁrst passage time T is extracted by noting
that
P[T ≤t] = P[Zh,p(t) > 0]
The probability of spillover is simply P[T < ∞] = P[Zh,p(∞) >
0]. Finite size corrections to the probability of spillover can be cal-
culated analytically. See Appendix for details.
D.
Multitype branching processes
The joint distribution of the number of infected animals and pri-
mary human infections at the end of an outbreak is generated by
Gah(1, y, z; ∞). This yields the following PGFs for the marginal
distributions.
Ha(y) = Gah(1, y, 1; ∞)
Hh,p(z) = Gah(1, 1, z; ∞)
(4)
The distributions of primary and secondary infections can be com-
bined assuming tree-like structure for the composite infection chains
which gives the nested PGF for the human outbreak sizes.
Hh(x) = Hh,p(x ˆHh,s(x))
(5)
where ˆHh,s(x) is the PGF for the secondary transmissions originat-
ing from a single primary (B3 in Appendix). The probability of a
large human outbreak is the defective probability mass in the distri-
bution.
P[large outbreak] = 1 −Hh(1)
(6)
E.
Finite size effects
Although the theory is derived in the limit of inﬁnite populations,
we ﬁnd a good agreement with simulations done for system sizes as
low as Na, Nh = 103. The simulations are done using Gillespie’s
direct method [27, 28].
ACKNOWLEDGMENTS
The authors would like to thank Jason Hindes, Oleg Kogan, Mar-
shall Hayes, Drew Dolgert and Jamie Lloyd-Smith for helpful dis-
cussions and comments on the manuscript. This work was supported
by the Science & Technology Directorate, Department of Homeland
Security via interagency agreement no. HSHQDC-10-X-00138.
[1] Woolhouse, MEJ & Gowtage-Sequeria, S (2005) Host range
and emerging and reemerging pathogens. Emerg. Infect. Dis.
11, 1842–1847.
[2] Kuiken, T et al. (2005) Pathogen surveillance in animals. Sci-
ence 309, 1680–1681.
[3] Lloyd-Smith, JO et al.
(2009) Epidemic dynamics at the
human-animal interface. Science 326, 1362–1367.
[4] Greger, M (2007) The human/animal interface: emergence and
resurgence of zoonotic infectious diseases. Crit. Rev. Microbiol
33, 243–299.
[5] Jones, KE et al. (2008) Global trends in emerging infectious
diseases. Nature 451, 990–993.
[6] Conti, LA & Rabinowitz, PM (2011) One health initiative. In-
fektoloˇski Glasnik 31, 176–178.


## Page 8


8
[7] Wood, JLN et al. (2012) A framework for the study of zoonotic
disease emergence and its drivers: spillover of bat pathogens
as a case study. Philos. Trans. R. Soc. Lond. B Biol. Sci 367,
2881–2892.
[8] Karesh, WB et al. (2012) Ecology of zoonoses: natural and
unnatural histories. Lancet 380, 1936–1945.
[9] Wolfe, ND, Dunavan, CP, & Diamond, J
(2007) Origins of
major human infectious diseases. Nature 447, 279–283.
[10] Morse, SS et al. (2012) Prediction and prevention of the next
pandemic zoonosis. Lancet 380, 1956–1965.
[11] Allen, LJS et al.
(2012) Mathematical modeling of viral
zoonoses in wildlife. Nat. Resour. Model. 25, 5–51.
[12] Collinge, SK & Ray, C (2006) Disease Ecology: Community
Structure and Pathogen Dynamics. (Oxford University Press,
USA).
[13] Childs, JE, Richt, JA, & Mackenzie, JS
(2007) Introduc-
tion: conceptualizing and partitioning the emergence process
of zoonotic viruses from wildlife to humans. Curr. Top. Micro-
biol. Immunol. 315, 1–31.
[14] Epstein, PR (1995) Emerging diseases and ecosystem insta-
bility: new threats to public health. Am. J. Public Health 85,
168–172.
[15] Van den Driessche, FBP, Wu, J, & Allen, LJS (2008) Mathe-
matical Epidemiology. (Springer).
[16] Sethna, JP (2006) Statistical mechanics: entropy, order param-
eters, and complexity. (Oxford Univ. Press).
[17] Antal, T & Krapivsky, PL (2012) Outbreak size distributions in
epidemics with multiple stages. J. Stat. Mech. 2012, P07018.
[18] Blumberg, S & Lloyd-Smith, JO (2013) Inference of R0 and
transmission heterogeneity from the size distribution of stutter-
ing chains. PLoS Comput. Biol. 9, e1002993.
[19] Bailey, NTJ (1990) The Elements of Stochastic Processes with
Applications to the Natural Sciences. (Wiley-Interscience).
[20] Grifﬁths, DA (1972) A bivariate birth-death process which ap-
proximates to the spread of a disease involving a vector. J. Appl.
Probab. 9, 65–75.
[21] Karlin, S & Tavar´e, S. (1982) Linear birth and death processes
with killing. J. Appl. Probab. 19, 477–487.
[22] Athreya, KB & Ney, PE
(1972) Branching Processes.
(Springer-Verlag Berlin Heidelberg).
[23] Ball, F & Clancy, D (1993) The ﬁnal size and severity of a
generalised stochastic multitype epidemic model. Adv. Appl.
Probab. 25, 721–736.
[24] Britton, T (2002) Epidemics in heterogeneous communities:
estimation of R0 and secure vaccination coverage. J. R. Stat.
Soc. Series B Stat. Methodol. 63, 705–715.
[25] Antia, R, Regoes, RR, Koella, JC, & Bergstrom, CT (2003)
The role of evolution in the emergence of infectious diseases.
Nature 426, 658–661.
[26] Restif, O et al. (2012) Model-guided ﬁeldwork: practical guide-
lines for multidisciplinary research on wildlife ecological and
epidemiological dynamics. Ecol. Lett. 15, 1083–1094.
[27] Gillespie, DT (1977) Exact stochastic simulation of coupled
chemical reactions. J. Phys. Chem. 81, 2340–2361.
[28] Keeling, MJ & Rohani, P (2008) Modeling Infectious Diseases
in Humans and Animals. (Princeton Univ. Press).
Appendix A: Dynamics of the multi-type birth and death
process
We investigate the multitype SIR model (ﬁgure 6 in Materials and
Methods) in the limit of Na, Nh →∞, Na/Nh →ρ. In this limit,
the process reduces to a multitype linear birth-death process. Let
Z⋆(t) = I⋆(t) + R⋆(t) where ⋆stands for particular subscripts
used in what follows. Zh,p(t) denotes the number of primary hu-
man infections and Zh,s(t) denotes the number of secondary human
infections irrespective of the human host type. The total number of
infected human hosts is then Zh(t) = Zh,p(t) + Zh,s(t). The mul-
titype linear birth-death process is summarized by the following re-
actions.
(Ia, Ra)
βaaIa
−−−−→(Ia + 1, Ra)
(Ia, Ra)
γaIa
−−−→(Ia −1, Ra + 1)
(Ih, Zh,p, Zh,s)
ˆβahIa
−−−−→(Ih + 1, Zh,p + 1, Zh,s)
(A1)
(Ih, Zh,p, Zh,s)
βhhIh
−−−−→(Ih + 1, Zh,p, Zh,s + 1)
(Ih, Zh,p, Zh,s)
γhIh
−−−→(Ih −1, Zh,p, Zh,s)
where ˆβah ≡νβah/ρ. The basic reproduction numbers associated
with the aa, ah and hh transmissions are (cf. eq. 2a, 2b in materials
and methods)
Raa
0
= βaa
γa ,
Rhh
0
= βhh
γh ,
Rah
0
= νβah
ργa ≡
ˆβah
γa
(A2)
In our model, we have used the population of the animal hosts to
dilute the per-contact rate of transmission, i.e.,
rateA-H = βahSh,1Ia
Na
(A3)
Alternatively, one might construct a different version of the model
that uses the population of at-risk human hosts to dilute the transmis-
sion rate,
˜rateA-H = βahSh,1Ia
νNh
(A4)
The choice of a particular cross-species rate depends on the context
and the animal-human ecology for a speciﬁc disease. We shall pro-
ceed with the ﬁrst description (eq. A3), but note that the results are
independent of the choice, as long as the parameter Rah
0
is rescaled
accordingly.
The distribution of the process can be solved using probability
generating functions (PGFs) [1, 2]. Let Ga(x, y, u, z, w; t) be the
PGF for the joint distribution of the dynamic variables when a sin-
gle animal host was infected at time 0. Similarly, let Gh(u, w; t)
be the PGF for the joint distribution of (Ih(t), Zh,s(t)) where a sin-
gle human host is infected at time 0 and there is no cross-species
transmission. From [1], we can write down the following backward
equation for these generating functions.
∂Ga
∂t
= Ua(Ga, y, Gh, z, w)
(A5)
∂Gh
∂t
= Uh(Gh, w)
where Ua(x, y, u, z, w) and Uh(u, w) are given by
Ua(x,y,u,z,w) = βaax2 + γay −(βaa+ ˆβah+γa)x + ˆβahxuz
Uh(u, w) = βhhu2w + γh −(βhh + γh)u
(A6)
The initial conditions for this set of equations are
Ga(x, y, u, z, w; 0) = x
Gh(u, w; 0) = u
(A7)


## Page 9


9
The equation for Gh can be solved exactly. The solution is provided
in [1, 2] and we reproduce it here.
Gh(u, w; t)= Ah(Bh−u)+Bh(u−Ah)e−βhhw(Bh−Ah)t
(Bh−u)+(u−Ah)e−βhhw(Bh−Ah)t
(A8)
where Ah(w) and Bh(w) are solutions of the following quadratic
equation such that 0 < Ah < 1 < Bh.
Rhh
0 ws2 −(Rhh
0
+ 1)s + 1 = 0
The PGF Gh quantiﬁes the distribution of a single small outbreak or
stuttering chain [3] which is disentangled from the A-H transmission
dynamics. The more interesting aspect of the zoonoses dynamics
is captured by the ﬁrst equation (for Ga). While a full analytical
solution to the process has recently been solved [4], we require the
solution to a subset of the complete process as described in the next
section.
1.
Distribution of primary human infections
The distribution of (Ia, Ra, Zh,p) is governed by a reduced set of
reaction equations.
(Ia, Ra, Zh,p)
βaaIa
−−−−→(Ia + 1, Ra, Zh,p)
(Ia, Ra, Zh,p)
γaIa
−−−→(Ia −1, Ra + 1, Zh,p)
(A9)
(Ia, Ra, Zh,p)
ˆβahIa
−−−−→(Ia, Ra, Zh,p + 1)
Let Gah(x, y, z; t) represent the PGF for the distribution of the above
process. Following the methods outlined in [2], we obtain the follow-
ing solution to the system. The distribution reported here has been
solved before in the context of a human-only epidemic process with
two types of hosts [5].
Gah(x,y,z;t)= Aa(Ba−x)+Ba(x−Aa)e−βaa(Ba−Aa)t
(Ba−x) + (x−Aa)e−βaa(Ba−Aa)t
(A10)
where Aa(y, z) and Ba(y, z) are roots of the following quadratic
equation such that 0 < Aa < 1 < Ba.
Raa
0 s2 −

Raa
0 +1+Rah
0 (1 −z)

s + y = 0
(A11)
In subsequent sections, we shall require the value of roots at the point
z = 0. Adopting notation from [6], we deﬁne
V0(y) = Aa(y, 0)
v0 = Aa(1, 0)
V1(y) = Ba(y, 0)
v1 = Ba(1, 0)
(A12)
2.
First passage time
We deﬁne the time to spillover as the ﬁrst passage time T for hu-
man infection, i.e., as the time when the ﬁrst primary infection occurs
in the human hosts.
P[T ≤t] = P[Zh,p(t) > 0]
= 1 −Gah(1, 1, 0; t)
= 1−v0(v1−1)+v1(1−v0)e−βaa(v1−v0)t
(v1 −1) + (1 −v0)e−βaa(v1−v0)t
(A13)
0
2
4
6
8
0.0
0.2
0.4
0.6
0.8
1.0
FIG. A1.
Comparison of analytical distribution given by eq. A13
(solid line) with discrete event simulation (Gillespie’s direct method)
for P[T < t] with ﬁnite system size (Na = Nh = 103). X-axis is
time normalized by the mean infectious period (1/γa), of the animal
species. The markers represent the mean of 8000 simulation runs.
1.0
2.0
3.0
0
1
2
3
1.0
2.0
3.0
0
1
2
3
0
1
2
3
Mean first passage time
FIG. A2.
Mean ﬁrst passage time plotted against Raa
0
for different
slices of Rah
0 . The spread around the mean is one standard deviation
of the distribution.
The distribution is plotted in ﬁgure A1 along with results of discrete
event simulation drawn from the underlying set of reactions. Sim-
ulations were done using Gillespie’s direct method [7] for reaction
kinetics. Figure A2 shows slices of the mean ﬁrst passage time sur-
face (ﬁgure 3 in main text) with one standard deviation spread.
It
can be seen that the distribution is defective since the disease can go
extinct in the animal population before the ﬁrst primary transmission
occurs in the human population. Thus, we can calculate the proba-
bility of spillover as
P[T < ∞] = 1 −v0
(A14)


## Page 10


10
The conditional distribution P[T < t | T < ∞] is
P[T < t | T < ∞] =
1 −e−βaa(v1−v0)t
1+
1−v0
v1−1

e−βaa(v1−v0)t
(A15)
a.
Moments of ﬁrst passage time
E[T n |T <∞] = E[T n1{T <∞}]
P[T < ∞]
= E[
 T1{T <∞}
n]
P[T < ∞]
= n
R ∞
0
tn−1 P[T1{T <∞} > t] dt
P[T < ∞]
= n(v1−v0)
Z ∞
0
tn−1e−βaa(v1−v0)t
(v1−1)+(1−v0)e−βaa(v1−v0)t dt
Let c = v1 −1, d = 1 −v0 and k = βaa(v1 −v0).
E[T n | T < ∞] = nk
βaa
Z ∞
0
tn−1e−kt
c + de−kt dt
(A16)
This is the integral of the Bose-Einstein distribution which can be
expressed using the polylogarithm function.
=
−n!
βaakn−1d Lin
−d
c

=
n!
(βaa)n (v0 −1) (v1 −v0)n−1 Lin
v0 −1
v1 −1

(A17)
where Lin(z) is the polylogarithm function of order n. Putting n =
1 in the expression, we obtain the conditional expected value of the
ﬁrst passage time.
E[T | T < ∞] =
1
βaa (1 −v0)log
v1 −v0
v1 −1

(A18)
To our knowledge, only the ﬁrst moment has been reported earlier in
[6], which was in the context of population genetics.
3.
Finite-size corrections to probability of spillover
. The probability of spillover, as calculated in eq. A14, is valid
only in the limit of Na, Nh →∞. Deviations from this result are
expected for ﬁnite system sizes, which we report here. Using the law
of total probability we can write
P[spill] = P[spill | small outbreak]·P[small outbreak]
+ P[spill | large outbreak]·P[large outbreak]
(A19)
where the probability is conditioned on the state of the outbreak in
the animal population. Henceforth, we shall use the symbol P∞to
represent the probability calculation done in the inﬁnite system size
limit whereas we shall use the symbol PN for probability in the ﬁnite
size calculation. For Raa
0
≤1, all outbreaks are small and there
are no corrections to eq. A14. For Raa
0
> 1, the probability of a
large outbreak is non-zero. In the inﬁnite size limit, it is implicitly
assumed that P∞[spill | large outbreak] = 1. Using this result and
P∞[large outbreak] = 1 −1/Raa
0
in eq. A19, we can calculate
P∞[spill | small outbreak] where Raa
0
> 1.
P∞[spill | small outbreak; Raa
0
> 1] = 1 −Raa
0 v0
(A20)
We assume that the above result will hold for ﬁnite N as well. Since
small outbreaks are o(N) in size, their distribution is independent of
the total system size provided N ≫1. More formally, we assume
PN[spill | small outbreak] = P∞[spill | small outbreak]
Now
we
calculate
the
ﬁnite
size
equivalent
of
P∞[spill | large outbreak] using the hazard function.
For this
calculation, we ignore the ﬂuctuations around the mean and assume
that the animal epidemic obeys the deterministic SIR. Before the
ﬁrst primary infection, the entire human population is susceptible
and thus Sh,1(t) = νNh.
PN[spill | large outbreak] = 1 −exp

−
Z ∞
0
βahSh,1Ia
Na
dt

= 1 −exp
n
−NaRah
0 fa
o
(A21)
where
fa =
lim
Na→∞
E[Ra(∞)]
Na
(A22)
is obtained by solving the ﬁnal size equation for a simple SIR
1 −fa = e−R0fa
From eq. A21, PN[spill | large outbreak] →1 as Na →∞and this
agrees with the large system size limit (eq. A14). Using the law of
total probability, we now arrive at the probability of spillover with
ﬁnite size corrections.
PN[spill; Raa
0
≤1] = 1 −v0
(A23)
PN[spill; Raa
0
> 1] = 1 −v0 −

1 −
1
Raa
0

exp
n
−NaRah
0 fa
o
Figure A3 shows the comparison of ﬁnite size corrections as calcu-
lated using eq. A23 with stochastic simulations.
In the limit of vanishingly small Rah
0 , it is important to consider
the limit of Rah
0 Na as Na →∞. Let ξ = Rah
0 Na. The probability
of spillover presented in the main text (ﬁgure 2) assumes the limit of
ξ →∞. More generally, the probability of spillover simpliﬁes to
lim
Rah
0
→0
Na→∞
PN[spill; Raa
0
≤1] = 0
(A24)
lim
Rah
0
→0
Na→∞
PN[spill; Raa
0
> 1] =

1 −
1
Raa
0

·[1 −exp {−ξfa}]
Thus, depending on the value of ξ, the limiting value for the proba-
bility of spillover when Raa
0
> 1 can assume any value in the range
[0, 1 −1/Raa
0 ]. Thus, if Raa
0
≫1, then the probability of spillover
is indeterminate if there is no information about Rah
0 Na.
4.
Prevalence in the animal population at spillover
The distribution of infectious and removed hosts in the animal
population at the ﬁrst passage time can be calculated by methods out-
lined in [6]. By interpreting our process as linear birth-death-killing
(BDK) process, the distribution of infectious hosts at spillover is the
same as the distribution of killing position in the BDK process – geo-
metrically distributed with parameter 1−1/v1 where v1 was deﬁned


## Page 11


11
0
1
2
0.0
0.1
0.2
0.3
0.4
0.5
0.6
Probability of spillover
FIG. A3.
Finite-size corrections to the probability of spillover.
Dashed lines represent the analytical solution (eq. A23) for differ-
ent values of Na. Solid line represents the solution from the linear
birth-death process (eq. A14). Colored markers represents values
calculated from 10,000 simulation runs done using Gillespie’s direct
method. All results are for ﬁxed Rah
0
= 10−3
in eq. A12. The calculation can be extended to include removed
hosts as well (which was not part of the original results in [6]). The
joint distribution of infectious and removed hosts at ﬁrst passage time
is generated by the following PGF.
HS
a (x, y) = x(v1 −1)
V1(y) −x
(A25)
The surface plot for the mean number of infectious animal hosts at
ﬁrst passage time was shown in ﬁgure 3 (main text) and the same
for the number of removed animal hosts is shown in ﬁgure A4. The
distribution is sampled analytically in ﬁgure A5 and the results are
compared with stochastic simulations for ﬁnite system sizes. As seen
in the ﬁgure A5 (top), the tail of the analytical distribution overes-
timates the prevalence slightly because of epidemic saturation that
occurs in ﬁnite size SIR.
Given a prevalence of n infected animal hosts at spillover (and no
information about removed hosts), the maximum likelihood estimate
for the parameters yields the equation v1 = n/(n −1). From eq.
A11 and A12, we arrive at the following relationship between the
model parameters
Raa
0
= (n −1)

Rah
0
+ 1
n

(A26)
Appendix B: Branching Processes
Here we solve the distribution of outbreak sizes for small out-
breaks in the limit of large system size. An outbreak is small (or
self-limited) if its size is a vanishingly small fraction of the system
size in the limit N →∞. On the other hand, an outbreak whose size
is a non-trivial fraction of the system size is deﬁned a large outbreak
[8, 9].
0
1
2
10−3
10−2
10−1
100
10−2
10−1
100
101
102
103
Mean # of removed hosts at spillover
FIG. A4.
The mean number of removed animal hosts at the
ﬁrst passage time (obtained from eq.
A25) plotted as a function
of Raa
0
and Rah
0 . The surface is colored according to the standard
deviation of the distribution (red:high, blue:low spanning the range
[5 × 10−3, 1.4 × 103] on a log scale).
1.
Distribution of outbreak sizes
A generating function always describes the distribution of ﬁnite
sized components. We shall therefore assume that the outbreaks are
self-limited in this calculation. For the animal population, let Ha(z)
be the PGF for the distribution of outbreak sizes. From equation
(A10), we obtain
Ha(z) = Gah(1, z, 1; ∞) = Aa(z, 1)
= Raa
0 + 1 −
p
(Raa
0 + 1)2 −4Raa
0 z
2Raa
0
(B1)
Let Hh,p(x) be the PGF for the distribution of primary infections
in the human population. Then, from equation (A10), we obtain
Hh,p(x) = Gah(1, 1, x; ∞) = Aa(1, x)
(B2)
= Raa
0 +1+Rah
0 (1−x)−
p
(Raa
0 +1+Rah
0 (1−x))2−4Raa
0
2Raa
0
Each primary infected host in the human population acts as the
progenitor for a branching process comprising of secondary infec-
tions. Let ˆHh,s(x) be the PGF for the distribution of secondary in-
fections emanating from a primary progenitor. Then, from equation
(A8)
ˆHh,s(z) = Gh(1, z; ∞) = Ah(z)
= Rhh
0
+ 1 −
p
(Rhh
0
+ 1)2 −4Rhh
0 z
2Rhh
0 z
(B3)
The PGF for the joint distribution of primary and secondary infec-
tions can be written as
Hh(x, z) = Hh,p(x ˆHh,s(z))
(B4)
The PGF for the total number (irrespective of whether the infection
was primary or secondary) is given by
Hh(z) = Hh,p(zHh,s(z))
(B5)


## Page 12


12
100
101
102
10-5
10-4
10-3
10-2
10-1
100
101
102
10-5
10-4
10-3
10-2
10-1
100
FIG. A5. The distribution of the number of infectious animal hosts
(top), and the number of removed animal hosts (bottom) at ﬁrst pas-
sage time T for ﬁnite system size (Na = Nh = 1000). Solid line
represents the analytical solution obtained by sampling from the PGF
in eq. A25. Colored markers represents values calculated from 2·105
simulation runs done using Gillespie’s direct method. All results are
for ﬁxed Rah
0
= 0.1
Lastly, the PGF for secondary infections is given by
Hh,s(z) = Hh(1, z)
(B6)
Following [10], we can extract probability of n human hosts getting
infected using Cauchy integral formula
P[Zh(∞) = n] =
1
2πi
I Hh(z)
zn+1 dz
(B7)
where the integral is done over the unit circle |z| = 1 in the complex
plane. Similarly, the joint probability distribution can be extracted
by extending the Cauchy integral formula to higher dimensions.
P[Zh,p(∞)=m, Zh,s(∞)=n] =
1
(2πi)2
I I
Hh(x, z)
xm+1zn+1 dx dz
(B8)
where the integrals are over two unit circles in the x and z complex
planes.
2.
Critical threshold
The critical threshold is deﬁned as the point in parameter space
where the average outbreak size diverges [8, 9] and the probability of
a large outbreak becomes greater than 0. For the animal population,
E[Ra(∞)] = H′
a(1)
=
1
1 −Raa
0
(B9)
which yields the condition Raa
0
= 1 as the critical threshold. For the
human population,
E[Zh(∞)] = H′
h(1)
= H′
h,p(1)

1 + H′
h,s(1)
	
=
Rah
0
(1 −Raa
0 )(1 −Rhh
0 )
(B10)
From the above expression, the critical threshold for the human pop-
ulation is given by max(Raa
0 , Rhh
0 ) = 1.
3.
Asymptotic scaling near the critical threshold
The scaling of the outbreak sizes near the critical threshold can be
investigated through the singularity analysis of the associated gen-
erated function H(z) [11]. The dominant singularity ζ of the PGF
determines the asymptotic form for P(n) which is the probability of
having an outbreak of size n. If a given PGF can be expanded around
the singularity such that
H(z) ∼

1 −z
ζ
α
(B11)
then
P(n) ∼ζ−nn−α−1
Γ(−α)
, n →∞
(B12)
where α /∈Z>0. The asymptotic form for P(n) can be derived by
substituting eq. B11 in the Cauchy integral formula (eq. B7) and
making the following substitution
z 7→ζ

1 + t
n

(B13)
Thus, the singularity determines the exponential factor and the
asymptotic form of the generating function determines the power-
law exponent. By rescaling the function H(z) →H(zζ), the calcu-
lation of the power-law exponent is simpliﬁed since the singularity is
now located at z = 1. We now apply this analysis to the generating
function Hh(z).
Let ∆a = 1 −Raa
0
and ∆h = 1 −Rhh
0
be the distances from
the critical thresholds. We ﬁrst calculate the scaling near the thresh-
old Raa
0
= 1, i.e., |∆a| < |∆h| and |∆a| ≪1. We assume that
the parameters are such that the singularities of the generating func-
tion Hh(z) are far apart. The dominant singularity near the chosen
threshold is given by
ζa =
 
1 +
 p
Raa
0 −1
2
Rah
0
!  
1 −Rhh
0
 p
Raa
0 −1
2
Rah
0
!
= 1 + ∆h
 ∆2
a
4Rah
0
+ O(∆3
a)

(B14)


## Page 13


13
The singularity ζa determines the exponential prefactor. To obtain
the power-law scaling, the generating function can be analyzed at the
critical point (Raa
0
= 1 in this case) without loss of generality. At
the critical point ζa = 1 and the PGF Hh,p(x) simpliﬁes as follows
Hh,p(z) = 2 + Rah
0 (1 −z) −
p
Rah
0 (1 −z)(4 + Rah
0 (1 −z))
2
(B15)
For further simpliﬁcation, let z ˆHh,s(z) be denoted by ˜Hh,s(z).
Making the substitution B13 and performing a series expansion in
fractional powers of (−t/n) gives
˜Hh,s(1 + t/n) ∼1 +
t
∆hn
(B16)
Using B5, we obtain
Hh(1 + t/n) ∼1 + Rah
0
2∆h
−t
n

−
s
Rah
0
∆h
−t
n
1/2
−1
8
Rah
0
∆h
3/2−t
n
3/2
(B17)
By using the Cauchy integral formula on the asymptotic expansion
of Hh(z), we obtain
P c
a(n) ∼n−3/2
(B18)
at the threshold boundary Raa
0
= 1, Rhh
0
̸= 1. Using the exponential
prefactor obtained in eq. B14 we arrive at the asymptotic scaling for
large n near Raa
0
= 1.
Pa(n) ∼ζ−n
a
n−3/2
(B19)
Note that the scaling can be guessed by looking at the leading term in
the expansion, which in eq. B17 is (−t/n)1/2. Similarly, performing
the same steps of analysis near the critical point of Rhh
0
= 1, we
obtain
Ph(n) ∼ζ−n
h n−3/2
(B20)
where
ζh = 1 + ∆2
h
4
Near the multicritical point Raa
0
= Rhh
0
= 1, the function has a
unique singularity if the value of the function ˜Hh,s(z) at its singu-
larity ζh coincides with the singularity of the function Hh,p(z), i.e.,
1 +
 p
Raa
0 −1
2
Rah
0
= Rhh
0
+ 1
2Rhh
0
(B21)
which simpliﬁes to
∆h =
∆2
a
2Rah
0
+ O(∆3
a)
(B22)
for ∆a, ∆h ≪1. The unique singularity is given by ζh. Thus,
the correction to the pure power-law would be ζ−n
h , but only on the
curve given by eq. B22. Next, we extract the power-law scaling at
the threshold. For Raa
0
= Rhh
0
= 1,
˜Hh,s(z) = 1 −
√
1 −z
(B23)
Hh,p(z) = 2 + Rah
0 (1 −z) −
p
Rah
0 (1 −z)(4 + Rah
0 (1 −z))
2
whose functional composition yields
Hh(z) = Hh,p( ˜Hh,s(z))
Hh(z) =
2 + Rah
0
√1 −z −
q
Rah
0
√1 −z(4 + Rah
0
√1 −z)
2
Substituting B13 and performing a series expansion in fractional
powers (−t/n), we obtain the (−t/n)1/4 as the leading term. Using
Cauchy integral formula, the asymptotic scaling is given by
P c
ah(n) ∼n−5/4
(B24)
Away from the multicritical threshold but staying on the curve B22,
the asymptotic form is
Pah(n) ∼ζ−n
h n−5/4
(B25)
The problem of estimating the corrections to the power-law scaling
away from the multi-critical point and away from the curve B22 is
currently being investigated. In this case, the generating function
will have two singularities which are coalescing at the multi-critical
point. In such a scenario, there will be a crossover regime where the
power-law exponent will switch from 3/2 to 5/4 depending on the
distance from the threshold boundary.
4.
Finite size scaling at critical threshold
Using the heuristic arguments presented in [12], we can calculate
how the average outbreak size scales with system size at the thresh-
old boundary max(Raa
0 , Rhh
0 ) = 1. For brevity, we shall adopt the
following notation in this section, similar to that used in [12]
⟨n⟩a ≡E[Ra(∞)]
⟨n⟩h ≡E[Rh(∞)]
(B26)
Let Ma be the ‘maximal’ size of an outbreak in the animal popu-
lation, when Raa
0
= 1, such that an outbreak cannot exceed this size
due to depletion of susceptible hosts [12]. The effective Raa
0
for a
ﬁnite sized system reduces to
ˆRaa
0
= 1 −Ma/Na
(B27)
Using eq. B9, we obtain the following estimate for the scale of the
average outbreak size
⟨n⟩a ∼Na/Ma
(B28)
From the 3/2 scaling law for single-type SIR [12], we obtain a second
estimate for the average outbreak size
⟨n⟩a =
Ma
X
n=1
n · n−3/2 ∼
√
Ma
(B29)
Equating the two estimates and imposing self-consistency, one ob-
tains the following scaling laws (see [12])
Ma ∼N 2/3
a
,
⟨n⟩a ∼N 1/3
a
(B30)
The calculation for human outbreaks is separated into 3 cases (as
highlighted in ﬁgure 4 B,C,D). For Raa
0
= 1, Rhh
0
< 1, the average
outbreak size is given by substituting ˆRaa
0
in eq. B10
⟨n⟩h ∼Na/Ma = N 1/3
a
(B31)
The second estimate is obtained by using the scaling law of 3/2 de-
rived in eq. B19.
⟨n⟩h =
Mh
X
n=1
n−1/2 ∼
√
Mh
(B32)


## Page 14


14
103
104
105
106
107
101
102
102
101
103
104
FIG. A6.
Finite size scaling at the threshold boundary Raa
0
=
1, Rhh
0
< 1. The plot shows the scaling law for average outbreak size
in humans ⟨n⟩h ∼N 1/3
a
and crossover to N 1/2
h
when Nh ∼N 2/3
a
on a log-log plot. The points are the average of 7 × 104 stochas-
tic realizations. The dashed line has slope 1/3. (Inset) The aver-
age outbreak size ⟨n⟩h plotted against Nh on a log-log scale for
ﬁxed Na = 107. The dashed line has slope of 1/2. The points
are the average over 105 stochastic realizations.
All results for
Raa
0
= 1, Rah
0
= 0.5, Rhh
0
= 0.1.
Equating the two estimates reveals Mh ∼N 2/3
a
. If O(Na) ≫
O(N 3/2
h
), the scaling relation leads to the maximal outbreak exceed-
ing the system size, which is physically inconsistent. Thus, the max-
imal outbreak scale needs to be capped at Nh, i.e.,
Mh ∼min(N 2/3
a
, Nh)
(B33)
From B33, we can estimate that the crossover regime between the
two scales in the min function is given by Nh ∼N 2/3
a
. The scaling
of average outbreak size is given by √Mh, i.e.,
⟨n⟩h ∼min(N 1/3
a
, N 1/2
h
)
(B34)
The results are validated in ﬁgure A6. The case of Raa
0
< 1, Rhh
0
=
1 results in the same calculations as for a single-type SIR. Thus, the
scaling laws are the same as in eq. B30.
Mh ∼N 2/3
h
,
⟨n⟩h ∼N 1/3
h
(B35)
At the multicritical point, the effective basic reproduction numbers
are
ˆRaa
0
= 1 −Ma/Na,
ˆRhh
0
= 1 −Mh/Nh
From B10, we arrive at the ﬁrst estimate
⟨n⟩h ∼Na
Ma
Nh
Mh = N 1/3
a
Nh
Mh
(B36)
The second estimate is derived from eq. B24.
⟨n⟩h =
Mh
X
n=1
n−1/4 ∼M 3/4
h
(B37)
Equating the two estimates provides the scaling for the maximal out-
break size
Mh ∼

N 1/3
a
Nh
4/7
(B38)
Since the maximal outbreak can not exceed the system size
Mh ∼min

Nh,

N 1/3
a
Nh
4/7
(B39)
The scale of the average outbreak size is given by
⟨n⟩h ∼min

N 3/4
h
,
 NaN 3
h
1/7
(B40)
The crossover region in the multicritical case is Nh ∼N 4/9
a
.
5.
Probability of large outbreak
For the animal population, the probability of large outbreak is cal-
culated as
P[Ra(∞) = ∞] = 1 −Ha(1)
= 1 −
1
Raa
0
(B41)
Let the probability of large human outbreak be represented by Q.
Assuming Rah
0
> 0,
Q = 1 −Hh(1, 1)
= 1 −Hh,p(1, Hh,s(1))
(B42)
=











0
if Rhh
0
≤1 and Raa
0
≤1,
1 −
1
Raa
0
if Rhh
0
≤1 and Raa
0
> 1,
1 −Aa

1,
1
Rhh
0

if Rhh
0
> 1.
If Rhh
0
≤1, an outbreak in the human population can be large iff
the outbreak in the animal population is large. In such a case, Q is
equal to the probability of a large outbreak in the animal population,
which is a function of only Raa
0
(see ﬁg. A8). On the other hand,
if Rhh
0
> 1, a large human outbreak can occur even if the animal
outbreak is small. Figures A7 and A8 compare the analytical results
with results from stochastic simulation. Away from the phase transi-
tions at Raa
0
= 1 and Rhh
0
= 1, the results from simulation shows
good agreement with the theory. Near the phase transition, the sim-
ulation results would converge to the theory for increasing N. Since
the deﬁnition of a large outbreak becomes precise only in the limit
of large system size, there are no ﬁnite size corrections that can be
derived in this case.
Appendix C: Large outbreaks
The size of a large outbreak scales with the system size in the large
population limit. The fraction of infected hosts can be calculated in
several ways: (1) analytically solving the equivalent deterministic
system, (2) hazard function [13] and (3) bond percolation on a com-
plete graph [8, 14]. We use the hazard function to obtain the solution.
First we write down the deterministic equations for our model.


## Page 15


15
0
1
2
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Probability of large outbreak
FIG. A7. The probability of a large human outbreak for ﬁnite pop-
ulations (Na = Nh = 103). The criteria for a large outbreak was
chosen as 100 or more infected human hosts. The points represent
the result of 10,000 stochastic simulations. The solid lines represent
the analytical solution from eq. B42. The simulations do not agree
with the analytical solution near the phase transition because of the
chosen criteria for large outbreaks and ﬁnite size effects. All results
are for ﬁxed Rah
0
= 1.
1.
Deterministic Equations
The deterministic representation of the model can be summarized
through the following system of ODEs.
dSa
dτ
= −Raa
0 SaIa
dIa
dτ = Raa
0 SaIa −Ia
dRa
dτ
= Ia
dSh,1
dτ
=−λ Sh,1Ia−κ Rhh
0 Sh,1(Ih,1,p+Ih,1,s+Ih,2)
dIh,1,p
dτ
= λ Sh,1Ia −κ Ih,1,p
dIh,1,s
dτ
= κ Rhh
0 Sh,1(Ih,1,p + I1,s + Ih,2) −κ Ih,1,s
(C1)
dRh,1,p
dτ
= κ Ih,1,p
dRh,1,s
dτ
= κ Ih,1,s
dSh,2
dτ
= −κ Rhh
0 Sh,2(Ih,1,p + I1,s + Ih,2)
dIh,2
dτ
= κ Rhh
0 Sh,2(Ih,1,p + I1,s + Ih,2) −κ Ih,2
dRh,2
dτ
= κ Ih,2
where the variables S⋆, I⋆, R⋆are non-dimensional state variables
that have been normalized by the total population of the species.
0
1
2
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0
1
2
0.00
0.02
0.04
0.06
0.08
0.10
Probability of large outbreak
FIG. A8. The probability of a large human outbreak for Rhh
0
= 0.8
and varying Nh. The criteria for a large outbreak was chosen as the
number of infected hosts being greater than 1% of the total popu-
lation. The points represent the result of 10,000 stochastic simula-
tions. The solid line is the analytical solution max(0, 1 −1/Raa
0 ).
(Inset) The absolute difference between the analytical solution and
ﬁnite size resuls. All results are for ﬁxed Rah
0
= 0.1.
Here, all dynamical variables for the human population are normal-
ized by Nh and time is normalized by the average infectious period
of the animal hosts. Two new variables are introduced here
λ = ρRah
0
ν
,
κ = γh
γa
(C2)
The non-dimensional parameters governing the dynamics of the sys-
tem are: (Raa
0 , λ, Rhh
0 , κ). The initial conditions that we use to solve
this system are given below
Sa(0) = 1 −1
Na , Ia(0) =
1
Na , Ra(0) = 0
Sh,1(0) = ν, Sh,2(0) = 1 −ν, Ih,⋆(0) = 0, Rh,⋆(0) = 0
2.
Mean ﬁnal size
Let f⋆be the relative size of the infected hosts in the various host
compartments in the limit of large system size for the stochastic ver-
sion of the model.
fa =
lim
Na→∞
E[Ra(∞)]
Na
fh,p =
lim
Nh→∞
E[Rh,1,p(∞)]
Nh
fh,s =
lim
Nh→∞
E[Rh,1,s(∞)] + E[Rh,2(∞)]
Nh
(C3)
fh,1 =
lim
Nh→∞
E[Rh,1,p(∞)] + E[Rh,1,s(∞)]
Nh
fh,2 =
lim
Nh→∞
E[Rh,2(∞)]
Nh
fh = fh,1 + fh,2
= fh,p + fh,s


## Page 16


16
Using survival analysis described in [13], we proceed with calcula-
tions for the various f⋆. The calculation is based on the result that in
the limit of large system size the ﬁnal epidemic size is the same as
that given by solving the deterministic system of equations, i.e.,
f⋆= R⋆(∞)
(C4)
For a randomly chosen susceptible host in the animal population, the
cumulative hazard function is the probability of not getting infected
before time t. This function can be calculated as follows
Λaa(t) = e−
R t
0 βaaIads
(C5)
At steady state, the hazard function simpliﬁes as follows
Λaa(∞) = e−Raa
0
Ra(∞) = e−Raa
0
fa
(C6)
The probability of escaping infection would be 1 −fa. Equating this
with equation (C6), we obtain
1 −fa = e−Raa
0
fa
(C7)
Similarly for the human hosts, we ﬁrst look at type 1 hosts (who are at
risk of both primary and secondary transmissions). The hazard func-
tions for the animal to human and human to human transmissions are
given by
Λah(∞) = e−λfa
Λhh(∞) = e−Rhh
0
fh
(C8)
A randomly chosen type 1 human host will not be infected during a
large outbreak only if it escapes getting infected from both the pri-
mary and secondary transmissions.
fh,1 = ν

1 −e−λfae−Rhh
0
fh
(C9)
The prefactor ν is to normalize the relative size of the epidemic by
size of the population of type 1 human hosts. Similarly, we can cal-
culate the size of the epidemic in type 2 hosts.
fh,2 = (1 −ν)

1 −e−Rhh
0
fh
(C10)
The total size of the epidemic in the human population is obtained
by adding equations C9 and C10
fh = fh,1 + fh,2
fh = 1 −

1 −ν + νe−λfa
e−Rhh
0
fh
(C11)
The solution of the implicit equation C7 feeds in to equation C11
whose solution can then be used to solve equations C9 and C10. In
the absence of secondary transmissions, i.e, Rhh
0
= 0, the epidemic
in the type 1 hosts would only consist of primary infections. Let this
fraction of infected hosts be denoted by f 0
h,p, which can be obtained
by setting Rhh
0
to 0 in equation C9.
f 0
h,p = ν

1 −e−λfa
(C12)
Immediately comparing equations C9 and C12, we can assert that
f 0
h,p ≤fh,1
(C13)
with the equality holding for Rhh
0
= 0. Note that fh,p ̸= f 0
h,p since
f 0
h,p is the size of the epidemic in the absence of human to human
transmissions whereas fh,p is the size of the epidemic when both
forces of infection are active. In the latter scenario, the two forces of
infection would be competing for a susceptible. Thus, the proportion
of the epidemic caused by primary infections would be reduced as
compared to the case where only the primary transmission is active.
fh,p ≤f 0
h,p
(C14)
For the last part of the analysis, consider a randomly chosen infected
type 1 human host i. This host is exposed to both primary and sec-
ondary forces of infection. Let T (i)
h,p be the time when this host re-
ceives disease via a primary transmission. Similarly, let T (i)
h,s be the
time when the host receives disease via a secondary transmission.
If T (i)
h,p < T (i)
h,s, a primary infection is realized else a secondary in-
fection is realized. Note that the idea of multiple transmissions is a
mathematical construct rather than a biological realism. A host that
has already been infected and recovered can not be infected again (in
the SIR framework). But the host is still subjected to the second force
of infection which can result in another successful (albeit redundant)
transmission. From the analogy with reaction kinetics [7], it is impor-
tant to know which transmission reaction ﬁred ﬁrst since that would
determine whether the infection was primary or secondary. We can
now write down an expression for the relative size of the epidemic
consisting of primary infections.
fh,p = ν · P[T (i)
h,p < T (i)
h,s]
(C15)
= ν

P[T (i)
h,p <T (i)
h,s, T (i)
h,s =∞] + P[T (i)
h,p <T (i)
h,s, T (i)
h,s <∞]

= ν e−Rhh
0
fh 
1 −e−λfa
fh,1 + ν P[T (i)
h,p < T (i)
h,s < ∞]
≥fh,p\s
where
fh,p\s ≡ν e−Rhh
0
fh 
1 −e−λfa
fh,1
(C16)
Combining equations C13, C14 and C16, we get
fh,p\s ≤fh,p ≤f 0
h,p ≤fh,1
(C17)
where the equality holds for Rhh
0
= 0.
3.
Primary vs Secondary
Figure A9 shows the average number of primary and secondary
infections occurring during a large outbreak for different values of ν
and Rhh
0 . The solutions were obtained by solving the deterministic
equations (eq. C1). The curve for the primary infections will always
be non-decreasing with ν. This follows from intuition that as more
and more susceptible hosts become at risk, the number of primary in-
fections will also increase. The fact that the effective R0 for the A-H
transmissions, i.e., Rah
0
also increases with ν compounds the effect.
The secondary infections on the other hand exhibit non-monotonicity
in some regions of parameter space. This can be attributed to the
love-hate relationship between the two forces of infection (ah and
hh) acting on susceptible human hosts. On one hand, the secondary
infections cannot occur unless there are primary infections. Thus,
for small values of ν, there is a strong correlation between the num-
ber of primary and secondary infections. On the other hand, as ν
increases, the two forces start competing for the same susceptible
hosts. Depending on the model parameters, either of the two forces
can dominate in different regions of the phase space which leads to
the rich behavior for the number of secondary infections.


## Page 17


17
0.0
0.2
0.4
0.6
0.8
1.0
0.1
0.2
0.3
0.4
0.0
0.2
0.4
0.6
0.8
1.0
0.1
0.2
0.3
0.4
FIG. A9. Fraction of human hosts infected during a large outbreak
via a primary transmission (fh,p, blue), and secondary transmission
(fh,s, green) plotted for different values of ν and Rhh
0 . Analytical
solution obtained from solving the deterministic system. Remaining
parameters for the plots: Na = Nh = 1000, βaa = 2.0, ˆβah =
1.5, γa = γh = 1.0
4.
Bifurcation point
As evident from ﬁgure A9, the curves fh,p and fh,s when plotted
against ν may or may not intersect apart from ν = 0. Here we calcu-
late the condition under which the bifurcation would occur creating
a second point of intersection. Since we do not have an explicit ex-
pression for fh,p or fh,s, the solution is not rigorous. But numerical
experiments over a large parameter ranges have revealed that the so-
lution does hold. The solution assumes that both fh,p and fh,s are
concave functions of ν. For small values of Rhh
0 , we can assert that
the secondary infections would be smaller than primary infections
for all values of ν. Thus ν = 0 would be the only solution. As we
increase Rhh
0 , a bifurcation would occur at ν = 0 and a second so-
lution would emerge. At the bifurcation point, the slope of fh,p and
fh,s would be equal. Thus, the bifurcation condition is
∂fh,p
∂ν

ν=0
= ∂fh,s
∂ν

ν=0
(C18)
Since we don’t have an analytical expression for fh,p, we will work
with equation C17. Assuming Rhh
0
< 1, from equation C11 we get
fh|ν=0 = 0
∂fh
∂ν

ν=0 =
1
1 −Rhh
0
(C19)
Using the above solutions in C12 and C15, we obtain
∂fh,p\s
∂ν

ν=0 = ∂f 0
h,p
∂ν

ν=0 = 1
(C20)
From equation C20 and C17, we obtain.
∂fh,p
∂ν

ν=0 = 1
(C21)
For fh,s,
∂fh,s
∂ν

ν=0 = ∂fh
∂ν

ν=0 −∂fh,p
∂ν

ν=0
=
Rhh
0
1 −Rhh
0
(C22)
Equating C21 and C22, we obtain Rhh
0
= 1/2 is the bifurcation
point where the two slopes are equal. For Rhh
0
< 1/2, the number
of secondary transmissions will always be smaller than primary ones
for ν > 0. For Rhh
0
> 1/2, the two curves will either intersect or
fh,s will be strictly greater than fh,p. We were unable to calculate
analytically the point ν⋆of intersection of the two curves or the point
in parameter space where the point of intersection disappears.
5.
Non-identiﬁability of epidemic driver
We present the argument in the main text that given just the time
series data for a large outbreak it is not possible to identify whether
the epidemic is driven by a large animal outbreak or by human to
human transmission. To make our case, we compare the distribu-
tion of stochastic epidemic proﬁles for the mentioned scenarios in
ﬁgure A10: one where there are only primary infections taking place
and other where there is only human to human transmission. As can
be seen in the plot, the distribution of the infection proﬁle is almost
identical for the chosen sets of parameters. The parameter combina-
tions chosen are not necessarily unique and such non-identiﬁability
can occur by choosing parameters from different parts of the phase
space.
0
50
100
FIG. A10. Box plots for simulated epidemic trajectories for the hu-
man population in each of the following two scenarios: (black) the
epidemic is driven by only A-H transmissions with no H-H trans-
missions (βaa = ˆβah = 1.5, βhh = 0, one infected animal host at
t = 0) ; and (red) the epidemic is driven by only H-H transmis-
sions after initial spillover (βaa = ˆβah = 0, βhh =1.5, one infected
human host at t = 0). The remaining parameters for the simulations:
Na = Nh = 1000, ν = 1, γa = γh = 1.0.


## Page 18


18
6.
Variance of the ﬁnal size
Since our model ﬁts in the formalism of a generalized multi-type
epidemic, we shall borrow notation and results from [15, 16]. We
have 3 host types in our system: animal, type 1 human and type
2 humans which we shall label as 1, 2 and 3 in this section. The
populations for the respective types are
N1 = Na,
N2 = νNh,
N3 = (1 −ν)Nh
Let πi be the fraction of hosts in each type,
π1 =
Na
Na + Nh ,
π2 =
νNh
Na + Nh ,
π3 = (1 −ν)Nh
Na + Nh
and Fi be the fraction of individuals infected in each type in the limit
of large (but ﬁnite) population.
F1 =Fa = Ra(∞)
Na
, F2 = Rh,1(∞)
νNh
,
F3 = Rh,2(∞)
(1−ν)Nh , Fh = Rh(∞)
Nh
and φi be the mean fraction.
φ1 = φa = fa, φ2 = fh,1
ν , φ3 = fh,2
1 −ν , φh = fh
Next we deﬁne Ωmatrix as
Ω=


Raa
0

1 + 1
ρ
 Rah
0
ν
(1 + ρ)
0
0
Rhh
0 (1 + ρ) Rhh
0 (1 + ρ)
0
Rhh
0 (1 + ρ) Rhh
0 (1 + ρ)


A central limit theorem in Ball and Clancy [15] shows that the vec-
tor
p
Nj(Fj −φj), j = 1, 2, 3
	
is asymptotically Gaussian with
mean 0 and variance matrix
Σ = ST −1ΞS−1
where the matrices S and Ξ are given by
Sij = δij −√πiπjΩij(1 −φj)
(C23)
Ξij = φi(1 −φj)δij + √πiπj(1 −φi)(1 −φj)
X
k=1,2,3
πkφkΩkiΩkj
where δij is the Kronecker delta. We have used the fact that for the
exponentially distributed infectious period such as in our case the
mean is equal to the standard deviation. Therefore the term (σk/µk)
which is present in general form of the expression given in [16], does
not appear here. Since the disease process in the animal population
can be treated as a single type epidemic process, the variance can be
written explicitly.
Var(Fa) = fa(1 −fa)

1 + (Raa
0 )2(1 −fa)

Na (1 −Raa
0 (1 −fa))2
(C24)
For the human population,
Fh = νF2 + (1 −ν)F3
The variance of the relative ﬁnal size in the human population can
then be calculated as
Var(Fh) = ν Ξ22 + (1 −ν) Ξ33 + 2
p
ν(1 −ν) Ξ23
Nh
(C25)
The special case of ν = 1 (which eliminates type 2 hosts) yields the
following expression for above
Var(Fh) = fh(1 −fh)

1 + (Rhh
0 )2(1 −fh)

Nh
 1 −Rhh
0 (1 −fh)
2
+
ρ(Rah
0 )2fa(2 −fa)(1 −fh)2
Nh (1 −Raa
0 (1 −fa))2  1 −Rhh
0 (1 −fh)
2
(C26)
[1] Athreya, KB & Ney, PE
(1972) Branching Processes.
(Springer-Verlag Berlin Heidelberg).
[2] Bailey, NTJ (1990) The Elements of Stochastic Processes with
Applications to the Natural Sciences. (Wiley-Interscience).
[3] Lloyd-Smith, JO et al.
(2009) Epidemic dynamics at the
human-animal interface. Science 326, 1362–1367.
[4] Antal, T & Krapivsky, PL (2011) Exact solution of a two-type
branching process: models of tumor progression. J. Stat. Mech.
2011, P08018.
[5] Grifﬁths, DA (1972) A bivariate birth-death process which ap-
proximates to the spread of a disease involving a vector. J. Appl.
Probab. 9, 65–75.
[6] Karlin, S & Tavar´e, S (1982) Linear birth and death processes
with killing. J. Appl. Probab. 19, 477–487.
[7] Keeling, MJ & Rohani, P (2008) Modeling Infectious Diseases
in Humans and Animals. (Princeton Univ. Press).
[8] Newman, MEJ (2002) Spread of epidemic disease on networks.
Phys. Rev. E Stat. Nonlin. Soft Matter Phys. 66, 16128.
[9] Kenah, E & Robins, JM (2007) Second look at the spread of
epidemics on networks. Phys. Rev. E Stat. Nonlin. Soft Matter
Phys. 76, 036113.
[10] Newman, MEJ, Strogatz, SH, & Watts., DJ (2001) Random
graphs with arbitrary degree distributions and their applications.
Phys. Rev. E Stat. Nonlin. Soft Matter Phys. 64, 026118.
[11] Flajolet, P & Sedgewick, R
(2009) Analytic combinatorics.
(Cambridge Univ. Press).
[12] Antal, T & Krapivsky, PL (2012) Outbreak size distributions in
epidemics with multiple stages. J. Stat. Mech. 2012, P07018.
[13] Van den Driessche, FBP, Wu, J, & Allen, LJS (2008) Mathe-
matical Epidemiology. (Springer).
[14] Kenah, E & Robins, JM
(2007) Network-based analysis of
stochastic SIR epidemic models with random and proportion-
ate mixing. J. Theor. Biol. 249, 706.
[15] Ball, F & Clancy, D (1993) The ﬁnal size and severity of a
generalised stochastic multitype epidemic model. Adv. Appl.
Probab. 25, 721–736.
[16] Britton, T (2002) Epidemics in heterogeneous communities:
estimation of R0 and secure vaccination coverage. J. R. Stat.
Soc. Series B Stat. Methodol. 63, 705–715.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
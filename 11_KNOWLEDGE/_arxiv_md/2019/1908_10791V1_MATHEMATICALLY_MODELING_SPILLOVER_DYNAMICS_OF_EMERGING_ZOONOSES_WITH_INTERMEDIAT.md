---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1908.10791v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1908.10791v1_Mathematically_Modeling_Spillover_Dynamics_of_Emerging_Zoonoses_with_Intermediat

> Source: 1908.10791v1_Mathematically_Modeling_Spillover_Dynamics_of_Emerging_Zoonoses_with_Intermediat.pdf

> Pages: 50

---


## Page 1


Mathematically Modeling Spillover Dynamics of Emerging
Zoonoses with Intermediate Hosts
Katherine P. Roycea, Feng Fu∗,a,b
aDepartment of Mathematics, Dartmouth College, Hanover, NH 03755, USA
bDepartment of Biomedical Data Science, Geisel School of Medicine at Dartmouth, Lebanon, NH 03756,
USA
Abstract
The World Health Organization describes zoonotic diseases as a major pandemic threat,
and modeling the behavior of such diseases is a key component of their control. Many
emerging zoonoses, such as SARS, Nipah, and Hendra, mutated from their wild type
while circulating in an intermediate host population, usually a domestic species, to be-
come more transmissible among humans, and moreover, this transmission route will
only become more likely as agriculture and trade intensiﬁes around the world. Passage
through an intermediate host enables many otherwise rare diseases to become better
adapted to humans, and so understanding this process with mathematical epidemio-
logical models is necessary to prevent epidemics of emerging zoonoses, guide policy
interventions in public health, and predict the behavior of an epidemic. In this pa-
per, we account for spillovers of a zoonotic disease mutating in an intermediate host
by means of modeling transmission dynamics within and between three host species,
namely, wild reservoir, intermediate domestic animals, and humans. We calculate the
basic reproductive number of the pathogen, present critical conditions for the emer-
gence dynamics of zoonosis, and perform stability analysis of admissible disease equi-
libria. Our analytical results agree well with long-term simulations of the system. We
ﬁnd that in the presence of biologically realistic interspecies transmission parameters,
a zoonotic disease can establish itself in humans even if it fails to persist in its reservoir
∗Corresponding author at: 6188 Kemeny Hall, 27 N. Main Street, Hanover, NH 03755, USA. Fax: +1
(603) 646 1312
Email addresses: Katherine.P.Royce.19@dartmouth.edu (Katherine P. Royce),
feng.fu@dartmouth.edu (Feng Fu)
Preprint submitted to Journal of Theoretical Biology
August 29, 2019
arXiv:1908.10791v1  [q-bio.PE]  28 Aug 2019


## Page 2


and intermediate host species. Our model and results can be used to understand the
dynamic behavior of any zoonosis with intermediate hosts and assist efforts to protect
public health.
Key words: Zoonosis, Evolutionary Epidemiology, Pathogen Adaptation, Global
Health, Mathematical Biology
1. Introduction
Zoonotic diseases, which originate in animals and infect humans, are one of the
most concerning epidemic threats of the 21st century and form 60% of all known infec-
tious diseases (Karesh et al., 2012). These pathogens cause a billion cases of illness per
year, inﬂict severe economic damage, and pose an increasing threat in a more connected
world; indeed, endemic zoonoses are currently the greatest global burden on human
health (Karesh et al., 2012). Public health threats such as HIV-AIDS, avian inﬂuenza,
SARS, Ebola, Nipah, Hendra, and rabies all trace their origin to nonhuman reservoir
species, and it is likely that the next global pandemic will be a zoonosis (Karesh et al.,
2012). Zoonoses have comprised a growing area of public health research for the last
two decades (Daszak et al., 2000), and the World Health Organization even cites “Dis-
ease X”, a pathogen currently unknown to cause human disease that might evolve to
become more transmissible among humans, as a priority for research and development
in pandemic prevention (WHO, 2018).
The frequency of new pathogens emerging into the human population−rapidly in-
creasing in incidence or geographic range to become a threat to public health−is in-
creasing (Morse et al., 2012), and zoonoses comprise 75% of emerging infectious dis-
eases (Woolhouse and Gowtage-Sequeria, 2005). Emergence of zoonoses is linked to
human behavioral changes and increasing rates of interaction with wildlife, human
travel, and global trade (Cunningham et al., 2017), as well as accelerating climate
change ((Cunningham et al., 2017), (Lloyd-Smith et al., 2015), (Wolfe et al., 2005)).
The dynamics of a zoonosis in its reservoir host are frequently cited as an inﬂuence
on its emergence in humans (Karesh et al., 2012), but to our knowledge, no attempt
has been made to quantify the entire course of an emerging zoonosis, from its origins
2


## Page 3


in a wild reservoir host to an epidemic in humans. Indeed, Lloyd-Smith et al. (2009)
blames a desire to view zoonoses in a piecewise manner, as a concatenation of different
epidemics rather than a connected system, for the lack of quantitative understanding of
zoonoses as a new type of disease. Some of the most pressing unaddressed questions
in establishing the mathematical theory of zoonoses include better capturing disease
dynamics within nonhuman species in order to characterize changes in the disease be-
fore it infects humans; focusing on the ﬁrst cases of human infection to understand
how a pathogen actively adapts to humans; and developing a theory for the role of in-
termediate hosts in the emergence of the disease (Lloyd-Smith et al., 2015). Despite
these recognized challenges and the frequent use of mathematical biology to assist with
risk assessment and surveillance strategies for other types of diseases, there is no uni-
fying mathematical theory or set of principles that can be used to frame discussions
of zoonotic spillovers (Lloyd-Smith et al., 2015). This gap in modeling spillover dy-
namics limits our understanding of zoonoses, as does a general lack of mathematical
modeling of multihost pathogens and quantiﬁcation of the rate of human-to-human
transmission ((Lloyd-Smith et al., 2009), (Allen et al., 2012)). This paper provides
such a mathematical model for a zoonosis emerging through an intermediate host.
Zoonotic diseases are currently classiﬁed on the basis of their human-to-human
transmissibility (Lloyd-Smith et al., 2009), which is assumed to be a critical distinc-
tion between pathogens with pandemic potential and pathogens that remain relatively
rare ((Karesh et al., 2012), (Woolhouse and Gowtage-Sequeria, 2005), (Lloyd-Smith
et al., 2015)). The major distinction in zoonotic spread within humans is whether the
pathogen can spread beyond its primary individual host to infect other humans: whether
the basic reproduction number R0, the number of secondary cases produced by an in-
dex case in an entirely naive population, is greater than 1 (Lloyd-Smith et al., 2015).
This classiﬁcation rests on a three-stage framework summarized by Morse et al. (2012),
Lloyd-Smith et al. (2009), and Wolfe et al. (2005). Stage 1, pre-emergence, represents
zoonoses circulating in an intermediate host but only capable of spillover into a dead-
end human host, with no further transmission. Stage 2, localized emergence, deﬁnes
diseases that can maintain stuttering chains in a human population with reinfection
from animal hosts but are incapable of sustaining themselves in humans alone. Stage
3


## Page 4


3, pandemic emergence, classiﬁes diseases that are fully adapted to humans and thus
capable of causing outbreaks in our species alone ((Morse et al., 2012), (Lloyd-Smith
et al., 2009)). In this paper, we examine the process of pathogen evolution through
these different stages to show that with a mutation to a human-transmissible strain in
an intermediate host, a pathogen can maintain an endemic equilibrium in humans even
in stage 1, suggesting that the epidemiological stratiﬁcation of zoonotic diseases based
on their perceived threat to humans may be myopic.
1.1. The Role of Intermediate Hosts for a Zoonosis
In contrast to pathogens which evolved to infect humans, such as smallpox, the
biology of emerging zoonoses is adapted to a different host species, called the reser-
voir host. Zoonoses are the product of a pathogen exploiting a new niche, sometimes
one exposed by anthropogenic changes or induced by the ampliﬁcation of its trans-
mission (Karesh et al., 2012). Zoonotic pandemics occur when the pathogen gains
the ability to circulate in a human population, rather than infrequently causing infec-
tion in an individual dead-end host (Richard et al., 2014), a change which usually
requires one or more mutations from the wild type (Lloyd-Smith et al., 2015). While
the change to a pathogen’s R0 in humans can take place over a single individual in-
fection, this modiﬁcation is considered to be a result of the role that different animal
hosts play in amplifying or transmitting a zoonosis to humans (Karesh et al., 2012).
Since a pathogen’s transmissibility can also be affected by anthropogenic factors such
as the host species’ population structure or resource and habitat availability (Allen
et al., 2012), intermediate hosts−a non-reservoir animal species in which a zoonotic
pathogen circulates−particularly domestic animals, provide greater opportunity for a
pathogen to mutate to a human-transmissible form, because these species are biolog-
ically similar to the pathogen’s wild reservoir and have greater contact with humans.
It is therefore extremely important to develop a theory for a human-transmissible dis-
ease arising from a zoonotic pathogen in an intermediate host population; with such
a framework, policymakers can move towards prevention of a human pandemic rather
than amelioration of one (Lloyd-Smith et al., 2015).
As an example of the role of intermediate hosts, the adaptation of avian inﬂuenza,
4


## Page 5


one of the most well-studied zoonoses, to humans requires a mutation in domestic pigs
or poultry. Avian inﬂuenza’s success in a new host species is governed by its receptor
binding speciﬁcity (Richard et al., 2014); with circulation in domestic pigs, which ex-
press both human- and avian-inﬂuenza type receptors in their tracheae, the virus has an
opportunity to mutate to a form that can infect humans ((Neumann et al., 2009), (Ma
et al., 2009)). Further, as domestic animals, swine have more contact with humans than
wild birds do and can thus spread a disease more quickly (Ma et al., 2009). Domestic
poultry can play a similar role for the disease, since circulation in a domestic poultry
population may increase the pathogenicity of avian inﬂuenza among birds ((Vandegrift
et al., 2010), (Ito et al., 2001)). As a result, human movement of livestock, not avian
migration, is the dominant factor in the spread of highly pathogenic avian inﬂuenza,
even though wild birds are the reservoir of the disease (Gauthier-Clerc et al., 2007).
The inﬂuenzas are perhaps the easiest example to understand, as reassortment of dif-
ferent hemagglutinin and neuraminidase subtypes within one infected pig can produce
entirely new pathogens (Neumann et al., 2009), but less drastic mutations can alter the
transmissibility or lethality of any zoonosis. Pigs are an intermediate host for Nipah
virus (Sharma et al., 2019), and the intensiﬁcation of the pig industry in Malaysia was
identiﬁed as the key factor in the spillover of the disease to humans in the 1990s (Cun-
ningham et al., 2017). In this case, the disease dynamics that resulted from repeated
introductions from bats, the pathogen’s reservoir host, to pigs enabled Nipah to persist
in its intermediate host and thus infect humans (Pulliam et al., 2011). These examples
support the general principle that the domestication of animals is linked to an increased
risk of emergence of zoonotic diseases into the human population (Karesh et al., 2012),
and Table 1, a sampling of zoonoses for which an intermediate host has been identiﬁed,
shows the prevalence of domesticated species as intermediate hosts.
1.2. The Role of Mathematical Modeling
Ordinary differential equations describing population dynamics and zoonotic trans-
mission are a crucial tool in understanding the nonlinear interactions that are a hallmark
of zoonotic diseases, a type of subgroup dynamics which can lead to counterintuitive
behaviors ((Lloyd-Smith et al., 2009), (Allen et al., 2012)). Mathematical models can
5


## Page 6


enable experiments that would be unfeasible with real populations, predict future trends
based on current data, and estimate key epidemic qualities such as the basic reproduc-
tion number of a pathogen in a speciﬁc population (Lloyd-Smith et al., 2009). Ex-
plicitly quantifying the dynamics behind this adaptive transformation is thus critical to
public health efforts; however, no previous models examine the changes an emerging
zoonosis undergoes as it spreads between different species (Lloyd-Smith et al., 2015).
There have been attempts to quantify the effect of pathogen mutations in humans
alone. Models for tuberculosis sometimes include a distinction between latent and
active forms of the disease (Gumel, 2012). Iwami et al. (2007) recognizes that the
ability of avian inﬂuenza to mutate during an epidemic is a crucial determinant of
its pandemic potential, but conceptualizes this mutation as occuring within humans
rather than another species, ignoring the intrinsically zoonotic behavior of the disease.
Gumel (2009) expands on this analysis by including a compartment for wild birds, but
still locates the mutation after the pathogen’s spillover to humans. This framework
occludes the key population in the spread of a zoonosis: Richard et al. (2014) cites
two barriers, jumping to humans and efﬁcient human-to-human transmission, that a
zoonotic pathogen must overcome, and this change frequently occurs in the “mixing
vessel” of an intermediate host species (Neumann et al., 2009). Further, controlling a
human epidemic of a zoonotic disease depends on controlling the basic reproduction
number in both animals and humans (Kim et al., 2010), interventions not previously
studied together.
In this paper, we present a model which incorporates a pathogen mutation to a
human-transmissible form in an intermediate host species, ﬁlling the gap noted by
Lloyd-Smith et al. (2015) with the introduction of a mathematical model that simulates
the entire course of an emerging zoonosis. We investigate whether the presence of
pathogen adaptation in intermediate hosts can amplify an epidemic among humans,
with the goal of informing public health efforts to curb emerging infectious diseases.
The model presented here is based on the basic SIR model ﬁrst presented by Ker-
mack and McKendrick (1927), as well as the introduction to multihost SIR models pre-
sented by Allen et al. (2012). As a baseline and example, we use parameters that most
closely reﬂect highly pathenogenic avian inﬂuenza, a classical example of a zoonosis
6


## Page 7


with an intermediate host (Daszak et al., 2000) and one for which the most data is
available. Further, although we model a traditional epidemic in the wild reservoir host,
the model retains the capacity to implement seasonal variation or a constant force of
infection in that species by changing the equations describing the wild compartment.
However, our model is intended to codify the idea of an intermediate host mathemat-
ically and therefore does not focus on a particular infectious disease. By changing its
parameters, this model can be applied to study any zoonosis that passes through an
intermediate host population, and its results are general to that theory.
1.3. Outline
This paper investigates two questions: how to model adaptation of a zoonotic
pathogen to a human-transmissible form in an intermediate host population and what
effects these interspecies dynamics have on the epidemic in humans. Section 2 intro-
duces the model; Section 3 analyzes its mathematical qualities, including its equilibria
and R0; Section 4 provides numerical simulations; and Section 5 suggests directions
for future research. We ﬁnd that completely accounting for the spillover and interpop-
ulation dynamics exhibited by emerging zoonoses links human populations to animal
ones more deeply than previously thought. With nonzero contact rates between species
and a nonzero mutation rate in an intermediate host, a zoonotic pathogen can establish
itself in humans even if it fails to take hold in animal hosts or achieve an R0 > 1 in
the human compartment, refuting the transmissibility framework ((Morse et al., 2012),
(Wolfe et al., 2005), and (Lloyd-Smith et al., 2009)) that currently forms the basis for
classiﬁcation of emerging zoonoses. This paper introduces a theory of spillover through
an intermediate host species that can be modiﬁed to study any zoonosis that exhibits
this behavior, and sounds an alarm for researchers and policymakers by showing that
zoonotic epidemics can persist in human populations under less stringent conditions
than previously assumed.
2. The Model
The traditional susceptible, infected, recovered (SIR) model originally developed
by Kermack and McKendrick ((Kermack and McKendrick, 1927), (Kermack and McK-
7


## Page 8


endrick, 1932), (Kermack and McKendrick, 1933)), shown below, accurately repro-
duces the standard epidemic curves for an infectious disease, and forms the basis for
many different epidemiological models.
dS
dt = −βSI,
dI
dt = βSI −γI,
dR
dt = γI.
Here S, I, and R stand for the proportion of individuals that are susceptible, in-
fected, and recovered, respectively.
This deterministic framework depends on the
transmission rate β and the recovery rate γ, parameters speciﬁc to the disease. This,
the simplest version, considers one disease that confers lifelong immunity spreading
within a closed, constant population of one species. There are no equilibria other than
the disease-free state, as there is no external force of infection or inﬂux of susceptible
individuals. The basic reproductive number R0 for this simple SIR model is
R0 = β/γ.
To model a disease over a longer time frame, vital dynamics modeling birth (b) and
mortality (m) rates are introduced:
dS/dt = b −βSI −mS,
dI/dt = βSI −γI −mI,
dR/dt = γI −mR.
This framework has a force b constantly introducing new susceptible individuals,
and the basic reproductive number for this model is
R0 =
bβ
m(m + γ).
The disease-free equilibrium is
(S∗, I∗, R∗) = ( b
m, 0, 0),
8


## Page 9


and the endemic equilibrium is
(S∗, I∗, R∗) = (m + γ
β
, m
β (R0 −1), γ
β (R0 −1)).
To our knowledge, the main class of SIR models that include two or more species
are those that consider vector-borne illnesses.
However, since a vector-borne dis-
ease must infect both its host species (rather than opportunistically jumping to a new
species) and follows set steps in its life cycle in both (rather than unpredictably mu-
tating in a new host), a vector-borne SIR model merely adds more compartments for
the pathogen to run through. Unlike vector-borne diseases such as malaria (see Flo-
rens et al. (2002) and Chang et al. (2013)), an emerging zoonosis does not need to
infect another species as part of its life cycle. Instead, it opportunistically infects an-
imals similar enough to its reservoir host, and−in the pattern of transmission consid-
ered here−mutates to a human-to-human transmissible form only if given the oppor-
tunity. Dengue, which spreads between mosquitoes and humans, is another exam-
ple of a vector-borne disease, and its analysis draws useful parallels with the type of
pathogen behavior modeled here. Andraud et al. (2012), a review paper of determin-
istic models of dengue, notes that the disease dynamics among the vector population
are frequently simpliﬁed to a mere force of infection for the human one, since the dis-
ease does not evolve within the vector species. In contrast, a zoonosis model must
consider the disease dynamics in its nonhuman compartments, since these dynamics
determine whether the pathogen reaches humans at all. Attempts have been made to
model zoonotic spillovers (Lloyd-Smith et al. (2009), Allen et al. (2012), Hussaini et al.
(2017)), but without incorporating changes in the pathogen’s ecology over the course of
an epidemic, these models are mathematically indistinguishable from those modeling a
vector-borne disease with more hosts or a multispecies model. While a sizeable litera-
ture exists on mathematical models of vectorborne diseases, and this class of pathogen
provides a useful comparison for the type of behavior modeled here, no model captures
the unintentional opportunism of zoonoses or incorporates selective pressure on viruses
(Allen et al., 2012).
To model this behavior, we create three compartments, representing the pathogen’s
wild reservoir host, an intermediate host assumed to be a domestic animal, and hu-
9


## Page 10


mans. The wild, domestic and human populations are each modeled by a SIR system
with vital dynamics and linked by transmission routes. An infected wild host can pass
the disease to a susceptible domestic animal at a transmission rate pd, and an infected
domestic animal can pass the human-transmissible strain of the disease to a human at
a rate ph. Finally, the model incorporates the hallmark of an emerging zoonosis: the
pathogen’s ability to mutate to a human-transmissible strain while circulating in a do-
mestic host. To model this phenomenon, we introduce a category T (transmissible) for
domestic animals in which the zoonosis has mutated to a human-transmissible form.
This mutation happens at a rate µ in infected domestic animals, who then transition
from the original infected category to the transmissible one and can infect other sus-
ceptible domestic animals with the new, human-transmissible strain. The full system
of 10 ordinary differential equations is shown in Table 2, with subscripts indicating
the species (wild, domestic, or human) to which the compartment belongs. Figure 1
provides a representation of the connections between populations, and Table 3 gives
the deﬁnition of each variable.
2.1. Model Assumptions
We make several assumptions to clarify the essential dynamics of the system.
Firstly, we equate the domestic animal recovery and transmission rates for both strains
of the pathogen; the human-transmissible strain is different from the wild one only in
that its transmission rate in humans is nonzero. We further assume that the population
of each compartment is constant over the course of the simulation, with each species’
vital dynamics set at replacement rates, and thus calculate the proportion of susceptible,
infected, and recovered animals in each species rather than the raw numbers present in
each category. To maintain a focus on population biology and the potential for the
spread of disease from infected individuals, we do not consider disease-induced mor-
tality. Finally, only domestic animals infected with the T strain can pass the disease
to humans, although both strains circulate in the domestic population. The model does
not account for coinfection in a domestic animal, since an individual infected with
both strains is still capable of starting a human epidemic and is thus counted in the T
category.
10


## Page 11


Figure 1: A representation of the model. Model parameters are summarized in Table 3.
We intend this model to provide a general framework that can be modiﬁed to ﬁt any
zoonosis with an intermediate host, and provide the analysis in Section 3 with the goal
of starting such a theory. However, to provide a baseline for the numerical simulations
in Section 4, we use parameters corresponding to highly pathenogenic avian inﬂuenza.
Table 4 provides the baseline values and the sources used in our examples.
Reﬂecting the lack of data for zoonoses over their entire range of species, the
sources used for these parameters reﬂect different strains of avian inﬂuenza. Bett et al.
(2014) calculates the transmission rate of H5N1 in Nigeria, while Xiao et al. (2014)
cites information about H7N9 in China. The values are also attained using different
data-gathering practices: Singh et al. (2018) surveyed experts in Australian avian in-
ﬂuenza for their assessment of the probability of domestic poultry becoming infected
with low pathogenic avian inﬂuenza from wild birds, as well as that strain mutating to
11


## Page 12


higly pathenogic avian inﬂuenza (HPAI) on a farm, while Henaux et al. (2010) provides
a review of some HPAI parameters. As stated in Table 4, we could not ﬁnd a source for
transmission parameters among wild birds, and thus assume the disease parameters in
that species to be equivalent to those in domestic poultry. The variety and inconsistency
of these sources reﬂects the need for more data and research into the actual effects of
particular zoonoses. Although it is crucial for public health interventions based on a
mathematical model to know the accuracy of each parameter, their speciﬁc values are
relatively unimportant for the theoretical results presented here, as the global analysis
of the system holds for all parameter values, and are accordingly not the focus of this
work.
2.2. Methods
To obtain the equilibria for the system, we set each of the 10 equations of Ta-
ble 2 to 0 and solve for the population variables. We further analyze the stability of
each equilibrium using the system’s Jacobian about the point and establish the impor-
tance of the model’s basic reproduction number as a threshold condition. The methods
we use to analyze the model’s R0 are based on the next-generation matrix technique
given by Diekmann et al. (2009) and Van den Driessche and Watmough (2002). This
method deﬁnes R0 in a compartmental model, where it has been proven to remain a
threshold condition for the stability of equilibria (Van den Driessche and Watmough,
2002). This approach is similar to that used to model the spread of avian inﬂuenza
in farm and market populations of domestic poultry (Li et al., 2018); to analyze the
effect of different growth laws in the avian population on the spread of avian inﬂuenza
(Liu et al., 2017); to give a model of a vector-host system for leishmaniasis (Hus-
saini et al., 2017); to analyze SEIR models (Khan et al., 2018); and to analyze models
with vaccination (Anguelov et al., 2014). Our work thus uses established mathematical
epidemiology techniques to analyze a new model of infectious disease dynamics, ex-
tending the preexisting SIR framework to study the spillover effect of a zoonosis with
an intermediate host. The model’s key innovations are linking three species together
based on their proximity to humans and distinguishing between human-transmissible
and non-human-transmissible strains of the pathogen, as no previous models simulate
12


## Page 13


either intermediate hosts for zoonoses or a mutation to a human-transmissible form
during the course of the epidemic in animals to study the entire range of an emerging
infectious zoonosis.
3. Analysis
In this section, we analyze the mathematical qualities of the model, proving that a
unique endemic equilibrium exists by analyzing each species compartment. We further
show that the stability of each equilibrium depends on the system’s R0 and distinguish
between the importance of intraspecies parameters−the transmission (β) and recovery
(γ) rates of a species, as well as its birth and mortality rate (b, m)−and interspecies
parameters governing connections between species −the contact rates pd and ph, as
well as the rate of mutation µ to a human-transmissible form. We show that, if there
is a nonzero number of infected wild animals, only the second type of parameters can
alter the global stability of the system.
3.1. The Wild Compartment
The equilibrium states (S∗
w, I∗
w, R∗
w) in the wild compartment satisfy the following
equations:
bw −βwS∗
wI∗
w −mwS∗
w
= 0,
(1)
βwS∗
wI∗
w −γwI∗
w −mwI∗
w
= 0,
(2)
γwI∗
w −mwR∗
w
= 0.
(3)
By summing (1), (2), and (3), we obtain the total abundance of wild animals in equi-
librium, bw/mw.
Theorem 1. There is one disease-free equilibrium, Ew
f , at
(S∗
w, I∗
w, R∗
w) =
 bw
mw
, 0, 0

,
and a unique endemic equilibrium, Ew
e , at
(S∗
w, I∗
w, R∗
w) =
mw + γw
βw
, bw −mwS∗
w
βwS∗w
, γwI∗
w
mw

13


## Page 14


Proof. Factoring equation (2) yields
I∗
w(βwS∗
w −γw −mw) = 0,
which holds either if I∗
w = 0 (case 1) or if βwS∗
w −γw −mw = 0 (case 2).
In the ﬁrst case, we obtain the disease-free equilibrium by substituting I∗
w = 0 into
equations (1) and (3), producing equilibrium values of S∗
w =
bw
mw and R∗
w = 0.
The second case holds if Sw = γw+mw
βw
. Substituting this value into equation (1),
we obtain I∗
w =
bw−mwS∗
w
βwS∗
w
. Solving equation (3) for Rw gives R∗
w −γwI∗
w
mw . Since
I∗
w > 0, this case produces an endemic equilibrium.
It is a basic epidemiological result that a simple SIR model with vital dynamics,
such as the system that models the wild compartment here, has Rw
0 =
bwβw
mw(γw+mw).
We prove the threshold value of Rw
0 in the wild compartment by using its Jacobian,
Jw =


−βwIw −mw
−βwSw
0
βwIw
βwSw −γw −mw
0
0
γw
−mw


Theorem 2. Ew
f is stable if R0 < 1 and Ef
e is stable if R0 > 1.
Proof. In the ﬁrst case, let Rw
0 < 1. We calculate that
Jw(Ew
f ) =


−mw
−bwβw
mw
0
0
bwβw
mw −γw −mw
0
0
γw
−mw


has eigenvalues −mw and bwβw
mw −γw −mw. Since mw > 0 by assumption and
bwβw
mw
< mw + γw by the restriction on R0, both eigenvalues are negative and so Ew
f
is stable when Rw
0 < 1.
In the second, let Rw
0 > 1. We have that
Jw(Ew
e ) =


−
bwβw
γw+mw
−γw −mw
0
bwβw
γw+mw −mw
0
0
0
γw
−mw


14


## Page 15


with eigenvalues −
bwβw
γw+mw , 0, −mw. Since all parameters are positive, these eigen-
values are all negative and thus Ew
e is stable.
We have thus shown that one disease-free equilibrium and one endemic equilibrium
exist among wild reservoir hosts, conﬁrming the importance of Iw > 0 as a threshold
condition for the spread of the disease.
3.2. The Domestic Compartment
In a similar manner, we can analyze the domestic compartment distinctly from the
other two species, since interspecies interactions are limited to the force of infection
pdSdIw attributed to the wild compartment. Any equilibrium (S∗
d, I∗
d, T ∗
d , R∗
d) in this
compartment must satisfy the system
bd −βdS∗
dI∗
d −pdS∗
dI∗
w −βdS∗
dT ∗
d −mdS∗
d
= 0,
(4)
βdS∗
dI∗
d + pdS∗
dI∗
w −µI∗
d −γdI∗
d −mdI∗
d
= 0,
(5)
µI∗
d + βdS∗
dT ∗
d −γdT ∗
d −mdT ∗
d
= 0,
(6)
γdI∗
d + γdT ∗
d −mdR∗
d
= 0.
(7)
Note that by summing equations (4)-(7), we obtain the abundance of the domestic
compartment at equilibrium, bd/md. Since this compartment is subject to an external
force of infection from the wild compartment, we also note that the existence of a
disease-free equilibrium depends on this external inﬂuence.
Lemma 1. A disease-free equilibrium, Ed
f, in the domestic compartment,
(S∗
d, I∗
d, T ∗
d , R∗
d) =
 bd
md
, 0, 0, 0

,
is only possible if Iw = 0 or pd = 0.
Proof. Let Iw > 0 for some value of t and pd ̸= 0, and assume that a disease-free
equilibrium exists with I∗
d = 0. We note that a disease-free equilibrium requires a
nonzero proportion of susceptible individuals, so S∗
d > 0 as well. Substituting these
values into equation (5), we obtain pdS∗
dI∗
w = 0, a contradiction with our assumptions.
Therefore I∗
d ̸= 0. Substituting this value into equation (6), we also obtain T ∗
d ̸=
15


## Page 16


0. However, these condition imply that there are infected individuals of both types
in the domestic animal population, a contradiction with our assumption that we are
analyzing a disease-free equilibrium. By contradiction, any disease-free equilibrium
in the domestic compartment must have either Iw = 0 or pd = 0 in the complete
system.
Note that this result is deeper than one about the equilibrium state of Iw: if Iw > 0
at any time over the course of the epidemic, even if the disease later vanishes from the
wild population, the pathogen will spread to the domestic species.
Assuming that there is a force of infection from the wild reservoir hosts, we analyze
the possible endemic equilibrium values and show that there is a unique possibility in
this compartment as well.
Theorem 3. There is only one admissible endemic equilibrium Ed
e in the domes-
tic compartment. At this equilibrium, we have S∗
d < min{bd/(md + pdI∗
w), (γd +
md)/βd}.
Proof. Adding equations (4)-(6), we obtain
bd −mdS∗
d −(γd + md)I∗
d −(γd + md)T ∗
d = 0.
(⋆1)
Further, from equation (6), we isolate
I∗
d = 1
µ(γd + md −βdS∗
d)T ∗
d .
(⋆2)
Substituting ⋆2 into ⋆1, we get
T ∗
d =
bd −mdS∗
d
(γd + md) + 1
µ(γd + md)(γd + md −βdS∗
d).
(⋆3)
Since the quantities I∗
d and T ∗
d are both nonnegative, it follows immediately that
the equilibrium value S∗
d must have a natural upper bound:
S∗
d ≤γd + md
βd
≤bd
md
.
(8)
Hence we can conﬁrm the denominator in (⋆3) is strictly positive.
16


## Page 17


We also note that from (7), we have R∗
d = γd(I∗
d+T ∗
d )
md
. We thus calculate the equi-
librium values S∗
d by substituting ⋆2, ⋆3 into (4) and obtain, after rearranging:
bd −pdS∗
dI∗
w −mdS∗
d = βdS∗
d(I∗
d + T ∗
d ) = βdS∗
d(1 + 1
µ(γd + md −βdS∗
d))T ∗
d
=
βdS∗
d(1 + 1
µ(γd + md −βdS∗
d))(bd −mdS∗
d)
(γd + md) + 1
µ(γd + md)(γd + md −βdS∗
d)
= βdS∗
d(bd −mdS∗
d)
(γd + md)
.
(9)
We note that in the last step of the derivations above we cancel out the common
factor 1 + 1
µ(γd + md −βdS∗
d) > 0, which is guaranteed by the inequality (8). It is
easy to observe that there exist at most two possible equilibrium values of S∗
d as the
roots of the quadratic equation (9), denoted by S∗
d(1) < S∗
d(2), a consequence of our
assumption that the transmission and recovery rates of both strains in domestic animals
are equal.
We now proceed to prove only the smaller root S∗
d(1) is admissible for the long-term
disease dynamics should there be nonzero disease burden (i.e., I∗
d > 0 and T ∗
d > 0) in
the domestic compartment. In fact, we can view S∗
d as the ﬁxed point(s) satisfying
f(x) = g(x),
where f(x) is a simple linear function, given by
f(x) = bd −(pdI∗
w + md)x,
and g(x) is a quadratic function, given by
g(x) = βdx(bd −mdx)
(γd + md)
.
We can show that f(0) = bd > 0 = g(0), f(bd/(md + pdI∗
w)) = 0 < g(bd/(md +
pdI∗
w)), and 0 > f(x) > g(x) for sufﬁciently large x. Furthermore, as both f and g
are smooth continuous functions, according to the intermediate value theorem, there
must exist two ﬁxed points satisfying f(x) = g(x), S∗
d(1) ∈(0, bd/(md + pdI∗
w)) and
S∗
d(2) ∈(bd/(md + pdI∗
w), ∞) (as also illustrated in Figure 2).
We have bd −pdS∗
dI∗
w −mdS∗
d = βdS∗
d(I∗
d + T ∗
d ) > 0, for nonzero disease burden
I∗
d > 0, T ∗
d > 0. Hence we must have S∗
d < bd/(md + pdI∗
w). So we complete our
17


## Page 18


0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
2
Proportion S d
-5
-4
-3
-2
-1
0
1
f, g
f
g
Sd1
Sd1
Figure 2: The graphs of f(S∗
d) and g(S∗
d); the x-coordinates of their intersection points give the proportion
of domestic animals infected at the equilibria.
proof that only the smaller root S∗
d(1) is admissible as the unique endemic equilibrium
in the domestic compartment.
In line with our proof above, it is easy to directly check the discriminant of the
quadratic equation in (9) is positive:
∆= [βdbd + (γd + md)(pdI∗
w + md)]2 −4βdmdbd(γd + md) > 0.
Then we obtain the endemic equilibrium for S∗
d = S∗
d(1):
S∗
d(1) = βdmd + (γd + md)(pdI∗
w + md) −
√
∆
2βdmd
.
We have thus shown that, in the domestic compartment, there is one unique en-
18


## Page 19


demic equilibrium Ed
e = (S∗
d, I∗
d, T ∗
d , R∗
d), where
S∗
d = S∗
d(1),
T ∗
d =
bd −mdS∗
d
(γd + md) + 1
µ(γd + md)(γd + md −βdS∗
d),
I∗
d = 1
µ(γd + md −βdS∗
d)T ∗
d ,
R∗
d = γd(I∗
d + T ∗
d )
md
.
Further, as we prove above, this equilibrium must be admissible in the presence of
a nonzero force of infection at any time from the wild host population (pdI∗
w > 0).
3.3. The Human Compartment
To complete our understanding of the different species involved in the model, we
analyze the system of equilibrium equations in the human compartment as follows,
bh −βhShIh −phShTd −mhSh
=
0,
(10)
βhShIh + phShTd −γhIh −mhIh
=
0,
(11)
γhIh −mhRh
=
0.
(12)
Adding (10) - (12) gives a total abundance of
bh
mh in the human compartment at equi-
librium. We begin our analysis of this compartment by noting an identical result from
the domestic one: a disease-free equilibrium can exist in the human compartment only
if the force of infection from domestic animals is zero.
Lemma 2. A disease-free equilibrium Eh
f in the human compartment, (S∗
h, I∗
h, R∗
h) =
( bh
mh , 0, 0), is only possible if Td = 0 or ph = 0.
Proof. In a manner similar to the proof of Lemma 1, let Td > 0 at any time over the
course of the model and ph ̸= 0, and assume that a disease-free equilibrium exists with
I∗
h = 0. By equation (9), we obtain phS∗
hT ∗
d = 0, a contradiction with our assumptions
and with the fact that S∗
h ̸= 0 at a disease-free equilibrium. By contradiction, any
disease-free equilibrium must have either Td = 0 or ph = 0.
19


## Page 20


Thus, in the presence of any force of infection phTd from domestic animals, there
must be an endemic equilibrium in the human compartment. We note again that if
Td > 0 at any time over the course of the epidemic, even if that population of animals
vanishes at equilibrium, it is enough to seed the infection into the human compartment.
Theorem 4. There exists only one admissible endemic equilibrium in the human com-
partment Ee
h = (S∗
h, I∗
h, R∗
h), where S∗
h is given by the smaller root of the quadratic
equation:
bh −phS∗
hT ∗
d −mhS∗
h = βhS∗
h(bh −mhS∗
h)/(γh + mh).
Proof. From equation (12), we know
R∗
h = γhI∗
h
mh
.
By adding equations (10) and (11), we obtain
bh −mhS∗
h −(γh + mh)I∗
h = 0.
Accordingly, I∗
h = bh−mhS∗
h
γh+mh . Substituting I∗
h into (10), we obtain
bh −phS∗
hT ∗
d −mhS∗
h = βhS∗
h(bh −mhS∗
h)
γh + mh
.
(13)
Deﬁning the left-hand side as f(S∗
h) = bh −phS∗
hT ∗
d −mhS∗
h and the right-hand side
as g(S∗
h) = βhS∗
h(bh−mhS∗
h)
γh+mh
, as in the proof of Theorem 3, any endemic equilibrium in
the human compartment must satisfy the ﬁxed point(s) f(S∗
h) = g(S∗
h) (see Figure 3).
f is a negatively-sloped line with its root at f1 =
bh
phT ∗
d +mh . g is a concave parabola
with roots at g1 = 0 and g2 =
bh
dh . We thus have g1 < f1 < g2, so there are two
intersection points S∗
h(1) < f1 and S∗
h(2) > g2 (by the intermediate value theorem).
However, g2 is the total compartment size in the human compartment; Sh(2) is thus
biologically impossible.
Solving the quadratic equation (13) directly and taking its smaller root, we obtain
the only viable endemic equilibrium:
S∗
h(1) = βhbh + (mh + γh)(phT ∗
d + md) −
p
[βhbh + (mh + γh)(phT ∗
d + md)]2 −4βhmhbh(γh + mh)
2βhmh
.
20


## Page 21


0
0.5
1
1.5
2
2.5
3
Proportion S h
-0.12
-0.1
-0.08
-0.06
-0.04
-0.02
0
0.02
f, g
f
g
Sh1
Sh2
Figure 3: The graphs of f(S∗
h) and g(S∗
h); the x-coordinates of their intersection points give the proportion
of humans infected at the equilibria.
21


## Page 22


We have thus shown that in the presence of a force of infection from domestic
animals, there is an admissible endemic equilibrium in the human compartment at
Ee
h = (S∗
h, I∗
h, R∗
h), where
S∗
h = S∗
h(1),
I∗
h = bh −mhS∗
h
γh + mh
.
R∗
h = γhI∗
h
mh
.
3.4. System Stability and Basic Reproduction Number
As shown in the previous sections, the endemic equilibria in each compartment are
unique; under the assumption that there is a nonzero force of infection between species
compartments and in the presence of circulating disease in the wild reservoir, we use
the results of Theorems 1, 3, and 4 to obtain an endemic equilibrium at
Ee = (S∗
w, I∗
w, R∗
w, S∗
d, I∗
d, T ∗
d , R∗
d, S∗
h, I∗
h, R∗
h).
The formula of these expressions can be found in detail above.
More precisely, the existence of such stable endemic disease equilibiria requires an
exact condition, that is, the basic reproductive number of the entire system R0 > 1.
Otherwise, there can exist a stable disease-free equilibria. We use next-generation
approach as detailed in Diekmann et al. (2009) and Van den Driessche and Watmough
(2002) to calculate R0 for the system.
The system’s R0 is the spectral radius of FV −1, where F describes the rate of
appearance of new infections in each compartment of host individuals,
F =


βwSw
0
0
0
pdSd
βdSd
0
0
0
0
βdSd
0
0
0
phSh
βhSh


,
and V describes the rate of transfer of individuals out of each compartment,
22


## Page 23


V =


γw + mw
0
0
0
0
µ + γd + md
0
0
0
−µ
γd + md
0
0
0
0
γh + mh


.
We thus get
FV −1 =


βwSw
mw(γw+mw)
0
0
0
pdSd
γw+mw
βdSd
µ+γd+md
0
0
0
µβdSd
(γd+md)(µ+γd+md)
βdSd
γd+md
0
0
µphSh
(γd+md)(µ+γd+md)
phSh
γd+md
βhSh
γh+mh


.
R0 is then the maximum of the eigenvalues of this matrix,
R0 = max{
βwSw
γw + mw
,
βdSd
µ + γd + md
,
βdSd
γd + md
,
βhSh
γh + mh
}.
At the disease-free equilibrium, we have Sw = bw/mw, Sd = bd/md, Sh =
bh/mh. Therefore, the R0 value in a population entirely composed of susceptible
individuals is
R0 = max

βwbw
mh(γw + mw),
βdbd
md(µ + γd + md),
βdbd
md(γd + md),
βhbh
mh(γh + mh)

.
(14)
We further establish that R0 > 1 retains its traditional role as the threshold for
determining the viability of an epidemic using an analysis of the system’s Jacobian
matrix at the disease-free equilibria. Since we are interested only in the total number
of infected individuals, we consider the time evolution of disease burden across all
three compartments in the form (Iw, Id, Td, Ih):
dIw/dt
=
βwSwIw −γwIw −mwIw,
dId/dt
=
βdSdId + pdSdIw −µId −γdId −mdId
dTd/dt
=
µId + βdSdTd −γdTd −mdTd
dIh/dt
=
βhShIh + phShTd −γhIh −mhIh.
The Jacobian matrix of this system above at the disease-free equilibrium Ef =
(0, 0, 0, 0) is
23


## Page 24


J(Ef) =


βwSw −(γw + mw)
0
0
0
pdSd
βdSd −(µ + γd + md)
0
0
0
µ
βdSd −(γd + md)
0
0
0
phSh
βhSh −(γh + mh)


.
We ﬁrst establish results on the stability of the disease-free equilibrium Ef.
Theorem 5. Ef is asymptotically stable if R0 < 1 and unstable if R0 > 1.
Proof. At Ef = (0, 0, 0, 0), we have Sw = bw/mw, Sd = bd/md, Sh = bh/mh.
Thus, J(Ef) =


βwbw/mw −(γw + mw)
0
0
0
pdSd
βdbd/md −(µ + γd + md)
0
0
0
µ
βdbd/md −(γd + md)
0
0
0
phSh
βhbh/mh −(γh + mh)


.
If R0 < 1, then the diagonal entries of J(Ef), which are actually the eigenvalues
of the Jacobian matrix J(Ef), are strictly negative. Thus Ef is asymptotically stable if
R0 < 1. If R0 > 1, then at least one of the eigenvalues of the Jacobian matrix J(Ef)
(its diagonal entries) is strictly positive. Therefore Ef is unstable if Ro > 1.
We then establish similar results for the endemic equilibrium.
Theorem 6. Ee is asymptotically stable if R0 > 1 and unstable if R0 < 1.
Proof. According to our analysis of endemic equilibria above, we have
S∗
w
=
γw + mw
βw
,
S∗
d
<
γd + md
βd
,
S∗
h
<
γh + mh
βh
.
Substituting into the Jacobian matrix J(Ee) the values for S∗
w, S∗
d, S∗
h, the diagonal
entries of J(Ee) are either zero or negative. Therefore Ee is asymptotically stable if
R0 > 1. Similarly, we can prove Ee is unstable if R0 < 1.
24


## Page 25


Thus R0 retains its role as the threshold condition for an epidemic.
3.5. Threshold Parameters
The results above replicate the standard epidemiological ﬁnding that R0 is a thresh-
old condition for the system, but the interspecies connections in this model allow us to
establish a more detailed result. By Theorem 2 and Lemmas 1 and 2, the stability of
the equilibria depends on pd, ph and µ, the same parameters which control Sw, Sd, and
Sh in the calculation of R0. Indeed, only these parameters determine the results of the
epidemic.
Theorem 7. In the presence of a nonzero number of infected wild animals, Ee is stable
if and only if pd, µ, ph > 0.
Proof. (⇒) If the disease-free equilibrium is stable, Lemmas 1 and 2 show that pd, Iw, ph, Td >
0. Considering equation (6), the only way to obtain Td > 0 is to have µ > 0 as well.
(⇐) If pd, ph, µ > 0, a nonzero proportion Iw creates a positive force of infection
in equation (5), and since µ > 0 there is a positive force of infection in equation (6)
as well. With T ∗
d > 0 and ph > 0, there is a positive force of infection in equation
(9), and so I∗
h > 0, creating an endemic equilibrium in the human compartment. If all
of these conditions hold, regardless of the values of βi or γi in any species, there is a
nonzero, constant force of infection for each species and so the system is forced into
an endemic equilibrium.
3.6. Conclusion
This model has one disease-free equilibrium and one endemic equilibrium, whose
stability depends on pd, ph and µ. Isolating these parameters thus provides suggestions
for possible interventions. The results of Theorem 7, in particular, show that while
many parameters of the model can be changed by human intervention−βd could be
lowered by increasing biosecurity on farms for domestic animals, for example, while
much of public health and medicine offers strategies for changing βh and γh−the only
effective route for eliminating the possibility of a zoonotic epidemic in humans is to
25


## Page 26


eliminate contact between species or the possibility of pathogen mutation, an impossi-
ble requirement in any real system.
4. Numerical Simulations
To clarify the results of the theoretical analysis presented in section 3, we present
simulations of different cases of the model drawn from available data (summarized
in Table 4). To elucidate the effects of the interspecies transmission parameters−pd,
ph, and µ−we simulate cases where the pathogen fails to establish itself in wildlife,
in domestic animals, and in both populations, showing that the human population will
still suffer an endemic disease even if animal populations remain relatively unaffected
by a brief epidemic.
4.1. Examples
We ﬁrst simulate a zoonosis that establishes endemic equilibria in each host species,
using the baseline parameters with 5βw = 5βd to ensure the spread of the pathogen.
The outbreak shown in ﬁgure 4 infects a maximum of 46.33% of the human pop-
ulation and stabilizes at 19.04% of the population infected, reaching equilibria in all
three species by 150 units of time.
Next, to elucidate the effect of the mutation, we simulate an outbreak that fails to
establish itself in the wild population (in this case, this species does not function as a
reservoir host).
Figure 5 shows that even if the disease fails to persist in its wild reservoir host,
it can still become endemic in the human population. A maximum of 49.75% of the
human population was infected, with 19.62% infected at equilibrium by time 150. This
case illustrates that even if the epidemic fails to take hold among wild animals, it can
still spread to domestic animals and thus humans, illustrating the importance of pd as
a threshold parameter.
For our ﬁnal example, we simulate avian inﬂuenza mutating from a low-pathogenic
to a highly-pathogenic strain in an intermediate host. One of the best-known examples
of a zoonosis with an intermediate host, avian inﬂuenza spreads from wild birds to
26


## Page 27


0
0.5
1
1.5
2
2.5
3
Proportion S h
-0.12
-0.1
-0.08
-0.06
-0.04
-0.02
0
0.02
f, g
f
g
Sh1
Sh2
Figure 4: A simulation showing endemic equilibria in each species. Parameter values are as shown in Table 4,
with βw and βd multiplied by 5 to ensure spread in each compartment.
domestic poultry to humans, a process for which there is some publicly available data.
Seeding the model with the parameters shown in Table 4 (and assuming that βw =
βd, γw = γd), we obtain the result shown in ﬁgure 6.
This example−which uses the most data publicly available−shows that even if a
pathogen’s R0 is less than one in both wild and intermediate hosts, it can still establish
itself in the human population. Here, both strains of avian inﬂuenza fade in the animal
populations while establishing an endemic equilibrium in the human population, with
a maximum of 10.94% and an equilibrium of 7.65% of the population infected over a
time span an order of magnitude larger than that necessary in the previous examples
(t = 2000, not shown in the ﬁgure). This result indicates that the unexpected behavior
described in section 3 and modeled above does appear in real epidemics.
The results here are summarized in Table 5. The equilibrium proportion of infected
humans is highest in row 2 because there are more domestic animals infected with the
27


## Page 28


0
10
20
30
40
t
-0.2
0
0.2
0.4
0.6
0.8
1
1.2
proportion
Wild
0
10
20
30
40
t
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
proportion
Domestic
susceptible
wildtype infected
transmissible infected
recovered
0
50
100
150
200
t
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
proportion
Human
Wild DFE
Figure 5: A simulation showing a disease-free equilibrium in the wild reservoir host species that spills over
to endemic equilibria in the domestic intermediate host and humans. Parameters are as shown in Table 4,
except with βd multiplied by 5 to ensure an epidemic in the domestic compartment.
transmissible strain when the force of infection with the wildtype strain vanishes over
time.
These simulations illustrate that with nonzero transmission parameters, an initial
infection in an upstream host species will spread to an endemic equilibrium in down-
stream ones even if the pathogen fails to establish itself in its animal hosts.
4.2. Effects of Interspecies Transmission Parameters
In this section, we evaluate the effect of varying the interspecies transmission pa-
rameters pd, µ, and ph on the equilibrium values I∗
d, T ∗
d , and I∗
h after 3000 units of
time, in addition to βd and βh for comparison. To produce the graphs shown below,
we vary the parameter in question from 0.01 to 5 (since values of 0, as shown in sec-
tion 3, inevitably lead to a disease-free equilibrium in the human compartment), with
28


## Page 29


0
10
20
30
40
t
-0.2
0
0.2
0.4
0.6
0.8
1
1.2
proportion
Wild
0
10
20
30
40
t
-0.2
0
0.2
0.4
0.6
0.8
1
1.2
proportion
Domestic
susceptible
wildtype infected
transmissible infected
recovered
0
500
1000
t
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
proportion
Human
Avian Influenza
Figure 6: A simulation of low-pathogenic avian inﬂuenza mutating to high-pathenogenic avian inﬂuenza.
Parameters are as shown in Table 4.
a step size of 0.1, holding the other values constant at the endemic equilibrium param-
eters detailed in section 4.1. Each simulation is run for 3000 timesteps, to ensure that
an equilibrium solution is reached. In the domestic compartment, varying the trans-
mission parameters pd and µ can change the relative prevalence of the wildtype and
human-transmissible strains, as shown in Figures 7 and 8. (We do not examine the
effect varying ph has on the domestic compartment because that parameter does not
appear in the equations governing its behavior.)
Similarly, we vary pd, µ, and ph to examine the effect of these parameters on the
proportion of infected humans, ﬁnding that while increasing the mutation and inter-
mediate host-human contact rate increases this proportion, increasing pd lowers it (see
Figures 9, 10, and 11), as a larger contact rate between wild and domestic animals leads
to a larger proportion of animals infected with the non-human-transmissible strain and
thus unable to pass the disease to humans. Further, for comparison, we vary βh from 0
29


## Page 30


0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
5
pd
0
0.05
0.1
0.15
0.2
0.25
0.3
proportion infected
wildtype infected
transmissible infected
Figure 7: Graphing the proportion of domestic animals infected with the wildtype strain and the human-
transmissible strain against pd, the contact rate (spillover rate) between wild animals and domestic ones.
to 5 using the same step length of 0.01. As shown in Figure 12, while increasing βh
can effect the proportion of infected humans, even decreasing βh to 0 still leads to an
endemic equilibrium, with I∗
h > 0.
The importance of the interspecies transmission parameters is reﬂected in Figures
12 and 13, which show that even when the transmission rates of the pathogen in hu-
mans or domestic animals is set to 0, the disease can reach an endemic equilibrium in
humans. The effect of setting each parameter to in an otherwise endemic equilibrium,
where the epidemic is expected to remain endemic in all three species, as in Figure 4,
is summarized in Table 6.
These comparisons suggest that a lower number of animals infected with the trans-
missible strain has the potential to lower the proportion of infected humans, while even
if the intraspecies parameters βd or βh are set to 0 the epidemic can spread to infect the
human population. These results show that the interspecies transmission parameters
are primary targets for intervention to lower the proportion of infected humans in this
model.
30


## Page 31


0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
5
0
0.05
0.1
0.15
0.2
0.25
0.3
proportion infected
wildtype infected
transmissible infected
Figure 8: Graphing the proportion of domestic animals infected with the wildtype strain and the human-
transmissible strain against µ, the rate of mutation from the wildtype strain to the human-transmissible
strain.
0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
5
pd
0.178
0.18
0.182
0.184
0.186
0.188
0.19
0.192
0.194
0.196
0.198
proportion infected
Figure 9: Graphing the proportion of infected humans against pd.
31


## Page 32


0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
5
0.11
0.12
0.13
0.14
0.15
0.16
0.17
0.18
0.19
0.2
proportion infected
infected humans
Figure 10: Graphing the proportion of infected humans against µ, the rate of mutation from the wildtype
strain to the human-transmissible strain.
4.3. Summary
To test the result from section 3 that changing µ, ph, and pd matters more to the
eventual number of infected humans than changing βi or γi, the traditional parameters
targeted in public health interventions, we varied the parameters pd, µ, ph, βd, and βh
while holding the other values constant at an endemic equilibrium condition. The re-
sults of these numerical simulations show that varying pd and µ can change the relative
prevalence of domestic animals infected with the wildtype and human-transmissible
strains, which in turn can change the proportion of infected humans. Further, only by
setting one or more interspecies transmission parameters µ, pd, ph to 0 can the model
avoid an endemic equilibrium in humans. In particular, the pathogen can persist in
humans even if βh = 0.
While varying traditional epidemic parameters such as βi and γi can change the
relative numbers of individuals in each compartment, section 3 shows that only pd,
ph, and µ control the global behavior of a zoonotic epidemic, a result detailed by the
simulations in this section. These results show that a zoonotic pathogen can establish
32


## Page 33


0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
5
ph
0.1
0.12
0.14
0.16
0.18
0.2
0.22
0.24
proportion infected
infected humans
Figure 11: Graphing the proportion of infected humans against ph, the contact rate (spillover rate) between
domestic animals and humans.
0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
5
h
0.18
0.185
0.19
0.195
0.2
0.205
0.21
0.215
0.22
0.225
0.23
proportion infected
wildtype infected
Figure 12: Graphing the proportion of infected humans against βh, the transmission rate among humans.
Here, setting βh to 0 still gives rise to an endemic equilibrium of infected humans.
33


## Page 34


0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
5
d
0
0.05
0.1
0.15
0.2
0.25
proportion infected
wildtype infected
transmissible infected
infected humans
Figure 13: Graphing the proportion of infected humans and domestic animals against βd, the transmission
rate among domestic animals. Here, setting βd to 0 still gives rise to an endemic equilibrium of infected
humans.
itself in the human population as long as it is seeded with an initial infection in the wild
compartment and pd, ph and µ are nonzero, even if the human-transmissible strain is
incapable of being transmitted between humans.
5. Discussion
The results of the mathematical analysis in section 3 suggest that we can categorize
the parameters of the model into two types. The ﬁrst type is intracompartment param-
eters: the transmission and recovery rates βi and γi, which describe interactions in a
single species. The second is intercompartment parameters, which govern interactions
between members of two species. pd and ph, which indicate the spillover rate to do-
mestic animals and humans, obviously fall into this category; µ quantiﬁes the rate of
a mutation arising in domestic animals that makes the pathogen transmissible among
humans, and is thus also included. From Theorems 2 and 7, we see that it is only
these second parameters, and the initial proportion of infected wild animals, that have
34


## Page 35


the potential to alter the global dynamics of the three-species system to a disease-free
equilibrium. The examples in section 4 crystallize the result that parameters of the
second type are threshold values for the global progression of an epidemic: changing
values in the ﬁrst category only changes the relative proportions of each type of in-
dividual present at an equilibrium, not the stability of the equilibria, while changing
the values of parameters in the second category can change the global behavior of the
pathogen.
This complete simulation of an emerging zoonosis shows that even in cases where
the disease dies out in the wild compartment and would fail without an external force
of infection in the domestic one, it can establish an endemic equilibrium in humans.
Further, this result holds even if βh = 0, reﬂecting a pathogen in Stage 1 of the tradi-
tional categorization for zoonoses that would not be deemed a pandemic threat under
that framework. While the high endemic prevalence seen in Figure 6 may be due to an
overestimate of the pathogen’s transmissibility in humans−the model assumes that all
humans have an equally high exposure to poultry, while in reality agricultural workers
are the group most at risk−these simulations suggest that the threat posed by zoonoses
is more severe than previously assumed. Only by entirely suppressing at least one of
the transmission parameters, an extraordinarily difﬁcult feat, can public health ofﬁcials
prevent a pathogen with an intermediate host from establishing a presence in humans.
This result indicates that even the slightest possibility of contact between species or
selection for a pathogen more suited to humans raises pd, ph, or µ above 0 and thus
can lead to an endemic infection in humans. While this endemic equilibrium or rates
of transmission may be negligible in real populations, our results that the threat of
an emerging zoonosis cannot be completely erased even with extraordinarily effective
public health and medical interventions, conﬁrming the focus on prioritizing zoonoses
as mathematically sound and offering a warning for public health ofﬁcials.
5.1. Future Research
The lack of large, publicly available data sets, especially regarding the prevalence
of zoonotic infections in wild and domestic animals and the values for pd, ph, and µ,
limits our ability to reﬁne any model (Allen et al., 2012). While some research attempts
35


## Page 36


an explicit response to the lack of such by assessing expert approximations (Singh
et al., 2018), this type of analysis cannot replace population-level data. Gathering such
data is thus critical to future modeling efforts in domestic and wild animal populations
((Lloyd-Smith et al., 2015), (Lloyd-Smith et al., 2009))−in particular, there is little data
available for any infectious diseases in wild animals and interspecies contact rates−and
should form a key component of future efforts.
This research introduces a model capable of replicating all stages of the emergence
of a zoonosis with an intermediate host. To keep this work at a preliminary level and to
maximize its use in more specialized contexts, we have not considered further modiﬁ-
cations to the SIR prototype model such as loss of immunity (SIRS) or exposure time
(SEIR), or possible variation patterns in the number of infected reservoir hosts, such
as seasonal migration. Given adequate data, future research could add any of these
modiﬁcations, as well as others not considered here, and can thus adapt this model
to any speciﬁc emerging zoonosis. More speciﬁcally, future models should incorpo-
rate backwards transmission to wild animals, direct interactions between humans and
wild reservoirs, as well as interactions between different pathogens in an intermediate
host (Lloyd-Smith et al., 2009). Finally, since not all humans have the same level of
exposure to a given intermediate host species, a more reﬁned model could relax the
assumption of mass action in the human compartment. The modiﬁcations discussed
above have the potential to introduce more exciting dynamics, such as backward bi-
furcations or strange attractors in the solution space (Barrientos et al., 2017), a type of
behavior that could have implications for the policies governing zoonosis interventions.
In particular, future models should investigate the effect of different transmission
rates for the two strains circulating in the intermediate host, which will change the en-
demic equilibrium in domestic animals and thus humans. Here, we have abstracted
the process of mutation to a binary question regarding human transmissibility, neglect-
ing the distinction between the different possible ways for a pathogen to mutate and
the different possible degrees of change. The mutation rate of a zoonotic disease can
depend on social factors such as culling in the intermediate host population, vaccina-
tion of infected individuals, and biosecurity, as well as biological ones such as RNA
mutation or interstrain competition (Goodwin et al., 2012), and future research should
36


## Page 37


investigate whether those different processes have noticeable differences on the num-
ber of infected humans or the mathematical structure of the model. There is also a lack
of investigation of disease dynamics in individual hosts, with little data investigating
the effect of different expressions of pathogen genotypes or animal superspreaders (in-
dividuals who infect many more secondary cases than average) on transmissibility in
humans (Lloyd-Smith et al., 2009). As this effect is the one abstracted by our param-
eter µ, delving deeper into individual-host pathogen dynamics such as cellular entry
and replication (Allen et al., 2012) has the potential to improve our model. No emerg-
ing infected disease has been predicted before infecting humans (Morse et al., 2012),
although progress is being made on identifying disease ‘hotspots’ (Daszak, 2012), and
this inability reinforces the importance of studying the factors that lead to successful
spillover and deﬁne transmission rates between species (Morse et al., 2012).
This research suggests future avenues of exploration for both researchers and pol-
icymakers seeking to understand and control the spread of an emerging infectious
zoonosis, and proves that interspecies connections are critical to controlling and un-
derstanding the effect an emerging zoonosis can have on human populations. We show
that with nonzero transmission parameters and an initial population of infected wild
animals, a pathogen can fail to achieve traditional markers of success, such as stage
3 transmissibility, and still maintain an endemic equilibrium in the human population.
This is a concerning result for public health, but offers areas in which policy rather than
medical interventions can be more effective in controlling disease.
6. Conclusion
With the ability to study the emergence of a zoonosis with an intermediate host, ﬁrst
quantiﬁed by the model introduced here, scientists and policymakers alike have a more
reﬁned tool with which to study and confront one of the most well-recognized threats
to global health: the emergence of a new pandemic into the human population. To our
knowledge, this is the ﬁrst model that accounts for the entire course−from infected
wild animals, through mutation in an intermediate host, to an endemic equilibrium in
humans−of the type of zoonotic pathogen the World Health Organization ranks in the
37


## Page 38


highest tier of priorities for research and development, and so provides a signiﬁcant
step forward in its study.
We establish that the model has one unique disease-free equilibrium and one en-
demic equilibrium, and that the stability of these points depends on pd, ph, and µ, the
contact rates between species and the pathogen’s rate of mutation. Accurately identify-
ing and describing the dynamics of a pathogen circulating in wild and domestic animals
provides an invaluable opportunity to avoid risk to humans (Morse et al., 2012), and
can be used to guide public health interventions for emerging zoonotic diseases.
That the interspecies transmission parameters are the only threshold conditions for
this model suggests that the problem of controlling the spread of a zoonotic epidemic
has less to do with intracompartment controls than with intercompartment ones: rather
than efforts to control the transmission or recovery rates in one species, it is a more
effective intervention to control pd, ph, or µ through better biosecurity or population
control. This ﬁnding provides a blueprint for public health interventions in zoonoses,
as well as a warning for ofﬁcials hoping to prevent the spread of wildlife diseases to hu-
mans. The interspecies parameters−pd, ph, and µ−may be more susceptible to policy
changes than the intraspecies parameters βi and γi, at least when the domestic interme-
diate host is a livestock or pet species entirely under human control (Cunningham et al.,
2017). Even before a zoonotic epidemic is detected in other species, restructuring agri-
cultural systems and controlling livestock movements offer public health policymakers
avenues to mitigate the effects of such a pathogen. For example, by preventing disease
circulation on farms, we can prevent pathogens such as avian inﬂuenza from becoming
persistent human health risks (Karesh et al. (2012), Morse et al. (2012)). Since accu-
rate models can assist in appropriately allocating surveillance resources (Lloyd-Smith
et al., 2015), these parameters can thus guide health ofﬁcials in their response to and
prevention of emerging zoonoses, policy changes which are essential in mitigating the
risks of such diseases (Cunningham et al., 2017).
Our results primarily offer a warning to public health ofﬁcials: without drastic in-
terventions to drive interspecies interactions or pathogen mutation rates to 0, which
may be biologically impossible, zoonoses with the capacity to mutate in a human-
adjacent intermediate host can spread to humans even if they are not viable in a human
38


## Page 39


population alone. More fundamentally to the ﬁeld of mathematical epidemiology, this
result conﬁrms previously held beliefs−unquantiﬁed until now−about the philosoph-
ical importance of zoonoses to humanity. It is a pillar of the movement variously
called “global”, “one”, or “planetary health” that human populations cannot isolate
themselves from changes that affect other species with interventions targeting only hu-
mans. By mathematically linking the progress of a zoonotic epidemic to parameters
governing interactions between species, this model shows that the framework of an in-
terconnected human and natural world that implicitly underlies much of the analysis
in this ﬁeld in the last twenty years agrees with the mathematics of infectious disease,
quantifying and conﬁrming a widespread belief in global health.
Acknowledgments
We are grateful for generous support from the Neukom Institute at Dartmouth, the
Neukom CompX Faculty Grant, Walter & Constance Burke Research Initiation Award,
and NIH COBRE Award. F.F. acknowledges a Junior Faculty Fellowship funded by the
Dartmouth’s Dean of the Faculty for this work.
References
Allen, L., Brown, V., Jonsson, C., Klein, S. L., Laverty, S., Magwedere, K., Owen, J.,
Van Den Driessche, P., 2012. Mathematical modeling of viral zoonoses in wildlife.
Natural resource modeling 25 (1), 5–51.
Andraud, M., Hens, N., Marais, C., Beutels, P., 2012. Dynamic epidemiological models
for dengue transmission: a systematic review of structural approaches. PloS one
7 (11), e49085.
Anguelov, R., Garba, S. M., Usaini, S., 2014. Backward bifurcation analysis of epi-
demiological model with partial immunity. Computers & Mathematics with Appli-
cations 68 (9), 931–940.
39


## Page 40


Barrientos, P. G., Rodr´ıguez, J. ´A., Ruiz-Herrera, A., 2017. Chaotic dynamics in the
seasonally forced sir epidemic model. Journal of mathematical biology 75 (6-7),
1655–1668.
Bett, B., Henning, J., Abdu, P., Okike, I., Poole, J., Young, J., Randolph, T. F.,
Perry, B. D., 2014. Transmission rate and reproductive number of the h5n1 highly
pathogenic avian inﬂuenza virus during the december 2005–july 2008 epidemic in n
igeria. Transboundary and emerging diseases 61 (1), 60–68.
Chang, H.-H., Moss, E. L., Park, D. J., Ndiaye, D., Mboup, S., Volkman, S. K., Sabeti,
P. C., Wirth, D. F., Neafsey, D. E., Hartl, D. L., 2013. Malaria life cycle intensi-
ﬁes both natural selection and random genetic drift. Proceedings of the National
Academy of Sciences 110 (50), 20129–20134.
Cui, J.-a., Chen, F., Fan, S., 2017. Effect of intermediate hosts on emerging zoonoses.
Vector-Borne and Zoonotic Diseases 17 (8), 599–609.
Cunningham, A. A., Daszak, P., Wood, J. L., 2017. One health, emerging infectious
diseases and wildlife: two decades of progress? Philosophical Transactions of the
Royal Society B: Biological Sciences 372 (1725), 20160167.
Daszak, P., 2012. Anatomy of a pandemic. The Lancet 380 (9857), 1883–1884.
Daszak, P., Cunningham, A. A., Hyatt, A. D., 2000. Emerging infectious diseases of
wildlife–threats to biodiversity and human health. Science 287 (5452), 443–449.
de Vries, R., Herfst, S., Richard, M., 2018. Avian inﬂuenza a virus pandemic prepared-
ness and vaccine development. Vaccines 6 (3), 46.
de Wit, E., Munster, V. J., 2013. Mers-cov: the intermediate host identiﬁed? The
Lancet. Infectious diseases 13 (10), 827.
Diekmann, O., Heesterbeek, J., Roberts, M. G., 2009. The construction of next-
generation matrices for compartmental epidemic models. Journal of the Royal Soci-
ety Interface 7 (47), 873–885.
40


## Page 41


Earn, D. J., Rohani, P., Bolker, B. M., Grenfell, B. T., 2000. A simple model for com-
plex dynamical transitions in epidemics. Science 287 (5453), 667–670.
Florens, L., Washburn, M. P., Raine, J. D., Anthony, R. M., Grainger, M., Haynes,
J. D., Moch, J. K., Muster, N., Sacci, J. B., Tabb, D. L., et al., 2002. A proteomic
view of the plasmodium falciparum life cycle. Nature 419 (6906), 520.
Fourni´e, G., Guitian, J., Desvaux, S., Cuong, V. C., Pfeiffer, D. U., Mangtani, P., Ghani,
A. C., et al., 2013. Interventions for avian inﬂuenza a (h5n1) risk management in live
bird market networks. Proceedings of the National Academy of Sciences 110 (22),
9177–9182.
Garamszegi, L. Z., Møller, A. P., 2007. Prevalence of avian inﬂuenza and host ecology.
Proceedings of the Royal Society B: Biological Sciences 274 (1621), 2003–2012.
Gauthier-Clerc, M., Lebarbenchon, C., Thomas, F., 2007. Recent expansion of highly
pathogenic avian inﬂuenza h5n1: a critical review. Ibis 149 (2), 202–214.
Goodwin, R., Schley, D., Lai, K.-M., Ceddia, G. M., Barnett, J., Cook, N., 2012.
Interdisciplinary approaches to zoonotic disease. Infectious disease reports 4 (2).
Gulbudak, H., Cannataro, V. L., Tuncer, N., Martcheva, M., 2017. Vector-borne
pathogen and host evolution in a structured immuno-epidemiological system. Bul-
letin of mathematical biology 79 (2), 325–355.
Gumel, A., 2012. Causes of backward bifurcations in some epidemiological models.
Journal of Mathematical Analysis and Applications 395 (1), 355–365.
Gumel, A. B., 2009. Global dynamics of a two-strain avian inﬂuenza model. Interna-
tional Journal of Computer Mathematics 86 (1), 85–108.
Hassan, M. M., Hoque, M. A., Debnath, N. C., Yamage, M., Klaassen, M., 2017.
Are poultry or wild birds the main reservoirs for avian inﬂuenza in bangladesh?
EcoHealth 14 (3), 490–500.
Henaux, V., Samuel, M. D., Bunck, C. M., 2010. Model-based evaluation of highly and
low pathogenic avian inﬂuenza dynamics in wild birds. PLoS One 5 (6), e10997.
41


## Page 42


Hill, E. M., House, T., Dhingra, M. S., Kalpravidh, W., Morzaria, S., Osmani, M. G.,
Yamage, M., Xiao, X., Gilbert, M., Tildesley, M. J., 2017. Modelling h5n1 in
bangladesh across spatial scales: Model complexity and zoonotic transmission risk.
Epidemics 20, 37–55.
Hosseini, P. R., Fuller, T., Harrigan, R., Zhao, D., Arriola, C. S., Gonzalez, A., Miller,
M. J., Xiao, X., Smith, T. B., Jones, J. H., et al., 2013. Metapopulation dynam-
ics enable persistence of inﬂuenza a, including a/h5n1, in poultry. PloS one 8 (12),
e80091.
Hu, Z., Liu, S., Wang, H., 2008. Backward bifurcation of an epidemic model with stan-
dard incidence rate and treatment rate. Nonlinear Analysis: Real World Applications
9 (5), 2302–2312.
Hussaini, N., Okuneye, K., Gumel, A. B., 2017. Mathematical analysis of a model for
zoonotic visceral leishmaniasis. Infectious Disease Modelling 2 (4), 455–474.
Ito, T., Goto, H., Yamamoto, E., Tanaka, H., Takeuchi, M., Kuwayama, M., Kawaoka,
Y., Otsuki, K., 2001. Generation of a highly pathogenic avian inﬂuenza a virus from
an avirulent ﬁeld isolate by passaging in chickens. Journal of virology 75 (9), 4439–
4443.
Iwami, S., Takeuchi, Y., Liu, X., 2007. Avian–human inﬂuenza epidemic model. Math-
ematical biosciences 207 (1), 1–25.
Ji, Z., Wu, W., Feng, Y., Zhang, G., 2013. Constructing the lyapunov function through
solving positive dimensional polynomial system. Journal of Applied Mathematics
2013.
Karesh, W. B., Dobson, A., Lloyd-Smith, J. O., Lubroth, J., Dixon, M. A., Bennett,
M., Aldrich, S., Harrington, T., Formenty, P., Loh, E. H., et al., 2012. Ecology of
zoonoses: natural and unnatural histories. The Lancet 380 (9857), 1936–1945.
Keeling, M., Gilligan, C., 2000. Bubonic plague: a metapopulation model of a zoono-
sis. Proceedings of the Royal Society of London B: Biological Sciences 267 (1458),
2219–2230.
42


## Page 43


Kermack, W. O., McKendrick, A. G., 1927. A contribution to the mathematical theory
of epidemics. Proceedings of the Royal Society of London. Series A, Containing
papers of a mathematical and physical character 115 (772), 700–721.
Kermack, W. O., McKendrick, A. G., 1932. Contributions to the mathematical the-
ory of epidemics. ii.?the problem of endemicity. Proceedings of the Royal Society
of London. Series A, containing papers of a mathematical and physical character
138 (834), 55–83.
Kermack, W. O., McKendrick, A. G., 1933. Contributions to the mathematical the-
ory of epidemics. iii.?further studies of the problem of endemicity. Proceedings of
the Royal Society of London. Series A, Containing Papers of a Mathematical and
Physical Character 141 (843), 94–122.
Khan, M. A., Khan, Y., Islam, S., 2018. Complex dynamics of an seir epidemic model
with saturated incidence rate and treatment. Physica A: Statistical Mechanics and its
Applications 493, 210–227.
Kim, K. I., Lin, Z., Zhang, L., 2010. Avian-human inﬂuenza epidemic model with
diffusion. Nonlinear Analysis: Real World Applications 11 (1), 313–322.
Li, X.-Z., Li, W.-S., Ghosh, M., 2009. Stability and bifurcation of an sis epidemic
model with treatment. Chaos, Solitons & Fractals 42 (5), 2822–2832.
Li, Y., Qin, P., Zhang, J., 2018. Dynamics analysis of avian inﬂuenza a (h7n9) epidemic
model. Discrete Dynamics in Nature and Society 2018.
Lin, J., Andreasen, V., Levin, S. A., 1999. Dynamics of inﬂuenza a drift: the linear
three-strain model. Mathematical biosciences 162 (1-2), 33–51.
Liu, S., Ruan, S., Zhang, X., 2017. Nonlinear dynamics of avian inﬂuenza epidemic
models. Mathematical biosciences 283, 118–135.
Liu, Z., Fang, C.-T., 2015. A modeling study of human infections with avian inﬂuenza
a h7n9 virus in mainland china. International Journal of Infectious Diseases 41, 73–
78.
43


## Page 44


Lloyd-Smith, J. O., Funk, S., McLean, A. R., Riley, S., Wood, J. L., 2015. Nine chal-
lenges in modelling the emergence of novel pathogens. Epidemics 10, 35–39.
Lloyd-Smith, J. O., George, D., Pepin, K. M., Pitzer, V. E., Pulliam, J. R., Dobson,
A. P., Hudson, P. J., Grenfell, B. T., 2009. Epidemic dynamics at the human-animal
interface. Science 326 (5958), 1362–1367.
Ma, W., Lager, K., Vincent, A., Janke, B., Gramer, M., Richt, J., 2009. The role of
swine in the generation of novel inﬂuenza viruses. Zoonoses and public health 56 (6-
7), 326–337.
May, R. M., 1975. Biological populations obeying difference equations: stable points,
stable cycles, and chaos. Journal of Theoretical Biology 51 (2), 511–524.
Morse, S. S., Mazet, J. A., Woolhouse, M., Parrish, C. R., Carroll, D., Karesh, W. B.,
Zambrana-Torrelio, C., Lipkin, W. I., Daszak, P., 2012. Prediction and prevention of
the next pandemic zoonosis. The Lancet 380 (9857), 1956–1965.
Naresh, R., Tripathi, A., Tchuenche, J. M., Sharma, D., 2009. Stability analysis of a
time delayed sir epidemic model with nonlinear incidence rate. Computers & Math-
ematics with Applications 58 (2), 348–359.
Neumann, G., Noda, T., Kawaoka, Y., 2009. Emergence and pandemic potential of
swine-origin h1n1 inﬂuenza virus. Nature 459 (7249), 931.
Nowak, M. A., 2006. Evolutionary dynamics. Harvard University Press.
Nuno, M., Feng, Z., Martcheva, M., Castillo-Chavez, C., 2005. Dynamics of two-
strain inﬂuenza with isolation and partial cross-immunity. SIAM Journal on Applied
Mathematics 65 (3), 964–982.
Oliveira, R. D., Rezende, A. C., 2013. Global phase portraits of a sis model. Applied
Mathematics and Computation 219 (9), 4924–4930.
Pulliam, J. R., Epstein, J. H., Dushoff, J., Rahman, S. A., Bunning, M., Jamaluddin,
A. A., Hyatt, A. D., Field, H. E., Dobson, A. P., Daszak, P., 2011. Agricultural
44


## Page 45


intensiﬁcation, priming for persistence and the emergence of nipah virus: a lethal
bat-borne zoonosis. Journal of the Royal Society Interface 9 (66), 89–101.
Qi, X., Qian, Y.-H., Bao, C.-J., Guo, X.-L., Cui, L.-B., Tang, F.-Y., Ji, H., Huang, Y.,
Cai, P.-Q., Lu, B., et al., 2013. Probable person to person transmission of novel avian
inﬂuenza a (h7n9) virus in eastern china, 2013: epidemiological investigation. Bmj
347, f4752.
Richard, M., Graaf, M. d., Herfst, S., 2014. Avian inﬂuenza a viruses: from zoonosis
to pandemic. Future virology 9 (5), 513–524.
Roy, S., McElwain, T. F., Wan, Y., 2011. A network control theory approach to mod-
eling and optimal control of zoonoses: case study of brucellosis transmission in
sub-saharan africa. PLoS neglected tropical diseases 5 (10), e1259.
Sharma, V., Kaushik, S., Kumar, R., Yadav, J. P., Kaushik, S., 2019. Emerging trends
of nipah virus: A review. Reviews in medical virology 29 (1), e2010.
Singh, M., Toribio, J.-A., Scott, A. B., Groves, P., Barnes, B., Glass, K., Moloney,
B., Black, A., Hernandez-Jover, M., 2018. Assessing the probability of introduction
and spread of avian inﬂuenza (ai) virus in commercial australian poultry operations
using an expert opinion elicitation. PloS one 13 (3), e0193730.
Stiefs, D., Venturino, E., Feudel, U., et al., 2009. Evidence of chaos in eco-epidemic
models. Math. Biosci. Eng 6 (4), 855–871.
Stollenwerk, N., Aguiar, M., Ballesteros, S., Boto, J., Kooi, B., Mateus, L., 2012. Dy-
namic noise, chaos and parameter estimation in population biology. Interface Focus
2 (2), 156–169.
Taubenberger, J. K., Morens, D. M., 2006. 1918 inﬂuenza: the mother of all pandemics.
Emerging infectious diseases 12 (1), 15.
van den Driessche, P., 2017. Reproduction numbers of infectious disease models. In-
fectious Disease Modelling 2 (3), 288–303.
45


## Page 46


Van den Driessche, P., Watmough, J., 2002. Reproduction numbers and sub-threshold
endemic equilibria for compartmental models of disease transmission. Mathematical
biosciences 180 (1-2), 29–48.
Vandegrift, K. J., Sokolow, S. H., Daszak, P., Kilpatrick, A. M., 2010. Ecology of avian
inﬂuenza viruses in a changing world. Annals of the New York Academy of Sciences
1195 (1), 113–128.
Wang, J., Liu, S., Zheng, B., Takeuchi, Y., 2012. Qualitative and bifurcation analysis
using an sir model with a saturated treatment function. Mathematical and computer
modelling 55 (3-4), 710–722.
WHO, July 2018. List of blueprint priority diseases.
URL https://www.who.int/blueprint/priority-diseases/en/
Wolfe, N. D., Daszak, P., Kilpatrick, A. M., Burke, D. S., 2005. Bushmeat hunting, de-
forestation, and prediction of zoonotic disease. Emerging infectious diseases 11 (12),
1822.
Woolhouse, M. E., Gowtage-Sequeria, S., 2005. Host range and emerging and reemerg-
ing pathogens. Emerging infectious diseases 11 (12), 1842.
Woolhouse, M. E., Taylor, L. H., Haydon, D. T., 2001. Population biology of multihost
pathogens. Science 292 (5519), 1109–1112.
Xiao, Y., Sun, X., Tang, S., Wu, J., 2014. Transmission potential of the novel avian
inﬂuenza a (h7n9) infection in mainland china. Journal of theoretical biology 352,
1–5.
Yang, X.-S., 2001. Chaos in small-world networks. Physical Review E 63 (4), 046206.
Yusuf, A., Qureshi, S., Inc, M., Aliyu, A. I., Baleanu, D., Shaikh, A. A., 2018.
Two-strain epidemic model involving fractional derivative with mittag-lefﬂer ker-
nel. Chaos: An Interdisciplinary Journal of Nonlinear Science 28 (12), 123121.
46


## Page 47


Table 1: Zoonotic diseases with intermediate hosts
Disease
Reservoir Host
Intermediate Host
Source
Nipah virus encephalitis
bats
pigs
Karesh et al. (2012), Cunningham et al. (2017), Lloyd-Smith et al. (2015), Daszak et al. (2000)
Hendra virus disease
bats
horses
Cunningham et al. (2017), Lloyd-Smith et al. (2015), Daszak et al. (2000)
SARS
bats
civets
Lloyd-Smith et al. (2015)
Avian inﬂuenza
wild birds
domestic poultry, pigs
Vandegrift et al. (2010), Ito et al. (2001), Iwami et al. (2007)
Menangle virus disease
bats
pigs
Cunningham et al. (2017), Daszak et al. (2000)
Middle East Respiratory Syndrome
bats
camels
de Wit and Munster (2013)
Campylobacteriosis
wild birds
domestic poultry
Goodwin et al. (2012)
Japanese encephalitis
wild birds
pigs
Goodwin et al. (2012)
47


## Page 48


Wild
dSw/dt = bw −βwSwIw −mwSw
dIw/dt = βwSwIw −γwIw −mwIw
dRw/dt = γwIw −mwRw
Domestic
dSd/dt = bd −βdSdId −pdSdIw −βdSdTd −mdSd
dId/dt = βdSdId + pdSdIw −µId −γdId −mdId
dTd/dt = µId + βdSdTd −γdTd −mdTd
dRd/dt = γdId + γdTd −mdRd
Humans
dSh/dt = bh −βhShIh −phShTd −mhSh
dIh/dt = βhShIh + phShTd −γhIh −mhIh
dRh/dt = γhIh −mhRh
Table 2: ODE systems of our model with three host compartments (species), composed of wild reservoir
hosts, intermediate domestic animal hosts, and human hosts.
Si
susceptible individuals of species i
Ii
infected individuals of species i
Td
intermediate hosts infected with human-transmissible strain
Ri
recovered individuals of species i
βi
transmission rate among species i
γi
recovery rate among species i
bi
birth rate among species i
mi
natural mortality rate among species i
pd
transmission rate from reservoir to intermediate hosts
ph
transmission rate from intermediate hosts to humans
µ
mutation rate of the pathogen in the intermediate host population
Table 3: Parameter deﬁnitions.
48


## Page 49


Parameter
Value
Source
initial Sw
0.5
Singh et al. (2018)
initial Iw
0.5
Singh et al. (2018)
pd
0.51
Singh et al. (2018) ﬁgure 1
βd
0.89
Henaux et al. (2010) table 1 for wild birds
γd
0.981
Henaux et al. (2010) table 1
bd
1
assumed
md
1
assumed
ph
0.207
Xiao et al. (2014)
βh
0.078
Xiao et al. (2014)
γh
0.091
Xiao et al. (2014)
bh
0.0118
CDC
mh
0.009
CDC
µ
0.499
Singh et al. (2018) ﬁgure 3
Table 4: Parameter values and sources for the model. Due to a lack of data for transmission parameters in
wild animals, we assume βw, γw, bw, and mw to be equivalent to their counterparts in domestic animals.
Situation
Max Ih
Equilibrium Ih
Time to Equilibrium
Endemic in all species
46.33%
19.04%
102
Disease-free in wildlife
49.75%
19.62%
102
Avian inﬂuenza
10.94%
7.65%
103
Table 5: A comparison of the maximal and equilibrium values for the percentage of infected humans for
each representative strain.
49


## Page 50


Parameter
Maximum % of Infected Humans
Equilibrium % of Infected Humans
–
46.33
19.04
pd
0
0
µ
0
0
ph
0
0
βw
49.77
19.62
βd
18.81
11.16
βh
36.13
18.06
Table 6: Comparing the effect of setting each transmission parameter to 0 in the endemic equilibrium of
Figure 4.
50

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
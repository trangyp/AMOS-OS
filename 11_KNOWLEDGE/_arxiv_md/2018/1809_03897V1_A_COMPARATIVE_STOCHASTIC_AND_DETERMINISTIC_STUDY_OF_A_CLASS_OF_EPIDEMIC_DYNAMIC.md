---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1809.03897v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1809.03897v1_A_comparative_stochastic_and_deterministic_study_of_a_class_of_epidemic_dynamic_

> Source: 1809.03897v1_A_comparative_stochastic_and_deterministic_study_of_a_class_of_epidemic_dynamic_.pdf

> Pages: 109

---


## Page 1


arXiv:1809.03897v1  [q-bio.PE]  10 Sep 2018
A comparative stochastic and deterministic study of a class of
epidemic dynamic models for malaria: exploring the impacts of
noise on eradication and persistence of disease
Divine Wanduku
Department of Mathematical Sciences, Georgia Southern University, 65 Georgia Ave, Room 3042,
Statesboro, Georgia, 30460, U.S.A. E-mail:dwanduku@georgiasouthern.edu;wandukudivine@yahoo.com1
Abstract
A comparative stochastic and deterministic study of a family of SEIRS epidemic dynamic
models for malaria is presented. The family type is determined by the qualitative behavior of
the nonlinear incidence rates of the disease. Furthermore, the malaria models exhibit three
random delays:- two of the delays represent the incubation periods of the disease inside the
vector and human hosts, whereas the third delay is the period of eﬀective natural immunity
against the disease. The stochastic malaria models are improved by including the random
environmental ﬂuctuations in the disease transmission and natural death rates of humans.
Insights about the eﬀects of the delays and the noises on the malaria dynamics are gained
via comparative analyses of the family of stochastic and deterministic models, and further
critical examination of the signiﬁcance of the intensities of the white noises in the system
on (1) the existence and stability of the equilibria, and also on (2) the eradication and
persistence of malaria in the human population. The basic reproduction numbers and other
threshold values for malaria in the stochastic and deterministic settings are determined and
compared for the cases of constant or random delays in the system. Numerical simulation
1Corresponding author. Tel: +14073009605.
Preprint submitted to ArXiv
June 10, 2022


## Page 2


2
results are presented.
Keywords:
Disease-free and endemic steady states, Stochastic asymptotic stability, Basic
reproduction number, Lyapunov functional technique, white noise process
1. Introduction
Despite all eﬀorts to reduce the global burden of malaria, the WHO estimates released
in December 2016 exhibit that 212 million cases of the disease occurred in 2015 resulting
in about 429 thousand deaths. Furthermore, the highest mortality rates occurred in the
sub-Saharan African countries where about 90% of the global malaria cases occurred and
led to about 75% of the total world’s malaria deaths. Moreover, more than two third of the
global malaria related deaths were children in the age group under the age ﬁve years old.
In addition, despite the fact that malaria is curable and preventable, and despite all other
advances to control and contain the disease, the world at large is still far from complete
safety from the health and economic menace exhibited by the disease.
Indeed, WHO reports that in 2015, nearly half of the world’s population was at risk of
malaria, and the disease was actively and continuously transmitted in about 91 countries in
the world. Moreover, the most vulnerable populations include infants and children under the
age of ﬁve, pregnant women, patients with HIV/AIDS and non-immune migrants, visitors
and travellers to malaria endemic zones[46, 47]. These facts and observations sound a loud
call for understanding, cooperation, national solidarity, social and scientiﬁc investigation in
the ﬁght to eradicate or ameliorate the burdens of malaria.
Malaria is a vector-borne disease caused by protozoa (a micro-parasitic organism) of the
genus Plasmodium. There are several diﬀerent species of the parasite that cause disease in
humans namely: P. falciparum, P. viviax, P. ovale and P. malariae. However, the species
that causes the most severe and fatal disease is the P. falciparum. Malaria is transmitted


## Page 3


3
between humans by the infectious bite of a female mosquito of the genus Anopheles. Similar
to other mosquito-borne parasitic diseases such lymphatic ﬁlariasis, the complete life cycle of
the malaria plasmodium entails two-hosts: (1) the female anopheles mosquito vector, and (2)
the susceptible or infectious human being. The stage of the parasite infective to humans is
called sporozoite, while the stage of the parasite infective to mosquitoes is called gametocyte.
Indeed, as an infected female anopheles mosquito persistently quests and successfully
bites a human being to obtain a blood meal, she injects sporozoites through the salivary
glands into the blood stream of the susceptible or infected person. Inside the exposed or
infectious person, the sporoziotes are thought to develop in the liver into schizont which
contain numerous merozoites2. The mature schizonts rupture releasing the meroziotes into
the bloodstream.
The meroziotes infect red blood cells, and within the red blood they
either (1.) develop to form additional schizont in the blood stream that continue to infect
the human body, or (2.)
they develop to form a sexual stage of the plasmodium called
gametocyte. The stages of maturation of the plasmodium from the sporozoite through the
schizont stage within the human body is called the exo-erythrocytic cycle. Moreover, the
total duration of the exo-erythrocytic cycle is estimated at between 7-30 days depending on
the species of plasmodium, with the exceptions of the plasmodia- P. vivax and P. ovale that
may be delayed for as long as 1 to 2 years.
The gametocyte stage of the plasmodium (also referred to as the sexual stage of the
malaria parasite) which is infectious to susceptible or infectious female mosquitoes is ingested
by the female mosquito when she successfully takes a blood meal from an infectious human
being. Within the mosquito, the gametocyte develops into female and male gametes which
undergo fertilization and develop into sporozoites which can infect humans. The stages of
2Schizonts and merozoites are intermediary developmental stages of the parasite.


## Page 4


4
development from the gametocyte to infectious sporozoites within the mosquito is called
the sporogonic cycle. It is estimated that the duration of the sporogonic cycle is over 2 to
3 weeks [45, 46, 47]. The delay between infection of the mosquito and maturation of the
sporozoites suggests that the mosquito must survive a minimum of the 2 to 3 weeks to be
able to transmit malaria. These facts are important in deriving a mathematical model to
represent the dynamics of malaria.
In the general class of infectious diseases, vector-borne diseases such as malaria and
dengue fever exhibit several unique biological characteristics. For instance, as observed in
the description about the life cycle of the malaria parasite above, the incubation of the disease
requires two hosts - the vector and human hosts, which may be either directly involved in
a full life cycle of the infectious agent consisting of two separate and independent segments
of sub-life cycles that are completed separately in the two hosts or directly involved in two
separate and independent half-life cycles of the infectious agent in the hosts. Therefore, there
exists a total latent time lapse of disease incubation which extends over the two segments
of delayed incubation times namely:- (1) the incubation period of the infectious agent (
or the half-life cycle) in the vector, and (2) the incubation period of the infectious agent
(or the other half-life cycle) in the human being.
For example, the dengue fever virus
transmitted primarily by the Aedes aegypti and Aedes albopictus mosquitos undergoes two
delay incubation periods:- (1) about 8-12 days incubation period inside the female mosquito
vector, which starts immediately after the ingestion of a dengue fever virus infected blood
meal, that has been successfully taken from a dengue fever infectious human being via a
mosquito bite, and (2) another delay incubation period of about 2-7 days in the human being
when the hosting female infectious vector acquires another blood meal from a susceptible
human being, whereby the virus is successfully transferred from the infectious mosquito to


## Page 5


5
the susceptible person[46, 47].
Malaria confers natural immunity after recovery from the disease. The strength and ef-
fectiveness of the natural immunity against the disease depends primarily on the frequency
of exposure to the parasites and other biological factors such as age, pregnancy, and genetic
nature of red blood cells of people with malaria. The naturally acquired immunity against
malaria, especially in areas where malaria is highly endemic such as sub-sahara African,
varies across age groups and people with various biological characteristics etc. For exam-
ple, newborns, pregnant women and visitors from areas with little or no malaria history
exhibit low immunity levels against the malaria parasites, while adults who have suﬀered
repeated attacks tend to exhibit higher levels of protective natural immunity against the oc-
currence of severe disease. Other adults with history of malaria exposure are asymptomatic
to subsequent malaria attacks. Furthermore, other biological characteristics related to the
nature of red blood cells such as sickle cell trait, and Duﬀy blood group negativity etc. are
also noted to confer long lasting protective resistance against certain species of the malaria
parasite. For example, people with sickle cell trait are relatively more protected against p.
falciparum malaria, while people who are Duﬀy negative show strong resistance against P.
vivax malaria[47, 48, 49].
Various types of compartmental mathematical epidemic dynamic models have been pro-
posed and utilized to investigate the dynamics of infectious diseases. For instance, dengue
fever and measles are studied in [24, 25, 26]. Furthermore, several diﬀerent authors have
proposed various epidemic dynamic models for malaria beginning with Ross[29] who stud-
ied mosquito control, Macdonald[30] who addressed superinfection, a combined dynamics of
mosquitoes and humans investigated in [31], the naturally acquired immunity by continuing
exposure to malaria explored in [32, 33] and several other studies such as [34, 35, 36] which


## Page 6


6
are based on the mosquito biting habit. There are also studies which have instead focused
on the malaria parasite as the agent of disease transmission such as [37].
In general, the compartmental mathematical epidemic dynamic models are largely clas-
siﬁed as SIS, SIR, SIRS, SEIRS, and SEIR etc. epidemic dynamic models depending on the
compartments of the disease classes directly involved in the general disease dynamics[11, 12,
14, 15, 16, 42, 38, 17]. Several studies devote interest to SEIRS and SEIR models[15, 16,
18, 19, 17] which allow the inclusion of the compartment of individuals who are exposed to
the disease, E, that is, infected but noninfectious individuals. This natural inclusion of the
exposed class of individuals allows for more insight about the disease dynamics during the
incubation stage of the disease. For example, the existence of periodic solutions are investi-
gated in the SEIRS epidemic study[15, 17]. In addition, the eﬀects of seasonal changes on
the disease dynamics are investigated in the SEIRS epidemic study in [22].
Many epidemic dynamic models are modiﬁed and improved in reality by including the
time delays that occur in the disease dynamics. Generally, two distinct classes of delays
are studied namely:-disease latency and immunity delay.
The disease latency has been
represented as the infected but noninfectious period of disease incubation and also as the
period of infectiousness which nonetheless is studied as a delay in the dynamics of the disease.
The immunity delay represents the period of eﬀective naturally acquired immunity against
the disease after exposure and successful recovery from infection. Whereas, some authors
study diseases and disease scenarios under the realistic assumption of one form of these two
classes of delays in the disease dynamics[38, 39, 10, 11], other authors study one or more
forms of the classes of delays represented as two separate delay times[17, 13, 20, 21]. The
occurrence of delays in the disease dynamics may inﬂuence the dynamics of the disease in
many important ways. For instance, in [17], the presence of delays in the epidemic dynamic


## Page 7


7
system creates periodic solutions. In [1, 2], the occurrence of a delay in the vector-borne
disease dynamics destabilizes the equilibrium population state of the system.
Stochastic epidemic dynamic models more realistically represent epidemic dynamic pro-
cesses because they include the randomness which naturally occurs during a disease outbreak,
owing to the presence of constant random environmental ﬂuctuations in the disease dynam-
ics. The presence of stochastic white noise process in the epidemic dynamic system may
directly impact the density of the system or indirectly inﬂuence other driving parameters of
the system such as the disease transmission, natural death, birth and disease related death
rates etc. In [38, 42, 39], the stochastic white noise process represents the random ﬂuctu-
ations in the disease transmission process. In [11], the white noise process represents the
variability in the natural death of the population. In [3], the white noise process represents
the random ﬂuctuations in the system which deviate the state of the system from the equi-
librium state, that is, the white noise process is proportional to the diﬀerence between the
state and equilibrium of the system. A stochastic white noise process driven system gener-
ally exhibits more complex behavior in the disease dynamics. For instance, the presence of
stochastic white noise process in the disease dynamics may destabilize a disease free steady
state population by exhibiting high intensity values or high standard deviation values which
generally displace the population from a disease free state. In some cases, the presence of
white noise may lead to massive oscillations of the state of the system depending on the
intensity value of the random ﬂuctuations, which can decrease the population size over time
and lead to the extinction of the population. For example, in [11, 38, 42, 39, 27, 23], the
occurrence of stochastic noise in the system destabilizes the disease free steady population
state. In [11], the disease free steady state fails to exist when the intensity value of the white
noise process from the natural death process of the susceptible population is positive.


## Page 8


8
The interaction between susceptible, S, and infectious individuals, I, during the disease
transmission process of an infectious disease sometimes exhibits more complex behavior than
a simple representation by the frequently used bilinear incidence rate or force of infection
given as βS(t)I(t −T) for vector-borne diseases, or βS(t)I(t) for infectious diseases that
involve direct human-to-human disease transmission, where β is the eﬀective contact rate,
and T is the incubation period for the vector-borne disease. More complex behaviors such
as the psychological or crowding eﬀects stemming from behavioral change of susceptible
individuals when the infectious population increases signiﬁcantly over time exist for certain
types of infectious diseases and disease scenarios, where the contact between the susceptible
and infectious classes are regulated, and consequently prevent unboundedness in the disease
transmission rate, or exhibit other nonlinear behaviors for the disease transmission rate. For
instance, in [50, 7, 8, 10, 11, 51, 5, 6, 4, 52, 53] several diﬀerent functional forms for the
force of infection or incidence rate are used to represent the nonlinear behavior that occurs
during the disease transmission process. In [50, 7, 6, 8] the authors consider a Holling Type
II functional form, βS(t)G(I(t)) = βS(t)I(t)
1+αI(t) , that saturates for large values of I. In [51, 7, 4],
a bounded Holling Type II function, βS(t)G(I(t)) = βS(t)Ip(t)
1+αIp(t) , p ≥0, is used to represent
the force of infection of the disease. In [52, 53], the nonlinear behavior of the incidence
rate is represented by the general functional form, βS(t)G(I(t)) = βSp(t)Iq(t), p, q ≥0.
In addition, the authors in [50, 8, 6, 51, 4, 11] studied vector-borne diseases with several
diﬀerent functional forms for the nonlinear incidence rates of the disease.
Cooke[1] presented a deterministic epidemic dynamic model for a vector-borne disease,
where the bilinear incidence rate deﬁned as βS(t)I(t −T) represents the number of new
infections occurring per unit time during the disease transmission process. It is assumed
in the formulation of this incidence rate that the number of infectious vectors at time t


## Page 9


9
interacting and eﬀectively transmitting infection to susceptible individuals, S, after β number
of eﬀective contacts per unit time per infective is proportional to the infectious human
population, I, at earlier time t −T. The study above allows insight about the dynamics of
the disease primarily in the human population while keeping tract of the inﬂuence of the
vector on the dynamics via the disease transmission process. Whereas vector control aides
in malaria prevention[31, 35], in various events of emergency malaria crisis such as when
severe disease erupts, urgent medical interference on the involved human being requires
direct intervention by medical experts through the use of anti-malaria medications. This
observation necessitates a thorough continuous understanding of the dynamics of malaria
with major emphasis based in the human population especially in a realistic framework
where the system is constantly bombarded by random environmental ﬂuctuations.
Very
little or nothing about the dynamics of malaria in the human population in a more realistic
white noise driven mathematical dynamic system is known. This study bridges the gap by
providing a comparative stochastic and deterministic study of a class of malaria models, in
an attempt to elucidate the inﬂuence of underlying random perturbations on the dynamics
of the disease, in particular, on disease eradication via studying the stability of equilibria,
extinction and permanence of disease via studying the asymptotic properties of the solutions
of the systems.
This paper employs similar reasoning in [1], to derive a general class of SEIRS stochastic
epidemic dynamic models with three delays for vector-borne diseases such as malaria. The
three delays are classiﬁed under the two general group types namely:- disease latency and
immunity delay. Two of the delays represent the incubation period of the infectious agent
(plasmodium for malaria) inside the vector and human hosts, and the third delay repre-
sents the period of eﬀective naturally acquired immunity against the vector-borne disease,


## Page 10


10
where the natural immunity is conferred after recovery from infection. Moreover, the delays
are random variables. In addition, the general vector-borne disease dynamics is driven by
stochastic white noise processes originating from the random environmental ﬂuctuations in
the natural death and disease transmission rates in the population. The deterministic version
of the epidemic dynamic model is a system of ordinary diﬀerential equations. The stochastic
version of the epidemic dynamic model is a system of Ito-Doob type stochastic diﬀerential
equations.
It should be noted that this study addresses some objectives of a sizeable ongoing project.
To conserve space, a parallel detailed study about the qualitative behavior of the intensity
of the random ﬂuctuations in the disease dynamics ( which are represented by the white
noise processes in the stochastic model) in relation to the stochastic asymptotic stability of
the steady states of the system, and with critical examination of the eﬀects of the intensi-
ties on disease eradication from the stochastic system appears elsewhere. In that parallel
study, various novel mathematical techniques are utilized to diagnose and elucidate the ﬁ-
nite properties of the white noise processes in the system, critically evaluate and describe
their impact on the disease dynamics. In the current paper, the primary goal is to gain
complete comparative insight about the general asymptotic properties of the deterministic
and stochastic systems:- (2.8)-(2.11) and (2.15)-(2.18), and with attention given to show
how the occurrence of noise and delays in the disease dynamics create several interesting
features of the disease dynamics in relation to the qualitative behavior of (1) the equilibria
of the systems, whenever the equilibria exist, and (2) the trajectories of the stochastic system
near potential deterministic equilibria in the system. Moreover, the interconnection between
the two diﬀerent types of dynamical systems (stochastic and deterministic) with respect to
the asymptotic stability of the equilibria, and asymptotic behavior of the solutions of the


## Page 11


11
stochastic system near potential deterministic equilibria is established.
This work is presented as follows:- In section 2, the stochastic and deterministic epidemic
dynamic models for malaria are derived.
In section 3, the model validation results are
presented for both the deterministic and stochastic systems.
In section 4, the existence
and asymptotic properties of the disease free equilibrium population in both systems are
investigated. In Section 5, existence and the asymptotic properties of the endemic equilibria
of both systems are also investigated. And in Section 6, numerical simulation results are
given to justify the results of this paper.
2. Derivation of Model
A generalized class of stochastic SEIRS delayed epidemic dynamic models for vector-
borne diseases is presented. The delays represent the incubation period of the infectious
agents in the vector T1, and in the human host T2. The third delay represents the naturally
acquired immunity period of the disease T3, where the delays are random variables with
density functions fT1, t0 ≤T1 ≤h1, h1 > 0, and fT2, t0 ≤T2 ≤h2, h2 > 0 and fT3, t0 ≤
T3 < ∞. Furthermore, the joint density of T1 and T2 is given by fT1,T2, t0 ≤T1 ≤h1, t0 ≤
T2 ≤h2. Moreover, it is assumed that the random variables T1 and T2 are independent
(i.e.
fT1,T2 = fT1.fT2, t0 ≤T1 ≤h1, t0 ≤T2 ≤h2).
Indeed, the independence between
T1 and T2 is justiﬁed from the understanding that the incubation of the infectious agent
for the vector-borne disease depends on the suitable biological environmental requirements
for incubation inside the vector and the human body which are unrelated. Furthermore,
the independence between T1 and T3 follows from the lack of any real biological evidence
to justify the connection between the incubation of the infectious agent inside the vector
and the acquired natural immunity conferred to the human being. But T2 and T3 may be


## Page 12


12
dependent as biological evidence suggests that the naturally acquired immunity is induced
by exposure to the infectious agent.
By employing similar reasoning in [1, 11, 4, 8], the expected incidence rate of the dis-
ease or force of infection of the disease at time t due to the disease transmission process
between the infectious vectors and susceptible humans, S(t), is given by the expression
β
R h1
t0 fT1(s)e−µsS(t)G(I(t −s))ds, where µ is the natural death rate of individuals in the
population, and it is assumed for simplicity that the natural death rate for the vectors and
human beings are the same. The probability rate, 0 < e−µs ≤1, s ∈[t0, h1], h1 > 0, repre-
sents the survival probability rate of exposed vectors over the incubation period, T1, of the
infectious agent inside the vectors with the length of the period given as T1 = s, ∀s ∈[t0, h1],
where the vectors acquired infection at the earlier time t −s from an infectious human via a
successful infected blood meal, and become infectious at time t. Furthermore, it is assumed
that the survival of the vectors over the incubation period of length s ∈[t0, h1] is independent
of the age of the vectors. In addition, I(t −s), is the infectious human population at earlier
time t −s, G is a nonlinear incidence function of the disease dynamics, and β is the average
number of eﬀective contacts per infectious individual per unit time. Indeed, the force of
infection, β
R h1
t0 fT1(s)e−µsS(t)G(I(t −s))ds signiﬁes the expected rate of new infections at
time t between the infectious vectors and the susceptible human population S(t) at time t,
where the infectious agent is transmitted per infectious vector per unit time at the rate β.
Furthermore, it is assumed that the number of infectious vectors at time t is proportional to
the infectious human population at earlier time t −s. Moreover, it is further assumed that
the interaction between the infectious vectors and susceptible humans exhibits nonlinear
behavior, for instance, psychological and overcrowding eﬀects, which is characterized by the


## Page 13


13
nonlinear incidence function G. Therefore, the force of infection given by
β
Z h1
t0
fT1(s)e−µsS(t)G(I(t −s))ds,
(2.1)
represents the expected rate at which infected individuals leave the susceptible state and
become exposed at time t.
The susceptible individuals who have acquired infection from infectious vectors but are
non infectious form the exposed class E. The population of exposed individuals at time t is
denoted E(t). After the incubation period, T2 = u ∈[t0, h2], of the infectious agent in the
exposed human host, the individual becomes infectious, I(t), at time t. Applying similar
reasoning in [13], the exposed population, E(t), at time t can be written as follows
E(t) = E(t0)e−µ(t−t0)p1(t −t0) +
Z t
t0
βS(ξ)e−µT1G(I(ξ −T1))e−µ(t−ξ)p1(t −ξ)dξ,
(2.2)
where
p1(t −ξ) =





0, t −ξ ≥T2,
1, t −ξ < T2
(2.3)
represents the probability that an individual remains exposed over the time interval [ξ, t].
It is easy to see from (2.2) that under the assumption that the disease has been in the
population for at least a time t > maxt0≤T1≤h1,t0≤T2≤h2 (T1 + T2), in fact, t > h1 + h2, so that
all initial perturbations have died out, the expected number of exposed individuals at time
t is given by
E(t) =
Z h2
t0
fT2(u)
Z t
t−u
β
Z h1
t0
fT1(s)e−µsS(v)G(I(v −s))e−µ(t−u)dsdvdu.
(2.4)


## Page 14


14
Similarly, for the removal population, R(t), at time t, individuals recover from the infectious
state I(t) at the per capita rate α and acquire natural immunity. The natural immunity
wanes after the varying immunity period T3 = r ∈[t0, ∞], and removed individuals become
susceptible again to the disease. Therefore, at time t, individuals leave the infectious state at
the rate αI(t) and become part of the removal population R(t). Thus, at time t the removed
population is given by the following equation
R(t) = R(t0)e−µ(t−t0)p2(t −t0) +
Z t
t0
αI(ξ)e−µ(t−ξ)p2(t −ξ)dξ,
(2.5)
where
p2(t −ξ) =





0, t −ξ ≥T3,
1, t −ξ < T3
(2.6)
represents the probability that an individual remains naturally immune to the disease over
the time interval [ξ, t]. But it follows from (2.5) that under the assumption that the disease
has been in the population for at least a time t > maxt0≤T1≤h1,t0≤T2≤h2,T3≥t0 (T1 + T2, T3) ≥
maxt0≤T3 (T3), in fact, the disease has been in the population for suﬃciently large amount
of time so that all initial perturbations have died out, then the expected number of removal
individuals at time t can be written as
R(t) =
Z ∞
t0
fT3(r)
Z t
t−r
αI(v)e−µ(t−v)dvdr.
(2.7)
There is also constant birth rate B of susceptible individuals in the population. Furthermore,
individuals die additionally due to disease related causes at the rate d. A compartmental
framework illustrating the transition rates between the diﬀerent states in the system and
also showing the delays in the disease dynamics is given in Figure 1.


## Page 15


15
S
E
I
R
B
Finite incubation period inside
the exposed human body
= T2
Short or sufficiently
long natural immunity period = T3
d
Figure 1: The compartmental framework illustrates the transition rates between the states S, E, I, R of the
system. It also shows the incubation delay T2 and the naturally acquired immunity T3 periods.
It follows from (2.1), (2.4), (2.7) and the transition rates illustrated in the compartmental
framework in Figure 1 above that the family of SEIRS epidemic dynamic models for a vector-
borne diseases in the absence of any random environmental ﬂuctuations can be written as


## Page 16


16
follows:
dS(t)
=

B −βS(t)
Z h1
t0
fT1(s)e−µsG(I(t −s))ds −µS(t) + α
Z ∞
t0
fT3(r)I(t −r)e−µrdr

dt,
(2.8)
dE(t)
=

βS(t)
Z h1
t0
fT1(s)e−µsG(I(t −s))ds −µE(t)
−β
Z h2
t0
fT2(u)S(t −u)
Z h1
t0
fT1(s)e−µs−µuG(I(t −s −u))dsdu

dt,
(2.9)
dI(t)
=

β
Z h2
t0
fT2(u)S(t −u)
Z h1
t0
fT1(s)e−µs−µuG(I(t −s −u))dsdu −(µ + d + α)I(t)

dt,
(2.10)
dR(t)
=

αI(t) −µR(t) −α
Z ∞
t0
fT3(r)I(t −r)e−µsdr

dt,
(2.11)
where the initial conditions are given in the following: Let h = h1 + h2 and deﬁne
(S(t), E(t), I(t), R(t)) = (ϕ1(t), ϕ2(t), ϕ3(t), ϕ4(t)) , t ∈(−∞, t0],
ϕk ∈C((−∞, t0], R+), ∀k = 1, 2, 3, 4,
ϕk(t0) > 0, ∀k = 1, 2, 3, 4,
(2.12)
where C((−∞, t0], R+) is the space of continuous functions with the supremum norm
||ϕ||∞= sup
t≤t0
|ϕ(t)|.
(2.13)
It is assumed that the eﬀects of random environmental ﬂuctuations lead to variability in
the disease transmission and natural death rates. For t ≥t0, let (Ω, F, P) be a complete


## Page 17


17
probability space, and Ft be a ﬁltration (that is, sub σ- algebra Ft that satisﬁes the following:
given t1 ≤t2 ⇒Ft1 ⊂Ft2; E ∈Ft and P(E) = 0 ⇒E ∈F0 ). Indeed, the variability in the
disease transmission and natural death rates are represented by the white noise processes as
follows:
µ →µ + σiξi(t),
ξi(t)dt = dwi(t), i = S, E, I, R,
β →β + σβξβ(t),
ξβ(t)dt = dwβ(t),
(2.14)
where ξi(t) and wi(t) represent the standard white noise and normalized Wiener processes for
the ith state at time t, with the following properties: w(0) = 0, E(W(t)) = 0, var(w(t)) = t.
Furthermore, var(µ(t)) = σ2
i , i = S, E, I, R, represents the intensity value of the environ-
mental white noise process due to the random ﬂuctuations in the natural death rate in the
ith state, and var(β(t)) = σ2
β is the intensity value of the white noise process due to the
random ﬂuctuations in the disease transmission rate.
Indeed, the intensity values σ2
i , i = S, E, I, R, β of the white noise processes: ˜µ(t) = µ +
σiξi(t) and ˜β(t) = β+σβξβ(t) representing the variability in the natural death rate, ˜µ(t), and
disease transmission rate, ˜β(t), at time t, owing to the random ﬂuctuations that occur during
the disease transmission and natural death processes of the disease dynamics, measures the
average deviation of the random variable disease transmission, ˜β, and natural death, ˜µ, rates
from their constant mean values - β and µ, respectively, over the inﬁnitesimally small time
interval [t, t + dt]. This measure reﬂects the force of the random ﬂuctuations that occur
during the disease outbreak at anytime, which lead to oscillations in the natural death and
disease transmission rates overtime, and consequently lead to oscillations of the sizes of the
susceptible, exposed, infectious and removal classes of the total population over time during
the disease outbreak.


## Page 18


18
Substituting (2.14) into the deterministic system (2.8)-(2.11) leads to the following gener-
alized system of Ito-Doob stochastic diﬀerential equations describing the dynamics of vector-
borne diseases in the human population.
dS(t)
=

B −βS(t)
Z h1
t0
fT1(s)e−µsG(I(t −s))ds −µS(t) + α
Z ∞
t0
fT3(r)I(t −r)e−µrdr

dt
−σSS(t)dwS(t) −σβS(t)
Z h1
t0
fT1(s)e−µsG(I(t −s))dsdwβ(t)
(2.15)
dE(t)
=

βS(t)
Z h1
t0
fT1(s)e−µsG(I(t −s))ds −µE(t)
−β
Z h2
t0
fT2(u)S(t −u)
Z h1
t0
fT1(s)e−µs−µuG(I(t −s −u))dsdu

dt
−σEE(t)dwE(t) + σβS(t)
Z h1
t0
fT1(s)e−µsG(I(t −s))dsdwβ(t)
−σβ
Z h2
t0
fT2(u)S(t −u)
Z h1
t0
fT1(s)e−µs−µuG(I(t −s −u))dsdudwβ(t)
(2.16)
dI(t)
=

β
Z h2
t0
fT2(u)S(t −u)
Z h1
t0
fT1(s)e−µs−µuG(I(t −s −u))dsdu −(µ + d + α)I(t)

dt
−σII(t)dwI(t) + σβ
Z h2
t0
fT2(u)S(t −u)
Z h1
t0
fT1(s)e−µs−µuG(I(t −s −u))dsdudwβ(t)
(2.17)
dR(t)
=

αI(t) −µR(t) −α
Z ∞
t0
fT3(r)I(t −r)e−µsdr

dt −σRR(t)dwR(t),
(2.18)
where the initial conditions are given in the following: Let h = h1 + h2 and deﬁne
(S(t), E(t), I(t), R(t)) = (ϕ1(t), ϕ2(t), ϕ3(t), ϕ4(t)) , t ∈(−∞, t0],
ϕk ∈C((−∞, t0], R+), ∀k = 1, 2, 3, 4,
ϕk(t0) > 0, ∀k = 1, 2, 3, 4,
(2.19)


## Page 19


19
where C((−∞, t0], R+) is the space of continuous functions with the supremum norm
||ϕ||∞= sup
t≤t0
|ϕ(t)|.
(2.20)
Furthermore, the random continuous functions ϕk, k = 1, 2, 3, 4 are F0 −measurable, or
independent of w(t) for all t ≥t0.
Several epidemiological studies [9, 17, 15, 10, 11] have been conducted involving families of
SIR, SEIRS, SIS etc. epidemic dynamic models, where the family type is determined by the
class of functions satisfying diﬀerent general assumptions which characterize the nonlinear
character of the incidence function G(I) of the disease dynamics. Some general properties
of the incidence function G assumed in this study include the following:
Assumption 2.1.
A1 G(0) = 0.
A2 G(I) is strictly monotonic on [0, ∞).
A3 G′′(I) < 0 ⇔G(I) is diﬀerentiable concave on [0, ∞).
A4 limI→∞G(I) = C, 0 ≤C < ∞⇔G(I) has a horizontal asymptote 0 ≤C < ∞.
A5 G(I) ≤I, ∀I > 0 ⇔G(I) is at most as large as the identity function f : I 7→I over
the positive all I ∈(0, ∞).
An incidence function G that satisﬁes Assumption 2.1 A1-A5 can be used to describe the
disease transmission process of a vector-borne disease scenario, where the disease dynam-
ics is represented by the system (2.15)-(2.18), and the disease transmission rate between
the vectors and the human beings initially increases or decreases for small values of the
infectious population size, and is bounded or steady for suﬃciently large size of the infec-
tious individuals in the population. It is noted that Assumption 2.1 is a generalization of
some subcases of the assumptions A1-A5 investigated in [9, 17, 10, 11]. Some examples
of frequently used incidence functions in the literature that satisfy Assumption 2.1A1-A5


## Page 20


20
include: G(I(t)) =
I(t)
1+αI(t), α > 0, G(I(t)) =
I(t)
1+αI2(t), α > 0, G(I(t)) = Ip(t), 0 < p < 1 and
G(I) = 1 −e−aI, a > 0.
Observe that (2.16) and (2.18), and the corresponding equations (2.9) and (2.11) all
decouple from the other two equations in their respective systems: (2.15)-(2.18) and (2.8)-
(2.11). Nevertheless, for convenience most of the results in this paper related to the systems
(2.15)-(2.18) and (2.8)-(2.11) will be shown mostly for the vector X(t) = (S(t), E(t), I(t))T.
The following notations are utilized:
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
Y (t)
=
(S(t), E(t), I(t), R(t))T
X(t)
=
(S(t), E(t), I(t))T
N(t)
=
S(t) + E(t) + I(t) + R(t).
(2.21)
3. Model Validation Results
The analysis and results in this manuscript are exhibited for both the deterministic and
stochastic systems (2.8)-(2.11) and (2.15)-(2.18). These necessitate the existence and unique-
ness of the solutions of the stochastic and deterministic systems. The standard methods
utilized in the earlier studies[41, 38, 39, 40] are applied to establish the results. The follow-
ing Lemma describes the behavior of the positive local solutions for the systems (2.8)-(2.11)
and (2.15)-(2.18). This result will be useful in establishing the existence and uniqueness
results for the global solutions of the deterministic and stochastic systems (2.8)-(2.11) and
(2.15)-(2.18).
Lemma 3.1. Suppose for some τe > t0 ≥0 the systems (2.8)-(2.11) and (2.15)-(2.18)
with initial conditions in (2.12)-(2.13) and (2.19)-(2.20) respectively have unique positive
solutions denoted Y (t) ∈R4
+, for all t ∈(−∞, τe], then if N(t0) ≤
B
µ , it follows that


## Page 21


21
N(t) ≤B
µ . In addition, the set denoted by
D(τe) =

Y (t) ∈R4
+ : N(t) = S(t) + E(t) + I(t) + R(t) ≤B
µ , ∀t ∈(−∞, τe]

= ¯B(−∞,τe]
R4
+,

0, B
µ

,
(3.1)
is locally self-invariant with respect to the systems (2.8)-(2.11) and (2.15)-(2.18), where
¯B(−∞,τe]
R4
+,

0, B
µ

is the closed ball in R4
+ centered at the origin with radius B
µ containing the
local positive solutions deﬁned over (−∞, τe].
Proof:
The proof of the result for (2.8)-(2.11) and (2.15)-(2.18) are the same, hence without of loss
of generality, the result will be shown only for the stochastic system (2.15)-(2.18). It follows
directly from (2.15)-(2.18) that
dN(t) = [B −µN(t) −dI(t)]dt.
(3.2)
The result then follows easily by observing that for Y (t) ∈R4
+, the equation (3.2) leads to
N(t) ≤B
µ −B
µ e−µ(t−t0) + N(t0)e−µ(t−t0). And under the assumption that N(t0) ≤B
µ , the
result follows.
The following set of theorems presents the existence and uniqueness results for the global
solutions of the deterministic and stochastic systems (2.8)-(2.11) and (2.15)-(2.18). First,
the existence results for the deterministic system (2.8)-(2.11) is established. The standard
technique applied in [41] is utilized to establish the results.
Theorem 3.1. Given the initial conditions (2.12)-(2.13), there exists a unique solution
Y (t) = (S(t), E(t), I(t), R(t))T satisfying (2.8)-(2.11), for all t ≥t0.
Moreover, the so-
lution is nonnegative for all t ≥t0 and also lies in D(∞). That is, S(t) > 0, E(t) > 0, I(t) >
0, R(t) > 0, ∀t ≥t0 and
lim sup
t→∞
N(t) ≤S∗
0 = B
µ ,
(3.3)
for N(t) = S(t) + E(t) + I(t) + R(t), and Y (t) ∈D(∞) = ¯B(−∞,∞)
R4
+,

0, B
µ

, where D(∞) is


## Page 22


22
deﬁned in (3.1).
Proof:
It is easy to see that the rate functions of the system (2.8)-(2.11) are nonlinear, continuous in
their argument variables, and satisfy the local Lipschitz condition for the given initial data
(2.12)-(2.13). Therefore, there exists a unique local solution Y (t) = (S(t), E(t), I(t), R(t))T
on t ∈(−∞, τe], where τe > t0 ≥0. The rest of the result such as showing that the local
solution is positive and extending the local solution inductively to a global positive solution
follow a standard technique [41]. Moreover, from Lemma 3.1, it follows that Y (t) ∈D(∞)
and (3.3) holds.
The next theorem presents the existence and uniqueness results for the global solutions
of the stochastic system (2.15)-(2.18). The standard technique applied in [38, 39] is utilized
to establish the results.
Theorem 3.2. Given the initial conditions (2.19) and (2.20), there exists a unique solu-
tion process X(t, w) = (S(t, w), E(t, w), I(t, w))T satisfying (2.15)-(2.18), for all t ≥t0.
Moreover, the solution process is positive for all t ≥t0 a.s. and lies in D(∞). That is,
S(t, w) > 0, E(t, w) > 0, I(t, w) > 0, ∀t ≥t0 a.s. and X(t, w) ∈D(∞) = ¯B(−∞,∞)
R4
+,

0, B
µ

,
where D(∞) is deﬁned in Lemma 3.1, (3.1).
Proof:
It is easy to see that the coeﬃcients of (2.15)-(2.18) satisfy the local Lipschitz condition
for the given initial data (2.19).
Therefore there exist a unique maximal local solution
X(t, w) = (S(t, w), E(t, w), I(t, w)) on t ∈(−∞, τe(w)], where τe(w) is the ﬁrst hitting time
or the explosion time[43]. The following shows that X(t, w) ∈D(τe) almost surely, where
D(τe(w)) is deﬁned in Lemma 3.1 (3.1). Deﬁne the following stopping time





τ+
=
sup{t ∈(t0, τe(w)) : S|[t0,t] > 0,
E|[t0,t] > 0,
and
I|[t0,t] > 0},
τ+(t)
=
min(t, τ+),
for
t ≥t0.
(3.4)


## Page 23


23
and lets show that τ+(t) = τe(w) a.s. Suppose on the contrary that P(τ+(t) < τe(w)) > 0.
Let w ∈{τ+(t) < τe(w)}, and t ∈[t0, τ+(t)). Deﬁne





V (X(t)) = V1(X(t)) + V2(X(t)) + V3(X(t)),
V1(X(t)) = ln(S(t)),
V2(X(t)) = ln(E(t)),
V3(X(t)) = ln(I(t)), ∀t ≤τ+(t).
(3.5)
It follows from (3.5) that
dV (X(t)) = dV1(X(t)) + dV2(X(t)) + dV3(X(t)),
(3.6)
where
dV1(X(t))
=
1
S(t)dS(t) −1
2
1
S2(t)(dS(t))2
=
 B
S(t) −β
Z h1
t0
fT1(s)e−µsG(I(t −s))ds −µ +
α
S(t)
Z ∞
t0
fT3(r)I(t −r)e−µrdr
−1
2σ2
S −1
2σ2
β
Z h1
t0
fT1(s)e−µsG(I(t −s))ds
2#
dt
−σSdwS(t) −σβ
Z h1
t0
fT1(s)e−µsG(I(t −s))dsdwβ(t),
(3.7)


## Page 24


24
dV2(X(t))
=
1
E(t)dE(t) −1
2
1
E2(t)(dE(t))2
=

β S(t)
E(t)
Z h1
t0
fT1(s)e−µsG(I(t −s))ds −µ
−β
1
E(t)
Z h2
t0
fT2(u)S(t −u)
Z h1
t0
fT1(s)e−µs−µuG(I(t −s −u))dsdu
−1
2σ2
E −1
2σ2
β
S2(t)
E2(t)
Z h1
t0
fT1(s)e−µsG(I(t −s))ds
2
−1
2σ2
β
1
E2(t)
Z h2
t0
fT2(u)S(t −u)
Z h1
t0
fT1(s)e−µs−µuG(I(t −s −u))dsdu
2#
dt
−σEdwE(t) + σβ
S(t)
E(t)
Z h1
t0
fT1(s)e−µsG(I(t −s))dsdwβ(t)
−σβ
1
E(t)
Z h2
t0
fT2(u)S(t −u)
Z h1
t0
fT1(s)e−µs−µuG(I(t −s −u))dsdudwβ(t),
(3.8)
and
dV3(X(t))
=
1
I(t)dI(t) −1
2
1
I2(t)(dI(t))2
=

β 1
I(t)
Z h2
t0
fT2(u)S(t −u)
Z h1
t0
fT1(s)e−µs−µuG(I(t −s −u))dsdu −(µ + d + α)
−1
2σ2
I −1
2σ2
β
Z h2
t0
fT2(u)S(t −u)
Z h1
t0
fT1(s)e−µs−µuG(I(t −s −u))dsdu
2#
dt
−σIdwI(t) + σβ
1
I(t)
Z h2
t0
fT2(u)S(t −u)
Z h1
t0
fT1(s)e−µs−µuG(I(t −s −u))dsdudwβ(t)
(3.9)


## Page 25


25
It follows from (3.6)-(3.9) that for t < τ+(t),
V (X(t)) −V (X(t0))
≥
Z t
t0

−β
Z h1
t0
fT1(s)e−µsG(I(ξ −s))ds −1
2σ2
S
−1
2σ2
β
Z h1
t0
fT1(s)e−µsG(I(ξ −s))ds
2#
dξ
+
Z t0
t

−β
1
E(ξ)
Z h2
t0
fT2(u)S(ξ −u)
Z h1
t0
fT1(s)e−µs−µuG(I(ξ −s −u))dsdu
−1
2σ2
E −1
2σ2
β
S2(ξ)
E2(ξ)
Z h1
t0
fT1(s)e−µsG(I(ξ −s))ds
2
−1
2σ2
β
1
E2(ξ)
Z h2
t0
fT2(u)S(ξ −u)
Z h1
t0
fT1(s)e−µs−µuG(I(ξ −s −u))dsdu
2#
dξ
+
Z t0
t

−(3µ + d + α) −1
2σ2
I
−1
2σ2
β
Z h2
t0
fT2(u)S(ξ −u)
Z h1
t0
fT1(s)e−µs−µuG(I(ξ −s −u))dsdu
2#
dξ
+
Z t0
t

−σSdwS(ξ) −σβ
Z h1
t0
fT1(s)e−µsG(I(ξ −s))dsdwβ(ξ)

+
Z t0
t

−σEdwE(ξ) + σβ
S(ξ)
E(ξ)
Z h1
t0
fT1(s)e−µsG(I(ξ −s))dsdwβ(ξ)

−
Z t0
t

σβ
1
E(ξ)
Z h2
t0
fT2(u)S(ξ −u)
Z h1
t0
fT1(s)e−µs−µuG(I(ξ −s −u))dsdudwβ(ξ
+
Z t
t0
[−σIdwI(ξ)
+σβ
1
I(ξ)
Z h2
t0
fT2(u)S(ξ −u)
Z h1
t0
fT1(s)e−µs−µuG(I(ξ −s −u))dsdudwβ(ξ)

.
(3.1
Taking the limit on (3.10) as t →τ+(t), it follows from (3.4)-(3.5) that the left-hand side
V (X(t)) −V (X(t0)) ≤−∞. This contradicts the ﬁniteness of the right-handside of the
inequality (3.10). Hence τ+(t) = τe(w) a.s., that is, X(t, w) ∈D(τe).


## Page 26


26
The following shows that τe(w) = ∞. Let k > 0 be a positive integer such that ||⃗ϕ||1 ≤k,
where ⃗ϕ = (ϕ1(t), ϕ2(t), ϕ3(t)) , t ∈(−∞, t0] deﬁned in (2.19), and ||.||1 is the p −sum norm
deﬁned on R3, when p = 1. Deﬁne the stopping time





τk = sup{t ∈[t0, τe) : ||X(s)||1 = S(s) + E(s) + I(s) ≤k, s ∈[t0, t]}
τk(t) = min(t, τk).
(3.11)
It is easy to see that as k →∞, τk increases. Set limk→∞τk(t) = τ∞. Then it follows that
τ∞≤τe a.s. We show in the following that: (1.) τe = τ∞
a.s. ⇔P(τe ̸= τ∞) = 0, (2.)
τ∞= ∞
a.s. ⇔P(τ∞= ∞) = 1.
Suppose on the contrary that P(τ∞< τe) > 0. Let w ∈{τ∞< τe} and t ≤τ∞. Deﬁne





ˆV1(X(t)) = eµt(S(t) + E(t) + I(t)),
∀t ≤τk(t).
(3.12)
The Ito-Doob diﬀerential d ˆV1 of (3.12) with respect to the system (2.15)-(2.18) is given as
follows:
d ˆV1
=
µeµt(S(t) + E(t) + I(t))dt + eµt(dS(t) + dE(t) + dI(t))
(3.13)
=
eµt

B + α
Z ∞
t0
fT3(r)I(t −r)e−µrdr −(α + d)I(t)

dt
−σSeµtS(t)dwS(t) −σEeµtE(t)dwE(t) −σIeµtI(t)dwI(t)
(3.14)
Integrating (3.12) over the interval [t0, τ], and applying some algebraic manipulations and


## Page 27


27
simpliﬁcations it follows that
V1(X(τ))
=
V1(X(t0)) + B
µ
 eµτ −eµt0
+
Z ∞
t0
fT3(r)e−µr
Z t0
t0−r
αI(ξ)dξ −
Z τ
τ−r
αI(ξ)dξ

dr −
Z τ
t0
dI(ξ)dξ
+
Z τ
t0

−σSeµξS(ξ)dwS(ξ) −σEeµξE(ξ)dwE(ξ) −σIeµξI(ξ)dwI(ξ)

(3.15)
Removing negative terms from (3.15), it implies from (2.19) that
V1(X(τ))
≤
V1(X(t0)) + B
µ eµτ
+
Z ∞
t0
fT3(r)e−µr
Z t0
t0−r
αϕ3(ξ)dξ

dr
+
Z τ
t0

−σSeµξS(ξ)dwS(ξ) −σEeµξE(ξ)dwE(ξ) −σIeµξI(ξ)dwI(ξ)

(3.16)
But from (3.12) it is easy to see that for ∀t ≤τk(t),
||X(t)||1 = S(t) + E(t) + I(t) ≤V (X(t)).
(3.17)
Thus setting τ = τk(t), then it follows from (3.11), (3.16) and (3.17) that
k = ||X(τk(t))||1 ≤V1(X(τk(t)))
(3.18)
Taking the limit on (3.18) as k →∞leads to a contradiction because the left-hand-side of
the inequality (3.18) is inﬁnite, but following the right-hand-side from (3.16) leads to a ﬁnite
value. Hence τe = τ∞a.s. The following shows that τe = τ∞= ∞a.s.


## Page 28


28
Let w ∈{τe < ∞}. It follows from (3.15)-(3.16) that
I{τe<∞}V1(X(τ))
≤
I{τe<∞}V1(X(t0)) + I{τe<∞}
B
µ eµτ
+I{τe<∞}
Z ∞
t0
fT3(r)e−µr
Z t0
t0−r
αϕ3(ξ)dξ

dr
+I{τe<∞}
Z τ
t0

−σSeµξS(ξ)dwS(ξ) −σEeµξE(ξ)dwE(ξ) −σIeµξI(ξ)dwI(ξ)

.
(3.19)
Suppose τ = τk(t) ∧T, where T > 0 is arbitrary, then taking the expected value of (3.19)
follows that
E(I{τe<∞}V1(X(τk(t) ∧T))) ≤V1(X(t0)) + B
µ eµT
(3.20)
But from (3.17) it is easy to see that
I{τe<∞,τk(t)≤T}||X(τk(t))||1 ≤I{τe<∞}V1(X(τk(t) ∧T))
(3.21)
It follows from (3.19)-(3.21) and (3.11) that
P({τe < ∞, τk(t) ≤T})k
=
E

I{τe<∞,τk(t)≤T}||X(τk(t))||1

≤
E

I{τe<∞}V1(X(τk(t) ∧T))

≤
V1(X(t0)) + B
µ eµT .
(3.22)
It follows immediately from (3.22) that P({τe < ∞, τ∞≤T}) →0 as k →∞. Furthermore,
since T < ∞is arbitrary, we conclude that P({τe < ∞, τ∞< ∞}) = 0. Finally, by the total


## Page 29


29
probability principle,
P({τe < ∞})
=
P({τe < ∞, τ∞= ∞}) + P({τe < ∞, τ∞< ∞})
≤
P({τe ̸= τ∞}) + P({τe < ∞, τ∞< ∞})
=
0.
(3.23)
Thus from (3.23), τe = τ∞= ∞a.s.. In addition, X(t) ∈D(∞).
Remark 3.1.
1. Theorem 3.2 and Lemma 3.1 signify that the stochastic system (2.15)-(2.18) has a unique
global positive solution process Y (t) ∈R4
+, for all t ∈(−∞, ∞). Furthermore, from Lemma 3.1
it follows that a positive solution of the system that starts in the closed ball centered at the
origin with a radius of B
µ , given by D(∞) = ¯B(−∞,∞)
R4
+,

0, B
µ

, will continue to oscillate in
the closed ball for all time t ≥t0. Hence, the set D(∞) = ¯B(−∞,∞)
R4
+,

0, B
µ

is a positive
self-invariant set for the stochastic system (2.15)-(2.18).
2. Theorem 3.1 and Lemma 3.1 also signify that the deterministic system (2.8)-(2.11) has a
unique global positive solution denoted by Y (t) ∈R4
+, for all t ∈(−∞, ∞). Furthermore,
from Lemma 3.1 it follows that any positive solution of the deterministic system that starts
in the closed ball centered at the origin with a radius of B
µ , given by D(∞) = ¯B(−∞,∞)
R4
+,

0, B
µ

,
grows and becomes bounded as signiﬁed by (3.3), within the closed ball for all time t ≥t0.
Hence, the set D(∞) = ¯B(−∞,∞)
R4
+,

0, B
µ

is a positive self-invariant set for the deterministic
system (2.8)-(2.11).
4. Existence and Asymptotic Behavior of Disease Free Equilibrium
In this section, the existence and the general asymptotic properties of the deterministic
and stochastic systems: (2.8)-(2.11) and (2.15)-(2.18), respectively with respect to the disease
free equilibrium of the systems are investigated. Generally, the equilibria for a deterministic
or stochastic system are obtained by solving a system of algebraic equations obtained via
setting the rate functions of the deterministic system, or the drift and diﬀusion parts of the


## Page 30


30
stochastic system to zero. In the case of a disease free equilibrium, the additional condition
that E = I = R = 0 is utilized in the event when there is no disease in the population. Let
the equilibria of the two delayed systems (2.8)-(2.11) and (2.15)-(2.18) be denoted generally
by E = (S∗, E∗, I∗).
Note that the existence of a disease free steady state solution for the stochastic system
is determined by the intensity values of the white noise processes representing the random
ﬂuctuations in the disease transmission and natural death rates, that is, σi, i = S, E, I, β.
For easy reference, the following result characterizes the existence of the disease-free steady
solution of the systems: (2.8)-(2.11) and (2.15)-(2.18).
Theorem 4.1.
1. There exists a disease-free steady state solution E0 = (S∗
0, 0, 0) for the deterministic system
(2.8)-(2.11), where S∗
0 = B
µ .
2. When σi ≥0, i = E, I, β and σS = 0, there exists a disease-free steady state solution
E0 = (S∗
0, 0, 0), for the stochastic system (2.15)-(2.18), where S∗
0 = B
µ .
3. When σi ≥0, i = E, I, β and σS > 0, the system (2.15)-(2.18) does not have a disease-free
steady state solution.
Proof:
The results follow immediately by applying the method of ﬁnding the equilibria of the system
described above.
Remark 4.1. Theorem 4.1[1.] signiﬁes that the deterministic system (2.8)-(2.11) always
has a disease free equilibrium given by E0. Theorem 4.1[2.] and Theorem 4.1[3.] signify that
regardless of the intensity values σi ≥0, i = E, I, β of the white processes due to random
ﬂuctuations in the natural death rates of the exposed, infectious and removal populations, and
also from the disease transmission rate, there exists a steady state disease-free population E0,
which is exactly the same as that of the deterministic system, provided the intensity value
of the white noise process due to the random ﬂuctuations in the natural death rate of the
susceptible population is equal to zero. That is, σS = 0
These observations suggest that the source- disease transmission or natural death rates,
and also the intensity of the random ﬂuctuations in the system represented by the white noise
processes in the stochastic system (2.15)-(2.18) have bearings on the asymptotic properties


## Page 31


31
of the stochastic system (2.15)-(2.18) with respect to the disease free steady state population
E0. A detailed qualitative study of the behavior of the intensity values σi, i = S, E, I, β of
the white noise processes in the system in relation to the stochastic asymptotic stability of
the disease-free steady state population E0, and with focus on disease eradication from the
system appears in a parallel study by the author. In this section, the primary goal is to gain
complete comparative insight about the general asymptotic properties of the deterministic and
stochastic systems (2.8)-(2.11) and (2.15)-(2.18) including but without limitation to (1) the
importance of the delays in the system, and (2) the asymptotic properties of the two systems
with respect to the disease free equilibrium of the systems.
In the following, the asymptotic stability of the disease free equilibrium, E0, of the deter-
ministic system (2.8)-(2.11) and the stochastic system (2.15)-(2.18), whenever σS = 0 are in-
vestigated. The deterministic and stochastic versions of the Lyapunov functional techniques
[41, 38, 39] are utilized to establish the stability results. In order to study the qualitative
properties of the systems: (2.8)-(2.11) and (2.15)-(2.18) with respect to the equilibrium state
E0 = (S∗
0, 0, 0), S∗
0 = B
µ , ﬁrst the following transformation of the variables of the systems
which shifts the equilibrium states of the systems to the origin is used:
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
U(t)
=
S(t) −S∗
0
V (t)
=
E(t)
W(t)
=
I(t).
(4.1)
By employing the transformation in (4.1) to the system (2.15)-(2.17), the following system


## Page 32


32
is obtained:
dU(t)
=

−βU(t)
Z h1
t0
fT1(s)e−µsG(W(t −s))ds −µU(t) + α
Z ∞
t0
fT3(r)W(t −r)e−µrdr

dt
−σS(S∗
0 + U(t))dwS(t) −σβ(S∗
0 + U(t))
Z h1
t0
fT1(s)e−µsG(W(t −s))dsdwβ(t)
(4.2)
dV (t)
=

β(S∗
0 + U(t))
Z h1
t0
fT1(s)e−µsG(W(t −s))ds −µV (t)
−β
Z h2
t0
fT2(u)(S∗
0 + U(t −u))
Z h1
t0
fT1(s)e−µs−µuG(W(t −s −u))dsdu

dt
−σEV (t)dwE(t) + σβ(S∗
0 + U(t))
Z h1
t0
fT1(s)e−µsG(W(t −s))dsdwβ(t)
−σβ
Z h2
t0
fT2(u)(S∗
0 + U(t −u))
Z h1
t0
fT1(s)e−µs−µuG(W(t −s −u))dsdudwβ(t)
(4.3)
dW(t)
=

β
Z h2
t0
fT2(u)(S∗
0 + U(t −u))
Z h1
t0
fT1(s)e−µs−µuG(W(t −s −u))dsdu −(µ + d + α)W(t)

dt
−σIW(t)dwI(t) + σβ
Z h2
t0
fT2(u)(S∗
0 + U(t −u))
Z h1
t0
fT1(s)e−µs−µuG(W(t −s −u))dsdudwβ(t)
(4.4)
The lemmas that follow in this section will be utilized to establish the asymptotic results for
the system (2.15)-(2.18) with respect to the steady state solution E0. Recall the following
lemma in the earlier study [[42], Lemma 4.1].
Lemma 4.1. Let V1 ∈C2,1(R3 × R+, R+), deﬁned by
V1(x, t)
=
(S(t) −S∗+ E(t))2 + c(E(t))2 + (I(t))2
(4.5)
x(t)
=
(S(t) −S∗, E(t), I(t))T,
(4.6)
where c is a positive constant. There exists two increasing positive real valued functions φ1,
and φ2, such that V1 satisﬁes the inequality
φ1(||x||)
≤
V1(x, (t)) ≤φ2(||x||).
(4.7)
Proof:


## Page 33


33
The result follows directly from Lemma 4.1 in [42].
Lemma 4.2. Let the hypothesis of Theorem 3.2 be satisﬁed. The diﬀerential operator[42,
41] applied to the Lyapunov function V1 in (4.6) with respect to the system of stochastic
diﬀerential equation (2.15)-(2.18) is given by
dV1 = LV1dt −2σS(U(t) + V (t))(S∗
0 + U(t))dwS(t)
−2σE(U(t)V (t) + (c + 1)V 2(t))dwE(t) −2σIW 2(t))dwI(t)
−2cσβ(S∗
0 + U(t))V (t)
Z h1
t0
fT1(s)e−µsG(W(t −s))dsdwβ
−2σE[U(t) + (c + 1)V (t) + W(t)] ×
×
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(S∗
0 + U(t −u))G(W(t −s −u))dsdudwβ(t) (4.8)
where for some positive valued function ˜K(µ) that depends on µ, the drift part LV1 of dV1
in (4.8), satisﬁes the inequality
LV1(x, t)
≤
(2βS∗
0 + β + α + 2
µ
˜K(µ)2 −2µ)U2(t)
+
h
2µ ˜K(µ)2 + α + β(2S∗
0 + 1) + cβ(3S∗
0 + 1) −2(1 + c)µ
i
V 2(t)
+2[βS∗
0 −(µ + d + α)]W 2(t)
+2α
Z ∞
t0
fT3(r)e−2µrW 2(t −r)dr
+[2βS∗
0 (1 + c) + σ2
β(S∗
0)2(4c + 2(1 −c)2)]
Z h1
t0
fT1(s)e−2µsG2(W(t −s))ds
+

βS∗
0(4 + c) + β(S∗
0)2(2 + c) + σ2
β(S∗
0)2(4c + 10)

×
×
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)G2(W(t −s −u))dsdu
+σ2
S (S∗
0 + U(t))2 + σ2
E(c + 1)V 2(t) + σ2
IW 2(t),
(4.9)
Proof:
The computation of the drift part LV [41, 39] of the diﬀerential operator dV applied to the
Lyapunov function V1 in (4.6) with respect to the system of stochastic diﬀerential equation


## Page 34


34
(2.15)-(2.18) gives the following:
LV1(x, t)
=
−4µU(t)V (t) −2µU2(t) −2(1 + c)µV 2(t) −2(µ + d + α)W 2(t)
+2α(U(t) + V (t))
Z ∞
t0
fT3(r)e−µrW(t −r)dr
+2β [S∗
0U(t) + (1 + c)S∗
0V (t) + cV (t)U(t)]
Z h1
t0
fT1(s)e−µsG(W(t −s))ds
−2β [U(t) + (1 + c)V (t) −W(t)] ×
×
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(S∗
0 + U(t −u))G(W(t −s −u))dsdu
+σ2
βc (S∗
0 + U(t))2
Z h1
t0
fT1(s)e−µsG(W(t −s))ds
2
+σ2
β(c + 2)
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(S∗
0 + U(t −u))G(W(t −s −u))dsdu
2
+σ2
β(1 −c) (S∗
0 + U(t))
Z h1
t0
fT1(s)e−µsG(W(t −s))ds

×
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(S∗
0 + U(t −u))G(W(t −s −u))dsdu

+σ2
S (S∗
0 + U(t))2 + σ2
E(c + 1)V 2(t) + σ2
EW 2(t).
(4.10)
Applying Theorem 3.2, Cauchy −Swartz, H¨older inequalities, and the following algebraic
inequality
2ab ≤a2
g(c) + b2g(c)
(4.11)
where a, b, c ∈R, and the function g is such that g(c) > 0, to estimate the terms with integral
signs in (4.10), one can see the following:
2α(U(t)+V (t))
Z ∞
t0
fT3(r)e−µrW(t−r)dr ≤αU2(t)+αV 2(t)+2α
Z ∞
t0
fT3(r)e−2µrW 2(t−r)dr.
(4.12)


## Page 35


35
2β [S∗
0U(t) + (1 + c)S∗
0V (t) + cV (t)U(t)]
Z h1
t0
fT1(s)e−µsG(W(t −s))ds
≤βS∗
0U2(t) + βS∗
0 (1 + 2c) V 2(t) + 2βS∗
0 (1 + c)
Z h1
t0
fT1(s)e−2µsG2(W(t −s))ds
(4.13)
−2β [U(t) + (1 + c)V (t) −W(t)] ×
×
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(S∗
0 + U(t −u))G(W(t −s −u))dsdu
≤β(S∗
0 + 1)U2(t) + (1 + c)β(S∗
0 + 1)V 2(t) + 2βS∗
0W 2(t)
+

βS∗
0(4 + c) + β(S∗
0)2(2 + c)
 Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)G2(W(t −s −u))dsdu.
(4.14)
σ2
βc (S∗
0 + U(t))2
Z h1
t0
fT1(s)e−µsG(W(t −s))ds
2
≤4cσ2
β(S∗
0)2
Z h1
t0
fT1(s)e−2µsG2(W(t −s))ds
(4.15)
σ2
β(c + 2)
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(S∗
0 + U(t −u))G(W(t −s −u))dsdu
2
≤4(c + 2)σ2
β(S∗
0)2
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)G2(W(t −s −u))dsdu.
(4.16)


## Page 36


36
σ2
β(1 −c) (S∗
0 + U(t))
Z h1
t0
fT1(s)e−µsG(W(t −s))ds

×
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(S∗
0 + U(t −u))G(W(t −s −u))dsdu

≤2σ2
β(1 −c)2(S∗
0)2
Z h1
t0
fT1(s)e−2µsG2(W(t −s))ds
+2σ2
β(S∗
0)2
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)G2(W(t −s −u))dsdu.
(4.17)
The result (4.9) follows from (4.12)-(4.17) and the inequality (4.11) that (4.10) becomes
LV1(x, t)
≤
(2βS∗
0 + β + α + 2
µ
˜K(µ)2 −2µ)U2(t)
+
h
2µ ˜K(µ)2 + α + β(2S∗
0 + 1) + cβ(3S∗
0 + 1) −2(1 + c)µ
i
V 2(t)
+2[βS∗
0 −(µ + d + α)]W 2(t)
+2α
Z ∞
t0
fT3(r)e−2µrW 2(t −r)dr
+[2βS∗
0 (1 + c) + σ2
β(S∗
0)2(4c + 2(1 −c)2)]
Z h1
t0
fT1(s)e−2µsG2(W(t −s))ds
+

βS∗
0(4 + c) + β(S∗
0)2(2 + c) + σ2
β(S∗
0)2(4c + 10)

×
×
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)G2(W(t −s −u))dsdu
+σ2
S (S∗
0 + U(t))2 + σ2
E(c + 1)V 2(t) + σ2
EW 2(t),
(4.18)
where ˜K(µ) = g(µ) and g is deﬁned in (4.11).
The following set of lemmas characterize the stochastic asymptotic stability of the disease
free equilibrium E0 of the system (2.15)-(2.18) when the intensity value of the white noise
process due to the natural death rate µ in the susceptible population is zero, that is, when
σS = 0. Lemma 4.3 presents the stochastic stability results for the case of constant and


## Page 37


37
ﬁnite delays in the system, and Lemma 4.4 presents stability results for arbitrary random
ﬁnite and inﬁnite delays in the system.
It is noted that the assumption of constant delay times representing the incubation period
of the disease in the vector, T1, incubation period of the disease in the host, T2, and immunity
period of the disease in the human population, T3 is equivalent to the special case of letting
the probability density functions fTi, i = 1, 2, 3 of the random variables T1, T2 and T3 be the
dirac-delta function. That is,
fTi(s) = δ(s −Ti) =





+∞, s = Ti,
0, otherwise,
, i = 1, 2, 3.
(4.19)
Moreover, under the assumption that T1 ≥0, T2 ≥0 and T3 ≥0 are constant, the fol-
lowing expectations can be written as E(e−2µ(T1+T2)) = e−2µ(T1+T2), E(e−2µT1) = e−2µT1 and
E(e−2µT3) = e−2µT3.
Lemma 4.3. Let the hypotheses of Theorem 3.2, Theorem 4.1[2.] and Lemma 4.2 be satis-
ﬁed. Also, let T1, T2 and T3 be constant positive values. There exists a Lyapunov functional
V = V1 + V12,
(4.20)
where V1 ∈C2,1(R3 × R+, R+) is deﬁned by (4.6) and V12 is deﬁned as follows:
V12(x, t) = 2αe−2µT3
Z t
t−r
I2(v)dv
+[2βS∗
0 (1 + c) + σ2
β(S∗
0)2(4c + 2(1 −c)2)]e−2µT1
Z t
t−s
G2(I(v))dv
+

βS∗
0(4 + c) + β(S∗
0)2(2 + c) + σ2
β(S∗
0)2(4c + 10)

e−2µ(T1+T2)
Z t
t−(T1+T2)
G2(I(v))dv
(4.21)


## Page 38


38
Furthermore, there exists threshold values R∗
1, R∗
0, U0 and V0 deﬁned as follows:
R∗
1 = βS∗
0 ˆK∗
1 + α
(µ + d + α),
(4.22)
R∗
0 = βS∗
0 + 1
2σ2
I
(µ + d + α),
(4.23)
U0 =
2βS∗
0 + β + α + 2
µ
˜
K(µ)2
2µ
,
(4.24)
and
V0 = (2µ ˜K(µ)2 + α + β(2S∗
0 + 1) + σ2
E)
2µ
,
(4.25)
with some constant ˆK∗
1 > 0 that depends on S∗
0 and σβ (in fact, ˆK∗
1 = 4 + 6 1
βσ2
βS∗
0), and
some positive constants φ, ψ, and ϕ, such that, under the assumptions that R∗
0 < 1, U0 ≤1,
and V0 ≤1, and
Tmax ≥1
2µ log
R∗
1
1 −R∗
0
,
(4.26)
where
Tmax = max (T1 + T2, T3),
(4.27)
the drift part LV of the diﬀerential operator dV applied to V with respect to the stochastic
dynamic system (2.15)-(2.18) satisﬁes the following inequality:
LV (x, t) ≤−
 φU2(t) + ψV 2(t) + ϕW 2(t)

.
(4.28)
Proof:
By applying the translation properties of the Dirac-Delata function (4.19), it can be seen from
Lemma 4.2 that the drift part LV of the diﬀerential operator dV applied to the Lyapunov
functional deﬁned in (4.20), (4.6) and (4.21) with respect to system (2.15)-(2.18) leads to


## Page 39


39
the following:
LV (x, t)
=
LV1(x, t)
+2αe−2µT3W 2(t)
+[2βS∗
0 (1 + c) + σ2
β(S∗
0)2(4c + 2(1 −c)2)]e−2µT1G2(W(t))
+

βS∗
0(4 + c) + β(S∗
0)2(2 + c) + σ2
β(S∗
0)2(4c + 10)

e−2µ(T1+T2)G2(W(t))
−2αe−2µT3W 2(t −T3)
−[2βS∗
0 (1 + c) + σ2
β(S∗
0)2(4c + 2(1 −c)2)]e−2µT1G2(W(t −T1))
−

βS∗
0(4 + c) + β(S∗
0)2(2 + c) + σ2
β(S∗
0)2(4c + 10)

×
×e−2µ(T1+T2)G2(W(t −T1 −T2)).
(4.29)
It follows that under the assumptions for σi, i = S, E, I, β in Theorem 4.1[2.], and for some
suitable choice of the positive constant c, it is easy to see from (4.9), (4.29), the statements
of Assumption 2.1, A5 (i.e. G2(x) ≤x2, x ≥0) and some further algebraic manipulations
and simpliﬁcations that
LV (x, t) ≤−
 φU2(t) + ψV 2(t) + ϕW 2(t)

,
(4.30)


## Page 40


40
where,
φ
=
2µ(1 −U0)
(4.31)
ψ
=
2µ(1 −V0) −2µc

1 −β(3S∗
0 + 1) + σ2
E
2µ

(4.32)
ϕ
=
2(µ + d + α) −

2βS∗
0 + σ2
I + 2αe−2µT3 + 2
 βS∗
0 + σ2
β(S∗
0)2
e−2µT3
+
 4βS∗
0 + 2β(S∗
0)2 + 10σ2
β(S∗
0)2
e−2µ(T1+T2)
−c(3βS∗
0 + β(S∗
0)2 + 4σ2
β(S∗
0)2)
−2c2σ2
β(S∗
0)2,
≥
2(µ + d + α)

1 −R∗
0 −R∗
1e−2µTmax
−c(3βS∗
0 + β(S∗
0)2 + 4σ2
β(S∗
0)2)
−2c2σ2
β(S∗
0)2.
(4.33)
and R∗
0 and R∗
1 are deﬁned in (4.22)-(4.23). It is now easy to see that under the assumptions
of R∗
0, R∗
1, U0, and V0 in the hypothesis and also for a suitable choice of the positive constant
c it follows that φ, ψ, and ϕ are positive constants and (4.28) follows immediately.
The following result describes the stochastic asymptotic stability of the disease free equi-
librium E0, whenever it exists and the delays in the stochastic system are constant.
Theorem 4.2. Suppose Theorem 4.1[2.] and the hypotheses of Lemma 4.2 and Lemma 4.3
are satisﬁed, then the disease free equilibrium E0 of the stochastic dynamic system (2.15)-
(2.18) is stochastically asymptotically stable in the large in the set D(∞). Moreover, the
steady state solution E0 is exponentially mean square stable.
Proof:
The result follows by applying the comparison stability results[43, 39]. Moreover, the disease
free equilibrium state is exponentially mean square stable.
The following result for the deterministic system (2.8)-(2.11) will be useful to compare
and obtain insight about the inﬂuence of the noise and delays in the stochastic system
(2.15)-(2.18), whenever the delays Ti, i = 1, 2, 3 in both systems are constant.


## Page 41


41
Theorem 4.3. Let the hypotheses of Theorem 3.2, Theorem 4.1[1.] and Lemma 4.2 be sat-
isﬁed. Also, let T1, T2 and T3 be constant positive values. There exists a Lyapunov functional
V = V1 + V13,
(4.34)
where V1 ∈C2,1(R3 × R+, R+) is deﬁned by (4.6) and V13 is deﬁned as follows:
V13(x, t) = 2αe−2µT3
Z t
t−r
I2(v)dv
+[2βS∗
0 (1 + c)]e−2µT1
Z t
t−s
G2(I(v))dv
+

βS∗
0(4 + c) + β(S∗
0)2(2 + c)

e−2µ(T1+T2)
Z t
t−(T1+T2)
G2(I(v))dv
(4.35)
Furthermore, there exists threshold values ˆR∗
1, ˆR∗
0, ˆU0 and ˆV0 deﬁned as follows:
ˆR∗
1 = βS∗
0 ˆK∗
0 + α
(µ + d + α),
(4.36)
ˆR∗
0 =
βS∗
0
(µ + d + α),
(4.37)
ˆU0 =
2βS∗
0 + β + α + 2
µ
˜
K(µ)2
2µ
,
(4.38)
and
ˆV0 = (2µ ˜K(µ)2 + α + β(2S∗
0 + 1))
2µ
,
(4.39)
with some constant ˆK∗
0 > 0 (in fact, ˆK∗
1 = 4), and some positive constants φ, ψ, and ϕ, such
that, under the assumptions that ˆR∗
0 < 1, ˆU0 ≤1, and ˆV0 ≤1, and
Tmax ≥1
2µ log
ˆR∗
1
1 −ˆR∗
0
,
(4.40)
where
Tmax = max (T1 + T2, T3),
(4.41)
the deterministic diﬀerential operator ˙V applied to V with respect to the deterministic dy-


## Page 42


42
namic system (2.8)-(2.11) satisﬁes the following inequality:
˙V (x, t) ≤−min (φ, ψ, ϕ)||X(t) −E0||2,
(4.42)
where X(t) is deﬁned in (2.21), and ||.|| is the natural Euclidean norm on R2.
Furthermore, the disease free steady state E0 is globally uniformly asymptotically stable
in D(∞). Moreover, it is exponentially stable.
Proof:
The results follow directly from Lemma 4.22, where for the intensities σi = 0, i = 1, 2, 3, it is
easily seen that when the assumptions in the hypothesis of Theorem 4.3 are satisﬁed, then
˙V (x, t) ≤−
 φU2(t) + ψV 2(t) + ϕW 2(t)

,
(4.43)
where φ, ψ, and ϕ (with σi = 0, i = 1, 2, 3 ) are deﬁned in (4.31)-(4.33). The result in
(4.42) follows immediately from (4.43). Furthermore, the rest of the stability results follow
by applying the comparison results in [56, 57, 40].
Remark 4.2.
1. Theorem 4.2 signiﬁes that in the absence of the white noise process in the system due to
the random ﬂuctuations from the natural death rate in the susceptible population, that is,
σS = 0, it follows that regardless of (1.) the variability in the natural death of the exposed,
infectious, and the removal populations, that is, σ2
i ≥0, i = E, I, R,, or (2.) the variability
in the disease transmission process, that is, σ2
β ≥0, or (3.) the value of the incubation
delay of the disease in the vector and in the human being (T1 and T2 respectively), or the
value of the delay of the natural immunity period T3, a disease free steady state E0 for
the population exists. Furthermore, the disease free steady state E0 for the population is
stochastically asymptotically stable in the large, whenever the threshold conditions: R∗
0 < 1,
U0 ≤1, V0 ≤1, and Tmax ≥
1
2µ log
R∗
1
1−R∗
0 are satisﬁed, where R∗
0, R∗
1, U0, V0, Tmax are deﬁned
in (4.22)-(4.27).
It should also be noted that the threshold values R∗
0, U0, and V0 are explicit in terms of the
parameters of the system (2.15)-(2.18) and also computationally attractive, whenever speciﬁc
values for the parameters of the system are given. This observation suggests that in a disease
scenario where there are no random ﬂuctuations in the natural death of susceptible individuals
in the population, that is, σS = 0, the stochastic dynamic system (2.15)-(2.18) exhibits a


## Page 43


43
disease free steady state for the population, regardless of whether there is (1.) signiﬁcant
variability in the disease transmission, that is, σ2
β ≥0, or (2.) signiﬁcant variability in the
natural death of the other states- E, I, R, that is, σ2
i ≥0, i = E, I, R. Furthermore, the
disease can be eradicated from the system (2.15)-(2.18), whenever the threshold conditions
R∗
0 < 1, U0 ≤1, V0 ≤1, and Tmax ≥
1
2µ log
R∗
1
1−R∗
0 are satisﬁed. In addition, it is noted that
the disease eradication is restricted by the values of the incubation and natural immunity
periods in the system, that is, Tmax ≥
1
2µ log
R∗
1
1−R∗
0 . This result is of signiﬁcance to policy
decisions related to malaria eradication from the human population noting that either the
total incubation phase of the plasmodium in the vector and human hosts (lasting for T1 + T2
time units) or the period of eﬀective immunity against malaria (T3) is delayed for at least
1
2µ log
R∗
1
1−R∗
0 time units, provided the other conditions R∗
0 < 1, U0 ≤1, V0 ≤1 hold.
2. Since the threshold conditions, that is, R∗
0 < 1, U0 ≤1, V0 ≤1, and Tmax ≥
1
2µ log
R∗
1
1−R∗
0 are
suﬃcient for the disease free steady state population, E0, to be stochastically asymptotically
stable in the large, and consequently for the eradication of the disease from the population, the
threshold value R∗
0 is the noise-modiﬁed basic reproduction number for the disease dynamics
described by stochastic system (2.15)-(2.18), whenever the following assumptions:- (1) that
σi ≥0, i = E, I, R, β, and σS = 0, and also (2) that the incubation and natural immunity
delays T1, T2 and T3 are constant.
3. The results in Theorem 4.3 in comparison to results in Theorem 4.2 exhibit the combined
eﬀects of the delays and the noise from the disease transmission and natural death rates on
the dynamics of the disease.
Indeed, the threshold value ˆR∗
0 =
βS∗
0
(µ+d+α) from (4.37), represents the total number of
infectious cases that result from one malaria infectious person present in a completely disease
free population with state given by S∗
0 = B
µ , over the average lifetime given by
1
(µ+d+α) of a
person who has survived from disease related death d, natural death µ and recovered at rate
α from infection.
Hence, ˆR∗
0 is the noise-free basic reproduction number of the disease,
whenever the incubation periods of the malaria parasite inside the human and mosquito
hosts given by Ti, i = 1, 2, and also the period of eﬀective natural immunity against malaria
given by T3, are all positive constants. Furthermore, the threshold condition ˆR∗
0 < 1 from
Theorem 4.3 is required for the disease to be eradicated from the human population.
Comparing the delay threshold conditions from (4.26) and (4.40), and the other threshold
values from Theorem 4.3 and Theorem 4.2, it can be seen that
Tmax ≥1
2µ log
R∗
1
1 −R∗
0
> 1
2µ log
ˆR∗
1
1 −ˆR∗
0
,
(4.44)
R∗
0 > ˆR∗
0, U0 = ˆU0 and V0 > ˆV0, whenever σi > 0, i = E, I, R, β. This observation suggests
clearly that the intensities σi, i = S, E, I, R, β of the white noise processes in the system from
the natural and disease transmission rates exhibit bearings on the stability of the disease


## Page 44


44
free equilibrium E0, and hence on disease eradication. Furthermore, in the event where the
disease free equilibrium E0 is stable for both deterministic and stochastic systems (2.8)-(2.11)
and (2.15)-(2.18), that is, when (4.44) and 1 > R∗
0 > ˆR∗
0, 1 ≥U0 = ˆU0 and 1 ≥V0 > ˆV0,
it can be seen easily that for higher intensity values for σi > 0, i = E, I, R, β, the following
hold: 1 > R∗
0 ≫ˆR∗
0, 1 ≥U0 = ˆU0, 1 ≥V0 ≫ˆV0 and
Tmax ≥1
2µ log
R∗
1
1 −R∗
0
≫1
2µ log
ˆR∗
1
1 −ˆR∗
0
.
(4.45)
Therefore, it is evident that the presence of random ﬂuctuations in the disease dynamics from
the disease transmission and natural death rates negatively impact the disease eradication
process by setting higher bounds for the threshold values that are suﬃcient for the stability
of the disease free population steady state E0. In addition, since in most malaria endemic
regions, the natural immunity period T3 is often longer than the combined duration T1 +T2 of
incubation of the malaria parasite inside the mosquito and human hosts, so that from (4.41),
Tmax = T3, the result in (4.45) shows that the occurrence of the white noise processes in the
system, and especially with high intensity values, potentially sets unrealistic bounds for the
natural immunity period in the human population needed for the disease to be eradicated.
Thus, malaria eradication policies must make eﬀorts to reduce the intensities of the ran-
dom ﬂuctuation in the disease transmission and natural death rates, perhaps via better care
of the people in malaria endemic zones, and application of eﬀective vector control strategies
or measures.
Lemma 4.4. Let the hypotheses of Theorem 3.2, Theorem 4.1[2.] and Lemma 4.2 be satis-
ﬁed. And let fTi, i = 1, 2, 3 be the arbitrary density functions of the random variables T1, T2
and T3. There exists a Lyapunov functional
V = V1 + V22,
(4.46)


## Page 45


45
where V1 ∈C2,1(R3 × R+, R+) is deﬁned by (4.6) and V22 is deﬁned as follows:
V22(x, t) = 2α
Z ∞
t0
fT3(r)e−2µr
Z t
t−r
I2(v)dvdr
+[2βS∗
0 (1 + c) + σ2
β(S∗
0)2(4c + 2(1 −c)2)]
Z h1
t0
fT1(s)e−2µs
Z t
t−s
G2(I(v))dvds
+

βS∗
0(4 + c) + β(S∗
0)2(2 + c) + σ2
β(S∗
0)2(4c + 10)

×
×
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)
Z t
t−u
G2(I(v −s))dvdsdu
+
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)
Z t
t−s
G2(I(v))dvdsdu

(4.47)
Furthermore, there exists threshold values R1, U0 and V0 deﬁned as follows:
R1 = βS∗
0 ˆK1 + α + 1
2σ2
I
(µ + d + α)
,
(4.48)
U0 =
2βS∗
0 + β + α + 2
µ
˜
K(µ)2
2µ
,
(4.49)
and
V0 = (2µ ˜K(µ)2 + α + β(2S∗
0 + 1) + σ2
E)
2µ
,
(4.50)
with some constant ˆK1 > 0 that depends on S∗
0 and σβ (in fact, ˆK1 = 4 + S∗
0 + 6 1
βσ2
βS∗
0), and
some positive constants φ, ψ, and ϕ, such that, under the assumptions that R1 ≤1, U0 ≤1,
and V0 ≤1, the drift part LV of the diﬀerential operator dV applied to V with respect to the
stochastic dynamic system (2.15)-(2.18) satisﬁes the following inequality:
LV (x, t) ≤−
 φU2(t) + ψV 2(t) + ϕW 2(t)

.
(4.51)
Proof:
The drift part LV of the diﬀerential operator dV applied to the Lyapunov functional deﬁned


## Page 46


46
in (4.46), (4.6) and (4.47) with respect to system (2.15)-(2.18) leads to the following:
LV (x, t)
=
LV1(x, t)
+2α
Z ∞
t0
fT3(r)e−2µrW 2(t)dr
+[2βS∗
0 (1 + c) + σ2
β(S∗
0)2(4c + 2(1 −c)2)]
Z h1
t0
fT1(s)e−2µsG2(W(t))ds
+

βS∗
0(4 + c) + β(S∗
0)2(2 + c) + σ2
β(S∗
0)2(4c + 10)

×
×
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)G2(W(t))dsdu
−2α
Z ∞
t0
fT3(r)e−2µrW 2(t −r)dr
−[2βS∗
0 (1 + c) + σ2
β(S∗
0)2(4c + 2(1 −c)2)]
Z h1
t0
fT1(s)e−2µsG2(W(t −s))ds
−

βS∗
0(4 + c) + β(S∗
0)2(2 + c) + σ2
β(S∗
0)2(4c + 10)

×
×
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)G2(W(t −s −u))dsdu.
(4.52)
Under the assumptions for σi, i = S, E, I, β in Theorem 4.1[2.], and for some suitable choice
of the positive constant c, it follows from (4.9), (4.52), the statements of Assumption 2.1, A5
(i.e. G2(x) ≤x2, x ≥0) and some further algebraic manipulations and simpliﬁcations that
LV (x, t) ≤−
 φU2(t) + ψV 2(t) + ϕW 2(t)

,
(4.53)


## Page 47


47
where,
φ
=
2µ(1 −U0)
(4.54)
ψ
=
2µ(1 −V0) −2µc

1 −β(3S∗
0 + 1) + σ2
E
2µ

(4.55)
ϕ
=
2(µ + d + α)(1 −R1) −c(3βS∗
0 + β(S∗
0)2 + 4σ2
β(S∗
0)2) −2c2σ2
β(S∗
0)2.
(4.56)
where R1 is deﬁned in (4.48). In addition, under the assumptions of R1, U0, and V0 in the
hypothesis and for a suitable choice of the positive constant c it follows that φ, ψ, and ϕ
are positive constants and (4.51) follows immediately. The following result describes the
stochastic asymptotic stability of the disease free equilibrium E0, whenever it exists.
Theorem 4.4. Suppose Theorem 4.1[2.] and the hypotheses of Lemma 4.1 and Lemma 4.4
are satisﬁed, then the disease free equilibrium E0 of the stochastic dynamic system (2.15)-
(2.18) is stochastically asymptotically stable in the large in the set D(∞). Moreover, the
steady state solution E0 is exponentially mean square stable.
Proof
The result follows by applying the comparison stability results[43, 39]. Moreover, the disease
free equilibrium state is exponentially mean square stable.
Remark 4.3.
1. Theorem 4.4 signiﬁes that in the absence of the white noise process in the system due to the
random ﬂuctuations in the natural death rate of the susceptible population, that is, σS = 0, it
follows that regardless of (1.) the variability in the natural death of the exposed, infectious,
and the removal populations, that is, σ2
i ≥0, i = E, I, R,, or (2.) the variability in the disease
transmission rate, that is, σ2
β ≥0, or (3.) the variability of the incubation delay of the disease
in the vector and in the human being (T1 and T2 respectively), or (4.) the variability of the
natural immunity period T3, a stochastically asymptotically stable in the large disease free
steady state E0 for the population exists, whenever the threshold conditions: R1 ≤1, U0 ≤1,
and V0 ≤1 are satisﬁed, where R1, U0, and V0 are deﬁned in (4.48)-(4.50). It should be
noted that the threshold values R1, U0, and V0 are explicit in terms of the parameters of
the system (2.15)-(2.18) and also computationally attractive, whenever speciﬁc values for
the parameters of the system are given. This observation suggests that in a disease scenario


## Page 48


48
where there are no random ﬂuctuations in the natural death rate of susceptible individuals
in the population, that is, σS = 0, the stochastic dynamic system (2.15)-(2.18) exhibits a
disease free steady state for the population, regardless of whether there is (1.) a signiﬁcant
variability in the disease transmission rate, that is, σ2
β ≥0, or (2.) a signiﬁcant variability
in the natural death rates of the other states- E, I, R, that is, σ2
i ≥0, i = E, I, R or (3.) a
signiﬁcant variability in the delay periods in the system- T1, T2 and T3. Moreover, the disease
can be eradicated from the system (2.15)-(2.18), whenever the threshold conditions R1 ≤1,
U0 ≤1, and V0 ≤1 are satisﬁed. Furthermore, unlike in the case of constant delays in
the system noted in Remark 4.2, the threshold conditions in Theorem 4.4 provide stronger
bases for policy decisions related to malaria eradication with no additional restrictions to the
average lengths of the incubation and natural immunity periods in the system.
2. Since the threshold conditions, that is, R1 ≤1, U0 ≤1, and V0 ≤1, are suﬃcient for
the disease free steady state population, E0, to be stochastically asymptotically stable in the
large, and consequently for the eradication of the disease from the population, it follows
that the threshold value R1 is the noise-modiﬁed basic reproduction number for the disease
dynamics described by stochastic system (2.15)-(2.18), whenever the assumptions:- σ2
i ≥
0, i = E, I, R, β and σ2
S = 0 are satisﬁed.
The following result characterizes the stability of the disease free equilibrium of the deter-
ministic system (2.8)-(2.11). The deterministic version of the Lyapunov functional technique
is used to establish the results.
Theorem 4.5. Let the hypotheses of Theorem 3.1, Theorem 4.1[1.]
and Lemma 4.2 be
satisﬁed. And let fTi, i = 1, 2, 3 be the arbitrary density functions of the random variables
T1, T2 and T3. There exists a Lyapunov functional
V = V1 + V32,
(4.57)


## Page 49


49
where V1 ∈C2,1(R3 × R+, R+) is deﬁned by (4.6) and V32 is deﬁned as follows:
V32(x, t) = 2α
Z ∞
t0
fT3(r)e−2µr
Z t
t−r
I2(v)dvdr
+[2βS∗
0 (1 + c)]
Z h1
t0
fT1(s)e−2µs
Z t
t−s
G2(I(v))dvds
+

βS∗
0(4 + c) + β(S∗
0)2(2 + c)

×
×
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)
Z t
t−u
G2(I(v −s))dvdsdu
+
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)
Z t
t−s
G2(I(v))dvdsdu

.
(4.58)
Furthermore, deﬁne R0, U0 and V0, as follows:
R0 = βS∗
0 ˆK0 + α
(µ + d + α),
(4.59)
ˆU0 =
2βS∗
0 + β + α + 2
µ
˜
K(µ)2
2µ
,
(4.60)
and
ˆV0 = (2µ ˜K(µ)2 + α + β(2S∗
0 + 1))
2µ
,
(4.61)
where, ˆK0 > 0 is a constant that depends only on S∗
0 (in fact, ˆK0 = 4 + S∗
0). Assume that
R0 ≤1, ˆU0 ≤1, and ˆV0 ≤1, then there exist positive constants φ1, ψ1, and ϕ1, such that
the diﬀerential operator ˙V applied to V with respect to the deterministic system (2.8)-(2.11)
satisﬁes the following diﬀerential inequality:
˙V (x, t) ≤−min (φ1, ψ1, ϕ1)||X(t) −E0||2,
(4.62)
where X(t) is deﬁned in (2.21), and ||.|| is the natural Euclidean norm on R2.
Moreover, under the assumptions in the hypothesis of Theorem 4.1[1.], the disease free
equilibrium E0 of the resulting system (2.15)-(2.18) is uniformly globally asymptotically stable
in the set D(∞).
Proof:
The result follows directly from the proofs of Lemma 4.2 and Lemma 4.4 by setting σi =


## Page 50


50
0, i = S, E, I, β, and also applying the comparison stability results in [44, 41], where from
(4.54)-(4.56), φ1 = φ > 0, ψ1 = ψ > 0, and ϕ1 = ϕ > 0.
Remark 4.4.
1. Theorem 4.5 signiﬁes that in the absence of random ﬂuctuations in the disease dynamics
leading to variability in any of the parameters of the system- natural death or disease trans-
mission rates, the system (2.8)-(2.11) has a disease free steady state, E0, which is globally
uniformly and asymptotically stable under the threshold conditions R0 ≤1, ˆU0 ≤1 and
ˆV0 ≤1, where the threshold values R0, ˆU0 and ˆV0 are deﬁned in (4.59)-(4.61).
It should also be noted that the threshold values R0, ˆU0 and ˆV0 are explicit in terms
of the parameters of the system (2.8)-(2.11) and also computationally attractive, whenever
speciﬁc values for the parameters of the system are given. This observation suggests that in
a disease scenario, where there are no random ﬂuctuations in the disease dynamics owing
to the disease transmission or natural death rates in the dynamic system (2.8)-(2.11), the
system has a disease free steady state, E0, for the population. In addition, if the threshold
values R0, ˆU0 and ˆV0 satisfy the conditions R0 ≤1, ˆU0 ≤1 and ˆV0 ≤1, then the disease can
be eradicated from the population.
2 Furthermore, comparing the threshold values for Theorem 4.5 and Theorem 4.4 deﬁned in
(4.59)-(4.61) and (4.48)-(4.50) respectively, it is easy to see that R0 ≤R1, U0 = ˆU0 and
ˆV0 ≤V0, whenever the intensity values of the white noise processes in the system (2.15)-
(2.18) satisfy the following conditions: σi > 0, i = E, I, β and σS = 0. It is easy to see that
the intensity values σi > 0, i = E, I, R, β of the corresponding white noise processes owning
to the disease transmission and natural death rates of the exposed, infections and removal
individuals in the stochastic dynamic system (2.15)-(2.18) exert constraints on the threshold
values: R1, U0, and V0, deﬁned in (4.48)-(4.50), than on the set of threshold values R0, ˆU0
and ˆV0 deﬁned in (4.59)-(4.61). Moreover, the threshold values- R0, ˆU0 and ˆV0 from (4.59)-
(4.61) attain the threshold condition of ”less than the bound 1” more rapidly compared to
the set of threshold values R1, U0, and V0 from (4.48)-(4.50), whenever the intensity values
σi > 0, i = E, I, R, β. Consequently, the disease would be eradicated more rapidly in a disease
scenario where the disease dynamics is driven by parameters that lead to the set of threshold
values R0, ˆU0 and ˆV0, and eradicated less rapidly in a disease scenario where the driving
parameters of the disease dynamics lead to the threshold values R1, U0, and V0 which depend
on σi > 0, i = E, I, β.
This observation suggests that the occurrence of random ﬂuctuations (in the disease trans-
mission and natural death rates) with signiﬁcant large intensity values in the disease dynam-
ics exert counter positive eﬀects against the disease eradication process. Furthermore, the
intensity levels of the random ﬂuctuations in the disease dynamics expressed in terms of the
sizes of the intensity values, σi, i = E, I, R, β, of the white noise processes in the stochas-
tic system (2.15)-(2.18), reﬂect the weight of the counter positive eﬀects exerted against the


## Page 51


51
disease eradication process. Therefore, good malaria eradication policies should embark on
controlling the intensities of the random ﬂuctuations of malaria transmission and natural
death rates of people who are infected (E, I). Perhaps this can be achieved by controlling the
mosquito populations, and better care of people who are infected with the malaria parasite.
3. The threshold conditions, that is, R0 ≤1, ˆU0 ≤1, and ˆV0 ≤1, are suﬃcient for the
existence of a globally uniformly asymptotically stable disease free steady state population,
E0 in the deterministic system (2.8)-(2.11). Furthermore, these conditions are suﬃcient for
the eradication of the disease from the population. Hence, the threshold value R0 is the noise-
free basic reproduction number for the disease dynamics described by deterministic system
(2.8)-(2.11).
While Theorem 4.1[3.] asserts that the stochastic system (2.15)-(2.18) has no disease free
steady state for the population, whenever the intensity value of the white noise process due
to the natural death rate of the susceptible population is positive, that is, σS > 0, it is
necessary to characterize the behavior of the solutions of the stochastic system near the
disease free steady state E0 of the deterministic system (2.8)-(2.11), in order to gain insight
about the extend of behavioral deviation of the stochastic system (2.15)-(2.18) away from
the deterministic system disease free equilibrium E0, whenever the intensity value σS > 0.
The following result describes the oscillatory behavior of the trajectories of the stochastic
system (2.15)-(2.18) in the neighborhood of the disease free equilibrium E0 obtained in
Theorem 4.1[1.],[2.], whenever Theorem 4.1[3.] is satisﬁed. That is, whenever the stochastic
system (2.15)-(2.18) does not have a disease free equilibrium.
This result characterizes
the expected average relative distance between solutions of the stochastic system (2.15)-
(2.18) and the disease free steady state E0, in an attempt to describe the average size or
amplitude of the trajectories of the stochastic system (2.15)-(2.18) relative to the position
of the deterministic disease free state E0.
Theorem 4.6. Let the hypothesis of Theorem 4.1[3.] be satisﬁed. And deﬁne the following
threshold values:
˜R1 = βS∗
0 ˆK1 + α + 1
2σ2
I
(µ + d + α)
,
(4.63)


## Page 52


52
˜U0 =
2βS∗
0 + β + α + 2
µ
˜
K(µ)2 + σ2
S
2µ
,
(4.64)
and
˜V0 = (2µ ˜K(µ)2 + α + β(2S∗
0 + 1) + σ2
E)
2µ
,
(4.65)
with some constant ˆK1 > 0 that depends on S∗
0 and σβ (in fact, ˆK1 = 4 + S∗
0 + 6 1
βσ2
βS∗
0). Let
X(t) = (S(t), E(t), I(t)) be a solution of the decoupled system from (2.15)-(2.18) with initial
conditions (2.19). Assume that, ˜R1 ≤1, ˜U0 ≤1, and ˜V0 ≤1, then there exists a positive
constant m > 0, such that the following inequality holds
lim sup
t→∞
1
t E
Z t
0

(S(v) −S∗
0)2 + E2(v) + I2(v)

dv ≤3σ2
S(S∗
0)2
m
.
(4.66)
Proof: Let Theorem 4.1[3.] be satisﬁed. Applying the diﬀerential operator dV to V deﬁned
in (4.46), and utilizing (4.8) and (4.9), it is easy to see that
dV = LV dt −2σS(U(t) + V (t))(S∗
0 + U(t))dwS(t)
−2σE(U(t)V (t) + (c + 1)V 2(t))dwE(t) −2σIW 2(t))dwI(t)
−2cσβ(S∗
0 + U(t))V (t)
Z h1
t0
fT1(s)e−µsG(W(t −s))dsdwβ
−2σE[U(t) + (c + 1)V (t) + W(t)] ×
×
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(S∗
0 + U(t −u))G(W(t −s −u))dsdudwβ(t) (4.67)
where for some positive constant valued function ˜K(µ), the drift part of (4.67), LV , satisﬁes
the inequality
LV (x, t) ≤−

˜φU2(t) + ˜ψV 2(t) + ˜ϕW 2(t)

,
(4.68)


## Page 53


53
where
˜φ
=
2µ(1 −˜U0)
(4.69)
˜ψ
=
2µ(1 −˜V0) −(2µ + σ2
E)c

1 −β(3S∗
0 + 1)
(2µ + σ2
E)

(4.70)
˜ϕ
=
2(µ + d + α)(1 −˜R1) −c(3βS∗
0 + β(S∗
0)2 + 4σ2
β(S∗
0)2) −2c2σ2
β(S∗
0)2.
(4.71)
Moreover, ˜R1 =
βS∗
0 ˆ
K1+α+ 1
2 σ2
I
(µ+d+α)
, where ˆK1 = 4 + S∗
0 + 6 1
βσ2
β. Under the assumptions of ˜R1, ˜U0,
and ˜V0 in the hypothesis and for suitable choice of the positive constant c it follows that ˜φ,
˜ψ, and ˜ϕ are positive constants. Therefore, by integrating (4.67) from 0 to t on both sides
and taking the expectation, it follows from (4.67)-(4.71) that
E(V (t) −V (0)) ≤−mE
Z t
0

(S(v) −S∗
0)2 + E2(v) + I2(v)

dv + 3σ2
S(S∗
0)2t,
(4.72)
where V (0) is constant and
m = min(˜φ, ˜ψ, ˜ϕ).
(4.73)
Hence, diving both sides of (4.72) by t and m, and taking the limit supremum as t →∞,
then (4.66) follows immediately.
Remark 4.5.
1. Theorem 4.6 signiﬁes that under conditions that warrant the nonexistence of a disease
free steady state for the stochastic system (2.15)-(2.18), the asymptotic expected average
relative distance between the trajectories of the stochastic system and the disease free steady
state, E0 obtained in Theorem 4.1[1.][2.], does not exceed a constant multiple of the intensity
value, σS, of the white noise process from the natural death rate of the susceptible population,
whenever the following threshold conditions ˜R1 ≤1, ˜U0 ≤1, and ˜V0 ≤1 are satisﬁed. That
is, asymptotically, when the physical characteristics of the disease scenario allow variability
in the natural death rate of susceptible individuals with intensity value σS > 0, there is
no disease free steady state for the stochastic system. Nevertheless, the trajectories of the
stochastic system (2.15)-(2.18) will continue to oscillate near the deterministic disease free
steady state E0 obtained in Theorem 4.1[1.][2.], whenever the threshold conditions ˜R1 ≤1,


## Page 54


54
˜U0 ≤1, and ˜V0 ≤1 are satisﬁed, whence, the threshold values ˜R1, ˜U0, and ˜V0 are deﬁned in
(4.63)-(4.65). Furthermore, the size or amplitude of the oscillations relative to the position
of the disease free state E0 depends on the size of the intensity value, σ2
S.
2. As similarly remarked in Remark 4.4[2.], comparing the threshold values from Theorem 4.5,
Theorem 4.4, and Theorem 4.6, that is, R1, U0, V0 in (4.48)-(4.50), R0, ˆU0, ˆV0 in (4.59)-
(4.61), and ˜R1, ˜U0, ˜V0 in (4.63)-(4.65), it is easy to see that R0 ≤R1 = ˜R1, U0 = ˆU0 ≤˜U0
and V0 ≤ˆV0 = ˜V0, whenever the intensity values of the white noise processes in the system
(2.15)-(2.18) satisfy the condition: σi > 0, i = S, E, I, R, β. It is also easy to see that the
threshold value ˜U0 in (4.64) has been further constrained by the assumption that σS > 0, from
the corresponding threshold value U0 = ˆU0 in (4.49) and (4.60). Meanwhile it was remarked
in Remark 4.4[2.] that the threshold values R1, U0 and V0 from Theorem 4.4 would attain the
threshold condition of ” less than the mark of 1” less rapidly compared to the set of threshold
values R0, ˆU0 and ˆV0 from Theorem 4.5, it is easy to see that the threshold values ˜R1, ˜U0,
and ˜V0 from Theorem 4.6 would attain the threshold condition of ”less than the bound 1”,
even less rapidly when compared to R1, U0 and V0 from Theorem 4.4, and even much less
rapidly when compared to R0, ˆU0 and ˆV0 from Theorem 4.5.
This observation suggests that the sources (natural death or disease transmission rates)
and intensity levels of random ﬂuctuations in the disease dynamics exhibit bearings on (1.)
the existence or attainment of a disease free population steady state for the system (2.15)-
(2.18) and also on (2.) the eradication disease. A critical analysis of the importance of the
source and intensity levels of the random ﬂuctuations in the disease transmission and natural
death rates in the system is a subject for another concurrent study by this author. A valuable
note in this remark, in line with the objectives of the current study, and also in comparing
the asymptotic behavior of the deterministic and stochastic systems (2.8)-(2.11) and (2.15)-
(2.18) relative to the disease free steady state E0, and consequently to disease eradication, is
the extend to which the presence of the noise in the system aﬀects the threshold hold values:
R1, U0, V0 in (4.48)-(4.50), R0, ˆU0, ˆV0 in (4.59)-(4.61), and ˜R1, ˜U0, ˜V0 in (4.63)-(4.65),
which control the asymptotic and qualitative properties of the disease free steady state E0 in
both systems.
3. Furthermore, as similarly remarked in Remark 4.4[2.], the results of Theorem 4.6 suggest
that in a disease scenario that exhibits random ﬂuctuations with signiﬁcant positive intensity
values (σS > 0) in the natural death rate of susceptible individuals and consequently does not
allow the existence of a disease free steady state population, but exhibit physical characteris-
tics which can be represented mathematically by the parameters of the system (2.15)-(2.18),
wherein the threshold values ˜R1, ˜U0, and ˜V0 in (4.63)-(4.65), R1, U0, V0 in (4.48)-(4.50) and
R0, ˆU0, ˆV0 in (4.59)-(4.61), can all be computed, and satisfy the relationship and threshold
conditions, R0 ≤R1 = ˜R1 ≤1, U0 = ˆU0 ≤˜U0 ≤1 and V0 ≤ˆV0 = ˜V0 ≤1, the occurrence of
the white noise processes due to the random environmental ﬂuctuations in the other sources
namely:- from (1.) the natural death rates of the exposed, infectious and removal popula-


## Page 55


55
tions, and also from (2.) the disease transmission rate, exert additional counter-positive
constraints against the disease eradication process as determined by the relationship between
the threshold values and the threshold conditions R0 ≤R1 = ˜R1 ≤1, U0 = ˆU0 ≤˜U0 ≤1
and V0 ≤ˆV0 = ˜V0 ≤1. That is, whereas the disease can be eradicated much less rapidly
when the disease scenario represented by (2.15)-(2.18) is controlled by the threshold values
R1, U0, V0 in (4.48)-(4.50) than when it is controlled by the threshold values R0, ˆU0, ˆV0 in
(4.59)-(4.61), it follows that when the disease scenario is controlled by the threshold values
˜R1, ˜U0, and ˜V0 in (4.63)-(4.65), the disease cannot be eradicated at all. Nevertheless, the
disease population can be maintained close to the disease free population steady state E0 ob-
tained in Theorem 4.1[1.][2.], whenever the value of σs is small and the threshold conditions
˜R1 ≤1, ˜U0 ≤1, and ˜V0 ≤1 are satisﬁed. Thus, good policy decisions about malaria control
must be informed by this fact that, wherever malaria cannot be completely eradicated, it is
important to reduce the intensity of the the random ﬂuctuations in the natural death of the
health susceptible population (perhaps via better care of this population), whenever the other
threshold conditions R0 ≤R1 = ˜R1 ≤1, U0 = ˆU0 ≤˜U0 ≤1 and V0 ≤ˆV0 = ˜V0 ≤1 hold, in
order to contain the disease, and keep the human population close to a disease free state.
5. Existence and Asymptotic properties of the Endemic Equilibrium
In this section the existence and asymptotic behavior of the nontrivial steady state of
the generalized systems (2.8)-(2.11) and (2.15)-(2.18) are discussed. It is easy to see that
the stochastic dynamic system (2.15)-(2.18) does not have a non-zero steady state, whenever
the system is perturbed by the white noise from at least one of the sources: the disease
transmission or the natural death rates, that is, when at least one of σi > 0, i = S, E, I, R, β.
The following result provides suﬃcient conditions for the existence of the endemic equilibrium
of the deterministic system (2.8)-(2.11). That is, when the system is unperturbed by random
ﬂuctuations in the disease dynamics.
Theorem 5.1. Let the threshold condition R0 > 1 be satisﬁed, where R0 is deﬁned in (4.59).
It follows that the deterministic system (2.8)-(2.11) has a unique positive equilibrium state
denoted by E1 = (S∗
1, E∗
1, I∗
1), whenever
E(e−µ(T1+T2)) ≥
ˆK0 +
α
β B
µ
G′(0)
,
(5.1)


## Page 56


56
where ˆK0 is deﬁned in Theorem 4.5.
Proof:
The nonzero steady state solution E1 = (S∗
1, E∗
1, I∗
1) of the decoupled deterministic system
associated with (2.8)-(2.11) is a solution to the following system:
B −βS
Z h1
t0
fT1(s)e−µsG(I))ds −µS + α
Z ∞
t0
fT3(r)Ie−µrdr = 0,
(5.2)
βS
Z h1
t0
fT1(s)e−µsG(I)ds −µE −β
Z h2
t0
fT2(u)S
Z h1
t0
fT1(s)e−µs−µuG(I)dsdu = 0,
(5.3)
β
Z h2
t0
fT2(u)S
Z h1
t0
fT1(s)e−µs−µuG(I)dsdu −(µ + d + α)I = 0.
(5.4)
Solving for E and S from (5.3) and (5.4) respectively and substituting the result into (5.2),
gives the following equation:
H(I) = 0
(5.5)
where,
H(I) = B−
1
E(e−µ(T1+T2))I
(µ + d + α)µ
βG(I)
+ (µ + d)E(e−µT1) + αE(e−µT1)
 1 −E(e−µT2)E(e−µT3)

.
(5.6)
But 0 < E(e−µTi) ≤1, i = 1, 2, 3, and limI→∞G(I) = C < ∞, hence for suﬃciently large
positive value of I, it is easy to see that H(I) is negative. Furthermore, the derivative of
H(I) is given by
H′(I)
=
−(µ + d + α)µ
βE(e−µ(T1+T2))
(G(I) −IG′(I))
G2(I)
−
1
E(e−µ(T1+T2))
 (µ + d)E(e−µT1) + αE(e−µT1)(1 −E(e−µT2)E(e−µT3))

.(5.7)


## Page 57


57
Without loss of generality assume that G′(I) > 0. It follows from the other properties of G
in Assumption 2.1, that is, G(0) = 0, G′′(I) < 0, that (G(I) −IG′(I)) > 0 and this further
implies that H′(I) < 0 for all I > 0. That is, H(I) is a decreasing function for all I > 0.
Therefore, a positive root of the equation (5.5) suﬃces that H(0) > 0. But, from (5.6),
H(0) = B
 
1 −
(µ + d + α)
β B
µ G′(0)E(e−µ(T1+T2))
!
≥B

1 −1
R0

.
(5.8)
Under the assumptions in the hypothesis of Theorem 5.1, it is easy to see that H(0) > 0.
To completely exhibit the inﬂuence of the delays in the system on the existence of the
endemic or nontrivial steady state of the system E1 in the absence of any random ﬂuctuations
in the disease dynamics, the following result which follows immediately from Theorem 5.1
and Theorem 4.3 for constant delays Ti, i = 1, 2, 3 in the system is stated as a theorem.
Theorem 5.2. Suppose the incubation periods of the malaria plasmodium inside the mosquito
and human hosts T1 and T2, and also the period of eﬀective natural immunity against malaria
inside the human being T3 are constant. Let the threshold condition R∗
0 > 1 be satisﬁed, where
R∗
0 is deﬁned in (4.23). It follows that the deterministic system (2.8)-(2.11) has a unique
positive equilibrium state denoted by E1 = (S∗
1, E∗
1, I∗
1), whenever
T1 + T2 ≤1
µ log (G
′(0)).
(5.9)
Proof:
The results in Theorem 5.2 follow easily from the proof of Theorem 5.1 by letting the
probability density functions fTi, i = 1, 2, 3 be the dirac-delata function (4.19), and further
applying the translation properties of the dirac-delta function. It can also be easily seen
from (5.8) that
H(0) = B

1 −1
R∗
0
1
G
′(0)e−µ(T1+T2)

≥B

1 −1
R0

.
(5.10)


## Page 58


58
Hence, H(0) > 0, whenever (5.9) holds and R∗
0 > 1, and the existence result follows imme-
diately.
Remark 5.1.
1. It is noted that (5.1) provides estimates for the expected survival rate E(e−µ(T1+T2)) of the
parasites or infectious agent inside the vectors and the human body over the full incubation
period of the disease. Therefore, Theorem 5.1 provides threshold conditions for the basic re-
production number R0, and the expected survival rate of the parasites of the disease described
by the system (2.8)-(2.11) that are suﬃcient for the dynamics to establish an endemic steady
state of the infection in the population. Thus, malaria control policy decisions should embark
on not only reducing the basic reproduction number of the disease R0, but also reduce the
survival rate of the parasites over the total incubation period in the mosquito and human
body.
2. The importance of the incubation periods of the malaria plasmodium in the human and
mosquito hosts are more highlighted in Theorem 5.2, where it is assumed that the random
variables Ti, i = 1, 2, 3 are constant. Observe that the assumption in (5.9) is also equivalent to
condition on the survival probability rate e−µ(T1+T2) ≥
1
G′(0). The term 1
µ log (G
′(0)) signiﬁes
a fraction of the average lifespan
1
µ of an individual in the population, where the fraction
is determined by the magnitude of log (G
′(0)). Therefore, the assumption in (5.9) signiﬁes
that the existence of the endemic equilibrium in the human population necessitates the total
incubation period of the malaria plasmodium inside the mosquito and human being to be at
most a fraction of the average lifespan of an individual in the population, whenever the basic
reproduction number satisﬁes R∗
0 > 1.
For example, when the nonlinear incidence function G deﬁned in Assumption 2.1 takes
one of the following forms: (1) G(I) =
I
1+aI , a > 0, or (2) G(I) =
I
1+aI2, a > 0 etc., it can
be easily seen that 1
µ log (G
′(0)) = 0. This result implies from Theorem 5.2 and in particular
(5.9), that when T1 + T2 = 0 and the basic reproduction number R∗
0 satisﬁes R∗
0 > 1, then an
endemic equilibrium state E1 exists. That is, in the case where the disease transmission is
instantaneous (T1 + T2 = 0) between humans and mosquitoes, an outbreak of the disease will
rapidly establish a steady endemic population state, whenever R∗
0 > 1.
More generally, let the logarithmic function in (5.9) be written with the base of b ≥1,
that is, log(.) ≡logb(.), b ≥1, and also denote gb(G
′) = 1
µ log (G
′(0)). It is easy to see that
for values of G
′(0) ∈[1, b), it follows that 0 ≤gb(G
′) < 1
µ, and for values of G
′(0) ≥b, it
is seen that gb(G
′) ≥1
µ. Therefore, the values of G
′(0) ≥b, lead to larger values of gb(G
′),
that further expand the length of the interval [0, gb(G
′)], which from (5.9), gives more leeway
for the condition T1 + T2 ∈[0, gb(G
′)] to hold, and consequently lead to the existence of an
endemic equilibrium E1, whenever all other conditions in the hypothesis of Theorem 5.2 are
satisfed. Conversely, the values of G
′(0) ∈[1, b), lead to smaller values of gb(G
′), which


## Page 59


59
further constrict the length of the interval [0, gb(G
′)], and as a result from (5.9), does not
give much leeway for the requirement T1+T2 ∈[0, gb(G
′)] to hold. This observation about the
relationship between the properties of the nonlinear incidence function G, and the existence
of the endemic equilibrium allows more insight about the properties of the incidence function
controlling the persistence of malaria in the human population.
The following lemma will be utilized to prove the results that characterize the asymptotic
behavior of the stochastic system (2.15)-(2.18) in the neighborhood of the nontrivial steady
state E1 = (S∗
1, E∗
1, I∗
1), whenever at least one of σi ̸= 0, i = S, E, I, R, β. It should be noted
from Assumption 2.1 that the nonlinear function G is bounded. Therefore, suppose
G∗= sup
x>0
G(x),
(5.11)
then it is easy to see that 0 ≤G(x) ≤G∗. It follows further from Assumption 2.1 that given
limI→∞G(I) = C, if G is strictly monotonic increasing then G∗≤C. Also, if G is strictly
monotonic decreasing then G∗≥C.
Lemma 5.1. Let the hypothesis of Theorem 5.1 (or Theorem 5.2) be satisﬁed and deﬁne the
C2,1−function V : R3
+ × R+ →R+ where
V (t) = V1(t) + V2(t) + V3(t) + V4(t),
(5.12)
where,
V1(t) = 1
2 (S(t) −S∗
1 + E(t) −E∗
1 + I(t) −I∗
1)2 ,
(5.13)
V2(t) = 1
2 (S(t) −S∗
1)2
(5.14)
V3(t) = 1
2 (S(t) −S∗
1 + E(t) −E∗
1)2 .
(5.15)


## Page 60


60
and
V4(t)
=
3
2
α
λ(µ)
Z ∞
t0
fT3(r)e−2µrdr(I(θ) −I∗)2dθdr
+ βS∗
1
λ(µ)(G′(I∗
1))2
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)
Z t
t−(s+u)
(I(θ) −I∗
1)2dθdsdu
+[βλ(µ)
2
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)
Z t
t−(s+u)
G2(I(θ))(S(θ) −S∗
1)2dθdsdu
+σ2
β
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)
Z t
t−(s+u)
G2(I(θ))(S(θ) −S∗
1)2dθdsdu,
(5.16)
where λ(µ) > 0 is a real valued function of µ. Suppose ˜φ1, ˜ψ1 and ˜ϕ1 are deﬁned as follows
˜φ1
=
3µ −

2µλ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ) + βS∗
1λ(µ)
2
+ 3σ2
S +
β(G∗)2
2λ(µ) + σ2
β(G∗)2

E(e−2µT1)
+
βλ(µ)(G∗)2
2
+ σ2
β(G∗)2

E(e−2µ(T1+T2))

(5.17)
˜ψ1
=
2µ −

β
2λ(µ) + βS∗
1λ(µ)
2
+ 2µ
λ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ) + 2σ2
E

(5.18)
˜ϕ1
=
(µ + d + α) −

(2µ + d + α)
1
λ(µ) + αλ(µ)
2
+ σ2
I +
3α
2λ(µ)E(e−2µT3)
+
βS∗
1(G′(I∗
1))2
λ(µ)

E(e−2µ(T1+T2))

.
(5.19)
The diﬀerential operator dV applied to V (t) with respect to the stochastic system (2.15)-
(2.18) can be written as follows:
dV = LV (t)dt + −→g (S(t), E(t), I(t))d−−→
w(t),
(5.20)
where for −−→
w(t) = (wS, wE, wI, wβ)T and the function (S(t), E(t), I(t)) 7→g(S(t), E(t), I(t)),


## Page 61


61
is deﬁned as follows:
−→g (S(t), E(t), I(t))d−−→
w(t) = −σS(3(S(t) −S∗
1) + 2(E(t) −E∗
1) + I(t) −I∗
1)S(t)dwS(t)
−σE(2(S(t) −S∗
1) + 2(E(t) −E∗
1) + I(t) −I∗
1)E(t)dwE(t)
−σI((S(t) −S∗
1) + (E(t) −E∗
1) + I(t) −I∗
1)I(t)dwI(t)
−σβ(S(t) −S∗
1)S(t)
Z h1
t0
fT1(s)e−µsG(I(t −s))dsdwβ(t)
−σβ((S(t) −S∗
1) + (E(t) −E∗
1))
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)S(t −u)G(I(t −s −u))dsdudwβ(t),
(5.21)
and LV satisﬁes the following inequality
LV (t)
≤
−
n
˜φ1(S(t) −S∗
1)2 + ˜ψ1(E(t) −E∗
1)2 + ˜ϕ1(I(t) −I∗
1)2o
+3σ2
S(S∗
1)2 + 2σ2
E(E∗
1)2 + σ2
I(I∗
1)2 + σ2
β(S∗
1)2(G∗)2E(e−2µ(T1+T2)) + σ2
β(S∗
1)2(G∗)2E(e−µT1).
(5.22)
Proof
From (5.13)-(5.15) the derivative of V1, V2 and V3 with respect to the system (2.15)-(2.18)
can be written in the form:
dV1
=
LV1dt −σS((S(t) −S∗
1) + (E(t) −E∗
1) + I(t) −I∗
1)S(t)dwS(t)
−σE((S(t) −S∗
1) + (E(t) −E∗
1) + I(t) −I∗
1)E(t)dwE(t)
−σI((S(t) −S∗
1) + (E(t) −E∗
1) + I(t) −I∗
1)I(t)dwI(t),
(5.23)


## Page 62


62
dV2
=
LV2dt −σS((S(t) −S∗
1))S(t)dwS(t)
−σβ(S(t) −S∗
1)S(t)
Z h1
t0
fT1(s)e−µsG(I(t −s))dsdwβ(t)
(5.24)
and
dV3
=
LV3dt −σS((S(t) −S∗
1) + (E(t) −E∗
1))S(t)dwS(t) −σS((S(t) −S∗
1) + (E(t) −E∗
1))E(t)dwE(t)
−σβ((S(t) −S∗
1) + (E(t) −E∗
1))
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)S(t −u)G(I(t −s −u))dsdudwβ(t),
(5.25
where utilizing (5.2)-(5.4), LV1, LV2 and LV3 can be written as follows:
LV1(t)
=
−µ(S(t) −S∗
1)2 −µ(E(t) −E∗
1)2 −(µ + d + α)(I(t) −I∗
1)2
−2µ(S(t) −S∗
1)(E(t) −E∗
1) −(2µ + d + α)(S(t) −S∗
1)(I(t) −I∗
1)
−(2µ + d + α)(E(t) −E∗
1)(I(t) −I∗
1)
+α((S(t) −S∗
1) + (E(t) −E∗
1) + (I(t) −I∗
1))
Z ∞
t0
fT3(r)e−µr(I(t −r) −I∗
1)dr
+1
2σ2
SS2(t) + 1
2σ2
EE2(t) + 1
2σ2
II2(t),
(5.26)


## Page 63


63
LV2(t)
=
−µ(S(t) −S∗
1)2 + α(S(t) −S∗
1)
Z ∞
t0
fT3(r)e−µr(I(t −r) −I∗
1)dr
−β(S(t) −S∗
1)2
Z h1
t0
fT1(s)e−µsG(I(t −s))ds
−βS∗
1(S(t) −S∗
1)
Z h1
t0
fT1(s)e−µs(G(I(t −s)) −G(I∗
1))ds
+1
2σ2
SS2(t) + 1
2σ2
βS2(t)
Z h1
t0
fT1(s)e−µsG(I(t −s))ds
2
,
(5.27)
and
LV3(t)
=
−µ(S(t) −S∗
1)2 −µ(E(t) −E∗
1)2 −2µ(S(t) −S∗
1)(E(t) −E∗
1)
+α((S(t) −S∗
1) + (E(t) −E∗
1))
Z ∞
t0
fT3(r)e−µr(I(t −r) −I∗
1)dr
−β(S(t) −S∗
1)
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(S(t −u) −S∗
1)G(I(t −s −u))dsdu
−β(E(t) −E∗
1)
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(S(t −u) −S∗
1)G(I(t −s −u))dsdu
−βS∗
1(S(t) −S∗
1)
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(G(I(t −s −u)) −G(I∗
1))dsdu
−βS∗
1(E(t) −E∗
1)
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(G(I(t −s −u)) −G(I∗
1))dsdu
+1
2σ2
SS2(t) + 1
2σ2
EE2(t)
+1
2σ2
β
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)S(t −u)G(I(t −s −u))dsdu
2
.
(5.28)
From (5.26)-(5.28), the set of inequalities that follow will be used to estimate the sum
LV1(t) + LV2(t) + LV3(t):- Applying Cauchy −Swartz and H¨older inequalities, and also
applying the algebraic inequality (4.11), the terms associated with the integral term (sign)


## Page 64


64
R ∞
t0 fT3(r)e−µr(I(t −r) −I∗
1)dr are estimated as follows:
(a(t)−a∗)
Z ∞
t0
fT3(r)e−µr(I(t−r)−I∗
1)dr ≤λ(µ)
2
(a−a∗)2+
1
2λ(µ)
Z ∞
t0
fT3(r)e−2µr(I(t−r)−I∗
1)2dr,
(5.29)
where a(t) ∈{S(t), E(t), I(t)} and a∗∈{S∗
1, E∗
1, I∗
1}.
Furthermore, the terms with the
integral sign that depend on G(I(t −s)) and G(I(t −s −u)) are estimated as follows:
−β(S(t) −S∗
1)2
Z h1
t0
fT1(s)e−µsG(I(t −s))ds ≤βλ(µ)
2
(S(t) −S∗
1)2
+
β
2λ(µ)(S(t) −S∗
1)2
Z h1
t0
fT1(s)e−2µsG2(I(t −s))ds.
−β(E(t) −E∗
1)
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(S(t −u) −S∗
1)G(I(t −s −u))dsdu ≤
β
2λ(µ)(E(t) −E∗
1)2
+βλ(µ)
2
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)(S(t −u) −S∗
1)2G2(I(t −s −u))dsdu.
(5.30)
The terms with the integral sign that depend on G(I(t−s))−G(I∗
1) and G(I(t−s−u))−G(I∗
1)


## Page 65


65
are estimated as follows:
−βS∗
1(S(t) −S∗
1)
Z h1
t0
fT1(s)e−µs(G(I(t −s)) −G(I∗
1))ds ≤βS∗
1λ(µ)
2
(S(t) −S∗
1)2
+ βS∗
1
2λ(µ)
Z h1
t0
fT1(s)e−2µs(I(t −s) −I∗
1)2
G(I(t −s)) −G(I∗
1)
I(t −s) −I∗
1
2
ds
≤βS∗
1λ(µ)
2
(S(t) −S∗
1)2
+ βS∗
1
2λ(µ)
Z h1
t0
fT1(s)e−2µs(I(t −s) −I∗
1)2 (G′(I∗
1))2 ds.
−βS∗
1(E(t) −E∗
1)
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)(G(I(t −s −u)) −G(I∗
1))dsdu ≤βS∗
1λ(µ)
2
(E(t) −E∗
1)2
+ βS∗
1
2λ(µ)
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µs(I(t −s −u) −I∗
1)2
G(I(t −s −u)) −G(I∗
1)
I(t −s −u) −I∗
1
2
ds
≤βS∗
1λ(µ)
2
(E(t) −E∗
1)2
+ βS∗
1
2λ(µ)
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µs(I(t −s −u) −I∗
1)2 (G′(I∗
1))2 ds,
(5.31)
where the inequality in (5.31) follows from Assumption 2.1. That is, G is a diﬀerentiable
monotonic function with G′′(I) < 0, and consequently, 0 < G(I)−G(I∗
1 )
(I−I∗
1 )
≤G′(I∗
1), ∀I > 0.
By also employing the Cauchy −Swartz and H¨older inequalities, and also applying the
following algebraic inequality (a + b)2 ≤2a2 + 2b2, the last set of terms with integral signs


## Page 66


66
on (5.27)-(5.28) are estimated as follows:
1
2σ2
βS2(t)
Z h1
t0
fT1(s)e−µsG(I(t −s))ds
2
≤σ2
β
 (S(t) −S∗
1)2 + (S∗
1)2
×
×
Z h1
t0
fT1(s)e−2µsG2(I(t −s))ds.
1
2σ2
β
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−µ(s+u)S(t −u)G(I(t −s −u))dsdu
2
≤σ2
β ×
×
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)  (S(t −u) −S∗
1)2 + (S∗
1)2
G2(I(t −s −u))dsdu.
(5.32)
By further applying the algebraic inequality (4.11) and the inequalities (5.29)-(5.32) on the


## Page 67


67
sum LV1(t) + LV2(t) + LV3(t), it is easy to see from (5.26)-(5.28) that
LV1(t) + LV2(t) + LV3(t) ≤(S(t) −S∗
1)2

−3µ + 2µλ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ)
+βλ(µ)
2
+ βS∗
1λ(µ)
2
+
β
2λ(µ)(G∗)2E(e−2µT1) + 3σ2
S + σ2
S(G∗)2E(e−2µT1)

(E(t) −E∗
1)2

−2µ + 2µ
λ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ) +
β
2λ(µ) + βS∗
1λ(µ)
2
+ 2σ2
E

+(I(t) −I∗
1)2

−(µ + d + α) + (2µ + d + α)
1
λ(µ) + αλ(µ)
2
+
β
2λ(µ) + βS∗
1λ(µ)
2
+ σ2
I

+ 3α
2λ(µ)
Z ∞
t0
fT3(r)e−2µr(I(t −r) −I∗
1)2dr
+ βS∗
1
λ(µ)(G′(I∗
1))2
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)(I(t −s −u) −I∗
1)2dsdu
+βλ(µ)
2
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)G2(I(t −s −u))(S(t −s) −S∗
1)2dsdu
+3σ2
S(S∗
1)2 + 2σ2
E(E∗
1)2 + σ2
I(I∗
1)2
+σ2
β(S∗
1)2
Z h1
t0
fT1(r)e−2µfT1(s)e−2µsG2(I(t −s))ds
+σ2
β
Z h2
t0
Z h1
t0
fT2(u)fT1(s)e−2µ(s+u)G2(I(t −s −u))(S(t −s −u) −S∗
1)2dsdu
(5.33)
But V (t) = V1(t) + V2(t) + V3(t) + V4(t), therefore from (5.33), (5.16) and (5.26)-(5.28), the
results in (5.20)-(5.22) follow directly.
Theorem 5.1 asserts that the deterministic system (2.8)-(2.11) has an endemic equilibrium
denoted E1 = (S∗
1, E∗
1, I∗
1). To obtain insight about the endemic asymptotic properties of the
disease dynamics in the absence of any random ﬂuctuations in the system, it is necessary
to study the global stability of the endemic equilibrium of the deterministic system. For
convenience, the following notations are introduced and used in the rest of the results that
follow in this section. Let a1(µ, d, α, β, B, σ2
S, σ2
β), a2(µ, d, α, β, B, σ2
I), a3(µ, d, α, β, B), and


## Page 68


68
a3(µ, d, α, β, B, σ2
E) represent the following set of parameters
a1(µ, d, α, β, B, σ2
S, σ2
β)
=
2µλ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ) + βS∗
1λ(µ)
2
+ 3σ2
S
+
βλ(µ)(G∗)2
2
+ σ2
β(G∗)2
 
1
G′(0)
2
(5.34)
a1(µ, d, α, β, B)
=
2µλ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ) + βS∗
1λ(µ)
2
+
βλ(µ)(G∗)2
2
 
1
G′(0)
2
(5.35)
a2(µ, d, α, β, B, σ2
I)
=
(2µ + d + α)
1
λ(µ) + αλ(µ)
2
+ σ2
I
+
βS∗
1(G′(I∗
1))2
λ(µ)
 
1
G′(0)
2
(5.36)
a2(µ, d, α, β, B)
=
(2µ + d + α)
1
λ(µ) + αλ(µ)
2
+
βS∗
1(G′(I∗
1))2
λ(µ)
 
1
G′(0)
2
(5.37)
a3(µ, d, α, β, B, σ2
E)
=
β
2λ(µ) + βS∗
1λ(µ)
2
+ 2µ
λ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ) + 2σ2
E
a3(µ, d, α, β, B)
=
β
2λ(µ) + βS∗
1λ(µ)
2
+ 2µ
λ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ)
(5.38)
Also let ˜a1(µ, d, α, β, B, σ2
S, σ2
β), ˜a1(µ, d, α, β, B), ˜a2(µ, d, α, β, B, σ2
I), ˜a2(µ, d, α, β, B) rep-


## Page 69


69
resent the following set of parameters
˜a1(µ, d, α, β, B, σ2
S, σ2
β)
=
2µλ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ) + βS∗
1λ(µ)
2
+ 3σ2
S
+
βλ(µ)(G∗)2
2
+ σ2
β(G∗)2

+
β(G∗)2
2λ(µ) + σ2
β(G∗)2

(5.39)
˜a1(µ, d, α, β, B)
=
2µλ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ) + βS∗
1λ(µ)
2
+
βλ(µ)(G∗)2
2

+
β(G∗)2
2λ(µ)

(5.40)
˜a2(µ, d, α, β, B, σ2
I)
=
(2µ + d + α)
1
λ(µ) + αλ(µ)
2
+ σ2
I
+
βS∗
1(G′(I∗
1))2
λ(µ)

+
3α
2λ(µ),
(5.41)
˜a2(µ, d, α, β, B)
=
(2µ + d + α)
1
λ(µ) + αλ(µ)
2
+
βS∗
1(G′(I∗
1))2
λ(µ)

+
3α
2λ(µ).
(5.42)
Theorem 5.3. Let the hypotheses of Theorem 5.1 and Lemma 5.1 be satisﬁed and let
µ > max
1
3˜a1(µ, d, α, β, B), 1
2a3(µ, d, α, β, B)

and
(µ + d + α) > ˜a2(µ, d, α, β, B).
(5.43)
For any probability distribution of the delay times T1, T2 and T3, the following are true:-
1. There exists a positive real number m2 > 0, such that the diﬀerential operator ˙V applied to
the Lyapunov functional V deﬁned in (5.12) with respect to the deterministic system (2.8)-
(2.11), satisﬁes the following inequality
˙V (t)
≤
−m2||X(t) −E1||2,
(5.44)
where X(t) is deﬁned in (2.21) and ||.|| is the natural norm deﬁned on R2.
2. The endemic equilibrium E1 is globally uniformly and asymptotically stable.
Proof:
From Lemma 5.1, (5.17)-(5.19), and letting the intensity values σi = 0, i = S, E, I, β, it


## Page 70


70
follows that
−˜φ1
=
−3µ +

2µλ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ) + βS∗
1λ(µ)
2
+
β(G∗)2
2λ(µ)

E(e−2µT1)
+
βλ(µ)(G∗)2
2

E(e−2µ(T1+T2))

≤−3µ +

2µλ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ) + βS∗
1λ(µ)
2
+
β(G∗)2
2λ(µ)

+
βλ(µ)(G∗)2
2

= −(3µ −˜a1(µ, d, α, β, B))
(5.45)
−˜ψ1
=
−2µ +

β
2λ(µ) + βS∗
1λ(µ)
2
+ 2µ
λ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ)

= −(2µ −a3(µ, d, α, β, B))
(5.46)
−˜ϕ1
=
−(µ + d + α) +

(2µ + d + α)
1
λ(µ) + αλ(µ)
2
+
3α
2λ(µ)E(e−2µT3)
+
βS∗
1(G′(I∗
1))2
λ(µ)

E(e−2µ(T1+T2))

≤
−(µ + d + α) +

(2µ + d + α)
1
λ(µ) + αλ(µ)
2
+
3α
2λ(µ)
+
βS∗
1(G′(I∗
1))2
λ(µ)

= −((µ + d + α) −˜a2(µ, d, α, β, B)),
(5.47)
since 0 < E(e−2µ(Ti)) ≤1, i = 1, 2, 3. It follows from (5.22) and (5.45)-(5.47) that
LV
≤
−min{(3µ −˜a1(µ, d, α, β, B)), (2µ −a3(µ, d, α, β, B)), ((µ + d + α) −˜a2(µ, d, α, β, B))} ×
×

(S(t) −S∗
1)2 + (E(t) −E∗
1)2 + (I(t) −I∗
1)2
.
(5.48)


## Page 71


71
Deﬁne
m2 = min{(3µ −˜a1(µ, d, α, β, B)), (2µ −a3(µ, d, α, β, B)), ((µ + d + α) −˜a2(µ, d, α, β, B))}.
(5.49)
Then under the assumption (5.43) in the hypothesis, m2 > 0. Thus, the result in (5.44)
follows directly from (5.48). Moreover, the global uniform asymptotic stability of the steady
state E1 follows easily by applying the comparison stability results in [44, 41].
The following result presence a clearer picture of the inﬂuence of the delays in the system
on the stability of the endemic equilibrium E1, whenever the system is unperturbed by the
random ﬂuctuations in the disease dynamics.
Theorem 5.4. Let the hypotheses of Theorem 5.2 and Lemma 5.1 be satisﬁed and let
µ > max
1
3a1(µ, d, α, β, B), 1
2a3(µ, d, α, β, B)

,
and
(µ + d + α) > a2(µ, d, α, β, B).
(5.50)
Also let the delay times T1, T2 and T3 be constant, that is, the probability density functions
of T1, T2 and T3 respectively denoted by fTi, i = 1, 2, 3 are the dirac-delta functions deﬁned in
(4.19). Furthermore, let the constants T1, T2 and T3 satisfy the following set of inequalities:
T1 > 1
2µ log



β(G∗)2
2λ(µ)

(3µ −a1(µ, d, α, β, B))

,
(5.51)
T2 < 1
2µ log


(3µ −a1(µ, d, α, β, B))

β(G∗)2
2λ(µ)
 
1
G′(0)
2


,
(5.52)
and
T3 > 1
2µ log
 
3α
2λ(µ)
(µ + d + α) −a2(µ, d, α, β, B)
!
.
(5.53)
There exists a positive real number m1 > 0, such that the diﬀerential operator ˙V applied to
the Lyapunov functional V deﬁned in (5.12) with respect to the deterministic system (2.8)-


## Page 72


72
(2.11), satisﬁes the following inequality
˙V (t)
≤
−m1||X(t) −E1||2,
(5.54)
where X(t) is deﬁned in (2.21) and ||.|| is the natural norm deﬁned on R2.
Furthermore, the endemic equilibrium E1 is globally uniformly and asymptotically stable.
Moreover, it is exponentially stable.
Proof:
From Lemma 5.1 and (5.17)-(5.19), by setting σi = 0, i = S, E, I, R, β, it is easy to see
that under the assumptions in (5.9), and (5.50)-(5.53), then ˜φ1 > 0, ˜ψ1 > 0 and ˜ϕ1 > 0.
Therefore, from (5.20)-(5.22) it is also easy to see that
˙V (t)
≤
−min (˜φ1, ˜ψ1, ˜ϕ1)

(S(t) −S∗
1)2 + (E(t) −E∗
1)2 + (I(t) −I∗
1)2	
.
(5.55)
Letting m1 = min (˜φ1, ˜ψ1, ˜ϕ1), the result in (5.54) follows immediately.
Moreover, the global uniform asymptotic stability of the steady state E1 follows easily
by applying the comparison stability results in [56, 57, 41].
Remark 5.2. Theorem 5.3 presents minimum suﬃcient conditions independent of the prob-
ability distribution of the delay time random variables T1, T2 and T3 that lead to the global
uniform stability of the endemic equilibrium E1. That is, when the disease dynamics is un-
perturbed by random ﬂuctuations in the disease, then all solutions of the system (2.8)-(2.11)
that start near the nontrivial steady state E1 stay in the neighborhood of the steady state,
and converge asymptotically at E1, whenever the conditions in hypothesis of Theorem 5.6 are
satisﬁed. In other words, the disease is persistent near the nontrivial steady state, whenever
the conditions in the hypothesis of Theorem 5.6 are satisﬁed.
A clearer picture of the impacts of the delays in the system Ti, i = 1, 2, 3 on the stability
of the endemic equilibrium is presented in Theorem 5.4, where it is assumed that the in-
cubation delay period of malaria inside the vector and human hosts, and also the period of
eﬀective natural immunity are all constant for all individuals in the population. The condi-
tions in (5.50) and (5.51)-(5.53) are suﬃcient for the disease to be persistent in the human
population. The threshold bounds for the delay times in (5.51)-(5.53) are all fractions of the
average lifespan 1
µ of individuals in the population. Moreover, the threshold bounds depend


## Page 73


73
on the parameters of the system and are computationally attractive, whenever a speciﬁc set
of parameter values are given. Therefore, in a disease scenario where the incubation delays
and natural immunity delay period are constant, an estimate for the values T1, T2 and T3 can
be determine which would lead to malaria persistence in the population.
The smooth behavior of the disease dynamics near the endemic equilibrium E1 depicted
in Theorem 5.3 and Theorem 5.4 is complicated by the presence of noise due to random
ﬂuctuations in the disease dynamics as it is shown by the subsequent results. The following
theorem characterizes the behavior of the stochastic system (2.15)-(2.18) in the neighborhood
of the nontrivial steady states E1 = (S∗
1, E∗
1, I∗
1) deﬁned in Theorem 5.1 and Theorem 5.2,
whenever the incubation and natural immunity delay times of the disease denoted by T1,
T2, and T3 are constant for all individuals in the population. The assumption that T1, T2
and T3 are constant, is also equivalent to the special case of letting the probability density
functions of T1, T2 and T3 to be the dirac-delta function deﬁned in (4.19). Moreover, under
the assumption that T1 ≥0, T2 ≥0 and T3 ≥0 are constant, it follows from (5.17)-(5.19),
that E(e−2µ(T1+T2)) = e−2µ(T1+T2), E(e−2µT1) = e−2µT1 and E(e−2µT3) = e−2µT3.
Theorem 5.5. Let the hypotheses of Theorem 5.2 and Lemma 5.1 be satisﬁed and let
µ > max
1
3a1(µ, d, α, β, B, σ2
S, σ2
β), 1
2a3(µ, d, α, β, B, σ2
E)

,
and
(µ+d+α) > a2(µ, d, α, β, B, σ2
I).
(5.56)
Also let the delay times T1, T2 and T3 be constant, that is, the probability density functions
of T1, T2 and T3 respectively denoted by fTi, i = 1, 2, 3 are the dirac-delta functions deﬁned in
(4.19). Furthermore, let the constants T1, T2 and T3 satisfy the following set of inequalities:
T1 > 1
2µ log



β(G∗)2
2λ(µ) + σ2
β(G∗)2
(3µ −a1(µ, d, α, β, B, σ2
S, σ2
β))

,
(5.57)
T2 < 1
2µ log



(3µ −a1(µ, d, α, β, B, σ2
S, σ2
β))

β(G∗)2
2λ(µ) + σ2
β(G∗)2
 
1
G′(0)
2


,
(5.58)


## Page 74


74
and
T3 > 1
2µ log
 
3α
2λ(µ)
(µ + d + α) −a2(µ, d, α, β, B, σ2
I)
!
.
(5.59)
There exists a positive real number m1 > 0, such that
lim sup
t→∞
1
t E
Z t
0

(S(v) −S∗
1)2 + (E(v) −E∗
1)2 + (I(v) −I∗
1)2
dv
≤3σ2
S(S∗
1)2 + 2σ2
E(E∗
1)2 + σ2
I(I∗
1)2 + σ2
β(S∗
1)2(G∗)2e−2µ(T1+T2) + σ2
β(S∗
1)2(G∗)2e−µT1
m1
.
(5.60)
Proof:
From Lemma 5.1, (5.17)-(5.19), it is easy to see that under the assumptions in (5.9) and
(5.56)-(5.59), then ˜φ1 > 0, ˜ψ1 > 0 and ˜ϕ1 > 0. Therefore, from (5.20)-(5.22) it is also easy
to see that
dV
=
LV (t)dt + −→g (S(t), E(t), I(t))d−−→
w(t),
≤
−min{˜φ1, ˜ψ1, ˜ϕ1}

(S(t) −S∗
1)2 + (E(t) −E∗
1)2 + (I(t) −I∗
1)2
+3σ2
S(S∗
1)2 + 2σ2
E(E∗
1)2 + σ2
I(I∗
1)2 + σ2
β(S∗
1)2(G∗)2e−2µ(T1+T2) + σ2
β(S∗
1)2(G∗)2e−µT1
+−→g (S(t), E(t), I(t))d−−→
w(t),
(5.61)
Integrating both sides of (5.61) from 0 to t and taking the expectation, it follows that
E(V (t) −V (0)) ≤−m1E
Z t
0

(S(v) −S∗
1)2 + (E(v) −E∗
1)2 + (I(v) −I∗
1)2
dv
+
 3σ2
S(S∗
1)2 + 2σ2
E(E∗
1)2 + σ2
I(I∗
1)2 + σ2
β(S∗
1)2(G∗)2e−2µ(T1+T2) + σ2
β(S∗
1)2(G∗)2e−µT1
t,
(5.62)


## Page 75


75
where V (0) is constant and
m1 = min(˜φ, ˜ψ, ˜ϕ) > 0.
(5.63)
Hence, diving both sides of (5.62) by t and m1, and taking the lim supt→∞, then (5.60) follows
directly.
Remark 5.3. When the disease dynamics is perturbed by random ﬂuctuations in the disease
transmission or natural death rates, that is, when at least one of the intensities σ2
i ̸= 0, i =
S, E, I, β, it has been noted earlier that the stochastic system (2.15)-(2.18) does not have an
endemic equilibrium state. Nevertheless, the conditions in Theorem 5.5 provide estimates
for the constant delay times T1, T2 and T3 in (5.57)-(5.59) in addition to other parametric
restrictions in (5.56) that are suﬃcient for the solutions of the perturbed stochastic system
(2.15)-(2.18) to oscillate near the nontrivial steady state, E1, of the deterministic system
(2.8)-(2.11) found in Theorem 5.1. The result in (5.60) that characterizes the average dis-
tance between the trajectories of the stochastic system and the nontrivial steady state E1 also
signiﬁes that the size of the oscillations of the trajectories relative to E1 depends on the size
of the intensity values, σ2
i ̸= 0, i = S, E, I, β, of the random ﬂuctuations.
As a physical interpretation and deduction, the results in Theorem 5.5 suggest that the
presence of random ﬂuctuations in the malaria dynamics stemming from the disease trans-
mission or natural death rates completely perturbs the stability of the endemic equilibrium E1
shown in Theorem 5.4. This means that the presence of noise in the malaria epidemic pro-
motes the persistence of malaria in the human population as described in Remark 5.2, where
the human population continues to oscillates in character near the nonzero steady state E1
as depicted in (5.60). Furthermore, for smaller intensity values of the random ﬂuctuations,
the human population also oscillates closely to the nonzero steady state E1, and vice versa.
While (5.60) indicates that larger intensity values of the random ﬂuctuations in the natural
death and disease transmission rates lead to the human population oscillating further away
from the nonzero steady state E1 asymptotically, it can be propositioned that the human pop-
ulation gets extinct overtime due to the high intensity of natural death rate of human beings
asymptotically. The numerical simulation results in Section 6 conﬁrm the proposition that
the human population becomes extinct asymptotically for suﬃciently large intensities of the
random ﬂuctuations.
These facts suggest that malaria control policies in the event where the disease is persis-
tent, should focus on reducing the intensities of the ﬂuctuations in the disease transmission
and natural death rates, perhaps through vector control and better care of the people in the
population, in order to reduce the number of deaths that may lead to human extinction by
the disease.
The subsequent result provides more general conditions irrespective of the probability dis-


## Page 76


76
tribution of the random variables T1, T2 and T3, that are suﬃcient for the trajectories of
the stochastic system (2.15)-(2.18) to oscillate near the nontrivial steady state E1, of the
deterministic system (2.8)-(2.11).
Theorem 5.6. Let the hypotheses of Theorem 5.1 and Lemma 5.1 be satisﬁed, and let
µ > max
1
3˜a1(µ, d, α, β, B, σ2
S, σ2
β), 1
2a3(µ, d, α, β, B, σ2
E)

and
(µ+d+α) > ˜a2(µ, d, α, β, B, σ2
I).
(5.64)
It follows that for any arbitrary probability distribution of the delay times: T1, T2 and T3,
there exists a positive real number m2 > 0 such that
lim sup
t→∞
1
t E
Z t
0

(S(v) −S∗
1)2 + (E(v) −E∗
1)2 + (I(v) −I∗
1)2
dv
≤3σ2
S(S∗
1)2 + 2σ2
E(E∗
1)2 + σ2
I(I∗
1)2 + σ2
β(S∗
1)2(G∗)2E(e−2µ(T1+T2)) + σ2
β(S∗
1)2(G∗)2E(e−µT1)
m2
.
(5.65)
Proof:


## Page 77


77
From Lemma 5.1, (5.17)-(5.19),
−˜φ1
=
−3µ +

2µλ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ) + βS∗
1λ(µ)
2
+ 3σ2
S +
β(G∗)2
2λ(µ) + σ2
β(G∗)2

E(e−2µT1
+
βλ(µ)(G∗)2
2
+ σ2
β(G∗)2

E(e−2µ(T1+T2))

≤−3µ +

2µλ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ) + βS∗
1λ(µ)
2
+ 3σ2
S +
β(G∗)2
2λ(µ) + σ2
β(G∗)2

+
βλ(µ)(G∗)2
2
+ σ2
β(G∗)2

= −
 3µ −˜a1(µ, d, α, β, B, σ2
S, σ2
β)

(5.6
−˜ψ1
=
−2µ +

β
2λ(µ) + βS∗
1λ(µ)
2
+ 2µ
λ(µ) + (2µ + d + α)λ(µ)
2
+ αλ(µ) + 2σ2
E

= −
 2µ −a3(µ, d, α, β, B, σ2
E)

(5.6
−˜ϕ1
=
−(µ + d + α) +

(2µ + d + α)
1
λ(µ) + αλ(µ)
2
+ σ2
I +
3α
2λ(µ)E(e−2µT3)
+
βS∗
1(G′(I∗
1))2
λ(µ)

E(e−2µ(T1+T2))

≤
−(µ + d + α) +

(2µ + d + α)
1
λ(µ) + αλ(µ)
2
+ σ2
I +
3α
2λ(µ)
+
βS∗
1(G′(I∗
1))2
λ(µ)

= −
 (µ + d + α) −˜a2(µ, d, α, β, B, σ2
I)

,
(5.6


## Page 78


78
since 0 < E(e−2µ(Ti)) ≤1, i = 1, 2, 3. It follows from (5.20)-(5.22) and (5.66)-(5.68) that
dV
=
LV (t)dt + −→g (S(t), E(t), I(t))d−−→
w(t),
≤
−min{(3µ −˜a1(µ, d, α, β, B)), (2µ −a3(µ, d, α, β, B)), ((µ + d + α) −˜a2(µ, d, α, β, B))} ×
×

(S(t) −S∗
1)2 + (E(t) −E∗
1)2 + (I(t) −I∗
1)2
+3σ2
S(S∗
1)2 + 2σ2
E(E∗
1)2 + σ2
I(I∗
1)2 + σ2
β(S∗
1)2(G∗)2e−2µ(T1+T2) + σ2
β(S∗
1)2(G∗)2e−µT1
+−→g (S(t), E(t), I(t))d−−→
w(t),
(5.69)
where under the assumptions (5.64) in the hypothesis,
m2 = min{(3µ −˜a1(µ, d, α, β, B)), (2µ −a3(µ, d, α, β, B)), ((µ + d + α) −˜a2(µ, d, α, β, B))} > 0.
(5.70)
Integrating both sides of (5.69) from 0 to t and taking the expectation, it follows that
E(V (t) −V (0)) ≤−m2E
Z t
0

(S(v) −S∗
1)2 + (E(v) −E∗
1)2 + (I(v) −I∗
1)2
dv
+
 3σ2
S(S∗
1)2 + 2σ2
E(E∗
1)2 + σ2
I(I∗
1)2 + σ2
β(S∗
1)2(G∗)2E(e−2µ(T1+T2)) + σ2
β(S∗
1)2(G∗)2E(e−µT1)

t,
(5.71)
where V (0) is constant. Hence, diving both sides of (5.71) by t and m2, and taking the
lim supt→∞, then (5.65) follows directly.
Remark 5.4. When the disease dynamics is perturbed by random ﬂuctuations in the disease
transmission or natural death rates, that is, when at least one of the intensities σ2
i ̸= 0, i =
S, E, I, β, it has been noted earlier that the stochastic system (2.15)-(2.18) does not have
an endemic equilibrium state. Nevertheless, the conditions in Theorem 5.6 provide mini-
mum general parametric restrictions in (5.64) irrespective of the probability distribution of
the random variable delay times T1, T2 and T3 that are suﬃcient for the solutions of the per-
turbed stochastic system (2.15)-(2.18) to oscillate near the nontrivial steady state, E1, of the


## Page 79


79
deterministic system (2.8)-(2.11) found in Theorem 5.1. The result in (5.65) that character-
izes the average distance between the trajectories of the stochastic system and the nontrivial
steady state E1 also signiﬁes that the size of the oscillations of the trajectories relative to E1
depends on the intensity values, σ2
i ̸= 0, i = S, E, I, β, of the random ﬂuctuations.
In addition, comparing the conditions in (5.64) with the deterministic case in (5.43), it
is easy to see that
µ > max
1
3˜a1(µ, d, α, β, B, σ2
S, σ2
β), 1
2a3(µ, d, α, β, B, σ2
E)

> max
1
3˜a1(µ, d, α, β, B), 1
2a3(µ, d, α, β, B)

and
(µ + d + α) > ˜a2(µ, d, α, β, B, σ2
I) > ˜a2(µ, d, α, β, B),
(5.72)
whenever σi > 0, i = S, E, I, β. It can be deduced from the observation in (5.72) and con-
clusions of Theorem 5.6 and Theorem 5.3 that in the absence of any random ﬂuctuations
in the disease dynamics from natural death and disease transmission rates, a solution that
starts in the neighborhood of the nontrivial steady state E1 stays in the neighborhood and
converges asymptotically to the steady state E1. However, the occurrence of random ﬂuctua-
tions in the disease dynamics from any of the sources-disease transmission or natural death
rates with intensity values σi > 0, i = S, E, I, β, destabilize the system from the equilibrium
state E1. Nevertheless, the solutions of the perturbed stochastic system (2.15)-(2.18) con-
tinue to oscillate near the nontrivial steady state E1, provided that the natural death rate µ
and the total removal by recovery, natural and disease related death rates (µ + d + α) sat-
isfy the conditions in (5.64). But, suﬃciently large values of σi > 0, i = S, E, I, β, that is,
σi →∞, i = S, E, I, β, imply from (5.64) and (5.65) that µ →∞, (µ + d + α) →∞, and
further imply that the solutions of (2.15)-(2.18) oscillate at much further distance away from
E1.
As a physical interpretation and deduction similar to Remark 5.3, these observations
above suggest that the presence of random ﬂuctuations in the malaria dynamics stemming
from the disease transmission or natural death rates leads to a persistent state of the disease
in the human population, where the population oscillates in character near the nonzero steady
state E1. Furthermore, for smaller intensity values of the random ﬂuctuations, the human
population also oscillates close to the nonzero steady state E1, and vice versa. But suﬃciently
large intensity values lead to very high natural and disease related death rates, that is, µ →∞,
and (µ + d + α) →∞, which postulate the fact that the human population goes extinct
asymptotically.
Indeed, while (5.65) indicates that larger intensity values of the random
ﬂuctuations lead to the human population oscillating further away from the nonzero steady
state E1 asymptotically, the numerical simulation results in Section 6 conﬁrm the proposition
that the human population becomes extinct asymptotically for suﬃciently large intensities of
the random ﬂuctuations.


## Page 80


80
These facts suggest that malaria control policies in the event where the disease is persis-
tent, should focus on reducing the intensities of the ﬂuctuations in the disease transmission
and natural death rates, perhaps through vector control and better care of the people in the
population, in order to reduce the number of deaths that may lead to human extinction by
the disease.
6. Example
It should be noted that some of the numerical examples discussed in this section are
utilized in various capacities elsewhere to address diﬀerent sub-objectives of the current on
going project. In this study, the examples presented below are used to facilitate understand-
ing about the inﬂuence of the noise in the system on the trajectories of the stochastic system
(2.15)-(2.18) relative to the equilibria of the stochastic/deterministic systems in Theorem 4.1
and Theorem 5.1.
6.1. Example 1: The eﬀect of the intensity of the white noise process on disease eradication:
This example illustrates the results in Theorem 4.4, Theorem 4.5 and Lemma 4.4, and
also provides numerical evidence in support of the results in Section 4 that characterize the
eﬀects of the intensity of the white noise processes in the system originating from the random
ﬂuctuations in the disease dynamics ( that is, from disease transmission and natural death
rates), on the stochastic asymptotic stability of the system in relation to the disease free
equilibrium E0 = (S∗
0, 0, 0), S∗
0 = B
µ . Recall, Theorem 4.4 and Lemma 4.4 provide conditions
for the threshold values R1, U0, and V0 deﬁned in (4.48)-(4.50) which are suﬃcient for the
stochastic stability of E0 and consequently for disease eradication. For simplicity in this
example, the following assumptions are considered:- (a1) there are no random ﬂuctuations
in the disease dynamics due to the natural death of susceptible individuals, that is, the
intensity of the white noise due to the random ﬂuctuations in the natural death of susceptible


## Page 81


81
individuals σS = 0. Indeed, from Theorem 4.4 and Lemma 4.4, there exists a stable disease
free equilibrium E0, whenever σS = 0 and the threshold values satisfy R1 ≤1, U0 ≤1, and
V0 ≤1. (a2) It is also assumed that the intensities of the white noise processes in the system
due to the random ﬂuctuations in the natural death and disease transmission rates for the
other disease classes-exposed, infectious and removal are equal, that is, σE = σI = σR =
σβ = σ.
The convenient list of system parameter values in Table 1 are used to generate diﬀerent
values for R1, U0, and V0 under continuous changes in the values of σ = σE = σI = σR = σβ.
The Figure 2 depicts the results for R1 and V0. For U0, it follows from Table 1 and (4.49)
that U0 ≈1, where ˜K(µ) = 0.999991.
Table 1: A list of speciﬁc values chosen for the system parameters for Example 1.
Disease transmission rate
β
6.277E −66
Constant Birth rate
B
22.39
1000
Recovery rate
α
5.5067E −07
Disease death rate
d
0.11838
Natural death rate
µ
0.6


## Page 82


82
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.5
1.0
1.5
(a) 
Intensity (σI = σβ = σ)
Basic reproduction ratio (R1)
0.000
0.001
0.002
0.003
0.004
0.005
0.006
0.999985
1.000005
(b)  
Intensity (σE)
Threshold value (V0)
Figure 2: (a) and (b) Show the values of the noise modiﬁed basic reproduction number, R1, (deﬁned in (4.48))
and the threshold parameter V0 (deﬁned in (4.50)) over continuous changes in the values of the intensities
of white noise processes due to random ﬂuctuations in natural death and disease transmission processes of
exposed, infectious and removal individuals, that is, σ = σE = σβ = σI = σR. The curves in (a) and (b)
show the values of R1 and V0 respectively. In addition, the broken horizontal lines depict the threshold
mark, 1, for the threshold values R1 and V0, where for the values of R1 and V0 below the threshold mark 1,
the disease free equilibrium E0 is stochastically asymptotically stable, and the disease can consequently be
eradicated. It is easy to see that low values of σ ∈[0, 0.7661] lead to R1 ≤1, and R1 > 1 other wise. For V0,
the low values of σ ∈[0, 0.0045] lead to V0 ≤1, and V0 > 1 other wise. Therefore, values for R1, U0, and V0
that satisfy R1 ≤1, U0 ≤1, and V0 ≤1 are achieved for very low values of σ. This observation signiﬁes that
for a disease scenario where the physical processes lead to the speciﬁc parameter values deﬁned in Table 1,
the disease can only be eradicated when the random ﬂuctuations in the disease dynamics exhibit very low
intensity values of σ ∈[0, 0.0045]. For any intensity values higher than 0.0045, the disease-free equilibrium
E0 is unstable, and this signiﬁes that the disease outbreak becomes naturally uncontrollable and establishes
either a stable endemic population E1, whenever the intensity value σ is small (see Theorem 5.3) or the
disease oscillates near the endemic population E1 as shown in Theorems [5.5 & 5.6].


## Page 83


83
6.2. Example 2: Eﬀect of the intensity of white noise on the trajectories of the system
The list of convenient choice of parameter values in Table 2 are used to generate the
trajectories of the stochastic system (2.15)-(2.18) in order to (1.) illustrate the impact of
the source of the white noise processes in the system (owing to the random ﬂuctuations
in the natural death or disease transmission rates) on the disease dynamics, and also to
(2.) illustrate the eﬀect of the intensity of the white noise processes in the system on the
trajectories of the diﬀerent disease classes (S, E, I, R) in the system.
These illustrations
also uncover the overall behavior of the stochastic system over time. The Euer-Maruyama
Table 2: A list of speciﬁc values chosen for the system parameters for Example 2.
Disease transmission rate
β
0.6277
Constant Birth rate
B
22.39
1000
Recovery rate
α
0.05067
Disease death rate
d
0.01838
Natural death rate
µ
0.002433696
Incubation delay time in vector
T1
2 units
Incubation delay time in host
T2
1 unit
Immunity delay time
T3
4 units
stochastic approximation scheme3 is used to generate trajectories for the diﬀerent states
S(t), E(t), I(t), R(t) over the time interval [0, T], where T = max(T1 + T2, T3) = 4. The
special nonlinear incidence functions G(I) =
aI
1+I , a = 0.05 in [9] is utilized to generate the
3A seed is set on the random number generator to reproduce the same sequence of random numbers for
the Brownian motion in order to generate reliable graphs for the trajectories of the system under diﬀerent
intensity values for the white noise processes, so that comparison can be made to identify diﬀerences that
reﬂect the eﬀect of intensity values.


## Page 84


84
numeric results. Furthermore, the following initial conditions are used

















S(t) = 10,
E(t) = 5,
I(t) = 6,
R(t) = 2,
∀t ∈[−T, 0], T = max(T1 + T2, T3) = 4.
(6.1)
The sample means for the sample paths of the S, E, I, R states generated over time t ∈[0, T]
are summarized in Table 3, and will be used to compare the eﬀect of the intensity values
of the white noise processes in the system on the trajectories of the system over time. The
Table 3:
Shows the intensity values of the white noise processes in the system and the corresponding sample
means for the trajectories of the S, E, I, R states generated over time t ∈[0, 4] in Example 2. The sample
means for S, E, I, R are denoted ¯S, ¯E, ¯I, ¯R respectively.
σi, i = S, E, I, R, β
Figure #
¯S
¯E
¯I
¯R
σi = 0, i = S, E, I, R, β
Figure 3
10.06048
4.979256
5.704827
1.975407
σi = 0, i = S, E, I, R, and σβ = 0.5
Figure 4
10.04129
4.978257
5.687113
1.973783
σi = 0, i = S, E, I, R, and σβ = 9
Figure 5
9.681482
4.906452
5.385973
1.94617
σi = 0.5, i = E, I, R, and σS = σβ = 0
Figure 6
10.06048
4.715779
5.42661
1.845652
σi = 0.5, i = S, E, I, R, and σβ = 0
Figure 7
9.553725
4.692877
5.42661
1.845652
σi = 9, i = S, E, I, R, and σβ = 0
Figure 8
1.980488
0.8066963
1.200498
0.240599
σi = 0.5, i = S, E, I, R, and σβ = 0.5
Figure 9
9.529665
4.687529
5.406493
1.843888
σi = 9, i = S, E, I, R, and σβ = 9
Figure 10
1.88787
0.4633994
0.8659143
0.2315721
following observations can be made from Table 3:
Remark 6.1.
1. When σi = 0, i = S, E, I, R, there is moderate decrease in the average values ¯S, ¯E, ¯I, ¯R of
S, E, I, R from the trajectories in Figures 3-5 as σβ increases from σβ = 0 to σβ = 9.
2. When σβ = 0, there is a sharp decrease in the average values ¯S, ¯E, ¯I, ¯R of S, E, I, R from
the trajectories in Figure 3, and Figures 7-8 as σi, i = S, E, I, R increases from σi = 0, i =
S, E, I, R to σi = 9, i = S, E, I, R.
3. When all the σi’s , that is, σi, i = S, E, I, R, β equally increase together from σi = 0, i =
S, E, I, R, β to σi = 9, i = S, E, I, R, β, there is a sharper decrease in the average values
¯S, ¯E, ¯I, ¯R of S, E, I, R from the trajectories in Figure 3, and Figures 9-10.


## Page 85


85
4. When σS = σβ = 0, there is no change in the average value ¯S of S and there is moderate
decrease in the average values ¯E, ¯I, ¯R of E, I, R from the trajectories in Figure 3 and Figure 6
as σi, i = E, I, R increases from σi = 0, i = E, I, R to σi = 0.5, i = E, I, R.
0
1
2
3
4
10.00
10.04
10.08
10.12
(c) Sample path for S(t)
time(t)
S(t)
0
1
2
3
4
4.96
4.97
4.98
4.99
5.00
 (d) Sample path for E(t) 
time(t)
E(t)
0
1
2
3
4
5.5
5.6
5.7
5.8
5.9
6.0
 (e) Sample path for I(t) 
time(t)
I(t)
0
1
2
3
4
1.93
1.95
1.97
1.99
 (f) Sample path for R(t)
time(t)
R(t)
Figure 3: (c), (d), (e) and (f) show the trajectories of the disease classes (S, E, I, R) respectively, when there
are no or only inﬁnitesimally small random ﬂuctuations in the disease dynamics, that is, when the intensities
of the white noise processes in the system due to random ﬂuctuations in the natural death and disease
transmission processes in all the classes (S, E, I, R) are described as follows: σS = σE = σβ = σI = σR = 0.


## Page 86


86
0
1
2
3
4
10.00
10.04
10.08
10.12
(g) Sample path for S(t)
time(t)
S(t)
0
1
2
3
4
4.96
4.97
4.98
4.99
5.00
 (h) Sample path for E(t) 
time(t)
E(t)
0
1
2
3
4
5.5
5.6
5.7
5.8
5.9
6.0
 (i) Sample path for I(t) 
time(t)
I(t)
0
1
2
3
4
1.93
1.95
1.97
1.99
 (j) Sample path for R(t)
time(t)
R(t)
Figure 4: (g), (h), (i) and (j) show the trajectories of the disease classes (S, E, I, R) respectively, when there
are no or only inﬁnitesimally small random ﬂuctuations in the disease dynamics from the natural death rate
of the classes (S, E, I, R), that is, when σS = σE = σI = σR = 0, but there are random ﬂuctuations in the
disease transmission process with low intensity value of σβ = 0.5.


## Page 87


87
0
1
2
3
4
9.2
9.4
9.6
9.8
10.0
(k) Sample path for S(t)
time(t)
S(t)
0
1
2
3
4
4.80
4.85
4.90
4.95
5.00
 (l) Sample path for E(t) 
time(t)
E(t)
0
1
2
3
4
4.8
5.2
5.6
6.0
 (m) Sample path for I(t) 
time(t)
I(t)
0
1
2
3
4
1.88
1.92
1.96
2.00
 (n) Sample path for R(t)
time(t)
R(t)
Figure 5: (k), (l), (m) and (n) show the trajectories of the disease classes (S, E, I, R) respectively, when
there are no or only inﬁnitesimally small random ﬂuctuations in the disease dynamics from the natural
death of the classes (S,E,I,R), that is, when σS = σE = σI = σR = 0, but there are random ﬂuctuations in
the disease transmission process with a high intensity value of σβ = 9. In addition, the broken line on the
sample path for S(t) in (k) depicts the S-coordinate S∗
0 = B
µ = 9.199999 for the disease free steady state
E0 = (S∗
0, 0, 0, 0), S∗
0 = B
µ , E∗
0 = 0, I∗
0 = 0, R∗
0 = 0.
The Figures 3-5 can be used to examine the eﬀect of increasing the intensity value of the
white noise process, σβ, originating from the random ﬂuctuations in the disease transmission
process on the trajectories for (S, E, I, R) in the absence of any signiﬁcant random ﬂuctu-
ations in the disease dynamics due to the natural death process for all the disease classes
(S, E, I, R), that is, σi = 0, i = S, E, I, R . It can be observed from Figure 3 that when the
intensity value σβ is inﬁnitesimally small, that is, σβ = 0, no signiﬁcant oscillations occur
over time on the trajectories for S, E, I, R in (a), (b), (c) and (d) respectively. Further-
more, for signiﬁcant but low intensity values for σβ, that is, σβ = 0.5, Figure 4 shows that


## Page 88


88
some signiﬁcant oscillations occur on the trajectories for the susceptible (g) and infectious
(i) populations. Moreover, the size of the oscillations observed on the trajectories for the
susceptible (g) and infectious population (i) seem to be small in value over time compared
to Figure 5. In addition, no signiﬁcant oscillations are observed on the trajectories for the
exposed (h) and removal (j) populations. In Figure 5, with an increase in the intensity value
for σβ to σβ = 9, more disease classes exhibit signiﬁcant oscillations on their trajectories, for
instance, more signiﬁcant sized oscillations are observed on the trajectory of one additional
class- exposed population (l) than is observed in Figure 4 (h). Moreover, it appears that the
high intensity value σβ = 9 has increased the size of the oscillations in the susceptible (k)
and infectious (m) populations, and further deviating the trajectories of the system away
from the noise-free state in Figure 3. In addition, the trajectories for the states- (S, E, I)
in Figure 5 (k), (l), (m) respectively, oscillate near the disease free state E0 = (S∗
0, 0, 0, 0),
where S∗
0 = B
µ = 9.199999, E∗
0 = 0, I∗
0 = 0, R∗
0 = 0.
One can also observe from Table 3 and Remark 6.1 that for small values σi = 0, i =
S, E, I, R, the average values of S, E, I, R over time on the trajectories in Figures 3-5 decrease
continuously with increase in the intensity value of σβ from σβ = 0 to σβ = 9.
These
observations related to the oscillatory behavior of the system, for example, comparing the
trajectory of S in Figure 3(c), Figure 4(g) and Figure 5(k), and also comparing the trajectory
for I in Figure 3(e), Figure 4(i) and Figure 5(m) suggest that continuously increasing the
intensity value for σβ tends to increase the oscillatory behavior of the trajectories of the
system that results in an average decrease in the size of the susceptible, exposed, infectious
and removal populations over time. Furthermore, the size of the oscillations in the system
is proportional to the size of the intensity values of the white noise process as remarked in
Remark 4.5.


## Page 89


89
0
1
2
3
4
10.00
10.04
10.08
10.12
(o) Sample path for S(t)
time(t)
S(t)
0
1
2
3
4
4.4
4.6
4.8
5.0
 (p) Sample path for E(t) 
time(t)
E(t)
0
1
2
3
4
5.0
5.2
5.4
5.6
5.8
6.0
 (q) Sample path for I(t) 
time(t)
I(t)
0
1
2
3
4
1.70
1.80
1.90
2.00
 (r) Sample path for R(t)
time(t)
R(t)
Figure 6: (o), (p), (q) and (r) show the trajectories of the disease classes (S, E, I, R) respectively, when
there are signiﬁcant small random ﬂuctuations in the disease dynamics from the natural death process of
exposed, infectious and removal classes, with intensity value σE = σI = σR = 0.5, but there are no or only
inﬁnitesimally small ﬂuctuations in the disease dynamics due to the disease transmission and natural death
processes of susceptible individuals, that is, σS = σβ = 0.
Figure 3 , Figure 6, and Figure 7 can be used as an example to examine the eﬀect
of the intensity of the white noise process, σi, i = S, E, I, R, originating from the random
ﬂuctuations in the natural death process of each class-S, E, I, R, on the trajectories of the
system, in the absence of any signiﬁcant ﬂuctuation in the disease dynamics owing to the
disease transmission process, that is, σβ = 0. For example, to examine the eﬀect of σβ for the
susceptible class, S, on the trajectories of the stochastic stochastic system, observe that in
Figure 6, when σS = σβ = 0 and σi = 0.5, i = E, I, R, no signiﬁcant oscillations occur on the
trajectories of S in Figure 6(o) and also on Figure 3(c). Furthermore, when σS is increased to
σS = 0.5, Figure 7(s) depicts signiﬁcant sized oscillations on the trajectory of S. Moreover,


## Page 90


90
the trajectory for S oscillates near the disease free steady state S∗
0 = 9.199999. It can be
further observed using Table 3 and Remark 6.1 that no major diﬀerences have occurred on
the trajectories of the other states E, I, R in both Figure 6(p),(q),(r) and Figure 7(t),(u),(v)
respectively. In addition, it can be seen from Table 3 and Remark 6.1 that when σβ = 0, the
increase in the intensity value of σS from σS = 0 to σS = 0.5 on average leads to a decrease
in the susceptible population size over time in Figure 7(s) than it is observed in Figure 6(o)
and Figure 3(c). These observations suggest that in the absence of random ﬂuctuations in
the disease dynamics from the disease transmission process, that is, σβ = 0, the intensity
of the white noise process, σS, owing to the natural death of the susceptible class S, (1.)
exhibits a signiﬁcant eﬀect primarily on its trajectory, and (2.) the eﬀect of increasing the
intensity value of σS leads to an oscillatory behavior on the trajectory of S that decreases
the susceptible population averagely over time. Note that a similar numerical and graphical
diagnostic approach can be used to examine the eﬀects of the other classes E, I, R, whenever
σβ = 0.


## Page 91


91
0
1
2
3
4
9.0
9.4
9.8
10.2
(s) Sample path for S(t)
time(t)
S(t)
0
1
2
3
4
4.4
4.6
4.8
5.0
 (t) Sample path for E(t) 
time(t)
E(t)
0
1
2
3
4
5.0
5.2
5.4
5.6
5.8
6.0
 (u) Sample path for I(t) 
time(t)
I(t)
0
1
2
3
4
1.70
1.80
1.90
2.00
 (v) Sample path for R(t)
time(t)
R(t)
Figure 7: (s), (t), (u) and (v) show the trajectories of the disease classes (S, E, I, R) respectively, when
there are signiﬁcant but small random ﬂuctuations in the disease dynamics from the natural death process
in all the disease classes- susceptible, exposed, infectious and removal classes with low intensity value of
σS = σE = σI = σR = 0.5, but there are no or only inﬁnitesimally small ﬂuctuations in the disease
dynamics from the disease transmission process, that is, σβ = 0.
In addition, the broken line on the
sample path for S(t) in (s) depicts the S-coordinate S∗
0 = B
µ = 9.199999 for the disease free steady state
E0 = (S∗
0, 0, 0, 0), S∗
0 = B
µ , E∗
0 = 0, I∗
0 = 0, R∗
0 = 0.


## Page 92


92
0
1
2
3
4
0
2
4
6
8
10
12
(w) Sample path for S(t)
time(t)
S(t)
0
1
2
3
4
0
1
2
3
4
5
6
 (x) Sample path for E(t) 
time(t)
E(t)
0
1
2
3
4
0
1
2
3
4
5
6
7
 (y) Sample path for I(t) 
time(t)
I(t)
0
1
2
3
4
−0.5
0.5
1.5
 (z) Sample path for R(t)
time(t)
R(t)
Figure 8: (w), (x), (y) and (z) show the trajectories of the disease classes (S, E, I, R) respectively, when there
are signiﬁcant and large random ﬂuctuations in the disease dynamics from the natural death process in all
the disease classes- susceptible, exposed, infectious and removal classes with suﬃciently high intensity value
of σS = σE = σI = σR = 9, but there are no or only inﬁnitesimally small ﬂuctuations in the disease dynamics
from the disease transmission process, that is, σβ = 0. In addition, the broken line on the sample paths for
S(t), E(t), I(t) and R(t) depict the S, E, I, R-coordinates S∗
0 = B
µ = 9.199999, E∗
0 = 0, I∗
0 = 0, R∗
0 = 0 for
the disease free steady state E0 = (S∗
0, 0, 0, 0), S∗
0 = B
µ , E∗
0 = 0, I∗
0 = 0, R∗
0 = 0. (w), (x), (y) and (z) also
show that the population goes extinct over time due to the high intensity of the white noise.
Figure 3, Figure 7 and Figure 8 can be used to examine the eﬀect of increasing the
intensity value of the white noise process originating from the natural death, σi, i = S, E, I, R,
in the absence of any signiﬁcant random ﬂuctuations in the disease dynamics from the disease
transmission process, that is, when σβ = 0. Figure 7 (s),(t),(u),(v) show that the trajectories
for S, E, I, R respectively, oscillate near the disease free equilibrium E0 = (9.199999, 0, 0, 0)
over time when the intensity value is increased from σi = 0, i = S, E, I, R to σi = 0.5, i =


## Page 93


93
S, E, I, R than is observed in the Figure 3 (c), (d), (e), (f). Furthermore, the oscillations on
the trajectories seem to be small in size over time. When the intensity value, σi, i = S, E, I, R,
is further increased to σi = 9, i = S, E, I, R, the oscillations on the trajectories in Figure 8
(w),(x),(y),(z), appear to have increased in size.
Furthermore, Table 3 and Remark 6.1
show that the oscillations lead to a decrease in the average values of S, E, I, R over time,
and further away from the disease free state of S∗
0 = 9.199999. Moreover, the population
rapidly becomes extinct over time.
These observations suggest that the increase in the
intensity value of the white noise due to natural death in all classes, σi, i = S, E, I, R, in the
population (1.)leads to an increase in the oscillatory behavior of the system which decreases
the population size averagely over time and also (2.)leads to population extinction over time.
Note that this observation is consistent with the results of Theorem 4.6, whenever σS is large
magnitude.


## Page 94


94
0
1
2
3
4
8.8
9.2
9.6
10.0
(a1) Sample path for S(t)
time(t)
S(t)
0
1
2
3
4
4.4
4.6
4.8
5.0
 (b1) Sample path for E(t) 
time(t)
E(t)
0
1
2
3
4
5.0
5.4
5.8
 (c1) Sample path for I(t) 
time(t)
I(t)
0
1
2
3
4
1.70
1.80
1.90
2.00
 (d1) Sample path for R(t)
time(t)
R(t)
Figure 9: (a1), (b1), (c1) and (d1) show the trajectories of the disease classes (S, E, I, R) respectively,
when there are signiﬁcant but small random ﬂuctuations in the disease dynamics from the natural death
process in all the disease classes- susceptible, exposed, infectious and removal classes with low intensity
value of σS = σE = σI = σR = 0.5, and there are also signiﬁcant ﬂuctuations in the disease dynamics
from the disease transmission with a low intensity value of σβ = 0.5. In addition, the broken line on the
sample path for S(t) in (a1) depicts the S-coordinate S∗
0 = B
µ = 9.199999 for the disease free steady state
E0 = (S∗
0, 0, 0, 0), S∗
0 = B
µ , E∗
0 = 0, I∗
0 = 0, R∗
0 = 0.


## Page 95


95
0
1
2
3
4
0
2
4
6
8
10
12
(e1) Sample path for S(t)
time(t)
S(t)
0
1
2
3
4
−1
0
1
2
3
4
5
6
 (f1) Sample path for E(t) 
time(t)
E(t)
0
1
2
3
4
0
2
4
6
 (g1) Sample path for I(t) 
time(t)
I(t)
0
1
2
3
4
−0.5
0.5
1.5
 (h1) Sample path for R(t)
time(t)
R(t)
Figure 10: (e1), (f1), (g1) and (h1) show the trajectories of the disease classes (S, E, I, R) respectively, when
there are signiﬁcant and large random ﬂuctuations in the disease dynamics from the natural death process in
all the disease classes- susceptible, exposed, infectious and removal classes with a suﬃciently high intensity
value of σS = σE = σI = σR = 9, and there are also signiﬁcant ﬂuctuations in the disease dynamics from the
disease transmission process with a suﬃciently high intensity value of σβ = 9. In addition, the broken line
on the sample paths for S(t), E(t), I(t) and R(t) depict the S, E, I, R-coordinates S∗
0 = B
µ = 9.199999, E∗
0 =
0, I∗
0 = 0, R∗
0 = 0 for the disease free steady state E0 = (S∗
0, 0, 0, 0), S∗
0 =
B
µ , E∗
0 = 0, I∗
0 = 0, R∗
0 = 0.
Furthermore, (e1), (f1), (g1) and (h1) show that the population goes extinct over time due to the high
intensity of the white noise.
Figure 3, Figure 9 and Figure 10 can be used to examine the eﬀect of increasing the
intensity values, σi, i = S, E, I, R, β, of all the white noise processes in the system on the tra-
jectories of the system. Figure 9 (a1),(b1),(c1),(d1) show that the trajectories for S, E, I, R
respectively oscillate near the disease free steady state E0 = (9.199999, 0, 0, 0) over time when
the intensity value is increased from σi = 0, i = S, E, I, R, β to σi = 0.5, i = S, E, I, R, β


## Page 96


96
than it is observed in Figure 3(c),(d),(e),(f). Furthermore, the oscillations of the trajectories
seem to be small in size compared to the corresponding trajectories in Figure 10. When the
intensity values of σi, i = S, E, I, R, β are further increased to σi = 9, i = S, E, I, R, it can be
seen from Figure 10(e1),(f1),(g1),(h1), Table 3 and Remark 6.1 that the oscillations increase
in size and lead to a sharp decrease in the average values of S, E, I, R on their trajectories
over time, and also further deviating the average susceptible population size away from the
disease free state of S∗
0 = 9.199999. Moreover, the population rapidly becomes extinct over
time. These observations suggests that the increase in the intensity value of the white noise
processes in the system due to the random ﬂuctuations in the disease dynamics originating
from the disease transmission and natural death processes for all disease classes in the pop-
ulation leads to (1.) an increase in the oscillatory behavior of the system which decreases
the average total population size over time, and also leads to (2.) the rapid extinction of the
population over time.
It can also be observed by comparing Figure 8(w),(x),(y),(z), and Figure 10(e1),(f1),(g1),(h1),
that for a ﬁxed value of σi = 9, i = S, E, I, R, if σβ increases from σβ = 0 in Fig-
ure 8(w),(x),(y),(z) to σβ = 9 in Figure 10(e1),(f1),(g1),(h1), then the population more
rapidly becomes extinct than it is observed in Figure 8(w),(x),(y),(z).
Indeed, in Fig-
ure 8(w),(x),(y),(z), the trajectories for the susceptible S, exposed E, infectious I and
Removal R states go extinct at approximately the following times t = 2, t = 1.8, t = 2
and t = 1.8 respectively.
Meanwhile, in Figure 10(e1),(f1),(g1),(h1), the trajectories for
susceptible S, exposed E, infectious I and Removal R go extinct earlier at the approximate
times t = 1.5, t = 1, t = 1 and t = 1.4 respectively. Note that this observation is consistent
with the results of Theorem 4.6, whenever σS is large in magnitude.
The following pairs of ﬁgures:- (Figure 4 (g),(h),(i),(j) & Figure 5 (k),(l),(m),(n)) and (


## Page 97


97
Figure 7 (s),(t),(u),(v) & Figure 8 (w),(x),(y),(z)), can be used with reference to Figure 3, to
examine and compare the two major sources of random ﬂuctuations in the disease dynamics
namely-natural death and disease transmission processes, in order to determine the source
which has stronger eﬀect on the trajectories of the system, whenever the intensity values of
the white noise processes increase in value. In the absence of random ﬂuctuations in the
natural death process, that is, σi = 0, i = S, E, I, R, as the intensity value of σβ is increased
from σβ = 0.5 to σβ = 9, the pair of ﬁgures (Figure 4 (g),(h),(i),(j) & Figure 5 (k),(l),
(m),(n)) show an increase in the oscillatory behavior on the trajectories of the system which
is more signiﬁcant in size for the S and I classes over time. Furthermore, the oscillatory
behavior leads to a decrease in the average susceptible and infectious populations over time
than it is observed in Figure 3 (c) and Figure 3(e) respectively, as shown in Table 3 and
Remark 6.1. Moreover, the general disease population does not go extinct over time.
Meanwhile, in the absence of random ﬂuctuations in the disease transmission process, that
is, σβ = 0, the increase in the intensity value of σi, i = S, E, I, R from σi = 0.5, i = S, E, I, R
to σi = 9, i = S, E, I, R, the pair of ﬁgures ( Figure 7(s),(t),(u),(v) & Figure 8(w),(x),(y),(z))
show very strong increase in the oscillatory behavior on the trajectories of the system which
is signiﬁcant in all the states- S, E, I and R . Furthermore, from Table 3 and Remark 6.1,
it can be seen that the oscillatory behavior of the system leads to a rapid decrease in the
average values of all the states-S, E, I and R over time, with the mean susceptible population
size deviating much further away from the disease free steady state S∗
0 = 9.199999, than it
is observed in Figure 3. Moreover, the disease population goes extinct over time with the
increase in the intensity value of σi, i = S, E, I, R.


## Page 98


98
7. Conclusion
The presented class of stochastic and deterministic SEIRS epidemic dynamic models with
nonlinear incidence rates, three distributed delays and random perturbations characterizes
the general dynamics of vector-borne diseases such as malaria and dengue fever, that are
inﬂuenced by random environmental ﬂuctuations from (1.) the disease transmission rate
between susceptible humans and infectious vectors mainly mosquitoes, and also from (2.)
the natural death rates in the sub-categories - susceptible, exposed, infectious and removal
individuals of the human population.
Moreover, the random ﬂuctuations in the disease
dynamics are incorporated into the epidemic dynamic models via white noise or Wiener
processes. Furthermore, the three delays are random variables. Whereas, two of the delays
represent the incubation periods of the infectious agent mainly the malaria parasites or
dengue fever virus in the vector and human being, the third delay represents the period of
eﬀective naturally acquired immunity against the disease, which is conferred to individuals
after recovery from infection. This study presents two classes of epidemic dynamic models,
one represented as a system of Ito-Doob type stochastic diﬀerential equations, and the other
represented as a system of ordinary diﬀerential equations, where the class type is determined
by a general nonlinear incidence function G, satisfying a set of mathematical conditions. The
nonlinear incidence function G can be used to characterize the nonlinear character of disease
transmission rates for disease scenarios that exhibit a striking initial increase or decrease in
disease transmission rates which become steady or bounded as the infectious population size
grows and becomes large.
Comparative conditions and threshold values pertaining to both stochastic and deter-
ministic systems that are suﬃcient for the existence of unique global positive solutions, and
other asymptotic properties are presented. For instance, detailed results that characterize


## Page 99


99
the asymptotic behavior of the trajectories or solutions of the stochastic and deterministic
dynamic systems are presented namely:- (1.) the existence and asymptotic stochastic sta-
bility of feasible equilibria of the systems- disease free E0 and endemic E1 steady states,
and (2.) the asymptotic oscillatory character of the solutions of the stochastic system near
the potential steady states- disease-free and endemic equilibria of the deterministic system.
In addition, comparative threshold values for the stochastic and deterministic stability of
the disease free steady state, and consequently for disease eradication, such as the noise de-
pendent and noise-free basic reproduction numbers for the disease dynamics are computed.
Moreover, the threshold values are exhibited for special cases when the delay times in the
system are both constant and random.
The results from the comparative asymptotic analyses of the stochastic and deterministic
systems suggest that the source (disease transmission or natural death rates ) and size of
the intensity values of the white noise processes in the system exhibit direct consequences on
the overall qualitative behavior of the class of epidemic dynamic models with respect to the
equilibria of the systems. For example, (1.) the existence and stability of the disease free and
endemic steady state populations of the epidemic dynamic models, and their consequences
on disease eradication or persistence depend on the source and intensity of the white noise
processes in the system, (2) the oscillatory character of the sample paths of the stochastic
system near the disease free and endemic equilibria, and the consequences on the persistence
of the disease in the population also depend on the source and intensity of the white noise
processes in the system.
Further thorough numerical examination of the asymptotic properties of the trajectories
of the stochastic and deterministic systems under the inﬂuence of various intensity levels of
the white noise processes in the system is conducted. The numerical simulation results sug-


## Page 100


100
gest that higher intensity values of the white processes in the system drive the sample paths
of the stochastic system further away from the common deterministic and stochastic disease
free steady state, and also further away from the endemic equilibrium of the deterministic
system. Moreover, the population seems to become extinct over time, whenever the intensity
values of the white noise processes become large.


## Page 101


101
8. References
References
[1] Cooke, Kenneth L. Stability analysis for a vector disease model. Rocky Mountain
Journal of Mathematics 9 (1979), no. 1, 31-42
[2] Y. Takeuchi, W. Ma and E. Beretta, Global asymptotic properties of a delay SIR
epidemic model with ﬁnite incubation times, Nonlinear Anal. 42 (2000), 931-947.
[3] E. Beretta, V. Kolmanovskii, L. Shaikhet, Stability of epidemic model with time delay
inﬂuenced by stochastic perturbations, Mathematics and Computers in Simulation 45
(1998) 269-277
[4] Vincenzo Capasso, Mathematical Structures of Epidemic Systems, Lecture Notes in
Biomathematics,Volume 97 1993
[5] Liu WM, Hethcote HW, Levin SA.Dynamical behavior of epidemiological models with
nonlinear incidence rates.J.Math Biol 1987; 25:359
[6] Capasso V, Serio G.A. A generalization of the Kermack-Mckendrick deterministic epi-
demic model. Math Biosc 1978; 42:43
[7] D. Xiao, S. Ruan, Global analysis of an epidemic model with nonmonotone incidence
rate. Math Biosci. 2007 Aug;208(2):419-29
[8] Huo, Hai-Feng; Ma, Zhan-Ping, Dynamics of a delayed epidemic model with non-
monotonic incidence rate,Communications in Nonlinear Science and Numerical Simu-
lation, Volume 15, Issue 2, p. 459-468.


## Page 102


102
[9] S.M. Moghadas, A.B. Gumel, Global Statbility of a two-stage epidemic model with
generalized nonlinear incidence, Mathematics and computers in simulation 60 (2002),
107-118
[10] Yuliya N. Kyrychko, Konstantin B. Blyussb, Global properties of a delayed SIR model
with temporary immunity and nonlinear incidence rate, Nonlinear Analysis: Real
World Applications Volume 6, Issue 3, July 2005, Pages 495507
[11] Qun Liu, Daqing Jiang, Ningzhong Shi, Tasawar Hayat, Ahmed Alsaedi, Asymptotic
behaviors of a stochastic delayed SIR epidemic model with nonlinear incidence, Com-
munications in Nonlinear Science and Numerical Simulation Volume 40, November
2016, Pages 89-99.
[12] Q. Liu, Q. Chen Analysis of the deterministic and stochastic SIRS epidemic models
with nonlinear incidence Physica A, 428 (2015), pp. 140153
[13] Cooke KL, van den Driessche P., Analysis of an SEIRS epidemic model with two delays,
J Math Biol. 1996 Dec;35(2):240-60.
[14] Nguyen Huu Du, Nguyen Ngoc Nhu, Permanence and extinction of certain stochastic
SIR models perturbed by a complex type of noises, Applied Mathematics Letters 64
(2017) 223230
[15] Joaquim P. Mateusa, , Csar M. Silvab, Existence of periodic solutions of a periodic
SEIRS model with general incidence, Nonlinear Analysis: Real World Applications
Volume 34, April 2017, Pages 379402
[16] M. De la Sena, S. Alonso-Quesadaa, A. Ibeasb, On the stability of an SEIR epidemic


## Page 103


103
model with distributed time-delay and a general class of feedback vaccination rules,
Applied Mathematics and Computation Volume 270, 1 November 2015, Pages 953976
[17] Zhichao Jianga, b, Wanbiao Mab, Junjie Wei, Global Hopf bifurcation and perma-
nence of a delayed SEIRS epidemic model, Mathematics and Computers in Simulation
Volume 122, April 2016, Pages 3554
[18] Joaquim P. Mateus, Csar M. Silva, A non-autonomous SEIRS model with general
incidence rate , Applied Mathematics and Computation Volume 247, 15 November
2014, Pages 169189
[19] M. De la Sen, S. Alonso-Quesada, , A. Ibeas, On the stability of an SEIR epidemic
model with distributed time-delay and a general class of feedback vaccination rules,
Applied Mathematics and Computation Volume 270, 1 November 2015, Pages 953976
[20] Shujing Gao, Zhidong Teng, Dehui Xie, The eﬀects of pulse vaccination on SEIR model
with two time delays, Applied Mathematics and Computation Volume 201, Issues 1-2,
15 July 2008, Pages 282-292
[21] B. G. Sampath Aruna Pradeep , Wanbiao Ma, Global Stability Analysis for Vector
Transmission Disease Dynamic Model with Non-linear Incidence and Two Time Delays,
Journal of Interdisciplinary Mathematics, Volume 18, 2015 - Issue 4
[22] Zhenguo Bai, Yicang Zhou, Global dynamics of an SEIRS epidemic model with periodic
vaccination and seasonal contact rate, Nonlinear Analysis: Real World Applications
Volume 13, Issue 3, June 2012, Pages 1060-1068
[23] Yanli Zhou, Weiguo Zhang, Sanling Yuan, Hongxiao Hu, Persistence And Extinction


## Page 104


104
In Stochastic Sirs Models With General Nonlinear Incidence Rate, Electronic Journal
of Diﬀerential Equations, Vol. 2014 (2014), No. 42, pp. 1-17.
[24] Eric Avila, ValesBruno Buonomo, Analysis of a mosquito-borne disease transmission
model with vector stages and nonlinear forces of infection, Ricerche di Matematica
November 2015, Volume 64, Issue 2, pp 377-390
[25] S. Syafruddin, Mohd Salmi Md. Noorani, Lyapunov function of SIR and SEIR model for
transmission of dengue fever disease, International Journal of Simulation and Process
Modelling (IJSPM), Vol. 8, No. 2-3, 2013
[26] Liuyong Pang, Shigui Ruan, Sanhong Liu , Zhong Zhao , Xinan Zhang, Transmis-
sion dynamics and optimal control of measles epidemics, Applied Mathematics and
Computation 256 (2015) 131147
[27] Ling ZhuHongxiao Hu, A stochastic SIR epidemic model with density dependent birth
rate, Advances in Diﬀerence Equations December 2015, 2015:330
[28] G.S. Ladde, V. Lakshmikantham, Random Diﬀerential Inequalities, Academic press,
New York, 1980
[29] R. Ross, The Prevention of Malaria, John Murray, London, 1911.
[30] Macdonald, G., The analysis of infection rates in diseases in which superinfection
occurs. Trop. Dis. Bull. 47, 907-915
[31] G. A. Ngwa, W. Shu, A mathematical model for endemic malaria with variable human
and mosquito population, Math. computer. model. 32, 747-763


## Page 105


105
[32] Hyun, M.Y., Malaria transmission model for diﬀerent levels of acquired immunity and
temperature dependent parameters (vector). Rev. Saude Publica 2000, 34 (3), 223231
[33] Anderson, R.M., May, R.M., Infectious Diseases of Humans: Dynamics and Control.
Oxford University Press, Oxford, 1991.
[34] G.A. Ngwa, A.M. Niger, A.B. Gumel, Mathematical assessment of the role of non-
linear birth and maturation delay in the population dynamics of the malaria vector,
Appl. Math. Comput. 217 (2010) 3286.
[35] Ngonghala CN, Ngwa GA, Teboh-Ewungkem MI, Periodic oscillations and backward
bifurcation in a model for the dynamics of malaria transmission. Math Biosci(2012),
240(1):4562
[36] N. Chitnis, J.M. Hyman, J.M. Cushing, Determining important parameters in the
spread of malaria through the sensitivity analysis of a mathematical model, Bull. Math.
Biol. 70 (2008) 1272.
[37] M.I. Teboh-Ewungkem, T. Yuster, A within-vector mathematical model of plasmodium
falciparum and implications of incomplete fertilization on optimal gametocyte sex ratio,
J. Theory Biol. 264 (2010) 273.
[38] D. Wanduku, Complete Global Analysis of a Two-Scale Network SIRS Epidemic Dy-
namic Model with Distributed Delay and Random Perturbation, Applied Mathematics
and Computation Vol. 294 (2017) p. 49 - 76
[39] D. Wanduku, G.S. Ladde, Global properties of a two-scale network stochastic de-
layed human epidemic dynamic model, nonlinear Analysis: Real World Applications
13(2012)794-816


## Page 106


106
[40] D. Wanduku, G.S. Ladde, The global analysis of a stochastic two-scale Network Hu-
man Epidemic Dynamic Model With Varying Immunity Period, Journal of Applied
Mathematics and Physics, 2017, 5, 1150-1173
[41] D. Wanduku and G.S. Ladde Global Stability of Two-Scale Network Human Epidemic
Dynamic Model, Neural, Parallel, and Scientiﬁc Computations 19 (2011) 65-90
[42] D. Wanduku, G.S. Ladde , Fundamental Properties of a Two-scale Network stochas-
tic human epidemic Dynamic model, Neural, Parallel, and Scientiﬁc Computations
19(2011) 229-270
[43] M. Xuerong, Stochastic diﬀerential equations and applications Horwood Publishing
Ltd.(2008), 2nd ed.
[44] G.S., Ladde, Cellular Systems-II. Stability of Campartmental Systems. Math. Biosci.
30(1976), 1-21
[45] James M. Crutcher, Stephen L. Hoﬀman, Malaria, Chapter 83-malaria, Medical Micro-
biology, 4th edition, Galveston (TX): University of Texas Medical Branch at Galveston;
1996.
[46] http://www.who.int/denguecontrol/human/en/
[47] https://www.cdc.gov/malaria/about/disease.html
[48] L. Hviid, Naturally acquired immunity to Plasmodium falciparum malaria ,Acta Trop-
ica 95(3):270-5, October 2005
[49] Denise L. Doolan, Carlota Dobano,J. Kevin Baird, Acquired Immunity to Malaria,
clinical microbiology reviews,Vol. 22, No. 1, Jan. 2009, p. 1336


## Page 107


107
[50] Yakui Xue And Xiafeng Duan, Dynamic Analysis Of An Sir Epidemic Model With
Nonlinear Incidence Rate And Double Delays, International Journal Of Information
And Systems Sciences (2011)Volume 7, Number 1, Pages 92102
[51] Yoshiaki Muroya , Yoichi Enatsu, Yukihiko Nakata,Global stability of a delayed SIRS
epidemic model with a non-monotonic incidence rate, Journal of Mathematical Anal-
ysis and Applications Volume 377, Issue 1, 1 May 2011, Pages 114
[52] W.M. Liu, H.W. Hethcote, S.A. Levin, Dynamical behavior of epidemiological models
with nonlinear incidence rates, J. Math. Biol. 25 (4) (1987) 359380
[53] A. Korobeinikov, P.K. Maini, A Lyapunov function and global properties for SIR and
SEIR epidemiological models with nonlinear incidence, Math. Biosci. Eng. 1 (1) (2004)
5760.
[54] Chen, L, Chen, J., Nonlinear Biologiical Dynamical System, beijing, Science Press,
1993.
[55] Y. Kuang, delay Diﬀerential Equations with Applications in population Dynamics,
Academic Press, boston. 1993
[56] D. Wanduku, G.S. Ladde, Global stability of a two-scale network SIR delayed epidemic
dynamic model Proceedings of Dynamic Systems and Applications 6 (2012) 437441
[57] D. Wanduku, Two-Scale Network Epidemic Dynamic Model for Vector Borne Diseases,
Proceedings of Dynamic Systems and Applications 6 (2016) 228232


## Page 108


0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.5
1.0
1.5
(a) 
Intensity (σI)
Basic reproduction ratio (R1)
0.000
0.001
0.002
0.003
0.004
0.005
0.006
0.999985
1.000005
(b)  
Intensity (σE)
Threshold value (V0)


## Page 109


0
1
2
3
4
9.0
10.0
11.0
Solution for S(t) over [0,T], T=4
t
S(t)
0
1
2
3
4
5.0
5.5
6.0
6.5
Solution for E(t) over [0,T], T=4
t
E(t)
0
1
2
3
4
5.8
6.0
6.2
6.4
6.6
6.8
Solution for I(t) over [0,T], T=4
t
I(t)
0
1
2
3
4
2.0
2.2
2.4
2.6
Solution for R(t) over [0,T], T=4
t
R(t)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1809_03897v1_a_comparative_stochastic_and_deterministic_study_of_a_class_of_epidemic_dynamic
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1809_03897V1_A_COMPARATIVE_STOCHASTIC_AND_DETERMINISTIC_STUDY_OF_A_CLASS_OF_EPIDEMIC_DYNAMIC.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1808.09842v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1808.09842v1_Analyzing_the_qualitative_properties_of_white_noise_on_a_family_of_infectious_di

> Source: 1808.09842v1_Analyzing_the_qualitative_properties_of_white_noise_on_a_family_of_infectious_di.pdf

> Pages: 95

---


## Page 1


arXiv:1808.09842v1  [q-bio.PE]  29 Aug 2018
Analyzing the qualitative properties of white noise on a family of
infectious disease models in a highly random environment
Divine Wanduku
Department of Mathematical Sciences, Georgia Southern University, 65 Georgia Ave, Room 3042,
Statesboro, Georgia, 30460, U.S.A. E-mail:dwanduku@georgiasouthern.edu;wandukudivine@yahoo.com1
Abstract
A class of stochastic vector-borne infectious disease models is derived and studied. The class
type is determined by a general nonlinear incidence rate of the disease. The disease spreads
in a highly random environment with variability from the disease transmission and natural
death rates. Other sources of variability include the random delays of disease incubation
inside the vector and the human being, and also the random delay due to the period of
eﬀective acquired immunity against the disease. The basic reproduction number and other
threshold conditions for disease eradication are computed.
The qualitative behaviors of
the disease dynamics are examined under the diﬀerent sources of variability in the system.
A technique to classify the diﬀerent levels of the intensities of the noises in the system is
presented, and used to investigate the qualitative behaviors of the disease dynamics in the
infection-free steady state population under the diﬀerent intensity levels of the white noises
in the system. Moreover, the possibility of population extinction, whenever the intensities
of the white noises in the system are high is examined. Numerical simulation results are
presented to elucidate the theoretical results.
Keywords:
Disease-free steady state, Stochastic stability, Basic reproduction number,
1Corresponding author. Tel: +14073009605.
Preprint submitted to Elsevier
August 30, 2018


## Page 2


2
Lyapunov functional technique, Intensity of white noise
1. Introduction
In the general class of infectious diseases, vector-borne diseases exhibit several unique
biological characteristics. For instance, the incubation of the disease requires two hosts -
the vector and human hosts, which may be either directly involved in a full life cycle of
the infectious agent consisting of two separate and independent segments of sub-life cycles
which are completed separately inside the two hosts, or directly involved in two separate
and independent half-life cycles of the infectious agent in the hosts. Therefore, there exists
a total latent time lapse of disease incubation which extends over the two segments of delay
incubation times namely:- (1) the incubation period of the infectious agent ( or the half-life
cycle) inside the vector, and (2) the incubation period of the infectious agent (or the other
half-life cycle) inside the human being. For example, the dengue fever virus transmitted pri-
marily by the Aedes aegypti and Aedes albopictus mosquitos undergoes two delay incubation
periods:- (1) about 8-12 days incubation period inside the female mosquito vector, which
starts immediately after the ingestion of a dengue fever virus infected blood meal, which is
successfully taken from a dengue fever infectious human being via a mosquito bite, and (2)
another delay incubation period of about 2-7 days in the human being when the hosting
female infectious vector bites a susceptible human being, whereby the virus is successfully
transmitted from the infectious mosquito to the susceptible person. See [46, 47].
Indeed, for dengue fever transmission, a susceptible vector acquires infected blood meal
from a dengue fever infectious person via a mosquito bite.
The virus incubates in the
mosquito for about 8-12 days, and at the end of the ﬁrst incubation period the exposed
mosquito becomes infectious. The virus is transferred to a susceptible human being after
another successful mosquito bite, and it subsequently undergoes a second incubation phase


## Page 3


3
in the exposed human being. The second incubation phase is mostly a viremia phase that
involves the complete circulation of the virus in the human blood stream, and at the end of
the phase the exposed person develops full blown fever. See [46, 47].
While the infectious dengue fever vector is known to stay infectious for the rest of the
life span, it is important to note in the modelling of the vector-borne disease dynamics
that no relationship between vector survival and viral invasion of the mosquito has been
determined[46, 47].
For the vector-borne disease, malaria, the parasite undergoes a ﬁrst half-life cycle called
the sporogonic cycle in the female Anopheles mosquito lasting approximately 10 −18 days
after the ﬁrst successful mosquito bite from a malaria infectious person. The parasite further
completes the remaining half-life cycle called the exo-erythrocytic cycle lasting about 7-30
days inside the exposed human being[46, 47], whenever the parasite is transferred to a
susceptible person after another successful infectious mosquito bite by the hosting female
mosquito.
Several vector-borne diseases induce or confer natural immunity against the disease after
infection and recovery. The eﬀectiveness and duration of the natural protective immunity
varies depending on the type of disease and also on other biological factors. For example, the
exposure and successful recovery from one dengue fever viral strain confers lifelong immunity
against the particular viral serotype[46].
Also, the exposure and successful recovery from a malaria parasite, for example, falci-
parum vivae induces natural immunity against the disease which can protect against sub-
sequent severe outbreaks of the disease.
Moreover, the eﬀectiveness and duration of the
naturally acquired immunity against malaria is determined by several factors such as the
species and the frequency of exposure to the parasites. Furthermore, it has been determined


## Page 4


4
that the naturally acquired immunity against malaria has bearings on other biological factors
such as the genetic characteristics of the human being[47, 14, 11].
Many infectious diseases have been investigated utilizing compartmental mathematical
epidemic dynamic models. For instance, malaria and dengue fever are studied in [1, 31], and
measles is studied in [29]. In general, these models are largely classiﬁed as SIS, SIR, SIRS,
SEIRS, and SEIR etc.[21, 22, 10, 25, 8, 40, 36, 15] epidemic dynamic models depending on
the compartments of the disease classes directly involved in the general disease dynamics.
Several studies devote interest to SEIRS and SEIR models[25, 8, 26, 9, 15] which allow
the inclusion of the compartment of individuals who are exposed to the disease, E, that
is, infected but noninfectious individuals.
This natural inclusion of the exposed class of
individuals allows for more insight about the disease dynamics during the incubation stage
of the disease. For example, the existence of periodic solutions are investigated in the SEIRS
epidemic study[25, 15]. And the eﬀects of seasonal changes on the disease dynamics are
investigated in the SEIRS epidemic study in [2].
Many epidemic dynamic models are modiﬁed and improved in reality by including the
time delays that occur in the disease dynamics. Generally, two distinct classes of delays
are studied namely:-disease latency and immunity delay.
The disease latency has been
represented as the infected but noninfectious period of disease incubation, and also as the
period of infectiousness which nonetheless is studied as a delay in the dynamics of the disease.
The immunity delay represents the period of eﬀective naturally acquired immunity against
the disease after exposure and successful recovery from infection. Whereas, some authors
study diseases and disease scenarios under the realistic assumption of one form of these two
classes of delays in the disease dynamics[36, 37, 17, 21], other authors study one or more
forms of the classes of delays represented as two separate delay times[15, 7, 12, 30]. The


## Page 5


5
occurrence of delays in the disease dynamics may inﬂuence the dynamics of the disease in
many important ways. For instance, in [15], the presence of delays in the epidemic dynamic
system leads to the existence of periodic solutions. In [6, 43], the occurrence of a delay in the
vector-borne disease dynamics destabilizes the equilibrium population state of the system.
Stochastic epidemic dynamic models more realistically represent epidemic dynamic pro-
cesses because they include the randomness which naturally occurs during a disease outbreak,
owing to the presence of constant random environmental ﬂuctuations in the disease dynam-
ics. The presence of stochastic white noise process in the epidemic dynamic system may
directly impact the density of the system or indirectly inﬂuence other driving parameters
of the infectious system such as the disease transmission, natural death, birth and disease
related death rates etc. In [36, 40, 37], the stochastic white noise process represents the
random ﬂuctuations in the disease transmission process. In [21], the white noise process
represents the variability in the natural death rate of the population. In [3], the white noise
process represents the random ﬂuctuations in the system which deviate the state of the
system from the equilibrium state, that is, the white noise process is proportional to the
diﬀerence between the state and equilibrium of the system.
A stochastic white noise process driven infectious system generally exhibits more complex
behavior in the disease dynamics, than would be observed in the corresponding deterministic
system. For instance, the presence of stochastic white noise process in the disease dynamics
may destabilize a disease free steady state population and drive the system into an endemic
state. In other cases, the presence of white noise with high intensity in the disease dynamics
may continuously decrease the population size over time, and eventually lead to the extinc-
tion of the population. For example, in [21, 36, 40, 37, 45, 44], the occurrence of stochastic
noise in the system destabilizes the disease free steady population state. In [21], it is ob-


## Page 6


6
served that the disease free steady state fails to exist when the intensity of the noise in the
system from the natural death rate of the susceptible population is high.
The interaction between susceptible, S, and infectious individuals, I, during the disease
transmission process can sometimes generate complex nonlinear responses from the suscep-
tible population as the infectious population increases. Such complex nonlinear responses
can no longer be represented by the the frequently used bilinear incidence rate (or force
of infection) given as βS(t)I(t −T) for vector-borne diseases, or βS(t)I(t), for infectious
diseases that involve direct human-to-human disease transmission, where β is the eﬀective
contact rate, and T is the incubation period for the vector-borne disease. Some examples
of nonlinear complex responses from the susceptible population include- psychological or
crowding eﬀects stemming from behavioral change of susceptible individuals when the infec-
tious population increases signiﬁcantly over time. These nonlinear response behaviors exist
for certain types of infectious diseases and disease scenarios, where the contact between the
susceptible and infectious classes are regulated, and consequently prevent unboundedness in
the disease transmission rate.
For instance, in [42, 41, 13, 17, 21, 28, 20, 5, 4, 23, 16] several diﬀerent functional forms for
the force of infection are used to represent the nonlinear behavior of the disease transmission
rate. In [42, 41, 5, 13] the authors consider a Holling Type II functional form, βS(t)G(I(t)) =
βS(t)I(t)
1+αI(t) , that saturates for large values of I.
In [28, 41, 4], a bounded Holling Type II
function, βS(t)G(I(t)) = βS(t)Ip(t)
1+αIp(t) , p ≥0, is used to represent the force of infection of the
disease. In [23, 16], the nonlinear incidence rate is represented by the general functional
form, βS(t)G(I(t)) = βSp(t)Iq(t), p, q ≥0. And the authors in [42, 13, 5, 28, 4, 21] studied
vector-borne diseases with several diﬀerent functional forms for the nonlinear incidence rates
of the disease.


## Page 7


7
Cooke[6] presented a deterministic epidemic dynamic model for vector-borne diseases,
where the bilinear incidence rate deﬁned as βS(t)I(t −T) represents the number of new
infections occurring per unit time during the disease transmission process. It is assumed
in the formulation of this incidence rate that the number of infectious vectors at time t
interacting and eﬀectively transmitting infection to susceptible individuals, S, after β number
of eﬀective contacts per unit time per infective is proportional to the infectious human
population, I, at earlier time t −T.
This paper employs similar reasoning in [6, 12], to derive a class of SEIRS stochastic
epidemic dynamic models with three delays for vector-borne diseases. The three delays are
classiﬁed under the two general forms-disease latency and immunity delay. Two of the delays
represent the incubation period of the infectious agent inside the vector and human hosts,
and the third delay represents the period of eﬀective naturally acquired immunity against
the vector-borne disease conferred after recovery from infection. Furthermore, the delays
are random variables. In addition, the general vector-borne disease dynamics is driven by
stochastic white noise processes originating from the random environmental ﬂuctuations in
the natural death and disease transmission rates in the population. The epidemic dynamic
model is represented as a system of Ito-Doob type stochastic diﬀerential equations.
It is important to note that this study is part of the broader project investigating vector-
borne diseases in the human population. As part of this project, a deterministic study of
malaria will appear in Wanduku[33]. Some specialized stochastic extensions of this project
addressing the impacts of noise on the persistence of malaria in the endemic equilibrium
population will appear in Wanduku[34]. Moreover, the stochastic permanence of malaria
and existence of stationary distribution will appear in Wanduku[35]. The primary focus of
the current study is to develop and study the fundamental properties of the class of stochastic


## Page 8


8
models for vector-borne diseases in a very noisy environment comprising of variability from
the disease transmission and natural death rates. In this study, the intensities of the noises
in the infectious system are classiﬁed, and their qualitative impacts on the eradication of the
vector-borne disease in the steady state population are characterized.
This work is presented as follows:- In section 2, the epidemic dynamic model is derived.
In section 3, the model validation results are presented.
In section 4, the existence and
asymptotic stochastic stability of the disease free equilibrium population is investigated. In
Section 5, the asymptotic behavior of the stochastic system under the inﬂuence of the various
intensity levels of the white noise processes in the system is characterized. In section 6,
numerical simulation results are given.
2. Derivation of Model
A generalized class of stochastic SEIRS delayed epidemic dynamic models for vector-
borne diseases is presented. The delays represent the incubation period of the infectious
agents in the vector T1, and in the human host T2. The third delay represents the naturally
acquired immunity period of the disease T3, where the delays are random variables with
density functions fT1, t0 ≤T1 ≤h1, h1 > 0, and fT2, t0 ≤T2 ≤h2, h2 > 0 and fT3, t0 ≤
T3 < ∞. Furthermore, the joint density of T1 and T2 is given by fT1,T2, t0 ≤T1 ≤h1, t0 ≤
T2 ≤h2. Moreover, it is assumed that the random variables T1 and T2 are independent (i.e.
fT1,T2 = fT1.fT2, t0 ≤T1 ≤h1, t0 ≤T2 ≤h2). Indeed, the independence between T1 and T2 is
justiﬁed from the understanding that the duration of incubation of the infectious agent for
the vector-borne disease depends only on the suitable biological environmental requirements
for incubation inside the vector and the human body which are unrelated. Furthermore,
the independence between T1 and T3 follows from the lack of any real biological evidence to


## Page 9


9
justify the interconnection between the incubation of the infectious agent inside the vector
and the acquired natural immunity conferred to the human being. But T2 and T3 may be
dependent as biological evidence suggests that the naturally acquired immunity is induced
by exposure to the infectious agent.
By employing similar reasoning in [6, 21, 4, 13], the expected incidence rate of the dis-
ease or force of infection of the disease at time t due to the disease transmission process
between the infectious vectors and susceptible humans, S(t), is given by the expression
β
R h1
t0 fT1(s)e−µsS(t)G(I(t −s))ds, where µ is the natural death rate of individuals in the
population, and it is assumed for simplicity that the natural death rate for the vectors and
human beings are the same. Assuming exponential lifetime for the random incubation period
T1, the probability rate, 0 < e−µs ≤1, s ∈[t0, h1], h1 > 0, represents the survival probability
rate of exposed vectors over the incubation period, T1, of the infectious agent inside the
vectors with the length of the period given as T1 = s, ∀s ∈[t0, h1], where the vectors ac-
quired infection at the earlier time t −s from an infectious human via for instance, biting
and collecting an infected blood meal, and become infectious at time t. Furthermore, it is
assumed that the survival of the vectors over the incubation period of length s ∈[t0, h1] is
independent of the age of the vectors. In addition, I(t −s), is the infectious human popula-
tion at earlier time t −s, G is a nonlinear incidence function for the disease dynamics, and
β is the average number of eﬀective contacts per infectious individual per unit time. Indeed,
the force of infection, β
R h1
t0 fT1(s)e−µsS(t)G(I(t −s))ds signiﬁes the expected rate of new
infections at time t between the infectious vectors and the susceptible human population
S(t) at time t, where the infectious agent is transmitted per infectious vector per unit time
at the rate β. Furthermore, it is assumed that the number of infectious vectors at time
t is proportional to the infectious human population at earlier time t −s. Moreover, it is


## Page 10


10
further assumed that the interaction between the infectious vectors and susceptible humans
exhibits nonlinear behavior, for instance, psychological and overcrowding eﬀects, which is
characterized by the nonlinear incidence function G. Therefore, the force of infection given
by
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
reasoning in [7], the exposed population, E(t), at time t can be written as follows
E(t) = E(t0)e−µ(t−t0)p1(t −t0) +
Z t
t0
βS(ξ)e−µT1G(I(ξ −T1))e−µ(t−ξ)p1(t −ξ)dξ,
(2.2)
where
p1(t) =





0, t ≥T2,
1, t < T2
(2.3)
represents the probability that an individual remains exposed over the time interval [0, t].
It is easy to see from (2.2) that under the assumption that the disease has been in the
population for at least a time t > maxt0≤T1≤h1,t0≤T2≤h2 (T1 + T2), in fact, t > h1 + h2, so that
all initial perturbations have died out, the expected number of exposed individuals at time


## Page 11


11
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
p2(t) =





0, t ≥T3,
1, t < T3
(2.6)
represents the probability that an individual remains naturally immune to the disease over
the time interval [0, t]. But it follows from (2.5) that under the assumption that the disease
has been in the population for at least a time t > maxt0≤T1≤h1,t0≤T2≤h2,T3≥t0 (T1 + T2, T3) ≥
maxT3≥t0 (T3), in fact, the disease has been in the population for suﬃciently large amount
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


## Page 12


12
There is also constant birth rate B of susceptible individuals in the population. Furthermore,
individuals die additionally due to disease related causes at the rate d. A compartmental
framework illustrating the transition rates between the diﬀerent states in the system and
also showing the delays in the disease dynamics is given in Figure 1.
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


## Page 13


13
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
dt.
(2.11)
It should be noted that the deterministic model (2.8)-(2.11) with the initial conditions in
(2.21)-(2.22) has been studied in the special case of malaria in Wanduku[33].
It is assumed in the current study that the eﬀects of random environmental ﬂuctuations
lead to variability in the disease transmission and natural death rates.
For t ≥t0, let
(Ω, F, P) be a complete probability space, and Ft be a ﬁltration (that is, sub σ- algebra Ft
that satisﬁes the following: given t1 ≤t2 ⇒Ft1 ⊂Ft2; E ∈Ft and P(E) = 0 ⇒E ∈F0
). The variability in the disease transmission and natural death rates are represented by
independent white noise processes, and the rates are expressed as follows:
µ →µ + σiξi(t),
ξi(t)dt = dwi(t), i = S, E, I, R,
β →β + σβξβ(t),
ξβ(t)dt = dwβ(t),
(2.12)
where ξi(t) and wi(t) represent the standard white noise and normalized wiener processes for
the ith state at time t, with the following properties: w(0) = 0, E(w(t)) = 0, var(w(t)) = t.


## Page 14


14
Furthermore, σi, i = S, E, I, R, represents the intensity value of the white noise process due
to the natural death rate in the ith state, and σβ is the intensity value of the white noise
process due to the disease transmission rate.
The ideas behind the formulation of the expressions in (2.12) are given in the following.
The constant parameters µ and β represent the natural death and disease transmission
rates per unit time, respectively. In reality, random environmental ﬂuctuations impact these
rates turning them into random variables ˜µ and ˜β. Thus, the natural death and disease
transmission rates over an inﬁnitesimally small interval of time [t, t + dt] with length dt
is given by the expressions ˜µ(t) = ˜µdt and ˜β(t) = ˜βdt, respectively. It is assumed that
there are independent and identical random impacts acting upon these rates at times tj+1
over n subintervals [tj, tj+1] of length △t = dt
n , where tj = t0 + j△t, j = 0, 1, · · · , n, and
t0 = t. Furthermore, it is assumed that ˜µ(t0) = ˜µ(t) = µdt is constant or deterministic, and
˜β(t0) = ˜β(t) = βdt is also a constant. It follows that by letting the independent identically
distributed random variables Zi, i = 1, · · · , n represent the random eﬀects acting on the
natural death rate, then it follows further that the rate at time tn = t + dt, that is,
˜µ(t + dt) = ˜µ(t) +
n
X
j=1
Zj,
(2.13)
where E(Zj) = 0,and V ar(Zj) = σ2
i △t, i ∈{S, E, I, R}. Note that ˜β(t+dt) can similarly be
expressed as (2.13). And for suﬃcient large value of n, the summation in (2.13) converges in
distribution by the central limit theorem to a random variable which is identically distributed
as the wiener process σi(wi(t + dt) −wi(t)) = σidwi(t), with mean 0 and variance σ2
i dt, i ∈
{S, E, I, R}. It follows easily from (2.13) that
˜µdt = µdt + σidwi(t), i ∈{S, E, I, R}.
(2.14)


## Page 15


15
Similarly, it can be easily seen that
˜βdt = βdt + σβdwβ(t).
(2.15)
Note that the intensities σ2
i , i = S, E, I, R, β of the independent white noise processes in the
expressions ˜µ(t) = µdt + σiξi(t) and ˜β(t) = βdt + σβξβ(t) that represent the natural death
rate, ˜µ(t), and disease transmission rate, ˜β(t), at time t, measure the average deviation of the
random variable disease transmission rate, ˜β, and natural death rate, ˜µ, about their constant
mean values β and µ, respectively, over the inﬁnitesimally small time interval [t, t+dt]. These
measures reﬂect the force of the random ﬂuctuations that occur during the disease outbreak
at anytime, and which lead to oscillations in the natural death and disease transmission
rates overtime, and consequently lead to oscillations of the susceptible, exposed, infectious
and removal states of the system over time during the disease outbreak. Thus, in this study
the words ”strength” and ”intensity” of the white noise are used synonymously. Also, the
constructions ”strong noise” and ”weak noise” are used to refer to white noise with high and
low intensities, respectively.
Under the assumptions in the formulation of the natural death rate per unit time ˜µ as a
brownian motion process above, it can also be seen easily that under further assumption that
the number of natural deaths N(t) over an interval [t0, t0 + t] of length t follows a poisson
process {N(t), t ≥t0} with intensity of the process E(˜µ) = µ, and mean E(N(t)) = E(˜µt) =
µt, then the lifetime is exponentially distributed with mean 1
µ and survival function
S(t) = e−µt, t > 0.
(2.16)
Substituting (2.12)-(2.16) into the deterministic system (2.8)-(2.11) leads to the following


## Page 16


16
generalized system of Ito-Doob stochastic diﬀerential equations describing the dynamics of
vector-borne diseases in the human population.
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
(2.17)
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
(2.18)
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
(2.19)
dR(t)
=

αI(t) −µR(t) −α
Z ∞
t0
fT3(r)I(t −r)e−µsdr

dt −σRR(t)dwR(t),
(2.20)
where the initial conditions are given in the following:- where ever necessary, we let h = h1+h2
and deﬁne
(S(t), E(t), I(t), R(t)) = (ϕ1(t), ϕ2(t), ϕ3(t), ϕ4(t)) , t ∈(−∞, t0],
ϕk ∈C((−∞, t0], R+), ∀k = 1, 2, 3, 4,
ϕk(t0) > 0, ∀k = 1, 2, 3, 4,
(2.21)


## Page 17


17
where C((−∞, t0], R+) is the space of continuous functions with the supremum norm
||ϕ||∞= sup
t≤t0
|ϕ(t)|.
(2.22)
Furthermore, the random continuous functions ϕk, k = 1, 2, 3, 4 are F0 −measurable, or
independent of w(t) for all t ≥t0.
Several epidemiological studies [27, 15, 25, 17, 21] have been conducted involving families
of SIR, SEIRS, SIS etc. epidemic dynamic models, where the family type is determined by a
set of general assumptions which characterize the nonlinear behavior of the incidence function
G(I) of the disease. Some general properties of the incidence function G assumed in this
study include the following:
Assumption 2.1.
A1 G(0) = 0.
A2 G(I) is strictly monotonic on [0, ∞).
A3 G′′(I) < 0 ⇔G(I) is diﬀerentiable concave on [0, ∞).
A4 limI→G(I) = C, 0 ≤C < ∞⇔G(I) has a horizontal asymptote 0 ≤C < ∞.
A5 G(I) ≤I, ∀I > 0 ⇔G(I) is at most as large as the identity function f : I 7→I over
the positive all I ∈(0, ∞).
An incidence function G that satisﬁes Assumption 2.1 A1-A5 can be used to describe the
disease transmission process of a vector-borne disease scenario, where the disease dynamics
is represented by the system (2.17)-(2.20), and the disease transmission rate between the
vectors and the human beings initially increases or decreases for relatively small values of
the infectious population size, and is bounded or steady for suﬃciently large size of the
infectious individuals in the population. It is noted that Assumption 2.1 is a generalization
of some subcases of the assumptions A1-A5 investigated in [27, 15, 17, 21]. Some examples
of frequently used incidence functions in the literature that satisfy Assumption 2.1A1-A5


## Page 18


18
include: G(I(t)) =
I(t)
1+αI(t), α > 0, G(I(t)) =
I(t)
1+αI2(t), α > 0, G(I(t)) = Ip(t), 0 < p < 1 and
G(I) = 1 −e−aI, a > 0.
It can be observed that (2.18) and (2.20) decouple from the other equations for S and I
in the system (2.17)-(2.20). It is customary to show the results for this kind of decoupled
system using the simpliﬁed system containing only the non-decoupled system equations for S
and I, and then infer the results to the states E and R, since these states depend exclusively
on S and I. Nevertheless, for convenience, the existence and stability results of the system
(2.17)-(2.20) will be shown for the vector X(t) = (S(t), E(t), I(t)). The following notations
will be used throughout this study:
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
(S(t), E(t), I(t), R(t))
X(t)
=
(S(t), E(t), I(t))
N(t)
=
S(t) + E(t) + I(t) + R(t).
(2.23)
3. Model Validation Results
In this section, the existence and uniqueness results for the solutions of the stochastic
system (2.17)-(2.20) are presented. The standard method utilized in the earlier studies[36,
37, 38] is applied to establish the results. It should be noted that the existence and qualitative
behavior of the positive solutions of the system (2.17)-(2.20) depend on the sources (natural
death or disease transmission rates) of variability in the system.
As it is shown below,
certain sources of variability lead to very complex uncontrolled behavior of the solutions
of the system. The following Lemma describes the behavior of the positive local solutions
for the system (2.17)-(2.20). This result will be useful in establishing the existence and
uniqueness results for the global solutions of the stochastic system (2.17)-(2.20).
Lemma 3.1. Suppose for some τe > t0 ≥0 the system (2.17)-(2.20) with initial condition


## Page 19


19
in (2.21) has a unique positive solution Y (t) ∈R4
+, for all t ∈(−∞, τe], then if N(t0) ≤B
µ ,
it follows that
(a.) if the intensities of the independent white noise processes in the system satisfy σi = 0,
i ∈{S, E, I} and σβ ≥0, then N(t) ≤B
µ , and in addition, the set denoted by
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
is locally self-invariant with respect to the system (2.17)-(2.20), where ¯B(−∞,τe]
R4
+,

0, B
µ

is the
closed ball in R4
+ centered at the origin with radius B
µ containing the local positive solutions
deﬁned over (−∞, τe].
(b.) If the intensities of the independent white noise processes in the system satisfy σi > 0,
i ∈{S, E, I} and σβ ≥0, then N(t) ≥0, for all t ∈(−∞, τe].
Proof:
It follows directly from (2.17)-(2.20) that when σi = 0, i ∈{S, E, I} and σβ ≥0, then
dN(t) = [B −µN(t) −dI(t)]dt
(3.2)
The result in (a.) follows easily by observing that for Y (t) ∈R4
+, the equation (3.2) leads
to N(t) ≤
B
µ −B
µ e−µ(t−t0) + N(t0)e−µ(t−t0). And under the assumption that N(t0) ≤
B
µ ,
the result follows immediately. The result in (b.) follows directly from Theorem 3.1. The
following theorem presents the existence and uniqueness results for the global solutions of
the stochastic system (2.17)-(2.20).
Theorem 3.1. Given the initial conditions (2.21) and (2.22), there exists a unique solu-
tion process X(t, w) = (S(t, w), E(t, w), I(t, w))T satisfying (2.17)-(2.20), for all t ≥t0.
Moreover,
(a.) the solution process is positive for all t ≥t0 a.s.
and lies in D(∞), whenever the
intensities of the independent white noise processes in the system satisfy σi = 0, i ∈{S, E, I}
and σβ ≥0. That is, S(t, w) > 0, E(t, w) > 0, I(t, w) > 0, ∀t ≥t0 a.s. and X(t, w) ∈
D(∞) = ¯B(−∞,∞)
R4
+,

0, B
µ

, where D(∞) is deﬁned in Lemma 3.1, (3.1).


## Page 20


20
(b.) Also, the solution process is positive for all t ≥t0 a.s. and lies in R4
+, whenever the
intensities of the independent white noise processes in the system satisfy σi > 0, i ∈{S, E, I}
and σβ ≥0. That is, S(t, w) > 0, E(t, w) > 0, I(t, w) > 0, ∀t ≥t0 a.s. and X(t, w) ∈R4
+.
Proof:
It is easy to see that the coeﬃcients of (2.17)-(2.20) satisfy the local Lipschitz condition
for the given initial data (2.21).
Therefore there exist a unique maximal local solution
X(t, w) = (S(t, w), E(t, w), I(t, w)) on t ∈(−∞, τe(w)], where τe(w) is the ﬁrst hitting time
or the explosion time[24]. The following shows that X(t, w) ∈D(τe) almost surely, whenever
σi = 0, i ∈{S, E, I} and σβ ≥0, where D(τe(w)) is deﬁned in Lemma 3.1 (3.1), and also
that X(t, w) ∈R4
+, whenever σi > 0, i ∈{S, E, I} and σβ ≥0. Deﬁne the following stopping
time
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
(3.3)
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
(3.4)
It follows from (3.4) that
dV (X(t)) = dV1(X(t)) + dV2(X(t)) + dV3(X(t)),
(3.5)


## Page 21


21
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
(3.6)
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
(3.7)


## Page 22


22
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
(3.8)


## Page 23


23
It follows from (3.5)-(3.8) that for t < τ+(t),
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
(3
Taking the limit on (3.9) as t →τ+(t), it follows from (3.3)-(3.4) that the left-hand side
V (X(t)) −V (X(t0)) ≤−∞. This contradicts the ﬁniteness of the right-handside of the
inequality (3.9).
Hence τ+(t) = τe(w) a.s., that is, X(t, w) ∈D(τe), whenever σi = 0,


## Page 24


24
i ∈{S, E, I} and σβ ≥0, and X(t, w) ∈R4
+, whenever σi > 0, i ∈{S, E, I} and σβ ≥0.
The following shows that τe(w) = ∞. Let k > 0 be a positive integer such that ||⃗ϕ||1 ≤k,
where ⃗ϕ = (ϕ1(t), ϕ2(t), ϕ3(t)) , t ∈(−∞, t0] deﬁned in (2.21), and ||.||1 is the p −sum norm
deﬁned on R3, when p = 1. Deﬁne the stopping time





τk = sup{t ∈[t0, τe) : ||X(s)||1 = S(s) + E(s) + I(s) ≤k, s ∈[t0, t]}
τk(t) = min(t, τk).
(3.10)
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
(3.11)
The Ito-Doob diﬀerential d ˆV1 of (3.11) with respect to the system (2.17)-(2.20) is given as
follows:
d ˆV1
=
µeµt(S(t) + E(t) + I(t))dt + eµt(dS(t) + dE(t) + dI(t))
(3.12)
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
(3.13)
Integrating (3.11) over the interval [t0, τ], and applying some algebraic manipulations and


## Page 25


25
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
(3.14)
Removing negative terms from (3.14), it implies from (2.21) that
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
(3.15)
But from (3.11) it is easy to see that for ∀t ≤τk(t),
||X(t)||1 = S(t) + E(t) + I(t) ≤V (X(t)).
(3.16)
Thus setting τ = τk(t), then it follows from (3.10), (3.15) and (3.16) that
k = ||X(τk(t))||1 ≤V1(X(τk(t)))
(3.17)
Taking the limit on (3.17) as k →∞leads to a contradiction because the left-hand-side of
the inequality (3.17) is inﬁnite, but following the right-hand-side from (3.15) leads to a ﬁnite
value. Hence τe = τ∞a.s. The following shows that τe = τ∞= ∞a.s.


## Page 26


26
Let w ∈{τe < ∞}. It follows from (3.14)-(3.15) that
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
(3.18)
Suppose τ = τk(t) ∧T, where T > 0 is arbitrary, then taking the expected value of (3.18)
follows that
E(I{τe<∞}V1(X(τk(t) ∧T))) ≤V1(X(t0)) + B
µ eµT
(3.19)
But from (3.16) it is easy to see that
I{τe<∞,τk(t)≤T}||X(τk(t))||1 ≤I{τe<∞}V1(X(τk(t) ∧T))
(3.20)
It follows from (3.18)-(3.20) and (3.10) that
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
(3.21)
It follows immediately from (3.21) that P({τe < ∞, τ∞≤T}) →0 as k →∞. Furthermore,
since T < ∞is arbitrary, we conclude that P({τe < ∞, τ∞< ∞}) = 0. Finally, by the total


## Page 27


27
probability principle,
P({τe < ∞})
=
P({τe < ∞, τ∞= ∞}) + P({τe < ∞, τ∞< ∞})
≤
P({τe ̸= τ∞}) + P({τe < ∞, τ∞< ∞})
=
0.
(3.22)
Thus from (3.22), τe = τ∞= ∞a.s.. In addition, X(t) ∈D(∞), whenever σi = 0, i ∈
{S, E, I} and σβ ≥0, and X(t, w) ∈R4
+, whenever σi > 0, i ∈{S, E, I} and σβ ≥0.
Remark 3.1. Theorem 3.1 and Lemma 3.1 signify that the stochastic system (2.17)-(2.20)
has a unique positive solution Y (t) ∈R4
+ globally for all t ∈(−∞, ∞). Furthermore, it
follows that a positive solution of the stochastic system that starts in the closed ball centered at
the origin with a radius of B
µ , D(∞) = ¯B(−∞,∞)
R4
+,

0, B
µ

, will continue to oscillate and remain
bounded in the closed ball for all time t ≥t0, whenever the intensities of the independent
white noise processes in the system satisfy σi = 0, i ∈{S, E, I} and σβ ≥0. Hence, the
set D(∞) = ¯B(−∞,∞)
R4
+,

0, B
µ

is a positive self-invariant set for the stochastic system (2.17)-
(2.20). In the case where the intensities of the independent white noise processes in the
system satisfy σi > 0, i ∈{S, E, I} and σβ ≥0, the solution are positive and unique, and
continue to oscillate in the unbounded space of positive real numbers R4
+. In other words,
the positive solutions of the system are bounded, whenever σi = 0, i ∈{S, E, I} and σβ ≥0
and unbounded, whenever σi > 0, i ∈{S, E, I} and σβ ≥0.
The implication of this result to the disease dynamics represented by (2.17)-(2.20) is that
the occurrence of noise exclusively from the disease transmission rate allows a controlled
situation for the disease dynamics, since the positive solutions exist within a positive self
invariant space. The additional source of variability from the natural death rate can lead to
more complex and uncontrolled situations for the disease dynamics, since it is obvious that
the intensities of the white noise processes from the natural death rates of the diﬀerent states
in the system are driving the positive solutions of the system unbounded. Some examples
of uncontrolled disease situations that can occur when the positive solutions are unbounded
include:- (1) extinction of the population, (2) failure to ﬁnd an infection-free steady popula-
tion state, wherein the disease be controlled by bringing the population into that state, and
(3) a sudden signiﬁcant random ﬂip of a given state such as the infectious state from a low
to high value, or vice versa over a short time interval etc. These facts become more apparent
in the subsequent sections where conditions for disease eradication are derived.


## Page 28


28
4. Existence and Asymptotic Behavior of Disease Free Equilibrium
In this section, the existence and the general asymptotic properties of the disease free
equilibrium for the stochastic system (2.17)-(2.20) are investigated.
Indeed, the disease-
free equilibrium for the stochastic system (2.17)-(2.20) is obtained by solving the system of
algebraic equations produced after setting the drift and the diﬀusion parts of the stochastic
system to zero. In addition, the condition E = I = R = 0 is utilized in the event when there
is no disease in the population. The equilibria of the delayed stochastic system (2.17)-(2.20)
are denoted generally by E = (S∗, E∗, I∗).
It is shown in the following result that the existence of an infection-free steady state
for the population with the disease dynamics given by (2.17)-(2.20) depends on the sources
(disease transmission or natural death rates) of the noises in the system which are reﬂected
by the intensities of the white noise processes in the system σi, i = S, E, I, β. In other words,
the following result presents the existence of the disease-free steady state solution for the
stochastic system (2.17)-(2.20) for diﬀerent restrictions of the intensities of the independent
white noise processes in the system σi, i = S, E, I, β. In the next section, the qualitative be-
havior of the infection-free steady state solution of the system (2.17)-(2.20) will be examined
under diﬀerent growth rates or growth orders for the intensities of the white noise processes
in the system.
Theorem 4.1.
1. Let σi = 0, i = E, I, β and σS = 0.
There exists a disease-free steady state solution
E0 = (S∗
0, 0, 0) for the stochastic system (2.17)-(2.20), where S∗
0 = B
µ . And this infection-
free steady state E0 is exactly the same infection-free steady state for the corresponding
deterministic system (2.8)-(2.11)(see [33]).
2. Let σi > 0, i = E, I, β and σS = 0.
There exists a disease-free steady state solution
E0 = (S∗
0, 0, 0) for the stochastic system (2.17)-(2.20), where S∗
0 = B
µ . And this infection-
free steady state E0 is again exactly the same infection-free steady state for the corresponding
deterministic system (2.8)-(2.11).


## Page 29


29
3. Let σi ≥0, i = E, I, β and σS > 0. The system (2.17)-(2.20) does not have a disease-free
steady state solution.
Proof:
The results follow immediately by applying the method of ﬁnding the equilibria of the system
described above.
Remark 4.1. In results of Theorem 4.1 can be interpreted in a physical context of a vector-
borne disease in a population following the disease dynamic model (2.17)-(2.20) as follows:-
Theorem 4.1[1.] asserts that the population has an infection-free population steady state,
whenever the strengths of the noises in the system from all the diﬀerent sources considered
in this study namely:- (1) the disease transmission rate, and (2) the natural death rates for
all the diﬀerent classes in the population (susceptible, exposed, infectious or removal) are
weak, that is, whenever the intensities σi, i = S, E, I, β are all inﬁnitesimally small.
The results in Theorem 4.1[2.] and Theorem 4.1[3.] signify that regardless of the strength
of the noises in the population from the disease transmission rate between the infectious
vectors and the susceptible class, or from the natural death rate of the exposed, infectious
and removal classes in the population, there always exist an infection-free population steady
state, provided that the strength of the noise in the population from the natural death rate
of susceptible individuals is inﬁnitesimally small, that is, whenever σS = 0. In the event
where the strength of the noise in the population from the natural death rate of susceptible
individuals is signiﬁcant, that is, when σS > 0, then the infection-free state ceases to exist.
Furthermore, it can be deduced from the results in Theorem 4.1[1.] and Theorem 4.1[2.]
that the sources and strengths of the noises in the system would not have any consequences
on the existence of the infection-free population steady state provided that the noises in the
population do not originate from the natural death rate of the susceptible class, since the same
steady state E0 is obtained in both cases where (1) there is complete absence of noise in the
population given by the deterministic system (2.8)-(2.11), and (2) there is some presence of
noise from every other source namely:- the disease transmission rate, and the natural death
rates of the exposed, infectious and removal classes in the population, except from the natural
death rate of the susceptible class.
Another important observation from Theorem 4.1 is that the intensity or strength of the
noise from the natural death rate of the susceptible class controls the existence of the infection-
free population steady state for the population primarily. This observation suggests that the
strength of the noise in the population from the natural death rate of susceptible individuals
plays a major role to determine the qualitative stability character of the infection-free state,
and consequently on controlling the disease in the population.
In this section, the stochastic stability of the disease-free steady state E0 will be examined
in the general case for which the intensities of the white noise processes satisfy σi ≥0,


## Page 30


30
i ∈{S, E, I, β}. In Section 5, special cases for the intensities of the white noise processes in
the system will be examined.
In the following, the asymptotic stability of the disease free equilibrium, E0, of the system
(2.17)-(2.20) is investigated. The stochastic version of the Lyapunov functional technique[36,
37] is utilized to establish the stability results. In order to study the qualitative properties of
(2.17)-(2.20) with respect to the equilibrium state E0 = (S∗
0, 0, 0), S∗
0 = B
µ , ﬁrst the following
transformation of the variables of the system (2.17)-(2.20) which shifts the equilibrium state
of the system to the origin is used:
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
By employing the transformation in (4.1) to the system (2.17)-(2.19), the following system


## Page 31


31
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
Furthermore, the lemmas that follow in this section will be utilized to establish the stability
results for the disease-free steady state E0 of the system (2.17)-(2.20). These results also
characterize the long-term behavior of the sample-paths of the stochastic system (2.17)-
(2.20) in the neighborhood of the infection-free steady state E0. Let us recall the following
result obtained in the earlier study [[40], Lemma 4.1].
Lemma 4.1. Suppose V1 ∈C2,1(R3 × R+, R+) is deﬁned by
V1(x, t)
=
(S(t) −S∗+ E(t))2 + c(E(t))2 + (I(t))2
(4.5)
x(t)
=
(S(t) −S∗, E(t), I(t))T,
(4.6)
where c is a positive constant. There exists two increasing positive real valued functions φ1,


## Page 32


32
and φ2, such that V1 satisﬁes the inequality
φ1(||x||)
≤
V1(x, (t)) ≤φ2(||x||).
(4.7)
Proof: The result follows directly from Lemma 4.1 in [40].
It should be noted that the result in Lemma 4.1 asserts that the function V1 is positive
deﬁnite, decrescent and radially unbounded in R3 × R+. These properties of the function V1
are required, whenever the objective in applying the Lyapunov techniques is to establish the
stochastic asymptotic stability in the large of the steady state of the system as stated in [24].
The next result presents an upper bound estimate for the drift part of the Ito-derivative of
V1.
Lemma 4.2. Let the hypothesis of Theorem 3.1 be satisﬁed. The diﬀerential operator[40,
39] applied to the Lyapunov function V1 in (4.6) with respect to the system of stochastic
diﬀerential equation (2.17)-(2.20) is given by
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
0 + U(t −u))G(W(t −s −u))dsdudwβ(t), (4.8)
where for some positive valued function ˜K(µ) that depends on µ, the drift part LV1 of dV1


## Page 33


33
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
The computation of the drift part LV ( see the references [39, 37]) of the diﬀerential operator
dV applied to the Lyapunov function V1 in (4.6) with respect to the system of stochastic


## Page 34


34
diﬀerential equation (2.17)-(2.20) gives the following:
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
Applying Theorem 3.1, Cauchy −Swartz, H¨older inequalities, and the following algebraic
inequality
2ab ≤a2
g(c) + b2g(c),
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
The result (4.9) follows by applying (4.12)-(4.17) and the inequality (4.11) into (4.10). That
is, LV1(x, t) becomes
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
The following result characterizes the stochastic asymptotic stability of the infection-free
equilibrium E0 of the system (2.17)-(2.20), whenever the intensity of the white noise process
from the natural death rate of the susceptible population is zero, that is, when σS = 0.


## Page 37


37
Lemma 4.3. Let the hypotheses of Theorem 3.1, Theorem 4.1[2.] and Lemma 4.2 be satis-
ﬁed. There exists a Lyapunov functional
V = V1 + V2,
(4.19)
where V1 ∈C2,1(R3 × R+, R+) is deﬁned by (4.6) and V2 is deﬁned as follows:
V2(x, t) = 2α
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
(4.20)
Furthermore, there exists threshold values R1, U0 and V0 deﬁned as follows:
R1 =
βS∗
0 ˆK1
(µ + d + α) +
α
(µ + d + α) +
ˆk1σ2
β + 1
2σ2
I
(µ + d + α),
(4.21)
U0 =
2βS∗
0 + β + α + 2
µ
˜
K(µ)2
2µ
,
(4.22)
and
V0 = (2µ ˜K(µ)2 + α + β(2S∗
0 + 1))
2µ
+ σ2
E
2µ,
(4.23)
with some constants ˆK1 > 0, ˆk1 > 0 that depends on S∗
0 (in fact, ˆk1 = 6S∗
0 and ˆK1 = 4+S∗
0),
and under the assumptions that R1 ≤1, U0 ≤1, and V0 ≤1, the drift part LV of the
diﬀerential operator dV applied to V with respect to the stochastic dynamic system (2.17)-
(2.20) satisﬁes the following inequality:
LV (x, t) ≤−
 φU2(t) + ψV 2(t) + ϕW 2(t)

.
(4.24)
Proof:
The drift part LV of the diﬀerential operator dV applied to the Lyapunov functional deﬁned


## Page 38


38
in (4.19), (4.6) and (4.20) with respect to system (2.17)-(2.20) leads to the following:
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
(4.25)
Under the assumptions for σi, i = S, E, I, β in Theorem 4.1[2.], and for some suitable choice
of the positive constant c, it follows from (4.9), (4.25), the statements of Assumption 2.1, A5
(i.e. G2(x) ≤x2, x ≥0) and some further algebraic manipulations and simpliﬁcations that
LV (x, t) ≤−
 φU2(t) + ψV 2(t) + ϕW 2(t)

,
(4.26)


## Page 39


39
where,
φ
=
2µ(1 −U0),
(4.27)
ψ
=
2µ(1 −V0) −2µc

1 −β(3S∗
0 + 1) + σ2
E
2µ

,
(4.28)
ϕ
=
2(µ + d + α)(1 −R1) −c(3βS∗
0 + β(S∗
0)2 + 4σ2
β(S∗
0)2) −2c2σ2
β(S∗
0)2,
(4.29)
and R1, V0 and U0 are deﬁned in (4.21)-(4.23). In addition, under the assumptions of R1, U0,
and V0 in the hypothesis of the theorem, and for a suitable choice of the positive constant c
it follows that φ, ψ, and ϕ are positive constants and (4.24) follows immediately.
The Lemma 4.3 asserts that there exists a positive-deﬁnite decrescent radially unbounded
functional V deﬁned in (4.19) which satisfy the conditions of the stochastic Lyapunov sta-
bility characterizations (see [24]).
This result implies that the zero steady state of the
transformed system (4.2)-(4.4), and consequently the nonzero infection-free steady state E0
of the original stochastic system (2.17)-(2.20) is stochastically asymptotically stable in the
large. The following theorem formally states the asymptotic stability result for the disease
free equilibrium E0, whenever it exists.
Theorem 4.2. Suppose Theorem 4.1[2.] and the hypotheses of Lemma 4.1 and Lemma 4.3
are satisﬁed, then the disease-free equilibrium E0 of the stochastic dynamic system (2.17)-
(2.20) is stochastically asymptotically stable in the large in the set D(∞). Moreover, the
steady state solution E0 is exponentially mean square stable.
Proof
The result follows directly from comparative stochastic stability results.Moreover, the disease
free equilibrium state is exponentially mean square stable from [Corollary 3.4, or Theorem 4.4
of [24]].
The results in Lemma 4.3 and Theorem 4.2 hold the key to understand the underlying
factors of the infectious dynamic system (2.17)-(2.20) that are controlling the eradication of


## Page 40


40
disease from the system. Since the primary goal of this paper is to provide mathematical
techniques to model and to interpret the impacts of noise in the infectious disease system,
the diﬀerent observations will be titled below and elaborated on in the following:
4.1. The disease eradication conditions
Theorem 4.2 signiﬁes that in the absence of the noise in the system from the random
ﬂuctuations in the natural death rate of the susceptible population which is reﬂected by the
condition that σS = 0, then regardless of whether there is strong or weak noise in the system
from the random ﬂuctuations in (1.) the natural death rates of the other disease related
subclasses namely- the exposed, the infectious, and the removal populations, which is also
reﬂected by the values of the intensities σi ≥0, i = E, I, R, or from random ﬂuctuation
in (2.) the disease transmission rate of the vector-borne disease which is again reﬂected
by the value of the intensity of the noise given by σ2
β ≥0, there is always an infection-free
steady state for the population exhibiting the disease dynamics given by (2.17)-(2.20), where
the infection-free steady state is given by E0. Moreover, the infection-free steady state is
stochastically asymptotically stable in the large, whenever the following threshold conditions
are satisﬁed, that is, R1 ≤1, U0 ≤1, and V0 ≤1, where the threshold values R1, U0, and V0
are deﬁned in (4.21)-(4.23).
In other words, if the threshold conditions R1 ≤1, U0 ≤1, and V0 ≤1 hold, then every
sample path of the system (2.17)-(2.20) that starts in the neighborhood of the disease-free
steady state E0 has a high chance to stay in the neighborhood of E0, and ultimately becomes
E0. That is, the sample paths of the disease related states E, I and R ultimately become
zero, whenever the threshold conditions hold, and as a consequence, the disease is eliminated
from the population.
It should be noted that the threshold values R1, U0, and V0 deﬁned in (4.21)-(4.23) are


## Page 41


41
explicit in terms of the parameters of the system (2.17)-(2.20), and also computationally
attractive, whenever the speciﬁc values for the parameters of the system are given. This
observation suggests in theory that in a physical disease outbreak, if the physical character-
istics of the disease scenario can be mathematically expressed in terms of the parameters
of the system (2.17)-(2.20), wherein the threshold values, R1, U0, and V0 can be computed,
then the disease eradication conditions R1 ≤1, U0 ≤1, and V0 ≤1 can be easily checked.
Moreover, the disease will be eradicated whenever the strength of the random ﬂuctuations in
the natural death rate of the susceptible individuals is very weak or unnoticeable, and this is
also true regardless of whether the strengths of the random ﬂuctuations in the natural death
rate of the other disease related classes, or the strength of the ﬂuctuation in the disease
transmission rate are strong or weak.
The threshold value R1 is called the basic reproduction number ( also called the noise-
modiﬁed basic reproduction number) for the disease dynamics described by the stochastic
system (2.17)-(2.20), and it exists only under the condition that the intensities of the indepen-
dent white noise processes in the system satisfy the assumptions that σi ≥0, i = E, I, R, β,
and σS = 0. This important threshold value is deﬁned in theory as the expected number of
secondary infectious cases that result from one infectious individual in a completely suscep-
tible population. Moreover, this parameter signals the stability of the infection-free steady
state, and consequently signal the eradication of disease from the system, whenever R1 ≤1.
It also signals the existence of an endemic equilibrium, and consequently signals that the
disease persists in the population, since an infectious steady state for the population exists,
whenever the condition R1 > 1 holds. This parameter can also be modiﬁed by the presence
of noise in the stochastic system, and as a result certain scenarios wherein the disease would
be eradicated in the absence of noise in the system, would tend to favor the persistence of


## Page 42


42
the disease, that is, the existence of a stable infectious state, whenever noise is introduced
in the system. This is the case in this study as it is shown below.
The noise modiﬁed basic reproduction number given by
R1 =
βS∗
0 ˆK1
(µ + d + α) +
α
(µ + d + α) +
ˆk1σ2
β + 1
2σ2
I
(µ + d + α),
(4.30)
can be interpreted as follows:- ﬁrstly, since β is the average number of eﬀective infections
contacts that every infectious individual can make in the population, whenever homogeneous
mixing is assumed, therefore the term
βS∗
0 ˆ
K1
(µ+d+α) represents a constant multiple ˆK1 of the disease
transmission rate (also deﬁned as the average number of new infections per unit time) given
by the term βS∗
0 in the infection-free steady state population N∗= S∗
0 deﬁned in (2.23) that
contains just one infectious individual over the average life-span of an infectious individual
in the population given by
1
(µ+d+α). Note that in a population where people can either die
naturally or die from disease related causes, or recover from the disease, the average life-spans
is aﬀected by these sources of mortality, and is given by
1
(µ+d+α).
Furthermore, the term
α
(µ+d+α) in (4.30) is the recovery rate in the infection-free steady
state population N∗= S∗
0 containing just one infectious individual over the average life-
span of an infectious individual in the population. Let us note that the recovery rate α
is a probabilistic rate deﬁned as the probability of recovery from vector-borne disease per
unit time per infective. The term
α
(µ+d+α) represents the inﬂuence of recovery on the basic
reproduction number since the single infectious individual in the infection-free steady state
population has a chance to survive from both natural and disease related deaths, and also
fully recover from infection.
The last term
ˆk1σ2
β+ 1
2σ2
I
(µ+d+α)
represents the inﬂuence of the noise in the system from the
disease transmission rate, and the natural death rate of the infectious population on the


## Page 43


43
basic reproduction number. As this last term may no longer exist in the absence of noise in
the system, so the name ”modiﬁed-basic reproduction number” is used to describe the basic
reproduction number for a stochastic dynamic system.
It is also easy to see that the basic reproduction number in (4.30) is inﬂated by the
noise term in the system, whenever the intensities σβ > 0 and σI > 0. This observation is
demonstrated in Figure 2 of Section 6, and elaborated upon further in the next section. This
observation also suggests that stronger noise in the system from the natural death rate of
infectious individuals, or from the disease transmission rate which may lead to higher values
of σβ > 0 and σI > 0, may also inﬂate the basic reproduction number beyond the threshold
bound R1 ≤1, thereby causing the disease to establish a stable endemic steady state in
the population. The next section considers diﬀerent growth orders for the intensities of the
white noise processes in the system, and examines how they aﬀect the stochastic system.
4.2. The eﬀects of the source and intensity of white noise
In addition to the existence results of Theorem 4.1, the results of Lemma 4.3 and Theo-
rem 4.2 also suggest that the sources of the noises in the system, that is, from the disease
transmission or natural death rates, and also the intensities of the white noises in the stochas-
tic system (2.17)-(2.20), which are a result of the random ﬂuctuations the disease dynamics
exhibit direct consequences on the qualitative outcome of the vector-borne disease dynamics
in the system with respect to the factors that determine disease eradication.
To explain further, while Lemma 4.3 and Theorem 4.2 assert that the stochastic system
(2.17)-(2.20) has a stochastically stable disease-free equilibrium, the result in Theorem 4.1[3.]
suggests the contrary.
That is, Theorem 4.1[3.]
asserts that introducing the additional
source of the random ﬂuctuations in the system from the natural death rate of susceptible
individuals in the population, then the stochastic system (2.17)-(2.20) no longer has a disease-


## Page 44


44
free steady state wherein the disease can be eradicated, whenever the intensity of the white
noise from the natural death rate of the susceptible population σS is signiﬁcant, that is,
whenever σS > 0. Consequently, the disease can no longer be eradicated by applying the
threshold conditions R1 ≤1, U0 ≤1, and V0 ≤1.
The physical interpretation of this observation, in theory, is that stronger noise in the
population from the natural deathrate of susceptible people in the population does no good
to ease the disease control process in the population. This is justiﬁcation for the obvious
fact that when more people without the disease die from other causes apart from the disease,
then only the disease related classes of people are left to continue to infect the remaining
susceptible population.
Furthermore, just like the basic reproduction number R1, the other threshold values U0
and V0 deﬁned in (4.21)-(4.23) also depend on the intensities of the white noise processes
σi ≥0, i = E, I, R, β in the stochastic dynamic system (2.17)-(2.20). It can also be observed
from (4.21)-(4.23) that high values of the intensities σi ≥0, i = E, I, R, β are associated
with high values for the threshold values R1, U0, and V0, and vice versa. This fact is much
more visible in Figure 2 of Section 6. Therefore, the intensities of the white noise processes
in the system tend to inﬂate all the threshold values for disease eradication R1, U0 and V0
of the stochastic dynamic system (2.17)-(2.20), and consequently exert constraints on the
threshold conditions R1 ≤1, U0 ≤1, and V0 ≤1 for disease eradication.
In other words, stronger noises in the population from the natural deathrates of the
disease related classes - exposed, infectious and removal populations, and also from the
disease transmission rate tend to inﬂate the threshold values for disease eradication U0, and
V0 beyond the maximum threshold bounds R1 ≤1, U0 ≤1, and V0 ≤1, and as a result,
destabilize the infection-free steady state E0 of the population, and lead to a stable endemic


## Page 45


45
state for the disease in the population.
Since it is obvious from the above discussion that the qualitative outcome of the disease
dynamics represented in the stochastic dynamic model (2.17)-(2.20) such as the existence and
stochastic stability of the disease-free equilibrium E0, and consequently disease eradication
from the population depend on the intensities of the white noise processes in the system,
it follows in the next section that the growth orders of the intensities of the white noise
processes in the system are classiﬁed, and their impacts on the stability of the disease-free
equilibrium, and also on disease eradication are examined. Moreover, numerical evidence for
the eﬀects of intensities of the white noise processes on the stochastic system (2.17)-(2.20)
are presented in Section 6.
As earlier mentioned in the introduction of this section, oftentimes the inﬂuence of the
noise in a random dynamical system is more apparent in a comparative analysis to the
stability results of the corresponding deterministic system. The following result characterizes
the stability of the disease-free equilibrium of the stochastic system (2.17)-(2.20), whenever
the intensities of the white noise processes in the system are so small that their existence
can be ignored.
Theorem 4.3. Let the hypotheses of Theorem 3.1, Theorem 4.1[1.]
and Lemma 4.2 be
satisﬁed. There exists a Lyapunov functional
V = V1 + V2,
(4.31)


## Page 46


46
where V1 ∈C2,1(R3 × R+, R+) is deﬁned by (4.6) and V2 is deﬁned as follows:
V2(x, t) = 2α
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
.
(4.32)
Furthermore, deﬁne R0, U0 and V0, as follows:
R0 =
βS∗
0 ˆK0
(µ + d + α) +
α
(µ + d + α),
(4.33)
ˆU0 =
2βS∗
0 + β + α + 2
µ
˜
K(µ)2
2µ
,
(4.34)
and
ˆV0 = (2µ ˜K(µ)2 + α + β(2S∗
0 + 1))
2µ
,
(4.35)
where, ˆK0 > 0 is a constant that depends only on S∗
0 (in fact, ˆK0 = 4 + S∗
0). Assume that
R0 ≤1, ˆU0 ≤1, and ˆV0 ≤1, then there exist positive constants φ1, ψ1, and ϕ1, such that
the diﬀerential operator ˙V applied to V with respect to the stochastic system (2.17)-(2.20)
satisﬁes the following inequality:
˙V (x, t) ≤−
 φ1U2(t) + ψ1V 2(t) + ϕ1W 2(t)

.
(4.36)
Moreover, under the assumptions in the hypothesis of Theorem 4.1[1.], the disease free equi-
librium E0 of the resulting system (2.17)-(2.20) is uniformly globally asymptotically stable
in the set D(∞).
Proof:
The result follows directly from the Proofs of Lemma 4.2 and Lemma 4.3 by applying the
conditions that σi = 0, i = S, E, I, β, and also applying the comparison stability results


## Page 47


47
utilized in [39], where from (4.27)-(4.29), φ1 = φ, ψ1 = ψ, and ϕ1 = ϕ.
The discussion in Subsection 4.2 is carried forward in the following subsection that ex-
pands on the results of the comparative analysis between the stability of the infection-free
steady state of the system (2.17)-(2.20) in the presence, and also in absence of noise in the
system. That is, the results given in Theorems [4.2-4.3] are compared.
4.3. stability in the absence of noise
Theorem 4.3 asserts that when the noise in the system from all sources, natural death
or disease transmission rates, is very weak that can be ignored, that is, when σi →0, i =
S, E, I, R, β, then the behavior of the stochastic system (2.17)-(2.20) is equivalent to the
behavior of the deterministic system (2.8)-(2.11). That is, there is an infection-free steady
state, E0, for the population which similarly to Theorem 4.2 is globally asymptotically stable,
whenever the threshold conditions: R0 ≤1, ˆU0 ≤1 and ˆV0 ≤1 hold, where the threshold
values R0, ˆU0 and ˆV0 are deﬁned in (4.33)-(4.35). In other words, the trajectories of the
systems (2.17)-(2.20) and (2.8)-(2.11) in this case are the same, and continuously smooth
all over time as there is less deﬂection by the noise in the system. Furthermore, all the
trajectories that start in the neighborhood of the infection-free steady state E0 certainly
remain in the neighborhood of E0 in a deterministic manner, and ultimately become the
disease-disease free steady state. That is, the disease is eradicated from the system, whenever
the threshold conditions R0 ≤1, ˆU0 ≤1 and ˆV0 ≤1 hold.
Furthermore, it should be noted similarly to Theorem 4.2 that the threshold values R0,
ˆU0 and ˆV0 are explicit in terms of the parameters of the system (2.8)-(2.11), or equivalently
in terms of the parameters of the system (2.17)-(2.20), whenever σi →0, i = S, E, I, R, β,
and they are also computationally attractive, whenever the speciﬁc values for the parameters
of the system are given. This observation, in theory, implies that the conditions for disease


## Page 48


48
eradication in a disease scenario which follows the disease dynamics (2.17)-(2.20), whenever
σi →0, i = S, E, I, R, β, are determined by verifying the threshold conditions R0 ≤1, ˆU0 ≤1
and ˆV0 ≤1 for the speciﬁc values of the parameters of the system that correspond to the
disease scenario.
It is also easy to see from (4.30) and (4.33) that the two threshold values R0 and R1
satisfy R0 = R1, whenever the conditions of Theorem 4.3 are satisﬁed. Therefore, these two
threshold parameters R0 and R1 are the basic reproduction numbers for the system (2.17)-
(2.20) without and with noise in the system, respectively. Moreover, R1 is a modiﬁcation of
R0 by adding the noise terms σβ and σI. Thus, R0 is called the ordinary basic reproduction
number for the system, while R1 is the noise-modiﬁed basic reproduction number for the
disease dynamics.
Also, comparing the threshold values for Theorem 4.3 and Theorem 4.2 deﬁned in (4.33)-
(4.35) and (4.21)-(4.23) respectively, it is easy to see that the basic reproduction numbers
satisfy R0 ≤R1, and the other threshold values also satisfy U0 = ˆU0 and ˆV0 ≤V0, whenever
the intensities of the white noise processes in the system (2.17)-(2.20) satisfy σi > 0, i =
E, I, β. It is also easy to see that the intensities σi > 0, i = E, I, R, β of the corresponding
white noise processes from the disease transmission rate, and the natural deathrates of the
exposed, infections and removal classes inﬂate the threshold values R1, U0, and V0 deﬁned
in (4.21)-(4.23), but have no inﬂuence on the threshold values R0, ˆU0 and ˆV0 deﬁned in
(4.33)-(4.35). Moreover, one can see that when the intensities satisfy σi > 0, i = E, I, R, β,
the threshold values - R0, ˆU0 and ˆV0 from (4.33)-(4.35) are smaller in magnitude than the
corresponding threshold values R1, U0, and V0. This implies that the threshold conditions
R0 ≤1, ˆU0 ≤1 and ˆV0 ≤1 are much more easily satisﬁed, when compared to the other
threshold conditions R1 ≤1, U0 ≤1, and V0 ≤1 for the set of threshold values R1, U0,


## Page 49


49
and V0 deﬁned in (4.21)-(4.23). This observation implies that, the disease is more easily
eradicated when there almost negligible noise in the system, than when the strength of
the noise in the system is strong.
Furthermore, this observation also suggests that the
intensities of the random ﬂuctuations in the disease dynamics (2.17)-(2.20) expressed as
σi, i = E, I, R, β reﬂect the weights of the counter barrier eﬀects exerted against the disease
eradication process.
In addition, comparing the results of Theorem 4.3 and Theorem 4.2, one can guess
that the noise from the natural deathrates of the disease related classes-exposed, infectious
and removal populations, and also the noise from the disease transmission rates do not
inﬂuence a change on the existence and stability of the disease-free steady state E0, since
the existence and stability of E0 does not change under the conditions of both theorems,
regardless of whether the intensities satisfy σi > 0, i = E, I, R, β, or the intensities satisfy
σi →0, i = E, I, R, β, provided that the threshold values satisfy R1 ≤1, U0 ≤1, and V0 ≤1.
This implies that the disease will be continuously eradicated from the system, regardless of
the strengths of the noises from the natural deathrates of the disease related classes-exposed,
infectious and removal populations, and also regardless of the strength of the noise from the
disease transmission rate, provided that the threshold conditions R1 ≤1, U0 ≤1, and V0 ≤1
are satisﬁed.
The result in Theorem 4.3 also conﬁrms the earlier observation from Theorem 4.2 that
the source of the environmental white noise processes in the stochastic system owing to
(1.) the disease transmission rate, or owing to (2.) the natural death rates of the diﬀerent
disease classes-S, E, I, R exhibit direct impacts on the disease eradication process from the
population.
This is because comparing the results of Theorem 4.3 and Theorem 4.1[3.],
it is easy to see that if the stochastic system is inﬂuenced by signiﬁcant random ﬂuctu-


## Page 50


50
ations, where the source is from the natural death rate of susceptible individuals in the
population, that is, σS > 0, then by Theorem 4.1[3.], there is no disease-free steady state
for the population, and the disease cannot be eradicated by applying neither the threshold
conditions (R1 ≤1, U0 ≤1, and V0 ≤1) from Theorem 4.2, nor the threshold conditions
(R0 ≤1, ˆU0 ≤1, and ˆV0) from Theorem 4.3. More detailed discussions about the disease
eradication process under the inﬂuence of various intensity levels of the white noise processes
in the system are given in Section 5. Moreover, numerical evidence for the eﬀects of the in-
tensities of the white noise processes in the system on the disease eradication process are
presented in Section 6.
4.4. Asymptotic behavior when there is no infection-free steady state
As earlier remarked in Remark 3.1, it is expected from the existence of solution results in
Theorem 3.1[b.], that the absence of a positively-self invariant space for the sample paths of
the stochastic system (2.17)-(2.20), whenever the intensities satisfy σi > 0, ∀i ∈{S, E, I, R}
can lead to complex uncontrolled situations for the disease dynamics in the system. This
fact is true as it will be shown later in this section.
We recall that Theorem 4.1[3.] asserts that the stochastic system (2.17)-(2.20) has no
disease-free steady state for the population, whenever the intensity of the white noise process
from the natural death rate of the susceptible population is signiﬁcant, that is, σS > 0. This
study will be incomplete unless we know the long-term fate of the disease dynamics in the
human population, whenever there is no disease-free steady state wherein the disease can
be eradicated. One approach to investigate nonlinear stochastic dynamic systems (where
explicit solutions are nontrivial), whenever the infection-free steady state exists no where,
involves estimating the expected distance between the trajectories of the stochastic system,
and a potential disease-free steady state for the system. The estimate obtained generally


## Page 51


51
informs us about the extend to which the noise from the natural deathrate of the susceptible
class in the system (2.17)-(2.20) deviates the trajectories of the stochastic system from the
potential disease-free steady state.
Since the stochastic system (2.17)-(2.20) has the disease-free steady state E0 = (S∗
0, 0, 0), S∗
0 =
B
µ from Theorem 4.1[1.- 2.], whenever σS = 0, and loses the steady state, whenever σS > 0,
therefore E0 is always a potential infection-free steady state for the system (2.17)-(2.20).
The following result describes the oscillatory behavior of the trajectories of the stochas-
tic system (2.17)-(2.20) in the neighborhood of the potential disease-free equilibrium E0
obtained in Theorem 4.1[1.- 2.], whenever Theorem 4.1[3.] is satisﬁed, that is, whenever the
stochastic system (2.17)-(2.20) does not have a disease-free equilibrium. This result char-
acterizes the expected average relative distance between the sample paths of the stochastic
system (2.17)-(2.20) and the potential disease-free steady state E0. Moreover, this result
builds the backbone to gain more insights about the asymptotic oscillatory behavior of the
stochastic system (2.17)-(2.20), whenever the system is subjected under the inﬂuence of var-
ious intensity levels of the white noise processes in the system which is discussed further in
Section 5.
Theorem 4.4. Let the hypothesis of Theorem 4.1[3.] be satisﬁed. And deﬁne the following
threshold values:
˜R1 =
βS∗
0 ˆK1
(µ + d + α) +
α
(µ + d + α) +
ˆk1σ2
β + 1
2σ2
I
(µ + d + α),
(4.37)
˜U0 =
2βS∗
0 + β + α + 2
µ
˜
K(µ)2
2µ
+ σ2
S
2µ,
(4.38)
and
˜V0 = (2µ ˜K(µ)2 + α + β(2S∗
0 + 1))
2µ
+ σ2
E
2µ,
(4.39)
with some constants ˆK1 > 0, ˆk1 > 0 that depends on S∗
0 (in fact, ˆk1 = 6S∗
0 and ˆK1 = 4+S∗
0),
Let X(t) = (S(t), E(t), I(t)) be a solution of the decoupled system from (2.17)-(2.20) with
initial conditions (2.21). Assume that, ˜R1 ≤1, ˜U0 ≤1, and ˜V0 ≤1, then there exists a


## Page 52


52
positive constant m > 0, such that the following inequality holds
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
(4.40)
Proof: Let Theorem 4.1[3.] be satisﬁed. Applying the diﬀerential operator dV to V deﬁned
in (4.19), and utilizing (4.8) and (4.9), it is easy to see that
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
0 + U(t −u))G(W(t −s −u))dsdudwβ(t) (4.41)
where for some positive constant valued function ˜K(µ), the drift part of (4.41), LV , satisﬁes
the inequality
LV (x, t) ≤−

˜φU2(t) + ˜ψV 2(t) + ˜ϕW 2(t)

,
(4.42)
where
˜φ
=
2µ(1 −˜U0)
(4.43)
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
(4.44)
˜ϕ
=
2(µ + d + α)(1 −˜R1) −c(3βS∗
0 + β(S∗
0)2 + 4σ2
β(S∗
0)2) −2c2σ2
β(S∗
0)2.
(4.45)
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
˜ψ, and ˜ϕ are positive constants. Therefore, by integrating (4.41) from 0 to t on both sides


## Page 53


53
and taking the expectation, it follows from (4.41)-(4.45) that
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
(4.46)
where V (0) is constant and
m = min(˜φ, ˜ψ, ˜ϕ).
(4.47)
Hence, diving both sides of (4.46) by t and m, and taking the limit supremum as t →∞,
then (4.40) follows immediately.
The results of Theorem 4.4 are interpreted in the following. Theorem 4.4 signiﬁes that
under conditions that warrant the nonexistence of a disease free steady state for the stochastic
system (2.17)-(2.20), the asymptotic expected average relative distance between the white
noise inﬂuenced trajectories of the stochastic system and the potential disease-free steady
state, E0 obtained in Theorem 4.1[1.][2.], does not exceed a constant multiple of the intensity,
σS, of the white noise process from the natural deathrate of the susceptible population,
whenever the following threshold conditions ˜R1 ≤1, ˜U0 ≤1, and ˜V0 ≤1 are satisﬁed.
That is, asymptotically, when the physical characteristics in a disease scenario allow
signiﬁcant random ﬂuctuations in the natural deathrate of susceptible individuals which
lead to a white noise process with intensity value σS > 0, and consequently lead to the
nonexistence or no where existence of an infection-free population steady state, and also
allow physical conditions which mathematically can be represented by the parameters of the
stochastic system (2.17)-(2.20), wherein the threshold values ˜R1, ˜U0, and ˜V0 in (4.37)-(4.39)
can be computed, it follows that if the following threshold conditions ˜R1 ≤1, ˜U0 ≤1,
and ˜V0 ≤1 are satisﬁed, then the noise inﬂuenced population which is aﬀected by the
disease outbreak is expected to oscillate over time near the potential disease-free steady


## Page 54


54
state population E0 obtained in Theorem 4.1[1.][2.].
Furthermore, the size or amplitude of the oscillations is determined primarily by the size
of the intensity, σ2
S, of the white noise process from the natural death rate of the susceptible
individuals in the population. It is easily observed that for inﬁnitesimally small values for
the intensity of the white noise from the natural deathrate of the susceptible class, that is,
for σ2
S →0, it follows from (4.40) that all trajectories of the stochastic system (2.17)-(2.20)
converge on average (in expectation) to the disease-free steady state E0 asymptotically. In
addition, for continuous increase in the values σ2
S, that is, for σ2
S →∞, it is also easy to see
from (4.40) that the average distance of the trajectories of the stochastic system from the
potential infection-free steady state E0 gets wider apart. This observation signiﬁes that, the
stronger the noise in the system from the natural deathrate of the susceptible population gets,
the further and further away the system gets from the infection-free steady state wherein
the disease can be eradicated.
Also, the dependence of the size of the random oscillations of the state of the system
near the infection-free steady state E0, and also the dependence of the magnitude of the
threshold values ˜R1, ˜U0, and ˜V0 on the intensities of the white noise processes in the system,
σi, i = S, E, I, R, β, suggests as similarly remarked in Remark 4.2 and Remark 4.3, that the
source (disease transmission or natural death rates) and intensity levels2 of the white noise
processes in the system exert inﬂuence on the asymptotic oscillatory behavior of the system
near the potential disease-free population steady state, E0, obtained in Theorem 4.1[1.][2.].
This is obvious as it is already remarked above that as σ2
S →∞, the sample paths of the
stochastic system get further and further away from E0.
2The intensity levels of the white noise processes in the system are described as inﬁnitesimally small,
signiﬁcant in magnitude and small but not inﬁnitesimally small, big in size and ﬁnite, and suﬃciently large.


## Page 55


55
The examination of the inﬂuence of the source and intensity levels of the white noise
processes on the oscillatory behavior of the system near E0 is elaborated in Section 5. More-
over, numerical evidence for the eﬀects of the intensity levels of the white noise processes
in the system (2.17)-(2.20) on the oscillatory behavior of the system , such as population
extinction etc., over time are presented in Section 6.
Furthermore, as similarly remarked in Remark 4.3[2.], comparing the threshold values
from Theorem 4.3, Theorem 4.2, and Theorem 4.4, that is, R1, U0, V0 in (4.21)-(4.23), R0,
ˆU0, ˆV0 in (4.33)-(4.35), and ˜R1, ˜U0, ˜V0 in (4.37)-(4.39), it is easy to see that R0 ≤R1 = ˜R1,
U0 = ˆU0 ≤˜U0 and V0 ≤ˆV0 = ˜V0, whenever the intensity values of the white noise processes
in the system (2.17)-(2.20) satisfy the condition σi > 0, i = S, E, I, R, β. It is also easy to
see that the threshold value ˜U0 in (4.38) has been further constrained by the assumption
that σS > 0, from the corresponding threshold value U0 = ˆU0 in (4.22) and (4.34).
Meanwhile it was remarked in Remark 4.3[2.] that the threshold values R1, U0 and V0
from Theorem 4.2 would satisfy the threshold conditions R1 ≤1, U0 ≤1 and V0 ≤1 less
easily compared to the set of threshold values R0, ˆU0 and ˆV0 from Theorem 4.3, it is easy to
see that the threshold values ˜R1, ˜U0, and ˜V0 from Theorem 4.4 would satisfy the threshold
conditions ˜R1 ≤1, ˜U0 ≤1, and ˜V0 ≤1 also less easily when compared to he threshold values
R1, U0 and V0 from Theorem 4.2, and much less easily compared to the threshold values R0,
ˆU0 and ˆV0 from Theorem 4.3.
This observation suggests that the sources (natural death or disease transmission rates)
and intensity levels of random ﬂuctuations in the disease dynamics exhibit bearings on
(1.)
the existence of a disease-free population steady state for the system (2.17)-(2.20),
and also on (2.) the disease eradication conditions for the system. For instance, adding
the new source of random ﬂuctuations due to the natural death rate of the susceptible


## Page 56


56
population which leads to the white noise process with intensity σS, then for inﬁnitesimally
small values for σS, there exists a disease free population state, and the disease can be
eradicated, whenever the conditions in Theorem 4.3 and Theorem 4.2 are satisﬁed. But for
signiﬁcant in magnitude values of the intensity σS > 0, the additional source of the white
noise from the random ﬂuctuations in the natural deathrate of the susceptible individuals
leads to a loss or nonexistence of the disease-free population steady state. Moreover, in such
events where the disease-free steady state ceases to exist, the solutions of the system (2.17)-
(2.20) can oscillate closely to the potential disease-free population steady state E0 obtained
in Theorem 4.1[1.][2.], provided that the conditions ˜R1 ≤1, ˜U0 ≤1, and ˜V0 ≤1 are satisﬁed,
and the value of the intensity σS is also relatively small, that is, σS →0.
Furthermore, as similarly remarked in Remark 4.3[2.], the results of Theorem 4.4 suggest
that in a disease outbreak scenario that exhibits random ﬂuctuations with high intensity
values for the noise from the natural deathrate of susceptible population, that is, σS > 0,
and as a result does not allow the existence of an infection-free steady state population, but
exhibit physical characteristics which can be represented mathematically by the parameters
of the system (2.17)-(2.20), wherein the threshold values ˜R1, ˜U0, and ˜V0 in (4.37)-(4.39),
R1, U0, V0 in (4.21)-(4.23) and R0, ˆU0, ˆV0 in (4.33)-(4.35) can all be computed, and satisfy
the following relationship between the threshold values and also the threshold conditions
given by R0 ≤R1 = ˜R1 ≤1, U0 = ˆU0 ≤˜U0 ≤1 and V0 ≤ˆV0 = ˜V0 ≤1, then the
occurrence of the white noise processes from the random environmental ﬂuctuations in all
other sources namely:- from (1.)
the natural deathrates of the exposed, infectious and
removal populations, and also from (2.)
the disease transmission rate, exerts additional
counter-positive constraints against the disease eradication process as determined by the
relationships between the threshold values, and the threshold conditions R0 ≤R1 = ˜R1 ≤1,


## Page 57


57
U0 = ˆU0 ≤˜U0 ≤1 and V0 ≤ˆV0 = ˜V0 ≤1.
That is, whereas the disease can be eradicated much less rapidly when the disease scenario
represented by (2.17)-(2.20) is controlled by the threshold values R1, U0, V0 in (4.21)-(4.23)
than when it is controlled by the threshold values R0, ˆU0, ˆV0 in (4.33)-(4.35), it follows that
when the disease scenario is controlled by the threshold values ˜R1, ˜U0, and ˜V0 in (4.37)-(4.39),
the disease cannot be eradicated. Nevertheless, the disease population can be maintained
close to a potential disease-free population steady state E0 obtained in Theorem 4.1[1.][2.],
whenever the intensity σs is small, and the threshold conditions ˜R1 ≤1, ˜U0 ≤1, and ˜V0 ≤1
are satisﬁed.
The oscillatory behavior of the system (2.17)-(2.20) relative to E0 obtained in Theo-
rem 4.1[1.][2.] under the inﬂuence of various intensity levels of the white noise processes in
the system is discussed further in Section 5.
5. Asymptotic behavior of the system subjected under various orders for the
intensities of noise
This section exhibits the asymptotic properties of the stochastic system (2.17)-(2.20),
whenever it is subjected under the direct inﬂuence of various growth orders of the intensities
of the white noise processes in the system. The techniques applied in Wanduku [36, 32] are
used to classify the intensities of the white noises in the system, and to study their impacts
on the disease eradication in the steady state population.
In Section 4, several observations were made about the bearings of the source (natural
death or disease transmission rates) and intensity levels of the white noise processes in
the system on (1)the existence and stability of the disease free steady state population E0
obtained in Theorem 4.1[1.-2.], and consequently on (2) the disease eradication and also on


## Page 58


58
(3) the expected distance between the solutions of the system (2.17)-(2.20) and the potential
disease free equilibrium E0. In this section, several special disease scenarios are characterized
to give more insight about the properties - (1), (2) and (3), with respect to the stochastic
system (2.17)-(2.20).
The special disease scenarios are determined by the qualitative behaviors of the inten-
sities, σ2
i , i = S, E, I, R, β, of the white noise processes originating from the natural death
and disease transmission rates in the system. Furthermore, the qualitative character of the
intensities of the white noise processes are classiﬁed in Hypothesis 5.1. The following deﬁni-
tions in [36, 32] are helpful to understand the assumptions made about the intensity levels
of the white noise processes described in Hypothesis 5.1:
Deﬁnition 5.1. Given two real valued functions f and g,
1. if ∃k > 0, and n0, such that ∀n > n0, |f(n)| ≤k|g(n)|, we say that f is big-o of g, and
is denoted by f(n) = 0(g(n)) or f = 0(g). If f(n) →0, as n →∞, that is, f turns in the
limit to a zero function for suﬃciently large n, we write f = 0(ǫ) or f(n) = 0( 1
n), for ǫ > 0.
Also, if f(n) is a constant function as n →∞, we write f(n) = 0(1).
2. if ∃k1, k2 > 0, and n0, such that ∀n > n0, k1|g(n)| ≤|f(n)| ≤k2|g(n)|, we say that f
is big-theta of g, and is denoted by f(n) = θ(g(n)). If f(n) →∞as n →∞, we write
f(n) = θ(n) or f = θ( 1
ǫ), for ǫ > 0.
The hypothesis that follows compares the intensity levels of the white noise processes from
the following (1) the disease transmission rate, (2) the natural death rate of the susceptible
population, and (3) the natural death rates of the three other subcategories - exposed,
infectious and removal populations.
Hypothesis 5.1. Using Deﬁnition 5.1, we assume that
H1: σβ →0, σS →0, σi →0, ∀i = E, I, R,
⇐⇒
σβ = 0(ǫ), σS = 0(ǫ), σi = 0(ǫ), ∀i =
E, I, R;
H2: σβ < ∞, σS →0, σi →0, ∀i = E, I, R,
⇐⇒
σβ = 0(1), σS = 0(ǫ), σi = 0(ǫ), ∀i =
E, I, R;
H3: σβ < ∞, σS →0, σi < ∞, ∀i = E, I, R, ⇐⇒σβ = 0(1), σS = 0(ǫ), σi = 0(1), ∀i =
E, I, R;


## Page 59


59
H4: (σβ →0, or σβ < ∞) and σS < ∞, and (σi →0 or σi < ∞, ∀i = E, I, R),
⇐⇒
(σβ = 0(ǫ), or σβ = 0(1) ), and σS = 0(1), and (σi = 0(ǫ) or σi = 0(1), ∀i = E, I, R;
H5: σβ →∞, σS →0, σi →0, ∀i = E, I, R, ⇐⇒σβ = θ( 1
ǫ), σS = 0(ǫ), σi = 0(ǫ), ∀i =
E, I, R;
H6: σβ →∞, σS →0, σi →∞, ∀i = E, I, R, ⇐⇒σβ = θ( 1
ǫ), σS = 0(ǫ), σi = θ( 1
ǫ), ∀i =
E, I, R;
H7: (σβ →∞, or σβ →0, or σβ < ∞), and (σS →∞), and (σi →∞, or σi < ∞, or
σi →0, ∀i = E, I, R), ⇐⇒(σβ = θ( 1
ǫ), or σβ = 0(ǫ), or σβ = 0(1)), and (σS = θ( 1
ǫ)), and
(σi = θ( 1
ǫ), or σi = 0(1), or σi = 0(ǫ), ∀i = E, I, R).
Hypothesis 5.1[H1] asserts that all the intensities, σi, i = S, E, I, R, β, of the white noise
processes in the system continuously decrease in size to inﬁnitesimally small values.
Hypothesis 5.1[H2] assumes that the intensity σβ of the white noise process from the dis-
ease transmission rate is ﬁnite in size, but the other white noise intensities σi, i = S, E, I, R
from the natural deathrates of the susceptible, exposed and infectious populations continu-
ously decrease in size to inﬁnitesimally small values.
Hypothesis 5.1[H3] assumes that the intensities σβ, σi, i = E, I, R of the white noise
processes from the disease transmission rate, and the natural deathrates of the exposed,
infectious and removal populations are ﬁnite in size, meanwhile the intensity, σS, of the
white noise process from the natural deathrate of the susceptible population continuously
decreases in size to inﬁnitesimally small values.
Hypothesis 5.1[H4] asserts that the intensity, σβ, of the white noise process from the
disease transmission rate either continuously decreases in size to inﬁnitesimally small values
or it is signiﬁcant and ﬁnite in size. At the same time, the intensities, σi, i = E, I, R, of the
white noise processes from the natural death rates in the exposed, infectious and removal
populations are also either signiﬁcant and ﬁnite in size, or they all continuously decrease in
size to inﬁnitesimally small values, meanwhile the intensity, σS, of the white noise process
from the natural deathrate of the susceptible population is signiﬁcant and ﬁnite in size.


## Page 60


60
Hypothesis 5.1[H5] states that the intensity, σβ, of the white noise process from the
disease transmission rate continuously increases in size to suﬃciently large values, whereas
the intensities, σi, i = S, E, I, R, of the white noise processes from the natural deathrates of
the susceptible, exposed, infectious and removal populations continuously decrease in size to
inﬁnitesimally small values.
Hypothesis 5.1[H6] assumes that the intensities, σi, i = E, I, R, β, of the white noise
processes from the disease transmission rate and the natural deathrates of the exposed,
infectious and removal populations continuously increase in size to suﬃciently large values,
but the intensity, σS, of the white noise process from the natural deathrate of the susceptible
population continuously decreases in size to inﬁnitesimally small values.
Hypothesis 5.1[H7] states that the intensities, σi, i = E, I, R, β, of the white noise pro-
cesses from the disease transmission rate and natural deathrates of the exposed, infectious
and removal populations either continuously increase in size to suﬃciently large values, or
they are signiﬁcant and ﬁnite in size, or they continuously decrease in size to inﬁnitesimally
small values, while the intensity, σS, of the white noise process from the natural deathrate
of the susceptible population continuously increases in size to suﬃciently large values.
The following results characterize the qualitative behavior of the solutions of the stochas-
tic system (2.17)-(2.20) under the assumptions of Hypothesis 5.1.
Theorem 5.1. If Hypothesis 5.1[H1] holds, then there exists a disease free equilibrium pop-
ulation E0 = (S∗
0, 0, 0), S∗
0 = B
µ for the stochastic system (2.17)-(2.20). Furthermore, there
exists threshold values R1, U0 and V0 deﬁne as follows:
R1 = βS∗
0 ˆK1 + α
(µ + d + α) +
α
(µ + d + α),
(5.1)
U0 =
2βS∗
0 + β + α + 2
µ
˜
K(µ)2
2µ
,
(5.2)


## Page 61


61
and
V0 = (2µ ˜K(µ)2 + α + β(2S∗
0 + 1))
2µ
,
(5.3)
with some constants ˆK1 > 0, ˆk1 > 0 that depends on S∗
0 (in fact, ˆk1 = 6S∗
0 and ˆK1 = 4+S∗
0),
such that under the assumptions that R1 ≤1, U0 ≤1, and V0 ≤1, the disease free equilibrium
state is stochastically asymptotically stable in the large in D(∞). Moreover, it is mean square
stable.
Proof: Let σβ = 0(ǫ), σS = 0(ǫ), σi = 0(ǫ), ∀i = E, I, R. It follows from the Theorem 4.1 that
(2.17)-(2.20) has a disease free steady state given by E0 = (S∗
0, 0, 0), S∗
0 = B
µ . Furthermore,
the rest of the result follows immediately from Lemma 4.3 and Theorem 4.2.
Remark 5.1. Theorem 5.1 signiﬁes that when the stochastic system (2.17)-(2.20) is contin-
uously inﬂuenced by white noise processes from the disease transmission and natural death
rates that have intensity values that continuously decrease in size to inﬁnitesimally small
values, the system has a disease-free steady state population E0, and the steady state is
stochastically asymptotically stable in the large, whenever the threshold conditions R1 ≤1,
U0 ≤1, and V0 ≤1 given in (5.1)-(5.3) are satisﬁed.
This result suggests that in a disease scenario where the disease outbreak results in ran-
dom ﬂuctuations in the disease transmission rate and in the natural death rates of all the
subclasses-susceptible, exposed, infectious and removal populations, there exists a disease-
free population steady state for the population given by E0 = (S∗
0, 0, 0), S∗
0 = B
µ , whenever the
random environmental ﬂuctuations in the disease transmission rate and also in the natural
death processes have inﬁnitesimally small intensity values. Furthermore, when the physical
characteristics of the disease scenario can be mathematically represented by the parameters
of the system (2.17)-(2.20), wherein the threshold values R1, U0 and V1 from (5.1)-(5.3) can
be computed, then the disease can be eradicated from the population, whenever the threshold
conditions R1 ≤1, U0 ≤1, and V0 ≤1 are satisﬁed.
Theorem 5.2. If Hypothesis 5.1[H2] holds, then there exists a disease free equilibrium pop-
ulation E0 = (S∗
0, 0, 0), S∗
0 = B
µ for the stochastic system (2.17)-(2.20). Furthermore, there
exists threshold values R1, U0 and V0 deﬁne as follows:
R1 =
βS∗
0 ˆK1
(µ + d + α) +
α
(µ + d + α) +
ˆk1σ2
β
(µ + d + α),
(5.4)
U0 =
2βS∗
0 + β + α + 2
µ
˜
K(µ)2
2µ
,
(5.5)


## Page 62


62
and
V0 = (2µ ˜K(µ)2 + α + β(2S∗
0 + 1))
2µ
,
(5.6)
with some constant ˆK1 > 0 that depends on S∗
0 (in fact, ˆK1 = 4 + S∗
0 + 1
β6σ2
β) such that,
under the assumptions that R1 ≤1, U0 ≤1, and V0 ≤1, the disease free equilibrium state is
stochastically asymptotically stable in the large in D(∞). Moreover, it is mean square stable.
Proof: Let σβ = 0(1), σS = 0(ǫ), σi = 0(ǫ), ∀i = E, I, R. It follows from the Theorem 4.1 that
(2.17)-(2.20) has a disease free steady state given by E0 = (S∗
0, 0, 0), S∗
0 = B
µ . Furthermore,
the rest of the result follows immediately from Lemma 4.3 and Theorem 4.2.
Theorem 5.3. If Hypothesis 5.1[H3] holds, then there exists a disease free equilibrium pop-
ulation E0 = (S∗
0, 0, 0), S∗
0 = B
µ for the stochastic system (2.17)-(2.20). Furthermore, there
exists threshold values R1, U0 and V0 deﬁne as follows:
R1 =
βS∗
0 ˆK1
(µ + d + α) +
α
(µ + d + α) +
ˆk1σ2
β + 1
2σ2
I
(µ + d + α),
(5.7)
U0 =
2βS∗
0 + β + α + 2
µ
˜
K(µ)2
2µ
,
(5.8)
and
V0 = (2µ ˜K(µ)2 + α + β(2S∗
0 + 1))
2µ
+ σ2
E
2µ,
(5.9)
with some constants ˆK1 > 0, ˆk1 > 0 that depend on S∗
0 (in fact, ˆk1 = 6S∗
0 and ˆK1 =
4 + S∗
0), such that, under the assumptions that R1 ≤1, U0 ≤1, and V0 ≤1, the disease free
equilibrium state is stochastically asymptotically stable in the large in D(∞). Moreover, it is
mean square stable.
Proof: Let σβ = 0(1), σS = 0(ǫ), σi = 0(1), ∀i = E, I, R. It follows from the Theorem 4.1 that
(2.17)-(2.20) has a disease-free steady state given by E0 = (S∗
0, 0, 0), S∗
0 = B
µ . Furthermore,
the rest of the result follows immediately from Lemma 4.3 and Theorem 4.2.
Remark 5.2. Theorem 5.2 and Theorem 5.3 signify that when the stochastic system (2.17)-
(2.20) is continuously inﬂuenced by white noise processes from the disease transmission rate
and natural deathrates where the intensity σβ of the white noise from the disease transmission
rate is signiﬁcant and ﬁnite in size, and the intensity σS of the white noise from the natural


## Page 63


63
deathrate of the susceptible population continuously decreases in size to inﬁnitesimally small
values, whereas the intensities, σi, i = E, I, R, of the white noise processes from the natural
deathrates of the exposed, infectious and removal populations are either signiﬁcant and ﬁnite
in size, or they continuously decrease in sizes to inﬁnitesimally small values, it follows that
the system has a disease-free steady state population E0, and the steady state is stochastically
asymptotically stable in the large, whenever the threshold conditions R1 ≤1, U0 ≤1, and
V0 ≤1 in (5.4)-(5.6) and (5.7)-(5.9) are satisﬁed.
This result suggests that in a disease scenario where the disease outbreak results in random
ﬂuctuations in the disease transmission and natural death rates, there exists a disease-free
population steady state for the population given by E0 = (S∗
0, 0, 0), S∗
0 = B
µ , whenever the ran-
dom environmental ﬂuctuations in the disease transmission rate have signiﬁcant and ﬁnite
intensity values, and the environmental ﬂuctuations in the natural deathrate of the susceptible
population has inﬁnitesimally small intensity values, regardless of whether there exists signif-
icant and ﬁnite in sizes, or there exists inﬁnitesimally small intensity values for the random
ﬂuctuations from the natural deathrates of the exposed, infectious and removal populations.
Furthermore, when the physical characteristics of the disease dynamics can be represented
by the parameters of the system (2.17)-(2.20), wherein the threshold values R1, U0 and V1
from (5.4)-(5.6) and (5.7)-(5.9) can be computed, then the disease can be eradicated from
the population, whenever the threshold conditions R1 ≤1, U0 ≤1, and V0 ≤1 are satisﬁed.
The following result characterizes the behavior of the solutions of the stochastic system
(2.17)-(2.20) whenever the assumption of Hypothesis 5.1[H4] is satisﬁed. For simplicity, the
results are presented only for the subcase when σβ = 0(ǫ) , σS = 0(1), and σi = 0(ǫ), ∀i =
E, I, R. The other subcases can similarly be derived.
Theorem 5.4. If Hypothesis 5.1[H4] holds, then there is no disease free equilibrium popu-
lation state for the stochastic system (2.17)-(2.20). But, when σβ = 0(ǫ) , σS = 0(1), and
σi = 0(ǫ), ∀i = E, I, R, there exists threshold values:
˜R1 =
βS∗
0 ˆK1
(µ + d + α) +
α
(µ + d + α),
(5.10)
˜U0 =
2βS∗
0 + β + α + 2
µ
˜
K(µ)2
2µ
+ σ2
S
2µ,
(5.11)
and
˜V0 = (2µ ˜K(µ)2 + α + β(2S∗
0 + 1))
2µ
,
(5.12)
with some constant ˆK1 > 0 that depends on S∗
0 (in fact, ˆK1 = 4 + S∗
0), such that letting


## Page 64


64
X(t) = (S(t), E(t), I(t)) be a solution of the decoupled system from (2.17)-(2.20) with ini-
tial conditions (2.21) then there exists a positive constant m > 0, such that the following
inequality holds
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
,
(5.13)
whenever ˜R1 ≤1, ˜U0 ≤1, and ˜V0 ≤1.
Proof: Let (σβ = 0(ǫ), or σβ = 0(1) ) and σS = 0(1), and (σi = 0(ǫ) or σi = 0(1), ∀i =
E, I, R). It follows from the Theorem 4.1[3.] that (2.17)-(2.20) does not have a disease free
steady state. Furthermore, when σβ = 0(ǫ) , σS = 0(1), and σi = 0(ǫ), ∀i = E, I, R, the rest
of the result follows immediately from Theorem 4.4.
Remark 5.3. Theorem 5.4 signiﬁes that when the stochastic system (2.17)-(2.20) is con-
tinuously inﬂuenced by the white noise processes from the disease transmission and natural
death rates, where the intensity value σβ of the white noise process from the disease trans-
mission process is signiﬁcant and ﬁnite in size, or it continuously decreases in size to an
inﬁnitesimally small value, and the intensity value σS of the white noise process from the
natural deathrate in the susceptible population is signiﬁcant and also ﬁnite in size, mean-
while the intensities, σi, i = E, I, R, of the white noise processes from the natural deathrates
of the exposed, infectious and removal populations are either signiﬁcant and ﬁnite in size, or
they continuously decrease in size to inﬁnitesimally small values, it follows that the system
(2.17)-(2.20) does not have any disease-free steady state for the population. Nevertheless,
the solutions of the system (2.17)-(2.20) continue to oscillate near the potential disease-free
steady state E0 = (S∗
0, 0, 0), S∗
0 = B
µ obtained from Theorem 4.1[1.]-[2.], whenever the thresh-
old conditions ˜R1 ≤1, ˜U0 ≤1, and ˜V0 ≤1 in (5.10)-(5.12) are satisﬁed. Moreover, the size
or amplitude of the oscillations of the solutions of (2.17)-(2.20) relative to the disease free
steady state E0 = (S∗
0, 0, 0), S∗
0 = B
µ , is proportional to the size of the intensity σS. This im-
plies that small values of σS result in small asymptotic expected average distance between the
solutions of (2.17)-(2.20) and the potential disease free steady state E0 = (S∗
0, 0, 0), S∗
0 = B
µ
and vice versa.
This result suggests that in a disease scenario where the disease outbreak results in random
ﬂuctuations in the disease transmission and natural death rates, when the random environ-
mental ﬂuctuations in the natural deathrate of the susceptible population has a signiﬁcant
and ﬁnite intensity value σS, the disease-free steady state population exists no where. Never-
theless, the states of the population ( which includes all subclasses- S, E, I, R) will oscillate
over time near the potential disease-free steady state population E0 = (S∗
0, 0, 0), S∗
0 =
B
µ ,


## Page 65


65
whenever the threshold conditions ˜R1 ≤1, ˜U0 ≤1, and ˜V0 ≤1 in (5.10)-(5.12) are satisﬁed.
Moreover, for small values of the intensity σS, the size of the oscillations of the population
relative to E0 is small proportionately to the size of σS.
This implies that in this disease scenario, whereas the disease can not be eradicated by
applying the threshold conditions in Theorem 4.2, it follows that when the intensity value,
σS, of the random ﬂuctuations in the natural deathrate of the susceptible population is small
in size, the population states aﬀected by the disease outbreak can be contained closely to the
potential disease-free steady state E0 = (S∗
0, 0, 0), S∗
0 = B
µ , whenever the threshold values ˜R1,
˜U0, and ˜V0 satisfy the threshold conditions ˜R1 ≤1, ˜U0 ≤1, and ˜V0 ≤1.
In addition, the states of the population will continue to oscillate over time near the
potential disease-free steady state E0 , regardless of the size of the intensities σi, i = E, I, R, β
of the random ﬂuctuations in the disease transmission rate, or in the natural death rates of
the exposed, infectious and removal individuals in the population, provided that the intensity
values σi, i = E, I, R, β are small in magnitude.
Theorem 5.5. If Hypothesis 5.1[H5] holds, then there exists a disease free equilibrium pop-
ulation E0 = (S∗
0, 0, 0), S∗
0 = B
µ for the stochastic system (2.17)-(2.20). But, the disease free
equilibrium state is stochastically unstable in D(∞).
Proof: Let σβ = θ( 1
ǫ), σS = 0(ǫ), σi = 0(ǫ), ∀i = E, I, R. It follows from the Theorem 4.1[1.-
2.]
that (2.17)-(2.20) has a disease free steady state given by E0 = (S∗
0, 0, 0), S∗
0 =
B
µ .
Furthermore, for any Lyapunov functional V , the diﬀerential operator LV associated with
the Ito-Doob type system (2.17)-(2.20) has the following structure:
LV (x) = Vt(x) + Vx(x)˜f(x) + 1
2˜gT(x)Vxx(x)˜g(x),
(5.14)
where ˜f(x) and ˜g(x) are vectors representing the drift and diﬀusion parts of the system (2.17)-
(2.20). It is easy to see that under the assumption of σβ = θ( 1
ǫ), the diﬀusion part ˜g(x) =
θ( 1
ǫ). Consequently, it follows from (5.14) that LV (x) = θ( 1
ǫ), ∀V . It follows further from
Lyapunov stability comparative results that the steady state E0 is stochastically unstable.
Theorem 5.6. If Hypothesis 5.1[H6] holds, then there exists a disease-free equilibrium pop-
ulation E0 = (S∗
0, 0, 0), S∗
0 = B
µ for the stochastic system (2.17)-(2.20). But, the disease free
equilibrium state is stochastically unstable in D(∞).


## Page 66


66
Proof: Let σβ = θ( 1
ǫ), σS = 0(ǫ), σi = θ( 1
ǫ), ∀i = E, I, R. It follows from the Theorem 4.1[1.-
2.]
that (2.17)-(2.20) has a disease free steady state given by E0 = (S∗
0, 0, 0), S∗
0 =
B
µ .
Furthermore, for any Lyapunov functional V , the diﬀerential operator LV associated with
the Ito-Doob type system (2.17)-(2.20) has the following structure:
LV (x) = Vt(x) + Vx(x)˜f(x) + 1
2˜gT(x)Vxx(x)˜g(x),
(5.15)
where ˜f(x) and ˜g(x) are vectors representing the drift and diﬀusion parts of the system
(2.17)-(2.20). It is easy to see that under the assumption of σβ = θ( 1
ǫ), the diﬀusion part
˜g(x) = θ( 1
ǫ). Consequently, it follows from (5.15) that LV (x) = θ( 1
ǫ), ∀V . Therefore, from
Lyapunov stability comparative results, the steady state E0 is stochastically unstable.
Remark 5.4. Theorem 5.5 and Theorem 5.6 signify that when the stochastic system (2.17)-
(2.20) is continuously inﬂuenced by white noise processes from the disease transmission
and natural death rates, where the intensity value σS of the white noise process from the
natural deathrate of the susceptible population continuously decreases in size to inﬁnites-
imally small values, then the system has a disease free steady state population given by
E0 = (S∗
0, 0, 0), S∗
0 = B
µ , regardless of the sizes of the intensities σi, i = E, I, R, β of the white
noise processes from the disease transmission rate and natural deathrates of the exposed,
infectious and removal populations. But the disease free steady state population E0 that ex-
ists is clearly stochastically unstable, whenever the intensities σi, i = E, I, R, β of the white
noise processes from the disease transmission rate or the natural deathrates of the exposed,
infectious and removal populations continuously increase in size to suﬃciently large values.
This result suggests that in a disease scenario where the disease outbreak results in random
ﬂuctuations in the disease transmission rate and natural deathrates, there exists a disease
free steady state for the population given by E0 = (S∗
0, 0, 0), S∗
0 =
B
µ , whenever the ran-
dom environmental ﬂuctuations in the natural deathrate of the susceptible population have
inﬁnitesimally small intensity values, regardless of the sizes of the intensity values of the ran-
dom environmental ﬂuctuations in the disease transmission rate and the natural deathrates of
the exposed, infectious and removal individuals in the population. However, the suﬃciently
large intensity values for the random ﬂuctuations in the disease transmission rate or the nat-
ural deathrates of the exposed, infectious and removal populations quickly ”drive” all sample
paths of the diﬀerent population states away from the disease free population steady state E0,
and consequently adversely favoring conditions that allow the disease to establish an endemic
stable steady state or a stable signiﬁcant number of the disease related classes-infectious,


## Page 67


67
exposed and removal individuals in the population. This result further suggests that signiﬁ-
cantly high intensity values for random ﬂuctuations in the disease transmission rate and the
natural deathrates of the exposed, infectious and removal populations exert strong negative
conditions against the disease eradication process. Numerical simulation results in Section 6
show that the high intensity values for the random ﬂuctuations in the disease transmission
rate or the natural deathrates of the exposed, infectious and removal populations lead to a
general decrease in the average total population size over time, which in some cases may lead
to the population extinction for suﬃciently large intensity values.
The following result describes the behavior of the solutions of the system (2.17)-(2.20) under
the assumptions of Hypothesis 5.1[H7]. For simplicity only the special case of σβ = 0(1),
and σS = θ( 1
ǫ), and σi = θ( 1
ǫ), ∀i = E, I, R. The results for the other cases can be similarly
derived.
Theorem 5.7. If Hypothesis 5.1[H7] holds, then there is no disease free equilibrium popula-
tion for the stochastic system (2.17)-(2.20). Furthermore, when σβ = 0(1), σS = θ( 1
ǫ), and
σi = θ( 1
ǫ), ∀i = E, I, R, the system does not oscillate in the neighborhood of the potential
disease free equilibrium E0 = (S∗
0, 0, 0), S∗
0 = B
µ obtained from Theorem 4.1[1.-2.].
Proof: Let σβ = 0(1), and σS = θ( 1
ǫ), and σi = θ( 1
ǫ), ∀i = E, I, R. It follows from the
Theorem 4.1[3.] that (2.17)-(2.20) does not have a disease free steady state. Furthermore,
the rest of the result follows immediately from the Proof of Theorem 4.4.
Remark 5.5. Theorem 5.7 signiﬁes that when the stochastic system (2.17)-(2.20) is contin-
uously inﬂuenced by the white noise processes from the disease transmission rate and natural
deathrates, where the intensity value σS of the white noise process from the natural deathrate
of the susceptible population continuously increases in size to suﬃciently large values, then
it follows from Theorem 4.1[3.] that the system (2.17)-(2.20) does not have a disease free
steady state population. Moreover, the signiﬁcantly large intensity values σi, i = E, I, R of
the white noise processes from the natural deathrates of the exposed, infectious or removal
populations lead to signiﬁcantly large threshold values ˜R1, ˜U0, and ˜V0 in (4.37)-(4.39), that
violate the threshold conditions, ˜R1 ≤1, ˜U0 ≤1, and ˜V0 ≤1 in Theorem 4.4. This implies
that the solutions of the system (2.17)-(2.20) do no longer oscillate near the disease free
steady state E0 obtained from Theorem 4.1[1.-2.].
Furthermore, for σS = θ( 1
ǫ), it follows from (4.40) that the asymptotic expected average
distance between the solutions of (2.17)-(2.20) and potential disease free equilibrium state E0
obtained from Theorem 4.1[1.-2.] is of the order θ( 1
ǫ). This also implies that the suﬃciently


## Page 68


68
large intensity values of σS lead to oscillations in the disease dynamics with very large oscilla-
tion sizes for the sample paths of the diﬀerent states of the population over time. In addition,
the sample paths of the diﬀerent states of the population oscillate over time at signiﬁcantly
large distances away from the potential disease-free equilibrium state E0 = (S∗
0, 0, 0), S∗
0 = B
µ
obtained from Theorem 4.1[1.-2.].
Thus, the disease can never be eradicated under the conditions of Theorem 5.7. More-
over, the numerical simulation results in Section 6 show that the high intensity values,
σi, i = E, I, R, β, for the random ﬂuctuations in the disease transmission rate or the natural
deathrates of the susceptible, exposed, infectious and removal populations lead to a general
decrease in the average total population size over time, which in some cases may lead to the
population extinction for suﬃciently large intensity values.
This result suggests that in a disease scenario where the disease outbreak results in random
ﬂuctuations in the disease transmission rate and natural deathrates, it follows that when the
random environmental ﬂuctuations in the natural deathrate of the susceptible population
exhibit suﬃciently large intensity values, then the population does not exhibit a disease-free
population steady state. Furthermore, when the intensity value of the random ﬂuctuations in
the natural death rates of the exposed, or infectious or removal populations is also suﬃciently
large in size, then the diﬀerent states of the population oscillates over time at a farther
distance away from the potential disease free population steady state E0 = (S∗
0, 0, 0), S∗
0 = B
µ
wherein the disease would be eradicated, regardless of the size of the intensity value, σβ, of
the random ﬂuctuations in the disease transmission rate. This implies that in this disease
scenario, the population experiencing the disease outbreak cannot contain the disease.
6. Example
6.1. Example 1: The eﬀect of the intensity of the white noise process on disease eradication:
This example illustrates the results in Theorem 4.2 and Lemma 4.3, and also provides
numerical evidence in support of the results in Section 5 that characterize the eﬀects of the
intensity of the white noise processes in the system originating from the random ﬂuctuations
in the disease dynamics on the stochastic asymptotic stability of the system in relation to
the disease free equilibrium E0 = (S∗
0, 0, 0), S∗
0 = B
µ . Recall, Theorem 4.2 and Lemma 4.3
provide conditions for the threshold values R1, U0, and V0 deﬁned in (4.21)-(4.23) which
are suﬃcient for the stochastic stability of E0 and consequently for disease eradication.
For simplicity in this example, the following assumptions are considered:- (a1) there are


## Page 69


69
no random ﬂuctuations in the disease dynamics due to the natural death of susceptible
individuals, that is, the intensity of the white noise due to the random ﬂuctuations in the
natural death of susceptible individuals σS = 0. Indeed, from Theorem 4.2 and Lemma 4.3,
there exists a stable disease free equilibrium E0, whenever σS = 0 and the threshold values
satisfy R1 ≤1, U0 ≤1, and V0 ≤1. (a2) It is also assumed that the intensities of the
white noise processes in the system due to the random ﬂuctuations in the natural death and
disease transmission processes for the other disease classes-exposed, infectious and removal
are equal, that is, σE = σI = σR = σβ = σ.
The list of system parameter values in Table 1 are used to generate diﬀerent values for
R1, U0, and V0 under continuous changes in the values of σ = σE = σI = σR = σβ. The
Figure 2 depicts the results for R1 and V0. For U0, it follows from Table 1 and (4.22) that
U0 ≈1, where ˜K(µ) = 0.999991.
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


## Page 70


70
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
Figure 2: (a) and (b) Show the values of the noise modiﬁed basic reproduction number, R1, (deﬁned in (4.21))
and the threshold parameter V0 (deﬁned in (4.23)) over continuous changes in the values of the intensities
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
a stable endemic population. Note that the observations of this example are consistent with the results in
Theorems [5.1-5.3,& 5.5-5.6].


## Page 71


71
6.2. Example 2: Eﬀect of the intensity of white noise on the trajectories of the system
The list of convenient choice of parameter values in Table 2 are used to generate the
trajectories of the stochastic system (2.17)-(2.20) in order to (1.) illustrate the impact of
the source of the white noise process in the system (owing to the random ﬂuctuations in
the natural death or disease transmission processes) and also to (2.) illustrate the eﬀect
of the intensity of the white noise process in the system on the trajectories of the diﬀerent
disease classes in the system, in order to uncover the overall behavior of the system over time.
The Euer-Maruyama stochastic approximation scheme3 is used to generate trajectories for
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
the diﬀerent states S(t), E(t), I(t), R(t) over the time interval [0, T], where T = max(T1 +
T2, T3) = 4. The special nonlinear incidence functions G(I) =
aI
1+I , a = 0.05 in [27] is utilized
3A seed is set on the random number generator to reproduce the same sequence of random numbers for
the Brownian motion in order to generate reliable graphs for the trajectories of the system under diﬀerent
intensity values for the white noise processes, so that comparison can be made to identify diﬀerences that
reﬂect the eﬀect of intensity values.


## Page 72


72
to generate the numeric results. Furthermore, the following initial conditions are used
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
σi = O(ǫ), i = S, E, I, R, β
Figure 3
10.06048
4.979256
5.704827
1.975407
σi = O(ǫ), i = S, E, I, R, and σβ = 0.5
Figure 4
10.04129
4.978257
5.687113
1.973783
σi = O(ǫ), i = S, E, I, R, and σβ = 9
Figure 5
9.681482
4.906452
5.385973
1.94617
σi = 0.5, i = E, I, R, and σS = σβ = O(ǫ)
Figure 6
10.06048
4.715779
5.42661
1.845652
σi = 0.5, i = S, E, I, R, and σβ = O(ǫ)
Figure 7
9.553725
4.692877
5.42661
1.845652
σi = 9, i = S, E, I, R, and σβ = O(ǫ)
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
1. When σi = O(ǫ), i = S, E, I, R, there is moderate decrease in the average values ¯S, ¯E, ¯I, ¯R
of S, E, I, R from the trajectories in Figures 3-5 as σβ increases from σβ = O(ǫ) to σβ = 9.
2. When σβ = O(ǫ), there is a sharp decrease in the average values ¯S, ¯E, ¯I, ¯R of S, E, I, R
from the trajectories in Figure 3, and Figures 7-8 as σi, i = S, E, I, R increases from σi =
O(ǫ), i = S, E, I, R to σi = 9, i = S, E, I, R.
3. When all the σi’s , that is, σi, i = S, E, I, R, β equally increase together from σi = O(ǫ), i =
S, E, I, R, β to σi = 9, i = S, E, I, R, β, there is a sharper decrease in the average values
¯S, ¯E, ¯I, ¯R of S, E, I, R from the trajectories in Figure 3, and Figures 9-10.


## Page 73


73
4. When σS = σβ = O(ǫ), there is no change in the average value ¯S of S and there is moderate
decrease in the average values ¯E, ¯I, ¯R of E, I, R from the trajectories in Figure 3 and Figure 6
as σi, i = E, I, R increases from σi = O(ǫ), i = E, I, R to σi = 0.5, i = E, I, R.
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
are only inﬁnitesimally small random ﬂuctuations in the disease dynamics, that is, when the intensities of the
white noise processes in the system due to random ﬂuctuations in the natural death and disease transmission
processes in all the classes (S, E, I, R) are described as follows: σS = σE = σβ = σI = σR = 0(ǫ).


## Page 74


74
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
are only inﬁnitesimally small random ﬂuctuations in the disease dynamics from the natural death of the
classes (S,E,I,R), that is, when σS = σE = σI = σR = 0(ǫ), but there are random ﬂuctuations in the disease
transmission process with low intensity value of σβ = 0.5.


## Page 75


75
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
there are only inﬁnitesimally small random ﬂuctuations in the disease dynamics from the natural death
of the classes (S,E,I,R), that is, when σS = σE = σI = σR = 0(ǫ), but there are random ﬂuctuations in
the disease transmission process with high intensity value of σβ = 9. In addition, the broken line on the
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
(S, E, I, R), that is, σi = (ǫ), i = S, E, I, R . It can be observed from Figure 3 that when
the intensity value σβ is inﬁnitesimally small, that is, σβ = 0(ǫ), no signiﬁcant oscillations
occur over time on the trajectories for S, E, I, R in (a), (b), (c) and (d) respectively. Further-


## Page 76


76
more, for signiﬁcant but low intensity values4 for σβ, that is, σβ = 0.5, Figure 4 shows that
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
One can also observe from Table 3 and Remark 6.1 that for σi = O(ǫ), i = S, E, I, R, the
average values of S, E, I, R over time on the trajectories in Figures 3-5 decrease continuously
with increase in the intensity value of σβ from σβ = O(ǫ) to σβ = 9. These observations
related to the oscillatory behavior of the system, for example, comparing the trajectory of
S in Figure 3(c), Figure 4(g) and Figure 5(k), and also comparing the trajectory for I in
Figure 3(e), Figure 4(i) and Figure 5(m) suggest that continuously increasing the intensity
value for σβ tends to increase the oscillatory behavior of the trajectories of the system that
results in an average decrease in the size of the susceptible, exposed, infectious and removal
populations over time. Furthermore, the size of the oscillations in the system is proportional
4That is, σβ = O(1).


## Page 77


77
to the size of the intensity values of the white noise process as remarked in the previous
section.
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
Figure 6: (o), (p), (q) and (r) show the trajectories of the disease classes (S, E, I, R) respectively, when there
are signiﬁcant small random ﬂuctuations in the disease dynamics from the natural death process of exposed,
infectious and removal classes, with intensity value σE = σI = σR = 0.5, but there are only inﬁnitesimally
small ﬂuctuations in the disease dynamics due to the disease transmission and natural death processes of
susceptible individuals, that is, σS = σβ = 0(ǫ).
Figure 3 , Figure 6, and Figure 7 can be used as an example to examine the eﬀect
of the intensity of the white noise process, σi, i = S, E, I, R, originating from the random
ﬂuctuations in the natural death process of each class-S, E, I, R, on the trajectories of the
system, in the absence of any signiﬁcant ﬂuctuation in the disease dynamics owing to the
disease transmission process, that is, σβ = O(ǫ). For example, to examine the eﬀect of σβ for
the susceptible class, S, on the trajectories of the stochastic stochastic system, observe that in
Figure 6, when σS = σβ = O(ǫ) and σi = 0.5, i = E, I, R, no signiﬁcant oscillations occur on


## Page 78


78
the trajectories of S in Figure 6(o) and also on Figure 3(c). Furthermore, when σS is increased
to σS = 0.5, Figure 7(s) depicts signiﬁcant sized oscillations on the trajectory of S. Moreover,
the trajectory for S oscillates near the disease free steady state S∗
0 = 9.199999. It can be
further observed using Table 3 and Remark 6.1 that no major diﬀerences have occurred on
the trajectories of the other states E, I, R in both Figure 6(p),(q),(r) and Figure 7(t),(u),(v)
respectively. In addition, it can be seen from Table 3 and Remark 6.1 that when σβ = O(ǫ),
the increase in the intensity value of σS from σS = O(ǫ) to σS = 0.5 on average leads to
a decrease in the susceptible population size over time in Figure 7(s) than it is observed
in Figure 6(o) and Figure 3(c). These observations suggest that in the absence of random
ﬂuctuations in the disease dynamics from the disease transmission process, that is, σβ = O(ǫ),
the intensity of the white noise process, σS, owing to the natural death of the susceptible
class S, (1.) exhibits a signiﬁcant eﬀect primarily on its trajectory, and (2.) the eﬀect of
increasing the intensity value5 of σS leads to an oscillatory behavior on the trajectory of S
that decreases the susceptible population averagely over time. Note that a similar numerical
and graphical diagnostic approach can be used to examine the eﬀects of the other classes
E, I, R, whenever σβ = O(ǫ).
5that is σS = θ( 1
ǫ)


## Page 79


79
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
σS = σE = σI = σR = 0.5, but there are inﬁnitesimally small ﬂuctuations in the disease dynamics from the
disease transmission process, that is, σβ = 0(ǫ). In addition, the broken line on the sample path for S(t)
in (s) depicts the S-coordinate S∗
0 = B
µ = 9.199999 for the disease free steady state E0 = (S∗
0, 0, 0, 0), S∗
0 =
B
µ , E∗
0 = 0, I∗
0 = 0, R∗
0 = 0.


## Page 80


80
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
Figure 8: (w), (x), (y) and (z) show the trajectories of the disease classes (S, E, I, R) respectively, when
there are signiﬁcant and large random ﬂuctuations in the disease dynamics from the natural death process
in all the disease classes- susceptible, exposed, infectious and removal classes with suﬃciently high intensity
value of σS = σE = σI = σR = 9, but there are inﬁnitesimally small ﬂuctuations in the disease dynamics
from the disease transmission process, that is, σβ = 0(ǫ). In addition, the broken line on the sample paths
for S(t), E(t), I(t) and R(t) depict the S, E, I, R-coordinates S∗
0 = B
µ = 9.199999, E∗
0 = 0, I∗
0 = 0, R∗
0 = 0
for the disease free steady state E0 = (S∗
0, 0, 0, 0), S∗
0 = B
µ , E∗
0 = 0, I∗
0 = 0, R∗
0 = 0. (w), (x), (y) and (z) also
show that the population goes extinct over time due to the high intensity of the white noise.
Figure 3, Figure 7 and Figure 8 can be used to examine the eﬀect of increasing the in-
tensity value of the white noise process originating from the natural death, σi, i = S, E, I, R,
in the absence of any signiﬁcant random ﬂuctuations in the disease dynamics from the
disease transmission process, that is, when σβ = O(ǫ). Figure 7 (s),(t),(u),(v) show that
the trajectories for S, E, I, R respectively, oscillate near the disease free equilibrium E0 =
(9.199999, 0, 0, 0) over time when the intensity value is increased from σi = O(ǫ), i =


## Page 81


81
S, E, I, R to σi = 0.5, i = S, E, I, R than is observed in the Figure 3 (c), (d), (e), (f). Fur-
thermore, the oscillations on the trajectories seem to be small in size over time. When the
intensity value, σi, i = S, E, I, R, is further increased to σi = 9, i = S, E, I, R, the oscillations
on the trajectories in Figure 8 (w),(x),(y),(z), appear to have increased in size. Furthermore,
Table 3 and Remark 6.1 show that the oscillations lead to a decrease in the average values
of S, E, I, R over time, and further away from the disease free state of S∗
0 = 9.199999. More-
over, the population rapidly becomes extinct over time. These observations suggest that
the increase6 in the intensity value of the white noise due to natural death in all classes,
σi, i = S, E, I, R, in the population (1.)leads to an increase in the oscillatory behavior of
the system which decreases the population size averagely over time and also (2.)leads to
population extinction over time. Note that this observation is consistent with the results of
Theorem 5.7.
6That is, σi = θ( 1
ǫ), i = S, E, I, R


## Page 82


82
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


## Page 83


83
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
the intensity value is increased from σi = O(ǫ), i = S, E, I, R, β to σi = 0.5, i = S, E, I, R, β


## Page 84


84
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
that for a ﬁxed value of σi = 9, i = S, E, I, R, if σβ increases from σβ = O(ǫ) in Fig-
ure 8(w),(x),(y),(z) to σβ = 9 in Figure 10(e1),(f1),(g1),(h1), then the population more
rapidly becomes extinct than it is observed in Figure 8(w),(x),(y),(z).
Indeed, in Fig-
ure 8(w),(x),(y),(z), the trajectories for the susceptible S, exposed E, infectious I and Re-
moval R states go extinct at approximately the following times t = 2, t = 1.8, t = 2 and
t = 1.8 respectively. Meanwhile, in Figure 10(e1),(f1),(g1),(h1), the trajectories for suscep-
tible S, exposed E, infectious I and Removal R go extinct earlier at the approximate times
t = 1.5, t = 1, t = 1 and t = 1.4 respectively. Note that these observations are consistent
with the results of Theorem 5.7.
The following pairs of ﬁgures:- (Figure 4 (g),(h),(i),(j) & Figure 5 (k),(l),(m),(n)) and (


## Page 85


85
Figure 7 (s),(t),(u),(v) & Figure 8 (w),(x),(y),(z)), can be used with reference to Figure 3, to
examine and compare the two major sources of random ﬂuctuations in the disease dynamics
namely-natural death and disease transmission processes, in order to determine the source
which has stronger eﬀect on the trajectories of the system, whenever the intensity values
of the white noise processes increase in value. In the absence of random ﬂuctuations in
the natural death process, that is, σi = O(ǫ), i = S, E, I, R, as the intensity value of σβ is
increased from σβ = 0.5 to σβ = 9, the pair of ﬁgures (Figure 4 (g),(h),(i),(j) & Figure 5
(k),(l), (m),(n)) show an increase in the oscillatory behavior on the trajectories of the system
which is more signiﬁcant in size for the S and I classes over time. Furthermore, the oscillatory
behavior leads to a decrease in the average susceptible and infectious populations over time
than it is observed in Figure 3 (c) and Figure 3(e) respectively, as shown in Table 3 and
Remark 6.1. Moreover, the general disease population does not go extinct over time.
Meanwhile, in the absence of random ﬂuctuations in the disease transmission process,
that is, σβ = O(ǫ), the increase in the intensity value of σi, i = S, E, I, R from σi =
0.5, i = S, E, I, R to σi = 9, i = S, E, I, R, the pair of ﬁgures ( Figure 7(s),(t),(u),(v) &
Figure 8(w),(x),(y),(z)) show very strong increase in the oscillatory behavior on the trajec-
tories of the system which is signiﬁcant in all the states- S, E, I and R . Furthermore, from
Table 3 and Remark 6.1, it can be seen that the oscillatory behavior of the system leads to
a rapid decrease in the average values of all the states-S, E, I and R over time, with the
mean susceptible population size deviating much further away from the disease free steady
state S∗
0 = 9.199999, than it is observed in Figure 3. Moreover, the disease population goes
extinct over time with the increase in the intensity value of σi, i = S, E, I, R.


## Page 86


86
7. Conclusion
The presented class of stochastic SEIRS epidemic dynamic models with nonlinear in-
cidence rates, three distributed delays and random perturbations characterizes the general
dynamics of vector-borne diseases such as malaria and dengue fever, that are inﬂuenced
by random environmental ﬂuctuations from (1.) the disease transmission process between
susceptible and infectious individuals, and also from (2.) the natural death processes in the
sub-categories - susceptible, exposed, infectious and removal individuals of the population.
Moreover, the random ﬂuctuations in the disease dynamics are incorporated into the epi-
demic dynamic models via white noise or Wiener processes. Furthermore, the three delays
are random variables. Whereas, two of the delays represent the incubation periods of the
infectious agent in the vector and human hosts, the third delay represents the period of
eﬀective naturally acquired immunity against the disease, that is conferred to individuals
after recovery from infection. The class of epidemic dynamic models is represented as a
system of Ito-Doob type stochastic diﬀerential equations with a general nonlinear incidence
function G. The nonlinear incidence function G can be used to characterize the disease
transmission rates for disease scenarios that exhibit a striking initial increase or decrease in
disease transmission rates that becomes steady or bounded when the infectious population
size is large.
The existence of unique global positive solutions is validated for the stochastic dynamic
system by applying the standard method of Lipschitz continuity, stopping times and en-
ergy functions. Moreover, a positive self-invariant set for the stochastic dynamic system is
presented. Detailed results for the asymptotic behavior of the stochastic dynamic system
are presented namely:- (1.) the existence and asymptotic stochastic stability of a feasible
disease-free equilibrium of the stochastic system, and (2.) the asymptotic oscillatory char-


## Page 87


87
acter of the solutions of the stochastic system near a potential disease-free equilibrium. The
threshold values for the stochastic stability of the disease free steady state, and for disease
eradication, such as the basic reproduction number for the disease dynamics are computed.
The analytic asymptotic results for the epidemic dynamic system suggest that the source
(disease transmission or natural death rates ) and size of the intensity values of the white
noise processes in the system exhibit direct consequences on the overall asymptotic behavior
of the epidemic dynamic model with respect to the feasible or potential disease free popula-
tion steady state for the epidemic dynamic model, and consequently on disease eradication.
This observation leads to further thorough examination of the asymptotic properties of the
stochastic epidemic dynamic system under various intensity levels of the white noise pro-
cesses in the system. In addition, two numerical simulation examples are presented to justify
the results from the analysis.


## Page 88


88
8. References
References
[1] E. Avila, V. Buonomo, Analysis of a mosquito-borne disease transmission model with
vector stages and nonlinear forces of infection, Ricerche di Matematica Volume 64,
Issue 2,(2005) pp 377390
[2] Z. Bai, Y. Zhou, Global dynamics of an SEIRS epidemic model with periodic vaccina-
tion and seasonal contact rate, Nonlinear Analysis: Real World Applications Volume
13, Issue 3, ( 2012) Pages 10601068
[3] E. Beretta, V. Kolmanovskii, L. Shaikhet, Stability of epidemic model with time delay
inﬂuenced by stochastic perturbations, Mathematics and Computers in Simulation 45
(1998) 269-277
[4] V. Capasso, Mathematical Structures of Epidemic Systems, Lecture Notes in Biomath-
ematics,Volume 97 (1993)
[5] V. Capasso, G.A. Serio, A generalization of the Kermack-Mckendrick deterministic
epidemic model. Math Biosc (1978) 42:43
[6] K. L.Cooke Stability analysis for a vector disease model. Rocky Mountain Journal of
Mathematics no. 1, 9(1979), 31-42
[7] k. L. Cooke, p. van den Driessche, Analysis of an SEIRS epidemic model with two
delays, J Math Biol.;35(2) (1996)240-60.
[8] M. De la Sena, S. Alonso-Quesadaa, A. Ibeasb, On the stability of an SEIR epidemic


## Page 89


89
model with distributed time-delay and a general class of feedback vaccination rules,
Applied Mathematics and Computation Volume 270, 1 (2015), Pages 953976
[9] M. De la Sen, S. Alonso-Quesada, A. Ibeas, On the stability of an SEIR epidemic
model with distributed time-delay and a general class of feedback vaccination rules,
Applied Mathematics and Computation Volume 270, 1 ( 2015), Pages 953976
[10] N. H. Du, N. N. Nhu, Permanence and extinction of certain stochastic SIR models
perturbed by a complex type of noises, Applied Mathematics Letters 64 (2017)
[11] D. L. Doolan, C. Dobano, J. K. Baird, Acquired Immunity to Malaria, clinical micro-
biology reviews, Vol. 22, No. 1, ( 2009), p. 1336
[12] S. Gao, Z. Teng, D. Xie, The eﬀects of pulse vaccination on SEIR model with two
time delays, Applied Mathematics and Computation Volume 201, Issues 12, 15 (2008),
Pages 282292
[13] H. Hai-Feng, M. Zhan-Ping, Dynamics of a delayed epidemic model with non-
monotonic incidence rate,Communications in Nonlinear Science and Numerical Simu-
lation, Volume 15, Issue 2,(2010) p. 459-468.
[14] L. Hviid, Naturally acquired immunity to Plasmodium falciparum malaria, Acta Trop-
ica 95(3):( 2005)270-5
[15] Z. Jianga, b, W. Mab, J. Wei, Global Hopf bifurcation and permanence of a de-
layed SEIRS epidemic model, Mathematics and Computers in Simulation Volume 122,
(2016), Pages 3554
[16] A. Korobeinikov, P.K. Maini, A Lyapunov function and global properties for SIR and


## Page 90


90
SEIR epidemiological models with nonlinear incidence, Math. Biosci. Eng. 1 (1) (2004)
5760.
[17] Y. N. Kyrychko, K. B. Blyussb, Global properties of a delayed SIR model with tem-
porary immunity and nonlinear incidence rate, Nonlinear Analysis: Real World Appli-
cations Volume 6, Issue 3, (2005), Pages 495-507
[18] G.S. Ladde, V. Lakshmikantham, Random Diﬀerential Inequalities, Academic press,
New York, 1980
[19] G.S. Ladde, Cellular Systems-II. Stability of Campartmental Systems. Math. Biosci.
30(1976), 1-21
[20] W.M. Liu, H.W. Hethcote , S.A.Levin, Dynamical behavior of epidemiological models
with nonlinear incidence rates, J.Math Biol (1987); 25:359
[21] Q. Liu, D. Jiang, N. Shi, T. Hayat, A. Alsaedi, Asymptotic behaviors of a stochastic
delayed SIR epidemic model with nonlinear incidence, Communications in Nonlinear
Science and Numerical Simulation Volume 40, (2016), Pages 89-99.
[22] Q. Liu, Q. Chen Analysis of the deterministic and stochastic SIRS epidemic models
with nonlinear incidence Physica A, 428 (2015), pp. 140153
[23] W.M. Liu, H.W. Hethcote, S.A. Levin, Dynamical behavior of epidemiological models
with nonlinear incidence rates, J. Math. Biol. 25 (4) (1987) 359380
[24] X. Mao, Stochastic diﬀerential equations and applications Horwood Publishing Ltd.,
2nd ed., (2008)


## Page 91


91
[25] J. P. Mateusa, C. M. Silvab, Existence of periodic solutions of a periodic SEIRS
model with general incidence, Nonlinear Analysis: Real World Applications Volume
34, (2017), Pages 379402
[26] J. P. Mateus, C. M. Silva, A non-autonomous SEIRS model with general incidence
rate , Applied Mathematics and Computation Volume 247, 15 (2014), Pages 169189
[27] S.M. Moghadas, A.B. Gumel, Global Statbility of a two-stage epidemic model with
generalized nonlinear incidence, Mathematics and computers in simulation 60 (2002),
107-118
[28] Y. Muroya , Y. Enatsu, Y. Nakata, Global stability of a delayed SIRS epidemic model
with a non-monotonic incidence rate, Journal of Mathematical Analysis and Applica-
tions Volume 377, Issue 1, (2011), Pages 114
[29] L. Pang, S. Ruan, S. Liu , Z. Zhao , X. Zhang, Transmission dynamics and opti-
mal control of measles epidemics, Applied Mathematics and Computation 256 (2015)
131147
[30] B. G. Sampath Aruna Pradeep , W. Ma, Global Stability Analysis for Vector Transmis-
sion Disease Dynamic Model with Non-linear Incidence and Two Time Delays, Journal
of Interdisciplinary Mathematics, Volume 18, Issue 4 (2015)Pages 395-415
[31] S. Syafruddin, M. Salmi, M.D. Noorani, Lyapunov function of SIR and SEIR model for
transmission of dengue fever disease, International Journal of Simulation and Process
Modelling (IJSPM), Vol. 8, No. 2-3, (2013) pp.177184.
[32] D. Wanduku, G. Ladde, A two-scale network dynamic model for human mobility pro-
cess, Math. Biosciences, vol. 229 (1)(2011),Pages 1-15


## Page 92


92
[33] D. Wanduku,
Threshold conditions for a family of epidemic dynamic models
for malaria with distributed delays in a non-random environment, International
Journal of Biomathematics Vol. 11,
No. 6 (2018) 1850085 (46 pages),
DOI:
10.1142/S1793524518500857
[34] D. Wanduku, A comparative stochastic and deterministic study of a class of epidemic
dynamic models for malaria: exploring the impacts of noise on eradication and persis-
tence of disease, in press, (2017)
[35] D. Wanduku, The stochastic permanence of malaria, and the existence of a stationary
distribution for a class of malaria models, in press, (2018)
[36] D. Wanduku, Complete Global Analysis of a Two-Scale Network SIRS Epidemic Dy-
namic Model with Distributed Delay and Random Perturbation, Applied Mathematics
and Computation Vol. 294 (2017) p. 49 - 76
[37] D. Wanduku, G.S. Ladde, Global properties of a two-scale network stochastic de-
layed human epidemic dynamic model, nonlinear Analysis: Real World Applications
13(2012)794-816
[38] D. Wanduku, G.S. Ladde, The global analysis of a stochastic two-scale Network Hu-
man Epidemic Dynamic Model With Varying Immunity Period, Journal of Applied
Mathematics and Physics, 5, (2017) 1150-1173
[39] D. Wanduku and G.S. Ladde Global Stability of Two-Scale Network Human Epidemic
Dynamic Model, Neural, Parallel, and Scientiﬁc Computations 19 (2011) 65-90
[40] D. Wanduku, G.S. Ladde , Fundamental Properties of a Two-scale Network stochas-


## Page 93


93
tic human epidemic Dynamic model, Neural, Parallel, and Scientiﬁc Computations
19(2011) 229-270
[41] D. Xiao, S. Ruan, Global analysis of an epidemic model with nonmonotone incidence
rate. Math Biosci.208(2) (2007):419-29
[42] Y. Xue, X. Duan, Dynamic Analysis Of An Sir Epidemic Model With Nonlinear In-
cidence Rate And Double Delays, International Journal Of Information And Systems
Sciences, Volume 7, Number 1,(2011) Pages 92102
[43] Y. Takeuchi, W. Ma and E. Beretta, Global asymptotic properties of a delay SIR
epidemic model with ﬁnite incubation times, Nonlinear Anal. 42 (2000), 931-947.
[44] Y. Zhou, W. Zhang, S. Yuan, H. Hu, Persistence And Extinction In Stochastic Sirs
Models With General Nonlinear Incidence Rate, Electronic Journal of Diﬀerential
Equations, Vol. 2014, No. 42,(2014) pp. 117.
[45] L. Zhu, H. Hu, A stochastic SIR epidemic model with density dependent birth rate,
Advances in Diﬀerence Equations (2015), 2015:330
[46] http://www.who.int/denguecontrol/human/en/
[47] https://www.cdc.gov/malaria/about/disease.html


## Page 94


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


## Page 95


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
node_id: 1808_09842v1_analyzing_the_qualitative_properties_of_white_noise_on_a_family_of_infectious_di
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1808_09842V1_ANALYZING_THE_QUALITATIVE_PROPERTIES_OF_WHITE_NOISE_ON_A_FAMILY_OF_INFECTIOUS_DI.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

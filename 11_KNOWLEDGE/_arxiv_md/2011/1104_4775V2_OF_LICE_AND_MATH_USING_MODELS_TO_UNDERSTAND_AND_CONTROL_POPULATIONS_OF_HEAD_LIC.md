---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1104.4775v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1104.4775v2_Of_lice_and_math__using_models_to_understand_and_control_populations_of_head_lic

> Source: 1104.4775v2_Of_lice_and_math__using_models_to_understand_and_control_populations_of_head_lic.pdf

> Pages: 36

---


## Page 1


arXiv:1104.4775v2  [q-bio.PE]  28 Apr 2011
1
Of lice and math: using models to understand and control
populations of head lice
Mar´ıa Fabiana Laguna1, Sebasti´an Risau-Gusman2,∗,
1 Consejo Nacional de Investigaciones Cient´ıﬁcas y T´ecnicas, Argentina, Centro At´omico
Bariloche, 8400 S. C. de Bariloche, Argentina
2 Consejo Nacional de Investigaciones Cient´ıﬁcas y T´ecnicas, Argentina, Centro At´omico
Bariloche, 8400 S. C. de Bariloche, Argentina
∗E-mail: Corresponding srisau@cab.cnea.gov.ar
Abstract
In this paper we use detailed data about the biology of the head louse (pediculus humanus capitis) to
build a model of the evolution of head lice colonies. Using theory and computer simulations, we show
that the model can be used to assess the impact of the various strategies usually applied to eradicate head
lice, both conscious (treatments) and unconscious (grooming). In the case of treatments, we study the
diﬀerence in performance that arises when they are applied in systematic and non-systematic ways. Using
some reasonable simplifying assumptions (as random mixing of human groups and the same mobility for
all life stages of head lice other than eggs) we model the contagion of pediculosis using only one additional
parameter. It is shown that this parameter can be tuned to obtain collective infestations whose variables
are compatible with what is given in the literature on real infestations. We analyze two scenarios: one
where group members begin treatment when a similar number of lice are present in each head, and another
where there is one individual who starts treatment with a much larger threshold (‘superspreader’). For
both cases we assess the impact of several collective strategies of treatment.
Author Summary
Head lice are ectoparasites that can only live on human heads, and their presence in human groups is
documented since antiquity. Infestations of head lice aﬀect primarily children, at all levels of society and
most ethnic groups. Its prevalence is so high that it is an important concern for public health oﬃces
worldwide. Thus, given the long history of pediculosis and the widespread application of mathematical
epidemiology to the study of various diseases, it is surprising to ﬁnd that the study of pediculosis has
long been neglected. In fact, most predictions about it are usually based on little more than educated
guesses. We developed a mathematical model of populations of head lice based in the few detailed data
available. It allows us to propose some answers for biologically relevant questions as, for example, what
is the mechanism responsible for the low levels of infestations in spite of the large number of eggs laid by
female lice. We also analyze the performance of some control measures that can be adopted to eradicate
head lice. Finally, we include in our model the interaction between populations to study the transmission
of lice from head to head and the eﬀect of collective control measures.
Introduction
Of the thousands of species of blood sucking ectoparasites known as lice, only three of them infest human
populations: Phtirus pubis (pubic lice), Pediculus humanus humanus (body lice), and Pediculus humanus
capitis (head lice). Pubic lice are not considered a serious threat for public health because they are not
known to be vectors of any diseases, and because their prevalence (deﬁned as the proportion of infested
people in a given population) is relatively low (≈2%) [1]. As they are mainly transmitted through sexual
contact, they are often used as predictors for the presence of sexually transmitted diseases. Body lice, on
the other hand, are vectors of several serious diseases such as trench fever and typhus. As infestations


## Page 2


2
with body lice are most frequent in conditions of heavy crowding and poor hygiene, they have been
responsible for outbreaks of typhus in times of war and in refugees camps [2]. After the 2nd World War,
however, they have ceased to be a major public health concern.
Even though they are not known to transmit any diseases, for centuries now head lice have been a
constant source of worries both for parents of infested children as for public health oﬃcials. After the
2nd World War the use of the insecticide DDT led to a temporary decrease in the prevalence of human
louse, and consequently the scientiﬁc community seemed to lose interest in the study in the biology of
this parasite [3]. Resistance to insecticides and other factors, however, led to a new increase in head lice
prevalence. As a result, there is a gap of almost 50 years in the few studies of the biology of the human
louse. An example of this is the taxonomic status of head and body lice, which still remains unclear, in
spite of several very recent studies (see, e.g., [4,5]).
In the 21st century the prevalence of head lice is still very high worldwide [6]: it is not uncommon to
ﬁnd more than 20 % of children infected in some schools. As a consequence, a large amount of resources
is dedicated each year by governments around the world to develop new products and to design strategies
for the control and prevention of the spread of head lice. To assess the impact of these measures and
to be able of making meaningful predictions, one needs either detailed experiments on human subjects
or a detailed knowledge of the fundamental biology of the louse. The obvious practical and moral issues
of experimenting in humans have turned research to in vitro experiments, but the extrapolation of the
corresponding results is far from straightforward. On the other hand, for theoretical predictions, the
problem of scarcity of detailed data about the fundamental biology of the louse is compounded by the
fact that in general only a small subset of these data is used, and only for qualitative reasonings.
Head lice are ectoparasites that can only live on human heads. They go through three life stages:
egg, nymph and adult. The eggs, usually called nits, are glued to the hair shafts, making its removal
very diﬃcult. After leaving the egg, the nymph moults three times before turning adult. Both adults
and nymphs feed on the blood of the host between 3 and 10 times a day [7], and can only survive a few
hours without a blood meal [8]. Transmission of lice occurs mainly from head to head [9], and it has been
argued that fomites may also play some role [10], but there is some controversy about this [11].
Infestations of head lice aﬀect primarily children between 3 and 11 year old, at all levels of society and
most ethnic groups [2]. Symptoms of prolonged infestations can include intense pruritus and sleeplessness
[2] and even lead to social stigmatization [12]. As mentioned before, the prevalence is so high that it
continues to be an important concern for public health oﬃces worldwide. In fact, the economical burden
of treating head lice infestations has been estimated at 1 billion [13]. This shows that many treatment
strategies and pharmacological therapies have been proposed to control and eliminate populations of head
lice. The assessment of such measures, however, is only very loosely based on biological data about the
louse. And, even when the few hard data available is used, the studies analyze only simple worst- and
average-case scenarios [14].
Mathematical models provide a framework into which available data can be integrated to obtain mean-
ingful predictions about the system which is being studied. In particular, models of animal populations
have a long history [15,16]. There are even some mathematical models of populations of some ectopara-
sites such as ticks [17], ﬂeas [18] and sea lice [19]. Here we propose a model of populations of head lice
which is based in the few detailed data available. Using both theory and computer simulations, we are
able to suggest some answers for biologically relevant questions as, for example, what is the mechanism
responsible for the low levels of infestations in human heads (typically ≈10 adult lice [2]) in spite of the
large number of eggs laid by female lice through their adult lives. We also analyze the performance of
some of the many possible control measures that can be adopted to control, or even eradicate, head lice.
The model is extended to include also the possibility of interaction between populations to model the
transmission of lice from head to head. In this framework, we are also able to analyze the eﬀect of the
possible collective control measures.


## Page 3


3
Materials and Methods
To build our model of head lice we use a mixed Leslie-Lefkovitch matrix approach. The Leslie matrix
approach [20, 21] implies characterizing the population by the age of the individuals, whereas with the
Lefkovitch matrix [22] age is disregarded in favour of life stages. In our case, we use both life stages
and the age of the individual inside every life stage. We consider ﬁve life stages: egg, nymph before
the ﬁrst, second and third moults, and adult. The maximal durations of each stage are, respectively,
ne, n1, n2, n3, and na, measured in days. Therefore, the vector that characterizes the population has
ne + n1 + n2 + n3 + na components. The ﬁrst component corresponds to the total number of eggs laid
in one day, the second corresponds to the total number of one day old eggs, etc. Component ne + 1
corresponds to the number of nymphs that just hatched, component ne + 2 to one day old nymphs, and
so on. In principle, transitions can occur from any day in any stage, to the ﬁrst day in the following
stage.
We have built two matrices, corresponding to two diﬀerent sets of data. Unfortunately, the detailed
data necessary to build the matrix is available only for body lice [23]. In that work, Evans and Smith
(hereafter ES) have measured the length of the ﬁve stages, as well as the fecundity for a large number of
individuals, and these measurements are one of our sets of data. Recently, Takano-Lee and co workers
(hereafter TL) have succeeded in rearing head lice both in vivo and in vitro and have obtained reasonable
accurate values for many biological parameters [8]. But they only provide mean values and dispersion
for the mortality in the adult stage, which does not allow for a reconstruction of the full survival curve.
To obtain the required detailed data, we note ﬁrst that the adult survivorship data of Evans and Smith
can be very well ﬁtted by a Weibull distribution [24] (as happens with other insects). Therefore we have
also proposed a Weibull distribution for head lice that is compatible with the data of [8]. Table 1 shows
the values we have used for the most important vital parameters (for the rest of them, see Appendix A).
Table 1. Summary of the average vital parameters of Pediculus humanus capitis. In the ﬁrst ﬁve
columns the duration of each stage is given in days. The last column indicates the average number of
eggs. For each model (TL and ES) the ﬁrst line gives the average value and the second the minimal and
maximal values. The standard error of the last ﬁgure of each average is given between parenthesis.
hatching
1st moult
2nd moult
3rd moult
adulthood
eggs
TL [8]
8.4(1)
3.0(0)
5.2(1)
8.0(0)
20.2(1.4)
4.9(2)
7 −11
3 −4
5 −7
8 −9
12 −31
1 −6
ES [23]
8.02(1)
5.23(4)
8.63(3)
12.81(4)
17.58(46)
4.9(2)
5 −12
4 −7
8 −10
12 −14
1 −46
3 −10
Given an initial population vector P0, the population at day n is given by Pn = M nP0, where M is
the Leslie-Lefkovich matrix obtained using TL or ES data. The long time behaviour of the population is
given by λ1, the largest eigenvalue of M: if λ1 > 1 there is exponential growth whereas if λ1 < 1 there is
extinction, regardless of the initial condition. But note that components of Pn give average values for the
number of insects at each stage of development. In a given population the vital parameters of each insect
are stochastic parameters, whose average values are given by the matrix M. Thus, in a ﬁnite population
there is the possibility of stochastic extinctions even if λ1 > 1. Evidently stochastic extinctions become
exponentially less probable as λ1 is made larger. Another important diﬀerence for ﬁnite populations is
that they can become extinct in ﬁnite time whereas in the matrix population approach this extinction
time is inﬁnite, because non-zero components pn remain greater than 0 at all times.
To go beyond average values, which are the only quantities that can be calculated with the matrix
approach, we have resorted to agent-based simulations. They consist of populations of ‘agents’ (i.e. head
lice) which evolve stochastically through the diﬀerent life stages according to their vital parameters. Each
vital parameter of each agent is drawn from an exponential distribution with the same average as that


## Page 4


4
given by the corresponding component of the evolution matrix. The algorithm is explained in detail in
Appendix A. Both in our simulations and in the matrix population formalism we have assumed that
lice do not interact. That is, the vital parameters of each agent do not depend on the total number of
individuals. As blood is readily available for head lice, it is reasonable to assume that lice do not compete
for the resources, if populations are not very large.
The results we obtained with both, TL and ES data sets, have only small diﬀerences. Consequently,
in the following sections the description of results applies to both group of data unless otherwise stated.
Moreover, to avoid an unnecessary duplication of ﬁgures, we only show the ones corresponding to TL
data. The ﬁgures drawn using ES data are given in Appendix B.
Results
Single population dynamics
For the two sets of parameters used, the intrinsic growth rate [25], i.e. the largest eigenvalue of the
corresponding evolution matrix, is: λ1 = 1.12 for the ES model and λ1 = 1.133 for the TL model. Fig.
B1 shows the average evolution of a population initiated by a 10-day old single female (i.e. a female which
has undergone her last moult 10 days ago). The time-dependence of the population is calculated using
evolution matrices and by means of numerical simulations. In the case of the simulations, we plot the
average values obtained from 1000 realizations which start with the same initial condition (one 10-day
old female). The ﬁgure shows that there is a very good agreement between theory and the average of
simulations, which conﬁrms that the algorithm is a stochastic version of the model. We also studied
the evolution of colonies starting with diﬀerent initial conditions, and found no substantial diﬀerences
with the case shown in Fig. B1. In all our calculations we have assumed that the ﬁrst female does not
need to be fertilized by a male: it has been reported that females can lay eggs during several days after
being fertilized [26], and it has even been suggested that a single mating could be enough to achieve
lifetime fertility [27]. The ﬁgure shows that after the ﬁrst month the number of adults grows rapidly
from hundreds to thousands of individuals. In real populations living in human heads, however, it is
well known that the average number of live lice is typically about 10 [2] (although there are records of
individuals with hundreds of adult lice [28,29]).
The strategies by which hosts control their populations of ectoparasites can be divided into three
classes [30]: physically avoiding the parasite, exterminating it, and minimizing the harm done by it. This
last line of defence is in fact an indirect means to control the population of the ectoparasite: for example,
immune response could decrease the amount of blood sucked, or make it less beneﬁcial, thereby reducing
the lifespan or the reproductive success of the parasite. We consider here two of the possible mechanisms
that have been suggested as responsible for the small sizes of the lice populations in human heads. One is
the triggering of some modiﬁcation of the hosts blood [2], which would in turn lead to a reduced fertility
of female lice.
With our model it is possible to estimate how much certain vital parameters should change to achieve
an eﬀective control of population growth. Mathematically, the critical value for a given parameter is
deﬁned as the value for which the evolution matrix has λ1 = 1.
In other words, the critical value
separates the parameter region for which the population increases exponentially (λ > 1) from the region
of parameters for which it becomes extinct (λ < 1). We have found that the critical value for the number
of daily eggs laid by each female is approximately 1 egg per week (both for TL and ES data), which is
much less than the ’natural’ value (see Table 1). Furthermore, Fig. A14 shows that, when considered
as a function of the daily number of eggs, λ1 grows rapidly in the vicinity of the critical value. Thus,
even a small increase on the critical number of daily eggs produces a signiﬁcant intrinsic growth of the
population. Studies carried out with lice fed on rabbit blood [31,32] have shown that, even when rabbits
are speciﬁcally immunized (which should have a stronger eﬀect than an spontaneously triggered immune


## Page 5


5
0
25
50
75
100
10
-1
10
1
10
3
10
5
10
0
10
1
10
2
10
3
0
20
40
number of lice
 mobiles (adults + nymphs)
 adults
 nymphs
 eggs
 
 
time (days)
 
 
 
Figure 1. Average number of lice of a colony that is started at day 0 by a female that had her last
moult 10 days before. Symbols represent averages taken over 1000 populations whereas full lines
represent the theoretical predictions. The inset shows the ﬁrst days of one of these populations. Here,
as in the rest of the ﬁgures, the error bars represent the standard error of the mean. Data whose error
bars are not shown have standard errors lower than symbol size.
response), the eﬀect on female lice is to diminish the number of eggs laid to 1 or 2 per day, which is far
from the critical value. This suggests that it is unlikely that the control of the lice population is done
through a lowering of the reproductive success of female lice.
Another possible explanation for the usually low number of lice observed is self-grooming of the
host [33], which includes such activities as combing, scratching, washing, and any other action that might
disturb the natural habitat of lice. Note that, in principle, these are activities that are not consciously
aimed at the eradication of lice (conscious strategies for eradication lice will be treated in the next
subsection). We assume that, each day, grooming eliminates a certain average fraction of all mobile lice
(which are deﬁned as the sum of nymphs and adults). It is also assumed that grooming does not remove
any eggs because they are strongly attached to hair shafts by their glue [34]. We ﬁnd that the critical
percentages of mobile lice that must be removed each day to guarantee eventual extinction of the colony
are 17% and 15% for TL and ES data respectively. These values seem at ﬁrst sight to be rather low:
extinction of the population is guaranteed if, on average, 1 out of 6 lice is removed (or killed) every day.
One could suspect that, at such low levels of grooming, extinction only happens after a very long time.
Figure 3 shows that this is not the case because extinction times drop sharply for grooming eﬃciencies
larger than the critical. Furthermore, even when grooming is not eﬀective enough to cause an extinction
of the population, it can slow down its evolution, as the inset in Fig. B3 shows. As an example, note
that when the eﬃciency of grooming is ≈10% it takes an additional week for the population to have 15
mobile lice, respect to the no grooming case.
These results suggest that it is more probable that an eﬀective control of the population is achieved
by killing or removing lice (i.e., by grooming) than by reducing the reproductive success of female lice


## Page 6


6
0
1
2
3
4
5
0.90
0.95
1.00
1.05
1.10
1.15
 
1
average daily eggs
 TL data
 ES data
Figure 2. Intrinsic growth rate for a lice population as a function of the average of daily eggs laid by a
single female. The rest of the parameters that deﬁne the population are taken from [8] (Takano-Lee
curve) and [23](Evans/Smith curve). The vertical line shows the position of the critical value.
(which could happens through some modiﬁcation of the host blood).
Evaluating control measures
In the long history of lice infestations in humans many elimination strategies and remedies have been
used. This has generated a ﬂood of tests which try to assess the eﬃcacy of the diﬀerent strategies and
chemical products, which in turn has generated a large number of review articles which compare the
results of diﬀerent tests [35]. In most cases the trials consist on the application of a given treatment
to a batch of infected people (mostly children) and then the fraction of ‘cured’ people is recorded. One
problem is that there seems to be no agreement on the very deﬁnition of ‘infestation’, at least on the
practical side. Infestations can be deﬁned as the presence of live lice, or lice and eggs. This is compounded
by the fact that there is no infallible method to detect head lice and/or eggs.
For trials of chemical products, a diﬀerent approach consists of applying the substance to a population
of lice placed in an artiﬁcial environment, and then recording the fraction of dead insects [36]. In this
case, however, it is not clear how to link that number with an assessment of the recommended treatment
to eliminate lice, or how to propose an eﬀective treatment. A detailed mathematical model can provide
such a link.
In the rest of this paper we use a deﬁnition of a treatment as a strategy to eradicate head lice,
consisting in a series of applications. An application is deﬁned simply as something that is done at some
deﬁnite time to kill as many head lice as possible. Its eﬃcacy is deﬁned by the percentage of lice that are


## Page 7


7
0
20
40
60
80
100
0.00
0.25
0.50
0.75
1.00
0
20
40
60
80
0
10
20
10
20
30
40
duration of the infestation (days)
fraction of extinctions
 
 
 
ef f icacy of  grooming (%)
 
efficacy of grooming (%)
days required to have 15 lice
 
 
 
Figure 3. Fraction of extinctions (squares), and average duration of the infestation for the extinct
populations (circles), as a function of the eﬃciency of grooming. Averages were taken over 1000
realizations, with a limit time of 500 simulation days (i.e. we only count extinctions happening within
the ﬁrst 500 days). The critical grooming eﬃcacy is deﬁned as the value at which the fraction of
extinctions reach the unity. In this plot, this happens for eﬃcacies closer to 17%. Inset: Number of days
required to reach a population of 15 lice as a function of the eﬃcacy of grooming.
eﬀectively eliminated. In principle, one could assume that the eﬀect of the application is diﬀerent for each
life stage of the insects, or even that it depends on their age. This is represented by a diagonal matrix,
T , of the same dimensions as the evolution matrix M, whose non-zero components give the fraction of
insects of each age that survive the treatment. But most experimental studies of topical treatments only
assess their eﬀect on adult lice (pediculicidity) and on eggs (ovicidity) [37]. For this reason we have only
considered matrices T whose elements for the egg stage are all equal to the proposed ovicidal activity of
the treatment, whereas the rest of the elements are all equal to the pediculicidity. In other words, we
assume that each treatment is deﬁned by only two numbers, the pediculicidity and the ovicidity, as is
done in most clinical trials. We have also included a detection threshold for the start of the treatment.
It is deﬁned as the number of mobile lice necessary for a parent to notice that his/her child has an
infestation, or to cause an itching feeling. In all the ﬁgures of this subsection this threshold is set to 15
mobile lice. In Ref. [2] it is stated that it usually takes several weeks for an individual to start itching
the ﬁrst time he or she has lice. Then, the threshold we choose is the number of mobile lice present in a
head 3 weeks after the start of the infestation, if we consider a grooming eﬃcacy of 5% (see the inset of
Fig. B3). This grooming eﬃcacy is kept constant in the rest of the simulations shown in this paper.
To specify a treatment one needs not only the frequency of the applications but also a criterion for
stopping them. In this regard we classify treatments as systematic and non systematic. For the former


## Page 8


8
it is assumed that the treatment is applied regardless of the state of the lice colony. In other words, it
is applied at least until the whole colony has been eliminated. This would correspond to strictly follow
the suggested treatment, in terms of number and frequency of applications, without using a personal
criterion for deciding whether the colony has already been exterminated. Non systematic treatments are
deﬁned as those where the stopping of the treatment depends on the state of the colony. This models
the situation of parents using their own discretion to decide when the infestation is over. In particular,
we consider that systematic treatments depend only on one parameter, ∆ta, which is the time elapsed
between two successive applications. Moreover, non systematic treatments depend not only on ∆ta but
also on the parameter λend, deﬁned as the threshold to stop the treatment: if the number of mobile lice
is smaller or equal than λend the treatment ceases to be applied. This is intended to model the fact that
it is very diﬃcult to detect every mobile lice in a given head, and thus if the number of mobile lice is
suﬃciently small, they will not be detected, the head would be assumed to be clean of lice, and therefore
the treatment will be stopped. For all treatments, we deﬁne the duration of the treatment as the time
elapsed between the ﬁrst application and the extinction of the colony.
Simulations show that, for all treatments, there is a critical value of the application eﬃcacy: below it,
the probability that the treatment succeeds in exterminating the lice colony is practically 0 whereas above
it it is practically 1 (see Fig.B4 (A)). Interestingly, comparing both panels of Fig. B4, we observe that
even though larger values of λend give longer infestations, the critical application eﬃcacy does not change
with λend. To calculate this critical value for systematic treatments that are applied daily, the equation
λ1 = 1 must be solved, where λ1 is the largest eigenvalue of the matrix M · T . If the treatment is applied
once every n days the procedure is the same, but replacing M · T by M n · T . Results are presented
in Table A6, where the pediculicidity necessary to guarantee the extinctions is given as a function of
ovicidity and frequency of the treatment. Ovicidal eﬃcacy however, is diﬃcult to measure both in vivo
and in vitro [38], and therefore the available estimates are not very reliable. Moreover it is generally
agreed that the ovicidal eﬃcacy of most products is rather low. For this reason, in Table 2 we have only
included a few values of ovicidity and in the rest of the paper we have arbitrarily ﬁxed this number at a
value of 10%.
Table 2. Daily fraction of mobile lice that should be eliminated to cause an extinction for treatments
that are applied once every n days (rows). Columns indicate the ovicidity o, i.e., the fraction of killed
eggs. The last column gives the critical fraction of eggs (feggs) that have to be eliminated to guarantee
the extinction of the population, when no action is taken against mobile lice. All fractions are given for
both TL and ES data.
❍❍❍❍❍
n
o
0
0.1
0.3
0.5
feggs
TL
ES
TL
ES
TL
ES
TL
ES
TL
ES
1d
0.174
0.146
0.126
0.11
0.022
003
0
0
0.34
0.367
2d
0.318
0.271
0.277
0.24
0.18
0.164
0.054
0.07
0.57
0.6
3d
0.439
0.379
0.404
0.351
0.319
0.284
0.204
0.194
0.728
0.76
4d
0.539
0.471
0.509
0.447
0.436
0.388
0.335
0.307
0.832
0.865
7d
0.757
0.68
0.737
0.663
0.688
0.622
0.621
0.566
0.957
0.989
10d
0.873
0.808
0.862
0.798
0.834
0.771
0.792
0.732
1
1
Table A6 shows that the number of lice that have to be eliminated at each application of the treatment
is relatively low, provided that the treatment is systematic. For example, if the treatment is applied every
2 days, eliminating one out every 3 insects guarantees the eventual extinction of the population. But two
questions arise. The ﬁrst is: after how many days since the treatment is begun will the population really
disappear? This is partially answered in Fig. B4(B), where we show the average durations for diﬀerent


## Page 9


9
treatments. As mentioned before, in the upper panel of this ﬁgure we also plot the probability of lice
colony extinction as a function of the eﬃcacy of the pediculicidal, for an ovicidity of 10%. Two systematic
treatments are shown, one corresponding to daily applications (∆ta = 1) and the other which is applied
every 4 days (∆ta = 4). We also plot the results obtained for three non systematic treatments, which
diﬀer in the value of λend. We observe that the critical eﬃcacy - deﬁned as the value of eﬃcacy above
which the probability of elimination of the colony is near to one - strongly depends on the parameter ∆ta,
but it is almost independent of λend. Moreover, note that a treatment which is applied systematically
every 4 days (squared symbols) would take more than 30 days (25 for ES data) to achieve total extinction
of the population if it eliminates 60% of the mobile lice each time. But if the same treatment is used with
a perfect pediculicidal (i.e., ∆ta = 4 and 100% of eﬃcacy) it would take only 10 days, on average, which
is equivalent to 3 applications of the treatment. We are assuming here that the treatment is perfectly
systematic, that is, that it is applied with a given ﬁxed frequency and for a period of time that assures
the extinction of the population. We are aware that this is a very unrealistic assumption, because it
implies that one can detect every live lice and every egg, which is well known to be far from true [39].
Seen from another angle, a systematic treatment assumes that parents will continue applying it even if
no lice are detected, which is also unrealistic. This leads to the second question: What changes if we
relax the assumption of systematicity?
Turning now to non systematic treatments, we assume that the threshold λend refers exclusively to
mobile lice, because eggs are not only diﬃcult to detect, but it is usually not easy to distinguish between
live and dead eggs. The eﬀect of using diﬀerent threshold values and several application frequencies
are shown in Figs. B4,
B5 and
B6, which present the results of 1000 simulations of the model. In
Figs. B4(B),
B5(A) and
B6(A) we plot the average duration of the treatments. It is interesting to
compare these times for systematic and non systematic treatments: from Fig. B4(B) we see that if the
applications have a reasonable eﬃcacy (i.e. when the daily fraction of killed lice is larger than ≈80%),
applying the treatment every day as long as there is at least one mobile lice (∆ta = 1, λend = 1) is less
eﬀective than applying it systematically every 4 days (∆ta = 4).
It is well known that almost all anti-lice treatments are a nuisance because chemical products can be
very aggressive and have side eﬀects, and combing can be tiresome and stressing, both for the patient as
for the comber, resulting in a loss of eﬃcacy. Thus, a relevant quantity is the number of times that the
treatment is applied in each strategy. This information is plotted in Figs. B5(B) and B6(B). Fig. B5
shows that even though the durations of treatments with diﬀerent frequencies can diﬀer markedly, in
terms of number of applications the diﬀerences are much less signiﬁcant. Moreover, Fig. B6 shows that
the curves for treatments with the same frequency but diﬀerent thresholds are roughly parallel. This
means that increasing the threshold λend multiplies the duration of the treatment by a number that, at
least in the interval shown, is independent of the eﬃcacy of the applications. Interestingly, the number
of applications depends only very weakly on λend.
The ﬁgures allow one to assess the eﬃcacy of the diﬀerent strategies. Not surprisingly, the time it
takes for a treatment to be eﬀective is positively correlated with the total number of applications of the
strategy. But the advantage of a detailed model is that it gives less intuitive predictions. For example,
Figs. B5 and B6 show that strategies that are applied every 3 days or less often require almost the same
number of applications. It also conﬁrms the results of [14], who showed that in the worst case, three
applications every 7 days were enough to eliminate all lice, if the treatment has 100% eﬃcacy against
mobile lice.
Interaction between populations
To model the interaction between colonies of head lice, we assume that there is a probability per day pt
that each mobile lice transfers (i.e. migrates) to another head. For simplicity, we have assumed random
mixing for the human populations considered, i.e. a louse on a given head can migrate to any other head
in the population. This parameter depends both on the behavioural and kinetic features that aﬀect the


## Page 10


10
0
20
40
60
80
100
0.0
0.2
0.4
0.6
0.8
1.0
0
20
40
60
80
100
0
20
40
60
 
 
probability of elimination
 
t
a
=4
 
t
a
=1
 
t
a
=1 
end
=0
 
t
a
=1 
end
=1
 
t
a
=1 
end
=2
(A)
(B)
 
duration of the treatment (days)
ef f icacy of  each applicacion (%)
Figure 4. Results of applying diﬀerent treatments to cure a head lice infestation. The upper panel
shows the probability that the infestation is cured (i.e. that all head lice and eggs are eliminated) and
the lower panel shows the duration of the treatment, when it is successful. Both variables are plotted as
functions of the fraction of lice that are eliminated by each application of the treatment for a ﬁxed
ovicidity of 10%. The limit time in our simulations to allow for the extintion of the colony was 500 days
of simulation time. Dotted vertical lines indicate the critical eﬃcacy of the treatments.
movement of lice (as, for example, the probability of ‘catching’ a passing hair shaft), as well on the social
factors that can make heads come together (playing together, sharing the same bed, etc.). Even though
there are some studies that try to quantify the mechanical aspects of the transmission of head lice [9,40],
many other factors remain whose quantiﬁcation seems very diﬃcult (many of them involving the various
ways of interaction among school-aged children). This makes it almost impossible to estimate pt from
ﬁrst principles.
To have an idea of the order of magnitude of pt we have used a diﬀerent method.
Recently, a
mathematical model of pediculosis [41] which treated head lice infestations as ‘infections’ (i.e. the number
of lice was not taken into account) determined that the number of secondary cases caused by an ‘infected’


## Page 11


11
70
80
90
100
2
3
4
5
6
7
8
9
10
70
80
90
100
15
25
35
45
55
65
  
t
a
=1  
  
t
a
=2   
 
end
=1 
  
t
a
=3   
 
end
=2 
  
t
a
=4  
  
t
a
=7
 
number of applications
ef f icacy of  each application (%)
(B)
(A)
 
duration of the treatment (days)
Figure 5. Comparison between the average durations (panel A) and between the number of
applications (panel B) for several treatments, when they are successful, as a function of the fraction of
lice eliminated by each application. Full symbols indicate systematic treatments, and ∆ta gives the
number of days between applications. Empty symbols correspond to a daily application (∆ta = 1) of
non systematic treatments which are stopped when the mobile lice remaining in the population are less
of equal than λend.
individual, usually called R0 [42], was slightly larger than 1. In terms of colonies of head lice, this is
equivalent to saying that, on average, during the whole life cycle of a colony, on average one adult female
lice migrates to a diﬀerent head to initiate a new colony. If we assume that the average duration of an
infestation is 2-3 weeks, and that the average daily number of adult female lice is 1, the resulting daily
migration probability should be between pt = .02 and pt = .07. As this gives only a rough estimate of
the range of ‘reasonable’ values for pt, we have performed simulations using diﬀerent values of pt, for
two diﬀerent scenarios detailed below. To avoid an unbounded growth of the number of lice, we have


## Page 12


12
70
80
90
100
3
4
5
6
7
8
9
70
80
90
100
10
15
20
25
30
35
40
45
ef f icacy of  each application (%)
(B)
 
t
a
=1
 
t
a
=3 
 
t
a
=1, 
end
=1  
 
t
a
=1, 
end
=2
 
t
a
=3, 
end
=1  
 
t
a
=3, 
end
=2 
number of applications
(A)
 
duration of the treatment (days)
Figure 6. Comparison between the average durations (panel A) and between the number of
applications (panel B) for several treatments, when they are successful, as a function of the fraction of
lice eliminated by each application. Squared symbols are systematic treatments, whereas the rest are
non systematic ones. Full symbols correspond to daily applications that are stopped when less than
λend mobile lice remain in the population. Empty symbols correspond to an application every 3 days.
assumed that at some point every infested individual starts some form of treatment. Diﬀerent surveys
have shown that this is indeed the case in most schools [43]. In the ﬁrst scenario we have considered
a population of 20 heads and we have assumed that in every infested head any louse can jump to any
other head, with probability pt. The treatment available to the population has an eﬃcacy of 80% and is
systematically applied every 4 days until no lice (mobiles or eggs) remain on that head. We have assumed
that the detection threshold for the start of the treatment, i.e. the number of mobile lice necessary for a
parent to notice that his/her child has an infestation, or to cause an itching feeling, is a number randomly


## Page 13


13
distributed between 10 and 20. Scenario 2 is obtained from scenario 1 by assuming that one individual
has a much larger threshold (100 mobile lice) for the start of the treatment. This choice is motivated by
the fact that, even though in most infestations only ≈10 lice are present, it is not uncommon to ﬁnd
a few children with much more acute infestations [28, 29]. As far as we know, no plausible biological
explanation has been put forward to account for this, thus it seems reasonable to assume that such heavy
infestations result from a delay in the beginning of the treatment.
Table 3. Result of the average of several variables over 1000 runs of collective infestations for scenario 1
(group of 20 heads with thresholds for treatment beginning randomly chosen between 10 and 20 mobile
lice). In the ﬁrst column the probability of transfer is indicated. Second column gives the average total
daily number of mobile lice involved. The third is the prevalence, i.e., the proportion of infested heads.
Fourth column indicates the average daily number of lice transferred from one head to another. The
ﬁfth and sixth columns give the average and median duration of collective infestations, respectively.
pt
total
prevalence
total
average duration
median duration
mobile
transferred
of infestation
of infestation
0.010
3.77
4.8%
0.14
28.88
24
0.050
4.91
6.3%
1.5
39.92
28
0.075
7.82
9.1%
8.68
68.43
32.5
0.100
13.07
14.1%
46.21
149.15
40
Table 4. Result of the average of several variables over 1000 runs of collective infestations for scenario
2 (almost identical to scenario 1, but with one individual having a treatment threshold of 100 mobile
lice). In the ﬁrst column the probability of transfer is indicated. Second column gives the average total
daily number of mobile lice involved. The third is the prevalence, i.e., the proportion of infested heads.
Fourth column indicates the average daily number of lice transferred from one head to another. The
ﬁfth and sixth columns give the average and median duration of collective infestations, respectively.
pt
total
prevalence
total
average duration
median duration
mobile
transferred
of infestation
of infestation
0.010
23.59
7.6%
1.89
72.93
73
0.050
30.48
19.4%
22.24
130.65
111
0.075
39.35
28.2%
83.80
243.47
171
0.100
51.89
38%
277.37
435.19
310.5
In Tables B3 and B4 we show the result of the average of several variables over 1000 runs of collective
infestations for both scenarios. One of the features that stands out is that in scenario 2 the presence of
the individual with the much larger threshold makes the collective infestation much more severe, in terms
both of duration and number of lice. Thus, this individual acts as what in epidemiology is known as a
‘superspreader’ [44]) and so, for want of a better term, in the following we use this word to refer to this
individual. One important aspect to notice is the diﬀerence between the average and the median of the
infestation duration, that can be rather large. This happens because the distribution of infestation times
is very skewed to the right, as can be seen from the histograms in Fig. B7.
Interestingly the values shown in the last two rows of Table 4 are in general consistent with the values
reported in a detailed study of lice infestations in several schools in Australia [28]. Even though that
study reports a somewhat higher number of lice per infested student than what our model predicts for
pt = 0.075 or pt = 0.1, it must be bear in mind that in this section we have used several assumptions
that might not be correct for that population. For example, parents might be using diﬀerent and less


## Page 14


14
0
200
400
600
800
0
150
300
450
 
 
 
 
scenario 1
p
t
=0.075
distribution average=68.43
distribution median=32.5
0
600
1200
1800
0
50
100
150
 
 
 
scenario 2
p
t
=0.075
distribution average=243.47
distribution median=171
counts
duration of infestation (days)
duration of infestation (days)
counts
0
150
300
450
600
0
100
200
300
 
 
 
scenario 2
p
t
=0.050
distribution average=130.65
distribution median=111
0
50
100
150
200
250
300
0
200
400
600
 
 
 
scenario 1
p
t
=0.050
distribution average=39.91
distribution median=28
Figure 7. Histograms of the duration of the collective infestation for 1000 runs of scenario 1 (upper
panels) and scenario 2 (lower panels) for two values of the probability of transfer: pt = 0.05 (left panels)
and pt = 0.075 (right panels).
eﬀective treatments from what we have assumed, and/or they might be starting to apply them with
diﬀerent thresholds. More importantly treatments are usually not applied in a systematic way, as has
been assumed in this section.
In this sense, it may be considered that ours are rather conservative
scenarios.
There are some interesting features that stand out when single runs are considered (see Fig. B8). One
is that even in scenario 1, where the infestation is rather mild in terms of total number of mobile lice,
re-infestations of the same head are not uncommon (see the evolution of mobile lice on head 1). For
scenario 2, infestations are made more severe by the presence of the superspreader. Fig. B8 shows that
scenario 2 infestations take a very long time to die out, even after the superspreader is no longer infested.
The histograms in Fig. B7 show that in general infestations last a very long time, which is consistent
with the widespread perception that head lice are very diﬃcult to eradicate from a human group, even
when individual actions are taken against the infestation.
It is important to note that the simulations shown above only include the heads in a group, and it does
not take into account the possible contagion from other members of the family of each child. To account
for this, we allow the inclusion of external lice to an otherwise closed group of heads. Our model shows


## Page 15


15
0
100
200
300
1
10
100
1000
0
25
50
75
100
125
1
10
100
0
25
50
75
1
10
0
15
30
45
60
1
10
days
 
 
 mobile lice (total)
 infested heads
 mobile lice (head 1)
 mobile lice (head 6)
scenario 2
p
t
=0.075
days
 
 
 
 mobile lice (total)
 infested heads
 mobile lice (head 1)
 mobile lice (head 6)
scenario 2
p
t
=0.050
 
 
 
 mobile lice (total)
 infested heads
 mobile lice (head 1)
 mobile lice (head 6)
scenario 1
p
t
=0.075
 
 
 
 mobile lice (total)
 infested heads
 mobile lice (head 1)
 mobile lice (head 5)
scenario 1
p
t
=0.050
Figure 8. Time evolution of 4 diﬀerent collective infestations in scenario 1 (upper panels) and scenario
2 (lower panels) for two values of the probability of transfer: pt = 0.05 (left panels) and pt = 0.075
(right panels). In all panels the total number of mobile lice as well as the number of infested heads is
shown. For the sake of clarity, we only show the evolution of the infestation of two heads. Head 1 is the
one where the ﬁrst female louse appears, whereas the other is randomly chosen. Besides, for scenario 2
head 1 is also the superspreader head.
that even a very weak ‘ﬂux’ of external lice, coming from family members or friends of the members of
the group, can produce a signiﬁcant increase in the duration of the collective infestation. As an example
of this, Fig. B9 shows the average (over 1000 simulations) duration of the collective infestation when one
female adult louse is introduced in a random head every n days in a population of 20 heads (inside the
colony the probability of transmission is pt = 0.075, and the treatment used consists of applications of
80% eﬃcacy every 4 days). Note that the introduction of one new female louse every two weeks suﬃces to
make the infestation last several months, or even years, even though all infested members use a systematic
treatment. Interestingly, the increase in prevalence, deﬁned as the proportion of infested heads, is much
less signiﬁcant reaching values that are still realistic.
Another important assumption is that each head is treated independently from other heads. But
logic, as well as some experiences [45, 46], suggest that ‘synchronized’ treatments might be eﬀective in


## Page 16


16
7
21
35
49
63
0
400
800
1200
1600
7
21
35
49
63
5
15
25
35
45
 
duration of the infestation (days)
n (days)
 scenario 1
 scenario 2
 
 
 
prevalence (%)
Figure 9. Average duration of infestation for a group of 20 heads in which an external female adult
louse is introduced every n days. Transmission probability is pt = 0.075 and the treatment used consists
of applications of 80% eﬃcacy every 4 days. Symbols represent average over 1000 simulations (lines are
guides to the eye). The inset shows the prevalence for the same situation, as a function of n.
eradicating head lice from a human group, be it a school or a community. Synchronized treatment of a
population means than when the number of mobile lice in one head becomes larger than a given threshold,
the systematic treatment is begun in every head of the population. In other words, a parent that detects
that his/her child has lice informs all the the other parents, who commit themselves to apply the same
treatment on exactly the same days. In the unsynchronized case the parents act in isolation and only
begin applying the treatment when lice are detected on his/her own child.
We have used our model to assess the performance of diﬀerent treatments in a group of 3 heads
(Fig. B10) and in a group of 20 heads (Fig. B11) with four diﬀerent transmission probabilities pt. We
have chosen a systematic treatment applied every 4 days with an eﬃcacy per application of 80%. We
compare the duration of the collective infestation of the synchronized case and the unsynchronized case
in scenario 1. The ﬁgures show that in this last case the duration of the treatment is multiplied by
a constant (at least in the range of eﬃcacies shown), and this constant gets larger as pt is increased.
Intuitively, the picture is clear: some lice manage to avoid the application of the remedy by jumping from
one head to another, and this gets worse with more mobile lice and larger groups of heads. On the other
hand, when the treatment is applied at the same moment in the whole group of heads there is almost no
dependence on the rate of transmission, because jumping from head to head does not help lice to avoid
the treatment. But the model allows us to quantify these eﬀects. For instance, the ﬁgures show that for
pt = 0.075 the lack of synchronization increases the duration of the infestation of 3 heads by almost 50 %,
whereas for a group of 20 heads lack of synchronization almost doubles the duration of the infestation. It
must be stressed that we are comparing with scenario 1, which lacks superspreaders. If these are included,
the eﬀect of synchronization is much more dramatic. To have an idea of the ‘perceived’ duration of the
infestation one must subtract the time it takes the population of lice to achieve the detection threshold,


## Page 17


17
which is approximately 3 weeks (see inset of Fig 3).
60
70
80
90
100
20
40
60
80
 p
t
=0.010
 p
t
=0.050
 p
t
=0.075
 p
t
=0.100
 
duration of the infestation (days)
ef f icacy of  each application (%)
3 heads (TL data)
Figure 10. Comparison between the duration of the infestation in a group of 3 heads, for a systematic
treatment applied every 4 days (∆ta = 4) applied in a synchronized (open symbols) and unsynchronized
way (full symbols), , for diﬀerent values of the transmission probability pt as a function of the eﬃcacy of
each application. For the unsynchronized case we have used scenario 1.
It is instructive to compare the eﬀect of applying systematic versus non systematic strategies in
groups of colonies. As in the previous section, the non systematic treatments cease to be applied when
the number of mobile lice is below a threshold λend. Note that, by deﬁnition, these treatments are not
synchronized because the precise days when the mobile lice number threshold is reached is an stochastic
event. In Figs. B12 and B13 we compare systematic treatments (synchronized and unsynchronized) with
treatments that have a threshold of 1 and 2 mobile lice. The ﬁgures show that the diﬀerence between
systematic and non-systematic treatments can be very large, even in the case that the former are not
synchronized. For instance, with an application eﬃcacy of 80 % non-systematic treatments can last more
than three times than the corresponding systematic treatment.
Discussion
We have presented in the previous sections a model of the evolution of populations of head lice based on
detailed data about their biology. It has allowed us to address questions related to the ‘natural’ growth
of a population, as well as to assess the eﬀectiveness of treatments that consist on several applications, as
a function of the eﬃcacy of each application. To explain the fact that colonies of head lice typically seem
to be composed of a few insects, in spite of their naturally exponential growth, the best candidate seems
to be self grooming of the host. But, whatever the mechanism, it is not clear what exactly would be its
action on individual lice. Using our model we ﬁnd that the reproductive success of female louse should
be drastically reduced to achieve a signiﬁcant slow down of population growth. On the other hand, a
modest increase of the mortality of the various life stages (as it is the case with grooming) can lead to a
very slow growth or even to the extinction of the population.
As is well known, a huge number of treatments have been proposed to deal with the problem of


## Page 18


18
60
70
80
90
100
20
60
100
140
 
ef f icacy of  each application (%)
20 heads (TL data)
 p
t
=0.010
 p
t
=0.050
 p
t
=0.075
 p
t
=0.100
 
duration of the infestation (days)
Figure 11. Comparison between the duration of the infestation in a group of 20 heads, for a
systematic treatment applied every 4 days applied in a synchronized (open symbols) and
unsynchronized way (full symbols), for diﬀerent values of the transmission probability pt as a function
of the eﬃcacy of each application. For the unsynchronized case we have used scenario 1.
pediculosis.
But, in general, the prediction of its outcome is either based on a few test cases, or in
reasonings that take into account a few loose estimates of some aspects of the biology of the louse, and
even in these cases, only very simple scenarios are analyzed. For example, assuming the treatment to be
100% eﬀective against head lice, in [14] the necessary application frequency for eradication is determined.
But even though in vitro studies seem to suggest that the eﬃcacy of some products is close to that value,
it must be acknowledged that applying the product in a real head, in a real situation, is very likely to
signiﬁcantly reduce that eﬃcacy. Thus, it is important to have a model where the result of a treatment
can be studied as a function of the eﬃcacy of each application. For the same example we ﬁnd that even
though 2 to 3 applications should be enough for a perfectly pediculicidal treatment, if the eﬃcacy of
each application is reduced to 80% the number of necessary applications increases to between 5 and 6
applications.
The model also allows the analysis of situations where a same treatment is applied in several diﬀerent
ways. As an example, we have analyzed what happens when treatments are applied systematically as
compared with the results of non systematic applications. Needless to say, when systematicity is dropped,
the exponential growth of possible treatments forces us to restrict to documented cases, or to common
sense. For the treatments analyzed we ﬁnd that systematicity can be very important: if the treatment is
stopped when there remains only one adult lice (presumably because it cannot be detected), the whole
duration of the treatment almost doubles the duration for the systematic variant. The problem with
systematic treatments is that one would not know when to stop, because it is almost impossible to detect
every lice and egg in a human head, and therefore it is impossible to know when the infestation has
been completely eradicated. But it is exactly in these cases that models like ours can be useful, because
they give a prediction of how many applications are necessary. In principle the model gives only average
values, but the width of the distribution of number of applications is not large. Thus, using one more
application than the average predicted by the model should ensure the eradication of lice in most cases.
To model the ‘contagion’ of pediculosis among members of the same group, we have used the simplest


## Page 19


19
60
70
80
90
100
20
50
80
110
efficacy of each application (%)
3 heads (TL data)
 
duration of the infestation (days)
 sincr, 
t
a
=4
 no sincr, 
t
a
=4
 no sincr,
end
=1
 no sincr,  
end
=2
Figure 12. Comparison between the average duration over 1000 realizations of 4 diﬀerent treatments
in group of 3 heads, as a function of the eﬃcacy of each application. Squares and circles correspond to
systematic treatments, whereas triangles represent non-systematic ones.
variant: at all times every louse can jump to any other head, with a probability per day pt. Even though
this is a very simpliﬁed picture of reality (it lacks the possible formation of playing subgroups among
children, does not take into account the likely diﬀerences in mobility for the various life stages of the louse,
etc.) the model seems to capture the essence of the process, because the results obtained are compatible
with what is found in the literature. We ﬁnd that even when every individual applies a treatment to try
to eradicate head lice, the duration of the collective infestation can be very large. The best strategy to
completely eliminate a collective infestation in a reasonable time seems to be the synchronized application
of the same treatment.
Our model makes use of most of the data available about the biology of the head louse, what makes
it dependent on a large number of parameters. In spite of this, we have shown that the predictions given
are quite robust, because they are very similar for two diﬀerent sets of data, one obtained by rearing
head lice (TL) and the other obtained by rearing body lice (ES).
Evidently, even though our model is quite detailed, it could still be improved in many ways. For
example, we have assumed that males are readily available and that with only one fertilization female
lice are able to lay eggs until they die. This assumption could be dropped, but then one should add some
form of interaction between male and female lice to the model, and have some idea of how many eggs can
be laid after each fertilization. For some treatments, the eﬃcacy could be assumed to depend on the life
stage of the louse, and even on the number of lice present on the head which is being treated. Regarding
contagion, the assumption of random mixing could be dropped, introducing a social network to model
the interactions between children at school. Note however that many of these modiﬁcations would need
to be based on real data that either are still very incomplete or do not even exist yet.
In a sense, our model is a compromise that tries to use as much detailed data as possible, while at
the same time using reasonable assumptions for those processes that still are not well known. Yet, the


## Page 20


20
60
70
80
90
100
10
50
90
130
170
210
250
290
efficacy of each application (%)
20 heads (TL data)
 
duration of the infestation (days)
 sincr, 
t
a
=4
 no sincr,
t
a
=4
 no sincr,
end
=1
 no sincr, 
end
=2
Figure 13. Comparison between the average duration over 1000 realizations of 4 diﬀerent treatments
in group of 20 heads, as a function of the eﬃcacy of each application. Squares and circles correspond to
systematic treatments, whereas triangles represent non-systematic ones.
level of detail used makes our model a useful tool to go beyond the usual educated guesses and predict
the outcome of a large number of strategies in a number of diﬀerent situations. In this sense, the cases
analyzed in this paper are only examples of what can be done with the model. Its real strength lies in
the possibility of adjusting it to analyze the practical strategies that are suggested to eradicate lice of
real human groups in speciﬁc real contexts.
Acknowledgements
We thank Guillermo Abramson for suggesting to us that building a model of populations of head lice
could be interesting as well as useful.
References
1. Anderson AL, Chaney E (2009) Pubic lice (pthirus pubis): History, biology and treatment vs.
knowledge and beliefs of us college students. Int J Envirn Res Public Health 6: 592–600.
2. Meinking TL (1999) Infestations. Current Problems in Dermatology 11: 75–118.
3. Burgess IF (2004) Human lice and their control. Annu Rev Entomol 49: 457–481.
4. Light JE, Toups MA, Reed DL (2008) Whats in a name: The taxonomic status of human head
and body lice. Molecular Phylogenetics and Evolutiony 47: 1203–1216.


## Page 21


21
5. Li W, Ortiz G, Fournier PE, Gimenez G, Reed DL, et al. (2010) Genotyping of human lice suggests
multiple emergences of body lice from local head louse populations.
PLoS Neglected Tropical
Diseases 4: e641.
6. Falagas ME, K MD, Rafailidis PI, Panos G, Pappas G (2008) Worldwide prevalence of head lice.
Emerging Infectious Diseases 14: 1493–1494.
7. Speare R, Canyon D, Melrose W (2006) Quantiﬁcation of blood intake of the head louse: Pediculus
humanus capitis. International Journal of Dermatology 45: 543–546.
8. Takano-Lee M, Yoon KS, Edman JD, Mullens B, Clark M John (2003) In vivo and in vitro rearing
of pediculus humanus capitis (anoplura: Pediculidae). Journal of Medical Entomology 40: 628–635.
9. Canyon DV, Speare R, Muller R (2002) Indirect transmission of head lice via inanimate objects.
The Journal of Investigative Dermatology 119: 629–631.
10. Burkhart CN, Burkhart CG (2007) Fomite transmission in head lice. Journal of the American
Academy of Dermatology 56: 1044–1047.
11. Canyon DV, Speare R (2010) Indirect transmission of head lice via inanimate objects. The Open
Dermatology Journal 4: 72–76.
12. McLaury P (1983) Head lice: Pediatric social disease. American Journal of Nursing 83: 1300–1303.
13. Hansen RC, OHaver J (2004) Economic considerations associated with pediculus humanus capitis
infestation. Clin Pediatr 43: 523–527.
14. Lebwohl M, Clark L, Levitt J (2007) Therapy for head lice based on life cycle, resistance, and
safety considerations. Pediatrics 119: 965–974.
15. Watt KEF (1966) Systems Analysis in Ecology. Academic Press.
16. Begon M, Townsend CR, Harper JL (2006) Ecology: From Individuals to Ecosystems. Blackwell
Publishing.
17. Beugnet F, Chalvet-Monfray K, Sabatier P (1998) Using of a mathematical model to study the
control measures of the cattle tick boophilus micropilus populations in new caledonia. Veterinary
parasitology 77: 277–288.
18. Beugnet F, Porphyre T, Sabatier P, Chalvet-Monfray K (2004) Use of a mathematical model to
study the dynamics of ctenocephalide felis populations in the home environment and the impact of
various control measures. Parasite 11: 387–399.
19. Revie CW, Robbins C, Gettinby G, Kelly L, Treasurer JW (2005) A mathematical model of the
growth of sea lice, lepeophtheirus salmonis, populations on farmed atlantic salmon, salmo salar
l., in scotland and its use in the assessment of treatment strategies. Journal of Fish Diseases 28:
603–613.
20. Leslie PH (1945) On the use of matrices in population mathematics. Biometrika 33: 183–213.
21. Caswell H (2001) Matrix Population models: Construction, analysis and interpretation. Sinauer
Associates.
22. Lefkovitch LP (1965) The study of populartion growth in organisms grouped by stages. Biometrics
21: 1–18.


## Page 22


22
23. Evans FC, Smith FE (1983) The intrinsic rate of natural increase for the human louse, pediculus
humanus l. American Naturalist 86: 299–310.
24. Pinder III JE, Wiener JG, Smith MH (1978) The weibull distribution: A new method of summa-
rizing survivorship data. Ecology 59: 175–179.
25. Allman ES, Rhodes JA (2004) Mathematical Models in Biology: an introduction.
Cambridge
University Press.
26. Bacot A (1915) A contribution to the bionomics of pediculus humanus (vestimenti) and pediculus
capitis. Parasitology 9: 228–258.
27. Maunder JW (1993) An update on head lice. Health Visitor 66: 317–318.
28. Speare R, Thomas G, Cahill C (2002) Head lice are not found on ﬂoors in primary school classrooms.
Australian and New Zealand Journal of Public Health 26: 208–211.
29. Mumcuoglu KY, Miller J, Goﬁn R, Adle B, Ben-Ishai F, et al. (1990) Epidemiological studies on
head lice infestations in israel. International Journal of Dermatology 29: 502–507.
30. Krasnov BR (2008) Functional and evolutionary ecology of ﬂeas: a model for ecological parasitology.
Cambridge University Press.
31. Ben-Yakir D, Mumcuoglu KY, Manor O, Galun R (1994) Immunization of rabbits with a midgut
extract of the human body louse pediculus humanus humanus: the eﬀect of induced resistance on
the louse population. Medical and Veterinary Entomology 8: 114–118.
32. Mumcuoglu KY, Ben-Yakir D, Ochanda JO, Miller J, Galun R (1997) Immunization of rabbits
with faecal extract of pediculus humanus, the human body louse: eﬀects on louse development and
reproduction. Medical and Veterinary Entomology 11: 315–318.
33. Buxton PA (1941) Discussion on prevention and treatment of parasitic diseases: recent work on
the louse. Proceedings of the Royal Society of Medicine 34: 193–204.
34. Burgess IF (2010) Do nit removal formulations and other treatments loosen head louse eggs and
nits from hair? Medical and Veterinary Entomology 24: 55–61.
35. Lapeere H, Vander Stichele R, Naeyaert J (2003) Evidence in the treatment of head lice: drowning
in a swamp of reviews. Clinical Infectious Diseases 37: 1580–1582.
36. Heukelbach J, Canyon DV, Oliveira F, Muller R, Speare R (2008) In vitro eﬃcacy of over-the-
counter botanical pediculicides against the head louse pediculus humanus var capitis based on a
stringent standard for mortality assessment. Medical and Veterinary Entomology 22: 264–272.
37. Vander Stichele RH, Dezeure EM, Bogaert MG (1995) Systematic review of clinical eﬃcacy of
topical treatments for head lice. BMJ 311: 604–608.
38. Sonnberg S, Oliveira FA, Ara´ujo de Melo IL, de Melo Soares MM, Becher H, et al. (2010) Ex Vivo
development of eggs from head lice (pediculus humanus capitis). The Open Dermatology Journal
4: 82–89.
39. Mumcuoglu KY, Friger M, Ioﬀe-Uspensky I, Ben-Ishai F, Miller J (2001) Louse comb versus direct
visual examination for the diagnosis of head louse infestations. Pediatric Dermatology 18: 9–12.


## Page 23


23
40. Takano-Lee M, Edman JD, Mullens BA, Clark M John (2005) Transmission potential of the human
head louse, pediculus capitis (anoplura: Pediculidae). International Journal of Dermatology 44:
811–816.
41. Stone P, Wilkinson-Herbots H, Isham V (2008) A stochastic model for head lice infections. Journal
of Mathematical Biology 56: 743–763.
42. Anderson RM, May RM (1992) Infectious Diseases of Humans: Dynamics and Control. Oxford
University Press.
43. Speare R, Buettner P (1999) Head lice in pupils of a primary school in australia and implications
for control. International Journal of Dermatology 38: 285–290.
44. Lloyd-Smith JO, Schreiber SJ, Kopp PE, Getz W (2005) Superspreading and the eﬀect of individual
variation on disease emergence. Nature 438: 355–359.
45. Chouela E, Abelda˜no A, Cirigliano M, Ducard M, Neglia V, et al. (1997) Head louse infestations:
epidemiologic survey and treatment evaluation in argentinian schoolchildren. International Journal
of Dermatology 36: 819–825.
46. Vermaak Z (1996) Model for the control of pediculus humanus capitis. Public Health 110: 283–288.


## Page 24


24
Appendix A
In this appendix we provide details of the two sets of data used to build our models. We include additional
tables constructed from the original data sets. We also give a brief description of the algorithm we use
to perform the numerical simulations shown in the paper.
Description of data used for the models
The data we have used for the models were taken from references [8] and [23] of the main text. The
fraction of eggs that hatch a given number of days after oviposition are given in Table A1. These data do
not include mortality of the whole egg stage, which was found to be 25% for Takano-Lee (TL) data and
12.3% for Evans-Smith (ES) ones. Table A2 gives the fraction of lice that undergo each moult a given
number of days after hatching. Mortality is included in these sets of data and consequently the fractions
for each moult do not add up to 1. The average mortality of the whole larvar stage is 25% (TL) and
13.7% (ES). As it is not possible to know how many lice or eggs die each day, we have used in our model a
mortality rate of 3% per day (TL) and 1% per day (ES) for both the egg and larval stages. These values
were chosen so that the average mortality obtained from them is consistent with the average mortality
data.
We have assumed that females lay a daily average of 5 eggs, from their fourth day of adulthood until
their deaths. For the ﬁrst three days we have assumed that females lay an average of 0, 2 and 4 eggs,
respectively. This corresponds to the rise observed in egg production in both sets of data. Moreover, we
have assumed that half of the eggs that hatch give rise to female lice, because no data set was reported
to be sex-biased.
Table A5. Fraction of eggs that hatch at a given day after oviposition, with respect to the total of
eggs that hatch (i.e. eggs which do not hatch are not taken into account).
Takano-Lee
Evans-Smith
days
fraction
days
fraction
7
0.299
6
0.144
8
0.285
7
0.174
9
0.211
8
0.298
10
0.127
9
0.305
11
0.078
10
0.079
For the ES data, the fraction of lice that are alive x days after the last moult can be ﬁtted by a
Weibull function: f(x) = exp(−x/a)2, with a = 20.0. Fig. A14 shows that the ﬁt is very good for female
lice. The TL data are not so detailed and only give average and variance for the mortalities. We have
assumed that the functional behaviour should be the same as for ES data and therefore we have simply
looked for the value of a which gives the average and variance of the Weibull function closest to the TL
data: average mortality 20.2 ± 1.4. The value found is a = 22.8 which gives an average of 20.2 ± 2.3.
Note that the number of lice for which the TL average was obtained is relatively small: 19 female lice.
A remark is in order regarding TL data. In their paper, the authors give the vital parameters of three
strains of head lice, collected in three diﬀerent places: California, Ecuador, and Florida. We have only
used the data corresponding to the California strain because it has better statistics (more individuals
for many life stages) and, more importantly, because the diﬀerences between strains are smaller than
diﬀerences between the California strain data and ES data.


## Page 25


25
Table A6. Fraction of lice that moult at a given day after hatching. Fractions are expressed respect to
the total of lice that have undergone the previous moult. Note that for some moults fractions do not
add up to 1, reﬂecting the fact that some lice died before that moult.
Takano-Lee
Evans-Smith
days
fraction
days
fraction
First Moult
3
0.96
4
0.141
4
0.04
5
0.488
6
0.308
7
0.026
Second Moult
5
0.673
8
0.413
6
0.154
9
0.512
7
0.02
10
0.050
Third Moult
8
0.591
12
0.325
9
0.273
13
0.497
14
0.141
Fraction of lice alive 
0
0.2
0.4
0.6
0.8
1
 
days after last moult
0
10
20
30
40
50
 
Figure A14. Fraction of lice alive as a function of the number of days elapsed since the last moult.
Symbols correspond to ES data. The full curve is a ﬁt to the curve of female lice mortality. The dotted
curve gives the same average and variance of the mortalities in the TL data.
Simulations
As there are many relevant variables that cannot be calculated with the theoretical approach, we have
resorted to stochastic simulations. This also allow us to see what happens in single infestations. In the
following we give a brief description of the algorithm used.
All simulations start with an adult female louse that has moulted 10 days before. The number of days


## Page 26


26
that she will live is a random number drawn from the corresponding mortality distribution (mentioned
in the previous subsection). In a ‘day’ of computation the following steps are followed:
1) grooming: each adult and nymph is killed with a given probability (.05 in all cases).
2) nymph and egg mortality: each nymph and egg is killed with a probability given probability (.01 for
ES data and .03 for TL ones).
3) births: for each alive female adult lice a random integer number is drawn to know how many eggs she
will lay. This depends on her age:
-adults less than 3 days old lay no eggs
-3-day olds lay 1, 2, or 3 eggs with probabilities 0.25, 0.5, 0.25, respectively.
-4-day olds lay 3, 4, or 5 eggs with probabilities 0.25, 0.5, 0.25, respectively.
-adults older than 4 days lay 4, 5, or 6 eggs with probabilities 0.25, 0.5, 0.25 respectively.
Each egg is assigned 5 random integer numbers corresponding to the day each of the life stages will
begin: hatching, ﬁrst moult, second moult, third moult, and death. Every number is drawn from the
corresponding distribution (see previous subsection). The internal clock of each new egg is set to 0.
4) death: all adults whose internal clock reaches the established date of death are killed.
5) contagion: each alive female adult louse jumps to a randomly chosen head with a probability pt.
6) treatment: each adult and nymph is killed with a probability given by the pediculicidity of the appli-
cation, and eggs are killed with the corresponding ovicidal probability.
7) counting: the number of alive lice in each life stage is counted.
8) updating: the internal clock of each alive louse is incremented in one day.
In the oviposition step we have chosen a set of probabilities for the numbers of eggs layed, to add
some stochasticity to the process. But we have checked that, given that the average is conserved, results
depend only very weakly on these probabilities.
Appendix B
In the main text, most tables and ﬁgures are made only with the TL data, to avoid a multiplication of
ﬁgures and tables. In this appendix we provide for each of them in the main text its analogue built from
ES data. To make the comparison easier, ﬁgures and tables have the same number as their analogue in
the main text, but preceded by a letter B.
Table B3. Result of the average of several variables over 1000 runs of collective infestations for
scenario 1 (group of 20 heads with thresholds for treatment beginning randomly chosen between 10 and
20 mobile lice). In the ﬁrst column the probability of transfer is indicated. Second column gives the
average total daily number of mobile lice involved. The third is the prevalence, i.e., the proportion of
infested heads. Fourth column indicates the average daily number of lice transferred from one head to
another. The ﬁfth and sixth columns give the average and median duration of collective infestations,
respectively.
pt
total
prevalence
total
average duration
median duration
mobile
transferred
of infestation
of infestation
0.010
3.67
4.57%
0.095
27.11
24
0.050
4.48
5.78%
0.82
34.22
24
0.075
5.43
6.94%
2.53
46.41
27
0.100
6.97
8.63%
6.60
63.94
33


## Page 27


27
0
25
50
75
100
10
-1
10
1
10
3
10
5
10
0
10
1
10
2
10
3
10
4
0
20
40
 
 
time (days)
 mobiles (adults + nymphs)
 adults
 nymphs
 eggs
number of lice
 
 
 
Figure B1. Average number of lice of a colony that is started at day 0 by a female that had her last
moult 10 days before. Symbols represent averages taken over 1000 populations whereas full lines
represent the theoretical predictions. The inset shows the ﬁrst days of one of these populations. Here,
as in the rest of the ﬁgures, the error bars represent the standard error of the mean. Data whose error
bars are not shown have standard errors lower than symbol size.
Table B4. Result of the average of several variables over 1000 runs of collective infestations for scenario
2 (almost identical to scenario 1, but with one individual having a treatment threshold of 100 mobile
lice). In the ﬁrst column the probability of transfer is indicated. Second column gives the average total
daily number of mobile lice involved. The third is the prevalence, i.e., the proportion of infested heads.
Fourth column indicates the average daily number of lice transferred from one head to another. The
ﬁfth and sixth columns give the average and median duration of collective infestations, respectively.
pt
total
prevalence
total
average duration
median duration
mobile
transferred
of infestation
of infestation
0.010
22.77
6.55%
1.40
72.59
73
0.050
25.52
14.35%
12.53
112.13
107
0.075
29.36
19.65%
30.89
161.02
139
0.100
35.54
25.8%
71.80
231.59
182
Figure Legends
Tables


## Page 28


28
0
20
40
60
80
100
0.00
0.25
0.50
0.75
1.00
0
20
40
60
80
0
5
10
15
15
20
25
 
duration of the infestation (days)
fraction of extinctions
ef f icacy of  grooming (%)
 
 
 
efficacy of grooming (%)
days required to have 15 lice
 
 
 
Figure B3. Fraction of extinctions (squares), and average duration of the infestation for the extinct
populations (circles), as a function of the eﬃciency of grooming. Averages were taken over 1000
realizations, with a limit time of 500 simulation days (i.e. we only count extinctions happening within
the ﬁrst 500 days). The critical grooming eﬃcacy is deﬁned as the value at which the fraction of
extinctions reach the unity. In this plot, this happens for eﬃcacies closer to 15%. Inset: Number of days
required to reach a population of 15 lice as a function of the eﬃcacy of grooming.


## Page 29


29
0
20
40
60
80
100
0.0
0.2
0.4
0.6
0.8
1.0
0
20
40
60
80
100
0
20
40
60
(A)
 
t
a
=4
 
t
a
=1
 
t
a
=1 
end
=0
 
t
a
=1 
end
=1
 
t
a
=1 
end
=2
 
 
(B)
probability of elimination
ef f icacy of  each application (%)
 
duration of the treatment (days)
Figure B4. Results of applying diﬀerent treatments to cure a head lice infestation. The upper panel
shows the probability that the infestation is cured (i.e. that all head lice and eggs are eliminated) and
the lower panel shows the duration of the treatment, when it is successful. Both variables are plotted as
functions of the fraction of lice that are eliminated by each application of the treatment for a ﬁxed
ovicidity of 10%. The limit time in our simulations to allow for the extinction of the colony was 500
days of simulation time. Dotted vertical lines indicate the critical eﬃcacy of the treatments.


## Page 30


30
70
80
90
100
5
10
15
20
25
30
70
80
90
100
2
3
4
5
6
7
8
(A)
 
ef f icacy of  each application (%)
 
duration of the treatment (days)
(B)
  
t
a
=1  
  
t
a
=2   
 
end
=1 
  
t
a
=3   
 
end
=2 
  
t
a
=4  
  
t
a
=7
 
number of applications
Figure B5. Comparison between the average durations (panel A) and between the number of
applications (panel B) for several treatments, when they are successful, as a function of the fraction of
lice eliminated by each application. Full symbols indicate systematic treatments, and ∆ta gives the
number of days between applications. Empty symbols correspond to a daily application (∆ta = 1) of
non systematic treatments which are stopped when the mobile lice remaining in the population are less
of equal than λend.


## Page 31


31
70
80
90
100
2
3
4
5
6
7
8
70
80
90
100
5
10
15
20
25
30
ef f icacy of  each application (%)
(B)
 
t
a
=1
 
t
a
=3 
 
t
a
=1, 
end
=1  
 
t
a
=1, 
end
=2
 
t
a
=3, 
end
=1  
 
t
a
=3, 
end
=2 
number of applications
(A)
 
duration of the treatment (days)
Figure B6. Comparison between the average durations (panel A) and between the number of
applications (panel B) for several treatments, when they are successful, as a function of the fraction of
lice eliminated by each application. Squared symbols are systematic treatments, whereas the rest are
non systematic ones. Full symbols correspond to daily applications that are stopped when less than
λend mobile lice remain in the population. Empty symbols correspond to an application every 3 days.


## Page 32


32
0
100
200
300
400
0
100
200
300
400
 
 
 
scenario 1
p
t
=0.075
distribution average=46.413
distribution median=27
0
50
100
150
200
0
150
300
450
600
 
 
 
scenario 1
p
t
=0.050
distribution average=34.215
distribution median=24
0
200
400
600
800
0
50
100
150
200
 
 
scenario 2
p
t
=0.075
distribution average=161.017
distribution median=139
0
100
200
300
400
500
0
100
200
300
 
 
scenario 2
p
t
=0.050
distribution average=112.131
distribution median=107
counts
duration of infestation (days)
duration of infestation (days)
counts
Figure B7. Histograms of the duration of the collective infestation for 1000 runs of scenario 1 (upper
panels) and scenario 2 (lower panels) for two values of the probability of transfer: pt = 0.05 (left panels)
and pt = 0.075 (right panels).


## Page 33


33
0
30
60
90
120
1
10
100
0
20
40
60
80
100
1
10
100
0
10
20
30
1
10
0
10
20
30
40
50
1
10
days
 
 
 mobile lice (total)
 infested heads
 mobile lice (head 1)
 mobile lice (head 5)
scenario 2
p
t
=0.075
days
 
 
 
 mobile lice (total)
 infested heads
 mobile lice (head 1)
 mobile lice (head 5)
scenario 2
p
t
=0.050
 
 
 mobile lice (total)
 infested heads
 mobile lice (head 1)
 mobile lice (head 6)
scenario 1
p
t
=0.075
 
 
 
 mobile lice (total)
 infested heads
 mobile lice (head 1)
 mobile lice (head 8)
scenario 1
p
t
=0.050
Figure B8. Time evolution of 4 diﬀerent collective infestations in scenario 1 (upper panels) and
scenario 2 (lower panels) for two values of the probability of transfer: pt = 0.05 (left panels) and
pt = 0.075 (right panels). In all panels the total number of mobile lice as well as the number of infested
heads is shown. For the sake of clarity, we only show the evolution of the infestation of two heads. Head
1 is the one where the ﬁrst female louse appears, whereas the other is randomly chosen. Besides, for
scenario 2 head 1 is also the superspreader head.


## Page 34


34
7
21
35
49
63
0
400
800
1200
1600
7
21
35
49
63
5
15
25
35
 
duration of the infestation (days)
n (days)
 scenario 1
 scenario 2
 
 
 
prevalence (%)
Figure B9. Average duration of infestation for a group of 20 heads in which an external female adult
louse is introduced every n days. Transmission probability is pt = 0.075 and the treatment used consists
of applications of 80% eﬃcacy every 4 days. Symbols represent average over 1000 simulations (lines are
guides to the eye). The inset shows the prevalence for the same situation, as a function of n.
60
70
80
90
100
20
30
40
50
3 heads (ES data)
duration of the infestation (days)
ef f icacy of  each application (%)
 p
t
=0.010
 p
t
=0.050
 p
t
=0.075
 p
t
=0.100
 
Figure B10. Comparison between the duration of the infestation in a group of 3 heads, for a
systematic treatment applied every 4 days (∆ta = 4) applied in a synchronized (open symbols) and
unsynchronized way (full symbols), , for diﬀerent values of the transmission probability pt as a function
of the eﬃcacy of each application. For the unsynchronized case we have used scenario 1.


## Page 35


35
60
70
80
90
100
20
40
60
80
20 heads (ES data)
duration of the infestation (days)
ef f icacy of  each application (%)
 p
t
=0.010
 p
t
=0.050
 p
t
=0.075
 p
t
=0.100
 
Figure B11. Comparison between the duration of the infestation in a group of 20 heads, for a
systematic treatment applied every 4 days applied in a synchronized (open symbols) and
unsynchronized way (full symbols), for diﬀerent values of the transmission probability pt as a function
of the eﬃcacy of each application. For the unsynchronized case we have used scenario 1.
60
70
80
90
100
20
40
60
80
100
 sincr, 
t
a
=4
 no sincr, 
t
a
=4
 no sincr, 
end
=1
 no sincr, 
end
=2
3 heads (ES data)
duration of the infestation (days)
ef f icacy of  each application (%)
 
Figure B12. Comparison between the average duration over 1000 realizations of 4 diﬀerent treatments
in group of 3 heads, as a function of the eﬃcacy of each application. Squares and circles correspond to
systematic treatments, whereas triangles represent non-systematic ones.


## Page 36


36
60
70
80
90
100
10
50
90
130
170
210
250
20 heads (ES data)
duration of the infestation (days)
ef f icacy of  each application (%)
 sincr, 
t
a
=4
 no sincr, 
t
a
=4
 no sincr, 
end
=1
 no sincr, 
end
=2
 
Figure B13. Comparison between the average duration over 1000 realizations of 4 diﬀerent treatments
in group of 20 heads, as a function of the eﬃcacy of each application. Squares and circles correspond to
systematic treatments, whereas triangles represent non-systematic ones.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
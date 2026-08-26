---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1002.4661v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1002.4661v1_Complementary_approaches_to_understanding_the_plant_circadian_clock

> Source: 1002.4661v1_Complementary_approaches_to_understanding_the_plant_circadian_clock.pdf

> Pages: 19

---


## Page 1


E. Merelli and P. Quaglia (Eds.)
From Biology To Concurrency and back 2010 (FBTC’10)
EPTCS 19, 2010, pp. 1–19, doi:10.4204/EPTCS.19.1
c⃝Akman, Guerriero, Loewe and Troein
This work is licensed under the
Creative Commons Attribution License.
Complementary approaches to understanding
the plant circadian clock
Ozgur E. Akman1,∗
Maria Luisa Guerriero1
Laurence Loewe1
Carl Troein1,2
1 Centre for Systems Biology at Edinburgh, University of Edinburgh, UK
2 School of Biological Sciences, University of Edinburgh, UK
∗Current address: School of Engineering, Computing & Mathematics, University of Exeter, UK
Circadian clocks are oscillatory genetic networks that help organisms adapt to the 24-hour day/night
cycle. The clock of the green alga Ostreococcus tauri is the simplest plant clock discovered so far.
Its many advantages as an experimental system facilitate the testing of computational predictions.
We present a model of the Ostreococcus clock in the stochastic process algebra Bio-PEPA and
exploit its mapping to diﬀerent analysis techniques, such as ordinary diﬀerential equations, stochastic
simulation algorithms and model-checking. The small number of molecules reported for this system
tests the limits of the continuous approximation underlying diﬀerential equations. We investigate the
diﬀerence between continuous-deterministic and discrete-stochastic approaches. Stochastic simula-
tion and model-checking allow us to formulate new hypotheses on the system behaviour, such as the
presence of self-sustained oscillations in single cells under constant light conditions.
We investigate how to model the timing of dawn and dusk in the context of model-checking,
which we use to compute how the probability distributions of key biochemical species change over
time. These show that the relative variation in expression level is smallest at the time of peak ex-
pression, making peak time an optimal experimental phase marker. Building on these analyses, we
use approaches from evolutionary systems biology to investigate how changes in the rate of mRNA
degradation impacts the phase of a key protein likely to aﬀect ﬁtness. We explore how robust this
circadian clock is towards such potential mutational changes in its underlying biochemistry. Our
work shows that multiple approaches lead to a more complete understanding of the clock.
1
Introduction
The daily cycles in sunlight, temperature and other environmental parameters are highly important to
most organisms. To follow and anticipate these cycles, living cells generate biochemical rhythms with
a period of approximately 24 hours (circadian). The majority of the known circadian clocks, including
those in eukaryotes, are based on one or more interlocking transcriptional feedback loops between a set
of key genes. Crucial to the function of the clock is its ability to entrain to environmental signals (i.e. to
adjust its internal rhythm by synchronising with external cycles), so that the phase of gene expression is
maintained under changes to the length of the day (photoperiod). Such entrainment acts through various
photoreceptor pathways, where light aﬀects kinetic parameters of the core clock. In addition to circadian
entrainment, a deﬁning feature of circadian clocks is that they exhibit continued oscillations in constant
light conditions [11].
The circadian clocks of many organisms are organised around complex feedback loop architectures,
making the determination of design principles a challenging computational problem. Although research
has revealed much about the clock of the foremost model plant organism, Arabidopsis thaliana, there
are still unidentiﬁed components and inconsistencies between computational models and experimental
observations [16]. For this reason, to increase our mechanistic understanding of circadian clocks, it is


## Page 2


2
Complementary approaches to understanding the plant circadian clock
desirable to investigate simpler systems that possess functional similarity with more complex networks.
The circadian clock of the green alga Ostreococcus tauri [8] is the simplest plant clock discovered so far,
and is thus an ideal model system for understanding plant circadian function with the help of experiments,
simulations and theory. A quantitative model describing the biochemical reactions of the Ostreococcus
clock can serve as a focal point for this research, yielding a low-dimensional test system for various
mathematical analysis techniques.
Bio-PEPA [6] is a stochastic process algebra speciﬁcally deﬁned to model and analyse biochemical
systems. Exploiting the deﬁned formal mappings of Bio-PEPA models into a number of equivalent rep-
resentations, it is possible to analyse Bio-PEPA models using diﬀerent mathematical and computational
techniques, including ordinary diﬀerential equations (ODEs), stochastic simulation algorithms (SSAs)
and model-checking.
In previous work we used both ODEs and SSAs to model the clock of the fungus Neurospora crassa,
demonstrating that combining diﬀerent analysis methods is important for fully quantifying the relation-
ship between feedback architecture and circadian behaviour [1]. Here we build on this approach, ap-
plying a broader range of computational techniques to the Ostreococcus clock. We develop and analyse
a Bio-PEPA model of the clock, focusing on various stochastic methods which are the most appropri-
ate in this case due to the low copy numbers characteristic of the system. In particular, we exploit the
automatic generation of PRISM models from Bio-PEPA to carry out a novel application of the PRISM
model-checker [15] to a circadian model, computing time-dependent probability distributions for the
clock components. We use the model to quantify the variability and robustness of the clock’s functional
behaviour with respect to the following factors: (i) internal stochastic noise, the inevitable consequence
of a system comprising a small number of molecules; (ii) environmental changes, such as photoperiod
variations and transitions between constant light/darkness; and (iii) mutational changes that aﬀect the
biochemical reaction rates of our model, representing perturbations to the system that occur on an evo-
lutionary timescale.
The rest of our paper is structured as follows. After an overview of Bio-PEPA in Section 2, the Os-
treococcus clock is introduced in Section 3, followed by the description of the corresponding Bio-PEPA
model. In Section 4 we analyse the model using various approaches. We ﬁrst use stochastic simula-
tion to investigate how diﬀerent light conditions aﬀect the oscillations of the clock. We then explore
approaches for modelling light entrainment in a continuous-time Markov chain (CTMC) before using
model-checking to compute the time-dependent probability distributions of protein levels. This enables
us to identify the phase markers that are most robust to stochastic ﬂuctuations. Finally we use ideas from
a recently developed framework for evolutionary systems biology [18] to test how mutational changes
in mRNA degradation rate aﬀect the phase of oscillations in comparison to the inherent stochastic noise
that is present at the individual cell level. The full Bio-PEPA model is given in Appendix A.
2
An overview of Bio-PEPA
Bio-PEPA [6] is a stochastic process algebra, recently developed for the modelling and analysis of bi-
ological systems. We give here a brief overview of the main features of the language. For a detailed
presentation of its syntax and semantics, see [6].
The main components of a Bio-PEPA system are the species components, describing the behaviour
of each species, and the model component, specifying all interactions and initial amounts of species. The
syntax of Bio-PEPA components is given by:
S ::= (α,κ) op S | S +S | C
with op = ↓| ↑| ⊕| ⊖| ⊙
P ::= P▷◁
I P | S (x)


## Page 3


Akman, Guerriero, Loewe and Troein
3
where S is the species component and P is the model component. In the preﬁx term (α,κ) op S , κ is
the stoichiometry coeﬃcient of species S in reaction α, and the preﬁx combinator “op” represents the
role of S in the reaction. Speciﬁcally, ↓indicates a reactant, ↑a product, ⊕an activator, ⊖an inhibitor
and ⊙a generic modiﬁer. The notation α op is a shorthand for (α,κ) op S when κ = 1. The operator
“+” expresses a choice between possible actions, and the constant C is deﬁned by an equation C
def= S .
The process P▷◁
I Q denotes synchronisation between components P and Q; the set I determines the
activities on which the operands are forced to synchronise, with ▷◁
∗denoting a synchronisation on all
common action types. In the model component S (x), the parameter x ∈N represents the initial number
of molecules S present. In addition to species and model components, a Bio-PEPA system consists of
kinetic rates, parameters and, if needed, locations, events and other auxiliary information for the species.
The formal representation oﬀered by Bio-PEPA allows for diﬀerent kinds of analysis through the
deﬁned mapping into continuous-deterministic and discrete-stochastic analysis methods (see [6] for de-
tails). More on Bio-PEPA can be found at [5], including two software tools, the Bio-PEPA Eclipse
Plug-in and the Bio-PEPA Workbench [10]. Both tools process Bio-PEPA models automatically and ei-
ther compute time-series results directly using various SSA or ODE solvers, or generate representations
that can be used by other tools.
3
The Ostreococcus clock
Ostreococcus tauri is an exceptionally small green alga with a highly reduced genome [9]. Experiments
and homology searches indicate that its circadian clock is very simple compared to higher plants, such
as Arabidopsis thaliana. Only a handful of the clock genes identiﬁed in other plants have been found in
Ostreococcus, and only two of these appear to be central to the clock. The ﬁrst of these, which we refer
to as TOC1, is homologous to Arabidopsis TOC1 (TIMING OF CAB EXPRESSION 1) and other PRRs
(PSEUDO RESPONSE REGULATORs). The other gene, here called LHY, is homologous to Arabidopsis
LHY (LATE ELONGATED HYPOCOTYL) and CCA1 (CIRCADIAN CLOCK ASSOCIATED 1) [8]. An
ODE model of the Ostreococcus clock as a negative feedback loop between these two genes was intro-
duced in [20], where it was applied to drug treatments and other perturbations. The full model includes
details of the luciferase assay used to measure mRNA and protein levels, but here we use only the cen-
tral parts of the model, which describe the dynamics of the native mRNAs and proteins. The model is
illustrated in Figure 1.
Figure 1: The genetic regulatory network underlying our model of the Ostreococcus clock. The network
comprises a single negative feedback loop involving the LHY and TOC1 genes, augmented by 5 light
inputs which synchronise the endogenous oscillations in gene expression to the day/night cycle [20].


## Page 4


4
Complementary approaches to understanding the plant circadian clock
TOC1 transcription requires light, which is buﬀered by a “light accumulator” (acc) and is inhibited
by the presence of nucleic LHY protein (LHY n) for most of the day. TOC1 activates LHY transcription
through an unknown mechanism, proposed in [20] to work as follows: TOC1 mRNA is translated into
inactive TOC1 protein (TOC1 i), which is activated slowly during the day but quickly after dusk. The
active form (TOC1 a) drives LHY transcription throughout the night but is quickly degraded after dawn.
LHY mRNA is translated into cytosolic LHY (LHY c), which is quickly translocated to the nucleus,
thereby closing the feedback loop. Light also accelerates the rate of LHY degradation.
The model parameters were estimated by ﬁtting simulated time-courses to equivalent data obtained
from experiments over a wide range of light conditions. Some experiments alternated 12 hours of light
and dark (denoted LD 12:12), others used longer or shorter days (such as LD 16:8 or 8:16), and many
included transitions between diﬀerent conditions, often into constant light (LL) [20].
3.1
A Bio-PEPA model of the clock
A model of the clock as described above was implemented in Bio-PEPA. Here we describe its main
features; for the full model, including kinetic laws and parameters, see Appendix A.
One of the key issues involved in obtaining a realistic stochastic model is the correct scaling of
the initial concentrations and kinetic parameters of the continuous ODE model in [20] so as to obtain
the respective molecule counts and rate constants for the Bio-PEPA discrete-state model. Since the
absolute values of the initial concentrations are not known, the initial values in the original ODE model
are given in arbitrary relative units. However, the peak number of TOC1 and LHY protein molecules
was estimated experimentally over a number of free-running cycles in LL conditions using a TopCount
luminometer. From this, approximate initial values for our discrete-state model were computed, yielding
a rough estimate for the scaling factor of Ω= 50. After such rescaling the Bio-PEPA model can be
analysed by ODEs and SSAs, which both give results in molecule counts.
The proteins and mRNAs shown in Figure 1 are modelled as the following Bio-PEPA species com-
ponents that describe the possible reactions they can participate in and how their amounts are aﬀected
by the occurrence of each reaction. Reactions are associated with functional rates representing the cor-
responding kinetic law.
TOC1 mRNA
def= transc3 ↑+ transl5 ⊕+deg7 ↓
LHY mRNA
def= transc8 ↑+ deg9 ↓+ transl10 ⊕
TOC1 i
def= transl5 ↑+ conv6 ↓
LHY c
def= transl10 ↑+ transp11 ↓+ deg12 ↓
TOC1 a
def= deg4 ↓+ conv6 ↑+ transc8 ⊕
LHY n
def= transc3 ⊖+transp11 ↑+ deg13 ↓
acc
def= prod1 ↑+ deg2 ↓+ transc3 ⊕
For instance, the transcription of TOC1 mRNA is modelled by reaction transc3, which involves three
diﬀerent species (TOC1 mRNA, LHY n, and acc), and is positively regulated by the light-accumulator
acc and negatively regulated by LHY n. The kinetic law for this reaction is given by a Hill function,
commonly used for describing transcription in clock models [1, 2, 13, 19]:
Ω·
tmp toc1 transcription
1+tmp toc1 transcription+
R toc1 lhy
Ω
·LHY n
H toc1 lhy .
Here, species names represent molecule counts, tmp toc1 transcription = L toc1 + acc · R toc1 acc/Ω
and L toc1, R toc1 acc, R toc1 lhy and H toc1 lhy are parameters. For comparisons with experiments
we also deﬁned the observables Total LHY = LHY c+LHY n and Total TOC1 = TOC1 i+TOC1 a.
Bio-PEPA functional rates allow the deﬁnition of general kinetic laws. We use this facility to rep-
resent the entrainment of the system to light/dark cycles through the time-dependent function below:


## Page 5


Akman, Guerriero, Loewe and Troein
5
light time = H

time−24·
time
24

−tdawn

·

tdusk −

time−24·
time
24

.
This allows us to model light-dependent reaction rates by returning the value 1 in day-time and 0 during
night-time. The parameters tdawn and tdusk give the time of the day (in hours) at which dawn and dusk
occur, respectively; H(x) is the Heaviside step function that returns 1 for x > 0 and 0 otherwise.
4
Analysis methods and results
Each technique that can be used to analyse Bio-PEPA models has its particular strengths: ordinary diﬀer-
ential equations (ODEs) easily predict mean values and quantify dynamical changes in terms of bifurca-
tions, stochastic simulation algorithms (SSAs) allow variability in the system’s responses to be measured,
and model-checking enables complex queries about the model to be formulated and veriﬁed automati-
cally. Here we analyse the clock model using these three analysis methods. After brieﬂy describing each
method, we explain why it is better suited for investigating a particular aspect of the system, and report
some of the results obtained.
4.1
Stochastic simulation: population versus single cell behaviour
Following the formulation of Gillespie’s stochastic simulation algorithm [12], the stochastic analysis of
biochemical systems has received increasing attention due to the impact that stochastic variability can
have on system behaviour. This is particularly relevant for systems such as gene regulatory networks,
where some molecules are present in copy numbers so small that random ﬂuctuations are too large for
the continuous approximation behind ODEs to be justiﬁed.
Within this framework, a single molecule-by-molecule stochastic simulation run can be viewed as
a faithful representation of behaviour at the cellular level (assuming the underlying model is accurate).
Observing the mean behaviour over a larger number of runs is then equivalent to observing a population
of cells. Most current experimental techniques only allow population-level assays. However, as progress
in high-resolution imaging techniques reduces the minimum population size that can be measured, it will
also become possible to consider the eﬀect of stochastic noise, which is expected to be more evident in
smaller populations.
In the rest of this section we report results obtained by solving the clock model using the Dormand–
Prince ODE solver and the Gibson–Bruck SSA, both available in the Bio-PEPA Eclipse Plug-in [5].
We consider three diﬀerent light conditions: constant dark (DD), constant light (LL), and alternating
light/dark cycles (LD). We also consider an experiment in which the system is transferred from constant
light into constant dark (LL-DD). For each of these, we compare results obtained by numerical inte-
gration of the deterministic model with those obtained by stochastic simulation. The initial conditions
are those of the original model at dawn following entrainment to 24 hour light/dark cycles (LD 12:12).
Figures 2 and 4 report the computed time-series behaviours for all settings.
The species of interest are TOC1 mRNA, LHY mRNA and the corresponding experimentally observ-
able total protein amounts (Total TOC1 and Total LHY as deﬁned in Section 3.1).
DD system.
The rapid damping behaviour of the system in constant dark (DD) is shown in Figure 2(a)–
2(c). This damping is seen in all analysis methods: ODEs, individual SSA runs, and the mean stochastic
behaviour calculated over 10000 independent SSA runs. Despite the fact that the self-sustained oscil-
lations observed by averaging over the SSA runs stop very quickly (within 1-2 days), when looking at


## Page 6


6
Complementary approaches to understanding the plant circadian clock
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(a) DD – ODE
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(b) DD – average 10000 SSA runs
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(c) DD – single SSA run
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(d) LL – ODE
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(e) LL – average 10000 SSA runs
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(f) LL – single SSA run
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(g) LL-DD – ODE
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(h) LL-DD – average 10000 SSA runs
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(i) LL-DD – single SSA run
Figure 2: Comparison of the deterministic and stochastic models in diﬀerent light conditions.
individual SSA runs we note that occasionally a non-zero number of molecules can be brieﬂy observed,
even after several circadian cycles (Figure 2(c)).
LL system.
In constant light (LL), the deterministic system also exhibits damped oscillations, with
all species tending to non-zero constant values after about 7-8 days (Figure 2(d)). Similar behaviour is
observed by averaging over 10000 SSA runs (Figure 2(e)), though the oscillations damp more rapidly and
the steady-state value is slightly diﬀerent (e.g. the LHY copy number is about 130 in ODEs compared
to about 160 in the SSA). However, a 10-fold increase of the scaling factor to Ω= 500 yields a perfect
quantitative agreement between the SSA and ODEs (see Figure 8 in Appendix C). Although the precise
source of the discrepancy is not known at present, we hypothesise that it is caused by a breakdown of the
continuous approximation underpinning ODEs, due to the low copy numbers obtained at small Ωvalues.
The other, most notable, diﬀerence between the deterministic and stochastic models is the behaviour
of individual SSA runs (Figure 2(f)), for which persistent irregular oscillations (in both phase and ampli-
tude) are observed. Because of phase diﬀusion eﬀects, however, these oscillations cannot be detected in


## Page 7


Akman, Guerriero, Loewe and Troein
7
the mean behaviour: hence, in this case, neither the simple average over multiple SSA runs nor the ODE
solution gives us a correct indication of the real behaviour of the system, emphasising the importance of
observing single realisations.
In view of these ﬁndings, we hypothesise that single cell experimental data may exhibit sustained
oscillations, whereas the behaviour observed in a large population of cells would be closer to the rapid
damping reproduced by both the ODE and SSA average. This is due to the fact that free-running oscilla-
tions are unlikely to be synchronised over diﬀerent cells. Furthermore, visual inspection of the solutions
obtained by averaging over diﬀerent numbers of SSA runs suggests that it should be possible to discern
the stochastic eﬀects with a population of around 100 cells. The experimental data currently available
for this system are at the level of a population comprising at least 10000 cells. However, we anticipate
that the development of new experimental techniques for measuring gene expression in single cells or
small populations will enable this hypothesis to tested experimentally in the not-too-distant future.
LL-DD system.
As an additional experiment, we consider a system which is kept in constant light
(LL) for 160 hours, and then transferred into constant dark (DD). The time-series results are reported
in Figures 2(g)–2(i). It can be seen that single realisations of the SSA — approximating the behaviour
of individual cells — exhibit immediate cessation of self-sustained oscillations following the LL-DD
transfer. This behaviour can be understood by considering the ﬁxed points of the deterministic model.
The LL ﬁxed point is located far from the origin in phase space and is of the stable focus type. Tra-
jectories of the ODE — approximating the behaviour of a large population of cells — spiral around the
ﬁxed point as they converge to it, producing slowly damping oscillations. In the corresponding stochas-
tic model, ﬂuctuations kick individual realisations of the system between these spiralling trajectories,
thereby preventing the system from remaining close to the ﬁxed point for long periods (see Figure 3).
This leads to the irregular self-sustained oscillations observed. By contrast, the DD ﬁxed point of the
ODE system is located at the origin. As species concentrations must be positive, the ﬁxed point cannot
be a stable focus, and is instead a stable node. Trajectories of the ODE converge directly onto it, gen-
erating oscillations that quickly damp to zero. Individual realisations of the stochastic model are thus
repeatedly perturbed between rapidly convergent trajectories. Consequently, they quickly approach the
DD steady-state following the LL-DD transition, remaining in its vicinity thereafter (see Figure 3).
The model thus predicts that the DD behaviour of the LL-DD system at the single-cell level mirrors
that at the population level. If further experiments were to reveal that self-sustained oscillations are
observed during the DD phase, this would indicate that the model requires modiﬁcation to convert the
DD ﬁxed point into a stable focus bounded away from the origin.
LD system.
The light conditions considered so far are experimental settings useful for observing the
system’s endogenous dynamics. It is also informative, however, to observe the behaviour of the clock
under natural conditions (alternating 24-hour cycles of light and dark). We present results obtained for
three diﬀerent photoperiods: 6 hours light/18 hours dark (LD 6:18), 12 hours light/12 hours dark (LD
12:12), and 18 hours light/6 hours dark (LD 18:6).
As described in Section 3, exposure to periodic external stimuli such as light/dark cycles has the
eﬀect of resetting the free-running oscillations observed in constant light, so as to establish stable phase
relationships with the forcing stimulus. Compared with the free-running LL system, the entrainment
to LD cycles regularises the dynamics of the system, markedly reducing the variability of oscillations,
particularly in terms of phase. As a consequence, persistent regular oscillations with a stable phase rela-
tionship to the light/dark cycle are observed in both ODEs (Figures 4(a), 4(d), 4(g)) and when averaging
over multiple SSA runs (Figures 4(b), 4(e), 4(h)). This phase regularisation can also be seen in indi-


## Page 8


8
Complementary approaches to understanding the plant circadian clock
0
20
40
60
80
100
120
140
160
180
0
50
100
150
200
250
300
350
Total LHY
Total TOC1
SSA-1
SSA-2
ODE
S
Figure 3: Phase-space for the LL-DD transfer experiment. White and grey dots indicate the ﬁxed points
(steady-states) of the deterministic system in LL and DD conditions, respectively. The eigenvalues of the
model obtained by linearising the deterministic equations around a ﬁxed point determine the behaviour
of the system in its neighbourhood. These are listed for both ﬁxed points in Table 2 of Appendix C.
vidual SSA runs of the entrained system (compare Figures 4(c), 4(f), 4(i)) with the simulations of the
free-running clock in Figure 2(f)). These observations are consistent with previous stochastic analyses
of clock models [13, 1]. We also note that, as for the LL system, the deterministic and mean stochastic
behaviour, whilst very similar, are not in perfect agreement.
4.2
Model-checking: time-dependent probability distributions
Model-checking [7] is a formal veriﬁcation method that allows modellers to state properties of a given
model and to automatically check whether they are met. Probabilistic model-checking (see, for instance,
[4, 15]) adds probabilistic measures in the evaluation of queries. Recently, model-checking has grown
in popularity within the ﬁeld of systems biology due to its ability to directly answer complex questions
on a model’s behaviour. Traditional model-checking veriﬁcation diﬀers from simulation-based analysis
in that the veriﬁcation of a property is obtained from a computation over the entire state-space of the
continuous-time Markov chain (CTMC) underlying the model. The major drawback of this approach is
the state-space explosion problem: the model’s dimension is often too large for computational viability.
Statistical model-checking (see, for instance, [21]) is an alternative query-based approach: it esti-
mates the probability distributions and computes approximate results of queries (together with an esti-
mate of the error) by generating random realisations of the CTMC and averaging the results obtained by
evaluating the queries on each of them. The advantage of statistical model-checking over exact veriﬁ-
cation approaches is that it does not need to build the explicit state-space of the model, which is often
intractable, and it does not rely on the transient solution of the CTMC. In essence, statistical model-
checking is a veriﬁcation technique which allows modellers to perform additional analyses of a stochas-
tic system by automatically evaluating queries over multiple simulation traces. The obvious drawback of
statistical model-checking is that it only considers a ﬁnite number of behaviours of the system (i.e. paths
in the CTMC) and, hence, the accuracy of the results is strongly related to that number. However, exact
veriﬁcation of biological systems is generally infeasible, and statistical model-checking often represents
a good practical solution. Another issue of probabilistic model-checking is that the transient solution of
the CTMC can incur the same averaging eﬀect discussed previously relating to ODEs and mean SSA be-
haviour: computing the expected value of the model variables might not be suﬃcient because this would
be exactly the same as the deterministic behaviour. Results of reward-based properties, for instance, are


## Page 9


Akman, Guerriero, Loewe and Troein
9
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(a) LD 6:18 – ODE
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(b) LD 6:18 – average 10000 SSA runs
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(c) LD 6:18 – single SSA run
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(d) LD 12:12 – ODE
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(e) LD 12:12 – average 10000 SSA runs
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(f) LD 12:12 – single SSA run
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(g) LD 18:6 – ODE
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(h) LD 18:6 – average 10000 SSA runs
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(i) LD 18:6 – single SSA run
Figure 4: Comparison of the deterministic and stochastic models for diﬀerent photoperiods.
computed in terms of expected values and this, especially in the case of oscillations which are out of
phase, does not give satisfactory results.
PRISM [15] is a probabilistic model-checker, which can be used to verify properties of a CTMC
model. It also includes a discrete-event simulator for statistical model-checking. PRISM has been used
to analyse systems from a wide range of application domains, and recently also biochemical systems [14].
Models are described using the state-based PRISM language, and it is possible to specify quantitative
properties of the system using a property speciﬁcation language which includes the temporal logic CSL
(Continuous Stochastic Logic) [3, 4].
Using the Bio-PEPA Workbench [5], we generated a PRISM model of the clock (together with a
set of reward structures and some standard CSL properties which are automatically generated). In the
PRISM model, one module is deﬁned for each species, and module local variables are used to record
the current quantity of each species. The transitions correspond to the activities of the Bio-PEPA model
and the updates take the stoichiometry into account. Transition rates are speciﬁed in an auxiliary module


## Page 10


10
Complementary approaches to understanding the plant circadian clock
which deﬁnes the functional rates corresponding to all the reactions. In order to have a ﬁnite CTMC,
lower and upper bounds are deﬁned for each variable. In the following, we focus on statistical model-
checking: in this case, the choice of the values for the bounds has no eﬀect on the performance of the
analysis (since the CTMC is not built) and so we can use arbitrarily high values that are guaranteed not
to be reached.
Modelling the light in PRISM.
In order to model the entrained clock (LD system), time-dependent
events must be represented. However, because of the intrinsic nature of model-checking algorithms,
which involve the numerical solution of the CTMC underlying stochastic models, deterministic events
and time-dependent functions cannot be explicitly speciﬁed in PRISM.
We investigated several approaches to address this problem. A ﬁrst possibility is to split the model-
checking algorithm into diﬀerent (two or more, depending on the time window we are interested in)
analysis steps over diﬀerent time intervals, each with constant light conditions: two diﬀerent CTMCs
would be considered (one for the day-time system and one for the night-time one) with the algorithm
switching back and forth between them. The main issue with this approach is how to merge the results
obtained over the diﬀerent time periods. For some particular queries, such as those relating to reachabil-
ity, this can be done by splitting them into a number of subqueries such that the result (i.e. probability
distributions) of one query can be used as the initial state for the next one. For an arbitrary CSL query,
however, this cannot be done, and this strongly limits the kind of queries that could be veriﬁed.
The alternative approach we consider here is to represent the light by approximating time using a
monotonically increasing stochastic variable. The main issue of this approach is that we introduce an
additional stochastic eﬀect which is absent in the system we have described so far (i.e. where light is
modelled as a deterministic on/oﬀswitch). In practice this does not matter, provided that the stochastic
variability introduced is kept smaller than the variability of any experiments the model may be compared
to. The introduction of an additional variable to model time also causes an increase in the state-space, but
this is not an issue here since we focus on statistical model-checking only. An extract from the PRISM
model showing how we model time and the day/night switch is provided in Appendix B.
Time-dependent probability distributions of protein levels.
Using model-checking we can compute
the time-dependent probability distributions for each of the model species. For instance, by verifying the
CSL property
P=?[F[T,T] (LHY c+LHY n = i)]
for time instant T ∈[0,96] and protein level i ∈[0,500], we can observe how the probability distribution
for LHY protein changes over time during the ﬁrst 96 hours of simulation.
Each of the plots in Figure 5 refers to a diﬀerent light condition (DD, LL, and LD 12:12), showing
how the probability of being at a particular level changes over time in each case. The plots also report
the mean value µ and the standard deviation σ of LHY expression. In all cases, the initial amount is
LHY = 200, and then the probability mass gradually moves away from this initial value. In DD, as
expected from the results of Section 4.1, the bulk of the probability mass rapidly moves close to zero.
In LL we can clearly observe the eﬀect of phase diﬀusion, resulting in a probability distribution spread
almost equally across a wide range of values. By contrast, in LD we are able to observe clear oscillations
in the probability distribution; we also note that the amplitude of peak expression is more variable than
that of trough expression, with a much broader spread of the probability mass around the mean.
In the following, we focus on the case of alternating light/dark cycles (LD 12:12). In Figure 6(a) we
report the probability distribution for LHY protein, together with its mean µ and standard deviation σ in


## Page 11


Akman, Guerriero, Loewe and Troein
11
Time
Total LHY level
 
 
0
6
12 18 24 30 36 42 48 54 60 66 72 78 84 90 96
0
50
100
150
200
250
300
350
400
450
500
0
0.005
0.01
0.015
0.02
0.025
0.03
(a) DD
Time
Total LHY level
 
 
0
6
12 18 24 30 36 42 48 54 60 66 72 78 84 90 96
0
50
100
150
200
250
300
350
400
450
500
0
0.005
0.01
0.015
0.02
0.025
0.03
(b) LL
Time
Total LHY level
 
 
0
6
12 18 24 30 36 42 48 54 60 66 72 78 84 90 96
0
50
100
150
200
250
300
350
400
450
500
0
0.005
0.01
0.015
0.02
0.025
0.03
(c) LD 12:12
Figure 5: Probability distribution of total LHY level over the ﬁrst 4 days (0–96 hours, 10000 runs).
The heatmap represents the probability distribution: a darker colour corresponds to a higher probability.
Blue lines show average and standard deviation (µ±σ). Similar changes in distribution with time were
obtained for TOC1 protein.
a single 24-hour cycle (from 120 to 144 hours). Figure 6(b) plots the oscillation in the corresponding
coeﬃcient of variation cv = σ
µ . This provides a normalised measure of the sensitivity of the LHY pro-
tein oscillation to stochastic ﬂuctuations as a function of circadian time. Small values of cv, therefore,
correspond to robust phase markers (a high signal-to-noise ratio) and large values poor phase markers (a
low-signal-to-noise ratio). Commonly used phase measures in circadian research are the times of peak
and trough expression together with the time at which the oscillation falls to its midpoint level. It can be
seen in Figure 6(b) that the coeﬃcient of variation is minimal around the peak, suggesting that the latter
is the best of the standard phase markers for analysing experimental LHY data.
As discussed in Section 4.1, for the DD system, both the deterministic solution and SSA average
quickly attain a constant value. Species amounts can, however, be greater than zero for short time
intervals in individual SSA runs (see Figure 2(c)). The following CSL property computes the probability
that the total LHY level remains in the range [0,e] between 96 and 500 hours.
P=?[G[96,500] (LHY c+ LHY n ≤0+e)]
e
0
2
4
6
8
10
12
14
16
18
20
P
0.8768
0.9276
0.9545
0.9737
0.9833
0.9903
0.9931
0.9964
0.9987
0.9993
0.9998
Table 1: Probability of total LHY to stay below the threshold e in DD (96–500 hours, 10000 runs).


## Page 12


12
Complementary approaches to understanding the plant circadian clock
Time
Total LHY level
 
 
0
2
4
6
8
10
12
14
16
18
20
22
24
0
50
100
150
200
250
300
350
400
450
500
0
0.005
0.01
0.015
0.02
(a) LHY – probability distribution and µ±σ
Time
Coefficient of variation
0
2
4
6
8
10
12
14
16
18
20
22
24
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
(b) LHY – coeﬃcient of variation cv = σ/µ
Figure 6: Probability distribution of LHY level over one day (120–144 hours) in LD 12:12 (10000 runs).
The distribution of TOC1 exhibits a qualitatively similar variation.
The results reported in Table 1 quantify the observed trend, showing that there is a small probability
that LHY exceeds e for 0 ≤e ≤20, and that this probability decreases with increasing e.
4.3
Distribution of Mutational Eﬀects: robustness analysis
Thus far we have investigated aspects of the inherent random noise caused by the small size of the system
and the discrete nature of its components. We have also explored the consequences of variations in the
light environment. We now consider the impact of mutational noise caused by DNA changes that alter
reaction rates by aﬀecting the structure of corresponding proteins. This analysis diﬀers from the above in
that it requires simulation of vast numbers of diﬀerent parameter combinations. We do this in the context
of a recently developed framework for evolutionary systems biology that describes how the eﬀects of
DNA changes propagate through various levels of organisation and abstraction until they impact ﬁtness
at the highest level of biological functionality [18]. We limit our analysis to what has been described as
the “third” level of the adaptive landscape [18], which maps a combination of biochemical reaction rates
to a computable system-level property likely to aﬀect ﬁtness via a quantitative mechanistic model.
We generated a StochKit [17] model using the Bio-PEPA Workbench [5] in order to build on the
code base of an analysis framework that has previously been used to investigate the evolutionary systems
biology of a diﬀerent, highly simpliﬁed circadian clock system that lacks entrainment [19]. We added a
class for computing phase in particularly noisy circadian clocks, using two thresholds to block stochastic
noise from generating artiﬁcially short ‘cycles’ with very low amplitude. Thresholds were set at 20% and
35% of the distance between the highest peak and lowest trough observed over 10 days, since minima
are less variable than maxima (see Figure 4(f)). We used the peak of total TOC1 as a phase marker since
our model checking results showed peaks to have higher signal/noise ratios (Figure 6(b)).
We consider the parameter combination used in the rest of the paper to be the wild-type and intro-
duce mutational noise by multiplying degradation rates of all mRNAs in the system (deg7 and deg9 in
Figure 1) by a uniformly distributed factor ([0.5,1.5], where 1.0 represents the wild-type). To diﬀeren-
tiate between internal stochastic noise and mutational noise we ran 40000 simulations in two sets, each
analysing 10000 time-courses for the wild-type and 10000 for mutants. In the ﬁrst set (Figure 7(a–c)),
the system size Ω= 50 corresponds to that of a single cell. The resulting noise is substantial as indi-
cated by the large width of the distribution of observed phase values (Figure 7(a)). In the second set of


## Page 13


Akman, Guerriero, Loewe and Troein
13
simulations (Figure 7(d–f)), we increased Ωa million fold. This results in an excellent approximation of
corresponding time-courses produced by ODEs; these simulations are thus denoted as ‘mean’ here. The
resulting internal stochastic noise is minimal (see the extremely narrow distribution in Figure 7(d)).
Our ‘mean’ results show how phase is aﬀected by mutational changes in the mRNA degradation rate
(Figure 7(d,e)). If the same mutational changes are introduced in the noisy single cell system, they are
much more diﬃcult to detect (see Figure 7(a,b)). As a diﬀerent way of visualising results, Figure 7(c,f)
plots the high-level consequences of mutations (phase) against their low-level eﬀect (the factor aﬀecting
mRNA degradation). The resulting graphs for the ‘mean’ system show clearly how a change in mRNA
degradation rate is expected to aﬀect the mean change in phase (Figure 7(f)). Figure 7(c) shows the
corresponding plot for single cell simulations. It demonstrates that a wave of TOC1 peaks starts around
the time of dusk (18h in these simulations) and continues for a few hours. The time at which the wave
starts is minimally aﬀected by the mutations we investigated, in stark contrast to the variance, which is
much lower for higher mRNA degradation rates. In other words, a lower rate of mRNA degradation leads
0
200
400
600
800
1000
High stochastic noise in 1 wildtype cell
Phase of peak of Total TOC1 [hour of day]
Counts
0
3
6
9
12
15
18
21
24
A
0
100
200
300
400
500
600
Low stochastic noise in mean wildtype
Phase of peak of Total TOC1 [hour of day]
Counts
0
3
6
9
12
15
18
21
24
D
0
200
400
600
800
1000
Mutational noise observed in 1 cell
Phase of peak of Total TOC1 [hour of day]
Counts
0
3
6
9
12
15
18
21
24
B
0
500
1000
1500
2000
2500
Mutational noise observed in mean
Phase of peak of Total TOC1 [hour of day]
Counts
0
3
6
9
12
15
18
21
24
E
0.6
0.8
1.0
1.2
1.4
Noise overview in 1 cell
Factor by which mRNA degradation is changed
Phase of peak of Total TOC1 [hour of day]
0
3
6
9
12
15
18
21
24
C
0.6
0.8
1.0
1.2
1.4
Noise overview in mean
Factor by which mRNA degradation is changed
Phase of peak of Total TOC1 [hour of day]
0
3
6
9
12
15
18
21
24
F
Figure 7: Robustness analysis showing how inherent stochastic noise and mutational noise aﬀect the peak
phase of total TOC1 in 4 sets of 10000 runs. Here, noise is measured by the width of the corresponding
distributions in phase values, where wider widths indicate greater noise. Plots (a–c) are dominated by the
high internal stochastic noise observed in single-cell simulations (Ω= 50). Plots (d–f) observe population
averages as computed with Ω= 50×106 and show virtually no internal stochastic noise. The ﬁrst column
(a,d) plots the behaviour of the wild-type, the second (b,e) adds mutational noise by changing the mRNA
degradation rate by a factor drawn from a uniform distribution [0.5,1.5], where 1.0 is the wild-type. The
third column (c,f) shows how phase depends on mutational eﬀects on mRNA degradation.


## Page 14


14
Complementary approaches to understanding the plant circadian clock
to greater internal stochastic noise. This increase in variance explains why the average phase is strongly
shifted towards later hours for smaller mRNA degradation rates in the ‘mean’ system (Figure 7(f)),
since the mean is strongly aﬀected by large values in skewed distributions as found in (Figure 7(c)).
Taken together, these results demonstrate that a higher mRNA degradation rate will on average move the
phase forward and make it more reliable (decrease the phase variance), whereas a decrease will move it
backwards and make it less reliable.
These subtle patterns in the mutational robustness of the clock could not have been uncovered with-
out running large numbers of simulations with varying parameter combinations. Such work requires a
diﬀerent infrastructure for data analysis from projects that analyse only a few parameter sets.
5
Conclusions
We have studied the circadian network of Ostreococcus tauri by developing a process algebra model of
the clock, based on an existing deterministic representation that was parameterised according to quanti-
tative experimental data. We have investigated several key aspects of the clock, such as the conditions
necessary for persistent oscillations in its constituent genes and proteins, as well as the eﬀect of diﬀer-
ent environmental and mutational changes on the phases of these oscillations. We used the Bio-PEPA
stochastic process algebra as a modelling language and applied a range of the analysis methods sup-
ported. Because of the low copy numbers of the molecular species involved in the clock network, we
focused on stochastic analysis methods which enable the system’s intrinsic variability to be observed.
In particular, we used stochastic simulation to explore how the clock responds to changes in the light
environment, and compared the results obtained against the behaviour of the corresponding deterministic
system. We predict that the qualitative behaviour of the free-running (LL) clock will be dependent on the
size of the cellular population; while damped oscillations will be observed in large populations (simulated
by the SSA average and the deterministic model), self-sustained oscillations may be detectable in single
cells (simulated by individual runs of the SSA). Model-checking was further used to investigate how the
variability of the clock’s behaviour changes over a circadian cycle. By computing the time-dependent
probability distributions of the clock proteins, we identiﬁed the time of peak expression as the most
robust phase marker, suggesting its use as an experimental measure.
Finally, we added mutational noise to our system by randomly changing the overall rate of mRNA
degradation and observing how this aﬀects the phase of the oscillations of a key clock protein, likely
to have an impact on ﬁtness. We found that the large amount of stochastic noise at the single cell level
makes it hard to observe functional changes that may be induced by mutations, without averaging over
many observations.
A number of the novel hypotheses we have formulated in this modelling study may provide new
biological insights into the behaviour of the Ostreococcus clock and will hopefully inspire subsequent
experimental research. In addition, further theoretical work can build on the novel model-checking re-
sults reported here, to explore additional ways in which systems biology models can be automatically
analysed using approaches based on concurrency theory. Our results demonstrate that the integration
of diﬀerent computational techniques is critical for fully quantifying the architectural [2] and muta-
tional [18] robustness of the circadian clock.
Acknowledgements
The authors thank Gerben van Ooijen for TopCount data and Jane Hillston and Andrew Millar for their
helpful comments. The Centre for Systems Biology at Edinburgh is a Centre for Integrative Systems Bi-


## Page 15


Akman, Guerriero, Loewe and Troein
15
ology (CISB) funded by BBSRC and EPSRC, ref. BB/D019621/1. CT is supported by The International
Human Frontier Science Program Organization.
References
[1] O.E. Akman, F. Ciocchetta, A. Degasperi & M.L. Guerriero (2009): Modelling Biological Clocks with
Bio-PEPA: Stochasticity and Robustness for the Neurospora Crassa Circadian Network.
In: Proc. of
CMSB’09, LNCS 5688, Springer, pp. 52–67.
[2] O.E. Akman, J.C.W. Locke, S. Tang, I. Carr´e, A.J. Millar & D.A. Rand (2008): Isoform switching facilitates
period control in the Neurospora crassa circadian clock. Mol. Sys. Biol. 4, p. 64.
[3] A. Aziz, K. Kanwal, V. Singhal & V. Brayton (1996): Verifying continuous time Markov chains. In: Proc. of
CAV’96, LNCS 1102, Springer, pp. 269–276.
[4] C. Baier, B. Haverkort, H. Hermann & J.-P. Katoen (2003): Model-Checking Algorithms for Continuous-Time
Markov Chains. IEEE Trans. on Software Eng. 29(6), pp. 524–541.
[5] Bio-PEPA Home Page. http://www.biopepa.org/.
[6] F. Ciocchetta & J. Hillston (2009): Bio-PEPA: a Framework for the Modelling and Analysis of Biological
Systems. Theoretical Computer Science 410(33-34), pp. 3065–3084.
[7] E.M. Clarke, O. Grumberg & D. Peled (1999): Model Checking. The MIT Press.
[8] F. Corellou, C. Schwartz, J.-P. Motta, E.B. Djouani-Tahri, F. Sanchez & F.-Y. Bouget (2009): Clocks in
the Green Lineage: Comparative Functional Analysis of the Circadian Architecture in the Picoeukaryote
Ostreococcus. Plant Cell 21, pp. 3436–3449.
[9] E. Derelle, C. Ferraz, S. Rombauts, P. Rouz´e, A.Z. Worden, Robbens S. et al. (2006): Genome analysis of the
smallest free-living eukaryote Ostreococcus tauri unveils many unique features. Proc. Natl. Acad. Sci. USA
103(31), p. 11647.
[10] A. Duguid, S. Gilmore, M.L. Guerriero, J. Hillston & L. Loewe (2009): Design and development of software
tools for Bio-PEPA. In: Proc. of WSC’09, pp. 956–967.
[11] J.C. Dunlap, J.J. Loros & P.J. DeCoursey (2004): Chronobiology: Biological Timekeeping. Sinauer.
[12] D.T. Gillespie (1977): Exact stochastic simulation of coupled chemical reactions. J. Phys. Chem. 81(25), pp.
2340–2361.
[13] D. Gonze, J. Halloy & A. Goldbeter (2002): Robustness of circadian rhythms with respect to molecular noise.
Proc. Natl. Acad. Sci. USA 99(2), pp. 673–678.
[14] J. Heath, M. Kwiatkowska, G. Norman, D. Parker & O. Tymchyshyn (2008): Probabilistic Model Checking
of Complex Biological Pathways. Theoretical Computer Science 319, pp. 239–257.
[15] A. Hinton, M. Kwiatkowska, G. Norman & D. Parker (2006): PRISM: A tool for automatic veriﬁcation of
probabilistic systems. In: Proc. of TACAS’06, LNCS 3920, pp. 441–444.
[16] M.A. Jones (2009): Entrainment of the Arabidopsis Circadian Clock. J. Plant Biology 52(3), pp. 202–209.
[17] H. Li, Y. Cao, L.R. Petzold & D.T. Gillespie (2008): Algorithms and Software for Stochastic Simulation of
Biochemical Reacting Systems. Biotechnology Progress 24(1), pp. 56–61.
[18] L. Loewe (2009): A framework for evolutionary systems biology. BMC Systems Biology 3(27).
[19] L. Loewe & J. Hillston (2008): The distribution of mutational eﬀects on ﬁtness in a simple circadian clock.
In: Proc. of CMSB’08, LNBI 5307, Springer, pp. 156–175.
[20] J.S. O’Neill, G. van Ooijen, C. Troein, L. Dixon, F.-Y. Bouget, F. Corellou & A. Millar (2009): Circadian
rhythms persisting in the absence of transcription in a eukaryote. Submitted.
[21] H.L.S. Younes & R.G. Simmons (2002): Probabilistic veriﬁcation of discrete event systems using acceptance
sampling. In: Proc. of CAV’02, LNCS 2404, Springer, pp. 223–235.


## Page 16


16
Complementary approaches to understanding the plant circadian clock
Appendix
A
The full Bio-PEPA model
Kinetic parameters:
acc rate
=
0.085759993119922787
R toc1 lhy
=
0.80473130211377397
H toc1 lhy
=
2.4786793492076216
L toc1
=
0.0001028030683282734
R toc1 acc
=
0.40030354494924164
D mrna toc1
=
0.33395900070057227
T toc1
=
0.65069237578254624
Di toc1 ia l
=
0.11696163098006726
Di toc1 ia d
=
0.34434576584349563
D toc1 a l
=
0.53999998111757508
D toc1 a d
=
0.3587344573844497
H lhy toc1
=
2.4123768479176113
R lhy toc1 a l
=
3.3859126401378155
R lhy toc1 a d
=
1.1074418532202324
D mrna lhy
=
1.9405472466939
T lhy
=
6.5204407183218498
Di lhy cn
=
7.0630744698933485
D lhy l
=
0.34866585983482207
D lhy d
=
0.21098655584281875
Time of the day at which dawn and dusk occur:
tdawn
=
6
tdusk
=
18
//
for the LD 12:12 system
Time-dependent function representing light in LD system:
light time = H

time−24·
time
24

−tdawn

·

tdusk −

time−24·
time
24

Scaling factor:
Ω
=
50
Initial values:
acc init
=
⌊0.99897249736755245·Ω⌋
TOC1 mRNA init
=
j
1.9315264449894309e−06 ·Ω
k
TOC1 i init
=
⌊0.34581773957827311·Ω⌋
TOC1 a init
=
⌊0.47960829226604956·Ω⌋
LHY mRNA init
=
j
9.9999999999999995e−07 ·Ω
k
LHY c init
=
⌊4.0361051173018776·Ω⌋
LHY n init
=
j
6.7029410613103796e−06 ·Ω
k
Additional functions:
tmp toc1 transcription
=
L toc1+acc· R toc1 acc
Ω
toc1 a decay
=
light time·D toc1 a l+(1−light time)·D toc1 a d
toc1 i a conversion
=
light time·Di toc1 ia l+(1−light time)·Di toc1 ia d
lhy decay
=
light time·D lhy l+(1−light time)·D lhy d
lhy toc1 reg
=
TOC1 a·

light time· R lhy toc1 a l
Ω
+(1−light time)· R lhy toc1 a d
Ω



## Page 17


Akman, Guerriero, Loewe and Troein
17
Functional Rates:
prod1
: acc rate·Ω·light time
// light accumulator increase: mass action
deg2
: acc rate·acc
// light accumulator decrease: mass action
transc3
: Ω·
tmp toc1 transcription
1+tmp toc1 transcription+
 R toc1 lhy
Ω
·LHY n
H toc1 lhy
// TOC1 transcription: Hill kinetics
deg4
: toc1 a decay·TOC1 a
// TOC1 degradation: mass action
transl5
: T toc1·TOC1 mRNA
// TOC1 translation: mass action
conv6
: TOC1 i a conversion·TOC1 i
// TOC1 conversion: mass action
deg7
: D mrna toc1·TOC1 mRNA
// TOC1 mRNA degradation: mass action
transc8
: Ω·
lhy toc1 regH lhy toc1
1+lhy toc1 regH lhy toc1
// LHY transcription: Hill kinetics
deg9
: D mrna lhy·LHY mRNA
// LHY mRNA degradation: mass action
transl10 : T lhy·LHY mRNA
// LHY translation: mass action
transp11 : Di lhy cn·LHY c
// LHY nuclear transport: mass action
deg12
: lhy decay·LHY c
// LHY degradation, cytosol: mass action
deg13
: lhy decay·LHY n
// LHY degradation, nucleus: mass action
Species components:
LHY c
def=
transl10 ↑+ transp11 ↓+ deg12 ↓
LHY mRNA
def=
transc8 ↑+ deg9 ↓+ transl10 ⊕
TOC1 a
def=
deg4 ↓+ conv6 ↑+ transc8 ⊕
TOC1 mRNA
def=
transc3 ↑+ transl5 ⊕+ deg7 ↓
acc
def=
prod1 ↑+ deg2 ↓+ transc3 ⊕
TOC1 i
def=
transl5 ↑+ conv6 ↓
LHY n
def=
transc3 ⊖+ transp11 ↑+ deg13 ↓
Species observables:
Total LHY
=
LHY c+LHY n
Total TOC1
=
TOC1 i+TOC1 a
Model component:
LHY c(LHY c init) ▷◁
∗LHY mRNA(LHY mRNA init) ▷◁
∗TOC1 a(TOC1 a init) ▷◁
∗
TOC1 mRNA(TOC1 mRNAinit) ▷◁
∗acc(acc init) ▷◁
∗TOC1 i(TOC1 i init) ▷◁
∗LHY n(LHY n init)


## Page 18


18
Complementary approaches to understanding the plant circadian clock
B
Modelling light/dark cycles in PRISM
const int max_days_simulated = 21;
module time
min : [0..59] init 0;
hour : [0..23] init 0;
day : [0..max_days_simulated] init 0;
light_time : [0..1] init 0;
[change_min] (min < 59) -> 60: (min’=min + 1);
[change_hour_dawn] (min = 59 & hour = (tdawn-1) ) -> 60: (min’=0) & (hour’ = hour + 1) & (light_time’ = 1);
[change_hour_dusk] (min = 59 & hour = (tdusk-1) ) -> 60: (min’=0) & (hour’ = hour + 1) & (light_time’ = 0);
[change_hour] (min = 59 & hour < 23 & hour != (tdawn-1) & (hour != tdusk-1) ) ->
60: (min’=0) & (hour’ = hour + 1);
[time_change_day] (min = 59 & hour = 23 & day < max_days_simulated) ->
60: (min’=0) & (hour’=0) & (day’ = day + 1);
[time_end_day] (min = 59 & hour = 23 & day = max_days_simulated) -> 60: (min’=0) & (hour’=0) & (day’=0);
endmodule
C
Additional simulation and analysis results
Figure 8 shows the comparison between the ODE results and the mean SSA behaviour with scaling fac-
tors Ω= 50 and Ω= 500. We observe a slight diﬀerence between the SSA results with the diﬀerent
scaling factors. The reference value is Ω= 50 (estimated from experimental protein counts), and con-
sequently the predicted biological behaviour is that shown in Figure 8(b). Note, instead, that the ODE
results (Figure 8(a)) agree perfectly with the SSA results for the larger value Ω= 500 (Figure 8(c)).
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(a) LL – ODE
0
50
100
150
200
250
0
100
200
300
400
500
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(b) LL – SSA Ω= 50
0
50
100
150
200
250
0
1000
2000
3000
4000
5000
Time (hours)
Level
 
 
 LHY mRNA
 TOC1 mRNA
Total LHY
Total TOC1
(c) LL – SSA Ω= 500
Figure 8: Comparison of deterministic and stochastic models for constant light (LL) with diﬀerent scaling
factors Ω.
Table 2 lists the eigenvalues of linearisation at the ﬁxed points of the deterministic model. These
determine the dynamics in the vicinity of the steady-states [1]. All eigenvalues of the DD ﬁxed point are
negative and real, identifying it as a stable node [1]. The LL ﬁxed point retains 3 of the DD eigenvalues;
the remaining ones comprise two complex conjugate pairs with negative real parts. The steady-state is
therefore a stable focus [1]. The positions of the ﬁxed points were estimated using the Nelder-Mead sim-
plex algorithm [2], as implemented in the MATLAB routine fminsearch. Derivatives were computed
analytically using the MATLAB Symbolic Math Toolbox.


## Page 19


Akman, Guerriero, Loewe and Troein
19
DD
LL
−0.0858
−0.0858
−0.2110
−0.0200−0.2509i
−0.3340
−0.0200+0.2509i
−0.3443
−0.6447−0.3216i
−0.3587
−0.6447+0.3216i
−1.9405
−1.9506
−7.2741
−7.4117
Table 2: Eigenvalues of the linearised ODE system about the DD and LL ﬁxed points.
References
[1] J. Guckenheimer & P. Holmes (1983): Nonlinear Oscillations, Dynamical Systems and Bifurcations of Vector
Fields. Springer.
[2] J.C.Lagarias, J. A. Reeds, M. H. Wright & P. E. Wright (1998): Convergence properties of the Nelder-Mead
simplex method in low dimensions. SIAM J. Optimiz. 9(1), pp. 112–147.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 1002_4661v1_complementary_approaches_to_understanding_the_plant_circadian_clock
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2010/1002_4661V1_COMPLEMENTARY_APPROACHES_TO_UNDERSTANDING_THE_PLANT_CIRCADIAN_CLOCK.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

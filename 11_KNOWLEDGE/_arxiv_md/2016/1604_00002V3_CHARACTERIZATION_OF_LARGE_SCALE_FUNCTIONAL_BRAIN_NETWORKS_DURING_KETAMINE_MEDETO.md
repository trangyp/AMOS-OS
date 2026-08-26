---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1604.00002v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1604.00002v3_Characterization_of_Large-Scale_Functional_Brain_Networks_During_Ketamine-Medeto

> Source: 1604.00002v3_Characterization_of_Large-Scale_Functional_Brain_Networks_During_Ketamine-Medeto.pdf

> Pages: 27

---


## Page 1


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
Characterization of Large-Scale
Functional Brain Networks During
Ketamine-Medetomidine Anesthetic
Induction
Eduardo C. Padovani *
Universidade de São Paulo
Abstract
Several experiments provide evidence that specialized brain regions functionally interact and reveal
that the brain processes and integrates information in a specific and structured manner. Networks
can be applied to model brain functional activities, providing means to characterize and quantify this
structured form of organization. Reports substantiate that different physiological states or diseases that
affect the central nervous system may be associated with alterations in these networks, which might
be reflected in graphs of different architectures. However, the relationship between their structure and
the organism’s distinct physiological conditions is poorly comprehended. Therefore, experiments that
estimate the functional neural networks of subjects exposed to different controlled conditions are highly
relevant. Within this context, this research has sought to model large-scale functional brain networks
during an anesthetic induction process. The experiment was based on intra-cranial recordings of the
neural activities of an old-world macaque of the species Macaca fuscata. Neural activity was recorded
during a Ketamine-Medetomidine anesthetic induction process, and networks were estimated sequentially
in five-second intervals. One and a half minutes after administering the anesthetics, changes occurred in
various network properties, revealing a transition in the network architecture. During general anesthesia,
functional connectivity and network integration capabilities were reduced at both local and global levels.
Additionally, it has been verified that the brain shifted to a highly specific and dynamic state. The
results provide empirical evidence and report the relationship between the induced state of anesthesia and
functional network properties, contributing to the elucidation of novel aspects of the neural correlates of
consciousness.
I.
Introduction
O
ne of the main goals of neuroscience is
to comprehend how the brain works by
understanding how cognitive abilities or phys-
iological states of the organisms are related
to neural processes involving functional inter-
actions of various brain structures. Although
neuroscience is a well-developed and consoli-
dated science, understanding has not yet been
reached at this level, and possibly the scien-
tific community will still need several years to
comprehend the brain to this extent. In recent
times, due to the influence of other fields of sci-
ence, such as the physics of complex systems,
allied with the constant realization that neural
activities involve the simultaneous participa-
tion of many distinct cortical areas, a new per-
spective has been gaining strength among the
community of neuroscientists. This perspective
aims to understand the brain as a whole from
a system point of view and considers as fun-
damental the comprehension of the way func-
tional interactions occur among distinct brain
structures to understand how the brain is able
to perform its activities (Bullmore and Sporns,
*Email: eduardo.padovani@alumni.usp.br
1
arXiv:1604.00002v3  [q-bio.NC]  4 Sep 2023


## Page 2


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
2009). Based on this perspective, researchers
have been using concepts and tools from the
Modern Network Science (Strogatz, 2001; New-
man, 2003) to model, characterize, and study
the brain.
The Modern Network Science is a highly in-
terdisciplinary field of science aimed at under-
standing the functioning, behavior, and evolu-
tion of complex systems, based on properties
of their structure, that is, the specific way in
which the elements of the system establish in-
teractions (Mitchell, 2009). One of the main
uses of complex networks in neuroscience is
the modeling of functional interactions estab-
lished among distinct cerebral regions by using
the mathematical structure of graphs. Assem-
bling those networks in which nodes represent
cortical areas and the edges functional inter-
actions (Friston et al., 1993; Friston, 1994) es-
tablished between these regions, several proce-
dures and analyses can be applied to evaluate
and study the properties of these networks. By
using complex networks measures (Rubinov
and Sporns, 2010), it is possible to estimate how
the connectivity is shaped, the organization at
local and global levels, the nodes that perform
great influence in the integration of several re-
gions, and the mediation of the information
flow (Bullmore and Sporns, 2009; Sporns, 2011;
Stam and Van Straaten, 2012). It is believed
that these networks reflect the specific ways
in which the processing and integration of in-
formation are performed among distinct brain
structures. There is also a consensus that differ-
ent cognitive demands or disorders that affect
the central nervous system may be associated
with specific network configurations (Stam and
Reijneveld, 2007; Sporns, 2011).
General Anesthesia
Understanding general anesthesia is highly
relevant to both medicine and neuroscience.
Given its importance and the fact that gen-
eral anesthesia’s underlying mechanisms are
not well understood, the Science Magazine has
pointed out the elucidation of processes and
mechanisms involving general anesthesia as
one of the 125 most important open questions
in science (Kennedy and Norman, 2005).
Anesthetic agents are small molecules that
can interact with and modulate the activity of
specific ionic channel proteins in neurons, pro-
moting dramatic physiological alterations in
the organism. General anesthesia is a drug-
induced physiologically stable and reversible
state characterized by analgesia, amnesia, im-
mobility, and loss of consciousness (Schwartz
et al., 2010). The anesthetic drug’s pharma-
cological effects are reasonably known and
described. However, the neurophysiological
mechanisms that underlie sedation and loss
of consciousness are not yet well understood
(Schwartz et al., 2010; Lewis et al., 2012). Be-
sides their undeniable importance and useful-
ness in clinical medicine, these drugs can also
constitute tools of great value to neuroscience.
As anesthetic agents are able to induce dif-
ferent levels of consciousness in a stable and
reproductive manner (Uhrig et al., 2014). They
can be used as experimental tools, providing
means for the study of consciousness and the
neural correlates of consciousness, thus offer-
ing possibilities to investigate fundamental pro-
cesses and phenomena that occur in the brain
(Hameroff et al., 1998).
There are several theories about anesthesia
(Flohr, 1995; Alkire et al., 2000; Mashour, 2004;
John and Prichep, 2005), as well as theories of
consciousness based on the interface between
consciousness and anesthesia (Hameroff, 2006;
Mashour, 2006).
There are also several hy-
potheses and reports on how anesthetic agents
lead to the loss of consciousness, based on
the depression of cerebral functions (Alkire
et al., 1995; Alkire, 1998), on the reduction of
functional interactions between brain areas
(White and Alkire, 2003; Imas et al., 2005), on
the fragmentation of neural networks (Lewis
et al., 2012), and others.
Within this context of several theories, hy-
potheses, and reports, the present study sought
to investigate the alterations in the organiza-
tion of functional brain activities that occur
at the onset of the anesthetic induction by us-
ing concepts and tools of the Modern Network
Science. In order to perform those analyses,
macaque’s functional brain networks were esti-
2


## Page 3


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
mated serially over time during an anesthetic
induction process. Complex network measures
were employed to characterize and compare
the graphs estimated at different instants of
time throughout the experiment.
II.
Methods
Database
In order to study the effects induced by gen-
eral anesthesia in the functional brain networks,
we have analyzed an ECoG electrophysiolog-
ical records database provided by the Adap-
tive Intelligence laboratory at the RIKEN Brain
Science Institute, Saitama, Japan.
The
database was respective to an experiment in-
volving a Ketamine-Medetomidine anesthetic in-
duction in a non-human primate animal model
subject of the species Macaca fuscata, who
had an MDR-ECoG matrix chronically im-
planted in the subdural space extensively cov-
ering the left brain hemisphere’s lateral cor-
tical surface and also the frontal and occipi-
tal medial walls (Nagasaka et al., 2011). The
database is available in the public domain at
(http://neurotycho.org). For further infor-
mation see (Nagasaka et al., 2011).
Recording Technique
The Multidimensional Recording Electrocor-
ticogram (MDR-ECoG) is considered the most
advanced and balanced technology to record
cortical electrophysiological activity (Yanagawa
et al., 2013). It can sample neural signals at
temporal resolutions higher than 1KHz, and
a spatial resolution of up to 3mm, offering
concomitantly high spatial and temporal res-
olution. Furthermore, once the electrodes are
positioned right over the cortex, beneath the
dura mater, the MDR-ECoG is also regarded to
provide reliable records of cortical electrophys-
iological activity along with low levels of noise
(Yanagawa et al., 2013; Fukushima et al., 2014).
Animal Model Subject
Experimentally, an old-world monkey of the
species Macaca fuscata was used as an animal
model. This species of macaque has consider-
able anatomical and evolutionary similarities
with humans, making them an excellent plat-
form for the study of the human brain (Iriki
and Sakura, 2008).
Anesthetic Agents
The neural records database is respective
to an experiment that involved a Ketamine
and Medetomidine anesthetic induction in a
macaque subject.
Ketamine is a drug that induces an anes-
thetic state characterized by the dissocia-
tion between the thalamocortical and lim-
bic systems (Bergman, 1999).
It acts as
a non-competitive antagonist of the recep-
tor N-methyl-D-aspartate (Green et al., 2011).
Medetomidine (an agonist of the alpha-2 adren-
ergic receptor) was combined with Ketamine
to promote muscular relaxation (Young et al.,
1999). The antagonist of Medetomidine, Ati-
pamezole, was used to trigger and promote the
recovery process (Young et al., 1999).
Neural Connectivity Estimator
As a neural connectivity estimator, a method-
ology based on Granger causality in the fre-
quency domain (Granger, 1969; Seth and Edel-
man, 2007) was used to infer the statistical de-
pendencies between the time series of the elec-
trodes. When applied in neuroscience, Granger
causality provides an estimate of the informa-
tion flow from one cortical area to another
(Seth and Edelman, 2007; Seth, 2010).
Experimental Procedures - Summary of Steps
The modeling of functional neural activities
performed in this study followed these steps:
1. The database is respective to neural reg-
isters recorded by the MDR-ECoG tech-
nique. The matrix of ECoG electrodes
continuously covered the entire left brain
hemisphere and parts of the cortical me-
dial walls.
3


## Page 4


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
2. Each electrode of the ECoG array was
considered a vertex of the network and
represented the respective cortical area in
which it was positioned.
3. A
neural
connectivity
estimator
of
Granger causality in the frequency do-
main was used to estimate the association
values between the electrodes registers
(time series).
4. An adjacency matrix was assembled, con-
taining all the pairwise association values
between the nodes.
5. The characterization of the topology of
the estimated networks was performed
using complex network measures.
Networks were estimated sequentially at
five-second intervals in five physiological fre-
quency bands throughout the experiment. In
each frequency band, all the networks in the
sequence were obtained using the same pro-
cedures and parameters. Thus, the alterations
observed in the properties of distinct networks
over the course of the experiment came only
from the differences in the records of neural
activity.
I.
Database - Anesthetic Induction Ex-
perimental Procedures
The database was recorded during an exper-
iment conducted according to the following
experimental procedures:
The monkey was seated in a proper chair
with its head and arms restrained. The neu-
ral activity started to be recorded while the
monkey was awake and with open eyes. Af-
ter that, the eyes were covered with a patch to
prevent visual evoked responses. After about
10 minutes, a Ketamine-Medetomidine cock-
tail (5.6mg/Kg of Ketamine + 0.01mg/Kg of
Medetomidine) was injected intramuscularly
to induce anesthesia. The loss of consciousness
point (LOC) was set at the time when the mon-
key no longer responded to external stimuli
(touching the nostrils or opening the hands).
After establishing the LOC, neural activity was
recorded for about 25-30 minutes. Heart rate
and breathing were monitored throughout the
entire experiment. For further information, see
(http://neurotycho.org).
II.
Signal Processing and Granger
Causality in the Frequency Domain
Data Processing
1. A reject-band IIR-notch filter was used
to attenuate components of the signal at
50Hz.
2. The signal was down-sampled from
1KHz to 200Hz.
3. The signal was divided into windows of
1000 points (equivalent to a five-second
recording of neural activity).
4. For each of the 128-time series, the trend
was removed, and the average was sub-
tracted.
5. To verify the stationary condition of the
time series, the KPSS (Kwiatkowski et al.,
1992) and the ADF [Augmented Dickey
Fuller] (Hamilton, 1989) tests were ap-
plied.
Libraries Used
For the computation of association values us-
ing Granger causality in the frequency domain,
were used with some adaptations the follow-
ing libraries: MVGC GRANGER TOOLBOX, devel-
oped by Ph.D. Anil Seth (Sussex University,
UK), described in (Seth, 2010), available at
www.anilseth.com, and the BSMART toolbox
(Brain-System for Multivariate AutoRegressive
Timeseries toolbox) described in (Cui et al.,
2008) and available at www.brain-smart.org.
4


## Page 5


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
Computation of Causal Interactions
1. Model Order:
To find the model order (number of ob-
servations to be used in the regression
model), the model’s selection criteria
from Akaike (AIC) and Bayes/Schwartz
(BIC) were used. Both methods returned
the order of the model equal to seven.
2. Causal Interactions
At each window of 1000 points, Granger
causality in the frequency domain in-
teractions
were
pair-wise
computed
among the 128-time series by the use
of the function cca_pwcausal() (MVGC
GRANGER TOOLBOX).
3. Frequency Bands
Granger causality interactions were cal-
culated in five physiological frequency
bands:
Delta (0-4Hz), Theta (4-8Hz),
Alpha (8-12Hz), Beta (13-30Hz), and
Gamma (25-100Hz).
The interaction values obtained were
saved in adjacency matrices.
Graphs and Networks
1. Assemble Networks
For each sequence of graphs respective
to a frequency band, a threshold was cho-
sen, and only the interactions with mag-
nitude values higher than this threshold
were considered edges of the graphs.
• Delta (0-4Hz), threshold = 0.8
• Theta (4-8Hz), threshold = 0.5
• Alpha (8-12Hz), threshold = 0.5
• Beta (13-30Hz), threshold = 1.0
• Gamma (25-100Hz), threshold = 2.5
As discussed in (Bullmore and Sporns,
2009; Sporns, 2011), scientists can rely
on various criteria to determine this pa-
rameter. In the present study, due to ex-
perimental conditions, each sequence of
networks contained graphs with distinct
connectivity. Thresholds were selected
in such a way as to prevent graphs with
lower connectivity in each sequence from
presenting many disconnected parts or
vertices, which could potentially intro-
duce distortions in the analysis.
After obtaining non-weighted graphs, the
directions of the edges were removed, re-
sulting in undirected and non-weighted
networks.
2. Analysis of Topology
Network measures (Rubinov and Sporns,
2010) were used to characterize the
graph’s topology.
III.
Results
Alterations in the topology of the functional
brain networks were observed along the anes-
thetic induction process, verifying the occur-
rence of changes over the distinct measures
used to characterize the networks. Those re-
sults reveal differences in how cortical areas
functionally interact regarding awake condi-
tions and the induced state of anesthesia.
About one and a half minutes after admin-
istering the anesthetic cocktail, abrupt changes
were observed over several network proper-
ties, revealing the existence of a rapid transi-
tion between the two states (awake and anes-
thetized). Alterations were also observed after
the macaque was blindfolded, demonstrating
that different stimuli presented to the animal
were able to promote changes in its functional
neural network structure.
I.
Average Degree
Significant alterations in the network’s average
degree were observed on the five frequency
bands analyzed during the experiment (see
Figure · 1; Table · 1).
Regarding the transition between resting
state with eyes open and blindfolded condi-
tions, changes in the network’s average connec-
tivity were noted in some frequency bands (see
5


## Page 6


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
Figure · 1). After placing a patch over the eyes,
the average degree presented a tendency to
increase and also to display a higher variation.
Noticeable changes in the average degree
of the graphs were also observed in the tran-
sitional period between the awake and anes-
thetized states (see Figure · 1); the average de-
gree presented a considerable reduction and
was less prone to variation.
Under general
anesthesia conditions, the graphs assumed a
tendency to possess the same connectivity over
time.
(A) Delta 0-4Hz
(B) Theta 4-8Hz
(C) Alpha 8-12Hz
(D) Beta 13-30Hz
(E) Gamma 25-100Hz
Figure 1: Average Degree Vertex. Vertical axis average degree; Horizontal axis time (minutes). At t=11 minutes, the
monkey was blindfolded; the first vertical red line represents this event in each sub-figure. At t=23 minutes,
the Ketamine-Medetomidine cocktail was injected, represented by the second vertical red line. Finally, the
point of loss of consciousness (LOC) was registered at t=33 minutes, indicated by the third vertical red line.
Low Frequencies (0-4Hz)
After the placement of the blindfold, the aver-
age degree respective to the Delta frequency
band assumed a higher variation and approxi-
mately doubled in mean values (see Figure · 1,
Sub-Figure A; Table · 1). After administering
the anesthetics, the degree of the graphs dimin-
ished and remained approximately constant
for about four minutes. Later, an increase and
a higher variation that lasted around 10 min-
utes were observed. After that time, the aver-
age degree fell again, keeping approximately
constant until the end of the experiment. The
networks respective to the awake (blindfolded)
and anesthetized states had approximately the
same mean connectivity (see Table · 1).
6


## Page 7


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
Table 1: Mean, variance (Var), and standard deviation (SD) of the average degree on the five physiological frequency
bands analyzed and on the three different conditions in which the monkey was exposed during the experiment:
awake with eyes open, awake with eyes closed and anesthesia (eyes closed).
Average Degree
Eyes Open
Eyes Closed
Anesthesia
Frequency Band
Mean
Var
SD
Mean
Var
SD
Mean
Var
SD
Delta (0-4Hz)
9.25
30.3
5.50
17.4
251
15.8
17.8
121
11.0
Theta (4-8Hz)
11.9
28.6
5.35
29.3
231
15.2
9.67
16.0
4.00
Alpha (8-12Hz)
10.6
26.1
5.11
26.7
189
13.7
3.21
1.64
1.28
Beta (13-30Hz)
23.6
83.2
9.12
28.0
152
12.3
4.47
5.00
2.23
Gamma (25-100Hz)
8.29
43.4
6.59
11.2
163
12.8
7.64
4.13
2.03
Medium Frequencies (4-30Hz)
The average degree on the Theta and Alpha
bands had increased significantly after the
placement of the blindfold, having assumed
a higher variation and approximately tripled
in mean values (see Table · 1). In the Beta band,
a similar dynamic behavior was also observed.
In this frequency band, the graph’s average
connectivity increased by the order of 20% due
to the placement of the blindfold (see Table · 1).
After administering the anesthetics, the
Theta,
Alpha,
and Beta bands presented
a
considerable
reduction
in
the
average
degree compared to the time when the
macaque was awake (blindfolded) (see Figure ·
1, Sub-Figures B, C, and D), the average de-
gree was reduced about three times in Theta,
eight times in Alpha, and six times in the Beta
band (see Table · 1). Under those experimental
conditions, the variation of the graph’s con-
nectivity had diminished, and the networks
assumed a quite constant degree along with
the anesthetized state.
High Frequencies (25-100Hz)
Between 25 and 100Hz, after covering the eyes
of the monkey, the average degree increased
in the order of 35%. The connectivity of the
networks assumed a higher variation, resulting
in a two-fold increase in the standard devia-
tion compared to the time when the macaque
eyes were open (see Table · 1). After administer-
ing the anesthetics, the variation of the values
decreased, and the average connectivity was
reduced by approximately 30% compared to
the time when the macaque was awake (eyes
closed) (see Table · 1).
II.
Correspondence Between Vertices
Degree and Cortical Areas
Through the use of a color gradient, it was pos-
sible to verify the relationship between the de-
gree of the vertices of the functional networks
and their corresponding cortical anatomical ar-
eas. It was noted that most of the nodes that
were physically closer to each other tended to
present a similar degree, as they reflected in
a similar color. However, it was also noticed
that not all nodes had the same degree. The
observed differences appeared to be related to
anatomical areas and divisions (see Figure · 2).
By analyzing the networks estimated se-
rially over time, it was possible to observe
changes among the patterns from one network
to another, revealing that the connectivity of
the vertices is dynamic. Besides the existence of
some changes in consecutive (time) networks,
two evident distinguishable patterns were ob-
served along with the experiment. The first
corresponds with the period when the mon-
key was awake, and the second pattern was
observed when the macaque was anesthetized.
7


## Page 8


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
II.1
Pattern of the Awake State
The presence of high-degree nodes over the
frontal and parietal lobes characterized the pat-
tern observed in the awake state (see Figure · 2,
Sub-Figures A - E). Highly connected nodes
were also observed, with a considerable likeli-
hood on the medial frontal wall and anterior
parts of the temporal lobe. It was also noted
that there were areas where the degree of the
vertices was relatively lower. Those areas en-
compassed mainly the occipital lobe, medial
occipital walls, and medial-posterior temporal
lobe areas.
II.2
Pattern of the Anesthetized State
The absence of high-degree nodes over the
entire network characterized the pattern ob-
served during the anesthesia-induced state. De-
spite the overall decrease in functional connec-
tivity, at certain moments, some regions pre-
sented vertices with a higher degree. Those
events of connectivity rise were mainly lo-
cated in the occipital lobe and sometimes in
the frontal and parietal areas (see Figure · 2,
Sub-Figures P - T).
Transition
About one and a half minutes after the injec-
tion of the Ketamine-Medetomidine cocktail,
an abrupt change in the degree of the ver-
tices was observed, revealing a new and dis-
tinct pattern that persisted while the macaque
was anesthetized.
The transition between
the two patterns occurred rapidly. From the
observation of (Figure · 2), it is possible to
note that the transition took approximately
20-25 seconds (4-5 networks) (see Figure · 2,
Sub-Figures I - O).
III.
Average Degree - Cortical Lobes
Aimed at observing and comparing the alter-
ations that occurred due to the anesthetic in-
duction in each of the four cortical lobes, net-
works respective to each lobe were assembled
(corresponding to subgraphs of the whole net-
work).
Table 2: Mean, variance (Var), and standard deviation (SD) of the average degree of the complete graph (128 nodes),
and the sub-graphs respective to each one of the four cortical lobes, on the frequency band Alpha (8-12Hz), on
the three different conditions in which the monkey was exposed during the experiment: awake with eyes open,
awake with eyes closed and anesthesia (eyes closed).
Average Degree
Eyes Open
Eyes Closed
Anesthesia
Corresponding Graph
Mean
Var
SD
Mean
Var
SD
Mean
Var
SD
Complete Graph
10.6
26.1
5.11
26.7
189
13.75
3.20
1.64
1.28
Subgraph Frontal Lobe
9.80
44.3
6.65
18.0
112
10.6
1.00
0.24
0.49
Subgraph Parietal Lobe
3.46
4.41
2.10
6.82
10.1
3.17
0.65
0.32
0.56
Subgraph Temporal Lobe
3.75
3.57
1.89
7.52
7.00
2.65
1.72
0.51
0.71
Subgraph Occipital Lobe
2.17
1.96
1.40
4.80
12.4
3.52
6.34
10.7
3.27
Significant alterations in the average de-
gree at each one of the four brain lobes an-
alyzed were verified over the experiment (see
Figure · 3; Table · 2). The frontal, parietal, and
temporal regions presented quite similar dy-
namic behavior. In those regions, the mean
connectivity degree increased and presented a
higher variation after placing a blindfold over
8


## Page 9


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
Figure 2: Vertices Degree. The transition between the awake and anesthetized states. Frequency band Alpha (8-12Hz).
On each sub-figure, the vertex degree is indicated by a color gradient over the respective coordinates of each
electrode. The sub-figures correspond to the degree of the vertices estimated sequentially over time, 5 seconds
being the time interval between each frame and the subsequent one. The frame A starts approximately one
minute after administering the anesthetics.
the eyes.
A minute and a half after the in-
jection of the anesthetic cocktail, an expres-
sive decrease in the connectivity was noted
(see Figure · 3, Sub-Figures A, B, and C). The
average degree was reduced 18 times in the
subgraphs of the frontal region, 10 times in
the parietal lobe, and four times in temporal
areas; in comparison to the awake state (blind-
folded) (see Table · 2). In addition, a substantial
decrease in the variation of the average de-
gree on those cortical lobes was also observed,
as the connectivity remained relatively con-
stant during general anesthesia (see Figure · 3,
Sub-Figures A, B, and C).
9


## Page 10


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
(A) Frontal Lobe
(B) Parietal Lobe
(C) Temporal Lobe
(D) Occipital Lobe
Figure 3: Average Degree Vertex. Vertical axis average degree in Alpha frequency band (8-12Hz); Horizontal axis
time (minutes). At t=11 minutes, the monkey was blindfolded. The first two vertical red lines in each
sub-figure represent the event of placing a patch over the eyes. At t=23 minutes, the third vertical red line
represents the Ketamine-Medetomidine cocktail injection event. The point of loss of consciousness (LOC) was
registered at t=33 minutes, indicated by the fourth vertical red line.
A distinct dynamic behavior in response
to the experimental conditions was observed
on the sub-graphs respective to the occipital
lobe. After covering the eyes of the monkey,
the average degree of the sub-graphs almost
doubled and also presented a higher variation
(see Figure · 3, Sub-Figure D). After adminis-
tering the anesthetics, a decrease in the mean
connectivity lasting about seven minutes was
verified. Then, the mean connectivity increased
and showed a higher variation (see Figure · 3,
Sub-Figure D).
IV.
Average Path Length
Noticeable changes in values of average path
length were observed during the anesthetic
induction process (see Figure · 4; Table · 2).
Considering the effects of blindfolding the
monkey, a subtle decrease in the average path
length occurred. However, it was also possible
to note that under this experimental condition,
there was a tendency for the graphs to present
quite the same values, keeping the average path
length almost constant, except for short periods
when higher values were observed.
Regarding the transition between the awake
(blindfolded) and the anesthetized states, the
anesthetic induction led to an expressive in-
crease in the average path length of the net-
works.
A higher variation of this property
was verified during general anesthesia (see
Figure · 4, Sub-Figures B - E).
Low Frequencies (0-4Hz)
In the Delta band, no substantial changes in the
average path length were observed along with
the experiment (see Figure · 4, Sub-Figure A).
Compared to when the monkey had its eyes
open, blindfolding the macaque has led to a
decrease in the order of 15% in the average
path length. After administering the anesthet-
ics, a decrease in the order of 5% was observed
compared to the awake state (blindfolded) (see
Table · 3).
10


## Page 11


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
(A) Delta 0-4Hz
(B) Theta 4-8Hz
(C) Alpha 8-12Hz
(D) Beta 13-30Hz
(E) Gamma 25-100Hz
Figure 4: Average Path Length. Vertical axis average path length; Horizontal axis time (minutes). At t=11 minutes,
the monkey was blindfolded; the first vertical red line represents this event in each sub-figure. At t=23
minutes, the Ketamine-Medetomidine cocktail was injected, represented by the second vertical red line.
Finally, the point of loss of consciousness (LOC) was registered at t=33 minutes, indicated by the third
vertical red line.
Medium Frequencies (4-30Hz)
On medium frequencies, the act of blindfold-
ing the macaque led to a slight decrease in
the average path length of the networks. Sim-
ilar behavior occurred in the Theta, Alpha,
and Beta bands during the anesthetic induc-
tion. A minute and a half after administering
the Ketamine and Medetomidine cocktail, a
substantial increase in the average path length
in the order of 45% in Theta and 50% in Al-
pha and Beta occurred (see Table · 3; Figure · 4,
Sub-Figures B - D). A higher variation in the
average path length was also observed when
the monkey was anesthetized.
High Frequencies (25-100Hz)
On the Gamma frequency band, putting a
patch over the eyes of the macaque has led
to a higher variation in the average path length
of the networks.
After the anesthetic injec-
tion, the average path length increased. Four
minutes later, some reduction was observed in
the values. A decrease in the variation over
time of the average path length was also veri-
fied during general anesthesia (see Figure · 4,
Sub-Figure E).
11


## Page 12


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
Table 3: Mean, variance (Var), and standard deviation (SD) of the average path length on the five physiological
frequency bands analyzed and on the three different conditions in which the monkey was exposed during the
experiment: awake with eyes open, awake with eyes closed and anesthesia (eyes closed).
Average Path
Eyes Open
Eyes Closed
Anesthesia
Frequency Band
Mean
Var
SD
Mean
Var
SD
Mean
Var
SD
Delta (0-4Hz)
3.11
0.73
0.85
2.67
0.56
0.75
2.50
0.21
0.46
Theta (4-8Hz)
2.87
0.50
0.71
2.20
0.54
0.73
3.16
0.30
0.55
Alpha (8-12Hz)
3.03
0.46
0.68
2.31
0.64
0.80
3.51
0.63
0.79
Beta (13-30Hz)
2.37
0.37
0.61
2.25
0.40
0.63
3.34
0.56
0.75
Gamma (25-100Hz)
2.94
0.48
0.69
2.91
0.81
0.90
3.16
0.17
0.41
V.
Diameter
Changes in the diameter of the networks
were observed along with the experiment (see
Figure · 5; Table · 4).
The diameter of the graphs respective to the
Delta band presented a distinct dynamic be-
havior compared to the other frequency bands.
From 0 to 4Hz, the anesthetic induction re-
duced and decreased the diameter variation
(see Figure · 5, Sub-Figure A).
Table 4: Mean, variance (Var), and standard deviation (SD) of the diameter on the five physiological frequency bands
analyzed and on the three different conditions in which the monkey was exposed during the experiment: awake
with eyes open, awake with eyes closed, and anesthesia (eyes closed).
Diameter
Eyes Open
Eyes Closed
Anesthesia
Frequency Band
Mean
Var
SD
Mean
Var
SD
Mean
Var
SD
Delta (0-4Hz)
7.77
7.15
2.67
6.70
5.36
2.31
6,02
2.12
1.46
Theta (4-8Hz)
7.05
4.27
2.07
5.36
6.62
2.57
8.28
3.77
1.94
Alpha (8-12Hz)
7.86
5.03
2.24
5.67
6.83
2.61
8.25
6.21
2.49
Beta (13-30Hz)
5.76
4.16
2.04
5.42
4.19
2.05
8.90
5.38
2.31
Gamma (25-100Hz)
7.80
5.44
2.33
7.60
10.10
3.18
8.00
3.10
1.76
Similar behavior was observed on the Theta,
Alpha, Beta, and Gamma bands. After blind-
folding the macaque, the diameter length sub-
tly decreased, and a slight increase in the vari-
ation amplitude of the values was noted. One
minute after the anesthetic cocktail adminis-
tration, the graph’s diameters increased sub-
stantially, staying this way until the end of the
experiment (see Figure · 5, Sub-Figures B - E).
VI.
Average Betweenness Centrality
Degree
On all frequency bands analyzed, no significant
changes in the average betweenness centrality
degree of the vertices occurred after blindfold-
ing the monkey (see Figure · 6). Nonetheless,
the administration of the anesthetics promoted
changes in this property of the networks.
In the Delta band, administering the anes-
thetics decreased the vertex’s average between-
ness centrality degree, which lasted for about
15 minutes. Then, the values started increasing
up to the recording section’s end (see Figure · 6,
Sub-Figure A).
12


## Page 13


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
(A) Delta 0-4Hz
(B) Theta 4-8Hz
(C) Alpha 8-12Hz
(D) Beta 13-30Hz
(E) Gamma 25-100Hz
Figure 5: Diameter. Vertical axis diameter; Horizontal axis time (minutes). At t=11 minutes, the monkey was
blindfolded; the first vertical red line represents this event in each sub-figure. At t=23 minutes, the Ketamine-
Medetomidine cocktail was injected, represented by the second vertical red line. Finally, the point of loss of
consciousness (LOC) was registered at t=33 minutes, indicated by the third vertical red line.
In both Theta and Gamma bands, after the
administration of the anesthetics, an increase
in the average betweenness centrality degree
and a reduction in the variation of the values
were observed compared to the awake state
(eyes open and blindfolded) (see Figure · 6,
Sub-Figures B and E).
In the Alpha band, after administering the
anesthetics, the vertice’s average centrality de-
gree was reduced, and an increase in the varia-
tion of the values was observed (see Figure · 6,
Sub-Figure C).
On the Beta band, one and a half minutes
after the anesthetic injection, the average be-
tweenness centrality degree of the nodes was
reduced. About 15 minutes later, the values
increased (see Figure · 6, Sub-Figure D).
VII.
Vertices Betweenness Centrality
Degree and Cortical Areas
By plotting the intermediation degree of each
vertice through a color gradient, it was possible
to verify the correspondence between the inter-
mediation degree of the network’s vertices and
their corresponding cortical areas and anatom-
ical divisions.
It was noticeable that nodes physically
closer to each other presented a quite simi-
lar intermediation degree. However, not all
13


## Page 14


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
(A) Delta 0-4Hz
(B) Theta 4-8Hz
(C) Alpha 8-12Hz
(D) Beta 13-30Hz
(E) Gamma 25-100Hz
Figure 6: Betweenness Centrality. Vertical axis betweenness centrality; Horizontal axis time (minutes). At t=11
minutes, the monkey was blindfolded; the first vertical red line represents this event in each sub-figure. At
t=23 minutes, the Ketamine-Medetomidine cocktail was injected, represented by the second vertical red line.
Finally, the point of loss of consciousness (LOC) was registered at t=33 minutes, indicated by the third
vertical red line.
vertices of the networks had the same between-
ness centrality degree. Furthermore, it was
possible to note that the betweenness centrality
degree of the vertices was related to cortical
anatomy and divisions (see Figure · 7).
It was verified that the intermediation de-
gree of the vertices is dynamic once varia-
tions from consecutive (time) networks have
occurred. Besides those variations, during the
experiment, two prominent patterns were ob-
served, the first respective to the time when the
monkey was awake and the second to when it
was anesthetized.
Awake State Pattern
While in awakening conditions, most nodes
had a relevant contribution to the network’s
geodesic paths. Notably, some vertices had
a higher intermediation degree and were fre-
quently located closer to each other. Moreover,
those higher-degree vertices extended and in-
volved continuous large areas of the cortex (see
Figure · 7, Sub-Figures A - E).
14


## Page 15


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
Table 5: Mean, variance (Var), and standard deviation (SD) of the mean betweenness centrality degree on the five
physiological frequency bands analyzed and on the three different conditions in which the monkey was exposed
during the experiment: awake with eyes open, awake with eyes closed and anesthesia (eyes closed).
Centrality
Eyes Open
Eyes Closed
Anesthesia
Frequency Band
Mean
Var
SD
Mean
Var
SD
Mean
Var
SD
Delta (0-4Hz)
102
875
29.6
88.6
920
30.3
91.2
662
25.7
Theta (4-8Hz)
99.5
744
27.3
67.5
822
28.7
117
642
25.3
Alpha (8-12Hz)
93.1
599
24.5
67.5
761
27.6
45.0
932
30.5
Beta (13-30Hz)
82.5
837
28.9
73.3
710
26.6
60.8
1270
35.6
Gamma (25-100Hz)
98.2
667
25.8
92.2
1840
42.9
112
413
20.3
Anesthetized State Pattern
While the macaque was anesthetized, a few
nodes (cortical areas) had a high between-
ness centrality degree, while the other net-
work nodes had a reduced centrality degree.
It was possible to observe that the vertices of
some specific cortical regions monopolized the
network’s intermediation.
Another remark-
able change observed was the coverage dis-
continuity of those areas of high betweenness
centrality located far from each other, sepa-
rated by regions characterized by vertices of
reduced intermediation degree (see Figure · 7,
Sub-Figures P - T).
Transition
About one minute and a half after administer-
ing the anesthetics, there was a transition in the
patterns of the vertices intermediation degree.
The pattern observed in the awake state was no
longer present, being replaced by a different
pattern that predominated while the monkey
was anesthetized. The transition between the
two patterns occurred in approximately 40 to
50 seconds (see Figure · 7, Sub-Figures J - Q).
VIII.
Assortativity
The placement of a blindfold over the eyes
of the monkey did not change the assorta-
tive coefficient of the graphs significantly (see
Figure · 8). Small changes were observed in
each frequency band. However, no significant
alteration in the dynamic behavior occurred
as a result of blindfolding the macaque (eyes
open vs. closed).
Table 6: Mean, variance (Var), and standard deviation (SD) of the assortativity coefficient on the five physiological
frequency bands analyzed and on the three different conditions in which the monkey was exposed during the
experiment: awake with eyes open, awake with eyes closed and anesthesia (eyes closed).
Assortativity
Eyes Open
Eyes Closed
Anesthesia
Frequency Band
Mean
Var
SD
Mean
Var
SD
Mean
Var
SD
Delta (0-4Hz)
-0.03
0.02
0.14
0.02
0.03
0.17
0.19
0.02
0.14
Theta (4-8Hz)
0.01
0.02
0.14
0.08
0.03
0.17
0.23
0.02
0.14
Alpha (8-12Hz)
0.02
0.03
0.17
0.10
0.03
0.17
0.22
0.03
0.17
Beta (13-30Hz)
0.25
0.02
0.14
0.25
0.03
0.17
0.14
0.02
0.14
Gamma (25-100Hz)
-0.17
0.01
0.10
-0.18
0.01
0.17
0.11
0.05
0.22
15


## Page 16


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
Figure 7: Vertice’s Intermediation Degree. The transition between the awake and anesthetized states. Frequency
band Alpha (8-12Hz). In each sub-figure, the vertice’s intermediation degree is represented through a color
gradient over the respective coordinates of the electrodes. The sub-figures correspond to the intermediation
degree of the vertices estimated sequentially over time, being 5 seconds the time interval between each frame
and its subsequent. The frame A starts approximately one minute after the administration of the anesthetics.
Significant changes in the network’s assor-
tative character occurred after administering
the anesthetics (see Figure · 8; Table · 6). Quite
similar behavior was observed in the Delta,
Theta, and Alpha bands. While the macaque
was awake, the assortativity varied in those fre-
quency bands, assuming positive and negative
values. On average, a disassortative character
was prevalent. A few seconds after the ad-
ministration of the anesthetics, an accentuated
change occurred, and the graphs assumed an
assortative character, having positive assorta-
tivity (see Figure · 8, Sub-Figures A, B, and C).
16


## Page 17


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
(A) Delta 0-4Hz
(B) Theta 4-8Hz
(C) Alpha 8-12Hz
(D) Beta 13-30Hz
(E) Gamma 25-100Hz
Figure 8: Assortativity. Vertical axis assortativity; Horizontal axis time (minutes). At t=11 minutes, the monkey
was blindfolded; the first vertical red line represents this event in each sub-figure. Next, at t=23 minutes, the
Ketamine-Medetomidine cocktail was injected, represented by the second vertical red line. Finally, the point
of loss of consciousness (LOC) was registered at t=33 minutes, indicated by the third vertical red line.
In the Beta band, an assortative character
prevailed throughout the experiment. After the
anesthetics were administered, the assortativity
gradually lowered for about 10 minutes. After
that time, the assortativity started to increase
and assumed the same dynamic behavior un-
til the end of the experiment (see Figure · 8,
Sub-Figure D).
While the monkey was awake, the networks
respective to the Gamma band were disassor-
tative. Almost right after the administration
of the drugs, the functional brain networks
started to assume a high variation in the assor-
tativity, being sometimes assortative and other
times disassortative, revealing in this frequency
band an expressive dynamics of network struc-
tural alterations during general anesthesia (see
Figure · 8, Sub-Figure E).
IX.
Transitivity
Blindfolding the monkey has led to an increase
in both the variation and the mean values of
the transitivity coefficient compared to the
time when the monkey had its eyes open (see
Figure · 9; Table · 7).
After the anesthetic injection, significant al-
terations in the transitivity coefficient (New-
man, 2001) were noticeable on some frequency
bands (see Figure · 9).
17


## Page 18


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
After administering the anesthetics, the
Delta band presented an increase in the tran-
sitivity coefficient, with the variation of the
values kept almost constant (see Figure · 9,
Sub-Figure A).
In the Theta and Alpha bands, during gen-
eral anesthesia, a decrease in the transitivity
and a reduction in the variation of the values
occurred (see Figure · 9, Sub-Figures B and C).
In Beta, one minute and a half after the
anesthetic injection, an expressive decline oc-
curred. The transitivity coefficient was rela-
tively smaller than when the macaque was
awake (eyes open and closed), remaining this
way while the monkey was anesthetized (see
Figure · 9, Sub-Figure D).
(A) Delta 0-4Hz
(B) Theta 4-8Hz
(C) Alpha 8-12Hz
(D) Beta 13-30Hz
(E) Gamma 25-100Hz
Figure 9: Transitivity. Vertical axis transitivity coefficient; Horizontal axis time (minutes). At t=11 minutes, the
monkey was blindfolded; the first vertical red line represents this event in each sub-figure. Next, at t=23
minutes, the Ketamine-Medetomidine cocktail was injected, represented by the second vertical red line.
Finally, the point of loss of consciousness (LOC) was registered at t=33 minutes, indicated by the third
vertical red line.
In Gamma, a reduction in the values was
observed one minute and a half after admin-
istering the anesthetics. Later, the transitiv-
ity coefficient started to increase. Another re-
markable alteration in this frequency band was
a smaller variation of the values compared
to the period when the monkey was awake
(see Figure · 9, Sub-Figure E).
18


## Page 19


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
Table 7: Mean, variance (Var), and standard deviation (SD) of the transitivity coefficient on the five physiological
frequency bands analyzed and on the three different conditions in which the monkey was exposed during the
experiment: awake with eyes open, awake with eyes closed and anesthesia (eyes closed).
Transitivity
Eyes Open
Eyes Closed
Anesthesia
Frequency Band
Mean
Var
SD
Mean
Var
SD
Mean
Var
SD
Delta (0-4Hz)
0,27
0,01
0.10
0,37
0.02
0.14
0.44
0.01
0.10
Theta (4-8Hz)
0,32
0,01
0.10
0,48
0.01
0.10
0.40
0.01
0.10
Alpha (8-12Hz)
0,32
0,01
0.10
0,49
0.02
0,14
0.35
0.01
0.10
Beta (13-30Hz)
0,51
0,01
0.10
0,55
0.01
0,10
0.32
0.01
0.10
Gamma (25-100Hz)
0,26
0,01
0.10
0,25
0.02
0,14
0.36
0.01
0.10
IV.
Discussion
In the experiment, the administration of the
Ketamine-Medetomidine cocktail led to al-
terations in various network properties on
the five physiological frequency bands ana-
lyzed.
The most remarkable alterations oc-
curred in the Theta, Alpha, and Beta bands.
Those experimental observations indicate that
the Ketamine-Medetomidine cocktail affected
more expressively neural activities occurring
between 4 and 30Hz.
Once the anesthetic
agents promoted physiological changes in
the animal subject, drastically reducing its
cognitive capacity and level of consciousness,
suggest that neural processes and activities
related to cognition and consciousness may
primarily occur within frequencies ranging
from 4 to 30 Hz.
Changes in several topological properties
of the networks occurred within approximately
one and a half minutes after administering
the anesthetics. This observation of consistent
changes occurring rapidly and simultaneously
in different properties of the graphs strongly
indicates a phase transition in the network’s
architecture. Furthermore, the fact that phe-
nomena occurred straight after the injection of
the anesthetic cocktail provides strong confi-
dence that the changes observed during the
experiment are directly related to the physio-
logical effects of the anesthetics on the animal
(a rapid and expressive reduction in the level
of consciousness).
Those results are exciting according to the
perspective of the Modern Network Science once
they bring empirical evidence involving rela-
tions between a change in the behavior of a
natural system and alterations in its respec-
tive underlying networks. They are in agree-
ment with one of the remarkable premises of
complex systems science, which states that the
behavior exhibited by a system is intimately re-
lated to its structure, that is, to the specific way
in which the elements of the system establish
interactions.
The present research is one of the first pa-
pers to report the existence and estimate the
structure and dynamics of large-scale func-
tional brain networks respective to induced
general anesthesia.
I.
Alterations on the Network’s Prop-
erties
Average degree
The average degree reflects the average number
of connections of the network’s vertices (Rubi-
nov and Sporns, 2010), providing information
related to the global connectivity of the graph,
indicating how interactive the elements of the
system are.
The results obtained in this research re-
vealed that after administering the anesthetics,
there was a significant reduction in the average
degree respective to the Theta, Alpha, and Beta
bands (see Figure · 1; Table · 1). From this exper-
imental evidence, it has been verified that the
19


## Page 20


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
anesthetic induction leads to a significant re-
duction in cortical connectivity, demonstrating
that functional interactions established among
various regions of the cortex are impaired dur-
ing general anesthesia.
Vertices Degree and Cortical Areas
Considering the functional brain networks, the
degree of each vertex brings information re-
garding the capacity of the area that it rep-
resents to influence or receive influence from
other distinct areas (Sporns, 2011).
The results of this experiment demonstrate
that in the awake state, high-degree vertices
cover all frontal and parietal lobes and tem-
poral areas anterior to the superior temporal
sulcus, indicating that in awakening conditions,
those cortical regions present high connectiv-
ity and functional integration. After adminis-
tering the anesthetics, highly connected ver-
tices were no longer observed in those cor-
tical areas, evidencing a drastic reduction in
functional connectivity. The results reveal that
the Ketamine-Medetomidine cocktail mainly af-
fected the prominent connectivity that existed
in areas of the secondary associative cortex of
the frontal and parietal lobes, strongly suggest-
ing that events of consciousness may be highly
dependent on the high functional integration
involving these anatomical regions. Such ex-
perimental evidence is in accordance with sev-
eral scientific reports relating the same regions
to neural correlates of consciousness. Further-
more, there is experimental evidence that the
administration of the general anesthetic Propo-
fol induces a significant decrease in blood flow
in areas of the pre-cuneus, cuneus, and poste-
rior cingulate cortex (Fiset et al., 1999), with
the inactivation of the posterior medial part
associated with loss of consciousness (Kaisti
et al., 2002). Damasio and Dolan reported that
injuries affecting the same cortical areas are
related to severe disturbances of cognition and
consciousness (Damasio and Dolan, 1999). Lau-
reys highlighted that frontoparietal regions are
preferentially deactivated in human patients
in the vegetative states (Laureys et al., 2004),
with the loss of consciousness of those patients
associated with the functional disconnectivity
between frontal and parietal regions (Laureys
et al., 1999).
Average Degree - Cortical Lobes
The analysis of the average degree of the sub-
graphs respective to the frontal, parietal, tem-
poral, and occipital lobes confirms some fea-
tures observed in the color gradient represent-
ing the degree of the vertices over the position
of the electrodes. In addition, those results
show that on the Theta, Alpha, and Beta1 fre-
quency bands, the anesthetic induction led to
an expressive decrease in functional connec-
tivity over the frontal, parietal, and temporal
lobes (see Figure · 3; Table · 2).
Unlike what happened in the frontal, pari-
etal, and temporal lobes, the average connectiv-
ity of the subgraphs respective to the occipital
lobe was three times higher2 during general
anesthesia (see Table · 2). Furthermore, such
an event was also observed in the color gra-
dient representing the vertice’s degree. These
results strongly suggest the presence of coher-
ent neural activity in the occipital lobe during
general anesthesia induced by Ketamine and
Metomidine.
Average Path Length
According to Latora and Marchiori, a network’s
capacity and global efficiency in transmitting
information are directly related to the average
of its minimum paths, the most efficient net-
works are those with the shortest paths (Latora
and Marchiori, 2001).
The experimental results demonstrate that
the administration of the anesthetics led to a
substantial increase in the average path length
(Costa et al., 2007) on the Theta, Alpha, and
Beta frequency bands (see Figure · 4; Table · 3).
Such an increase in the average path length
1Theta and Beta frequency bands data not shown.
2When compared to the awake state (eyes open).
20


## Page 21


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
strongly indicates that the overall capacity for
transmitting information between multiple cor-
tical areas is significantly reduced during gen-
eral anesthesia.
Diameter
The diameter of the network (Costa et al., 2007),
once related only to the larger geodesic path of
the graph, is a less informative measure than
the average path length once the latter takes
into account all the minimum paths of the net-
work. The diameter reflects the length of the
largest minimum path, representing the maxi-
mum distance existent on the network3.
The experimental results reveal a consider-
able increase in the length of the diameter of
the networks on the Theta, Alpha, and Beta
bands, which occurred one and a half minutes
after the administration of the anesthetics (see
Figure · 5). Such a result supports the conclu-
sions obtained by analyzing the average path
length, that the global transmission of informa-
tion is reduced during general anesthesia.
Transitivity
According to Latora and Marchiori, the local
efficiency of information transmission in a net-
work is directly related to its transitivity coef-
ficient. The larger the coefficient, the greater
the local efficiency of the network (Latora and
Marchiori, 2003).
The results obtained in this study demon-
strate that the anesthetics led to a reduction
of the transitivity coefficient4 (see Table · 7;
Figure · 9). Such a decrease indicates that the
transmission of information efficiency is re-
duced at local levels during the induced state
of anesthesia.
Assortativity Coefficient
The assortativity coefficient (Boccaletti et al.,
2006) is related to the preferential attachment
between vertices concerning their connectiv-
ity degree (Boccaletti et al., 2006). Alterations
in this coefficient reveal structural changes in
the graphs, specifically the manner in which
the connections between the vertices are estab-
lished.
The results of this experiment revealed that
the anesthetics led to significant alterations
in the network’s assortativity character. The
most accentuated changes were observed in the
Delta, Theta, and Gamma bands (see Figure · 8).
These results demonstrate structural changes
in the neural activity network’s organization
over those frequency bands. The graphs cor-
responding to the Delta and Gamma bands
showed no noticeable changes in other net-
work measures after the anesthetic induction
process. However, alterations in the assortativ-
ity coefficient highlight that the anesthetics led
to significant structural rearrangements in the
large-scale functional brain networks.
As reported by Costa, the network’s assor-
tativity character may influence the dynamic
processes supported by the system (Costa et al.,
2007). The fact that the networks respective to
the induced state of anesthesia assumed a pre-
dominantly assortative character might imply
a higher instability of those networks (Brede
and Sinha, 2005) and a reduction in their syn-
chronization capacity (di Bernardo et al., 2005).
Intermediation Degree and Cortical Ar-
eas
The betweenness centrality degree of a vertex
(Freeman, 1979) is related to the relevance of
this vertex, given its participation in the min-
imum paths of the network. The larger the
number of minimum paths passing through
a node, the more significant the impact on
the network integration performed by this ver-
tex. The analysis of the relationship between
the intermediation degree of the vertices and
the position of the electrodes over the cor-
3Assuming that the graph is connected.
4Mainly when compared to the awake state (eyes closed), in Theta, Alpha, and Beta, the most prominent reduction
observed in the Beta band.
21


## Page 22


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
tex provides an estimate of how information
transmission is performed on the network,
highlighting the areas that monopolize the flux
of information and play an essential role in
functional integration.
The results obtained experimentally demon-
strate that during awake conditions (eyes open
and closed), the vast majority of the vertices
of the graph had a high intermediation degree
(see Figure · 7), indicating that the flow of infor-
mation on the network is in a certain way dis-
tributed between multiple cortical areas. Those
results suggest that during awake conditions,
the vast majority of the cortex gives support
and is possibly actively involved in informa-
tion transmission. Another remarkable charac-
teristic is that high intermediation vertices ex-
tended, covering continuously large cortical ar-
eas, without being separated by regions charac-
terized by vertices possessing a low intermedia-
tion degree (see Figure · 7, Sub-Figures A - E).
After administering the anesthetics, a signif-
icant change concerning the intermediation de-
gree of the vertices and their respective cortical
areas occurred (see Figure · 7). It was possible
to observe that some areas monopolized the
integration of the network and that the vast ma-
jority of the cortex presented a reduced degree
of intermediation, revealing that the structure
of the network did not provide the distribu-
tion of the flow of information over “the entire”
cortex anymore. Another remarkable charac-
teristic observed was the discontinuity of the
occupancy of the areas having a high degree of
intermediation, being those physically segre-
gated by extensive regions marked by vertices
possessing a low intermediation degree (see
Figure · 7, Sub-Figures P - T). From the anal-
ysis of the results, it is possible to infer the
hypothesis that activity and neural processes
associated with conscious experiences may re-
quire the involvement of a significant portion
of the cortex in the integration of the entire
network.
Average Betweenness Centrality De-
gree
A direct association between the average inter-
mediation degree of the vertices and functional
or structural properties of the network is not
trivial once distinct alterations in the graph’s
topology may lead to similar changes in the
mean intermediation degree of the vertices. Be-
sides not being able to comprehend straight-
forwardly the meanings and implications of
the alterations observed on this property, the
existence of changes confirms that structural
alterations have occurred on the graphs.
In this experiment, after administering the
anesthetics, noticeable changes were observed
in the average betweenness centrality degree in
the Theta, Alpha, Beta, and Gamma bands (see
Table · 5; Figure · 6), confirming the occurrence
of structural rearrangements in the large-scale
functional brain networks during general anes-
thesia.
II.
Alterations due to Anesthesia on
Small-World Architecture
Regarding the five frequency bands analyzed,
the most significant alterations observed dur-
ing the anesthetic induction occurred on the
networks respective to the Theta, Alpha, and
Beta bands. In general, those frequency bands
presented mainly the same kind of alterations:
• An expressive reduction on the average
degree of the vertices.
• A considerable increase in the average
path length.
• A decrease in the transitivity coefficient.
The considerable reduction in the average de-
gree and transitivity and the significant in-
crease in the average path length have direct
consequences, impacting the small world ar-
chitecture (Watts and Strogatz, 1998) observed
during the awake state.
According to Olaf
Sporns, the small-world architecture, charac-
terized by high values of the transitivity coeffi-
cient and a small average path length, provides
22


## Page 23


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
a structural substrate of great relevance, impor-
tant in many aspects of the brain’s functional
organization. This architecture supports pro-
cessing information segregated locally and inte-
grated globally (Sporns, 2011). The small world
architecture is also considered to promote the
efficiency of transmission and processing of
information, the wiring economy, and the sup-
port of diverse and complex network dynamics
(Bullmore and Sporns, 2012).
Several authors consider segregation and
integration as two of the main principles of the
organization of activities that occur in the cere-
bral cortex (Zeki, 1978; Zeki and Shipp, 1988;
Tononi et al., 1994; Tononi and Edelman, 1998;
Friston, 2002, 2005, 2009). Sporns highlights
that the balance between those two properties
constitutes a key mechanism necessary for the
brain to perform its activities (Sporns, 2011).
The results of this study demonstrate that
the anesthetic induction had most significantly
impacted two network properties over the
Theta, Alpha, and Beta frequency bands. These
properties were the integration capacity at
global levels (an increase in the average path
length) and the integration capacity at local
levels (a decrease in the transitivity coefficient).
Those factors have a direct consequence on the
breakdown of the small-world architecture that
was observed in the awake state. These experi-
mental results support hypotheses pointed out
by many authors, relating the loss of funda-
mental structural properties of functional net-
works to alterations and suppression of brain
functions.
Alterations Observed After the Place-
ment of the Blindfold
Several alterations in the topology and dy-
namic behavior of the properties of the large-
scale functional brain networks were observed
after placing a blindfold over the eyes of the
macaque. It is possible from the figures and
graphs to note clear distinctions regarding the
time when the monkey had its eyes open and
when it had its eyes closed.
The researchers who conducted the experi-
ments and provided the database of the neu-
ral activity records did not provide enough
information regarding the placement of the
blindfold on the state of the animal. The ef-
fects may depend on several factors, such as
the macaque’s conditioning to the experimen-
tal settings, the animal’s familiarity with the
researchers, the handling techniques used dur-
ing the experiment, and other variables. For
example, placing a blindfold over the eyes of
the monkey and restraining the animal in a
chair might have led to a calm and relaxed
state or triggered fear and apprehension. Thus,
conclusions regarding the relationship between
the network measures and the specific state in
which the monkey was can only be drawn un-
der an experiment’s detailed description. The
fact that alterations were observed in the net-
work measures immediately after blindfolding
the monkey demonstrates that the functional
networks are dependent on the conditions pre-
sented to the animal. Those observed phenom-
ena follow some of the suppositions from Olaf
Sporns, who stated that functional connectivity
might vary considerably over time, modulated
by demands due to different types of activities
or due to different sensory stimuli presented
(Sporns, 2011).
Point of Loss of Consciousness (LOC)
The scientists who conducted the experimental
procedures and recorded the data reported the
occurrence of the loss of consciousness point
(LOC) at the moment when the animal ceased
to respond to stimuli, such as touching the nos-
trils and hands. However, no prominent alter-
ations in network properties were observed at
the (LOC), registered by the researchers about
ten minutes after administering the anesthet-
ics. Therefore, the awake state probably ended
when several changes in the properties of the
networks were observed, which occurred less
than two minutes after the anesthetic injection.
However, after that time, the monkey was still
able to exhibit involuntary reactions to stimuli,
being in an intermediary state between deep se-
23


## Page 24


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
dation and general anesthesia, probably in sim-
ilar conditions as the pharmacological effects
of the administration of Ketamine in human
patients are described (Bergman, 1999).
V.
Conclusions
The supposed view of general anesthesia be-
ing given by a "whole brain shutdown" is not
supported by the experimental findings of this
study. Instead, it was possible to observe that
during the Ketamine-medetomidine-induced
anesthesia, the brain entered into a highly spe-
cific, complex, and dynamic state.
By modeling the interactions established
among several cortical areas through graphs
and complex networks, it was possible to ver-
ify that the networks corresponding to the in-
duced state of anesthesia were structurally dis-
tinct from the networks respective to the awake
state.
Those results reveal that anesthetics
can impact several properties of the large-scale
functional brain networks, resulting in graphs
of different architectures.
Furthermore, the
changes observed in the experiment indicate
that the behavior exhibited and the processes
supported by the brain may be directly related
to the structural properties of large-scale func-
tional networks. It was possible to conclude
that functional neural activities are dynamic,
as significant changes were observed in the
network measures over short time intervals.
Observing the degree of the vertices through
a color gradient also reveals consistent pattern
changes occurring within a few seconds. Such
evidence demonstrates that functional neural
activities are not static; they reveal that the
brain’s functional activity organization is re-
markably dynamic5.
The Ketamine-Medetomidine cocktail did
not alter the functional activities in only some
specific and restricted areas of the cortex; a gen-
eral change in the state of the brain in which all
the cortex presented alterations in functional
connectivity occurred.
The most remarkable changes observed in
the large-scale functional brain networks due
to the anesthetic induction were an accentu-
ated decrease in functional connectivity and a
reduction in the capacities of integration of the
networks at both local and global levels.
From the characterization of the functional
networks during the anesthetic induction pro-
cess, we verified a transition between the awake
and anesthetized states.
The transition oc-
curred in a pretty fast manner, taking about 20
to 30 seconds.
Financial Support
This research was partially financed by CAPES
(Coordenação de Aperfeiçoamento de Pessoal
de Nível Superior).
During part of the development of the
study, the author used the structure of the
Laboratory Vision-eScience at Universidade de
São Paulo, a laboratory supported by FAPESP,
CNPq, CAPES, NAP-eScience, PRP, and USP.
References
Michael T Alkire.
Quantitative eeg correla-
tions with brain glucose metabolic rate dur-
ing anesthesia in volunteers. Anesthesiology,
89(2):323–333, 1998.
Michael T Alkire, Richard J Haier, Steven J
Barker, Nitin K Shah, Joseph C Wu, and
Y James Kao. Cerebral metabolism during
propofol anesthesia in humans studied with
positron emission tomography. Anesthesiol-
ogy, 82(2):393–403, 1995.
MT Alkire, RJ Haier, and JH Fallon. Toward
a unified theory of narcosis: brain imaging
evidence for a thalamocortical switch as the
neurophysiologic basis of anesthetic-induced
unconsciousness. Consciousness and cognition,
9(3):370–386, 2000.
Stewart A Bergman. Ketamine: review of its
pharmacology and its use in pediatric anes-
thesia. Anesthesia progress, 46(1):10, 1999.
5In both awake and anesthetized conditions.
24


## Page 25


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
Stefano Boccaletti, Vito Latora, Yamir Moreno,
Martin Chavez, and D-U Hwang. Complex
networks: Structure and dynamics. Physics
reports, 424(4):175–308, 2006.
Markus Brede and Sitabhra Sinha. Assortative
mixing by degree makes a network more un-
stable. arXiv preprint cond-mat/0507710, 2005.
Ed Bullmore and Olaf Sporns. Complex brain
networks: graph theoretical analysis of struc-
tural and functional systems. Nature Reviews
Neuroscience, 10(3):186–198, 2009.
Ed Bullmore and Olaf Sporns. The economy of
brain network organization. Nature Reviews
Neuroscience, 13(5):336–349, 2012.
L da F Costa, Francisco A Rodrigues, Gonzalo
Travieso, and Paulino Ribeiro Villas Boas.
Characterization of complex networks: A
survey of measurements. Advances in Physics,
56(1):167–242, 2007.
Jie Cui, Lei Xu, Steven L Bressler, Mingzhou
Ding, and Hualou Liang. Bsmart: a matlab/c
toolbox for analysis of multichannel neural
time series. Neural Networks, 21(8):1094–1104,
2008.
Antonio Damasio and Raymond J Dolan. The
feeling of what happens. Nature, 401(6756):
847–847, 1999.
Mario di Bernardo, Franco Garofalo, and
Francesco Sorrentino.
Synchronization of
degree correlated physical networks. arXiv
preprint cond-mat/0506236, 2005.
Pierre Fiset, Tomás Paus, Thierry Daloze,
Gilles Plourde, Pascal Meuret, Vincent Bon-
homme, Nadine Hajj-Ali, Steven B Backman,
and Alan C Evans.
Brain mechanisms of
propofol-induced loss of consciousness in
humans: a positron emission tomographic
study. The Journal of neuroscience, 19(13):5506–
5513, 1999.
Hans Flohr. An information processing the-
ory of anaesthesia. Neuropsychologia, 33(9):
1169–1180, 1995.
Linton C Freeman.
Centrality in social net-
works conceptual clarification.
Social net-
works, 1(3):215–239, 1979.
Karl Friston. Beyond phrenology: what can
neuroimaging tell us about distributed cir-
cuitry? Annual review of neuroscience, 25(1):
221–250, 2002.
Karl J Friston. Functional and effective connec-
tivity in neuroimaging: a synthesis. Human
brain mapping, 2(1-2):56–78, 1994.
Karl J Friston.
Models of brain function in
neuroimaging. Annu. Rev. Psychol., 56:57–87,
2005.
Karl J Friston. Modalities, modes, and mod-
els in functional neuroimaging. Science, 326
(5951):399–403, 2009.
KJ Friston, CD Frith, PF Liddle, and RSJ
Frackowiak.
Functional connectivity: the
principal-component analysis of large (pet)
data sets. Journal of Cerebral Blood Flow &
Metabolism, 13(1):5–14, 1993.
Makoto Fukushima,
Richard C Saunders,
Matthew Mullarkey, Alexandra M Doyle,
Mortimer Mishkin, and Naotaka Fujii. An
electrocorticographic electrode array for si-
multaneous recording from medial, lateral,
and intrasulcal surface of the cortex in
macaque monkeys.
Journal of neuroscience
methods, 233:155–165, 2014.
Clive WJ Granger.
Investigating causal re-
lations by econometric models and cross-
spectral methods. Econometrica: Journal of
the Econometric Society, pages 424–438, 1969.
Steven M Green, Mark G Roback, Robert M
Kennedy, and Baruch Krauss. Clinical prac-
tice guideline for emergency department ke-
tamine dissociative sedation: 2011 update.
Annals of emergency medicine, 57(5):449–461,
2011.
Stuart Hameroff. The entwined mysteries of
anesthesia and consciousness. Anesthesiology,
105(2):400–12, 2006.
25


## Page 26


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
Stuart R Hameroff, Alfred W Kaszniak, and
Alwyn Scott. Toward a science of consciousness
II: The second Tucson discussions and debates,
volume 2. Mit Press, 1998.
James D Hamilton. A new approach to the eco-
nomic analysis of nonstationary time series
and the business cycle. Econometrica: Jour-
nal of the Econometric Society, pages 357–384,
1989.
Olga A Imas, Kristina M Ropella, B Dou-
glas Ward, James D Wood, and Anthony G
Hudetz. Volatile anesthetics disrupt frontal-
posterior recurrent information transfer at
gamma frequencies in rat. Neuroscience let-
ters, 387(3):145–150, 2005.
Atsushi Iriki and Osamu Sakura.
The neu-
roscience of primate intellectual evolution:
natural selection and passive and intentional
niche construction. Philosophical Transactions
of the Royal Society B: Biological Sciences, 363
(1500):2229–2241, 2008.
E Roy John and Leslie S Prichep. The anesthetic
cascade: a theory of how anesthesia sup-
presses consciousness. Anesthesiology, 102(2):
447, 2005.
Kaike K Kaisti, Liisa Metsähonkala, Mika
Teräs, Vesa Oikonen, Sargo Aalto, Satu
Jääskeläinen, Susanna Hinkka, and Harry
Scheinin. Effects of surgical levels of propo-
fol and sevoflurane anesthesia on cerebral
blood flow in healthy subjects studied with
positron emission tomography. Anesthesiol-
ogy, 96(6):1358–1370, 2002.
Donald Kennedy and Colin Norman. What
don’t we know?
Science, 309(5731):75–75,
2005.
Denis Kwiatkowski, Peter CB Phillips, Peter
Schmidt, and Yongcheol Shin. Testing the
null hypothesis of stationarity against the
alternative of a unit root: How sure are we
that economic time series have a unit root?
Journal of econometrics, 54(1):159–178, 1992.
Vito Latora and Massimo Marchiori. Efficient
behavior of small-world networks. Physical
review letters, 87(19):198701, 2001.
Vito Latora and Massimo Marchiori. Economic
small-world behavior in weighted networks.
The European Physical Journal B-Condensed
Matter and Complex Systems, 32(2):249–263,
2003.
Steven Laureys, Serge Goldman, Christophe
Phillips, Patrick Van Bogaert, Joël Aerts, An-
dré Luxen, Georges Franck, and Pierre Ma-
quet. Impaired effective cortical connectivity
in vegetative state: preliminary investigation
using pet. Neuroimage, 9(4):377–382, 1999.
Steven
Laureys,
Adrian
M
Owen,
and
Nicholas D Schiff. Brain function in coma,
vegetative state, and related disorders. The
Lancet Neurology, 3(9):537–546, 2004.
Laura D Lewis, Veronica S Weiner, Eran A
Mukamel, Jacob A Donoghue, Emad N Es-
kandar, Joseph R Madsen, William S An-
derson, Leigh R Hochberg, Sydney S Cash,
Emery N Brown, et al. Rapid fragmenta-
tion of neuronal networks at the onset of
propofol-induced unconsciousness. Proceed-
ings of the National Academy of Sciences, 109
(49):E3377–E3386, 2012.
George A Mashour. Consciousness unbound:
toward a paradigm of general anesthesia.
2004.
George A Mashour. Integrating the science of
consciousness and anesthesia. Anesthesia &
Analgesia, 103(4):975–982, 2006.
Melanie Mitchell. Complexity: A guided tour.
Oxford University Press, 2009.
Yasuo Nagasaka, Kentaro Shimoda, and Nao-
taka Fujii. Multidimensional recording (mdr)
and data sharing: an ecological open re-
search and educational platform for neuro-
science. PloS one, 6(7):e22561, 2011.
Mark EJ Newman. The structure of scientific
collaboration networks.
Proceedings of the
National Academy of Sciences, 98(2):404–409,
2001.
26


## Page 27


Padovani, E. C. - arXiv preprint - Neurons and Cognition • March 2016 •
Mark EJ Newman. The structure and function
of complex networks. SIAM review, 45(2):
167–256, 2003.
Mikail Rubinov and Olaf Sporns. Complex net-
work measures of brain connectivity: uses
and interpretations. Neuroimage, 52(3):1059–
1069, 2010.
Robert S Schwartz, Emery N Brown, Ralph
Lydic, and Nicholas D Schiff. General anes-
thesia, sleep, and coma. New England Journal
of Medicine, 363(27):2638–2650, 2010.
Anil K Seth.
A matlab toolbox for granger
causal connectivity analysis. Journal of neuro-
science methods, 186(2):262–273, 2010.
Anil K Seth and Gerald M Edelman. Distin-
guishing causal interactions in neural pop-
ulations. Neural computation, 19(4):910–933,
2007.
Olaf Sporns. Networks of the Brain. MIT press,
2011.
CJ Stam and ECW Van Straaten. The organiza-
tion of physiological brain networks. Clinical
Neurophysiology, 123(6):1067–1087, 2012.
Cornelis J Stam and Jaap C Reijneveld. Graph
theoretical analysis of complex networks in
the brain. Nonlinear biomedical physics, 1(1):3,
2007.
Steven H Strogatz.
Exploring complex net-
works. Nature, 410(6825):268–276, 2001.
Giulio Tononi and Gerald M Edelman. Con-
sciousness and complexity. Science, 282(5395):
1846–1851, 1998.
Giulio Tononi, Olaf Sporns, and Gerald M Edel-
man. A measure for brain complexity: re-
lating functional segregation and integration
in the nervous system. Proceedings of the Na-
tional Academy of Sciences, 91(11):5033–5037,
1994.
L Uhrig, S Dehaene, and B Jarraya. Cerebral
mechanisms of general anesthesia. In An-
nales francaises d’anesthesie et de reanimation,
volume 33, pages 72–82. Elsevier, 2014.
Duncan J Watts and Steven H Strogatz. Col-
lective dynamics of ”small-world” networks.
Nature, 393(6684):440–442, 1998.
Nathan S White and Michael T Alkire. Im-
paired thalamocortical connectivity in hu-
mans during general-anesthetic-induced un-
consciousness.
Neuroimage, 19(2):402–411,
2003.
Toru
Yanagawa,
Zenas
C
Chao,
Naomi
Hasegawa, and Naotaka Fujii. Large-scale in-
formation flow in conscious and unconscious
states: an ecog study in monkeys. PloS one,
8(11):e80845, 2013.
SS Young, AM Schilling, S Skeans, and G Ri-
tacco.
Short duration anaesthesia with
medetomidine and ketamine in cynomolgus
monkeys. Laboratory animals, 33(2):162–168,
1999.
Semir Zeki and Stewart Shipp. The functional
logic of cortical connections. Nature, 1988.
Semir M Zeki. Functional specialisation in the
visual cortex of the rhesus monkey. Nature,
274(5670):423–428, 1978.
27

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
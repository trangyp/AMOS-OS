---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1903.05590v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1903.05590v1_Noisy_network_attractor_models_for_transitions_between_EEG_microstates

> Source: 1903.05590v1_Noisy_network_attractor_models_for_transitions_between_EEG_microstates.pdf

> Pages: 16

---


## Page 1


Noisy network attractor models for transitions between EEG
microstates
Jennifer Creaser1,*, Peter Ashwin1, Claire Postlethwaite2, and Juliane Britz3
1Department of Mathematics and EPSRC Centre for Predictive Modelling in
Healthcare, University of Exeter, Exeter, Devon, UK
2Department of Mathematics, University of Auckland, Auckland, NZ
3Department of Psychology and Department of Medicine, Neurology, University of
Fribourg, Fribourg, Switzerland
*j.creaser@exeter.ac.uk
Abstract
The brain is intrinsically organized into large-scale networks that constantly re-organize
on multiple timescales, even when the brain is at rest. The timing of these dynamics is cru-
cial for sensation, perception, cognition and ultimately consciousness, but the underlying
dynamics governing the constant reorganization and switching between networks are not yet
well understood. Functional magnetic resonance imaging (fMRI) and electroencephalogra-
phy (EEG) provide anatomical and temporal information about the resting-state networks
(RSNs), respectively. EEG microstates are brief periods of stable scalp topography, and
four distinct conﬁgurations with characteristic switching patterns between them are reli-
ably identiﬁed at rest. Microstates have been identiﬁed as the electrophysiological correlate
of fMRI-deﬁned RSNs, this link could be established because EEG microstate sequences
are scale-free and have long-range temporal correlations. This property is crucial for any
approach to model EEG microstates. This paper proposes a novel modeling approach for
microstates: we consider nonlinear stochastic diﬀerential equations (SDEs) that exhibit
a noisy network attractor between nodes that represent the microstates. Using a single
layer network between four states, we can reproduce the transition probabilities between
microstates but not the heavy tailed residence time distributions. Introducing a two layer
network with a hidden layer gives the ﬂexibility to capture these heavy tails and their
long-range temporal correlations. We ﬁt these models to capture the statistical proper-
ties of microstate sequences from EEG data recorded inside and outside the MRI scanner
and show that the processing required to separate the EEG signal from the fMRI machine
noise results in a loss of information which is reﬂected in diﬀerences in the long tail of the
dwell-time distributions.
Introduction
The human brain is intrinsically organized into large-scale networks that can be identiﬁed at
rest [1, 2]. These networks have to reorganize on a sub-second temporal scale in order to allow
the precise execution of mental processes [3]. Spatial and temporal aspects of the dynamics
underlying the reorganization of these large-scale networks require non-invasive measures with
high spatial (functional magnetic resonance imaging (fMRI)) and temporal resolution (elec-
troencephalography (EEG)). While fMRI uses the blood oxygenation level dependent (BOLD)
response as a proxy for neuronal activity with a temporal resolution of several seconds, the
EEG is a direct measure of neuronal activity which captures the temporal evolution of the scalp
electrical ﬁeld with millisecond resolution. Unlike local measures of the EEG in channel space
that vary from time-point to time-point and as a function of the reference, the global measure of
1
arXiv:1903.05590v1  [q-bio.NC]  13 Mar 2019


## Page 2


EEG topography remains stable for brief periods (50–100 ms) before changing to another quasi-
stable state, the so-called EEG microstates [4, 5]. Interestingly, four dominant topographies
are consistently reported both in healthy individuals as well as in neurological and psychiatric
patients at rest [6, 7, 5]. While neurological and psychiatric diseases rarely aﬀect their topog-
raphy, they fundamentally alter their temporal dynamics [8, 9, 10]. They have been coined the
“atoms of thought and can be considered the basic building blocks of spontaneous mentation
that make up the spontaneous electrophysiological activity measured at the scalp [11].
A study using simultaneously recorded EEG-fMRI identiﬁed EEG microstates as the elec-
trophysiological correlate of four fMRI-deﬁned resting-state networks (RSNs)[12]. This link is
surprising because EEG microstates and fMRI RSNs are two global measures of large-scale
brain activity that are observed at temporal scales two orders of magnitude apart: 50–100 ms
(microstates) and 10–20 seconds (fMRI-RSNs). Convolving the rapidly changing microstate
time series with the hemodynamic response function (HRF) to obtain regressors for BOLD
estimation acts like a strong temporal low-pass ﬁlter. The microstate time series is ’scale-free’
i.e. it shows the same behavior at diﬀerent temporal scales, therefore no information is using
this approach. Later, it was conﬁrmed that this link could be established because EEG mi-
crostate time-series are mono-fractal and show long-range dependency (LRD) over six dyadic
scales spanning two orders of magnitude (256 ms to 16 s) [13]. EEG microstates and fMRI
RSNs hence capture the same underlying physiological process at diﬀerent temporal scales with
an electrophysiological and a hemodynamic measure, respectively.
Importantly, Britz et al.
demonstrate that the precise timing but not the order of local transitions of the microstate se-
quences is crucial for their fractal properties: shuﬄing their local transitions without changing
their timing has no eﬀect, whereas equalizing their durations degrades the time series to white
noise without memory, hence attempts at modeling microstate sequences have to go beyond
modelling the local transitions.
We note that the “state transition process” and the waiting (residence) time distribution
for the “renewal process” where the transitions occur are essentially independent processes. In
the case that the renewal process is memoryless then the whole process can be seen as Markov
jump process, but it is possible for the transitions to be Markov but the jump times to be non-
Markov. von Wegner et al. show that neither memoryless Markov models nor single parameter
LRD models fully capture the data and conclude that more sophisticated models need to be
developed to understand the underlying mechanisms of microstates [14].
In this paper we provide a novel modelling approach based on dynamical structures called
noisy network attractors.
These are stochastic models that exhibit heteroclinic or excitable
network attractors in their noise-free dynamics [15]. A heteroclinic network is a collection of
solutions (heteroclinic orbits) that link a set of steady states (saddles) that themselves are
unstable. Excitable networks, in the sense introduced in [15], are close relations of heteroclinic
networks that have a small but ﬁnite threshold of perturbation that needs to be overcome to
make a transition between a number of attracting states. Heteroclinic networks have been found
in models of many natural systems, for example from neuroscience [16, 17], population dynamics
[18] and game theory [19]. The dynamics near a network attractor looks like a long transient:
trajectories spend long periods of time close to one state before switching to another. Such
transient dynamics have been observed for neural processes at a variety of levels of description
[20] and examples ranging from olfactory processing in the zebraﬁsh [21] to human working
memory [22] have been successfully modeled using heteroclinic cycles or networks.
Similar
networks with noise have previously been shown to produce non-Markovian dynamics [23, 15].
Given the powerful capacities of network attractors to model transient dynamics at diﬀerent
levels these are a promising candidate to model EEG microstate sequences.
The transition probabilities and residence times in the EEG microstates sequence are mod-
eled using SDEs that possess such a noisy network attractor, which is excitable (as described
above) in the absence of noise.
The noisy network attractor captures statistical properties
2


## Page 3


of the observed microstate sequences including the distributions of residence times in each mi-
crostate and the transition probabilities. We apply this model to the analysis of EEG microstate
sequences obtained from resting state EEG recordings reported in [13]. We show that the distri-
butions of times spent in each microstate best ﬁt a sum of exponentials, and so the transitions
are non Markov. We construct one and two layer models and apply each model to microstate
sequences. We demonstrate that the one layer model produces a single exponential distribution
of residence times with the same local transition probabilities as the data but no LRD. We
further show that the double layer model is required to achieve distributions that are a sum
of exponentials that capture both the local transition probabilities, distribution of dwell times
and LRD and provides hence a better ﬁt to the data.
Methods
Data collection
Detailed description of the procedures used to collect the EEG recordings and convert them
into microstates are given in [13]; here we provide a brief summary for completeness.
Subjects and Procedure
Nine healthy volunteers (24 – 33 years, mean age 28.37 years) participated for monetary com-
pensation after giving informed consent approved by the ethics commission of the University
Hospital of Geneva. None suﬀered from current or prior neurological or psychiatric illness or
from claustrophobia. For each subject, we recorded one 5-minute session outside the scanner
prior to recording three 5-minute runs of resting-state EEG inside the MRI scanner. Subjects
were instructed to relax and rest with their eyes closed without falling asleep and to move as
little as possible. Data from one subject had to be excluded due to subsequent self-report of
sleep and the presence of sleep patterns in the EEG, and the data from the remaining eight
subjects were submitted to further analysis.
EEG Recording
The EEG was recorded from 64 sintered Ag/AgCL electrodes mounted in an elastic cap and
arranged in an extended 10-10 system. The electrodes were equipped with an additional 5kΩre-
sistor, and impedances were kept below 15kΩ. The EEG was digitized using a battery-powered
and MRI-compatible EEG system (BrainAmp MR plus, Brainproducts) with a sampling fre-
quency of 5 kHz and a hardware bandpass ﬁlter of 0.016 – 250 Hz with the midline fronto-central
electrode as the physical reference. The ampliﬁer was placed ca. 15 cm outside the magnet
bore and data were transmitted via ﬁberoptic cables to the recording computer placed outside
the scanner room.
EEG Data Preprocessing
Three types of artifacts were removed for data recorded inside the scanner: ﬁrst, gradient
artifacts were removed using a sliding average [24] and then the EEG was down-sampled to
500 Hz and low-pass ﬁltered with a ﬁnite-impulse response ﬁlter with a low-pass of 70 Hz.
Next, the ballistocardiographic (BCG) artifact was removed using a sliding average and ﬁnally,
independent component analysis (ICA) was used to remove the residual BCG artifact along with
oculomotor and myogenic artifacts. Data recorded outside the scanner were ﬁrst downsampled
to 500 Hz and subsequently, oculo-motor and myogenic artifacts were removed using ICA.
Finally, both the EEG recorded inside and outside the scanner was further downsampled to 125
Hz and bandpass ﬁltered between 1 and 40 Hz.
3


## Page 4


EEG Microstates
The Global Field Power (GFP) is a measure of the overall strength of the scalp electrical ﬁeld.
Between the local troughs of the GFP, the scalp topography remains stable and only varies in
strength. Hence, the local peaks of the GFP are the best representative of an EEG microstate.
We extracted the EEG at all local peaks of the GFP and submitted those to a modiﬁed Atomize-
Agglomerate Hierarchical (AAHC) clustering method [25] in order to determine the best solution
representing the most dominant topographies. The best solution was identiﬁed using a cross-
validation criterion [26], a measure of residual variance, which identiﬁed four template maps as
the optimal solution in each run. Finally, we computed the spatial correlation between the four
dominant template maps of the optimal solution and the continuous EEG data using a temporal
constraint criterion of 32 ms to obtain the time-course of the dominant EEG microstates.
In total we process and analyze 8 recordings outside the scanner and 24 recordings inside
the scanner. We convert the resting state EEG into time series where each time point of the
recording is classiﬁed into one of the four classically identiﬁed microstates [6, 7, 5]. The raw
data is ﬁrst cleaned to remove oculo-motor and other artifacts, and resampled at 125Hz. For
each time point of the cleaned data we computed the global ﬁeld potential
G(t) =
rPn
i=1(vi(t) −¯v(t))2
n
where vi(t) is the voltage of channel i and ¯v(t) is the voltage mean. The EEG topography at the
local maxima of the G has a good signal to noise ratio and so we take these points as momentary
maps. All momentary maps then undergo a clustering analysis to identify the four dominant
map topographies, these are the microstates. The four microstates are shown in Figure 1B.
Finally, each time point of the (resampled) recording is classiﬁed into one of the four possible
microstates.
EEG Microstate Sequence Analysis
We denote the sequence of microstates m(t) where m ∈{1, 2, 3, 4} at any given sampling time
point t. We classify m(t) into epochs of the same state deﬁned by saying that we enter a new
epoch if and only if t = 0 or m(t + 1) ̸= m(t).
Analogous to the model output, we describe the kth epoch in terms of its state σ(k) and
residence time ρ(k) respectively. This means we choose the unique sequence such that if
k−1
X
i=1
ρ(i) < j ≤
k
X
i=1
ρ(i)
then m(j) = σ(k) and moreover σ(k) ̸= σ(k + 1) (there is a change of state at the end of each
epoch).
Speciﬁcally, we deﬁne
• R(t) is the distribution of residence times ρ(k) for all epochs k.
• T(m, j) is the probability of transition from an epoch in state m to one in state j,
T(m, j) = #{k : σ(k) = m and σ(k + 1) = j}
#{k : σ(k) = m}
.
We call the sequence of nodes visited σ(k) the transition process, and a sequence of residence
times ρ(k) the renewal process. These processes are essentially independent. The state tran-
sition process is often represented as a transition matrix containing the probabilities T. Each
probability only depends on the state that you are currently in. In the case that the renewal
4


## Page 5


0
100
200
300
400
500
0
1
pj
0
100
200
300
400
500
Time
-1
0
1
yj
p2
p4
p1
p3
y1
y2
y8
y3
y4
y5
y6
y7
y9
y10
y11
y12
C
A
B
D
Figure 1: Structure and dynamics of the excitable network model. A The four canonical
microstates. B The coupling architecture of the sixteen-cell network. Each node represents one
of the microstates shown in panel A. C Time series of the p-cells (nodes), note at most only
one node is equal to one at any given time point. D Time series of the y-cells (edges). The
edges only become active (non-zero) during transitions between nodes.
process is memoryless, the whole process can be seen as Markov jump process, but it is possible
for the transitions to be Markov but the renewal process to be non-Markov. In the latter case
the distribution of residence times would be not be a simple exponential.
The average number of epochs per recording for outside is 2010, and for inside is 3031. We
compute R by plotting a histogram of the residence times for each recording, then ﬁnd the
average and standard error of each bin over all recordings in that group (outside or inside).
Similarly we calculate T for each recording and ﬁnd the average and standard error for each
probability.
Mathematical models
Single-layer network model
We aim to build a model that captures the statistical properties of the transition and renewal
processes. To this end, we construct a model of stochastic diﬀerential equations perturbed by
low amplitude additive white noise, using a general method that allows us to realize any desired
graph as an attracting heteroclinic or excitable network in phase space. This model has evolved
from work in [27] and is detailed in [15] so we brieﬂy outline the construction.
We realize the network of all possible transitions between the four canonical microstates
as an excitable network with four nodes (p-cells). There is an edge between two nodes in the
network if there can be transition between the two corresponding microstates; here the network
is all-to-all connected with twelve edges (y-cells). The coupling architecture of the network and
corresponding microstates are shown in Figure 1A–B.
The system is given by:
τdpj = [f(pj, y)] + ηpdwj
τdyk =
h
g
 yk, A −Bp2
α(k) + C(y2 −y2
k)
i
dt + ηykdwk
(1)
5


## Page 6


for j = 1, · · · , M and k = 1, · · · , Q. The functions f and g are deﬁned by
f(pj, y) = pj
 F
 1 −p2
+ D
 p2
jp2 −p4
+ E

−Z(o)
j (p, y) + Z(i)
j (p, y)

,
(2)
g(yk, λ) = −yk
 (y2
k −1)2 + λ

,
(3)
where
p2 =
M
X
j=1
p2
j,
p4 =
M
X
j=1
p4
j,
y2 =
Q
X
j=1
y2
j
and the outputs (O) and inputs (I) to the p cells from the y cells are:
Z(O)
j
(p, y) =
X
{k : α(k)=j}
y2
kpω(k)pj
Z(I)
j
(p, y) =
X
{k′ : ω(k′)=j}
y2
k′p2
α(k′).
(4)
The w are independent identically distributed noise processes, η are noise weights and A, B, C, D, E, F
are constants. Here we introduce the time scaling τ because although the p cells can be scaled
by the parameters the y cells have a functional form which is ﬁxed. The full equations are given
in S1 Appendix.
The pj variables classify which node of the network (i.e. which of the four microstates) is
visited. In the system with no noise, there are equilibrium solutions with pj = 1 and all other
coordinates zero. The yk variables become non-zero during a transition between nodes.
We use the parameter set
A = 0.5, B = 1.49, C = 2, D = 10, E = 4, F = 2
(5)
throughout as in [15], where B < 1.5 gives an excitable network.
In an excitable network
nodes are stable equilibria and transitions between nodes are driven by the additive noise. The
transition rates between nodes are modulated by the noise levels on the edges (rather than on
the nodes) as described in [15]. We choose the noise levels so that the model statistics, namely
the transition probabilities the distribution of the renewal process (residence times) ﬁt the data;
see Model simulation and ﬁtting for details. We ﬁx the noise on the nodes ηp = 10−4. The time
scaling constant τ is set to 8ms (in line with the sampling rate of the data) throughout.
Figures 1C–D show example time series output for the nodes and the edges, respectively,
for the excitable network model. At any given moment in the time series the trajectory in the
simulation is close to one of the equilibrium solutions, and one of the pj variables is close to
1. To determine where the trajectory is close to a given node we deﬁne a box in phase space
around that node so that when the trajectory is in the box we say it is near the node. Here we
ﬁx the box size H = 0.49 such that each box contains one node and the boxes do not overlap.
The duration of time spent in the box is then the residence time for that node [15].
The output of the model simulation is a series of k epochs where each epoch is deﬁned by
the state it is in σ ∈{1, 2, 3, 4} and its residence time ρ. The transition and renewal processes
generated by the network construction given here are both Markov. Due to the evidence of
multi-scale behavior of the temporal dynamics of microstate sequences [28, 13] we also present
a more sophisticated model a with a multi-layer construction that will generate a non-Markov
renewal process.
Multi-layer network model
We construct a system of N levels, where each level l has Ml nodes, and we assume all-to-all
connections, so we thus have Ql ≡Ml(Ml −1) edges. In each level, we set up a system of SDEs
6


## Page 7


in the form of that described in [15], as follows, where pl,j ∈RMl and yl,k ∈RQl:
τdpl,j = [fl(pj, y)] dt + ηpdw
τdyl,k =

gl(yk, pα(k)) + zl,k

dt + ηl,kdwk.
(6)
Here we allow for a general input into the y-cells zl,k(t) that linearly couples layers from the pl
nodes to the yl+1,k edges by:
zl+1,k =
Ml
X
j=1
ζl,j p2
l,j.
The parameter ζl,j is a constant that scales the activity from node pl,j to all the edges in level
l + 1. The functions f, g, Z(O) and Z(I) are analogous to those in the single layer model,
fl(pj, y) = pl,j
 F(1 −p2
l ) + D(p2
l,jp2
l −p4
l )

+ E

−Z(O)
l,j (p, y) + Z(I)
l,j (p, y)

,
gl(yk, pα(k)) = −yl,k

(y2
l,k −1)2 + A −Bp2
l,α(k) + C(y2
l −y2
l,k)

,
for j = 1, . . . , Ml and k = 1, . . . , Ql,
Z(O)
l,j (p, y) =
X
{k : α(k)=j}
y2
l,kpl,ω(k)pl,j
Z(I)
l,j (p, y) =
X
{k′ : ω(k′)=j}
y2
l,k′p2
l,α(k′),
(7)
and
p2
l =
Ml
X
j=1
p2
l,j,
p4
l =
Ml
X
j=1
p4
l,j,
y2
l =
Ql
X
k=1
y2
l,k.
We consider in particular a two layer model where M1 = 2 and M2 = 4 and the constants
A, B, C, D, E, F are set as (5) for each layer. Note that both layers are excitable networks.
Layer one with two nodes is a “hidden layer" and we only consider the output from layer 2 with
four nodes. As before the output is a transition process and a renewal process.
Figure 2A shows the coupling architecture for the two layer model, B–C show the time
series of the nodes and edges in layer one, respectively, and D–E show the time series of the
nodes and edges in layer two, respectively. Compare layer two topography and dynamics to
Figure 1.
The two nodes in layer one eﬀect the dynamics on the edges (and therefore the
residence times) in layer two by the scalings ζ1,1 = ζ1 and ζ1,2 = ζ2. These scale the dwell times
in the renewal process output from layer two. For illustrative purposes we choose ζ1 = 10−1
and ζ2 = 10−3 here. Panels B–E clearly show that when p1,2 = 1 the residence times at each
node p2,j are longer (transitions between nodes are less frequent) as the edges in layer two y2,k
are scaled by ζ2. Note that if ζ1 = ζ2 layer one would be redundant as the residence times
would be consistent (drawn from the same distribution) in either node and the renewal process
would again be Markov.
Model simulation and ﬁtting
We wish to use the model capture the transition probabilities and distribution of residence
times of the data. To this end we ﬁrst ﬁt exponential curves to the residence distributions for
the data recorded inside and outside the fMRI scanner. Speciﬁcally, we compute the histogram
of residence times from the microstate sequences for bin size 40. The distribution is truncated
7


## Page 8


0
400
800
1200
1600
0
1
0
400
800
1200
1600
0
0
400
800
1000
1200
1600
0
1
0
400
800
1200
1600
0
2
1
layer 1
layer 2
p1,1
p1,2
y1,1
y1,2
p2,2
p2,4
p2,1
p2,3
y1
y2
y8
y3
y4
y5
y6
y7
y9
y10
y11
y12
C
A
B
D
E
Time
p
y
p
y
2,j
2,k
1,k
1,j
Figure 2: Structure and dynamics of a two-layer model. A The coupling architecture of
the two networks. Compare layer two to Figure 1B. Example time series are shown for layer
one nodes B and edges C, layer two nodes D and edges E. The noise on all edges ηl,k = 10−2
is ﬁxed, residence times are scaled by ζ1 = 0.1 and ζ2 = 0.001. When p1,2 = 1 in panel A the
noise on the edges in layer two is scaled by ζ2 and residence times of nodes in layer two, shown
in panel D, are much longer than when p1,1 = 1.
at the ﬁrst empty bin. We then use the fit function in Matlab to ﬁt the single and double
exponentials
E(1)(t) = A1 exp(−k1t),
E(2)(t) = A1 exp(−k1t) + A2 exp(−k2t),
(8)
to each dataset where we constrain Ai > 0 and ki ≥0. We use an F-test to indicate whether
the double exponential was a better ﬁt to the data; code used as written for [29].
We numerically simulate the one and two-layer models with a stochastic Heun method
implemented using a custom code written in Matlab. We compute 10 realizations of the model
using step size 0.05 up to maximum of 100,000 steps. This gives approximately 5750 epochs per
realization. We calculate the residence time distribution R and transition probabilities T, then
average the values over 10 realizations. The results of the averaged simulations (model output)
are compared by eye to the data.
To ﬁt the one-layer model output to the data we adjust the noise amplitude parameters on
the edges ηyk. The noise amplitude on each edge controls the probability of transition along that
edge, therefore we change the amplitudes so the model output transition probabilities are within
the error bars of the transition probabilities from the data. For example if T(1, 2) > T(2, 1)
then we set ηy1 > ηy4. The overall magnitude of the ηyk parameters controls the decay rate of
the residence time distribution. If all ηyk are large, for example, O(10−1) transitions happen
quickly, the residence times are short, and the decay rate of the distribution R is large (slope is
steep); whereas if ηyk are small, for example, O(10−4) there are long residence times between
8


## Page 9


transitions and the decay rate is small (slope is shallow). In this way we can ﬁt the distribution
of the model to the ﬁtted curves E(1)(t).
To ﬁt the transition probabilities in the two-layer model we adjust the noise values of
the edges in layer two η2,k in the same way as for the one-layer model. To ﬁt the residence
distributions we ﬁrst ﬁx the overall magnitude of the η2,k in line with the one-layer model, then
adjust the transfer parameters ζj and noise values of the edges on layer one η1,k. Changing ζj
changes the dynamics on the edges of layer two in a homogeneous way (the same scaling on
all edges): if ζ is increased the residence times decrease and the decay rate of the distribution
is becomes larger; if ζ is decreased, the decay rate of the distribution of the residence times is
decreased. As there are two transfer parameters (one for each node in layer one) the residence
distribution of the output from the model is a linear combination of the two decay rates; one ζ
is associated with the distribution at short times and the other captures the heavy tails. The
proportion of each distribution (the mixing) is controlled by the noise on the edges is layer
one. If η1,1 > η1,2 more time will be spent in node p1,2 than in node p1,1 so in the residence
distribution there will be a larger proportion of the decay rate associated with ζ2. In this way
we can ﬁt the distribution of the model to the ﬁtted curves E(2)(t).
Results
Microstate residence time distributions have two phase decay
The residence time distributions R(t) for data collected inside and outside the scanner and the
transition probabilities T(m, j) for the EEG recordings are shown in Figure 3. The distributions
R(t) are plotted on a logarithmic scale with E(1)(t) and E(2)(t) given by (8). The transition
probabilities for each dataset are shown in panels C.
For each dataset we perform a comparison of ﬁts of E(1) and E(2) to the data. We ﬁnd that an
F-test rejects the null hypothesis that the distribution is E(1): details are given in Table 1. Using
the Kruskall-Wallis ANOVA the mean rank fo the residence time distributions are signiﬁcantly
diﬀerent (p < 0.0005). Signiﬁcant diﬀerences in transition probabilities between outside and
inside can be seen between in the transition from state 1 to state 2, and from state 4 to state
2. Note there are no self transitions due to our deﬁnition of an epoch.
Table 1:
Two phase decay captures residence time distributions.
E(1)
Outside
Inside
A1
3.523 × 10−2
4.931 × 10−2
k1
1.828 × 10−2
2.119 × 10−2
E(2)
Outside
Inside
A1
4.111 × 10−2
5.141 × 10−2
k1
2.340 × 10−2
2.620 × 10−2
A2
2.617 × 10−3
6.611 × 10−3
k2
6.249 × 10−3
1.198 × 10−2
F(dn, dd)
5685(2, 32)
1105(2, 32)
Preferred
E(2)
E(2)
Best ﬁt parameters for one-phase decay E(1) and two-phase decay E(2) as in (8). The ﬁnal
rows give the F-test results with threshold α = 0.05.
9


## Page 10


Figure 3: Statistical properties of the recordings and curve ﬁtting. Top row shows
histograms of residence times for the microstate sequences outside and inside the scanner, with
bin size 40. Note the data is truncated at the ﬁrst empty bin. The best ﬁt curves for one-
phase decay E(1) and two-phase decay E(2) are shown for each distribution. The bottom four
panels show the probability of transition T(m, j) from state m to state j for each microstate
m = 1, 2, 3, 4. Signiﬁcant diﬀerences p < 0.05 are denoted with a star.
One-layer network model captures transition probabilities
The results of ﬁtting the one-layer model to the data from outside the scanner are shown in
Figure 4. The single exponential ﬁt E(1) from Table 1 is shown. The transition probabilities for
the model and the data show a good ﬁt as the model probabilities are within the error bars of
the data for all transitions. The noise weights ηyk used are given in Table 2. The distribution of
the one-layer model aligns with E(1). However, this model fails to capture the two decay rates
observed in the data.
Two-layer model captures two-phase decay of residence times
The results of ﬁtting the two-layer model to the data from outside the scanner are shown in
Figure 5 with the double exponential ﬁt E(2) from Table 1. The distributions of the simulations
agree closely with E(2) and ﬁt within the error bars of the distribution. The transition proba-
bilities for the model and data are also shown. The parameters for the simulations are shown
in Table 3. The two layer model captures the two-phase decay of the data.
10


## Page 11


Figure 4: One-layer model captures transition probabilities. One-layer model simulation
(purple) with residence distribution for the ‘outside’ dataset (blue) in the top panel. The single
and double exponential ﬁts from Table 1 are shown for comparison (black dashed lines). The
transition probabilities T(m, j) are shown below for both the data (blue) and the simulation
(purple). The parameters used in the simulations in each panel are given in Table 2. There is
good agreement between the model transition probabilities and the data as this was our ﬁtting
criteria. The residence time distribution of the model closely follows the single exponential ﬁt
to the data but does not capture the data distribution well at all.
Discussion
In this article we have demonstrated a new modelling approach applied to capture the statistical
properties of the temporal dynamics of EEG microstates. We analyze EEG microstate sequences
from EEG data recorded inside and outside an fMRI scanner, previously reported in [12, 13]. We
consider the transition probabilities between microstates and the distributions of the residence
times.
We show that there are signiﬁcant diﬀerences between the residence time distributions.
Both residence time distributions are best ﬁt by two decay rates. We note the similarity in the
ﬁrst decay rates given by 2.340 × 10−2 and 2.620 × 10−2 for outside and inside respectively.
However, the second decay rate is very diﬀerent 6.249 × 10−3 and 1.198 × 10−2 for outside
and inside respectively. We also see a change in the transition probabilities; the inside dataset
transition probabilities have less variance than the outside dataset, with a signiﬁcant increase
of the probability of transition to microstate 2 from microstates 1 and 4.
The most likely
explanation for the diﬀerence in long-range temporal correlation for the data recorded inside and
outside the scanner is the diﬀerence in artifact removal. The data recorded outside the scanner
11


## Page 12


Table 2: Parameters for the one-layer model.
ηy1
ηy2
ηy3
ηy4
ηy5
ηy6
0.0272
0.0324
0.0286
0.0301
0.0329
0.0284
ηy7
ηy8
ηy9
ηy10
ηy11
ηy12
0.0276
0.0269
0.0278
0.0290
0.0270
0.0328
The noise values on the edges ηyk are given for the model simulation to ﬁt the ‘outside’
dataset shown in Figure 4.
Table 3: Parameters for the two-layer model.
ζ1
ζ2
η1,1
η1,2
0.19
0.0001
0.05
0.05
η2,1
η2,2
η2,3
η2,4
η2,5
η2,6
0.00080
0.00230
0.00120
0.00150
0.00210
0.00110
η2,7
η2,8
η2,9
η2,10
η2,11
η2,12
0.00138
0.00120
0.00138
0.00146
0.00080
0.00250
The noise values on the edges ηl,k are given for each layer l = 1, 2 with the transfer parameters
ζn for the model simulation shown in Figure 5. Compare the noise values on the edges of layer
two ηl,k to the values in Table 2.
were only contaminated by very occasional oculomotor artifacts (eye-movements) which can be
reliably detected and removed with ICA. EEG data recorded inside the scanner are additionally
contaminated by the gradient and the ballistocardiographic artifacts. The gradient artifact has
an amplitude three orders of magnitude larger than the EEG, but it is very regular and can thus
be removed reliably by a sliding average. The amplitude of the ballistocardiogram is roughly an
order of magnitude larger than the EEG, and its removal requires two steps: a sliding average
to remove the major amplitude and ICA to remove the residual. The latter is essential but also
prone to remove not only the residual artifacts but also to remove part of the signal.
In the past few years there have been various attempts to model EEG-microstate sequences.
Gärtner et al. [30] construct a hidden-Markov type stochastic model based on the transition
probabilities between microstates extracted from the data.
The transition matrix gives the
probabilities of moving from one state to another, where each probability only depends on
the state that you are currently in. Such a one-step Markov construction assumes that the
transitions between microstates depend on the current state but otherwise are memoryless.
However, no restrictions are placed on the distributions of the residence times.
The Markov model approach taken in [30] has been criticized for the underlying assumption
that the microstate transition process is independent of the underlying global ﬁeld power time
series [31]. Further, the authors do not comment on possible long range dependencies (LRDs)
in the data. Gschwind et al. argue that LRDs are an intrinsic property of neural dynamics
that manifest in the microstate sequences as scale-free or fractal structure in the data [28]. To
elucidate this fractal structure and verify and expand the work of [13] they subject the data to
a battery of tests, including computing the power spectral density and Hurst exponents using
detrended ﬂuctuation analysis (DFA), a wavelet framework, and time-variance analysis. Using
wavelet detrended ﬂuctuation analysis EEG-microstate time series have been shown to exhibit
mono-fractal behavior over six dyadic scales indicative of long range [12].
Further analysis of scale-free properties in EEG-microstate data, subsequently conducted
by von Wegner et al., shows that these measures, when applied to real (instead of simulated)
12


## Page 13


Figure 5: Two-layer model captures longer residence times. The distribution for the
‘outside’ dataset (blue) with the residence time distributions from the simulation of the two-
layer model (purple); see Figure 2. The parameters used in the simulations in each panel are
given in Table 3. The double exponential ﬁt E(2) from Table 1 is also shown. The two layer
model ﬁts the transition probabilities well as this was the ﬁtting criteria. The model simulations
ﬁt the two decay rates of the residence time distribution of the data capturing both long and
short times.
EEG-data, do not guarantee the existence of LRDs [14]. Speciﬁcally, they compute the Hurst
exponent of a given EEG-microstates data set using three diﬀerent methods and perform sta-
tistical tests that show that the results are not always signiﬁcantly diﬀerent from a constructed
white noise process. The assumptions underlying the analysis that provide a connection be-
tween the Hurst exponent and long range dependencies in data and therefore temporal fractal
structure, may also not be applicable to real EEG-data.
That the microstate residence times presented here are best represented by two decays rates
provides additional evidence that the temporal properties of microstates are non-Markovian in
line with [28]. It is clear that Markovian or single parameter LRD models do not adequately
represent the temporal dynamics of microstate sequences [14].
One limitation of this approach is that we only consider memoryless transitions, and assume
that the transition probabilities do not change over time. These assumption may be incorrect as
they do not ﬁt with the non-Markovian properties of microstate sequences previously found [13].
Future work would be to look at transition probabilities of sequences of microstates, thereby
including diﬀerent levels of history.
Combined fMRI-EEG studies have found correlates between each microstate and resting
state networks [13]; A is the auditory network, B is the visual network, C is the saliency network
13


## Page 14


and D is the attention network. The switching dynamics between microstates indicates changes
in switching between these underlying neural networks [12].
Multiple decay rates point to
complex switching dynamics required for cognition. More work needs to be done to understand
how these dynamic changes correlate to the cognitive dysfunction observed in this state, for
example loss of short term memory.
Finally this modelling approach could be used to identify dynamic diﬀerences and their
brain network correlates at diﬀerent levels of consciousness and in other neurological disorders
for example Alzheimer’s disease, epilepsy and schizophrenia.
Conclusions
Using EEG data from [13] we show that the residence time distributions of resting state EEG
microstate sequences have a two phase decay. We also show that the additional processing
of the data recorded inside the fMRI scanner leads to a decrease of very long residence times
(> 900ms) in the distribution. Using the construction outlined in [15] we build systems of
stochastic diﬀerential equations (SDE) that have a “noisy network attractor”. Using a one-
layer model we show that this captures the transition probabilities between microstates. The
distribution given by this model is (single) exponential. We also build a two-layer model with
a (hidden) layer containing two nodes each associated with a transfer parameter that scales
the behavior of the edges in the four-node network layer. This model produces a residence
time distribution with two decay rates (sum of two exponentials) that better captures the two-
phase decay seen in the data. The identiﬁcation of EEG-microstates as correlates of resting
state brain networks means that analysis of the temporal dynamics of microstate sequences can
lead to crucial insights into the switching between these networks required for cognition and
perception in resting state and could provide indicators of underlying mechanisms of dynamic
changes characteristic of neurological disorders.
Supporting information
S1 Appendix.
Single-layer model equations.
Acknowledgements
JC and PA gratefully acknowledge the ﬁnancial support of the EPSRC Centre for Predictive
Modelling in Healthcare, via grant EP/N014391/1. JC acknowledges funding from MRC Skills
Development Fellowship MR/S019499/1. CMP acknowledges funding from the Marsden Fund,
Royal Society of New Zealand.
References
[1] Damoiseaux J, Rombouts S, Barkhof F, Scheltens P, Stam C, Smith SM, et al. Consistent
resting-state networks across healthy subjects. Proceedings of the national academy of
sciences. 2006;103(37):13848–13853.
[2] Mantini D, Perrucci MG, Del Gratta C, Romani GL, Corbetta M. Electrophysiological
signatures of resting state networks in the human brain.
Proceedings of the National
Academy of Sciences. 2007;104(32):13170–13175.
[3] Deco G, Jirsa VK, McIntosh AR. Emerging concepts for the dynamical organization of
resting-state activity in the brain. Nature Reviews Neuroscience. 2011;12(1):43–56.
14


## Page 15


[4] Lehmann D.
Past, present and future of topographic mapping.
Brain Topography.
1990;3(1):191–202.
[5] Wackermann J, Lehmann D, Michel C, Strik W. Adaptive segmentation of spontaneous
EEG map series into spatially deﬁned microstates. International Journal of Psychophysi-
ology. 1993;14(3):269–283.
[6] Koenig T, Prichep L, Lehmann D, Sosa PV, Braeker E, Kleinlogel H, et al.
Millisec-
ond by millisecond, year by year: normative EEG microstates and developmental stages.
Neuroimage. 2002;16(1):41–48.
[7] Strik W, Lehmann D.
Data-determined window size and space-oriented segmentation
of spontaneous EEG map series.
Electroencephalography and clinical neurophysiology.
1993;87(4):169–174.
[8] Lehmann D, Faber PL, Galderisi S, Herrmann WM, Kinoshita T, Koukkou M, et al. EEG
microstate duration and syntax in acute, medication-naive, ﬁrst-episode schizophrenia: a
multi-center study. Psychiatry Research: Neuroimaging. 2005;138(2):141–156.
[9] Nishida K, Morishima Y, Yoshimura M, Isotani T, Irisawa S, Jann K, et al. EEG mi-
crostates associated with salience and frontoparietal networks in frontotemporal dementia,
schizophrenia and Alzheimer’s disease. Clinical Neurophysiology. 2013;124(6):1106–1114.
[10] Tomescu MI, Rihs TA, Roinishvili M, Karahanoglu FI, Schneider M, Menghetti S, et al.
Schizophrenia patients and 22q11. 2 deletion syndrome adolescents at risk express the
same deviant patterns of resting state EEG microstates: a candidate endophenotype of
schizophrenia. Schizophrenia Research: Cognition. 2015;2(3):159–165.
[11] Lehmann D, Strik W, Henggeler B, König T, Koukkou M. Brain electric microstates and
momentary conscious mind states as building blocks of spontaneous thinking: I. Visual
imagery and abstract thoughts. International Journal of Psychophysiology. 1998;29(1):1–
11.
[12] Britz J, Van De Ville D, Michel CM. BOLD correlates of EEG topography reveal rapid
resting-state network dynamics. Neuroimage. 2010;52(4):1162–1170.
[13] Van de Ville D, Britz J, Michel CM.
EEG microstate sequences in healthy humans
at rest reveal scale-free dynamics.
Proceedings of the National Academy of Sciences.
2010;107(42):18179–18184.
[14] von Wegner F, Tagliazucchi E, Brodbeck V, Laufs H. Analytical and empirical ﬂuctua-
tion functions of the EEG microstate random walk-Short-range vs. long-range correlations.
NeuroImage. 2016;141:442–451.
[15] Ashwin P, Postlethwaite C. Designing heteroclinic and excitable networks in phase space
using two populations of coupled cells. Journal of Nonlinear Science. 2016;26(2):345–364.
[16] Ashwin P, Karabacak Ö, Nowotny T. Criteria for robustness of heteroclinic cycles in neural
microcircuits. The Journal of Mathematical Neuroscience. 2011;1(1):13.
[17] Chossat P, Krupa M.
Heteroclinic cycles in Hopﬁeld networks.
Journal of Nonlinear
Science. 2016;26(2):315–344.
[18] Meyer-Ortmanns H, Voit M. From structural to temporal and spatial hierarchies in hete-
roclinic networks. Bulletin of the American Physical Society. 2019.
15


## Page 16


[19] Aguiar MA. Is there switching for replicator dynamics and bimatrix games? Physica D:
Nonlinear Phenomena. 2011;240(18):1475–1488.
[20] Hutt A, beim Graben P.
Sequences by Metastable Attractors: Interweaving Dynami-
cal Systems and Experimental Data.
Frontiers in Applied Mathematics and Statistics.
2017;3(11):1–14.
[21] Friedrich RW, Laurent G. Dynamic optimization of odor representations by slow temporal
patterning of mitral cell activity. Science. 2001;291(5505):889–894.
[22] Bick C, Rabinovich MI. Dynamical origin of the eﬀective storage capacity in the brain’s
working memory. Physical Review Letters. 2009;103(21):218101.
[23] Armbruster D, Stone E, Kirk V. Noisy heteroclinic networks. Chaos: An Interdisciplinary
Journal of Nonlinear Science. 2003;13(1):71–79.
[24] Allen PJ, Josephs O, Turner R. A Method for Removing Imaging Artifact from Continuous
EEG Recorded during Functional MRI. NeuroImage. 2000;12(2):230–239.
[25] Tibshirani R, Walther G. Cluster Validation by Prediction Strength. Journal of Compu-
tational and Graphical Statistics. 2005;14(3):511–528.
[26] Pascual-Marqui RD, Michel CM, Lehmann D. Segmentation of brain electrical activity
into microstates: model estimation and validation.
IEEE Transactions on Biomedical
Engineering. 1995;42(7):658–665.
[27] Ashwin P, Postlethwaite C. On designing heteroclinic networks from graphs. Physica D:
Nonlinear Phenomena. 2013;265:26–39.
[28] Gschwind M, Michel CM, Van De Ville D.
Long-range dependencies make the diﬀer-
ence—Comment on “A stochastic model for EEG microstate sequence analysis”. NeuroIm-
age. 2015;117:449–455.
[29] Anderson KB, Conder JA. Discussion of multicyclic Hubbert modeling as a method for
forecasting future petroleum production. Energy & Fuels. 2011;25(4):1578–1584.
[30] Gärtner M, Brodbeck V, Laufs H, Schneider G. A stochastic model for EEG microstate
sequence analysis. Neuroimage. 2015;104:199–208.
[31] Koenig T, Brandeis D. Inappropriate assumptions about EEG state changes and their
impact on the quantiﬁcation of EEG state dynamics—Comment on “A stochastic model
for EEG microstate sequence analysis”. NeuroImage. 2015;125:1104–1106.
16

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
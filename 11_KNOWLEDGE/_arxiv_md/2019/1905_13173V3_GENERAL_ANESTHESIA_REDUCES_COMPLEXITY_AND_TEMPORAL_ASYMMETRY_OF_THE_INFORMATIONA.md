---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.13173v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1905.13173v3_General_anesthesia_reduces_complexity_and_temporal_asymmetry_of_the_informationa

> Source: 1905.13173v3_General_anesthesia_reduces_complexity_and_temporal_asymmetry_of_the_informationa.pdf

> Pages: 14

---


## Page 1


Accepted in Physical Review Research 3 April, 2020. Click title to verify. Published under CC-BY 4.0.
General anaesthesia reduces complexity and temporal asymmetry of the informational structures
derived from neural recordings in Drosophila
Roberto N. Muñoz,1, ∗Angus Leung,2, † Aidan Zecevik,1, ‡ Felix A. Pollock,1, §
Dror Cohen,3, 4, ¶ Bruno van Swinderen,5, ∗∗Naotsugu Tsuchiya,4, 6, 3, †† and Kavan Modi1, ‡‡
1School of Physics & Astronomy, Monash University, Clayton, Victoria 3800, Australia
2School of Psychological Sciences, Monash University, Clayton, Victoria 3800, Australia
3Center for Information and Neural Networks (CiNet),
National Institute of Information and Communications Technology (NICT), Suita, Osaka 565-0871, Japan
4School of Psychological Sciences and Turner Institute for Brain and Mental Health,
Monash University, Melbourne, Victoria 3800, Australia
5Queensland Brain Institute, The University of Queensland, St Lucia, Queensland 4072, Australia
6Advanced Telecommunications Research Computational Neuroscience Laboratories,
2-2-2 Hikaridai, Seika-cho, Soraku-gun, Kyoto 619-0288, Japan
(Dated: June 4, 2020)
We apply techniques from the ﬁeld of computational mechanics to evaluate the statistical complexity of
neural recording data from fruit ﬂies. First, we connect statistical complexity to the ﬂies’ level of conscious
arousal, which is manipulated by general anaesthesia (isoﬂurane). We show that the complexity of even single
channel time series data decreases under anaesthesia. The observed difference in complexity between the two
states of conscious arousal increases as higher orders of temporal correlations are taken into account. We then
go on to show that, in addition to reducing complexity, anaesthesia also modulates the informational structure
between the forward and reverse-time neural signals. Speciﬁcally, using three distinct notions of temporal
asymmetry we show that anaesthesia reduces temporal asymmetry on information-theoretic and information-
geometric grounds. In contrast to prior work, our results show that: (1) Complexity differences can emerge
at very short time scales and across broad regions of the ﬂy brain, thus heralding the macroscopic state of
anaesthesia in a previously unforeseen manner, and (2) that general anaesthesia also modulates the temporal
asymmetry of neural signals. Together, our results demonstrate that anaesthetised brains become both less
structured and more reversible.
I.
INTRODUCTION
Complex phenomena are everywhere in the physical world.
Typically, these emerge from simple interactions among ele-
ments in a network, such as atoms making up molecules or
organisms in a society. Despite their diversity, it is possible
to approach these subjects with a common set of tools, using
numerical and statistical techniques to relate microscopic de-
tails to emergent macroscopic properties [1]. There has long
been a trend of applying these tools to the brain, the archety-
pal complex system, and much of neuroscience is concerned
with relating electrical activity in networks of neurons to psy-
chological and cognitive phenomena [2]. In particular, there
is a growing body of experimental evidence [3], that neural
ﬁring patterns can be strongly related to the level of conscious
arousal in animals.
In humans, level of consciousness varies from very low
in coma and under deep general anaesthesia, to very high
in fully wakeful states of conscious arousal [4]. With the
∗roberto.munoz@monash.edu
† angus.leung1@monash.edu
‡ aidanzecevik@gmail.com
§ felix.pollock@monash.edu
¶ dror.cohen@nict.go.jp
∗∗b.vanswinderen@uq.edu.au
†† naotsugu.tsuchiya@monash.edu
‡‡ kavan.modi@monash.edu
current technology, precise discrimination between uncon-
scious vegetative states and minimally conscious states are
particularly challenging and remains a clinical challenge [5].
Therefore, substantial improvement in accuracy of determin-
ing such conscious states using neural recording data will
have signiﬁcant societal impacts. Towards such a goal, neural
data has been analysed using various techniques and notions
of complexity to try to ﬁnd the most reliable measure of con-
sciousness [6, 7].
One of the most successful techniques to date in distin-
guishing levels of conscious arousal is the perturbational
complexity index [8–10], which measures the neural activity
patterns that follows a perturbation of the brain through mag-
netic stimulation. The evoked patterns are processed through
a pipeline then ﬁnally summarised using Lempel-Ziv com-
plexity [9]. This method is inspired by a theory of conscious-
ness, called integrated information theory (IIT) [11, 12],
which proposes that a high level of conscious arousal should
be correlated with the amount of so-called integrated infor-
mation, or the degree of differentiated integration in a neu-
ral system (see Ref. [13] for details). While there are vari-
ous ways to capture this essential concept [14, 15], one way
to interpret integrated information is as the amount of loss
of information a system has on its own future or past states
based on its current state, when the system is minimally dis-
connected [16–18].
These complexity measures, inspired by IIT, are motivated
by the fundamental properties of conscious phenomenology,
such as informativeness and integratedness of any experience
arXiv:1905.13173v3  [q-bio.NC]  3 Jun 2020


## Page 2


2
[11]. While there are ongoing efforts to accurately translate
these phenomenological properties into mathematical postu-
lates [13], such translation often contains assumptions about
the underlying process which are not necessarily borne out
in reality. For example, the derived mathematical postulates
in IIT assume Markovian dynamics, i.e., that the future evo-
lution of a neural system is determined statistically by its
present state [15]. Moreover, IIT requires computing the cor-
relations across all possible partitions between subsystems,
which is computationally heavy [16] in relation to methods
which do not require such partitioning to work. Assuming
that the hierarchical causal inﬂuences in the brain would man-
ifest as oscillations across a range of frequencies and spa-
tial regions [19], non-Markovian temporal correlations likely
play a signiﬁcant role in explaining any experimentally mea-
surable behaviours, including the level of conscious arousal.
There is therefore, scope for applying more general notions
of complexity to meaningfully distinguish macroscopic brain
states that support consciousness.
A conceptually simple approach to quantifying the com-
plexity of time series data, such as the ﬂuctuating potential
in a neuron, is to construct the minimal model which statisti-
cally reproduces it. Remarkably, this minimal model, known
as an epsilon machine (ϵ-machine), can be found via a sys-
tematic procedure which has been developed within the ﬁeld
of computational mechanics [20–22]. Crucially, ϵ-machines
account for multiple temporal correlations contained in the
data and can be used to quantify the statistical complexity of
a process – the minimal amount of information required to
specify its state. As such they have been applied over vari-
ous ﬁelds, ranging from neuroscience [23, 24] and psychol-
ogy [25] to crystallography [26] and ecology [27], to the stock
market [28]. Lastly, unlike IIT the ϵ-machine analysis can be
performed for data coming from a single channel.
In this paper, we use the statistical complexity derived from
an ϵ-machine analysis of neural activity to distinguish states
of conscious arousal in fruit ﬂies (D. melanogaster). We anal-
yse neural data collected from ﬂies under different concen-
trations of isoﬂurane [29, 30].
By analysing signals from
individual electrodes and disregarding spatial correlations,
we ﬁnd that statistical complexity distinguishes between the
two states of conscious arousal through temporal correlations
alone. In particular, as the degree of temporal correlations
increases, the difference in complexity between the wakeful
and anaesthetised states becomes larger. In addition to mea-
suring complexity, the ϵ-machine framework also allows us to
assess the temporal irreversibility of a process- the difference
in the statistical structure of the process when read forwards
vs. backwards in time. This may be particularly important
for wakeful brains which are thought to be sensitive to the
statistical structure of the environment which runs forward in
time [30–32]. Using the nuanced characterisation of temporal
information ﬂow offered by the ϵ-machine framework [33],
we then analyse the time irreversibility and crypticity of the
neural signals to further distinguish the conscious states. We
ﬁnd that the asymmetry in information structure between for-
ward and reverse-time neural signals is reduced under anaes-
thesia.
The present approach singularly differentiates between
highly random and highly complex information structure; ac-
counts for temporal correlations beyond the Markov assump-
tion; and quantiﬁes temporal asymmetry of the process. None
of the standard methods possesses all of these features within
a single uniﬁed framework. Before presenting these results in
detail in Sec. III and discussing their implications in Sec. IV,
we begin with a brief overview of the ϵ-machine framework
we will use for our analysis.
II.
THEORY: ϵ-MACHINES AND STATISTICAL
COMPLEXITY
To uncover the underlying statistical structure of neural ac-
tivity that characterises a given conscious state, we treat the
measured neural data, given by voltage ﬂuctuations in time,
as discrete time series. To analyse these time series, we use
the mathematical tools of computational mechanics, which
we outline in this section. We start with a general discus-
sion on the ways to use time series data to infer a model of
a system while placing ϵ-machines in this context. Next, we
explain how we construct ϵ-machines in practice. Finally, we
show how this can be used to extract a meaningful notion of
statistical complexity of a process.
A.
From time series to ϵ-Machines
In abstract terms, a discrete-time series is a sequence of
symbols r = (r0, . . . , rk, . . .) that appear over time, one af-
ter the other [34]. Each element of r corresponds to a sym-
bol from a ﬁnite alphabet A observed at the discrete time
step labelled by the subscript k. The occurrence of a sym-
bol, at a given time step, is random in general and thus the
process, which produces the time series, is stochastic [35].
However, the symbols may not appear in a completely in-
dependent manner, i.e., the probability of seeing a particular
symbol may strongly depend on symbols observed in the past.
These temporal correlations are often referred to as memory,
and they play an important role in constructing models that
are able to predict the future behaviour of a given stochastic
process [36].
Relative to an arbitrary time k, let us denote the future and
the past partitions of the complete sequence as r = (
⃗
r,⃗r),
where the past and the future are
⃗
r = (. . . , rk−2, rk−1) and
⃗r = (rk, rk+1, . . .) respectively. In general, for the prediction
of the immediate future symbol rk, knowledge of the past
ℓsymbols
⃗
rℓ:= (rk−ℓ, . . . , rk−2, rk−1), may be necessary.
The number of past symbols we need to account for in order
to optimally predict the future sequence is called the Markov
order [37].
In general, the difﬁculty of modelling a time series in-
creases exponentially with its Markov order. However, not
all distinct pasts lead to unique future probability distribu-
tions, leaving room for compression in the model. In a sem-
inal work, Crutchﬁeld and Young showed the existence of a
class of models, which they called ϵ-machines, that are prov-
ably the optimal predictive models for a non-Markovian pro-
cess under the assumption of statistical stationarity [20, 21].


## Page 3


3
Constructing the ϵ-machine is achieved by partitioning sets
of partial past observations
⃗
rℓinto causal states. That is, two
distinct sequences of partial past observations
⃗
rℓand
⃗
r′
ℓbe-
long to the same causal state Si ∈S, if the probability of
observing a speciﬁc ⃗r given
⃗
rℓor
⃗
r′
ℓis the same; that is
⃗
rℓ∼ϵ
⃗
r′
ℓ
if
P(⃗r |
⃗
rℓ) = P(⃗r |
⃗
r′
ℓ),
(1)
where ∼ϵ indicates that two histories correspond to the same
causal state.
The conditional probability distributions in
Eq. (1) may always be estimated from a ﬁnite set of statis-
tically stationary data via the naive maximum likelihood es-
timate, given by P(rk|
⃗
rℓ) = ν(rk,
⃗
rℓ)/ν(
⃗
rℓ), where ν(X) is
the frequency of occurrence of sub-sequence X in the data.
For the case of non-stationary data, the probabilities obtained
by this method will produce a non-minimal model that cor-
responds to a time-averaged representation of the time series.
We now discuss how to practically construct an ϵ-machine for
a given time series.
B.
Constructing ϵ-machines with the CSSR algorithm
Several algorithms have been developed to construct
ϵ-machines from time series data [20, 38, 39].
Here, we
brieﬂy explain the Causal State Splitting Reconstruction
(CSSR) algorithm [25], which we use in this work to infer
ϵ-machines predicting the statistics of neural data we provide
as input.
The CSSR algorithm proceeds to iteratively construct
sets of causal states accounting for longer and longer sub-
sequences of symbols. In each iteration, the algorithm ﬁrst es-
timates the probabilities P(rk|
⃗
rℓ) of observing a symbol con-
ditional on each length ℓprior sequence and compares them
with the distribution P(rk|S = Si) it would expect from
the causal states it has so far reconstructed. If P(rk|
⃗
rℓ) =
P(rk|S = Si) for some causal state, then
⃗
rℓis identiﬁed with
it. If the probability is found to be different for all existing Si,
then a new causal state is created to accommodate the sub-
sequence. By constructing new causal states only as neces-
sary, the algorithm guarantees a minimal model that describes
the non-Markovian behaviour of the data (up to a given mem-
ory length), and hence the corresponding ϵ-machine of the
process.
The CSSR algorithm compares probability distributions
via the Kolmogorov-Smirnov (KS) test [40, 41]. The hypothe-
sis that P(rk|
⃗
rℓ) and P(rk|S = Si) are identical up to statis-
tical ﬂuctuations is rejected by the KS test at the signiﬁcance
level σ when a distance DKS [42] is greater than tabulated
critical values of σ [43]. In other words, σ sets a limit on the
accuracy of the history grouping by parametrising the proba-
bility that an observed history
⃗
rℓbelonging to a causal state
Si, is mistakenly split off and placed in a new causal state
Sj. Our analysis, in agreement with Ref. [25], found that
the choice of this value does not affect the outcome of CSSR
within the tested range of 0.001 < σ < 0.01. As a result, we
set σ = 0.005.
As it progresses, the CSSR algorithm compares future
probabilities for longer sub-sequences, up to a maximum past
history length of λ, which is the only important parameter that
must be selected prior to running CSSR in addition to σ. If the
considered time series is generated by a stochastic process of
Markov order ℓ, choosing λ < ℓresults in poor prediction be-
cause the inferred ϵ-machine cannot capture the long-memory
structures present in the data. Despite this, the CSSR algo-
rithm will still produce an ϵ-machine that is consistent with
the approximate future statistics of the process up to order-
λ correlations [25]. Given sufﬁcient data, choosing λ ≥ℓ
guarantees convergence on the true ϵ-machine. One impor-
tant caveat to note is that the time complexity of the algorithm
scales asymptotically as O(|A|2λ+1), putting an upper limit
to the longest history length that is computationally feasible
to use. Furthermore, the ﬁnite length of the time series data
implies an upper limit on an ‘acceptable’ value of λ. Estimat-
ing P(rk|
⃗
rλ) requires sampling strings of length λ from the
ﬁnite data sequence. Since the number of such strings grows
exponentially with λ, a value of λ that is too long relative to
the size N of the data, will result in a severely under-sampled
estimation of the distribution. A distribution P(rk|
⃗
rλ) that
has been estimated from an under-sampled space is almost al-
ways never equal to P(rk|S = Si), resulting in the algorithm
creating a new causal state for every string of length λ it en-
counters. A bound for the largest permissible history length
is L(N) ≥log2 N/ log2 |A|, where L(N) denotes maximum
length for a given data size of N [44, 45]. Once these con-
siderations have been taken into account, the ϵ-machine pro-
duced by the algorithm provides us with a meaningful quan-
tiﬁer of the complexity of the process generating the time se-
ries, as we now discuss.
C.
Measuring the complexity and asymmetry of a process
The output of the CSSR algorithm is the set of causal states
and rules for transitioning from one state to another. That is,
CSSR gives a Markov chain represented by a digraph [20, 37]
G(V, E) consisting of a set of vertices vi ∈V and directed
edges {i, j} ∈E, e.g. Figs. 1(c) and (d). Using these rules,
one can ﬁnd P(Si), which represents the probability that the
ϵ-machine is in the causal state Si at a any time. The Shannon
entropy of this distribution quantiﬁes the minimal number of
bits of information required to optimally predict the future
process; this measure, ﬁrst introduced in Ref. [20], is called
the statistical complexity:
Cµ := H [S] = −
X
i
P(Si) log P(Si).
(2)
Formally, the causal states of a time series depend upon
the direction in which the data is read [33]. The main conse-
quence of this result is that the set of causal states obtained
by reading the time series in the forward direction S+, are not
necessarily the same as those obtained by reading the time se-
ries in the reverse direction S−. Naturally, this corresponds
to potential differences in forward and reverse-time processes
and the associated complexities, which is known as causal ir-
reversibility
Ξ := C+
µ −C−
µ ,
(3)
capturing the time-asymmetry of the process.


## Page 4


4
Another (stronger) measure of time-asymmetry is cryptic-
ity:
d := 2C±
µ −C+
µ −C−
µ .
(4)
This quantity measures the amount of information hidden in
the forwards and reverse ϵ-machines that is not revealed in the
future or past time series, respectively. Speciﬁcally, it com-
bines the information that must be supplemented to determine
the forwards ϵ-machine given the reverse ϵ-machines and the
information to determine reverse ϵ-machines given the for-
wards ϵ-machine. In each case, this is equivalent to the dif-
ference between the complexity of a bidirectional ϵ-machine,
denoted C±
µ [33], and that of the corresponding unidirectional
machine. Throughout this manuscript, we implicitly refer to
the usual forward-time statistical complexity C+
µ when writ-
ing Cµ, unless otherwise stated.
Finally, an operational measure for time-asymmetry is
deﬁned by the microscopic irreversibility, which quanti-
ﬁes how statistically distinguishable the forwards and re-
verse ϵ-machines are, in terms of the sequences of sym-
bols they produce. If the forward-time ϵ-machine produces
the same sequences with similar probabilities to the reverse-
time ϵ-machine, then the process is reversible. Should a se-
quence available to M + be impossible for M −to produce,
then the process is strictly irreversible. Here, we assess the
distinguishability between two ϵ-machines by estimating the
asymptotic rate of (symmetric) Kullback-Leibler (KL) diver-
gence DKLS between long output sequences; this measure is
commonly applied to stochastic models [46]. Speciﬁcally
DKLS = DKL(M +∥M −) + DKL(M −∥M +),
(5)
where DKL is the regular, non-symmetric estimated KL di-
vergence rate [47]. The KL divergence can be proved to be
a unique measure that satisﬁes all of the theoretical require-
ments of information-geometry [17, 48, 49].
A few remarks are in order: in general, any one of the
above measures vanishing does not imply that the other mea-
sures must also vanish. For instance, consider the case where
the structures of the forward (M +) and reverse-time (M −)
ϵ-machines are different but they happen to have the same
complexities, i.e., C+
µ = C−
µ . Then, clearly we have Ξ = 0
but d ̸= 0 and DKLS ̸= 0. On the other hand, consider
the case when M + and M −are the same; here, we have
Ξ = DKLS = 0, yet may not have d = 0. This means that
vanishing DKLS implies that Ξ = 0 (but not the converse,
and not d = 0). This turns out be an interesting extremal case
because, while the forward and reverse processes are iden-
tical, the non-vanishing crypticity accounts for the informa-
tion required to synchronise the corresponding ϵ-machines,
i.e., producing the joint statistics of the paired ϵ-machines.
Moreover, we can conclude that microscopic irreversibility is
a stronger measure than causal irreversibility; this comes at
the expense of computational cost, i.e., the former is harder
to compute than the latter. In essence, each measure above
represents a different notion of temporal asymmetry, with its
own operational signiﬁcance. Causal irrversibility and cryp-
ticity are information-theoretic constructs, while microscopic
irrversibility is a information-geometric construct.
In the next section, we describe the experimental and an-
alytical methods, as well as the results: that the statistical
complexity and temporal asymmetry of the neural time se-
ries, taken from fruit ﬂies, signiﬁcantly differ between states
of conscious arousal.
III.
EXPERIMENTAL RESULTS AND ANALYSIS
A.
Methods
We analysed local ﬁeld potential (LFP) data from
the
brains
of
awake
and
isoﬂurane-anaesthetised
D.
melanogaster (Canton S wild type) ﬂies. Here, we brieﬂy
provide the essential experimental outline that is necessary to
understand this paper. The full details of the experiment are
presented in Refs. [29, 30]. LFPs were recorded by inserting a
linear silicon probe (Neuronexus 3mm-25-177) with 16 elec-
trodes separated by 25 µm. The probe covered approximately
half of the ﬂy brain and recorded neural activity as illustrated
in Fig. 1(a). A tungsten wire inserted into the thorax acted
as the reference. The LFPs at each electrode were recorded
for 18s while the ﬂy was awake and 18s more after the ﬂy
was anaesthetised (isoﬂurane, 0.6% by volume, through an
evaporator). Flies’ unresponsiveness during anaesthesia was
conﬁrmed by the absence of behavioural responses to a series
of air puffs, and recovery was also conﬁrmed after isoﬂurane
gas was turned off [29].
We used data sampled at 1kHz for the analysis [29], and to
obtain an estimate of local neural activity, the 16 electrodes
were re-referenced by subtracting adjacent signals giving 15
channels which we parametrise as c ∈[1, 15]. Line noise was
removed from the recordings, followed by linear de-trending
and removing the mean. The resulting data is a ﬂuctuating
voltage signal, which is time-binned (1ms bins) and bina-
rised by splitting over the median, leading to a time series,
see Fig. 1(b).
For each of the 13 ﬂies in our data set, we considered 30
time series of length N = 18, 000.
These correspond to
the 15 channels, labelled numerically from the central to pe-
ripheral region as depicted in Fig. 1(a), and the two states
of conscious arousal. Using the CSSR algorithm [25], we
constructed ϵ-machines for each of these time series as a
function of maximum memory length within the range λ ∈
[2, 11], measured in milliseconds. This is below the mem-
ory length L(N) ∼14 beyond which we would be unable
to reliably determine transition probabilities for a sequence
of length N (see Sec. II B) [51]. For a given time direction
ξ ∈{+ : forward, −: reverse}, we recorded the resulting
3, 900 ϵ-machine structures and their corresponding statisti-
cal complexities C(ξ,ψ)
µ
, and grouped them according to their
respective level of conscious arousal, ψ ∈{w, a} for awake
and anaesthesia, channel location, c, and maximum memory
length, λ. Thus, the statistical complexity we computed in
a given time direction is a function of the set of parameters
{ψ, c, λ} for each ﬂy, f. We also determined the irreversibil-
ity Ξ, crypticity d, and symmetric KL divergence rate DKLS
for each ﬂy and again grouped them over the same set of pa-
rameters {ψ, c, λ}. While we found that not all the data is


## Page 5


5
Figure 1. Evolution of experimental data from neural signals to ϵ-machines. (a) Representative schematic of D. melanogaster brain (modiﬁed
from Ref. [50]) depicted with probe and approximate channel locations. Each channel c ∈[1, 15] samples around a localised region in the
brain, with numerical labels ordered from the central (c = 1) to peripheral (c = 15) regions. (b) Example reading of a processed local ﬁeld
potential (LFP) for a single channel. Points along the x-axis represent LFP measurements at each sampling time step. The median LFP
measurement of the sample is shown as the grey line bisecting data. LFP binarisation is determined via splitting over the median with the
encoding scheme 0 : LFP ≤Median, and 1 : otherwise. The ϵ-machines are inferred by using the binary string as the input to the CSSR
algorithm. (c) Digraph representation of the CSSR-inferred ϵ-machine for channel 1 readings of ﬂy 1 under anaesthesia (0.6 vol.% isoﬂurane)
with σ = 0.005 and λ = 3. Graph vertices correspond to causal states. Vertex labels distinguishing causal states are assigned arbitrarily and
do not imply state equivalence across multiple graphs. Directed edges correspond to transitions between causal states. Edge labels denote the
probability (2 signiﬁcant ﬁgures) of a transition occurring, and edge colour encodes the emitted symbol upon making the transition (1: Red,
0: Blue). The histories stored in the causal states for this ϵ-machine are visualised in Fig. 6. (d) Digraph representation of ϵ-machine for the
wakeful (0 vol.% isoﬂurane) level of conscious arousal for the same channel, ﬂy, σ, and λ as in (c). We report the forward-time statistical
complexities Ca
µ = 1.88 and Cw
µ = 2.96 for (c) and (d) respectively.
strictly stationary, in that the moving means of the LFP sig-
nals were not normally distributed, the conclusions we draw
from them are still broadly valid. As mentioned in Sec. II A,
ϵ-machines reconstructed from approximately stationary data
are time-averaged models, and are likely to underestimate the
true statistical complexity of the corresponding neural pro-
cesses.
We are principally interested in the differences the infor-
mational quantities Qψ ∈{C(ξ,ψ)
µ
, Ξψ, dψ, Dψ
KLS} have
over states of conscious arousal and thus consider
∆Q := Qw −Qa,
(6)
for ﬁxed values of {f, c, λ}.
Positive values of ∆Q indi-
cate higher complexities observed in the wakeful state rela-
tive to the anaesthetised one. Finally, we use the notation
⟨Qψ⟩x to denote taking an average of any information quan-
tity Qψ, over a speciﬁc parameter x ∈{f, c, λ}. For ex-
ample ⟨∆C+
µ ⟩f means taking the ﬂy-averaged difference in
forward-time statistical complexity.
To assess the signiﬁcance of each of the parameters ψ, c, λ,
and ξ, or some combination of them, have on the response of
the elements in the set Q across ﬂies, we conducted a statisti-
cal analysis using linear mixed effects modelling [52] (LME).
The LME analysis describes the response of a given quantity
Q by modelling it as a multidimensional linear regression of
the form
Q = Fβ + Rb + E.
(7)
The resulting model in Eq. (7) consists of a family of equa-
tions where Q is the vector allowing for different responses
of a quantity Q for each speciﬁc ﬂy, channel location, level
of conscious arousal, and time direction where applicable.
Memory length λ, channel location c, state of conscious
arousal ψ, and time direction ξ (again, where applicable)
are the parameters that Q responds to. To account for vari-
ations in the response caused by interactions between param-
eters (e.g. between memory length and channel location), we
included them in the model. Letting X = {λ, c, ψ, ξ} be
the set of the parameters which may induce responses, we
can write all the non-empty k-combinations between them
as F = {λ, c, ψ, ξ, λc, λψ, ..., λcψξ} =
 X
k

\∅. The ele-
ments in F are known as the ﬁxed effects of Eq. (7), and are


## Page 6


6
contained as elements within the matrix F. The vector β,
contains the regression coefﬁcients describing the strength of
each of the ﬁxed effects F.
In addition to ﬁxed effects affecting the response of an el-
ement of Q in our experiment, we also took into account any
variation in response caused by known random effects. In par-
ticular, we expected stronger response variations to be caused
by correlations occurring between the channels within a sin-
gle ﬂy, compared to between channels across ﬂies. These ran-
dom effects are contained as elements of the matrix R, and
the vector b encodes the regression coefﬁcients describing
their strengths. Finally, the vector E describes the normally-
distributed unknown random effects in the model. The re-
gression coefﬁcients contained in the vectors β and b, were
obtained via maximum likelihood estimation such that E are
minimised. The explicit form of Eq. (7) used in this analysis
is detailed in the Appendix IV A.
With the full linear mixed effects model given by Eq. (7),
we tested the statistical signiﬁcance of a ﬁxed effect in F.
This was accomplished by comparing the log-likelihood of
the full model with all ﬁxed effects, to the log-likelihood of
a reduced model with the effect of interest removed [53] (re-
gression coefﬁcients associated with the effect are removed).
This comparison between the likelihood models is given by
Λ = 2(hfull −hreduced), where Λ is the likelihood ratio, hfull
is the log-likelihood of full model, and hreduced is the log-
likelihood of the model with the effect of interest removed.
Under the null hypothesis, when a ﬁxed effect does not
have any inﬂuence on an informational quantity Q, i.e., the
regression coefﬁcients for the effect are vanishing, the likeli-
hood ratio Λ is χ2 distributed with degrees of freedom equal
to the difference in the number of coefﬁcients between the
models. Therefore, we considered any ﬁxed effect in the set
F to have a statistically signiﬁcant effect on a quantity if the
probability of obtaining the likelihood ratio given the relevant
χ2 distribution was less than 5% (p < 0.05). Thus, for each
signiﬁcant effect we report the ﬁxed effect being tested, i.e.,
an element of F, the obtained likelihood ratio χ2(n−1) with
n associated degrees of freedom, and the associated probabil-
ity p of obtaining the statistic under the null hypothesis.
In addition to all the quantities in the set Qψ, the LME and
likelihood ratio test was also performed for ∆Q, in order to
ﬁnd the signiﬁcant interaction effects of the parameters. Here,
we also modelled ∆Q as dependent on a ﬁxed effect in F as
in Eq. (7), but excluding the parameter ψ as it was already
implicitly considered. Once the signiﬁcant effects of memory
length, level of conscious arousal, and channel location were
characterised with our statistical analysis, we followed with
post-hoc, paired t-tests for elements in Qψ given by
t = ⟨∆Q⟩f
sf/
p
|f|
,
(8)
where sf is the standard deviation of ⟨∆Q⟩f, and |f| = 13
is the sample size. The paired t-tests examine the nature of
interactions between the parameters on a given quantity over
the two states of conscious arousal. Positive t-scores indi-
cate a quantity is larger for the wakeful state. We present
the results of these analyses in the following sections, sorted
categorically by whether time-direction is considered.
Anaesthetised (0.6% isoflurane)
Wakeful (0% isoflurane)
Figure 2. Colour map of statistical complexity response averaged
over (n = 13) ﬂies ⟨C(+,ψ)
µ
⟩f, during wakefulness (left) and anaes-
thesia (right), over channel location and memory length λ, measured
in milliseconds. Hatched cells on the right sub-ﬁgure, show regions
where Cµ did not decrease under anaesthesia.
B.
Results
1.
Forward-time complexity results
In order to observe the effects of isoﬂurane on neural
complexity, we began by visually inspecting the structure of
the reconstructed ϵ-machines for the two levels of conscious
arousal for the forward-time direction. We took special inter-
est in observing the differences in the characteristics of the
two groups of ϵ-machines heralding the two levels of con-
scious arousal. Here, memory length λ plays an important
role. At a given λ, the maximum number of causal states
that may be generated scales according to |A|λ [25]. In our
case, the alphabet is binary, A = {0, 1}. This greatly restricts
the space of ϵ-machine conﬁgurations available for short his-
tory lengths [54]. For λ = 2 we can observe up to four dis-
tinct conﬁgurations, which is unlikely to reveal the difference
based on conscious states. Given the previous ﬁndings [30],
we generally expected that the data from the wakeful state
would present more complexity than those from the anaes-
thetised state.
Visual inspection of the directed graphs indeed suggested
higher ϵ-machine complexity during the wakeful state com-
pared to the anaesthetised state, at a given set of parameters
{f, c, λ}. In particular, the data from the anaesthetised state
tended to result in fewer causal states and overall reduced
graph connectivity. Panels (c) and (d) of Fig. 1 are examples
of ϵ-machines (channel 1 data recorded from ﬂy 1, at maxi-
mum memory length λ = 3), where a simpler ϵ-machine is
derived from the data under the anaesthetised condition. Dif-
ferentiating between two conscious arousal states by visual
inspection quickly becomes impractical because of the large
number of ϵ-machines. Moreover, for large values of λ the
number of causal states is exponentially large and it becomes
difﬁcult to see the difference in two graphs. To overcome
these challenges, we looked at a simpler index, the statisti-
cal complexity Cµ, to differentiate between conscious arousal
states. To systematically determine the relationships between
Cµ and the set of variables {c, f, ψ} we employed the LME
analysis outlined in Sec. III A. We ﬁrst tested whether λ sig-
niﬁcantly affects Cµ. We found λ to indeed have a signiﬁcant


## Page 7


7
effect on Cµ (λ, χ2(1) = 443.64, p < 10−16). Fig. 2 shows
that independent of the conscious arousal condition or chan-
nel location, Cµ increases with larger λ. This indicates that
the Markov order of the neural data is much larger than the
largest memory length (λ = 11) we consider. Nevertheless,
we have enough information to work with.
We then sought to conﬁrm if the complexity of ϵ-machines
during anaesthesia are reduced, as suggested from visual in-
spection.
Our statistical analysis indicates that Cµ is not
invariably reduced during anaesthesia (ψ, χ2(1) = 0.212,
p = 0.645) at all levels of λ and all channel locations.
This means that Cµ cannot simply indicate the causal arousal
state without some additional information about time (λ) or
space (c). In addition, we found that neither c alone nor cψ
strongly affects Cµ. However, we found signiﬁcant reduc-
tions in complexity when either the level of conscious arousal
or the channel location, interacted with memory length (λψ,
χ2(1) = 14.63, p = 1.31×10−4) and (cλ, χ2(14) = 42.876,
p = 8.97 × 10−5) respectively. Moreover, the three-way
interaction also had a strong effect (λψc, χ2(14) = 24.00,
p = 0.0458).
As the three-way interaction between λ, ψ, and c compli-
cates interpretation of their effects, we performed a second
LME analysis where we modelled ∆Cµ instead of Cµ, thus
accounting for ψ implicitly.
In doing so, we investigated
whether the change in statistical complexity due to anaes-
thesia is affected by memory length λ or channel location
c. Using this model, we found a non-signiﬁcant effect of c
on ∆Cµ, while a signiﬁcant effect of λ on ∆Cµ was seen
(λ, χ2(1) = 20.97, p = 4.65 × 10−6), indicating that ∆Cµ
overall changes with λ. Speciﬁcally, ∆Cµ tended to increase
with larger λ when ignoring channel location, as is evident in
Fig. 3 (top). Further, explaining our previous interaction be-
tween λ and ψ, ∆Cµ was not clearly larger than 0 for small
memory length (λ = 2; the top panel of Fig. 3). This sug-
gests that the information to differentiate between states of
conscious arousal is contained in higher order correlations.
We also found that the interaction between λ and channel lo-
cation has a signiﬁcant effect on ∆Cµ (λc, χ2(14) = 37.19,
p = 6.90 × 10−4), indicating that the effect of λ is not con-
stant across channels. Given that ∆Cµ overall increases with
λ, we considered that that the largest ∆Cµ should occur at
the largest λ. Fig. 3 (bottom) examines ∆Cµ across channels
at λ = 11.
To further break down the interaction between λ and c,
we performed a one sample t-test at each value of memory
length and channel location to ﬁnd regions in the parame-
ter space (λ, c) where Cµ reliably differentiates wakefulness
from anaesthesia across ﬂies. We plot the t-statistic at each
parameter combination in the top-left panel of Fig. 4, out-
lining regions in the parameter space where ∆Cµ is signif-
icantly greater than 0 (with p < 0.05, uncorrected, two-
tailed), ﬁnding that the majority of the signiﬁcance map is
directed towards positive values of the t-statistic. However,
only a subset of (λ, c) cells contain values which are signif-
icantly different from 0. Interestingly, we observed that for
λ = 2, ∆Cµ is actually signiﬁcantly negative, corresponding
to greater complexity during anaesthesia, not during wakeful-
ness. This marks λ = 2 as anomalous relative to other levels
Figure 3. Statistical complexity differences ∆Cµ = Cw
µ −Ca
µ of
ϵ-machines between states of conscious arousal for: (Top) increas-
ing memory length λ. Grey lines indicate complexity averages over
channels per ﬂy (n = 13), ⟨∆Cµ⟩c, while the blue line denotes
the average over both channels and ﬂies ⟨∆Cµ⟩c,f. Error bars are
95% conﬁdence intervals of the population. (Bottom) maximum
memory length λ = 11 (in milliseconds), mapped throughout the
ﬂy brain (channels). Grey and red lines indicate the result per ﬂy
and the average over (n = 13) ﬂies, ⟨∆Cµ⟩f, respectively. Error
bars corresponding to the 95% conﬁdence intervals over the sample
of ﬁles.
of λ, and this reversal of the direction of the effect of anaes-
thesia likely contributed to the interaction between λ and ψ.
Disregarding λ = 2, we ﬁnd ∆Cµ to be signiﬁcantly
greater than 0 for channels 1, 3, 5-7, 9, 10, and 13, at vary-
ing levels of λ. As expected from our reported interaction
between λ and c, we observe ∆Cµ to already be signiﬁcantly
greater than 0 at small λ for channels 5-7, while ∆Cµ only
became signiﬁcantly greater at larger λ for channels 1, 3, 10
and 13. Further, other channels such as the most peripheral
channel (c = 15) did not have ∆Cµ signiﬁcantly greater than
0 at any λ. All signiﬁcance results, due to LME tests, are
reported in Table I.
The above results suggest that the measured difference in
complexity is present across various brain regions (top-left
panel of Fig. 4), and that it grows as longer temporal correla-
tions are taken into account (up to the largest value λ = 11
tested). While Fig. 3 shows a continued increase in the differ-
ence of statistical complexity, ∆Cµ, as a function of λ, we did
not analyse longer history lengths, due to limitations in the
amount of the data and stability of the estimation of Cµ. In
addition to this general observation of increasing ∆Cµ with
λ, we observe that, remarkably, some brain regions discrimi-
nate the conscious arousal states with a history length of only
3. One trivial explanation for this effect is that under anaes-
thesia, the required memory length is indeed λ = 2, while the
optimal λ for awake is much larger. However, a quick obser-
vation of Fig. 2 rules out this simple possibility; under both


## Page 8


8
Figure 4.
Colour map of two-tailed paired t-scores over channel location and memory length λ for statistical complexity differences
⟨∆C+
µ ⟩f = ⟨C(+,w)
µ
−C(+,a)
µ
⟩f (top left); causal irreversibility differences ⟨∆Ξ⟩f = ⟨Ξw −Ξa⟩f (top right); crypticity differences
⟨∆d⟩f = ⟨dw −da⟩f (bottom left); and the differences in KL divergence rate ⟨∆DKLS⟩f = ⟨Dw
KLS −Da
KLS⟩f (bottom right). The dotted
lines indicate the memory length and channel locations that exceed p < 0.05 (uncorrected). The colour scale is consistent across all subplots.
wakeful and anaesthetised states, Cµ continues to increase.
It is likely, however, that the tested range for λ remains
below the Markov order of the neural data; this is clearly
indicated by the lack of a plateau in statistical complexity
in Fig. 3. This suggests that we are far from saturating the
Markov order of the process, and with more data we would
be able to further distinguish between the two states. Fu-
ture analyses with longer time series would also contribute
to our understanding of the Markov order (maximum mem-
ory length) differences between the two states of conscious
arousal. Nevertheless, our results, in Figs. 3 and 4, demon-
strate that saturation of Markov order is not required for
discrimination between conscious arousal states. This ﬁnd-
ing has a practical implication about the empirical utility of
ϵ-machines; even if the history length is too low, the inferred
ϵ-machine and its statistical complexity can be useful. We
now discuss the temporal asymmetry of neural processes.
2.
Temporal asymmetry
Unlike other complexity measures, we obtain a distinct
ϵ-machine from each given time series, and for each direction
we read the time series, i.e., forward or backward in time.
Based on the notion that wakeful brains should be better at
predicting the next sensory input [30], we expect that anaes-
thesia should alter the information structures depending on
the time direction. Our expectation translates to the follow-
ing three hypotheses:
1. Causal irreversibility (Ξ := C+
µ −C−
µ ), which is purely
based on the summary measure of statistical complex-
ity, should be higher for awake but lower for anaes-
thetised brains;
2. Crypticity (d := 2C±
µ −C+
µ −C−
µ ) should be higher
for wakeful than anaesthetised brains;
3. Symmetric KL divergence rate (DKLS) should behave
similarly.
On visual inspection of the variation in Ξ for the wake-
ful and anaesthetised conditions, both appeared close to zero,


## Page 9


9
suggesting that Ξ would not have signiﬁcant dependence
on the condition.
This impression was conﬁrmed statisti-
cally with two-tailed t-tests against zero with corrections for
multiple comparisons, as shown in the top-right panel of
Fig. 4. Thus, Hypothesis 1 above, that irreversibility should
be higher for wakeful over anaesthetised brains, is not sup-
ported by the data. However, as mentioned earlier, vanishing
Ξ does not imply that either d = 0 or DKLS = 0. To rule out
the possibility that the information structure of ϵ-machines
are different when read forwards, as opposed to backwards,
depending on the condition, we also tested the latter two hy-
potheses.
With respect to crypticity, ﬁrst, visual inspection of the
two-tailed t-score map, which compares crypticity for the
wakeful dw and anaesthetised da conditions (bottom-left
panel of Fig. 4) strongly implies that crypticity is larger in
the former compared to the latter. This difference is largest
over channels 5-7 and 9.
To systematically evaluate this
impression, we used LME statistical analysis (described in
Sec. III A) to determine the relationships between cryptic-
ity, d, and the set of variables {c, λ, ψ} we employ.
As
expected, we found that both memory length (λ) and level
of conscious arousal (ψ) signiﬁcantly affected crypticity (λ,
χ2(1) = 470.5, p < 10−16) and (ψ, χ2(1) = 5.896,
p = 0.0152) respectively.
Crypticity also depended on a
signiﬁcant interaction between memory length and condition
(λψ, χ2(1) = 6.119, p = 0.0134). Speciﬁc increases in
crypticity around the middle brain region (bottom-left panel
of Fig. 4) were also evident, with a strong interaction between
channel location and memory length (λc, χ2(14) = 35.86,
p = 1.09 × 10−3), which is similar to the result obtained for
∆Cµ. This LME analysis, together with the direction of ef-
fects in Fig. 4 (bottom-left) strongly conﬁrms our Hypothesis
2.
Furthermore, as a more direct measure of microscopic
structure, we also analysed the symmetric KL divergence
rate, DKLS.
Again, the two-tailed t-score map (Fig. 4,
bottom-right panel) showed support for our hypothesis. Our
formal statistical analysis with LME conﬁrmed a criti-
cal interaction between memory length and condition (λψ,
χ2(1) = 15.37, p < 10−16), meaning that time-asymmetric
information structure is lost due to anaesthesia, especially
when a long memory length is taken into account. (We also
note other signiﬁcant effects: mainly the effect of memory
length (λ, χ2(1) = 127.4, p < 10−16) and interaction be-
tween memory length and channel location (λc, χ2(14) =
85.81, p < 10−16). Again, all signiﬁcant results, due to LME
tests, are reported in Table I.
Taken together, these results show that the relative com-
plexity of the forward versus reverse direction, as measured
by causal irreversibility, does not distinguish between the
wakeful and anaesthetised states. However, our crypticity re-
sults demonstrate that, under anaesthesia, the structures of the
forward and reverse processes are relatively similar, whereas
during wakefulness their structures differ.
Fig. 5 demon-
strates this effect with exemplar ϵ-machines reconstructed
from a representative channel, from which we derived six dis-
tinct ϵ-machines: three for wakeful (a, c, d), and three for
anaesthetised (e-g) ﬂies. Panel (b) shows how the time series
and the transitions in the causal states of forward, reversed,
and bidirectional ϵ-machines are related.
Our ﬁnding, that causal irreversibilities were not above
zero for wakeful brains, corresponds to the fact that com-
plexities of forward and reverse ϵ-machines were not signif-
icantly different. However, the bidirectional ϵ-machines for
the wakeful condition were substantially more complex than
those for the anaesthetised condition. The statistical complex-
ity of bidirectional ϵ-machines should equal that of forward or
reverse ϵ-machines if the process is completely time symmet-
ric and deterministic [33], resulting in zero crypticity. How-
ever, for non-deterministic processes, additional information
for synchronising the forward and reversed process may be
needed, which would mean d > 0. For instance, in Fig. 5(e-
f), if we are told that the forward machine is in causal state
A, we need extra information to determine whether the re-
versed machine is in causal state X or Y . Yet, the detailed
structure of the forward and reverse machines are the same
in this example. Our analysis is supplemented with a study
of the symmetric KL divergence rate between forwards and
backwards processes, which measures the distance between
the reconstructed ϵ-machines. In other words, crypticity and
symmetric KL divergence rate quantify two different notions
of temporal asymmetry; the former is information theoretic,
and the latter is information-geometric. Indeed, in general
we ﬁnd that the processes in the two directions are different
in both ways and, further, their difference varies signiﬁcantly
between conditions, as shown in the bottom two panels of
Fig. 4.
IV.
DISCUSSION
Discovering a reliable measure of conscious arousal in an-
imals and humans remains one of the major outstanding chal-
lenges of neuroscience.
The present study addresses this
challenge by connecting a complexity measure to the degree
of conscious arousal, taking a step forward to strengthen-
ing the link between physics, complexity science, and neu-
roscience. Here, we have taken tools from the former and
have applied them to a problem in the latter. Namely, we
have studied the statistical complexity and time asymmetry
of neural recordings in the brains of ﬂies over two states of
conscious arousal: awake and anaesthetised. We have demon-
strated that differences between these macroscopic states can
be revealed by both the statistical complexity of local elec-
trical ﬂuctuations in various brain regions, and various mea-
sures of temporal asymmetry of hidden models that explain
their behaviour. Speciﬁcally, we have analysed the single-
channel signals from electrodes embedded in the brain using
the ϵ-machine formalism, and quantiﬁed the statistical com-
plexity Cµ, causal and microscopic reversibility Ξ & DKLS,
and crypticity d of the recorded data for 15 channels in 13
ﬂies over two states of conscious arousal. We ﬁnd the statis-
tical complexity is larger on average when a ﬂy is awake than
when the same ﬂy is anaesthetised (∆Cµ > 0; Figs. 3 and 4),
and that the structural complexity of information and its time
reversibility captured by crypticity and KL rate are also re-
duced under anaesthesia (∆d > 0 and ∆DKLS > 0; Fig. 4).


## Page 10


10
0.49
0.57
X
0.51
0.43
0.51
Y
Z
0.49
B
0.52
A
C
D
0.51
0.53
0.47
0.40
0.60
0.48
0.49
A
D
A
B
C
C
D
D
A
B
0
1
1
1
1
0
0
1
1
X
Y
Y
Y
Y
Z
X
Y
Y
X
(b)
(c)
(a)
A,Z
A,Y
D,Y
0.64
A,X
C,X
D,X
B,X
C,Z
B,Z
B,Y
0.51
0.26
0.23
1.0
1.0
0.41
0.59
0.47
1.0
0.53
1.0
D,Z
C,Y
0.52
0.48
0.19
0.17
0.44
0.25
0.21
0.54
0.56
0.25
0.53
0.22
(d)
0.52
A
B
0.52
0.48
0.48
(e)
0.52
X
Y
0.52
0.48
0.48
A,X
0.53
B,Y
A,Y
B,X
0.53
0.47
0.51
0.49
0.47
0.51
0.49
(f)
(g)
Figure 5. Exemplary digraph representations of ϵ-machines for wakeful (a-d) and anaesthetised (e-g) conditions for forward-time (a, e),
reverse-time (c, f), and bidirectional (d, g) analyses, all constructed from channel 5 in ﬂy 7, at memory length λ = 3. Panel (b) gives an
example emission sequence and causal state sequence for forward and reverse-time ϵ-machine pair (a) and (c). The vertex labelling denoting
causal states in (a-d) is consistent to show composition of forward and reverse-time ϵ-machines in the bidirectional ϵ-machine. The ϵ-machines
for the wakeful condition have statistical complexity of C(+,w)
µ
= 1.76, C(−,w)
µ
= 1.50, and C(±,w)
µ
= 3.25. In this example the process
is irreversible for all three quantities. The ϵ-machines for the anaesthetised condition have statistical complexity of C(+,a)
µ
= C(−,a)
µ
= 1.0
and C(±,a)
µ
= 1.9989. The process is causally and microscopically reversible, but has ﬁnite crypticity.
As we have demonstrated in this study, the local informa-
tion contained within a single channel can contain informa-
tion about global conscious states, which are believed to arise
from interactions among many neurons. Theoretically, single
channels can reﬂect the complexity of the multiple channels
due to the concept of Sugihara causality [55]. This arises due
to any one region of the brain causally interacting with the
rest of the brain, making the temporal correlation in a single
channel time series contain information about the spatial cor-
relations, i.e., information that would be contained in multiple
channels. With this logic, Ref. [56] infers the complexity of
the multi-channel interactions from a single channel temporal
structure of the time series. This is often known as the back-
ﬂow of information in non-Markovian dynamics [57]. The
periodic structure of statistical complexity observed across
channels in Fig. 2, demonstrates an unexpected example of
spatial effects present in our study – one that was not observed
with conventional LFP analyses. This observation may pro-
vide a motivation for multi-channel analyses.
While we already ﬁnd differences between conscious states
in the single channel based ϵ-machine analysis, it would be
beneﬁcial to extend the present analysis to the multi-channel
scenario, in which ϵ-machine can be contrasted with the
methods of IIT [9–18]. Formal comparison of the distinguish-
ing power of conscious states among proposed methods (such
as those in Ref. [6, 7]) will contribute to reﬁning models and
theories of consciousness.
Our results can be informally compared with a previous
study, where the power spectra of the same data in the fre-
quency domain [30] was analysed. There, a principal obser-
vation was the power in low-frequency signals in central and
peripheral regions, which was more pronounced in the cen-
tral region (corresponding to channel 1-6 in this study). Our
ϵ-machine analysis here reveals that the region between pe-
riphery and centre (channels 5-7) shows most consistent dif-
ference in Cµ across history length λ > 2. Ultimately, the
reason for this difference is due to our distinct approach, in-
sofar as ϵ-machines are provably the optimal predictive mod-
els of a large class of time series that take into account higher
order correlations memory structure [20, 21]. Thus, our ap-
plication of ϵ-machines contrasts with the power spectra anal-
ysis, by considering these higher order correlations for very
high-frequency signals, instead of only two-point correlations
in both high- and low-frequency signals. Finally, the top-left
panel of Fig. 4 shows that in regions corresponding to chan-
nels 1 and 13, the differences in the conditions are only seen
at high values of λ.
Our multi-time analysis further reveals an interesting ef-
fect when we look more closely at, e.g., the anaesthetised
ϵ-machine example shown in Fig. 1(c). When we examine the
binary strings belonging to each causal state, we ﬁnd a clear
split between active (consecutive strings of ones) and inactive
(consecutive strings of zeros) neural behaviour corresponding
to the left and right hand sides of Fig. 6 respectively. Previ-
ous studies have demonstrated an increase in low-frequency
LFP and EEG power for mammals and birds during sleep and
anaesthesia, mediated by similar neural states of activity and
inactivity known as ‘up’ and ‘down’ states [58, 59]. A simi-
lar phenomenon has recently been observed in sleep deprived
ﬂies [60]. Consistent with other studies, our study, using gen-
eral anaesthesia, does not observe this slow oscillations. Fu-
ture studies with more formal comparisons between up and
down states and ϵ-machines, in both theory and computer
simulations, may be a fruitful avenue for further research in


## Page 11


11
0.58
0.42
0.50
0.50
0.60
0.41
0.50
0.50
B
*110 
*010
D
*001
A
*111 
*101 
*011
C
*100 
*000
Figure 6.
ϵ-machine for same channel, ﬂy, conscious state as
Fig. 1(c), but with histories stored in each causal state explicitly
stated. The sequences after the asterisk ∗represent the sequence
of symbol observations with the most recent observed symbol on
the far right. Sequences collected within a causal state (grey circle)
warrant signiﬁcantly different future statistics to observed sequences
in other causal states. The red lines emit a “1" upon transition, and
blue lines emit “0"s.
this regard.
An analysis in terms of ϵ-machines has also allowed us to
discriminate between levels of conscious arousal by examin-
ing causal structures found in both forward and reverse time
directions. Based on our previous ﬁnding [30] as well as re-
lated concepts in temporal predictive [31, 61–63] and causal
matching [32], we hypothesised that the wakeful brain may
be tuned to causal structures of the world, which run forward
in time, and thus ϵ-machines would be more complex for for-
ward than reverse readings. Further, we hypothesised that
such temporally tuned structural matching will be lost under
anaesthesia. Our results (Sec. III B 2) are highly intriguing
in three ways. First, near-zero causal irreversibility indicates
that reducing the structural complexity to a simple index is
not enough to capture effects on the information structure that
are sensitive to the direction of time. This is the case regard-
less of the level of consciousness (at least at the timescales of
this study). Second, nonzero crypticity indicates that the un-
derlying information structure is not symmetric in time. More
precisely, the signals themselves encode different amounts
of information when run forwards as opposed to backwards.
Third, the KL divergence rate analysis deﬁnitively demon-
strated the existence of greater temporal irreversibility in the
wakeful as opposed to the anaesthetised state. Having said
this, we are limited in drawing strong conclusions due, in
part, to the relatively small observed effect size of Ξ, likely
a consequence of our relatively small data set. Despite this,
even at millisecond time scales, our study successfully iden-
tiﬁes signiﬁcant differences in the time direction of the neural
recordings.
Identifying the decrease in temporal-reversibility due to
anaesthesia in tandem with complexity is of broad interest
in neuroscience. While some physicists and neuroscientists
have conjectured links among physics, the brain, and even
consciousness through the lens of the direction of the time,
their accounts have remained rather speculative, and not built
on any solid theoretical foundations (for related and alter-
native theoretical foundations, see the work by Cofré and
colleagues [64, 65]). For example, using reversely played
movies, the sensitivity to the direction of time is shown to
differ across brain regions in humans [66]. In animal stud-
ies, some populations of neurons (in the hippocampus) are
known to become activated in a particular sequential order
while the animal experiences a particular event. For example,
in anticipation of the event, the neurons activate in a forward
direction, but in retrospection, the neurons activate in reverse
order [67]. While direct links between these empirical ﬁnd-
ings and the ϵ-machine framework remains elusive, we fore-
see that our uniﬁed theoretical and analytical framework can
potentially bridge this gap in the future.
Our study is not the ﬁrst to apply complexity measure in
consciousness research. Indeed, many deﬁnitions and mea-
sures of complexity have been proposed in the literature (see
Ref. [68] for a list). Moreover, there is a ﬂow of ideas going
the other way as well [69–71]. However, many, if not most,
of these measures cannot account for temporal correlations
(memory), temporal asymmetry, or differentiate between ran-
dom and structured processes. Our interdisciplinary study,
based on ϵ-machines, opens up new possibilities; physics can
improve its theoretical constructs through the application of
tools to empirical data, while neuroscience can beneﬁt from
rigorous quantitative tools that have proven their physical
basis across different spatio-temporal scales. Among those
complexity measures, Cµ can be easily interpreted in terms
of temporal structure [72], as it has a direct relation to pro-
cess predictability and memory requirements. We empha-
sise that statistical complexity Cµ derived from ϵ-machines,
drastically differentiates itself from other scalar complex-
ity indices such as Lempel-Ziv complexity [73].
For one
Lempel-Ziv complexity is maximal for a random noise pro-
cess whereas statistical complexity for the same process is
zero (see Eq. (2)). In addition, the notion of temporal re-
versibility available in the ϵ-machine framework has no coun-
terpart in Lempel-Ziv complexity. This is a critical differ-
ence since it is known that a low-complexity forward-time
ϵ-machine consisting of only two causal states can have a
very high-complexity reverse-time ϵ-machine with countably
inﬁnite states [74]. Thus, explicitly considering the inﬂuence
of time is critical for addressing questions about complexity.
When coupled with our results, we can conclude that anaes-
thetised brains become less structured, more random, more
reversible, and approach a stochastic process with a smaller
memory capacity compared to the wakeful brains.
Overall, our results suggest that measures of complexity
extracted from ϵ-machines might be able to identify further
structures that are affected by anaesthesia at different spatial
and temporal scales. It is also likely that applying a similar
analysis to other data sets, in particular, human EEG data will
lead to new discoveries regarding the relationship between
consciousness and complexity that can be retrieved simply at
the single channel level.


## Page 12


12
ACKNOWLEDGMENTS
RNM, FAP, NT, KM acknowledge support from Monash
University’s Network of Excellence scheme and the Foun-
dational Questions Institute (FQXi) grant on Agency in the
Physical World.
AZ was supported through Monash Uni-
versity’s Science-Medicine Interdisciplinary Research grant.
DC was funded by an Overseas JSPS Postdoctoral Fellow-
ship. NT was funded by Australian Research Council Discov-
ery Project grants (DP180104128, DP180100396). NT and
CD were supported by a grant (TWCF0199) from Temple-
ton World Charity Foundation, Inc. We thank Felix Binder,
Alec Boyd, Mile Gu, Rhiannon Jeans, and Jayne Thompson
for valuable comments. KM is supported through Australian
Research Council Future Fellowship FT160100073.
APPENDIX
A.
Linear mixed-effects model
In this section, we demonstrate an example of an LME
analysis for the case of statistical complexity Cµ in the for-
ward time direction. For the case when time direction ξ is in-
cluded as an effect, the only change this makes to the process
is increasing the dimensions of the effects matrix F. Perform-
ing an LME analysis on other quantities used in this study like
crypticity or KL rate follow the same procedure outlined here.
The main goal of the LME analysis we perform in this
study is to determine the degree of contributions each and
combinations of memory length (λ), channel location (c),
and level of conscious arousal (ψ) have on statistical com-
plexity Cµ. LME accomplishes this by modelling statistical
complexity as a general linear regression equation (Eq. (7)),
whose response is predicted by the aforementioned param-
eters λ, c, and ψ.
In this Appendix, we show the exact
form of the linear regression equation used in this analysis,
while referring to the terminology introduced in the methods
(Sec. III A).
We begin by restating Eq. (7) for the case of statistical com-
plexity, C = Fβ + Rb + E, which has the form of a general
multidimensional linear equation. We will set aside the right
hand side of the equality for now. On the left hand side, sta-
tistical complexity takes the form of a column vector C. Each
row corresponds to the unique response of Cµ, at a speciﬁc
selection of parameters. There is a general freedom of choice
associated with the number of parameters one would like to
assign to the elements C. We index the rows with ﬂy number
f, channel location c, and the conscious arousal state ψ. That
is, the (i, j, k)th element is
[C](i,j,k) = C(i,j,k)
µ
.
(9)
In other words, it is the ith ﬂy’s jth channel in kth condition.
Thus, C has length of |f| × |c| × |ψ| = 390. Each Cµ in this
vector is a function of λ.
The matrix F introducing the set of ﬁxed effects F =
{λ, c, ψ, λc, λψ, cψ, λcψ} into the model (known in the con-
text of general linear models as the design matrix) can then
be represented as F = (F1, . . . , F13)T , with each element
corresponding to the design matrix of a speciﬁc ﬂy. These
individual ﬂy response matrices can be explicitly expressed
as
Ff =
 
⃗λ D ⃗ΨW λD λ⃗ΨW DΨW λDΨW
⃗λ D
⃗ΨA λD λ⃗ΨA
DΨA
λDΨA
!
,
(10)
where ⃗λ = (λ, . . . , λ)T and ⃗ΨX = (ΨX, . . . , ΨX)T are col-
umn vectors of length 15 containing the predictor variables of
memory length and level of conscious arousal respectively, D
is the 15 × 15 identity matrix which “selects out" the channel
of interest, DΨX = diag(ΨX, . . . , ΨX) is the 15 × 15 matrix
which “selects out" the condition of interest correlated with
the level of conscious arousal, where
ΨW (A) =
(
1
if ψ = wakeful (anaesthetised)
0
otherwise.
(11)
In a similar fashion, the expression for the matrix contain-
ing the random effects R can be determined. For the case of
our study, we only consider random effects arising due to cor-
relations between channels within a speciﬁc ﬂy. The result of
this is an adjustment to the intercept of the linear model for
each ﬂy and channel combination. Therefore, the random ef-
fects matrix R is simply an identity matrix of dimension 390.
The accompanying elements of the random effects vector b
consist of regression coefﬁcients bfc describing the strength
of each intercept adjustment.
The execution of the LME analysis which included coefﬁ-
cient ﬁtting, and log-likelihood estimations was facilitated by
running fitlme.m in MATLAB R2108b.
[1] S. Thurner, P. Klimek, and R. Hanel, Introduction to the The-
ory of Complex Systems (Oxford University Press, Oxford,
2018).
[2] M. S. Gazzaniga, The Cognitive Neurosciences, 4th ed. (The
MIT Press, 2009).
[3] M. Boly, A. Seth, M. Wilke, P. Ingmundson, B. Baars, S. Lau-
reys, D. Edelman,
and N. Tsuchiya, Front. Psychol. 4, 625
(2013).
[4] S. Laureys and N. D. Schiff, Neuroimage 61, 478 (2012).
[5] S. Laureys, O. Gosseries, and G. Tononi, The Neurology of
Consciousness, 2nd ed. (Elsevier, 2015).
[6] D. A. Engemann, F. Raimondo, J.-R. King, B. Rohaut,
G. Louppe, F. Faugeras, J. Annen, H. Cassol, O. Gosseries,
D. Fernandez-Slezak, et al., Brain 141, 3179 (2018).
[7] J. D. Sitt, J.-R. King, I. El Karoui, B. Rohaut, F. Faugeras,
A. Gramfort, L. Cohen, M. Sigman, S. Dehaene, and L. Nac-
cache, Brain 137, 2258 (2014).
[8] M. Massimini, F. Ferrarelli, R. Huber, S. K. Esser, H. Singh,
and G. Tononi, Science 309, 2228 (2005).
[9] A. G. Casali, O. Gosseries, M. Rosanova, M. Boly, S. Sarasso,


## Page 13


13
Q
1st Order
2nd Order
3rd Order
C+
µ
λ : χ2(1) = 443.64
p < 10−16
λc : χ2(14) = 42.876
p = 8.97 × 10−5 λcψ : χ2(14) = 24.00
p = 0.0458
λψ : χ2(1) = 14.63
p = 1.31 × 10−4
∆C+
µ
λ : χ2(1) = 20.97
p = 4.65 × 10−6 λc : χ2(14) = 37.19
p = 6.90 × 10−4
Ξ
ψ : χ2(1) = 4.870
p = 0.0273
λψ : χ2(1) = 5.565
p = 0.0183
λcψ : χ2(14) = 31.79
p = 4.29 × 10−3
λ : χ2(1) = 6.725
p = 9.51 × 10−3
d
ψ : χ2(1) = 5.896
p = 0.0152
λψ : χ2(1) = 6.119
p = 0.0134
λ : χ2(1) = 460.5
p < 10−16
λc : χ2(14) = 35.86
p = 1.09 × 10−3
DKLS λ : χ2(1) = 127.4
p < 10−16
λc : χ2(14) = 85.81
p < 10−16
λψ : χ2(1) = 127.4
p < 10−16
Table I. Signiﬁcant χ2 and p values of effects of channel c, memory length λ, and condition ψ, for informational quantities Q obtained via
LME analysis. First order effects correspond to signiﬁcant channel, memory, or condition responses on an informational quantity, while
second and third-order effects correspond to interactions between these effects. χ2 values are reported with n −1 degrees of freedom in the
parentheses, corresponding to the number of effects removed under the null model, described in Sec. III A
K. R. Casali, S. Casarotto, M.-A. Bruno, S. Laureys, G. Tononi,
and M. Massimini, Sci. Transl. Med. 5, 198ra105 (2013).
[10] S. Casarotto, A. Comanducci, M. Rosanova, S. Sarasso,
M. Fecchio, M. Napolitani, A. Pigorini, A. G. Casali, P. D. Tri-
marchi, M. Boly, O. Gosseries, O. Bodart, F. Curto, C. Landi,
M. Mariotti, G. Devalle, S. Laureys, G. Tononi, and M. Mas-
simini, Ann. Neurol. 80, 718 (2016).
[11] G. Tononi, BMC Neurosci. 5, 42 (2004).
[12] G. Tononi, M. Boly, M. Massimini, and C. Koch, Nat. Rev.
Neurosci. 17, 450 (2016).
[13] M. Oizumi, L. Albantakis,
and G. Tononi, PLOS Comput.
Biol. 10, e1003588 (2014).
[14] P. A. M. Mediano, A. K. Seth, and A. B. Barrett, Entropy 21,
17 (2019).
[15] A. B. Barrett and A. K. Seth, PLOS Comput. Biol. 7, e1001052
(2011).
[16] M. Tegmark, PLOS Comput. Biol. 12, e1005123 (2016).
[17] M. Oizumi, N. Tsuchiya, and S. Amari, Proc. Natl. Acad. Sci.
113, 14817 (2016).
[18] M. Oizumi, S. Amari, T. Yanagawa, N. Fujii, and N. Tsuchiya,
PLOS Comput. Biol. 12, 1 (2016).
[19] G. Buzsaki, Rhythms of the Brain (Oxford University Press,
2006).
[20] J. P. Crutchﬁeld and K. Young, Phys. Rev. Lett. 63, 105 (1989).
[21] N. F. Travers and J. P. Crutchﬁeld, arXiv:1111.4500 (2011).
[22] J. P. Crutchﬁeld, arXiv:1710.06832 (2017).
[23] R. Heinz Haslinger, K. Lisa Klinkner, and C. Rohilla Shalizi,
Neural Comput. 22, 121 (2009).
[24] K. Klinkner, C. Shalizi, and M. Camperi, in Advances in neu-
ral information processing systems (2006) pp. 667–674.
[25] C. R. Shalizi and K. L. Klinkner, in Uncertainty in Artiﬁcial
Intelligence: Proceedings of the Twentieth Conference (UAI
2004), edited by M. Chickering and J. Y. Halpern (AUAI Press,
Arlington, Virginia, 2004) pp. 504–511.
[26] D. Varn and J. Crutchﬁeld, Phys. Lett. A 324, 299 (2004).
[27] F. Boschetti, Ecol. Complex. 5, 37 (2008).
[28] J. B. Park, J. W. Lee, J.-S. Yang, H.-H. Jo, and H.-T. Moon,
Physica A 379, 179 (2007).
[29] D. Cohen, O. H. Zalucki, B. van Swinderen, and N. Tsuchiya,
eNeuro 3 (2016).
[30] D. Cohen, B. van Swinderen,
and N. Tsuchiya, eNeuro 5
(2018).
[31] J. Hohwy, The Predictive Mind (Oxford University Press,
United Kingdom, 2013).
[32] G. Tononi, Arch. Ital. Biol. 148, 299 (2010).
[33] J. P. Crutchﬁeld, C. J. Ellison, and J. R. Mahoney, Phys. Rev.
Lett. 103, 094101 (2009).
[34] L. R. Rabiner, Proc. IEEE 77, 257 (1989).
[35] J. L. Doob, Stochastic Processes (Wiley, New York, 1953).
[36] M. Gu, K. Wiesner, E. Rieper, and V. Vedral, Nat. Commun.
3, 762 (2012).
[37] P. A. Gagniuc, Markov chains: from theory to implementation
and experimentation (John Wiley & Sons, 2017).
[38] P. Tino and G. Dorffner, Mach. Learn. 45, 187 (2001).
[39] J. P. Crutchﬁeld and K. Young, “Computation at the onset of
chaos,” in Entropy, Complexity, and the Physics of Informa-
tion, Vol. 8, edited by W. Zurek (Addison-Wesley, Reading,
Massachusetts, 1990) pp. 223–269.
[40] F. J. Massey, J. Am. Stat. Assoc. 46, 68 (1951).
[41] M. Hollander, D. A. Wolfe, and E. Chicken, Nonparametric
statistical methods, Vol. 751 (John Wiley & Sons, 2013).
[42] The distance DKS = max |F(rk|S = Si)−F(rk|
⃗
rℓ)|, where
F(rk|S = Si) and F(rk|
⃗
rℓ) are cumulative distributions of
P(rk|S = Si) and P(rk|
⃗
rℓ) respectively.
[43] L. H. Miller, J. Am. Stat. Assoc. 51, 111 (1956).
[44] K. Marton and P. C. Shields, Ann. Probab. 23 (1994).
[45] T. M. Cover and J. A. Thomas, Elements of Information Theory
(Wiley, New York, 1991).
[46] C. Yang,
F. C. Binder,
M. Gu,
and T. J. Elliott,
arXiv:1909.08366 (2019).
[47] Z. Rached, F. Alajaji, and L. L. Campbell, IEEE Trans. Inf.
Theory 50, 917 (2004).
[48] S. Amari, Information geometry and its applications, Vol. 194
(Springer, 2016).
[49] S. Amari, N. Tsuchiya, and M. Oizumi, in Information Geom-
etry and Its Applications, edited by N. Ay, P. Gibilisco, and
F. Matús (Springer International Publishing, Cham, 2018) pp.
3–17.
[50] A. C. Paulk, Y. Zhou, P. Stratton, L. Liu,
and B. van
Swinderen, J. Neurophysiol. 110, 1703 (2013).
[51] L(N) ∼14 only serves as a lower bound on λ, past which
CSSR is guaranteed to return incorrect causal states for the
neural data. In practice, this may occur at even lower mem-
ory lengths than this limit. We observed this effect marked by


## Page 14


14
an exponential increase in the number of inferred causal states
for λ > 11, and thus excluded these memory lengths from the
study.
[52] X. A. Harrison, L. Donaldson, M. E. Correa-Cano, J. Evans,
D. N. Fisher, C. E. Goodwin, B. S. Robinson, D. J. Hodgson,
and R. Inger, PeerJ 6, e4794 (2018).
[53] D. Bates, M. Mächler, B. Bolker, and S. Walker, J. Stat. Softw.
67, 1 (2015).
[54] B. D. Johnson, J. P. Crutchﬁeld, C. J. Ellison, and C. S. Mc-
Tague, arXiv:1011.0036 (2010).
[55] G. Sugihara, R. May, H. Ye, C.-h. Hsieh, E. Deyle, M. Fogarty,
and S. Munch, Science 338, 496 (2012).
[56] S. Tajima, T. Yanagawa, N. Fujii, and T. Toyoizumi, PLOS
Comput. Biol. 11, e1004537 (2015).
[57] H.-P. Breuer, E.-M. Laine, and J. Piilo, Phys. Rev. Lett. 103,
210401 (2009).
[58] S. Sarasso, M. Boly, M. Napolitani, O. Gosseries, V. Charland-
Verville, S. Casarotto, M. Rosanova, A. G. Casali, J.-F.
Brichant, P. Boveroux, S. Rex, G. Tononi, S. Laureys,
and
M. Massimini, Curr. Biol. 25, 3099 (2015).
[59] L. D. Lewis, V. S. Weiner, E. A. Mukamel, J. A. Donoghue,
E. N. Eskandar, J. R. Madsen, W. S. Anderson, L. R. Hochberg,
S. S. Cash, E. N. Brown, and P. L. Purdon, Proc. Natl. Acad.
Sci. 109, E3377 (2012).
[60] D. Raccuglia, S. Huang, A. Ender, M.-M. Heim, D. Laber,
R. Suárez-Grimalt, A. Liotta, S. J. Sigrist, J. R. Geiger, and
D. Owald, Curr. Biol. 29, 3611 (2019).
[61] K. Friston, Nat. Rev. Neurosci. 11, 127 (2010).
[62] J. Tani and S. Nolﬁ, Neural Netw. 12, 1131 (1999).
[63] A. M. Bastos, W. M. Usrey, R. A. Adams, G. R. Mangun,
P. Fries, and K. J. Friston, Neuron, Neuron 76, 695 (2012).
[64] R. Cofré, L. Videla,
and F. Rosas, Entropy 21, e21090884
(2019).
[65] R. Cofré and C. Maldonado, Entropy 20, e20010034 (2018).
[66] U. Hasson, E. Yang, I. Vallines, D. J. Heeger, and N. Rubin, J.
Neurosci. 28, 2539 (2008).
[67] K. Diba and G. Buzsáki, Nat. Neurosci. 10, 1241 (2007).
[68] B. H. Edmonds, “Hypertext bibliography of measures of com-
plexity,” (1997).
[69] M. A. Valdez, D. Jaschke, D. L. Vargas, and L. D. Carr, Phys.
Rev. Lett. 119, 225301 (2017).
[70] B. Sundar, M. A. Valdez, L. D. Carr, and K. R. A. Hazzard,
Phys. Rev. A 97, 052320 (2018).
[71] P. Zanardi, M. Tomka, and L. C. Venuti, arXiv:1806.01421
(2018).
[72] D. P. Feldman and J. P. Crutchﬁeld, Phys. Lett. A 238, 244
(1998).
[73] M. Schartner, A. Seth, Q. Noirhomme, M. Boly, M.-A. Bruno,
S. Laureys, and A. Barrett, PLOS One 10, 1 (2015).
[74] C. J. Ellison, J. R. Mahoney, R. G. James, J. P. Crutchﬁeld, and
J. Reichardt, Chaos 21, 037107 (2011).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
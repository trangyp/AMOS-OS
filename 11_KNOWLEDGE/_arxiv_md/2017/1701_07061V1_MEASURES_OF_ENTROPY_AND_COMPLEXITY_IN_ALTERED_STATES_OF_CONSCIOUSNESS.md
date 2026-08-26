---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1701.07061v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1701.07061v1_Measures_of_Entropy_and_Complexity_in_altered_states_of_consciousness

> Source: 1701.07061v1_Measures_of_Entropy_and_Complexity_in_altered_states_of_consciousness.pdf

> Pages: 9

---


## Page 1


Measures of Entropy and Complexity in altered states of consciousness
D. M. Mateos1∗, R. Guevara Erra2, R. Wennberg3, J.L. Perez Velazquez1
1 Neuroscience and Mental Health Programme, Division of Neurology, Hospital for Sick Children.
Institute of Medical Science and Department of Paediatrics, University of Toronto, Toronto, Canada.
2 Laboratoire Psychologie de la Perception, CNRS and Université Paris Descartes, Sorbonne Paris Cité, Paris, France.
3 Krembil Neuroscience Centre, Toronto Western Hospital, University of Toronto, Toronto, Canada.
* mateosdiego@gmail.com
January 26, 2017
Abstract
Quantiﬁcation of complexity in neurophysiological signals has been studied using diﬀerent methods, espe-
cially those from information or dynamical system theory. These studies revealed the dependence on diﬀerent
states of consciousness, particularly that wakefulness is characterized by larger complexity of brain signals
perhaps due to the necessity of the brain to handle varied sensorimotor information. Thus these frameworks
are very useful in attempts at quantifying cognitive states. We set out to analyze diﬀerent types of signals
including scalp and intracerebral electroencephalography (EEG), and magnetoencephalography (MEG) in
subjects during diﬀerent states of consciousness: awake, sleep stages and epileptic seizures. The signals were
analyzed using a statistical (Permutation Entropy) and a deterministic (Permutation Lempel Ziv Complexity)
analytical method. The results are presented in a complexity vs entropy graph, showing that the values of
entropy and complexity of the signals tend to be greatest when the subjects are in fully alert states, falling
in states with loss of awareness or consciousness. These results are robust for all three types of recordings.
We propose that the investigation of the structure of cognition using the frameworks of complexity will reveal
mechanistic aspects of brain dynamics associated not only with altered states of consciousness but also with
normal and pathological conditions.
1
Introduction
Multitude of studies focus on the investigation of patterns of correlated activity among brain cell ensembles
based on magnitudes of a variety of synchrony indices or similar measures. A prominent common aspect that is
emerging from those studies is that of the importance of the variability in the brain coordination dynamics. In
general, neurophysiological signals associated with normal cognition demonstrate ﬂuctuating patterns of activity
that represent interactions among cell networks distributed in the brain [1]. This variability allows for a wide
range of conﬁgurations of connections among those net-works exchanging information, and thus it supports the
ﬂexibility needed to process sensory inputs. Therefore, it has been argued that a certain degree of complexity
in brain signals will be associated with healthy cognition, whereas low complexity may be a sign of pathologies
[2, 3, 4]. We sought to obtain evidence for the correlation between complexity in brain signals and conscious
states, using brain electrophysiological recordings in conscious and unconscious states.
There exist a number of statistical measures to analyses electrophysiological recording [5]. In our work we use
two well knows measures, one statistical –Shannon entropy, a measure of unpredictability of information content
in a message [6] and the other deterministic the Lempel-Ziv complexity based in the minimum information required
to recreate the original signal [7]. For both measures, we use use the quantiﬁers introduced by Bandt and Pompe
[8], called permutation vectors, these are based on the relationship of the neighbour values belonging a time series.
The Shannon entropy applying to the permutation vector is knowing as permutation entropy (HPE) [8]. In a
similar manner the Lempel-Ziv complexity applied to the permutation vectors is called permutation Lempel-Ziv
complexity (PLZC) [9]. We used these two method to obtain information about the signals dynamics from two
diﬀerents perspective, probabilistic (HPE) and deterministic (PLZC). The permutation entropy and the Lempel-
Ziv complexity have been employed in previous studies analyzing electrophysiological recording in epilepsy, coma
or sleep stages [10, 11, 12, 13, 14]. Moreover , there is an interesting relation, under certain restrictions, between
the Shannon entropy and the Lempel-Ziv complexity that naturally can extend to the HPE and PLZC [15, 9].
The result we obtain are shown in a complexity-entropy graph.
This kind of representation allows us to
visualize better the results. In a recent study on chaotic maps and random sequences, it was shown that the
complexity-entropy graph allows the distinction of diﬀerent dynamics which are impossible to discern using
1
arXiv:1701.07061v1  [q-bio.NC]  9 Jan 2017


## Page 2


each analysis separately ( [16], unpublished results). In our work we analyze brain signals recorded using scalp
(EEG), intracranial electroencephalogram (iEEG) and magnetoencephalogram (MEG), in fully alert states and
in two conditions where consciousness is impaired: seizures and sleep. The hypothesis derived from the previous
consideration on the variability of activity is that the brain tends towards larger complexity and entropy in
wakefulness as compared with the altered states of consciousness.
2
Methods
Electrophysiological recordings
Recordings were analysed from 9 subjects using magnetoencephalography (MEG), scalp electroencephalography
(EEG) or intracranial EEG (iEEG). Three epilepsy patients were studied with MEG; one epilepsy patient was
studied with iEEG; 3 epilepsy patients were studied with simultaneous iEEG and scalp EEG; and 2 nonepileptic
subjects were studied with scalp EEG.
For the study of seizures versus alert states, the three subjects with MEG recordings and the one with iEEG
were used. Details of the patients’ epilepsies, seizure types and the recording speciﬁcs have been presented in
previous studies (MEG patients in [17], 2005; iEEG patients in [18]). For the study of sleep versus alert states,
the 3 patients with combined iEEG and scalp EEG have been described previously (patients 1, 3, 4 in [19]); the 2
subjects studied with scalp EEG alone had been investigated because of a suspected history of epilepsy, but both
were ultimately diagnosed with syncope, with no evidence of epilepsy found during prolonged EEG monitoring.
In brief, the MEG seizure recordings were obtained in one patient with primary generalized absence epilepsy,
in one patient with symptomatic generalized epilepsy, and in one patient with frontal lobe epilepsy. The iEEG
seizure recordings were obtained from a patient with medically refractory temporal lobe epilepsy as part of the
patient’s routine clinical pre-surgical investigation.
MEG recordings were obtained using a whole head CTF MEG system (Port Coquitlam, BC, Canada) with
sensors covering the entire cerebral cortex, whereas iEEG electrodes were positioned in various locations including
the temporal lobe epilepsy patient, the amygdala and hippocampal structures of both temporal lobes. EEG
recordings were obtained using an XLTEK EEG system (Oakville, ON, Canada). The details of the acquisitions
varied from patient to patient (e.g., acquisition rate varied from 200 to 625 Hz) and were taken into consideration
for the data analyses. The duration of the recordings varied as well: for the seizure study, the MEG sample
epochs were of 2 minutes duration each, with total recording times of 30-40 minutes; the iEEG patient sample
was of 55 minutes duration. The sleep study data segments were each 2-4 minutes in duration, selected from
continuous 24-hour recordings.
Data analysis
The data were analyzed throw the permutation Lempel Ziv complexity (PLZC) and the permutation entropy
(PE). Due the relationship existing between these quantities the result were shown in a complexity-entropy graph,
to extract information from the signals either deterministic to statistic. In this section we give a breve explanation
of both method and the relationship between then.
Permutation entropy
The permutation entropy (HPE) is a measure develop by Bandt and Pompe [8], for time series based on com-
paring neighboring values. The continuous time series is mapped onto a sequence of symbols which describe the
relationship between present values and a ﬁxed number of equidistant values at a given past time.
To understand the idea let us consider a real-valued discrete-time series {Xt}t≥0 , and let d ≥2 and τ ≥1 be
two integers. They will be called the embedding dimension and the time delay, respectively. From the original
time series, we introduce a d-dimensional vector Y (d,τ)
t
:
Y(d,τ)
t
→(Xt−(d−1)τ, ..., Xt−τ, Xt); t ≥(d −1)τ
There are conditions on d and τ in order that the vector Y(d,τ)
t
preserves the dynamical properties of the full
dynamical system1. The components of the phase space trajectory Y(d,τ) are sorted in ascending order. Then,
we can deﬁne a permutation vector, Πd,τ
t
, with components given by the position of the sorted values of the
component of Y(d,τ)
t
Each one of these vectors represents a pattern (or motif). There are d! possible patterns. It
is possible to calculate the frequencies of occurrence of any of the d! possible permutation vectors. From these
1For EEG signals values of d = 3, ..., 7 have been recommended [8]; For the time lag, it is adequate to use a value of τ = 1 [20],
For all signals in this work we used the parameter d = 3, .., 6 and τ = 1.
2


## Page 3


frequencies, we can estimate the Shannon entropy associated with the probability distributions of permutation
vector. If we denote the probability of occurrence of the i-th pattern by P(Πd,τ)i = Pi with i ≤d! then the
(normalized) permutation entropy associated with the time series {Xt} is (measured in bits):
HP E = −Pd!
i=1 Pi log2Pi
log2d!
(1)
The fundamental assumption behind the deﬁnition of HPE is that the d! possible permutation vectors might not
have the same probability of occurrence, and thus, this probability might unveil knowledge about the underlying
system.
Permutation Lempel-Ziv complexity
Entropy is a statistical characterization of a random variable and/or sequence. An alternative caracterization of
time series is the deterministic notion of complexity of sequences due to Kolomogorof. In this view, complexity
is deﬁned as the size of the minimal (deterministic) program (or algorithm) allowing to generate the observed
sequence [15, Chap. 14]. Later on, Lempel and Ziv proposed to deﬁne such a complexity for the class of “programs”
based on recursive copy-paste operators [7].
To be more precise, let us consider a ﬁnite-size sequence S1:T = S1...ST of size T, of symbols Si that take
their values in an alphabet A of ﬁnite size α = |A|. The deﬁnition of the Lempel–Ziv complexity lies in the two
fundamental concepts of reproduction and production:
• Reproduction: it consists of extending a sequence S1:T by a sequence Q1:N via recursive copy-paste opera-
tions, which leads to S1:T +N = S1:T Q1:N, i.e., where the ﬁrst letter Q1 is in S1:T , let us say Q1 = Si, the
second one is the following one in the extended sequence of size T + 1, i.e., Q1 = Si+1 , etc.: Q1:N is a
subsequence of S1:T +N−1. In a sense, all of the “information” of the extended sequence S1:T +N is in S1:T .
• Production: the extended sequence S1:T +N is now such that S1:T +N−1 can be reproduced by S1:T , but
the last symbol of the extension can either follow the recursive copy-paste operation (thus we face to a
reproduction) or can be “new”. Note thus that a reproduction is a production, but the converse is false.
Let us denote a production by S1:T ⇒S1:N+T .
Any sequence can be viewed as constructed through a succession of productions, called a history H. For
instance, a history of S1:T can be H(S1:T ) : ∅⇒S1 ⇒S1:2 ⇒· · · ⇒S1:T . The number the productions used for
the generation CH(S1:T ) is in this case equals to the size of the sequence. A given sequence does not have a unique
history and in the spirit of the Kolmogorov complexity, Lempel and Ziv were interested in the optimal history,
i.e., the minimal number of production necessary to generate the sequence. The size of the shortest history is the
so-called Lempel–Ziv complexity, denoted as C[S1:T ] = minH(S1:T ) CH(S1:T ) [7]. In a sense, C[S1:T ] describes the
“minimal” information needed to generate the sequence S1:T by recursive copy-paste operations.
As explained above, the Lempel–Zip complexity (CLZ) needed a alphabet of ﬁnite size to be used. In continuos
time series as EEG or MEG it is necessary to discretized the series before calculating the CLZ. Using the same
idea that in permutation entropy can be taken the alphabet as the set of permutation vectors A = {Π(d,τ)} and
the alphabet large α = |d!|. This is called permutation Lempel–Ziv complexity (PLZC)2 [9]
The most interesting thing is although analyzing a sequence from a completely deterministic point of view,
it appears that CLZ[S1:T ] sometimes also contains the concept of information in a statistical sense. Indeed, it
was shown in references [15, 7] that for a random stationary and ergodic process, when correctly normalized, the
Lempel-Ziv complexity of the sequence tends to the entropy rate of the process; this result were extend to the
permutation Lempel-Ziv complexity and the permutation entropy [9]; i.e.,
lim
T →+∞CLZ[S1:T ]log(T)
T
=
lim
T →+∞
HP E[S1:T ]
T
(2)
where HP E[S0:T −1] is the joint permutation entropy of the T symbols, and the righthand side is the permutation
entropy rate (entropy per symbol) of the process.
Such a property gave rise to the use of the permutation
Lempel-Ziv complexity for permutation entropy estimation purposes.
3
Results
The results obtained with recordings acquired during conscious state are compared with those acquired during
unconscious states, with include sleep (all stages) and epileptic seizures. We note that while we work at the
2 From now we call the permtation Lempel–Ziv complexity as CLZ
3


## Page 4


signal level we made the reasonable assumption that the MEG and scalp EEG sensors record cortical activity
underlying those sensors and thus throughout the text we used the term brain signals. On the other hand, the
iEEG, obviously, records signals at the source level. For all the signals the permutation vector parameter used
were d = 3, ..., 6 and τ = 1.
3.1
Entropy-complexity analysis from epileptic recordings
To visualize the dynamics of entropy and complexity in the time, we use a non overlapping running window
(∆= 625) corresponding to 1s MEG recording points. For each window the PLZC and HPE were calculated.Fig. 1
shows the complexity (PLZC) and entropy (HPE) values correspond to a MEG recording from a patient suﬀering
primary generalized epilepsy (A), secondary generalized epilepsy (B) and an frontal lobe epilepsy (C). For patients
A and B the entropy and complexity values represented were calculated the average over the 143 channels. For
patient C the values in each plot correspond a particular channel.
One MEG channel corresponding to patient A, are shown in the inset of Fig. 1A), where the seizure is visible as
a high amplitude in signal. The complexity-entropy graph depict clearly the dynamics of the ictal event. During
conscious states (baseline) – when patients remain conscious since they are not having generalized seizures– the
PLZC and HPE tent to maximum values, but as the patients experience seizures both values decrease widely,
returning to the original baseline values after the event.
Similar result can be seen in patient B who had 7 seizures, the seizures are visible in the inset of Fig. 1B.
We can see in the graph that the baseline and the interictal activity – the recording between to seizures – reach
always the highest values in entropy and complexity, declining to values well below in the ictal state (seizure).
This result is repeated for each of the seizures.
In Fig. 1C we show the analysis for 4 diﬀerent MEG channels corresponding to: left frontal (LF23), left
temporal (LT5), left occipital (LO41) and right occipital (RO43). The ﬁrst two belong to the region where the
seizure spread. For all channels the values of HPE and PLZC are higher in baseline, however the entropy and
complexity decay in the most aﬀected areas (LF23, LT5), while for the other areas (LO41, RO43) the complexity
doesn’t change, there being a small decrease in entropy. Similar result were found in the signals of the other
epileptic patients, recorded with scalp EEG and iEEG.
A possible explanation for this decreas in complexity and entropy during seizures, is that there is higher
synchrony during ictal periods (seizures), therefore this causes the recording signals become more stereotyped,
the number of permutation vectors used to quantized the signals are smaller and more regular giving a lower
entropy and complexity. This will be further commented in the discussion.
3.2
Entropy-complexity analysis during sleep stages
Te recording in these cases were of 2-4 minutes duration during wakefulness with eyes opened (’Awake’) or closed,
and in sleep stages slow-wave 2 (Sws2), slow-wave 3-4 (Sws3-4) and rapid eye movement (’REM’). Fig. 2A shows
entropy and complexity values applying to 4 whole recording (iEEG channels): left frontal media (LFM1), right
frontal media (RFM4), left temporal anterior (LTA1), right temporal anterior (RTA4). The various stages of
sleep are remarkably diﬀerentiated in the graph. Note how during wakefulness entropy and the complexity is in
the higher region of the graph, whereas for the slow wave stages, the values stay in the lower region. The deepest
sleep stage, slow wave 3-4 (sws 3-4), has consistently the lowest entropy and complexity. Interestingly, entropy
during REM sleep is very close, in most cases, to the normal, alert state. This result may not be as surprising
as it appeare, if we consider the mental activity during REM episodes that are normally associated with dreams.
The results are in agreement with those reported in [12, 13].
The results for 4 scalp EEG channels are shown in Fig. 2B, where the same result was obtained: higher
complexity and entropy for awake state and lower for deep sleep state. In this case, during REM, the values
remains between slow-wave period and wakefulness. For the other 2 subjects analyzed we obtained similar results.
This example demonstrates that the same qualitative result is obtained with diﬀerent recording techniques. The
similarity of the result indicate that these type of analysis is not inﬂuenced by the recording methodology.
4
Discusion
Our results indicate a pronounced loss of entropy and complexity in brain signals during unconscious states or
in states that do not represent full alertness (eyes closed). This is consistent with what the signals represent:
the coordinated collective activity of cell ensembles, which, in alert states, are responsible for optimal sensory
processing. This optimality requires certain variability in the interactions among those cell networks, which will
be conceivably represented in greater complexity.
4


## Page 5


Previous work has indicated less variability in the coordinated activity patterns in altered states of conscious-
ness, mainly derived from the analysis of synchronization in patients in coma [21, 22], or during seizures [17, 23].
A common feature of several theories of consciousness is the notion of a broad distribution of cellular interactions
in the brain that results in conscious awareness (reviewed in [24]). This requirement implies that a certain, high
degree of variability in the formation and dissolution of functional cell ensembles should take place [25], and
this variability will be reﬂected in higher complexity of the brain signals during alert states. Moreover in several
computational studies have revealed as well the lower complexity associated with epilepsy and abnormal cognitive
states, like schizophrenia [26]
In fully alert states, brain recordings exhibit higher frequencies of relatively low amplitude, and are less regular
than during other states where alertness is perturbed, including closing the eyes (when a prominent periodic
alpha rhythm appears in parieto-occipital areas, for instance). Brain cell ensembles that need to integrate and
segregate sensorimotor transformations while they receive rich sensory-motor inputs [27]; it is then conceivable
that these characteristics will be reﬂected in the high entropy and complexity values we observe. As consciousness
is gradually lost, during sleep, the values of entropy and complexity decrease because brain networks do not need
the richness in states needed to process the sensorium. The lack of arrival of multiple sensory inputs during
unconscious states decreases the need for neurons to display many diﬀerent ﬁring frequencies, since there is not
much integration/segregation being done at those stages and there is not much sensory load. One consequence of
this change in ﬁring patterns during unconscious states, particularly in sleep (for a comprehensive review of the
neurophysiological mechanisms leading to slow-wave sleep and other thalamocortical phenomena see [28]) is that
the high frequencies (gamma range) become less prominent and there is higher synchrony at lower frequencies. As
well, the amplitude of the slow waves is now high since there are more synchronized cells. Thus, all these events
result in the recording becoming more regular and exhibiting the typical slow wave frequencies, and therefore our
complexity measures decrease as compared to alert states. These results are consistent with measures obtained
from analysis of sleep EEG using permutation entropy [12] and other nonlinear measures, such as approximate
entropy, correlation dimension, recurrence plots and Hurst exponent, amongst others [29, 30, 31].
In the case of the epileptic recordings we have observed that the complexity and entropy values are larger in
the interictal stage (between seizures) and decline sharply in the ictal stage (seizures). This may be due to the fact
that seizures are characterized by excessive synchronous neuronal activity, which generates predominance of large
amplitude waveforms, the frequencies depending on the seizure type; e.g., the frequency is low in absence seizures
(3-4 Hz), but vary substantially in temporal lobe seizures. However, the frequencies remain relatively constant
for certain time periods (originating a distribution of periodic epochs, or laminar phases), that have been used in
the characterization of dynamical regimes in epileptiform activity [32], and therefore the complexity and entropy
tend to decrease. During the sleep stages we also found decreased entropy and complexity as compared with alert
states, a reﬂection of the aforementioned emergence of highly synchronous cell activity during slow wave sleep.
On the other hand, we found that complexity during REM sleep is similar to that of the awake state. This is
conceivable since REM episodes are normally associated with dreaming, and there is certain cognitive activity
going on in dreams, when there is partial awareness. Previous work has shown decreases in HPE and LZC in
patients under anesthesia eﬀects [14, 10, 33], thus the decreased complexity of brain signals in unconscious states
may be a common phenomenon.
Hence in the ﬁnal analysis what we measure, at the macro(meso)scopic level (through the recording of collective
cel activity in EEG or MEG), is a reﬂection of that the brain handles more information during wakefulness. A
larger code is required to manipulate more information.
The complexity/entropy of the signals used in this
work have been quantiﬁed through the Bandt and Pompe method [8], which focuses on the relative values of
neighbouring data points in a time series. Every embedding vector (or motif Πd,τ
i
) gives an idea of how the
waveform is, in a small section, of the original signal. As the original signal carries more variable information, the
waveform tend to be more ﬂuctuating, and the number of distinct motifs required to map it increases. Because
of that the probability distribution of motifs P(Πd,τ) tends to be uniform, and this caused entropy increase.
Besides, due to of the waveform ﬂuctuation, the PLZC increases too, since much more information is required
to reconstruct the signal. In contrast, for monotonal repetitive signals which have little new information, just a
limited number of motifs are required, e.g. for a sinusoidal signal the PLZC and HPE tend to be zero.
We note that our present resutls are complementary to those recently obtained using measures of coordinated
activity, namely the number of conﬁgurations of connections derived from an index of phase synchronization [1];
we should consider that the present analysis, done on the raw signals, represent too correlated activity as each
local ﬁeld potential (in case of iEEG) or signals recorded in scalp EEG or MEG represent the collective activity
in cell ensembles, thus these signals are themselves a measure of coordinated cell activity, and therefore it is not
surprising we obtain similar observations
It can be concluded that in the awake state, when information has to be handled is larger, the complexity
and entropy of the signals recorded from the brain tend to be higher than in absence of consciousness, a result
that stems from the distinct waveforms recorded in these mental states.
5


## Page 6


References
[1] R. M. Guevara Erra, D. M. Mateos, R. Wennberg, and J. L. Perez Velazquez. Towards a statistical mechanics
of consciousness: maximization of number of connections is associated with conscious awareness. Physical
Review E, (in press), 2016.
[2] Douglas D Garrett, Gregory R Samanez-Larkin, Stuart WS MacDonald, Ulman Lindenberger, Anthony R
McIntosh, and Cheryl L Grady. Moment-to-moment brain signal variability: a next frontier in human brain
mapping? Neuroscience & Biobehavioral Reviews, 37(4):610–624, 2013.
[3] Jose L Perez Velazquez, Miguel A Cortez, O Carter Snead, and Richard Wennberg. Dynamical regimes
underlying epileptiform events: role of instabilities and bifurcations in brain activity. Physica D: Nonlinear
Phenomena, 186(3):205–220, 2003.
[4] D. M. Mateos, J. M. Diaz, and P. W. Lamberti. Permutation entropy applied to the characterization of the
clinical evolution of epileptic patients under pharmacologicaltreatment. Entropy, 16(11):5668–5676, 2014.
[5] Katerina Hlaváčková-Schindler, Milan Paluš, Martin Vejmelka, and Joydeep Bhattacharya. Causality de-
tection based on information-theoretic approaches in time series analysis.
Physics Reports, 441(1):1–46,
2007.
[6] C. E. Shannon. A mathematical theory of communication. The Bell System Technical Journal, 27(4):623–656,
October 1948.
[7] A. Lempel and J. Ziv. On the complexity of ﬁnite sequences. IEEE Transactions on Information Theory,
22(1):75–81, January 1976.
[8] C. Bandt and B. Pompe. Permutation entropy: A natural complexity measure for time series. Physical
Review Letters, 88(17):174102, April 2002.
[9] S. Zozor, D. Mateos, and P. W. Lamberti. Mixing Bandt–Pompe and Lempel–Ziv approaches: another way
to analyze the complexity of continuous-states sequences. The European Physical Journal B, 87(5):107, kli
2014.
[10] E. Olofsen, J. W. Sleigh, and A. Dahan. Permutation entropy of the electroencephalogram: a measure of
anaesthetic drug eﬀect. British journal of anaesthesia, 101(6):810–821, 2008.
[11] E. Ferlazzo, N. Mammone, V. Cianci, S. Gasparini, A. Gambardella, A. Labate, M. A. Latella, V. Soﬁa,
M. Elia, F. C. Morabito, et al. Permutation entropy of scalp eeg: A tool to investigate epilepsies: Suggestions
from absence epilepsies. Clinical Neurophysiology, 125(1):13–20, 2014.
[12] N. Nicolaou and J. Georgiou. The use of permutation entropy to characterize sleep electroencephalograms.
Clinical EEG and Neuroscience, 42(1):24–28, 2011.
[13] A. G. Casali, O. Gosseries, M. Rosanova, M. Boly, S. Sarasso, K. R. Casali, S. Casarotto, M. Bruno,
S. Laureys, G. Tononi, et al. A theoretically based index of consciousness independent of sensory processing
and behavior. Science translational medicine, 5(198):198ra105–198ra105, 2013.
[14] X. S. Zhang, R. J. Roy, and E. W. Jensen. Eeg complexity as a measure of depth of anesthesia for patients.
Biomedical Engineering, IEEE Transactions on, 48(12):1424–1433, 2001.
[15] T. M. Cover and J. A. Thomas. Elements of Information Theory. John Wiley & Sons, Hoboken, New Jersey,
2nd edition, 2006.
[16] D. Mateos and S. Zozor. On the analysis of signals in a permutation lempel–ziv complexity - permutation
shannon entropy plane. Manuscript submitted for publication., 2016.
[17] L. Garcia Dominguez, R. A Wennberg, W. Gaetz, D. Cheyne, O. C. Snead, and J. L. Perez Velazquez.
Enhanced synchrony in epileptiform activity?
local versus distant phase synchronization in generalized
seizures. The Journal of neuroscience, 25(35):8077–8084, 2005.
[18] J. L. Perez Velazquez, L. G. Dominguez, V. Nenadovic, and R. A. Wennberg. Experimental observation of
increased ﬂuctuations in an order parameter before epochs of extended brain synchronization. Journal of
biological physics, 37(1):141–152, 2011.
6


## Page 7


[19] R. Wennberg.
Intracranial cortical localization of the human k-complex.
Clinical Neurophysiology,
121(8):1176–1186, 2010.
[20] A. A Bruzzo, B. Gesierich, M. Santi, C. A. Tassinari, N. Birbaumer, and G. Rubboli. Permutation entropy
to detect vigilance changes and preictal states from scalp eeg in epileptic patients. a preliminary study.
Neurological sciences, 29(1):3–9, 2008.
[21] Vera Nenadovic, James S Hutchison, Luis Garcia Dominguez, Hiroshi Otsubo, Martin P Gray, Rohit Sharma,
Jason Belkas, and Jose Luis Perez Velazquez. Fluctuations in cortical synchronization in pediatric traumatic
brain injury. Journal of neurotrauma, 25(6):615–627, 2008.
[22] V Nenadovic, J. L. Perez Velazquez, and J. S. Hutchison. Phase synchronization in electroencephalographic
recordings prognosticates outcome in paediatric coma. PloS one, 9(4):e94942, 2014.
[23] J. L. Perez Velazquez, L. Garcia Dominguez, and R. Wennberg. Complex phase synchronization in epileptic
seizures: evidence for a devil’s staircase. Physical Review E, 75(1):011922, 2007.
[24] P. C. Klink, M. W. Self, V. A.F. Lamme, P. R Roelfsema, and S.M. Miller. Theories and methods in the
scientiﬁc study of consciousness. The Constitution of Phenomenal Consciousness: Toward a Science and
Theory, 92, 2015.
[25] H. Flohr. Sensations and brain processes. Behavioural brain research, 71(1):157–161, 1995.
[26] G Karl Steinke and Roberto F Galán. Brain rhythms reveal a hierarchical network organization. PLoS
Comput Biol, 7(10):e1002207, 2011.
[27] G. Tononi. An information integration theory of consciousness. BMC neuroscience, 5(1):42, 2004.
[28] Alain Destexhe and Terrence J Sejnowski. Thalamocortical assemblies: How ion channels, single neurons
and large-scale networks organize sleep oscillations. 2001.
[29] J. Röschke and J.B. Aldenhoﬀ. A nonlinear approach to brain function: deterministic chaos and sleep eeg.
Sleep: Journal of Sleep Research & Sleep Medicine, 1992.
[30] R. Acharya, O. Faust, N. Kannathal, T. Chua, and S. Laxminarayan. Non-linear analysis of eeg signals at
various sleep stages. Computer methods and programs in biomedicine, 80(1):37–45, 2005.
[31] N. Burioka, M. Miyata, G. Cornélissen, F. Halberg, T. Takeshima, D. T. Kaplan, H. Suyama, M. Endo,
Y. Maegaki, T. Nomura, et al. Approximate entropy in the electroencephalogram during wake and sleep.
Clinical EEG and neuroscience, 36(1):21–24, 2005.
[32] J.L. Perez Velazquez, H. Khosravani, A. Lozano, B. Bardakjian, P. L. Carlen, R. Wennberg, et al. Type iii
intermittency in human partial epilepsy. European Journal of Neuroscience, 11(7):2571–2576, 1999.
[33] D. Li, X. Li, Z. Liang, L. J. Voss, and J. W. Sleigh. Multiscale permutation entropy analysis of eeg recordings
during sevoﬂurane anesthesia. Journal of neural engineering, 7(4):046010, 2010.
7


## Page 8


0.94
0.95
0.96
0.97
0.98
0.99
0.62
0.63
0.64
0.65
0.66
0.67
0.68
0.69
CLZ
HPE
  
BL
Sz
0.7
0.75
0.8
0.85
0.9
0.95
1
0.35
0.4
0.45
0.5
0.55
0.6
0.65
0.7
CLZ
HPE
  
BL
Sz 1
Sz 2
Sz 3
Sz 4
Sz 5
Sz 6
0.85
0.9
0.95
1
0.52
0.54
0.56
0.58
0.6
0.62
0.64
CLZ
HPE
0.8
0.85
0.9
0.95
1
0.4
0.45
0.5
0.55
0.6
0.65
HPE
0.9
0.92
0.94
0.96
0.98
0.54
0.56
0.58
0.6
0.62
0.64
HPE
0.88
0.9
0.92
0.94
0.96
0.98
0.5
0.52
0.54
0.56
0.58
0.6
0.62
HPE
 
 
BL
Sz
A
10 seg
B
60 seg
LF23
C
LT15
LO41
RO43
Figure 1:
Represent the permutation Lempel Ziv complexity (CLZ) vs permutation entropy (HP E) (with
parameter d = 4 and τ = 1) time tracking values for a MEG signal in epileptic patients during conscious, baseline
(BL) and unconscious, seizure (Sz) states. A) Patient with primary generalized epilepsy, the MEG signal for one
channel is plotted in the inset (the high amplitude represent the seizure). We observe that before the seizure
entropy and the complexity the values remains very high, decreasing in the seizure epoch and return to the
original values after the seizure. B) Patient with secondary generalized epilepsy, who had 7 seizure during the
recording period, is in the inset. When the patient stay in the inter-ictal state (no seizure period) entropy and
complexity values are higher and decreasing in the every attack. C) Patient suﬀering from frontal lobe epilepsy;
4 channels were analysed separately, left frontal (LF23), left temporal (LT5), left occipital (LO41), right occipital
(RO43). For the two recording areas aﬀecting by the seizure (LF23 and LT5) entropy and complexity change in
the ictal state, but for the areas which are not aﬀected (LO41 and RO43), the CLZ and HP E values are the same
that in baseline state. The same result we obtained for the parameter d = 3, 4, 5, 6 and τ = 1.
8


## Page 9


0.35
0.4
0.45
0.5
0.1
0.12
0.14
0.16
0.18
HPE
CLZ
0.35
0.4
0.45
0.5
0.55
0.11
0.13
0.15
0.17
0.19
HPE
 
 
Aw Oc
REM
Sws 2
Sws 3-4
0.44
0.46
0.48
0.5
0.14
0.15
0.16
0.17
CLZ
0.42
0.45
0.48
0.52
0.13
0.14
0.16
0.18
0.75
0.8
0.85
0.89
0.31
0.33
0.35
0.37
HPE
C
LZ
0.75
0.8
0.85
0.3
0.32
0.34
0.36
HPE
  
Aw Oc
REM
Sws 2
Sws 3-4
0.82
0.84
0.86
0.88
0.9
0.33
0.34
0.35
0.36
0.37
C
LZ
0.75
0.8
0.85
0.3
0.32
0.34
0.36
A
B
LTA1
RTA4
RFM4
LFM1
T1
O1
F3
F4
Figure 2:
A) Each windows the channel recording from one iEEG channels analyzing by the permutation
Lempel-Ziv complexity (CLZ) vs permutation entropy (HP E) graph (with parameter d = 4 and τ = 1), for a
patient recording during sleep. Data samples were of 2-4 minutes duration during wakefulness with eyes open
(’Aw Oe’) , and sleep stages slow-wave 2 (‘Sws2’), slow-wave 3-4 (‘Sws3-4’) and rapid eye movement (’REM’).
The electrode localization are: left frontal media (LFM1), rigth frontal media (RFM4), left temporal anterior
(LTA1), right temporal anterior (RTA4), the yellow circle show the position of the channel in the brain. When
the patient go in deeper sleep states, both PLZC and HPE decreases across all channels. B) The same analysis
as in A applied to another subject (scalp EEG channel recording), as in the previous one, awake state has the
higher entropy and complexity and the values decrease for deeper state of sleep. For the REM stage the values
are remains between the sleep stages and the wakefulness stage. The same result we obtained for all patient
analyzed with the parameter d = 3, .., 6 and τ = 1.
9

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1701_07061v1_measures_of_entropy_and_complexity_in_altered_states_of_consciousness
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1701_07061V1_MEASURES_OF_ENTROPY_AND_COMPLEXITY_IN_ALTERED_STATES_OF_CONSCIOUSNESS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

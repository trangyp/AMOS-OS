---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1611.08913v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1611.08913v2_A_Simple_Model_of_Attentional_Blink

> Source: 1611.08913v2_A_Simple_Model_of_Attentional_Blink.pdf

> Pages: 14

---


## Page 1


A Simple Model of Attentional Blink
Nadav Amir
The Edmond and Lily Safra Center for Brain Sciences
The Hebrew University of Jerusalem
nadav.amir2@mail.huji.ac.il
Israel Nelken
Department of Neurobiology, Institute for Life Sciences &
The Edmond and Lily Safra Center for Brain Sciences
The Hebrew University of Jerusalem
israel@cc.huji.ac.il
Naftali Tishby
The Rachel and Selim Benin School of Computer Science and Engineering &
The Edmond and Lily Safra Center for Brain Sciences
The Hebrew University of Jerusalem
tishby@cs.huji.ac.il
September 28, 2017
Abstract
The attentional blink (AB) effect is the reduced ability of subjects to report a second target stimuli (T2) among
a rapidly presented series of non-target stimuli, when it appears within a time window of about 200-500 ms
after a ﬁrst target (T1). We present a simple dynamical systems model explaining the AB as resulting from
the temporal response dynamics of a stochastic, linear system with threshold, whose output represents the
amount of attentional resources allocated to the incoming sensory stimuli. The model postulates that the
available attention capacity is limited by activity of the default mode network (DMN), a correlated set of
brain regions related to task irrelevant processing which is known to exhibit reduced activation following
mental training such as mindfulness meditation. The model provides a parsimonious account relating key
ﬁndings from the AB, DMN and meditation research literature, and suggests some new testable predictions.
I.
Introduction
Questions regarding the characteristics, and
limitations, of attention allocation over time
have attracted considerable interest over the
last decades (see [1] for an overview). More
recently, it has been shown that intensive men-
tal training, in the form of mindfulness med-
itation, can modulate the control of attention
allocation over time [2, 3, 4], yet the computa-
tional and neural mechanisms underlying this
process remain unclear. A possible clue lies
in the recent deluge of studies concerning the
so called default mode network (DMN) (see
[5, 6] for reviews): an anatomically deﬁned, in-
terconnected system of cortical regions which
are preferentially activated when individuals
are involved in self referential processing and
mind wandering, rather than paying attention
to the external environment [7, 8, 9]. Various
meditation practices have been shown to be
associated with reduced activity levels of the
DMN [10, 11, 12, 13], as well as improved sus-
tained [14] and selective [3] attention capabili-
1
arXiv:1611.08913v2  [q-bio.NC]  27 Sep 2017


## Page 2


ties.
Here we describe a simple dynamical sys-
tems model suggesting that changes in DMN
activity levels can modulate attentional capac-
ity.
The proposed mechanism is quite gen-
eral in nature but we demonstrate it using the
well-known attentional blink (AB) paradigm
[15, 16], which is the reduced ability (“blink-
ing") of subjects asked to report a second tar-
get stimuli in a rapid serial visual presenta-
tion (RSVP) task, when it appears within a
time window of about 200-500 ms after the
ﬁrst one. This AB effect has played a central
role in studying the limits of humans’ ability
to allocate attention over time (for reviews see
[17, 18]) and more recently has also been used
to study the effects of mental training (in the
form of mindfulness meditation) on the tempo-
ral distribution of attentional resources [2, 3, 4].
While several theoretical accounts have been
suggested over the last decade for explaining
the AB (see discussion below), the model pro-
posed here has the advantage of being sim-
ple and parsimonious in parameters, while ac-
counting for many empirical ﬁndings relating
the AB, DMN and mental training research
literature. Additionally, it provides testable
hypotheses relating changes in DMN activity
levels with performance in attention demand-
ing tasks and associated ERP amplitudes.
II.
Methods
i.
Basic description of the model
Formally, we model the “attentional channel”
as a linear time-invariant (LTI) system [19] with
additive Gaussian noise and an upper response
threshold (Eq. 1). The system’s output, or re-
sponse, y(t), corresponds to the amount of at-
tentional resources currently used by the brain.
When this response reaches a predetermined
blinking threshold, y(t) = yB, the attentional
resources are exhausted and the system can-
not respond to incoming stimuli for a short
“refractory” period, resulting in decreased iden-
tiﬁcation of the subsequent target stimuli - the
AB effect.
The system’s response consists of determin-
istic and stochastic components. The former
is given by a convolution of the input stim-
uli’s cognitive representation uc(t) (see next sub-
section), with the system’s impulse response
function h(t), which describes the time course
of the system’s response to a pulse shaped
input. The stochastic part of the response is
given by the additive Gaussian random vari-
able nDMN(t) „ N (µDMN, σ2
DMN), with µDMN
representing the DMN activity baseline (mean)
and σDMN its ﬂuctuations (standard deviation).
Conceptually, DMN activity is represented by
the model as task irrelevant noise loading the
attentional system and thus modulating blink-
ing propensity.
To summarize, we present a model describ-
ing the temporal capture of attention using a
dynamical system described by Eq. 1, which
is speciﬁed by the cognitive representation of
the input stimuli uc(t), the blinking threshold
yB, the impulse response function h(t) and the
DMN noise nDMN.
y(t) = min
#
uc(t) ˚ h(t) + nDMN(t)
yB
(1)
ii.
Cognitive representation of input
stimuli
In line with other two-stage accounts of the
AB (e.g. [20, 16] and see discussion below),
the model assumes that sensory stimuli un-
dergo an initial cognitive representation stage
before they can be further processed, or consol-
idated into working memory. The input sen-
sory stimuli stream is represented by a discrete
(10Hz) signal of impulses us(t), with ampli-
tudes corresponding to stimulus saliency. Tar-
get stimuli are represented as unit impulses
and non-targets as zeros, i.e.
us(t) = 1 if
one of the target stimuli (T1 or T2) appears
at time t and us(t) = 0 otherwise. This for-
mulation can be easily adjusted to account for
various target/distractor saliency relationships
by modulating the impulse amplitudes of the
different stimuli (see discussion section below).
Concretely, the representation stage is imple-
2


## Page 3


mented by resampling the sensory stimulus
signal us(t) at a higher sampling rate (1KHz),
and clipping it at a threshold value uc(t) = 1
(not to be confused with the blinking threshold
yB in Eq. 1). The resulting cognitive represen-
tation signal uc(t), is then used as input to the
attentional system described by Eq. 1. Con-
ceptually, resampling represents the temporal
resolution of the attentional system and clip-
ping corresponds to sub-linear combination of
temporally close sensory stimuli. Importantly,
the sub-linearity is most pronounced when the
two target stimuli appear successively, in which
case their combined cognitive representation
signal exhibits maximal overlap and clipping.
As discussed below, this sub-linear summation
of temporally proximal target stimuli can ex-
plain various effects related to the somewhat
counterintuitive ﬁnding that blinking is signif-
icantly attenuated when T2 appears directly
after T1 - the so called “lag-1 sparing” effect
[21].
iii.
DMN activity as attentional noise
A central feature of the model is its interpre-
tation of DMN activity as stochastic noise in
the attentional system. This is formally de-
scribed by the additive noise term nDMN(t) in
Eq. 1 which is a Gaussian random variable,
nDMN(t) „ N (µDMN, σ2
DMN), with mean and
variance corresponding to the DMN’s baseline
activity and moment-by-moment ﬂuctuation
levels respectively.
Conceptually, the mean
DMN activity level represents the underlying
mental state (e.g. mind wandering vs task en-
gagement), whereas the variance represents
momentary attentional ﬂuctuations around the
baseline level. A lower DMN activity level re-
sults in more attentional resources available for
task performance and less probability of cross-
ing the blinking threshold. This mechanism en-
ables the model to relate DMN activity and AB
task performance in a quantitative way. The
recognition probability of T2 can be directly
computed from the blinking gap, deﬁned as the
difference between yB (the blinking threshold),
and the maximal value of y(t) during the sys-
tem’s excitation by the stimulus inputs.
iv.
The impulse response function of
the attentional system
The impulse response function h(t), deter-
mines the temporal proﬁle of attentional re-
source allocation.
It is modeled here using
the Gamma (or Erlang) distribution function
(Eq. 2):
h(t) =
#
st(n´1)e´t/τ
t ą 0
0
t ď 0
(2)
Here n and τ are the shape and scale parame-
ters which ﬁx the half duration and maximum
response time of h(t) (Fig. 2) and the scaling
factor s controls the system’s gain. While the
precise form of h(t) is not of major signiﬁcance,
the Gamma distribution function is known to
provide a reasonably good ﬁt for attention re-
lated responses such as pupillary dilation (a
correlate of attentional effort) [22, 23] , tempo-
ral sensitivity in the visual system [24] and
even Blood-oxygen-level dependent (BOLD)
signal hemodynamic responses [25].
v.
The P3b brain potential
The P3b is a positive ERP, peaking at around
300ms, associated with updating of working
memory [26, 27, 28] and attentional resources
allocation [29, 30]. To interpret the P3b ampli-
tude in terms of the model’s parameters, we
ﬁrst deﬁne the Resource Allocation Index (RAI),
as the ratio between attentional resources allo-
cated to the stimuli under consideration and
the total resources available (Eq. 3).
RAI = maxt y(t) ´ µDMN
yB ´ µDMN
(3)
The maximum is taken over the time period
during which the system is responding to the
stimuli under consideration. Note that the RAI
is a dimensionless number taking values be-
tween 0, corresponding to no excitation of the
attentional system and 1, representing maxi-
mal excitation or exhaustion of attentional re-
sources. Since P3b amplitude ranges typically
3


## Page 4


differ between subjects, even when performing
the same task, we deﬁne the model correlate of
the P3b amplitude as the RAI divided by the
subject speciﬁc DMN activity standard devia-
tion σDMN, which serves as a natural signal to
noise scaling factor in this context (Eq. 4).
P3b = RAI
σDMN
(4)
How are changes in DMN activity levels re-
ﬂected in the P3b amplitude deﬁned by equa-
tion 4?
For non-blinking trials, i.e.
when
RAI ă 1, the RAI and thus the P3b amplitude
increases as µDMN is decreased and σDMN re-
mains ﬁxed. However, when both µDMN and
σDMN are decreased, the expected P3b ampli-
tude may increase or decrease depending on
their speciﬁc values, since reducing σDMN re-
duces both the numerator in equation 3 and
the denominator in 4. For blinking trials, i.e.
when RAI = 1, the situation is simpler since
in this case P3b = σ´1
DMN regardless of µDMN’s
value.
III.
Results
We ﬁrst tested whether the model can repro-
duce the basic AB effect, namely a reduction in
detection accuracy of T2 within a time window
of approximately 200-500 ms after T1 presen-
tation. Due to the resampling of stimuli at
the cognitive representation stage, and the ﬁ-
nite rise and fall time of the system’s impulse
response function (Fig. 2), two targets which
appear close to each other will have overlap-
ping responses. This overlap can cause the
system’s response to the combined signal to
reach the blinking threshold, even though the
individual response to each one of the targets
does not do so (Fig. 1, top). As the time in-
terval between T1 and T2 increases, their over-
lap decreases and the system’s response to the
combined signal no longer reaches the blinking
threshold (Fig. 1, bottom). Importantly, when
T2 appears immediately after T1, the combined
response may not cross the blinking threshold
since in this case a signiﬁcant portion of the
overlap between targets is clipped at the cogni-
0
20
40
60
80
100
120
up(t)
0
1
T1
T2
0
200
400
600
800
1000
1200
uc(t)
-0.5
0
0.5
1
time (msec)
0
200
400
600
800
1000
1200
y(t)
0
20
40
60
0
20
40
60
80
100
120
up(t)
0
1
T1
T2
0
200
400
600
800
1000
1200
uc(t)
-0.5
0
0.5
1
time (msec)
0
200
400
600
800
1000
1200
y(t)
0
20
40
60
Figure 1: Attentional Blink model Top: When
T2 (in green) appears close (but not directly, see
Fig. 3) after T1 (blue), the blinking threshold
(red line) is reached and blinking occurs. Bot-
tom: When the time interval between T1 and
T2 is longer, both targets can be processed with-
out causing the system to reach the blinking
threshold.
4


## Page 5


Time
0
50
100
150
200
250
300
Amplitude
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
Figure 2: Impulse response function
The temporal response of the attentional sys-
tem to an impulse stimuli follows the Gamma
distribution function (Eq. 2). The values of
the shape and scale parameters used here are
n = 1 and τ = 0.05 respectively.
tive representation stage (Fig. 3), resulting in a
sub-linearly combined signal.
Next, we tested whether the effects of men-
tal training on AB performance and the corre-
sponding P3b ERP can be reproduced by the
model. In [2] it was shown that mental training,
in the form of a 3 month mindfulness medi-
tation retreat, resulted in signiﬁcantly lower
blinking probability and larger reduction in
T1 elicited P3b amplitudes for non-blinking vs
blinking trials in expert meditators compared
to a group of matched novice controls who did
not attend the retreat. Furthermore, the medi-
tators’ reduction in T1 evoked P3b amplitudes
was signiﬁcantly correlated with improvement
in T2 detection accuracy, suggesting that the
ability to detect T2 depends on efﬁcient deploy-
ment of attentional resources to T1 [2]. Using
the theoretical P3b amplitude deﬁned in Eq. 4,
the model was able to reproduce the three-way
interaction (meditators vs. novices, before vs.
after retreat, blinking vs. non-blinking trials),
Fig. 4, (cf. ﬁgure 3 in [2]), and the relationship
between T2 detection accuracy and reduction
in T1 elicited P3b amplitude. Fig. 5 bottom
right, (cf. ﬁgure 4 in [2]).
0
20
40
60
80
100
120
up(t)
0
1
T1
T2
0
200
400
600
800
1000
1200
uc(t)
-0.5
0
0.5
1
time (msec)
0
200
400
600
800
1000
1200
y(t)
0
20
40
60
T2-T1 lag
1
2
3
4
5
6
7
8
T2 detection probability
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Figure 3: Lag-1 sparing Top: When T2 (green)
appears immediately after T1 (blue), their
larger overlap at the cognitive representation
stage results in more clipping which in turn re-
duces the maximal response of the system and
decreases blinking probability. Bottom: Proba-
bility of T2 detection as a function of the time
lag between T1 and T2. This u-shaped proﬁle
is typical in AB experiments ([15]).
5


## Page 6


Blink
No Blink
0.2
0.25
0.3
Novices
Time 1
Blink
No Blink
0.2
0.25
0.3
Practitioners
Blink
No Blink
0.2
0.25
0.3
Time 2
Blink
No Blink
0.2
0.25
0.3
Time 1
Time 2
0.2
0.25
0.3
Novices
Blink
Time 1
Time 2
0.2
0.25
0.3
Practitioners
Time 1
Time 2
0.2
0.25
0.3
No blink
Time 1
Time 2
0.2
0.25
0.3
Figure 4: Effects of mental training on T1
elicited P3b Top: Modeled T1 evoked P3b
amplitude as a function of T2 accuracy: no-
blink vs. blink, session: Time 1 (before the
meditation retreat) vs. Time 2 (after the re-
treat), and group (practitioners vs. novices).
Meditation practitioners show a greater reduc-
tion in T1 evoked P3b amplitude compared
to novices in no-blink vs blink trials at time
2 vs time 1. Bottom: Selective reduction in
T1 evoked P3b amplitude in no-blink trials in
the practitioner group. DMN parameter levels
(µDMN, σDMN), for practitioners: (3.65, 28) at
time 1 and (3.5, 25) at time 2.
For novices:
(3.7, 30) at both times.
These results, and
choice of colors, follow ﬁgure 3 in [2].The larger
T1 evoked P3b amplitude for practitioners at
time 1, for blinking vs. non-blinking trials and
at time 2 vs. time 1, for blinking trials are novel
predictions of the model.
The model reproduced these results only for
certain values of DMN activity levels before
and after training. We thus wanted to iden-
tify all pairs of (µDMN, σDMN) points, repre-
senting DMN activity at times 1 and 2, which
reproduce the main ﬁndings reported in [2],
namely a reduction of about 25% in T1 elicited
P3b amplitude and an increase of about 20%
(from 60% to 80%) in T2 detection accuracy. In
addition to reproducing these empirical ﬁnd-
ings, we required that these points reproduce
the lag-1 sparing effect, which we deﬁned as
the condition of crossing the blinking thresh-
old for T2-T1 lags of 2 but not for lags 1 or 5
and higher. We plotted the probability of lag-1
sparing occurrence, as well as the model P3b
amplitude (Eq. 4) and T2 detection probability,
both at a T2-T1 lag of 4 (Fig. 5, top left, bottom
left and top right respectively). We then tested
which pairs of (µDMN, σDMN) points, repre-
senting DMN activity at time 1 and 2, yield
a substantial probability (ą 0.2) of lag-1 spar-
ing occurrence at both times and reproduce
the main empirical ﬁndings of [2] mentioned
above (Fig. 5, blue and red crosses, top left
and right and bottom left). For these pairs
of points, we plotted the change in T2 detec-
tion probability a function of the reduction in
P3b amplitude (Fig. 5, bottom right). This
yielded a set of DMN activity parameter pairs
which reproduce the empirical correlation be-
tween improvement in T2 detection accuracy
and reduction in T1 elicited P3b amplitude as
reported in ﬁgure 4 of [2]. Thus, the model
provides a quantiﬁable relationship between
DMN activity levels, AB task performance and
T1 evoked P3b amplitudes, which can presum-
ably be tested empirically.
IV.
Discussion
i.
Meditation, P3b and the default
mode network
Differences in attentional processing between
expert meditators and novices have been re-
ported in several studies over the last years
(for an overview see [3]). Of particular inter-
6


## Page 7


µDMN
25
30
35
σDMN
3
3.1
3.2
3.3
3.4
3.5
3.6
3.7
3.8
3.9
4
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
0.45
µDMN
25
30
35
σDMN
3
3.1
3.2
3.3
3.4
3.5
3.6
3.7
3.8
3.9
4
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
µDMN
25
30
35
σDMN
3
3.1
3.2
3.3
3.4
3.5
3.6
3.7
3.8
3.9
4
0.25
0.26
0.27
0.28
0.29
0.3
0.31
0.32
0.33
P3b amplitude, Time2-Time1
-0.095
-0.09
-0.085
-0.08
-0.075
-0.07
-0.065
-0.06
%T2 accuracy, Time2-Time1
-0.2
-0.1
0
0.1
0.2
0.3
0.4
0.5
Figure 5: Model behavior in DMN parameter
space Top left: lag-1 sparing probability as a
function of DMN activity parameters (mean
and variance). The color indicates the prob-
ability of crossing the blinking threshold at
lag 2 but not at lags 1 and 5. Top right: T2
detection probability for a T2-T1 lag of 4. Bot-
tom left: The model P3b amplitude deﬁned in
Eq. 4, for a T2-T1 lag of 4. Blue and red crosses
correspond to possible (µDMN, σDMN) values
at time 1 and time 2 respectively, for which
the model reproduces lag-1 sparing as well as
the main ﬁndings of [2], namely an increase
of T2 detection probability from about 60% to
about 80% (ibid. ﬁgure 2) and a reduction of
about 25% in P3b amplitude (ibid. ﬁgure 3)
and. Bottom right: Change in T2 detection ac-
curacy as a function of the change in P3b for
(µDMN, σDMN) pairs reproducing lag-1 sparing
and the effects of meditation (cf. ﬁgure 4. in
[2]).
est here is a study dealing with the effect of
meditation on the AB and the related P3b po-
tentials evoked during the task performance
[2]. The P3b wave is an event related potential
(ERP) component linked with attention alloca-
tion and memory encoding of targeted stim-
uli [29, 26]. The results reported in [2] show
that experienced meditators exhibit a smaller
attentional blink effect (higher T2 recognition
accuracy), and larger amplitudes of T1 evoked
P3b compared to a matched control group of
meditation novices. In addition, after attend-
ing a 3 month intensive meditation retreat, the
meditators showed a signiﬁcant reduction of T1
evoked P3b amplitudes but only during non-
blinking trials. The novice control group, who
did not attend the meditation retreat, showed
a signiﬁcantly smaller reduction in both at-
tentional blink size and T1 evoked P3b ampli-
tude. The magnitude of reduction in T1 evoked
P3b amplitudes during no-blink trials was cor-
related with the improvement in T2 recogni-
tion accuracy for both meditators and novices.
These results suggest that the ability to identify
T2 depends on efﬁcient attentional resource al-
location to T1 and that mental training, such as
mindfulness meditation, can improve this re-
source allocation process. The model suggests
a concrete mechanism, namely the reduction in
DMN noise levels, through which this process
can take place. This also provides a quanti-
tative interpretation of the widespread claim
that mindfulness meditation reduces ongoing
mental noise in the brain.
Interestingly, the T1 evoked P3b amplitudes
were larger for the experienced meditators com-
pared to the novices in all experimental con-
ditions (blinking and non-blinking trials, be-
fore and after the retreat), with the possible
exception of non-blinking trials after the re-
treat, where they were of comparable magni-
tude (ﬁgure 3. in [2]). The model suggests that
these differences may be due to smaller ﬂuctu-
ations (noise variance) in the DMN activity of
experienced meditators compared to novices.
Over the last few years, several studies have
shown that different types of meditation are
linked with reduced DMN activity levels com-
7


## Page 8


pared to rest [11, 14] and other active tasks [10].
It has also been shown recently that experi-
enced mindfulness meditators exhibit reduced
resting state DMN activity and ﬂuctuations
amplitudes during a visual memory task [13]
compared to novice controls. By proposing that
DMN activity reduction is the neural mecha-
nism by which meditation increases attentional
capacity, our model relates these studies with
the ﬁnding that meditation affects performance
and brain potentials in the AB task [2, 3, 4].
In a 2004 study measuring BOLD activation
levels during AB task performance [32], the
only brain area reported to exhibit decreased
activation for non-blinking vs. blinking trials
was the right temporoparietal junction (TPJ), a
DMN associated region known to deactivate
during attention demanding tasks [33]. Other,
non DMN related regions, showed the oppo-
site effect, namely increased activation during
non-blinking compared to blinking trials [32].
This ﬁnding is also in line with the model’s
hypothesis regarding the relationship between
DMN activity and blinking probability.
ii.
Comparison with existing models
Several mathematical models for the AB effect
have been suggested over the past decade or
so (for an overview see the section “Formal
Theories" in [17]). Formally, these models can
be divided into two classes: connectionist and
symbolic [34]. Connectionist, also known as
neural-network models (e.g [35, 36, 37, 38, 39]),
usually rely on tuning a large number of pa-
rameters without providing much insight re-
garding the underlying mechanisms. On the
other hand, symbolic, or computationalist mod-
els (e.g. [40, 41]), are often described using
complex box-and-arrow type rules which seem
rigid and ad-hoc. Another way of categoriz-
ing AB models is by the underlying cause for
blinking. The two pravelant mechanisms are ca-
pacity limitations and attentional control ([18]).
Models emphasizing capacitiy limits attribute
blinking to some resource bottleneck at the at-
tentional or working memory systems, while
those emphasizing a control mechanism posit
that blinking is due to top-down inhibition of
attention while T1 is being processed.
The model proposed here can be broadly
categorized as symbolic and capacity limited.
However, it is based on ﬁrst-principles (lin-
ear dynamical-systems) and is essentially de-
scribed by a single equation (Eq. 1) assum-
ing only a few free parameters. The model
also incorporates a top-down control element
by modulating the available attentional capac-
ity through changes in DMN activity. As dis-
cussed below, this element enables the model
to explain certain ﬁndings which challenge the
notion of a purely capacity-limited account of
the AB, such as the“spreading” of lag-1 sparing
(see below).
While simple, the model can explain many
ﬁndings from the AB literature and, in par-
ticular, reproduce the results reported in [2]
relating mental training with improved AB per-
formance and reduced P3b amplitudes. We
discuss below the central ﬁndings relating to
the AB and describe how they are accounted
for by the model.
ii.1
Reversal of T1 and T2
It has been reported that when T2 appears im-
mediately after T1 (lag 1 trials), identiﬁcation
of T2 is often superior to T1 and report order is
often reversed [42, 20]. The model is consistent
with these effects since it posits that during
the cognitive representation stage, T1 may be
partially occluded by T2 and both are merged
together into a single “cognitive” trace. This
process of occlusion and merging may explain
degredation of T1 detection probability and
T1,T2 order confusion.
ii.2
Spreading of the sparing
This refers to a set of ﬁndings showing that
AB can be attenuated or even eliminated as
long as a target is not followed by a distractor.
Thus, when subjects were presented with RSVP
streams containing three consecutive targets
(T1,T2,T3), there was no deﬁciency in report-
ing T3 even though it appeared at the temporal
8


## Page 9


position in which blinking is typically maxi-
mal (lag 2) [43]. This phenomenon was called
“spreading of lag-1 sparing” [44] since the atten-
uation of blinking at lag-1 spreads to additional
(target) stimuli. A related ﬁnding is the atten-
uation of AB when subjects were required to
give a whole report of a six letter sequence, i.e.
when all stimuli were considered targets, com-
pared to the standard case in which only two
letters had to be reported [45]. Such ﬁndings
pose a challenge for limited-capacity accounts
of the AB and seem to indicate the workings of
a top-down attentional control mechanism [18].
However, the model presented here can pro-
vide an interesting explanation of these ﬁnd-
ings by assuming that a consecutive sequence
of targets temporarily reduces DMN ﬂuctua-
tions, perhaps by focusing the subject’s atten-
tion on the task, thus reducing blinking prob-
ability until appearance of the next distractor.
This hypothesis explains “spreading” effects in
terms of an interaction between capacity limita-
tion (the blinking threshold), and a top-down
control mechanism (temporary reducing DMN
noise). The partial occlusion of earlier by later
targets at the cognitive representation stage
may also explain the poorer identiﬁcation of
T1 typically observed when three targets are
presented sequentially [43, 46].
ii.3
No T2 evoked P3b during blinking tri-
als
In [47] it was shown that missed T2 targets
do not evoke a P3b ERP. In the model, these
trials correspond to cases in which the atten-
tional resources were depleted by the T1, or the
combined representation of T1 and T2, signal.
This results in a large P3b amplitude elicited
by the T1, or combined T1,T2, signal and no
attentional resource capture, and thus no P3b
signal, evoked in response to T2 itself.
ii.4
Distractor and target saliency
The experiments reported in [48, 49] showed
that salient distractors which match features
with the target set (having the same color),
can also trigger an AB for a subsequent target.
The model can account for these ﬁndings by
representing salient distractors as pulses with
smaller amplitudes (compared to targets) at the
sensory signal level. These distractor pulses
will also contribute towards triggering an AB
but to a lesser extent than an additional tar-
get pulse would. Using a similar amplitude
modulation mechanism, the model can explain
why targets which capture the attention more
powerfully (e.g. by switching their color com-
pared to pre-target distractors) have a higher
propensity for causing AB [50].
ii.5
Effect of inter-target blanks
There are mixed results in the AB literature
regarding the effects of inserting a blank stim-
ulus between T1 and T2. In some cases blink-
ing was reported although at attenuated lev-
els compared to the case of a (non-blank) dis-
tractor (e.g. [15, 51, 52]), while other studies
showed no blinking when inserting inter-target
blanks (e.g. [20, 53, 54]). Such blanks can be
represented in the model by small inter-target
impulses whereas (non-blank) distractors can
be represented by somewhat larger, yet still
smaller than target, pulses. While this particu-
lar analysis is beyond the scope of the current
work, we wish to point out that this and similar
questions can be addressed by the model using
slight modiﬁcations of the basic framework.
ii.6
Task-irrelevant mental activity
A somewhat counterintuitive series of ﬁndings
reported in [55, 56] suggest that certain seem-
ingly task irrelevant stimuli, or mental activi-
ties (background music or visual motion, per-
forming a concurrent memory task etc.) can
signiﬁcantly attenuate the AB. These interven-
tions presumably load the attentional channel,
and thus seem at odds with a capacity lim-
ited account of the AB. However, the model
provides an interesting explanation for these
ﬁndings by hypothesizing that such activities
may reduce DMN activity levels, and this in-
crease attentional capacity, perhaps by focusing
subjects on their immediate environment thus
reducing mind wandering.
9


## Page 10


V.
Conclusion
This paper proposed a model of attentional
blink which is simple and parsimonious while
providing explanatory and predictive power.
The model’s main features are a dynamical sys-
tem’s account of attentional capacity with a
top-down control mechanism in the form of
DMN activity, represented by stochastic noise
loading the system’s capacity. The model gen-
erates quantiﬁable predictions relating DMN
activity levels, AB task performance and the
P3b ERP, which can be tested in future experi-
ments.
VI.
Acknowledgments
The authors thank the ICRI-CI, the Israel Sci-
ence Foundation, the Gatsby Charitable Foun-
dation and the European Research Council. We
wish to thank Leon Deuoell and Tamar Regev
for helpful discussions.
References
[1] K. Shapiro and K. (Ed), The Limits of
Attention: Temporal Constraints in Human
Information Processing.
Oxford University
Press, oct 2001. [Online]. Available: http:
//www.oxfordscholarship.com/view/
10.1093/acprof:oso/9780198505150.001.
0001/acprof-9780198505150
[2] H. A. Slagter, A. Lutz, L. L. Greischar,
A. D. Francis, S. Nieuwenhuis, J. M.
Davis,
and R. J. Davidson,
“Mental
Training Affects Distribution of Limited
Brain Resources,” PLoS Biology, vol. 5,
no. 6,
p. e138,
may 2007. [Online].
Available:
http://dx.plos.org/10.1371/
journal.pbio.0050138
[3] A. Lutz, H. A. Slagter, N. B. Rawl-
ings, A. D. Francis, L. L. Greischar,
and R. J. Davidson, “Mental Training
Enhances Attentional Stability:
Neu-
ral and Behavioral Evidence,” Journal
of Neuroscience,
vol. 29,
no. 42,
pp.
13 418–13 427, oct 2009. [Online]. Avail-
able: http://www.jneurosci.org/cgi/doi/
10.1523/JNEUROSCI.1614-09.2009
[4] M. K. van Vugt and H. A. Slagter, “Con-
trol over experience? Magnitude of the
attentional blink depends on meditative
state,” Consciousness and Cognition, vol. 23,
pp. 32–39, 2014.
[5] M. E. Raichle, A. M. MacLeod, A. Z.
Snyder, W. J. Powers, D. A. Gusnard,
and G. L. Shulman, “A default mode of
brain function.” Proceedings of the National
Academy of Sciences of the United States of
America, vol. 98, no. 2, pp. 676–82, jan 2001.
[Online]. Available:
http://www.ncbi.
nlm.nih.gov/pubmed/11209064http:
//www.pubmedcentral.nih.gov/
articlerender.fcgi?artid=PMC14647
[6] M. E. Raichle,
“The Brain’s Default
Mode
Network,”
Annual
Review
of
Neuroscience,
vol.
38,
no.
1,
pp.
433–447,
2015.
[Online].
Available:
http://www.annualreviews.org/doi/10.
1146/annurev-neuro-071013-014030
[7] M. F. Mason, M. I. Norton, J. D. Van Horn,
D. M. Wegner, S. T. Grafton, and C. N.
Macrae, “Wandering minds: the default
network
and
stimulus-independent
thought.” Science (New York, N.Y.), vol.
315,
no. 5810,
pp. 393–5,
jan 2007.
[Online]. Available:
http://www.ncbi.
nlm.nih.gov/pubmed/17234951http:
//www.pubmedcentral.nih.gov/
articlerender.fcgi?artid=PMC1821121
[8] K. Christoff, A. M. Gordon, J. Smallwood,
R. Smith, and J. W. Schooler, “Experience
sampling during fMRI reveals default
network and executive system contribu-
tions to mind wandering,” Proceedings
of the National Academy of Sciences, vol.
106, no. 21, pp. 8719–8724, may 2009.
[Online]. Available:
http://www.pnas.
org/cgi/doi/10.1073/pnas.0900234106
[9] R. L. Buckner, J. R. Andrews-Hanna, and
D. L. Schachter, “The Brain’s Default
10


## Page 11


Network:
Anatomy,
Function,
and
Relevance to Disease,”
Annals of the
New York Academy of Sciences, vol. 1124,
no. 1,
pp. 1–38,
mar 2008. [Online].
Available: http://doi.wiley.com/10.1196/
annals.1440.011
[10] K. A. Garrison, T. A. Zefﬁro, D. Scheinost,
R. Todd Constable, and J. A. Brewer,
“Meditation leads to reduced default mode
network activity beyond an active task,”
2015.
[11] J. A. Brewer, P. D. Worhunsky, J. R. Gray,
Y.-Y. Tang, J. Weber, and H. Kober, “Med-
itation experience is associated with dif-
ferences in default mode network activity
and connectivity.”
[12] N. A. S. Farb, Z. V. Segal, H. Mayberg,
J. Bean, D. McKeon, Z. Fatima, and
A. K. Anderson,
“Attending to the
present: mindfulness meditation reveals
distinct neural modes of self-reference.”
Social cognitive and affective neuroscience,
vol. 2,
no. 4,
pp. 313–22,
dec 2007.
[Online]. Available:
http://www.ncbi.
nlm.nih.gov/pubmed/18985137http:
//www.pubmedcentral.nih.gov/
articlerender.fcgi?artid=PMC2566754
[13] A. Berkovich-Ohana, M. Harel, A. Ha-
hamy, A. Arieli, and R. Malach, “Alter-
ations in task-induced activity and resting-
state ﬂuctuations in visual and DMN
areas revealed in long-term meditators,”
NeuroImage, vol. 135, pp. 125–134, 2016.
[14] G.
Pagnoni,
“Dynamical
properties
of
BOLD
activity
from
the
ventral
posteromedial cortex associated with
meditation and attentional skills.” The
Journal
of
neuroscience
:
the
ofﬁcial
journal of the Society for Neuroscience,
vol. 32, no. 15, pp. 5242–9, apr 2012.
[Online]. Available:
http://www.ncbi.
nlm.nih.gov/pubmed/22496570http:
//www.pubmedcentral.nih.gov/
articlerender.fcgi?artid=PMC3362741
[15] J. Raymond, K. Shapiro, and K. Arnell,
“Temporary suppression of visual pro-
cessing in an RSVP task: An attentional
blink?”
Journal of experimental, 1992.
[Online]. Available: http://psycnet.apa.
org/journals/xhp/18/3/849/
[16] D. E. Broadbent and M. H. P. Broad-
bent,
“From
detection
to
identiﬁca-
tion:
Response
to
multiple
targets
in
rapid
serial
visual
presentation,”
Perception
&
Psychophysics,
vol.
42,
no. 2,
pp. 105–113,
mar 1987. [On-
line]. Available: http://www.springerlink.
com/index/10.3758/BF03210498
[17] P. Dux, “The attentional blink: A review
of data and theory,” vol. 71, no. 8, pp.
1683–1700, 2009.
[18] S. Martens and B. Wyble, “The attentional
blink:
past, present, and future of a
blind spot in perceptual awareness.”
Neuroscience
and
biobehavioral
reviews,
vol. 34, no. 6, pp. 947–57, may 2010.
[Online]. Available:
http://www.ncbi.
nlm.nih.gov/pubmed/20025902http:
//www.pubmedcentral.nih.gov/
articlerender.fcgi?artid=PMC2848898
[19] C.-T. Chen and C.-T. Chen, Linear system
theory and design.
Holt, Rinehart, and
Winston, 1984.
[20] M. M. Chun and M. C. Potter, “A Two-
Stage Model for Multiple Target Detection
in Rapid Serial Visual Presentation,” Jour-
nal of Experimental Psychology: Human Per-
ception and Performance, vol. 21, no. 1, pp.
109–127, 1995.
[21] M. C. Potter, M. M. Chun, B. S. Banks,
and M. Muckenhoupt, “Two Attentional
Deﬁcits in Serial Target Search: The Visual
Attentional Blink and an Amodal Task-
Switch Deﬁcit,” Journal of Experimental Psy-
chology: Learning, Memory, and Cognition,
vol. 24, no. 4, pp. 979–992, 1998.
[22] B. Hoeks and W. J. M. Levelt, “Pupillary
dilation as a measure of attention: A quan-
titative system analysis,” Behavior Research
11


## Page 12


Methods, Instruments, & Computers, vol. 25,
no. l, pp. 16–26, 1993.
[23] S.
M.
Wierda,
H.
van
Rijn,
N.
A.
Taatgen, and S. Martens, “Pupil dilation
deconvolution reveals the dynamics of
attention at high temporal resolution.”
Proceedings of the National Academy of
Sciences of the United States of America,
vol. 109, no. 22, pp. 8456–60, may 2012.
[Online]. Available:
http://www.ncbi.
nlm.nih.gov/pubmed/22586101http:
//www.pubmedcentral.nih.gov/
articlerender.fcgi?artid=PMC3365158
[24] A. Watson, “Temporal sensitivity,” in
Handbook of perception and human per-
formance. Vol 1:
Sensory processes and
perception., B. et Al., Ed.
Wiley New York,
1986, vol. 18, no. 4, p. 340. [Online]. Avail-
able:
http://www.sciencedirect.com/
science/article/pii/000368708790144X
[25] G.
M.
Boynton,
S.
A.
Engel,
and
D. J. Heeger, “Linear systems analysis
of
the
fMRI
signal.”
NeuroImage,
vol. 62, no. 2, pp. 975–84, aug 2012.
[Online]. Available:
http://www.ncbi.
nlm.nih.gov/pubmed/22289807http:
//www.pubmedcentral.nih.gov/
articlerender.fcgi?artid=PMC3359416
[26] J. Polich, “Updating P300: an integrative
theory of P3a and P3b.” Clinical neurophys-
iology : ofﬁcial journal of the International
Federation
of
Clinical
Neurophysiology,
vol. 118, no. 10, pp. 2128–48, oct 2007.
[Online]. Available:
http://www.ncbi.
nlm.nih.gov/pubmed/17573239http:
//www.pubmedcentral.nih.gov/
articlerender.fcgi?artid=PMC2715154
[27] J. Polich and J. R. Criado, “Neuropsychol-
ogy and neuropharmacology of P3a and
P3b,” International Journal of Psychophysiol-
ogy, vol. 60, no. 2, pp. 172–185, 2006.
[28] E. Donchin and M. Coles, “Is the P300
component a manifestation of context up-
dating?”
Behavioral and Brain Sciences,
1988.
[29] C. Wickens, A. Kramer, L. Vanasse, and
E. Donchin, “Performance of concurrent
tasks: a psychophysiological analysis of
the reciprocity of information-processing
resources.” Science (New York, N.Y.), vol.
221, no. 4615, pp. 1080–2, sep 1983.
[Online]. Available:
http://www.ncbi.
nlm.nih.gov/pubmed/6879207
[30] J. Johnson, R., “The amplitude of the P300
component of the event-related potential:
Review and synthesis,” in Advances in Psy-
chophysiology, 3, 1988, pp. 69–137.
[31] H. A. Slagter, A. Lutz, L. L. Greischar,
S. Nieuwenhuis, and R. J. Davidson,
“Theta phase synchrony and conscious
target perception:
impact of intensive
mental
training.”
Journal
of
cognitive
neuroscience,
vol.
21,
no.
8,
pp.
1536–49,
2009.
[Online].
Available:
http://www.ncbi.nlm.nih.gov/pubmed/
18823234$\delimiter"047A648$nhttp:
//www.pubmedcentral.nih.gov/
articlerender.fcgi?artid=PMC2698032
[32] R. Marois, D.-J. Yi, and M. M. Chun, “The
Neural Fate of Consciously Perceived and
Missed Events in the Attentional Blink,”
Neuron, vol. 41, pp. 465–472, 2004.
[33] G. L. Shulman, S. V. Astaﬁev, M. P.
McAvoy, G. D’Avossa, and M. Corbetta,
“Right TPJ deactivation during visual
search:
functional
signiﬁcance
and
support for a ﬁlter hypothesis.” Cerebral
cortex (New York, N.Y. : 1991), vol. 17,
no. 11, pp. 2625–33, nov 2007. [Online].
Available: http://www.ncbi.nlm.nih.gov/
pubmed/17264254
[34] M. L. Minsky, “Logical Versus Analogical
or Symbolic Versus Connectionist or Neat
Versus Scruffy,” AI Magazine, vol. 12, no. 2,
p. 34, 1991.
[35] B. Wyble, H. Bowman, and M. Nieuwen-
stein, “The Attentional Blink Provides
Episodic
Distinctiveness:
Sparing
at
a
Cost.”
[Online].
Available:
http:
//dx.doi.org/10.1037/a0013902.supp
12


## Page 13


[36] S. Nieuwenhuis, M. S. Gilzenrat, B. D.
Holmes, and J. D. Cohen, “The Role of
the Locus Coeruleus in Mediating the At-
tentional Blink: A Neurocomputational
Theory.”
[37] S. Chartier, D. Cousineau, and D. Char-
bonneau, “A Connectionist Model of the
Attentional Blink Effect During a Rapid
Serial Visual Presentation Task,” 2004.
[38] N. Fragopanagos, S. Kockelkoren, and J. G.
Taylor, “A neurodynamic model of the
attentional blink,” 2005.
[39] C. N. L. Olivers and M. Meeter, “A Boost
and Bounce Theory of Temporal Atten-
tion,” 2008.
[40] S.-I. Shih, “The attention cascade model
and attentional blink,” 2007.
[41] N. A. Taatgen, I. Juvina, M. Schipper, J. P.
Borst, and S. Martens, “Too much control
can hurt: A threaded cognition model of
the attentional blink,” Cognitive Psychology,
vol. 59, no. 1, pp. 1–29, 2009.
[42] B. Hommel and E. G. Akyürek, “Lag-1
sparing in the attentional blink: beneﬁts
and costs of integrating two events
into a single episode.” The Quarterly
journal
of
experimental
psychology.
A,
Human experimental psychology, vol. 58,
no. 8, pp. 1415–33, nov 2005. [Online].
Available: http://www.ncbi.nlm.nih.gov/
pubmed/16365947
[43] V. DiLollo, J.-I. Kawahara, S. M. Shahab,
G. Ae, and J. T. Enns, “The attentional
blink: Resource depletion or temporary
loss of control?”
[44] C. N. L. Olivers, S. Van Der Stigchel,
and J. Hulleman, “Spreading the sparing:
against a limited-capacity account of the
attentional blink.”
[45] M. R. Nieuwenstein and M. C. Potter,
“Temporal limits of selection and memory
encoding: A comparison of whole versus
partial
report
in
rapid
serial
visual
presentation.” Psychological science, vol. 17,
no. 6, pp. 471–5, jun 2006. [Online].
Available: http://www.ncbi.nlm.nih.gov/
pubmed/16771795
[46] J.-i. Kawahara, J. T. Enns, and V. D.
Lollo,
“The attentional blink is not
a unitary phenomenon,” Psychological
Research, vol. 70, no. 6, pp. 405–413, oct
2006. [Online]. Available:
http://link.
springer.com/10.1007/s00426-005-0007-5
[47] E. K. Vogel, S. J. Luck, K. L. Shapiro,
S. J. Luck, E. K. Vogel, K. L. Shapiro,
L. Berglan, M. Chun, V. Di Lollo, H. Egeth,
J. Hoffman, B. Maki, lane Raymond, and
E. K. Vogel or Steven J Luck, “Electrophys-
iological Evidence for a Postperceptual Lo-
cus of Suppression During the Attentional
Blink,” Journal of Experimental Psychology
Nature, vol. 24, no. 382, pp. 616–618, 1998.
[48] Folk L. Charles, Leber B. Andrew, and
Egeth E. Howard, “Made you blink! Con-
tingent attentional capture produces a
spatial blink,” Perception & Psychophysics,
2002.
[49] W. Maki and M. Mebane, “Attentional
capture triggers an attentional blink,”
Psychonomic Bulletin & Review, vol. 13,
no.
1,
pp.
125–131,
2006.
[Online].
Available:
http://dx.doi.org/10.3758/
BF03193823
[50] P.
E.
Dux,
C.
L.
Asplund,
and
R.
Marois,
“An
attentional
blink
for
sequentially
presented
targets:
evidence in favor of resource depletion
accounts.” Psychonomic bulletin & review,
vol. 15, no. 4, pp. 809–13, aug 2008.
[Online]. Available:
http://www.ncbi.
nlm.nih.gov/pubmed/18792508http:
//www.pubmedcentral.nih.gov/
articlerender.fcgi?artid=PMC3644218
[51] F.
K.
Chua,
“The
effect
of
target
contrast on the attentional blink,” Per-
ception & Psychophysics, vol. 67, no. 5,
13


## Page 14


pp. 770–788, jul 2005. [Online]. Avail-
able:
http://www.springerlink.com/
index/10.3758/BF03193532
[52] T. A. W. Visser and T. A. W., “Masking T1
difﬁculty: Processing time and the atte-
nional blink.” Journal of Experimental Psy-
chology: Human Perception and Performance,
vol. 33, no. 2, pp. 285–297, 2007. [Online].
Available: http://doi.apa.org/getdoi.cfm?
doi=10.1037/0096-1523.33.2.285
[53] T.
D.
Grandison,
T.
G.
Ghirardelli,
and H. E. Egeth, “Beyond similarity:
masking of the target is sufﬁcient to
cause the attentional blink.” Perception &
psychophysics, vol. 59, no. 2, pp. 266–74, feb
1997. [Online]. Available: http://www.
ncbi.nlm.nih.gov/pubmed/9055621
[54] B.
G.
Breitmeyer,
A.
Ehrenstein,
K. Pritchard, M. Hiscock, and J. Crisan,
“The roles of location speciﬁcity and
masking mechanisms in the attentional
blink.” Perception & psychophysics, vol. 61,
no. 5, pp. 798–809, jul 1999. [Online].
Available: http://www.ncbi.nlm.nih.gov/
pubmed/10498996
[55] C. N. L. Olivers and S. Nieuwenhuis,
“The beneﬁcial effect of concurrent task-
irrelevant mental activity on temporal
attention.” Psychological science, vol. 16,
no. 4, pp. 265–9, apr 2005. [Online].
Available: http://www.ncbi.nlm.nih.gov/
pubmed/15828972
[56] I. Arend, S. Johnston, and K. Shapiro,
“Task-irrelevant visual motion and ﬂicker
attenuate the attentional blink.” Psy-
chonomic
bulletin
&
review,
vol.
13,
no. 4, pp. 600–7, aug 2006. [Online].
Available: http://www.ncbi.nlm.nih.gov/
pubmed/17201358
14

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
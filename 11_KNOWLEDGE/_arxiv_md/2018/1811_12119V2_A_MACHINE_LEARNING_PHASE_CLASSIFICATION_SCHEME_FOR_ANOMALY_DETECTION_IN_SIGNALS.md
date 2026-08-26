---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1811.12119v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1811.12119v2_A_Machine-Learning_Phase_Classification_Scheme_for_Anomaly_Detection_in_Signals_

> Source: 1811.12119v2_A_Machine-Learning_Phase_Classification_Scheme_for_Anomaly_Detection_in_Signals_.pdf

> Pages: 25

---


## Page 1


Ahrens et al.
RESEARCH
A Machine-Learning Phase Classiﬁcation Scheme
for Anomaly Detection in Signals with Periodic
Characteristics
Lia Ahrens1*, Julian Ahrens1 and Hans D. Schotten1,2
Abstract
In this paper we propose a novel machine-learning method for anomaly detection applicable to data with
periodic characteristics where randomly varying period lengths are explicitly allowed. A multi-dimensional time
series analysis is conducted by training a data-adapted classiﬁer consisting of deep convolutional neural
networks performing phase classiﬁcation. The entire algorithm including data pre-processing, period detection,
segmentation, and even dynamic adjustment of the neural networks is implemented for fully automatic
execution. The proposed method is evaluated on three example datasets from the areas of cardiology, intrusion
detection, and signal processing, presenting reasonable performance.
Keywords:
anomaly detection; time series analysis; phase classiﬁcation; machine learning; convolutional neural networks
1 Introduction
Many real-world systems, both natural and anthro-
pogenic, exhibit periodic behaviour. Monitoring such
systems necessarily produces periodic time series. In
one particular instance of such a monitoring appli-
cation, one is interested in automatically detecting
changes in the periodically repeating pattern and thus
anomalies in the systems operation. This type of
anomaly detection occurs in a wide range of diﬀer-
ent ﬁelds and applications, be they medical, e.g. diag-
nosing diseases of the cardiovascular and respiratory
systems, in industrial contexts, e.g. monitoring the op-
eration of a transformer or rotating machinery, and in
signal processing and communications. The pursued
aims range from simple monitoring to intrusion detec-
tion and prevention.
Traditionally, anomaly detection is performed in
the form of outlier detection in mathematical statis-
tics. Numerous methods have been proposed, includ-
ing but not limited to distance- and density-based
techniques [1, 2] and subspace- or submanifold-based
techniques [3, 4, 5]. Most of these approaches make
no explicit use of the concept of time and are there-
fore usually less suited for the analysis of time series.
*Correspondence: Lia.Ahrens@dfki.de
1Deutsches Forschungszentrum f¨ur K¨unstliche Intelligenz, Trippstadter
Straße 112 67663 Kaiserslautern, Germany
Full list of author information is available at the end of the article
Methods making explicit use of the temporal struc-
ture include classical models from statistical time se-
ries analysis such as autoregressive–moving average
(ARMA) models [6], Kalman ﬁlters [7] or more gen-
eral hidden Markov models [8], and rolling-window
distance-based methods such as matrix proﬁles [9].
Distance analysing methods are eﬀective for clean data
but not robust against noise, whereas distribution-
based methods from mathematical statistics are still
powerful in the presence of noise, requiring data-
speciﬁc parametrisation. In the past few years, non-
linear methods, such as diﬀerent types of recurrent
neural networks (RNNs) and in particular long short-
term memory (LSTM) networks, have also come into
use [10, 11]. Many of these methods are diﬃcult to
train [12, 13, 14] or need large amounts of data in or-
der to achieve reasonable performance while avoiding
overﬁtting. On the other hand, in recent years, con-
volutional neural networks (CNNs) have gained pop-
ularity in image processing [15, 16] where they are
used mainly for classiﬁcation tasks. The same prin-
ciples that are responsible for the success of CNNs
in image processing carry over to other types of sig-
nal processing when the number of dimensions of the
convolutional kernels is changed accordingly. Most of
the work using recurrent or convolutional networks for
time series analysis focusses on forecasting or detect-
ing certain patterns explicitly known at training time.
arXiv:1811.12119v2  [eess.SP]  27 Mar 2019


## Page 2


Ahrens et al.
Page 2 of 25
On these tasks, convolutional networks have recently
been shown to outperform the previously state of the
art LSTMs [17].
In this paper we consider data with periodic charac-
teristics and design a machine-learning algorithm for
time series analysis, in particular anomaly detection,
applying convolutional neural nets in a manner which,
to the best of the authors knowledge, has not been pro-
posed previously. In contrast to existing methods and
inspired by machine-learning methods for image pro-
cessing, we employ a convolutional net acting not as a
predictor or estimator but as a classiﬁer whose classes
indicate phase i.e. the relative location in time. We also
integrate general procedures for data pre-processing
and automated phase reclustering so that no manual
action is required in between.
Our algorithm is tested on three datasets: a car-
diology dataset (ECG database) [18], an industrial
network dataset for cyber attack research (SCADA
dataset) [19], and a synthetic waveform dataset de-
scribed in detail in Section 4.3. It turns out that, to a
certain extent, our method is robust against unclean
data and the related neural networks do not show high
sensitivity to the hyperparameters and are relatively
easy to train.
The remainder of the paper is organised as follows.
In Section 2 we specify the types of anomaly detec-
tion considered in this paper, comment on traditional
methods, and introduce the concept of our solution.
In Section 3 our general approach to the considered
anomaly detection problems is described in detail,
including data pre-processing, mathematical basis of
convolutional neural networks, and training algorithm.
In Section 4 our method is ﬁne-tuned for the three
aforementioned example datasets and in Section 5 the
empirical results are evaluated. In Appendix A, deal-
ing with the issue of randomly varying period length
which shows up in many real world applications such
as in the ECG data (Section 4.1) and synthetic waves
(Section 4.3), an auxiliary period detection scheme is
designed based on classical principles of signal process-
ing. In Appendix B we perform some comparisons with
other methods for anomaly detection in order to fur-
ther highlight the advantage of using a convolutional
neural network in the proposed manner.
2 Preliminaries
In preparation for the detailed description of our
machine-learning phase classﬁcation scheme given in
Section 3, in this section we clarify the tasks of
anomaly detection in time series with periodic charac-
teristics, discuss some common methods, and outline
the essential ideas of our approach.
2.1 Context of this work
In general, a time series {Xt}t=0,1,2,... (i.e. a temporal
sequence of observations X0, X1, X2, . . ., also termed
signal) is said to exhibit periodic behaviour with pe-
riod length s if similarities occur after every s time
units, i.e., observations that are s time units apart,
Xt0, Xt0+s, Xt0+2s, . . . for any t0, are similar.
Periodic signals occur naturally in a wide range of
applications and in a large number of ﬁelds such as
audio processing, vibration analysis, biomedical engi-
neering, climatology, and economic time series analy-
sis. Oftentimes, one wishes to monitor the behaviour
of such a system. In particular, a common task when
observing a signal is that of anomaly detection, i.e., the
detection of deviations from a certain normal mode of
operation. This has a variety of applications such as
disease diagnosis, network security, fraud recognition
in bank transactions, etc.
The general approach to anomaly detection is to
relate a mathematical model (parametric or non-
parametric) to the normal behaviour of the underlying
system based on historic observations (training data)
and set a conﬁdence region for data of normal type;
applying the data-adapted model to the ongoing ob-
servations (test data), whether the output lies within
or outside the pre-deﬁned conﬁdence region decides
if the corresponding input observation is considered
normal or abnormal, respectively.
As with most naturally occurring siganals, many of
the aforementioned signals do not satisfy the exact
mathematical deﬁnition of periodicity. Instead, they
exhibit a property which is referred to as quasiperiod-
icity which basically means that the signal does not
exactly repeat itself, but has deviations both in its
values and in the length of the actual periods. This
behaviour is very common for instance in biological
or climatological systems. As a consequence for the
task of anomaly detection, a sophisticated mathemat-
ical model is required to capture the essence of the
diverse and noise corrupted signals.
2.2 Tasks of anomaly detection
Mathematically, the approach to anomaly detection
proposed in this paper applies to the following two
types of problems:
Type A The historic observations of normal type
(training data) are made up of various sig-
nals {{X(ι)
t }t | ι ∈I (index set)}. The signals
{X(ι)
t }, ι ∈I, share certain common normal-type-
characterising features, but diﬀer in their values
and exhibit periodic characteristics with individ-
ual period length s(ι) which may also ﬂuctuate
over time. The task of anomaly detection in such
a setting consists in rating each ongoing observa-
tion signal {Xt}t as normal or abnormal.


## Page 3


Ahrens et al.
Page 3 of 25
Type B The historic observations of normal type
(training data) are made up of consecutive single
data points X0, X1, . . . , XN−1 which jointly form
a time series {Xt}t=0,...,N−1. The occurance of the
data points X0, . . . , XN−1 follows certain normal-
type-characterising patterns, which is reﬂected
in the corresponding time series {Xt}t=0,...,N−1
as seasonal eﬀects associated with period length
s where s may randomly vary over time. The
task of anomaly detection in such a setting con-
sists in specifying segments of onging observations
{Xt}t≥N which are abnormal.
Problems of Type A arise from areas such as dis-
ease diagnosis, climatology, vibration analysis, etc.,
whereas problems of Type B are often addressed in the
security sector and building monitoring systems within
the framework of signal processing. In general, estab-
lishing an adequate mathematical model for the nor-
mal behaviour of a system requires a proper amount
of training data. In our experiments in Section 4, our
approach to the considered problems is applied to a
cardiology dataset for detecting heart disease (cf. ECG
database [18]) as an example of problems of Type A,
a relatively small industry dataset in the context of
network security (cf. SCADA dataset [19]) as an ex-
ample of problems of Type B, and a more extensive
synthetic waveform dataset injected with a variety of
noise and anomalies (cf. Section 4.3) again as an exam-
ple of problems of Type B. The experimental results
are provided in Section 5.
From
a
mathematical
perspective,
problems
of
Type A are more challenging than those of Type B. In
the setting of Type A a considerably complex math-
ematical model is needed for capturing diverse varia-
tions of the normal behaviour across a variety of train-
ing signals, whereas in the setting of Type B the re-
quired mathematical model for the normal behavior
is to be ﬁtted to a single training time series. Many
traditional methods for anomaly detection in periodic
signals may ﬁnd direct applications to problems of
Type B but fail to be applicable to problems of Type A.
This will be further discussed in the subsequent sec-
tion.
2.3 On common methods
Let us comment on the adequacy of some traditional
methods for detecting anomalies in periodic signals in
our context.
2.3.1 Distance-analysing methods
The most straightforward treatment of seasonal data
goes back to cross correlation analysis, e.g. matrix pro-
ﬁles [9]. The basic idea therein is to apply a rolling win-
dow and deﬁne a Euclidean-type metric which mea-
sures the distance of consecutive values within the
rolling window at diﬀerent locations of the underlying
time series from one another or from a ﬁxed reference
sequence (e.g. a mean window consisting of seasonal
means); data points exhibiting large distance from the
reference value are considered abnormal.
In general, distance-analysing approaches are not re-
sistant against noise and fail to capture complex struc-
tures in the data. In the appendix, we evaluate a
simple distance-based self-similarity approach in Sec-
tion B.1. We also provide a distance-based version of
our phase classiﬁcation scheme (without artiﬁcial neu-
ral networks) for comparison in Section B.2.
2.3.2 ARIMA methodology and Kalman ﬁltering
A more sophisticated class of methods arises from
mathematical statistics, e.g. autoregressive integrated
moving
average
(ARIMA)
methodology,
methods
based on structural component time series models or
more general Kalman ﬁltering (based on the linear
case of the general state-space model or hidden Markov
model), cf. [20, 21] for detailed description of the corre-
sponding mathematical models. These approaches can
be directly applied to problems of Type B described
in Section 2.2 and are based on relating a stochas-
tic model with parameters Θ = {θ1, . . . , θr} to the
training part {Xt}t=0,1,...,N−1 of the observed time se-
ries {Xt}t so as to make short-term (usually one-step
ahead) forecasts, i.e., to estimate the conditional ex-
pectation E[Xt+∆t | Xt, Xt−1, . . . ; Θ] by ˆXt+∆t for all
t (in particular for t + ∆t ≥N), which basically re-
lies on calculating the maximum likelihood estimate
ˆΘ of the parameters Θ, making use of available ob-
servations. Setting a threshold value δ, if the actual
observation Xt0 varies enough from the forecast value
ˆXt0 in the sense that |Xt0 −ˆXt0| > δ, then the data
point Xt0 observed at time t0 is considered abnormal.
Among the aforementioned stochastic models, the
most demonstrative one is to decompose the under-
lying time series into trend, seasonal, and independent
noise components, where the trend and seasonal com-
ponents are assumed to be deterministic functions of
time which can be ﬁtted by a polynomial and con-
ducting Fourier analysis, respectively. In fact, this is a
special case of the general structural component time
series model with trend and seasonal conmponents be-
ing stochastic processes. Each structural component
model can be straightforwardly represented as a linear
state-space model for which Kalman ﬁltering comes
into use to generate forecasts; it also has an equivalent
ARIMA model representation for which forecasting
can be conducted by following the ARIMA methodol-
ogy. The ARIMA approach is based on spectral theory.
For seasonal time series, a parsimonious form termed
(multiplicative) seasonal ARIMA (SARIMA) model


## Page 4


Ahrens et al.
Page 4 of 25
may be considered. In general, modelling a time series
with an ARIMA representation requires data-speciﬁc
transformation (i.e. data pre-processing e.g. logarith-
mising, power transformation, and diﬀerencing) and a
data-adaptive hyperparameter choice (i.e. the design of
the parameter set Θ = {θ1, . . . , θr}, in particular the
number of parameters r) which relies on inspection
of the autocorrelogram and partial autocorrelogram.
Each ARIMA model has an equivalent linear state-
space model representation allowing Kalman ﬁltering
to be employed for forecasting.
The ARIMA approach and Kalman ﬁltering are pow-
erful tools in many applications and in particular in
the presence of noise, provided that the hyperparame-
ter choice is reasonable. However, being the most tech-
nically manageble segment of the general state-space
models, linear models lack complexity and therefore
do not always deliver a feasible approximation for real
world applications. In addition, the associated data-
adapted model selection including data pre-processing
requires speciﬁc expert knowledge and is therefore dif-
ﬁcult to implement for fully automatic execution as in
our machine-learning framework. Furthermore, consid-
ering problems of Type A described in Section 2.2, it is
unclear how to choose a general representative time se-
ries {X∗
t }t in which the diverse variations arising from
the individual training signals {{X(ι)
t }t | ι ∈I} are
incorporated so that the model ﬁtted to {X∗
t }t applies
to all normal signals.
2.3.3 Long Short-Term Memory Units
Long short-term memory units (LSTM) are a special
type of recurrent neural network (RNN). As such, the
LSTM reads the input time series sequentially, trans-
forming at each point in time the input data into a hid-
den state which is a nonlinear function of the current
input and the hidden state one time step earlier. The
advantage of LSTMs over most other types of RNN
is that the dependency of the current on the previous
hidden state is designed in such a way that the LSTM
obtains the ability to keep (parts of) its hidden state
over a larger number of time steps than is possible
with other RNN architectures, i.e., LSTMs are able to
“memorise” values from the past.
Applying LSTMs to prediction tasks for the purpose
of anomaly detection works in a similar manner to the
application of statistical methods described in the be-
ginning of Section 2.3.2. The main diﬀerences are that
LSTMs allow for nonlinear parametrisation and have
the potential to support a much larger number of pa-
rameters which are not estimated directly but instead
are randomly initialised at ﬁrst and then optimised
during training (learnt) to obtain the desired predictor.
The complexity of the LSTMs allows them to ingest
characteristics of rich and varied training data such as
those from large training data sets of Type A as de-
scribed in Section 2.2 through the process of training
with a stochastic gradient descent (SGD) type algo-
rithm. The training set is processed repeatedly and
the parameters of the LSTM are adjusted to optimise
the quality of the forecast across the entire training
dataset.
Technically, the main drawback of LSTMs is the fact
that they are fundamentally still RNNs and hence also
suﬀer from some of the diﬃculties typical for training
this class of artiﬁcial neural network such as exploding
gradients and a high potential for overﬁtting.
As a general drawback of using one-step ahead pre-
diction for anomaly detection in time series, if the time
series is very complex and exhibits regions in which
it is diﬃcult to make precise forecasts, such as when
analysing periodic signals containing steep edges or
spikes whose positions or values vary randomly over
time, reliably estimating the values in these regions can
actually be impossible for any type of one-step ahead
prediction. It is thus diﬃcult to derive an anomaly de-
tector from such a predictor as the estimated values
can have a large distance to the actual ones and thus
show up as false positives. In Appendix B.3 this is il-
lustrated in more detail by training and evaluating an
LSTM on the ECG database.
2.4 Concept of this paper
Let us now introduce the concept of our machine-
learning phase classiﬁcation approach to the problems
speciﬁed in Section 2.2.
2.4.1 Motivation of using convolutional neural
networks for phase classiﬁcation
Convolutional neural networks (CNNs) are a speciﬁc
architecture of feed-forward neural networks. When
compared to a fully connected neural network, convo-
lutional neural networks need fewer parameters. Hence
they do not require as large a training dataset and are
less prone to overﬁtting. CNNs make explicit use of the
temporal or spatial structure of the input signal; the
signal is analysed locally (local receptive ﬁelds) and
in a shift invariant manner (translation invariance).
Investiagtions on the internal representations present
throughout the layers of CNNs show a high tolerance
to noise of various kinds.
Like LSTMs, compared to statistical methods, CNNs
have the advantage that, through the use of multiple
channels and non-linearities, they provide enough ﬂex-
ibility to capture intricate structures of analysed sig-
nals and are able to ﬁnd representations for large and
varied data sets. They are however easier to train than
RNNs, as they suﬀer less from the vanishing and ex-
ploding gradient problems. The capability of a CNN of


## Page 5


Ahrens et al.
Page 5 of 25
being able to process high amounts of complexity has
been analysed in the ﬁeld of image processing, where it
was shown [22] that the neurons inside a convolutional
neural network can activate on patterns ranging from
simple edges to things as complex as faces.
While CNNs can be used to make forecasts in time
series, they particularly excel at classiﬁcation of spa-
tial or temporal data. Since the main problem of the
LSTM-based approach to anomaly detection in time
series outlined above is the general unfeasability of
using one-step ahead forecasts, we capitalise on the
strength of CNNs in classiﬁcation tasks and devise
a new type of anomaly detection scheme relying on
phase classiﬁcation instead of one-step ahead forecast-
ing. More details on the properties and operation of
CNNs are given in Section 3.2.
2.4.2 Phase classiﬁcation and anomaly detection
Motivated by the advantages of convolutional neural
networks in classiﬁcation tasks when dealing with spa-
tial or temporal data, the maching-learning approach
proposed in this paper is based on the following key
ideas:
1
Conducting multi-dimensional time series analy-
sis by means of multi-channel deep convolutional
neural networks, where each channel in the input
layer corresponds to a single feature (dimension)
of the considered time series
2
Identifying phases or, equivalently, relative loca-
tions (order of occurrence) of subpatterns from
time series with periodic characteristics by means
of training data-adapted classiﬁers so that sub-
patterns over diﬀerent periods of the underlying
time series are properly separated into a certain
amount of classes
To be more speciﬁc, considering a seasonal time se-
ries {Xt}t with period begins (e.g. time of local peak
values) {τk}k, for a pre-determined initial number of
classes n0, sampling from the original signal n0 over-
lapping segments per period with a sliding window of
length T, each subpattern {X(m)
t
}t=0,...,T −1 with
X(m)
t
:= Xτk+(τk+1−τk)(m mod n0)/n0+t,
k = ⌊m/n0⌋,
m ∈N, is assigned to the class labelled m mod n0.
For seasonal data, subpatterns sampled from the
time series occur repeatedly and in ﬁxed order within
each single period. A successfully trained classiﬁer out-
puts the correct class indicating the phase or, equiva-
lently, the relative location in time (i.e. time distance
between subpattern and period begin) of the input
subpattern. Abnormal datapoints in an input pattern
are expected to cause false classiﬁcation results and
therefore to be identiﬁed as anomalies, which yields
a direct solution to problems of Type B described in
Section 2.2. For problems of Type A described in Sec-
tion 2.2, setting a minimum expected classiﬁcation ac-
curacy (threshold value) and evaluating the classiﬁca-
tion accuracy of each test signal over a certain number
of periods (which is denoted by K in the sequel), those
signals that fail to achieve this minimum are consid-
ered abnormal.
In order to optimise the classiﬁcation accuracy of
normal data and hence prevent false positive anomaly
detection results, we carry out a dynamic recluster-
ing which cancels confusing classes, i.e., subpatterns
within a period of the signal that are similar enough
to one another are merged into one class. This reclus-
tering procedure along with the optimisation of the
stride length ∆t := s/n0 (i.e. time distance between
the segments to be classiﬁed) is implemented as a dy-
namic model selection scheme integrated in our train-
ing algorithm. In addition, we design an auxiliary pe-
riod detection scheme which is employed in case of a
randomly varying period length s.
The block diagram in Figure 1 outlines the major
steps of our training algorithm and anomaly detection
scheme where the steps marked by dashed lines are
conditioned by some model-adequacy monitoring cri-
teria which are described in the subsequent section.
3 Method
In this section we present the general procedure of our
phase classiﬁcation scheme in detail and provide some
guidelines for the hyperparameter choice.
3.1 Data pre-processing
Prior to being fed into the classiﬁer neural nets, all
input signals (including training, validation, and test
data) are processed by a period detector, cut into
overlapping segments by a sliding window, and subse-
quently normalised, where the segmentation and nor-
malisation depend on the initial number of classes n0.
3.1.1 Period detection
In general, the seasonal eﬀects of a time series can be
recognised by examining the autocorrelogram (cf. [20,
2.1.4]) or periodogram (cf. [20, 2.2.1]). In many cases
the period length s is ﬁxed and known. In case of a
ﬂuctuating s (cf. e.g. data from cardiology), an auxil-
iary period detector is designed in Appendix A, cap-
turing the time of local extremum values (considered
as period begins in our setting) {τk}k within individual
periods and using cross-correlations in order to achieve
robust period detection. Note that in our setting for
randomly varying period length s, the stride length
∆t = s/n0 while segmenting the signal varies propor-
tionally to s so that the number of overlapping seg-
ments from each period is ﬁxed and equal to n0.


## Page 6


Ahrens et al.
Page 6 of 25
training signals

Type A: {{X(ι)
t }t | ι ∈I}
Type B: {Xt}t=0,...,N−1
period detector
segmentation
with n0 segments per period
normalisation
initial labelling
initialse CNN w.r.t. n0
train CNN with SGD,
repeatedly using input from X
trained classiﬁer neural network
w.r.t. n0
relabel input from X
re-initialse CNN w.r.t. n < n0
train new CNN
trained classiﬁer neural network
w.r.t. nn0 (optimal n for n0)
update n
reclustering
update n0
dynamic model selection
optimal classiﬁer neural network
w.r.t. optimal n0 and nn0
training signals
period begins

Type A: {{τ (ι)
k }k=0,...,K−1 | ι ∈I}
Type B: {τk}k=0,...,K−1
overlapping subpatterns
Type A: {{
:=X(ι)
τk+(τk+1−τk)(m mod n0)/n0+t where k=⌊m/n0⌋
z }| {
X(ι,m)
t
}t=0,...,T −1 | ι ∈I, m = 0, . . . , Kn0 −1}
Type B: {{X(m)
t
| {z }
:=Xτk+(τk+1−τk)(m mod n0)/n0+t where k=⌊m/n0⌋
}t=0,...,T −1 | m = 0, . . . , Kn0 −1}
normalised subpatterns
Type A: {
=: ˜
X(ι,m)
z
}|
{
{ ˜X(ι,m)
t
}t=0,...,T −1 | ι ∈I, m = 0, . . . , Kn0 −1}
Type B: {{ ˜X(m)
t
}t=0,...,T −1
|
{z
}
=: ˜
X(m)
| m = 0, . . . , Kn0 −1}
training dataset: X :=
Type A: { ˜X(ι,m), labelled m mod n0 | ι ∈I, m = 0, . . . , Kn0 −1}
Type B: { ˜X(m), labelled m mod n0 | m = 0, . . . , Kn0 −1}
test signal
Type A: {Xt}t
Type B: {Xt}t≥N
period detector
segmentation
w.r.t. optimal n0
normalisation
labelling in accordance with
ﬁnal labelling of training input
phase classiﬁcation
process segments from Y
with optimal classiﬁer neural network
w.r.t. optimal n0 and nn0
compare output with labels
anomaly detection result
Type A: if #{m | ˜X(m) correctly classiﬁed} / Kn0 < δ (threshold) then {Xt}t abnormal
Type B: if ˜X(m) is misclassiﬁed then segment {X(m)
t
}t=0,...,T −1 abnormal
test signal
period begins
Type A: {τk}k=0,...,K−1
Type B: {τk}k≥K
overlapping subpatterns
(
Type A: {{X(m)
t
}t=0,...,T −1 | m = 0, . . . , Kn0 −1}
Type B: {{X(m)
t
}t=0,...,T −1 | m ≥Kn0}
where X(m)
t
:= Xτk+(τk+1−τk)(m mod n0)/n0+t
k = ⌊m/n0⌋
normalised subpattern
Type A: {
=: ˜
X(m)
z
}|
{
{ ˜X(m)
t
}t=0,...,T −1 | m = 0, . . . , Kn0 −1}
Type B: {{ ˜X(m)
t
}t=0,...,T −1
|
{z
}
=: ˜
X(m)
| m ≥Kn0}
test input: Y :=
Type A: { ˜X(m) with ﬁnal label | m = 0, . . . , Kn0 −1}
Type B: { ˜X(m) with ﬁnal label | m ≥Kn0}
Figure 1: Block diagram of training algorithm and anomaly detection


## Page 7


Ahrens et al.
Page 7 of 25
3.1.2 Sliding window
The classiﬁcation accuracy of our approach turns out
not to be highly sensitive to the length of the sliding
window T. In the context of anomaly detection, the
value of T should be kept relatively small (e.g. less
than or equal to three times the average duration of
a single abnormal data sequence) in order to highlight
the local eﬀect of the abnormal data points on the
time series. We use a window size of T = ⌊3s/n0⌋
(approximately three times the stride length) where s
refers to the average value of s (recall that in general s
may vary over time). Empirically, this has proven to be
adequate for our purpose. Note that the length of the
sliding window remains constant even in the case of
randomly varying period length s, the varying stride
length merely aﬀects the amount of overlap between
adjacent sliding windows.
3.1.3 Normalisation
In order to remove trend components and avoid skewed
results due to dominating extreme values, the sam-
ples within the sliding window are normalised by ad-
justing the local mean and variance, that is, each
time considering a d-dimensional time series {Xt}t =
{Xi
t}i=0,...d−1
t
with period begins {τk}k to be pro-
cessed by a classiﬁer neural network corresponding to
initial number of classes n0, for i = 0, . . . , d −1 and
m ∈N, the vector ( ˜Xi,(m)
t
)t=0,...,T −1 is fed into chan-
nel i of the convolutional neural net, where
˜Xi,(m)
t
:= Xi,(m)
t
−µi,(m)
σi,(m)
for
t = 0, . . . , T −1
with
Xi,(m)
t
:= Xi
τk+(τk+1−τk)(m mod n0)/n0+t, k = ⌊m/n0⌋,
µi,(m) := 1
T
T −1
X
t=0
Xi,(m)
t
,
σi,(m) :=
v
u
u
t 1
T
T −1
X
t=0
(Xi,(m)
t
−µi,(m))2.
For the training and validation data, each subpat-
tern
˜X(m) := { ˜X(m)
t
}t=0,...,T −1 is initially labelled
m mod n0. If reclustering occurs during the training so
that the training and validation inputs are relabelled
(cf. Section 3.3.3 for more details), then the test data
are labelled in accordance with the ﬁnal labelling of
the training and validation data.
3.2 Convolutional neural networks
The core of our phase classiﬁer is a convolutional neu-
ral network (CNN). CNNs are a special type of feedfor-
ward neural network, which exploit structures of space
or time by sharing many of the weights among diﬀerent
neurons. We provide a short description of the math-
ematical basis of a convolutional neural network. For
more detail on the subject, we refer the reader to the
literature, e.g. [23, Ch. 9].
Basically, a feedforward neural network is a function
f : RN(0) × RP −→Rn, mapping an input vector x ∈
RN(0) to an output vector y = f(x, p) ∈Rn, using a
vector of parameters p ∈RP to adapt the mapping.
When acting as a classiﬁer, n is the number of classes
and the predicted class of a given input x is taken to be
arg maxj<n yj. The network can be decomposed into
layers, each of which represents a diﬀerent function
mapping vectors to vectors, i.e.,
f(x, p) = f (L−1)(· · · f (0)(x, p(0)) · · · , p(L−1))
where L is the number of layers and for l = 0, . . . , L−1
the functions f (l) : RN (l) × RP (l) −→RN(l+1) are the
transformations performed by each of the single layers
and the vectors p(l) ∈RP (l) are again parameter vec-
tors used to adapt the mapping and given as subvec-
tors of p. For ease of notation, let us denote the input
to the function f (l) by x(l), starting with x(0) = x and
the output of the function f (l) by x(l+1), ending with
x(L) = y.
In the most simple feedforward neural networks, each
of the transformations f (l) is given by a multiplication
with a matrix a(l) ∈RN(l)×N(l+1) called the weight ma-
trix followed by an addition of a vector b(l) ∈RN (l+1)
called the bias vector followed by the application of
some non-linear function g: R −→R called the activa-
tion function to each of the components of the result-
ing vector, i.e.,
x(l+1) = f (l)(x(l), p(l))
= g(x(l) · a(l) + b(l))
=

g
N(l)−1
X
i=0
x(l)
i
· a(l)
i,j + b(l)
j

j<N(l+1).
The entries of the matrix a(l) and the vector b(l) are
exactly the components of the parameter vector p(l).
This is called a fully connected layer.
In the case of a one-dimensional convolutional layer,
the aﬃne transformation x(l) 7−→x(l) · a(l) + b(l) is re-
placed with a more restrictive kind of aﬃne transfor-
mation, the so-called batched convolution. For this, the


## Page 8


Ahrens et al.
Page 8 of 25
vector x(l) = (x(l)
i )i<N(l) is reindexed to form a two-
dimensional array (x(l)
i,t)i<M (l),t<T (l) with M (l) · T (l) =
N (l) and we say that the sequence (x(l)
i,t)t<T (l) is fed
into the i-th channel of the convolutional layer l.[1]
Similarly, the parameter vector p(l) is distributed not
into a matrix a(l) and a vector b(l), but into a matrix of
vectors (k(l)
i,j,s)i<M (l),j<M (l+1),s<S(l) called the convolu-
tion kernels and a vector b(l) ∈RM (l+1). The operation
performed by the function f (l) is now given by
x(l+1)
= f (l)(x(l), p(l))
= g(x(l) ˙∗k(l) + b(l))
=

g
 X
i<M (l)
s<S(l)
x(l)
i,t+S(l)−1−s · k(l)
i,j,s + b(l)
j

j<M(l+1)
t<T (l+1)
and we have the constraint that T (l+1) = T (l)−S(l)+1.
In many convolutional networks, the input vectors
(x(l)
i,t)t<T (l) are extended (padded) by additional zero
entries prior to being convolved. When padding with
exactly S(l) −1 zeros, the output vectors are of the
same size as the input vectors. If furthermore the
padding is performed symmetrically, i.e., if (S(l)−1)/2
zeros are added to both ends of the signal, this is re-
ferred to as ‘SAME’-padding.
We also use a type of layer called a max pooling layer
between two convolutional layers. The transfer func-
tion f (l) : RM (l)×T (l) −→RM (l+1)×T (l+1) of this layer is
given by
f (l)(x(l)) =

max
r<R(l)
t·R(l)+r<T (l)
x(l)
j,t·R(l)+r

j<M(l+1)
t<T (l+1)
where R(l) is a positive integer called the pool size and
we have the constraints M (l+1) = M (l) and T (l+1) =
⌈T (l)/R(l)⌉. Note that max pooling layers have no ad-
justable parameters p(l).
In our networks, we employ both convolutional and
regular fully connected layers. We apply ‘SAME’-
padding in all convolutional layers and use the hyper-
bolic tangent (tanh) as activation function g through-
out the entire network, which is a common choice in
feedforward neural networks.
[1]Vice versa, when placing a fully connected layer af-
ter a convolutional layer, the inverse reindexing is per-
formed. When using a convolutional layer as the ﬁrst
layer of an artiﬁcial neural network and the input is in
fact a segment of a multivariate time series {Xi,t}i<M,t
with M = M (0) features, no reindexing is required. This
is the case in all of our set-ups.
The exact layout of the convolutional network used
for our task is displayed in Table 1. Here d, T, and n
Table 1: Layers of classiﬁer neural network
Layer Type
Sizes
0
convolutional
M(0) = d, T (0) = T,
S(0) = (⌊T/6⌋+ 1) · 2 + 1
1
max pooling
M(1) = M(0) · 6, T (1) = T (0),
R(1) = 3 if applicable, else R(1) = 1
2
convolutional
M(2) = M(1), T (2) = ⌈T (1)/R(1)⌉,
S(2) = (⌊T/12⌋+ 1) · 2 + 1
M(3) = M(2) · 3, T (3) = T (2)
3
fully connected
N(3) = M(3) · T (3)
4
fully connected
N(4) = ⌊
√
N(3) · N(5)⌋
5
output
N(5) = n
denote the dimension of the input time series, the slid-
ing window size, and the current number of classes, re-
spectively. The layer and kernel sizes are chosen to best
adapt to varying input time series dimensions, sliding
window sizes, and numbers of classes. In the convolu-
tional layers, the number of channels is increased ﬁrst
by a factor of 6, then by a factor of 3. Such increases are
common in convolutional neural networks and allow
the layers to capture diﬀerent aspects of the incoming
signal such as edges and more complex patterns.
The method, by which the parameter vector p is ad-
justed and the network adapts, is the minimisation
of a function h: Rn −→R applied to the output of
the neural network, called the loss function. Since we
are classifying phases, to each training input x (and
hence to each output y), there corresponds a label
z ∈{0, . . . , n−1}. In our case, we use the cross entropy
loss function, which is given by
h(y, z) = −wz log

exp yz
PM−1
j=0 exp yj

where wz denotes a weight by which the losses of each
class are scaled. The weights are statically determined
and are in our case chosen to be proportional to the
inverse of the number of training examples for each
class in order to counteract bias caused by unbalanced
classes.
3.3 Training algorithm
The neural networks in our algorithm are trained by
the ADAM training algorithm which is a reﬁned ver-
sion of stochastic gradient descent (SGD). In SGD, the
average loss for a set Xbatch containing pairs of train-
ing inputs x and corresponding labels z is minimised
by changing the randomly initialised parameters p of
the neural network according to the update rule
p ←p −
γ
#Xbatch
X
(x,z)∈Xbatch
∇ph(f(x, p), z)


## Page 9


Ahrens et al.
Page 9 of 25
where γ is a tuning hyperparameter called the learn-
ing rate and ∇p is the gradient operator with respect
to the vector of parameters p. This minimises the
average of the loss values h(f(x, p), z). The gradient
∇ph(f(x, p), z) is computed in an eﬃcient manner via
reverse-mode auto diﬀerentiation which is basically an
application of the chain rule. This is also known as the
backpropagation algorithm and more details on the
process can be found in the literature, e.g. [23, Ch. 4].
The set Xbatch is called a mini-batch and is taken to
be a subset of the set of all available training inputs
X. The update steps are performed with changing dis-
joint mini-batches until the entire training dataset X
is exhausted. Each pass through the entire set of avail-
able training data is referred to as an epoch. To en-
hance the training process (cf. [24]), for rich datasets
we change the size of the mini-batches during train-
ing, later epochs use larger mini-batch sizes. The adap-
tive adjustments performed by the ADAM algorithm
detailed in [25] provide further enhancements to this
process.
In contrast to usual classiﬁers, our algorithm encap-
sulates the gradient descent algorithm in a decision
process monitoring the necessity of dynamic reclus-
tering which aims to optimise the classiﬁcation accu-
racy. The complete algorithm is given in Algorithm 1
(cf. also Figure 1), the single steps are described in
more detail in the remainder of this section.
Each time having initialised the neural network for
separating the currently considered classes, the gradi-
ent descent optimiser is run until a training-progress-
monitoring stop criterion is fulﬁlled (cf. training stop
criterion in Section 3.3.2 for more details). The classiﬁ-
cation ability of the underlying neural net is evaluated
by means of the so-called confusion matrices (cf. Sec-
tion 3.3.1) throughout the entire training. If at the end
of training all classes are evaluated with suﬃcient ac-
curacy (cf. reclustering stop criterion in Section 3.3.2),
the trained neural net is stored; otherwise a relabelling
procedure according to the overall confusion matrix is
conducted where the class with least average evalua-
tion accuracy is merged into the class to which the
corresponding inputs are most commonly misclassi-
ﬁed during training and the neural net is re-initialised
with respect to the updated classes (cf. Section 3.3.3).
Among all stored neural nets, the ultimate classiﬁer
is chosen as the one having the maximum number of
output classes (cf. Section 3.3.4).
In the subsequent subsections, the aforementioned
reclustering process and stop criteria are described in
detail.
3.3.1 Confusion matrix
In order to track the progression of classiﬁcation accu-
racy during training, we record the confusion matrix
Algorithm 1 Training algorithm
nbest ←0
for n0 ∈{n∗
0, n∗
0 −2, . . . , 4} do
if n0 ≤nbest then
return stored net
end if
n ←n0
while true do
initialise net and labels
repeat
perform training iteration
until no improvement in validation loss
within 4 consecutive epochs
▷training stop crit.
if minimum class accuracy ≥1 −α then
▷reclustering stop crit.
store net
nbest ←n
break
end if
if n −1 < 3 or n −1 ≤nbest then
break
end if
n ←n −1
recluster according to overall confusion matrix
update weights of loss function
end while
end for
if nbest ̸= 0 then
return stored net
else
change α and rerun
end if
evaluated on the training data after each epoch. For
a current number of classes n and existing classes la-
belled as 0, . . . , n −1, the confusion matrix evaluated
after the k-th epoch is an (n × n)-dimensional matrix
denoted by V (n)
k
:= (V ij,(n)
k
)i,j=0,1,...,n−1, where the
entry V ij,(n)
k
refers to the number of training inputs
labelled as i and predicted by the neural net during
the k-th training epoch as class j, k ≥0.
During the experimentation, we observe that classes
which are easily distinguishable can already be sepa-
rated after very few training iterations, whereas classes
sharing more similarity perform signiﬁcantly worse in
the beginning and also show a slower increase of eval-
uation accuracy during training. Taking into account
that the evaluated value of the loss function commonly
follows a convex decreasing trend throughout the en-
tire training, the above observation motivates us to
assess the separation ability of the underlying neural
net during training by weighting the confusion ma-
trix with the respective contribution to the training
progress and to introduce the overall confusion matrix
denoted by V
(n) := (V
ij,(n))i,j=0,...,n−1 and deﬁned as
V
ij,(n) :=
E(n)−1
X
k=1
V ij,(n)
k
(H(n)
k−1 −H(n)
k
),
(3.1)


## Page 10


Ahrens et al.
Page 10 of 25
where n, E(n), and H(n)
k
refer to the current num-
ber of classes, the number of training epochs that are
performed until the training stop criterion (cf. Sec-
tion 3.3.2) is satisﬁed, and the average training loss
during the k-th epoch, respectively.
In our setting, the confusion matrices serve as the key
objects of the decision criteria for our dynamic reclus-
tering (cf. Sections 3.3.2 and 3.3.3). The deﬁnition of
the overall confusion matrix in terms of (3.1) by taking
the weighted average throughout the entire training
and dropping the values from the initial epoch (k = 0)
aims to mitigate the random eﬀect of the initialisation
of the neural network. Empirically, this yields robust
reclustering results during diﬀerent test runs for ﬁxed
n0.
3.3.2 Stop criteria
The criteria for stopping the loops are related to
parametrised eﬀectiveness and accuracy reqirements in
the following manner:
Training stop criterion We monitor the training
progress by evaluating the average loss of vali-
dation data over each training epoch. For each
(re-)initialised neural network, training is stopped
if no improvement in the average validation loss
during the latest 4 epochs can be observed.
Reclustering stop criterion Allowing a maximum
per-class margin of error α ∈[0, 1), the recluster-
ing procedure is stopped if
min
i=0,...,n−1
V ii,(n)
E(n)−1
Pn−1
j=0 V ij,(n)
E(n)−1
≥1 −α,
where n, E(n), and V (n)
E(n)−1 refer to the current
number of classes, number of epochs for training
the related network (i.e. until the training stop
criterion is fulﬁlled), and the respective confusion
matrix evaluated at the end of training (recall the
deﬁnition in Section 3.3.1), respectively.
By deﬁnition of the confusion matrix in Section 3.3.1,
for k = E(n) −1 and each i = 0, . . . , n −1, the di-
agonal element V ii,(n)
k
divided by the respective row
sum Pn−1
j=0 V ij,(n)
k
of the confusion matrix is the share
of correctly classiﬁed training inputs in all training in-
puts labelled as i evaluated during the last epoch while
training the classiﬁer neural network with n existing
classes. Therefore, for a pre-deﬁned margin of error
α ∈[0, 1), the above reclustering stop criterion re-
quires that at the end of training the corresponding
classiﬁer neural network should correctly classify the
training inputs of each existing class at least at the
rate of 1 −α.
3.3.3 Reclustering
As long as the recustering stop criterion is not ful-
ﬁlled, the subsequent reclustering procedure is consid-
ered necessary.
For a current number of classes n and existing classes
labelled as 0, . . . , n −1, let i◦and j◦denote the worst
evaluated class and the correponding most misassigned
class during the entire training of the respective neural
net (i.e. until the training stop criterion is fulﬁlled)
which are deﬁned as
i◦:= arg min
i=0,...,n−1
V
ii,(n)
Pn−1
j=0 V
ij,(n)
and
j◦:= arg max
j=0,...,n−1
j̸=i◦
V
i◦j,(n)
respectively (recall the deﬁnition of V
(n) in (3.1)). The
class labelled as i◦is merged into class j◦. Further-
more, since we always assume the labels to be con-
secutive, the training and validation inputs with the
largest label n−1 are assigned the label of the dropped
class i◦.
Each time after relabelling, the weights correspond-
ing to the remaining classes in the cost function are ad-
justed to be again inversely proportional to the current
shares of the classes in order to warrant a well-balanced
training of the updated classiﬁer and the neural net is
re-initialised.
3.3.4 Final number of classes
In the context of anomaly detection, we are dealing
with the trade-oﬀbetween optimising the classiﬁca-
tion accuracy of normal data preventing false positives
(i.e. to cancel confusing classes) and maintaining the
ability of misclassifying abnormal data for the sake of
anomaly detection (i.e. to still retain suﬃciently many
classes characterising diﬀerent phases within a period).
Keeping this in mind, the ﬁnal number of classes de-
termining the ultimate classiﬁer neural network is se-
lected in the following manner:
Given a maximum allowed number of classes n∗
0 with
n∗
0 an even number n∗
0 > 3, the starting initial number
of classes is set to n0 := n∗
0. Each time for an updated
initial number of classes n0, the relabelling procedure
described in Section 3.3.3 is run at most (n0 −3)-times
(i.e. with at least 3 remaining classes). If the reclus-
tering stop criterion is fulﬁlled after relabelling ∆nn0-
times, the candidate ﬁnal number of classes related to
n0 is set to nn0 := n0 −∆nn0 and the corresponding
neural net is stored. If maxn′
0=n∗
0,...,n0 nn′
0 ≥n0−2, the


## Page 11


Ahrens et al.
Page 11 of 25
updating processes of n0 is ﬁnished; otherwise n0 is re-
duced by 2. The overall ﬁnal number of classes refers
to the maximum of nn0 taken along the entire path of
n0, i.e. maxn′
0=n∗
0,...,4 nn′
0 and the ﬁnal classiﬁer neural
network is the one stored when this overall maximum
was achieved. If this maximum was achieved more than
once, we choose the neural network corresponding to
the highest n0 such that nn0 achieved this maximum.
This is because a high value of n0 corresponds to a
narrow sliding window (cf. Section 3.1.2) and hence
maximises the sensitivity of the anomaly detector.
If in the end no suitable network has been stored,
we increase α and rerun the algorithm.
Finally, it is worth mentioning that once all the
hyperparameters are determined, the whole train-
ing algorithm introduced above, including data pre-
processing and dynamic reclustering, is implemented
in a machine-learning manner so that the classiﬁcation
and anomaly detection process can be accomplished
fully automatically.
3.4 Anomaly detection
Once training is ﬁnished and in particular when the
ultimate classiﬁer neural network determined by the
model selection process turns out to use initial num-
ber of classes n0 and ﬁnal number of classes nn0, each
test signal is pre-processed following the procedure de-
scribed in Section 3.1 with respect to n0, labelled with
respect to nn0 in accordance with the training and val-
idation data (recall the relabelling step along with the
dynamic reclustering described in Section 3.3.3), and
then processed by the trained ultimate classiﬁer neural
network.
For problems of Type A described in Section 2.2,
a minimum expected per-signal average classiﬁcation
accuracy δ (threshold value) should be set depending
on individual needs. For instance, δ could be deter-
mined on the basis of classiﬁcation accuracy on vali-
dation data. For each test signal {Xt}t recorded over
K periods of time with period begins {τk}k=0,...,K−1,
if the normalised segments ˜X(m), m = 0, . . . , Kn0 −1
(recall Section 3.1.3), processed by the ultimate clas-
siﬁer neural net are evaluated with an average clas-
siﬁcation accuracy rate less than δ, i.e., if #{m |
˜X(m) correctly classiﬁed}/Kn0 < δ, then the signal
{Xt}t is considered abnormal.
Considering problems of Type B described in Sec-
tion 2.2, if a normalised segment { ˜X(m)
t
}t=0,...,T −1 (re-
call Section 3.1.3) of the test signal {Xt}t≥N is mis-
classiﬁed by the ultimate classiﬁer neural net, then the
original segment {X(m)
t
}t=0,...,T −1 with
X(m)
t
= Xτk+(τk+1−τk)(m mod n0)/n0+t,
k = ⌊m/n0⌋
is considered abnormal.
4 Experiments
In this section we apply our machine-learning algo-
rithm proposed in Section 3 to three example datasets
choosing from the domains of cardiology, industry, and
signal processing, aiming to show the feasibility of
the method in a range of applications. The cardiology
dataset is the most complex and challenging dataset
representing problems of Type A described in Sec-
tion 2.2, as the recordings taken from healthy control
patients exhibit a high level of diversity which needs to
be captured by the classiﬁer. This diversity mandates
the use of a more complex representation which is one
of the strengths of deep neural networks over other
parametric models. The other two datasets demon-
strate the applicability of the method in diﬀerent con-
texts, including the detection of anomalies occurring
only at certain instances in time and thus represent-
ing problems of Type B described in Section 2.2.
4.1 Cardiology dataset
The PTB Diagnostic ECG Database is a database
created by the Physikalisch-Technische Bundesanstalt
(PTB) consisting of 549 electrocardiogram (ECG)
recordings gathered from 290 subjects aged 18 to 87.
The ECGs were recorded using a non-commercial PTB
prototype recorder, the speciﬁcations of which can be
found on the database website[2]. The dataset is part
of PhysioNet [26] and is further described in [18].
4.1.1 Input data
We use 3/5 and 1/5 of the measurements from healthy
patients for training and validation, respectively. The
trained classiﬁer is tested on the remainder of the data
from healthy patients and data from all ill patients.
Due to the large data volume, we manually resam-
ple the input data to a sample rate of 50 samples per
second instead of the original 1000 before feeding it
into the neural network (i.e. the actual time unit ap-
plied in our training amounts to 1 time unit = 20 ms).
This operation is not strictly necessary, but it speeds
up the training process. Also, we only use the ﬁrst 60
periods of each recording during training and for test-
ing. We train our classiﬁer with resampled time series
from healthy patients and use the data coming from
all 12 conventional leads and 3 Frank leads (cf. [27])
for the ECG diagnostic, resulting in a convolutional
neural net with 15 channels on the input layer.
[2]https://physionet.org/physiobank/database/ptbdb/


## Page 12


Ahrens et al.
Page 12 of 25
4.1.2 Period detection
The ﬁrst challenge when analysing ECG data consists
in detecting the randomly varying periods of individual
patients, for which we design a period detector. This
detector is described in greater detail in Appendix A.
The detector has a number of parameters which need
to be adjusted to the dataset, the actual values used
here are given in Table 2. For this dataset, the entire
Table 2: Parameters for period detector on ECG
database
Parameter
Value
preﬁlter window half-length n
10
minimum base period length smin
500
maximum base period length smax
2000
maximum period length deviation factor σ
1/2
reference window half-length factor λ
1/3
time series for feature ‘i’ is used as both the reference
and input time series to the period detector. However,
in order to ensure the requirement that no trend com-
ponent exists in the signal, the ﬁrst diﬀerence of the
signal is used instead of the raw signal. In order to ad-
just for the oﬀsets thus introduced at peak detection,
between Steps 4 and 5 described in Appendix A, the
reference window is adjusted to be precisely centred
on the corresponding peak in the original (smoothed
but not diﬀerentiated) signal, i.e., its midpoint Tk0 is
changed to
arg max
Tk0−10≤t≤Tk0+10
Xt.
The maximum allowed adjustment of 10 has empiri-
cally been found to yield satisfactory results.
The median of all observed period lengths approxi-
mately amounts to s = 700 ms = 35 time units.
4.1.3 Hyperparameters
During the training, the maximum allowed number of
classes and per-class margin of error are set to n∗
0 := 10
and α := 2−5, respectively.
As per description in Table 1, each of the class-
ﬁer neural networks encountered during the run con-
sists of two convolutional layers with M (0) = 15 and
M (1) = 90 channels, respectively, with max pooling
of size R(1) = 3 applied in between, followed by two
fully connected layers, and the output layer. During
the classiﬁer selection process, the length T (0) of the
input sequence, the kernel sizes S(0), S(2) of the con-
volutional layers, and the size N (3) of the ﬁrst fully
connected layer vary proportionally to the sliding win-
dow length T = ⌊3s/n0⌋= ⌊105/n0⌋where n0 runs
over the values in {10(= n∗
0), 8, 6, 4} if not stopped
earlier. The size N (4) of the second fully connected
layer is determined by the geometric mean of the sizes
N (3), N (5) of its adjacent layers and the size N (5) of the
output layer is equal to the current number of classes
n which runs over the values in {n0, n0 −1, . . .} during
the dynamic reclustering.
The ADAM optimiser with learning rate γ = 0.1 is
employed for training with SGD. We start at a mini-
batch size of 800 and increase it after every 2 or 3
epochs up to 4800.
4.2 SCADA dataset
In [19], Antoine Lemay and Jos´e M. Fernandez de-
scribe a simulation of an industrial control system,
speciﬁcally designed for providing supervisory control
and data acquisition (SCADA) network datasets for
intrusion detection research. The generated datasets
are openly available on GitHub[3] and contain peri-
ods of regular operation, manual interactions with the
system, and anomalies caused by network intrusions.
Since the operation of the simulated system is cyclic,
the resulting data is mostly periodic.
4.2.1 Input data
Among the available datasets with common charac-
teristics, we choose the ﬁrst 4/5 and the last 1/5 of
the dataset named ‘characterization modbus 6RTU
with operate’ with a duration of 5.5 minutes in total
for training and validation, respectively, where nei-
ther the injected malicious activities nor the manual
operations included are labelled, both resulting in a
certain proportion of noise in the corresponding time
series. The trained classiﬁer is tested on the only three
correctly labelled datasets ‘moving two ﬁles modbus
6RTU’ (‘Test Data 1’), ‘CnC uploading exe modbus
6RTU with operate’ (‘Test Data 2’), and ‘send a fake
command modbus 6RTU with operate’
(‘Test
Data
3’), including no manual operations, a small portion
of manual operations, and a large amount of noise
e.g. manual operations (causing non-intrusion anoma-
lies), respectively. In each dataset, four features are
considered: number and total size of sent packets, and
number of active IP address and port pairs. At one-
second intervals, we record the increase in each feature
and consider the corresponding 4-dimensional time se-
ries.
The given 10-seconds polling interval yields periodic
characteristics of the considered time series with a
ﬁxed period length of s = 10 seconds.
4.2.2 Hyperparameters
We set α := 2−3 and n∗
0 := 10 for training the classiﬁer
neural networks.
According to Table 1, all convolutional neural net-
works considered during the entire run include M (0) =
[3]https://github.com/antoine-lemay/Modbus_dataset


## Page 13


Ahrens et al.
Page 13 of 25
4 and M (1) = 24 channels on the ﬁrst and second con-
volutional layers, respectively, and two fully connected
layers placed between the last convolutional layer and
the output layer. Considering the short input sequence
length T (0) = ⌊3s/n0⌋= ⌊30/n0⌋with n0 taking val-
ues in {10(= n∗
0), 8, . . .}, we do not apply any max
pooling, i.e. R(1) = 1. During the classiﬁer selection
process, the sizes S(0), S(2) and N (3) of the connvolu-
tion kernels and the ﬁrst fully connected layer, respec-
tively, vary proportionally to the input length T (0).
The size of the output layer N (5) is equal to the cur-
rent number of classes n which runs over the values in
{n0, n0 −1, . . .} during the dynamic reclustering and
the size of its preceding fully connected layer N (4) is
the geometric mean of N (5) and N (3).
The ADAM optimiser with learning rate γ = 0.01
and a mini-batch size of 4 are used for training with
SGD.
4.3 Wave dataset
The waves dataset is a synthetic dataset loosely mod-
elled on a system transmitting a periodic signal. From
the theory of Fourier analysis, every diﬀerentiable peri-
odic signal {xt}t with frequency f can be decomposed
into its frequency components
xt = a0 +
∞
X
k=1
ak cos(2π(fkt + ϕk)),
cf. [28, Theorem 2.1], which motivates the principal
rule of our wave generator. In our consideration, the
generated waves have no DC oﬀset, i.e. a0 := 0, and
components only up to frequency 4f, i.e. ak := 0 for
all k ≥5. The signals are supposed to be transmitted
over a noisy channel which we assume to add ﬁltered
Brownian and white noise. The wave generator also
has some inherent randomness in the form of clock
jitter, amplitude noise, and phase noise. There are also
a number of fault conditions which form the basis of
the anomalies to be detected.
4.3.1 Wave generator
The waves in this dataset are of the form
Xt =
4
X
k=1
Ramp k
t
cos(2π(fkTt +Rph k
t
))+Rnoise
t
+Nt,
t = 0, 1, 2, . . . , with Tt given by
Tt =
t−1
X
u=0
Rtime
u
for t = 0, 1, 2, . . .
and f
:= 2−8. Here, {Nt}t is a Gaussian white
noise process, i.e., N0, N1, N2, . . . are independent and
identically distributed (i.i.d.) random variables with
Nt ∼N(0, σ2) for all t = 0, 1, 2, . . . , and {Ramp k
t
}t,
{Rph k
t
}t, {Rnoise
t
}t, and {Rtime
t
}t are independent (dis-
crete) Ornstein-Uhlenbeck processes with individual
sets of parameters. In general, an Ornstein-Uhlenbeck
process {Rt}t obeys the stochastic diﬀerential equa-
tion
dRt = θ(µ −Rt) dt + σ dWt,
(4.1)
where µ ∈R, σ > 0, θ ∈[0, 1], and {Wt}t is a
standard Brownian motion, cf. e.g. [29, Ex. 6.6]. In
discrete time, a process {Rt}t=0,1,2,... following (4.1)
can be approximated by generating i.i.d. random vari-
ables ˜N0, ˜N1, ˜N2, . . . with ˜Nt ∼N(µ, (σ/θ)2) for all
t = 0, 1, 2, . . . and exponentially smoothing them:
Rt+1 := θ ˜Nt + (1 −θ)Rt
for t = 0, 1, 2, . . . . (4.2)
Indeed, letting
N ∗
t :=
˜Nt −µ
σ/θ
for t = 0, 1, 2, . . . ,
the process {Wt}t=0,1,2,... with
Wt :=
t−1
X
u=0
N ∗
u
is a random walk with Gaussian increments and thus
corresponds to a discretely sampled standard Brown-
ian motion [30, (1.9)]. Therefore, (4.2) can be written
as
Rt+1 −Rt = θ

µ + σ
θ N ∗
t

−θRt
= θ(µ −Rt) + σ(Wt+1 −Wt),
which yields a discrete counterpart of (4.1). The
Ornstein-Uhlenbeck process can be thought of as a
process performing a random walk where the incre-
ments are biased towards the mean µ. As such, it
behaves locally like a Brownian motion, causing the
power of the higher frequency parts of its spectrum
to average 1/f 2 (brownian noise). The process can be
used to model parameters of systems that tend to shift
over time, while generally remaining close to a certain
average value.
For each single wave, a set of parameters controlling
the governing processes is randomly generated using
the parameters in Table 3. The means of the processes
for amplitude and phase variation are sampled accord-
ing to the following law:
log2 µamp k ∼U(−1, 1)
and
µph k ∼U(0, 1)


## Page 14


Ahrens et al.
Page 14 of 25
Table 3: Parameters for processes governing generated
waves (k = 1, 2, 3, 4)
Process
µ
σ
θ
R0
{Rtime
t
}t
1
2−8
2−8
0
{Ramp k
t
}t
µamp k
2−8
2−8
µamp k
{Rph k
t
}t
µph k
2−10
2−8
µph k
{Rnoise
t
}t
0
2−6
2−8
0
{Nt}t
0
2−4
N/A
N/A
for k = 1, 2, 3, 4, where U(a, b) denotes the uniform
distribution on the interval [a, b). They remain con-
stant throughout the wave and determine the overall
shape of the wave.
4.3.2 Generated anomalies
Based on the parameters and processes employed by
the wave generator, we inject the following four types
of anomalies or noise:
Amplitude anomalies The
amplitude
process
{Ramp k
t
}t of one of the frequency components
(i.e., for a single k ∈{1, 2, 3, 4}) is increased by
a, where a is randomly sampled for each anomaly
according to the law log2 a ∼U(1, 2).
Phase anomalies The phase process {Rph k
t
}t of one
of the frequency components is changed. The
amount of change is randomly sampled for each
anomaly from the distribution U(1/4, 3/4) result-
ing in a random phase change of at least 90◦and
at most 270◦.
Pulse anomalies A pulse of random amplitude is
added onto the wave. For each anomaly, the am-
plitude p of the pulse is randomly sampled ac-
cording to the law log2 p ∼U(2, 4) and the pulse
width is a random integer drawn from the interval
[25, 26).
White noise The white noise process {Nt}t is am-
pliﬁed by a factor α which is randomly sampled
for each anomaly according to the law log2 α ∼
U(2, 6).
For each wave, a segment of 216 samples is generated.
Then 16 segments, each consisting of 212 samples are
generated, the last 211 samples of which the anomaly
or noise is injected into. For the evaluation, we use 24
generated waves, resulting in a number of 290 anoma-
lies and 94 waves with increased white noise in the test
dataset.
4.3.3 Input data and period detection
The generated waves are considered in 24 groups,
where each group consists of a normal wave recorded
over 28 = 256 periods and further recordings, each
injected with a single type of anomaly with a nor-
mal start-up time of at least 211 = 2048 time units
(i.e. the ﬁrst entrance time of anomalies following the
respective normal wave is to the right of the time
stamp 211 = 2048). In each group, we take the ﬁrst
7/8 and the remainder of the normal wave for training
and validation, respectively, and subsequently test the
trained classiﬁer on the respective anomaly-injected
test recordings.
Since the simulated waves contain interference in
the time component which results in random period
lengths s, we again make use of the period detector
decribed in Appendix A using the parameters speci-
ﬁed in Table 4. Note that in contrast to the treatment
Table 4: Parameters for period detector on wave
dataset
Parameter
Value
preﬁlter window half-length n
8
minimum base period length smin
240
maximum base period length smax
272
maximum period length deviation factor σ
1/4
reference window half-length factor λ
1/3
of ECG data, in each data group the reference window
is selected among the subpatterns extracted from the
training data.
By construction, the average period length equals
s = 28 = 256 time untis.
4.3.4 Hyperparameters
Throughout the entire training, we set the maximum
number of classes and allowed per-class margin of error
to n∗
0 := 10 and α := 2−6, respectively.
As presented in Table 1, for each of the 24 waves
the corresponding classiﬁer neural nets are all endowed
with M (0) = 1 channel and M (1) = 6 channels on
the ﬁrst and second convolutional layers, respectively,
where max pooling of size R(1) = 3 is applied between
the covolutional layers, and two fully connected layers
are set between the last convolutional layer and the
output layer. During the classiﬁer selection process,
the length T (0) of the input sequence, the sizes S(0),
S(2) of the convolution kernels, and the size N (3) of
the ﬁrst fully connected layer vary proportionally to
the sliding window length T = ⌊3s/n0⌋= ⌊768/n0⌋
where n0 runs over the values in {10(= n∗
0), 8, 6, 4} if
not stopped earlier. The size N (4) of the second fully
connected layer is the geometric mean of the sizes N (3)
and N (5) of its adjecent layers and the size N (5) of the
output layer is equal to the current number of classes
n which runs over the values in {n0, n0 −1, . . .} during
the dynamic reclustering.
The ADAM optimiser with learning rate γ = 0.01 is
employed for training with SGD. The mini-batch sizes
are dynamically increased after every 2 or 3 epochs
from 40 to 360.


## Page 15


Ahrens et al.
Page 15 of 25
5 Experimental results
In this section we present the empirical results of the
treatment of the example datasets given in Section 4
following our general phase classiﬁcation scheme de-
scribed in Section 3. Here we provide both the re-
sults of selecting and training the optimal classiﬁer
neural networks and the results of anomaly detection
obtained by evaluating the trained classiﬁer neural net-
works on the test data (recall Section 3.4).
5.1 Cardiology dataset
The ultimate classiﬁer resulting from the dynamic
model selection process turns out to be a classiﬁer neu-
ral network corresponding to initial number of classes
n0 = 6 and ﬁnal number of classes nn0 = 4, cf. Ta-
ble 5 for the layout of the ﬁnal CNN. The label his-
Table 5: Layers of ﬁnal classiﬁer neural network for
ECG dataset
Layer Type
Sizes
0
convolutional
M(0) = 15, T (0) = 17,
S(0) = 7
1
max pooling
M(1) = 90, T (1) = 17,
R(1) = 3
2
convolutional
M(2) = 90, T (2) = 6,
S(2) = 5
M(3) = 270, T (3) = 6
3
fully connected
N(3) = 1620
4
fully connected
N(4) = 80
5
output
N(5) = 4
tory recorded along with the dynamic reclustering is
shown in Table 6. The average validation loss recorded
Table 6: Label History
Epochs
Merge
New Labels
0 – 9
N/A
[0, 1, 2, 3, 4, 5]
9 →10
3 to 2
[0, 1, 2, 2, 4, 3]
24 →25
4 to 2
[0, 1, 2, 2, 2, 3]
25 – 43
N/A
[0, 1, 2, 2, 2, 3]
during the training of the respective neural nets is pre-
sented in Figure 2. A training accuracy of 99% and a
validation accuracy of 96% are achieved.
Figures 3 and 4 illustrate the result of testing the
trained classiﬁer on three patients from the category
‘healthy control’ and three ill patients: the measure-
ments on feature ‘i’ from the test patients are pre-
sented in a temporal resolution of 20 ms and the bars
in the upper and lower halves of the ﬁgures refer to the
predicted classes and the true labels of the segments
from the considered test signals, respectively.[4]
[4]Note that here and in the sequel the coloured bars in
these diagrams are always plotted between the begin-
nings of adjacent segments to be classiﬁed, thus only
covering approximately the ﬁrst third of each segment.
0
10
20
30
40
0.0
0.1
0.2
0.3
0.4
0.5
Figure 2: Validation loss over 44 epochs for training
the classiﬁer neural nets with n0 = 6, nn0 = 4
Figure 5 presents a statistical evaluation of the
per-patient test results on patients from the 7 most
recorded categories in the considered database: ‘dys-
rhythma’, ‘valvular heart disease’, ‘cardiomyopathy/
heart failure’, ‘bundle branch block’, ‘hypertrophy’,
‘myocardial infarction’, and ‘healthy control’.
The
lines in diﬀerent colors represent the empirical distri-
bution functions of the per-patient classiﬁcation accu-
racy from the aforementioned categories. Observe that
the blue line related to healthy patients is located in
the bottom right corner of the diagram, to the left
of which all other lines corresponding to ill patients
are centred (cf. the median for each category), which
enables us to distinguish ill patients from healthy pa-
tients in some cases. For instance, according to the ﬁg-
ure, if we take the average validation accuracy of 96%
as the threshold for the per-patient classiﬁcation accu-
racy, all test patients from the categories ‘dysrhythma’
and ‘valvular heart disease’, 90% and nearly 85% of the
patients from the categories ‘cardiomyopathy/heart
failure’ and ‘myocardial infarction’, respectively, and
over 70% of the patients from the categotries ‘bundle
branch block’ and ‘hypertrophy’ will be considered as
anomalies, whereas up to three false positive results
(25% of) all tested patients from the category ‘healthy
control’ will be assessed as normal. Since the sample
sizes provided for the individual categories vary a lot
(e.g. there are 148 subjects for ‘myocardial infarction’
whereas the entire category ‘healthy control’ consists
of only 52 subjects including training, validation and
test data applied in our context), we are not in the
position to make a general statement on the choice of
an ideal threshold value. Table 7 provides a statisti-
cal evaluation of the per-disease average classiﬁcation
accuracy. It turns out that the category ‘healthy con-
trol’ presents by far the best test result compared to
all other categories related to heart disease (anomaly).
Note that our anomaly detection scheme does not in-
corporate any speciﬁc cardiological knowledge. It gives


## Page 16


Ahrens et al.
Page 16 of 25
700
750
800
850
900
950
1000
500
1000
1500
2000
2500
700
750
800
850
900
950
1500
1000
500
0
500
1000
700
750
800
850
900
950
1000
500
0
500
1000
1500
2000
Figure 3: Classiﬁer applied to patients from cate-
gory ‘healthy control’
Table 7: Results of per-disease classiﬁcation accuracy
Disease
Classiﬁcation
Accurracy
Valvular heart disease
56%
Dysrhythmia
60%
Cardiomyopathy/Heart failure
64%
Myocardial infarction
73%
Bundle branch block
76%
Hypertrophy
86%
Healthy control
97%
700
800
900
1000
1100
1000
500
0
500
1000
1500
(a) Classiﬁer applied to a dysrthythmia patient
700
750
800
850
900
500
0
500
1000
1500
2000
(b) Classiﬁer applied to a valvular-heart-disease patient
700
750
800
850
900
1000
750
500
250
0
250
500
750
1000
(c) Classiﬁer applied to a myocardial-infarction patient
Figure 4: Classiﬁer applied to ill patients


## Page 17


Ahrens et al.
Page 17 of 25
Figure 5: Distribution of per-patient classiﬁcation
accuracy evaluated on test patients from diﬀerent
categories
an indication whether a patient may be ill or not, it de-
tects deviations from the known healthy data and does
not classify the diseases separately. It also only gives a
statistical indication, which is a result somewhat sim-
ilar to the one reported in [31] where it was observed
that the ECGs of ill patients showed deviations in cer-
tain aﬃne dependencies usually present between the
12-lead and 3-lead ECGs of healthy patients.
5.2 SCADA dataset
The ﬁnal classiﬁer determined by means of the dy-
namic model selection scheme uses n0 = 10 and nn0 =
4, cf. Table 8 for the layout of the ﬁnal CNN. The
Table 8: Layers of ﬁnal classiﬁer neural network for
SCADA dataset
Layer Type
Sizes
0
convolutional
M(0) = 4, T (0) = 3,
S(0) = 3
1
max pooling
M(1) = 24, T (1) = 3,
R(1) = 1
2
convolutional
M(2) = 24, T (2) = 3,
S(2) = 3
M(3) = 72, T (3) = 3
3
fully connected
N(3) = 216
4
fully connected
N(4) = 29
5
output
N(5) = 4
respective label history recorded during the dynamic
reclustering and the evolution of the average validation
loss are presented in Table 9 and Figure 6, respectively.
In Figure 7, the number of active port pairs extracted
from ‘Test Data 1’ is plotted against time (in seconds)
and the bars in the upper and lower halves represent
the classes predicted by our trained neural net and
the true labels of the test segments, respectively; seg-
ments which result in prediction errors are considered
anomalies.
Table 9: Label History
Epochs
Merge
New Labels
0 – 34
N/A
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
34 →35
1 to 4
[0, 4, 2, 3, 4, 5, 6, 7, 8, 1]
68 →69
3 to 4
[0, 4, 2, 4, 4, 5, 6, 7, 3, 1]
92 →93
7 to 4
[0, 4, 2, 4, 4, 5, 6, 4, 3, 1]
110 →111
5 to 4
[0, 4, 2, 4, 4, 4, 5, 4, 3, 1]
128 →129
2 to 4
[0, 4, 4, 4, 4, 4, 2, 4, 3, 1]
143 →144
2 to 4
[0, 2, 2, 2, 2, 2, 2, 2, 3, 1]
144 – 160
N/A
[0, 2, 2, 2, 2, 2, 2, 2, 3, 1]
0
20
40
60
80
100
120
140
160
0.0
0.5
1.0
1.5
2.0
Figure 6: Validation loss over 161 epochs for train-
ing the classiﬁer neural nets with n0 = 10, nn0 = 4
50
60
70
80
90
100
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
20.0
Figure 7: Classiﬁer applied to test data


## Page 18


Ahrens et al.
Page 18 of 25
The ﬁnal results of our anomaly detection algorithm
on the entire test data are summarised in Table 10.
In the ﬁrst two (cleaner) test datasets with no or only
Table 10: Results of Intrusion Detection
Dataset
Detection Rate
False Positives
Test Data 1
4/4
0
Test Data 2
3/3
1%
Test Data 3
0/1
8%
a small amount of manual operations (noise), all cy-
ber attacks in the test data are detected along with
a single false positive detection (corresponding to 1%
false detection rate in ‘Test Data 1’), whereas the clas-
siﬁer tested on the last test dataset including a large
amount of noise performs not as good, which is not
surprising taking into account that only malicious ac-
tivities but no manual operations or any other types
of interference are labelled as anomalies and our time
series analysis does not include the respective context
consideration.
Indeed, the SCADA datasets which are applica-
ble in our setting are quite small. Due to the non-
compatability between datasets with small and large
amounts of noise (i.e. non-intrusion anomalies appear-
ing in the form of pulses), it is diﬃcult to choose one
suitable dataset for training and to test the intrusion
detector on datasets with incompatible characteristics,
e.g., it would be unfeasible to train an anomaly de-
tector on one of the cleaner datasets and then test
it against a noisy dataset, or vice versa. For a more
extensive treatment of anomaly detection of Type B
described in Section 2.2 using a richer dataset and the
corresponding results, cf. Section 4.3 and Section 5.3.
5.3 Wave dataset
Overall, an average classiﬁcation accuracy of 99% is
achieved on both training and validation data.
Figures 8, 9, 10 and Figure 11 present the detection
results of our classiﬁers trained by individual exam-
ple waves and tested on segments injected with diﬀer-
ent types of anomalies and white noise, respectively.
Again, in each diagram the bars in the upper and
lower halves refer to the predicted classes and true
labels of the data from the test segments fed into
the trained classiﬁer, respectively. Notice that in Fig-
ure 11, slightly increased white noise does not lead to
any classiﬁcation errors, which suggests some robust-
ness property of our classiﬁer against noise.
The ﬁnal results of our anomaly detection algorithm
tested on the 24 groups of synthetic waves are shown
in Table 11. The amount of anomalies and white noise
are obtained by counting the number of test waves in-
jected with the respective type of interference, whereas
the denominator for evaluating false positives equals
2600
2700
2800
2900
3000
3100
3200
3300
3400
3
2
1
0
1
2
3
4
5
Figure 8: Classiﬁer with n0 = 10, nn0 = 10 applied
to wave with pulse anomaly injected at time stamp
3072
1600
1700
1800
1900
2000
2100
2200
2300
2400
3
2
1
0
1
2
3
4
Figure 9: Classiﬁer with n0 = 10, nn0 = 6 applied to
wave with abnormal phases starting at time stamp
2048
1600
1700
1800
1900
2000
2100
2200
2300
4
3
2
1
0
1
2
3
4
Figure 10: Classiﬁer with n0 = 10, nn0 = 9 applied
to wave with abnormal amplitudes starting at time
stamp 2048


## Page 19


Ahrens et al.
Page 19 of 25
1600
1700
1800
1900
2000
2100
2200
2300
2400
3
2
1
0
1
2
3
4
Figure 11: Classiﬁer with n0 = 10, nn0 = 8 applied
to wave with slightly increased white noise (σ =
4.77) starting at time stamp 2048
Table 11: Results of Anomaly Detection
Type
Detection Rate
%
Phases
83/85
98%
Amplitudes
102/102
100%
Pulse
102/103
99%
Total Anomalies
287/290
99%
False Positives
115/26798
0.43%
White noise (σ ≤6)
11/19
58%
White noise (σ > 6)
64/75
85%
the number of available prediction windows (test seg-
ments) in the clean test data. Overall, our algorithm
yields high detection rates of all types of injected
anomalies (99% on average); the small rate of false
positives (< 1%) conﬁrms the model adequacy of our
phase classiﬁcation scheme; the low error rate in the
presence of increased white noise shows the robustness
of our classiﬁer neural networks against noise to a cer-
tain extent.
6 Conclusion
In this paper, we proposed a novel approach to de-
tecting anomalies in time series exhibiting periodic
characteristics, where we applied deep convolutional
neural networks for phase classiﬁcation and automated
phase similarity tagging. We evaluated our approach
on three example datasets corresponding to the do-
mains of cardiology, industry, and signal processing,
conﬁrming that our method is feasible in a number of
contexts.
Appendix A: Period detection scheme
In this section, we provide the details for the period
detection scheme used for the ECG and synthetic wave
datasets. This period detection scheme is primed us-
ing a reference signal {Y raw
t
}t and then applied to the
actual input signal {Xraw
t
}t. It is assumed that the
input signals do not have a trend component, which
can be achieved by a suitable transformation of the
input signals, such as taking the ﬁrst diﬀerence as in
the ECG data case, cf. Section 4.1. The detection is
now performed in the following steps:
1
Smooth the signals by applying a rolling mean
2
Infer approximate base period using the autocor-
relation of the reference signal
3
Detect peaks in the reference signal spaced ap-
proximately one base period apart using a simple
peak detection logic
4
Take the average of segments around the detected
peaks and ﬁnd one reference segment which most
closely matches this average
5
Cross-correlate the input signal with the reference
segment
6
Detect peaks in the cross-correlation spaced ap-
proximately one base period apart using again the
simple peak detection logic
The steps are described in more detail in the follow-
ing paragraphs.
Step 1: The raw signals {Xraw
t
}t and {Y raw
t
}t
are subjected to a rolling mean ﬁlter, resulting in
smoothed signals {Xt}t and {Yt}t, respectively, i.e.,
Xt :=
1
2n + 1
n
X
k=−n
Xraw
t+k, Yt :=
1
2n + 1
n
X
k=−n
Y raw
t+k .
The window length 2n + 1 of this ﬁlter is chosen to
provide just enough ﬁltering to dampen some of the
noise contained within the input signal.
Step 2: The sample autocorrelation
ˆρY
τ
of the
(smoothed) reference signal {Yt}t at lag τ is computed
via
ˆρY
τ := ˆrY
τ
ˆrY
0
for τ = 0, . . . , NY −1
with
ˆrY
τ :=
1
NY
NY −1−τ
X
t=0
(Yt+τ −¯Y )(Yt −¯Y )
(cf. [20, 2.1.5]), where NY and ¯Y denote the sample
size and sample mean of the reference signal Y , re-
spectively. Now the mean period length ˆs is inferred
by taking the arg max of ˆρτ restricted to some interval
[smin, smax], i.e.,
ˆs :=
arg max
smin≤τ≤smax
ˆρY
τ .
A plot of an example autocorellation function is shown
in Figure 12, the inferred mean period length is dis-
played by the vertical line.


## Page 20


Ahrens et al.
Page 20 of 25
0
2000
4000
6000
0.5
0.0
0.5
1.0
Figure 12: Autocorrelation function of one of the
ECG database records
Step 3: The reference signal is now fed into a simple
peak detector which proceeds to inductively ﬁnd peaks
Tk spaced approximately one base period apart via
T0 :=
arg max
0≤t≤⌈ˆs(1+σ)⌉
Yt, Tk+1 :=
arg max
Tk+⌊ˆs(1−σ)⌋≤t≤Tk+⌈ˆs(1+σ)⌉
Yt,
where σ ∈[0, 1) is a tolerance value to account for the
variability of period lengths in the signals.
Step 4: The detector now extracts subpatterns
{U (k)
t
}⌈ˆsλ⌉
t=⌊−ˆsλ⌋from the reference signal Yt centred at
the peaks Tk, i.e., U (k)
t
= YTk+t. Here, λ ∈(0, 1/2] is
another tolerance parameter to mitigate the eﬀects of
period length variability. Then the seasonal means
¯Ut := 1
M
M−1
X
k=0
U (k)
t
are computed. Here M denotes the total number of
subpatterns. Let now
k0 := arg max
k
⌈ˆsλ⌉
X
t=⌊−ˆsλ⌋
U (k)
t
¯Ut
and
U ref
t
:= U (k0)
t
.
The choice of k0 ensures that {U ref
t
}⌈ˆsλ⌉
t=⌊−ˆsλ⌋is the
subpattern with maximum similarity to the mean
{ ¯Ut}⌈ˆsλ⌉
t=⌊−ˆsλ⌋and is thus suited as a reference pattern.
Step 5: The reference pattern is now used for detect-
ing the periods in the input signal by computing the
cross-correlation function:
Cτ := (X ⋆U ref)τ =
⌈ˆsλ⌉
X
t=⌊−ˆsλ⌋
Xτ+tU ref
t
, τ ≥0
Step 6: Finally the simple peak detector from Step 3
is applied to the cross-correlation {Cτ}τ to obtain the
ﬁnal segment beginnings.
A comparison of the periods detected by the simple
peak detector from Step 3 and the cross-correlating pe-
riod detector from Step 6 can be seen in Figure 13. The
0
2000
6000
8000 10000 12000 14000
0
50000
Figure 13: Comparison of periods detected in the
Steps 3 and 6
top graph shows the input to the simple peak detector,
the bottom graph shows the cross-correlation; the gray
boxes in the top half of the backgrounds represent the
segments inferred by the simple peak detector, those
in the bottom half represent those found by the cross-
correlating period detector. Notice how glitches in the
input signal easily manage to confuse the simple peak
detector while the cross-correlating period detector is
robust to such perturbations.
Appendix B: Comparison with other
methods
In this section we perform some comparative evalua-
tion of other methods in order to highlight in particu-
lar the utility of phase classiﬁcation via convolutional
neural networks for anomaly detection. We consider
two classes of methods: distance-based approaches em-
ploying various types of Euclidean distance compar-
ison (cf. Sections B.1 and B.2) and one-step ahead
forecasting (cf. Section B.3). In the ﬁrst class of com-
parison we demonstrate that even in a phase classi-
ﬁcation framework, simply comparing the Euclidean-
type norm of segments of the underlying signals is less
suited for capturing the essence of complex and noise
corrupted data. In the second class of comparison we
show that even with the highly complex parametrisa-
tion of LSTMs, anomaly detection based on one-step
ahead prediction is prone to false positive results. Since
the ECG dataset exhibits the highest level of diversity
and is thus most diﬃcult to treat among all example


## Page 21


Ahrens et al.
Page 21 of 25
datasets introduced in Section 4, for this demonstra-
tion we only evaluate the reference methods on this
dataset.
B.1 Self-similarity approach
One way of detecting anomalies in periodic signals is
to take a sliding window of roughly one period length,
normalise it, and look for a similar segment in the data
preceding the window by e.g. one to two periods. A
threshold is then used to determine whether the con-
sidered window is similar enough to one of the preced-
ing segments. This principle is used in the so-called
matrix proﬁles approach, cf. e.g. [9]. No training data
is used in this method and thus no particular charac-
teristics of the normal data themselves are employed
during the anomaly detection. The only point where
training data can be useful in this approach is to deter-
mine the similarity threshold mentioned above, choos-
ing it so as to avoid having too many false positives on
non-anomalous data.
B.1.1 Method
Formally, if {Xt}t is the input signal and T is the
window length, normalise each segment X(τ)
:=
{Xτ+t}t=0,...,T −1 for τ ≥0 in an analogous manner to
that of Section 3.1.3 and denote by ˜X(τ), τ ≥0, the re-
spective normalised segments. Now choose a minimum
shift dmin and a maximum shift dmax and compute for
each τ ≥dmax
aτ :=
min
τ ′=τ−dmax,...,τ−dmin∥˜X(τ ′) −˜X(τ)∥2
where ∥˜X(τ ′) −˜X(τ)∥denotes the Euclidean distance
of ˜X(τ ′) to ˜X(τ), i.e.,
∥˜X(τ ′) −˜X(τ)∥2 =
T −1
X
t=0
∥˜X(τ ′)
t
−˜X(τ)
t
∥2
Rd.
aτ is called the self-dissimilarity of {Xt}t at time τ.
Now depending on the type of problem, there are
two ways to decide whether a signal is anomalous: If
the task is one of Type A described in Section 2.2, the
average self-dissimilarity of the test signal is computed
and compared against some threshold which can for in-
stance be determined by the average self-dissimilarities
of the training signals. If on the other hand the task
is one of Type B described Section 2.2, a threshold
is chosen close to the maximum self-dissimilarity of
the known normal part of the signal and the self-
dissimilarity for the remaining part of the signal is
compared against this threshold.
B.1.2 Results
For the sake of comparison, we evaluate the perfor-
mance of the self-similarity-based approach on the
ECG database in a similar manner as in our main
result in Section 5.1 and ﬁrst transform the self-
dissimilarity computed as described above into a self-
similarity rating via the transformation x 7→1/(x+1).
We then average the self-similarities for each recording
and plot the distributions of these averages grouped
by disease. This plot is shown in Figure 14a. One can
clearly see that, apart from patients of the category
‘dysrhythmia’ which have the lowest self-similarity,
this approach does not manage to produce any sep-
aration of ill from healthy patients.
B.2 Distance-based phase classiﬁcation
A distance analysing method similar to that of Sec-
tion B.1 but more closely related to our main ap-
proach is to compute reference windows for the dif-
ferent phases of non-anomalous signals and use these
to classify the corresponding segments of the other sig-
nals by assigning the class whose reference window has
maximum similarity. Basically, this is the same method
as our phase classiﬁcation scheme but with the classi-
ﬁer neural network replaced by a simple nearest refer-
ence classiﬁer.
B.2.1 Method
For this method the same data pre-processing with
respect to a chosen number of classes n0 as described
in Section 3.1 is applied to training, validation, and
test signals.
For the training dataset X consisting of normalised
segments ˜Xθ labelled as belonging to class θ for θ =
0, . . . , n0 −1 (recall the set X in Figure 1 for both
types A and B), we compute for each class of phase θ
the seasonal averages
˜Xθ,mean := n0
#X
X
˜
Xθ∈X labelled θ
˜Xθ.
The classiﬁcation of a normalised segment ˜X(m) =
{ ˜X(m)
t
}t=0,...,T −1 (labelled m mod n0) of a test (or val-
idation) signal {Xt}t is now performed by computing
arg min
θ=0,...,n0−1
∥˜X(m) −˜Xθ,mean∥
where again ∥·∥denotes the Euclidean norm as de-
scribed in Section B.1.
The remaining part of anomaly detection is per-
formed as in Section 3.4.


## Page 22


Ahrens et al.
Page 22 of 25
0.55
0.60
0.65
0.70
0.75
0.80
0.85
Values of per-patient self-similarity
0.0
0.2
0.4
0.6
0.8
1.0
Relative cumulative frequency of occurrence
Empirical distribution functions
Healthy control
Dysrhythmia
Valvular heart disease
Cardiomyopathy/Heart failure
Bundle branch block
Hypertrophy
Myocardial infarction
(a) Distribution of per-patient self-similarity evaluated
on test patients from diﬀerent categories
0.0
0.2
0.4
0.6
0.8
1.0
Values of per-patient classification accuracy
0.0
0.2
0.4
0.6
0.8
1.0
Relative cumulative frequency of occurrence
Empirical distribution functions
Healthy control
Dysrhythmia
Valvular heart disease
Cardiomyopathy/Heart failure
Bundle branch block
Hypertrophy
Myocardial infarction
(b) Distribution of per-patient distance-based classiﬁca-
tion accuracy evaluated on test patients from diﬀerent
categories
0.2
0.4
0.6
0.8
Values of per-patient prediction precision
0.0
0.2
0.4
0.6
0.8
1.0
Relative cumulative frequency of occurrence
Empirical distribution functions
Healthy control
Dysrhythmia
Valvular heart disease
Cardiomyopathy/Heart failure
Bundle branch block
Hypertrophy
Myocardial infarction
(c) Distribution of per-patient forecasting precision
evaluated on test patients from diﬀerent categories
Figure 14: Distribution of per-patient values for dif-
ferent comparison algorithms
B.2.2 Results
To evaluate the performance of the distance-based
phase classier on the ECG database, just as in our
main result in Section 5.1 we record the classiﬁcation
accuracy on the diﬀerent types of heart disease and
analyse the distribution of the per-patient classiﬁca-
tion accuracy grouped by the corresponding disease.
The separation into training, validation, and test data
is the same as in our main experiment on the ECG
database (cf. Section 4.1.1). For the number of classes,
a setting of n0 = 6 shows the best results, which con-
forms to our model selection result (cf. optimal n0 pre-
sented in Section 5.1). The average validation accuracy
amounts to 79%. The per-disease average classiﬁcation
accuracy is evaluated in Table 12. A plot of the distri-
Table 12: Results of per-disease classiﬁcation accuracy
Disease
Classiﬁcation
Accurracy
Valvular heart disease
28%
Dysrhythmia
37%
Cardiomyopathy/Heart failure
44%
Myocardial infarction
51%
Bundle branch block
59%
Hypertrophy
60%
Healthy control
78%
bution of per-patient classiﬁcation accuracy evaluated
on test patients from diﬀerent categories is shown in
Figure 14b. As can be seen from both the table and
the plot when compared to the results of our approach
(cf. Figure 5 and Table 7), the convolutional classiﬁer
neural network delivers generally better classiﬁcation
performance with far better results being obtained on
the healthy control patients. In particular, we see that
the blue line representing the healthy test patients in
Figure 5 is located much closer to the bottom right
corner than in Figure 14b, indicating better modelling
of the normal data by our convolutional classiﬁer neu-
ral network. An anomaly detection using the distance-
based classiﬁer thus would have a higher false positive
rate than one using the convolutional neural network
for classiﬁcation when achieving comparable detection
performance. For instance, according to Figure 14b,
if we use the average validation accuracy of 79% as
the threshold value as discussed in our main result in
Section 5.1, a similar detection rate in most of the ill
categories but a higher false positive rate of 38% on
healthy test patients will be achieved compared to the
result of our approach (25% on healthy test patients,
cf. Section 5.1).
B.3 Long short-term memory predictor approach
As described in Section 2.3.3, one can use a long short-
term memory unit (LSTM) to predict the signal one


## Page 23


Ahrens et al.
Page 23 of 25
time step ahead, then use a threshold on the diﬀer-
ence of this prediction to the actual signal to decide
whether the signal behaves as expected or should be
considered anomalous. We choose to demonstrate this
method in preference to the statistical forecasting ap-
proaches mentioned in Section 2.3.2, as no further ad-
justment to the method is needed for handling prob-
lems of Type A described in Section 2.2 and, more im-
portantly, the forecasting performance of LSTMs on
data with complex patterns has been shown to be bet-
ter than that of linear models in general.
B.3.1 Method
Since LSTMs are a somewhat complex type of recur-
rent neural network, we will not describe their con-
struction here and instead refer the reader to the liter-
ature on the subject, e.g. [32]. In our treatment of the
ECG database, we use an LSTM with an input layer
size of 15, a hidden layer size of 60, and an output
layer size of again 15. We use a mean-squared-error
loss function, discarding the ﬁrst 200 predictions (four
seconds) to allow the LSTM to ﬁrst align with the
given signal. We use the same ADAM algorithm for the
training of the LSTM that we also employed for train-
ing our convolutional classiﬁer neural networks with a
learning rate of γ = 2−10 and 210 training epochs. The
separation into training, validation, and test data is
also the same as in our main experiment on the ECG
database (cf. Section 4.1.1).
B.3.2 Results
To evaluate the performance of the LSTM on the ECG
database, we analyse the distribution of the forecast-
ing precision on the patients coming from the diﬀer-
ent groups. A plot of this distribution is shown in
Figure 14c. The measure of performance used here is
given by 1/(MSE + 1) where MSE denotes the mean
squared error of the predictions on the ECG record-
ing. This transformation is applied again for the sake
of easier comparability with our main result in Sec-
tion 5.1. Using the same measure of performance, the
prediction precision evaluated on the training and vali-
dation data are 91% and 63% on average, respectively.
The large gap between the training and validation per-
formance suggests the presence of the overﬁtting phe-
nomenon mentioned in Section 2.3.3, whereas our clas-
siﬁer CNN approach does not suﬀer from this problem
(see the consistency of training and validation accu-
racy results presented in Section 5.1). As presented
in Figure 14c, if we choose a threshold value of 63%
based on the validation performance as discussed in
our main result in Section 5.1, this will lead to a false
positive anomaly detection rate of 31% on healthy test
patients, which is higher than that of our approach
(25%); at the same time, the detection performance
of the LSTM-based detector is lower, with e.g. only
about 75% of the patients labelled ‘myocardial infarc-
tion’ (the largest category) being detected as anoma-
lous, compared to the almost 85% of our approach.
Furthermore, for illustration purposes, two examples
of the predictions coming from the LSTM are displayed
in Figure 15. Notice that for both patients, the pre-
0
100
200
2
1
0
1
2
3
(d) Prediction for a healthy patient
0
100
200
4
2
0
2
4
(e) Prediction for a patient with myocardial infarction
Figure 15: Example prediction results of LSTM pre-
dictor
diction fails to guess the (randomly varying) values
at the spikes in the signals correctly. This (randomly)
contributes to the mean squared error and thus results
in a weaker separation ability of the anomaly detector.
List of Abbreviations
ARIMA autoregressive integrated moving average
ARMA autoregressive–moving average
CNN convolutional neural network
DC direct current


## Page 24


Ahrens et al.
Page 24 of 25
ECG electrocardiogram
i.i.d. independent and identically distributed
IP Internet Protocol
LSTM long short-term memory
MSE mean squared error
PTB Physikalisch-Technische Bundesanstalt
RNN recurrent neural network
SARIMA seasonal autoregressive integrated moving
average
SCADA supervisory control and data acquisition
SGD stochastic gradient descent
Availability of data and materials
The datasets used for the evaluation of the algorithm are available online at
PhysioNet https://physionet.org/physiobank/database/ptbdb/ and
the GitHub repository
https://github.com/antoine-lemay/Modbus_dataset.
Competing interests
The authors declare that they have no competing interests.
Funding
The work has been funded by the German Research Center for Artiﬁcial
Intelligence and the Technical University of Kaiserslautern.
Authors’ contributions
LA devolped and implemented the core concepts of the algorithm presented
within this manuscript, JA provided reﬁnements and performed data
acquisition and generation as well as further supplemental programming,
HDS provided further technical knowledge and support.
Acknowledgements
The authors would like to thank the anonymous referees for providing
valuable suggestions which helped clarify the exposition of the material.
Furthermore, the authors would like to thank Dr.-Ing. J¨org Schneider for
many fruitful discussions, in particular about the cardiology dataset.
Authors’ information
LA has a Ph.D. in Mathematics, specialises in stochastic processes,
stochastic ﬁltering, and machine learning, and is currently working as a
senior researcher at the German Research Center for Artiﬁcial Intelligence.
JA has a Master’s degree in mathematics, specialises in non-commutative
harmonic analysis, has a background in digital signal processing and
machine learning, and is currently working as a researcher at the German
Research Center for Artiﬁcial Intelligence. HDS is the Scientiﬁc Director of
the Intelligent Networks Research Group at the German Research Center for
Artiﬁcial Intelligence and head of the Institute for Wireless Communication
and Navigation at the Technical University of Kaiserslautern.
Author details
1Deutsches Forschungszentrum f¨ur K¨unstliche Intelligenz, Trippstadter
Straße 112 67663 Kaiserslautern, Germany.
2Technische Universit¨at
Kaiserslautern, Paul-Ehrlich-Straße 11 67663 Kaiserslautern, Germany.
References
1. Dang, T.T., Ngan, H.Y.T., Liu, W.: Distance-Based k-Nearest
Neighbors Outlier Detection Method in Large-Scale Traﬃc Data. In:
Proceedings of the 2015 IEEE International Conference on Digital
Signal Processing (DSP 2015), Singapore, pp. 507–510 (2015)
2. Breunig, M.M., Kriegel, H.-P., Ng, R.T., Sander, J.: LOF: Identifying
Density-Based Local Outliers. In: Proceedings of the 2000 ACM
SIGMOD International Conference on Management of Data, pp.
93–104. SIGMOD, Dallas, TX, USA (2000)
3. Kailing, K., Kriegel, H.-P., Kr¨oger, P.: Density-Connected Subspace
Clustering for High-Dimensional Data. In: Proceedings of the 2004
SIAM International Conference on Data Mining, Lake Buena Vista,
FL, USA, pp. 246–256 (2004)
4. Chen, J., Sathe, S., Aggarwal, C., Turaga, D.: Outlier Detection with
Autoencoder Ensembles. In: Proceedings of the 2017 SIAM
International Conference on Data Mining, Houston, TX, USA, pp.
90–98 (2017)
5. Xu, H., Chen, W., Zhao, N., Li, Z., Bu, J., Li, Z., Liu, Y., Zhao, Y.,
Pei, D., Feng, Y., Chen, J., Wang, Z., Qiao, H.: Unsupervised
Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in
Web Applications. In: Proceedings of the 2018 World Wide Web
Conference. WWW ’18, pp. 187–196. International World Wide Web
Conferences Steering Committee, Republic and Canton of Geneva,
Switzerland (2018)
6. Louni, H.: Outlier detection in ARMA models. Journal of Time Series
Analysis 29(6) (2008)
7. Ting, J.-A., Theodorou, E., Schaal, S.: A Kalman ﬁlter for robust
outlier detection. In: Proceedings of the IEEE/RSJ International
Conference on Intelligent Robots and Systems, San Diego, CA, USA,
pp. 1514–1519 (2007)
8. Yin, Q., Shen, L.-R., Zhang, R.-B., Li, X.-Y., Wang, H.-Q.: Intrusion
detection based on hidden Markov model. In: Proceedings of the
Second International Conference on Machine Learning and
Cybernetics, Xi’an, China, pp. 3115–3118 (2003)
9. Yeh, C.-C.M., Zhu, Y., Ulanova, L., Begum, N., Ding, Y., Dau, H.A.,
Silva, D.F., Mueen, A., Keogh, E.: Matrix Proﬁle I: All Pairs Similarity
Joins for Time Series: A Unifying View That Includes Motifs, Discords
and Shapelets. In: 2016 IEEE 16th International Conference on Data
Mining (ICDM), Barcelona, Spain, pp. 1317–1322 (2016)
10. Gers, F.A., Schmidhuber, J., Cummins, F.: Learning to Forget:
Continual Prediction with LSTM. Neural Computation 12(10),
2451–2471 (2000)
11. Yan, H., Ouyang, H.: Financial Time Series Prediction Based on Deep
Learning. Wireless Personal Communications 102(2), 683–700 (2018)
12. Bengio, Y., Simard, P., Frasconi, P.: Learning Long-Term
Dependencies with Gradient Descent is Diﬃcult. IEEE Transactions on
Neural Networks 5(2), 157–166 (1994)
13. Hochreiter, S., Bengio, Y., Frasconi, P., Schmidhuber, J.: Gradient
Flow in Recurrent Nets: the Diﬃculty of Learning Long-Term
Dependencies. In: Kolen, J.F., Kremer, S.C. (eds.) A Field Guide to
Dynamical Recurrent Networks, pp. 237–244. IEEE Press, Piscataway,
NJ, USA (2001)
14. Pascanu, R., Mikolov, T., Bengio, Y.: On the diﬃculty of training
Recurrent Neural Networks. In: 30th International Conference on
Machine Learning, ICML, Atlanta, GA, USA, pp. 2347–2355 (2013)
15. Krizhevsky, A., Sutskever, I., Hinton, G.E.: ImageNet Classiﬁcation
with Deep Convolutional Neural Networks. In: Pereira, F., Burges,
C.J.C., Bottou, L., Weinberger, K.Q. (eds.) Advances in Neural
Information Processing Systems 25, pp. 1097–1105. Curran Associates,
Inc., Lake Tahoe, NV, USA (2012)
16. Szegedy, C., Ioﬀe, S., Vanhoucke, V., Alemi, A.A.: Inception-v4,
Inception-ResNet and the Impact of Residual Connections on Learning.
In: ICLR 2016 Workshop, San Juan, Puerto Rico (2016)
17. Borovykh, A., Bohte, S., Oosterlee, C.W.: Dilated Convolutional
Neural Networks for Time Series Forecasting. Journal of
Computational Finance (online early) (2018)
18. Bousseljot, R., Kreiseler, D., Schnabel, A.: Nutzung der
EKG-Signaldatenbank CARDIODAT der PTB ¨uber das Internet.
Biomedizinische Technik/Biomedical Engineering 40(s1), 317–318
(1995)
19. Lemay, A., Fernandez, J.M.: Providing SCADA network data sets for
intrusion detection research. In: 9th USENIX Workshop on Cyber
Security Experimentation and Test (CSET ’16), Austin, TX, USA
(2016). USENIX Association
20. Box, G.E.P., Jenkins, G.M., Reinsel, G.C.: Time Series Analysis:
Forecasting and Control, 4th edn. Wiley Series in Probability and
Statistics, p. 784. John Wiley & Sons, Inc., Hoboken, NJ, USA (2008)
21. Elliott, R.J., Aggoun, L., Moore, J.B.: Hidden Markov Models:
Estimation and Control, 1st edn. Stochastic Modelling and Applied
Probability, vol. 29, p. 382. Springer, NY, USA (1995)
22. Zeiler, M.D., Fergus, R.: Visualizing and Understanding Convolutional
Networks. In: Fleet, D., Pajdla, T., Schiele, B., Tuytelaars, T. (eds.)
Computer Vision – ECCV 2014, Lecture Notes in Computer Science,
pp. 818–833. Springer, Cham, Switzerland (2014)
23. Goodfellow, I., Bengio, Y., Courville, A.: Deep Learning. MIT Press,
Cambridge, MA, USA (2016)
24. Smith, S.L., Kindermans, P.-J., Le, Q.V.: Don’t Decay the Learning
Rate, Increase the Batch Size. In: International Conference on Learning


## Page 25


Ahrens et al.
Page 25 of 25
Representations, Vancouver, Canada (2018)
25. Kingma, D.P., Ba, J.L.: Adam: A Method for Stochastic Optimization.
In: International Conference on Learning Representations, San Diego,
CA, USA (2015)
26. Goldberger, A.L., Amaral, L.A.N., Glass, L., Hausdorﬀ, J.M., Ivanov,
P.C., Mark, R.G., Mietus, J.E., Moody, G.B., Peng, C.-K., Stanley,
H.E.: PhysioBank, PhysioToolkit, and PhysioNet: Components of a
New Research Resource for Complex Physiologic Signals. Circulation
101(23) (2000)
27. Frank, E.: An Accurate, Clinically Practical System For Spatial
Vectorcardiography. Circulation 13(5), 737–749 (1956)
28. Stein, E.M., Shakarchi, R.: Fourier Analysis: An Introduction.
Princeton Lectures in Analysis, vol. 1, p. 326. Princeton University
Press, Princeton, NJ, USA (2003)
29. Shreve, S.: Stochastic Calculus for Finance II: Continuous-Time
Models, 1st edn. Springer Finance Textbooks, p. 550. Springer, NY,
USA (2004)
30. Revuz, D., Yor, M.: Continuous Martingales and Brownian Motion, 3rd
edn. Grundlehren der mathematischen Wissenschaften, vol. 293, p.
602. Springer, Berlin Heidelberg, Germany (1999)
31. Dawson, D., Yang, H., Malshe, M., Bukkapatnam, S.T.S., Benjamin,
B., Komanduri, R.: Linear aﬃne transformations between 3-lead
(Frank XYZ leads) vectorcardiogram and 12-lead electrocardiogram
signals. Journal of Electrocardiology 42(6), 622–630 (2009)
32. Hochreiter, S., Schmidhuber, J.: Long Short-Term Memory. Neural
Computation 9(8), 1735–1780 (1997)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
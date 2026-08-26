---
canon-group: reference
rscf-state: source-claim
arxiv_id: 0901.4295v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 0901.4295v1_Breakdown_of_Long-Range_Correlations_in_Heart_Rate_Fluctuations_During_Meditatio

> Source: 0901.4295v1_Breakdown_of_Long-Range_Correlations_in_Heart_Rate_Fluctuations_During_Meditatio.pdf

> Pages: 6

---


## Page 1


Breakdown of Long-Range Correlations in Heart Rate Fluctuations During Meditation
Nikitas Papasimakis∗† and Fotini Pallikari
University of Athens, Faculty of Physics, Department of Solid State Physics,
Panepistimiopolis Zografou, 15784 Athens, Greece
The average wavelet coeﬃcient method is applied to investigate the scaling features of heart rate
variability during meditation, a state of induced mental relaxation. While periodicity dominates
the behavior of the heart rate time series at short intervals, the meditation induced correlations
in the signal become signiﬁcantly weaker at longer time scales. Further study of these correlations
by means of an entropy analysis in the natural time domain reveals that the induced mental re-
laxation introduces substantial loss of complexity at larger scales, which indicates a change in the
physiological mechanisms involved.
INTRODUCTION
In the past decade, the erratic behavior of heart in-
terbeat intervals in humans has attracted considerable
attention and its study has evolved to a virtually inter-
disciplinary topic, encompassing diverse disciplines, such
as cardiology, engineering and more recently physics. It
has been suggested that heart rate variability (HRV) can
provide non-invasive prognosis and diagnosis tools for a
number of pathological conditions [1, 2]. Most impor-
tantly, it was demonstrated that heart rate variability
exhibits various features that can be used to distinguish
between heart rate under healthy and life-threatening
conditions [3, 4, 5]. Furthermore, it has been shown that
the study of HRV can lead to a better understanding of
the dynamics of the underlying physiological mechanisms
[6] in a variety of diﬀerent conditions, such as apnea [7],
sleep [8] etc. It is widely accepted that neuroautonomic
control results in modulation of HRV [9] through the an-
tagonistic action of the two branches of the autonomic
system, namely the sympathetic (SNS) and parasympa-
thetic (PNS). The ﬁrst tends to increase heart rate and
acts on long time scales (below 0.15 Hz, while the latter
is related to decreased heart rate and dominates frequen-
cies above 0.15 Hz. The eﬀects of meditation on heart
rate were observed to excite prominent low frequency os-
cillations appearing to be driven by the regularity of the
imposed breathing pattern.
This observation is rather
unexpected considering that meditation is thought of as
a quiescent state of the brain. [10]. Further studies sug-
gested that diﬀerent meditative protocols induce diﬀerent
types of cardiovascular response that are not necessarily
linked to respiratory conditions (sinus arrhythmia) [11].
In this work we investigate the behavior of heart rate
variability during meditation at even longer time scales
that range from roughly 15 sec to 20 min covering the low
(LF) and very low (VL) frequency band. By estimating
∗Current Aﬃliation: Optoelectronics Research Centre, University
of Southampton, Southampton SO17 1BJ, United Kingdom
†Electronic Address: N.Papasimakis@orc.soton.ac.uk
FIG. 1: RR intervals before (a) and during (b) meditation.
the corresponding scaling exponent, we show that medi-
tation leads to the breakdown of long-range correlations
and loss of the 1/f character. Our ﬁndings extend previ-
ous studies [12, 13] to indicate that complex physiological
changes take place during meditation.
METHODS
We studied a publicly available (RR) interbeat inter-
val database (www.physionet.org) consisting of data col-
lected from eight healthy subjects (aged 29-35) before
and during Qigong meditation (more information on the
dataset and the meditation method can be found in [10]).
The length of the time series varied between 50 and
80 minutes. One characteristic case of the RR interval
time series, before and during meditation, is presented in
Figs. 1a & 1b, respectively, where the evident irregular
character of the time series before meditation gives its
place to smoother cyclic oscillations during meditation.
The evolution of the time series was studied by the ap-
plication of two techniques, namely the average wavelet
coeﬃcient (AWC) method, which quantiﬁes the intensity
of long-range correlations and the method that estimates
arXiv:0901.4295v1  [physics.bio-ph]  27 Jan 2009


## Page 2


2
the entropy in the natural time domain which captures
the complexity characteristics of the time series.
Scaling exponent estimation - average wavelet
coeﬃcient method
The complex features exhibited by HRV stem from the
presence of the regulatory systems operating at diﬀerent
time scales. Such systems that that generate ﬂuctuations
in the heart rate at all time scales, can be characterized
by means of a fractal analysis [8]. A time series is termed
fractal, when it possesses scale invariant characteristics
at all scales. In practice the fractal character is usually
limited to a range of scales and is traditionally quantiﬁed
by a scaling exponent H. When 0 < H < 1, then the
process possesses stationary increments and H is usu-
ally called the Hurst exponent.
In particular, a truly
random process, YH(t), with uncorrelated but stationary
increments exhibits H = 0.5.
For H < 0.5 the pro-
cess is mean-returning and is said to demonstrate anti-
persistent fractal behavior, while for H > 0.5 the pro-
cess is mean-averting and persistent [14]. The graph of
YH(t) is then a fractal, with fractal dimension D = 2−H
[14, 15]. The increments of YH(t) also exhibit scale in-
variance with a scaling exponent equal to H −1, where H
is the scaling exponent of YH(t). Therefore, it is through
integration that one goes from a process of negative scal-
ing exponents to one whose scaling exponents range in
the interval (0,1).
For diﬀerentiable processes or pro-
cesses with non-stationary increments H > 1. Heart rate
variability, on the other hand, has characteristics lying
on the threshold of non- stationarity for which H ≃1, a
behavior typical for systems far from equilibrium. The
power spectrum of such a process scales with frequency f
as 1/f, known from this as 1/f noise. In the present study,
the analyzed time series exhibit close to zero or negative
scaling exponents. In order to facilitate interpretation,
they will always be considered to be the increments of
the process of interest; hence all values of H will refer to
the latter and not to the original time series.
The estimation of the scaling exponent in the case
of non-stationary processes is a complex problem, espe-
cially when deterministic trends are superimposed on the
stochastic signal of interest. A range of methods has been
developed to overcome this obstacle, each one being more
appropriate for a speciﬁc kind of trends [16, 17, 18]. A
very popular approach is the use of detrended ﬂuctua-
tion analysis (DFA). During DFA the data are coarse-
grained and a best-ﬁt polynomial is selected at each seg-
ment of the time series for every scale [16]. While this
method is ideal for slowly varying polynomial trends, it
fails when it comes to cyclic components. Its shortcoming
is illustrated in Fig. 2a, where DFA is applied on a ran-
dom Gaussian noise signal of standard deviation σ = 1
with a superimposed sinusoidal trend of amplitude 1 and
FIG. 2:
DFA (a) and AWC analysis (b) of Gaussian noise
(σ = 1) with (blue squares) and without (red circles) a super-
imposed sinusoidal trend (sin(0.15x)).
frequency 0.15 Hz. DFA identiﬁes correctly the global
scaling behavior of the random signal yielding a scaling
exponent H = 0.51 with standard error 0.03.
On the
contrary, when the sinusoidal component is introduced,
DFA indicates three diﬀerent scaling regions each yield-
ing a diﬀerent scaling exponent and fails to isolate the
behavior of the stochastic component which might lead
to spurious results [6]. Measures to overcome such diﬃ-
culties have been addressed in the past [19].
We have adopted here the wavelet-based method, since
the wavelet transform provides localization both in the
time and frequency domain, while at the same time it
can be made orthogonal to polynomial trends.
More
precisely, the wavelet transform W[f(t)] of a function
f(t) is given by: Wa,b[f(t)] =
R
f(t)ψa,b(t)∗dt, where
a and b are scale and location parameters, respectively,
while the ”child” wavelet ψa,b(t) is derived by appropriate
scaling of the so-called ”mother” wavelet ψ(t) through
the transformation ψa,b(t) =
1
√aψ( t−b
a ) [20].
Figure 3
presents color maps of wavelet coeﬃcients over the time-
scale plane before and during meditation. In both cases,
the behavior of the interbeat intervals shows great com-
plexity as ﬂuctuations of varying intensity occur at all
scales. However, during meditation increased values of
the wavelet coeﬃcient can be observed as a light colored
band parallel to the horizontal (time) axis at scales in the
range of 8−32 beats. This is a signature of periodic com-
ponents present at these frequencies in agreement with
previous studies [1]. In our analysis we apply the aver-
age wavelet coeﬃcient method [18].
According to this
approach, at every scale a, the average value, < Wa >,
of the wavelet coeﬃcients (over all values of the location
parameter b) is calculated. If the analyzed time series
is self-similar with scaling exponent H, then its average
wavelet coeﬃcient will scale as aH+0.5 [18]. Therefore,


## Page 3


3
FIG. 3:
Absolute values of wavelet transform coeﬃcients,
|W|, of interbeat intervals for subject no. 1 of the studied
dataset before (a) and during (b) meditation.
one can estimate the scaling exponent of a given time
series by plotting the average wavelet coeﬃcient versus
the scale parameter a in a log-log plot (scalogram) and
performing a linear least-squares ﬁt to the graph.
Figure 2b illustrates how the sinusoidal component can
be isolated in the frequency (scale) domain by the AWC
method. Indeed, both the Gaussian noise and that with
the superimposed sinusoidal trend are indistinguishable
and exhibit linear scaling apart from a small frequency
region around the frequency of the sinusoidal component,
where the scalogram shows an isolated peak indicative of
the narrow frequency spectrum of the sinusoidal compo-
nent. These localization properties of the wavelet trans-
form allow for a robust estimation of the scaling expo-
nent, even in the presence of strong cyclic components.
Entropy in the natural time domain
The complexity characteristics of the heart rate time
series are investigated by means of an entropy approach
based on the concept of natural time x, which has origi-
nally been introduced in [21, 22, 23] to distinguish seismic
electric signals [24] from artiﬁcial noise. This analysis was
later extended [25, 26] to electrocardiograms (ECG) [27],
since it is equally applicable to deterministic as well as
stochastic processes and physiological time series most
likely contain components of both types (see [25, 28]
and references therein). The entropy approach in nat-
ural time works as follows. In a signal composed of N
pulses, the natural time x is introduced by ascribing the
value xm = m/N to the m−th pulse, so that the analysis
is made in terms of the couple (xm, Qm), where Qm de-
notes the duration of the m−th pulse [21]. The entropy S
is deﬁned as [27] S =< xlnx > −< x > ln < x >, where
< f(x) >= PN
m=1 ρmf(xm) and ρm = Qm/ PN
n=1 Qn.
The entropy S−obtained after time reversal T [29] so
that Tpm = pN−m+1, is diﬀerent from the initial S and
their diﬀerence ∆S = S −S−was found to be of major
importance towards distinguishing sudden cardiac death
(SCD) individuals from healthy subjects (H) [28].
In
particular, the analysis considers a window of width i
sliding over the whole RR (beat-to-beat) interval time
series, read in natural time, one pulse at a time. The
entropies S, S−and their diﬀerence ∆Si are then esti-
mated at every step. This diﬀerence provides a measure
of the temporal asymmetry of the correlations in the time
series. More precisely, the physical meaning of ∆Si is de-
rived in the following way. It has been shown [30] (see
also Appendix 4 of Ref. [28]) that the estimated ∆Si for
the parametric family p(x, ϵ) = 1 + ϵ(x −1/2), (|ϵ| < 1)
becomes negative for values of ϵ in the range 0 < ϵ < 1
(increasing trend).
∆Si becomes positive for ϵ < 0 (
decreasing trend).
Applying this result in the case of
ECGs indicates that the variation of the ∆Si with scale
i may be thought of as capturing the net result of the
competing mechanisms that either decrease or increase
the heart rate (cf. the complex dynamics of heart rate is
attributed to the antagonistic activity of the parasympa-
thetic and the sympathetic nervous systems decreasing
and increasing heart rate,respectively [5]. Furthermore,
the variability of ∆Si, quantiﬁed by its standard devia-
tion σ[∆Si] with respect to time, indicates whether one
of the two mechanisms is dominant (large values σ[∆Si])
or both are of roughly the same intensity (small values
σ[∆Si]). Such an analysis performed on 159 ECG cases
in natural time has shown [28] that ventricular ﬁbrilla-
tion starts within three hours after ∆Si (at the scale
i = 13 heartbeats) had become maximum for the 16 out
of 18 SCD subjects. This time scale corresponds to the
so-called low frequency (LF) band found in heart rate
(from 0.04 to 0.15 Hz), i.e. at around 0.1 Hz, which
is usually attributed to ”the process of slow regulation
in blood pressure and heart rate” [31]. Beyond the LF
band, it was demonstrated that at scale i= 3 (HF band)
a similar complexity measure based on natural time do-
main entropy allows for the distinction between SCD and
in the healthy subjects, since a smaller variability in en-
tropy was observed in SCD than the healthy subjects,
suggesting a breaking down of the high complexity [28].
In the present study, it is shown that the variance of
the ∆S can be used to probe distinctive physiological
changes occurring at the VLF band during meditation,
marking the loss of the 1/f character of heart rate at
normal breathing conditions.
RESULTS
The AWC analysis was applied in the range of scales
from Nmin = 4 up to Nmax = 512 conditioned by the pre-
requisite that the average must be estimated over a suf-


## Page 4


4
FIG. 4:
Characteristic scalogram before (blue) and during
(red) meditation for subject no. 1 of the studied dataset.
ﬁcient number of uncorrelated wavelet coeﬃcients even
for Nmax.
Color maps of the wavelet coeﬃcients as a
function of scale and time before and during meditation
are shown in Fig. 3 for one characteristic case. While be-
fore meditation, the wavelet transform exhibits complex
behavior over all scales, during meditation the wavelet
presents strong maxima at a narrow scale region around
N = 15 beats, where most of the signal power is concen-
trated. This variance of behavior is more clearly seen in
Fig. 4, where the corresponding scalograms are presented
before (blue) and during meditation (red) obtained by av-
eraging the wavelet coeﬃcients over the time axis. The
time series before meditation exhibits the typical 1/f be-
havior of HRV with linear scaling across all scales and a
scaling exponent of 1.1 with standard error 0.1. The pic-
ture changes dramatically during meditation. A strong
peak appears in the scalogram at a frequency of about
0.22 Hz, which marks the maximum of spectral power.
At longer time scales, the graph returns to linear scal-
ing, but with a much lower scaling exponent, H = 0.43
with standard error 0.1, which indicates the weak anti-
persistence of a mean-returning process.
A summary of the results for all subjects is presented
in Fig. 5. In all cases but two (6 and 7), the scaling ex-
ponent during meditation drops signiﬁcantly. In the two
other cases there is no statistically signiﬁcant change in
the scaling exponents before and after meditation (at a
p = 0.05 level). The collective average scaling exponent
before meditation is 1.15 with standard error 0.03, while
during meditation it drops to 0.71 with standard error
0.08. This decrease indicates a change from the verge of
non-stationarity to a medium level of persistence. It im-
plies that the overall long-range correlations of the RR
interbeat intervals at normal breathing have gotten sig-
niﬁcantly weaker during meditation. The H values ex-
hibit now a persistent fBm character [14, 15] most likely
induced by the regularity of the breathing pattern.
The entropy S in the natural time domain was calcu-
lated in a range of scales from Nmin = 3 to Nmax = 60
beats. Then the time series were inverted with respect
FIG. 5:
Scaling exponents before (blue) and during (red)
meditation.
to time so that S−and consequently the diﬀerence ∆S
was estimated. The standard deviation of ∆S as a func-
tion of scale (number of beats) is presented in Fig. 6 for a
characteristic case (subject no. 1). In both conditions be-
fore (blue) and during (red) meditation, σ[∆S] increases
rapidly at small scales up to about 10-15 beats. At larger
scales however, the two curves present distinctively diﬀer-
ent features. Before meditation, σ[∆S] increases steadily
with increasing scale but at a lower rate than before. On
the other hand, during meditation, the situation reverses
and σ[∆S] decreases with increasing scale. The decrease
or increase of σ[∆S] at longer time scales, is quantiﬁed by
ﬁtting a linear trend and calculating the corresponding
slope, s. Most other subjects’ σ[∆S] behaves similarly,
increasing before meditation and decreasing during med-
itation. An exception was seen for subject no. 7, where
the two slopes are practically indistinguishable. Includ-
ing this odd case, the average slope before meditation
(over all subjects) is found to be 14 · 10−6 with stan-
dard error 3 · 10−6, while during meditation its value is
−10·10−6 with standard error 4·10−6, implying that the
two values are statistically diﬀerent.
DISCUSSION
This study provides evidence that meditation, a state
of induced deep mental relaxation, brings about changes
in the cardiovascular system in addition to the previ-
ously observed enhancement of its low frequency compo-
nents [10]. Such changes occur at even lower frequencies
and cannot be attributed to cardio-respiratory synchro-
nization. In particular, the drop of the scaling exponent
during meditation suggests that the 1/f-noise character
that was previously identiﬁed to portray inﬁnite long-
range correlations within the heart rate time series is
now lost. That result can be related to the antagonis-


## Page 5


5
FIG. 6:
Standard deviation of ∆S before (blue) and (red)
during meditation for subject no. 1 of the studied dataset.
Dashed lines represent linear ﬁts on the estimated values.
tic control between the two branches of the autonomic
nervous system which is responsible for the HRV at the
LF band [6].
In particular, it appears that the heart
rate interbeat interval time series during meditation ex-
hibits fBm character [14, 15], either appearing as weak
persistence or as anti-persistence. This diversity can be
considered as evidence of an irregular competitive inter-
play between the sympathetic (SNS) and the parasym-
pathetic nervous system (PNS). Whereas for 1/f noise
large deviations from the average behavior of heart rate
are common, such deviations become rare when persis-
tence is observed (1 > H > 0.5). They get however quite
sparse in the case of anti-persistence, i.e. when mean-
returning traits are present in the heart rate time series.
We argue here that during meditation the balance be-
tween SNS and PNS can be readily restored and con-
sequently, small deviations of one of the two are quickly
compensated by the other, avoiding thus the known large
excursions from the typical heart rate behavior.
Such
a view can also explain the fact that the characteristic
features are located even further at the VLF band. In-
deed, although the physiological mechanisms responsible
for HRV at this band have not been yet elucidated, it is
believed that they include a strong contribution from the
autonomic nervous system [32].
The results of the entropy analysis performed on the
same data conﬁrm the above picture. The standard de-
viation of ∆S during meditation exhibits an overall de-
creasing trend at large scales, as opposed to its premed-
itation trend. A diminishing trend in the standard de-
viation of ∆S at larger scales, implies that the correla-
tions in the heart rate do not vary considerably during
meditation.
In fact, since ∆S quantiﬁes the temporal
asymmetry of these correlations, the observed behavior
can be interpreted as follows: Under normal conditions,
the asymmetry seen in the correlations of the heart rate
picture under time reversal, varies strongly and becomes
more intense at larger scales [33]. On the contrary, dur-
ing meditation this variation is much weaker and it di-
minishes further with increasing scale.
Hence, we can
argue that during meditation the mechanisms responsi-
ble for the observed correlations (and their asymmetries)
in heart rate variability do not vary considerably with
respect to time. Plausible causes for this change of be-
havior under meditation may involve both internal and
external sources. One possible origin can be the calm,
quiescent state adopted by those who meditate. Another
factor may be the shielding from external stimuli and the
absence of physical movement, frequent in normal waken
states that may no more pose great demands towards the
balancing action between the two nervous systems.
It is inevitable to question the implications of the cur-
rent results regarding the state of health of a subject
who is meditating.
There is the assumption that the
1/f behavior is a sign of a healthy condition [34] and
given that meditation seems to alter this state of be-
ing, one may wonder if meditation is beneﬁcial condi-
tion for the heart. This line of thinking, however, may
lead to wrong assumptions, because an induced decrease
in heart rate variability does not exclude its ability to
behave in reverse fashion at normal conditions. In any
case, further study comparing the heart rate variability
of both meditating and non-meditating subjects under
non-meditating conditions is needed in order to clarify
whether the physiological eﬀects of meditation are bene-
ﬁcial to the cardiovascular system.
CONCLUSIONS
In summary, we show that meditation induces distinct
patterns in the heart interbeat intervals. One is a peri-
odic feature in the LF band and another is the loss of
the 1/f character in the VLF band. Our ﬁndings are cor-
roborated through the study of the entropy of the time
series which reveals substantial loss of complexity in the
LF and VLF bands. We argue that the observed behav-
ior can be attributed, at least partly, to changes in the
balance between the sympathetic and parasympathetic
branch of the autonomous nervous system.
[1] K. K. L. Ho et al., Circ. 96, 842-848 (1997).
[2] C. K. Peng et al., Phys. Rev. Lett. 70, 1343-1346 (1993).
[3] C. Raab, N. Wessel, A. Schirdewan, and J. Kurths, Phys.
Rev. E 73, 041907 (2006).
[4] P. C. Ivanov, L. A. N. Amaral, A. L. Goldberger, S.
Havlin, M. G. Rosenblum, Z. R. Struzik, and H. E. Stan-
ley, Nature 399, 461 (1999).
[5] K. Kotani, Z. R. Struzik, K. Takamasu, H. E. Stanley,
and Y. Yamamoto, Phys. Rev. E 72, 041904 (2005).
[6] Z. R. Struzik, J. Hayano, S. Sakata, S. Kwak, and Y.
Yamamoto, Phys. Rev. E 70, 050901(R) (2004).


## Page 6


6
[7] P. C. Ivanov, M. G. Rosenblum, C. K. Peng, J. E. Mietus,
S. Havlin, H. E. Stanley, and A. L. Goldberger, Physica
A 249, 587 (1998).
[8] A. Bunde, S. Havlin, J. W. Kantelhardt, T. Penzel, J. H.
Peter, and K. Voigt, Phys. Rev. Lett 85, 3736 (2000).
[9] G. Parati, G. Mancia, M. D. Rienzo, P. Castiglioni, J.
A. Taylor, and P. Studinger, J. Appl. Physiol. 101, 676
(2006).
[10] C. K. Peng et al., Int. J. Cardiol. 70, 101-107 (1999).
[11] C. K. Peng et al., Int. J. Cardiol. 95, 19-27 (2004).
[12] N. Papasimakis and F. Pallikari, Fractal 2006, Vienna,
Austria, 12-15 February 2006.
[13] A. Sarkar and P. Barat, Fractals 16, 199 (2008).
[14] J. Feder, Fractals (Plenum New York, 1989).
[15] F. Pallikari, Chaos, Solitons & Fractals 12, 1499 (2001).
[16] C. K. Peng, S. Havlin, H. E. Stanley, and A. L. Gold-
berger, Chaos 5, 82 (1995).
[17] C. V. Chianca, A. Ticona, and T. J. P. Penna, Physica
A 357, 447 (2005).
[18] I. Simonsen, A. Hansen, and O. M. Nes, Phys. Rev. E
58, 2779-2787 (1998).
[19] K. Hu, P. C. Ivanov, Z. Chen, P. Carpena, and H. E.
Stanley, Phys. Rev. E 64, 011114 (2001).
[20] I.
Daubechies,
Ten
Lectures
on
Wavelets
(SIAM,
Philladelphia, 1992).
[21] P. A. Varotsos, N. V. Sarlis, and E. S. Skordas, Phys.
Rev. E 66, 011902 (2002).
[22] P. A. Varotsos, N. V. Sarlis, and E. S. Skordas, Phys.
Rev. Lett. 91 , 148501 (2003).
[23] P. A. Varotsos, N. V. Sarlis, H. K. Tanaka, and E. S.
Skordas, Phys. Rev. E 72, 041103 (2005).
[24] P. Varotsos, K. Alexopoulos and K. Nomicos, Phys. Sta-
tus Solidi B 111, 581 (1982)
[25] P. A. Varotsos, N. V. Sarlis, E. S. Skordas, and M. S.
Lazaridou, Phys. Rev. E 70, 011106 (2004).
[26] P. A. Varotsos, N. V. Sarlis, E. S. Skordas, and M. S.
Lazaridou, Phys. Rev. E 71, 011110 (2005).
[27] P. A. Varotsos, N. V. Sarlis, and E. S. Skordas, Phys.
Rev. E 68, 031106 (2003).
[28] P. A. Varotsos, N. V. Sarlis, and E. S. Skordas, and M.
S. Lazaridou, Appl. Phys. Lett. 91, 064106 (2007).
[29] P. A. Varotsos, N. V. Sarlis, H. K. Tanaka, and E. S.
Skordas, Phys. Rev. E. 71, 032102 (2005)
[30] P. A. Varotsos, N. V. Sarlis, E. S. Skordas, H. K. Tanaka,
and M. S. Lazaridou, Phys. Rev. E 73, 031114 (2006).
[31] M. D. Prokhorov, V. I. Ponomarenko, V. I. Gridnev, M.
B. Bodrov, and A.B. Bespyatov, Phys. Rev. E 68, 041913
(2003).
[32] Task Force of the European Society of Cardiology the
North American Society of Pacing and Electrphysiology,
Circulation 93, 1043 (1996).
[33] P. A. Varotsos, N. V. Sarlis, E. S. Skordas, and M. S.
Lazaridou, J. Appl. Phys. 103, 014906 (2008).
[34] A. L. Goldberger, L. A. N. Amaral, J. M. Hausdorﬀ, P.
C. Ivanov, C. K. Peng, and H. E. Stanley, Proc. Natl.
Acad. Sci. USA 99, 2466 (2002).

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 0901_4295v1_breakdown_of_long_range_correlations_in_heart_rate_fluctuations_during_meditatio
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2009/0901_4295V1_BREAKDOWN_OF_LONG_RANGE_CORRELATIONS_IN_HEART_RATE_FLUCTUATIONS_DURING_MEDITATIO.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

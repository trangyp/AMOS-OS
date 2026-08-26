---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.04218v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1911.04218v3_Dynamical_Heart_Beat_Correlations_during_Running

> Source: 1911.04218v3_Dynamical_Heart_Beat_Correlations_during_Running.pdf

> Pages: 19

---


## Page 1


Dynamical Heart Beat Correlations during Running
Matti Molkkari,1, ∗Giorgio Angelotti,2, † Thorsten Emig,2, 3, ‡ and Esa Räsänen1, 2, §
1Computational Physics Laboratory, Tampere University, FI-33720 Tampere, Finland
2Laboratoire de Physique Théorique et Modèles Statistiques, CNRS UMR 8626,
Université Paris-Sud, Université Paris-Saclay, 91405 Orsay cedex, France
3Massachusetts Institute of Technology, MultiScale Materials Science for Energy and
Environment, Joint MIT-CNRS Laboratory (UMI 3466), Cambridge, Massachusetts 02139, USA
(Dated: 2020-07-03)
Fluctuations of the human heart beat constitute a complex system that has been studied mostly
under resting conditions using conventional time series analysis methods. During physical exercise,
the variability of the ﬂuctuations is reduced, and the time series of beat-to-beat RR intervals (RRIs)
become highly non-stationary. Here we develop a dynamical approach to analyze the time evolution
of RRI correlations in running across various training and racing events under real-world conditions.
In particular, we introduce dynamical detrended ﬂuctuation analysis and dynamical partial autocor-
relation functions, which are able to detect real-time changes in the scaling and correlations of the
RRIs as functions of the scale and the lag. We relate these changes to the exercise intensity quantiﬁed
by the heart rate (HR). Beyond subject-speciﬁc HR thresholds the RRIs show multiscale anticor-
relations with both universal and individual scale-dependent structure that is potentially aﬀected
by the stride frequency. These preliminary results are encouraging for future applications of the
dynamical statistical analysis in exercise physiology and cardiology, and the presented methodology
is also applicable across various disciplines.
INTRODUCTION
The increasing popularity and accuracy of wearable
devices and sensors present new opportunities to study
human physiology in a continuous, non-invasive man-
ner for a huge number of subjects under real-world con-
ditions.
These devices enable the measurement of a
plethora of physiological and mechanical signals such as
the heart rate, beat-to-beat (RR) intervals, overall mo-
tion via GPS, motion of speciﬁc body locations via ac-
celerations, and skin temperature.
These data can be
recorded in real time, often at one second intervals, and
uploaded to web services. To date, most recorded data
are not analyzed in scientiﬁc rigour due to a lack of suit-
able models for the dynamics of physiological signals un-
der various intensities of exercise load, and also due to
restricted availability of the data (property of industry
and users). This limits opportunities for a better under-
standing of complex physiological processes, diagnostics
and monitoring for patients in rehabilitation, and the op-
timal training of athletes.
However, it has been long known that a variety of
physiological conditions and cardiac diseases aﬀect heart
rate variability (HRV) and the correlations in RR inter-
vals [1].
In exercise physiology, HRV is often used at
rest to evaluate recovery, fatigue and overtraining.
It
is known that during exercise the overall variability of
the RR intervals (RRI) is strongly suppressed. Regard-
less, the RRI correlations contain valuable information
∗matti.molkkari@tuni.ﬁ
† giorgio.angelotti@isae-supaero.fr
‡ thorsten.emig@lptms.u-psud.fr
§ esa.rasanen@tuni.ﬁ
even during exercise [2–4].
For example, the possibil-
ity to determine certain physiological thresholds, such as
the anaerobic threshold, from the frequency spectrum of
HRV has been examined [5, 6]. Often the relative im-
portance of low-frequency (LF: 0.04–0.15 Hz) and high-
frequency (HF: 0.15–0.4 Hz) spectral power is studied
during exercise. Using this concept as a measure of the
relative sympathetic (SNS) and parasympathetic nervous
system (PNS) activity, it has been shown that the PNS
activity decreases dramatically during exercise [7].
In
contrast, the SNS activity remains unchanged past the
ﬁrst ventilatory threshold before increasing abruptly [7].
However, the use of the HF/LF ratio to measure cardiac
sympatho-vagal balance has been criticized [8].
More-
over, it is known that Fourier decomposition of dynamic
signals is often hampered by non-stationarity.
To overcome the complications of Fourier methods and
non-stationarities, we base our analysis on detrended
ﬂuctuation analysis[9] (DFA), which was developed to
measure correlations in non-stationary time series by uti-
lizing systematic detrending [9–11]. Furthermore, we are
interested in analyzing real world exercises recorded with
readily available commercial sports watches. Hence, we
study real-time correlations of RRIs during marathon
races (group M) and freeform training runs (group T).
Such uncontrolled data may be plagued by severe non-
stationary conditions, and the conventional division into
short- and long-scale DFA exponents[10, 12] is likely
to be insuﬃcient.
To this end, we introduce dynamic
DFA (DDFA) for the accurate determination of time-
and scale-dependent scaling exponents α(t, s) with high
temporal resolution.
To check the consistency of our
methodology, we also apply similar dynamic approach
to partial autocorrelation functions (PACFs) to obtain
their dynamic counterpart (DPACF).
arXiv:1911.04218v3  [physics.data-an]  3 Jul 2020


## Page 2


2
RESULTS
Our main result is the discovery of scale-dependent
anticorrelations (α < 0.5) in the RRIs during running
that vary with the heart rate. The anticorrelations ap-
pear after the HR exceeds a subject-speciﬁc threshold.
Their magnitude and the scale with the most dominant
anticorrelations changes with exercise intensity. We ﬁnd
that the DDFA method can reliably determine the dy-
namic, scale-dependent scaling exponent α(t, s) (please
see the Supplementary Information for its numerical val-
idation). Hence, it provides a powerful method for mea-
suring multiscale correlations of non-stationary physio-
logical signals. The results from the DDFA and DPACF
methods are found to be mutually consistent.
Marathon Races
Figure 1 demonstrates our methods applied to a single
marathon run (subject M1) of group M. The color-coded
value of the scale-dependent exponent α(s) is shown
in the ﬁrst row as a function of the binned heart rate
(HR) [Fig. 1(a)] and also as a function of running time
t [Fig. 1(c)]. Over the studied scales s from 5 to 5000
heart beats, the scaling exponent α(s) exhibits complex
behavior that could not be adequately described by the
conventional division into short- and long-range scaling
exponents. We consider the HR-dependent shift to anti-
correlated RRIs at the shortest scales s <∼10–30 as the
most interesting of our observations. As the heart rate
increases the anticorrelations extend to slightly longer
scales until there is a qualitative change at approximately
175 BPM. The strongest anticorrelations shift from the
shortest scales to roughly 20 beats, and gradually reﬁll
the shortest scales as the HR is increased even further.
At larger scales s >∼100 the RRIs become mostly non-
stationary (α > 1, fractional-Brownian-motion-like be-
havior). In contrast, a typical 24-hour RR-tachogram of
a healthy subject at rest usually displays 1/f or pink
noise on long time scales (or low frequencies <∼0.05 Hz),
corresponding to α = 1, and larger values for α at the
shortest scales or higher frequencies [1].
The black curve in Fig. 1(a) corresponds to the con-
ventional DFA exponent α1 over the scales from 4 to
16 heart beats. It shows almost linear decrease to val-
ues around 1/2 and below, when the DDFA exponent
α(s) displays short-scale anticorrelated behavior. How-
ever, this simpler estimate is not suﬃcient for uniquely
distinguishing the presence of anticorrelations from their
shift to slightly longer scales. To explore the scale depen-
dence of the anticorrelations in more detail, we show in
Fig. 1(e) the probability density for the values of α(s) for
six diﬀerent scales s from 5 to 20 heart beats as a func-
tion of the binned HR. On all six scales, the probability
is maximum for α < 1/2 with a HR dependent modula-
tion and an absence of anticorrelations on the two largest
scales s = 15, 20 for lower beat rates.
In order to estimate the relevant time scales of the
physiological processes behind the observed anticorre-
lated beat intervals, we have also performed a DPACF
analysis. The result is shown for lags between 1 and 20
heart beats in Figs. 1(b) and 1(d). The PACF reveals
direct anticorrelations (negative values) after a time lag
of 1 and 2 beats, starting at low exercise intensities, and
additional anticorrelations up to about 10 beats beyond
HR of about 175 BPM, being consistent with the DDFA
results.
The probability density of the DPACF values
for lags between 1 and 6 beats, shown in Fig. 1(f), con-
ﬁrm dominant direct anticorrelations on the shortest time
scales of 1 to 2 beats, and 4 beats for high exercise in-
tensities (here HR >∼170).
Subject M1 as the chosen example has the most promi-
nent anticorrelations and particularly simple, almost lin-
ear, trend in the HR over the whole marathon. The indi-
vidual DDFA and DPACF results, similarly to Fig. 1, for
all the subjects of group M are shown in Supplementary
Fig. S5. The results share qualitative similarities across
the subjects, as they all exhibit short-scale suppression
of correlations and the appearance of anticorrelations as
a function of the HR. However, some diﬀerences are also
apparent, as only three subjects (M1, M3, and M7) show
the shift of the anticorrelations to elevated scales at the
highest exercise intensities. Some short-scale anticorre-
lations, particularly for subject M6 and to some extent
for M4 and M5, also appear at elevated scales, but these
happen at lower intensities and are likely diﬀerent in ori-
gin. Regardless, additional research is required to deter-
mine the eﬀect of individual strains relative to standard
physiological thresholds on the results.
To further study the consistency of the results between
the diﬀerent subjects, the aggregated DDFA (top) and
DPACF (bottom) results for all members of group M are
shown in Fig. 2 as a function of both the absolute (left)
and relative (right) HR. The most notable features are
the high-intensity elevated-scale anticorrelations starting
to appear at 87% and 95% relative HR, or at the abso-
lute HR of 175 BPM (this congruence on the absolute
scale is likely to be coincidental). In these ranges also
the conventional DFA exponent α1 (black curve) drops
slightly below 1/2, but its limitations are apparent, as
it is based on linear regression over the scales of 4 to 16
beats. The anticorrelations at lower intensities (approx-
imately 155–175 BPM) appear to be more condensed on
the relative scale (roughly 78–87%, with a more concen-
trated maximum between 80–85%), which is apparent
both on the DDFA results and in the more pronounced
dip of the short-scale exponent α1. There is also a band of
short-scale suppressed correlations with a trend towards
longer scales at even lower relative HR (≈72–79%) that
is practically indistinguishable on the absolute scale. On
the relative scale, the DPACF results also show a sharper
transition into anticorrelated behavior at approximately
80% HR for lag τ = 1, whereas on the absolute scale the
transition is more gradual. These lag τ = 1 anticorrela-
tions appear consistently for all the subjects and become


## Page 3


3
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Dynamic scaling exponent (t,s)
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Dynamic PACF (t, )
101
102
103
Scale s (RRI)
(a)
(c)
120
140
160
180
Heart rate HR (BPM)
160
170
180
Heart rate HR (BPM)
1
5
10
15
20
Lag  (RRI)
(b)
2,000
4,000
6,000
8,000
10,000
12,000
Time t (s)
(d)
0.00
0.05
0.10
0.15
0.20
Density
0.00
0.04
0.08
0.12
0.16
Density
0.0
0.5
1.0
1.5
2.0
(t,s)
(e)
s=5
s=6
s=8
s=10
s=15
s=20
160
170
180
1.0
0.5
0.0
0.5
1.0
(t, )
(f)
=1
160
170
180
=2
160
170
180
=3
160
170
180
=4
160
170
180
=5
160
170
180
=6
0.0
0.5
1.0
1.5
2.0
Conventional 1
Heart rate HR (BPM)
FIG. 1.
Beat-to-beat (RR) interval correlations for the Marathon race of subject M1. Note that the upper-left and upper-right
color bars refer to (a,c) and (b,d), respectively. (a) Color-coded dynamic (DDFA-1) scaling exponent α(t, s) on diﬀerent scales
s (y-axis) as a function of binned HR (x-axis). Here α(t, s) is averaged over those dynamic segments, whose average HR falls
within 0.1 BPM wide bins. The values for empty bins are linearly interpolated if the gap does not exceed 0.5 BPM. The black
solid line shows the mean together with the standard deviation (thin lines) and the the standard error of the mean (thick
lines, barely visible) of the conventional short-scale (4–16 RRIs) scaling exponent α1. The exponent is computed in moving
windows of 50 RRIs in HR bins of 2 BPM. (b) Color-coded partial autocorrelation functions (DPACF-0) C(t, τ) with diﬀerent
lags τ (y-axis) as a function of the binned HR. (c) Similar to (a) but as a function of time during the marathon race. The
instantaneous heart rate is overlaid on the data. (d) Similar to (b) but as a function of time. The values that do not pass the
non-zero signiﬁcance test as described in the text are shown in white. (e) Probability density histogram for α(t, s) for diﬀerent
scales s as a function of the HR. (f) Probability density histogram of the DPACF-0 for diﬀerent lags τ as a function of the HR.
The histograms in (e-f) consist of 31-by-31 bins, and the probability densities are separately normalized for each HR bin, so
that they better depict the distributions as a function of the HR instead of measuring the prevalence of diﬀerent HR regions.
Furthermore, the color bar is capped at the 99.5th percentile to avoid outliers dominating the color scale.
stronger with increasing HR, and also appear at longer
lags at the regions where the DDFA anticorrelations shift
to larger scales. Naturally, the aggregated results should
be interpreted with care as they represent an average re-
sult over all the samples. Secondly, there is uncertainty
in the maximum HR values of the subjects. Neverthe-
less, the results suggest that neither the absolute nor the
relative scale is universal for diﬀerent individuals.
Freeform Training Runs
In order to study the correlations of RRIs over a wide
range of exercise durations and intensities, we perform
the same analysis for subjects in group T. It is instruc-
tive to consider ﬁrst a single exercise of one subject which
is shown in Fig. 3. It consists of six intervals of high-
intensity running, each interval lasting about 160 seconds
with the subsequent intervals reaching higher and higher
intensities. As a function of exercise time t the DDFA ex-
ponent α(s) [Fig. 3(c)] and the PACF [Fig. 3(d)] consis-


## Page 4


4
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Dynamic scaling exponent (t,s)
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Dynamic PACF (t, )
101
102
103
Scale s (RRI)
(a)
150
160
170
180
Heart rate HR (BPM)
1
5
10
Lag 
(RRI)
(b)
(c)
0.70
0.75
0.80
0.85
0.90
0.95
1.00
Relative heart rate HR/HRmax
(d)
0.0
0.5
1.0
1.5
2.0
Conventional
1
FIG. 2.
Aggregate beat-to-beat (RR) interval correlations as a function of heart rate for all subjects of group M. (a) Average
values for α(t, s) for each scale s (y-axis) and HR bin (x-axis). The solid line depicts the conventional short-range α1. (b)
Average values for C(t, τ) for each lag τ (y-axis) and HR bin (x-axis). In (a-b), the data is processed as in Fig. 1. (c-d) Similar
to (a-b) but as a function of the relative HR. In (c-d), the data is processed as in Fig. 1, but with the distinction that the
relative HR bin width is 0.001, the interpolation threshold is 0.005, and the bin width for the conventional short-scale exponent
α1 in (c) is 0.01.
tently reveal strong anticorrelations of RR intervals that
develop rapidly after the start of the intense interval. The
shortest-scale anticorrelations span to longer and longer
scales with increasing HR in the latter intervals.
The
earlier lower-intensity intervals exhibit anticorrelations at
elevated scales, separated by a band of correlations from
the shortest scale anticorrelations. This behavior was al-
ready suggested by some of the marathon data (M4, M5,
and M6), and in a following analysis we will relate these
to a distinct band of anticorrelations appearing at mod-
erate exercise intensity.
At rest between the intervals
the anticorrelations rapidly vanish. The DPACF shows
strong lag τ = 1, 2 anticorrelations, whose magnitudes
are in accordance with the short-scale DDFA anticorrela-
tions as observed in group M. The existence of patches of
anticorrelations over time lags up to 10 beats is also con-
sistently observed with the elevated-scale DDFA anticor-
relations. As a function of HR, the anticorrelated behav-
ior develops rapidly after an intensity threshold (≈175
BPM) [see Fig. 3(a)]. The elevated-scale anticorrelations
are visible as a spike of suppressed correlations at ap-
proximately 172
BPM with a weak tail towards short
scales and lower intensities. This latter phenomenon is
more visible in the DPACF data [Fig. 3(b)] as a weak
band of anticorrelations surrounded by correlated bands
at shorter and longer lags.
Next, we study the typical behavior of RRI correla-
tions when averaged over many running exercises of dif-
ferent intensity and duration, but for the same subject
to avoid eﬀects due to individual variability. The cor-
responding aggregated results from DDFA and DPACF
analysis for the subject T07 are shown in Fig. 4, repre-
senting a total running distance of 1889 km.
For this
large data set, we obtain good statistics for the aggre-
gated data and expect them to provide a reliable repre-
sentation of the typical RRI correlations as function of
the exercise intensity. Indeed, both DDFA exponent α(s)
and DPACF clearly show two distinct bands of anticor-
related RRIs [see Fig. 4(a) and (b)]. The ﬁrst band at
moderate exercise intensity (≈125–170 BPM) displays a
distinct, approximately exponential, trend in the DDFA
anticorrelations shifting to longer scales as a function of
the HR. It is plausible that the elevated scale anticorrela-
tions appearing at lower intensities in Fig. 3 and for M4,
M5, and M6 originate from this band of anticorrelations.
The corresponding band in the DPACF results is split by
a band of strong positive correlations. The latter band of
anticorrelations at high exercise intensities (>∼175 BPM)
does not show a clear trend as a function of the HR,
although there is tendency towards spanning to longer
scales with increasing intensity. Notably, the anticorre-
lations remain present even at the shortest scales and
lag. This is in contrast to some of the marathon data,
where the highest-intensity anticorrelations appear at el-
evated scales. This could be due to the diﬀerent nature
of the exercises, as in the marathon races these anticorre-
lations appear after prolonged exercise at high intensity,
and changes in, e.g., body temperature or electrolyte bal-
ance may inﬂuence the results. On the other hand, in the
discussion section we make an argument that this could
be due to interactions with the stride frequency.
The
conventional α1 indicates the suppression of correlations
that is consistent with the DDFA anticorrelations when
taking into account its limitation to the scales of 4–16
beats. The α1 is clearly insuﬃcient to capture anticor-
related behavior concentrated on thin bands of scales.
Figures 4(c) and 4(d) show the probability density plots
of α(s) and PACF values for diﬀerent scales s and lags
τ, respectively. The existence of two regions with anti-
correlated RRIs is clearly visible. They are separated by
a region with positive correlations (or α > 1/2).
The aggregated data for all the subjects of group T are


## Page 5


5
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Dynamic scaling exponent (t,s)
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Dynamic PACF (t, )
101
102
Scale s (RRI)
(a)
(c)
120
140
160
180
Heart rate HR (BPM)
130
140
150
160
170
180
Heart rate HR (BPM)
1
5
10
Lag  (RRI)
(b)
200
400
600
800
1,000
1,200
Time t (s)
(d)
0.0
0.5
1.0
1.5
2.0
Conventional 1
FIG. 3. Beat-to-beat RR interval correlations for one interval exercise from group T. (a) Dynamic scaling exponents (DDFA-1)
α(t, s) (colors) and the conventional short-range α1 (solid line) as a function of the binned HR. (b) DPACF-0 correlations
C(t, τ) as a function of the binned HR. (c-d) As in (a-b) but as a function of time, and in (c) the HR value is overlaid on the
data. For details on the data processing, see the caption of Fig. 1.
shown in Supplementary Fig. S4.
Most subjects show
common qualitative similarities in the form of two an-
ticorrelated bands as described for T07.
However, for
some subjects the split into the two anticorrelated re-
gions is not that clear; particularly there is the lack of
correlated shortest scale behavior separating these two
regions. In the absence of the correlated bands the be-
havior is remarkably simple; the higher the intensity, the
more prominent the anticorrelations are in both magni-
tude and scales covered.
In addition to individual in-
trinsic cardiac variability, a possible explanation could
be diﬀerent training practices and external conditions,
as for example T05 shows behavior that is most simi-
lar to the marathon data. Another explanation could be
highly regular running motion, which could promote cor-
relations induced by, e.g., muscle contractions and blood
pressure variations, which is an argument set forth in the
next section. It is also worth noting that T11 reported
problems with the chest strap, and as a result his data
has unusually high amount of missed beats (up to 50%).
Despite of this, two regions of suppressed correlations
are present that are consistent with the other subjects,
highlighting the robustness of the methodology.
We assessed the suitability of higher order detrending
for our analysis and decided to employ DDFA-1 due to
the following reasons: (i) The qualitative behavior re-
mains the same at the shortest scales, which is the most
interesting region for dynamic exercise intensity analysis,
(ii) the short-scale bias in DFA is larger and crossover
scales are shifted with higher order methods, (iii) higher
orders of DDFA appear to require longer dynamic seg-
ments for similar statistical accuracy and have increased
computational cost.
Finally, we point out that it is important to check the
reliability of our DDFA and DPACF methods with re-
spect to trends. Hence, we have ﬁltered the data of sub-
ject T07 according to the condition that the standard de-
viation of the HR within the dynamic segments is smaller
than the values for certain quantiles. We ﬁnd that the
observation of the bands with anticorrelations is robust
and independent of the choice of the quantile ﬁlter. In
fact, the anticorrelations appear stronger when limiting
to dynamic segments with less HR variation, as the av-
eraging is not performed over segments with transient
changes in the HR that could lead to spurious correla-
tions. The exact results of this analysis for six diﬀerent
choices of quantiles are shown in Supplementary Fig. S6.
DISCUSSION
It is important to understand the physiological mech-
anism causing the observed anticorrelations. Due to the
lack of time series for other physiological variables, we
can present below only simple arguments that we con-
sider to be potentially relevant for explaining the ob-
served dynamic correlations.
First, we point out that
there are three physiologically relevant time scales that
fall into the range over which the anticorrelations oc-
cur: (i) the stride frequency which is typically around 85
strides per leg and per minute [13], (ii) the respiration
cycle which is typically three to ﬁve heart beats long,
and (iii) arterial blood pressure ﬂuctuations, i.e., the so-
called Mayer waves, which result from an oscillation of
sympathetic vasomotor tone and is of the order of ten
seconds [14].


## Page 6


6
0.0
0.5
1.0
1.5
2.0
Dynamic scaling exponent (t,s)
1.0
0.5
0.0
0.5
1.0
Dynamic PACF (t, )
110
120
130
140
150
160
170
180
190
Heart rate HR (BPM)
101
102
103
Scale s (RRI)
(a)
110
120
130
140
150
160
170
180
190
Heart rate HR (BPM)
1
5
10
15
20
Lag  (RRI)
(b)
0.00
0.02
0.04
0.06
0.08
Density
0.00
0.03
0.06
0.09
0.12
Density
0.0
0.5
1.0
1.5
2.0
(t,s)
(c)
s=5
s=6
s=8
s=10
s=15
s=20
120 140 160 180
1.0
0.5
0.0
0.5
1.0
(t, )
(d)
=1
120 140 160 180
=2
120 140 160 180
=3
120 140 160 180
=4
120 140 160 180
=5
120 140 160 180
=6
0.0
0.5
1.0
1.5
2.0
Conventional 1
Heart rate HR (BPM)
FIG. 4. Aggregate beat-to-beat (RR) interval correlations for all the exercises of one subject (T07) in group T. (a) Average
values for α(t, s) for each scale s (y-axis) and binned HR (x-axis). The solid line shows the conventional short-range α1. (b)
Average values for C(t, τ) for each lag τ (y-axis) and binned HR (x-axis). (c) Probability density histogram for α(t, s) for
diﬀerent scales s as a function of the HR. (d) Probability density histogram for C(t, τ) for diﬀerent lags τ as a function of the
HR. Note that the probability densities are separately normalized for each HR bin. For details on data processing, please see
the caption of Fig. 1.
All three processes are cyclic and hence can induce
periodic modulations to the heart rate through hemody-
namics. Such periodicities could result in anticorrelated
RRIs when observed at scales similar to the period mea-
sured in heart beats. Furthermore, the overall heart rate
variability is reduced under exercise due to withdrawal
of cardiac vagal tone and parasympathetic control[2–4],
i.e., the local short-term RRIs are more regular with-
out 1/f- or Brownian-like diﬀusion for extended peri-
ods of time. Therefore, subtler patterns should become
more discernible, as they are not masked by the complex
ﬂuctuations of a healthy heart under resting conditions.
Similarly, the relative magnitudes of the modulating sig-
nals could aﬀect the scale-dependence of the anticorre-
lations. If some of the eﬀects is much stronger, it will
mask higher frequency periodicities as they will appear
correlated when superimposed on the stronger lower fre-
quency oscillations. Additionally, when a periodic signal
is sampled at discrete intervals, the result is a new signal
whose period depends on the sampling frequency. This
eﬀect is manifested, e.g., when the inﬂuence of the blood
pressure variations due to the stride frequency is sampled
at each heart beat.
This latter phenomenon could explain some of the
qualitative diﬀerences in the dynamic correlations be-
tween the subjects. For some subjects (particularly T08,
but also T02, T03, T10, and T12) the RRIs show clearly
deﬁned behavior under exercise, becoming short-scale an-
ticorrelated at moderate intensity, with the magnitude
and the scale of the anticorrelations increasing in con-
junction with intensity. In contrast other subjects exhibit
more complex RRI-correlations where the simple anticor-
relations are interrupted by bands of decreased or altered
correlations at shorter scales (please see Supplementary
Figs. S4 and S5 for the individual RRI-correlation plots
as a function of the HR). These more correlated bands ap-
pear at heart rates corresponding to sampling frequencies
where typical stride frequencies would look correlated at
the shortest scales. If these bands arise from the stride
frequency, that could also explain the better congruence
on the absolute HR scale in Fig. 2, as there is generally
less variance in the stride frequencies than in the maxi-


## Page 7


7
mum heart rates.
These
considerations
would
imply
that
the
(anti)correlations
arise
from
underlying
universal
cardiolocomotor mechanisms, but detailed response to
exercise may depend on individual physiology, biome-
chanics of running and training status [6]. Furthermore,
the onset of the anticorrelations, their strength, and
scales of appearance show individual variability. Study-
ing the relationship of these variables to standardized
thresholds and markers in exercise physiology could
allow utilizing the dynamic correlations for monitoring
the exercise intensity in real-time without the knowledge
of parameters such as the maximal oxygen uptake
(VO2max) or maximum heart rate.
We are aware of
the possibility that the universal emergence of anticor-
relations at elevated heart rates is most likely aﬀected
by other physiological factors beyond the ones discussed
here.
Clearly, further research is required, but the
approach herein provides a promising avenue forward.
CONCLUSIONS
Our main result is the discovery of multiscale anticor-
relations in RR intervals during running exercises under
real-world conditions.
The anticorrelations have a dy-
namical structure that depends on the exercise intensity
as measured by the heart rate. The characteristics of the
dynamical structure are revealed by our methodology,
in particular the dynamic detrended ﬂuctuation analysis
and dynamic partial autocorrelation functions, which we
anticipate becoming useful tools in data analysis across
various disciplines. While we have demonstrated the ca-
pability to study the dynamical RRI correlations dur-
ing varying real-world circumstances, a more systematic
evaluation of the methodology is required to control for
exercise conditions.
The observed anticorrelations appear on short scales
(a few beats) at low to moderate exercise intensities. As
the intensity is increased, the anticorrelations increase
in magnitude and span to longer scales (up to 20–30
beats). This simpliﬁed picture is complicated by correla-
tions arising potentially from interactions with the regu-
lar running motion when the stride frequency is appropri-
ately proportional to the heart beat. These correlations
mask the anticorrelated behavior on bands of increas-
ing or decreasing scales at moderate and high exercise
intensities, respectively. At rest, e.g., between running
intervals, the anticorrelations rapidly vanish, and appear
immediately when the intensity is increased again. These
changes happen before the HR saturates at the level nec-
essary to maintain the ongoing exercise intensity. Hence,
our ﬁndings allude the possibility of quantifying the rel-
ative exercise intensity by measuring the dynamic corre-
lation exponent α(t, s) in real time during exercise.
This report of our initial ﬁndings serves as a prelude
for highlighting the potential of the dynamic correlation
analysis so that further advances could be pursued. It
is highly desirable to develop a theoretical model for the
complex dynamics of the cardiovascular feedback loops
during high-intensity exercise load that can explain the
observed time scales for the anticorrelated RR intervals.
Clearly, a more systematic study with subjects perform-
ing speciﬁc exercise protocol should be performed to ver-
ify our observations. Besides, a thorough validation and
calibration of our results with data collected during run-
ning exercise in a physiology laboratory is a natural next
step for our study to relate the changes in the dynamic
correlations to standard exercise physiology models. The
inclusion of accelerometer data, from which the stride
frequencies could be derived, would facilitate the veriﬁ-
cation of the running modalities as a possible cause for
the bands of correlations present for some subjects.
Such controlled and systematic studies are not only
necessary to elucidate the speculative nature of the re-
sults herein, but they are further motivated by poten-
tially enabling the application of this methodology in ex-
ercise physiology. We expect that the reported RR in-
terval correlations are suitable to represent a dynamical
“ﬁngerprint” of the exercise-induced cardiovascular load.
Hence, our methodology – which could be integrated with
the present devices on the market – has a potential to be-
come a new tool in real-time exercise monitoring without
previous knowledge of maximal thresholds such as the
maximum hearth rate and lactate or ventilatory thresh-
olds.
MATERIALS AND METHODS
Heart Rate Data during Exercise
We study real-time correlations of RRIs during exer-
cises of various intensities. All heart rate data for this
study have been collected during regular running train-
ing and racing under real-world conditions, i.e., outside
the laboratory. Two groups of data were used for our the-
oretical analysis. The ﬁrst group of data was recorded by
human volunteers during their regular running training
with freely chosen intensity and volume (group T). The
study period was at least 4 weeks, and some subjects
provided data over a longer period of time. We obtained
institutional approval and informed consent (COUHES
exemption for the employed protocol has been granted
under protocol no. 1711132002). The research was per-
formed in accordance with the rules and regulations set
by the participating universities. This group involved 12
volunteers (5 female, 7 male, with an age span from 27
to 65 years). Their performances span a wide range from
top national level to recreational runners: the personal
bests in 10 km range from 29 min 31 sec to 44 min 57
sec, in marathon from 2 hours 43 min 20 sec to 4 hours
26 min 3 sec.
During exercises, heart rate (HR), RR intervals (RRI),
running velocity and distance were recorded using a
Garmin heart rate monitor HRM4-Run and a GPS watch


## Page 8


8
(Forerunner 935, Garmin Inc., Olathe, KS, USA). A pre-
vious study has investigated and validated the accuracy
of this HRM [15]. The data were recorded by the GPS
watch in the Flexible and Interoperable Data Transfer
(FIT) format [16] and subsequently uploaded by the sub-
jects to a web service that we had launched for this study.
The total number of exercise ﬁles analyzed per subject
(samples) varied between 18 and 261, with total covered
distances from 150 to 1889 km.
The second group of data was obtained by selecting
randomly the marathon races of 7 subjects from data
uploaded to the Polar Flow web service[17] (group M).
Within registration to Polar Flow, the subjects have
given their consent for the use of their data for research
purposes. The metadata were provided by the users of
this web service (all male, with an age span from 28 to 53
years, and marathon ﬁnishing times between 3 hours 30
min and 4 hours 17 min). HR and RRIs were recorded
for this group of subjects with a Polar heart rate monitor
H10 and a Pro Strap (Polar Electro Oy, Kempele, Fin-
land). Recently, the RR signal quality of this HRM has
been shown to be excellent from low- to high-intensity
activities in comparison to a ECG Holter device [18].
In both groups T and M, the subjects provided their
maximum and resting heart rates. Summaries of all the
metadata for the two groups are shown in Supplementary
Table S1.
As ECG data is not available, we do not attempt to
remove ectopic beats or other artifacts based on physi-
ological criteria. Therefore we merely remove technical
artifacts, such as missed beats, that can be isolated with
reasonable certainty. The details for this data prepro-
cessing are provided in Supplementary Appendix A.
Conventional Methods
For comparison we apply ordinary detrended ﬂuctua-
tion analysis [9, 11] to the RRI time series. By comput-
ing the root-mean-squared ﬂuctuations F(s) around local
trends at multiple scales s, the method assesses power law
scaling relations F(s) ∝sα characterized by the scaling
exponent α. In the context of HRV, typically two expo-
nents are determined, for short- (α1) and long-scale (α2)
correlations, respectively [10, 12]. We extract the conven-
tional short-scale (4–16 RRIs) scaling exponents α1 [10]
in segments consisting of 50 RRIs. We compute the ﬂuc-
tuation functions in maximally overlapping windows for
enhanced statistical properties [19]. A summary of the
DFA method is provided in Supplementary Appendix B.
We also provide a helpful summary of partial autocor-
relation functions in Supplementary Appendix C before
introducing their dynamic counterparts here.
Dynamic Segmentation
The dynamic behavior of the time series can be studied
by performing the analysis in moving temporal segments.
However, to guarantee suﬃcient statistical accuracy, the
length of these segments is dictated by the largest scale s
(DFA) or the lag τ (PACF), resulting in diminished tem-
poral resolution for small scales. Therefore, we propose
a dynamic segmentation procedure, where the segment
length is varied as a function of the scale or the lag:
1. Choose a function for determining the segment
lengths ℓ(s) as a function of the scale s. Here we
adopt a simple linear relationship ℓ(s) = as where
a is a constant. Smaller values increase the tem-
poral resolution but also the statistical noise. The
dynamic length factor a itself may also be varied
for diﬀerent scales.
2. For each scale divide the time series into segments
of length ℓ(s). The segments themselves may be
overlapping if desired for smoother results. Identify
the segments Ss,t by their temporal indices t, which
may be, e.g., the mean time within the segment or
any other suitable quantity.
Dynamic Detrended Fluctuation Analysis (DDFA)
The dynamic segmentation together with the maxi-
mally overlapping windows in the DFA scheme enables
the following procedure for dynamic DFA (DDFA):
1. Perform the dynamic segmentation for each scale
s. The value of a = 5 was found to be an accept-
able value for the dynamic length factor, which is
employed in all of our DDFA calculations.
2. Utilizing overlapping windows, compute the ﬂuc-
tuation function in each segment Ss,t at scales
{s −1, s, s + 1}. Denote the logarithmic ﬂuctua-
tion function at these scales by ˜Ft(s−1), ˜Ft(s) and
˜Ft(s + 1), respectively.
3. In each segment, compute the dynamic scaling ex-
ponent α(t, s) by the ﬁnite diﬀerence approxima-
tion [20]
α(t, s) ≈

h2
−˜Ft(s + 1) +
 h2
+ −h2
−
 ˜Ft(s)
−h2
+ ˜Ft(s −1)

/

h−h+ (h+ + h−)

,
(1)
where h−
=
log(s) −log(s −1) and h+
=
log(s + 1) −log(s) are the logarithmic backward
and forward diﬀerences.
Fluctuation functions
computed with maximally overlapping windows are
empirically found to be smooth enough to per-
mit the direct application of the ﬁnite diﬀerence
scheme.


## Page 9


9
The performance of the method is numerically vali-
dated by applying it to simulated time series with known
properties. Supplementary Appendix D explains the de-
tails for analytically obtaining the theoretically expected
scale-dependency of DFA scaling exponents for diﬀerent
processes. In Supplementary Appendix E these theoreti-
cal results are utilized for conﬁrming the acceptable per-
formance of the DDFA method.
Dynamic Partial Autocorrelation Function (DPACF)
In order to obtain a local estimate of the partial au-
tocorrelation function C(τ) we compute it using an ap-
proach similar to that of the DDFA algorithm. The steps
of this approach can be summarized as follows:
1. Perform dynamic segmentation for each lag τ. The
value of a = 10 was found to be an acceptable value
for the dynamic length factor, which is utilized in
all of our DPACF calculations.
2. In each segment Sτ,t, perform polynomial detrend-
ing of order m.
3. For each segment, compute C(τ) by, for exam-
ple, solving the Yule-Walkers equations with the
Levinson-Durbin recursive scheme [21].
Choose
each time for the maximum lag the parameter for
which we are estimating the partial autocorrelation
function. Denote this dynamic PACF by C(t, τ).
Resorting to the central limit theorem, it is a known
result that the partial autocorrelation function is approx-
imately non-zero at 5% signiﬁcance level if |C(t, τ)| <
1.96/
p
ℓ(τ). The evaluation of this signiﬁcance band is
statistically valid only if ℓ(τ) >∼30 and therefore if τ > 3
for a = 10.
Notice that in DPACF the detrending is applied to the
original time series in contrast to the integrated series
in DDFA. Therefore, the results would be expected to
be qualitatively similar when the DPACF detrending or-
der is one smaller than the DDFA detrending order n.
This explanation is complicated by, e.g., the removal of
linear correlations in PACF. However, the relationship
m ≈n −1 is supported by empirical observations.
While both DDFA and DPACF measure dynamic cor-
relations, it is important to realize the qualitative dif-
ference between them.
DDFA describes the collective
behavior of all beats over the scale s, whereas DPACF
considers the average behavior of individual beats sepa-
rated by the lag τ (with the linear dependence from the
preceding lags removed)
ACKNOWLEDGMENTS
We acknowledge insightful discussions with Ary Gold-
berger.
We also thank Jyrki Schroderus, Laura Kar-
avirta, Jussi Peltonen and Arto Hautala for all the
support and suggestions.
The authors acknowledge
Polar Electro Oy (Oulu, Finland) for providing exer-
cise data and CSC – IT Center for Science, Finland,
for computational resources.
Additional support was
provided by an EMERGENCE grant of CNRS, INP,
and the ICoME2 Labex (ANR-11-LABX-0053) and the
A*MIDEX projects (ANR-11-IDEX-0001-02) funded by
the French program “Investissements d’Avenir” managed
by ANR.
Appendix A: Dataset details and preprocessing
We study two datasets of running exercises and races
under real-world conditions. These consist of voluntary
running exercises at freely chosen intensities and sched-
ules (group T) and marathon races (group M). Metadata
for these datasets are presented in Supplementary Table
S1.
Artifacts in the data are removed prior to the analysis
by utilizing the following scheme:
1. RR intervals below or above the threshold values
RRmin and RRmax are removed.
2. Compute the local median of the RR intervals
RRmed(t) in a moving window of length lmed.
3. Remove RR intervals that fall outside the range
(1 ± cmed)RRmed(t), where the threshold cmed is a
constant.
The values for the ﬁltering parameters are listed in Sup-
plementary Table S2. Acceptable performance of the ﬁl-
ter is manually inspected for all the samples in group M
and a representative subset of 17 samples from the group
T. The ﬁlter is particularly adept at removing too long
intervals arising from missed beats, which is the most
common error in exercise data [22]. As ECG data is not
available, we do not attempt to ﬁlter the data based on
physiological criteria, and merely remove technical arti-
facts that can be isolated with reasonable certainty.
Appendix B: Detrended Fluctuation Analysis (DFA)
Ever since its introduction in the study of correla-
tions in DNA sequences [9], DFA for time series has
been widely employed across multiple disciplines such as
physics [23, 24], medicine [1, 10, 25], ﬁnance [26], and
even music [27, 28]. The DFA method has been exten-
sively studied [11, 29–36] and it has been expanded to
account for eﬀects such as multifractality [37] and cross-
correlations [38].
We brieﬂy summarize the conventional DFA algorithm
which has been developed to detect correlations in non-
stationary time series [9, 10]. First, for a time series X(j)


## Page 10


10
Supplementary Table S1. Summary of the metadata for the two groups of subjects: Training runs of various durations and
intensities (T) and marathon races (M). For group T shown are the age, gender, resting heart rate HRrest and maximum heart
rate HRmax (as reported by the subject), the personal best (PB) time for 10 km and marathon (time in hh:mm:ss) within 3
years before this study, the number of exercise samples analyzed, the average heart rate HRavg of all samples, and the total
distance and duration of all samples. For group M all subjects were male, and shown are their age, resting heart rate HRrest
and maximum heart rate HRmax (as reported by the subject), marathon ﬁnishing time, and average heart rate HRavg during
the marathon.
Group T
subject age [y] gender HRrest HRmax PB 10 km PB Marath. samples HRavg distance [km] duration [h]
T01
48
m
40
192
00:36:49
02:50:49
186
151
1527
121.5
T02
27
m
40
193
00:29:31
–
54
130
576
43.5
T03
29
f
43
200
00:36:50
02:47:56
20
155
170
13.7
T04
29
f
50
205
00:42:30
–
103
167
1076
92.8
T05
39
f
–
200
00:44:57
03:40:09
15
176
150
11.7
T06
–
m
40
192
00:35:22
02:43:25
26
153
666
49.3
T07
33
m
42
214
00:33:56
02:43:20
261
154
1889
138.7
T08
37
f
43
200
–
04:26:03
20
149
209
22.1
T09
27
m
48
195
00:31:32
–
21
143
199
16.7
T10
37
f
45
179
–
–
18
154
215
18.1
T11
65
m
47
170
00:43:10
03:13:29
26
134
287
28.2
T12
47
m
48
182
–
03:09:49
53
129
1133
95.4
Group M
subject age [y] HRrest HRmax Finishing time [hh:mm:ss] HRavg
M1
53
56
185
03:40:09
172
M2
50
46
174
03:36:47
149
M3
28
58
198
04:17:04
171
M4
34
50
195
04:12:36
155
M5
43
55
200
03:49:03
162
M6
39
55
194
04:19:36
155
M7
50
50
200
03:30:33
174
Supplementary Table S2. Data ﬁltering parameters.
Group RRmin (ms) RRmax (ms) lmed (beats) cmed
M
250
600
15
0.026
T
250
1000
11
0.03
of length N a cumulative summation is performed,
Y (k) =
k
X
j=1
(X(j) −⟨X⟩) ,
(B1)
where the mean ⟨X⟩of the time series is subtracted, but
that is not strictly necessary for DFA [11]. Convention-
ally, the integrated time series of (B1) is divided into
non-overlapping windows of length s. In each window w,
a local trend is determined as the least-squares ﬁt of a
low order polynomial ps,w(k) to the data. (The method
is denoted by DFA-n if the degree of the detrending poly-
nomial is n [11].) The ﬂuctuations are measured as the
variance from the local trend ps,w(k) in each window:
F 2
s,w = 1
s
P
k∈w (Y (k) −ps,w(k))2. These squared ﬂuctu-
ations are averaged over the windows to yield the ﬂuctu-
ation function
F(s) =

F 2
s,w
1/2.
(B2)
Allowing the windows to overlap enhances the statistical
properties of this estimate [19]. When this procedure is
repeated for diﬀerent window sizes, or scales s, a power-
law increase of the ﬂuctuations with the window size may
be observed, i.e., F(s) ∼sα. Here α is a scaling exponent
that can be considered as a generalization of the Hurst
exponent H [39]. See Supplementary Appendix E below
for more details.
However, experimental time series rarely exhibit exact
scaling over several scales. Many previous studies have
focused on ﬁnding a robust determination of the scaling
regimes [40, 41], or on extracting a spectra of scaling ex-
ponents α(s) [42–46]. These methods are based on the
notion that the spectra may be deﬁned as the local slope
of the logarithmic ﬂuctuation function,
α(s) = d [log F(s)]
d [log s]
.
(B3)
In the context of HRV, these methods generalize and ex-
pand the conventional division into short (4–16 beats)
and long-range (16–64 beats) scaling exponents. In prac-
tice, the behavior may also change over time, either due
to external inﬂuences, or the process itself may comprise
several distinct intrinsic modes. This paper develops a
methodology that takes these temporal variations into
account in a consistent manner.
Depending on the value of the exponent α, diﬀerent
degrees of correlations of the time series or its increments


## Page 11


11
Supplementary Table S3. Meaning of values of the DFA scal-
ing exponent α. The qualitative interpretation remains the
same for even higher exponents that become discernible with
higher-order DFA: For each integral interval the lower and
upper halves correspond to originally anticorrelated or corre-
lated increments, respectively.
Scaling exponent
Interpretation
Stationarity
0 < α < 1/2
anti-correlated
stationary
α = 1/2
white noise
1/2 < α < 1
correlated
α = 1
1/f (pink) noise
1 < α < 11/2
anti-correlated increments
non-stationary,
stationary
increments
α = 11/2
Brownian noise
11/2 < α < 2
correlated increments
can be identiﬁed. The meaning of the diﬀerent ranges for
α are summarized in Supplementary Table S3.
The scaling exponent α is related to other scaling ex-
ponents in time series analysis. Scale invariance is also
observed in the Fourier domain as a function of the fre-
quency f with a power spectral density that scales in the
low frequency limit as P(f) ∼f −β. The exponent β is
related to the DFA exponent by the scaling relation β =
2α−1 [31, 32]. In exercise physiology, the power spectrum
of heart rate time series is a frequently employed tool to
quantify the cardiological response to exercise. However,
analyses in the frequency domain are potentially plagued
by non-stationarity. For stationary signals, the autocor-
relation function C(τ) = ⟨X(τ0)X(τ0 + τ)⟩decays for
long lags τ with a power law ∼τ −γ. Then the scaling
relation γ = 2 −2α holds [33]. For more details on the
DFA method and its relation to correlation functions, see
Supplementary Appendix D.
Appendix C: Partial Autocorrelation Function
(PACF)
It is instructive to supplement DFA analyses by a di-
rect study of correlations at diﬀerent time scales by com-
puting the autocorrelation function C(τ) and the par-
tial autocorrelation function C(τ) at lag τ. The latter
has been successfully used to identify the best autore-
gressive (AR) process to ﬁt a time series, using the fact
that C(τ) = 0 for all τ > p for an AR model of order
p [47]. The autocorrelation function C(τ) is dominated
by trends in the data, suggesting apparent correlations.
On the contrary, C(τ) is less aﬀected by trends due to
the subtraction of the linear dependence on intermediate
lags from the autocorrelation function. If the time series
contains oscillations, C(τ) shows a periodic pattern with
a frequency that modulates the data. On the contrary,
C(τ) shows anticorrelations. The lags τ for which C(τ)
assumes negative values can be related to the periodic-
ity of the oscillations. More speciﬁcally, for a time series
X(τ) the partial autocorrelation function is given by
C(τ) =
D
[X(τ0) −ˆXτ0τ(τ0)][X(τ0 + τ) −ˆXτ0τ(τ0 + τ)]
E
(C1)
where ˆXτ0τ(τ ′) is the best linear predictor, determined
by
ˆXτ0τ(τ ′) = c0 +
τ−1
X
i=1
ciX(τ0 + i) ,
(C2)
where the coeﬃcients ci are determined by the conditions
c0 +
τ−1
X
i=1
ci ⟨X(τ0 + i)⟩= ⟨X(τ ′)⟩,
(C3)
c0 ⟨X(j)⟩+
τ−1
X
i=1
ci ⟨X(τ0 + i)X(j)⟩= ⟨X(τ ′)X(j)⟩
(C4)
for j = τ0 + 1, . . . , τ0 + τ −1. The function C(τ) can
be computed practically from the Yule-Walker equations
[47]. The relation between the AR ﬁts and C(τ) is useful
in the performed analysis.
Indeed, it has been shown
that a signal with non-trivial periodic behavior can be,
for short time scales, successfully ﬁtted by an AR process,
and its dominant frequency of oscillation can be extracted
from the estimated coeﬃcients. These ﬁndings have been
also conﬁrmed by DFA [48].
Appendix D: Additional remarks on DFA for the
validation of DDFA
In this section we provide some known theoretical re-
sults for the conventional DFA algorithm to support
the validation procedure presented in the following sec-
tion. In DFA, the range of detectable exponents is de-
termined by the degree of detrending, n, and is given
by 0 ≤α ≤n + 1 [32]. While the existence of values
α > 1 may be criticized as a failure of the detrend-
ing procedure [49], they may also be understood as an
advantage of the method for allowing meaningful quan-
tiﬁcation of non-stationary processes [35, 36]. The de-
trending may be considered successful if it achieves the
statistical equivalence over the DFA windows, so that
the ﬂuctuation function F(s) does not depend on the
window [35, 36].
This condition is fulﬁlled for DFA-
n with time series exhibiting polynomial trends of de-
gree n −1.
In general, for two uncorrelated signals
XA(t), XB(t) (random processes or trends), a superposi-
tion principle holds, stating that the squared ﬂuctuation
function of the sum XA+B(t) = XA(t) + XB(t) is given
by F 2
A+B(s) = F 2
A(s) + F 2
B(s) [29].
For stationary processes and for non-stationary pro-
cesses with stationary increments the ﬂuctuation func-
tion Fs does not depend on the window and may be an-
alytically computed [33, 34]. Its squared value is deter-
mined as the weighted sum of the autocovariance function


## Page 12


12
ˆC(τ) = ⟨X(τ0)X(τ0 + τ)⟩−⟨X⟩2 in the former case, and
that of the variogram S(τ) =
D
[X(τ0 + τ) −X(τ0)]2E
in
the latter case,
F 2
s =
s−1
X
j=−s+1
G(j, s) ˆC(j)
(D1)
F 2
s = −
s−1
X
j=1
G(j, s)S(j)
(D2)
with the weight function G(j, s) given by [50]
G(j, s) = 1
s
s−|j|
X
k=1
ak,k+|j|,
(D3)
where ak,k′ are the elements of the matrix
A = D⊤h
I −B⊤ BB⊤−1 B
i
D,
(D4)
where the elements di,j of the matrix D are unity if i ≥j
and zero otherwise [33, 34]. The eﬀect of detrending is
incorporated into the so-called design matrix B of least
squares regression, which for DFA-1 is given by [34]
B =

1 1 · · · 1
1 2 · · · s

.
(D5)
This matrix A describes an operator for constructing the
squared ﬂuctuations F 2
s = X⊤
s,wAXs,w from the values
of the time series Xs,w in window w at the scale s [34].
The autocovariance function for fractional Gaussian
noise (fGn) and the variogram for fractional Brownian
motion (fBm) with Hurst parameter H are known to be
ˆCfGn
H (τ) = σ2
2

|τ + 1|2H −2|τ|2H + |τ −1|2H
, (D6)
SfBm
H
(τ) = σ2|τ|2H,
(D7)
where σ2 corresponds to the variance of ordinary Gaus-
sian noise [51].
From these correlations and by using
Eqs. D1 and D2, the theoretical ﬂuctuation function may
be computed for these processes. The spectrum of the
scaling exponent α(s) is then obtained from (B3). These
theoretical results may be utilized for studying the be-
havior of the DFA method as a function of the scale s.
For example, the deviation between the DFA estimate
for α(s) and the asymptotic large scale exponent α is
visualized in Supplementary Fig. S1 for fGn and fBm.
The well-known overestimation of the scaling exponent
at the shortest scales is clearly visible, and it is most
pronounced in the anticorrelated region with α < 1/2.
Around the asymptotic value of α = 1 there is an abrupt
qualitative change as the scaling exponent is suddenly
underestimated for an extended range of scales. This has
been observed previously [34].
In general, the short scale behavior depends on the
details of the underlying process, and hence can be dif-
ferent for other processes such as an autoregressive model
101
102
103
Scale s
0.0
0.5
1.0
1.5
2.0
Asymptotic  of fGn and fBm
-0.5
-0.2
-0.1
-0.05
-0.02
-0.01
0.01
0.02
0.05
0.1
0.2
0.5
Deviation from asymptotic 
Supplementary Figure S1. Theoretical deviation of the DFA
estimate α(s) from asymptotic scaling exponent α for fGn
and fBm as a function of the scale s. The deviation is deﬁned
as the theoretical scale-dependent exponent α(s) minus the
asymptotic scaling exponent α. Note the quasi-logarithmic
scale for the deviation.
AR(p). For more details on the scale dependence of the
deviation between asymptotic α and α(s), please see also
Ref. [52].
Appendix E: Numerical Validation of DDFA
Fractional Brownian motion (fBm) and its increments,
fractional Gaussian noise (fGn), are commonly utilized
for benchmarking DFA (see, e.g., Ref. [53] and references
therein). These processes are characterized by the Hurst
parameter 0 ≤H < 1, and exhibit long-range correla-
tions with the asymptotic (large-scale) scaling exponents
α = H for fGn and α = H+1 for fBm [34, 51]. Deviations
from the asymptotic behavior occur at shorter scales due
to the ﬁnite length of the samples and the intrinsic bias
in DFA due to the detrending. It is, however, possible
to compute the exact theoretical scale-dependent scaling
exponent α(s) for these processes, as described in Sup-
plementary Appendix D.
We validate the dynamic DFA (DDFA) method by ap-
plying it to simulated fGn and fBm, and comparing the
results to the theoretically expected values. We utilize
the Davies–Harte method, which is an eﬃcient method
for simulating these processes with their exact covariance
structure [54][55]. We generate 103 samples of fGn and
fBm of length 105 for each value of the Hurst parame-
ter H.
From these simulated time series, we compute
the dynamic scaling exponent α(t, s) in non-overlapping
dynamic segments with various dynamic segment length
factors a. The mean diﬀerence between the DDFA expo-
nent α(t, s) and the theoretically expected DFA exponent
α(s) is illustrated in Supplementary Fig. S2. The general
trend is that the limited sample size results in underesti-
mation of the scaling exponents: the shorter the dynamic
segments, the greater the bias. Similarly, processes with


## Page 13


13
-0.125
-0.1
-0.075
-0.05
-0.025
0.025
0.05
Bias relative to theoretical (s)
10
5
20 40
0.0
0.5
1.0
1.5
2.0
Asymptotic  of fGn and fBm
(a)
10
5
20 40
(b)
10
5
20 40
(c)
10
5
20 40
(d)
Scale s
Supplementary Figure S2.
Bias of the dynamic detrended
ﬂuctuation analysis (DDFA) estimate of α(t, s) relative to
its theoretically expected value for fractional Gaussian noise
(fGn) and fractional Brownian motion (fBm). Characterized
by the Hurst parameter 0 ≤H < 1, the asymptotic α for
these processes is α = H and α = H + 1 respectively. Details
for computing the theoretical scale-dependent DFA exponent
α(s) are provided in Supplementary Appendix D. The bias
is deﬁned as the observed α(t, s) minus its theoretically ex-
pected value α(s). The dynamic segment length factors a are
4, 5, 7, and 10 in (a-d), respectively.
larger asymptotic α suﬀer from larger bias, with a weak
discontinuity at α = 1 (when the process changes from
fGn to fBm). This tendency can be understood as aris-
ing from the increased abundance and length of streaks
in more correlated time series. This eﬀect is not fully
captured by the relatively short segments. However, for
the shortest scales (5 and 6), particularly in the anti-
correlated region, the exponent is slightly overestimated
instead. We also observe that the contour lines for the
bias in α(t, s) have nearly converged to a constant value
of the asymptotic α already at the scale s = 40.
The standard deviation of the DDFA estimation of the
exponent α is shown in Supplementary Fig. S3 for seg-
ment lengths 4, 5, 7, and 10 in (a-d), respectively. The
deviation consistently decreases with the increasing seg-
ment length. On the other hand, the deviation reduced
as the DFA-1 exponents approach the limits α = 0 and
α = 2, since at these boundaries there is less room for
variations. In particular, as α is reduced from 1/2 to-
wards zero (corresponding to the anticorrelated regime)
the deviations are strongly reduced. The local reduction
in the deviation just above α = 1 is due to the most anti-
correlated increments in this regime (see Supplementary
Table S3).
Generally, the bias and the standard deviation of the
DDFA method are found to be acceptable for our pur-
poses, especially in view of the fact that we have par-
ticular interest in the anticorrelated region as underlined
below in the results. All our DDFA computations are per-
formed with the dynamic segment length factor a = 5.
This was found to be a good compromise between the
0.05
0.1
0.15
0.2
0.25
Standard deviation of (t,s)
10
5
20 40
0.0
0.5
1.0
1.5
2.0
Asymptotic  of fGn and fBm
(a)
10
5
20 40
(b)
10
5
20 40
(c)
10
5
20 40
(d)
Scale s
Supplementary Figure S3.
Standard deviation of the dy-
namic detrended ﬂuctuation analysis (DDFA) estimate of
α(t, s) for fGn and fBm as a function of the scale s. Charac-
terized by the Hurst parameter 0 ≤H < 1, the asymptotic α
for these processes is α = H and α = H + 1 respectively. The
dynamic segment length factors a are 4, 5, 7, and 10 in (a-d),
respectively.
accuracy of the DDFA method and the dynamical reso-
lution requiring a suﬃciently small segment size.
Appendix F: Additional Heartbeat Correlation Plots
Here we present beat-to-beat (RR) interval (RRI) cor-
relations for all the subjects in the study. In Supplemen-
tary Fig. S4 we illustrate the average RRI correlation
results as a function of the heart rate aggregated over all
the runs for each subject of Group T. The relative heart
rate is utilized to better facilitate the comparison be-
tween diﬀerent individuals. Similar correlation plots for
the marathons of Group M are shown in Supplementary
Fig. S5, along with the correlation landscapes as a func-
tion of time during the marathon races. Additionally, we
establish the consistency of the anticorrelated bands in
the presence of possible trends in Supplementary Fig. S6.
We demonstrate this by limiting the analysis to subsets of
data where the heart rate within the dynamic segments
exhibits subsequently lower and lower standard devia-
tion. The analysis is performed for subject T07, who has
the most data.
Each correlation plot consists of pairs of color-coded
DDFA (upper panels) and DPACF (lower panels) results.
Plots as a function of the heart rate (HR) are based on
data that is averaged of dynamic segments whose average
HR falls within bins with widths of 0.1 BPM or 0.001 for
the absolute and relative HR, respectively. The values
for empty bins are linearly interpolated if the gap does
not exceed 0.5 BPM (absolute) or 0.005 (relative). The
DDFA plots (as a function of the HR) also display the
conventional short-scale (4–16 RRIs) scaling exponents
α1 by a semi-transparent black line with error bars (thin
bars: standard deviation, thick bars: standard error of


## Page 14


14
the mean, barely visible). The exponent is computed in
moving windows of 50 RRIs in HR bins of 2 BPM (abso-
lute) or 0.01 (relative). The DDFA plots displaying the
correlation landscapes for single runs show the instanta-
neous HR with the semi-transparent black line instead,
and in the corresponding single run DPACF plots the
values that do not pass the non-zero signiﬁcance test are
shown in white.


## Page 15


15
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Dynamic scaling exponent (t,s)
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Dynamic PACF (t, )
101
102
103
Scale s (RRI)
T01
1
5
10
Lag 
(RRI)
T02
0.0
0.5
1.0
1.5
2.0
Conventional
1
101
102
103
Scale s (RRI)
T03
1
5
10
Lag 
(RRI)
T04
0.0
0.5
1.0
1.5
2.0
Conventional
1
101
102
103
Scale s (RRI)
T05
1
5
10
Lag 
(RRI)
T06
0.0
0.5
1.0
1.5
2.0
Conventional
1
101
102
103
Scale s (RRI)
T07
1
5
10
Lag 
(RRI)
T08
0.0
0.5
1.0
1.5
2.0
Conventional
1
101
102
103
Scale s (RRI)
T09
1
5
10
Lag 
(RRI)
T10
0.0
0.5
1.0
1.5
2.0
Conventional
1
101
102
103
Scale s (RRI)
T11
90
100
110
120
130
140
150
160
170
180
190
Heart rate HR (BPM)
1
5
10
Lag 
(RRI)
T12
90
100
110
120
130
140
150
160
170
180
190
Heart rate HR (BPM)
0.0
0.5
1.0
1.5
2.0
Conventional
1
Supplementary Figure S4. Aggregate RRI correlation results for each subject of Group T. For each subject the average DDFA-1
scaling exponents α(t, s) (upper panels) and DPACF-0 correlations C(t, τ) (lower panels) as a function of binned relative heart
rate. For a detailed explanation about how the data is computed, please see Supplementary Appendix F.


## Page 16


16
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Dynamic scaling exponent (t,s)
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Dynamic PACF (t, )
101
102
103
Scale s (RRI)
M01
120
140
160
180
200
Heart rate HR (BPM)
1
5
10
Lag 
(RRI)
0.0
0.5
1.0
1.5
2.0
Conventional 1
101
102
103
Scale s (RRI)
M02
120
140
160
180
200
Heart rate HR (BPM)
1
5
10
Lag 
(RRI)
0.0
0.5
1.0
1.5
2.0
Conventional 1
101
102
103
Scale s (RRI)
M03
120
140
160
180
200
Heart rate HR (BPM)
1
5
10
Lag 
(RRI)
0.0
0.5
1.0
1.5
2.0
Conventional 1
101
102
103
Scale s (RRI)
M04
120
140
160
180
200
Heart rate HR (BPM)
1
5
10
Lag 
(RRI)
0.0
0.5
1.0
1.5
2.0
Conventional 1
101
102
103
Scale s (RRI)
M05
120
140
160
180
200
Heart rate HR (BPM)
1
5
10
Lag 
(RRI)
0.0
0.5
1.0
1.5
2.0
Conventional 1
101
102
103
Scale s (RRI)
M06
120
140
160
180
200
Heart rate HR (BPM)
1
5
10
Lag 
(RRI)
0.0
0.5
1.0
1.5
2.0
Conventional 1
101
102
103
Scale s (RRI)
M07
120
140
160
180
200
Heart rate HR (BPM)
140
150
160
170
180
190
Heart rate HR (BPM)
1
5
10
Lag 
(RRI)
2,000
4,000
6,000
8,000
10,000
12,000
14,000
Time t (s)
0.0
0.5
1.0
1.5
2.0
Conventional 1
Supplementary Figure S5. Overview of all the marathons in Group M. Left: Average RRI correlation results as a function of
binned relative heart rate for each subject of Group M. Right: RRI correlation landscapes of the marathon runs. For each
subject the DDFA-1 scaling exponents α(t, s) (upper panels) and DPACF-0 correlations C(t, τ) (lower panels) are shown. For
a detailed explanation about how the data is computed, please see Supplementary Appendix F.


## Page 17


17
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Dynamic scaling exponent (t,s)
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Dynamic PACF (t, )
120
140
160
180
Heart rate, mean
DFA
1 2 3 4 5 6 7 8 910
Lag 
DPACF
101
102
103
Scale s
DDFA
Q: 1/2
1/4
1/8
1/16
1/32
2.5
5.0
7.5
10.0
12.5
15.0
Heart rate, S.D.
DFA
1 2 3 4 5 6 7 8 910
Lag 
DPACF
101
102
103
Scale s
DDFA
101
102
103
Scale s (RRI)
Q=1
1
5
10
Lag  (RRI)
Q=1/2
0.0
0.5
1.0
1.5
2.0
Conventional 1
101
102
103
Scale s (RRI)
Q=1/4
1
5
10
Lag  (RRI)
Q=1/8
0.0
0.5
1.0
1.5
2.0
Conventional 1
101
102
103
Scale s (RRI)
Q=1/16
90
100
110
120
130
140
150
160
170
180
190
Heart rate HR (BPM)
1
5
10
Lag  (RRI)
Q=1/32
0.0
0.5
1.0
1.5
2.0
Conventional 1
90
100
110
120
130
140
150
160
170
180
190
Heart rate HR (BPM)
Supplementary Figure S6. Consistency of the results with respect to trends. Top row: diﬀerent quantiles Q of the mean and
standard deviation of the heart rate within the dynamic segments for all the data of subject T07. For DPACF-0 and DDFA-1
the dynamic segment length factor a has values of 10 and 5, respectively, and for conventional DFA the short-range (4–16 beats)
scaling exponent is computed in moving windows consisting of 50 RRIs. Lower panels: the average RRI correlation results as
a function of the heart rate when the data is limited to dynamic segments with the heart rate standard deviation less than
the value for the speciﬁed quantiles Q. For a detailed explanation about how the data is computed, please see Supplementary
Appendix F.


## Page 18


18
[1] A. L. Goldberger, L. A. N. Amaral, J. M. Hausdorﬀ, P. C.
Ivanov, C.-K. Peng, and H. E. Stanley, Fractal dynamics
in physiology: Alterations with disease and aging, Pro-
ceedings of the National Academy of Sciences 99, 2466
(2002).
[2] R. Karasik, N. Sapir, Y. Ashkenazy, P. C. Ivanov, I. Dvir,
P. Lavie, and S. Havlin, Correlation diﬀerences in heart-
beat ﬂuctuations during rest and exercise, Phys. Rev. E
66, 062902 (2002).
[3] A.
J.
Hautala,
T.
H.
Mäkikallio,
T.
Seppänen,
H. V. Huikuri, and M. P. Tulppo, Short-term cor-
relation
properties
of
R–R
interval
dynamics
at
diﬀerent
exercise
intensity
levels,
Clinical
Phys-
iology
and
Functional
Imaging
23,
215
(2003),
https://onlinelibrary.wiley.com/doi/pdf/10.1046/j.1475-
097X.2003.00499.x.
[4] T.
Gronwald
and
O.
Hoos,
Correlation
proper-
ties
of
heart
rate
variability
during
endurance
exercise:
A
systematic
review,
Annals
of
Non-
invasive
Electrocardiology
25,
e12697
(2020),
https://onlinelibrary.wiley.com/doi/pdf/10.1111/anec.12697.
[5] M. Buchheit, S. R., and G. P. Millet, Heart-rate deﬂec-
tion point and the second heart-rate variability threshold
during running exercise in trained boys, Pediatric Exer-
cise Science 19, 192 (2007).
[6] R. Di Michelle, G. Gatta, A. Di Leo, M. Cortesi, F. An-
dina, E. Tam, M. Da Boit, and F. Merni, Estimation
of the anaerobic threshold from heart rate variability in
an incremental swimming test, Journal of Strength and
Conditioning Research 26, 3059 (2012).
[7] Y. Yamamoto, R. L. Hughson, and J. C. Peterson, Au-
tonomic control of heart rate during exercise studied
by heart rate variability spectral analysis, Journal of
Applied Physiology 71, 1136 (1991), pMID: 1757310,
https://doi.org/10.1152/jappl.1991.71.3.1136.
[8] G. Billman, The LF/HF ratio does not accurately mea-
sure cardiac sympatho-vagal balance, Frontiers in Phys-
iology 4, 26 (2013).
[9] C.-K. Peng, S. V. Buldyrev, S. Havlin, M. Simons, H. E.
Stanley, and A. L. Goldberger, Mosaic organization of
DNA nucleotides, Physical Review E 49, 1685 (1994).
[10] C. Peng, S. Havlin, H. E. Stanley, and A. L. Goldberger,
Quantiﬁcation of scaling exponents and crossover phe-
nomena in nonstationary heartbeat time series, Chaos:
An Interdisciplinary Journal of Nonlinear Science 5, 82
(1995).
[11] J. W. Kantelhardt, E. Koscielny-Bunde, H. H. Rego,
S. Havlin, and A. Bunde, Detecting long-range correla-
tions with detrended ﬂuctuation analysis, Physica A: Sta-
tistical Mechanics and its Applications 295, 441 (2001).
[12] F. Shaﬀer and J. P. Ginsberg, An overview of heart rate
variability metrics and norms, Frontiers in Public Health
5, 258 (2017).
[13] D. E. Lieberman, A. G. Warrener, J. Wang, and E. R.
Castillo, Eﬀects of stride frequency and foor position at
landing on braking force, hip torque, impact peak force
and the metabolic cost of running in humans, J. Exp.
Biol. 218, 3406 (2015).
[14] C. Julien, The enigma of Mayer waves: Facts and models,
Cardiovascular Research 70, 12 (2006).
[15] J. Cassirame, R. Vanhaesebrouck, S. Chevrolat, and
L. Mourot, Accuracy of the Garmin 920 XT HRM to
perform HRV analysis, Austr. Phys. Eng. Sci. in Med.
40, 831 (2017).
[16] Garmin Canada, The ﬂexible and interoperable data
transfer (FIT) protocol software development kit, https:
//www.thisisant.com/resources/fit (2020).
[17] Polar Electro, Polar Flow web service, https://flow.
polar.com/ (2020).
[18] R. Gilgen-Ammann, T. Schweizer, and T. Wyss, RR in-
terval signal quality of a heart rate monitor and an ECG
Holter at rest and during exercise, Euro. J. App. Phys.
119, 1525 (2019).
[19] K. Kiyono and Y. Tsujimoto, Nonlinear ﬁltering proper-
ties of detrended ﬂuctuation analysis, Physica A: Statis-
tical Mechanics and its Applications 462, 807 (2016).
[20] B. Fornberg, Generation of ﬁnite diﬀerence formulas on
arbitrarily spaced grids, Mathematics of Computation
51, 699 (1988).
[21] J. Durbin, The ﬁtting of time-series models, Revue de
l’Institut International de Statistique / Review of the In-
ternational Statistical Institute 28, 233 (1960).
[22] D. A. Giles and N. Draper, Heart rate variability during
exercise: A comparison of artefact correction methods,
The Journal of Strength & Conditioning Research 32,
10.1519/JSC.0000000000001800 (2018).
[23] M. S. Santhanam, J. N. Bandyopadhyay, and D. Angom,
Quantum spectrum as a time series: Fluctuation mea-
sures, Phys. Rev. E 73, 015201(R) (2006).
[24] V. Kotimäki, E. Räsänen, H. Hennig, and E. J. Heller,
Fractal dynamics in chaotic quantum transport, Phys.
Rev. E 88, 022913 (2013).
[25] J. Kim, D. Shah, I. Potapov, J. Latukka, K. Aalto-Setälä,
and E. Räsänen, Scaling and correlation properties of RR
and QT intervals at the cellular level, Scientiﬁc Reports
9, 3651 (2019).
[26] N. Vandewalle and M. Ausloos, Coherent and random
sequences in ﬁnancial ﬂuctuations, Physica A: Statistical
Mechanics and its Applications 246, 454 (1997).
[27] H. Hennig, R. Fleischmann, A. Fredebohm, Y. Hag-
mayer, J. Nagler, A. Witt, F. Theis, and T. Geisel, The
nature and perception of ﬂuctuations in human musical
rhythms, PloS one 6, e26457 (2011).
[28] E. Räsänen, O. Pulkkinen, T. Virtanen, M. Zollner, and
H. Hennig, Fluctuations of hi-hat timing and dynamics
in a virtuoso drum track of a popular music recording,
PLOS ONE 10, 1 (2015).
[29] K. Hu, P. C. Ivanov, Z. Chen, P. Carpena, and H. E.
Stanley, Eﬀect of trends on detrended ﬂuctuation analy-
sis, Phys. Rev. E 64, 011114 (2001).
[30] Z. Chen, P. C. Ivanov, K. Hu, and H. E. Stanley, Ef-
fect of nonstationarities on detrended ﬂuctuation analy-
sis, Phys. Rev. E 65, 041107 (2002).
[31] C. Heneghan and G. McDarby, Establishing the relation
between detrended ﬂuctuation analysis and power spec-
tral density analysis for stochastic processes, Phys. Rev.
E 62, 6103 (2000).
[32] K. Kiyono, Establishing a direct connection between de-
trended ﬂuctuation analysis and fourier analysis, Phys.
Rev. E 92, 042925 (2015).
[33] M. Höll and H. Kantz, The relationship between the
detrendend ﬂuctuation analysis and the autocorrelation


## Page 19


19
function of a signal, The European Physical Journal B
88, 327 (2015).
[34] O. Løvsletten, Consistency of detrended ﬂuctuation anal-
ysis, Phys. Rev. E 96, 012141 (2017).
[35] M. Höll, H. Kantz, and Y. Zhou, Detrended ﬂuctuation
analysis and the diﬀerence between external drifts and
intrinsic diﬀusionlike nonstationarity, Phys. Rev. E 94,
042201 (2016).
[36] M. Höll, K. Kiyono, and H. Kantz, Theoretical founda-
tion of detrending methods for ﬂuctuation analysis such
as detrended ﬂuctuation analysis and detrending moving
average, Phys. Rev. E 99, 033305 (2019).
[37] J. W. Kantelhardt, S. A. Zschiegner, E. Koscielny-Bunde,
S. Havlin, A. Bunde, and H. E. Stanley, Multifractal de-
trended ﬂuctuation analysis of nonstationary time series,
Physica A: Statistical Mechanics and its Applications
316, 87 (2002).
[38] B. Podobnik and H. E. Stanley, Detrended cross-
correlation analysis: A new method for analyzing two
nonstationary time series, Phys. Rev. Lett. 100, 084102
(2008).
[39] Originally it was the exponent in Hurst’s R/S analysis
[56], and Mandelbrot and van Ness used it as a parame-
ter for deﬁning fGn and fBm [51]. For these processes it
can be related to the (asymptotic) DFA scaling exponent
(fGn: α = H, fBm: α = H + 1). In the 0 < α < 1 range
the relationship (between R/S and DFA exponents) is
approximate, and for fGn/fBm holds asymptotically for
large scales. For α > 1 the interpretation α = H + 1 is
essentially due to the deﬁnition of fBm. It also could be
argued to hold, at least approximately, for processes that
are deﬁned as the cumulative sum of another process,
similarly as the (discrete) fGn/fBm.
[40] E. Ge and Y. Leung, Detection of crossover time scales
in multifractal detrended ﬂuctuation analysis, Journal of
Geographical Systems 15, 115 (2013).
[41] A. Habib, J. P. Sorensen, J. P. Bloomﬁeld, K. Muchan,
A. J. Newell, and A. P. Butler, Temporal scaling phenom-
ena in groundwater-ﬂoodplain systems using robust de-
trended ﬂuctuation analysis, Journal of Hydrology 549,
715 (2017).
[42] G. M. Viswanathan, C.-K. Peng, H. E. Stanley, and A. L.
Goldberger, Deviations from uniform power law scaling
in nonstationary time series, Phys. Rev. E 55, 845 (1997).
[43] J. C. Echeverría, M. S. Woolfson, J. A. Crowe, B. R.
Hayes-Gill, G. D. H. Croaker, and H. Vyas, Interpreta-
tion of heart rate variability via detrended ﬂuctuation
analysis and αβ ﬁlter, Chaos: An Interdisciplinary Jour-
nal of Nonlinear Science 13, 467 (2003).
[44] P. Castiglioni, G. Parati, A. Civijian, L. Quintin, and
M. D. Rienzo, Local scale exponents of blood pressure
and heart rate variability by detrended ﬂuctuation anal-
ysis: Eﬀects of posture, exercise, and aging, IEEE Trans-
actions on Biomedical Engineering 56, 675 (2009).
[45] J. Xia, P. Shang, and J. Wang, Estimation of local scale
exponents for heartbeat time series based on DFA, Non-
linear Dynamics 74, 1183 (2013).
[46] M. Molkkari and E. Räsänen, Robust estimation of the
scaling exponent in detrended ﬂuctuation analysis of beat
rate variability, in Computing in Cardiology (2018).
[47] G. E. Box, G. M. Jenkins, and G. C. Reinsel, Time Series
Analysis, Forecasting and Control, 4th ed., Wiley Series
in Probability and Statistics (Wiley, 2008).
[48] P. G. Meyer and H. Kantz, Inferring characteristic
timescales from the eﬀect of autoregressive dynamics on
detrended ﬂuctuation analysis, New Journal of Physics
21, 033022 (2019).
[49] R. M. Bryce and K. B. Sprague, Revisiting detrended
ﬂuctuation analysis, Scientiﬁc reports 2, 315 (2012).
[50] We adapt the notation from Ref. [34] with the following
changes: The factor s−1 is included in the weight func-
tion G(j, s) that is symmetrically extended for negative
j by G(−j, s) = G(j, s). This allows for a more succinct
notation for Eqs. D1 and D2.
[51] B. Mandelbrot and J. Van Ness, Fractional brownian mo-
tions, fractional noises and applications, SIAM Review
10, 422 (1968).
[52] M. Molkkari, Advanced Methods in Detrended Fluctua-
tion Analysis with Applications in Computational Cardi-
ology, Master’s thesis, Tampere University (2019).
[53] Y.-H. Shao, G.-F. Gu, Z.-Q. Jiang, W.-X. Zhou, and
D. Sornette, Comparing the performance of FA, DFA and
DMA using diﬀerent synthetic long-range correlated time
series, Scientiﬁc Reports 2, 835 (2012).
[54] R. B. Davies and D. S. Harte, Tests for Hurst eﬀect,
Biometrika 74, 95 (1987).
[55] The accuracy of the simulated time series is established
by comparing their joint ﬂuctuation functions (the mean
in (B2) is taken over the squared ﬂuctuations F 2
s,w of all
realizations of the simulated time series) to the theoreti-
cal ﬂuctuation functions of fGn and fBm.
[56] H. E. Hurst, The problem of long-term storage in reser-
voirs, International Association of Scientiﬁc Hydrology.
Bulletin 1, 13 (1956).

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
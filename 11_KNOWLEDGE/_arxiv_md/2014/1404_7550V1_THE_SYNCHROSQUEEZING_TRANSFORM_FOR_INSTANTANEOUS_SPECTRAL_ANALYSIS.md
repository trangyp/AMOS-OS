---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1404.7550v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1404.7550v1_The_Synchrosqueezing_transform_for_instantaneous_spectral_analysis

> Source: 1404.7550v1_The_Synchrosqueezing_transform_for_instantaneous_spectral_analysis.pdf

> Pages: 9

---


## Page 1


The Synchrosqueezing transform for instantaneous spectral analysis
Gaurav Thakur
April 11, 2014
Abstract
The Synchrosqueezing transform is a time-frequency analysis method that can decompose complex
signals into time-varying oscillatory components. It is a form of time-frequency reassignment that is
both sparse and invertible, allowing for the recovery of the signal. This article presents an overview of
the theory and stability properties of Synchrosqueezing, as well as applications of the technique to topics
in cardiology, climate science and economics.
1
Introduction
The Synchrosqueezing transform is a time-frequency analysis method that can characterize signals with
time-varying oscillatory properties. It is designed to analyze and decompose signals of the form
f(t) =
K
∑
k=1
Ak(t)e2πiφk(t),
(1)
where the Ak and φk are time-varying amplitude and phase functions respectively. The goal is to recover
the instantaneous frequencies (IFs) {φ ′
k}1≤k≤K and the oscillatory components {Ake2πiφk}1≤k≤K. Signals
of the form (1) arise in numerous scientiﬁc and engineering applications1 but are not well represented in
a traditional Fourier basis, where the individual elements of the basis fail to capture localized oscillations
in the components {Ake2πiφk}. Standard time-frequency methods such as the short-time Fourier transform
(STFT) and the continuous wavelet transform (CWT) are often used to analyze such signals, but do not take
advantage of any sparsity of the form (1) in the signal and incur a tradeoff in time-frequency resolution
[5, 8]. Synchrosqueezing is a variant of time-frequency reassignment (TFR), a class of techniques that ap-
ply a nonlinear post-processing mapping to a conventional STFT or CWT plot. The mapping is designed to
“push” the energy in an STFT closer to its most prominent frequencies, resulting in a sparse and concen-
trated time-frequency representation of the signal [2, 9]. However, traditional TFR methods result in a loss
of information from the underlying transform and cannot be used to recover the original signal, and also
often involve heuristics that are difﬁcult to justify rigorously.
Synchrosqueezing combines the localization and sparsity properties of TFR with the invertibility of a tradi-
tional time-frequency transform, and is robust to a variety of disturbances in the signal. The main concepts
behind Synchrosqueezing were originally introduced in the mid-1990s for audio signal analysis [7], but
it has received much closer attention in recent years, with an extensive mathematical theory developed in
[6] and [15]. Unlike traditional TFR, Synchrosqueezing performs the post-processing mapping only in the
frequency direction and does so in a manner that preserves the total energy of the signal f, allowing for
1Such signals are often called “nonstationary” in these domains, although this terminology is not related to its meaning for
random processes.
1
arXiv:1404.7550v1  [cs.CE]  29 Apr 2014


## Page 2


the decomposition of the signal into the components {Ake2πiφk}. This article provides a concise survey of
the Synchrosqueezing methodology and its associated theory, and also discusses real-world applications in
several different domains where the technique has provided new insights.
2
The Synchrosqueezing process
The Synchrosqueezing transform was originally developed in [6] and [7] in terms of the CWT. We choose a
(complex) mother wavelet ψ such that the Fourier transform ˆψ has strictly positive support and satisﬁes the
standard admissibility condition
´ ∞
0 z−1 ˆψ(z)dz < ∞[5]. The CWT Wψ f(a,t) at the scale a and time shift t
is then given by
Wψ f(a,t) = a−1/2
ˆ ∞
−∞
f(u)ψ
u−t
a

du.
(2)
We then take the phase transform ω f(a,b), deﬁned as the derivative of the complex phase of Wψ f,
ω f(a,t) =
∂
∂tWψ f(a,t)
2πiWψ f(a,t).
(3)
Intuitively, this nonlinear operator can be thought of as removing the inﬂuence of ψ from the CWT and “en-
coding” the localized frequency information we want. The key step is to consider the CWT Synchrosqueezing
transform,
Sδ,M
ε
f(t,η) =
ˆ
{(a,t):a∈[M−1,M],|Wψ f(a,t)|>ε}
a−3/2Wψ f(a,t) 1
δ h
η −ω f(a,t)
δ

da
(4)
for a test function h ∈C∞
0 , a sufﬁciently large parameter M, and sufﬁciently small δ > 0 and ε > 0. The
motivation for (4) is that it is a smoothed out approximation to
S f(t,η) =
ˆ
{(a,t):η=ω f(a,t)}
a−3/2Wψ f(a,t)da,
or in other words, a partial inversion of the CWT that is only taken over the level curves of the phase
transform ω f and ignores the rest of the time-scale plane (a,t). This localization process allows us to
recover the components Ake2πiφk more accurately than inverting the CWT over the entire time-scale plane.
Alternatively, the mapping Wψ f(a,t) →S f(t,η) can be thought of as a reassignment operation that squeezes
energy from the scales a into IFs η centered on the level curves of ω f, but leaves the total energy in
Wψ f(a,t) at each time t unchanged. For appropriate signals f, the energy in the Synchrosqueezing transform
Sδ,M
ε
f(b,η) is concentrated precisely around the IF curves {φ ′
k(t)}. Finally, once Sδ,M
ε
f is computed, we
can recover each of the components by completing the inversion of the CWT and integrating over small
bands around each IF curve,
Rδ,M
k,ε f(t) =
1
´ ∞
0
ˆψ(z)
z dz
ˆ
|η−φ′
k(t)|<ε
Sδ,M
ε
f(t,η)dη.
(5)
Under certain conditions, it can be shown that Rδ,M
k,ε f(t) ≈Ak(t)e2πiφk(t). In practice, an additional, inter-
mediate step is needed to identify the integration bands in (5), which is typically accomplished by a ridge
extraction method that determines the maxima in the time-frequency plot |Sδ,M
ε
f(t,η)|. A discretized for-
mulation of the steps (2)-(5) and related computational details can be found in [14].
2


## Page 3


The main concepts behind Synchrosqueezing can also be applied to other underlying time-frequency repre-
sentations. The paper [15] develops a parallel approach based on the short-time Fourier transform (STFT),
which is shown to have some advantages.2 The STFT Synchrosqueezing process is similar to the above
development, but instead of (2) is based on the modiﬁed STFT for an appropriate window function G,
VG f(t,z) =
ˆ ∞
−∞
f(u)G(u−t)e−2πiz(u−t)du.
(6)
This is simply the standard STFT with an additional modulation factor e2πizt, and can be thought of as a
ﬁlter bank taken by sliding the window G over different frequency bands. The phase transform (3) and
Synchrosqueezing transform (4) respectively become
˜ω f(z,t) =
∂
∂tVG f(t,z)
2πiVG f(t,z),
˜Sδ,M
ε
f(t,η) =
ˆ
{(t,z):z∈[M−1,M],|VG f(t,η)|>ε}
VG f(t,z) 1
δ h
η −˜ω f(t,z)
δ

dz,
(7)
and the components can be recovered by fully inverting (7) as before by taking
˜Rδ,M
k,ε f(t) =
1
´ ∞
−∞|G(z)|2dz
ˆ
|η−φ′
k|<ε
˜Sδ,M
ε
f(t,η)dη.
(8)
A simple example of the time-frequency plots |Sδ,M
ε
(t,η)| and | ˜Sδ,M
ε
f(t,η)| is shown in Figure 1. While the
traditional STFT and CWT plots are blurry, reﬂecting the fact that they are not sparse representations of the
signal, the Synchrosqueezing transforms have a much more concentrated proﬁle and distinct IF curves in the
time-frequency plane. Several additional examples can be found in [14], comparing CWT Synchrosqueez-
ing with TFR methods and other techniques. An open source MATLAB toolbox implementing both forms
of Synchrosqueezing is available [3] and has facilitated the use of the technique across different disciplines.
We brieﬂy describe several extensions of these concepts that have been developed. The paper [16] considers
a variant of the signal model in (1), where the mode Ak(t)e2πiφk(t) is replaced by a more general form
Ak(t)s(φk(t)) for a given “shape function” s chosen to ﬁt a particular application at hand. This turns out to
be a natural model for the analysis of electrocardiogram signals, in which the sharp spikes (see Figure 2) are
not well represented by standard Fourier harmonics. In [12], another generalization is presented based on
replacing (6) with a “generalized Fourier transform,” i.e an oscillatory integral of the form
´ ∞
−∞f(u)g(u −
t)e−2πizθ(u)du where θ is a nonlinear phase function incorporating some prior knowledge of the signal’s
structure. The paper [19] develops another approach based on wave packet transforms, which encompasses
some aspects of both the CWT and STFT formulations.
3
Theory
Synchrosqueezing has a fairly comprehensive mathematical theory developed for it, providing performance
guarantees on selected classes of signals. As of 2014, most of the published theory in [6] and [14] covers the
CWT version (4), but analogous results can be shown for the STFT formulation (7) from [15] using similar
techniques. We review the results for the CWT case here, which are based on a sparsity model for the signal
(1) in the frequency domain.
2We present a slightly different formulation of the transform than [15] that is more comparable with the approach in [6].
3


## Page 4


Frequency (hz)
CWT
 
 
0
2.8571
5.7143
8.5714
11.4286 14.2857 17.1429
20
0.046
0.21
0.97
4.5
20
STFT
 
 
0
2.8571
5.7143
8.5714
11.4286 14.2857 17.1429
20
0
10
20
30
40
50
Time (seconds)
Frequency (hz)
CWT Synchrosqueezing
 
 
0
2.8571
5.7143
8.5714
11.4286 14.2857 17.1429
20
0.05
10
20
30
40
50
Time (seconds)
STFT Synchrosqueezing
 
 
0
2.8571
5.7143
8.5714
11.4286 14.2857 17.1429
20
0
10
20
30
40
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
0.5
1
1.5
2
0.005
0.01
0.015
0.02
0.025
0.03
0
1
2
3
4
5
Figure 1:
Time-frequency plots of the signal f(t) = cos(2π(0.1t2.6 + 3sin(2t) + 10t)) under different
transforms.
Deﬁnition 1. For given parameters ε,d > 0, we deﬁne the class Aε,d = { f : f(t) = ∑K
k=1 Ak(t)e2πiφk(t)},
where
Ak ∈L∞∩C1,
φk ∈C2,
φ ′
k,φ ′′
k ∈L∞,
Ak(t) > 0,
φ ′
k(t) > 0
∀t
A′
k(t)
 ≤ε
φ ′
k(t)
,
φ ′′
k (t)
 ≤ε
φ ′
k(t)
,
and
φ ′
k(t)−φ ′
k−1(t)
φ ′
k(t)+φ ′
k−1(t) ≥d.
(9)
The key condition here is (9), which says that higher frequency IFs are spaced exponentially further apart
than lower frequency IFs. Under this signal model, the following result can be obtained [6].
Theorem 2. Let f ∈Aε,d for some ε,d > 0, h ∈C∞
0 with ∥h∥L1 = 1, and ψ ∈C1 with ˆψ supported in
[1 −∆,1 + ∆] for some ∆<
d
1+d. Let M be sufﬁciently large and deﬁne ˜ε = ε1/3 and the “scale band”
Zk = {(a,b) : |aφ ′
k(t)−1| < ∆}. If (a,t) ∈Zk and |Wψ f(a,t)| > ˜ε, then |ω f(a,t)−φ ′
k(t)| ≤˜ε. Conversely,
if (a,t) ̸∈Zk for any k, then |Wψ f(a,t)| ≤˜ε. Futhermore, for some constant C1,
lim
δ→0Rδ,M
k,˜ε f(t)−Ak(t)e2πiφk(t)
 ≤C1˜ε.
This result says that the energy in the Synchrosqueezing time-frequency plane is concentrated around the IF
curves {φ ′
k(t)}, and the inverted components fk approximate the actual oscillatory components {Ake2πiφk}.
Additional results of this type were proved in [14], describing the robustness of the Synchrosqueezing trans-
form under unstructured perturbations (e.g. quantization error) as well as white noise. We slightly para-
phrase these theorems for clarity.
Theorem 3. Let f, ε, d, h, ψ and ∆be given as in Theorem 2. Let g = f + E for some error E with
∥E∥L∞sufﬁciently small. There are positive constants M, C2, C3 and C4 such that the following holds. Let
4


## Page 5


a ∈[ 1
M,M]. If (a,t) ∈Zk and |Wψg(a,t)| > C2˜ε, then |ωg(a,t)−φ ′
k(t)| ≤C3˜ε. Conversely, if (a,t) ̸∈Zk for
any k, then |Wψg(a,t)| ≤C2˜ε. Futhermore,
lim
δ→0Rδ,M
k,C2 ˜εg(t)−Ak(t)e2πiφk(t)
 ≤C4˜ε.
Theorem 4. Let f, ε, d, h, ψ and ∆be given as in Theorem 2, with ψ also satisfying |⟨ψ,ψ′⟩| < ∥ψ∥L2 ∥ψ′∥L2.
Let g = f +N, where N is Gaussian white noise with power ε2+p for some p > 0. There are positive constants
M, E1, E2, C′
2, C′
3 and C′
4 such that the following holds. Let a ∈[ 1
M,M]. If (a,t) ∈Zk and |Wψg(a,t)| > C′
2˜ε,
then with probability 1 −e−E1ε−p, |ωg(a,t) −φ ′
k(t)| ≤C′
3˜ε. Conversely, if (a,t) ̸∈Zk for any k, then with
probability 1−e−E2ε−p, |Wψg(a,t)| ≤C′
2˜ε. Futhermore, with probability 1−e−E1ε−p,
lim
δ→0Rδ,M
k,C2 ˜εg(t)−Ak(t)e2πiφk(t)
 ≤C′
4˜ε.
For STFT Synchrosqueezing, a result similar to Theorem 2 was proved in [15], although presented in slightly
different terms there. The main distinction with the STFT approach is that the theory is developed for a dif-
ferent function class Bε,d, deﬁned in the same way as Aε,d in Deﬁnition 1 but with (9) replaced by the
weaker separation requirement that inft φ ′
k(t)−supt φ ′
k−1(t) > d. The linear frequency scale of the modiﬁed
STFT effectively allows the IF curves {φ ′
k} to be spaced much closer to each other than the logarithmic scale
of the CWT. In practical terms, STFT Synchrosqueezing is well suited for decomposing signals with multiple
components that have closely packed IFs, especially at higher frequencies, while CWT Synchrosqueezing
is more appropriate for studying low frequency, trend-like components in a signal.
We ﬁnally mention that the above results have mostly been formulated in a deterministic setting, where the
signal of interest f is assumed to lie in the class Aε,d but without any particular mechanism that generated it.
The paper [4] develops extensions of these ideas to a stochastic model of the form Y(t) = f(t)+T(t)+X(t),
where f is essentially of the type Aε,d, T is a slowly varying trend and X is an autoregressive moving average
(ARMA) process with a time-dependent variance. The authors use CWT Synchrosqueezing to extract the
components f, T and X from an observed signal Y, and prove several results on conﬁdence bounds and other
aspects of the decomposition.
4
Applications
Due to its wide applicability, the Synchrosqueezing transform has been used to address problems in many
diverse disciplines. The technique was ﬁrst applied to topics in cardiology, speciﬁcally the analysis of elec-
trocardiogram (ECG) signals [15, 17, 18]. The sharp spikes in an ECG signal are called the R peaks (see
Figure 2) and encode important information about a patient’s heart rate, respiration and many other phys-
iological properties. The analysis of respiration, or breathing characteristics, is important in many clinical
applications such as testing for sleep apnea. However, recording the respiration directly requires hooking
up a breathing apparatus (ventilator) to the patient and is often impractical to perform over a long period
of time. A patient’s respiration inﬂuences the ECG measurement and can be modeled as a low frequency
envelope ﬁtting over the R peaks, with the ECG signal’s IF closely following the unobserved respiration
signal’s IF. The R peaks are not spaced uniformly but can be used to form an impulse train ∑k f(tk)δ(·−tk),
where {tk} are the locations of the R peaks. Applying the STFT Synchrosqueezing transform to this impulse
train provides an IF that accurately reﬂects short-range frequency variations in the respiration signal (Figure
2), and can be used for diagnosing irregularities in the patient’s breathing.
5


## Page 6


Synchrosqueezing has also been used for the analysis of long term trends in the global climate. The pa-
per [14] studies sediment cores extracted from the ocean ﬂoor, in which the relative concentrations of the
oxygen isotopes δ 18O and δ 16O indicate changes in the sea level, ice volume and deep ocean temperature.
These are caused by long term ﬂuctuations in the Earth’s eccentricity and other rotational properties over
time, known as Milankovitch cycles, which inﬂuence the amount of solar radiation received at the top of the
atmosphere. The CWT Synchrosqueezing transform is used to analyze the δ 18O levels in several composite
stacks of cores over the last 2.5 million years (Figure 3). It is able to distinguish the different Milankovitch
cycles more accurately than the regular CWT, commonly used in this ﬁeld, and identify when certain com-
ponents faded away or became more prominent. The invertibility of the transform also allows one to extract
the oscillatory components corresponding to each of the Milankovitch cycles, and better characterize some
sudden changes in the climate between 0.5 and 1 million years ago.
Another application of Synchrosqueezing can be found in economics. The paper [10] studies the stability of
the US ﬁnancial system by considering time-frequency decompositions of equity indices, Treasury yields,
foreign exchange rates and several other macroecomonic time series. Each time series is thought of as the
output of a dynamical system that produces slowly time-varying frequencies of the form (1), but which are
interspersed by abrupt frequency transitions (structural breaks) that indicate the starting or stopping of new
underlying dynamics. Among other events, the stock market crash in 1987 is contrasted with the global
recession in 2008. It is shown that the former had a minimal impact on the dominant, low frequency com-
ponents despite being prominent in the original data, while the latter was both preceded and followed by a
variety of new dynamics, which left the economy in a permanently altered state (Figure 4). The authors also
discuss a measure of instability in a time series called the “density index,” taking the L1 norm of the IFs at
each point in time as a measure of how spread out or concentrated the frequencies are. A sharp jump in the
density index corresponds to a structural break, which is shown to coincide with some of the major ﬁnancial
stress events over the last 25 years and which may provide “early warning” signs of future economic crises.
We brieﬂy mention several other applications of Synchrosqueezing that have appeared in the literature. In
[13], it is used to detect and analyze faults in a mechanical gearbox. The Synchrosqueezing plot of the
gearbox’s vibration signal reveals extra sideband components surrounding a central IF curve, which indicate
the presence of a chipped gear in the transmission. In geophysics, [11] discusses the use of Synchrosqueez-
ing to separate out resonant frequencies in data from micro-seismic experiments, which are used to study
deformations in injection wells for oil extraction. Finally, [1] develops an automated trading strategy based
on Synchrosqueezing, using the technique to model the relationship between correlated asset pairs such as
the stocks of competing ﬁrms. The rise in one asset’s price often precedes a fall in the other one, and a
strategy based on identifying the prices’ IFs is shown to describe short-range oscillations and outperform
some standard approaches used in the industry.
6


## Page 7


0
2
4
6
8
10
12
1000
1500
2000
2500
3000
3500
50
100
150
200
250
300
1000
2000
3000
4000
5000
Time
Signal
Figure 2: Top: 10 second portion of ECG signal. Bottom: True respiration signal (blue) and the IF computed
from the ECG signal’s R peaks (red) using STFT Synchrosqueezing.
Period (kyr)
 e − Insolation Index 
5
14
38
1.1e+002
2.9e+002
8e+002
 f − DSDP607 
5
14
38
1.1e+002
2.9e+002
8e+002
Period (kyr)
Time (Myr)
 g − LR05 Stack 
−2500.0−2143.0−1786.0−1429.0−1072.0 −715.0 −358.0
−1.0
5
14
38
1.1e+002
2.9e+002
8e+002
Time (Myr)
 h − H07 Stack 
−2.5 −2.1429−1.7857−1.4286−1.0714−0.7143−0.3571
0
5
14
38
1.1e+002
2.9e+002
8e+002
Figure 3: Left: CWT Synchrosqueezing plots of the insolation index, a single core (DSPD07) and stacks of
such cores (LR05 and H07). Right: Reconstructed oscillatory components, corresponding to the obliquity,
precession and eccentricity cycles.
7


## Page 8


S&P500
Frequency (cycles/year)
 
 
1987
1992
1997
2002
2007
2012
0.19
0.93
4.6
23
T−note
 
 
1987
1992
1997
2002
2007
2012
0.19
0.93
4.6
23
0
0.5
1
1.5
2
2.5
3
3.5
4
x 10
−3
0
0.5
1
1.5
2
2.5
3
3.5
x 10
−3
Figure 4: CWT Synchrosqueezing plots of the S&P 500 price and the 10-year US Treasury yield.
References
[1] A. Ahrabian, C. C. Took, and D. Mandic. Algorithmic Trading Using Phase Synchronization. IEEE
Journal of Selected Topics in Signal Processing, 99, 2012.
[2] F. Auger, P. Flandrin, Y.-T. Lin, S. McLaughlin, S. Meignen, T. Oberlin, and H.-T. Wu.
Time-
Frequency Reassignment and Synchrosqueezing. IEEE Signal Processing Magazine, pages 32–41,
2013.
[3] E.
Brevdo,
G.
Thakur,
and
H.-T.
Wu.
The
Synchrosqueezing
Toolbox.
2013.
https://web.math.princeton.edu/~ebrevdo/synsq/.
[4] Y.-C. Chen, M.-Y. Cheng, and H.-T. Wu. Nonparametric and adaptive modeling of dynamic periodicity
and trend with heteroscedastic and dependent errors. Journal of the Royal Statistical Society: Series
B, 2013.
[5] I. Daubechies. Ten lectures on wavelets. Society for Industrial and Applied Mathematics, 1992.
[6] I. Daubechies, J. Lu, and H.-T. Wu.
Synchrosqueezed wavelet transforms: An empirical mode
decomposition-like tool. Applied and Computational Harmonic Analysis, 30(2):243–261, 2011.
[7] I. Daubechies and S. Maes. A nonlinear squeezing of the continuous wavelet transform based on
auditory nerve models. Wavelets in Medicine and Biology, pages 527–546, 1996.
[8] P. Flandrin. Time-frequency/time-scale analysis, volume 10 of Wavelet Analysis and its Applications.
Academic Press Inc., San Diego, CA, 1999.
[9] P. Flandrin, F. Auger, and E. Chassande-Mottin. Time-Frequency Reassignment – From Principles to
Algorithms. In A. Papandreou-Suppappola, editor, Applications in time-frequency signal processing.
CRC, 2003.
8


## Page 9


[10] S. K. Guharay, G. S. Thakur, F. J. Goodman, S. L. Rosen, and D. Houser. Analysis of non-stationary
dynamics in the ﬁnancial system. Economics Letters, 121:454–457, 2013.
[11] R. H. Herrera, J.-B. Tary, and M. van der Baan. Time-frequency representation of microseismic signals
using the Synchrosqueezing transform. GeoConvention, 2013.
[12] C. Li and M. Liang. A generalized synchrosqueezing transform for enhancing signal time-frequency
separation. Signal Processing, 92:2264–2274, 2012.
[13] C. Li and M. Liang. Time-frequency analysis for gearbox fault diagnosis using a generalized syn-
chrosqueezing transform. Mechanical Systems and Signal Processing, 26:205–217, 2012.
[14] G. Thakur, E. Brevdo, N.-S. Fuckar, and H.-T. Wu.
The Synchrosqueezing algorithm for time-
varying spectral analysis: robustness properties and new paleoclimate applications. Signal Processing,
93:1079–1094, 2013.
[15] G. Thakur and H.-T. Wu. Synchrosqueezing-based Recovery of Instantaneous Frequency from Nonuni-
form Samples. SIAM Journal on Mathematical Analysis, 43(5):2078–2095, 2011.
[16] H.-T. Wu. Instantaneous frequency and wave shape functions (I). Applied and Computational Har-
monic Analysis, 35:181–199, 2013.
[17] H.-T. Wu, Y.-H. Chan, Y.-T. Lin, and Y.-H. Yeh. Using synchrosqueezing transform to discover breath-
ing dynamics from ECG signals. Applied and Computational Harmonic Analysis, 36(2):354–359,
2014.
[18] H.-T. Wu, S.-S. Hseu, M.-Y. Bien, Y. R. Kou, and I. Daubechies. Evaluating the physiological dynam-
ics via Synchrosqueezing: Prediction of the Ventilator Weaning. IEEE Transactions on Biomedical
Engineering, 2014. to appear.
[19] H. Yang. Synchrosqueezed Wave Packet Transforms and Diffeomorphism Based Spectral Analysis for
1D General Mode Decompositions. arXiv, 1311.4655, 2013.
9

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
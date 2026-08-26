---
canon-group: reference
rscf-state: source-claim
arxiv_id: 0802.0885v2
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 0802.0885v2_Amplified_Dispersive_Optical_Tomography

> Source: 0802.0885v2_Amplified_Dispersive_Optical_Tomography.pdf

> Pages: 7

---


## Page 1


arXiv:0802.0885v2  [physics.optics]  27 Feb 2008
Ampliﬁed Dispersive Optical Tomography
Keisuke Goda, Daniel R. Solli, and Bahram Jalali
Department of Electrical Engineering, University of California, Los Angeles, California 90095, USA
Optical coherence tomography (OCT) [1, 2] has proven to be a powerful technique for studying
tissue morphology in ophthalmology [3, 4], cardiology [2], gastroenterology [2, 5, 6], and endomi-
croscopy [7]. Its performance is limited by the fundamental trade-oﬀbetween the imaging sensitivity
and acquisition speed [8, 9, 10] – a predicament common in virtually all imaging systems. In this
paper, we circumvent this limit by using distributed Raman post-ampliﬁcation of the reﬂection from
the sample. We combine the ampliﬁcation with simultaneously performed dispersive Fourier trans-
formation, a process that maps the optical spectrum into an easily measured time-domain waveform.
The Raman ampliﬁcation enables measurement of weak signals which are otherwise buried in noise.
It extends the depth range without sacriﬁcing the acquisition speed or causing damage to the sam-
ple. As proof of concept, single-shot imaging with 15 dB improvement in sensitivity at an axial scan
rate of 36.6 MHz is demonstrated.
I.
INTRODUCTION
Since the invention of OCT in 1991 [1], it has evolved into several diﬀerent varieties, all of which can be placed into
two major categories: time-domain OCT [1] and frequency-domain OCT [7, 8, 11, 12, 13]. Frequency-domain OCT
provides higher acquisition speed and better signal-to-noise ratio (SNR) than the time-domain approach [8, 10] because
it avoids mechanical scanning. The frequency-domain OCT uses a broadband optical source, and the depth proﬁle
is encoded into the optical spectrum through the interference between the two arms of a Michelson interferometer.
There are two implementations of this, which use diﬀerent optical sources. In one implementation (the so-called
swept-source OCT [7, 11, 12]), the optical frequency is encoded in time with a frequency-tunable source. In the
other implementation (the so-called Fourier-domain OCT [3, 13]), the source has a wide instantaneous bandwidth
and the spectrum is obtained using a diﬀraction grating combined with a linear detector array. In both cases, due to
the Fourier relation between the temporal autocorrelation and the spectral power density, the depth information is
obtained after an inverse Fourier transform of acquired spectra.
Among the two frequency domain approaches, Fourier-domain OCT achieves better axial resolution as it beneﬁts
from the availability of supercontinuum sources with large bandwidth (hundreds of nm). However, Fourier-domain
OCT is bulky and expensive, and has low environmental tolerance because it requires a diﬀraction grating and array
detector (e.g. a CCD or CMOS) [3, 13, 14]. Moreover, the data acquisition speed of a CCD is low (only up to 10
kHz), limiting the imaging speed. In other words, there is a trade-oﬀbetween the spectral resolution and imaging
speed. On the other hand, swept-source OCT does not require an optical spectrometer because the wavelength is
known for each time sample; however, the bandwidth, and hence the axial resolution, is limited by the tuning range
of the laser, and the broadening of the instantaneous linewidth limits the depth range.
Dispersive Fourier transformation (FT) exploits the mathematical equivalence between paraxial diﬀraction and
temporal dispersion [15]. Its ability to map the spectrum into a temporal waveform has been used in measurement
of the spectrum of laser pulses [16, 17], ﬁber dispersion measurement [17, 18], absorption spectroscopy [19, 20, 21],
Raman spectroscopy [15], reﬂectometry [22], and OCT [23]. Measuring the spectrum in Fourier-domain OCT using
dispersive FT avoids these issues by eliminating the diﬀraction grating and detector array [22, 23]. These elements
are replaced by a dispersive ﬁber, a single detector, and a digitizer. This simpliﬁes the system, and more importantly,
enables fast real-time image acquisition. However, the loss in the dispersive medium, which, at the most basic level,
is caused by the intimate connection between dispersion and loss described by the Kramers-Kronig relations, [24]
limits the imaging sensitivity as well as the depth range. The latter can be understood by recognizing that, by virtue
of spectrum-to-time conversion, the spectral resolution (which determines the depth range) is ﬁxed by the temporal
resolution of the electrical detection system. Stated diﬀerently, the electrical bandwidth of the digitizer limits the
spectral resolution, a relation given by ∆f = 0.35λ2
0/cDfdig, where ∆f is the spectral resolution, λ0 is the center
wavelength, c is the speed of light in vacuum, D is the total group-velocity dispersion, and fdig is the input bandwidth
of the real-time digitizer. The product of ∆f × D is ﬁxed by the bandwidth of the digitizer; hence, to increase the
optical resolution (i.e., to increase the depth range) one is forced to increase the total group-velocity dispersion, D.
But this comes at the expense of increased optical loss and reduced detection sensitivity. The loss in the dispersive
element is therefore the central problem in high sensitivity detection. This implies that a longer integration time
must be used, limiting the axial scan rate. Therefore, the loss in the dispersive element creates a trade-oﬀbetween
the sensitivity and scan rate. Increasing the laser power is not an attractive solution because it can cause damage to
the tissue [25].


## Page 2


2
Mirror
50/50
Coupler
Sample
DCF
Photodetector
Fiber
Collimator
Fiber
Collimator
Pump In/Out
WDM
WDM
Lens
Dispersive
Fourier Transformation
Amplified Dispersive
Fourier Transformation
DCF
Inverse Fourier
Transformation
LASER
Digitizer
Computer
FIG. 1: Schematic of the experimental ampliﬁed dispersive optical tomography (ADOT) system. WDM: wavelength-division
multiplexer; DCF: dispersion compensation ﬁber. The optical source is a mode-locked femtosecond laser with a repetition rate
of 36.6 MHz. It is injected into the Michelson interferometer that contains a mirror and sample. The reﬂections from the
mirror and sample interfere at the 50/50 ﬁber coupler. Each interferometer arm has a DCF module with equal round-trip
dispersion of -1316 ps/nm and loss of 7.6 dB. Dispersive Fourier transformation is performed in the DCF of each arm, mapping
the spectrum into a temporal waveform. The equal dispersion balances the dispersive Fourier transforms in the arms. During
the dispersive Fourier transformation in the sample arm, distributed Raman ampliﬁcation is implemented by pumping it with
two diode lasers with center wavelengths of 1470 nm and 1480 nm. The Raman pumps are injected into and removed from the
DCF by the WDMs. The output of the interferometer is detected by the AC-coupled photodetector with 50 ps response time,
and captured with the 50 GS/s real-time digitizer with 16 GHz bandwidth. Inverse Fourier transformation is performed on the
digitizer output to map the temporal waveform into the depth proﬁle.
Our approach is diﬀerent from previously demonstrated dispersive Fourier-domain OCT through the use of internal
ampliﬁcation in the dispersive element. By compensating for the loss in the dispersive element, it overcomes the trade-
oﬀbetween the imaging sensitivity (and hence the imaging depth) and acquisition speed. For optimum performance,
we perform this function in the sample arm of the Michelson interferometer (Fig. 1) in order to increase the strength of
the signal reﬂected from the sample, which enhances the interference contrast in the interference fringe and improves
the imaging sensitivity. Internal ampliﬁcation in a dispersive element has previously been used to demonstrate real-
time Raman [15] and absorption spectroscopy [21], and a femtosecond digitizer [26].
The desirable features for a dispersive element are high total dispersion, low loss, large optical bandwidth, smooth
dispersion over the bandwidth, and commercial availability. Dispersion compensation ﬁber (DCF) oﬀers an optimum
combination of these parameters and is our preferred choice. While the loss can also be compensated by discrete
optical ampliﬁers (such as erbium-doped ﬁber ampliﬁers, or even semiconductor optical ampliﬁers), distributed Raman
ampliﬁcation within the dispersive DCF is superior because it maintains a relatively constant signal level throughout
the FT process. This important property maximizes the signal-to-noise-and-distortion ratio by keeping the signal
power away from low power (noisy) and high power (nonlinear) regimes. Incidentally, this advantage of distributed
Raman ampliﬁcation over discrete ampliﬁcation is known in long haul ﬁber optic communication links [27]. Raman
ampliﬁcation has another signiﬁcant advantage: in an amorphous medium such as glass, it is naturally broadband.
The gain spectrum can be further tailored by using multi-wavelength pump lasers, and, surprisingly but fortuitously,
extremely broadband gain spectra can be realized using incoherent pump sources [15]. This is highly desirable because
a large optical bandwidth results in high axial image resolution in OCT. Raman-ampliﬁed dispersive elements also
eliminate the need for a high power source, which can potentially cause damage to the sample [25] and unwanted
nonlinear signal distortion [28].
II.
EXPERIMENT
The schematic of the ampliﬁed dispersive optical tomography (ADOT) is shown in Fig. 1. The optical source is a
mode-locked femtosecond laser with 36.6 MHz repetition rate. Its spectrum is shown in Fig. 2. A pulse train with 2.7
kW peak power and 150 fs pulse width is injected into the Michelson interferometer where the reference and sample


## Page 3


3
0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
5
5.5
0
50
100
150
200
250
300
Imaging Depth (mm)
Amplitude (a.u.)
1560 1570 1580 1590 1600 1610
0
0.2
0.4
0.6
0.8
1
Wavelength (nm)
Amplitude (a.u.)
FIG. 2: Basic performance of the ADOT system showing the spectrum of the optical source and single-shot point spread
functions at various imaging depths.
After ﬁltering and ampliﬁcation, a spectrum centered at 1583.8 nm with a FWHM
bandwidth of 15.0 nm is obtained. The axial resolution (227 µm) is limited by the modest bandwidth of the source (15.0 nm)
centered at 1583.8 nm in this proof-of-principle demonstration, but this is not an inherent limitation of the technique, and can
be signiﬁcantly improved using a supercontinuum source which much broader bandwidth as long as temporal pulse overlap
after dispersion does not occur.
arms contain a mirror and sample at their ends, respectively. Each arm has a DCF module with equal round-trip
dispersion of -1316 ps/nm and loss of 7.6 dB. The DCF performs dispersive FT to map the spectrum to a temporal
waveform. The equal dispersion balances the dispersive FTs in the arms. The reﬂections from the sample and mirror
interfere at the 50/50 ﬁber coupler, resulting in a spectral fringe in which the depth proﬁle of the sample is encoded.
Distributed Raman ampliﬁcation is implemented in the DCF by pumping it with two 98.5 mW diode lasers with
center wavelengths of 1470 nm and 1480 nm. The interferometer output is detected by an AC-coupled photodetector
with 50 ps response time and captured with a 50 GS/s real-time digitizer with 16 GHz bandwidth. Inverse FT is
performed on the digitizer output to map the time-domain waveform into the depth proﬁle. The axial scan rate is
equivalent to the repetition rate of the laser (36.6 MHz), which is the highest axial scan speed ever reported. It is
two orders of magnitude faster than conventional OCT [7].
The basic performance of the ADOT is shown in Fig. 2. Single-shot ADOT point spread functions with a mirror
in the sample arm at various imaging depths are evident in the ﬁgure. In this proof-of-principle demonstration, the
axial resolution (227 µm) is limited by the modest bandwidth of the source (15 nm) centered at 1583.8 nm, but
we emphasize that this is not an inherent limitation of the technique, and can be signiﬁcantly improved using a
supercontinuum source which much broader bandwidth. To avoid temporal pulse overlap – after dispersion – this will
also require a proportional reduction in the pulse repetition rate. As an example, a source with 150 nm bandwidth
will give an axial resolution of 22.7 µm (with a theoretical limit of 7.4 µm), while still achieving an axial scan rate of
3.66 MHz.
Fig. 3a shows the single-shot spectrum of an interferometer output pulse (with and without the Raman ampliﬁ-
cation) encoded using a sample with multiple reﬂecting layers. The ampliﬁcation scheme utilizes two diode lasers to
create a uniform Raman gain proﬁle across the signal bandwidth. The ampliﬁcation improves the fringe visibility
of the interferometer, which is otherwise buried in noise. Fig. 3b shows the depth proﬁle obtained by performing
inverse FT on the pulse in Fig. 3a. The, otherwise invisible, depth proﬁle becomes visible due to the ampliﬁcation.
Although signals in both directions (to and from the sample) pass through the ampliﬁer, only the return signal is
eﬀectively ampliﬁed – the incident signal is not ampliﬁed signiﬁcantly because its peak power is much larger than
the pump power supplied to the Raman ampliﬁer. Fig. 4 shows the depth proﬁle of a -26 dB reﬂector at an imaging
depth of 2.8 mm with and without the Raman ampliﬁcation. An improvement in sensitivity by 15 dB is evident in
the ﬁgure, resulting in a SNR increase. Although the Raman gain bandwidth in this system is limited, broadband
Raman ampliﬁcation can be implemented for high-resolution OCT systems through the usage of additional Raman
pump lasers or broadband incoherent pump light [15].
ADOT can be extended to any wavelength band where dispersive elements and Raman pump lasers are available.
Balanced detection [7, 8], which is used to cancel out common-mode noise by diﬀerential measurement of the two


## Page 4


4
0
5
10
15
20
25
−100
0
100
200
300
400
Time (ns)
Amplitude (mV)
Raman Pump Off
Raman Pump On
Wavelength (nm)
1594.8
1590.5
1586.3
1582.1
1577.9
1573.7
−100
0
100
200
300
400
6
6.5
7
7.5
8
8.5
9
9.5
10
10.5
11
−68
−66
−64
−62
−60
−58
−56
−54
−52
−50
−48
Imaging Depth (mm)
Reflectivity (dB)
Detector Noise
Raman Pump Off
Raman Pump On
FIG. 3: Demonstration of the distributed Raman post-ampliﬁcation to boost an, otherwise invisible, weak reﬂection signal. (a)
Single-shot interference spectrum measured on a digital oscilloscope, with and without the Raman ampliﬁcation. The sample
is a partial reﬂector with two layers (both about -60 dB reﬂectivity) at imaging depths of 6.6 mm and 9.1 mm. The spectrum
is mapped into the time-domain waveform by the dispersive Fourier transformation. Raman ampliﬁcation improves the fringe
visibility, which is otherwise invisible. The spikes at 13 ns are due to the reﬂection of the input beam from the 50/50 ﬁber
coupler without going into the interferometer, and can be used as a trigger for the digitizer. The calibrated wavelength axis is
shown above of the ﬁgure. The detector noise without any light incident on it is also shown in the ﬁgure. (b) Depth proﬁle of
the sample obtained by performing inverse Fourier transformation on the pulse with and without the Raman ampliﬁcation. The
depth proﬁle only becomes visible with the ampliﬁcation. Balanced detection [7, 8], which is used to cancel out common-mode
noise by diﬀerential measurement of the two outputs of the 50/50 coupler, can also be incorporated into the ADOT system to
further increase the sensitivity. The sensitivity can also be improved by multi-shot time-integrated detection and averaging.
outputs of the 50/50 coupler, can also be incorporated into ADOT to further increase the imaging sensitivity. The
imaging sensitivity can also be improved by multi-shot time-integrated detection and averaging. Additionally, although
the enhancement factor in sensitivity is limited to 15 dB in this proof-of-principle demonstration, the use of more
powerful Raman pumps or a ﬁber with higher Raman gain coeﬃcient can enhance the sensitivity signiﬁcantly. To the
best of our knowledge, this is the ﬁrst time optical post-ampliﬁcation has been used for improvement in imaging.
III.
ACKNOWLEDGMENTS
This work was partially supported by DARPA. We are grateful to S. Gupta at UCLA for valuable discussions.


## Page 5


5
1
1.5
2
2.5
3
3.5
4
4.5
5
−40
−35
−30
−25
−20
−15
−10
Imaging Depth (mm)
Reflectivity (dB)
  Raman Pump Off
  Raman Pump On
15 dB
FIG. 4: Demonstration of an improvement in sensitivity due to the distributed Raman post-ampliﬁcation. Single-shot depth
proﬁle of a -26 dB reﬂector at an imaging depth of 2.8 mm with and without the Raman ampliﬁcation. An improvement in
sensitivity by 15 dB is evident in the ﬁgure.
IV.
APPENDIX
A.
Theory
As described above, ADOT is based on ampliﬁed dispersive FT where the reﬂection signal from a sample is Raman-
ampliﬁed during dispersive FT. The dispersive FT based on the second-order mode-propagation constant, β2, has
been characterized previously [15]. For large bandwidths (over 100 nm), it is, however, important to include the
higher-order mode-propagation constants. In this case, the mode evolution of a Fourier-domain signal ˜U(0, ω) in an
ampliﬁed dispersive element is given by
U(z, T ) = G
2π
Z ∞
−∞
˜U(0, ω)exp
 i
2β2(ω −ω0)2z + i
6β3(ω −ω0)3z −i(ω −ω0)T

dω,
(1)
where z is the dispersion length, T is measured in a frame of reference moving with the pulse at the group-velocity
vg = 1/β1 and given by T = t−β1z, ω0 is the center frequency of the optical source, ω is the measurement (sideband)
frequency, β3 is the third-order mode-propagation constant, and G is the gain factor (in amplitude) which is assumed
to be constant. If the group-velocity dispersion is large, applying the stationary-phase approximation [15] to Eq. 1
yields
|U(z, T )| ≃G
2π | ˜U(0, ω)|,
(2)
where
ω = ω0 −β2
β3
+
sβ2
β3
2
+ 2T
β3z ≃ω0 + T
β2z −β3T 2
β3
2z2 .
(3)
Eqs. 2 and 3 indicate the transformation of the input spectrum into an ampliﬁed temporal waveform. The approx-
imation holds as 2β3T/β2
2z ≪1, and agrees with the dispersive Fourier transformation with only the second-order
mode-propagation constant considered [15]. The transformation can also be expressed in terms of the dispersion
parameter, D, and its dispersion slope, dD/dλ,
∆T (λ) = D(λ0)z∆λ + 1
2
dD
dλ

λ0
z(∆λ)2,
(4)
where ∆λ = λ −λ0 is the bandwidth of the optical source, λ0 = 2πc/ω0 is the center wavelength, λ = 2πc/ω is the
measurement wavelength, D(λ0) = −2πcβ2/λ2
0 is the dispersion parameter evaluated at λ = λ0, and dD/dλ|λ0 =


## Page 6


6
4πcβ2/λ3
0 + (2πc)2β3/λ4
0 is the dispersion slope evaluated at λ = λ0. In this experiment, D(λ0)z = −1316 ps/nm,
dD/dλ|λ0 z = −0.46 ps/nm2, and ∆λ = 15.0 nm, and therefore, the dispersion slope is of little importance. However,
for optical sources with large bandwidths, the eﬀect of the dispersion slope on the ampliﬁed dispersive FT needs to
be taken into account.
B.
Experimental Details
In our experiment, the light from the femtosecond mode-locked laser (Precision Photonics) is ﬁltered and ampliﬁed
by an erbium-doped ﬁber ampliﬁer (PriTel), and a broadband spectrum with a center wavelength of 1583.8 nm
and a FWHM bandwidth of 15.0 nm is obtained. A variable attenuator (Thorlabs) and a polarization controller
(Precision Photonics) are used in the reference arm to optimize the fringe formed by the reﬂections from the sample
and reference arms. The mirror in the reference arm is placed on a translation stage with a micrometer actuator
(Newport) to adjust time delay between the return pulses in the sample and reference arms. The sample in Fig. 3
consists of a weakly reﬂecting transparent thin ﬁlm and a weakly reﬂecting mirror which is located 2.5 mm apart from
the ﬁlm. The incident light is focused onto the ﬁlm so that the mirror reﬂection coupled back into the ﬁber is about
-60 dB of the light incident on it. The sample in Fig. 4 is also a weakly reﬂecting mirror. The sample is mounted
on a translation stage in the transverse direction. The Raman pumps used to pump the DCF module are diode
lasers (Furukawa) designed for distributed Raman ampliﬁcation in telecommunications systems. The photodetector
is an AD-50ir ampliﬁed photodetector (Newport) with a noise-equivalent-power of 15 pW/
√
Hz. The digitizer is a
DPO71604 oscilloscope (Tektronix).
Based on the group-velocity dispersion of -1316 ps/nm and the digitizer sampling rate of 50 GS/s, the spectral
resolution of the ADOT system is found to be δλ = 30.4 pm (assuming that at least two sampling points are required
to resolve spectra), which corresponds to a depth range of 20.6 mm in air.
[1] Huang, D. et al. Optical coherence tomography. Science 254, 1178–1181 (1991).
[2] Fujimoto, J. G. Optical coherence tomography for ultrahigh resolution in vivo imaging. Nature Biotech. 21, 1361–1367
(2003).
[3] Fercher, A. F., Hitzenberger, C. K., Kamp, G. & El-Zaiat, S. Y. Measurement of intraocular distances by backscattering
spectral interferometry. Opt. Commun. 117, 43–45 (1995).
[4] Swanson, E. A. et al. In vivo retinal imaging by optical coherence tomography. Opt. Lett. 1864–1866 (1993).
[5] Tearney,
G. J. et al.
Optical biopsy in human gastrointestinal
tissue
using optical coherence
tomography.
Am. J. Gastroenterol. 92, 1800–1804 (1997).
[6] Yun, S. H. et al. Comprehensive volumetric optical microscopy in vivo. Nature Med. 12, 1429–1433 (2006).
[7] Adler, D. C. et al. Three-dimensional endomicroscopy using optical coherence tomography. Nature Photon. 1, 709–716
(2007).
[8] Choma, M. A., Sarunic, M. V., Yang, C. & Izatt, J. A. Sensitivity advantages of swept source and Fourier domain optical
coherence tomography. Opt. Express 11, 2183–2189 (2003).
[9] Fercher, A. F., Drexler, W., Hitzenberger, C. K. & Lasser, T. Optical coherence tomography - principles and applications.
Rep. Prog. Phys. 66, 239–303 (2003).
[10] Leitgeb, R., Hitzenberger, C. K. & Fercher, A. F. Performance of Fourier domain vs. time domain optical coherence
tomography. Opt. Express 11, 889–894 (2003).
[11] Yun, S. H., Tearney, G. J., de Boer, J. F., Iftimia, N. & Bouma, B. E. High-speed optical frequency-domain imaging.
Opt. Express 11, 2593–2963 (2003).
[12] Chinn, S. R., Swanson, E. & Fujimoto, J. G. Optical coherence tomography using a frequency-tunable optical source.
Opt. Lett. 22, 340–342 (1997).
[13] Wojtkowski, M. et al. Ultrahigh-resolution, high-speed, Fourier domain optical coherence tomography and methods for
dispersion compensation. Opt. Express 12, 2404–2422 (2004).
[14] Leitgeb, R. et al. Ultrahigh resolution Fourier domain optical coherence tomography. Opt. Express 12, 2156–2165 (2004).
[15] Solli, D. R., Chou, J. & Jalali, B. Ampliﬁed wavelength-time transformation for real-time spectroscopy. Nature Photon.
2, 48–51 (2008).
[16] Fetterman, H. R. et al.
Real-time spectral analysis of far-infrared laser pulses using a saw dispersive delay line.
Appl. Phys. Lett. 34, 123–125 (1979).
[17] Tong, Y. C., Chan, L. Y. & Tsang, H. K. Fibre dispersion or pulse spectrum measurement using a sampling oscilloscope.
Electron. Lett. 33, 983–985 (1997).
[18] Hult, J., Watt, R. S. & Kaminski, C. F.
Dispersion measurement in optical ﬁbers using supercontinuum pulses.
J. Lightwave Technol. 25, 820–824 (2007).


## Page 7


7
[19] Chou, J., Han, Y. & Jalali, B. Time-wavelength spectroscopy for chemical sensing.
IEEE Photon. Technol. Lett. 16,
1140–1142 (2004).
[20] Hult, J., Watt, R. S. & Kaminski, C. F. High bandwidth absorption spectroscopy with a dispersed supercontinuum source.
Opt. Express 15, 11385–11395 (2007).
[21] Chou, J., Solli, D. R. & Jalali, B. Raman ampliﬁed wavelength-time spectroscopy with picometer spectral resolution and
single-shot detection. LEOS. The 20th Annual Meeting of the IEEE 222–223 (2007).
[22] Saperstein, R. E. et al. Processing advantages of linear chirped ﬁber Bragg gratings in the time domain realization of
optical frequency-domain reﬂectrometry. Opt. Express 15, 15464–15479 (2007).
[23] Moon, S. & Kim, D. Y.
Ultra-high-speed optical coherence tomography with a stretched pulse continuum source.
Opt. Express 14, 11575–11584 (2006).
[24] Jackson, J. D. Classical Electrodynamics (Wiley, New York, 1999).
[25] K¨onig, K., So, P. T. C., Mantulin, W. W. & Gratton, E. Cellular response to near-infrared femtosecond laser pulses in
two-photon microscopes. Opt. Lett. 22, 135–136 (1997).
[26] Chou, J., Boyraz, O., Sollli, D. & Jalali, B. Femtosecond real-time single-shot digitizer. Appl. Phys. Lett. 91, 161105–
161107 (2007).
[27] Islam, M. N. Raman ampliﬁers for telecommunications. IEEE J. Sel. Top. Quant. Electron. 8, 548–559 (2002).
[28] Bouma, B. E., Tearney, G. J., Bilinsky, I. P., Golubovic, B. & Fujimoto, J. G. Self-phase-modulated Kerr-lens mode-locked
Cr:forsterite laser source for optical coherence tomography. Opt. Lett. 21, 1839–1841 (1996).

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

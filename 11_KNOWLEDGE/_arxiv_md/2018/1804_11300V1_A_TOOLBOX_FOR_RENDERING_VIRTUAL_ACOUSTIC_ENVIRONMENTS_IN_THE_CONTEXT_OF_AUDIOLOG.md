---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1804.11300v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1804.11300v1_A_toolbox_for_rendering_virtual_acoustic_environments_in_the_context_of_audiolog

> Source: 1804.11300v1_A_toolbox_for_rendering_virtual_acoustic_environments_in_the_context_of_audiolog.pdf

> Pages: 17

---


## Page 1


A toolbox for rendering virtual acoustic environments in the
context of audiology
Giso Grimm1,2,*, Joanna Luberadzka1, Volker Hohmann1,2
1 Medizinische Physik and Cluster of Excellence “Hearing4all”, Department of Medical
Physics and Acoustics, University of Oldenburg, Germany
2 H¨orTech gGmbH, Marie-Curie-Str. 2, 26129 Oldenburg, Germany
* g.grimm@uni-oldenburg.de
Abstract
A toolbox for creation and rendering of dynamic virtual acoustic environments
(TASCAR) that allows direct user interaction was developed for application in hearing
aid research and audiology. This technical paper describes the general software
structure and the time-domain simulation methods, i.e., transmission model, image
source model, and render formats, used to produce virtual acoustic environments with
moving objects. Implementation-specific properties are described, and the
computational performance of the system was measured as a function of simulation
complexity. Results show that on commercially available commonly used hardware the
simulation of several hundred virtual sound sources is possible in the time domain.1
Introduction
Hearing aids are evolving from simple amplifiers to complex signal processing devices.
Current hearing devices typically contain spatially sensitive algorithms, e.g., directional
microphones, direction of arrival estimators, or binaural noise reduction, as well as
automatic classification of the acoustic environment that is used for context-adaptive
processing and amplification [25]. Several of these features cannot be tested in the
current lab-based setups for hearing-aid evaluation, because they employ rather simple
acoustic configurations. Furthermore, it was shown in several studies that hearing aid
performance depends on the spatial complexity of the environment, and that the
hearing aid performance in simple laboratory conditions is not a good predictor of the
performance in more realistic environment or in the real life [36, 13, 6, 9, 24]. Finally,
recent developments in hearing aid technology led to an increased level of interaction
between the user, the environment and the hearing devices, e.g., by means of motion
interaction [39, 40], gaze direction [29] or even with brain-computer interfaces [17].
Thus, for an improved assessment of hearing aid benefit as well as for the development
and evaluation of user interaction techniques, a reproduction of complex listening
environments in the laboratory may be beneficial.
Advances in computer technology in combination with recent multi-channel
reproduction [7, 34, 14] and acoustic simulation methods [3, 31, 42] allow for the
reproduction of virtual acoustic environments in the laboratory. Limitations in
reproduction and simulation quality have been studied in terms of perceptual effects
[8, 22] as well as in terms of technical accuracy of hearing aid benefit prediction [21, 33].
1Parts of this study have been presented at the Linux Audio Conference, Mainz, Germany, 2015.
1
arXiv:1804.11300v1  [cs.SD]  30 Apr 2018


## Page 2


These studies support the general applicability of virtual acoustic environments to
hearing-aid evaluation and audiology, but show that care must be taken in designing the
simulation and reproduction methods, to ensure that the outcome measures are not
biased by the artifacts of the applied methods.
Several further requirements apply when using virtual acoustic environment in
hearing research and audiology. To allow for a systematic evaluation of hearing device
performance, virtual acoustic environments need to be reproducible and scalable in their
complexity. The presence of early reflections and late reverberation in the simulation is
essential for the application of hearing aid evaluation, since both of these factors may
affect hearing aid performance [36]. For assessment of user interaction, but also for the
analysis of hearing aid benefit, simulation of the effects of motion of listeners and
sources might be desired. These effects do not only include time-variant spatial cues,
but also Doppler-shift and time-variant spectral cues due to comb filtering.
Existing virtual acoustic environment engines often target authentic simulations for
room acoustics [19, 32], resulting in a large computational complexity. They typically
render impulse responses for off-line analysis or auralization and thus do not allow
studying motion and user interaction. Other interactive tools, e.g., the
SoundScapeRenderer [1], do not provide all features required here, such as room
simulation and diffuse source handling.
To accommodate the requirements listed above, a toolbox for acoustic scene creation
and rendering (TASCAR) was developed as a Linux audio application [23] with an open
source core [37] and commercial support [38]. The aim of TASCAR is to interactively
render complex and time varying virtual acoustic environments via loudspeakers or
headphones. For a seamless integration into existing measurement tools of
psycho-acoustics and audiology, low-delay real-time processing of external audio streams
in the time domain is applied, and interactive modification of the geometry is possible.
This technical paper aims at describing the general structure of applications in hearing
aid evaluation and audiology, the applied underlying simulation and rendering methods,
and their specific implementation. A measurement of the computational performance
and its underlying factors is provided to allow for an estimation of maximum simulation
complexity in relation to the available computing power. This paper also serves as a
technical reference for the TASCAR open source software (TASCAR/GPL).
General structure
The structure of TASCAR can be divided into four major components (see Figure 1 for
an overview): The audio player (block a in Fig 1) serves as a source of audio signals.
The geometry processor (block b) controls position and orientation of objects over time.
The acoustic model (blocks c) simulates sound propagation, room acoustics and diffuse
sounds. Finally, the rendering subsystem (block d) renders the output of the acoustic
model for a physical reproduction system.
A virtual acoustic environment in TASCAR is defined as a space containing several
types of objects: point sources (e.g., speakers, distinct noise sources), diffuse sources
(e.g., remote traffic, babble noise), receivers (e.g., dummy head), reflectors (e.g.,
boundaries of a room) and obstacles. Source objects are provided with the audio
content, delivered either by the internal audio player module, or externally e.g., from
physical sources, audiological measurement tools, or digital audio workstations (DAW).
Objects in the virtual acoustic scene can change their positions and orientations over
time. Information about the object geometry at a given time is taken either from
sampled trajectories, from algorithmic trajectory generators, or from external devices,
e.g., a joystick or head-motion tracker (interactive controller of an object’s movement,
e.g., motion of a dummy head).
2


## Page 3


Fig 1. The major components of TASCAR are the audio player (a), the
geometry processor (b), the acoustic model (c) and the rendering
subsystem (d). Point sources and diffuse sources are the interface between
the audio player and the acoustic model. Receivers are the interface
between the acoustic model and the rendering subsystem.
Geometry information is exploited in the acoustic model to modify the input audio
signals delivered by the audio player. Modifications performed by the acoustic model
mimic basic acoustic properties like distance law, reflections and air absorption. The
resulting sound corresponds to the time-variant spatial arrangement of the objects in
the virtual scene. Geometry data can also be exchanged with external modules, e.g.,
game engines, to make the visualization consistent with the acoustic scene content.
At the final stage of the acoustic model, there is a receiver model, which encodes the
modified signals into a receiver type specific render format, used subsequently by the
rendering subsystem for the reproduction of the simulated environment on a physical
reproduction system.
Simulation methods
Geometry processing
Each object in a virtual acoustic environment is determined by its position p(t) and
orientation Ω(t) in space at a given time t. Position is defined in Cartesian coordinates
p = (px, py, pz), and orientation is defined in the Euler angles, Ω= (Ωz, Ωy, Ωx), where
Ωz is the rotation around the z-axis, Ωy around the y-axis and Ωx around the x-axis.
Trajectories Γ for a moving object are created by specifying the position and
orientation for more then one point in time:
Γp
=
{p(t1), p(t2), p(t3), . . . }
ΓΩ
=
{Ω(t1), Ω(t2), Ω(t3), . . . } ,
where t1, t2, · · · ∈R are the sampling times of the trajectory. The time variant position
p(t) is linearly interpolated between sample times of Γp, either in Cartesian coordinates,
3


## Page 4


or in spherical coordinates relative to the origin, respectively. The time variant
orientation Ω(t) is linearly interpolated from ΓΩ, in Euler-coordinates. To apply the
orientation to objects, a rotation matrix O is calculated from the Euler coordinates.
Acoustic model
For each sound source object k, the acoustic model modifies its associated original
source signal x(t) delivered by the audio player using geometry data into an output
signal y(t) that is then used as input signal to a receiver. The performed computations
simulate basic acoustic phenomena as described below. Signals y(t) serve at the
subsequent stage to calculate the output of a receiver (see Section on render formats
below).
The acoustic model consists of the source model (omni-directional or
frequency-dependent directivity), the transmission model simulating sound propagation,
an image source model, which depends on the reflection properties of the reflecting
surfaces as well as on the ‘visibility’ of the reflected image source, and a receiver model,
which encodes the direction of the sound source relative to the receiver into an receiver
output for further processing by the rendering subsystem.
Image source model
Early reflections are generated with a geometric image source model, i.e., reflections are
simulated for each reflecting plane surface with polygon-shaped boundary by placing an
image source at the position of the reflection. Each image source is rendered in the time
domain, in the same way as primary sources. This is different to the more efficient
“shoe-box” image source models commonly used in room acoustic simulations [3], which
calculate impulse responses by solving the wave equations. For a first order image
source model, each pair of primary source and reflector face creates an image source,
where the plane on which the reflector lies is a symmetry axis between the primary and
image source (see Fig 2). The image source position pimg is determined by the closest
point on the (infinite) reflector plane pcut to the source psrc: pimg = 2pcut −psrc.
For higher order image source models, lower order image sources are treated as
primary sources leading to higher order image sources.
The image source position itself is independent of the receiver position. However, for
finite reflectors there are two types of reflections in TASCAR, and depending on the
receiver position it is determined which reflection type is executed (see Fig 2). If the
intersection point pis of the line connecting the image source with the receiver and the
reflector plane lies within the reflector boundaries, the image source is ‘visible’ in the
reflector, and a ‘specular’ reflection is applied. If pis is not within the reflector
boundaries, the source is ‘invisible’ from a receiver perspective and the ‘edge reflection’
is applied. For ‘edge’ reflections, the apparent image source position is shifted so that
the distance between the source and receiver remains unchanged, whereas the receiver,
edge of the reflector and the apparent source position form one line (see Fig 2, right
panel). The angle θ by which the image source is shifted to create effective image source
controls a soft-fade gain by which the source signal is multiplied g:
g = cos(θ)κ
(1)
The coefficient κ = 2.7 was chosen for a rough approximation of diffraction of
speech-shaped signals and medium-sized reflectors. If a receiver or a sound source are
behind the reflector, the image source is not rendered. A reflector object has only one
reflecting side in the direction of the face normal.
To simulate the reflection properties of a reflector object, the source signal is filtered
with a first order low pass filter determined by a reflectivity coefficient ρ, and a
4


## Page 5


Fig 2. Schematic sketch of the image model geometry. Left panel:
‘specular’ reflection, i.e., the image source is visible within the reflector;
right panel: ‘edge’ reflection.
damping coefficient δ, which can be specified for each reflector object:
y(t) = δy(t −f −1
s
) + ρx(t).
(2)
In room acoustics material properties are commonly defined by frequency dependent
absorption coefficients α(f). These can be calculated from the reflection filter
coefficients ρ and δ by
α(f) =

1 −
ρ
1 −δ
1 −δe−i2πff −1
s

2
.
(3)
The filter coefficients ρ and δ can be derived from frequency dependent absorption
coefficients by minimization of the mean-square error between desired ˜α(f) and α(f)
derived from the filter coefficients.
Source directivity
For the simulation of source directivity, the receiver position relative to the source
prec,rel = O−1
src(prec −psrc)
(4)
is calculated. Frequency-dependent directivity with omni-directional characteristics at
low frequencies and higher directivity at high frequencies is achieved by controlling a
low-pass filter by the angular distance between the receiver and the source direction.
The normalized relative receiver position ˜prec,rel is
˜prec,rel =
prec,rel
||prec,rel||
(5)
The cosine of the angular distance is then ˜px,rec,rel. The cut-off frequency f6dB defines
the frequency, for which −6 dB at ±90 degrees are achieved. With ξ = πf6dB/fs
log(2) , a first
5


## Page 6


order low-pass filter with the recursive filter coefficient clp,
clp =
1
2 −1
2 ˜px,rec,rel
ξ(fcut)
,
(6)
is applied to the signal, to achieve the frequency-dependent directivity, or in other
words, the direction-dependent frequency characteristics.
Transmission model
The transmission model simulates the delay, attenuation and air absorption, which
depend on the distance r(t) between the sound source (primary or image source) and
the receiver, as well as attenuation, caused by obstacles between source and receiver.
Point sources follow a 1/r sound pressure law, i.e., doubling the distance r results in
half of the sound pressure. Air absorption is approximated by a simple first order
low-pass filter model with the filter coefficient a1 controlled by the distance:
a1 = e−r(t)fs
cα ,
(7)
where fs is the sampling frequency and c the speed of sound. The empiric constant
α = 7782 was manually adjusted to provide appropriate values for distances below 50
meters. This approach is very similar to that of [27] who used an FIR filter to model
the frequency response at certain distances. However, in this approach the distance
parameter r can be varied dynamically. The distance dependent part of the
transmission model without obstacles can then be written as
y(t) = a1y(t −f −1
s
) + (1 −a1)x(t −r(t)c−1)
r(t)
,
(8)
where x(t) is the source signal at time t, and y(t) is the output audio signal of the
transmission model. The time-variant delay line uses either nearest neighbor
interpolation or sinc interpolation, depending on the user needs and computational
performance of the computing system.
Obstacles are modeled by plane surfaces with polygon-shaped boundaries. The
acoustic signal is split into a direct path, which is attenuated by the obstacle-specific
frequency-independent attenuation ao, and an indirect path, to which a simple
diffraction model is applied. The diffracted path is filtered with a second order low pass
filter which is controlled by the shortest path from the source via the obstacle boundary
to the receiver. With the angle θo between the connection from the intersection point of
the shortest path with the obstacle boundary to the source position, and the connection
from the receiver position to the intersection point, the cut-off frequency of the low-pass
filter is
fo = 3.8317
c
2πa sin(θo),
(9)
with the aperture a = 2
p
A/π defined as the radius of a circle with the same area A as
the obstacle polygon. This simple diffraction model is based on the diffraction on the
boundary of a circular disc [2], however, position-dependent notches are not simulated.
The diffracted signal is weighted with 1 −ao and added to the attenuated signal.
Diffuse sources
Sound sources with lower spatial resolution, e.g., diffuse background noise or diffuse
reverberation [42], are added in first order Ambisonics (FOA) format. No distance law
is applied to these sound sources; instead, they have a rectangular spatial range box,
6


## Page 7


i.e., they are only rendered if the receiver is within their range box, with a von-Hann
ramp at the boundaries of the range box. Position and orientation of the range box can
vary with time. The size of the range box is typically adjusted to match the dimension
of the simulated room. The diffuse source signal is rotated by the difference between
box orientation and receiver orientation.
Diffuse reverberation is not simulated in TASCAR. To use diffuse reverberation, the
input signals of the image source model can be passed to external tools which return
FOA signals, e.g., feedback-delay networks or convolution with room impulse responses
in FOA format [12]. A smooth transition between early reflections from the image
source model and diffuse reverberation based on room impulse responses can be
achieved by removing the first reflections from the impulse responses. To account for
position-independent late reverberation, room receivers can render independent from
the distance between source and receiver, e.g., the transmission model can be replaced
by a room-volume dependent fixed gain.
Receiver model
The interface between the acoustic model and the rendering subsystem is the receiver.
A receiver renders the output of the transmission model depending on the relative
position and orientation between receiver and sound source. Signals from the
transmission models belonging to all sound sources are summed up after
direction-dependent processing. The render format determines the number of channels
and the method of encoding the relative spatial information into a multi-channel audio
signal. The output signal of a receiver is
z(t) = (z1 (t) , z2 (t) , . . . , zN (t)) .
(10)
The receiver functionality can be split into the panning or directional encoding of
primary and image sources y(t), and the decoding of diffuse source signals f(t) in first
order Ambisonics format with Furse-Malham normalization (’B-format’):
z(t) =
K
X
k=1
w(prel,k)yk(t)
|
{z
}
panning
+
L
X
l=1
D ˆO−1
recfl(t)T
|
{z
}
diffuse decoding
(11)
In the panning part, the driving weights w = (w1, w2, . . . , wN) depend on the direction
of the relative source position in the receiver coordinate system,
prel,k = O−1
rec (pk −prec); Orec is the receiver orientation matrix, and pk is the position
of the k-th sound source. yk(t) is the output signal of the transmission model, i.e., it
contains the distance-dependent gain, air absorption and obstacle attenuation, for the
k-th source; K is the number of all primary and image point sources.
In the diffuse decoding part, D is the receiver-type specific first order Ambisonics
decoding matrix for the w, x, y and z channels of the first order Ambisonics signal,
D =



d1,w
d1,x
d1,y
d1,z
...
...
...
...
dn,w
dn,x
dn,y
dn,z


,
and ˆO−1
recis the rotation matrix for first order Ambisonics signals, to compensate the
receiver orientation. fl is the first order Ambisonics signal of the l-th diffuse source,
rotated by the source orientation; L is the number of all diffuse sources, including
diffuse reverberation inputs.
7


## Page 8


Render formats
The render formats of TASCAR can be divided into three categories: Virtual
microphones simulate the characteristics of microphones. They primarily serve as a
sensor in a virtual acoustic environment. Speaker-based receiver types render signals
which can drive real or virtual loudspeakers, used for auralization of virtual scenes.
Ambisonics receiver types render the scenes to first, second or third order Ambisonics
format, which can be rendered to virtual microphones, loudspeakers or other
reproduction methods using external decoders. Receivers can render either for
three-dimensional reproduction or for two-dimensional reproduction. In both cases, the
directional information of the relative source position is encoded in the normalized
relative source position,
˜prel =
prel
||prel||.
(12)
However, in the two-dimensional case prel is projected onto x, y-plane before the
normalization by setting its z-component to zero. In both cases, the acoustic model,
containing all distance-dependent effects, and the image source model are calculated
based on the three-dimensional relative source position.
Virtual microphones
The virtual microphone receiver type has a single output channel. The driving weight is
w = 1 + a(˜prel,x −1).
(13)
It’s directivity pattern can be controlled between omni-directional and figure-of-eight
with the directivity coefficient a; with a = 0 this is an omni-directional microphone,
with a = 1
2 a standard cardioid, and with a = 1 a figure-of-eight. The diffuse decoding
matrix is
D =
√
2(1 −a)
a
0
0

.
(14)
The factor
√
2 of the w-channel is needed to account for the Furse-Malham
normalization of the diffuse signals.
Speaker-based render formats
This class of render formats contains all types which render the signals directly to a
loudspeaker array. The number N and position sn of speakers can be user-defined; ˜sn is
the normalized speaker position. A measure of angular distance between a source and a
loudspeaker is dn = 1 −˜sn˜pT
rel. The most basic speaker-based receiver type is nearest
speaker panning (NSP). The driving weights are:
wn =
 1
n = arg min{dn}
0
otherwise
(15)
Another commonly used speaker-based render format is two-dimensional vector-base
amplitude panning (VBAP) [34]. The two speakers n1 and n2 which are closest to the
source are chosen. A gain vector (gn1, gn2)T based on the normalized speaker positions
and the normalized relative source position in the x, y-plane is defined:
 gn1
gn2

=
 ˜sn1,x
˜sn2,x
˜sn1,y
˜sn2,y
−1  ˜prel,x
˜prel,y

(16)
Then the driving weights are
 wn1
wn2

=
1
p
g2n1 + g2n2
 gn1
gn2

.
(17)
8


## Page 9


For ambisonic panning with arbitrary order, the signal of each source is encoded into
horizontal Ambisonics format (HOA2D). Decoding into speaker signals is applied after a
summation of the signals across all sources. In the decoder, the order gains can be
configured to form a ’basic’ decoder or a ’max rE’ decoder [14]. An equal circular
distribution of loudspeakers is assumed for this render format. Although this receiver
applies principles of Ambisonics, it is a speaker-based receiver, because encoding and
decoding is combined.
All speaker based receiver types use a max rE first-order Ambisonics decoder for
decoding of diffuse sounds:
D = 1
N



√
2
g˜s1,x
g˜s1,y
g˜s1,z
...
...
...
...
√
2
g˜sn,x
g˜sn,y
g˜sn,z


.
(18)
g is the decoder type dependent gain; for max rE this is g =
1
√
2 in the two-dimensional
case and g =
1
√
3 in the three-dimensional case [14].
Ambisonics-based receivers
First, second and third order receiver types were implemented. They follow the channel
sequence and panning weight definition of the Ambisonics Association [4], using
Furse-Malham normalization. The Ambisonics-based receivers encode plane waves, i.e.,
they do not account for near-field effects. For two-dimensional encoding, all output
channels which are zero, wn ≡0, are discarded.
Binaural rendering
Binaural signals and multi-channel signals for hearing aid microphone arrays
ˆz = (ˆz1, . . . , ˆzm) are generated by rendering to a virtual loudspeaker array, i.e., using a
speaker-based render format, and applying a convolution of the loudspeaker signals zn
with the corresponding head-related impulse responses (HRIRs) hn,m for the respective
loudspeaker directions. The HRIRs can be either recorded (e.g., [28, 41]) or modeled
[18].
Implementation
The implementation of TASCAR utilizes the Jack Audio Connection Kit [16], a tool for
real-time audio routing between different pieces of software, and between software and
audio hardware. The audio content is transferred between different components of
TASCAR via JACK input and output ports. The JACK time-line is used as a base of
all time-varying features, for data logging and as a link to the time-line of external tools.
The audio signals are processed in blocks. Time-variant geometry and the dependent
simulation coefficients, e.g., delay, air absorption filter coefficients or panning weights,
are updated at the block boundaries. The simulation coefficients are linearly
interpolated between the boundaries. This approximation by linear interpolation might
be inaccurate if the simulation coefficients vary non-linearly within a block, e.g.,
panning weights during fast lateral movements.
Render formats and algorithmic trajectory generators are implemented as modules.
Object properties, like geometry data, reflection properties and gains, and the time-line
can be controlled interactively via a network interface.
To achieve parallel processing in TASCAR, virtual acoustic environments can be
separated into multiple scenes. Independent scenes can be processed in parallel.
9


## Page 10


Table 1. Parameter space of the performance measurements.
Factor
Values
number of sources K
1, 10, 100, 256
number of output channels N
8, 48, 128
block size P
64, 256, 1024 samples
maximum delay line length ld
1 m, 10 km
render format
NSP, VBAP, HOA2D
CPU model
i5-2400@3.1GHz
i5-6300HQ@2.3GHz
i5-6500@3.2GHz
i7-7567U@3.5GHz
AMD FX-4300@3.8GHz
AMD Ryzen 71700
Feedback signal paths, e.g., caused by room coupling or external reverberation, are
possible, but will lead to an additional block of delay. The delay and processing order of
scenes is managed by the JACK audio back-end.
Performance measurements
For a rough estimation of the factors of computational complexity in TASCAR, the
CPU load was measured as a function of several relevant factors. The performance
measurements were done with version 0.169 of TASCAR. All underlying render tools are
part of the TASCAR repository [37].
Methods
CPU load C caused by audio signal processing was assessed using the ’clock()’ system
function, after processing 10 seconds of white noise in each virtual sound source. The
number of primary sources K, number of output channels N, block size P, maximum
length of delay lines ld and the render format was varied (see Table 1 for an overview of
the parameter space). No image sources were processed, i.e., all simulated sources were
primary sources, and no reflectors were used during the performance measurements.
Each measurement of a combination of K, N, P, ld and render format was repeated
twice. The CPU load C is time per cycle τP in samples divided by length of cycle P in
samples.
Number of sources and number of output channels are directly related to the
numerical complexity in the receiver module. The block size controls the frequency of
the geometry update. Memory usage is mainly affected by the maximum delay line
length. One delay line is allocated in memory for each sound source. At 44.1 kHz
sampling rate, the memory usage of the delay lines is 520 Bytes per meter and source.
Different render formats may differ in their numerical complexity.
Results
A one-way analysis of variances revealed that at all tested factors except for the delay
line length and repetition showed a significant influence on the τP at a significance level
of p = 0.05. Thus, in the following analysis the data was averaged across ld and
repetitions.
To provide an estimation of the contribution of different factors to the numerical
complexity, a model function based on the implementation was fitted to the measured
10


## Page 11


data:
τP =
a0
|{z}
overhead
+
a1K
|{z}
geometry
+
a2KP
| {z }
source audio
+ a3NP
| {z }
postproc.
+ a4NKP
|
{z
}
panning
.
(19)
In this model, a0 represents the overhead by framework which is not related to the
simulation properties. a1 is an estimate of geometry processing time, which is
performed for each source, but not depending on the number of audio samples per
processing block P. The factor a2 is related to source audio processing time per sample
in the transmission model, and the processing time spent in the receiver, which does not
depend on the number of speakers. a3 is an estimate of the post processing time per
audio sample in the receiver, which does not depend on the number of sources. a4 is
time per audio sample for each loudspeaker and sound source, i.e., time spent in the
panning function of the render format. The model parameters were found by minimizing
the mean-square error between the measured and predicted CPU load C, and are shown
in Table 2. An example data set for one architecture and receiver type is shown in Fig 3.
Fig 3. Example CPU load (i7-7567U@3.5GHz, HOA2D receiver, P = 1024):
Measured data (symbols) with model fit (Eq (19), gray solid lines), for
N = 8 speakers (diamonds), N = 48 speakers (circles) and N = 128 speakers
(squares). Vertical dashed lines indicate the maximum possible number of
sources, Eq (20), for the given hardware.
It is often required to estimate the maximum number of sound sources K for a given
CPU, render format and loudspeaker setup (affecting N) and latency constraint
(affecting P). Eq (19) can be transformed to
Kmax ≤C −a0P −1 −a3N
a1P −1 + a2 + a4N .
(20)
As an example, Kmax was calculated for all tested combinations of CPU model and
receiver type, for C = 90% and P = 1024. These results are given in the last two
columns of Table 2, for N = 8 and N = 48.
The results show that on CPU models which are commonly used at the time of
writing, several hundred sound sources can be simulated. From the tested render
formats, ’HOA2D’ was most efficient, especially for larger values of N. These results
11


## Page 12


Table 2. Results of the model fits of CPU load measurement.
CPU
format
a0
a1
a2
a3
a4
Kmax,8
Kmax,48
i5-2400
NSP
0.045
0.017
0.001
0.00052
7.8e-05
541
182
@3.1GHz
VBAP
0.41
0.093
0.00036
0.00051
8.1e-05
812
201
HOA2D
0.52
0.02
0.001
0.00088
4.1e-05
662
288
i5-6300HQ
NSP
0.028
0.0051
0.0011
0.00043
6.3e-05
548
210
@2.3GHz
VBAP
0.019
0.062
0.00059
0.00046
7e-05
742
220
HOA2D
2.1e-06
0.016
0.0011
0.00069
3.7e-05
636
302
i5-6500
NSP
0.057
0.0034
0.001
0.00038
5.6e-05
615
238
@3.2GHz
VBAP
0.021
0.059
0.00053
0.00042
6.2e-05
825
246
HOA2D
0.066
0.014
0.00098
0.00062
3.2e-05
714
341
i7-7567U
NSP
0.099
0.0046
0.00077
0.00036
4.6e-05
790
298
@3.5GHz
VBAP
0.036
0.071
0.00014
0.00033
5.2e-05
1443
329
HOA2D
0.096
0.014
0.0008
0.00053
2.7e-05
868
410
AMD FX-4300
NSP
0.099
1.8e-09
0.00019
3.2e-05
0.00021
490
89
@3.8GHz
VBAP
1.4e-09
0.28
0.0012
3e-14
0.00017
316
93
HOA2D
0.056
0.019
0.0016
0.0011
4.5e-05
441
221
AMD Ryzen 71700
NSP
1.1e-06
0.015
0.00087
0.00046
6e-05
661
234
@3.6GHz
VBAP
0.46
0.065
0.00027
0.00029
6.5e-05
1058
258
HOA2D
0.064
0.016
0.00083
0.00061
3.6e-05
789
339
take only a single core into account. On multi-core computers, more complex
environments can be simulated by splitting them into multiple environments of lower
complexity, and rendering them in parallel.
Validation and applications
The proposed simulation tool is based on established render formats, such as VBAP [34]
or HOA [14]. The physical and perceptual properties of these render methods have been
extensively studied [30, 15, 11, 35, 1, 5, 8]. The limitations for applications in hearing
aid evaluation differ from perceptual limitations [21]. They depend on the sensitivity of
hearing aid algorithms and the applied hearing aid performance measures on spatial
aliasing artifacts of the render methods. Thus the optimal render method depends on
the context of a specific application of the proposed simulation tool. Based on the data
by [21], a specific TASCAR scene can be designed such that it meets the requirements
of an application-specific receiver, e.g., a human head with two-microphone hearing aids
on each ear.
Distance perception in human listeners is believed to be dominated by the
direct-to-reverberant ratio [10]. In the proposed simulation tool with a simple image
source model and position-independent externally generated late reverberation, the
distance perception may depend on simulation parameters. Thus, in a previous study
the distance perception and modeling with room-acoustic parameters in simulations
with TASCAR was evaluated [22]. It was shown in a comparison of binaural recordings
in a real room and a simulation of the same geometry that in the simulation a distance
perception similar to real rooms can be achieved.
An overview over a number of possible applications is shown in Fig 4. The simplest
application of TASCAR is to play back a pre-defined virtual acoustic environment via
multiple loudspeakers (Fig 4.a). For subjective audiological or psycho-acoustic
measurements in virtual acoustic environments, without hearing aids or aided with
conventional hearing aids, the audio input of virtual sound sources can be provided by
external measurement tools (Fig 4.b). TASCAR can also be applied to assess hearing
12


## Page 13


aid (HA) performance in simulated virtual environments, based on instrumental
measures, or with human listeners, e.g., in combination with the open Master Hearing
Aid (openMHA) [26]. Subjective or instrumental evaluation of research hearing aids can
be performed by feeding the output of the virtual acoustic environment directly to the
inputs of a research hearing aid [20] (Fig 4.c). An example study of this use case can be
found in [24], where hearing aid performance in eight different virtual acoustic
environments of different spatial complexity was assessed. Test stimuli as well as the
configuration of virtual acoustic environment and the research hearing aid can be
controlled from the measurement platform, e.g., MATLAB or GNU/Octave (Fig 4.d).
Motion data can also be recorded from motion sensors or controllers, to interact with
the environment in real-time, or for data logging (Fig 4.e).
Fig 4. Example applications of TASCAR and its interaction. Solid arrows
indicate audio signals, dashed arrows represent control information, e.g.,
geometry data.
These use cases serve as an illustration of typical applications of TASCAR. The
interfaces of TASCAR allow for a large number of applications.
Summary and conclusions
In this technical paper, a toolbox for creation and rendering of dynamic virtual acoustic
environments (TASCAR) was described, which allows direct user interaction. This tool
was developed for application in hearing aid research and audiology. The three main
modules of TASCAR - audio player, geometry processor and acoustic model - form the
simulation framework. The audio player provides the tool with audio signals, the
geometry processor keeps track of the distribution of the objects in the virtual space,
and the acoustic model performs the room acoustic simulation and renders the scene
into a chosen output format. The simulation uses a transmission model and a geometric
image source model in the time domain, to allow for interactivity, and for a simple
physical model of motion-related acoustic properties, such as Doppler shift and comb
filtering effects. TASCAR allows selecting from a number of various rendering formats,
customized to the needs of a range of applications, including higher order Ambisonics
and binaural rendering formats.
Performance measurements quantify the influence of factors related to simulation
complexity. The results show that, despite some limitations in terms of complexity of
the virtual acoustic environment, several hundred virtual sound sources can be
interactively rendered, even over huge reproduction systems and on consumer-grade
render hardware.
It can be concluded that the proposed tool is suitable for hearing aid evaluation. It
offers a set of features, e.g., dynamic time-domain geometric image source model, diffuse
13


## Page 14


source handling, directional sources, which is to current knowledge unique in this
combination.
Acknowledgments
This study was funded by the German Research Council DFG FOR1732.
References
1. J. Ahrens and S. Spors. An analytical approach to sound field reproduction using
circular and spherical loudspeaker distributions. Acta Acustica united with
Acustica, 94(6):988–999, 2008.
2. G. B. Airy. On the diffraction of an object-glass with circular aperture.
Transactions of the Cambridge Philosophical Society, 5:283, 1835.
3. J. B. Allen and D. A. Berkley. Image method for efficiently simulating small-room
acoustics. The Journal of the Acoustical Society of America, 65:943, 1979.
4. Ambisonics Association. Ambisonic standards, 2008. URL
http://ambisonics.ch/. Accessed 2015.
5. E. Benjamin, A. Heller, and R. Lee. Why ambisonics does work. In Audio
Engineering Society Convention 129, 11 2010. URL
http://www.aes.org/e-lib/browse.cfm?elib=15664.
6. R. A. Bentler. Effectiveness of directional microphones and noise reduction
schemes in hearing aids: A systematic review of the evidence. Journal of the
American Academy of Audiology, 16(7):473–484, 2005. doi:
doi:10.3766/jaaa.16.7.7.
7. A. J. Berkhout, D. de Vries, and P. Vogel. Acoustic control by wave field
synthesis. The Journal of the Acoustical Society of America, 93(5):2764–2778,
1993. doi: 10.1121/1.405852.
8. S. Bertet, J. Daniel, E. Parizet, and O. Warusfel. Investigation on localisation
accuracy for first and higher order ambisonics reproduced sound sources. Acta
Acustica united with Acustica, 99(4):642–657, 2013.
9. V. Best, G. Keidser, J. M. Buchholz, and K. Freeston. An examination of speech
reception thresholds measured in a simulated reverberant cafeteria environment.
International Journal of Audiology, (0):1–9, 2015.
10. A. W. Bronkhorst and T. Houtgast. Auditory distance perception in rooms.
Nature, 397(6719):517–520, 1999.
11. K. Carlsson. Objective Localisation Measures in Ambisonic Surround-sound. PhD
thesis, Master Thesis in Music Technology, Supervisor: Dr. Damian Murphy.
Department of Speech, Music and Hearing, Royal Institute of Technology,
Stockholm. Work carried out at Dept. of Electronics University of York, 2004.
12. A. J. Chadwick and S. Shelley. Openair lib impulse response database.
http://www.openairlib.net/, 2015. Audio Lab, University of York.
14


## Page 15


13. M. Cord, R. Surr, B. Walden, and O. Dyrlund. Relationship between laboratory
measures of directional advantage and everyday success with directional
microphone hearing aids. Journal of the American Academy of Audiology, 15(5):
353–364, 2004.
14. J. Daniel. Repr´esentation de champs acoustiques, application `a la transmission et
`a la reproduction de sc`enes sonores complexes dans un contexte multim´edia. PhD
thesis, Universit´e Pierre et Marie Curie (Paris VI), Paris, 2001.
15. J. Daniel, R. Nicol, and S. Moreau. Further investigations of high-order
ambisonics and wavefield synthesis for holophonic sound imaging. In Audio
Engineering Society Convention 114, March 2003.
16. P. Davis and T. Hohn. Jack audio connection kit. In Proceedings of the Linux
Audio Developer Conference. ZKM Karlsruhe, 2003.
17. M. De Vos, K. Gandras, and S. Debener. Towards a truly mobile auditory
brain–computer interface: exploring the p300 to take away. International journal
of psychophysiology, 91(1):46–53, 2014.
18. R. O. Duda. Modeling head related transfer functions. In Signals, Systems and
Computers, 1993. Conference Record of The Twenty-Seventh Asilomar
Conference on, pages 996–1000. IEEE, 1993.
19. EASE. Ease. http://ease.afmg.eu/.
20. G. Grimm, T. Herzke, D. Berg, and V. Hohmann. The Master Hearing Aid – a
PC-based platform for algorithm development and evaluation. Acta Acustica
united with Acustica, 92:618–628, 2006.
21. G. Grimm, S. Ewert, and V. Hohmann. Evaluation of spatial audio reproduction
schemes for application in hearing aid research. Acta Acustica united with
Acustica, 101(4):841–854, 2015. doi: 10.3813/AAA.918878.
22. G. Grimm, J. Heeren, and V. Hohmann. Comparison of distance perception in
simulated and real rooms. In Proceedings of the International Conference on
Spatial Audio, Graz, 2015.
23. G. Grimm, J. Luberadzka, T. Herzke, and V. Hohmann. Toolbox for acoustic
scene creation and rendering (tascar): Render methods and research applications.
In F. Neumann, editor, Proceedings of the Linux Audio Conference, Mainz,
Germany, 2015. Johannes-Gutenberg Universit¨at Mainz.
24. G. Grimm, B. Kollmeier, and V. Hohmann. Spatial acoustic scenarios in
multichannel loudspeaker systems for hearing aid evaluation. Journal of the
American Academy of Audiology, 27(7):557–566, 2016.
25. V. Hamacher, J. Chalupper, J. Eggers, E. Fischer, U. Kornagel, H. Puder, and
U. Rass. Signal processing in high-end hearing aids: state of the art, challenges,
and future trends. EURASIP Journal on Applied Signal Processing, 2005:
2915–2929, 2005.
26. T. Herzke, H. Kayser, F. Loshaj, G. Grimm, and V. Hohmann. Open signal
processing software platform for hearing aid research (openMHA). In Proceedings
of the Linux Audio Conference, pages 35–42. Universit´e Jean Monnet,
Saint-´Etienne, 2017.
15


## Page 16


27. J. Huopaniemi, L. Savioja, and M. Karjalainen. Modeling of reflections and air
absorption in acoustical spaces a digital filter design approach. In Workshop on
Applications of Signal Processing to Audio and Acoustics (WASPAA). IEEE,
1997.
28. H. Kayser, J. Anem¨uller, T. Rohdenburg, V. Hohmann, B. Kollmeier, et al.
Database of multichannel in-ear and behind-the-ear head-related and binaural
room impulse responses. EURASIP Journal on Advances in Signal Processing,
2009.
29. G. Kidd Jr, S. Favrot, J. G. Desloge, T. M. Streeter, and C. R. Mason. Design
and preliminary testing of a visually guided hearing aid. The Journal of the
Acoustical Society of America, 133(3):EL202–EL207, 2013.
30. C. Landone and M. Sandler. Issues in performance prediction of surround
systems in sound reinforcement applications. In Proceedings of the 2nd COST
G-6 Workshop on Digital Audio Effects (DAFx99), Norwegian University of
Science and Technology, Trondheim, Norway, December 1999.
31. T. Lentz, D. Schr¨oder, M. Vorl¨ander, and I. Assenmacher. Virtual reality system
with integrated sound field simulation and reproduction. EURASIP Journal on
Applied Signal Processing, 2007(1):187–187, 2007.
32. G. M. Naylor. Odeon—another hybrid room acoustical model. Applied Acoustics,
38(2-4):131–143, 1993.
33. C. Oreinos and J. M. Buchholz. Objective analysis of ambisonics for hearing aid
applications: Effect of listener&apos;s head, room reverberation, and directional
microphones. The Journal of the Acoustical Society of America, 137(6):
3447–3465, 2015. doi: http://dx.doi.org/10.1121/1.4919330. URL http://
scitation.aip.org/content/asa/journal/jasa/137/6/10.1121/1.4919330.
34. V. Pulkki. Virtual sound source positioning using vector base amplitude panning.
J. Audio Eng. Soc, 45(6):456–466, 1997.
35. V. Pulkki and T. Hirvonen. Localization of virtual sources in multichannel audio
reproduction. Speech and Audio Processing, IEEE Transactions on, 13(1):
105–119, 2005.
36. T. Ricketts. Impact of noise source configuration on directional hearing aid
benefit and performance. Ear and Hearing, 21(3):194–205, 2000.
37. TASCAR/GPL. Tascar/gpl. https://github.com/gisogrimm/tascar.
38. TASCAR/H¨orTech. Tascar/h¨ortech.
http://www.hoertech.de/en/f-e-products/tascarpro.html.
39. B. Tessendorf, A. Bulling, D. Roggen, T. Stiefmeier, M. Feilner, P. Derleth, and
G. Tr¨oster. Recognition of hearing needs from body and eye movements to
improve hearing instruments. In Pervasive Computing, pages 314–331. Springer,
2011.
40. B. Tessendorf, A. Kettner, D. Roggen, T. Stiefmeier, G. Tr¨oster, P. Derleth, and
M. Feilner. Identification of relevant multimodal cues to enhance context-aware
hearing instruments. In Proceedings of the 6th International Conference on Body
Area Networks, pages 15–18. ICST (Institute for Computer Sciences,
Social-Informatics and Telecommunications Engineering), 2011.
16


## Page 17


41. J. Thiemann, A. Escher, and S. van de Par. Multiple model high-spatial
resolution hrtf measurements. In Proceedings of the German annual conference
on acoustics (DAGA), N¨urnberg, 2015.
42. T. Wendt, S. Van De Par, and S. D. Ewert. A computationally-efficient and
perceptually-plausible algorithm for binaural room impulse response simulation.
Journal of the Audio Engineering Society, 62(11):748–766, 2014.
17

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1804_11300v1_a_toolbox_for_rendering_virtual_acoustic_environments_in_the_context_of_audiolog
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1804_11300V1_A_TOOLBOX_FOR_RENDERING_VIRTUAL_ACOUSTIC_ENVIRONMENTS_IN_THE_CONTEXT_OF_AUDIOLOG.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1901.07452v3
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1901.07452v3_Satellite-mediated_quantum_atmospheric_links

> Source: 1901.07452v3_Satellite-mediated_quantum_atmospheric_links.pdf

> Pages: 30

---


## Page 1


PHYSICAL REVIEW A 99, 053830 (2019)
Satellite-mediated quantum atmospheric links
D. Vasylyev and W. Vogel
Institut f¨ur Physik, Universit¨at Rostock, Albert-Einstein-Straße 23, 18059 Rostock, Germany
F. Moll
Institute of Communications and Navigation, German Aerospace Center, 82234 Wessling, Germany
The establishment of quantum communication links over a global scale is enabled by satellite
nodes. We examine the inﬂuence of Earth’s atmosphere on the performance of quantum optical
communication channels with emphasis on the downlink scenario. We derive the geometrical path
length between a moving low Earth orbit satellite and an optical ground station as a function of the
ground observer’s zenith angle, his geographical latitude, and the meridian inclination angle of the
satellite. We show that the signal distortions due to regular atmospheric refraction, atmospheric
absorption, and turbulence have a strong dependence on the zenith angle. The observed saturation
of transmittance ﬂuctuations for large zenith angles is explained. The probability distribution of
the transmittance for slant propagation paths is derived, which enables us to perform the security
analysis of decoy state protocols implemented via satellite-mediated links.
I.
INTRODUCTION
The recent success in practical realization of quantum
state transfer between satellites and ground stations [1–
11] has established the cornerstone of future global quan-
tum communication. This achievement is especially im-
pressive in the view of how fast the quantum communica-
tion over free-space quantum links reached its maturity.
During only three decades the free-space quantum com-
munication reached distances of 7600 km [9], while start-
ing from proof-of-principle demonstration over a 30-cm
quantum channel [12].
An acceleration of the development of satellite-based
quantum technologies is caused by the need to establish
global secure communication networks. The present clas-
sical public key cryptography is based on mathematical
problems that admit no eﬃcient solutions with currently
available technologies. However, its security is vulnera-
ble to quantum computer hacking attacks, in particular,
those based on Shor’s factoring algorithm [13]. There-
fore, the future realization of quantum computers threat-
ens the currently used classical cryptographic protocols
to become insecure and hence useless.
Conversely, quantum key distribution (QKD) estab-
lishes unconditional secure cryptographic keys between
two distinct parties [14, 15].
The security of QKD
is based on some fundamental principles of quantum
physics such as the no-cloning theorem [16], Bell cor-
relations [17], uncertainty relations for the most of
continuous-variable protocols [18–24], etc.
Ironically,
while providing the security of QKD, the no-cloning the-
orem at the same time puts limitations on possible com-
munication distances due to inability to amplify a quan-
tum signal. One way to bring quantum communication
to global scale is the use of satellites. Satellite-mediated
QKD networks could span large communication distances
by linking widely separated ground stations [9, 10].
The setup of the satellite-mediated quantum links is
a demanding task.
The following problems must be
overcome for successfully establishing a feasible quantum
communication with satellites:
the relative motion of
the communication parties [25–27], the inﬂuence of grav-
ity [28, 29], the clock synchronization problem [30, 31],
acquisition, tracking and pointing issues with moving
platforms [32–34], the inﬂuence of background noise [35–
37], to name just a few. For low Earth orbiting (LEO)
satellites, the communication time is limited to a few
minutes [38, 39] and this puts additional tight bounds
on communication security. Finally, Earth’s atmosphere
contributes signiﬁcantly to the loss budget and to the
deterioration of the quantum signal due to diﬀraction,
scattering, absorption, and atmospheric turbulence [40–
42].
The common feature of the aforementioned issues is
the strong dependence of disturbing factors on the rela-
tive position of the moving satellite and the ground sta-
tion. For the observer at the ground station the instan-
taneous position of the satellite is given by the zenith
angle, i.e., by the angle between the satellite and the
vertical direction. The dependence of atmospheric dis-
turbances on the zenith angle has attracted the atten-
tion of scientists since ancient times. Already Ptolemy
(100-175 A.D.) noticed that the atmospheric refraction
displaces the apparent position of celestial bodies toward
the zenith [43]. Such a regular refraction is caused by
the altitude variation of the atmospheric refractive in-
dex. It inﬂuences the precision of satellite measurements
and is responsible for apparent elongation of celestial ob-
jects, mirages, green ﬂashes on setting sun, to name just
a few [44]. Other types of disturbances, such as inten-
sity scintillation [45, 46] and image dancing [40, 47], arise
from turbulent ﬂuctuations of the atmospheric refractive
index. The strength of these ﬂuctuations varies with alti-
tude and hence its inﬂuence on optical light propagation
is also a function of the zenith angle. Thus, the exami-
nation of the zenith angle dependence of relevant charac-
teristics is of immense importance for the establishing of
robust and reliable optical quantum communication links
via the satellites.
arXiv:1901.07452v3  [quant-ph]  5 Apr 2021


## Page 2


2
In this article we address several aspects of ground-
to-space communication connected with Earth’s atmo-
sphere.
We focus on quantum links between optical
ground stations (OGS) and LEO satellites. Orbital pe-
riods of LEO satellites are of 120 min or less, leading
to short passage times of the OGS, with which commu-
nication is aimed to be established. Depending on the
inclination angle of the satellite orbit, the expected com-
munication time varies in the range of 8-16 min. This
communication time window is actually narrower due
to the time needed for satellite acquisition.
Addition-
ally, satellites with trajectories of small inclination angle
could lose the contact with the OGS because of natural
barriers, while OGS telescopes could disconnect commu-
nication with satellites at small zenith angles due to me-
chanical construction of telescope mounts. Under these
circumstances, it is desirable to start the acquisition pro-
cedure when the satellite appears on the horizon. In this
case, quantum communication could be established al-
ready at small satellite elevation angles (large zenith an-
gles). Since the disturbing inﬂuence of the atmosphere
grows with the growth of the zenith angle, the zenith an-
gle dependence is crucial for the strict analysis of quan-
tum satellite communication links.
In the following we provide a systematic analysis of
quantum communication channels with the inclusion of
disturbance eﬀects due to geometrical elongation of com-
munication links, atmospheric regular refraction, extinc-
tion, and turbulence.
In our consideration we focus
on the zenith angle dependence of the associated sig-
nal losses. Additionally, the ﬁnite communication time
puts severe restrictions on secure quantum key length in
satellite-mediated communication. Careful estimation of
the loss budget of quantum channels is needed to esti-
mate the lower bound of the key length and its rate. In
this article we perform the security analysis of a decoy
state protocol that is commonly used in practice.
This article is structured as follows. In Sec. II we re-
view some basic communication scenarios with satellites
and in Sec. III A we obtain the geometrical distance be-
tween a ground station and a satellite. We focus on atmo-
spheric refraction eﬀects in Sec. III B. The regular extinc-
tion of the optical signal due to scattering and absorption
on air particles is discussed in Sec. III C. In Sec. IV, the
dependence of optical ﬁeld correlation functions on the
zenith angle for the optical ﬁeld propagating in turbu-
lence is studied. These functions allow us to calculate
the scintillation index, the mean beam-spot radius, and
the beam wandering variance. In Sec. V, we derive the
probability distribution of the transmittance that charac-
terizes satellite-mediated atmospheric quantum channels.
An application of the developed theory to the security
analysis of decoy-state protocols is discussed in Sec. VI.
A summary and conclusions are given in Sec. VII.
II.
SATELLITE-MEDIATED COMMUNICATION
LINKS
A low Earth orbit (LEO) is an orbit around Earth with
an altitude above Earth’s surface H ranging from 160 to
2000 km and an orbital period between about 80 and
130 min. The fast movement of the satellite puts certain
restrictions on the communication performance with the
ground stations and limits the communication window
to several minutes. The duration of the communication
session depends on OGS’ geographical position, the du-
ration of acquisition procedure, the presence of natural
obstacles along the optical path, etc. The signal-to-noise
ratio for satellite-mediated optical link is connected with
the length of the optical path between the communication
parties and hence it is related with the shape of the satel-
lite orbit and its relative position to the ground-station
communication party. Moreover, atmospheric refraction
bends the optical ray paths, while the atmospheric tur-
bulence corresponds to various random refraction and
diﬀraction phenomena.
In this section we remind the
reader of some basic geometrical concepts of satellite-
mediated optical links and leave the detailed analysis of
some aforementioned aspects to the following sections.
(a)
(b)
(c)
(d)
S2
S3
OGS1
OGS2
S1
FIG. 1.
Typical communication scenarios of optical ground
stations (OGS) with satellites S via uplink (d) and downlinks
(a)-(c).
The subscript i = 1, 2, 3 in the notation Si refers
to the successive positions of the satellite. After the satellite
makes one orbital revolution along its orbit (i) its new position
S3 as well as orbit (ii) appear inclined for the ground observer
OGS2. This apparent change in the orbit inclination is due
to the Earth rotation.
Figure 1 shows the generic communication experiment
with classical or quantum light.
Two ground stations
OGS1 and OGS2 establish the communication links with
satellite S shown in successive moments of time.
The
instantaneous positions of the satellite at times t1, t2,
and t3 are denoted as S1, S2, and S3, respectively. The
satellite has a polar orbit which passes over the Earth’s
polar regions from south to north. Moreover, since orbits
of most LEO satellites have vanishingly small elliptic-
ity, we will consider circular orbits in the following. Ini-
tially at time t1, the orbit, denoted as (i), passes through
the meridian plane of OGS2 but has some inclination to


## Page 3


3
meridian plane of OGS1. At later time t2, the satellite ap-
proaches the horizon, makes one full orbit revolution and
appears at the point S3. For a ground observer1 the ap-
parent satellite trajectory changes from (i) to (ii) during
this single revolution period due to the Earth rotation.
In the following we will also assume that the observer’s
parallax due to Earth’s rotation during one communica-
tion session can be neglected. This is justiﬁed if the ﬂight
time over the observer horizon is much smaller than the
satellite orbiting period2.
The satellite zenith trajectory that passes through the
observer’s meridian plane can be considered as the most
favorable for establishing a communication link and is
called as the ”best pass” by some authors [42]. Indeed, in
this case the link length is smaller compared to the link’s
lengths for inclined satellites. However, in many practi-
cal cases the mechanical mount of the OGS receiver or
sender telescopes prevents one to use the whole advan-
tage of the link that can lead to the interruption of the
communication process near small zenith angles of the
observer [39]. In such cases the trade-oﬀexists between
the use of optimal propagation path and the duration
of communication session. In this context the analysis
of communication with the satellites moving along the
inclined orbits is important.
Depending on the location of the source we distinguish
downlink [paths (a)-(c) in Fig. 1] and uplink [path (d)]
communication scenarios. A downlink geometry is favor-
able for optical signal transmission since the optical beam
starts to propagate in vacuum until it enters the atmo-
sphere. As a consequence the transmitted beam shows
smaller diﬀraction-induced broadening and small beam
wandering due to refraction on turbulent atmospheric
inhomogeneities.
This is the reason why the majority
of quantum optical experiments are being performed in
downlink conﬁguration [5, 8, 9, 39]. Under comparable
atmospheric conditions an uplink communication shows
inferior performance due to the inﬂuence of atmospheric
turbulence already on early stages of optical signal trans-
mission. Theoretical studies [42] reported the reduction
in received key bits being less than one order of magni-
tude compared to downlink scenario. However, an uplink
for quantum communication purposes poses the follow-
ing advantages: simple design of satellite missions or use
of already launched satellites [1], relaxed requirements
on data storage and processing equipment, variability of
quantum light sources and their accessibility for main-
tenance and repair [34].
In this article, we will focus
primarily on downlink communication scenarios.
1 In the following we use the word ”observer” in general referring to
the communication party located in the optical ground station.
2 Strictly speaking, for satellites with small altitudes above the
ground and for observers located at small geographical latitudes
the corrections due to the aforementioned parallax eﬀects should
be included.
III.
REGULAR LOSSES OF
SATELLITE-MEDIATED LINK
An optical Gaussian beam undergoes diﬀraction-
induced broadening while propagating in free space.
The amount of broadening depends on propagation path
length and whether beam is focused, collimated, or di-
vergent.
Since the receiver collects the incoming light
with the aid of ﬁnite-aperture device such as telescope,
only a fraction of the signal reaches the detector. For
ﬁxed aperture size, the signal losses due to truncation on
the aperture will increase with the increase of the prop-
agation path.
Moreover, absorption and scattering on
atmospheric gases and aerosols leads to the degradation
of the signal-to-noise ratio as well.
In this section we consider the eﬀects leading to
the regular diﬀraction-induced and extinction losses in
satellite-mediated links. By the word ”regular” we refer
to eﬀects that occur in a systematical manner. Among
such eﬀects we distinguish purely geometric optical path
elongation due to increase of relative positions of commu-
nication parties. The regular losses in this case depend
on the geographical location of the OGS, on the type
of the satellite orbit, and on such characteristics as the
satellite altitude, orbit inclination angle, and the satel-
lite declination angle to the Equator plane. Additionally,
regular atmospheric refraction bends the light rays, in-
creasing the optical propagation path and contributing
to loss budget.
This eﬀect is especially pronounced if
the satellite is positioned close to the observer horizon.
Finally, we discuss the signal loss due to atmospheric ab-
sorption and scattering.
A.
Slant range
We consider the communication scenario with an or-
biting satellite which has been described in the previous
section and derive the length of the line segment connect-
ing the ground observer and the satellite. This purely
geometric length referred as the slant range does not ac-
count for any elongation eﬀects due to atmosphere and
depends on the geographical location of the observer and
on the parameters of the satellite orbit.
In the following we consider a perfect polar satellite or-
bit that passes through both north and south poles. For
simplicity, we assume that the orbit is perfectly circular
with the radius R = R⊕+ H, where R⊕= 6 371 km be-
ing the Earth radius and H being the satellite altitude
above the ground. The slant range between the OGS and
the satellite is obtained then from simple trigonometric
considerations, [see Fig. 2 (a) and Appendix A]
L(Z) =
q
H2 + 2HR⊕+ R2
⊕cos2 Z −R⊕cos Z,
(1)
where Z is the zenith angle lying between the vertical
direction of the observer and the direction pointing on
the satellite. In Appendix A we show that for the satellite


## Page 4


4
orbits inclined to the observer meridian plane on angle
∆ι the zenith angle varies in the range Z ∈[Z∆ι
min, π/2]
with
Z∆ι
min = arccos
hp
1 −cos2 Ψ sin2 ∆ι
i
,
(2)
where Ψ is the geographical latitude of the observer.
Consequently, the slant range (1) varies from the min-
imal value L(Z∆ι
min) at zenith to the maximal value
q
(R⊕+ H)2 −R2
⊕at the observer’s horizon.
R⊕
L
H
a)
b)
R⊕
L
H
FIG. 2.
Geometry of the communication conﬁguration shown
in the plane that passes through the Earth center C, the ob-
server’s location O, and the satellite position S (a). The same
communication link OS is shown in its relative position to the
observer’s meridian plane ABOC (b). The cross-section of the
trajectory with the cone of angle 2Z and side SO yields the
associated link OS′ of the same length.
In order to relate the orbit inclination angle ∆ι with
the characteristics of the relative motion of the satellite
and the observer, we restrict our attention to the com-
munication scenario shown in Fig. 1 for the OGS2. If
the satellite is initially at zenith of the observer (indi-
cated as S1 in Fig. 1) and moves towards the observer’s
horizon along the zenith trajectory (i), after one satel-
lite orbiting period Tsat it reappears at S3 and moves
along the inclined trajectory (ii). The trajectory (ii) is
then inclined to the observer’s meridian plane due to the
Earth rotation. After nth satellite revolution the incli-
nation angle ∆ι between the satellite orbit plane and the
observer meridian is given by
∆ι = nTsatv⊕
R⊕
,
(3)
where v⊕= 1669.8 km/h is the speed of Earth’s rotation
at the Equator.
We refer the orbit with zero inclina-
tion, ∆ι = 0, as to the zenith orbit. In this case, the
orbit plane coincides with the observer meridian. In our
convention, ∆ι is positive (negative) if the satellite ﬂies
westwards (eastwards) of the observer meridian plane.
In order to get some impression of the communica-
tion geometry with the satellite with the inclined orbit,
we consider two satellite positions S and S′ at successive
times and the observer at O as shown in Fig. 2 (b). These
positions are chosen in such way that the slant ranges OS
and OS′ are equal as well as the corresponding zenith an-
gles, i.e., ∢SOB = ∢S′OB = Z. Let us choose the plane
ABOC as the observer meridian.
Then, the instanta-
neous position of the satellite is given by both its zenith
and azimuth angles. The latter is the angle between the
projected segment that connects the observer with the
satellite and the reference vector in the meridian plane
pointed toward the north pole. Clearly, for the inclined
orbit at geographical latitudes diﬀerent from the polar
or equatorial ones, the positions S and S′ have the same
zenith angle but diﬀerent azimuth angles.
One can imagine that the points S and S′ lie on the
cross sections of the satellite trajectory with the right
circular cone whose height is aligned along the observer’s
zenith and the apex coincides with O [cf. the segment of
the cone OASS′ in Fig. 2 (b)]. For inclined orbits that
pass above the observer’s horizon, each cone of angle 2Z
crosses the trajectory in two points if Z ∈(Z∆ι
min, π/2)
and in one point if Z = Z∆ι
min. Due to this symmetry
we are able to characterize the length of geometrical link
between the observer and the satellite by Eq. (1) with
Z ∈[Z∆ι
min, π/2] and ignore the detailed information on
the corresponding azimuth values. The latter assumption
is well justiﬁed if the detailed position of satellite is de-
termined by a tracking system that aligns automatically
the sender and the receiver telescopes. In this case, the
observer coordinate system is associated with the plane
OSC [cf. Fig. 2 (a)] that rotates around the axis OC.
Therefore, for optical communication with the automat-
ical azimuth angle tracking the relevant link information
is incorporated in the zenith angle dependence of the rel-
evant quantities. It is worth to note that the cross sec-
tion of the cone of given Z with other satellite trajectory
determines the slant ranges of the same length. For ex-
ample, link AO on Fig. 2 (b) for the zenith orbit AB is
equivalent to the links SO and S′O which results in equal
propagation properties of light along these links.
B.
Regular refraction
In this subsection we calculate the elongation of the
slant range due to atmospheric refraction. Atmospheric
refraction phenomena are based on the fact that Earth’s
atmosphere has an optical refractive index that is diﬀer-
ent from its value in vacuum. Furthermore, the value of
the refractive index varies with the altitude, geograph-
ical location, and meteorological conditions and hence
refraction depends on space and time variables. We re-
fer to refraction phenomena that systematically occur
in the atmosphere as to regular refraction [44, 48–50].
Regular refraction changes with altitude in a theoreti-
cally predictable fashion. Time variation of regular at-
mospheric refraction has rather seasonal behavior even
for large zenith angles [51] and can be ignored.
Due to a spatial variability of the refractive index
with altitude, the light coming from a distant source and
reaching the ground observer propagates along a curved


## Page 5


5
path rather than a straight line. As a consequence, the
signal from distant objects arrives under the apparent
zenith angle Za rather than under the true zenith angle
Z. Both zenith angles are related as
Za = arcsin
 1
n0
sin Z

(4)
where n0 = 1.00027 is the air refractive index near the
ground. We consider the eﬀect of regular refraction on
elongation of the slant range given L(Z).
Earth’s atmosphere can be viewed as a spherically
stratiﬁed medium with speciﬁc distribution of refractive
index values within each strata. In order to obtain this
distribution we use the so-called standard atmosphere
model [52].
The standard atmosphere is an idealized
steady-state representation of Earth’s atmosphere that
gives values of atmospheric pressure, temperature, and
other parameters for altitudes up to 1000 km.
The
altitude-dependent values of the air refractive index can
be found using the distributions of temperature and pres-
sure according to the Edl´en equation [53, 54]. We distin-
guish 10 atmospheric layers above the ground and within
each layer we approximate the latitude dependence of
refractive index in linear manner (for details see Ap-
pendix B) If we denote the latitude of i-th layer upper
bound as Hi, the linear path within the layer is deter-
mined as
Li =
n
(R⊕+ Hi−1)2 + (R⊕+ Hi)2
(5)
−2(R⊕+ Hi−1)(R⊕+ Hi) cos[Φ(Z, ri)]
o1/2
.
The rest of the total optical path lies in the vacuum and
is given by
L11 =
n
(R⊕+ H10)2 + (R⊕+ H)2
(6)
−2(R⊕+ H10)(R⊕+ H) cos[Θ(Z, r10)]
o1/2
.
The angles Φ and Θ determine the relative position of in-
coming and refracted light rays within each layer and are
complex functions of observer’s zenith angle Z and the
so-called refraction integral ri [44]. The explicit expres-
sions for the lengths (5) and (6) are given in Appendix C
[cf. Eqs. (C19) and (C21)].
It is worth to note that it was assumed that the paths
segments Li in the form (5) are obtained with the as-
sumption that they are linear within each atmospheric
layer. This is approximately true for the standard at-
mosphere model, which gives the minimal ray curvature
of 4.4R⊕near the ground at Za=90◦(cf. Ref. [55] for
empirical formulas). This allows us to neglect the ray
curvature eﬀects in the following. This is of course an
idealization and for speciﬁc daytime and meteorological
conditions the accounting for ray curvature eﬀects turns
out to be important [56].
Zenith angle
1.30
1.20
1.15
1.05
1.00
Elongation factor, εr
1.10
1.25
50◦
60◦
70◦
80◦
90◦
εr(Za)
εr(Z)
H = 400 km
780 km
1200 km
FIG. 3.
Optical path length elongation factor due to at-
mospheric refraction as a function of observer’s apparent, Za,
and true, Z, zenith angles for several LEO satellite orbits with
altitudes H.
Figure 3 shows the path elongation factor due to at-
mospheric refraction,
εr(Za) =
1
L(Za)
11
X
i=1
Li(Za),
(7)
where L(Za) is given by Eqs. (1) and (4) and Li(Za) are
deﬁned by Eqs. (5) and (6). Alternatively, Eq. (7) can be
written as a function of the true zenith angle, i.e. εr(Z).
The behavior of εr as a function of the apparent zenith
angle Za starts to deviate from εr(Z) while approaching
the horizon due to larger optical density along the prop-
agation path near the horizon.
The elongation factor
diminishes with the growth of orbit altitude. This is due
to the increase of the propagation path in the vacuum
with the increase of satellite altitude. For further conve-
nience we give a polynomial ﬁt to the elongation factor
as a function of the apparent zenith angle (in degrees)
for the orbit with H = 780 km:
εr(Za) = 1 + 1.818908×10−4Z2
a
(8)
−4.066061×10−5|Za|3 + 3.813573×10−6Z4
a
−1.920844×10−7|Za|5 + 5.710429×10−9Z6
a
−1.032821×10−10|Za|7 + 1.117105×10−12Z8
a
−6.644358×10−15|Za|9 + 1.672433×10−17Z10
a .
Finally, the slant range that accounts the elongation due
to atmospheric refraction reads as
Lr(Za) = εr(Za)L(Za),
(9)
where L is given by Eq. (1).
C.
Regular extinction
Another source of losses that can be considered as reg-
ular or deterministic losses are associated with molecular


## Page 6


6
and aerosol scattering. For the horizontal atmospheric
links, the extinction factor is χext = exp[−βext(h)L],
where βext(h) is the extinction coeﬃcient due to molecu-
lar absorption and scattering at given height h above sea
level and L is the distance between the communication
parties. Clearly, for elevated links this formula should be
modiﬁed in order to include the variation of the extinc-
tion coeﬃcient with the height. If the slant range to the
satellite is given by Eq. (9) we can write
χext = exp
h
−
Lr(Za)
Z
0
dL′βext(L′)
i
,
(10)
where the observer is assumed to be located at sea level
and L′ = h sec Za. Since the value of the extinction co-
eﬃcient depends on the number density N(h) of air con-
stituents at given height h its altitude dependence can
be written as
βext(L′) = β0
ext
N(L′)
N0
= β0
ext exp [−L′/(H0 sec Za)] ,
(11)
where β0
ext is the extinction coeﬃcient at sea level and N0
is the corresponding number density of air constituents.
Here, we have used the altitude dependence of N derived
within the standard atmosphere model [cf. Appendix B,
Eq. (B8)] with the scale parameter H0 = 6600 m. Sub-
stituting Eq. (11) in Eq. (10) we ﬁnally derive
χext = exp
h
−β0
ext
H0 sec Za
1000

1 −e−Lr(Za)/(H0 sec Z0)i
.
(12)
Here we have adopted the conventional units of the ex-
tinction coeﬃcient to be given in km−1. Molecular or
Rayleigh scattering contributes 2.544 × 10−3 km−1 to
this coeﬃcient for optical wavelength λ = 800 nm [57].
The aerosol distribution has a more complex dependence
on altitude than the model (B8). Nevertheless, for the
most part of the optical propagation path one can con-
sider that aerosol scattering contributes roughly the same
amount to extinction as the Rayleigh scattering. For the
total extinction coeﬃcient in (10), we adopt therefore the
value β0
ext = 5 × 10−3 km−1. We also note that a similar
expression to (12) has been derived in Ref. [58].
IV.
ATMOSPHERIC TURBULENCE
In the previous section we considered the inﬂuence of
regular refraction on the elongation of the optical path
length for light propagating in the atmosphere. The reg-
ular refraction is caused by the variation of the air re-
fraction index with the altitude and is predictable pro-
vided the altitude variation of temperature and pressure
is known. Other types of refractive and diﬀraction phe-
nomena arise due to the irregular variation in space and
time of the refractive index. Such random variations are
connected with temperature ﬂuctuations and wind shear
and have statistical properties of turbulent scalar ﬁelds.
The strength of turbulent refractive index ﬂuctuations
also varies with the altitude. Hence, the irregular dis-
turbances of the optical signal in satellite-mediated com-
munication depend on the zenith angle. In this section
we discuss the dependence of aperture-averaged scintil-
lations, beam broadening, and beam wandering on the
zenith angle.
A.
Statistical description of optical turbulence
Turbulent air motion consists of a set of vortices or ed-
dies of various diameters, ranging from extremely large
with characteristic so-called outer scale Lo to extremely
small with a scale lo.
Under the inﬂuence of inertial
forces, larger eddies break up into smaller ones.
This
cascade process continues until the minimal scale lo, re-
ferred to as the inner scale, is reached and dissipation
of turbulent ﬂow energy takes place. This evolution of
turbulent air vortices leads to a random variability of the
refractive index,
ni(ρ, t) = ni + δn(ρ, t),
(13)
where ρ = (x
y
z)T and ni is the regular part of the
refractive index within ith atmospheric layer [cf. Eq. (B7)
of Appendix B]. In the following we will omit the index i
for convenience and adopt the notation n(ρ, t) for the re-
fractive index (13). In Eq. (13) the z axis is chosen along
the optical ray while r=(x
y)T lies in the transverse
plane to the ray direction. At optical wavelengths, the
ﬂuctuating part δn is of the order of 10−6 or less. When
the Taylor’s ”frozen turbulence” hypothesis [59] holds,
implying that the random ﬁeld n(ρ, t) is transported with
constant velocity v, therefore remaining stationary in the
moving coordinate system, n(ρ, t) = n(ρ −vt), the time
dependence of refractive index is incorporated in the spa-
tial variable.
In the statistical theory of optical turbulence, the re-
fractive index ﬂuctuations δn are described by the power
spectrum
Φn(k) =
1
(2π)3
Z
R3
d3ρ Bn(ρ)e−ik·ρ,
(14)
where the Bn is the correlation function
Bn(ρ1 −ρ2) = ⟨[n(ρ1) −⟨n⟩] [n(ρ2) −⟨n⟩]⟩
(15)
= ⟨δn(ρ1)δn(ρ2)⟩.
For a locally isotropic random ﬁeld the correlation func-
tion simpliﬁes further and the turbulent spectrum can be


## Page 7


7
written as
Φn(κ; z) = 1
π
z
Z
0
dz′Fn(κ; z′),
(16)
Fn(κ; z) =
Z
R2
d2rBI(r, z)e−iκ·r,
(17)
where κ=(kx
ky)T and r=r1−r2. For the inertial range
of spatial wave-numbers values, |κ| ∈[2π/Lo, 2π/lo], the
spectrum for Kolmogorov turbulence is
Φn(κ, z) = 0.033C2
n(z)|κ|−11
3 .
(18)
Here, C2
n is the refractive index structure parameter char-
acterizing the strength of refractive index ﬂuctuations.
In the following considerations we will require the spe-
ciﬁc form of correlation function, called structure func-
tion, for optical phase ﬂuctuations:
DS(r1, r2, r′
1, r′
2; z) = ⟨[S(r1, r′
1; z) −S(r2, r′
2; z)]2⟩,
(19)
where ri, r′
i, i = 1, 2, are the transverse components
of the corresponding spatial vectors ρi = (ri
z) and
ρ′
i = (r′
i
z). Here, the ﬂuctuating phase is found from
the ﬁrst approximation of geometric optics
SUL(r, r′; z) = k
2
z
Z
0
dz′ δn

r z′
z + r′ z −z′
z
, z′

(20)
for uplink and
SDL(r, r′; z)=k
2
z
Z
0
dz′ δn

r z −z′
z
+r′ z′
z , L−z′

(21)
for downlink communication scenarios.
In this article
we focus our attention on the downlink communication
conﬁguration and omit the corresponding superscripts for
simplicity in the notations. The formulas for uplink can
be then obtained by replacing z′ →L −z′ in integrals
similar to the one in Eq. (21).
For a locally isotropic and homogeneous random ﬁeld
δn, the Markov approximation,
⟨δn(r; z)δn(r′; z′)⟩= 2πδ(z −z′)
Z
R2
d2κ
× Φn(κ, z) exp [iκ · (r −r′)] ,
(22)
is well justiﬁed [40, 60]. The phase structure function
(19) is evaluated then as
DS(r1, r2, r′
1, r′
2; z) = DS(r1 −r2, r′
1 −r′
2; z)
= πk2
z
Z
0
dz′
Z
R2
d2κΦn(κ, z−z′)
(23)
×
(
1 −exp

iκ·
h
(r1−r2)z −z′
z
+ (r′
1−r′
2)z′
z
i)
.
For the Kolmogorov spectrum (18), in the case of down-
link the structure function (23) reduces to [61]
DS(r, r′, Lr)
(24)
= 2ρ
−5
3
0
1
Z
0
dξ C2
n([1−ξ]Lr)
C2
n,0
|r(1 −ξ)+r′ξ|
5
3 ,
where
ρ0 ≈(1.5C2
n,0k2Lturb)−3/5
(25)
is the radius of spatial coherence of a plane wave in the
atmosphere, Lturb is the propagation length within the
optically active turbulent atmospheric layer, Lr is the to-
tal propagation length, ξ is the dimensionless integration
variable, and
C2
n,0 = C2
n(h0 sec Za)
(26)
is the refractive index structure function taken at some
reference height h0 above the ground (see also Ap-
pendix D). The structure function (24) for uplink is ob-
tained by the change of the variable ξ →1 −ξ.
B.
Aperture-averaged scintillations
The dependence of optical intensity ﬂuctuations, i.e.,
scintillations, on the zenith angle has attracted attention
in the connection with astronomical photometry. Early
measurements of the scintillation index σ2
η [62–64] have
shown that the aperture-averaged scintillations (or power
scintillations) grow with the growth of the zenith angle
as
σ2
η = ⟨∆η2⟩
⟨η⟩2
∝(sec Za)γ ,
(27)
where
η =
Z
A
d2rI(r, Lr)
(28)
is the transmittance of the light intensity I(r, Lr)
through the receiver aperture with opening area A, and
r is the spatial variable transversal to propagation di-
rection.
The exponent γ in Eq. (27) is related to the
statistics of turbulent ﬂuctuations of the refractive in-
dex and depends on the characteristics of the receiver
telescope. Theoretical considerations [40] based on the
Rytov approximation yield γ = 11/6 for small receiv-
ing apertures and γ = 3 for large receiving apertures,
respectively. These results agree reasonably with the ex-
periments [65].
The later investigations [65–68] have shown that de-
pendence (27) is valid for small and moderate zenith an-
gles or for highly elevated optical ground stations. For
large zenith angles measured stellar scintillations exhibit


## Page 8


8
a saturation or decrease in its value.
A similar be-
havior has been reported for optical signals from satel-
lites [69, 70].
On the other hand, the Rytov approxi-
mation (27) yields the divergent scintillation index for
Za→90◦and does not account for the saturation eﬀect.
The phenomenon of saturation of scintillations has been
theoretically studied in Refs. [71–75] and is attributed
to multiple scattering phenomena on turbulent inhomo-
geneities.
In this section we derive the scintillation index of the
aperture-averaged optical signal from the satellite and
discuss its dependence on the zenith angle. As an ac-
companying result we obtain the expressions for two ﬁrst
moments of the transmittance (28), the mean width of
the beam spot at the receiver and the beam wandering
variance. These parameters will be used in Sec. V for
the derivation of the probability distribution of quantum
channel transmittance.
The scintillation index (27) is derived from the ﬁrst
two moments of the transmittance (28), namely
⟨η⟩=
Z
|r|≤a
d2r Γ2(r; Lr),
(29)
⟨η2⟩=
Z
|r1|≤a
d2r1
Z
|r2|≤a
d2r2 Γ4(r1r2; Lr),
(30)
where
Γ2(r; z) = ⟨u(r; z)u∗(r; z)⟩= ⟨I(r; z)⟩,
(31)
Γ4(r1, r2; z) = ⟨u(r1; z)u∗(r1; z)u(r2; z)u∗(r2; z)⟩
= ⟨I(r1; L)I(r2; z)⟩
(32)
a is the receiving aperture radius, and u(r; L) is the opti-
cal ﬁeld amplitude. Obviously, the ﬁeld correlation func-
tions Γ2 and Γ4 turn to be important ingredients for the
evaluation of σ2
η. On the other hand, their moments are
related to the beam wandering variance,
σ2
BW =
Z
R4
d2r1d2r2 x1x2Γ4(r1, r2; L),
(33)
and to the mean short-term beam spot radius of the
transmitted beam,
WST =
q
W 2
LT −4σ2
BW
(34)
= 2
" Z
R2
d2rx2Γ2(r; L) −σ2
BW
#1/2
.
Here the variable x denotes the x component of the trans-
verse vector r. The short-term beam spot radius is as-
sociated with the intensity distribution observed during
small exposure times while the long-term radius WLT in-
cludes broadening eﬀects due to beam wandering and is
associated with long detection times.
In the following
section we show that the quantities (29), (30), (33), (34)
are of primary importance for the description of quantum
atmospheric channels.
The correlation functions Γ2 and Γ4 we calculate us-
ing the phase approximation of the Huygens-Kirchhoﬀ
method [76, 77].
This approximative method neglects
the ﬂuctuations of the ﬁeld amplitude.
On the other
hand, the phase ﬂuctuations characterized by Eqs. (20)
and (21) are caused by random diﬀraction and refraction
in the turbulent medium, which are included up to the
terms of order ⟨δn2⟩1/2. The former condition is justi-
ﬁed for communication scenarios through links with sat-
urated turbulence
[78], which is the case for satellite-
mediated atmospheric channels. More rigorous methods
[79] and experiments [40, 80] suggest that the latter con-
dition is satisﬁed for arbitrary propagation paths and
turbulence strengths. Thus, the phase approximation of
the Huygens-Kirchhoﬀmethod accounts for the diﬀrac-
tion and refraction eﬀects arising due to the optical beam
propagation in the turbulent atmosphere in most practi-
cally important cases.
For the TE00 mode of the laser beam in the plane of
the radiating aperture,
u(r; 0) =
s
2
π2W 2
0
exp

−
 1
W 2
0
−ik
2F

r2

,
(35)
with W0 being the initial beam spot size and F being the
initial beam wavefront radius, the correlation functions
(31) and (32) read as
Γ2(r; Lr)=
k2
4π2L2r
Z
R2
d2r′
(36)
× e
−g2r′2
2W 2
0
−2i
Ω
W 2
0
r·r′−1
2 DS(0,r′;Lr),
Γ4(r, R; Lr) =
2k4
π2(2π)3L4rW 2
0
Z
R6
d2r′
1d2r′
2d2r′
3
× e
−
1
W 2
0
(r′
1
2+r′
2
2+g2r′
3
2)+2i
Ω
W 2
0
[1−L
F ]r′
1·r′
2
(37)
× e
−2i
Ω
W 2
0
r·r′
2−4i
Ω
W 2
0
R·r′
3J (r, r′
1, r′
2, r′
3)
J = exp
h1
2
X
j=1,2
n
DS(r, r′
1 + (−1)jr′
2; Lr)
(38)
−DS(r, r′
1+(−1)jr′
3; Lr)−DS(0, r′
2+(−1)jr′
3; Lr)
i
,
where we have used the relative and the center-of-mass
coordinates r = r1−r2 and R = (r1+r2)/2, respectively.
Here, Ω= kW 2
0 /(2Lr) is the Fresnel number of the trans-
mitter aperture, g2 = 1+Ω2[1−Lr/F]2 is the generalized
diﬀraction parameter, and the phase structure function
DS is given by (24). We also note that Eqs. (36) and (37)
incorporate multiple-scattering eﬀects.


## Page 9


9
1.
Mean transmittance
The average intensity at the receiver aperture is found
from Eqs. (31) and (36). We use the quadratic approxi-
mation [41]
exp
h
−(r/ρ0)
5
3
i
≈exp
h
−(r/ρ0)2i
,
(39)
for the spatial dependence of the phase structure func-
tion (24). This approximation gives a good accuracy for
small values of the radius of spatial coherence ρ0, i.e.,
for long propagation distances and strong optical tur-
bulence, which is always the case for satellite-mediated
links. Performing the integration in Eq. (36), we obtain
the Gaussian distribution of the intensity distribution at
the receiver aperture plane,
⟨I(r; Lr)⟩=
2
πW 2
LT
exp

−2 r2
W 2
LT

,
(40)
where the long-term beam spot radius at the receiver is
[cf. also Eq. (34)]
WLT(Lr) = W0
"
1 −Lr
F
2
+ Ω−2

1 + W 2
0
ρ2
0
X 2
#1/2
.
(41)
Here, ρ0 is deﬁned in Eq. (25) and
X 2 =
1
C2
n,0
1
Z
0
dξ C2
n(Lr, 1 −ξ)ξ5/3
(42)
is the weighting factor that depends on the slant proﬁle
of the refractive index structure function C2
n(Lr, 1 −ξ).
This proﬁle is related with the vertical proﬁle of turbu-
lence as C2
n(Lr, 1−ξ) = C2
n[h(ξ)=Lr(1 −ξ) cos Za] (see
Appendix D for details). The natural diﬀraction of the
laser beam is included in Eq. (41) by considering the ini-
tial beam waist W0, wavelength λ (Fresnel number Ω),
and propagation distance Lr. The resulting natural laser
beam divergence is usually the main source of signal loss.
The obtained formula (41) coincides with the long-term
beam spot radius given in Ref. [81].
The obtained mean intensity allows one to calculate
the mean transmittance straightforwardly.
Inserting
Eq. (40) in Eq. (28) and performing the integration with
respect to the spatial variable, we obtain
⟨η⟩≈1 −e
−2a2
W 2
LT .
(43)
This is the transmittance of Gaussian beam with the
beam-spot radius WLT through a circular aperture of ra-
dius a. The approximation sign is used due to the used
quadratic approximation (39).
This formula can serve
for estimative calculations only and for the precise eval-
uations from Eqs. (29) and (36) we derive
⟨η⟩= k2
L2r
a
Z
0
drr
∞
Z
0
dr′r′e
−g2r′2
2W 2
0
−1
2 DS(0,r′;Lr)J0
 2Ω
W 2
0
rr′

,
(44)
where Jn(x) is the Bessel function of nth order.
For the sake of completeness, we give the expression of
the short-time beam spot size (34). Following Ref. [82]
it is calculated as
WST(Lr) = W0
"
1 −Lr
F
2
(45)
+ Ω−2
 
1 + W 2
0
ρ2
0
X 2
1 + 0.24
  ρ0
aX
1/3
!#1/2
.
Here, the term proportional to X arises due to the
diﬀraction-induced beam broadening caused by the tur-
bulent atmosphere. In the limit X →0 we obtain from
Eq. (45) the diﬀraction-induced beam broadening in vac-
uum. We also note that Eq. (45) does not account for
the beam broadening due to the random scattering on
particles, aerosols, and precipitations.
This additional
broadening might be relevant under the condition of high
moisture or low visibility, as has been shown in Ref. [83].
In this article, however, we deal with ideal weather con-
ditions for optical communication. The short-term beam
spot radius (45) is important for the derivation of the
probability distribution of the channel transmittance as
will be shown in the next section.
2.
Second moment of transmittance
The second moment of transmittance is obtained by
substituting Eq. (37) in (30). Unfortunately, the integra-
tion cannot be performed in analytic form. However, for
satellite-mediated atmospheric links we can simplify the
integral kernel (38) for the further numerical integration
(for details see Appendix E):


## Page 10


10
J (r, r′
1, r′
2, r′
3)
≈exp
h
−ρ
−5
3
0
1
Z
0
dξ C2
n(Lr, 1 −ξ)
C2
n,0
X
j=1,2
r(1−ξ)+[r′
1+(−1)jr′
3]ξ

5
3 i
+ exp
h
−ρ
−5
3
0
1
Z
0
dξ C2
n(Lr, 1 −ξ)
C2
n,0
X
j=1,2
[r′
2+(−1)jr′
3]ξ

5
3 i
−exp
h
−ρ
−5
3
0
1
Z
0
dξ C2
n(Lr, 1 −ξ)
C2
n,0
X
j=1,2
n[r′
2+(−1)jr′
3]ξ

5
3 +
r(1 −ξ)+[r′
1+(−1)jr′
3]ξ

5
3 oi
,
(46)
This expression can be simpliﬁed further by noting that
most of the optical propagation path lies in vacuum as
well as in the atmosphere with negligibly small turbu-
lence, i.e., Lturb ≪Lr. As a consequence, for small values
of the integration variable ξ in (46), when the contribu-
tions from the r(1 −ξ) term are dominant, the value of
the refractive index structure constant is equal to zero.
On the other hand, for ξ ≈1 the structure constant is ﬁ-
nite but the contribution from r(1−ξ) is negligibly small.
Therefore, one can neglect the dependence on r in (46)
along the whole propagation path
J (r, r′
1, r′
2, r′
3) ≈J (0, r′
1, r′
2, r′
3).
(47)
We stress that this formula is justiﬁed for downlink con-
ﬁgurations only.
Inserting (37) in (30) and using the
approximation (47), we obtain
⟨η2⟩=
2k4
π2(2π)3L4rW 2
0
Z
|r1|≤a
d2r1
Z
|r2|≤a
d2r2
Z
R6
d2r′
1d2r′
2d2r′
3
× e
−
1
W 2
0
(r′
1
2+r′
2
2+g2r′
3
2)+2i
Ω
W 2
0
[1−L
F ]r′
1·r′
2
(48)
× e
−2i
Ω
W 2
0
r1·(r′
2+r′
3)+2i
Ω
W 2
0
r2·(r′
2−r′
3)J (0, r′
1, r′
2, r′
3).
The further evaluation of integrals in (48) should be per-
formed numerically.
TABLE I. Atmospheric, optical beam, and geographical pa-
rameters used in the simulations.
Zenith-dependent values
are given at Za = 0◦.
Parameter
Notation
Value
Radius of spatial coherence
ρ0 (cm)
13
Reference structure parameter C2
n,0 (m−2/3)
10−17
Wavelength
λ (nm)
840
Initial beam-spot radius
W0 (cm)
2
Receiver’s aperture radius
a (m)
0.5
Wave-front radius
F (m)
105
Observer’s coordinates
48◦N, 11.5◦E
Figure 4 shows the aperture-averaged scintillation in-
dex σ2
η = ⟨∆η2⟩/⟨η⟩2 as a function of the zenith an-
gle calculated by using the phase approximation of the
∆ι=0◦
∆ι=25◦
∆ι=50◦
Scintillation index, σ2
η
0.1
0.0
0.2
0.4
0◦
20◦
40◦
60◦
80◦
Zenith angle, Za
Z25◦
min
Z50◦
min
0.3
(sec Za)3
FIG. 4.
Aperture-averaged scintillation index as a function
of the zenith angle for several inclination angles of the satellite
orbit. The dotted intervals indicate the minimal zenith angles
for inclined orbits [cf. Eq. (2)]. The dotted curve corresponds
to the asymptotic value (27).
Huygens-Kirchhoﬀmethod. For the calculation of ⟨η2⟩
we have used the approximate expression (48), whereas
⟨η⟩is calculated from Eq. (44). Table I lists the atmo-
spheric and optical beam parameters used in the calcu-
lation of the scintillation index. The curves shown for
three inclination angles yield the same functional depen-
dence on zenith angle for medium and large Za due to
the properties discussed in Sec. III A and diﬀer on the
minimal value of the zenith angle Z∆ι
min [ see Eq. (2)]. For
small and moderate zenith angles the scintillation index
σ2
η shows the asymptotic behavior given by Eq. (27). The
scintillation index calculated within the phase approxi-
mation of Huygens-Kirchhoﬀmethod shows the satura-
tion and decrease of intensity ﬂuctuations for large zenith
angles.
This result can be qualitatively compared with the ex-
perimental data that have been taken within ﬁve mea-
surement campaigns between 2006 and 2016 and shown
in Fig. 5 (shaded area). The direct quantitative compar-
ison of theoretical curves in Fig. 4 with any individual
experimental curve contributing to Fig. 5 is hardly pos-
sible due to the lack of all needed parameters of turbu-
lence and the hardly measurable proﬁle of C2
n(z) inherent
to the given meteorological conditions. Measurements of


## Page 11


11
intensity scintillation index were conducted with an op-
tical ground station nearby Munich, Germany, with el-
evation of about 602 m above sea level. Measurement
wavelength was 847 and 1550 nm, depending on the used
satellite (see Table II for an overview of measurement
campaigns).
We also note that the diﬀerence in zenith angles with
maximal scintillation index in Figs. 4 and 5 arises due to
the diﬀerent elevations of the observers.
TABLE II. Overview of conducted measurement campaigns.
Year
Satellites/
Wavelength (nm) No. Measurements
(Laser terminal)
2006 OICETS (LUCE)
847
5
2009 OICETS (LUCE)
847
4
2015
ISS (OPALS)
1550
1
2016
ISS (OPALS)
1550
1
2016 Socrates (SOTA)
1550
1
The measurement device that delivered the data for
the scintillation index analysis is an infrared camera lo-
cated in the exit pupil of the telescope. Thus, images
of the intensity ﬁeld incident onto the telescope aperture
are recorded and analyzed. The experimental curves in
Fig. 5 are obtained based on data from a single camera
pixel. The eﬀective radius of the pixel, taking magniﬁca-
tion of the optical system into account, is a = 3.2 mm.
The small value of the detector aperture as well as short
exposure times (of order 0.1-1 ms) reduce the telescope
aperture smoothing eﬀect, yielding the intensity scintil-
lation index
σ2
I = ⟨∆I2⟩
⟨I⟩2
≈σ2
η

a→0.
For the sake of better comparison, the 1550-nm data are
re-calculated to 847-nm wavelength using weak scatter-
ing theory. This is possible since the 1550 nm measure-
ments lie well within the weak scattering regime, i.e. at
low zenith angles.
Twelve measurements are analyzed
to form the mean run of scintillation index as shown in
Fig. 5. The grey area indicates the conﬁdence bound de-
ﬁned by the standard deviation. At low and high zenith
angles, the standard deviation is not illustrated since only
a single measurement track is recorded in these regimes
and, thus, determination of standard deviation is not pos-
sible. Further description of the individual measurement
campaigns and the data analysis method are found in
[70, 84].
In Appendix F we consider an estimation for the
aperture-averaged scintillation index based on approxi-
mate phenomenological expressions for ﬁeld correlation
functions. This can give some insight into saturation ef-
fects observed at large zenith angles. The consideration
30◦
40◦
50◦
60◦
70◦
80◦
90◦
Zenith angle, Za
20◦
Model, Eq. (49)
Experiment
2.5
2.0
1.5
1.0
0.5
0.0
Scintillation index
FIG. 5.
Intensity scintillation index of LEO-ground down-
link at 847 nm. Experimental data are given with conﬁdence
intervals (shaded area) and mean value (dashed line) cal-
culated from the individual measurements. The theoretical
curve (solid) is calculated using Eq. (49).
yields
σ2
η = 1.12 C2
n,0 [∆κ]
7
3 (H0 sec Za)3
(49)
× 2F3
7
6, 3
2; 2, 13
6 , 3; −a2∆κ2

,
∆κ=0.69 µ C−6/5
n,0
k−1/5(H0 sec Za)−8/5.
Here, a is the receiving aperture radius, k = 2π/λ is
the optical wave number, and 2F3(a, b; c, d, e; x) is the
hypergeometric function. This simple analytic formula
contains three phenomenological parameters: the refrac-
tive index structure parameter at the ground C2
n,0, the
characteristic height of the atmospheric turbulent layer
H0, and the dimensionless proportionality parameter µ.
The theoretical curve based on Eq. (49) shows a rea-
sonable agreement with the experimental data in Fig. 5.
The model parameters are: C2
n,0 = 2.5×10−17 m−2/3,
H0 = 0.5 km, a = 3.2 mm, λ = 847 nm, and µ = 0.92.
3.
Beam wandering variance
For the sake of completeness, we give the expression
for the beam wandering variance (33).
Beam wander-
ing phenomenon depends strongly on the outer scale of
turbulence, Lo. The ﬁnite Lo deﬁnes the upper bound
on the size of turbulent inhomogeneities that are able
to deﬂect the beam as a whole. Since the Kolmogorov
spectrum (18) has a discontinuity at the turbulent wave
numbers, |κ| ≈κo = 2π/Lo, it is more suitable to use
the smoothed spectrum
Φn(κ, z) = 0.033C2
n(z)|κ|−11
2

1 + e
−|κ|2
κ2◦

.
(50)
For slant paths the outer turbulence scale varies with
the height h. Very well known is the empirical Coulman-


## Page 12


12
Vernin proﬁle that reads as [85]
L◦(h) =
4
1 +

h−8500
2500
2 ,
(51)
where the outer scale is given in meters.
Using the spectrum (50) and following the derivation
steps of Ref. [86] we obtain
σ2
BW = 1.29L3
r
1
Z
0
dξξ2C2
n(Lr, 1−ξ)
n
W −1/3
ST
([1 −ξ]Lr)
+

W 2
ST([1 −ξ]Lr) + L2
◦([1 −ξ]Lr) /(2π)2−1/6o
. (52)
Here WST(Lr) is given by (34) and the altitude de-
pendence of the outer scale is given by (51) with h ≈
Lr cos Za. Appendix D summarizes the model for the C2
n
proﬁle needed for the calculation of the beam wandering
variance (52).
0◦
20◦
40◦
60◦
80◦
Zenith angle, Za
2
0
8
4
  0
1
0
2
1
0
(µrad)
(arcsecond)
(µrad)
(arcsecond)
∆ι=0◦
∆ι=25◦
∆ι=50◦
Z25◦
min
Z50◦
min
Z25◦
min
Z50◦
min
3
6
5
  2
6
10
1
4
σBW/Lr
σBW/Lr
WST/Lr
WST/Lr
FIG. 6.
Variation of the mean short-term divergence angle
WST/Lr and the standard deviation of the angle-of-arrival
ﬂuctuations, σBW/Lr, with the zenith angle. The results are
presented for several inclination angles of the satellite orbit
∆ι. Dotted lines indicate the minimal zenith angles (2) for
inclined orbits.
Figure 6 shows the divergence angle WST/Lr and
the standard deviation of the angle-of-arrival ﬂuctua-
tions σBW/Lr as a function of the apparent zenith an-
gle and several inclination angles ∆ι of the satellite or-
bit. For the simulation of turbulent atmosphere we use
the AFGL+WK (the Air Force Geophysics Laboratory
and Walters-Kunkel model) night model for the altitude
variation of the refractive index structure parameter (see
Appendix D). Other relevant atmospheric parameters are
listed in Table I. The beam spot radius and the beam
wandering variance grow with the growth of the zenith
angle. The asymmetry of the curves for inclined orbits is
dictated by the geographical position of the observer as
discussed in Sec. III A. For zenith angles near Za = 80◦
some saturation of both quantities appears. This is due
to the drop of the turbulence strength in the lower tropo-
sphere (3-10 km), the region that has its maximal contri-
bution to the optical path at this zenith angle. Near the
observer horizon the contributions of boundary layer tur-
bulence at 1 km as well as of the atmospheric refraction
have a maximal eﬀect on the optical beam distortions
leading to the growth of both beam-spot size and beam
wandering.
V.
PROBABILITY DISTRIBUTION OF
TRANSMITTANCE
In this section we consider the model of atmospheric
quantum channels. For the physical consistence of this
model the preservation of the canonical commutation re-
lations for the quantized optical ﬁeld operators is im-
portant.
This requirement puts certain restrictions on
the probability distribution that governs the statistics
of ﬂuctuating channel transmittance. We also show the
relationship of the statistical characteristics of this distri-
bution and the moments of the ﬁeld correlation functions
derived in the previous section.
Quantum light transmission through a linear medium,
such as Earth’s atmosphere, is conveniently characterized
via the input-output relations
ˆaout = √ηˆain +
p
1 −ηˆc,
(53)
where ˆain(out) is the input (output) ﬁeld annihilation op-
erator and ˆc is an environmental mode operator. The
random transmittance η ∈[0, 1] equals to the instanta-
neously transmitted normalized intensity truncated by
the receiver aperture [cf. Eq. (28)]. The transmission of
the quantum state through the atmospheric link depends
not only on the characteristics of the channel, but also on
the parameters of the receiver aperture. In terms of the
Glauber-Sudarshan P function [87, 88], the input-output
relation (53) reads [89] as
Pout(α) =
1
Z
0
dη P(η)1
η Pin
 α
√η

,
(54)
where we have assumed that the environmental modes
are in the vacuum state. Here, Pin(α) and Pout(α) are
P functions of the input and output quantum ﬁelds and
P(η) is the probability distribution of the transmittance
(PDT). Hence, the description of quantum-light propa-
gation through the atmosphere reduces merely to identi-
fying P(η).
An important requirement for the PDT is that its do-
main of deﬁnition is restricted to the interval [0, 1], which
is the consequence of the canonical commutation relation


## Page 13


13
for ˆaout and ˆa†
out. Violation of this requirement may lead
to unphysical eﬀects which have critical inﬂuence, e.g.,
on security bounds of communication protocols. The ﬁrst
consistent model of the PDT [90] considered beam wan-
dering as the main source of ﬂuctuating losses on the
receiver.
In this case, the PDT can be derived in an-
alytical form and is given by the log-negative Weibull
distribution.
This beam wandering model was further
extended to include eﬀects due to random beam broad-
ening and deformation of the beam proﬁle into an el-
liptic form [91]. In Ref. [83] this so-called elliptic-beam
model was extended to include additional beam broad-
ening and extinction due to random scattering on atmo-
spheric aerosols and dust particles.
The elliptic-beam
model gives reasonable agreement with the PDT mea-
surements for short-distance links.
For long-distance
channels, a discrepancy arises between the transmittance
moments calculated via the elliptic-beam PDT and the
corresponding moments (29) and (30) calculated from
the ﬁrst principles. For elimination of this discrepancy,
a PDT model has been proposed based on the law of
total probability [92]. This model is most suitable for
the description of long-length quantum channels and in
this section we extend it to the case of slant propagation
paths.
Analyzing experimental PDTs for short and long prop-
agation distances, one observes two limiting behaviors.
For short distances, the beam wandering appears to be
the major source of ﬂuctuating losses and the correspond-
ing PDT has similar form to the log-negative Weibull dis-
tribution. For long propagation distances, beam broad-
ening and deformation are the dominating eﬀects yielding
the PDT in the form of truncated log-normal distribu-
tion. In the general case, using the law of total probabil-
ity [93], the PDT can be written as
P(η) =
Z
R2
d2r0P(η|r0)ρ(r0),
(55)
where the random vector r0 transverse to the propaga-
tion direction describes the position of the deﬂected beam
centroid relative to the aperture center. The correspond-
ing probability distribution in (55),
ρ(r0) =
1
2πσ2
BW
exp

−|r0|2
2σ2
BW

,
(56)
describes the beam-wandering contribution to the to-
tal PDT. Here, σ2
BW is the beam wandering variance,
Eq. (33). The eﬀects of beam-spot distortions are incor-
porated in the conditional distribution P(η|r0). Physi-
cally it can be interpreted as the conditional PDT for the
beam with a centroid position tracked to the position r0
relative to the aperture center.
For negligible small beam wandering, σBW →0, the
distribution (56) reduces to Dirac delta function and the
conditional probability according to (55) reduces to the
PDT. In this limit, the PDT resembles the log-normal
distribution. Hence, for general situations we can assume
that the conditional distribution can be approximated by
the truncated log-normal distribution
P(η|r0)
(57)
≈
(
1
F(1)
1
√
2πησr0 exp
h
−(log η+µr0)2
2σ2r0
i
for
η ∈[0, 1],
0
otherwise,
where F(1) is the cumulative function of the (untrun-
cated) log-normal distribution at η = 1. The parameters
of this distribution are related to the conditional mo-
ments ⟨η⟩r0 and ⟨η2⟩r0. These conditional moments can
be considered as the corresponding moments of the aper-
ture transmittance of the eﬀective beam with beam-spot
radius WST whose centroid is displaced to the distance
r0 from the aperture center. In the limit of weak beam
wandering, the conditional moments can be written as
(see Ref. [92] for details)
⟨η⟩r0 ≈η0 exp

−
|r0|
R
λ
,
(58)
⟨η2⟩r0 ≈ζ2
0 exp

−2
|r0|
R
λ
,
(59)
where
η0 =
⟨η⟩
R ∞
0
dξ ξ e−ξ2/2e−[(σBW /R)ξ]λ ,
(60)
ζ2
0 =
⟨η2⟩
R ∞
0
dξ ξ e−ξ2/2e−2[(σBW /R)ξ]λ ,
(61)
R = a
(
ln

2
1 −exp

−2 a2
W 2
ST

1 −exp
h
−4 a2
W 2
ST
i
I0

4 a2
W 2
ST

)−1/λ
, (62)
λ = 8 a2
W 2
ST
e−4(a2/W 2
ST)I1

4 a2
W 2
ST

1 −exp
h
−4 a2
W 2
ST
i
I0

4 a2
W 2
ST

(63)
×
"
ln

2
1 −exp

−2 a2
W 2
ST

1 −exp
h
−4 a2
W 2
ST
i
I0

4 a2
W 2
ST

#−1
.
Here, WST is given by (45) and In(x) is the modiﬁed
Bessel function of nth order. The parameters of the con-
ditional distribution (57) are determined from Eqs. (58)
and (59) approximately:
µr ≈−ln
"
⟨η⟩2
r0
p
⟨η2⟩r0
#
≈−ln
η2
0
ζ0

+
|r0|
R
λ
,
(64)


## Page 14


14
σ2
r0 ≈
s
ln
⟨η2⟩r0
⟨η⟩2r0

≈ln
ζ2
0
η2
0

.
(65)
The knowledge of the parameter set {⟨η⟩, ⟨η2⟩, σBW,
WST} is therefore suﬃcient for the determination of the
channel PDT. For detection with a Cassegrain-type tele-
scope, the PDT derivation procedure can be further gen-
eralized as described in Ref. [94].
Practical optical communication via satellites is impos-
sible without acquiring and tracking the received signal.
Both beam wandering due to atmospheric turbulence [41]
or satellite vibrations [95] cause changes in the direction
of the received beam that result in misalignment between
the communication parties. Moreover, the velocity aber-
ration point ahead and the atmospheric dispersion ef-
fects [96] should be taken into account. The compensa-
tion of these disturbances requires an active beam steer-
ing that is accomplished by mechanical means. Quantum
key exchange with low mean intensities requires espe-
cially precise beam tracking and stable pointing [97, 98].
Applying coarse and ﬁne tracking and pointing strategies,
one can achieve a tracking accuracy of approximately
θtr ∼1.2µrad for LEO-ground communication links [99].
We incorporate the tracking procedure in the PDT model
(55) by replacing
σBW →σtr = θtrLr(Za)
(66)
in Eq. (56). Finally, we note that the parameters (60)
and (63) still contain the beam wandering variance, and
we calculate σ2
BW by means of Eq. (52).
VI.
APPLICATION: DECOY STATE
PROTOCOL
We apply the developed theory of satellite-mediated
quantum atmospheric channels for the calculation of the
secret key rate when decoy states are in use [100, 101].
Conventionally, we refer to communication parties Alice
and Bob as to the sender and the receiver, respectively.
Based on the BB84 protocol [14], the decoy-state method
estimates channel parameters by sending two types of
states. While one type of states (signal states) is used for
transmission of quantum keys, the other is called the de-
coy state, which is used for the estimation of the number
of transmitted single-photon states. Ideally, the single-
photon states are most suitable to be used as the signal.
Practically perfect single-photon sources are hard to at-
tain and one uses weak coherent states instead. In the
security analysis of the decoy-state method, both signal
and decoy states possess equal properties except for their
intensity.
Usually, only a few decoy states are needed for practi-
cal implementations. A simple two-decoy-state protocol
with vacuum+weak decoy states gives an optimal key
generation rate which is the same as having an inﬁnite
number of decoy states [102]. On the ﬁrst stage of the
protocol, Alice, who has a phase-randomized source of
coherent states, encodes the bits in the X or Z basis as
in the standard BB84 scheme, e.g., by utilizing polariza-
tion degrees of freedom. Additionally to the signal ﬁeld,
she generates decoy states in vacuum and weak coher-
ent states. The phase randomization makes the source
statistically equivalent to a Poissonian distribution of
Fock states such that, when the average photon num-
ber from the light source is µ, the probability to send an
n-photon pulse is e−µµn/n!. We denote the mean pho-
ton numbers as µj, j = s, d, v for signal, weak-decoy, and
vacuum states.
The following conditions are satisﬁed:
µd < µs < 1, µv = 0. After transmission through the
free-space channel, Bob performs measurement of trans-
mitted bits in a randomly chosen X or Z basis.
The
conditional probability of a detection event at Bob’s side
given that Alice sends an i-input state is referred to as
the yield Yi of an i-photon state. The vacuum state is
used for the estimation of the background detection prob-
ability Y0 while the weak-decoy state allows one to esti-
mate the single-photon yield Y1 and the error rate of the
single-photon state e1. Since both signal and weak-decoy
states propagate through the same channel, the single-
photon yield would be the same for these states. Due
to this property, the security of the decoy-state protocol
against the photon-number splitting attacks [15, 103] or
the Trojan-horse attacks [104] can be veriﬁed.
As the next step, the parties perform the sifting of
the raw key, its error correction, and privacy ampliﬁca-
tion. Finally, if these steps were successful, Alice and Bob
share a shorter but more secure key. Deﬁning the aver-
aging over channel ﬂuctuations with the applied beam
tracking procedure (66) as
⟨f(η)⟩tr =
1
Z
0
dη f(η) P(η)

σBW→σtr
,
(67)
we ﬁnd for the lower bound of the average secure key rate
R = q

−⟨Qµs⟩trf(QBER)H[QBER]
(68)
+
X
γ=x,z
⟨QγL
1 ⟩tr{1 −H[⟨eγU
1 QγL
1 ⟩tr/⟨QγL
1 ⟩tr]}

.
Here, q depends on the implemented protocol, H(x) =
−x log2(x) −(1 −x) log2(1 −x) is the binary Shannon
information function, Qµs is the gain of the signal states,
Q1 is the gain of single-photon states, and f(x) ≥1 is the
bidirectional error correction eﬃciency (f(x) = 1 corre-
sponds to the perfect error correction case). The quan-
tum bit error rate, QBER, is estimated as
QBER = ⟨EµsQµs⟩tr
⟨Qµs⟩tr
.
(69)
The gain Qµs represents the ratio between the number
of events where Bob observes a click under the condi-
tion that Alice sends a certain number of signal states.


## Page 15


15
This overall gain with respect to an ideal threshold de-
tector [105] can be evaluated as [102]
Qµs =
∞
X
i=0
Qs
i =
∞
X
i=0
Yi
µi
s
i! e−µs = 1 −e−ηdηµs(1 −Y0),
(70)
where the yield of the i-photon state is
Yi = 1 −(1 −Y0)(1 −ηdη)i.
(71)
Here
ηd = ηdetχextχopt
(72)
accounts for deterministic losses such as detector ef-
ﬁciency, channel losses due to atmospheric extinction
(10), and absorption by optical components, while η is
the random transmittance of the free-space channel [cf.
Eq. (28)]. Similarly, deﬁning the error rate of the i-state
as
eiYi = e0Y0 + edet[1 −(1 −ηdη)i](1 −Y0),
(73)
one derives for the overall error gain
EµsQµs =
∞
X
i=0
eiYi
µi
s
i! e−µs
(74)
= e0Y0 + edet(1 −e−ηdηµs)(1 −Y0).
Here, edet is the probability that an incorrect bit value
occurred that depends on the alignment and the stabil-
ity of the optical system. The background error rate is
e0 = 1/2 for randomly occurring dark and background
counts. The dark count contribution to Y0 is of order
10−6 for a commercially available Geiger-mode APD at
room temperature and can be further decreased with
proper cooling. The contribution from transmitted vac-
uum decoy states with the accounting of ﬁnite-size eﬀects
is given in Appendix G. The total value Y0 can be further
enhanced due to sky-noise photodetection [35, 106, 107].
In this article we assume that the background error rate
is constant with the value taken from Ref. [6].
For the determination of the single-photon gain, Q1,
and the single-photon error rate, e1, in Eq. (68) the sta-
tistical ﬂuctuations must be considered.
Indeed, since
the communication link with a LEO satellite can be es-
tablished for only several minutes, only a ﬁnite set of
data can be transmitted.
In the security analysis the
accounting for possible deviations from most probable
values must be taken into account. Moreover, statisti-
cal ﬂuctuations tend to become more important as the
distance of the QKD increases, i.e. for large values of
the zenith angle. In Ref. [102] the Gaussian model and
in Refs. [108, 109] the Chernoﬀ-Hoeﬀding method have
been applied for deriving ﬁnite-key security bounds. We
adopt the statistical ﬂuctuation analysis of Ref. [110] that
uses the Chernoﬀbound for establishing the lower bound
for single-photon gain,
QγL
1 (η) = Y γL
1
(η)µse−µs,
γ = x, z,
(75)
and the relation between the upper bounds for single-
photon error rates,
ezU
1 (η) = exU
1 (η) + θU,
(76)
in X and Z bases. Appendix G summarizes the method
for obtaining θU [cf.
Eq. (G17)], the lower bound for
the single-photon yield Y γL
1
[cf. Eq (G9)] and the upper
bound for the bit-ﬂip error rate exU
1
[cf. Eq. (G10)].
We calculate the secure key rate for the downlink com-
munication scenario.
Table III lists the values of pa-
rameters used in the calculation, whereas Table I gives
parameters of the atmospheric link and communication
system. With the source of repetition rate 150 MHz, the
total number of generated bits by Alice during 14 min-
utes of communication session is N = 1011. We estimate
the mean number of sifted key bits,
M a ≈ηsiftηdηN a,
a = s, d, v,
(77)
where ηsift = 0.5 is the sifting eﬃciency for conventional
sifting protocols. The number of sifted key bits is aver-
aged over the ﬂuctuations of the channel transmittance
and depends on the zenith angle (e.g., for zenith orbit
⟨M s⟩tr = 1.46×105, ⟨M d⟩tr = 5.64×104 for Za = 0◦, and
⟨M s⟩tr = 1.93×104, ⟨M d⟩tr = 7.43×103 for Za = 70◦).
TABLE III. Parameters for a QKD system.
Parameter
Notation
Value
Detector eﬃciency
ηdet
60%
Extinction due to optics
χopt
84%
Background yield (dark count)
Y DC
0
5.89 × 10−7
Erroneous detector prob.
edet
1%
Background error rate
e0
50%
Failure probability
ε
10−5
Mean intensity of signal
µs
0.8
weak decoy state
µd
0.1
Number of sent bits
N
1011
Pulse repetition rate
rN (MHz)
150
Generation prob. signal bits
ps
65%
weak decoy bits
pd
25%
Generation prob. of x-basis bits
px
a, (a=s, d)
60%
Error correction eﬃciency
f(QBER)
1.16
Tracking precision
σtr (µrad)
1
Figure 7 shows the QBER and the lower bound of the
secure key rate calculated for several inclination angles of
satellite orbits relative to the observer’s meridian plane.
For small zenith angles scintillations, atmospheric refrac-
tion, and absorption have minimal impact on the perfor-
mance of decoy-state protocols. The QBER has almost
constant value, the phenomenon that was theoretically
predicted for satellite links in Ref. [111] and experimen-
tally observed in Refs. [6, 39, 99]. Figure 7 a) shows a
similar behavior for the zenith angles where the aperture-
averaged scintillation index has the asymptotic behavior


## Page 16


16
∆ι=0◦
∆ι=25◦
∆ι=50◦
0.10
0.08
0.06
0.04
0.02
0.00
Time (min)
10−4
10−5
10−6
Secure key rate per pulse
QBER
a)
b)
FIG. 7.
Quantum bit error rates (a) and lower bounds of av-
eraged secure key rates (b) as functions of the communication
time for several inclination angles.
(27) and satisﬁes the condition σ2
η < 1. In the region of
saturated scintillations the QBER grows making quan-
tum communication impossible for large zenith angles. In
this region the wavefront distortions are maximal. These
distortions together with the extinction losses lower the
signal-to-noise ratio and correspondingly the QBER is in-
ﬂated by the larger relative contributions from the back-
ground. The ﬂat region of the QBER diminishes with
the growing inclination angle of the satellite orbit allow-
ing smaller time windows for the secure key exchange as
shown in Fig. 7 b).
It is worth to note that by placing the observer at
high altitudes above sea level this time window can be
increased.
Indeed, the thickness of the dense ground
layer, which is responsible for scintillation, is diﬀerent
at sea level and at high altitudes. This causes a shift of
the region with saturated scintillations to higher zenith
angles. This phenomenon can be observed if one com-
pares the curves of Fig. 4 calculated for the observer at
sea level with the experimental curve of Fig. 5 with ob-
server’s elevation of 602 m above sea level. The satu-
ration region may even vanish at particularly high alti-
tudes, the phenomenon which is known in optical astron-
omy [62, 67, 68]. This observation makes observatories in
mountains especially attractive as a OGS node for quan-
tum free-space communication with satellites.
VII.
CONCLUSIONS
In this article we have presented the theoretical anal-
ysis of satellite-mediated quantum links. We have dis-
cussed the inﬂuence of regular refraction, extinction, and
turbulence on the transmission properties of optical sig-
nals through the Earth’s atmosphere. Since in satellite-
mediated communication scenario the position of the
satellite changes rapidly for the observer located on the
Earth’s surface, the thoughtful analysis is presented of
how atmospheric disturbances depend on the observer’s
geographical position, observer’s zenith angle, and the
orbit inclination angle.
We focus our analysis on low orbit satellites with per-
fect polar orbit.
In particular, we considered the case
when the satellite orbit is inclined to the observer merid-
ian and derived the corresponding slant range. The orbit
inclination restricts the deﬁnition range of the zenith an-
gle by introducing the lower bound of the angle. As a
consequence, the most favorable satellite trajectory cor-
responds to the zenith orbit that passes through the ob-
server meridian. In this case, the smallest zenith angle
is zero and the slant range is the shortest one at the ob-
server zenith.
The eﬀect of regular atmospheric refraction increases
the optical slant range and changes the value of the true
zenith angle to the apparent one.
This eﬀect is espe-
cially pronounced near the horizon where it can increase
the propagation path of the optical signal up to 30%.
Based on the standard atmosphere model we derived the
corresponding path elongation factor as a function of the
apparent zenith angle and gave the corresponding analyt-
ical ﬁt formula. The resulting slant range has been used
for the calculation of the atmospheric extinction factor
due to absorption and scattering on atmospheric gases
and aerosols.
Another important factor that deteriorates the optical
performance of satellite-ground links is the atmospheric
turbulence. It appears that the second- and the fourth-
order optical ﬁeld correlation functions play a central role
in the description of light propagation through the tur-
bulent media. These functions allow one to derive the
aperture-averaged scintillation index, as well as the mean
beam-spot radius and the beam wandering variance of
the transmitted beam. Based on the properties of inten-
sity covariance function, we have derived an analytical
expression for the aperture-averaged scintillation index.
For large zenith angles these scintillations saturate and
decrease; this eﬀect is well observed in experiment. It
arises due to multiple scattering in most turbulent air
layers near the ground, the process that degrades the
performance of the receiver telescope and leads to the
additional aperture-averaging of scintillations. Based on
this simple model of aperture averaged scintillations, we
have developed the rigorous approach for calculating ﬁeld
correlation functions and their moments.
The developed description of atmospheric channels has
been adopted for the description of quantum light prop-
agation through the Earth’s atmosphere. For this sake
we use the input-output relations for optical ﬁeld oper-
ators, rewritten in terms of Glauber-Sudarshan P func-
tion. Fluctuations of the channel transmittance due to


## Page 17


17
atmospheric turbulence are accounted with the help of
the probability distribution of transmittance. We have
obtained the latter for satellite-mediated quantum links
using the law of total probability.
Finally, the security of quantum decoy-state communi-
cation protocols is analyzed with realistic channel param-
eters and communication conditions. In this connection,
the inclusion of the ﬁnite-key eﬀects plays an important
role. Scintillation phenomena at large zenith angles inﬂu-
ence greatly the performance of quantum channels, lead-
ing to a growth of the quantum bit error rate. In the re-
gion of saturated scintillations that appears close to the
horizon, no secure quantum key can be obtained. For
small zenith angles the quantum bit error rate has minor
variation that allows one to obtain secure key bits within
a certain time window. This window increases with the
decrease of the satellite inclination angle relative to ob-
server’s meridian plane. We also expect that the increase
of the observer’s altitude relative to the sea level will lead
to a decrease of the region with saturated scintillations
and hence to a better communication performance.
We have omitted several aspects aﬀecting the perfor-
mance of the satellite-mediated quantum communica-
tion. Background radiation from the Sun, Moon, stars,
or light reﬂected from the satellite introduce additional
noise.
This noise is detected by photodetectors, and
therefore, it increases the quantum bit error rate. The
use of light buﬀers, time gate, frequency, and spatial ﬁl-
ters can partially mitigate the problem of background
noise.
In this study we have neglected the parallax-
connected errors due to the Earth’s rotation during one
communication session. For observers at small geograph-
ical latitudes, and for the satellites with small altitude
such parallax eﬀects should be included in the rigorous
analysis. On the other hand, for the analysis of realis-
tic communication scenarios not only the instantaneous
position of a satellite relative to the observer is impor-
tant, but also the relative position of the Sun or of the
Moon. We refer to extensive literature that study the
inﬂuence of background noise and dark counts on the
satellite-mediated quantum key distribution.
Much less studied is the inﬂuence of random scattering
on atmospheric aerosols and dust particles on the per-
formance of satellite-based communication.
Especially
in overcast conditions the dominance of Mie scattering
makes the optical quantum communication with satel-
lites impossible. We have included in the model atmo-
spheric extinction eﬀects due to absorption and scatter-
ing on molecules and aerosols which correspond to aver-
age communication conditions. Under the conditions of
low visibility and overcast skies, the performed analysis
is not applicable.
Finally, here we have considered fundamental spatial
modes for the light beams that have Gaussian proﬁles
of the intensity distributions. The eﬃcient generation of
diﬀraction-free beams will allow one to reduce losses asso-
ciated with regular and random diﬀraction in free-space
and may extend the range of satellite-mediated quantum
communication.
ACKNOWLEDGMENTS
The work was supported by the Deutsche Forschungs-
gemeinschaft through projects VO 501/21-2 and VO
501/22-2.
The authors are grateful to A. A. Semenov
for useful and enlightening discussions.
Appendix A: Slant range of optical beam
In this appendix we derive the length of geometrical
distance between the satellite and the optical ground sta-
tion.
1.
Geometry of satellite communication links
The geometric path length for a speciﬁc communica-
tion scenario is determined from the value of the zenith
angle Z, which in turn is a function of the satellite orbit
inclination, the instant position of the satellite, and geo-
metric latitude of the observer. In the Earth surface coor-
dinate system of the observer the position of the satellite
is given by the zenith angle Z and the azimuth angle A.
The latter we measure from the north point eastwards.
In the Earth center (geocentric) coordinate system the
satellite position is determined by its declination angle
and its orbit inclination angle.
For circular orbits the
declination angle is given by
δ = ωsat(t−tPole),
(A1)
where ωsat = 2π/Tsat is the angular speed of the satellite
with orbiting period Tsat and tPole is the reference time
associated with the trajectory crossing either the North
or South Pole. During a single communication session
the declination angle changes from δ0 to δ0 + δcom with
δ0 being the initial declination of the satellite when it
appears on the observer horizon and
δcom = ωsattcom = 2 arctan
hp
H2 + 2R⊕H
R⊕
i
.
(A2)
Here tcom is the maximal duration of the communication
session, H is the satellite altitude above the ground, and
R⊕is the Earth radius.
Finally, the inclination angle
∆ι we deﬁne as the angle between the observer meridian
plane and the satellite orbit plane and the geographi-
cal latitude of the observer we denote as Ψ.
The set
{Ψ, δ, ∆ι} determines the instantaneous position of the
satellite relative to the observer in the geocentric coordi-
nate system and is the alternative parameter set to the
set {A, Z} in the Earth surface coordinate system.
The following relation between angles Z, δ, ∆ι, Ψ
shown in Fig. 8 can be established using spherical


## Page 18


18
ϕ
FIG. 8.
Geometric representation of the surface and geocen-
tric coordinate systems. The Earth surface coordinate system
for the observer showing the azimuth A and the zenith Z an-
gles.
The geocentric coordinate system is deﬁned in terms
of the declination angle δ and the inclination angle ∆ι. The
geographical position of the observer is given by the latitude
Ψ while the parallax correction caused by the ﬁniteness of the
satellite altitude H is determined by the angle ϕ.
trigonometry
cos ξ = sin Ψ sin δ + cos Ψ cos δ cos ∆ι,
(A3)
Z = arctan
 
sin ξ
cos ξ −
R⊕
R⊕+H
!
.
(A4)
Here δ changes during the communication session from
δ0 = −arctan(cos ∆ι cot Ψ) to δ0 + δcom. We note that
the ﬁnite value of the inclination angle ∆ι in (A4) re-
stricts the deﬁnition domain of Z to [Z∆ι
min, π/2] for the
observer located at the geographical latitude Ψ.
The
minimal value of Z can be found from Eq. (A4) as
Z∆ι
min = arccos
hp
1 −cos2 Ψ sin2 ∆ι
i
,
(A5)
which corresponds to the satellite declination angle
(counted from the Equator)
δ∆ι
min = arccos
"
cos Ψ cos ∆ι
p
1 −cos2 Ψ sin2 ∆ι
#
.
(A6)
The knowledge of the satellite declination angle, the or-
bit inclination angle, and geographical position of the
observer allows one to determine the instantaneous val-
ues of zenith angle from Eqs. (A4) as well as to determine
the slant range.
2.
Inclined and zenith orbits
In most practical cases the satellite trajectory is in-
clined relative to the observer zenith direction. For exam-
ple, the initial trajectory with zero inclination to the ob-
server’s zenith becomes inclined when the satellite makes
one or more revolutions.
Let us consider the satellite
whose orbit initially has zero inclination relative to the
meridian plane of the observer eO (see Fig. 9).
Let us
also assume that initially the satellite is positioned at
observer’s zenith, i.e., at point S′.
For simplicity we
consider the ideal polar orbit that passes through both
Earth’s celestial poles. After time Tsat, i.e., the satellite
orbiting period, the satellite is positioned again in the
point S′. Meanwhile the observer position eO is moved
to the point O due to Earth’s rotation. The resulting
inclination angle reads as
∆ι = Tsatv⊕
R⊕
,
(A7)
where v⊕is the speed of Earth’s rotation at the Equator.
Here and in the following we assume that the change of
the inclination angle during the satellite transition over
the observer horizon is relatively small, so that we can ap-
proximate it being constant (A7) during the whole com-
munication session. The negative values of ∆ι refer to
situations when the visible satellite trajectory is posi-
tioned eastwards to the observer. We calculate the slant
range between O and S along the satellite orbit provided
the trajectory S′S of the moving satellite lies above the
observer horizon H.
The instantaneous position of the satellite relative to
the observer is determined by zenith Z and azimuth A
angles as shown in Fig. 8. For satellite tracking purposes
both these angles are of importance. In the context of
optical satellite-based communication we are interested
primarily in the instantaneous value of the slant range
as a function of zenith angle. Indeed, by assuming that
tracking systems point correctly the telescope towards
the ﬂying satellite, we can can ignore the dependence of
the slant range on the azimuth angle. Then, the slant
range L for the inclined orbit can be determined from
the triangle OSC in Fig. 2 using the law of cosines
L2 + R2
⊕−2LR⊕cos(π −Z) = (R⊕+ H)2.
(A8)
Solving this equation with respect to L we obtain
L(Z) =
q
H2 + 2HR⊕+ R2
⊕cos2 Z −R⊕cos Z.
(A9)
The root of the quadratic equation (A8) is chosen to yield
the non-negative slant range.
At the observer’s hori-
zon the slant range reaches its maximal value L(90◦)=
q
(R⊕+ H)2 −R2
⊕≈
p
2HR⊕.
The shortest slant
range is determined as L(Z∆ι
min), where the minimal
zenith angle is given by Eq. (A5).
The special case of the slant range (A9) corresponds
to the zenith satellite orbit with zero inclination angle


## Page 19


19
N
˜
˜
FIG. 9.
Geometry of a typical satellite-ground communi-
cation. Initially, the ground observer eO establishes the com-
munication link with the satellite whose trajectory lies within
the meridian plane of the observer eO. At a later time, due
to Earth’s rotation, the observer is translated to the point O
while the satellite trajectory is inclined by an angle ∆ι rel-
ative to the new observer meridian plane (or ﬁctitious orbit
plane). Circles eH and H denote the local horizons of the ob-
servers eO and O, respectively. The communication between
the observer O and the satellite S can be established provided
the satellite trajectory S′S lies above the horizon H.
∆ι.
Some authors refer to this orbit as to the ”best
pass” [42] since the slant range, that we denote as L0,
gives the shortest distance between the observer and the
satellite at zenith, namely, L0(0◦) = H. This fact makes
the zenith orbit as well as the orbits with small incli-
nation angle ∆ι most attractive for the optical commu-
nication.
Denoting the zenith angle within the zenith
orbit plane (observer’s meridian plane) as Z0, it follows
from Eq. (A4) that Z0 = Ψ −δ. Consequently, we have
L0(Z0) = L(Z)

∆ι=0.
Appendix B: Standard Atmosphere
The standard atmosphere is an idealized model of the
Earth’s atmosphere for heights ranging from the surface
to 1000 km [52]. The model yields the air density, vis-
cosity, etc., for various altitudes. For our purposes, the
most useful values calculated within the standard atmo-
sphere model are the temperature T and the pressure P.
These variables are important for the calculation of the
refractive index variation with altitude.
The altitude dependence of the temperature is approx-
imated with linear segments
T(h) = Tb +
dT
dh

b
(h −Hb).
(B1)
Each segment lies within an atmospheric layer bounded
by the surfaces with the altitudes Hb−1 and Hb. Table
IV summarizes the reference values Tb and the vertical
gradient values of temperature (lapse rates)
λb = (dT/dh)b,
(B2)
which enter Eq. (B1). The altitude dependence of pres-
sure can be found from the gas law and hydrostatic equa-
tion and reads as
P = Pb

1 + λb
Tb
(h −Hb)
−g/λbR
(B3)
for constant lapse rate and
P = Pb exp [−(h −Hb) g/RTb]
(B4)
for isothermal layers (λb = 0). Here g = 9.8 m/s2 is the
gravitational acceleration and R = 287.053 J/kg · K is
the gas constant for air. The reference values of pressure
Pb are given in Table IV.
TABLE IV. The reference altitudes and values and gradients
of the linearly segmented temperature-height and pressure-
height proﬁles from the Earth’s surface up to altitude of 85
km.
Sub-
Height
Temperature
Temperature
Pressure
script
gradient
b
Hb, (km)
λb, (K/km)
Tb, (K)
Pb, (mb)
0
0
-6.5
288
1 013
1
11
0.0
217
226
2
20
+1.0
217
54.7
3
32
+2.8
229
8.68
4
47
0.0
271
1.11
5
51
-2.8
271
0.67
6
71
-2.0
215
0.04
7
84.8
-
188
0.004
Following Birch and Downs [54] we adopt the revised
form of the Edl´en equation for the atmospheric refractive
index n,
(n −1) = (P/Pa)(n −1)s
96095.43
× 1 + 10−8(0.601 −0.00972T/◦C)P/Pa
1 + 0.0036610 T/◦C
,
(B5)
where (n −1)s is given by the dispersion equation
(n −1)s × 108 = 8342.54
+ 2406147
h
130 −(1/λ)2i−1
(B6)
+ 15998
h
38.9 −(1/λ)2i−1
.
Here λ is the optical wavelength given in µm. Since the
values of the refractive index are distinct from the vac-
uum value n = 1 up to the mesosphere, we restrict our
attention only to altitudes ranging from 0 to 85 km.


## Page 20


20
Figure 10 shows the variation of temperature, pressure
and refractive index with altitude. The temperature pro-
ﬁle shows several layers where temperature dependence
on altitude can be approximated by linear relations. We
use these speciﬁc altitudes for the calculation of the re-
fractive index proﬁle using linear segmentation. Such a
procedure simpliﬁes the calculation of atmospheric re-
fraction but introduces errors that grow for large zenith
angles Z ∼90◦. The altitude dependence of the refrac-
tive index within the ith segment reads as
ni(h) = ni +
dn
dh

i
(Hi −h).
(B7)
Table V summarizes the corresponding values of the re-
fractive index values and gradients for the corresponding
segments.
TABLE V. The deﬁned reference levels, gradients, and values
of the linearly segmented refractive index-height proﬁles from
surface to 85 km.
Sub-
Height
Refractive index
Refractive index
script
gradient
i
Hi, (km) (dn/dh)i ×10−6, (km−1)
(ni −1) × 108
0
0
-
27 340
1
5
25.68
14 660
2
7
17.58
11 142
3
11
12.50
6 141
4
15
7.183
3 268
5
20
3.565
1 485
6
32
1.042
235
7
47
0.134
34
8
51
0.034
21
9
71
0.010
1
10
84.8
0.001
0.1
For the calculation of the deterministic atmospheric ex-
tinction, the number density of absorbing and scattering
particles is required.
The standard atmosphere model
gives the following dependence of the relative number
density on altitude h (given in meters) [58],
N(h)/N0 = exp

−h/H0

.
(B8)
Here N0 is the number density at the observer level (N0 =
2.55 × 1025 m−3 at sea level) and H0 = 6 600 m.
Appendix C: Path elongation due to atmospheric
refraction
In the presence of Earth’s atmosphere, the slant path L
is elongated due to refraction on interfaces of atmospheric
layers with diﬀerent refractive indices (see Fig. 11). In
the real atmosphere the gradient of the refractive index is
a continuous function of height. We use the standard at-
mosphere model and consider 10 atmospheric layers (c.f.
Altitude (km)
Troposphere
Stratosphere
Mesosphere
80
60
40
20
0
Refractive index,
(n −1) × 105
Temperature (K)
Pressure (mb)
FIG. 10.
Temperature, pressure and refractive index as
functions of altitude. Dots represent the standard atmosphere
values and lines show the linear approximation of temperature
and refractive index curves used in this article, as well as the
functional dependence (B3), (B4) for the pressure.
Appendix B, Table V). The refractive index is linearly
segmented, such that it is a linear function of height
within one layer [cf. Eq. (B7)].
As a consequence of atmospheric refraction the appar-
ent zenith angle Za starts to deviate from the true zenith
angle Z. These angles are related with each other as
Za = arcsin
 1
n0
sin Z

,
(C1)
where n0 = 1.00027 is the refractive index of the lower
layer of atmosphere [54]. Near sea level the two zenith
angles diﬀer by approximately a minute of arc at Z = 45◦
and half a degree near the horizon.
Refraction of optical rays happens on the ith interface
of two adjoined ith and (i+1)th layers of heights Hi and
Hi+1, correspondingly, and is characterized by the angle
of incidence π/2 −βi and the angle of refraction ψi (see
Fig. 11). If the ray enters the observer telescope at the
zenith angle Za, Snell’s law yields the geometric invariant
n0R⊕cos α01 = ni(R⊕+ Hi) cos βi = const,
(C2)
where
α01 = π/2 −Za
(C3)
is the elevation angle at the observer O and R⊕is the
Earth radius. Using the notation
Ci =
R⊕
R⊕+ Hi
,
CH =
R⊕
R⊕+ H
(C4)


## Page 21


21
FIG. 11.
The inﬂuence of atmospheric refraction on the
elongation of the optical ray trajectory (a). The geometrical
path of length OS deforms into the curved path OP1P2...PnS
while the true zenith angle Z changes to the apparent zenith
angle Za. The magniﬁed upper part of the ray path shows
the relevant refraction angles b).
with H being the altitude of the satellite above the
ground we derive from Eq. (C2)
βi = arccos
n0
ni
Ci sin Za

= arccos
Ci
ni
sin Z

,
βN = arccos (n0CH sin Za) = arccos (CH sin Z) , (C5)
where the index N corresponds to the last atmospheric
layer at altitude 85 km which is accounted in our cal-
culations (in our case N = 10). We also use the index
i = 1, ..., N to denote the atmospheric layers above the
ground level.
Using simple geometric considerations and Snell’s law,
we derive the following relations for the angles relevant
for the calculation of the ray path length,
αi = arccos
 ni
ni−1
cos βi

,
(C6)
α0i = αi −α0(i−1) + βi + χi + ψi −Za,
i ̸= 1,
(C7)
χi = ri −(αi −βi),
(C8)
ψ1 = π −Za −δ1 −α1 + α01 −χ1,
(C9)
ψi = arcsin
 Ci
Ci−1
sin[Za −βi−1 + α0(i−1)]

,
i ̸= 1,
(C10)
ψ = arcsin
CH
CN
sin[rN −δN + ψN]

.
(C11)
The remaining angles to be determined are δi and ri. The
former angle is associated with the local elevation angle
error and can be found from the law of sines
(R⊕+ Hi−1) cos α0i = (R⊕+ Hi) cos αi,
(C12)
(R⊕+ Hi−1) cos (α0i −δi) = (R⊕+ Hi) cos (αi + χi −δi) .
(C13)
Solving these equations with respect to δi we derive
tan δi =
cos αi −cos(αi + χi)
sin(αi + χi) −Ci/Ci−1 sin α0i
,
(C14)
tan δN =
cos αN −cos(αN + χN)
sin(αN + χN) −CH/CN sin α0N
.
(C15)
The remaining angle ri is the bending angle within an ith
layer which is calculated from the refraction integral [48],
ri=
Hi
Z
Hi−1
dh 1
n
dn
dh
cos βi−1
p
(nCi−1/ni−1Ci)2−cos2 βi−1
. (C16)
The total angle r = P
i ri is known in optical astronomy
as atmospheric refraction. It can be shown that the re-
fraction integral (C16) can be simpliﬁed to the following
approximate analytical form,
ri ≈2
ni−1 −ni
tan βi + tan βi−1
,
(C17)
provided that Hi −Hi−1 ≪Hi−1 and if the refractive
index gradient dn/dh is constant within the atmospheric
layer.
The length of the optical ray path inside the ith layer
can be found from the triangle CPi−1Pi applying the law
of cosines
Li=
n
(R⊕+Hi−1)2+(R⊕+Hi)2
(C18)
−2(R⊕+Hi−1)(R⊕+Hi) cos [Φ(Za, ri)]
o1/2
,
Φ(Za, ri) = αi−α0i+χi.
(C19)
For the optical path length in vacuum we ﬁnd from the
triangle CPNS
LN+1=
n
(R⊕+HN)2+(R⊕+H)2
(C20)
−2(R⊕+HN)(R⊕+H) cos [Θ(Za, rN)]
o1/2
.
Herein we need the angle
Θ(Za, rN) = rN−δN+ψN −ψ.
(C21)


## Page 22


22
The ratio of the total length of the ray trajectory to the
geometric path length [c.f. Eq. (1)] reads as,
εr = 1
L
N+1
X
i=1
Li,
(C22)
which is the elongation factor due to atmospheric refrac-
tion.
The elongation factor (C22) is calculated without tak-
ing into account the ﬁnite radius of curvature of optical
rays. Actually, the beam curvature near the ground is
the smallest one, i.e. the ray bending is the greatest. In
this case the empirical function for ray curvature K is
given by [55, 56]
K = R⊕

670.87 P
T 2

0.034 + λ(h)10−3
sin Za
−1
,
(C23)
where T is the temperature in K, P is the pressure in
mb, λ(h) = dT/dh is the lapse rate in K/km. For the
standard atmosphere at Za = 90◦the curvature reaches
its minimum value of 4.4R⊕. Since this value is still larger
than the Earth’s radius, we can assume that the optical
rays within each atmospheric layer can be considered to
be straight lines.
Appendix D: Atmospheric model of optical
turbulence
Dewan et al.
[112] proposed a simpliﬁed version of
the multiparameter VanZandt model [113] for the refrac-
tive index structure parameter variation with altitude.
This so-called Air Force Geophysics Laboratory (AFGL)
model utilizes the meteorological data derived from ra-
diosondes and yields the following analytic formula for
the refractive-index structure parameter proﬁle:
C2
n(h) = 2.8 [M(h)]2 (0.1)
4
3 10Y (h).
(D1)
Here the factors (0.1)4/310Y (h) determine the outer scale
of turbulence in a statistical manner. The function Y (h)
is empirically related with the altitude-dependent wind
shear S(h) and the lapse rate λ(h) as [114]
Y (h) = 2.9767+27.9804S(h)+2.9012λ(h)+1.1843λ(h)2+0.1741λ(h)3+0.0086λ(h)4,
(lower troposphere)
(D2)
= 0.7152+30.6024S(h)+0.0003λ(h)−0.0057λ(h)2−0.0016λ(h)3+0.0001λ(h)4,
(troposphere)
(D3)
= 0.6763+8.1569S(h)−0.0536λ(h)+0.0084λ(h)2−0.0007λ(h)3+0.00002λ(h)4.
(stratosphere).
(D4)
The parameter M is connected with the gradient of the
index of refraction,
M(h) = −79 × 10−6P(h)N 2(h)
gT(h)
,
(D5)
where P is the pressure in mb, the temperature T is given
in K, the buoyancy frequency (Brunt-V¨ais¨al¨a frequency)
in s−1. The buoyancy frequency reads as
N 2 = g [λ(h) + γ]
T(h)
,
(D6)
where g is the acceleration of gravity, and γ = 9.8 K/km
is the dry air adiabatic lapse rate.
The altitude de-
pendencies of pressure and temperature are governed by
Eqs. (B1), (B3), and (B4).
The altitude variation of the refractive index structure
parameter can be determined from Eq. (D1), provided
the altitude variation of the wind shear S(h) is known.
In this study we assume horizontal homogeneity of the
atmosphere, which means that the mean wind proper-
ties do not depend on the horizontal position of the ob-
server. Thus, we assume a ﬂat terrain and neglect any
spatial inhomogeneity of Earth’s surface. This assump-
tion is equivalent to the independence of the vertical wind
component on altitude [115]. For the determination of
the vertical wind shear components due to meridional
and zonal winds we use the HWM93 thermospheric wind
model [116]. The examples of winds and corresponding
shear components are shown in Fig. 12 for summer night
and the observer located near Munich [117].
For the atmospheric boundary layer close to the
Earth’s surface, the refractive index structure parameter
given by Eq. (D1) is not applicable. We use the Walters
and Kunkel model (WK) [118] for the C2
n proﬁle within
the boundary layer,
C2
n(h)
C2n(h0) = (h/h0)−2/3,
h0, h ≤hi
(D7)
for nighttime and
C2
n(h)
C2n(h0) =
(h/h0)−4/3,
h0, h ≤0.5hi,
(0.5hi/h0)−4/3,
0.5hi ≤h ≤0.7hi,
2.9(0.5hi/h0)−4/3(h/hi)3, 0.7hi ≤h ≤hi
(D8)
for daytime. Here hi is the height of the inversion layer
above the ground (hi ∼0.5 km at nighttime and ∼1 km
at daytime), h0 is the reference height referred to as the


## Page 23


23
-
70
60
50
40
30
20
10
0
−20
−
Meridional
Zonal
Altitude (km)
FIG. 12.
Typical example of the mean meridional (solid
line) and the zonal (dashed) winds is shown together with
the corresponding vertical wind shear components.
The
HWM93 empirical wind model [116] for the northern hemi-
sphere (48◦N, 11.5◦E) summer (day 236) at midnight has
been used for the calculation.
Monin-Obukhov scale (h0 ∼10 m at nighttime and ∼
5 m at daytime).
35
30
25
20
15
10
5
0
10−22
10−20
10−18
10−16
10−14
Hufnagel
AFGL+WK, day
AFGL+WK, night
Thermosonde
1
0.1
0.01
0.
Altitude,h/hi
C2
n(h)/C2
n(h0)
FIG. 13.
Proﬁles of the refractive index structure func-
tion: AFGL, WK, and Hufnagel models are compared to the
thermosonde data adopted from Ref. [120]. The inset shows
the refractive-index structure parameter within the boundary
layer with respect to the inversion height.
Figure 13 shows the proﬁle of the refractive-index
structure parameter calculated using the AFGL and the
WK models [cf. Eqs. (D1), (D7), and (D8)]. For com-
parison, the widely used Hufnagel model [119] as well as
the estimation of C2
n based on thermosonde data [120]
are shown. The AFGL+WK model agrees better with
the experimental proﬁle than the Hufnagel model. The
diﬀerence between nighttime and daytime proﬁles is neg-
ligibly small for the altitudes above the inversion layer
height hi. Figure 12 shows the diﬀerent behavior of the
wind shear for meridional and zonal winds. However this
anisotropy has almost no inﬂuence on the C2
n proﬁle. As
a consequence, we could neglect the dependence of this
turbulence characteristics on the direction of view of the
observer.
Finally, we relate the vertical proﬁle C2
n(h) to the cor-
responding proﬁle along the slant range. For the uplink
conﬁguration, the relation between the height h of the
certain point along the slant path and the distance be-
tween this point and the light source, Lrξ, ξ ∈[0, 1], can
be found from the law of cosines [cf. Ref. [61] and see
Fig. 2 (a)]
hUL(ξ) = R⊕
s
1 + 2 Lξ
R⊕
cos Z + (Lξ)2
R2
⊕
−R⊕
(D9)
≈R⊕
s
1 + 2Lrξ
R⊕
cos Za + (Lrξ)2
R2
⊕
−R⊕.
Similarly, for the downlink we derive by replacing ξ →
1 −ξ
hDL(ξ) ≈R⊕
s
1 + 2Lr[1 −ξ]
R⊕
cos Za + (Lr[1 −ξ])2
R2
⊕
−R⊕.
(D10)
Under the condition Lr/R⊕≪1, these equations reduce
to
hUL(ξ) ≈Lrξ cos Za,
(D11)
hDL(ξ) ≈Lr(1 −ξ) cos Za.
(D12)
The refractive index structure parameter given by
Eqs. (D1), (D7), and (D8) maps for the uplink slant range
as C2
n(h) →C2
n(hUL) = C2
n(Lr, ξ) and for the downlink
as C2
n(h) →C2
n(Lr, 1 −ξ).
Appendix E: Approximation of Eq. (38) for
satellite-mediated links
In this appendix we give the approximation for the
integral kernel (38). We consider the downlink conﬁg-
uration and just note that the formulas for uplink are
obtained in the similar footing with the variable replace-
ment ξ →1 −ξ. For the case of strong turbulence or
long propagation distances in turbulence the coherence
radius ρ0 [cf. Eq. (25)] is small. This condition is well
satisﬁed for satellite-mediated atmospheric links. In this
case, the exponential in Eq. (38), J (r, r′
1, r′
2, r′
3), diﬀers
signiﬁcantly from zero in the following regions:
|r′
2|ξ ≫ρ0,
|r′
3|ξ, |r(1−ξ)+r′
1ξ| ≲ρ0;
(E1)
|r(1−ξ)+r′
1ξ| ≫ρ0,
|r′
2|ξ, |r′
3|ξ ≲ρ0;
(E2)
|r′
2|ξ, |r′
3|ξ, |r(1−ξ)+r′
1ξ| ≲ρ0.
(E3)
The function (38) can be approximated then as linear
combination of three terms [77, 121]
J = J1 + J2 −J3,
(E4)


## Page 24


24
J1(r, r′
1, r′
2, r′
3) = exp
h
−ρ
−5
3
0
1
Z
0
dξ C2
n(Lr, 1−ξ)
C2
n,0
X
j=1,2
r(1−ξ)+[r′
1+(−1)jr′
3]ξ

5
3 i
(E5)
×
∞
X
n=0
ρ
−5
3 n
0
n!
n 1
Z
0
dξ C2
n(Lr, 1−ξ)
C2
n,0
X
j=1,2
r(1−ξ)+[r′
1+(−1)jr′
2]ξ

5
3 −
[r′
2+(−1)jr′
3]ξ

5
3 on
,
J2(r, r′
1, r′
2, r′
3) = exp
h
−ρ
−5
3
0
1
Z
0
dξ C2
n(Lr, 1−ξ)
C2
n,0
[r′
2+(−1)jr′
3]ξ

5
3 i
(E6)
×
∞
X
n=0
ρ
−5
3 n
0
n!
n 1
Z
0
dξ C2
n(Lr, 1−ξ)
C2
n,0
X
j=1,2
r(1−ξ)+[r′
1+(−1)jr′
2]ξ

5
3 −
r(1−ξ)+[r′
1+(−1)jr′
3]ξ

5
3 on
,
J3(r, r′
1, r′
2, r′
3) = exp
h
−ρ
−5
3
0
1
Z
0
dξ C2
n(Lr, 1−ξ)
C2
n,0
X
j=1,2
n[r′
2+(−1)jr′
3]ξ

5
3
(E7)
+
r(1−ξ)+[r′
1+(−1)jr′
3]ξ

5
3 oi ∞
X
n=0
ρ
−5
3 n
0
n!
n 1
Z
0
dξ C2
n(Lr, 1−ξ)
C2
n,0
X
j=1,2
r(1−ξ)+[r′
1+(−1)jr′
2]ξ

5
3 on
.
The ﬁrst term (E5) accounts for the contributions from regions (E1) and (E3). The term (E6) accounts for the regions
(E2) and (E3), while the term (E7) eliminates the double counting of the region (E3) in the integral kernel J . In the
ﬁrst approximation (n = 0) we have
J (r, r′
1, r′
2, r′
3)
≈exp
h
−ρ
−5
3
0
1
Z
0
dξ C2
n(Lr, 1−ξ)
C2
n,0
X
j=1,2
r(1−ξ)+[r′
1+(−1)jr′
3]ξ

5
3 i
+ exp
h
−ρ
−5
3
0
1
Z
0
dξ C2
n(Lr, 1−ξ)
C2
n,0
[r′
2+(−1)jr′
3]ξ

5
3 i
−exp
h
−ρ
−5
3
0
1
Z
0
dξ C2
n(Lr, 1−ξ))
C2
n,0
X
j=1,2
n[r′
2+(−1)jr′
3]ξ

5
3 +
r(1 −ξ)+[r′
1+(−1)jr′
3]ξ

5
3 oi
,
(E8)
which already gives a good approximation to the kernel J (cf. Ref. [77]).
Appendix F: Phenomenological model of
aperture-averaged scintillations
The rigorous analysis of satellite-mediated quantum
communication links should account for turbulent dis-
turbances for a wide range of the zenith angle. Here we
calculate the aperture averaged scintillation index with
accounting for saturation eﬀects. The aperture-averaged
scintillation index can be obtained by substitution of
Eq. (28) in Eq. (27), which leads to [40] 3
σ2
η =
1
⟨I⟩2
Z
R2 d2κFI(κ, Lr)fA(κ),
(F1)
where
fA(κ) =

1
A
Z
A
d2reiκ·r

2
(F2)
3 Originally, the expression for the scintillation index for the
log transmittance,
σ2
log η,
is derived in the chapter 13 of
Ref. [40].
Equation (F1) is then obtained from the relation
σ2
η = exp[σ2
log η] −1 (cf. Ref. [41]).


## Page 25


25
is the aperture ﬁlter function, and ⟨I⟩is the mean inten-
sity. The Fourier transformed correlation function of the
intensity ﬂuctuations is given by
FI(κ, Lr) =
Z
R2
d2rBI(r, Lr)e−iκ·r,
(F3)
BI(r1−r2, Lr) = ⟨[I(r1, Lr)−⟨I⟩] [I(r2, Lr)−⟨I⟩]⟩.
For a circular aperture of radius a the ﬁlter function (F2)
is easily evaluated to be
fA(κ) = fa(κ) =
2J1(κa)
κa
2
,
(F4)
where κ = |κ| and Jn(x) is a Bessel function of the ﬁrst
kind.
In the limiting case of the vanishingly small Fresnel
number Ω= kW 2
0 /(2Lr) →0 the collimated beam with
the initial beam spot size W0 can be considered as a
plane wave. Indeed, for the satellite-mediated link under
consideration the slant range Lr is large enough even at
the zenith and Ω→0. In this limiting case the intensity
spectral density FI(κ, Lr) can be obtained by solving the
equations of geometrical optics [40]4
FI(κ, Lr) = 2π⟨I⟩2κ4
Lr
Z
0
dzz2Φn(κ, z),
(F5)
where the turbulence spectrum Φn is given in Eq. (16).
For the Kolmogorov turbulence spectrum (18) the inten-
sity spectral density FI(κ, Lr) is proportional to κ1/3 in
the inertial range. Thus, for large values of the trans-
verse wave number the intensity spectral function di-
verges.
In order to remedy this nonphysical eﬀect we
introduce the cutoﬀof higher spatial frequencies ∆κ such
that κ ∈[0, ∆κ]. The speciﬁcal choice of ∆κ will be dis-
cussed later in this appendix. Taking into account this
cutoﬀeﬀect the aperture averaged scintillation index is
calculated straightforwardly,
σ2
η = 16π2
a2
Lr
Z
0
dzz2
∆κ
Z
0
dκκ3Φn(κ, z) [J1(κa)]2 .
(F6)
The obtained result shows that the intensity ﬂuctuations
are directly related to spectrum of turbulent ﬂuctuations
of the refractive index.
For the Kolmogorov turbulence spectrum (18) the in-
tegrations can be performed, provided the altitude de-
pendence of structure constant is known. Here we adopt
a simple dependence on the z variable assuming that the
4 Reference [40] derives the formula for the logarithmic amplitude
of the light wave χ = log(A/A0). Under weak ﬂuctuation condi-
tions the relation FI(κ, Lr) = 4⟨I⟩2Fχ(κ, Lr) is valid [41].
strongest turbulence is near the Earth surface and de-
creases exponentially with the height [71],
C2
n(z) = C2
n,0 exp

−
z
H0 sec Za

.
(F7)
Here H0 is the characteristic length at zenith and the
factor sec Za accounts for the increase of this length for
the slant paths. The integral with respect to z in Eq. (F6)
is evaluated as
I(Za) = 2(H0 sec Za)3 −exp

−Lr(Za)
H0 sec Za

H0 sec Za
×

2(H0 sec Za)2 + 2H0 sec ZaLr(Za) + L2
r(Za)
	
.
(F8)
In the limit of inﬁnitely distant light source, Lr →∞,
we get I(Za) = 2(H0 sec Za)3. Consequently, the scintil-
lation index (F6) for ∆κ →∞has the same dependence
on the zenith angle as those obtained within the Rytov
approximation, cf. Eq. (27).
The cutoﬀspatial frequency ∆κ in Eq. (F6) can be es-
timated from the following considerations. The rigorous
asymptotic analysis shows [122] that for long propaga-
tion paths the covariance function BI(r, Lr) in Eq. (F5)
diﬀers from zero if |r| ≤∆r, where
∆r = 0.18λLturb/ρ0.
(F9)
Here, λ is the optical wavelength, Lturb is the propagation
path length in turbulence, and ρ0 is the spatial coherence
length given by Eq. (25). According to Eq. (F7) the tur-
bulence is suﬃcient for heights h ≤H0. Hence, without
loss of generality we set Lturb = H0 sec Za. The ﬁnite-
ness of the deﬁnition domain for the covariance func-
tion BI(r, Lr) introduces the cutoﬀfrequency ∆κ for the
spectral density FI(κ, Lr). Using the relation of Fourier
analysis ∆κ∆r ≥µ, we may estimate ∆κ = µ/∆r, where
µ ∼1 is a phenomenological parameter. It is easy to see
that ∆κ ∝(sec Za)−8/5 and decreases while the zenith
angle approaches the horizon. For further insight into
physical meaning of the parameters ∆r and ∆κ we point
the reader’s attention on Ref. [123]. Finally, performing
the integration of (F6) over κ and over z variable [cf.
Eq. (F8)] we obtain Eq. (49), where only the ﬁrst term
of I(Za) is accounted. At the cost of analytic simplic-
ity, the obtained result can be further generalized for the
case of Cassegrain-type apertures with the inner circular
obscuration [94].
Appendix G: Decoy state: statistical ﬂuctuation
analysis
In this appendix, we summarize the method for estima-
tion the lower (upper) bounds of single-photon gain and
error rate taking into account the ﬁnite-key eﬀects [110].
On quantum state preparation stage, Alice generates
each bit in her raw key by randomly choosing the en-
coding basis (X or Z) and the intensity (corresponding


## Page 26


26
to the vacuum state, weak decoy state, and signal state).
The total number of bits sent by Alice to Bob is given by
N = N s + N d + N v,
(G1)
where the superscripts correspond to signal (s), weak-
decoy (d), and vacuum (v) states. We denote qa = N a/N
as the rate with which Alice encodes a state with intensity
µa, a = s, d, v. The conditional probability that an i-
photon state corresponds to a coherent pulse with the
intensity µa is
pa
i ≈N a
i
Ni
=
N ae−µa(µa)i/i!
P
α∈{s,d,v} N αe−µα(µα)i/i!,
(G2)
where the approximation sign is due to statistical ﬂuctu-
ations. The ﬁniteness of numbers of generated bits yields
q = N s
2N
(G3)
for the q parameter in Eq. (68).
Bob measures the received states in X or Z basis cho-
sen randomly. After basis reconciliation and key sifting,
Bob possesses the total number of sifted bits
M = M s + M d + M v.
(G4)
For the atmospheric quantum channel, the bit numbers
N and M are related as
M = 1
2ηdηN,
(G5)
where the factor 1/2 is due to the sifting procedure, ηd is
the deterministic channel loss including the detector eﬃ-
ciency given by Eq. (72), and η is the ﬂuctuating channel
transmittance. The bit number corresponding to the i-
photon state is determined as
M a
i ≈pa
i Mi = pa
i
X
α∈{s,d,v}
M αe−µα(µα)i/i!,
(G6)
where pa
1 is the same as the probability (G2) chosen by
Alice.
After error correction and error veriﬁcation the secure
key rate depends on a lower bound, on the gain of single-
photon components of the signal state QL
1 and an upper
bound, on the corresponding error rate eU
1 . The estima-
tion of QL
1 and eU
1 should be performed in each basis. The
corresponding components we denote by superscripts x
and z referring to the X and Z bases, correspondingly.
For the Z basis the bounds on the single-photon gain and
the error rate are given by
QzL
1
= Y zL
1
µse−µs,
(G7)
ezU
1
= exU
1
+ θU,
(G8)
where
Y γL
1
=
µs
µsµd −µ2
d

QγL
µd eµd −µ2
d
µ2s
QγU
µs eµs
(G9)
−µ2
s −µ2
d
µ2s
Y U
0

,
γ = x, z,
exU
1
= (EµdQx
µd)Ueµd −e0Y L
0
µdY xL
1
.
(G10)
Here e0 = 1/2 and the lower and upper bounds
QzL
µd =
Qz
µd
1 + δ(M dz) =
Qz
µd
1 + δ(N dzQzµd),
(G11)
QzU
µs =
Qz
µs
1 −δ(N szQzµs),
(G12)
Y L
0 =
Y0
1 + δ(N vY0),
Y U
0 =
Y0
1 −δ(N vY0),
(G13)
(EµdQx
µd)U =
Ex
µdQx
µd
1 −δ(N dxExµdQxµd)
(G14)
are estimated by using the Chernoﬀbound method and
are related to the overall gain (70), with the overall quan-
tum bit error rate (74) components, and with the count-
ing rate for vacuum decoy states and dark count contri-
butions
Y0 =
M v
N(e−µsqs + e−µdqd + qv) + Y DC
0
.
(G15)
The deviation function
δ(x) = −3 ln(ε/2) +
p
[ln(ε/2)]2 −8 ln(ε/2)x
2[x + log(ε/2)]
(G16)
can be determined for the speciﬁed failure probability ε.
Finally, the upper bound θU in (G8) is obtained by
numerically solving
ε =
p
⟨M xL
1 ⟩tr + ⟨M szL
1
⟩tr
p
⟨exU
1 ⟩tr(1 −⟨exU
1 ⟩tr)⟨M xL
1 ⟩tr⟨M szL
1
⟩tr
(G17)
× 2−(⟨M xL
1
⟩tr+⟨M szL
1
⟩tr)ξ(θU)
with respect to θU [110, 124]. Here, the averaging ⟨...⟩tr
is performed according to Eq. (67) and the lower bounds
of sifted key numbers are
M γL
1
= Y γL
1
N(e−µsµsqs + e−µdµdqd),
γ = x, z,
(G18)
M szL
1
= [1 −δ(ps
1M zL
1 )]ps
1M zL
1
(G19)
with qa = N a/N. In Eq. (G17) the exponential function
ξ(θ) read as [124]
ξ(θ) ≈ln 2
2
(1 −qx)qx
(1 −⟨exU
1 ⟩tr)⟨exU
1 ⟩tr
θ2,
(G20)
where qx=⟨M xL
1 ⟩tr/(⟨M xL
1 ⟩tr+⟨M szL
1
⟩tr) is the bias ra-
tio.


## Page 27


27
[1] G. Vallone, D. Bacco, D. Dequal, S. Gaiarin, V.
Luceri, G. Bianco, and P. Villoresi, Experimental Satel-
lite Quantum Communications, Phys. Rev. Lett. 115,
040502 (2015).
[2] G. Vallone, D. Dequal, M. Tomasin, F. Vedovato, M.
Schiavon, V. Luceri, G. Bianco, and P. Villoresi, In-
terference at the Single Photon Level Along Satellite-
Ground Channels, Phys. Rev. Lett. 116, 253601 (2016).
[3] J. Yin, Y. Cao, Y. H. Li, S.-K. Liao, L. Zhang, J. G.
Ren, W. Q. Cai, W. Y. Liu, B. Li et al., Satellite-based
entanglement distribution over 1200 kilometers, Science
356, 1140 (2017).
[4] J. Yin, Y. Cao, Y. H. Li, J. G. Ren, S. K. Liao, L. Zhang,
W. Q. Cai, W. Y. Liu, B. Li et al., Satellite-to-Ground
Entanglement-Based Quantum Key Distribution, Phys.
Rev. Lett. 119, 200501 (2017).
[5] K. G¨unthner, I. Khan, D. Elser, B. Stiller, ¨O. Bayraktar,
C. R. M¨uller, K. Saucke. D. Tr¨ondle. F. Heine et al.
Quantum-limited measurements of optical signals from
a geostationary satellite, Optica 4, 611 (2017).
[6] S. K. Liao, J. Lin, J. G. Ren, W. Y. Liu, J. Qiang, J.
Yin, Y. Li, Q. Shen, L. Zhang, and X. F. Liang, Space-
to-Ground Quantum Key Distribution Using a Small-
Sized Payload on Tiangong-2 Space Lab, Chin. Phys.
Lett. 34, 090302 (2017).
[7] S. K. Liao, H. L. Yong, C. Liu, G. L. Shen tu, D. D. Li,
J. Lin, H. Dai, S. Q. Zhao, B. Li et al., Long-distance
free-space quantum key distribution in daylight towards
inter-satellite communication, Nature Photonics 11, 509
(2017).
[8] H. Takenaka, A. Carrasco-Casado, M. Fujiwara, M.
Kitamura, M. Sasaki, and M. Toyoshima, Satellite-to-
ground quantum-limited communication using a 50-kg-
class microsatellite, Nature Photonics 11, 502 (2017).
[9] S.-K. Liao, W. Q. Cai, J. Handsteiner, B. Liu, J. Yin, L.
Zhang, D. Rauch, M. Fink, J. G. Ren, et al., Satellite-
relayed intercontinental quantum network, Phys. Rev.
Lett. 120, 030501 (2018).
[10] R. Bedington, J. M. Arrazola, and A. Ling, Progress in
satellite quantum key distribution, npj Quantum Infor-
mation 3:30, 1 (2017).
[11] L. Calderaro, C. Agnesti, D. Dequal, F. Vedovato, M.
Schiavon, A. Santamanto, V. Luceri, G. Bianco, G. Val-
lone, and P. Villoresi, Towards quantum communication
from global navigation satellite system, Quantum Sci.
Technol. 4, 015012 (2018).
[12] C. H. Benett and G. Brassard, Experimental quantum
cryptography: the dawn of a new era for quantum cryp-
tography: the experimental prototype is working, ACM
SIGACT News, 20, 78 (1989).
[13] P. W. Shor, Algorithms for quantum computation: dis-
crete logarithms and factoring, in Proceedings of the
35th Annual Symposium on Foundations of Computer
Science (IEEE Computer Society Press, Los Alamitos
1994), p. 124.
[14] C. H. Bennett and G. Brasard, Quantum cryptography:
public key distribution and coin tossing, in Proc. of the
IEEE International Conf. on Computers, Systems and
Signal Processing (IEEE Press, New York 1984), p. 175.
[15] V. Scarani, H. Bechmann-Pasquinucci, N. Cerf, J.
Duˇsek, N. L¨utkenhaus, and M. Peev, The security of
practical quantum key distribution, Rev. Mod. Phys.
81, 1301 (2009).
[16] W. K. Wooters and W. H. Zurek, A single quantum
cannot be cloned, Nature (London) 299, 802 (1982).
[17] A. K. Ekert, Quantum cryptography based on Bell’s
theorem, Phys. Rev. Lett. 67, 661 (1991).
[18] M.
Hillery,
Quantum
cryptography
with
squeezed
states, Phys. Rev. A. 61, 022309 (2000).
[19] N. J. Cerf, M. Levy and G. Van Assche, Quantum dis-
tribution of Gaussian keys using squeezed states, Phys.
Rev. A 63, 052311 (2001).
[20] D. Gottesman and J. Preskill, Secure quantum key
distribution using squeezed states, Phys. Rev. A 63,
022309 (2001).
[21] F. Grosshans and P. Grangier, Continuous Variable
Quantum Cryptography Using Coherent States, Phys.
Rev. Lett. 88, 057902 (2002).
[22] F. Grosshans, G. V. Assche, R. M. Wenger, R. Brouri,
N. J. Cerf, and P. Grangier, Quantum key distribution
using gaussian-modulated coherent states, Nature 421,
238 (2003).
[23] L.S. Madsen, V.C. Usenko, M. Lassen, R. Filip, and
U.L. Andersen, Continuous variable quantum key distri-
bution with two-mode squeezed states, Nat. Commun.
3, 1083 (2012).
[24] S. L. Braunstein and P. van Loock, Quantum informa-
tion with continuous variables, Rev. Mod. Phys. 77, 513
(2005).
[25] C.
Bonato,
M.
Aspelmeyer,
T.
Jennewein,
C.
Pernechele, P. Villoresi, A. Zeilinger, Inﬂuence of satel-
lite motion on polarization qubits in a Space-Earth
quantum communication link, Opt. Express 14, 10050
(2006).
[26] M. Zhang, L. Zhang, J. Wu, S. Yang, X. Wan, Z. He, J.
Jia, D. S. Citrin, and J. Wang, Detection and compen-
sation of basis deviation in satellite-to-ground quantum
communications, Opt. Express 22, 9871 (2014).
[27] T. Pramanik, B. K. Park, Y.-W. Cho, S.-W. Han, Y.-
S. Kim, and S. Moon, Robustness of reference-frame-
independent quantum key distribution against the rela-
tive motion of the reference frames, Phys. Lett. A 381,
2497 (2017).
[28] D. E. Bruschi, T. C. Ralph, I. Fuentes, T. Jennewein,
and M. Razavi, Spacetime eﬀects on satellite-based
quantum communications, Phys. Rev. D 90, 045041
(2014).
[29] J. Kohlrus, D. E. Bruschi, and I. Fuentes, Quantum
metrology of spacetime parameters of the Earth beating
classical precision, Phys. Rev. A 99, 032350 (2019).
[30] C. Robert, J.-M. Conan, and P. Wolf, Impact of turbu-
lence on high-precision ground-satellite frequency trans-
fer with two-way coherent optical links, Phys. Rev. A
93, 033860 (2016).
[31] J. Wang, Z. Tian, J. Jing, and H. Fan, Inﬂuence of rela-
tivistic eﬀects on satellite-based clock synchronization,
Phys. Rev. D 93, 065008 (2016).
[32] S. Nauerth, F. Moll, M. Rau, C. Fuchs, J. Horwath,
S. Frick, and H. Weinfurther, Air-to-ground quantum
communication, Nat. Phot. 7, 382 (2013).
[33] J. Y. Wang, B. Yang, S. K. Liao, L. Zhang, Q. Shen,
X. F. Hu, J. C. Wu, S. J. Yang, H. Jiang et al., Di-


## Page 28


28
rect and full-scale experimental veriﬁcations towards
ground-satellite quantum key distribution, Nature 7,
387 (2013).
[34] C. J. Pugh, S. Kaiser, J.-P. Bourgoin, J. Jin, N. Sultana,
S. Agne, E. Anisimova, V. Makarov, E. Choi, and B.
L. Higgins, Airborne demonstration of a quantum key
distribution receiver payload, Quantum Sci. Technol. 2,
024009 (2017).
[35] M. Er-long, H. Zheng-fu, G. Shun-sheng, Z. Tao, D. Da-
sheng, and G. Guang-can, Background noise of satellite-
to-ground- quantum key distribution, New J. Phys. 7,
215 (2005).
[36] C. Bonato, A. Tomaello, V. Da Deppo, G. Naletto, and
P. Villoresi, Feasibility of satellite quantum key distri-
bution, New J. Phys. 11, 04017 (2009).
[37] A. Tomaello, C. Bonato, V. Da Deppo, G. Naletto, and
P. Villoresi, Link budget and background noise for satel-
lite quantum key distribution, Advances in Space Re-
search 47, 802 (2011).
[38] D. Bacco, M. Canale, N. Laurenti, G. Vallone, and P.
Villoresi, Experimental quantum key distribution with
ﬁnite-key security analysis for noisy channels, Nature
Communications 4, 2363 (2013).
[39] A. Carrasco-Casado, H. Takenaka, D. Kolev, Y. Mune-
masa, H. Kunimori, K. Suzuki, T. Fuse, T. Kobo-
Oka, M. Akioka et al., LEO-to-ground optical commu-
nications using SOTA (Small Optical TrAnsponder) -
Payload veriﬁcation results and experiments on space
quantum communications, Acta Astronautica 139, 377
(2017).
[40] V. I. Tatarski,
Wave Propagation in a Turbulent
Medium, (Dover Publ., Mineola, 2016).
[41] L. C. Andrews and R. L. Phillips, Laser Beam Prop-
agation Through Random Media, (SPIE, Bellingham,
2001).
[42] J.-P. Bourgoin, E. Meyer-Scott, B. L. Higgins, B. Helou,
C. Erven, H. H¨ubel, B. Kumar, D. Hudson, I. D’Souza,
and R. Girard , A comprehensive design and perfor-
mance analysis of low Earth orbit satellite quantum
communication, New J. Phys. 15, 023006 (2013).
[43] W. H. Lehn and S. van der Werf, Atmospheric refrac-
tion: a history, Appl. Opt. 44, 5624 (2005).
[44] A. T. Young, Understanding Astronomical Refraction,
The Observatory 126, 82 (2006).
[45] L. C. Andrews, R. L. Phillips, C. Y. Hopen, Scintillation
model for a satellite communication link at large zenith
angles, Opt. Eng. 39, 3272 (2000).
[46] D. Dravins, L. Lindegren, E. Mezey, and A. T. Young,
Atmospheric Intensity Scintillation of Stars. I. Statisti-
cal Distributions and Temporal Properties, PASP 109,
173 (1997).
[47] T. Chiba, Spot Dancing of the Laser Beam Propagated
Through the Turbulent Atmosphere, Apl. Opt. 10, 2456
(1971).
[48] A. I. Mahan, Astronomical Refraction - Some History
and Theories, Appl. Opt. 1, 497 (1962).
[49] A. D. Wittmann, Astronomical refraction: formulas for
all zenith distances, Astron. Nachr. 318, 305 (1997).
[50] Dagang Jiang, Peng Zhang, Ke Deng, Zhoushi Yao,
Bin Zhu, and Kaiyu Qin, The atmospheric refraction
and beam wander inﬂuence on the acquisition of LEO-
Ground optical communication link, Optik 125, 3986
(2014).
[51] R. D. Sampson, E. P. Lozowski, A. E. Peterson, and D.
P. Hube, Variability in the Astroinomical Refraction of
the Rising and Setting Sun, PASP 115, 1256 (2003).
[52] U.S. Standard Atmosphere, 1976, National Oceanic and
Atmospheric Administration - S/T 76-1562 (1976).
[53] B. Edl´en, The Refractive Index of Air, Metrologia 2, 71
(1966).
[54] K. P. Birch and M. J. Downs, Corrections to the Up-
dated Edl´en Equation for the Refractive Index of Air,
Metrologia 31, 315 (1994).
[55] D. Gaiﬁllia, V. Pagounis, M. Tsakiri, and V. Zacharis,
Empirical Modelling of Refraction Factor in Trigono-
metric Heighting Using Meteoroligal Parameters, Jour-
nal of Geosciences and Geomatics. 4, 8 (2016).
[56] C. Hirt, S. Guillaume, A. Wisbar, B. B¨urki, and H.
Sternberg, Monitoring of the refraction coeﬃcient in the
lower atmosphere using a controlled setup of simultane-
ous reciprocal vertical angle measurements, J. Geophys.
Res. 115, D21102 (2010).
[57] L. Elterman, UV, visible, and IR attenuation for alti-
tudes to 50 km, Air Force Cambridge Research Labora-
tories Report No. AFCRL68-0153, Environmental Re-
search Paper No. 285, 1968 (unpublished)
[58] S. Q. Duntley, The Reduction of Apparent Contrast by
the Atmosphere, J. Opt. Soc. Am. 38, 179 (1948).
[59] G. I. Taylor, The spectrum of turbulence, Proc. R. Soc.
Lond. A 164, 476 (1938).
[60] O. O. Chumak and R. A. Baskov, Strong enhancing ef-
fect of correlations of photon trajectories on laser beam
scintillations, Phys. Rev. A 93, 033821 (2016).
[61] A. S. Gurvich, A. I. Kon, V. I. Mironov, and S. S.
Khmelevtsov, Laser Radiation in a Turbulent Atmo-
sphere [in Russian], (Nauka, Moscow, 1976).
[62] H. E. Butler, Observations of stellar scintillations, Proc.
R.I.A. Section A 54, 321 (1952).
[63] M. A. Ellison and H. Seddon, Some experiments on
the scintillation of stars and planets, MNRAS 112, 73
(1952).
[64] B. H. Briggs and I. A. Parkin, On the variation of ra-
dio star and satellite scintillations with zenith angle, J.
Atm. Terr. Phys. 25, 339 (1963).
[65] B. Stecklum, Measurements of stellar scintillation us-
ing photon counting statistics, Astron. Nachr. 306, 145
(1985).
[66] J. J. Burke, Observations of the Wavelength Depen-
dence of Stellar Scintillation, J. Opt. Soc. Am. 60, 1262
(1970).
[67] N. I. Kucherov, ed. Optical Instability of the Earth’s
Atmosphere, (Israel Program for Scientiﬁc Translations,
Jerusalem, 1966).
[68] F. J. Fuentes, J. J. Fuensalida, and C. Sanchez-Margo,
Measurements of the near-infrared stellar scintillation
above the Observatorio del Teide (Tenerife), Mon. Not.
astr. Soc. 226, 769 (1987).
[69] F. Moll, Experimental analysis of channel coherence
time and fading behavior in the LEO-ground link, Inter-
national Conference on Space Optical Systems and Ap-
plications. ICSOS 2014, 07.-09. May 2014, Kobe, Japan.
[70] F. Moll, Experimental characterization of intensity scin-
tillation in the LEO downlink, 4th International Work-
shop on Optical Wireless Communications (IWOW), Is-
tanbul, pp. 31-35 (2015).
[71] A. T. Young, Photometric Error Analysis. VIII. the
Temporal Power Spectrum of Scintillation, Appl. Opt.
8, 869 (1969).


## Page 29


29
[72] A. T. Young, Aperture Filtering and Saturation of Scin-
tillation, J. Opt. Soc. Am. 60, 248 (1970).
[73] A. T. Young, Saturation of Scintillation, J. Opt. Soc.
Am. 60, 1495 (1970).
[74] M. J. Beran and A. M. Whitman, Scintillation index
calculations using an altitude-dependent structure con-
stant, Appl. Opt. 27, 2178 (1988).
[75] L. C. Andrews, R. L. Phillips, and C. Y. Hopen, Scintil-
lation model for a satellite communication link at large
zenith angles, Opt. Eng. 39, 3272 (2000).
[76] V. A. Banakh and V. L. Mironov, Phase approximation
of the Huygens-Kirchhoﬀmethod in problems of laser-
beam propagation in the turbulent atmosphere, Opt.
Lett. 1, 172 (1977).
[77] V. A. Banakh and V. L. Mironov, Phase approximation
of the Huygens-Kirchhoﬀmethod in problems of space-
limited optical-beam propagation in the turbulent at-
mosphere, Opt. Lett. 4, 259 (1979).
[78] J. F. Holmes, M. H. Lee, and J. R. Kerr, Eﬀect of the
log-amplitude covariance function on the statistics of
speckle propagating through the turbulent atmosphere,
J. Opt. Soc. Am. 70, 355 (1980).
[79] V. I. Klyatskin and V. Tatarskii, Statistical Theory of
Light Propagation in a Turbulent Medium (Review),
Radiophysics and Quantum Electronics 15, 1095 (1974).
[80] A. V. Artem’ev and A. S. Gurvich, Experimental study
of coherence-function spectra, Radiophysics and Quan-
tum Electronics 14, 580 (1971).
[81] R. L. Fante, Electromagnetic Beam Propagation in Tur-
bulent Media, Proc. IEEE 63, 1669 (1975).
[82] H. T. Yura, Short-term average optical-beam spread in
a turbulent medium, J. Opt. Soc. Am. 63, 567 (1973).
[83] D. Vasylyev, A. Semenov, W. Vogel, K. G¨unthner, A.
Thurn, ¨O. Bayraktar, and Ch. Marquardt, Free-space
quantum links under diverse weather conditions, Phys.
Rev. A 96, 043856 (2017).
[84] F. Moll, D. Kolev, M. Abrahamsonc, C. Schmidt, R.
M. Calvo, and C. Fuchs, LEO-ground scintillation mea-
surements with the Optical Ground Station Oberpfaf-
fenhofen and SOTA/OPALS space terminals, Proc. of
SPIE 9991, 999102-1 (2016).
[85] C. E. Coulman, J. Vernin, Y. Coqueugniot, and J. L.
Caccia, Outer scale of turbulence appropriate to mod-
eling refractive-index structure proﬁles , Appl. Opt. 27,
155 (1988).
[86] V. L. Mironov and V. V. Nosov, On the theory of spa-
tially limited light beam displacements in a randomly
inhomogeneous medium, J. Opt. Soc. Am. 67, 1073
(1977).
[87] R. J. Glauber, Photon correlations, Phys. Rev. Lett. 10,
84 (1963).
[88] E. C. G. Sudarshan, Equivalence of Semiclassical and
Quantum Mechanical Descriptions of Statistical Light
Beams, Phys. Rev. Lett. 10, 277 (1963).
[89] A. A. Semenov and W. Vogel, Quantum light in the tur-
bulent atmosphere, Phys. Rev. A 80, 021802(R) (2009).
[90] D. Vasylyev, A. Semenov, and W. Vogel, Toward Global
Quantum Communication: Beam Wandering Preserves
Nonclassicality, Phys. Rev. Lett. 108, 220501 (2012).
[91] D. Vasylyev, A. Semenov, and W. Vogel, Atmospheric
Quantum Channels with Weak and Strong Turbulence,
Phys. Rev. Lett. 117, 090501 (2016).
[92] D. Vasylyev, W. Vogel, and A. Semenov, Theory of at-
mospheric quantum channels based on the law of total
probability, Phys. Rev. A 97, 063852 (2018).
[93] M. J. Schervish, Theory of Statistics, (Springer, New
York, 1995).
[94] D. Vasylyev, A. Semenov, and W. Vogel, Characteriza-
tion of free-space quantum channels, Proc. SPIE 10771,
107710V-1 (2018).
[95] S. Arnon, S. R. Rotman, and N. S. Kopeika, Perfor-
mance limitations of a free-space optical communica-
tion satellite network owing to vibrations: heterodyne
detection, Appl. Opt. 37, 6366 (1998).
[96] D. K. Oi, A. Ling, G. Vallone, P. Villoresi, S. Green-
land, E. Kerr, M. Macdonald, H. Weinfurter, H. Kuiper
et al., CubeSat quantum communications mission, EPJ
Quantum Technology.4:6, 1 (2017).
[97] F. Moll, S. Nauerth, C. Fuchs, J. Horwath, M. Rau,
and H. Weinfurter, Communication system technology
for demonstration of BB84 quantum key distribution
in optical aircraft downlinks, Proc. SPIE 8517, 851703
(2012).
[98] J.-P. Bourgoin, B. L. Higgins, N. Gigov, C. Holloway,
C. J. Pugh, S. Kaiser, M. Cranmer, and T. Jennewein,
Free-space quantum key distribution to a moving re-
ceiver, Opt. Express 23, 33437 (2015).
[99] S.-K. Liao, W. Q. Cai, W. Y. Liu, L. Zhang, Y. Li,
J. G. Ren, J. Yin, Q. Shen, Y. Cao et al., Satellite-
to-ground quantum key distribution, Nature (London)
549, 43 (2017).
[100] W.-Y. Hwang, Quantum Key Distribution with High
Loss:
Toward Global Secure Communication, Phys.
Rev. Lett. 91, 057901 (2003).
[101] H.-K. Lo, X. Ma, and K. Chen, Decoy State Quantum
Key Distribution, Phys. Rev. Lett. 94, 230504 (2005).
[102] X. Ma, B. Qi, Y. Zhao, and H.-K. Lo, Practical decoy
state for quantum key distribution, Phys. Rev. A 72,
012326 (2005).
[103] C. Pﬁster, N. L¨utkenhaus, S. Wehner, and P. J. Coles,
Sifting attacks in ﬁnite-size quantum key distribution,
New J. Phys. 18, 053001 (2016).
[104] K. Tamaki, M. Curty, and M. Lucamarini, Decoy-state
quantum key distribution with a leaky source, New J.
Phys. 18, 065008 (2016).
[105] P. Kok, W. J. Munro, K. Nemoto, T. C. Ralph, J. P.
Dowling, and G. J. Milburn, Linear optical quantum
computing with photonic qubits, Rev. Mod. Phys. 79,
135 (2007).
[106] M. T. Gruneisen, M. B. Flanagan, B. A. Sickmiller, J.
P. Black, K. E. Stoltenberg, and A. W. Duchance, Mod-
eling daytime sky access for a satellite quantum key dis-
tribution downlink, Opt. Express 23, 23924 (2015).
[107] J. E. Nordholt, R. J. Hughes, G. L. Morgan, C. G. Peter-
son, C. C. Wipf, Present and Future Free-Space Quan-
tum Key Distribution, Proc. SPIE 4635, 116 (2002).
[108] M. Curty, F. Xu, W. Cui, C. C. W. Lim, K. Tamaki, and
H.-K. Lo, Modeling daytime sky access for a satellite
quantum key distribution downlink, Nat. Commun. 5,
3732 (2014).
[109] C. C. W. Lim, M. Curty, N. Walenta, F. Xu, and H.
Zbinden, Concise security bounds for practical decoy-
state quantum key distribution, Phys. Rev. A 89,
022307 (2014).
[110] Z. Zhang, Q. Zhao, M. Razavi, and X. Ma, Improved-
key-rate bounds for practical decoy-state quantum-key-
distribution systems, Phys. Rev. A 95, 012333 (2017).


## Page 30


30
[111] J. H. Shapiro, Scintillation has minimal impact on far-
ﬁeld Bennett-Brassard 1984 protocol quantum key dis-
tribution, Phys. Rev. A 84, 032340 (2011).
[112] E. M. Dewan, R. E. Good, R. Beland, and J. Brown,
A model for C2
n (optical turbulence) proﬁles using ra-
diosonde data, Environmental Research Papers, N0.
1121, PL-TR-93-2043 (1993).
[113] T. W. VanZandt, J. L. Green, K. S. Gage, and W. L.
Clark, Vertical proﬁles of refractivity turbulence struc-
ture constant: Comparison of observations by the Sun-
set Radar with a new theoretical model, Radio Sci. 5,
819 (1978).
[114] A.
Jackson,
Modiﬁed-Dewan
optical
turbulence
parametrization, Phillips Laboratory Technical Report
AFRL-VS-TR-2004-1116 (2004).
[115] J. C. Wyngaard, Turbulence in the Atmosphere, (Cam-
bridge University Press, Cambridge, 2010).
[116] A. E. Hedin, E. L. Fleming, A. H. Manson, F. J.
Schmidlin, S. K. Avery, R. R. Clark, S. J. Franke, G.
J. Fraser, T. Tsuda et al, Empirical wind model for the
upper, middle and lower atmosphere, J. Atmos. Terr.
Phys. 58, 1421 (1996).
[117] Code
for
the
HWM93
model
is
available
at
https://github.com/scivision/hwm93
[118] D. L. Walters and K. E. Kunkel, Atmospheric modula-
tion transfer function for desert and mountain locations:
The atmospheric eﬀects on r0, J. Opt. Soc. Am. 71, 397
(1981).
[119] R. Hufnagel and N. R. Stanley, Modulation transfer
function associated with image transmission through
turbulent media, J. Opt. Soc. Am. 54, 52 (1964).
[120] R. Frehlich, R. Sharman, F. Vandenberghe, W. Yu, Y.
Liu, and J. Knievel, Estimates of C2
n from Numeri-
cal Weather Prediction Model Output and Comparison
with Thermosonde Data, J. Appl. Meteor. Climatol. 49,
1742 (2010).
[121] M. Charnotskii, Beam scintillations for ground-to-space
propagation. Part I: Path integrals and analytic tech-
niques, J. Opt. Soc. Am. A 27, 2169 (2010).
[122] R. L. Fante, Inner-scale size eﬀects on the scintillations
of light in the turbulent atmosphere, J. Opt. Soc. Am.
73, 277 (1983).
[123] L. C. Andrews, R. L. Phillips, C. Y. Hopen. and M. A.
Al-Habash, Theory of optical scintillation, J. Opt. Soc.
Am. A 16, 1417 (1999).
[124] C.-H. F. Fung, X. Ma, and H. F. Chau, Practical issues
in quantum-key-distribution postprocessing, Phys. Rev.
A 81, 012318 (2010).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
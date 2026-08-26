---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1912.02862v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1912.02862v2_On_the_Habitable_Lifetime_of_Terrestrial_Worlds_with_High_Radionuclide_Abundance

> Source: 1912.02862v2_On_the_Habitable_Lifetime_of_Terrestrial_Worlds_with_High_Radionuclide_Abundance.pdf

> Pages: 7

---


## Page 1


Draft version January 27, 2020
Typeset using LATEX twocolumn style in AASTeX63
On the Habitable Lifetime of Terrestrial Worlds with High Radionuclide Abundances
Manasvi Lingam1, 2 and Abraham Loeb2
1Department of Aerospace, Physics and Space Sciences, Florida Institute of Technology, Melbourne FL 32901, USA
2Institute for Theory and Computation, Harvard University, Cambridge MA 02138, USA
ABSTRACT
The presence of a liquid solvent is widely regarded as an essential prerequisite for habitability.
We investigate the conditions under which worlds outside the habitable zones of stars are capable
of supporting liquid solvents on their surface over geologically signiﬁcant timescales via combined
radiogenic and primordial heat. Our analysis suggests that super-Earths with radionuclide abundances
that are ≳103 times higher than Earth can host long-lived water oceans. In contrast, the requirements
for long-lived ethane oceans, which have been explored in the context of alternative biochemistries,
are less restrictive: relative radionuclide abundances of ≳102 could be suﬃcient. We ﬁnd that this
class of worlds might be detectable (10σ detection over ∼10 days integration time at 12.8 µm) in
principle by the James Webb Space Telescope at distances of ∼10 pc if their ages are ≲1 Gyr.
1. INTRODUCTION
Due to the rapid growth of exoplanetary science, there
has been renewed interest in determining the conditions
that render a planet habitable (Kasting 2012; Lingam &
Loeb 2019a). One of the most widely used criteria for
habitability is the existence of a suitable liquid solvent,
based on which the concept of the habitable zone (HZ)
was introduced. The HZ is deﬁned as the region around
the host star where liquid water can theoretically exist
on the planet’s surface (Dole 1964; Kasting et al. 1993;
Ramirez 2018; Ramirez et al. 2019). It is, however, cru-
cial to recognize that habitability is a broader concept
than the HZ, implying that worlds outside the HZ may
be habitable.
It is expected that worlds beyond the HZ outnum-
ber those in the HZ by orders of magnitude (Lingam &
Loeb 2019b). The most widely studied class of poten-
tially habitable worlds beyond the HZ, motivated by the
likes of Europa and Enceladus in our Solar system, is icy
worlds with subsurface oceans (Nimmo & Pappalardo
2016). Along similar lines, it has been proposed that car-
bonaceous asteroids and Kuiper belt objects could also
be abodes for life (Abramov & Mojzsis 2011). Looking
even farther aﬁeld, free-ﬂoating planets might also be
capable of hosting life, especially in subsurface environ-
ments (Stevenson 1999; Badescu 2011; Abbot & Switzer
2011; Lingam & Loeb 2019b). In many of these cases,
the heating necessary for sustaining liquid solvents is de-
rived from radioactivity, which is sensitive to the age of
the world under consideration.
Corresponding author: Manasvi Lingam
mlingam@ﬁt.edu
In this Letter, we investigate the role of primordial
and radiogenic heating in sustaining liquid solvents on
the surface as a function of the size, age and radionu-
clide abundances of the objects. Unlike most previous
studies, we will analyze the prospects for multiple sol-
vents because there are no deﬁnitive grounds for sup-
posing that water is the only solvent capable of hosting
life (Schulze-Makuch & Irwin 2018). We also study the
prospects for their detectability via JWST.
2. CONTRIBUTIONS TO SURFACE HEAT FLUX
The current heat ﬂow to Earth’s surface is generated
by radiogenic decay and primordial heat from Earth’s
formation (Melosh 2011). We can likewise estimate the
corresponding heat ﬂuxes for other worlds. Before doing
so, we note that the total radiogenic surface heat ﬂux
(QR) is estimated via
QR =
X
i
Qi0 exp

−t
τi

,
(1)
where t denotes the age of the world, whereas Qi0 and
τi represent the initial radioactive heat ﬂux (at t = 0)
and characteristic decay timescale of the ith element,
respectively. In our subsequent analysis, we will address
short- and long-lived radionuclides separately and focus
on the dominant isotopes.1
First, we consider the contribution from the decay
of long-lived radionuclides such as uranium-238 and
1 A third category (“medium-life” isotopes), comprising the likes
of plutonium-244 (τ ∼115 Myr) and lead-205 (τ ∼25 Myr),
may have to be included for certain stellar systems (Lugaro et al.
2018). For Solar system analogs, however, the conventional divi-
sion into short- and long-lived nuclides is suﬃcient.
arXiv:1912.02862v2  [astro-ph.EP]  24 Jan 2020


## Page 2


2
thorium-232. The radiogenic heating rate (in W) is usu-
ally modeled as being proportional to the mass M of the
world; this amounts to assuming that the heating rate
per unit mass (units of W/kg) is constant. Using this
scaling in conjunction with the mass-radius relationship
R ∝M 0.27 (Zeng et al. 2016), the radiogenic heat ﬂux
associated with long-lived radionuclides (QL) is
QL ≈0.166 W m−2 ΓL
 M
M⊕
0.46
exp

−t
τL

,
(2)
where τL represents the characteristic timescale for the
decay of long-lived radionuclides and ΓL measures the
abundance of radionuclides per unit mass relative to
the Earth. In obtaining this formula, we used the fact
that radionuclide concentration exhibits exponential de-
cay along with the scaling QL ∝M/R2. Although the
magnitude of τL depends on the speciﬁc composition of
the world under consideration, we will adopt τL ≈3.61
Gyr for Earth-like worlds (see Section 6.24 of Turcotte
& Schubert 2002). The normalization has been chosen
such that we obtain a heat ﬂux of 47 mW m−2 for mod-
ern Earth (The KamLAND Collaboration 2011).
The next major contribution is the primordial heat re-
leased as the world cools after its formation. The surface
heat ﬂux arising from this activity (QP ) is estimated
from Eq. (7.200) of Turcotte & Schubert (2002):
QP = −R¯ρ ¯C
3
dTm
dt ,
(3)
where ¯C is the mean speciﬁc heat, ¯ρ denotes the mean
mass density and dTm/dt signiﬁes the average rate of
mantle cooling.
By using the scaling R ∝M 0.27, we
ﬁnd that ¯ρ ∝M/R3 ∝M 0.19. Estimating the temporal
dependence of dTm/dt is complicated because it depends
on several mantle properties, but we will suppose that
it can be heuristically modeled using Eq.
(7.211) of
Turcotte & Schubert (2002):
dTm
dt
= −CT 2
m,
(4)
where C is a composite variable that depends solely on
the radionuclide composition and rheology of the man-
tle; however, it does not depend on the mantle thickness,
its ﬁducial viscosity and current rate of heat generation.
As our analysis deals with rocky worlds akin to Earth,
we will hold C ∼C⊕, where C⊕≈1.2 × 10−14 K−1 yr−1
is the value for Earth (Turcotte & Schubert 2002). After
solving the above diﬀerential equation and substituting
the expression into (3), we arrive at
QP ≈0.04 W m−2
 M
M⊕
0.46 
1 + 0.1
t −t⊕
τL
−2
,
(5)
where t⊕≈4.54 Gyr is the Earth’s current age; the
normalization factor preserves consistency with present-
day Earth (The KamLAND Collaboration 2011).
Although QL and QP represent the dominant long-
term contributions to the surface heat ﬂow, it is im-
portant to recognize that short-lived radionuclides can
contribute to brief, but intense, initial heating (Hevey
& Sanders 2006; Abramov & Mojzsis 2011). Although a
number of short-lived radionuclides exist, the most no-
table among them are iron-60 and aluminium-26, but
we shall concentrate on the latter due to its relatively
higher abundance in planetesimals of the early Solar sys-
tem (Lichtenberg et al. 2016). The heat ﬂux associated
with this short-lived radionuclide (QS) is obtained by
following the derivation that led to (2), thereby yielding
QS ≈89.5 W m−2 ΓS
 M
M⊕
0.46
exp

−t
τS

,
(6)
where τS ≈1.02 Myr, ΓS measures the abundance of
aluminium-26 relative to early Solar system planetesi-
mals, and the normalization constant follows upon uti-
lizing the heat generation per unit mass (Abramov &
Mojzsis 2011); this derivation assumed that the world is
primarily composed of rocky material.
The total heat ﬂux (Q) is given by the sum of the
various contributions, i.e., we have
Q = QL + QP + QS.
(7)
We are now in a position to estimate the eﬀective tem-
perature (Teﬀ) using the StefanBoltzmann law:
Q = σT 4
eﬀ.
(8)
At this stage, it is important to recognize that Teﬀis
not only dependent on the age of the world but also on
its mass as well as ΓL and ΓS. In order to simplify the
problem, we will presume that the relative abundances
of short- and long-lived radionuclides are equal to each
other, i.e., we specify ΓL = ΓS = Γ.
3. SURFACE TEMPERATURE AND
HABITABILITY DURATION
Our goal is to determine the duration of surface hab-
itability, i.e., the length of time over which a liquid sol-
vent can exist on the surface. There are two points that
need to be underscored at this juncture. First, we do
not address the prospects for subsurface habitability in
this work. The primary reason is that subsurface bio-
spheres are virtually impossible to detect at interstellar
distances, even if they emit plumes (Lingam & Loeb
2019b). The temperature in the interior (Ti) can be cal-
culated by solving the heat transfer equation (see Eq.
(4.13) of Melosh 2011):
∂Ti
∂t = ∇· (κ∇Ti) + H
CP
,
(9)
where CP is the heat capacity at constant pressure, H
is the heating rate per unit mass, and κ is the thermal


## Page 3


3
Γ = 1
Γ = 100
Γ = 104
1
10
100
1000
104
0
100
200
300
400
Age of the world (Myr)
Surface temperature (K)
Figure 1.
Surface temperature (K) as a function of the
age (in Myr) for an object with M ≈M⊕. The black curves
correspond to diﬀerent choices of radionuclide concentrations
relative to Earth.
The horizontal blue, green and brown
lines delineate the regions where water, ammonia and ethane
oceans can exist, respectively.
diﬀusivity; the time-dependent boundary condition for
this PDE is set by Ti(r = R) = Ts, where Ts is the sur-
face temperature. We will not solve this PDE because
it pertains to subsurface habitable conditions.
The second issue concerns the atmosphere, which per-
mits the solvent to exist in liquid form on the surface.
Massive and optically thick atmospheres have the ca-
pacity to mitigate cooling and thereby retain potentially
habitable surface conditions for long timescales (Steven-
son 1999; Badescu 2011). We shall, instead, adopt the
conservative choice of tenuous and optically thin atmo-
spheres for several reasons. For starters, the habitability
timescale herein constitutes a lower bound as explained
above. In addition, biosignatures in thick atmospheres
dominated by hydrogen and other reducing gases have
not been widely modeled. Lastly, the retention of mas-
sive atmospheres over long timescales might prove to
be diﬃcult for some rocky worlds (Dong et al. 2017;
Lingam & Loeb 2019a). For suﬃciently tenuous atmo-
spheres, the surface temperature (Ts) is approximated
by Teﬀhereafter. Our results for the habitability life-
time are not very sensitive to the optical depth if it is
much smaller than unity.
To complete our analysis, it is necessary to choose ap-
propriate solvents. A number of compounds apart from
water have been identiﬁed as viable candidates for bio-
chemical reactions to occur. We choose ammonia, an in-
organic polar solvent, because it has been the subject of
several experimental studies (Schulze-Makuch & Irwin
2018). We adopt ethane, an organic polar solvent, on
M = 0.1M⊕
M = M⊕
M = 10M⊕
1
10
100
1000
104
0
100
200
300
400
Age of the world (Myr)
Surface temperature (K)
Figure 2. Surface temperature (K) as a function of the age
(in Myr) for a world with radionuclide abundances ∼103
times higher than Earth.
The black curves correspond to
diﬀerent choices of the object’s mass. The horizontal blue,
green and brown lines delineate the regions where water,
ammonia and ethane oceans can exist, respectively.
account of its presumed commonality and its potential
to harbor alternative biochemistries (Ballesteros et al.
2019). For a surface pressure of ∼1 bar, water, ammo-
nia and ethane are liquids between ∼273 K to ∼373
K, ∼195.5 K to ∼240 K and ∼90 K to ∼184.5 K,
respectively. The surface temperature as a function of
time is determined from (8), and the above ranges are
employed to estimate the habitability timescale (tH).
Fig. 1 depicts the surface temperature for M ≈M⊕
and diﬀerent choices of Γ.
It is apparent that Γ has
a major impact on tH. For Γ = 1, we ﬁnd that nei-
ther water nor ammonia oceans are feasible, although
ethane oceans can persist for ∼10 Myr. In contrast, for
Γ = 100, short-lived water and ammonia oceans may
exist for ∼1 Myr, but ethane oceans are capable of sur-
viving for several Gyr. Lastly, when it comes to Γ = 104,
we observe that both water and ammonia oceans are fea-
sible over Gyr timescales.
Next, we examine the role of the object’s mass. From
(7) and (8), the ensuing scaling is Ts ∝M 0.115, thus
suggesting that both Ts and tH should have a weak de-
pendence on M. In actuality, tH exhibits a complex re-
lationship with M due to the co-dependence on Γ. This
becomes evident upon inspecting Fig. 2, where Γ = 103
while M is varied. For M ≈0.1M⊕, we observe that
water and ammonia oceans can exist for only ∼1 Myr.
In contrast, for M ≈10M⊕, these oceans could persist
over Gyr timescales.
4. DISCUSSION AND CONCLUSIONS


## Page 4


4
Γ = 1
Γ = 100
Γ = 104
1
10
100
1000
104
10-4
0.001
0.010
0.100
1
10
Age of the world (Myr)
Spectral flux density (μJy)
Figure 3. Spectral ﬂux density (in µJy) as a function of the
age (in Myr) for an object with M ≈M⊕at a distance of 10
pc. The black curves show diﬀerent choices of radionuclide
concentrations relative to Earth.
The horizontal red line
corresponds to the sensitivity of the MIRI-JWST for a 10σ
detection over ∼10 days at 12.8 µm.
Finally, we will brieﬂy discuss some implications for
biology and feasibility of detection.
4.1. Biological implications
We do not have a clear picture of when life originated
on Earth, under the implicit assumption that it was not
transported via panspermia. As per the latest phyloge-
netic and paleontological evidence, allied to theoretical
arguments, there are tentative grounds for supposing
that abiogenesis occurred ≲100 Myr after Earth’s for-
mation (Lazcano & Miller 1994; Dodd et al. 2017; Betts
et al. 2018). It is important, however, to recognize that
we have no knowledge of the timescale for abiogenesis
on other worlds (Spiegel & Turner 2012). In addition,
the process of terrestrial planet formation from the pro-
toplanetary disk may necessitate ≲10-100 Myr (Mor-
bidelli et al. 2012; Armitage 2018).
Based on the above arguments, it would seem de-
sirable for tH to exceed 100 Myr in order for life to
originate. If the pace of evolution is similar to that on
Earth, the manifestation of detectable biosignatures en-
gendered by microbes might require ∼1 Gyr. Thus, in
order for tH ∼0.1-1 Gyr to be realized, Figs. 1 and
2 suggest that Γ ≳103 and M ≳M⊕are necessary.
This immediately raises the question of whether such
high concentrations of long-lived radionuclides are at-
tainable, and by what pathways they can occur.
Before tackling this issue, a comment on potential mi-
crobial ecosystems is in order. Although radioactivity
levels will indubitably be high on these worlds, many
Earth-based extremophiles (e.g., Deinococcus radiodu-
rans) readily tolerate high doses. In fact, the chemoau-
totrophic bacterium Desulforudis audaxviator derives its
energy requirements indirectly from radioactivity (Chi-
vian et al. 2008). The surface heat ﬂux is ∼300-1100
W/m2 when conditions suitable for liquid water exist.
Of this energy ﬂux, only a small fraction will be accessi-
ble to perform work due to thermodynamic constraints
(Lingam & Loeb 2019c). Nevertheless, even if merely
∼0.1% of the total ﬂux is utilized, it is still ∼4 or-
ders of magnitude higher than the basal requirement
of 1.48 × 10−5 W/m2 imposed by metabolism (Kempes
et al. 2017); it is also two orders of magnitude higher
than the energy ﬂux required by Chlorobiaceae in the
Black Sea (Manske et al. 2005).
Now, we examine the abundances of long-lived ra-
dionuclides.
Analysis of near-infrared signatures has
revealed that r-process elements (which include ura-
nium and thorium) are predominantly synthesized dur-
ing neutron star mergers (Kasen et al. 2017; Kajino et al.
2019).2 Thus, if the rate of neutron star mergers per
unit volume tracks the stellar density, it is conceivable
that worlds in the inner regions of the Galactic bulge
or in environments that are gas-poor (e.g., in elliptical
galaxies) could exhibit higher radionuclide concentra-
tions; furthermore, many metal-poor stars with enriched
r-process elements have been detected (Frebel 2018).
Spectroscopic surveys of solar twins and analogs have
shown that the solar abundance of thorium is a few
times lower (< 3) than other stars in the sample (Un-
terborn et al. 2015; Botelho et al. 2019). Overall, some
worlds will be characterized by elevated abundances of
long-lived radionuclides (Lugaro et al. 2018). Turning
our attention to short-lived radionuclides, speciﬁcally
aluminium-26, they are unlikely to aﬀect habitability
over Gyr timescales, irrespective of their initial inven-
tory. However, a number of crucial short-term factors
depend on its abundance such as diﬀerentiation and de-
hydration of planetesimals (Gilmour & Middleton 2009;
Lichtenberg et al. 2019), and melting ice to initiate ser-
pentinization (G´obi & Kereszturi 2017). A number of
metrics indicate that high levels of aluminium-26 are
widespread in extrasolar systems, especially in young
stars (Lugaro et al. 2018).
The situation is rendered quite diﬀerent when we con-
sider oceans of liquid ethane.
For super-Earths with
relatively modest enhancements of Γ ≳10, we ﬁnd
that tH ∼0.1-1 Gyr is realizable.
Due to the rela-
tively weaker constraints on Γ, the existence of long-
lived ethane oceans is more plausible with respect to wa-
ter oceans; for diﬀerent reasons, Ballesteros et al. (2019)
concluded that ethane seas may be the most common in
the Universe. Thus, there exist compelling grounds to
2 https://blog.sdss.org/wp-content/uploads/2017/01/
periodic table.png


## Page 5


5
M = 0.1M⊕
M = M⊕
M = 10M⊕
1
10
100
1000
104
10-4
0.001
0.010
0.100
1
10
Age of the world (Myr)
Spectral flux density (μJy)
Figure 4. Spectral ﬂux density (in µJy) as a function of the
age (in Myr) for a world at a distance of 10 pc with radionu-
clide abundances ∼103 times higher than Earth. The black
curves embody diﬀerent choices of the object’s mass. The
horizontal red line corresponds to the sensitivity of MIRI-
JWST for a 10σ detection over ∼10 days at 12.8 µm.
investigate potential biochemistries in liquid ethane as
well as the resultant biosignatures.
If habitable conditions persist for ≳100 Myr, another
factor must be taken into consideration for free-ﬂoating
worlds. Due to the relative motion of stars as well as
their ejection from the parent stellar system, they ought
to have typical velocities of ∼20 km/s with respect to
nearby stars. Thus, over a period of ∼100 Myr, they
can traverse distances of ≳1 kpc. During the course
of this journey, they may be captured by three-body
gravitational interactions into binary systems (Ginsburg
et al. 2018). Once they have been captured, this opens
the possibility of seeding other worlds in that system via
interplanetary panspermia.3
4.2. Detectability of objects
In order to detect worlds that are rendered habitable
by radiogenic and primordial heating, the spectral ﬂux
density (S) received at Earth via black body emission
must be suﬃciently high (see Abbot & Switzer 2011).4
S is determined by scaling the black body spectral ra-
3 Note that the prospects for interplanetary panspermia are en-
hanced for clustered planetary systems such as those around M-
dwarfs (Lingam & Loeb 2017).
4 In some respects, our analysis is similar to the detection of free-
ﬂoating Y-type brown dwarfs (Burrows et al. 2003; Biller 2017),
because they have black body temperatures as low as ∼250 K.
diance of the object as follows:
S = Bλ
4
R
d
2
= hν3R2
2c2d2

exp

hν
kBTeﬀ

−1
−1
,
(10)
where Bλ is the Planck function, ν is the frequency and
d is the distance of the object from Earth. We adopt
a wavelength of 12.8 µm, for which the sensitivity of
the imager corresponding to the Mid-Infrared Instru-
ment (MIRI) instrument on board JWST is 0.84 µJy to
achieve 10σ detection over 104 s of integration time (see
Table 2 of Rieke et al. 2015).5 Hence, over an integration
time of ∼106 s (viz., ∼10 days), the detection thresh-
old would be lowered to 84 nJy. At this wavelength, the
above expression can be rewritten to yield
S ≈2.03 µJy
 M
M⊕
0.54 
d
10 pc
−2
×

exp
1124.82 K
Teﬀ

−1
−1
.
(11)
Due to the exponential dependence of S on Teﬀ, S will
naturally be very sensitive to the age, radionuclide abun-
dance and mass of the object.
Figs.
3 and 4 depict S for the ﬁducial choices of
λ = 12.8 µm and d = 10 pc. For relatively high radionu-
clide abundances (Γ ≳103) and high masses (M ≳M⊕),
we ﬁnd that the MIRI instrument may detect such
worlds provided they are ≲1 Gyr old. In contrast, ob-
jects with lower values of Γ and M are unlikely to be de-
tectable by MIRI unless they are located relatively close
to Earth. Based on available estimates for the density of
free-ﬂoating planets, Lingam & Loeb (2019b) suggested
that the distance to the nearest roughly Mars-sized free-
ﬂoating object might be on the order of 0.1 pc. In this
case, objects with Γ ∼100 are potentially detectable by
MIRI during the ﬁrst ∼10 Myr of their existence, while
Γ ≳103 could boost detectability to Gyr timescales.
Hence, in principle, planets with suﬃciently high
abundances that are relatively nearby might remain de-
tectable over long timescales. A number of young stel-
lar comoving groups have been detected at distances of
∼10-100 pc from Earth with stellar ages of ∼10-50 Myr
(Zuckerman & Song 2004). Examples of such groups in-
clude the β Pictoris moving group (Mamajek & Bell
2014) and the TW Hydrae association (Ducourant et al.
2014; Gagn´e et al. 2017), whose median ages are ∼20
Myr and ∼10 Myr, respectively. If worlds far removed
from the HZs of such stars are characterized by M ≳M⊕
and suﬃciently high radionuclide abundances, they may
fulﬁll the requirements for detectability by JWST based
on Figs. 3 and 4.
In the event that JWST detects either a free-ﬂoating
object or one that is far beyond the HZ with an anoma-
5 https://www.jwst.nasa.gov/


## Page 6


6
lously high temperature (and thin atmosphere), one can
use Ts to place constraints on its age and radionuclide
abundance.
For such worlds, thermal emission spec-
troscopy could be utilized to discern potential atmo-
spheric biosignatures (Fujii et al. 2018).
ACKNOWLEDGMENTS
We thank the reviewer for the constructive report.
This work was supported in part by the Breakthrough
Prize Foundation, Harvard University’s Faculty of Arts
and Sciences, and the Institute for Theory and Compu-
tation (ITC) at Harvard University.
REFERENCES
Abbot, D. S., & Switzer, E. R. 2011, Astrophys. J. Lett.,
735, L27, doi: 10.1088/2041-8205/735/2/L27
Abramov, O., & Mojzsis, S. J. 2011, Icarus, 213, 273,
doi: 10.1016/j.icarus.2011.03.003
Armitage, P. J. 2018, A Brief Overview of Planet
Formation, ed. H. J. Deeg & J. A. Belmonte (Springer),
2185–2203, doi: 10.1007/978-3-319-55333-7 135
Badescu, V. 2011, Icarus, 216, 485,
doi: 10.1016/j.icarus.2011.09.013
Ballesteros, F. J., Fernandez-Soto, A., & Mart´ınez, V. J.
2019, Astrobiology, 19, 642, doi: 10.1089/ast.2017.1720
Betts, H. C., Puttick, M. N., Clark, J. W., et al. 2018, Nat.
Ecol. Evol., 2, 1556, doi: 10.1038/s41559-018-0644-x
Biller, B. 2017, Astron. Rev., 13, 1,
doi: 10.1080/21672857.2017.1303105
Botelho, R. B., Milone, A. d. C., Mel´endez, J., et al. 2019,
Mon. Not. R. Astron. Soc., 482, 1690,
doi: 10.1093/mnras/sty2791
Burrows, A., Sudarsky, D., & Lunine, J. I. 2003, Astrophys.
J., 596, 587, doi: 10.1086/377709
Chivian, D., Brodie, E. L., Alm, E. J., et al. 2008, Science,
322, 275, doi: 10.1126/science.1155495
Dodd, M. S., Papineau, D., Grenne, T., et al. 2017, Nature,
543, 60, doi: 10.1038/nature21377
Dole, S. H. 1964, Habitable planets for man (Blaisdell
Pub. Co.)
Dong, C., Lingam, M., Ma, Y., & Cohen, O. 2017,
Astrophys. J. Lett., 837, L26,
doi: 10.3847/2041-8213/aa6438
Ducourant, C., Teixeira, R., Galli, P. A. B., et al. 2014,
Astron. Astrophys., 563, A121,
doi: 10.1051/0004-6361/201322075
Frebel, A. 2018, Annu. Rev. Nucl. Part. Sci., 68, 237,
doi: 10.1146/annurev-nucl-101917-021141
Fujii, Y., Angerhausen, D., Deitrick, R., et al. 2018,
Astrobiology, 18, 739, doi: 10.1089/ast.2017.1733
Gagn´e, J., Faherty, J. K., Mamajek, E. E., et al. 2017,
Astrophys. J. Suppl., 228, 18,
doi: 10.3847/1538-4365/228/2/18
Gilmour, J. D., & Middleton, C. A. 2009, Icarus, 201, 821,
doi: 10.1016/j.icarus.2009.03.013
Ginsburg, I., Lingam, M., & Loeb, A. 2018, Astrophys. J.
Lett., 868, L12, doi: 10.3847/2041-8213/aaef2d
G´obi, S., & Kereszturi, ´A. 2017, Mon. Not. R. Astron. Soc.,
466, 2099, doi: 10.1093/mnras/stw3223
Hevey, P. J., & Sanders, I. S. 2006, Meteorit. Planet. Sci.,
41, 95, doi: 10.1111/j.1945-5100.2006.tb00195.x
Kajino, T., Aoki, W., Balantekin, A. B., et al. 2019, Prog.
Part. Nucl. Phys., 107, 109,
doi: 10.1016/j.ppnp.2019.02.008
Kasen, D., Metzger, B., Barnes, J., Quataert, E., &
Ramirez-Ruiz, E. 2017, Nature, 551, 80,
doi: 10.1038/nature24453
Kasting, J. 2012, How to Find a Habitable Planet
(Princeton University Press)
Kasting, J. F., Whitmire, D. P., & Reynolds, R. T. 1993,
Icarus, 101, 108, doi: 10.1006/icar.1993.1010
Kempes, C. P., van Bodegom, P. M., Wolpert, D., et al.
2017, Front. Microbiol., 8, 31,
doi: 10.3389/fmicb.2017.00031
Lazcano, A., & Miller, S. L. 1994, J. Mol. Evol., 39, 546,
doi: 10.1007/BF00160399
Lichtenberg, T., Golabek, G. J., Burn, R., et al. 2019, Nat.
Astron., 3, 307, doi: 10.1038/s41550-018-0688-5
Lichtenberg, T., Golabek, G. J., Gerya, T. V., & Meyer,
M. R. 2016, Icarus, 274, 350,
doi: 10.1016/j.icarus.2016.03.004
Lingam, M., & Loeb, A. 2017, Proc. Natl. Acad. Sci., 114,
6689, doi: 10.1073/pnas.1703517114


## Page 7


7
—. 2019a, Rev. Mod. Phys., 91, 021002,
doi: 10.1103/RevModPhys.91.021002
—. 2019b, Int. J. Astrobiol., 18, 112,
doi: 10.1017/S1473550418000083
—. 2019c, Astrophys. J., 883, 143,
doi: 10.3847/1538-4357/ab3f35
Lugaro, M., Ott, U., & Kereszturi, ´A. 2018, Prog. Part.
Nucl. Phys., 102, 1, doi: 10.1016/j.ppnp.2018.05.002
Mamajek, E. E., & Bell, C. P. M. 2014, Mon. Not. R.
Astron. Soc., 445, 2169, doi: 10.1093/mnras/stu1894
Manske, A. K., Glaeser, J., Kuypers, M. M. M., &
Overmann, J. 2005, Appl. Environ. Microbiol., 71, 8049,
doi: 10.1128/AEM.71.12.8049-8060.2005
Melosh, H. J. 2011, Planetary Surface Processes
(Cambridge University Press)
Morbidelli, A., Lunine, J. I., O’Brien, D. P., Raymond,
S. N., & Walsh, K. J. 2012, Annu. Rev. Earth Planet.
Sci., 40, 251, doi: 10.1146/annurev-earth-042711-105319
Nimmo, F., & Pappalardo, R. T. 2016, J. Geophys. Res. E,
121, 1378, doi: 10.1002/2016JE005081
Ramirez, R., Abbot, D. S., Fujii, Y., et al. 2019, in Bulletin
of the American Astronomical Society, Vol. 51, 31
Ramirez, R. M. 2018, Geosciences, 8, 280,
doi: 10.3390/geosciences8080280
Rieke, G. H., Wright, G. S., B¨oker, T., et al. 2015, Publ.
Astron. Soc. Pac, 127, 584, doi: 10.1086/682252
Schulze-Makuch, D., & Irwin, L. N. 2018, Life in the
Universe: Expectations and Constraints, 3rd edn.
(Springer), doi: 10.1007/978-3-319-97658-7
Spiegel, D. S., & Turner, E. L. 2012, Proc. Natl. Acad. Sci.
USA, 109, 395, doi: 10.1073/pnas.1111694108
Stevenson, D. J. 1999, Nature, 400, 32, doi: 10.1038/21811
The KamLAND Collaboration. 2011, Nat. Geosci., 4, 647,
doi: 10.1038/ngeo1205
Turcotte, D. L., & Schubert, G. 2002, Geodynamics, 2nd
edn. (Cambridge University Press)
Unterborn, C. T., Johnson, J. A., & Panero, W. R. 2015,
Astrophys. J., 806, 139,
doi: 10.1088/0004-637X/806/1/139
Zeng, L., Sasselov, D. D., & Jacobsen, S. B. 2016,
Astrophys. J., 819, 127,
doi: 10.3847/0004-637X/819/2/127
Zuckerman, B., & Song, I. 2004, Annu. Rev. Astron.
Astrophys., 42, 685,
doi: 10.1146/annurev.astro.42.053102.134111

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1912_02862v2_on_the_habitable_lifetime_of_terrestrial_worlds_with_high_radionuclide_abundance
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1912_02862V2_ON_THE_HABITABLE_LIFETIME_OF_TERRESTRIAL_WORLDS_WITH_HIGH_RADIONUCLIDE_ABUNDANCE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

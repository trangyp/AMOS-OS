---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1704.05885v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1704.05885v1_Integrating_optimization_with_thermodynamics_and_plant_physiology_for_crop_ideot

> Source: 1704.05885v1_Integrating_optimization_with_thermodynamics_and_plant_physiology_for_crop_ideot.pdf

> Pages: 40

---


## Page 1


1 
 
Integrating optimization with thermodynamics and plant physiology for crop 
ideotype design 
Talukder Z. Jubery1, Baskar Ganapathysubramanian1, Matthew E. Gilbert2, and Daniel 
Attinger1 
1Department of Mechanical Engineering and Department of Electrical and Computer 
Engineering, Iowa State University, Ames, IA, 50011;  
2Department of Plant Sciences, University of California, Davis, CA 95616, USA. 
*Correspondence to: baskarg@iastate.edu, gilbert@ucdavis.edu, attinger@iastate.edu 
Abstract 
A computational framework integrating optimization algorithms, parallel computing and plant 
physiology was developed to explore crop ideotype design. The backbone of the framework is a 
plant physiology model that accurately tracks water use (i.e. a plant hydraulic model) coupled 
with mass transport (CO2 exchange and transport), energy conversion (leaf temperature due to 
radiation, convection and mass transfer) and photosynthetic biochemistry of an adult maize plant. 
For a given trait configuration, soil parameters and hourly weather data, the model computes 
water use and photosynthetic output over the life of an adult maize plant. We coupled this 
validated model with a parallel, meta-heuristic optimization algorithm, specifically a genetic 
algorithm (GA), to identify trait sets (ideotypes) that resulted in desired water use behavior of the 
adult maize plant. We detail features of the model as well as the implementation details of the 
coupling with the optimization framework and deployment on high performance computing 
platforms. We illustrate a representative result of this framework by identifying maize ideotypes 
with optimized photosynthetic yields using weather and soil conditions corresponding to Davis, 
CA. Finally, we show how the framework can be used to identify broad ideotype trends that can 
inform breeding efforts. The developed presented tool has the potential to inform the 
development of future climate-resilient crops.  
Keywords: ideotypes, optimization, net photosynthesis, hydraulic traits. 
Introduction 
To ensure food security, crop grain yields should be increased globally by 70–100% within the 
next 40 years [1]. To increase yields, plant breeders and plant scientists are working to develop 
improved and appropriate varieties of crops. However, the intrinsic uncertainty of climate 
change, limited water supply and reduction of agricultural land increase the challenges in the 
crop development process [2]. We have limited time and resources to select the most appropriate 
crop varieties, and crop modeling provides a rational approach to designing new crop varieties 
[3].  
Traditional methods for finding the best crop varieties, or ideotypes [4], rely on agronomic 
experiments. The evaluated ideotypes are restricted in time and space, making results site- and


## Page 2


2 
 
season-specific, and the experiments are time consuming and expensive. The use of crop models 
has greatly enabled crop breeding by reducing costs and accelerating the process of 
identifying/designing ideotypes.  
Many physiological models of crops [5]–[15] have been developed since the pioneering 1948 
model of van den Honert [16]. These models are focused on specific aspects of plant physiology: 
water transport, time-dependence, influence of environmental conditions, heat and mass 
transfer, effect of plant geometry, nutrient transport, plant growth, or phloem transport. While 
these models can determine and explain optimum relationships between existing traits [5], there 
is increasing interest in coupling them with optimization tools to identify the most promising 
traits for a desired response [24], [25]. Over the last three decades, publications on numerical 
optimization methods have emerged and their number has grown at a rate higher than the growth 
rate of publications on traditional plant breeding. Considering also that breeding is, per se, an 
optimization problem, the recent emergence of limited publications at the intersection of 
“breeding” and “numerical optimization” is not unexpected. Some of these publications describe 
numerical methods inspired by animal breeding strategies [17], [18], while others seek to 
optimize the management of a breeding program [19], [20] , either by improving the phenotyping 
associated with breeding [21], or minimizing the genotyping efforts [22]. While these models 
can determine and explain optimum relationships between existing traits [5], [10], [23], there is 
work yet to be done to efficiently leverage this knowledge to direct breeding efforts. This is the 
motivation of our work. We describe our model and how we integrate it with an optimization 
framework. We then demonstrate an application of the framework by identifying crop ideotypes 
for a specific location parameterized by weather and soil conditions. 
Materials and Methods 
 
Plant physiology model  
The backbone of our framework is a mechanistic crop physiological model that is based upon a 
detailed one-dimensional representation of plant hydraulic characteristics. Liquid-phase, plant-
water relations are simply represented as a static series of conductances resistances for stems, 
leaves and roots ( disregarding capacitive behavior, i.e. stems, leaves and roots do not store any 
water) , as described in the seminal work of van den Honert [16]. The model is a physiologically 
explicit representation of C4 maize water-use after canopy closure. The model explicitly 
accounts for energy balance (convection, radiation, latent heat), transpiration, intercellular CO2 
concentration (via both diffusion and biochemical processes), weather conditions (temperature, 
precipitation, pressure, radiation), and soil type. Seven plant hydraulic ‘traits’ are considered 
within the model, as shown in Fig. 1, and can be used to represent the response of leaf 
evapotranspiration to environmental variation. We next provide details of each submodel that is 
used to construct the full plant model. Figure 2 shows the various submodels schematically.


## Page 3


3 
 
 
Water transport submodel 
Uptake of water by the root from the soil reaches the top of the canopy due to cohesive-adhesion 
interactions, but the main driving force for this transport is the dryness of the atmosphere. Water 
travels from the soil to the leaf as a liquid. Subsequently, as a gas it evaporates from the leaf 
(through the stomatal pores) to the surrounding environment. The evaporation rate depends on 
the leaf temperature, external relative humidity, air temperature and boundary layer effects.  This 
is called environmental water demand. To fulfill this demand, the plant supplies liquid water to 
the leaf. This flow is driven by the potential difference of water between the soil and the leaf and 
is controlled by the hydraulic resistance of the plant.  
 
Using a one-dimensional representation of plant hydraulic characteristics, as shown in Fig. 1,  
the water supply, 
s
W
J
, , can be expressed as [26] 
 
 


leaf
soil
soil
plant
s
W
K
K
J











1
,
1
1
, 
(1) 
where Kplant is hydraulic conductance of the plant, Ksoil is hydraulic conductance of soil; ψleaf is 
the water potential at the leaf, ψsoil is water potential at the soil. Water potential is a combined 
effect of hydrostatic pressure, osmotic pressure, matric pressure, and gravitational pull.1  
The hydraulic conductance of the plant can be expressed as  
 
1
1
1
1










leaf
stem
root
plant
K
K
K
K
, 
(2) 
where Kroot is the hydraulic conductance of the root, Kstem is hydraulic conductance of the stem, 
and Kleaf is hydraulic conductance of the leaf.  
The hydraulic conductance of the soil, Ksoil, depends on the type of soil, the amount of water in 
the soil and the relative occupancy of the root in the soil. The effect of these parameters is 
captured via the following equation [27], 
 

















root
s
b
root
soil
soil
sat
sat
soil
r
L
LH
k
K





log
2
/
3
2
,
, 
(3) 
                                                          
1 . Osmotic pressure that depends on the presence of ions in the water is neglected in our model, 
as we considered the water as pure and free from any minerals.


## Page 4


4 
 
where  ksat, b, ψsat and ψsoil vary among the types of soil, and they represent saturated hydraulic 
conductivity, texture, water potential of saturated soil, and water potential of the soil, 
respectively. The rest of the terms are used to capture the effect of the presence of root on the 
soil conductance. The symbols L, Hs and rroot represent root length density of the absorbing root 
(length per soil volume), depth of the soil occupied by the root and radius of the root. 
The water potential of the soil, ψsoil, can be expressed as a function of soil water content using an 
empirical equation developed by Campbell et al. [28] as 
 
b
sat
sat
soil











, 
(4) 
where θsat is the saturated water content in the soil, and θ is current volumetric water content in 
the soil. In this model, soil water content would gradually deplete as plants fulfill the 
atmospheric water demand. The depletion of water due to evaporation of water from the soil was 
not considered here. There is no addition of water in the case of drought conditions. However, 
under irrigated conditions, based on the irrigation frequency, water is added to the soil until 
water content reaches θsat of the soil. e.g., for irrigation frequency 7, the soil is fully saturated 
every 7*24 hours.  
Soil water potential at the root (Eq. 3), ψsoil,root, can be evaluated from leaf water potential and 
water demand by the plants,  
 









soil
plant
d
W
leaf
root
soil
K
K
J
1
1
,
,


, 
(5) 
Water demand is driven by the gradient of water vapor concentration between the leaves and the 
surrounding environment and is controlled by the stomatal conductance and air boundary layer 
conductance. It can be expressed as [26] 
 
 
















a
va
vl
blc
st
d
W
P
P
P
g
g
J
1
,
1
1
, 
(6) 
where Pvl and Pva represent water vapor pressure in the leaf and atmosphere, respectively. Water 
vapor pressures are evaluated using Tetens formula [29] ,








2
1
0
,
c
T
T
c
i
i
v
i
i
e
c
RH
P
, where RH is the 
relative humidity, c0 = 0.617 kPa, c1 =17.38, and c2= 239°C. Generally, the leaf inter-cellular 
space is close to equilibrium with the cells having a relative humidity of greater than 99%, and 
thus for each of calculation of evaporation we consider the leaf to be fully saturated. gst and gblc  
are the stomatal conductance and boundary layer conductance to the water vapor transport, 
respectively.


## Page 5


5 
 
Boundary layer conductance to water vapor, gblc depends on the atmospheric wind speed and the 
morphology as well as the orientation of the leaf. Wind speed and leaf dimension are designated 
as  Uc, and d as in [28]. Conductance of water vapor through the air boundary layer on the leaf 
can be considered as forced convection and can be expressed via an empirical equation. Note 
that, here, contribution from the free convection is neglected, as the ratio of dimensionless 
parameters Re2/Gr which reflects the forced convection/free convection is usually much greater 
thanone. The empirical correlation among the dimensionless Reynolds number, Re, and Schmidt 
number, Sc, and the conductance can be calculated as,  
 
e
WV
blc
d
Sc
D
g
3
/1
2
/1
Re


, 
(7) 
where
a
e
cd
U


Re
; 
WV
a
D
Sc


; α=0.644*1.4 is an empirical parameter; and de =0.72d, with d 
being the width of the maize leaf and 0.72 being used to find the equivalent parabola of the leaf 
where wind is flowing in the width direction of the parabola. Uc , νa and Dwv  represent the wind 
speed on the top of the canopy, kinetic viscosity of air and water vapor diffusivity in air.  
Wind speed can increase approximately logarithmically with distance above a plant canopy, and 
is also influenced by the plants. The variation in wind speed can be described by 
 
c
c
c
c
nH
mH
H
U
U


ln
4.0
*
, 
(8) 
where 0.4 is related to the von Karman constant, Hc is the height of the plant, mHc is the zero-
plane displacement, and nHc is the roughness length. Generally, m is 0.7 and n is 0.1. U* is 
termed the shearing or friction velocity and can be calculated from the wind speed Um that is 
measured at height Hm from the ground as 
 
c
c
m
m
nH
mH
H
U
U


ln
4.0
*
. 
(9) 
Only around 3% of water that is absorbed from the soil is used by the plant for 
metabolism/growth, and less than 0.1% is used for photosynthesis. 
CO2 transport and net photosynthesis submodel 
 Along with water, the plant needs CO2, sunlight and enzymes for photosynthesis. From the 
environment, gaseous CO2 diffuses into the leaf via stomata and then dissolves in water and 
diffuses to the cells where photosynthesis takes place. The consumption of CO2 during 
photosynthesis depends on the sunlight and enzyme activity (plants always have sufficient water 
to split in photosynthesis).


## Page 6


6 
 
The rate of gaseous CO2 transport to the leaf is named as CO2 supply. The supply is driven by the 
CO2 concentration gradient between the atmosphere and the leaf inter-cellular space, and is 
controlled by the conductance of stomata and the air boundary layer. This supply can be 
expressed as [26] 
 
 


i
C
a
C
blc
st
s
C
C
C
g
g
J
,
,
1
,












, 
(10) 
where β and χ are the ratio of CO2 conductance and water vapor conductance through stomata 
and air boundary layer, respectively. β is the ratio of the molecular diffusivities of H2O and CO2, 
χ is power ¾ of β, and CC,a and CC,i are the concentration of CO2 at the atmosphere and inside the 
intercellular space of the leaf. 
The demand of atmospheric CO2 depends on the supply of sunlight and the performance of the 
enzymes that control photosynthetic activity. The plant gets some CO2 as a byproduct of 
metabolism or respiration activity in the mitochondria and lowers the atmospheric CO2 demand.  
 
For C4 plants, the electron transport to support CO2 reduction occurs in mesophyll (C4 cycle) 
and bundle-sheath (C3 cycle) cells. If the supply of sunlight is lowered compared with enzyme 
performance, which mainly occurs during the morning, sunset, or cloudy days, the 
photosynthetic rate can be expressed as [30] 
 
t
t
e
d
C
R
J
x
light
J



3
)
1(
)
(
,
,
, 
(11) 
where Je,t is the total electron transport rate is at leaf temperature, Rt is the rate of CO2 production 
from respiration in the mesophyll and bundle sheath cell, and x  is a fraction of total electrons 
that are used by the mesophyll.  
PEPCase, phosphoenolpyruvate carboxylase, and Rubisco are two enzymes that significantly 
control the photosynthesis activity in C4 plants. PEP (three-carbon backbone) controls the 
activity of the mesophyll cell (it catalyzes the primary carboxylation in a tissue that is close 
to the external atmosphere) and Rubisco controls activity in bundle sheath cell.  In the case of 
no limitations on the supply of reductant to photosynthesis (higher light intensities), the 
photosynthetic demand can be expressed as, [30] 
 









t
RO
m
m
C
bs
C
PEP
d
C
R
V
R
C
g
V
enzyme
J
max
,
,
,
min
)
(
, 
(12) 
Where the top expression in the right-hand side depends on the performance of PEPcase in the 
mesophyll cell, and the bottom expression depends on the Rubisco performance in the bundle


## Page 7


7 
 
sheath cell. gC,bs is the bundle-sheath conductance to CO2 , CC,m is the concentration of CO2  in the 
mesophyll cell (note that we assume that  
m
C
C , = 
i
C
C , ,  CO2 concentration in inter-cellar space), 
Rm is mitochondrial respiration in the mesophyll at leaf temperature (i.e. CO2 supply from the 
respiration of the mesophyll cell), Rt is the total mitochondrial respiration in the mesophyll and 
bundle sheath at leaf temperature, and VRO max is the maximum rubisco carboxylation rate.  
VPEP is the effective PEP carboxylation at leaf temperature. It depends on the availability of CO2 
and the regeneration of PEP and can be expressed as [30] 
 





R
PEP
p
m
C
PEP
m
C
PEP
V
K
C
V
C
V
,
,
,
max
min
, 
(13) 
where the top expression in right-hand side is related to the carboxylation rate of PEP, expressed 
with the Michaelis-Menten Equation. 
m
C
C , is the CO2 partial pressure in Mesophyll, 
max
PEP
V
is the 
maximum PEP carboxylation rate at leaf temperature, and Kp is the Michaelis-Menten constant 
for PEP carboxylase for CO2 at leaf temperature. Note that the Michaelis-Menten constant, Kp, 
refers to the concentration of CO2 at which the reaction rate is half of VPEPmax. The carboxylation 
rate can be decreased if there is not enough PEP, and that depends on the VPEP,R, the PEP 
regeneration rate at leaf temperature.  
The temperature-dependent properties in the equations are evaluated using the following 
equations [31] 
 








C
T
A
T
B
A
T
V
RO
RO
leaf
leaf
leaf
RO
e
e
Q
V
V






1
1
10
/)
25
(
,
10
max
25
max,
max
, 
(14) 
 
10
/)
25
(
,
10
max
25
max,
max


leaf
PEP
T
V
PEP
PEP
Q
V
V
, 
(15) 
 
10
/)
25
(
,
10
,
,
,
25


leaf
R
PEP
T
V
R
PEP
R
PEP
Q
V
V
, 
(16) 
 
10
/)
25
(
,
10
25
,


leaf
PEP
T
V
PEP
PEP
Q
V
V
, 
(17) 
 
10
/)
25
(
,
10
25
,


leaf
m
T
R
m
m
Q
R
R
, 
(18) 
 
10
/)
25
(
,
10
25
,


leaf
t
T
R
t
t
Q
R
R
, 
(19) 
 
)
15
.
273
(
00831
.0
25
,
,
leaf
b
a
T
J
J
e
t
e
e
J
J



, 
(20)


## Page 8


8 
 
where, A, B, C , Ja and Jb are physiological parameters related to the carboxylation rate and 
electron transport rate. The subscript 25 in the symbols indicates the parameters at 25◦C. Hourly 
Je,25 can be expressed as [30] 
 




2
4
25
,
2
25
,
25
,
25
,
max
max
max
e
e
e
e
IJ
J
I
J
I
J





, 
(21) 
where λ is the empirical curvature factor and
PSII
PAR
f
PAR
I
_


. fPAR_PSII is the fraction of PAR 
that contributes to the Photosystem II. 
Using the photosynthesis rate of the above two limiting cases, the CO2 demand can be expressed 
as [30] 
 

)
(
),
(
min
,
,
,
enzyme
J
light
J
J
d
C
d
C
d
C

, 
(22) 
Energy balance on leaf submodel 
In the above equations many of the parameters related to leaves, for instance, water vapor 
pressure, enzyme activities, etc., depend on the leaf temperature. Leaf temperature can be 
evaluated by using first principles in so-called “big leaf models” [28]. Several assumptions are 
considered in this model: the leaf is flat and perpendicular to the incident sunlight; leaf does not 
store any energy; and energy storage ; and there is negligible heat generation due to metabolic 
activity in the leaf.. Considering the leaf is at steady state, the energy balance equation on a leaf 
can be expressed as [28] 
 







0
]
2
[
]
1
[
,
4
4







vap
d
W
a
leaf
hbc
p
leaf
IR
a
IR
L
J
T
T
g
C
T
e
T
a
S
r
a

, 
(23) 
where the terms are energy input by solar irradiation and the surrounding irradiation, cooling by 
leaf irradiation, convective/conductive cooling by the air/temperature gradient and heat loss 
accompanying water evaporation. In Equation (23), a is the absorptance of the leaf, r is the 
reflectance, S is the solar irradiation, aIR is the absorptance of leaf for thermal infrared radiation, 
Lvap is the latent heat of vaporization of water, hc is the convective heat transfer coefficient, and 
ghbc is the air boundary conductance to heat transfer. 
The boundary layer conductance depends on leaf morphology and wind speed, and can be 
expressed via empirical relationships of dimensionless parameters Reynolds number, Re, and 
Prandtl number, Pr. It can be expressed as  
 
e
H
hbc
d
D
g
3
/
1
2
/
1 Pr
Re


, 
(24)


## Page 9


9 
 
where
a
e
cd
U


Re
;
H
a
D


Pr
; β=0.644*1.4 is an empirical parameter; de =0.72d, with d being the 
width of maize leaf and 0.72 being used to find the equivalent parabola of the leaf where the 
wind is flowing in the width direction of the parabola. Uc , νa and DH  represent the wind speed on 
the top of the canopy, kinetic viscosity of air and thermal diffusivity in air. The effect of the 
temporal variation of soil is not explicitly included in Equation (23). Instead, the effect was 
implemented using the FAO56 algorithm, as in [32]. 
Stomatal conductance submodel 
In the pathway of the supply of CO2 (Eq. (10)) from the environment and demand of H2O (Eq. 
(6)) to the environment, stomatal conductance is the most significant parameter. In general, 
stomatal conductance is around several orders of magnitude lower than that for air boundary 
layer conductance. Stomatal conductance is a very complex parameter that is affected by 
environment, plant physiology and heredity.   
 
At least 35 empirical models have been proposed to capture the complex relationship between 
stomata conductance and various factors including [5], [8], [33]–[38] Such factors include 
environmental factors, for example, solar radiation, soil water content, humidity and wind speed, 
etc., and physiological factors, for example, leaf water potential, root water potential, hydraulic 
root conductance, etc. Few models explicitly include the plant physiological influences on the 
stomatal conductance apart from entirely empirical functions. Here, we propose a model which is 
developed based on the sigmodal response of the stomatal conductance with respect to the leaf 
water potential [39]. The main concept of this model is shown in Fig. 1. Here, the stomatal 
conductance will start decreasing when leaf water potential touches the threshold potential, 
which depends on the plant genotype. Closing rate is controlled by the two sensitivity terms Sl 
and Sr and also the root water potential. The model is expressed as, 
 






Z
S
S
th
leaf
g
d
C
st
r
root
l
J
g
g
g
g













0526
.0
1
,
min
2
,
1
max
min
, 
(25) 
where the environmental response on the stomatal conductance is implicitly influenced by JC,d 
and ψleaf . ψth is the threshold bulk leaf water potential at stomatal closure, and Sr is the slope of 
the relationship between stomatal conductance and root water potential, ψroot.
1
g and 
2
g  are plant 
physiological properties related to photosynthesis. Z is a parameter to make the exponent 
dimensionless.  
Method to evaluate net photosynthesis and water usage 
Figure 2 shows the schematic of the concept and Fig. 3 shows the flow chart of the model 
implementation. For the input weather condition, soil and agronomic/management practices   the 
net photosynthesis and water transpiration (Tr) can be evaluated iteratively by satisfying (Eq. 6)


## Page 10


10 
 
(Eq. 10), (Eq. 23) and (Eq. 25).  A plant is considered dead and net photosynthesis is zero if the 
plant experiences a permanent wilting condition or permanent temperature damage. Both states 
cause irreversible damage to the plant. 
Framework for crop design  
Ideotype design requires identifying the optimal combination of plant physiological traits to 
maximize photosynthesis for specific environmental conditions and management practices. We 
formulate the design problem as an optimization problem. Thus, by writing photosynthesis as the 
following functional form, 


Traits
 
f
AN 
  
The optimization problem is defined as  



N
i
i
i
Trait
Trait
Traits
AN
1
....)
2
,1
(
max
arg

,  
(26) 
where i represents different conditions related with agronomic practices (e.g. no-irrigation, 
weekly irrigation, etc.), weather conditions, or soil type.  is a weighing factor that depends on 
the preference of the designer.  
 
Physiological traits and location/weather/management conditions 
Physiological Traits: In our model, a plant has been represented by 37 physiological traits. 
Typical values of most of those traits were collected from the current literature (Table 1). Note 
that these traits represent the adult crop. The traits used in the photosynthetic submodel were 
collected via gas exchange calibration.  
Among the 37 traits in this study, we considered seven hydraulic traits: minimum stomatal 
opening (
min
g
); maximum stomatal opening (
max
g
); sensitivity of stomatal opening with leaf 
water potential (
lS ); threshold bulk leaf water potential at stomatal closure (
th
); sensitivity of  
lS  with root water potential (
rS ); shoot hydraulic conductance (
shoot
K
); and root hydraulic 
conductance (
root
K
). These traits affect the stomatal conductance which is a vital trait for 
photosynthesis [ref]. For the optimization problem, those traits were bounded within the ranges 
in Table 2, ranges currently found in nature.  
Traits related to the photosynthetic submodel: Parameters used in the photosynthetic submodel 
are difficult to find in literature. Seventeen physiological parameters used in the model (that are 
related to the photosynthesis equations 14-20) were calibrated using gas exchange data. The net 
photosynthetic rate (An) was calibrated using gas exchange measurements made on leaves of two 
maize plants grown in mini-lysimeters at the Davis Agricultural experimental station in June to 
July 2013. Net photosynthetic rate was modelled as a function of three inputs: intercellular CO2 
concentration, photosynthetically active radiation (PAR) and leaf temperature. Thus, these three 
variables were varied using a LI-COR 6400 gas exchange system to obtain sufficient variation to 
calibrate the photosynthesis submodel.


## Page 11


11 
 
The CO2 response data is shown in Fig. 4(a-b) and the PAR-light-response data in Fig. 4(c-d). 
The entire dataset was used to calibrate the C4 photosynthetic parameters using an optimization 
algorithm.  
Location/weather/management conditions: We considered a drought-prone environment 
condition, i.e. Davis, CA in 2010 June-July (see S1) with clay soil (see Table 1) and irrigation 
frequency of seven days. 
 
Method to implement crop design framework 
There are several approaches to solve this optimization problem. Here, we utilize a gradient free, 
evolutionary optimization strategy. This strategy is selected because, as Figure 5 shows, the cost 
functional (Equation 26, when varying only two traits) is non-convex and corrugated. This 
highly-corrugated surface has many local maximum. This precludes the utilization of gradient-
based methods, and instead suggests the applicability of stochastic, multistart methods that can 
explore the phase space efficiently. We specifically use a genetic algorithm (GA) (a gradient-free 
meta-heuristic evolutionary search algorithm) to identify the optimal traits. GA is well suited to 
multi-modal, highly corrugated solution spaces, especially when the cost function is not easily 
adapted to gradient-based methods. 
Because GA deploys a population of potential solutions distributed over the design space, they 
are less prone to getting stuck in shallow local minima. GA is an inherently stochastic method, so 
we repeat each optimization multiple times (10 times) to consider statistical significance of 
results and attempt to reliably explore the phase space. The implementation framework can be 
found in Figure 6.  
 
Results and discussion 
 
Plant Physiology Model Validation  
The physiological model is implemented in MATLAB with inputs of soil and hourly weather 
data over a 60-day period. Each model evaluation for a given trait configuration – producing 
hourly outputs – took about 40 seconds on a standard laptop. 
The plant physiology model builds on the water transport model, and the temperature model 
depends on the conservation principles, which are inherently satisfied in our method. Therefore, 
we perform a validation exercise on the photosynthetic submodel. The excerise was performed 
where marked leaves on 14 maize plants, growing adjacent to the calibration plants, were 
monitored repeatedly using the LI-COR 6400 gas exchange system for a day. During that period 
the plants were subjected to a diurnal gradient of low to high ambient temperature, and a range of 
light. A subset of the plants also had water withheld to evaluate the photosynthetic submodel’s 
performance under water stress.


## Page 12


12 
 
The photosynthesis submodel, trained on the light, temperature and CO2 response curves, 
successfully predicted the photosynthesis of the 14 validation plants during the day of drought 
and varying temperature (Fig. 7). Current models of photosynthesis do not account for major 
damage to the photosynthetic apparatus in a mechanistic manner.  Thus, the model is unable to 
predict photosynthetic rates of a couple of points that represented very severely stressed plants.  
Design of ideotypes 
We deployed the crop design framework on the computing clusters available at Iowa State 
(CyEnce cluster) and via NSF XSEDE resources at TACC (Stampede). The simulations usually 
took about 4 hours to run for each optimization run on a server with 16 core 2.0 GHz Processer 
with 128 GB RAM. Optimizations were initialized with different random seeds and rerun 10 
times. In this process, over one million distinct trait combinations were evaluated, and 10 
ideotypes were designed. 
Comparison between Designed Crop and a Typical Crop 
Figure 8 (A) shows that the ideotype produces 10% higher net photosynthesis (yield) than that of 
the typical maize. To investigate that, we compare and explore the performances of those two 
crops on the hottest day of the season, June 27. The weather on that day is shown in Figure 8, 
with an average daytime temperature of 39.810C. Starting from the morning, the hourly value of 
solar radiation increases till midday and then decreases till sunset. Relative humidity is high at 
night and it decreases during the daytime. Hourly precipitations on that day are zero. It is noted 
that the atmospheric temperature increased as the day progresses and went as high as 430C. This 
temperature is higher than the optimum functional temperature of maize plants. Thus, plants that 
can cool their leaves are desirable. 
Figure 8 (D-E) reveals that for the above weather inputs, at the early and later part of the day, 
there is no significant variation of hourly net Photosynthesis (An) between the two plants. 
However, significant variation is observed at the midday. Photosynthesis depends on CO2, PAR, 
enzyme and temperature.  
Midday generally has enough PAR, so An depends on CO2 supply, enzyme performance and 
temperature. In our study, the enzyme performance profile is the same for both of the plants. 
Therefore, midday variation of An depends on the supply of CO2 and temperature.  
Figure 8 shows that during the midday period the average CO2 supply is 180 and 200 ppm for 
the typical maize and ideotype, respectively. The leaf temperature of the ideotype is lower than 
that of the typical maize. These two conditions enable a higher An for the ideotype (Fig 8). The 
lower temperature facilitates a shorter duration in which the leaf temperature is above the 
optimum temperature for photosynthesis. 
Reduced CO2 and lower temperature are related to high stomatal conductance, as shown in Fig. 
8. Therefore, Figure 8 (F &G) shows that the typical maize plant has lower stomatal conductance 
than that of an ideotype, but should create higher concentration gradient by lower CO2


## Page 13


13 
 
concentration than that of an ideotype in the early part of the day. Figure 8 (E & H) shows that, 
due to low stomatal conductance of the typical plant, the cooling of the leaf due to transpiration 
of water is lower, and as a result, leaf temperature is higher than that of an ideotype. In short, the 
main driver behind the increase of photosynthesis for the ideotype is the positive shift of 
stomatal opening operating range.  
Values and Significance of the Traits of the optimized ideotype 
The positive shift of stomatal conductance depends on the convoluted effect of the seven traits.  
Here, we present and discuss on the values and significance of the traits. 
 
Designed Values of the Traits  
Our framework provides ten different combinations of traits for the designed crop (Fig 9), all of 
them has the same yield (photosynthesis). Based on the variability, we came up with following 
two hypotheses:  
1) any values of traits within the upper and lower values of suggested traits can be a design crop; 
2) some traits might be insensitive for our condition and some traits have threshold values after 
which they are insensitive.  
Hypothesis 1 does not hold when we use arbitrary combinations of traits within the ranges (see 
Fig S2). To test the second hypothesis, we perform sensitivity analysis for all ten combinations 
by varying one parameter within the allowable range while keeping the others fixed. The 
sensitivity plots indicate that there are threshold values for all of the parameters. There are higher 
limits for Sl, ψth, Sr and lower limits for gmin, gmax, kshoot and kroot. Maintaining those threshold 
values and subtly changing the other threshold values in the opposite direction shows the 
decrease in photosynthesis. 
Significance of the Traits  
In short, photosynthesis mostly depends on the available sunlight, CO2 and temperature. Among 
these parameters, CO2 and temperature can be optimized by adjusting hydraulic parameters. 
Among the hydraulic parameters: gmin and gmax are the most directly constraining. gst (a direct 
function of gmin and gmax) is the dominating parameter in the transport pathways (causes the 
highest path resistance for both CO2 and H2O transports).  Rate of water transpiration controls 
the cooling effect on the leaves. Cooling (not freezing) is always beneficial during the night (it 
reduces the cost of respiration), however, during day it may have positive or negative effect on 
the photosynthesis based on the optimum temperature for the enzyme activity (Fig 8). Other 
variables including kshoot, Sl, Sr, ψth, kroot primarily ensure that the plant does not reach the 
permanent wilting potential. These values will affect the gst if the plant senses water scarcity 
when leaf water potential reaches the ‘red alert’ point, indicated by ψth value.   
More specifically, for our designed ideotype


## Page 14


14 
 
• 
gmax should be higher than a specific value, so that the plant is able to use its available 
photosynthetic capacity. The required value of gmax mostly depends on the highest solar 
radiation (PPF: photosensitive photon flux density, mostly 400 and 700 nm). 
• 
gmin should be as high as possible to reduce night-time respiration cost, although it may 
increase the irrigation cost for the season. gmin sets the minimum transpiration the plant 
can do under high VPD or extreme soil water deficit, and thus affects the rate of water 
depletion under the most extreme of circumstances.  
• 
Our designed ideotypes do not feel water stress (i.e. red alert) in well-watered conditions, 
and are never forced to adjust gst due to water-related issues. However, an ideotype’s 
kplant and red alert value, ψth, must be selected appropriately. A lower kplant than the 
specified value may cause a leaf water potential that is lower than the ‘red alert’ value, 
i.e. the plant will register water stress. A similar effect will happen if the plant increases 
(less negative) the ψth value. Required values for kplant and ψth have an inverse 
relationship. Therefore, to reduce the cost of root generation, the plant should operate at 
the lowest (more negative) possible ψth, i.e. a value close to the permanent wilting 
potential, thus lowering the kplant requirement, i.e.  it refers to less root production. 
Tradeoff between below ground mass and photosynthesis/above ground mass 
Next, we extrapolate our results from our design space (reproductive stage) to vegetative stage. 
During the vegetative stage, to increase the photosynthetic capability of the plant (LAI), a bigger 
shoots could be better, whereas smaller roots would help the plant to invest more resources into 
growing the shoot. Therefore, we explore the effect of a smaller root, i.e. smaller kroot, on the net 
photosynthesis of the ideotypes.   
 
Figure 10 shows that a 50% reduction of kroot from 40 to 20 reduces the net photosynthesis by 
only 0.06%. For the reduced kroot plant, the leaf water potential sometimes reaches lower than the 
threshold leaf water potential (ψth) and closes (Figure 11). The modified plant has the potential to 
increase LAI during the vegetative stage, leading to improvement in net photosynthesis (yield).  
Conclusions 
An integrated framework of optimization, thermodynamics and plant physiology was developed 
to design a crop ideotype. The backbone of the framework is a 1-D plant physiology model and 
the coupling of transport and energy conversion models based on laws of thermodynamics. The 
models were augmented with a nature-inspired meta-heuristic optimization method, the genetic 
algorithm (GA), and was implemented via the MATLAB® software. The framework was used to 
design maize crop for a drought-prone weather condition in Davis, CA. Seven physiological 
traits which are primarily related to plant hydraulics and ultimately affect the photosynthesis and 
water usage were considered in the study. The traits are minimum stomatal opening (
min
g
); 
maximum stomatal opening (
max
g
); sensitivity of stomatal opening with leaf water potential (
lS
); threshold bulk leaf water potential at stomatal closure (
th
); and sensitivity of  
lS  with root


## Page 15


15 
 
water potential (
rS ); shoot hydraulic conductance (
shoot
K
); and root hydraulic conductance (
root
K
). With enough irrigation, the designed crop showed 10% improvement in yield, and 
max
g
, 
min
g
 and 
th
 are found to be the vital traits. Currently, the model is using hourly data; however, 
it could be easily modified for more frequent data. The framework is modular and can be easily 
augmented with other existing mechanistic models to capture more physics. The developed tool 
can help plant breeders and scientists to determine the optimal crop ideotypes for various 
climates (climate-smart crops) and locations. Integration of the developed framework with 
breeding programs can speed the crop development process, wherein the framework can be used 
to propose ideotypes for target environments and the breeder can breed plants like based on the 
ideotypes. 
 
Potentially, ideotypes designed using a different crop model might look different from those 
presented, as shown for  wheat in [40]. These models can simulate observed yields under a range 
of environments for the current conditions. However, simulated climate change impacts could 
vary across models due to differences in model structures and parameter values [41]. Further 
improvements of crop models and a more rigorous framework will be required for robust crop 
ideotype design. 
 
ACKNOWLEDGEMENTS 
T.Z.J, B.G, D.A gratefully acknowledge financial support from the Presidential initiative for 
interdisciplinary research of Iowa State University. B.G and T.Z.J gratefully acknowledge the 
Plant Science Institute at Iowa State University, and computing support via NSF XSEDE 
CTS110007. M.E.G gratefully acknowledges support via USDA National Institute of Food and 
Agriculture, Hatch project number #1001480. 
AUTHOR CONTRIBUTIONS:  
D.A formed the interdisciplinary team and proposed to couple numerical optimization and plant 
physiology, D.A, M.E.G, B.G designed research plan, M.E.G. designed the crop hydraulic 
model, B.G. implemented model, all authors improved the model, B.G and T.Z.J designed the 
optimization framework, T.Z.J ran the simulations and processed the data, all authors analyzed 
data and wrote the paper. 
COMPETING FINANCIAL INTERESTS 
The author(s) declare no competing financial interests.


## Page 16


16 
 
References 
[1] H. C. J. Godfray et al., “Food Security: The Challenge of Feeding 9 Billion People,” 
Science, vol. 327, no. 5967, pp. 812–818, Feb. 2010. 
[2] A. J. Challinor, F. Ewert, S. Arnold, E. Simelton, and E. Fraser, “Crops and climate change: 
progress, trends, and challenges in simulating impacts and informing adaptation,” J. Exp. 
Bot., vol. 60, no. 10, pp. 2775–2789, Jul. 2009. 
[3] K. J. Boote, M. J. Kropff, and P. S. Bindraban, “Physiology and modelling of traits in crop 
plants: implications for genetic improvement,” Agric. Syst., vol. 70, no. 2–3, pp. 395–420, 
Nov. 2001. 
[4] P. Martre, B. Quilot-Turion, D. Luquet, M.-M. O.-S. Memmah, K. Chenu, and P. Debaeke, 
“Model-assisted phenotyping and ideotype design,” in Crop Physiology, Elsevier, 2015, pp. 
349–373. 
[5] K. H. Jensen, J. Lee, T. Bohr, H. Bruus, N. M. Holbrook, and M. A. Zwieniecki, 
“Optimality of the Münch mechanism for translocation of sugars in plants,” J. R. Soc. 
Interface, vol. 8, no. 61, pp. 1155–1165, Aug. 2011. 
[6] C. Doussan, L. Pagès, and G. Vercambre, “Modelling of the Hydraulic Architecture of Root 
Systems: An Integrated Approach to Water Absorption—Model Description,” Ann. Bot., 
vol. 81, no. 2, pp. 213–223, Feb. 1998. 
[7] C.-T. Lai and G. Katul, “The dynamic role of root-water uptake in coupling potential to 
actual transpiration,” Adv. Water Resour., vol. 23, no. 4, pp. 427–439, Jan. 2000. 
[8] P. J. Sellers, Y. Mintz, Y. C. Sud, and A. Dalcher, “A Simple Biosphere Model (SIB) for 
Use within General Circulation Models,” J. Atmospheric Sci., vol. 43, no. 6, pp. 505–531, 
Mar. 1986. 
[9] T. Vogel, M. Dohnal, J. Dusek, J. Votrubova, and M. Tesar, “Macroscopic Modeling of 
Plant Water Uptake in a Forest Stand Involving Root-Mediated Soil Water Redistribution,” 
Vadose Zone J., vol. 12, no. 1, Feb. 2013. 
[10] J. Rings et al., “Bayesian Inference of Tree Water Relations Using a Soil-Tree-Atmosphere 
Continuum Model,” Procedia Environ. Sci., vol. 19, pp. 26–36, Jan. 2013. 
[11] V. Couvreur, J. Vanderborght, and M. Javaux, “A simple three-dimensional macroscopic 
root water uptake model based on the hydraulic architecture approach,” Hydrol Earth Syst 
Sci, vol. 16, no. 8, pp. 2957–2971, Aug. 2012. 
[12] J. Wang, Q. Yu, and X. Lee, “Simulation of crop growth and energy and carbon dioxide 
fluxes at different time steps from hourly to daily,” Hydrol. Process., vol. 21, no. 18, pp. 
2474–2492, Aug. 2007. 
[13] K. Steppe, D. J. W. De Pauw, R. Lemeur, and P. A. Vanrolleghem, “A mathematical model 
linking tree sap flow dynamics to daily stem diameter fluctuations and radial stem growth,” 
Tree Physiol., vol. 26, no. 3, pp. 257–273, Mar. 2006. 
[14] F. Somma, J. W. Hopmans, and V. Clausnitzer, “Transient three-dimensional modeling of 
soil water and solute transport with simultaneous root growth, root water and nutrient 
uptake,” Plant Soil, vol. 202, no. 2, pp. 281–293, May 1998. 
[15] R. A. Duursma and B. E. Medlyn, “MAESPA: a model to study interactions between water 
limitation, environmental drivers and vegetation function at tree and stand levels, with an 
example application to [CO2] ? drought interactions,” Geosci. Model Dev. Katlenburg-
Lindau, vol. 5, no. 4, p. 919, 2012. 
[16] T. H. van den Honert, “Water transport in plants as a catenary process,” Discuss. Faraday 
Soc., vol. 3, no. 0, pp. 146–153, 1948.


## Page 17


17 
 
[17] A. Askarzadeh, “Bird mating optimizer: An optimization algorithm inspired by bird mating 
strategies,” Commun. Nonlinear Sci. Numer. Simul., vol. 19, no. 4, pp. 1213–1228, Apr. 
2014. 
[18] I. F. Jr, X.-S. Yang, D. Fister, and I. Fister, “Cuckoo Search: A Brief Literature Review,” in 
Cuckoo Search and Firefly Algorithm, X.-S. Yang, Ed. Springer International Publishing, 
2014, pp. 49–62. 
[19] K. Elofsson, G. Bengtsson, and I.-M. Gren, “Optimal Management of Invasive Species with 
Different Reproduction and Survival Strategies,” Nat. Resour. Model., vol. 25, no. 4, pp. 
599–628, Nov. 2012. 
[20] C. Riedelsheimer and A. E. Melchinger, “Optimizing the allocation of resources for 
genomic selection in one breeding cycle,” TAG Theor. Appl. Genet. Theor. Angew. Genet., 
vol. 126, no. 11, pp. 2835–2848, Nov. 2013. 
[21] C. XiangWei, Y. TianLi, and Y. GongMing, “Research advances in non-destructive 
prediction technologies using VIS/NIR spectroscopy for kiwifruit property,” Transactions 
of the Chinese Society of Agricultural Engineering, 20-Jul-2006. [Online]. Available: 
https://eurekamag.com/research/012/927/012927668.php. [Accessed: 21-Mar-2017]. 
[22] G. Decoux and F. Hospital, “Popmin: A Program for the Numerical Optimization of 
Population Sizes in Marker-Assisted Backcross Programs,” J. Hered., vol. 93, no. 5, pp. 
383–384, Sep. 2002. 
[23] S. Manzoni, G. Vico, S. Palmroth, A. Porporato, and G. Katul, “Optimization of stomatal 
conductance for maximum carbon gain under dynamic soil moisture,” Adv. Water Resour., 
vol. 62, pp. 90–105, Dec. 2013. 
[24] M. A. Semenov and P. Stratonovitch, “Designing high-yielding wheat ideotypes for a 
changing climate,” Food Energy Secur., vol. 2, no. 3, pp. 185–196, Dec. 2013. 
[25] V. Picheny et al., “Finding realistic and efficient plant phenotypes using numerical 
models,” ArXiv Prepr. ArXiv160303238, 2016. 
[26] N. Park, Physicochemical & environmental plant physiology, Park vols. Academic Press, 
2009. 
[27] I. R. Cowan, “Transport of Water in the Soil-Plant-Atmosphere System,” J. Appl. Ecol., 
vol. 2, no. 1, pp. 221–239, 1965. 
[28] G. S. Campbell and J. M. Norman, An introduction to environmental biophysics. New 
York, NY, USA: Springer, 1998. 
[29] A. L. Buck, “New Equations for Computing Vapor Pressure and Enhancement Factor,” J. 
Appl. Meteorol., vol. 20, no. 12, pp. 1527–1532, Dec. 1981. 
[30] S. V. Caemmerer, Biochemical models of leaf photosynthesis. 2000. 
[31] G. J. Collatz, M. Ribas-Carbo, and J. A. Berry, “Coupled Photosynthesis-Stomatal 
Conductance Model for Leaves of C4 Plants,” Funct. Plant Biol., vol. 19, no. 5, pp. 519–
538, Oct. 1992. 
[32] R. G. Allen, L. S. Pereira, D. Raes, M. Smith, and others, “Crop evapotranspiration-
Guidelines for computing crop water requirements-FAO Irrigation and drainage paper 56,” 
FAO Rome, vol. 300, no. 9, p. D05109, 1998. 
[33] Z. Dong, O. Danilevskaya, T. Abadie, C. Messina, N. Coles, and M. Cooper, “A Gene 
Regulatory Network Model for Floral Transition of the Shoot Apex in Maize and Its 
Dynamic Modeling,” PLOS ONE, vol. 7, no. 8, p. e43450, Aug. 2012.


## Page 18


18 
 
[34] M. A. Zwieniecki, H. A. Stone, A. Leigh, C. K. Boyce, and N. M. Holbrook, “Hydraulic 
design of pine needles: one-dimensional optimization for single-vein leaves,” Plant Cell 
Environ., vol. 29, no. 5, pp. 803–809, May 2006. 
[35] D. N. L. Menge, F. Ballantyne, and J. S. Weitz, “Dynamics of nutrient uptake strategies: 
lessons from the tortoise and the hare,” Theor. Ecol., vol. 4, no. 2, pp. 163–177, May 2011. 
[36] V. M. Dunbabin, S. McDermott, and A. G. Bengough, “Upscaling from Rhizosphere to 
Whole Root System: Modelling the Effects of Phospholipid Surfactants on Water and 
Nutrient Uptake,” Plant Soil, vol. 283, no. 1–2, pp. 57–72, May 2006. 
[37] A. J. Guswa, “Soil-moisture limits on plant uptake: An upscaled relationship for water-
limited ecosystems,” Adv. Water Resour., vol. 28, no. 6, pp. 543–552, Jun. 2005. 
[38] G. Damour, T. Simonneau, H. Cochard, and L. Urban, “An overview of models of stomatal 
conductance at the leaf level,” Plant Cell Environ., vol. 33, no. 9, pp. 1419–1438, Sep. 
2010. 
[39] T. J. Brodribb and N. M. Holbrook, “Declining hydraulic efficiency as transpiring leaves 
desiccate: two types of response*,” Plant Cell Environ., vol. 29, no. 12, pp. 2205–2215, 
Dec. 2006. 
[40] S. Asseng et al., “Uncertainty in simulating wheat yields under climate change,” Nat. Clim. 
Change, vol. 3, no. 9, pp. 827–832, Sep. 2013. 
[41] R. P. Rötter, T. R. Carter, J. E. Olesen, and J. R. Porter, “Crop-climate models need an 
overhaul,” Nat. Clim. Change Lond., vol. 1, no. 4, pp. 175–177, Jul. 2011.


## Page 19


19 
 
Figures and Legends 
  
 
Figure 1: A conventional resistance or conductance (resistance=1/conductance) model of maize 
hydraulics (panel a), and the model used for simulating maize hydraulics including feedbacks 
(panel b). The conductance of the stomata to water vapor (gst) and CO2 is modulated by the 
water potential of the leaf (ψleaf) if below a threshold (ψth). The stomatal opening is scaled to the 
maximum stomatal conductance (gmax; a proxy of how many stomata and how wide they open) 
which sets the maximum water loss rate and the maximum CO2 uptake rate for sunlit leaves. 
How effective stomatal closure is (minimum stomatal conductance; gmin) is determined by 
cuticle waxes which stop water loss from the leaf surface, affecting the rate of desiccation under 
drought, but this state also prevents CO2 uptake. The slope of the response is tuned by an 
inherent sensitivity (Sl) or a contribution of the root, based upon sensing of soil drying (Sr). The 
supply of water is proportional to the difference of water potential between soil and air, and 
inversely proportional to three conductances in series: Ksoil, Kroot, and Kstem+leaf. The 
demand for water is driven by environmental variables: the boundary layer conductance and the 
temperature of the leaf. The leaf temperature is determined through an energy balance and 
influences both transpiration and a coupled model of photosynthesis.  
 
1/Ksoil
Ysoil
Yleaf
1/Kleaf
1/Kstem
1/Kroot
1/gblc
Yair
Tr
1/gst
a
1/Kroot
1/gblc
ψleaf 
ψth 
ψsoil
Tr
1/gmax
breaks at ψleaf < ψth 
1/gmin- 1/gmax
Resistance adjustment
1/gst
1/gst
Ψair 
ψroot
f(Sl ,Sr)
1/Kshoot
1/gst- 1/gmax
b


## Page 20


20 
 
 
Figure 2: Model input, output and connectivity among the submodels.


## Page 21


21 
 
 
 
Figure 3: Flowchart for the implementation of plant physiology model 
 
 
 
 
Evaluate ψleaf by satisfying  supply and 
demand of water via minimizing (Jw,d-
Jw,s)2 . Supply of water from soil to the 
leaf, Jw,d , and evaporation of water 
vapor from leaf to the atmosphere 
Jw,s, are calculated from equations, (1) 
and (6), respectively.   
Evaluate leaf temperature (Tleaf) by 
considering energy equilibrium on 
the leaf via satisfying equation (23)
Evaluate CO2 concentration inside the 
intercellular space of the leaf (Cc,i) by 
satisfying transport balance via 
minimizing (JC,s-JC,d)2
.  supply of CO2 
from the environment, JC,s and the 
damend of CO2 by the plant, JC,d, are 
calculated from equations (10) and 
(22), respectively.
At a particular time step, 
ti calculate soil water 
potential using Eq. 4
Guess stomatal 
conductance, gst
(gst,new –
gst)2<tol
Calculate corrected gst,new
using Eq 25
Two factors must be 
favorable for a leaf to 
remain alive: leaf water 
potential (ψwilt) and 
temperature (Tdamage) must 
remain within nonlethal 
bounds. Check for survival 
of plant: if ψleaf ≤ψwilt or 
Tleaf ≤Tdamage
Using corrected gst,new , 
evaluate ψleaf, Tleaf, and Cc,i
using steps 3,4 and 5, 
respectivley 
Store water loss/usage, Tr 
= Jw,d, and net CO2
consumption, An = Jc,d as 
photo
Cumulative 
photosynthesis, Photo = 
sum(photoiΔt), and 
cumulative water usage 
=sum(TriΔt)  
gst = gst,new
ti+1 = ti +Δt, Δt is the 
period of the inputted 
weather data
Average net 
photosynthesis 
must be positive 
for a leaf to 
remain alive. 
Output: Photo 
and Water 
Usage
Output:
Photo = 0
yes
no
yes
no
yes
no
no
yes
ti+1<period
Start


## Page 22


22 
 
 
Figure 4: (a-b) CO2 responses of maize photosynthesis at varying leaf temperatures for two 
plants used in the calibration of the photosynthesis submodel. Lines connect points measured at 
the same leaf temperature. (c-d) Response of maize photosynthesis to photosynthetically active 
radiation (PAR) measured at varying leaf temperatures for two plants used in the calibration. 
Lines connect points measured at the same leaf temperature.  
 
 
a
b
c
d


## Page 23


23 
 
 
 
Figure 5: Distribution of photosynthesis, in terms of CO2 assimilation, within the selected 
ranges of gmin and ψth for typical maize as in Table 1.


## Page 24


24 
 
 
 
Figure 6:  Flowchart of crop design framework implementation.


## Page 25


25 
 
 
 
Figure 7: Validation of the C4 photosynthesis submodel. The circles represent the predicted and 
observed calibration data for light, CO2 and temperature responses for plant 1 and triangles for 
plant 2. The diamonds represent the validation data: the observed and predicted photosynthesis 
of 14 plants measured over a day varying in drought treatments, temperature and light. The 
points that deviate from the 1:1 relationship were plants that underwent the greatest drought 
stress during the hottest time of the day, and represent photosynthetic inhibition or damage. 
-10
0
10
20
30
40
50
-10
0
10
20
30
40
50
Predicted An ( mol/m 2/s)
Observed An ( mol/m 2/s)
e


## Page 26


26 
 
 
Figure 8: (A) Hourly cumulative photosynthesis for the typical plant (red line) and the sets of 
simulated ideotypes at well-irrigated condition. For simulated plants, the profiles are overlapped. 
Here, instead of days of the months, time has been presented as hours. (B-C) Hourly variation of 
solar radiation and relative humidity on June 27. (D-E) Hourly variation of photosynthesis (An), 
and CO2
 concentration inside the leaf. (F) Green for PEP limited case, Orange for Rubisco 
limited case, Red symbol (for ideotypes) is the net effect with CO2 concentration 180 ppm, Gray 
symbol (for typical) is the net effect with CO2 concentration 120 ppm.  Blue lines are light 
(PAR) limited case. (G-H) Hourly variation of variation stomatal conductance with respect to 
minimum conductance, and leaf temperature. 
4 am 8 am 12 4 pm 8 pm
An (mol/m
2)
0
10
20
30
40
4 am 8 am 12 4 pm 8 pm
gst-gmin (mol/m
ss)
0
0.1
0.2
0.3
4 am 8 am 12 4 pm 8 pm
Ci (ppm)
0
200
400
600
4 am 8 am 12 4 pm 8 pm
PAR ( mmol/m
2s)
T (
o)C
0
0.5
1
1.5
2
25
30
35
40
45
4 am 8 am 12 4 pm 8 pm
RH(%)
U (m/s)
40
60
80
1
2
3
June 1
June 15
July 31
Photo (mol/ m
2)
20
40
60
80
Photo
4 am 8 am 12 4 pm 8 pm
Tleaf (
oC)
20
25
30
35
40
An(mol/m
2s)
Tleaf ( C)
0
20
40
60
20
40
11 am
1 pm
9 am
6 am
7 am
6 pm
4 pm
2 pm
A
B
C
D
E
F
G
H


## Page 27


27 
 
 
Figure 9: Variation of the traits among the outcomes obtained via optimizations. The big red 
symbol corresponds to the typical value and the numbers indicate the upper and lower limits of 
the traits (Table 1).


## Page 28


28 
 
 
  
 
Figure 10: (top) Effect of kroot on the photosynthesis (mid-bottom) hourly variation of stomatal 
conductance and leaf water potential for the designed ideotype (red) and modified ideotype 
(blue).


## Page 29


29 
 
Table 1 Management/Agronomic parameters, plant physiological parameters of typical maize, 
and bio-chemistry parameters for gas exchange calculations. 
Management/Agronomic parameters 
b , Soil-texture-dependent parameter (unit less) 
14.95 
sat
k
, Saturated soil hydraulic conductivity [mol m-1 s-1 MPa-1] 
1.69 
sat

[MPa] 
-0.00598 
sat

( Saturated water content in the soil) [m3 m-3] 
0.39 
s
H  (depth of soil) [m] 
1 
Rs,  Radius of soil occupied/supplied for one plant [m] 
0.1128 
Irrigation frequency (day) 
7 
Plant physiological parameters 
L, Root length density (m m-3) 
15200 
rroot, Root radius at the end of rhizosphere (m) 
0.0005 
d, leaf width (m) 
0.1 
Hc, Height of the plant (m) 
1 
Permanent wilting soil water potential for leaf wilting (MPa) 
-1.33 
Temperature for permanent leaf damage (0C) 
60 
LAI, Leaf area index, [m2m-2] 
1 
Plant Hydraulic Parameters 
min
g
,  minimum stomatal conductance mol m-2s-1 
0.02 
max
g
, maximum stomatal conductance mol m
-2s
-1 
0.25 
lS , response of stomatal conductance with leaf water potential mol m
-2s
-1MPa
-1 
15 
rS , response of stomatal conductance upon sensing drying soil mol m
-2s
-1MPa
-2 
-1.25 
th

, threshold of leaf water potential for stomatal closure, MPa 
200 
leaf
K
,  hydraulic conductance of leaf mmol m
-2s
-1 MPa
-1 
45 
Kroot, hydraulic conductance of root mmol m-2s-1MPa-1 
45 
Kroot, hydraulic conductance of stem mmol m-2s-1MPa-1 
45 
Bio-chemistry parameters from gas exchange data 
1
g (unitless) 
0.0036 
b
J (unitless) 
4.93 
max
,
10
PEP
V
Q
 (unitless) 
1.39 
2
g (unitless) 
1.1693 x (unitless) 
0.0844 
10
,Q
d
R
(unit less) 
1.55 
max
,
,
10
R
VPEP
Q
 (unit less) 13.1 
(unitless) 
0.00445 
a
J (unit less) 
5.57 
max
,
10
RO
V
Q
 (unit less) 
0.945 
(unitless) 
0.0715 
25
,tR
 [mol m-2 s-1] 
2.28 
A (unit less) 
0.094 
25
max,
J
 [mol m-2 s-1] 322.3 
25
,
,R
PEP
V
 [mol m-2 s-1] 
96.1 
B (unit less) 
31.6 
25
max,
PEP
V
 [mol m-2 s-1] 51


## Page 30


30 
 
C (unit less) 
42.1 
25
max,
RO
V
 [mol m-2 s-1] 126.7


## Page 31


31 
 
Table 2 Bounds to hydraulic parameters varied in the genetic algorithm. 
 
min
g
 
max
g
 
l
lS

tan

 
r
rS

tan

 
th

 
stem
leaf
K

 
root
K
 
mol m-2s-1 
mol m-2s-1MPa-1 mol m-2s-1MPa-2 
MPa 
mmol m-2s-1  MPa-1 
Lower 
bound 
1e-6 
0.07 
l=0 
r
=0 
-1.33 
1e-6 
1e-6 
Upper 
bound 
3 
3.0 
l=89.99 
r
=89.99 
0 
30  
60


## Page 32


32 
 
Nomenclature 
a  
- 
Absorptance of leaf 
IR
a
 
- 
Absorptance of leaf for thermal infrared radiation 
A  
- 
Constant related with carboxylation rate 
An  
[mol m-2 s-1] 
Hourly net assimilation or net photosynthesis 
b  
- 
Soil texture dependent parameter 
0
b  
- 
Parameter related with probabilistic GA formulation 
1b  
- 
Parameter related with probabilistic GA formulation 
2b  
- 
Parameter related with probabilistic GA formulation 
B  
- 
Constant related with carboxylation rate 
0c  
kPa 
Constant related with Tetens formula 
1c  
- 
Constant related with Tetens formula 
2c  
° C 
Constant related with Tetens formula 
C  
- 
Constant related with carboxylation rate 
a
c
C ,  
[Pa Pa-1] or ppm 
Atmosphere CO2 partial pressure, or concentration 
i
c
C ,  
[Pa Pa-1] or ppm 
Intercellular airspace CO2 partial pressure, or concentration 
m
c
C ,  
[Pa Pa-1] 
Mesophyll CO2 partial pressure, or concentration. 
P
C  
[J mol-1K-1] 
Specific heat of air. 
d  
[m] 
Leaf average width 
e
d  
[m] 
Parameter related with leaf width 
H
D  
[m2s-1] 
Thermal diffusivity in air 
WV
D
 
[m2s-1] 
Water vapor diffusivity in air 
PSII
PAR
f
_
 
- 
Fraction of PAR contributes to the Photosystem II


## Page 33


33 
 
1
g  
- 
lant physiological parameter related with photosynthesis or 
CO2 assimilation 
2
g  
- 
lant physiological parameter related with photosynthesis or 
CO2 assimilation 
blc
g
 
[mol m-2 s-1] 
Boundary conductance to water transport 
hbc
g
 
[mol m-2 s-1] 
Boundary conductance to heat transfer on leaf surface. 
min
g
 
[mol m-2 s-1] 
Minimum Stomatal conductance, or stomatal conductance  at 
light compensation point, minimum stomatal conductance to 
water vapor including epidermal conductance 
max
g
 
[mol m-2 s-1] 
Maximum Stomata conductance 
bs
C
g
,
 
[mol m-2 s-1] 
Bundle-sheath conductance to CO2 
st
g  
[mol m-2 s-1] 
Effective stomata conductance to water 
Gr  
- 
Grashof number 
s
H  
[m] 
Depth of soil 
c
H  
[m] 
Height of the plant 
m
H
 
[m] 
Height at which wind speed obtained from weather data 
I  
[mol m-2 s-1] 
A parameter related with electron transport rate 
a
J  
[mol m-2 s-1] 
Physiological parameter related with electron transport rate 
b
J  
[mol m-2 s-1] 
Physiological parameter related with electron transport rate 
(enzyme)
,d
C
J
 
[mol m-2 s-1] 
CO2 demand by photosynthetic activity based enzyme limited 
condition 
)
(
,
light
J
d
C
 
[mol m-2 s-1] 
CO2 demand by photosynthetic activity based sunlight limited 
condition 
t
eJ ,  
[mol m-2 s-1] 
total electron transport rate is at leaf temperature 
25
,eJ
 
[mol m-2 s-1] 
total electron transport rate is at 25 ° C 
25
max,
eJ
 
[mol m-2 s-1] 
Maximum total electron transport rate is at 25 ° C


## Page 34


34 
 
d
W
J
,  
[mol m-2 s-1] 
Rate of water vapor  demanded by atmosphere from leaf 
s
W
J
,  
[mol m-2 s-1] 
Rate of water supplied from soil to leaf 
sat
k
 
[mol m-2 s-1 Pa-1] 
hydraulic conductivity of saturated soil 
leaf
K
 
[mol m-2 s-1 Pa-1] 
leaf hydraulic conductance to water 
p
K  
[mol m-2 s-1 Pa-1] 
the Michaelis-Menten constant 
plant
K
 
[mol m-2 s-1 Pa-1] 
plant hydraulic conductance to water 
root
K
 
[mol m-2 s-1 Pa-1] 
root hydraulic conductance to water 
soil
K
 
[mol m-2 s-1 Pa-1] 
soil hydraulic conductance to water 
stem
K
 
[mol m-2 s-1 Pa-1] 
stem hydraulic conductance to water 
L  
[m m-3] 
Root length density , root length per unit volume of soil 
vap
L
 
[J mol-1] 
Latent heat of vaporization of water. 
LAI  
[m2m-2] 
Leaf area index 
m  
- 
a factor related with zero plane displacement for wind speed 
n  
- 
a factor related to the momentum roughness parameter for 
wind speed 
photo  
[mol m-2 s-1] 
Hourly net CO2 assimilation 
Photo  
[mol m-2 ] 
Total photo 
PAR  
[mol m-2 s-1] 
Photo active radiation 
o
P  
- 
Initial population in genetic algorithm 
aP  
[Pa] 
Atmospheric pressure 
Pr  
 
Prandtl number 
va
P  
[Pa] 
Vapor pressure of air 
vl
P  
[Pa] 
Vapor pressure of leaf surface


## Page 35


35 
 
Rt
Q
,
10
 
- 
Q10 coefficient conversion factor related to mitochondrial 
respiration calculation 
max
,
10
PEP
V
Q
 
- 
Q10 coefficient conversion factor related to maximum PEP 
carboxylation 
max
,
,
10
R
VPEP
Q
 
- 
Q10 coefficient conversion factor related to maximum PEP 
regeneration 
max
,
10
RO
V
Q
 
- 
Q10 coefficient conversion factor related to maximum rubisco 
carboxylation 
r  
- 
Reflectance, i.e. amount of sunlight reflected from the 
surroundings, 
root
r
 
[m] 
Root radius including rhizosphere 
tR  
[mol m-2 s-1] 
Total mitochondrial respiration in the mesophyll and bundle 
sheath at leaf temperature 
25
,tR
 
[mol m-2 s-1] 
Total mitochondrial respiration in the mesophyll and bundle 
sheath at  25° C  temperature 
Re  
- 
Reynolds number 
RH  
- 
Relative humidity of surrounding air. 
S  
[W m -2] 
Solar radiation, 
cS  
- 
Schmidt number 
lS  
[mol m-2 s-1MPa-1] 
Slope of stomatal conductance with leaf water potential 
rS  
[mol m-2 s-1MPa-2] 
Slope of 
lS  with root water potential 
a
T  
[° C] 
Temperature of air 
leaf
T
 
[° C] 
Temperature of leaf 
wilt
T
 
[° C] 
leaf temperature at permanent leaf damage 
Tr  
[mol m-2 s-1] 
Rate of water transpires from soil to environment through the 
plant 
c
U  
[m s-1] 
Wind speed on the canopy 
m
U
 
[m s-1] 
Wind speed from weather data


## Page 36


36 
 
*
U  
[m s-1] 
Shearing velocity 
PEP
V
 
[mol m-2 s-1] 
Effective Rate of PEP carboxylation at leaf temperature given 
by Michaelis-Menten Equation 
max
PEP
V
 
[mol m-2 s-1] 
Maximum PEP carboxylation rate at leaf temperature 
25
max,
PEP
V
 
[mol m-2 s-1] 
Maximum PEP carboxylation rate at 25 C temperature 
R
PEP
V
,  
[mol m-2 s-1] 
PEP regeneration rate at leaf temperature 
25
,
,R
PEP
V
 
[mol m-2 s-1] 
PEP regeneration rate at 25 C temperature 
max
RO
V
 
[mol m-2 s-1] 
Maximum rubisco carboxylation rate at leaf temperature 
25
max,
RO
V
 
[mol m-2 s-1] 
Maximum rubisco carboxylation rate at 25 C temperature 
VPD  
[Pa Pa-1] 
Vapor pressure deficit between intercellular space and 
atmosphere 
Loss
Water 
 
[mol m-2 s-1] 
Transpiration of water  through the plant 
x  
- 
is a fitting parameter related to photosynthesis rate 
Z  
- 
parameter to make the exponent dimensionless in stomatal 
conductance model 
 
Greek 
 
- 
empirical parameter related with boundary layer conductance 
 
- 
ratio of CO2 conductance and water vapor conductance through 
stomata 
 
- 
Empirical curvature factor related with electron transport rate 
 
- 
ratio of CO2 conductance and water vapor conductance through 
air boundary layer 
a

 
[m2s-1] 
kinetic viscosity of air 
 
[m3m-3] 
Volumetric water content in the soil 
sat

 
[m3m-3] 
Soil volumetric saturation


## Page 37


37 
 
leaf

 
[Pa] 
Leaf water potential 
root

 
[Pa] 
Root water potential 
sat

 
[Pa] 
Saturated soil water potential 
soil

 
[Pa] 
Soil water potential 
root
soil,

 
[Pa] 
Soil water potential at root 
th

 
[Pa] 
Threshold leaf water potential at stomatal closure 
 
[W m−2 K−4] 
Stefan Boltzmann constant


## Page 38


38 
 
Supplementary Materials 
 
Integrating optimization with thermodynamics and plant physiology for crop 
ideotype design 
Talukder Z. Jubery1, Baskar Ganapathysubramanian1, Matthew E. Gilbert2, and Daniel 
Attinger1 
1Department of Mechanical Engineering and Department of Electrical and Computer 
Engineering, Iowa State University, Ames, IA, 50011;  
2Department of Plant Sciences, University of California, Davis, CA 95616, USA. 
*Correspondence to: baskarg@iastate.edu, gilbert@ucdavis.edu, attinger@iastate.edu 
Justification for selecting June-July weather 
Maximum solar radiance is observed in this period of year in the northern hemisphere. Our 
hypothesis was that a crop should be the most productive in this period provided that the plant 
has access to adequate water and nutrients. Due to high solar radiance that results high 
temperature, and generally low relative humidity in drought-prone areas, this period should also 
mimic the highest water demand by the environment from the plant.  
We considered that the typical maize plant was fully grown, i.e. at the beginning of full canopy 
closure, and total yielding period was two months. During this two-month period average solar 
radiation was 489.17 W/m2, relative humidity 45.63%, air temperature was 30.6 0C, and wind 
speed was 3.048 m/s, precipitation does not occur in drought conditions..  The hourly variations 
of weather parameters are in Figure S1.


## Page 39


39 
 
 
Fig. S1 Hourly variation of solar radiation (S), relative humidity (RH), atmospheric temperature 
(Ta), wind speed (Um), precipitation (Precip) and photosynthetically active radiation (PAR) in 
June-July 2010, Davis, CA. 
Hours
Um (m/s)
0
500
1000
0
2
4
6
8
10
Hours
Precip (mm)
0
500
1000
0
0.5
1
1.5
Hours
PAR (W/m
2)
0
500
1000
0
500
1000
1500
2000
Hours
S (kW/m
2)
0
500
1000
0
0.2
0.4
0.6
0.8
1
Hours
RH (%)
0
500
1000
20
40
60
80
Hours
Ta (
oC)
0
500
1000
10
20
30
40
A
B
C
D
E
F


## Page 40


40 
 
 
Figure S2:  Sensitivity analysis of the traits obtained from GA optimization.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1704_05885v1_integrating_optimization_with_thermodynamics_and_plant_physiology_for_crop_ideot
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1704_05885V1_INTEGRATING_OPTIMIZATION_WITH_THERMODYNAMICS_AND_PLANT_PHYSIOLOGY_FOR_CROP_IDEOT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

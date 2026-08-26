---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1801.00383
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1801.00383_Integration_of_Renewable_Power_Sources_into_the_Vietnamese_Power_System

> Source: 1801.00383_Integration_of_Renewable_Power_Sources_into_the_Vietnamese_Power_System.pdf

> Pages: 5

---


## Page 1


Integration of Renewable Power Sources into the
Vietnamese Power System
Alexander Kies∗, Bruno Schyska†, Dinh Thanh Viet‡, Lueder von Bremen†, Detlev Heinemann†,Stefan Schramm∗
∗Frankfurt Institute for Advanced Studies, Goethe University Frankfurt, Ruth-Moufang-Str. 1, 60438 Frankfurt am Main, Germany
† ForWind, Center for Wind Energy Research, University of Oldenburg, Kuepkersweg 70, 26129 Oldenburg, Germany
‡ Department of Electrical Engineering, University of Danang, 41 Le Duan St, Danang, Vietnam
Abstract—The Vietnamese Power system is expected to expand
considerably in upcoming decades. However, pathways towards
higher shares of renewables ought to be investigated. In this work,
we investigate a highly renewable Vietnamese power system by
jointly optimising the expansion of renewable generation facilities
and the transmission grid. We show that in the cost-optimal
case, highest amounts of wind capacities are installed in southern
Vietnam and solar photovoltaics (PV) in central Vietnam. In
addition, we show that transmission has the potential to reduce
levelised cost of electricity by approximately 10%.
I. INTRODUCTION
Power systems are transforming worldwide. The transfor-
mation from conventional dispatchable power generation from
fossil sources towards power generation from the renewable
sources of mainly wind, solar and hydro is driven by goals of
sustainability and reduction of climate gas emissions to mit-
igate climate change. However, renewable power generation
depends on the weather and therefore has strongly ﬂuctuating
feed-in proﬁles which, in turn, make the system integration of
renewables difﬁcult. Among solutions to integrate high shares
of renewable into power systems are: i) optimising the mix of
generation from different renewable sources ([1], [2], [3], [4],
[5], [6]) ii) storage ([7], [8]) iii) dispatchable backup power
([9], [10]) iv) sector coupling ([11], [12]) v) transmission grid
extensions ([13], [14]) vi) controllable hydro power ([15]) vii)
system-friendly renewables ([16], [17]) or viii) demand-side
management ([18], [19]).
In developing countries such as Vietnam, power demand grows
strongly and a reliable energy supply has imminent importance
for stable economic growth and prosperity. The Vietnamese
demand for electricity is growing at an average speed of 7-
8% per year and the peak demand is estimated to reach 42.1
GW by 2020 and 90.7 GW by 2030 ([20]).
At present, Vietnam has exploited mainly thermal and hydro
power resources. Coal as major energy carrier is being im-
ported from abroad. However, the number of thermal power
plants is likely to be limited in the future due to concerns
raised by environmental pollution and dependency on imports.
Therefore, the importance of renewable energy sources such as
wind, solar, tidal, biomass will play an increasingly important
role for Vietnam.
The national energy development vision until 2050, which was
approved by the Vietnamese Prime Minister, emphasises the
role of renewable energy sources in particular. It is expected
that by 2050, 43% of Vietnam’s electricity will be provided
from renewable sources. Expectations about installed wind
power capacity are 800 MW in 2020, 2,000 MW in 2025
and around 6,000 MW by 2030. For solar energy, predicted
numbers of installed capacities are 850 MW by 2020, 4,000
MW by 2025 and 12,000 MW by 2030. In addition, biomass
will contribute about 1% of entire generation by 2020, 1.2%
by 2025 and 2.1% by 2030 ([21]).
In 2014, the Vietnamese electricity production of 145.5 TWh
was mainly supplied by hydro power (38%, not including
small hydro), CCGT (31%) and coal (26%). The dominance of
those three sources was also reﬂected by their shares in overall
installed capacities of 34 GW, comprising hydro (40%, not
including small hydro), gas (22%) and coal (29%). However,
the Vietnamese power development plan predicts total installed
capacities by 2030 of 116 GW with shrinking shares of hydro
(18%) and gas (17%) and growing shares of coal (50%) and
renewables (10%) ([22]).
In this paper, we investigate the optimal mix of renewables
from wind and photovoltaics distributed among the highest
voltage substations of a simplied future Vietnamese power
system.
Similar studies of the power system transition of developing
countries have been performed for a variety of countries such
as Iran ([23]) and also Vietnam ([24]), but in the latter case
with a strong focus on conventional generation technologies
and without including time-dependent renewable resource
availabilities.
II.
METHODOLOGY
We use a simpliﬁed version of the Vietnamese power
system, where loads and generation are connected to the
closest existing highest voltage substation. The topology of the
resulting network is shown in Fig. 1. The model is formulated
as a linear optimisation model that minimises total system cost.
The objective reads
min
g,G,f,F(
X
n,s
cn,sGn,s +
X
l
clFl +
X
n,s,t
on,sgn,s(t)),
(1)
where cn,s is the equivalent investment cost for generation
capacity, cl is the equivalent investment cost for transmission
capacity, on,s is the marginal cost of energy generation, Gn,s
arXiv:1801.00383v1  [physics.soc-ph]  1 Jan 2018


## Page 2


and Fl are the capacities of generators and transmission links
and gn,s is the dispatch time series. The index n runs over all
nodes and s over considered technologies (wind, solar PV and
OCGT).
In addition to the objective, multiple constraints have to be
satisﬁed. To ensure stable power system operation, generation
and demand need to match in space and time:
X
s
gn,s(t) −dn(t) =
X
l
Kn,lfl(t)∀n, t,
(2)
where dn(t) is the demand, K is the incidence matrix of the
network and fl the ﬂow over link l.
The dispatch of a generator gn,s(t) is constrained by the
corresponding generator capacity Gn,s multiplied with the
corresponding hourly capacity factor ¯gn,s(t):
0 ≤gn,s(t) ≤¯gn,s(t)Gn,s∀n, s, t.
(3)
Flows between nodes can not exceed transmission limits,
|fl(t)| ≤Fl∀l, t,
(4)
where Fl denotes the transmission limit of link l (e.g., due to
thermal limits). However, line capacities can be expanded by
the model.
Lastly, in some cases a global CO2 emission constraint is
enforced,
X
n,s,t
1
ηn,s
gn,s(t)en,s ≤CAPCO2,
(5)
where η and e denote the technology speciﬁc efﬁciency and
CO2 emissions. This constraint is varied in the results section
to investigate its inﬂuence on the optimal mix and system cost.
The methodology is described in more detail by Schlacht-
berger et al. ([25]). We use the software toolbox Python for
Power System Analysis (PyPSA, pypsa.org) to perform the
simulations.
The optimisation problem (Eq. 1) is solved for two transmis-
sion grid scenarios. First, with optimised transmission, i.e.,
without a global limit on P
l Fl and with neglible capital
cost for transmission grid capacity expansion. Second, without
transmission, i.e., Fl = 0∀l.
A.
Data and assumptions
The model simulates a full year with hourly resolution. Data
is based on the meteorological year 2012. We use weather data
from the MERRA reanalysis ([26]) to model spatially resolved
generation from the renewable sources of wind and PV. Raw
weather data (wind speeds, irradiation and temperature) are
converted to power as described by Kies et al. ([27]). For wind
power calculations, the power curve of a Vestas V90 at 90 m
hub height is used and wind speeds are extrapolated to the
desired hub height. Capacities within the areas aggregated to
nodes are distributed homogeneously among the single cells.
To obtain irradiation on the tilted modules for PV power
calculations, the Klucher model is applied ([28]).
Cost assumptions for different technologies used to perform
the cost optimisation are shown in Table I.
10°N
20°N
110°E
Transmission lines
Nodes
Fig. 1: Topology of the investigated simpliﬁed Vietnamese
power system. The sizes of the circles indicate the relative
average demand per node.
III.
RESULTS
The optimised generation mix for both transmission sce-
narios is depicted in Fig. 2. With transmission, the major
share of wind generation facilities is installed in the South
and partly the central North, whereas solar PV is installed in
central Vietnam. This comes jointly with a strongly reinforced
transmission grid in southern Vietnam, while the connection
to the northernmost region is comparably weak. In addition,
no renewable resources are installed in the uppermost north,
where capacities are less cost-effective. It should be noted
that OCGT plants are not effected by location-dependent
availability. Consequently, their production capabilities are in-
dependent of their location (with transmission grid restrictions)
and therefore the optimum is ﬂat with respect to the spatial
distribution of OCGT capacities.
Without transmission, the picture changes partially. All nodes
have similar shares of solar PV of 25% to 35%, while the
remaining generation is provided mostly (for some nodes
entirely) by OCGT. Nodes with comparably large wind shares
are still allocated these, thus indicating the resource potentials
being responsible for the installations instead of the topo-
logical position within the network. This is also suggested
by the assumption that transmission costs are almost entirely
neglected, hence rendering transmission grid expansion cheap.
To increase the shares of renewables in the system, the CO2
emission constraint (Eq. 5) is introduced and tightened. The
resulting generation mixes in dependency of the CO2 reduction
relative to the cost-optimal case without constraints are shown


## Page 3


technology
investment cost
marginal cost
lifetime
efﬁciency
CO2 emissions
[USD/kW]
[USD/MWh]
[a]
[tons / MWhthermal]
wind
1300
0.02
20
solar
660
0.03
20
OCGT
440
64.0
30
0.39
0.1872
TABLE I: Cost assumptions for generation technologies based on 2030 value estimates from Schroeder et al. ([29]). For
transmission, plain cost of 0.01 USD/MVA was assumed for each link to ensure uniqueness of the solution.
in Fig. 3 for both transmission scenarios. For OCGT and solar
PV, the picture looks similar in both cases. Shares of solar
PV remain, especially with transmission, roughly constant,
while OCGT is gradually replaced by wind. However, the cost-
optimal share of wind generation is at 38% much larger with
the fully optimised transmission grid than in the case without
transmission (11%). This represents the fact that wind is less
correlated on the spatial scale than PV and therefore beneﬁts
much stronger from a transmission grid ([17]).
Fig. 4 shows levelised cost of electricity (LCOE) in depen-
dency of the CO2 reduction relative to the optimum distribu-
tion without any constraints for both transmission grid scenar-
ios. With optimised transmission, LCOE is at 62 USD/MWh
considerably below marginal cost of dispatchable generation,
thus indicating the high favourability of renewable generation
as well as a signiﬁcant importance of transmission for the
Vietnamese power system. Without transmission, LCOE is at
68 USD/MWh in the optimal case, but costs rise drastically,
if the CO2 constraint is tightened.
IV. CRITICAL APPRAISAL
A number of simpliﬁcations made might effect the conclu-
sions presented in this paper.
In the paper, we have not considered hydro power as part
of the Vietnamese power supply. However, hydro power is
considered fairly well exploited in Vietnam with installed
hydro power capacities expected to grow (according to the
Vietnamese power development plan) from 13.6 GW in 2014
to 20.8 GW in 2030. This compares to an overall growth of
installed capacities from 34 GW to 116 GW. Hence, hydro
power might have the potential to complement the renewable
mix in an extraordinary beneﬁcial way and it is planned to
consider hydro power using an potential energy approach to
calculate energy inﬂow into hydro power storages in future
versions of this work.
Neither hydro nor any other possibility to store energy over
time is incorporated in the presented work. Hence, in future
work medium-scale storage technologies like batteries will be
investigated to quantify their potential impact on the future
Vietnamese power system. However, such storage solutions
are usually not cost-competitive today and it is difﬁcult to
model their future characteristics (cost, efﬁciencies, degrada-
tion in case of battery storage, etc.). In addition, degradation
processes of batteries are highly non-linear.
We have also only considered a single year (meteorological
year 2012) so far. Therefore, results might only represent this
year and not be generalizable to a longer temporal period.
It is planned to address all of the aforementioned deﬁciencies
in future work.
V. SUMMARY, CONCLUSIONS AND OUTLOOK
This paper investigates the integration of large shares of
ﬂuctuating generation from the renewable sources of wind and
photovoltaics into the Vietnamese power system.
It is shown that wind and solar PV can provide more than
two thirds of the overall generation, if the transmission grid
is sufﬁciently strong. However, for even higher shares the
possibility to shift generation in time, i.e., storage, is required.
In many countries around the world, signiﬁcant energy storage
is provided by hydro power and Vietnam already uses a fair
share of hydro power. Therefore, a straightforward extension
of this work is to include hydro power into calculations and to
investigate the question, to what extent existing hydro power
facilities can contribute to the system integration of renewables
in Vietnam.
The transmission grid has the potential to reduce LCOE in a
highly renewable Vietnamese power system by around 10%
caused by the large beneﬁt for wind power that is provided
by the transmission network. The advantage of wind over PV
from transmission can be concluded from the large increase
of wind shares in the optimal solution with vs. without
transmission. To distangle the optimum caused by resources
and by network topology, more investigations towards the cost
sensitivity in case of transmission grid expansion are required.
Together with the fact that renewable generation capacities
were mostly installed in southern Vietnam and that major
demand centres are in southern and northern Vietnam, the
results emphasize the potentials of renewables in Vietnam
together with an expanded transmission grid. This cost-optimal
system has LCOE of approximately 62 USD/MWh. However,
investment and operational costs for the transmission grid are
not included in this number.
This work has highlighted the potentials of ﬂuctuating renew-
able generation from the sources of wind and solar PV in a
future Vietnamese power system. In a forthcoming study, the
methodology and database will be expanded to cover more
meteorological years to reduce the sensitivity towards potential
extreme events in the data, and to include more technologies
such as hydro power, energy storage, etc. In addition, it is
planned increase the spatial detail and also consider existing
ofﬁcial expansion plans of Vietnam’s electricity grid.
ACKNOWLEDGEMENTS
This work is part of the R&D Project Analysis of the
Large Scale Integration of Renewable Power into the Future


## Page 4


Vietnamese Power System ﬁnanced by Gesellschaft fuer Inter-
nationale Zusammenarbeit GmbH (GIZ, 2016-2018). Further-
more, A. Kies is ﬁnancially supported by Stiftung Polytech-
nische Gesellschaft. A slightly different version of this paper
has been published in Energy Procedia ([30]).
REFERENCES
[1] H. Lund. Large-scale integration of optimal combinations of pv, wind
and wave power into the electricity supply. Renewable Energy, (31):503
– 515, (2006).
[2] B Franc¸ois, B Hingray, D Raynaud, M Borga, and JD Creutin. Increas-
ing climate-related-energy penetration by integrating run-of-the river
hydropower to wind/solar mix. Renewable Energy, 87:686–696, (2016).
[3] Alexander Kies, Kabitri Nag, Lder von Bremen, Elke Lorenz, and Detlev
Heinemann. Investigation of balancing effects in long term renewable
energy feed-in with respect to the transmission grid.
Adv. Sci. Res.,
12:91–95, (2015).
[4] FJ Santos-Alamillos, D Pozo-V´azquez, JA Ruiz-Arias, L¨uder Von Bre-
men, and J Tovar-Pescador. Combining wind farms with concentrating
solar plants to provide stable renewable power.
Renewable Energy,
76:539–550, (2015).
[5] Alexander Kies, Bruno U Schyska, and Lueder von Bremen. The optimal
share of wave power in a highly renewable power system on the iberian
peninsula. Energy Reports, 2:221–228, (2016).
[6] Jakub Jurasz. Modeling and forecasting energy ﬂow between national
power grid and a solar–wind–pumped-hydroelectricity (pv–wt–psh) en-
ergy source. Energy Conversion and Management, 136:382–394, (2017).
[7] Dominik Heide, Martin Greiner, Lueder Von Bremen, and Clemens
Hoffmann. Reduced storage and balancing needs in a fully renewable
european power system with excess wind and solar power generation.
Renewable Energy, 36(9):2515–2523, (2011).
[8] Kabitri Chattopadhyay, Alexander Kies, Elke Lorenz, L¨uder von Bre-
men, and Detlev Heinemann.
The impact of different pv module
conﬁgurations on storage and additional balancing needs for a fully
renewable european power system. Renewable Energy, 113:176–189,
(2017).
[9] DP Schlachtberger, S Becker, S Schramm, and Martin Greiner. Backup
ﬂexibility classes in emerging large-scale renewable electricity systems.
Energy Conversion and Management, 125:336–346, (2016).
[10] Guido Pleßmann, Matthias Erdmann, Markus Hlusiak, and Christian
Breyer. Global energy storage demand for a 100% renewable electricity
supply. Energy Procedia, 46:22–31, (2014).
[11] Tom Brown, David Schlachtberger, Alexander Kies, and Martin Greiner.
Sector coupling in a highly renewable european energy system. In 15th
Wind Integration Workshop, (2017).
[12] Katrin Schaber, Florian Steinke, and Thomas Hamacher.
Managing
temporary oversupply from renewables efﬁciently: Electricity storage
versus energy sector coupling in germany.
In International Energy
Workshop, Paris, (2013).
[13] Tom Brown. Transmission network loading in europe with high shares
of renewables. IET Renewable Power Generation, 9(1):57–65, (2014).
[14] Sarah Becker, Rolando A Rodriguez, Gorm B Andresen, Stefan
Schramm, and Martin Greiner. Transmission grid extensions during the
build-up of a fully renewable pan-european electricity supply. Energy,
64:404–418, (2014).
[15] Alexander Kies, Bruno U Schyska, and Lueder von Bremen.
The
effect of hydro power on the optimal distribution of wind and solar
generation facilities in a simpliﬁed highly renewable european power
system. Energy Procedia, 97:149–155, (2016).
[16] Lion Hirth and Simon M¨uller.
System-friendly wind power: How
advanced wind turbine design can increase the economic value of
electricity generated through wind power. Energy Economics, 56:51–
63, (2016).
[17] A Kies, BU Schyska, and L von Bremen.
Curtailment in a highly
renewable power system and its effect on capacity factors. Energies,
9(7):510, (2016).
[18] Peter Palensky and Dietmar Dietrich.
Demand side management:
Demand response, intelligent energy systems, and smart loads. IEEE
transactions on industrial informatics, 7(3):381–388, (2011).
[19] Alexander Kies, Bruno U Schyska, and Lueder von Bremen.
The
demand side management potential to balance a highly renewable
european power system. Energies, 9(11):955, (2016).
[20] Aruna K Wanniachchi and et al. Vietnam - energy sector assessment,
strategy and roadmap.
Technical report, Asian Development Bank
(ADB), Manila, Philippines, 12 (2015).
[21] Vietnam’s power development plan vii (pdp 7 revised).
Technical
report, Decision No 428/QD-TTg of Vietnam’s Prime Minister, Hanoi,
Vietnam,, (2016).
[22] Long Thang Nguyen. Regulatory frameworks, market cultivation and
outlook for wind energy in vietnam, (2015).
[23] Arman Aghahosseini, Dmitrii Bogdanov, Narges Ghorbani, and Chris-
tian Breyer.
The role of a 100% renewable energy system for the
future of iran: Integrating solar pv, wind energy, hydropower and storage.
(2016).
[24] Quoc Khanh Nguyen.
Long term optimization of energy supply and
demand in Vietnam with special reference to the potential of renewable
energy. PhD thesis, Universit¨at Oldenburg, (2005).
[25] David P Schlachtberger, Tom Brown, Stefan Schramm, and Martin
Greiner. The beneﬁts of cooperation in a highly renewable european
electricity network. arXiv preprint arXiv:1704.05492, (2017).
[26] Michele M Rienecker, Max J Suarez, Ronald Gelaro, Ricardo Todling,
Julio Bacmeister, Emily Liu, Michael G Bosilovich, Siegfried D Schu-
bert, Lawrence Takacs, Gi-Kong Kim, et al. Merra: Nasa’s modern-era
retrospective analysis for research and applications. Journal of Climate,
24(14):3624–3648, (2011).
[27] Alexander Kies, Kabitri Chattopadhyay, Lueder von Bremen, Elke
Lorenz, and Detlev Heinemann. Restore 2050: Simulation of renewable
feed-in for power system studies.
Technical report, University of
Oldenburg, (2016).
[28] Thomas M Klucher. Evaluation of models to predict insolation on tilted
surfaces. Solar energy, 23(2):111–114, (1979).
[29] Andreas Schroeder, F Kunz, R Mendelevitsch, and Christian von
Hirschhausen. Current and prospective costs of electricity generation.
In Energy Economics of Phasing out Carbon and Uranium, 13th IAEE
European Conference, August 18-21, 2013. International Association for
Energy Economics, (2013).
[30] Alexander Kies, Bruno Schyska, Dinh Thanh Viet, Lueder von Bremen,
Detlev Heinemann, and Stefan Schramm.
Large scale integration of
renewable power sources into the vietnamese power system.
Energy
Procedia, 125:207–213, 2017.


## Page 5


Generation distribution
(a) With optimised transmission
Generation distribution
(b) Without transmission
Fig. 2: Cost-optimal distribution and mix of generation. The
colors indicate the shares of OCGT (red), wind (blue) and
solar PV (green) and the sizes of the dots indicate overall
generation. Widths of transmission links indicate capacity of
transmission link.
0.0
0.95
CO2 reduction relative to optimum
0.0
0.2
0.4
0.6
0.8
1.0
Share
Optimal Mix
Wind
PV
OCGT
(a) With optimised transmission
0.0
0.95
CO2 reduction relative to optimum
0.0
0.2
0.4
0.6
0.8
1.0
Share
Optimal Mix
Wind
PV
OCGT
(b) Without transmission
Fig. 3:
Optimal generation mix in dependency of the CO2
reduction relative to the cost-optimum without any constraints.
0.0
0.2
0.4
0.6
0.8
CO2 reduction relative to optimum
0
25
50
75
100
125
150
175
200
LCOE [USD/MWh]
transmission
no transmission
Fig. 4: Levelised cost of electricity in dependency of the CO2
reduction relative to the cost-optimum without any constraints
with and without transmission grid.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1706.05121v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1706.05121v1_Community_interactions_determine_role_of_species_in_parasite_spread_amplificatio

> Source: 1706.05121v1_Community_interactions_determine_role_of_species_in_parasite_spread_amplificatio.pdf

> Pages: 11

---


## Page 1


Community interactions determine role of species in parasite spread
ampliﬁcation: the ecomultiplex network model
Massimo Stella
Institute for Complex Systems Simulation, University of Southampton, UK
Sanja Selakovic
Faculty of Geosciences, Utrecht University, The Netherlands
Alberto Antonioni
Institute for BioComputation and Physics of Complex Systems, University of Zaragoza, Spain and
Grupo Interdisciplinar de Sistemas Complejos,
Departamento de Matematicas, Universidad Carlos III de Madrid, Spain
Cecilia S. Andreazzi
Campus Fiocruz, Fundação Oswaldo Cruz, Brazil∗
Most of zoonoses are multi-host parasites with multiple transmission routes that are usually inves-
tigated separately despite their potential interplay. As a unifying framework for modelling parasite
spread through diﬀerent paths of infection, we suggest "ecomultiplex" networks, i.e.
multiplex
networks representing interacting animal communities with (i) spatial structure and (ii) metabolic
scaling. We exploit this ecological framework for testing potential control strategies for T. cruzii
spread in two real-world ecosystems. Our investigation highlights two interesting results. Firstly,
the ecomultiplex topology can be as eﬃcient as more data-demanding epidemiological measures in
identifying which species facilitate parasite spread. Secondly, the interplay between predator-prey
and host-parasite interactions leads to a phenomenon of parasite ampliﬁcation in which top preda-
tors facilitate T. cruzii spread, oﬀering theoretical interpretation of previous empirical ﬁndings. Our
approach is broadly applicable and could provide novel insights in designing immunisation strategies
for pathogens with multiple transmission routes in real-world ecosystems.
Zoonoses are infections naturally transmitted
between animals and humans, and are the most
important cause of emerging and re-emerging
diseases in humans [24, 30, 38]. The majority of
the zoonotic agents are multi-host pathogens or
parasites [1, 35], whose various host species may
diﬀer in their contribution to parasite trans-
mission and persistence over space and time
[21, 46]. This heterogeneity of host species con-
tribution to parasite transmission is related to
diﬀerences in host species’ abundance, exposure
and susceptibility to infection [2, 17, 51]. Fur-
ther, many multi-host parasites have complex
life cycles with multiple transmission modes,
such as vertical, direct contact, sexual, aerosol,
vector-borne and/or food-borne [52].
Among the zoonotic parasites with mul-
tiple
hosts
and
transmission
modes,
Try-
panosoma cruzi (Kinetoplastida:
Trypanoso-
matidae), which causes Chagas disease in hu-
mans, has complex ecology that challenges
transmission modelling and disease control [21,
34]. T. cruzi has already been found in more
than 100 mammalian species and its transmis-
sion may be mediated by several interdepen-
dent mechanisms [21, 34].
For instance, T.
cruzi has a contaminative route of transmis-
sion that is mediated by invertebrate vectors
∗Corresponding author: candreazzi@ﬁocruz.br
(Triatominae, eng. kissing bug); and a trophic
route of transmission that cascades along the
food-web when a susceptible predator feeds on
infected prey [21, 34].
Chemical insecticides and housing improve-
ment have been the main strategies for control-
ling Chagas disease in rural and urban areas
of Latin America [12]. However, these strate-
gies are proving to be ineﬃcient [44]. This is
possibly related to the maintenance and trans-
mission of parasites among local wild mam-
malian hosts and its association with sylvatic
triatomine vectors [44, 45].
Therefore, mod-
elling parasite transmission in a way that is ex-
plicitly considering the ecology of wildlife trans-
mission, is fundamental to understanding and
predicting outbreaks.
In this work we propose to address this chal-
lenge through the mathematical framework of
multiplex networks [4, 5, 10, 11, 27], which are
already recognised as a powerful tool in epi-
demiology [10, 29, 48] and ecology [25, 26, 39,
50].
Multiplex networks are multi-layer net-
works where multi-relational interactions give
rise to a collection of network layers so that
the same node can engage in diﬀerent inter-
actions with diﬀerent neighbours in each layer
[5, 11, 27].
We study the ecology of multi-host parasite
spread by multiple routes of transmission and
potential control strategies by developing the
arXiv:1706.05121v1  [q-bio.QM]  16 Jun 2017


## Page 2


2
"ecomultiplex" framework (short for ecological
multiplex framework). This framework is inno-
vative because: (i) it accounts for multiple in-
teraction types, reconciling food web structure
and parasitic interactions from epidemiological
contacts, (ii) it uses metabolic theory [22] for es-
timating species frequencies, which are known
to inﬂuence parasite transmission [31], and (iii)
it considers large-scale realistic spatial struc-
ture of wildlife communities [20].
We develop a general model, that could in-
clude any ecological interaction among any set
of species in real-world ecosystems through
ecological multiplex networks. We apply this
"ecomultiplex" formalism in investigating par-
asite spread in two host communities in Brazil:
Canastra [43] and Pantanal [18].
We exploit
the theoretical framework enriched with empir-
ical data for designing and comparing diﬀerent
wild host immunisation strategies based on: (i)
main biological taxonomic groups (e.g. immu-
nising species of a family); (ii) species interac-
tion patterns (e.g. immunising species feeding
on the vector); and (iii) species’ epidemiolog-
ical role (e.g. immunising species with higher
parasite prevalence). Multiplex network topol-
ogy proves as powerful as epidemiological ﬁeld
work measurements in predicting the species fa-
cilitating parasite spread in both tested ecosys-
tems.
More importantly, considering multi-
ple transmission mechanisms conﬁrms the com-
plexity science motto "more is diﬀerent": on
the 2-layers multiplex structure we detect an-
other mechanism for which top predators can
indeed facilitate parasite transmission.
Our
quantitative results challenge the mainstream
idea of predators regulating and containing par-
asite spread in ecosystems [53].
I.
MATERIAL AND METHODS
A.
Ecological multiplex network model
The "ecomultiplex" model describes an eco-
logical community interacting in a spatially ex-
plicit ecosystem (Fig.
1).
Each layer of the
ecomultiplex represents a diﬀerent type of in-
teraction between species groups that can po-
tentially lead to parasite transmission. We con-
sider (i) food-web and (ii) contaminative inter-
actions. These interactions give rise to an eco-
multiplex network of two layers. Links on the
food-web layer are directed to predator species
and represent predator-prey interactions. Links
on the vectorial layer are undirected and rep-
resent vector blood meals of parasitic insects
acting as parasite vectors. Nodes represent set
of individuals from a given species, i.e.
ani-
mal groups. Distance among animal groups de-
termines possible interactions: only geographi-
cally close groups can interact with each other.
We ﬁxed the home range of all animal groups as
a circle of radius r = 0.03 over a square of size
one and studied a total of N = 10000 animal
groups, cf. Stella et al. [50].
B.
Ecological data: trophic interactions
and body masses
Predator-prey and vector-host interactions in
the ecomultiplex network are based on ecolog-
ical data related to T. cruzi infection in wild
hosts within two diﬀerent areas: Canastra, a
tropical savannah in Eastern Brazil [43] and
Pantanal, a vast ﬂoodplain in Southern Brazil
[18]. Both biomes are highly diverse environ-
ments where pandemics of T. cruzi have been
registered [18].
Trophic interactions in the food web are as-
signed according to literature data about ani-
mals’ diets [7, 8, 32, 40–42, 47] (cf. SI Sect. 1).
All vector species are grouped as one functional
group due to missing species-level classiﬁcation.
Species prevalence is used to estimate the con-
taminative interactions in the vectorial layer
[18, 43]. Positive parasitological diagnostics for
T. cruzi (hemoculture) are used as a proxy for
connections on the vectorial layer, since only in-
dividuals with positive parasitaemia (i.e. with
high parasite loads in their blood) are able to
transmit the parasite [21]. Body masses of host
species represent averages over several available
references [6, 18, 33, 41, 49].
D.
Metrics for multiplex network analysis
We investigate the structure of a given eco-
multiplex network through the concept of mul-
tiplex network cartography [3] (cf. SI Sect. 3).
Multiplex cartography provides a map of the
centralities of nodes/animal groups in the eco-
multiplex network and it is based on two "coor-
dinates". One is the total number of trophic in-
teractions an animal group is involved in (mul-
tidegree [3, 11]). The higher the multidegree,
the more an animal group interacts with other
groups. The second coordinate is the ratio of
uniform link distribution across layers (partici-
pation coeﬃcient [3]), ranging between 0 (when
all links of a node are focused in one layer only)
and 1 (when all links of a node are uniformly
distributed across layers). The higher the par-
ticipation coeﬃcient the more an animal group
will engage in feeding and contaminative inter-
actions in equal measure (see SI for more de-
tails).


## Page 3


3
Food Web Layer 
Vectorial Layer 
Spatially Embedded Ecosystem 
x 
y 
O 
Figure 1. Visual representation of our ecological multiplex model. Animal groups are embedded in space
and can interact only if they are close enough.
Interactions are either predator-prey relationships or
host-parasitoid interactions.
C.
Mathematical formulation for group frequencies
Geographical proximity and ecological data regulate link creation in the ecomultiplex model.
Ecological data, in particular body masses, regulate the frequency of animal groups.
Previous literature Jetz et al. [22] showed that the density n−1
i
of individuals of body mass mi
within a home range follows the metabolic scaling:
n−1
i
= β−1R−1
i m3/4
i
(1)
when Ri is the species-speciﬁc energy supply rate, i.e. the energy resources available to sustain
the animal group in a given area and unit of time and β a normalisation constant expressing
species metabolism. Empirical work has shown that Ri is independent on body mass [22].
Assuming metabolic theory provides a good approximation for species densities, the above
equation can be used for determining the scaling relationship between body mass mi and
frequency fi of animal groups for species i, depending on vector frequency fv (cf. SI Sect.2):
fi = (1 −fv)
m−1/4
i
P
j=1 m−1/4
j
.
(2)
The above scaling relationship assumes that a fraction of the energy acquired by individual
animals gets transformed into body mass at the global population level, i.e. when all individuals
of a species are considered. This global constraint leads to frequencies of animal groups scaling
as a power-law with exponent −1/4, which is diﬀerent from the coeﬃcient −3/4, which always
comes from metabolic theory but refers to individuals rather than groups.
E.
SI Model on the Ecological multiplex
Network
Parasite spread is simulated as a Susceptible-
Infected (SI) process on the ecomultiplex struc-
ture.
We assume that parasite transmission
among animal groups happens considerably
faster than both (i) group creation or extinction
and (ii) parasite transmission within groups,
so that meta-populations dynamics can be ne-
glected.
At each time step, the parasite can
spread from an infected group to another one
along a connection either in the vectorial (with
probability p) or food-web (with probability


## Page 4


4
Immunisation Type
Strategy Name
Strategy Targets
Ecomultiplex Topological Features
Insectivores
Species feeding on the vector in a food-web
Parasitised
Didelphidae
Didelphidae contaminated by the vector on a
vectorial layer
Parasitised
Mammals
All species contaminated by the vector on a
vectorial layer
Biological Features Only
All Cricetidae
All Cricetidae
All Didelphidae All Didelphidae
Large Mammals All species with a body mass > 1 kg
Epidemiological Features
Hemoculture N
The N species with the highest likelihood of
being found infected with the parasite in ﬁeld
work (see SI).
Serology N
The N species with the highest likelihood of
having been infected with the parasite during
their life time (see SI).
Table I. Immunisation types, names and targets of the strategies we tested (cf. SI).
1 −p) layer. We consider p as a model free pa-
rameter called vectorial layer importance, i.e.
the rate at which transmission occurs through
the consumption of blood by vectors rather
than predator-prey feeding interactions.
We
characterise the SI dynamics at a global scale by
deﬁning a global infection time t∗as the earliest
time at which the parasite reaches its maximum
spread within the networked ecosystem [50].
F.
Immunisation Strategies
Immunisation strategies provide information
on how species inﬂuence the parasite spread at
a global level: immunising species that facili-
tate parasite spread, the global infection time t∗
is expected to increase compared to immunising
random species. We focus on immunising only1
10% of animal groups in ecomultiplex networks
with 10000 nodes, in either high (fv = 0.25) or
low vector frequency scenarios (fv = 0.1). Im-
munised groups are selected according to three
categories of host immunisation strategies fo-
cusing on (see also Table 1):
• Biological features:
main taxonomic
groups or body mass;
• Ecomultiplex network features: in-
teraction patterns on the ecomultiplex
structure;
1 By immunising groups at random in ecomultiplex net-
works with N = 10000 nodes, we identiﬁed φ = 1000
as the minimum number of groups/nodes that have
to be immunised in order to observe increases in in-
fection times compared to the case of random im-
munisation with a signiﬁcance level of 5% (sign test,
p-value< 0.01).
• Epidemiological features:
epidemio-
logical measures of parasite prevalence in
wildlife.
We deﬁne the infection time increase ∆ti as
the normalised diﬀerence between the median
infection time ts when φ = 1000 nodes are im-
munised according to the strategy s and the
median infection time tr when the same num-
ber of nodes is immunised uniformly at random
among all mammal groups, ∆ti = ti−tr
tr
. Infec-
tion times are averages sampled from 500 sim-
ulated replicates. Diﬀerences are always tested
at 95% conﬁdence level.
Positive increases imply that the immunisa-
tion strategy slowed down the parasite in reach-
ing its maximum spread over the whole ecosys-
tem more than random immunisation. Nega-
tive increases imply that random immunisation
performs better than the given immunisation
strategy in hampering parasite diﬀusion.
II.
RESULTS
Ecomultiplex structure demonstrates high ef-
ﬁciency in designing strategies for slowing down
parasite spread in both Canastra and Pan-
tanal.
Immunisation experiments also high-
light a mechanism where top predators facil-
itate parasite spread, challenging the main-
stream idea of predators containing parasite dif-
fusion [16, 36, 53].
A.
Network Analysis
Multiplex cartography for both Canastra and
Pantanal (Fig. 1) shows that vectors are: (i)


## Page 5


5
more connected and (ii) distribute their links
more equally across the ecomultiplex layers
than other species. Hence, vectors can get in-
fected in one layer, spread the parasite on an-
other layer with equal likelihood and poten-
tially infect many species: vectors can indeed
facilitate parasite spread through their inter-
actions.
The local network structure around
vectors in Canastra and Pantanal (cf.
Fig.
2) shows that vector groups are in the cen-
tre of star-like topologies on both network lay-
ers. These topological results conﬁrm that Tri-
atoma species promote parasite spread. In fact,
control strategies for hampering parasite diﬀu-
sion can focus on vector removal from the en-
vironment [54]. However, these strategies are
not stable as vector reintroduction can happen
shortly after elimination [14]. Hence, we focus
on immunisation strategies considering vectors’
importance but immunising other species in the
ecomultiplex network.
B.
Immunisation Strategies
As expected, immunising species with the
highest likelihood of being found infected (an
epidemiological strategy) is the best strategy
for hampering parasite spread for both Canas-
tra and Pantanal in both vector frequencies sce-
narios Fig.
4.
The epidemiological strategy
slows down parasite spread by almost 30% in
Canastra and 26% in Pantanal when the para-
site spreads mainly on the food-web layer (pv =
0.1) Fig.
4.
Immunising species interacting
with vectors on the vectorial layer (an ecomul-
tiplex strategy) also performs better than ran-
dom. The diﬀerence between the epidemiologi-
cal and the ecomultiplex strategies is present
only at low vector frequencies (fv = 0.1) in
both Canastra (Fig.
4A) and Pantanal (Fig.
4C) but vanishes when fv = 0.25 and pv > 0.2
(Fig. 4B,D).
In Canastra, when 10% of the animal groups
are vector colonies (Fig.
4A), biological im-
munisation strategies are equivalent to immu-
nising species at random.
The performance
of biological immunisation changes dramati-
cally when vector colonies become more fre-
quent (Fig.
4B). Immunising large mammals
decreases by 12% the global infection time when
p = 0.1:
immunising large mammals boosts
parasite spread compared to random immuni-
sation. This suggests that large mammals are
not the ones facilitating parasite transmission
in the model. Immunising all the Didelphidae
species leads to similar results (Fig. 4B). Mod-
est increases in infection time are reported for
immunising Cricetidae species when pv = 0.2
(Fig. 4B). Immunising species feeding on the
vector (Insectivores) is equivalent to random
immunisation (sign Test, p-values> 0.1).
In Pantanal, immunising parasitised mam-
mals, parasitised Didelphidae and species with
the highest parasite prevalence (hemoculture)
are at least two times more eﬀective in slowing
down parasite spread compared to other strate-
gies (Fig. 4C-4D). contrary to what happens
in Canastra, when fv = 0.1 and the parasite
spreads mainly on the food web (p ≤0.2), im-
munising parasitised Didelphidae hampers par-
asite diﬀusion more than immunising all par-
asitised mammals (Sign Test, p-value< 0.01)
(Fig.
4C). Immunising insectivores or large
mammals is equivalent to random immunisa-
tion (Fig. 4C). Immunising Cricetidae species
always performs worse than random immunisa-
tion (Fig. 4C,D).
C.
Top predators can lead to parasite
ampliﬁcation
In Canastra, the strategy Hemoculture 3 con-
sists of immunising also one species of top
predator, the Leopardus pardalis (ocelot) (see
SI). We compare the performances of Hemocul-
ture 3 against another immunisation strategy
where instead of the ocelot we immunise an-
other top predator, the Chrysocyon brachyurus
(maned wolf), which had negative prevalence
in this area [43]. In general, top predators are
related to parasite transmission control in nat-
ural environments [53] so we do not expect dif-
ferences.
Instead, results from Fig.
5A indicate a
drastic increase of global infection time when
a predator with positive parasite prevalence is
immunised. This indicates that in Canastra the
Leopardus pardalis (ocelot) has an ampliﬁcation
eﬀect in spreading the parasite (Fig. 5B). This
phenomenon crucially depends on epidemiolog-
ical importance, as discussed in the following
section.
III.
DISCUSSION
We present a novel theoretical framework for
modelling transmission of multiple-host para-
site by multiple routes in real-world ecosystems.
We identify three key points related to para-
site spread on ecomultiplex networks.
First,
we show that topological information oﬀers in-
sights on which host species facilitate parasite
spread.
Second, we use such topological in-
formation for designing immunisation strate-
gies for transmission control at diﬀerent vector
abundances. Third, we identify that top preda-
tors interaction patterns aﬀect their functional
role in parasite transmission, potentially ampli-
fying the parasite spread.


## Page 6


6
C. brachyurus
L. pardalis
C. thous
L. vetulus
C. semistriatus
D. albiventris
L. crassicaudata
C. philander
N. squamipes
Monodelphis spp
M. incanus
O. delator
C. subﬂavus
N. lasiurus
A. montensis
Akodon spp
G. agilis
Oligoryzomys spp
Calomys spp 
C. brachyurus
L. pardalis
C. thous
L. vetulus
C. semistriatus
D. albiventris
L. crassicaudata
C. philander
N. squamipes
Monodelphis spp
M. incanus
O. delator
C. subﬂavus
N. lasiurus
A. montensis
Akodon spp
G. agilis
Oligoryzomys spp
Calomys spp 
Canastra trophic interactions
Canastra vectorial interactions
(a)
C. brachyurus
L. pardalis
C. thous
L. vetulus
C. semistriatus
D. albiventris
L. crassicaudata
C. philander
N . squamip
Monode
M. incanus
O. delator
C. subﬂavus
N. lasiurus
A. montensis
Akodon spp
G. agilis
Oligoryzomys spp
Calomys spp 
C.
brachyurus
L. pardalis
C. thous
L. vetulus
C.
semistriatus
D. albiventris
L. crassicaudata
C. philander
N. squamipes
Monodelphis spp
M. incan
O. delator
C. subﬂavus
N. lasiurus
A. montensis
Akodon spp
G. agilis
Oligoryzomys spp
Calomys spp 
(b)       Pantanal trophic interactions
Pantanal vectorial interactions
L. pardalis
C. thous
N. nasua
S. scrofa
P. tajacu
H. hydrochaeris
T. pecari
E. sexcinctus
P. frenatus
T. pachyurus C. laticeps
H. brasiliensis
C. scotti
M. domestica
O. mamorae
T. macrurus
C. callosus
G. agilis
L. pardalis
C. thous
N. nasua
S. scrofa
P. tajacu
H. hydrochaeris
T. pecari
E. sexcinctus
P. frenatus
T. pachyurus C. laticeps
H. brasiliensis
C. scotti
M. domestica
O. mamorae
T. macrurus
C. callosus
G. agilis
Figure 2. Neighbourhood topology of vectors within the Canastra ecosystem on the trophic layer (left)
and contaminative layer (right). Predators are highlighted in blue, prey in orange and vectors in green.
Interactions involving the insect are highlighted in red. Interactions involving other species are reported
for completeness in blue. Vectors are the most highly connected species on the whole multiplex structure:
they have the highest outdegree on the trophic layer and the highest degree on the contaminative layer.
Furthermore, vectors have the most overlapping connections across the two layers.
These ﬁndings are
reﬂected in the multiplex cartography.
Network structure is eﬃcient in designing im-
munisation strategies which perform success-
fully as epidemiological strategies at higher vec-
tor abundances. Ecomultiplex strategies always
outperform biological strategies which neglect
species’ topology.
This quantitative evidence
suggests the importance of including trophic in-
teractions in case of T. cruzii spread [9, 23, 37].
Although Pantanal and Canastra diﬀer in di-
versity of species and their interactions, immu-
nising species exposed to parasitic interactions
proves eﬃcient in both ecosystems. This un-
derlines the importance of access to the vecto-
rial layer for boosting parasite spread also in
the food web. Since the vectorial layer contains
only parasitic interactions, our analysis agrees
with previous studies [13, 28] which underlined
the importance of considering the interplay be-
tween parasite-host and predator-prey interac-
tions. The ecomultiplex model represents an at-
tempt along the research direction of investigat-
ing ecosystems with multiple routes of pathogen
transmission [14].
The ecomultiplex model provides insights
on how individual species inﬂuence parasite
spreading. In Pantanal, immunising only para-


## Page 7


7
●■
■
■
■■■■■■■■■■■■
■
■
◆▲▼○□
◇
◇◇◇◇
◇◇
△▽●
●●●
●●●●●●●●●
■◆
◆◆◆◆
◆
◆◆◆◆◆◆◆◆◆
▲▼
▼▼▼▼▼
▼
▼▼▼▼▼▼▼▼▼
○
○○○○○
○○○○○○○○○○
□◇△
△△△△
△△△△△△△△△△
▽▽▽▽▽▽▽▽▽▽▽▽
0.0
0.2
0.4
0.6
0.8
1.0
0
20
40
60
80
Ratio U of Uniform Link Distribution
Across Layers
Total Degree Across Layers K
(a)  
 
 
      Canastra
                     Vector Frequency = 0.1
Nodes in a 2D Bin
0
200
400
600
800
1000
●
■
■
■■
■■■■■■■■■■■■■
◆▲▼○□
◇◇◇
◇
△▽
●
●
●●●●●●
■
◆
◆
◆◆◆◆◆◆◆◆
▲
▼▼▼
▼
▼▼
▼▼▼▼▼▼▼
○
○
○
○○○○○○
□◇
△△
△
△△△△△△△△△△
▽▽▽▽
▽▽▽▽▽▽▽▽▽▽▽▽
0.0
0.2
0.4
0.6
0.8
1.0
0
20
40
60
80
Ratio U of Uniform Link Distribution
Across Layers
Total Degree Across Layers K
(b)                      Canastra
                   Vector Frequency = 0.25
Nodes in a 2D Bin
0
200
400
600
●■◆
◆
◆◆
◆◆◆◆◆◆◆◆◆
◆
◆
▲
▼○□◇
◇
◇◇◇◇◇◇◇◇◇
△
△
△△
△△△△△△△△△△△△
△
▽
▽▽
▽▽▽▽▽▽▽▽▽
●
●
●
●●●●●●●●●
■
◆▲
▲▲▲▲
▲
▲▲▲▲▲▲▲▲▲
▼
▼▼
▼
▼▼▼▼▼▼▼▼▼
○□◇
◇◇◇
◇
◇◇◇◇◇◇◇◇◇
△△
△△△△
0.0
0.2
0.4
0.6
0.8
1.0
0
20
40
60
80
Ratio U of Uniform Link Distribution
Across Layers
Total Degree Across Layers K
(c)                       Pantanal
                    Vector Frequency = 0.1
Nodes in a 2D Bin
0
200
400
600
800
●
■
◆◆◆◆◆◆◆◆◆◆◆◆◆
▲
▼
○
□
◇
◇◇
◇◇
◇◇
△
△△
△△△△△△△△△△△△
▽
▽▽▽▽
●
●●●●
●●
■
◆
▲
▲▲▲▲▲▲▲▲▲
▼
▼
▼
▼▼▼▼▼▼
○□
◇
◇
◇
◇◇◇◇
◇◇
△
△△△△△△△
0.0
0.2
0.4
0.6
0.8
1.0
0
20
40
60
80
Ratio U of Uniform Link Distribution
Across Layers
Total Degree Across Layers K
(d)                       Pantanal
                   Vector Frequency = 0.25
Nodes in a 2D Bin
0
100
200
300
400
500
600
Figure 3. Cartography of the ecomultiplex network for the Canastra ecosystem with 10% (top left) and
25% (top right) of total groups as vectors. Cartography of the ecomultiplex network for the Pantanal
ecosystem with 10% (bottom left) and 25% (bottom right) of total groups as vectors. The cartography is
presented as a heat map (grey background tiles) and it distinguishes the average trends of species: blue for
predators, orange for prey, and green for vectors. Vectors have higher total degree in the ecosystem and
tend to distribute more equally their links across both the multiplex layers than all other species. Vectors
are therefore pivotal in the ecosystem.
sitised Didelphidae slows down parasite spread
more than immunising all parasitised mam-
mals. This ﬁnding is in agreement with previ-
ous works identifying Didelphidae as reservoirs
for the T. cruzii [19, 34], and thus of major im-
portance for facilitating parasite transmission.
Notice that our approach identiﬁes Didelphi-
dae as facilitators simply by means of topolog-
ical interactions, conﬁrming the importance of
the ecomultiplex structure in modelling para-
site diﬀusion.
As expected, immunisation strategies based
on epidemiological measures are the most eﬀec-
tive for control of parasite transmission. How-
ever, these strategies require intensive measure-
ments of parasite prevalence across host com-
munities.
Instead, ecomultiplex strategies re-
quire less data, since building the network re-
quires ﬁnding just positive parasitaemia.
We
show that ecomultiplex strategies slow down
parasite spread as much as epidemiological
strategies when parasite abundance is high in
both Canastra and Pantanal. This shows that
ecomultiplex network information is as power-
ful as epidemiological measurements for gaining
insights in the dynamics of parasite diﬀusion.
Within food webs, top predators are gener-
ally considered playing a regulating role in par-
asite spread by preying on infected individuals
and eliminating additional sources of infection
for other animals [16, 36, 53].
Our ecomul-
tiplex network shows that predators can also
facilitate rather than just slow down parasite
spread depending on their epidemiological in-
teractions with vectors.
An example is the
ocelot in Canastra. As reported in Fig. 5 (b),
ocelots are top predators, feed on more prey
than other species and have an increased like-


## Page 8


8
Figure 4. Immunisation strategies for the Canastra (top) and Pantanal (bottom) ecosystems when the
vector frequency is 0.1 (left) and 0.25 (right).
lihood of becoming infected with the parasite
on the food-web layer. Once infected, ocelots
can also transmit the parasite to vectors on the
vectorial layer. Since vectors themselves facili-
tate parasite spread, then top predators para-
sitised by vectors can indeed amplify parasite
diﬀusion. This phenomenon of parasite ampli-
ﬁcation emerges only when both ecomultiplex
layers are considered together. Therefore, this
mechanism remarks the importance of unifying
ecological and epidemiological approaches for
better modelling of multi-host parasite trans-
mission. Interestingly, the ampliﬁcation mech-
anism would support previous remarks of ocelot
being deeply related with the transmission of T.
cruzii in wildlife [42, 43].
Our
theoretical
model
allows
to
design
and test immunisation strategies in real-world
ecosystems by relying on speciﬁc assumptions.
For instance, since animal groups are embed-
ded in space, home ranges need to be speciﬁed
for them. For the sake of simplicity, in this eco-
logical version of the model we considered only
one average interaction radius for all species.
Considering species-dependent empirical radii
(home ranges) represents a challenging yet in-
teresting generalisation for future work.
Notice that we consider the same parasite
transmission probability across species in the SI
dynamics.
This is because species-dependent
transmission rates in our model are encap-
sulated within:
(i) structure of interactions
and (ii) diﬀerent frequencies of animal groups.
These two elements play a role equivalent to
considering diﬀerent transmission rates. In pre-
vious work [50], we quantitatively conﬁrmed
that considering these two elements in mean-
ﬁeld SI models was suﬃcient for species to dis-
play diﬀerent probabilities of catching the para-
site. Here, immunisation strategies conﬁrm this
ﬁnding: immunising species that are more ex-
posed to parasites leads to better immunisation
performances compared to random immunisa-
tion. Considering species-dependent transmis-
sion rates as encapsulated in frequencies and
network links reduces the number of model pa-
rameters.
We assume that parasite spread is happening


## Page 9


9
!
Food Web 
Layer 
 
Vectorial 
Layer 
 
1. Predators get the parasite from infected prey; 
2. Predators transmit the parasite to vectors. 
Top predators can facilitate parasite spread on ecomultiplex networks 


















0
0.2
0.4
0.6
0.8
-0.1
0
0.1
0.2
0.3
Vectorial Layer Importance
Infection Time Increase
CANASTRA
Vector Frequency = 0.1
⊙  Hemoculture – Highest 3 
      (Leopardus, Marmosops, Cerradomys) 
 
⊕  Alternative Immunisation Strategy 
      (Chrysocyon, Marmosops, Cerradomys) 
 
(a) 
(b) 
Figure 5. Diﬀerence in performances of the best immunisation strategy (hemoculture - Highest 3) when
instead of the Leopardii the other top predator in the ecosystem (not parasitised by the vector) is immunised
instead (hemoculture - H 3 No Leopardus).
The other top predator is the maned wolf (Chrysocyon
brachiurus).
at much faster rates compared to other meta-
population dynamics (e.g extinction or migra-
tion), which are not currently considered in the
model.
However, including meta-population
dynamics would allow to explore important re-
search questions such as: (i) the interplay be-
tween predation and parasite ampliﬁcation over
top predators inﬂuencing parasite spread; (ii)
the inﬂuence of migration on parasite diﬀusion;
(iii) how extinction patterns inﬂuence parasite
spread. A promising candidate is the Marko-
vian analytical approach from Gómez-Gardeñes
et al. [15], in order to have even more realistic
representations of ecosystems through an eco-
multiplex framework.
IV.
ACKNOWLEDGEMENTS
The authors thank Alireza Goudarzi for
insightful
discussions
and
acknowledge
the
WWCS2017.
M.S. was supported by an EP-
SRC DTC grant (EP/G03690X/1).
S.S. ac-
knowledges support from the NWO Complex-
ity grant no. 645.000.013 and ERC Estuaries
grant no.
647570.
A.A. acknowledges sup-
port from the Swiss National Science Foun-
dation under grants no. P2LAP1-161864 and
P300P1-171537. C.S.A was supported by Con-
selho Nacional de Desenvolvimento Cientíﬁco e
Tecnológico (CNPq/Brazil).
[1] Alexander, K.A., Lewis, B.L., Marathe, M.,
Eubank, S. & Blackburn, J.K. (2012). Mod-
eling of wildlife-associated zoonoses: applica-
tions and caveats. Vector-Borne and Zoonotic
Diseases, 12, 1005–1018.
[2] Altizer, S., Nunn, C.L., Thrall, P.H., Gittle-
man, J.L., Antonovics, J., Cunningham, A.A.,
Dobson, A.P., Ezenwa, V., Jones, K.E., Peder-
sen, A.B. et al. (2003). Social organization and
parasite risk in mammals: integrating theory
and empirical studies. Annual Review of Ecol-
ogy, Evolution, and Systematics, 34, 517–547.
[3] Battiston, F., Nicosia, V. & Latora, V. (2014).
Structural measures for multiplex networks.
Physical Review E, 89, 032804.
[4] Battiston,
F.,
Nicosia,
V. & Latora,
V.
(2016). The new challenges of multiplex net-
works: measures and models. arXiv preprint
arXiv:1606.09221.
[5] Boccaletti,
S.,
Bianconi,
G.,
Criado,
R.,
Del Genio, C.I., Gómez-Gardenes, J., Ro-
mance, M., Sendina-Nadal, I., Wang, Z. &


## Page 10


10
Zanin, M. (2014). The structure and dynamics
of multilayer networks. Physics Reports, 544,
1–122.
[6] Bonvicino, C.R., Oliveira, J.d. & D’Andrea,
P.S. (2008). Guia dos roedores do Brasil, com
chaves para gêneros baseadas em caracteres ex-
ternos. Rio de Janeiro: Centro Pan-Americano
de Febre Aftosa-OPAS/OMS.
[7] Bueno, A.d.A., Belentani, S.C.d.S. & Motta-
Junior, J.C. (2002).
Feeding ecology of the
maned wolf, chrysocyon brachyurus (illiger,
1815)(mammalia: Canidae), in the ecological
station of itirapina, são paulo state, brazil.
Biota Neotropica, 2, 1–9.
[8] Cavalcanti, G.N. (2010).
Biologia comporta-
mental de Conepatus semistriatus (Carnivora,
Mephitidae) em Cerrado do Brasil Central.
Ph.D. thesis, PhD thesis, Universidade Federal
de Minas Gerais.
[9] Coura, J. (2005). Transmission of chagasic in-
fection by oral route in the natural history of
chagas disease. Revista da Sociedade Brasileira
de Medicina Tropical, 39, 113–117.
[10] De Domenico, M., Granell, C., Porter, M.A.
& Arenas, A. (2016). The physics of spread-
ing processes in multilayer networks. Nature
Physics.
[11] De Domenico, M., Solé-Ribalta, A., Cozzo, E.,
Kivelä, M., Moreno, Y., Porter, M.A., Gómez,
S. & Arenas, A. (2013). Mathematical formu-
lation of multilayer networks. Physical Review
X, 3, 041022.
[12] Dias, J. & Schoﬁeld, C.J. (1999).
The evo-
lution of chagas disease (american trypanoso-
miasis) control after 90 years since carlos cha-
gas discovery. Memórias do Instituto Oswaldo
Cruz, 94, 103–121.
[13] Dunne, J.A., Laﬀerty, K.D., Dobson, A.P.,
Hechinger, R.F., Kuris, A.M., Martinez, N.D.,
McLaughlin, J.P., Mouritsen, K.N., Poulin, R.,
Reise, K. et al. (2013). Parasites aﬀect food
web structure primarily through increased di-
versity and complexity.
PLoS Biology, 11,
e1001579.
[14] Funk, S., Nishiura, H., Heesterbeek, H., Ed-
munds, W.J. & Checchi, F. (2013). Identifying
transmission cycles at the human-animal inter-
face: the role of animal reservoirs in maintain-
ing gambiense human african trypanosomiasis.
PLoS Comput Biol, 9, e1002855.
[15] Gómez-Gardeñes, J., de Barros, A.S., Pinho,
S.T. & Andrade, R.F. (2015).
Abrupt tran-
sitions from reinfections in social contagions.
EPL (Europhysics Letters), 110, 58006.
[16] Hatcher, M.J., Dick, J.T. & Dunn, A.M.
(2006). How parasites aﬀect interactions be-
tween competitors and predators. Ecology Let-
ters, 9, 1253–1271.
[17] Haydon, D.T., Cleaveland, S., Taylor, L.H.,
Laurenson, M.K. et al. (2002).
Identifying
reservoirs of infection: a conceptual and prac-
tical challenge. Emerging infectious diseases,
8, 1468–1473.
[18] Herrera, H.M., Rocha, F.L., Lisboa, C., Rade-
maker, V., Mourão, G. & Jansen, A. (2011).
Food web connections and the transmission
cycles of trypanosoma cruzi and trypanosoma
evansi (kinetoplastida, trypanosomatidae) in
the pantanal region, brazil.
Transactions of
the Royal Society of Tropical Medicine and Hy-
giene, 105, 380–387.
[19] Herrera, L. & Urdaneta-Morales, S. (1992).
Didelphis marsupialis: a primary reservoir of
trypanosoma cruzi in urban areas of caracas,
venezuela. Annals of Tropical Medicine & Par-
asitology, 86, 607–612.
[20] Hudson,
P.J.,
Rizzoli,
A.,
Grenfell,
B.T.,
Heesterbeek, H. & Dobson, A.P. (2002). The
ecology of wildlife diseases. Oxford University
Press Oxford.
[21] Jansen, A.M., Xavier, S.C. & Roque, A.L.R.
(2015). The multiple and complex and change-
able scenarios of the trypanosoma cruzi trans-
mission cycle in the sylvatic environment. Acta
tropica, 151, 1–15.
[22] Jetz, W., Carbone, C., Fulford, J. & Brown,
J.H. (2004). The scaling of animal space use.
Science, 306, 266–268.
[23] Johnson, P.T., Dobson, A., Laﬀerty, K.D.,
Marcogliese, D.J., Memmott,
J., Orlofske,
S.A., Poulin, R. & Thieltges, D.W. (2010).
When parasites become prey: ecological and
epidemiological signiﬁcance of eating parasites.
Trends in ecology & evolution, 25, 362–371.
[24] Jones, K.E., Patel, N.G., Levy, M.A., Storey-
gard, A., Balk, D., Gittleman, J.L. & Daszak,
P. (2008). Global trends in emerging infectious
diseases. Nature, 451, 990–993.
[25] Kéﬁ, S., Berlow, E.L., Wieters, E.A., Joppa,
L.N., Wood, S.A., Brose, U. & Navarrete, S.A.
(2015). Network structure beyond food webs:
mapping non-trophic and trophic interactions
on chilean rocky shores. Ecology, 96, 291–303.
[26] Kéﬁ, S., Miele, V., Wieters, E.A., Navarrete,
S.A. & Berlow, E.L. (2016). How structured
is the entangled bank? the surprisingly simple
organization of multiplex ecological networks
leads to increased persistence and resilience.
PLoS Biol, 14, e1002527.
[27] Kivelä, M., Arenas, A., Barthelemy, M., Glee-
son, J.P., Moreno, Y. & Porter, M.A. (2014).
Multilayer networks. Journal of complex net-
works, 2, 203–271.
[28] Laﬀerty, K.D., Allesina, S., Arim, M., Briggs,
C.J., De Leo, G., Dobson, A.P., Dunne, J.A.,
Johnson, P.T., Kuris, A.M., Marcogliese, D.J.
et al. (2008). Parasites in food webs: the ul-
timate missing links. Ecology letters, 11, 533–
546.
[29] Lima, A., De Domenico, M., Pejovic, V. & Mu-
solesi, M. (2015). Disease containment strate-
gies based on mobility and information dissem-
ination. Scientiﬁc reports, 5, 10650.
[30] Lloyd-Smith, J.O., George, D., Pepin, K.M.,
Pitzer, V.E., Pulliam, J.R., Dobson, A.P.,
Hudson, P.J. & Grenfell, B.T. (2009).
Epi-
demic dynamics at the human-animal inter-
face. science, 326, 1362–1367.
[31] McCallum, H., Barlow, N. & Hone, J. (2001).
How should pathogen transmission be mod-
elled? Trends in ecology & evolution, 16, 295–
300.


## Page 11


11
[32] de Melo Amboni, M.P. (2007). Dieta, disponi-
bilidade alimentar e padrão de movimentação
de lobo-guará,
Chrysocyon brachyurus,
no
Parque Nacional da Serra da Canastra, MG.
Ph.D. thesis, Universidade Federal de Minas
Gerais.
[33] Myers, P., Espinosa, R., Parr, C., Jones, T.,
Hammond, G. & Dewey, T. (2008). The an-
imal diversity web. Accessed May16, 2017at:
http://animaldiversity. org.
[34] Noireau, F., Diosque, P. & Jansen, A.M.
(2009). Trypanosoma cruzi: adaptation to its
vectors and its hosts. Veterinary research, 40,
1–23.
[35] Ostfeld, R.S. & Holt, R.D. (2004). Are preda-
tors good for your health?
evaluating evi-
dence for top-down regulation of zoonotic dis-
ease reservoirs. Frontiers in Ecology and the
Environment, 2, 13–20.
[36] Packer, C., Holt, R.D., Hudson, P.J., Laﬀerty,
K.D. & Dobson, A.P. (2003).
Keeping the
herds healthy and alert: implications of preda-
tor control for infectious disease. Ecology Let-
ters, 6, 797–802.
[37] Penczykowski, R.M., Laine, A.L. & Koskella,
B. (2016).
Understanding the ecology and
evolution of host–parasite interactions across
scales. Evolutionary applications, 9, 37–52.
[38] Perkins, S.E., Cattadori, I. & Hudson, P.J.
(2005).
The role of mammals in emerging
zoonoses. Mammal Study, 30, S67–S71.
[39] Pilosof, S., Porter, M.A., Pascual, M. & Kéﬁ,
S. (2017).
The multilayer nature of ecologi-
cal networks. Nature Ecology & Evolution, 1,
0101.
[40] Ramos, V.d.N. et al. (2007). Ecologia alimen-
tar de pequenos mamíferos de áreas de cerrado
no sudeste do brasil.
[41] Reis, N.R., Peracchi, A.L., Pedro, W.A. &
Lima, I.P. (2006). Mamíferos do Brasil. Uni-
versidade Estadual de Londrina.
[42] Rocha, F. (2006).
Área de uso e seleção
de habitats de três espécies de carnívoros
de
médio
porte
na
fazenda
Nhumirin,
e
arredores,
Pantanal
da
Nhecolândia,
MS.
Ph.D.
thesis,
Dissertação
(Mestrado
em
Ecologia
e
Conservação)–Curso
de
Pós-
graduação em Ecologia, Universidade Federal
de
Matogrosso
do
Sul,
Campo
Grande.
Disponível
em:>
http://repositorio.
cbc.
ufms.
br:
8080/jspui/bitstream/123456
789/569/1/Fabiana%
20Lopes%
20Rocha.
pdf.> Acessado em: 2012-03-01.
[43] Rocha, F.L., Roque, A.L.R., de Lima, J.S.,
Cheida,
C.C.,
Lemos,
F.G.,
de Azevedo,
F.C., Arrais, R.C., Bilac, D., Herrera, H.M.,
Mourão, G. et al. (2013). Trypanosoma cruzi
infection in neotropical wild carnivores (mam-
malia: Carnivora): at the top of the t. cruzi
transmission chain. Plos one, 8, e67463.
[44] Roque, A.L.R., Xavier, S.C., Gerhardt, M.,
Silva, M.F., Lima, V.S., D’Andrea, P.S. &
Jansen, A.M. (2013).
Trypanosoma cruzi
among wild and domestic mammals in diﬀer-
ent areas of the abaetetuba municipality (pará
state, brazil), an endemic chagas disease trans-
mission area. Veterinary parasitology, 193, 71–
77.
[45] Roque, A.L.R., Xavier, S.C., da Rocha, M.G.,
Duarte, A.C.M., D’Andrea, P.S. & Jansen,
A.M. (2008). Trypanosoma cruzi transmission
cycle among wild and domestic mammals in
three areas of orally transmitted chagas dis-
ease outbreaks. The American journal of trop-
ical medicine and hygiene, 79, 742–749.
[46] Rushmore,
J.,
Caillaud,
D.,
Hall,
R.J.,
Stumpf, R.M., Meyers, L.A. & Altizer, S.
(2014).
Network-based vaccination improves
prospects for disease control in wild chim-
panzees. Journal of the Royal Society Inter-
face, 11, 20140349.
[47] dos Santos, E.M. (2012). Predação do roedor
calomys sp.(cricetidae) pelo marsupial mon-
odelphis domestica (didelphidae) em buíque–
pe, brasil. Biotemas, 25, 317–320.
[48] Sanz, J., Xia, C.Y., Meloni, S. & Moreno,
Y. (2014). Dynamics of interacting diseases.
Physical Review X, 4, 041005.
[49] Schoﬁeld, C.J. et al. (1994). Triatominae: bi-
ology & control. Eurocommunica Publications.
[50] Stella, M., Andreazzi, C.S., Selakovic, S.,
Goudarzi, A. & Antonioni, A. (2016). Para-
site spreading in spatial ecological multiplex
networks.
Journal of Complex Networks, p.
cnw028.
[51] Streicker, D.G., Fenton, A. & Pedersen, A.B.
(2013). Diﬀerential sources of host species het-
erogeneity inﬂuence the transmission and con-
trol of multihost parasites. Ecology Letters, 16,
975–984.
[52] Webster, J.P., Borlase, A. & Rudge, J.W.
(2017).
Who acquires infection from whom
and how? disentangling multi-host and multi-
mode transmission dynamics in the ‘elimina-
tion’era. Phil. Trans. R. Soc. B, 372, 20160091.
[53] Wobeser, G.A. (2013). Essentials of disease in
wild animals. John Wiley & Sons.
[54] Yamagata, Y. & Nakagawa, J. (2006). Control
of chagas disease. Advances in parasitology, 61,
129–165.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
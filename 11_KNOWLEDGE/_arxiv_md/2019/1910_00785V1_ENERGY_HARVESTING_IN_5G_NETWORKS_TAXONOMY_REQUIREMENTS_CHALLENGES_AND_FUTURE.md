---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1910.00785v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1910.00785v1_Energy_Harvesting_in_5G_Networks__Taxonomy__Requirements__Challenges__and_Future

> Source: 1910.00785v1_Energy_Harvesting_in_5G_Networks__Taxonomy__Requirements__Challenges__and_Future.pdf

> Pages: 9

---


## Page 1


1
Energy Harvesting in 5G Networks: Taxonomy,
Requirements, Challenges, and Future
Directions
Muhammad Imran, Latif U. Khan, Ibrar Yaqoob, Senior Member, IEEE, Ejaz Ahmed, Senior
Member, IEEE, Muhammad Ahsan Qureshi, and Arif Ahmed
Abstract—Consciousness of energy saving is increasing in ﬁfth-generation (5G) wireless networks due to the high energy consumption
issue. Energy harvesting technology is a possible appealing solution for ultimately prolonging the lifetime of devices and networks.
Although considerable research efforts have been conducted in the context of using energy harvesting technology in 5G wireless
networks, these efforts are in their infancy, and a tutorial on this topic is still lacking. This study aims to discuss the beneﬁcial role of
energy harvesting technology in 5G networks. We categorize and classify the literature available on energy harvesting in 5G networks
by devising a taxonomy based on energy sources; energy harvesting devices, phases, and models; energy conversion methods, and
energy propagation medium. The key requirements for enabling energy harvesting in 5G networks are also outlined. Several core
research challenges that remain to be addressed are discussed. Furthermore, future research directions are provided.
Index Terms—Energy harvesting, ﬁfth-generation networks, green networking, energy emission, adaptive energy management.
!
1
INTRODUCTION
With the fruition of Internet of Things (IoT) and machine-
to-machine communication, the design and implementation
of emerging ﬁfth-generation (5G) networks must be tailored
accordingly. These 5G networks are projected to be widely
deployed in 2020 to enable massive connectivity and pro-
vide data rate speeds of 10 Gbps in the peak hours for
low mobility and 1 Gbps of data rate for high mobility
[1]. With the signiﬁcant reduction of delay, support for
real-time multimedia applications is likely to increase but
satisfying stringent energy and computation constraints in
an affordable and sustainable way is a real challenge [2].
To cope with these challenges, 5G networks are expected to
deploy low-powered radio access nodes, which form small
cells across a region. These radio access nodes can work in
licensed and unlicensed spectrum bands, thereby increasing
energy consumption in the network infrastructure [3].
The contribution of CO2 emission by the ICT in 2015
was 5% and expected to increase due to proliferation of a
sheer number of mobile devices in upcoming years. By 2020,
75% of the ICT sector would be wireless, thereby indicating
that wireless communications will be the critical sector for
•
Muhammad Imran is with the College of Applied Computer Science, King
Saud University, Riyadh, Saudi Arabia.
•
Latif U. Khan is with the Department of Telecommunication Engineering,
University of Engineering & Technology, Mardan, Pakistan.
•
Ibrar Yaqoob is with the Department of Computer Science and Engineer-
ing, Kyung Hee University, Yongin-si 17104, South Korea.
•
Ejaz Ahmed is with the Centre for Mobile cloud Computing Research
(C4MCCR), University of Malaya, 50603 Kuala Lumpur, Malaysia.
•
Muhammad Ahsan Qureshi is with Faculty of Computing and Informa-
tion technology, University of Jeddah, Khulais, Saudi Arabia.
•
Arif Ahmed is with Department of Computer Science & Engineering,
National Institute of Technology, Silchar, Silchar, India.
researchers as far as reducing ICT-related CO2 emissions
is concerned. This condition will trigger the innovations
in the network architecture and technologies of wireless
communication, thereby leading to 5G cellular networks [4].
Thus, providing and supplying energy from other sources
to support the high rates and continuous availability of
the network and designing energy-efﬁcient architectures are
essential.
Energy harvesting techniques can be used to produce
energy from the surrounding environment, thereby con-
verting energy to electrical power for use in 5G network
devices, such as base stations (BSs) and mobile phones
[5]. Figure 1 shows the process of energy harvesting in
5G networks. Energy harvesting is a promising technology
that does not diminish energy consumption of devices but
enables a device to be self-powered when emergency power
shortage is encountered.
Although several studies have been conducted on 5G
networks in terms of energy harvesting, a tutorial on this
topic is lacking. The contributions of this study are as
follows:
•
We present motivation for employing energy har-
vesting in 5G networks.
•
We provide an overview of several possible ways
of harvesting energy in 5G multi-tier heterogeneous
network architecture.
•
We taxonomize the literature based on indispensable
parameters.
•
We outline the key requirements of deploying energy
harvesting solutions in 5G networks.
•
Several open challenges and future directions in en-
abling energy harvesting on 5G networks are identi-
ﬁed, enumerated and discussed.
arXiv:1910.00785v1  [cs.NI]  2 Oct 2019


## Page 2


2
Macro-Cell
Micro-Cell
Kinetic
Wind
RF
Heat
Solar
Finding Source
Acquiring Energy
Energy Storage
Energy Distribution
Battery
Search
Fig. 1: Energy harvesting process in 5G networks.
These contributions are provided in separate sections from
2-7. We provide concluding remarks in section 8.
2
MOTIVATION
Various applications, ranging from basic communication
and social networking to infotainment services that utilize
mobile network for their effective usage, are currently avail-
able. These applications demand high data transfer rate and
massive connected network. The ever-increasing demand of
faster mobile communication and utilization of increasing
data paved the way toward 5G mobile networks. The 5G
network provides higher data transfer rate and improved
coverage than its predecessors. However, the quest toward
faster and more reliable mobile communication has resulted
in the overall energy consumption stipulation in 5G net-
works [6]. One the basis of the extrapolation of important
metrics, such as number of communication devices sold per
year and data trafﬁc, communication technology could use
51% of the global electricity by 2030 if adequate improve-
ment in electric efﬁciency is unachieved.
Typical household and ofﬁce environments are consid-
erably changed in terms of energy requirements, especially
in the past decade as increasing wireless nodes are being
added to the network. A total of 4.43 billion mobile phone
subscribers exist worldwide as opposed to 4.01 and 4.23
billion in 2013 and 2014, respectively, thereby indicating an
approximately 5% annual increase. The external and inter-
nal networks with a sufﬁcient quantity of battery-powered
wireless nodes require energy to be harvested [7].
The development of energy-efﬁcient algorithms, stan-
dards, and protocols is a passable way that decreases energy
consumption in mobile communication [8]. However, one
of the most adequate measures to fulﬁll the increasing
energy requirements is to use renewable energy sources. Re-
searchers have explored numerous ways to obtain adequate
power for wireless networks. Energy harvesting involves
capturing and storing energy derived from external sources,
including solar, thermal, wind, vibration, and human body
energies, for wireless devices. These sources are commonly
and abundantly available in the environment; hence, energy
harvesting is the most promising technique to fulﬁll the
energy requirements of wireless networks.
3
5G MULTI-TIER HETEROGENEOUS NETWORK
ARCHITECTURE
The 5G cellular network is envisioned to enable users with
novel applications, such as augmented reality, self-driving
cars, smart homes, smart farming, and smart e-health care.
All 5G applications are generally divided into three use
cases identiﬁed by the International Telecommunication
Union Radio communication Sector. These use cases include
enhanced mobile broadband (eMBB), ultra-reliable low-
latency communication (URLLC), and massive machine-
type communication (mMTC). In these use cases, mMTC
is characterized by a massive number of nodes with low
sensitivity to latency. The URLLC has the lowest latency
requirements among the three uses cases with enhanced
reliability and includes various applications, such as self-
driving cars and mission critical applications. Meanwhile,
eMBB has high throughput requirement applications, such
as HD video streaming, virtual, and augmented reality. To
enable these use cases, 5G networks will use heterogeneous
networks (HetNets) along with densiﬁcation of small-cell
BSs and device-to-device (D2D) communication. The results
of densiﬁcation are high spectral efﬁciency and decreased
mobile transmission power. However, these results will
cause an increase in the overall energy consumption of
networks. Therefore, fulﬁlling the energy demands of 5G
networks is imperative, as shown in Figure 2.
The different tiers of 5G HetNets can be empowered by
grid station and energy harvesting. Using harvested energy
and grid power simultaneously is highly effective. Power
from energy harvesting and grid is used because of the
substantial random variations that exist in harvested energy.
Therefore, grid energy, in addition to harvested energy, is
necessary to fulﬁll the energy requirements of the different
tiers of 5G networks.
Macrocell BSs can be used to transmit information and
energy simultaneously. This technique enables mobile de-
vices with limited energy to fulﬁll their energy require-
ments. Radio frequency (RF) energy harvesting zone is
smaller than the transmission zone because the former re-
quires higher energy than the that required for information
detection. In addition to RF energy harvesting from macro-
cell BSs, RF energy harvesting sources with a low range can


## Page 3


3
be used to supply energy to devices in its proximity. Interfer-
ence signals can also be used for energy harvesting, which
improves energy efﬁciency of cellular networks in contrast
to system performance degradation due to interference.
The D2D tier in 5G cellular networks can be used to
improve the system throughput. Harvested energy along
with devices that have battery sources can be leveraged to
enable energy-efﬁcient D2D communication. Furthermore,
D2D communication can be assisted by relays to enhance
further their performance, especially during poor channel
conditions. The third-layer relays can be connected to the
macrocell eNB and then used to serve D2D and mobile
users with poor channel conditions [9]. The relays can also
be operated by harvesting energy from the environment in
addition to RF energy and then simultaneously assist D2D
communication and communication between the user and
the BS.
Fig. 2: 5G HetNets with energy harvesting.
4
TAXONOMY OF 5G NETWORKS WITH ENERGY
HARVESTING
The taxonomy on energy harvesting in 5G network is shown
in Figure 3. This taxonomy is categorized on the basis
of the following attributes: a) harvesting technologies, b)
harvesting devices, c) energy conversion methods, d) har-
vesting phases, e) energy harvesting models, and f) energy
propagation medium.
4.1
Energy Sources
Many energy sources are available in the surroundings for
energy harvesting in 5G networks [10]. These energy sources
can be classiﬁed into ﬁve main categories: a) RF, b) solar, c)
wind, d) thermal, and e) body temperature.
The RF-based harvesting uses RF signals in the air to
produce energy. This type of energy is mined from the
electromagnetic radiations generated by different sources,
such as telecom BS, Bluetooth, and infrared devices. Solar
energy is an established technology for energy generation
at a large scale. Photovoltaic systems are used to produce
electricity from solar energy. Electricity can be produced
from milliwatt to megawatt range. In addition, energy can
be produced from wind using wind turbines that convert
kinetic energy of the wind into mechanical power. There-
after, the mechanical power is transformed into electricity by
using generators. The electricity through wind energy can
be produced from kilowatt to megawatt range. The energy
can be rapidly produced from various thermal sources, such
as animals, persons, and machines, using a thermoelectric
generator. This power can be classiﬁed as thermal energy.
Energy harvested from kinetic sources can be a key enabling
mechanism for emerging 5G-based IoT and wearable de-
vices. A kinetic energy harvester converts the mechanical
power obtained from the movement of an object into elec-
trical energy using a micro-electromechanical system.
4.2
Energy Harvesting Devices
The harvesting devices in 5G networks range from the
user mobile devices connected to the 5G network to the
telecom network operator’s BSs. The mobile devices are
one of energy-drained devices with limited power storage
capacity [11]. However, mobile devices can leverage the
vibration and thermal harvesting mechanisms to produce
energy from the human body. Similarly, wearable devices
can leverage body temperature and movement to mitigate
the energy scarcity problem. Although SBS and eNB are
supposed to deploy densely in 5G networks, they will
require substantial energy for power. These deployments
are in underdeveloped regions, such as hill terrain and
frequently ﬂood-affected areas. In such places, BSs of 5G
network can utilize the energy harvesting technologies to
acquire wind, solar, and thermal energies.
4.3
Energy Conversion Methods
The performance of energy harvesting in 5G is considerably
dependent on the available energy to harvest and energy
conversion technique used (i.e., the efﬁciency of energy
conversion from the source ambient to the usable electric
energy). Energy conversion techniques are related with the
power sources. Some key energy conversion techniques are
photovoltaic and electromagnetic conversion and turbine-
, piezoelectric-, and microelectromechanical system-based.
Photovoltaic conversion is used to transform light into
electricity by semiconducting materials that possess photo-
voltaic characteristics. A turbine is a rotary turbomachine
that transforms kinetic energy into electrical power. An
example of a turbomachine is wind turbine. A piezoelectric-
based technique collects the electric charge in a solid ma-
terial resulting from a mechanical stress. Electromagnetic
energy conversion is an important mechanism for energy
harvesting. The conversion requires an energy conversion
device and adapter. Microelectromechanical systems are
small devices comprised of integrated electrical and me-
chanical components that are used to produce a small
amount of energy by vibration and movement of an object.
4.4
Energy Harvesting Phases
The energy harvesting process in 5G can be divided into
four phases: a) ﬁnding ambient source, b) acquiring energy,


## Page 4


4
Energy Harvesting in 5G Networks
Energy
Harvesting 
Phases
Energy
Harvesting 
Devices
Energy 
Conversion 
Methods
Photovoltaic 
Conversion
Turbine-based
Piezoelectrics-
based
Electromagnetic 
Conversion
Energy
Sources
Radio 
Frequency 
Solar
Mobile Devices
Wearable 
Devices
Sensor Nodes
SBS
Finding 
Ambient 
Source
Acquiring 
Energy
Storing 
Energy
Wind
Thermal
Energy 
Distribution
Energy 
Harvesting 
Models
Cenralized
Decentralized
Distributed
eNB
Energy 
Propagation
Medium
Wired
Wireless
Kinetic 
Sources
Microelectro-
mechanical 
Systems-based
Fig. 3: Taxonomy of energy harvesting in 5G networks.
c) energy storage, and d) energy distribution phase. In the
ambient source ﬁnding phase, the harvesting device scans
the surrounding environment to ﬁnd any harvesting energy
sources. The harvesting devices will switch on the conver-
sion device to acquire energy on the basis of the available
ambient sources. The next phase is transferring the energy
from the conversion device to the storage section to store the
energy for future utilization. The last phase is to distribute
the acquired energy to the ﬁnal harvesting devices.
4.5
Energy Harvesting Models
The solutions of energy harvesting can be centralized, de-
centralized, and distributed. In the centralized energy har-
vesting model, a central harvesting device is responsible to
harvest the energy in the region (nearby BSs), and the 5G
devices and energy storage components are also co-located
with each other. In this type of solution, the devices remain
in static, and the environment is easily predictable, thereby
indicating that the complexity is low. The central devices
dissipate the energy to the surrounding environment. How-
ever, in the decentralized energy harvesting solution, the
devices are in a random state. The devices individually har-
vest the energy, and no or less communication exists among
the devices (such as sensor nodes and mobile devices) in
the region. Finally, distributed energy harvesting is similar
to the centralized harvesting solution; however, the number
of harvesting devices is more than one. Harvesting devices
coordinate with each other.
4.6
Energy Propagation Medium
Similar to information ﬂow in the 5G network, the harvested
energy can be distributed among the peer devices in wired
and wireless medium. RF energy is transferred around the
environment in a radio wave form. The harvesting device
in this category, such as wireless mobile charger, uses a
wireless energy propagation medium. In the wired medium,
the energy is transmitted in the physical wire from one
point to another (e.g., from conversion device to the battery
storage).
5
ENERGY HARVESTING REQUIREMENTS FOR 5G
NETWORKS
Figure 4 summarizes the key requirements for enabling
energy harvesting in 5G cellular networks. Further details
are provided in the following subsections.
5.1
Continuous Uniform Energy Availability
Energy harvesting produce power supply without any inter-
ruption and produce energy from the surroundings without
using any power supply from other sources. The scarcity
of energy harvesting will be prevalent in 5G networks and
in cases of emergency situation, such as ﬂood and earth-
quake, electric supply is unavailable to power 5G network
equipment from nowhere. In such a situation, energy drawn
from the surrounding is the only option left to power 5G
devices. Given the variations in harvesting energy, we must
use energy storing devices to enable the continuous energy
supply to 5G network devices. For example, if harvested
energy is the only source in a disaster situation and we
are using solar energy harvesting, then we will face the
challenge of variations in the harvested energy and run
out of energy at night time or during a cloudy weather. To
cope with above discussed potential issues, the harvesting
energy device must be equipped with a battery to enable its
continuous uniform operation.


## Page 5


5
BS Assisted 
Infrastructure
5G Energy Harvesting Requirements
Efficient Sharing of 
Energy
Continuous Uniform 
Energy Availability
RF Energy Harvesting 
Infrastructure
Adaptive Energy 
Management 
Mechanisms
Biased User 
Association
Hybrid Energy 
Harvesting
Energy Storage 
Devices 
Environmental 
Harvesting 
Energy
Energy 
Monitoring
Energy Resource 
Allocation
Power Prediction
Dynamic Power 
Control
Infrastructure-
less
Energy-Aware 
Association
Energy Prediction
Grid Energy 
Harvested Energy
Fig. 4: Energy harvesting requirements for 5G networks.
5.2
Efﬁcient Sharing of Energy
The 5G network can use the harvested energy and energy
derived from the main power supply, and they can be
transmitted in wired line and wireless connection, such as
a wireless charger. A new efﬁcient energy sharing proto-
col needs to incorporate several 5G network performance
parameters, such as bandwidth and delay, to share the
harvested energy because energy harvesting is dependent
on the availability of resources in the environment. Various
schemes based on optimization theory and game theory can
be used to ensure efﬁcient sharing of harvested energy. On
the other hand, a hybrid scheme using both optimization
theory and game theory can be leveraged to enable efﬁcient
sharing of harvested energy.
5.3
Adaptive Energy Management Mechanisms
Generally, energy harvesting system in 5G network involves
power harvesting devices, battery for energy storage, and
supercapacitors. The system can monitor the electric con-
sumption level of the various components and the power
level of the battery with energy harvesting devices. On the
other hand, both environmental and harvested energy have
limitations in their availability. Therefore, we must develop
an adaptive energy management mechanism that will pro-
vide dynamic power from the harvested energy depending
on the energy requirement. The two main aspects of adap-
tive energy mechanism are energy consumption prediction
of the operating device and dynamic power control of the
harvesting device.
5.4
RF Energy harvesting Infrastructure
In 5G cellular networks, presence of wide-band commu-
nication signals offer opportunity to harvest RF energy.
The 5G user devices generally have energy limitations
compared to BS and access point (AP). Therefore, AP and
BS can be utilized to jointly transmit energy and infor-
mation signals. The RF energy harvesting architecture can
be either infrastructure-based or infrastructure-less. In the
infrastructure-based architecture, the centralized BS or AP
transmits RF energy and information. The users commu-
nicate one another through the same centralized BS or AP
from which they harvest energy. By contrast, infrastructure-
less architecture involves the utilization of wireless energy
transmitters, and users in its vicinity can use this RF energy.
The users can communicate with one another while using
energy from the RF energy source to continue its operation
in a cost-effective way. New protocols should be designed
to enable the architecture of 5G that supports RF energy
harvesting in infrastructure-based and -less modes.
5.5
Hybrid Energy harvesting
5G devices empowered by harvesting energy sources must
be able to withstand the device power requirements. How-
ever, there exist signiﬁcant variations in RF energy. Addi-
tionally, environmental harvesting energy has both varia-
tions and outage issue. For instance, harvesting energy from
the sun is possible only at day times. To cope with variations
in harvesting energy sources, it is necessary to use hybrid
energy sources that jointly utilize the harvested energy and
energy from the power grid and diesel generators. Such a
hybrid energy harvesting system should fully utilize the
harvested energy. In addition, the system should use the
energy from power if required for the operation of 5G
devices.
5.6
Biased User Association
In 5G networks, HetNets are used to meet the high data
rate and latency requirements. HetNets consist of multiple
tiers, such as macrocell and child tiers. The transmission
power of the child tier is lower than the parent one. There-
fore, the HetNets empowered by energy harvesting suffer
from the challenge of unbalanced user association because
the user association based on the received signal strength
might result in overloading of the macrocell tier. This type
of unbalanced operation in cellular networks empowered


## Page 6


6
jointly by energy harvesting and other sources results in
inefﬁcient energy consumption. To avoid such type of situa-
tion, it is necessary to consider biased user association in 5G
cellular networks. A biased user association that achieves
a load-balanced operation should be performed to prevent
overloading of the macrocell tier. Alternatively, we can say
that it results in energy-aware user association.
6
OPEN RESEARCH CHALLENGES
The following discussion highlights the challenges involve
in enabling energy harvesting on 5G networks that must be
overcome. Table 1 summarizes the research challenges along
with their perceived solutions.
6.1
Broadband Energy Harvesting
In a 5G cellular network, novel frequency bands in addition
to predecessor cellular networks bands are expected to use
for enabling superfast access. Numerous devices operating
at a wide range frequency bands offer opportunity for other
devices to harvest their RF energy. More speciﬁcally, the
mobile devices that are on the edge of a cell may expe-
rience interference from the neighboring cells. The edge
devices need more power to obtain a sufﬁcient level of
signal-to-noise ratio while transmitting on the uplink. This
energy requirement can be fulﬁlled by harvesting the energy
from ambient RF neighboring cell sources. However, this
approach needs a new receiver architecture with circuits
to harvest the energy from signals of wide range of fre-
quencies. The unreliable and dynamic nature of the RF
ambient sources make it challenging to harvest and store
the sufﬁcient amount of energy for meeting the edge device
requirement.
6.2
RF Energy Harvesting Relays
5G cellular networks are intended to use relay for through-
put, especially at the cell edges. These relays have energy
constraints and must be powered by harvested energy.
Both energy from environmental sources and RF sources
can be used. However, there exist signiﬁcant variations
in the environmental sources, such as sun-light and wind
energy. Therefore, RF energy harvesting relays is a feasible
solution to enable simultaneous communication and RF
energy harvesting. In cellular networks, the intermediate
relay node can use the source signal energy to forward it
to the destination. Determining the positions and selection
of relays for improving overall performance is an open
research area for 5G cellular networks given that energy
harvesting is used in cellular networks for achieving an
energy-optimized operation. Other than optimal placement
of relays, novel protocols offering joint communication and
energy harvesting performance enhancement must be pro-
posed.
6.3
Online Energy Harvesting
Energy in wireless communication can be harvested either
from the environment, such as wind and sun, or RF signals.
In both cases, the variations that exist in the available
energy of the harvesting sources (e.g., wind, sun, and RF
signals) will impose limitations on the device design that
range from a user equipment to the operator BS. The device
energy requirement at a certain time should not exceed
the harvested energy up to that time. Energy harvesting
techniques can work in an ofﬂine fashion using prior as-
sumption of the known harvested energy from the source.
However, obtaining the information about harvested energy
in practical scenarios is difﬁcult. Therefore, efforts must
be made to design the effective online approaches for 5G,
which are not based on the prior assumption of the amount
of energy harvested, to overcome the limitation of the
ofﬂine approach. Stochastic optimization-based techniques
that utilize the assumption of the known energy process
statistics can be used. In addition to stochastic optimization,
techniques based on learning theory can also be used for
online energy harvesting.
6.4
Interference-Assisted Energy Harvesting
In 5G cellular networks, the existence of a variety of in-
terference signal offers the opportunity to harvest their RF
energy. Additionally, environmental energy harvesting has
limitations that impose challenges on devices operating via
harvested energy only. Although interference has degraded
the performance of the communication systems, it can be
used positively in energy harvesting. Wireless signal con-
tains energy and information; therefore, we can harvest
energy from the interference signal. In 5G HetNets, different
tiers exist, such as macrocell and small-cell tiers, in which
interference is a prominent issue, especially at the macrocell
edges. On the other hand, there exist signiﬁcant limitations
in the environmental energy harvesting. Therefore, we can
use interference in energy harvesting to improve the overall
system performance. The architecture of energy harvesting
devices that range from user devices to network operator
BSs should be designed in a way that it effectively utilizes
interference in energy harvesting.
6.5
Harvested Energy Resource Allocation
Harvested energy from both environmental and RF sources
has signiﬁcant limitations. Therefore, they must be used efﬁ-
ciently to fulﬁll need of 5G networks. The manner in which
energy resources from different energy harvesting sources
should be allocated among 5G devices to maximize jointly
the overall proﬁt and QoS must be determined. Numerous
harvested energy resource allocation schemes suffer from
high latency due to their associated computational com-
plexity. To address this concern, designing algorithms that
will perform efﬁcient resource allocation with low latency
to maximize the overall quality of experience is necessary
to address the aforementioned concern. Energy harvesting
systems can obtain power either from natural sources or
RF signals. Therefore, we must design adaptive algorithms
to allocate the energy resources among the 5G network
devices. Several schemes based on game theory, learning
theory, and optimization theory can be used for efﬁcient
harvested energy resource allocation. On the other hand,
an adaptive harvesting energy resource allocation scheme
based jointly on game theory and learning can be a viable
solution.


## Page 7


7
TABLE 1: Summary of the research challenges and their perceived solutions.
Challenges
Causes
Guidelines
Broadband Energy Harvesting
•
Wide range of spectrum usage in 5G
•
High interference at cell edges
•
Energy harvesters with high range of
operating frequencies
RF Energy Harvesting Relays
•
Existence of relays for throughput en-
hancement
•
Signiﬁcant variations in environmental
harvested energy
•
Novel joint communication and energy
harvesting protocols for relays
•
Optimal placement of relays based on
joint optimization of energy harvesting
and communication
Online Energy Harvesting
•
Harvested energy outage
•
Frequent variations in both RF and en-
vironmental harvesting energy sources
•
Stochastic
optimization-based
techniques
•
Harvesting schemes based on machine
learning
Interference-Assisted
Energy
Harvesting
•
Presence of interference signals in wire-
less medium from a variety of sources
•
Environmental harvested energy limita-
tions
•
Novel transceiver design for joint com-
munication and energy harvesting
Harvested Energy Resource Al-
location
•
Limited harvested energy
•
High latency in harvested energy re-
source allocation
•
Adaptive harvested energy resource al-
location
•
Optimization theory based harvested
energy resource allocation
•
Game theory based harvested energy
resource allocation
•
Learning theory based harvested en-
ergy resource allocation
7
FUTURE DIRECTIONS
This section provides several indispensable future directions
to new researchers working in the domain.
7.1
Energy-Optimized Wearable 5G Network
The inadequate battery volume and intensive processing
requirement of the future 5G wearable networks is attracting
the researchers to come up with the new energy efﬁciency
schemes. It is obvious that the solutions based on modern
energy harvesting can improve the battery life of wear-
able devices. For the wearable devices, the energy can be
harvested in a variety of ways using the existing energy
harvesting techniques. Energy for the wearable devices can
be harvested through wireless signals and through human
body (body movement, body heat and body friction), to
name a few [12]. However, the higher frequency spectra
and potentially multiple sources of energy-harvesting for
the 5G wearable network demand the network to be energy-
optimized. Further research on the selection of energy har-
vesting techniques and optimization of usable energy for
individual categories of wearable 5G devices is required in
the future.
7.2
Three-tier Cooperative 5G Network with Energy
Harvesting as Core Aspect
Energy efﬁciency and spectral efﬁciency are among the most
important issues in the 5G network. Most of the existing 5G
architectures consider the energy and spectrum efﬁciency
separately [13]. A few studies also exist in the literature;
which tend to integrate the energy efﬁciency and spectral
efﬁciency. Furthermore, the mobility of individual 5G de-
vices introduces ambient noise that affects both the energy
efﬁciency and the spectral efﬁciency. One way of coping
with this challenge is to present a three-tier cooperative 5G
network while considering energy harvesting as core aspect
in which the trio (a) energy efﬁciency, (b) spectral efﬁciency
and c) mobility scenarios are collectively considered. The ex-
isting energy harvesting techniques can improve the energy
efﬁciency while the efﬁcient use of available spectra can deal
with exponential growth of 5G devices. The consideration
of mobility scenario will further complement the future
5G technologies by managing ambient noise. However, the
cooperation among the above mentioned three tiers demand
new algorithms and techniques to be developed in the
future.


## Page 8


8
7.3
Wireless Power Transfer
Simultaneous Wireless Information and Power Transfer
(SWIPT) essentially allows the information and power to be
transmitted simultaneously using the same RF signal [14].
Non-orthogonal Multiple Access (NOMA) is a key enabler
for 5G network that addresses various challenges such as
serving multiple users over same radio resources and high
throughput. Researchers have already investigated the ap-
plication of SWIPT to NOMA and presented promising re-
sults in terms of increased network throughput and energy
efﬁciency [15]. However, the existing studies investigate
the SWIPT-NOMA applications by considering idealistic
assumptions such as perfect channel state information and
perfect hardware. Nonetheless, 5G devices can suffer from
imperfections such as hardware impairments and imper-
fect channel state information. However, the practical con-
straints such as residual hardware impairments and channel
state information over multiple real-world scenarios are yet
to be analyzed in detail.
8
CONCLUSION
Tremendous advances in wireless technologies have raised
the concern of substantial energy consumption. In the fore-
seeable future, improving the energy efﬁciency of battery-
equipped smart devices in 5G networks will become one
of the main issues. This study was conducted in the context
of utilizing energy harvesting technology to prolong the life-
time of devices and networks. In this study, we taxonomized
the literature on the basis of several important parameters.
The key requirements to enable energy harvesting in 5G net-
works for providing guidelines to the new researchers are
discussed. Furthermore, some open challenges and future
research directions are presented. Finally, we conclude that
energy harvesting plays an important role in prolonging the
battery life of devices and networks by harvesting energy
from environmental sources and ambient RF signals. Thus,
serious attention must be given in addressing the discussed
challenges in the future.
ACKNOWLEDGMENT
Imran’s work is supported by the Deanship of Scientiﬁc
Research, King Saud University through Research Group
Project number RG-1435-051.
REFERENCES
[1]
A. ¨O. Ercan, M. O. Sunay, and I. F. Akyildiz, “Rf energy harvesting
and transfer for spectrum sharing cellular iot communications in
5g systems,” IEEE Transactions on Mobile Computing, vol. 17, no. 7,
pp. 1680–1694, 2018.
[2]
P.-V. Mekikis, E. Kartsakli, A. Antonopoulos, L. Alonso, and
C. Verikoukis, “Connectivity analysis in clustered wireless sensor
networks powered by solar energy,” IEEE Transactions on Wireless
Communications, vol. 17, no. 4, pp. 2389–2401, 2018.
[3]
S. A. A. Shah, E. Ahmed, M. Imran, and S. Zeadally, “5g for ve-
hicular communications,” IEEE Communications Magazine, vol. 56,
no. 1, pp. 111–117, 2018.
[4]
L. Wang, K.-K. Wong, S. Jin, G. Zheng, and R. W. Heath, “A
new look at physical layer security, caching, and wireless energy
harvesting for heterogeneous ultra-dense networks,” IEEE Com-
munications Magazine, vol. 56, no. 6, pp. 49–55, 2018.
[5]
M. Sinaie, P.-H. Lin, A. Zappone, P. Azmi, and E. A. Jorswieck,
“Delay-aware resource allocation for 5g wireless networks with
wireless power transfer,” IEEE Transactions on Vehicular Technology,
vol. 67, no. 7, pp. 5841–5855, 2018.
[6]
L. Guntupalli, M. Gidlund, and F. Y. Li, “An on-demand energy
requesting scheme for wireless energy harvesting powered iot
networks,” IEEE Internet of Things Journal, vol. 5, no. 4, pp. 2868–
2879, 2018.
[7]
X. Chen, W. Ni, T. Chen, I. B. Collings, X. Wang, and G. B.
Guanacos, “Real-time energy trading and future planning for ﬁfth
generation wireless communications,” IEEE Wireless Communica-
tions, vol. 24, no. 4, pp. 24–30, 2017.
[8]
N.-P. Nguyen, T. Q. Duong, H. Q. Ngo, Z. Hadzi-Velkov, and
L. Shu, “Secure 5g wireless communications: A joint relay selection
and wireless power transfer approach,” IEEE access, vol. 4, pp.
3349–3359, 2016.
[9]
S. Kishk, N. Almofari, and F. Zaki, “Distributed resource allocation
in d2d communication networks with energy harvesting relays
using stable matching,” Ad Hoc Networks, vol. 61, pp. 114–123,
2017.
[10] W.-K. Lee, M. J. Schubert, B.-Y. Ooi, and S. J.-Q. Ho, “Multi-
source energy harvesting and storage for ﬂoating wireless sensor
network nodes with long range communication capability,” IEEE
Transactions on Industry Applications, vol. 54, no. 3, pp. 2606–2615,
2018.
[11] M. Moradian and F. Ashtiani, “On the tradeoff between collision
and cooperation in a random access wireless network with en-
ergy harvesting nodes,” IEEE Transactions on Vehicular Technology,
vol. 67, no. 3, pp. 2501–2513, 2018.
[12] Y. Chong, W. Ismail, K. Ko, and C. Lee, “Energy harvesting for
wearable devices: A review, in press,” IEEE Sensors Journal, 2019.
[13] Q. Wu, W. Chen, D. W. K. Ng, and R. Schober, “Spectral and
energy-efﬁcient wireless powered iot networks: Noma or tdma?”
IEEE Transactions on Vehicular Technology, vol. 67, no. 7, pp. 6663–
6667, 2018.
[14] W. Wu, X. Yin, P. Deng, T. Guo, and B. Wang, “Transceiver design
for downlink swipt noma systems with cooperative full-duplex
relaying,” IEEE Access, vol. 7, pp. 33 464–33 472, 2019.
[15] Z. Xiao, L. Zhu, J. Choi, P. Xia, and X.-G. Xia, “Joint power
allocation and beamforming for non-orthogonal multiple access
(noma) in 5g millimeter wave communications,” IEEE Transactions
on Wireless Communications, vol. 17, no. 5, pp. 2961–2974, 2018.
Muhammad Imran is an associate professor at
King Saud University. His research interest in-
cludes MANET, WSNs, WBANs, M2M/IoT, SDN,
Security and privacy. He has published a num-
ber of research papers in refereed international
conferences and journals. He served as a Co-
Editor in Chief for EAI Transactions and Asso-
ciate/Guest editor for IEEE (Access, Commu-
nications, Wireless Communications Magazine),
Future Generation Computer Systems, Com-
puter Networks, Sensors, IJDSN, JIT, WCMC,
AHSWN, IET WSS, IJAACS and IJITEE.
Latif U. Khan is currently working as a faculty
member at Department of Telecommunication
Engineering, University of Engineering & Tech-
nology, Mardan, Pakistan. He received his MS
(Electrical Engineering) degree with distinction
from University of Engineering and Technology,
Peshawar, Pakistan in 2017. His research inter-
ests include analytical techniques of optimization
and game theory to edge computing and end-to-
end network slicing.


## Page 9


9
Ibrar Yaqoob (S’16, M’18, SM’19) is a research
professor at the Department of Computer Sci-
ence and Engineering, Kyung Hee University,
South Korea, where he completed his postdoc-
toral fellowship. He received his Ph.D. (Com-
puter Science) from the University of Malaya,
Malaysia. He is a guest/associate editor in vari-
ous Journals. He has been involved in a number
of conferences and workshops in numerous ca-
pacities. His research interests include big data,
mobile cloud computing, the Internet of Things,
and computer networks.
Ejaz Ahmed (S’12, M’17, SM’18) received his
PhD in Computer Science from University of
Malaya, Malaysia. He is Associate Technical
Editor/Editor of IEEE Communications Surveys
& Tutorials, IEEE Communications Magazine,
IEEE Access, Elsevier JNCA, KSII TIIS, and El-
sevier FGCS. He has served as Chair and Co-
chair in several international conferences. His
areas of research interest include Mobile Cloud
Computing, Mobile Edge Computing, Internet of
Things, Cognitive Radio Networks, Big Data, and
Internet of Things.
Muhammad Ahsan Qureshi received his PhD
from
University
of
Malaya,
Kuala
Lumpur,
Malaysia in 2016. His major work is on radio
propagation modeling for Vehicular Ad Hoc Net-
works (VANETS). He is currently serving as
Assistant Professor in the Faculty of Comput-
ing and Information Technology, University of
Jeddah, Khulais, Saudi Arabia. His research in-
terests include Wireless Communication, Trafﬁc
Management, Green Computing and Internet of
Vehicles.
Arif Ahmed received his M.Tech. degree in com-
puter science and engineering from the National
Institute of Technology Silchar, India, in 2014. He
worked as a visiting scientist at the Centre for
Development of Advanced Computing, Mumbai,
India, from 2014 to 2015. His research inter-
ests are in the ﬁeld of mobile cloud comput-
ing, fog computing, software-deﬁned networking,
and mathematical modeling.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
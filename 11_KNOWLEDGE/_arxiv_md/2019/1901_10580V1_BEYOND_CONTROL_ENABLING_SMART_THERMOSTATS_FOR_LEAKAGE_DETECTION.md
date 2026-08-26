---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1901.10580v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1901.10580v1_Beyond_Control__Enabling_Smart_Thermostats_For_Leakage_Detection

> Source: 1901.10580v1_Beyond_Control__Enabling_Smart_Thermostats_For_Leakage_Detection.pdf

> Pages: 21

---


## Page 1


1
Beyond Control: Enabling Smart Thermostats For Leakage Detection
MILAN JAIN, IIIT-Delhi, India
MRIDULA GUPTA, University of California Davis, USA
AMARJEET SINGH, IIIT-Delhi, India
VIKAS CHANDAN, Pacific Northwest National Laboratory, USA
Smart thermostats, with multiple sensory abilities, are becoming pervasive and ubiquitous, in both residential and commercial
buildings. By analyzing occupants’ behavior, adjusting set temperature automatically, and adapting to temporal and spatial
changes in the atmosphere, smart thermostats can maximize both - energy savings and user comfort. In this paper, we study
smart thermostats for refrigerant leakage detection. Retail outlets, such as milk-booths and quick service restaurants set up
cold-rooms to store perishable items. In each room, a refrigeration unit (akin to air-conditioners) is used to maintain a suitable
temperature for the stored products. Often, refrigerant leaks through the coils (or valves) of the refrigeration unit which
slowly diminishes the cooling capacity of the refrigeration unit while allowing it to be functional. Such leaks waste significant
energy, risk occupants’ health, and impact the quality of stored perishable products. While store managers usually fail to
sense the early symptoms of such leaks, current techniques to report refrigerant leakage are often not scalable. We propose
Greina - to continuously monitor the readily available ambient information from the thermostat and timely report such leaks.
We evaluate our approach on 74 outlets of a retail enterprise and results indicate that Greina can report the leakage a week in
advance when compared to manual reporting.
CCS Concepts: • Information systems →Decision support systems; • Human-centered computing →Ubiquitous
and mobile computing systems and tools; • Applied computing →Operations research.
Additional Key Words and Phrases: Smart Thermostat; Refrigerant Gas Leakage; Ambient Sensing; Fault Detection; Refrigera-
tion Unit
ACM Reference Format:
Milan Jain, Mridula Gupta, Amarjeet Singh, and Vikas Chandan. 2019. Beyond Control: Enabling Smart Thermostats For
Leakage Detection. Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. 3, 1, Article 1 (March 2019), 21 pages. https:
//doi.org/0000001.0000001
1
INTRODUCTION
Refrigerant leakage is a common mechanical fault in compressor based appliances which are primarily used for
air-conditioning and refrigeration purposes [7]. The puncture hole often starts as a pinhole leak and becomes
bigger when goes undetected. Due to the loss of refrigerant, compressor (a component within the RU) works
with reduced efficiency and takes more time than the usual to cool the room; thus, wasting significant energy. In
addition to that, the leakage exposes tenants to refrigerant which is extremely dangerous for their health [1].
The consequences of refrigerant leakage are even worse for retail outlets who set up cold-rooms to preserve
perishable food items (usually at 5◦C-8◦C), and the stored product goes bad due to improper cooling by the RU
during the leakage. Early detection of such leaks can benefit the retail enterprises in - (1) increasing their profits
This work was done in collaboration with Zenatix Solutions Pvt. Ltd. We would like to thank TCS Innovation Lab for Ph.D. fellowship to the
first author, the administration of the retail enterprise to allow us to collect data, and all the outlet managers and the technicians to help us
during the data collection.
Authors’ addresses: Milan Jain, IIIT-Delhi, Delhi, India; Mridula Gupta, University of California Davis, Davis, California, USA; Amarjeet
Singh, IIIT-Delhi, Delhi, India; Vikas Chandan, Pacific Northwest National Laboratory, Richland, Washington, USA.
© 2019 Association for Computing Machinery.
This is the author’s version of the work. It is posted here for your personal use. Not for redistribution. The definitive Version of Record was
published in Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, https://doi.org/0000001.0000001.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.
arXiv:1901.10580v1  [cs.CY]  22 Jan 2019


## Page 2


1:2
•
M. Jain et al.
Normal RU 
Operations
Faulty RU
Downtime
(a) Gas leakage started on March 21, but
manager kept using the RU for a week
and complained on March 29 when it
stopped cooling.
(b) During daytime store manager fre-
quently visits the cold-room which leads
to high temperature in working hours.
(c) In winters (December 2016 - March
2017), room temperature stays in a lower
range as compared to summers.
Fig. 1. [Left] Delay in reporting refrigeration leak led to complete shutdown of store operations for 2-3 days. [Middle and
Right] Room temperature depends on the activities of store manager and seasonal environmental changes.
by reducing the energy wastage, (2) avoiding leakage of hazardous refrigerant in the open environment, and
(3) maintaining the product quality [13, 16, 17, 22].
Unfortunately, store managers usually lack essential skills to sense the leakage at an early stage, and undetected
leaks widen with time as RU remains functional during the leakage. At breakdown point, RU stops cooling
followed by a complete shutdown of the outlet for several days. Figure 1a depicts one such scenario where store
manager reported the problem when RU broke, and the store went out of operations. In addition to repairing
cost, the owner also dealt with the staling of stored products and business loss owing to the downtime. Current
techniques for leakage detection are either direct or indirect [71]. Direct methods, such as Halide leak detector,
require an expert to use the device with certain precautions for on-spot leakage detection [6, 31, 43]. On the
other hand, indirect techniques need specialized sensors to monitor temperature, pressure, and mass flow rate at
multiple points inside the appliance [20, 53, 57]. As pressure and mass flow sensors are more expensive than
temperature sensor, several studies focused on limiting the number of sensors for leakage detection [21, 71].
However, even with the limited sensors, Yoo et al. [71] required temperature sensors at five points inside the
system - (1) air inlet of indoor unit, (2) air inlet of outdoor unit, (3) evaporator midpoint, (4) condenser midpoint,
and (5) compressor discharge point. Such an extensive sensor installation (that too within the appliance) often
limits indirect techniques to laboratory setup and considered as an expensive and unscalable solution to the
problem.
In this paper, we reinforce smart thermostats with Greina1 - a framework that observes deviations in the
measured temperature from the estimated temperature to detect refrigerant leakage. The estimates come from
a lumped parameter thermal model whose parameters are tuned to a particular room environment by the
ambient information sensed by the thermostat. Smart thermostats are (1) plug-n-play - no need of technician for
installation, (2) allow remote sensing of RU, (3) never intervene in the daily routine of the store managers, and
(4) anticipated to increase by 400% in next couple of years [38]. Given the benefits, studies in the past explored
smart thermostats for user feedback [30], occupancy detection [36], energy-efficient control [42], among many
other applications. However, to the best of our knowledge, no one has studied smart thermostats for leakage
detection. We believe enhancing smart thermostats for leakage detection presents a genuinely low-cost and
scalable solution for the problem.
Despite all the benefits, one must also note that the overall problem is non-trivial and exhibits multiple
challenges. Room temperature is sensitive to the actions of outlet manager (Figure 1b) and outside weather
1Greina is an Icelandic word that means to identify.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 3


Beyond Control: Enabling Smart Thermostats For Leakage Detection
•
1:3
conditions (Figure 1c), and both these parameters differ significantly across the outlets. Even within a store, the
daily routine of the manager, climatic conditions, and fitness level of an appliance change considerably with time.
To consider both temporal and spatial variations, Greina utilizes a first-order thermal model which simulates the
room temperature while considering the influence of outlet manager and climate outside the room. Greina collects
weather data through a cloud-based weather service, and monitors user activity through a door sensor. With time,
as the framework receives more and more clean data, it keeps updating the model parameters to accommodate
temporal changes in the building’s thermal behavior. To gather clean data for the learning phase, Greina does
not consider those days which were identified as leaking while monitoring the RU. In the initial stages, when
sufficient clean data is unavailable to tune the model parameters, Greina benefits from transfer learning and uses
the parameters of a contextually ‘similar’ outlet to simulate the room temperature. Transfer learning ensures that
the proposed framework is ready-to-work from the day of installation. Eventually, Greina compares the estimates
from the tuned thermal model with sensor measurements and when the actual temperature is sufficiently above
the estimate, the system raises a red flag.
Of course, not every red flag is a leakage flag. Room temperature can be higher than the estimates even
when RU is working fine (false positive), and vice-a-versa, the framework might confuse the initial symptoms
of leakage with the noise generated from manual interventions (false negative). For instance, in Figure 1a, the
room temperature is in the range of 8◦C-10◦C in the initial stages of the refrigerant leak, akin to temperature
variations due to tenants’ activities in Figure 1b. If misclassification is a false negative (misinformed that RU is
fine), then repairing will get delayed until the outlet manager identifies the leakage. However, if misclassification
is a false positive (misinformed that RU broke), then the company might end up paying a significant amount to
their maintenance contractor for the unnecessary visits. While such visits are immoderate, they are annoying for
the store manager and disruptive to the daily operations. Henceforth, Greina employs CUSUM (Cumulative Sum
Control) technique to ensure that the user gets notified only when the system is confident about the leakage.
We evaluate Greina using the data collected from 74 outlets of a retail enterprise for one year. For ground
truth verification, we use fault logs as reported by the servicing company after addressing the fault. Our results
indicate that Greina is comparable or better than manual reporting. The proposed framework can reduce average
reporting delay by 5-6 days, when compared to manual reporting. In other words, even if outlet managers could
use the leakage detectors (such as Halide leak detector), they would have delayed the repairing by almost a week.
We couldn’t compare Greina with indirect methods (of leakage detection) because proposed techniques require
specialized sensors to monitor temperature at multiple points within the RU.
Given the energy-saving features and other advancements, smart thermostats are anyways going to replace
traditional thermostats very soon. As of now, thermostats can monitor room temperature, tenants’ daily activities 2,
and even upload the sensed information to the cloud. Location-based detailed weather information is readily
available from several cloud-based climate monitoring applications. By combining the two pieces of information,
we can use Greina for leakage detection without instrumenting the appliance. In addition to being scalable,
the proposed approach is reliable enough to maintain food quality and generate minimal false alarms. Finally,
Greina requires minimal (or no) intervention from the store manager and ensures non-interruptive working
hours. Currently, in collaboration with an energy-analytics based venture, we are working on the deployment of
proposed thermostats across all the 74 outlets which were considered as part of this study.
2
RELATED WORK
Anomaly detection is an active area of research with extensive literature in numerous domains and applications [9,
37]. One such problem is fault detection and diagnosis (FDD) where the objective is first to identify a malfunctioned
2Though, in this study, we used door sensor to monitor human activities, Appendix A discusses an extended thermal model which replaces
door sensor with the motion sensor of the smart thermostat.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 4


1:4
•
M. Jain et al.
appliance followed by a root-cause analysis to diagnose the problem [24, 29]. Usually, the partial or complete
failure of the hardware (present in the equipment) brings down the whole system. Though the literature on
fault detection in mechanical units is considerably extensive, we will limit the scope of this survey only to
compressor-based appliances.
2.1
Fault Detection Frameworks
Typically, fault detection frameworks for compressor-based appliances are designed either for Refrigeration
Units [5, 65] or Heating, Ventilation, and Air Conditioning Units (HVAC) [7, 15, 68, 72]. Irrespective of the type
of appliance, most fault detection engines are based on a conventional design - simulate a baseline and compare
with the measured signal (mostly energy) to mark any deviations due to the fault [10, 18, 23, 45, 48, 51]. O’Neil
et al. [50] simulated the energy consumption through a building simulation framework, EnergyPlus [12], and
compared with actual energy consumption data to identify unacceptable performance. Mavromatidis et al. [44]
computed baseline energy consumption through an artificial neural network model and used the baseline to
detect faults in supermarket refrigerators. Li et al. [41] studied the correlation between electrical signals and the
common faults for roof-top air conditioners by conducting a series of experiments. Srinivasan et al. [61] proposed
an energy model to pick anomalies in the power signature of supermarket refrigerators.
Studies also monitored different other parameters to develop a black box model for fault detection [28, 69, 70].
Keres et al. [34] observed compressor frequency to identify a faulty refrigerant unit. Porter et al. [56] collected
actual operating parameters from a set of microsystem sensors installed throughout the refrigeration and
compared with ideal conditions of the system for fault detection. Payne et al. [53, 54] monitored temperature
at nine points within an air-conditioner for a self-trained fault-free model and then a data-clustering approach
to segregate faulty instances. Similarly, Kulkarni et al. [39] designed a random forest binary classifier to detect
issues in refrigeration cases by observing temperature and defrost state within supermarket refrigeration cases.
While most of the above-mentioned studies focused only on detecting ‘abrupt’ faults, none of them looked
into the problem of refrigerant leakage. Though such a fault detection engine would confirm the presence of a
fault, the engine won’t label the fault. In the absence of labeling, we couldn’t compare Greina with any of the
above-mentioned generic fault detection frameworks3.
2.2
Leakage Detection Frameworks
Specifically for leakage detection, exiting systems are typically categorized as direct and indirect methods.
2.2.1
Direct Methods. In direct methods, typically a technician visits the site and uses a leakage detector [6, 43]
to confirm the leak. Hailey detector [31] is one such widely used leak detector in which flame changes the color
when the refrigerant is present in the environment. Parekh [52] proposed composition of fluorescent, alkyl
substituted perylene-dye, and a polyhalogenated hydrocarbon refrigerant to visually detect refrigerant leakage.
Though these detectors are accurate, one must use them with certain precautions. For instance, we cannot use
Hailey detector with hydrocarbon refrigerants. Moreover, the effectiveness of direct methods primarily relies on
manager’s ability in timely detecting the leakage.
2.2.2
Indirect Methods. Alternatively, in indirect methods, studies often monitor multiple parameters at different
points within the appliance for leakage detection [19, 32, 33, 46, 47, 58, 63]. Taylor et al. [64] designed a neural
network to analyze data from multiple monitoring alarms to predict refrigerant leakage. Rossi et al. [59] proposed
a statistical rule-based leakage detection technique which could detect 5% loss of refrigerant through extensive
3If we would have considered all anomaly instances as leakage, our analysis would have shown high false alarm rate for any generic fault
detection framework. Therefore, though we had data to implement some of these techniques, we couldn’t compare the performance of any
generic fault detection framework with Greina in our evaluation (Section 4).
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 5


Beyond Control: Enabling Smart Thermostats For Leakage Detection
•
1:5
Simulator
Greina
Real-World 
Environment
Tr
(t+1) = µr ×Tr
(t) + µe ×Te
(t) + µdr × Sdr
(t) + µru × Sru
(t) +ηr
Learn
Monitor
Sensed
Simulated
Server
Greina
(a) Greina is a two-step process. The proposed framework first learns the
typical temperature profile of the room followed by monitoring the RU for
refrigerant leakage.
Fit
May be Fit
Refrigerant 
Leaking
May be 
Leaking
br < 24
br ≥ 24
br < 12
br < 36
br ≥ 12
br < 12
br ≥ 36
(b) For each room r, Greina maintains a bucket
variable (br ) to label the RU at each hour.
Fig. 2. [Left] Greina takes ambient information from the smart thermostat and weather conditions from a third-party
cloud-based weather server to tune the parameters of a lumped thermal model. Tuned thermal model simulates the room
temperature for leakage detection. To incorporate temporal changes in the environment, Greina regularly updates the model
parameters. [Right] From data, we observed that if the temperature within a room is consistently beyond the estimates for
36 hours, then there are high chances of refrigerant leakage in the RU.
instrumentation. Breuker et al. [8] studied temperature at nine different locations and relative humidity to
characterize soft faults (such as loss of refrigerant) and their impact on the operations of rooftop air conditioners.
Since the majority of leakage detection studies [25, 40, 49] assume steady-state, Kim et al. [35] proposed a
methodology for developing a steady-state detector for any generic vapor-compression system. Steady-state in
itself is a misleading term because parameters of a vapor-compression system are dynamic in real-world [35].
Therefore, the study recommended inclusion of all leakage detection features (for best results) which makes the
overall approach expensive due to extensive instrumentation of the appliance.
To minimize the number of sensors and sensing points, Fisera et al. [20, 21] developed an energy consumption
model by monitoring nine parameters (including relative humidity and carbon-dioxide level) to distinguish
anomalous and degradation events. In a patented technology, Suzuki et al. [62] compared theoretical heat
dissipation of the condenser with the actual temperature difference (in the condenser) for leakage detection. In
the same direction, Yoo et al. [71] monitored temperature difference between inlet air and midpoint of the heat
exchanger to detect the refrigerant charge level. Though stated approaches require less number of sensing points,
invasive sensing often limits their evaluation to a controlled environment. Consequently, the efficacy relies on
the validity of assumptions from the controlled environment to a real-world scenario.
3
APPROACH
In Greina, every outlet goes through a two-step process - (1) learn the normal behavior, and (2) monitor refrigera-
tion unit for leakage, as shown in Figure 2.
3.1
Learn Normal Behaviour
In a typical room r, the change in temperature, in a given time interval τ (in seconds), primarily depends on the
heat transferred by the weather outside the room, the heat added by the open door, and the heat extracted by the
refrigeration unit (Equation 1).
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 6


1:6
•
M. Jain et al.
(T (t+1)
r
−T (t)
r ) × Cr
τ
= Kr
e × (T (t)
e
−T (t)
r ) + (Qdr × S(t)
dr ) + (Qru × S(t)
rur ) + ηr
(1)
Here, T (t)
r
and T (t)
e
denote the average room and external temperature in the last time interval τ (between t
and t −1), respectively. Cr is the thermal capacity of the room, and Kr
e is the heat transfer coefficient between
room and external weather conditions. We derived the model from Bacher et al. [2].
When supply in the front runs out, the manager opens the room to get the fresh stock and S(t)
dr denotes the
state of door (open/close) at time t. Given that RU is a two-state appliance - (1) compressor on, and (2) compressor
off, where compressor is the major power consuming component of RU, S(t)
rur is the state of RU at time t.
Correspondingly, Qdr and Qru denote the amount of heat added through the door, and heat extracted by the
refrigeration unit, respectively. ηr is the thermal noise introduced by the random events.
µr = 1 −Kr
e ∗τ
Cr
,
µe = Kr
e ∗τ
Cr
,
µdr = Qdr ∗τ
Cr
,
µru = Qru ∗τ
Cr
,
η′
r = ηr ∗τ
Cr
(2)
In state space representation, we can lump the parameters (as shown in Equation 2) and rewrite the thermal
model as Equation 3. Greina learns the model parameters (θ =< µr, µe, µdr, µru,η′
r >) through linear regression
while using the data streams of room temperature (Tr), external temperature (Te), door status (Sdr), and RU status
(Srur). Tuning the parameters of a physics-based thermal model by using the real-world data is called Grey Box
Modelling and widely practised by the researchers in several domains [14]. As tuning involves sensor data, the
model with adjusted parameters represents an approximate thermal behaviour of the room.
T (t+1)
r
= µr ×T (t)
r
+ µe ×T (t)
e
+ µdr × S(t)
dr + µru × S(t)
rur + η′
r
(3)
Greina tunes model parameters every month through Stochastic Gradient Descent [55]. The online learning
ensures that model adapts to recent changes occurring in the environment, without forgetting the existing
knowledge. Now, to tune the model parameters, the proposed framework require clean data - data when the
refrigeration unit was working fine. To gather clean data for the learning phase, Greina does not consider those
days which were identified as leaking during the monitoring phase. For instance, if Greina labeled refrigeration
unit as Refrigerant Leaking for five days in the last month, the learning module won’t consider data from those five
days to tune the model parameters. The rationale behind this is that if RU was unable to keep room temperature
within limits for more than 36 hours consecutively, it was not an ideal situation and there was a problem. During
those five days, the problem could have been Refrigerant Leakage (true positive), or an ongoing maintenance
(false positive); either way, those days are not ideal (or regular) days for the training. Thus, we discard those from
the learning data and only use clean data.
Initially, we specified two key features of Greina - (1) it uses readily available information from the smart
thermostat, and (2) it can start monitoring the RU without waiting for the sensor data for a long time. Though the
proposed framework can collect room temperature (Tr) and door status (Sdr) information from the thermostat,
and external temperature (Te) from any third-party weather server, the refrigeration state (Srur), which typically
requires appliance-level monitoring is unavailable to the framework. In addition to that, waiting for clean data for
a long time in the initial stages of deployment can significantly delay the monitoring process. Greina leverages
domain advancements to fulfill these requirements.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 7


Beyond Control: Enabling Smart Thermostats For Leakage Detection
•
1:7
ALGORITHM 1: Ranking Algorithm
/* Dh
r indicates the median of total
number of door opening instances
occurred in the hth hour for the rth
room across all the days. h ∈[1, 24]
*/
Input: Dr where r is the ID of new room
Output: Parameters < µr, µe, µdr, µru,η′
r > of
most ‘similar’ outlet (room r ∗)
/* Score indicates the ‘similarity’ in
the door opening patterns of two rooms
across the day.
*/
Compute Score:
Si = ∥Di −Dr∥2, ∀i ∈{available outlets};
/* Select the room number with minimum
score
*/
Select ‘Similar’ Outlet:
r ∗= argmin
i
(S)
10
15
20
25
30
Similarity (in door opening events)
1
2
3
4
5
Similarity (in temperature)
Fig. 3. If the managers of two rooms have ‘similar’ routine,
then there are good chances that the hourly temperature
profile of those rooms will also be ‘similar’.
3.1.1
State of Refrigeration Unit. Jain et. al. [30], proposed a classification based algorithm to determine com-
pressor state from the room temperature. The intuition was to first identify compressor on and off events from
the temperature data followed by event sequencing to estimate the state vector for RU. When compressor turns
on, the room temperature quickly goes down due to the addition of cold air, and when compressor turns off, the
room temperature shoots up due to thermal leakage. The estimation algorithm (EA) uses k-means to segregate
sudden increase and sudden decrease in room temperature (in τ time) from normal variations. On the segregated
events, the algorithm applies sequencing and recreates the compressor cycles of the refrigeration unit. We employ
estimation algorithm to represent RU state as a function of room temperature (Srur = EA(Tr)) and learn the model
parameters. One must note that Greina estimates state vector only when RU is working fine because learning
requires clean data.
3.1.2
Parameter Initialization. When a store comes under monitoring, there exists no data to learn the model
parameters for the particular outlet. In such a scenario, Greina uses the parameters of a contextually ‘similar’ store
to monitor the refrigeration unit for leakage detection until sufficient clean data from the new outlet is available
to update the model parameters. To find ’similar’ outlet, we compare the average daily routine of managers in
each store. We do not use room temperature directly to measure ‘similarity’ because it is possible that RU is faulty
at the time of installation. The rationale for using daily schedule is that out of all the factors, room temperature
is most sensitive to managers’ activities. While the efficiency of the refrigeration unit, building insulation, and
other building characteristics are static and change over a long span of time (in months or years), the schedule of
any manager is stochastic. Therefore, if the managers of two outlets have ‘similar’ routine, there are high chances
that the hourly temperature profile will also be ‘similar’ for those outlets (Figure 3). Our ranking algorithm
(Algorithm 1) then sorts all the available stores based on the ‘similarity’ in the daily routine of their respective
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 8


1:8
•
M. Jain et al.
managers. We use l2-norm to measure the similarity. When there exists no ‘similar’ outlet, the monitoring module
(of Greina) uses 10◦C as a default threshold 4.
3.2
Monitor for Leakage Detection
At the end of each hour, the tuned thermal model estimates typical temperature profile of the room (˜Tr), for
the framework to look for refrigerant leakage. However, it is infeasible to estimate the temperature profile
which perfectly aligns with the actual temperature profile, and the reason lies in the control strategy embedded
within the internal thermostat of a typical refrigeration unit. The inbuilt thermostat of an RU uses on hysteresis
as an upper threshold and off hysteresis as a lower threshold. When room temperature goes beyond the on
hysteresis, the thermostat turns on the compressor, and the room temperature starts decreasing. Subsequently,
when the room temperature reaches the off hysteresis, the thermostat turns off the compressor and allows room
temperature to increase up to on hysteresis. However, in real-world, the temperature readings from the inbuilt
thermostat of RU differs significantly from the deployed sensor measurements. As it is difficult for the external
temperature sensor to match the temperature readings as sensed by the inbuilt sensor, it is also hard to accurately
predict room temperature at every time instance. If we observe deviations in the raw temperature profiles (Tr
and ˜Tr) for anomaly detection, the misalignments will lead to false conclusions 5.
Instead, Greina analyses hourly mean temperature to mark if the RU in a particular hour is anomalous or
not. In any hour, the thermostat tries to achieving a temperature which is the average of on and off hysteresis.
For instance, in the current scenario, outlets use 5◦C as off hysteresis and 8◦C as on hysteresis to maintain an
average temperature of 6.5◦C in the room. Though the temperature at any time instance may misalign, the
average temperature in that hour should remain close to 6.5◦C. Thus, Greina first computes mean actual (T h
r ) and
estimated ( ˜T h
r ) temperature in Equation 4 followed by decision boundary for leakage detection in Equation 5.
T h
r =
Í
h Tr
(3600/τ),
˜T h
r =
Í
h ˜Tr
(3600/τ)
(4)
ˆT h
r = ˜T h
r + σh
r
(5)
Here, ˜T h
r is the estimated mean temperature, σh
r is the standard deviation in Tr in an hour h, and ˆT h
r denotes
the estimated decision boundary for the particular hour h and room r. If the sensed mean temperature (T h
r )
is beyond the estimate ( ˆT h
r ), then we mark that specific hour anomalous (Algorithm 2). Furthermore, to gain
confidence that deviations are due to leakage, Greina applies CUSUM (Cumulative Sum) control strategy [67] and
maintains a bucket variable (br) to monitor consecutive such anomalous instances. Whenever room temperature
goes beyond the decision boundary, the monitoring module increments the br value by one (Algorithm 2). For
every consecutive hour, when room temperature is within the estimated limits, br decreases by one unit. If room
temperature stays below the decision boundary for consecutive hmon hours, Greina assumes RU is working fine
and resets the bucket. In case of missing information, br remains unchanged.
3.2.1
Label the Refrigeration Unit. In the final step, Greina labels the refrigeration unit based on its bucket value
(br ) in the particular hour h. Our analysis indicates that if the room temperature is beyond the estimated decision
boundary for consecutively 36 hours, then there are maximum chances of refrigerant leakage. Though we learned
the current transition thresholds from the data, we can always adjust these settings based on user requirements.
4The refrigeration units are supposed to maintain a temperature range of 5◦C-8◦C in the cold-rooms. Typically, temperature remains higher
(than the limits) during the working hours, and within the limits during the non-working hours. The 10◦C is the median value for both
working and non-working hours.
5We discuss misalignment in detail in Section 5 - Discussions
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 9


Beyond Control: Enabling Smart Thermostats For Leakage Detection
•
1:9
ALGORITHM 2: Update Bucket
/* Sensed and Estimated Room Temperature
*/
Input: T h
r , ˆT h
r , hmon, anlock, br
Output: br
/* Update Bucket Value
*/
if T h
r > ˆT h
r then
br = br + 1;
anlock = hmon; // Reset the lock
else if T h
r ≤ˆT h
r then
anlock = anlock −1;
if anlock == 0 then
br = 0; // Reset the bucket
else
br = br −1;
Hour of Day
0
2
4
6
8
Absolute Error ( C)
Hour of Day
0
2
4
6
8
Absolute Error ( C)
Fig. 4. During working hours, the outlet managers are much
more noisy than the non-working hours.
Manual
Greina
0
10
20
30
Number of Days
(a) Greina performed better or
comparable to manual report-
ing in leakage detection.
Instance#
10
0
10
20
30
40
Number of Days
(b) In 25 instances both Greina and manual
reported correctly identified the fault. In 19
out of 25, Greina detected the leakage before
store manager.
Outlet#
10
0
10
20
30
40
Number of Days
(c) Due to delay in fixing the fault and backlog
complaints, Greina detected the fault after
manual logging in six instances.
Fig. 5. Our analysis indicates, a simple yet powerful framework, Greina reduced the average leakage reporting delay by 5-6
days, significant enough to avoid energy wastage and maintain food quality by timely repairing the refrigeration unit.
4
EVALUATION
For the study, we deployed a customized thermostat and power meter across 74 outlets of a retail enterprise. From
July 2016 until June 2017, thermostats collected room temperature and door information from the cold-rooms,
and energy meters gathered appliance level power consumption. Every cold room is 9 ft wide, 9 ft long, and 8 ft
high. With thick walls and doors, these highly insulated cold rooms can maintain storage temperature anywhere
between −2◦C and 5◦C. We keep thermostats close to the blower fan (of the RU), because that allows Greina to
focus more on the output of refrigeration unit and less on the thermal noises in the environment. We monitored
weather conditions (in the region) through an API of a cloud-based weather service [66]. The outlets were located
in a city where outside temperature usually stays between 21◦C and 37◦C, all around the year. The retail enterprise
maintains a log of calls from the store managers regarding the complaint in their cold-rooms. We used the fault
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 10


1:10
•
M. Jain et al.
logs for ground truth verification. During the study period, repair person identified 42 cases of refrigerant leakage
across 39 outlets, in addition to several other defects. In remaining 35 stores, neither manager nor repair person
mentioned any instance of refrigerant leakage in the logs during the study period. In one instance, the outlet
manager called a local repair person instead of reporting the fault to the authorised maintenance contractor.
4.1
Evaluation Metrics
We evaluate Greina primarily on two aspects - (1) model accuracy in estimating the decision boundary (ˆTr), and
(2) minimising the delay in reporting refrigerant leakage.
4.1.1
Modelling Error. For each hour, we compute mean absolute deviation (denoted by eh) in measured (Tr) and
estimated temperature (˜Tr) to quantify the accuracy of model parameters in simulating the room temperature in
an hour h (Equation 6).
eh =
Í
h | ˜T (t)
r
−T (t)
r |
(3600/τ)
(6)
rdm = dtm −dts
rdд = dtд −dts
(7)
4.1.2
Delay in Reporting the Leakage. We labelled all the leakage instances by start date (dts) - when symptoms
became visible in the data, and end date (dte) - when repair person repaired the leak. Reporting delay is the
number of days between the start and the leakage reporting dates. Equation 6 computes reporting delay for store
manager (rdm) and Greina (rdд). Here, dtm and dtд are the dates when the manager and Greina reported the leaks,
respectively.
4.2
Model Validation
Across all the outlets, our analysis indicates that the model tuned with clean data (when RU was fit) can simulate
the room temperature with a mean absolute error of 2◦C (with σ = 0.9◦C), as shown in (Figure 4). Estimation
error is primarily due to misalignment and noise due to random events - such as leaving the door open, refilling
the food products at a higher temperature. For the same reason, the error is usually higher during the operational
hours, as also evident from the bumps. Erroneous estimations might mislead Greina that room temperature is
above the estimated temperature, but adding standard deviation in Equation 5 minimises such instances.
4.3
Results and Analysis
In the study period, we noted 42 instances in the logs where either the store manager or the repair person
mentioned the keywords - gas6 and leakage. In 4 cases, though the records had the gas keyword, no leakage
occurred in the refrigeration unit at that time, as validated by the store manager and the data. Furthermore,
refrigerant leakage shows physical symptoms, such as water dripping and ice formation, which are visible
before any leakage pattern in the temperature data. In 3 such instances, outlet managers quickly intimated the
maintenance contractor to fix the refrigeration unit and Greina had no data to analyse the symptoms for leakage
detection. In remaining 35 instances, the proposed framework correctly identified 25 leaks and failed to detect
leakage in the remaining scenarios. While few of them were genuine system failures, others happened due to
ungovernable circumstances -
(1) Too Early to Detect: During the learning phase, Greina borrows model parameters from a ‘similar’ outlet.
While Greina successfully identified six leaks when knowledge transferred from one store to another, it
failed twice.
6local people often use the word ‘gas’ to refer refrigerant
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 11


Beyond Control: Enabling Smart Thermostats For Leakage Detection
•
1:11
Hour of Day
0.0
0.2
0.4
0.6
0.8
1.0
Energy Consumption (kWh)
Normal Operations
Faulty Operations
(a) Leakage increases the power con-
sumption of RU by 4x and 2x during
non-working and working hours, re-
spectively.
Hour of Day
1.0
0.5
0.0
0.5
1.0
1.5
Energy Wastage (kWh)
(b) Within reporting delay period (dд
m),
outlets wasted significant energy in
both working and non-working hours
of the day.
Outlet#
0
10
20
30
Energy Wastage (kWh)
(c) The company could have saved 5-6
kWh energy every day during dд
m pe-
riod which is twice the daily consump-
tion.
Hour of Day
8
9
10
11
12
Mean Temperature ( C)
Normal Operations
Faulty Operations
(d) When compared with normal oper-
ations, the temperature increased by
2◦C-5◦C across the day, during refrig-
erant leakage.
Hour of Day
0.0
2.5
5.0
7.5
10.0
12.5
15.0
Temperature Rise ( C)
(e) The increase in temperature is evi-
dent across all the outlets; thus, risking
perishable items every day during the
reporting delay.
Outlet#
0
2
4
6
8
10
12
Temperature Rise ( C)
(f) Early detection of refrigerant leakage
by Greina had kept the rooms 5◦C-6◦C
colder during the reporting delay period
(dд
m).
Fig. 6. Beyond being accurate in detecting the gas leakages, Greina can also save energy and keep the room 5◦C-6◦C colder,
every day during the dд
m period - the number of days between manual reporting and leakage detection by Greina.
(2) Improper Learning: Outlet managers generate significant thermal noise in the room through their
dynamic and random activities. While the model can deal with such noise with a substantial amount of data,
Greina incorrectly learns the model parameters when the data is insufficient. As the occupants’ behaviour
differs significantly across the outlets, there exists no definite way to compute - How much data will suffice
to train the model correctly?
(3) Noisy Sensor: In two cases, we noticed that a faulty sensor was providing incorrect temperature readings
which resulted in false negative. However, we believe that these issues are solvable with better governance
around the deployment.
(4) Low on Refrigerant: Quite often, a refrigeration unit is actually low on refrigerant (due to heavy usage),
and there exists no leakage. In such scenarios, though temperature remains in a higher range as RU is not
running at the full capacity, but differs from the temperature patterns as in the case of refrigerant leakage.
Therefore, when RU was low on refrigerant in 3 such instances, the technician mentioned gas top up in the
log; however, Greina failed to find the symptoms of refrigerant leakage.
Furthermore, Greina reported only 6 instances of false positives - marked RU as leaking while it was working
fine. In four out of six cases, either store manager or technician shut down the refrigeration unit for construction
and the repairing work. As the shutdown was unexpected, Greina confused the rise in room temperature with
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 12


1:12
•
M. Jain et al.
Power (kWh)
Temperature ( C)
(a) When ice forms due to other reasons
(such as dirty filters), the peak power
consumption remains consistent.
Power (kWh)
Temperature ( C)
(b) Before failure, motor within the RU
draws high current which increases the
peak power consumption of RU by 1.5x.
Outlet#
0
5
10
15
20
25
30
35
40
Number of Days
(c) Even though outlet managers timely
report the leakage, the technicians intro-
duce a significant delay in repairing the
RU.
Fig. 7. [Left and Middle] In addition to leakage, Greina also reported 28 instances of ice formation and motor failure during
the study. [Right] Greina can be extended to monitor the efficiency of maintenance contractor in repairing a reported fault.
leakage and marked the refrigeration unit as leaking. In remaining two instances, RU broke abruptly due to an
electrical fault and stayed down until a technician came to fix it. Consequently, room temperature went high and
Greina raised a refrigerant leakage flag. As the company, maintenance contractor, and the outlet managers are
usually aware of these situations; we believe these flags are harmless. In addition to this, Greina also pinpointed a
case of refrigerant leakage where store manager called an unauthorised technician to repair the RU and didn’t
notify the enterprise. Though such cases are rare, they are a serious concern for the company.
Beyond Accuracy
Though accuracy is essential, minimisation of reporting delay is a more significant concern for the stakeholders
because the delay is directly proportional to energy wastage, health hazards, and product wastage. In our analysis,
we noted an average reporting delay of seven days for Greina, while managers had a mean reporting delay of 12
days (Figure 5a). In 19 out of 25 instances, Greina detected leakage before the store manager (Figure 5). In eight
cases, the difference was as high as 10-30 days. The early detection of leakage exhibits several benefits.
Minimise Energy Wastage. In Section 1, we presented a scenario (Figure 1a) when refrigeration unit had a gas
leakage, and outlet manager kept using the RU for more than a week. While such situations are common across
all the stores, we noticed significant energy wastage in doing so. Figure 6a compares hourly energy consumption
during the normal operations with faulty operations, when RU has a leakage. There are two essential takeaways -
(1) energy consumption increases significantly during the working hours (almost 4x), and (2) energy consumption
is very high when refrigeration unit is leaking (around 7x during the non-working hours).
dд
m = dtд −dtm
(8)
While the activities (or routine) of store managers are hard to change, Greina seems robust enough to minimise
the energy wastage due to gas leakage. Figure 6b compares the hourly energy wasted in the dд
m period - the
number of days between the reporting dates of manager and Greina (Equation 8). Our analysis indicates that if
central maintenance team had taken the recommendations from Greina, they might have saved 5-10 kWh energy
every day (when RU was faulty) which is twice the typical daily power consumption of RU (Figure 6c). The
negative wastage depicted those scenarios when RU stopped working, and the outlet ended up consuming less
energy in comparison to normal operations.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 13


Beyond Control: Enabling Smart Thermostats For Leakage Detection
•
1:13
Minimising Risk to Product Quality. Next, we observed that room temperature remains significantly high during
the gas leakage (Figure 6d). High temperature risks the product quality and impacts the store operations. The
average room temperature increased by 2◦C-3◦C in both working and non-working hours. When we analysed
across all the 19 instances where Greina reported before the store manager, we noted a median increase of 6◦C
during the dд
t period for each hour of the day, across different outlets (Figure 6e). If maintenance team had taken
the recommendations from Greina, they could have kept the rooms 5◦C-6◦C colder every day (when RU was
faulty), by timely repairing the RU (Figure 6f).
Even though store managers have a benefit of observing the physical symptoms of leakage, Greina identified 19
out of 25 leakages before the store manager. Though in two instances, Greina couldn’t detect the leakage before
manager; we also noted that in remaining three cases, it occurred due to the negligence of the maintenance
contractor. While outlet manager timely reported the leakage to the maintenance team, the maintenance contractor
didn’t take any action for several days. Consequently, the symptoms became visible and Greina detected the
leakage even though store manager repeatedly complained about the leakage.
Beyond Leakage
Though we designed Greina for refrigerant leakage, we observed that the proposed framework also identified
other common time-varying faults.
Ice Formation. Dirty air filters, defective evaporator or condenser fans, lack of refrigerant often results in the
formation of ice in the refrigeration unit. The ice obstructs the path of cold air and the refrigeration unit works
at a reduced efficiency. Though the symptoms of ice formation in temperature data may depend on the fault,
Figure 7a depicts one scenario where the increase in temperature is akin to refrigerant leakage (Figure 1a). If the
ice forms due to heavy usage or a dirty filter, store managers usually clean the filters, however, if the ice forms
due to a fault, ice keeps on forming even after cleaning and manager needs to call the technician to repair the RU.
Greina identified 18 such instances where ice formed due to dirty air filter or defective fans.
Condenser Motor Failure. The job of the condenser is to cool the high-pressure refrigerant gas received from
the compressor by moving outside air across the condenser coils. Through condensation, the high-pressure,
high-temperature refrigerant gas changes to low-temperature liquid refrigerant. However, due to wear and tear,
and high temperature during the summers, the condenser fan motor usually fails and RU stops cooling the room.
In an attempt to cool the room during the motor failure, RU starts drawing more current which increases the
peak power consumption of RU and heats up the system further (Figure 7b). Eventually, RU breaks down, and
manager calls a technician to repair the motor. Greina detected ten such instances of motor failure and raised the
alarm 1-2 days before complete shutdown of the RU.
To conclude, our analysis on a reasonably rich dataset collected from actual field deployments, indicates that
Greina possesses the power to timely identify the refrigerant leakage instances. Beyond being accurate, on an
average, Greina also proved to reduce the reporting delay by five to six days. The improvement in reporting
delay can minimize the energy wastage and maintain desired temperature for the stored items. Interestingly, to
achieve these benefits, the company needs to only upgrade their traditional thermostat to a smart thermostat
with Greina running in the cloud and leveraging the data collected from the thermostat. Our study indicates that
with smart thermostats, the simple yet powerful framework, Greina is easily scalable.
5
DISCUSSION
In this paper, we proposed a leakage detection framework Greina for smart thermostats and validated its efficacy
on a year-long field data collected from 74 outlets of a retail enterprise. In collaboration with an energy-analytic
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 14


1:14
•
M. Jain et al.
On 
Hysteresis
Off 
Hysteresis
Room 
Temperature
Compressor 
Status
(a) For a compressor cycle, the
room temperature stays within
on and off hysteresis.
Temperature ( ◦C)
(b) While hard line depicts recorded tem-
perature signal, dashed line represents es-
timated temperature signal.
Window 
Open
Door 
Open
Power 
Cut
Fan Running
(c) Stochastic user activities (especially
in residential apartments) require time-
varying noise in the thermal model.
Fig. 8. [Left and Middle] Inability to accurately estimate room temperature close to on and off hysteresis leads to misalignment
in estimated and recorded temperature signals. [Right] Current model is unaware of dynamic user activities and assumes
constant thermal noise in the room. It is another major source of modelling error, especially in residential apartments.
firm, we are currently deploying Greina across all the 74 outlets. In this section, we discuss three possible
dimensions to extend the proposed framework.
5.1
Modelling Error
We rely on our thermal model to first learn a decision boundary for Greina to monitor the RU for any leakage
on a daily basis. Though current model estimates room temperature with a mean absolute error of 2◦C (with
σ = 0.9◦C), the reader should also be mindful of the fact that the model is a replaceable module of the whole
framework. In Appendix A, we discuss one such extension of the current thermal model which can estimate
room temperature with an RMSE of 2.85◦C (with σ = 1.3◦C) even in a highly noisy environment of residential
apartments. In our analysis, we noticed that Misalignment and Constant Thermal Noise are the primary sources of
error.
Misalignment. When we turn on the RU (also applicable on AC), the compressor turns on and starts putting cold
air into the room. Due to the flow of cold air, room temperature drops up to a certain level - off hysteresis and
compressor turns off (as depicted in Figure 8a). At this point, RU allows room temperature to increase up to a
certain level - on hysteresis. As temperature reaches the on hysteresis, compressor turns on again and starts
cooling the space.
The control algorithm of RU decides compressor state based on the return air temperature which is measured
inside the RU, near the filters. Let’s call it Trat. On the other hand, we install temperature sensor just outside the
RU, near the fan. Now, let’s say Tr represents room temperature as measured by the sensor and ˜Tr depicts the
estimated room temperature. As per the control logic, the controller will turn off the compressor when Trat ≥Toff .
However, given the complex non-linear thermodynamics, it is impractical to precisely estimate Trat or Tr at any
time instance; thus, Trat −Toff andTrat −Ton. As a result, Trat −Toff , ˜Tr −Toff andTrat −Ton , ˜Tr −Ton. As a result,
though the estimated room temperature will follow the pattern, it will fail to align perfectly with the measured
room temperature. As depicted in Figure 8b also, the actual (hard black line) and estimated (dashed black line)
temperature signals are misaligned. To minimize the effect of error due to misalignment, we consider hourly
mean temperature and add standard deviation to monitor the RU for refrigerant leakage.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 15


Beyond Control: Enabling Smart Thermostats For Leakage Detection
•
1:15
Constant Thermal Noise. Another primary reason is the thermal noise due to multiple dynamic activities at
the same time. In current implementation (Equation 1 and Equation 9-12), we assume that the thermal noise
is constant at any time. However, if the noise is coming from multiple sources, the impact of noise on room
temperature will vary with time. For instance, consider Figure 8c where initially noise is coming through two
activities (window open and ceiling fan running), however, later noise is coming only through an open door. As
the current model is unaware of time-varying noise, it will compute room temperature with time-independent
noise learned from the data; thus inflating the error. While constant noise makes little impact on room temperature
estimation in cold rooms (space is highly insulated and activities are limited), it causes a significant estimation
error for residential apartments. One way to handle time-varying noise is to first identify the activity (based on
temperature, occupancy, and time of the day), and then compute thermal noise for that particular time instance.
At this point, we repeat that the model is a replaceable module of the whole framework; thus, the community is
encouraged to explore other such variants of the current model to enhance Greina’s performance.
5.2
False Negatives & Positives
We discussed multiple scenarios when Greina generated both, false negatives and false positives. After scrutinizing
those situations, we noted that we could avoid many of those instances through user-friendly and interactive
interfaces (or advanced notification systems). Basically, by involving users, we can empower Greina with two-
way communication with the outlet managers for accurate estimation of the refrigerant leakage. In several
instances, managers spotted unusual events, such as high temperature or ice formation. If they could have
notified Greina through a device, Greina would have used the information to detect the leak, even early. Similarly,
we discussed multiple cases where store manager timely reported the leakage, but the repair person (or the
maintenance contractor) only refilled the gas instead of fixing the leakage. Consequently, refrigeration unit
again went down in a couple of weeks and company had to suffer from the business loss, in addition to typical
consequences of refrigeration leakage. If Greina could validate the existence of unusual pattern even after the
corrective action, the maintenance company could reassess the appliance. Not only the two-way communication
would minimize such instances, but it will also develop a sense of trust for the system.
However, one must also remember that user attention is costly. When users are involved, the line between a
useful system and an annoying system is typically very thin. User input is valuable only if the system is designed
while considering -
(1) How frequently user should input the information?
(2) How much time does it take the user to input the information?
(3) How frequently system should notify the users?
(4) Is the interface intuitive and user-friendly?
For the same reason, the new frontiers opening in the domain of smart and ambient notification and attention
management systems, the design of web and mobile application, and many such factors can significantly influence
the outcome of this study. In the future, we plan to implement the proposed framework (along with the user
feedback) to critically evaluate the effectiveness of Greina in achieving the desired goals at a much larger scale.
5.3
Beyond Temperature Signal
From data, we noticed that power consumption data provides better visibility of leakage than the room temperature
because it is less sensitive to thermal noise in the environment and occupants’ dynamic activities. We believe, for
the same reason, technicians analyze electrical component such as input/output voltage and supply current for
fault detection. Moreover, with the advent of advanced techniques to estimate usage and operating conditions
of the appliance through NILM (Non-Intrusive Load Monitoring) [3, 4] and EMI (Electromagnetic Interference)
signatures [11, 26, 27, 60], the use of energy signal for fault detection is worthwhile. However, even though
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 16


1:16
•
M. Jain et al.
the power signal is useful for fault detection, power signal alone won’t allow us to monitor the consequences7.
Although, a smart thermostat together with appliance-level power consumption monitoring could provide best
of both the worlds; one must also note that the duo could significantly impact the scalability of Greina. Until now,
Greina only needed a smart thermostat, however, to realize the pair, the home must either have a smart plug
to monitor AC power consumption, or a smart meter to get AC power consumption profile by disaggregating
meter-level data through NILM algorithms.
If we first look at smart plugs, besides cost, significant variation in supply voltage, type of socket, and power
quality across countries challenge the ubiquity of smart plugs. For instance, domestic appliances in India works at
230 V at 50 Hz frequency, however, in United States, 120 V power is supplied at 60 Hz for domestic use. In addition
to that, voltage fluctuations, frequency variation, generation of spikes, high earth current leaking are some of the
many power quality issues (especially in developing economies) that further hinders the ubiquity of smart plugs.
On the other hand, if we consider smart meter data, the effectiveness of the duo would rely on the accuracy of
disaggregation algorithm in capturing the AC power consumption signal. If we look at power consumption data
(blue curve) in Figure 1a, refrigerant leakage mainly impacts peak power consumption (decreases with time) and
the duration of each cycle (increases with time). Since peak power consumption is critical for leakage detection,
the disaggregation algorithm should ensure that we correctly capture the drop in peak value, and not confuse
with the power consumption of small appliances. Though there are challenges, we believe that a study exploring
the effectiveness of smart thermostats along with smart meter/plug for fault detection could significantly enhance
the performance of Greina without impacting its scalability.
5.4
Beyond Refrigeration
Beauty of Greina lies in its modular and systematic architecture, especially the replaceable thermal model and
ability to work on top of smart thermostats. While Greina can benefit from readily available information from the
thermostat (temperature, occupancy), we can adapt it to diverse environments by tweaking the proposed thermal
model. In Appendix A, we discuss one such extension to a noisy home environment. Poor thermal insulation and
time-varying stochastic activities of people are the primary two bases of thermal noise in residential apartments.
In a separate analysis across five apartments for a month, we found that a non-linear thermal model can estimate
room temperature with an RMSE of 2.85◦C (with σ = 1.3◦C).
Though it is feasible to extend Greina for the home environment, the real challenge lies in evaluating the efficacy
of the proposed framework in such an environment. In residential apartments, tenants call local technicians, and
typically no fault logs are available. Ground truth data collection (at a large scale) demands enormous support
from tenants and the technicians in sharing the information whenever there is a fault. For the same reason,
several studies in the past have either evaluated their approach in theory, or in a controlled environment. We
believe a comprehensive evaluation of Greina across residential apartments can bring up additional intriguing
insights about both, the environment and the system.
6
CONCLUSION
In this paper, we discussed an unsupervised self-learning framework, Greina that senses ambient information
from smart thermostat for leakage detection. The proposed technique employs Grey-Box Modelling to estimate a
decision boundary and later uses the estimates for leakage monitoring. The performance evaluation of Greina on
data from 74 stores (from a city in India) testifies that the simple yet powerful framework can reduce the reporting
delay by a week with best of around 20-30 days in few instances. During these days, the retail enterprise could
have saved twice the energy RU consumes on a typical day. Moreover, by timely repairing the refrigeration unit,
7When a fault occurs, the power signal cannot tell if the appliance is maintaining a suitable temperature for the occupants (if the aim is
maintain user comfort), or the stored products (when using for refrigeration).
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 17


Beyond Control: Enabling Smart Thermostats For Leakage Detection
•
1:17
Table 1. List of symbols used in the proposed thermal model
Symbol
Description
Unit
τ
Sampling Interval
s
r
Thermal region ∈{r1,r2,r3}
−
ηr
Thermal noise in region r
−
Qoc
Cooling load due to occupants and their activities
−
Qac
Cooling capacity of AC
kW
T (t)
r
Temperature in region r at time instance t
◦C
T (t)
e
External temperature at time instance t
◦C
T (t)
w
Temperature of wall (facing outside) at time instance t
◦C
Cr
Thermal capacity of region r
kJ/K
Cw
Thermal capacity of wall (facing outside)
kJ/K
Kr
w
Heat transfer coefficient between wall (facing outside) and region r
kW /K
Kr
e
Heat transfer coefficient between external environment and region r
kW /K
Kw
e
Heat transfer coefficient between wall (facing outside) and weather
kW /K
Kr2
r1
Heat transfer coefficient between r1 and r2
kW /K
Kr3
r2
Heat transfer coefficient between r2 and r3
kW /K
S(t)
ac
AC compressor state (on/off ) at time instance t
−
S(t)
oc
State of occupants at time instance t
−
they could have kept the rooms 5◦C-10◦C colder every day when refrigerant was leaking. In the future, we plan
to deploy the retrofitted thermostats across multiple outlets and study various other challenges, as discussed in
the paper.
A
EXTENSION TO HOME ENVIRONMENT
A residential apartment differs from a cold room in two major aspects:
(1) Poor Insulation - Typically, thermal insulation in a residential apartment is substandard as compared to a
cold room. Often, heat leaks through walls, gaps around doors and windows, and multiple such sources.
(2) Noisy Occupants - In cold room, loss of cooling only happens (given superior insulation) when manager
opens the door for cleaning or shifting the goods. However, significant amount of cooling is consumed by
the occupants in a residential apartment.
Thus, we need a high order thermal model to capture the non-linearity and estimate the room temperature in
a residential apartment. Equation 9-12 depict one such thermal model derived from Bacher et al. [2].
(T (t+1)
w
−T (t)
w ) × Cw
τ
= Kw
e × (T (t)
e
−T (t)
w ) +
rl
Õ
r=1
Kr
w × (T (t)
r
−T (t)
w )
(9)
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 18


1:18
•
M. Jain et al.
(T (t+1)
r1
−T (t)
r1 ) × Cr1
τ
= Kr1
e × (T (t)
e
−T (t)
r1 ) + Kr1
w × (T (t)
w −T (t)
r1 ) + Kr2
r1 × (T (t)
r2 −T (t)
r1 )
+Qac × Sac + ηr1
(10)
(T (t+1)
r2
−T (t)
r2 ) × Cr2
τ
= Kr2
e × (T (t)
e
−T (t)
r2 ) + Kr2
w × (T (t)
w −T (t)
r2 ) + Kr2
r1 × (T (t)
r1 −T (t)
r2 )
+Kr3
r2 × (T (t)
r3 −T (t)
r2 ) + Qoc × Soc + ηr2
(11)
(T (t+1)
r3
−T (t)
r3 ) × Cr3
τ
= Kr3
e × (T (t)
e
−T (t)
r3 ) + Kr3
w × (T (t)
w −T (t)
r3 ) + Kr3
r2 × (T (t)
r3 −T (t)
2 ) + ηr3
(12)
Here, the first region (r1) is the area in proximity of the AC, thus facing direct and the maximal impact of
cold air coming from the AC. The second region, r2 is the region where occupants stay, and the region receives
indirect cooling from r1 region where AC is present. r3 indicates corner spaces in the room. The thermal model
in Equation 1 is a special case of above mentioned model where whole room is considered as single region and
manager’s activities are monitored through a door sensor. Table 1 describes all the notations used in the extended
thermal model.
The idea is to logically divide the room into multiple thermal regions and capture heat transfer at region
level. In the model, we assume that thermostat is installed closer to the AC and each region is considered to
be separated by a thin layer of air having negligible thermal mass. To evaluate the model, we installed smart
thermostat in the bedrooms of five residential apartments, and collected temperature and occupancy data for
a month. In parallel, we gathered weather information from a cloud based weather service. Leave p-out cross
validation (with p = 10) indicates that even in such a noisy environment, the extended model can estimate room
temperature with a mean RMSE of 2.85◦C (with σ = 1.3◦C).
θ = {Cw,Cr1,Cr2,Cr3,Kr1
w ,Kr2
w ,Kr3
w ,Kr1
e ,Kr2
e ,Kr3
e ,Kw
e ,Kr2
r1,Kr3
r2,ηr1,ηr2,ηr3,Qac,Qoc}
(13)
One must note that we only used temperature in r1 (Tr1), outside temperature (Te), and occupancy information
(Soc) to learn the parameter set θ (Equation 13). While temperature and motion data can certainly be captured
from a smart thermostat, climatic conditions are readily available from cloud based weather services. Once
Greina learns the model parameters, it will simulate temperature in r1 and compare with actual temperature
data for leakage detection. Details for monitoring stage remain same as specified in Section 3. We believe, an
interchangeable thermal model empowers Greina to be genuinely pervasive and ubiquitous. Depending upon the
design requirements, researchers can explore different variants of the thermal model for diverse scenarios.
REFERENCES
[1] Kriengkrai Assawamartbunlue and Michael J Brandemuehl. 2006. Refrigerant leakage detection and diagnosis for a distributed
refrigeration system. HVAC&R Research 12 (2006), 389–405.
[2] Peder Bacher and Henrik Madsen. 2011. Identifying suitable models for the heat dynamics of buildings. Energy and Buildings 43 (2011),
1511–1522.
[3] Nipun Batra, Amarjeet Singh, and Kamin Whitehouse. 2016. Gemello: Creating a Detailed Energy Breakdown from Just the Monthly
Electricity Bill. In Proceedings of the 22Nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. ACM, New
York, NY, USA, 431–440.
[4] Nipun Batra, Hongning Wang, Amarjeet Singh, and Kamin Whitehouse. 2017. Matrix Factorisation for Scalable Energy Breakdown. In
AAAI Conference on Artificial Intelligence. AAAI Press, Palo Alto, CA, USA, 4467–4473.
[5] Alireza Behfar, David Yuill, and Yuebin Yu. 2017. Automated fault detection and diagnosis methods for supermarket equipment (RP-1615).
Science and Technology for the Built Environment 23 (2017), 1253–1266.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 19


Beyond Control: Enabling Smart Thermostats For Leakage Detection
•
1:19
[6] Florian Bender, Aleksandr Skrypnik, Achim Voigt, Joachim Marcoll, and Michael Rapp. 2003. Selective detection of HFC and HCFC
refrigerants using a surface acoustic wave sensor system. Analytical Chemistry 75 (2003), 5262–5266.
[7] Michael R Brambley, Philip Haves, Sean C McDonald, Paul Torcellini, D Hansen, DR Holmberg, and KW Roth. 2005. Advanced sensors
and controls for building applications: Market assessment and potential R&D pathways. Technical Report. EERE Publication and Product
Library, Washington, DC (United States).
[8] Mark S Breuker and James E Braun. 1998. Common faults and their impacts for rooftop air conditioners. HVAC&R Research 4 (1998),
303–318.
[9] Varun Chandola, Arindam Banerjee, and Vipin Kumar. 2009. Anomaly detection: A survey. ACM computing surveys (CSUR) 41 (2009),
15.
[10] Bin Chen and James E Braun. 2001. Simple rule-based methods for fault detection and diagnostics applied to packaged air condition-
ers/Discussion. ASHRAE Transactions 107 (2001), 847.
[11] Ke-Yu Chen, Sidhant Gupta, Eric C Larson, and Shwetak Patel. 2015. Dose: Detecting user-driven operating states of electronic
devices from a single sensing point. In Pervasive Computing and Communications (PerCom), 2015 IEEE International Conference on. IEEE,
Piscataway, NJ, USA, 46–54.
[12] Drury B Crawley, Linda K Lawrie, Curtis O Pedersen, and Frederick C Winkelmann. 2000. Energy plus: energy simulation program.
ASHRAE journal 42 (2000), 49–56.
[13] Lucas W Davis and Paul J Gertler. 2015. Contribution of air conditioning adoption to future energy use under global warming. Proceedings
of the National Academy of Sciences 112 (2015), 5962–5967.
[14] T Dewson, B Day, and AD Irving. 1993. Least squares parameter estimation of a reduced order thermal model of an experimental
building. Building and Environment 28 (1993), 127–137.
[15] Temperature-Only Refrigeration Cycle Diagnostics. 2005. Advanced Automated HVAC Fault Detection and Diagnostics Commercializa-
tion Program. Contract 500 (2005), 03–030.
[16] Bing Dong, Mikhail Gorbounov, Shui Yuan, Tiejun Wu, Abhishek Srivastav, Trevor Bailey, and Zheng OâĂŹNeill. 2013. Integrated
energy performance modeling for a retail store building. In Building simulation, Vol. 6. Springer, Salmon Tower Building, NY, USA,
283–295.
[17] Tom Downey and John Proctor. 2002. What can 13,000 air conditioners tell us? the Proceedings of the 2002 ACEEE Summer Study on
Energy Efficiency in Buildings 1 (2002), 53–67.
[18] Zhimin Du, Xinqiao Jin, and Lizhou Wu. 2007. Fault detection and diagnosis based on improved PCA with JAA method in VAV systems.
Building and Environment 42 (2007), 3221–3232.
[19] Serge Dube. 2009. Refrigerant leak-detection systems. US Patent App. 12/256,504.
[20] Radek Fisera and Martin Hrncar. 2012. System and method for performance monitoring of commercial refrigeration. US Patent App.
12/976,088.
[21] Radek Fisera and Petr Stluka. 2012. Performance monitoring of the refrigeration system with minimum set of sensors. World Academy
of Science, Engineering and Technology 6 (2012), 396–401.
[22] Christina Francis, Graeme Maidment, and Gareth Davies. 2017. An investigation of refrigerant leakage in commercial refrigeration.
International Journal of Refrigeration 74 (2017), 12–21.
[23] Tanuja Ganu, Dwi Rahayu, Deva P Seetharam, Rajesh Kunnath, Ashok Pon Kumar, Vijay Arya, Saiful A Husain, and Shivkumar
Kalyanaraman. 2014. SocketWatch: an autonomous appliance monitoring system. In Pervasive Computing and Communications (PerCom),
2014 IEEE International Conference on. IEEE, Piscataway, NJ, USA, 38–43.
[24] Janos Gertler. 2013. Fault detection and diagnosis. Springer, Salmon Tower Building, NY, USA.
[25] IN Grace, Datta Datta, and SA Tassou. 2005. Sensitivity of refrigeration system performance to charge levels and parameters for on-line
leak detection. Applied Thermal Engineering 25 (2005), 557–566.
[26] Manoj Gulati, Shobha Sundar Ram, and Amarjeet Singh. 2014. An in Depth Study into Using EMI Signatures for Appliance Identification.
In Proceedings of the 1st ACM Conference on Embedded Systems for Energy-Efficient Buildings. ACM, New York, NY, USA, 70–79.
[27] Sidhant Gupta, Matthew S. Reynolds, and Shwetak N. Patel. 2010. ElectriSense: Single-point Sensing Using EMI for Electrical Event
Detection and Classification in the Home. In Proceedings of the 12th ACM International Conference on Ubiquitous Computing. ACM, New
York, NY, USA, 139–148.
[28] Hua Han, Zhikun Cao, Bo Gu, and Neng Ren. 2010. PCA-SVM-based automated fault detection and diagnosis (AFDD) for vapor-
compression refrigeration systems. HVAC&R Research 16 (2010), 295–313.
[29] Rolf Isermann. 2011. Fault-Diagnosis Applications: Model-Based Condition Monitoring Actuators, Drives, Machinery, Plants, Sensors, and
Fault-tolerant Systems (1st ed.). Springer Publishing Company, Incorporated, Salmon Tower Building, NY, USA.
[30] Milan Jain, Amarjeet Singh, and Vikas Chandan. 2016. Non-intrusive estimation and prediction of residential ac energy consumption. In
Pervasive Computing and Communications (PerCom), 2016 IEEE International Conference on. IEEE, Piscataway, NJ, USA, 1–9.
[31] Edward A Jeffers, R Philip McLeroy, and Jose L Sacerio. 1984. Halogen gas leak detector. US Patent 4,488,118.
[32] Jin-Ho Jeong. 2005. Refrigerant leakage sensing system and method. US Patent App. 10/938,647.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 20


1:20
•
M. Jain et al.
[33] Prasad S Kadle and Mahmoud Ghodbane. 2014. Refrigerant leak detection system. US Patent 8,695,404.
[34] Stephen L Keres, Alberto Regio Gomes, and Andrew D Litch. 2016. Fault detection and diagnosis for refrigerator from compressor
sensor. US Patent 9,513,043.
[35] Minsung Kim, Seok Ho Yoon, Piotr A Domanski, and W Vance Payne. 2008. Design of a steady-state detector for fault detection and
diagnosis of a residential air conditioner. International journal of refrigeration 31 (2008), 790–799.
[36] Sun Ho Kim, Hyeun Jun Moon, and Young Ran Yoon. 2017. Improved occupancy detection accuracy using PIR and door sensors for a
smart thermostat. Building Simulation 2017 15 (2017), 2753–2758.
[37] Woohyun Kim and Srinivas Katipamula. 2018. A review of fault detection and diagnostics methods for building systems. Science and
Technology for the Built Environment 24 (2018), 3–21.
[38] Knud Lasse Lueth. 2016. Smart Thermostat market for the period 2015 to 2021. https://goo.gl/uRccu4 [Online; accessed 12-November-
2018].
[39] Kedar Kulkarni, Umamaheswari Devi, Amith Sirighee, Jagabondhu Hazra, and Praveen Rao. 2018. Predictive Maintenance for Supermarket
Refrigeration Systems Using Only Case Temperature Data. In 2018 Annual American Control Conference (ACC). IEEE, Piscataway, NJ,
USA, 4640–4645.
[40] Haorong Li. 2004. A decoupling-based unified fault detection and diagnosis approach for packaged air conditioners. Ph.D. Dissertation.
Purdue University.
[41] Yunhua Li, Mingsheng Liu, Josephine Lau, and Bei Zhang. 2014. Experimental study on electrical signatures of common faults for
packaged DX rooftop units. Energy and Buildings 77 (2014), 401–415.
[42] Jiakang Lu, Tamim Sookoor, Vijay Srinivasan, Ge Gao, Brian Holben, John Stankovic, Eric Field, and Kamin Whitehouse. 2010. The Smart
Thermostat: Using Occupancy Sensors to Save Energy in Homes. In Proceedings of the 8th ACM Conference on Embedded Networked
Sensor Systems. ACM, New York, NY, USA, 211–224.
[43] Dennis Martell and Jan Krcma. 1994. Refrigerant gas leak detector. US Patent 5,351,037.
[44] Georgios Mavromatidis, Salvador Acha, and Nilay Shah. 2013. Diagnostic tools of energy performance for supermarkets using Artificial
Neural Network algorithms. Energy and Buildings 62 (2013), 304–314.
[45] Yu Meng, Margaret H Dunham, F Marco Marchetti, and Jie Huang. 2006. Rare event detection in a spatiotemporal environment. In
Granular Computing, 2006 IEEE International Conference on. IEEE, Piscataway, NJ, USA, 629–634.
[46] Gordon R Morrow. 1994. Refrigerant leak detector system. US Patent 5,351,500.
[47] Gordon R Morrow and Coy M White. 1996. Refrigerant leak detector system. US Patent 5,524,445.
[48] Balakrishnan Narayanaswamy, Bharathan Balaji, Rajesh Gupta, and Yuvraj Agarwal. 2014. Data Driven Investigation of Faults in HVAC
Systems with Model, Cluster and Compare (MCC). In Proceedings of the 1st ACM Conference on Embedded Systems for Energy-Efficient
Buildings. ACM, New York, NY, USA, 50–59.
[49] J Navarro-Esbri, Eb Torrella, and R Cabello. 2006. A vapour compression chiller fault detection technique based on adaptative algorithms.
Application to on-line refrigerant leakage detection. International Journal of Refrigeration 29 (2006), 716–723.
[50] Zheng O’Neill, Xiufeng Pang, Madhusudana Shashanka, Philip Haves, and Trevor Bailey. 2014. Model-based real-time whole building
energy performance monitoring and diagnostics. Journal of Building Performance Simulation 7 (2014), 83–99.
[51] Kartik Palani, Nabeel Nasir, Vivek Chil Prakash, Amandeep Chugh, Rohit Gupta, and Krithi Ramamritham. 2014. Putting Smart Meters
to Work: Beyond the Usual. In Proceedings of the 5th International Conference on Future Energy Systems. ACM, New York, NY, USA,
237–238.
[52] Manher Parekh. 1992. Method for detecting leakage in a refrigeration system. US Patent 5,149,453.
[53] William V Payne, Piotr A Domanski, Jaehyeok Heo, and Zhimin Du. 2015. Self-Training of a Fault-Free Model for Residential Air
Conditioner Fault Detection and Diagnostics. Technical Report. NIST, USA.
[54] W Vance Payne, Jaehyeok Heo, and Piotr A Domanski. 2018. A Data-Clustering Technique for Fault Detection and Diagnostics in
Field-Assembled Air Conditioners. International Journal of Air-Conditioning and Refrigeration 26 (2018), 1850015.
[55] Fabian Pedregosa, Gaël Varoquaux, Alexandre Gramfort, Vincent Michel, Bertrand Thirion, Olivier Grisel, Mathieu Blondel, Peter
Prettenhofer, Ron Weiss, Vincent Dubourg, et al. 2011. Scikit-learn: Machine learning in Python. Journal of machine learning research 12
(2011), 2825–2830.
[56] Michael Ramey Porter, Joseph James Rozsnaki, and Osman Ahmed. 2008. Refrigeration system fault detection and diagnosis using
distributed microsystems. US Patent App. 11/786,033.
[57] Neng Ren, Jun Liang, Bo Gu, and Hua Han. 2008. Fault diagnosis strategy for incompletely described samples and its application to
refrigeration system. Mechanical Systems and Signal Processing 22 (2008), 436–450.
[58] Charlie M Rinehart. 2004. Refrigerant leak detection system. US Patent 6,772,598.
[59] Todd M Rossi and James E Braun. 1997. A statistical, rule-based fault detection and diagnostic method for vapor compression air
conditioners. Hvac&R Research 3, 1 (1997), 19–37.
[60] Sense. 2018. The Sense Home Energy Monitor. https://sense.com [Online; accessed 12-November-2018].
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.


## Page 21


Beyond Control: Enabling Smart Thermostats For Leakage Detection
•
1:21
[61] Shravan Srinivasan, Arunchandar Vasan, Venkatesh Sarangan, and Anand Sivasubramaniam. 2015. Bugs in the Freezer: Detecting Faults
in Supermarket Refrigeration Systems Using Energy Signals. In Proceedings of the 2015 ACM Sixth International Conference on Future
Energy Systems. ACM, New York, NY, USA, 101–110.
[62] Takahisa Suzuki, Tatsuo Tsunooka, Toshihiro Tahara, and Tetsuji Nobuta. 2004. Vapor compression type refrigeration apparatus
including leak detection and method for detecting refrigerant leaks. US Patent 6,681,582.
[63] SA Tassou and IN Grace. 2005. Fault diagnosis and refrigerant leak detection in vapour compression refrigeration systems. International
Journal of Refrigeration 28 (2005), 680–688.
[64] Dan W Taylor and David W Corne. 2004. Refrigerant leak prediction in supermarkets using evolved neural networks. In Recent Advances
In Simulated Evolution And Learning. World Scientific, Hackensack, NJ, USA.
[65] Claus Thybo and Roozbeh Izadi-Zamanabadi. 2004. Development of fault detection and diagnosis schemes for industrial refrigeration
systems-Lessons learned. In Control Applications, 2004. Proceedings of the 2004 IEEE International Conference on, Vol. 2. IEEE, Piscataway,
NJ, USA, 1248–1253.
[66] TWC Product and Technology. 2014. Wunderground. http://www.wunderground.com/ [Online; accessed 12-November-2018].
[67] Wikipedia contributors. 2017. CUSUM — Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/w/index.php?title=CUSUM&
oldid=786593468 [Online; accessed 12-November-2018].
[68] Dick Wirz. 2017. Commercial refrigeration for air conditioning technicians. Cengage Learning, Boston, USA.
[69] Zhenyu Yang, Karsten B Rasmussen, Anh T Kieu, and Roozbeh Izadi-Zamanabadi. 2011. Fault Detection and Isolation for a Supermarket
Refrigeration System–Part One: Kalman-Filter-Based Methods. IFAC Proceedings Volumes 44 (2011), 13233–13238.
[70] Zhenyu Yang, Karsten B Rasmussen, Anh T Kieu, and Roozbeh Izadi-Zamanabadi. 2011. Fault Detection and Isolation for a Supermarket
Refrigeration System–Part Two: Unknown-Input-Observer Method and Its Extension. IFAC Proceedings Volumes 44 (2011), 4238–4243.
[71] Jin Woo Yoo, Sung Bin Hong, and Min Soo Kim. 2017. Refrigerant leakage detection in an EEV installed residential air conditioner with
limited sensor installations. International Journal of Refrigeration 78 (2017), 157–165.
[72] Yuebin Yu, Denchai Woradechjumroen, and Daihong Yu. 2014. A review of fault detection and diagnosis methodologies on air-handling
units. Energy and Buildings 82 (2014), 550–562.
Received November 2017; Revised May 2018; Revised November 2018; Accepted January 2019
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., Vol. 3, No. 1, Article 1. Publication date: March 2019.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
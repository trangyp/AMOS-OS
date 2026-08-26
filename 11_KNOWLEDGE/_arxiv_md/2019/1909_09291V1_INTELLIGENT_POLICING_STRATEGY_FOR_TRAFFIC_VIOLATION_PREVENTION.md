---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1909.09291v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1909.09291v1_Intelligent_Policing_Strategy_for_Traffic_Violation_Prevention

> Source: 1909.09291v1_Intelligent_Policing_Strategy_for_Traffic_Violation_Prevention.pdf

> Pages: 6

---


## Page 1


Intelligent Policing Strategy for Trafﬁc Violation
Prevention
Monireh Dabaghchian
†, Amir Alipour-Fanid
∗, and Kai Zeng
∗
†Department of Computer Science, and Cybersecurity Assurance and Policy (CAP)
Center, Morgan State University
∗Department of Electrical and Computer Engineering, George Mason University
E-mail: †monireh.dabaghchian@morgan.edu, {∗aalipour, ∗kzeng2}@gmu.edu
1
Abstract
Police ofﬁcer presence at an intersection discourages a potential trafﬁc violator from violating the law. It
also alerts the motorists’ consciousness to take precaution and follow the rules.
However, due to the
abundant intersections and shortage of human resources, it is not possible to assign a police ofﬁcer to
every intersection. In this paper, we propose an intelligent and optimal policing strategy for trafﬁc violation
prevention. Our model consists of a speciﬁc number of targeted intersections and two police ofﬁcers with
no prior knowledge on the number of the trafﬁc violations in the designated intersections. At each time
interval, the proposed strategy, assigns the two police ofﬁcers to different intersections such that at the end
of the time horizon, maximum trafﬁc violation prevention is achieved. Our proposed methodology adapts the
PROLA (Play and Random Observe Learning Algorithm) algorithm [1] to achieve an optimal trafﬁc violation
prevention strategy. Finally, we conduct a case study to evaluate and demonstrate the performance of the
proposed method.
2
Introduction and Motivation
A popular and well-sensible proverb, “Prevention is better than cure”, reveals that efforts to prevent a
negative incident from happening are much better than ﬁnding out a solution to resolve a problem. Along
with this belief, public law enforcement agencies (Local police, Sheriffs’ departments, Special police, Fed-
eral and State police) also endeavor in reduction of criminal activities, robbery, assault, major/minor trafﬁc
violation, and physical violence through mission assignments or a regular and predeﬁned strategies [2].
Trafﬁc violation is one of the major concerns for the law enforcement agencies among other illegal and
unlawful activities. In this regard, intersections in city streets or main roads are the critical and important
regions in severity and frequency of trafﬁc violation in the records [3, 4]. There are, for example, various
intersection trafﬁc violation types, including but not limited to disobeying trafﬁc lights, signs (yield on green,
do not turn right, left and U-turn) or signals, blocking or retarding trafﬁc, failure to stop or yield to pedes-
trian, speeding, improper blowing of horn, improper turn, racing, dragging, or contest for speed. Depending
on the violation degree, trafﬁc law violation may cause single/multi-vehicle collision or in some cases fa-
tal pedestrian/vehicle crash. Law enforcement agencies utilize various effective law enforcement methods
such as proper trafﬁc signs deployment, radar speed gun, red light camera and etc, in order to prevent the
trafﬁc violations [5].
Among all approaches, police ofﬁcer presence in the ﬁeld is the most effective and functional way to help
reduce the trafﬁc violation dramatically. Vehicle drivers take precautions and get alerted when observing the
police ofﬁcer or his/her car standing close to the intersections. Therefore, trafﬁc managers and engineers
assign police ofﬁcers to some places based on some strategies to monitor and combat trafﬁc violation. Typ-
ically, these strategies are based on personal experiences i.e., prior knowledge on the frequency of trafﬁc
1
arXiv:1909.09291v1  [cs.AI]  20 Sep 2019


## Page 2


Figure 1: Trafﬁc violation prevention model
violations happening in a speciﬁc region. Although the value and usefulness of the law enforcement ofﬁcer’s
experiences cannot be ignored [6], however, research community also continuously strives to discover su-
perior and optimal strategies based on the advanced technologies and scientiﬁc methods such as historical
data (evidence-based records) analysis methodologies [7–9].
Nowadays, due to the rapid outward growth and development of the cities and sub-urban areas on
the one hand, and shortage of law enforcement resources on the other hand, the need for intelligent and
cost-effective policing strategies are of a great signiﬁcance and importance to the law enforcement policy
planners and administration. Inspired by the idea of police ofﬁcer presence in the ﬁelds for prevention
purposes, in this paper, we propose a novel intelligent policing strategy which mathematically is proven to
be an optimal strategy subject to the proposed model.
In this model, we consider a geographical region of a city/sub-urban which consists of a set of intersec-
tions. We then consider a police ofﬁcer which intends to choose and attend a speciﬁc intersection out of
all intersections at different time intervals to help prevent the trafﬁc violations. Considering various trafﬁc
violation rates for different intersections, the goal is for the police ofﬁcer to ﬁnd the intersection with the most
trafﬁc violation rates and to be present in that intersection more often than others to maximize the number of
trafﬁc violation prevention. We utilize an online learning strategy called PROLA (Play and Random Observe
Learning Algorithm) [1] for the police ofﬁcer to learn the trafﬁc violation rates at different intersections. The
proposed method promised to be efﬁcient and cost-effective by enabling intelligent police ofﬁcer assignment
to work actually smarter, not harder.
Challenge: The key in the police ofﬁcer’s efﬁcient learning process is to be able to observe/know
whether his/her presence in a speciﬁc location prevented trafﬁc violations or not. However, due to the
nature of this problem, any time attending a location the police ofﬁcer will have no idea whether his presence
was effective or not. This is because either there were no violators in the area or if there were any, they
recognized the police ofﬁcer via his marked car and did not violate the trafﬁc law. This poses a challenge
in obtaining an optimal policing strategy to prevent the trafﬁc violations as based on the existing work in
the literature for any agent interacting with the environment, the agent needs to observe some feedback
on the action he/she takes. However, in this problem, the police ofﬁcer as an agent is not able to observe
the feedback on his action which is deﬁned as the intersection he/she attends. In order to overcome the
challenge, we apply the PROLA algorithm for optimal policing strategy that achieves an optimal performance
in terms of trafﬁc violation prevention.
3
Trafﬁc Violation Prevention Model
Our model consists of two types of law enforcement ofﬁcers. One of the ofﬁcers wears a police uniform
and uses a marked car, so he/she and his/her car are recognizable by the other vehicle drivers. We name
this type of ofﬁcer as Police Ofﬁcer with Marked Car (POMC) and for simplicity of the notation we denote
2


## Page 3


Algorithm 1: PROLA (Play and Random Observe Learning Algorithm) [1]
Parameters: γ ∈(0, 1), η ∈

0,
γ
2(K−1)
i
.
Initialization: ω1(i) = 1,
i = 1, ..., K.
For each t = 1, 2, ..., T
1. Set pt(i) = (1 −γ)
ωt(i)
PK
j=1 ωt(j) + γ
K ,
i = 1, ..., K.
2. MC select intersection It ∼pt and accumulate the unobservable reward xt(It).
3. UC chooses an intersection Jt other than the intersection chosen by the MC uniformly at random
and observes its reward xt(Jt) based on equation (1).
4. For j = 1, ..., K
ˆxt(j) =
(
xt(j)
(1/(K−1))(1−pt(j)),
j = Jt
0,
o.w.,
ωt+1(j) = ωt(j) exp(ηˆxt(j)).
Table 1: Main Notation
T
total number of time intervals
K
total number of intersections
It
index of the intersection that MC is assigned at time t
Jt
index of the intersection that UC is assigned at time t
R
total regret of the MC
γ
exploration rate
η
learning rate
pt (i)
MC assignment distribution on intersection i at time t
ωt (i)
weight assignment to intersection i at time t
it by MC. The other ofﬁcer is not in police uniform and utilizes unmarked police car, so he/she and his/her
car are not recognizable as a law enforcement ofﬁcer by the other vehicle drivers. We also name this type
of ofﬁcer as Police Ofﬁcer with Unmarked Car (POUC) and denote it by UC. We also consider that in the
targeted area for trafﬁc violation prevention there are K intersections. We assume that MC and UC get
assigned to a speciﬁc intersection for a ﬁxed time interval. At the end of the time interval, Algorithm 1 is run
and the MC and UC are assigned to next chosen intersections. We also assume that the MC and UC are
never assigned to the same intersection. Figure 1 illustrates the main components of the proposed model.
4
Intelligent Policing Strategy
Once MC is assigned to an intersection, his/her presence prevents the trafﬁc violation but cannot see
the reward. However, once UC is assigned to an intersection, the drivers are not aware of the presence
of the police, so a potential violator may violate the trafﬁc law so then the UC can observe the violator but
receive no reward. The point is that MC cannot observe the trafﬁc violation prevention (reward), hence,
the MC is not aware of his/her presence impact. However, UC can observe the trafﬁc violation, but his/her
presence cannot prevent the trafﬁc violation (meaning no reward). Instead, he gathers data to learn the
intersection(s) that have high trafﬁc violation rates.
In this regard, our proposed method adresses the following question. Which intersection the MC and
UC have to be assigned in each time interval over the whole time horizon such that the trafﬁc violation due
to the presence of the MC is minimized? Since the MC needs to learn and prevent trafﬁc violation at the
same time and it has no prior knowledge of the violation activity on different intersections beforehand, we
formulate this problem as an online learning problem as follows.
We deﬁne xt(j) as the MC’s reward on the intersection j (1 ≤j ≤K) at time interval t (1 ≤t ≤T)
where K is the number of the intersections in the region and T is the total number of time intervals. Table
3


## Page 4


Figure 2: Algorithm 1 performance on trafﬁc violation prevention by MC assignment
1 summarizes the main notation used in this paper.
Without loss of generality, we normalize xt(j) ∈[0, 1]. More speciﬁcally:
xt(j) =
(
1,
trafﬁc is violated at intersection j at time interval t
0,
o.w.
.
(1)
Suppose the proposed algorithm applies learning policy ϕ to assign MC and UC to the intersections.
The aggregated expected reward of the MC by time interval T is equal to
Gϕ(T) = Eϕ
" T
X
t=1
xt(It)
#
,
(2)
where It indicates the intersection index that the MC is assigned by the algorithm at time t. The MC’s goal
is to maximize the expected value of the aggregated reward, thus to minimize the trafﬁc vilolation,
maximize
Gϕ(T).
(3)
For a learning algorithm, regret is commonly used to measure its performance [1]. The regret of the MC
can be deﬁned as follows:
Regret = Gmax −Gϕ (T) ,
(4)
where
Gmax = max
j
T
X
t=1
xt (j) .
(5)
4


## Page 5


(a) MC assignment probability on the intersections, K = 10.
(b) Total regret of MC for different K over the time.
Figure 3: Algorithm 1 performance evaluation
The regret measures the gap between the accumulated reward achieved by applying a learning algo-
rithm and the maximum accumulated reward the MC can obtain when it always (i.e., for the all time intervals)
stays in the intersection with the highest number of trafﬁc violations. From the MC point of view, we call this
speciﬁc intersection as Best Intersection (BI). The BI is the intersection with highest accumulated reward
up to time T. Then, the problem can be transformed to minimize the regret as follows:
minimize
Gmax −Gϕ (T) .
(6)
In order to solve the Eq. (6), we adapt the PROLA (Play and Random Observe Learning Algorithm)
algorithm [1], and propose MC and UC to be assigned to different intersections over the time based on the
strategy outlined in Algorithm 1. We have proved the optimality of this algorithm in [1].
5
Case Study and Performance Evaluation
Number of intersections in the targeted area may vary and depend on several urban design factors such
as whether it is a residential, commercial or industrial area, etc. In this case study, we consider various
scenarios with different number of intersections i.e., K ∈{10, 20, 30, 40, 50}. We can also assume that each
time interval is one hour and at the beginning of each time interval, police ofﬁcers (MC/UC) are assigned to
different intersections according to Algorithm 1.
At the end of each time interval, UC reports the number of the trafﬁc violations (if ever happened) in the
intersection to the algorithm. Then, based on the information acquired till the end of that time interval, the
algorithm chooses the indices of the two intersections for the next time interval in which both ofﬁcers will be
assigned to them. This process is repeated for the whole time horizon T.
We assume that at each time interval, trafﬁc violation follows a Bernoulli distribution. For instance, for
K = 10 we assume p1 = 0.04, p2 = 0.2, p3 = 0.17, p4 = 0.2, p5 = 0.08, p6 = 0.6, p7 = 0.16, p8 = 0.1, p9 =
0.12, p10 = 0.2, where pi for i = 1, 2, ..., 10 indicates the probability of the trafﬁc violation at each time interval
in the ith intersection. Figure 2(a) illustrates the generated trafﬁc violation for different intersections in time
horizon 1 to 600 according to the aforementioned distribution. According to the BI deﬁnition, in the generated
data, intersection 6 is the BI. Figure 2(b) shows how Algorithm 1 assigns MC to different intersections to
maximize the trafﬁc violation prevention. It is shown in this ﬁgure that as time goes on, the MC is assigned
to intersection 6 (i.e., BI) more frequently to prevent trafﬁc violation.
For the case of K = 10, Fig. 3(a) illustrates the probability of assigning the MC to the various intersec-
tions by the Algorithm 1 for the whole time horizon T. Intersection 6 is the BI, so the probability that the
Algorithm 1 assigns MC to the BI increases as time goes on. Figure 3(b) shows the MC’s regret for various
number of intersections. As the number of the intersections increases the MC’s regret increases, as well.
5


## Page 6


However, since the nature of PROLA algorithm is a no-regret algorithm [1,10], the MC’s regret independent
from K approaches to zero as T −→∞.
Remark: Since the proposed learning algorithm performs online, if the BI changes to another intersec-
tion, the algorithm adaptively learns and converges to the new BI. As a result, MC is assigned to the new
BI more frequently to maximize the trafﬁc violation prevention.
6
Conclusion
In this paper, we proposed an intelligent policing strategy for trafﬁc violation prevention. The proposed
online learning algorithm assigns two types of police ofﬁcers, Police Ofﬁcer with Marked Car (MC) and
Unmarked Car (UC), to various intersections strategically such that at the end of the time horizon maximum
trafﬁc violation prevention is achieved. We evaluated the performance of the algorithm through simulation
on various settings and showed that as time goes on, the algorithm learns the environment and assigns the
MC to the best intersection in the region to maximize the trafﬁc violation prevention.
We hope that the proposed methodology and the model insight can further pave the path to invent
new types of intelligent algorithms which are essential to unlock the full potential of artiﬁcial intelligence in
strategic policing.
References
[1] M. Dabaghchian, A. Alipour-Fanid, K. Zeng, Q. Wang, and P. Auer, “Online learning with random-
ized feedback graphs for optimal pue attacks in cognitive radio networks,” IEEE/ACM Transaction on
Networking, vol. 26, no. 5, pp. 2268–2281, Oct. 2018.
[2] J. Potts, “The beneﬁts, challenges, and lessons of evidence-based policing,” The Journal of California
Law Enforcement, vol. 51, no. 2, 2017.
[3] C. D. Hughes, Warren and S.-R. Chen, “Innovative intersection safety improvement strategies and
management practices: A domestic scan,” Federal Highway Administration, 2006. [Online]. Available:
https://safety.fhwa.dot.gov/intersection/other topics/fhwasa06016/fhwasa06016.pdf
[4] C. Y. D. Yang and W. G. Najm, “Analysis of red light violation data collected from intersections equipped
with red light photo enforcement cameras,” National Highway Trafﬁc Safety Administration (NHTSA), in
conjunction with the Research and Innovative Technology Administrations Volpe National Transporta-
tion Systems Center (Volpe Center), 2006.
[5] M. Grifﬁth, “Safety evaluation of red-light cameras-executive summary,” Federal Highway Administra-
tion, no. FHWA-HRT-05-049, 2005.
[6] J. Fleming and R. Rhodes, “Can experience be evidence? craft knowledge and evidence-based polic-
ing,” Policy and Politics, vol. 46, no. 1, 2018.
[7] C. Rigano, “Using artiﬁcial intelligence to address criminal justice needs,” National Institute of Justice
Journal, no. 280, Law Enforcement, 2018.
[8] “Law enforcement advancing data and science (LEADS) strategic plan 2018-2023,” National Criminal
Justice Reference Service (NCJRS), 2018. [Online]. Available:
https://www.ncjrs.gov/pdfﬁles1/nij/
251765.pdf
[9] “Policing strategic research plan 2017-2021,” National Criminal Justice Reference Service (NCJRS),
2018. [Online]. Available: https://www.ncjrs.gov/pdfﬁles1/nij/250915.pdf
[10] A. Blum and Y. Mansour, “From external to internal regret,” in Learning Theory, P. Auer and R. Meir,
Eds.
Berlin, Heidelberg: Springer Berlin Heidelberg, 2005, pp. 621–636.
6

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
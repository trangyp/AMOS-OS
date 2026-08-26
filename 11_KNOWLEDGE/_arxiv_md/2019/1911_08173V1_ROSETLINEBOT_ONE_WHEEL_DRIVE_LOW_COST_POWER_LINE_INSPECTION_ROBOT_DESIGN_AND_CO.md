---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.08173v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1911.08173v1_ROSETLineBot__One-Wheel-Drive_Low-Cost_Power_Line_Inspection_Robot_Design_and_Co

> Source: 1911.08173v1_ROSETLineBot__One-Wheel-Drive_Low-Cost_Power_Line_Inspection_Robot_Design_and_Co.pdf

> Pages: 7

---


## Page 1


(PREPRINT) ROSETLineBot: One-Wheel-Drive Low-Cost
Power Line Inspection Robot Design and Control
A. Tarık Zengin1, Gokhan Erdemir2, T. Cetin Akinci3, F. Anil Selcuk1,4, M. Nizamettin Erduran1, S. Serhat Seker3
1 Istanbul Sabahattin Zaim University, Dep. of Computer Engineering, Istanbul, Turkey; {tarik.zengin, nizamettin.erduran}@izu.edu.tr
2 Istanbul Sabahattin Zaim University, Dep. of Electrical and Electronics Engineering, Istanbul, Turkey; gokhan.erdemir@izu.edu.tr
3 Istanbul Technical University, Department of Electrical Engineering, Istanbul, Turkey; {akincitc, sekers}@itu.edu.tr
4 Marmara University, Department of Mechatronics Engineering, Istanbul, Turkey; anilselcuk@marun.edu.tr
2 Correspondence author
Abstract:  Continuous operation of the electrical transmission lines is of great  importance for today's electricity-
dependent world. It is crucial to detect and diagnose a possible problem on the lines before that occurs. In general,
maintenance,  repair  and  error  detection  operations  of  the  electrical  transmission lines  are  performed  by humans
periodically. However, these difficult tasks contain high-risks in terms of occupational health and safety. Moreover, it is
not possible to continuously inspect these lines which extend over long distances by maintenance and repair personnel.
For all these reasons, it is very convenient to use robotic systems for inspection on power transmission lines. By
evaluating the data which are provided from sensors and cameras of robotic systems, it would be possible to take
precautions before an error occurs. Robotic systems that can move continuously along the line would be able to gather
continuous and uninterrupted information. Thus, potential problems can be detected and identified in advance. In this
study, a single wheel drive low-cost mobile robot is designed and controlled which can work and move on the electrical
transmission lines. Because of the modular structure of the designed robot, different types of sensors can be integrated
into the robot, easily. The designed low-cost robotic system will cause minimum losses in case of possible breakage.
Keywords: power line inspection, one-wheel-drive robot, control control, ROSETLineBot.
1. Introduction
Energy dependency of today's world obliges energy transmission lines to more productive and uninterrupted operation
without any problem[1]. Energy transmission lines (systems) face many challenges  due to the growing need for
sustainable energy worldwide [1-5]. It is important to do maintenance, repair, breakdown, leak detection, and etc.
operations of the power lines, rapidly [1-26]. Although the operations to be carried out on power transmission lines are
often performed by humans, it can be fully or partially automated by using robotic systems with direct or teleoperated
(remote control) robot systems [1-10]. There are various risks to humans who will work in the maintenance of power
lines and transformers in terms of occupational health and safety. The maintenance of power lines contains various risks
for humans who will work for maintenance operations in terms of occupational health and safety. Using robotic systems
on the power lines can increase productivity, reduce labor costs and, most importantly, eliminate operational risks that
threaten human life[1]. Although, development and implementation of the robotic applications for various tasks on the
power  lines  is  still  so  challenging  and  popular  research  area  in  robotics  science  [1-5].  The  specifications  and
characteristics of the robotic systems which will be used on the power line inspection depend on the tasks to be
performed on the power lines[1-10]. Research on energy transmission systems in robotics generally focus on high
voltage lines [10-15, 21-26]. It is a suitable research area for the use of robotic systems due to the fact that high-voltage
lines are far from the urban areas, being high above the ground, and carrying a large number of risks for the maintenance
personnel[5-12]. 
In literature, robotic systems used in high voltage lines vary. Generally, wheeled systems that are seated on the cable and
grasp the cable tightly are preferred [8]. Some of the developed robotic systems for power line inspections are shown in
Figure 1. The “Expliner©" robot which is developed by HiBot has been used in Japan, South Korea, the Netherlands and
the United States [27]. The robot, developed by the EPRI (Electric Power Research Institute), is actively used in high-
voltage lines between cities or states, especially in the United States [28].
Medium voltage lines are also another research area for robotic systems [1, 3, 5-10]. However, some problems which are
listed below in medium voltage lines make it difficult to use robotic systems in these lines. General problems in medium
voltage  line;  (i) the  absence  of  a  certain  standard  in the  types  of electricity  pole,  (ii)  using different  types  of
materials(cable, bowl, connection apparatus, etc.), (iii) they are densely located within the urban areas, and (iv) they have
different connection types. Because of the mentioned problems, it is more appropriate to use semi-autonomous or
teleoperated robotics systems instead of fully autonomous systems in medium voltage lines [1-5].


## Page 2


Figure 1. (a) LineScout robot [18], (b) HiBot “Expliner©” [27], (c) LineROVer [1], and (d) DJI – M200 – Powerline Inspection Tool[29].
In this study, the design, and control of a one-wheel-drive low-cost power line ınspection robot which is named
"ROSETLineBot" is proposed. In section 2, the structure, components and design of ROSETLineBot are explained. Then
the components of ROSETLineBot are described in the same section. The system integration and testing results are
presented in section 3. Finally, our conclusions are presented in section IV.
2. The structure of ROSETLineBot
In this section, 3D design steps, wheel kinematics, rothe robot electronics and control design of the robot are given in
detail.
2.1. 3D Model of ROSETLineBot
In the prototyping stage, SOLIDWORKS software was used in the design of the ROSETLineBot. In the prototyping
phase, PLA filament was used for 3D printing of the robot. Each part of the robot was printing, separately. And then,
each component was combined by using special fasteners.
Figure 2. 3D model of ROSETLineBot.


## Page 3


The structure of the robot mechanism consists of the mainframe, actuator wheel, dummy wheel, and control box. The
dummy wheel is mounted to the mainframe with the steel spring. Shafts produced from ASP23 high-speed steel have
been utilized in the special dimensions determined for strengthening the main body and the control box.
The robot moves on the test line by DC motor which is connected to the actuator wheel. The actuator and dummy wheels
grasp the power line by means of pulling force of the steel spring. While the actuator wheel moves only in its own axis,
the dummy wheel can move both in its own axis and in the vertical axis by force of the steel spring. When the robot faces
an obstacle while it is moving on the line, the spring opens when the actuator wheel is trying to pass the obstacle, the
robot gains suitable grip space with the expansion of the steel spring on the vertical axis. Thus, the obstacles can be
easily crossed. After passing the obstacle, the spring closes and the dummy wheel takes its actual position and keeps
going to its movement on the power line.
2.2. Wheel Kinematics
In this section, we consider only a simplified case of the robot movement for which the longitudinal slip between the
wheels and the power line can be neglected. In [30], velocities and forces on one wheel are described in detail. Forces
and velocities of a wheel which described in [30] are shown in Figure 3. A quarter vehicle model was used to calculate
velocity of the robot in this study. Equation (1) was used to calculate the velocity of the robot.
v=
Cnt×C
C pr ×n×dt
(1)
In Equation (1),  Cnt is the encoder count, C is the circumference of the wheel, Cpr is the counts per rotation of encoder, n
is the gear ratio of motor reductor and dt is the count period.
Figure 3. Wheel description for one-wheel-drive system [30].
2.3. Electronics Circuit Design
Electronics components of robot were chosen it to be affordable as it is aimed at one of the main objectives. Block
diagram of the electronics circuit is shown in Figure 4. An ATMega2560 microcontroller together with a L298 motor
driver were used as the main control unit. It got the velocity feedback from the quadrature encoder integrated with the
DC motor. The encoder had 34:1 gear ratio and 48 CPR, hence the total counts per revolution was 1632. That brought
precision to the measurement since the encoder is quite sensitive. 
Figure 4. Block diagram of the electronics circuit.


## Page 4


Besides the quadrature encoder, a 9DOF IMU was placed onto the robot in order to acquire orientation and acceleration.
Additionally, an XBee Pro module was used for remote operation and parameter setting. Although an S2B model having
a 120m range was used in this experiment, it’s easy to change it to a long range model since they’re pin compatible.
2.4. Control Algorithm
PID control which is shown in Equation (2) was used to control the velocity of the robot. The feedback was obtained by
data that was gathering from the motor encoder. Encoder values were converted to the velocity values by using Equation
(1).
u(t)=K pe(t)+Ki∫
0
t
e(t)dt +Kd
d
dt e(t)
(2)
In Equation (2),  u(t) is the control signal.  K p,  Ki, and  Kd are proportional, integral and derivative coefficients,
respectively.   e(t) is the error between actual and desired speed. In the PID control block, its coefficients were selected as
. K p=30, Ki=1, and Kd=0.1 by experimentally. The block diagram of the control algorithm is shown in Figure 5.
Figure 5. Block diagram of the control algorithm.
3. Experimental Studies
In this section, experimental results are shown graphically. Pictures of ROSETLineBot on the test line from different
perspectives is shown in Figure 6.  In the experiment, measured velocity, pitch, roll, and yaw values are shown in Figure
7 and 8 when reference velocity set as u(t)=20cm/sec. According to test results which are shown in figures 7 and 8,
PID control shows satisfying performance for the power line inspection robot. The experimental setup was conducted
with a 25mm diameter sagged actual power line cable in the laboratory. The objective was to maintain the velocity of
robot on a sagged line. Experimental results show the robot climbing the sagged cable. Figure 7 shows that the controller
maintained the velocity by increasing the control signal during the climbing and achieved an almost-stable ride. Figure 8
shows the orientation during ride. The oscillation was kept in ±10 degrees.


## Page 5


Figure 6. Pictures of ROSETLineBot on the test line from different perspectives.
Figure 7. Speed measurement on a sagged power line during speed control test.
Figure 8. Roll, picth, and yaw angles of  ROSETLineBot during speed control test.


## Page 6


4. Conclusion
The main purpose of the study is to examine the feasibility of error (problem) detection and identification operations
which can be performed by robotic systems on the power lines. Operations on the power line contain high-risks in terms
of occupational health and safety for humans. These risks sometimes lead to undesirable results. To prevent these deadly
results, robotic systems can be used for maintenance, repair and error detection operations of the electrical transmission
lines. In this study, a single-wheel-drive low-cost fully 3D printed mobile robot is designed and controlled for inspection
of the power transmission lines. In the experimental study which is presented in section 3 in detail, the velocity control of
the robot was performed by using PID control. It was observed that the robot was able to strongly grasp the power wire
and smoothly move on it. A sensor fusion control method was remained as the future work.
References
[1]
O. Menendez, F. A. Auat Cheein, M. Perez and S. Kouro, "Robotics in Power Systems: Enabling a More Reliable and Safe Grid,"
in IEEE Industrial Electronics Magazine, vol. 11, no. 2, pp. 22-34, June 2017. doi: 10.1109/MIE.2017.2686458
[2]
J. H. Yoo, C. Kim and D. H. Kim, "Mono-camera based simultaneous obstacle recognition and distance estimation for obstacle
avoidance of power transmission lines inspection robot," 2017 IEEE/RSJ International Conference on Intelligent Robots and
Systems (IROS), Vancouver, BC, Canada, 2017, pp. 6902-6907. doi: 10.1109/IROS.2017.8206613
[3]
S. Xiao and H. Wang, "Research on a novel bionic robot mechanism for power transmission lines inspection," 2016 IEEE
International  Conference  on  Robotics  and  Biomimetics  (ROBIO),  Qingdao,  2016,  pp.  1361-1366.  doi:
10.1109/ROBIO.2016.7866516
[4]
M. Jelisavcic, M. De Carlo, E. Haasdijk and A. E. Eiben, "Improving RL power for on-line evolution of gaits in modular robots,"
2016 IEEE Symposium Series on Computational Intelligence (SSCI), Athens, 2016, pp. 1-8. doi: 10.1109/SSCI.2016.7850166
[5]
K. Kurabe et al., "A robot controller for power distribution line maintenance robot working by task-level command," 2016 IEEE/
SICE International Symposium on System Integration (SII), Sapporo, 2016, pp. 441-446. doi: 10.1109/SII.2016.7844038
[6]
M. Koike, K. Kurabe, K. Yamashita, Y. Kato, K. Jinno and K. Tatsuno, "An approach to object recognition for a power
distribution line maintenance robot. The case of identifying a mechanical bolt to be tightened with a nut," 2016 International
Symposium on Micro-NanoMechatronics and Human Science (MHS), Nagoya, 2016, pp. 1-7. doi: 10.1109/MHS.2016.7824219
[7]
Y. Kato, M. Koike, K. Kurabe, K. Jinno, K. Yamashita and K. Tatsuno, "Task performance test on grasping the bolt by a power
distribution line maintenance experimental robot system," 2016 International Symposium on Micro-NanoMechatronics and
Human Science (MHS), Nagoya, 2016, pp. 1-7. doi: 10.1109/MHS.2016.7824232
[8]
Z. Qing, Z. Xiao-long, L. Xin-ping, X. Jie, Z. Ting and W. Cheng-jiang, "Mechanical design and research of a novel power lines
inspection robot," 2016 International Conference on Integrated Circuits and Microsystems (ICICM), Chengdu, 2016, pp. 363-366.
doi: 10.1109/ICAM.2016.7813625
[9]
G. Tao, L. Fang and Xuxin Lin, "Optimization design of the multi-unit serial inspection robot for power transmission line," 2016
4th  International  Conference  on  Applied  Robotics  for  the  Power  Industry  (CARPI),  Jinan,  2016,  pp.  1-6.  doi:
10.1109/CARPI.2016.7745637
[10] Xiang Yue, H. Wang, Yingchun Yang and Y. Jiang, "Geometric design of an inspection robot for 110kV power transmission
lines," 2016 4th International Conference on Applied Robotics for the Power Industry (CARPI), Jinan, 2016, pp. 1-5. doi:
10.1109/CARPI.2016.7745636
[11] Shiyu Xiao, H. Wang and Lie Ling, "Research on a novel maintenance robot for power transmission lines," 2016 4th International
Conference on Applied Robotics for the Power Industry (CARPI), Jinan, 2016, pp. 1-6. doi: 10.1109/CARPI.2016.7745642
[12] L. Wang and H. Wang, "A survey on insulator inspection robots for power transmission lines," 2016 4th International Conference
on Applied Robotics for the Power Industry (CARPI), Jinan, 2016, pp. 1-6. doi: 10.1109/CARPI.2016.7745639
[13] Z. Sun, D. Tang, D. Chen, M. Wang, B. Zeng and B. Wu, "Mechanical design of the finder, a teleoperated robot for vibration
damper recover on power line," 2016 International Conference on Advanced Robotics and Mechatronics (ICARM), Macau, 2016,
pp. 159-164. doi: 10.1109/ICARM.2016.7606912
[14] W. Chang, G. Yang, J. Yu, Z. Liang, L. Cheng and C. Zhou, "Development of a power line inspection robot with hybrid operation
modes," 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Vancouver, BC, Canada, 2017, pp.
973-978. doi: 10.1109/IROS.2017.8202263
[15] S. Dian, L. Chen, S. Hoang, M. Pu and J. Liu, "Dynamic balance control based on an adaptive gain-scheduled backstepping
scheme  for  power-line  inspection  robots,"  in  IEEE/CAA  Journal  of  Automatica  Sinica,  vol.  PP,  no.  99,  pp.  1-11.  doi:
10.1109/JAS.2017.7510721
[16] Edward Boje, Attitude and Position Estimation for a Power Line Inspection Robot, In IFAC-PapersOnLine, Volume 49, Issue 21,
2016, Pages 529-535, ISSN 2405-8963. doi: 10.1016/j.ifacol.2016.10.656.
[17] S. Dian, S. Hoang, M. Pu, J. Liu and L. Chen, "Gain scheduling based backstepping control for motion balance adjusting of a
power-line  inspection  robot,"  2016  35th  Chinese  Control  Conference  (CCC),  Chengdu,  2016,  pp.  441-446.  doi:
10.1109/ChiCC.2016.7553124
[18] N. Pouliot, P. L. Richard and S. Montambault, "LineScout Technology Opens the Way to Robotic Inspection and Maintenance of
High-Voltage Power Lines," in IEEE Power and Energy Technology Systems Journal, vol. 2, no. 1, pp. 1-11, March 2015. doi:
10.1109/JPETS.2015.2395388
[19] Y. Song, H. Wang and J. Zhang, "A Vision-Based Broken Strand Detection Method for a Power-Line Maintenance Robot," in
IEEE Transactions on Power Delivery, vol. 29, no. 5, pp. 2154-2161, Oct. 2014. doi: 10.1109/TPWRD.2014.2328572


## Page 7


[20] J. Patel and E. Boje, "Brachiating power line inspection robot," Proceedings of the 2014 3rd International Conference on Applied
Robotics for the Power Industry, Foz do Iguassu, 2014, pp. 1-6. doi: 10.1109/CARPI.2014.7030043
[21] E. Boje, "Modelling and control of a power supply for a power line inspection robot," Proceedings of the 2014 3rd International
Conference on Applied Robotics for the Power Industry, Foz do Iguassu, 2014, pp. 1-6. doi: 10.1109/CARPI.2014.7030039
[22] J. Y. Park, J. K. Lee, B. H. Cho and K. Y. Oh, "An Inspection Robot for Live-Line Suspension Insulator Strings in 345-kV Power
Lines," in IEEE Transactions on Power Delivery, vol. 27, no. 2, pp. 632-639, April 2012. doi: 10.1109/TPWRD.2011.2182620
[23] S. Han, R. Hao and J. Lee, "Inspection of Insulators on High-Voltage Power Transmission Lines," in IEEE Transactions on
Power Delivery, vol. 24, no. 4, pp. 2319-2327, Oct. 2009. doi: 10.1109/TPWRD.2009.2028534
[24] D.  Pernebayeva,  M.  Bagheri  and  A.  James,  "High  voltage  insulator  surface  evaluation  using  image  processing,"  2017
International  Symposium  on  Electrical  Insulating  Materials  (ISEIM),  Toyohashi,  2017,  pp.  520-523.  doi:
10.23919/ISEIM.2017.8166540
[25] H. Ha, S. Han and J. Lee, "Fault Detection on Transmission Lines Using a Microphone Array and an Infrared Thermal Imaging
Camera,"  in  IEEE  Transactions  on  Instrumentation  and  Measurement,  vol.  61,  no.  1,  pp.  267-275,  Jan.  2012.  doi:
10.1109/TIM.2011.2159322
[26] F. Zhang, G. Liu, L. Fang and H. Wang, "Estimation of Battery State of Charge With H∞ Observer: Applied to a Robot for
Inspecting Power Transmission Lines," in IEEE Transactions on Industrial Electronics, vol. 59, no. 2, pp. 1086-1095, Feb. 2012.
doi: 10.1109/TIE.2011.2159691
[27] https://www.hibot.co.jp/ecommerce/prod-detail/13 (Access Date: December 2017)
[28] EPRI – Electric Power Research Institute, “Robotic Transmission Line Inspections”,  Technical Brief, December 2009.
[29] https://enterprise.dji.com/news/detail/m200-power-line-inspection-tool  (Access Date: December 2017)
[30]K. Kozlowski and D. Pazderski (2004), “Modeling and Control of A 4-Wheel Skid-Steering Mobile Robot”,
International Journal of Applied Mathematics and Computer Science, Vol. 14, No. 4, pages 477-496.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
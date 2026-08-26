---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1806.04752v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1806.04752v1_Optimal_control_in_cancer_immunotherapy_by_the_application_of_particle_swarm_opt

> Source: 1806.04752v1_Optimal_control_in_cancer_immunotherapy_by_the_application_of_particle_swarm_opt.pdf

> Pages: 12

---


## Page 1


arXiv:1806.04752v1  [q-bio.QM]  8 Jun 2018
Optimal control in cancer immunotherapy by the application of particle swarm
optimization
Sima Sarv Ahrabi∗
Dipartimento di Scienze di Base e Applicate per l’Ingegneria, Sapienza Universit`a di Roma, Via Antonio Scarpa n. 16, 00161 Rome,
Italy
Abstract
In this article, a well-known mathematical model of cancer immunotherapy is discussed and used to represent
therapeutic protocols for cancer treatment. The optimal control problem is formulated based on the Pontrya-
gin maximum principle to deal with adoptive cellular immunotherapy, then the problem has been solved by the
application of particle swarm optimization (PSO) in combination with regular methods of solutions to optimal
control problems. The results are compared with those of other researchers. It is explained how the PSO algorithm
could be enlisted to obtain the optimal controls, then the obtained optimal controls are demonstrated to be more
appropriate to the elimination of cancer cells by using fewer amounts of external sources of medicines.
Keywords:
Cancer immunotherapy, ACI therapy, Optimal control, Pontryagin maximum principle, Particle
swarm optimization.
2000 MSC: 49J15, 49J30.
1. Introduction
In recent years, pioneering research has been undertaken into the cancer immunotherapy as a method of en-
hancing the features of cancer treatment [1–5]. Immunotherapy has been considered as one of the most eﬀective
methods of dealing reasonably with cancer by reinforcing humans’ natural defenses in order to cope with cancer.
Immunotherapy refers to the use of natural and synthetic substances to boost the immune response. The way that
immunotherapy functions is as follows:
• restraining or decreasing the growth of tumours.
• preventing cancer cells from spreading to adjoining organs.
• increasing the immune system’s capability to destroy cancer cells.
Over the past years, the dynamics of tumour-immune interaction have been investigated, resulting in the
development of various theoretical models in order to analyse the inﬂuence of immune system and tumour on each
other [2, 6–10]. In [11] the authors have widely discussed more mathematical models, incorporating systems of delay
and stochastic diﬀerential equations. The authors of [2] have represented a mathematical model of immunotherapy,
which is consisted of a system of three ordinary diﬀerential equations. The system, which is mentioned as the
∗sima.sarvahrabi@sbai.uniroma1.it
Preprint submitted to arXiv
June 14, 2018


## Page 2


Kirschner-Panetta model, expresses the interaction between tumour cells, eﬀector cells and IL-2, where the model
will be brieﬂy described in Section 2. The constant parameter s1 and s2 (see Eq. (1)), which denote respectively
the external sources of eﬀector cells and IL-2, have been considered in the model to stimulate the immune system.
Since the main goal in immunotherapy is to remove the tumour cells with the least probable medication side eﬀects,
an advanced version of the model may include a time dependent external sources of medical treatment, meaning
that the parameter s1 and s2 could be considered as control functions of time and therefore the optimum use of
medical sources can be evaluated in order to achieve the optimal measure of an objective function (the so-called
performance index). Thus the main goal, the elimination of cancer cells by using the minimum amount of medical
sources, can be expressed in terms of an optimal control problem.
Burden et al. [12] have investigated the Kirschner-Panetta model by using optimal control theory in order to
examine under what circumstances the tumor could be removed. They have considered a single ACI therapy in
which there is not an external source of IL-2. In [13], the authors have presented an optimal ACI therapy for the
same model by making a slight modiﬁcation to the performance index considered in [12]. Then, the results were
compared with those of the article [12]. In Section 3 the optimal control problem, which has been represented in
[13], will be dealt with by utilizing the PSO algorithm, then it is demonstrated that the obtained results are more
appropriate than those represented in [13]. The PSO algorithm is one of the most noticeable features of the ﬁeld of
nature-inspired metaheuristics. The PSO deals with an optimization problem by iteratively trying to improve the
solutions. PSO was originally introduced in [14, 15]. In the PSO algorithm, an imaginary population of particles is
deﬁned. The particles move in the search space. Each particle represents a solution for the optimization problem.
any particle is able to compare its position and solution with the best solutions and the best positions of the
neighbour particles. All particles are controlled to move towards the best position and then update their current
solutions. This process is reiterated until the best solution will be obtained. The PSO algorithm has experienced
many changes since its introduction in [14]. Many research has been conducted on the theoretical eﬀects of the
various parameters and aspects of the algorithm. More detailed studies of various aspects of the PSO algorithm
could be observed in [16–22]
An optimal multi-therapeutic schedule for the administration of eﬀectors and IL-2 has been determined in [23].
The control function u (t) has been deﬁned as the sum of h separate injections, where each injection is based on
the Dirac delta function. An optimization problem has been constructed and then, solved numerically by using
gradient descent method. The result shows a better condition in comparison with the untreated case, nonetheless,
the optimal schedule leads to an oscillation of cancer cells (see [23, Fig. 2 (c)]). More optimal control of cancer
immunotherapy could be observed in, for instance, [10, 24–26].
2. Kirschner-Panetta model
In [2], the authors have introduced a mathematical model consisted of a system of three ordinary diﬀerential
equations, which presents richly the immune-tumour dynamics. The Kirschner-Panetta model (KP model) indicates
the immune-tumour dynamics by deﬁning three populations, namely the eﬀector cells such as cytotoxic T-cells,
2


## Page 3


Table 1: Values of parameters in Eq. (1)
Values of parameters
Equation (1a)
Equation (1b)
Equation (1c)
0 ≤c ≤0.05
r2 = 0.18
p2 = 5
µ2 = 0.03
b = 1 × 10−5
g3 = 0.1
p1 = 0.1245
a = 1
µ3 = 10
g1 = 2 × 103
g2 = 10
x (t), the tumour cells, y (t) and the concentration of IL-2, z (t):
dx
dt = cy −µ2x + p1xz
g1 + z + s1 ,
(1a)
dy
dt = r2y (1 −by) −
axy
g2 + y ,
(1b)
dz
dt = p2xy
g3 + y −µ3z + s2 ,
(1c)
with the initial conditions
x (0) = x0 ,
y (0) = y0 ,
z (0) = z0 .
(2)
The stimulation of eﬀectors, x, is represented by the ﬁrst and third term on the right-hand side of Eq. (1a), where
the parameter c denotes the immunogenicity of the tumour, i.e. the ability of the tumour to provoke an immune
response and the third term (Michaelis-Menten kinetics) shows that eﬀector cells are stimulated by IL-2. The
parameter s1 represents an external source of eﬀectors such as LAK cells as medical treatments. µ2 indicates the
decay rate of the eﬀectors. Eq. (1b) expresses the rate of change of tumour cells which is described by logistic
growth r2y (1 −by) and the second term, the Michaelis-Menten term, shows the lose of tumour cells. Eq. (1c)
describes the rate of change of IL-2, produced as the result of interaction between eﬀectors and tumour cells. The
parameter µ3 denotes the decay rate of IL-2. The values of all parameters [2] in Eq. (1) are given in Table 1, where
the units are in day−1 except for b, g1, g2 and g3 whose units are volume.
A detailed stability analysis of the KP model has been discussed in the original article [2]. In immunotherapy,
where external source of eﬀector cells is used, for tumour with any immunogenicity, c, the eﬀect of ACI therapy
could results in elimination of tumour cells, while the level of administration of external eﬀector cells is almost
high (more than a critical level s1,cr = r2g2µ2
a
). Nevertheless, for tumours with smaller immunogenicity, the ACI
treatment must be started when the tumour is still in the early stages.
3


## Page 4


3. Adoptive cellular immunotherapy
In [13], the authors have represented an optimal control problem for the KP model
dx
dt = cy −µ2x + p1xz
g1 + z + s1u (t) ,
(3a)
dy
dt = r2y (1 −by) −
axy
g2 + y ,
(3b)
dz
dt = p2xy
g3 + y −µ3z ,
(3c)
with the initial conditions
x (0) = 1 ,
y (0) = 1 ,
z (0) = 1 .
(4)
The existence of solution to Eq. (3) can be observed by referring to [27, Theorem 9.2.1]. The control function u (t)
denotes the percentage of the external source of eﬀectors, s1, and therefore it is bounded by 0 ≤u (t) ≤1. The
goal is to design a protocol leading to eradication of cancer cells, y (t), at the end of treatment, in addition to using
the least amount of drug, and causing the level of cancer cells to be as low as possible and the levels of eﬀectors
and IL-2 to be remained at a high degree. Thus the performance index, which must be maximized, is obtained as
follows:
J (u) = −Ay (tf) +
Z tf
0

x (t) −y (t) + z (t) −1
2B(u (t))2

dt ,
(5)
where tf is the ﬁxed ﬁnal time and denotes the period of the treatment.
The linear payoﬀterm −Ay (tf) is
considered in order to minimize the level of tumour cells at the end of treatment, where A is a constant coeﬃcient.
The coeﬃcient B in quadratic term −1
2B(u (t))2 expresses the importance of minimizing u in comparison to
minimization of tumour cells. The terme x (t) −y (t) + z (t) is added to Eq. (5) with the intention of holding
the cancer cells at a low level, and the eﬀectors and IL-2 as high as possible during the treatment. The existence
and uniqueness of an optimal control has been proved in [12]. The Pontryagin maximum principle [28] is used to
formulate the necessary conditions of optimality. The Hamiltonian function [29] is as follows
H
=
x −y + z −1
2Bu2 + λ1

cy −µ2x + p1xz
g1 + z + s1u (t)

+λ2

r2y (1 −by) −
axy
g2 + y

+ λ3
 p2xy
g3 + y −µ3z

,
(6)
where λ1, λ2 and λ3 are the adjoint variables, and the adjoint system is:
dλ1
dt = −

1 + λ1

−µ2 +
p1z
g1 + z

−
ay
g2 + y λ2 +
p2y
g3 + yλ3

,
(7a)
dλ2
dt = −
"
−1 + cλ1 + (r2 −2r2by) λ2 −
ag2x
(g2 + y)2 λ2 +
p2g3x
(g3 + y)2 λ3
#
,
(7b)
dλ3
dt = −
"
1 +
p1g1x
(g1 + z)2 λ1 −µ3λ3
#
.
(7c)
The values of adjoint variables at the ﬁnal time tf are evaluated by using the transversality condition [27, Eq.
5.1-20]:
λ1 (tf) = 0 ,
λ2 (tf) = −A ,
λ3 (tf) = 0 .
(8)
4


## Page 5


The derivative of Hamiltonian (6) with respect to u is calculated as follows:
∂H
∂u = −Bu + λ1s1 .
(9)
In order to characterize the optimal control, there exist three cases [30, Eq. 8.6]:
1. If u (t) = 0, then ∂H
∂u ≤0, therefore λ1 ≤0 .
2. If 0 < u (t) < 1, then ∂H
∂u = 0, therefore u = s1
B λ1, where 0 < λ1 < B
s1 .
3. If u (t) = 1, then ∂H
∂u ≥0, therefore λ1 ≥B
s1 .
Thus, the characterization of optimality is:
u (t) =











0
if λ1 ≤0 ,
s1
B λ1
if 0 < λ1 < B
s1 ,
1
if λ1 ≥B
s1 .
(10)
The optimal control problem, described above, consists of state system (3), adjoint system (7), and optimality
condition (10). This is obviously a two-point boundary value problem, since the initial state of the state variables
(see (4)) and the ﬁnal state of the adjoint variables (see (8)) are known. Despite the fact that the general methods
of solving these types of problems are those such as the shooting method, the problem mentioned above may be
solved more straightforward due to the fact that state system (3) is independent of adjoint variables. Thus, an
initial guess for adjoint variables is made, by which the control function, u (t), can be evaluated referring to Eq.
(10). Using the obtained control function, u (t), state system (3) is solved forward in time, then adjoint system
(7) is updated backward in time by using the evaluated state variables. The process continues until the diﬀerences
between the current and previous values of state variables, adjoint variables, control function and the performance
index are within a speciﬁed error bound.
Although solving the problem sounds uncomplicated, here the main issue is that any initial guess for the
adjoint variables does not necessarily leads to ﬁnding the optimal control maximizing the performance index. In
most cases, the initial guess is such that the algorithm does not even converge to a solution and more important,
the convergence to the optimal control is almost impossible. As illustrated in [13], typical optimal controls for these
types of problems are generally bang-bang, in the sense that the optimal control switches periodically between lower
and upper bounds. This can be observed from Eq. (10). While B = 5 and s1 = 500 (see, for instance, [13, Fig.
2]), the value of B
s1 is 0.01 and therefore u is practically a bang-bang control.
Due to above statement, a hybrid of the PSO algorithm and the method mentioned above is used to ﬁnd the
optimal therapeutic protocol for the problem. First the optimal control and corresponding adjoint variables are
obtained by applying the PSO algorithm, where the control function, u (t), is considered to be a bang-bang control.
While a speciﬁed criterion is fulﬁlled (for instance, the convergence of the performance index), the algorithm is
switched to the above method to search for a probable better solution. The problem is solved for two diﬀerent set
of values of the parameters c, B and s1. The period of therapy is considered to be 350 days, i.e. tf = 350.
5


## Page 6


4. Discussion
The results are obtained for three diﬀerent cases, based on the choice of diﬀerent values for c, s1, and B. The
duration of therapy is consider to be 350 days, i.e. tf = 350:
Case 1: c = 0.04, s1 = 500, and B = 1. Fig. 1 shows the state variables, i.e. tumor cells (x), the eﬀector cells
(y), and the concentration of interleukin-2 (z). The non-tumor equilibrium point in this case is unstable because
the value of s1 is smaller than critical value s1,cr = 540 [2]. Nonetheless, the control pushes the system to the area
with smaller cancerous cells. In this work, in comparison with the work done in [13], the amount of total used
drug has been decreased (Fig. 2), and the maximum value of interleukin-2 is larger. The most important thing, in
this work, is that the objective function is maximized (J = 6449194) which is larger than the objective function
obtained in [13].
0
50
100
150
200
250
300
350
×104
0
2
4
x
y
z
0
50
100
150
200
250
300
350
States
×104
0
2
4
b
States Equations
Time
0
50
100
150
200
250
300
350
×104
0
5
10
c
Figure 1: State variables, (a): in this work, (b): in [13], (c): in [2] for c = 0.04, s1 = 500, B = 1.
Case 2: c = 0.025, s1 = 550, and B = 1. The results are shown in Figs. 3 and 4. Since s1 > s1,cr, the
non-tumour state is stable. Thus, it is expected that the tumor completely inhibited.
Fig. 3 shows that the
maximum value of the tumour has been minimized over the treatment. In addition, as it is illustrated in Fig. 4,
The performance index has been maximized in comparison with [13].
Case 3: c = 0.04, s1 = 550, and B = 10000. The results are shown in Figs. 5 and 6. Since s1 > s1,cr,
the non-tumour state is stable. The stress is here on minimizing the total amount of administration, since the
parameter B has been chosen to be very large. The performance index has been maximized in comparison with
the work done in [13]. The maximum value of tumour cells are at a lower level compared with [13].
6


## Page 7


0
50
100
150
200
250
300
350
0
0.5
1
J=6449194.5058
0
50
100
150
200
250
300
350
u(t)
0
0.5
1
J=5945999.9678
b
Control
Time
0
50
100
150
200
250
300
350
-1
0
1
c
Figure 2: Optimal Control, (a): in this work, (b): in [13], (c): in [2] for c = 0.04, s1 = 500, B = 1.
0
50
100
150
200
250
300
350
×104
0
1
2
3
a
x
y
z
0
50
100
150
200
250
300
350
States
×104
0
1
2
3
b
States Equations
Time
0
50
100
150
200
250
300
350
×105
0
1
2
3
c
Figure 3: State variables, (a): in this work, (b): in [13], (c): in [2] for c = 0.025, s1 = 550, B = 1.
7


## Page 8


0
50
100
150
200
250
300
350
0
0.5
1
J=6555432.9644
a
0
50
100
150
200
250
300
350
u(t)
0
0.5
1
J=6181566.5315
b
Control
Time
0
50
100
150
200
250
300
350
-1
0
1
c
Figure 4: Optimal Control, (a): in this work, (b): in [13], (c): in [2] for c = 0.025, s1 = 550, B = 1.
0
50
100
150
200
250
300
350
×104
0
2
4
a
x
y
z
0
50
100
150
200
250
300
350
States
×104
0
1
2
3
b
States Equations
Time
0
50
100
150
200
250
300
350
×104
0
5
10
c
Figure 5: State variables, (a): in this work, (b): in [13], (c): in [2] for c = 0.04, s1 = 550, B = 10000.
8


## Page 9


0
50
100
150
200
250
300
350
0
0.5
1
J=5313022.3299
a
0
50
100
150
200
250
300
350
u(t)
0
0.5
1
J=4981214.5035
b
Control
Time
0
50
100
150
200
250
300
350
-1
0
1
c
Figure 6: Optimal Control, (a): in this work, (b): in [13], (c): in [2] for c = 0.04, s1 = 550, B = 10000.
9


## Page 10


5. Conclusion
As it was shown, by using the hybrid method of PSO and forward-backward sweep method the obtained results
are much better and more acceptable than those represented in other research. Using the PSO algorithm along
with classical methods for numerical solution of optimal controls deﬁnitely improves the performance of ﬁnding
the optimal control. It is a fact that classical approaches are very time-consuming, since any initial guess cannot
guarantee the convergence.
References
References
[1] S. A. Rosenberg, M. T. Lotze, Cancer immunotherapy using interleukin-2 and interleukin-2-activated lympho-
cytes, Annual review of immunology 4 (1) (1986) 681–709.
[2] D. Kirschner, J. C. Panetta, Modeling immunotherapy of the tumor–immune interaction, Journal of mathe-
matical biology 37 (3) (1998) 235–252.
[3] S. A. Rosenberg, J. C. Yang, N. P. Restifo, Cancer immunotherapy: moving beyond current vaccines, Nature
medicine 10 (9) (2004) 909.
[4] S. A. Rosenberg, Il-2: the ﬁrst eﬀective immunotherapy for human cancer, The Journal of Immunology 192 (12)
(2014) 5451–5458.
[5] E. Tran, P. F. Robbins, S. A. Rosenberg, ’ﬁnal common pathway’of human cancer immunotherapy: targeting
random somatic mutations, Nature immunology 18 (3) (2017) 255.
[6] V. A. Kuznetsov, I. A. Makalkin, M. A. Taylor, A. S. Perelson, Nonlinear dynamics of immunogenic tumors:
parameter estimation and global bifurcation analysis, Bulletin of mathematical biology 56 (2) (1994) 295–321.
[7] J. Adam, Eﬀects of vascularization on lymphocyte/tumor cell dynamics: Qualitative features, Mathematical
and computer modelling 23 (6) (1996) 1–10.
[8] R. De Boer, P. Hogeweg, H. Dullens, R. A. De Weger, W. Den Otter, Macrophage T lymphocyte interactions
in the anti-tumor immune response: a mathematical model., The journal of immunology 134 (4) (1985) 2748–
2758.
[9] S. Banerjee, R. R. Sarkar, Delay-induced model for tumor–immune interaction and control of malignant tumor
growth, Biosystems 91 (1) (2008) 268–288.
[10] F. Castiglione, B. Piccoli, Optimal control in a model of dendritic cell transfection cancer immunotherapy,
Bulletin of mathematical biology 68 (2) (2006) 255–274.
[11] R. Eftimie, J. L. Bramson, D. J. Earn, Interactions between the immune system and cancer: a brief review of
non-spatial mathematical models, Bulletin of mathematical biology 73 (1) (2011) 2–32.
10


## Page 11


[12] T. N. Burden, J. Ernstberger, K. R. Fister, Optimal control applied to immunotherapy, Discrete and Contin-
uous Dynamical Systems Series B 4 (1) (2004) 135–146.
[13] A. Ghaﬀari, N. Naserifar, Optimal therapeutic protocols in cancer immunotherapy, Computers in biology and
medicine 40 (3) (2010) 261–270.
[14] J. Kennedy, R. Eberhart, C. 1995. particle swarm optimization, in: IEEE International Conference on Neural
Networks (Perth, Australia), IEEE Service Center, Piscataway, NJ, pp. 1942–1948.
[15] Y. Shi, R. Eberhart, A modiﬁed particle swarm optimizer, in: Evolutionary Computation Proceedings, 1998.
IEEE World Congress on Computational Intelligence., The 1998 IEEE International Conference on, IEEE,
1998, pp. 69–73.
[16] J. Kennedy, R. Mendes, Neighborhood topologies in fully informed and best-of-neighborhood particle swarms,
IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews) 36 (4) (2006)
515–519.
[17] J. Kennedy, R. Mendes, Population structure and particle swarm performance, in: Evolutionary Computation,
2002. CEC’02. Proceedings of the 2002 Congress on, Vol. 2, IEEE, 2002, pp. 1671–1676.
[18] R. Mendes, Population topologies and their inﬂuence in particle swarm performance, PhD Final Dissertation,
Departamento de Inform´atica Escola de Engenharia Universidade do Minho.
[19] R. Mendes, J. Kennedy, J. Neves, The fully informed particle swarm: simpler, maybe better, IEEE transactions
on evolutionary computation 8 (3) (2004) 204–210.
[20] T. Ying, Y.-p. Yang, J.-c. Zeng, An enhanced hybrid quadratic particle swarm optimization, in: Intelligent
Systems Design and Applications, 2006. ISDA’06. Sixth International Conference on, Vol. 2, IEEE, 2006, pp.
980–985.
[21] M. R. Bonyadi, Z. Michalewicz, Particle swarm optimization for single objective continuous space problems:
a review, MIT Press, 2017.
[22] S. Alam, G. Dobbie, Y. S. Koh, P. Riddle, S. U. Rehman, Research on particle swarm optimization based
clustering: a systematic review of literature and techniques, Swarm and Evolutionary Computation 17 (2014)
1–13.
[23] A. Cappuccio, F. Castiglione, B. Piccoli, Determination of the optimal therapeutic protocols in cancer im-
munotherapy, Mathematical biosciences 209 (1) (2007) 1–13.
[24] F. Castiglione, B. Piccoli, Cancer immunotherapy, mathematical modeling and optimal control, Journal of
theoretical Biology 247 (4) (2007) 723–732.
[25] K. R. Fister, J. H. Donnelly, Immunotherapy: an optimal control theory approach., Mathematical biosciences
and engineering: MBE 2 (3) (2005) 499–510.
11


## Page 12


[26] S. Khajanchi, D. Ghosh, The combined eﬀects of optimal control in cancer remission, Applied Mathematics
and Computation 271 (2015) 375–388.
[27] D. L. Lukes, Diﬀerential equations: classical to controlled, Elsevier, 1982.
[28] L. S. Pontryagin, Mathematical theory of optimal processes, CRC Press, 1987.
[29] D. E. Kirk, Optimal control theory: an introduction, Courier Corporation, 2012.
[30] S. Lenhart, J. T. Workman, Optimal control applied to biological models, Crc Press, 2007.
12

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
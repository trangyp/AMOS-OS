---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1803.05025v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1803.05025v1_FDG_kinetics_in_cells_and_tissues__a_biochemically-driven_compartmental_approach

> Source: 1803.05025v1_FDG_kinetics_in_cells_and_tissues__a_biochemically-driven_compartmental_approach.pdf

> Pages: 36

---


## Page 1


FDG kinetics in cells and tissues: a
biochemically-driven compartmental approach
Mara Scussolini · Vanessa Cossu ·
Cecilia Marini · Gianmario Sambuceti ·
Giacomo Caviglia
Abstract The radioactive glucose analogue 2-deoxy-2-[18F]ﬂuoro-D-glucose
(FDG) is widely used to reconstruct glucose metabolism and other biologi-
cal functions in cells and tissues. The analysis of data on the time course of
FDG tracer distribution is performed by the use of appropriate compartmen-
tal models. Motivated by recent results in cell biochemistry, we describe a new
compartmental model aiming at the reconstruction of tracer kinetics in cells
and tissues, which emphasizes the diﬀerent roles of the cytosol and of the endo-
plasmic reticulum. Two applications of the new model are examined, that are
concerned with real data from cancer cell cultures in vitro, and cancer tissues
in vivo. The results are compared with those obtained through application of
more standard compartmental models against the same datasets and appear
to be in a better agreement with respect to recent biochemical experimental
evidence. In particular, it is shown that tracer tends to accumulate in the en-
doplasmic reticulum, rather than cytosol, and that the rate of phosphorylation
is higher than predicted by current models.
M. Scussolini
Dipartimento di Matematica, Universit`a di Genova, Via Dodecaneso 35, 16146 Genova, Italy
E-mail: scussolini@dima.unige.it
V. Cossu
Dipartimento di Medicina Nucleare, IRCCS-IST San Martino, Salita Superiore della Noce
29, 16131 Genova, Italy
C. Marini
Dipartimento di Medicina Nucleare, IRCCS-IST San Martino, Salita Superiore della Noce
29, 16131 Genova, Italy, and Dipartimento di Scienze della Salute, Universit`a di Genova,
Via Antonio Pastore 1 16132, Genova, Italy, and CNR Istituto di Bioimmagini e Fisiologia
Molecolare (IBFM), Via Fratelli Cervi 93, 20090 Milano, Italy
G. Sambuceti
Dipartimento di Medicina Nucleare, IRCCS-IST San Martino, Salita Superiore della Noce
29, 16131 Genova, Italy, and Dipartimento di Scienze della Salute, Universit`a di Genova,
Via Antonio Pastore 1, 16132 Genova, Italy
G. Caviglia
Dipartimento di Matematica, Universit`a di Genova, Via Dodecaneso 35, 16146 Genova, Italy
arXiv:1803.05025v1  [q-bio.TO]  13 Mar 2018


## Page 2


2
Mara Scussolini et al.
Keywords Tracer kinetics · Compartmental analysis · Nuclear medicine
data · Identiﬁability · Numerical inverse problems · Cancer
Mathematics Subject Classiﬁcation (2000) 92C45 · 34A30 · 65R32 ·
62P10
1 Introduction
The radiopharmaceutical tracer 2-deoxy-2-[18F]ﬂuoro-D-glucose (FDG) is ex-
tensively used to reconstruct glucose metabolism in cells and tissues, especially
in nuclear medicine. Following glucose path, FDG is ﬁrst transported through
cell membranes and is then trapped inside cells by phosphorylation. However,
unlike phosphorylated glucose, phosphorylated FDG tends to accumulate in
cells. For this reason, the measurable radioactive amount of FDG is consid-
ered an accurate marker of overall glucose uptake and consumption by cells
and tissues (Cherry et al., 2012; Schmidt and Turkheimer, 2002; Wernick and
Aarsvold, 2004). In addition, FDG assumption by cancer cells is increased by
the Warburg eﬀects for glucose (Vander et al., 2009); consequently, FDG is
used in cancer detection and staging, and to assess the eﬀectiveness of medical
treatments.
A basic datum for a detailed analysis of FDG kinetics is the time course of
FDG concentration. Concentration of FDG in a suitable region of interest of
the target tissue in vivo is reconstructed by the use of Positron Emission
Tomography (PET) (Bailey et al., 2005; Ollinger and Fessler, 1997). In a
forthcoming work by our group (Scussolini et al. manuscript in preparation),
the time dependent activity curve of FDG uptake by a cancer cell culture
has been measured also in vitro by the use of a LigandTracer (LT) device of
Ridgeview Instruments AB Sweden. The LT technology was ﬁrst described in
Bj¨orke and Andersson (2006a) and Bj¨orke and Andersson (2006b).
In general, the measured time dependent radioactive signal coming from a
target biological system results from superposition of signals emitted by FDG
sources occupying, e.g., interstitial tissue, blood, and cells, possibly in either
free or phosphorylated forms. Since available measurement devices cannot re-
solve single emitters, a compartmental model approach is applied, whereby a
detailed characterization of tracer kinetics can be reconstructed (Watabe et
al., 2006). Essentially, compartments represent uniform spatial distributions
or speciﬁc chemical compounds of the basic radioactive molecules; radioactiv-
ity concentrations in the various compartments are the natural state variables
of the system; tracer ﬂow, resulting from interchange of radioactive molecules
between compartments, is modeled by a Cauchy problem for a system of lin-
ear ordinary diﬀerential equations (ODEs) for concentrations; the constant
coeﬃcients, also called rate constants or kinetic parameters, represent tracer
kinetics and may be related to the action of enzymes, such as hexokinase (HK)
responsible for phosphorylation in cells.
In typical compartmental problems the rate coeﬃcients are unknown. The
measured data are the total amount of tracer (concentration or activity) in a


## Page 3


FDG kinetics in cells and tissues
3
given region of interest, and the input function (IF), describing the time rate of
tracer carried into the system. Tracer kinetics results from the solution of the
inverse problem of determining the unknown rate coeﬃcients compatible with
the data, and the subsequent explicit determination of the concentration (or
activity) of each compartment through the solution of the system of ODEs. In
the applications presented in this paper, the inverse problem is solved in two
steps: ﬁrst, a formal expression of the solution of the direct Cauchy problem is
evaluated, where dependence on the unknown rate constants is made explicit;
second, an inversion algorithm is applied in order to recover the kinetic param-
eters through comparison of the formal solution with the data. The inversion
algorithm makes use of an optimization regularization method which is based
on a Newton-type algorithm.
“Classical” compartmental models have been developed under the assump-
tion that phosphorylation and dephosphorylation of FDG occur in the same
intracellular cytosolic volume, as described by Sokoloﬀet al. (1977) and Wer-
nick and Aarsvold (2004). Recent progresses in cell biochemistry have shown
that the appropriate location of dephosphorylation is the endoplasmic reticu-
lum (ER) (Ghosh et al., 2002), which is spatially separated from cytosol. The
schematic path of FDG kinetics is illustrated in Fig. 1.
Fig. 1 The biochemical path of FDG inside the cell: the FDG moves in and out the cell
environment thanks to GLUT transporters; once inside the cytosol of the cell, free FDG
is phosphorylated by hexokinase (HK) and the phosphorylated FDG (FDG6P) can enter
the endoplasmic reticulum (ER) transported by G6PT; only inside the ER, FDG6P can
be dephosphorylated by G6Pase, after which the FDG turns back in a free status and is
released out into the cytosol
Following this pattern for FDG kinetics in the cell, here we describe and for-
malize a new model consisting of three compartments which account for free
FDG in cytosol, phosphorylated FDG in cytosol, and phosphorylated FDG
in ER. The new biochemically-driven compartmental model is referred to as
BCM; a classical simpliﬁed compartmental model (SCM) is recovered from the
proposed model under the assumption that the ER is removed from consider-
ation. In the forthcoming paper (Scussolini et al. manuscript in preparation),
as a ﬁrst test of its feasibility, the new BCM has been directly applied to the
analysis of data coming from highly controlled in vitro experiments on FDG
uptake by cell cultures. Attention has been concentrated on: (1) the calibra-
tion procedure of the LT device, which has been used for the generation of
the data; (2) the examination of tracer kinetics when cells were exposed to
diﬀerent glucose concentrations, in order to assess FDG-glucose competition;


## Page 4


4
Mara Scussolini et al.
(3) the biological interpretation of the results. It has been found that tracer
tends to accumulates in the ER, a result which has been conﬁrmed by direct
measurement on cells seeded in vitro and immersed in ﬂuorescent 2DG ana-
logue NBDG; moreover, the value of the rate constant for phosphorylation
estimated by application of BCM is greater than that produced by classical
SCM, and shows better agreement with results of direct measurements avail-
able in the literature (Gao et al., 2015; Muzi et al., 2001).
The analysis of the forthcoming paper by Scussolini et al. (manuscript in
preparation) embodies the fundamental role of ER in the description and un-
derstanding of tracer kinetics of cancer cell cultures. On this basis, the main
aims of the present paper are described as follows. (1) To re-examine FDG
kinetics in a single cell, in order to construct a new general compartmental
model for tracer kinetics capable of being extended to more complex systems,
such as cell cultures and tissues, and to verify its applicability. (2) To an-
alyze the mathematical properties of BCM, such as identiﬁability, and the
connections with the diﬀerent types of available data. (3) To compare recon-
structions of tracer kinetics following from application of BCM and standard
SCM to the same set of data, concerning either cancer cell cultures or cancer
tissues. (4) To discuss consistency and interpretation of the results obtained
from applications to cell cultures and tissues. (5) To conﬁrm tracer accumula-
tion in ER, and increase in the estimated value of the phosphorylation rate in
the new broader framework. For completeness and for ease of comparison and
interpretation, results on cell cultures are brieﬂy reviewed and new data are
analyzed with respect to the forthcoming paper (Scussolini et al. manuscript
in preparation).
The new mathematical models, and the related features, for compartmental
analysis of tracer kinetics in cell cultures and tissues are introduced and exam-
ined in Section 2. Section 3 deals with application on data from cell cultures
in vitro, while Section 4 deals with data from tissues in vivo. Our comments
and conclusions on the results are oﬀered in Section 5.
2 Basic mathematical model for tracer kinetics in cell cultures and
tissues
FDG kinetics provides an analogue of glucose metabolism in cells and tis-
sues. Starting from local measurements on the diﬀusion of these radioactive
molecules, it allows a quantiﬁcation of functions in living cells, such as rates
of activity of enzymes. To this aim, a suitable set of diﬀerent functional com-
partments is identiﬁed in the assigned target, where each compartment is
associated with a speciﬁc metabolic state of the tracer, possibly contained
in a predeﬁned physiologic volume. Tracer ﬂow corresponds to exchange of
radioactive molecules between compartments. Most considered approaches to
tracer kinetics are based on application of such compartmental models.


## Page 5


FDG kinetics in cells and tissues
5
In this section we examine a new compartmental model originating from
the analysis of the biochemical path of FDG, and partially of glucose, in a
single cell. The mathematical counterpart of this compartmental description of
intracellular tracer kinetics is given by a system of three linear ODEs for three
unknown concentrations and with ﬁve unknown constant coeﬃcients. We recall
that the constant coeﬃcients are the rate constants. Extensions to cell culture
and tissue systems are then introduced, illustrating how the general scheme is
adapted to the analysis of data provided by allowable measurement devices.
In so doing, additional parameters of physiologic interest are introduced, in
order to formulate more realistic models. A simpliﬁed model is also examined,
for the ease of comparison with most diﬀused existing models. To go deeply
into the mathematical aspects, we deal with the problem of retrieving the rate
constants as solutions of an inverse problem. The corresponding uniqueness
problem is also discussed.
(a) BCM
(b) SCM
Fig. 2 The two compartmental models considered in this work: (a) the biochemically-
driven compartment model (BCM) accounting for compartments i of input tracer, f of free
tracer in the cytosol, p of cytosolic phosphorylated tracer, and r of ER-localized phosphory-
lated tracer. (b) The simpliﬁed compartmental model or Sokoloﬀ-type compartmental model
(SCM) considering the input pool i, the tracer in a free status inside the cell f and the phos-
phorylated tracer trapped by the cell p. The arrows connecting the functional compartments
represent the model kinetic parameters, which are denoted as k for the BCM and as k∗for
the SCM


## Page 6


6
Mara Scussolini et al.
2.1 The model: single cell perspective
Consider a cell which is in contact with a liquid containing glucose at physio-
logic concentration and FDG at a smaller concentration, so that FDG may be
regarded as a perturbation of glucose. This general situation is representative
of any cells coming into contact with glucose and FDG, both in vitro and in
vivo. The biochemical path of glucose and FDG uptake inside the cell may be
characterized according to the following scheme. FDG is transported into the
cytosol, and back, by glucose transport proteins (GLUT). Inside the cell, glu-
cose and FDG are phosphorylated by hexokinase (HK) to G6P and FDG6P,
respectively. Once phosphorylated, glucose continues along the metabolic path-
way of glycolysis and pentose-phosphate pathway or participates to glycogen
synthesis; instead, FDG cannot follow the same channels and accumulates in-
tracellularly as FDG6P. It is well known that FDG6P is a substrate for G6Pase
but, according to recent advances in biological chemistry, G6Pase is anchored
to the endoplasmic reticulum (ER) (Ghosh et al., 2002) so that its action of
hydrolysis of FDG6P, resulting in the creation of a phosphate group and free
tracer, occurs after FDG6P has been transported into the ER lumen by glu-
cose 6-phosphate transporter (G6PT). Subsequently, the free tracer is released
into the cytosol.
The whole process is illustrated symbolically in Fig. 2(a), which in turn
is consistent with Fig. 1. The “squares” i, f, p, r identify the compartments
associated with the main steps of tracer kinetics. Speciﬁcally, lower indexes
i, f, p, and r refer systematically to tracer in the input pool, free tracer in
the cytosol, phosphorylated tracer in the cytosol, phosphorylated tracer in the
ER. In principle, a pool for free tracer in ER could also be considered, which
receives tracer also from the free compartment in cytosol; here we assume that
its equilibrium value is reached almost instantaneously at the beginning of the
experiment and represents a small fraction of tracer contained in ER, so that
it is discarded.
We assume that standard assumptions for application of compartmen-
tal models are satisﬁed. In particular, underlying physiological processes and
molecular interactions are not aﬀected by the presence of tracer, distribution
of tracer in each compartment is spatially homogeneous, and tracer exchanged
between compartments is instantaneously mixed (Cherry et al., 2012; Schmidt
and Turkheimer, 2002; Wernick and Aarsvold, 2004). We also assume that ap-
propriate correction for the physical decay of radioactivity has been applied.
We denote by cf, cp, and cr the time dependent and decay corrected con-
centrations of tracer in the compartments inside a cell, which are regarded
as the state variables. The concentration of tracer in the external medium,
ci, is the given input function of the system. The system of ODEs for the
biochemically-driven compartmental model (BCM) is





˙cf = −(k2 + k3) cf + k6 cr + k1 ci
˙cp = k3 cf −k5 cp
˙cr = k5 cp −k6 cr
,
(1)


## Page 7


FDG kinetics in cells and tissues
7
where the superposed dot denotes the time derivative, and explicit reference
to time dependence is omitted. Time is measured in minutes. The initial con-
ditions are cf(0) = cp(0) = cr(0) = 0, which mean that there is no tracer
amount in the cell at the beginning of the experiment. The rate constants ki
(1/min), with i ∈{1, 2, 3, 5, 6}, describe the ﬁrst order process of tracer trans-
fer between compartments. In each equation, products of rate constants and
concentrations represent ﬂuxes of tracer per unit time and unit volume; plus
and minus signs refer to incoming and outgoing ﬂuxes, respectively. The system
(1) expresses conservation of the tracer interchanged between free, phospho-
rylated and reticular compartments. In view of natural applications and for
the ease of comparison of the results, we have adopted the usual notations of
nuclear medicine for the rate constants, as done by Cherry et al. (2012) and
by Wernick and Aarsvold (2004).
Consistently with Fig. 2(a), the parameters k1 and k2 are the kinetic pa-
rameters for transport of FDG from medium to cell and back from cell to
medium, respectively; k3 is the phosphorylation rate of FDG; k5 is the input
rate of FDG6P into ER; k6 refers to the dephosphorylation rate of FDG6P to
FDG. Since the dephosphorylation occurs only inside the ER, a parameter k4,
corresponding to an arrow from p to f, is not considered. The values of the rate
constants depend on the conditions of the experiment: for example, they are
inﬂuenced by the amount of glucose present in the surrounding environment.
Consider the system (1) with vanishing initial conditions and deﬁne the
vector k5 = (k1, k2, k3, k5, k6). The direct problem consists in ﬁnding the solu-
tion of the system of ODEs in the unknowns cf, cp, and cr, for a given vector
k5 and input function ci. Here, we are mainly concerned with the inverse prob-
lem of ﬁnding FDG kinetics, i.e., determining the vector k5 of rate coeﬃcients
which corresponds to a given set of data. Following standard approaches, the
data are the input function ci and the total tracer concentration cT inside the
cell. The connection between cT and the state variables is obtained as follows.
Denote by vcyt and ver the cell volumes of cytosol and ER, respectively,
where intracellular tracer is located. The total activity aT inside the cell is
given by
aT = vcyt (cf + cp) + vercr .
(2)
On letting cT = aT /(vcyt + ver) be the total density, it is found that
cT = (1 −vr) (cf + cp) + vr cr ,
(3)
where vr = ver/(vcyt + ver) is the volume fraction of the ER. Henceforth we
regard vr as a given experimental parameter. The expression (3) for the total
density agrees with similar expression that can be found in the literature on
tracer kinetics in tissues (see, e.g., Wernick and Aarsvold (2004)).
In principle, cT (or aT ) may be regarded as a physical quantity whose
time course is determined by measurement procedures. Then (3) provides the
connection between the measured quantity cT and the solution of the system
(1), expressed in terms of k5. Therefore, (3) is the starting point for the solution
of the inverse problem.


## Page 8


8
Mara Scussolini et al.
2.2 Cell cultures and tissue systems
The crucial point of the previous formulation is the remark that, usually, a
single cell is not accessible to measurements of radiation emitted in time.
Applications are based on observation of the time course of radiation emitted
by cell cultures in vitro or tissues in vivo. Thus the model described in Fig. 2(a)
has to be adapted to applications on a higher scale. For example, if we consider
a colony of N cells, it is natural to deﬁne the concentration of free tracer of the
colony as Cf = N cf, and so on. Similarly, we denote by Cf the concentration
of free tracer in a given tissue.
Accordingly, we introduce the (macroscopic) state variables Cf, Cp, and
Cr which describe the concentrations of free tracer, phosphorylated tracer
in cytosol, and phosphorylated tracer ER, respectively. It is assumed that
the corresponding system of ODEs takes the form (1), which is rewritten
compactly as
˙C = M C + k1 Ci e
C(0) = 0 ,
(4)
where
M =


−(k2 + k3)
0
k6
k3
−k5
0
0
k5 −k6

, C =


Cf
Cp
Cr

, e =


1
0
0

,
(5)
and where Ci is the given input function. The rate constants maintain the
interpretation discussed in the previous subsection. The analytic solution of
the Cauchy problem (4) takes the form
C(t; k5, Ci) = k1
Z t
0
eM (t−τ) e Ci(τ) dτ ,
(6)
with the time variable t ∈R+.
The system (4) is regarded as the basic mathematical formulation of com-
partmental analysis adopted in this work. Equation (6) provides the solution
of the direct problem, at given k5. Before dealing with the inverse problem,
the connection with data for both cell cultures and tissues must be considered
rather carefully.
2.2.1 Data for cell cultures and activity formulation
Available data on the time course of radioactivity for a cell culture are given
in terms of total activity. In principle, rephrasing of the data in concentrations
was allowed but this required, at least, the knowledge of parameters such as
the total number of cells, and the volumes of cytosol and ER. These param-
eters are only roughly known. Besides other advantages, the reformulation of
the system (4) in activities allows to reduce the parameters to one, precisely,
the ratio between the volumes of the cytosol and ER, which can be estimated
and is independent of the number of cells.


## Page 9


FDG kinetics in cells and tissues
9
Concentrations and corresponding activities of the cell culture are related
by
Cf = Af
Vcyt
,
Cp = Ap
Vcyt
,
Cr = Ar
Ver
,
Ci = Ai
Vi
,
(7)
where Vcyt, Ver, and Vi are the volumes of the total cytosolic region, ER, and
external liquid, respectively. Substitution of the activities into the system (4)
leads to the formulation of the Cauchy problem
˙A = M A + ¯k1 Aie ,
A(0) = 0 ,
(8)
where
A =


Af
Ap
¯Ar

,
¯Ar = Ar
Vcyt
Ver
,
¯k1 = k1
Vcyt
Vi
,
(9)
and where Ai is the given input function, representing in our case the total
activity of the incubation medium in which cells are immersed. Notice that
the matrices M and e are left unchanged by the transformation of the state
variables. The auxiliary variable ¯Ar is related to the “natural” activity Ar of
the ER through the dimensionless ratio Vcyt/Ver, which is independent of the
number of cells and coincides with vcyt/ver. Accordingly, we ﬁnd
Ar = v ¯Ar ,
v = Ver
Vcyt
= ver
vcyt
,
(10)
where in particular v < 1 (Milo and Phillips, 2015). The coeﬃcient ¯k1 =
k1Vcyt/Vi provides the rate constant adapted to the description in terms of
activities and plays the same role as k1. The other coeﬃcients k2, k3, k5,
and k6 preserve the interpretation as rate constants and the numerical value
pertaining to the system (4).
The analytic solution of the Cauchy problem (8) takes the form
A(t; ¯k5, Ai) = ¯k1
Z t
0
eM (t−τ) e Ai(τ) dτ ,
(11)
where, by a slight abuse of language, we let ¯k5 = (¯k1, k2, k3, k5, k6).
Denote as AT the measured time course of the total activity of the cell
culture. Following the analogy with equation (2), we have
AT = Af + Ap + Ar = Af + Ap + v ¯Ar .
(12)
Equation (12) may be written in compact form as
AT (t) = α A(t; ¯k5, Ai) ,
α =

1 1 v

.
(13)
Equation (13) is the basic equation for the formulation of the inverse problem
of determining the rate coeﬃcients, in that it relates measured quantities of
cell culture system to formal expressions of the unknown vector ¯k5.


## Page 10


10
Mara Scussolini et al.
2.2.2 Data for tissues
Widely applied models for tracer kinetics in tissues assume that tracer is ini-
tially injected into blood. Next it is carried from blood to tissues and cells;
once it has reached the target tissue, it may remain in cells, mainly in phos-
phorylated form, or may be transported back to blood in free form. A small
percentage of phosphorylated tracer can be dephosphorylated. In the corre-
sponding compartmental formulation it has been customary to consider a com-
partment corresponding to blood, and two tissue compartments, for free and
phosphorylated tracer, respectively. In particular, the compartment for free
tracer accounted for both free interstitial tracer and free intracellular tracer
(Schmidt and Turkheimer, 2002; Sokoloﬀet al., 1977).
In order to insert into the tissue scheme details on tracer kinetics in cells,
we consider:
– a blood compartment of concentration Ci, providing the input function;
– a compartment of concentration Cf, for free tracer in the interstitial space
and in the cytosol of tissue cells;
– a compartment of concentration Cp, for phosphorylated tracer in cytosol;
– a compartment of concentration Cr, for phosphorylated tracer in ER.
According to this BCM approach, tracer kinetics is still described by the
Cauchy problem (4) for concentrations, with analytic solution C given by
equation (6).
The data are the input function Ci and the concentration CT , measured
over a suitable region of interest, belonging to the target tissue. We show that
CT is a weighted sum of the state variables Cf, Cp, Cr, and Ci.
The volume Vtot of the region of interest may be partitioned as
Vtot = Vblood + Vint + Vcyt + Ver ,
(14)
where Vblood and Vint denote the volume occupied by blood and interstitial
ﬂuid, respectively; extending previous notations, Vcyt and Ver denote total
volumes of cytosol and ER of the tissue cells. The total activity AT = Vtot CT
of the tracer occupying the volume of interest is related to the state variables
and the input function by the equation
Vtot CT = Vblood Ci + Vint Cf + Vcyt Cf + Vcyt Cp + Ver Cr .
(15)
Division of both sides by Vtot leads to
CT = Vblood
Vtot
Ci + Vint + Vcyt
Vtot
Cf + Vcyt
Vtot
Cp + Ver
Vtot
Cr .
(16)
We deﬁne the volume fractions of blood and interstitial ﬂuid as
Vb = Vblood
Vtot
,
Vi = Vint
Vtot
.
(17)


## Page 11


FDG kinetics in cells and tissues
11
Next application of (14) and (17) yields
Ver
Vtot
= vr (1 −Vb −Vi) ,
(18)
where
vr =
Ver
Vcyt + Ver
=
ver
vcyt + ver
(19)
is independent of the number of cells. Similarly, comparison with (14), (17),
and (18) provides
Vcyt
Vtot
= (1 −vr) (1 −Vb −Vi) .
(20)
Replacing (17), (18), and (20) into the expression (16) of CT provides the
required result
CT = Vb Ci + α Cf + β Cp + γ Cr ,
(21)
where the adimensional constants α, β and γ are deﬁned as
α = Vi + (1 −vr) (1 −Vb −Vi),
(22)
β = (1 −vr) (1 −Vb −Vi),
(23)
γ = vr (1 −Vb −Vi).
(24)
In compact form, we can write equation (21) as
CT (t) = Vb Ci(t) + α C(t; k5, Ci) ,
α =

α β γ

,
(25)
where Vb and α depend on speciﬁc tissue and cell features; they are regarded
as given in the inversion procedure.
2.3 Simpliﬁed BCM
A simpliﬁed compartmental model (SCM) for compartmental analysis is shown
in Fig. 2(b). As in the compartmental system of Fig. 2(a), tracer is ﬁrst ex-
changed between the input compartment (either incubation medium or blood)
and the compartment for free tracer, with rate coeﬃcients k∗
1 and k∗
2. Unlike
the system of Fig. 2(a), there is only one cytosolic pool for phosphorylated
FDG. The coeﬃcients k∗
3 and k∗
4, providing phosphorylation and dephospho-
rylation rates, can be regarded as the functional correspondent of k3 and k6,
respectively. The model of Fig. 2(a) is known conventionally as the Sokoloﬀ
model, ﬁrst introduced in Sokoloﬀet al. (1977). In view of further comparison,
a few details of the SCM formulation are now outlined.
Following the conventions already introduced, the system of ODEs for the
two state variables C∗
f and C∗
p takes the form
( ˙C∗
f = −(k∗
2 + k∗
3) C∗
f + k∗
1 Ci,
˙C∗
p = k∗
3 C∗
f −k4 C∗
p,
,
(26)


## Page 12


12
Mara Scussolini et al.
with initial conditions C∗
f(0) = C∗
p(0) = 0, and given input function Ci. We
denote by k∗
4 = (k∗
1, k∗
2, k∗
3, k∗
4) the vector of parameters of the simpliﬁed formu-
lation. Notice that a star is used systematically to refer to quantities pertaining
to the simpliﬁed model.
In the modeling of a cell culture, the state variable Ci describes concentra-
tion of tracer in the incubation medium, while C∗
f and C∗
p describe intracellular
concentration of free and phosphorylated tracer. We do not go into the details
of the compact formulation in terms of activities, which is obtained straight-
forwardly. We only observe that the connection between the datum and the
state variables takes the simpliﬁed form
AT = A∗
f + A∗
p = α A∗,
(27)
where
A∗=
A∗
f
A∗
p

,
α =
1 1
.
(28)
Here, A∗= A∗(t; ¯k
∗
4, Ai), where ¯k
∗
4 = (¯k∗
1, k∗
2, k∗
3, k∗
4) includes the modiﬁed
parameter ¯k1 deﬁned in (9).
In the analysis of a tissue model, Ci corresponds to tracer concentration in
blood. The state variable C∗
f is interpreted as the concentration of free tracer in
interstitial tissue and tissue cells, while C∗
p is the concentration of phosphory-
lated tracer inside tissue cells. It is assumed that extracellular phosphorylated
tracer can be disregarded. In this simpliﬁed framework, the equation connect-
ing data to state variables is
CT = Vb Ci + (1 −Vb) C∗
f + (1 −Vb −Vi) C∗
p = Vb Ci + α C∗,
(29)
where
C∗=
C∗
f
C∗
p

,
α =
1 −Vb, 1 −Vb −Vi

.
(30)
Here, C∗= C∗(t; k∗
4, Ci), where k∗
4 = (k∗
1, k∗
2, k∗
3, k∗
4).
The SCM can be derived from the BCM simply by omitting consideration
of the role of the ER, i.e., by formal substitution of the condition Ver = 0. If
in addition we assume that Vi = 0, then equation (29) reduces to
CT = Vb Ci + (1 −Vb) (C∗
f + C∗
p) ,
(31)
which is the standard equation often used in tissue kinetics.
In this work the SCM is considered explicitly for the ease of comparison.
Speciﬁcally, we will apply the BCM and the SCM to the analysis of the same
data in order to discuss similarities and diﬀerences between the results.


## Page 13


FDG kinetics in cells and tissues
13
2.4 A general relation between rate constants of BCM and SCM
This subsection is devoted to the determination of a general relation between
the rate constants of the BCM and the corresponding SCM, which holds if the
two models are consistent with the same data. Under suitable assumptions,
this relation is further reduced to a remarkable diﬀerence in the rates of phos-
phorylation k3 and k∗
3, which is to be regarded as a direct consequence of the
modeling assumptions.
With the aim of performing a qualitative analysis on the two models BCM
and SCM, the following considerations are made. It is well known that the
dephosphorylation rate is rather small (Sokoloﬀet al., 1977); therefore, we
assume that k6 and k∗
4 are small with respect to the other coeﬃcients, so that
their contribution can be neglected. Next, we suppose that the concentrations
Ci, Cf, Cp, and C∗
f are almost constant at large time values. The systems of
ODEs (4) and (26) reduce to the algebraic conditions
(k2 + k3) ˜Cf = k1 ˜Ci
k3 ˜Cf = k5 ˜Cp
˙Cr = k5 ˜Cp
and
(k∗
2 + k∗
3) ˜C∗
f = k∗
1 ˜Ci
˙C∗
p = k∗
3 ˜C∗
f
where the superposed tilde refers to the constant values of the concentrations
and ˜Ci is the common forcing contribution, independent of the model. The
constant rates of growth of phosphorylated FDG are given by
˙Cr =
k1 k3
k2 + k3
˜Ci ,
(32)
˙C∗
p =
k∗
1 k∗
3
k∗
2 + k∗
3
˜Ci .
(33)
Consider the case of cell cultures. Comparison of eqs (12) and (27) for the
total activity shows that
AT = Af + Ap + Ar = A∗
f + A∗
p .
In view of the assumptions, evaluation of the time derivative of the last equa-
tion leads to ˙Ar = ˙A∗
p, which is written in the equivalent form
Ver ˙Cr = Vcyt ˙C∗
p ,
(34)
after comparison with (7). Substitution into (34) of (32), (33), and the deﬁni-
tion (9) of ¯k1, shows that
¯k∗
1 k∗
3
k∗
2 + k∗
3
= v
¯k1 k3
k2 + k3
,
(35)


## Page 14


14
Mara Scussolini et al.
where we recall that v = Ver/Vcyt. Equation (35) may be used as a check on
the eﬀectiveness of the numerical reconstructions.
If ¯k∗
1 ≈¯k1, k∗
2 ≈k2, k∗
3 ≪k∗
2, and k3 ≪k2, as it is shown to be the case
in subsequent developments, then equation (35) simpliﬁes to k∗
3 ≈v k3. This
shows that the factor v connects the reconstructed phosphorylation rates of
SCM and BCM.
Similar considerations hold for the case of tissues. Comparison of the ex-
pressions (21) and (29) of the total concentration for the BCM and SCM shows
that
α Cf + β Cp + γ Cr = (1 −Vb) C∗
f + (1 −Vb −Vi) C∗
p .
In view of the original assumptions and the deﬁnition of γ, evaluation of the
time derivative yields
vr ˙Cr = ˙C∗
p .
(36)
Substitution into (36) of the expressions (32) and (33) leads to equation
k∗
1 k∗
3
k∗
2 + k∗
3
= vr
k1 k3
k2 + k3
,
(37)
which is similar to (35), with vr replacing v.
2.5 Compartmental inverse problem
The compartmental inverse problem consists in ﬁnding the rate coeﬃcients
of the model, starting from the available data. In this subsection we discuss
the two main issues related to the inverse problem: the identiﬁability of the
model, assessing whether the parameters are uniquely determined by the given
data, and the numerical method applied in order to reduce the compartmental
model and return the numerical values of the kinetic parameters.
2.5.1 Identiﬁability issues
Before proceeding to numerical evaluation of the rate coeﬃcients, we discuss
the formal identiﬁability of the model, namely, whether the rate coeﬃcients
are uniquely determined by the given input data, under the assumption that
they are not contaminated by noise (Miao et al., 2011; Yates, 2006). The
proof of uniqueness may be regarded as an a priori test on the compartmental
model, assuring that it is eﬀective in providing a unique description of tracer
kinetics, independently of the numerical values of the data. We show that the
BCM is identiﬁable for both the tissue and cell culture systems, under general
conditions. Identiﬁability of the tissue model, the more complicated system,
is considered ﬁrst; then the cell culture model is examined. Notice that, it is
already well known that the SCM is identiﬁable, and we refer to Delbary et
al. (2016) for the proof.


## Page 15


FDG kinetics in cells and tissues
15
The discussion of identiﬁability of BCM tissue model is based on the sys-
tem of ODEs (4) and equation (21), with CT and Ci given. Identiﬁability
corresponds to uniqueness of the vector k5. Following the procedure used in
Delbary et al. (2016), we consider the Laplace transform of the system (4)
and equation (21), in order to reduce the identiﬁability issue to the proof of
uniqueness of the solution of an algebraic system.
We denote by ˜f(s) the Laplace transform of a function f(t). Assuming that
suitable regularity conditions are satisﬁed, we obtain the linear system





(s + k2 + k3) ˜Cf −k6 ˜Cr = k1 ˜Ci
−k3 ˜Cf + (s + k5) ˜Cp = 0
−k5 ˜Cp + (s + k6) ˜Cr = 0
(38)
for the transform of the system (4), and equation
˜CT −Vb ˜Ci = α ˜Cf + β ˜Cp + γ ˜Cr
(39)
from the transform of (21).
The solution of the linear system (38) is
˜Cf =
k1
D(s) (s + k5) (s + k6) ˜Ci
(40)
˜Cp =
k1
D(s) k3 (s + k6) ˜Ci
(41)
˜Cr =
k1
D(s) k3 k5 ˜Ci
(42)
where
D(s) = s3+(k2+k3+k5+k6) s2+[(k2+k3) (k5+k6)+k5 k6] s+k2 k5 k6 . (43)
Substitution of the expressions (40), (41), and (42) of ˜Cf, ˜Cp, and ˜Cr into
equation (39) yields the necessary condition
˜CT −Vb ˜Ci
˜Ci
= k1 Q(s)
D(s)
,
(44)
where
Q(s) = α s2 + [α (k5 + k6) + β k3] s + α k5 k6 + β k3 k6 + γ k3 k5 .
(45)
If h5 = (h1, h2, h3, h5, h6) is another vector of rate coeﬃcients consistent
with the data, we have to prove that h5 = k5. Compatibility with data implies
equality between the right-hand sides of (44), expressed in terms of h5 and in
terms of k5. With obvious meaning of symbols, we have
h1 Qh5(s)
Dh5(s)
= k1 Qk5(s)
Dk5(s)
.
(46)


## Page 16


16
Mara Scussolini et al.
Assume that the polynomials Q and D are coprime, i.e. they do not have
common roots. Since the leading coeﬃcients of Qh5 and Qk5 are identical, as
well as those of Dh5 and Dk5, equation (46) holds if and only if h1 = k1,
Dh5 = Dk5, and Qh5 = Qk5. The last two equations give rise to the system
h2 + h3 + h5 + h6 = k2 + k3 + k5 + k6
(47)
(h2 + h3) (h5 + h6) + h5 h6 = (k2 + k3) (k5 + k6) + k5 k6
(48)
h2 h5 h6 = k2 k5 k6
(49)
β h3 + α (h5 + h6) = β k3 + α (k5 + k6)
(50)
α h5 h6 + β h3 h6 + γ h3 h5 = α k5 k6 + β k3 k6 + γ k3 k5
(51)
of ﬁve equations for the four unknowns h2, h3, h5, h6.
The analysis of the system (47)–(51) proceeds in three steps. First, eqs
(47), (49), (50) are solved for h3, h5 and h6 in terms of h2. Next equation (48)
is solved for h2 in terms of k5, α, β. Finally, (51) is used to discard spurious
solutions.
In the ﬁrst step, h5 + h6 and h3 are determined from the linear system
(47), (50) as
h5 + h6 =
β
α −β (h2 −k2) + k5 + k6
(52)
h3 = −
α
α −β (h2 −k2) + k3 .
(53)
It follows from (49) that
h5 h6 = k2
h2
k5 k6 .
(54)
The system (52), (54) can be solved for the unknowns h5 and h6. The resulting
pair of solutions may be expressed as
(h5, h6) = (x1, x2) ,
(h5, h6) = (x2, x1) ,
(55)
where
x1,2 = 1
2

β
α −β (h2 −k2) + k5 + k6 ±
√
∆

,
with
∆=

β
α −β (h2 −k2) + k5 + k6
2 −4 k2
h2
k5 k6 .
In the second step, substitution of equations (52)–(54) into (48) provides
a third order polynomial equation for h2. After long and tedious calculations,
it is written in the form
(h2 −k2)
h
β2
(α −β)2 h2
2 −
β
α −β B h2 + k5 k6
i
= 0 ,
(56)
where
B = k3 −k5 −k6 +
α
α −β k2 .


## Page 17


FDG kinetics in cells and tissues
17
We obtain the three solutions
h(1)
2
= k2
h(2)
2
= α −β
2 β
(B+
p
∆B) ,
h(3)
2
= α −β
2 β
(B−
p
∆B) , (57)
with
∆B = B2 −4k5 k6 .
In principle, each solution h(i)
2 , (i = 1, 2, 3) generates two vectors h5, through
substitution into (53) and (55).
In the third step, we discuss admissibility of the solutions. In general a
parameter vector h5 can be accepted only if its components are strictly posi-
tive. Whenever this condition is not satisﬁed, the related solution is discarded,
and we shall not mention this any more. Moreover, any admissible parameter
vector h5 must satisfy equation (51).
Consider the case h2 = h(1)
2
= k2. The associated vector parameters h(1a)
5
and h(1b)
5
are given by
h(1a)
5
= (k1, k2, k3, k5, k6) ,
h(1b)
5
= (k1, k2, k3, k6, k5) .
(58)
The vector h(1a)
5
satisﬁes equation (51), but h(1b)
5
does not, unless k5 = k6.
We conclude that h(1a)
5
is admissible, while h(1b)
5
is not, if k5 ̸= k6. Similarly,
consider the (positive) components of any vector h(2a),(2b)
5
, h(3a),(3b)
5
generated
by either h(2)
2
or h(3)
2 ; they are expressed in terms of (k2, k3, k5, k6), α, and β.
We say that k5 is generic if the corresponding vectors h(1b)
5
, h(2a),(2b)
5
, h(3a),(3b)
5
do not satisfy equation (51), that is, if they are not admissible. Then we can
state the following result.
Theorem 1 Assume that the polynomials
Q(s) = α s2 + [α (k5 + k6) + β k3] s + α k5 k6 + β k3 k6 + γ k3 k5
and
D(s) = s3 + (k2 + k3 + k5 + k6) s2 + [(k2 + k3) (k5 + k6) + k5 k6] s + k2 k5 k6
are coprime. If k5 is generic, the rate coeﬃcients k5 = (k1, k2, k3, k5, k6) are
uniquely determined by Ci and CT , and the compartmental model of equations
(4) and (21) is identiﬁable.
The proof of identiﬁability for the BCM dedicated to the kinetics of the
cell culture model follows the same lines as the proof of Theorem 1. Therefore,
we show here only the main steps. Application of the Laplace transform to
equations (8) and (12) for the activities, leads to
˜
AT
˜Ai
=
¯k1 Q(s)
D(s)
,
(59)
where
Q(s) = s2 + (k3 + k5 + k6) s + (k3 + k5) k6 + v k3 k5 ,
(60)


## Page 18


18
Mara Scussolini et al.
and
D(s) = s3+(k2+k3+k5+k6) s2+[(k2+k3) (k5+k6)+k5 k6] s+k2 k5 k6 . (61)
Assume that Q and D are coprime. If ¯h5 = (¯h1, h2, h3, h5, h6) is another vector
of rate coeﬃcients consistent with the cell culture data, it follows that ¯h1 = ¯k1,
while the remaining components of ¯h5 and ¯k5 satisfy the following system of
equations:
h2 + h3 + h5 + h6 = k2 + k3 + k5 + k6
(62)
(h2 + h3) (h5 + h6) + h5 h6 = (k2 + k3) (k5 + k6) + k5 k6
(63)
h2 h5 h6 = k2 k5 k6
(64)
h3 + h5 + h6 = k3 + k5 + k6
(65)
(h3 + h5) h6 + v h3 h5 = (k3 + k5) k6 + v k3 k5 .
(66)
Comparison between (62) and (65) shows that h2 = k2. As a consequence,
(64) reduces to h5 h6 = k5 k6.
Next h5 + h6 is determined from (65) in terms of h3, and substituted into
equation (63), which takes the form of a vanishing polynomial of degree 2, in
the unknown h3. The corresponding solutions are:
h(1)
3
= k3 ,
h(2)
3
= −k2 + k5 + k6 .
If h(1)
3
= k3, it is easily shown that h(1)
5
= k5 and h(1)
6
= k6, which implies
¯h
(1)
5
= ¯k5.
If h(2)
3
≤0 this solution is not admissible. If h(2)
3
> 0 then equations (65)
and (66) reduce to a linear system for the unknowns h(2)
5
and h(2)
6 . The solution
is
h(2)
5
=
1
1 −v
 k2 −k3
k6 + v k5
−k2 + k5 + k6

,
h(2)
6
= k2 −h(2)
5
.
If at least one between h(2)
5
and h(2)
6
is negative or vanishing, then h(2)
3
gives
rise to a vector solution which not admissible. If h(2)
5
and h(2)
6
are positive then
the compatibility condition
h(2)
5
(k2 −h(2)
5 ) = k5 k6
(67)
must be satisﬁed. Thus we conclude that the solution reconstructed from h(2)
3
is not admissible, unless the data satisfy equation (67).
Following the previous procedure, we say that the parameter vector ¯k5 is
generic if it does not satisfy equation (67), and we state the following result.
Theorem 2 Assume that the polynomials
Q(s) = s2 + (k3 + k5 + k6) s + (k3 + k5) k6 + v k3 k5
and
D(s) = s3 + (k2 + k3 + k5 + k6) s2 + [(k2 + k3) (k5 + k6) + k5 k6] s + k2 k5 k6
are coprime. If ¯k5 is generic, the rate coeﬃcients ¯k5 = (¯k1, k2, k3, k5, k6) are
uniquely determined by Ai and AT , and the compartmental model of equations
(8) and (12) is identiﬁable.


## Page 19


FDG kinetics in cells and tissues
19
2.5.2 Estimation of rate constants
The solution of the compartmental inverse problem for the unknown rate con-
stants requires an optimization-regularization method. Here we describe our
approach, based on a Newton-type method, in general terms. For details, see
Bauer et al. (2009), Delbary and Garbarino (2016), and Vogel (2002). This for-
mulation has already been applied successfully in the compartmental frame-
work, e.g. to reduce non-standard compartmental models representing com-
plicated physiologies such as the liver (Garbarino et al., 2015), to solve the
compartmental inverse problem pixelwise in the so-called indirect parametric
imaging context (Scussolini et al., 2017), and to address the reference tissue
problem of recovering the parameters when the IF is not available (Scussolini
et al., 2018). In these applications the Newton-type method resulted to be
rather eﬃcient in the reconstruction of the compartmental kinetic parame-
ters, providing reliable and stable estimates, and performed better than the
usual Levenberg-Marquardt method (see Tables 1–3 in Delbary and Garbarino
(2016), Table III in Scussolini et al. (2018)).
The underlying ideas of our approach may be described as follows. We
rewrite the equation connecting the given data and the compartmental model
as a zero ﬁnding problem. This means that, for the cell culture, we redeﬁne
equation (13) as
α A(t; ¯k5, Ai) −AT (t) := Ft(¯k5) = 0 ;
(68)
similarly, equation (25) for the tissue becomes
Vb Ci + α C(t; k5, Ci) −CT (t) := Ft(k5) = 0 .
(69)
The vector α is chosen according to the data model. The input functions Ai
and Ci are regarded as given. The total activity of the cell culture AT and the
total concentration of the target tissue CT depend on the unknown vector of
parameters ¯k5 and k5, respectively. Notice that equations (68) and (69) are
general enough to hold for both the BCM and SCM, provided that A and C
are substituted with the starred variables A∗and C∗, as in equations (27) and
(29), and the unknown vector of parameters to be considered are ¯k
∗
4 and k∗
4.
In general, the operator Ft : Rp
+ →C1(R+, R), where p indicates the num-
ber of the model coeﬃcients, is a non-linear analytic operator parameterized
by the time variable t ∈R+. The Gauss-Newton method transforms the non-
linear optimization problem of equation (68), or equation (69), into a linear
problem by computing the Fr`echet derivative of the operator Ft with respect
to the kinetic parameters. What is found is a linear equation
dFt
dk (k(0); h(0))

(t) = −Ft(k(0)) ,
(70)
with the bounded and linear diﬀerential operator dFt/dk, unknown step-size
h(0) ∈Rp, initial guess k(0) ∈Rp
+, and for t ∈R+. In real applications,
only noisy versions of the data for a ﬁnite number of sampling time points


## Page 20


20
Mara Scussolini et al.
t1, . . . , tn ∈R+ are available. Therefore, equation (70) becomes the discretized
linear system
F 0 h(0) = Y 0 ,
(71)
where F 0 is the matrix encoding the Fre`chet derivatives with respect to k(0),
and Y 0 is the vector discretizing −Ft computed in k(0). The system (71)
constitutes a classic linear ill-posed inverse problem, since the solution may
not exist, may not be unique, and may not be stable. In order to ﬁnd a unique
stable solution of (71), we consider a Tikhonov-type regularization, with the
Tikhonov penalty on the step-size vector, which leads to the regularized system
(F T
0 F 0 + λ0 I[p]) h(0) = F T
0 Y 0 ,
(72)
where I[p] is the identity matrix of dimension p, and λ0 is the regularization
parameter which is allowed to change at every iteration. The regularization
parameter may be ﬁxed a priori, or selected with a proper method, e.g. the
Generalized Cross Validation (GCV) method (Golub et al., 1979). The op-
timization algorithm performs an iterative scheme which: 1) starts from a
random initial guess k(0), 2) determines the step-size h(0) as the least-square
solution of (72), 3) updates the values of the kinetic parameters by letting
k(1) = k(0) + h(0) and 4) iterates the process. To stop the iterative algorithm,
we check the relative error between the given experimental datum and the
model-predicted one, using a threshold coinciding with the uncertainty on the
measurement as a stopping criterion.
3 Applications to cancer cell cultures in vitro
In this section we determine the rate coeﬃcients describing FDG kinetics of
cultures of 4T1 cancer cells (breast cancer cell lines), and the correspond-
ing compartment activities. The data have been obtained by the use of a
LigandTracer (LT) device of Ridgeview Instruments (Bj¨orke and Andersson,
2006a,b; Mertens et al., 2012). Details on experimental procedures and calibra-
tion methods applied in order to follow tracer uptake by cell cultures can be
found in the forthcoming paper (Scussolini et al. manuscript in preparation).
Here, we make use of new experimental data.
Application of the BCM to cell cultures is in natural relation with the
cell origin of the model. Cell cultures allow for repeated experiments under
constant conditions, whereas experiments on tracer uptake in vivo may be
inﬂuenced by absorption by other organs, speciﬁc tissue environment, blood
perfusion, and so on. Moreover, LT-measurements allow a direct estimate of
FDG consumption, and thus of glucose consumption, without any distortion
introduced by physical corrections or signal reconstruction algorithm, which
are essential steps to be made in, e.g., PET experiments in vivo. For this
reasons, the data coming from LT-cells experiments are highly stable and
reliable with respect to cell biology, and the results give a fair interpretation
of the phenomenon observed.


## Page 21


FDG kinetics in cells and tissues
21
Comparison with the results obtained from the analysis of cancer tissues,
described in the next section, provides a deep understanding of the feasibility
and eﬀectiveness of the compartmental model. Contrast with results available
in the literature is obtained through application of the SCM to data reduction.
3.1 Data
(a) LT device.
0
20
40
60
80
100
120
140
160
180
time [min]
0
1
2
3
4
5
6
7
8
activity [Bq]
×104
(b) AT .
0
20
40
60
80
100
120
140
160
180
time [min]
5.38
5.39
5.4
5.41
5.42
5.43
5.44
5.45
5.46
5.47
5.48
activity [Bq]
×106
(c) Ai.
Fig. 3 (a) Measurement principle of the LT device: the petri dish containing attached target
cells is placed on an inclined and rotating support; the incubation medium with the FDG
radioactive tracer occupies the lower part of the dish due to the dish inclination; the detector
points towards the upper part of the dish and the uptake of FDG by cells is measured once
per rotation in the upper position. (b) The time-dependent activity curve of FDG uptake
AT and its standard deviation, related to experiment e1. (c) The time-dependent activity
curve of the incubation medium Ai and its standard deviation, related to experiment e1
Cultured 4T1 cancer cells have been seeded and then attached over a spe-
ciﬁc portion of the surface of a petri dish held by the LT device (see Fig. 3(a)).


## Page 22


22
Mara Scussolini et al.
Table 1 Experimental values of the number of cells Nc, the initial FDG activity in the
medium Ai0 (Bq), the ﬁnal total activity of cells AT (180) (Bq), and the growth rate of AT
as the slope (Bq/min) of the line approximating the curve, for each LT experiment. Notice
that [M] refers to multiplication by 106
Nc [M]
Ai0 [M]
AT (180)
growth rate
e1
0.96
5.46
7.72 · 104
348
e2
0.40
5.26
7.85 · 104
434
e3
0.40
5.46
6.61 · 104
305
e4
0.80
6.39
1.01 · 105
545
e5
0.80
8.37
9.16 · 104
412
e6
0.60
4.74
2.26 · 104
82
The bottom of the dish has been ﬁlled with a radioactive incubation medium
containing both glucose at physiological concentration 1 g/L, i.e. 5.5mM, and
an amount of FDG corresponding to about 106 Bq, diluted in a volume of 3
mL. Notice that the amount of FDG can be considered negligible with respect
to that of glucose, i.e., FDG has to be regarded as a perturbation of glucose.
The dish has been subject to a periodic motion around its axis, inclined from
the vertical; at each rotation cycle, lasting one minute, the LT device has col-
lected the radioactivity emitted by the cells. Experiments have been performed
for a total time interval of 180 minutes.
In the course of a typical experiment, radioactive FDG molecules, initially
added to the incubation medium, have been uptaken and then retained by the
cell culture. For each experiment we have considered the time dependent total
activity (Bq) of the cell culture AT , and the corresponding input function Ai,
describing the activity inside the incubation medium. Both activity curves have
been decay corrected. Since the LT is a closed system for radioactive molecules,
the two curves satisfy the conservation law Ai + AT = Ai0, where the known
constant Ai0 represents the activity in the medium available at the beginning
of the measuring procedure, after absorption by wet surfaces, which occurs in
a very short time interval. The total activity AT has been reconstructed on the
basis of the counts of the detector available with the LT. The input function
has been determined by the conservation law as Ai = Ai0 −AT .
Following Milo and Phillips (2015), we have chosen the value of the intra-
cellular relative size of the ER with respect to the cytosol as v = 0.17, which
holds for a rough ER in a liver hepatocyte cell.
We have considered six LT experiments, denoted as ei, with i = 1, . . . , 6,
diﬀering between each other for number of cells Nc and initial amount of FDG
in the medium Ai0. Table 1 reports the experimental values of the number of
cells Nc, the initial amount of FDG in the medium Ai0, the end-time total
activity of the cell culture AT , and the slope (Bq/min) of the line approxi-
mating AT (by means of linear regression, with a coeﬃcient of determination
r2 oscillating between 0.97 and 0.99), as an estimate of the growth rate of the
activity of cells.


## Page 23


FDG kinetics in cells and tissues
23
Table 2 Reconstructed kinetic parameters (1/min) by the use of the BCM for the 4T1 cell
culture of the LT experimental group of six experiments, as mean and standard deviation
over 50 runs of the Gauss-Newton algorithm. The last two lines report mean and standard
deviation of each kinetic parameter computed over the mean estimates of the six experiments
¯k1
k2
k3
k5
k6
e1
0.0083 ± 0.0007
2.8722 ± 0.2710
0.1340 ± 0.0021
2.0803 ± 0.3009
0.0000 ± 0.0000
e2
0.0073 ± 0.0012
4.0378 ± 0.7763
0.3396 ± 0.0022
0.7936 ± 0.0099
0.0021 ± 0.0000
e3
0.0050 ± 0.0006
2.4056 ± 0.3527
0.1939 ± 0.0030
2.2454 ± 0.6789
0.0014 ± 0.0000
e4
0.0152 ± 0.0018
6.3428 ± 0.8059
0.2497 ± 0.0434
3.7148 ± 0.8222
0.0354 ± 0.1702
e5
0.0153 ± 0.0012
7.1280 ± 0.5583
0.1510 ± 0.0002
4.5027 ± 0.1900
0.0009 ± 0.0000
e6
0.0067 ± 0.0001
5.1039 ± 0.1030
0.0948 ± 0.0002
2.7223 ± 0.2495
0.0020 ± 0.0000
mean
0.0096
4.6484
0.1938
2.6765
0.0070
std
0.0045
1.8860
0.0890
1.3040
0.0140
As typical example of time-dependent activity curve of FDG uptake by the
cell culture, Fig. 3(b) shows the datum AT of experiment e1. In general, the
graph of AT exhibits a certain degree of variability among the experiments
because of the the diﬀerent experimental setup. Nevertheless, the qualitative
behavior of the uptake curves is relatively well deﬁned: at each experiment
AT grows almost linearly, with small random oscillations that should be due
to experimental errors. A similar behavior had already been observed both in
vitro and in vivo (see, e.g., Mertens et al. (2012) and references cited therein).
An example of input function can be seen in Fig. 3(c) (experiment e1).
The graph of Ai is almost constant, in that the relative loss of tracer from the
medium with respect to the initial amount, in the total time-interval of 180
min, is about 1%; in other terms, the cell culture uptake of tracer from the
incubation medium is small with respect to the total amount of tracer in the
medium.
3.2 Results
We have analyzed 4T1 cell culture data with both the BCM and SCM. The
results are reported in Table 2 for the BCM reduction, and in Table 3 for
the SCM reduction. Means and standard deviations have been computed over
50 runs of the iterative algorithm, with diﬀerent initialization of the kinetic
parameters, randomly chosen in the interval (0, 1) with uniform distribution.
The regularized Gauss-Newton algorithm is rather robust with respect to the
choice of the regularization parameter, as showed in Delbary and Garbarino
(2016); in this application the regularization parameter has been ﬁxed for each
iteration at the value of 106. The iterative algorithm was stopped when the
relative error between the experimental activity and the model-predicted one,
computed with the L2 norm, was lower than a threshold of the order of 10−2.
The following comments to the results of Table 2 and Table 3 are in order.
– At each experiment, the reconstructed values of ¯k1 and ¯k∗
1 show only slight
numeric diﬀerences and are very small (order of magniture 10−2). We recall


## Page 24


24
Mara Scussolini et al.
Table 3 Reconstructed kinetic parameters (1/min) by the use of the SCM for the 4T1 cell
culture of the LT experimental group of six experiments, as mean and standard deviation
over 50 runs of the Gauss-Newton algorithm. The last two lines report mean and standard
deviation of each kinetic parameter computed over the mean estimates of the six experiments
¯k∗
1
k∗
2
k∗
3
k∗
4
e1
0.0078 ± 0.0011
2.6919 ± 0.3771
0.0222 ± 0.0006
0.0000 ± 0.0000
e2
0.0041 ± 0.0017
1.7424 ± 0.7908
0.0426 ± 0.0010
0.0020 ± 0.0000
e3
0.0048 ± 0.0008
2.3039 ± 0.3913
0.0307 ± 0.0001
0.0013 ± 0.0000
e4
0.0144 ± 0.0001
5.8915 ± 0.0450
0.0417 ± 0.0000
0.0020 ± 0.0000
e5
0.0150 ± 0.0002
6.9155 ± 0.0966
0.0250 ± 0.0000
0.0010 ± 0.0000
e6
0.0068 ± 0.0000
5.1015 ± 0.0318
0.0157 ± 0.0000
0.0019 ± 0.0000
mean
0.0088
4.1078
0.0296
0.0014
std
0.0048
2.1404
0.0108
0.0008
that ¯k1 was deﬁned as ¯k1 = k1 Vcyt/Vi, with Vcyt ≪Vi, which implies that
the smallness of ¯k1 is ultimately related to the choice of activities as state
variables. Of course, the contribution ¯k1 Ai cannot be discarded from the
system (8) because it is of the order of 104. Similar remarks apply to ¯k∗
1.
– The estimated values of ¯k2 and ¯k∗
2 are almost equal and of order of unity.
– Taking into account also the activity curves, it may be shown that the over-
all contribution −k2 Af + ¯k1 Ai to the time rate ˙Af, due to FDG exchange
between incubation medium and cytosol, is strictly positive (as expected)
but rather small. This is consistent with the small decrease rate in time of
the activity Ai of the incubation medium, and the expectation that only
a small fraction of the FDG contained in the medium is consumed by the
system of cells.
– The result that ¯k1 ≈¯k∗
1 and k2 ≈k∗
2 shows that the two rate constants
cannot be used to discriminate between the two models BCM and SCM.
This also implies that the reconstructed tracer exchange between cells and
incubation medium is independent of the model applied.
– The estimated values of k6 result of the order of 10−3 and are almost
coincident with those of the corresponding parameter k∗
4 of the SCM. They
can be set equal to 0, as it is often done, following Sokoloﬀet al. (1977).
– The estimated values of k3 are greater than those of k∗
3, implying a diﬀerent
value for the phosphorylation rate predicted by the competing models. We
also observe that the assumptions made in subsection 2.4 may be consid-
ered as satisﬁed by the reconstructed parameters and related compartment
activities; indeed, the reconstructed values satisfy the relation k∗
3 ≈vk3,
with v = 0.17, which is a particular case of (35). From a diﬀerent viewpoint,
this shows the reliability of the inversion procedure.
Fig. 4(a) shows the reconstructed time-activity curves of the BCM com-
partments for the experiment e1, as representative of all experiments con-
ducted. It is immediately evident that the FDG is accumulated in the ER
compartment; in fact, the ER activity Ar increases in time almost linearly
and reaches the maximum value at the end-time point. The free tracer ac-


## Page 25


FDG kinetics in cells and tissues
25
tivity Af is almost constant, with stationary value reached in the ﬁrst few
minutes of the experiment. The cytosolic phosphorylated tracer Ap is approx-
imately constant, and it is almost one order of magnitude smaller than Af,
showing that a small (constant) amount of phosphorylated FDG occupies the
cytosol, where the amount of free tracer prevails over that of phosphorylated;
by the way, this also indicates a high eﬃciency of the process of transfer of
tracer molecules to ER. For comparison, in Fig. 4(b) the time-activity curves
of the reconstructed SCM compartments for experiment e1 are shown. Again,
the compartment A∗
f for free tracer becomes asymptotically stable in the ﬁrst
minutes, while the compartment A∗
p for phosphorylated tracer contains the
greater amount of radioactive molecules and represents the pool where the
FDG is accumulated.
0
20
40
60
80
100
120
140
160
180
time [min]
0
1
2
3
4
5
6
7
activity [Bq]
×104
Af
Ap
Ar
(a) BCM.
0
20
40
60
80
100
120
140
160
180
time [min]
0
1
2
3
4
5
6
7
activity [Bq]
×104
A∗
f
A∗
p
(b) SCM.
Fig. 4 Model-predicted time curves of the compartment activities for the experiment e1:
(a) Af, Ap and Ar of the BCM; (b) A∗
f, and A∗
p of the SCM
4 Applications to cancer tissues in vivo
In this section, the BCM and the SCM approaches are applied to the reduction
of the same cancer tissue data, in order to give evidence to diﬀerences in
the reconstructed kinetics. In the ﬁrst step, we compare results obtained by
the action of the two alternative compartmental models on the same set of
synthetic data. In the second step, we consider application of the two models
to real FDG–PET data of cancer murine models. This allows in particular
comparison with reconstructions of FDG kinetics in tumor tissue available in
the literature, which have been obtained by application of the Sokoloﬀ-type
two-compartment model.


## Page 26


26
Mara Scussolini et al.
4.1 Validation on simulation setting
In order to test the proposed BCM against the standard SCM, we have gen-
erated tissue data by a standard procedure: choice of a realistic IF, selection
of realistic ground-truth values for the rate constants, solution of the related
direct problem for BCM, reconstruction of the total concentration. Then, the
inverse problem has been solved by application of the BCM and SCM, with
the speciﬁc aim of analyzing the change in the numerical values of the recon-
structed parameters induced by change of the model applied for reduction.
Synthetic data have been produced by using 27 time frames equivalent to
the typical total acquisition time of the FDG experiments performed with the
microPET scanner “Albira” available at our lab (Carestream Health, Genova,
user manual by Bruker (2012)), and in agreement with usual time points of
the experiments (10 × 15 sec + 1 × 22 sec + 4 × 30 sec + 5 × 60 sec + 2 × 150
sec + 5×300 sec). The arterial IF has been simulated by ﬁtting with a gamma
variate function (Golish et al., 2001) a set of real measurements acquired from
a healthy mouse in a controlled experiment. With the ground-truth values of
the BCM parameters k5 = (k1, k2, k3, k5, k6), and with the synthetic IF, the
state variables have been evaluated by means of equation (6). The total tissue
concentration CT has been computed by equation (25), where the values of the
volume fractions have been ﬁxed as Vb = 0.15, Vi = 0.3, and v = 0.17 so that
vr = v/(1 + v) = 0.14.
We have created ﬁfty independent identically-distributed noisy datasets
by adding to CT white Gaussian noise with a signal-to-noise ratio of 30 dB,
producing realistic signals for the activity of radio-tracer in tissues. For each
dataset, we have solved the inverse problem of equation (69) for the unknown
vector of parameters k5, by applying the BCM, and for the unknown vector
k∗
4, by applying the SCM. In so doing we have performed a model-sensitivity
analysis, as well as we have tested the Gauss-Newton algorithm reliability for
BCM. The starting point of the iterative method has been randomly chosen in
the interval (0,1), and the regularization parameter has been optimized at each
iteration through the GCV method (Golub et al., 1979), by the requirement
of a predeﬁned range of variability (between 102 and 104). The algorithm
has been stopped when the relative error between the original noisy total
concentration and the model-predicted one, computed with the L2 norm, has
become lower than a threshold of order of 10−2. The ground-truth values and
the reconstructed values of the parameters for both the BCM and the SCM
are reported in Table 4. Means and standard deviations are computed over the
ﬁfty diﬀerent realizations. Notice that in Table 4 we do not indicate explicitly
the notation k∗for the SCM coeﬃcients, but, with a slight abuse of language,
we identify the BCM and SCM parameters with the same kinetic meaning, i.e.
k1 with k∗
1, k2 with k∗
2, k3 with k∗
3, and k6 with k∗
4.
The following comments to Table 4 are now in order.
– The procedure for the solution of the inverse problem may be considered
as suﬃciently reliable: in particular, the reduction of the BCM by means


## Page 27


FDG kinetics in cells and tissues
27
Table 4 Ground-truth and reconstructed values for the kinetic parameters (1/min) of the
BCM and of the SCM by the use of the Gauss-Newton method, as mean and standard
deviation over 50 diﬀerent runs of the algorithm. The parameters of the BCM and of the
SCM with the same kinetic meaning are identiﬁed: k1 with k∗
1, k2 with k∗
2, k3 with k∗
3, and
k6 with k∗
4
k1
k2
k3
k5
k6
ground-truth
0.4
0.2
0.7
0.5
0.03
BCM
0.40 ± 0.02
0.22 ± 0.07
0.69 ± 0.18
0.49 ± 0.14
0.03 ± 0.03
SCM
0.36 ± 0.01
0.44 ± 0.03
0.11 ± 0.05
−
0.02 ± 0.03
of the Gauss-Newton algorithm provides accurate reconstructions of the
ground-truth values with rather small standard deviations.
– Comparison of k∗
1 and k∗
4 with k1 and k6, respectively, shows that change
of the model in the reduction procedure has a negligible inﬂuence on these
reconstructed values.
– The k∗
2 value returned by the SCM overestimates the k2 ground-truth value,
while the k∗
3 value underestimates the k3 ground-truth value.
To summarize, diﬀerences in the reconstructed parameter values resulting from
application of the BCM and the SCM are mainly concerned with the pairs
(k2, k∗
2) and (k3, k∗
3); the gaps originate from the non equivalent choices of the
number of state variables in the two models, and the diﬀerent expressions of
the total concentration CT , either given by (25) or (29).
4.2 Analysis of real data in vivo
FDG–PET real data of murine models have been obtained by means of a
dedicated microPET system (Albira, Carestream Health, Genova, described
in Bruker (2012)), currently operational at our lab (IRCCS San Martino IST,
Genova). The experimental protocol for FDG–PET experiments has followed
the steps described in Massollo et al. (2013). In particular, all animals have
been studied after a fasting period of six hours, to ensure a steady state of
substrate and hormones governing glucose metabolism, and have been properly
anesthetized and positioned on the bed of the microPET system, whose two-
ring conﬁguration covers the whole animal body in a single bed position. A
dose of 3 to 4 MBq of FDG has been injected through a tail vein, soon after
the start of a dynamic list mode acquisition lasting 40 min. The acquisition
has been reconstructed using the framing rate 10 × 15 sec + 1 × 22 sec +
4 × 30 sec + 5 × 60 sec + 2 × 150 sec + 5 × 300 sec, and then PET data have
been reconstructed using a Maximum Likelihood Expectation Maximization
(MLEM) method (Shepp and Vardi, 1982). Animals have been inoculated
subcutaneously in the dorsal hip muscles with 2 · 105 murine cancer cell lines
CT26 (colon carcinoma cell lines).
To obtain the Region Of Interest (ROI) concentrations (kBq/mL), each
image dataset has been reviewed by an experienced observer who recognized


## Page 28


28
Mara Scussolini et al.
(a) ROIs.
0
10
20
30
40
time [min]
0
50
100
150
200
250
300
350
concentration [kBq/mL]
(b) CT .
0
10
20
30
40
time [min]
0
200
400
600
800
1000
1200
1400
1600
concentration [kBq/mL]
(c) Ci.
Fig. 5 (a) Last frame of the FDG–PET acquisition of the murine model m1 with ROIs
around the CT26 tumor (green color) and the aortic arc (red color). (b) The time-dependent
ROI concentration curve of the CT26 tumor CT and its standard deviation, related to
experiment m1. (c) The time-dependent concentration curve of the arterial input function
Ci and its standard deviation, related to experiment m1
two ROIs: one over the cancer lesion to compute CT , and one over the left
ventricle in order to compute the blood IF Ci. The blood volume fraction
has been set equal to Vb = 0.15, according to Montet et al. (2007) for tumor
in CT26-tumor bearing mice, and the interstitial volume fraction has been
chosen as Vi = 0.3, following Kim et al. (2004). The relative size of the ER
with respect to the cytosol has been imposed as v = 0.17, as for the cell
cultures. Therefore, the volume fraction of the ER with respect to the cell
environment has been ﬁxed as vr = 0.14.
A group of six mice, denoted as mi, with i = 1, . . . , 6, have been analyzed.
The experimental ROI concentration of the CT26 tumor CT obtained for one


## Page 29


FDG kinetics in cells and tissues
29
of the mice (speciﬁcally, the mouse m1) is shown in Fig. 5(b); the related
canonical arterial IF Ci is shown in Fig. 5(c). Tissue data have been processed
by both the BCM and SCM. Estimates of the parameters obtained for each
experiment of the group are reported in Table 5 for the BCM, and in Table 6
for the SCM. Means and standard deviations have been computed by using 50
runs of the code for the regularized algorithm, with ﬁfty diﬀerent random ini-
tialization values, and with the regularization parameter determined at each
iteration through the GCV (Golub et al., 1979) with a conﬁdence interval
ranging between 104 and 106. To stop the iterative algorithm we checked the
relative error between the experimental concentration and the reconstructed
one, computed with the L2 norm, using a threshold of order of 10−1 as a stop-
ping criterion. For ease of comparison between the reconstructions obtained
with the BCM and SCM, Fig. 6 shows the bar plot of the kinetic parameters
as means and standard deviations computed over the six mouse experiments.
To comment on the parameter values reported in Table 5, Table 6, and in
Fig. 6, we observe the following.
– Diﬀerences in the estimated values obtained for each mouse agree with the
results of simulations of subsection 4.1: (1) there is only a slight diﬀerence
between the reconstructed values of k1, k∗
1, and k6, k∗
4, respectively; (2) the
value of k∗
2 is overestimated with respect to k2; (3) k∗
3 is underestimated
with respect to k3.
– The parameters k6 and k∗
4, related to dephosphorylation, are rather small,
but they cannot be neglected since the corresponding ﬂuxes, k6Cr and
k∗
4C∗
p, are comparable with the other contributions; often k∗
4 is considered
vanishing in Sokoloﬀ-type models, as done by Røe et al. (2010), Rusten et
al. (2013), and Sokoloﬀet al. (1977).
– Within each table, each parameter is rather stable among the mice of the
group, thus showing characteristic kinetic properties of the FDG inside the
CT26 tumor tissue, independently of the speciﬁc murine experiment.
Estimates of the rate constants available in the literature refer to tissues,
and have been obtained by application of compartmental models that are
comparable with SCM and are connected to data by equations of the simpliﬁed
form (31), instead of equation (21), which has been applied in the present
reduction procedure. The values obtained for k∗
1, k∗
2, k∗
3 and k∗
4 are slightly
higher than the estimates found, e.g., in Sokoloﬀet al. (1977), referring to
cerebral metabolism of albino rats, and in Reivich et al. (1985) and Ishibashi et
al. (2016), for cerebral consumption in healthy human brains. On the contrary,
the present values are comparable with those estimated in Røe et al. (2010),
for mice with prostate carcinoma xenograft, and in Rusten et al. (2013), for
soft tissue carcinomas in human patients; in both cases the rate constant
corresponding to k∗
4 was set equal to zero.
Substitution of the values of the rate constants into the systems of ODEs
(4) and (26) allows a more complete analysis of tracer kinetics. Fig. 7 shows
the reconstructed compartment concentrations for the mouse m1 according to
BCM, panel (a), and SCM, panel (b). The curves are representative of the


## Page 30


30
Mara Scussolini et al.
Table 5 Reconstructed kinetic parameters (1/min) by the use of the BCM for the CT26 tu-
mor tissue of the FDG–PET experimental group of six mice, as mean and standard deviation
over 50 runs of the Gauss-Newton algorithm
k1
k2
k3
k5
k6
m1
0.32 ± 0.03
0.37 ± 0.15
0.45 ± 0.19
0.51 ± 0.28
0.03 ± 0.02
m2
0.47 ± 0.04
0.67 ± 0.14
0.54 ± 0.16
0.59 ± 0.26
0.03 ± 0.04
m3
0.17 ± 0.03
0.34 ± 0.17
0.58 ± 0.21
0.56 ± 0.25
0.03 ± 0.02
m4
0.25 ± 0.03
0.22 ± 0.12
0.64 ± 0.21
0.58 ± 0.23
0.08 ± 0.02
m5
0.30 ± 0.04
0.33 ± 0.19
0.85 ± 0.31
0.61 ± 0.27
0.09 ± 0.05
m6
0.31 ± 0.03
0.36 ± 0.12
0.61 ± 0.21
0.53 ± 0.27
0.09 ± 0.03
Table 6 Reconstructed kinetic parameters (1/min) by the use of the SCM for the CT26 tu-
mor tissue of the FDG–PET experimental group of six mice, as mean and standard deviation
over 50 runs of the Gauss-Newton algorithm
k∗
1
k∗
2
k∗
3
k∗
4
m1
0.32 ± 0.02
0.62 ± 0.09
0.13 ± 0.09
0.03 ± 0.04
m2
0.43 ± 0.02
0.84 ± 0.06
0.11 ± 0.01
0.03 ± 0.01
m3
0.16 ± 0.03
0.60 ± 0.19
0.14 ± 0.06
0.03 ± 0.02
m4
0.23 ± 0.02
0.57 ± 0.11
0.26 ± 0.14
0.04 ± 0.03
m5
0.28 ± 0.02
0.67 ± 0.12
0.23 ± 0.05
0.03 ± 0.01
m6
0.30 ± 0.02
0.64 ± 0.09
0.23 ± 0.05
0.05 ± 0.01
kinetics of the other mice of the group analyzed. As to comparison of results
obtained for concentrations, it is found that Cf and C∗
f are almost equal for
the two models and reach the stationary value in a rather short time. Also, for
the BCM, stationarity is achieved by Cp in a few minutes, and its stationary
value is smaller than the value of Cf. According to BCM, tracer accumulates
in ER, whose compartment concentration Cr grows with time. Similarly, the
analysis performed with the use of SCM shows that accumulation of tracer
takes place in the cytosolic phosphorylated pool C∗
p. Notice that, at each time t,
Cr(t) is almost four times C∗
p(t). This observed diﬀerence follows from the fact
that the ER compartment in BCM occupies a diﬀerent volume with respect
to the cytosolic phosphorylated compartment in SCM, speciﬁcally a smaller
volume. Indeed, the activities corresponding to Cr and C∗
p are almost equal,
as expected.
5 Comments and Conclusions
In this paper we have examined a new biochemically-driven compartmental
model (BCM) aiming at the reconstruction of FDG kinetics in cell cultures
and tissues by means of the time dependent input function and total amount
of tracer uptake, measured in activity or concentration. The BCM originates
from an eﬀort of reproducing basic features of tracer kinetics in a single cell;
in particular it emphasizes the role of the endoplasmic reticulum, where de-
phosphorylation of tracer occurs, which had not been considered in previous


## Page 31


FDG kinetics in cells and tissues
31
k1
k2
k3
k5
k6
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
[min−1]
(a) BCM.
k∗
1
k∗
2
k∗
3
k∗
4
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
[min−1]
(b) SCM.
Fig. 6 Bar plot of the reconstructed kinetic parameters: for each model parameter, the
mean value and the standard deviation are computed over the mean estimates of the six
mouse models for the (a) BCM, and (b) SCM
0
10
20
30
40
time [min]
0
200
400
600
800
1000
1200
1400
concentration [kBq/mL]
Cf
Cp
Cr
(a) BCM.
0
10
20
30
40
time [min]
0
50
100
150
200
250
300
350
400
concentration [kBq/mL]
C∗
f
C∗
p
(b) SCM.
Fig. 7 Model-predicted time curves of the compartment concentrations for the mouse m1:
(a) Cf, Cp and Cr of the BCM; (b) C∗
f , and C∗
p of the SCM
reconstructions. To this aim, an additional compartment for phosphorylated
tracer in ER has been introduced, besides the two standard compartments for
free and phosphorylated tracer in cytosol.
The new model has been adapted to the analysis of real data coming from
six experiments on cancer cell cultures in vitro, and six cancer tissues in vivo,
also to test its feasibility and eﬀectiveness. In fact, the framework of cell cul-
tures is naturally related to the cell origin of the model; the tissue framework
is related to clinical and physiological applications and allows comparison with
results available in literature. A simpliﬁed version of BCM, referred to as SCM,
has been described, which is essentially coincident with a largely used com-
partmental model, also called Sokoloﬀmodel. A second kind of test has been
performed, by contrasting the kinetics obtained from the reduction of the same


## Page 32


32
Mara Scussolini et al.
data (on cells and tissues) by application of the two alternative models, BCM
and SCM. We have found rather strong similarities in the process of FDG
uptake, and signiﬁcant diﬀerences in (1) the reconstructed values of the phos-
phorylation rate constant (k3 for BCM higher than k∗
3 for SCM) and (2) the
compartment where accumulation of radioactive tracer occurs (ER for BCM,
cytosol for SCM).
From the modeling viewpoint, the direct connection of BCM to cell biology
has been explicitly discussed. It has been found that tracer kinetics is described
in terms of ﬁve rate constants, instead of the usual four. Then, the cell-based
three-compartment BCM has been successfully extended to the analysis of
data coming from in vitro and in vivo measurements. In order to connect the
formal model compartments with the available data, additional parameters
related to, e.g., cell and tissue physiologies, have been introduced in the model;
they have been regarded as given, in order to concentrate on applicability of
BCM under natural conditions.
From a mathematical perspective, it has been shown that the BCMs for
cells and tissues are identiﬁable under rather general conditions. This means
that the rate constants are uniquely deﬁned as solutions of the inverse problem,
under the assumption that the data are free of noise. A detailed comparison
has also been made on the kinetic parameters obtained by application of BCM
and SCM to the reduction of the same data; it is shown in particular that the
two alternative set of values of the rate constants must satisfy an equation
that may be regarded as an a priori constraint. Slightly diﬀerent constraint
equations hold for cell cultures and tissues.
From the viewpoint of the data, we observe that deeply diﬀerent features
characterize the cell and tissue systems analyzed in this work. (1) The IFs of
the cell systems are almost constant, while the IFs of tissue systems show a
sharp peak at the initial time. (2) The datum of tracer assumption has been
reconstructed through highly diﬀering processes based on direct measurement
of the radiation emitted (LT) and analysis of reconstructed images (PET im-
age data). (3) Cell cultures and tissues are inserted in diﬀerent environments
(clean incubation medium vs heterogeneous background, including blood and
interstitial tissue), are constituted by diﬀerent type of cancer cells (4T1 vs
CT26), and occupy diﬀerent total volumes. However, despite all these discrep-
ancies, reconstructed kinetics have shown rather “stable” characteristics with
respect to the two diﬀerent biological systems. The similar performance of
BCM in such diﬀerent environments is thus a further strong indication of its
reliability.
From the viewpoint of the new results obtained by application of the BCM,
we point out that our conclusions come from analysis of real data. Tracer is
shown to accumulate in phosphorylated form in the ER compartment, both for
cancer cells and cancer tissues; only a relatively small amount of phosphory-
lated tracer is found outside the ER. This result follows only from an analysis
where, in principle, the two available pools for phosphorylated tracer have
been treated on the same level; in this sense, accumulation of tracer in ER is
a direct consequence of the inversion procedure and of the properties of data.


## Page 33


FDG kinetics in cells and tissues
33
We recall that the result has been conﬁrmed in the forthcoming paper (Scus-
solini et al. manuscript in preparation) by direct measurement on cells seeded
in vitro and immersed in ﬂuorescent FDG-analogue tracer NBDG. The value
of the phosphorylation rate constant k3, estimated by application of BCM
to tissue data (about 0.6 min−1), is greater than k∗
3 of the SCM (about 0.18
min−1), and agrees with results of direct measurements reconstructed from the
literature (Gao et al., 2015; Muzi et al., 2001). Moreover, k∗
3 is higher than,
or comparable to, estimates of this parameter obtained in literature by appli-
cation of Sokoloﬀ-type compartmental models (Ishibashi et al., 2016; Reivich
et al., 1985; Røe et al., 2010; Rusten et al., 2013; Sokoloﬀet al., 1977). This
shows that the phosphorylation rate has been underestimated, and that the
proposed BCM gives rise to realistic results.
As to future tissue applications, the basic scheme of BCM is rather general
and may be modiﬁed to allow for consideration of speciﬁc organs, as done for
the SCM in Garbarino et al. (2014, 2015), may be associated with reference
tissue formulations (Scussolini et al., 2018) or to pixel-wise analysis (Scussolini
et al., 2017). As to cell cultures, an immediate application of BCM is obtained
when the composition of the incubation medium is changed in order to examine
eﬀects induced on FDG (and perhaps glucose) consumption. As to cell biology,
the transport of FDG towards the ER is likely to be paralleled by similar
migration of glucose in the same direction. Together with the competition
between FDG and glucose for cell transmembrane transport and entrapment
mechanisms, the role of the ER in the glucose metabolism needs for further
investigation.
Although endowed with new realistic features, the BCM is to be regarded as
a simpliﬁcation with respect to the eﬀective biochemical path followed by FDG
inside cells. Nevertheless, the results obtained show that BCM may represent
the starting point for the development of a ﬁner and more detailed model able
to depict faithfully the FDG and glucose destiny in cancer cells.
References
Bailey DL, Townsend DW, Valk PE, Maisey MN (2005) Positron Emission
Tomography Basic Sciences. Springer, London, pp 1–12
Bauer F, Hohage T, Munk A (2009) Iteratively regularized Gauss–Newton
method for nonlinear inverse problems with random noise. SIAM J Numer
Anal 47(3):1827–1846. https://doi.org/10.1137/080721789
Bj¨orke H, Andersson K (2006) Measuring the aﬃnity of a radioligand with its
receptor using a rotating cell dish with in situ reference area. Appl Radiat
Isot 64(1):32–37. https://doi.org/10.1016/j.apradiso.2005.06.007
Bj¨orke
H,
Andersson
K
(2006)
Automated,
high-resolution
cel-
lular
retention
and
uptake.
Appl
Radiat
Isot
64(8):901–905.
https://doi.org/10.1016/j.apradiso.2006.03.002
Bruker (2012) Albira Imaging. Bruker Albira Imaging System User Manual


## Page 34


34
Mara Scussolini et al.
Cherry SR, Sorenson JA, Phelps ME (2012) Physics in Nuclear Medicine.
Elsevier, Philadelphia, pp 379–405
Delbary F, Garbarino S, Vivaldi V (2016) Compartmental analysis of dy-
namic nuclear medicine data: models and identiﬁability. Inverse Problems
32(12):125010. https://doi.org/10.1088/0266-5611/32/12/125010
Delbary F, Garbarino S (2016) Compartmental analysis of dynamic nu-
clear medicine data: regularization procedure and application to physiology.
arXiv:1608.01825
Gao F, Shi K, Li S (2015) Computational methods for molecular imaging.
Springer, New York, pp 123–137
Garbarino S, Caviglia G, Sambuceti G, Benvenuto F, Piana M (2014)
A novel description of FDG excretion in the renal system: applica-
tion to metformin-treated models. Phys Med Biol 59(10):2469–2484.
https://doi.org/10.1088/0031-9155/59/10/2469
Garbarino S, Vivaldi V, Delbary F, Caviglia G, Piana M, Marini C, Capitanio
S, Calamia I, Buschiazzo A, Sambuceti G (2015) A new compartmental
method for the analysis of liver FDG kinetics in small animals. EJNMMI
Res 5(1):107. https://doi.org/10.1186/s13550-015-0107-1
Golish SR, Hove JD, Schelbert HR, Gambhir SS (2001) A fast nonlinear
method for parametric imaging of myocardial perfusion by dynamic 13N-
ammonia PET. J Nucl Med 42(6):924–931
Golub GH, Heath M, Wahba G (1979) Generalized cross-validation as a
method for choosing a good ridge parameter. Technometrics 21(2):215–223.
https://doi.org/10.2307/1268518
Ghosh A, Shieh JJ, Pan CJ, Sun MS, Chou JY (2002) The catalytic
center of glucose-6-phosphatase. HIS176 is the nucleophile forming the
phosphohistidine-enzyme intermediate during catalysis. J Biol Chem
277(36):32837–32842. https://doi.org/10.1074/jbc.M201853200
Kim
YR,
Savellano
MD,
Savellano
DH,
Weissleder
R,
Bogdanov
A
(2004)
Measurement
of
tumor
interstitial
volume
fraction:
method
and implication for drug delivery. Magn Reson Med 52(3):485–494.
https://doi.org/10.1002/mrm.20182
Ishibashi K, Wagatsuma K, Ishiwata K, Ishii K(2016) Alteration of the re-
gional cerebral glucose metabolism in healthy subjects by glucose loading.
Hum Brain Mapp 37(8):2823–2832. https://doi.org/10.1002/hbm.23210
Massollo M, Marini C, Brignone M, Emionite L, Salani B, Riondato M, Capi-
tanio S, Fiz F, Democrito A, Amaro A, Morbelli S, Piana M, Maggi D, Cilli
M, Pfeﬀer U, Sambuceti G (2013) Metformin temporal and localized eﬀects
on gut glucose metabolism assessed using 18F-FDG PET in mice. J Nucl
Med 54(2):259–266. https://doi.org/10.2967/jnumed.112.106666
Mertens K, Mees G, Lambert B, Van de Wiele C, Goethals I (2012) In vitro 2-
deoxy-2-[18F]ﬂuoro-D-glucose uptake: practical considerations. Cancer Bio-
ther Radiopharm 27(3):183–188. https://doi.org/10.1089/cbr.2011.1125
Miao H, Xia X and Perelson AS, Wu H (2011) On identiﬁability of nonlinear
ODE models and applications in viral dynamics. SIAM Rev Soc Ind Appl
Math 53(1):3–39. https://doi.org/10.1137/090757009


## Page 35


FDG kinetics in cells and tissues
35
Milo R, Phillips R (2015) Cell Biology by the Numbers. Garland Science, New
York, pp 59–62
Montet X, Figueiredo JL, Alencar H, Ntziachristos V, Mahmood U, Weissleder
R (2007) Tomographic ﬂuorescence imaging of tumor vascular volume in
mice. Radiology 242(3):751–758. https://doi.org/10.1148/radiol.2423052065
Muzi M, Freeman SD, Burrows RC, Wiseman RW, Link JM, Krohn K A,
Graham MM, Spence AM (2001) Kinetic characterization of hexokinase
isoenzymes from glioma cells: implications for FDG imaging of human brain
tumors. Nucl Med Biol 28(2):107-116
Ollinger JM, Fessler JA (1997) Positron-Emission Tomography. IEEE Signal
Process Mag 14(1):43–55. https://doi.org/10.1109/79.560323
Reivich M, Alavi A, Wolf A, Fowler J, Russell J, Arnett C, MacGre-
gor RR, Shiue CY, Atkins H, Anand A, Dann R, Greenberg JH (1985)
Glucose metabolic rate kinetic model parameter determination in hu-
mans: the lumped constants and rate constants for [18F]Fluorodeoxyglucose
and
[11C]Deoxyglucose.
J
Cereb
Blood
Flow
Metab
5(2):179–192.
https://doi.org/10.1038/jcbfm.1985.24
Røe K, Aleksandersen TB, Kristian A, Nilsen LB, Seierstad T, Qu
H, Ree AH, Olsen DR, Malinen E (2010) Preclinical dynamic
18F-
FDG PET - tumor characterization and radiotherapy response assess-
ment by kinetic compartmental analysis. Acta Oncol 49(7):914–921.
https://doi.org/10.3109/0284186X.2010.498831
Rusten
E,
Rødal
J,
Revheim
ME,
Skretting
A,
Bruland
ØS,
Ma-
linen
E
(2013)
Quantitative
dynamic
18FDG-PET
and
tracer
ki-
netic analysis of soft tissue sarcomas. Acta Oncol 52(6):1160–1167.
https://doi.org/10.3109/0284186X.2012.728713
Shepp
L,
Vardi
Y
(1982)
Maximum
likelihood
reconstruction
for
emission
tomography.
IEEE
Trans
Med
Imaging
1(2):113–122.
https://doi.org/10.1109/TMI.1982.4307558
Schmidt KC, Turkheimer F E (2002) Kinetic modeling in positron emission
tomography. Q J Nucl Med 46(1):70–85
Scussolini M, Garbarino S, Sambuceti G, Caviglia G, Piana M (2017) A
physiology-based parametric imaging method for FDG–PET data. Inverse
Problems 33(12):125010. https://doi.org/10.1088/1361-6420/aa9544
Scussolini
M,
Garbarino
S,
Piana
M,
Sambuceti
G,
Caviglia
G
(2018)
Reference
Tissue
Models
for
FDG–PET
Data:
Identiﬁ-
ability
and
Solvability.
IEEE
Trans
Radiat
Plasma
Med
Sci.
https://doi.org/10.1109/TRPMS.2018.2801029
SokoloﬀL, Reivich M, Des Rosiers MH, Patlak CS, Pettrigrew KD, Sakurada
O, Shinihara M (1977) The [14C]deoxyglucose method for the measurement
of local cerebral glucose utilization: theory, procedure, and normal values in
the conscious and anesthetized albino rat. J Neurochem 28(5):897–916
Vogel CR (2002) Computational Methods for Inverse Problems. SIAM,
Philadelphia, pp 29–39
Yates JW (2006) Structural identiﬁability of physiologically based phar-
macokinetic
models.
J
Pharmacokinet
Pharmacodyn
33(4):421–439.


## Page 36


36
Mara Scussolini et al.
https://doi.org/10.1007/s10928-006-9011-7
Vander Heiden MG, Cantley LC, Thompson CB (2009) Understanding the
Warburg eﬀect: the metabolic requirements of cell proliferation. Science
324(5930):1029–1033. https://doi.org/10.1126/science.1160809
Watabe H, Ikoma Y, Kimura Y, Naganawa M, Shidahara M (2006) PET ki-
netic analysis - compartmental model. Ann Nucl Med 20:(9)583–588
Wernick MN, Aarsvold JN (2004) Emission Tomography: The Fundamentals
of PET and SPECT. Elsevier Academic Press, San Diego, pp 499–535

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
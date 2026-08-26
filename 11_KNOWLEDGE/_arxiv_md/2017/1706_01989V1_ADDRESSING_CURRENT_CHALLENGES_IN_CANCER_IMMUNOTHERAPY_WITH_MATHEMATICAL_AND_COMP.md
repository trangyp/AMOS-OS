---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1706.01989v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1706.01989v1_Addressing_current_challenges_in_cancer_immunotherapy_with_mathematical_and_comp

> Source: 1706.01989v1_Addressing_current_challenges_in_cancer_immunotherapy_with_mathematical_and_comp.pdf

> Pages: 15

---


## Page 1


Addressing current challenges in cancer immunotherapy with
mathematical and computational modeling
Anna Konstorum1, Anthony T. Vella2, Adam J. Adler2 and Reinhard Laubenbacher∗3
1Center for Quantitative Medicine, UConn Health, Farmington, CT
2Department of Immunology, UConn Health, Farmington, CT
1,3Jackson Laboratory for Genomic Medicine, Farmington, CT
Abstract
The goal of cancer immunotherapy is to boost a patient’s immune response to a tumor. Yet, the design of
an eﬀective immunotherapy is complicated by various factors, including a potentially immunosuppressive
tumor microenvironment, immune-modulating eﬀects of conventional treatments, and therapy-related
toxicities. These complexities can be incorporated into mathematical and computational models of can-
cer immunotherapy that can then be used to aid in rational therapy design. In this review, we survey
modeling approaches under the umbrella of the major challenges facing immunotherapy development,
which encompass tumor classiﬁcation, optimal treatment scheduling, and combination therapy design.
Although overlapping, each challenge has presented unique opportunities for modelers to make contri-
butions using analytical and numerical analysis of model outcomes, as well as optimization algorithms.
We discuss several examples of models that have grown in complexity as more biological information has
become available, showcasing how model development is a dynamic process interlinked with the rapid
advances in tumor-immune biology. We conclude the review with recommendations for modelers both
with respect to methodology and biological direction that might help keep modelers at the forefront of
cancer immunotherapy development.
1
Introduction
The involvement of the immune system in all stages
of the tumor lifecycle, including prevention, mainte-
nance, and response to therapy is now recognized as
central to understanding cancer development from
a systemic point of view. Therefore, it is not sur-
prising that one of the most rapidly developing and
exciting ﬁelds in cancer treatment is that of cancer
immunotherapy, i.e. therapy that boosts the func-
tion of the patient’s own immune system in target-
ing the cancer. The development of a knowledge-
base of tumor-immune interactions and basic and
clinical work on cancer immunotherapy has been
paralleled by the development of mathematical and
computational models that utilize this knowledge-
base to design in silico model systems upon which
immune-based and other treatments can be mod-
eled. In the best case scenario, these models can
∗Corresponding author: laubenbacher@uchc.edu
1
arXiv:1706.01989v1  [q-bio.TO]  6 Jun 2017


## Page 2


serve to guide clinicians and developers of clinical
trials towards optimizing mono- and combination
therapies and basic scientists in understanding the
underlying mechanisms of the eﬀectiveness (or, in-
eﬀectiveness) of therapy combinations. Therefore,
in a ﬁeld as rapidly developing and clinically impor-
tant as cancer immunotherapy, mathematical and
computational modeling can play a central role in
helping to guide the direction the ﬁeld takes.
In this review, we survey the mathematical
modeling work in cancer immunotherapy organized
by the ’major challenges’ that the immunotherapy
community is currently grappling with. We will also
outline strategies that modelers can use to further
enhance their contribution to addressing these chal-
lenges.
This review is organized as follows. In Section 2,
we give a brief overview of tumor immunology and
cancer immunotherapy. We also outline ‘major chal-
lenges’ that have been posed in the immunotherapy
community.
In Sections 3-5, we survey how each
challenge has been addressed by the modeling com-
munity; in Section 6, we provide recommendations
as to what techniques the community can employ
to further progress on each challenge and to address
other rising challenges, and in Section 7, we sum-
marize our ﬁndings.
2
The major challenges for can-
cer immunotherapy
A tumor can, in principle, be recognized and con-
trolled by the patient’s immune system via a coor-
dinated process that has recently been summarized
as the ‘cancer-immunity’ cycle [14]. Dying tumor
cells release proteins that contain unique tumor-
speciﬁc antigens that are either mutated or diﬀeren-
tially modiﬁed post-translationally relative to nor-
mal cells [29].
Tumors also release inﬂammatory
signals in the form of cytokines and other factors
(such as heat-shock proteins) that lead to a lo-
cal innate inﬂammatory response.
Dendritic cells
(DCs), which form a part of this response, can up-
take these antigens and, if properly activated by
other factors in the tumor microenvironment, diﬀer-
entiate to present these antigens to lymphoid cells
via their MHC class I and II molecules.
Activa-
tion of cytotoxic CD8+ T cells results in their pro-
liferation and traﬃcking to the tumor site in or-
der to kill the tumor cells, leading to the release
of more tumor-associated antigens and thus repeat-
ing the cycle. This process by which the immune
system keeps a tumor in check is deﬁned as cancer
immunosurveillance. Via a counter-process termed
immunoediting, a tumor can evolve and strengthen
various mechanisms to escape immunosurveillance
[25, 59, 49].
The goal of cancer immunotherapy is to boost
the response of the immune system to the tumor by
intervening at one or several points of the cancer-
immunity cycle.
The antigen-based activation of
dendritic cells can be achieved by administration
of a therapeutic vaccine harboring one or multi-
ple tumor-associated antigens, with or without ad-
ditional factors that prime dendritic cells for acti-
vation. Another approach has been to extract pe-
ripheral blood monocytes and stimulate them to
become DCs via presentation of antigens plus cos-
timulatory molecules ex vivo before reintroducing
them into the patient.
An FDA-approved exam-
ple of the latter is the drug Provenge (sipuleucel-T;
Valeant Pharmaceuticals), which improves median
survival time in advanced prostate cancer by ∼4%
[38].
Therapies that directly boost anti-tumor T
cell activity include adoptive T cell therapy and in-
hibition of T cell checkpoint molecules. In adoptive
cell therapy (ACT), T cells are collected from a pa-
tient, expanded ex vivo, and reintroduced into the
patient. This method has been highly successful in
melanoma, and is being explored for other cancers
[56].
Checkpoint therapy involves antagonizing T
cell inhibitory receptors (such as CTLA-4 or PD-
1). Reciprocally, there are a number of activating
costimulatory receptors on T cells (such as OX40,
4-1BB, GITR, and CD27) that can be engaged to
boost T cell clonal expansion and acquisition of tu-
moricidal eﬀector functions [46].
Major successes
2


## Page 3


using this method include the FDA-approved Yer-
voy (ipilimumab; Bristo-Myers Squibb), a mono-
clonal antibody (mAb) to CTLA-4 that is used for
patients with melanoma [66, 32]. In 2016, the FDA
approved Tecentriq (atezolizumab; Genentech), an
inhibitor of the ligand for PD-1 (PD-L1) that is ex-
pressed on tumor cells and that would otherwise
engage PD-1 on tumor-inﬁltrating T cells, for treat-
ment of locally advanced or metastatic bladder can-
cer [63]. For a more extensive discussion of cancer
immunotherapies and drugs in clinical development,
see [46, 14, 35].
There are particular challenges that present
themselves in almost all applications of cancer im-
munotherapy, and have been addressed by the
mathematical community. These major challenges
include:
1. Tumor classiﬁcation for treatment and predic-
tion of response.
2. Optimal scheduling and dosage of treatment.
3. Design
and
identiﬁcation
of
combination
treatment regimes.
In this review, we use these ‘major challenges’ as a
means by which to present how mathematical mod-
eling can help to address each challenge and thereby
help to progress the ﬁeld of immunotherapy research
and application. A summary of the tumor-immune
and immunotherapy interactions consistently ad-
dressed by the models across these challenges is
depicted in Figure 1.
Figure 1:
Summary of modeling eﬀorts in immunotherapy. Generally, models (both mathematical and computational) are
at the cell-population level and consist of tumor and immune cells (immune cells may be represented cumulatively as eﬀector
cells or more speciﬁcally by cell-types), cytokines, and other immune-activating or inhibiting factors such as VEGF or TGFβ,
with therapies (in green) targeting any of these factors. Models can assume spatial homogeneity (ordinary diﬀerential equation,
ODE models) or be spatially heterogeneous (agent-based and partial diﬀerential equation (PDE) models). For addressing tumor
classiﬁcation for treatment (Challenge 1, Section 3), analytical, numerical, and/or parameter sensitivity analysis is performed
on the models to determine which system parameters contribute most strongly to prediction of treatment response. Control
theory and evolutionary algorithms (depicted by cogwheels) are applied to modeled treatments to optimize scheduling and
dosage (Challenge 2, Section 4), and all these methods can be applied to multiple treatments, including non-immune therapy
such as chemo- and molecular therapy, to model combination treatment regimes (Challenge 3, Section 5). Abbreviations: CTL,
cytotoxic T cells; DC, dendritic cells; CD4, CD4+ T cells, M, macrophages.
3


## Page 4


3
Challenge: Tumor classiﬁca-
tion for treatment and pre-
diction of response
Tumor classiﬁcation, usually based on histopatho-
logical grading, does not serve as a strong predic-
tive tool for post-treatment outcome. More sophis-
ticated methods of tumor classiﬁcation, such as im-
mune proﬁling [30], inclusion of markers of the tu-
mor microenvironment [51], and incorporation of
high-throughput data [62], can improve the predic-
tive strength of the classiﬁcations.
Nevertheless,
due to both the increasing availability of patient
data and treatment options, it can become diﬃ-
cult to predict how a patient with a speciﬁc set of
tumor characteristics will respond to a given treat-
ment. Modeling eﬀorts in this regard have been used
to identify which patient parameters may be most
important to predicting therapy outcomes.
Since
mathematical models, unlike statistical models, are
typically mechanistic, they can be used to predict
the eﬀect of therapy or therapy combinations that
have not yet been tried in the clinic (i.e. for which
patient data is as yet unavailable). We begin with
the Panetta-Kirschner (PK) model [40], one of the
ﬁrst to layer immunotherapy into a tumor-immune
model. The PK model consists of system of three
ordinary diﬀerential equations (ODEs) that model
the dynamics of eﬀector (E) and tumor (T) cells,
and the cytokine IL-2 (IL). For the sake of expe-
diency and since one of the parameters is especially
important in the analysis of model behavior, we only
show the equation for E,
dE
dt = cT −µ2E + p1EIL
g1 + IL
+ s1.
(1)
The antigenecity of the tumor is modeled by the
parameter c, µ2 represents the death rate of E, and
the proliferative eﬀect of IL-2 on E is in Michaelis-
Menton form to model saturation of response. Ther-
apies are considered by terms s1 and s2 added to the
right-hand side of dE/dt and dIL/dt, respectively.
Michaelis-Menton terms are also used to model the
negative eﬀect of E-induced tumor destruction on
T, and the positive eﬀect of tumor-resident E on IL
production. Tumor growth is modeled using the lo-
gistic growth function. The authors show that with
no therapy, if c is below a critical c0, the only stable
steady state is a large tumor. As c increases, the
tumor size oscillates between large and small, with
the time it spends in its ’large’ state (and the magni-
tude of the ’large’ state) decreasing with increasing
c. Adding therapy s1 creates a tumor-free equilib-
rium that is stable if s1 > s1
crit where s1
crit depends
on several parameters of the model. A bifurcation
diagram of s1
crit vs. c shows that there exist regions
where the tumor will either die or survive depending
on c, hence providing a mathematical basis for tu-
mor classiﬁcation for treatment. The authors show
similar results for s2 > 0 and both s1 and s2 > 0.
Models with a relatively small number of equa-
tions can be analyzed in this way and have con-
sistently shown that knowledge of system parame-
ters can help lead to tumor classiﬁcation for treat-
ment via bifurcation and stability analysis (e.g.
[50, 8, 6, 41]). Identiﬁcation of parameters where
thresholds exist with respect to system response to
therapy can aid in the identiﬁcation of eﬀective ther-
apies. For example, for the system modeled in [40],
a therapy that increases the antigenecity, c, of the
tumor can push the tumor past the critical point
necessary for response to other therapies and/or re-
duction in size to a small, stable steady state. An
excellent review of simpler tumor-immune models
and their associated analyses, which may or may not
incorporate immunotherapy, can be found in [26]. A
meta-modeling approach was taken by d’Onofrio et
al. [22] to synthesize the analytical results of such
models. These models can serve as baseline models
that can be extended to incorporate immunother-
apy.
Numerical analysis of models has also focused
on the concept of thresholds for predicting patient
response. For example, Kronik et al. [42] set out to
answer the question whether ‘mathematical model-
ing would help to deﬁne the prerequisites of an ef-
fective immunotherapy approach’. They extended a
4


## Page 5


previously published model of T cell transfer im-
munotherapy for glioblastoma [43] to a model of
ex vivo expanded tumor-speciﬁc T cell transfer for
melanoma and used clinical data to retroactively
validate it. The model consists of a system of ODEs
with 5 equations representing tumor and immune
cells, and critical signaling molecules produced by
the two cell populations (TGFβ, IFNγ, and MHC
Class I molecules). The authors varied initial tumor
size and growth rate to imitate a virtual population
of patients with heterogeneous tumor proﬁles. Four
diﬀerent T-cell therapy regimens were then simu-
lated over this population that corresponded to four
diﬀerent clinical trials. For one such trial, the model
was able to oﬀer an explanation for the lack of a
dose-response relationship with therapy: the model
showed that for patients with large enough tumors,
the therapy would have no eﬀect, whereas in smaller
tumors a dose-response relationship could be iden-
tiﬁed, again pointing to a threshold for therapy ef-
fectiveness, this time via simulation in lieu of a bi-
furcation analysis.
Indeed, the authors suggested
that volumetric tumor analysis is a better predictor
for clinical eﬀectiveness of T cell therapy than the
traditional staging method. The authors also called
for large doses of T cell therapy due to presence of
thresholds for eﬃcacy of T cell killing with respect
to T cell concentrations, although this recommenda-
tion should be considered in light of potential toxi-
cities. More broadly, parameter sensitivity analysis
has played a critical role in the numerical analysis
of models of immunotherapy (e.g., [20, 5, 37, 3]) by
helping to elucidate which tumor characteristics are
most predictive of therapy success.
To investigate how spatial organization of dif-
ferent cell types can impact tumor-immune evolu-
tion and response to therapy, Wells et al. [67] de-
veloped a hybrid discrete-continuous (HDC) agent-
based model. These models treat cells as agents that
sit on a lattice and can interact with and respond to
other cells in a stochastic manner through growth
factors and cytokines that can diﬀuse throughout
the lattice.
The cell types in this model were
naive, M1 (’tumor-suppressive’), and M2 (’tumor-
promoting’) macrophages, and live and dead tu-
mor cells.
In addition to secreted factors, oxy-
gen diﬀusion was also implemented in the model,
thereby creating oxygen-rich and hypoxic regions
in the tumor and its microenvironment.
The au-
thors used a multiparametric sensitivity analysis
(MPSA) to observe that the ratio of M2 to other
cell types (termed the Macrophage Polarization In-
dex, MPI) early in the simulation is predictive of
tumor survival. Another key predictive outcome of
the model was that increased tumor heterogeneity
is associated with tumor survival. Tumor hetero-
geneity was associated with locally elevated stim-
ulated macrophages, leading to local peaks of M2
diﬀerentiation which increased overall MPI. It fol-
lowed that a decrease in secretion of diﬀerentiation
factors for M2 cells abrogated the association be-
tween tumor heterogeneity and survival in the sim-
ulation. Therefore, the model provided a novel hy-
pothesis for tumor-induced immunosuppression via
increases in tumor-heterogeneity, but also a poten-
tial new prognostic tool for tumors where biopsies
and cell-speciﬁc stains are available. This observa-
tion was further used by the authors to hypothesize
and test in silico that introduction of genetically
engineered macrophages that could block the M2
transition would be eﬀective in killing the tumor by
blocking the feedback loop that generates localized
sites of highly concentrated immunosuppressive M2
cells, thereby constructing a novel treatment using
their observations of the most critical contributors
to tumor growth.
Lattice- and/or agent-based models (ABMs) can
provide additional information regarding spatially
explicit parameters inﬂuencing tumor-immune in-
teractions and response to immunotherapies.
In
addition to [67], this approach has been used by
Papalardo et al. [53, 52] to develop an agent-based
simulator of the Triplex vaccine, SimTriplex, which
is eﬀective in preventing mammary carcinoma in
HER-2/neu transgenic mice, and Dréau et al. [24]
to examine the interactions between a vascularized
tumor and the immune response. While partial dif-
ferential equation (PDE) models have been much
5


## Page 6


more sparsely employed to model immunotherapy,
they can be especially useful when modeling a large
number of interacting cells in a tissue, in which case
building a corresponding ABM would be too compu-
tationally costly. For example, Eikenberry et al. [27]
developed a PDE of melanoma with immune inﬁl-
trate, and showed that surgical removal of primary
tumors with high levels of immune inﬁltrate could
promote growth of satellite metastases, as was ob-
served clinically, thereby providing a model-based
hypothesis for tumor classiﬁcation with respect to
responsiveness to therapy (in this case, surgery).
4
Challenge: Optimal schedul-
ing and dosage of treatment
For any given treatment, an exhaustive experimen-
tal search for optimal dosage and/or scheduling is
unrealistic. There are several techniques which de-
velopers of mathematical models for immunother-
apy have used to identify optimal treatment sched-
ules in silico, including optimal control and genetic
algorithms.
4.1
Optimal control theory
Optimal control theory has played a prominent
role for using mathematical models of cancer im-
munotherapy for design of optimal therapy regimes.
We can consider a system of ordinary diﬀerential
equations,
(
˙x = f(x(t), u(t)) (t > 0)
x(0) = x0
(2)
where x ∈Rn and u ∈U ⊂Rm is a control parame-
ter (e.g. x(t) can represent concentrations of tumor
cells, immune cells and cytokine and u(t) can rep-
resent an immunotherapy treatment) and an initial
condition x0. The optimal u, u∗, is chosen from a
space U of admissible controls based on constraints
on x and u via calculation of an extremal of an ob-
jective functional
J(u) =
Z T
0
r(x(t), u(t))dt + g(x(T)),
(3)
where r is termed the running payoﬀand g the
terminal payoﬀ[28].
This formulation is termed
the Bolza form. The optimal u∗found using this
method then represents the best possible therapy
given conditions on the control parameters (such
as minimization of tumor cells, minimization of
therapy dosage, maximization of immune response,
etc.).
Optimal control theory has been applied exten-
sively to the Panetta-Kirschner (PK) model [40], de-
scribed in Section 3. Burden et al. [7] made ACI
therapy in the PK model into a control parameter,
u, and built an objective functional
JB(u) =
Z T
0
[x(t)−y(t)+z(t)−1
2B ·u(t)2]dt, (4)
where x(t) are activated eﬀector cells, y(t) are the
tumor cells, z(t) the local concentration of IL-2,
and B the strength of patient tolerance to treat-
ment (i.e., B is inversely correlated to side eﬀects of
treatment). For t ∈[0, T], The class of admissible
controls was set to
U = {u(t) piecewise continuous |0 ≤u(t) ≤1}
and u∗was found such that max0≤u≤1 JB(u) =
J(u∗), which minimized tumor mass and therapy
administration, and maximized eﬀector cell and IL-
2 concentration.
A down-side to the model was
that at the end of treatment, tumor mass tended
to start regrowth. Ghaﬀeri and Naserifar [31] im-
proved upon the model of Burden at al. [7] by in-
cluding a linear penalty, −ωy(tf), where ω is con-
stant, y is the quantity of cancer cells and tf is the
ﬁnal time-point of observation, such that their ob-
jective functional is JG(u) = −ωy(tf)+JB(u) (note
that −ωy(tf) is the terminal payoﬀfor JG(u), as
deﬁned above). The updated objective functional
allowed for identiﬁcation of a treatment that stops
tumor regrowth and also acts faster than the treat-
ment identiﬁed with JB(u).
6


## Page 7


Similarly, Castiglione and Piccoli [11] used opti-
mal control for a model they developed to investi-
gate dendritic cell vaccine (DCV) therapy for solid
avascular tumors. For N total number of vaccina-
tions and η total time for one vaccination, the space
of admissible controls, U, was taken to be
U = {us : S ∈S},
where S = {ti : i = 0, ..., N −1, 0 ≤t0 ≤T −η}
is the space of DCV injection schedules, S, and for
every S in the space of schedules US, u was taken
to be
us(T) =
N−1
X
i=0
¯u(t −ti)χ[ti,ti+η],
(5)
where ¯u : [0, η] 7→[0, ¯V ], with η the total time of
vaccination, ¯V maximum vaccine amount, and χ the
indicator function. For every us, the therapy con-
sisted of vaccine injections, modeled by ¯u, at time-
intervals [ti −η, ti] for all ti in S.
The objective
functional (here termed the cost functional since it
was minimized) was taken to be the ﬁnal value of
the tumor mass M, and the optimal control prob-
lem was stated as follows: for initial condition x0,
what is the schedule S ∈US such that M attains
a minimum? The problem stated as such is known
as the Mayer form, which can be used when the
running payoﬀ, r, is zero in Equation 3. The au-
thors took T =6 months, N = 10 DCV injections,
and η = 0. An initial schedule S0 was chosen ran-
domly and 2000 optimization steps were taken to
ﬁnd the optimal ¯S, which resulted in almost com-
plete clearance of a tumor. Nevertheless, resurgence
of tumor cells occured between vaccinations and the
ﬁnal value of the tumor mass was highly dependent
on the timing of the last vaccination.
In order to correct for this eﬀect, Piccoli and
Castiglione [54] expanded the cost functional in [11]
to also minimize the time during which the tumor
is above a maximum mass, M max, necessitating a
switch back to the Bolza form for their objective
functional. The authors emphasized that the opti-
mal injection schedule u∗obtained is highly depen-
dent on the parameter values and initial conditions
of the system, indicating that the parametrization
of the system from patient characteristics or other
relevant knowledge should be performed carefully.
Castiglione and Piccoli [10] further expanded the
cost functional in [54] to include, in addition to the
previous constraints, drug holidays and minimiza-
tion of vaccine injected to lower toxicity. The au-
thors also considered diﬀerent types of cost func-
tions: continuous, impulsive (similar to Equation 5,
but with η = 0), or hybrid (Equation 5, η ̸= 0), to
take into account the diﬀerent scales between du-
ration of drug injection and tumor growth.
The
hybrid method was found to be most eﬀective for
their system and the optimal treatment schedule
that was identiﬁed consisted of a high initial dose
and repeated smaller follow-up doses.
These examples of optimal control theory ap-
plied to cancer immunotherapy show that the con-
trols are developed slowly, with complex control
functions often built upon more simple and estab-
lished ones.
4.2
Genetic algorithms
For computational agent-based models, function op-
timizers such as genetic algorithms (GAs) are more
suitable.
GAs are part of a class of evolutionary
algorithms that work as follows:
a set of n ini-
tial binary strings, {S(1)
i
}n
i=1, sometimes termed
‘chromosomes’, representing possible solutions to
the problem of interest are processed via an evalu-
ation function, Ei = Ei(Si), which gives a measure
of the string’s performance, and a ﬁtness function,
Fi = Fi({Ei}), that compares the performance of all
the strings to each other. In the intermediate selec-
tion phase, strings S(1)
i
are kept and duplicated with
probability proportional to their respective ﬁtness
functions, Fi. The strings of this intermediate popu-
lation, {S(1∗)
i
} are then recombined with each other
by cross-over and mutated at a low rate to obtain
a new generation of strings, {S(2)
i
} (note that the i
do not represent the same string between the gener-
ations (1), (1*), and (2)). This process is repeated
until an ‘optimal‘ string is found, either via running
7


## Page 8


the algorithm for a ﬁxed number of generations, or
until a string is found that surpasses a threshold set
by the ﬁtness function. This optimal string, like ×
u∗in optimal control theory, represents an optimal
therapy solution given constraints imposed by the
evaluation and/or ﬁtness functions.
Importantly,
an agent-based or other computational model can
be run with any possible therapy (’string’), and
the results can be used to determine the output of
the evaluation function, thus the optimal string will
give the optimal therapy vis-a-vis the computational
model. We have described the ‘canonical genetic al-
gorithm’ [68] originally developed in [33], and there
exist many modiﬁcations that will not be presented
here [68, 48].
Lollini et al. [44] set out to use a GA to de-
velop an optimal vaccine schedule for the agent-
based SimTriplex model [53] described in Section
3.
The Triplex vaccine is a cell-based vaccine
that stimulates an immune response via engineered
HER-2/neu positive cells that express allogenic
MHC Class-1 molecules (for increased recognition
by CD8+ T cells) and IL-12, which boosts both hu-
moral and adaptive immunity [16].
The GA was
initialized with 80 binary 1200-bit strings, where
each bit represents a time-step where a vaccine in-
jection is/is not (1/0) given. For each string, the
SimTriplex simulator was used to determine mouse
survival time (s) and maximum number of cancer
cells in the transient (N 1
cc) and steady (N 2
cc) tumor
growth phases. The evaluation function was then
taken to be,
f(n, s, β) = n2
s · β,
(6)
where n is the number of injections speciﬁed by the
test string, and β = β(N 1
cc, N 2
cc) is proportional to
the maximum number of cancer cells. Note that in
this implementation, the aim was to minimize the
ﬁtness function. Via tournament selection (the ﬁt-
ness functions of two or more strings are compared
and the probability of selecting a string is propor-
tional to the ﬁtness ranking of the string), followed
by mutation and elitism (the best strings are not
mutated), an optimal string (i.e. vaccination sched-
ule) was selected. Also, in this case, Equation 6 was
referred to as the ‘ﬁtness’ function, which is not to
be confused with our deﬁnition above.
An extension of this ﬁtness function was ap-
plied in the algorithm in [44] which incorporated
several instances of in silico mice with varying im-
mune backgrounds to choose the optimal vaccina-
tion schedule, S∗. This schedule was applied to two
sets of 100 virtual HER-2/neu positive mice and re-
sulted in 90% survival rate (this is in comparison
to a chronic protocol, which requires 4 vaccinations
in a 2-week ’on’ and 2-week ’oﬀ’ protocol, over the
course of at least one year, and has 100% success
rate, but is not realistic for clinical development).
A previous ’trial and error’ schedule was found to
reduce the number of injections by ∼27% over the
chronic schedule, whereas the one identiﬁed by the
GA reduced it by ∼42%, yielded excellent survival,
and generated similar immune dynamics to the cur-
rent protocol. In a follow-up study, Palladini et al.
[52] showed excellent agreement between the in sil-
ico predictions and in vivo experiments, and made
additional observations, such as the importance of
vaccination density in the early phase of the im-
mune response and dependence of vaccine success on
age of the mouse. GAs and evolutionary algorithms
have also been used to identify potential epitopes for
vaccine development [4], to develop an initial guess
for a discrete optimal control problem based on the
model in [10], [47], and to solve a multi-objective
optimization problem for a model of combination
chemo- and immunotherapy [39].
By example of optimal control theory and ge-
netic algorithms, we have shown how mathematical
methods in optimization used in conjunction with
appropriate models yield treatment schedules de-
rived in a systematic, rather than experimental or
computational ‘trial and error’ method, that can be
used not only to create optimal treatment schedules,
but to also better understand immune response to
treatment, such as the observations obtained from
both methods above to the relative importance of
early vs. late immunization protocols.
8


## Page 9


5
Challenge: Design and iden-
tiﬁcation
of
combination
treatment regimes
Just
as
combination
therapy
using
non-
immunotherapeutic approaches is a mainstay in
cancer treatment, combination immunotherapy ei-
ther with just immunotherapeutic agents or with
immune- and non-immunotherapeutic agents can
and should be designed rationally to maximize
treatment response [46, 51].
Modeling can con-
tribute to this process as it can aid in the develop-
ment of a mechanistic understanding for eﬀective-
ness of combination vs. mono-therapies and make
the search for an optimal combination therapy more
eﬃcient. For example, de Pillis et al. developed a
system of six ODEs for combination chemo- and
immunotherapy that included tumor, NK, CD8+,
and white blood cells, as well as bloodstream con-
centrations of chemotherapy (doxorubicin) and im-
munotherapy drugs, the latter of which include
tumor-inﬁltrating-lymphocyte (TIL) therapy and
IL-2 stimulation [17]. The model extended an ear-
lier model by de Pillis et al. [18] to include more re-
cent biological ﬁndings. The eﬀect of chemotherapy,
M, was modeled using a saturation term, 1−e−δM,
where δ represents the eﬃcacy of M, and the boost
to CD8+ activity by addition of IL-2 was modeled
using a Michaelis-Menten interaction term, similar
to what we see in Equation 1 from [40]. Cell-cell
interaction terms were modeled using previously ﬁt
equations, often of Michaelis-Menten type. For ex-
ample, the CD8+ T cell stimulation by the tumor
was taken to be
dL
dT ∝j
T
k + T L,
(7)
where
T
and
L
represent
the
tumor
and
CD8+populations, respectively, and j and k are pa-
rameters. Following [18], several parameters of the
model, which collectively determine CD8+ T cell
eﬃcacy at tumor cell killing, were ﬁtted to patient-
speciﬁc data. The authors found that the success
of combination vs. mono-therapy diﬀered based on
initial patient characteristics. or example a patient
with higher CD8+ T cell eﬃcacy would beneﬁt more
strongly from immuno- or combination therapy than
a patient with low eﬃcacy, since an injection of IL-2
for the latter group would result in more CD8+ T
cells, but not enough to increase overall anti-tumor
response. Notably, had the authors modeled an im-
munotherapy that altered these variables directly
(such as injection of CD8+ T cell costimulator ago-
nists that boost CD8+ eﬀector activity), they would
have obtained diﬀerent success rates for the therapy
combinations. Nevertheless, the model can serve as
a forerunner to models parametrized with patient-
speciﬁc parameters that can then be used to identify
optimal therapy combinations.
Targeted therapies, such as antibodies against
the breast cancer cell receptor HER2 and EGFR,
elicit a strong, adaptive immune response, raising
the implication that combination immunotherapy
with targeted therapy can achieve a synergistic anti-
tumor immune response [64, 70]. The humanized
antibody to VEGF, Avastin (bevacizumab), is FDA-
approved for a number of diﬀerent cancers, and in
addition to blocking the pro-angiogenic activity of
tumor-produced VEGF, also blocks the immuno-
suppressive activity of VEGF, which includes sup-
pression of DC maturation [36]. Soto-Ortiz et al.
[61] hypothesized that a combination therapy of an
anti-VEGF antibody followed by administration of
DC cells would result in a strong anti-tumor re-
sponse by the immune system. The authors built
upon a model that focuses on tumor-immune inter-
actions [55] to develop a system of 18 ODEs that in-
clude tumor, immune, and vascular endothelial cells,
and a number of cytokines and growth factors in-
cluding IL-2, TGFβ, and VEGF (TGFβ and VEGF
are both considered to be immunosuppressive). The
authors simulated treatment with injection of anti-
VEGF antibody and/or unstimulated DC cells and
analyzed the results numerically. The simulations
showed that for tumors with low immunosuppres-
sion and high antigenecity, which is represented by
a parameter that models the strength of matura-
9


## Page 10


tion of DCs after encounter with a tumor antigen,
the immune system can keep the tumor at a small
size and administration of either therapy can kill the
entire tumor.
When tumor antigenecity was low-
ered and immunosuppression increased, the simu-
lated tumor grew and vascularized without therapy.
The authors observed that for tumors with high im-
munosuppression, DC therapy alone was not suﬃ-
cient to kill the tumor without additional modiﬁca-
tion of the immunosuppressive microenvironment,
which is an example of a prediction for eﬀectiveness
of a mono-therapy vs. combination when given ini-
tial system parameters. The authors made a num-
ber of other observations regarding the interdepen-
dencies of tumor growth, antigenecity, and immuno-
suppression that would not have been possible in a
simpler model. A prediction arising from this anal-
ysis was that there exists a therapeutic window for
optimal eﬀectiveness of diﬀerent immunotherapies
that is dependent on the tumor size and growth rate,
and thus knowledge of these tumor characteristics
can be used to design the optimal mono- or com-
bination therapy for a given tumor/patient. More-
over, synergy in combination therapy was predicted
to occur when immunotherapy followed anti-VEGF
treatment, thus the model was able to address ques-
tions of eﬃcacy prediction and optimal time and se-
lection of treatment, and hence eﬀectively address
all the major challenges we have discussed.
Models for various combinations of traditional
and immunotherapies have been developed [9, 23,
69, 60], which generally build on earlier mono-
therapy, tumor-immune, or even combination ther-
apy models. For example, Chareyron and Alamir
[12] extend earlier models developed by de Pillis et
al. [19, 20] to include chemo- and immunotherapy
and use control theory to determine optimal therapy
protocols, again addressing multiple big challenges
discussed herein. These models can give insights as
to mechanism and eﬃcacy of combination therapies
in order to guide clinical development.
6
Recommendations
6.1
Intracellular
and
multi-scale
modeling
Most current immunotherapy models are developed
at the resolution level of cell populations.
How-
ever, modeling intracellular signaling cascades and
metabolic responses in speciﬁc cell types can give
insight into how therapies can act at the intracel-
lular level, and what the relative contribution of
diﬀerent therapies is to cell response:
intracellu-
lar vs.
cell-cell.
As in the case of population-
level models of immunotherapy, where the therapy
component is often added to an existing, validated
model of tumor-immune interactions, the intracel-
lular models of therapy can build on known sig-
naling pathways that interact with proposed ther-
apies in tumors and T cells.
Intracellular signal-
ing models have been developed for cancer signal-
ing pathways for a variety of tumor types[34, 2],
and can be modiﬁed to include subpathways of in-
terest, such as induction of PD-L1 or secreted im-
munosuppressive factors. Saez-Rodriguez et al.[58]
built a Boolean network model of a signaling net-
work activated upon T cell receptor and corecep-
tor activation and validated it using both literature
and experimental wild-type and knock-out data that
matched in silico predictions. This network could
be made more speciﬁc for diﬀerent T cells (CD4+,
CD8+, Treg), receptors of therapeutic interest (e.g.
CTLA-4, PD-1) and their downstream signaling tar-
gets, which can be added to the model in order to
examine how therapy would aﬀect T cell activation
status.
Modiﬁcation of networks identiﬁed in the
literature may require additional experimental in-
put, depending on the current availability of data.
Such models would allow a more granular systems-
level analysis of mechanisms of pharmaceutical ac-
tion and subsequent therapy optimization and com-
bination. Furthermore, since immunotherapy drugs
can act on multiple cell targets, for example CTLA-
4 is expressed not only on CD8+ T cells but also
10


## Page 11


Tregs, development of multi-scale models that in-
corporate both the interactions of diﬀerent immune
and tumor cell types and their respective intracellu-
lar dynamics would have the power to elucidate the
multi-scale mechanisms of therapy action. Indeed,
multi-scale modeling has already been identiﬁed as a
important method for generating systems-level pre-
dictions of cancer progression and therapy eﬀective-
ness [21, 65].
6.2
Addressing toxicity
Immune-mediated toxicities, including retinal dys-
function, liver toxicity, and pancreatitis can oc-
cur upon administration of immunotherapy. Tox-
icity, which is generally caused by targeting of
self-antigens by the drug-strengthened immune re-
sponse, is often associated with clinical response
[1].
Incorporation of immunotherapy-related tox-
icity into models can result in estimates of ther-
apy dose that take into account toxicity-related ef-
fects, as was already done in [7]. Development of
more mechanistic models can help to optimize ther-
apies to maximize eﬀectiveness and minimize tox-
icity if mechanisms for each are not entirely over-
lapping. This may be especially important in mod-
els of combination immunotherapy, where toxicity-
related events tend to be more common than with
monotherapies [45]. One route of interest towards
this goal can be a joint experimental-modeling fo-
cus on Fc-FcR interactions.
Immunomodulatory
mAbs such as ipilimumab, a mAb to CTLA-4, are
most often of IgG isotope: in addition to contain-
ing two antigen-binding (Fab) domains, they con-
tain a fragment crystallizable (Fc) ’tail’ that can
bind Fc receptors (FcRs) found on eﬀector cells
such as macrophages and DCs. Fc-FcR interactions
have been shown to contribute to cytokine-related
adverse events during mAb treatment, and hence
modulation of these interactions during mAb de-
sign could help to decouple therapeutic from toxic
responses. A better mechanistic understanding of
Fc-FcR engagement and response during treatment
could help lead to rational design of mAbs that re-
duce adverse events related to Fc-FcR interactions
(reviewed in [57]).
By developing models of Fc-
FcR action in concert with experimentalists, model-
ers can hasten this process and use their models to
guide development of optimized therapy options.
7
Conclusion
Immunotherapy is one of the most exciting recent
developments in cancer treatment, with new drugs
coming on the market at an increasing rate, for
an ever-larger number of cancers.
But, as this
review highlights, many unanswered questions re-
main, and the ﬁeld faces several challenges. Math-
ematical modelers have addressed these challenges
as early as the 1980’s (e.g., [15]). The models we
have reviewed here and their use in understanding
various aspects of immunotherapy crucial for eﬀec-
tive treatment, show that mathematical and com-
putational models can play the role of a key en-
abling technology to improve the application of this
type of treatment. However, as this review also dis-
cusses, there is much work to be done. Almost all
immunotherapy-speciﬁc modeling eﬀorts we could
identify focus on the population level, even though
it is clear that a multi-scale approach is needed that
also incorporates the molecular scale. To aid this
process and to stay at the forefront of immunother-
apy technology development, high-throughput data
derived from technologies such as microarrays and
RNA-Seq for cell-level transcriptional information
and mass cytometry (CyTOF) for population-level
marker distribution can be incorporated into model
development [13].
Collaborations between modelers, basic scien-
tists, and clinicians are crucial for the realization of
the translational potential of mathematical model-
ing in the service of a precision medicine approach to
this revolutionary new cancer treatment. As many
of the models show, parameter values matter greatly
in predicting treatment outcomes and devising op-
timal treatment approaches.
Personalized models
that can be calibrated with parameters characteris-
11


## Page 12


tic of an individual patient will turn mathematical
models into powerful tools that can play an essential
role at the bedside, not just in the laboratory.
Acknowledgments
AK gratefully acknowledges support from the National
Cancer Institute of the National Institutes of Health
postdoctoral fellowship award F32CA214030. RL grate-
fully acknowledges support from the National Cancer In-
stitute of the National Institutes of Health under grant
1R01CA188025-01.
References
[1] Sally M Amos, Connie P M Duong, Jennifer A
Westwood, David S Ritchie, Richard P Junghans,
Phillip K Darcy, and Michael H Kershaw. Autoim-
munity associated with immunotherapy of cancer.
Blood, 118(3):499–509, Jul 2011.
[2] J Bachmann, A Raue, M Schilling, V Becker,
J Timmer, and U Klingmüller.
Predictive math-
ematical models of cancer signalling pathways. J
Intern Med, 271(2):155–65, Feb 2012.
[3] Sandip Banerjee, Subhas Khajanchi, and Swapna
Chaudhuri.
A mathematical model to elucidate
brain tumor abrogation by immunotherapy with
t11 target structure.
PLoS One, 10(5):e0123611,
2015.
[4] V Brusic, G Rudy, G Honeyman, J Hammer, and
L Harrison.
Prediction of MHC class ii-binding
peptides using an evolutionary algorithm and artiﬁ-
cial neural network. Bioinformatics, 14(2):121–30,
1998.
[5] Svetlana Bunimovich-Mendrazitsky, Helen Byrne,
and Lewi Stone. Mathematical model of pulsed im-
munotherapy for superﬁcial bladder cancer.
Bull
Math Biol, 70(7):2055–76, Oct 2008.
[6] Svetlana
Bunimovich-Mendrazitsky,
Eliezer
Shochat, and Lewi Stone. Mathematical model of
BCG immunotherapy in superﬁcial bladder cancer.
Bull Math Biol, 69(6):1847–70, Aug 2007.
[7] Thalya Burden, Jon Ernstberger, and K. Renee Fis-
ter.
Optimal control applied to immunotherapy.
Discrete and Continuous Dynamical Systems - Se-
ries B, 4(1):135–146, 2004.
[8] HM Byrne and CE Kelly. Macrophage-tumour in-
teractions: In vivo dynamics. Discrete and Con-
tinuous Dynamical Systems - Series B, 4(1):81–98,
2004.
[9] Antonio
Cappuccio,
Filippo
Castiglione,
and
Benedetto Piccoli.
Determination of the optimal
therapeutic protocols in cancer immunotherapy.
Math Biosci, 209(1):1–13, Sep 2007.
[10] F Castiglione and B Piccoli. Cancer immunother-
apy, mathematical modeling and optimal control. J
Theor Biol, 247(4):723–32, Aug 2007.
[11] Filippo Castiglione and Benedetto Piccoli. Optimal
control in a model of dendritic cell transfection can-
cer immunotherapy. Bull Math Biol, 68(2):255–74,
Feb 2006.
[12] S. Chareyron and M. Alamir. Mixed immunother-
apy and chemotherapy of tumors: Feedback design
and model updating schemes. Journal of Theoreti-
cal Biology, 258(3):444–454, 2009.
[13] Pornpimol Charoentong, Mihaela Angelova, Mir-
jana
Efremova,
Ralf
Gallasch,
Hubert
Hackl,
Jerome Galon, and Zlatko Trajanoski.
Bioinfor-
matics for cancer immunology and immunother-
apy.
Cancer Immunol Immunother, 61(11):1885–
903, Nov 2012.
[14] Daniel S Chen and Ira Mellman. Oncology meets
immunology: the cancer-immunity cycle.
Immu-
nity, 39(1):1–10, Jul 2013.
[15] R J De Boer, P Hogeweg, H F Dullens, R A
De Weger, and W Den Otter.
Macrophage T
lymphocyte interactions in the anti-tumor immune
response:
a mathematical model.
J Immunol,
134(4):2748–58, Apr 1985.
[16] Carla De Giovanni, Giordano Nicoletti, Lorena
Landuzzi, Annalisa Astolﬁ, Stefania Croci, Al-
berto Comes, Silvano Ferrini, Raﬀaella Meazza,
Manuela Iezzi, Emma Di Carlo, Piero Musiani,
Federica Cavallo, Patrizia Nanni, and Pier-Luigi
Lollini.
Immunoprevention of HER-2/neu trans-
genic mammary carcinoma through an interleukin
12-engineered allogeneic cell vaccine. Cancer Res,
64(11):4001–9, Jun 2004.
12


## Page 13


[17] Lisette G de Pillis, K. Renee Fister, Weiqing Gu,
Craig Collins, Michael Daub, David Gross, James
Moore,
and Benjamin Preskill.
Mathematical
model creation for cancer chemo-immunotherapy.
Computational
and
Mathematical
Methods
in
Medicine, 10(3):165–184, 2009.
[18] Lisette G de Pillis, Weiqing Gu, and Ami E Radun-
skaya.
Mixed immunotherapy and chemotherapy
of tumors: modeling, applications and biological
interpretations. J Theor Biol, 238(4):841–62, Feb
2006.
[19] Lisette G de Pillis and Ami E Radunskaya.
Im-
mune response to tumor invasion.
In K. Bathe,
editor, Computational Fluid and Solid Mechanics
2003, volume 2, pages 1661–1668, Cambridge, MA,
2003. MIT Press.
[20] Lisette G de Pillis,
Ami E Radunskaya,
and
Charles L Wiseman.
A validated mathematical
model of cell-mediated immune response to tumor
growth. Cancer Res, 65(17):7950–8, Sep 2005.
[21] Thomas S Deisboeck, Zhihui Wang, Paul Macklin,
and Vittorio Cristini. Multiscale cancer modeling.
Annu Rev Biomed Eng, 13:127–55, Aug 2011.
[22] Alberto d’Onofrio. Metamodeling tumor–immune
system
interaction,
tumor
evasion
and
im-
munotherapy.
Mathematical and Computer Mod-
elling, 47:614–637, 2008.
[23] Alberto d’Onofrio, Ledzewixa Urszula, and Heinz
Schattler.
New
challenges
for
cancer
sys-
tems biomedicine, chapter On the Dynamics of
Tumor-Immune System Interactions and Combined
Chemo- and Immunotherapy. Springer Milan, 2012.
[24] D. Dréau, D. Stanimirov, T. Carmichael, and
M. Hadzikadic. An agent-based model of solid tu-
mor progression. In Rajasekaran S., editor, Bioin-
formatics and Computational Biology, volume 5462
of Lecture Notes in Computer Science, pages 187–
198. Springer, 2009.
[25] Gavin P Dunn, Allen T Bruce, Hiroaki Ikeda,
Lloyd J Old, and Robert D Schreiber. Cancer im-
munoediting: from immunosurveillance to tumor
escape. Nat Immunol, 3(11):991–8, Nov 2002.
[26] Raluca Eftimie, Jonathan L Bramson, and David
J D Earn. Interactions between the immune sys-
tem and cancer: a brief review of non-spatial math-
ematical models. Bull Math Biol, 73(1):2–32, Jan
2011.
[27] Steﬀen Eikenberry, Craig Thalhauser, and Yang
Kuang. Tumor-immune interaction, surgical treat-
ment,
and cancer recurrence in a mathemati-
cal model of melanoma.
PLoS Comput Biol,
5(4):e1000362, Apr 2009.
[28] Lawrence C. Evans.
An introduction to math-
ematical
optimal
control
theory,
Version
0.2.
https://math.berkeley.edu/ evans/control.course.pdf.
Accessed: 2017-05-03.
[29] Olivera J Finn. Cancer immunology. N Engl J Med,
358(25):2704–15, Jun 2008.
[30] Jérôme Galon, Franck Pagès, Francesco M Marin-
cola, Helen K Angell, Magdalena Thurin, Alessan-
dro Lugli, Inti Zlobec, Anne Berger, Carlo Bi-
fulco, Gerardo Botti, Fabiana Tatangelo, Cedrik M
Britten,
Sebastian
Kreiter,
Lotﬁ
Chouchane,
Paolo
Delrio,
Hartmann
Arndt,
Martin
Ass-
laber, Michele Maio, Giuseppe V Masucci, Mar-
tin Mihm, Fernando Vidal-Vanaclocha, James P
Allison, Sacha Gnjatic, Leif Hakansson, Christoph
Huber, Harpreet Singh-Jasuja, Christian Ottens-
meier, Heinz Zwierzina, Luigi Laghi, Fabio Grizzi,
Pamela S Ohashi, Patricia A Shaw, Blaise A
Clarke, Bradly G Wouters, Yutaka Kawakami,
Shoichi Hazama, Kiyotaka Okuno, Ena Wang,
Jill O’Donnell-Tormey, Christine Lagorce, Graham
Pawelec, Michael I Nishimura, Robert Hawkins,
Réjean Lapointe, Andreas Lundqvist, Samir N
Khleif,
Shuji Ogino,
Peter Gibbs,
Paul War-
ing,
Noriyuki Sato,
Toshihiko Torigoe,
Kyogo
Itoh, Prabhu S Patel, Shilin N Shukla, Richard
Palmqvist, Iris D Nagtegaal, Yili Wang, Corrado
D’Arrigo, Scott Kopetz, Frank A Sinicrope, Giorgio
Trinchieri, Thomas F Gajewski, Paolo A Ascierto,
and Bernard A Fox. Cancer classiﬁcation using the
immunoscore:
a worldwide task force.
J Transl
Med, 10:205, Oct 2012.
[31] A Ghaﬀari and N Naserifar. Optimal therapeutic
protocols in cancer immunotherapy. Comput Biol
Med, 40(3):261–70, Mar 2010.
[32] F Stephen Hodi, Steven J O’Day, David F Mc-
Dermott, Robert W Weber, Jeﬀrey A Sosman,
John B Haanen, Rene Gonzalez, Caroline Robert,
Dirk Schadendorf, Jessica C Hassel, Wallace Ak-
erley, Alfons J M van den Eertwegh, Jose Lutzky,
13


## Page 14


Paul Lorigan, Julia M Vaubel, Gerald P Linette,
David Hogg, Christian H Ottensmeier, Celeste
Lebbé, Christian Peschel, Ian Quirt, Joseph I
Clark, Jedd D Wolchok, Jeﬀrey S Weber, Jason
Tian, Michael J Yellin, Geoﬀrey M Nichol, Axel
Hoos, and Walter J Urba. Improved survival with
ipilimumab in patients with metastatic melanoma.
N Engl J Med, 363(8):711–23, Aug 2010.
[33] John H Holland. Adaptation in natural and artiﬁ-
cial systems. University of Michigan Press. (Second
edition: MIT Press, 1992), 1975.
[34] Jorrit J Hornberg, Frank J Bruggeman, Hans V
Westerhoﬀ, and Jan Lankelma. Cancer: a systems
biology disease. Biosystems, 83(2-3):81–90, 2006.
[35] Laura Jeanbart and Melody A Swartz. Engineering
opportunities in cancer immunotherapy. Proc Natl
Acad Sci U S A, 112(47):14467–72, Nov 2015.
[36] Benjamin F Johnson, Timothy M Clay, Amy C
Hobeika, H Kim Lyerly, and Michael A Morse. Vas-
cular endothelial growth factor and immunosup-
pression in cancer: current knowledge and potential
for new therapy. Expert Opin Biol Ther, 7(4):449–
60, Apr 2007.
[37] Badal Joshi, Xueying Wang, Sayanti Banerjee,
Haiyan Tian, Anastasios Matzavinos, and Mark
A J Chaplain.
On immunotherapies and cancer
vaccination protocols: a mathematical modelling
approach. J Theor Biol, 259(4):820–7, Aug 2009.
[38] Philip W Kantoﬀ, Celestia S Higano, Neal D
Shore, E Roy Berger, Eric J Small, David F
Penson,
Charles H Redfern,
Anna C Ferrari,
Robert Dreicer, Robert B Sims, Yi Xu, Mark W
Frohlich,
Paul F Schellhammer,
and IMPACT
Study Investigators. Sipuleucel-T immunotherapy
for castration-resistant prostate cancer. N Engl J
Med, 363(5):411–22, Jul 2010.
[39] Kanchi Lakshmi Kiran and S. Lakshminarayanan.
Optimization of chemotherapy and immunother-
apy:
In silico analysis using pharmacokinetic–
pharmacodynamic and tumor growth models. Jour-
nal of Process Control, 23(3):396–403, 2013.
[40] D Kirschner and J C Panetta.
Modeling im-
munotherapy of the tumor-immune interaction. J
Math Biol, 37(3):235–52, Sep 1998.
[41] Anna Konstorum, Thomas Hillen, and John Lowen-
grub.
Feedback regulation in a cancer stem cell
model can cause an allee eﬀect.
Bull Math Biol,
78(4):754–85, Apr 2016.
[42] Natalie Kronik, Yuri Kogan, Paul G Schlegel, and
Matthias Wölﬂ. Improving T-cell immunotherapy
for melanoma through a mathematically motivated
strategy:
eﬃcacy in numbers?
J Immunother,
35(2):116–24, 2012.
[43] Natalie Kronik, Yuri Kogan, Vladimir Vainstein,
and Zvia Agur.
Improving alloreactive CTL im-
munotherapy for malignant gliomas using a simu-
lation model of their interactive dynamics. Cancer
Immunol Immunother, 57(3):425–39, Mar 2008.
[44] Pier-Luigi Lollini, Santo Motta, and Francesco
Pappalardo. Discovery of cancer vaccination pro-
tocols with a genetic algorithm driving an agent
based simulator. BMC Bioinformatics, 7:352, Jul
2006.
[45] Ignacio Melero, David M Berman, M Angela Az-
nar, Alan J Korman, José Luis Pérez Gracia, and
John Haanen. Evolving synergistic combinations of
targeted immunotherapies to combat cancer. Nat
Rev Cancer, 15(8):457–72, Aug 2015.
[46] Ira Mellman, George Coukos, and Glenn Dranoﬀ.
Cancer immunotherapy comes of age.
Nature,
480(7378):480–9, Dec 2011.
[47] Andrea Minelli, Francesco Topputo, and Franco
Bernelli-Zazzera. Controlled drug delivery in can-
cer immunotherapy:
Stability, optimization, and
monte carlo analysis.
SIAM Journal on Applied
Mathematics, 71(6):2229–2245, 2011.
[48] Melanie Mitchell. An Introduction to Genetic Al-
gorithms. MIT Press, Cambridge, MA, USA, 1998.
[49] Deepak Mittal, Matthew M Gubin, Robert D
Schreiber, and Mark J Smyth. New insights into
cancer immunoediting and its three component
phases–elimination, equilibrium and escape. Curr
Opin Immunol, 27:16–25, Apr 2014.
[50] F Nani and H I Freedman. A mathematical model
of cancer treatment by immunotherapy.
Math
Biosci, 163(2):159–99, Feb 2000.
[51] Abigail E. Overacre, Sema Kurtulus, Mario Sznol,
Drew M. Pardoll, Ana Anderson, and Dario A. A.
Vignali. Combination immunotherapy: Where do
we go from here?
J Immunother Cancer, 3(38),
2015.
14


## Page 15


[52] Arianna Palladini, Giordano Nicoletti, Francesco
Pappalardo, Annalisa Murgo, Valentina Grosso,
Valeria Stivani, Marianna L Ianzano, Agnese An-
tognoli, Stefania Croci, Lorena Landuzzi, Carla
De Giovanni, Patrizia Nanni, Santo Motta, and
Pier-Luigi Lollini. In silico modeling and in vivo
eﬃcacy of cancer-preventive vaccinations. Cancer
Res, 70(20):7755–63, Oct 2010.
[53] F Pappalardo, P-L Lollini, F Castiglione, and
S
Motta.
Modeling
and
simulation
of
can-
cer immunoprevention vaccine.
Bioinformatics,
21(12):2891–7, Jun 2005.
[54] Benedetto Piccoli and Filippo Castiglione.
Opti-
mal vaccine scheduling in cancer immunotherapy.
Physica A: Statistical Mechanis and its Applica-
tions, 370(2):672–680, 2006.
[55] Mark Robertson-Tessi, Ardith El-Kareh, and Alain
Goriely. A mathematical model of tumor-immune
interactions. J Theor Biol, 294:56–73, Feb 2012.
[56] Steven A Rosenberg, Nicholas P Restifo, James C
Yang, Richard A Morgan, and Mark E Dudley.
Adoptive cell transfer: a clinical path to eﬀective
cancer immunotherapy. Nat Rev Cancer, 8(4):299–
308, Apr 2008.
[57] Joseph M Ryan, Jeﬀrey S Wasser, Adam J Adler,
and Anthony T Vella.
Enhancing the safety of
antibody-based immunomodulatory cancer therapy
without compromising therapeutic beneﬁt: Can we
have our cake and eat it too?
Expert Opin Biol
Ther, 16(5):655–74, 2016.
[58] Julio Saez-Rodriguez, Luca Simeoni, Jonathan A
Lindquist,
Rebecca
Hemenway,
Ursula
Bommhardt,
Boerge
Arndt,
Utz-Uwe
Haus,
Robert Weismantel, Ernst D Gilles, Steﬀen Klamt,
and Burkhart Schraven. A logical model provides
insights into T cell receptor signaling.
PLoS
Comput Biol, 3(8):e163, Aug 2007.
[59] Robert D Schreiber, Lloyd J Old, and Mark J
Smyth. Cancer immunoediting: integrating immu-
nity’s roles in cancer suppression and promotion.
Science, 331(6024):1565–70, Mar 2011.
[60] Raphael
Serre,
Sebastien
Benzekry,
Laetitia
Padovani,
Christophe
Meille,
Nicolas
André,
Joseph Ciccolini, Fabrice Barlesi, Xavier Muracci-
ole, and Dominique Barbolosi. Mathematical mod-
eling of cancer immunotherapy and its synergy with
radiotherapy.
Cancer Res, 76(17):4931–40, Sep
2016.
[61] Luis Soto-Ortiz and Stacey D Finley.
A can-
cer treatment based on synergy between anti-
angiogenic and immune cell therapies. J Theor Biol,
394:197–211, Apr 2016.
[62] Pramod K Srivastava and Fei Duan. Harnessing the
antigenic ﬁngerprint of each individual cancer for
immunotherapy of human cancer: genomics shows
a new way and its challenges. Cancer Immunol Im-
munother, 62(5):967–74, May 2013.
[63] Pam Tarapchak. Tecentriq approved for targeted
treatment of bladder cancer. Oncology Times, 2016.
[64] Matthew Vanneman and Glenn Dranoﬀ. Combin-
ing immunotherapy and targeted therapies in can-
cer treatment. Nat Rev Cancer, 12(4):237–51, Mar
2012.
[65] Zhihui Wang, Joseph D Butner, Romica Kerketta,
Vittorio Cristini, and Thomas S Deisboeck. Sim-
ulating cancer growth with multiscale agent-based
modeling. Semin Cancer Biol, 30:70–8, Feb 2015.
[66] Jeﬀrey Weber.
Review:
anti-ctla-4 antibody
ipilimumab:
case
studies
of
clinical
response
and immune-related adverse events.
Oncologist,
12(7):864–72, Jul 2007.
[67] Daniel K Wells, Yishuan Chuang, Louis M. Knapp,
Dirk Brockmann, William L. Kath, and Joshua N.
Leonard.
Spatial and functional heterogeneities
shape collective behavior of tumor-immune net-
works. PLoS Comput Biol, 11(4):e1004181, 2015.
[68] Darrell Whitley.
A genetic algorithm tutorial.
Statistics and Computing, 4(2):65–85, 1994.
[69] Shelby Wilson and Doron Levy. A mathematical
model of the enhancement of tumor vaccine eﬃcacy
by immunotherapy.
Bull Math Biol, 74(7):1485–
500, Jul 2012.
[70] Meng Michelle Xu, Yang Pu, Yuan Zhang, and
Yang-Xin Fu.
The role of adaptive immunity in
the eﬃcacy of targeted cancer therapies.
Trends
Immunol, 37(2):141–53, Feb 2016.
15

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
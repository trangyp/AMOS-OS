---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.12958v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1905.12958v2_Physically-Plausible_Modelling_of_Biomolecular_Systems__A_Simplified__Energy-Bas

> Source: 1905.12958v2_Physically-Plausible_Modelling_of_Biomolecular_Systems__A_Simplified__Energy-Bas.pdf

> Pages: 31

---


## Page 1


Physically-Plausible Modelling of Biomolecular Systems:
A Simpliﬁed, Energy-Based Model of the Mitochondrial
Electron Transport Chain
Peter J. Gawthrop1a,b, Peter Cudmorea,c, Edmund J. Crampina,b,c
aSystems Biology Laboratory, Department of Biomedical Engineering, Melbourne School of Engineering,
University of Melbourne, Victoria 3010, Australia
bSystems Biology Laboratory, School of Mathematics and Statistics, University of Melbourne, Victoria
3010, Australia
cARC Centre of Excellence in Convergent Bio-Nano Science and Technology, School of Chemical and
Biomedical Engineering, Melbourne School of Engineering, University of Melbourne, Victoria 3010,
Australia
Abstract
Advances in systems biology and whole-cell modelling demand increasingly compre-
hensive mathematical models of cellular biochemistry. Such models require the de-
velopment of simpliﬁed representations of speciﬁc processes which capture essential
biophysical features but without unnecessarily complexity. Recently there has been
renewed interest in thermodynamically-based modelling of cellular processes. Here
we present an approach to developing of simpliﬁed yet thermodynamically consistent
(hence physically plausible) models which can readily be incorporated into large scale
biochemical descriptions but which do not require full mechanistic detail of the un-
derlying processes. We illustrate the approach through development of a simpliﬁed,
physically plausible model of the mitochondrial electron transport chain and show that
the simpliﬁed model behaves like the full system.
1. Introduction
In mathematical biology, and more widely, the relative merits of simple ‘toy’ mod-
els, which represent some key aspects of the system but not full mechanistic detail,
and comprehensive mechanistically detailed representations have long been debated.
1Corresponding author. peter.gawthrop@unimelb.edu.au
Preprint submitted to Elsevier
January 8, 2020
arXiv:1905.12958v2  [q-bio.QM]  7 Jan 2020


## Page 2


Simple ‘toy’ models allow rigorous mathematical analysis and are generally easy to
simulate, but are diﬃcult to relate to the full system and measurements thereof. Full
mechanistically detailed models on the other hand provide a straight-forward mapping
to the real system, but are challenging to parameterize and analyse, and may require
signiﬁcant computational overhead to simulate.
Simple models of complex biochemical processes can elucidate basic behaviour
and biologically signiﬁcant trade-oﬀs (Scott et al., 2014; Weiße et al., 2015) and as
such can be used as an aid to synthetic biology (Darlington et al., 2018). Furthermore,
models of individual processes may be used as part of a model of an overall system
as, for example, in the Physiome Project (Crampin et al., 2004; Hunter, 2016), or in
whole-cell modelling Karr et al. (2012); Macklin et al. (2014); this requires models to
be modular and reusable (Neal et al., 2014; Nickerson et al., 2016).
Recently there has been renewed interest in thermodynamically-based mechanistic
modelling of cellular processes (Mason and Covert, 2019; Pan et al., 2019; Gawthrop
et al., 2017; Klipp et al., 2016; Beard and Qian, 2010). A modular approach to energy-
based modelling has been developed in the context of biomolecular systems (Gawthrop
et al., 2015; Gawthrop and Crampin, 2016). This raises the question as to whether it is
possible to develop energy-based models that are nevertheless simple.
Like engineering systems, living systems are subject to the laws of physics in gen-
eral and the laws of thermodynamics in particular. This fact gives the opportunity of
applying engineering approaches to the modelling, analysis and understanding of liv-
ing systems. The bond graph method of Paynter (1961) is one such well-established
engineering approach (Cellier, 1991; Gawthrop and Smith, 1996; Gawthrop and Be-
van, 2007; Borutzky, 2010; Karnopp et al., 2012) which has been extended to include
biomolecular systems (Oster et al., 1971, 1973; Gawthrop and Crampin, 2014, 2017;
Gawthrop et al., 2017; Gawthrop and Crampin, 2018a,b; Pan et al., 2018, 2019).
When developing simpliﬁed models of biomolecular systems where energy trans-
duction is important, it is essential that models be physically-plausible. A physically-
plausible model of a physical system has two attributes: it is itself a model of a physical
system (i.e. it does not contravene the laws of physics); and it shares key behaviours
with the actual physical system (Gawthrop, 2003). Such an approach will, however,
2


## Page 3


only be of use if there are complex physical systems which can indeed be represented
by a simpler physical model. This paper shows that this is indeed the case. In particular
we demonstrate that it is possible to develop a simpliﬁed model of the mitochondrial
electron transport chain that is thermodynamically consistent, but which doesn’t repre-
sent full mechanistic detail, and show that it behaves like the full model.
Mitochondria make use of reduction-oxidation (redox) reactions in which the trans-
fer of electrons is used to provide the power driving many living systems. As dis-
covered by Mitchell (1961, 1976, 1993, 2011), the key feature of mitochondria is
the chemiosmotic energy transduction whereby a chain of redox reactions pumps pro-
tons across the mitochondrial inner membrane to generate an electrochemical gradient
known as the proton-motive force (PMF). The PMF is then used to power the synthe-
sis of ATP – the universal fuel of living systems. Due to this central role in living
systems, mathematical modelling of the key components of mitochondria is thus an
important challenge to systems biology. Because mitochondria transduce energy, an
energy-based modelling method is desirable, and Beard and colleagues have developed
the most comprehensive such models to date (Beard, 2005; Wu et al., 2007; Beard and
Qian, 2010; Beard, 2012; Bazil et al., 2016). A bond graph model of mitochondrial
oxidative phosphorylation has been given by Gawthrop (2017). This model is based
on modelling the redox reactions associated with complexes CI, CIII and CIV of the
mitochondrial electron transport chain.
Below we brieﬂy outline the bond graph approach to modelling energy ﬂows in bio-
chemical reactions, in particular describing the Faraday-equivalent potential approach
to modelling electrochemical phenomena, and we describe a modiﬁed mass action ki-
netics approach which will be central to development of a simpliﬁed thermodynamic
modelling approach. A set of Python based tools has been developed to assist the
development and analysis of bond graph models and these tools are brieﬂy outlined.
We then discuss the Mitochondrial Electron Transport Chain (ETC) as an example
of a complex biomolecular system which can be successfully modelled by a simple
physically-plausible model, and use data from Bazil et al. (2016) to derive parameters
of the physically-plausible of the ETC to show that this simple model behaves the same
as a fully mechanistic description of the ETC. Finally we conclude with suggestions for
3


## Page 4


1
Ce:A
0
Ce:B
1
Re:r
Figure 1: Bond Graph representation of A
r
2 B. The bond graph components Ce:A and Ce:B represent
species A and B; the bond graph component Re:r represents the reaction the bonds ⇁together with the zero
0 and one 1 junctions deﬁne the stoichiometry (Gawthrop and Crampin, 2014). The bonds carry the energy
covariables chemical potential µ and and molar ﬂow v.
future research directions using simpliﬁed physically-plausible modelling as a strategy
in systems and synthetic biology.
2. Modelling Bioenergetics of Biochemical Systems using Bond Graphs
Bond graphs provide a convenient modular framework for modelling energy ﬂow
within and across diﬀerent physical domains: electrical, mechanical, chemical and so
on; and as such are useful for representing biomolecular systems. In brief, bonds repre-
sent pairs of variables: potential and ﬂow, whose product is power. In the biomolecular
domain, the product of chemical potential µ (with units J mol−1) and molar ﬂow v
(with units mol s−1) is power with units J s−1 (Oster et al., 1971, 1973; Gawthrop and
Crampin, 2014). Bonds connect components which represent either storage or dissipa-
tion of energy. In biomolecular systems, chemical potential is stored as concentration
of chemical species, denoted Ce 2 , whereas chemical reactions, denoted Re , in which
chemical species are converted from one form to another are dissipative processes. The
biochemical network stoichiometry is represented in the coupling of Ce components
via the reactions Re using bonds which represent the ﬂow of energy, connected using
common potential 0 (‘zero’) and common ﬂow 1 (‘one’) junctions.
2In this paper, Ce components are used to represent chemical species and C components to represent
electrical capacitors.
4


## Page 5


To illustrate, Figure 1 is the bond graph representation of the chemical reaction:
A
r
2 B
(2.1)
Ce components correspond to constitutive relations which relate the chemical poten-
tial to the amount of chemical species stored: the constitutive relations of Ce:A and
Ce:B are:
µA = RT ln KAxA
(2.2)
µB = RT ln KBxB
(2.3)
where xA and xB are the concentrations of A and B, KA and KB are species thermo-
dynamic constants (mol−1) for A and B, speciﬁc to each chemical species, R is the
universal gas constant and T the absolute temperature.
The constitutive relations for the reaction components Re provide the relationship
between forward and backward chemical aﬃnities A (stoichiometric combinations of
the chemical potentials) which provide the driving force for the reaction, and the molar
ﬂow (the reaction rate) f. The stoichiometry of reaction Re:r with formation of 2
molecules of species B for each molecule of A is represented by the two parallel bonds
on the right hand side of Re:r. With mass-action kinetics, the constitutive relation of
Re:r is
f = κ
 
exp A f
RT −exp Ar
RT
!
(2.4)
where κ is a reaction rate constant (mol s−1), speciﬁc to each reaction, and the forwards
and backwards aﬃnities are given by
Af = µA
(2.5)
and Ar = 2µB
(2.6)
Combining these expressions gives the familiar mass-action expression for the reaction
ﬂow f:
f = κ

KAxA −K2
Bx2
B

(2.7)
where the forward reaction rate constant k+ = κKA and the reverse reaction rate con-
stant k−= κK2
B.
5


## Page 6


The bond graph approach is naturally allied to stoichiometric concepts (Klipp et al.,
2016; Palsson, 2006, 2011, 2015). In particular, the stoichiometric matrix N can be
automatically generated from the network represented in the system bond graph. N can
be used to give species ﬂows fx in terms of reaction ﬂows f and, conversely, reaction
aﬃnity A in terms of species potentials µ:
fx = N f
A = −NTµ
(2.8)
In the case of the system of Figure 1:
N =

−1
2
T
(2.9)
2.1. Modiﬁed mass action kinetics
Simpliﬁed representation of biomolecular system requires a representation of the
reaction network that approximates, but does not fully represent the complete set of bio-
chemical reactions. Physically-plausible models of biomolecular systems will there-
fore typically contain reactions which are an approximation to a sequence of elemen-
tary reactions. Thus even if elementary reaction steps have the mass action kinetics of
Equation (2.4), this would not necessarily be the case for the overall reactions used to
represent the system (see for example Atkins et al., 2018, chapter 17).
In bond graph terms, one may represent the dissipative reaction component with
any appropriate constitutive relation for the reaction ﬂow f in terms of the forward and
reverse aﬃnities: mass action, as given by (2.4) leading to (2.7) is one example. In
particular, non-elementary reactions may be represented using rate equations where,
unlike the mass-action formulation, the concentration exponents are not the stoichio-
metric coeﬃcients. One particular case of this would be to divide all of the stoichio-
metric coeﬃcients by an positive integer constant α in the rate equations. Thus, for
example, if α = 2, the reaction rate (2.7) corresponding to the reaction (2.1) would
become:
f = κ
 p
KAxA −KBxB

(2.10)
This corresponds to the non-integer stoichiometry
Nα =

−1
2
1
T
(2.11)
6


## Page 7


Note that in the context of modelling the Mitochondrial Electron Transport Chain, the
exponent 1/2, corresponding to α = 2, commonly appears in the ﬂux expression for
complex III, as given by Beard (2005, equation B72) and Beard and Qian (2010, equa-
tion 7.38) for example, and the exponent 1/4, corresponding to α = 4, appears in the
ﬂux expression for complex IV given by Beard (2005, equation B73) and Beard and
Qian (2010, equation 7.41). This can be achieved by replacing the mass-action formula
(2.4) by the modiﬁed mass-action (MMA) formula:
f = κ
 
exp A f
αRT −exp Ar
αRT
!
(2.12)
which contains the additional parameter α, which is used below as an essential part of
the model ﬁtting process.
For thermodynamic consistency, it is important that Equation (2.12) represents a
dissipative system; that is, any non zero ﬂow dissipates energy (Willems, 1972; Pold-
erman and Willems, 1997; Willems, 2007). With this in mind, it is now shown that the
MMA equation can be rewritten in mass-action form but with the positive constant κ
replaced by the positive function of concentration κα. As a simple example of this, it
can be veriﬁed that Equation (2.10) can be rewritten as
f = κα

KAxA −K2
Bx2
B

(2.13)
where κα(xA, xB) =
¯κ
√KAxA + KBxB
(2.14)
As xA and xB are positive, κα is also positive. Thus (2.13) corresponds to the mass-
action equation (2.4) with the positive constant κ replaced by the positive function of
concentration κα(xA, xB). The general modiﬁed-mass action kinetics of Equation (2.12)
can also be rewritten in mass-action form with the positive constant κ replaced by the
positive κα:
f = κα(A f , Ar)
 
exp Af
RT −exp Ar
RT
!
(2.15)
2.2. Redox reactions
Oxidative phosphorylation involves a series of electrochemical redox reactions.
Nicholls and Ferguson write that ‘Whereas all redox reactions can quite properly be
7


## Page 8


described in thermodynamic terms by their Gibbs energy changes, electrochemical pa-
rameters can be employed because the reactions involve the transfer of electrons.” (Nicholls
and Ferguson, 2013, chapter 3.3). Rather than to deal directly with conversion be-
tween electrical and chemical potentials and associated variables, it is convenient to
have a common system of units and convert the chemical energy covariables chem-
ical potential and molar ﬂow to equivalent electrical energy covariables voltage and
current (Gawthrop, 2017). The relevant conversion factor is Faraday’s constant F ≈
96 485 C mol−1 (Nicholls and Ferguson, 2013; Gawthrop et al., 2017; Gawthrop, 2017).
In particular, we deﬁne:
Faraday-equivalent potential
φ = µ
F (V)
(2.16)
Faraday-equivalent ﬂow
f = Fv (A)
(2.17)
Using these Faraday-equivalent variables, the Ce constitutive relations (2.2) and (2.3)
become:
φA = VN ln KAxA
(2.18)
φB = VN ln KBxB
(2.19)
where VN = RT
F ≈26 mV
(2.20)
and the modiﬁed mass-action formula (2.12) becomes:
f = κ
 
exp Af
αVN
−exp Ar
αVN
!
(2.21)
As noted by Nicholls and Ferguson, an advantage of transforming the chemical
potentials into equivalent electrical potentials in the treatment of redox reactions is:
“the ability to dissect the overall electron transfer into two half-reactions involving
the donation and acceptance of electrons, respectively.” (Nicholls and Ferguson, 2013,
chapter 3.3). For example, the two half-reactions:
A
r1
C + 2 e –
1
B + e –
2
r2
D
(2.22)
electron e –
1 donation in the ﬁrst (oxidation of A), and e –
2 acceptance in the second
(reduction of B), correspond to the overall reaction:
A + 2 B
r
C + 2 D
(2.23)
8


## Page 9


1
Ce:A
0
C:E
1
Ce:C
1
Ce:B
Re:r1
Re:r2
1
Ce:D
Figure 2: Bond Graph representation of two half-reactions: A
r1
C + 2 e– and B + e–
r2
D. As
in Figure 1, the bond graph components Ce:A, Ce:B, Ce:C and Ce:D represent species A, B, C and D; the
bond graph component Re:r1 represent the two half-reactions; the bonds ⇁together with the zero 0 and one
1 junctions deﬁne the stoichiometry. The component C:E represents the electrons of the half-reaction and is
related to the redox potentials. The corresponding voltage is V. As discussed in § 2.2, the bonds carry the
energy covariables electrical potential φ and and current v.
Figure 2 shows a bond graph representation of these two half-reactions (2.22), ex-
plicitly representing the transfer of electrons e– using the linear electrical capacitor
represented by C:E with voltage V; the two-electron stoichiometry of reaction r1 is
represented by the two parallel bonds. If reaction r1 is in equilibrium, then the voltage
V is exactly that required to stop reaction r1 from proceeding and thus V = −E1 where
E1 is the redox potential of reaction r1. Conversely, if reaction r2 is in equilibrium,
then the voltage V is exactly that require to stop reaction r2 from proceeding and thus
V = −E2 where E2 is the redox potential of reaction r2.
2.3. Hierarchical Modelling
Hierarchical modelling and modularity provide one approach to understanding the
complex systems associated with cellular biochemistry (Hartwell et al., 1999; Lauf-
fenburger, 2000; Csete and Doyle, 2002; Bruggeman et al., 2002, 2008; Szallasi et al.,
2010). Bond graphs provide an eﬀective foundation for modular construction of hierar-
chical models of biochemical systems (Gawthrop et al., 2015; Gawthrop and Crampin,
2016). Bond graphs model the interaction between modules, in particular retroactivity
(Jayanthi and Del Vecchio, 2011; Del Vecchio, 2013; Del Vecchio and Murray, 2014),
in a straightforward manner whilst retaining thermodynamic compliance.
Bond graph modules use the notion of chemostats (Polettini and Esposito, 2014;
Gawthrop and Crampin, 2016) which have an number of interpretations:
9


## Page 10


1. one or more species is ﬁxed to give a constant concentration; this implies that an
appropriate external ﬂow is applied to balance the internal ﬂow of the species.
2. as a Ce component with a ﬁxed state.
3. as a module port through which chemical, mechanical or electrical energy ﬂows.
Thus if the bond graph of Figure 2 were to be used as a module, then Ce:A, Ce:B, Ce:C
and Ce:D could be chemostats. If the module were to be examined in isolation, then
the interpretations of items 1 and 2 would be used; if, on the other hand, the module
were to be embedded in a larger system, then the interpretation of item 3 would be
used.
When examining the properties of a complex system, such as a whole cell model,
the replacement of some modules by physically-plausible equivalents with the same
ports would not only reduce computational complexity but also allow attention to be
focussed on detailed models of other modules.
2.4. Dynamical Simulation
Bond graphs, together with the component constitutive relationships, can be used
to automatically derive the ordinary diﬀerential equations (ODE) describing the system
dynamics (Karnopp et al., 2012). These ODEs can be in symbolic form or in the form
of computer code for a particular simulation engine. In general, a set of ODEs does
not guarantee thermodynamic consistency; but, because these ODEs are derived from
a bond graph, they inherit the thermodynamic properties of the bond graph.
In some systems, the system states are not independent; in particular, biomolecular
systems usually have conserved moieties. In such circumstances, the system bond
graph can be used to automatically generate the minimal number of ODEs describing
the independent states from which dependent states and reaction ﬂows can be derived
(Gawthrop and Crampin, 2014, § 3(c)).
Although in this paper we have focused on species described by the standard log-
arithmic constitutive relation (2.2) and reaction ﬂows determined by the mass action
formula (2.4), bond graph components can have a wide range of constitutive relations
constrained only by thermodynamics. A simple example of this is the modiﬁed mass-
action formula of equation (2.12); a more complex example is the Goldman-Hodgkin-
10


## Page 11


Katz ﬂux equation used in bond graph models of action potential (Gawthrop et al.,
2017). Moreover, models with complex characteristics, such as transporters, can be
built from simple bond graph components (Pan et al., 2019).
2.5. BondGraphTools – a Python Toolkit
Computational tools are necessary for model capture, parameterisation and simu-
lation. As the name suggests, BondGraphTools is an application programming in-
terface (API) for capturing, simplifying and simulating bond graph models, and is an
important part of the bond graph approach (Cudmore et al., 2019).
BondGraphTools is written in Python and is built upon the Scientiﬁc Python
(SciPy) libraries, all of which are open source and easily accessible. The core use-
case of BondGraphTools is to turn bond graphs into a set of reduced equations which
can be then passed into other SciPy libraries (parameter estimation routines, or ODE
integrators, for example). As model reduction is performed symbolically, the simpliﬁ-
cation routines are free from numerical errors, which is important for systems involving
parameters that are unknown.
3. A Simpliﬁed Physically-Plausible Model for the Mitochondrial Electron Trans-
port Chain
Mitochondria make use of redox reactions to provide the power driving many living
systems. The key process in the generation of ATP is chemiosmotic energy transduc-
tion, whereby a sequence of redox reactions pumps protons across the mitochondrial
inner membrane to generate the proton-motive force (PMF), an electrochemical gra-
dient which is then used to power the synthesis of ATP. Generation of the PMF is
accomplished by the mitochondrial electron transport chain. Beard and colleagues
have developed the most comprehensive thermodynamically consistent models of mi-
tochondrial oxidative phosphorylation including the electron transport chain (Beard,
2005; Wu et al., 2007; Bazil et al., 2016). Recently Gawthrop (2017) provided a bond
graph model of mitochondrial oxidative phosphorylation based on the redox reactions
associated with complexes CI, CIII and CIV of the mitochondrial electron transport
chain.
11


## Page 12


In contrast, here we develop a simple, but physically-plausible, model based on the
overall chemical reaction of the Electron Transport Chain in which 2 NADH is com-
bined with O2 and 2 H+ to give 2 NAD+ and 2 H2O; the 2 protons (2 H+) are consumed
from the mitochondrial matrix. The free energy of this overall reaction pumps 20 pro-
tons across the mitochondrial inner membrane. Denoting the protons in the mitochon-
drial matrix as H +
x and those in the mitochondrial inner membrane space as H +
i
the
overall reaction is thus:
2 NADH + O2 + 22 H +
x
2 NAD+ + 2 H2O + 20 H +
i
(3.1)
Reaction (3.1) can be rewritten as the weighted sum of three reactions:
NADH
r1
NAD+ + H +
x + 2 e –
1
(×2)
(3.2)
O2 + 4 H +
x + 4 e –
2
r2
2 H2O
(×1)
(3.3)
5 H +
x + e –
1
rloss
5 H +
i + e –
2
(×4)
(3.4)
where e –
1 and e –
2 are the electrons transfered from and to the left and right half re-
actions respectively as discussed in § 2.2.
Reaction (3.2) converts NADH to NAD
producing a proton H +
x in the mitochondrial matrix and donating two electrons e –
1 .
Reaction (3.3) converts O2 and protons H +
x in the mitochondrial matrix and consumes
four electrons e –
2 to produce water H2O. Reaction (3.4) transfers electrons e –
1 to e –
2 and,
in so doing, utilises the corresponding free energy to pump ﬁve protons from the mi-
tochondrial matrix H +
x to the mitochondrial inter-membrane space H +
i against the H+
concentration gradient and the trans-membrane electrical potential ∆Ψ.
Figure 3 shows the bond graph of a physically-plausible model of the mitochondrial
electron transport chain. The the components of the model are:
1. The electron donation reaction r1 (3.2) is represented by Re:r1 and the associated
species by Ce:NADH, Ce:NAD and Ce:Hx. The electrons e –
1 accumulate in the
electrical capacitor C:E1.
2. The electron consumption reaction r2 (3.3) is represented by Re:r2 and the asso-
ciated species by Ce:O2, Ce:H2O and Ce:Hx. The electrons e –
2 accumulate in
the electrical capacitor C:E2.
12


## Page 13


C:dV
R:r_loss
0
Ce:Hx
1
0
1
Re:r2
1
C:E2
C:E1
Ce:O2
1
Re:r1
0
Ce:H2O
0
1
Ce:NAD
Ce:NADH
Φr
2
f2
Φf
2
f2
Φf
1
f1
Φr
1
f1
f
f
V1
V2
∆V
V1
i1
V2
i2
f
Figure 3: Mitochondrial electron transport chain: a physically-plausible model. The reaction represented by
Re:r1 is the electron donating reaction (3.2) and the reaction represented by Re:r2 is the electron consuming
reaction (3.3). The dashed box demarcates the electrical part of the model: the electrical resistor R:r loss
models electrical energy dissipation; C:E1 and C:E2 are electrical capacitors accumulating donated and
consumed electrons. The electrical capacitor C:dV corresponds to the net voltage available to pump protons
across the mitochondrial inner membrane.
3. The electron transfer part of the electron transfer/proton pump (3.4) is modelled
by the two electrical capacitors C:E1 and C:E1 and the (linear) electrical resistor
(with resistance rloss) R:r loss. The voltage V1 associated with C:E1 is the redox
potential of half reaction (3.2) and the voltage V2 associated with C:E2 is the
redox potential of half reaction (3.3). The electrical capacitor C:dV with voltage
∆V represents by the the net redox potential minus the potential drop associated
with the resistor rloss:
∆V = V1 −V2 −rloss f
(3.5)
4. Proton transfer is not explicitly modelled in Fig. 3. However, the corresponding
membrane potential ∆Ψ is given in terms of ∆V as by:
∆Ψ = ∆V
np
−ΦH
(3.6)
where np =
20
4 = 5 is the number of protons pumped per electron and ΦH =
φHi −φHx, the chemical potential diﬀerence due to proton concentration diﬀer-
ence across the membrane.
13


## Page 14


Substance
ρ
φ⊖(V)
φ⊘(V)
H2O
1.000
−2.443
−2.443
H +
x
1.660 × 10−8
0.000
−4.217 × 10−1
NAD+
1.500 × 10−3
1.876 × 10−1
3.454 × 10−2
NADH
1.500 × 10−3
4.074 × 10−1
2.544 × 10−1
O2
2.500 × 10−5
1.700 × 10−1 −7.945 × 10−2
Table 1: Physical Parameters of the Physically-plausible model. x⊘is the concentration at nominal conditions
relative to standard conditions, φ⊖and φ⊘are the Faraday-equivalent potentials at standard and nominal
conditions related by Equation (3.8) and where ρ is given by Equation (3.9). H +
x are protons in the matrix.
3.1. Physical Parameters
The Ce constitutive relation (2.18) can be rewritten in the alternative form:
φA = φ⊖
A + VN ln xA
x⊖
A
(3.7)
where VN is given by (2.20) and φ⊖is the potential of substance A at standard con-
ditions where xA = x⊖
A. Using tables of standard chemical potentials µ⊖, equation
(2.16) can be used to derive the corresponding potential φ⊖. As discussed by Gawthrop
(2017), the Faraday-equivalent chemical potential of substance A at nominal conditions
φ⊘can be computed from Faraday-equivalent chemical potential at standard conditions
φ⊖from the formula:
φ⊘
A = φ⊖
A + VN ln ρA
(3.8)
where ρA = x⊘
A
x⊖
A
(3.9)
where x⊘
A and x⊖
A are the concentrations of substance A at nominal conditions and stan-
dard conditions. Table 1 shows nominal values φ⊘for a number of diﬀerent substances.
These values will be used below to model the mitochondrial electron transport chain.
The stoichiometric equations (2.8) can be rewritten in Faraday-equivalent form as
fx = N f
Φ = −NTφ
(3.10)
In the case of the half-reaction (3.2)
NADH
NAD+ + H +
x + 2 e –
1
(3.11)
14


## Page 15


the stoichiometric matrix is:
NT =

−1
1
1
2

(3.12)
It follows that the reaction potential Φ is:
Φ = NTφ = φ⊘
NADH −φ⊘
NAD −φ⊘
Hx −2φ⊘
E
(3.13)
At equilibrium, Φ = 0 and so:
V = φ⊘
E = 1
2

φ⊘
NADH −φ⊘
NAD −φ⊘
Hx

= 1
2 (254.4 −34.54 −(−421.7)) ≈320 mV
(3.14)
and so this corresponds to a redox potential of E = −V = −320 mV for this half-
reaction.
Similarly, in the case of the half-reaction (3.3)
O2 + 4 H +
x + 4 e –
2
2 H2O
(3.15)
the redox potential is E = −V = 780 mV.
3.2. An explicit formula
From a systems point of view, the model of the ETC can be characterised by the
voltage/current relationship of the bond graph component C:dV. This represents the
steady state relationship between the ﬂow (rate of electron transport along the ETC,
or equivalently the rate of oxygen consumption) and the mitochondrial membrane po-
tential which is established. Letting n1 and n2 be the number of bonds connecting
reactions r1 and r2 to the electrical subsystem, the steady-state ﬂows are related by:
f = n1 f1 = n2 f2
(3.16)
and the steady-state potentials by Equation (3.5) with:
V1 = 1
n1
Φ1
(3.17)
andV2 = 1
n2
Φ2
(3.18)
15


## Page 16


Using the modiﬁed mass action formula (2.21), the reaction ﬂows are given by
f1 = κ1
 
exp Φ f 1
αVN
−exp Φr1 + n1V1
αVN
!
(3.19)
f2 = κ2
 
exp Φf 2 + n2V2
αVN
−exp Φr2
αVN
!
(3.20)
where the parameter α remains to be determined (by ﬁtting to data). At equilibrium,
the ﬂows are zero and thus:
V1 = Veq
1 = 1
n1

Φf
1 −Φr
1

= 1
n1
Φ1
(3.21)
V2 = Veq
2 = 1
n2

Φr
2 −Φf
2

= −1
n2
Φ2
(3.22)
Writing ∆V1 = V1 −Veq
1 and ∆V2 = V2 −Veq
2 it follows that the ﬂows can be rewritten
as:
f1 = (1 −λ1)K1
f2 = (λ2 −1)K2
(3.23)
where
λ1 = exp n1∆V1
αVN
λ2 = exp n2∆V2
αVN
(3.24)
K1 = κ exp Φf 1
αVN
K2 = κ exp Φr2
αVN
(3.25)
Hence using (3.23)
λ1 = 1 −
f
n1K1
λ2 = 1 +
f
n2K2
(3.26)
Using (3.24) and (3.5)
∆V = ∆Veq + αVN
n1
ln
 
1 −
f
n1K1
!
−αVN
n2
ln
 
1 +
f
n2K2
!
−rloss f
(3.27)
where ∆Veq = Veq
1 −Veq
2 . Using the results of § 3.1
∆Veq = 320 + 780 = 1100 mV
(3.28)
This formula, derived from the simpliﬁed model using modiﬁed mass action, thus pro-
vides a voltage/current steady state relationship that describes the operation of the ETC.
Using equation (3.6) and a value of ΦH = 25 mV this corresponds to an equilibrium
mitochondrial membrane potential ∆Ψeq of: ∆Ψeq = 1100
5
−25 = 195 mV.
16


## Page 17


3.3. Model Fitting
The simpliﬁed, physically plausible model of the electron transport chain derived
above contains physical parameters which are known a-priori, as well as parameters
which are model-dependent and must be obtained by ﬁtting to relevant data. In particu-
lar, the explicit formula (3.27) relating ﬂow f to potential diﬀerence ∆V has four known
physical parameters: ∆Veq, VN, n1 and n2 and four unknown parameters: α, K1, K2 and
rloss. Bazil et al. (2016) develop a detailed physically based mathematical model of
mitochondrial oxidative phosphorylation and ROS generation and compare the results
with in-vitro experimental data. These results are used below to ﬁt the parameters of
the physically-plausible model developed above.
Figure 2B in Bazil et al.
shows four datasets: two sets of simulation results
corresponding to two concentrations of inorganic phosphate Pi: [Pi] = 1 mM and
[Pi] = 5 mM, and two sets of experimental data corresponding to these two condi-
tions. The maximum value for VO2 (Figure 2B in Bazil et al.) is 150 nmol/min/U CS.
This value is used to normalise the reported ﬂows for the purposes of parameter ﬁtting.
Thus in Figure 5, the mitochondrial membrane potential ∆Ψ mV is plotted against the
normalised rate of oxygen consumption f.
In ideal circumstances, the experimental
data would correspond to an isolated module where the species concentrations corre-
sponding to each chemostat in the model (see § 2.3) were constant. This is not the
case here as, for example, NADH is generated from the mitochondial TCA (citric acid)
cycle and so concentration of NADH depends on the ﬂow though the TCA cycle.
For the purposes of illustrating parameter ﬁtting in the context of physically-plausible
models, this lack of isolation is not included; but would be an interesting topic of future
research.
A further approximation is that inorganic phosphate Pi does not appear in the phys-
ically plausible model developed above and therefore it is not possible to take account
of the variation of Pi in this approximate model.
However, the experimental data
shown in Figure 2B of Bazil et al. does not show a strong dependence of this part
of the system on Pi and so the lack of dependence of our simpliﬁed model on Pi is
reasonable. For this reason, experimental data for both values of Pi are considered
for the purposes of model ﬁtting to the raw data. We note that other components of
17


## Page 18


2
4
6
8
10
K1
0.0
0.5
1.0
1.5
2.0
ϵ (mV)
sim-0
sim-1
exp
(a) K1
0
1
2
3
4
5
6
7
8
9
10 11 12
α
0
1
2
3
4
ϵ (mV)
sim-0
sim-1
exp
(b) α
Figure 4: Fitting K1 and α. (a) The RMS error ϵ as parameter K1 is varies; all other parameters are optimised.
The value of K1 is not important if greater than about 2; the reaction r1 is in equilibrium. (b) The RMS error
ϵ as parameter α of the modiﬁed mass-action kinetics (2.21) is varies; all other parameters are optimised.
For data sets sim-0 and sim-1 (data from the experimentally ﬁtted model of Bazil et al. (2016)) there is a
clear minimum at about α = 6.
mitochondrial metabolism not modelled here, such as ATPase, do depend strongly on
Pi.
Known physical parameters Φ⊖of Table 1 are drawn from the supplementary ma-
terial of Wu et al. (2007), the concentrations of NAD and NADH from Bazil et al.
(2016), the pH values from Porcelli et al. (2005) and the O2 concentration from Mur-
phy (2009). Parameter ﬁtting was implemented using the Python function within the
SciPy.optimize module opt.minimize with method = "L-BFGS-B" and parame-
ter bounds of 10−12 and ∞as the parameters are all positive. The cost function ϵ is the
root-mean-square (RMS) diﬀerence between the value of ∆Ψ predicted by equations
(3.6) and (3.27) and the data for each value of (normalised) ﬂow.
The form of the cost function was examined by ﬁxing one of the four parameters
and minimising with the other three and plotting the cost against the ﬁxed parameter.
Figure 4(a) shows the dependence of the cost function on parameters K1 and α, and
indicates that the parameter K1 has little eﬀect as long as it is greater than about K1 = 5.
For the rest of this paper, K1 was ﬁxed at a large positive value and not included further
in the optimisation. Thus there are three signiﬁcant parameters: α, K2 and rloss. Figure
4(b) shows that the parameter α has a signiﬁcant eﬀect. For the two simulation data
18


## Page 19


Source
α
K2
rloss (mΩ)
ϵ (mV)
sim0
5.8
1.8 × 10−3
3.1 × 101
9.2 × 10−3
sim1
5.9
4.6 × 10−3
4.6 × 101
8.6 × 10−2
exp
10.9
1.3 × 10−2
1.0 × 10−6
1.3
sim0
6.0
2.0 × 10−3
2.7 × 101
5.1 × 10−2
sim1
6.0
4.8 × 10−3
4.4 × 101
9.0 × 10−2
exp
6.0
4.4 × 10−3
5.6 × 101
1.7
Table 2: Optimal parameters. The table summarises the ﬁtting results using the two sets of simulation data
(sim0&sim1) and the experimental data (exp) from Bazil et al. (2016). Rows 1–3 correspond to free α and
the rows 4–6 to ﬁxed α = 6.
sets, there is a clear minimum at about α = 6. The rows 1–3 of Table 2 show the optimal
parameters α, K2 and rloss, together with the minimal cost ϵ for the two simulations
and the experimental data. Rows 4–6 correspond to ﬁxing α = 6 and estimating the
remaining two parameters K2 and rloss.
Finally, the current-voltage relationship derived above and given in (3.27) is plotted
in Figure 5 for diﬀerent sets of ﬁtted parameters given in Table 2, along with simulation
results from the full model of Bazil et al. (2016), and the corresponding experimental
data, showing that the explicit formula for the steady state current/voltage behaviour of
the ETC is well captured by the physically plausible model. Figures 5(a)–5(c) corre-
spond to rows 4–6 of Table 2; Figure 5(d) corresponds to row 3 of Table 2.
19


## Page 20


0.00
0.25
0.50
0.75
1.00
f (normalised)
160
170
180
190
∆Ψ (mV)
sim-0
sim-1
exp
p-p model
(a) Fit to sim0 (ﬁxed α = 6)
0.00
0.25
0.50
0.75
1.00
f (normalised)
160
170
180
190
∆Ψ (mV)
sim-0
sim-1
exp
p-p model
(b) Fit to sim1 (ﬁxed α = 6)
0.00
0.25
0.50
0.75
1.00
f (normalised)
160
170
180
190
∆Ψ (mV)
sim-0
sim-1
exp
p-p model
(c) Fit to exp (ﬁxed α = 6)
0.00
0.25
0.50
0.75
1.00
f (normalised)
160
170
180
190
∆Ψ (mV)
sim-0
sim-1
exp
p-p model
(d) Fit to exp (free α)
Figure 5: Model ﬁtting. All four plots show four data sets: sim-0 and sim-1 are simulation data from
the experimentally ﬁtted simulation of Bazil et al. (2016) for two values of [Pi]; exp is the corresponding
experimental data; pp-model is the simulation of the physically-plausible model using the formula of § 3.2.
(a) The physically-plausible model is ﬁtted to the experimentally ﬁtted simulation of Bazil et al. (2016) with
[Pi] = 1 mM using ﬁxed α = 6 and estimating K2 and rloss. See row 4 of Table 2. (b) As (a) but with
[Pi] = 5 mM. See row 5 of Table 2. (c) The physically-plausible model is ﬁtted to the experimental points
combining both values of Pi using ﬁxed α = 6 and estimating K2 and rloss, see row 6 of Table 2. (d) As (c)
except that α is also estimated, see row 3 of Table 2.
20


## Page 21


4. Discussion
Simpliﬁed models of biochemical and biophysical processes have a central role to
play in the development of large whole-cell and multi-scale Physiome models, and the
use of such models in biomedical and synthetic biology applications. Here we have
argued that such simpliﬁed models need to be physically plausible, in the sense that
they are consistent with the laws of physics (for example, that they obey mass conser-
vation, are consistent with thermodynamic principles, and so on) as well as providing
a suitable ﬁt to available data sets. We have demonstrated that energy-based modelling
using bond graphs provides a useful framework for the development of such models.
The advantages of thermodynamically-consistent modelling have been argued recently
by us and a number of other authors (Beard and Qian, 2010; Gawthrop and Crampin,
2014; Klipp et al., 2016; Gawthrop and Crampin, 2017; Mason and Covert, 2019). Key
amongst these advantages are that models comprised of physically-plausible compo-
nents are themselves physically plausible; that such models can be constructed and
assembled in a modular fashion; and that such models enforce thermodynamic prin-
ciples which allow identiﬁcation of conserved moieties and furthermore restrict the
possible parameter space. Here we have shown that by using a modiﬁed form of mass
action we can generate a simple physically-plausible model of the mitochondrial elec-
tron transport chain that is able to reproduce experimentally measured properties of the
system.
Bond graphs provide a framework within which is represented both the biochem-
ical network stoichiometry and the constitutive relationship between thermodynamic
driving force and biochemical reaction rate for each constituent bond graph element,
describing the mechanism of enzymatic processes and so forth. Therefore, bond graphs
describe the complete dynamical behaviour of the biochemical system, and can be used
to derive the ordinary diﬀerential equations describing full system dynamics. A par-
ticular advantage, however, of a simple model as derived here over a fully mechanistic
model is the possibility of deriving explicit formulae for key properties and behaviours
of the system. Here we have shown that using the physically plausible modelling ap-
proach we can derive an explicit algebraic formula for the ﬂux through the electron
21


## Page 22


transport chain to the PMF that is generated across the mitochondrial membrane at
steady state, given in equation (3.27). This is not in general possible from a full dy-
namical representation (whether represented as a bond graph or otherwise). This is of
signiﬁcance both as it drastically simpliﬁes the model, and also because it allows a di-
rect analysis of the dependence of the mitochondrial membrane potential on parameters
of the ETC ﬂux, as discussed below. Such a simpliﬁed but thermodynamically realistic
representation of mitochondrial energy production is particularly suitable to be used
in simulation of spatially-distributed networks of mitochondria (Jarosz et al., 2017;
Ghosh et al., 2018), for which detailed mechanistic It remains to be determined how
diﬀerent possible modiﬁcations to mass action, or indeed other constitutive relations
that may be used to relate chemical potential and reaction rate, aﬀect the ability of sim-
ple physically plausible models to represent complex biochemical processes. models
of mitochondrial bioenergetics have too high a computational overhead.
The physically plausible model of the electron transport chain derived above con-
tains physical parameters which are known a-priori, as well as parameters which are
model-dependent and therefore obtained by ﬁtting to relevant data. In particular, the
explicit formula (3.27) relating ﬂow f to potential diﬀerence ∆V has four known phys-
ical parameters: ∆Veq, VN, n1 and n2 and four unknown parameters: α, K1, K2 and
rloss. Using an optimization approach to model ﬁtting, we have shown that the value
of the parameter K1 appears unimportant, as long as K1 > 10; this corresponds to the
rate constant κ1 of reaction r1 being large enough so that there is negligible potential
drop across the reaction; in other words, this requires that the reaction (3.2) is operating
essentially at equilibrium under the experimental conditions considered.
In contrast, the α parameter of the modiﬁed mass-action equation (2.21) is found
to be important. Choosing α = 6 gives a good ﬁt for both the experimentally-ﬁtted
simulations and experimental data. This dependence is to be expected as the physically
plausible model subsumes a number of individual reactions and this is known to lead
to non-stoichiometric exponents (Atkins et al., 2018, chapter 17).
We have shown that despite it’s simplicity, the physically-plausible model ﬁts the
(complex) simulation data from Bazil et al. (2016) closely (RMS error ϵ ≪1 mV) for
both values of Pi and for free α and ﬁxed α = 6. Furthermore the experimental data
22


## Page 23


can be ﬁtted with the model with an error ϵ of about 2 mV.
Despite the success of the simpliﬁed, physically-plausible model of the electron
transport chain that we have developed here, it should be noted that there are choices
and trade-oﬀs inherent in the simpliﬁcation process. Therefore it is important that such
simpliﬁed models are analysed and used only in the appropriate context. Firstly, the
simpliﬁed model was generated using a speciﬁc form of modiﬁed mass action kinetics.
While motivated by existing literature and approaches for representing non-elemental
biochemical reaction steps, diﬀerent choices could have been made. It remains to be
determined how diﬀerent possible modiﬁcations to mass action, or indeed other con-
stitutive relations that may be used to relate chemical potential and reaction rate, aﬀect
the ability of simple physically plausible models to represent complex biochemical
processes.
Secondly, the simpliﬁed model was developed using data relevant to normal phys-
iological conditions.
Most signiﬁcantly, simplifying assumptions have been made
about the physiological regime in which the model operates, and hence perturbations
to species concentrations and speciﬁc enzymatic regulators outside of this regime are
not captured in the simpliﬁed model. Full mechanistic exploration of mitochondrial
dynamics under a broad range of perturbations and experimental data beyond those
used to ﬁt the simpliﬁed model should of course be pursued using the full bond graph
representation of mitochondrial bioenergetics.
Finally, because the physically-plausible model is energy based, any or all of the
Ce components can provide connections with energy-based models of other parts of
the mitochondria system such as the TCA cycle, ATPase and ROS generation. In bond
graph terminology, the Ce components become ports (Gawthrop and Crampin, 2018b)
with which to connect to other bond graph components representing other aspects of
mitochondrial biochemistry, for simulation and analysis of larger-scale models of mi-
tochondrial and cellular bioenergetics. In our future work we intend to exploit this
feature of bond graphs to investigate in larger models of mitochondrial function the
basis of ROS generation and damage.
23


## Page 24


Acknowledgements
PJG would like to thank the Melbourne School of Engineering for its support via
a Professorial Fellowship. This research was in part conducted and funded by the
Australian Research Council Centre of Excellence in Convergent Bio-Nano Science
and Technology (project number CE140100036). The authors would like to thank an
anonymous reviewer for pointing out an error in an early version of the manuscript and
suggesting a number of points of clariﬁcation.
References
Peter Atkins, Julio De Paula, and James Keeler. Atkins’ Physical Chemistry. Oxford
University Press, Oxford, 11th edition, 2018.
Jason N. Bazil, Daniel A. Beard, and Kalyan C. Vinnakota.
Catalytic cou-
pling of oxidative phosphorylation, ATP demand, and reactive oxygen species
generation.
Biophysical Journal, 110(4):962 – 971, 2016.
ISSN 0006-3495.
doi:10.1016/j.bpj.2015.09.036.
Daniel A Beard.
A biophysical model of the mitochondrial respiratory sys-
tem and oxidative phosphorylation.
PLoS Comput Biol, 1(4):e36, 09 2005.
doi:10.1371/journal.pcbi.0010036.
Daniel A. Beard. Biosimulation: Simulation of Living Systems. Cambridge University
Press, Cambridge, UK., 2012. ISBN 978-0-521-76823-8.
Daniel A Beard and Hong Qian. Chemical biophysics: quantitative analysis of cellular
systems. Cambridge University Press, 2010.
Wolfgang Borutzky. Bond graph methodology: development and analysis of multidis-
ciplinary dynamic system models. Springer, Berlin, 2010. ISBN 978-1-84882-881-0.
doi:10.1007/978-1-84882-882-7.
F.J. Bruggeman, J.L. Snoep, and H.V. Westerhoﬀ. Control, responses and modularity
of cellular regulatory networks: a control analysis perspective. Systems Biology, IET,
2(6):397–410, November 2008. ISSN 1751-8849. doi:10.1049/iet-syb:20070065.
24


## Page 25


Frank J. Bruggeman, Hans V. Westerhoﬀ, Jan B. Hoek, and Boris N. Kholodenko.
Modular response analysis of cellular regulatory networks. Journal of Theoretical
Biology, 218(4):507 – 520, 2002. ISSN 0022-5193. doi:10.1006/jtbi.2002.3096.
F. E. Cellier. Continuous system modelling. Springer-Verlag, New York, 1991.
E. J. Crampin, N. P. Smith, and P. J. Hunter. Multi-scale modelling and the IUPS
Physiome project. Journal of Molecular Histology, 35(7):707–714, 2004.
Marie E. Csete and John C. Doyle.
Reverse engineering of biological complexity.
Science, 295(5560):1664–1669, 2002. doi:10.1126/science.1069981.
Peter Cudmore, Peter J. Gawthrop, Michael Pan, and Edmund J. Crampin. Computer-
aided modelling of complex physical systems with BondGraphTools. Jun 2019.
Alexander P. S. Darlington,
Juhyun Kim,
Jose I. Jimenez,
and Declan G.
Bates. Dynamic allocation of orthogonal ribosomes facilitates uncoupling of co-
expressed genes.
Nature Communications, 9(1):695, 2018.
ISSN 2041-1723.
doi:10.1038/s41467-018-02898-6.
Domitilla Del Vecchio. A control theoretic framework for modular analysis and design
of biomolecular networks. Annual Reviews in Control, 37(2):333 – 345, 2013. ISSN
1367-5788. doi:10.1016/j.arcontrol.2013.09.011.
Domitilla Del Vecchio and Richard M Murray.
Biomolecular Feedback Systems.
Princeton University Press, 2014. ISBN 0691161534.
P. Gawthrop and E. J. Crampin. Bond graph representation of chemical reaction net-
works.
IEEE Transactions on NanoBioscience, 17(4):449–455, October 2018a.
ISSN 1536-1241. doi:10.1109/TNB.2018.2876391. Available at arXiv:1809.00449.
P. J. Gawthrop. Bond graph modeling of chemiosmotic biomolecular energy trans-
duction. IEEE Transactions on NanoBioscience, 16(3):177–188, April 2017. ISSN
1536-1241. doi:10.1109/TNB.2017.2674683. Available at arXiv:1611.04264.
25


## Page 26


P. J. Gawthrop and E. J. Crampin. Modular bond-graph modelling and analysis of
biomolecular systems. IET Systems Biology, 10(5):187–201, October 2016. ISSN
1751-8849. doi:10.1049/iet-syb.2015.0083. Available at arXiv:1511.06482.
P. J. Gawthrop and L. P. S. Smith. Metamodelling: Bond Graphs and Dynamic Systems.
Prentice Hall, Hemel Hempstead, Herts, England., 1996. ISBN 0-13-489824-9.
P. J. Gawthrop, I. Siekmann, T. Kameneva, S. Saha, M. R. Ibbotson, and E. J. Crampin.
Bond graph modelling of chemoelectrical energy transduction. IET Systems Biology,
11(5):127–138, 2017. ISSN 1751-8849. doi:10.1049/iet-syb.2017.0006. Available
at arXiv:1512.00956.
Peter J Gawthrop.
Physically-plausible models for identiﬁcation.
In Proceedings
of the 2003 International Conference On Bond Graph Modeling and Simulation
(ICBGM’03), Simulation Series, pages 59–64, Orlando, Florida, U.S.A., January
2003. Society for Computer Simulation.
Peter J Gawthrop and Geraint P Bevan. Bond-graph modeling: A tutorial introduction
for control engineers. IEEE Control Systems Magazine, 27(2):24–45, April 2007.
doi:10.1109/MCS.2007.338279.
Peter J. Gawthrop and Edmund J. Crampin. Energy-based analysis of biochemical
cycles using bond graphs. Proceedings of the Royal Society A: Mathematical, Phys-
ical and Engineering Science, 470(2171):1–25, 2014. doi:10.1098/rspa.2014.0459.
Available at arXiv:1406.2447.
Peter J. Gawthrop and Edmund J. Crampin.
Energy-based analysis of biomolec-
ular pathways.
Proceedings of the Royal Society of London A: Mathemati-
cal, Physical and Engineering Sciences, 473(2202), 2017.
ISSN 1364-5021.
doi:10.1098/rspa.2016.0825. Available at arXiv:1611.02332.
Peter J. Gawthrop and Edmund J. Crampin.
Biomolecular system energetics.
In Proceedings of the 13th International Conference on Bond Graph Modeling
(ICBGM’18), Bordeaux, 2018b. Society for Computer Simulation.
Available at
arXiv:1803.09231.
26


## Page 27


Peter J. Gawthrop, Joseph Cursons, and Edmund J. Crampin. Hierarchical bond graph
modelling of biochemical networks. Proceedings of the Royal Society A: Mathemat-
ical, Physical and Engineering Sciences, 471(2184):1–23, 2015. ISSN 1364-5021.
doi:10.1098/rspa.2015.0642. Available at arXiv:1503.01814.
Shouryadipta Ghosh, Kenneth Tran, Edmund Crampin, Eric Hanssen, and Vijay Ra-
jagopal. Creatine-kinase shuttle and rapid mitochondrial membrane potential con-
ductivity are needed simultaneously to maintain uniform metabolite distributions in
the cardiac cell contraction cycle. Biophysical Journal, 114(3, Supplement 1):550a,
2018. ISSN 0006-3495. doi:10.1016/j.bpj.2017.11.3004.
Leland H Hartwell, John J Hopﬁeld, Stanislas Leibler, and Andrew W Murray. From
molecular to modular cell biology. Nature, 402:C47–C52, 1999.
Peter Hunter. The virtual physiological human: The physiome project aims to develop
reproducible, multiscale models for clinical practice. IEEE Pulse, 7(4):36–42, July
2016. ISSN 2154-2287. doi:10.1109/MPUL.2016.2563841.
Jan Jarosz, Shouryadipta Ghosh, Lea M. D. Delbridge, Amorita Petzer, Anthony J. R.
Hickey, Edmund J. Crampin, Eric Hanssen, and Vijay Rajagopal. Changes in mi-
tochondrial morphology and organization can enhance energy supply from mito-
chondrial oxidative phosphorylation in diabetic cardiomyopathy. American Jour-
nal of Physiology - Cell Physiology, 312(2):C190–C197, 2017. ISSN 0363-6143.
doi:10.1152/ajpcell.00298.2016.
S. Jayanthi and Domitilla Del Vecchio. Retroactivity attenuation in bio-molecular sys-
tems based on timescale separation. Automatic Control, IEEE Transactions on, 56
(4):748–761, April 2011. ISSN 0018-9286. doi:10.1109/TAC.2010.2069631.
Dean C Karnopp, Donald L Margolis, and Ronald C Rosenberg. System Dynamics:
Modeling, Simulation, and Control of Mechatronic Systems. John Wiley & Sons,
5th edition, 2012. ISBN 978-0470889084.
Jonathan R. Karr, Jayodita C. Sanghvi, Derek N. Macklin, Miriam V. Gutschow,
Jared M. Jacobs, Benjamin Bolival Jr., Nacyra Assad-Garcia, John I. Glass,
27


## Page 28


and Markus W. Covert.
A whole-cell computational model predicts phe-
notype from genotype.
Cell, 150(2):389 – 401, 2012.
ISSN 0092-8674.
doi:10.1016/j.cell.2012.05.044.
Edda Klipp, Wolfram Liebermeister, Christoph Wierling, and Axel Kowald. Systems
biology: a textbook. Wiley-VCH, Weinheim, Germany, 2nd edition, 2016.
Douglas A. Lauﬀenburger. Cell signaling pathways as control modules: Complexity
for simplicity?
Proceedings of the National Academy of Sciences, 97(10):5031–
5033, 2000. doi:10.1073/pnas.97.10.5031.
Derek N Macklin, Nicholas A Ruggero, and Markus W Covert. The future of whole-
cell modeling. Current Opinion in Biotechnology, 28(0):111 – 115, 2014. ISSN
0958-1669. doi:10.1016/j.copbio.2014.01.012.
John C. Mason and Markus W. Covert.
An energetic reformulation of ki-
netic rate laws enables scalable parameter estimation for biochemical net-
works.
Journal of Theoretical Biology,
461:145 – 156,
2019.
ISSN
0022-5193.
doi:https://doi.org/10.1016/j.jtbi.2018.10.041.
URL http://www.
sciencedirect.com/science/article/pii/S002251931830523X.
Peter Mitchell.
Coupling of phosphorylation to electron and hydrogen transfer
by a chemi-osmotic type of mechanism.
Nature, 191(4784):144–148, Jul 1961.
doi:10.1038/191144a0.
Peter Mitchell.
Possible molecular mechanisms of the protonmotive function of
cytochrome systems.
Journal of Theoretical Biology, 62(2):327–367, 1976.
doi:10.1016/0022-5193(76)90124-7.
Peter Mitchell. David Keilin’s Respiratory Chain Concept and its Chemiosmotic Con-
sequences. In Tore Fr¨angsmyr and Sture Fors´en, editors, Nobel Lectures in Chem-
istry, 1971-1980. World Scientiﬁc, Singapore, 1993. ISBN 981-02-0786-7.
Peter Mitchell. Chemiosmotic coupling in oxidative and photosynthetic phosphoryla-
tion. Biochimica et Biophysica Acta (BBA) - Bioenergetics, 1807(12):1507 – 1538,
28


## Page 29


2011. ISSN 0005-2728. doi:10.1016/j.bbabio.2011.09.018. Special Section: Peter
Mitchell - 50th anniversary of the chemiosmotic theory.
Michael P. Murphy. How mitochondria produce reactive oxygen species. Biochemical
Journal, 417(1):1–13, 2009. ISSN 0264-6021. doi:10.1042/BJ20081386.
Maxwell L. Neal, Michael T. Cooling, Lucian P. Smith, Christopher T. Thompson, Her-
bert M. Sauro, Brian E. Carlson, Daniel L. Cook, and John H. Gennari. A reappraisal
of how to build modular, reusable models of biological systems. PLoS Comput Biol,
10(10):e1003849, 10 2014. doi:10.1371/journal.pcbi.1003849.
David G Nicholls and Stuart Ferguson. Bioenergetics 4. Academic Press, Amsterdam,
2013.
David Nickerson, Koray Atalag, Bernard de Bono, J¨org Geiger, Carole Goble, Su-
sanne Hollmann, Joachim Lonien, Wolfgang M¨uller, Babette Regierer, Natalie J.
Stanford, Martin Golebiewski, and Peter Hunter.
The human physiome: how
standards, software and innovative service infrastructures are providing the build-
ing blocks to make it achievable. Interface Focus, 6(2), 2016. ISSN 2042-8898.
doi:10.1098/rsfs.2015.0103.
George Oster, Alan Perelson, and Aharon Katchalsky. Network thermodynamics. Na-
ture, 234:393–399, December 1971. doi:10.1038/234393a0.
George F. Oster, Alan S. Perelson, and Aharon Katchalsky. Network thermodynamics:
dynamic modelling of biophysical systems. Quarterly Reviews of Biophysics, 6(01):
1–134, 1973. doi:10.1017/S0033583500000081.
Bernhard Palsson. Systems biology: properties of reconstructed networks. Cambridge
University Press, 2006. ISBN 0521859034.
Bernhard Palsson. Systems Biology: Simulation of Dynamic Network States. Cam-
bridge University Press, 2011.
Bernhard Palsson. Systems Biology: Constraint-Based Reconstruction and Analysis.
Cambridge University Press, Cambridge, 2015.
29


## Page 30


Michael Pan, Peter J. Gawthrop, Kenneth Tran, Joseph Cursons, and Edmund J.
Crampin. Bond graph modelling of the cardiac action potential: implications for
drift and non-unique steady states. Proceedings of the Royal Society of London A:
Mathematical, Physical and Engineering Sciences, 474(2214), 2018. ISSN 1364-
5021. doi:10.1098/rspa.2018.0106. Available at arXiv:1802.04548.
Michael Pan,
Peter J. Gawthrop,
Kenneth Tran,
Joseph Cursons,
and Ed-
mund J. Crampin. A thermodynamic framework for modelling membrane trans-
porters.
Journal of Theoretical Biology, 481:10 – 23, 2019.
ISSN 0022-5193.
doi:10.1016/j.jtbi.2018.09.034. Available at arXiv:1806.04341.
H. M. Paynter. Analysis and design of engineering systems. MIT Press, Cambridge,
Mass., 1961.
Jan Willem Polderman and Jan C. Willems. Introduction to Mathematical System The-
ory: A Behavioral Approach. Number 26 in Texts in Applied Mathematics. Springer,
1997.
Matteo Polettini and Massimiliano Esposito.
Irreversible thermodynamics of open
chemical networks. I. Emergent cycles and broken conservation laws. The Journal
of Chemical Physics, 141(2):024117, 2014. doi:10.1063/1.4886396.
Anna Maria Porcelli, Anna Ghelli, Claudia Zanna, Paolo Pinton, Rosario Riz-
zuto, and Michela Rugolo.
pH diﬀerence across the outer mitochondrial mem-
brane measured with a green ﬂuorescent protein mutant.
Biochemical and Bio-
physical Research Communications, 326(4):799 – 804, 2005. ISSN 0006-291X.
doi:10.1016/j.bbrc.2004.11.105.
Matthew Scott, Stefan Klumpp, Eduard M Mateescu, and Terence Hwa. Emergence
of robust growth laws from optimal regulation of ribosome synthesis. Molecular
Systems Biology, 10(8):747, 2014. doi:10.15252/msb.20145379.
Z. Szallasi, V. Periwal, and Jorg Stelling. On modules and modularity. In Z. Szallasi,
J. Stelling, and V. Periwal, editors, System Modeling in Cellular Biology: From
Concepts to Nuts and Bolts, pages 19–40. MIT press, 2010.
30


## Page 31


Andrea Y. Weiße, Diego A. Oyarz´un, Vincent Danos, and Peter S. Swain. Mechanis-
tic links between cellular trade-oﬀs, gene expression, and growth. Proceedings of
the National Academy of Sciences, 112(9):E1038–E1047, 2015. ISSN 0027-8424.
doi:10.1073/pnas.1416533112.
J. C. Willems. Dissipative dynamical systems, part I: General theory, part II: Linear
system with quadratic supply rates. Arch. Rational Mechanics and Analysis, 45(5):
321–392, 1972.
J. C. Willems.
The behavioral approach to open and interconnected sys-
tems.
IEEE Control Systems, 27(6):46–99, Dec 2007.
ISSN 1066-033X.
doi:10.1109/MCS.2007.906923.
Fan Wu, Feng Yang, Kalyan C. Vinnakota, and Daniel A. Beard. Computer model-
ing of mitochondrial tricarboxylic acid cycle, oxidative phosphorylation, metabolite
transport, and electrophysiology. Journal of Biological Chemistry, 282(34):24525–
24537, 2007. doi:10.1074/jbc.M701024200.
31

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
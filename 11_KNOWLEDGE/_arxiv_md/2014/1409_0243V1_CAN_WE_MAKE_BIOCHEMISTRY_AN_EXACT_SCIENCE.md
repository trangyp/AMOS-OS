---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1409.0243v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1409.0243v1_Can_we_make_biochemistry_an_exact_science_

> Source: 1409.0243v1_Can_we_make_biochemistry_an_exact_science_.pdf

> Pages: 14

---


## Page 1


Shouldn’t we make biochemistry an exact science? 
 
August 31, 2014 
 
 
 
Bob Eisenberg 
Department of Molecular Biophysics and Physiology 
Rush University Medical Center 
Chicago IL 
60612 
 
Email Address: beisenbe@rush.edu 
 
 
 
This is a documented, expanded version of a paper with a similar title scheduled for publication in the  
October 2014  
issue of  
 
ASBMB Today 
 http://www.asbmb.org/asbmbtoday 
Editor: Angela Hopp 
Chair of Advisory Board: Charlie Brenner 
 
 
a journal of the 
American Society for Biochemistry and Molecular Biology 
http://www.asbmb.org


## Page 2


August 31, 2014 
 
2 
 
Exact science is useful. The physics of X-rays is exact. Biochemists can trust X-ray 
crystallography because the equations of X-rays are exact. But we rarely trust the 
equations that describe our own experiments and that is for good reason. The equations 
fail so often. 
Biochemists know that the law of mass action we use every day is not exact. The rate 
constants of that law change as conditions change. When we try to use that law, we 
must change parameters, but we do not know how. The law of mass action is not exact 
and not very useful because we cannot transfer it—parameters unchanged—from one 
set of conditions to another. This fact is known to every enzymologist who measures 
rate constants, but sad to say, other scientists often are not aware of this reality. 
High resolution calculations do not guarantee useful results 
Biochemists have tried to make their theories exact by increasing resolution. Our 
models of enzymes include thousands of atoms in cathedrals of structure. The hope has 
been that computing all the atoms of those cathedrals would produce exact 
simulations, if not exact equations. But, as the calculations of molecular dynamics 
reach from atomic to biological scales, we face disappointment once again. Issues of 
scale in time, space, and concentration must be dealt with all at once, in one calibrated 
calculation [13]. Enormous resolution does not guarantee useful biological results.[13, 
46, 53]  
We know very well that most enzyme reactions are controlled biologically by trace 
concentrations, 10−8 to 10−6 M, of ions like Ca2+. All atom simulations are not large 
enough, however, to deal with the 55 M water that dissolves each calcium ion in a 10−8 
to 10−6 M solution. The atomic resolution of simulations will have limited use if we 
cannot deal with the trace concentrations that control enzymes in health and disease. 
Force fields of molecular dynamics: boundary charges 
Molecular dynamics almost always uses force fields that depend on the coordinates of 
only two atoms at a time, calibrated at infinite dilution, i.e., in distilled water. But no 
two body force field can deal with electric charges that depend on the location of all 
charges in the system, like polarization charges at the boundaries of systems or at 
interfaces within the system. The electric force field is defined by the Poisson 
equation. Dependence on the location of all charges, including boundary charges, is 
displayed explicitly in the general solution of Poisson’s equation, see Jackson [32], 
Section 1.10, specifically eq. (1.36) and eq. (1.42). Boundary charges cannot be 
neglected in biological problems because they include polarization charges near lipid 
membranes. Charge at lipid membranes defines the electrical potential of cells and is 
responsible for the electrical function of nerve and muscle, and all other cells, for that 
matter. Neglecting boundary charges in force fields means ignoring electrical 
properties of cells.


## Page 3


August 31, 2014 
 
3 
 
Polarization force fields that ignore macroscopic boundary charges — no matter how 
sophisticated their derivation from quantum theory — cannot deal with the natural 
function of nerve cells as long as they depend on the coordinates of only two atoms at 
a time. 
Force fields of molecular dynamics: calibration 
Molecular dynamics uses force fields almost always calibrated at infinite dilution, in 
distilled water. That may be reasonable for the atoms inside a protein, away from 
mobile ions, but such a calibration must fail, in my view, for side chains of a protein 
that mix with mobile ions or for the mobile ions near and around proteins in bulk 
solution. When mobile ions are involved, screening/shielding is involved, as a general 
principle of physics.[8] Screening always depends on the concentration of ions, and (in 
nonideal cases) depends on the size and type of ions as well because ‘everything’ 
interacts with everything else in non-ideal solutions.[15, 16] Thus, force fields 
calibrated in distilled water will fail when dealing with concentrated solutions derived 
from seawater.  
Seawater and the solutions of biological systems are nothing like distilled water. In 
fact, distilled water is lethal for nearly all cells and most proteins. Molecular dynamics 
computed with force fields calibrated in distilled water will have certain errors when 
computing proteins in physiological solutions. 
Exact equations must use the mathematics of multiscale interactions, not the 
mathematics of ideal solutions  
Biology occurs in modified seawater and changes in ion concentration change the 
reactions of most enzymes. An exact version of biochemistry must deal with ions. 
I argue here that exact equations have not been possible because interactions in salt 
solutions that require multiscale analysis. Many types of interactions occur in ionic 
mixtures like seawater. All the ions in seawater are linked globally by electrostatic 
forces in flow, as we shall see later. Many are linked by steric interactions as well. 
Some are linked by orbital delocalization of electrons shared with water or other 
molecules, i.e., chemical bonds.  
Exact theories in biochemistry must use the mathematics of interactions but that 
mathematics is not widely known because it has only recently been discovered. 
Interactions are not small effects  
Most biological ionic solutions, like seawater, are far too concentrated to behave like 
ideal fluids or electrolyte. They are, in fact, complex (not simple) fluids.[15, 16] 
The free energy per mole (the experimental quantity called the activity of an ion, 
extensively measured in the literature [37, 39, 51, 71]) is the simplest property of an 
electrolyte. It is important to emphasize that activity is an experimental measurement


## Page 4


August 31, 2014 
 
4 
 
not a theoretical construct. Physical chemists for many decades measured the activity 
of electrolyte solutions of a wide range of composition and concentration and showed 
that different methods gave similar results.[1, 10, 26, 29, 37, 52, 54, 71] 
Activity plays a role something like height in a gravitational field and voltage in an 
electric circuit. In seawater, the activity of the bio-ions Na+, K+, Cl− and Ca2+ does not 
vary linearly with concentration (as in an ideal fluid) or even with the square root of 
concentration (as in extremely dilute solutions of NaCl).[21, 38-40]  
Interactions and non-ideality are not small effects in mixed ionic solutions like 
seawater. Interactions and non-ideality can dominate in biological systems, because 
ions are highly concentrated where they are most important, in and near active sites 
[35], ion channels, binding proteins and nucleic acids, near the ‘working’ electrodes of 
electrochemical cells, at charged boundaries in general. There, concentrations are often 
more than 5 molal and solution properties there are dominated by interactions.[15, 16] 
The activity of one ion depends on the individual concentration of every other ion. 
‘Everything’ interacts with everything else. Some of the interactions, usually called 
‘allosteric’ and attributed to enzymes and proteins, as structural or ensemble properties 
[7, 11, 28, 49], may in fact arise in the highly concentrated solutions in and near active 
sites of proteins. 
Mathematics of interactions 
The mathematics of interactions has been understood for a very long time when the 
systems involved are conservative and do not involve friction. Hamiltonians and 
variational calculus are the language of high-energy physicists when they build their 
bright X-ray sources.  
Hamiltonians have not been used in most biological systems because biology occurs in 
condensed phases where friction is always present. Until recently, no one knew how to 
use Hamiltonians in systems with friction. Friction accompanies all ionic movement 
and conformation changes in biology because atomic collisions occur on a 10-16 sec 
time scale in solutions containing little empty space— that is why solutions are called 
‘condensed phases’ — and only three or four collisions are enough to convert 
deterministic motion into the random motion we call heat.[6] 
Theory of complex fluids 
Recently, mathematicians have developed a theory of complex fluids that generalizes 
Hamiltonians into an energetic variational calculus dealing with friction. The theory 
has had striking successes. 
Variational methods deal successfully with liquid crystals, polymeric fluids, colloids, 
suspensions and electrorheological fluids.[4, 5, 31, 58, 69, 70]. Variational methods 
describe solid balls in liquids; deformable electrolyte droplets that fission and fuse [55,


## Page 5


August 31, 2014 
 
5 
 
69]; and suspensions of ellipsoids, including the interfacial properties of these complex 
mixtures, such as surface tension and the Marangoni effects of ‘oil on water’ and ‘tears 
of wine’.[25, 64, 69, 70] Variational methods allow the reformulation and 
understanding of problems involving interactions of considerable complexity [18, 65, 
67, 68], some of which have resisted analysis for a long time. It is a little early to say 
the theory of complex fluids provides exact equations in general, but the theory 
certainly provides a productive pathway towards that goal.  
The perspective offered by the variational calculus — see the tutorial presentations 
based on the lectures of Chun Liu [18, 24, 66] — is striking even if its results are 
immature. Complex fluids must be analyzed by variational methods because 
everything interacts with everything else. If those interactions are not addressed with 
mathematics, the interactions are bewildering and the results cannot be analyzed. A 
mathematics designed to handle interactions is needed to produce exact equations. 
Otherwise, interactions vary in so many ways that fixed parameters cannot deal with 
them [34, 37, 41, 50, 57, 71], even at infinite dilution.[30] 
Flow of charge requires global interactions and correlations 
The flow of charge at one location interacts with the flow everywhere else. Kirchoff’s 
current law ensures correlation of charge movement everywhere, with a correlation 
coefficient something like 0.999 999 999 999 999 999. The correlations produced by 
Kirchoff’s current law are global. Changes in flow at distant locations changes the 
flow everywhere.  
Just consider what happens when you ‘pull the plug’ on an electronic device. Flow of 
charge into the plug ceases and atomic scale flows stop in the junctions and boundary 
layers of transistors. Flow on atomic scale is controlled by flows from the plug meters 
away. The electronic device depends on flow. The vital functions of our computers die 
without flow from the plug. 
Life at equilibrium is usually death 
Life also depends on flow. Flow must be dealt with consistently in biochemistry, 
because life does not occur without flow. Life at equilibrium is usually death. Flows of 
electricity are accompanied by charge imbalances that can produce large effects 
throughout a system. The equations of electricity are sensitive. 
The equations of electricity are global, like Kirchoff’s current law. The electric field in 
ionic solutions of living systems links everything with everything else. Exact equations 
must be consistent equations in which all the variables satisfy all the equations and 
boundary conditions in all conditions.[19, 20]  
.


## Page 6


August 31, 2014 
 
6 
 
An exact version of biochemistry must satisfy the equations of electricity, 
including global correlations of Kirchoff’s current law 
The electrical forces and potentials must be computed from all charges present and 
their flows — in solution, in proteins and nucleic acids and macromolecules in 
general, in layers near lipid membranes and boundaries — because those electric 
forces can change qualitatively and quantitatively when net charge changes a little bit, 
anywhere. See the unforgettable third paragraph (p.1-1 of [23]) of “Feynman’s 
Lectures…, Mainly Electromagnetism…”) that describes how a tiny imbalance of 
charge is enough to lift “the entire earth.” 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Charge is an Abstraction, with different physics in different systems 
 
Continuity of Current is Exact, no matter what carries current!


## Page 7


August 31, 2014 
 
7 
 
Charge is an abstraction: the physical nature of current is diverse  
The global dependence of the electric field is glimpsed in the cartoons of Kirchoff’s 
current law used in computational electronics. Kirchoff’s law and Maxwell’s exact 
equations of electricity are inseparable.[2, 3, 27] Charge is the central subject of 
Maxwell’s theory. Kirchoff’s current law is really a statement of conservation of 
charge, including displacement charge, the abstraction and discovery of Maxwell that 
is his key contribution to understanding electromagnetic radiation, including light.  
Charge is abstract. Charge changes physical nature as it flows through a circuit (see 
figure). It is ions in salt water; it is electrons in a vacuum tube; it is quasi-particles in a 
semiconductor; it is diverse in batteries–because of complex electrochemical reactions 
at electrodes; and it is nothing much in a vacuum capacitor (i.e., displacement current 
[27, 32]).  
The flow of current is exactly the same in every element in a series circuit, although 
the physical nature of that current is strikingly diverse. 
Mass Action is about mass conservation, not charge  
Most of biochemistry describes flow by the law of mass action. The law of mass action 
is about mass conservation. It is not about charge conservation. The laws of electricity 
guarantee that the current will be the same for all reactions in series. The law of mass 
action does not.  
The global nature of electric flow prevents the law of mass action from being exact. 
The law of mass action — with rate constants that are constant — does not know about 
charge. Its rate constants do not depend on charge in a way that guarantees Kirchoff’s 
current law. (If you want to prove this for yourself, write the mass action equations for 
flux in different reactions and try to derive Kirchoff’s current law as we do in the 
equation inset below.) 
I believe the law of mass action must be consistent with Kirchoff’s current law if 
biochemistry is to be an exact science. 
How do we make changes? 
How can we fix this problem and make biochemistry an exact science? How can we 
remake our laws so they deal well with interacting systems and electric charge? I do 
not know a general answer, but I know where to look for help.  
Physicists for years have used consistent analysis of flow and diffusion of charges to 
design transistors for devices.[22, 33, 44, 47, 56, 59-63] Those devices have increased 
in capability by billions in the 55 years since 1959 — more precisely by 1.555 = 4.8 × 
109 [45, 48] — and that striking success may have something to do with the exact laws 
that those devices follow.


## Page 8


August 31, 2014 
 
8 
 
I believe biochemistry can add to its own substantial successes of the past 60 years by 
trying to make its laws exact. If global spatial dependence on the electric field is built 
into a new version of the law of mass action, along with the interactions found in 
nonideal solutions, we surely will do better than we have done in understanding how 
enzymes, channels and nucleic acids do their work. 
Consistent treatments will not be easy 
Giving up inconsistent treatments will be like giving up part of our intellectual 
heritage. We can no longer take the easy ways out. We can no longer look the other 
way when rate constants vary.  
When studying allosteric interactions, we must use activities, that account for 
interactions among ions, not concentrations, which are appropriate only for ideal 
infinitely dilute solutions, because reactants and products are usually concentrated near 
active and allosteric sites.  
We must learn to deal with fluctuating electric fields in our treatments of Brownian 
motion of ions so that results will not seem so anomalous.[12, 17] We can no longer 
compute fluctuating concentrations of charge and assume electric fields do not 
fluctuate. 
We must incorporate boundary conditions and finite size ions into the law of mass 
action. Algebra and ordinary differential equations must give way to field theories, 
partial differential equations and variational calculus.[18, 24, 66] 
We have begun that process for rate models of ionic channels [14] as I grew out of my 
original prejudice against such models.[9] (Stochastic analysis was responsible for that 
growth, more than anything else, reviewed in [14]. Applications to conduction in 
calcium channels are in [36, 43]. A specific example showing important consequences 
of long range coupling is in [42] but even there the work has just begun.)  
We must even incorporate spatial inhomogeneities and electric fields into our 
treatments of covalent chemical reactions in ionic solution, because those spatial 
inhomogeneities are likely to produce very large local concentrations lasting long 
enough so many reactions occur at concentrations quite different from the average 
reactions in a spatially uniform system.  
We cannot just calculate models with higher and higher resolution. We must calibrate 
our simulations.[46, 53] We must compute consistently with the electric field, on all 
scales, with theories appropriate for each scale.[13]  
Mathematics is now available 
Mathematics is finally available to deal with diffusion and electric fields in a 
consistent way, and the theory of complex fluids and simulations of computational 
electronics have shown that mathematics can describe complex fluids and devices 
(nearly) exactly. Now let’s try that mathematics on the classical problems of 
biochemistry to see if we can construct a consistent theory of reactions that is exact 
and useful.


## Page 9


August 31, 2014 
 
9 
Analysis  
 
Consider the nonequilibrium situation, for a reaction where reactants and products are at 
different locations  
 
*
*
f
f
b
b
k
k
k
k
X
Y
Z








 
(1) 
The flux of reactants (in a unit cross sectional area) is 
 




*
*
;
XY
f
b
YZ
f
b
J
k
X
k
Y
J
k
Y
k
Z




  
(2) 
where forward and backward rate constants are defined by subscripts with an asterisk for the 
right hand reaction, and brackets  denote number density, i.e., concentration. 
The flow of electric charge (in a unit cross sectional area) is current given by 
 




*
*
;
XY
X
f
Y
b
YZ
Y
f
Z
b
I
Fz
k
X
Fz
k
Y
I
Fz
k
Y
Fz
k
Z








  
(3) 
where F  is Faraday’s constant; 
, 
,
X
Y
Z
z
z
z  are the charges on one molecule of the reactants 
and products. These currents are obviously not always equal even though Kirchoff’s current 
law says they must be equal under all conditions. Algebra shows they can be equal only under 
special conditions: 
 





*
*
if and only if
XY
YZ
X
f
Y
b
Y
f
Z
b
I
I
z k
X
z k
Y
z k
Y
z k
Z




?
?
  
(4) 
Of course, experiments can be done under conditions that approximate the special condition 
of eq. (4), Then the law of mass action and Kirchoff’s current law will be in approximate 
agreement under those conditions.  
It may be possible to find a functional for rate constants which reconciles mass action with 
the electric field, but of course that functional must include ions throughout the system, as 
well as interactions of all sorts including with distant induced charge on lipid membranes and 
other boundaries.  
We seek a global version of mass action that automatically satisfies Kirchoff’s current law 
under all conditions.


## Page 10


August 31, 2014 
 
10 
 
 
 
 
Acknowledgement 
 
This is a documented, expanded version of a paper with a similar title scheduled for 
publication in the October 2014 issue of ASBMB Today, Editor: Angela Hopp. Chair of 
Editorial Advisory Board: Charlie Brenner. http://www.asbmb.org/asbmbtoday 
Charlie and Angela have contributed much more to this paper than its conception and 
title. Fred Cohen and Tom DeCoursey made most helpful suggestions. Many thanks to 
them all!  
I alone, of course, am responsible and for shadows cast by the particular stark light 
with which I view the classical landscape of chemical reactions. I am happy to fill in 
shadows and correct ambiguities and errors as you send them to me at my email 
address beisenbe@rush.edu or bob.eisenberg@gmail.com.


## Page 11


August 31, 2014 
 
11 
References  
 
1. Barthel, J., R. Buchner, and M. Münsterer, Electrolyte Data Collection Vol. 12, Part 2: 
Dielectric Properties of Water and Aqueous Electrolyte Solutions. 1995, Frankfurt 
am Main: DECHEMA. 
2. Bhat, H.S. and B. Osting, Kirchhoff's Laws as a Finite Volume Method for the Planar 
Maxwell Equations. Antennas and Propagation, IEEE Transactions on, 2011. 
59(10): p. 3772-3779. 
3. Bhat, H.S. and B. Osting, Kirchhoff’s Laws as a Finite Volume Method for the Planar 
Maxwell Equations. IEEE Transactions on Antennas and Propagation, 2011. 
59(10): p. 3772-3778. 
4. Bird, R.B., R.C. Armstrong, and O. Hassager, Dynamics of Polymeric Fluids, Fluid 
Mechanics. Vol. Volume 1. 1977, New York: Wiley. 672. 
5. Bird, R.B., O. Hassager, R.C. Armstrong, and C.F. Curtiss, Dynamics of Polymeric 
Fluids, Kinetic Theory Vol. Volume 2. 1977, New York: Wiley. 437. 
6. Brush, S.G., The Kind of Motion We Call Heat. 1986, New York: North Holland. 
7. Changeux, J.-P., Allostery and the Monod-Wyman-Changeux model after 50 years 
Annual Review Biophysics, 2012. 41: p. 103-133. 
8. Chazalviel, J.-N., Coulomb Screening by Mobile Charges. 1999, New York: Birkhäuser. 
355. 
9. Chen, D., L. Xu, A. Tripathy, G. Meissner, and R. Eisenberg, Rate Constants in 
Channology. Biophys. J., 1997. 73(3): p. 1349-1354. 
10. Conway, B.E., Electrochemical Data. 1969, Westport CT USA: Greenwood Press 
Publishers. 374. 
11. Cooper, A. and D.T.F. Dryden, Allostery without conformational change. European 
Biophysics Journal, 1984. 11(2): p. 103-109. 
12. Eisenberg, B., The value of Einstein’s mistakes. Letter to the Editor: “Einstein should be 
allowed his mistakes …” Physics Today, 2006. 59(4): p. 12. 
13. Eisenberg, B., Multiple Scales in the Simulation of Ion Channels and Proteins. The 
Journal of Physical Chemistry C, 2010. 114(48): p. 20719-20733. 
14. Eisenberg, B., Mass Action in Ionic Solutions. Chemical Physics Letters, 2011. 511: p. 1-
6. 
15. Eisenberg, B., Life's Solutions. A Mathematical Challenge. 2012. Available on arXiv as 
http://arxiv.org/abs/1207.4737. 
16. Eisenberg, B., Interacting ions in Biophysics: Real is not ideal. . Biophysical Journal, 
2013. 104: p. 1849-1866. 
17. Eisenberg, B., Electrostatic effects in living cells. Physics Today, 2013. 66(7): p. 10-11. 
18. Eisenberg, B., Y. Hyon, and C. Liu, Energy Variational Analysis EnVarA of Ions in 
Water and Channels: Field Theory for Primitive Models of Complex Ionic Fluids. 
Journal of Chemical Physics, 2010. 133: p. 104104  
19. Eisenberg, R.S., Atomic Biology, Electrostatics and Ionic Channels., in New 
Developments and Theoretical Studies of Proteins, R. Elber, Editor. 1996, World 
Scientific: Philadelphia. p. 269-357.  Published in the Physics ArXiv as 
arXiv:0807.0715. 
20. Eisenberg, R.S., Computing the field in proteins and channels. J. Membrane Biol., 1996. 
150: p. 1–25. Also available on http:\\arxiv.org as  arXiv 1009.2857.


## Page 12


August 31, 2014 
 
12 
21. Fawcett, W.R., Liquids, Solutions, and Interfaces: From Classical Macroscopic 
Descriptions to Modern Microscopic Details. 2004, New York: Oxford University 
Press. 621. 
22. Ferry, D.K., S.M. Goodnick, and J. Bird, Transport in Nanostructures. 2009, New York: 
Cambridge University Press. 670. 
23. Feynman, R.P., R.B. Leighton, and M. Sands, The Feynman: Lectures on Physics,  Mainly 
Electromagnetism and Matter. Vol. 2. 1963, New York: Addison-Wesley 
Publishing Co. 
24. Forster, J., Mathematical Modeling of Complex Fluids, in Department of Mathematics. 
2013, University of Wurzburg: Wurzburg, Germany. p. 67. 
25. Franklin, B., W. Brownrigg, and M. Farish, Of the Stilling of Waves by means of Oil. 
Philosophical Transactions of the Royal Society of London, 1774. 64: p. 445-460. 
26. Harned, H.S. and B.B. Owen, The Physical Chemistry of Electrolytic Solutions. Third ed. 
1958, New York: Reinhold Publishing Corporation. 
27. Heras, J.A., A formal interpretation of the displacement current and the instantaneous 
formulation of Maxwell?s equations. American Journal of Physics, 2011. 79(4): p. 
409. 
28. Hilser, V.J., J.O. Wrabl, and H.N. Motlagh, Structural and Energetic Basis of Allostery. 
Annual Review of Biophysics, 2012. 41(1): p. 585-609. 
29. Hovarth, A.L., Handbook of aqueous electrolyte solutions: physical properties, 
estimation, and correlation methods. 1985, New York: Ellis Horwood,. 631. 
30. Hünenberger, P. and M. Reif, Single-Ion Solvation. Experimental and Theoretical 
Approaches to Elusive Thermodynamic Quantities. 2011, London: Royal Society 
of Chemistry. 690. 
31. Hyon, Y., J.A. Carrillo, Q. Du, and C. Liu, A Maximum Entropy Principle Based Closure 
Method for Macro-Micro Models of Polymeric Materials. Kinetic and Related 
Models, 2008. 1(2): p. 171-184. 
32. Jackson, J.D., Classical Electrodynamics, Third Edition. Second Edition ed. 1999, New 
York: Wiley. 832. 
33. Jacoboni, C. and P. Lugli, The Monte Carlo Method for Semiconductor Device 
Simulation. 1989, New York: Springer Verlag. pp. 1-356. 
34. Jacobsen, R.T., S.G. Penoncello, E.W. Lemmon, and R. Span, Multiparameter Equations 
of State, in Equations of State for Fluids and Fluid Mixtures, J.V. Sengers, R.F. 
Kayser, C.J. Peters, and H.J. White, Jr., Editors. 2000, Elsevier: New York. p. 849-
882. 
35. Jimenez-Morales, D., J. Liang, and B. Eisenberg, Ionizable side chains at catalytic active 
sites of enzymes. European Biophysics Journal, 2012. 41(5): p. 449-460. 
36. Kaufman, I., D.G. Luchinsky, R. Tindjong, P.V. McClintock, and R.S. Eisenberg, 
Energetics of discrete selectivity bands and mutation-induced transitions in the 
calcium-sodium ion channels family. Phys Rev E Stat Nonlin Soft Matter Phys, 
2013. 88(5): p. 052712. 
37. Kontogeorgis, G.M. and G.K. Folas, Thermodynamic Models for Industrial Applications: 
From Classical and Advanced Mixing Rules to Association Theories. 2009: John 
Wiley & Sons. 721. 
38. Kraus, C.A., The present status of the theory of electrolytes. Bull. Amer. Math. Soc., 
1938. 44: p. 361-383. 
39. Kunz, W., Specific Ion Effects. 2009, Singapore: World Scientific 348


## Page 13


August 31, 2014 
 
13 
40. Laidler, K.J., J.H. Meiser, and B.C. Sanctuary, Physical Chemistry. Fourth ed. 2003: 
BrooksCole, Belmont CA. 1060. 
41. Lin, Y., K. Thomen, and J.-C.d. Hemptinne, Multicomponent Equations of State for 
Electrolytes. American Institute of Chemical Engineers AICHE Journal, 2007. 53: 
p. 989-1005. 
42. Luchinsky, D.G., R. Tindjong, I. Kaufman, P.V.E. McClintock, and R.S. Eisenberg, Self-
consistent analytic solution for the current and the access resistance in open ion 
channels. Physical Review E (Statistical, Nonlinear, and Soft Matter Physics), 
2009. 80(2): p. 021925-021912. 
43. Luchinsky, D.G., R. Tindjong, I. Kaufman, P.V.E. McClintock, and R.S. Eisenberg, 
Charge fluctuations and their effect on conduction in biological ion channels. 
Journal of Statistical Mechanics: Theory and Experiment, 2009. 2009(01): p. 
P01010. 
44. Lundstrom, M., Fundamentals of Carrier Transport. Second Edition ed. 2000, NY: 
Addison-Wesley. 
45. Lundstrom, M., Applied Physics Enhanced: Moore's Law Forever? Science, 2003. 
299(5604): p. 210-211. 
46. Maginn, E.J., From discovery to data: What must happen for molecular simulation to 
become a mainstream chemical engineering tool. AIChE Journal, 2009. 55(6): p. 
1304-1310. 
47. Markowich, P.A., C.A. Ringhofer, and C. Schmeiser, Semiconductor Equations. 1990, 
New York: Springer-Verlag. 248. 
48. Moore, G.E., Cramming more components onto integrated circuits. Electronics 
Magazine., 1965. 38: p. 114–117. 
49. Motlagh, H.N., J.O. Wrabl, J. Li, and V.J. Hilser, The Ensemble Nature of Allostery. 
Nature, 2014. 508(7496): p. 331-339. 
50. Myers, J.A., S.I. Sandler, and R.H. Wood, An Equation of State for Electrolyte Solutions 
Covering Wide Ranges of Temperature, Pressure, and Composition. Industrial and 
Engineering Chemical Research, 2002. 41: p. 3282-3297. 
51. Pitzer, K.S., Thermodynamics. 3rd ed. 1995, New York: McGraw Hill. 626. 
52. Pitzer, K.S. and J.J. Kim, Thermodynamics of electrolytes. IV. Activity and osmotic 
coefficients for mixed electrolytes. Journal of the American Chemical Society, 
1974. 96(18): p. 5701-5707. 
53. Post, D.E. and L.G. Votta, Computational Science Demands a New Paradigm. Physics 
Today, 2005. 58: p. 35-41. 
54. Pytkowicz, R.M., Activity Coefficients in Electrolyte Solutions. Vol. 1. 1979, Boca Raton 
FL USA: CRC. 288. 
55. Ryham, R., C. Liu, and L. Zikatanov, Mathematical models for the deformation of 
electrolyte droplets. Discrete and Continuous Dynamical Systems-Series B, 2007. 
8(3): p. 649-661. 
56. Selberherr, S., Analysis and Simulation of Semiconductor Devices. 1984, New York: 
Springer-Verlag. pp. 1-293. 
57. Sengers, J.V., R.F. Kayser, C.J. Peters, and H.J. White, Jr., Equations of State for Fluids 
and Fluid Mixtures (Experimental Thermodynamics) 2000, New York: Elsevier. 
928. 
58. Sheng, P., J. Zhang, and C. Liu, Onsager Principle and Electrorheological Fluid 
Dynamics. Progress of Theoretical Physics Supplement No. 175, 2008: p. 131-
143.


## Page 14


August 31, 2014 
 
14 
59. Shockley, W., Electrons and Holes in Semiconductors to applications in transistor 
electronics. 1950, New York: van Nostrand. 558. 
60. Shur, M., Physics of Semiconductor Devices. 1990, New York: Prentice Hall. 680. 
61. Streetman, B.G., Solid State Electronic Devices. 4th ed. 1972, Englewood Cliffs, NJ: 
Prentice Hall. 462. 
62. Sze, S.M., Physics of Semiconductor Devices. 1981, New York: John Wiley & Sons. 838. 
63. Vasileska, D., S.M. Goodnick, and G. Klimeck, Computational Electronics: Semiclassical 
and Quantum Device Modeling and Simulation. 2010, New York: CRC Press. 764. 
64. Velarde, M.G., Interfacial Phenomena and the Marangoni Effect. Interfacial Phenomena 
and the Marangoni Effect. 2003, New York: Springer. 
65. Wan, L., S. Xu, M. Liao, C. Liu, and P. Sheng, Self-Consistent Approach to Global 
Charge Neutrality in Electrokinetics: A Surface Potential Trap Model. Physical 
Review X, 2014. 4(1): p. 011042. 
66. Xu, S., P. Sheng, and C. Liu, An energetic variational approach to ion transport. 
Communications in Mathematical Sciences, 2014. 12(4): p. 779–789 Available on 
arXiv as http://arxiv.org/abs/1408.4114. 
67. Xu, X., C. Liu, and T. Qian, Hydrodynamic boundary conditions for one-component 
liquid-gas flows on non-isothermal solid substrates Communications in 
Mathematical Sciences, 2012. 10(4 (December 2012)  ): p. 1027-1053. 
68. Yang, X., M. Gregory Forest, H. Li, C. Liu, J. Shen, Q. Wang, and F. Chen, Modeling and 
simulations of drop pinch-off from liquid crystal filaments and the leaky liquid 
crystal faucet immersed in viscous fluids. Journal of Computational Physics, 2013. 
236(0): p. 1-14. 
69. Yue, P., J.J. Feng, C. Liu, and J. Shen, A Diffuse-Interface Method for Simulating Two-
Phase Flows of Complex Fluids. Journal of Fluid Mechanics, 2004. 515: p. 293--
317. 
70. Yue, P., J.J. Feng, C. Liu, and J. Shen, Viscoelastic effects on drop formation in steady 
shear. Journal of Fluid Mechanics, 2005. 540: p. 427-437. 
71. Zemaitis, J.F., Jr., D.M. Clark, M. Rafal, and N.C. Scrivner, Handbook of Aqueous 
Electrolyte Thermodynamics. 1986, New York: Design Institute for Physical 
Property Data, American Institute of Chemical Engineers.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1409_0243v1_can_we_make_biochemistry_an_exact_science
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2014/1409_0243V1_CAN_WE_MAKE_BIOCHEMISTRY_AN_EXACT_SCIENCE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

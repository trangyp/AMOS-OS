---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1606.02151v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1606.02151v2_Trends_for_isolated_amino_acids_and_dipeptides__Conformation__divalent_ion_bindi

> Source: 1606.02151v2_Trends_for_isolated_amino_acids_and_dipeptides__Conformation__divalent_ion_bindi.pdf

> Pages: 21

---


## Page 1


Trends for isolated amino acids and dipeptides:
Conformation, divalent ion binding, and remarkable
similarity of binding to calcium and lead
M. Ropo1,2,3,*, V. Blum1,4,*, and C. Baldauf1,*
1Fritz-Haber-Institut der Max-Planck-Gesellschaft, Faradayweg 4-6, D-14195 Berlin, Germany
2Department of Physics, Tampere University of Technology, Finland
3COMP, Department of Applied Physics, Aalto University, Finland
4Department of Mechanical Engineering and Materials Science, Duke University, Durham, NC, USA
*Corresponding authors: ropo@fhi-berlin.mpg.de, volker.blum@duke.edu, baldauf@fhi-berlin.mpg.de
ABSTRACT
We derive structural and binding energy trends for twenty amino acids, their dipeptides, and their interactions with the divalent
cations Ca2+, Ba2+, Sr2+, Cd2+, Pb2+, and Hg2+. The underlying data set consists of 45,892 ﬁrst-principles predicted
conformers with relative energies up to ∼4 eV (∼400 kJ/mol). We show that only very few distinct backbone structures of
isolated amino acids and their dipeptides emerge as lowest-energy conformers. The isolated amino acids predominantly
adopt structures that involve an acidic proton shared between the carboxy and amino function. Dipeptides adopt one of
two intramolecular-hydrogen bonded conformations C5 or Ceq
7 . Upon complexation with a divalent cation, the accessible
conformational space shrinks and intramolecular hydrogen bonding is prevented due to strong electrostatic interaction of
backbone and side chain functional groups with cations. Clear correlations emerge from the binding energies of the six divalent
ions with amino acids and dipeptides. Cd2+ and Hg2+ show the largest binding energies – a potential correlation with their
known high acute toxicities. Ca2+ and Pb2+ reveal almost identical binding energies across the entire series of amino acids
and dipeptides. This observation validates past indications that ion-mimicry of calcium and lead should play an important role
in a toxicological context.
Introduction
Proteins are the machinery of life. Their function is directly linked to their structure and dynamics. Natural proteins are
polyamides that are composed predominantly of the twenty amino acids, shown in Figure 1. Their three-dimensional structures
are shaped and their dynamics are inﬂuenced by several well-known conformational factors: (i) intrinsic structural propensities
of the individual building blocks, (ii) intramolecular interactions such as hydrogen bonding, salt bridges, aromatic stacking, and
van der Waals interactions, (iii) the surrounding medium, via bulk effects as well as by speciﬁc interactions. While many of
the details of protein structure arise only when speciﬁc amino acids are combined in a chain, a ﬁrst perimeter of the available
conformation space is already set out at the level of individual amino acids.1,2 This includes conformational preferences, e.g.,
through rigidity of bond lengths and angles, or through preferred backbone conformations deﬁned by torsion angle patterns
due to steric constraints. Furthermore, steric demands of side chain rotamers, electrostatics, protonation propensity, speciﬁc
chemical interactions with side chains, and other local molecular properties are already present at the monomer level.
A particularly important example of speciﬁc interactions between proteins and their environment is that with cations. About
40% of all proteins are known to bind metals.3–5 For example, Ca2+ is essential for living organisms due to its important role in
a multitude of functions, from cell signaling to bone growth.6 Calcium mediated functions can be disturbed by the presence of
alternative divalent heavy metal cations.5,7,8 In particular, lead is understood to “partially mimic the function of Ca2+”,9 with
a range of speciﬁc, documented long-term detrimental neurotoxic effects as a result. On the other hand, the sometimes very
different chemical action of lead in a toxicological context compared to Ca2+ has also been pointed out.10 It should be possible
to establish the overall chemical similarity of two different ions such as Pb2+ and Ca2+ across a large series of potentially
ligating biochemical groups based on atomistic simulations. This task is, however, fraught with difﬁculty even for simple
descriptors such as binding energies. The reason is the large space of possible molecular conformations that must be assessed
with uniform accuracy for both ions across a large series, even for comparatively small ligating molecules. Without knowing
what are the relevant conformers to consider, structural trends based on total or free energies would remain qualitative and
prone to accidental omissions of relevant conformers. Empirical potential energy surface descriptions could certainly cover the
relevant spaces, but accurate ion-molecule interactions present signiﬁcant difﬁculty in empirical atomistic modeling.
1
arXiv:1606.02151v2  [q-bio.BM]  14 Sep 2016


## Page 2


Figure 1. Molecular systems covered by this study. Top row: Basic chemical formulae of an amino acid and the
corresponding dipeptide. Side chains are represented by R. Lower panel: The chemical structures for the 20 proteinogenic side
chains R considered in this work. Where applicable, the alternative side chain protonation states considered in this work are
shown as well.
In this work, we categorize the intrinsic structural properties of twenty proteinogenic amino acids and dipeptides, as
well as their interactions with the series of divalent cations Ca2+, Ba2+, Sr2+, Cd2+, Pb2+, and Hg2+, based on a recently
published, exhaustive ﬁrst-principles dataset of their possible conformational-energy minima.11,12 The complete dataset covers
20×2×7=280 molecular systems (cf. Figure 1): 20 proteinogenic amino acid side chains attached to 2 different backbone types,
either free termini or capped (N-terminally acetylated and C-terminally amino-methylated), in 7 distinct complexation states,
i.e., either the isolated system or in complex with one of the six cations Ca2+, Ba2+, Sr2+, Cd2+, Pb2+, or Hg2+. Different
protonation states of the side chains (basic and acidic amino acids, see Figure 1) or the backbone (neutral and zwitterionic)
were considered where applicable. The total number of conformers covered is 45,892. This is close to the limit of what can be
accomplished computationally for a conformational search of this extent and for the extensively benchmarked11,13–19 level of
theory used to create the database (density-functional theory (DFT) based on a van-der Waals corrected generalized gradient
functional (PBE+vdW)20–22, see Methods).
We here study the local, speciﬁc bonding contribution of the amino acids and dipeptides in conjunction with divalent cations,
but otherwise in isolation. This environment does, of course, not resemble biological conditions, where cations like Ca2+
highly interact with their surrounding environment, e.g., water molecules forming hydration shells. However, for peptide-bound
cations, such water-ion interactions do not interfere directly with the ion-peptide interactions. From a modeling perspective,
including solvent effects either implicitly (by polarization effects)23–26 or by direct calculations of free-energy differences
from molecular dynamics is in principle possible. For the breadth of the conformational study presented here, though, such an
attempt would introduce the inevitable ambiguity of which exact solvent environment and/or which model to consider, as well
as (for an explicit treatment) a sheer amount of free-energy calculations that is signiﬁcantly beyond the scope of the present
work. In the present paper, we therefore focus on the large and precisely deﬁnable total-energy contribution emerging from the
speciﬁc ion-peptide bond.
Speciﬁcally, we show how a large-scale and systematic computational effort enables us to reveal conformational and binding
energy trends that would not be readily apparent from isolated case studies based on different, potentially disparate levels of
theory or experimental setups. A particularly striking example is the remarkable similarity of Ca2+ and Pb2+ interactions with a
broad range of biologically relevant ligands, proven below and indicating that the related observations in toxicology9,10 emerge
directly from the fundamental underlying potential energy surface.
2/21


## Page 3


Figure 2. The conformational hierarchies for each amino acids (a) and the capped amino acids (dipeptides) are shown for the
isolated (”bare”, red) and, alternatively, for the Ca2+ coordinated form (blue). The labels ”Ca” and ”bare” are accompanied by
numbers that reﬂect the total number of conformers found for each system.
Results and discussion
Trend 1: Size of conformational space
Figure 2 summarizes the PBE+vdW conformational energy hierarchies and overall numbers of conformers considered in our
study. For the amino acids and dipeptides without ions, the number of minima with the size (number of atoms) and ﬂexibility
(number of freely rotatable bonds) of the side chains of the building blocks. Consequently, we predict only a few conformers
(from below ten to a few tens) for the small amino acids and dipeptides without a side chain (Gly), with a short side chain
(Ala), or with a constrained side chain (Pro). In contrast, thousand(s) of conformers are predicted for the amino acids with long
and ﬂexible side chains, especially Arg and Lys. This number is not surprising, since the side chains alone give rise to many
different conformations that are close in energy. Tabulations of these possible conformations, so-called rotamer libraries,27
are sometimes used in protein modeling in order to predict, for a given backbone conformation, a set of probable side chain
conformations. Current standard rotamer libraries are either (i) derived from protein crystal structures applying ﬁltering and
selection criteria28,29 or (ii) based on carefully curated sets of experimental protein structures or model peptides (GGXGG) that
were subjected to molecular dynamics simulations.30,31 From the latter, rotamers can be obtained that do not carry the bias of
the crystal structures, yet they still rely on the empirical parametrization of the underlying force ﬁelds. Our data set11,12 offers
an alternative, empiricism free, basis for the derivation of rotamer libraries.
3/21


## Page 4


If the amino acids are instead coordinated to the positive ion Ca2+, the overall space of conformational minima contracts
signiﬁcantly (1,694 and 4,103 conformers overall for the amino acids and dipeptides, respectively). Simultaneously, the relative
energy range expands to up to about 4 eV or 400 kJ/mol (Figure 2). Evidently, the cation places a strong electrostatic constraint
on the positions of electronegative atoms and therefore reduces the accessible conformational space. This effect is especially
pronounced for amino acids with a ﬂexible side chain that interacts strongly with the cation due a lone pair, as exempliﬁed
by the difference between the unprotonated and protonated pairs Arg/ArgH and Lys/LysH. Here, the protonation results in a
Coulomb repulsion between the positively charged cation and the positively charged end group of the amino acid side chain. As
a results, the overall number of conformation changes from 484 to 135 for Arg/ArgH + Ca2+ and from 188 to 52 for Lys/LysH
+ Ca2+.
Trend 2: Conformational preferences
For the isolated amino acids, the preferred conformation types are schematically summarized in Figure 3A. Isolated amino
acids (with the exception of Arg) are found to assume one of three basic backbone conformations (type I, type II, zwitterionic)
as their lowest-energy structure. There is a close relation between type II and the zwitterionic state: only a minuscule shift
of the shared proton from the carboxylic group to the amino function converts one type to the other. Most of the lowest
energy conformers feature the shared acidic proton between the backbone carboxylic acid function and the backbone amino-N.
Thus, this group of lowest-energy conformers is either type II or zwitterionic. In the case of Arg, a similar conformation is
assumed by the zwitterionic backbone carboxyl group and the side chain guanidino function. We caution that, in several cases,
the conformational energy differences between the basic backbone conformations are rather narrow. In these cases, changes
to the level of theory could alter the detailed hierarchy observed.16–19 In fact, the comparison to previous ﬁrst principles
studies of amino acids shows that different methods of calculation (level of theory and basis set) predict different preferred
conformations.32,33 In experimental studies of aliphatic amino acids, both states (type II/zwitterionic and type I) have been
observed,34,35 also highlighting the close energetic competition of the different states. Nevertheless, the emergence of just a
few basic preferred backbone conformations from the vast overall conformation space studied is remarkable and, as a trend,
robust based on the PBE+vdW level of theory applied here.
For the amino acids interacting with Ca2+ cations, zwitterionic and neutral/uncharged state of the backbone can be clearly
distinguished. As illustrated in Figure 3B, the cation can either bind to the lone pairs of the amino and carboxyl groups in
the neutral/uncharged state (a.k.a. charge-solvated structure) or interact solely with the deprotonated and negatively charged
carboxyl group in the zwitterionic state (a.k.a. salt-bridge structure).36 The zwitterionic backbone state is more stable than the
uncharged backbone state for 13 of 20 amino acid-Ca2+ systems (see Figure 3B). The cation-amino acid complexes of the
aliphatic amino acids as well as of Gly, Pro, and Lys are predicted to be zwitterionic for all different cations in this study. Thr
and Asn prefer the uncharged/neutral backbone state when interacting with the divalent cations covered by the present study.
The amino-methylation and acetylation of the backbone functional groups of the amino acids leads to the so-called
dipeptides, as schematically shown in Figures 1 and 4A. Since both termini resemble the local bonding environment of peptide
bond, the dipeptide form is closer to the situation of building block embedded in a poly-peptide chain. In particular, end group
effects such as a zwitterionic form cannot occur in the dipeptides. The backbone conformational space of the dipeptides can be
represented by Ramachandran plots37 of the torsion angles φ and ψ. Figure 4A includes a graphical deﬁnition of both angles.
The two dominant conformer types found for the dipeptides are referred to as Ceq
7 and C5. The nomenclature indicates the
size of the hydrogen-bonded pseudocycle (5 or 7 members) The C7 pseudocycle can occur in two different conformations
that are approximate mirror images. These images are, however, distinguished by the axial or equatorial orientation of the
side chain ’R’ relative to the plane of the hydrogen-bonded pseudocycle. The lowest energy conformers of each dipeptide are
highlighted in the Ramachandran plot in Figure 4A. The area occupied by C5 is located at the 180/-180 degree border between
quadrants II and III. The area occupied by Ceq
7 can be found roughly in the center of quadrant II. All dipeptides that preferably
exhibit the C5 backbone conformation have bulky side chains. This is in accordance with the known propensity of bulky side
chains to enforce the formation of β strand conformations. In contrast, the Ceq
7 group almost exclusively features members with
comparatively small side chains, with the sole exception of Trp and its large indole side chain functional group that is also
predicted to fall into the Ceq
7 group.
The interaction with a Ca2+ cation has a major impact on the predicted conformations (see Figure 4B). Structure types that
are preferred without the cation, like C5 or Ceq
7 , are hardly populated at all in the presence of Ca2+. Instead, there are now two
new dominant areas in the Ramachandran plot in Figure 4B that differ from the preferences exhibited by the isolated dipeptides.
The global minima for most of the dipeptide-Ca2+ systems are located in quadrant I. The backbone oxygens of the acetyl
moiety and the amino acid carbonyl group bind the cation. The corresponding structure is schematically shown in Figure 4B.
The cation is bound to the two backbone oxygens and thus closes an otherwise incomplete 7-membered pseudocycle (iC7).
Similar structures were observed before by simulation and experiment for the interaction of sodium cations with small model
peptides.14 The side chain ’R’ is oriented parallel to the axis (”axial”) of this pseudocycle and is hence referred to as iCax
7 . This
4/21


## Page 5


Figure 3. Preferred backbone conformations and protonation states for bare amino acids and for amino acids with Ca2+.
(a) Schematic representations of the possible backbone H bonded structure types in amino acids together with a plot detailing
the energy hierarchy of types I and II and the zwitterionic state for the isolated amino acids. (b) The two basic backbone-cation
conformation types for amino acids with Ca2+ and a plot of their relative energies for each amino acid system studied. For
clarity, only the lowest energy representatives of the respective structure types are shown. The energy of the respective global
minimum is set to 0. The order of the amino acids on the x axis reﬂects chemical groups in the following sequence: aliphatic,
aromatic, basic, acidic, amides, alcohol/thiol, other.
5/21


## Page 6


Figure 4. Ramachandran plots for the bare dipeptides (a) and for the dipeptides interacting with Ca2+ (B). The φ/ψ tuples of
the populated conformers of all dipeptides are shown by black crosses. The respective lowest energy conformers for each
amino acid type are highlighted by red circles. Structural sketches illustrate the different dominant structure types of the global
minima.
6/21


## Page 7


orientation also allows for interactions between cation and respective side chain functional groups. For LysH, ArgH, HisH, Ala,
and Leu, the predicted global minima are located in quadrant III. The corresponding backbone structure is again characterized
by a 7-membered ring that is closed by the cation. For this group of dipeptides, the side chain is oriented equatorially, i.e. it is
within the plane of the pseudocycle. Hence, the conformation is referred to as iCeq
7 . It is the approximate mirror image of iCax
7 .
The preference for the equatorial side chain orientation is particularly strong for in case of the protonated sidechains of LysH,
ArgH, HisH due to charge repulsion. Finally, Pro is conformationally restricted due to the heterocycle bridging the backbone.
Trend 3: Ion binding energies
In addition to the structural effects of the cation, the binding energy of the individual amino acids to Ca2+ and to other
divalent cations (Ba2+, Cd2+, Hg2+, Pb2+, or Sr2+) reveals distinct, remarkable trends across the series of amino acids and
their dipeptidic form. Starting from the predicted conformers involving Ca2+, we created conformational energy hierarchies
involving the other divalent cations by replacing Ca2+ with the respective alternative cation and re-optimizing the resulting
structure. Importantly, we include all local structure minima found with Ca2+, not just the Ca2+-containing global minimum
structure for each amino acid or dipeptide. In this way, we can faithfully compute the binding energies for all the alternative
cations to the different proteinogenic amino acids and dipeptides, including the various protonations states. We deﬁne the
binding energy from total energies of the lowest-energy conformations of the individual constituents as follows:
Ebinding = Eamino acid +Ecation −Ecomplex.
(1)
The order of the amino acids (or dipeptides) along the x-axis of the plots in Figure 5 follows their afﬁnity to the alkaline
earth metals Ca2+, Ba2+, and Sr2+. The ranking for the amino acids binding Pb2+, Cd2+, and Hg2+ is similar but features
slight deviations. Especially for the sulfur containing amino acids Met and Cys, the afﬁnities to Pb2+, Cd2+, and Hg2+ increase
more than for the other amino acids (dipeptides). The amino acids (dipeptides) can be roughly grouped according to their Ca2+
afﬁnity (from strongest to weakest):
deprotonated acids >> amides, bases > aromatic, acids > aliphatic >> protonated bases.
Electrostatic interactions are deﬁning here, best illustrated by the high binding energies that result from the attractive interaction
between the cation and the negatively charged deprotonated side chains of Glu and Asp and the low binding energies resulting
from the repulsive interactions between cation and positively charged side chains in case of ArgH, LysH, and HisH.
Figure 5 also shows the increasing afﬁnity of the cations to the amino acids (and dipeptides) following the order:
Hg2+ > Cd2+ > Pb2+ ∼Ca2+ > Sr2+ > Ba2+
(order based on average binding energies from strong to weak binding cation).
Importantly, the observed order of the binding energies of different cations holds uniformly across all amino acids and
must therefore be intrinsic to the individual ions. We therefore exemplify an a posteriori explanation of this behavior by a
comparison of the lowest-energy conformations for a few representative dipeptides (Glu, Arg, GluH, and Cys) as ligands to
each of the six cations covered by this study.
Without loss of generality, we may discuss the interaction strength in terms of distinct contributions that are well established
in chemistry: ionic (well deﬁned if touching charged hard spheres are assumed), static polarizability, dispersion interactions,
and, lastly, a contribution from covalent bonding that accounts for all remaining terms. We note at the outset that the computed
differences in dispersion interactions between the six different ions and the peptides are much smaller than the trends shown in
Figure 5 and can therefore be neglected for the following discussion.
In case of the alkaline earth metal cations (Ca2+, Sr2+, Ba2+), the binding strength trend is well represented already by the
bond distances represented in Figure 6a, which essentially reﬂect the increasing ionic radii from Ca2+ via Sr2+ to Ba2+.38,39
For the pairs Ca2+/Pb2+ and Cd2+/Hg2+, however, ionic radii and ionic binding alone do not sufﬁce to explain the observed
trends. Covalent and/or polarization contributions must therefore account for the remaining differences. For a more quantitative
description in terms of our own data, we plot the ion-ligand binding distances for all six cations considered to Glu, Arg, GluH,
and Cys in Figure 6a.
Pb2+ is in principle larger than Ca2+, consistent with our data. By purely ionic considerations, Pb2+ should therefore bind
somewhat less strongly than Ca2+. However, Pb2+ features a relatively shallow ﬁlled s shell in Pb2+ that is absent in Ca2+.
Thus, Pb2+ should be slightly more polarizable and may have a slightly larger covalent contribution to the binding strength,
which results in the comparable binding energy trend for Pb2+ and Ca2+.
What sets Hg2+ and Cd2+ apart from Ca2+, Sr2+ and Ba2+ is a relatively shallow ﬁlled d shell for Hg2+/Cd2+. Ionic, static
polarizability and/or residual covalent contributions should thus all lead to an overall stronger binding of Hg2+ and Cd2+ to the
dipeptides than for the alkaline earth metals, as we observe. Between Hg2+ and Cd2+, however, Hg2+ is larger than Cd2+ in
7/21


## Page 8


Figure 5. Binding afﬁnity of the unprotected amino acids (a) and the dipeptides (b). The building blocks are sorted according
to their Ca2+ afﬁnity with strongest to weakest afﬁnity from left to right. Open symbols in (a) indicate the zwitterionic form
and ﬁlled symbols the uncharged/neutral form as the respective global minimum. The amino acids and dipeptides (and their
protomers where applicable) were sorted according to the binding energy to Ca2+ from the highest to the lowest values.
8/21


## Page 9


Figure 6. (a) Binding distances between the divalent cations and their nearest ligands in the lowest-energy conformations of
cation-coordinated dipeptide forms of Glu, Arg, GluH, and Cys. The structure images in the insets show the Ca2+ coordinated
forms and are structurally equivalent for the other cations as well. Different ligand atoms are distinguished by different-colored
curves (red: O, blue: N, orange: S), as noted in the ﬁgure. (b) Histograms of cation-O distances for lowest-energy conformers
over all dipeptides or uncapped amino acids and the cations covered in the study.
9/21


## Page 10


terms of tabulated ionic radii for the same coordination number,38,39 and thus Cd2+ should bind more strongly for otherwise
equivalent conformation. Yet, the opposite is the case in Figure 5, i.e., Hg2+ binds signiﬁcantly more strongly. The reason
can be discerned from Figure 6a. While Cd2+ retains approximately equal distances from its ligands, Hg2+ changes its local
coordination shell to pull two of the ligands closer than the others, in fact closer than any of the ligands of Cd2+. This suggests
a strongly covalent and/or static polarizability driven contribution to the Hg2+-dipeptide bond. The orbital-based explanation
likely resides in the fact that the 5d shells of Hg2+ are shallower than the 4d shells of Cd2+. As a result, the frontier orbitals of
Hg2+ are more ﬂexible and have a larger incentive to participate in some form of residual bond. Overall, Figure 6a reveals
that the coordination chemistry of Hg2+ is in detail different from that of Cd2+, explaining the much stronger overall binding
strength of Hg2+ to the amino acid and dipeptide ligands studied here.
The trend that we just discussed for a few selected amino acid dipeptides holds over the whole range of amino acids and
dipeptides as is illustrated by plots in the Supplementary Information similar to the ones shown in Figure 6a. Additionally,
Figure 6b shows histograms of cation-oxygen distances across the respective lowest-energy structures of all amino acids and
dipeptides considered in this study. The histograms also reﬂect the trends of Figure 6a, e.g. the increase of the median distances
for Ca2+, Sr2+, and Ba2+ or the change of the one-peak distribution of Cd2+ to a multi-modal distribution for Hg2+ that
indicates strongly covalent and/or static polarizability driven cation-O interactions existing alongside purely ionic interactions
for Hg2+.
Trend 4: Ion mimicry and toxicity
We next attempt to correlate toxicological effects of the different ions with their respective interactions across the series of
amino acids and dipeptides. For acute (short-term) toxicity, we consider median lethal doses (LD50)40 for the chloride salts
(selected because of their generally high solubility) of the respective divalent cations. The LD50 is the dose of a toxin required
to kill half of the individuals in a test population; it is thus a measure of acute, not long-term toxicity. An interesting trend
emerges when comparing these LD50 values to the binding energy trends reported in Figure 5 of the present study. Ca2+ might
naturally serve as a reference point in this comparison. The chloride salt is moderately toxic with an LD50 of 2,301 mg/kg.
Sr2+ exhibits relatively low binding energies to the amino acids. The LD50 of the respective chloride is also moderate with
1,253 mg/kg. Toxic effects of Strontium result from radioactive isotopes and not from the binding competition of Sr2+ with
Ca2+. Pb2+ and Ca2+ show almost exactly the same binding energy trend. Their acute toxicities are similar and not high, with
LD50 values of 1,947 mg/kg and 2,301 mg/kg, respectively, for PbCl2 and CaCl2. The divalent cations of mercury and cadmium
show the highest binding energies in our comparison. Interestingly, the acute toxicities of CdCl2 and HgCl2 are also much
higher than those of SrCl2, CaCl2 and PbCl2, with LD50 values of values of 107 and 47 mg/kg for Cd and Hg, respectively.
Indeed, cadmium ions bind tightly to proteins and compete with Zn2+ and Ca2+ and especially also with sulfur bound Cu+ and
with iron in iron-sulfur centers in proteins.41 For the cations Hg2+, Cd2+, Pb2+, Ca2+, and Sr2+, we might thus infer a tentative
correlation of acute toxicities with binding energy trends. A clear outlier, however, is Ba2+. Figure 5 shows it to be the cation
in this study with the lowest afﬁnity to the amino acids and dipeptides. In contrast, its known acute toxicity is rather high, with
LD50 values ranging from 100 to 300 mg/kg. Indeed, the toxic species is the bare cation and not (as in the case of Hg or Cd) the
protein bound cation. Due to its large size and weak binding energy for a divalent cation, Ba2+ may interfere with K+ channels
instead and consequently has effects on, e.g., the function of muscle tissue.42,43
We ﬁnally return to the remarkable, almost exact quantitative agreement of the computed binding energies for Ca2+ and
Pb2+, respectively, in Figure 5. This trend is here revealed across an entire series of molecular ligands that are central to
biochemistry. Consistent with low acute toxicities, their similarity supports directly the available evidence that Pb2+ can
mimic Ca2+:9 individual amino side group functions will not distinguish these two ions. Additionally, tabulated qualitative
descriptors such as their standard hydration enthalpies (Pb2+: −1479.9 kJ/mol, Ca2+: 1592.4 kJ/mol)44 and Shannon ionic
radii (octahedral: Pb2+: 98 pm, Ca2+: 100 pm)38,39 are also close. Yet, Pb and Ca are certainly not chemically identical,10
e.g., due to possible multivalency of Pb. Thus, Pb2+ may ﬂy “under the radar” of typical factors distinguishing ions, helping
facilitate its more subtle (neuro)toxic actions9 or other detrimental effects on protein folding, maturation, and interaction in
some instances.45
Summary
This study is a ﬁrst step towards an unbiased understanding of peptide cation interactions from ﬁrst principles. A large, ﬁrst-
principles data base of more than 45,000 conformers of 20 proteinogetic aminoacids, their dipeptides, and their coordination
with the six divalent cations Ca2+, Ba2+, Sr2+, Cd2+, Hg2+, and Pb2+11,12 allows us to identify trends across an entire series
of biochemically relevant functionalities:
• In the gas phase and at the PBE+vdW level of theory, the type II/zwitterionic form of the amino acid backbone dominates
over type I.
10/21


## Page 11


• The dipeptides (acetylated and amino-methylated amino acids) assume only two distinct types of low-energy conforma-
tions, C5 and Ceq
7 .
• The conformational space of amino acids and dipeptides, as measured by the number of local minima found for each
system, contracts upon coordination with divalent cations (with Ca2+ attachment, signiﬁcantly fewer minima are found).
Their conformational freedom is reduced by strong electrostatic interactions of backbone and side chain functionalities
with the cation.
• The interaction of amino acids and Ca2+ occurs preferably via the deprotonated (negatively charged) backbone carbonyl
functions. In the cases of the dipeptides, the Ca2+ cation preferentially interacts with the backbone carbonyl groups of
the amino acid and the acetyl capping.
• The heavy-metal cations Hg2+ and Cd2+ bind more strongly to the amino acids and dipeptides than Ca2+.
• We can construct an a posteriori plausible correlation between the general binding energies of divalent cations to the
amino acids and the acute toxicities of their chloride salts. The strong binding energies of Cd2+ and Hg2+ correlate with
their much higher acute toxicities, while the weakest binder, Ba2+, is known to affect the function of another much more
weakly binding cation, K+.
• At the PBE+vdW level of theory, Pb2+ shows binding energies to all studied amino acids and dipeptides that are virtually
identical to those of Ca2+. Pb2+ thus has the ability to mimic much of the function of Ca2+, but not precisely, consistent
with its interference with Ca2+ functions over longer time scales and/or in speciﬁc circumstances.
The insights generated in this work are inherently enabled by having access to an essentially exhaustive conformational
energy data set for a wide range of amino acids, their dipeptides, and their various cation bound forms. The focus of our study
is to study general trends across a large portion of chemical space. This of course comes at the expense of investigating more
subtle effects, e.g. effects of electronic correlation energy treatments at higher levels and the effects of ﬁnite temperature, and
entropy are not reﬂected but could be included in future reﬁnements of the existing database. By considering only single amino
acids/dipeptides we consider steric effects only to a limited extend. Next steps could include the reconstruction of protein
cation binding sites in a similar fashion a outlined in the review articles by Dudev and Lim and in references cited therein.46–48
In addition and as noted in the introduction, the environment or solvent medium surrounding cations bound to peptides is,
of course, very important. For a quantitative understanding of speciﬁc environmental conditions, we believe that dedicated
simulations incorporating effective continuum models23–26 or simulations of free energy differences by explicit molecular
dynamics constitute excellent follow-up opportunities to our study.
Nonetheless, the emergence of unambiguous overall trends from an entirely non-empirical ﬁrst-principles treatment (not
relying on any speciﬁc “chemical intuition” at the outset) in our study is encouraging, showing the relevance of trends at the
Born-Oppenheimer potential energy surface as a basic quantity and highlighting the power of systematically scanning large
segments of chemical space with high computational accuracy to underpin empirically suspected trends.
Methods
The level of theory employed to assemble the conformer database11 is a high-accuracy49 numeric atom-centered basis
set implementation20,50 of density-functional theory (DFT) in the Perdew-Burke-Ernzerhof (PBE)21 generalized-gradient
approximation, combined with the pairwise van der Waals correction by Tkatchenko and Schefﬂer (PBE+vdW).22 The reliability
of PBE+vdW for the peptide structure problem has been established by (i) comparisons to CCSD(T) benchmark investigations
for oligo-alanine systems13 and alanine dipeptides with Li+14, (ii) comparison to carefully performed basis-set extrapolated
MP2 calculations11, and comparisons to experimental spectroscopic benchmarks.15 Importantly, the actual conformations
identiﬁed by PBE+vdW remain meaningful even in cases where, for larger oligopeptides, more expensive higher levels of theory
are needed to reproduce small energetic differences to the exact conformational energy hierarchy found in experiment.16–19
As described in detail in Ref.11, for each of the amino acids and dipeptides with and without Ca2+, a global basin-hopping
search with TINKER51,52 was performed using the OPLS-AA force ﬁeld53 to pre-screen for relevant conformations. This set of
conformations was then relaxed at the PBE+vdW level. After this global search step, a local conformational reﬁnement was
performed by PBE+vdW based replica-exchange molecular dynamics (REMD)54–56 followed again by geometry relaxations
with PBE+vdW. For a subset of seven dipeptides (Ala, Gly, Phe, Val, Ile, Trp, Leu) and by comparing to an independently
performed genetic algorithm search at the same level of theory,57 this search was shown to be essentially complete. Conformers
for amino acids and dipeptides in complex with Ba2+, Sr2+, Cd2+, Pb2+, and Hg2+ were generated by substituting a different
ion into the geometries of the Ca2+ complexes and locally optimizing the new geometry.
11/21


## Page 12


References
1. Bouchoux, G. Gas phase basicities of polyfunctional molecules. part 3: Amino acids. Mass Spectrom. Rev. 31, 391–435
(2012).
2. Baldauf, C. & Hofmann, H.-J. Ab initio MO theory - An important tool in foldamer research: Prediction of helices in
oligomers of ω-amino acids. Helv. Chim. Acta 95, 2348–2383 (2012).
3. Holm, R. H., Kennepohl, P. & Solomon, E. I. Structural and functional aspects of metal sites in biology. Chem. Rev. 96,
2239–2314 (1996).
4. Tainer, J. A., Roberts, V. A. & Getzoff, E. D. Protein metal-binding sites. Curr. Opin. Biotech. 3, 378 – 387 (1992).
5. Kirberger, M. & Yang, J. J. Structural differences between Pb2+- and Ca2+-binding sites in proteins: Implications with
respect to toxicity. J. Inorg. Biochem. 102, 1901–1909 (2008).
6. Cheng, R. & Zhorov, B. Docking of calcium ions in proteins with ﬂexible side chains and deformable backbones. Eur.
Biophys. J. 39, 825–838 (2010).
7. Sadiq, S., Ghazala, Z., Chowdhury, A. & B¨usselberg, D. Metal toxicity at the synapse: Presynaptic, postsynaptic, and
long-term effects. J. Toxicol. 132671 (2012).
8. Sharma, S. K., Goloubinoff, P. & Christen, P. Heavy metal ions are potent inhibitors of protein folding. Biochem. Bioph.
Res. Co. 372, 341 – 345 (2008).
9. Florea, A.-M. et al. Lead (Pb2+) neurotoxicity: Ion-mimicry with calcium (Ca2+) impairs synaptic transmission. A review
with animated illustrations of the pre- and post-synaptic effects of lead. Journal of Local and Global Health Science 4,
1–38 (2013).
10. Simons, T. Cellular interactions between lead and calcium. Br. Med. Bull. 42, 431–434 (1986).
11. Ropo, M., Schneider, M., Baldauf, C. & Blum, V. First-principles data set of 45,892 isolated and cation-coordinated
conformers of 20 proteinogenic amino acids. Sci. Data 3, 160009 (2016).
12. Ropo, M., Baldauf, C., Blum, V. & Schefﬂer, M. Berlin ab initio amino acid DB (2016). http://aminoaciddb.rz-
berlin.mpg.de/ .
13. Tkatchenko, A., Rossi, M., Blum, V., Ireta, J. & Schefﬂer, M. Unraveling the stability of polypeptide helices: Critical role
of van der Waals interactions. Phys. Rev. Lett. 106, 118102 (2011).
14. Baldauf, C. et al. How cations change peptide structure. Chem. Eur. J. 19, 11224–11234 (2013).
15. Rossi, M. et al. Secondary structure of Ac-Alan-LysH+ polyalanine peptides (n = 5,10,15) in vacuo: Helical or not? J.
Phys. Chem. Lett. 1, 3465–3470 (2010).
16. Schubert, F. et al. Exploring the conformational preferences of 20-residue peptides in isolation: Ac-Ala19-Lys + H+ vs.
Ac-Lys-Ala19 + H+ and the current reach of DFT. Phys. Chem. Chem. Phys. 17, 7373–7385 (2015).
17. Schubert, F. et al. Native like helices in a specially designed β peptide in the gas phase. Phys. Chem. Chem. Phys. 17,
5376–5385 (2015).
18. Rossi, M., Chutia, S., Schefﬂer, M. & Blum, V. Validation challenge of density-functional theory for peptides - example of
Ac-Phe-Ala5-LysH+. J. Phys. Chem. A 118, 7349–7359 (2014).
19. Baldauf, C. & Rossi, M. Going clean: structure and dynamics of peptides in the gas phase and paths to solvation. J. Phys.
Condens. Matter 27, 493002 (2015).
20. Blum, V. et al. Ab initio molecular simulations with numeric atom-centered orbitals. Comput. Phys. Commun. 180, 2175 –
2196 (2009).
21. Perdew, J. P., Burke, K. & Ernzerhof, M. Generalized gradient approximation made simple. Phys. Rev. Lett. 77, 3865–3868
(1996).
22. Tkatchenko, A. & Schefﬂer, M. Accurate molecular van der Waals interactions from ground-state electron density and
free-atom reference data. Phys. Rev. Lett. 102, 073005 (2009).
23. Marenich, A. V., Cramer, C. J. & Truhlar, D. G. Universal Solvation Model Based on Solute Electron Density and on a
Continuum Model of the Solvent Deﬁned by the Bulk Dielectric Constant and Atomic Surface Tensions. J. Phys. Chem. B
113, 6378–6396 (2009).
24. Klamt, A. The COSMO and COSMO-RS solvation models. WIREs Comput. Mol. Sci. 1, 699–709 (2011).
12/21


## Page 13


25. Mennucci, B. Polarizable continuum model. WIREs Comput. Mol. Sci. 2, 386–404 (2012).
26. Ringe, S., Oberhofer, H., Hille, C., Matera, S. & Reuter, K. Function-Space-Based Solution Scheme for the Size-Modiﬁed
Poisson–Boltzmann Equation in Full-Potential DFT. J. Chem. Theory Comput. 12, 4052–4066 (2016).
27. Dunbrack Jr., R. L. Rotamer libraries in the 21st century. Curr. Opin. Struct. Biol. 12, 431 – 440 (2002).
28. Lovell, S. C., Word, J. M., Richardson, J. S. & Richardson, D. C. The penultimate rotamer library. Proteins 40, 389–408
(2000).
29. http://kinemage.biochem.duke.edu/databases/rotamer.php .
30. Scouras, A. D. & Daggett, V. The dynameomics rotamer library: Amino acid side chain conformations and dynamics from
comprehensive molecular dynamics simulations in water. Protein Sci. 20, 341–352 (2011).
31. http://www.dynameomics.org/rotamer/indexRotamer.aspx .
32. Cs´asz´ar, A. G. Conformers of gaseous α-alanine. J. Phys. Chem. 100, 3541–3551 (1996).
33. Maul, R., Ortmann, F., Preuss, M., Hannewald, K. & Bechstedt, F. DFT studies using supercells and projector-augmented
waves for structure, energetics, and dynamics of glycine, alanine, and cysteine. J. Comput. Chem. 28, 1817–1833 (2007).
34. Stepanian, S. G., Reva, I. D., Radchenko, E. D. & Adamowicz, L. Conformational behavior of α-alanine. Matrix-isolation
infrared and theoretical DFT and ab initio study. J. Phys. Chem. A 102, 4623–4629 (1998).
35. Lesarri, A., S´anchez, R., Cocinero, E. J., L´opez, J. C. & Alonso, J. L. Coded amino acids in gas phase: The shape of
isoleucine. J. Am. Chem. Soc. 127, 12952–12956 (2005).
36. Corral, I., Lamsabhi, A. M., M´o, O. & Y´a˜nez, M. Infrared spectra of charge-solvated versus salt-bridge conformations of
glycine-, serine-, and cysteine-Ca2+ complexes. Int. J. Quantum Chem. 112, 2126–2134 (2012).
37. Ramachandran, G., Ramakrishnan, C. & Sasisekharan, V. Stereochemistry of polypeptide chain conﬁgurations. J. Mol.
Biol. 7, 95 – 99 (1963).
38. Shannon, R. D. Revised effective ionic radii and systematic studies of interatomic distances in halides and chalcogenides.
Acta Crystallographica Section A 32, 751–767 (1976).
39. Grimes, R. Shannon Radii. URL http://abulafia.mt.ic.ac.uk/shannon/ptable.php.
40. Material Safety Data Sheets by Sigma Aldrich http://www.sigmaaldrich.com/safety–center.html.
41. Maret, W. & Moulis, J.-M. The bioinorganic chemistry of cadmium in the context of its toxicity. In Sigel, A., Sigel, H. &
Sigel, R. K. (eds.) Cadmium: From Toxicity to Essentiality, vol. 11 of Metal Ions in Life Sciences (Springer Netherlands,
2013).
42. Welsh, M. Barium inhibition of basolateral membrane potassium conductance in tracheal epithelium. Am. J. Physiol. 244,
F639–645 (1983).
43. Raisbeck, M. F. et al. Water Quality for Wyoming Livestock and Wildlife: A review of the literature pertaining to the health
effects of inorganic contaminants (University of Wyoming).
44. Burgess, J. Metal Ions in Solution (Ellis Horwood, Chichester, 1978).
45. Garza, A., Vega, R. & Soto, E. Cellular mechanisms of lead neurotoxicity. Med. Sci. Monit. 12, RA57–65 (2006).
46. Dudev, T. & Lim, C. Principles Governing Mg, Ca, and Zn Binding and Selectivity in Proteins. Chem. Rev. 103, 773–788
(2003).
47. Dudev, T. & Lim, C. Metal Binding Afﬁnity and Selectivity in Metalloproteins: Insights from Computational Studies.
Annu. Rev. Biophys. 37, 97–116 (2008).
48. Dudev, T. & Lim, C. Competition among Metal Ions for Protein Binding Sites: Determinants of Metal Ion Selectivity in
Proteins. Chem. Rev. 114, 538–556 (2014).
49. Lejaeghere, K. et al. Reproducibility in density functional theory calculations of solids. Science 351 (2016).
50. Havu, V., Blum, V., Havu, P. & Schefﬂer, M. Efﬁcient integration for all-electron electronic structure calculation using
numeric basis functions. J. Comput. Phys. 228, 8367 – 8379 (2009).
51. Ponder, J. W. & Richards, F. M. An efﬁcient Newton-like method for molecular mechanics energy minimization of large
molecules. J. Comput. Chem. 8, 1016–1024 (1987).
52. Ren, P., & Ponder, J. W. Polarizable atomic multipole water model for molecular mechanics simulation. J. Phys. Chem. B
107, 5933–5947 (2003).
13/21


## Page 14


53. Jorgensen, W. L., Maxwell, D. S. & Tirado-Rives, J. Development and testing of the OPLS all-atom force ﬁeld on
conformational energetics and properties of organic liquids. J. Am. Chem. Soc. 118, 11225–11236 (1996).
54. Swendsen, R. H. & Wang, J.-S. Replica Monte Carlo simulation of spin-glasses. Phys. Rev. Lett. 57, 2607–2609 (1986).
55. Sugita, Y. & Okamoto, Y. Replica-exchange molecular dynamics method for protein folding. Chem. Phys. Lett. 314, 141 –
151 (1999).
56. Beret, E. C., Ghiringhelli, L. M. & Schefﬂer, M. Free gold clusters: beyond the static, monostructure description. Faraday
Discuss.png 152, 153–167 (2011).
57. Supady, A., Blum, V. & Baldauf, C. First-principles molecular structure search with a genetic algorithm. J. Chem. Inf.
Model. 55, 2338–2348 (2015).
Acknowledgements
The authors thank Matthias Schefﬂer (FHI Berlin) for continuous support of this work.
Author contributions
M.R., V.B., C.B. designed the study. M.R. performed the simulations. M.R., C.B. analyzed the data. M.R., V.B., C.B. wrote the
article.
Competing ﬁnancial interests
The authors declare no competing ﬁnancial interests.
14/21


## Page 15


Supplementary Information
Binding distances between the divalent cations and their nearest ligands in the lowest-energy conformations of 20 cation-
coordinated proteinogenic dipeptides. Different ligand atoms are distinguished by different-colored curves (red: O, blue: N,
orange: S), as noted in the following ﬁgures.
15/21

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
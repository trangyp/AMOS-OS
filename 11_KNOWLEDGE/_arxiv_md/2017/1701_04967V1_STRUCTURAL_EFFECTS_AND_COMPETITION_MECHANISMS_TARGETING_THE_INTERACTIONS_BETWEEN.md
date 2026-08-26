---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1701.04967v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1701.04967v1_Structural_Effects_and_Competition_Mechanisms_Targeting_the_Interactions_between

> Source: 1701.04967v1_Structural_Effects_and_Competition_Mechanisms_Targeting_the_Interactions_between.pdf

> Pages: 9

---


## Page 1


arXiv:1701.04967v1  [q-bio.MN]  18 Jan 2017
Structural Eﬀects and Competition Mechanisms Targeting the Interactions between
p53 and Mdm2 for Cancer Therapy
Shuxia Liu,1 Yizhao Geng,2 and Shiwei Yan1, 3, ∗
1College of Nuclear Science and Technology, Beijing Normal University, Beijing 100875, China
2School of Science, Hebei University of Technology, Tianjin 300401, China
3Beijing Radiation Center, Beijing 100875, China
(Dated: August 6, 2018)
About half of human cancers show normal TP53 gene and aberrant overexpression of Mdm2
and/or MdmX. This fact promotes a promising cancer therapeutic strategy which targeting the
interactions between p53 and Mdm2/MdmX. For developing the inhibitors to disrupt the p53-
Mdm2/MdmX interactions, we systematically investigate structural and interaction characteristics
of p53 and inhibitors with Mdm2 and MdmX from atomistic level by exploiting stochastic molecular
dynamics simulations. We ﬁnd that some speciﬁc α helices in Mdm2 and MdmX structure play key
role in their bindings with inhibitors and the hydrogen bond formed by residue Trp23 of p53 with
its counterpart in Mdm2/MdmX determines dynamical competition processes of the disruption of
Mdm2-p53 interaction and replacement of p53 from Mdm2-p53 complex in vivo.
We hope that
the results reported in this paper provide basic information for designing functional inhibitors and
realizing cancer gene therapy.
PACS numbers: 89.75.-k, 82.39.Rt, 87.15.km, 87.15.ap
Keywords: p53; MdmX; Mdm2; molecular dynamics simulation; inhibitors; cancer therapy
I.
INTRODUCTION
p53, a tumor suppressor protein, is the guardian of
the genome and plays a crucial role in the regulation of
cell cycle, apoptosis, DNA repair and angiogenesis [1].
p53 concentration increase and, thus, cause cell cycle ar-
rest or apoptosis response to the signal of DNA damage.
The activation of p53 can also activate another kind of
protein, Mdm2, which negatively regulate the concen-
tration of p53. In normal cells, both concentrations of
Mdm2 and p53 are low that provide growth advantage
to cells.
However, about half of human cancers show
normal TP53 gene and aberrant overexpression of Mdm2
and/or MdmX [2] that inhibit the activation of p53. This
fact provides a potent strategy for cancer therapy, i.e.
restoration the activity of p53 by inhibitors which can
occupy the p53-binding site of Mdm2 and inhibit the in-
teraction of p53 and Mdm2.
Once freed from Mdm2,
p53 rapidly accumulates in the nuclei of cancer cells, ac-
tivates p53 target genes and the p53 pathway, resulting
in cell-cycle arrest and apoptosis [3–5].
In history, it has been diﬃcult to develop small-
molecule inhibitors of nonenzyme protein-protein inter-
actions [3]. Protein-protein interactions usually involve
large and ﬂat surfaces that are diﬃcult to break by low
molecular weight compounds [6, 7]. However, the crystal
structure of Mdm2 bound to a peptide from the transacti-
vation domain of p53 has revealed that Mdm2 possesses
a relatively deep hydrophobic pocket that is ﬁlled pri-
marily by three side chains from the helical region of the
peptide [4]. The existence of such a well-deﬁned pocket
∗Email address:yansw@bnu.edu.cn
on the Mdm2 molecule raised the expectation that com-
pounds with low molecular weights could be found that
would block the interaction of Mdm2 with p53.
In terms of the characteristic of p53 binding to Mdm2,
the design of inhibitors should follow the principle that
the inhibitor can model the Mdm2-binding site of p53
[5]. The interactions between p53 and Mdm2 are mainly
hydrophobic interactions and hydrogen bonds.
Three
residues of p53, Phe19, Trp23 and Leu26, have been
found essential for the binding between p53 and Mdm2
and they are inserted into a deep hydrophobic pocket
on the surface of the MDM2 molecule. These features
of interactions between p53 and Mdm2 should be main-
tained in the design of eﬃcient inhibitor. The interface
between p53 and Mdm2 is small that permits the de-
sign of relatively small inhibitors which have higher oral
bioavailability [8].
Recently, rational designing with molecular docking
and high throughput virtual screening approaches has
led to the generation of diversiﬁed set of small molecules
and peptides that can restore the activity of p53 [5, 9, 10].
In these inhibitors, Nutlin family is a kind of non-
polypeptide inhibitor which include Nutlin1, Nutlin2,
Nutlin3, RG7112 and et. al. [11]. One of these promis-
ing Mdm2 inhibitors is Nutlin3 which is currently under
clinical investigations. It has been shown that Nutlin3
can tightly combine to Mdm2 and eﬃciently inhibit the
p53-Mdm2 interaction [12].
Moreover, MdmX (Mdm4 in mice) is another negative
regulator of p53, control the stability and activity of p53
in a diﬀerent mechanism to Mdm2 [13]. MdmX is highly
homologous to Mdm2, with the diﬀerence that it does not
possess any ubiquitin ligase activity and does not cause
p53 degradation although it binds to the N-terminus of
p53 and suppresses p53 transcriptional activities [14].


## Page 2


2
However, even Mdm2 and MdmX are homologous pro-
teins with high degree of homolog especially in their
N-terminal p53 binding domain, existing inhibitors of
Mdm2-p53 have weak function on interactions of MdmX-
p53 that highly reduce the eﬀect of inhibitors in cancer
therapy. Some has suggested the importance to develop
dual small-molecule inhibitors of p53-Mdm2/p53-MdmX
interactions for the complete reactivation of p53 [15].
To this end, the structural characteristics and interac-
tion properties of inhibitor-Mdm2 and inhibitor-MdmX
should be systematically investigated. Consider the fact
that the currently used docking scoring functions are not
expected to consistently provide accurate predictions of
the protein-ligand binding free energies for all of the
protein-ligand binding systems and are diﬃcult to ac-
count for the eﬀects of protein dynamics on the micro-
scopic binding during the simple docking process [16], we
will exploit molecular dynamics (MD) simulations that
can more reasonably account for the solvation eﬀects and
the dynamics of the protein-ligand binding. The MD sim-
ulations allow us to obtain a dynamically stable protein-
ligand binding mode associated with a stable MD trajec-
tory.
In this paper, we set up four models (p53-Mdm2, p53-
MdmX, Nutlin3-Mdm2 and Nutlin3-MdmX) to inves-
tigate the interactions between p53-Mdm2/MdmX and
between Nutlin3-Mdm2/MdmX by using MD simula-
tions through comparison of interactions between p53-
Mdm2/MdmX and between inhibitor-Mdm2/MdmX. We
will ﬁnd that the binding patterns of p53-Mdm2 and p53-
MdmX are same despite of some diﬀerences in the se-
quences and structures between Mdm2 and MdmX. Con-
trary to the tightly binding of Nutlin-3 to Mdm2, Nutlin-
3 can not bind to MdmX due to three factors arise from
such sequence diﬀerence between Mdm2 and MdmX.
II.
METHODS
In the modeling, complexes of p53-Mdm2 (PDB ID:
1YCR[4]), p53-MdmX (PDB ID: 3DAB[17]) and Nutlin3-
Mdm2 (PDB ID: 4HG7[18]) are extracted from the cor-
responding PDB ﬁles and solvated by explicit water
molecules, respectively.
The radius of water sphere is
10 ˚A larger than that of proteins. Because there is still
no crystal structure of Nutlin3-MdmX complex, we re-
place the Mdm2 molecule of 4HG7 by MdmX molecule
to construct Nutlin3-MdmX complex. This complex is
also buried by explicit water molecules.
The ionic concentration is 150mM. TIP3P[19] is used
to model water molecules. The protein-water complexes
are performed 30,000 steps energy minimization and then
performed 50 nanoseconds (ns) MD simulations. In our
MD simulations, α-carbons of ILE500, ASP67, LEU109
in MdmX and GLU25, VAL109 in Mdm2 are ﬁxed. The
models are made by VMD (version 1.9) [20] and MD sim-
ulations are performed by NAMD code (version 2.9)[21]
with the force ﬁle CHARMM [22] at constant temper-
ature of 310 K. The non-bonded Coulomb and van der
Waals interactions are calculated with a cutoﬀusing a
switching function starting at a distance of 13 ˚A and
reaching zero at 15 ˚A. The integration time step is 2
femtoseconds (fs).
III.
RESULTS AND DISCUSSIONS
A.
Comparison of sequences and structures
between MdmX and Mdm2
The functions of a bio-molecule are mainly determined
by its structure. As the starting point, we investigate the
sequence and structure diﬀerence between MdmX and
Mdm2. Indeed, the fact that existing Mdm2 inhibitors
have weaker binding aﬃnity for MdmX protein [23–25]
may indicate that some structural diﬀerence between
p53-binding domains of Mdm2 and MdmX play crucial
role in the binding properties of inhibitors to Mdm2 and
MdmX [12, 15].
In order to investigate such structural diﬀerences, we
compare the amino acid sequences and the tertiary struc-
tures of Mdm2/MdmX’s p53-binding domain, as shown
in Fig. 1. It is clear that the sequence identity degree
between N-termini of Mdm2 and MdmX is 53.9% and
the diﬀerences between them can be classiﬁed as three
types with changes of polarity (∼36.6%), hydrophobic-
ity (∼19.5%) and geometric structures of side chains
(∼39%).
There are four main regions in their back-
bone that show relatively large diﬀerence (Cαs’ distances
larger than 0.7 ˚A) among proteins, which are residues
Ser40 to Met50, Thr63 to Gln71, Ser78 to Phe86 and
Lys94 to Arg105 in Mdm2 as in Fig. 1b and Fig. 1c,
although the superposition of tertiary structures of cor-
responding region between Mdm2 and MdmX shows high
similarity. The segments of Ser40 to Met50 and Thr63
to Gln71 are loops in secondary structures which show
large ﬂexibility in water environment [26]. Therefore, the
structural diﬀerence between Mdm2 and MdmX caused
by sequence diﬀerences is on two helices, H3 (Mdm2;
residues 78-84 ) and H4 (Mdm2; residues 94-106), within
which, H4 is the key element of p53 binding sites of Mdm2
and MdmX.
Note here that, Mdm2 and MdmX’s α helix H1s show
obvious diﬀerence. From crystal structures of p53-Mdm2,
H1 of Mdm2 covers the p53-binding site of Mdm2, which
indicates the potential function of H1 in the binding of
two proteins. However, H1 of MdmX is absent in the
crystal structures and we can not identify its exact posi-
tion. We will discuss the roles of helix H1 further in the
following Sec. III C.
B.
Binding patterns of p53 to Mdm2 and MdmX
We also should keep in mind that structures and
functions of a bio-molecule are bridged by dynamical


## Page 3


3
FIG. 1. Comparison of sequences and structures of Mdm2/MdmX’s p53-binding sites. (a) Amino acid sequence alignment of
p53-binding sites of Mdm2 and MdmX. The diﬀerent amino acids are highlighted by diﬀerent colors which represent the three
types with changes of polarity(red), hydrophobicity (brown) and geometric structures (yellow). Abbreviations for the amino
acid residues are: A, Ala; C, Cys; D, Asp; E, Glu; F, Phe; G, Gly; H, His; I, Ile; K, Lys; L, Leu; M, Met; N, Asn; P, Pro; Q,
Gln; R, Arg; S, Ser; T, Thr; V, Val; W, Trp; Y, Tyr. (b) Superposition of crystal structures of N-termini of Mdm2 (red) and
MdmX (green). p53 is depicted with purple lines. The large structural diﬀerences appear on two loop regions and two α helices
(H3 and H4). (c) Every pairs of Cα distances of the structure in (b). The red region show the the correspondant pairs of Cα
whose distances are longer than 1 ˚A. Due to the uncertainty of H1 structure of MdmX, the comparison of distance between
two H1s are not shown.
process occuring from micro- to macro-scales.
In or-
der to clarify why the above-mentioned structural dif-
ference results in diﬀerent binding characteristics be-
tween p53-Mdm2/p53-MdmX and between inhibitor-
Mdm2/inhibitor-MdmX, we ﬁrst compare binding pat-
tern of p53 to Mdm2 and MdmX with MD simulation.
It is known that both Mdm2 and MdmX proteins can
bind to p53 with the same binding sites to negatively
control the concentration of p53 in cells [27, 28]. To iden-
tify the binding patterns of p53 with Mdm2 and MdmX,
we solvate the p53-Mdm2 and p53-MdmX complexes re-
spectively to perform MD simulations. After 50 ns MD
simulation, we obtained the stable complexes of p53’s N-
terminal helix and Mdm2/MamX’s p53-binding sites, as
shown in Fig. 2a, b and c.
The superposition of sta-
ble complex structures of p53-Mdm2 and p53-MdmX in-
dicates that the binding patterns of p53 to Mdm2 and
MdmX are same though there is some diﬀerence between
Mdm2 and MdmX’s sequences and structures.
We analyse structure of p53-Mdm2 and p53-MdmX
complexes respectively and ﬁnd that hydrophobic inter-
actions and hydrogen bond interactions are important
for the binding of p53 to Mdm2/MdmX (Same as in
[1, 4, 8, 30–33]). The hydrophobic surfaces of the p53
binding sites on Mdm2 and MdmX are similar, as in
Fig. 2c.
There are three hydrogen bonds formed be-
tween Phe19, Trp23 and Leu26 of p53 and Gln72/Gln71,
Leu54/Met53 and Val93/Val92 of Mdm2/MdmX, as
shown in Fig. 2d. For p53-Mdm2 complex, such three
hydrogen bonds formed by the hydrogen atom HE1 of
residue Trp23 of p53 and the oxygen atom O of residue
Leu54 of Mdm2 (HB1), the hydrogen atom HZ of residue
Phe19 of p53 and the oxygen atom of OE1 of residue
Gln72 of Mdm2 (HB2) and the hydrogen atom of H15
of residue Leu26 of p53 and the oxygen atom O of Val93
of Mdm2 (HB3), respectively. In these three hydrogen
bonds, the most important and stable one is the hy-
drogen bond between Trp23 of p53 and Leu54/Met53 of
Mdm2/MdmX. The same conclusion has been reported
in previous studies [5, 29]. The other two hydrogen bonds
are not such stable since they locate at the margin of
the complex models and expose to surrounding water
molecules.
It is worthwhile to note that our MD simulation has


## Page 4


4
FIG. 2. Simulation results of p53-Mdm2 and p53-MdmX complexes. (a) RMSD of protein-protein distance in p53-Mdm2 and
p53-MdmX complexes relative to their initial structures. After 5 ns, the two systems reach stable state. (b) Superposition of
two stable p53-Mdm2 (red) and p53-MdmX (blue) complex structures. (c) The hydrophobic surface of the p53-binding sites
of Mdm2 and MdmX. The volume of this site on Mdm2 are slightly smaller than that on MdmX. (d) The three hydrogen
bonds formed between PHE19, TRP23 and LEU26 of p53 protein and GLN72/GLN71, LEU54/MET53 and VAL93/VAL92 of
Mdm2/MdmX. The distances between O and H atoms of these hydrogen bonds are explicitly shown.
realized the situation in which Phe19, Trp23, and Leu26
residues of p53 inserts into the hydrophobic cavity in
Mdm2 to form hydrophobic interactions (Fig. 2b). The
total energy of three hydrogen bonds is −12.68 kcal/mol.
This reproduces the experimental observations and the-
oretical analyses reported in various literatures, i.e.,
[1, 4, 5, 8, 11, 29–33].
C.
Binding of Nutlin3 with MdmX and Mdm2
proteins
In this subsection, we analyse the binding character-
istics of Nutlin3 with MdmX and Mdm2 proteins. As
the same as in Sec. III B, we solvate the Nutlin3-Mdm2
and Nutlin3-MdmX complexes to perform MD simula-
tions.
To check the stability of this two systems, we
calculate the root mean square deviation (RMSD) of the
distance between Nutlin3 and Mdm2, as well as Nutlin3
and MdmX, respectively (shown in Fig. 3).
It can be
seen that Mdm2-Nutlin3 complex is fully stabilized after
∼5 ns and reaches a nearly stationary state. However,
MamX-Nutlin3 complex seems loosely combine and can
not become stable. This is consistent with the segmental
mutagenesis experiments reported in [12]. The snapshots
of MdmX-Nutlin3 complex conformations at various sim-
ulation moments in the trajectory are shown in Fig. 4,
which also shows that Nutlin3 can not bind to MdmX
stably.
We here note that, in Fig. 4, there is a large ampli-
tude motion of helix H3. In Fig. 4c and d, H3 is not a
standard helix structure. H3 locates in the bottom of the
binding pocket of MdmX and eﬀectively protects the in-
teractions between p53/Nutlin3 and the binding pocket
of MdmX. However, H3 itself is not so stable because
it is exposed to the surrounding water molecules. Two


## Page 5


5
0
10
20
30
40
50
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
10
 
 
RMSD (Å
)
Tim e (ns)
 Mdm2-Nutlin3
 Mdmx-Nutlin3
FIG. 3.
RMSD of distance between Nutlin3 and Mdm2
(black), as well as Nutlin3 and MdmX (red), respectively.
Mdm2-Nutlin3 reaches stable state after 5 ns.
However,
MdmX-Nutlin3 can not reach a stable structure.
hydrogen bonds (Asp79-Glu83 and Leu80-Leu84) which
maintain the helix structure show ﬂuctuation between
forming and opening states.
In this way, H3 exhibits
large amplitude motions in our simulation.
In order to understand above results deeper from atom-
istic level, we go further step to analyse the interactions
between Nutlin3 with Mdm2 and MdmX and the dy-
namical evolution of their complex structures. Since the
hydrogen bonding site of Nutlin3 is limit, Nutlin3 can
not form stable hydrogen bond with Mdm2 or MdmX
in our MD simulations.
Therefore, we propose that
the diﬀerent binding behavior of Nutlin3 to Mdm2 and
MdmX is caused by steric diﬀerences between Mdm2 and
MdmX underlying the sequence diﬀerences between these
two proteins. We superimpose the initial Mdm2-Nutlin3
and MdmX-Nutlin3 complexes (at the moment just af-
ter 30,000 steps energy minimization) of MD simulation
to analyse their conformational diﬀerence as in Fig. 5.
Based on such analysis, we summarize the reasons why
Nutlin3 can not bind to MdmX stably into the following
three aspects.
First, in our simulation models, Mdm2 has an extra
α helix (helix H1 in Fig. 1) formed by residues Gln18
to Ala21 (Fig. 5).
This α helix eﬀectively conﬁne the
movement of Nutlin3 molecule. However, the model of
MdmX-Nutlin3 complex lack this α helical structure. We
can not identify whether this α helix exists in the nat-
ural environment because there still lacks of the crystal
structure of MdmX-Nutlin3 complex.
To estimate the
function of this extra α helix in the binding of Nutlin3 to
Mdm2 or MdmX protein, we performed two MD simula-
tions as, (1) Mdm2-Nutlin3 complex in which this extra α
helix is deleted and (2) MdmX-Nutlin3 complex in which
this extra α helix exists. The RMSD values of Ntulin3
in these two simulations are shown in Fig. 6. It is clear
that when lacking of the extra α helix, Mdm2-Nutlin3
complex becomes relatively instable compared with that
when the extra α helix exists. Even in this case, such
instable binding of Nutlin3 to Mdm2 is much more sta-
ble than that of Nutlin3 to MdmX without the extra α
helix. When this helix exists, Nutlin3 can bind to MdmX
stably. These results convincingly suggest that the extra
α helix formed by Gln18 to Ala21 play a crucial role in
stabilizing Nutlin3 molecule when its binding to Mdm2
or MdmX proteins.
Second, the volume sizes of Nutlin3-binding sites of
Mdm2 and MdmX become diﬀerent upon binding with
Nutlin3. As discussed in Sec. III A, the hydrophobic sur-
faces of Mdm2 and MdmX are similar (shown in Fig. 2c).
However, seen from Fig. 5, α helices H2 and H4 which
form the p53 and inhibitor binding site of both Mdm2
and MdmX become diﬀerent upon Nutlin3 binding. This
diﬀerence results in the volume of inhibitor binding site of
MdmX being larger than that of Mdm2 and thus Nutlin3
can not binding tightly to MdmX. This conformational
diﬀerence between Mdm2 and MdmX’s H2 and H4 arises
from the sequence diﬀerences of two ends of H2 and H4
regions.
Third, when focusing on individual residues, we ﬁnd
that sequence diﬀerence at the following sites between
Mdm2 and MdmX also contribute to the diﬀerent bind-
ing behavior of Nutlin3 to Mdm2 and MdmX. The 96th
site of Mdm2 is histidine and the corresponding site of
MdmX is proline. The long side chain of His96 in Mdm2
can form stacking interaction with Nutlin3 and conﬁne
the movement of Nutlin3 molecule that further enhance
the stability of Nutlin3 when binding to Mdm2 (Fig. 3).
However, Pro95 in MdmX can not form such interactions
with Nutlin3.
At the end of this subsection, one may come to the fol-
lowing conclusions. There are various structural diﬀer-
ences between Nutlin3-Mdm2 and Nutlin3-MdmX com-
plex structures that result in the diﬀerent binding char-
acters of Nutlin3 to Mdm2 and MdmX. Such sequence-
based structural diﬀerences are in three α helices (H1,
H2 and H4) and one amino-acid site (His96 of Mdm2
and Pro95 of MdmX). One should suﬃciently consider
these diﬀerences of Mdm2 and MdmX for designing dual
inhibitors of Mdm2 and MdmX and enhancing the sta-
bility of inhibitors in its binding site of MdmX.
D.
Disruption of Mdm2-p53 interaction with small
molecules
From the static binding point of view, small molecules
like Nutlins can used to displace recombinant p53 protein
from its complex with Mdm2 as shown in Fig. 7. How-
ever, it is still unclear how such small molecules dynam-
ically to realize the disruption of Mdm2-p53 interaction
and replacement of p53 from Mdm2-p53 complex in vivo,
because, initially, inhibitors are far way from Mdm2-p53
complex in a water environment. This is an important
issue to understand the action principle of inhibitors.
In general, such process of disruption and replacement


## Page 6


6
FIG. 4. Snapshots of MdmX-Nutlin3 complex at 0(a), 10(b), 20(c), 30(d), 40(e) and 50(f) ns in MD simulation. Nutlin3
molecule can bind to the p53-binding site of MdmX but highly ﬂexible.
FIG. 5.
Superposition of stable Mdm2 -Nutlin3 (red) and
MdmX-Nutlin3 (blue) complex structures. H2 and H4 helices
of Mdm2 are close to each other relative to that of MdmX
upon binding with Nutlin3, that result in the diﬀerent bind-
ing volume of Mdm2 and MdmX. The His96 of Mdm2, cor-
responding to Pro95 of MdmX, covers the Nutlin3 in binding
state, which enhances the stability of inhibitor in the binding
site of Mdm2.
is dynamical and is aﬀected by the complex biological en-
vironment. In order to investigate whether Nutlin3 can
disturb the interaction between p53 and Mdm2 and com-
petes with p53 for binding to the extended hydrophobic-
cleft on the N-terminus of Mdm2, we put a Nutlin3
molecule far away from the p53-Mdm2 complex and run
the simulation for 180 ns. The whole system is in a water
environment with temperature 310K.
Five dynamical snapshots of the system are shown in
Fig. 8.
Initially at 0 ns, p53 and Mdm2 bind stably,
0
10
20
30
40
50
0
1
2
3
4
5
6
 
 
RMSD (Å
)
Tim e (ns)
 Mdm2-Nutlin3
 Mdmx-Nutlin3
FIG. 6. RMSD of Ntulin3 in Mdm2-Nutlin3 without the extra
α helix (black) and MdmX-Nutlin3 complex with the extra α
helix (red) .
and Nutlin3 is far away from the complex. As mentioned
above, in this initial case, there are three hydrogen bonds
HB1, HB2 and HB3.
Within in those three hydrogen
bonds, HB1 is the most stable one.
The interactions
between p53 and Mdm2 in this initial snapshot is the
same with the aforementioned simulations.
At 50 ns,
the interactions between p53 and Mdm2 are disturbed
slightly, and the Nutlin3 moves closer to the binding site
of Mdm2. HB1 is still stable, however, the other two hy-
drogen bonds (HB2 and HB3) has become rather weak
and then even break down. Till 100 ns, even HB1 also
become weak. At 150 ns through 180 ns, HB1 completely
breaks down and p53 moves further away from the bind-
ing cavity, compared with the snapshot at 100 ns.


## Page 7


7
FIG. 7. p53 and Nutlin3 binding to the extended hydrophobic
cleft on the N-terminus of Mdm2
Above results intuitively and dynamically reveals that
Nutlin3 can destroy the interactions between p53 and
Mdm2, go into the binding site of Mdm2 and ﬁnally
form complex with Mdm2 in expectation (we hope so if
the MD simulation ran long enough). This competition
mechanism is the most important basis for understanding
the inhibiting mechanism of small molecular inhibitors
and cancer therapeutic strategy. Meaningfully, this mi-
croscopic study may establish a linkage with the macro-
scopic study of p53 pathway with stochastic dynamics
[34–36], for example, providing the important parame-
ters like reaction rate constants and timescales.
IV.
CONCLUDING REMARKS
In this paper,
we systematically investigated the
structural characteristics and interaction properties of
inhibitor-Mdm2 and -MdmX at atomistic level and com-
pare it to the interaction of p53 with Mdm2 and MdmX
to explore the molecular basis of inhibition. It is revealed
that the structure of Mdm2 and MdmX are very similar
except some amino acids in two α helices H3 and H4 of
Mdm2 and/or MdmX. The formation of the complexes
of p53-MdmX and p53-Mdm2 rely on the hydrophobic
interactions and the hydrogen bond interactions.
We analyse the reason why Nutlin3 can combine to
Mdm2 rather than MdmX. Now it is clear that there
are three factors which inﬂuence the binding of Nut-
lin3 to Mdm2 and/or MdmX. First, an extra α helix
at the N-terminus of Mdm2 and/or MdmX is important
in the tightly binding of Nutlin3 to Mdm2 and MdmX.
Second, in the dynamical docking process of Nutlin3 to
Mdm2/MdmX, there are conformational changes in two
α helices H2 and H4 which results in the diﬀerent volume
of inhibitor-binding site of Mdm2 and MdmX. Third,
His96 in Mdm2 has an important role in the binding of
Nutlin3 to Mdm2.
From dynamical point of view, we have proven that
Nutlin3 can combine to Mdm2 and eﬀectively inhibit the
p53-Mdm2 interaction. Restoration the activity of p53 by
inhibiting the interaction of p53-Mdm2 and/or MdmX is
a promising and feasible method for cancer therapy, al-
though its true therapeutic potential is yet to be eluci-
dated.
It should be noted that the studies reported in this
paper is still in a very initial stage. The detailed infor-
mation needs to be veriﬁed through structural and dy-
namical investigation.
In order to get a suﬃcient un-
derstanding of the inhibiting mechanisms, one has to
combine methods, such as molecular docking method,
MD simulation, free energy analysis and even stochas-
tic network dynamics [37].
Molecular docking method
is expected to provide a reasonable initial structure of
inhibitor molecules for MD simulation.
Consider that
bio-molecules are generally in a most heterogenous, ex-
tremely dynamical, far from equilibrium and complex
ﬂuctuating environment, stochastic network dynamics is
needed to study p53 pathway [38]. It is no doubt that
such study is a challenging project. Let us leave it for
further eﬀorts.
ACKNOWLEDGEMENTS
This work is supported by the National Nature Science
Foundation of China (Grant Nos. 11675018, 10975019,
11605038, 11545014), Beijing Natural Science Founda-
tion (Grant No. 1172008), the Foundation of the Min-
istry of Personnel of China for Returned Scholars (Grant
No. MOP2006138) and the Fundamental Research Funds
for the Central Universities (Grant No. 2015KJJCB01)
[1] G.
M.
Popowicz,
A.
Domling,
T.
A.
Holak,
Angew. Chem. Int. Ed. 50, 2680(2011).
[2] X. Wang, J. Wang, X. Jiang,
J. Bio. Chem 286,
23725(2011).


## Page 8


8
FIG. 8. Dynamical snapshots of Nutlin3-Mdm2-p53 complex at various moment of MD simulation
[3] L. T. Vassilev, B. T. Vu, B. Graves, et al., Science 303,
844(2004).
[4] P. H. Kussie, S. Gorina, V. Marechal, et al., Science 274,
948(1996).
[5] P. Chene, Nat. Rev. Cancer 3, 102(2003).
[6] M. R. Arkin, J. A. Wells, Nat. Rev. Drug. Discov. 3,
301(2004).
[7] D. C. Fry, L. T. Vassilev, J. Mol. Med. 83, 955(2005).
[8] M. Bista, S. Wolf, K. Khoury, Structure 21, 2143(2013).
[9] K. K. Hoe, C. S. Verma, D. P. Lane, Nat. Rev. Drug.
Discov. 13, 217(2014).
[10] T. Saha, R. K. Kar, G. Sa, Prog. Biophys. Mol. Biol.
117, 250(2015).
[11] S. Tovar, B. Graves, K. Packman, et al., Cancer Res. 73,
2587(2013)
[12] L. Y. Qin, F. Yang, C. Zhou, et al., J. Am. Chem. Soc.
136, 18023(2014)
[13] U. M. Moll, O. Petrenko, Mol. Cancer Res. 1, 1001
(2003).
[14] R. Stad, N. A. Little, D. P. Xirodimas, et. al., EMBO
Rep. 2, 1029(2001).
[15] S. Shangary, S. Wang, Annu. Rev. Pharmacol. Toxicol.
49, 223(2009).
[16] M. D. M. AbdulHameed, A. Hamza, C. -G. Zhan, Annu.
J. Phys. Chem. B 110, 26365(2006).
[17] G. M. popowicz, A. Czarna, T. A. Holak, Cell Cycle 7,
2441(2008).
[18] M. E. M. Noble, B. Anil, C. Riedinger, et al., Acta Crys-
tallogr. Sect. D 69, 1358(2013).
[19] W. J. Jorgensen, J. Chandrasekhar, J. D. Madura, et al.,
J. Chem. Phys. 79, 926(1983).
[20] W. Humphrey, A. Dalke, K. Schulten, J. Mol. Graphics
14, 33(1996).
[21] J. C. Phillips, R. Braun, W. Wang, et al., J. Comput.
Chem 26, 1781(2005).
[22] A. D. MacKerell, D. Bashford, M. Bashford, et al., J.
Phys. Chem. 102, 3586(1998).
[23] S. Shangary, D. Qin, D. McEachern, et al., Proc. Natl.
Acad. Sci. USA 105, 3933(2008).
[24] B. Hu, D. M. Gilkes, B. Farooqi, et al., J. Biol. Chem.
281, 33030(2006).
[25] N. A. Laurie, S. L. Donovan, C. S. Shih, et al., Nature
444, 61(2006).
[26] V. Hariharan and W. O. Hancock, Cell. Mol. Bioeng. 2,
177 (2009).
[27] J. D. Oliner, K. W. Kinzler, P. S. Meltzer, D. L. George,
B. Vogelstein, Nature 358, 80(1992).
[28] J. D. Oliner, et al., Nature 362, 857(1993).
[29] S. Md. A. Rauf, H. T. C. A. D. Carpio, A. Miyamoto,
Med. Chem. Res. 23, 1998(2014).
[30] M. A. McCoy, J.J. Gesell, M.M. Senior, et al., Proc. Natl.
Acad. Sci. USA 100, 164(2003).
[31] S. A. Showalter, L. Bruschweiler-Li, E. Johnson, et al.,
J. Am. Chem. Soc. 130, 6472(2008).
[32] C. Y. Zhan, K. Varney, W. Y. Yuan, et al., J. Am. Chem.
Soc. 134, 6855(2012).
[33] A. C. Joerger, A. R. Fersht, Annu. Rev. Biochem. 77,
557(2008).
[34] K. M. ElSawy, C. S. Verma, T. L. Joseph, et al., Cell.
Cycle 12, 394(2013).
[35] L. Hernychova, P. Man, C. Verma, et al., Proteomics 13,
2512(2013).


## Page 9


9
[36] K. Puszynski, A. Gandolﬁand A. dOnofrio, PLOS Com-
putat. Biol. 10, e1003991(2014).
[37] S. X. Liu, Y. Z. Geng and S. W. Yan, to be published in
Prog. Biochem. Biophys.
[38] B. Liu, S. W. Yan and X. F. Gao, PloS ONE, 6,
e22487(2011) .

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
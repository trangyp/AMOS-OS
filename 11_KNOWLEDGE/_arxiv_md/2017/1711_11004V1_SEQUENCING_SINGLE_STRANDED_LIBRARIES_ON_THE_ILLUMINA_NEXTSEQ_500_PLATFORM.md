---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1711.11004v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1711.11004v1_Sequencing_single-stranded_libraries_on_the_Illumina_NextSeq_500_platform

> Source: 1711.11004v1_Sequencing_single-stranded_libraries_on_the_Illumina_NextSeq_500_platform.pdf

> Pages: 5

---


## Page 1


Sequencing single-stranded libraries on the Illumina
NextSeq 500 platform
Johanna L.A. Paijmans1,*, Sina Baleka1, Kirstin Henneberger1,
Ulrike H. Taron1, Alexandra Trinks2, Michael V. Westbury1,
Axel Barlow1,*
1. Institute for Biochemistry and Biology, University of Potsdam, Potsdam, Germany
2. IRI Life Sciences, Humboldt University Berlin, Berlin, Germany
* Corresponding Authors: paijmans.jla@gmail.com, axel.barlow.ab@gmail.com
Introduction
In recent years, a major contribution to the ﬁeld of palaeogenomics has been the development of a
novel Illumina R
⃝sequencing library preparation protocol based on single-stranded DNA (Gansauge
and Meyer, 2013; Gansauge et al., 2017; Meyer et al., 2012). This innovative method is particularly
suited for the recovery of extremely short DNA fragments typically found in ancient samples,
and is associated with greatly increased conversion eﬃciency compared to alternative methods
(e.g. Barlow et al., 2016)). Although the method was developed speciﬁcally for ancient DNA, it
has also found application in other ﬁelds such as medicine (e.g. prenatal testing from amniotic
ﬂuid (Karlsson et al., 2015) and transplantation medicine (Burnham et al., 2016)) and analysis of
preserved tissue samples (e.g. formalin-ﬁxed paraﬃn embedded cells; Stiller et al., 2016).
Single-stranded libraries have speciﬁc sequencing requirements. They require a custom read 1
sequencing primer. In addition, the use of dual index barcodes may also require a custom index
read 2 sequencing primer on some Illumina platforms. Finally, short library molecules associated
with ancient DNA templates are expected to behave diﬀerently during the annealing to the ﬂow
cell and subsequent cluster generation (bridge PCR), requiring optimisation of loading amounts to
obtain optimal and consistent cluster densities.
For the past 3 years, we have carried out sequencing of single-stranded libraries on the Illu-
mina NextSeq 500 sequencing platform at the Institute for Biochemistry and Biology, University
of Potsdam. Achieving consistent, high quality data outputs required considerable optimisation
and the design of a novel index 2 read sequencing primer (Table 1). We found that the short
library molecules typically generated from ancient DNA templates do not produce clusters on the
ﬂow cell as eﬃciently as modern, standard double-stranded libraries. In our experience, single-
stranded libraries beneﬁt from an increased loading quantity for sequencing (2.2 pM) compared
with double-stranded libraries (2.0 pM). Note that both these loading quantities are higher than
that typically recommended by Illumina, which is 1.8 pM (NextSeq System Denature and Di-
lute Libraries Guide, Document #15048776, January 2016). Furthermore, we have found that for
single-stranded libraries, cluster densities can be raised substantially above that recommended
by Illumina (recommended 129 - 165 k/mm2; https://www.illumina.com/systems/sequencing-
platforms/nextseq/speciﬁcations.html), greatly increasing sequencing yield with little reduction
in data quality (>200 k/mm2; Fig. 1).
We report our optimisations here. This document may be useful for other researchers wishing
to sequence single-stranded libraries on the NextSeq 500 platform. It does not replace the excel-
1
arXiv:1711.11004v1  [q-bio.OT]  29 Nov 2017


## Page 2


0
50
100
150
200
250
300
0
20
40
60
80
100
A.
Cluster density (k/mm2)
Clusters passing filters (%)
% clusters passing filter
% clusters > Q30
0
50
100
150
200
250
300
0
10
20
30
40
50
60
B.
Cluster density (k/mm2)
Data yield (Gb)
total yield (Gb)
total yield > Q30 (Gb)
Figure 1:
A) Percentage of clusters passing the ﬁlters (y-axis) versus the cluster density (x-axis)
for single-stranded libraries with a 2.2 pM loading quantity.
For the majority of runs, cluster
densities up to 250 k/mm2 still yield >80% passing both the chastity ﬁlter and the q30 ﬁlters. B)
Data yield (y-axis) versus cluster density (only taking single-stranded library sequencing runs on
75 cycle high-output kit into account). Data yield increases more or less linearly with increasing
cluster density, with only slight drop oﬀobserved around 200-250 k/mm2.
lent documentation provided by Illumina (links provided below), but rather serves as additional
information speciﬁc to single-stranded libraries. The original papers describing the library protocol
should also be studied in detail, and complement the information presented here.
• Single-stranded library protocol (Gansauge and Meyer, 2013)
• Custom primer guide
• Denature and diluting libraries guide
• Full NextSeq systems guide
Finally, these procedures are what works well in our laboratory. We provide no guarantees for
the success or failure of sequencing runs performed according to these recommendations. For any
further discussion readers are also welcome to contact the corresponding authors by email. We are
interested in combining our experiences with those of other people with a view to further optimise
sequencing single-stranded libraries on the NextSeq platform.
Sequencing read
Primer name
Sequence (5’-3’)
Reference
Read 1
CL72
ACA CTC TTT CCC TAC
ACG ACG CTC TTC C
Gansauge and Meyer (2013)
Index Read 2
Gesaﬀelstein*
GGA AGA GCG TCG TGT
AGG GAA AGA GTG T
This document
Table 1:
Custom oligos required for sequencing dual indexed single-stranded libraries on the
NextSeq 500. Oligos should be synthesized on a 0.05-µmole scale and puriﬁed by reverse-phase
HPLC. Stock concentrations should be 100 µM. See also Gansauge & Meyer 2013. * = the accepted
abbreviation for this oligo, as may be written on a microcentrifuge tube, is “G’stein”
2


## Page 3


Figure 2:
Tapestation Electropherogram report from a typical single-stranded library: approxi-
mately 5 nM, D1000 High-Sensitivity ScreenTape
Library pooling and quantiﬁcation using Qubit and Tapesta-
tion
1. The following recommendations for measuring the concentration and the modal fragment
size allow the molarity of the sequencing pool to be calculate. The target concentration is
4nM, but reliable sequencing can be performed using lower concentrations (Table 2). We ﬁnd
that a library with starting concentration less than 2.5 nM gives inconsistent results. Ideally,
libraries comprising the pool should be unimodal and free of any obvious heteroduplexes or
adapter/primer artefacts (Fig. 2). These factors will complicate library quantiﬁcation and
can lead to sub-optimal cluster densities.
2. We recommend using a dedicated pipette set that is regularly calibrated, as small inaccuracies
can lead to unreliable and inconsistent sequencing results.
3. Measure the concentration with the Qubit HS DNA Assay (Qubit 2.0), using at least 10 µl
of the sequencing library. Using less than 10 µl for quantiﬁcation leads to unreliable results
and thus unreliable cluster density.
4. We recommend using a 1:2 dilution of the Standard #2 from the Qubit BR Assay as quan-
tiﬁcation control; this should be roughly 50 ng/µl and will allow for a veriﬁcation of the
quantiﬁcation (use a diﬀerent stock than the one used in the measurement).
5. Run sequencing pool on a D1000 HS ScreenTape (Agilent Tapestation 2200; Fig.
2) to
estimate the modal fragment length
6. Calculate the molarity based on the modal fragment length and measured concentration.
Although the modal length will not represent the true average as the fragment length dis-
tribution for single-stranded libraries is typically skewed, we ﬁnd this to yield the most
consistent method of quantiﬁcation. We ﬁnd this approach is able to produce consistent and
predictable cluster densities without the need for qPCR.
3


## Page 4


Starting concentration
of library
Volume Library/NaOH
Volume HT1 Buﬀer
4
5
985
3.9
5.13
984.62
3.8
5.26
984.21
3.7
5.41
983.78
3.6
5.56
983.33
3.5
5.71
982.86
3.4
5.88
982.35
3.3
6.06
981.82
3.2
6.25
981.25
3.1
6.45
980.65
3
6.67
980
2.9
6.9
979.31
2.8
7.14
978.57
2.7
7.41
977.78
2.6
7.69
976.92
2.5
8
976
Table 2:
Volumes of libraries for denaturing and dilution stages in the NextSeq sequencing
protocol. The volumes follow the formula 20^1/nM.
References
Barlow, A., Fortes, G. M. G., Dalen, L., Pinhasi, R., Gasparyan, B., Rabeder, G., Frischauf, C.,
Paijmans, J. L. A., and Hofreiter, M. (2016). Massive inﬂuence of DNA isolation and library
preparation approaches on palaeogenomic sequencing data. bioRxiv. DOI:10.1101/075911.
Burnham, P., Kim, M. S., Agbor-Enoh, S., Luikart, H., Valantine, H. A., Khush, K. K., and Vlam-
inck, I. D. (2016). Single-stranded DNA library preparation uncovers the origin and diversity of
ultrashort cell-free DNA in plasma. Scientiﬁc Reports, 6:srep27859. DOI:10.1038/srep27859.
Gansauge, M.-T., Gerber, T., Glocke, I., Korlević, P., Lippik, L., Nagel, S., Riehl, L. M., Schmidt,
A., and Meyer, M. (2017). Single-stranded DNA library preparation from highly degraded DNA
using T4 DNA ligase. Nucleic Acids Research, 45(10):e79–e79. DOI:10.1093/nar/gkx033.
Gansauge, M.-T. and Meyer, M. (2013). Single-stranded DNA library preparation for the sequenc-
ing of ancient or damaged DNA. Nature Protocols, 8(4):737–748. DOI:10.1038/nprot.2013.038.
Karlsson, K., Sahlin, E., Iwarsson, E., Westgren, M., Nordenskjöld, M., and Linnarsson, S. (2015).
Ampliﬁcation-free sequencing of cell-free DNA for prenatal non-invasive diagnosis of chromoso-
mal aberrations. Genomics, 105(3):150–158. DOI:10.1016/j.ygeno.2014.12.005.
Meyer, M., Kircher, M., Gansauge, M.-T., Li, H., Racimo, F., Mallick, S., Schraiber, J. G.,
Jay, F., Prüfer, K., Filippo, C. d., Sudmant, P. H., Alkan, C., Fu, Q., Do, R., Rohland, N.,
Tandon, A., Siebauer, M., Green, R. E., Bryc, K., Briggs, A. W., Stenzel, U., Dabney, J.,
Shendure, J., Kitzman, J., Hammer, M. F., Shunkov, M. V., Derevianko, A. P., Patterson, N.,
Andrés, A. M., Eichler, E. E., Slatkin, M., Reich, D., Kelso, J., and Pääbo, S. (2012). A High-
Coverage Genome Sequence from an Archaic Denisovan Individual. Science, 338(6104):222–226.
DOI:10.1126/science.1224344.
4


## Page 5


Stiller,
M.,
Sucker,
A.,
Griewank,
K.,
Aust,
D.,
Baretton,
G.
B.,
Schadendorf,
D.,
and Horn,
S. (2016).
Single-strand DNA library preparation improves sequencing of
formalin-ﬁxed and paraﬃn-embedded (FFPE) cancer DNA.
Oncotarget, 7(37):59115–59128.
DOI:10.18632/oncotarget.10827.
5

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1711_11004v1_sequencing_single_stranded_libraries_on_the_illumina_nextseq_500_platform
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1711_11004V1_SEQUENCING_SINGLE_STRANDED_LIBRARIES_ON_THE_ILLUMINA_NEXTSEQ_500_PLATFORM.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

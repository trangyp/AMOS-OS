---
canon-group: reference
rscf-state: source-claim
arxiv_id: 0908.0649v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 0908.0649v1_sscMap__An_extensible_Java_application_for_connecting_small-molecule_drugs_using

> Source: 0908.0649v1_sscMap__An_extensible_Java_application_for_connecting_small-molecule_drugs_using.pdf

> Pages: 4

---


## Page 1


arXiv:0908.0649v1  [q-bio.QM]  5 Aug 2009
sscMap: An extensible Java application for connecting small-molecule drugs using
gene-expression signatures
Shu-Dong Zhang
MRC Toxicology Unit, Hodgkin Building, Lancaster Road, University of Leicester, Leicester, UK and
Centre for Cancer Research and Cell Biology (CCRCB), Queen’s University Belfast, Belfast, UK
Timothy W. Gant
MRC Toxicology Unit, Hodgkin Building, Lancaster Road, University of Leicester, Leicester, UK
Background: Connectivity mapping is a process to recognize novel pharmacological and toxico-
logical properties in small molecules by comparing their gene expression signatures with others in
a database. A simple and robust method for connectivity mapping with increased speciﬁcity and
sensitivity was recently developed, and its utility demonstrated using experimentally derived gene
signatures.
Results: This paper introduces sscMap (statistically signiﬁcant connections’ map), a Java ap-
plication designed to undertake connectivity mapping tasks using the recently published method.
The software is bundled with a default collection of reference gene-expression proﬁles based on the
publicly available dataset from the Broad Institute Connectivity Map 02, which includes data from
over 7000 Aﬀymetrix microarrays, for over 1000 small-molecule compounds, and 6100 treatment in-
stances in 5 human cell lines. In addition, the application allows users to add their custom collections
of reference proﬁles and is applicable to a wide range of other ’omics technologies.
Conclusions: The utility of sscMap is two fold. First, it serves to make statistically signiﬁcant
connections between a user-supplied gene signature and the 6100 core reference proﬁles based on
the Broad Institute expanded dataset. Second, it allows users to apply the same improved method
to custom-built reference proﬁles which can be added to the database for future referencing. The
software can be freely downloaded from http://purl.oclc.org/NET/sscMap.
I.
BACKGROUND
Interaction of a drug or chemical with a biological sys-
tem can result in a gene-expression proﬁle or signature
characteristic of the event.
Lamb et al were the ﬁrst
to propose using these data in connectivity mapping to
make connections between the pharmacological and toxi-
cological properties of small molecules [1]. The three key
components in the working of a connectivity map are: 1)
a collection of pre-built reference gene-expression proﬁles
that serves as a core database; 2) a query gene signature,
usually prepared by the user, which best characterizes a
compound-induced biological state and; 3) a similarity
metric to quantify the connection between a gene signa-
ture and a reference proﬁle. In a previous publication [2]
we presented a simple and robust method for connecting
small-molecule drugs using gene-expression signatures,
the utility of which was shown using three experimen-
tally derived gene signatures from independent studies
for HDAC inhibitors [3], estrogen [4], and immunosup-
pressive drugs [5], respectively.
Here in this paper we
describe sscMap, a Java application that implements the
method, and we focus on its utility and extensibility from
a user’s perspective.
II.
IMPLEMENTATION
The software was built using Java programming lan-
guage (Java Platform, Standard Edition 6). JFC/Swing
classes were used to provide a Graphical User Interface
(GUI) of the program. In designing the software, user
extensibility was considered to be an important feature.
To this end each individual reference proﬁle is stored as
a separate ﬁle on the disk. This setting greatly enhances
ﬂexibility and extensibility of the software, as it allows
users to supplement the default collection of reference
proﬁles, or to build custom collection of reference proﬁles
by following a simple contract speciﬁed in the README
ﬁle. In the execution of the program, a set of reference
proﬁles are ﬁrst loaded to memory and compared to all
the query gene signatures to calculate the related con-
nection scores and p-values, the memory is then released
and the program proceeds to load another set of reference
proﬁles from disk.
This memory management scheme
enables the program to handle an anticipated increasing
number of reference proﬁles at a moderate cost of speed.
If all the available reference proﬁles were residing in mem-
ory, the number of reference proﬁles allowed would soon
be limited.
III.
RESULTS
A.
The core database
The Broad Institute released Build 02 of their Con-
nectivity Map (http://www.broad.mit.edu/cmap/) with
an expanded dataset over the 01 version with more com-
pounds utilized. Using these data we constructed 6100
reference gene-expression proﬁles using the method de-
scribed in our previous report [2]. In brief the genes were


## Page 2


2
primarily sorted by the absolute value of log-ratios in de-
scending order, so that the most diﬀerentially expressed
gene has the highest rank. Thus sscMap comes with a de-
fault core database of 6100 reference proﬁles, each char-
acterizes a treatment instance as described in [1]. This
core database covers the treatment instances of over 1000
small-molecule compounds applied to 5 human cell lines.
So the primary utility of sscMap is for users who want
to compare their gene signatures to the reference pro-
ﬁles based on the Connectivity Map 02 dataset.
The
beneﬁts of the method implemented in this application
include a more principled statistical procedure [6, 7, 8],
eﬀective safeguards against false connections, and an in-
creased sensitivity. The sscMap program can be run in
two execution modes: as a command line program, or as
a GUI (Graphical User Interface) application. In the sim-
ple command line mode using the built-in core database
users can simply put their gene signature ﬁles into the
queries folder and run the application. Detailed instruc-
tions and guided tours on how to run the program in
GUI mode can be found in the accompanying README
ﬁle. For more advanced application the database can be
added to at the users discretion as described below.
B.
Extensibility: Building custom extensions
Users who want a greater capacity for comparison than
the built-in database can build up their own custom ref-
erence proﬁles and apply the same scoring scheme and
statistical testing procedures introduced in [2]. This sec-
tion brieﬂy describes how users can customize the appli-
cation.
A plain text ﬁle, parameters.ini for the command
line mode, or for-gui/default-parameters.ini for the GUI
mode, sets the key parameters used by the program,
e.g., where to ﬁnd the ref-ﬁles (reference gene-expression
proﬁles).
In the default settings, we speciﬁed reﬃles
as the default folder, where the 6100 reference proﬁles
are stored.
It is possible to supplement them by sim-
ply putting more similarly built ref-ﬁles into the default
folder. Users can also create a new directory, for example,
custom-reﬃles, and put all the custom ref-ﬁles there, and
then point the reference proﬁles folder to that directory,
either by editing the parameters.ini ﬁle for the command
line, or by browsing to the custom directory in the GUI
mode.
As an example, we have included with sscMap a folder
custom-example, which contains all the key components
of a customized extension to the application. Following
the example provided users should be able to build their
own extension. A more detailed description of the gen-
eral contracts for adding a custom collection of reference
proﬁles to sscMap can be found in the README ﬁle
accompanying the software.
C.
Flexibility: Treatment set deﬁnition
The sscMap software downloads with a default ref-
ﬁles
folder
containing
6100
pre-built
reference
ex-
pression proﬁles.
An
example
ref-ﬁle
is
azathio-
prine 0.1mM MCF7 338.ref.tab, which characterizes the
biological state of MCF7 cells treated with 0.1mM aza-
thioprine. The name of a typical ref-ﬁle is divided by the
underscore character , the default ﬁeld separator, into
4 ﬁelds: drug name, dose, cell type, and instance ID,
respectively. The program allows users to specify which
ﬁeld(s) to use for deﬁning a “treatment set” (A term
we use interchangeably with “reference set”, or simply
ref-set elsewhere). Our preferred choice for the default
ref-ﬁles is to use the 3 ﬁelds: drug name (ﬁeld 0), dose
(ﬁeld 1), and cell type (ﬁeld 2) together to deﬁne a treat-
ment set, meaning that only reference proﬁles with the
same drug, same dose, and same cell type should be re-
garded as forming a set in the set-level analysis.
The
original Connectivity Map uses only the drug name to
deﬁne a treatment set, disregarding possible diﬀerence in
dose and cell type. This tends to average out the distinct
characteristics attributable to the cell type or dose dif-
ference, making some set-level connections insigniﬁcant
or their interpretation diﬃcult. We described in the dis-
cussion section of [2] why it was preferable to use 3 ﬁelds
to deﬁne a treatment set. However, the program does
not force users to follow this preference. With sscMap,
users can choose whatever ﬁeld(s) they feel appropriate
to deﬁne a set. One extreme case is to use all the ﬁelds of
a ref-ﬁle name, and consequently each treatment set will
have only one treatment instance (such a treatment set
is called a singleton set) and this reduces to the instance-
level analysis.
In the custom-example folder, the custom ref-ﬁles
names are divided by a custom ﬁled separator, --, ie, two
hyphen characters, into 4 ﬁelds: drug name, dose, tissue
type, and time point, as in Drug2--LowDose--Tissue3-
-Day11.ref.tab.
Treatment sets are deﬁned using two
ﬁelds, Drug name (ﬁeld 0) and Tissue type (ﬁeld 2) in
this case. Thus the example here demonstrates the ﬂexi-
bility oﬀered by the application: users have the freedom
to choose their own ﬁeld separator, the number of ﬁelds,
and which ﬁelds to deﬁne a treatment set.
D.
Example 1: Using the default core collection of
ref-ﬁles
As an example of querying the default core database,
we used the ﬁve gene signatures previously reported
in [2].
Note that this default core database contains
6100 reference gene-expression proﬁles, which is a much-
expanded collection as compared to 453 in [2]. The con-
nection scores and p-values for the Estrogen gene sig-
nature are shown here in Figure 1 in graphical view.
The detailed tabulated results can be found as a tab ﬁle
(Estrogen.sig.sscmap.tab) in the results folder within the


## Page 3


3
FIG. 1: A screenshot of the sscMap program displaying the
volcano plot for the Estrogen gene signature. The x-axis is
for the standardized connection score, while the y-axis is for
−log10 p. The green horizontal line is for the pre-set threshold
p-value. Any data points above that line are considered as
statistically signiﬁcant. In the example shown in this ﬁgure,
the threshold p-value was set as 1/N = 1/3738.
TABLE I: The connections of the rat reference proﬁles with
a mouse gene signature. n, set size; s, set score; p, p value; σ,
the standard deviation of random scores; z = s/σ.
ref-set
n
s
p
σ
z
Drug2--Tissue2 3 0.0036 0.9716 0.0908 0.0394
Drug1--Tissue1 3 0.1553 0.0468 0.0790 1.9651
Drug1--Tissue2 3 0.0167 0.8638 0.0983 0.1694
Drug1--Tissue3 3 0.0221 0.7816 0.0799 0.2767
Drug2--Tissue1 3 -0.1934 0.0574 0.1020 -1.8953
Drug2--Tissue3 3 0.0648 0.3674 0.0709 0.9143
downloaded software.
E.
Example 2: Using a custom collection of ref-ﬁles
In the folder custom-example we provided a small col-
lection of 18 custom reference proﬁles, constructed using
Aﬀymetrix RAT230 2 microarray data. We then queried
this small database of custom reference proﬁles using 2
specially prepared gene signatures based on mouse cDNA
microarray data. To query the rat reference proﬁles using
mouse gene signatures, we ﬁrst converted the gene IDs
on the mouse array to the Aﬀymetrix Rat230 2 probeset
IDs, using the annotation ﬁle provided by Aﬀymetrix.
The biological contexts of these reference proﬁles and
gene signatures in this example are not directly relevant,
as we are here simply demonstrating the possibility of ex-
tending the sscMap software with custom reference pro-
ﬁles. In Table I, we list all the connections of the 6 refer-
ence sets, each containing 3 individual reference proﬁles,
to one of the mouse gene signatures.
IV.
CONCLUSIONS
The utility of sscMap is two fold. First, it serves to
make statistically signiﬁcant connections between a user-
supplied gene signature and the 6100 core reference pro-
ﬁles based on the Broad Institute expanded dataset. Sec-
ond, it allows users to apply the scoring scheme and sta-
tistical procedures described in [2] to custom-built ref-
erence proﬁles which can be added to the database for
future referencing.
V.
AVAILABILITY AND REQUIREMENTS
Project name: sscMap
Project home page: http://purl.oclc.org/NET/sscMap
Operating system(s): Platform independent
Programming language: Java
Other requirements: Java Runtime Environment 1.6
or later version is required to run the program.
License: None required for research and academic use.
Any restrictions to use by non-academics: For com-
mercial use, please contact the authors.
VI.
AUTHORS’ CONTRIBUTIONS
SDZ and TWG designed the study.
SDZ developed
the algorithm, implemented the method, and analyzed
the data. SDZ and TWG wrote the paper. All authors
read and approved the ﬁnal manuscript.
VII.
ACKNOWLEDGMENTS
We thank the reviewers for their constructive comments
and suggestions. Financial support for this project was
provided by the Medical Research Council UK (MRC)
and the work carried out with the support of all members
of the Systems Toxicology Group of the MRC Toxicology
Unit. SDZ thanks Qing Wen for helpful discussions on a
searching algorithm in the implementation of the appli-
cation.
[1] J. Lamb, E. D. Crawford, D. Peck, J. W. Modell, I. C.
Blat, M. J. Wrobel, J. Lerner, J.-P. Brunet, A. Subrama-
nian, K. N. Ross, et al., Science 313, 1929 (2006).
[2] S.-D. Zhang and T. W. Gant, BMC Bioinformatics 9
(2008).
[3] K. B. Glaser, M. J. Staver, J. F. Waring, J. Stender,
R. G. Ulrich, and S. K. Davidsen, Mol Cancer Ther 2,
151 (2003).
[4] J. Frasor, F. Stossi, J. M. Danes, B. Komm, C. R. Lyttle,
and B. S. Katzenellenbogen, Cancer Res 64, 1522 (2004).
[5] P. A. Horwitz, E. J. Tsai, M. E. Putt, J. M. Gilmore, J. J.
Lepore, M. S. Parmacek, A. C. Kao, S. S. Desai, L. R.
Goldberg, S. C. Brozena, et al., Circulation 110, 3815
(2004).
[6] L. Tian, S. A. Greenberg, S. W. Kong, J. Altschuler, I. S.
Kohane, and P. J. Park, PNAS 102, 13544 (2005).
[7] B. Efron and R. Tibshirani, Ann. Appl. Statist. 1, 107
(2007).
[8] J. J. Chen, T. Lee, R. R. Delongchamp, T. Chen, and
C.-A. Tsai, Bioinformatics 23, 2104 (2007).

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

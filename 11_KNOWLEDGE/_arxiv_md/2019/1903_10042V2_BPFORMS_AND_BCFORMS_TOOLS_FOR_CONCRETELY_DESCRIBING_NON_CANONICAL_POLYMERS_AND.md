---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1903.10042v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1903.10042v2_BpForms_and_BcForms__Tools_for_concretely_describing_non-canonical_polymers_and_

> Source: 1903.10042v2_BpForms_and_BcForms__Tools_for_concretely_describing_non-canonical_polymers_and_.pdf

> Pages: 21

---


## Page 1


BpForms and BcForms: Tools for concretely describing
non-canonical polymers and complexes to facilitate comprehensive
biochemical networks
Paul F. Lang1,2,3,*, Yassmine Chebaro1,2,4,*, Xiaoyue Zheng1,2,*, John A. P. Sekar1,2, Bilal
Shaikh1,2, Darren A. Natale5, and Jonathan R. Karr1,2,**
1Icahn Institute for Data Science and Genomic Technology, Icahn School of Medicine at
Mount Sinai, New York, NY 10029, USA
2Department of Genetics and Genomic Sciences, Icahn School of Medicine at Mount Sinai,
New York, NY 10029, USA
3Department of Biochemistry, Oxford University, South Parks Road, Oxford OX1 3QU, UK
4Institut de Génétique et de Biologie Moléculaire et Cellulaire, Institut National de la
Santé et de la Recherche Médicale, Centre National de la Recherche Scientiﬁque, Université
de Strasbourg, 67404, Illkirch, France
5Protein Information Resource, Georgetown University Medical Center, Washington, DC
20007, USA
*These authors contributed equally to this work
**Correspondence: karr@mssm.edu
August 26, 2019
Abstract
Although non-canonical residues, caps, crosslinks, and nicks play an important role in the function
of many DNA, RNA, proteins, and complexes, we do not fully understand how networks of non-
canonical macromolecules generate behavior. One barrier is our limited formats, such as IUPAC,
for abstractly describing macromolecules. To overcome this barrier, we developed BpForms and
BcForms, a toolkit of ontologies, grammars, and software for abstracting the primary structure of
polymers and complexes as combinations of residues, caps, crosslinks, and nicks. The toolkit can
help quality control, exchange, and integrate information about the primary structure of macro-
molecules into ﬁne-grained global networks of intracellular biochemistry.
Keywords
format; software; polymer; proteoform; complex; residue; modiﬁcation; crosslink; ﬁne-grained net-
work; genome-scale network
1. Background
A central goal in biology is to understand how networks of metabolites, DNA, RNA, proteins,
and complexes generate behavior. Non-canonical residues, caps, crosslinks, and nicks are essential
1
arXiv:1903.10042v2  [q-bio.BM]  3 Sep 2019


## Page 2


to these networks. For example, prokaryotic restriction/modiﬁcation systems use methylation to
selectively degrade foreign DNA, tRNA use pseudouridine to translate multiple codons, and signaling
networks use phosphorylation to encode information into the states of proteins.
Recent technical advances have enabled detailed information about individual DNA, RNA, and
protein modiﬁcations. For example, SMRT-seq can identify the locations of DNA methylations with
single-nucleotide resolution1 and mass-spectrometry can identify hundreds of protein modiﬁcations.2
Furthermore, several repositories have compiled extensive data about non-canonical residues and
crosslinks in DNA,3–6 RNA,7,8 and proteins,9–14 as well data about the subunit composition and
crosslinks of complexes.12,14–17 Despite this progress, it remains diﬃcult to integrate this information
into ﬁne-grained global networks of intracellular biochemistry, in part, because these resources use
chemically-ambiguous and incompatible formats.
Consequently, we still do not have a holistic
understanding of how non-canonical macromolecules help generate behavior.
Whole-cell (WC) models,18,19 which aim to predict phenotype from genotype by representing all
of the biochemical activity in cells, are a promising tool for integrating diverse information about
macromolecules into a holistic understanding of cellular behavior. However, it remains challeng-
ing to build ﬁne-grained, global biochemical networks, such as WC models, because we have few
tools for capturing the structures of non-canonical macromolecules and linking them together into
networks. For example, formats such as BioNetGen20 and the Systems Biology Markup Language
(SBML)21 are cumbersome for modeling post-transcriptional modiﬁcation because they have limited
capabilities to represent the primary structure of RNA.22,23 Abstractions of the primary structures
of macromolecules that can be combined with modeling frameworks such as SBML would provide
a signiﬁcant step toward ﬁne-grained global biochemical networks. Combined with software tools,
such abstractions could also facilitate the curation, exchange, and quality control of structural
information about macromolecules for a wide range of omics and systems and synthetic biology
research.
Currently, several formats have limited abilities to abstract the primary structures of non-canonical
polymers and complexes.
Molecular formats which represent each atom and bond, such as the
International Chemical Identiﬁer (InChI),24 the PDB format,25 and the Simpliﬁed Molecular-Input
Line-Entry System (SMILES),26 can represent non-canonical residues, caps, crosslinks, and nicks.
However, their ﬁne granularity is cumbersome for network-scale research. Omics and systems biology
formats, such as BioPAX,27 the Biological Expression Language (BEL),28 the MODOMICS nomen-
clature,7 the PRO notation,13 ProForma,29 and the Synthetic Biology Open Language (SBOL),30
use abstractions that are conducive to network-scale research. However, these formats have limited
abilities to represent non-canonical residues, caps, crosslinks and nicks, and they do not concretely
represent the primary structures of macromolecules.
Toward ﬁne-grained global networks of intracellular biochemistry, we developed BpForms-BcForms,
an open-source toolkit for abstractly representing the primary structure of polymers and complexes.
BpForms includes extensible alphabets of hundreds of DNA, RNA and protein residues; an ontol-
ogy of common crosslinks; and a human and machine-readable grammar for combining residues,
residue modiﬁcations, intra-chain crosslinks, and nicks into polymers. BcForms includes a human
and machine-readable grammar for combining polymers, small molecules, and inter-chain crosslinks
into complexes. Both tools include software for validating descriptions of macromolecules, calculat-
ing properties of macromolecules such as their formula, visualizing macromolecules, and exporting
macromolecules to molecular formats such as SMILES. Both tools are available as a web application,
REST API, command-line program, and Python library.
2


## Page 3


Here, we describe the toolkit and demonstrate how it can facilitate omics, systems modeling, and
synthetic biology. First, we describe the toolkit, including the alphabets of residues, the ontology
of crosslinks, the grammars, the software tools, and the user interfaces. Second, we describe how
BpForms and BcForms can be integrated with knowledge about pathways, kinetic models, and
genetic designs through formats such as BioPAX, CellML,31 SBML, and SBOL. Next, we describe
the advantages of the toolkit over existing formats for representing polymers and complexes and
existing alphabets of residues.
Lastly, we present multiple case studies that illustrate how the
toolkit can help researchers describe, quality control, exchange, and integrate diverse information
about macromolecules into networks. We anticipate that BpForms and BcForms will help facilitate
ﬁne-grained, global networks of cellular biochemistry.
2. Results
2.1. Toolkit for abstracting non-canonical polymers and complexes
The BpForms-BcForms toolkit includes several interrelated tools for describing, validating, visual-
izing, and calculating properties of the primary structure of DNA, RNA, proteins, and complexes
(Figure 1). Here, we describe the components of the toolkit including the abstractions and gram-
mars for polymers and complexes; the alphabets of residues; the ontology of crosslinks; the software
tools for quality controlling, analyzing, and visualizing macromolecules; the protocols for integrating
BpForms and BcForms with formats for network research; and the user interfaces.
Abstract representation of the primary structure of polymers and complexes. BpForms
represents polymers as a sequence of residues, a set of crosslinks, a set of nicks, and a Boolean
indicator of circularity (Figure 2B, D). BcForms represents complexes as a set of subunits and
a set of crosslinks (Figure 2A, C). Each subunit is represented by its molecular structure and
stoichiometry. The structure of each subunit can be described using BpForms or SMILES.
Residues. Each residue is represented by its molecular structure, a list of the atoms which can form
bonds with preceding and following residues, and a list of the atoms which are displaced by the
formation of these bonds (Figure 2E). These lists of atoms are optional to enable the toolkit to
represent internal nucleic and amino acids, as well as 3’ and 5’ caps. The toolkit can also capture
metadata and missing information about residues.
Crosslinks. Each crosslink is represented as lists of the atoms which can form a bond between
residues and the atoms which are displaced by the formation of these bonds (Figure 2F). The
toolkit represents each nick as a tuple of adjacent residues which are not bonded.
Alphabets of residues and ontology of crosslinks. The toolkit uses a hybrid approach to abstract the
molecular details of residues and crosslinks from the descriptions of macromolecules. The chemical
details of common residues and crosslinks are abstracted into alphabets of residues and an ontology of
crosslinks. Users can deﬁne additional residues and crosslinks within descriptions of macromolecules
or create custom alphabets and ontologies. This hybrid approach standardizes the representation
of common residues and crosslinks while enabling the toolkit to represent any residue or crosslink.
Coordinate system. The toolkit uses a structured coordinate system to describe the atoms involved
in each inter-residue bond and crosslink. The coordinate of each repeated subunit ranges from one
to the stoichiometry of the subunit. The coordinate of each residue is its position within the residue
sequence of its parent polymer. The coordinate of each atom is its position within the canonical
SMILES ordering of the atoms in its parent residue. Additional File 1.4 contains more information
3


## Page 4


about the coordinate system.
Examples. Boxes 1 and 2 illustrate the toolkit’s grammars for describing polymers and complexes,
and Figure 2 illustrates the chemical semantics of a homodimer encoded in the grammars. Additional
File 1.2 and the BpForms and BcForms websites provide detailed descriptions of the grammars and
additional examples. Additional File 1.3 contains formal descriptions of the grammars.
Alphabets of DNA, RNA, and protein residues. To support a broad range of research, Bp-
Forms includes the most extensive alphabets of DNA, RNA, and protein residues to date. The DNA
alphabet includes 422 deoxyribose nucleotide monophosphates and 3’ and 5’ caps derived from data
about DNA damage and repair from REPAIREtoire,4 structural data from the Protein Data Bank
Chemical Component Dictionary (PDB CCD),32 and chemoinformatics data from DNAmod.3 The
RNA alphabet includes 378 ribose nucleotide monophosphates and 3’ and 5’ caps derived from bio-
chemical data from MODOMICS33 and the RNA Modiﬁcation Database8 and structural data from
the PDB CCD. The protein alphabet has 1,435 amino acids and carboxy and amino termini derived
from biochemical data from RESID10 and structural data from the PDB CCD. The BpForms web-
site contains pages which display the residues in each alphabet. Additional File 1.5 describes how
we constructed the alphabets.
Ontology of crosslinks. To abstract the molecular structures of polymers and complexes, the
toolkit includes the ﬁrst ontology of crosslinks.
Currently, the ontology contains 36 common
crosslinks. We plan to continue to curate additional crosslinks as needed to represent WC models.
The BpForms website contains a page which displays the crosslinks in the ontology. Additional
File 1.6 describes how we constructed the ontology.
Syntactic and semantic validation of descriptions of macromolecules. To help quality
control information about macromolecules, the toolkit can verify the syntactic and semantic cor-
rectness of macromolecules encoded in BpForms and BcForms. First, the toolkit can verify that
textual descriptions of macromolecules are syntactically consistent with the BpForms and BcForms
grammars and identify any errors. Second, the toolkit can verify that macromolecules represented
by BpForms and BcForms are semantically consistent and identify any errors. For example, the
toolkit can identify pairs of adjacent amino acids that cannot form peptide bonds because the ﬁrst
amino acid does not have a carboxy terminus or because the second amino acid does not have an
amino terminus. Additional File 1.7 details the semantic validations implemented by the toolkit.
We anticipate that these quality controls will help researchers exchange reliable information and
assemble this information into high-quality networks.
Analyses of polymers and complexes. The toolkit can calculate several properties of macro-
molecules such as their primary structure, major protonation and tautomerization states, chemical
formula, molecular weight, and charge. We have begun to use these properties to quality control
WC models. For example, we are using the chemical formulae to verify that each reaction is element
and charge balanced, including reactions that represent transformations of macromolecules such as
the post-transcriptional modiﬁcation of tRNA.
The toolkit can also compare macromolecules to determine their equality or identify diﬀerences. We
plan to use this feature to implement automated procedures for merging models that share species
and reactions.
Molecular and sequence visualizations. To help analyze macromolecules, the toolkit can gen-
erate molecular and sequence visualizations of residues, caps, crosslinks, polymers, and complexes.
4


## Page 5


The molecular visualizations display each atom and bond and use colors to highlight features such
as individual residues, inter-residue and crosslink bonds, and the atoms that are displaced by the
formation of the inter-residue bonds (Figure S1A–C). The molecular visualizations can also display
the coordinate of each residue and atom. The sequence visualizations include interactive tooltips
that describe each non-canonical residue, crosslink, and nick (Figure S1D).
Export to other molecular and sequence formats. For compatibility with structural and
biochemical research, the toolkit can export BpForms and BcForms-encoded macromolecules to
molecular formats such as InChI, the PDB format, and SMILES. For compatibility with genomics
research, the toolkit can also export the canonical sequences of BcForms-encoded polymers to the
IUPAC/IUBMB format34 and FASTA documents.35
Integration with frameworks for network-scale research. BpForms and BcForms can fa-
cilitate network-scale research through integration with omics and systems and synthetic biology
frameworks such as BioPAX, CellML, SBML, and SBOL. Additional File 1.9 illustrates how Bp-
Forms and BcForms can be incorporated into these frameworks.
User interfaces. BpForms and BcForms each include four user-friendly interfaces: a web appli-
cation, a REST API, a command-line program, and a Python library.
2.2. Comparison with existing formats and alphabet-like resources
BpForms and BcForms are the ﬁrst abstractions that can represent the primary structure of any
DNA, RNA, protein, and complex, including non-canonical residues, caps, crosslinks, nicks, and cir-
cularity. The toolkit also contains the most extensive alphabets of DNA, RNA, and protein residues
and the ﬁrst ontology of concrete crosslinks. Furthermore, the toolkit has several innovative features
to facilitate research about non-canonical macromolecules: the toolkit includes a novel coordinate
system that makes it easy to address speciﬁc atoms in macromolecules, the toolkit uses a novel
combination of ontologies and inline deﬁnitions of residues and crosslinks to standardize the repre-
sentation of common residues and crosslinks while accommodating any residue or crosslink, and the
toolkit includes novel quality controls for abstractions of the primary structures of macromolecules.
Taken together, BpForms and BcForms are well-suited for network research. Here, we summarize
how BpForms and BcForms improve upon several existing resources for abstracting polymers and
complexes.
Comparison of BpForms with existing formats for polymers. BpForms is the ﬁrst for-
mat that can abstract the primary structure of DNA, RNA, and proteins, including non-canonical
residues, caps, crosslinks, nicks, and circularity. In contrast, molecular formats such as SMILES do
not abstract the structures of polymers, and abstract formats such as ProForma and network formats
such as BioPAX do not represent concrete molecular structures. BpForms also provides a unique
blend of the features of previous molecular and abstract formats: BpForms can capture missing in-
formation similar to ProForma, BpForms is human-readable like other abstract formats, BpForms
is machine-readable like molecular formats, BpForms is composable with network formats such as
SBML like molecular formats, and BpForms is backward compatible with the IUPAC/IUBMB for-
mat like other abstract formats. Additional File 1.11.1 and Table S1 provide a detailed comparison
of BpForms with several other formats.
Comparison of BpForms alphabets with existing databases. The BpForms alphabets are
the most extensive alphabets of DNA, RNA, and protein residues because they are based on struc-
tural, biochemical, and physiological data from several sources. In addition, the BpForms alphabets
and the PDB CCD are the only alphabets which consistently represent DNA, RNA, and protein
5


## Page 6


residues and which represent the inter-residue bonding sites of each residue, enabling residues to be
combined into concrete molecular structures. In contrast, DNAmod, REPAIRtoire, MODOMICS,
RESID, and the RNA Modiﬁcation Database each only represent DNA, RNA, or protein residues;
the residues in DNAmod, REPAIRtoire, MODOMICS, and the RNA Modiﬁcation Database are
hard to compose into polymers because they represent nucleobases and nucleosides rather than nu-
cleotides; and DNAmod, REPAIRtoire, MODOMICS, RESID, and the RNA Modiﬁcation Database
do not capture bonding sites. Additional File 1.11.2 and Table S2 provide a detailed comparison of
the BpForms alphabets with several other resources.
Comparison of the BpForms crosslinks ontology with existing resources. Several resources
contain information about crosslinks.
In particular, the UniProt controlled vocabulary of post-
translational modiﬁcations includes textual descriptions of over 100 types of crosslinks. In addition,
MOD, REPAIRtoire, and RESID indirectly represent crosslinks by representing crosslinked dimers
and trimers.
The BpForms ontology is the ﬁrst resource which directly represents the chemical structures of
crosslinks, enabling crosslinks to be composed into concrete structures. In contrast, MOD, RE-
PAIRtoire, and RESID represent crosslinks indirectly and the crosslinks in UniProt do not have
concrete chemical semantics.
Consequently, the crosslinks in MOD, REPAIRtoire, RESID, and
UniProt cannot be composed into concrete structures. Additional File 1.11.3 and Table S3 provide
a detailed comparison of the BpForms crosslinks ontology with these resources.
Comparison of BcForms with existing formats for complexes. Despite the importance
of complexes, only a few formats can represent complexes.
The PDB format is well-suited to
capturing the 3-dimensional structures of complexes.
BioPAX and SBOL can also capture the
subunit composition of complexes.
BcForms is the ﬁrst format which abstracts the primary structures of complexes including crosslinks.
In contrast, the PDB format has limited capabilities to abstract crosslinks, and BioPAX and SBOL
have limited abilities to represent stochiometric information and crosslinks. BcForms is also the
ﬁrst format which can be composed with formats for networks such as SBML. Additional File 1.11.4
and Table S4 provide a detailed comparison of BcForms with several other formats.
2.3. Case studies
We believe that the BpForms-BcForms toolkit can support a wide range of omics and systems and
synthetic biology research. Here, we illustrate how we have used the toolkit to improve the quality of
the PRO database of proteoforms; analyze the metabolic cost of tRNA modiﬁcation in Escherichia
coli; reﬁne, expand, a compose a model of MAPK signaling with models of other pathways; and
identify constraints on designing new strains of E. coli.
Proteomics: Quality control of the Protein Ontology. One of the goals of proteomics is to
characterize the proteoforms in cells. Toward a comprehensive catalog of proteoforms, the PRO
consortium has manually integrated several diﬀerent types of data into PRO, a database of 8,095
proteoforms. Because the consortium constructs PRO, in part, by hand, automated quality controls
could help the consortium identify and correct errors in PRO.
We have used BpForms quality control PRO. First, we encoded each entry in PRO into the BpForms
grammar and used the BpForms software to validate each entry. This identiﬁed several types of
syntactical and semantic errors. For example, we identiﬁed annotated processing sites that have
invalid coordinates that are greater than the length of the translated sequence of their parent protein.
6


## Page 7


We also identiﬁed modiﬁed residues whose structures are inconsistent with the translated sequences
of their parent proteins, such as a phosphorylated serine which is annotated at the position of a
tyrosine in the translated sequence of its parent. Second, the consortium corrected these errors.
These improvements will be published with the next release later this year.
To enable the consortium to continue to use BpForms to quality control PRO, we developed a
script which automates this analysis. Going forward, the consortium also plans to use BpForms
and BcForms to visualize and export proteoforms to molecular formats such as SMILES.
Systems biology: Analysis of the metabolic cost of prokaryotic tRNA modiﬁcation.
To achieve WC models, we must integrate information about all of the processes in cells and their
interactions. Here, we illustrate how BpForms can help integrate information about the interaction
between the RNA modiﬁcation and metabolism of E. coli and identify gaps in models.
First, we estimated the abundance of each tRNA from the total observed abundance of tRNA36,37
and the observed relative abundance of each tRNA.38 Second, we estimated the synthesis rate of
each tRNA from the estimated abundance of each tRNA, the observed half-life of tRNAAsn,39 and
the observed doubling time of E. coli in glucose media.40 Third, we used BpForms to analyze
the curated modiﬁcations of each tRNA.7 Fourth, we estimated the total synthesis rate of each
modiﬁcation from the synthesis rate and modiﬁcation of each tRNA (Figure 3).
This analysis revealed that E. coli tRNA contain 26 modiﬁed residues, and that the ﬁve most abun-
dant residues account for 73.8% of all modiﬁcations. Next, we tried to use the iML1515 metabolic
model,41 one of the most comprehensive models of cellular metabolism, to analyze the impact of
these modiﬁcations on metabolism and understand how E. coli allocates its limited metabolic re-
sources among these modiﬁcations. This analysis revealed that the model only represents one of
the modiﬁed residues (9U, pseudouridine). Therefore, the model must be expanded to capture the
metabolic cost of tRNA modiﬁcation.
Systems biology: Systematic identiﬁcation of gaps in the Kholodenko model of MAPK
signaling. The Kholodenko model of the eukaryotic MAPK signaling cascade42 describes how the
cascade transduces extracellular signals for growth, diﬀerentiation, and survival into the phosphory-
lation state of MAPK. However, the model does not account for factors such as the cell’s nutritional
status.
Toward a more holistic model of the cascade, we used BpForms to systematically identify gaps in
the Kholodenko model and opportunities to merge the model with models of other pathways. First,
we obtained an SBML-encoded version of the model. Second, we determined the speciﬁc proteins
represented by the model. We had to do this manually because Kholodenko did not report this
information. Third, we curated the sequences and post-translational modiﬁcations of the species
represented by the model from UniProt and encoded them into BpForms (Figure 4A). Fourth, we
embedded these BpForms representations into the SBML representation of the model. We believe
that the BpForms annotations make the model more understandable.
Fifth, we used the BpForms annotations to systematically identify missing proteoforms that could
help the model better explain how the MAPK pathway transduces signals. Speciﬁcally, we used
BpForms to identify two missing combinations of the individual protein modiﬁcations represented
by the model and four missing reactions that involve these species (Figure 4B). These additional
species and reactions could help the model better capture the kinetics of MAPKK and MAPKKK
activation and deactivation and, in turn, better capture how the pathway transduces signals.
7


## Page 8


Next, we used the BpForms annotations to identify opportunities to merge the Kholodenko model
with models of other signaling cascades.
Speciﬁcally, we searched BioModels for other models
that represent similar proteoforms. This analysis identiﬁed several models that represent EGFR,
PI3K, S6K, and the transcriptional outputs of the MAPK pathway that could be composed with
the Kholodenko model. Furthermore, this combination of models enabled us to identify emergent
combinations of proteoforms that are missing from the individual models (Figure 4C).
Lastly, to identify opportunities to merge the Kholodenko model with a model of metabolism,
we used the BpForms annotations to systematically identify unbalanced reactions with missing
metabolites. This analysis identiﬁed four missing species that, if added to the Kholodenko model,
would make the model composable with models of metabolism (Figure 4D).
Synthetic biology: Systematic identiﬁcation of design constraints. A promising way to
engineer cells is to combine naturally-occurring parts, such as genes that encode metabolic enzymes,
in an accommodating host, such as E. coli.
However, there are numerous potential barriers to
transforming parts into other cells. For example, parts that require post-translational modiﬁcations
cannot be transformed into cells which cannot synthesize the modiﬁcations. Currently, it is diﬃcult
to identify such design constraints because we have limited tools to describe the dependencies of
parts. Here, we illustrate how BpForms can systematically identify potential ﬂaws in the design of
a novel strain of E. coli due to missing post-translational modiﬁcation machinery.
First, we used the PDB and BpForms to identify all of the modiﬁcations that have been observed
in E. coli. Second, we used the PDB and BpForms to identify modiﬁcations which have never been
observed in E. coli and the proteins which contain these modiﬁcations. For example, we found
that proteins that contain 4-hydroxproline (PDB CCD: HYP), such as collagen (UniProt: P02452),
potentially cannot be transformed into E. coli. Third, we used the literature to conﬁrm the absence
of these modiﬁcations from E. coli.43–45 Table S5 lists the most common modiﬁcations which could
constrain the transformation of proteins into E. coli.
Bioengineers could use this information to more reliably modify strains by limiting designs to
post-translationally compatible proteins or by co-transforming parts with their requisite post-
translational modiﬁcation machinery. Furthermore, the synthetic biology community could make
such information more accessible for learning design rules by incorporating this information into
parts repositories such as SynBioHub.46 This information would enable these repositories to function
as dependency management systems for synthetic organisms, analogous to the Advanced Package
Tool (APT) for Ubuntu packages.
3. Discussion
3.1. Community adoption as a common toolkit
Realizing the full potential of BpForms and BcForms as formats for the primary structures of
macromolecules will require acceptance by the omics, systems biology, and synthetic biology com-
munities. We have begun to solicit users by submitting the BpForms and BcForms grammars to the
FAIRsharing registry of standards and the EDAM ontology of formats, contributing the alphabets
of residues and the ontology of crosslinks to BioPortal, proposing a protocol for using BpForms
with SBOL, and helping the PRO consortium use BpForms to represent proteoforms. To further
encourage community adoption, we plan to encourage the developers of central repositories of DNA,
RNA, and protein modiﬁcations such as MethSMRT,5 the PDB, and RMBase6 to export their data
in BpForms format. We also plan to stimulate discussion among the BioPAX, CellML, and SBML
8


## Page 9


communities about formalizing our integrations of BpForms and BcForms with their formats. Ad-
ditionally, we also plan to use the grammars to generate parsers for other languages, such as C++,
to help developers incorporate BpForms and BcForms into software tools.
3.2. Community adoption as standards
Because BpForms and BcForms aim to help researchers exchange information, we believe that the
alphabets of residues, the ontology of crosslinks, and the grammars should ultimately become com-
munity standards. To start, we encourage the community to contribute to BpForms and BcForms
via Git pull requests. Going forward, we would like these resources to be governed by the community
through an organization such as the Computational Modeling in Biology Network (COMBINE).47
3.3. Integrating closed chemical representations with open informatics represen-
tations to enable WC models
BpForms and BcForms achieve abstract descriptions of macromolecules by combining a closed,
deﬁned grammar with open, extensible ontologies of residues and crosslinks. This hybrid approach
enables BpForms and BcForms to integrate diverse data into chemically-concrete descriptions of a
wide range of macromolecules. Achieving WC models swimilarly requires integrating heterogeneous
data about a wide range of processes from a wide range of methods and sources into physically-
concrete kinetic simulations. Consequently, we believe that hybrid open-closed approaches such
as BpForms and BcForms will be essential for WC modeling.
For example, we are developing
a hybrid methodology that enables chemically-concrete coarse-grained simulations by using ﬁne-
grained reactions to describe the chemical semantics of coarse-grained reactions.
3.4. Enabling multiscale models that bridge structural information with net-
works
We have begun to use BpForms and BcForms to describe the chemical semantics of the species
represented by network models. Going forward, we also plan to use BpForms and BcForms to help
network models capture ﬁner-grained mechanisms that involve combinatorial interactions, such
as how methylation impacts transcription factor-DNA binding. To do this, we are developing a
generalized rule-based modeling framework which encapsulates properties such as primary structures
into species and links these properties to reactions and rate laws. We anticipate that this framework,
together with BpForms and BcForms, will make it easier to build ﬁne-grained kinetic models of
complex processes such as transcriptional backtracking, ribosomal queuing, and tmRNA ribosomal
rescuing and combine them into WC models.
4. Conclusions
The BpForms-BcForms toolkit abstracts the primary structure of polymers and complexes, in-
cluding non-canonical residues, caps, crosslinks, nicks, and several types of missing information.
Furthermore, the toolkit standardizes the representation of common residues and crosslinks while
extensibly accommodating any residue and crosslink by supporting both centrally and user-deﬁned
abstractions of residues and crosslinks. The toolkit includes the most extensive alphabets of hun-
dreds of DNA, RNA, and protein residues; the ﬁrst ontology of common crosslinks; an intuitive
coordinate system for the subunits, residues, and atoms in macromolecules; the ﬁrst human and
machine-readable grammar for composing residues, caps, crosslinks, and nicks into polymers and
complexes; and user-friendly web, REST, command-line and Python interfaces. The toolkit is back-
ward compatible with the IUPAC/IUBMB format to maximize compatibility with existing bioin-
formatics tools and knowledge. The toolkit can also be integrated with frameworks for network
9


## Page 10


research such as BioPAX, CellML, SBML, and SBOL.
We anticipate that BpForms and BcForms will be valuable tools for omics, systems biology, and
synthetic biology. First, the tools can help researchers precisely communicate information about
macromolecules. For example, the tools can help experimentalists communicate observations of
proteoforms and help bioinformaticians exchange information among databases of polymers and
complexes.
Similarly, the tools can make models and genetic designs more understandable by
capturing the semantic meaning of the species represented by models and capturing the structures
of the parts of synthetic organisms. For example, BpForms could describe proteins produced by
expanded genetic codes.
The tools can also help quality control information about macromolecules. For example, the tools
could help researchers ﬁnd errors in reconstructed proteoforms such as inconsistencies between the
modiﬁed and translated sequences, merge duplicate entries in databases of proteoforms, and identify
gaps and element imbalances in models.
In addition, BpForms and BcForms can help researchers integrate structural, epigenomic, tran-
scriptomic, and proteomic information about macromolecules.
For example, the tools can help
researchers integrate observations of individual protein modiﬁcations into descriptions of entire pro-
teoforms. The tools can also help researchers integrate databases of modiﬁed proteins into a model of
post-translational processing, combine the model with models of other processes to create WC mod-
els, and reﬁne the model by identifying missing combinations of protein states. Similarly, the tools
can help bioengineers design biochemical networks by identifying parts that must be co-transformed
with post-transcriptional and post-translational modiﬁcation machinery.
5. Methods
We designed BpForms and BcForms as separate, but interrelated tools, to provide users light-
weight tools for the distinct use cases of describing polymers and complexes.
We implemented
the toolkit using Python, ChemAxon Marvin, Flask-RESTPlus, Lark, Open Babel,48 YAML Ain’t
Markup Language, and Zurb Foundation. Additional File 1.10 provides more information about
the implementation.
Declarations
Availability of data and materials
The web applications are located at https://bpforms.org and https://bcforms.org, the REST APIs
are located at https://bpforms.org/api and https://bcforms.org/api, the command-line programs
and Python libraries are available from PyPI, and the code and ontologies are available at https://
github.com/KarrLab.
BpForms and BcForms are available open-source under the MIT license.
Optionally, a license
for ChemAxon Marvin is needed to calculate protonation and tautomerization states and generate
molecular visualizations. Free licenses are available for academic researchers.
BpForms and BcForms are platform independent.
The installation of BpForms and BcForms
requires Python 3.6 or higher, Open Babel, and, optionally, ChemAxon Marvin. A Docker image
with these dependencies is available at http://dockerhub.com/u/karrlab.
10


## Page 11


Documentation, including installation instructions, is available at https://docs.karrlab.org. Inter-
active Jupyter notebook tutorials are available at https://sandbox.karrlab.org.
This article refers to versions 0.0.9 of BpForms and 0.0.2 of BcForms.
Competing interests
The authors declare that they have no competing interests.
Funding
This work was supported by the National Institutes of Health [grant numbers R35 GM119771, P41
EB023912]; the National Science Foundation [grant number 1649014]; and the Engineering and
Physical Sciences Research Council [grant number EP/L016494/1].
Authors’ contributions
PFL, YC, XZ, DAN, and JRK built the alphabets of residues and the ontology of crosslinks. XZ,
BS, and JRK developed the software. XZ, DAN, and JRK developed the case studies. PFL, YC,
JAPC, and JRK wrote the manuscript. All authors read and approved the ﬁnal manuscript.
Acknowledgements
We thank Chris Myers and Jacob Beal for helpful discussion about integrating BpForms with SBOL
and Nicola Hawes for help designing Figure 1.
References
1.
Plongthongkum, N., Diep, D. H. & Zhang, K. Advances in the proﬁling of DNA modiﬁcations:
cytosine methylation and beyond. Nat. Rev. Genet. 15, 647–661 (2014).
2.
Toby, T. K., Fornelli, L. & Kelleher, N. L. Progress in top-down proteomics and the analysis
of proteoforms. Annu. Rev. Anal. Chem. 9, 499–519 (2016).
3.
Sood, A. J., Viner, C. & Hoﬀman, M. M. DNAmod: the DNA modiﬁcation database. J.
Cheminform. 11, 30 (2019).
4.
Milanowska, K., Krwawicz, J., Papaj, G., Kosiński, J., Poleszak, K., Lesiak, J., Osińska, E.,
Rother, K. & Bujnicki, J. M. REPAIRtoire–a database of DNA repair pathways. Nucleic Acids
Res. 39, D788–D792 (2010).
5.
Ye, P., Luan, Y., Chen, K., Liu, Y., Xiao, C. & Xie, Z. MethSMRT: an integrative database
for DNA N6-methyladenine and N4-methylcytosine generated by single-molecular real-time
sequencing. Nucleic Acids Res. 45, D85–D89 (2017).
6.
Xuan, J.-J., Sun, W.-J., Lin, P.-H., Zhou, K.-R., Liu, S., Zheng, L.-L., Qu, L.-H. & Yang, J.-H.
RMBase v2.0: deciphering the map of RNA modiﬁcations from epitranscriptome sequencing
data. Nucleic Acids Res. 46, D327–D334 (2017).
7.
Boccaletto, P., Machnicka, M. A., Purta, E., Piątkowski, P., Bagiński, B., Wirecki, T. K.,
de Crécy-Lagard, V., Ross, R., Limbach, P. A., Kotter, A., et al. MODOMICS: a database of
RNA modiﬁcation pathways. 2017 update. Nucleic Acids Res. 46, D303–D307 (2017).
8.
Cantara, W. A., Crain, P. F., Rozenski, J., McCloskey, J. A., Harris, K. A., Zhang, X., Vendeix,
F. A., Fabris, D. & Agris, P. F. The RNA Modiﬁcation Database, RNAMDB: 2011 update.
Nucleic Acids Res. 39, D195–D201 (2010).
11


## Page 12


9.
Montecchi-Palazzi, L., Beavis, R., Binz, P.-A., Chalkley, R. J., Cottrell, J., Creasy, D., Shofs-
tahl, J., Seymour, S. L. & Garavelli, J. S. The PSI-MOD community standard for representation
of protein modiﬁcation data. Nat. Biotechnol. 26, 864–866 (2008).
10.
Garavelli, J. S. The RESID Database of Protein Modiﬁcations as a resource and annotation
tool. Proteomics 4, 1527–1533 (2004).
11.
Hornbeck, P. V., Kornhauser, J. M., Latham, V., Murray, B., Nandhikonda, V., Nord, A.,
Skrzypek, E., Wheeler, T., Zhang, B. & Gnad, F. 15 years of PhosphoSitePlus R⃝: integrating
post-translationally modiﬁed sites, disease variants and isoforms. Nucleic Acids Res. 47, D433–
D441 (2018).
12.
Rose, P. W., Bi, C., Bluhm, W. F., Christie, C. H., Dimitropoulos, D., Dutta, S., Green, R. K.,
Goodsell, D. S., Prlić, A., Quesada, M., et al. The RCSB Protein Data Bank: new resources
for research and education. Nucleic Acids Res. 41, D475–D482 (2012).
13.
Natale, D. A., Arighi, C. N., Blake, J. A., Bona, J., Chen, C., Chen, S.-C., Christie, K. R.,
Cowart, J., D’Eustachio, P., Diehl, A. D., et al. Protein Ontology (PRO): enhancing and scaling
up the representation of protein entities. Nucleic Acids Res. 45, D339–D346 (2016).
14.
UniProt Consortium et al. UniProt: the universal protein knowledgebase. Nucleic Acids Res.
45, D158–D169 (2017).
15.
Meldal, B. H. M., Bye-A-Jee, H., Gajdoš, L., Hammerová, Z., Horáčková, A., Melicher, F.,
Perfetto, L., Pokorn`y, D., Lopez, M. R., Türková, A., et al. Complex Portal 2018: extended
content and enhanced visualization tools for macromolecular complexes. Nucleic Acids Res.
47, D550–D558 (2018).
16.
Giurgiu, M., Reinhard, J., Brauner, B., Dunger-Kaltenbach, I., Fobo, G., Frishman, G., Mon-
trone, C. & Ruepp, A. CORUM: the comprehensive resource of mammalian protein com-
plexes—2019. Nucleic Acids Res. 47, D559–D563 (2018).
17.
Karp, P. D., Billington, R., Caspi, R., Fulcher, C. A., Latendresse, M., Kothari, A., Keseler,
I. M., Krummenacker, M., Midford, P. E., Ong, Q., et al. The BioCyc collection of microbial
genomes and metabolic pathways. Brief. Bioinform. (2017).
18.
Karr, J. R., Sanghvi, J. C., Macklin, D. N., Gutschow, M. V., Jacobs, J. M., Bolival Jr, B.,
Assad-Garcia, N., Glass, J. I. & Covert, M. W. A whole-cell computational model predicts
phenotype from genotype. Cell 150, 389–401 (2012).
19.
Goldberg, A. P., Szigeti, B., Chew, Y. H., Sekar, J. A., Roth, Y. D. & Karr, J. R. Emerging
whole-cell modeling principles and methods. Curr. Opin. Biotechnol. 51, 97–102 (2018).
20.
Harris, L. A., Hogg, J. S., Tapia, J.-J., Sekar, J. A., Gupta, S., Korsunsky, I., Arora, A.,
Barua, D., Sheehan, R. P. & Faeder, J. R. BioNetGen 2.2: advances in rule-based modeling.
Bioinformatics 32, 3366–3368 (2016).
21.
Hucka, M., Bergmann, F. T., Dräger, A., Hoops, S., Keating, S. M., Le Novère, N., Myers,
C. J., Olivier, B. G., Sahle, S., Schaﬀ, J. C., et al. The Systems Biology Markup Language
(SBML): language speciﬁcation for level 3 version 2 core. J. Integr. Bioinform. 15 (2018).
22.
Misirli, G., Cavaliere, M., Waites, W., Pocock, M., Madsen, C., Gilfellon, O., Honorato-Zimmer,
R., Zuliani, P., Danos, V. & Wipat, A. Annotation of rule-based models with formal semantics
to enable creation, analysis, reuse and visualization. Bioinformatics 32, 908–917 (2015).
23.
Courtot, M., Juty, N., Knüpfer, C., Waltemath, D., Zhukova, A., Dräger, A., Dumontier, M.,
Finney, A., Golebiewski, M., Hastings, J., et al. Controlled vocabularies and semantics in
systems biology. Mol. Syst. Biol. 7, 543 (2011).
12


## Page 13


24.
Heller, S. R., McNaught, A., Pletnev, I., Stein, S. & Tchekhovskoi, D. InChI, the IUPAC
international chemical identiﬁer. J. Cheminform. 7, 23 (2015).
25.
Westbrook, J. D. & Fitzgerald, P. in Structural Bioinformatics (eds Bourne, P. E. & Weissig,
H.) 161–179 (Wiley Online Library, 2003).
26.
Weininger, D. SMILES, a chemical language and information system. 1. Introduction to meth-
odology and encoding rules. J. Chem. Inform. Comp. Sci. 28, 31–36 (1988).
27.
Demir, E., Cary, M. P., Paley, S., Fukuda, K., Lemer, C., Vastrik, I., Wu, G., D’eustachio, P.,
Schaefer, C., Luciano, J., et al. The BioPAX community standard for pathway data sharing.
Nat. Biotechnol. 28, 935–942 (2010).
28.
Fluck, J., Madan, S., Ansari, S., Karki, R., Rastegar-Mojarad, M., Catlett, N. L., Hayes, W.,
Szostak, J., Hoeng, J., Peitsch, M., et al. Training and evaluation corpora for the extraction of
causal relationships encoded in biological expression language (BEL). Database 2016, baw113
(2016).
29.
LeDuc, R. D., Schwämmle, V., Shortreed, M. R., Cesnik, A. J., Solntsev, S. K., Shaw, J. B.,
Martin, M. J., Vizcaino, J. A., Alpi, E., Danis, P., et al. ProForma: a standard proteoform
notation. J. Proteome Res. 17, 1321–1325 (2018).
30.
Cox, R. S., Madsen, C., McLaughlin, J. A., Nguyen, T., Roehner, N., Bartley, B., Beal, J.,
Bissell, M., Choi, K., Clancy, K., et al. Synthetic Biology Open Language (SBOL) version
2.2.0. J. Integr. Bioinform. 15 (2018).
31.
Cuellar, A., Hedley, W., Nelson, M., Lloyd, C., Halstead, M., Bullivant, D., Nickerson, D.,
Hunter, P. & Nielsen, P. The CellML 1.1 speciﬁcation. J. Integr. Bioinform. 12, 4–85 (2015).
32.
Westbrook, J. D., Shao, C., Feng, Z., Zhuravleva, M., Velankar, S. & Young, J. The Chemical
Component Dictionary: complete descriptions of constituent molecules in experimentally de-
termined 3D macromolecules in the Protein Data Bank. Bioinformatics 31, 1274–1278 (2014).
33.
Machnicka, M. A., Milanowska, K., Osman Oglou, O., Purta, E., Kurkowska, M., Olchowik,
A., Januszewski, W., Kalinowski, S., Dunin-Horkawicz, S., Rother, K. M., et al. MODOMICS:
a database of RNA modiﬁcation pathways–2013 update. Nucleic Acids Res. 41, D262–D267
(2012).
34.
Leonard, S. A. IUPAC/IUB single-letter codes within nucleic acid and amino acid sequences.
Curr. Protoc. Bioinformatics, A–1A (2003).
35.
Pearson, W. R. Rapid and sensitive sequence comparison with FASTP and FASTA. Methods
Enzymol. 183, 63–98 (1990).
36.
Dong, H., Nilsson, L. & Kurland, C. G. Co-variation of tRNA abundance and codon usage in
Escherichia coli at diﬀerent growth rates. J. Mol. Biol. 260, 649–663 (1996).
37.
Mackie, G. A. RNase E: at the interface of bacterial RNA processing and decay. Nat. Rev.
Microbiol. 11, 45–57 (2013).
38.
Wei, Y., Silke, J. R. & Xia, X. An improved estimation of tRNA expression to better elucidate
the coevolution between tRNA abundance and codon usage in bacteria. Sci. Rep. 9, 3184
(2019).
39.
Bailly, M., Giannouli, S., Blaise, M., Stathopoulos, C., Kern, D. & Becker, H. D. A single
tRNA base pair mediates bacterial tRNA-dependent biosynthesis of asparagine. Nucleic Acids
Res. 34, 6083–6094 (2006).
13


## Page 14


40.
Woldringh, C., De Jong, M., Van den Berg, W & Koppes, L. Morphological analysis of the
division cycle of two Escherichia coli substrains during slow growth. J. Bacteriol. 131, 270–279
(1977).
41.
Monk, J. M., Lloyd, C. J., Brunk, E., Mih, N., Sastry, A., King, Z., Takeuchi, R., Nomura, W.,
Zhang, Z., Mori, H., et al. iML1515, a knowledgebase that computes Escherichia coli traits.
Nat. Biotechnol. 35, 904–908 (2017).
42.
Kholodenko, B. N. Negative feedback and ultrasensitivity can bring about oscillations in the
mitogen-activated protein kinase cascades. Eur. J. Biochem. 267, 1583–1588 (2000).
43.
Pinkas, D. M., Ding, S., Raines, R. T. & Barron, A. E. Tunable, post-translational hydroxy-
lation of collagen domains in Escherichia coli. ACS Chem. Biol. 6, 320–324 (2011).
44.
An, B., Kaplan, D. L. & Brodsky, B. Engineered recombinant bacterial collagen as an alter-
native collagen-based biomaterial for tissue engineering. Front. Chem. 2, 40 (2014).
45.
Yi, Y., Sheng, H., Li, Z. & Ye, Q. Biosynthesis of trans-4-hydroxyproline by recombinant
strains of Corynebacterium glutamicum and Escherichia coli. BMC Biotechnol. 14, 44 (2014).
46.
McLaughlin, J. A., Myers, C. J., Zundel, Z., Mısırlı, G., Zhang, M., Oﬁteru, I. D., Goñi Moreno,
A. & Wipat, A. SynBioHub: a standards-enabled design repository for synthetic biology. ACS
Synth. Biol. 7, 682–688 (2018).
47.
Hucka, M., Nickerson, D. P., Bader, G. D., Bergmann, F. T., Cooper, J., Demir, E., Garny,
A., Golebiewski, M., Myers, C. J., Schreiber, F., et al. Promoting coordinated development
of community-based information standards for modeling in biology: the COMBINE initiative.
Front. Bioeng. Biotechnol. 3, 19 (2015).
48.
O’Boyle, N. M., Guha, R., Willighagen, E. L., Adams, S. E., Alvarsson, J., Bradley, J.-C.,
Filippov, I. V., Hanson, R. M., Hanwell, M. D., Hutchison, G. R., et al. Open data, open
source and open standards in chemistry: the Blue Obelisk ﬁve years on. J. Cheminform. 3, 37
(2011).
14


## Page 15


Figure legends and boxes
…A{cnmA}GU{25U}CU…
Modified tRNA
C. Grammar for polymers
A. Alphabets of 
residues
DNA
RNA
Protein
User-defined
B. Ontology of 
crosslinks
Disulfide bond
Isopeptide bond
Thioesterbond
User-defined
E. Calculated properties
Molecular structure
Major microspecies,
Formula, weight, charge
H. User interfaces
Web app
CLI
REST
Python
F. Exported formats
Structure: SMILES
Canonical seq: IUPAC
Image: PNG, SVG, ...
G. Integrations with
network formats
Pathways: BioPAX
Models: CellML, SBML
Designs: SBOL
Disulfide-linked homodimer
2 * P83658 |
x-link: [id: “disulfide”
| l: P83658(1)-7
 | r: P83658(2)-12] ...
D. Grammar for complexes
Figure 1.
The BpForms-BcForms toolkit can abstract, validate, and analyze the pri-
mary structures of non-canonical polymers and complexes and help integrate structural
information about macromolecules into networks. The toolkit includes (A) extensible al-
phabets that represent individual DNA, RNA and protein residues; (B) an ontology of crosslinks;
(C) a grammar for composing polymers from residues, caps, crosslinks and nicks; (D) a grammar
for composing complexes from polymers and crosslinks; software tools for validating descriptions
of macromolecules, (E) calculating molecular properties of macromolecules, (F) exporting macro-
molecules to other formats, and visualizing macromolecules; (G) protocols for integrating structural
information about macromolecules into omics, systems biology, and synthetic biology formats for
networks, models, and genetic designs; and (H) multiple user interfaces.
15


## Page 16


1: A (Alanine)
3: U (Selenocysteine)
2: C (Cysteine)
Left bond atom
Inter-residue bonds
Left displaced atom
Right bond bond
Right displaced atom
Bond
Crosslink
Bond atom
Displaced atom
Bond
Coordinate system
Atom (in residue)
1
1
1
Residue (in seq)
Subunit (in 
repeated subunit
of complex)
Compound
Polymer
Complex
Residue
1
2
N
4
8
10
1
O
9
N
5
4
2
O
3
N
1
2
4
O
5
O
6
7
Se8
10
S H
11
OH
OH
H+H
H+
H
1
2
N
4
8
O
9
N
5
4
2
O
3
N
1
2
4
O
5
O
6
7
Se
8
10
S H
11
1
10
OH
OH
H+H
H+
H
Subunit (BpForms)
Pept: ACU
Residues (In alphabet)
A: C[C@H]([NH3+])C(=O)O
C: OC(=O)[C@@H]([NH3+])CS
U: N[C@H](C(=O)O)C[SeH]
Crosslink (In crosslinks ontology)
disulfide: C-S11|C-S11
Complex (BcForms)
Dimer: 2 * Pept 
| x-link: [
       id: “disulfide” 
      | l: PeptA(1)-2
      | r: PeptA(2)-2]
1: A (Alanine)
3: U (Selenocysteine)
2: C (Cysteine)
1: Pept
2: Pept
C
D
E
F
B
Dimer
A
Figure 2.
BpForms and BcForms abstract the primary structures of polymers and
complexes as combinations of residues, crosslinks, and nicks. For example, BcForms ab-
stracts a disulﬁde-linked homodimer (A, green box) of a selenocysteine-modiﬁed tripeptide (B, blue
boxes) as two copies of the tripeptide and a single crosslink (C, green text) and BpForms abstracts
the peptide as a sequence of three residues, including selenocysteine (U) (D, blue text). These
abstractions are enabled by alphabets of residues (E, black text) and an ontology of crosslinks (F,
black text).
16


## Page 17


A
B
Canonical residue
Freq (105 nt cell cycle-1)
Freq (105 nt cell cycle-1)
Modified residue
Figure 3.
BpForms and BcForms can facilitate integrative analyses of ﬁne-grained
global intracellular networks. For example, we used BpForms to estimate the metabolic cost of
tRNA modiﬁcation in E. coli by canonical residue (A) and modiﬁed residue (B) from information
about the modiﬁcation, abundance, and turnover of each tRNA.
17


## Page 18


MAPKKKK
EGFR
MAPKKK
MAPKKK-P
MAPKK
MAPKKK
MAPKK
MAPKK-P
MAPKK-PP
GTP +
H2O
GDP +
H+
Pi
Pi
Pi
Pi
Pi
GTP +
H2O
GDP +
H+
GTP +
H2O
GDP +
H+
Transcriptional
regulation
PI3K
S6K
MAPKK-P
MAPK
MAPK-P
MAPK-PP
GTP +
H2O
GDP +
H+
Pi
Pi
Pi
GTP +
H2O
GDP +
H+
MAPK-P
Pi
MAPKKK-P
MAPKK-PP
329
218
222
329
188
188
190
190
188 190
188 190
188 190
188 190
MAPKKKK
MAPKKK
MAPKKK-P
MAPKK
MAPKK-PP
GTP +
H2O
GDP +
H+
Pi
Pi
Pi
GTP +
H2O
GDP +
H+
GTP +
H2O
GDP +
H+
MAPKK-P
MAPK
MAPK-PP
GTP +
H2O
GDP +
H+
Pi
GTP +
H2O
GDP +
H+
MAPK-P
Pi
329
218
188
MAPKKKK
MAPKKK
MAPKKK-P
MAPKK
MAPKK-P
MAPKK-PP
MAPKK-P
MAPK
MAPK-P
MAPK-PP
MAPK-P
329
218
222
218 222
218 222
218 222
218 222
218 222
218 222
218 222
188
190
MAPKKKK
EGFR
MAPKKK
MAPKKK-P
MAPKK
MAPKKK
MAPKK
MAPKK-PP
Transcriptional
regulation
PI3K
S6K
MAPKK-P
MAPK
MAPK-PP
MAPK-P
MAPKKK-P
MAPKK-PP
329
218
329
188
MAPKKKK
MAPKKK
MAPKKK-P
MAPKK
MAPKK-PP
MAPKK-P
MAPK
MAPK-PP
MAPK-P
329
218
188
E
A
Proteoforms and reactions 
found by enumerating each 
combination of modifications
Connections to other pathways
found with BioModels
Connections to metabolism
identified by mass balance
Proteoforms and reactions
found through composition
with models of other pathways
BpForms annotations
Original model
C
D
B
18


## Page 19


Figure 4.
BpForms and BcForms can facilitate the construction, expansion, composi-
tion, and reﬁnement of ﬁne-grained global intracellular networks. For example, we used
BpForms to systematically identify ways to improve and expand the Kholodenko model of MAPK
signaling (A, grey) by using BpForms to capture the semantic meaning of each species (A, red),
identify missing protein states (B, blue), identify other models that represent similar proteins which
could be composed with the Kholodenko model (C, yellow) which could reveal additional missing
combinations of species (C, green), and identify mass imbalances which indicate missing metabo-
lites which could facilitate composition with metabolic models (D). Together, this could enable a
substantially expanded model (E).
19


## Page 20


Residue sequence
This example illustrates how to use BpForms to describe a DNA which begins with deoxyinosine.
{dI}ACGC
User-deﬁned residues
Residues which are not captured by our public alphabets can be captured within descriptions of polymers. This
example illustrates how to describe a protein which ends with N5-methyl-L-arginine.
CRGN[
id:
"AA0305"
| structure:
"OC(=O)[C@H](CCCN(C(=[NH2])N)C)[NH3+]"
| l-bond-atom:
N16-1
| r-bond-atom:
C2
| l-displaced-atom:
H16+1
| l-displaced-atom:
H16
| r-displaced-atom:
O1
| r-displaced-atom:
H1
| name:
"N5-methyl-L-arginine"
| synonym:
"delta-N-methylarginine"
| synonym:
"N5-carbamimidoyl-N5-methyl-L-ornithine"
| identifier:
"MOD:00310" @ "mod"
| identifier:
"CHEBI:21848" @ "chebi"
| base-monomer:
"R"
| comments:
"Generated by protein-arginine N5-methyltransferase (EC 2.1.1.-)."
]
Crosslinks and nicks
This example illustrates how to describe a peptide that contains a disulﬁde bond between the cysteines at the ﬁrst
and third positions and a nick between the cysteine and alanine at the ﬁrst and second positions.
C:AC | x-link:
[
id:
"disulfide"
| l:
1 | r:
3
]
User-deﬁned crosslinks
Crosslinks which are not captured by our public ontology can be described inline. This example illustrates how to
describe a peptide that contains a disulﬁde bond between the cysteines at the ﬁrst and third positions.
CAC | x-link:
[
l-bond-atom:
1S11 | r-bond-atom:
3S11
| l-displaced-atom:
1H11 | r-displaced-atom:
3H11
| comments:
"disulfide bond between 1C and 3C"
]
Circularity
This example illustrates how to describe a circular di-deoxyribonucleic acid.
AC | circular
Missing knowledge
User-deﬁned residues can also capture missing information about the mass, charge, location, and biosynthesis of
residues. This example illustrates how to describe a protein which contains a methylated cysteine or asparagine at
an unknown position between the ﬁfth and tenth residues.
CRGN[
base-monomer:
"C"
| delta-mass:
12 | delta-charge:
0
| position:
5-10 [C, N]
]
EGYNNYCRAKYRGH
Box 1.
Examples of the BpForms grammar for describing polymers.
20


## Page 21


Subunit composition
This example illustrates how to use BcForms to describe MalEFGK (Complex Portal: CPX-1932), a heteropen-
tameric maltose ABC transporter.
MalE + MalF + MalG + 2 * MalK
Crosslinks
This example illustrates how to use the crosslinks ontology to describe a disulﬁde-linked antiparallel homodimer
of disintegrin schistatin of Echis carinatus (UniProt: P83658).
2 * P83658
| x-link:
[
id:
"disulfide"
| l:
P83658(1)-7
| r:
P83658(2)-12
]
| x-link:
[
id:
"disulfide"
| l:
P83658(1)-12
| r:
P83658(2)-7
]
User-deﬁned crosslinks
Crosslinks which are not captured by our public ontology can be deﬁned within descriptions of complexes. This
example illustrates how to describe the crosslinking of 10 kDa chaperonin (UniProt: P9WPE5) of Mycobacterium
tuberculosis with prokaryotic ubiquitin-like protein Pup (UniProt: P9WHN5) via a isoglutamyl lysine isopeptide
bond (RESID: AA0124). Cells use this crosslink to mark 10 kDa chaperonin for proteasomal degradation.
P9WPE5 + P9WHN5
| x-link:
[
l-bond-atom:
P9WHN5(1)-100N1-1
| r-bond-atom:
P9WPE5(1)-63C2
| l-displaced-atom:
P9WHN5(1)-100H1+1
| l-displaced-atom:
P9WHN5(1)-100H1
| r-displaced-atom:
P9WPE5(1)-63N1
| r-displaced-atom:
P9WPE5(1)-63H1
| r-displaced-atom:
P9WPE5(1)-63H1
| comments:
"isoglutamyl lysine isopeptide bond"
]
Box 2.
Examples of the BcForms grammar for describing complexes.
21

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1903_10042v2_bpforms_and_bcforms_tools_for_concretely_describing_non_canonical_polymers_and
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1903_10042V2_BPFORMS_AND_BCFORMS_TOOLS_FOR_CONCRETELY_DESCRIBING_NON_CANONICAL_POLYMERS_AND.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

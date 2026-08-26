---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1907.08400v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1907.08400v1_An_Information_Extraction_and_Knowledge_Graph_Platform_for_Accelerating_Biochemi

> Source: 1907.08400v1_An_Information_Extraction_and_Knowledge_Graph_Platform_for_Accelerating_Biochemi.pdf

> Pages: 4

---


## Page 1


An Information Extraction and Knowledge Graph Platform
for Accelerating Biochemical Discoveries
MATTEO MANICA, CHRISTOPH AUER, VALERY WEBER, FEDERICO ZIPOLI, MICHELE
DOLFI, PETER STAAR, TEODORO LAINO, and COSTAS BEKAS, IBM Research, Switzerland
AKIHIRO FUJITA, HAYASHIBARA & CO., LTD., Japan
HIROKI TODA, SHUICHI HIROSE, and YASUMITSU ORII, NAGASE & CO., LTD., Japan
Information extraction and data mining in biochemical literature is a daunting task that demands resource-
intensive computation and appropriate means to scale knowledge ingestion. Being able to leverage this
immense source of technical information helps to drastically reduce costs and time to solution in multiple
application fields from food safety to pharmaceutics. We present a scalable document ingestion system that
integrates data from databases and publications (in PDF format) in a biochemistry knowledge graph (BCKG).
The BCKG is a comprehensive source of knowledge that can be queried to retrieve known biochemical facts and
to generate novel insights. After describing the knowledge ingestion framework, we showcase an application
of our system in the field of carbohydrate enzymes. The BCKG represents a way to scale knowledge ingestion
and automatically exploit prior knowledge to accelerate discovery in biochemical sciences.
CCS Concepts: • Information systems →Information extraction; • Applied computing →Chemistry;
Biological networks; Systems biology.
Additional Key Words and Phrases: knowledge graph, biochemistry, data mining, network biology, systems
biology, material science
ACM Reference Format:
Matteo Manica, Christoph Auer, Valery Weber, Federico Zipoli, Michele Dolfi, Peter Staar, Teodoro Laino,
Costas Bekas, Akihiro Fujita, Hiroki Toda, Shuichi Hirose, and Yasumitsu Orii. 2019. An Information Extraction
and Knowledge Graph Platform for Accelerating Biochemical Discoveries. In Proceedings of KDD 2019: Workshop
on Applied Data Science for Healthcare (KDD 2019 Workshop). ACM, New York, NY, USA, 4 pages.
1
INTRODUCTION
The discovery of novel biotechnological processes to produce chemicals and materials with com-
petitive industrial conditions is of paramount importance for new and old businesses. Relying
on opportunistic or occasional discoveries prevents innovation that could be pursued instead, by
reasoning on the large knowledge corpus of science collected in the last century. For this reason, the
industrial competitive advantage of the next decade will be strongly connected with the possibility
to extract and represent the immense human knowledge accumulated in the past to accelerate
the discovery of new processes and materials. To get a glimpse of the task’s complexity, as of
writing, by simply querying NCBI [12] for the keyword carbohydrate we retrieve: >220K genes,
>1.5M papers, >12.9M proteins. Ideally, we would like to be able to ingest all this information at
scale and translate it right away into actionable insights. For example, in the context of food or
pharmaceutical ingredients, carbohydrates play a crucial role and it is of primary importance to
retrieve information about any characterized enzyme able to synthesize them. The design of a
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and
the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored.
Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from permissions@acm.org.
KDD 2019 Workshop, August 05, 2019, Anchorage, AK, USA
© 2019 Association for Computing Machinery.
1
arXiv:1907.08400v1  [cs.IR]  19 Jul 2019


## Page 2


KDD 2019 Workshop, August 05, 2019, Anchorage, AK, USA
Manica et al.
digital platform implementing the possibility to explore the vast amount of data available will
speed up and improve the discovery of novel ingredients and methodologies to synthesize them,
directly impacting key aspects of the health care and life sciences domain, e.g., food safety, drug
design. Over the years efforts to collect biomolecular information in a structured format have
led to the compilation of multiple database resources: protein-specific databases, enzyme-specific
databases, chemical compound databases and various resources regarding pathways, taxonomy
information, DNA or protein sequences. While these resources are extremely valuable, they present
two problematic aspects: first, despite of the fact that some databases integrate multiple sources or
report links to other knowledge bases, having independent data collections hinders our ability to
effectively reason on knowledge, find patterns or generate novel insights; secondly, a large portion
of scientific and technical knowledge is stored in an unstructured format in publications or in books.
Recently, an interesting framework, called biochem4j, has been developed by Swainston et al. [14].
This resource integrates multiple databases with a focus on metabolic engineering in a queryable
knowledge graph (KG). While extremely useful, it only addresses one of the aforementioned issues,
as it overlooks the information contained in publications and books in the form of natural language,
tables, figures, etc. To bridge this gap, herein we present a scalable document ingestion platform for
biochemical knowledge: BCKG (see Figure 1). The platform integrates information from multiple
database resources and it leverages recent developments in machine learning-based document
parsing to assemble a comprehensive biochemistry Knowledge Graph (KG). Organizing knowledge
in a graph structure allows to integrate disparate data resources and to efficiently retrieve the
knowledge ingested. Moreover, graph analytic techniques enable the generation of novel insights,
a key aspect in research and industrial applications.
Uniprot
Family
EnzymeClass
Cazy-Proteins
GenBankID
EC-Number
Activities
Organism
RefSeq-Id
KEGG-Id
DOI
Accessions
SwissProt-Proteins
Brenda
MeltingTemperature
MeltingPoint
MeltingPressure
Base-Carbohydrates
ChemicalFormulas
CAS-Numbers
Cyclic-Carbohydrates
MolecularWeight
Derivate-Carbohydrates
BoilingTemperature
BoilingPoint
BoilingPressure
BCKG
Publications
Graph analytics
Databases
Fig. 1. BCKG concept and current structure. The platform ingests knowledge from different data sources
and implements graph analytics techniques in a comprehensive and queryable knowledge base (left). The
currently assembled KG integrates multiple data sources organizing them in linked collections of nodes
(right).
2


## Page 3


BCKG
KDD 2019 Workshop, August 05, 2019, Anchorage, AK, USA
2
METHODS
2.1
Data Ingestion
The BioChemistry Knowledge Graph (BCKG) is created from two distinct, separate sources. On
the one hand, we ingest data from a comprehensive list of structured databases: UniProt [15],
Pfam [4], BRENDA [8], CAZy [3], PubChem [10], ChEMBL [6], KEGG [9, 11], The NCBI Taxonomy
database [5], GenBank [1] and PDB [2]. On the other hand, we also ingest unstructured data, such
as the Handbook of Carbohydrate Engineering [16] and scientific articles. The ingestion of both
type of sources into a single KG presents unique challenges. First, the size of some databases is large
and it is therefore necessary to have a scalable, cloud-native platform to host this data. Furthermore,
the data within the databases is not represented in a unique way (e.g., the concept of the EC number
is represented in at least 3 different ways), which requires us to normalize all database structures
in order to link key-value pairs from one database to another. Second, the ingestion of scientific
articles and books in (scanned) PDF format poses a real problem, since the PDF format does not
allow one to easily extract the information encoded in the documents. To address this issue we
use the Corpus Conversion Service (CCS) [13], a scalable, cloud-native platform to convert large
collections of PDF documents into a structured JSON format. The latter contains all the titles,
abstracts, section-titles, paragraphs, tables, images in textual form. As such, it easily allows us to
perform Named Entity Recognition (NER) and Fact Extraction (FE) on the text/tables of the original
documents. Using NER, we can find the entities referred to in the databases (e.g., taxonomies, genes,
proteins, etc). Using the FE, we can find properties of these entities in the documents.
2.2
KG construction
The KG is assembled by executing the following steps consecutively. First, we parse the structured
databases representing each entity in a JSON document with normalized keys. Second, we extract
and aggregate common concepts from these documents (e.g., the EC number) and create links
between the extracted items. These links form indirect connections between the documents obtained
from the database. Next, we parse the handbooks and the scientific articles using the CCS. The
latter provides us with a JSON file for each PDF-document. From these JSON documents, we then
extract paragraphs and tables, on which we perform NER and FE. The NER provides us with entities
found in the text/tables and allows us to link structured databases with the text/tables from the
PDF-documents via co-occurrence. Furthermore, we also aggregate all facts form the FE process,
which allows us to further add links between entities (e.g., organisms producing carbohydrates
with similar properties). The resulting KG contains >6M nodes and >61M edges.
2.3
KG queries and analytics
Our platform supports a wide range of queries and standard graph analytics: node retrieval, graph
traversal, centrality analysis, clustering, etc. A unique feature of the BCKG resides in its query-
engine, capable of running long workflows on the graph. A workflow is a group of queries linked
in a Directed Acyclic Graph (DAG). Given their DAG structure, workflows can be used to efficiently
perform complex queries, allowing us to explore the graph and to potentially generate novel
insights.
3
RESULTS AND DISCUSSION
To showcase the BCKG platform, we implemented a KG workflow to retrieve enzymes synthesizing
Trehalose, a carbohydrate that has major applications in food, cosmetics and pharmaceutics [7].
Its extraction has been optimized around 2000 by the Hayashibara Company (NAGASE Group)
discovering a cost-effective biotech process using starch as a starting material. The search of new
3


## Page 4


KDD 2019 Workshop, August 05, 2019, Anchorage, AK, USA
Manica et al.
enzymes producing Trehalose is a field of research still very active and with a great business
potential. For carbohydrate research, CAZy represents the relevant source of knowledge. In an
effort to plan for serendipity, we compiled a query to identify, in the larger UniProt database
(Swiss-Prot, manually reviewed), candidate enzymes able to process Trehalose that have not yet
been reported in CAZy. The resulting workflow is composed of:
(1) Trehalose node identification in the Handbook of Carbohydrate Engineering.
(2) Graph traversal in the UniProt database to gather all proteins whose catalytic activity node
has a direct connection with the Trehalose node.
(3) Identify those UniProt protein nodes that have no connection in CAZy.
Among the several hits returned by this query, we report: (a) stf0 - Trehalose 2-sulfotransferase
- Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv) and (b) TPP1 - Probable trehalose-
phosphate phosphatase 1 - Oryza sativa subsp. japonica (Rice). The TPP1 is quite interesting as the
phosphatase class is well represented in CAZy and still this specific enzyme was not listed.
This example, in its simplicity, demonstrates the great capabilities of knowledge graphs in
planning for serendipity, accelerating the discovery process thanks to the effective representation
of the domain knowledge.
REFERENCES
[1] Dennis A. Benson, Mark Cavanaugh, Karen Clark, et al. 2017. GenBank. Nucleic Acids Research 45, D1 (jan 2017),
D37–D42. https://doi.org/10.1093/nar/gkw1070
[2] Helen M. Berman, Tammy Battistuz, T. N. Bhat, et al. 2002. The protein data bank. Acta Crystallographica Section D:
Biological Crystallography 58, 6 I (jan 2002), 899–907. https://doi.org/10.1107/S0907444902003451
[3] Brandi I. Cantarel, Pedro M. Coutinho, Corinne Rancurel, et al. 2009. The Carbohydrate-Active EnZymes database
(CAZy): An expert resource for glycogenomics. Nucleic Acids Research 37, SUPPL. 1 (jan 2009), D233–8.
https:
//doi.org/10.1093/nar/gkn663
[4] Sara El-Gebali, Jaina Mistry, Alex Bateman, et al. 2019. The Pfam protein families database in 2019. Nucleic Acids
Research 47, D1 (jan 2019), D427–D432. https://doi.org/10.1093/nar/gky995
[5] Scott Federhen. 2012. The NCBI Taxonomy database. Nucleic Acids Research 40, D1 (jan 2012), D136–43.
https:
//doi.org/10.1093/nar/gkr1178
[6] Anna Gaulton, Anne Hersey, Micha L. Nowotka, et al. 2017. The ChEMBL database in 2017. Nucleic Acids Research 45,
D1 (2017), D945–D954. https://doi.org/10.1093/nar/gkw1074
[7] Takanobu Higashiyama. 2002. Novel functions and applications of trehalose. Pure and Applied Chemistry 74, 7 (jan
2002), 1263–1269. https://doi.org/10.1351/pac200274071263
[8] Lisa Jeske, Sandra Placzek, Ida Schomburg, et al. 2019. BRENDA in 2019: A European ELIXIR core data resource.
Nucleic Acids Research 47, D1 (jan 2019), D542–D549. https://doi.org/10.1093/nar/gky1048
[9] Minoru Kanehisa, Miho Furumichi, Mao Tanabe, et al. 2017. KEGG: New perspectives on genomes, pathways, diseases
and drugs. Nucleic Acids Research 45, D1 (jan 2017), D353–D361. https://doi.org/10.1093/nar/gkw1092
[10] Sunghwan Kim, Jie Chen, Tiejun Cheng, et al. 2019. PubChem 2019 update: Improved access to chemical data. Nucleic
Acids Research 47, D1 (jan 2019), D1102–D1109. https://doi.org/10.1093/nar/gky1033
[11] Hiroyuki Ogata, Susumu Goto, Kazushige Sato, et al. 1999. KEGG: Kyoto encyclopedia of genes and genomes. Nucleic
Acids Research 27, 1 (jan 1999), 29–34. https://doi.org/10.1093/nar/27.1.29
[12] Eric W. Sayers, Richa Agarwala, Evan E. Bolton, et al. 2019. Database resources of the National Center for Biotechnology
Information. Nucleic Acids Research 47, D1 (jan 2019), D23–D28. https://doi.org/10.1093/nar/gky1069
[13] Peter W J Staar, Michele Dolfi, Christoph Auer, et al. 2018. Corpus Conversion Service. In Proceedings of the 24th ACM
SIGKDD International Conference on Knowledge Discovery & Data Mining - KDD ’18. ACM Press, New York, New York,
USA, 774–782. https://doi.org/10.1145/3219819.3219834
[14] Neil Swainston, Riza Batista-Navarro, Pablo Carbonell, et al. 2017. biochem4j: Integrated and extensible biochemical
knowledge through graph databases. PLoS ONE 12, 7 (jul 2017), e0179130. https://doi.org/10.1371/journal.pone.0179130
[15] The UniProt Consortium. 2018. UniProt: a worldwide hub of protein knowledge. Nucleic Acids Research 47, D1 (jan
2018), D506–D515. https://doi.org/10.1093/nar/gky1049
[16] Kevin J. Yarema. 2010. Handbook of Carbohydrate Engineering. Taylor & Francis. 904 pages. https://doi.org/10.1201/
9781420027631
4

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
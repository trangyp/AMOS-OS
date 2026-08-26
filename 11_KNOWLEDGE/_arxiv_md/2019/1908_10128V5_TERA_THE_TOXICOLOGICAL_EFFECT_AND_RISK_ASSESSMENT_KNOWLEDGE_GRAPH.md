---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1908.10128v5
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1908.10128v5_TERA__the_Toxicological_Effect_and_Risk_Assessment_Knowledge_Graph

> Source: 1908.10128v5_TERA__the_Toxicological_Effect_and_Risk_Assessment_Knowledge_Graph.pdf

> Pages: 16

---


## Page 1


TERA: the Toxicological Eﬀect and Risk
Assessment Knowledge Graph
Erik B. Myklebust1,2, Ernesto Jim´enez-Ruiz2,3, Jiaoyan Chen4,
Raoul Wolf1, and Knut Erik Tollefsen1,5
1 Norwegian Institute for Water Research, Oslo, Norway
2 Department of Informatics, University of Oslo, Norway
3 City, University of London, United Kingdom
4 Department of Computer Science, University of Oxford, United Kingdom
5 Faculty of Environmental Sciences and Natural Resource Management, Norwegian
University of Life Sciences, ˚As, Norway
Abstract. Ecological risk assessment requires large amounts of chemi-
cal eﬀect data from laboratory experiments. Due to experimental eﬀort
and animal welfare concerns it is desired to extrapolate data from ex-
isting sources. To cover the required chemical eﬀect data several data
sources need to be integrated to enable their interoperability. In this pa-
per we introduce the Toxicological Eﬀect and Risk Assessment (TERA)
knowledge graph, which aims at providing such integrated view, and the
data preparation and steps followed to construct this knowledge graph.
We also present the applications of TERA for chemical eﬀect prediction
and the potential applications within the Semantic Web community.
Keywords: Ecotoxicology, Risk Assessment, Knowledge Graph
1
Introduction
Expanding the scope of ecological risk assessment models is a key goal in compu-
tational ecotoxicological research. However, the limiting factor in risk assessment
is often the availability of toxicological eﬀect data for a given compound and a
given organism (species). The potential use of ten to hundreds of test organisms
becomes ethically questionable. Moreover, collection of these data is labour- and
cost-intensive and often requires extensive laboratory experiments.
One major challenge in risk assessment processes is the interoperability of
data. In this paper we present the Toxicological Eﬀect and Risk Assessment
(TERA) Knowledge Graph that aims at providing an integrated view of the rel-
evant data sources.† The data sources that TERA integrates vary from tabular,
to RDF ﬁles and SPARQL queries over public linked data. Certain sources are
† This paper focuses and extends on the construction of the TERA knowledge graph
as a resource for the ecotoxicological and Semantic Web domains, while our paper
in [1] had a special focus on the use of knowledge graph embeddings and machine
learning for chemical eﬀect prediction.
arXiv:1908.10128v5  [cs.AI]  12 Dec 2019


## Page 2


2
E. B. Myklebust et. al.
very large and frequently updated, therefore TERA is materialized upon request
via a series of APIs that are created to interact with TERA.
The main contributions of this paper are summarized as follows:
(i) We have released the TERA knowledge graph. A partially materialized
snapshot among other relevant resources are publicly available (see Zenodo
repository [2]).
(ii) TERA also includes the mappings between ECOTOX and NCBI for which
there was not a complete and public alignment.
(iii) We have created a series of APIs to access, update and extend TERA (see
GitLab repository [3]).
(iv) We describe several applications of the TERA knowledge graph both in
the ecotoxicology domain (e.g., chemical eﬀect prediction) and the Seman-
tic Web domain (e.g., embedding of hierarchical biased knowledge graphs,
large scale ontology alignment).
This paper is organized as follows. Section 2 provides an introduction to
ecotoxicological risk assessment, while Section 3 provides some background to
facilitate the understanding of the subsequent sections. In Section 4 we ﬁrst
present the data sources used to construct TERA, before we show the integration
of these sources, and ﬁnally show several ways of accessing TERA. Section 5
describes the potential applications of TERA, while Section 6 elaborates on the
contribution of this work.
2
Background
Ecotoxicology is a multidisciplinary ﬁeld that studies the potentially adverse
toxicological eﬀects of chemicals on individuals, sub-populations, communities
and ecosystems. In this context, risk is the result of the intrinsic hazards of a
substance on species, populations or ecosystems, combined with an estimate of
the environmental exposure, i.e., the product of exposure and eﬀect (hazard).
Figure 1 shows a simpliﬁed risk assessment pipeline. Exposure data is gath-
ered from analysis of environmental concentrations of one or more chemicals,
while eﬀects (hazards) are characterized for a number of species in the labora-
tory as a proxy for more ecologically relevant organisms. These two data sources
are used to calculate risk, using so-called assessment factors to extrapolate a risk
quotient (RQ; ratio between exposure and eﬀects). The RQ for one chemical or
the mixture of many chemicals is used to identify chemicals with the highest RQs
(risk drivers), susceptible species (or taxa), identify relevant modes of action1
(MoA) and characterize detailed toxicity mechanisms for one or more species (or
taxa). Results from these predictions can generate a number of new hypotheses
that can be investigated in the laboratory or studied in the environment.
The eﬀect data is obtained from available data, or in the case of no avail-
able data, during laboratory experiments, where the sub-population of a single
1 The functional or anatomical change in an organism due to exposure to a compound
is called MoA.


## Page 3


TERA: the Toxicological Eﬀect and Risk Assessment Knowledge Graph
3
Risk Quotient
Exposure
Effects
Hot spot
identiﬁcation
Susceptible
Species
Risk Driver
Risk
Fig. 1: Simpliﬁed ecological risk assessment pipeline.
species is exposed to a gradient of concentrations of a chemical. Most commonly,
mortality rate, growth, development or reproductive output are measured over
time.
To give a good indication of the toxicity to a species, these experiments are
conducted with a concentration range spanning from no eﬀect (0%) to complete
eﬀect (100%) when this is pragmatically possible. Hence some compounds will
be more toxic than others and variance in susceptibility between species may
provide a distribution of the eﬀective concentration for one speciﬁc compound.
Ecological risk assessment requires large amounts of eﬀect data to eﬃciently
predict risk for the ecosystems and ecosystem components (e.g., species and
taxa). The data must cover a minimum number of the chemicals found when
analysing environmental samples, along with covering species and taxa present
in the ecosystem. This leads to an immense search space that is close to impos-
sible to encompass in its entirety and risk assessment is thus often limited by
lack of suﬃciently high quality eﬀect data. It becomes essential to extrapolate
from known to unknown combinations of chemical–species pairs, which in some
degree can be overcome by predicting the eﬀects themselves through the use
of quantitative structure–activity relationship models (QSARs). These models
have shown promising results for use in risk assessment, e.g., [4], but have lim-
ited application domain (coverage), both in terms of compounds and species.
Use of read-across and selection of proxy compounds that are chemically sim-
ilar, display similar toxicity or have similar MoA and toxicity mechanisms are
therefore becoming an attractive solution with increasing popularity (e.g., [5,6]).
Development of computational approaches that identify data that can be used
for identifying proxy compounds to be used for read-across and data gap ﬁlling,
is key to facilitate rapid, cost-eﬀective, reliable and transparent predictions of


## Page 4


4
E. B. Myklebust et. al.
new eﬀects. We contribute in this regard by creating a semantic layer, i.e., a
knowledge graph, to enable extraction and integration of this high quality data.
3
Preliminaries
Knowledge graphs. We follow [7] in the notion of a RDF-based knowledge
graph which is represented as a set of RDF triples ⟨s, p, o⟩, where s represents
a subject (a class or an instance), p represents a predicate (a property) and
o represents an object (a class, an instance or a data value e.g., text, date
and number). RDF entities (i.e., classes, properties and instances) are repre-
sented by URIs (Uniform Resource Identiﬁer). A knowledge graph consits of
a terminology and an assertions box (TBox and ABox). The TBox is com-
posed by RDF Schema constructs like class subsumption (e.g., ncbi:taxon/6668
rdfs:subClassOf ncbi:taxon/6657) and property domains and ranges (e.g.,
et:concentration rdfs:domain et:Chemical).2 The ABox contains relation-
ships among instances and type deﬁnitions (e.g., et:taxon/28868
rdf:type
et:Taxon).
SPARQL Queries. RDF-based knowledge graphs can be accessed by SPARQL
query language.3 Next we summarise the SPARQL constructs used in this work:
(i) Select queries are used when the desired output is tabular.
(ii) Construct queries can be used if the purpose of the query is to create a
new graph. We use this in Listing 3 to create equivalence triples.
(iii) Property paths express multiple edges in a graph. e.g., alternate paths (e.g.,
rdfs:label | foaf:name), inverse relations (e.g., ˆrdf:type), path se-
quences (e.g., rdf:type / rdfs:subClassOf), and any combination of these.
(iv) A blank node is a node where the identiﬁer is not explicitly given. This al-
lows the use of temporary nodes in queries. e.g., Listing 4 uses [rdfs:label
"Oslofjorden"@no] to represent a node with label Oslofjorden.
Moreover, the extended syntax of SPARQL enables the use of complex property
paths (e.g., a path of minimum 1 to maximum n rdfs:subClassOf relations
is represented as rdfs:subClassOf{1,n}), concatenating variables (e.g., Listing
3), aggregations and more.4
Ontology alignment. Finding the corresponding mappings between a source
and a target ontology or knowledge graph is called ontology alignment [9]. In
this work, computed mappings are represented in the knowledge graph as triples
among the entities of the source and target (e.g., ncbi:taxon/13402 owl:sameAs
et:taxon/Carya).
2 The OWL 2 ontology language provides more expressive constructors. Note that the
graph projection of an OWL 2 ontology can be seen as a knowledge graph (e.g., [8]).
3 https://www.w3.org/TR/rdf-sparql-query/
4 https://www.w3.org/wiki/SPARQL/Extensions


## Page 5


TERA: the Toxicological Eﬀect and Risk Assessment Knowledge Graph
5
test id reference number
test cas
species number
1068553
5390
877-43-0 (2,6-Dimethylquinoline)
5156 (Danio rerio)
2037887
848
79-06-1 (2-Propenamide)
14 (Rasbora heteromorpha)
Table 1: ECOTOX database tests examples.
result id test id endpoint conc1 mean conc1 unit
98004
1068553
LC50
400
mg/kg diet
2063723 2037887
LC10
220
mg/L
Table 2: ECOTOX database results examples.
4
The TERA Knowledge Graph
This sections presents the data sources currently integrated within TERA, the
APIs to prepare an integrate these data sources and the available entry points
to access TERA.
4.1
Data sources
The TERA knowledge graph is constructed from a number of sources, including
tabular data, RDF triples and SPARQL endpoints.
Eﬀect data. The largest publicly available repository of eﬀect data is the ECO-
TOXicology knowledgebase (ECOTOX) developed by the US Environmental
Protection Agency [10]. This data is gathered from published toxicological pa-
pers and limited internal experiments. The dataset consists of 940k experiments
using 12k compounds and 13k species, implying a compound–species pair con-
verge of maximum ∼0.6%. The resulting endpoint5 from an experiment is cat-
egorised in one of a plethora of predeﬁned endpoints. e.g., for endpoints such
as EC50 (eﬀective concentration on 50% of test population), an eﬀect must be
deﬁned in conjunction with the endpoint. Mortality, chronic, and reproductive
toxicity are common eﬀect outcomes to characterise the eﬀective concentration
of a compound upon a given target species.
Tables 1 and 2 contains an excerpt of the ECOTOX database. ECOTOX
includes information about the compounds and species used in the tests. This
information, however, is limited and additional (external) resources are required
to complement ECOTOX.
Compounds. The ECOTOX database use an identiﬁer called CAS Registry
Number assigned by the Chemical Abstracts Service to identify compounds. The
CAS numbers are proprietary, however, Wikidata [11] (indirectly) encodes map-
pings between CAS numbers and open identiﬁers like InChIKey, a 27-character
5 Not to be confused with a SPARQL endpoint.


## Page 6


6
E. B. Myklebust et. al.
hash of the International Chemical Identiﬁer (InChI) which encodes chemi-
cal information uniquely6 [13]. Moreover, chemical features can be gathered
from the chemical information dataset PubChem [14] using the open identi-
ﬁers. The classiﬁcation of compounds in PubChem only concerns permutations
of compounds. Therefore, we use the (Ch)EBI SPARQL endpoint to access the
ChEMBL dataset, which enables us to create a more extensive classiﬁcation hi-
erarchy. To gather the functional properties of a chemical (e.g., painkiller) we
use the MeSH dataset, which is available from the MeSH SPARQL endpoint.
Taxonomy. ECOTOX contains a taxonomy, however, this only considers the
species represented in the ECOTOX eﬀect data. Hence, to enable extrapola-
tion of eﬀects across a larger taxonomic domain, we introduce the NCBI taxon-
omy [15]. This taxonomy data source consists of a number of database dump ﬁles,
which contains a hierarchy for all sequenced species, which equates to around
10% of the currently known life on Earth. For each of the taxa (species and
classes), the taxonomy deﬁnes a handful of labels, most commonly used are the
scientiﬁc and common names. However, labels such as authority can be used
to see the citation where the species was ﬁrst mentioned, while synonym is a
alternate scientiﬁc name, that may be used in the literature.
Species traits. As an analog to chemical features, we use species traits to
expand the usability of the knowledge graph. The traits we have included in the
knowledge graph are the habitat, endemic regions, and presence. This data is
gathered from the Encyclopedia of Life (EOL) [16], which is available as tabular
ﬁles. Moreover, EOL uses external deﬁnitions of certain concepts, and mappings
to these sources are available as glossary ﬁles. In addition to traits, researchers
may be interested in species that have diﬀerent conservation statuses, e.g., if the
population is stable or declining, etc. This data can also be extracted from EOL.
4.2
Preparing and Integrating Data into TERA
We have created four APIs for wrangling and incorporating eﬀect, taxonomy,
and chemical data into the TERA knowledge graph. These APIs also provide
(predeﬁned) methods to access the knowledge in TERA. Figure 2 shows how
the data sources integrate into the APIs and how the APIs map among each
other. Excluding the SPARQL endpoints,7 the data can be downloaded from
the sources websites.8
6 While InChI is unique, InChiKey is not, although collisions are few [12]
7 Wikidata: https://query.wikidata.org/sparql
ChEMBL: https://www.ebi.ac.uk/rdf/services/sparql
MeSH: https://id.nlm.nih.gov/mesh/query
8 ECOTOX: https://cfpub.epa.gov/ecotox/
PubChem: https://pubchemdocs.ncbi.nlm.nih.gov/downloads
NCBI Taxonomy: https://www.ncbi.nlm.nih.gov/guide/taxonomy/
EOL: https://opendata.eol.org/


## Page 7


TERA: the Toxicological Eﬀect and Risk Assessment Knowledge Graph
7
Fig. 2: Data sources and colour-coded elements of the TERA knowledge graph.
Species API. This API uses data from various tabular sources to describe the
species taxonomy and related features. We use the namespace https://www.
ncbi.nlm.nih.gov/taxonomy (ncbi) for the NCBI taxonomy.
1. The integration of the the NCBI Taxonomy into the knowledge graph is split
into several sub-tasks.
(a) Loading the hierarchical structure included in nodes.dmp. The columns
of interest are the taxon identiﬁers of the child and parent taxon, along
with the rank of the child taxon and the division where the taxon belongs.
We use this to create triples like (v) and (vi) in Table 3.
(b) To aid alignment between NCBI and ECOTOX identiﬁers, we add the
synonyms found in names.dmp. Here, the taxon identiﬁer, its name and
name type are used to create triples similar to (vii) in Table 3. Note
that a taxon in NCBI can have a plethora of synonyms while a taxon in
ECOTOX usually have two, i.e., common name and Latin name.
(c) Finally, we add the labels of the divisions found in divisions.dmp. In
addition, we add disjointness axioms among all divisions, e.g., Triple
(ii) in Table 3.
2. The EOL traits data is available as tabular data, however using URIs, such
that integrating the data is trivial.
Chemical API. This API can be used either with local ﬁles downloaded from
their respective sources (PubChem, ChEMBL, MeSH), or a local or online end-
points, depending on requirements. These chemical data sources are available as
RDF and therefore integrating them into TERA is straightforward.


## Page 8


8
E. B. Myklebust et. al.
#
subject
predicate
object
(i)
et:group/Worms
owl:disjointWith
et:group/Fish
(ii)
ncbi:division/2
owl:disjointWith
ncbi:division/4
(iii)
ncbi:division/2
rdfs:label
‘‘Mammals’’
(iv)
et:taxon/34010
rdfs:subClassOf
et:taxon/hirta
(v)
ncbi:taxon/687295
rdfs:subClassOf
ncbi:taxon/513583
(vi)
ncbi:taxon/687295
ncbi:rank
ncbi:Species
(vii)
ncbi:taxon/687295 ncbi:scientific name ‘‘Coleophora cornella’’
(viii)
ncbi:taxon/35525
eol:habitat
ENVO:00000873
(ix)
ncbi:taxon/35525
eol:presentIn
worms:Oostende
(x)
et:test/001
et:compound
et:chemical/115866
(xi)
et:test/001
et:species
et:taxon/26812
(xi)
et:test/001
et:organsimLifestage
et:lifestage/adult
(xiii)
et:taxon/33155
owl:sameAs
ncbi:taxon/311871
(xiv)
ncbi:taxon/311871
owl:sameAs
wd:Q13828695
(xv)
et:chemical/115866
owl:sameAs
wd:Q418573
Table 3: Example triples from the TERA knowledge graph.
Eﬀect API The tabular data in ECOTOX requires signiﬁcantly more cleaning
than the other data. We use the namespace https://cfpub.epa.gov/ecotox/
(et) for this part of TERA.
1. ECOTOX contains metadata about the species and compounds used in the
experiments. We use this information to aim alignment between the eﬀect
and the background data.
(a) Species metadata in species.txt include common and Latin names, along
with a (species) ECOTOX group. This group is a categorization of the
species based on ECOTOX use cases. We ﬁlter the species names, e.g.,
sp., var. (i.e., unidentiﬁed species and variant) are removed along with
various missing value shorthands used in the metadata.
(b) The full hierarchical lineage is also available in the species.txt ﬁle. Each
column represent a taxonomic level, e.g., genus or family. If a column
is empty, we construct a intermediate classiﬁcation, e.g., say Daphnia
magna has no genus classiﬁcation in the data, then its classiﬁcation will
be Daphniidae genus (family name + genus, actually called Daphnia).
We construct these classiﬁcations to ensure the number of levels in the
taxonomy is consistent. This consistency will help when aligning to the
NCBI data. Note that when adding triples such as (iv) in Table 3, we
also add a classiﬁcation based on the column to aid easier querying for
a speciﬁc taxonomic level.
(c) Chemical metadata in chemicals.txt is handled similarly, the data in-
cludes chemical name and a (compound) ECOTOX group.
2. The eﬀect data consist of two parts, a test deﬁnition and results associated
with that test. Note that a test can have multiple results. An example of
triples associated with a test is shown in Figure 3.


## Page 9


TERA: the Toxicological Eﬀect and Risk Assessment Knowledge Graph
9
Fig. 3: Example of a ECOTOX test and related triples.
(a) The important aspects of a test is the compound and the species used,
other columns include metadata, but these are optional and often empty.
Each result gives an endpoint, an eﬀect (e.g., chronic or mortal), and a
concentration and unit at which the endpoint and eﬀect where recorded.
(b) We construct a node of type result (e.g., et:result/001) and link each
result component to it.
For the units in the eﬀect data, e.g., chemical concentrations (mg/L, mol/L,
mg/kg, etc.), we reuse the QUDT9 ontologies. Where a unit is not deﬁned, such
as mg/L, we deﬁne it as shown in Listing 1.
@prefix rdf:
<http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:
<http://www.w3.org/2000/01/rdf-schema#> .
@prefix qudt: <http://qudt.org/schema/qudt#> .
@prefix et:
<https://cfpub.epa.gov/ecotox> .
et:MilligramPerLiter
rdf:type qudt:MassPerVolumeUnit, qudt:SIDerivedUnit, qudt:DerivedUnit ;
rdfs:label "Milligram per Liter"^^xsd:string ;
qudt:abbreviation "mg/L"^^xsd:string ;
qudt:conversionMultiplier 0.000001 ;
qudt:conversionOffset 0.0 ;
qudt:symbol "mg/dm^3"^^xsd:string .
Listing 1: Unit deﬁnition of mg/L using QUDT.
Data alignment API. We use various techniques to align the datasets de-
scribed above.
ECOTOX-NCBI (Species). There does not exist a complete and public align-
ment between ECOTOX species and the NCBI taxonomy. There exists a partial
9 http://qudt.org/1.1/schema/qudt#


## Page 10


10
E. B. Myklebust et. al.
Method
#mappings
Recall
Levensthein
LogMap
AML
Levenshtein
14915
1.0
0
6711
12611
LogMap
12612
0.99
4408
0
10373
AML
4299
0.71
1995
2060
0
Intersection
1979
0.71
Table 4: Alignment results (left of double line) and disagreement between meth-
ods (right of double line). Intersection is the mappings which are common across
all methods.
mapping curated by experts through the ECOTOX search interface,10 we have
gathered a total of 929 mappings for validation purposes. We use three methods
for aligning the two vocabularies.
(i) String matching. We use the Levenshtein distance [17] between labels of
the entities.
(ii) LogMap ontology alignment tool [18,19].
(iii) AgreementMakerLight (AML) ontology alignment tool [20].
As shown in Table 4, the methods achieved high recall over the reference map-
pings, with Levensthein and LogMap covering all and almost all the reference
mappings. Table 4 also show the disagreement between methods, which we deﬁne
as |S1 \ S2|, where S1 and S2 are the sets of computed mappings for methods 1
and 2. The disagreement shows that even though AML has the lowest recall, it
still suggest a large amount of mappings not discovered by the other methods.
This suggests that further analysis of the mappings are required and that a con-
sensus among the diﬀerent systems will be necessary. Note that, both AML and
LogMap exploit the semantics of the input knowledge graphs and implement
mapping repair techniques to minimize logical errors in the integration. Such
functionality is missing in pure lexical methods like the Levenshtein distance
and may lead to noise in the alignment.
NCBI-Wikidata (Species). The use of more external sources (e.g., EOL, MeSH,
Freebase) requires a mapping from NCBI identiﬁers. We construct equivalence
triples between NCBI identiﬁers and Wikidata entities using query shown in
Listing 2. This query is then used on the Wikidata endpoint.11
ECOTOX-Wikidata (Compounds). By mapping ECOTOX chemical identiﬁers
(CAS) to Wikidata entities, we enable the use of a vast external chemical
datasets, e.g., PubChem, ChEBI, KEGG, ChemSpider, MeSH, UMLS, to name
a few. The construction of equivalence triples is shown in Listing 3.
10 https://cfpub.epa.gov/ecotox/search.cfm
11 https://query.wikidata.org/sparql


## Page 11


TERA: the Toxicological Eﬀect and Risk Assessment Knowledge Graph
11
PREFIX owl: <http://www.w3.org/2002/07/owl#> .
PREFIX wdt: <http://www.wikidata.org/prop/direct/> .
CONSTRUCT {?ncbitaxon owl:sameAs ?taxon .}
WHERE {
?taxon wdt:P685 ?ncbi .
BIND(IRI(
CONCAT("https://www.ncbi.nlm.nih.gov/taxonomy/taxon/",
?ncbi)) AS ?ncbitaxon)
}
Listing 2: Construct mapping between NCBI and Wikidata.
PREFIX owl: <http://www.w3.org/2002/07/owl#> .
PREFIX wdt: <http://www.wikidata.org/prop/direct/> .
CONSTRUCT {?etcompound owl:sameAs ?compound .}
WHERE {
?compound wdt:P231 ?cas .
BIND(IRI(
CONCAT("https://cfpub.epa.gov/ecotox/chemical/",
REPLACE(?cas,'-',''))) AS ?etcompound)
}
Listing 3: Construct mapping between ECOTOX and Wikidata.
4.3
Accessing TERA
The knowledge in TERA can be accessed via SPARQL queries or via the pre-
deﬁned APIs introduced in Section 4.2. The (ﬁnal) output will depend on the
required task, and can be given either as a graph or in tabular format.
SPARQL queries. For researchers competent in SPARQL the most powerful
method for accessing data in TERA is via SPARQL queries. TERA provides an
improved and intuitive method for accessing eﬀect data over the current tabular
data base structure. We will here give an example of the usability of TERA in
extracting data for a risk assessment case study.
As an example, we have gathered water samples from the inner Oslofjord.
Then, we can extract the compounds and concentrations, at which, the species in
the Oslofjord experience lethal eﬀects, as shown in Listing 4. The concentrations
can then be compared with water samples (exposure) to see if the populations
are at risk from contaminants.12
Predeﬁned APIs. In addition to SPARQL queries for extracting data from
the knowledge graph, the TERA APIs povide predeﬁned methods which enable
access to the data without being proﬁcient in SPARQL,13 but rather prefer a
scripting language (here, we use Python).
12 The comparison can be done with another (case study) API. However, this uses only
private data and therefore is not included here.
13 Methods are, for the most part, abstractions of SPARQL queries.


## Page 12


12
E. B. Myklebust et. al.
PREFIX eol: <http://eol.org/schema/terms/> .
PREFIX et:
<https://cfpub.epa.gov/ecotox/> .
SELECT ?s ?c ?conc ?concunit
WHERE {
?s
eol:endemicTo [ rdfs:label "Oslofjorden"@no ] .
_:b a et:Test ;
et:species ?s .
et:compound ?c .
et:hasResult [
et:endpoint et:LC50 ;
et:effectType et:ACUTE ;
et:concentration [ rdf:value ?conc ;
unit:units ?concunit ] .
]
}
Listing 4: Query to select all species, compounds, and concentrations and unit,
where the species is endemic to the Oslofjord.
1. In addition to classiﬁcation, sibling, and name queries, the Species API has
methods for fuzzy querying of identiﬁers based on close matched names. This
is a necessary feature, since the name deﬁnition may vary from user to user.
2. As mentioned before, not all chemical features are included in the TERA
knowledge graph, purely for practical reasons. Therefore, fetching features
from PubChem is a method in the API. We also include methods for other
properties available in PubChem, such as chemical ﬁngerprints, which is
a string of bits representing the presence or absence of selected chemical
properties.
3. For convenience, the Chemical API has methods which wrap SPARQL queries
over endpoints or local instances of PubChem, ChEBI or MeSH. This also
includes methods for easily converting between identiﬁers.
4. The Eﬀect API has also methods that wrap SPARQL queries over the gen-
erated knowledge graph.
5
TERA Applications
In this section, we describe potential uses of TERA that complement the data
access application in the ecotoxicological domain.
Benchmarking embedding models. TERA can be used to benchmark exist-
ing knowledge graph embedding models for the speciﬁc task of eﬀect prediction.
This task uses the three parts (eﬀect, chemical, and taxonomy) separately, where
the chemical and taxonomy knowledge graphs are embedded and thereafter used
in a prediction model. In [1] we showed that the use of knowledge graph embed-
ding models drastically improved prediction results over a deterministic graph
distance approach. However, the work also showed that using embedding mod-
els in this novel setting revealed a few shortcomings. First, TERA is majority


## Page 13


TERA: the Toxicological Eﬀect and Risk Assessment Knowledge Graph
13
Dataset
Relational density
Entity density
Absolute density
TERA (ECOTOX)
354k
4
1.1 × 10−6
TERA (NCBI)
433k
12
2.9 × 10−6
TERA (full)
42k
9
1.1 × 10−6
YAGO3-10
29k
18
7.1 × 10−5
FB15k
359
65
2.1 × 10−3
FB15k-237
1148
38
1.3 × 10−3
WN18
7858
7
8.4 × 10−5
WN18RR
3
4
5.5 × 10−5
Table 5: Densities of benchmark datasets.
hierarchical, which could not be properly represented in the embeddings. Eﬀorts
have been made to represent hierarchies (e.g., Poincare embeddings [21]), how-
ever, we are not aware of models capable of simultaneous capture of horizontal
and vertical relations [22]. Second, sparsity has a large eﬀect on the perfor-
mance of knowledge graph embedding models [23]. Table 5 show the sparsity of
common benchmark datasets and TERA (literals removed). TERA (ECOTOX)
and TERA (NCBI) refers to the parts of the knowledge graph that was gener-
ated from ECOTOX and NCBI, respectively. TERA (full) contains all data in
the materialized snapshot from [2]. We follow [23] and calculate the relational,
RD = |T|/|R|, and entity density, ED = |T|/|E|, where T, R, and E are the set
of triples, relations, and entities in the knowledge graphs respectably. In addi-
tion, we calculate the absolute density of the graph, which is |T|/(|E|(|E| −1)).
This is the ratio of edges to the maximum number of edges possible in a simple
directed graph [24].
In Table 5 we can see that TERA (all) has a high RD, which is down to the
mostly hierarchical structure which use the rdfs:subClassOf relation. We see
that TERA has similar ED as WN18RR which is a datasets where embedding
models has less predictive performance than on e.g., FB15k [25]. The absolute
density of TERA is one order of magnitude lower than WN18 and YAGO3-10.
This makes TERA a very challenging knowledge graph for the next generation
of embedding models.
TERA as background knowledge. The prediction problem above use the
knowledge graph outright. However, using TERA as background knowledge
where other methods for extrapolating toxicity of chemicals exists is a possi-
ble application. These methods often use chemical features, images, ﬁngerprints
and so on as input, and machine learning methods such as Convolutional Neural
Networks and Random Forests as prediction models [26,27]. These models are of-
ten uninterpretable, and the predictions lack domain explanations. For machine
learning tasks such as preprocessing, feature extraction, transfer and zero/few-
shot learning TERA can provide context. Furthermore, the knowledge graph is
a possible source for the (semantic) explanation of the predictions (e.g., [28]).


## Page 14


14
E. B. Myklebust et. al.
Alignment between ECOTOX and NCBI. As mentioned in Section 4.2,
there does not exist a complete and public alignment between ECOTOX species
and the NCBI taxonomy. Therefore the computed mappings can also be seen
as a very relevant resource to the ecotoxicology community. The used alignment
techniques achieve high scores for recall over the available (incomplete) reference
mappings. However, aligning such large and challenging datasets requires prepro-
cessing before ontology alignment systems can cope with them. We removed all
nodes which did not share a word (or shared only a stop word) in labels across
the two taxonomies. This quartered the size of ECOTOX and reduced NCBI
50 fold. However, the possible alignment between entities without labels is lost
when reducing the dataset size. Thus, the alignment of ECOTOX and NCBI has
the potential of becoming a new track of the Ontology Alignment Evaluation
Initiative (OAEI) [29] to push the limits of large scale ontology alignment tools.
Furthermore, the output of the diﬀerent OAEI participants could be merged
into a rich consensus alignment that could become the reference to integrate
ECOTOX and NCBI.
6
Discussion and Conclusion
We have created a knowledge graph called TERA and accompanying tools. This
knowledge graph aims at covering the knowledge and data relevant to the eco-
toxicological domain. We have also shown the applications of the knowledge
graph, including data retrieval and eﬀect prediction. These applications show
the beneﬁts of having a integrated view of the diﬀerent knowledge and data
sources.
Knowledge graph. The creation of TERA is of great importance to future
eﬀect modelling and computational risk assessment approaches within ecotox-
icology, whose strategic goal is designing and developing prediction models to
assess the hazard and risks of chemicals and their mixtures where traditional
laboratory data cannot easily be acquired. Diﬀerent knowledge and data sources
are integrated into TERA, which aims at consolidating the relevant informa-
tion to the ecological risk assessment domain. The adaption of a RDF-based
knowledge graph enables the use of an extensive range of Semantic Web infras-
tructure (e.g., reasoning engines, ontology alignment systems, SPARQL query
engines). The accompanying tools enables us to draw conclusions on the eﬀect
data from background knowledge, and extrapolate on it. TERA enables an inte-
grated and semantic access across data sets, and facilitate resource-eﬀective and
transparent approaches to optimise this work. Moreover, the contribution is in
line with a larger shift in ecological risk assessment towards the use of artiﬁcial
intelligence [30].
Value. The data integration eﬀorts and the construction of the TERA knowledge
graph goes in line with visions in the computational risk assessment communi-
ties (e.g., Norwegian Institute for Water Research’s Computational Toxicology
Program (NCTP)), where increasing the availability and accessibility of knowl-
edge enables optimal decision making. For the semantic web community TERA


## Page 15


TERA: the Toxicological Eﬀect and Risk Assessment Knowledge Graph
15
provides a unique dataset which can be used to benchmark new solutions for
knowledge graph embedding or in prediction problems.
Resources. The knowledge graph is available for download from Zenodo [2].
This download includes all necessary links to the PubChem, ChEMBL, MeSH,
EOL, and Wikidata datasets. We also provide a materialized snapshot of TERA.
The APIs are available from GitLab [3] Moreover, given the frequency with
which ECOTOX is updated (quarterly), the repository also contains a script for
updating the TERA knowledge graph.
Maintenance. The construction of TERA is a part of a PhD project. After the
ﬁnalization of the PhD, there are already plans to maintain and evolve TERA
within the Norwegian Institute for Water Research (NIVA) as the use of TERA
falls into one of the main research lines of NIVA’s Computational Toxicology Pro-
gram (NCTP). We also expect an engagement from the ecotoxicology community
since there is a growing interest in applying artiﬁcial intelligence solutions [30].
Acknowledgements
This work is supported by grant 272414 from the Research Council of Norway
(RCN), the MixRisk project (RCN 268294), the AIDA project, The Alan Turing
Institute under the EPSRC grant EP/N510129/1, the SIRIUS Centre for Scal-
able Data Access (RCN 237889), the Royal Society, EPSRC projects DBOnto,
MaSI3 and ED3, and is organized under the Computational Toxicology Pro-
gram (NCTP) at NIVA. We would also like to thank Martin Giese and Zoﬁa C.
Rudjord for their contribution in diﬀerent stages of this project.
References
1. E. B. Myklebust et al. Knowledge Graph Embedding for Ecotoxicological Eﬀect
Prediction. In Int’l Sem. Web Conf. (ISWC), 2019.
2. E. B. Myklebust et al. Toxicological Eﬀect and Risk Assessment (TERA) Knowl-
edge Graph (Version 1.0.0) [Data set], Dec 2019.
https://doi.org/10.5281/
zenodo.3559865.
3. E. B. Myklebust et al. RAPPT: APIs for (pre)processing ecological risk assessment
data and creating TERA, Dec 2019. https://gitlab.com/Erik-BM/rappt.
4. P. Pradeep et al. An ensemble model of QSAR tools for regulatory risk assessment.
Journal of cheminformatics, 8:48–48, 2016.
5. T. I. Netzeva et al. Review of (quantitative) structureactivity relationships for
acute aquatic toxicity. QSAR & Combinatorial Science, 27(1):77–90, 2008.
6. S. Wu et al. A framework for using structural, reactivity, metabolic and physico-
chemical similarity to evaluate the suitability of analogs for sar-based toxicological
assessments. Regulatory Toxicology and Pharmacology, 56(1):67 – 81, 2010.
7. H. Arnaout and S. Elbassuoni. Eﬀective Searching of RDF Knowledge Graphs.
Web Semantics: Science, Services and Agents on the World Wide Web, 48(0),
2018.
8. A. Agibetov et al. Supporting shared hypothesis testing in the biomedical domain.
J. Biomedical Semantics, 9(1):9:1–9:22, 2018.


## Page 16


16
E. B. Myklebust et. al.
9. J. Euzenat and P. Shvaiko. Ontology Matching, Second Edition. Springer, 2013.
10. U.S. EPA. ECOTOXicology knowledgebase (ECOTOX), 2019.
11. D. Vrandecic and M. Kr¨otzsch.
Wikidata: a free collaborative knowledgebase.
Commun. ACM, 57(10):78–85, 2014.
12. E. Willighagen. InChIKey collision: the DIY copy/pastables, 2011.
13. S. R. Heller et al. InChI, the IUPAC International Chemical Identiﬁer. Journal of
Cheminformatics, 7(1):23, 2015.
14. S. Kim et al. PubChem 2019 update: improved access to chemical data. Nucleic
Acids Research, 47(D1):D1102–D1109, 10 2018.
15. E. W. Sayers et al. Database resources of the National Center for Biotechnology
Information. Nucleic Acids Research, 37(suppl 1):D5–D15, 10 2008.
16. C. S. Parr et al. The encyclopedia of life v2: Providing global access to knowledge
about life on earth., 2014.
17. V. I. Levenshtein. Binary Codes Capable of Correcting Deletions, Insertions and
Reversals. Soviet Physics Doklady, 10:707, Feb 1966.
18. E. Jim´enez-Ruiz and B. Cuenca Grau. LogMap: Logic-Based and Scalable On-
tology Matching. In 10th International Semantic Web Conference, pp. 273–288,
2011.
19. E. Jim´enez-Ruiz et al.
Large-scale interactive ontology matching: Algorithms
and implementation. In the 20th European Conference on Artiﬁcial Intelligence
(ECAI), pp. 444–449. IOS Press, 2012.
20. D. Faria et al. The agreementmakerlight ontology matching system. In R. Meers-
man et al., editors, On the Move to Meaningful Internet Systems: OTM 2013 Con-
ferences, pp. 527–541, Berlin, Heidelberg, 2013. Springer Berlin Heidelberg.
21. M. Nickel and D. Kiela. Poincar Embeddings for Learning Hierarchical Represen-
tations, 2017.
22. O. M. Holter et al. Embedding owl ontologies with owl2vec. CEUR Workshop
Proceedings, 2456:33–36, January 2019.
23. J. Pujara et al. Sparsity and noise: Where knowledge graph embeddings fall short.
In Proceedings of the 2017 Conference on Empirical Methods in Natural Language
Processing, pp. 1751–1756, Copenhagen, Denmark, September 2017. Association
for Computational Linguistics.
24. T. F. Coleman and J. J. Mor. Estimation of sparse jacobian matrices and graph
coloring blems. SIAM Journal on Numerical Analysis, 20(1):187–209, 1983.
25. T. Dettmers et al. Convolutional 2d knowledge graph embeddings. 02 2018.
26. Y. Wu and G. Wang. Machine Learning Based Toxicity Prediction: From Chem-
ical Structural Description to Transcriptome Analysis.
International journal of
molecular sciences, 19(8):2358, Aug 2018.
27. H. Yang et al. In silico prediction of chemical toxicity for drug design using machine
learning methods and structural alerts. Frontiers in chemistry, 6:30, 2018.
28. F. L´ecu´e and J. Wu. Semantic explanations of predictions. CoRR, abs/1805.10587,
2018.
29. A. Algergawy et al. Results of the ontology alignment evaluation initiative 2018.
In 13th International Workshop on Ontology Matching, pp. 76–116, 2018.
30. C. Wittwehr et al. Artiﬁcial intelligence for chemical risk assessment. Computa-
tional Toxicology, pp. 100114, 2019.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
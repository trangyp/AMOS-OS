---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1801.05058v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1801.05058v1_Predictive_Systems_Toxicology

> Source: 1801.05058v1_Predictive_Systems_Toxicology.pdf

> Pages: 37

---


## Page 1


1
Predictive Systems Toxicology 
Narsis A. Kiani*124 , Ming-Mei Shang14 , Hector Zenil124, Jesper Tegner*134 
1 Unit     of     Computational     Medicine,     Center     for     Molecular     Medicine,     Department     of     Medicine,     Solna,    
Karolinska    Institutet,    Stockholm,    171    76,    Sweden 
2 Algorithmic     Dynamics     Lab,    Center     for     Molecular     Medicine,     Karolinska     Institutet,     Stockholm,     171     76,    
Sweden 
3  Biological     and     Environmental     Sciences     and     Engineering     Division,     Computer,     Electrical     and     
Mathematical    Sciences     and     Engineering     Division,     King     Abdullah     University     of     Science     and     
Technology     (KAUST),     Thuwal    23955–6900,    Kingdom    of    Saudi    Arabia 
4 Science for Life Laboratory, 171 21 Solna, Sweden 
  *Correspondence should be  addressed to  narsis.kiani @ki.se and Jesper.Tegner @ki.se 
 
ABSTRACT: 
In this review we address to what extent computational techniques can augment our ability to 
predict toxicity. The first section provides a brief history of empirical observations on toxicity 
dating back to the dawn of Sumerian civilization. Interestingly, the concept of dose emerged 
very early on, leading up to the modern emphasis on kinetic properties, which in turn encodes 
the insight that toxicity is not solely a property of a compound but instead depends on the 
interaction with the host organism. The next logical step is the current conception of evaluating 
drugs from a personalized medicine point-of-view. We review recent work on integrating what 
could be referred to as classical pharmacokinetic analysis with emerging systems biology 
approaches incorporating multiple omics data. These systems approaches employ advanced 
statistical analytical data processing complemented with machine learning techniques and use 
both pharmacokinetic and omics data. We find that such integrated approaches not only 
provide improved predictions of toxicity but also enable mechanistic interpretations of the 
molecular mechanisms underpinning toxicity and drug resistance. We conclude the chapter by 
discussing some of the main challenges, such as how to balance the inherent tension between 
the predicitive capacity of models, which in practice amounts to constraining the number of 
features in the models versus allowing for rich mechanistic interpretability, i.e. equipping 
models with numerous molecular features. This challenge also requires patient-specific 
predictions on toxicity, which in turn requires proper stratification of patients as regards how 
they respond, with or without adverse toxic effects. In summary, the transformation of the 
ancient concept of dose is currently successfully operationalized using rich integrative data 
encoded in patient-specific models.  
Key words Toxicology, Systems Biology , Network Pharmacology, Algorithmic Complexity


## Page 2


2
A brief history of Toxicology – from Sumerian drugs to pharmacokinetic 
analysis of toxicity  
There are numerous examples of “drug” usage in ancient times. The first documented 
evidence of drug receipts is believed to be approximately 5000 years old, on a 
Sumerian clay slab [1]. In contrast to the long history of using substances from plants 
for therapeutic purposes, it was only a couple of hundred years ago that people 
realized the hazards of these substances. This insight can be expressed as “All 
substances are poisons; there is none which is not a poison. The right dose 
differentiates a poison and a remedy” [2]. While Paracelsus (1493-1541) had this key 
insight, the boundary between poison and remedy is hazy. The toxicity of individual 
chemicals is indeed a complex feature which itself depends on several factors, such 
as dose, chemistry, individual genetic make-up and exposure to environmental 
conditions, which all play key roles, to different degrees, in determining susceptibility 
to disease and adverse drug responses. In modern times it has become increasingly 
evident that it is not the case that each medicine works equally well, as regards both 
efficacy and safety, in individuals in a population—hence the rationale behind the idea 
of personalized medicine [3]. Following the work of Paracelsus, Mathieu Orfila (1787-
1853) first described specific organ damage caused by toxins. Toxicity studies of 
individual substances using animals began in 1920. J.W. Trevan proposed the concept 
of a 50% lethal dose (LD50), defining the lethal dose of individual chemicals. As a new 
subject, the field of toxicology slowly developed until the occurrence of the thalidomide 
disaster in the early 1960s, one of the gloomiest episodes in pharmaceutical history. 
The drug was approved as a mild sleeping pill with a good safety profile and beneficial 
effects on morning sickness in pregnant women. However, this caused thousands of 
babies worldwide to be born with malformed limbs in less than 4 years. Since then, all


## Page 3


3
regulatory agencies have made it obligatory to report the toxicity profiles of 
Investigational New Drugs (IND). In the late 1980s, the Organization for Economic Co-
operation and Development (OECD) and the International Conference on 
Harmonization (ICH) brought out the guidelines for the toxicity testing of 
pharmaceutical substances, which are still in use, supplemented with occasional 
amendments. In the context of regulatory guidelines, the lowest dose able to induce 
adverse effects (LOAEL) and the highest dose without observable adverse effects 
(NOAEL) must be tested to extrapolate the derived no-effect level (DNEL), which is 
more useful in defining the appropriate dose in clinical trials. Other conventional toxicity 
testing includes repeated dose toxicity testing, carcinogenicity testing, one-generation 
reproduction toxicity testing, and two-generation reproduction toxicity testing, et al. 
These depend on the formulation and indication of the drug. The toxicity testing of 
pharmaceuticals depends strongly on different animal models. Not surprisingly, such 
an evaluation is expensive (reported to cost more than $3B per year), time-consuming 
(two-generation reproduction toxicity testing takes around 2 years), suffers from low 
throughput, and in some cases raises ethical concerns relating to animal welfare [3]. 
The low throughput of toxicity testing methods has serious consequences for public 
health, as 86% of chemicals (not limited to drugs) currently on the market lack the 
necessary toxicity data [4, 5]. The most controversial issue is the translational 
efficiency of those compounds being tested in humans [6]. No doubt, the current 
toxicity model is not optimal, motivating both regulatory authorities and pharmaceutical 
companies to promote innovative alternatives to limit the use of animals and to better 
assess the risk of drug candidates as early as possible. In 2003, an EPA report 
proposed a computational toxicology research agenda promising several advantages, 
including prioritizing candidates and developing predictive models for quantitative risk


## Page 4


4
assessment. Yet the use of computational methods to predict toxicity has a history in 
toxicology. In 1962, Hansch et al. developed a Quantitative Structure-Activity 
Relationship (QSAR) model to estimate the concentration of chemicals using the 
octanol/water partition and the Hammett constant, which laid the foundation for in silico 
toxicity prediction [7]. Numerous tools were developed to predict carcinogenicity, 
mutagenicity, and developmental toxicity using pre-built QSAR models such as TopKat 
and METEOR, most of which have been modified and are currently deployed in 
academia and the pharmaceutical industry [8] . QSAR models provide a wide range of 
complexity for toxic endpoints, given flexible feature selection, i.e. qualitative and 
quantitative toxicity plus molecular descriptors can be used. Yet, QSARs require a 
large dataset to produce robust statistics, which makes the framework less useful in 
applications where data is limited. Benezra [9] used structural alerts (SAs) (also called 
toxicophores/toxic fragments) for skin sensitization in 1982, which was more 
practicable and economical with the low throughput experimental technologies 
available at the time. SA based models flourished in toxicity prediction in almost all 
types of toxic endpoint [10, 11]. Several expert systems are available for toxicity 
prediction based on pre-built rules and SAs, e.g. HazardExpert, Oncologic Cancer 
Expert System (OCES), Toxtree, et al.[12–14]. These models are limited to producing 
qualitative binary output, i.e. toxic or non-toxic. Chemical similarity cluster methods 
take into account the structural similarity of chemicals, physiochemical features, ADME 
and mechanisms of action (MoA), which in turn can provide qualitative or quantitative 
predictions depending on the toxicity endpoint [15]. Multiple tools implement this 
approach, such as AMBIT, DSSTox and Toxmatch, with applications including 
prediction of environmental risk, reproductive toxicity, skin sensitization and so on [16–
18]. The statistically-derived rule-based approaches mentioned above share a


## Page 5


5
common limitation, namely, lack of biological insights into the mechanistic basis of 
toxicity. Analogous to pharmacokinetics/pharmacodynamics features indicating the 
mutual interaction of recipient and chemicals, toxicokinetics/toxicodynamics analysis 
selects the toxic response related to the chemical concentration in vivo. Importantly, 
measurement of the internal doses rather than administered doses and key 
metabolites provide a more accurate relationship to the response. In addition, it is a 
well-developed practice to extrapolate between various administration routes, as 
different species use non-identical PK/PD and ADME. However, the toxicity pathway 
and the MoA can only be defined with expert knowledge [19–21]. Drug toxicity is a 
complex response occurring at system, tissue, cellular and molecular levels. Classic 
toxicity testing and prediction methods, using either animals or in silico chemicals, 
similarity based or PK/PD based models, simplified complexity and left the mechanistic 
understanding of the chemical-induced toxicity pathways out of consideration. In 2007, 
the NRC released the report Toxicity testing in the 21st century: A Vision and a 
Strategy, in which it addressed future directions that would take complexity and toxicity 
pathways into account [22].  
From Systems Biology to Systems Toxicology  
The revolution in biomedical science in the post genome era has made it feasible to 
study the effects of chemicals using cells, cellular components and tissues, preferably 
of human origin. High-throughput assay technologies, bioinformatics and systems 
biology have significantly empowered scientists to decipher how molecular 
components, different cells or tissues cooperate to carry out normal physiological 
functions that are key to maintaining health [23, 24]. Three high-throughput assays 
developed in recent decades have provided major impetus to the field of toxicology: 
omics technologies, image techniques, and automated robotic platform techniques.


## Page 6


6
The platforms enable testing of huge numbers of chemicals in a high-throughput 
number of samples under standardized conditions. Omics technologies collect the 
molecular responses to a substance while image methods decode the phenotypical 
and functional change of cells, organs or organisms in response to exposure to a 
compound. Together, these three technologies allow researchers to characterize 
toxicity rapidly at affordable cost [25–27]. As an interdisciplinary field of science, 
bioinformatics combines computer science, statistics, mathematics, and engineering 
to analyze and interpret biological data, and serves as a key tool with which to decode 
the enormous quantum of data generated with high-throughput assays [28]. Since 
2000, Systems Biology had been used widely to “understand biology at the system 
level” using computational and mathematical modeling of complex biological systems 
[29]. The emergence of systems toxicology can be characterized as the integration of 
classical toxicology with the quantitative analysis of large networks of molecular and 
functional changes occurring across multiple levels of biological organization. This is 
in essence a holistic approach to deciphering the impact of environmental agents 
(chemicals, complex mixtures, occupational exposures, physical agents, biological 
agents, and lifestyle factors) on complex biological systems using an engineering 
approach applied to toxicological research [30]. Systems toxicology is rooted in the on-
going revolution in biology and biotechnology, and is founded on the premise that 
morphological and functional changes in cellular, tissue, organ, and organism levels 
are caused by and cause changes at the omics level. One example is the Human 
Toxome project launched by NIH/DDD that is intended to test the strategies that 
combine omics data and computational models, aiming to develop a common, 
community accessible framework [31]. Another is Tox-21c, which focuses on toxicity 
pathways, mechanisms/modes of action, and adverse outcome pathways (AOP) in


## Page 7


7
humans. Tox-21c largely overlaps with 3Rs (replace, reduce, and refine) proposed half 
a century ago [32, 33]. The Systems Toxicology computational challenge, sbv 
IMPROVER computational challenge, used crowd resourcing to demonstrate that gene 
expression data from blood cells are sufficiently informative to predict response to 
smoking in humans and across species translation [34].  
Yet, a comprehensive understanding of the mechanisms of drug toxicity in specific 
cases requires the integration of different data modalities, from changes at the 
genomic, proteomic, and metabolomics level across several scales of cellular 
organization. In contrast to classical approaches, systems toxicology resides at the 
intersection of systems biology and toxicology where chemistry incorporates 
mechanisms into the predictive framework [35]. To understand how this complex 
interaction system in cells and tissues leads to toxicity requires the integration of two 
disciplines that have been increasingly useful in biomedical research: “Systems 
Biology” and “Quantitative Pharmacology”. In systems biology, a system is generally 
described as a set of nodes (vertices) connected by edges describing functional 
interactions. These edges can represent physical interactions, functional interactions, 
and connections between data across several scales. Similarly, in systems toxicology 
biological networks are the basis for the prediction of drug action in complex biological 
systems[36]. 
Systems toxicology models contain expressions that characterize functional 
interactions within a biological network, which are very useful when drugs act at 
multiple targets in the network or when homeostatic feedback mechanisms are 
operative[37]. Therefore, these models are particularly useful in describing complex 
patterns of drug action such as synergies between different drugs. Although systems 
toxicology is still in its infancy, it has tremendous potential to change the way we


## Page 8


8
approach biomedical research. It represents a movement beyond a traditional study-
centric approach towards a continuous quantitative integration of data across studies 
and the different phases of drug development. Network-based approaches offer a wide 
range of possibilities for deciphering and possibly for understanding the complexity of 
human disease, thereby providing new tools with which to develop novel drugs. Here 
we review some current efforts and recent methods through the lens of quantitative 
systems pharmacology (QSP). 
 
Examples of Predictive Systems Toxicology 
The general notion of a network-based approach rests upon the ambition to connect 
several entities across the molecular, cellular pathways, organs and systems to 
facilitate the prediction of the effect of a drug candidate or any kind of perturbation on 
biological outcomes of interest [38, 39]. The way in which one defines or infers a 
network from data is the main determining factor of the degree of reliability and 
applicability of network analysis in drug design. It is crucial to have a clear definition of 
network nodes early on, edges and edge weights in the specific application case, and 
in that context to consider data quality and refinements of the data based on genetic 
variability, aging, environmental effects. Different types of networks such as networks 
of chemical compounds, signaling networks, gene-gene interaction networks, protein-
protein interaction (PPI) networks or metabolic networks and disease networks can be 
(and have been) used in QSP models and methods [40] . Following the work on 
inferring a network comes the analysis of the network and its properties. In the last 
step, the result of analysis needs to be converted to a series of actionable hypotheses, 
which then need to be tested and validated or refuted (see Fig1).


## Page 9


9
Drug–target interaction is the first and most common type of network analysis that has 
been used in QSP models. Interactions between drugs and targets can facilitate the 
process of drug discovery by deciphering a drug's mechanism of action, thereby 
assisting researchers seeking new targets for an old (FDA approved) drug as well as 
new drug candidates for a known target [41–45]. The main source of information in 
reconstruction of the Drug- Target interaction network (DTN) is the Drug Bank, which 
is one of the major publicly available integrated sources of drugs and targets. It is a 
highly comprehensive database combining chemical properties and detailed clinical 
information about drugs and their targets. It also provides drug-related data feeds for 
well-known databases such as Uniprot, PubChem, PDB and KEGG [46, 47]. 
In spite of the fact that mining drug-target interaction data is increasing at an amazing 
rate [42], drug-target interaction data currently available from public sources are largely 
incomplete and biased toward targets of common therapeutic interest [48–50]. 
Biochemical experiments or in vitro methods for finding drug–target interaction are 
costly and time-consuming. An attempt to address the issue of data completeness of 
drug-target interaction involves using in silico methods [51]. For example, docking 
simulations are extensively used in pharmacology. AutoDock [52] is one of the most 
complete suites of free open–source software for the computational docking and virtual 
screening of small molecules to macromolecular receptors. Xie et al. identified drug 
off-targets by docking the drug into protein binding pockets similar to those of its 
primary target, followed by mapping the proteins with the best docking scores to known 
biological pathways, thus predicting potential side effects[53].Classically, the process 
starts with a target of known three-dimensional structure, and docking is used to predict 
the bound conformation and binding energy. In most cases, the three-dimensional 
structure of a target is needed to compute the binding of each drug candidate to the


## Page 10


10
target, which for many targets are still unavailable [54–56]. Wallach et al. have 
developed a method to mitigate the impact of this important limitation. They utilize a 
dataset where there is a pairing of drugs with their observed adverse drug reactions 
(ADRs), the protein structure database and in silico virtual docking to identify putative 
protein targets for each drug and search for correlated pairs of side effects and 
biological pathways [57]. Another challenge when performing docking simulation is that 
it is computationally expensive and most of the methods must simplify the problem to 
make the computation feasible. The reduction of conformational space by imposing 
limitations on the system, such as fixed bond angles and lengths in the ligand or a 
simplified scoring function such as those based on empirical free energies of binding 
to score poses quickly at each step of the conformation search, are the most common 
short-cuts that are currently used in the field [52, 58]. 
 In a more recent effort, machine-learning approaches have been used for larger-scale 
predictions of drug–target interactions. The new interactions between drugs and 
targets can lead to potential insights on previously unidentified side effects for a 
particular drug. This idea is the basis of another category of systems toxicology 
methods. Machine learning-based methods mostly use structural and chemical 
descriptors of drugs and sequences of targets, similarity matrix or (and) any other 
pharmacological information about drugs as input. Then they use any machine learning 
method, such as support vector machines (SVMs) or kernel regression, for predicting 
the drug–target interactions [59–63]. Cobanoglu et al. used the known interactions in 
the Drug Bank in the form of a bipartite network to train a model that represents each 
drug and target as a vector of latent variables and assigns weights to drug-target 
interactions using probabilistic matrix factorization [64]. Approaches that use similarity 
scores as input are more promising than other approaches [41].


## Page 11


11
In general, the use of machine-learning algorithms is one of most promising 
approaches to extracting knowledge from big data using a data-driven framework. 
However, the performance of machine-learning algorithms relies heavily on data 
representations called features, and identifying which features are more appropriate 
for the given task is very difficult. Deep Learning has recently emerged as a promising 
technique where the features do not need to be hand-crafted a priori. Recent success 
has been accomplished thanks to the availability of fast computations, massive 
(labeled) datasets and sophisticated algorithms [65]. Machine learning using deep 
learning is defined by neural networks with multiple hidden layers. Each layer basically 
constructs a feature from the preceding layers [66]. The training process allows layers 
deeper in the network to contribute to the refinement of earlier layers. For this reason, 
these algorithms can automatically engineer or discover features that are suitable for 
representing the data at hand. When sufficient data are available, these methods 
construct features attuned to a specific problem and combine those features into a 
predictor [67]. Deep learning algorithms have shown promise in fields as diverse as 
high-energy physics[68] , dermatology[69], and translation[70]. DEEPtox is one of the 
first methods using Deep Learning for computational toxicity prediction [65]. DeepTox 
normalizes the chemical representations of the compounds and computes a large 
number of chemical descriptors that are used as input in machine learning methods. 
As a next step, DeepTox trains several models, evaluates them, and combines the 
best of them into ensembles. Finally, DeepTox predicts the toxicity of new compounds. 
In DEEPTox SVMs, random forests, and elastic nets are used for cross-checking, 
supplementing the Deep Learning models, and for ensemble learning to complement 
Deep Neural Networks (DNNs). The networks consist of multiple layers of rectified 
linear units (ReLUs) to enforce sparse representations and counteract the appearance


## Page 12


12
of a vanishing gradient. ReLUs are followed by a final layer of sigmoid output units, 
one for each task. One output unit is used for single-task learning. Stochastic gradient 
descent learning has been used to train the DNNs, and both dropout and L2 weight 
decay were implemented for the DNNs in the DeepTox pipeline for regularizing 
learning and avoiding overfitting. Of note is the fact that DEEPtox outperformed many 
other computational approaches like naive Bayes, support vector machines, and 
random forests in toxicity prediction of 12,000 environmental chemicals.  
The output of all the above-mentioned methods is a DTN, an undirected bipartite 
network composed of two sets of nodes, drugs and targets. DTN have a complex 
topology that reflects the inherently rich polypharmacology of drugs (also known as 
drug repurposing) [51]. The analysis of DTN has recently emerged as an effective 
means to study targets and to identify new targets for known drugs. In one of the very 
first attempts, Ma’ayan et al. [71] reconstructed such a bipartite network, and the nodes 
have been connected if there is an association between a drug and a target on the 
basis of data from the Drug Bank. They report several classes of proteins as better 
targets for drugs based on network statistics and gene ontology. A decade later, Lin et 
al. [72] have followed the same approach to studying the drug–target interaction and 
could characterize the drug–target relations of different kinds of drugs. They showed 
that the number of multi-target new molecular entities (NME) has increased over the 
years, but less than single-target NMEs. In both these cases and several other cases 
in the literature, it has proven useful to analyze the general structure of a network in 
order to extract new knowledge facilitating the classification of drugs and/or their 
targets. Structural (graphical) analysis of a network provides insights into the 
organization and topology of the DTN and targets for hypothesis generation and 
experimental testing. As a rule this is performed through computation and analysis of


## Page 13


13
network parameters–parameters that quantify different aspects of the network’s 
internal structure, such as parameters measuring centrality, a node or more global 
parameters such as modularity index, network density, network entropy or network 
diameter [73]. Several methods have been developed and applied based on network 
topology, graph theory, and cluster analysis (see [8] for a recent review). Methods 
based on the similarity of networks is another set of techniques that have been used 
to uncover novel target or disease-specific changes [74, 75]. A wide range of similarity 
measures have been used in the literature, ranging from intuitive measures such as 
the number of edge changes required to get one network from another or the 
comparison of the top-k nodes to the more complicated ones, such as using an 
ensemble of different model networks, and the distribution of the best-fitting ensemble. 
However, it should be kept in mind that the fundamental question of checking whether 
two given networks have the same structure, network comparison, is computationally 
expensive, and despite extensive progress in the field, it remains one of the greatest 
challenges in the field. For example, it is still not known whether graph isomorphism is 
polynomial solvable or whether it is NP-complete. Therefore most of the current 
methods in the network comparison field are heuristic, which in turn may affect the 
outcome strongly, depending on which kind of prior biases exist in the particular 
method.  
All interactions, from protein-protein interactions (PPI) to gene expression and 
pathways, are useful in the quest to understand the mechanism(s) of interaction 
between drugs and complex diseases. Remez et al. used predicted drug−protein 
interactions obtained with a CT-link in combination gene expression data to obtain a 
projected anatomical profile of a drug and use it for connecting in vitro assays with in 
vivo outcomes and predict potential in in vivo organ toxicities [76, 77].


## Page 14


14
Kuhn et al. used a network based on drug–target interaction data and drug–ADR 
interaction data to systematically predict and characterize proteins that cause drug side 
effects. They integrated phenotypic data obtained during clinical trials with known 
drug–target relations to identify overrepresented protein–side effect combinations [78]. 
Their networks have three types of nodes: drugs, targets, and side effects, and links 
are identified side effect causality predictors. The authors considered overrepresented 
protein-side effect pairs, and hypothesized that such overrepresentation could be 
indicative of causality. Their approach can make predictions for proteins that are the 
targets of a certain number of drugs. In this context, Yildirim et al. used a bipartite 
graph composed of FDA-approved drugs and target proteins in the context of cellular 
and disease networks and quantitatively demonstrated an overabundance of ‘follow-
on’ drugs[79]. The authors overlaid the drug-protein network with a network of physical 
PPI. They demonstrated a significant increase in the number of interacting proteins as 
compared to the average in the PPI network. They used the distance between drugs 
and a drug target and the corresponding disease to show that most drug targets are 
not closer to the disease genes in the protein interaction network than a randomly 
selected group of proteins.  
Similarly, several other approaches have been developed based on the notion of 
expanded drug-target interactions, combined with protein-protein interactions data, in 
order to develop a network-based pharmacology that could better explain the drug-
phenotype relationship, and this approach has been used to predict novel targets and 
drug repositioning [80–85]. For example, Guney et al. in [86]integrated protein–protein 
interaction, drug-disease association and drug-target association data. They analyzed 
the topological characteristics of drug targets with respect to disease proteins and 
showed that for a drug to be effective against a disease, it had to target proteins within


## Page 15


15
or in the immediate vicinity of the corresponding disease module. Such approaches 
were also considered for issues related to drug safety and side effects. Cami et al. 
constructed a network representation of drug-ADR associations for approximately 800 
drugs and ADRs and pharmacological information for toxicity prediction. They 
exploited network structure to predict likely unknown adverse events using a trained 
logistic regression model [87]. Berger et al. used PPI networks to predict and identify 
drugs that likely cause Long QT Syndrome based on both a direct drug-target 
interaction and separate neighborhood [88] . 
Complementary to protein-protein interactions, transcriptomic data and gene 
expression differentiation have been used in drug discovery and safety [88–93]. For 
example, Gottlieb et al. introduced a method for inferring drug-specific pathways [89]. 
They connect known drug associated genes over protein, metabolic and transcriptional 
interaction networks while preferring high confidence interactions participating in 
curated cellular processes. They use their computed pathways to suggest novel drug 
repositioning opportunities, gene-side effect associations, and gene-drug interactions. 
Huang et al. developed a new metric to measure the strength of network connection 
between drug targets to predict the pharmacodynamics of drug-drug interactions [92, 
93]. 
 For the purpose of predicting drug toxicity, in most cases we require a collection of 
experimental data reflecting molecular changes in the context of quantifiable cellular 
changes across different biological scales that are linked to toxicity at the body level 
[35]. So in addition to all the above-mentioned data, systems toxicology depends 
strongly on the quality and scope of databases annotating side effects (SIDER) and 
drug-induced differential gene expression, or a combination thereof [94–97].


## Page 16


16
As an example, Lounkine et al. developed an association metric asking how to prioritize 
those new off-targets that explained side effects better than any known target of a 
given drug, thereby creating a drug–target–adverse drug reaction network [43]. 
Network-based approaches allow the generation of hypotheses about drug-target-
phenotype-side effect associations but currently available interaction data are 
incomplete and the available parts are often non-homogeneous and biased. This 
situation results in the fact that the conclusions of such studies strongly depend not 
only on the quality, but importantly, on the degree of completeness of the data [98]. 
The other relevant point is that most of the suggested approaches in QSP are largely 
based upon the analysis of the structure of a network or on comparison of networks, 
while it has been shown[99] that network dynamics, the study of temporal changes in 
network structures or describing changes of phenotypes of a complex system in the 
state-space, is crucial to understanding the complexity of diseases and the action of 
drugs[39]. In this context Mucha et al. [100] developed the technique of multilayer 
networks, incorporating different types of nodes and edges, in order to follow the 
changes in module structure in a system having multiple and different types of edges. 
Interestingly these methods have also been used to predict drug synergies. However, 
most of them are limited to estimating target links on the PPI network. The advantage 
of using a network-based approach lies in that it helps to explain the hidden molecular 
mechanism of drug synergy from the interactions. Due to their effectiveness, some 
approaches aiming at identifying synergistic drug combinations are based on the 
dynamic simulation of specific subnetworks. However, these models relied on a very 
detailed dynamical model, where the lack of information and the uncertainties involved 
in their kinetics parameters and lots of artificial constraints often limit the usefulness of 
the simulations, resulting in the model working only for a few specific pathways. Kiani


## Page 17


17
et al. developed a novel integrative pipeline for systematic exploration of drug 
combinations as a comprehensive and flexible network-based model in the context of 
the DREAM challenge, a pipeline called HotPPI. Here they constructed a human 
protein interaction network from major PPI resources, and included both 
experimentally validated and computationally predicted interactions. The overall 
procedure resulted in a vast protein interaction network comprising 15,383 proteins 
and 337,413 interactions. Next, PPI was filtered based on targets of the DREAM 
challenge and the top 50 pathways involving these targets (table 1). The filtered PPI 
network comprises 6000 proteins and 16000 interactions. Molecular data are used to 
weigh interaction in our PPI. The main goal of HOTPPI is to find the best combination 
to eliminate cancer cell lines. Therefore any combination that eliminates most 
interactions in a network can cause network collapse followed by death of cancer cells. 
Thus the heat diffusion algorithm is used to predict potential synergistic drug 
combinations by calculating how efficient drugs are in hitting the top 200 selected 
nodes in a network based on their betweenness score. The Hot PPI is generally 
applicable to high-throughput experimental data where the challenge is to select a 
small number of the most promising combinations for further mechanistic studies. 
Using this score, we could rank all possible combinations in a reasonable amount of 
time. Interestingly, we learned that we should not include too many details (i.e. features 
or molecular components) in our network descriptions, since we may shift our 
description from optimal towards the ‘knowledge of everything,’ with the precision of 
the method dropping drastically as a result. This underscores the importance and 
challenge of pruning a large, but for the given application reasonable number of 
features to include in the network model.


## Page 18


18
Pathway maps 
pValue 
Ligand-independent activation of Androgen receptor in Prostate Cancer 
1,203E-15 
Cell adhesion_PLAU signaling 
4,362E-14 
Development_EGFR signaling pathway 
8,380E-14 
Apoptosis and survival_Anti-apoptotic action of Gastrin 
1,451E-13 
K-RAS signaling in pancreatic cancer 
1,920E-13 
Development_G-CSF signaling 
7,018E-13 
Development_Growth factors in regulation of oligodendrocyte precursor cell proliferation 
1,065E-12 
Main growth factor signaling cascades in multiple myeloma cells 
3,352E-12 
Development_VEGF signaling and activation 
5,644E-12 
Main pathways of Schwann cells transformation in neurofibromatosis type 1  
1,107E-11 
Immune response_IL-5 signaling 
1,172E-11 
Signal transduction_PTEN pathway 
1,172E-11 
Immune response_IL-15 signaling 
1,331E-11 
Ovarian cancer (main signaling cascades) 
1,595E-11 
Tissue Factor signaling in cancer via PAR1 and PAR2 
2,309E-11 
Development_EPO-induced Jak-STAT pathway 
2,549E-11 
Apoptosis and survival_HTR1A signaling 
2,864E-11 
Development_GM-CSF signaling 
2,864E-11 
Cytoskeleton remodeling_TGF, WNT and cytoskeletal remodeling 
3,189E-11 
HBV signaling via protein kinases leading to HCC 
3,373E-11 
Development_Delta-type opioid receptor mediated cardioprotection 
4,422E-11


## Page 19


19
Apoptosis and survival_Anti-apoptotic action of membrane-bound ESR1 
5,750E-11 
Translation_Non-genomic (rapid) action of Androgen Receptor 
9,496E-11 
Apoptosis and survival_BAD phosphorylation 
1,525E-10 
Development_Growth hormone signaling via PI3K/AKT and MAPK cascades 
1,525E-10 
Development_Ligand-independent activation of ESR1 and ESR2 
2,960E-10 
Development_Membrane-bound ESR1: interaction with growth factors signaling 
2,960E-10 
Development_VEGF signaling via VEGFR2 - generic cascades 
3,413E-10 
Role of Tissue factor-induced Thrombin signaling in carcinogenesis 
5,194E-10 
Development_CNTF receptor signaling 
7,526E-10 
IL-6 signaling in multiple myeloma 
9,699E-10 
Some pathways of EMT in cancer cells 
9,699E-10 
Development_IGF-1 receptor signaling 
1,164E-09 
Development_FGF-family signaling 
1,164E-09 
Signal transduction_Additional pathways of NF-kB activation (in the cytoplasm) 
1,391E-09 
Development_Growth factors in regulation of oligodendrocyte precursor cell survival 
1,563E-09 
Development_Dopamine D2 receptor transactivation of EGFR 
1,746E-09 
Aberrant B-Raf signaling in melanoma progression 
1,965E-09 
Immune response_TSLP signaling 
2,453E-09 
Development_Prolactin receptor signaling 
3,215E-09 
Development_VEGF-family signaling 
3,751E-09 
Immune response_IL-7 signaling in B lymphocytes 
5,605E-09 
Signal transduction_AKT signaling 
5,605E-09


## Page 20


20
Regulation of Tissue factor signaling in cancer 
5,605E-09 
Immune response_IL-4 signaling pathway 
6,797E-09 
Influence of smoking on activation of EGFR signaling in lung cancer cells 
6,797E-09 
Immune response_TNF-R2 signaling pathways 
8,203E-09 
Development_Role of IL-8 in angiogenesis 
9,139E-09 
Immune response_IL-4 - antiapoptotic action 
9,803E-09 
 
 
Fig. 1 overview of predictive system toxicology approaches 
Network data  
assembly 
Public data bases 
Expanding the 
network by 
combining different 
data bases
Predicting new 
edges using  silico
methods
Analyzing network 
Network structure 
analysis
Network 
comparison
Network dynamics 
Translation 
&Validation
Drug target  
identification
Drug synergy
Drug  repositioning
Drug efficacy 
ADMET side-effects


## Page 21


21
 
Fig. 2 Overview of HotPPI approach 
Information theoretic approach to toxicity  
Both network analysis and pharmacokinetic analysis share a focus and grounding in 
the physical and functional interactions between molecules within the cell or tissue and 
the corresponding drugs. Here the overarching aim is not only to predict but also to be 
able to interpret the mechanism in terms of the underlying biology and chemistry. Since 
the design of new drugs for new targets is difficult, and the prediction problem is easier 
from an inference point-of-view, compared to elucidating the mechanisms driving 
toxicity, complementary approaches are warranted. For example, instead of 
engineering a drug to target the unique pathways or mutations of a tiny subset of 
diseases, drug repositioning, such as the one exemplified in the DREAM challenge, 
involves starting with approved drugs to find combinations that can be used to treat 
diseases different from the ones they have been designed for, with the advantage that


## Page 22


22
approved drugs can bypass much regulation if correctly controlling for the effects they 
can have. Thus prediction and simulation are key. This means that the whole field has 
to move towards causal modeling and functional inference rather than traditional 
statistical classification (e.g. Tanimoto coefficients) or computational simulation based 
on classical geometric approaches (e.g. distance between molecules, grid-based 
docking). To this end, information indexes can facilitate the characterization of drugs 
by the combinatorial and structural properties shared with or at a remove from the 
structural properties of the targets, because just as for any molecule, structure means 
function. Then all these approaches can contribute to determining drug function based 
on the fact that structurally similar molecules usually have similar properties (known as 
“neighborhood behavior”). For example, statins are associated with the heart and 
cholesterol, while morphine, codeine and heroin share structural properties and 
effects. However, algorithmic information-theoretic approaches based on both 
classical information and computability theory introduce predictive causal models that 
go beyond statistical similarities and can find, in principle, similar mechanisms shared 
by sets of drugs with respect to targets and functions. 
It is not difficult to see that complementary regions between drug and target will have 
a similar classical and algorithmic information content, because the structure of one is 
the complement of the other. Another advantage is that these measures are 
parameter-free and thus require no training, even though they can complement and 
guide machine learning approaches [101, 102]. Because drug docking is not invariant 
to, e.g., scaling factors, but information theoretic measures are, they may fail to 
characterize the positive or negative docking properties of a drug. While coarse-
graining techniques may be introduced, algorithmic complexity has the advantage of 
being able to account for scaling effects. The basic idea is the likelihood of a drug being


## Page 23


23
causally generated by a mechanistic model (an algorithm). This is, in general, hard if 
not impossible to find (the problem is uncomputable), but approximations are possible 
and new numerical methods have been advanced complementary to statistical and 
lossless compression approaches that cannot or are very limited at accounting for 
causation. Drugs, and molecules in general, can be represented in many ways (see 
Fig. 3a,b,c), some of which are natural networks or networks representing properties 
of the molecules. Most of these representations are lossless representations, meaning 
that they can reconstruct the primary representation of the molecule that they encode, 
e.g., the simplified molecular-input line-entry system or SMILES. The SMILES of a 
molecule is a string obtained by printing the symbol nodes encountered in a depth-first 
tree traversal of a chemical graph. SMILES can be converted back (almost) uniquely 
to the 2-dimensional representation of a drug.  
Fig. 3 shows some of these network (a,b) and 2-dimensional representations (c), 
together with 2 figures (d,e) plotting 3 information-theoretic indexes, two classical and 
one algorithmic based on the drugs’ contact networks. While the 2 classical indexes 
are the ones most correlated, as one is extracted from the other with the additional 
information of the sequence valence, the length of the algorithmic complexity (Z-axis) 
represents the complexity of a hypothesized model producing the contact network.


## Page 24


24
 
Fig. 3 Drug profiling by (algorithmic) information indexes: (a) The molecular 
(chemical) graph of Atorvastatin (C33H35FN2O5), a member of the drug class known as 
statins used primarily as a lipid-lowering agent for prevention associated with treatment 
of cardiovascular diseases. (b) In a molecular network geographical coordinates and 
shapes are no longer important, but rather their topology (which element is connected 
to which other), which can be built upon (c) the molecular contact map where grey 
scale (left matrix) indicates proximity between each element that can be binarized 
(right) using a cut-off value based on the grey scale median. (d) Algorithmic information 
landscape of more than 4000 drugs from the DrugBank (extracted from the Wolfram 
Language) constructed by taking the entropy of their SMILES codes, the valence 
sequences of each of the elements in their formula (from SMILES), given the 
importance they have for bonding (e) Algorithmic information landscape of the drugs 
involved in the DREAM challenge. Color is determined by the ‘contact map complexity’; 
the less complex (the shorter the length of the algorithm generating it) the closer to 
blue, the longer (more algorithmic-random) the closer to red.


## Page 25


25
Concluding remarks 
Here we have reviewed different attempts to predict toxicity from observations (i.e. the 
Sumerian) to classical pharmacokinetic, advancing to recent integrative systems 
oriented approaches taking more data into account. These systems approaches resort 
to performing advanced statistical analytical data processing complemented with 
machine learning techniques to generate paradigms attempting not only to predict 
toxicity but also to identify (molecular) mechanisms of toxicity. Information theoretic 
approaches can be situated in between, as they are as a rule less dependent upon 
biochemical representations in their problem formulation, while the ones presented 
here also aim for causal understanding of toxicity in addition to targeting prediction.  
 
In a broader perspective, there are several immediate challenges where we need more 
work. These include which features to include when predicting toxicity? Minimal 
models may suffer from being less understandable from a mechanistic standpoint, 
whereas including too many features, as in the dream example above, could hamper 
the prediction capability of the model. Overall, a systems biology approach extends the 
feature space compared to classical pharmacokinetics, while an (algorithmic) 
information approach facilitates predictions in combination, being both scale invariant 
and parameter free. Hence there is a tension between predicitive capacity and 
mechanistic interpretability.  
 
Furthermore, overtraining and overfitting in solving high-dimensional and complex 
nonlinear problems such as toxicity prediction is one of the most common problems of 
existing machine learning methods. This originates from the need for estimating and


## Page 26


26
optimizing numerous hyper parameters. However, a method such as the relevance 
vector machine method solves this problem by incorporating Bayesian criteria into the 
learning process to reduce the irrelevant support vectors of the decision boundary in 
feature space, thus resulting in a sparser model[103]. Methods such as Random Forest 
classifiers are another category of successful methods in systems toxicology. They are 
one of the most robust algorithms and are able to identify the patterns important for the 
preferred class, even when there is a large imbalance in the class distribution within 
the training dataset [104]. Inspecting the results of the TOX21 data challenge 
demonstrates that a hybrid strategy which combines similarity scores for structural 
fingerprints and molecular descriptors (features) and machine-learning based 
prediction models can readily improve the accuracies of toxicity prediction [105]. In 
general, an ensemble model can be effective, since taking into account the prediction 
of other models can compensate for an incorrect prediction on the part of one of the 
individual methods. Certainly, each of the systems toxicology methods has intrinsic 
advantages, limitations, and practical constraints. Moreover, the performance of these 
methods depends on the structural diversity and representativeness of the molecules 
in the data set. Therefore, it is quite important to choose the most suitable machine 
learning method to develop the prediction model for a specific toxicity data set. Finally, 
the computational cost associated with each method is another practical and important 
factor determining the usability of a given method. 
In conclusion, beyond the above challenges and considerations, the grand remaining 
challenge is to advance the state-of-the-art towards personalized medicine. This 
requires patient specific predictions on toxicity, which in turn requires proper 
stratification of patients with regard to how they respond or not, with or without adverse 
toxic effects. This most likely requires integration of multiple layers of information as a


## Page 27


27
background upon which an individual has to be characterized/described, while a 
machinery for toxicity prediction has to be specific enough for a given patient, given 
the amount of (sparse) patient-specific information. This challenge and perspective will 
keep the field of data-driven computational toxicology busy. 
ACKNOWLEDGMENTS 
 We  thank the contributors to HotPPI,  Dr. Gordon Ball , Dr. David Gomez, Alireza Mazaheri  and 
Dr. Francesco Marabita. This study was supported by the Swedish ResearchCouncil ( J.T. & H. 
Z. ) and  Karolinska Institutet funds (N.K. ). The funders had no role in study design, data 
collection and analysis, decision to publish, or preparation of the manuscript.


## Page 28


28
REFERENCES 
1.  
Petrovska BB (2012) Historical review of medicinal plants’ usage. Pharmacogn Rev 6:1–5 . doi: 
10.4103/0973-7847.95849 
2.  
Hunter P (2008) A toxic brew we cannot live without. Micronutrients give insights into the interplay 
between geochemistry and evolutionary biology. EMBO Rep 9:15–8 . doi: 10.1038/sj.embor.7401148 
3.  
Bottini AA, Amcoff P, Hartung T (2007) Food for thought ... on globalisation of alternative methods. 
ALTEX 24:255–69 
4.  
Adeleye Y, Andersen M, Clewell R, Davies M, Dent M, Edwards S, Fowler P, Malcomber S, Nicol B, 
Scott A, Scott S, Sun B, Westmoreland C, White A, Zhang Q, Carmichael PL (2015) Implementing 
Toxicity Testing in the 21st Century (TT21C): Making safety decisions using toxicity pathways, and 
progress in a prototype risk assessment. Toxicology 332:102–111 . doi: 10.1016/j.tox.2014.02.007 
5.  
Pease W (1997) Toxic ignorance : the continuing absence of basic health testing for top-selling 
chemicals in the ... Diane Pub Co 
6.  
Mak IW, Evaniew N, Ghert M (2014) Lost in translation: animal models and clinical trials in cancer 
treatment. Am J Transl Res 6:114–8 
7.  
HANSCH C, MALONEY PP, FUJITA T, MUIR RM (1962) Correlation of Biological Activity of 
Phenoxyacetic Acids with Hammett Substituent Constants and Partition Coefficients. Nature 194:178–
180 . doi: 10.1038/194178b0 
8.  
Raies AB, Bajic VB (2016) In silico toxicology: computational methods for the prediction of chemical 
toxicity. Wiley Interdiscip Rev Comput Mol Sci 6:147–172 . doi: 10.1002/wcms.1240 
9.  
Lepoittevin J-P, Benezra C (1991) Allergic contact dermatitis caused by naturally occurring quinones. 
Pharm Weekbl Sci Ed 13:119–122 . doi: 10.1007/BF01981527 
10.  
Hewitt M, Enoch SJ, Madden JC, Przybylak KR, Cronin MTD (2013) Hepatotoxicity: A scheme for 
generating chemical categories for read-across, structural alerts and insights into mechanism(s) of action. 
Crit Rev Toxicol 43:537–558 . doi: 10.3109/10408444.2013.811215 
11.  
Gerner I, Barratt MD, Zinke S, Schlegel K, Schlede E (2004) Development and prevalidation of a list of 
structure-activity relationship rules to be used in expert systems for prediction of the skin-sensitising


## Page 29


29
properties of chemicals. Altern Lab Anim 32:487–509 
12.  
Milan C, Schifanella O, Roncaglioni A, Benfenati E (2011) Comparison and Possible Use of In Silico 
Tools for Carcinogenicity Within REACH Legislation. J Environ Sci Heal Part C 29:300–323 . doi: 
10.1080/10590501.2011.629973 
13.  
Ellison CM, Enoch SJ, Cronin MTD (2011) A review of the use of in silico methods to predict the 
chemistry of molecular initiating events related to drug toxicity. Expert Opin Drug Metab Toxicol 
7:1481–95 . doi: 10.1517/17425255.2011.629186 
14.  
Bhatia S, Schultz T, Roberts D, Shen J, Kromidas L, Marie Api A (2015) Comparison of Cramer 
classification between Toxtree, the OECD QSAR Toolbox and expert judgment. Regul Toxicol 
Pharmacol 71:52–62 . doi: 10.1016/j.yrtph.2014.11.005 
15.  
Hardy B, Douglas N, Helma C, Rautenberg M, Jeliazkova N, Jeliazkov V, Nikolova I, Benigni R, 
Tcheremenskaia O, Kramer S, Girschick T, Buchwald F, Wicker J, Karwath A, Gutlein M, Maunz A, 
Sarimveis H, Melagraki G, Afantitis A, Sopasakis P, Gallagher D, Poroikov V, Filimonov D, Zakharov 
A, Lagunin A, Gloriozova T, Novikov S, Skvortsova N, Druzhilovsky D, Chawla S, Ghosh I, Ray S, 
Patel H, Escher S (2010) Collaborative development of predictive toxicology applications. J 
Cheminform 2:7 . doi: 10.1186/1758-2946-2-7 
16.  
Gallegos-Saliner A, Poater A, Jeliazkova N, Patlewicz G, Worth AP (2008) Toxmatch—A chemical 
classification and activity prediction tool based on similarity measures. Regul Toxicol Pharmacol 52:77–
84 . doi: 10.1016/j.yrtph.2008.05.012 
17.  
Williams-DeVane CR, Wolf MA, Richard AM (2009) DSSTox chemical-index files for exposure-related 
experiments in ArrayExpress and Gene Expression Omnibus: enabling toxico-chemogenomics data 
linkages. Bioinformatics 25:692–694 . doi: 10.1093/bioinformatics/btp042 
18.  
Jeliazkova N, Jeliazkov V (2011) AMBIT RESTful web services: an implementation of the OpenTox 
application programming interface. J Cheminform 3:18 . doi: 10.1186/1758-2946-3-18 
19.  
Ait-Oudhia S, Zhang W, Mager DE (2017) A Mechanism-Based PK/PD Model for Hematological 
Toxicities Induced by Antibody-Drug Conjugates. AAPS J 19:1436–1448 . doi: 10.1208/s12248-017-
0113-5 
20.  
Caldwell GW, Yan Z, Tang W, Dasgupta M, Hasting B (2009) ADME optimization and toxicity


## Page 30


30
assessment in early- and late-phase drug discovery. Curr Top Med Chem 9:965–80 
21.  
Mager DE, Wyska E, Jusko WJ (2003) Diversity of mechanism-based pharmacodynamic models. Drug 
Metab Dispos 31:510–8 
22.  
Krewski D, Acosta D, Andersen M, Anderson H, Bailar JC, Boekelheide K, Brent R, Charnley G, 
Cheung VG, Green S, Kelsey KT, Kerkvliet NI, Li AA, McCray L, Meyer O, Patterson RD, Pennie W, 
Scala RA, Solomon GM, Stephens M, Yager J, Zeise L, Staff of Committee on Toxicity Test (2010) 
Toxicity Testing in the 21st Century: A Vision and a Strategy. J Toxicol Environ Heal Part B 13:51–138 
. doi: 10.1080/10937404.2010.483176 
23.  
Tegnér JN, Compte A, Auffray C, An G, Cedersund G, Clermont G, Gutkin B, Oltvai ZN, Stephan K, 
Thomas R, Villoslada P (2009) Computational disease modeling – fact or fiction? BMC Syst Biol 3:56 . 
doi: 10.1186/1752-0509-3-56 
24.  
Tegnér J, Zenil H, Kiani NA, Ball G, Gomez-Cabrero D (2016) A perspective on bridging scales and 
design of models using low-dimensional manifolds and data-driven model inference. Philos Trans A 
Math Phys Eng Sci 374:20160144 . doi: 10.1098/rsta.2016.0144 
25.  
Blankenburg M, Haberland L, Elvers H-D, Tannert C, Jandrig B (2009) High-Throughput Omics 
Technologies: Potential Tools for the Investigation of Influences of EMF on Biological Systems. Curr 
Genomics 10:86–92 . doi: 10.2174/138920209787847050 
26.  
Lam F, Ma C, Clifford B, Johnson CL, Liang Z-P (2016) High-resolution 1 H-MRSI of the brain using 
SPICE: Data acquisition and image reconstruction. Magn Reson Med 76:1059–1070 . doi: 
10.1002/mrm.26019 
27.  
Chapman T (2003) Lab automation and robotics: Automation on the move. Nature 421:661–666 . doi: 
10.1038/421661a 
28.  
Butte AJ, Ohno-Machado L (2013) Making it personal: translational bioinformatics. J Am Med Inform 
Assoc 20:595–6 . doi: 10.1136/amiajnl-2013-002028 
29.  
Kitano H (2002) Systems Biology: A Brief Overview. Science (80- ) 295:1662–1664 . doi: 
10.1126/science.1069492 
30.  
Plant NJ, Vinken M, Kolodkin A, Boogerd FC, Al. E, Borisy AA (2015) An introduction to systems 
toxicology. Toxicol Res 4:9–22 . doi: 10.1039/C4TX00058G


## Page 31


31
31.  
Bouhifd M, Hogberg HT, Kleensang A, Maertens A, Zhao L, Hartung T (2014) Mapping the Human 
Toxome by Systems Toxicology. Basic Clin Pharmacol Toxicol 115:24–31 . doi: 10.1111/bcpt.12198 
32.  
Flecknell P (2002) Replacement, reduction and refinement. ALTEX 19:73–8 
33.  
Hartung T (2010) Lessons Learned from Alternative Methods and their Validation for a New Toxicology 
in the 21st Century. J Toxicol Environ Heal Part B 13:277–290 . doi: 10.1080/10937404.2010.483945 
34.  
Guryanova S, Guryanova A (2017) sbv IMPROVER: Modern Approach to Systems Biology. In: 
Methods in molecular biology (Clifton, N.J.). pp 21–29 
35.  
Kiani NA, Shang M-M, Tegner J (2016) Systems Toxicology: Systematic Approach to Predict Toxicity. 
Curr Pharm Des 22:6911–6917 . doi: 10.2174/1381612822666161003115629 
36.  
Kiani NA, Zenil H, Olczak J, Tegnér J (2016) Evaluating network inference methods in terms of their 
ability to preserve the topology and complexity of genetic networks. Semin Cell Dev Biol 51:44–52 . 
doi: 10.1016/j.semcdb.2016.01.012 
37.  
Danhof M (2016) Systems pharmacology – Towards the modeling of network interactions. Eur J Pharm 
Sci 94:4–14 . doi: 10.1016/j.ejps.2016.04.027 
38.  
Arrell DK, Terzic A (2010) Network Systems Biology for Drug Discovery. Clin Pharmacol Ther 
88:120–125 . doi: 10.1038/clpt.2010.91 
39.  
Csermely P, Korcsm??ros T, Kiss HJM, London G, Nussinov R (2013) Structure and dynamics of 
molecular networks: A novel paradigm of drug discovery: A comprehensive review. Pharmacol. Ther. 
138:333–408 
40.  
Knight-Schrijver VR, Chelliah V, Cucurull-Sanchez L, Le Novère N (2016) The promises of quantitative 
systems pharmacology modelling for drug development. Comput Struct Biotechnol J 14:363–370 . doi: 
10.1016/j.csbj.2016.09.002 
41.  
Ding H, Takigawa I, Mamitsuka H, Zhu S (2014) Similarity-based machine learning methods for 
predicting drug–target interactions: a brief review. Brief Bioinform 15:734–747 . doi: 
10.1093/bib/bbt056 
42.  
Hopkins AL (2009) Drug discovery: Predicting promiscuity. Nature 462:167–168 . doi: 
10.1038/462167a


## Page 32


32
43.  
Lounkine E, Keiser MJ, Whitebread S, Mikhailov D, Hamon J, Jenkins JL, Lavan P, Weber E, Doak 
AK, Côté S, Shoichet BK, Urban L (2012) Large-scale prediction and testing of drug activity on side-
effect targets. Nature 486:361–7 . doi: 10.1038/nature11159 
44.  
Pauwels E, Stoven V, Yamanishi Y (2011) Predicting drug side-effect profiles: a chemical fragment-
based approach. BMC Bioinformatics 12:169 . doi: 10.1186/1471-2105-12-169 
45.  
Wang F, Zhang P, Cao N, Hu J, Sorrentino R (2014) Exploring the associations between drug side-
effects and therapeutic indications. J Biomed Inform 51:15–23 . doi: 10.1016/j.jbi.2014.03.014 
46.  
Barneh F, Jafari M, Mirzaie M (2015) Updates on drug–target network; facilitating polypharmacology 
and data integration by growth of DrugBank database. Brief Bioinform 17:bbv094 . doi: 
10.1093/bib/bbv094 
47.  
Campbell SJ, Gaulton A, Marshall J, Bichko D, Martin S, Brouwer C, Harland L (2012) Visualizing the 
drug target landscape. Drug Discov Today 17:S3–S15 . doi: 10.1016/j.drudis.2011.12.005 
48.  
Swamidass SJ (2011) Mining small-molecule screens to repurpose drugs. Brief Bioinform 12:327–335 . 
doi: 10.1093/bib/bbr028 
49.  
Moriaud F, Richard SB, Adcock SA, Chanas-Martin L, Surgand J-S, Ben Jelloul M, Delfaud F (2011) 
Identify drug repurposing candidates by mining the Protein Data Bank. Brief Bioinform 12:336–340 . 
doi: 10.1093/bib/bbr017 
50.  
Dobson CM (2004) Chemical space and biology. Nature 432:824–8 . doi: 10.1038/nature03192 
51.  
Vogt I, Mestres J (2010) Drug-Target Networks. Mol Inform 29:10–14 . doi: 10.1002/minf.200900069 
52.  
Forli S, Huey R, Pique ME, Sanner MF, Goodsell DS, Olson AJ (2016) Computational protein–ligand 
docking and virtual drug screening with the AutoDock suite. Nat Protoc 11:905–919 . doi: 
10.1038/nprot.2016.051 
53.  
Xie L, Wang J, Bourne PE (2007) In silico elucidation of the molecular mechanism defining the adverse 
effect of selective estrogen receptor modulators. PLoS Comput Biol 3:2324–2332 . doi: 
10.1371/journal.pcbi.0030217 
54.  
Halperin I, Ma B, Wolfson H, Nussinov R (2002) Principles of docking: An overview of search 
algorithms and a guide to scoring functions. Proteins 47:409–43 . doi: 10.1002/prot.10115


## Page 33


33
55.  
Shoichet BK, McGovern SL, Wei B, Irwin JJ (2002) Lead discovery using molecular docking. Curr 
Opin Chem Biol 6:439–46 
56.  
Cheng AC, Coleman RG, Smyth KT, Cao Q, Soulard P, Caffrey DR, Salzberg AC, Huang ES (2007) 
Structure-based maximal affinity model predicts small-molecule druggability. Nat Biotechnol 25:71–5 . 
doi: 10.1038/nbt1273 
57.  
Wallach I, Jaitly N, Lilien R (2010) A structure-based approach for mapping adverse drug reactions to 
the perturbation of underlying biological pathways. PLoS One 5:e12063 . doi: 
10.1371/journal.pone.0012063 
58.  
Huey R, Morris GM, Olson AJ, Goodsell DS (2007) A semiempirical free energy force field with 
charge-based desolvation. J Comput Chem 28:1145–52 . doi: 10.1002/jcc.20634 
59.  
Xia Z, Wu L-Y, Zhou X, Wong ST (2010) Semi-supervised drug-protein interaction prediction from 
heterogeneous biological spaces. BMC Syst Biol 4:S6 . doi: 10.1186/1752-0509-4-S2-S6 
60.  
van Laarhoven T, Nabuurs SB, Marchiori E (2011) Gaussian interaction profile kernels for predicting 
drug–target interaction. Bioinformatics 27:3036–3043 . doi: 10.1093/bioinformatics/btr500 
61.  
Yabuuchi H, Niijima S, Takematsu H, Ida T, Hirokawa T, Hara T, Ogawa T, Minowa Y, Tsujimoto G, 
Okuno Y (2014) Analysis of multiple compound-protein interactions reveals novel bioactive molecules. 
Mol Syst Biol 7:472–472 . doi: 10.1038/msb.2011.5 
62.  
Perlman L, Gottlieb A, Atias N, Ruppin E, Sharan R (2011) Combining drug and gene similarity 
measures for drug-target elucidation. J Comput Biol 18:133–45 . doi: 10.1089/cmb.2010.0213 
63.  
Yamanishi Y, Pauwels E, Kotera M (2012) Drug side-effect prediction based on the integration of 
chemical and biological spaces. J Chem Inf Model 52:3284–3292 . doi: 10.1021/ci2005548 
64.  
Cobanoglu MC, Liu C, Hu F, Oltvai ZN, Bahar I (2013) Predicting drug-target interactions using 
probabilistic matrix factorization. J Chem Inf Model 53:3399–3409 . doi: 10.1021/ci400219z 
65.  
Mayr A, Klambauer G, Unterthiner T, Hochreiter S (2016) DeepTox: Toxicity Prediction using Deep 
Learning. Front Environ Sci 3:80 . doi: 10.3389/fenvs.2015.00080 
66.  
Min S, Lee B, Yoon S (2016) Deep learning in bioinformatics. Brief Bioinform bbw068 . doi: 
10.1093/bib/bbw068


## Page 34


34
67.  
LeCun Y, Bengio Y, Hinton G (2015) Deep learning. Nature 521:436–444 . doi: 10.1038/nature14539 
68.  
Baldi P, Sadowski P, Whiteson D (2014) Searching for exotic particles in high-energy physics with deep 
learning. Nat Commun 5:ncomms5308 . doi: 10.1038/ncomms5308 
69.  
Esteva A, Kuprel B, Novoa RA, Ko J, Swetter SM, Blau HM, Thrun S (2017) Dermatologist-level 
classification of skin cancer with deep neural networks. Nature 542:115–118 . doi: 10.1038/nature21056 
70.  
Wu Y, Schuster M, Chen Z, Le Q V., Norouzi M, Macherey W, Krikun M, Cao Y, Gao Q, Macherey K, 
Klingner J, Shah A, Johnson M, Liu X, Kaiser Ł, Gouws S, Kato Y, Kudo T, Kazawa H, Stevens K, 
Kurian G, Patil N, Wang W, Young C, Smith J, Riesa J, Rudnick A, Vinyals O, Corrado G, Hughes M, 
Dean J (2016) Google’s Neural Machine Translation System: Bridging the Gap between Human and 
Machine Translation 
71.  
Ma’ayan A, Jenkins SL, Goldfarb J, Iyengar R (2007) Network analysis of FDA approved drugs and 
their targets. Mt Sinai J Med A J Transl Pers Med 74:27–32 . doi: 10.1002/msj.20002 
72.  
Lin H-H, Zhang L-L, Yan R, Lu J-J, Hu Y (2017) Network Analysis of Drug-target Interactions: A 
Study on FDA-approved New Molecular Entities Between 2000 to 2015. Sci Rep 7:12230 . doi: 
10.1038/s41598-017-12061-8 
73.  
Kiani NA, Zenil H, Olczak J, Tegnér J (2016) Evaluating network inference methods in terms of their 
ability to preserve the topology and complexity of genetic networks. Semin. Cell Dev. Biol. 51:44–52 
74.  
McGary KL, Park TJ, Woods JO, Cha HJ, Wallingford JB, Marcotte EM (2010) Systematic discovery of 
nonobvious human disease models through orthologous phenotypes. Proc Natl Acad Sci 107:6544–6549 
. doi: 10.1073/pnas.0910200107 
75.  
Korcsmáros T, Szalay MS, Rovó P, Palotai R, Fazekas D, Lenti K, Farkas IJ, Csermely P, Vellai T 
(2011) Signalogs: Orthology-Based Identification of Novel Signaling Pathway Components in Three 
Metazoans. PLoS One 6:e19240 . doi: 10.1371/journal.pone.0019240 
76.  
Garcia-Serna R, Vidal D, Remez N, Mestres J (2015) Large-Scale Predictive Drug Safety: From 
Structural Alerts to Biological Mechanisms. Chem Res Toxicol 28:1875–1887 . doi: 
10.1021/acs.chemrestox.5b00260 
77.  
Remez N, Garcia-Serna R, Vidal D, Mestres J (2016) The in Vitro Pharmacological Profile of Drugs as a 
Proxy Indicator of Potential in Vivo Organ Toxicities. Chem Res Toxicol 29:637–648 . doi:


## Page 35


35
10.1021/acs.chemrestox.5b00470 
78.  
Kuhn M, Al Banchaabouchi M, Campillos M, Jensen LJ, Gross C, Gavin A-C, Bork P (2014) Systematic 
identification of proteins that elicit drug side effects. Mol Syst Biol 9:663–663 . doi: 
10.1038/msb.2013.10 
79.  
Yildirim MA, Goh K-I, Cusick ME, Barabási A-L, Vidal M (2007) Drug-target network. Nat Biotechnol 
25:1119–26 . doi: 10.1038/nbt1338 
80.  
Luo H, Chen J, Shi L, Mikailov M, Zhu H, Wang K, He L, Yang L (2011) DRAR-CPI: a server for 
identifying drug repositioning potential and adverse drug reactions via the chemical-protein interactome. 
Nucleic Acids Res 39:W492-8 . doi: 10.1093/nar/gkr299 
81.  
Daminelli S, Haupt VJ, Reimann M, Schroeder M (2012) Drug repositioning through incomplete bi-
cliques in an integrated drug-target-disease network. Integr Biol (Camb) 4:778–88 . doi: 
10.1039/c2ib00154c 
82.  
Gottlieb A, Stein GY, Ruppin E, Sharan R (2014) PREDICT: a method for inferring novel drug 
indications with application to personalized medicine. Mol Syst Biol 7:496–496 . doi: 
10.1038/msb.2011.26 
83.  
Lee H, Bae T, Lee J-H, Kim D, Oh Y, Jang Y, Kim J-T, Lee J-J, Innocenti A, Supuran CT, Chen L, Rho 
K, Kim S (2012) Rational drug repositioning guided by an integrated pharmacological network of 
protein, disease and drug. BMC Syst Biol 6:80 . doi: 10.1186/1752-0509-6-80 
84.  
Zhao S, Li S (2012) A co-module approach for elucidating drug–disease associations and revealing their 
molecular basis. Bioinformatics 28:955–961 . doi: 10.1093/bioinformatics/bts057 
85.  
Guney E, Garcia-Garcia J, Oliva B (2014) GUILDify: a web server for phenotypic characterization of 
genes through biological data integration and network-based prioritization algorithms. Bioinformatics 
30:1789–90 . doi: 10.1093/bioinformatics/btu092 
86.  
Guney E, Menche J, Vidal M, Barábasi A-L (2016) Network-based in silico drug efficacy screening. Nat 
Commun 7:10331 . doi: 10.1038/ncomms10331 
87.  
Cami A, Arnold A, Manzi S, Reis B (2011) Predicting Adverse Drug Events Using Pharmacological 
Network Models. Sci Transl Med 3:114ra127-114ra127 . doi: 10.1126/scitranslmed.3002774 
88.  
Brouwers L, Iskar M, Zeller G, van Noort V, Bork P (2011) Network neighbors of drug targets


## Page 36


36
contribute to drug side-effect similarity. PLoS One 6:e22187 . doi: 10.1371/journal.pone.0022187 
89.  
Gottlieb A, Altman RB (2014) Integrating Systems Biology Sources Illuminates Drug Action. Clin 
Pharmacol Ther 95:1–7 . doi: 10.1038/clpt.2014.51 
90.  
Fan S, Geng Q, Pan Z, Li X, Tie L, Pan Y, Li X (2012) Clarifying off-target effects for torcetrapib using 
network pharmacology and reverse docking approach. BMC Syst Biol 6:152 . doi: 10.1186/1752-0509-
6-152 
91.  
Azuaje FJ, Zhang L, Devaux Y, Wagner DR (2011) Drug-target network in myocardial infarction 
reveals multiple side effects of unrelated drugs. Sci Rep 1:1–10 . doi: 10.1038/srep00052 
92.  
Huang LC, Wu X, Chen JY (2013) Predicting adverse drug reaction profiles by integrating protein 
interaction networks with drug structures. Proteomics 13:313–324 . doi: 10.1002/pmic.201200337 
93.  
Huang J, Niu C, Green CD, Yang L, Mei H, Han JDJ (2013) Systematic Prediction of Pharmacodynamic 
Drug-Drug Interactions through Protein-Protein-Interaction Network. PLoS Comput Biol 9:e1002998 . 
doi: 10.1371/journal.pcbi.1002998 
94.  
Pouliot Y, Chiang AP, Butte AJ (2011) Predicting adverse drug reactions using publicly available 
PubChem BioAssay data. Clin Pharmacol Ther 90:90–99 . doi: 10.1038/clpt.2011.81 
95.  
Iskar M, Zeller G, Zhao XM, van Noort V, Bork P (2012) Drug discovery in the age of systems biology: 
The rise of computational approaches for data integration. Curr. Opin. Biotechnol. 23:609–616 
96.  
Bai JPF, Abernethy DR (2013) Systems pharmacology to predict drug toxicity: integration across levels 
of biological organization. Annu Rev Pharmacol Toxicol 53:451–73 . doi: 10.1146/annurev-pharmtox-
011112-140248 
97.  
Rahmani H, Weiss G, Méndez-Lucio O, Bender A (2016) ARWAR: A network approach for predicting 
Adverse Drug Reactions. Comput Biol Med 68:101–108 . doi: 10.1016/j.compbiomed.2015.11.005 
98.  
Dorel M, Barillot E, Zinovyev A, Kuperstein I (2015) Network-based approaches for drug response 
prediction and targeted therapy development in cancer. Biochem. Biophys. Res. Commun. 464:386–391 
99.  
Pujol A, Mosca R, Farr??s J, Aloy P (2010) Unveiling the role of network and systems biology in drug 
discovery. Trends Pharmacol. Sci. 31:115–123 
100.  
Mucha PJ, Richardson T, Macon K, Porter MA, Onnela J-P (2010) Community structure in time-


## Page 37


37
dependent, multiscale, and multiplex networks. Science 328:876–8 . doi: 10.1126/science.1184819 
101.  
Zenil H, Kiani NA, Tegnér J (2016) Methods of information theory and algorithmic complexity for 
network biology. Semin Cell Dev Biol 51:32–43 . doi: 10.1016/j.semcdb.2016.01.011 
102.  
Zenil H, Hernández-Orozco S, Kiani NA, Soler-Toscano F, Rueda-Toicen A (2016) A Decomposition 
Method for Global Evaluation of Shannon Entropy and Local Estimations of Algorithmic Complexity 
103.  
Burden FR, Winkler DA (2015) Relevance Vector Machines: Sparse Classification Methods for QSAR. 
J Chem Inf Model 55:1529–1534 . doi: 10.1021/acs.jcim.5b00261 
104.  
Vladimir Svetnik, Andy Liaw, Christopher Tong, J. Christopher Culberso, Robert P. Sheridan and, 
Feuston‡ BP (2003) Random Forest:  A Classification and Regression Tool for Compound Classification 
and QSAR Modeling. doi: 10.1021/CI034160G 
105.  
Lei T, Li Y, Song Y, Li D, Sun H, Hou T (2016) ADMET evaluation in drug discovery: 15. Accurate 
prediction of rat oral acute toxicity using relevance vector machine and consensus modeling. J 
Cheminform 8:6 . doi: 10.1186/s13321-016-0117-7

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]